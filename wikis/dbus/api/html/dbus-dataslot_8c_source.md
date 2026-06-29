dbus-dataslot.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-dataslot.c storing data on objects

3 \*

4 \* Copyright (C) 2003 Red Hat, Inc.

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

27\#include "dbus-dataslot.h"

28\#include "dbus-threads-internal.h"

29\#include \<dbus/dbus-test-tap.h\>

30

48dbus_bool_t

49\_dbus_data_slot_allocator_init (DBusDataSlotAllocator \*allocator,

50 DBusGlobalLock lock)

51{

52 allocator-\>allocated_slots = NULL;

53 allocator-\>n_allocated_slots = 0;

54 allocator-\>n_used_slots = 0;

55 allocator-\>lock = lock;

56

57 return TRUE;

58}

59

71dbus_bool_t

72\_dbus_data_slot_allocator_alloc (DBusDataSlotAllocator \*allocator,

73 dbus_int32_t \*slot_id_p)

74{

75 dbus_int32_t slot;

76

77 if (!\_dbus_lock (allocator-\>lock))

78 return FALSE;

79

80 if (\*slot_id_p \>= 0)

81 {

82 slot = \*slot_id_p;

83

84 \_dbus_assert (slot \< allocator-\>n_allocated_slots);

85 \_dbus_assert (allocator-\>allocated_slots\[slot\].slot_id == slot);

86

87 allocator-\>allocated_slots\[slot\].refcount += 1;

88

89 goto out;

90 }

91

92 \_dbus_assert (\*slot_id_p \< 0);

93

94 if (allocator-\>n_used_slots \< allocator-\>n_allocated_slots)

95 {

96 slot = 0;

97 while (slot \< allocator-\>n_allocated_slots)

98 {

99 if (allocator-\>allocated_slots\[slot\].slot_id \< 0)

100 {

101 allocator-\>allocated_slots\[slot\].slot_id = slot;

102 allocator-\>allocated_slots\[slot\].refcount = 1;

103 allocator-\>n_used_slots += 1;

104 break;

105 }

106 ++slot;

107 }

108

109 \_dbus_assert (slot \< allocator-\>n_allocated_slots);

110 }

111 else

112 {

113 DBusAllocatedSlot \*tmp;

114

115 slot = -1;

116 tmp = dbus_realloc (allocator-\>allocated_slots,

117 sizeof (DBusAllocatedSlot) \* (allocator-\>n_allocated_slots + 1));

118 if (tmp == NULL)

119 goto out;

120

121 allocator-\>allocated_slots = tmp;

122 slot = allocator-\>n_allocated_slots;

123 allocator-\>n_allocated_slots += 1;

124 allocator-\>n_used_slots += 1;

125 allocator-\>allocated_slots\[slot\].slot_id = slot;

126 allocator-\>allocated_slots\[slot\].refcount = 1;

127 }

128

129 \_dbus_assert (slot \>= 0);

130 \_dbus_assert (slot \< allocator-\>n_allocated_slots);

131 \_dbus_assert (\*slot_id_p \< 0);

132 \_dbus_assert (allocator-\>allocated_slots\[slot\].slot_id == slot);

133 \_dbus_assert (allocator-\>allocated_slots\[slot\].refcount == 1);

134

135 \*slot_id_p = slot;

136

137 \_dbus_verbose ("Allocated slot %d on allocator %p total %d slots allocated %d used\n",

138 slot, allocator, allocator-\>n_allocated_slots, allocator-\>n_used_slots);

139

140 out:

141 \_dbus_unlock (allocator-\>lock);

142 return slot \>= 0;

143}

144

156void

157\_dbus_data_slot_allocator_free (DBusDataSlotAllocator \*allocator,

158 dbus_int32_t \*slot_id_p)

159{

160 if (!\_dbus_lock (allocator-\>lock))

161 \_dbus_assert_not_reached ("we should have initialized global locks "

162 "before we allocated this slot");

163

164 \_dbus_assert (\*slot_id_p \< allocator-\>n_allocated_slots);

165 \_dbus_assert (allocator-\>allocated_slots\[\*slot_id_p\].slot_id == \*slot_id_p);

166 \_dbus_assert (allocator-\>allocated_slots\[\*slot_id_p\].refcount \> 0);

167

168 allocator-\>allocated_slots\[\*slot_id_p\].refcount -= 1;

169

170 if (allocator-\>allocated_slots\[\*slot_id_p\].refcount \> 0)

171 {

172 \_dbus_unlock (allocator-\>lock);

173 return;

174 }

175

176 /\* refcount is 0, free the slot \*/

177 \_dbus_verbose ("Freeing slot %d on allocator %p total %d allocated %d used\n",

178 \*slot_id_p, allocator, allocator-\>n_allocated_slots, allocator-\>n_used_slots);

179

180 allocator-\>allocated_slots\[\*slot_id_p\].slot_id = -1;

181 \*slot_id_p = -1;

182

183 allocator-\>n_used_slots -= 1;

184

185 if (allocator-\>n_used_slots == 0)

186 {

187 dbus_free (allocator-\>allocated_slots);

188 allocator-\>allocated_slots = NULL;

189 allocator-\>n_allocated_slots = 0;

190 }

191

192 \_dbus_unlock (allocator-\>lock);

193}

194

199void

200\_dbus_data_slot_list_init (DBusDataSlotList \*list)

201{

202 list-\>slots = NULL;

203 list-\>n_slots = 0;

204}

205

223dbus_bool_t

224\_dbus_data_slot_list_set (DBusDataSlotAllocator \*allocator,

225 DBusDataSlotList \*list,

226 int slot,

227 void \*data,

228 DBusFreeFunction free_data_func,

229 DBusFreeFunction \*old_free_func,

230 void \*\*old_data)

231{

232\#ifndef DBUS_DISABLE_ASSERT

233 /\* We need to take the allocator lock here, because the allocator could

234 \* be e.g. realloc()ing allocated_slots. We avoid doing this if asserts

235 \* are disabled, since then the asserts are empty.

236 \*/

237 if (!\_dbus_lock (allocator-\>lock))

238 \_dbus_assert_not_reached ("we should have initialized global locks "

239 "before we allocated this slot");

240

241 \_dbus_assert (slot \< allocator-\>n_allocated_slots);

242 \_dbus_assert (allocator-\>allocated_slots\[slot\].slot_id == slot);

243 \_dbus_unlock (allocator-\>lock);

244\#endif

245

246 if (slot \>= list-\>n_slots)

247 {

248 DBusDataSlot \*tmp;

249 int i;

250

251 tmp = dbus_realloc (list-\>slots,

252 sizeof (DBusDataSlot) \* (slot + 1));

253 if (tmp == NULL)

254 return FALSE;

255

256 list-\>slots = tmp;

257 i = list-\>n_slots;

258 list-\>n_slots = slot + 1;

259 while (i \< list-\>n_slots)

260 {

261 list-\>slots\[i\].data = NULL;

262 list-\>slots\[i\].free_data_func = NULL;

263 ++i;

264 }

265 }

266

267 \_dbus_assert (slot \< list-\>n_slots);

268

269 \*old_data = list-\>slots\[slot\].data;

270 \*old_free_func = list-\>slots\[slot\].free_data_func;

271

272 list-\>slots\[slot\].data = data;

273 list-\>slots\[slot\].free_data_func = free_data_func;

274

275 return TRUE;

276}

277

287void\*

288\_dbus_data_slot_list_get (DBusDataSlotAllocator \*allocator,

289 DBusDataSlotList \*list,

290 int slot)

291{

292\#ifndef DBUS_DISABLE_ASSERT

293 /\* We need to take the allocator lock here, because the allocator could

294 \* be e.g. realloc()ing allocated_slots. We avoid doing this if asserts

295 \* are disabled, since then the asserts are empty.

296 \*/

297 if (!\_dbus_lock (allocator-\>lock))

298 \_dbus_assert_not_reached ("we should have initialized global locks "

299 "before we allocated this slot");

300

301 \_dbus_assert (slot \>= 0);

302 \_dbus_assert (slot \< allocator-\>n_allocated_slots);

303 \_dbus_assert (allocator-\>allocated_slots\[slot\].slot_id == slot);

304 \_dbus_unlock (allocator-\>lock);

305\#endif

306

307 if (slot \>= list-\>n_slots)

308 return NULL;

309 else

310 return list-\>slots\[slot\].data;

311}

312

319void

320\_dbus_data_slot_list_clear (DBusDataSlotList \*list)

321{

322 int i;

323

324 i = 0;

325 while (i \< list-\>n_slots)

326 {

327 if (list-\>slots\[i\].free_data_func)

328 (\* list-\>slots\[i\].free_data_func) (list-\>slots\[i\].data);

329 list-\>slots\[i\].data = NULL;

330 list-\>slots\[i\].free_data_func = NULL;

331 ++i;

332 }

333}

334

342void

343\_dbus_data_slot_list_free (DBusDataSlotList \*list)

344{

345 \_dbus_data_slot_list_clear (list);

346

347 dbus_free (list-\>slots);

348 list-\>slots = NULL;

349 list-\>n_slots = 0;

350}

351

354\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

355\#include "dbus-test.h"

356\#include \<stdio.h\>

357

358/\* Test-only, does not need to be thread-safe \*/

359static int free_counter;

360

361static void

362test_free_slot_data_func (void \*data)

363{

364 int i = \_DBUS_POINTER_TO_INT (data);

365

366 \_dbus_assert (free_counter == i);

367 ++free_counter;

368}

369

373dbus_bool_t

374\_dbus_data_slot_test (const char \*test_data_dir \_DBUS_GNUC_UNUSED)

375{

376 DBusDataSlotAllocator allocator;

377 DBusDataSlotList list;

378 int i;

379 DBusFreeFunction old_free_func;

380 void \*old_data;

381

382 if (!\_dbus_data_slot_allocator_init (&allocator, \_DBUS_LOCK_server_slots))

383 \_dbus_test_fatal ("no memory for allocator");

384

385 \_dbus_data_slot_list_init (&list);

386

387\#define N_SLOTS 100

388

389 i = 0;

390 while (i \< N_SLOTS)

391 {

392 /\* we don't really want apps to rely on this ordered

393 \* allocation, but it simplifies things to rely on it

394 \* here.

395 \*/

396 dbus_int32_t tmp = -1;

397

398 \_dbus_data_slot_allocator_alloc (&allocator, &tmp);

399

400 if (tmp != i)

401 \_dbus_test_fatal ("did not allocate slots in numeric order");

402

403 ++i;

404 }

405

406 i = 0;

407 while (i \< N_SLOTS)

408 {

409 if (!\_dbus_data_slot_list_set (&allocator, &list,

410 i,

411 \_DBUS_INT_TO_POINTER (i),

412 test_free_slot_data_func,

413 &old_free_func, &old_data))

414 \_dbus_test_fatal ("no memory to set data");

415

416 \_dbus_assert (old_free_func == NULL);

417 \_dbus_assert (old_data == NULL);

418

419 \_dbus_assert (\_dbus_data_slot_list_get (&allocator, &list, i) ==

420 \_DBUS_INT_TO_POINTER (i));

421

422 ++i;

423 }

424

425 free_counter = 0;

426 i = 0;

427 while (i \< N_SLOTS)

428 {

429 if (!\_dbus_data_slot_list_set (&allocator, &list,

430 i,

431 \_DBUS_INT_TO_POINTER (i),

432 test_free_slot_data_func,

433 &old_free_func, &old_data))

434 \_dbus_test_fatal ("no memory to set data");

435

436 \_dbus_assert (old_free_func == test_free_slot_data_func);

437 \_dbus_assert (\_DBUS_POINTER_TO_INT (old_data) == i);

438

439 (\* old_free_func) (old_data);

440 \_dbus_assert (i == (free_counter - 1));

441

442 \_dbus_assert (\_dbus_data_slot_list_get (&allocator, &list, i) ==

443 \_DBUS_INT_TO_POINTER (i));

444

445 ++i;

446 }

447

448 free_counter = 0;

449 \_dbus_data_slot_list_free (&list);

450

451 \_dbus_assert (N_SLOTS == free_counter);

452

453 i = 0;

454 while (i \< N_SLOTS)

455 {

456 dbus_int32_t tmp = i;

457

458 \_dbus_data_slot_allocator_free (&allocator, &tmp);

459 \_dbus_assert (tmp == -1);

460 ++i;

461 }

462

463 return TRUE;

464}

465

466\#endif /\* DBUS_ENABLE_EMBEDDED_TESTS \*/

\_dbus_data_slot_allocator_free

void \_dbus_data_slot_allocator_free(DBusDataSlotAllocator \*allocator, dbus_int32_t \*slot_id_p)

Deallocates an ID previously allocated with \_dbus_data_slot_allocator_alloc().

**Definition** dbus-dataslot.c:157

\_dbus_data_slot_list_clear

void \_dbus_data_slot_list_clear(DBusDataSlotList \*list)

Frees all data slots contained in the list, calling application-provided free functions if they exist...

**Definition** dbus-dataslot.c:320

\_dbus_data_slot_allocator_init

dbus_bool_t \_dbus_data_slot_allocator_init(DBusDataSlotAllocator \*allocator, DBusGlobalLock lock)

Initializes a data slot allocator object, used to assign integer IDs for data slots.

**Definition** dbus-dataslot.c:49

\_dbus_data_slot_list_init

void \_dbus_data_slot_list_init(DBusDataSlotList \*list)

Initializes a slot list.

**Definition** dbus-dataslot.c:200

\_dbus_data_slot_list_free

void \_dbus_data_slot_list_free(DBusDataSlotList \*list)

Frees the data slot list and all data slots contained in it, calling application-provided free functi...

**Definition** dbus-dataslot.c:343

\_dbus_data_slot_list_get

void \* \_dbus_data_slot_list_get(DBusDataSlotAllocator \*allocator, DBusDataSlotList \*list, int slot)

Retrieves data previously set with \_dbus_data_slot_list_set_data().

**Definition** dbus-dataslot.c:288

\_dbus_data_slot_list_set

dbus_bool_t \_dbus_data_slot_list_set(DBusDataSlotAllocator \*allocator, DBusDataSlotList \*list, int slot, void \*data, DBusFreeFunction free_data_func, DBusFreeFunction \*old_free_func, void \*\*old_data)

Stores a pointer in the data slot list, along with an optional function to be used for freeing the da...

**Definition** dbus-dataslot.c:224

\_dbus_data_slot_allocator_alloc

dbus_bool_t \_dbus_data_slot_allocator_alloc(DBusDataSlotAllocator \*allocator, dbus_int32_t \*slot_id_p)

Allocates an integer ID to be used for storing data in a DBusDataSlotList.

**Definition** dbus-dataslot.c:72

\_DBUS_INT_TO_POINTER

\#define \_DBUS_INT_TO_POINTER(integer)

Safely stuffs an integer into a pointer, to be extracted later with \_DBUS_POINTER_TO_INT.

**Definition** dbus-internals.h:192

\_dbus_assert_not_reached

\#define \_dbus_assert_not_reached(explanation)

Aborts with an error message if called.

**Definition** dbus-internals.h:164

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_DBUS_POINTER_TO_INT

\#define \_DBUS_POINTER_TO_INT(pointer)

Safely casts a void\* to an integer; should only be used on void\* that actually contain integers,...

**Definition** dbus-internals.h:191

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

dbus_realloc

void \* dbus_realloc(void \*memory, size_t bytes)

Resizes a block of memory previously allocated by dbus_malloc() or dbus_malloc0().

**Definition** dbus-memory.c:610

DBusAllocatedSlot

An allocated slot for storing data.

**Definition** dbus-dataslot.h:49

DBusAllocatedSlot::refcount

int refcount

Number of uses of the slot.

**Definition** dbus-dataslot.h:51

DBusAllocatedSlot::slot_id

dbus_int32_t slot_id

ID of this slot.

**Definition** dbus-dataslot.h:50

DBusDataSlotAllocator

An allocator that tracks a set of slot IDs.

**Definition** dbus-dataslot.h:58

DBusDataSlotAllocator::allocated_slots

DBusAllocatedSlot \* allocated_slots

Allocated slots.

**Definition** dbus-dataslot.h:59

DBusDataSlotAllocator::n_allocated_slots

int n_allocated_slots

number of slots malloc'd

**Definition** dbus-dataslot.h:60

DBusDataSlotAllocator::lock

DBusGlobalLock lock

index of thread lock

**Definition** dbus-dataslot.h:62

DBusDataSlotAllocator::n_used_slots

int n_used_slots

number of slots used

**Definition** dbus-dataslot.h:61

DBusDataSlotList

Data structure that stores the actual user data set at a given slot.

**Definition** dbus-dataslot.h:72

DBusDataSlotList::n_slots

int n_slots

Slots we have storage for in data_slots.

**Definition** dbus-dataslot.h:74

DBusDataSlotList::slots

DBusDataSlot \* slots

Data slots.

**Definition** dbus-dataslot.h:73

DBusDataSlot

DBusDataSlot is used to store application data on the connection.

**Definition** dbus-dataslot.h:39

DBusDataSlot::data

void \* data

The application data.

**Definition** dbus-dataslot.h:40

DBusDataSlot::free_data_func

DBusFreeFunction free_data_func

Free the application data.

**Definition** dbus-dataslot.h:41
