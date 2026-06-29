dbus-hash.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-hash.c Generic hash table utility (internal to D-Bus implementation)

3 \*

4 \* Copyright 1991-1993 The Regents of the University of California.

5 \* Copyright 1994 Sun Microsystems, Inc.

6 \* Copyright 2002-2005 Red Hat, Inc.

7 \* Copyright 2003 Joe Shaw

8 \* Copyright 2006 Sjoerd Simons

9 \* Copyright 2010 Fridrich Štrba

10 \* Copyright 2016 Ralf Habacker

11 \* Copyright 2017 Endless Mobile, Inc.

12 \* SPDX-License-Identifier: (AFL-2.1 OR GPL-2.0-or-later) AND TCL

13 \*

14 \* Hash table implementation based on generic/tclHash.c from the Tcl

15 \* source code. The original Tcl license applies to portions of the

16 \* code from tclHash.c; the Tcl license follows this standad D-Bus

17 \* license information.

18 \*

19 \* Licensed under the Academic Free License version 2.1

20 \*

21 \* This program is free software; you can redistribute it and/or modify

22 \* it under the terms of the GNU General Public License as published by

23 \* the Free Software Foundation; either version 2 of the License, or

24 \* (at your option) any later version.

25 \*

26 \* This program is distributed in the hope that it will be useful,

27 \* but WITHOUT ANY WARRANTY; without even the implied warranty of

28 \* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the

29 \* GNU General Public License for more details.

30 \*

31 \* You should have received a copy of the GNU General Public License

32 \* along with this program; if not, write to the Free Software

33 \* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

34 \*

35 \*/

36/\*

37 \* The following copyright applies to code from the Tcl distribution.

38 \*

39 \* Copyright (c) 1991-1993 The Regents of the University of California.

40 \* Copyright (c) 1994 Sun Microsystems, Inc.

41 \*

42 \* This software is copyrighted by the Regents of the University of

43 \* California, Sun Microsystems, Inc., Scriptics Corporation, and

44 \* other parties. The following terms apply to all files associated

45 \* with the software unless explicitly disclaimed in individual files.

46 \*

47 \* The authors hereby grant permission to use, copy, modify,

48 \* distribute, and license this software and its documentation for any

49 \* purpose, provided that existing copyright notices are retained in

50 \* all copies and that this notice is included verbatim in any

51 \* distributions. No written agreement, license, or royalty fee is

52 \* required for any of the authorized uses. Modifications to this

53 \* software may be copyrighted by their authors and need not follow

54 \* the licensing terms described here, provided that the new terms are

55 \* clearly indicated on the first page of each file where they apply.

56 \*

57 \* IN NO EVENT SHALL THE AUTHORS OR DISTRIBUTORS BE LIABLE TO ANY

58 \* PARTY FOR DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL

59 \* DAMAGES ARISING OUT OF THE USE OF THIS SOFTWARE, ITS DOCUMENTATION,

60 \* OR ANY DERIVATIVES THEREOF, EVEN IF THE AUTHORS HAVE BEEN ADVISED

61 \* OF THE POSSIBILITY OF SUCH DAMAGE.

62 \*

63 \* THE AUTHORS AND DISTRIBUTORS SPECIFICALLY DISCLAIM ANY WARRANTIES,

64 \* INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF

65 \* MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND

66 \* NON-INFRINGEMENT. THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS,

67 \* AND THE AUTHORS AND DISTRIBUTORS HAVE NO OBLIGATION TO PROVIDE

68 \* MAINTENANCE, SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.

69 \*

70 \* GOVERNMENT USE: If you are acquiring this software on behalf of the

71 \* U.S. government, the Government shall have only "Restricted Rights"

72 \* in the software and related documentation as defined in the Federal

73 \* Acquisition Regulations (FARs) in Clause 52.227.19 (c) (2). If you

74 \* are acquiring the software on behalf of the Department of Defense,

75 \* the software shall be classified as "Commercial Computer Software"

76 \* and the Government shall have only "Restricted Rights" as defined

77 \* in Clause 252.227-7013 (c) (1) of DFARs. Notwithstanding the

78 \* foregoing, the authors grant the U.S. Government and others acting

79 \* in its behalf permission to use and distribute the software in

80 \* accordance with the terms specified in this license.

81 \*/

82

83\#include \<config.h\>

84\#include "dbus-hash.h"

85\#include "dbus-internals.h"

86\#include "dbus-mempool.h"

87\#include \<dbus/dbus-test-tap.h\>

88

111\#define REBUILD_MULTIPLIER 3

112

129\#define RANDOM_INDEX(table, i) \\

130 (((((uintptr_t) (i))\*1103515245) \>\> (table)-\>down_shift) & (table)-\>mask)

131

137\#define DBUS_SMALL_HASH_TABLE 4

138

142typedef struct DBusHashEntry DBusHashEntry;

143

150struct DBusHashEntry

151{

152 DBusHashEntry \*next;

156 void \*key;

157 void \*value;

158};

159

163typedef DBusHashEntry\* (\* DBusFindEntryFunction) (DBusHashTable \*table,

164 void \*key,

165 dbus_bool_t create_if_not_found,

166 DBusHashEntry \*\*\*bucket,

167 DBusPreallocatedHash \*preallocated);

168

175struct DBusHashTable {

176 int refcount;

178 DBusHashEntry \*\*buckets;

182 DBusHashEntry \*static_buckets\[DBUS_SMALL_HASH_TABLE\];

186 int n_buckets;

189 int n_entries;

192 int hi_rebuild_size;

195 int lo_rebuild_size;

198 int down_shift;

202 int mask;

205 DBusHashType key_type;

208 DBusFindEntryFunction find_function;

210 DBusFreeFunction free_key_function;

211 DBusFreeFunction free_value_function;

213 DBusMemPool \*entry_pool;

214};

215

219typedef struct

220{

221 DBusHashTable \*table;

222 DBusHashEntry \*\*bucket;

226 DBusHashEntry \*entry;

227 DBusHashEntry \*next_entry;

228 int next_bucket;

229 int n_entries_on_init;

230} DBusRealHashIter;

231

232\_DBUS_STATIC_ASSERT (sizeof (DBusRealHashIter) == sizeof (DBusHashIter));

233

234static DBusHashEntry\* find_direct_function (DBusHashTable \*table,

235 void \*key,

236 dbus_bool_t create_if_not_found,

237 DBusHashEntry \*\*\*bucket,

238 DBusPreallocatedHash \*preallocated);

239static DBusHashEntry\* find_string_function (DBusHashTable \*table,

240 void \*key,

241 dbus_bool_t create_if_not_found,

242 DBusHashEntry \*\*\*bucket,

243 DBusPreallocatedHash \*preallocated);

244static unsigned int string_hash (const char \*str);

245static dbus_bool_t rebuild_table (DBusHashTable \*table);

246static DBusHashEntry\* alloc_entry (DBusHashTable \*table);

247static void remove_entry (DBusHashTable \*table,

248 DBusHashEntry \*\*bucket,

249 DBusHashEntry \*entry);

250static void free_entry (DBusHashTable \*table,

251 DBusHashEntry \*entry);

252static void free_entry_data (DBusHashTable \*table,

253 DBusHashEntry \*entry);

254

255

291DBusHashTable\*

292\_dbus_hash_table_new (DBusHashType type,

293 DBusFreeFunction key_free_function,

294 DBusFreeFunction value_free_function)

295{

296 DBusHashTable \*table;

297 DBusMemPool \*entry_pool;

298

299 table = dbus_new0 (DBusHashTable, 1);

300 if (table == NULL)

301 return NULL;

302

303 entry_pool = \_dbus_mem_pool_new (sizeof (DBusHashEntry), TRUE);

304 if (entry_pool == NULL)

305 {

306 dbus_free (table);

307 return NULL;

308 }

309

310 table-\>refcount = 1;

311 table-\>entry_pool = entry_pool;

312

313 \_dbus_assert (DBUS_SMALL_HASH_TABLE == \_DBUS_N_ELEMENTS (table-\>static_buckets));

314

315 table-\>buckets = table-\>static_buckets;

316 table-\>n_buckets = DBUS_SMALL_HASH_TABLE;

317 table-\>n_entries = 0;

318 table-\>hi_rebuild_size = DBUS_SMALL_HASH_TABLE \* REBUILD_MULTIPLIER;

319 table-\>lo_rebuild_size = 0;

320 table-\>down_shift = 28;

321 table-\>mask = 3;

322 table-\>key_type = type;

323

324 \_dbus_assert (table-\>mask \< table-\>n_buckets);

325

326 switch (table-\>key_type)

327 {

328 case DBUS_HASH_INT:

329 case DBUS_HASH_UINTPTR:

330 table-\>find_function = find_direct_function;

331 break;

332 case DBUS_HASH_STRING:

333 table-\>find_function = find_string_function;

334 break;

335 default:

336 \_dbus_assert_not_reached ("Unknown hash table type");

337 break;

338 }

339

340 table-\>free_key_function = key_free_function;

341 table-\>free_value_function = value_free_function;

342

343 return table;

344}

345

346

353DBusHashTable \*

354\_dbus_hash_table_ref (DBusHashTable \*table)

355{

356 table-\>refcount += 1;

357

358 return table;

359}

360

367void

368\_dbus_hash_table_unref (DBusHashTable \*table)

369{

370 table-\>refcount -= 1;

371

372 if (table-\>refcount == 0)

373 {

374\#if 0

375 DBusHashEntry \*entry;

376 DBusHashEntry \*next;

377 int i;

378

379 /\* Free the entries in the table. \*/

380 for (i = 0; i \< table-\>n_buckets; i++)

381 {

382 entry = table-\>buckets\[i\];

383 while (entry != NULL)

384 {

385 next = entry-\>next;

386

387 free_entry (table, entry);

388

389 entry = next;

390 }

391 }

392\#else

393 DBusHashEntry \*entry;

394 int i;

395

396 /\* Free the entries in the table. \*/

397 for (i = 0; i \< table-\>n_buckets; i++)

398 {

399 entry = table-\>buckets\[i\];

400 while (entry != NULL)

401 {

402 free_entry_data (table, entry);

403

404 entry = entry-\>next;

405 }

406 }

407 /\* We can do this very quickly with memory pools ;-) \*/

408 \_dbus_mem_pool_free (table-\>entry_pool);

409\#endif

410

411 /\* Free the bucket array, if it was dynamically allocated. \*/

412 if (table-\>buckets != table-\>static_buckets)

413 dbus_free (table-\>buckets);

414

415 dbus_free (table);

416 }

417}

418

424void

425\_dbus_hash_table_remove_all (DBusHashTable \*table)

426{

427 DBusHashIter iter;

428 \_dbus_hash_iter_init (table, &iter);

429 while (\_dbus_hash_iter_next (&iter))

430 {

431 \_dbus_hash_iter_remove_entry(&iter);

432 }

433}

434

435static DBusHashEntry\*

436alloc_entry (DBusHashTable \*table)

437{

438 DBusHashEntry \*entry;

439

440 entry = \_dbus_mem_pool_alloc (table-\>entry_pool);

441

442 return entry;

443}

444

445static void

446free_entry_data (DBusHashTable \*table,

447 DBusHashEntry \*entry)

448{

449 if (table-\>free_key_function)

450 (\* table-\>free_key_function) (entry-\>key);

451 if (table-\>free_value_function)

452 (\* table-\>free_value_function) (entry-\>value);

453}

454

455static void

456free_entry (DBusHashTable \*table,

457 DBusHashEntry \*entry)

458{

459 free_entry_data (table, entry);

460 \_dbus_mem_pool_dealloc (table-\>entry_pool, entry);

461}

462

463static void

464remove_entry (DBusHashTable \*table,

465 DBusHashEntry \*\*bucket,

466 DBusHashEntry \*entry)

467{

468 \_dbus_assert (table != NULL);

469 \_dbus_assert (bucket != NULL);

470 \_dbus_assert (\*bucket != NULL);

471 \_dbus_assert (entry != NULL);

472

473 if (\*bucket == entry)

474 \*bucket = entry-\>next;

475 else

476 {

477 DBusHashEntry \*prev;

478 prev = \*bucket;

479

480 while (prev-\>next != entry)

481 prev = prev-\>next;

482

483 \_dbus_assert (prev != NULL);

484

485 prev-\>next = entry-\>next;

486 }

487

488 table-\>n_entries -= 1;

489 free_entry (table, entry);

490}

491

523void

524\_dbus_hash_iter_init (DBusHashTable \*table,

525 DBusHashIter \*iter)

526{

527 DBusRealHashIter \*real;

528

529 \_DBUS_STATIC_ASSERT (sizeof (DBusHashIter) == sizeof (DBusRealHashIter));

530

531 real = (DBusRealHashIter\*) iter;

532

533 real-\>table = table;

534 real-\>bucket = NULL;

535 real-\>entry = NULL;

536 real-\>next_entry = NULL;

537 real-\>next_bucket = 0;

538 real-\>n_entries_on_init = table-\>n_entries;

539}

540

549dbus_bool_t

550\_dbus_hash_iter_next (DBusHashIter \*iter)

551{

552 DBusRealHashIter \*real;

553

554 \_DBUS_STATIC_ASSERT (sizeof (DBusHashIter) == sizeof (DBusRealHashIter));

555

556 real = (DBusRealHashIter\*) iter;

557

558 /\* if this assertion failed someone probably added hash entries

559 \* during iteration, which is bad.

560 \*/

561 \_dbus_assert (real-\>n_entries_on_init \>= real-\>table-\>n_entries);

562

563 /\* Remember that real-\>entry may have been deleted \*/

564

565 while (real-\>next_entry == NULL)

566 {

567 if (real-\>next_bucket \>= real-\>table-\>n_buckets)

568 {

569 /\* invalidate iter and return false \*/

570 real-\>entry = NULL;

571 real-\>table = NULL;

572 real-\>bucket = NULL;

573 return FALSE;

574 }

575

576 real-\>bucket = &(real-\>table-\>buckets\[real-\>next_bucket\]);

577 real-\>next_entry = \*(real-\>bucket);

578 real-\>next_bucket += 1;

579 }

580

581 \_dbus_assert (real-\>next_entry != NULL);

582 \_dbus_assert (real-\>bucket != NULL);

583

584 real-\>entry = real-\>next_entry;

585 real-\>next_entry = real-\>entry-\>next;

586

587 return TRUE;

588}

589

598void

599\_dbus_hash_iter_remove_entry (DBusHashIter \*iter)

600{

601 DBusRealHashIter \*real;

602

603 real = (DBusRealHashIter\*) iter;

604

605 \_dbus_assert (real-\>table != NULL);

606 \_dbus_assert (real-\>entry != NULL);

607 \_dbus_assert (real-\>bucket != NULL);

608

609 remove_entry (real-\>table, real-\>bucket, real-\>entry);

610

611 real-\>entry = NULL; /\* make it crash if you try to use this entry \*/

612}

613

619void\*

620\_dbus_hash_iter_get_value (DBusHashIter \*iter)

621{

622 DBusRealHashIter \*real;

623

624 real = (DBusRealHashIter\*) iter;

625

626 \_dbus_assert (real-\>table != NULL);

627 \_dbus_assert (real-\>entry != NULL);

628

629 return real-\>entry-\>value;

630}

631

642void

643\_dbus_hash_iter_set_value (DBusHashIter \*iter,

644 void \*value)

645{

646 DBusRealHashIter \*real;

647

648 real = (DBusRealHashIter\*) iter;

649

650 \_dbus_assert (real-\>table != NULL);

651 \_dbus_assert (real-\>entry != NULL);

652

653 if (real-\>table-\>free_value_function && value != real-\>entry-\>value)

654 (\* real-\>table-\>free_value_function) (real-\>entry-\>value);

655

656 real-\>entry-\>value = value;

657}

658

665int

666\_dbus_hash_iter_get_int_key (DBusHashIter \*iter)

667{

668 DBusRealHashIter \*real;

669

670 real = (DBusRealHashIter\*) iter;

671

672 \_dbus_assert (real-\>table != NULL);

673 \_dbus_assert (real-\>entry != NULL);

674

675 return \_DBUS_POINTER_TO_INT (real-\>entry-\>key);

676}

677

684uintptr_t

685\_dbus_hash_iter_get_uintptr_key (DBusHashIter \*iter)

686{

687 DBusRealHashIter \*real;

688

689 real = (DBusRealHashIter\*) iter;

690

691 \_dbus_assert (real-\>table != NULL);

692 \_dbus_assert (real-\>entry != NULL);

693

694 return (uintptr_t) real-\>entry-\>key;

695}

696

702const char\*

703\_dbus_hash_iter_get_string_key (DBusHashIter \*iter)

704{

705 DBusRealHashIter \*real;

706

707 real = (DBusRealHashIter\*) iter;

708

709 \_dbus_assert (real-\>table != NULL);

710 \_dbus_assert (real-\>entry != NULL);

711

712 return real-\>entry-\>key;

713}

714

747dbus_bool_t

748\_dbus_hash_iter_lookup (DBusHashTable \*table,

749 void \*key,

750 dbus_bool_t create_if_not_found,

751 DBusHashIter \*iter)

752{

753 DBusRealHashIter \*real;

754 DBusHashEntry \*entry = NULL;

755 DBusHashEntry \*\*bucket = NULL;

756

757 \_DBUS_STATIC_ASSERT (sizeof (DBusHashIter) == sizeof (DBusRealHashIter));

758

759 real = (DBusRealHashIter\*) iter;

760

761 entry = (\* table-\>find_function) (table, key, create_if_not_found, &bucket, NULL);

762

763 /\* entry == NULL means not found, and either !create_if_not_found or OOM \*/

764 if (entry == NULL)

765 return FALSE;

766

767 \_dbus_assert (bucket != NULL);

768 \_dbus_assert (table-\>n_buckets \>= 1);

769 \_dbus_assert (bucket \>= table-\>buckets);

770 \_dbus_assert (bucket \<= &table-\>buckets\[table-\>n_buckets - 1\]);

771

772 if (create_if_not_found)

773 {

774 if (table-\>free_key_function && entry-\>key != key)

775 (\* table-\>free_key_function) (entry-\>key);

776

777 entry-\>key = key;

778 }

779

780 real-\>table = table;

781 real-\>bucket = bucket;

782 real-\>entry = entry;

783 real-\>next_entry = entry-\>next;

784 real-\>next_bucket = (bucket - table-\>buckets) + 1;

785 real-\>n_entries_on_init = table-\>n_entries;

786

787 \_dbus_assert (real-\>next_bucket \>= 0);

788 \_dbus_assert (real-\>next_bucket \<= table-\>n_buckets);

789 \_dbus_assert (&(table-\>buckets\[real-\>next_bucket-1\]) == real-\>bucket);

790

791 return TRUE;

792}

793

794static void

795add_allocated_entry (DBusHashTable \*table,

796 DBusHashEntry \*entry,

797 unsigned int idx,

798 void \*key,

799 DBusHashEntry \*\*\*bucket)

800{

801 DBusHashEntry \*\*b;

802

803 entry-\>key = key;

804

805 b = &(table-\>buckets\[idx\]);

806 entry-\>next = \*b;

807 \*b = entry;

808

809 if (bucket)

810 \*bucket = b;

811

812 table-\>n_entries += 1;

813

814 /\* note we ONLY rebuild when ADDING - because you can iterate over a

815 \* table and remove entries safely.

816 \*/

817 if (table-\>n_entries \>= table-\>hi_rebuild_size \|\|

818 table-\>n_entries \< table-\>lo_rebuild_size)

819 {

820 if (!rebuild_table (table))

821 return;

822

823 if (bucket)

824 {

825 /\* Recalculate hash for the new table size \*/

826 switch (table-\>key_type)

827 {

828 case DBUS_HASH_STRING:

829 idx = string_hash (entry-\>key) & table-\>mask;

830 break;

831

832 case DBUS_HASH_INT:

833 case DBUS_HASH_UINTPTR:

834 idx = RANDOM_INDEX (table, entry-\>key);

835 break;

836

837 default:

838 idx = 0;

839 \_dbus_assert_not_reached ("Unknown hash table type");

840 break;

841 }

842

843 \*bucket = &(table-\>buckets\[idx\]);

844 }

845 }

846}

847

848static DBusHashEntry\*

849add_entry (DBusHashTable \*table,

850 unsigned int idx,

851 void \*key,

852 DBusHashEntry \*\*\*bucket,

853 DBusPreallocatedHash \*preallocated)

854{

855 DBusHashEntry \*entry;

856

857 if (preallocated == NULL)

858 {

859 entry = alloc_entry (table);

860 if (entry == NULL)

861 {

862 if (bucket)

863 \*bucket = NULL;

864 return NULL;

865 }

866 }

867 else

868 {

869 entry = (DBusHashEntry\*) preallocated;

870 }

871

872 add_allocated_entry (table, entry, idx, key, bucket);

873 \_dbus_assert (bucket == NULL \|\| \*bucket != NULL);

874

875 return entry;

876}

877

878/\* This is g_str_hash from GLib which was

879 \* extensively discussed/tested/profiled

880 \*/

881static unsigned int

882string_hash (const char \*str)

883{

884 const char \*p = str;

885 unsigned int h = \*p;

886

887 if (h)

888 for (p += 1; \*p != '\0'; p++)

889 h = (h \<\< 5) - h + \*p;

890

891 return h;

892}

893

895typedef int (\* KeyCompareFunc) (const void \*key_a, const void \*key_b);

896

897static DBusHashEntry\*

898find_generic_function (DBusHashTable \*table,

899 void \*key,

900 unsigned int idx,

901 KeyCompareFunc compare_func,

902 dbus_bool_t create_if_not_found,

903 DBusHashEntry \*\*\*bucket,

904 DBusPreallocatedHash \*preallocated)

905{

906 DBusHashEntry \*entry;

907

908 if (bucket)

909 \*bucket = NULL;

910

911 /\* Search all of the entries in this bucket. \*/

912 entry = table-\>buckets\[idx\];

913 while (entry != NULL)

914 {

915 if ((compare_func == NULL && key == entry-\>key) \|\|

916 (compare_func != NULL && (\* compare_func) (key, entry-\>key) == 0))

917 {

918 if (bucket)

919 \*bucket = &(table-\>buckets\[idx\]);

920

921 if (preallocated)

922 \_dbus_hash_table_free_preallocated_entry (table, preallocated);

923

924 return entry;

925 }

926

927 entry = entry-\>next;

928 }

929

930 if (create_if_not_found)

931 {

932 entry = add_entry (table, idx, key, bucket, preallocated);

933

934 if (entry == NULL) /\* OOM \*/

935 return NULL;

936

937 \_dbus_assert (bucket == NULL \|\| \*bucket != NULL);

938 }

939 else if (preallocated)

940 {

941 \_dbus_hash_table_free_preallocated_entry (table, preallocated);

942 }

943

944 return entry;

945}

946

947static DBusHashEntry\*

948find_string_function (DBusHashTable \*table,

949 void \*key,

950 dbus_bool_t create_if_not_found,

951 DBusHashEntry \*\*\*bucket,

952 DBusPreallocatedHash \*preallocated)

953{

954 unsigned int idx;

955

956 idx = string_hash (key) & table-\>mask;

957

958 return find_generic_function (table, key, idx,

959 (KeyCompareFunc) strcmp, create_if_not_found, bucket,

960 preallocated);

961}

962

963static DBusHashEntry\*

964find_direct_function (DBusHashTable \*table,

965 void \*key,

966 dbus_bool_t create_if_not_found,

967 DBusHashEntry \*\*\*bucket,

968 DBusPreallocatedHash \*preallocated)

969{

970 unsigned int idx;

971

972 idx = RANDOM_INDEX (table, key) & table-\>mask;

973

974

975 return find_generic_function (table, key, idx,

976 NULL, create_if_not_found, bucket,

977 preallocated);

978}

979

980/\* Return FALSE if nothing happened. \*/

981static dbus_bool_t

982rebuild_table (DBusHashTable \*table)

983{

984 int old_size;

985 int new_buckets;

986 DBusHashEntry \*\*old_buckets;

987 DBusHashEntry \*\*old_chain;

988 DBusHashEntry \*entry;

989 dbus_bool_t growing;

990

991 /\*

992 \* Allocate and initialize the new bucket array, and set up

993 \* hashing constants for new array size.

994 \*/

995

996 growing = table-\>n_entries \>= table-\>hi_rebuild_size;

997

998 old_size = table-\>n_buckets;

999 old_buckets = table-\>buckets;

1000

1001 if (growing)

1002 {

1003 /\* overflow paranoia \*/

1004 if (table-\>n_buckets \< \_DBUS_INT_MAX / 4 &&

1005 table-\>down_shift \>= 2)

1006 new_buckets = table-\>n_buckets \* 4;

1007 else

1008 return FALSE; /\* can't grow any more \*/

1009 }

1010 else

1011 {

1012 new_buckets = table-\>n_buckets / 4;

1013 if (new_buckets \< DBUS_SMALL_HASH_TABLE)

1014 return FALSE; /\* don't bother shrinking this far \*/

1015 }

1016

1017 table-\>buckets = dbus_new0 (DBusHashEntry\*, new_buckets);

1018 if (table-\>buckets == NULL)

1019 {

1020 /\* out of memory, yay - just don't reallocate, the table will

1021 \* still work, albeit more slowly.

1022 \*/

1023 table-\>buckets = old_buckets;

1024 return FALSE;

1025 }

1026

1027 table-\>n_buckets = new_buckets;

1028

1029 if (growing)

1030 {

1031 table-\>lo_rebuild_size = table-\>hi_rebuild_size;

1032 table-\>hi_rebuild_size \*= 4;

1033

1034 table-\>down_shift -= 2; /\* keep 2 more high bits \*/

1035 table-\>mask = (table-\>mask \<\< 2) + 3; /\* keep 2 more high bits \*/

1036 }

1037 else

1038 {

1039 table-\>hi_rebuild_size = table-\>lo_rebuild_size;

1040 table-\>lo_rebuild_size /= 4;

1041

1042 table-\>down_shift += 2; /\* keep 2 fewer high bits \*/

1043 table-\>mask = table-\>mask \>\> 2; /\* keep 2 fewer high bits \*/

1044 }

1045

1046\#if 0

1047 printf ("%s table to lo = %d hi = %d downshift = %d mask = 0x%x\n",

1048 growing ? "GROW" : "SHRINK",

1049 table-\>lo_rebuild_size,

1050 table-\>hi_rebuild_size,

1051 table-\>down_shift,

1052 table-\>mask);

1053\#endif

1054

1055 \_dbus_assert (table-\>lo_rebuild_size \>= 0);

1056 \_dbus_assert (table-\>hi_rebuild_size \> table-\>lo_rebuild_size);

1057 \_dbus_assert (table-\>down_shift \>= 0);

1058 \_dbus_assert (table-\>mask != 0);

1059 /\* the mask is essentially the max index \*/

1060 \_dbus_assert (table-\>mask \< table-\>n_buckets);

1061

1062 /\*

1063 \* Rehash all of the existing entries into the new bucket array.

1064 \*/

1065

1066 for (old_chain = old_buckets; old_size \> 0; old_size--, old_chain++)

1067 {

1068 for (entry = \*old_chain; entry != NULL; entry = \*old_chain)

1069 {

1070 unsigned int idx;

1071 DBusHashEntry \*\*bucket;

1072

1073 \*old_chain = entry-\>next;

1074 switch (table-\>key_type)

1075 {

1076 case DBUS_HASH_STRING:

1077 idx = string_hash (entry-\>key) & table-\>mask;

1078 break;

1079 case DBUS_HASH_INT:

1080 case DBUS_HASH_UINTPTR:

1081 idx = RANDOM_INDEX (table, entry-\>key);

1082 break;

1083 default:

1084 idx = 0;

1085 \_dbus_assert_not_reached ("Unknown hash table type");

1086 break;

1087 }

1088

1089 bucket = &(table-\>buckets\[idx\]);

1090 entry-\>next = \*bucket;

1091 \*bucket = entry;

1092 }

1093 }

1094

1095 /\* Free the old bucket array, if it was dynamically allocated. \*/

1096

1097 if (old_buckets != table-\>static_buckets)

1098 dbus_free (old_buckets);

1099

1100 return TRUE;

1101}

1102

1112void\*

1113\_dbus_hash_table_lookup_string (DBusHashTable \*table,

1114 const char \*key)

1115{

1116 DBusHashEntry \*entry;

1117

1118 \_dbus_assert (table-\>key_type == DBUS_HASH_STRING);

1119

1120 entry = (\* table-\>find_function) (table, (char\*) key, FALSE, NULL, NULL);

1121

1122 if (entry)

1123 return entry-\>value;

1124 else

1125 return NULL;

1126}

1127

1137void\*

1138\_dbus_hash_table_lookup_int (DBusHashTable \*table,

1139 int key)

1140{

1141 DBusHashEntry \*entry;

1142

1143 \_dbus_assert (table-\>key_type == DBUS_HASH_INT);

1144

1145 entry = (\* table-\>find_function) (table, \_DBUS_INT_TO_POINTER (key), FALSE, NULL, NULL);

1146

1147 if (entry)

1148 return entry-\>value;

1149 else

1150 return NULL;

1151}

1152

1162void\*

1163\_dbus_hash_table_lookup_uintptr (DBusHashTable \*table,

1164 uintptr_t key)

1165{

1166 DBusHashEntry \*entry;

1167

1168 \_dbus_assert (table-\>key_type == DBUS_HASH_UINTPTR);

1169

1170 entry = (\* table-\>find_function) (table, (void\*) key, FALSE, NULL, NULL);

1171

1172 if (entry)

1173 return entry-\>value;

1174 else

1175 return NULL;

1176}

1177

1186dbus_bool_t

1187\_dbus_hash_table_remove_string (DBusHashTable \*table,

1188 const char \*key)

1189{

1190 DBusHashEntry \*entry;

1191 DBusHashEntry \*\*bucket;

1192

1193 \_dbus_assert (table-\>key_type == DBUS_HASH_STRING);

1194

1195 entry = (\* table-\>find_function) (table, (char\*) key, FALSE, &bucket, NULL);

1196

1197 if (entry)

1198 {

1199 remove_entry (table, bucket, entry);

1200 return TRUE;

1201 }

1202 else

1203 return FALSE;

1204}

1205

1214dbus_bool_t

1215\_dbus_hash_table_remove_int (DBusHashTable \*table,

1216 int key)

1217{

1218 DBusHashEntry \*entry;

1219 DBusHashEntry \*\*bucket;

1220

1221 \_dbus_assert (table-\>key_type == DBUS_HASH_INT);

1222

1223 entry = (\* table-\>find_function) (table, \_DBUS_INT_TO_POINTER (key), FALSE, &bucket, NULL);

1224

1225 if (entry)

1226 {

1227 remove_entry (table, bucket, entry);

1228 return TRUE;

1229 }

1230 else

1231 return FALSE;

1232}

1233

1242dbus_bool_t

1243\_dbus_hash_table_remove_uintptr (DBusHashTable \*table,

1244 uintptr_t key)

1245{

1246 DBusHashEntry \*entry;

1247 DBusHashEntry \*\*bucket;

1248

1249 \_dbus_assert (table-\>key_type == DBUS_HASH_UINTPTR);

1250

1251 entry = (\* table-\>find_function) (table, (void\*) key, FALSE, &bucket, NULL);

1252

1253 if (entry)

1254 {

1255 remove_entry (table, bucket, entry);

1256 return TRUE;

1257 }

1258 else

1259 return FALSE;

1260}

1261

1277dbus_bool_t

1278\_dbus_hash_table_insert_string (DBusHashTable \*table,

1279 char \*key,

1280 void \*value)

1281{

1282 DBusPreallocatedHash \*preallocated;

1283

1284 \_dbus_assert (table-\>key_type == DBUS_HASH_STRING);

1285

1286 preallocated = \_dbus_hash_table_preallocate_entry (table);

1287 if (preallocated == NULL)

1288 return FALSE;

1289

1290 \_dbus_hash_table_insert_string_preallocated (table, preallocated,

1291 key, value);

1292

1293 return TRUE;

1294}

1295

1311dbus_bool_t

1312\_dbus_hash_table_insert_int (DBusHashTable \*table,

1313 int key,

1314 void \*value)

1315{

1316 DBusHashEntry \*entry;

1317

1318 \_dbus_assert (table-\>key_type == DBUS_HASH_INT);

1319

1320 entry = (\* table-\>find_function) (table, \_DBUS_INT_TO_POINTER (key), TRUE, NULL, NULL);

1321

1322 if (entry == NULL)

1323 return FALSE; /\* no memory \*/

1324

1325 if (table-\>free_key_function && entry-\>key != \_DBUS_INT_TO_POINTER (key))

1326 (\* table-\>free_key_function) (entry-\>key);

1327

1328 if (table-\>free_value_function && entry-\>value != value)

1329 (\* table-\>free_value_function) (entry-\>value);

1330

1331 entry-\>key = \_DBUS_INT_TO_POINTER (key);

1332 entry-\>value = value;

1333

1334 return TRUE;

1335}

1336

1352dbus_bool_t

1353\_dbus_hash_table_insert_uintptr (DBusHashTable \*table,

1354 uintptr_t key,

1355 void \*value)

1356{

1357 DBusHashEntry \*entry;

1358

1359 \_dbus_assert (table-\>key_type == DBUS_HASH_UINTPTR);

1360

1361 entry = (\* table-\>find_function) (table, (void\*) key, TRUE, NULL, NULL);

1362

1363 if (entry == NULL)

1364 return FALSE; /\* no memory \*/

1365

1366 if (table-\>free_key_function && entry-\>key != (void\*) key)

1367 (\* table-\>free_key_function) (entry-\>key);

1368

1369 if (table-\>free_value_function && entry-\>value != value)

1370 (\* table-\>free_value_function) (entry-\>value);

1371

1372 entry-\>key = (void\*) key;

1373 entry-\>value = value;

1374

1375 return TRUE;

1376}

1377

1385DBusPreallocatedHash\*

1386\_dbus_hash_table_preallocate_entry (DBusHashTable \*table)

1387{

1388 DBusHashEntry \*entry;

1389

1390 entry = alloc_entry (table);

1391

1392 return (DBusPreallocatedHash\*) entry;

1393}

1394

1402void

1403\_dbus_hash_table_free_preallocated_entry (DBusHashTable \*table,

1404 DBusPreallocatedHash \*preallocated)

1405{

1406 DBusHashEntry \*entry;

1407

1408 \_dbus_assert (preallocated != NULL);

1409

1410 entry = (DBusHashEntry\*) preallocated;

1411

1412 /\* Don't use free_entry(), since this entry has no key/data \*/

1413 \_dbus_mem_pool_dealloc (table-\>entry_pool, entry);

1414}

1415

1429void

1430\_dbus_hash_table_insert_string_preallocated (DBusHashTable \*table,

1431 DBusPreallocatedHash \*preallocated,

1432 char \*key,

1433 void \*value)

1434{

1435 DBusHashEntry \*entry;

1436

1437 \_dbus_assert (table-\>key_type == DBUS_HASH_STRING);

1438 \_dbus_assert (preallocated != NULL);

1439

1440 entry = (\* table-\>find_function) (table, key, TRUE, NULL, preallocated);

1441

1442 \_dbus_assert (entry != NULL);

1443

1444 if (table-\>free_key_function && entry-\>key != key)

1445 (\* table-\>free_key_function) (entry-\>key);

1446

1447 if (table-\>free_value_function && entry-\>value != value)

1448 (\* table-\>free_value_function) (entry-\>value);

1449

1450 entry-\>key = key;

1451 entry-\>value = value;

1452}

1453

1460int

1461\_dbus_hash_table_get_n_entries (DBusHashTable \*table)

1462{

1463 return table-\>n_entries;

1464}

1465

1478dbus_bool_t

1479\_dbus_hash_table_from_array (DBusHashTable \*table, char \*\*array, char delimiter)

1480{

1481 DBusString key;

1482 DBusString value;

1483 int i;

1484 dbus_bool_t retval = FALSE;

1485

1486 \_dbus_assert (table != NULL);

1487 \_dbus_assert (array != NULL);

1488

1489 if (!\_dbus_string_init (&key))

1490 {

1491 return FALSE;

1492 }

1493

1494 if (!\_dbus_string_init (&value))

1495 {

1496 \_dbus_string_free (&key);

1497 return FALSE;

1498 }

1499

1500 for (i = 0; array\[i\] != NULL; i++)

1501 {

1502 if (!\_dbus_string_append (&key, array\[i\]))

1503 break;

1504

1505 if (\_dbus_string_split_on_byte (&key, delimiter, &value))

1506 {

1507 char \*hash_key, \*hash_value;

1508

1509 if (!\_dbus_string_steal_data (&key, &hash_key))

1510 break;

1511

1512 if (!\_dbus_string_steal_data (&value, &hash_value))

1513 break;

1514

1515 if (!\_dbus_hash_table_insert_string (table,

1516 hash_key, hash_value))

1517 break;

1518 }

1519 \_dbus_string_set_length (&key, 0);

1520 \_dbus_string_set_length (&value, 0);

1521 }

1522

1523 if (array\[i\] != NULL)

1524 goto out;

1525

1526 retval = TRUE;

1527out:

1528

1529 \_dbus_string_free (&key);

1530 \_dbus_string_free (&value);

1531

1532 return retval;

1533}

1534

1543char \*\*

1544\_dbus_hash_table_to_array (DBusHashTable \*table, char delimiter)

1545{

1546 int i, length;

1547 DBusString entry;

1548 DBusHashIter iter;

1549 char \*\*array;

1550

1551 \_dbus_assert (table != NULL);

1552

1553 length = \_dbus_hash_table_get_n_entries (table);

1554

1555 array = dbus_new0 (char \*, length + 1);

1556

1557 if (array == NULL)

1558 return NULL;

1559

1560 i = 0;

1561 \_dbus_hash_iter_init (table, &iter);

1562

1563 if (!\_dbus_string_init (&entry))

1564 {

1565 dbus_free_string_array (array);

1566 return NULL;

1567 }

1568

1569 while (\_dbus_hash_iter_next (&iter))

1570 {

1571 const char \*key, \*value;

1572

1573 key = (const char \*) \_dbus_hash_iter_get_string_key (&iter);

1574 value = (const char \*) \_dbus_hash_iter_get_value (&iter);

1575

1576 if (!\_dbus_string_append_printf (&entry, "%s%c%s", key, delimiter, value))

1577 break;

1578

1579 if (!\_dbus_string_steal_data (&entry, array + i))

1580 break;

1581 i++;

1582 }

1583

1584 \_dbus_string_free (&entry);

1585

1586 if (i != length)

1587 {

1588 dbus_free_string_array (array);

1589 array = NULL;

1590 }

1591

1592 return array;

1593}

1594

DBUS_SMALL_HASH_TABLE

\#define DBUS_SMALL_HASH_TABLE

Initial number of buckets in hash table (hash table statically allocates its buckets for this size an...

**Definition** dbus-hash.c:137

REBUILD_MULTIPLIER

\#define REBUILD_MULTIPLIER

When there are this many entries per bucket, on average, rebuild the hash table to make it larger.

**Definition** dbus-hash.c:111

RANDOM_INDEX

\#define RANDOM_INDEX(table, i)

Takes a preliminary integer hash value and produces an index into a hash tables bucket list.

**Definition** dbus-hash.c:129

DBusFindEntryFunction

DBusHashEntry \*(\* DBusFindEntryFunction)(DBusHashTable \*table, void \*key, dbus_bool_t create_if_not_found, DBusHashEntry \*\*\*bucket, DBusPreallocatedHash \*preallocated)

Function used to find and optionally create a hash entry.

**Definition** dbus-hash.c:163

\_dbus_hash_table_get_n_entries

int \_dbus_hash_table_get_n_entries(DBusHashTable \*table)

Gets the number of hash entries in a hash table.

**Definition** dbus-hash.c:1461

\_dbus_hash_table_ref

DBusHashTable \* \_dbus_hash_table_ref(DBusHashTable \*table)

Increments the reference count for a hash table.

**Definition** dbus-hash.c:354

\_dbus_hash_table_remove_uintptr

dbus_bool_t \_dbus_hash_table_remove_uintptr(DBusHashTable \*table, uintptr_t key)

Removes the hash entry for the given key.

**Definition** dbus-hash.c:1243

\_dbus_hash_iter_get_value

void \* \_dbus_hash_iter_get_value(DBusHashIter \*iter)

Gets the value of the current entry.

**Definition** dbus-hash.c:620

DBusPreallocatedHash

struct DBusPreallocatedHash DBusPreallocatedHash

A preallocated hash entry.

**Definition** dbus-hash.h:150

\_dbus_hash_table_insert_int

dbus_bool_t \_dbus_hash_table_insert_int(DBusHashTable \*table, int key, void \*value)

Creates a hash entry with the given key and value.

**Definition** dbus-hash.c:1312

\_dbus_hash_table_insert_string

dbus_bool_t \_dbus_hash_table_insert_string(DBusHashTable \*table, char \*key, void \*value)

Creates a hash entry with the given key and value.

**Definition** dbus-hash.c:1278

\_dbus_hash_table_from_array

dbus_bool_t \_dbus_hash_table_from_array(DBusHashTable \*table, char \*\*array, char delimiter)

Imports a string array into a hash table The hash table needs to be initialized with string keys,...

**Definition** dbus-hash.c:1479

\_dbus_hash_iter_get_uintptr_key

uintptr_t \_dbus_hash_iter_get_uintptr_key(DBusHashIter \*iter)

Gets the key for the current entry.

**Definition** dbus-hash.c:685

\_dbus_hash_table_lookup_uintptr

void \* \_dbus_hash_table_lookup_uintptr(DBusHashTable \*table, uintptr_t key)

Looks up the value for a given integer in a hash table of type DBUS_HASH_UINTPTR.

**Definition** dbus-hash.c:1163

\_dbus_hash_table_unref

void \_dbus_hash_table_unref(DBusHashTable \*table)

Decrements the reference count for a hash table, freeing the hash table if the count reaches zero.

**Definition** dbus-hash.c:368

KeyCompareFunc

int(\* KeyCompareFunc)(const void \*key_a, const void \*key_b)

Key comparison function.

**Definition** dbus-hash.c:895

\_dbus_hash_iter_next

dbus_bool_t \_dbus_hash_iter_next(DBusHashIter \*iter)

Move the hash iterator forward one step, to the next hash entry.

**Definition** dbus-hash.c:550

\_dbus_hash_iter_get_int_key

int \_dbus_hash_iter_get_int_key(DBusHashIter \*iter)

Gets the key for the current entry.

**Definition** dbus-hash.c:666

\_dbus_hash_iter_init

void \_dbus_hash_iter_init(DBusHashTable \*table, DBusHashIter \*iter)

Initializes a hash table iterator.

**Definition** dbus-hash.c:524

\_dbus_hash_table_free_preallocated_entry

void \_dbus_hash_table_free_preallocated_entry(DBusHashTable \*table, DBusPreallocatedHash \*preallocated)

Frees an opaque DBusPreallocatedHash that was not used in order to insert into the hash table.

**Definition** dbus-hash.c:1403

\_dbus_hash_table_new

DBusHashTable \* \_dbus_hash_table_new(DBusHashType type, DBusFreeFunction key_free_function, DBusFreeFunction value_free_function)

Constructs a new hash table.

**Definition** dbus-hash.c:292

\_dbus_hash_table_remove_int

dbus_bool_t \_dbus_hash_table_remove_int(DBusHashTable \*table, int key)

Removes the hash entry for the given key.

**Definition** dbus-hash.c:1215

\_dbus_hash_table_preallocate_entry

DBusPreallocatedHash \* \_dbus_hash_table_preallocate_entry(DBusHashTable \*table)

Preallocate an opaque data blob that allows us to insert into the hash table at a later time without ...

**Definition** dbus-hash.c:1386

\_dbus_hash_table_remove_string

dbus_bool_t \_dbus_hash_table_remove_string(DBusHashTable \*table, const char \*key)

Removes the hash entry for the given key.

**Definition** dbus-hash.c:1187

\_dbus_hash_table_to_array

char \*\* \_dbus_hash_table_to_array(DBusHashTable \*table, char delimiter)

Creates a string array from a hash table.

**Definition** dbus-hash.c:1544

\_dbus_hash_iter_set_value

void \_dbus_hash_iter_set_value(DBusHashIter \*iter, void \*value)

Sets the value of the current entry.

**Definition** dbus-hash.c:643

DBusHashType

DBusHashType

Indicates the type of a key in the hash table.

**Definition** dbus-hash.h:68

\_dbus_hash_table_lookup_string

void \* \_dbus_hash_table_lookup_string(DBusHashTable \*table, const char \*key)

Looks up the value for a given string in a hash table of type DBUS_HASH_STRING.

**Definition** dbus-hash.c:1113

\_dbus_hash_iter_lookup

dbus_bool_t \_dbus_hash_iter_lookup(DBusHashTable \*table, void \*key, dbus_bool_t create_if_not_found, DBusHashIter \*iter)

A low-level but efficient interface for manipulating the hash table.

**Definition** dbus-hash.c:748

\_dbus_hash_table_remove_all

void \_dbus_hash_table_remove_all(DBusHashTable \*table)

Removed all entries from a hash table.

**Definition** dbus-hash.c:425

\_dbus_hash_iter_get_string_key

const char \* \_dbus_hash_iter_get_string_key(DBusHashIter \*iter)

Gets the key for the current entry.

**Definition** dbus-hash.c:703

\_dbus_hash_table_insert_uintptr

dbus_bool_t \_dbus_hash_table_insert_uintptr(DBusHashTable \*table, uintptr_t key, void \*value)

Creates a hash entry with the given key and value.

**Definition** dbus-hash.c:1353

\_dbus_hash_iter_remove_entry

void \_dbus_hash_iter_remove_entry(DBusHashIter \*iter)

Removes the current entry from the hash table.

**Definition** dbus-hash.c:599

\_dbus_hash_table_insert_string_preallocated

void \_dbus_hash_table_insert_string_preallocated(DBusHashTable \*table, DBusPreallocatedHash \*preallocated, char \*key, void \*value)

Inserts a string-keyed entry into the hash table, using a preallocated data block from \_dbus_hash_tab...

**Definition** dbus-hash.c:1430

\_dbus_hash_table_lookup_int

void \* \_dbus_hash_table_lookup_int(DBusHashTable \*table, int key)

Looks up the value for a given integer in a hash table of type DBUS_HASH_INT.

**Definition** dbus-hash.c:1138

DBUS_HASH_INT

@ DBUS_HASH_INT

Hash keys are integers.

**Definition** dbus-hash.h:70

DBUS_HASH_UINTPTR

@ DBUS_HASH_UINTPTR

Hash keys are integer capable to hold a pointer.

**Definition** dbus-hash.h:71

DBUS_HASH_STRING

@ DBUS_HASH_STRING

Hash keys are strings.

**Definition** dbus-hash.h:69

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

\_DBUS_INT_MAX

\#define \_DBUS_INT_MAX

Maximum value of type "int".

**Definition** dbus-internals.h:327

\_DBUS_POINTER_TO_INT

\#define \_DBUS_POINTER_TO_INT(pointer)

Safely casts a void\* to an integer; should only be used on void\* that actually contain integers,...

**Definition** dbus-internals.h:191

\_DBUS_N_ELEMENTS

\#define \_DBUS_N_ELEMENTS(array)

Computes the number of elements in a fixed-size array using sizeof().

**Definition** dbus-internals.h:189

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

dbus_free

void dbus_free(void \*memory)

Frees a block of memory previously allocated by dbus_malloc() or dbus_malloc0().

**Definition** dbus-memory.c:710

dbus_new0

\#define dbus_new0(type, count)

Safe macro for using dbus_malloc0().

**Definition** dbus-memory.h:60

dbus_free_string_array

void dbus_free_string_array(char \*\*str_array)

Frees a NULL-terminated array of strings.

**Definition** dbus-memory.c:758

\_dbus_string_set_length

dbus_bool_t \_dbus_string_set_length(DBusString \*str, int length)

Sets the length of a string.

**Definition** dbus-string.c:847

\_dbus_string_append

dbus_bool_t \_dbus_string_append(DBusString \*str, const char \*buffer)

Appends a nul-terminated C-style string to a DBusString.

**Definition** dbus-string.c:980

\_dbus_string_init

dbus_bool_t \_dbus_string_init(DBusString \*str)

Initializes a string.

**Definition** dbus-string.c:182

\_dbus_string_steal_data

dbus_bool_t \_dbus_string_steal_data(DBusString \*str, char \*\*data_return)

Like \_dbus_string_get_data(), but removes the gotten data from the original string.

**Definition** dbus-string.c:686

\_dbus_string_split_on_byte

dbus_bool_t \_dbus_string_split_on_byte(DBusString \*source, unsigned char byte, DBusString \*tail)

Looks for the first occurance of a byte, deletes that byte, and moves everything after the byte to th...

**Definition** dbus-string.c:1529

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_string_append_printf

dbus_bool_t \_dbus_string_append_printf(DBusString \*str, const char \*format,...)

Appends a printf-style formatted string to the DBusString.

**Definition** dbus-string.c:1147

DBusHashEntry

Internal representation of a hash entry.

**Definition** dbus-hash.c:151

DBusHashEntry::value

void \* value

Hash value.

**Definition** dbus-hash.c:157

DBusHashEntry::next

DBusHashEntry \* next

Pointer to next entry in this hash bucket, or NULL for end of chain.

**Definition** dbus-hash.c:152

DBusHashEntry::key

void \* key

Hash key.

**Definition** dbus-hash.c:156

DBusHashIter

Hash iterator object.

**Definition** dbus-hash.h:50

DBusHashTable

Internals of DBusHashTable.

**Definition** dbus-hash.c:175

DBusHashTable::buckets

DBusHashEntry \*\* buckets

Pointer to bucket array.

**Definition** dbus-hash.c:178

DBusHashTable::key_type

DBusHashType key_type

Type of keys used in this table.

**Definition** dbus-hash.c:205

DBusHashTable::hi_rebuild_size

int hi_rebuild_size

Enlarge table when n_entries gets to be this large.

**Definition** dbus-hash.c:192

DBusHashTable::n_buckets

int n_buckets

Total number of buckets allocated at \*\*buckets.

**Definition** dbus-hash.c:186

DBusHashTable::down_shift

int down_shift

Shift count used in hashing function.

**Definition** dbus-hash.c:198

DBusHashTable::free_key_function

DBusFreeFunction free_key_function

Function to free keys.

**Definition** dbus-hash.c:210

DBusHashTable::lo_rebuild_size

int lo_rebuild_size

Shrink table when n_entries gets below this.

**Definition** dbus-hash.c:195

DBusHashTable::find_function

DBusFindEntryFunction find_function

Function for finding entries.

**Definition** dbus-hash.c:208

DBusHashTable::refcount

int refcount

Reference count.

**Definition** dbus-hash.c:176

DBusHashTable::entry_pool

DBusMemPool \* entry_pool

Memory pool for hash entries.

**Definition** dbus-hash.c:213

DBusHashTable::mask

int mask

Mask value used in hashing function.

**Definition** dbus-hash.c:202

DBusHashTable::static_buckets

DBusHashEntry \* static_buckets\[DBUS_SMALL_HASH_TABLE\]

Bucket array used for small tables (to avoid mallocs and frees).

**Definition** dbus-hash.c:182

DBusHashTable::free_value_function

DBusFreeFunction free_value_function

Function to free values.

**Definition** dbus-hash.c:211

DBusHashTable::n_entries

int n_entries

Total number of entries present in table.

**Definition** dbus-hash.c:189

DBusMemPool

Internals fields of DBusMemPool.

**Definition** dbus-mempool.c:109

DBusRealHashIter

Internals of DBusHashIter.

**Definition** dbus-hash.c:220

DBusRealHashIter::table

DBusHashTable \* table

Pointer to table containing entry.

**Definition** dbus-hash.c:221

DBusRealHashIter::next_entry

DBusHashEntry \* next_entry

Next entry to be iterated onto in current bucket.

**Definition** dbus-hash.c:227

DBusRealHashIter::entry

DBusHashEntry \* entry

Current hash entry.

**Definition** dbus-hash.c:226

DBusRealHashIter::n_entries_on_init

int n_entries_on_init

used to detect table resize since initialization

**Definition** dbus-hash.c:229

DBusRealHashIter::bucket

DBusHashEntry \*\* bucket

Pointer to bucket that points to first entry in this entry's chain: used for deleting the entry.

**Definition** dbus-hash.c:222

DBusRealHashIter::next_bucket

int next_bucket

index of next bucket

**Definition** dbus-hash.c:228

DBusString

**Definition** dbus-string.h:47
