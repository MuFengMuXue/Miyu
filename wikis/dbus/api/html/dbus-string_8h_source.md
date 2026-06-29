dbus-string.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-string.h String utility class (internal to D-Bus implementation)

3 \*

4 \* Copyright (C) 2002, 2003 Red Hat, Inc.

5 \* Copyright (C) 2006 Ralf Habacker \<ralf.habacker@freenet.de\>

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

27\#ifndef DBUS_STRING_H

28\#define DBUS_STRING_H

29

30\#include \<dbus/dbus-macros.h\>

31\#include \<dbus/dbus-types.h\>

32\#include \<dbus/dbus-memory.h\>

33

34\#include \<stdarg.h\>

35

36\#include \<dbus/dbus-macros-internal.h\>

37

38DBUS_BEGIN_DECLS

39

44typedef struct DBusString DBusString;

45

46struct DBusString

47{

48\#if defined(DBUS_WIN) && defined(\_DEBUG)

49 const char \*dummy1;

50\#else

51 const void \*dummy1;

52\#endif

53 int dummy2;

54 int dummy3;

55 unsigned int dummy_bit1 : 1;

56 unsigned int dummy_bit2 : 1;

57 unsigned int dummy_bit3 : 1;

58 unsigned int dummy_bits : 3;

59};

60

66\#define \_DBUS_STRING_INIT_INVALID \\

67{ \\

68 NULL, /\* dummy1 \*/ \\

69 0, /\* dummy2 \*/ \\

70 0, /\* dummy3 \*/ \\

71 0, /\* dummy_bit1 \*/ \\

72 0, /\* dummy_bit2 \*/ \\

73 0, /\* dummy_bit3 \*/ \\

74 0 /\* dummy_bits \*/ \\

75}

76

77\#ifdef DBUS_DISABLE_ASSERT

78/\* Some simple inlining hacks; the current linker is not smart enough

79 \* to inline non-exported symbols across files in the library.

80 \* Note that these break type safety (due to the casts)

81 \*/

82\#define \_dbus_string_get_data(s) ((char\*)(((DBusString\*)(s))-\>dummy1))

83\#define \_dbus_string_get_length(s) (((DBusString\*)(s))-\>dummy2)

84\#define \_dbus_string_set_byte(s, i, b) ((((unsigned char\*)(((DBusString\*)(s))-\>dummy1))\[(i)\]) = (unsigned char) (b))

85\#define \_dbus_string_get_byte(s, i) (((const unsigned char\*)(((DBusString\*)(s))-\>dummy1))\[(i)\])

86\#define \_dbus_string_get_const_data(s) ((const char\*)(((DBusString\*)(s))-\>dummy1))

87\#define \_dbus_string_get_const_data_len(s,start,len) (((const char\*)(((DBusString\*)(s))-\>dummy1)) + (start))

88\#endif

89

90DBUS_PRIVATE_EXPORT

91dbus_bool_t \_dbus_string_init (DBusString \*str);

92DBUS_PRIVATE_EXPORT

93void \_dbus_string_init_const (DBusString \*str,

94 const char \*value);

95DBUS_PRIVATE_EXPORT

96void \_dbus_string_init_const_len (DBusString \*str,

97 const char \*value,

98 int len);

99DBUS_PRIVATE_EXPORT

100dbus_bool_t \_dbus_string_init_preallocated (DBusString \*str,

101 int allocate_size);

102

103DBUS_PRIVATE_EXPORT

104dbus_bool_t \_dbus_string_init_from_string (DBusString \*str,

105 const DBusString \*from);

106DBUS_PRIVATE_EXPORT

107void \_dbus_string_free (DBusString \*str);

108void \_dbus_string_lock (DBusString \*str);

109DBUS_PRIVATE_EXPORT

110dbus_bool_t \_dbus_string_compact (DBusString \*str,

111 int max_waste);

112DBUS_PRIVATE_EXPORT

113int \_dbus_string_get_allocated_size (const DBusString \*str);

114\#ifndef \_dbus_string_get_data

115DBUS_PRIVATE_EXPORT

116char\* \_dbus_string_get_data (DBusString \*str);

117\#endif /\* \_dbus_string_get_data \*/

118\#ifndef \_dbus_string_get_const_data

119DBUS_PRIVATE_EXPORT

120const char\* \_dbus_string_get_const_data (const DBusString \*str);

121\#endif /\* \_dbus_string_get_const_data \*/

122DBUS_PRIVATE_EXPORT

123char\* \_dbus_string_get_data_len (DBusString \*str,

124 int start,

125 int len);

126\#ifndef \_dbus_string_get_const_data_len

127DBUS_PRIVATE_EXPORT

128const char\* \_dbus_string_get_const_data_len (const DBusString \*str,

129 int start,

130 int len);

131\#endif

132\#ifndef \_dbus_string_set_byte

133DBUS_PRIVATE_EXPORT

134void \_dbus_string_set_byte (DBusString \*str,

135 int i,

136 unsigned char byte);

137\#endif

138\#ifndef \_dbus_string_get_byte

139DBUS_PRIVATE_EXPORT

140unsigned char \_dbus_string_get_byte (const DBusString \*str,

141 int start);

142\#endif /\* \_dbus_string_get_byte \*/

143DBUS_PRIVATE_EXPORT

144dbus_bool_t \_dbus_string_insert_bytes (DBusString \*str,

145 int i,

146 int n_bytes,

147 unsigned char byte);

148DBUS_PRIVATE_EXPORT

149dbus_bool_t \_dbus_string_insert_byte (DBusString \*str,

150 int i,

151 unsigned char byte);

152DBUS_PRIVATE_EXPORT

153dbus_bool_t \_dbus_string_steal_data (DBusString \*str,

154 char \*\*data_return);

155dbus_bool_t \_dbus_string_steal_data_len (DBusString \*str,

156 char \*\*data_return,

157 int start,

158 int len);

159DBUS_PRIVATE_EXPORT

160dbus_bool_t \_dbus_string_copy_data (const DBusString \*str,

161 char \*\*data_return);

162dbus_bool_t \_dbus_string_copy_data_len (const DBusString \*str,

163 char \*\*data_return,

164 int start,

165 int len);

166void \_dbus_string_copy_to_buffer (const DBusString \*str,

167 char \*buffer,

168 int len);

169DBUS_PRIVATE_EXPORT

170void \_dbus_string_copy_to_buffer_with_nul (const DBusString \*str,

171 char \*buffer,

172 int avail_len);

173\#ifndef \_dbus_string_get_length

174DBUS_PRIVATE_EXPORT

175int \_dbus_string_get_length (const DBusString \*str);

176\#endif /\* !\_dbus_string_get_length \*/

177

188static inline unsigned int

189\_dbus_string_get_length_uint (const DBusString \*str)

190{

191 return (unsigned int) \_dbus_string_get_length (str);

192}

193

194DBUS_PRIVATE_EXPORT

195dbus_bool_t \_dbus_string_lengthen (DBusString \*str,

196 int additional_length);

197DBUS_PRIVATE_EXPORT

198void \_dbus_string_shorten (DBusString \*str,

199 int length_to_remove);

200DBUS_PRIVATE_EXPORT

201dbus_bool_t \_dbus_string_set_length (DBusString \*str,

202 int length);

203dbus_bool_t \_dbus_string_align_length (DBusString \*str,

204 int alignment);

205dbus_bool_t \_dbus_string_alloc_space (DBusString \*str,

206 int extra_bytes);

207DBUS_PRIVATE_EXPORT

208dbus_bool_t \_dbus_string_append (DBusString \*str,

209 const char \*buffer);

210DBUS_PRIVATE_EXPORT

211dbus_bool_t \_dbus_string_append_len (DBusString \*str,

212 const char \*buffer,

213 int len);

214DBUS_PRIVATE_EXPORT

215dbus_bool_t \_dbus_string_append_byte (DBusString \*str,

216 unsigned char byte);

217DBUS_PRIVATE_EXPORT

218dbus_bool_t \_dbus_string_append_strings (DBusString \*str,

219 char \*\*strings,

220 char separator);

221DBUS_PRIVATE_EXPORT

222dbus_bool_t \_dbus_string_append_printf (DBusString \*str,

223 const char \*format,

224 ...) \_DBUS_GNUC_PRINTF (2, 3);

225DBUS_PRIVATE_EXPORT

226dbus_bool_t \_dbus_string_append_printf_valist (DBusString \*str,

227 const char \*format,

228 va_list args) \_DBUS_GNUC_PRINTF (2, 0);

229dbus_bool_t \_dbus_string_insert_2_aligned (DBusString \*str,

230 int insert_at,

231 const unsigned char octets\[2\]);

232dbus_bool_t \_dbus_string_insert_4_aligned (DBusString \*str,

233 int insert_at,

234 const unsigned char octets\[4\]);

235DBUS_PRIVATE_EXPORT

236dbus_bool_t \_dbus_string_insert_8_aligned (DBusString \*str,

237 int insert_at,

238 const unsigned char octets\[8\]);

239dbus_bool_t \_dbus_string_insert_alignment (DBusString \*str,

240 int \*insert_at,

241 int alignment);

242DBUS_PRIVATE_EXPORT

243void \_dbus_string_delete (DBusString \*str,

244 int start,

245 int len);

246DBUS_PRIVATE_EXPORT

247dbus_bool_t \_dbus_string_move (DBusString \*source,

248 int start,

249 DBusString \*dest,

250 int insert_at);

251DBUS_PRIVATE_EXPORT

252dbus_bool_t \_dbus_string_copy (const DBusString \*source,

253 int start,

254 DBusString \*dest,

255 int insert_at);

256dbus_bool_t \_dbus_string_move_len (DBusString \*source,

257 int start,

258 int len,

259 DBusString \*dest,

260 int insert_at);

261DBUS_PRIVATE_EXPORT

262dbus_bool_t \_dbus_string_copy_len (const DBusString \*source,

263 int start,

264 int len,

265 DBusString \*dest,

266 int insert_at);

267DBUS_PRIVATE_EXPORT

268dbus_bool_t \_dbus_string_replace_len (const DBusString \*source,

269 int start,

270 int len,

271 DBusString \*dest,

272 int replace_at,

273 int replace_len);

274DBUS_PRIVATE_EXPORT

275dbus_bool_t \_dbus_string_split_on_byte (DBusString \*source,

276 unsigned char byte,

277 DBusString \*tail);

278DBUS_PRIVATE_EXPORT

279dbus_bool_t \_dbus_string_parse_int (const DBusString \*str,

280 int start,

281 long \*value_return,

282 int \*end_return);

283DBUS_PRIVATE_EXPORT

284dbus_bool_t \_dbus_string_parse_uint (const DBusString \*str,

285 int start,

286 unsigned long \*value_return,

287 int \*end_return);

288DBUS_PRIVATE_EXPORT

289dbus_bool_t \_dbus_string_parse_int64 (const DBusString \*str,

290 int start,

291 dbus_int64_t \*value_return,

292 int \*end_return);

293DBUS_PRIVATE_EXPORT

294dbus_bool_t \_dbus_string_find (const DBusString \*str,

295 int start,

296 const char \*substr,

297 int \*found);

298DBUS_PRIVATE_EXPORT

299dbus_bool_t \_dbus_string_find_eol (const DBusString \*str,

300 int start,

301 int \*found,

302 int \*found_len);

303DBUS_PRIVATE_EXPORT

304dbus_bool_t \_dbus_string_find_to (const DBusString \*str,

305 int start,

306 int end,

307 const char \*substr,

308 int \*found);

309dbus_bool_t \_dbus_string_find_byte_backward (const DBusString \*str,

310 int start,

311 unsigned char byte,

312 int \*found);

313DBUS_PRIVATE_EXPORT

314dbus_bool_t \_dbus_string_find_blank (const DBusString \*str,

315 int start,

316 int \*found);

317DBUS_PRIVATE_EXPORT

318void \_dbus_string_skip_blank (const DBusString \*str,

319 int start,

320 int \*end);

321DBUS_PRIVATE_EXPORT

322void \_dbus_string_skip_white (const DBusString \*str,

323 int start,

324 int \*end);

325void \_dbus_string_skip_white_reverse (const DBusString \*str,

326 int end,

327 int \*start);

328DBUS_PRIVATE_EXPORT

329dbus_bool_t \_dbus_string_equal (const DBusString \*a,

330 const DBusString \*b);

331DBUS_PRIVATE_EXPORT

332dbus_bool_t \_dbus_string_equal_c_str (const DBusString \*a,

333 const char \*c_str);

334DBUS_PRIVATE_EXPORT

335dbus_bool_t \_dbus_string_equal_len (const DBusString \*a,

336 const DBusString \*b,

337 int len);

338DBUS_PRIVATE_EXPORT

339dbus_bool_t \_dbus_string_equal_substring (const DBusString \*a,

340 int a_start,

341 int a_len,

342 const DBusString \*b,

343 int b_start);

344DBUS_PRIVATE_EXPORT

345dbus_bool_t \_dbus_string_starts_with_c_str (const DBusString \*a,

346 const char \*c_str);

347dbus_bool_t \_dbus_string_ends_with_c_str (const DBusString \*a,

348 const char \*c_str);

349DBUS_PRIVATE_EXPORT

350dbus_bool_t \_dbus_string_starts_with_words_c_str (const DBusString \*a,

351 const char \*c_str,

352 char word_separator);

353DBUS_PRIVATE_EXPORT

354dbus_bool_t \_dbus_string_pop_line (DBusString \*source,

355 DBusString \*dest);

356DBUS_PRIVATE_EXPORT

357void \_dbus_string_delete_first_word (DBusString \*str);

358DBUS_PRIVATE_EXPORT

359void \_dbus_string_delete_leading_blanks (DBusString \*str);

360DBUS_PRIVATE_EXPORT

361void \_dbus_string_chop_white (DBusString \*str);

362dbus_bool_t \_dbus_string_append_byte_as_hex (DBusString \*str,

363 unsigned char byte);

364DBUS_EMBEDDED_TESTS_EXPORT

365dbus_bool_t \_dbus_string_append_buffer_as_hex (DBusString \*str,

366 void \*buf,

367 int size);

368DBUS_PRIVATE_EXPORT

369dbus_bool_t \_dbus_string_hex_encode (const DBusString \*source,

370 int start,

371 DBusString \*dest,

372 int insert_at);

373DBUS_PRIVATE_EXPORT

374dbus_bool_t \_dbus_string_hex_decode (const DBusString \*source,

375 int start,

376 int \*end_return,

377 DBusString \*dest,

378 int insert_at);

379DBUS_PRIVATE_EXPORT

380void \_dbus_string_tolower_ascii (const DBusString \*str,

381 int start,

382 int len);

383DBUS_PRIVATE_EXPORT

384void \_dbus_string_toupper_ascii (const DBusString \*str,

385 int start,

386 int len);

387dbus_bool_t \_dbus_string_validate_ascii (const DBusString \*str,

388 int start,

389 int len);

390DBUS_PRIVATE_EXPORT

391dbus_bool_t \_dbus_string_validate_utf8 (const DBusString \*str,

392 int start,

393 int len);

394DBUS_PRIVATE_EXPORT

395dbus_bool_t \_dbus_string_validate_nul (const DBusString \*str,

396 int start,

397 int len);

398void \_dbus_string_zero (DBusString \*str);

399

400static inline unsigned char \*

401\_dbus_string_get_udata (DBusString \*str)

402{

403 return (unsigned char \*) \_dbus_string_get_data (str);

404}

405

406static inline unsigned char \*

407\_dbus_string_get_udata_len (DBusString \*str, int start, int len)

408{

409 return (unsigned char \*) \_dbus_string_get_data_len (str, start, len);

410}

411

412static inline const unsigned char \*

413\_dbus_string_get_const_udata (const DBusString \*str)

414{

415 return (const unsigned char \*) \_dbus_string_get_const_data (str);

416}

417

418static inline const unsigned char \*

419\_dbus_string_get_const_udata_len (const DBusString \*str, int start, int len)

420{

421 return (const unsigned char \*) \_dbus_string_get_const_data_len (str, start, len);

422}

423

429\#define \_DBUS_STRING_ALLOCATION_PADDING 8

430

438\#define \_DBUS_STRING_DEFINE_STATIC(name, str) \\

439 static const char \_dbus_static_string\_##name\[\] = str; \\

440 static const DBusString name = { \_dbus_static_string\_##name, \\

441 sizeof(\_dbus_static_string\_##name) - 1, \\

442 sizeof(\_dbus_static_string\_##name) + \\

443 \_DBUS_STRING_ALLOCATION_PADDING, \\

444 TRUE, TRUE, TRUE, 0 }

445

446DBUS_END_DECLS

447

448\#endif /\* DBUS_STRING_H \*/

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

\_dbus_string_set_length

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_set_length(DBusString \*str, int length)

Sets the length of a string.

**Definition** dbus-string.c:847

\_dbus_string_hex_decode

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_hex_decode(const DBusString \*source, int start, int \*end_return, DBusString \*dest, int insert_at)

Decodes a string from hex encoding.

**Definition** dbus-string.c:2432

\_dbus_string_append

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_append(DBusString \*str, const char \*buffer)

Appends a nul-terminated C-style string to a DBusString.

**Definition** dbus-string.c:980

\_dbus_string_insert_8_aligned

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_insert_8_aligned(DBusString \*str, int insert_at, const unsigned char octets\[8\])

Inserts 8 bytes aligned on an 8 byte boundary with any alignment padding initialized to 0.

**Definition** dbus-string.c:1053

\_dbus_string_validate_nul

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_validate_nul(const DBusString \*str, int start, int len)

Checks that the given range of the string is all nul bytes.

**Definition** dbus-string.c:2776

\_dbus_string_equal_substring

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_equal_substring(const DBusString \*a, int a_start, int a_len, const DBusString \*b, int b_start)

Tests two sub-parts of two DBusString for equality.

**Definition** dbus-string.c:2166

\_dbus_string_insert_alignment

dbus_bool_t \_dbus_string_insert_alignment(DBusString \*str, int \*insert_at, int alignment)

Inserts padding at \*insert_at such to align it to the given boundary.

**Definition** dbus-string.c:1081

\_dbus_string_init

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_init(DBusString \*str)

Initializes a string.

**Definition** dbus-string.c:182

\_dbus_string_append_strings

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_append_strings(DBusString \*str, char \*\*strings, char separator)

Append vector with strings connected by separator.

**Definition** dbus-string.c:1213

\_dbus_string_init_const

DBUS_PRIVATE_EXPORT void \_dbus_string_init_const(DBusString \*str, const char \*value)

Initializes a constant string.

**Definition** dbus-string.c:197

\_dbus_string_copy

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_copy(const DBusString \*source, int start, DBusString \*dest, int insert_at)

Like \_dbus_string_move(), but does not delete the section of the source string that's copied to the d...

**Definition** dbus-string.c:1345

\_dbus_string_parse_int64

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_parse_int64(const DBusString \*str, int start, dbus_int64_t \*value_return, int \*end_return)

Parses a dbus_int64_t integer contained in a DBusString.

**Definition** dbus-sysdeps.c:449

\_dbus_string_find_eol

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_find_eol(const DBusString \*str, int start, int \*found, int \*found_len)

Finds end of line ("\r\n" or "\n") in the string, returning TRUE and filling in the byte index where ...

**Definition** dbus-string.c:1689

\_dbus_string_ends_with_c_str

dbus_bool_t \_dbus_string_ends_with_c_str(const DBusString \*a, const char \*c_str)

Returns whether a string ends with the given suffix.

**Definition** dbus-string-util.c:54

\_dbus_string_starts_with_c_str

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_starts_with_c_str(const DBusString \*a, const char \*c_str)

Checks whether a string starts with the given C string.

**Definition** dbus-string.c:2250

\_dbus_string_alloc_space

dbus_bool_t \_dbus_string_alloc_space(DBusString \*str, int extra_bytes)

Preallocate extra_bytes such that a future lengthening of the string by extra_bytes is guaranteed to ...

**Definition** dbus-string.c:944

\_dbus_string_steal_data

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_steal_data(DBusString \*str, char \*\*data_return)

Like \_dbus_string_get_data(), but removes the gotten data from the original string.

**Definition** dbus-string.c:686

\_dbus_string_skip_blank

DBUS_PRIVATE_EXPORT void \_dbus_string_skip_blank(const DBusString \*str, int start, int \*end)

Skips blanks from start, storing the first non-blank in \*end (blank is space or tab).

**Definition** dbus-string.c:1865

\_dbus_string_init_preallocated

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_init_preallocated(DBusString \*str, int allocate_size)

Initializes a string that can be up to the given allocation size before it has to realloc.

**Definition** dbus-string.c:139

\_dbus_string_skip_white_reverse

void \_dbus_string_skip_white_reverse(const DBusString \*str, int end, int \*start)

Skips whitespace from end, storing the start index of the trailing whitespace in \*start.

**Definition** dbus-string.c:1932

\_dbus_string_init_from_string

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_init_from_string(DBusString \*str, const DBusString \*from)

Initializes a string from another string.

**Definition** dbus-string.c:254

\_dbus_string_split_on_byte

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_split_on_byte(DBusString \*source, unsigned char byte, DBusString \*tail)

Looks for the first occurance of a byte, deletes that byte, and moves everything after the byte to th...

**Definition** dbus-string.c:1529

\_dbus_string_find

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_find(const DBusString \*str, int start, const char \*substr, int \*found)

Finds the given substring in the string, returning TRUE and filling in the byte index where the subst...

**Definition** dbus-string.c:1666

\_dbus_string_get_data_len

DBUS_PRIVATE_EXPORT char \* \_dbus_string_get_data_len(DBusString \*str, int start, int len)

Gets a sub-portion of the raw character buffer from the string.

**Definition** dbus-string.c:535

\_dbus_string_validate_utf8

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_validate_utf8(const DBusString \*str, int start, int len)

Checks that the given range of the string is valid UTF-8.

**Definition** dbus-string.c:2678

\_dbus_string_find_blank

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_find_blank(const DBusString \*str, int start, int \*found)

Finds a blank (space or tab) in the string.

**Definition** dbus-string.c:1827

\_dbus_string_init_const_len

DBUS_PRIVATE_EXPORT void \_dbus_string_init_const_len(DBusString \*str, const char \*value, int len)

Initializes a constant string with a length.

**Definition** dbus-string.c:217

\_dbus_string_tolower_ascii

DBUS_PRIVATE_EXPORT void \_dbus_string_tolower_ascii(const DBusString \*str, int start, int len)

Converts the given range of the string to lower case.

**Definition** dbus-string.c:2608

\_dbus_string_append_len

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_append_len(DBusString \*str, const char \*buffer, int len)

Appends block of bytes with the given length to a DBusString.

**Definition** dbus-string.c:1170

\_dbus_string_get_data

DBUS_PRIVATE_EXPORT char \* \_dbus_string_get_data(DBusString \*str)

Gets the raw character buffer from the string.

**Definition** dbus-string.c:496

\_dbus_string_free

DBUS_PRIVATE_EXPORT void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_string_shorten

DBUS_PRIVATE_EXPORT void \_dbus_string_shorten(DBusString \*str, int length_to_remove)

Makes a string shorter by the given number of bytes.

**Definition** dbus-string.c:825

\_dbus_string_delete

DBUS_PRIVATE_EXPORT void \_dbus_string_delete(DBusString \*str, int start, int len)

Deletes a segment of a DBusString with length len starting at start.

**Definition** dbus-string.c:1255

\_dbus_string_copy_data

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_copy_data(const DBusString \*str, char \*\*data_return)

Copies the data from the string into a char\*.

**Definition** dbus-string.c:717

\_dbus_string_parse_uint

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_parse_uint(const DBusString \*str, int start, unsigned long \*value_return, int \*end_return)

Parses an unsigned integer contained in a DBusString.

**Definition** dbus-sysdeps.c:410

\_dbus_string_equal_c_str

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_equal_c_str(const DBusString \*a, const char \*c_str)

Checks whether a string is equal to a C string.

**Definition** dbus-string.c:2214

\_dbus_string_skip_white

DBUS_PRIVATE_EXPORT void \_dbus_string_skip_white(const DBusString \*str, int start, int \*end)

Skips whitespace from start, storing the first non-whitespace in \*end.

**Definition** dbus-string.c:1899

\_dbus_string_find_byte_backward

dbus_bool_t \_dbus_string_find_byte_backward(const DBusString \*str, int start, unsigned char byte, int \*found)

Find the given byte scanning backward from the given start.

**Definition** dbus-string-util.c:98

\_dbus_string_pop_line

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_pop_line(DBusString \*source, DBusString \*dest)

Assigns a newline-terminated or \r\n-terminated line from the front of the string to the given dest s...

**Definition** dbus-string.c:1971

\_dbus_string_append_printf_valist

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_append_printf_valist(DBusString \*str, const char \*format, va_list args)

Appends a printf-style formatted string to the DBusString.

**Definition** dbus-string.c:1105

\_dbus_string_lengthen

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_lengthen(DBusString \*str, int additional_length)

Makes a string longer by the given number of bytes.

**Definition** dbus-string.c:805

\_dbus_string_zero

void \_dbus_string_zero(DBusString \*str)

Clears all allocated bytes in the string to zero.

**Definition** dbus-string.c:2808

\_dbus_string_parse_int

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_parse_int(const DBusString \*str, int start, long \*value_return, int \*end_return)

Parses an integer contained in a DBusString.

**Definition** dbus-sysdeps.c:371

\_dbus_string_toupper_ascii

DBUS_PRIVATE_EXPORT void \_dbus_string_toupper_ascii(const DBusString \*str, int start, int len)

Converts the given range of the string to upper case.

**Definition** dbus-string.c:2639

\_dbus_string_insert_bytes

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_insert_bytes(DBusString \*str, int i, int n_bytes, unsigned char byte)

Inserts a number of bytes of a given value at the given position.

**Definition** dbus-string.c:629

\_dbus_string_validate_ascii

dbus_bool_t \_dbus_string_validate_ascii(const DBusString \*str, int start, int len)

Checks that the given range of the string is valid ASCII with no nul bytes.

**Definition** dbus-string.c:2573

\_dbus_string_get_length

DBUS_PRIVATE_EXPORT int \_dbus_string_get_length(const DBusString \*str)

Gets the length of a string (not including nul termination).

**Definition** dbus-string.c:784

\_dbus_string_append_byte

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_append_byte(DBusString \*str, unsigned char byte)

Appends a single byte to the string, returning FALSE if not enough memory.

**Definition** dbus-string.c:1190

\_dbus_string_chop_white

DBUS_PRIVATE_EXPORT void \_dbus_string_chop_white(DBusString \*str)

Deletes leading and trailing whitespace.

**Definition** dbus-string.c:2051

\_dbus_string_starts_with_words_c_str

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_starts_with_words_c_str(const DBusString \*a, const char \*c_str, char word_separator)

Checks whether a string starts with the given C string, after which it ends or is separated from the ...

**Definition** dbus-string.c:2288

\_dbus_string_hex_encode

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_hex_encode(const DBusString \*source, int start, DBusString \*dest, int insert_at)

Encodes a string in hex, the way MD5 and SHA-1 are usually encoded.

**Definition** dbus-string.c:2382

\_dbus_string_append_printf

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_append_printf(DBusString \*str, const char \*format,...)

Appends a printf-style formatted string to the DBusString.

**Definition** dbus-string.c:1147

\_dbus_string_insert_byte

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_insert_byte(DBusString \*str, int i, unsigned char byte)

Inserts a single byte at the given position.

**Definition** dbus-string.c:659

\_dbus_string_get_const_data_len

DBUS_PRIVATE_EXPORT const char \* \_dbus_string_get_const_data_len(const DBusString \*str, int start, int len)

const version of \_dbus_string_get_data_len().

**Definition** dbus-string.c:559

\_dbus_string_set_byte

DBUS_PRIVATE_EXPORT void \_dbus_string_set_byte(DBusString \*str, int i, unsigned char byte)

Sets the value of the byte at the given position.

**Definition** dbus-string.c:583

\_dbus_string_move_len

dbus_bool_t \_dbus_string_move_len(DBusString \*source, int start, int len, DBusString \*dest, int insert_at)

Like \_dbus_string_move(), but can move a segment from the middle of the source string.

**Definition** dbus-string.c:1370

\_dbus_string_get_const_data

DBUS_PRIVATE_EXPORT const char \* \_dbus_string_get_const_data(const DBusString \*str)

Gets the raw character buffer from a const string.

**Definition** dbus-string.c:513

\_dbus_string_get_allocated_size

DBUS_PRIVATE_EXPORT int \_dbus_string_get_allocated_size(const DBusString \*str)

Returns the allocated size of the string.

**Definition** dbus-string.c:476

\_dbus_string_get_byte

DBUS_PRIVATE_EXPORT unsigned char \_dbus_string_get_byte(const DBusString \*str, int start)

Gets the byte at the given position.

**Definition** dbus-string.c:607

\_dbus_string_copy_to_buffer_with_nul

DBUS_PRIVATE_EXPORT void \_dbus_string_copy_to_buffer_with_nul(const DBusString \*str, char \*buffer, int avail_len)

Copies the contents of a DBusString into a different buffer.

**Definition** dbus-string.c:764

\_dbus_string_compact

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_compact(DBusString \*str, int max_waste)

Compacts the string to avoid wasted memory.

**Definition** dbus-string.c:420

\_dbus_string_equal_len

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_equal_len(const DBusString \*a, const DBusString \*b, int len)

Tests two DBusString for equality up to the given length.

**Definition** dbus-string.c:2118

\_dbus_string_move

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_move(DBusString \*source, int start, DBusString \*dest, int insert_at)

Moves the end of one string into another string.

**Definition** dbus-string.c:1321

\_dbus_string_equal

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_equal(const DBusString \*a, const DBusString \*b)

Tests two DBusString for equality.

**Definition** dbus-string.c:2075

\_dbus_string_insert_4_aligned

dbus_bool_t \_dbus_string_insert_4_aligned(DBusString \*str, int insert_at, const unsigned char octets\[4\])

Inserts 4 bytes aligned on a 4 byte boundary with any alignment padding initialized to 0.

**Definition** dbus-string.c:1029

\_dbus_string_insert_2_aligned

dbus_bool_t \_dbus_string_insert_2_aligned(DBusString \*str, int insert_at, const unsigned char octets\[2\])

Inserts 2 bytes aligned on a 2 byte boundary with any alignment padding initialized to 0.

**Definition** dbus-string.c:1005

\_dbus_string_append_byte_as_hex

dbus_bool_t \_dbus_string_append_byte_as_hex(DBusString \*str, unsigned char byte)

Appends a two-character hex digit to a string, where the hex digit has the value of the given byte.

**Definition** dbus-string.c:2313

\_dbus_string_align_length

dbus_bool_t \_dbus_string_align_length(DBusString \*str, int alignment)

Align the length of a string to a specific alignment (typically 4 or 8) by appending nul bytes to the...

**Definition** dbus-string.c:928

\_dbus_string_find_to

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_find_to(const DBusString \*str, int start, int end, const char \*substr, int \*found)

Finds the given substring in the string, up to a certain position, returning TRUE and filling in the ...

**Definition** dbus-string.c:1759

\_dbus_string_copy_len

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_copy_len(const DBusString \*source, int start, int len, DBusString \*dest, int insert_at)

Like \_dbus_string_copy(), but can copy a segment from the middle of the source string.

**Definition** dbus-string.c:1437

\_dbus_string_copy_to_buffer

void \_dbus_string_copy_to_buffer(const DBusString \*str, char \*buffer, int len)

Copies the contents of a DBusString into a different buffer.

**Definition** dbus-string.c:742

\_dbus_string_replace_len

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_replace_len(const DBusString \*source, int start, int len, DBusString \*dest, int replace_at, int replace_len)

Replaces a segment of dest string with a segment of source string.

**Definition** dbus-string.c:1466

DBusString

**Definition** dbus-string.h:47

DBusString::dummy1

const void \* dummy1

placeholder

**Definition** dbus-string.h:51

DBusString::dummy_bits

unsigned int dummy_bits

placeholder

**Definition** dbus-string.h:58

DBusString::dummy_bit3

unsigned int dummy_bit3

placeholder

**Definition** dbus-string.h:57

DBusString::dummy3

int dummy3

placeholder

**Definition** dbus-string.h:54

DBusString::dummy_bit1

unsigned int dummy_bit1

placeholder

**Definition** dbus-string.h:55

DBusString::dummy_bit2

unsigned int dummy_bit2

placeholder

**Definition** dbus-string.h:56

DBusString::dummy2

int dummy2

placeholder

**Definition** dbus-string.h:53
