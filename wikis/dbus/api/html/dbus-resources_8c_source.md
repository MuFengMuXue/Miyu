dbus-resources.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-resources.c Resource tracking/limits

3 \*

4 \* Copyright (C) 2003 Red Hat Inc.

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

27\#include \<dbus/dbus-resources.h\>

28\#include \<dbus/dbus-internals.h\>

29

56struct DBusCounter

57{

58 int refcount;

60 long size_value;

61 long unix_fd_value;

63\#ifdef DBUS_ENABLE_STATS

64 long peak_size_value;

65 long peak_unix_fd_value;

66\#endif

67

68 long notify_size_guard_value;

69 long notify_unix_fd_guard_value;

71 DBusCounterNotifyFunction notify_function;

72 void \*notify_data;

73 dbus_bool_t notify_pending : 1;

74 DBusRMutex \*mutex;

75};

76

/\* end of resource limits internals docs \*/

78

90DBusCounter\*

91\_dbus_counter_new (void)

92{

93 DBusCounter \*counter;

94

95 counter = dbus_new0 (DBusCounter, 1);

96 if (counter == NULL)

97 return NULL;

98

99 counter-\>refcount = 1;

100

101 \_dbus_rmutex_new_at_location (&counter-\>mutex);

102 if (counter-\>mutex == NULL)

103 {

104 dbus_free (counter);

105 counter = NULL;

106 }

107

108 return counter;

109}

110

117DBusCounter \*

118\_dbus_counter_ref (DBusCounter \*counter)

119{

120 \_dbus_rmutex_lock (counter-\>mutex);

121

122 \_dbus_assert (counter-\>refcount \> 0);

123

124 counter-\>refcount += 1;

125

126 \_dbus_rmutex_unlock (counter-\>mutex);

127

128 return counter;

129}

130

137void

138\_dbus_counter_unref (DBusCounter \*counter)

139{

140 dbus_bool_t last_ref = FALSE;

141

142 \_dbus_rmutex_lock (counter-\>mutex);

143

144 \_dbus_assert (counter-\>refcount \> 0);

145

146 counter-\>refcount -= 1;

147 last_ref = (counter-\>refcount == 0);

148

149 \_dbus_rmutex_unlock (counter-\>mutex);

150

151 if (last_ref)

152 {

153 \_dbus_rmutex_free_at_location (&counter-\>mutex);

154 dbus_free (counter);

155 }

156}

157

168void

169\_dbus_counter_adjust_size (DBusCounter \*counter,

170 long delta)

171{

172 long old = 0;

173

174 \_dbus_rmutex_lock (counter-\>mutex);

175

176 old = counter-\>size_value;

177

178 counter-\>size_value += delta;

179

180\#ifdef DBUS_ENABLE_STATS

181 if (counter-\>peak_size_value \< counter-\>size_value)

182 counter-\>peak_size_value = counter-\>size_value;

183\#endif

184

185\#if 0

186 \_dbus_verbose ("Adjusting counter %ld by %ld = %ld\n",

187 old, delta, counter-\>size_value);

188\#endif

189

190 if (counter-\>notify_function != NULL &&

191 ((old \< counter-\>notify_size_guard_value &&

192 counter-\>size_value \>= counter-\>notify_size_guard_value) \|\|

193 (old \>= counter-\>notify_size_guard_value &&

194 counter-\>size_value \< counter-\>notify_size_guard_value)))

195 counter-\>notify_pending = TRUE;

196

197 \_dbus_rmutex_unlock (counter-\>mutex);

198}

199

208void

209\_dbus_counter_notify (DBusCounter \*counter)

210{

211 DBusCounterNotifyFunction notify_function = NULL;

212 void \*notify_data = NULL;

213

214 \_dbus_rmutex_lock (counter-\>mutex);

215 if (counter-\>notify_pending)

216 {

217 counter-\>notify_pending = FALSE;

218 notify_function = counter-\>notify_function;

219 notify_data = counter-\>notify_data;

220 }

221 \_dbus_rmutex_unlock (counter-\>mutex);

222

223 if (notify_function != NULL)

224 (\* notify_function) (counter, notify_data);

225}

226

237void

238\_dbus_counter_adjust_unix_fd (DBusCounter \*counter,

239 long delta)

240{

241 long old = 0;

242

243 \_dbus_rmutex_lock (counter-\>mutex);

244

245 old = counter-\>unix_fd_value;

246

247 counter-\>unix_fd_value += delta;

248

249\#ifdef DBUS_ENABLE_STATS

250 if (counter-\>peak_unix_fd_value \< counter-\>unix_fd_value)

251 counter-\>peak_unix_fd_value = counter-\>unix_fd_value;

252\#endif

253

254\#if 0

255 \_dbus_verbose ("Adjusting counter %ld by %ld = %ld\n",

256 old, delta, counter-\>unix_fd_value);

257\#endif

258

259 if (counter-\>notify_function != NULL &&

260 ((old \< counter-\>notify_unix_fd_guard_value &&

261 counter-\>unix_fd_value \>= counter-\>notify_unix_fd_guard_value) \|\|

262 (old \>= counter-\>notify_unix_fd_guard_value &&

263 counter-\>unix_fd_value \< counter-\>notify_unix_fd_guard_value)))

264 counter-\>notify_pending = TRUE;

265

266 \_dbus_rmutex_unlock (counter-\>mutex);

267}

268

275long

276\_dbus_counter_get_size_value (DBusCounter \*counter)

277{

278 long result;

279 \_dbus_rmutex_lock (counter-\>mutex);

280 result = counter-\>size_value;

281 \_dbus_rmutex_unlock (counter-\>mutex);

282 return result;

283}

284

291long

292\_dbus_counter_get_unix_fd_value (DBusCounter \*counter)

293{

294 long result;

295 \_dbus_rmutex_lock (counter-\>mutex);

296 result = counter-\>unix_fd_value;

297 \_dbus_rmutex_unlock (counter-\>mutex);

298 return result;

299}

300

312void

313\_dbus_counter_set_notify (DBusCounter \*counter,

314 long size_guard_value,

315 long unix_fd_guard_value,

316 DBusCounterNotifyFunction function,

317 void \*user_data)

318{

319 \_dbus_rmutex_lock (counter-\>mutex);

320 counter-\>notify_size_guard_value = size_guard_value;

321 counter-\>notify_unix_fd_guard_value = unix_fd_guard_value;

322 counter-\>notify_function = function;

323 counter-\>notify_data = user_data;

324 counter-\>notify_pending = FALSE;

325 \_dbus_rmutex_unlock (counter-\>mutex);

326}

327

328\#ifdef DBUS_ENABLE_STATS

329long

330\_dbus_counter_get_peak_size_value (DBusCounter \*counter)

331{

332 return counter-\>peak_size_value;

333}

334

335long

336\_dbus_counter_get_peak_unix_fd_value (DBusCounter \*counter)

337{

338 return counter-\>peak_unix_fd_value;

339}

340\#endif

341

/\* end of resource limits exported API \*/

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

dbus_free

void dbus_free(void \*memory)

Frees a block of memory previously allocated by dbus_malloc() or dbus_malloc0().

**Definition** dbus-memory.c:710

dbus_new0

\#define dbus_new0(type, count)

Safe macro for using dbus_malloc0().

**Definition** dbus-memory.h:60

\_dbus_counter_set_notify

void \_dbus_counter_set_notify(DBusCounter \*counter, long size_guard_value, long unix_fd_guard_value, DBusCounterNotifyFunction function, void \*user_data)

Sets the notify function for this counter; the notify function is called whenever the counter's value...

**Definition** dbus-resources.c:313

\_dbus_counter_new

DBusCounter \* \_dbus_counter_new(void)

Creates a new DBusCounter.

**Definition** dbus-resources.c:91

\_dbus_counter_get_unix_fd_value

long \_dbus_counter_get_unix_fd_value(DBusCounter \*counter)

Gets the current value of the unix fd counter.

**Definition** dbus-resources.c:292

\_dbus_counter_unref

void \_dbus_counter_unref(DBusCounter \*counter)

Decrements refcount of the counter and possibly finalizes the counter.

**Definition** dbus-resources.c:138

\_dbus_counter_get_size_value

long \_dbus_counter_get_size_value(DBusCounter \*counter)

Gets the current value of the size counter.

**Definition** dbus-resources.c:276

\_dbus_counter_adjust_unix_fd

void \_dbus_counter_adjust_unix_fd(DBusCounter \*counter, long delta)

Adjusts the value of the unix fd counter by the given delta which may be positive or negative.

**Definition** dbus-resources.c:238

\_dbus_counter_notify

void \_dbus_counter_notify(DBusCounter \*counter)

Calls the notify function from \_dbus_counter_set_notify(), if that function has been specified and th...

**Definition** dbus-resources.c:209

\_dbus_counter_ref

DBusCounter \* \_dbus_counter_ref(DBusCounter \*counter)

Increments refcount of the counter.

**Definition** dbus-resources.c:118

\_dbus_counter_adjust_size

void \_dbus_counter_adjust_size(DBusCounter \*counter, long delta)

Adjusts the value of the size counter by the given delta which may be positive or negative.

**Definition** dbus-resources.c:169

\_dbus_rmutex_new_at_location

void \_dbus_rmutex_new_at_location(DBusRMutex \*\*location_p)

Creates a new mutex or creates a no-op mutex if threads are not initialized.

**Definition** dbus-threads.c:56

\_dbus_rmutex_unlock

DBUS_PRIVATE_EXPORT void \_dbus_rmutex_unlock(DBusRMutex \*mutex)

Unlocks a mutex.

**Definition** dbus-threads.c:153

\_dbus_rmutex_free_at_location

void \_dbus_rmutex_free_at_location(DBusRMutex \*\*location_p)

Frees a DBusRMutex; does nothing if passed a NULL pointer.

**Definition** dbus-threads.c:97

\_dbus_rmutex_lock

DBUS_PRIVATE_EXPORT void \_dbus_rmutex_lock(DBusRMutex \*mutex)

Locks a mutex.

**Definition** dbus-threads.c:125

DBusCounter

Internals of DBusCounter.

**Definition** dbus-resources.c:57

DBusCounter::refcount

int refcount

reference count

**Definition** dbus-resources.c:58

DBusCounter::notify_data

void \* notify_data

data for notify function

**Definition** dbus-resources.c:72

DBusCounter::notify_function

DBusCounterNotifyFunction notify_function

notify function

**Definition** dbus-resources.c:71

DBusCounter::notify_unix_fd_guard_value

long notify_unix_fd_guard_value

call notify function when crossing this unix fd value

**Definition** dbus-resources.c:69

DBusCounter::notify_pending

dbus_bool_t notify_pending

TRUE if the guard value has been crossed.

**Definition** dbus-resources.c:73

DBusCounter::size_value

long size_value

current size counter value

**Definition** dbus-resources.c:60

DBusCounter::mutex

DBusRMutex \* mutex

Lock on the entire DBusCounter.

**Definition** dbus-resources.c:74

DBusCounter::unix_fd_value

long unix_fd_value

current unix fd counter value

**Definition** dbus-resources.c:61

DBusCounter::notify_size_guard_value

long notify_size_guard_value

call notify function when crossing this size value

**Definition** dbus-resources.c:68

DBusRMutex

**Definition** dbus-sysdeps-pthread.c:51
