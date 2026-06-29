dbus-bus.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-bus.c Convenience functions for communicating with the bus.

3 \*

4 \* Copyright (C) 2003 CodeFactory AB

5 \* Copyright (C) 2003 Red Hat, Inc.

6 \*

7 \* SPDX-License-Identifier: AFL-2.1 OR GPL-2.0-or-later

8 \*

9 \* Licensed under the Academic Free License version 2.1

10 \*

11 \* This program is free software; you can redistribute it and/or modify

12 \* it under the terms of the GNU General Public License as published by

13 \* the Free Software Foundation; either version 2 of the License, or

14 \* (at your option) any later version.

15 \*

16 \* This program is distributed in the hope that it will be useful,

17 \* but WITHOUT ANY WARRANTY; without even the implied warranty of

18 \* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the

19 \* GNU General Public License for more details.

20 \*

21 \* You should have received a copy of the GNU General Public License

22 \* along with this program; if not, write to the Free Software

23 \* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

24 \*

25 \*/

26

27\#include \<config.h\>

28\#include "dbus-bus.h"

29\#include "dbus-protocol.h"

30\#include "dbus-internals.h"

31\#include "dbus-message.h"

32\#include "dbus-marshal-validate.h"

33\#include "dbus-misc.h"

34\#include "dbus-threads-internal.h"

35\#include "dbus-connection-internal.h"

36\#include "dbus-string.h"

37

79typedef struct

80{

81 DBusConnection \*connection;

82 char \*unique_name;

84 unsigned int is_well_known : 1;

85} BusData;

86

90static dbus_int32_t bus_data_slot = -1;

91

93\#define N_BUS_TYPES 3

94

95/\* Protected by \_DBUS_LOCK_bus, except during shutdown, which can't safely

96 \* be done in a threaded application anyway. \*/

97static DBusConnection \*bus_connections\[N_BUS_TYPES\];

98static char \*bus_connection_addresses\[N_BUS_TYPES\] = { NULL, NULL, NULL };

99static DBusBusType activation_bus_type = DBUS_BUS_STARTER;

100static dbus_bool_t initialized = FALSE;

101

102static void

103addresses_shutdown_func (void \*data)

104{

105 int i;

106

107 i = 0;

108 while (i \< N_BUS_TYPES)

109 {

110 if (bus_connections\[i\] != NULL)

111 \_dbus_warn_check_failed ("dbus_shutdown() called but connections were still live. This probably means the application did not drop all its references to bus connections.");

112

113 dbus_free (bus_connection_addresses\[i\]);

114 bus_connection_addresses\[i\] = NULL;

115 ++i;

116 }

117

118 activation_bus_type = DBUS_BUS_STARTER;

119

120 initialized = FALSE;

121}

122

123static dbus_bool_t

124get_from_env (char \*\*connection_p,

125 const char \*env_var)

126{

127 const char \*s;

128

129 \_dbus_assert (\*connection_p == NULL);

130

131 s = \_dbus_getenv (env_var);

132 if (s == NULL \|\| \*s == '\0')

133 return TRUE; /\* successfully didn't use the env var \*/

134 else

135 {

136 \*connection_p = \_dbus_strdup (s);

137 return \*connection_p != NULL;

138 }

139}

140

141static dbus_bool_t

142init_session_address (void)

143{

144 dbus_bool_t retval;

145

146 retval = FALSE;

147

148 /\* First, look in the environment. This is the normal case on

149 \* freedesktop.org/Unix systems. \*/

150 get_from_env (&bus_connection_addresses\[DBUS_BUS_SESSION\],

151 "DBUS_SESSION_BUS_ADDRESS");

152 if (bus_connection_addresses\[DBUS_BUS_SESSION\] == NULL)

153 {

154 dbus_bool_t supported;

155 DBusString addr;

156 DBusError error = DBUS_ERROR_INIT;

157

158 if (!\_dbus_string_init (&addr))

159 return FALSE;

160

161 supported = FALSE;

162 /\* So it's not in the environment - let's try a platform-specific method.

163 \* On MacOS, this involves asking launchd. On Windows (not specified yet)

164 \* we might do a COM lookup.

165 \* Ignore errors - if we failed, fall back to autolaunch. \*/

166 retval = \_dbus_lookup_session_address (&supported, &addr, &error);

167 if (supported && retval)

168 {

169 retval =\_dbus_string_steal_data (&addr, &bus_connection_addresses\[DBUS_BUS_SESSION\]);

170 }

171 else if (supported && !retval)

172 {

173 if (dbus_error_is_set(&error))

174 \_dbus_warn ("Dynamic session lookup supported but failed: %s", error.message);

175 else

176 \_dbus_warn ("Dynamic session lookup supported but failed silently");

177 }

178 \_dbus_string_free (&addr);

179 }

180 else

181 retval = TRUE;

182

183 if (!retval)

184 return FALSE;

185

186 /\* We have a hard-coded (but compile-time-configurable) fallback address for

187 \* the session bus. \*/

188 if (bus_connection_addresses\[DBUS_BUS_SESSION\] == NULL)

189 bus_connection_addresses\[DBUS_BUS_SESSION\] =

190 \_dbus_strdup (DBUS_SESSION_BUS_CONNECT_ADDRESS);

191

192 if (bus_connection_addresses\[DBUS_BUS_SESSION\] == NULL)

193 return FALSE;

194

195 return TRUE;

196}

197

198static dbus_bool_t

199init_connections_unlocked (void)

200{

201 if (!initialized)

202 {

203 const char \*s;

204 int i;

205

206 i = 0;

207 while (i \< N_BUS_TYPES)

208 {

209 bus_connections\[i\] = NULL;

210 ++i;

211 }

212

213 /\* Don't init these twice, we may run this code twice if

214 \* init_connections_unlocked() fails midway through.

215 \* In practice, each block below should contain only one

216 \* "return FALSE" or running through twice may not

217 \* work right.

218 \*/

219

220 if (bus_connection_addresses\[DBUS_BUS_SYSTEM\] == NULL)

221 {

222 \_dbus_verbose ("Filling in system bus address...\n");

223

224 if (!get_from_env (&bus_connection_addresses\[DBUS_BUS_SYSTEM\],

225 "DBUS_SYSTEM_BUS_ADDRESS"))

226 return FALSE;

227 }

228

229

230 if (bus_connection_addresses\[DBUS_BUS_SYSTEM\] == NULL)

231 {

232 /\* Use default system bus address if none set in environment \*/

233 bus_connection_addresses\[DBUS_BUS_SYSTEM\] =

234 \_dbus_strdup (DBUS_SYSTEM_BUS_DEFAULT_ADDRESS);

235

236 if (bus_connection_addresses\[DBUS_BUS_SYSTEM\] == NULL)

237 return FALSE;

238

239 \_dbus_verbose (" used default system bus \\%s\\\n",

240 bus_connection_addresses\[DBUS_BUS_SYSTEM\]);

241 }

242 else

243 \_dbus_verbose (" used env var system bus \\%s\\\n",

244 bus_connection_addresses\[DBUS_BUS_SYSTEM\]);

245

246 if (bus_connection_addresses\[DBUS_BUS_SESSION\] == NULL)

247 {

248 \_dbus_verbose ("Filling in session bus address...\n");

249

250 if (!init_session_address ())

251 return FALSE;

252

253 \_dbus_verbose (" \\%s\\\n", bus_connection_addresses\[DBUS_BUS_SESSION\] ?

254 bus_connection_addresses\[DBUS_BUS_SESSION\] : "none set");

255 }

256

257 if (bus_connection_addresses\[DBUS_BUS_STARTER\] == NULL)

258 {

259 \_dbus_verbose ("Filling in activation bus address...\n");

260

261 if (!get_from_env (&bus_connection_addresses\[DBUS_BUS_STARTER\],

262 "DBUS_STARTER_ADDRESS"))

263 return FALSE;

264

265 \_dbus_verbose (" \\%s\\\n", bus_connection_addresses\[DBUS_BUS_STARTER\] ?

266 bus_connection_addresses\[DBUS_BUS_STARTER\] : "none set");

267 }

268

269

270 if (bus_connection_addresses\[DBUS_BUS_STARTER\] != NULL)

271 {

272 s = \_dbus_getenv ("DBUS_STARTER_BUS_TYPE");

273

274 if (s != NULL)

275 {

276 \_dbus_verbose ("Bus activation type was set to \\%s\\\n", s);

277

278 if (strcmp (s, "system") == 0)

279 activation_bus_type = DBUS_BUS_SYSTEM;

280 else if (strcmp (s, "session") == 0)

281 activation_bus_type = DBUS_BUS_SESSION;

282 }

283 }

284 else

285 {

286 /\* Default to the session bus instead if available \*/

287 if (bus_connection_addresses\[DBUS_BUS_SESSION\] != NULL)

288 {

289 bus_connection_addresses\[DBUS_BUS_STARTER\] =

290 \_dbus_strdup (bus_connection_addresses\[DBUS_BUS_SESSION\]);

291 if (bus_connection_addresses\[DBUS_BUS_STARTER\] == NULL)

292 return FALSE;

293 }

294 }

295

296 /\* If we return FALSE we have to be sure that restarting

297 \* the above code will work right

298 \*/

299

300 if (!\_dbus_register_shutdown_func (addresses_shutdown_func,

301 NULL))

302 return FALSE;

303

304 initialized = TRUE;

305 }

306

307 return initialized;

308}

309

310static void

311bus_data_free (void \*data)

312{

313 BusData \*bd = data;

314

315 if (bd-\>is_well_known)

316 {

317 int i;

318

319 if (!\_DBUS_LOCK (bus))

320 \_dbus_assert_not_reached ("global locks should have been initialized "

321 "when we attached bus data");

322

323 /\* We may be stored in more than one slot \*/

324 /\* This should now be impossible - these slots are supposed to

325 \* be cleared on disconnect, so should not need to be cleared on

326 \* finalize

327 \*/

328 i = 0;

329 while (i \< N_BUS_TYPES)

330 {

331 if (bus_connections\[i\] == bd-\>connection)

332 bus_connections\[i\] = NULL;

333

334 ++i;

335 }

336 \_DBUS_UNLOCK (bus);

337 }

338

339 dbus_free (bd-\>unique_name);

340 dbus_free (bd);

341

342 dbus_connection_free_data_slot (&bus_data_slot);

343}

344

345static BusData\*

346ensure_bus_data (DBusConnection \*connection)

347{

348 BusData \*bd;

349

350 if (!dbus_connection_allocate_data_slot (&bus_data_slot))

351 return NULL;

352

353 bd = dbus_connection_get_data (connection, bus_data_slot);

354 if (bd == NULL)

355 {

356 bd = dbus_new0 (BusData, 1);

357 if (bd == NULL)

358 {

359 dbus_connection_free_data_slot (&bus_data_slot);

360 return NULL;

361 }

362

363 bd-\>connection = connection;

364

365 if (!dbus_connection_set_data (connection, bus_data_slot, bd,

366 bus_data_free))

367 {

368 dbus_free (bd);

369 dbus_connection_free_data_slot (&bus_data_slot);

370 return NULL;

371 }

372

373 /\* Data slot refcount now held by the BusData \*/

374 }

375 else

376 {

377 dbus_connection_free_data_slot (&bus_data_slot);

378 }

379

380 return bd;

381}

382

389void

390\_dbus_bus_notify_shared_connection_disconnected_unlocked (DBusConnection \*connection)

391{

392 int i;

393

394 if (!\_DBUS_LOCK (bus))

395 {

396 /\* If it was in bus_connections, we would have initialized global locks

397 \* when we added it. So, it can't be. \*/

398 return;

399 }

400

401 /\* We are expecting to have the connection saved in only one of these

402 \* slots, but someone could in a pathological case set system and session

403 \* bus to the same bus or something. Or set one of them to the starter

404 \* bus without setting the starter bus type in the env variable.

405 \* So we don't break the loop as soon as we find a match.

406 \*/

407 for (i = 0; i \< N_BUS_TYPES; ++i)

408 {

409 if (bus_connections\[i\] == connection)

410 {

411 bus_connections\[i\] = NULL;

412 }

413 }

414

415 \_DBUS_UNLOCK (bus);

416}

417

418static DBusConnection \*

419internal_bus_get (DBusBusType type,

420 dbus_bool_t private,

421 DBusError \*error)

422{

423 const char \*address;

424 DBusConnection \*connection;

425 BusData \*bd;

426 DBusBusType address_type;

427

428 \_dbus_return_val_if_fail (type \>= 0 && type \< N_BUS_TYPES, NULL);

429 \_dbus_return_val_if_error_is_set (error, NULL);

430

431 connection = NULL;

432

433 if (!\_DBUS_LOCK (bus))

434 {

435 \_DBUS_SET_OOM (error);

436 /\* do not "goto out", that would try to unlock \*/

437 return NULL;

438 }

439

440 if (!init_connections_unlocked ())

441 {

442 \_DBUS_SET_OOM (error);

443 goto out;

444 }

445

446 /\* We want to use the activation address even if the

447 \* activating bus is the session or system bus,

448 \* per the spec.

449 \*/

450 address_type = type;

451

452 /\* Use the real type of the activation bus for getting its

453 \* connection, but only if the real type's address is available. (If

454 \* the activating bus isn't a well-known bus then

455 \* activation_bus_type == DBUS_BUS_STARTER)

456 \*/

457 if (type == DBUS_BUS_STARTER &&

458 bus_connection_addresses\[activation_bus_type\] != NULL)

459 type = activation_bus_type;

460

461 if (!private && bus_connections\[type\] != NULL)

462 {

463 connection = bus_connections\[type\];

464 dbus_connection_ref (connection);

465 goto out;

466 }

467

468 address = bus_connection_addresses\[address_type\];

469 if (address == NULL)

470 {

471 dbus_set_error (error, DBUS_ERROR_FAILED,

472 "Unable to determine the address of the message bus (try 'man dbus-launch' and 'man dbus-daemon' for help)");

473 goto out;

474 }

475

476 if (private)

477 connection = dbus_connection_open_private (address, error);

478 else

479 connection = dbus_connection_open (address, error);

480

481 if (!connection)

482 {

483 goto out;

484 }

485

486 if (!dbus_bus_register (connection, error))

487 {

488 \_dbus_connection_close_possibly_shared (connection);

489 dbus_connection_unref (connection);

490 connection = NULL;

491 goto out;

492 }

493

494 if (!private)

495 {

496 /\* store a weak ref to the connection (dbus-connection.c is

497 \* supposed to have a strong ref that it drops on disconnect,

498 \* since this is a shared connection)

499 \*/

500 bus_connections\[type\] = connection;

501 }

502

503 /\* By default we're bound to the lifecycle of

504 \* the message bus.

505 \*/

506 dbus_connection_set_exit_on_disconnect (connection,

507 TRUE);

508

509 if (!\_DBUS_LOCK (bus_datas))

510 \_dbus_assert_not_reached ("global locks were initialized already");

511

512 bd = ensure_bus_data (connection);

513 \_dbus_assert (bd != NULL); /\* it should have been created on

514 register, so OOM not possible \*/

515 bd-\>is_well_known = TRUE;

516 \_DBUS_UNLOCK (bus_datas);

517

518out:

519 /\* Return a reference to the caller, or NULL with error set. \*/

520 if (connection == NULL)

521 \_DBUS_ASSERT_ERROR_IS_SET (error);

522

523 \_DBUS_UNLOCK (bus);

524 return connection;

525}

526

527

/\* end of implementation details docs \*/

529

560DBusConnection \*

561dbus_bus_get (DBusBusType type,

562 DBusError \*error)

563{

564 return internal_bus_get (type, FALSE, error);

565}

566

592DBusConnection \*

593dbus_bus_get_private (DBusBusType type,

594 DBusError \*error)

595{

596 return internal_bus_get (type, TRUE, error);

597}

598

648dbus_bool_t

649dbus_bus_register (DBusConnection \*connection,

650 DBusError \*error)

651{

652 DBusMessage \*message, \*reply;

653 char \*name;

654 BusData \*bd;

655 dbus_bool_t retval;

656

657 \_dbus_return_val_if_fail (connection != NULL, FALSE);

658 \_dbus_return_val_if_error_is_set (error, FALSE);

659

660 retval = FALSE;

661 message = NULL;

662 reply = NULL;

663

664 if (!\_DBUS_LOCK (bus_datas))

665 {

666 \_DBUS_SET_OOM (error);

667 /\* do not "goto out", that would try to unlock \*/

668 return FALSE;

669 }

670

671 bd = ensure_bus_data (connection);

672 if (bd == NULL)

673 {

674 \_DBUS_SET_OOM (error);

675 goto out;

676 }

677

678 if (bd-\>unique_name != NULL)

679 {

680 \_dbus_verbose ("Ignoring attempt to register the same DBusConnection %s with the message bus a second time.\n",

681 bd-\>unique_name);

682 /\* Success! \*/

683 retval = TRUE;

684 goto out;

685 }

686

687 message = dbus_message_new_method_call (DBUS_SERVICE_DBUS,

688 DBUS_PATH_DBUS,

689 DBUS_INTERFACE_DBUS,

690 "Hello");

691

692 if (!message)

693 {

694 \_DBUS_SET_OOM (error);

695 goto out;

696 }

697

698 reply = dbus_connection_send_with_reply_and_block (connection, message, -1, error);

699

700 if (reply == NULL)

701 goto out;

702 else if (dbus_set_error_from_message (error, reply))

703 goto out;

704 else if (!dbus_message_get_args (reply, error,

705 DBUS_TYPE_STRING, &name,

706 DBUS_TYPE_INVALID))

707 goto out;

708

709 bd-\>unique_name = \_dbus_strdup (name);

710 if (bd-\>unique_name == NULL)

711 {

712 \_DBUS_SET_OOM (error);

713 goto out;

714 }

715

716 retval = TRUE;

717

718 out:

719 \_DBUS_UNLOCK (bus_datas);

720

721 if (message)

722 dbus_message_unref (message);

723

724 if (reply)

725 dbus_message_unref (reply);

726

727 if (!retval)

728 \_DBUS_ASSERT_ERROR_IS_SET (error);

729

730 return retval;

731}

732

733

768dbus_bool_t

769dbus_bus_set_unique_name (DBusConnection \*connection,

770 const char \*unique_name)

771{

772 BusData \*bd;

773 dbus_bool_t success = FALSE;

774

775 \_dbus_return_val_if_fail (connection != NULL, FALSE);

776 \_dbus_return_val_if_fail (unique_name != NULL, FALSE);

777

778 if (!\_DBUS_LOCK (bus_datas))

779 {

780 /\* do not "goto out", that would try to unlock \*/

781 return FALSE;

782 }

783

784 bd = ensure_bus_data (connection);

785 if (bd == NULL)

786 goto out;

787

788 \_dbus_assert (bd-\>unique_name == NULL);

789

790 bd-\>unique_name = \_dbus_strdup (unique_name);

791 success = bd-\>unique_name != NULL;

792

793out:

794 \_DBUS_UNLOCK (bus_datas);

795

796 return success;

797}

798

817const char\*

818dbus_bus_get_unique_name (DBusConnection \*connection)

819{

820 BusData \*bd;

821 const char \*unique_name = NULL;

822

823 \_dbus_return_val_if_fail (connection != NULL, NULL);

824

825 if (!\_DBUS_LOCK (bus_datas))

826 {

827 /\* We'd have initialized locks when we gave it its unique name, if it

828 \* had one. Don't "goto out", that would try to unlock. \*/

829 return NULL;

830 }

831

832 bd = ensure_bus_data (connection);

833 if (bd == NULL)

834 goto out;

835

836 unique_name = bd-\>unique_name;

837

838out:

839 \_DBUS_UNLOCK (bus_datas);

840

841 return unique_name;

842}

843

867unsigned long

868dbus_bus_get_unix_user (DBusConnection \*connection,

869 const char \*name,

870 DBusError \*error)

871{

872 DBusMessage \*message, \*reply;

873 dbus_uint32_t uid;

874

875 \_dbus_return_val_if_fail (connection != NULL, DBUS_UID_UNSET);

876 \_dbus_return_val_if_fail (name != NULL, DBUS_UID_UNSET);

877 \_dbus_return_val_if_fail (\_dbus_check_is_valid_bus_name (name), DBUS_UID_UNSET);

878 \_dbus_return_val_if_error_is_set (error, DBUS_UID_UNSET);

879

880 message = dbus_message_new_method_call (DBUS_SERVICE_DBUS,

881 DBUS_PATH_DBUS,

882 DBUS_INTERFACE_DBUS,

883 "GetConnectionUnixUser");

884

885 if (message == NULL)

886 {

887 \_DBUS_SET_OOM (error);

888 return DBUS_UID_UNSET;

889 }

890

891 if (!dbus_message_append_args (message,

892 DBUS_TYPE_STRING, &name,

893 DBUS_TYPE_INVALID))

894 {

895 dbus_message_unref (message);

896 \_DBUS_SET_OOM (error);

897 return DBUS_UID_UNSET;

898 }

899

900 reply = dbus_connection_send_with_reply_and_block (connection, message, -1,

901 error);

902

903 dbus_message_unref (message);

904

905 if (reply == NULL)

906 {

907 \_DBUS_ASSERT_ERROR_IS_SET (error);

908 return DBUS_UID_UNSET;

909 }

910

911 if (dbus_set_error_from_message (error, reply))

912 {

913 \_DBUS_ASSERT_ERROR_IS_SET (error);

914 dbus_message_unref (reply);

915 return DBUS_UID_UNSET;

916 }

917

918 if (!dbus_message_get_args (reply, error,

919 DBUS_TYPE_UINT32, &uid,

920 DBUS_TYPE_INVALID))

921 {

922 \_DBUS_ASSERT_ERROR_IS_SET (error);

923 dbus_message_unref (reply);

924 return DBUS_UID_UNSET;

925 }

926

927 dbus_message_unref (reply);

928

929 return (unsigned long) uid;

930}

931

950char\*

951dbus_bus_get_id (DBusConnection \*connection,

952 DBusError \*error)

953{

954 DBusMessage \*message, \*reply;

955 char \*id;

956 const char \*v_STRING;

957

958 \_dbus_return_val_if_fail (connection != NULL, NULL);

959 \_dbus_return_val_if_error_is_set (error, NULL);

960

961 message = dbus_message_new_method_call (DBUS_SERVICE_DBUS,

962 DBUS_PATH_DBUS,

963 DBUS_INTERFACE_DBUS,

964 "GetId");

965

966 if (message == NULL)

967 {

968 \_DBUS_SET_OOM (error);

969 return NULL;

970 }

971

972 reply = dbus_connection_send_with_reply_and_block (connection, message, -1,

973 error);

974

975 dbus_message_unref (message);

976

977 if (reply == NULL)

978 {

979 \_DBUS_ASSERT_ERROR_IS_SET (error);

980 return NULL;

981 }

982

983 if (dbus_set_error_from_message (error, reply))

984 {

985 \_DBUS_ASSERT_ERROR_IS_SET (error);

986 dbus_message_unref (reply);

987 return NULL;

988 }

989

990 v_STRING = NULL;

991 if (!dbus_message_get_args (reply, error,

992 DBUS_TYPE_STRING, &v_STRING,

993 DBUS_TYPE_INVALID))

994 {

995 \_DBUS_ASSERT_ERROR_IS_SET (error);

996 dbus_message_unref (reply);

997 return NULL;

998 }

999

1000 id = \_dbus_strdup (v_STRING); /\* may be NULL \*/

1001

1002 dbus_message_unref (reply);

1003

1004 if (id == NULL)

1005 \_DBUS_SET_OOM (error);

1006

1007 /\* FIXME it might be nice to cache the ID locally \*/

1008

1009 return id;

1010}

1011

1114int

1115dbus_bus_request_name (DBusConnection \*connection,

1116 const char \*name,

1117 unsigned int flags,

1118 DBusError \*error)

1119{

1120 DBusMessage \*message, \*reply;

1121 dbus_uint32_t result;

1122

1123 \_dbus_return_val_if_fail (connection != NULL, 0);

1124 \_dbus_return_val_if_fail (name != NULL, 0);

1125 \_dbus_return_val_if_fail (\_dbus_check_is_valid_bus_name (name), 0);

1126 \_dbus_return_val_if_error_is_set (error, 0);

1127

1128 message = dbus_message_new_method_call (DBUS_SERVICE_DBUS,

1129 DBUS_PATH_DBUS,

1130 DBUS_INTERFACE_DBUS,

1131 "RequestName");

1132

1133 if (message == NULL)

1134 {

1135 \_DBUS_SET_OOM (error);

1136 return -1;

1137 }

1138

1139 if (!dbus_message_append_args (message,

1140 DBUS_TYPE_STRING, &name,

1141 DBUS_TYPE_UINT32, &flags,

1142 DBUS_TYPE_INVALID))

1143 {

1144 dbus_message_unref (message);

1145 \_DBUS_SET_OOM (error);

1146 return -1;

1147 }

1148

1149 reply = dbus_connection_send_with_reply_and_block (connection, message, -1,

1150 error);

1151

1152 dbus_message_unref (message);

1153

1154 if (reply == NULL)

1155 {

1156 \_DBUS_ASSERT_ERROR_IS_SET (error);

1157 return -1;

1158 }

1159

1160 if (dbus_set_error_from_message (error, reply))

1161 {

1162 \_DBUS_ASSERT_ERROR_IS_SET (error);

1163 dbus_message_unref (reply);

1164 return -1;

1165 }

1166

1167 if (!dbus_message_get_args (reply, error,

1168 DBUS_TYPE_UINT32, &result,

1169 DBUS_TYPE_INVALID))

1170 {

1171 \_DBUS_ASSERT_ERROR_IS_SET (error);

1172 dbus_message_unref (reply);

1173 return -1;

1174 }

1175

1176 dbus_message_unref (reply);

1177

1178 return result;

1179}

1180

1181

1200int

1201dbus_bus_release_name (DBusConnection \*connection,

1202 const char \*name,

1203 DBusError \*error)

1204{

1205 DBusMessage \*message, \*reply;

1206 dbus_uint32_t result;

1207

1208 \_dbus_return_val_if_fail (connection != NULL, 0);

1209 \_dbus_return_val_if_fail (name != NULL, 0);

1210 \_dbus_return_val_if_fail (\_dbus_check_is_valid_bus_name (name), 0);

1211 \_dbus_return_val_if_error_is_set (error, 0);

1212

1213 message = dbus_message_new_method_call (DBUS_SERVICE_DBUS,

1214 DBUS_PATH_DBUS,

1215 DBUS_INTERFACE_DBUS,

1216 "ReleaseName");

1217

1218 if (message == NULL)

1219 {

1220 \_DBUS_SET_OOM (error);

1221 return -1;

1222 }

1223

1224 if (!dbus_message_append_args (message,

1225 DBUS_TYPE_STRING, &name,

1226 DBUS_TYPE_INVALID))

1227 {

1228 dbus_message_unref (message);

1229 \_DBUS_SET_OOM (error);

1230 return -1;

1231 }

1232

1233 reply = dbus_connection_send_with_reply_and_block (connection, message, -1,

1234 error);

1235

1236 dbus_message_unref (message);

1237

1238 if (reply == NULL)

1239 {

1240 \_DBUS_ASSERT_ERROR_IS_SET (error);

1241 return -1;

1242 }

1243

1244 if (dbus_set_error_from_message (error, reply))

1245 {

1246 \_DBUS_ASSERT_ERROR_IS_SET (error);

1247 dbus_message_unref (reply);

1248 return -1;

1249 }

1250

1251 if (!dbus_message_get_args (reply, error,

1252 DBUS_TYPE_UINT32, &result,

1253 DBUS_TYPE_INVALID))

1254 {

1255 \_DBUS_ASSERT_ERROR_IS_SET (error);

1256 dbus_message_unref (reply);

1257 return -1;

1258 }

1259

1260 dbus_message_unref (reply);

1261

1262 return result;

1263}

1264

1282dbus_bool_t

1283dbus_bus_name_has_owner (DBusConnection \*connection,

1284 const char \*name,

1285 DBusError \*error)

1286{

1287 DBusMessage \*message, \*reply;

1288 dbus_bool_t exists;

1289

1290 \_dbus_return_val_if_fail (connection != NULL, FALSE);

1291 \_dbus_return_val_if_fail (name != NULL, FALSE);

1292 \_dbus_return_val_if_fail (\_dbus_check_is_valid_bus_name (name), FALSE);

1293 \_dbus_return_val_if_error_is_set (error, FALSE);

1294

1295 message = dbus_message_new_method_call (DBUS_SERVICE_DBUS,

1296 DBUS_PATH_DBUS,

1297 DBUS_INTERFACE_DBUS,

1298 "NameHasOwner");

1299 if (message == NULL)

1300 {

1301 \_DBUS_SET_OOM (error);

1302 return FALSE;

1303 }

1304

1305 if (!dbus_message_append_args (message,

1306 DBUS_TYPE_STRING, &name,

1307 DBUS_TYPE_INVALID))

1308 {

1309 dbus_message_unref (message);

1310 \_DBUS_SET_OOM (error);

1311 return FALSE;

1312 }

1313

1314 reply = dbus_connection_send_with_reply_and_block (connection, message, -1, error);

1315 dbus_message_unref (message);

1316

1317 if (reply == NULL)

1318 {

1319 \_DBUS_ASSERT_ERROR_IS_SET (error);

1320 return FALSE;

1321 }

1322

1323 if (!dbus_message_get_args (reply, error,

1324 DBUS_TYPE_BOOLEAN, &exists,

1325 DBUS_TYPE_INVALID))

1326 {

1327 \_DBUS_ASSERT_ERROR_IS_SET (error);

1328 dbus_message_unref (reply);

1329 return FALSE;

1330 }

1331

1332 dbus_message_unref (reply);

1333 return exists;

1334}

1335

1358dbus_bool_t

1359dbus_bus_start_service_by_name (DBusConnection \*connection,

1360 const char \*name,

1361 dbus_uint32_t flags,

1362 dbus_uint32_t \*result,

1363 DBusError \*error)

1364{

1365 DBusMessage \*msg;

1366 DBusMessage \*reply;

1367

1368 \_dbus_return_val_if_fail (connection != NULL, FALSE);

1369 \_dbus_return_val_if_fail (\_dbus_check_is_valid_bus_name (name), FALSE);

1370

1371 msg = dbus_message_new_method_call (DBUS_SERVICE_DBUS,

1372 DBUS_PATH_DBUS,

1373 DBUS_INTERFACE_DBUS,

1374 "StartServiceByName");

1375

1376 if (!dbus_message_append_args (msg, DBUS_TYPE_STRING, &name,

1377 DBUS_TYPE_UINT32, &flags, DBUS_TYPE_INVALID))

1378 {

1379 dbus_message_unref (msg);

1380 \_DBUS_SET_OOM (error);

1381 return FALSE;

1382 }

1383

1384 reply = dbus_connection_send_with_reply_and_block (connection, msg,

1385 -1, error);

1386 dbus_message_unref (msg);

1387

1388 if (reply == NULL)

1389 {

1390 \_DBUS_ASSERT_ERROR_IS_SET (error);

1391 return FALSE;

1392 }

1393

1394 if (dbus_set_error_from_message (error, reply))

1395 {

1396 \_DBUS_ASSERT_ERROR_IS_SET (error);

1397 dbus_message_unref (reply);

1398 return FALSE;

1399 }

1400

1401 if (result != NULL &&

1402 !dbus_message_get_args (reply, error, DBUS_TYPE_UINT32,

1403 result, DBUS_TYPE_INVALID))

1404 {

1405 \_DBUS_ASSERT_ERROR_IS_SET (error);

1406 dbus_message_unref (reply);

1407 return FALSE;

1408 }

1409

1410 dbus_message_unref (reply);

1411 return TRUE;

1412}

1413

1414static void

1415send_no_return_values (DBusConnection \*connection,

1416 DBusMessage \*msg,

1417 DBusError \*error)

1418{

1419 if (error)

1420 {

1421 /\* Block to check success codepath \*/

1422 DBusMessage \*reply;

1423

1424 reply = dbus_connection_send_with_reply_and_block (connection, msg,

1425 -1, error);

1426

1427 if (reply == NULL)

1428 \_DBUS_ASSERT_ERROR_IS_SET (error);

1429 else

1430 dbus_message_unref (reply);

1431 }

1432 else

1433 {

1434 /\* Silently-fail nonblocking codepath \*/

1435 dbus_message_set_no_reply (msg, TRUE);

1436 dbus_connection_send (connection, msg, NULL);

1437 }

1438}

1439

1528void

1529dbus_bus_add_match (DBusConnection \*connection,

1530 const char \*rule,

1531 DBusError \*error)

1532{

1533 DBusMessage \*msg;

1534

1535 \_dbus_return_if_fail (rule != NULL);

1536

1537 msg = dbus_message_new_method_call (DBUS_SERVICE_DBUS,

1538 DBUS_PATH_DBUS,

1539 DBUS_INTERFACE_DBUS,

1540 "AddMatch");

1541

1542 if (msg == NULL)

1543 {

1544 \_DBUS_SET_OOM (error);

1545 return;

1546 }

1547

1548 if (!dbus_message_append_args (msg, DBUS_TYPE_STRING, &rule,

1549 DBUS_TYPE_INVALID))

1550 {

1551 dbus_message_unref (msg);

1552 \_DBUS_SET_OOM (error);

1553 return;

1554 }

1555

1556 send_no_return_values (connection, msg, error);

1557

1558 dbus_message_unref (msg);

1559}

1560

1578void

1579dbus_bus_remove_match (DBusConnection \*connection,

1580 const char \*rule,

1581 DBusError \*error)

1582{

1583 DBusMessage \*msg;

1584

1585 \_dbus_return_if_fail (rule != NULL);

1586

1587 msg = dbus_message_new_method_call (DBUS_SERVICE_DBUS,

1588 DBUS_PATH_DBUS,

1589 DBUS_INTERFACE_DBUS,

1590 "RemoveMatch");

1591

1592 if (!dbus_message_append_args (msg, DBUS_TYPE_STRING, &rule,

1593 DBUS_TYPE_INVALID))

1594 {

1595 dbus_message_unref (msg);

1596 \_DBUS_SET_OOM (error);

1597 return;

1598 }

1599

1600 send_no_return_values (connection, msg, error);

1601

1602 dbus_message_unref (msg);

1603}

1604

\_dbus_bus_notify_shared_connection_disconnected_unlocked

void \_dbus_bus_notify_shared_connection_disconnected_unlocked(DBusConnection \*connection)

Internal function that checks to see if this is a shared connection owned by the bus and if it is unr...

**Definition** dbus-bus.c:390

N_BUS_TYPES

\#define N_BUS_TYPES

Number of bus types.

**Definition** dbus-bus.c:93

dbus_bus_set_unique_name

dbus_bool_t dbus_bus_set_unique_name(DBusConnection \*connection, const char \*unique_name)

Sets the unique name of the connection, as assigned by the message bus.

**Definition** dbus-bus.c:769

dbus_bus_register

dbus_bool_t dbus_bus_register(DBusConnection \*connection, DBusError \*error)

Registers a connection with the bus.

**Definition** dbus-bus.c:649

dbus_bus_get_id

char \* dbus_bus_get_id(DBusConnection \*connection, DBusError \*error)

Asks the bus to return its globally unique ID, as described in the D-Bus specification.

**Definition** dbus-bus.c:951

dbus_bus_get_unix_user

unsigned long dbus_bus_get_unix_user(DBusConnection \*connection, const char \*name, DBusError \*error)

Asks the bus to return the UID the named connection authenticated as, if any.

**Definition** dbus-bus.c:868

dbus_bus_add_match

void dbus_bus_add_match(DBusConnection \*connection, const char \*rule, DBusError \*error)

Adds a match rule to match messages going through the message bus.

**Definition** dbus-bus.c:1529

dbus_bus_name_has_owner

dbus_bool_t dbus_bus_name_has_owner(DBusConnection \*connection, const char \*name, DBusError \*error)

Asks the bus whether a certain name has an owner.

**Definition** dbus-bus.c:1283

dbus_bus_remove_match

void dbus_bus_remove_match(DBusConnection \*connection, const char \*rule, DBusError \*error)

Removes a previously-added match rule "by value" (the most recently-added identical rule gets removed...

**Definition** dbus-bus.c:1579

dbus_bus_get

DBusConnection \* dbus_bus_get(DBusBusType type, DBusError \*error)

Connects to a bus daemon and registers the client with it.

**Definition** dbus-bus.c:561

dbus_bus_start_service_by_name

dbus_bool_t dbus_bus_start_service_by_name(DBusConnection \*connection, const char \*name, dbus_uint32_t flags, dbus_uint32_t \*result, DBusError \*error)

Starts a service that will request ownership of the given name.

**Definition** dbus-bus.c:1359

dbus_bus_request_name

int dbus_bus_request_name(DBusConnection \*connection, const char \*name, unsigned int flags, DBusError \*error)

Asks the bus to assign the given name to this connection by invoking the RequestName method on the bu...

**Definition** dbus-bus.c:1115

dbus_bus_get_unique_name

const char \* dbus_bus_get_unique_name(DBusConnection \*connection)

Gets the unique name of the connection as assigned by the message bus.

**Definition** dbus-bus.c:818

dbus_bus_get_private

DBusConnection \* dbus_bus_get_private(DBusBusType type, DBusError \*error)

Connects to a bus daemon and registers the client with it as with dbus_bus_register().

**Definition** dbus-bus.c:593

dbus_bus_release_name

int dbus_bus_release_name(DBusConnection \*connection, const char \*name, DBusError \*error)

Asks the bus to unassign the given name from this connection by invoking the ReleaseName method on th...

**Definition** dbus-bus.c:1201

\_dbus_connection_close_possibly_shared

void \_dbus_connection_close_possibly_shared(DBusConnection \*connection)

Closes a shared OR private connection, while dbus_connection_close() can only be used on private conn...

**Definition** dbus-connection.c:1962

dbus_connection_set_exit_on_disconnect

void dbus_connection_set_exit_on_disconnect(DBusConnection \*connection, dbus_bool_t exit_on_disconnect)

Set whether \_exit() should be called when the connection receives a disconnect signal.

**Definition** dbus-connection.c:3160

dbus_connection_get_data

void \* dbus_connection_get_data(DBusConnection \*connection, dbus_int32_t slot)

Retrieves data previously set with dbus_connection_set_data().

**Definition** dbus-connection.c:6144

dbus_connection_open_private

DBusConnection \* dbus_connection_open_private(const char \*address, DBusError \*error)

Opens a new, dedicated connection to a remote address.

**Definition** dbus-connection.c:2678

dbus_connection_unref

void dbus_connection_unref(DBusConnection \*connection)

Decrements the reference count of a DBusConnection, and finalizes it if the count reaches zero.

**Definition** dbus-connection.c:2832

dbus_connection_allocate_data_slot

dbus_bool_t dbus_connection_allocate_data_slot(dbus_int32_t \*slot_p)

Allocates an integer ID to be used for storing application-specific data on any DBusConnection.

**Definition** dbus-connection.c:6047

dbus_connection_free_data_slot

void dbus_connection_free_data_slot(dbus_int32_t \*slot_p)

Deallocates a global ID for connection data slots.

**Definition** dbus-connection.c:6065

dbus_connection_set_data

dbus_bool_t dbus_connection_set_data(DBusConnection \*connection, dbus_int32_t slot, void \*data, DBusFreeFunction free_data_func)

Stores a pointer on a DBusConnection, along with an optional function to be used for freeing the data...

**Definition** dbus-connection.c:6095

dbus_connection_send_with_reply_and_block

DBusMessage \* dbus_connection_send_with_reply_and_block(DBusConnection \*connection, DBusMessage \*message, int timeout_milliseconds, DBusError \*error)

Sends a message and blocks a certain time period while waiting for a reply.

**Definition** dbus-connection.c:3551

dbus_connection_open

DBusConnection \* dbus_connection_open(const char \*address, DBusError \*error)

Gets a connection to a remote address.

**Definition** dbus-connection.c:2635

dbus_connection_send

dbus_bool_t dbus_connection_send(DBusConnection \*connection, DBusMessage \*message, dbus_uint32_t \*serial)

Adds a message to the outgoing message queue.

**Definition** dbus-connection.c:3317

dbus_connection_ref

DBusConnection \* dbus_connection_ref(DBusConnection \*connection)

Increments the reference count of a DBusConnection.

**Definition** dbus-connection.c:2700

DBUS_ERROR_INIT

\#define DBUS_ERROR_INIT

Expands to a suitable initializer for a DBusError on the stack.

**Definition** dbus-errors.h:64

dbus_set_error

void dbus_set_error(DBusError \*error, const char \*name, const char \*format,...)

Assigns an error name and message to a DBusError.

**Definition** dbus-errors.c:356

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

\_DBUS_UNLOCK

\#define \_DBUS_UNLOCK(name)

Unlocks a global lock.

**Definition** dbus-internals.h:438

\_DBUS_LOCK

\#define \_DBUS_LOCK(name)

Locks a global lock, initializing it first if necessary.

**Definition** dbus-internals.h:437

\_dbus_warn_check_failed

void \_dbus_warn_check_failed(const char \*format,...)

Prints a "critical" warning to stderr when an assertion fails; differs from \_dbus_warn primarily in t...

**Definition** dbus-internals.c:310

\_dbus_strdup

char \* \_dbus_strdup(const char \*str)

Duplicates a string.

**Definition** dbus-internals.c:621

\_dbus_warn

void \_dbus_warn(const char \*format,...)

Prints a warning message to stderr.

**Definition** dbus-internals.c:278

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

\_dbus_register_shutdown_func

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_register_shutdown_func(DBusShutdownFunction function, void \*data)

Register a cleanup function to be called exactly once the next time dbus_shutdown() is called.

**Definition** dbus-memory.c:819

dbus_free

void dbus_free(void \*memory)

Frees a block of memory previously allocated by dbus_malloc() or dbus_malloc0().

**Definition** dbus-memory.c:710

dbus_new0

\#define dbus_new0(type, count)

Safe macro for using dbus_malloc0().

**Definition** dbus-memory.h:60

dbus_message_set_no_reply

void dbus_message_set_no_reply(DBusMessage \*message, dbus_bool_t no_reply)

Sets a flag indicating that the message does not want a reply; if this flag is set,...

**Definition** dbus-message.c:3247

dbus_message_append_args

dbus_bool_t dbus_message_append_args(DBusMessage \*message, int first_arg_type,...)

Appends fields to a message given a variable argument list.

**Definition** dbus-message.c:1843

dbus_message_new_method_call

DBusMessage \* dbus_message_new_method_call(const char \*destination, const char \*path, const char \*iface, const char \*method)

Constructs a new message to invoke a method on a remote object.

**Definition** dbus-message.c:1378

dbus_message_unref

void dbus_message_unref(DBusMessage \*message)

Decrements the reference count of a DBusMessage, freeing the message if the count reaches 0.

**Definition** dbus-message.c:1735

dbus_set_error_from_message

dbus_bool_t dbus_set_error_from_message(DBusError \*error, DBusMessage \*message)

Sets a DBusError based on the contents of the given message.

**Definition** dbus-message.c:4059

dbus_message_get_args

dbus_bool_t dbus_message_get_args(DBusMessage \*message, DBusError \*error, int first_arg_type,...)

Gets arguments from a message given a variable argument list.

**Definition** dbus-message.c:2032

DBUS_TYPE_BOOLEAN

\#define DBUS_TYPE_BOOLEAN

Type code marking a boolean.

**Definition** dbus-protocol.h:72

DBUS_TYPE_STRING

\#define DBUS_TYPE_STRING

Type code marking a UTF-8 encoded, nul-terminated Unicode string.

**Definition** dbus-protocol.h:104

DBUS_TYPE_INVALID

\#define DBUS_TYPE_INVALID

Type code that is never equal to a legitimate type code.

**Definition** dbus-protocol.h:62

DBUS_ERROR_FAILED

\#define DBUS_ERROR_FAILED

A generic error; "something went wrong" - see the error message for more.

**Definition** dbus-protocol.h:361

DBUS_TYPE_UINT32

\#define DBUS_TYPE_UINT32

Type code marking a 32-bit unsigned integer.

**Definition** dbus-protocol.h:88

DBUS_PATH_DBUS

\#define DBUS_PATH_DBUS

The object path used to talk to the bus itself.

**Definition** dbus-shared.h:82

DBusBusType

DBusBusType

Well-known bus types.

**Definition** dbus-shared.h:59

DBUS_SERVICE_DBUS

\#define DBUS_SERVICE_DBUS

The bus name used to talk to the bus itself.

**Definition** dbus-shared.h:78

DBUS_INTERFACE_DBUS

\#define DBUS_INTERFACE_DBUS

The interface exported by the object with DBUS_SERVICE_DBUS and DBUS_PATH_DBUS.

**Definition** dbus-shared.h:90

DBUS_BUS_SESSION

@ DBUS_BUS_SESSION

The login session bus.

**Definition** dbus-shared.h:60

DBUS_BUS_STARTER

@ DBUS_BUS_STARTER

The bus that started us, if any.

**Definition** dbus-shared.h:62

DBUS_BUS_SYSTEM

@ DBUS_BUS_SYSTEM

The systemwide bus.

**Definition** dbus-shared.h:61

\_dbus_string_init

dbus_bool_t \_dbus_string_init(DBusString \*str)

Initializes a string.

**Definition** dbus-string.c:182

\_dbus_string_steal_data

dbus_bool_t \_dbus_string_steal_data(DBusString \*str, char \*\*data_return)

Like \_dbus_string_get_data(), but removes the gotten data from the original string.

**Definition** dbus-string.c:686

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

DBUS_UID_UNSET

\#define DBUS_UID_UNSET

an invalid UID used to represent an uninitialized dbus_uid_t field

**Definition** dbus-sysdeps.h:148

\_dbus_getenv

const char \* \_dbus_getenv(const char \*varname)

Wrapper for getenv().

**Definition** dbus-sysdeps.c:197

\_dbus_lookup_session_address

dbus_bool_t \_dbus_lookup_session_address(dbus_bool_t \*supported, DBusString \*address, DBusError \*error)

Determines the address of the session bus by querying a platform-specific method.

**Definition** dbus-sysdeps-unix.c:4670

BusData

Block of message-bus-related data we attach to each DBusConnection used with these convenience functi...

**Definition** dbus-bus.c:80

BusData::is_well_known

unsigned int is_well_known

Is one of the well-known connections in our global array.

**Definition** dbus-bus.c:84

BusData::connection

DBusConnection \* connection

Connection we're associated with.

**Definition** dbus-bus.c:81

BusData::unique_name

char \* unique_name

Unique name of this connection.

**Definition** dbus-bus.c:82

DBusConnection

Implementation details of DBusConnection.

**Definition** dbus-connection.c:259

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

DBusString

**Definition** dbus-string.h:47
