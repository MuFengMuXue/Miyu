dbus-threads.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-threads.h D-Bus threads handling

3 \*

4 \* Copyright (C) 2002, 2003, 2006 Red Hat Inc.

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

26\#include "dbus-threads.h"

27\#include "dbus-internals.h"

28\#include "dbus-threads-internal.h"

29\#include "dbus-list.h"

30

31/\* Protected by \_dbus_threads_lock_platform_specific() \*/

32static int thread_init_generation = 0;

33

55void

56\_dbus_rmutex_new_at_location (DBusRMutex \*\*location_p)

57{

58 \_dbus_assert (location_p != NULL);

59

60 if (!dbus_threads_init_default ())

61 {

62 \*location_p = NULL;

63 return;

64 }

65

66 \*location_p = \_dbus_platform_rmutex_new ();

67}

68

79void

80\_dbus_cmutex_new_at_location (DBusCMutex \*\*location_p)

81{

82 \_dbus_assert (location_p != NULL);

83

84 if (!dbus_threads_init_default ())

85 {

86 \*location_p = NULL;

87 return;

88 }

89

90 \*location_p = \_dbus_platform_cmutex_new ();

91}

92

96void

97\_dbus_rmutex_free_at_location (DBusRMutex \*\*location_p)

98{

99 if (location_p == NULL)

100 return;

101

102 if (\*location_p != NULL)

103 \_dbus_platform_rmutex_free (\*location_p);

104}

105

109void

110\_dbus_cmutex_free_at_location (DBusCMutex \*\*location_p)

111{

112 if (location_p == NULL)

113 return;

114

115 if (\*location_p != NULL)

116 \_dbus_platform_cmutex_free (\*location_p);

117}

118

124void

125\_dbus_rmutex_lock (DBusRMutex \*mutex)

126{

127 if (mutex == NULL)

128 return;

129

130 \_dbus_platform_rmutex_lock (mutex);

131}

132

138void

139\_dbus_cmutex_lock (DBusCMutex \*mutex)

140{

141 if (mutex == NULL)

142 return;

143

144 \_dbus_platform_cmutex_lock (mutex);

145}

146

152void

153\_dbus_rmutex_unlock (DBusRMutex \*mutex)

154{

155 if (mutex == NULL)

156 return;

157

158 \_dbus_platform_rmutex_unlock (mutex);

159}

160

166void

167\_dbus_cmutex_unlock (DBusCMutex \*mutex)

168{

169 if (mutex == NULL)

170 return;

171

172 \_dbus_platform_cmutex_unlock (mutex);

173}

174

183DBusCondVar \*

184\_dbus_condvar_new (void)

185{

186 if (!dbus_threads_init_default ())

187 return NULL;

188

189 return \_dbus_platform_condvar_new ();

190}

191

192

201void

202\_dbus_condvar_new_at_location (DBusCondVar \*\*location_p)

203{

204 \_dbus_assert (location_p != NULL);

205

206 \*location_p = \_dbus_condvar_new();

207}

208

209

214void

215\_dbus_condvar_free (DBusCondVar \*cond)

216{

217 if (cond == NULL)

218 return;

219

220 \_dbus_platform_condvar_free (cond);

221}

222

226void

227\_dbus_condvar_free_at_location (DBusCondVar \*\*location_p)

228{

229 if (location_p == NULL)

230 return;

231

232 if (\*location_p != NULL)

233 \_dbus_platform_condvar_free (\*location_p);

234}

235

242void

243\_dbus_condvar_wait (DBusCondVar \*cond,

244 DBusCMutex \*mutex)

245{

246 if (cond == NULL \|\| mutex == NULL)

247 return;

248

249 \_dbus_platform_condvar_wait (cond, mutex);

250}

251

263dbus_bool_t

264\_dbus_condvar_wait_timeout (DBusCondVar \*cond,

265 DBusCMutex \*mutex,

266 int timeout_milliseconds)

267{

268 if (cond == NULL \|\| mutex == NULL)

269 return TRUE;

270

271 return \_dbus_platform_condvar_wait_timeout (cond, mutex,

272 timeout_milliseconds);

273}

274

280void

281\_dbus_condvar_wake_one (DBusCondVar \*cond)

282{

283 if (cond == NULL)

284 return;

285

286 \_dbus_platform_condvar_wake_one (cond);

287}

288

289/\* Protected by \_dbus_threads_lock_platform_specific() \*/

290static DBusRMutex \*global_locks\[\_DBUS_N_GLOBAL_LOCKS\] = { NULL };

291

292static void

293shutdown_global_locks (void \*nil)

294{

295 int i;

296

297 for (i = 0; i \< \_DBUS_N_GLOBAL_LOCKS; i++)

298 {

299 \_dbus_assert (global_locks\[i\] != NULL);

300 \_dbus_platform_rmutex_free (global_locks\[i\]);

301 global_locks\[i\] = NULL;

302 }

303}

304

305static dbus_bool_t

306init_global_locks (void)

307{

308 int i;

309 dbus_bool_t ok;

310

311 for (i = 0; i \< \_DBUS_N_GLOBAL_LOCKS; i++)

312 {

313 \_dbus_assert (global_locks\[i\] == NULL);

314

315 global_locks\[i\] = \_dbus_platform_rmutex_new ();

316

317 if (global_locks\[i\] == NULL)

318 goto failed;

319 }

320

321 \_dbus_platform_rmutex_lock (global_locks\[\_DBUS_LOCK_shutdown_funcs\]);

322 ok = \_dbus_register_shutdown_func_unlocked (shutdown_global_locks, NULL);

323 \_dbus_platform_rmutex_unlock (global_locks\[\_DBUS_LOCK_shutdown_funcs\]);

324

325 if (!ok)

326 goto failed;

327

328 return TRUE;

329

330 failed:

331 for (i = i - 1; i \>= 0; i--)

332 {

333 \_dbus_platform_rmutex_free (global_locks\[i\]);

334 global_locks\[i\] = NULL;

335 }

336

337 return FALSE;

338}

339

340dbus_bool_t

341\_dbus_lock (DBusGlobalLock lock)

342{

343 \_dbus_assert (lock \>= 0);

344 \_dbus_assert (lock \< \_DBUS_N_GLOBAL_LOCKS);

345

346 if (thread_init_generation != \_dbus_current_generation &&

347 !dbus_threads_init_default ())

348 return FALSE;

349

350 \_dbus_platform_rmutex_lock (global_locks\[lock\]);

351 return TRUE;

352}

353

354void

355\_dbus_unlock (DBusGlobalLock lock)

356{

357 \_dbus_assert (lock \>= 0);

358 \_dbus_assert (lock \< \_DBUS_N_GLOBAL_LOCKS);

359

360 \_dbus_platform_rmutex_unlock (global_locks\[lock\]);

361}

362

/\* end of internals \*/

364

394dbus_bool_t

395dbus_threads_init (const DBusThreadFunctions \*functions)

396{

397 \_dbus_threads_lock_platform_specific ();

398

399 if (thread_init_generation == \_dbus_current_generation)

400 {

401 \_dbus_threads_unlock_platform_specific ();

402 return TRUE;

403 }

404

405 if (!\_dbus_threads_init_platform_specific() \|\|

406 !init_global_locks ())

407 {

408 \_dbus_threads_unlock_platform_specific ();

409 return FALSE;

410 }

411

412 thread_init_generation = \_dbus_current_generation;

413

414 \_dbus_threads_unlock_platform_specific ();

415 return TRUE;

416}

417

418

419

420/\* Default thread implemenation \*/

421

441dbus_bool_t

442dbus_threads_init_default (void)

443{

444 return dbus_threads_init (NULL);

445}

446

447

450\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

451

452\#endif /\* DBUS_ENABLE_EMBEDDED_TESTS \*/

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

\_dbus_current_generation

int \_dbus_current_generation

\_dbus_current_generation is used to track each time that dbus_shutdown() is called,...

**Definition** dbus-memory.c:790

\_dbus_threads_lock_platform_specific

void \_dbus_threads_lock_platform_specific(void)

Lock a static mutex used to protect \_dbus_threads_init_platform_specific().

**Definition** dbus-sysdeps-pthread.c:296

\_dbus_threads_unlock_platform_specific

void \_dbus_threads_unlock_platform_specific(void)

Undo \_dbus_threads_lock_platform_specific().

**Definition** dbus-sysdeps-pthread.c:302

\_dbus_threads_init_platform_specific

dbus_bool_t \_dbus_threads_init_platform_specific(void)

Initialize threads as in dbus_threads_init_default(), appropriately for the platform.

**Definition** dbus-sysdeps-pthread.c:281

\_dbus_rmutex_new_at_location

void \_dbus_rmutex_new_at_location(DBusRMutex \*\*location_p)

Creates a new mutex or creates a no-op mutex if threads are not initialized.

**Definition** dbus-threads.c:56

\_dbus_cmutex_free_at_location

void \_dbus_cmutex_free_at_location(DBusCMutex \*\*location_p)

Frees a DBusCMutex; does nothing if passed a NULL pointer.

**Definition** dbus-threads.c:110

\_dbus_condvar_new

DBusCondVar \* \_dbus_condvar_new(void)

Creates a new condition variable using the function supplied to dbus_threads_init(),...

**Definition** dbus-threads.c:184

\_dbus_condvar_free_at_location

void \_dbus_condvar_free_at_location(DBusCondVar \*\*location_p)

Frees a condition variable; does nothing if passed a NULL pointer.

**Definition** dbus-threads.c:227

\_dbus_rmutex_unlock

void \_dbus_rmutex_unlock(DBusRMutex \*mutex)

Unlocks a mutex.

**Definition** dbus-threads.c:153

\_dbus_condvar_wait

void \_dbus_condvar_wait(DBusCondVar \*cond, DBusCMutex \*mutex)

Atomically unlocks the mutex and waits for the conditions variable to be signalled.

**Definition** dbus-threads.c:243

\_dbus_condvar_new_at_location

void \_dbus_condvar_new_at_location(DBusCondVar \*\*location_p)

This does the same thing as \_dbus_condvar_new.

**Definition** dbus-threads.c:202

\_dbus_cmutex_new_at_location

void \_dbus_cmutex_new_at_location(DBusCMutex \*\*location_p)

Creates a new mutex or creates a no-op mutex if threads are not initialized.

**Definition** dbus-threads.c:80

\_dbus_condvar_wake_one

void \_dbus_condvar_wake_one(DBusCondVar \*cond)

If there are threads waiting on the condition variable, wake up exactly one.

**Definition** dbus-threads.c:281

\_dbus_condvar_wait_timeout

dbus_bool_t \_dbus_condvar_wait_timeout(DBusCondVar \*cond, DBusCMutex \*mutex, int timeout_milliseconds)

Atomically unlocks the mutex and waits for the conditions variable to be signalled,...

**Definition** dbus-threads.c:264

\_dbus_cmutex_lock

void \_dbus_cmutex_lock(DBusCMutex \*mutex)

Locks a mutex.

**Definition** dbus-threads.c:139

\_dbus_cmutex_unlock

void \_dbus_cmutex_unlock(DBusCMutex \*mutex)

Unlocks a mutex.

**Definition** dbus-threads.c:167

\_dbus_rmutex_free_at_location

void \_dbus_rmutex_free_at_location(DBusRMutex \*\*location_p)

Frees a DBusRMutex; does nothing if passed a NULL pointer.

**Definition** dbus-threads.c:97

\_dbus_rmutex_lock

void \_dbus_rmutex_lock(DBusRMutex \*mutex)

Locks a mutex.

**Definition** dbus-threads.c:125

\_dbus_condvar_free

void \_dbus_condvar_free(DBusCondVar \*cond)

Frees a conditional variable created with dbus_condvar_new(); does nothing if passed a NULL pointer.

**Definition** dbus-threads.c:215

dbus_threads_init_default

dbus_bool_t dbus_threads_init_default(void)

Initializes threads.

**Definition** dbus-threads.c:442

dbus_threads_init

dbus_bool_t dbus_threads_init(const DBusThreadFunctions \*functions)

Initializes threads, like dbus_threads_init_default().

**Definition** dbus-threads.c:395

DBusCMutex

**Definition** dbus-sysdeps-pthread.c:55

DBusCondVar

**Definition** dbus-sysdeps-pthread.c:59

DBusRMutex

**Definition** dbus-sysdeps-pthread.c:51

DBusThreadFunctions

Functions that must be implemented to make the D-Bus library thread-aware.

**Definition** dbus-threads.h:155
