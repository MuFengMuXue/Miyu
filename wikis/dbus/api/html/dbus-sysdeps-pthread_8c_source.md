dbus-sysdeps-pthread.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-sysdeps-pthread.c Implements threads using pthreads (internal to libdbus)

3 \*

4 \* Copyright (C) 2002, 2003, 2006 Red Hat, Inc.

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

27\#include "dbus-internals.h"

28\#include "dbus-sysdeps.h"

29\#include "dbus-threads.h"

30

31\#include \<sys/time.h\>

32\#include \<pthread.h\>

33\#include \<stdio.h\>

34\#include \<string.h\>

35

36\#ifdef HAVE_ERRNO_H

37\#include \<errno.h\>

38\#endif

39

40\#include \<config.h\>

41

42\#ifdef HAVE_MONOTONIC_CLOCK

43/\* Whether we have a "monotonic" clock; i.e. a clock not affected by

44 \* changes in system time.

45 \* This is initialized once in check_monotonic_clock below.

46 \* https://bugs.freedesktop.org/show_bug.cgi?id=18121

47 \*/

48static dbus_bool_t have_monotonic_clock = 0;

49\#endif

50

51struct DBusRMutex {

52 pthread_mutex_t lock;

53};

54

55struct DBusCMutex {

56 pthread_mutex_t lock;

57};

58

59struct DBusCondVar {

60 pthread_cond_t cond;

61};

62

63\#define DBUS_MUTEX(m) ((DBusMutex\*) m)

64\#define DBUS_MUTEX_PTHREAD(m) ((DBusMutexPThread\*) m)

65

66\#define DBUS_COND_VAR(c) ((DBusCondVar\*) c)

67\#define DBUS_COND_VAR_PTHREAD(c) ((DBusCondVarPThread\*) c)

68

69

70\#ifdef DBUS_DISABLE_ASSERT

71/\* (tmp != 0) is a no-op usage to silence compiler \*/

72\#define PTHREAD_CHECK(func_name, result_or_call) \\

73 do { int tmp = (result_or_call); if (tmp != 0) {;} } while (0)

74\#else

75\#define PTHREAD_CHECK(func_name, result_or_call) do { \\

76 int tmp = (result_or_call); \\

77 if (tmp != 0) { \\

78 \_dbus_warn_check_failed ("pthread function %s failed with %d %s in %s", \\

79 func_name, tmp, strerror(tmp), \_DBUS_FUNCTION_NAME); \\

80 } \\

81} while (0)

82\#endif /\* !DBUS_DISABLE_ASSERT \*/

83

84DBusCMutex \*

85\_dbus_platform_cmutex_new (void)

86{

87 DBusCMutex \*pmutex;

88 int result;

89

90 pmutex = dbus_new (DBusCMutex, 1);

91 if (pmutex == NULL)

92 return NULL;

93

94 result = pthread_mutex_init (&pmutex-\>lock, NULL);

95

96 if (result == ENOMEM \|\| result == EAGAIN)

97 {

98 dbus_free (pmutex);

99 return NULL;

100 }

101 else

102 {

103 PTHREAD_CHECK ("pthread_mutex_init", result);

104 }

105

106 return pmutex;

107}

108

109DBusRMutex \*

110\_dbus_platform_rmutex_new (void)

111{

112 DBusRMutex \*pmutex;

113 pthread_mutexattr_t mutexattr;

114 int result;

115

116 pmutex = dbus_new (DBusRMutex, 1);

117 if (pmutex == NULL)

118 return NULL;

119

120 pthread_mutexattr_init (&mutexattr);

121 pthread_mutexattr_settype (&mutexattr, PTHREAD_MUTEX_RECURSIVE);

122 result = pthread_mutex_init (&pmutex-\>lock, &mutexattr);

123 pthread_mutexattr_destroy (&mutexattr);

124

125 if (result == ENOMEM \|\| result == EAGAIN)

126 {

127 dbus_free (pmutex);

128 return NULL;

129 }

130 else

131 {

132 PTHREAD_CHECK ("pthread_mutex_init", result);

133 }

134

135 return pmutex;

136}

137

138void

139\_dbus_platform_cmutex_free (DBusCMutex \*mutex)

140{

141 PTHREAD_CHECK ("pthread_mutex_destroy", pthread_mutex_destroy (&mutex-\>lock));

142 dbus_free (mutex);

143}

144

145void

146\_dbus_platform_rmutex_free (DBusRMutex \*mutex)

147{

148 PTHREAD_CHECK ("pthread_mutex_destroy", pthread_mutex_destroy (&mutex-\>lock));

149 dbus_free (mutex);

150}

151

152void

153\_dbus_platform_cmutex_lock (DBusCMutex \*mutex)

154{

155 PTHREAD_CHECK ("pthread_mutex_lock", pthread_mutex_lock (&mutex-\>lock));

156}

157

158void

159\_dbus_platform_rmutex_lock (DBusRMutex \*mutex)

160{

161 PTHREAD_CHECK ("pthread_mutex_lock", pthread_mutex_lock (&mutex-\>lock));

162}

163

164void

165\_dbus_platform_cmutex_unlock (DBusCMutex \*mutex)

166{

167 PTHREAD_CHECK ("pthread_mutex_unlock", pthread_mutex_unlock (&mutex-\>lock));

168}

169

170void

171\_dbus_platform_rmutex_unlock (DBusRMutex \*mutex)

172{

173 PTHREAD_CHECK ("pthread_mutex_unlock", pthread_mutex_unlock (&mutex-\>lock));

174}

175

176DBusCondVar \*

177\_dbus_platform_condvar_new (void)

178{

179 DBusCondVar \*pcond;

180 pthread_condattr_t attr;

181 int result;

182

183 pcond = dbus_new (DBusCondVar, 1);

184 if (pcond == NULL)

185 return NULL;

186

187 pthread_condattr_init (&attr);

188\#ifdef HAVE_MONOTONIC_CLOCK

189 if (have_monotonic_clock)

190 pthread_condattr_setclock (&attr, CLOCK_MONOTONIC);

191\#endif

192

193 result = pthread_cond_init (&pcond-\>cond, &attr);

194 pthread_condattr_destroy (&attr);

195

196 if (result == EAGAIN \|\| result == ENOMEM)

197 {

198 dbus_free (pcond);

199 return NULL;

200 }

201 else

202 {

203 PTHREAD_CHECK ("pthread_cond_init", result);

204 }

205

206 return pcond;

207}

208

209void

210\_dbus_platform_condvar_free (DBusCondVar \*cond)

211{

212 PTHREAD_CHECK ("pthread_cond_destroy", pthread_cond_destroy (&cond-\>cond));

213 dbus_free (cond);

214}

215

216void

217\_dbus_platform_condvar_wait (DBusCondVar \*cond,

218 DBusCMutex \*mutex)

219{

220 PTHREAD_CHECK ("pthread_cond_wait", pthread_cond_wait (&cond-\>cond, &mutex-\>lock));

221}

222

223dbus_bool_t

224\_dbus_platform_condvar_wait_timeout (DBusCondVar \*cond,

225 DBusCMutex \*mutex,

226 int timeout_milliseconds)

227{

228 struct timeval time_now;

229 struct timespec end_time;

230 int result;

231

232\#ifdef HAVE_MONOTONIC_CLOCK

233 if (have_monotonic_clock)

234 {

235 struct timespec monotonic_timer;

236 clock_gettime (CLOCK_MONOTONIC,&monotonic_timer);

237 time_now.tv_sec = monotonic_timer.tv_sec;

238 time_now.tv_usec = monotonic_timer.tv_nsec / 1000;

239 }

240 else

241 /\* This else falls through to gettimeofday \*/

242\#endif

243 gettimeofday (&time_now, NULL);

244

245 end_time.tv_sec = time_now.tv_sec + timeout_milliseconds / 1000;

246 end_time.tv_nsec = (time_now.tv_usec + (timeout_milliseconds % 1000) \* 1000) \* 1000;

247 if (end_time.tv_nsec \> 1000\*1000\*1000)

248 {

249 end_time.tv_sec += 1;

250 end_time.tv_nsec -= 1000\*1000\*1000;

251 }

252

253 result = pthread_cond_timedwait (&cond-\>cond, &mutex-\>lock, &end_time);

254

255 if (result != ETIMEDOUT)

256 {

257 PTHREAD_CHECK ("pthread_cond_timedwait", result);

258 }

259

260 /\* return true if we did not time out \*/

261 return result != ETIMEDOUT;

262}

263

264void

265\_dbus_platform_condvar_wake_one (DBusCondVar \*cond)

266{

267 PTHREAD_CHECK ("pthread_cond_signal", pthread_cond_signal (&cond-\>cond));

268}

269

270static void

271check_monotonic_clock (void)

272{

273\#ifdef HAVE_MONOTONIC_CLOCK

274 struct timespec dummy;

275 if (clock_getres (CLOCK_MONOTONIC, &dummy) == 0)

276 have_monotonic_clock = TRUE;

277\#endif

278}

279

280dbus_bool_t

281\_dbus_threads_init_platform_specific (void)

282{

283 /\* These have static variables, and we need to handle both the case

284 \* where dbus_threads_init() has been called and when it hasn't;

285 \* so initialize them before any threads are allowed to enter.

286 \*/

287 check_monotonic_clock ();

288 (void) \_dbus_check_setuid ();

289

290 return TRUE;

291}

292

293static pthread_mutex_t init_mutex = PTHREAD_MUTEX_INITIALIZER;

294

295void

296\_dbus_threads_lock_platform_specific (void)

297{

298 pthread_mutex_lock (&init_mutex);

299}

300

301void

302\_dbus_threads_unlock_platform_specific (void)

303{

304 pthread_mutex_unlock (&init_mutex);

305}

306

307\#ifdef DBUS_ENABLE_VERBOSE_MODE

308/\*

309 \* If we can identify the current process and/or thread, print them to stderr followed by a colon.

310 \*/

311void

312\_dbus_print_thread (void)

313{

314\#ifdef \_\_linux\_\_

315 /\* we know a pthread_t is numeric on Linux \*/

316 fprintf (stderr, "%lu: 0x%lx: ", \_dbus_pid_for_log (), (unsigned long) pthread_self ());

317\#else

318 /\* in principle pthread_t isn't required to be printable \*/

319 fprintf (stderr, "%lu: ", \_dbus_pid_for_log ());

320\#endif

321}

322\#endif

NULL

\#define NULL

A null pointer, defined appropriately for C or C++.

**Definition** dbus-macros.h:51

TRUE

\#define TRUE

Expands to "1".

**Definition** dbus-macros.h:41

dbus_free

void dbus_free(void \*memory)

Frees a block of memory previously allocated by dbus_malloc() or dbus_malloc0().

**Definition** dbus-memory.c:710

dbus_new

\#define dbus_new(type, count)

Safe macro for using dbus_malloc().

**Definition** dbus-memory.h:59

\_dbus_pid_for_log

unsigned long \_dbus_pid_for_log(void)

The only reason this is separate from \_dbus_getpid() is to allow it on Windows for logging but not fo...

**Definition** dbus-sysdeps-unix.c:3157

\_dbus_threads_lock_platform_specific

void \_dbus_threads_lock_platform_specific(void)

Lock a static mutex used to protect \_dbus_threads_init_platform_specific().

**Definition** dbus-sysdeps-pthread.c:296

\_dbus_check_setuid

dbus_bool_t \_dbus_check_setuid(void)

NOTE: If you modify this function, please also consider making the corresponding change in GLib.

**Definition** dbus-sysdeps-unix.c:5002

\_dbus_threads_unlock_platform_specific

void \_dbus_threads_unlock_platform_specific(void)

Undo \_dbus_threads_lock_platform_specific().

**Definition** dbus-sysdeps-pthread.c:302

\_dbus_threads_init_platform_specific

dbus_bool_t \_dbus_threads_init_platform_specific(void)

Initialize threads as in dbus_threads_init_default(), appropriately for the platform.

**Definition** dbus-sysdeps-pthread.c:281

DBusCMutex

**Definition** dbus-sysdeps-pthread.c:55

DBusCMutex::lock

pthread_mutex_t lock

the lock

**Definition** dbus-sysdeps-pthread.c:56

DBusCondVar

**Definition** dbus-sysdeps-pthread.c:59

DBusCondVar::cond

pthread_cond_t cond

the condition

**Definition** dbus-sysdeps-pthread.c:60

DBusRMutex

**Definition** dbus-sysdeps-pthread.c:51

DBusRMutex::lock

pthread_mutex_t lock

the lock

**Definition** dbus-sysdeps-pthread.c:52
