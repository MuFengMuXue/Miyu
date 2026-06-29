dbus-list.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-list.c Generic linked list utility (internal to D-Bus implementation)

3 \*

4 \* Copyright (C) 2002 Red Hat, Inc.

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

28\#include "dbus-list.h"

29\#include "dbus-mempool.h"

30\#include "dbus-threads-internal.h"

31\#include \<dbus/dbus-test-tap.h\>

32

41/\* Protected by \_DBUS_LOCK (list) \*/

42static DBusMemPool \*list_pool;

43

54/\* the mem pool is probably a speed hit, with the thread

55 \* lock, though it does still save memory - unknown.

56 \*/

57static DBusList\*

58alloc_link (void \*data)

59{

60 DBusList \*link;

61

62 if (!\_DBUS_LOCK (list))

63 return FALSE;

64

65 if (list_pool == NULL)

66 {

67 list_pool = \_dbus_mem_pool_new (sizeof (DBusList), TRUE);

68

69 if (list_pool == NULL)

70 {

71 \_DBUS_UNLOCK (list);

72 return NULL;

73 }

74

75 link = \_dbus_mem_pool_alloc (list_pool);

76 if (link == NULL)

77 {

78 \_dbus_mem_pool_free (list_pool);

79 list_pool = NULL;

80 \_DBUS_UNLOCK (list);

81 return NULL;

82 }

83 }

84 else

85 {

86 link = \_dbus_mem_pool_alloc (list_pool);

87 }

88

89 if (link)

90 link-\>data = data;

91

92 \_DBUS_UNLOCK (list);

93

94 return link;

95}

96

97static void

98free_link (DBusList \*link)

99{

100 if (!\_DBUS_LOCK (list))

101 \_dbus_assert_not_reached ("we should have initialized global locks "

102 "before we allocated a linked-list link");

103

104 if (\_dbus_mem_pool_dealloc (list_pool, link))

105 {

106 \_dbus_mem_pool_free (list_pool);

107 list_pool = NULL;

108 }

109

110 \_DBUS_UNLOCK (list);

111}

112

113static void

114link_before (DBusList \*\*list,

115 DBusList \*before_this_link,

116 DBusList \*link)

117{

118 if (\*list == NULL)

119 {

120 link-\>prev = link;

121 link-\>next = link;

122 \*list = link;

123 }

124 else

125 {

126 link-\>next = before_this_link;

127 link-\>prev = before_this_link-\>prev;

128 before_this_link-\>prev = link;

129 link-\>prev-\>next = link;

130

131 if (before_this_link == \*list)

132 \*list = link;

133 }

134}

135

136static void

137link_after (DBusList \*\*list,

138 DBusList \*after_this_link,

139 DBusList \*link)

140{

141 if (\*list == NULL)

142 {

143 link-\>prev = link;

144 link-\>next = link;

145 \*list = link;

146 }

147 else

148 {

149 link-\>prev = after_this_link;

150 link-\>next = after_this_link-\>next;

151 after_this_link-\>next = link;

152 link-\>next-\>prev = link;

153 }

154}

155

156\#ifdef DBUS_ENABLE_STATS

157void

158\_dbus_list_get_stats (dbus_uint32_t \*in_use_p,

159 dbus_uint32_t \*in_free_list_p,

160 dbus_uint32_t \*allocated_p)

161{

162 if (!\_DBUS_LOCK (list))

163 {

164 \*in_use_p = 0;

165 \*in_free_list_p = 0;

166 \*allocated_p = 0;

167 return;

168 }

169

170 \_dbus_mem_pool_get_stats (list_pool, in_use_p, in_free_list_p, allocated_p);

171 \_DBUS_UNLOCK (list);

172}

173\#endif

174

244DBusList\*

245\_dbus_list_alloc_link (void \*data)

246{

247 return alloc_link (data);

248}

249

256void

257\_dbus_list_free_link (DBusList \*link)

258{

259 free_link (link);

260}

261

262

272dbus_bool_t

273\_dbus_list_append (DBusList \*\*list,

274 void \*data)

275{

276 if (!\_dbus_list_prepend (list, data))

277 return FALSE;

278

279 /\* Now cycle the list forward one so the prepended node is the tail \*/

280 \*list = (\*list)-\>next;

281

282 return TRUE;

283}

284

294dbus_bool_t

295\_dbus_list_prepend (DBusList \*\*list,

296 void \*data)

297{

298 DBusList \*link;

299

300 link = alloc_link (data);

301 if (link == NULL)

302 return FALSE;

303

304 link_before (list, \*list, link);

305

306 return TRUE;

307}

308

317void

318\_dbus_list_append_link (DBusList \*\*list,

319 DBusList \*link)

320{

321 \_dbus_list_prepend_link (list, link);

322

323 /\* Now cycle the list forward one so the prepended node is the tail \*/

324 \*list = (\*list)-\>next;

325}

326

335void

336\_dbus_list_prepend_link (DBusList \*\*list,

337 DBusList \*link)

338{

339 link_before (list, \*list, link);

340}

341

350dbus_bool_t

351\_dbus_list_insert_after (DBusList \*\*list,

352 DBusList \*after_this_link,

353 void \*data)

354{

355 DBusList \*link;

356

357 if (after_this_link == NULL)

358 return \_dbus_list_prepend (list, data);

359 else

360 {

361 link = alloc_link (data);

362 if (link == NULL)

363 return FALSE;

364

365 link_after (list, after_this_link, link);

366 }

367

368 return TRUE;

369}

370

378void

379\_dbus_list_insert_before_link (DBusList \*\*list,

380 DBusList \*before_this_link,

381 DBusList \*link)

382{

383 if (before_this_link == NULL)

384 \_dbus_list_append_link (list, link);

385 else

386 link_before (list, before_this_link, link);

387}

388

396void

397\_dbus_list_insert_after_link (DBusList \*\*list,

398 DBusList \*after_this_link,

399 DBusList \*link)

400{

401 if (after_this_link == NULL)

402 \_dbus_list_prepend_link (list, link);

403 else

404 link_after (list, after_this_link, link);

405}

406

417dbus_bool_t

418\_dbus_list_remove (DBusList \*\*list,

419 void \*data)

420{

421 DBusList \*link;

422

423 link = \*list;

424 while (link != NULL)

425 {

426 if (link-\>data == data)

427 {

428 \_dbus_list_remove_link (list, link);

429 return TRUE;

430 }

431

432 link = \_dbus_list_get_next_link (list, link);

433 }

434

435 return FALSE;

436}

437

448dbus_bool_t

449\_dbus_list_remove_last (DBusList \*\*list,

450 void \*data)

451{

452 DBusList \*link;

453

454 link = \_dbus_list_find_last (list, data);

455 if (link)

456 {

457 \_dbus_list_remove_link (list, link);

458 return TRUE;

459 }

460 else

461 return FALSE;

462}

463

474DBusList\*

475\_dbus_list_find_last (DBusList \*\*list,

476 void \*data)

477{

478 DBusList \*link;

479

480 link = \_dbus_list_get_last_link (list);

481

482 while (link != NULL)

483 {

484 if (link-\>data == data)

485 return link;

486

487 link = \_dbus_list_get_prev_link (list, link);

488 }

489

490 return NULL;

491}

492

501void

502\_dbus_list_unlink (DBusList \*\*list,

503 DBusList \*link)

504{

505 if (link-\>next == link)

506 {

507 /\* one-element list \*/

508 \*list = NULL;

509 }

510 else

511 {

512 link-\>prev-\>next = link-\>next;

513 link-\>next-\>prev = link-\>prev;

514

515 if (\*list == link)

516 \*list = link-\>next;

517 }

518

519 link-\>next = NULL;

520 link-\>prev = NULL;

521}

522

529void

530\_dbus_list_remove_link (DBusList \*\*list,

531 DBusList \*link)

532{

533 \_dbus_list_unlink (list, link);

534 free_link (link);

535}

536

544void

545\_dbus_list_clear (DBusList \*\*list)

546{

547 DBusList \*link;

548

549 link = \*list;

550 while (link != NULL)

551 {

552 DBusList \*next = \_dbus_list_get_next_link (list, link);

553

554 free_link (link);

555

556 link = next;

557 }

558

559 \*list = NULL;

560}

561

569void

570\_dbus_list_clear_full (DBusList \*\*list,

571 DBusFreeFunction function)

572{

573 DBusList \*link;

574

575 link = \*list;

576 while (link != NULL)

577 {

578 DBusList \*next = \_dbus_list_get_next_link (list, link);

579

580 function (link-\>data);

581 free_link (link);

582

583 link = next;

584 }

585

586 \*list = NULL;

587}

588

596DBusList\*

597\_dbus_list_get_first_link (DBusList \*\*list)

598{

599 return \*list;

600}

601

609DBusList\*

610\_dbus_list_get_last_link (DBusList \*\*list)

611{

612 if (\*list == NULL)

613 return NULL;

614 else

615 return (\*list)-\>prev;

616}

617

625void\*

626\_dbus_list_get_last (DBusList \*\*list)

627{

628 if (\*list == NULL)

629 return NULL;

630 else

631 return (\*list)-\>prev-\>data;

632}

633

641void\*

642\_dbus_list_get_first (DBusList \*\*list)

643{

644 if (\*list == NULL)

645 return NULL;

646 else

647 return (\*list)-\>data;

648}

649

657DBusList\*

658\_dbus_list_pop_first_link (DBusList \*\*list)

659{

660 DBusList \*link;

661

662 link = \_dbus_list_get_first_link (list);

663 if (link == NULL)

664 return NULL;

665

666 \_dbus_list_unlink (list, link);

667

668 return link;

669}

670

678void\*

679\_dbus_list_pop_first (DBusList \*\*list)

680{

681 DBusList \*link;

682 void \*data;

683

684 link = \_dbus_list_get_first_link (list);

685 if (link == NULL)

686 return NULL;

687

688 data = link-\>data;

689 \_dbus_list_remove_link (list, link);

690

691 return data;

692}

693

701void\*

702\_dbus_list_pop_last (DBusList \*\*list)

703{

704 DBusList \*link;

705 void \*data;

706

707 link = \_dbus_list_get_last_link (list);

708 if (link == NULL)

709 return NULL;

710

711 data = link-\>data;

712 \_dbus_list_remove_link (list, link);

713

714 return data;

715}

716

726dbus_bool_t

727\_dbus_list_copy (DBusList \*\*list,

728 DBusList \*\*dest)

729{

730 DBusList \*link;

731

732 \_dbus_assert (list != dest);

733

734 \*dest = NULL;

735

736 link = \*list;

737 while (link != NULL)

738 {

739 if (!\_dbus_list_append (dest, link-\>data))

740 {

741 /\* free what we have so far \*/

742 \_dbus_list_clear (dest);

743 return FALSE;

744 }

745

746 link = \_dbus_list_get_next_link (list, link);

747 }

748

749 return TRUE;

750}

751

759int

760\_dbus_list_get_length (DBusList \*\*list)

761{

762 DBusList \*link;

763 int length;

764

765 length = 0;

766

767 link = \*list;

768 while (link != NULL)

769 {

770 ++length;

771

772 link = \_dbus_list_get_next_link (list, link);

773 }

774

775 return length;

776}

777

788void

789\_dbus_list_foreach (DBusList \*\*list,

790 DBusForeachFunction function,

791 void \*data)

792{

793 DBusList \*link;

794

795 link = \*list;

796 while (link != NULL)

797 {

798 DBusList \*next = \_dbus_list_get_next_link (list, link);

799

800 (\* function) (link-\>data, data);

801

802 link = next;

803 }

804}

805

812dbus_bool_t

813\_dbus_list_length_is_one (DBusList \*\*list)

814{

815 return (\*list != NULL &&

816 (\*list)-\>next == \*list);

817}

818

\_dbus_assert_not_reached

\#define \_dbus_assert_not_reached(explanation)

Aborts with an error message if called.

**Definition** dbus-internals.h:164

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_DBUS_UNLOCK

\#define \_DBUS_UNLOCK(name)

Unlocks a global lock.

**Definition** dbus-internals.h:438

\_DBUS_LOCK

\#define \_DBUS_LOCK(name)

Locks a global lock, initializing it first if necessary.

**Definition** dbus-internals.h:437

\_dbus_list_get_first_link

DBusList \* \_dbus_list_get_first_link(DBusList \*\*list)

Gets the first link in the list.

**Definition** dbus-list.c:597

\_dbus_list_insert_before_link

void \_dbus_list_insert_before_link(DBusList \*\*list, DBusList \*before_this_link, DBusList \*link)

Inserts a link into the list before the given existing link.

**Definition** dbus-list.c:379

\_dbus_list_copy

dbus_bool_t \_dbus_list_copy(DBusList \*\*list, DBusList \*\*dest)

Copies a list.

**Definition** dbus-list.c:727

\_dbus_list_pop_first_link

DBusList \* \_dbus_list_pop_first_link(DBusList \*\*list)

Removes the first link in the list and returns it.

**Definition** dbus-list.c:658

\_dbus_list_length_is_one

dbus_bool_t \_dbus_list_length_is_one(DBusList \*\*list)

Check whether length is exactly one.

**Definition** dbus-list.c:813

\_dbus_list_get_last

void \* \_dbus_list_get_last(DBusList \*\*list)

Gets the last data in the list.

**Definition** dbus-list.c:626

\_dbus_list_remove

dbus_bool_t \_dbus_list_remove(DBusList \*\*list, void \*data)

Removes a value from the list.

**Definition** dbus-list.c:418

\_dbus_list_append_link

void \_dbus_list_append_link(DBusList \*\*list, DBusList \*link)

Appends a link to the list.

**Definition** dbus-list.c:318

\_dbus_list_insert_after_link

void \_dbus_list_insert_after_link(DBusList \*\*list, DBusList \*after_this_link, DBusList \*link)

Inserts a link into the list after the given existing link.

**Definition** dbus-list.c:397

\_dbus_list_clear_full

void \_dbus_list_clear_full(DBusList \*\*list, DBusFreeFunction function)

Free every link and every element in the list.

**Definition** dbus-list.c:570

\_dbus_list_insert_after

dbus_bool_t \_dbus_list_insert_after(DBusList \*\*list, DBusList \*after_this_link, void \*data)

Inserts data into the list after the given existing link.

**Definition** dbus-list.c:351

\_dbus_list_remove_link

void \_dbus_list_remove_link(DBusList \*\*list, DBusList \*link)

Removes a link from the list.

**Definition** dbus-list.c:530

\_dbus_list_get_first

void \* \_dbus_list_get_first(DBusList \*\*list)

Gets the first data in the list.

**Definition** dbus-list.c:642

\_dbus_list_get_last_link

DBusList \* \_dbus_list_get_last_link(DBusList \*\*list)

Gets the last link in the list.

**Definition** dbus-list.c:610

\_dbus_list_unlink

void \_dbus_list_unlink(DBusList \*\*list, DBusList \*link)

Removes the given link from the list, but doesn't free it.

**Definition** dbus-list.c:502

\_dbus_list_find_last

DBusList \* \_dbus_list_find_last(DBusList \*\*list, void \*data)

Finds a value in the list.

**Definition** dbus-list.c:475

\_dbus_list_pop_last

void \* \_dbus_list_pop_last(DBusList \*\*list)

Removes the last value in the list and returns it.

**Definition** dbus-list.c:702

\_dbus_list_get_prev_link

\#define \_dbus_list_get_prev_link(list, link)

Gets the previous link in the list, or NULL if there are no more links.

**Definition** dbus-list.h:122

\_dbus_list_free_link

void \_dbus_list_free_link(DBusList \*link)

Frees a linked list node allocated with \_dbus_list_alloc_link.

**Definition** dbus-list.c:257

\_dbus_list_pop_first

void \* \_dbus_list_pop_first(DBusList \*\*list)

Removes the first value in the list and returns it.

**Definition** dbus-list.c:679

\_dbus_list_foreach

void \_dbus_list_foreach(DBusList \*\*list, DBusForeachFunction function, void \*data)

Calls the given function for each element in the list.

**Definition** dbus-list.c:789

\_dbus_list_get_length

int \_dbus_list_get_length(DBusList \*\*list)

Gets the length of a list.

**Definition** dbus-list.c:760

\_dbus_list_clear

void \_dbus_list_clear(DBusList \*\*list)

Frees all links in the list and sets the list head to NULL.

**Definition** dbus-list.c:545

\_dbus_list_prepend_link

void \_dbus_list_prepend_link(DBusList \*\*list, DBusList \*link)

Prepends a link to the list.

**Definition** dbus-list.c:336

\_dbus_list_prepend

dbus_bool_t \_dbus_list_prepend(DBusList \*\*list, void \*data)

Prepends a value to the list.

**Definition** dbus-list.c:295

\_dbus_list_alloc_link

DBusList \* \_dbus_list_alloc_link(void \*data)

Allocates a linked list node.

**Definition** dbus-list.c:245

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

\_dbus_mem_pool_alloc

void \* \_dbus_mem_pool_alloc(DBusMemPool \*pool)

Allocates an object from the memory pool.

**Definition** dbus-mempool.c:227

\_dbus_mem_pool_dealloc

dbus_bool_t \_dbus_mem_pool_dealloc(DBusMemPool \*pool, void \*element)

Deallocates an object previously created with \_dbus_mem_pool_alloc().

**Definition** dbus-mempool.c:366

\_dbus_mem_pool_free

void \_dbus_mem_pool_free(DBusMemPool \*pool)

Frees a memory pool (and all elements allocated from it).

**Definition** dbus-mempool.c:200

\_dbus_mem_pool_new

DBusMemPool \* \_dbus_mem_pool_new(int element_size, dbus_bool_t zero_elements)

Creates a new memory pool, or returns NULL on failure.

**Definition** dbus-mempool.c:148

DBusFreeFunction

void(\* DBusFreeFunction)(void \*memory)

The type of a function which frees a block of memory.

**Definition** dbus-memory.h:65

DBusList

A node in a linked list.

**Definition** dbus-list.h:37

DBusList::data

void \* data

Data stored at this element.

**Definition** dbus-list.h:40

DBusList::next

DBusList \* next

Next list node.

**Definition** dbus-list.h:39

DBusList::prev

DBusList \* prev

Previous list node.

**Definition** dbus-list.h:38

DBusMemPool

Internals fields of DBusMemPool.

**Definition** dbus-mempool.c:109
