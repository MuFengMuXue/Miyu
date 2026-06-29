dbus-transport-socket.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-transport-socket.c Socket subclasses of DBusTransport

3 \*

4 \* Copyright (C) 2002, 2003, 2004, 2006 Red Hat Inc.

5 \*

6 \* SPDX-License-Identifier: AFL-2.1 OR GPL-2.0-or-later

7 \*

8 \* Licensed under the Academic Free License version 2.1

9 \*

10 \* This program is free software; you can redistribute it and/or modify

11 \* it under the terms of the GNU General Public License as published by

12 \* the Free Software Foundation; either version 2 of the License, or

13 \* (at your option) any later version.

14 \*

15 \* This program is distributed in the hope that it will be useful,

16 \* but WITHOUT ANY WARRANTY; without even the implied warranty of

17 \* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the

18 \* GNU General Public License for more details.

19 \*

20 \* You should have received a copy of the GNU General Public License

21 \* along with this program; if not, write to the Free Software

22 \* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

23 \*

24 \*/

25

26\#include \<config.h\>

27

28\#include \<stdio.h\>

29

30\#include "dbus-internals.h"

31\#include "dbus-connection-internal.h"

32\#include "dbus-nonce.h"

33\#include "dbus-transport-socket.h"

34\#include "dbus-transport-protected.h"

35\#include "dbus-watch.h"

36\#include "dbus-credentials.h"

37

49typedef struct DBusTransportSocket DBusTransportSocket;

50

54struct DBusTransportSocket

55{

56 DBusTransport base;

57 DBusSocket fd;

58 DBusWatch \*read_watch;

59 DBusWatch \*write_watch;

61 int max_bytes_read_per_iteration;

62 int max_bytes_written_per_iteration;

64 int message_bytes_written;

68 DBusString encoded_outgoing;

71 DBusString encoded_incoming;

74};

75

76static void

77free_watches (DBusTransport \*transport)

78{

79 DBusTransportSocket \*socket_transport = (DBusTransportSocket\*) transport;

80

81 \_dbus_verbose ("start\n");

82

83 if (socket_transport-\>read_watch)

84 {

85 if (transport-\>connection)

86 \_dbus_connection_remove_watch_unlocked (transport-\>connection,

87 socket_transport-\>read_watch);

88 \_dbus_watch_invalidate (socket_transport-\>read_watch);

89 \_dbus_watch_unref (socket_transport-\>read_watch);

90 socket_transport-\>read_watch = NULL;

91 }

92

93 if (socket_transport-\>write_watch)

94 {

95 if (transport-\>connection)

96 \_dbus_connection_remove_watch_unlocked (transport-\>connection,

97 socket_transport-\>write_watch);

98 \_dbus_watch_invalidate (socket_transport-\>write_watch);

99 \_dbus_watch_unref (socket_transport-\>write_watch);

100 socket_transport-\>write_watch = NULL;

101 }

102

103 \_dbus_verbose ("end\n");

104}

105

106static void

107socket_finalize (DBusTransport \*transport)

108{

109 DBusTransportSocket \*socket_transport = (DBusTransportSocket\*) transport;

110

111 \_dbus_verbose ("\n");

112

113 free_watches (transport);

114

115 \_dbus_string_free (&socket_transport-\>encoded_outgoing);

116 \_dbus_string_free (&socket_transport-\>encoded_incoming);

117

118 \_dbus_transport_finalize_base (transport);

119

120 \_dbus_assert (socket_transport-\>read_watch == NULL);

121 \_dbus_assert (socket_transport-\>write_watch == NULL);

122

123 dbus_free (transport);

124}

125

126static void

127check_write_watch (DBusTransport \*transport)

128{

129 DBusTransportSocket \*socket_transport = (DBusTransportSocket\*) transport;

130 dbus_bool_t needed;

131

132 if (transport-\>connection == NULL)

133 return;

134

135 if (transport-\>disconnected)

136 {

137 \_dbus_assert (socket_transport-\>write_watch == NULL);

138 return;

139 }

140

141 \_dbus_transport_ref (transport);

142

143 if (\_dbus_transport_try_to_authenticate (transport))

144 needed = \_dbus_connection_has_messages_to_send_unlocked (transport-\>connection);

145 else

146 {

147 if (transport-\>send_credentials_pending)

148 needed = TRUE;

149 else

150 {

151 DBusAuthState auth_state;

152

153 auth_state = \_dbus_auth_do_work (transport-\>auth);

154

155 /\* If we need memory we install the write watch just in case,

156 \* if there's no need for it, it will get de-installed

157 \* next time we try reading.

158 \*/

159 if (auth_state == DBUS_AUTH_STATE_HAVE_BYTES_TO_SEND \|\|

160 auth_state == DBUS_AUTH_STATE_WAITING_FOR_MEMORY)

161 needed = TRUE;

162 else

163 needed = FALSE;

164 }

165 }

166

167 \_dbus_verbose ("check_write_watch(): needed = %d on connection %p watch %p fd = %" DBUS_SOCKET_FORMAT " outgoing messages exist %d\n",

168 needed, transport-\>connection, socket_transport-\>write_watch,

169 \_dbus_socket_printable (socket_transport-\>fd),

170 \_dbus_connection_has_messages_to_send_unlocked (transport-\>connection));

171

172 \_dbus_connection_toggle_watch_unlocked (transport-\>connection,

173 socket_transport-\>write_watch,

174 needed);

175

176 \_dbus_transport_unref (transport);

177}

178

179static void

180check_read_watch (DBusTransport \*transport)

181{

182 DBusTransportSocket \*socket_transport = (DBusTransportSocket\*) transport;

183 dbus_bool_t need_read_watch;

184

185 \_dbus_verbose ("fd = %" DBUS_SOCKET_FORMAT "\n",

186 \_dbus_socket_printable (socket_transport-\>fd));

187

188 if (transport-\>connection == NULL)

189 return;

190

191 if (transport-\>disconnected)

192 {

193 \_dbus_assert (socket_transport-\>read_watch == NULL);

194 return;

195 }

196

197 \_dbus_transport_ref (transport);

198

199 if (\_dbus_transport_try_to_authenticate (transport))

200 need_read_watch =

201 (\_dbus_counter_get_size_value (transport-\>live_messages) \< transport-\>max_live_messages_size) &&

202 (\_dbus_counter_get_unix_fd_value (transport-\>live_messages) \< transport-\>max_live_messages_unix_fds);

203 else

204 {

205 if (transport-\>receive_credentials_pending)

206 need_read_watch = TRUE;

207 else

208 {

209 /\* The reason to disable need_read_watch when not WAITING_FOR_INPUT

210 \* is to avoid spinning on the file descriptor when we're waiting

211 \* to write or for some other part of the auth process

212 \*/

213 DBusAuthState auth_state;

214

215 auth_state = \_dbus_auth_do_work (transport-\>auth);

216

217 /\* If we need memory we install the read watch just in case,

218 \* if there's no need for it, it will get de-installed

219 \* next time we try reading. If we're authenticated we

220 \* install it since we normally have it installed while

221 \* authenticated.

222 \*/

223 if (auth_state == DBUS_AUTH_STATE_WAITING_FOR_INPUT \|\|

224 auth_state == DBUS_AUTH_STATE_WAITING_FOR_MEMORY \|\|

225 auth_state == DBUS_AUTH_STATE_AUTHENTICATED)

226 need_read_watch = TRUE;

227 else

228 need_read_watch = FALSE;

229 }

230 }

231

232 \_dbus_verbose (" setting read watch enabled = %d\n", need_read_watch);

233 \_dbus_connection_toggle_watch_unlocked (transport-\>connection,

234 socket_transport-\>read_watch,

235 need_read_watch);

236

237 \_dbus_transport_unref (transport);

238}

239

240static void

241do_io_error (DBusTransport \*transport)

242{

243 \_dbus_transport_ref (transport);

244 \_dbus_transport_disconnect (transport);

245 \_dbus_transport_unref (transport);

246}

247

248/\* return value is whether we successfully read any new data. \*/

249static dbus_bool_t

250read_data_into_auth (DBusTransport \*transport,

251 dbus_bool_t \*oom)

252{

253 DBusTransportSocket \*socket_transport = (DBusTransportSocket\*) transport;

254 DBusString \*buffer;

255 int bytes_read;

256 int saved_errno;

257

258 \*oom = FALSE;

259

260 \_dbus_auth_get_buffer (transport-\>auth, &buffer);

261

262 bytes_read = \_dbus_read_socket (socket_transport-\>fd,

263 buffer, socket_transport-\>max_bytes_read_per_iteration);

264 saved_errno = \_dbus_save_socket_errno ();

265

266 \_dbus_auth_return_buffer (transport-\>auth, buffer);

267

268 if (bytes_read \> 0)

269 {

270 \_dbus_verbose (" read %d bytes in auth phase\n", bytes_read);

271

272 return TRUE;

273 }

274 else if (bytes_read \< 0)

275 {

276 /\* EINTR already handled for us \*/

277

278 if (\_dbus_get_is_errno_enomem (saved_errno))

279 {

280 \*oom = TRUE;

281 }

282 else if (\_dbus_get_is_errno_eagain_or_ewouldblock (saved_errno))

283 ; /\* do nothing, just return FALSE below \*/

284 else

285 {

286 \_dbus_verbose ("Error reading from remote app: %s\n",

287 \_dbus_strerror (saved_errno));

288 do_io_error (transport);

289 }

290

291 return FALSE;

292 }

293 else

294 {

295 \_dbus_assert (bytes_read == 0);

296

297 \_dbus_verbose ("Disconnected from remote app\n");

298 do_io_error (transport);

299

300 return FALSE;

301 }

302}

303

304/\* Return value is whether we successfully wrote any bytes \*/

305static dbus_bool_t

306write_data_from_auth (DBusTransport \*transport)

307{

308 DBusTransportSocket \*socket_transport = (DBusTransportSocket\*) transport;

309 int bytes_written;

310 int saved_errno;

311 const DBusString \*buffer;

312

313 if (!\_dbus_auth_get_bytes_to_send (transport-\>auth,

314 &buffer))

315 return FALSE;

316

317 bytes_written = \_dbus_write_socket (socket_transport-\>fd,

318 buffer,

319 0, \_dbus_string_get_length (buffer));

320 saved_errno = \_dbus_save_socket_errno ();

321

322 if (bytes_written \> 0)

323 {

324 \_dbus_auth_bytes_sent (transport-\>auth, bytes_written);

325 return TRUE;

326 }

327 else if (bytes_written \< 0)

328 {

329 /\* EINTR already handled for us \*/

330

331 if (\_dbus_get_is_errno_eagain_or_ewouldblock (saved_errno))

332 ;

333 else

334 {

335 \_dbus_verbose ("Error writing to remote app: %s\n",

336 \_dbus_strerror (saved_errno));

337 do_io_error (transport);

338 }

339 }

340

341 return FALSE;

342}

343

344/\* FALSE on OOM \*/

345static dbus_bool_t

346exchange_credentials (DBusTransport \*transport,

347 dbus_bool_t do_reading,

348 dbus_bool_t do_writing)

349{

350 DBusTransportSocket \*socket_transport = (DBusTransportSocket\*) transport;

351 DBusError error = DBUS_ERROR_INIT;

352

353 \_dbus_verbose ("exchange_credentials: do_reading = %d, do_writing = %d\n",

354 do_reading, do_writing);

355

356 if (do_writing && transport-\>send_credentials_pending)

357 {

358 if (\_dbus_send_credentials_socket (socket_transport-\>fd,

359 &error))

360 {

361 transport-\>send_credentials_pending = FALSE;

362 }

363 else

364 {

365 \_dbus_verbose ("Failed to write credentials: %s\n", error.message);

366 dbus_error_free (&error);

367 do_io_error (transport);

368 }

369 }

370

371 if (do_reading && transport-\>receive_credentials_pending)

372 {

373 /\* FIXME this can fail due to IO error \_or\_ OOM, broken

374 \* (somewhat tricky to fix since the OOM error can be set after

375 \* we already read the credentials byte, so basically we need to

376 \* separate reading the byte and storing it in the

377 \* transport-\>credentials). Does not really matter for now

378 \* because storing in credentials never actually fails on unix.

379 \*/

380 if (\_dbus_read_credentials_socket (socket_transport-\>fd,

381 transport-\>credentials,

382 &error))

383 {

384 transport-\>receive_credentials_pending = FALSE;

385 }

386 else

387 {

388 \_dbus_verbose ("Failed to read credentials %s\n", error.message);

389 dbus_error_free (&error);

390 do_io_error (transport);

391 }

392 }

393

394 if (!(transport-\>send_credentials_pending \|\|

395 transport-\>receive_credentials_pending))

396 {

397 if (!\_dbus_auth_set_credentials (transport-\>auth,

398 transport-\>credentials))

399 return FALSE;

400 }

401

402 return TRUE;

403}

404

405static dbus_bool_t

406do_authentication (DBusTransport \*transport,

407 dbus_bool_t do_reading,

408 dbus_bool_t do_writing,

409 dbus_bool_t \*auth_completed)

410{

411 dbus_bool_t oom;

412 dbus_bool_t orig_auth_state;

413

414 oom = FALSE;

415

416 orig_auth_state = \_dbus_transport_try_to_authenticate (transport);

417

418 /\* This is essential to avoid the check_write_watch() at the end,

419 \* we don't want to add a write watch in do_iteration before

420 \* we try writing and get EAGAIN

421 \*/

422 if (orig_auth_state)

423 {

424 if (auth_completed)

425 \*auth_completed = FALSE;

426 return TRUE;

427 }

428

429 \_dbus_transport_ref (transport);

430

431 while (!\_dbus_transport_try_to_authenticate (transport) &&

432 \_dbus_transport_get_is_connected (transport))

433 {

434 if (!exchange_credentials (transport, do_reading, do_writing))

435 {

436 /\* OOM \*/

437 oom = TRUE;

438 goto out;

439 }

440

441 if (transport-\>send_credentials_pending \|\|

442 transport-\>receive_credentials_pending)

443 {

444 \_dbus_verbose ("send_credentials_pending = %d receive_credentials_pending = %d\n",

445 transport-\>send_credentials_pending,

446 transport-\>receive_credentials_pending);

447 goto out;

448 }

449

450\#define TRANSPORT_SIDE(t) ((t)-\>is_server ? "server" : "client")

451 switch (\_dbus_auth_do_work (transport-\>auth))

452 {

453 case DBUS_AUTH_STATE_WAITING_FOR_INPUT:

454 \_dbus_verbose (" %s auth state: waiting for input\n",

455 TRANSPORT_SIDE (transport));

456 if (!do_reading \|\| !read_data_into_auth (transport, &oom))

457 goto out;

458 break;

459

460 case DBUS_AUTH_STATE_WAITING_FOR_MEMORY:

461 \_dbus_verbose (" %s auth state: waiting for memory\n",

462 TRANSPORT_SIDE (transport));

463 oom = TRUE;

464 goto out;

465 break;

466

467 case DBUS_AUTH_STATE_HAVE_BYTES_TO_SEND:

468 \_dbus_verbose (" %s auth state: bytes to send\n",

469 TRANSPORT_SIDE (transport));

470 if (!do_writing \|\| !write_data_from_auth (transport))

471 goto out;

472 break;

473

474 case DBUS_AUTH_STATE_NEED_DISCONNECT:

475 \_dbus_verbose (" %s auth state: need to disconnect\n",

476 TRANSPORT_SIDE (transport));

477 do_io_error (transport);

478 break;

479

480 case DBUS_AUTH_STATE_AUTHENTICATED:

481 \_dbus_verbose (" %s auth state: authenticated\n",

482 TRANSPORT_SIDE (transport));

483 break;

484

485 case DBUS_AUTH_STATE_INVALID:

486 /\* fall through \*/

487 default:

488 \_dbus_assert_not_reached ("invalid auth state");

489 }

490 }

491

492 out:

493 if (auth_completed)

494 \*auth_completed = (orig_auth_state != \_dbus_transport_try_to_authenticate (transport));

495

496 check_read_watch (transport);

497 check_write_watch (transport);

498 \_dbus_transport_unref (transport);

499

500 if (oom)

501 return FALSE;

502 else

503 return TRUE;

504}

505

506/\* returns false on oom \*/

507static dbus_bool_t

508do_writing (DBusTransport \*transport)

509{

510 int total;

511 DBusTransportSocket \*socket_transport = (DBusTransportSocket\*) transport;

512 dbus_bool_t oom;

513

514 /\* No messages without authentication! \*/

515 if (!\_dbus_transport_try_to_authenticate (transport))

516 {

517 \_dbus_verbose ("Not authenticated, not writing anything\n");

518 return TRUE;

519 }

520

521 if (transport-\>disconnected)

522 {

523 \_dbus_verbose ("Not connected, not writing anything\n");

524 return TRUE;

525 }

526

527\#if 1

528 \_dbus_verbose ("do_writing(), have_messages = %d, fd = %" DBUS_SOCKET_FORMAT "\n",

529 \_dbus_connection_has_messages_to_send_unlocked (transport-\>connection),

530 \_dbus_socket_printable (socket_transport-\>fd));

531\#endif

532

533 oom = FALSE;

534 total = 0;

535

536 while (!transport-\>disconnected &&

537 \_dbus_connection_has_messages_to_send_unlocked (transport-\>connection))

538 {

539 int bytes_written;

540 DBusMessage \*message;

541 const DBusString \*header;

542 const DBusString \*body;

543 int header_len, body_len;

544 int total_bytes_to_write;

545 int saved_errno;

546

547 if (total \> socket_transport-\>max_bytes_written_per_iteration)

548 {

549 \_dbus_verbose ("%d bytes exceeds %d bytes written per iteration, returning\n",

550 total, socket_transport-\>max_bytes_written_per_iteration);

551 goto out;

552 }

553

554 message = \_dbus_connection_get_message_to_send (transport-\>connection);

555 \_dbus_assert (message != NULL);

556 dbus_message_lock (message);

557

558\#if 0

559 \_dbus_verbose ("writing message %p\n", message);

560\#endif

561

562 \_dbus_message_get_network_data (message,

563 &header, &body);

564

565 header_len = \_dbus_string_get_length (header);

566 body_len = \_dbus_string_get_length (body);

567

568 if (\_dbus_auth_needs_encoding (transport-\>auth))

569 {

570 /\* Does fd passing even make sense with encoded data? \*/

571 \_dbus_assert(!DBUS_TRANSPORT_CAN_SEND_UNIX_FD(transport));

572

573 if (\_dbus_string_get_length (&socket_transport-\>encoded_outgoing) == 0)

574 {

575 if (!\_dbus_auth_encode_data (transport-\>auth,

576 header, &socket_transport-\>encoded_outgoing))

577 {

578 oom = TRUE;

579 goto out;

580 }

581

582 if (!\_dbus_auth_encode_data (transport-\>auth,

583 body, &socket_transport-\>encoded_outgoing))

584 {

585 \_dbus_string_set_length (&socket_transport-\>encoded_outgoing, 0);

586 oom = TRUE;

587 goto out;

588 }

589 }

590

591 total_bytes_to_write = \_dbus_string_get_length (&socket_transport-\>encoded_outgoing);

592

593\#if 0

594 \_dbus_verbose ("encoded message is %d bytes\n",

595 total_bytes_to_write);

596\#endif

597

598 bytes_written =

599 \_dbus_write_socket (socket_transport-\>fd,

600 &socket_transport-\>encoded_outgoing,

601 socket_transport-\>message_bytes_written,

602 total_bytes_to_write - socket_transport-\>message_bytes_written);

603 saved_errno = \_dbus_save_socket_errno ();

604 }

605 else

606 {

607 total_bytes_to_write = header_len + body_len;

608

609\#if 0

610 \_dbus_verbose ("message is %d bytes\n",

611 total_bytes_to_write);

612\#endif

613

614\#ifdef HAVE_UNIX_FD_PASSING

615 if (socket_transport-\>message_bytes_written \<= 0 && DBUS_TRANSPORT_CAN_SEND_UNIX_FD(transport))

616 {

617 /\* Send the fds along with the first byte of the message \*/

618 const int \*unix_fds;

619 unsigned n;

620

621 \_dbus_message_get_unix_fds(message, &unix_fds, &n);

622

623 bytes_written =

624 \_dbus_write_socket_with_unix_fds_two (socket_transport-\>fd,

625 header,

626 socket_transport-\>message_bytes_written,

627 header_len - socket_transport-\>message_bytes_written,

628 body,

629 0, body_len,

630 unix_fds,

631 n);

632 saved_errno = \_dbus_save_socket_errno ();

633

634 if (bytes_written \> 0 && n \> 0)

635 \_dbus_verbose("Wrote %i unix fds\n", n);

636 }

637 else

638\#endif

639 {

640 if (socket_transport-\>message_bytes_written \< header_len)

641 {

642 bytes_written =

643 \_dbus_write_socket_two (socket_transport-\>fd,

644 header,

645 socket_transport-\>message_bytes_written,

646 header_len - socket_transport-\>message_bytes_written,

647 body,

648 0, body_len);

649 }

650 else

651 {

652 bytes_written =

653 \_dbus_write_socket (socket_transport-\>fd,

654 body,

655 (socket_transport-\>message_bytes_written - header_len),

656 body_len -

657 (socket_transport-\>message_bytes_written - header_len));

658 }

659

660 saved_errno = \_dbus_save_socket_errno ();

661 }

662 }

663

664 if (bytes_written \< 0)

665 {

666 /\* EINTR already handled for us \*/

667

668 /\* If the other end closed the socket with close() or shutdown(), we

669 \* receive EPIPE here but we must not close the socket yet: there

670 \* might still be some data to read. See:

671 \* http://lists.freedesktop.org/archives/dbus/2008-March/009526.html

672 \*/

673

674 if (\_dbus_get_is_errno_eagain_or_ewouldblock (saved_errno) \|\| \_dbus_get_is_errno_epipe (saved_errno))

675 goto out;

676

677 /\* Since Linux commit 25888e (from 2.6.37-rc4, Nov 2010), sendmsg()

678 \* on Unix sockets returns -1 errno=ETOOMANYREFS when the passfd

679 \* mechanism (SCM_RIGHTS) is used recursively with a recursion level

680 \* of maximum 4. The kernel does not have an API to check whether

681 \* the passed fds can be forwarded and it can change asynchronously.

682 \* See:

683 \* https://bugs.freedesktop.org/show_bug.cgi?id=80163

684 \*/

685

686 else if (\_dbus_get_is_errno_etoomanyrefs (saved_errno))

687 {

688 /\* We only send fds in the first byte of the message.

689 \* ETOOMANYREFS cannot happen after.

690 \*/

691 \_dbus_assert (socket_transport-\>message_bytes_written == 0);

692

693 \_dbus_verbose (" discard message of %d bytes due to ETOOMANYREFS\n",

694 total_bytes_to_write);

695

696 socket_transport-\>message_bytes_written = 0;

697 \_dbus_string_set_length (&socket_transport-\>encoded_outgoing, 0);

698 \_dbus_string_compact (&socket_transport-\>encoded_outgoing, 2048);

699

700 /\* The message was not actually sent but it needs to be removed

701 \* from the outgoing queue

702 \*/

703 \_dbus_connection_message_sent_unlocked (transport-\>connection,

704 message);

705 }

706 else

707 {

708 \_dbus_verbose ("Error writing to remote app: %s\n",

709 \_dbus_strerror (saved_errno));

710 do_io_error (transport);

711 goto out;

712 }

713 }

714 else

715 {

716 \_dbus_verbose (" wrote %d bytes of %d\n", bytes_written,

717 total_bytes_to_write);

718

719 total += bytes_written;

720 socket_transport-\>message_bytes_written += bytes_written;

721

722 \_dbus_assert (socket_transport-\>message_bytes_written \<=

723 total_bytes_to_write);

724

725 if (socket_transport-\>message_bytes_written == total_bytes_to_write)

726 {

727 socket_transport-\>message_bytes_written = 0;

728 \_dbus_string_set_length (&socket_transport-\>encoded_outgoing, 0);

729 \_dbus_string_compact (&socket_transport-\>encoded_outgoing, 2048);

730

731 \_dbus_connection_message_sent_unlocked (transport-\>connection,

732 message);

733 }

734 }

735 }

736

737 out:

738 if (oom)

739 return FALSE;

740 else

741 return TRUE;

742}

743

744/\* returns false on out-of-memory \*/

745static dbus_bool_t

746do_reading (DBusTransport \*transport)

747{

748 DBusTransportSocket \*socket_transport = (DBusTransportSocket\*) transport;

749 DBusString \*buffer;

750 int bytes_read;

751 int total;

752 dbus_bool_t oom;

753 int saved_errno;

754

755 \_dbus_verbose ("fd = %" DBUS_SOCKET_FORMAT "\n",

756 \_dbus_socket_printable (socket_transport-\>fd));

757

758 /\* No messages without authentication! \*/

759 if (!\_dbus_transport_try_to_authenticate (transport))

760 return TRUE;

761

762 oom = FALSE;

763

764 total = 0;

765

766 again:

767

768 /\* See if we've exceeded max messages and need to disable reading \*/

769 check_read_watch (transport);

770

771 if (total \> socket_transport-\>max_bytes_read_per_iteration)

772 {

773 \_dbus_verbose ("%d bytes exceeds %d bytes read per iteration, returning\n",

774 total, socket_transport-\>max_bytes_read_per_iteration);

775 goto out;

776 }

777

778 \_dbus_assert (socket_transport-\>read_watch != NULL \|\|

779 transport-\>disconnected);

780

781 if (transport-\>disconnected)

782 goto out;

783

784 if (!dbus_watch_get_enabled (socket_transport-\>read_watch))

785 return TRUE;

786

787 if (\_dbus_auth_needs_decoding (transport-\>auth))

788 {

789 /\* Does fd passing even make sense with encoded data? \*/

790 \_dbus_assert(!DBUS_TRANSPORT_CAN_SEND_UNIX_FD(transport));

791

792 if (\_dbus_string_get_length (&socket_transport-\>encoded_incoming) \> 0)

793 bytes_read = \_dbus_string_get_length (&socket_transport-\>encoded_incoming);

794 else

795 bytes_read = \_dbus_read_socket (socket_transport-\>fd,

796 &socket_transport-\>encoded_incoming,

797 socket_transport-\>max_bytes_read_per_iteration);

798

799 saved_errno = \_dbus_save_socket_errno ();

800

801 \_dbus_assert (\_dbus_string_get_length (&socket_transport-\>encoded_incoming) ==

802 bytes_read);

803

804 if (bytes_read \> 0)

805 {

806 \_dbus_message_loader_get_buffer (transport-\>loader,

807 &buffer,

808 NULL,

809 NULL);

810

811 if (!\_dbus_auth_decode_data (transport-\>auth,

812 &socket_transport-\>encoded_incoming,

813 buffer))

814 {

815 \_dbus_verbose ("Out of memory decoding incoming data\n");

816 \_dbus_message_loader_return_buffer (transport-\>loader,

817 buffer);

818

819 oom = TRUE;

820 goto out;

821 }

822

823 \_dbus_message_loader_return_buffer (transport-\>loader,

824 buffer);

825

826 \_dbus_string_set_length (&socket_transport-\>encoded_incoming, 0);

827 \_dbus_string_compact (&socket_transport-\>encoded_incoming, 2048);

828 }

829 }

830 else

831 {

832 int max_to_read = DBUS_MAXIMUM_MESSAGE_LENGTH;

833 dbus_bool_t may_read_unix_fds = TRUE;

834

835 \_dbus_message_loader_get_buffer (transport-\>loader,

836 &buffer,

837 &max_to_read,

838 &may_read_unix_fds);

839

840 if (max_to_read \> socket_transport-\>max_bytes_read_per_iteration)

841 max_to_read = socket_transport-\>max_bytes_read_per_iteration;

842

843\#ifdef HAVE_UNIX_FD_PASSING

844 if (DBUS_TRANSPORT_CAN_SEND_UNIX_FD(transport) && may_read_unix_fds)

845 {

846 int \*fds;

847 unsigned int n_fds;

848

849 if (!\_dbus_message_loader_get_unix_fds(transport-\>loader, &fds, &n_fds))

850 {

851 \_dbus_verbose ("Out of memory reading file descriptors\n");

852 \_dbus_message_loader_return_buffer (transport-\>loader, buffer);

853 oom = TRUE;

854 goto out;

855 }

856

857 bytes_read = \_dbus_read_socket_with_unix_fds(socket_transport-\>fd,

858 buffer,

859 max_to_read,

860 fds, &n_fds);

861 saved_errno = \_dbus_save_socket_errno ();

862

863 if (bytes_read \>= 0 && n_fds \> 0)

864 \_dbus_verbose("Read %i unix fds\n", n_fds);

865

866 \_dbus_message_loader_return_unix_fds(transport-\>loader, fds, bytes_read \< 0 ? 0 : n_fds);

867 }

868 else

869\#endif

870 {

871 bytes_read = \_dbus_read_socket (socket_transport-\>fd,

872 buffer, max_to_read);

873 saved_errno = \_dbus_save_socket_errno ();

874 }

875

876 \_dbus_message_loader_return_buffer (transport-\>loader,

877 buffer);

878 }

879

880 if (bytes_read \< 0)

881 {

882 /\* EINTR already handled for us \*/

883

884 if (\_dbus_get_is_errno_enomem (saved_errno))

885 {

886 \_dbus_verbose ("Out of memory in read()/do_reading()\n");

887 oom = TRUE;

888 goto out;

889 }

890 else if (\_dbus_get_is_errno_eagain_or_ewouldblock (saved_errno))

891 goto out;

892 else

893 {

894 \_dbus_verbose ("Error reading from remote app: %s\n",

895 \_dbus_strerror (saved_errno));

896 do_io_error (transport);

897 goto out;

898 }

899 }

900 else if (bytes_read == 0)

901 {

902 \_dbus_verbose ("Disconnected from remote app\n");

903 do_io_error (transport);

904 goto out;

905 }

906 else

907 {

908 \_dbus_verbose (" read %d bytes\n", bytes_read);

909

910 total += bytes_read;

911

912 if (!\_dbus_transport_queue_messages (transport))

913 {

914 oom = TRUE;

915 \_dbus_verbose (" out of memory when queueing messages we just read in the transport\n");

916 goto out;

917 }

918

919 /\* Try reading more data until we get EAGAIN and return, or

920 \* exceed max bytes per iteration. If in blocking mode of

921 \* course we'll block instead of returning.

922 \*/

923 goto again;

924 }

925

926 out:

927 if (oom)

928 return FALSE;

929 else

930 return TRUE;

931}

932

933static dbus_bool_t

934unix_error_with_read_to_come (DBusTransport \*itransport,

935 DBusWatch \*watch,

936 unsigned int flags)

937{

938 DBusTransportSocket \*transport = (DBusTransportSocket \*) itransport;

939

940 if (!(flags & DBUS_WATCH_HANGUP \|\| flags & DBUS_WATCH_ERROR))

941 return FALSE;

942

943 /\* If we have a read watch enabled ...

944 we -might have data incoming ... =\> handle the HANGUP there \*/

945 if (watch != transport-\>read_watch &&

946 \_dbus_watch_get_enabled (transport-\>read_watch))

947 return FALSE;

948

949 return TRUE;

950}

951

952static dbus_bool_t

953socket_handle_watch (DBusTransport \*transport,

954 DBusWatch \*watch,

955 unsigned int flags)

956{

957 DBusTransportSocket \*socket_transport = (DBusTransportSocket\*) transport;

958

959 \_dbus_assert (watch == socket_transport-\>read_watch \|\|

960 watch == socket_transport-\>write_watch);

961 \_dbus_assert (watch != NULL);

962

963 /\* If we hit an error here on a write watch, don't disconnect the transport yet because data can

964 \* still be in the buffer and do_reading may need several iteration to read

965 \* it all (because of its max_bytes_read_per_iteration limit).

966 \*/

967 if (!(flags & DBUS_WATCH_READABLE) && unix_error_with_read_to_come (transport, watch, flags))

968 {

969 \_dbus_verbose ("Hang up or error on watch\n");

970 \_dbus_transport_disconnect (transport);

971 return TRUE;

972 }

973

974 if (watch == socket_transport-\>read_watch &&

975 (flags & DBUS_WATCH_READABLE))

976 {

977 dbus_bool_t auth_finished;

978\#if 1

979 \_dbus_verbose ("handling read watch %p flags = %x\n",

980 watch, flags);

981\#endif

982 if (!do_authentication (transport, TRUE, FALSE, &auth_finished))

983 return FALSE;

984

985 /\* We don't want to do a read immediately following

986 \* a successful authentication. This is so we

987 \* have a chance to propagate the authentication

988 \* state further up. Specifically, we need to

989 \* process any pending data from the auth object.

990 \*/

991 if (!auth_finished)

992 {

993 if (!do_reading (transport))

994 {

995 \_dbus_verbose ("no memory to read\n");

996 return FALSE;

997 }

998 }

999 else

1000 {

1001 \_dbus_verbose ("Not reading anything since we just completed the authentication\n");

1002 }

1003 }

1004 else if (watch == socket_transport-\>write_watch &&

1005 (flags & DBUS_WATCH_WRITABLE))

1006 {

1007\#if 1

1008 \_dbus_verbose ("handling write watch, have_outgoing_messages = %d\n",

1009 \_dbus_connection_has_messages_to_send_unlocked (transport-\>connection));

1010\#endif

1011 if (!do_authentication (transport, FALSE, TRUE, NULL))

1012 return FALSE;

1013

1014 if (!do_writing (transport))

1015 {

1016 \_dbus_verbose ("no memory to write\n");

1017 return FALSE;

1018 }

1019

1020 /\* See if we still need the write watch \*/

1021 check_write_watch (transport);

1022 }

1023\#ifdef DBUS_ENABLE_VERBOSE_MODE

1024 else

1025 {

1026 if (watch == socket_transport-\>read_watch)

1027 \_dbus_verbose ("asked to handle read watch with non-read condition 0x%x\n",

1028 flags);

1029 else if (watch == socket_transport-\>write_watch)

1030 \_dbus_verbose ("asked to handle write watch with non-write condition 0x%x\n",

1031 flags);

1032 else

1033 \_dbus_verbose ("asked to handle watch %p on fd %" DBUS_SOCKET_FORMAT " that we don't recognize\n",

1034 watch, \_dbus_socket_printable (\_dbus_watch_get_socket (watch)));

1035 }

1036\#endif /\* DBUS_ENABLE_VERBOSE_MODE \*/

1037

1038 return TRUE;

1039}

1040

1041static void

1042socket_disconnect (DBusTransport \*transport)

1043{

1044 DBusTransportSocket \*socket_transport = (DBusTransportSocket\*) transport;

1045

1046 \_dbus_verbose ("\n");

1047

1048 free_watches (transport);

1049

1050 \_dbus_close_socket (&socket_transport-\>fd, NULL);

1051}

1052

1053static dbus_bool_t

1054socket_connection_set (DBusTransport \*transport)

1055{

1056 DBusTransportSocket \*socket_transport = (DBusTransportSocket\*) transport;

1057

1058 \_dbus_watch_set_handler (socket_transport-\>write_watch,

1059 \_dbus_connection_handle_watch,

1060 transport-\>connection, NULL);

1061

1062 \_dbus_watch_set_handler (socket_transport-\>read_watch,

1063 \_dbus_connection_handle_watch,

1064 transport-\>connection, NULL);

1065

1066 if (!\_dbus_connection_add_watch_unlocked (transport-\>connection,

1067 socket_transport-\>write_watch))

1068 return FALSE;

1069

1070 if (!\_dbus_connection_add_watch_unlocked (transport-\>connection,

1071 socket_transport-\>read_watch))

1072 {

1073 \_dbus_connection_remove_watch_unlocked (transport-\>connection,

1074 socket_transport-\>write_watch);

1075 return FALSE;

1076 }

1077

1078 check_read_watch (transport);

1079 check_write_watch (transport);

1080

1081 return TRUE;

1082}

1083

1091static void

1092socket_do_iteration (DBusTransport \*transport,

1093 unsigned int flags,

1094 int timeout_milliseconds)

1095{

1096 DBusTransportSocket \*socket_transport = (DBusTransportSocket\*) transport;

1097 DBusPollFD poll_fd;

1098 int poll_res;

1099 int poll_timeout;

1100

1101 \_dbus_verbose (" iteration flags = %s%s timeout = %d read_watch = %p write_watch = %p fd = %" DBUS_SOCKET_FORMAT "\n",

1102 flags & DBUS_ITERATION_DO_READING ? "read" : "",

1103 flags & DBUS_ITERATION_DO_WRITING ? "write" : "",

1104 timeout_milliseconds,

1105 socket_transport-\>read_watch,

1106 socket_transport-\>write_watch,

1107 \_dbus_socket_printable (socket_transport-\>fd));

1108

1109 /\* the passed in DO_READING/DO_WRITING flags indicate whether to

1110 \* read/write messages, but regardless of those we may need to block

1111 \* for reading/writing to do auth. But if we do reading for auth,

1112 \* we don't want to read any messages yet if not given DO_READING.

1113 \*/

1114

1115 poll_fd.fd = \_dbus_socket_get_pollable (socket_transport-\>fd);

1116 poll_fd.events = 0;

1117

1118 if (\_dbus_transport_try_to_authenticate (transport))

1119 {

1120 /\* This is kind of a hack; if we have stuff to write, then try

1121 \* to avoid the poll. This is probably about a 5% speedup on an

1122 \* echo client/server.

1123 \*

1124 \* If both reading and writing were requested, we want to avoid this

1125 \* since it could have funky effects:

1126 \* - both ends spinning waiting for the other one to read

1127 \* data so they can finish writing

1128 \* - prioritizing all writing ahead of reading

1129 \*/

1130 if ((flags & DBUS_ITERATION_DO_WRITING) &&

1131 !(flags & (DBUS_ITERATION_DO_READING \| DBUS_ITERATION_BLOCK)) &&

1132 !transport-\>disconnected &&

1133 \_dbus_connection_has_messages_to_send_unlocked (transport-\>connection))

1134 {

1135 do_writing (transport);

1136

1137 if (transport-\>disconnected \|\|

1138 !\_dbus_connection_has_messages_to_send_unlocked (transport-\>connection))

1139 goto out;

1140 }

1141

1142 /\* If we get here, we decided to do the poll() after all \*/

1143 \_dbus_assert (socket_transport-\>read_watch);

1144 if (flags & DBUS_ITERATION_DO_READING)

1145 poll_fd.events \|= \_DBUS_POLLIN;

1146

1147 \_dbus_assert (socket_transport-\>write_watch);

1148 if (flags & DBUS_ITERATION_DO_WRITING)

1149 poll_fd.events \|= \_DBUS_POLLOUT;

1150 }

1151 else

1152 {

1153 DBusAuthState auth_state;

1154

1155 auth_state = \_dbus_auth_do_work (transport-\>auth);

1156

1157 if (transport-\>receive_credentials_pending \|\|

1158 auth_state == DBUS_AUTH_STATE_WAITING_FOR_INPUT)

1159 poll_fd.events \|= \_DBUS_POLLIN;

1160

1161 if (transport-\>send_credentials_pending \|\|

1162 auth_state == DBUS_AUTH_STATE_HAVE_BYTES_TO_SEND)

1163 poll_fd.events \|= \_DBUS_POLLOUT;

1164 }

1165

1166 if (poll_fd.events)

1167 {

1168 int saved_errno;

1169

1170 if (flags & DBUS_ITERATION_BLOCK)

1171 poll_timeout = timeout_milliseconds;

1172 else

1173 poll_timeout = 0;

1174

1175 /\* For blocking selects we drop the connection lock here

1176 \* to avoid blocking out connection access during a potentially

1177 \* indefinite blocking call. The io path is still protected

1178 \* by the io_path_cond condvar, so we won't reenter this.

1179 \*/

1180 if (flags & DBUS_ITERATION_BLOCK)

1181 {

1182 \_dbus_verbose ("unlock pre poll\n");

1183 \_dbus_connection_unlock (transport-\>connection);

1184 }

1185

1186 again:

1187 poll_res = \_dbus_poll (&poll_fd, 1, poll_timeout);

1188 saved_errno = \_dbus_save_socket_errno ();

1189

1190 if (poll_res \< 0 && \_dbus_get_is_errno_eintr (saved_errno))

1191 goto again;

1192

1193 if (flags & DBUS_ITERATION_BLOCK)

1194 {

1195 \_dbus_verbose ("lock post poll\n");

1196 \_dbus_connection_lock (transport-\>connection);

1197 }

1198

1199 if (poll_res \>= 0)

1200 {

1201 if (poll_res == 0)

1202 poll_fd.revents = 0; /\* some concern that posix does not guarantee this;

1203 \* valgrind flags it as an error. though it probably

1204 \* is guaranteed on linux at least.

1205 \*/

1206

1207 if (poll_fd.revents & \_DBUS_POLLERR)

1208 do_io_error (transport);

1209 else

1210 {

1211 dbus_bool_t need_read = (poll_fd.revents & \_DBUS_POLLIN) \> 0;

1212 dbus_bool_t need_write = (poll_fd.revents & \_DBUS_POLLOUT) \> 0;

1213 dbus_bool_t authentication_completed;

1214

1215 \_dbus_verbose ("in iteration, need_read=%d need_write=%d\n",

1216 need_read, need_write);

1217 do_authentication (transport, need_read, need_write,

1218 &authentication_completed);

1219

1220 /\* See comment in socket_handle_watch. \*/

1221 if (authentication_completed)

1222 goto out;

1223

1224 if (need_read && (flags & DBUS_ITERATION_DO_READING))

1225 do_reading (transport);

1226 if (need_write && (flags & DBUS_ITERATION_DO_WRITING))

1227 do_writing (transport);

1228 }

1229 }

1230 else

1231 {

1232 \_dbus_verbose ("Error from \_dbus_poll(): %s\n",

1233 \_dbus_strerror (saved_errno));

1234 }

1235 }

1236

1237

1238 out:

1239 /\* We need to install the write watch only if we did not

1240 \* successfully write everything. Note we need to be careful that we

1241 \* don't call check_write_watch \*before\* do_writing, since it's

1242 \* inefficient to add the write watch, and we can avoid it most of

1243 \* the time since we can write immediately.

1244 \*

1245 \* However, we MUST always call check_write_watch(); DBusConnection code

1246 \* relies on the fact that running an iteration will notice that

1247 \* messages are pending.

1248 \*/

1249 check_write_watch (transport);

1250

1251 \_dbus_verbose (" ... leaving do_iteration()\n");

1252}

1253

1254static void

1255socket_live_messages_changed (DBusTransport \*transport)

1256{

1257 /\* See if we should look for incoming messages again \*/

1258 check_read_watch (transport);

1259}

1260

1261

1262static dbus_bool_t

1263socket_get_socket_fd (DBusTransport \*transport,

1264 DBusSocket \*fd_p)

1265{

1266 DBusTransportSocket \*socket_transport = (DBusTransportSocket\*) transport;

1267

1268 \*fd_p = socket_transport-\>fd;

1269

1270 return TRUE;

1271}

1272

1273static const DBusTransportVTable socket_vtable = {

1274 socket_finalize,

1275 socket_handle_watch,

1276 socket_disconnect,

1277 socket_connection_set,

1278 socket_do_iteration,

1279 socket_live_messages_changed,

1280 socket_get_socket_fd

1281};

1282

1294DBusTransport\*

1295\_dbus_transport_new_for_socket (DBusSocket fd,

1296 const DBusString \*server_guid,

1297 const DBusString \*address)

1298{

1299 DBusTransportSocket \*socket_transport;

1300 DBusString invalid = \_DBUS_STRING_INIT_INVALID;

1301

1302 socket_transport = dbus_new0 (DBusTransportSocket, 1);

1303 if (socket_transport == NULL)

1304 return NULL;

1305

1306 /\* So they can be "freed" without error \*/

1307 socket_transport-\>encoded_outgoing = invalid;

1308 socket_transport-\>encoded_incoming = invalid;

1309

1310 if (!\_dbus_string_init (&socket_transport-\>encoded_outgoing))

1311 goto failed;

1312

1313 if (!\_dbus_string_init (&socket_transport-\>encoded_incoming))

1314 goto failed;

1315

1316 socket_transport-\>write_watch = \_dbus_watch_new (\_dbus_socket_get_pollable (fd),

1317 DBUS_WATCH_WRITABLE,

1318 FALSE,

1319 NULL, NULL, NULL);

1320 if (socket_transport-\>write_watch == NULL)

1321 goto failed;

1322

1323 socket_transport-\>read_watch = \_dbus_watch_new (\_dbus_socket_get_pollable (fd),

1324 DBUS_WATCH_READABLE,

1325 FALSE,

1326 NULL, NULL, NULL);

1327 if (socket_transport-\>read_watch == NULL)

1328 goto failed;

1329

1330 if (!\_dbus_transport_init_base (&socket_transport-\>base,

1331 &socket_vtable,

1332 server_guid, address))

1333 goto failed;

1334

1335\#ifdef HAVE_UNIX_FD_PASSING

1336 \_dbus_auth_set_unix_fd_possible(socket_transport-\>base.auth, \_dbus_socket_can_pass_unix_fd(fd));

1337\#endif

1338

1339 socket_transport-\>fd = fd;

1340 socket_transport-\>message_bytes_written = 0;

1341

1342 /\* These values should probably be tunable or something. \*/

1343 socket_transport-\>max_bytes_read_per_iteration = 2048;

1344 socket_transport-\>max_bytes_written_per_iteration = 2048;

1345

1346 return (DBusTransport\*) socket_transport;

1347

1348failed:

1349 if (socket_transport-\>read_watch != NULL)

1350 {

1351 \_dbus_watch_invalidate (socket_transport-\>read_watch);

1352 \_dbus_watch_unref (socket_transport-\>read_watch);

1353 }

1354

1355 if (socket_transport-\>write_watch != NULL)

1356 {

1357 \_dbus_watch_invalidate (socket_transport-\>write_watch);

1358 \_dbus_watch_unref (socket_transport-\>write_watch);

1359 }

1360

1361 \_dbus_string_free (&socket_transport-\>encoded_incoming);

1362 \_dbus_string_free (&socket_transport-\>encoded_outgoing);

1363 dbus_free (socket_transport);

1364 return NULL;

1365}

1366

1378DBusTransport\*

1379\_dbus_transport_new_for_tcp_socket (const char \*host,

1380 const char \*port,

1381 const char \*family,

1382 const char \*noncefile,

1383 DBusError \*error)

1384{

1385 DBusSocket fd;

1386 DBusTransport \*transport;

1387 DBusString address;

1388

1389 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

1390

1391 if (!\_dbus_string_init (&address))

1392 {

1393 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

1394 return NULL;

1395 }

1396

1397 if (host == NULL)

1398 host = "localhost";

1399

1400 if (!\_dbus_string_append (&address, noncefile ? "nonce-tcp:" : "tcp:"))

1401 goto error;

1402

1403 if (!\_dbus_string_append (&address, "host=") \|\|

1404 !\_dbus_string_append (&address, host))

1405 goto error;

1406

1407 if (!\_dbus_string_append (&address, ",port=") \|\|

1408 !\_dbus_string_append (&address, port))

1409 goto error;

1410

1411 if (family != NULL &&

1412 (!\_dbus_string_append (&address, ",family=") \|\|

1413 !\_dbus_string_append (&address, family)))

1414 goto error;

1415

1416 if (noncefile != NULL &&

1417 (!\_dbus_string_append (&address, ",noncefile=") \|\|

1418 !\_dbus_string_append (&address, noncefile)))

1419 goto error;

1420

1421 fd = \_dbus_connect_tcp_socket_with_nonce (host, port, family, noncefile, error);

1422 if (!\_dbus_socket_is_valid (fd))

1423 {

1424 \_DBUS_ASSERT_ERROR_IS_SET (error);

1425 \_dbus_string_free (&address);

1426 return NULL;

1427 }

1428

1429 \_dbus_verbose ("Successfully connected to tcp socket %s:%s\n",

1430 host, port);

1431

1432 transport = \_dbus_transport_new_for_socket (fd, NULL, &address);

1433 \_dbus_string_free (&address);

1434 if (transport == NULL)

1435 {

1436 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

1437 \_dbus_close_socket (&fd, NULL);

1438 }

1439

1440 return transport;

1441

1442error:

1443 \_dbus_string_free (&address);

1444 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

1445 return NULL;

1446}

1447

1456DBusTransportOpenResult

1457\_dbus_transport_open_socket(DBusAddressEntry \*entry,

1458 DBusTransport \*\*transport_p,

1459 DBusError \*error)

1460{

1461 const char \*method;

1462 dbus_bool_t isTcp;

1463 dbus_bool_t isNonceTcp;

1464

1465 method = dbus_address_entry_get_method (entry);

1466 \_dbus_assert (method != NULL);

1467

1468 isTcp = strcmp (method, "tcp") == 0;

1469 isNonceTcp = strcmp (method, "nonce-tcp") == 0;

1470

1471 if (isTcp \|\| isNonceTcp)

1472 {

1473 const char \*host = dbus_address_entry_get_value (entry, "host");

1474 const char \*port = dbus_address_entry_get_value (entry, "port");

1475 const char \*family = dbus_address_entry_get_value (entry, "family");

1476 const char \*noncefile = dbus_address_entry_get_value (entry, "noncefile");

1477

1478 if ((isNonceTcp == TRUE) != (noncefile != NULL)) {

1479 \_dbus_set_bad_address (error, method, "noncefile", NULL);

1480 return DBUS_TRANSPORT_OPEN_BAD_ADDRESS;

1481 }

1482

1483 if (port == NULL)

1484 {

1485 \_dbus_set_bad_address (error, method, "port", NULL);

1486 return DBUS_TRANSPORT_OPEN_BAD_ADDRESS;

1487 }

1488

1489 \*transport_p = \_dbus_transport_new_for_tcp_socket (host, port, family, noncefile, error);

1490 if (\*transport_p == NULL)

1491 {

1492 \_DBUS_ASSERT_ERROR_IS_SET (error);

1493 return DBUS_TRANSPORT_OPEN_DID_NOT_CONNECT;

1494 }

1495 else

1496 {

1497 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

1498 return DBUS_TRANSPORT_OPEN_OK;

1499 }

1500 }

1501 else

1502 {

1503 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

1504 return DBUS_TRANSPORT_OPEN_NOT_HANDLED;

1505 }

1506}

1507

1517DBusTransport\*

1518\_dbus_transport_new_for_domain_socket (const char \*path,

1519 dbus_bool_t abstract,

1520 DBusError \*error)

1521{

1522 DBusSocket fd = DBUS_SOCKET_INIT;

1523 DBusTransport \*transport;

1524 DBusString address;

1525 DBusString unescaped_path;

1526

1527 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

1528

1529 if (!\_dbus_string_init (&address))

1530 {

1531 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

1532 return NULL;

1533 }

1534

1535 \_dbus_string_init_const (&unescaped_path, path);

1536

1537 if ((abstract &&

1538 !\_dbus_string_append (&address, "unix:abstract=")) \|\|

1539 (!abstract &&

1540 !\_dbus_string_append (&address, "unix:path=")) \|\|

1541 !\_dbus_address_append_escaped (&address, &unescaped_path))

1542 {

1543 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

1544 goto failed_0;

1545 }

1546

1547 fd = \_dbus_connect_unix_socket (path, abstract, error);

1548 if (!\_dbus_socket_is_valid (fd))

1549 {

1550 \_DBUS_ASSERT_ERROR_IS_SET (error);

1551 goto failed_0;

1552 }

1553

1554 \_dbus_verbose ("Successfully connected to unix socket %s\n",

1555 path);

1556

1557 transport = \_dbus_transport_new_for_socket (fd, NULL, &address);

1558 if (transport == NULL)

1559 {

1560 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

1561 goto failed_1;

1562 }

1563

1564 \_dbus_string_free (&address);

1565

1566 return transport;

1567

1568 failed_1:

1569 \_dbus_close_socket (&fd, NULL);

1570 failed_0:

1571 \_dbus_string_free (&address);

1572 return NULL;

1573}

1574

1583DBusTransportOpenResult

1584\_dbus_transport_open_unix_socket (DBusAddressEntry \*entry,

1585 DBusTransport \*\*transport_p,

1586 DBusError \*error)

1587{

1588 const char \*method;

1589

1590 method = dbus_address_entry_get_method (entry);

1591 \_dbus_assert (method != NULL);

1592

1593 if (strcmp (method, "unix") == 0)

1594 {

1595 const char \*path = dbus_address_entry_get_value (entry, "path");

1596 const char \*tmpdir = dbus_address_entry_get_value (entry, "tmpdir");

1597 const char \*abstract = dbus_address_entry_get_value (entry, "abstract");

1598

1599 if (tmpdir != NULL)

1600 {

1601 \_dbus_set_bad_address (error, NULL, NULL,

1602 "cannot use the \\tmpdir\\ option for an address to connect to, only in an address to listen on");

1603 return DBUS_TRANSPORT_OPEN_BAD_ADDRESS;

1604 }

1605

1606 if (path == NULL && abstract == NULL)

1607 {

1608 \_dbus_set_bad_address (error, "unix",

1609 "path or abstract",

1610 NULL);

1611 return DBUS_TRANSPORT_OPEN_BAD_ADDRESS;

1612 }

1613

1614 if (path != NULL && abstract != NULL)

1615 {

1616 \_dbus_set_bad_address (error, NULL, NULL,

1617 "can't specify both \\path\\ and \\abstract\\ options in an address");

1618 return DBUS_TRANSPORT_OPEN_BAD_ADDRESS;

1619 }

1620

1621 if (path)

1622 \*transport_p = \_dbus_transport_new_for_domain_socket (path, FALSE,

1623 error);

1624 else

1625 \*transport_p = \_dbus_transport_new_for_domain_socket (abstract, TRUE,

1626 error);

1627 if (\*transport_p == NULL)

1628 {

1629 \_DBUS_ASSERT_ERROR_IS_SET (error);

1630 return DBUS_TRANSPORT_OPEN_DID_NOT_CONNECT;

1631 }

1632 else

1633 {

1634 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

1635 return DBUS_TRANSPORT_OPEN_OK;

1636 }

1637 }

1638 else

1639 {

1640 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

1641 return DBUS_TRANSPORT_OPEN_NOT_HANDLED;

1642 }

1643}

1644

\_dbus_address_append_escaped

dbus_bool_t \_dbus_address_append_escaped(DBusString \*escaped, const DBusString \*unescaped)

Appends an escaped version of one string to another string, using the D-Bus address escaping mechanis...

**Definition** dbus-address.c:109

\_dbus_set_bad_address

void \_dbus_set_bad_address(DBusError \*error, const char \*address_problem_type, const char \*address_problem_field, const char \*address_problem_other)

Sets DBUS_ERROR_BAD_ADDRESS.

**Definition** dbus-address.c:70

dbus_address_entry_get_method

const char \* dbus_address_entry_get_method(DBusAddressEntry \*entry)

Returns the method string of an address entry.

**Definition** dbus-address.c:232

dbus_address_entry_get_value

const char \* dbus_address_entry_get_value(DBusAddressEntry \*entry, const char \*key)

Returns a value from a key of an entry.

**Definition** dbus-address.c:249

\_dbus_auth_do_work

DBusAuthState \_dbus_auth_do_work(DBusAuth \*auth)

Analyzes buffered input and moves the auth conversation forward, returning the new state of the auth ...

**Definition** dbus-auth.c:2548

\_dbus_auth_encode_data

dbus_bool_t \_dbus_auth_encode_data(DBusAuth \*auth, const DBusString \*plaintext, DBusString \*encoded)

Called post-authentication, encodes a block of bytes for sending to the peer.

**Definition** dbus-auth.c:2735

\_dbus_auth_needs_encoding

dbus_bool_t \_dbus_auth_needs_encoding(DBusAuth \*auth)

Called post-authentication, indicates whether we need to encode the message stream with \_dbus_auth_en...

**Definition** dbus-auth.c:2708

\_dbus_auth_set_credentials

dbus_bool_t \_dbus_auth_set_credentials(DBusAuth \*auth, DBusCredentials \*credentials)

Sets credentials received via reliable means from the operating system.

**Definition** dbus-auth.c:2830

\_dbus_auth_get_bytes_to_send

dbus_bool_t \_dbus_auth_get_bytes_to_send(DBusAuth \*auth, const DBusString \*\*str)

Gets bytes that need to be sent to the peer we're conversing with.

**Definition** dbus-auth.c:2592

\_dbus_auth_decode_data

dbus_bool_t \_dbus_auth_decode_data(DBusAuth \*auth, const DBusString \*encoded, DBusString \*plaintext)

Called post-authentication, decodes a block of bytes received from the peer.

**Definition** dbus-auth.c:2798

\_dbus_auth_set_unix_fd_possible

void \_dbus_auth_set_unix_fd_possible(DBusAuth \*auth, dbus_bool_t b)

Sets whether unix fd passing is potentially on the transport and hence shall be negotiated.

**Definition** dbus-auth.c:2906

\_dbus_auth_return_buffer

void \_dbus_auth_return_buffer(DBusAuth \*auth, DBusString \*buffer)

Returns a buffer with new data read into it.

**Definition** dbus-auth.c:2655

\_dbus_auth_get_buffer

void \_dbus_auth_get_buffer(DBusAuth \*auth, DBusString \*\*buffer)

Get a buffer to be used for reading bytes from the peer we're conversing with.

**Definition** dbus-auth.c:2637

\_dbus_auth_needs_decoding

dbus_bool_t \_dbus_auth_needs_decoding(DBusAuth \*auth)

Called post-authentication, indicates whether we need to decode the message stream with \_dbus_auth_de...

**Definition** dbus-auth.c:2767

\_dbus_auth_bytes_sent

void \_dbus_auth_bytes_sent(DBusAuth \*auth, int bytes_sent)

Notifies the auth conversation object that the given number of bytes of the outgoing buffer have been...

**Definition** dbus-auth.c:2617

\_dbus_connection_handle_watch

dbus_bool_t \_dbus_connection_handle_watch(DBusWatch \*watch, unsigned int condition, void \*data)

A callback for use with dbus_watch_new() to create a DBusWatch.

**Definition** dbus-connection.c:1500

\_dbus_connection_has_messages_to_send_unlocked

dbus_bool_t \_dbus_connection_has_messages_to_send_unlocked(DBusConnection \*connection)

Checks whether there are messages in the outgoing message queue.

**Definition** dbus-connection.c:576

\_dbus_connection_unlock

DBUS_PRIVATE_EXPORT void \_dbus_connection_unlock(DBusConnection \*connection)

Releases the connection lock.

**Definition** dbus-connection.c:403

\_dbus_connection_lock

DBUS_PRIVATE_EXPORT void \_dbus_connection_lock(DBusConnection \*connection)

Acquires the connection lock.

**Definition** dbus-connection.c:392

\_dbus_connection_remove_watch_unlocked

void \_dbus_connection_remove_watch_unlocked(DBusConnection \*connection, DBusWatch \*watch)

Removes a watch using the connection's DBusRemoveWatchFunction if available.

**Definition** dbus-connection.c:765

\_dbus_connection_toggle_watch_unlocked

void \_dbus_connection_toggle_watch_unlocked(DBusConnection \*connection, DBusWatch \*watch, dbus_bool_t enabled)

Toggles a watch and notifies app via connection's DBusWatchToggledFunction if available.

**Definition** dbus-connection.c:785

\_dbus_connection_add_watch_unlocked

dbus_bool_t \_dbus_connection_add_watch_unlocked(DBusConnection \*connection, DBusWatch \*watch)

Adds a watch using the connection's DBusAddWatchFunction if available.

**Definition** dbus-connection.c:747

\_dbus_connection_get_message_to_send

DBusMessage \* \_dbus_connection_get_message_to_send(DBusConnection \*connection)

Gets the next outgoing message.

**Definition** dbus-connection.c:613

\_dbus_connection_message_sent_unlocked

void \_dbus_connection_message_sent_unlocked(DBusConnection \*connection, DBusMessage \*message)

Notifies the connection that a message has been sent, so the message can be removed from the outgoing...

**Definition** dbus-connection.c:629

DBUS_WATCH_READABLE

@ DBUS_WATCH_READABLE

As in POLLIN.

**Definition** dbus-connection.h:63

DBUS_WATCH_WRITABLE

@ DBUS_WATCH_WRITABLE

As in POLLOUT.

**Definition** dbus-connection.h:64

DBUS_WATCH_HANGUP

@ DBUS_WATCH_HANGUP

As in POLLHUP (can't watch for it, but can be present in current state passed to dbus_watch_handle())...

**Definition** dbus-connection.h:70

DBUS_WATCH_ERROR

@ DBUS_WATCH_ERROR

As in POLLERR (can't watch for this, but can be present in current state passed to dbus_watch_handle(...

**Definition** dbus-connection.h:65

DBUS_ERROR_INIT

\#define DBUS_ERROR_INIT

Expands to a suitable initializer for a DBusError on the stack.

**Definition** dbus-errors.h:64

dbus_set_error

void dbus_set_error(DBusError \*error, const char \*name, const char \*format,...)

Assigns an error name and message to a DBusError.

**Definition** dbus-errors.c:356

dbus_error_free

void dbus_error_free(DBusError \*error)

Frees an error that's been set (or just initialized), then reinitializes the error as in dbus_error_i...

**Definition** dbus-errors.c:213

\_dbus_get_is_errno_epipe

dbus_bool_t \_dbus_get_is_errno_epipe(int e)

See if errno is EPIPE.

**Definition** dbus-sysdeps.c:700

\_dbus_assert_not_reached

\#define \_dbus_assert_not_reached(explanation)

Aborts with an error message if called.

**Definition** dbus-internals.h:164

\_dbus_get_is_errno_etoomanyrefs

dbus_bool_t \_dbus_get_is_errno_etoomanyrefs(int e)

See if errno is ETOOMANYREFS.

**Definition** dbus-sysdeps.c:710

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_dbus_get_is_errno_eintr

dbus_bool_t \_dbus_get_is_errno_eintr(int e)

See if errno is EINTR.

**Definition** dbus-sysdeps.c:690

\_dbus_get_is_errno_enomem

dbus_bool_t \_dbus_get_is_errno_enomem(int e)

See if errno is ENOMEM.

**Definition** dbus-sysdeps.c:680

NULL

\#define NULL

A null pointer, defined appropriately for C or C++.

**Definition** dbus-macros.h:51

TRUE

\#define TRUE

Expands to "1".

**Definition** dbus-macros.h:41

FALSE

\#define FALSE

Expands to "0".

**Definition** dbus-macros.h:44

dbus_free

void dbus_free(void \*memory)

Frees a block of memory previously allocated by dbus_malloc() or dbus_malloc0().

**Definition** dbus-memory.c:710

dbus_new0

\#define dbus_new0(type, count)

Safe macro for using dbus_malloc0().

**Definition** dbus-memory.h:60

dbus_message_lock

void dbus_message_lock(DBusMessage \*message)

Locks a message.

**Definition** dbus-message.c:431

\_dbus_message_get_unix_fds

DBUS_PRIVATE_EXPORT void \_dbus_message_get_unix_fds(DBusMessage \*message, const int \*\*fds, unsigned \*n_fds)

Gets the unix fds to be sent over the network for this message.

**Definition** dbus-message.c:262

\_dbus_message_get_network_data

void \_dbus_message_get_network_data(DBusMessage \*message, const DBusString \*\*header, const DBusString \*\*body)

Gets the data to be sent over the network for this message.

**Definition** dbus-message.c:243

\_dbus_message_loader_get_buffer

DBUS_PRIVATE_EXPORT void \_dbus_message_loader_get_buffer(DBusMessageLoader \*loader, DBusString \*\*buffer, int \*max_to_read, dbus_bool_t \*may_read_unix_fds)

Gets the buffer to use for reading data from the network.

**Definition** dbus-message.c:4274

\_dbus_message_loader_return_buffer

DBUS_PRIVATE_EXPORT void \_dbus_message_loader_return_buffer(DBusMessageLoader \*loader, DBusString \*buffer)

Returns a buffer obtained from \_dbus_message_loader_get_buffer(), indicating to the loader how many b...

**Definition** dbus-message.c:4380

DBUS_MAXIMUM_MESSAGE_LENGTH

\#define DBUS_MAXIMUM_MESSAGE_LENGTH

The maximum total message size including header and body; similar rationale to max array size.

**Definition** dbus-protocol.h:212

DBUS_ERROR_NO_MEMORY

\#define DBUS_ERROR_NO_MEMORY

There was not enough memory to complete an operation.

**Definition** dbus-protocol.h:363

\_dbus_counter_get_unix_fd_value

long \_dbus_counter_get_unix_fd_value(DBusCounter \*counter)

Gets the current value of the unix fd counter.

**Definition** dbus-resources.c:292

\_dbus_counter_get_size_value

long \_dbus_counter_get_size_value(DBusCounter \*counter)

Gets the current value of the size counter.

**Definition** dbus-resources.c:276

\_dbus_string_set_length

dbus_bool_t \_dbus_string_set_length(DBusString \*str, int length)

Sets the length of a string.

**Definition** dbus-string.c:847

\_dbus_string_append

dbus_bool_t \_dbus_string_append(DBusString \*str, const char \*buffer)

Appends a nul-terminated C-style string to a DBusString.

**Definition** dbus-string.c:980

\_dbus_string_init

dbus_bool_t \_dbus_string_init(DBusString \*str)

Initializes a string.

**Definition** dbus-string.c:182

\_dbus_string_init_const

void \_dbus_string_init_const(DBusString \*str, const char \*value)

Initializes a constant string.

**Definition** dbus-string.c:197

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_string_get_length

int \_dbus_string_get_length(const DBusString \*str)

Gets the length of a string (not including nul termination).

**Definition** dbus-string.c:784

\_dbus_string_compact

dbus_bool_t \_dbus_string_compact(DBusString \*str, int max_waste)

Compacts the string to avoid wasted memory.

**Definition** dbus-string.c:420

\_DBUS_POLLOUT

\#define \_DBUS_POLLOUT

Writing now will not block.

**Definition** dbus-sysdeps.h:448

\_dbus_get_is_errno_eagain_or_ewouldblock

dbus_bool_t \_dbus_get_is_errno_eagain_or_ewouldblock(int e)

See if errno is EAGAIN or EWOULDBLOCK (this has to be done differently for Winsock so is abstracted)

**Definition** dbus-sysdeps-unix.c:4801

\_dbus_read_socket

int \_dbus_read_socket(DBusSocket fd, DBusString \*buffer, int count)

Like \_dbus_read(), but only works on sockets so is available on Windows.

**Definition** dbus-sysdeps-unix.c:338

\_DBUS_POLLERR

\#define \_DBUS_POLLERR

Error condition.

**Definition** dbus-sysdeps.h:450

\_dbus_socket_can_pass_unix_fd

dbus_bool_t \_dbus_socket_can_pass_unix_fd(DBusSocket fd)

Checks whether file descriptors may be passed via the socket.

**Definition** dbus-sysdeps-unix.c:4850

\_dbus_write_socket

int \_dbus_write_socket(DBusSocket fd, const DBusString \*buffer, int start, int len)

Like \_dbus_write(), but only supports sockets and is thus available on Windows.

**Definition** dbus-sysdeps-unix.c:356

\_dbus_read_socket_with_unix_fds

int \_dbus_read_socket_with_unix_fds(DBusSocket fd, DBusString \*buffer, int count, int \*fds, unsigned int \*n_fds)

Like \_dbus_read_socket() but also tries to read unix fds from the socket.

**Definition** dbus-sysdeps-unix.c:394

\_dbus_read_credentials_socket

dbus_bool_t \_dbus_read_credentials_socket(DBusSocket client_fd, DBusCredentials \*credentials, DBusError \*error)

Reads a single byte which must be nul (an error occurs otherwise), and reads unix credentials if avai...

**Definition** dbus-sysdeps-unix.c:2209

\_DBUS_POLLIN

\#define \_DBUS_POLLIN

There is data to read.

**Definition** dbus-sysdeps.h:444

\_dbus_send_credentials_socket

dbus_bool_t \_dbus_send_credentials_socket(DBusSocket server_fd, DBusError \*error)

Sends a single nul byte with our UNIX credentials as ancillary data.

**Definition** dbus-sysdeps-unix.c:2568

\_dbus_close_socket

dbus_bool_t \_dbus_close_socket(DBusSocket \*fd, DBusError \*error)

Closes a socket and invalidates it.

**Definition** dbus-sysdeps-unix.c:314

\_dbus_connect_unix_socket

DBusSocket \_dbus_connect_unix_socket(const char \*path, dbus_bool_t abstract, DBusError \*error)

Creates a socket and connects it to the UNIX domain socket at the given path.

**Definition** dbus-sysdeps-unix.c:957

\_dbus_poll

int \_dbus_poll(DBusPollFD \*fds, int n_fds, int timeout_milliseconds)

Wrapper for poll().

**Definition** dbus-sysdeps-unix.c:3303

\_dbus_write_socket_two

int \_dbus_write_socket_two(DBusSocket fd, const DBusString \*buffer1, int start1, int len1, const DBusString \*buffer2, int start2, int len2)

Like \_dbus_write_two() but only works on sockets and is thus available on Windows.

**Definition** dbus-sysdeps-unix.c:694

\_dbus_transport_open_socket

DBusTransportOpenResult \_dbus_transport_open_socket(DBusAddressEntry \*entry, DBusTransport \*\*transport_p, DBusError \*error)

Opens a TCP socket transport.

**Definition** dbus-transport-socket.c:1457

\_dbus_transport_open_unix_socket

DBusTransportOpenResult \_dbus_transport_open_unix_socket(DBusAddressEntry \*entry, DBusTransport \*\*transport_p, DBusError \*error)

Opens a UNIX socket transport.

**Definition** dbus-transport-socket.c:1584

\_dbus_transport_new_for_tcp_socket

DBusTransport \* \_dbus_transport_new_for_tcp_socket(const char \*host, const char \*port, const char \*family, const char \*noncefile, DBusError \*error)

Creates a new transport for the given hostname and port.

**Definition** dbus-transport-socket.c:1379

\_dbus_transport_new_for_socket

DBusTransport \* \_dbus_transport_new_for_socket(DBusSocket fd, const DBusString \*server_guid, const DBusString \*address)

Creates a new transport for the given socket file descriptor.

**Definition** dbus-transport-socket.c:1295

\_dbus_transport_new_for_domain_socket

DBusTransport \* \_dbus_transport_new_for_domain_socket(const char \*path, dbus_bool_t abstract, DBusError \*error)

Creates a new transport for the given Unix domain socket path.

**Definition** dbus-transport-socket.c:1518

\_dbus_transport_queue_messages

dbus_bool_t \_dbus_transport_queue_messages(DBusTransport \*transport)

Processes data we've read while handling a watch, potentially converting some of it to messages and q...

**Definition** dbus-transport.c:1166

\_dbus_transport_ref

DBusTransport \* \_dbus_transport_ref(DBusTransport \*transport)

Increments the reference count for the transport.

**Definition** dbus-transport.c:469

\_dbus_transport_disconnect

void \_dbus_transport_disconnect(DBusTransport \*transport)

Closes our end of the connection to a remote application.

**Definition** dbus-transport.c:511

\_dbus_transport_init_base

dbus_bool_t \_dbus_transport_init_base(DBusTransport \*transport, const DBusTransportVTable \*vtable, const DBusString \*server_guid, const DBusString \*address)

Initializes the base class members of DBusTransport.

**Definition** dbus-transport.c:104

\_dbus_transport_unref

void \_dbus_transport_unref(DBusTransport \*transport)

Decrements the reference count for the transport.

**Definition** dbus-transport.c:486

\_dbus_transport_try_to_authenticate

dbus_bool_t \_dbus_transport_try_to_authenticate(DBusTransport \*transport)

Returns TRUE if we have been authenticated.

**Definition** dbus-transport.c:733

\_dbus_transport_get_is_connected

dbus_bool_t \_dbus_transport_get_is_connected(DBusTransport \*transport)

Returns TRUE if the transport has not been disconnected.

**Definition** dbus-transport.c:536

\_dbus_transport_finalize_base

void \_dbus_transport_finalize_base(DBusTransport \*transport)

Finalizes base class members of DBusTransport.

**Definition** dbus-transport.c:218

\_dbus_watch_set_handler

void \_dbus_watch_set_handler(DBusWatch \*watch, DBusWatchHandler handler, void \*data, DBusFreeFunction free_data_function)

Sets the handler for the watch.

**Definition** dbus-watch.c:500

\_dbus_watch_new

DBusWatch \* \_dbus_watch_new(DBusPollable fd, unsigned int flags, dbus_bool_t enabled, DBusWatchHandler handler, void \*data, DBusFreeFunction free_data_function)

Creates a new DBusWatch.

**Definition** dbus-watch.c:90

\_dbus_watch_unref

void \_dbus_watch_unref(DBusWatch \*watch)

Decrements the reference count of a DBusWatch object and finalizes the object if the count reaches ze...

**Definition** dbus-watch.c:140

\_dbus_watch_invalidate

void \_dbus_watch_invalidate(DBusWatch \*watch)

Clears the file descriptor from a now-invalid watch object so that no one tries to use it.

**Definition** dbus-watch.c:171

dbus_watch_get_enabled

DBUS_EXPORT dbus_bool_t dbus_watch_get_enabled(DBusWatch \*watch)

Returns whether a watch is enabled or not.

**Definition** dbus-watch.c:704

DBusAddressEntry

Internals of DBusAddressEntry.

**Definition** dbus-address.c:49

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusError::message

const char \* message

public error message field

**Definition** dbus-errors.h:53

DBusMessage

Internals of DBusMessage.

**Definition** dbus-message-private.h:102

DBusPollFD

**Definition** dbus-sysdeps.h:437

DBusPollFD::events

short events

Events to poll for.

**Definition** dbus-sysdeps.h:439

DBusPollFD::revents

short revents

Events that occurred.

**Definition** dbus-sysdeps.h:440

DBusPollFD::fd

DBusPollable fd

File descriptor.

**Definition** dbus-sysdeps.h:438

DBusSocket

Socket interface.

**Definition** dbus-sysdeps.h:185

DBusString

**Definition** dbus-string.h:47

DBusTransportSocket

Implementation details of DBusTransportSocket.

**Definition** dbus-transport-socket.c:55

DBusTransportSocket::write_watch

DBusWatch \* write_watch

Watch for writability.

**Definition** dbus-transport-socket.c:59

DBusTransportSocket::message_bytes_written

int message_bytes_written

Number of bytes of current outgoing message that have been written.

**Definition** dbus-transport-socket.c:64

DBusTransportSocket::max_bytes_written_per_iteration

int max_bytes_written_per_iteration

To avoid blocking too long.

**Definition** dbus-transport-socket.c:62

DBusTransportSocket::encoded_incoming

DBusString encoded_incoming

Encoded version of current incoming data.

**Definition** dbus-transport-socket.c:71

DBusTransportSocket::encoded_outgoing

DBusString encoded_outgoing

Encoded version of current outgoing message.

**Definition** dbus-transport-socket.c:68

DBusTransportSocket::fd

DBusSocket fd

File descriptor.

**Definition** dbus-transport-socket.c:57

DBusTransportSocket::base

DBusTransport base

Parent instance.

**Definition** dbus-transport-socket.c:56

DBusTransportSocket::read_watch

DBusWatch \* read_watch

Watch for readability.

**Definition** dbus-transport-socket.c:58

DBusTransportSocket::max_bytes_read_per_iteration

int max_bytes_read_per_iteration

To avoid blocking too long.

**Definition** dbus-transport-socket.c:61

DBusTransportVTable

The virtual table that must be implemented to create a new kind of transport.

**Definition** dbus-transport-protected.h:44

DBusTransport

Object representing a transport such as a socket.

**Definition** dbus-transport-protected.h:83

DBusTransport::max_live_messages_size

long max_live_messages_size

Max total size of received messages.

**Definition** dbus-transport-protected.h:96

DBusTransport::max_live_messages_unix_fds

long max_live_messages_unix_fds

Max total unix fds of received messages.

**Definition** dbus-transport-protected.h:97

DBusTransport::disconnected

unsigned int disconnected

TRUE if we are disconnected.

**Definition** dbus-transport-protected.h:115

DBusTransport::send_credentials_pending

unsigned int send_credentials_pending

TRUE if we need to send credentials

**Definition** dbus-transport-protected.h:117

DBusTransport::connection

DBusConnection \* connection

Connection owning this transport.

**Definition** dbus-transport-protected.h:88

DBusTransport::receive_credentials_pending

unsigned int receive_credentials_pending

TRUE if we need to receive credentials

**Definition** dbus-transport-protected.h:118

DBusTransport::loader

DBusMessageLoader \* loader

Message-loading buffer.

**Definition** dbus-transport-protected.h:90

DBusTransport::credentials

DBusCredentials \* credentials

Credentials of other end read from the socket.

**Definition** dbus-transport-protected.h:94

DBusTransport::auth

DBusAuth \* auth

Authentication conversation.

**Definition** dbus-transport-protected.h:92

DBusTransport::live_messages

DBusCounter \* live_messages

Counter for size/unix fds of all live messages.

**Definition** dbus-transport-protected.h:99

DBusWatch

Implementation of DBusWatch.

**Definition** dbus-watch.c:43
