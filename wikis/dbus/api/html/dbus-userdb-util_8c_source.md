dbus-userdb-util.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-userdb-util.c Would be in dbus-userdb.c, but not used in libdbus

3 \*

4 \* Copyright (C) 2003, 2004, 2005 Red Hat, Inc.

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

26\#include \<unistd.h\>

27\#define DBUS_USERDB_INCLUDES_PRIVATE 1

28\#include "dbus-userdb.h"

29\#include "dbus-test.h"

30\#include "dbus-internals.h"

31\#include "dbus-protocol.h"

32\#include \<dbus/dbus-test-tap.h\>

33\#include \<string.h\>

34

35/\* It isn't obvious from its name, but this file is part of the Unix

36 \* system-dependent part of libdbus. \*/

37\#if defined(DBUS_WIN) \|\| !defined(DBUS_UNIX)

38\#error "This file only makes sense on Unix OSs"

39\#endif

40

41\#ifdef HAVE_SYSTEMD

42\#include \<systemd/sd-login.h\>

43\#endif

44

50static DBusGroupInfo \*

51\_dbus_group_info_ref (DBusGroupInfo \*info)

52{

53 \_dbus_assert (info-\>refcount \> 0);

54 \_dbus_assert (info-\>refcount \< SIZE_MAX);

55 info-\>refcount++;

56 return info;

57}

58

66dbus_bool_t

67\_dbus_is_console_user (dbus_uid_t uid,

68 DBusError \*error)

69{

70\#ifdef HAVE_SYSTEMD

71 /\* check if we have logind \*/

72 if (access ("/run/systemd/seats/", F_OK) \>= 0)

73 {

74 int r;

75

76 /\* Check whether this user is logged in on at least one physical

77 seat \*/

78 r = sd_uid_get_seats (uid, 0, NULL);

79 if (r \< 0)

80 {

81 dbus_set_error (error, \_dbus_error_from_errno (-r),

82 "Failed to determine seats of user \\" DBUS_UID_FORMAT "\\: %s",

83 uid,

84 \_dbus_strerror (-r));

85 return FALSE;

86 }

87

88 return (r \> 0);

89 }

90\#endif

91

92\#ifdef HAVE_CONSOLE_OWNER_FILE

93

94 DBusString f;

95 DBusStat st;

96

97 if (!\_dbus_string_init (&f))

98 {

99 \_DBUS_SET_OOM (error);

100 return FALSE;

101 }

102

103 if (!\_dbus_string_append(&f, DBUS_CONSOLE_OWNER_FILE))

104 {

105 \_dbus_string_free(&f);

106 \_DBUS_SET_OOM (error);

107 return FALSE;

108 }

109

110 if (\_dbus_stat(&f, &st, NULL) && (st.uid == uid))

111 {

112 \_dbus_string_free(&f);

113 return TRUE;

114 }

115

116 \_dbus_string_free(&f);

117

118\#endif /\* HAVE_CONSOLE_OWNER_FILE \*/

119

120 return FALSE;

121}

122

130dbus_bool_t

131\_dbus_get_user_id (const DBusString \*username,

132 dbus_uid_t \*uid)

133{

134 return \_dbus_get_user_id_and_primary_group (username, uid, NULL);

135}

136

144dbus_bool_t

145\_dbus_get_group_id (const DBusString \*groupname,

146 dbus_gid_t \*gid)

147{

148 DBusUserDatabase \*db;

149 const DBusGroupInfo \*info;

150

151 /\* FIXME: this can't distinguish ENOMEM from other errors \*/

152 if (!\_dbus_user_database_lock_system ())

153 return FALSE;

154

155 db = \_dbus_user_database_get_system ();

156 if (db == NULL)

157 {

158 \_dbus_user_database_unlock_system ();

159 return FALSE;

160 }

161

162 info = \_dbus_user_database_lookup_group (db, DBUS_GID_UNSET, groupname,

163 NULL);

164

165 if (info == NULL)

166 {

167 \_dbus_user_database_unlock_system ();

168 return FALSE;

169 }

170

171 \*gid = info-\>gid;

172

173 \_dbus_user_database_unlock_system ();

174 return TRUE;

175}

176

185dbus_bool_t

186\_dbus_get_user_id_and_primary_group (const DBusString \*username,

187 dbus_uid_t \*uid_p,

188 dbus_gid_t \*gid_p)

189{

190 DBusUserDatabase \*db;

191 const DBusUserInfo \*info;

192

193 /\* FIXME: this can't distinguish ENOMEM from other errors \*/

194 if (!\_dbus_user_database_lock_system ())

195 return FALSE;

196

197 db = \_dbus_user_database_get_system ();

198 if (db == NULL)

199 {

200 \_dbus_user_database_unlock_system ();

201 return FALSE;

202 }

203

204 if (!\_dbus_user_database_get_username (db, username,

205 &info, NULL))

206 {

207 \_dbus_user_database_unlock_system ();

208 return FALSE;

209 }

210

211 if (uid_p)

212 \*uid_p = info-\>uid;

213 if (gid_p)

214 \*gid_p = info-\>primary_gid;

215

216 \_dbus_user_database_unlock_system ();

217 return TRUE;

218}

219

232const DBusGroupInfo \*

233\_dbus_user_database_lookup_group (DBusUserDatabase \*db,

234 dbus_gid_t gid,

235 const DBusString \*groupname,

236 DBusError \*error)

237{

238 DBusGroupInfo \*info;

239

240 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

241

242 /\* See if the group is really a number \*/

243 if (gid == DBUS_UID_UNSET)

244 {

245 unsigned long n;

246

247 if (\_dbus_is_a_number (groupname, &n))

248 gid = n;

249 }

250

251 if (gid != DBUS_GID_UNSET)

252 info = \_dbus_hash_table_lookup_uintptr (db-\>groups, gid);

253 else

254 info = \_dbus_hash_table_lookup_string (db-\>groups_by_name,

255 \_dbus_string_get_const_data (groupname));

256 if (info)

257 {

258 \_dbus_verbose ("Using cache for GID "DBUS_GID_FORMAT" information\n",

259 info-\>gid);

260 return info;

261 }

262 else

263 {

264 if (gid != DBUS_GID_UNSET)

265 \_dbus_verbose ("No cache for GID "DBUS_GID_FORMAT"\n",

266 gid);

267 else

268 \_dbus_verbose ("No cache for groupname \\%s\\\n",

269 \_dbus_string_get_const_data (groupname));

270

271 info = dbus_new0 (DBusGroupInfo, 1);

272 if (info == NULL)

273 {

274 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

275 return NULL;

276 }

277 info-\>refcount = 1;

278

279 if (gid != DBUS_GID_UNSET)

280 {

281 if (!\_dbus_group_info_fill_gid (info, gid, error))

282 {

283 \_DBUS_ASSERT_ERROR_IS_SET (error);

284 \_dbus_group_info_unref (info);

285 return NULL;

286 }

287 }

288 else

289 {

290 if (!\_dbus_group_info_fill (info, groupname, error))

291 {

292 \_DBUS_ASSERT_ERROR_IS_SET (error);

293 \_dbus_group_info_unref (info);

294 return NULL;

295 }

296 }

297

298 /\* don't use these past here \*/

299 gid = DBUS_GID_UNSET;

300 groupname = NULL;

301

302 if (\_dbus_hash_table_insert_uintptr (db-\>groups, info-\>gid, info))

303 {

304 \_dbus_group_info_ref (info);

305 }

306 else

307 {

308 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

309 \_dbus_group_info_unref (info);

310 return NULL;

311 }

312

313

314 if (\_dbus_hash_table_insert_string (db-\>groups_by_name,

315 info-\>groupname,

316 info))

317 {

318 \_dbus_group_info_ref (info);

319 }

320 else

321 {

322 \_dbus_hash_table_remove_uintptr (db-\>groups, info-\>gid);

323 \_dbus_group_info_unref (info);

324 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

325 return NULL;

326 }

327

328 /\* Release the original reference \*/

329 \_dbus_group_info_unref (info);

330

331 /\* Return a borrowed reference to the DBusGroupInfo owned by the

332 \* two hash tables \*/

333 return info;

334 }

335}

336

348dbus_bool_t

349\_dbus_groups_from_uid (dbus_uid_t uid,

350 dbus_gid_t \*\*group_ids,

351 int \*n_group_ids,

352 DBusError \*error)

353{

354 DBusUserDatabase \*db;

355 const DBusUserInfo \*info;

356 dbus_bool_t ret = FALSE;

357

358 \*group_ids = NULL;

359 \*n_group_ids = 0;

360

361 if (!\_dbus_user_database_lock_system ())

362 {

363 \_DBUS_SET_OOM (error);

364 return FALSE;

365 }

366

367 db = \_dbus_user_database_get_system ();

368 if (db == NULL)

369 {

370 \_DBUS_SET_OOM (error);

371 goto out;

372 }

373

374 if (!\_dbus_user_database_get_uid (db, uid, &info, error))

375 goto out;

376

377 \_dbus_assert (info-\>uid == uid);

378

379 if (info-\>n_group_ids \> 0)

380 {

381 \*group_ids = dbus_new (dbus_gid_t, info-\>n_group_ids);

382 if (\*group_ids == NULL)

383 {

384 \_DBUS_SET_OOM (error);

385 goto out;

386 }

387

388 \*n_group_ids = info-\>n_group_ids;

389

390 memcpy (\*group_ids, info-\>group_ids, info-\>n_group_ids \* sizeof (dbus_gid_t));

391 }

392

393 ret = TRUE;

394out:

395 \_DBUS_ASSERT_ERROR_XOR_BOOL (error, ret);

396 \_dbus_user_database_unlock_system ();

397 return ret;

398}

dbus_set_error

void dbus_set_error(DBusError \*error, const char \*name, const char \*format,...)

Assigns an error name and message to a DBusError.

**Definition** dbus-errors.c:356

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

\_dbus_hash_table_lookup_string

void \* \_dbus_hash_table_lookup_string(DBusHashTable \*table, const char \*key)

Looks up the value for a given string in a hash table of type DBUS_HASH_STRING.

**Definition** dbus-hash.c:1113

\_dbus_hash_table_insert_uintptr

dbus_bool_t \_dbus_hash_table_insert_uintptr(DBusHashTable \*table, uintptr_t key, void \*value)

Creates a hash entry with the given key and value.

**Definition** dbus-hash.c:1353

\_dbus_stat

dbus_bool_t \_dbus_stat(const DBusString \*filename, DBusStat \*statbuf, DBusError \*error)

stat() wrapper.

**Definition** dbus-sysdeps-util-unix.c:593

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_dbus_user_database_lock_system

dbus_bool_t \_dbus_user_database_lock_system(void)

Locks global system user database.

**Definition** dbus-userdb.c:353

\_dbus_error_from_errno

const char \* \_dbus_error_from_errno(int error_number)

Converts a UNIX errno, or Windows errno or WinSock error value into a DBusError name.

**Definition** dbus-sysdeps.c:565

\_dbus_user_database_unlock_system

void \_dbus_user_database_unlock_system(void)

Unlocks global system user database.

**Definition** dbus-userdb.c:370

\_dbus_user_database_get_uid

dbus_bool_t \_dbus_user_database_get_uid(DBusUserDatabase \*db, dbus_uid_t uid, const DBusUserInfo \*\*info, DBusError \*error)

Gets the user information for the given UID, returned user info should not be freed.

**Definition** dbus-userdb.c:705

\_dbus_get_group_id

dbus_bool_t \_dbus_get_group_id(const DBusString \*groupname, dbus_gid_t \*gid)

Gets group ID given groupname.

**Definition** dbus-userdb-util.c:145

\_dbus_group_info_unref

void \_dbus_group_info_unref(DBusGroupInfo \*info)

Decrements the reference count.

**Definition** dbus-userdb.c:87

\_dbus_is_console_user

dbus_bool_t \_dbus_is_console_user(dbus_uid_t uid, DBusError \*error)

Checks to see if the UID sent in is the console user.

**Definition** dbus-userdb-util.c:67

\_dbus_user_database_lookup_group

const DBusGroupInfo \* \_dbus_user_database_lookup_group(DBusUserDatabase \*db, dbus_gid_t gid, const DBusString \*groupname, DBusError \*error)

Looks up a gid or group name in the user database.

**Definition** dbus-userdb-util.c:233

\_dbus_groups_from_uid

dbus_bool_t \_dbus_groups_from_uid(dbus_uid_t uid, dbus_gid_t \*\*group_ids, int \*n_group_ids, DBusError \*error)

Gets all groups corresponding to the given UID.

**Definition** dbus-userdb-util.c:349

\_dbus_get_user_id_and_primary_group

dbus_bool_t \_dbus_get_user_id_and_primary_group(const DBusString \*username, dbus_uid_t \*uid_p, dbus_gid_t \*gid_p)

Gets user ID and primary group given username.

**Definition** dbus-userdb-util.c:186

\_dbus_user_database_get_username

dbus_bool_t \_dbus_user_database_get_username(DBusUserDatabase \*db, const DBusString \*username, const DBusUserInfo \*\*info, DBusError \*error)

Gets the user information for the given username.

**Definition** dbus-userdb.c:724

\_dbus_is_a_number

dbus_bool_t \_dbus_is_a_number(const DBusString \*str, unsigned long \*num)

Checks if a given string is actually a number and converts it if it is.

**Definition** dbus-userdb.c:135

\_dbus_get_user_id

dbus_bool_t \_dbus_get_user_id(const DBusString \*username, dbus_uid_t \*uid)

Gets user ID given username.

**Definition** dbus-userdb-util.c:131

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

dbus_new

\#define dbus_new(type, count)

Safe macro for using dbus_malloc().

**Definition** dbus-memory.h:59

dbus_new0

\#define dbus_new0(type, count)

Safe macro for using dbus_malloc0().

**Definition** dbus-memory.h:60

DBUS_ERROR_NO_MEMORY

\#define DBUS_ERROR_NO_MEMORY

There was not enough memory to complete an operation.

**Definition** dbus-protocol.h:363

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

\_dbus_string_get_const_data

const char \* \_dbus_string_get_const_data(const DBusString \*str)

Gets the raw character buffer from a const string.

**Definition** dbus-string.c:513

\_dbus_group_info_fill

dbus_bool_t \_dbus_group_info_fill(DBusGroupInfo \*info, const DBusString \*groupname, DBusError \*error)

Initializes the given DBusGroupInfo struct with information about the given group name.

**Definition** dbus-sysdeps-util-unix.c:884

\_dbus_group_info_fill_gid

dbus_bool_t \_dbus_group_info_fill_gid(DBusGroupInfo \*info, dbus_gid_t gid, DBusError \*error)

Initializes the given DBusGroupInfo struct with information about the given group ID.

**Definition** dbus-sysdeps-util-unix.c:903

dbus_uid_t

unsigned long dbus_uid_t

A user ID.

**Definition** dbus-sysdeps.h:141

dbus_gid_t

unsigned long dbus_gid_t

A group ID.

**Definition** dbus-sysdeps.h:143

DBUS_UID_UNSET

\#define DBUS_UID_UNSET

an invalid UID used to represent an uninitialized dbus_uid_t field

**Definition** dbus-sysdeps.h:148

DBUS_GID_UNSET

\#define DBUS_GID_UNSET

an invalid GID used to represent an uninitialized dbus_gid_t field

**Definition** dbus-sysdeps.h:150

DBUS_GID_FORMAT

\#define DBUS_GID_FORMAT

an appropriate printf format for dbus_gid_t

**Definition** dbus-sysdeps.h:157

DBUS_UID_FORMAT

\#define DBUS_UID_FORMAT

an appropriate printf format for dbus_uid_t

**Definition** dbus-sysdeps.h:155

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusGroupInfo

Information about a UNIX group.

**Definition** dbus-sysdeps-unix.h:107

DBusGroupInfo::gid

dbus_gid_t gid

GID.

**Definition** dbus-sysdeps-unix.h:109

DBusGroupInfo::groupname

char \* groupname

Group name.

**Definition** dbus-sysdeps-unix.h:110

DBusGroupInfo::refcount

size_t refcount

Reference count.

**Definition** dbus-sysdeps-unix.h:108

DBusStat

Portable struct with stat() results.

**Definition** dbus-sysdeps.h:570

DBusStat::uid

dbus_uid_t uid

User owning file.

**Definition** dbus-sysdeps.h:573

DBusString

**Definition** dbus-string.h:47

DBusUserInfo

Information about a UNIX user.

**Definition** dbus-sysdeps-unix.h:93

DBusUserInfo::n_group_ids

int n_group_ids

Size of group IDs array.

**Definition** dbus-sysdeps-unix.h:98

DBusUserInfo::uid

dbus_uid_t uid

UID.

**Definition** dbus-sysdeps-unix.h:95

DBusUserInfo::group_ids

dbus_gid_t \* group_ids

Groups IDs, including above primary group.

**Definition** dbus-sysdeps-unix.h:97

DBusUserInfo::primary_gid

dbus_gid_t primary_gid

GID.

**Definition** dbus-sysdeps-unix.h:96
