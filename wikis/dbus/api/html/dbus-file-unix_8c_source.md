dbus-file-unix.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-file-unix.c unix related file implementation (internal to D-Bus implementation)

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

28

29\#include "dbus-protocol.h"

30\#include "dbus-errors.h"

31\#include "dbus-file.h"

32\#include "dbus-internals.h"

33\#include "dbus-sysdeps.h"

34\#include "dbus-sysdeps-unix.h"

35

36\#ifdef HAVE_LINUX_MAGIC_H

37\#include \<linux/magic.h\>

38\#endif

39\#include \<sys/stat.h\>

40\#ifdef HAVE_SYS_VFS_H

41\#include \<sys/vfs.h\>

42\#endif

43\#include \<stdio.h\>

44\#include \<fcntl.h\>

45\#include \<unistd.h\>

46\#include \<errno.h\>

47

48\#ifndef O_BINARY

49\#define O_BINARY 0

50\#endif

51

62dbus_bool_t

63\_dbus_file_get_contents (DBusString \*str,

64 const DBusString \*filename,

65 DBusError \*error)

66{

67 int fd;

68 struct stat sb;

69\#if defined(HAVE_FSTATFS) && defined(PROC_SUPER_MAGIC)

70 struct statfs sfs;

71\#endif

72 int orig_len;

73 int total;

74 int file_size;

75 const char \*filename_c;

76 dbus_bool_t is_procfs = FALSE;

77

78 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

79

80 filename_c = \_dbus_string_get_const_data (filename);

81

82 /\* O_BINARY useful on Cygwin \*/

83 fd = open (filename_c, O_RDONLY \| O_BINARY);

84 if (fd \< 0)

85 {

86 dbus_set_error (error, \_dbus_error_from_errno (errno),

87 "Failed to open \\%s\\: %s",

88 filename_c,

89 \_dbus_strerror (errno));

90 return FALSE;

91 }

92

93 \_dbus_verbose ("file fd %d opened\n", fd);

94

95 if (fstat (fd, &sb) \< 0)

96 {

97 dbus_set_error (error, \_dbus_error_from_errno (errno),

98 "Failed to stat \\%s\\: %s",

99 filename_c,

100 \_dbus_strerror (errno));

101

102 \_dbus_verbose ("fstat() failed: %s",

103 \_dbus_strerror (errno));

104

105 \_dbus_close (fd, NULL);

106

107 return FALSE;

108 }

109

110 if (sb.st_size \> \_DBUS_ONE_MEGABYTE)

111 {

112 dbus_set_error (error, DBUS_ERROR_FAILED,

113 "File size %lu of \\%s\\ is too large.",

114 (unsigned long) sb.st_size, filename_c);

115 \_dbus_close (fd, NULL);

116 return FALSE;

117 }

118

119 /\* procfs has different semantics - most files are 0 size,

120 \* we can do only one read, and at most we can read 4M.

121 \*/

122\#if defined(HAVE_FSTATFS) && defined(PROC_SUPER_MAGIC)

123 if (sb.st_size == 0)

124 {

125 if (fstatfs(fd, &sfs) \< 0)

126 {

127 dbus_set_error (error, \_dbus_error_from_errno (errno),

128 "Failed to stat \\%s\\: %s",

129 filename_c,

130 \_dbus_strerror (errno));

131

132 \_dbus_verbose ("fstatvfs() failed: %s",

133 \_dbus_strerror (errno));

134

135 \_dbus_close (fd, NULL);

136

137 return FALSE;

138 }

139 if (sfs.f_type == PROC_SUPER_MAGIC)

140 is_procfs = TRUE;

141 }

142\#endif

143

144 if (is_procfs)

145 file_size = \_DBUS_ONE_MEGABYTE;

146 else

147 file_size = sb.st_size;

148

149 total = 0;

150 orig_len = \_dbus_string_get_length (str);

151 if (file_size \> 0 && S_ISREG (sb.st_mode))

152 {

153 int bytes_read;

154

155 do

156 {

157 bytes_read = \_dbus_read (fd, str,

158 file_size - total);

159 if (bytes_read \<= 0)

160 {

161 dbus_set_error (error, \_dbus_error_from_errno (errno),

162 "Error reading \\%s\\: %s",

163 filename_c,

164 \_dbus_strerror (errno));

165

166 \_dbus_verbose ("read() failed: %s",

167 \_dbus_strerror (errno));

168

169 \_dbus_close (fd, NULL);

170 \_dbus_string_set_length (str, orig_len);

171 return FALSE;

172 }

173 else

174 total += bytes_read;

175 }

176 while (total \< file_size && !is_procfs);

177

178 \_dbus_close (fd, NULL);

179 return TRUE;

180 }

181 else if (file_size != 0)

182 {

183 \_dbus_verbose ("Can only open regular files at the moment.\n");

184 dbus_set_error (error, DBUS_ERROR_FAILED,

185 "\\%s\\ is not a regular file",

186 filename_c);

187 \_dbus_close (fd, NULL);

188 return FALSE;

189 }

190 else

191 {

192 \_dbus_close (fd, NULL);

193 return TRUE;

194 }

195}

196

207dbus_bool_t

208\_dbus_string_save_to_file (const DBusString \*str,

209 const DBusString \*filename,

210 dbus_bool_t world_readable,

211 DBusError \*error)

212{

213 int fd;

214 int bytes_to_write;

215 const char \*filename_c;

216 DBusString tmp_filename;

217 const char \*tmp_filename_c;

218 int total;

219 dbus_bool_t need_unlink;

220 dbus_bool_t retval;

221

222 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

223

224 fd = -1;

225 retval = FALSE;

226 need_unlink = FALSE;

227

228 if (!\_dbus_string_init (&tmp_filename))

229 {

230 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

231 return FALSE;

232 }

233

234 if (!\_dbus_string_copy (filename, 0, &tmp_filename, 0))

235 {

236 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

237 \_dbus_string_free (&tmp_filename);

238 return FALSE;

239 }

240

241 if (!\_dbus_string_append (&tmp_filename, "."))

242 {

243 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

244 \_dbus_string_free (&tmp_filename);

245 return FALSE;

246 }

247

248\#define N_TMP_FILENAME_RANDOM_BYTES 8

249 if (!\_dbus_generate_random_ascii (&tmp_filename, N_TMP_FILENAME_RANDOM_BYTES,

250 error))

251 {

252 \_dbus_string_free (&tmp_filename);

253 return FALSE;

254 }

255

256 filename_c = \_dbus_string_get_const_data (filename);

257 tmp_filename_c = \_dbus_string_get_const_data (&tmp_filename);

258

259 fd = open (tmp_filename_c, O_WRONLY \| O_BINARY \| O_EXCL \| O_CREAT,

260 world_readable ? 0644 : 0600);

261 if (fd \< 0)

262 {

263 dbus_set_error (error, \_dbus_error_from_errno (errno),

264 "Could not create %s: %s", tmp_filename_c,

265 \_dbus_strerror (errno));

266 goto out;

267 }

268 if (world_readable)

269 {

270 /\* Ensure the file is world readable even in the presence of

271 \* possibly restrictive umasks;

272 \* see http://lists.freedesktop.org/archives/dbus/2010-September/013367.html

273 \*/

274 if (fchmod (fd, 0644) \< 0)

275 {

276 dbus_set_error (error, \_dbus_error_from_errno (errno),

277 "Could not chmod %s: %s", tmp_filename_c,

278 \_dbus_strerror (errno));

279 goto out;

280 }

281 }

282

283 \_dbus_verbose ("tmp file fd %d opened\n", fd);

284

285 need_unlink = TRUE;

286

287 total = 0;

288 bytes_to_write = \_dbus_string_get_length (str);

289

290 while (total \< bytes_to_write)

291 {

292 int bytes_written;

293

294 bytes_written = \_dbus_write (fd, str, total,

295 bytes_to_write - total);

296

297 if (bytes_written \<= 0)

298 {

299 dbus_set_error (error, \_dbus_error_from_errno (errno),

300 "Could not write to %s: %s", tmp_filename_c,

301 \_dbus_strerror (errno));

302

303 goto out;

304 }

305

306 total += bytes_written;

307 }

308

309 if (fsync(fd))

310 {

311 dbus_set_error (error, \_dbus_error_from_errno (errno),

312 "Could not synchronize file %s: %s",

313 tmp_filename_c, \_dbus_strerror (errno));

314

315 goto out;

316 }

317

318 if (!\_dbus_close (fd, NULL))

319 {

320 dbus_set_error (error, \_dbus_error_from_errno (errno),

321 "Could not close file %s: %s",

322 tmp_filename_c, \_dbus_strerror (errno));

323

324 goto out;

325 }

326

327 fd = -1;

328

329 if (rename (tmp_filename_c, filename_c) \< 0)

330 {

331 dbus_set_error (error, \_dbus_error_from_errno (errno),

332 "Could not rename %s to %s: %s",

333 tmp_filename_c, filename_c,

334 \_dbus_strerror (errno));

335

336 goto out;

337 }

338

339 need_unlink = FALSE;

340

341 retval = TRUE;

342

343 out:

344 /\* close first, then unlink, to prevent ".nfs34234235" garbage

345 \* files

346 \*/

347

348 if (fd \>= 0)

349 \_dbus_close (fd, NULL);

350

351 if (need_unlink && unlink (tmp_filename_c) \< 0)

352 \_dbus_verbose ("Failed to unlink temp file %s: %s\n",

353 tmp_filename_c, \_dbus_strerror (errno));

354

355 \_dbus_string_free (&tmp_filename);

356

357 \_DBUS_ASSERT_ERROR_XOR_BOOL (error, retval);

358 return retval;

359}

360

367dbus_bool_t

368\_dbus_make_file_world_readable(const DBusString \*filename,

369 DBusError \*error)

370{

371 const char \*filename_c;

372

373 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

374

375 filename_c = \_dbus_string_get_const_data (filename);

376 if (chmod (filename_c, 0644) == -1)

377 {

378 dbus_set_error (error,

379 DBUS_ERROR_FAILED,

380 "Could not change permissions of file %s: %s\n",

381 filename_c,

382 \_dbus_strerror (errno));

383 return FALSE;

384 }

385 return TRUE;

386}

387

394dbus_bool_t

395\_dbus_create_file_exclusively (const DBusString \*filename,

396 DBusError \*error)

397{

398 int fd;

399 const char \*filename_c;

400

401 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

402

403 filename_c = \_dbus_string_get_const_data (filename);

404

405 fd = open (filename_c, O_WRONLY \| O_BINARY \| O_EXCL \| O_CREAT,

406 0600);

407 if (fd \< 0)

408 {

409 dbus_set_error (error,

410 DBUS_ERROR_FAILED,

411 "Could not create file %s: %s\n",

412 filename_c,

413 \_dbus_strerror (errno));

414 return FALSE;

415 }

416

417 \_dbus_verbose ("exclusive file fd %d opened\n", fd);

418

419 if (!\_dbus_close (fd, NULL))

420 {

421 dbus_set_error (error,

422 DBUS_ERROR_FAILED,

423 "Could not close file %s: %s\n",

424 filename_c,

425 \_dbus_strerror (errno));

426 return FALSE;

427 }

428

429 return TRUE;

430}

431

440dbus_bool_t

441\_dbus_delete_file (const DBusString \*filename,

442 DBusError \*error)

443{

444 const char \*filename_c;

445

446 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

447

448 filename_c = \_dbus_string_get_const_data (filename);

449

450 if (unlink (filename_c) \< 0)

451 {

452 dbus_set_error (error, DBUS_ERROR_FAILED,

453 "Failed to delete file %s: %s\n",

454 filename_c, \_dbus_strerror (errno));

455 return FALSE;

456 }

457 else

458 return TRUE;

459}

dbus_set_error

void dbus_set_error(DBusError \*error, const char \*name, const char \*format,...)

Assigns an error name and message to a DBusError.

**Definition** dbus-errors.c:356

\_dbus_delete_file

dbus_bool_t \_dbus_delete_file(const DBusString \*filename, DBusError \*error)

Deletes the given file.

**Definition** dbus-file-unix.c:441

\_dbus_create_file_exclusively

dbus_bool_t \_dbus_create_file_exclusively(const DBusString \*filename, DBusError \*error)

Creates the given file, failing if the file already exists.

**Definition** dbus-file-unix.c:395

\_dbus_string_save_to_file

dbus_bool_t \_dbus_string_save_to_file(const DBusString \*str, const DBusString \*filename, dbus_bool_t world_readable, DBusError \*error)

Writes a string out to a file.

**Definition** dbus-file-unix.c:208

\_dbus_make_file_world_readable

dbus_bool_t \_dbus_make_file_world_readable(const DBusString \*filename, DBusError \*error)

Makes the file readable by every user in the system.

**Definition** dbus-file-unix.c:368

\_dbus_file_get_contents

dbus_bool_t \_dbus_file_get_contents(DBusString \*str, const DBusString \*filename, DBusError \*error)

Appends the contents of the given file to the string, returning error code.

**Definition** dbus-file-unix.c:63

\_dbus_error_from_errno

const char \* \_dbus_error_from_errno(int error_number)

Converts a UNIX errno, or Windows errno or WinSock error value into a DBusError name.

**Definition** dbus-sysdeps.c:565

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

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_string_get_length

int \_dbus_string_get_length(const DBusString \*str)

Gets the length of a string (not including nul termination).

**Definition** dbus-string.c:784

\_dbus_string_get_const_data

const char \* \_dbus_string_get_const_data(const DBusString \*str)

Gets the raw character buffer from a const string.

**Definition** dbus-string.c:513

\_dbus_close

dbus_bool_t \_dbus_close(int fd, DBusError \*error)

Closes a file descriptor.

**Definition** dbus-sysdeps-unix.c:3727

\_dbus_write

int \_dbus_write(int fd, const DBusString \*buffer, int start, int len)

Thin wrapper around the write() system call that writes a part of a DBusString and handles EINTR for ...

**Definition** dbus-sysdeps-unix.c:827

\_dbus_read

int \_dbus_read(int fd, DBusString \*buffer, int count)

Thin wrapper around the read() system call that appends the data it reads to the DBusString buffer.

**Definition** dbus-sysdeps-unix.c:767

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusString

**Definition** dbus-string.h:47
