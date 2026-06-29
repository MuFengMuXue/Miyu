dbus-mempool.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-mempool.h Memory pools

3 \*

4 \* Copyright (C) 2002, 2003 Red Hat, Inc.

5 \* Copyright (C) 2003 CodeFactory AB

6 \* Copyright (C) 2011-2012 Collabora Ltd.

7 \*

8 \* SPDX-License-Identifier: AFL-2.1 OR GPL-2.0-or-later

9 \*

10 \* Licensed under the Academic Free License version 2.1

11 \*

12 \* This program is free software; you can redistribute it and/or modify

13 \* it under the terms of the GNU General Public License as published by

14 \* the Free Software Foundation; either version 2 of the License, or

15 \* (at your option) any later version.

16 \*

17 \* This program is distributed in the hope that it will be useful,

18 \* but WITHOUT ANY WARRANTY; without even the implied warranty of

19 \* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the

20 \* GNU General Public License for more details.

21 \*

22 \* You should have received a copy of the GNU General Public License

23 \* along with this program; if not, write to the Free Software

24 \* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

25 \*

26 \*/

27

28\#include \<config.h\>

29\#include "dbus-mempool.h"

30\#include "dbus-internals.h"

31\#include "dbus-valgrind-internal.h"

32

58typedef struct DBusFreedElement DBusFreedElement;

59

65struct DBusFreedElement

66{

67 DBusFreedElement \*next;

68};

69

74typedef struct DBusMemBlock DBusMemBlock;

75

80struct DBusMemBlock

81{

82 DBusMemBlock \*next;

87 size_t used_so_far;

88\#if defined(\_\_STDC_VERSION\_\_) && (\_\_STDC_VERSION\_\_ \>= 201112L)

89 /\*

90 \* Ensure that elements is aligned correctly. For all supported pre-C11

91 \* targets, the size_t above should ensure that the elements array is

92 \* sufficiently aligned (this is checked in the static assert below).

93 \*/

94 \_Alignas (dbus_max_align_t)

95\#endif

96 unsigned char elements\[\];

97};

98

99\_DBUS_STATIC_ASSERT (\_DBUS_IS_ALIGNED (sizeof (struct DBusMemBlock),

100 \_DBUS_ALIGNOF (dbus_max_align_t)));

101\_DBUS_STATIC_ASSERT (\_DBUS_IS_ALIGNED (offsetof (struct DBusMemBlock,

102 elements),

103 \_DBUS_ALIGNOF (dbus_max_align_t)));

104

108struct DBusMemPool

109{

110 size_t element_size;

111 size_t block_size;

112 unsigned int zero_elements : 1;

114 DBusFreedElement \*free_elements;

115 DBusMemBlock \*blocks;

116 int allocated_elements;

117};

118

147DBusMemPool\*

148\_dbus_mem_pool_new (int element_size,

149 dbus_bool_t zero_elements)

150{

151 DBusMemPool \*pool;

152

153 pool = dbus_new0 (DBusMemPool, 1);

154 if (pool == NULL)

155 return NULL;

156

157 /\* Make the element size at least 8 bytes. \*/

158 if (element_size \< 8)

159 element_size = 8;

160 if (element_size \< (int) sizeof (void \*))

161 element_size = sizeof (void \*);

162

163 /\* these assertions are equivalent but the first is more clear

164 \* to programmers that see it fail.

165 \*/

166 \_dbus_assert (element_size \>= (int) sizeof (void\*));

167 \_dbus_assert (element_size \>= (int) sizeof (DBusFreedElement));

168

169 /\* align the element size to be suitable for the most-aligned type

170 \* that we care about (in practice usually a pointer).

171 \*/

172 pool-\>element_size =

173 \_DBUS_ALIGN_VALUE (element_size, \_DBUS_ALIGNOF (dbus_max_align_t));

174

175 pool-\>zero_elements = zero_elements != FALSE;

176

177 pool-\>allocated_elements = 0;

178

179 /\* pick a size for the first block; it increases

180 \* for each block we need to allocate. This is

181 \* actually half the initial block size

182 \* since \_dbus_mem_pool_alloc() unconditionally

183 \* doubles it prior to creating a new block. \*/

184 pool-\>block_size = pool-\>element_size \* 8;

185

186 \_dbus_assert ((pool-\>block_size %

187 pool-\>element_size) == 0);

188

189 VALGRIND_CREATE_MEMPOOL (pool, 0, zero_elements);

190

191 return pool;

192}

193

199void

200\_dbus_mem_pool_free (DBusMemPool \*pool)

201{

202 DBusMemBlock \*block;

203

204 VALGRIND_DESTROY_MEMPOOL (pool);

205

206 block = pool-\>blocks;

207 while (block != NULL)

208 {

209 DBusMemBlock \*next = block-\>next;

210

211 dbus_free (block);

212

213 block = next;

214 }

215

216 dbus_free (pool);

217}

218

226void\*

227\_dbus_mem_pool_alloc (DBusMemPool \*pool)

228{

229\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

230 if (\_dbus_disable_mem_pools ())

231 {

232 DBusMemBlock \*block;

233 size_t alloc_size;

234

235 /\* This is obviously really silly, but it's

236 \* debug-mode-only code that is compiled out

237 \* when tests are disabled (\_dbus_disable_mem_pools()

238 \* is a constant expression FALSE so this block

239 \* should vanish)

240 \*/

241

242 alloc_size = sizeof (DBusMemBlock) + pool-\>element_size;

243

244 if (pool-\>zero_elements)

245 block = dbus_malloc0 (alloc_size);

246 else

247 block = dbus_malloc (alloc_size);

248

249 if (block != NULL)

250 {

251 block-\>next = pool-\>blocks;

252 pool-\>blocks = block;

253 pool-\>allocated_elements += 1;

254

255 VALGRIND_MEMPOOL_ALLOC (pool, (void \*) &block-\>elements\[0\],

256 pool-\>element_size);

257 \_dbus_assert (\_DBUS_IS_ALIGNED (&block-\>elements\[0\],

258 \_DBUS_ALIGNOF (dbus_max_align_t)));

259 return (void\*) &block-\>elements\[0\];

260 }

261 else

262 return NULL;

263 }

264 else

265\#endif

266 {

267 if (\_dbus_decrement_fail_alloc_counter ())

268 {

269 \_dbus_verbose (" FAILING mempool alloc\n");

270 return NULL;

271 }

272 else if (pool-\>free_elements)

273 {

274 DBusFreedElement \*element = pool-\>free_elements;

275

276 pool-\>free_elements = pool-\>free_elements-\>next;

277

278 VALGRIND_MEMPOOL_ALLOC (pool, element, pool-\>element_size);

279

280 if (pool-\>zero_elements)

281 memset (element, '\0', pool-\>element_size);

282

283 pool-\>allocated_elements += 1;

284 \_dbus_assert (

285 \_DBUS_IS_ALIGNED (element, \_DBUS_ALIGNOF (dbus_max_align_t)));

286 return element;

287 }

288 else

289 {

290 void \*element;

291

292 if (pool-\>blocks == NULL \|\|

293 pool-\>blocks-\>used_so_far == pool-\>block_size)

294 {

295 /\* Need a new block \*/

296 DBusMemBlock \*block;

297 size_t alloc_size;

298\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

299 int saved_counter;

300\#endif

301

302 if (pool-\>block_size \<= \_DBUS_INT_MAX / 4) /\* avoid overflow \*/

303 {

304 /\* use a larger block size for our next block \*/

305 pool-\>block_size \*= 2;

306 \_dbus_assert ((pool-\>block_size %

307 pool-\>element_size) == 0);

308 }

309

310 alloc_size = sizeof (DBusMemBlock) + pool-\>block_size;

311

312\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

313 /\* We save/restore the counter, so that memory pools won't

314 \* cause a given function to have different number of

315 \* allocations on different invocations. i.e. when testing

316 \* we want consistent alloc patterns. So we skip our

317 \* malloc here for purposes of failed alloc simulation.

318 \*/

319 saved_counter = \_dbus_get_fail_alloc_counter ();

320 \_dbus_set_fail_alloc_counter (-1);

321\#endif

322

323 if (pool-\>zero_elements)

324 block = dbus_malloc0 (alloc_size);

325 else

326 block = dbus_malloc (alloc_size);

327 \_dbus_assert (

328 \_DBUS_IS_ALIGNED (block, \_DBUS_ALIGNOF (dbus_max_align_t)));

329

330\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

331 \_dbus_set_fail_alloc_counter (saved_counter);

332 \_dbus_assert (saved_counter == \_dbus_get_fail_alloc_counter ());

333\#endif

334

335 if (block == NULL)

336 return NULL;

337

338 block-\>used_so_far = 0;

339 block-\>next = pool-\>blocks;

340 pool-\>blocks = block;

341 }

342

343 element = &pool-\>blocks-\>elements\[pool-\>blocks-\>used_so_far\];

344

345 pool-\>blocks-\>used_so_far += pool-\>element_size;

346

347 pool-\>allocated_elements += 1;

348

349 VALGRIND_MEMPOOL_ALLOC (pool, element, pool-\>element_size);

350 \_dbus_assert (

351 \_DBUS_IS_ALIGNED (element, \_DBUS_ALIGNOF (dbus_max_align_t)));

352 return element;

353 }

354 }

355}

356

365dbus_bool_t

366\_dbus_mem_pool_dealloc (DBusMemPool \*pool,

367 void \*element)

368{

369 VALGRIND_MEMPOOL_FREE (pool, element);

370

371\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

372 if (\_dbus_disable_mem_pools ())

373 {

374 DBusMemBlock \*block;

375 DBusMemBlock \*prev;

376

377 /\* mmm, fast. ;-) debug-only code, so doesn't matter. \*/

378

379 prev = NULL;

380 block = pool-\>blocks;

381

382 while (block != NULL)

383 {

384 if (block-\>elements == (unsigned char\*) element)

385 {

386 if (prev)

387 prev-\>next = block-\>next;

388 else

389 pool-\>blocks = block-\>next;

390

391 dbus_free (block);

392

393 \_dbus_assert (pool-\>allocated_elements \> 0);

394 pool-\>allocated_elements -= 1;

395

396 if (pool-\>allocated_elements == 0)

397 \_dbus_assert (pool-\>blocks == NULL);

398

399 return pool-\>blocks == NULL;

400 }

401 prev = block;

402 block = block-\>next;

403 }

404

405 \_dbus_assert_not_reached ("freed nonexistent block");

406 return FALSE;

407 }

408 else

409\#endif

410 {

411 DBusFreedElement \*freed;

412

413 freed = element;

414 /\* used for internal mempool administration \*/

415 VALGRIND_MAKE_MEM_UNDEFINED (freed, sizeof (\*freed));

416

417 freed-\>next = pool-\>free_elements;

418 pool-\>free_elements = freed;

419

420 \_dbus_assert (pool-\>allocated_elements \> 0);

421 pool-\>allocated_elements -= 1;

422

423 return pool-\>allocated_elements == 0;

424 }

425}

426

427\#ifdef DBUS_ENABLE_STATS

428void

429\_dbus_mem_pool_get_stats (DBusMemPool \*pool,

430 dbus_uint32_t \*in_use_p,

431 dbus_uint32_t \*in_free_list_p,

432 dbus_uint32_t \*allocated_p)

433{

434 DBusMemBlock \*block;

435 DBusFreedElement \*freed;

436 dbus_uint32_t in_use = 0;

437 dbus_uint32_t in_free_list = 0;

438 dbus_uint32_t allocated = 0;

439

440 if (pool != NULL)

441 {

442 in_use = pool-\>element_size \* pool-\>allocated_elements;

443

444 for (freed = pool-\>free_elements; freed != NULL; freed = freed-\>next)

445 {

446 in_free_list += pool-\>element_size;

447 }

448

449 for (block = pool-\>blocks; block != NULL; block = block-\>next)

450 {

451 if (block == pool-\>blocks)

452 allocated += pool-\>block_size;

453 else

454 allocated += block-\>used_so_far;

455 }

456 }

457

458 if (in_use_p != NULL)

459 \*in_use_p = in_use;

460

461 if (in_free_list_p != NULL)

462 \*in_free_list_p = in_free_list;

463

464 if (allocated_p != NULL)

465 \*allocated_p = allocated;

466}

467\#endif /\* DBUS_ENABLE_STATS \*/

468

\_dbus_assert_not_reached

\#define \_dbus_assert_not_reached(explanation)

Aborts with an error message if called.

**Definition** dbus-internals.h:164

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_DBUS_INT_MAX

\#define \_DBUS_INT_MAX

Maximum value of type "int".

**Definition** dbus-internals.h:327

NULL

\#define NULL

A null pointer, defined appropriately for C or C++.

**Definition** dbus-macros.h:51

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

dbus_free

void dbus_free(void \*memory)

Frees a block of memory previously allocated by dbus_malloc() or dbus_malloc0().

**Definition** dbus-memory.c:710

dbus_malloc0

void \* dbus_malloc0(size_t bytes)

Allocates the given number of bytes, as with standard malloc(), but all bytes are initialized to zero...

**Definition** dbus-memory.c:540

dbus_new0

\#define dbus_new0(type, count)

Safe macro for using dbus_malloc0().

**Definition** dbus-memory.h:60

dbus_malloc

void \* dbus_malloc(size_t bytes)

Allocates the given number of bytes, as with standard malloc().

**Definition** dbus-memory.c:470

DBusFreedElement

struct representing an element on the free list.

**Definition** dbus-mempool.c:66

DBusFreedElement::next

DBusFreedElement \* next

next element of the free list

**Definition** dbus-mempool.c:67

DBusMemBlock

DBusMemBlock object represents a single malloc()-returned block that gets chunked up into objects in ...

**Definition** dbus-mempool.c:81

DBusMemBlock::used_so_far

size_t used_so_far

bytes of this block already allocated as elements.

**Definition** dbus-mempool.c:87

DBusMemBlock::elements

unsigned char elements\[\]

the block data, actually allocated to required size

**Definition** dbus-mempool.c:96

DBusMemBlock::next

DBusMemBlock \* next

next block in the list, which is already used up; only saved so we can free all the blocks when we fr...

**Definition** dbus-mempool.c:82

DBusMemPool

Internals fields of DBusMemPool.

**Definition** dbus-mempool.c:109

DBusMemPool::allocated_elements

int allocated_elements

Count of outstanding allocated elements.

**Definition** dbus-mempool.c:116

DBusMemPool::zero_elements

unsigned int zero_elements

whether to zero-init allocated elements

**Definition** dbus-mempool.c:112

DBusMemPool::block_size

size_t block_size

size of most recently allocated block

**Definition** dbus-mempool.c:111

DBusMemPool::blocks

DBusMemBlock \* blocks

blocks of memory from malloc()

**Definition** dbus-mempool.c:115

DBusMemPool::element_size

size_t element_size

size of a single object in the pool

**Definition** dbus-mempool.c:110

DBusMemPool::free_elements

DBusFreedElement \* free_elements

a free list of elements to recycle

**Definition** dbus-mempool.c:114

DBusBasicValue

A simple value union that lets you access bytes as if they were various types; useful when dealing wi...

**Definition** dbus-types.h:161
