dbus-errors.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-errors.c Error reporting

3 \*

4 \* Copyright (C) 2002, 2004 Red Hat Inc.

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

28\#include "dbus-errors.h"

29\#include "dbus-internals.h"

30\#include "dbus-string.h"

31\#include "dbus-protocol.h"

32\#include \<stdarg.h\>

33\#include \<string.h\>

34

67typedef struct

68{

69 char \*name;

70 char \*message;

72 unsigned int const_message : 1;

74 unsigned int dummy2 : 1;

75 unsigned int dummy3 : 1;

76 unsigned int dummy4 : 1;

77 unsigned int dummy5 : 1;

79 void \*padding1;

81} DBusRealError;

82

83\_DBUS_STATIC_ASSERT (sizeof (DBusRealError) == sizeof (DBusError));

84

93static const char\*

94message_from_error (const char \*error)

95{

96 if (strcmp (error, DBUS_ERROR_FAILED) == 0)

97 return "Unknown error";

98 else if (strcmp (error, DBUS_ERROR_NO_MEMORY) == 0)

99 return "Not enough memory available";

100 else if (strcmp (error, DBUS_ERROR_IO_ERROR) == 0)

101 return "Error reading or writing data";

102 else if (strcmp (error, DBUS_ERROR_BAD_ADDRESS) == 0)

103 return "Could not parse address";

104 else if (strcmp (error, DBUS_ERROR_NOT_SUPPORTED) == 0)

105 return "Feature not supported";

106 else if (strcmp (error, DBUS_ERROR_LIMITS_EXCEEDED) == 0)

107 return "Resource limits exceeded";

108 else if (strcmp (error, DBUS_ERROR_ACCESS_DENIED) == 0)

109 return "Permission denied";

110 else if (strcmp (error, DBUS_ERROR_AUTH_FAILED) == 0)

111 return "Could not authenticate to server";

112 else if (strcmp (error, DBUS_ERROR_NO_SERVER) == 0)

113 return "No server available at address";

114 else if (strcmp (error, DBUS_ERROR_TIMEOUT) == 0)

115 return "Connection timed out";

116 else if (strcmp (error, DBUS_ERROR_NO_NETWORK) == 0)

117 return "Network unavailable";

118 else if (strcmp (error, DBUS_ERROR_ADDRESS_IN_USE) == 0)

119 return "Address already in use";

120 else if (strcmp (error, DBUS_ERROR_DISCONNECTED) == 0)

121 return "Disconnected.";

122 else if (strcmp (error, DBUS_ERROR_INVALID_ARGS) == 0)

123 return "Invalid arguments.";

124 else if (strcmp (error, DBUS_ERROR_NO_REPLY) == 0)

125 return "Did not get a reply message.";

126 else if (strcmp (error, DBUS_ERROR_FILE_NOT_FOUND) == 0)

127 return "File doesn't exist.";

128 else if (strcmp (error, DBUS_ERROR_OBJECT_PATH_IN_USE) == 0)

129 return "Object path already in use";

130 else

131 return error;

132}

133

/\* End of internals \*/

135

189void

190dbus_error_init (DBusError \*error)

191{

192 DBusRealError \*real;

193

194 \_DBUS_STATIC_ASSERT (sizeof (DBusError) == sizeof (DBusRealError));

195

196 \_dbus_return_if_fail (error != NULL);

197

198 real = (DBusRealError \*)error;

199

200 real-\>name = NULL;

201 real-\>message = NULL;

202

203 real-\>const_message = TRUE;

204}

205

212void

213dbus_error_free (DBusError \*error)

214{

215 DBusRealError \*real;

216

217 \_dbus_return_if_fail (error != NULL);

218

219 real = (DBusRealError \*)error;

220

221 if (!real-\>const_message)

222 {

223 dbus_free (real-\>name);

224 dbus_free (real-\>message);

225 }

226

227 dbus_error_init (error);

228}

229

244void

245dbus_set_error_const (DBusError \*error,

246 const char \*name,

247 const char \*message)

248{

249 DBusRealError \*real;

250

251 \_dbus_return_if_error_is_set (error);

252 \_dbus_return_if_fail (name != NULL);

253

254 if (error == NULL)

255 return;

256

257 \_dbus_assert (error-\>name == NULL);

258 \_dbus_assert (error-\>message == NULL);

259

260 if (message == NULL)

261 message = message_from_error (name);

262

263 real = (DBusRealError \*)error;

264

265 real-\>name = (char\*) name;

266 real-\>message = (char \*)message;

267 real-\>const_message = TRUE;

268}

269

280void

281dbus_move_error (DBusError \*src,

282 DBusError \*dest)

283{

284 \_dbus_return_if_error_is_set (dest);

285

286 if (dest)

287 {

288 dbus_error_free (dest);

289 \*dest = \*src;

290 dbus_error_init (src);

291 }

292 else

293 dbus_error_free (src);

294}

295

303dbus_bool_t

304dbus_error_has_name (const DBusError \*error,

305 const char \*name)

306{

307 \_dbus_return_val_if_fail (error != NULL, FALSE);

308 \_dbus_return_val_if_fail (name != NULL, FALSE);

309

310 \_dbus_assert ((error-\>name != NULL && error-\>message != NULL) \|\|

311 (error-\>name == NULL && error-\>message == NULL));

312

313 if (error-\>name != NULL)

314 {

315 DBusString str1, str2;

316 \_dbus_string_init_const (&str1, error-\>name);

317 \_dbus_string_init_const (&str2, name);

318 return \_dbus_string_equal (&str1, &str2);

319 }

320 else

321 return FALSE;

322}

323

330dbus_bool_t

331dbus_error_is_set (const DBusError \*error)

332{

333 \_dbus_return_val_if_fail (error != NULL, FALSE);

334 \_dbus_assert ((error-\>name != NULL && error-\>message != NULL) \|\|

335 (error-\>name == NULL && error-\>message == NULL));

336 return error-\>name != NULL;

337}

338

355void

356dbus_set_error (DBusError \*error,

357 const char \*name,

358 const char \*format,

359 ...)

360{

361 va_list args;

362

363 if (error == NULL)

364 return;

365

366 /\* it's a bug to pile up errors \*/

367 \_dbus_return_if_error_is_set (error);

368 \_dbus_return_if_fail (name != NULL);

369

370 va_start (args, format);

371 \_dbus_set_error_valist (error, name, format, args);

372 va_end (args);

373}

374

375void

376\_dbus_set_error_valist (DBusError \*error,

377 const char \*name,

378 const char \*format,

379 va_list args)

380{

381 DBusRealError \*real;

382 DBusString str;

383

384 \_dbus_assert (name != NULL);

385

386 if (error == NULL)

387 return;

388

389 \_dbus_assert (error-\>name == NULL);

390 \_dbus_assert (error-\>message == NULL);

391

392 if (!\_dbus_string_init (&str))

393 goto nomem;

394

395 if (format == NULL)

396 {

397 if (!\_dbus_string_append (&str,

398 message_from_error (name)))

399 {

400 \_dbus_string_free (&str);

401 goto nomem;

402 }

403 }

404 else

405 {

406 if (!\_dbus_string_append_printf_valist (&str, format, args))

407 {

408 \_dbus_string_free (&str);

409 goto nomem;

410 }

411 }

412

413 real = (DBusRealError \*)error;

414

415 if (!\_dbus_string_steal_data (&str, &real-\>message))

416 {

417 \_dbus_string_free (&str);

418 goto nomem;

419 }

420 \_dbus_string_free (&str);

421

422 real-\>name = \_dbus_strdup (name);

423 if (real-\>name == NULL)

424 {

425 dbus_free (real-\>message);

426 real-\>message = NULL;

427 goto nomem;

428 }

429 real-\>const_message = FALSE;

430

431 return;

432

433 nomem:

434 \_DBUS_SET_OOM (error);

435}

436

/\* End public API \*/

dbus_move_error

void dbus_move_error(DBusError \*src, DBusError \*dest)

Moves an error src into dest, freeing src and overwriting dest.

**Definition** dbus-errors.c:281

dbus_set_error_const

void dbus_set_error_const(DBusError \*error, const char \*name, const char \*message)

Assigns an error name and message to a DBusError.

**Definition** dbus-errors.c:245

dbus_error_has_name

dbus_bool_t dbus_error_has_name(const DBusError \*error, const char \*name)

Checks whether the error is set and has the given name.

**Definition** dbus-errors.c:304

dbus_error_init

void dbus_error_init(DBusError \*error)

Initializes a DBusError structure.

**Definition** dbus-errors.c:190

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

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_dbus_strdup

char \* \_dbus_strdup(const char \*str)

Duplicates a string.

**Definition** dbus-internals.c:621

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

DBUS_ERROR_TIMEOUT

\#define DBUS_ERROR_TIMEOUT

Certain timeout errors, possibly ETIMEDOUT on a socket.

**Definition** dbus-protocol.h:389

DBUS_ERROR_NOT_SUPPORTED

\#define DBUS_ERROR_NOT_SUPPORTED

Requested operation isn't supported (like ENOSYS on UNIX).

**Definition** dbus-protocol.h:375

DBUS_ERROR_ADDRESS_IN_USE

\#define DBUS_ERROR_ADDRESS_IN_USE

Can't bind a socket since its address is in use (i.e.

**Definition** dbus-protocol.h:393

DBUS_ERROR_BAD_ADDRESS

\#define DBUS_ERROR_BAD_ADDRESS

A D-Bus bus address was malformed.

**Definition** dbus-protocol.h:373

DBUS_ERROR_IO_ERROR

\#define DBUS_ERROR_IO_ERROR

Something went wrong reading or writing to a socket, for example.

**Definition** dbus-protocol.h:371

DBUS_ERROR_AUTH_FAILED

\#define DBUS_ERROR_AUTH_FAILED

Authentication didn't work.

**Definition** dbus-protocol.h:381

DBUS_ERROR_OBJECT_PATH_IN_USE

\#define DBUS_ERROR_OBJECT_PATH_IN_USE

There's already an object with the requested object path.

**Definition** dbus-protocol.h:456

DBUS_ERROR_ACCESS_DENIED

\#define DBUS_ERROR_ACCESS_DENIED

Security restrictions don't allow doing what you're trying to do.

**Definition** dbus-protocol.h:379

DBUS_ERROR_NO_SERVER

\#define DBUS_ERROR_NO_SERVER

Unable to connect to server (probably caused by ECONNREFUSED on a socket).

**Definition** dbus-protocol.h:383

DBUS_ERROR_LIMITS_EXCEEDED

\#define DBUS_ERROR_LIMITS_EXCEEDED

Some limited resource is exhausted.

**Definition** dbus-protocol.h:377

DBUS_ERROR_NO_NETWORK

\#define DBUS_ERROR_NO_NETWORK

No network access (probably ENETUNREACH on a socket).

**Definition** dbus-protocol.h:391

DBUS_ERROR_FAILED

\#define DBUS_ERROR_FAILED

A generic error; "something went wrong" - see the error message for more.

**Definition** dbus-protocol.h:361

DBUS_ERROR_NO_MEMORY

\#define DBUS_ERROR_NO_MEMORY

There was not enough memory to complete an operation.

**Definition** dbus-protocol.h:363

DBUS_ERROR_INVALID_ARGS

\#define DBUS_ERROR_INVALID_ARGS

Invalid arguments passed to a method call.

**Definition** dbus-protocol.h:397

DBUS_ERROR_NO_REPLY

\#define DBUS_ERROR_NO_REPLY

No reply to a message expecting one, usually means a timeout occurred.

**Definition** dbus-protocol.h:369

DBUS_ERROR_DISCONNECTED

\#define DBUS_ERROR_DISCONNECTED

The connection is disconnected and you're trying to use it.

**Definition** dbus-protocol.h:395

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

\_dbus_string_steal_data

dbus_bool_t \_dbus_string_steal_data(DBusString \*str, char \*\*data_return)

Like \_dbus_string_get_data(), but removes the gotten data from the original string.

**Definition** dbus-string.c:686

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_string_append_printf_valist

dbus_bool_t \_dbus_string_append_printf_valist(DBusString \*str, const char \*format, va_list args)

Appends a printf-style formatted string to the DBusString.

**Definition** dbus-string.c:1105

\_dbus_string_equal

dbus_bool_t \_dbus_string_equal(const DBusString \*a, const DBusString \*b)

Tests two DBusString for equality.

**Definition** dbus-string.c:2075

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusError::name

const char \* name

public error name field

**Definition** dbus-errors.h:52

DBusError::message

const char \* message

public error message field

**Definition** dbus-errors.h:53

DBusRealError

Internals of DBusError.

**Definition** dbus-errors.c:68

DBusRealError::dummy2

unsigned int dummy2

placeholder

**Definition** dbus-errors.c:74

DBusRealError::name

char \* name

error name

**Definition** dbus-errors.c:69

DBusRealError::const_message

unsigned int const_message

Message is not owned by DBusError.

**Definition** dbus-errors.c:72

DBusRealError::dummy5

unsigned int dummy5

placeholder

**Definition** dbus-errors.c:77

DBusRealError::dummy4

unsigned int dummy4

placeholder

**Definition** dbus-errors.c:76

DBusRealError::dummy3

unsigned int dummy3

placeholder

**Definition** dbus-errors.c:75

DBusRealError::padding1

void \* padding1

placeholder

**Definition** dbus-errors.c:79

DBusRealError::message

char \* message

error message

**Definition** dbus-errors.c:70

DBusString

**Definition** dbus-string.h:47
