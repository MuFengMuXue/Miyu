dbus-server.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-server.c DBusServer object

3 \*

4 \* Copyright (C) 2002, 2003, 2004, 2005 Red Hat Inc.

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

27\#include "dbus-server.h"

28\#include "dbus-server-socket.h"

29\#include "dbus-string.h"

30\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

31\#include "dbus-server-debug-pipe.h"

32\#endif

33\#include "dbus-address.h"

34\#include "dbus-protocol.h"

35

57\#ifndef \_dbus_server_trace_ref

58void

59\_dbus_server_trace_ref (DBusServer \*server,

60 int old_refcount,

61 int new_refcount,

62 const char \*why)

63{

64 static int enabled = -1;

65

66 \_dbus_trace_ref ("DBusServer", server, old_refcount, new_refcount, why,

67 "DBUS_SERVER_TRACE", &enabled);

68}

69\#endif

70

71/\* this is a little fragile since it assumes the address doesn't

72 \* already have a guid, but it shouldn't

73 \*/

74static char\*

75copy_address_with_guid_appended (const DBusString \*address,

76 const DBusString \*guid_hex)

77{

78 DBusString with_guid;

79 char \*retval;

80

81 if (!\_dbus_string_init (&with_guid))

82 return NULL;

83

84 if (!\_dbus_string_copy (address, 0, &with_guid,

85 \_dbus_string_get_length (&with_guid)) \|\|

86 !\_dbus_string_append (&with_guid, ",guid=") \|\|

87 !\_dbus_string_copy (guid_hex, 0,

88 &with_guid, \_dbus_string_get_length (&with_guid)))

89 {

90 \_dbus_string_free (&with_guid);

91 return NULL;

92 }

93

94 retval = NULL;

95 \_dbus_string_steal_data (&with_guid, &retval);

96

97 \_dbus_string_free (&with_guid);

98

99 return retval; /\* may be NULL if steal_data failed \*/

100}

101

112dbus_bool_t

113\_dbus_server_init_base (DBusServer \*server,

114 const DBusServerVTable \*vtable,

115 const DBusString \*address,

116 DBusError \*error)

117{

118 server-\>vtable = vtable;

119

120\#ifdef DBUS_DISABLE_ASSERT

121 \_dbus_atomic_inc (&server-\>refcount);

122\#else

123 {

124 dbus_int32_t old_refcount = \_dbus_atomic_inc (&server-\>refcount);

125

126 \_dbus_assert (old_refcount == 0);

127 }

128\#endif

129

130 server-\>address = NULL;

131 server-\>watches = NULL;

132 server-\>timeouts = NULL;

133 server-\>published_address = FALSE;

134

135 if (!\_dbus_string_init (&server-\>guid_hex))

136 {

137 \_DBUS_SET_OOM (error);

138 return FALSE;

139 }

140

141 if (!\_dbus_generate_uuid (&server-\>guid, error))

142 goto failed;

143

144 if (!\_dbus_uuid_encode (&server-\>guid, &server-\>guid_hex))

145 goto oom;

146

147 server-\>address = copy_address_with_guid_appended (address,

148 &server-\>guid_hex);

149 if (server-\>address == NULL)

150 goto oom;

151

152 \_dbus_rmutex_new_at_location (&server-\>mutex);

153 if (server-\>mutex == NULL)

154 goto oom;

155

156 server-\>watches = \_dbus_watch_list_new ();

157 if (server-\>watches == NULL)

158 goto oom;

159

160 server-\>timeouts = \_dbus_timeout_list_new ();

161 if (server-\>timeouts == NULL)

162 goto oom;

163

164 \_dbus_data_slot_list_init (&server-\>slot_list);

165

166 \_dbus_verbose ("Initialized server on address %s\n", server-\>address);

167

168 return TRUE;

169

170 oom:

171 \_DBUS_SET_OOM (error);

172 failed:

173 \_dbus_rmutex_free_at_location (&server-\>mutex);

174 server-\>mutex = NULL;

175 if (server-\>watches)

176 {

177 \_dbus_watch_list_free (server-\>watches);

178 server-\>watches = NULL;

179 }

180 if (server-\>timeouts)

181 {

182 \_dbus_timeout_list_free (server-\>timeouts);

183 server-\>timeouts = NULL;

184 }

185 if (server-\>address)

186 {

187 dbus_free (server-\>address);

188 server-\>address = NULL;

189 }

190 \_dbus_string_free (&server-\>guid_hex);

191

192 return FALSE;

193}

194

201void

202\_dbus_server_finalize_base (DBusServer \*server)

203{

204 /\* We don't have the lock, but nobody should be accessing

205 \* concurrently since they don't have a ref

206 \*/

207\#ifndef DBUS_DISABLE_CHECKS

208 \_dbus_assert (!server-\>have_server_lock);

209\#endif

210 \_dbus_assert (server-\>disconnected);

211

212 /\* calls out to application code... \*/

213 \_dbus_data_slot_list_free (&server-\>slot_list);

214

215 dbus_server_set_new_connection_function (server, NULL, NULL, NULL);

216

217 \_dbus_watch_list_free (server-\>watches);

218 \_dbus_timeout_list_free (server-\>timeouts);

219

220 \_dbus_rmutex_free_at_location (&server-\>mutex);

221

222 dbus_free (server-\>address);

223

224 dbus_free_string_array (server-\>auth_mechanisms);

225

226 \_dbus_string_free (&server-\>guid_hex);

227}

228

229

231typedef dbus_bool_t (\* DBusWatchAddFunction) (DBusWatchList \*list,

232 DBusWatch \*watch);

234typedef void (\* DBusWatchRemoveFunction) (DBusWatchList \*list,

235 DBusWatch \*watch);

237typedef void (\* DBusWatchToggleFunction) (DBusWatchList \*list,

238 DBusWatch \*watch,

239 dbus_bool_t enabled);

240

241static dbus_bool_t

242protected_change_watch (DBusServer \*server,

243 DBusWatch \*watch,

244 DBusWatchAddFunction add_function,

245 DBusWatchRemoveFunction remove_function,

246 DBusWatchToggleFunction toggle_function,

247 dbus_bool_t enabled)

248{

249 DBusWatchList \*watches;

250 dbus_bool_t retval;

251

252 HAVE_LOCK_CHECK (server);

253

254 /\* This isn't really safe or reasonable; a better pattern is the "do

255 \* everything, then drop lock and call out" one; but it has to be

256 \* propagated up through all callers

257 \*/

258

259 watches = server-\>watches;

260 if (watches)

261 {

262 server-\>watches = NULL;

263 \_dbus_server_ref_unlocked (server);

264 SERVER_UNLOCK (server);

265

266 if (add_function)

267 retval = (\* add_function) (watches, watch);

268 else if (remove_function)

269 {

270 retval = TRUE;

271 (\* remove_function) (watches, watch);

272 }

273 else

274 {

275 retval = TRUE;

276 (\* toggle_function) (watches, watch, enabled);

277 }

278

279 SERVER_LOCK (server);

280 server-\>watches = watches;

281 \_dbus_server_unref_unlocked (server);

282

283 return retval;

284 }

285 else

286 return FALSE;

287}

288

296dbus_bool_t

297\_dbus_server_add_watch (DBusServer \*server,

298 DBusWatch \*watch)

299{

300 HAVE_LOCK_CHECK (server);

301 return protected_change_watch (server, watch,

302 \_dbus_watch_list_add_watch,

303 NULL, NULL, FALSE);

304}

305

312void

313\_dbus_server_remove_watch (DBusServer \*server,

314 DBusWatch \*watch)

315{

316 HAVE_LOCK_CHECK (server);

317 protected_change_watch (server, watch,

318 NULL,

319 \_dbus_watch_list_remove_watch,

320 NULL, FALSE);

321}

322

330void

331\_dbus_server_toggle_all_watches (DBusServer \*server,

332 dbus_bool_t enabled)

333{

334 \_dbus_watch_list_toggle_all_watches (server-\>watches, enabled);

335}

336

338typedef dbus_bool_t (\* DBusTimeoutAddFunction) (DBusTimeoutList \*list,

339 DBusTimeout \*timeout);

341typedef void (\* DBusTimeoutRemoveFunction) (DBusTimeoutList \*list,

342 DBusTimeout \*timeout);

344typedef void (\* DBusTimeoutToggleFunction) (DBusTimeoutList \*list,

345 DBusTimeout \*timeout,

346 dbus_bool_t enabled);

347

348

349static dbus_bool_t

350protected_change_timeout (DBusServer \*server,

351 DBusTimeout \*timeout,

352 DBusTimeoutAddFunction add_function,

353 DBusTimeoutRemoveFunction remove_function,

354 DBusTimeoutToggleFunction toggle_function,

355 dbus_bool_t enabled)

356{

357 DBusTimeoutList \*timeouts;

358 dbus_bool_t retval;

359

360 HAVE_LOCK_CHECK (server);

361

362 /\* This isn't really safe or reasonable; a better pattern is the "do everything, then

363 \* drop lock and call out" one; but it has to be propagated up through all callers

364 \*/

365

366 timeouts = server-\>timeouts;

367 if (timeouts)

368 {

369 server-\>timeouts = NULL;

370 \_dbus_server_ref_unlocked (server);

371 SERVER_UNLOCK (server);

372

373 if (add_function)

374 retval = (\* add_function) (timeouts, timeout);

375 else if (remove_function)

376 {

377 retval = TRUE;

378 (\* remove_function) (timeouts, timeout);

379 }

380 else

381 {

382 retval = TRUE;

383 (\* toggle_function) (timeouts, timeout, enabled);

384 }

385

386 SERVER_LOCK (server);

387 server-\>timeouts = timeouts;

388 \_dbus_server_unref_unlocked (server);

389

390 return retval;

391 }

392 else

393 return FALSE;

394}

395

405dbus_bool_t

406\_dbus_server_add_timeout (DBusServer \*server,

407 DBusTimeout \*timeout)

408{

409 return protected_change_timeout (server, timeout,

410 \_dbus_timeout_list_add_timeout,

411 NULL, NULL, FALSE);

412}

413

420void

421\_dbus_server_remove_timeout (DBusServer \*server,

422 DBusTimeout \*timeout)

423{

424 protected_change_timeout (server, timeout,

425 NULL,

426 \_dbus_timeout_list_remove_timeout,

427 NULL, FALSE);

428}

429

439void

440\_dbus_server_toggle_timeout (DBusServer \*server,

441 DBusTimeout \*timeout,

442 dbus_bool_t enabled)

443{

444 protected_change_timeout (server, timeout,

445 NULL, NULL,

446 \_dbus_timeout_list_toggle_timeout,

447 enabled);

448}

449

450

456void

457\_dbus_server_ref_unlocked (DBusServer \*server)

458{

459 dbus_int32_t old_refcount;

460

461 \_dbus_assert (server != NULL);

462 HAVE_LOCK_CHECK (server);

463

464 old_refcount = \_dbus_atomic_inc (&server-\>refcount);

465 \_dbus_assert (old_refcount \> 0);

466 \_dbus_server_trace_ref (server, old_refcount, old_refcount + 1,

467 "ref_unlocked");

468}

469

475void

476\_dbus_server_unref_unlocked (DBusServer \*server)

477{

478 dbus_int32_t old_refcount;

479

480 /\* Keep this in sync with dbus_server_unref \*/

481

482 \_dbus_assert (server != NULL);

483

484 HAVE_LOCK_CHECK (server);

485

486 old_refcount = \_dbus_atomic_dec (&server-\>refcount);

487 \_dbus_assert (old_refcount \> 0);

488

489 \_dbus_server_trace_ref (server, old_refcount, old_refcount - 1,

490 "unref_unlocked");

491

492 if (old_refcount == 1)

493 {

494 \_dbus_assert (server-\>disconnected);

495

496 SERVER_UNLOCK (server);

497

498 \_dbus_assert (server-\>vtable-\>finalize != NULL);

499

500 (\* server-\>vtable-\>finalize) (server);

501 }

502}

503

525static const struct {

526 DBusServerListenResult (\* func) (DBusAddressEntry \*entry,

527 DBusServer \*\*server_p,

528 DBusError \*error);

529} listen_funcs\[\] = {

530 { \_dbus_server_listen_socket }

531 , { \_dbus_server_listen_unix_socket }

532 , { \_dbus_server_listen_platform_specific }

533\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

534 , { \_dbus_server_listen_debug_pipe }

535\#endif

536};

537

558DBusServer\*

559dbus_server_listen (const char \*address,

560 DBusError \*error)

561{

562 DBusServer \*server;

563 DBusAddressEntry \*\*entries;

564 int len, i;

565 DBusError first_connect_error = DBUS_ERROR_INIT;

566 dbus_bool_t handled_once;

567

568 \_dbus_return_val_if_fail (address != NULL, NULL);

569 \_dbus_return_val_if_error_is_set (error, NULL);

570

571 if (!dbus_parse_address (address, &entries, &len, error))

572 return NULL;

573

574 server = NULL;

575 handled_once = FALSE;

576

577 for (i = 0; i \< len; i++)

578 {

579 int j;

580

581 for (j = 0; j \< (int) \_DBUS_N_ELEMENTS (listen_funcs); ++j)

582 {

583 DBusServerListenResult result;

584 DBusError tmp_error = DBUS_ERROR_INIT;

585

586 result = (\* listen_funcs\[j\].func) (entries\[i\],

587 &server,

588 &tmp_error);

589

590 if (result == DBUS_SERVER_LISTEN_OK)

591 {

592 \_dbus_assert (server != NULL);

593 \_DBUS_ASSERT_ERROR_IS_CLEAR (&tmp_error);

594 handled_once = TRUE;

595 goto out;

596 }

597 else if (result == DBUS_SERVER_LISTEN_ADDRESS_ALREADY_USED)

598 {

599 \_dbus_assert (server == NULL);

600 \_DBUS_ASSERT_ERROR_IS_CLEAR (&tmp_error);

601 dbus_set_error (error,

602 DBUS_ERROR_ADDRESS_IN_USE,

603 "Address '%s' already used",

604 dbus_address_entry_get_method (entries\[0\]));

605 handled_once = TRUE;

606 goto out;

607 }

608 else if (result == DBUS_SERVER_LISTEN_BAD_ADDRESS)

609 {

610 \_dbus_assert (server == NULL);

611 \_DBUS_ASSERT_ERROR_IS_SET (&tmp_error);

612 dbus_move_error (&tmp_error, error);

613 handled_once = TRUE;

614 goto out;

615 }

616 else if (result == DBUS_SERVER_LISTEN_NOT_HANDLED)

617 {

618 \_dbus_assert (server == NULL);

619 \_DBUS_ASSERT_ERROR_IS_CLEAR (&tmp_error);

620

621 /\* keep trying addresses \*/

622 }

623 else if (result == DBUS_SERVER_LISTEN_DID_NOT_CONNECT)

624 {

625 \_dbus_assert (server == NULL);

626 \_DBUS_ASSERT_ERROR_IS_SET (&tmp_error);

627 if (!dbus_error_is_set (&first_connect_error))

628 dbus_move_error (&tmp_error, &first_connect_error);

629 else

630 dbus_error_free (&tmp_error);

631

632 handled_once = TRUE;

633

634 /\* keep trying addresses \*/

635 }

636 else

637 {

638 \_dbus_assert_not_reached ("Unknown result in dbus_server_listen");

639 }

640 }

641

642 \_dbus_assert (server == NULL);

643 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

644 }

645

646 out:

647

648 if (!handled_once)

649 {

650 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

651 if (len \> 0)

652 dbus_set_error (error,

653 DBUS_ERROR_BAD_ADDRESS,

654 "Unknown address type '%s'",

655 dbus_address_entry_get_method (entries\[0\]));

656 else

657 dbus_set_error (error,

658 DBUS_ERROR_BAD_ADDRESS,

659 "Empty address '%s'",

660 address);

661 }

662

663 dbus_address_entries_free (entries);

664

665 if (server == NULL)

666 {

667 \_dbus_assert (error == NULL \|\| dbus_error_is_set (&first_connect_error) \|\|

668 dbus_error_is_set (error));

669

670 if (error && dbus_error_is_set (error))

671 {

672 /\* already set the error \*/

673 }

674 else

675 {

676 /\* didn't set the error but either error should be

677 \* NULL or first_connect_error should be set.

678 \*/

679 \_dbus_assert (error == NULL \|\| dbus_error_is_set (&first_connect_error));

680 dbus_move_error (&first_connect_error, error);

681 }

682

683 \_DBUS_ASSERT_ERROR_IS_CLEAR (&first_connect_error); /\* be sure we freed it \*/

684 \_DBUS_ASSERT_ERROR_IS_SET (error);

685

686 return NULL;

687 }

688 else

689 {

690 dbus_error_free (&first_connect_error);

691 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

692 return server;

693 }

694}

695

702DBusServer \*

703dbus_server_ref (DBusServer \*server)

704{

705 dbus_int32_t old_refcount;

706

707 \_dbus_return_val_if_fail (server != NULL, NULL);

708

709 old_refcount = \_dbus_atomic_inc (&server-\>refcount);

710

711\#ifndef DBUS_DISABLE_CHECKS

712 if (\_DBUS_UNLIKELY (old_refcount \<= 0))

713 {

714 \_dbus_atomic_dec (&server-\>refcount);

715 \_dbus_warn_return_if_fail (\_DBUS_FUNCTION_NAME, "old_refcount \> 0",

716 \_\_FILE\_\_, \_\_LINE\_\_);

717 return NULL;

718 }

719\#endif

720

721 \_dbus_server_trace_ref (server, old_refcount, old_refcount + 1, "ref");

722

723 return server;

724}

725

734void

735dbus_server_unref (DBusServer \*server)

736{

737 dbus_int32_t old_refcount;

738

739 /\* keep this in sync with unref_unlocked \*/

740

741 \_dbus_return_if_fail (server != NULL);

742

743 old_refcount = \_dbus_atomic_dec (&server-\>refcount);

744

745\#ifndef DBUS_DISABLE_CHECKS

746 if (\_DBUS_UNLIKELY (old_refcount \<= 0))

747 {

748 /\* undo side-effect first

749 \* please do not try to simplify the code here by using

750 \* \_dbus_atomic_get(), why we don't use it is

751 \* because it issues another atomic operation even though

752 \* DBUS_DISABLE_CHECKS defined.

753 \* Bug: https://bugs.freedesktop.org/show_bug.cgi?id=68303

754 \*/

755 \_dbus_atomic_inc (&server-\>refcount);

756 \_dbus_warn_return_if_fail (\_DBUS_FUNCTION_NAME, "old_refcount \> 0",

757 \_\_FILE\_\_, \_\_LINE\_\_);

758 return;

759 }

760\#endif

761

762 \_dbus_server_trace_ref (server, old_refcount, old_refcount - 1, "unref");

763

764 if (old_refcount == 1)

765 {

766 /\* lock not held! \*/

767 \_dbus_assert (server-\>disconnected);

768

769 \_dbus_assert (server-\>vtable-\>finalize != NULL);

770

771 (\* server-\>vtable-\>finalize) (server);

772 }

773}

774

775void

776\_dbus_server_disconnect_unlocked (DBusServer \*server)

777{

778 \_dbus_assert (server-\>vtable-\>disconnect != NULL);

779

780 if (!server-\>disconnected)

781 {

782 /\* this has to be first so recursive calls to disconnect don't happen \*/

783 server-\>disconnected = TRUE;

784

785 (\* server-\>vtable-\>disconnect) (server);

786 }

787}

788

797void

798dbus_server_disconnect (DBusServer \*server)

799{

800 \_dbus_return_if_fail (server != NULL);

801

802 dbus_server_ref (server);

803 SERVER_LOCK (server);

804

805 \_dbus_server_disconnect_unlocked (server);

806

807 SERVER_UNLOCK (server);

808 dbus_server_unref (server);

809}

810

816dbus_bool_t

817dbus_server_get_is_connected (DBusServer \*server)

818{

819 dbus_bool_t retval;

820

821 \_dbus_return_val_if_fail (server != NULL, FALSE);

822

823 SERVER_LOCK (server);

824 retval = !server-\>disconnected;

825 SERVER_UNLOCK (server);

826

827 return retval;

828}

829

837char\*

838dbus_server_get_address (DBusServer \*server)

839{

840 char \*retval;

841

842 \_dbus_return_val_if_fail (server != NULL, NULL);

843

844 SERVER_LOCK (server);

845 retval = \_dbus_strdup (server-\>address);

846 SERVER_UNLOCK (server);

847

848 return retval;

849}

850

873char\*

874dbus_server_get_id (DBusServer \*server)

875{

876 char \*retval;

877

878 \_dbus_return_val_if_fail (server != NULL, NULL);

879

880 SERVER_LOCK (server);

881 retval = NULL;

882 \_dbus_string_copy_data (&server-\>guid_hex, &retval);

883 SERVER_UNLOCK (server);

884

885 return retval;

886}

887

908void

909dbus_server_set_new_connection_function (DBusServer \*server,

910 DBusNewConnectionFunction function,

911 void \*data,

912 DBusFreeFunction free_data_function)

913{

914 DBusFreeFunction old_free_function;

915 void \*old_data;

916

917 \_dbus_return_if_fail (server != NULL);

918

919 SERVER_LOCK (server);

920 old_free_function = server-\>new_connection_free_data_function;

921 old_data = server-\>new_connection_data;

922

923 server-\>new_connection_function = function;

924 server-\>new_connection_data = data;

925 server-\>new_connection_free_data_function = free_data_function;

926 SERVER_UNLOCK (server);

927

928 if (old_free_function != NULL)

929 (\* old_free_function) (old_data);

930}

931

948dbus_bool_t

949dbus_server_set_watch_functions (DBusServer \*server,

950 DBusAddWatchFunction add_function,

951 DBusRemoveWatchFunction remove_function,

952 DBusWatchToggledFunction toggled_function,

953 void \*data,

954 DBusFreeFunction free_data_function)

955{

956 dbus_bool_t result;

957 DBusWatchList \*watches;

958

959 \_dbus_return_val_if_fail (server != NULL, FALSE);

960

961 SERVER_LOCK (server);

962 watches = server-\>watches;

963 server-\>watches = NULL;

964 if (watches)

965 {

966 SERVER_UNLOCK (server);

967 result = \_dbus_watch_list_set_functions (watches,

968 add_function,

969 remove_function,

970 toggled_function,

971 data,

972 free_data_function);

973 SERVER_LOCK (server);

974 }

975 else

976 {

977 \_dbus_warn_check_failed ("Re-entrant call to %s", \_DBUS_FUNCTION_NAME);

978 result = FALSE;

979 }

980 server-\>watches = watches;

981 SERVER_UNLOCK (server);

982

983 return result;

984}

985

1001dbus_bool_t

1002dbus_server_set_timeout_functions (DBusServer \*server,

1003 DBusAddTimeoutFunction add_function,

1004 DBusRemoveTimeoutFunction remove_function,

1005 DBusTimeoutToggledFunction toggled_function,

1006 void \*data,

1007 DBusFreeFunction free_data_function)

1008{

1009 dbus_bool_t result;

1010 DBusTimeoutList \*timeouts;

1011

1012 \_dbus_return_val_if_fail (server != NULL, FALSE);

1013

1014 SERVER_LOCK (server);

1015 timeouts = server-\>timeouts;

1016 server-\>timeouts = NULL;

1017 if (timeouts)

1018 {

1019 SERVER_UNLOCK (server);

1020 result = \_dbus_timeout_list_set_functions (timeouts,

1021 add_function,

1022 remove_function,

1023 toggled_function,

1024 data,

1025 free_data_function);

1026 SERVER_LOCK (server);

1027 }

1028 else

1029 {

1030 \_dbus_warn_check_failed ("Re-entrant call to %s", \_DBUS_FUNCTION_NAME);

1031 result = FALSE;

1032 }

1033 server-\>timeouts = timeouts;

1034 SERVER_UNLOCK (server);

1035

1036 return result;

1037}

1038

1052dbus_bool_t

1053dbus_server_set_auth_mechanisms (DBusServer \*server,

1054 const char \*\*mechanisms)

1055{

1056 char \*\*copy;

1057

1058 \_dbus_return_val_if_fail (server != NULL, FALSE);

1059

1060 SERVER_LOCK (server);

1061

1062 if (mechanisms != NULL)

1063 {

1064 copy = \_dbus_dup_string_array (mechanisms);

1065 if (copy == NULL)

1066 {

1067 SERVER_UNLOCK (server);

1068 return FALSE;

1069 }

1070 }

1071 else

1072 copy = NULL;

1073

1074 dbus_free_string_array (server-\>auth_mechanisms);

1075 server-\>auth_mechanisms = copy;

1076

1077 SERVER_UNLOCK (server);

1078

1079 return TRUE;

1080}

1081

1082static DBusDataSlotAllocator slot_allocator =

1083 \_DBUS_DATA_SLOT_ALLOCATOR_INIT (\_DBUS_LOCK_NAME (server_slots));

1084

1099dbus_bool_t

1100dbus_server_allocate_data_slot (dbus_int32_t \*slot_p)

1101{

1102 return \_dbus_data_slot_allocator_alloc (&slot_allocator,

1103 slot_p);

1104}

1105

1117void

1118dbus_server_free_data_slot (dbus_int32_t \*slot_p)

1119{

1120 \_dbus_return_if_fail (\*slot_p \>= 0);

1121

1122 \_dbus_data_slot_allocator_free (&slot_allocator, slot_p);

1123}

1124

1138dbus_bool_t

1139dbus_server_set_data (DBusServer \*server,

1140 int slot,

1141 void \*data,

1142 DBusFreeFunction free_data_func)

1143{

1144 DBusFreeFunction old_free_func;

1145 void \*old_data;

1146 dbus_bool_t retval;

1147

1148 \_dbus_return_val_if_fail (server != NULL, FALSE);

1149

1150 SERVER_LOCK (server);

1151

1152 retval = \_dbus_data_slot_list_set (&slot_allocator,

1153 &server-\>slot_list,

1154 slot, data, free_data_func,

1155 &old_free_func, &old_data);

1156

1157

1158 SERVER_UNLOCK (server);

1159

1160 if (retval)

1161 {

1162 /\* Do the actual free outside the server lock \*/

1163 if (old_free_func)

1164 (\* old_free_func) (old_data);

1165 }

1166

1167 return retval;

1168}

1169

1178void\*

1179dbus_server_get_data (DBusServer \*server,

1180 int slot)

1181{

1182 void \*res;

1183

1184 \_dbus_return_val_if_fail (server != NULL, NULL);

1185

1186 SERVER_LOCK (server);

1187

1188 res = \_dbus_data_slot_list_get (&slot_allocator,

1189 &server-\>slot_list,

1190 slot);

1191

1192 SERVER_UNLOCK (server);

1193

1194 return res;

1195}

1196

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

DBusWatchToggledFunction

void(\* DBusWatchToggledFunction)(DBusWatch \*watch, void \*data)

Called when dbus_watch_get_enabled() may return a different value than it did before.

**Definition** dbus-connection.h:100

DBusAddWatchFunction

dbus_bool_t(\* DBusAddWatchFunction)(DBusWatch \*watch, void \*data)

Called when libdbus needs a new watch to be monitored by the main loop.

**Definition** dbus-connection.h:94

DBusTimeoutToggledFunction

void(\* DBusTimeoutToggledFunction)(DBusTimeout \*timeout, void \*data)

Called when dbus_timeout_get_enabled() may return a different value than it did before.

**Definition** dbus-connection.h:120

DBusAddTimeoutFunction

dbus_bool_t(\* DBusAddTimeoutFunction)(DBusTimeout \*timeout, void \*data)

Called when libdbus needs a new timeout to be monitored by the main loop.

**Definition** dbus-connection.h:113

DBusRemoveWatchFunction

void(\* DBusRemoveWatchFunction)(DBusWatch \*watch, void \*data)

Called when libdbus no longer needs a watch to be monitored by the main loop.

**Definition** dbus-connection.h:106

DBusRemoveTimeoutFunction

void(\* DBusRemoveTimeoutFunction)(DBusTimeout \*timeout, void \*data)

Called when libdbus no longer needs a timeout to be monitored by the main loop.

**Definition** dbus-connection.h:126

\_dbus_data_slot_allocator_free

void \_dbus_data_slot_allocator_free(DBusDataSlotAllocator \*allocator, dbus_int32_t \*slot_id_p)

Deallocates an ID previously allocated with \_dbus_data_slot_allocator_alloc().

**Definition** dbus-dataslot.c:157

\_dbus_data_slot_list_init

void \_dbus_data_slot_list_init(DBusDataSlotList \*list)

Initializes a slot list.

**Definition** dbus-dataslot.c:200

\_dbus_data_slot_list_free

void \_dbus_data_slot_list_free(DBusDataSlotList \*list)

Frees the data slot list and all data slots contained in it, calling application-provided free functi...

**Definition** dbus-dataslot.c:343

\_dbus_data_slot_list_get

void \* \_dbus_data_slot_list_get(DBusDataSlotAllocator \*allocator, DBusDataSlotList \*list, int slot)

Retrieves data previously set with \_dbus_data_slot_list_set_data().

**Definition** dbus-dataslot.c:288

\_dbus_data_slot_list_set

dbus_bool_t \_dbus_data_slot_list_set(DBusDataSlotAllocator \*allocator, DBusDataSlotList \*list, int slot, void \*data, DBusFreeFunction free_data_func, DBusFreeFunction \*old_free_func, void \*\*old_data)

Stores a pointer in the data slot list, along with an optional function to be used for freeing the da...

**Definition** dbus-dataslot.c:224

\_dbus_data_slot_allocator_alloc

dbus_bool_t \_dbus_data_slot_allocator_alloc(DBusDataSlotAllocator \*allocator, dbus_int32_t \*slot_id_p)

Allocates an integer ID to be used for storing data in a DBusDataSlotList.

**Definition** dbus-dataslot.c:72

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

\_dbus_generate_uuid

dbus_bool_t \_dbus_generate_uuid(DBusGUID \*uuid, DBusError \*error)

Generates a new UUID.

**Definition** dbus-internals.c:752

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

\_DBUS_LOCK_NAME

\#define \_DBUS_LOCK_NAME(name)

Expands to name of a global lock variable.

**Definition** dbus-internals.h:436

\_dbus_uuid_encode

dbus_bool_t \_dbus_uuid_encode(const DBusGUID \*uuid, DBusString \*encoded)

Hex-encode a UUID.

**Definition** dbus-internals.c:788

\_dbus_dup_string_array

char \*\* \_dbus_dup_string_array(const char \*\*array)

Duplicates a string array.

**Definition** dbus-internals.c:672

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

dbus_free_string_array

void dbus_free_string_array(char \*\*str_array)

Frees a NULL-terminated array of strings.

**Definition** dbus-memory.c:758

DBUS_ERROR_ADDRESS_IN_USE

\#define DBUS_ERROR_ADDRESS_IN_USE

Can't bind a socket since its address is in use (i.e.

**Definition** dbus-protocol.h:393

DBUS_ERROR_BAD_ADDRESS

\#define DBUS_ERROR_BAD_ADDRESS

A D-Bus bus address was malformed.

**Definition** dbus-protocol.h:373

\_dbus_server_add_watch

dbus_bool_t \_dbus_server_add_watch(DBusServer \*server, DBusWatch \*watch)

Adds a watch for this server, chaining out to application-provided watch handlers.

**Definition** dbus-server.c:297

DBusWatchRemoveFunction

void(\* DBusWatchRemoveFunction)(DBusWatchList \*list, DBusWatch \*watch)

Function to be called in protected_change_watch() with refcount held.

**Definition** dbus-server.c:234

\_dbus_server_remove_watch

void \_dbus_server_remove_watch(DBusServer \*server, DBusWatch \*watch)

Removes a watch previously added with \_dbus_server_remove_watch().

**Definition** dbus-server.c:313

\_dbus_server_remove_timeout

void \_dbus_server_remove_timeout(DBusServer \*server, DBusTimeout \*timeout)

Removes a timeout previously added with \_dbus_server_add_timeout().

**Definition** dbus-server.c:421

\_dbus_server_unref_unlocked

void \_dbus_server_unref_unlocked(DBusServer \*server)

Like dbus_server_unref() but does not acquire the lock (must already be held)

**Definition** dbus-server.c:476

\_dbus_server_toggle_timeout

void \_dbus_server_toggle_timeout(DBusServer \*server, DBusTimeout \*timeout, dbus_bool_t enabled)

Toggles a timeout and notifies app via server's DBusTimeoutToggledFunction if available.

**Definition** dbus-server.c:440

DBusTimeoutToggleFunction

void(\* DBusTimeoutToggleFunction)(DBusTimeoutList \*list, DBusTimeout \*timeout, dbus_bool_t enabled)

Function to be called in protected_change_timeout() with refcount held.

**Definition** dbus-server.c:344

DBusTimeoutRemoveFunction

void(\* DBusTimeoutRemoveFunction)(DBusTimeoutList \*list, DBusTimeout \*timeout)

Function to be called in protected_change_timeout() with refcount held.

**Definition** dbus-server.c:341

\_dbus_server_add_timeout

dbus_bool_t \_dbus_server_add_timeout(DBusServer \*server, DBusTimeout \*timeout)

Adds a timeout for this server, chaining out to application-provided timeout handlers.

**Definition** dbus-server.c:406

\_dbus_server_init_base

dbus_bool_t \_dbus_server_init_base(DBusServer \*server, const DBusServerVTable \*vtable, const DBusString \*address, DBusError \*error)

Initializes the members of the DBusServer base class.

**Definition** dbus-server.c:113

\_dbus_server_finalize_base

void \_dbus_server_finalize_base(DBusServer \*server)

Finalizes the members of the DBusServer base class.

**Definition** dbus-server.c:202

\_dbus_server_ref_unlocked

void \_dbus_server_ref_unlocked(DBusServer \*server)

Like dbus_server_ref() but does not acquire the lock (must already be held)

**Definition** dbus-server.c:457

DBusTimeoutAddFunction

dbus_bool_t(\* DBusTimeoutAddFunction)(DBusTimeoutList \*list, DBusTimeout \*timeout)

Function to be called in protected_change_timeout() with refcount held.

**Definition** dbus-server.c:338

DBusWatchToggleFunction

void(\* DBusWatchToggleFunction)(DBusWatchList \*list, DBusWatch \*watch, dbus_bool_t enabled)

Function to be called in protected_change_watch() with refcount held.

**Definition** dbus-server.c:237

\_dbus_server_toggle_all_watches

void \_dbus_server_toggle_all_watches(DBusServer \*server, dbus_bool_t enabled)

Toggles all watch and notifies app via server's DBusWatchToggledFunction if available.

**Definition** dbus-server.c:331

DBusWatchAddFunction

dbus_bool_t(\* DBusWatchAddFunction)(DBusWatchList \*list, DBusWatch \*watch)

Function to be called in protected_change_watch() with refcount held.

**Definition** dbus-server.c:231

\_dbus_server_listen_socket

DBusServerListenResult \_dbus_server_listen_socket(DBusAddressEntry \*entry, DBusServer \*\*server_p, DBusError \*error)

Tries to interpret the address entry for various socket-related addresses (well, currently only tcp a...

**Definition** dbus-server-socket.c:540

\_dbus_server_listen_unix_socket

DBusServerListenResult \_dbus_server_listen_unix_socket(DBusAddressEntry \*entry, DBusServer \*\*server_p, DBusError \*error)

Tries to interpret the address entry for UNIX socket addresses.

**Definition** dbus-server-socket.c:761

\_dbus_server_listen_platform_specific

DBusServerListenResult \_dbus_server_listen_platform_specific(DBusAddressEntry \*entry, DBusServer \*\*server_p, DBusError \*error)

Tries to interpret the address entry in a platform-specific way, creating a platform-specific server ...

**Definition** dbus-server-unix.c:55

dbus_server_allocate_data_slot

dbus_bool_t dbus_server_allocate_data_slot(dbus_int32_t \*slot_p)

Allocates an integer ID to be used for storing application-specific data on any DBusServer.

**Definition** dbus-server.c:1100

dbus_server_disconnect

void dbus_server_disconnect(DBusServer \*server)

Releases the server's address and stops listening for new clients.

**Definition** dbus-server.c:798

dbus_server_set_auth_mechanisms

dbus_bool_t dbus_server_set_auth_mechanisms(DBusServer \*server, const char \*\*mechanisms)

Sets the authentication mechanisms that this server offers to clients, as a NULL-terminated array of ...

**Definition** dbus-server.c:1053

dbus_server_get_id

char \* dbus_server_get_id(DBusServer \*server)

Returns the unique ID of the server, as a newly-allocated string which must be freed by the caller.

**Definition** dbus-server.c:874

dbus_server_listen

DBusServer \* dbus_server_listen(const char \*address, DBusError \*error)

Listens for new connections on the given address.

**Definition** dbus-server.c:559

dbus_server_get_address

char \* dbus_server_get_address(DBusServer \*server)

Returns the address of the server, as a newly-allocated string which must be freed by the caller.

**Definition** dbus-server.c:838

dbus_server_get_is_connected

dbus_bool_t dbus_server_get_is_connected(DBusServer \*server)

Returns TRUE if the server is still listening for new connections.

**Definition** dbus-server.c:817

dbus_server_unref

void dbus_server_unref(DBusServer \*server)

Decrements the reference count of a DBusServer.

**Definition** dbus-server.c:735

dbus_server_set_new_connection_function

void dbus_server_set_new_connection_function(DBusServer \*server, DBusNewConnectionFunction function, void \*data, DBusFreeFunction free_data_function)

Sets a function to be used for handling new connections.

**Definition** dbus-server.c:909

dbus_server_set_watch_functions

dbus_bool_t dbus_server_set_watch_functions(DBusServer \*server, DBusAddWatchFunction add_function, DBusRemoveWatchFunction remove_function, DBusWatchToggledFunction toggled_function, void \*data, DBusFreeFunction free_data_function)

Sets the watch functions for the server.

**Definition** dbus-server.c:949

dbus_server_set_data

dbus_bool_t dbus_server_set_data(DBusServer \*server, int slot, void \*data, DBusFreeFunction free_data_func)

Stores a pointer on a DBusServer, along with an optional function to be used for freeing the data whe...

**Definition** dbus-server.c:1139

dbus_server_ref

DBusServer \* dbus_server_ref(DBusServer \*server)

Increments the reference count of a DBusServer.

**Definition** dbus-server.c:703

dbus_server_get_data

void \* dbus_server_get_data(DBusServer \*server, int slot)

Retrieves data previously set with dbus_server_set_data().

**Definition** dbus-server.c:1179

dbus_server_free_data_slot

void dbus_server_free_data_slot(dbus_int32_t \*slot_p)

Deallocates a global ID for server data slots.

**Definition** dbus-server.c:1118

dbus_server_set_timeout_functions

dbus_bool_t dbus_server_set_timeout_functions(DBusServer \*server, DBusAddTimeoutFunction add_function, DBusRemoveTimeoutFunction remove_function, DBusTimeoutToggledFunction toggled_function, void \*data, DBusFreeFunction free_data_function)

Sets the timeout functions for the server.

**Definition** dbus-server.c:1002

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

\_dbus_string_copy

dbus_bool_t \_dbus_string_copy(const DBusString \*source, int start, DBusString \*dest, int insert_at)

Like \_dbus_string_move(), but does not delete the section of the source string that's copied to the d...

**Definition** dbus-string.c:1345

\_dbus_string_steal_data

dbus_bool_t \_dbus_string_steal_data(DBusString \*str, char \*\*data_return)

Like \_dbus_string_get_data(), but removes the gotten data from the original string.

**Definition** dbus-string.c:686

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

\_dbus_atomic_dec

dbus_int32_t \_dbus_atomic_dec(DBusAtomic \*atomic)

Atomically decrement an integer.

**Definition** dbus-sysdeps-unix.c:3205

\_dbus_atomic_inc

dbus_int32_t \_dbus_atomic_inc(DBusAtomic \*atomic)

Atomically increments an integer.

**Definition** dbus-sysdeps-unix.c:3178

\_dbus_rmutex_new_at_location

void \_dbus_rmutex_new_at_location(DBusRMutex \*\*location_p)

Creates a new mutex or creates a no-op mutex if threads are not initialized.

**Definition** dbus-threads.c:56

\_dbus_rmutex_free_at_location

void \_dbus_rmutex_free_at_location(DBusRMutex \*\*location_p)

Frees a DBusRMutex; does nothing if passed a NULL pointer.

**Definition** dbus-threads.c:97

\_dbus_timeout_list_add_timeout

dbus_bool_t \_dbus_timeout_list_add_timeout(DBusTimeoutList \*timeout_list, DBusTimeout \*timeout)

Adds a new timeout to the timeout list, invoking the application DBusAddTimeoutFunction if appropriat...

**Definition** dbus-timeout.c:314

\_dbus_timeout_list_free

void \_dbus_timeout_list_free(DBusTimeoutList \*timeout_list)

Frees a DBusTimeoutList.

**Definition** dbus-timeout.c:217

\_dbus_timeout_list_toggle_timeout

void \_dbus_timeout_list_toggle_timeout(DBusTimeoutList \*timeout_list, DBusTimeout \*timeout, dbus_bool_t enabled)

Sets a timeout to the given enabled state, invoking the application's DBusTimeoutToggledFunction if a...

**Definition** dbus-timeout.c:366

\_dbus_timeout_list_new

DBusTimeoutList \* \_dbus_timeout_list_new(void)

Creates a new timeout list.

**Definition** dbus-timeout.c:200

\_dbus_timeout_list_set_functions

dbus_bool_t \_dbus_timeout_list_set_functions(DBusTimeoutList \*timeout_list, DBusAddTimeoutFunction add_function, DBusRemoveTimeoutFunction remove_function, DBusTimeoutToggledFunction toggled_function, void \*data, DBusFreeFunction free_data_function)

Sets the timeout functions.

**Definition** dbus-timeout.c:243

\_dbus_timeout_list_remove_timeout

void \_dbus_timeout_list_remove_timeout(DBusTimeoutList \*timeout_list, DBusTimeout \*timeout)

Removes a timeout from the timeout list, invoking the application's DBusRemoveTimeoutFunction if appr...

**Definition** dbus-timeout.c:344

\_dbus_watch_list_add_watch

dbus_bool_t \_dbus_watch_list_add_watch(DBusWatchList \*watch_list, DBusWatch \*watch)

Adds a new watch to the watch list, invoking the application DBusAddWatchFunction if appropriate.

**Definition** dbus-watch.c:383

\_dbus_watch_list_new

DBusWatchList \* \_dbus_watch_list_new(void)

Creates a new watch list.

**Definition** dbus-watch.c:234

\_dbus_watch_list_free

void \_dbus_watch_list_free(DBusWatchList \*watch_list)

Frees a DBusWatchList.

**Definition** dbus-watch.c:251

\_dbus_watch_list_set_functions

dbus_bool_t \_dbus_watch_list_set_functions(DBusWatchList \*watch_list, DBusAddWatchFunction add_function, DBusRemoveWatchFunction remove_function, DBusWatchToggledFunction toggled_function, void \*data, DBusFreeFunction free_data_function)

Sets the watch functions.

**Definition** dbus-watch.c:297

\_dbus_watch_list_toggle_all_watches

void \_dbus_watch_list_toggle_all_watches(DBusWatchList \*watch_list, dbus_bool_t enabled)

Sets all watches to the given enabled state, invoking the application's DBusWatchToggledFunction if a...

**Definition** dbus-watch.c:474

\_dbus_watch_list_remove_watch

void \_dbus_watch_list_remove_watch(DBusWatchList \*watch_list, DBusWatch \*watch)

Removes a watch from the watch list, invoking the application's DBusRemoveWatchFunction if appropriat...

**Definition** dbus-watch.c:416

DBusAddressEntry

Internals of DBusAddressEntry.

**Definition** dbus-address.c:49

DBusDataSlotAllocator

An allocator that tracks a set of slot IDs.

**Definition** dbus-dataslot.h:58

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusServerVTable

Virtual table to be implemented by all server "subclasses".

**Definition** dbus-server-protected.h:46

DBusServerVTable::disconnect

void(\* disconnect)(DBusServer \*server)

Disconnect this server.

**Definition** dbus-server-protected.h:50

DBusServerVTable::finalize

void(\* finalize)(DBusServer \*server)

The finalize method must free the server.

**Definition** dbus-server-protected.h:47

DBusServer

Internals of DBusServer object.

**Definition** dbus-server-protected.h:59

DBusServer::published_address

dbus_bool_t published_address

flag which indicates that server has published its bus address.

**Definition** dbus-server-protected.h:72

DBusServer::slot_list

DBusDataSlotList slot_list

Data stored by allocated integer ID.

**Definition** dbus-server-protected.h:76

DBusServer::address

char \* address

Address this server is listening on.

**Definition** dbus-server-protected.h:71

DBusServer::new_connection_free_data_function

DBusFreeFunction new_connection_free_data_function

Callback to invoke to free new_connection_data when server is finalized or data is replaced.

**Definition** dbus-server-protected.h:82

DBusServer::refcount

DBusAtomic refcount

Reference count.

**Definition** dbus-server-protected.h:60

DBusServer::watches

DBusWatchList \* watches

Our watches.

**Definition** dbus-server-protected.h:68

DBusServer::guid

DBusGUID guid

Globally unique ID of server.

**Definition** dbus-server-protected.h:64

DBusServer::guid_hex

DBusString guid_hex

Hex-encoded version of GUID.

**Definition** dbus-server-protected.h:66

DBusServer::disconnected

unsigned int disconnected

TRUE if we are disconnected.

**Definition** dbus-server-protected.h:89

DBusServer::mutex

DBusRMutex \* mutex

Lock on the server object.

**Definition** dbus-server-protected.h:62

DBusServer::new_connection_function

DBusNewConnectionFunction new_connection_function

Callback to invoke when a new connection is created.

**Definition** dbus-server-protected.h:78

DBusServer::vtable

const DBusServerVTable \* vtable

Virtual methods for this instance.

**Definition** dbus-server-protected.h:61

DBusServer::new_connection_data

void \* new_connection_data

Data for new connection callback.

**Definition** dbus-server-protected.h:80

DBusServer::have_server_lock

unsigned int have_server_lock

Does someone have the server mutex locked.

**Definition** dbus-server-protected.h:92

DBusServer::auth_mechanisms

char \*\* auth_mechanisms

Array of allowed authentication mechanisms.

**Definition** dbus-server-protected.h:87

DBusServer::timeouts

DBusTimeoutList \* timeouts

Our timeouts.

**Definition** dbus-server-protected.h:69

DBusString

**Definition** dbus-string.h:47

DBusTimeoutList

DBusTimeoutList implementation details.

**Definition** dbus-timeout.c:183

DBusTimeout

Internals of DBusTimeout.

**Definition** dbus-timeout.c:43

DBusWatchList

DBusWatchList implementation details.

**Definition** dbus-watch.c:217

DBusWatch

Implementation of DBusWatch.

**Definition** dbus-watch.c:43
