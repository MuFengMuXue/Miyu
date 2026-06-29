dbus-timeout.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-timeout.c DBusTimeout implementation

3 \*

4 \* Copyright (C) 2003 CodeFactory AB

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

28\#include "dbus-timeout.h"

29\#include "dbus-list.h"

30

42struct DBusTimeout

43{

44 int refcount;

45 int interval;

47 DBusTimeoutHandler handler;

48 void \*handler_data;

49 DBusFreeFunction free_handler_data_function;

51 void \*data;

52 DBusFreeFunction free_data_function;

53 unsigned int enabled : 1;

54 unsigned int needs_restart : 1;

55};

56

65DBusTimeout\*

66\_dbus_timeout_new (int interval,

67 DBusTimeoutHandler handler,

68 void \*data,

69 DBusFreeFunction free_data_function)

70{

71 DBusTimeout \*timeout;

72

73 timeout = dbus_new0 (DBusTimeout, 1);

74 if (timeout == NULL)

75 return NULL;

76

77 timeout-\>refcount = 1;

78 timeout-\>interval = interval;

79

80 timeout-\>handler = handler;

81 timeout-\>handler_data = data;

82 timeout-\>free_handler_data_function = free_data_function;

83

84 timeout-\>enabled = TRUE;

85 timeout-\>needs_restart = FALSE;

86

87 return timeout;

88}

89

96DBusTimeout \*

97\_dbus_timeout_ref (DBusTimeout \*timeout)

98{

99 timeout-\>refcount += 1;

100

101 return timeout;

102}

103

110void

111\_dbus_timeout_unref (DBusTimeout \*timeout)

112{

113 \_dbus_assert (timeout != NULL);

114 \_dbus_assert (timeout-\>refcount \> 0);

115

116 timeout-\>refcount -= 1;

117 if (timeout-\>refcount == 0)

118 {

119 dbus_timeout_set_data (timeout, NULL, NULL); /\* call free_data_function \*/

120

121 if (timeout-\>free_handler_data_function)

122 (\* timeout-\>free_handler_data_function) (timeout-\>handler_data);

123

124 dbus_free (timeout);

125 }

126}

127

139void

140\_dbus_timeout_restart (DBusTimeout \*timeout,

141 int interval)

142{

143 \_dbus_assert (interval \>= 0);

144

145 timeout-\>interval = interval;

146 timeout-\>enabled = TRUE;

147 timeout-\>needs_restart = TRUE;

148}

149

160void

161\_dbus_timeout_disable (DBusTimeout \*timeout)

162{

163 timeout-\>enabled = FALSE;

164}

165

182struct DBusTimeoutList

183{

184 DBusList \*timeouts;

186 DBusAddTimeoutFunction add_timeout_function;

187 DBusRemoveTimeoutFunction remove_timeout_function;

188 DBusTimeoutToggledFunction timeout_toggled_function;

189 void \*timeout_data;

190 DBusFreeFunction timeout_free_data_function;

191};

192

199DBusTimeoutList\*

200\_dbus_timeout_list_new (void)

201{

202 DBusTimeoutList \*timeout_list;

203

204 timeout_list = dbus_new0 (DBusTimeoutList, 1);

205 if (timeout_list == NULL)

206 return NULL;

207

208 return timeout_list;

209}

210

216void

217\_dbus_timeout_list_free (DBusTimeoutList \*timeout_list)

218{

219 /\* free timeout_data and remove timeouts as a side effect \*/

220 \_dbus_timeout_list_set_functions (timeout_list,

221 NULL, NULL, NULL, NULL, NULL);

222

223 \_dbus_list_clear_full (&timeout_list-\>timeouts,

224 (DBusFreeFunction) \_dbus_timeout_unref);

225

226 dbus_free (timeout_list);

227}

228

242dbus_bool_t

243\_dbus_timeout_list_set_functions (DBusTimeoutList \*timeout_list,

244 DBusAddTimeoutFunction add_function,

245 DBusRemoveTimeoutFunction remove_function,

246 DBusTimeoutToggledFunction toggled_function,

247 void \*data,

248 DBusFreeFunction free_data_function)

249{

250 /\* Add timeouts with the new function, failing on OOM \*/

251 if (add_function != NULL)

252 {

253 DBusList \*link;

254

255 link = \_dbus_list_get_first_link (&timeout_list-\>timeouts);

256 while (link != NULL)

257 {

258 DBusList \*next = \_dbus_list_get_next_link (&timeout_list-\>timeouts,

259 link);

260

261 if (!(\* add_function) (link-\>data, data))

262 {

263 /\* remove it all again and return FALSE \*/

264 DBusList \*link2;

265

266 link2 = \_dbus_list_get_first_link (&timeout_list-\>timeouts);

267 while (link2 != link)

268 {

269 DBusList \*next2 = \_dbus_list_get_next_link (&timeout_list-\>timeouts,

270 link2);

271

272 (\* remove_function) (link2-\>data, data);

273

274 link2 = next2;

275 }

276

277 return FALSE;

278 }

279

280 link = next;

281 }

282 }

283

284 /\* Remove all current timeouts from previous timeout handlers \*/

285

286 if (timeout_list-\>remove_timeout_function != NULL)

287 {

288 \_dbus_list_foreach (&timeout_list-\>timeouts,

289 (DBusForeachFunction) timeout_list-\>remove_timeout_function,

290 timeout_list-\>timeout_data);

291 }

292

293 if (timeout_list-\>timeout_free_data_function != NULL)

294 (\* timeout_list-\>timeout_free_data_function) (timeout_list-\>timeout_data);

295

296 timeout_list-\>add_timeout_function = add_function;

297 timeout_list-\>remove_timeout_function = remove_function;

298 timeout_list-\>timeout_toggled_function = toggled_function;

299 timeout_list-\>timeout_data = data;

300 timeout_list-\>timeout_free_data_function = free_data_function;

301

302 return TRUE;

303}

304

313dbus_bool_t

314\_dbus_timeout_list_add_timeout (DBusTimeoutList \*timeout_list,

315 DBusTimeout \*timeout)

316{

317 if (!\_dbus_list_append (&timeout_list-\>timeouts, timeout))

318 return FALSE;

319

320 \_dbus_timeout_ref (timeout);

321

322 if (timeout_list-\>add_timeout_function != NULL)

323 {

324 if (!(\* timeout_list-\>add_timeout_function) (timeout,

325 timeout_list-\>timeout_data))

326 {

327 \_dbus_list_remove_last (&timeout_list-\>timeouts, timeout);

328 \_dbus_timeout_unref (timeout);

329 return FALSE;

330 }

331 }

332

333 return TRUE;

334}

335

343void

344\_dbus_timeout_list_remove_timeout (DBusTimeoutList \*timeout_list,

345 DBusTimeout \*timeout)

346{

347 if (!\_dbus_list_remove (&timeout_list-\>timeouts, timeout))

348 \_dbus_assert_not_reached ("Nonexistent timeout was removed");

349

350 if (timeout_list-\>remove_timeout_function != NULL)

351 (\* timeout_list-\>remove_timeout_function) (timeout,

352 timeout_list-\>timeout_data);

353

354 \_dbus_timeout_unref (timeout);

355}

356

365void

366\_dbus_timeout_list_toggle_timeout (DBusTimeoutList \*timeout_list,

367 DBusTimeout \*timeout,

368 dbus_bool_t enabled)

369{

370 enabled = !!enabled;

371

372 if (enabled == timeout-\>enabled)

373 return;

374

375 timeout-\>enabled = enabled;

376

377 if (timeout_list-\>timeout_toggled_function != NULL)

378 (\* timeout_list-\>timeout_toggled_function) (timeout,

379 timeout_list-\>timeout_data);

380}

381

388dbus_bool_t

389\_dbus_timeout_needs_restart (DBusTimeout \*timeout)

390{

391 return timeout-\>needs_restart;

392}

393

400void

401\_dbus_timeout_restarted (DBusTimeout \*timeout)

402{

403 timeout-\>needs_restart = FALSE;

404}

405

443int

444dbus_timeout_get_interval (DBusTimeout \*timeout)

445{

446 return timeout-\>interval;

447}

448

456void\*

457dbus_timeout_get_data (DBusTimeout \*timeout)

458{

459 return timeout-\>data;

460}

461

473void

474dbus_timeout_set_data (DBusTimeout \*timeout,

475 void \*data,

476 DBusFreeFunction free_data_function)

477{

478 if (timeout-\>free_data_function != NULL)

479 (\* timeout-\>free_data_function) (timeout-\>data);

480

481 timeout-\>data = data;

482 timeout-\>free_data_function = free_data_function;

483}

484

499dbus_bool_t

500dbus_timeout_handle (DBusTimeout \*timeout)

501{

502 return (\* timeout-\>handler) (timeout-\>handler_data);

503}

504

505

513dbus_bool_t

514dbus_timeout_get_enabled (DBusTimeout \*timeout)

515{

516 return timeout-\>enabled;

517}

518

DBusTimeoutToggledFunction

void(\* DBusTimeoutToggledFunction)(DBusTimeout \*timeout, void \*data)

Called when dbus_timeout_get_enabled() may return a different value than it did before.

**Definition** dbus-connection.h:120

DBusAddTimeoutFunction

dbus_bool_t(\* DBusAddTimeoutFunction)(DBusTimeout \*timeout, void \*data)

Called when libdbus needs a new timeout to be monitored by the main loop.

**Definition** dbus-connection.h:113

DBusRemoveTimeoutFunction

void(\* DBusRemoveTimeoutFunction)(DBusTimeout \*timeout, void \*data)

Called when libdbus no longer needs a timeout to be monitored by the main loop.

**Definition** dbus-connection.h:126

\_dbus_assert_not_reached

\#define \_dbus_assert_not_reached(explanation)

Aborts with an error message if called.

**Definition** dbus-internals.h:164

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_dbus_list_get_first_link

DBusList \* \_dbus_list_get_first_link(DBusList \*\*list)

Gets the first link in the list.

**Definition** dbus-list.c:597

\_dbus_list_remove

dbus_bool_t \_dbus_list_remove(DBusList \*\*list, void \*data)

Removes a value from the list.

**Definition** dbus-list.c:418

\_dbus_list_clear_full

void \_dbus_list_clear_full(DBusList \*\*list, DBusFreeFunction function)

Free every link and every element in the list.

**Definition** dbus-list.c:570

\_dbus_list_foreach

void \_dbus_list_foreach(DBusList \*\*list, DBusForeachFunction function, void \*data)

Calls the given function for each element in the list.

**Definition** dbus-list.c:789

\_dbus_list_remove_last

dbus_bool_t \_dbus_list_remove_last(DBusList \*\*list, void \*data)

Removes a value from the list.

**Definition** dbus-list.c:449

\_dbus_list_append

dbus_bool_t \_dbus_list_append(DBusList \*\*list, void \*data)

Appends a value to the list.

**Definition** dbus-list.c:273

\_dbus_list_get_next_link

\#define \_dbus_list_get_next_link(list, link)

Gets the next link in the list, or NULL if there are no more links.

**Definition** dbus-list.h:121

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

DBusFreeFunction

void(\* DBusFreeFunction)(void \*memory)

The type of a function which frees a block of memory.

**Definition** dbus-memory.h:65

dbus_free

void dbus_free(void \*memory)

Frees a block of memory previously allocated by dbus_malloc() or dbus_malloc0().

**Definition** dbus-memory.c:710

dbus_new0

\#define dbus_new0(type, count)

Safe macro for using dbus_malloc0().

**Definition** dbus-memory.h:60

\_dbus_timeout_list_add_timeout

dbus_bool_t \_dbus_timeout_list_add_timeout(DBusTimeoutList \*timeout_list, DBusTimeout \*timeout)

Adds a new timeout to the timeout list, invoking the application DBusAddTimeoutFunction if appropriat...

**Definition** dbus-timeout.c:314

\_dbus_timeout_list_free

void \_dbus_timeout_list_free(DBusTimeoutList \*timeout_list)

Frees a DBusTimeoutList.

**Definition** dbus-timeout.c:217

\_dbus_timeout_list_toggle_timeout

void \_dbus_timeout_list_toggle_timeout(DBusTimeoutList \*timeout_list, DBusTimeout \*timeout, dbus_bool_t enabled)

Sets a timeout to the given enabled state, invoking the application's DBusTimeoutToggledFunction if a...

**Definition** dbus-timeout.c:366

\_dbus_timeout_list_new

DBusTimeoutList \* \_dbus_timeout_list_new(void)

Creates a new timeout list.

**Definition** dbus-timeout.c:200

\_dbus_timeout_unref

void \_dbus_timeout_unref(DBusTimeout \*timeout)

Decrements the reference count of a DBusTimeout object and finalizes the object if the count reaches ...

**Definition** dbus-timeout.c:111

\_dbus_timeout_list_set_functions

dbus_bool_t \_dbus_timeout_list_set_functions(DBusTimeoutList \*timeout_list, DBusAddTimeoutFunction add_function, DBusRemoveTimeoutFunction remove_function, DBusTimeoutToggledFunction toggled_function, void \*data, DBusFreeFunction free_data_function)

Sets the timeout functions.

**Definition** dbus-timeout.c:243

\_dbus_timeout_disable

void \_dbus_timeout_disable(DBusTimeout \*timeout)

Disable the timeout.

**Definition** dbus-timeout.c:161

\_dbus_timeout_new

DBusTimeout \* \_dbus_timeout_new(int interval, DBusTimeoutHandler handler, void \*data, DBusFreeFunction free_data_function)

Creates a new DBusTimeout, enabled by default.

**Definition** dbus-timeout.c:66

\_dbus_timeout_restart

void \_dbus_timeout_restart(DBusTimeout \*timeout, int interval)

Change the timeout interval to be interval milliseconds from now (forgetting when the timeout was ini...

**Definition** dbus-timeout.c:140

DBusTimeoutHandler

dbus_bool_t(\* DBusTimeoutHandler)(void \*data)

function to run when the timeout is handled

**Definition** dbus-timeout.h:43

\_dbus_timeout_ref

DBusTimeout \* \_dbus_timeout_ref(DBusTimeout \*timeout)

Increments the reference count of a DBusTimeout object.

**Definition** dbus-timeout.c:97

\_dbus_timeout_restarted

void \_dbus_timeout_restarted(DBusTimeout \*timeout)

Mark timeout as restarted (setting timestamps is responsibility of the event loop).

**Definition** dbus-timeout.c:401

\_dbus_timeout_list_remove_timeout

void \_dbus_timeout_list_remove_timeout(DBusTimeoutList \*timeout_list, DBusTimeout \*timeout)

Removes a timeout from the timeout list, invoking the application's DBusRemoveTimeoutFunction if appr...

**Definition** dbus-timeout.c:344

\_dbus_timeout_needs_restart

dbus_bool_t \_dbus_timeout_needs_restart(DBusTimeout \*timeout)

Returns whether a timeout needs restart time counting in the event loop.

**Definition** dbus-timeout.c:389

dbus_timeout_handle

DBUS_EXPORT dbus_bool_t dbus_timeout_handle(DBusTimeout \*timeout)

Calls the timeout handler for this timeout.

**Definition** dbus-timeout.c:500

dbus_timeout_get_enabled

DBUS_EXPORT dbus_bool_t dbus_timeout_get_enabled(DBusTimeout \*timeout)

Returns whether a timeout is enabled or not.

**Definition** dbus-timeout.c:514

dbus_timeout_get_interval

DBUS_EXPORT int dbus_timeout_get_interval(DBusTimeout \*timeout)

Gets the timeout interval.

**Definition** dbus-timeout.c:444

dbus_timeout_get_data

DBUS_EXPORT void \* dbus_timeout_get_data(DBusTimeout \*timeout)

Gets data previously set with dbus_timeout_set_data() or NULL if none.

**Definition** dbus-timeout.c:457

dbus_timeout_set_data

DBUS_EXPORT void dbus_timeout_set_data(DBusTimeout \*timeout, void \*data, DBusFreeFunction free_data_function)

Sets data which can be retrieved with dbus_timeout_get_data().

**Definition** dbus-timeout.c:474

DBusList

A node in a linked list.

**Definition** dbus-list.h:37

DBusList::data

void \* data

Data stored at this element.

**Definition** dbus-list.h:40

DBusTimeoutList

DBusTimeoutList implementation details.

**Definition** dbus-timeout.c:183

DBusTimeoutList::timeout_toggled_function

DBusTimeoutToggledFunction timeout_toggled_function

Callback when timeout is enabled/disabled or changes interval.

**Definition** dbus-timeout.c:188

DBusTimeoutList::remove_timeout_function

DBusRemoveTimeoutFunction remove_timeout_function

Callback for removing a timeout.

**Definition** dbus-timeout.c:187

DBusTimeoutList::timeouts

DBusList \* timeouts

Timeout objects.

**Definition** dbus-timeout.c:184

DBusTimeoutList::add_timeout_function

DBusAddTimeoutFunction add_timeout_function

Callback for adding a timeout.

**Definition** dbus-timeout.c:186

DBusTimeoutList::timeout_free_data_function

DBusFreeFunction timeout_free_data_function

Free function for timeout callback data.

**Definition** dbus-timeout.c:190

DBusTimeoutList::timeout_data

void \* timeout_data

Data for timeout callbacks.

**Definition** dbus-timeout.c:189

DBusTimeout

Internals of DBusTimeout.

**Definition** dbus-timeout.c:43

DBusTimeout::data

void \* data

Application data.

**Definition** dbus-timeout.c:51

DBusTimeout::refcount

int refcount

Reference count.

**Definition** dbus-timeout.c:44

DBusTimeout::enabled

unsigned int enabled

True if timeout is active.

**Definition** dbus-timeout.c:53

DBusTimeout::handler

DBusTimeoutHandler handler

Timeout handler.

**Definition** dbus-timeout.c:47

DBusTimeout::handler_data

void \* handler_data

Timeout handler data.

**Definition** dbus-timeout.c:48

DBusTimeout::interval

int interval

Timeout interval in milliseconds.

**Definition** dbus-timeout.c:45

DBusTimeout::needs_restart

unsigned int needs_restart

Flag that timeout should be restarted after re-enabling.

**Definition** dbus-timeout.c:54

DBusTimeout::free_handler_data_function

DBusFreeFunction free_handler_data_function

Free the timeout handler data.

**Definition** dbus-timeout.c:49

DBusTimeout::free_data_function

DBusFreeFunction free_data_function

Free the application data.

**Definition** dbus-timeout.c:52
