dbus-asv-util.c

1/\* dbus-asv-util.c - utility functions for a{sv}

2 \*

3 \* Copyright © 2011-2012 Nokia Corporation

4 \* Copyright © 2012-2013 Collabora Ltd.

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

22 \* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA

23 \* 02110-1301 USA

24 \*/

25

26\#include \<config.h\>

27

28\#include \<dbus/dbus.h\>

29

30\#include "dbus/dbus-asv-util.h"

31

47DBusMessage \*

48\_dbus_asv_new_method_return (DBusMessage \*message,

49 DBusMessageIter \*iter,

50 DBusMessageIter \*arr_iter)

51{

52 DBusMessage \*reply = dbus_message_new_method_return (message);

53

54 if (reply == NULL)

55 return NULL;

56

57 dbus_message_iter_init_append (reply, iter);

58

59 if (!dbus_message_iter_open_container (iter, DBUS_TYPE_ARRAY, "{sv}",

60 arr_iter))

61 {

62 dbus_message_unref (reply);

63 return NULL;

64 }

65

66 return reply;

67}

68

69/\*

70 \* Open a new entry in an a{sv} (map from string to variant).

71 \*

72 \* This must be paired with a call to either \_dbus_asv_close_entry()

73 \* or \_dbus_asv_abandon_entry().

74 \*

75 \* If this function fails, the a{sv} must be abandoned, for instance

76 \* with \_dbus_asv_abandon().

77 \*

78 \* @param arr_iter the iterator which is appending to the array

79 \* @param entry_iter will be initialized to append to the dict-entry

80 \* @param key a UTF-8 key for the map

81 \* @param type the type of the variant value, e.g. DBUS_TYPE_STRING_AS_STRING

82 \* @param var_iter will be initialized to append (i.e. write) to the variant

83 \* @returns \#TRUE on success, or \#FALSE if not enough memory

84 \*/

85dbus_bool_t

86\_dbus_asv_open_entry (DBusMessageIter \*arr_iter,

87 DBusMessageIter \*entry_iter,

88 const char \*key,

89 const char \*type,

90 DBusMessageIter \*var_iter)

91{

92 if (!dbus_message_iter_open_container (arr_iter, DBUS_TYPE_DICT_ENTRY,

93 NULL, entry_iter))

94 return FALSE;

95

96 if (!dbus_message_iter_append_basic (entry_iter, DBUS_TYPE_STRING, &key))

97 {

98 dbus_message_iter_abandon_container (arr_iter, entry_iter);

99 return FALSE;

100 }

101

102 if (!dbus_message_iter_open_container (entry_iter, DBUS_TYPE_VARIANT,

103 type, var_iter))

104 {

105 dbus_message_iter_abandon_container (arr_iter, entry_iter);

106 return FALSE;

107 }

108

109 return TRUE;

110}

111

112/\*

113 \* Closes an a{sv} entry after successfully appending the value.

114 \*

115 \* If this function fails, the a{sv} must be abandoned, for instance

116 \* with \_dbus_asv_abandon().

117 \*

118 \* @param arr_iter the iterator which is appending to the array

119 \* @param entry_iter the iterator appending to the dict-entry, will be closed

120 \* @param var_iter the iterator appending to the variant, will be closed

121 \* @returns \#TRUE on success, or \#FALSE if not enough memory

122 \*/

123dbus_bool_t

124\_dbus_asv_close_entry (DBusMessageIter \*arr_iter,

125 DBusMessageIter \*entry_iter,

126 DBusMessageIter \*var_iter)

127{

128 if (!dbus_message_iter_close_container (entry_iter, var_iter))

129 {

130 dbus_message_iter_abandon_container (arr_iter, entry_iter);

131 return FALSE;

132 }

133

134 if (!dbus_message_iter_close_container (arr_iter, entry_iter))

135 return FALSE;

136

137 return TRUE;

138}

139

150dbus_bool_t

151\_dbus_asv_close (DBusMessageIter \*iter,

152 DBusMessageIter \*arr_iter)

153{

154 return dbus_message_iter_close_container (iter, arr_iter);

155}

156

157/\*

158 \* Closes an a{sv} entry after unsuccessfully appending a value.

159 \* You must also abandon the a{sv} itself (for instance with

160 \* \_dbus_asv_abandon()), and abandon whatever larger data structure

161 \* the a{sv} was embedded in.

162 \*

163 \* @param iter the iterator which is appending to the message or other data structure containing the a{sv}

164 \* @param arr_iter the iterator appending to the array, will be closed

165 \* @returns \#TRUE on success, or \#FALSE if not enough memory

166 \*/

167void

168\_dbus_asv_abandon_entry (DBusMessageIter \*arr_iter,

169 DBusMessageIter \*entry_iter,

170 DBusMessageIter \*var_iter)

171{

172 dbus_message_iter_abandon_container (entry_iter, var_iter);

173 dbus_message_iter_abandon_container (arr_iter, entry_iter);

174}

175

185void

186\_dbus_asv_abandon (DBusMessageIter \*iter,

187 DBusMessageIter \*arr_iter)

188{

189 dbus_message_iter_abandon_container (iter, arr_iter);

190}

191

204dbus_bool_t

205\_dbus_asv_add_uint32 (DBusMessageIter \*arr_iter,

206 const char \*key,

207 dbus_uint32_t value)

208{

209 DBusMessageIter entry_iter, var_iter;

210

211 if (!\_dbus_asv_open_entry (arr_iter, &entry_iter, key,

212 DBUS_TYPE_UINT32_AS_STRING, &var_iter))

213 return FALSE;

214

215 if (!dbus_message_iter_append_basic (&var_iter, DBUS_TYPE_UINT32,

216 &value))

217 {

218 \_dbus_asv_abandon_entry (arr_iter, &entry_iter, &var_iter);

219 return FALSE;

220 }

221

222 if (!\_dbus_asv_close_entry (arr_iter, &entry_iter, &var_iter))

223 return FALSE;

224

225 return TRUE;

226}

227

240dbus_bool_t

241\_dbus_asv_add_string (DBusMessageIter \*arr_iter,

242 const char \*key,

243 const char \*value)

244{

245 DBusMessageIter entry_iter, var_iter;

246

247 if (!\_dbus_asv_open_entry (arr_iter, &entry_iter, key,

248 DBUS_TYPE_STRING_AS_STRING, &var_iter))

249 return FALSE;

250

251 if (!dbus_message_iter_append_basic (&var_iter, DBUS_TYPE_STRING,

252 &value))

253 {

254 \_dbus_asv_abandon_entry (arr_iter, &entry_iter, &var_iter);

255 return FALSE;

256 }

257

258 if (!\_dbus_asv_close_entry (arr_iter, &entry_iter, &var_iter))

259 return FALSE;

260

261 return TRUE;

262}

263

276dbus_bool_t

277\_dbus_asv_add_object_path (DBusMessageIter \*arr_iter,

278 const char \*key,

279 const char \*value)

280{

281 DBusMessageIter entry_iter, var_iter;

282

283 if (!\_dbus_asv_open_entry (arr_iter, &entry_iter, key,

284 DBUS_TYPE_OBJECT_PATH_AS_STRING, &var_iter))

285 return FALSE;

286

287 if (!dbus_message_iter_append_basic (&var_iter, DBUS_TYPE_OBJECT_PATH,

288 &value))

289 {

290 \_dbus_asv_abandon_entry (arr_iter, &entry_iter, &var_iter);

291 return FALSE;

292 }

293

294 if (!\_dbus_asv_close_entry (arr_iter, &entry_iter, &var_iter))

295 return FALSE;

296

297 return TRUE;

298}

299

313dbus_bool_t

314\_dbus_asv_add_fixed_array (DBusMessageIter \*arr_iter,

315 const char \*key,

316 char element_type,

317 const void \*value,

318 int n_elements)

319{

320 const char type\[\] = { DBUS_TYPE_ARRAY, element_type, 0 };

321 DBusMessageIter entry_iter;

322 DBusMessageIter var_iter;

323 DBusMessageIter array_iter;

324

325 \_dbus_assert (dbus_type_is_fixed (element_type) && element_type != DBUS_TYPE_UNIX_FD);

326

327 if (!\_dbus_asv_open_entry (arr_iter, &entry_iter, key, type, &var_iter))

328 return FALSE;

329

330 if (!dbus_message_iter_open_container (&var_iter, DBUS_TYPE_ARRAY, type + 1,

331 &array_iter))

332 {

333 \_dbus_asv_abandon_entry (arr_iter, &entry_iter, &var_iter);

334 return FALSE;

335 }

336

337 if (!dbus_message_iter_append_fixed_array (&array_iter, element_type,

338 &value, n_elements))

339 {

340 dbus_message_iter_abandon_container (&var_iter, &array_iter);

341 \_dbus_asv_abandon_entry (arr_iter, &entry_iter, &var_iter);

342 return FALSE;

343 }

344

345 if (!dbus_message_iter_close_container (&var_iter, &array_iter))

346 {

347 \_dbus_asv_abandon_entry (arr_iter, &entry_iter, &var_iter);

348 return FALSE;

349 }

350

351 if (!\_dbus_asv_close_entry (arr_iter, &entry_iter, &var_iter))

352 return FALSE;

353

354 return TRUE;

355}

356

370dbus_bool_t

371\_dbus_asv_add_byte_array (DBusMessageIter \*arr_iter,

372 const char \*key,

373 const void \*value,

374 int n_elements)

375{

376 return \_dbus_asv_add_fixed_array (arr_iter, key, DBUS_TYPE_BYTE, value,

377 n_elements);

378}

379

395dbus_bool_t

396\_dbus_asv_add_unix_fd (DBusMessageIter \*arr_iter,

397 const char \*key,

398 int value)

399{

400 DBusMessageIter entry_iter, var_iter;

401

402 if (!\_dbus_asv_open_entry (arr_iter, &entry_iter, key,

403 DBUS_TYPE_UNIX_FD_AS_STRING, &var_iter))

404 return FALSE;

405

406 if (!dbus_message_iter_append_basic (&var_iter, DBUS_TYPE_UNIX_FD,

407 &value))

408 {

409 \_dbus_asv_abandon_entry (arr_iter, &entry_iter, &var_iter);

410 return FALSE;

411 }

412

413 if (!\_dbus_asv_close_entry (arr_iter, &entry_iter, &var_iter))

414 return FALSE;

415

416 return TRUE;

417}

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

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

dbus_message_iter_append_basic

dbus_bool_t dbus_message_iter_append_basic(DBusMessageIter \*iter, int type, const void \*value)

Appends a basic-typed value to the message.

**Definition** dbus-message.c:2771

dbus_message_iter_append_fixed_array

dbus_bool_t dbus_message_iter_append_fixed_array(DBusMessageIter \*iter, int element_type, const void \*value, int n_elements)

Appends a block of fixed-length values to an array.

**Definition** dbus-message.c:2922

dbus_message_iter_abandon_container

void dbus_message_iter_abandon_container(DBusMessageIter \*iter, DBusMessageIter \*sub)

Abandons creation of a contained-typed value and frees resources created by dbus_message_iter_open_co...

**Definition** dbus-message.c:3123

dbus_message_iter_open_container

dbus_bool_t dbus_message_iter_open_container(DBusMessageIter \*iter, int type, const char \*contained_signature, DBusMessageIter \*sub)

Appends a container-typed value to the message.

**Definition** dbus-message.c:2986

dbus_message_new_method_return

DBusMessage \* dbus_message_new_method_return(DBusMessage \*method_call)

Constructs a message that is a reply to a method call.

**Definition** dbus-message.c:1418

dbus_message_unref

void dbus_message_unref(DBusMessage \*message)

Decrements the reference count of a DBusMessage, freeing the message if the count reaches 0.

**Definition** dbus-message.c:1735

dbus_message_iter_close_container

dbus_bool_t dbus_message_iter_close_container(DBusMessageIter \*iter, DBusMessageIter \*sub)

Closes a container-typed value appended to the message; may write out more information to the message...

**Definition** dbus-message.c:3089

dbus_message_iter_init_append

void dbus_message_iter_init_append(DBusMessage \*message, DBusMessageIter \*iter)

Initializes a DBusMessageIter for appending arguments to the end of a message.

**Definition** dbus-message.c:2533

DBUS_TYPE_UNIX_FD_AS_STRING

\#define DBUS_TYPE_UNIX_FD_AS_STRING

DBUS_TYPE_UNIX_FD as a string literal instead of a int literal

**Definition** dbus-protocol.h:118

DBUS_TYPE_OBJECT_PATH

\#define DBUS_TYPE_OBJECT_PATH

Type code marking a D-Bus object path.

**Definition** dbus-protocol.h:108

DBUS_TYPE_BYTE

\#define DBUS_TYPE_BYTE

Type code marking an 8-bit unsigned integer.

**Definition** dbus-protocol.h:68

DBUS_TYPE_VARIANT

\#define DBUS_TYPE_VARIANT

Type code marking a D-Bus variant type.

**Definition** dbus-protocol.h:126

DBUS_TYPE_UNIX_FD

\#define DBUS_TYPE_UNIX_FD

Type code marking a unix file descriptor.

**Definition** dbus-protocol.h:116

DBUS_TYPE_STRING

\#define DBUS_TYPE_STRING

Type code marking a UTF-8 encoded, nul-terminated Unicode string.

**Definition** dbus-protocol.h:104

DBUS_TYPE_OBJECT_PATH_AS_STRING

\#define DBUS_TYPE_OBJECT_PATH_AS_STRING

DBUS_TYPE_OBJECT_PATH as a string literal instead of a int literal

**Definition** dbus-protocol.h:110

DBUS_TYPE_ARRAY

\#define DBUS_TYPE_ARRAY

Type code marking a D-Bus array type.

**Definition** dbus-protocol.h:122

DBUS_TYPE_STRING_AS_STRING

\#define DBUS_TYPE_STRING_AS_STRING

DBUS_TYPE_STRING as a string literal instead of a int literal

**Definition** dbus-protocol.h:106

DBUS_TYPE_DICT_ENTRY

\#define DBUS_TYPE_DICT_ENTRY

Type code used to represent a dict entry; however, this type code does not appear in type signatures,...

**Definition** dbus-protocol.h:145

DBUS_TYPE_UINT32_AS_STRING

\#define DBUS_TYPE_UINT32_AS_STRING

DBUS_TYPE_UINT32 as a string literal instead of a int literal

**Definition** dbus-protocol.h:90

DBUS_TYPE_UINT32

\#define DBUS_TYPE_UINT32

Type code marking a 32-bit unsigned integer.

**Definition** dbus-protocol.h:88

dbus_type_is_fixed

dbus_bool_t dbus_type_is_fixed(int typecode)

Tells you whether values of this type can change length if you set them to some other value.

**Definition** dbus-signature.c:355

DBusMessageIter

DBusMessageIter struct; contains no public fields.

**Definition** dbus-message.h:64

DBusMessage

Internals of DBusMessage.

**Definition** dbus-message-private.h:102
