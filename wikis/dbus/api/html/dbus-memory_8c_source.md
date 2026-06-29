dbus-memory.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-memory.c D-Bus memory handling

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

27\#include "dbus-memory.h"

28\#include "dbus-internals.h"

29\#include "dbus-sysdeps.h"

30\#include "dbus-list.h"

31\#include "dbus-threads.h"

32\#include \<dbus/dbus-test-tap.h\>

33\#include \<stdlib.h\>

34

/\* end of public API docs \*/

96

103\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

104/\* Test-only, does not need to be thread-safe \*/

105static dbus_bool_t debug_initialized = FALSE;

106static int fail_nth = -1;

107static size_t fail_size = 0;

108static int fail_alloc_counter = -1;

109static int n_failures_per_failure = 1;

110static int n_failures_this_failure = 0;

111static dbus_bool_t guards = FALSE;

112static dbus_bool_t disable_mem_pools = FALSE;

113static dbus_bool_t backtrace_on_fail_alloc = FALSE;

114static dbus_bool_t malloc_cannot_fail = FALSE;

115static DBusAtomic n_blocks_outstanding = {0};

116

118\#define GUARD_VALUE 0xdeadbeef

120\#define GUARD_INFO_SIZE 8

122\#define GUARD_START_PAD 16

124\#define GUARD_END_PAD 16

126\#define GUARD_START_OFFSET (GUARD_START_PAD + GUARD_INFO_SIZE)

128\#define GUARD_EXTRA_SIZE (GUARD_START_OFFSET + GUARD_END_PAD)

129

130static void

131\_dbus_initialize_malloc_debug (void)

132{

133 if (!debug_initialized)

134 {

135 debug_initialized = TRUE;

136

137 if (\_dbus_getenv ("DBUS_MALLOC_FAIL_NTH") != NULL)

138 {

139 fail_nth = atoi (\_dbus_getenv ("DBUS_MALLOC_FAIL_NTH"));

140 fail_alloc_counter = fail_nth;

141 \_dbus_verbose ("Will fail dbus_malloc every %d times\n", fail_nth);

142 }

143

144 if (\_dbus_getenv ("DBUS_MALLOC_FAIL_GREATER_THAN") != NULL)

145 {

146 fail_size = atoi (\_dbus_getenv ("DBUS_MALLOC_FAIL_GREATER_THAN"));

147 \_dbus_verbose ("Will fail mallocs over %ld bytes\n",

148 (long) fail_size);

149 }

150

151 if (\_dbus_getenv ("DBUS_MALLOC_GUARDS") != NULL)

152 {

153 guards = TRUE;

154 \_dbus_verbose ("Will use dbus_malloc guards\n");

155 }

156

157 if (\_dbus_getenv ("DBUS_DISABLE_MEM_POOLS") != NULL)

158 {

159 disable_mem_pools = TRUE;

160 \_dbus_verbose ("Will disable memory pools\n");

161 }

162

163 if (\_dbus_getenv ("DBUS_MALLOC_BACKTRACES") != NULL)

164 {

165 backtrace_on_fail_alloc = TRUE;

166 \_dbus_verbose ("Will backtrace on failing a dbus_malloc\n");

167 }

168

169 if (\_dbus_getenv ("DBUS_MALLOC_CANNOT_FAIL") != NULL)

170 {

171 malloc_cannot_fail = TRUE;

172 \_dbus_verbose ("Will abort if system malloc() and friends fail\n");

173 }

174 }

175}

176

182dbus_bool_t

183\_dbus_disable_mem_pools (void)

184{

185 \_dbus_initialize_malloc_debug ();

186 return disable_mem_pools;

187}

188

201void

202\_dbus_set_fail_alloc_counter (int until_next_fail)

203{

204 \_dbus_initialize_malloc_debug ();

205

206 fail_alloc_counter = until_next_fail;

207

208\#if 0

209 \_dbus_verbose ("Set fail alloc counter = %d\n", fail_alloc_counter);

210\#endif

211}

212

223int

224\_dbus_get_fail_alloc_counter (void)

225{

226 \_dbus_initialize_malloc_debug ();

227

228 return fail_alloc_counter;

229}

230

237void

238\_dbus_set_fail_alloc_failures (int failures_per_failure)

239{

240 n_failures_per_failure = failures_per_failure;

241}

242

249int

250\_dbus_get_fail_alloc_failures (void)

251{

252 return n_failures_per_failure;

253}

254

263dbus_bool_t

264\_dbus_decrement_fail_alloc_counter (void)

265{

266 \_dbus_initialize_malloc_debug ();

267

268 if (fail_alloc_counter \< 0)

269 {

270 /\* We never fail in this case, but we still decrement the counter,

271 \* so that \_dbus_test_oom_handling() can use it to count allocations.

272 \* Saturate at \_DBUS_INT_MIN to avoid undefined integer overflow

273 \* (or in this case underflow). \*/

274 if (fail_alloc_counter \> \_DBUS_INT_MIN)

275 fail_alloc_counter -= 1;

276

277 return FALSE;

278 }

279 else if (fail_alloc_counter == 0)

280 {

281 /\* It's time to pretend we ran out of memory. \*/

282 if (backtrace_on_fail_alloc)

283 \_dbus_print_backtrace ();

284

285 \_dbus_verbose ("failure %d\n", n_failures_this_failure);

286

287 n_failures_this_failure += 1;

288 if (n_failures_this_failure \>= n_failures_per_failure)

289 {

290 fail_alloc_counter = fail_nth;

291 n_failures_this_failure = 0;

292

293 \_dbus_verbose ("reset fail alloc counter to %d\n", fail_alloc_counter);

294 }

295

296 return TRUE;

297 }

298 else

299 {

300 /\* Don't fail this allocation, but count down to the next time we

301 \* will fail an allocation. \*/

302 fail_alloc_counter -= 1;

303 return FALSE;

304 }

305}

306

312int

313\_dbus_get_malloc_blocks_outstanding (void)

314{

315 return \_dbus_atomic_get (&n_blocks_outstanding);

316}

317

321typedef enum

322{

323 SOURCE_UNKNOWN,

324 SOURCE_MALLOC,

325 SOURCE_REALLOC,

326 SOURCE_MALLOC_ZERO,

327 SOURCE_REALLOC_NULL

328} BlockSource;

329

330static const char\*

331source_string (BlockSource source)

332{

333 switch (source)

334 {

335 case SOURCE_UNKNOWN:

336 return "unknown";

337 case SOURCE_MALLOC:

338 return "malloc";

339 case SOURCE_REALLOC:

340 return "realloc";

341 case SOURCE_MALLOC_ZERO:

342 return "malloc0";

343 case SOURCE_REALLOC_NULL:

344 return "realloc(NULL)";

345 default:

346 \_dbus_assert_not_reached ("Invalid malloc block source ID");

347 return "invalid!";

348 }

349}

350

351static void

352check_guards (void \*free_block,

353 dbus_bool_t overwrite)

354{

355 if (free_block != NULL)

356 {

357 unsigned char \*block = ((unsigned char\*)free_block) - GUARD_START_OFFSET;

358 size_t requested_bytes = \*(dbus_uint32_t \*) (void \*) block;

359 BlockSource source = \*(dbus_uint32_t \*) (void \*) (block + 4);

360 unsigned int i;

361 dbus_bool_t failed;

362

363 failed = FALSE;

364

365\#if 0

366 \_dbus_verbose ("Checking %d bytes request from source %s\n",

367 requested_bytes, source_string (source));

368\#endif

369

370 i = GUARD_INFO_SIZE;

371 while (i \< GUARD_START_OFFSET)

372 {

373 dbus_uint32_t value = \*(dbus_uint32_t \*) (void \*) &block\[i\];

374 if (value != GUARD_VALUE)

375 {

376 \_dbus_warn ("Block of %lu bytes from %s had start guard value 0x%ux at %d expected 0x%x",

377 (long) requested_bytes, source_string (source),

378 value, i, GUARD_VALUE);

379 failed = TRUE;

380 }

381

382 i += 4;

383 }

384

385 i = GUARD_START_OFFSET + requested_bytes;

386 while (i \< (GUARD_START_OFFSET + requested_bytes + GUARD_END_PAD))

387 {

388 dbus_uint32_t value = \*(dbus_uint32_t \*) (void \*) &block\[i\];

389 if (value != GUARD_VALUE)

390 {

391 \_dbus_warn ("Block of %lu bytes from %s had end guard value 0x%ux at %d expected 0x%x",

392 (long) requested_bytes, source_string (source),

393 value, i, GUARD_VALUE);

394 failed = TRUE;

395 }

396

397 i += 4;

398 }

399

400 /\* set memory to anything but nul bytes \*/

401 if (overwrite)

402 memset (free_block, 'g', requested_bytes);

403

404 if (failed)

405 \_dbus_assert_not_reached ("guard value corruption");

406 }

407}

408

409static void\*

410set_guards (void \*real_block,

411 size_t requested_bytes,

412 BlockSource source)

413{

414 unsigned char \*block = real_block;

415 unsigned int i;

416

417 if (block == NULL)

418 return NULL;

419

420 \_dbus_assert (GUARD_START_OFFSET + GUARD_END_PAD == GUARD_EXTRA_SIZE);

421

422 \*((dbus_uint32_t \*) (void \*) block) = requested_bytes;

423 \*((dbus_uint32_t \*) (void \*) (block + 4)) = source;

424

425 i = GUARD_INFO_SIZE;

426 while (i \< GUARD_START_OFFSET)

427 {

428 (\*(dbus_uint32_t \*) (void \*) &block\[i\]) = GUARD_VALUE;

429

430 i += 4;

431 }

432

433 i = GUARD_START_OFFSET + requested_bytes;

434 while (i \< (GUARD_START_OFFSET + requested_bytes + GUARD_END_PAD))

435 {

436 (\*(dbus_uint32_t \*) (void \*) &block\[i\]) = GUARD_VALUE;

437

438 i += 4;

439 }

440

441 check_guards (block + GUARD_START_OFFSET, FALSE);

442

443 return block + GUARD_START_OFFSET;

444}

445

446\#endif

447

/\* End of internals docs \*/

449

450

469void\*

470dbus_malloc (size_t bytes)

471{

472\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

473 \_dbus_initialize_malloc_debug ();

474

475 if (\_dbus_decrement_fail_alloc_counter ())

476 {

477 \_dbus_verbose (" FAILING malloc of %ld bytes\n", (long) bytes);

478 return NULL;

479 }

480\#endif

481

482 if (bytes == 0) /\* some system mallocs handle this, some don't \*/

483 return NULL;

484\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

485 else if (fail_size != 0 && bytes \> fail_size)

486 return NULL;

487 else if (guards)

488 {

489 void \*block;

490

491 block = malloc (bytes + GUARD_EXTRA_SIZE);

492 if (block)

493 {

494 \_dbus_atomic_inc (&n_blocks_outstanding);

495 }

496 else if (malloc_cannot_fail)

497 {

498 \_dbus_warn ("out of memory: malloc (%ld + %ld)",

499 (long) bytes, (long) GUARD_EXTRA_SIZE);

500 \_dbus_abort ();

501 }

502

503 return set_guards (block, bytes, SOURCE_MALLOC);

504 }

505\#endif

506 else

507 {

508 void \*mem;

509 mem = malloc (bytes);

510

511\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

512 if (mem)

513 {

514 \_dbus_atomic_inc (&n_blocks_outstanding);

515 }

516 else if (malloc_cannot_fail)

517 {

518 \_dbus_warn ("out of memory: malloc (%ld)", (long) bytes);

519 \_dbus_abort ();

520 }

521\#endif

522

523 return mem;

524 }

525}

526

539void\*

540dbus_malloc0 (size_t bytes)

541{

542\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

543 \_dbus_initialize_malloc_debug ();

544

545 if (\_dbus_decrement_fail_alloc_counter ())

546 {

547 \_dbus_verbose (" FAILING malloc0 of %ld bytes\n", (long) bytes);

548

549 return NULL;

550 }

551\#endif

552

553 if (bytes == 0)

554 return NULL;

555\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

556 else if (fail_size != 0 && bytes \> fail_size)

557 return NULL;

558 else if (guards)

559 {

560 void \*block;

561

562 block = calloc (bytes + GUARD_EXTRA_SIZE, 1);

563

564 if (block)

565 {

566 \_dbus_atomic_inc (&n_blocks_outstanding);

567 }

568 else if (malloc_cannot_fail)

569 {

570 \_dbus_warn ("out of memory: calloc (%ld + %ld, 1)",

571 (long) bytes, (long) GUARD_EXTRA_SIZE);

572 \_dbus_abort ();

573 }

574

575 return set_guards (block, bytes, SOURCE_MALLOC_ZERO);

576 }

577\#endif

578 else

579 {

580 void \*mem;

581 mem = calloc (bytes, 1);

582

583\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

584 if (mem)

585 {

586 \_dbus_atomic_inc (&n_blocks_outstanding);

587 }

588 else if (malloc_cannot_fail)

589 {

590 \_dbus_warn ("out of memory: calloc (%ld)", (long) bytes);

591 \_dbus_abort ();

592 }

593\#endif

594

595 return mem;

596 }

597}

598

609void\*

610dbus_realloc (void \*memory,

611 size_t bytes)

612{

613\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

614 \_dbus_initialize_malloc_debug ();

615

616 if (\_dbus_decrement_fail_alloc_counter ())

617 {

618 \_dbus_verbose (" FAILING realloc of %ld bytes\n", (long) bytes);

619

620 return NULL;

621 }

622\#endif

623

624 if (bytes == 0) /\* guarantee this is safe \*/

625 {

626 dbus_free (memory);

627 return NULL;

628 }

629\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

630 else if (fail_size != 0 && bytes \> fail_size)

631 return NULL;

632 else if (guards)

633 {

634 if (memory)

635 {

636 size_t old_bytes;

637 void \*block;

638

639 check_guards (memory, FALSE);

640

641 block = realloc (((unsigned char\*)memory) - GUARD_START_OFFSET,

642 bytes + GUARD_EXTRA_SIZE);

643

644 if (block == NULL)

645 {

646 if (malloc_cannot_fail)

647 {

648 \_dbus_warn ("out of memory: realloc (%p, %ld + %ld)",

649 memory, (long) bytes, (long) GUARD_EXTRA_SIZE);

650 \_dbus_abort ();

651 }

652

653 return NULL;

654 }

655

656 old_bytes = \*(dbus_uint32_t\*)block;

657 if (bytes \>= old_bytes)

658 /\* old guards shouldn't have moved \*/

659 check_guards (((unsigned char\*)block) + GUARD_START_OFFSET, FALSE);

660

661 return set_guards (block, bytes, SOURCE_REALLOC);

662 }

663 else

664 {

665 void \*block;

666

667 block = malloc (bytes + GUARD_EXTRA_SIZE);

668

669 if (block)

670 {

671 \_dbus_atomic_inc (&n_blocks_outstanding);

672 }

673 else if (malloc_cannot_fail)

674 {

675 \_dbus_warn ("out of memory: malloc (%ld + %ld)",

676 (long) bytes, (long) GUARD_EXTRA_SIZE);

677 \_dbus_abort ();

678 }

679

680 return set_guards (block, bytes, SOURCE_REALLOC_NULL);

681 }

682 }

683\#endif

684 else

685 {

686 void \*mem;

687 mem = realloc (memory, bytes);

688

689\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

690 if (mem == NULL && malloc_cannot_fail)

691 {

692 \_dbus_warn ("out of memory: malloc (%ld)", (long) bytes);

693 \_dbus_abort ();

694 }

695

696 if (memory == NULL && mem != NULL)

697 \_dbus_atomic_inc (&n_blocks_outstanding);

698\#endif

699 return mem;

700 }

701}

702

709void

710dbus_free (void \*memory)

711{

712\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

713 if (guards)

714 {

715 check_guards (memory, TRUE);

716 if (memory)

717 {

718\#ifdef DBUS_DISABLE_ASSERT

719 \_dbus_atomic_dec (&n_blocks_outstanding);

720\#else

721 dbus_int32_t old_value;

722

723 old_value = \_dbus_atomic_dec (&n_blocks_outstanding);

724 \_dbus_assert (old_value \>= 1);

725\#endif

726

727 free (((unsigned char\*)memory) - GUARD_START_OFFSET);

728 }

729

730 return;

731 }

732\#endif

733

734 if (memory) /\* we guarantee it's safe to free (NULL) \*/

735 {

736\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

737\#ifdef DBUS_DISABLE_ASSERT

738 \_dbus_atomic_dec (&n_blocks_outstanding);

739\#else

740 dbus_int32_t old_value;

741

742 old_value = \_dbus_atomic_dec (&n_blocks_outstanding);

743 \_dbus_assert (old_value \>= 1);

744\#endif

745\#endif

746

747 free (memory);

748 }

749}

750

757void

758dbus_free_string_array (char \*\*str_array)

759{

760 if (str_array)

761 {

762 int i;

763

764 i = 0;

765 while (str_array\[i\])

766 {

767 dbus_free (str_array\[i\]);

768 i++;

769 }

770

771 dbus_free (str_array);

772 }

773}

774

/\* End of public API docs block \*/

776

777

790int \_dbus_current_generation = 1;

791

795typedef struct ShutdownClosure ShutdownClosure;

796

800struct ShutdownClosure

801{

802 ShutdownClosure \*next;

803 DBusShutdownFunction func;

804 void \*data;

805};

806

807/\* Protected by \_DBUS_LOCK (shutdown_funcs) \*/

808static ShutdownClosure \*registered_globals = NULL;

809

818dbus_bool_t

819\_dbus_register_shutdown_func (DBusShutdownFunction func,

820 void \*data)

821{

822 dbus_bool_t ok;

823

824 if (!\_DBUS_LOCK (shutdown_funcs))

825 return FALSE;

826

827 ok = \_dbus_register_shutdown_func_unlocked (func, data);

828 \_DBUS_UNLOCK (shutdown_funcs);

829 return ok;

830}

831

832dbus_bool_t

833\_dbus_register_shutdown_func_unlocked (DBusShutdownFunction func,

834 void \*data)

835{

836 ShutdownClosure \*c;

837

838 c = dbus_new (ShutdownClosure, 1);

839

840 if (c == NULL)

841 return FALSE;

842

843 c-\>func = func;

844 c-\>data = data;

845

846 c-\>next = registered_globals;

847 registered_globals = c;

848

849 return TRUE;

850}

851

/\* End of private API docs block \*/

853

854

905void

906dbus_shutdown (void)

907{

908 while (registered_globals != NULL)

909 {

910 ShutdownClosure \*c;

911

912 c = registered_globals;

913 registered_globals = c-\>next;

914

915 (\* c-\>func) (c-\>data);

916

917 dbus_free (c);

918 }

919

920 /\* We wrap this in the thread-initialization lock because

921 \* dbus_threads_init() uses the current generation to tell whether

922 \* we're initialized, so we need to make sure that un-initializing

923 \* propagates into all threads. \*/

924 \_dbus_threads_lock_platform_specific ();

925 \_dbus_current_generation += 1;

926 \_dbus_threads_unlock_platform_specific ();

927}

928

931\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

932\#include "dbus-test.h"

933

939dbus_bool_t

940\_dbus_memory_test (const char \*test_data_dir \_DBUS_GNUC_UNUSED)

941{

942 dbus_bool_t old_guards;

943 void \*p;

944 size_t size;

945

946 old_guards = guards;

947 guards = TRUE;

948 p = dbus_malloc (4);

949 if (p == NULL)

950 \_dbus_test_fatal ("no memory");

951 for (size = 4; size \< 256; size += 4)

952 {

953 p = dbus_realloc (p, size);

954 if (p == NULL)

955 \_dbus_test_fatal ("no memory");

956 }

957 for (size = 256; size != 0; size -= 4)

958 {

959 p = dbus_realloc (p, size);

960 if (p == NULL)

961 \_dbus_test_fatal ("no memory");

962 }

963 dbus_free (p);

964 guards = old_guards;

965 return TRUE;

966}

967

968\#endif

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

\_DBUS_INT_MIN

\#define \_DBUS_INT_MIN

Minimum value of type "int".

**Definition** dbus-internals.h:326

\_dbus_warn

void \_dbus_warn(const char \*format,...)

Prints a warning message to stderr.

**Definition** dbus-internals.c:278

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

\_dbus_current_generation

int \_dbus_current_generation

\_dbus_current_generation is used to track each time that dbus_shutdown() is called,...

**Definition** dbus-memory.c:790

\_dbus_register_shutdown_func

dbus_bool_t \_dbus_register_shutdown_func(DBusShutdownFunction func, void \*data)

Register a cleanup function to be called exactly once the next time dbus_shutdown() is called.

**Definition** dbus-memory.c:819

dbus_shutdown

void dbus_shutdown(void)

Frees all memory allocated internally by libdbus and reverses the effects of dbus_threads_init().

**Definition** dbus-memory.c:906

dbus_free

void dbus_free(void \*memory)

Frees a block of memory previously allocated by dbus_malloc() or dbus_malloc0().

**Definition** dbus-memory.c:710

dbus_realloc

void \* dbus_realloc(void \*memory, size_t bytes)

Resizes a block of memory previously allocated by dbus_malloc() or dbus_malloc0().

**Definition** dbus-memory.c:610

dbus_new

\#define dbus_new(type, count)

Safe macro for using dbus_malloc().

**Definition** dbus-memory.h:59

dbus_malloc0

void \* dbus_malloc0(size_t bytes)

Allocates the given number of bytes, as with standard malloc(), but all bytes are initialized to zero...

**Definition** dbus-memory.c:540

dbus_free_string_array

void dbus_free_string_array(char \*\*str_array)

Frees a NULL-terminated array of strings.

**Definition** dbus-memory.c:758

dbus_malloc

void \* dbus_malloc(size_t bytes)

Allocates the given number of bytes, as with standard malloc().

**Definition** dbus-memory.c:470

\_dbus_atomic_dec

dbus_int32_t \_dbus_atomic_dec(DBusAtomic \*atomic)

Atomically decrement an integer.

**Definition** dbus-sysdeps-unix.c:3205

\_dbus_getenv

const char \* \_dbus_getenv(const char \*varname)

Wrapper for getenv().

**Definition** dbus-sysdeps.c:197

\_dbus_atomic_get

dbus_int32_t \_dbus_atomic_get(DBusAtomic \*atomic)

Atomically get the value of an integer.

**Definition** dbus-sysdeps-unix.c:3233

\_dbus_threads_lock_platform_specific

void \_dbus_threads_lock_platform_specific(void)

Lock a static mutex used to protect \_dbus_threads_init_platform_specific().

**Definition** dbus-sysdeps-pthread.c:296

\_dbus_threads_unlock_platform_specific

void \_dbus_threads_unlock_platform_specific(void)

Undo \_dbus_threads_lock_platform_specific().

**Definition** dbus-sysdeps-pthread.c:302

\_dbus_atomic_inc

dbus_int32_t \_dbus_atomic_inc(DBusAtomic \*atomic)

Atomically increments an integer.

**Definition** dbus-sysdeps-unix.c:3178

\_dbus_abort

void \_dbus_abort(void)

Aborts the program with SIGABRT (dumping core).

**Definition** dbus-sysdeps.c:89

DBusAtomic

An atomic integer safe to increment or decrement from multiple threads.

**Definition** dbus-sysdeps.h:340

ShutdownClosure

This struct represents a function to be called on shutdown.

**Definition** dbus-memory.c:801

ShutdownClosure::next

ShutdownClosure \* next

Next ShutdownClosure.

**Definition** dbus-memory.c:802

ShutdownClosure::func

DBusShutdownFunction func

Function to call.

**Definition** dbus-memory.c:803

ShutdownClosure::data

void \* data

Data for function.

**Definition** dbus-memory.c:804
