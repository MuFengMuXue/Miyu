dbus-pollable-set-poll.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-pollable-set-poll.c - a pollable set implemented via \_dbus_poll

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

31\#include \<dbus/dbus-list.h\>

32\#include \<dbus/dbus-sysdeps.h\>

33\#include \<dbus/dbus-watch.h\>

34

35\#ifndef DOXYGEN_SHOULD_SKIP_THIS

36

37typedef struct {

38 DBusPollableSet parent;

39 DBusPollFD \*fds;

40 int n_fds;

41 int n_reserved;

42 int n_allocated;

43} DBusPollableSetPoll;

44

45\#define REALLOC_INCREMENT 8

46\#define MINIMUM_SIZE 8

47

48/\* If we're in the regression tests, force reallocation to happen sooner \*/

49\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

50\#define DEFAULT_SIZE_HINT 1

51\#else

52\#define DEFAULT_SIZE_HINT MINIMUM_SIZE

53\#endif

54

55static inline DBusPollableSetPoll \*

56socket_set_poll_cast (DBusPollableSet \*set)

57{

58 \_dbus_assert (set-\>cls == &\_dbus_pollable_set_poll_class);

59 return (DBusPollableSetPoll \*) set;

60}

61

62/\* this is safe to call on a partially-allocated socket set \*/

63static void

64socket_set_poll_free (DBusPollableSet \*set)

65{

66 DBusPollableSetPoll \*self = socket_set_poll_cast (set);

67

68 dbus_free (self-\>fds);

69 dbus_free (self);

70 \_dbus_verbose ("freed socket set %p\n", self);

71}

72

73DBusPollableSet \*

74\_dbus_pollable_set_poll_new (int size_hint)

75{

76 DBusPollableSetPoll \*ret;

77

78 if (size_hint \<= 0)

79 size_hint = DEFAULT_SIZE_HINT;

80

81 ret = dbus_new0 (DBusPollableSetPoll, 1);

82

83 if (ret == NULL)

84 return NULL;

85

86 ret-\>parent.cls = &\_dbus_pollable_set_poll_class;

87 ret-\>n_fds = 0;

88 ret-\>n_allocated = size_hint;

89

90 ret-\>fds = dbus_new0 (DBusPollFD, size_hint);

91

92 if (ret-\>fds == NULL)

93 {

94 /\* socket_set_poll_free specifically supports half-constructed

95 \* socket sets \*/

96 socket_set_poll_free ((DBusPollableSet \*) ret);

97 return NULL;

98 }

99

100 \_dbus_verbose ("new socket set at %p\n", ret);

101 return (DBusPollableSet \*) ret;

102}

103

104static short

105watch_flags_to_poll_events (unsigned int flags)

106{

107 short events = 0;

108

109 if (flags & DBUS_WATCH_READABLE)

110 events \|= \_DBUS_POLLIN;

111 if (flags & DBUS_WATCH_WRITABLE)

112 events \|= \_DBUS_POLLOUT;

113

114 return events;

115}

116

117static dbus_bool_t

118socket_set_poll_add (DBusPollableSet \*set,

119 DBusPollable fd,

120 unsigned int flags,

121 dbus_bool_t enabled)

122{

123 DBusPollableSetPoll \*self = socket_set_poll_cast (set);

124\#ifndef DBUS_DISABLE_ASSERT

125 int i;

126

127 for (i = 0; i \< self-\>n_fds; i++)

128 \_dbus_assert (!\_dbus_pollable_equals (self-\>fds\[i\].fd, fd));

129\#endif

130

131 if (self-\>n_reserved \>= self-\>n_allocated)

132 {

133 DBusPollFD \*new_fds = dbus_realloc (self-\>fds,

134 sizeof (DBusPollFD) \* (self-\>n_allocated + REALLOC_INCREMENT));

135

136 \_dbus_verbose ("inflating set %p from %d en/%d res/%d alloc to %d\n",

137 self, self-\>n_fds, self-\>n_reserved, self-\>n_allocated,

138 self-\>n_allocated + REALLOC_INCREMENT);

139

140 if (new_fds == NULL)

141 return FALSE;

142

143 self-\>fds = new_fds;

144 self-\>n_allocated += REALLOC_INCREMENT;

145 }

146

147 \_dbus_verbose ("before adding fd %" DBUS_POLLABLE_FORMAT " to %p, %d en/%d res/%d alloc\n",

148 \_dbus_pollable_printable (fd), self, self-\>n_fds, self-\>n_reserved, self-\>n_allocated);

149 \_dbus_assert (self-\>n_reserved \>= self-\>n_fds);

150 \_dbus_assert (self-\>n_allocated \> self-\>n_reserved);

151

152 self-\>n_reserved++;

153

154 if (enabled)

155 {

156 self-\>fds\[self-\>n_fds\].fd = fd;

157 self-\>fds\[self-\>n_fds\].events = watch_flags_to_poll_events (flags);

158 self-\>n_fds++;

159 }

160

161 return TRUE;

162}

163

164static void

165socket_set_poll_enable (DBusPollableSet \*set,

166 DBusPollable fd,

167 unsigned int flags)

168{

169 DBusPollableSetPoll \*self = socket_set_poll_cast (set);

170 int i;

171

172 for (i = 0; i \< self-\>n_fds; i++)

173 {

174 if (\_dbus_pollable_equals (self-\>fds\[i\].fd, fd))

175 {

176 self-\>fds\[i\].events = watch_flags_to_poll_events (flags);

177 return;

178 }

179 }

180

181 /\* we allocated space when the socket was added \*/

182 \_dbus_assert (self-\>n_fds \< self-\>n_reserved);

183 \_dbus_assert (self-\>n_reserved \<= self-\>n_allocated);

184

185 self-\>fds\[self-\>n_fds\].fd = fd;

186 self-\>fds\[self-\>n_fds\].events = watch_flags_to_poll_events (flags);

187 self-\>n_fds++;

188}

189

190static void

191socket_set_poll_disable (DBusPollableSet \*set,

192 DBusPollable fd)

193{

194 DBusPollableSetPoll \*self = socket_set_poll_cast (set);

195 int i;

196

197 for (i = 0; i \< self-\>n_fds; i++)

198 {

199 if (\_dbus_pollable_equals (self-\>fds\[i\].fd, fd))

200 {

201 if (i != self-\>n_fds - 1)

202 {

203 self-\>fds\[i\].fd = self-\>fds\[self-\>n_fds - 1\].fd;

204 self-\>fds\[i\].events = self-\>fds\[self-\>n_fds - 1\].events;

205 }

206

207 self-\>n_fds--;

208 return;

209 }

210 }

211}

212

213static void

214socket_set_poll_remove (DBusPollableSet \*set,

215 DBusPollable fd)

216{

217 DBusPollableSetPoll \*self = socket_set_poll_cast (set);

218

219 socket_set_poll_disable (set, fd);

220 self-\>n_reserved--;

221

222 \_dbus_verbose ("after removing fd %" DBUS_POLLABLE_FORMAT " from %p, %d en/%d res/%d alloc\n",

223 \_dbus_pollable_printable (fd), self, self-\>n_fds, self-\>n_reserved, self-\>n_allocated);

224 \_dbus_assert (self-\>n_fds \<= self-\>n_reserved);

225 \_dbus_assert (self-\>n_reserved \<= self-\>n_allocated);

226

227 if (self-\>n_reserved + MINIMUM_SIZE \< self-\>n_allocated / 2)

228 {

229 /\* Our array is twice as big as it needs to be - deflate it until it's

230 \* only slightly larger than the number reserved. \*/

231 DBusPollFD \*new_fds = dbus_realloc (self-\>fds,

232 sizeof (DBusPollFD) \* (self-\>n_reserved + MINIMUM_SIZE));

233

234 \_dbus_verbose ("before deflating %p, %d en/%d res/%d alloc\n",

235 self, self-\>n_fds, self-\>n_reserved, self-\>n_allocated);

236

237 if (\_DBUS_UNLIKELY (new_fds == NULL))

238 {

239 /\* Weird. Oh well, never mind, the too-big array is untouched \*/

240 return;

241 }

242

243 self-\>fds = new_fds;

244 self-\>n_allocated = self-\>n_reserved;

245 }

246}

247

248static unsigned int

249watch_flags_from_poll_revents (short revents)

250{

251 unsigned int condition = 0;

252

253 if (revents & \_DBUS_POLLIN)

254 condition \|= DBUS_WATCH_READABLE;

255 if (revents & \_DBUS_POLLOUT)

256 condition \|= DBUS_WATCH_WRITABLE;

257 if (revents & \_DBUS_POLLHUP)

258 condition \|= DBUS_WATCH_HANGUP;

259 if (revents & \_DBUS_POLLERR)

260 condition \|= DBUS_WATCH_ERROR;

261

262 if (\_DBUS_UNLIKELY (revents & \_DBUS_POLLNVAL))

263 condition \|= \_DBUS_WATCH_NVAL;

264

265 return condition;

266}

267

270static int

271socket_set_poll_poll (DBusPollableSet \*set,

272 DBusPollableEvent \*revents,

273 int max_events,

274 int timeout_ms)

275{

276 DBusPollableSetPoll \*self = socket_set_poll_cast (set);

277 int i;

278 int n_events;

279 int n_ready;

280

281 \_dbus_assert (max_events \> 0);

282

283 for (i = 0; i \< self-\>n_fds; i++)

284 self-\>fds\[i\].revents = 0;

285

286 n_ready = \_dbus_poll (self-\>fds, self-\>n_fds, timeout_ms);

287

288 if (n_ready \<= 0)

289 return n_ready;

290

291 n_events = 0;

292

293 for (i = 0; i \< self-\>n_fds; i++)

294 {

295 if (self-\>fds\[i\].revents != 0)

296 {

297 revents\[n_events\].fd = self-\>fds\[i\].fd;

298 revents\[n_events\].flags = watch_flags_from_poll_revents (self-\>fds\[i\].revents);

299

300 n_events += 1;

301

302 /\* We ignore events beyond max_events because we have nowhere to

303 \* put them. \_dbus_poll is level-triggered, so we'll just be told

304 \* about them next time round the main loop anyway. \*/

305 if (n_events == max_events)

306 return n_events;

307 }

308 }

309

310 return n_events;

311}

312

313DBusPollableSetClass \_dbus_pollable_set_poll_class = {

314 socket_set_poll_free,

315 socket_set_poll_add,

316 socket_set_poll_remove,

317 socket_set_poll_enable,

318 socket_set_poll_disable,

319 socket_set_poll_poll

320};

321

322\#endif /\* !DOXYGEN_SHOULD_SKIP_THIS \*/

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

dbus_realloc

void \* dbus_realloc(void \*memory, size_t bytes)

Resizes a block of memory previously allocated by dbus_malloc() or dbus_malloc0().

**Definition** dbus-memory.c:610

dbus_new0

\#define dbus_new0(type, count)

Safe macro for using dbus_malloc0().

**Definition** dbus-memory.h:60

\_DBUS_POLLOUT

\#define \_DBUS_POLLOUT

Writing now will not block.

**Definition** dbus-sysdeps.h:448

\_DBUS_POLLERR

\#define \_DBUS_POLLERR

Error condition.

**Definition** dbus-sysdeps.h:450

\_DBUS_POLLHUP

\#define \_DBUS_POLLHUP

Hung up.

**Definition** dbus-sysdeps.h:452

\_DBUS_POLLNVAL

\#define \_DBUS_POLLNVAL

Invalid request: fd not open.

**Definition** dbus-sysdeps.h:454

\_DBUS_POLLIN

\#define \_DBUS_POLLIN

There is data to read.

**Definition** dbus-sysdeps.h:444

\_dbus_poll

int \_dbus_poll(DBusPollFD \*fds, int n_fds, int timeout_milliseconds)

Wrapper for poll().

**Definition** dbus-sysdeps-unix.c:3303

DBusPollFD

**Definition** dbus-sysdeps.h:437
