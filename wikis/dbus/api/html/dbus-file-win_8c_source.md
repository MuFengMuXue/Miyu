dbus-file-win.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-file-win.c windows related file implementation (internal to D-Bus implementation)

3 \*

4 \* Copyright (C) 2002, 2003, 2006 Red Hat, Inc.

5 \* Copyright (C) 2003 CodeFactory AB

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

28\#include "dbus-protocol.h"

29\#include "dbus-string.h"

30\#include "dbus-internals.h"

31\#include "dbus-sysdeps-win.h"

32\#include "dbus-pipe.h"

33

34\#include \<windows.h\>

35

36

48static int

49\_dbus_file_read (HANDLE hnd,

50 DBusString \*buffer,

51 int count,

52 DBusError \*error)

53{

54 BOOL result;

55 DWORD bytes_read;

56 int start;

57 char \*data;

58

59 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

60

61 \_dbus_assert (count \>= 0);

62

63 start = \_dbus_string_get_length (buffer);

64

65 if (!\_dbus_string_lengthen (buffer, count))

66 {

67 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

68 return -1;

69 }

70

71 data = \_dbus_string_get_data_len (buffer, start, count);

72

73 result = ReadFile (hnd, data, count, &bytes_read, NULL);

74 if (result == 0)

75 {

76 char \*emsg = \_dbus_win_error_string (GetLastError ());

77 dbus_set_error (error, \_dbus_win_error_from_last_error (),

78 "Failed to read from %p: %s", hnd, emsg);

79 \_dbus_win_free_error_string (emsg);

80 return -1;

81 }

82

83 if (bytes_read)

84 {

85 /\* put length back (doesn't actually realloc) \*/

86 \_dbus_string_set_length (buffer, start + bytes_read);

87

88\#if 0

89 if (bytes_read \> 0)

90 \_dbus_verbose_bytes_of_string (buffer, start, bytes_read);

91\#endif

92 }

93

94 return bytes_read;

95}

96

97

108dbus_bool_t

109\_dbus_file_get_contents (DBusString \*str,

110 const DBusString \*filename,

111 DBusError \*error)

112{

113 HANDLE hnd;

114 DWORD fsize;

115 DWORD fsize_hi;

116 int orig_len;

117 unsigned int total;

118 const char \*filename_c;

119

120 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

121

122 filename_c = \_dbus_string_get_const_data (filename);

123

124 hnd = CreateFileA (filename_c, GENERIC_READ,

125 FILE_SHARE_READ \| FILE_SHARE_WRITE,

126 NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);

127 if (hnd == INVALID_HANDLE_VALUE)

128 {

129 char \*emsg = \_dbus_win_error_string (GetLastError ());

130 dbus_set_error (error, \_dbus_win_error_from_last_error (),

131 "Failed to open \\%s\\: %s", filename_c, emsg);

132 \_dbus_win_free_error_string (emsg);

133 return FALSE;

134 }

135

136 \_dbus_verbose ("file %s hnd %p opened\n", filename_c, hnd);

137

138 fsize = GetFileSize (hnd, &fsize_hi);

139 if (fsize == 0xFFFFFFFF && GetLastError() != NO_ERROR)

140 {

141 char \*emsg = \_dbus_win_error_string (GetLastError ());

142 dbus_set_error (error, \_dbus_win_error_from_last_error (),

143 "Failed to get file size for \\%s\\: %s",

144 filename_c, emsg);

145 \_dbus_win_free_error_string (emsg);

146

147 \_dbus_verbose ("GetFileSize() failed: %s", emsg);

148

149 CloseHandle (hnd);

150

151 return FALSE;

152 }

153

154 if (fsize_hi != 0 \|\| fsize \> \_DBUS_ONE_MEGABYTE)

155 {

156 dbus_set_error (error, DBUS_ERROR_FAILED,

157 "File size %lu/%lu of \\%s\\ is too large.",

158 (unsigned long) fsize_hi,

159 (unsigned long) fsize, filename_c);

160 CloseHandle (hnd);

161 return FALSE;

162 }

163

164 total = 0;

165 orig_len = \_dbus_string_get_length (str);

166 if (fsize \> 0)

167 {

168 int bytes_read;

169

170 while (total \< fsize)

171 {

172 bytes_read = \_dbus_file_read (hnd, str, fsize - total, error);

173 if (bytes_read \<= 0)

174 {

175 if (bytes_read == 0)

176 {

177 dbus_set_error (error, DBUS_ERROR_FAILED,

178 "Premature EOF reading \\%s\\",

179 filename_c);

180 }

181 else

182 \_DBUS_ASSERT_ERROR_IS_SET (error);

183

184 CloseHandle (hnd);

185 \_dbus_string_set_length (str, orig_len);

186 return FALSE;

187 }

188 else

189 total += bytes_read;

190 }

191

192 CloseHandle (hnd);

193 return TRUE;

194 }

195 else

196 {

197 CloseHandle (hnd);

198 return TRUE;

199 }

200}

201

202

213dbus_bool_t

214\_dbus_string_save_to_file (const DBusString \*str,

215 const DBusString \*filename,

216 dbus_bool_t world_readable,

217 DBusError \*error)

218{

219 HANDLE hnd;

220 int bytes_to_write;

221 const char \*filename_c;

222 DBusString tmp_filename;

223 const char \*tmp_filename_c;

224 int total;

225 const char \*str_c;

226 dbus_bool_t need_unlink;

227 dbus_bool_t retval;

228

229 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

230

231 hnd = INVALID_HANDLE_VALUE;

232 retval = FALSE;

233 need_unlink = FALSE;

234

235 if (!\_dbus_string_init (&tmp_filename))

236 {

237 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

238 return FALSE;

239 }

240

241 if (!\_dbus_string_copy (filename, 0, &tmp_filename, 0))

242 {

243 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

244 \_dbus_string_free (&tmp_filename);

245 return FALSE;

246 }

247

248 if (!\_dbus_string_append (&tmp_filename, "."))

249 {

250 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

251 \_dbus_string_free (&tmp_filename);

252 return FALSE;

253 }

254

255\#define N_TMP_FILENAME_RANDOM_BYTES 8

256 if (!\_dbus_generate_random_ascii (&tmp_filename, N_TMP_FILENAME_RANDOM_BYTES,

257 error))

258 {

259 \_dbus_string_free (&tmp_filename);

260 return FALSE;

261 }

262

263 filename_c = \_dbus_string_get_const_data (filename);

264 tmp_filename_c = \_dbus_string_get_const_data (&tmp_filename);

265

266 /\* TODO - support world-readable in an atomic fashion \*/

267 hnd = CreateFileA (tmp_filename_c, GENERIC_WRITE,

268 FILE_SHARE_READ \| FILE_SHARE_WRITE,

269 NULL, CREATE_NEW, FILE_ATTRIBUTE_NORMAL,

270 INVALID_HANDLE_VALUE);

271 if (hnd == INVALID_HANDLE_VALUE)

272 {

273 char \*emsg = \_dbus_win_error_string (GetLastError ());

274 dbus_set_error (error, \_dbus_win_error_from_last_error (),

275 "Could not create \\%s\\: %s", filename_c, emsg);

276 \_dbus_win_free_error_string (emsg);

277 goto out;

278 }

279 if (world_readable)

280 {

281 if (! \_dbus_make_file_world_readable (&tmp_filename, error))

282 goto out;

283 }

284

285 \_dbus_verbose ("tmp file %s hnd %p opened\n", tmp_filename_c, hnd);

286

287 need_unlink = TRUE;

288

289 total = 0;

290 bytes_to_write = \_dbus_string_get_length (str);

291 str_c = \_dbus_string_get_const_data (str);

292

293 while (total \< bytes_to_write)

294 {

295 DWORD bytes_written;

296 BOOL res;

297

298 res = WriteFile (hnd, str_c + total, bytes_to_write - total,

299 &bytes_written, NULL);

300

301 if (res == 0 \|\| bytes_written \<= 0)

302 {

303 char \*emsg = \_dbus_win_error_string (GetLastError ());

304 dbus_set_error (error, \_dbus_win_error_from_last_error (),

305 "Could not write to %s: %s", tmp_filename_c, emsg);

306 \_dbus_win_free_error_string (emsg);

307 goto out;

308 }

309

310 total += bytes_written;

311 }

312

313 if (CloseHandle (hnd) == 0)

314 {

315 char \*emsg = \_dbus_win_error_string (GetLastError ());

316 dbus_set_error (error, \_dbus_win_error_from_last_error (),

317 "Could not close file %s: %s", tmp_filename_c, emsg);

318 \_dbus_win_free_error_string (emsg);

319 goto out;

320 }

321

322 hnd = INVALID_HANDLE_VALUE;

323

324 /\* Unlike rename(), MoveFileEx() can replace existing files \*/

325 if (!MoveFileExA (tmp_filename_c, filename_c, MOVEFILE_REPLACE_EXISTING))

326 {

327 char \*emsg = \_dbus_win_error_string (GetLastError ());

328 dbus_set_error (error, \_dbus_win_error_from_last_error (),

329 "Could not rename %s to %s: %s",

330 tmp_filename_c, filename_c, emsg);

331 \_dbus_win_free_error_string (emsg);

332

333 goto out;

334 }

335

336 need_unlink = FALSE;

337

338 retval = TRUE;

339

340 out:

341 /\* close first, then unlink \*/

342

343 if (hnd != INVALID_HANDLE_VALUE)

344 CloseHandle (hnd);

345

346 if (need_unlink && DeleteFileA (tmp_filename_c) == 0)

347 {

348 char \*emsg = \_dbus_win_error_string (GetLastError ());

349 \_dbus_verbose ("Failed to unlink temp file %s: %s", tmp_filename_c,

350 emsg);

351 \_dbus_win_free_error_string (emsg);

352 }

353

354 \_dbus_string_free (&tmp_filename);

355

356 if (!retval)

357 \_DBUS_ASSERT_ERROR_IS_SET (error);

358

359 return retval;

360}

361

362

369dbus_bool_t

370\_dbus_create_file_exclusively (const DBusString \*filename,

371 DBusError \*error)

372{

373 HANDLE hnd;

374 const char \*filename_c;

375

376 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

377

378 filename_c = \_dbus_string_get_const_data (filename);

379

380 hnd = CreateFileA (filename_c, GENERIC_WRITE,

381 FILE_SHARE_READ \| FILE_SHARE_WRITE,

382 NULL, CREATE_NEW, FILE_ATTRIBUTE_NORMAL,

383 INVALID_HANDLE_VALUE);

384 if (hnd == INVALID_HANDLE_VALUE)

385 {

386 char \*emsg = \_dbus_win_error_string (GetLastError ());

387 dbus_set_error (error, \_dbus_win_error_from_last_error (),

388 "Could not create file %s: %s",

389 filename_c, emsg);

390 \_dbus_win_free_error_string (emsg);

391 return FALSE;

392 }

393

394 \_dbus_verbose ("exclusive file %s hnd %p opened\n", filename_c, hnd);

395

396 if (CloseHandle (hnd) == 0)

397 {

398 char \*emsg = \_dbus_win_error_string (GetLastError ());

399 dbus_set_error (error, \_dbus_win_error_from_last_error (),

400 "Could not close file %s: %s",

401 filename_c, emsg);

402 \_dbus_win_free_error_string (emsg);

403

404 return FALSE;

405 }

406

407 return TRUE;

408}

dbus_set_error

void dbus_set_error(DBusError \*error, const char \*name, const char \*format,...)

Assigns an error name and message to a DBusError.

**Definition** dbus-errors.c:356

\_dbus_create_file_exclusively

dbus_bool_t \_dbus_create_file_exclusively(const DBusString \*filename, DBusError \*error)

Creates the given file, failing if the file already exists.

**Definition** dbus-file-win.c:370

\_dbus_string_save_to_file

dbus_bool_t \_dbus_string_save_to_file(const DBusString \*str, const DBusString \*filename, dbus_bool_t world_readable, DBusError \*error)

Writes a string out to a file.

**Definition** dbus-file-win.c:214

\_dbus_make_file_world_readable

dbus_bool_t \_dbus_make_file_world_readable(const DBusString \*filename, DBusError \*error)

Makes the file readable by every user in the system.

**Definition** dbus-file-unix.c:368

\_dbus_file_get_contents

dbus_bool_t \_dbus_file_get_contents(DBusString \*str, const DBusString \*filename, DBusError \*error)

Appends the contents of the given file to the string, returning error code.

**Definition** dbus-file-win.c:109

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

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

\_dbus_verbose_bytes_of_string

DBUS_PRIVATE_EXPORT void \_dbus_verbose_bytes_of_string(const DBusString \*str, int start, int len)

Dump the given part of the string to verbose log.

**Definition** dbus-marshal-basic.c:1428

DBUS_ERROR_FAILED

\#define DBUS_ERROR_FAILED

A generic error; "something went wrong" - see the error message for more.

**Definition** dbus-protocol.h:361

DBUS_ERROR_NO_MEMORY

\#define DBUS_ERROR_NO_MEMORY

There was not enough memory to complete an operation.

**Definition** dbus-protocol.h:363

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

\_dbus_string_copy

dbus_bool_t \_dbus_string_copy(const DBusString \*source, int start, DBusString \*dest, int insert_at)

Like \_dbus_string_move(), but does not delete the section of the source string that's copied to the d...

**Definition** dbus-string.c:1345

\_dbus_string_get_data_len

char \* \_dbus_string_get_data_len(DBusString \*str, int start, int len)

Gets a sub-portion of the raw character buffer from the string.

**Definition** dbus-string.c:535

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_string_lengthen

dbus_bool_t \_dbus_string_lengthen(DBusString \*str, int additional_length)

Makes a string longer by the given number of bytes.

**Definition** dbus-string.c:805

\_dbus_string_get_length

int \_dbus_string_get_length(const DBusString \*str)

Gets the length of a string (not including nul termination).

**Definition** dbus-string.c:784

\_dbus_string_get_const_data

const char \* \_dbus_string_get_const_data(const DBusString \*str)

Gets the raw character buffer from a const string.

**Definition** dbus-string.c:513

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusString

**Definition** dbus-string.h:47
