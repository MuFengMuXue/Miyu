dbus-userdb.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-userdb.c User database abstraction

3 \*

4 \* Copyright (C) 2003, 2004 Red Hat, Inc.

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

25\#include \<config.h\>

26\#define DBUS_USERDB_INCLUDES_PRIVATE 1

27\#include "dbus-userdb.h"

28\#include "dbus-hash.h"

29\#include "dbus-test.h"

30\#include "dbus-internals.h"

31\#include "dbus-protocol.h"

32\#include "dbus-credentials.h"

33\#include \<string.h\>

34

35/\* It isn't obvious from its name, but this file is part of the Unix

36 \* system-dependent part of libdbus. Windows has a parallel

37 \* implementation of some of it in dbus-sysdeps-win.c. \*/

38\#if defined(DBUS_WIN) \|\| !defined(DBUS_UNIX)

39\#error "This file only makes sense on Unix OSs"

40\#endif

41

47static DBusUserInfo \*

48\_dbus_user_info_ref (DBusUserInfo \*info)

49{

50 \_dbus_assert (info-\>refcount \> 0);

51 \_dbus_assert (info-\>refcount \< SIZE_MAX);

52 info-\>refcount++;

53 return info;

54}

55

63void

64\_dbus_user_info_unref (DBusUserInfo \*info)

65{

66 if (info == NULL) /\* hash table will pass NULL \*/

67 return;

68

69 \_dbus_assert (info-\>refcount \> 0);

70 \_dbus_assert (info-\>refcount \< SIZE_MAX);

71

72 if (--info-\>refcount \> 0)

73 return;

74

75 \_dbus_user_info_free (info);

76 dbus_free (info);

77}

78

86void

87\_dbus_group_info_unref (DBusGroupInfo \*info)

88{

89 if (info == NULL) /\* hash table will pass NULL \*/

90 return;

91

92 \_dbus_assert (info-\>refcount \> 0);

93 \_dbus_assert (info-\>refcount \< SIZE_MAX);

94

95 if (--info-\>refcount \> 0)

96 return;

97

98 \_dbus_group_info_free (info);

99 dbus_free (info);

100}

101

107void

108\_dbus_user_info_free (DBusUserInfo \*info)

109{

110 dbus_free (info-\>group_ids);

111 dbus_free (info-\>username);

112 dbus_free (info-\>homedir);

113}

114

120void

121\_dbus_group_info_free (DBusGroupInfo \*info)

122{

123 dbus_free (info-\>groupname);

124}

125

134dbus_bool_t

135\_dbus_is_a_number (const DBusString \*str,

136 unsigned long \*num)

137{

138 int end;

139

140 if (\_dbus_string_parse_uint (str, 0, num, &end) &&

141 end == \_dbus_string_get_length (str))

142 return TRUE;

143 else

144 return FALSE;

145}

146

159const DBusUserInfo \*

160\_dbus_user_database_lookup (DBusUserDatabase \*db,

161 dbus_uid_t uid,

162 const DBusString \*username,

163 DBusError \*error)

164{

165 DBusUserInfo \*info;

166

167 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

168 \_dbus_assert (uid != DBUS_UID_UNSET \|\| username != NULL);

169

170 /\* See if the username is really a number \*/

171 if (uid == DBUS_UID_UNSET)

172 {

173 unsigned long n;

174

175 if (\_dbus_is_a_number (username, &n))

176 uid = n;

177 }

178

179 if (uid != DBUS_UID_UNSET)

180 info = \_dbus_hash_table_lookup_uintptr (db-\>users, uid);

181 else

182 info = \_dbus_hash_table_lookup_string (db-\>users_by_name, \_dbus_string_get_const_data (username));

183

184 if (info)

185 {

186 \_dbus_verbose ("Using cache for UID "DBUS_UID_FORMAT" information\n",

187 info-\>uid);

188 return info;

189 }

190 else

191 {

192 if (uid != DBUS_UID_UNSET)

193 \_dbus_verbose ("No cache for UID "DBUS_UID_FORMAT"\n",

194 uid);

195 else

196 \_dbus_verbose ("No cache for user \\%s\\\n",

197 \_dbus_string_get_const_data (username));

198

199 info = dbus_new0 (DBusUserInfo, 1);

200 if (info == NULL)

201 {

202 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

203 return NULL;

204 }

205 info-\>refcount = 1;

206

207 if (uid != DBUS_UID_UNSET)

208 {

209 if (!\_dbus_user_info_fill_uid (info, uid, error))

210 {

211 \_DBUS_ASSERT_ERROR_IS_SET (error);

212 \_dbus_user_info_unref (info);

213 return NULL;

214 }

215 }

216 else

217 {

218 if (!\_dbus_user_info_fill (info, username, error))

219 {

220 \_DBUS_ASSERT_ERROR_IS_SET (error);

221 \_dbus_user_info_unref (info);

222 return NULL;

223 }

224 }

225

226 /\* be sure we don't use these after here \*/

227 uid = DBUS_UID_UNSET;

228 username = NULL;

229

230 /\* insert into hash \*/

231 if (\_dbus_hash_table_insert_uintptr (db-\>users, info-\>uid, info))

232 {

233 \_dbus_user_info_ref (info);

234 }

235 else

236 {

237 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

238 \_dbus_user_info_unref (info);

239 return NULL;

240 }

241

242 if (\_dbus_hash_table_insert_string (db-\>users_by_name,

243 info-\>username,

244 info))

245 {

246 \_dbus_user_info_ref (info);

247 }

248 else

249 {

250 \_dbus_hash_table_remove_uintptr (db-\>users, info-\>uid);

251 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

252 \_dbus_user_info_unref (info);

253 return NULL;

254 }

255

256 \_dbus_user_info_unref (info);

257

258 /\* Return a borrowed pointer to the DBusUserInfo owned by the

259 \* hash tables \*/

260 return info;

261 }

262}

263

264/\* Protected by \_DBUS_LOCK_system_users \*/

265static dbus_bool_t database_locked = FALSE;

266static DBusUserDatabase \*system_db = NULL;

267static DBusString process_username;

268static DBusString process_homedir;

269

270static void

271shutdown_system_db (void \*data)

272{

273 if (system_db != NULL)

274 \_dbus_user_database_unref (system_db);

275 system_db = NULL;

276 \_dbus_string_free (&process_username);

277 \_dbus_string_free (&process_homedir);

278}

279

280static dbus_bool_t

281init_system_db (void)

282{

283 \_dbus_assert (database_locked);

284

285 if (system_db == NULL)

286 {

287 DBusError error = DBUS_ERROR_INIT;

288 const DBusUserInfo \*info;

289

290 system_db = \_dbus_user_database_new ();

291 if (system_db == NULL)

292 return FALSE;

293

294 if (!\_dbus_user_database_get_uid (system_db,

295 \_dbus_getuid (),

296 &info,

297 &error))

298 {

299 \_dbus_user_database_unref (system_db);

300 system_db = NULL;

301

302 if (dbus_error_has_name (&error, DBUS_ERROR_NO_MEMORY))

303 {

304 dbus_error_free (&error);

305 return FALSE;

306 }

307 else

308 {

309 /\* This really should not happen. \*/

310 \_dbus_warn ("Could not get password database information for UID of current process: %s",

311 error.message);

312 dbus_error_free (&error);

313 return FALSE;

314 }

315 }

316

317 if (!\_dbus_string_init (&process_username))

318 {

319 \_dbus_user_database_unref (system_db);

320 system_db = NULL;

321 return FALSE;

322 }

323

324 if (!\_dbus_string_init (&process_homedir))

325 {

326 \_dbus_string_free (&process_username);

327 \_dbus_user_database_unref (system_db);

328 system_db = NULL;

329 return FALSE;

330 }

331

332 if (!\_dbus_string_append (&process_username,

333 info-\>username) \|\|

334 !\_dbus_string_append (&process_homedir,

335 info-\>homedir) \|\|

336 !\_dbus_register_shutdown_func (shutdown_system_db, NULL))

337 {

338 \_dbus_string_free (&process_username);

339 \_dbus_string_free (&process_homedir);

340 \_dbus_user_database_unref (system_db);

341 system_db = NULL;

342 return FALSE;

343 }

344 }

345

346 return TRUE;

347}

348

352dbus_bool_t

353\_dbus_user_database_lock_system (void)

354{

355 if (\_DBUS_LOCK (system_users))

356 {

357 database_locked = TRUE;

358 return TRUE;

359 }

360 else

361 {

362 return FALSE;

363 }

364}

365

369void

370\_dbus_user_database_unlock_system (void)

371{

372 database_locked = FALSE;

373 \_DBUS_UNLOCK (system_users);

374}

375

382DBusUserDatabase\*

383\_dbus_user_database_get_system (void)

384{

385 \_dbus_assert (database_locked);

386

387 init_system_db ();

388

389 return system_db;

390}

391

395void

396\_dbus_user_database_flush_system (void)

397{

398 if (!\_dbus_user_database_lock_system ())

399 {

400 /\* nothing to flush \*/

401 return;

402 }

403

404 if (system_db != NULL)

405 \_dbus_user_database_flush (system_db);

406

407 \_dbus_user_database_unlock_system ();

408}

409

417dbus_bool_t

418\_dbus_username_from_current_process (const DBusString \*\*username)

419{

420 if (!\_dbus_user_database_lock_system ())

421 return FALSE;

422

423 if (!init_system_db ())

424 {

425 \_dbus_user_database_unlock_system ();

426 return FALSE;

427 }

428 \*username = &process_username;

429 \_dbus_user_database_unlock_system ();

430

431 return TRUE;

432}

433

441dbus_bool_t

442\_dbus_homedir_from_current_process (const DBusString \*\*homedir)

443{

444 if (!\_dbus_user_database_lock_system ())

445 return FALSE;

446

447 if (!init_system_db ())

448 {

449 \_dbus_user_database_unlock_system ();

450 return FALSE;

451 }

452 \*homedir = &process_homedir;

453 \_dbus_user_database_unlock_system ();

454

455 return TRUE;

456}

457

465dbus_bool_t

466\_dbus_homedir_from_uid (dbus_uid_t uid,

467 DBusString \*homedir)

468{

469 DBusUserDatabase \*db;

470 const DBusUserInfo \*info;

471

472 if (uid == \_dbus_getuid () && uid == \_dbus_geteuid ())

473 {

474 const char \*from_environment;

475

476 from_environment = \_dbus_getenv ("HOME");

477

478 if (from_environment != NULL)

479 return \_dbus_string_append (homedir, from_environment);

480 }

481

482 /\* FIXME: this can't distinguish ENOMEM from other errors \*/

483 if (!\_dbus_user_database_lock_system ())

484 return FALSE;

485

486 db = \_dbus_user_database_get_system ();

487 if (db == NULL)

488 {

489 \_dbus_user_database_unlock_system ();

490 return FALSE;

491 }

492

493 if (!\_dbus_user_database_get_uid (db, uid,

494 &info, NULL))

495 {

496 \_dbus_user_database_unlock_system ();

497 return FALSE;

498 }

499

500 if (!\_dbus_string_append (homedir, info-\>homedir))

501 {

502 \_dbus_user_database_unlock_system ();

503 return FALSE;

504 }

505

506 \_dbus_user_database_unlock_system ();

507 return TRUE;

508}

509

524dbus_bool_t

525\_dbus_credentials_add_from_user (DBusCredentials \*credentials,

526 const DBusString \*username,

527 DBusCredentialsAddFlags flags,

528 DBusError \*error)

529{

530 DBusUserDatabase \*db;

531 const DBusUserInfo \*info;

532 unsigned long uid = DBUS_UID_UNSET;

533

534 /\* Fast-path for the common case: if the "username" is all-numeric,

535 \* then it's a Unix uid. This is true regardless of whether that uid

536 \* exists in NSS or /etc/passwd or equivalent. \*/

537 if (\_dbus_is_a_number (username, &uid))

538 {

539 \_DBUS_STATIC_ASSERT (sizeof (uid) == sizeof (dbus_uid_t));

540

541 if (\_dbus_credentials_add_unix_uid (credentials, uid))

542 {

543 return TRUE;

544 }

545 else

546 {

547 \_DBUS_SET_OOM (error);

548 return FALSE;

549 }

550 }

551

552 /\* If we aren't allowed to look in NSS or /etc/passwd, fail now. \*/

553 if (!(flags & DBUS_CREDENTIALS_ADD_FLAGS_USER_DATABASE))

554 {

555 dbus_set_error (error, DBUS_ERROR_INVALID_ARGS,

556 "Expected a numeric Unix uid");

557 return FALSE;

558 }

559

560 if (!\_dbus_user_database_lock_system ())

561 {

562 \_DBUS_SET_OOM (error);

563 return FALSE;

564 }

565

566 db = \_dbus_user_database_get_system ();

567 if (db == NULL)

568 {

569 \_dbus_user_database_unlock_system ();

570 \_DBUS_SET_OOM (error);

571 return FALSE;

572 }

573

574 if (!\_dbus_user_database_get_username (db, username,

575 &info, error))

576 {

577 \_dbus_user_database_unlock_system ();

578 return FALSE;

579 }

580

581 if (!\_dbus_credentials_add_unix_uid(credentials, info-\>uid))

582 {

583 \_dbus_user_database_unlock_system ();

584 \_DBUS_SET_OOM (error);

585 return FALSE;

586 }

587

588 \_dbus_user_database_unlock_system ();

589 return TRUE;

590}

591

597DBusUserDatabase\*

598\_dbus_user_database_new (void)

599{

600 DBusUserDatabase \*db;

601

602 db = dbus_new0 (DBusUserDatabase, 1);

603 if (db == NULL)

604 return NULL;

605

606 db-\>refcount = 1;

607

608 db-\>users = \_dbus_hash_table_new (DBUS_HASH_UINTPTR,

609 NULL, (DBusFreeFunction) \_dbus_user_info_unref);

610

611 if (db-\>users == NULL)

612 goto failed;

613

614 db-\>groups = \_dbus_hash_table_new (DBUS_HASH_UINTPTR,

615 NULL, (DBusFreeFunction) \_dbus_group_info_unref);

616

617 if (db-\>groups == NULL)

618 goto failed;

619

620 db-\>users_by_name = \_dbus_hash_table_new (DBUS_HASH_STRING,

621 NULL, (DBusFreeFunction) \_dbus_user_info_unref);

622 if (db-\>users_by_name == NULL)

623 goto failed;

624

625 db-\>groups_by_name = \_dbus_hash_table_new (DBUS_HASH_STRING,

626 NULL, (DBusFreeFunction) \_dbus_group_info_unref);

627 if (db-\>groups_by_name == NULL)

628 goto failed;

629

630 return db;

631

632 failed:

633 \_dbus_user_database_unref (db);

634 return NULL;

635}

636

640void

641\_dbus_user_database_flush (DBusUserDatabase \*db)

642{

643 \_dbus_hash_table_remove_all(db-\>users_by_name);

644 \_dbus_hash_table_remove_all(db-\>groups_by_name);

645 \_dbus_hash_table_remove_all(db-\>users);

646 \_dbus_hash_table_remove_all(db-\>groups);

647}

648

649\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

655DBusUserDatabase \*

656\_dbus_user_database_ref (DBusUserDatabase \*db)

657{

658 \_dbus_assert (db-\>refcount \> 0);

659

660 db-\>refcount += 1;

661

662 return db;

663}

664\#endif /\* DBUS_ENABLE_EMBEDDED_TESTS \*/

665

670void

671\_dbus_user_database_unref (DBusUserDatabase \*db)

672{

673 \_dbus_assert (db-\>refcount \> 0);

674

675 db-\>refcount -= 1;

676 if (db-\>refcount == 0)

677 {

678 if (db-\>users)

679 \_dbus_hash_table_unref (db-\>users);

680

681 if (db-\>groups)

682 \_dbus_hash_table_unref (db-\>groups);

683

684 if (db-\>users_by_name)

685 \_dbus_hash_table_unref (db-\>users_by_name);

686

687 if (db-\>groups_by_name)

688 \_dbus_hash_table_unref (db-\>groups_by_name);

689

690 dbus_free (db);

691 }

692}

693

704dbus_bool_t

705\_dbus_user_database_get_uid (DBusUserDatabase \*db,

706 dbus_uid_t uid,

707 const DBusUserInfo \*\*info,

708 DBusError \*error)

709{

710 \*info = \_dbus_user_database_lookup (db, uid, NULL, error);

711 return \*info != NULL;

712}

713

723dbus_bool_t

724\_dbus_user_database_get_username (DBusUserDatabase \*db,

725 const DBusString \*username,

726 const DBusUserInfo \*\*info,

727 DBusError \*error)

728{

729 \*info = \_dbus_user_database_lookup (db, DBUS_UID_UNSET, username, error);

730 return \*info != NULL;

731}

732

735/\* Tests in dbus-userdb-util.c \*/

\_dbus_credentials_add_unix_uid

dbus_bool_t \_dbus_credentials_add_unix_uid(DBusCredentials \*credentials, dbus_uid_t uid)

Add a UNIX user ID to the credentials.

**Definition** dbus-credentials.c:220

DBUS_ERROR_INIT

\#define DBUS_ERROR_INIT

Expands to a suitable initializer for a DBusError on the stack.

**Definition** dbus-errors.h:64

dbus_error_has_name

dbus_bool_t dbus_error_has_name(const DBusError \*error, const char \*name)

Checks whether the error is set and has the given name.

**Definition** dbus-errors.c:304

dbus_set_error

void dbus_set_error(DBusError \*error, const char \*name, const char \*format,...)

Assigns an error name and message to a DBusError.

**Definition** dbus-errors.c:356

dbus_error_free

void dbus_error_free(DBusError \*error)

Frees an error that's been set (or just initialized), then reinitializes the error as in dbus_error_i...

**Definition** dbus-errors.c:213

\_dbus_hash_table_remove_uintptr

dbus_bool_t \_dbus_hash_table_remove_uintptr(DBusHashTable \*table, uintptr_t key)

Removes the hash entry for the given key.

**Definition** dbus-hash.c:1243

\_dbus_hash_table_insert_string

dbus_bool_t \_dbus_hash_table_insert_string(DBusHashTable \*table, char \*key, void \*value)

Creates a hash entry with the given key and value.

**Definition** dbus-hash.c:1278

\_dbus_hash_table_lookup_uintptr

void \* \_dbus_hash_table_lookup_uintptr(DBusHashTable \*table, uintptr_t key)

Looks up the value for a given integer in a hash table of type DBUS_HASH_UINTPTR.

**Definition** dbus-hash.c:1163

\_dbus_hash_table_unref

void \_dbus_hash_table_unref(DBusHashTable \*table)

Decrements the reference count for a hash table, freeing the hash table if the count reaches zero.

**Definition** dbus-hash.c:368

\_dbus_hash_table_new

DBusHashTable \* \_dbus_hash_table_new(DBusHashType type, DBusFreeFunction key_free_function, DBusFreeFunction value_free_function)

Constructs a new hash table.

**Definition** dbus-hash.c:292

\_dbus_hash_table_lookup_string

void \* \_dbus_hash_table_lookup_string(DBusHashTable \*table, const char \*key)

Looks up the value for a given string in a hash table of type DBUS_HASH_STRING.

**Definition** dbus-hash.c:1113

\_dbus_hash_table_remove_all

void \_dbus_hash_table_remove_all(DBusHashTable \*table)

Removed all entries from a hash table.

**Definition** dbus-hash.c:425

\_dbus_hash_table_insert_uintptr

dbus_bool_t \_dbus_hash_table_insert_uintptr(DBusHashTable \*table, uintptr_t key, void \*value)

Creates a hash entry with the given key and value.

**Definition** dbus-hash.c:1353

DBUS_HASH_UINTPTR

@ DBUS_HASH_UINTPTR

Hash keys are integer capable to hold a pointer.

**Definition** dbus-hash.h:71

DBUS_HASH_STRING

@ DBUS_HASH_STRING

Hash keys are strings.

**Definition** dbus-hash.h:69

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_dbus_user_database_lock_system

dbus_bool_t \_dbus_user_database_lock_system(void)

Locks global system user database.

**Definition** dbus-userdb.c:353

\_dbus_homedir_from_current_process

dbus_bool_t \_dbus_homedir_from_current_process(const DBusString \*\*homedir)

Gets homedir of user owning current process.

**Definition** dbus-userdb.c:442

\_DBUS_UNLOCK

\#define \_DBUS_UNLOCK(name)

Unlocks a global lock.

**Definition** dbus-internals.h:438

\_dbus_user_database_new

DBusUserDatabase \* \_dbus_user_database_new(void)

Creates a new user database object used to look up and cache user information.

**Definition** dbus-userdb.c:598

\_DBUS_LOCK

\#define \_DBUS_LOCK(name)

Locks a global lock, initializing it first if necessary.

**Definition** dbus-internals.h:437

\_dbus_user_database_unlock_system

void \_dbus_user_database_unlock_system(void)

Unlocks global system user database.

**Definition** dbus-userdb.c:370

\_dbus_user_database_unref

void \_dbus_user_database_unref(DBusUserDatabase \*db)

Decrements refcount of user database.

**Definition** dbus-userdb.c:671

\_dbus_credentials_add_from_user

dbus_bool_t \_dbus_credentials_add_from_user(DBusCredentials \*credentials, const DBusString \*username, DBusCredentialsAddFlags flags, DBusError \*error)

Adds the credentials corresponding to the given username.

**Definition** dbus-userdb.c:525

\_dbus_user_database_get_uid

dbus_bool_t \_dbus_user_database_get_uid(DBusUserDatabase \*db, dbus_uid_t uid, const DBusUserInfo \*\*info, DBusError \*error)

Gets the user information for the given UID, returned user info should not be freed.

**Definition** dbus-userdb.c:705

\_dbus_user_database_flush_system

void \_dbus_user_database_flush_system(void)

Flushes the system global user database;.

**Definition** dbus-userdb.c:396

\_dbus_group_info_unref

void \_dbus_group_info_unref(DBusGroupInfo \*info)

Decrements the reference count.

**Definition** dbus-userdb.c:87

\_dbus_user_database_lookup

const DBusUserInfo \* \_dbus_user_database_lookup(DBusUserDatabase \*db, dbus_uid_t uid, const DBusString \*username, DBusError \*error)

Looks up a uid or username in the user database.

**Definition** dbus-userdb.c:160

\_dbus_user_info_unref

void \_dbus_user_info_unref(DBusUserInfo \*info)

Decrements the reference count.

**Definition** dbus-userdb.c:64

\_dbus_username_from_current_process

dbus_bool_t \_dbus_username_from_current_process(const DBusString \*\*username)

Gets username of user owning current process.

**Definition** dbus-userdb.c:418

\_dbus_user_info_free

void \_dbus_user_info_free(DBusUserInfo \*info)

Frees the members of info (but not info itself)

**Definition** dbus-userdb.c:108

\_dbus_user_database_flush

void \_dbus_user_database_flush(DBusUserDatabase \*db)

Flush all information out of the user database.

**Definition** dbus-userdb.c:641

\_dbus_homedir_from_uid

dbus_bool_t \_dbus_homedir_from_uid(dbus_uid_t uid, DBusString \*homedir)

Gets the home directory for the given user.

**Definition** dbus-userdb.c:466

\_dbus_warn

void \_dbus_warn(const char \*format,...)

Prints a warning message to stderr.

**Definition** dbus-internals.c:278

\_dbus_group_info_free

void \_dbus_group_info_free(DBusGroupInfo \*info)

Frees the members of info (but not info itself).

**Definition** dbus-userdb.c:121

\_dbus_user_database_get_username

dbus_bool_t \_dbus_user_database_get_username(DBusUserDatabase \*db, const DBusString \*username, const DBusUserInfo \*\*info, DBusError \*error)

Gets the user information for the given username.

**Definition** dbus-userdb.c:724

\_dbus_is_a_number

dbus_bool_t \_dbus_is_a_number(const DBusString \*str, unsigned long \*num)

Checks if a given string is actually a number and converts it if it is.

**Definition** dbus-userdb.c:135

\_dbus_user_database_get_system

DBusUserDatabase \* \_dbus_user_database_get_system(void)

Gets the system global user database; must be called with lock held (\_dbus_user_database_lock_system(...

**Definition** dbus-userdb.c:383

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

DBusFreeFunction

void(\* DBusFreeFunction)(void \*memory)

The type of a function which frees a block of memory.

**Definition** dbus-memory.h:65

dbus_free

void dbus_free(void \*memory)

Frees a block of memory previously allocated by dbus_malloc() or dbus_malloc0().

**Definition** dbus-memory.c:710

dbus_new0

\#define dbus_new0(type, count)

Safe macro for using dbus_malloc0().

**Definition** dbus-memory.h:60

DBUS_ERROR_NO_MEMORY

\#define DBUS_ERROR_NO_MEMORY

There was not enough memory to complete an operation.

**Definition** dbus-protocol.h:363

DBUS_ERROR_INVALID_ARGS

\#define DBUS_ERROR_INVALID_ARGS

Invalid arguments passed to a method call.

**Definition** dbus-protocol.h:397

\_dbus_string_append

dbus_bool_t \_dbus_string_append(DBusString \*str, const char \*buffer)

Appends a nul-terminated C-style string to a DBusString.

**Definition** dbus-string.c:980

\_dbus_string_init

dbus_bool_t \_dbus_string_init(DBusString \*str)

Initializes a string.

**Definition** dbus-string.c:182

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_string_parse_uint

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_parse_uint(const DBusString \*str, int start, unsigned long \*value_return, int \*end_return)

Parses an unsigned integer contained in a DBusString.

**Definition** dbus-sysdeps.c:410

\_dbus_string_get_length

int \_dbus_string_get_length(const DBusString \*str)

Gets the length of a string (not including nul termination).

**Definition** dbus-string.c:784

\_dbus_string_get_const_data

const char \* \_dbus_string_get_const_data(const DBusString \*str)

Gets the raw character buffer from a const string.

**Definition** dbus-string.c:513

\_dbus_user_info_fill

dbus_bool_t \_dbus_user_info_fill(DBusUserInfo \*info, const DBusString \*username, DBusError \*error)

Gets user info for the given username.

**Definition** dbus-sysdeps-unix.c:2966

\_dbus_geteuid

dbus_uid_t \_dbus_geteuid(void)

Gets our effective UID.

**Definition** dbus-sysdeps-unix.c:3145

\_dbus_user_info_fill_uid

dbus_bool_t \_dbus_user_info_fill_uid(DBusUserInfo \*info, dbus_uid_t uid, DBusError \*error)

Gets user info for the given user ID.

**Definition** dbus-sysdeps-unix.c:2983

dbus_uid_t

unsigned long dbus_uid_t

A user ID.

**Definition** dbus-sysdeps.h:141

DBUS_UID_UNSET

\#define DBUS_UID_UNSET

an invalid UID used to represent an uninitialized dbus_uid_t field

**Definition** dbus-sysdeps.h:148

\_dbus_getenv

const char \* \_dbus_getenv(const char \*varname)

Wrapper for getenv().

**Definition** dbus-sysdeps.c:197

\_dbus_getuid

dbus_uid_t \_dbus_getuid(void)

Gets our UID.

**Definition** dbus-sysdeps-unix.c:3136

DBUS_UID_FORMAT

\#define DBUS_UID_FORMAT

an appropriate printf format for dbus_uid_t

**Definition** dbus-sysdeps.h:155

DBusCredentials

**Definition** dbus-credentials.c:60

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusError::message

const char \* message

public error message field

**Definition** dbus-errors.h:53

DBusGroupInfo

Information about a UNIX group.

**Definition** dbus-sysdeps-unix.h:107

DBusGroupInfo::groupname

char \* groupname

Group name.

**Definition** dbus-sysdeps-unix.h:110

DBusGroupInfo::refcount

size_t refcount

Reference count.

**Definition** dbus-sysdeps-unix.h:108

DBusString

**Definition** dbus-string.h:47

DBusUserInfo

Information about a UNIX user.

**Definition** dbus-sysdeps-unix.h:93

DBusUserInfo::uid

dbus_uid_t uid

UID.

**Definition** dbus-sysdeps-unix.h:95

DBusUserInfo::homedir

char \* homedir

Home directory.

**Definition** dbus-sysdeps-unix.h:100

DBusUserInfo::group_ids

dbus_gid_t \* group_ids

Groups IDs, including above primary group.

**Definition** dbus-sysdeps-unix.h:97

DBusUserInfo::refcount

size_t refcount

Reference count.

**Definition** dbus-sysdeps-unix.h:94

DBusUserInfo::username

char \* username

Username.

**Definition** dbus-sysdeps-unix.h:99
