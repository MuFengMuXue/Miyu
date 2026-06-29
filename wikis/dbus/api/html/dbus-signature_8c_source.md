dbus-signature.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-signature.c Routines for reading recursive type signatures

3 \*

4 \* Copyright (C) 2005 Red Hat, Inc.

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

28\#include "dbus-signature.h"

29\#include "dbus-marshal-recursive.h"

30\#include "dbus-marshal-basic.h"

31\#include "dbus-internals.h"

32\#include "dbus-test.h"

33\#include \<dbus/dbus-test-tap.h\>

34

38typedef struct

39{

40 const char \*pos;

41 unsigned int finished : 1;

42 unsigned int in_array : 1;

43} DBusSignatureRealIter;

44

45\_DBUS_STATIC_ASSERT (sizeof (DBusSignatureIter) \>= sizeof (DBusSignatureRealIter));

46

48\#define TYPE_IS_CONTAINER(typecode) \\

49 ((typecode) == DBUS_TYPE_STRUCT \|\| \\

50 (typecode) == DBUS_TYPE_DICT_ENTRY \|\| \\

51 (typecode) == DBUS_TYPE_VARIANT \|\| \\

52 (typecode) == DBUS_TYPE_ARRAY)

53

54

71void

72dbus_signature_iter_init (DBusSignatureIter \*iter,

73 const char \*signature)

74{

75 DBusSignatureRealIter \*real_iter = (DBusSignatureRealIter \*) iter;

76

77 real_iter-\>pos = signature;

78 real_iter-\>finished = FALSE;

79 real_iter-\>in_array = FALSE;

80}

81

96int

97dbus_signature_iter_get_current_type (const DBusSignatureIter \*iter)

98{

99 DBusSignatureRealIter \*real_iter = (DBusSignatureRealIter \*) iter;

100

101 return \_dbus_first_type_in_signature_c_str (real_iter-\>pos, 0);

102}

103

116char \*

117dbus_signature_iter_get_signature (const DBusSignatureIter \*iter)

118{

119 DBusSignatureRealIter \*real_iter = (DBusSignatureRealIter \*) iter;

120 DBusString str;

121 char \*ret;

122 int pos;

123

124 if (!\_dbus_string_init (&str))

125 return NULL;

126

127 pos = 0;

128 \_dbus_type_signature_next (real_iter-\>pos, &pos);

129

130 if (!\_dbus_string_append_len (&str, real_iter-\>pos, pos))

131 return NULL;

132 if (!\_dbus_string_steal_data (&str, &ret))

133 ret = NULL;

134 \_dbus_string_free (&str);

135

136 return ret;

137}

138

150int

151dbus_signature_iter_get_element_type (const DBusSignatureIter \*iter)

152{

153 DBusSignatureRealIter \*real_iter = (DBusSignatureRealIter \*) iter;

154

155 \_dbus_return_val_if_fail (dbus_signature_iter_get_current_type (iter) == DBUS_TYPE_ARRAY, DBUS_TYPE_INVALID);

156

157 return \_dbus_first_type_in_signature_c_str (real_iter-\>pos, 1);

158}

159

168dbus_bool_t

169dbus_signature_iter_next (DBusSignatureIter \*iter)

170{

171 DBusSignatureRealIter \*real_iter = (DBusSignatureRealIter \*) iter;

172

173 if (real_iter-\>finished)

174 return FALSE;

175 else

176 {

177 int pos;

178

179 if (real_iter-\>in_array)

180 {

181 real_iter-\>finished = TRUE;

182 return FALSE;

183 }

184

185 pos = 0;

186 \_dbus_type_signature_next (real_iter-\>pos, &pos);

187 real_iter-\>pos += pos;

188

189 if (\*real_iter-\>pos == DBUS_STRUCT_END_CHAR

190 \|\| \*real_iter-\>pos == DBUS_DICT_ENTRY_END_CHAR)

191 {

192 real_iter-\>finished = TRUE;

193 return FALSE;

194 }

195

196 return \*real_iter-\>pos != DBUS_TYPE_INVALID;

197 }

198}

199

211void

212dbus_signature_iter_recurse (const DBusSignatureIter \*iter,

213 DBusSignatureIter \*subiter)

214{

215 DBusSignatureRealIter \*real_iter = (DBusSignatureRealIter \*) iter;

216 DBusSignatureRealIter \*real_sub_iter = (DBusSignatureRealIter \*) subiter;

217

218 \_dbus_return_if_fail (dbus_type_is_container (dbus_signature_iter_get_current_type (iter)));

219

220 \*real_sub_iter = \*real_iter;

221 real_sub_iter-\>in_array = FALSE;

222 real_sub_iter-\>pos++;

223

224 if (dbus_signature_iter_get_current_type (iter) == DBUS_TYPE_ARRAY)

225 real_sub_iter-\>in_array = TRUE;

226}

227

237dbus_bool_t

238dbus_signature_validate (const char \*signature,

239 DBusError \*error)

240

241{

242 DBusString str;

243 DBusValidity reason;

244

245 \_dbus_string_init_const (&str, signature);

246 reason = \_dbus_validate_signature_with_reason (&str, 0, \_dbus_string_get_length (&str));

247

248 if (reason == DBUS_VALID)

249 return TRUE;

250 else

251 {

252 dbus_set_error (error, DBUS_ERROR_INVALID_SIGNATURE, "%s",

253 \_dbus_validity_to_error_message (reason));

254 return FALSE;

255 }

256}

257

269dbus_bool_t

270dbus_signature_validate_single (const char \*signature,

271 DBusError \*error)

272{

273 DBusSignatureIter iter;

274

275 if (!dbus_signature_validate (signature, error))

276 return FALSE;

277

278 dbus_signature_iter_init (&iter, signature);

279 if (dbus_signature_iter_get_current_type (&iter) == DBUS_TYPE_INVALID)

280 goto lose;

281 if (!dbus_signature_iter_next (&iter))

282 return TRUE;

283 lose:

284 dbus_set_error (error, DBUS_ERROR_INVALID_SIGNATURE, "Exactly one complete type required in signature");

285 return FALSE;

286}

287

299dbus_bool_t

300dbus_type_is_container (int typecode)

301{

302 /\* only reasonable (non-line-noise) typecodes are allowed \*/

303 \_dbus_return_val_if_fail (dbus_type_is_valid (typecode) \|\| typecode == DBUS_TYPE_INVALID,

304 FALSE);

305 return TYPE_IS_CONTAINER (typecode);

306}

307

323dbus_bool_t

324dbus_type_is_basic (int typecode)

325{

326 /\* only reasonable (non-line-noise) typecodes are allowed \*/

327 \_dbus_return_val_if_fail (dbus_type_is_valid (typecode) \|\| typecode == DBUS_TYPE_INVALID,

328 FALSE);

329

330 /\* everything that isn't invalid or a container \*/

331 return !(typecode == DBUS_TYPE_INVALID \|\| TYPE_IS_CONTAINER (typecode));

332}

333

354dbus_bool_t

355dbus_type_is_fixed (int typecode)

356{

357 /\* only reasonable (non-line-noise) typecodes are allowed \*/

358 \_dbus_return_val_if_fail (dbus_type_is_valid (typecode) \|\| typecode == DBUS_TYPE_INVALID,

359 FALSE);

360

361 switch (typecode)

362 {

363 case DBUS_TYPE_BYTE:

364 case DBUS_TYPE_BOOLEAN:

365 case DBUS_TYPE_INT16:

366 case DBUS_TYPE_UINT16:

367 case DBUS_TYPE_INT32:

368 case DBUS_TYPE_UINT32:

369 case DBUS_TYPE_INT64:

370 case DBUS_TYPE_UINT64:

371 case DBUS_TYPE_DOUBLE:

372 case DBUS_TYPE_UNIX_FD:

373 return TRUE;

374 default:

375 return FALSE;

376 }

377}

378

388dbus_bool_t

389dbus_type_is_valid (int typecode)

390{

391 switch (typecode)

392 {

393 case DBUS_TYPE_BYTE:

394 case DBUS_TYPE_BOOLEAN:

395 case DBUS_TYPE_INT16:

396 case DBUS_TYPE_UINT16:

397 case DBUS_TYPE_INT32:

398 case DBUS_TYPE_UINT32:

399 case DBUS_TYPE_INT64:

400 case DBUS_TYPE_UINT64:

401 case DBUS_TYPE_DOUBLE:

402 case DBUS_TYPE_STRING:

403 case DBUS_TYPE_OBJECT_PATH:

404 case DBUS_TYPE_SIGNATURE:

405 case DBUS_TYPE_ARRAY:

406 case DBUS_TYPE_STRUCT:

407 case DBUS_TYPE_DICT_ENTRY:

408 case DBUS_TYPE_VARIANT:

409 case DBUS_TYPE_UNIX_FD:

410 return TRUE;

411

412 default:

413 return FALSE;

414 }

415}

416

/\* end of DBusSignature group \*/

dbus_set_error

void dbus_set_error(DBusError \*error, const char \*name, const char \*format,...)

Assigns an error name and message to a DBusError.

**Definition** dbus-errors.c:356

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

DBusValidity

DBusValidity

This is primarily used in unit testing, so we can verify that each invalid message is invalid for the...

**Definition** dbus-marshal-validate.h:54

\_dbus_validate_signature_with_reason

DBusValidity \_dbus_validate_signature_with_reason(const DBusString \*type_str, int type_pos, int len)

Verifies that the range of type_str from type_pos to type_end is a valid signature.

**Definition** dbus-marshal-validate.c:53

\_dbus_first_type_in_signature_c_str

int \_dbus_first_type_in_signature_c_str(const char \*str, int pos)

Similar to \_dbus_first_type_in_signature, but operates on a C string buffer.

**Definition** dbus-marshal-basic.c:1499

\_dbus_type_signature_next

void \_dbus_type_signature_next(const char \*type_str, int \*type_pos)

Skips to the next "complete" type inside a type signature.

**Definition** dbus-marshal-recursive.c:340

DBUS_VALID

@ DBUS_VALID

the data is valid

**Definition** dbus-marshal-validate.h:60

DBUS_TYPE_SIGNATURE

\#define DBUS_TYPE_SIGNATURE

Type code marking a D-Bus type signature.

**Definition** dbus-protocol.h:112

DBUS_DICT_ENTRY_END_CHAR

\#define DBUS_DICT_ENTRY_END_CHAR

Code marking the end of a dict entry type in a type signature.

**Definition** dbus-protocol.h:170

DBUS_TYPE_OBJECT_PATH

\#define DBUS_TYPE_OBJECT_PATH

Type code marking a D-Bus object path.

**Definition** dbus-protocol.h:108

DBUS_TYPE_BYTE

\#define DBUS_TYPE_BYTE

Type code marking an 8-bit unsigned integer.

**Definition** dbus-protocol.h:68

DBUS_TYPE_INT16

\#define DBUS_TYPE_INT16

Type code marking a 16-bit signed integer.

**Definition** dbus-protocol.h:76

DBUS_TYPE_VARIANT

\#define DBUS_TYPE_VARIANT

Type code marking a D-Bus variant type.

**Definition** dbus-protocol.h:126

DBUS_TYPE_INT32

\#define DBUS_TYPE_INT32

Type code marking a 32-bit signed integer.

**Definition** dbus-protocol.h:84

DBUS_TYPE_UNIX_FD

\#define DBUS_TYPE_UNIX_FD

Type code marking a unix file descriptor.

**Definition** dbus-protocol.h:116

DBUS_TYPE_BOOLEAN

\#define DBUS_TYPE_BOOLEAN

Type code marking a boolean.

**Definition** dbus-protocol.h:72

DBUS_TYPE_STRING

\#define DBUS_TYPE_STRING

Type code marking a UTF-8 encoded, nul-terminated Unicode string.

**Definition** dbus-protocol.h:104

DBUS_TYPE_ARRAY

\#define DBUS_TYPE_ARRAY

Type code marking a D-Bus array type.

**Definition** dbus-protocol.h:122

DBUS_TYPE_INVALID

\#define DBUS_TYPE_INVALID

Type code that is never equal to a legitimate type code.

**Definition** dbus-protocol.h:62

DBUS_TYPE_INT64

\#define DBUS_TYPE_INT64

Type code marking a 64-bit signed integer.

**Definition** dbus-protocol.h:92

DBUS_TYPE_DOUBLE

\#define DBUS_TYPE_DOUBLE

Type code marking an 8-byte double in IEEE 754 format.

**Definition** dbus-protocol.h:100

DBUS_ERROR_INVALID_SIGNATURE

\#define DBUS_ERROR_INVALID_SIGNATURE

A type signature is not valid.

**Definition** dbus-protocol.h:448

DBUS_TYPE_UINT64

\#define DBUS_TYPE_UINT64

Type code marking a 64-bit unsigned integer.

**Definition** dbus-protocol.h:96

DBUS_TYPE_DICT_ENTRY

\#define DBUS_TYPE_DICT_ENTRY

Type code used to represent a dict entry; however, this type code does not appear in type signatures,...

**Definition** dbus-protocol.h:145

DBUS_TYPE_UINT16

\#define DBUS_TYPE_UINT16

Type code marking a 16-bit unsigned integer.

**Definition** dbus-protocol.h:80

DBUS_TYPE_STRUCT

\#define DBUS_TYPE_STRUCT

STRUCT and DICT_ENTRY are sort of special since their codes can't appear in a type string,...

**Definition** dbus-protocol.h:138

DBUS_STRUCT_END_CHAR

\#define DBUS_STRUCT_END_CHAR

Code marking the end of a struct type in a type signature.

**Definition** dbus-protocol.h:162

DBUS_TYPE_UINT32

\#define DBUS_TYPE_UINT32

Type code marking a 32-bit unsigned integer.

**Definition** dbus-protocol.h:88

dbus_signature_iter_recurse

void dbus_signature_iter_recurse(const DBusSignatureIter \*iter, DBusSignatureIter \*subiter)

Initialize a new iterator pointing to the first type in the current container.

**Definition** dbus-signature.c:212

dbus_signature_validate

dbus_bool_t dbus_signature_validate(const char \*signature, DBusError \*error)

Check a type signature for validity.

**Definition** dbus-signature.c:238

dbus_type_is_basic

dbus_bool_t dbus_type_is_basic(int typecode)

A "basic type" is a somewhat arbitrary concept, but the intent is to include those types that are ful...

**Definition** dbus-signature.c:324

dbus_type_is_fixed

dbus_bool_t dbus_type_is_fixed(int typecode)

Tells you whether values of this type can change length if you set them to some other value.

**Definition** dbus-signature.c:355

dbus_type_is_valid

dbus_bool_t dbus_type_is_valid(int typecode)

Return TRUE if the argument is a valid typecode.

**Definition** dbus-signature.c:389

dbus_signature_iter_get_signature

char \* dbus_signature_iter_get_signature(const DBusSignatureIter \*iter)

Returns the signature of the single complete type starting at the given iterator.

**Definition** dbus-signature.c:117

dbus_signature_iter_next

dbus_bool_t dbus_signature_iter_next(DBusSignatureIter \*iter)

Skip to the next value on this "level".

**Definition** dbus-signature.c:169

dbus_type_is_container

dbus_bool_t dbus_type_is_container(int typecode)

A "container type" can contain basic types, or nested container types.

**Definition** dbus-signature.c:300

dbus_signature_iter_init

void dbus_signature_iter_init(DBusSignatureIter \*iter, const char \*signature)

Initializes a DBusSignatureIter for reading a type signature.

**Definition** dbus-signature.c:72

dbus_signature_validate_single

dbus_bool_t dbus_signature_validate_single(const char \*signature, DBusError \*error)

Check that a type signature is both valid and contains exactly one complete type.

**Definition** dbus-signature.c:270

dbus_signature_iter_get_current_type

int dbus_signature_iter_get_current_type(const DBusSignatureIter \*iter)

Returns the current type pointed to by the iterator.

**Definition** dbus-signature.c:97

dbus_signature_iter_get_element_type

int dbus_signature_iter_get_element_type(const DBusSignatureIter \*iter)

Convenience function for returning the element type of an array; This function allows you to avoid in...

**Definition** dbus-signature.c:151

\_dbus_string_init

dbus_bool_t \_dbus_string_init(DBusString \*str)

Initializes a string.

**Definition** dbus-string.c:182

\_dbus_string_init_const

void \_dbus_string_init_const(DBusString \*str, const char \*value)

Initializes a constant string.

**Definition** dbus-string.c:197

\_dbus_string_steal_data

dbus_bool_t \_dbus_string_steal_data(DBusString \*str, char \*\*data_return)

Like \_dbus_string_get_data(), but removes the gotten data from the original string.

**Definition** dbus-string.c:686

\_dbus_string_append_len

dbus_bool_t \_dbus_string_append_len(DBusString \*str, const char \*buffer, int len)

Appends block of bytes with the given length to a DBusString.

**Definition** dbus-string.c:1170

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_string_get_length

int \_dbus_string_get_length(const DBusString \*str)

Gets the length of a string (not including nul termination).

**Definition** dbus-string.c:784

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusSignatureIter

DBusSignatureIter struct; contains no public fields.

**Definition** dbus-signature.h:47

DBusSignatureRealIter

Implementation details of DBusSignatureIter, all fields are private.

**Definition** dbus-signature.c:39

DBusSignatureRealIter::finished

unsigned int finished

true if we are at the end iter

**Definition** dbus-signature.c:41

DBusSignatureRealIter::in_array

unsigned int in_array

true if we are a subiterator pointing to an array's element type

**Definition** dbus-signature.c:42

DBusSignatureRealIter::pos

const char \* pos

current position in the signature string

**Definition** dbus-signature.c:40

DBusString

**Definition** dbus-string.h:47
