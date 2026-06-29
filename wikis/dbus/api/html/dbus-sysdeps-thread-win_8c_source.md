dbus-sysdeps-thread-win.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-sysdeps-pthread.c Implements threads using Windows threads (internal to libdbus)

3 \*

4 \* Copyright (C) 2006 Red Hat, Inc.

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

27\#include "dbus-init-win.h"

28\#include "dbus-internals.h"

29\#include "dbus-sysdeps.h"

30\#include "dbus-sysdeps-win.h"

31\#include "dbus-threads.h"

32\#include "dbus-list.h"

33

34\#include \<stdio.h\>

35

36\#include \<windows.h\>

37

38\#ifdef DBUS_DISABLE_ASSERT

39\#define THREAD_CHECK_TRUE(func_name, result_or_call) \\

40 do { if (!(result_or_call)) { /\* ignore \*/ } } while (0)

41\#else

42\#define THREAD_CHECK_TRUE(func_name, result_or_call) do { \\

43 if (!(result_or_call)) { \\

44 \_dbus_warn_check_failed ("thread function %s failed (windows error code=%ld) in %s", \\

45 func_name, GetLastError (), \_DBUS_FUNCTION_NAME); \\

46 } \\

47} while (0)

48\#endif /\* !DBUS_DISABLE_ASSERT \*/

49

50/\* Protected by DllMain lock, effectively \*/

51static dbus_bool_t global_init_done = FALSE;

52static CRITICAL_SECTION init_lock;

53

54/\* Called from C++ code in dbus-init-win.cpp. \*/

55void

56\_dbus_threads_windows_init_global (void)

57{

58 /\* this ensures that the object that acts as our global constructor

59 \* actually gets linked in when we're linked statically \*/

60 \_dbus_threads_windows_ensure_ctor_linked ();

61

62 InitializeCriticalSection (&init_lock);

63 global_init_done = TRUE;

64}

65

66struct DBusCondVar {

67 DBusList \*list;

68 CRITICAL_SECTION lock;

69};

70

71static DWORD dbus_cond_event_tls = TLS_OUT_OF_INDEXES;

72

73/\* Protected by DllMain lock, effectively \*/

74static HMODULE dbus_dll_hmodule;

75

76void \*

77\_dbus_win_get_dll_hmodule (void)

78{

79 return dbus_dll_hmodule;

80}

81

82\#ifdef DBUS_WINCE

83\#define hinst_t HANDLE

84\#else

85\#define hinst_t HINSTANCE

86\#endif

87

88BOOL WINAPI DllMain (hinst_t, DWORD, LPVOID);

89

90/\* We need this to free the TLS events on thread exit \*/

91BOOL WINAPI

92DllMain (hinst_t hinstDLL,

93 DWORD fdwReason,

94 LPVOID lpvReserved)

95{

96 HANDLE event;

97 switch (fdwReason)

98 {

99 case DLL_PROCESS_ATTACH:

100 dbus_dll_hmodule = hinstDLL;

101 break;

102 case DLL_THREAD_DETACH:

103 if (dbus_cond_event_tls != TLS_OUT_OF_INDEXES)

104 {

105 event = TlsGetValue(dbus_cond_event_tls);

106 CloseHandle (event);

107 TlsSetValue(dbus_cond_event_tls, NULL);

108 }

109 break;

110 case DLL_PROCESS_DETACH:

111 if (dbus_cond_event_tls != TLS_OUT_OF_INDEXES)

112 {

113 event = TlsGetValue(dbus_cond_event_tls);

114 CloseHandle (event);

115 TlsSetValue(dbus_cond_event_tls, NULL);

116

117 TlsFree(dbus_cond_event_tls);

118 }

119 break;

120 default:

121 break;

122 }

123 return TRUE;

124}

125

126DBusCMutex \*

127\_dbus_platform_cmutex_new (void)

128{

129 HANDLE handle;

130 handle = CreateMutex (NULL, FALSE, NULL);

131 THREAD_CHECK_TRUE ("CreateMutex", handle);

132 return (DBusCMutex \*) handle;

133}

134

135DBusRMutex \*

136\_dbus_platform_rmutex_new (void)

137{

138 HANDLE handle;

139 handle = CreateMutex (NULL, FALSE, NULL);

140 THREAD_CHECK_TRUE ("CreateMutex", handle);

141 return (DBusRMutex \*) handle;

142}

143

144DBusRMutex \*

145\_dbus_win_rmutex_named_new (const char \*name)

146{

147 HANDLE handle;

148 handle = CreateMutex (NULL, FALSE, name);

149 THREAD_CHECK_TRUE ("CreateMutex", handle);

150 return (DBusRMutex \*) handle;

151}

152

153void

154\_dbus_platform_cmutex_free (DBusCMutex \*mutex)

155{

156 THREAD_CHECK_TRUE ("CloseHandle", CloseHandle ((HANDLE \*) mutex));

157}

158

159void

160\_dbus_platform_rmutex_free (DBusRMutex \*mutex)

161{

162 THREAD_CHECK_TRUE ("CloseHandle", CloseHandle ((HANDLE \*) mutex));

163}

164

165void

166\_dbus_platform_cmutex_lock (DBusCMutex \*mutex)

167{

168 THREAD_CHECK_TRUE ("WaitForSingleObject", WaitForSingleObject ((HANDLE \*) mutex, INFINITE) == WAIT_OBJECT_0);

169}

170

171void

172\_dbus_platform_rmutex_lock (DBusRMutex \*mutex)

173{

174 THREAD_CHECK_TRUE ("WaitForSingleObject", WaitForSingleObject ((HANDLE \*) mutex, INFINITE) == WAIT_OBJECT_0);

175}

176

177void

178\_dbus_platform_cmutex_unlock (DBusCMutex \*mutex)

179{

180 THREAD_CHECK_TRUE ("ReleaseMutex", ReleaseMutex ((HANDLE \*) mutex));

181}

182

183void

184\_dbus_platform_rmutex_unlock (DBusRMutex \*mutex)

185{

186 THREAD_CHECK_TRUE ("ReleaseMutex", ReleaseMutex ((HANDLE \*) mutex));

187}

188

189DBusCondVar \*

190\_dbus_platform_condvar_new (void)

191{

192 DBusCondVar \*cond;

193

194 cond = dbus_new (DBusCondVar, 1);

195 if (cond == NULL)

196 return NULL;

197

198 cond-\>list = NULL;

199

200 InitializeCriticalSection (&cond-\>lock);

201 return cond;

202}

203

204void

205\_dbus_platform_condvar_free (DBusCondVar \*cond)

206{

207 DeleteCriticalSection (&cond-\>lock);

208 \_dbus_list_clear (&cond-\>list);

209 dbus_free (cond);

210}

211

212static dbus_bool_t

213\_dbus_condvar_wait_win32 (DBusCondVar \*cond,

214 DBusCMutex \*mutex,

215 int milliseconds)

216{

217 DWORD retval;

218 dbus_bool_t ret;

219 HANDLE event = TlsGetValue (dbus_cond_event_tls);

220

221 if (!event)

222 {

223 event = CreateEvent (0, FALSE, FALSE, NULL);

224 if (event == 0)

225 return FALSE;

226 TlsSetValue (dbus_cond_event_tls, event);

227 }

228

229 EnterCriticalSection (&cond-\>lock);

230

231 /\* The event must not be signaled. Check this \*/

232 \_dbus_assert (WaitForSingleObject (event, 0) == WAIT_TIMEOUT);

233

234 ret = \_dbus_list_append (&cond-\>list, event);

235

236 LeaveCriticalSection (&cond-\>lock);

237

238 if (!ret)

239 return FALSE; /\* Prepend failed \*/

240

241 \_dbus_platform_cmutex_unlock (mutex);

242 retval = WaitForSingleObject (event, milliseconds);

243 \_dbus_platform_cmutex_lock (mutex);

244

245 if (retval == WAIT_TIMEOUT)

246 {

247 EnterCriticalSection (&cond-\>lock);

248 \_dbus_list_remove (&cond-\>list, event);

249

250 /\* In the meantime we could have been signaled, so we must again

251 \* wait for the signal, this time with no timeout, to reset

252 \* it. retval is set again to honour the late arrival of the

253 \* signal \*/

254 retval = WaitForSingleObject (event, 0);

255

256 LeaveCriticalSection (&cond-\>lock);

257 }

258

259\#ifndef DBUS_DISABLE_ASSERT

260 EnterCriticalSection (&cond-\>lock);

261

262 /\* Now event must not be inside the array, check this \*/

263 \_dbus_assert (\_dbus_list_remove (&cond-\>list, event) == FALSE);

264

265 LeaveCriticalSection (&cond-\>lock);

266\#endif /\* !G_DISABLE_ASSERT \*/

267

268 return retval != WAIT_TIMEOUT;

269}

270

271void

272\_dbus_platform_condvar_wait (DBusCondVar \*cond,

273 DBusCMutex \*mutex)

274{

275 \_dbus_condvar_wait_win32 (cond, mutex, INFINITE);

276}

277

278dbus_bool_t

279\_dbus_platform_condvar_wait_timeout (DBusCondVar \*cond,

280 DBusCMutex \*mutex,

281 int timeout_milliseconds)

282{

283 return \_dbus_condvar_wait_win32 (cond, mutex, timeout_milliseconds);

284}

285

286void

287\_dbus_platform_condvar_wake_one (DBusCondVar \*cond)

288{

289 EnterCriticalSection (&cond-\>lock);

290

291 if (cond-\>list != NULL)

292 {

293 SetEvent (\_dbus_list_pop_first (&cond-\>list));

294 /\* Avoid live lock by pushing the waiter to the mutex lock

295 instruction, which is fair. If we don't do this, we could

296 acquire the condition variable again before the waiter has a

297 chance itself, leading to starvation. \*/

298 Sleep (0);

299 }

300 LeaveCriticalSection (&cond-\>lock);

301}

302

303dbus_bool_t

304\_dbus_threads_init_platform_specific (void)

305{

306 /\* We reuse this over several generations, because we can't

307 \* free the events once they are in use

308 \*/

309 if (dbus_cond_event_tls == TLS_OUT_OF_INDEXES)

310 {

311 dbus_cond_event_tls = TlsAlloc ();

312 if (dbus_cond_event_tls == TLS_OUT_OF_INDEXES)

313 return FALSE;

314 }

315

316 return TRUE;

317}

318

319void

320\_dbus_threads_lock_platform_specific (void)

321{

322 \_dbus_assert (global_init_done);

323 EnterCriticalSection (&init_lock);

324}

325

326void

327\_dbus_threads_unlock_platform_specific (void)

328{

329 \_dbus_assert (global_init_done);

330 LeaveCriticalSection (&init_lock);

331}

332

333\#ifdef DBUS_ENABLE_VERBOSE_MODE

334void

335\_dbus_print_thread (void)

336{

337 fprintf (stderr, "%lu: 0x%04lx: ", \_dbus_pid_for_log (), GetCurrentThreadId ());

338}

339\#endif

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_dbus_list_remove

dbus_bool_t \_dbus_list_remove(DBusList \*\*list, void \*data)

Removes a value from the list.

**Definition** dbus-list.c:418

\_dbus_list_pop_first

void \* \_dbus_list_pop_first(DBusList \*\*list)

Removes the first value in the list and returns it.

**Definition** dbus-list.c:679

\_dbus_list_clear

void \_dbus_list_clear(DBusList \*\*list)

Frees all links in the list and sets the list head to NULL.

**Definition** dbus-list.c:545

\_dbus_list_append

dbus_bool_t \_dbus_list_append(DBusList \*\*list, void \*data)

Appends a value to the list.

**Definition** dbus-list.c:273

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

**Definition** dbus-sysdeps-thread-win.c:320

\_dbus_threads_unlock_platform_specific

void \_dbus_threads_unlock_platform_specific(void)

Undo \_dbus_threads_lock_platform_specific().

**Definition** dbus-sysdeps-thread-win.c:327

\_dbus_threads_init_platform_specific

dbus_bool_t \_dbus_threads_init_platform_specific(void)

Initialize threads as in dbus_threads_init_default(), appropriately for the platform.

**Definition** dbus-sysdeps-thread-win.c:304

DBusCMutex

**Definition** dbus-sysdeps-pthread.c:55

DBusCondVar

**Definition** dbus-sysdeps-pthread.c:59

DBusCondVar::lock

CRITICAL_SECTION lock

lock protecting the list

**Definition** dbus-sysdeps-thread-win.c:68

DBusCondVar::list

DBusList \* list

list thread-local-stored events waiting on the cond variable

**Definition** dbus-sysdeps-thread-win.c:67

DBusList

A node in a linked list.

**Definition** dbus-list.h:37

DBusRMutex

**Definition** dbus-sysdeps-pthread.c:51
