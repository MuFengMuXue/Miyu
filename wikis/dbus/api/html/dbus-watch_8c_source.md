dbus-watch.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-watch.c DBusWatch implementation

3 \*

4 \* Copyright (C) 2002, 2003 Red Hat Inc.

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

28\#include "dbus-watch.h"

29\#include "dbus-list.h"

30

42struct DBusWatch

43{

44 int refcount;

45 DBusPollable fd;

46 unsigned int flags;

48 DBusWatchHandler handler;

49 void \*handler_data;

50 DBusFreeFunction free_handler_data_function;

52 void \*data;

53 DBusFreeFunction free_data_function;

54 unsigned int enabled : 1;

55 unsigned int oom_last_time : 1;

56};

57

58dbus_bool_t

59\_dbus_watch_get_enabled (DBusWatch \*watch)

60{

61 return watch-\>enabled;

62}

63

64dbus_bool_t

65\_dbus_watch_get_oom_last_time (DBusWatch \*watch)

66{

67 return watch-\>oom_last_time;

68}

69

70void

71\_dbus_watch_set_oom_last_time (DBusWatch \*watch,

72 dbus_bool_t oom)

73{

74 watch-\>oom_last_time = oom;

75}

76

89DBusWatch\*

90\_dbus_watch_new (DBusPollable fd,

91 unsigned int flags,

92 dbus_bool_t enabled,

93 DBusWatchHandler handler,

94 void \*data,

95 DBusFreeFunction free_data_function)

96{

97 DBusWatch \*watch;

98

99\#define VALID_WATCH_FLAGS (DBUS_WATCH_WRITABLE \| DBUS_WATCH_READABLE)

100

101 \_dbus_assert ((flags & VALID_WATCH_FLAGS) == flags);

102

103 watch = dbus_new0 (DBusWatch, 1);

104 if (watch == NULL)

105 return NULL;

106

107 watch-\>refcount = 1;

108 watch-\>fd = fd;

109 watch-\>flags = flags;

110 watch-\>enabled = enabled;

111

112 watch-\>handler = handler;

113 watch-\>handler_data = data;

114 watch-\>free_handler_data_function = free_data_function;

115

116 return watch;

117}

118

125DBusWatch \*

126\_dbus_watch_ref (DBusWatch \*watch)

127{

128 watch-\>refcount += 1;

129

130 return watch;

131}

132

139void

140\_dbus_watch_unref (DBusWatch \*watch)

141{

142 \_dbus_assert (watch != NULL);

143 \_dbus_assert (watch-\>refcount \> 0);

144

145 watch-\>refcount -= 1;

146 if (watch-\>refcount == 0)

147 {

148 if (\_dbus_pollable_is_valid (watch-\>fd))

149 \_dbus_warn ("this watch should have been invalidated");

150

151 dbus_watch_set_data (watch, NULL, NULL); /\* call free_data_function \*/

152

153 if (watch-\>free_handler_data_function)

154 (\* watch-\>free_handler_data_function) (watch-\>handler_data);

155

156 dbus_free (watch);

157 }

158}

159

170void

171\_dbus_watch_invalidate (DBusWatch \*watch)

172{

173 \_dbus_pollable_invalidate (&watch-\>fd);

174 watch-\>flags = 0;

175}

176

186void

187\_dbus_watch_sanitize_condition (DBusWatch \*watch,

188 unsigned int \*condition)

189{

190 if (!(watch-\>flags & DBUS_WATCH_READABLE))

191 \*condition &= ~DBUS_WATCH_READABLE;

192 if (!(watch-\>flags & DBUS_WATCH_WRITABLE))

193 \*condition &= ~DBUS_WATCH_WRITABLE;

194}

195

196

216struct DBusWatchList

217{

218 DBusList \*watches;

220 DBusAddWatchFunction add_watch_function;

221 DBusRemoveWatchFunction remove_watch_function;

222 DBusWatchToggledFunction watch_toggled_function;

223 void \*watch_data;

224 DBusFreeFunction watch_free_data_function;

225};

226

233DBusWatchList\*

234\_dbus_watch_list_new (void)

235{

236 DBusWatchList \*watch_list;

237

238 watch_list = dbus_new0 (DBusWatchList, 1);

239 if (watch_list == NULL)

240 return NULL;

241

242 return watch_list;

243}

244

250void

251\_dbus_watch_list_free (DBusWatchList \*watch_list)

252{

253 /\* free watch_data and removes watches as a side effect \*/

254 \_dbus_watch_list_set_functions (watch_list,

255 NULL, NULL, NULL, NULL, NULL);

256

257 \_dbus_list_clear_full (&watch_list-\>watches,

258 (DBusFreeFunction) \_dbus_watch_unref);

259

260 dbus_free (watch_list);

261}

262

263\#ifdef DBUS_ENABLE_VERBOSE_MODE

264static const char\*

265watch_flags_to_string (int flags)

266{

267 const char \*watch_type;

268

269 if ((flags & DBUS_WATCH_READABLE) &&

270 (flags & DBUS_WATCH_WRITABLE))

271 watch_type = "readwrite";

272 else if (flags & DBUS_WATCH_READABLE)

273 watch_type = "read";

274 else if (flags & DBUS_WATCH_WRITABLE)

275 watch_type = "write";

276 else

277 watch_type = "not read or write";

278 return watch_type;

279}

280\#endif /\* DBUS_ENABLE_VERBOSE_MODE \*/

281

296dbus_bool_t

297\_dbus_watch_list_set_functions (DBusWatchList \*watch_list,

298 DBusAddWatchFunction add_function,

299 DBusRemoveWatchFunction remove_function,

300 DBusWatchToggledFunction toggled_function,

301 void \*data,

302 DBusFreeFunction free_data_function)

303{

304 /\* Add watches with the new watch function, failing on OOM \*/

305 if (add_function != NULL)

306 {

307 DBusList \*link;

308

309 link = \_dbus_list_get_first_link (&watch_list-\>watches);

310 while (link != NULL)

311 {

312 DBusList \*next = \_dbus_list_get_next_link (&watch_list-\>watches,

313 link);

314\#ifdef DBUS_ENABLE_VERBOSE_MODE

315 DBusWatch \*watch = link-\>data;

316

317 \_dbus_verbose ("Adding a %s watch on fd %" DBUS_POLLABLE_FORMAT " using newly-set add watch function\n",

318 watch_flags_to_string (dbus_watch_get_flags (link-\>data)),

319 \_dbus_pollable_printable (watch-\>fd));

320\#endif

321

322 if (!(\* add_function) (link-\>data, data))

323 {

324 /\* remove it all again and return FALSE \*/

325 DBusList \*link2;

326

327 link2 = \_dbus_list_get_first_link (&watch_list-\>watches);

328 while (link2 != link)

329 {

330 DBusList \*next2 = \_dbus_list_get_next_link (&watch_list-\>watches,

331 link2);

332\#ifdef DBUS_ENABLE_VERBOSE_MODE

333 DBusWatch \*watch2 = link2-\>data;

334

335 \_dbus_verbose ("Removing watch on fd %" DBUS_POLLABLE_FORMAT " using newly-set remove function because initial add failed\n",

336 \_dbus_pollable_printable (watch2-\>fd));

337\#endif

338

339 (\* remove_function) (link2-\>data, data);

340

341 link2 = next2;

342 }

343

344 return FALSE;

345 }

346

347 link = next;

348 }

349 }

350

351 /\* Remove all current watches from previous watch handlers \*/

352

353 if (watch_list-\>remove_watch_function != NULL)

354 {

355 \_dbus_verbose ("Removing all pre-existing watches\n");

356

357 \_dbus_list_foreach (&watch_list-\>watches,

358 (DBusForeachFunction) watch_list-\>remove_watch_function,

359 watch_list-\>watch_data);

360 }

361

362 if (watch_list-\>watch_free_data_function != NULL)

363 (\* watch_list-\>watch_free_data_function) (watch_list-\>watch_data);

364

365 watch_list-\>add_watch_function = add_function;

366 watch_list-\>remove_watch_function = remove_function;

367 watch_list-\>watch_toggled_function = toggled_function;

368 watch_list-\>watch_data = data;

369 watch_list-\>watch_free_data_function = free_data_function;

370

371 return TRUE;

372}

373

382dbus_bool_t

383\_dbus_watch_list_add_watch (DBusWatchList \*watch_list,

384 DBusWatch \*watch)

385{

386 if (!\_dbus_list_append (&watch_list-\>watches, watch))

387 return FALSE;

388

389 \_dbus_watch_ref (watch);

390

391 if (watch_list-\>add_watch_function != NULL)

392 {

393 \_dbus_verbose ("Adding watch on fd %" DBUS_POLLABLE_FORMAT "\n",

394 \_dbus_pollable_printable (watch-\>fd));

395

396 if (!(\* watch_list-\>add_watch_function) (watch,

397 watch_list-\>watch_data))

398 {

399 \_dbus_list_remove_last (&watch_list-\>watches, watch);

400 \_dbus_watch_unref (watch);

401 return FALSE;

402 }

403 }

404

405 return TRUE;

406}

407

415void

416\_dbus_watch_list_remove_watch (DBusWatchList \*watch_list,

417 DBusWatch \*watch)

418{

419 if (!\_dbus_list_remove (&watch_list-\>watches, watch))

420 \_dbus_assert_not_reached ("Nonexistent watch was removed");

421

422 if (watch_list-\>remove_watch_function != NULL)

423 {

424 \_dbus_verbose ("Removing watch on fd %" DBUS_POLLABLE_FORMAT "\n",

425 \_dbus_pollable_printable (watch-\>fd));

426

427 (\* watch_list-\>remove_watch_function) (watch,

428 watch_list-\>watch_data);

429 }

430

431 \_dbus_watch_unref (watch);

432}

433

442void

443\_dbus_watch_list_toggle_watch (DBusWatchList \*watch_list,

444 DBusWatch \*watch,

445 dbus_bool_t enabled)

446{

447 enabled = !!enabled;

448

449 if (enabled == watch-\>enabled)

450 return;

451

452 watch-\>enabled = enabled;

453

454 if (watch_list-\>watch_toggled_function != NULL)

455 {

456 \_dbus_verbose ("Toggling watch %p on fd %" DBUS_POLLABLE_FORMAT " to %d\n",

457 watch,

458 \_dbus_pollable_printable (watch-\>fd),

459 watch-\>enabled);

460

461 (\* watch_list-\>watch_toggled_function) (watch,

462 watch_list-\>watch_data);

463 }

464}

465

473void

474\_dbus_watch_list_toggle_all_watches (DBusWatchList \*watch_list,

475 dbus_bool_t enabled)

476{

477 DBusList \*link;

478

479 for (link = \_dbus_list_get_first_link (&watch_list-\>watches);

480 link != NULL;

481 link = \_dbus_list_get_next_link (&watch_list-\>watches, link))

482 {

483 \_dbus_watch_list_toggle_watch (watch_list, link-\>data, enabled);

484 }

485}

486

499void

500\_dbus_watch_set_handler (DBusWatch \*watch,

501 DBusWatchHandler handler,

502 void \*data,

503 DBusFreeFunction free_data_function)

504{

505 if (watch-\>free_handler_data_function)

506 (\* watch-\>free_handler_data_function) (watch-\>handler_data);

507

508 watch-\>handler = handler;

509 watch-\>handler_data = data;

510 watch-\>free_handler_data_function = free_data_function;

511}

512

544int

545dbus_watch_get_fd (DBusWatch \*watch)

546{

547 \_dbus_return_val_if_fail (watch != NULL, -1);

548

549 return dbus_watch_get_unix_fd(watch);

550}

551

565int

566dbus_watch_get_unix_fd (DBusWatch \*watch)

567{

568 \_dbus_return_val_if_fail (watch != NULL, -1);

569

570 /\* FIXME remove \#ifdef and do this on a lower level

571 \* (watch should have set_socket and set_unix_fd and track

572 \* which it has, and the transport should provide the

573 \* appropriate watch type)

574 \*/

575\#ifdef DBUS_UNIX

576 return watch-\>fd;

577\#else

578 return dbus_watch_get_socket( watch );

579\#endif

580}

581

594int

595dbus_watch_get_socket (DBusWatch \*watch)

596{

597 \_dbus_return_val_if_fail (watch != NULL, -1);

598

599\#ifdef DBUS_UNIX

600 return watch-\>fd;

601\#else

602 return \_dbus_socket_get_int (watch-\>fd);

603\#endif

604}

605

606DBusSocket

607\_dbus_watch_get_socket (DBusWatch \*watch)

608{

609 DBusSocket s;

610

611 \_dbus_assert (watch != NULL);

612

613\#ifdef DBUS_UNIX

614 s.fd = watch-\>fd;

615\#else

616 s = watch-\>fd;

617\#endif

618

619 return s;

620}

621

622DBusPollable

623\_dbus_watch_get_pollable (DBusWatch \*watch)

624{

625 \_dbus_assert (watch != NULL);

626

627 return watch-\>fd;

628}

629

643unsigned int

644dbus_watch_get_flags (DBusWatch \*watch)

645{

646 \_dbus_return_val_if_fail (watch != NULL, 0);

647 \_dbus_assert ((watch-\>flags & VALID_WATCH_FLAGS) == watch-\>flags);

648

649 return watch-\>flags;

650}

651

659void\*

660dbus_watch_get_data (DBusWatch \*watch)

661{

662 \_dbus_return_val_if_fail (watch != NULL, NULL);

663

664 return watch-\>data;

665}

666

678void

679dbus_watch_set_data (DBusWatch \*watch,

680 void \*data,

681 DBusFreeFunction free_data_function)

682{

683 \_dbus_return_if_fail (watch != NULL);

684

685 \_dbus_verbose ("Setting watch fd %" DBUS_POLLABLE_FORMAT " data to data = %p function = %p from data = %p function = %p\n",

686 \_dbus_pollable_printable (watch-\>fd),

687 data, free_data_function, watch-\>data, watch-\>free_data_function);

688

689 if (watch-\>free_data_function != NULL)

690 (\* watch-\>free_data_function) (watch-\>data);

691

692 watch-\>data = data;

693 watch-\>free_data_function = free_data_function;

694}

695

703dbus_bool_t

704dbus_watch_get_enabled (DBusWatch \*watch)

705{

706 \_dbus_return_val_if_fail (watch != NULL, FALSE);

707

708 return watch-\>enabled;

709}

710

711

734dbus_bool_t

735dbus_watch_handle (DBusWatch \*watch,

736 unsigned int flags)

737{

738 \_dbus_return_val_if_fail (watch != NULL, FALSE);

739

740\#ifndef DBUS_DISABLE_CHECKS

741 if (!\_dbus_pollable_is_valid (watch-\>fd) \|\| watch-\>flags == 0)

742 {

743 \_dbus_warn_check_failed ("Watch is invalid, it should have been removed");

744 return TRUE;

745 }

746\#endif

747

748 \_dbus_return_val_if_fail (\_dbus_pollable_is_valid (watch-\>fd) /\* fails if watch was removed \*/, TRUE);

749

750 \_dbus_watch_sanitize_condition (watch, &flags);

751

752 if (flags == 0)

753 {

754 \_dbus_verbose ("After sanitization, watch flags on fd %" DBUS_POLLABLE_FORMAT " were 0\n",

755 \_dbus_pollable_printable (watch-\>fd));

756 return TRUE;

757 }

758 else

759 return (\* watch-\>handler) (watch, flags,

760 watch-\>handler_data);

761}

762

763

DBusWatchToggledFunction

void(\* DBusWatchToggledFunction)(DBusWatch \*watch, void \*data)

Called when dbus_watch_get_enabled() may return a different value than it did before.

**Definition** dbus-connection.h:100

DBusAddWatchFunction

dbus_bool_t(\* DBusAddWatchFunction)(DBusWatch \*watch, void \*data)

Called when libdbus needs a new watch to be monitored by the main loop.

**Definition** dbus-connection.h:94

DBusRemoveWatchFunction

void(\* DBusRemoveWatchFunction)(DBusWatch \*watch, void \*data)

Called when libdbus no longer needs a watch to be monitored by the main loop.

**Definition** dbus-connection.h:106

DBUS_WATCH_READABLE

@ DBUS_WATCH_READABLE

As in POLLIN.

**Definition** dbus-connection.h:63

DBUS_WATCH_WRITABLE

@ DBUS_WATCH_WRITABLE

As in POLLOUT.

**Definition** dbus-connection.h:64

\_dbus_assert_not_reached

\#define \_dbus_assert_not_reached(explanation)

Aborts with an error message if called.

**Definition** dbus-internals.h:164

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_dbus_warn_check_failed

void \_dbus_warn_check_failed(const char \*format,...)

Prints a "critical" warning to stderr when an assertion fails; differs from \_dbus_warn primarily in t...

**Definition** dbus-internals.c:310

\_dbus_warn

void \_dbus_warn(const char \*format,...)

Prints a warning message to stderr.

**Definition** dbus-internals.c:278

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

\_dbus_watch_list_add_watch

dbus_bool_t \_dbus_watch_list_add_watch(DBusWatchList \*watch_list, DBusWatch \*watch)

Adds a new watch to the watch list, invoking the application DBusAddWatchFunction if appropriate.

**Definition** dbus-watch.c:383

\_dbus_watch_list_toggle_watch

void \_dbus_watch_list_toggle_watch(DBusWatchList \*watch_list, DBusWatch \*watch, dbus_bool_t enabled)

Sets a watch to the given enabled state, invoking the application's DBusWatchToggledFunction if appro...

**Definition** dbus-watch.c:443

\_dbus_watch_list_new

DBusWatchList \* \_dbus_watch_list_new(void)

Creates a new watch list.

**Definition** dbus-watch.c:234

\_dbus_watch_list_free

void \_dbus_watch_list_free(DBusWatchList \*watch_list)

Frees a DBusWatchList.

**Definition** dbus-watch.c:251

\_dbus_watch_list_set_functions

dbus_bool_t \_dbus_watch_list_set_functions(DBusWatchList \*watch_list, DBusAddWatchFunction add_function, DBusRemoveWatchFunction remove_function, DBusWatchToggledFunction toggled_function, void \*data, DBusFreeFunction free_data_function)

Sets the watch functions.

**Definition** dbus-watch.c:297

\_dbus_watch_set_handler

void \_dbus_watch_set_handler(DBusWatch \*watch, DBusWatchHandler handler, void \*data, DBusFreeFunction free_data_function)

Sets the handler for the watch.

**Definition** dbus-watch.c:500

\_dbus_watch_list_toggle_all_watches

void \_dbus_watch_list_toggle_all_watches(DBusWatchList \*watch_list, dbus_bool_t enabled)

Sets all watches to the given enabled state, invoking the application's DBusWatchToggledFunction if a...

**Definition** dbus-watch.c:474

\_dbus_watch_sanitize_condition

void \_dbus_watch_sanitize_condition(DBusWatch \*watch, unsigned int \*condition)

Sanitizes the given condition so that it only contains flags that the DBusWatch requested.

**Definition** dbus-watch.c:187

\_dbus_watch_new

DBusWatch \* \_dbus_watch_new(DBusPollable fd, unsigned int flags, dbus_bool_t enabled, DBusWatchHandler handler, void \*data, DBusFreeFunction free_data_function)

Creates a new DBusWatch.

**Definition** dbus-watch.c:90

DBusWatchHandler

dbus_bool_t(\* DBusWatchHandler)(DBusWatch \*watch, unsigned int flags, void \*data)

function to run when the watch is handled

**Definition** dbus-watch.h:45

\_dbus_watch_ref

DBusWatch \* \_dbus_watch_ref(DBusWatch \*watch)

Increments the reference count of a DBusWatch object.

**Definition** dbus-watch.c:126

\_dbus_watch_unref

void \_dbus_watch_unref(DBusWatch \*watch)

Decrements the reference count of a DBusWatch object and finalizes the object if the count reaches ze...

**Definition** dbus-watch.c:140

\_dbus_watch_list_remove_watch

void \_dbus_watch_list_remove_watch(DBusWatchList \*watch_list, DBusWatch \*watch)

Removes a watch from the watch list, invoking the application's DBusRemoveWatchFunction if appropriat...

**Definition** dbus-watch.c:416

\_dbus_watch_invalidate

void \_dbus_watch_invalidate(DBusWatch \*watch)

Clears the file descriptor from a now-invalid watch object so that no one tries to use it.

**Definition** dbus-watch.c:171

dbus_watch_get_unix_fd

DBUS_EXPORT int dbus_watch_get_unix_fd(DBusWatch \*watch)

Returns a UNIX file descriptor to be watched, which may be a pipe, socket, or other type of descripto...

**Definition** dbus-watch.c:566

dbus_watch_set_data

DBUS_EXPORT void dbus_watch_set_data(DBusWatch \*watch, void \*data, DBusFreeFunction free_data_function)

Sets data which can be retrieved with dbus_watch_get_data().

**Definition** dbus-watch.c:679

dbus_watch_get_fd

DBUS_EXPORT DBUS_DEPRECATED int dbus_watch_get_fd(DBusWatch \*watch)

Deprecated former name of dbus_watch_get_unix_fd().

**Definition** dbus-watch.c:545

dbus_watch_get_data

DBUS_EXPORT void \* dbus_watch_get_data(DBusWatch \*watch)

Gets data previously set with dbus_watch_set_data() or NULL if none.

**Definition** dbus-watch.c:660

dbus_watch_get_socket

DBUS_EXPORT int dbus_watch_get_socket(DBusWatch \*watch)

Returns a socket to be watched, on UNIX this will return -1 if our transport is not socket-based so d...

**Definition** dbus-watch.c:595

dbus_watch_handle

DBUS_EXPORT dbus_bool_t dbus_watch_handle(DBusWatch \*watch, unsigned int flags)

Called to notify the D-Bus library when a previously-added watch is ready for reading or writing,...

**Definition** dbus-watch.c:735

dbus_watch_get_enabled

DBUS_EXPORT dbus_bool_t dbus_watch_get_enabled(DBusWatch \*watch)

Returns whether a watch is enabled or not.

**Definition** dbus-watch.c:704

dbus_watch_get_flags

DBUS_EXPORT unsigned int dbus_watch_get_flags(DBusWatch \*watch)

Gets flags from DBusWatchFlags indicating what conditions should be monitored on the file descriptor.

**Definition** dbus-watch.c:644

DBusList

A node in a linked list.

**Definition** dbus-list.h:37

DBusList::data

void \* data

Data stored at this element.

**Definition** dbus-list.h:40

DBusSocket

Socket interface.

**Definition** dbus-sysdeps.h:185

DBusWatchList

DBusWatchList implementation details.

**Definition** dbus-watch.c:217

DBusWatchList::watch_free_data_function

DBusFreeFunction watch_free_data_function

Free function for watch callback data.

**Definition** dbus-watch.c:224

DBusWatchList::remove_watch_function

DBusRemoveWatchFunction remove_watch_function

Callback for removing a watch.

**Definition** dbus-watch.c:221

DBusWatchList::watch_data

void \* watch_data

Data for watch callbacks.

**Definition** dbus-watch.c:223

DBusWatchList::watches

DBusList \* watches

Watch objects.

**Definition** dbus-watch.c:218

DBusWatchList::add_watch_function

DBusAddWatchFunction add_watch_function

Callback for adding a watch.

**Definition** dbus-watch.c:220

DBusWatchList::watch_toggled_function

DBusWatchToggledFunction watch_toggled_function

Callback on toggling enablement.

**Definition** dbus-watch.c:222

DBusWatch

Implementation of DBusWatch.

**Definition** dbus-watch.c:43

DBusWatch::enabled

unsigned int enabled

Whether it's enabled.

**Definition** dbus-watch.c:54

DBusWatch::oom_last_time

unsigned int oom_last_time

Whether it was OOM last time.

**Definition** dbus-watch.c:55

DBusWatch::refcount

int refcount

Reference count.

**Definition** dbus-watch.c:44

DBusWatch::free_handler_data_function

DBusFreeFunction free_handler_data_function

Free the watch handler data.

**Definition** dbus-watch.c:50

DBusWatch::data

void \* data

Application data.

**Definition** dbus-watch.c:52

DBusWatch::fd

DBusPollable fd

File descriptor.

**Definition** dbus-watch.c:45

DBusWatch::flags

unsigned int flags

Conditions to watch.

**Definition** dbus-watch.c:46

DBusWatch::handler

DBusWatchHandler handler

Watch handler.

**Definition** dbus-watch.c:48

DBusWatch::free_data_function

DBusFreeFunction free_data_function

Free the application data.

**Definition** dbus-watch.c:53

DBusWatch::handler_data

void \* handler_data

Watch handler data.

**Definition** dbus-watch.c:49
