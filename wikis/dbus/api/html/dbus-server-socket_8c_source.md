dbus-server-socket.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-server-socket.c Server implementation for sockets

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

27\#include "dbus-internals.h"

28\#include "dbus-server-socket.h"

29\#include "dbus-transport-socket.h"

30\#include "dbus-connection-internal.h"

31\#include "dbus-memory.h"

32\#include "dbus-nonce.h"

33\#include "dbus-string.h"

34

46typedef struct DBusServerSocket DBusServerSocket;

47

52struct DBusServerSocket

53{

54 DBusServer base;

55 int n_fds;

56 DBusSocket \*fds;

57 DBusWatch \*\*watch;

58 char \*socket_name;

59 DBusNonceFile \*noncefile;

60};

61

62static void

63socket_finalize (DBusServer \*server)

64{

65 DBusServerSocket \*socket_server = (DBusServerSocket\*) server;

66 int i;

67

68 \_dbus_server_finalize_base (server);

69

70 for (i = 0 ; i \< socket_server-\>n_fds ; i++)

71 if (socket_server-\>watch\[i\])

72 {

73 \_dbus_watch_unref (socket_server-\>watch\[i\]);

74 socket_server-\>watch\[i\] = NULL;

75 }

76

77 dbus_free (socket_server-\>fds);

78 dbus_free (socket_server-\>watch);

79 dbus_free (socket_server-\>socket_name);

80 \_dbus_noncefile_delete (&socket_server-\>noncefile, NULL);

81 dbus_free (server);

82}

83

84/\* Return value is just for memory, not other failures. \*/

85static dbus_bool_t

86handle_new_client_fd_and_unlock (DBusServer \*server,

87 DBusSocket client_fd)

88{

89 DBusConnection \*connection;

90 DBusTransport \*transport;

91 DBusNewConnectionFunction new_connection_function;

92 void \*new_connection_data;

93

94 \_dbus_verbose ("Creating new client connection with fd %" DBUS_SOCKET_FORMAT "\n",

95 \_dbus_socket_printable (client_fd));

96

97 HAVE_LOCK_CHECK (server);

98

99 if (!\_dbus_set_socket_nonblocking (client_fd, NULL))

100 {

101 SERVER_UNLOCK (server);

102 return TRUE;

103 }

104

105 transport = \_dbus_transport_new_for_socket (client_fd, &server-\>guid_hex, NULL);

106 if (transport == NULL)

107 {

108 \_dbus_close_socket (&client_fd, NULL);

109 SERVER_UNLOCK (server);

110 return FALSE;

111 }

112

113 if (!\_dbus_transport_set_auth_mechanisms (transport,

114 (const char \*\*) server-\>auth_mechanisms))

115 {

116 \_dbus_transport_unref (transport);

117 SERVER_UNLOCK (server);

118 return FALSE;

119 }

120

121 /\* note that client_fd is now owned by the transport, and will be

122 \* closed on transport disconnection/finalization

123 \*/

124

125 connection = \_dbus_connection_new_for_transport (transport);

126 \_dbus_transport_unref (transport);

127 transport = NULL; /\* now under the connection lock \*/

128

129 if (connection == NULL)

130 {

131 SERVER_UNLOCK (server);

132 return FALSE;

133 }

134

135 /\* See if someone wants to handle this new connection, self-referencing

136 \* for paranoia.

137 \*/

138 new_connection_function = server-\>new_connection_function;

139 new_connection_data = server-\>new_connection_data;

140

141 \_dbus_server_ref_unlocked (server);

142 SERVER_UNLOCK (server);

143

144 if (new_connection_function)

145 {

146 (\* new_connection_function) (server, connection,

147 new_connection_data);

148 }

149 dbus_server_unref (server);

150

151 /\* If no one grabbed a reference, the connection will die. \*/

152 \_dbus_connection_close_if_only_one_ref (connection);

153 dbus_connection_unref (connection);

154

155 return TRUE;

156}

157

158static dbus_bool_t

159socket_handle_watch (DBusWatch \*watch,

160 unsigned int flags,

161 void \*data)

162{

163 DBusServer \*server = data;

164 DBusServerSocket \*socket_server = data;

165

166\#ifndef DBUS_DISABLE_ASSERT

167 int i;

168 dbus_bool_t found = FALSE;

169\#endif

170

171 SERVER_LOCK (server);

172

173\#ifndef DBUS_DISABLE_ASSERT

174 for (i = 0 ; i \< socket_server-\>n_fds ; i++)

175 {

176 if (socket_server-\>watch\[i\] == watch)

177 {

178 found = TRUE;

179 break;

180 }

181 }

182 \_dbus_assert (found);

183\#endif

184

185 \_dbus_verbose ("Handling client connection, flags 0x%x\n", flags);

186

187 if (flags & DBUS_WATCH_READABLE)

188 {

189 DBusSocket client_fd;

190 DBusSocket listen_fd;

191 int saved_errno;

192

193 listen_fd = \_dbus_watch_get_socket (watch);

194

195 if (socket_server-\>noncefile)

196 client_fd = \_dbus_accept_with_noncefile (listen_fd, socket_server-\>noncefile);

197 else

198 client_fd = \_dbus_accept (listen_fd);

199

200 saved_errno = \_dbus_save_socket_errno ();

201

202 if (!\_dbus_socket_is_valid (client_fd))

203 {

204 /\* EINTR handled for us \*/

205

206 if (\_dbus_get_is_errno_eagain_or_ewouldblock (saved_errno))

207 \_dbus_verbose ("No client available to accept after all\n");

208 else

209 \_dbus_verbose ("Failed to accept a client connection: %s\n",

210 \_dbus_strerror (saved_errno));

211

212 SERVER_UNLOCK (server);

213 }

214 else

215 {

216 if (!handle_new_client_fd_and_unlock (server, client_fd))

217 \_dbus_verbose ("Rejected client connection due to lack of memory\n");

218 }

219 }

220

221 if (flags & DBUS_WATCH_ERROR)

222 \_dbus_verbose ("Error on server listening socket\n");

223

224 if (flags & DBUS_WATCH_HANGUP)

225 \_dbus_verbose ("Hangup on server listening socket\n");

226

227 return TRUE;

228}

229

230static void

231socket_disconnect (DBusServer \*server)

232{

233 DBusServerSocket \*socket_server = (DBusServerSocket\*) server;

234 int i;

235

236 HAVE_LOCK_CHECK (server);

237

238 for (i = 0 ; i \< socket_server-\>n_fds ; i++)

239 {

240 if (socket_server-\>watch\[i\])

241 {

242 \_dbus_server_remove_watch (server,

243 socket_server-\>watch\[i\]);

244 \_dbus_watch_invalidate (socket_server-\>watch\[i\]);

245 \_dbus_watch_unref (socket_server-\>watch\[i\]);

246 socket_server-\>watch\[i\] = NULL;

247 }

248

249 if (\_dbus_socket_is_valid (socket_server-\>fds\[i\]))

250 \_dbus_close_socket (&socket_server-\>fds\[i\], NULL);

251 }

252

253 if (socket_server-\>socket_name != NULL)

254 {

255 DBusString tmp;

256 \_dbus_string_init_const (&tmp, socket_server-\>socket_name);

257 \_dbus_delete_file (&tmp, NULL);

258 }

259

260 if (server-\>published_address)

261 \_dbus_daemon_unpublish_session_bus_address();

262

263 HAVE_LOCK_CHECK (server);

264}

265

266static const DBusServerVTable socket_vtable = {

267 socket_finalize,

268 socket_disconnect

269};

270

287DBusServer\*

288\_dbus_server_new_for_socket (DBusSocket \*fds,

289 int n_fds,

290 const DBusString \*address,

291 DBusNonceFile \*noncefile,

292 DBusError \*error)

293{

294 DBusServerSocket \*socket_server;

295 DBusServer \*server;

296 int i;

297

298 socket_server = dbus_new0 (DBusServerSocket, 1);

299 if (socket_server == NULL)

300 goto failed;

301

302 socket_server-\>noncefile = noncefile;

303

304 socket_server-\>fds = dbus_new (DBusSocket, n_fds);

305 if (!socket_server-\>fds)

306 goto failed;

307

308 socket_server-\>watch = dbus_new0 (DBusWatch \*, n_fds);

309 if (!socket_server-\>watch)

310 goto failed;

311

312 for (i = 0 ; i \< n_fds ; i++)

313 {

314 DBusWatch \*watch;

315

316 watch = \_dbus_watch_new (\_dbus_socket_get_pollable (fds\[i\]),

317 DBUS_WATCH_READABLE,

318 TRUE,

319 socket_handle_watch, socket_server,

320 NULL);

321 if (watch == NULL)

322 goto failed;

323

324 socket_server-\>n_fds++;

325 socket_server-\>fds\[i\] = fds\[i\];

326 socket_server-\>watch\[i\] = watch;

327 }

328

329 if (!\_dbus_server_init_base (&socket_server-\>base,

330 &socket_vtable, address,

331 error))

332 goto failed;

333

334 server = (DBusServer\*)socket_server;

335

336 SERVER_LOCK (server);

337

338 for (i = 0 ; i \< n_fds ; i++)

339 {

340 if (!\_dbus_server_add_watch (&socket_server-\>base,

341 socket_server-\>watch\[i\]))

342 {

343 int j;

344

345 /\* The caller is still responsible for closing the fds until

346 \* we return successfully, so don't let socket_disconnect()

347 \* close them \*/

348 for (j = 0; j \< n_fds; j++)

349 \_dbus_socket_invalidate (&socket_server-\>fds\[j\]);

350

351 /\* socket_disconnect() will try to remove all the watches;

352 \* make sure it doesn't see the ones that weren't even added

353 \* yet \*/

354 for (j = i; j \< n_fds; j++)

355 {

356 \_dbus_watch_invalidate (socket_server-\>watch\[j\]);

357 \_dbus_watch_unref (socket_server-\>watch\[j\]);

358 socket_server-\>watch\[j\] = NULL;

359 }

360

361 \_dbus_server_disconnect_unlocked (server);

362 SERVER_UNLOCK (server);

363 \_dbus_server_finalize_base (&socket_server-\>base);

364 goto failed;

365 }

366 }

367

368 SERVER_UNLOCK (server);

369

370 \_dbus_server_trace_ref (&socket_server-\>base, 0, 1, "new_for_socket");

371 return (DBusServer\*) socket_server;

372

373failed:

374 if (socket_server != NULL)

375 {

376 if (socket_server-\>watch != NULL)

377 {

378 for (i = 0; i \< n_fds; i++)

379 {

380 if (socket_server-\>watch\[i\] != NULL)

381 {

382 \_dbus_watch_invalidate (socket_server-\>watch\[i\]);

383 \_dbus_watch_unref (socket_server-\>watch\[i\]);

384 socket_server-\>watch\[i\] = NULL;

385 }

386 }

387 }

388

389 dbus_free (socket_server-\>watch);

390 dbus_free (socket_server-\>fds);

391 dbus_free (socket_server);

392 }

393

394 if (error != NULL && !dbus_error_is_set (error))

395 \_DBUS_SET_OOM (error);

396

397 return NULL;

398}

399

419DBusServer\*

420\_dbus_server_new_for_tcp_socket (const char \*host,

421 const char \*bind,

422 const char \*port,

423 const char \*family,

424 DBusError \*error,

425 dbus_bool_t use_nonce)

426{

427 DBusServer \*server = NULL;

428 DBusSocket \*listen_fds = NULL;

429 int nlisten_fds = 0, i;

430 DBusString address = \_DBUS_STRING_INIT_INVALID;

431 DBusString host_str; /\* Initialized as const later, not freed \*/

432 DBusString port_str = \_DBUS_STRING_INIT_INVALID;

433 DBusNonceFile \*noncefile = NULL;

434 const char \*family_used = NULL;

435

436 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

437

438 if (!\_dbus_string_init (&address))

439 {

440 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

441 goto failed;

442 }

443

444 if (!\_dbus_string_init (&port_str))

445 {

446 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

447 goto failed;

448 }

449

450 if (host == NULL)

451 host = "localhost";

452

453 if (port == NULL)

454 port = "0";

455

456 if (bind == NULL)

457 bind = host;

458 else if (strcmp (bind, "\*") == 0)

459 bind = NULL;

460

461 nlisten_fds =\_dbus_listen_tcp_socket (bind, port, family,

462 &port_str,

463 &family_used,

464 &listen_fds, error);

465 if (nlisten_fds \<= 0)

466 {

467 \_DBUS_ASSERT_ERROR_IS_SET(error);

468 goto failed;

469 }

470

471 \_dbus_string_init_const (&host_str, host);

472 if (!\_dbus_string_append (&address, use_nonce ? "nonce-tcp:host=" : "tcp:host=") \|\|

473 !\_dbus_address_append_escaped (&address, &host_str) \|\|

474 !\_dbus_string_append (&address, ",port=") \|\|

475 !\_dbus_string_append (&address, \_dbus_string_get_const_data(&port_str)))

476 {

477 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

478 goto failed;

479 }

480 if (family_used &&

481 (!\_dbus_string_append (&address, ",family=") \|\|

482 !\_dbus_string_append (&address, family_used)))

483 {

484 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

485 goto failed;

486 }

487

488 if (use_nonce)

489 {

490 if (!\_dbus_noncefile_create (&noncefile, error))

491 goto failed;

492

493 if (!\_dbus_string_append (&address, ",noncefile=") \|\|

494 !\_dbus_address_append_escaped (&address, \_dbus_noncefile_get_path (noncefile)))

495 {

496 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

497 goto failed;

498 }

499 }

500

501 server = \_dbus_server_new_for_socket (listen_fds, nlisten_fds, &address, noncefile, error);

502 if (server == NULL)

503 goto failed;

504

505 /\* server has taken ownership of noncefile and the fds in listen_fds \*/

506 \_dbus_string_free (&port_str);

507 \_dbus_string_free (&address);

508 dbus_free(listen_fds);

509

510 return server;

511

512failed:

513 \_dbus_noncefile_delete (&noncefile, NULL);

514

515 if (listen_fds != NULL)

516 {

517 for (i = 0; i \< nlisten_fds; i++)

518 \_dbus_close_socket (&listen_fds\[i\], NULL);

519 dbus_free (listen_fds);

520 }

521

522 \_dbus_string_free (&port_str);

523 \_dbus_string_free (&address);

524 return NULL;

525}

526

539DBusServerListenResult

540\_dbus_server_listen_socket (DBusAddressEntry \*entry,

541 DBusServer \*\*server_p,

542 DBusError \*error)

543{

544 const char \*method;

545

546 \*server_p = NULL;

547

548 method = dbus_address_entry_get_method (entry);

549

550 if (strcmp (method, "tcp") == 0 \|\| strcmp (method, "nonce-tcp") == 0)

551 {

552 const char \*host;

553 const char \*port;

554 const char \*bind;

555 const char \*family;

556

557 host = dbus_address_entry_get_value (entry, "host");

558 bind = dbus_address_entry_get_value (entry, "bind");

559 port = dbus_address_entry_get_value (entry, "port");

560 family = dbus_address_entry_get_value (entry, "family");

561

562 \*server_p = \_dbus_server_new_for_tcp_socket (host, bind, port,

563 family, error, strcmp (method, "nonce-tcp") == 0 ? TRUE : FALSE);

564

565 if (\*server_p)

566 {

567 \_DBUS_ASSERT_ERROR_IS_CLEAR(error);

568 return DBUS_SERVER_LISTEN_OK;

569 }

570 else

571 {

572 \_DBUS_ASSERT_ERROR_IS_SET(error);

573 return DBUS_SERVER_LISTEN_DID_NOT_CONNECT;

574 }

575 }

576 else

577 {

578 \_DBUS_ASSERT_ERROR_IS_CLEAR(error);

579 return DBUS_SERVER_LISTEN_NOT_HANDLED;

580 }

581}

582

592void

593\_dbus_server_socket_own_filename (DBusServer \*server,

594 char \*filename)

595{

596 DBusServerSocket \*socket_server = (DBusServerSocket\*) server;

597

598 socket_server-\>socket_name = filename;

599}

600

609DBusServer\*

610\_dbus_server_new_for_domain_socket (const char \*path,

611 dbus_bool_t abstract,

612 DBusError \*error)

613{

614 DBusServer \*server;

615 DBusSocket listen_fd;

616 DBusString address;

617 char \*path_copy;

618 DBusString path_str;

619

620 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

621

622 if (!\_dbus_string_init (&address))

623 {

624 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

625 return NULL;

626 }

627

628 \_dbus_string_init_const (&path_str, path);

629 if ((abstract &&

630 !\_dbus_string_append (&address, "unix:abstract=")) \|\|

631 (!abstract &&

632 !\_dbus_string_append (&address, "unix:path=")) \|\|

633 !\_dbus_address_append_escaped (&address, &path_str))

634 {

635 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

636 goto failed_0;

637 }

638

639 if (abstract)

640 {

641 path_copy = NULL;

642 }

643 else

644 {

645 path_copy = \_dbus_strdup (path);

646 if (path_copy == NULL)

647 {

648 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

649 goto failed_0;

650 }

651 }

652

653 listen_fd = \_dbus_listen_unix_socket (path, abstract, error);

654

655 if (!\_dbus_socket_is_valid (listen_fd))

656 {

657 \_DBUS_ASSERT_ERROR_IS_SET (error);

658 goto failed_1;

659 }

660

661 server = \_dbus_server_new_for_socket (&listen_fd, 1, &address, 0, error);

662 if (server == NULL)

663 {

664 goto failed_2;

665 }

666

667 if (path_copy != NULL)

668 \_dbus_server_socket_own_filename(server, path_copy);

669

670 \_dbus_string_free (&address);

671

672 return server;

673

674 failed_2:

675 \_dbus_close_socket (&listen_fd, NULL);

676 failed_1:

677 dbus_free (path_copy);

678 failed_0:

679 \_dbus_string_free (&address);

680

681 return NULL;

682}

683

692static DBusServer \*

693\_dbus_server_new_for_dir (const char \*dir,

694 DBusError \*error)

695{

696 DBusServer \*server;

697 DBusString full_path;

698 DBusString filename;

699

700 if (!\_dbus_string_init (&full_path))

701 {

702 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

703 return NULL;

704 }

705

706 if (!\_dbus_string_init (&filename))

707 {

708 \_dbus_string_free (&full_path);

709 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

710 return NULL;

711 }

712

713 if (!\_dbus_string_append (&filename, "dbus-"))

714 {

715 \_dbus_string_free (&full_path);

716 \_dbus_string_free (&filename);

717 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

718 return NULL;

719 }

720

721 if (!\_dbus_generate_random_ascii (&filename, 10, error))

722 {

723 \_dbus_string_free (&full_path);

724 \_dbus_string_free (&filename);

725 return NULL;

726 }

727

728 if (!\_dbus_string_append (&full_path, dir) \|\|

729 !\_dbus_concat_dir_and_file (&full_path, &filename))

730 {

731 \_dbus_string_free (&full_path);

732 \_dbus_string_free (&filename);

733 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

734 return NULL;

735 }

736

737 server =

738 \_dbus_server_new_for_domain_socket (\_dbus_string_get_const_data (&full_path),

739 FALSE, /\* not abstract \*/

740 error);

741

742 \_dbus_string_free (&full_path);

743 \_dbus_string_free (&filename);

744

745 return server;

746}

747

760DBusServerListenResult

761\_dbus_server_listen_unix_socket (DBusAddressEntry \*entry,

762 DBusServer \*\*server_p,

763 DBusError \*error)

764{

765 const char \*method;

766

767 \*server_p = NULL;

768

769 method = dbus_address_entry_get_method (entry);

770

771 if (strcmp (method, "unix") == 0)

772 {

773 const char \*path = dbus_address_entry_get_value (entry, "path");

774 const char \*dir = dbus_address_entry_get_value (entry, "dir");

775 const char \*tmpdir = dbus_address_entry_get_value (entry, "tmpdir");

776 const char \*abstract = dbus_address_entry_get_value (entry, "abstract");

777 const char \*runtime = dbus_address_entry_get_value (entry, "runtime");

778 int mutually_exclusive_modes = 0;

779

780 mutually_exclusive_modes = (path != NULL) + (tmpdir != NULL) +

781 (abstract != NULL) + (runtime != NULL) + (dir != NULL);

782

783 if (mutually_exclusive_modes \< 1)

784 {

785 \_dbus_set_bad_address(error, "unix",

786 "path or tmpdir or abstract or runtime or dir",

787 NULL);

788 return DBUS_SERVER_LISTEN_BAD_ADDRESS;

789 }

790

791 if (mutually_exclusive_modes \> 1)

792 {

793 \_dbus_set_bad_address(error, NULL, NULL,

794 "cannot specify two of \\path\\, \\tmpdir\\, \\abstract\\, \\runtime\\ and \\dir\\ at the same time");

795 return DBUS_SERVER_LISTEN_BAD_ADDRESS;

796 }

797

798 if (runtime != NULL)

799 {

800 DBusString full_path;

801 DBusString filename;

802 const char \*runtimedir;

803

804 if (strcmp (runtime, "yes") != 0)

805 {

806 \_dbus_set_bad_address(error, NULL, NULL,

807 "if given, the only value allowed for \\runtime\\ is \\yes\\");

808 return DBUS_SERVER_LISTEN_BAD_ADDRESS;

809 }

810

811 runtimedir = \_dbus_getenv ("XDG_RUNTIME_DIR");

812

813 if (runtimedir == NULL)

814 {

815 dbus_set_error (error,

816 DBUS_ERROR_NOT_SUPPORTED, "\\XDG_RUNTIME_DIR\\ is not set");

817 return DBUS_SERVER_LISTEN_DID_NOT_CONNECT;

818 }

819

820 \_dbus_string_init_const (&filename, "bus");

821

822 if (!\_dbus_string_init (&full_path))

823 {

824 \_DBUS_SET_OOM (error);

825 return DBUS_SERVER_LISTEN_DID_NOT_CONNECT;

826 }

827

828 if (!\_dbus_string_append (&full_path, runtimedir) \|\|

829 !\_dbus_concat_dir_and_file (&full_path, &filename))

830 {

831 \_dbus_string_free (&full_path);

832 \_DBUS_SET_OOM (error);

833 return DBUS_SERVER_LISTEN_DID_NOT_CONNECT;

834 }

835

836 /\* We can safely use filesystem sockets in the runtime directory,

837 \* and they are preferred because they can be bind-mounted between

838 \* Linux containers. \*/

839 \*server_p = \_dbus_server_new_for_domain_socket (

840 \_dbus_string_get_const_data (&full_path),

841 FALSE, error);

842

843 \_dbus_string_free (&full_path);

844 }

845 else if (tmpdir != NULL \|\| dir != NULL)

846 {

847 /\* tmpdir is now equivalent to dir. Previously it would try to

848 \* use an abstract socket. \*/

849 if (tmpdir != NULL)

850 dir = tmpdir;

851

852 \*server_p = \_dbus_server_new_for_dir (dir, error);

853 }

854 else

855 {

856 if (path)

857 \*server_p = \_dbus_server_new_for_domain_socket (path, FALSE, error);

858 else

859 \*server_p = \_dbus_server_new_for_domain_socket (abstract, TRUE, error);

860 }

861

862 if (\*server_p != NULL)

863 {

864 \_DBUS_ASSERT_ERROR_IS_CLEAR(error);

865 return DBUS_SERVER_LISTEN_OK;

866 }

867 else

868 {

869 \_DBUS_ASSERT_ERROR_IS_SET(error);

870 return DBUS_SERVER_LISTEN_DID_NOT_CONNECT;

871 }

872 }

873 else

874 {

875 /\* If we don't handle the method, we return NULL with the

876 \* error unset

877 \*/

878 \_DBUS_ASSERT_ERROR_IS_CLEAR(error);

879 return DBUS_SERVER_LISTEN_NOT_HANDLED;

880 }

881}

882

883

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

\_dbus_connection_new_for_transport

DBusConnection \* \_dbus_connection_new_for_transport(DBusTransport \*transport)

Creates a new connection for the given transport.

**Definition** dbus-connection.c:1253

\_dbus_connection_close_if_only_one_ref

void \_dbus_connection_close_if_only_one_ref(DBusConnection \*connection)

Used internally to handle the semantics of dbus_server_set_new_connection_function().

**Definition** dbus-connection.c:2160

dbus_connection_unref

void dbus_connection_unref(DBusConnection \*connection)

Decrements the reference count of a DBusConnection, and finalizes it if the count reaches zero.

**Definition** dbus-connection.c:2832

DBUS_WATCH_READABLE

@ DBUS_WATCH_READABLE

As in POLLIN.

**Definition** dbus-connection.h:63

DBUS_WATCH_HANGUP

@ DBUS_WATCH_HANGUP

As in POLLHUP (can't watch for it, but can be present in current state passed to dbus_watch_handle())...

**Definition** dbus-connection.h:70

DBUS_WATCH_ERROR

@ DBUS_WATCH_ERROR

As in POLLERR (can't watch for this, but can be present in current state passed to dbus_watch_handle(...

**Definition** dbus-connection.h:65

dbus_set_error

void dbus_set_error(DBusError \*error, const char \*name, const char \*format,...)

Assigns an error name and message to a DBusError.

**Definition** dbus-errors.c:356

dbus_error_is_set

dbus_bool_t dbus_error_is_set(const DBusError \*error)

Checks whether an error occurred (the error is set).

**Definition** dbus-errors.c:331

\_dbus_delete_file

dbus_bool_t \_dbus_delete_file(const DBusString \*filename, DBusError \*error)

Deletes the given file.

**Definition** dbus-file-unix.c:441

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_dbus_strdup

char \* \_dbus_strdup(const char \*str)

Duplicates a string.

**Definition** dbus-internals.c:621

\_dbus_generate_random_ascii

dbus_bool_t \_dbus_generate_random_ascii(DBusString \*str, int n_bytes, DBusError \*error)

Generates the given number of random bytes, where the bytes are chosen from the alphanumeric ASCII su...

**Definition** dbus-sysdeps.c:525

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

dbus_new

\#define dbus_new(type, count)

Safe macro for using dbus_malloc().

**Definition** dbus-memory.h:59

dbus_new0

\#define dbus_new0(type, count)

Safe macro for using dbus_malloc0().

**Definition** dbus-memory.h:60

DBUS_ERROR_NOT_SUPPORTED

\#define DBUS_ERROR_NOT_SUPPORTED

Requested operation isn't supported (like ENOSYS on UNIX).

**Definition** dbus-protocol.h:375

DBUS_ERROR_NO_MEMORY

\#define DBUS_ERROR_NO_MEMORY

There was not enough memory to complete an operation.

**Definition** dbus-protocol.h:363

\_dbus_server_add_watch

dbus_bool_t \_dbus_server_add_watch(DBusServer \*server, DBusWatch \*watch)

Adds a watch for this server, chaining out to application-provided watch handlers.

**Definition** dbus-server.c:297

\_dbus_server_remove_watch

void \_dbus_server_remove_watch(DBusServer \*server, DBusWatch \*watch)

Removes a watch previously added with \_dbus_server_remove_watch().

**Definition** dbus-server.c:313

\_dbus_server_init_base

dbus_bool_t \_dbus_server_init_base(DBusServer \*server, const DBusServerVTable \*vtable, const DBusString \*address, DBusError \*error)

Initializes the members of the DBusServer base class.

**Definition** dbus-server.c:113

\_dbus_server_finalize_base

void \_dbus_server_finalize_base(DBusServer \*server)

Finalizes the members of the DBusServer base class.

**Definition** dbus-server.c:202

\_dbus_server_ref_unlocked

DBUS_PRIVATE_EXPORT void \_dbus_server_ref_unlocked(DBusServer \*server)

Like dbus_server_ref() but does not acquire the lock (must already be held)

**Definition** dbus-server.c:457

\_dbus_server_new_for_domain_socket

DBusServer \* \_dbus_server_new_for_domain_socket(const char \*path, dbus_bool_t abstract, DBusError \*error)

Creates a new server listening on the given Unix domain socket.

**Definition** dbus-server-socket.c:610

\_dbus_server_new_for_tcp_socket

DBusServer \* \_dbus_server_new_for_tcp_socket(const char \*host, const char \*bind, const char \*port, const char \*family, DBusError \*error, dbus_bool_t use_nonce)

Creates a new server listening on TCP.

**Definition** dbus-server-socket.c:420

\_dbus_server_new_for_socket

DBusServer \* \_dbus_server_new_for_socket(DBusSocket \*fds, int n_fds, const DBusString \*address, DBusNonceFile \*noncefile, DBusError \*error)

Creates a new server listening on the given file descriptor.

**Definition** dbus-server-socket.c:288

\_dbus_server_listen_socket

DBusServerListenResult \_dbus_server_listen_socket(DBusAddressEntry \*entry, DBusServer \*\*server_p, DBusError \*error)

Tries to interpret the address entry for various socket-related addresses (well, currently only tcp a...

**Definition** dbus-server-socket.c:540

\_dbus_server_listen_unix_socket

DBusServerListenResult \_dbus_server_listen_unix_socket(DBusAddressEntry \*entry, DBusServer \*\*server_p, DBusError \*error)

Tries to interpret the address entry for UNIX socket addresses.

**Definition** dbus-server-socket.c:761

\_dbus_server_socket_own_filename

void \_dbus_server_socket_own_filename(DBusServer \*server, char \*filename)

This is a bad hack since it's really unix domain socket specific.

**Definition** dbus-server-socket.c:593

dbus_server_unref

void dbus_server_unref(DBusServer \*server)

Decrements the reference count of a DBusServer.

**Definition** dbus-server.c:735

DBusNewConnectionFunction

void(\* DBusNewConnectionFunction)(DBusServer \*server, DBusConnection \*new_connection, void \*data)

Called when a new connection to the server is available.

**Definition** dbus-server.h:50

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

\_dbus_string_get_const_data

const char \* \_dbus_string_get_const_data(const DBusString \*str)

Gets the raw character buffer from a const string.

**Definition** dbus-string.c:513

\_dbus_get_is_errno_eagain_or_ewouldblock

dbus_bool_t \_dbus_get_is_errno_eagain_or_ewouldblock(int e)

See if errno is EAGAIN or EWOULDBLOCK (this has to be done differently for Winsock so is abstracted)

**Definition** dbus-sysdeps-unix.c:4801

\_dbus_getenv

const char \* \_dbus_getenv(const char \*varname)

Wrapper for getenv().

**Definition** dbus-sysdeps.c:197

\_dbus_listen_unix_socket

DBusSocket \_dbus_listen_unix_socket(const char \*path, dbus_bool_t abstract, DBusError \*error)

Creates a socket and binds it to the given path, then listens on the socket.

**Definition** dbus-sysdeps-unix.c:1170

\_dbus_set_socket_nonblocking

dbus_bool_t \_dbus_set_socket_nonblocking(DBusSocket fd, DBusError \*error)

Sets a file descriptor to be nonblocking.

**Definition** dbus-sysdeps-unix.c:3797

\_dbus_listen_tcp_socket

int \_dbus_listen_tcp_socket(const char \*host, const char \*port, const char \*family, DBusString \*retport, const char \*\*retfamily, DBusSocket \*\*fds_p, DBusError \*error)

Creates a socket and binds it to the given path, then listens on the socket.

**Definition** dbus-sysdeps-unix.c:1606

\_dbus_close_socket

dbus_bool_t \_dbus_close_socket(DBusSocket \*fd, DBusError \*error)

Closes a socket and invalidates it.

**Definition** dbus-sysdeps-unix.c:314

\_dbus_concat_dir_and_file

dbus_bool_t \_dbus_concat_dir_and_file(DBusString \*dir, const DBusString \*next_component)

Appends the given filename to the given directory.

**Definition** dbus-sysdeps-unix.c:3497

\_dbus_accept

DBusSocket \_dbus_accept(DBusSocket listen_fd)

Accepts a connection on a listening socket.

**Definition** dbus-sysdeps-unix.c:2589

\_dbus_transport_new_for_socket

DBusTransport \* \_dbus_transport_new_for_socket(DBusSocket fd, const DBusString \*server_guid, const DBusString \*address)

Creates a new transport for the given socket file descriptor.

**Definition** dbus-transport-socket.c:1295

\_dbus_transport_set_auth_mechanisms

dbus_bool_t \_dbus_transport_set_auth_mechanisms(DBusTransport \*transport, const char \*\*mechanisms)

Sets the SASL authentication mechanisms supported by this transport.

**Definition** dbus-transport.c:1565

\_dbus_transport_unref

void \_dbus_transport_unref(DBusTransport \*transport)

Decrements the reference count for the transport.

**Definition** dbus-transport.c:486

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

DBusAddressEntry

Internals of DBusAddressEntry.

**Definition** dbus-address.c:49

DBusConnection

Implementation details of DBusConnection.

**Definition** dbus-connection.c:259

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusNonceFile

**Definition** dbus-nonce.c:36

DBusServerSocket

Implementation details of DBusServerSocket.

**Definition** dbus-server-socket.c:53

DBusServerSocket::n_fds

int n_fds

Number of active file handles.

**Definition** dbus-server-socket.c:55

DBusServerSocket::fds

DBusSocket \* fds

File descriptor or DBUS_SOCKET_INVALID if disconnected.

**Definition** dbus-server-socket.c:56

DBusServerSocket::noncefile

DBusNonceFile \* noncefile

Nonce file used to authenticate clients.

**Definition** dbus-server-socket.c:59

DBusServerSocket::watch

DBusWatch \*\* watch

File descriptor watch.

**Definition** dbus-server-socket.c:57

DBusServerSocket::base

DBusServer base

Parent class members.

**Definition** dbus-server-socket.c:54

DBusServerSocket::socket_name

char \* socket_name

Name of domain socket, to unlink if appropriate.

**Definition** dbus-server-socket.c:58

DBusServerVTable

Virtual table to be implemented by all server "subclasses".

**Definition** dbus-server-protected.h:46

DBusServer

Internals of DBusServer object.

**Definition** dbus-server-protected.h:59

DBusServer::published_address

dbus_bool_t published_address

flag which indicates that server has published its bus address.

**Definition** dbus-server-protected.h:72

DBusServer::guid_hex

DBusString guid_hex

Hex-encoded version of GUID.

**Definition** dbus-server-protected.h:66

DBusServer::new_connection_function

DBusNewConnectionFunction new_connection_function

Callback to invoke when a new connection is created.

**Definition** dbus-server-protected.h:78

DBusServer::new_connection_data

void \* new_connection_data

Data for new connection callback.

**Definition** dbus-server-protected.h:80

DBusServer::auth_mechanisms

char \*\* auth_mechanisms

Array of allowed authentication mechanisms.

**Definition** dbus-server-protected.h:87

DBusSocket

Socket interface.

**Definition** dbus-sysdeps.h:185

DBusString

**Definition** dbus-string.h:47

DBusTransport

Object representing a transport such as a socket.

**Definition** dbus-transport-protected.h:83

DBusWatch

Implementation of DBusWatch.

**Definition** dbus-watch.c:43
