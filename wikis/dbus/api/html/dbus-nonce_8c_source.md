dbus-nonce.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-nonce.c Nonce handling functions used by nonce-tcp (internal to D-Bus implementation)

3 \*

4 \* Copyright (C) 2009 Klaralvdalens Datakonsult AB, a KDAB Group company, info@kdab.net

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

22 \* Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

23 \*

24 \*/

25

26\#include \<config.h\>

27// major sections of this file are modified code from libassuan, (C) FSF

28\#include "dbus-nonce.h"

29\#include "dbus-internals.h"

30\#include "dbus-protocol.h"

31\#include "dbus-sysdeps.h"

32

33\#include \<stdio.h\>

34

35struct DBusNonceFile

36{

37 DBusString path;

38 DBusString dir;

39};

40

41static dbus_bool_t

42do_check_nonce (DBusSocket fd, const DBusString \*nonce, DBusError \*error)

43{

44 DBusString buffer;

45 DBusString p;

46 size_t nleft;

47 dbus_bool_t result;

48 int n;

49

50 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

51

52 nleft = 16;

53

54 /\* This is a trick to make it safe to call \_dbus_string_free on these

55 \* strings during error unwinding, even if allocating memory for them

56 \* fails. A constant DBusString is considered to be valid to "free",

57 \* even though there is nothing to free (of course the free operation

58 \* is trivial, because it does not own its own buffer); but

59 \* unlike a mutable DBusString, initializing a constant DBusString

60 \* cannot fail.

61 \*

62 \* We must successfully re-initialize the strings to be mutable before

63 \* writing to them, of course.

64 \*/

65 \_dbus_string_init_const (&buffer, "");

66 \_dbus_string_init_const (&p, "");

67

68 if ( !\_dbus_string_init (&buffer)

69 \|\| !\_dbus_string_init (&p) ) {

70 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

71 \_dbus_string_free (&p);

72 \_dbus_string_free (&buffer);

73 return FALSE;

74 }

75

76 while (nleft)

77 {

78 int saved_errno;

79

80 n = \_dbus_read_socket (fd, &p, nleft);

81 saved_errno = \_dbus_save_socket_errno ();

82

83 if (n == -1 && \_dbus_get_is_errno_eintr (saved_errno))

84 ;

85 else if (n == -1 && \_dbus_get_is_errno_eagain_or_ewouldblock (saved_errno))

86 \_dbus_sleep_milliseconds (100);

87 else if (n==-1)

88 {

89 dbus_set_error (error, DBUS_ERROR_IO_ERROR, "Could not read nonce from socket (fd=%" DBUS_SOCKET_FORMAT ")", \_dbus_socket_printable (fd));

90 \_dbus_string_free (&p);

91 \_dbus_string_free (&buffer);

92 return FALSE;

93 }

94 else if (!n)

95 {

96 \_dbus_string_free (&p);

97 \_dbus_string_free (&buffer);

98 dbus_set_error (error, DBUS_ERROR_IO_ERROR, "Could not read nonce from socket (fd=%" DBUS_SOCKET_FORMAT ")", \_dbus_socket_printable (fd));

99 return FALSE;

100 }

101 else

102 {

103 if (!\_dbus_string_append_len (&buffer, \_dbus_string_get_const_data (&p), n))

104 {

105 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

106 \_dbus_string_free (&p);

107 \_dbus_string_free (&buffer);

108 return FALSE;

109 }

110 nleft -= n;

111 }

112 }

113

114 result = \_dbus_string_equal_len (&buffer, nonce, 16);

115 if (!result)

116 dbus_set_error (error, DBUS_ERROR_ACCESS_DENIED, "Nonces do not match, access denied (fd=%" DBUS_SOCKET_FORMAT ")", \_dbus_socket_printable (fd));

117

118 \_dbus_string_free (&p);

119 \_dbus_string_free (&buffer);

120

121 return result;

122}

123

132dbus_bool_t

133\_dbus_read_nonce (const DBusString \*fname, DBusString \*nonce, DBusError\* error)

134{

135 FILE \*fp;

136 char buffer\[17\];

137 size_t nread;

138

139 buffer\[sizeof buffer - 1\] = '\0';

140

141 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

142

143 \_dbus_verbose ("reading nonce from file: %s\n", \_dbus_string_get_const_data (fname));

144

145

146 fp = fopen (\_dbus_string_get_const_data (fname), "rb");

147 if (!fp)

148 {

149 dbus_set_error (error,

150 \_dbus_error_from_system_errno (),

151 "Failed to open %s for read: %s",

152 \_dbus_string_get_const_data (fname),

153 \_dbus_strerror_from_errno ());

154 return FALSE;

155 }

156

157 nread = fread (buffer, 1, sizeof buffer - 1, fp);

158 fclose (fp);

159 if (!nread)

160 {

161 dbus_set_error (error, DBUS_ERROR_FILE_NOT_FOUND, "Could not read nonce from file %s", \_dbus_string_get_const_data (fname));

162 return FALSE;

163 }

164

165 if (!\_dbus_string_append_len (nonce, buffer, sizeof buffer - 1 ))

166 {

167 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

168 return FALSE;

169 }

170 return TRUE;

171}

172

173DBusSocket

174\_dbus_accept_with_noncefile (DBusSocket listen_fd, const DBusNonceFile \*noncefile)

175{

176 DBusSocket fd = \_dbus_socket_get_invalid ();

177 DBusString nonce;

178

179 \_dbus_assert (noncefile != NULL);

180

181 /\* Make it valid to "free" this even if \_dbus_string_init() runs

182 \* out of memory: see comment in do_check_nonce() \*/

183 \_dbus_string_init_const (&nonce, "");

184

185 if (!\_dbus_string_init (&nonce))

186 goto out;

187

188 //PENDING(kdab): set better errors

189 if (\_dbus_read_nonce (\_dbus_noncefile_get_path(noncefile), &nonce, NULL) != TRUE)

190 goto out;

191

192 fd = \_dbus_accept (listen_fd);

193

194 if (!\_dbus_socket_is_valid (fd))

195 goto out;

196

197 if (do_check_nonce(fd, &nonce, NULL) != TRUE) {

198 \_dbus_verbose ("nonce check failed. Closing socket.\n");

199 \_dbus_close_socket (&fd, NULL);

200 goto out;

201 }

202

203out:

204 \_dbus_string_free (&nonce);

205 return fd;

206}

207

208static dbus_bool_t

209generate_and_write_nonce (const DBusString \*filename, DBusError \*error)

210{

211 DBusString nonce;

212 dbus_bool_t ret;

213

214 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

215

216 if (!\_dbus_string_init (&nonce))

217 {

218 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

219 return FALSE;

220 }

221

222 if (!\_dbus_generate_random_bytes (&nonce, 16, error))

223 {

224 \_dbus_string_free (&nonce);

225 return FALSE;

226 }

227

228 ret = \_dbus_string_save_to_file (&nonce, filename, FALSE, error);

229

230 \_dbus_string_free (&nonce);

231

232 return ret;

233}

234

244dbus_bool_t

245\_dbus_send_nonce (DBusSocket fd,

246 const DBusString \*noncefile,

247 DBusError \*error)

248{

249 dbus_bool_t read_result;

250 int send_result;

251 DBusString nonce;

252

253 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

254

255 if (\_dbus_string_get_length (noncefile) == 0)

256 return FALSE;

257

258 if (!\_dbus_string_init (&nonce))

259 {

260 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

261 return FALSE;

262 }

263

264 read_result = \_dbus_read_nonce (noncefile, &nonce, error);

265 if (!read_result)

266 {

267 \_DBUS_ASSERT_ERROR_IS_SET (error);

268 \_dbus_string_free (&nonce);

269 return FALSE;

270 }

271 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

272

273 send_result = \_dbus_write_socket (fd, &nonce, 0, \_dbus_string_get_length (&nonce));

274

275 \_dbus_string_free (&nonce);

276

277 if (send_result == -1)

278 {

279 dbus_set_error (error,

280 \_dbus_error_from_system_errno (),

281 "Failed to send nonce (fd=%" DBUS_SOCKET_FORMAT "): %s",

282 \_dbus_socket_printable (fd),

283 \_dbus_strerror_from_errno ());

284 return FALSE;

285 }

286

287 return TRUE;

288}

289

290static dbus_bool_t

291do_noncefile_create (DBusNonceFile \*\*noncefile_out,

292 DBusError \*error,

293 dbus_bool_t use_subdir)

294{

295 DBusNonceFile \*noncefile = NULL;

296 DBusString randomStr;

297 const char \*tmp;

298

299 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

300

301 \_dbus_assert (noncefile_out != NULL);

302 \_dbus_assert (\*noncefile_out == NULL);

303

304 noncefile = dbus_new0 (DBusNonceFile, 1);

305 if (noncefile == NULL)

306 {

307 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

308 return FALSE;

309 }

310

311 /\* Make it valid to "free" these even if \_dbus_string_init() runs

312 \* out of memory: see comment in do_check_nonce() \*/

313 \_dbus_string_init_const (&randomStr, "");

314 \_dbus_string_init_const (&noncefile-\>dir, "");

315 \_dbus_string_init_const (&noncefile-\>path, "");

316

317 if (!\_dbus_string_init (&randomStr))

318 {

319 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

320 goto on_error;

321 }

322

323 if (!\_dbus_generate_random_ascii (&randomStr, 8, error))

324 {

325 goto on_error;

326 }

327

328 tmp = \_dbus_get_tmpdir ();

329

330 if (!\_dbus_string_init (&noncefile-\>dir)

331 \|\| tmp == NULL

332 \|\| !\_dbus_string_append (&noncefile-\>dir, tmp))

333 {

334 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

335 goto on_error;

336 }

337 if (use_subdir)

338 {

339 if (!\_dbus_string_append (&noncefile-\>dir, "/dbus_nonce-")

340 \|\| !\_dbus_string_append (&noncefile-\>dir, \_dbus_string_get_const_data (&randomStr)) )

341 {

342 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

343 goto on_error;

344 }

345 if (!\_dbus_string_init (&noncefile-\>path)

346 \|\| !\_dbus_string_copy (&noncefile-\>dir, 0, &noncefile-\>path, 0)

347 \|\| !\_dbus_string_append (&noncefile-\>path, "/nonce"))

348 {

349 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

350 goto on_error;

351 }

352 if (!\_dbus_create_directory (&noncefile-\>dir, error))

353 {

354 \_DBUS_ASSERT_ERROR_IS_SET (error);

355 goto on_error;

356 }

357 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

358

359 }

360 else

361 {

362 if (!\_dbus_string_init (&noncefile-\>path)

363 \|\| !\_dbus_string_copy (&noncefile-\>dir, 0, &noncefile-\>path, 0)

364 \|\| !\_dbus_string_append (&noncefile-\>path, "/dbus_nonce-")

365 \|\| !\_dbus_string_append (&noncefile-\>path, \_dbus_string_get_const_data (&randomStr)))

366 {

367 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

368 goto on_error;

369 }

370

371 }

372

373 if (!generate_and_write_nonce (&noncefile-\>path, error))

374 {

375 \_DBUS_ASSERT_ERROR_IS_SET (error);

376 if (use_subdir)

377 \_dbus_delete_directory (&noncefile-\>dir, NULL); //we ignore possible errors deleting the dir and return the write error instead

378 goto on_error;

379 }

380 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

381

382 \*noncefile_out = noncefile;

383 \_dbus_string_free (&randomStr);

384

385 return TRUE;

386 on_error:

387 if (use_subdir && \_dbus_string_get_length (&noncefile-\>dir) != 0)

388 \_dbus_delete_directory (&noncefile-\>dir, NULL);

389 \_dbus_string_free (&noncefile-\>dir);

390 \_dbus_string_free (&noncefile-\>path);

391 dbus_free (noncefile);

392 \_dbus_string_free (&randomStr);

393 return FALSE;

394}

395

396\#ifdef DBUS_WIN

404dbus_bool_t

405\_dbus_noncefile_create (DBusNonceFile \*\*noncefile_out,

406 DBusError \*error)

407{

408 return do_noncefile_create (noncefile_out, error, /\*use_subdir=\*/FALSE);

409}

410

421dbus_bool_t

422\_dbus_noncefile_delete (DBusNonceFile \*\*noncefile_location,

423 DBusError \*error)

424{

425 DBusNonceFile \*noncefile;

426

427 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

428 \_dbus_assert (noncefile_location != NULL);

429

430 noncefile = \*noncefile_location;

431 \*noncefile_location = NULL;

432

433 if (noncefile == NULL)

434 {

435 /\* Nothing to do \*/

436 return TRUE;

437 }

438

439 \_dbus_delete_file (&noncefile-\>path, error);

440 \_dbus_string_free (&noncefile-\>dir);

441 \_dbus_string_free (&noncefile-\>path);

442 dbus_free (noncefile);

443 return TRUE;

444}

445

446\#else

455dbus_bool_t

456\_dbus_noncefile_create (DBusNonceFile \*\*noncefile_out,

457 DBusError \*error)

458{

459 return do_noncefile_create (noncefile_out, error, /\*use_subdir=\*/TRUE);

460}

461

472dbus_bool_t

473\_dbus_noncefile_delete (DBusNonceFile \*\*noncefile_location,

474 DBusError \*error)

475{

476 DBusNonceFile \*noncefile;

477

478 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

479 \_dbus_assert (noncefile_location != NULL);

480

481 noncefile = \*noncefile_location;

482 \*noncefile_location = NULL;

483

484 if (noncefile == NULL)

485 {

486 /\* Nothing to do \*/

487 return TRUE;

488 }

489

490 \_dbus_delete_directory (&noncefile-\>dir, error);

491 \_dbus_string_free (&noncefile-\>dir);

492 \_dbus_string_free (&noncefile-\>path);

493 dbus_free (noncefile);

494 return TRUE;

495}

496\#endif

497

498

505const DBusString\*

506\_dbus_noncefile_get_path (const DBusNonceFile \*noncefile)

507{

508 \_dbus_assert (noncefile);

509 return &noncefile-\>path;

510}

511

522dbus_bool_t

523\_dbus_noncefile_check_nonce (DBusSocket fd,

524 const DBusNonceFile \*noncefile,

525 DBusError\* error)

526{

527 return do_check_nonce (fd, \_dbus_noncefile_get_path (noncefile), error);

528}

529

530

dbus_set_error

void dbus_set_error(DBusError \*error, const char \*name, const char \*format,...)

Assigns an error name and message to a DBusError.

**Definition** dbus-errors.c:356

\_dbus_delete_file

dbus_bool_t \_dbus_delete_file(const DBusString \*filename, DBusError \*error)

Deletes the given file.

**Definition** dbus-file-unix.c:441

\_dbus_string_save_to_file

dbus_bool_t \_dbus_string_save_to_file(const DBusString \*str, const DBusString \*filename, dbus_bool_t world_readable, DBusError \*error)

Writes a string out to a file.

**Definition** dbus-file-unix.c:208

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_dbus_generate_random_ascii

dbus_bool_t \_dbus_generate_random_ascii(DBusString \*str, int n_bytes, DBusError \*error)

Generates the given number of random bytes, where the bytes are chosen from the alphanumeric ASCII su...

**Definition** dbus-sysdeps.c:525

\_dbus_error_from_system_errno

const char \* \_dbus_error_from_system_errno(void)

Converts the current system errno value into a DBusError name.

**Definition** dbus-sysdeps.c:657

\_dbus_strerror_from_errno

const char \* \_dbus_strerror_from_errno(void)

Get error message from errno.

**Definition** dbus-sysdeps.c:724

\_dbus_get_is_errno_eintr

dbus_bool_t \_dbus_get_is_errno_eintr(int e)

See if errno is EINTR.

**Definition** dbus-sysdeps.c:690

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

dbus_free

void dbus_free(void \*memory)

Frees a block of memory previously allocated by dbus_malloc() or dbus_malloc0().

**Definition** dbus-memory.c:710

dbus_new0

\#define dbus_new0(type, count)

Safe macro for using dbus_malloc0().

**Definition** dbus-memory.h:60

DBUS_ERROR_IO_ERROR

\#define DBUS_ERROR_IO_ERROR

Something went wrong reading or writing to a socket, for example.

**Definition** dbus-protocol.h:371

DBUS_ERROR_ACCESS_DENIED

\#define DBUS_ERROR_ACCESS_DENIED

Security restrictions don't allow doing what you're trying to do.

**Definition** dbus-protocol.h:379

DBUS_ERROR_NO_MEMORY

\#define DBUS_ERROR_NO_MEMORY

There was not enough memory to complete an operation.

**Definition** dbus-protocol.h:363

DBUS_ERROR_FILE_NOT_FOUND

\#define DBUS_ERROR_FILE_NOT_FOUND

Missing file.

**Definition** dbus-protocol.h:399

\_dbus_string_append

dbus_bool_t \_dbus_string_append(DBusString \*str, const char \*buffer)

Appends a nul-terminated C-style string to a DBusString.

**Definition** dbus-string.c:980

\_dbus_string_init

dbus_bool_t \_dbus_string_init(DBusString \*str)

Initializes a string.

**Definition** dbus-string.c:182

\_dbus_string_init_const

void \_dbus_string_init_const(DBusString \*str, const char \*value)

Initializes a constant string.

**Definition** dbus-string.c:197

\_dbus_string_copy

dbus_bool_t \_dbus_string_copy(const DBusString \*source, int start, DBusString \*dest, int insert_at)

Like \_dbus_string_move(), but does not delete the section of the source string that's copied to the d...

**Definition** dbus-string.c:1345

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

\_dbus_string_get_const_data

const char \* \_dbus_string_get_const_data(const DBusString \*str)

Gets the raw character buffer from a const string.

**Definition** dbus-string.c:513

\_dbus_string_equal_len

dbus_bool_t \_dbus_string_equal_len(const DBusString \*a, const DBusString \*b, int len)

Tests two DBusString for equality up to the given length.

**Definition** dbus-string.c:2118

\_dbus_get_is_errno_eagain_or_ewouldblock

dbus_bool_t \_dbus_get_is_errno_eagain_or_ewouldblock(int e)

See if errno is EAGAIN or EWOULDBLOCK (this has to be done differently for Winsock so is abstracted)

**Definition** dbus-sysdeps-unix.c:4801

\_dbus_read_socket

int \_dbus_read_socket(DBusSocket fd, DBusString \*buffer, int count)

Like \_dbus_read(), but only works on sockets so is available on Windows.

**Definition** dbus-sysdeps-unix.c:338

\_dbus_write_socket

int \_dbus_write_socket(DBusSocket fd, const DBusString \*buffer, int start, int len)

Like \_dbus_write(), but only supports sockets and is thus available on Windows.

**Definition** dbus-sysdeps-unix.c:356

\_dbus_sleep_milliseconds

void \_dbus_sleep_milliseconds(int milliseconds)

Sleeps the given number of milliseconds.

**Definition** dbus-sysdeps-unix.c:3542

\_dbus_close_socket

dbus_bool_t \_dbus_close_socket(DBusSocket \*fd, DBusError \*error)

Closes a socket and invalidates it.

**Definition** dbus-sysdeps-unix.c:314

\_dbus_generate_random_bytes

dbus_bool_t \_dbus_generate_random_bytes(DBusString \*str, int n_bytes, DBusError \*error)

Generates the given number of securely random bytes, using the best mechanism we can come up with.

**Definition** dbus-sysdeps-unix.c:3572

\_dbus_delete_directory

dbus_bool_t \_dbus_delete_directory(const DBusString \*filename, DBusError \*error)

Removes a directory; Directory must be empty.

**Definition** dbus-sysdeps-unix.c:4822

\_dbus_accept

DBusSocket \_dbus_accept(DBusSocket listen_fd)

Accepts a connection on a listening socket.

**Definition** dbus-sysdeps-unix.c:2589

\_dbus_get_tmpdir

const char \* \_dbus_get_tmpdir(void)

Gets the temporary files directory by inspecting the environment variables TMPDIR,...

**Definition** dbus-sysdeps-unix.c:4029

\_dbus_create_directory

dbus_bool_t \_dbus_create_directory(const DBusString \*filename, DBusError \*error)

Creates a directory.

**Definition** dbus-sysdeps-unix.c:3466

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusNonceFile

**Definition** dbus-nonce.c:36

DBusSocket

Socket interface.

**Definition** dbus-sysdeps.h:185

DBusString

**Definition** dbus-string.h:47
