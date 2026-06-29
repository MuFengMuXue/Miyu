dbus-transport.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-transport.c DBusTransport object (internal to D-Bus implementation)

3 \*

4 \* Copyright (C) 2002, 2003 Red Hat Inc.

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

27\#include "dbus-transport-protected.h"

28\#include "dbus-transport-unix.h"

29\#include "dbus-transport-socket.h"

30\#include "dbus-connection-internal.h"

31\#include "dbus-watch.h"

32\#include "dbus-auth.h"

33\#include "dbus-address.h"

34\#include "dbus-credentials.h"

35\#include "dbus-mainloop.h"

36\#include "dbus-message.h"

37\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

38\#include "dbus-server-debug-pipe.h"

39\#endif

40

62static void

63live_messages_notify (DBusCounter \*counter,

64 void \*user_data)

65{

66 DBusTransport \*transport = user_data;

67

68 \_dbus_connection_lock (transport-\>connection);

69 \_dbus_transport_ref (transport);

70

71\#if 0

72 \_dbus_verbose ("Size counter value is now %d\n",

73 (int) \_dbus_counter_get_size_value (counter));

74 \_dbus_verbose ("Unix FD counter value is now %d\n",

75 (int) \_dbus_counter_get_unix_fd_value (counter));

76\#endif

77

78 /\* disable or re-enable the read watch for the transport if

79 \* required.

80 \*/

81 if (transport-\>vtable-\>live_messages_changed)

82 {

83 (\* transport-\>vtable-\>live_messages_changed) (transport);

84 }

85

86 \_dbus_transport_unref (transport);

87 \_dbus_connection_unlock (transport-\>connection);

88}

89

103dbus_bool_t

104\_dbus_transport_init_base (DBusTransport \*transport,

105 const DBusTransportVTable \*vtable,

106 const DBusString \*server_guid,

107 const DBusString \*address)

108{

109 DBusMessageLoader \*loader;

110 DBusAuth \*auth;

111 DBusCounter \*counter;

112 char \*address_copy;

113 DBusCredentials \*creds;

114

115 loader = \_dbus_message_loader_new ();

116 if (loader == NULL)

117 return FALSE;

118

119 if (server_guid)

120 auth = \_dbus_auth_server_new (server_guid);

121 else

122 auth = \_dbus_auth_client_new ();

123 if (auth == NULL)

124 {

125 \_dbus_message_loader_unref (loader);

126 return FALSE;

127 }

128

129 counter = \_dbus_counter_new ();

130 if (counter == NULL)

131 {

132 \_dbus_auth_unref (auth);

133 \_dbus_message_loader_unref (loader);

134 return FALSE;

135 }

136

137 creds = \_dbus_credentials_new ();

138 if (creds == NULL)

139 {

140 \_dbus_counter_unref (counter);

141 \_dbus_auth_unref (auth);

142 \_dbus_message_loader_unref (loader);

143 return FALSE;

144 }

145

146 if (server_guid)

147 {

148 \_dbus_assert (address == NULL);

149 address_copy = NULL;

150 }

151 else

152 {

153 \_dbus_assert (address != NULL);

154

155 if (!\_dbus_string_copy_data (address, &address_copy))

156 {

157 \_dbus_credentials_unref (creds);

158 \_dbus_counter_unref (counter);

159 \_dbus_auth_unref (auth);

160 \_dbus_message_loader_unref (loader);

161 return FALSE;

162 }

163 }

164

165 transport-\>refcount = 1;

166 transport-\>vtable = vtable;

167 transport-\>loader = loader;

168 transport-\>auth = auth;

169 transport-\>live_messages = counter;

170 transport-\>authenticated = FALSE;

171 transport-\>disconnected = FALSE;

172 transport-\>is_server = (server_guid != NULL);

173 transport-\>send_credentials_pending = !transport-\>is_server;

174 transport-\>receive_credentials_pending = transport-\>is_server;

175 transport-\>address = address_copy;

176

177 transport-\>unix_user_function = NULL;

178 transport-\>unix_user_data = NULL;

179 transport-\>free_unix_user_data = NULL;

180

181 transport-\>windows_user_function = NULL;

182 transport-\>windows_user_data = NULL;

183 transport-\>free_windows_user_data = NULL;

184

185 transport-\>expected_guid = NULL;

186

187 /\* Try to default to something that won't totally hose the system,

188 \* but doesn't impose too much of a limitation.

189 \*/

190 transport-\>max_live_messages_size = \_DBUS_ONE_MEGABYTE \* 63;

191

192 /\* On Linux RLIMIT_NOFILE defaults to 1024, so allowing 4096 fds live

193 should be more than enough \*/

194 transport-\>max_live_messages_unix_fds = 4096;

195

196 /\* credentials read from socket if any \*/

197 transport-\>credentials = creds;

198

199 \_dbus_counter_set_notify (transport-\>live_messages,

200 transport-\>max_live_messages_size,

201 transport-\>max_live_messages_unix_fds,

202 live_messages_notify,

203 transport);

204

205 if (transport-\>address)

206 \_dbus_verbose ("Initialized transport on address %s\n", transport-\>address);

207

208 return TRUE;

209}

210

217void

218\_dbus_transport_finalize_base (DBusTransport \*transport)

219{

220 if (!transport-\>disconnected)

221 \_dbus_transport_disconnect (transport);

222

223 if (transport-\>free_unix_user_data != NULL)

224 (\* transport-\>free_unix_user_data) (transport-\>unix_user_data);

225

226 if (transport-\>free_windows_user_data != NULL)

227 (\* transport-\>free_windows_user_data) (transport-\>windows_user_data);

228

229 \_dbus_message_loader_unref (transport-\>loader);

230 \_dbus_auth_unref (transport-\>auth);

231 \_dbus_counter_set_notify (transport-\>live_messages,

232 0, 0, NULL, NULL);

233 \_dbus_counter_unref (transport-\>live_messages);

234 dbus_free (transport-\>address);

235 dbus_free (transport-\>expected_guid);

236 if (transport-\>credentials)

237 \_dbus_credentials_unref (transport-\>credentials);

238}

239

240

251static DBusTransport\*

252check_address (const char \*address, DBusError \*error)

253{

254 DBusAddressEntry \*\*entries;

255 DBusTransport \*transport = NULL;

256 int len, i;

257

258 \_dbus_assert (address != NULL);

259 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

260

261 if (!dbus_parse_address (address, &entries, &len, error))

262 return NULL; /\* not a valid address \*/

263

264 for (i = 0; i \< len; i++)

265 {

266 dbus_error_free (error);

267 transport = \_dbus_transport_open (entries\[i\], error);

268

269 if (transport != NULL)

270 break;

271 }

272

273 dbus_address_entries_free (entries);

274 return transport;

275}

276

285static DBusTransport\*

286\_dbus_transport_new_for_autolaunch (const char \*scope, DBusError \*error)

287{

288 DBusString address;

289 DBusTransport \*result = NULL;

290

291 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

292

293 if (!\_dbus_string_init (&address))

294 {

295 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

296 return NULL;

297 }

298

299 if (!\_dbus_get_autolaunch_address (scope, &address, error))

300 {

301 \_DBUS_ASSERT_ERROR_IS_SET (error);

302 goto out;

303 }

304

305 result = check_address (\_dbus_string_get_const_data (&address), error);

306 \_DBUS_ASSERT_ERROR_XOR_BOOL (error, result != NULL);

307

308 out:

309 \_dbus_string_free (&address);

310 return result;

311}

312

313static DBusTransportOpenResult

314\_dbus_transport_open_autolaunch (DBusAddressEntry \*entry,

315 DBusTransport \*\*transport_p,

316 DBusError \*error)

317{

318 const char \*method;

319

320 method = dbus_address_entry_get_method (entry);

321 \_dbus_assert (method != NULL);

322

323 if (strcmp (method, "autolaunch") == 0)

324 {

325 const char \*scope = dbus_address_entry_get_value (entry, "scope");

326

327 \*transport_p = \_dbus_transport_new_for_autolaunch (scope, error);

328

329 if (\*transport_p == NULL)

330 {

331 \_DBUS_ASSERT_ERROR_IS_SET (error);

332 return DBUS_TRANSPORT_OPEN_DID_NOT_CONNECT;

333 }

334 else

335 {

336 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

337 return DBUS_TRANSPORT_OPEN_OK;

338 }

339 }

340 else

341 {

342 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

343 return DBUS_TRANSPORT_OPEN_NOT_HANDLED;

344 }

345}

346

347static const struct {

348 DBusTransportOpenResult (\* func) (DBusAddressEntry \*entry,

349 DBusTransport \*\*transport_p,

350 DBusError \*error);

351} open_funcs\[\] = {

352 { \_dbus_transport_open_socket },

353 { \_dbus_transport_open_unix_socket },

354\#ifndef \_WIN32

355 { \_dbus_transport_open_unixexec },

356\#endif

357 { \_dbus_transport_open_platform_specific },

358 { \_dbus_transport_open_autolaunch }

359\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

360 , { \_dbus_transport_open_debug_pipe }

361\#endif

362};

363

372DBusTransport\*

373\_dbus_transport_open (DBusAddressEntry \*entry,

374 DBusError \*error)

375{

376 DBusTransport \*transport;

377 const char \*expected_guid_orig;

378 char \*expected_guid;

379 int i;

380 DBusError tmp_error = DBUS_ERROR_INIT;

381

382 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

383

384 transport = NULL;

385 expected_guid_orig = dbus_address_entry_get_value (entry, "guid");

386 expected_guid = \_dbus_strdup (expected_guid_orig);

387

388 if (expected_guid_orig != NULL && expected_guid == NULL)

389 {

390 \_DBUS_SET_OOM (error);

391 return NULL;

392 }

393

394 for (i = 0; i \< (int) \_DBUS_N_ELEMENTS (open_funcs); ++i)

395 {

396 DBusTransportOpenResult result;

397

398 \_DBUS_ASSERT_ERROR_IS_CLEAR (&tmp_error);

399 result = (\* open_funcs\[i\].func) (entry, &transport, &tmp_error);

400

401 switch (result)

402 {

403 case DBUS_TRANSPORT_OPEN_OK:

404 \_DBUS_ASSERT_ERROR_IS_CLEAR (&tmp_error);

405 goto out;

406 break;

407 case DBUS_TRANSPORT_OPEN_NOT_HANDLED:

408 \_DBUS_ASSERT_ERROR_IS_CLEAR (&tmp_error);

409 /\* keep going through the loop of open funcs \*/

410 break;

411 case DBUS_TRANSPORT_OPEN_BAD_ADDRESS:

412 \_DBUS_ASSERT_ERROR_IS_SET (&tmp_error);

413 goto out;

414 break;

415 case DBUS_TRANSPORT_OPEN_DID_NOT_CONNECT:

416 \_DBUS_ASSERT_ERROR_IS_SET (&tmp_error);

417 goto out;

418 break;

419 default:

420 \_dbus_assert_not_reached ("invalid transport open result");

421 break;

422 }

423 }

424

425 out:

426

427 if (transport == NULL)

428 {

429 if (!dbus_error_is_set (&tmp_error))

430 \_dbus_set_bad_address (&tmp_error,

431 NULL, NULL,

432 "Unknown address type (examples of valid types are \\tcp\\ and on UNIX \\unix\\)");

433

434 \_DBUS_ASSERT_ERROR_IS_SET (&tmp_error);

435 dbus_move_error(&tmp_error, error);

436 dbus_free (expected_guid);

437 }

438 else

439 {

440 \_DBUS_ASSERT_ERROR_IS_CLEAR (&tmp_error);

441

442 /\* In the case of autostart the initial guid is NULL

443 \* and the autostart transport recursively calls

444 \* \_dbus_open_transport wich returns a transport

445 \* with a guid. That guid is the definitive one.

446 \*

447 \* FIXME: if more transports are added they may have

448 \* an effect on the expected_guid semantics (i.e.

449 \* expected_guid and transport-\>expected_guid may

450 \* both have values). This is very unlikely though

451 \* we should either throw asserts here for those

452 \* corner cases or refactor the code so it is

453 \* clearer on what is expected and what is not

454 \*/

455 if(expected_guid)

456 transport-\>expected_guid = expected_guid;

457 }

458

459 return transport;

460}

461

468DBusTransport \*

469\_dbus_transport_ref (DBusTransport \*transport)

470{

471 \_dbus_assert (transport-\>refcount \> 0);

472

473 transport-\>refcount += 1;

474

475 return transport;

476}

477

485void

486\_dbus_transport_unref (DBusTransport \*transport)

487{

488 \_dbus_assert (transport != NULL);

489 \_dbus_assert (transport-\>refcount \> 0);

490

491 transport-\>refcount -= 1;

492 if (transport-\>refcount == 0)

493 {

494 \_dbus_verbose ("finalizing\n");

495

496 \_dbus_assert (transport-\>vtable-\>finalize != NULL);

497

498 (\* transport-\>vtable-\>finalize) (transport);

499 }

500}

501

510void

511\_dbus_transport_disconnect (DBusTransport \*transport)

512{

513 \_dbus_verbose ("start\n");

514

515 \_dbus_assert (transport-\>vtable-\>disconnect != NULL);

516

517 if (transport-\>disconnected)

518 return;

519

520 (\* transport-\>vtable-\>disconnect) (transport);

521

522 transport-\>disconnected = TRUE;

523

524 \_dbus_verbose ("end\n");

525}

526

535dbus_bool_t

536\_dbus_transport_get_is_connected (DBusTransport \*transport)

537{

538 return !transport-\>disconnected;

539}

540

541static dbus_bool_t

542auth_via_unix_user_function (DBusTransport \*transport)

543{

544 DBusCredentials \*auth_identity;

545 dbus_bool_t allow;

546 DBusConnection \*connection;

547 DBusAllowUnixUserFunction unix_user_function;

548 void \*unix_user_data;

549 dbus_uid_t uid;

550

551 /\* Dropping the lock here probably isn't that safe. \*/

552

553 auth_identity = \_dbus_auth_get_identity (transport-\>auth);

554 \_dbus_assert (auth_identity != NULL);

555

556 connection = transport-\>connection;

557 unix_user_function = transport-\>unix_user_function;

558 unix_user_data = transport-\>unix_user_data;

559 uid = \_dbus_credentials_get_unix_uid (auth_identity);

560

561 \_dbus_verbose ("unlock\n");

562 \_dbus_connection_unlock (connection);

563

564 allow = (\* unix_user_function) (connection,

565 uid,

566 unix_user_data);

567

568 \_dbus_verbose ("lock post unix user function\n");

569 \_dbus_connection_lock (connection);

570

571 if (allow)

572 {

573 \_dbus_verbose ("Client UID "DBUS_UID_FORMAT" authorized\n", uid);

574 }

575 else

576 {

577 \_dbus_verbose ("Client UID "DBUS_UID_FORMAT

578 " was rejected, disconnecting\n",

579 \_dbus_credentials_get_unix_uid (auth_identity));

580 \_dbus_transport_disconnect (transport);

581 }

582

583 return allow;

584}

585

586static dbus_bool_t

587auth_via_windows_user_function (DBusTransport \*transport)

588{

589 DBusCredentials \*auth_identity;

590 dbus_bool_t allow;

591 DBusConnection \*connection;

592 DBusAllowWindowsUserFunction windows_user_function;

593 void \*windows_user_data;

594 char \*windows_sid;

595

596 /\* Dropping the lock here probably isn't that safe. \*/

597

598 auth_identity = \_dbus_auth_get_identity (transport-\>auth);

599 \_dbus_assert (auth_identity != NULL);

600

601 connection = transport-\>connection;

602 windows_user_function = transport-\>windows_user_function;

603 windows_user_data = transport-\>unix_user_data;

604 windows_sid = \_dbus_strdup (\_dbus_credentials_get_windows_sid (auth_identity));

605

606 if (windows_sid == NULL)

607 {

608 /\* OOM \*/

609 return FALSE;

610 }

611

612 \_dbus_verbose ("unlock\n");

613 \_dbus_connection_unlock (connection);

614

615 allow = (\* windows_user_function) (connection,

616 windows_sid,

617 windows_user_data);

618

619 \_dbus_verbose ("lock post windows user function\n");

620 \_dbus_connection_lock (connection);

621

622 if (allow)

623 {

624 \_dbus_verbose ("Client SID '%s' authorized\n", windows_sid);

625 }

626 else

627 {

628 \_dbus_verbose ("Client SID '%s' was rejected, disconnecting\n",

629 \_dbus_credentials_get_windows_sid (auth_identity));

630 \_dbus_transport_disconnect (transport);

631 }

632

633 return allow;

634}

635

636static dbus_bool_t

637auth_via_default_rules (DBusTransport \*transport)

638{

639 DBusCredentials \*auth_identity;

640 DBusCredentials \*our_identity;

641 dbus_bool_t allow;

642

643 auth_identity = \_dbus_auth_get_identity (transport-\>auth);

644 \_dbus_assert (auth_identity != NULL);

645

646 /\* By default, connection is allowed if the client is 1) root or 2)

647 \* has the same UID as us or 3) anonymous is allowed.

648 \*/

649

650 our_identity = \_dbus_credentials_new_from_current_process ();

651 if (our_identity == NULL)

652 {

653 /\* OOM \*/

654 return FALSE;

655 }

656

657 if (transport-\>allow_anonymous \|\|

658 \_dbus_credentials_get_unix_uid (auth_identity) == 0 \|\|

659 \_dbus_credentials_same_user (our_identity,

660 auth_identity))

661 {

662 if (\_dbus_credentials_include(our_identity,DBUS_CREDENTIAL_WINDOWS_SID))

663 \_dbus_verbose ("Client authorized as SID '%s'"

664 "matching our SID '%s'\n",

665 \_dbus_credentials_get_windows_sid(auth_identity),

666 \_dbus_credentials_get_windows_sid(our_identity));

667 else

668 \_dbus_verbose ("Client authorized as UID "DBUS_UID_FORMAT

669 " matching our UID "DBUS_UID_FORMAT"\n",

670 \_dbus_credentials_get_unix_uid(auth_identity),

671 \_dbus_credentials_get_unix_uid(our_identity));

672 /\* We have authenticated! \*/

673 allow = TRUE;

674 }

675 else

676 {

677 if (\_dbus_credentials_include(our_identity,DBUS_CREDENTIAL_WINDOWS_SID))

678 \_dbus_verbose ("Client authorized as SID '%s'"

679 " but our SID is '%s', disconnecting\n",

680 (\_dbus_credentials_get_windows_sid(auth_identity) ?

681 \_dbus_credentials_get_windows_sid(auth_identity) : "\<null\>"),

682 (\_dbus_credentials_get_windows_sid(our_identity) ?

683 \_dbus_credentials_get_windows_sid(our_identity) : "\<null\>"));

684 else

685 \_dbus_verbose ("Client authorized as UID "DBUS_UID_FORMAT

686 " but our UID is "DBUS_UID_FORMAT", disconnecting\n",

687 \_dbus_credentials_get_unix_uid(auth_identity),

688 \_dbus_credentials_get_unix_uid(our_identity));

689 \_dbus_transport_disconnect (transport);

690 allow = FALSE;

691 }

692

693 \_dbus_credentials_unref (our_identity);

694

695 return allow;

696}

697

709dbus_bool_t

710\_dbus_transport_peek_is_authenticated (DBusTransport \*transport)

711{

712 return transport-\>authenticated;

713}

714

732dbus_bool_t

733\_dbus_transport_try_to_authenticate (DBusTransport \*transport)

734{

735 if (transport-\>authenticated)

736 return TRUE;

737 else

738 {

739 dbus_bool_t maybe_authenticated;

740

741 if (transport-\>disconnected)

742 return FALSE;

743

744 /\* paranoia ref since we call user callbacks sometimes \*/

745 \_dbus_connection_ref_unlocked (transport-\>connection);

746

747 maybe_authenticated =

748 (!(transport-\>send_credentials_pending \|\|

749 transport-\>receive_credentials_pending));

750

751 if (maybe_authenticated)

752 {

753 switch (\_dbus_auth_do_work (transport-\>auth))

754 {

755 case DBUS_AUTH_STATE_AUTHENTICATED:

756 /\* leave as maybe_authenticated \*/

757 break;

758

759 case DBUS_AUTH_STATE_WAITING_FOR_INPUT:

760 case DBUS_AUTH_STATE_WAITING_FOR_MEMORY:

761 case DBUS_AUTH_STATE_HAVE_BYTES_TO_SEND:

762 case DBUS_AUTH_STATE_NEED_DISCONNECT:

763 maybe_authenticated = FALSE;

764 break;

765

766 case DBUS_AUTH_STATE_INVALID:

767 default:

768 \_dbus_assert_not_reached ("invalid authentication state");

769 }

770 }

771

772 /\* If we're the client, verify the GUID

773 \*/

774 if (maybe_authenticated && !transport-\>is_server)

775 {

776 const char \*server_guid;

777

778 server_guid = \_dbus_auth_get_guid_from_server (transport-\>auth);

779 \_dbus_assert (server_guid != NULL);

780

781 if (transport-\>expected_guid &&

782 strcmp (transport-\>expected_guid, server_guid) != 0)

783 {

784 \_dbus_verbose ("Client expected GUID '%s' and we got '%s' from the server\n",

785 transport-\>expected_guid, server_guid);

786 \_dbus_transport_disconnect (transport);

787 \_dbus_connection_unref_unlocked (transport-\>connection);

788 return FALSE;

789 }

790 }

791

792 /\* If we're the server, see if we want to allow this identity to proceed.

793 \*/

794 if (maybe_authenticated && transport-\>is_server)

795 {

796 dbus_bool_t allow;

797 DBusCredentials \*auth_identity;

798

799 auth_identity = \_dbus_auth_get_identity (transport-\>auth);

800 \_dbus_assert (auth_identity != NULL);

801

802 /\* If we have an auth'd user and a user function, delegate

803 \* deciding whether auth credentials are good enough to the

804 \* app; otherwise, use our default decision process.

805 \*/

806 if (transport-\>unix_user_function != NULL &&

807 \_dbus_credentials_include (auth_identity, DBUS_CREDENTIAL_UNIX_USER_ID))

808 {

809 allow = auth_via_unix_user_function (transport);

810 }

811 else if (transport-\>windows_user_function != NULL &&

812 \_dbus_credentials_include (auth_identity, DBUS_CREDENTIAL_WINDOWS_SID))

813 {

814 allow = auth_via_windows_user_function (transport);

815 }

816 else

817 {

818 allow = auth_via_default_rules (transport);

819 }

820

821 if (!allow)

822 maybe_authenticated = FALSE;

823 }

824

825 transport-\>authenticated = maybe_authenticated;

826

827 \_dbus_connection_unref_unlocked (transport-\>connection);

828 return maybe_authenticated;

829 }

830}

831

838dbus_bool_t

839\_dbus_transport_get_is_anonymous (DBusTransport \*transport)

840{

841 DBusCredentials \*auth_identity;

842

843 if (!transport-\>authenticated)

844 return TRUE;

845

846 auth_identity = \_dbus_auth_get_identity (transport-\>auth);

847

848 if (\_dbus_credentials_are_anonymous (auth_identity))

849 return TRUE;

850 else

851 return FALSE;

852}

853

860dbus_bool_t

861\_dbus_transport_can_pass_unix_fd(DBusTransport \*transport)

862{

863 return DBUS_TRANSPORT_CAN_SEND_UNIX_FD(transport);

864}

865

873const char\*

874\_dbus_transport_get_address (DBusTransport \*transport)

875{

876 return transport-\>address;

877}

878

886const char\*

887\_dbus_transport_get_server_id (DBusTransport \*transport)

888{

889 if (transport-\>is_server)

890 return NULL;

891 else if (transport-\>authenticated)

892 return \_dbus_auth_get_guid_from_server (transport-\>auth);

893 else

894 return transport-\>expected_guid;

895}

896

906dbus_bool_t

907\_dbus_transport_handle_watch (DBusTransport \*transport,

908 DBusWatch \*watch,

909 unsigned int condition)

910{

911 dbus_bool_t retval;

912

913 \_dbus_assert (transport-\>vtable-\>handle_watch != NULL);

914

915 if (transport-\>disconnected)

916 return TRUE;

917

918 if (dbus_watch_get_socket (watch) \< 0)

919 {

920 \_dbus_warn_check_failed ("Tried to handle an invalidated watch; this watch should have been removed");

921 return TRUE;

922 }

923

924 \_dbus_watch_sanitize_condition (watch, &condition);

925

926 \_dbus_transport_ref (transport);

927 \_dbus_watch_ref (watch);

928 retval = (\* transport-\>vtable-\>handle_watch) (transport, watch, condition);

929 \_dbus_watch_unref (watch);

930 \_dbus_transport_unref (transport);

931

932 return retval;

933}

934

944dbus_bool_t

945\_dbus_transport_set_connection (DBusTransport \*transport,

946 DBusConnection \*connection)

947{

948 \_dbus_assert (transport-\>vtable-\>connection_set != NULL);

949 \_dbus_assert (transport-\>connection == NULL);

950

951 transport-\>connection = connection;

952

953 \_dbus_transport_ref (transport);

954 if (!(\* transport-\>vtable-\>connection_set) (transport))

955 transport-\>connection = NULL;

956 \_dbus_transport_unref (transport);

957

958 return transport-\>connection != NULL;

959}

960

968dbus_bool_t

969\_dbus_transport_get_socket_fd (DBusTransport \*transport,

970 DBusSocket \*fd_p)

971{

972 dbus_bool_t retval;

973

974 if (transport-\>vtable-\>get_socket_fd == NULL)

975 return FALSE;

976

977 if (transport-\>disconnected)

978 return FALSE;

979

980 \_dbus_transport_ref (transport);

981

982 retval = (\* transport-\>vtable-\>get_socket_fd) (transport,

983 fd_p);

984

985 \_dbus_transport_unref (transport);

986

987 return retval;

988}

989

1001void

1002\_dbus_transport_do_iteration (DBusTransport \*transport,

1003 unsigned int flags,

1004 int timeout_milliseconds)

1005{

1006 \_dbus_assert (transport-\>vtable-\>do_iteration != NULL);

1007

1008 \_dbus_verbose ("Transport iteration flags 0x%x timeout %d connected = %d\n",

1009 flags, timeout_milliseconds, !transport-\>disconnected);

1010

1011 if ((flags & (DBUS_ITERATION_DO_WRITING \|

1012 DBUS_ITERATION_DO_READING)) == 0)

1013 return; /\* Nothing to do \*/

1014

1015 if (transport-\>disconnected)

1016 return;

1017

1018 \_dbus_transport_ref (transport);

1019 (\* transport-\>vtable-\>do_iteration) (transport, flags,

1020 timeout_milliseconds);

1021 \_dbus_transport_unref (transport);

1022

1023 \_dbus_verbose ("end\n");

1024}

1025

1026static dbus_bool_t

1027recover_unused_bytes (DBusTransport \*transport)

1028{

1029 if (\_dbus_auth_needs_decoding (transport-\>auth))

1030 {

1031 DBusString plaintext;

1032 const DBusString \*encoded;

1033 DBusString \*buffer;

1034 int orig_len;

1035

1036 if (!\_dbus_string_init (&plaintext))

1037 goto nomem;

1038

1039 \_dbus_auth_get_unused_bytes (transport-\>auth,

1040 &encoded);

1041

1042 if (!\_dbus_auth_decode_data (transport-\>auth,

1043 encoded, &plaintext))

1044 {

1045 \_dbus_string_free (&plaintext);

1046 goto nomem;

1047 }

1048

1049 \_dbus_message_loader_get_buffer (transport-\>loader,

1050 &buffer,

1051 NULL,

1052 NULL);

1053

1054 orig_len = \_dbus_string_get_length (buffer);

1055

1056 if (!\_dbus_string_move (&plaintext, 0, buffer,

1057 orig_len))

1058 {

1059 \_dbus_string_free (&plaintext);

1060 goto nomem;

1061 }

1062

1063 \_dbus_verbose (" %d unused bytes sent to message loader\n",

1064 \_dbus_string_get_length (buffer) -

1065 orig_len);

1066

1067 \_dbus_message_loader_return_buffer (transport-\>loader,

1068 buffer);

1069

1070 \_dbus_auth_delete_unused_bytes (transport-\>auth);

1071

1072 \_dbus_string_free (&plaintext);

1073 }

1074 else

1075 {

1076 const DBusString \*bytes;

1077 DBusString \*buffer;

1078\#ifdef DBUS_ENABLE_VERBOSE_MODE

1079 int orig_len;

1080\#endif

1081 dbus_bool_t succeeded;

1082

1083 \_dbus_message_loader_get_buffer (transport-\>loader,

1084 &buffer,

1085 NULL,

1086 NULL);

1087

1088\#ifdef DBUS_ENABLE_VERBOSE_MODE

1089 orig_len = \_dbus_string_get_length (buffer);

1090\#endif

1091

1092 \_dbus_auth_get_unused_bytes (transport-\>auth,

1093 &bytes);

1094

1095 succeeded = TRUE;

1096 if (!\_dbus_string_copy (bytes, 0, buffer, \_dbus_string_get_length (buffer)))

1097 succeeded = FALSE;

1098

1099 \_dbus_verbose (" %d unused bytes sent to message loader\n",

1100 \_dbus_string_get_length (buffer) -

1101 orig_len);

1102

1103 \_dbus_message_loader_return_buffer (transport-\>loader,

1104 buffer);

1105

1106 if (succeeded)

1107 \_dbus_auth_delete_unused_bytes (transport-\>auth);

1108 else

1109 goto nomem;

1110 }

1111

1112 return TRUE;

1113

1114 nomem:

1115 \_dbus_verbose ("Not enough memory to transfer unused bytes from auth conversation\n");

1116 return FALSE;

1117}

1118

1126DBusDispatchStatus

1127\_dbus_transport_get_dispatch_status (DBusTransport \*transport)

1128{

1129 if (\_dbus_counter_get_size_value (transport-\>live_messages) \>= transport-\>max_live_messages_size \|\|

1130 \_dbus_counter_get_unix_fd_value (transport-\>live_messages) \>= transport-\>max_live_messages_unix_fds)

1131 return DBUS_DISPATCH_COMPLETE; /\* complete for now \*/

1132

1133 if (!\_dbus_transport_try_to_authenticate (transport))

1134 {

1135 if (\_dbus_auth_do_work (transport-\>auth) ==

1136 DBUS_AUTH_STATE_WAITING_FOR_MEMORY)

1137 return DBUS_DISPATCH_NEED_MEMORY;

1138 else if (!\_dbus_transport_try_to_authenticate (transport))

1139 return DBUS_DISPATCH_COMPLETE;

1140 }

1141

1142 if (!transport-\>unused_bytes_recovered &&

1143 !recover_unused_bytes (transport))

1144 return DBUS_DISPATCH_NEED_MEMORY;

1145

1146 transport-\>unused_bytes_recovered = TRUE;

1147

1148 if (!\_dbus_message_loader_queue_messages (transport-\>loader))

1149 return DBUS_DISPATCH_NEED_MEMORY;

1150

1151 if (\_dbus_message_loader_peek_message (transport-\>loader) != NULL)

1152 return DBUS_DISPATCH_DATA_REMAINS;

1153 else

1154 return DBUS_DISPATCH_COMPLETE;

1155}

1156

1165dbus_bool_t

1166\_dbus_transport_queue_messages (DBusTransport \*transport)

1167{

1168 DBusDispatchStatus status;

1169

1170\#if 0

1171 \_dbus_verbose ("enter\n");

1172\#endif

1173

1174 /\* Queue any messages \*/

1175 while ((status = \_dbus_transport_get_dispatch_status (transport)) == DBUS_DISPATCH_DATA_REMAINS)

1176 {

1177 DBusMessage \*message;

1178 DBusList \*link;

1179

1180 link = \_dbus_message_loader_pop_message_link (transport-\>loader);

1181 \_dbus_assert (link != NULL);

1182

1183 message = link-\>data;

1184

1185 \_dbus_verbose ("queueing received message %p\n", message);

1186

1187 if (!\_dbus_message_add_counter (message, transport-\>live_messages))

1188 {

1189 \_dbus_message_loader_putback_message_link (transport-\>loader,

1190 link);

1191 status = DBUS_DISPATCH_NEED_MEMORY;

1192 break;

1193 }

1194 else

1195 {

1196 /\* We didn't call the notify function when we added the counter, so

1197 \* catch up now. Since we have the connection's lock, it's desirable

1198 \* that we bypass the notify function and call this virtual method

1199 \* directly. \*/

1200 if (transport-\>vtable-\>live_messages_changed)

1201 (\* transport-\>vtable-\>live_messages_changed) (transport);

1202

1203 /\* pass ownership of link and message ref to connection \*/

1204 \_dbus_connection_queue_received_message_link (transport-\>connection,

1205 link);

1206 }

1207 }

1208

1209 if (\_dbus_message_loader_get_is_corrupted (transport-\>loader))

1210 {

1211 \_dbus_verbose ("Corrupted message stream, disconnecting\n");

1212 \_dbus_transport_disconnect (transport);

1213 }

1214

1215 return status != DBUS_DISPATCH_NEED_MEMORY;

1216}

1217

1224void

1225\_dbus_transport_set_max_message_size (DBusTransport \*transport,

1226 long size)

1227{

1228 \_dbus_message_loader_set_max_message_size (transport-\>loader, size);

1229}

1230

1237void

1238\_dbus_transport_set_max_message_unix_fds (DBusTransport \*transport,

1239 long n)

1240{

1241 \_dbus_message_loader_set_max_message_unix_fds (transport-\>loader, n);

1242}

1243

1250long

1251\_dbus_transport_get_max_message_size (DBusTransport \*transport)

1252{

1253 return \_dbus_message_loader_get_max_message_size (transport-\>loader);

1254}

1255

1262long

1263\_dbus_transport_get_max_message_unix_fds (DBusTransport \*transport)

1264{

1265 return \_dbus_message_loader_get_max_message_unix_fds (transport-\>loader);

1266}

1267

1274void

1275\_dbus_transport_set_max_received_size (DBusTransport \*transport,

1276 long size)

1277{

1278 transport-\>max_live_messages_size = size;

1279 \_dbus_counter_set_notify (transport-\>live_messages,

1280 transport-\>max_live_messages_size,

1281 transport-\>max_live_messages_unix_fds,

1282 live_messages_notify,

1283 transport);

1284}

1285

1292void

1293\_dbus_transport_set_max_received_unix_fds (DBusTransport \*transport,

1294 long n)

1295{

1296 transport-\>max_live_messages_unix_fds = n;

1297 \_dbus_counter_set_notify (transport-\>live_messages,

1298 transport-\>max_live_messages_size,

1299 transport-\>max_live_messages_unix_fds,

1300 live_messages_notify,

1301 transport);

1302}

1303

1310long

1311\_dbus_transport_get_max_received_size (DBusTransport \*transport)

1312{

1313 return transport-\>max_live_messages_size;

1314}

1315

1322long

1323\_dbus_transport_get_max_received_unix_fds (DBusTransport \*transport)

1324{

1325 return transport-\>max_live_messages_unix_fds;

1326}

1327

1335dbus_bool_t

1336\_dbus_transport_get_unix_user (DBusTransport \*transport,

1337 unsigned long \*uid)

1338{

1339 DBusCredentials \*auth_identity;

1340

1341 \*uid = \_DBUS_INT32_MAX; /\* better than some root or system user in

1342 \* case of bugs in the caller. Caller should

1343 \* never use this value on purpose, however.

1344 \*/

1345

1346 if (!transport-\>authenticated)

1347 return FALSE;

1348

1349 auth_identity = \_dbus_auth_get_identity (transport-\>auth);

1350

1351 if (\_dbus_credentials_include (auth_identity,

1352 DBUS_CREDENTIAL_UNIX_USER_ID))

1353 {

1354 \*uid = \_dbus_credentials_get_unix_uid (auth_identity);

1355 return TRUE;

1356 }

1357 else

1358 return FALSE;

1359}

1360

1368dbus_bool_t

1369\_dbus_transport_get_unix_process_id (DBusTransport \*transport,

1370 unsigned long \*pid)

1371{

1372 DBusCredentials \*auth_identity;

1373

1374 \*pid = DBUS_PID_UNSET; /\* Caller should never use this value on purpose,

1375 \* but we set it to a safe number, INT_MAX,

1376 \* just to root out possible bugs in bad callers.

1377 \*/

1378

1379 if (!transport-\>authenticated)

1380 return FALSE;

1381

1382 auth_identity = \_dbus_auth_get_identity (transport-\>auth);

1383

1384 if (\_dbus_credentials_include (auth_identity,

1385 DBUS_CREDENTIAL_UNIX_PROCESS_ID))

1386 {

1387 \*pid = \_dbus_credentials_get_pid (auth_identity);

1388 return TRUE;

1389 }

1390 else

1391 return FALSE;

1392}

1393

1402dbus_bool_t

1403\_dbus_transport_get_adt_audit_session_data (DBusTransport \*transport,

1404 void \*\*data,

1405 int \*data_size)

1406{

1407 DBusCredentials \*auth_identity;

1408

1409 \*data = NULL;

1410 \*data_size = 0;

1411

1412 if (!transport-\>authenticated)

1413 return FALSE;

1414

1415 auth_identity = \_dbus_auth_get_identity (transport-\>auth);

1416

1417 if (\_dbus_credentials_include (auth_identity,

1418 DBUS_CREDENTIAL_ADT_AUDIT_DATA_ID))

1419 {

1420 \*data = (void \*) \_dbus_credentials_get_adt_audit_data (auth_identity);

1421 \*data_size = \_dbus_credentials_get_adt_audit_data_size (auth_identity);

1422 return TRUE;

1423 }

1424 else

1425 return FALSE;

1426}

1427

1438void

1439\_dbus_transport_set_unix_user_function (DBusTransport \*transport,

1440 DBusAllowUnixUserFunction function,

1441 void \*data,

1442 DBusFreeFunction free_data_function,

1443 void \*\*old_data,

1444 DBusFreeFunction \*old_free_data_function)

1445{

1446 \*old_data = transport-\>unix_user_data;

1447 \*old_free_data_function = transport-\>free_unix_user_data;

1448

1449 transport-\>unix_user_function = function;

1450 transport-\>unix_user_data = data;

1451 transport-\>free_unix_user_data = free_data_function;

1452}

1453

1454dbus_bool_t

1455\_dbus_transport_get_linux_security_label (DBusTransport \*transport,

1456 char \*\*label_p)

1457{

1458 DBusCredentials \*auth_identity;

1459

1460 \*label_p = NULL;

1461

1462 if (!transport-\>authenticated)

1463 return FALSE;

1464

1465 auth_identity = \_dbus_auth_get_identity (transport-\>auth);

1466

1467 if (\_dbus_credentials_include (auth_identity,

1468 DBUS_CREDENTIAL_LINUX_SECURITY_LABEL))

1469 {

1470 /\* If no memory, we are supposed to return TRUE and set NULL \*/

1471 \*label_p = \_dbus_strdup (\_dbus_credentials_get_linux_security_label (auth_identity));

1472

1473 return TRUE;

1474 }

1475 else

1476 {

1477 return FALSE;

1478 }

1479}

1480

1488DBusCredentials \*

1489\_dbus_transport_get_credentials (DBusTransport \*transport)

1490{

1491 if (!transport-\>authenticated)

1492 return FALSE;

1493

1494 return \_dbus_auth_get_identity (transport-\>auth);

1495}

1496

1504dbus_bool_t

1505\_dbus_transport_get_windows_user (DBusTransport \*transport,

1506 char \*\*windows_sid_p)

1507{

1508 DBusCredentials \*auth_identity;

1509

1510 \*windows_sid_p = NULL;

1511

1512 if (!transport-\>authenticated)

1513 return FALSE;

1514

1515 auth_identity = \_dbus_auth_get_identity (transport-\>auth);

1516

1517 if (\_dbus_credentials_include (auth_identity,

1518 DBUS_CREDENTIAL_WINDOWS_SID))

1519 {

1520 /\* If no memory, we are supposed to return TRUE and set NULL \*/

1521 \*windows_sid_p = \_dbus_strdup (\_dbus_credentials_get_windows_sid (auth_identity));

1522

1523 return TRUE;

1524 }

1525 else

1526 return FALSE;

1527}

1528

1540void

1541\_dbus_transport_set_windows_user_function (DBusTransport \*transport,

1542 DBusAllowWindowsUserFunction function,

1543 void \*data,

1544 DBusFreeFunction free_data_function,

1545 void \*\*old_data,

1546 DBusFreeFunction \*old_free_data_function)

1547{

1548 \*old_data = transport-\>windows_user_data;

1549 \*old_free_data_function = transport-\>free_windows_user_data;

1550

1551 transport-\>windows_user_function = function;

1552 transport-\>windows_user_data = data;

1553 transport-\>free_windows_user_data = free_data_function;

1554}

1555

1564dbus_bool_t

1565\_dbus_transport_set_auth_mechanisms (DBusTransport \*transport,

1566 const char \*\*mechanisms)

1567{

1568 return \_dbus_auth_set_mechanisms (transport-\>auth, mechanisms);

1569}

1570

1577void

1578\_dbus_transport_set_allow_anonymous (DBusTransport \*transport,

1579 dbus_bool_t value)

1580{

1581 transport-\>allow_anonymous = value != FALSE;

1582}

1583

1589int

1590\_dbus_transport_get_pending_fds_count (DBusTransport \*transport)

1591{

1592 return \_dbus_message_loader_get_pending_fds_count (transport-\>loader);

1593}

1594

1602void

1603\_dbus_transport_set_pending_fds_function (DBusTransport \*transport,

1604 void (\* callback) (void \*),

1605 void \*data)

1606{

1607 \_dbus_message_loader_set_pending_fds_function (transport-\>loader,

1608 callback, data);

1609}

1610

1611\#ifdef DBUS_ENABLE_STATS

1612void

1613\_dbus_transport_get_stats (DBusTransport \*transport,

1614 dbus_uint32_t \*queue_bytes,

1615 dbus_uint32_t \*queue_fds,

1616 dbus_uint32_t \*peak_queue_bytes,

1617 dbus_uint32_t \*peak_queue_fds)

1618{

1619 if (queue_bytes != NULL)

1620 \*queue_bytes = \_dbus_counter_get_size_value (transport-\>live_messages);

1621

1622 if (queue_fds != NULL)

1623 \*queue_fds = \_dbus_counter_get_unix_fd_value (transport-\>live_messages);

1624

1625 if (peak_queue_bytes != NULL)

1626 \*peak_queue_bytes = \_dbus_counter_get_peak_size_value (transport-\>live_messages);

1627

1628 if (peak_queue_fds != NULL)

1629 \*peak_queue_fds = \_dbus_counter_get_peak_unix_fd_value (transport-\>live_messages);

1630}

1631\#endif /\* DBUS_ENABLE_STATS \*/

1632

\_dbus_set_bad_address

void \_dbus_set_bad_address(DBusError \*error, const char \*address_problem_type, const char \*address_problem_field, const char \*address_problem_other)

Sets DBUS_ERROR_BAD_ADDRESS.

**Definition** dbus-address.c:70

dbus_address_entries_free

void dbus_address_entries_free(DBusAddressEntry \*\*entries)

Frees a NULL-terminated array of address entries.

**Definition** dbus-address.c:194

dbus_parse_address

dbus_bool_t dbus_parse_address(const char \*address, DBusAddressEntry \*\*\*entry_result, int \*array_len, DBusError \*error)

Parses an address string of the form:

**Definition** dbus-address.c:368

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

\_dbus_auth_get_identity

DBusCredentials \* \_dbus_auth_get_identity(DBusAuth \*auth)

Gets the identity we authorized the client as.

**Definition** dbus-auth.c:2848

\_dbus_auth_decode_data

dbus_bool_t \_dbus_auth_decode_data(DBusAuth \*auth, const DBusString \*encoded, DBusString \*plaintext)

Called post-authentication, decodes a block of bytes received from the peer.

**Definition** dbus-auth.c:2798

\_dbus_auth_unref

void \_dbus_auth_unref(DBusAuth \*auth)

Decrements the refcount of an auth object.

**Definition** dbus-auth.c:2463

\_dbus_auth_set_mechanisms

dbus_bool_t \_dbus_auth_set_mechanisms(DBusAuth \*auth, const char \*\*mechanisms)

Sets an array of authentication mechanism names that we are willing to use.

**Definition** dbus-auth.c:2513

\_dbus_auth_delete_unused_bytes

void \_dbus_auth_delete_unused_bytes(DBusAuth \*auth)

Gets rid of unused bytes returned by \_dbus_auth_get_unused_bytes() after we've gotten them and succes...

**Definition** dbus-auth.c:2691

\_dbus_auth_get_guid_from_server

const char \* \_dbus_auth_get_guid_from_server(DBusAuth \*auth)

Gets the GUID from the server if we've authenticated; gets NULL otherwise.

**Definition** dbus-auth.c:2872

\_dbus_auth_needs_decoding

dbus_bool_t \_dbus_auth_needs_decoding(DBusAuth \*auth)

Called post-authentication, indicates whether we need to decode the message stream with \_dbus_auth_de...

**Definition** dbus-auth.c:2767

\_dbus_auth_client_new

DBusAuth \* \_dbus_auth_client_new(void)

Creates a new auth conversation object for the client side.

**Definition** dbus-auth.c:2410

\_dbus_auth_server_new

DBusAuth \* \_dbus_auth_server_new(const DBusString \*guid)

Creates a new auth conversation object for the server side.

**Definition** dbus-auth.c:2364

\_dbus_auth_get_unused_bytes

void \_dbus_auth_get_unused_bytes(DBusAuth \*auth, const DBusString \*\*str)

Returns leftover bytes that were not used as part of the auth conversation.

**Definition** dbus-auth.c:2674

\_dbus_connection_unlock

DBUS_PRIVATE_EXPORT void \_dbus_connection_unlock(DBusConnection \*connection)

Releases the connection lock.

**Definition** dbus-connection.c:403

\_dbus_connection_lock

DBUS_PRIVATE_EXPORT void \_dbus_connection_lock(DBusConnection \*connection)

Acquires the connection lock.

**Definition** dbus-connection.c:392

\_dbus_connection_unref_unlocked

DBUS_PRIVATE_EXPORT void \_dbus_connection_unref_unlocked(DBusConnection \*connection)

Decrements the reference count of a DBusConnection.

**Definition** dbus-connection.c:1447

\_dbus_connection_queue_received_message_link

void \_dbus_connection_queue_received_message_link(DBusConnection \*connection, DBusList \*link)

Adds a message-containing list link to the incoming message queue, taking ownership of the link and t...

**Definition** dbus-connection.c:484

\_dbus_connection_ref_unlocked

DBUS_PRIVATE_EXPORT DBusConnection \* \_dbus_connection_ref_unlocked(DBusConnection \*connection)

Increments the reference count of a DBusConnection.

**Definition** dbus-connection.c:1424

DBusAllowUnixUserFunction

dbus_bool_t(\* DBusAllowUnixUserFunction)(DBusConnection \*connection, unsigned long uid, void \*data)

Called during authentication to check whether the given UNIX user ID is allowed to connect,...

**Definition** dbus-connection.h:146

DBusDispatchStatus

DBusDispatchStatus

Indicates the status of incoming data on a DBusConnection.

**Definition** dbus-connection.h:83

DBusAllowWindowsUserFunction

dbus_bool_t(\* DBusAllowWindowsUserFunction)(DBusConnection \*connection, const char \*user_sid, void \*data)

Called during authentication to check whether the given Windows user ID is allowed to connect,...

**Definition** dbus-connection.h:156

DBUS_DISPATCH_NEED_MEMORY

@ DBUS_DISPATCH_NEED_MEMORY

More memory is needed to continue.

**Definition** dbus-connection.h:86

DBUS_DISPATCH_COMPLETE

@ DBUS_DISPATCH_COMPLETE

All currently available data has been processed.

**Definition** dbus-connection.h:85

DBUS_DISPATCH_DATA_REMAINS

@ DBUS_DISPATCH_DATA_REMAINS

There is more data to potentially convert to messages.

**Definition** dbus-connection.h:84

\_dbus_credentials_include

dbus_bool_t \_dbus_credentials_include(DBusCredentials \*credentials, DBusCredentialType type)

Checks whether the given credential is present.

**Definition** dbus-credentials.c:365

\_dbus_credentials_same_user

dbus_bool_t \_dbus_credentials_same_user(DBusCredentials \*credentials, DBusCredentials \*other_credentials)

Check whether the user-identifying credentials in two credentials objects are identical.

**Definition** dbus-credentials.c:747

\_dbus_credentials_get_unix_uid

dbus_uid_t \_dbus_credentials_get_unix_uid(DBusCredentials \*credentials)

Gets the UNIX user ID in the credentials, or DBUS_UID_UNSET if the credentials object doesn't contain...

**Definition** dbus-credentials.c:440

\_dbus_credentials_new_from_current_process

DBusCredentials \* \_dbus_credentials_new_from_current_process(void)

Creates a new object with the most important credentials (user ID and process ID) from the current pr...

**Definition** dbus-credentials.c:113

\_dbus_credentials_new

DBusCredentials \* \_dbus_credentials_new(void)

Creates a new credentials object.

**Definition** dbus-credentials.c:86

\_dbus_credentials_get_adt_audit_data

void \* \_dbus_credentials_get_adt_audit_data(DBusCredentials \*credentials)

Gets the ADT audit data in the credentials, or NULL if the credentials object doesn't contain ADT aud...

**Definition** dbus-credentials.c:479

\_dbus_credentials_get_linux_security_label

const char \* \_dbus_credentials_get_linux_security_label(DBusCredentials \*credentials)

Gets the Linux security label (as used by LSMs) from the credentials, or NULL if the credentials obje...

**Definition** dbus-credentials.c:466

\_dbus_credentials_unref

void \_dbus_credentials_unref(DBusCredentials \*credentials)

Decrement refcount on credentials.

**Definition** dbus-credentials.c:148

\_dbus_credentials_get_pid

dbus_pid_t \_dbus_credentials_get_pid(DBusCredentials \*credentials)

Gets the UNIX process ID in the credentials, or DBUS_PID_UNSET if the credentials object doesn't cont...

**Definition** dbus-credentials.c:401

\_dbus_credentials_get_adt_audit_data_size

dbus_int32_t \_dbus_credentials_get_adt_audit_data_size(DBusCredentials \*credentials)

Gets the ADT audit data size in the credentials, or 0 if the credentials object doesn't contain ADT a...

**Definition** dbus-credentials.c:492

\_dbus_credentials_get_windows_sid

const char \* \_dbus_credentials_get_windows_sid(DBusCredentials \*credentials)

Gets the Windows user SID in the credentials, or NULL if the credentials object doesn't contain a Win...

**Definition** dbus-credentials.c:453

\_dbus_credentials_are_anonymous

dbus_bool_t \_dbus_credentials_are_anonymous(DBusCredentials \*credentials)

Checks whether a credentials object contains a user identity.

**Definition** dbus-credentials.c:558

DBUS_ERROR_INIT

\#define DBUS_ERROR_INIT

Expands to a suitable initializer for a DBusError on the stack.

**Definition** dbus-errors.h:64

dbus_move_error

void dbus_move_error(DBusError \*src, DBusError \*dest)

Moves an error src into dest, freeing src and overwriting dest.

**Definition** dbus-errors.c:281

dbus_set_error

void dbus_set_error(DBusError \*error, const char \*name, const char \*format,...)

Assigns an error name and message to a DBusError.

**Definition** dbus-errors.c:356

dbus_error_free

void dbus_error_free(DBusError \*error)

Frees an error that's been set (or just initialized), then reinitializes the error as in dbus_error_i...

**Definition** dbus-errors.c:213

dbus_error_is_set

dbus_bool_t dbus_error_is_set(const DBusError \*error)

Checks whether an error occurred (the error is set).

**Definition** dbus-errors.c:331

\_dbus_assert_not_reached

\#define \_dbus_assert_not_reached(explanation)

Aborts with an error message if called.

**Definition** dbus-internals.h:164

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_dbus_warn_check_failed

void \_dbus_warn_check_failed(const char \*format,...)

Prints a "critical" warning to stderr when an assertion fails; differs from \_dbus_warn primarily in t...

**Definition** dbus-internals.c:310

\_dbus_strdup

char \* \_dbus_strdup(const char \*str)

Duplicates a string.

**Definition** dbus-internals.c:621

\_DBUS_N_ELEMENTS

\#define \_DBUS_N_ELEMENTS(array)

Computes the number of elements in a fixed-size array using sizeof().

**Definition** dbus-internals.h:189

\_DBUS_INT32_MAX

\#define \_DBUS_INT32_MAX

Maximum value of type "int32".

**Definition** dbus-internals.h:323

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

DBusFreeFunction

void(\* DBusFreeFunction)(void \*memory)

The type of a function which frees a block of memory.

**Definition** dbus-memory.h:65

dbus_free

void dbus_free(void \*memory)

Frees a block of memory previously allocated by dbus_malloc() or dbus_malloc0().

**Definition** dbus-memory.c:710

\_dbus_message_loader_set_max_message_size

void \_dbus_message_loader_set_max_message_size(DBusMessageLoader \*loader, long size)

Sets the maximum size message we allow.

**Definition** dbus-message.c:4843

\_dbus_message_loader_get_is_corrupted

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_message_loader_get_is_corrupted(DBusMessageLoader \*loader)

Checks whether the loader is confused due to bad data.

**Definition** dbus-message.c:4814

\_dbus_message_loader_unref

DBUS_PRIVATE_EXPORT void \_dbus_message_loader_unref(DBusMessageLoader \*loader)

Decrements the reference count of the loader and finalizes the loader when the count reaches zero.

**Definition** dbus-message.c:4239

\_dbus_message_loader_set_pending_fds_function

void \_dbus_message_loader_set_pending_fds_function(DBusMessageLoader \*loader, void(\*callback)(void \*), void \*data)

Register a function to be called whenever the number of pending file descriptors in the loader change...

**Definition** dbus-message.c:4922

\_dbus_message_loader_putback_message_link

void \_dbus_message_loader_putback_message_link(DBusMessageLoader \*loader, DBusList \*link)

Returns a popped message link, used to undo a pop.

**Definition** dbus-message.c:4798

\_dbus_message_loader_get_pending_fds_count

int \_dbus_message_loader_get_pending_fds_count(DBusMessageLoader \*loader)

Return how many file descriptors are pending in the loader.

**Definition** dbus-message.c:4904

\_dbus_message_loader_get_buffer

DBUS_PRIVATE_EXPORT void \_dbus_message_loader_get_buffer(DBusMessageLoader \*loader, DBusString \*\*buffer, int \*max_to_read, dbus_bool_t \*may_read_unix_fds)

Gets the buffer to use for reading data from the network.

**Definition** dbus-message.c:4274

\_dbus_message_add_counter

dbus_bool_t \_dbus_message_add_counter(DBusMessage \*message, DBusCounter \*counter)

Adds a counter to be incremented immediately with the size/unix fds of this message,...

**Definition** dbus-message.c:376

\_dbus_message_loader_peek_message

DBusMessage \* \_dbus_message_loader_peek_message(DBusMessageLoader \*loader)

Peeks at first loaded message, returns NULL if no messages have been queued.

**Definition** dbus-message.c:4755

\_dbus_message_loader_set_max_message_unix_fds

void \_dbus_message_loader_set_max_message_unix_fds(DBusMessageLoader \*loader, long n)

Sets the maximum unix fds per message we allow.

**Definition** dbus-message.c:4874

\_dbus_message_loader_get_max_message_size

DBUS_PRIVATE_EXPORT long \_dbus_message_loader_get_max_message_size(DBusMessageLoader \*loader)

Gets the maximum allowed message size in bytes.

**Definition** dbus-message.c:4862

\_dbus_message_loader_new

DBUS_PRIVATE_EXPORT DBusMessageLoader \* \_dbus_message_loader_new(void)

Creates a new message loader.

**Definition** dbus-message.c:4177

\_dbus_message_loader_pop_message_link

DBusList \* \_dbus_message_loader_pop_message_link(DBusMessageLoader \*loader)

Pops a loaded message inside a list link (passing ownership of the message and link to the caller).

**Definition** dbus-message.c:4786

\_dbus_message_loader_queue_messages

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_message_loader_queue_messages(DBusMessageLoader \*loader)

Converts buffered data into messages, if we have enough data.

**Definition** dbus-message.c:4692

\_dbus_message_loader_return_buffer

DBUS_PRIVATE_EXPORT void \_dbus_message_loader_return_buffer(DBusMessageLoader \*loader, DBusString \*buffer)

Returns a buffer obtained from \_dbus_message_loader_get_buffer(), indicating to the loader how many b...

**Definition** dbus-message.c:4380

\_dbus_message_loader_get_max_message_unix_fds

long \_dbus_message_loader_get_max_message_unix_fds(DBusMessageLoader \*loader)

Gets the maximum allowed number of unix fds per message.

**Definition** dbus-message.c:4893

DBUS_ERROR_NO_MEMORY

\#define DBUS_ERROR_NO_MEMORY

There was not enough memory to complete an operation.

**Definition** dbus-protocol.h:363

\_dbus_counter_set_notify

void \_dbus_counter_set_notify(DBusCounter \*counter, long size_guard_value, long unix_fd_guard_value, DBusCounterNotifyFunction function, void \*user_data)

Sets the notify function for this counter; the notify function is called whenever the counter's value...

**Definition** dbus-resources.c:313

\_dbus_counter_new

DBusCounter \* \_dbus_counter_new(void)

Creates a new DBusCounter.

**Definition** dbus-resources.c:91

\_dbus_counter_get_unix_fd_value

long \_dbus_counter_get_unix_fd_value(DBusCounter \*counter)

Gets the current value of the unix fd counter.

**Definition** dbus-resources.c:292

\_dbus_counter_unref

void \_dbus_counter_unref(DBusCounter \*counter)

Decrements refcount of the counter and possibly finalizes the counter.

**Definition** dbus-resources.c:138

\_dbus_counter_get_size_value

long \_dbus_counter_get_size_value(DBusCounter \*counter)

Gets the current value of the size counter.

**Definition** dbus-resources.c:276

\_dbus_string_init

dbus_bool_t \_dbus_string_init(DBusString \*str)

Initializes a string.

**Definition** dbus-string.c:182

\_dbus_string_copy

dbus_bool_t \_dbus_string_copy(const DBusString \*source, int start, DBusString \*dest, int insert_at)

Like \_dbus_string_move(), but does not delete the section of the source string that's copied to the d...

**Definition** dbus-string.c:1345

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_string_copy_data

dbus_bool_t \_dbus_string_copy_data(const DBusString \*str, char \*\*data_return)

Copies the data from the string into a char\*.

**Definition** dbus-string.c:717

\_dbus_string_get_length

int \_dbus_string_get_length(const DBusString \*str)

Gets the length of a string (not including nul termination).

**Definition** dbus-string.c:784

\_dbus_string_get_const_data

const char \* \_dbus_string_get_const_data(const DBusString \*str)

Gets the raw character buffer from a const string.

**Definition** dbus-string.c:513

\_dbus_string_move

dbus_bool_t \_dbus_string_move(DBusString \*source, int start, DBusString \*dest, int insert_at)

Moves the end of one string into another string.

**Definition** dbus-string.c:1321

dbus_uid_t

unsigned long dbus_uid_t

A user ID.

**Definition** dbus-sysdeps.h:141

DBUS_PID_UNSET

\#define DBUS_PID_UNSET

an invalid PID used to represent an uninitialized dbus_pid_t field

**Definition** dbus-sysdeps.h:146

DBUS_UID_FORMAT

\#define DBUS_UID_FORMAT

an appropriate printf format for dbus_uid_t

**Definition** dbus-sysdeps.h:155

\_dbus_get_autolaunch_address

dbus_bool_t \_dbus_get_autolaunch_address(const char \*scope, DBusString \*address, DBusError \*error)

Returns the address of a new session bus.

**Definition** dbus-sysdeps-unix.c:4299

\_dbus_transport_open_socket

DBusTransportOpenResult \_dbus_transport_open_socket(DBusAddressEntry \*entry, DBusTransport \*\*transport_p, DBusError \*error)

Opens a TCP socket transport.

**Definition** dbus-transport-socket.c:1457

\_dbus_transport_open_unix_socket

DBusTransportOpenResult \_dbus_transport_open_unix_socket(DBusAddressEntry \*entry, DBusTransport \*\*transport_p, DBusError \*error)

Opens a UNIX socket transport.

**Definition** dbus-transport-socket.c:1584

\_dbus_transport_open_platform_specific

DBusTransportOpenResult \_dbus_transport_open_platform_specific(DBusAddressEntry \*entry, DBusTransport \*\*transport_p, DBusError \*error)

Opens platform specific transport types.

**Definition** dbus-transport-unix.c:248

\_dbus_transport_set_max_message_size

void \_dbus_transport_set_max_message_size(DBusTransport \*transport, long size)

See dbus_connection_set_max_message_size().

**Definition** dbus-transport.c:1225

\_dbus_transport_set_max_received_size

void \_dbus_transport_set_max_received_size(DBusTransport \*transport, long size)

See dbus_connection_set_max_received_size().

**Definition** dbus-transport.c:1275

\_dbus_transport_get_dispatch_status

DBusDispatchStatus \_dbus_transport_get_dispatch_status(DBusTransport \*transport)

Reports our current dispatch status (whether there's buffered data to be queued as messages,...

**Definition** dbus-transport.c:1127

\_dbus_transport_set_auth_mechanisms

dbus_bool_t \_dbus_transport_set_auth_mechanisms(DBusTransport \*transport, const char \*\*mechanisms)

Sets the SASL authentication mechanisms supported by this transport.

**Definition** dbus-transport.c:1565

\_dbus_transport_get_pending_fds_count

int \_dbus_transport_get_pending_fds_count(DBusTransport \*transport)

Return how many file descriptors are pending in the loader.

**Definition** dbus-transport.c:1590

\_dbus_transport_get_adt_audit_session_data

dbus_bool_t \_dbus_transport_get_adt_audit_session_data(DBusTransport \*transport, void \*\*data, int \*data_size)

See dbus_connection_get_adt_audit_session_data().

**Definition** dbus-transport.c:1403

\_dbus_transport_get_windows_user

dbus_bool_t \_dbus_transport_get_windows_user(DBusTransport \*transport, char \*\*windows_sid_p)

See dbus_connection_get_windows_user().

**Definition** dbus-transport.c:1505

\_dbus_transport_queue_messages

dbus_bool_t \_dbus_transport_queue_messages(DBusTransport \*transport)

Processes data we've read while handling a watch, potentially converting some of it to messages and q...

**Definition** dbus-transport.c:1166

\_dbus_transport_get_socket_fd

dbus_bool_t \_dbus_transport_get_socket_fd(DBusTransport \*transport, DBusSocket \*fd_p)

Get the socket file descriptor, if any.

**Definition** dbus-transport.c:969

\_dbus_transport_get_address

const char \* \_dbus_transport_get_address(DBusTransport \*transport)

Gets the address of a transport.

**Definition** dbus-transport.c:874

\_dbus_transport_handle_watch

dbus_bool_t \_dbus_transport_handle_watch(DBusTransport \*transport, DBusWatch \*watch, unsigned int condition)

Handles a watch by reading data, writing data, or disconnecting the transport, as appropriate for the...

**Definition** dbus-transport.c:907

\_dbus_transport_ref

DBusTransport \* \_dbus_transport_ref(DBusTransport \*transport)

Increments the reference count for the transport.

**Definition** dbus-transport.c:469

\_dbus_transport_peek_is_authenticated

dbus_bool_t \_dbus_transport_peek_is_authenticated(DBusTransport \*transport)

Returns TRUE if we have been authenticated.

**Definition** dbus-transport.c:710

\_dbus_transport_set_allow_anonymous

void \_dbus_transport_set_allow_anonymous(DBusTransport \*transport, dbus_bool_t value)

See dbus_connection_set_allow_anonymous()

**Definition** dbus-transport.c:1578

\_dbus_transport_disconnect

void \_dbus_transport_disconnect(DBusTransport \*transport)

Closes our end of the connection to a remote application.

**Definition** dbus-transport.c:511

\_dbus_transport_get_max_received_size

long \_dbus_transport_get_max_received_size(DBusTransport \*transport)

See dbus_connection_get_max_received_size().

**Definition** dbus-transport.c:1311

\_dbus_transport_get_credentials

DBusCredentials \* \_dbus_transport_get_credentials(DBusTransport \*transport)

If the transport has already been authenticated, return its credentials.

**Definition** dbus-transport.c:1489

\_dbus_transport_set_connection

dbus_bool_t \_dbus_transport_set_connection(DBusTransport \*transport, DBusConnection \*connection)

Sets the connection using this transport.

**Definition** dbus-transport.c:945

\_dbus_transport_set_unix_user_function

void \_dbus_transport_set_unix_user_function(DBusTransport \*transport, DBusAllowUnixUserFunction function, void \*data, DBusFreeFunction free_data_function, void \*\*old_data, DBusFreeFunction \*old_free_data_function)

See dbus_connection_set_unix_user_function().

**Definition** dbus-transport.c:1439

\_dbus_transport_get_max_message_unix_fds

long \_dbus_transport_get_max_message_unix_fds(DBusTransport \*transport)

See dbus_connection_get_max_message_unix_fds().

**Definition** dbus-transport.c:1263

\_dbus_transport_init_base

dbus_bool_t \_dbus_transport_init_base(DBusTransport \*transport, const DBusTransportVTable \*vtable, const DBusString \*server_guid, const DBusString \*address)

Initializes the base class members of DBusTransport.

**Definition** dbus-transport.c:104

\_dbus_transport_set_max_received_unix_fds

void \_dbus_transport_set_max_received_unix_fds(DBusTransport \*transport, long n)

See dbus_connection_set_max_received_unix_fds().

**Definition** dbus-transport.c:1293

\_dbus_transport_unref

void \_dbus_transport_unref(DBusTransport \*transport)

Decrements the reference count for the transport.

**Definition** dbus-transport.c:486

\_dbus_transport_can_pass_unix_fd

dbus_bool_t \_dbus_transport_can_pass_unix_fd(DBusTransport \*transport)

Returns TRUE if the transport supports sending unix fds.

**Definition** dbus-transport.c:861

\_dbus_transport_try_to_authenticate

dbus_bool_t \_dbus_transport_try_to_authenticate(DBusTransport \*transport)

Returns TRUE if we have been authenticated.

**Definition** dbus-transport.c:733

\_dbus_transport_do_iteration

void \_dbus_transport_do_iteration(DBusTransport \*transport, unsigned int flags, int timeout_milliseconds)

Performs a single poll()/select() on the transport's file descriptors and then reads/writes data as a...

**Definition** dbus-transport.c:1002

\_dbus_transport_get_max_received_unix_fds

long \_dbus_transport_get_max_received_unix_fds(DBusTransport \*transport)

See dbus_connection_set_max_received_unix_fds().

**Definition** dbus-transport.c:1323

\_dbus_transport_get_is_connected

dbus_bool_t \_dbus_transport_get_is_connected(DBusTransport \*transport)

Returns TRUE if the transport has not been disconnected.

**Definition** dbus-transport.c:536

\_dbus_transport_set_max_message_unix_fds

void \_dbus_transport_set_max_message_unix_fds(DBusTransport \*transport, long n)

See dbus_connection_set_max_message_unix_fds().

**Definition** dbus-transport.c:1238

\_dbus_transport_set_pending_fds_function

void \_dbus_transport_set_pending_fds_function(DBusTransport \*transport, void(\*callback)(void \*), void \*data)

Register a function to be called whenever the number of pending file descriptors in the loader change...

**Definition** dbus-transport.c:1603

\_dbus_transport_set_windows_user_function

void \_dbus_transport_set_windows_user_function(DBusTransport \*transport, DBusAllowWindowsUserFunction function, void \*data, DBusFreeFunction free_data_function, void \*\*old_data, DBusFreeFunction \*old_free_data_function)

See dbus_connection_set_windows_user_function().

**Definition** dbus-transport.c:1541

\_dbus_transport_get_max_message_size

long \_dbus_transport_get_max_message_size(DBusTransport \*transport)

See dbus_connection_get_max_message_size().

**Definition** dbus-transport.c:1251

\_dbus_transport_get_unix_process_id

dbus_bool_t \_dbus_transport_get_unix_process_id(DBusTransport \*transport, unsigned long \*pid)

See dbus_connection_get_unix_process_id().

**Definition** dbus-transport.c:1369

\_dbus_transport_open

DBusTransport \* \_dbus_transport_open(DBusAddressEntry \*entry, DBusError \*error)

Try to open a new transport for the given address entry.

**Definition** dbus-transport.c:373

\_dbus_transport_get_server_id

const char \* \_dbus_transport_get_server_id(DBusTransport \*transport)

Gets the id of the server we are connected to (see dbus_server_get_id()).

**Definition** dbus-transport.c:887

\_dbus_transport_get_is_anonymous

dbus_bool_t \_dbus_transport_get_is_anonymous(DBusTransport \*transport)

See dbus_connection_get_is_anonymous().

**Definition** dbus-transport.c:839

\_dbus_transport_finalize_base

void \_dbus_transport_finalize_base(DBusTransport \*transport)

Finalizes base class members of DBusTransport.

**Definition** dbus-transport.c:218

\_dbus_transport_get_unix_user

dbus_bool_t \_dbus_transport_get_unix_user(DBusTransport \*transport, unsigned long \*uid)

See dbus_connection_get_unix_user().

**Definition** dbus-transport.c:1336

\_dbus_watch_sanitize_condition

void \_dbus_watch_sanitize_condition(DBusWatch \*watch, unsigned int \*condition)

Sanitizes the given condition so that it only contains flags that the DBusWatch requested.

**Definition** dbus-watch.c:187

\_dbus_watch_ref

DBusWatch \* \_dbus_watch_ref(DBusWatch \*watch)

Increments the reference count of a DBusWatch object.

**Definition** dbus-watch.c:126

\_dbus_watch_unref

void \_dbus_watch_unref(DBusWatch \*watch)

Decrements the reference count of a DBusWatch object and finalizes the object if the count reaches ze...

**Definition** dbus-watch.c:140

dbus_watch_get_socket

DBUS_EXPORT int dbus_watch_get_socket(DBusWatch \*watch)

Returns a socket to be watched, on UNIX this will return -1 if our transport is not socket-based so d...

**Definition** dbus-watch.c:595

DBusAddressEntry

Internals of DBusAddressEntry.

**Definition** dbus-address.c:49

DBusAuth

Internal members of DBusAuth.

**Definition** dbus-auth.c:156

DBusConnection

Implementation details of DBusConnection.

**Definition** dbus-connection.c:259

DBusCounter

Internals of DBusCounter.

**Definition** dbus-resources.c:57

DBusCredentials

**Definition** dbus-credentials.c:60

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusList

A node in a linked list.

**Definition** dbus-list.h:37

DBusList::data

void \* data

Data stored at this element.

**Definition** dbus-list.h:40

DBusMessageLoader

Implementation details of DBusMessageLoader.

**Definition** dbus-message-private.h:63

DBusMessage

Internals of DBusMessage.

**Definition** dbus-message-private.h:102

DBusSocket

Socket interface.

**Definition** dbus-sysdeps.h:185

DBusString

**Definition** dbus-string.h:47

DBusTransportVTable

The virtual table that must be implemented to create a new kind of transport.

**Definition** dbus-transport-protected.h:44

DBusTransportVTable::get_socket_fd

dbus_bool_t(\* get_socket_fd)(DBusTransport \*transport, DBusSocket \*fd_p)

Get socket file descriptor.

**Definition** dbus-transport-protected.h:71

DBusTransportVTable::disconnect

void(\* disconnect)(DBusTransport \*transport)

Disconnect this transport.

**Definition** dbus-transport-protected.h:55

DBusTransportVTable::live_messages_changed

void(\* live_messages_changed)(DBusTransport \*transport)

Outstanding messages counter changed.

**Definition** dbus-transport-protected.h:68

DBusTransportVTable::do_iteration

void(\* do_iteration)(DBusTransport \*transport, unsigned int flags, int timeout_milliseconds)

Called to do a single "iteration" (block on select/poll followed by reading or writing data).

**Definition** dbus-transport-protected.h:61

DBusTransportVTable::handle_watch

dbus_bool_t(\* handle_watch)(DBusTransport \*transport, DBusWatch \*watch, unsigned int flags)

The handle_watch method handles reading/writing data as indicated by the flags.

**Definition** dbus-transport-protected.h:48

DBusTransportVTable::finalize

void(\* finalize)(DBusTransport \*transport)

The finalize method must free the transport.

**Definition** dbus-transport-protected.h:45

DBusTransportVTable::connection_set

dbus_bool_t(\* connection_set)(DBusTransport \*transport)

Called when transport-\>connection has been filled in.

**Definition** dbus-transport-protected.h:58

DBusTransport

Object representing a transport such as a socket.

**Definition** dbus-transport-protected.h:83

DBusTransport::authenticated

unsigned int authenticated

Cache of auth state; use \_dbus_transport_peek_is_authenticated() to query value.

**Definition** dbus-transport-protected.h:116

DBusTransport::windows_user_function

DBusAllowWindowsUserFunction windows_user_function

Function for checking whether a user is authorized.

**Definition** dbus-transport-protected.h:110

DBusTransport::refcount

int refcount

Reference count.

**Definition** dbus-transport-protected.h:84

DBusTransport::max_live_messages_size

long max_live_messages_size

Max total size of received messages.

**Definition** dbus-transport-protected.h:96

DBusTransport::max_live_messages_unix_fds

long max_live_messages_unix_fds

Max total unix fds of received messages.

**Definition** dbus-transport-protected.h:97

DBusTransport::allow_anonymous

unsigned int allow_anonymous

TRUE if an anonymous client can connect

**Definition** dbus-transport-protected.h:121

DBusTransport::windows_user_data

void \* windows_user_data

Data for windows_user_function.

**Definition** dbus-transport-protected.h:111

DBusTransport::is_server

unsigned int is_server

TRUE if on the server side

**Definition** dbus-transport-protected.h:119

DBusTransport::disconnected

unsigned int disconnected

TRUE if we are disconnected.

**Definition** dbus-transport-protected.h:115

DBusTransport::address

char \* address

Address of the server we are connecting to (NULL for the server side of a transport)

**Definition** dbus-transport-protected.h:101

DBusTransport::unused_bytes_recovered

unsigned int unused_bytes_recovered

TRUE if we've recovered unused bytes from auth

**Definition** dbus-transport-protected.h:120

DBusTransport::vtable

const DBusTransportVTable \* vtable

Virtual methods for this instance.

**Definition** dbus-transport-protected.h:86

DBusTransport::free_unix_user_data

DBusFreeFunction free_unix_user_data

Function to free unix_user_data.

**Definition** dbus-transport-protected.h:108

DBusTransport::send_credentials_pending

unsigned int send_credentials_pending

TRUE if we need to send credentials

**Definition** dbus-transport-protected.h:117

DBusTransport::unix_user_data

void \* unix_user_data

Data for unix_user_function.

**Definition** dbus-transport-protected.h:106

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

DBusTransport::expected_guid

char \* expected_guid

GUID we expect the server to have, NULL on server side or if we don't have an expectation.

**Definition** dbus-transport-protected.h:103

DBusTransport::free_windows_user_data

DBusFreeFunction free_windows_user_data

Function to free windows_user_data.

**Definition** dbus-transport-protected.h:113

DBusTransport::unix_user_function

DBusAllowUnixUserFunction unix_user_function

Function for checking whether a user is authorized.

**Definition** dbus-transport-protected.h:105

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
