dbus-pollable-set-epoll.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-pollable-set-epoll.c - a pollable set implemented via Linux epoll(4)

3 \*

4 \* Copyright © 2011 Nokia Corporation

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

22 \* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,

23 \* MA 02110-1301 USA

24 \*

25 \*/

26

27\#include \<config.h\>

28\#include "dbus-pollable-set.h"

29

30\#include \<dbus/dbus-internals.h\>

31\#include \<dbus/dbus-sysdeps.h\>

32

33\#ifndef \_\_linux\_\_

34\# error This file is for Linux epoll(4)

35\#endif

36

37\#include \<errno.h\>

38\#include \<fcntl.h\>

39\#include \<sys/epoll.h\>

40\#include \<unistd.h\>

41

42\#ifndef DOXYGEN_SHOULD_SKIP_THIS

43

44typedef struct {

45 DBusPollableSet parent;

46 int epfd;

47} DBusPollableSetEpoll;

48

49static inline DBusPollableSetEpoll \*

50socket_set_epoll_cast (DBusPollableSet \*set)

51{

52 \_dbus_assert (set-\>cls == &\_dbus_pollable_set_epoll_class);

53 return (DBusPollableSetEpoll \*) set;

54}

55

56/\* this is safe to call on a partially-allocated socket set \*/

57static void

58socket_set_epoll_free (DBusPollableSet \*set)

59{

60 DBusPollableSetEpoll \*self = socket_set_epoll_cast (set);

61

62 if (self == NULL)

63 return;

64

65 if (self-\>epfd != -1)

66 close (self-\>epfd);

67

68 dbus_free (self);

69}

70

71DBusPollableSet \*

72\_dbus_pollable_set_epoll_new (void)

73{

74 DBusPollableSetEpoll \*self;

75

76 self = dbus_new0 (DBusPollableSetEpoll, 1);

77

78 if (self == NULL)

79 return NULL;

80

81 self-\>parent.cls = &\_dbus_pollable_set_epoll_class;

82

83 self-\>epfd = epoll_create1 (EPOLL_CLOEXEC);

84

85 if (self-\>epfd == -1)

86 {

87 int flags;

88

89 /\* the size hint is ignored unless you have a rather old kernel,

90 \* but must be positive on some versions, so just pick something

91 \* arbitrary; it's a hint, not a limit \*/

92 self-\>epfd = epoll_create (42);

93

94 flags = fcntl (self-\>epfd, F_GETFD, 0);

95

96 if (flags != -1)

97 fcntl (self-\>epfd, F_SETFD, flags \| FD_CLOEXEC);

98 }

99

100 if (self-\>epfd == -1)

101 {

102 socket_set_epoll_free ((DBusPollableSet \*) self);

103 return NULL;

104 }

105

106 return (DBusPollableSet \*) self;

107}

108

109static uint32_t

110watch_flags_to_epoll_events (unsigned int flags)

111{

112 uint32_t events = 0;

113

114 if (flags & DBUS_WATCH_READABLE)

115 events \|= EPOLLIN;

116 if (flags & DBUS_WATCH_WRITABLE)

117 events \|= EPOLLOUT;

118

119 return events;

120}

121

122static unsigned int

123epoll_events_to_watch_flags (uint32_t events)

124{

125 short flags = 0;

126

127 if (events & EPOLLIN)

128 flags \|= DBUS_WATCH_READABLE;

129 if (events & EPOLLOUT)

130 flags \|= DBUS_WATCH_WRITABLE;

131 if (events & EPOLLHUP)

132 flags \|= DBUS_WATCH_HANGUP;

133 if (events & EPOLLERR)

134 flags \|= DBUS_WATCH_ERROR;

135

136 return flags;

137}

138

139static dbus_bool_t

140socket_set_epoll_add (DBusPollableSet \*set,

141 DBusPollable fd,

142 unsigned int flags,

143 dbus_bool_t enabled)

144{

145 DBusPollableSetEpoll \*self = socket_set_epoll_cast (set);

146 struct epoll_event event;

147 int err;

148

149 \_DBUS_ZERO (event);

150 event.data.fd = fd;

151

152 if (enabled)

153 {

154 event.events = watch_flags_to_epoll_events (flags);

155 }

156 else

157 {

158 /\* We need to add \*something\* to reserve space in the kernel's data

159 \* structures: see socket_set_epoll_disable for more details \*/

160 event.events = EPOLLET;

161 }

162

163 if (epoll_ctl (self-\>epfd, EPOLL_CTL_ADD, fd, &event) == 0)

164 return TRUE;

165

166 /\* Anything except ENOMEM, ENOSPC means we have an internal error. \*/

167 err = errno;

168 switch (err)

169 {

170 case ENOMEM:

171 case ENOSPC:

172 /\* be silent: this is basically OOM, which our callers are expected

173 \* to cope with \*/

174 break;

175

176 case EBADF:

177 \_dbus_warn ("Bad fd %d", fd);

178 break;

179

180 case EEXIST:

181 \_dbus_warn ("fd %d added and then added again", fd);

182 break;

183

184 default:

185 \_dbus_warn ("Misc error when trying to watch fd %d: %s", fd,

186 strerror (err));

187 break;

188 }

189

190 return FALSE;

191}

192

193static void

194socket_set_epoll_enable (DBusPollableSet \*set,

195 DBusPollable fd,

196 unsigned int flags)

197{

198 DBusPollableSetEpoll \*self = socket_set_epoll_cast (set);

199 struct epoll_event event;

200 int err;

201

202 \_DBUS_ZERO (event);

203 event.data.fd = fd;

204 event.events = watch_flags_to_epoll_events (flags);

205

206 if (epoll_ctl (self-\>epfd, EPOLL_CTL_MOD, fd, &event) == 0)

207 return;

208

209 err = errno;

210

211 /\* Enabling a file descriptor isn't allowed to fail, even for OOM, so we

212 \* do our best to avoid all of these. \*/

213 switch (err)

214 {

215 case EBADF:

216 \_dbus_warn ("Bad fd %d", fd);

217 break;

218

219 case ENOENT:

220 \_dbus_warn ("fd %d enabled before it was added", fd);

221 break;

222

223 case ENOMEM:

224 \_dbus_warn ("Insufficient memory to change watch for fd %d", fd);

225 break;

226

227 default:

228 \_dbus_warn ("Misc error when trying to watch fd %d: %s", fd,

229 strerror (err));

230 break;

231 }

232}

233

234static void

235socket_set_epoll_disable (DBusPollableSet \*set,

236 DBusPollable fd)

237{

238 DBusPollableSetEpoll \*self = socket_set_epoll_cast (set);

239 struct epoll_event event;

240 int err;

241

242 /\* The naive thing to do would be EPOLL_CTL_DEL, but that'll probably

243 \* free resources in the kernel. When we come to do socket_set_epoll_enable,

244 \* there might not be enough resources to bring it back!

245 \*

246 \* The next idea you might have is to set the flags to 0. However, events

247 \* always trigger on EPOLLERR and EPOLLHUP, even if libdbus isn't actually

248 \* delivering them to a DBusWatch. Because epoll is level-triggered by

249 \* default, we'll busy-loop on an unhandled error or hangup; not good.

250 \*

251 \* So, let's set it to be edge-triggered: then the worst case is that

252 \* we return from poll immediately on one iteration, ignore it because no

253 \* watch is enabled, then go back to normal. When we re-enable a watch

254 \* we'll switch back to level-triggered and be notified again (verified to

255 \* work on 2.6.32). Compile this file with -DTEST_BEHAVIOUR_OF_EPOLLET for

256 \* test code.

257 \*/

258 \_DBUS_ZERO (event);

259 event.data.fd = fd;

260 event.events = EPOLLET;

261

262 if (epoll_ctl (self-\>epfd, EPOLL_CTL_MOD, fd, &event) == 0)

263 return;

264

265 err = errno;

266 \_dbus_warn ("Error when trying to watch fd %d: %s", fd,

267 strerror (err));

268}

269

270static void

271socket_set_epoll_remove (DBusPollableSet \*set,

272 DBusPollable fd)

273{

274 DBusPollableSetEpoll \*self = socket_set_epoll_cast (set);

275 int err;

276 /\* Kernels \< 2.6.9 require a non-NULL struct pointer, even though its

277 \* contents are ignored \*/

278 struct epoll_event dummy;

279 \_DBUS_ZERO (dummy);

280

281 if (epoll_ctl (self-\>epfd, EPOLL_CTL_DEL, fd, &dummy) == 0)

282 return;

283

284 err = errno;

285 \_dbus_warn ("Error when trying to remove fd %d: %s", fd, strerror (err));

286}

287

288/\* Optimally, this should be the same as in DBusLoop: we use it to translate

289 \* between struct epoll_event and DBusSocketEvent without allocating heap

290 \* memory. \*/

291\#define N_STACK_DESCRIPTORS 64

292

293static int

294socket_set_epoll_poll (DBusPollableSet \*set,

295 DBusPollableEvent \*revents,

296 int max_events,

297 int timeout_ms)

298{

299 DBusPollableSetEpoll \*self = socket_set_epoll_cast (set);

300 struct epoll_event events\[N_STACK_DESCRIPTORS\];

301 int n_ready;

302 int i;

303

304 \_dbus_assert (max_events \> 0);

305

306 n_ready = epoll_wait (self-\>epfd, events,

307 MIN (\_DBUS_N_ELEMENTS (events), max_events),

308 timeout_ms);

309

310 if (n_ready \<= 0)

311 return n_ready;

312

313 for (i = 0; i \< n_ready; i++)

314 {

315 revents\[i\].fd = events\[i\].data.fd;

316 revents\[i\].flags = epoll_events_to_watch_flags (events\[i\].events);

317 }

318

319 return n_ready;

320}

321

322DBusPollableSetClass \_dbus_pollable_set_epoll_class = {

323 socket_set_epoll_free,

324 socket_set_epoll_add,

325 socket_set_epoll_remove,

326 socket_set_epoll_enable,

327 socket_set_epoll_disable,

328 socket_set_epoll_poll

329};

330

331\#ifdef TEST_BEHAVIOUR_OF_EPOLLET

332/\* usage: cat /dev/null \| ./epoll

333 \*

334 \* desired output:

335 \* ctl ADD: 0

336 \* wait for HUP, edge-triggered: 1

337 \* wait for HUP again: 0

338 \* ctl MOD: 0

339 \* wait for HUP: 1

340 \*/

341

342\#include \<sys/epoll.h\>

343

344\#include \<stdio.h\>

345

346int

347main (void)

348{

349 struct epoll_event input;

350 struct epoll_event output;

351 int epfd = epoll_create1 (EPOLL_CLOEXEC);

352 int fd = 0; /\* stdin \*/

353 int ret;

354

355 \_DBUS_ZERO (input);

356

357 input.events = EPOLLHUP \| EPOLLET;

358 ret = epoll_ctl (epfd, EPOLL_CTL_ADD, fd, &input);

359 printf ("ctl ADD: %d\n", ret);

360

361 ret = epoll_wait (epfd, &output, 1, -1);

362 printf ("wait for HUP, edge-triggered: %d\n", ret);

363

364 ret = epoll_wait (epfd, &output, 1, 1);

365 printf ("wait for HUP again: %d\n", ret);

366

367 input.events = EPOLLHUP;

368 ret = epoll_ctl (epfd, EPOLL_CTL_MOD, fd, &input);

369 printf ("ctl MOD: %d\n", ret);

370

371 ret = epoll_wait (epfd, &output, 1, -1);

372 printf ("wait for HUP: %d\n", ret);

373

374 return 0;

375}

376

377\#endif /\* TEST_BEHAVIOUR_OF_EPOLLET \*/

378

379\#endif /\* !DOXYGEN_SHOULD_SKIP_THIS \*/

DBUS_WATCH_READABLE

@ DBUS_WATCH_READABLE

As in POLLIN.

**Definition** dbus-connection.h:63

DBUS_WATCH_WRITABLE

@ DBUS_WATCH_WRITABLE

As in POLLOUT.

**Definition** dbus-connection.h:64

DBUS_WATCH_HANGUP

@ DBUS_WATCH_HANGUP

As in POLLHUP (can't watch for it, but can be present in current state passed to dbus_watch_handle())...

**Definition** dbus-connection.h:70

DBUS_WATCH_ERROR

@ DBUS_WATCH_ERROR

As in POLLERR (can't watch for this, but can be present in current state passed to dbus_watch_handle(...

**Definition** dbus-connection.h:65

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_dbus_warn

void \_dbus_warn(const char \*format,...)

Prints a warning message to stderr.

**Definition** dbus-internals.c:278

\_DBUS_N_ELEMENTS

\#define \_DBUS_N_ELEMENTS(array)

Computes the number of elements in a fixed-size array using sizeof().

**Definition** dbus-internals.h:189

\_DBUS_ZERO

\#define \_DBUS_ZERO(object)

Sets all bits in an object to zero.

**Definition** dbus-internals.h:194

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
