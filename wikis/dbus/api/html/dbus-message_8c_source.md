dbus-message.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-message.c DBusMessage object

3 \*

4 \* Copyright (C) 2002, 2003, 2004, 2005 Red Hat Inc.

5 \* Copyright (C) 2002, 2003 CodeFactory AB

6 \*

7 \* SPDX-License-Identifier: AFL-2.1 OR GPL-2.0-or-later

8 \*

9 \* Licensed under the Academic Free License version 2.1

10 \*

11 \* This program is free software; you can redistribute it and/or modify

12 \* it under the terms of the GNU General Public License as published by

13 \* the Free Software Foundation; either version 2 of the License, or

14 \* (at your option) any later version.

15 \*

16 \* This program is distributed in the hope that it will be useful,

17 \* but WITHOUT ANY WARRANTY; without even the implied warranty of

18 \* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the

19 \* GNU General Public License for more details.

20 \*

21 \* You should have received a copy of the GNU General Public License

22 \* along with this program; if not, write to the Free Software

23 \* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

24 \*

25 \*/

26

27\#include \<config.h\>

28\#include "dbus-internals.h"

29\#include "dbus-marshal-recursive.h"

30\#include "dbus-marshal-validate.h"

31\#include "dbus-marshal-byteswap.h"

32\#include "dbus-marshal-header.h"

33\#include "dbus-signature.h"

34\#include "dbus-message-private.h"

35\#include "dbus-object-tree.h"

36\#include "dbus-memory.h"

37\#include "dbus-list.h"

38\#include "dbus-threads-internal.h"

39\#ifdef HAVE_UNIX_FD_PASSING

40\#include "dbus-sysdeps.h"

41\#include "dbus-sysdeps-unix.h"

42\#endif

43

44\#include \<string.h\>

45

46\#define \_DBUS_TYPE_IS_STRINGLIKE(type) \\

47 (type == DBUS_TYPE_STRING \|\| type == DBUS_TYPE_SIGNATURE \|\| \\

48 type == DBUS_TYPE_OBJECT_PATH)

49

50static void dbus_message_finalize (DBusMessage \*message);

51

62\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

63static dbus_bool_t

64\_dbus_enable_message_cache (void)

65{

66 static int enabled = -1;

67

68 if (enabled \< 0)

69 {

70 const char \*s = \_dbus_getenv ("DBUS_MESSAGE_CACHE");

71

72 enabled = TRUE;

73

74 if (s && \*s)

75 {

76 if (\*s == '0')

77 enabled = FALSE;

78 else if (\*s == '1')

79 enabled = TRUE;

80 else

81 \_dbus_warn ("DBUS_MESSAGE_CACHE should be 0 or 1 if set, not '%s'",

82 s);

83 }

84 }

85

86 return enabled;

87}

88\#else

89 /\* constant expression, should be optimized away \*/

90\# define \_dbus_enable_message_cache() (TRUE)

91\#endif

92

93\#ifndef \_dbus_message_trace_ref

94void

95\_dbus_message_trace_ref (DBusMessage \*message,

96 int old_refcount,

97 int new_refcount,

98 const char \*why)

99{

100 static int enabled = -1;

101

102 \_dbus_trace_ref ("DBusMessage", message, old_refcount, new_refcount, why,

103 "DBUS_MESSAGE_TRACE", &enabled);

104}

105\#endif

106

107/\* Not thread locked, but strictly const/read-only so should be OK

108 \*/

110\_DBUS_STRING_DEFINE_STATIC(\_dbus_empty_signature_str, "");

111

112/\* these have wacky values to help trap uninitialized iterators;

113 \* but has to fit in 3 bits

114 \*/

115enum {

116 DBUS_MESSAGE_ITER_TYPE_READER = 3,

117 DBUS_MESSAGE_ITER_TYPE_WRITER = 7

118};

119

121typedef struct DBusMessageRealIter DBusMessageRealIter;

122

128struct DBusMessageRealIter

129{

130 DBusMessage \*message;

131 dbus_uint32_t changed_stamp : CHANGED_STAMP_BITS;

132 dbus_uint32_t iter_type : 3;

133 dbus_uint32_t sig_refcount : 8;

134 union

135 {

136 DBusTypeWriter writer;

137 DBusTypeReader reader;

138 } u;

139};

140

141\#if DBUS_SIZEOF_VOID_P \> 8

142/\*

143 \* Architectures with 128-bit pointers were not supported in DBus 1.10, so we

144 \* do no check for DBus 1.10 structure layout compatibility for such

145 \* architectures (e.g. Arm Morello).

146 \*/

147\#define CHECK_DBUS_1_10_BINARY_COMPATIBILITY 0

148\#else

149\#define CHECK_DBUS_1_10_BINARY_COMPATIBILITY 1

155typedef struct

156{

157 void \*dummy1;

158 void \*dummy2;

159 dbus_uint32_t dummy3;

160 int dummy4;

161 int dummy5;

162 int dummy6;

163 int dummy7;

164 int dummy8;

165 int dummy9;

166 int dummy10;

167 int dummy11;

168 int pad1;

169 int pad2;

170 void \*pad3;

171} DBusMessageIter_1_10_0;

172\#endif

173

174static void

175get_const_signature (DBusHeader \*header,

176 const DBusString \*\*type_str_p,

177 int \*type_pos_p)

178{

179 if (\_dbus_header_get_field_raw (header,

180 DBUS_HEADER_FIELD_SIGNATURE,

181 type_str_p,

182 type_pos_p))

183 {

184 \*type_pos_p += 1; /\* skip the signature length which is 1 byte \*/

185 }

186 else

187 {

188 \*type_str_p = &\_dbus_empty_signature_str;

189 \*type_pos_p = 0;

190 }

191}

192

198static void

199\_dbus_message_byteswap (DBusMessage \*message)

200{

201 const DBusString \*type_str;

202 int type_pos;

203 char byte_order;

204

205 byte_order = \_dbus_header_get_byte_order (&message-\>header);

206

207 if (byte_order == DBUS_COMPILER_BYTE_ORDER)

208 return;

209

210 \_dbus_verbose ("Swapping message into compiler byte order\n");

211

212 get_const_signature (&message-\>header, &type_str, &type_pos);

213

214 \_dbus_marshal_byteswap (type_str, type_pos,

215 byte_order,

216 DBUS_COMPILER_BYTE_ORDER,

217 &message-\>body, 0);

218

219 \_dbus_header_byteswap (&message-\>header, DBUS_COMPILER_BYTE_ORDER);

220 \_dbus_assert (\_dbus_header_get_byte_order (&message-\>header) ==

221 DBUS_COMPILER_BYTE_ORDER);

222}

223

230\#define ensure_byte_order(message) \_dbus_message_byteswap (message)

231

242void

243\_dbus_message_get_network_data (DBusMessage \*message,

244 const DBusString \*\*header,

245 const DBusString \*\*body)

246{

247 \_dbus_assert (message-\>locked);

248

249 \*header = &message-\>header.data;

250 \*body = &message-\>body;

251}

252

262void \_dbus_message_get_unix_fds(DBusMessage \*message,

263 const int \*\*fds,

264 unsigned \*n_fds)

265{

266 \_dbus_assert (message-\>locked);

267

268\#ifdef HAVE_UNIX_FD_PASSING

269 \*fds = message-\>unix_fds;

270 \*n_fds = message-\>n_unix_fds;

271\#else

272 \*fds = NULL;

273 \*n_fds = 0;

274\#endif

275}

276

283dbus_bool_t

284\_dbus_message_remove_unknown_fields (DBusMessage \*message)

285{

286 return \_dbus_header_remove_unknown_fields (&message-\>header);

287}

288

300void

301dbus_message_set_serial (DBusMessage \*message,

302 dbus_uint32_t serial)

303{

304 \_dbus_return_if_fail (message != NULL);

305 \_dbus_return_if_fail (!message-\>locked);

306

307 \_dbus_header_set_serial (&message-\>header, serial);

308}

309

326void

327\_dbus_message_add_counter_link (DBusMessage \*message,

328 DBusList \*link)

329{

330 /\* right now we don't recompute the delta when message

331 \* size changes, and that's OK for current purposes

332 \* I think, but could be important to change later.

333 \* Do recompute it whenever there are no outstanding counters,

334 \* since it's basically free.

335 \*/

336 if (message-\>counters == NULL)

337 {

338 message-\>size_counter_delta =

339 \_dbus_string_get_length (&message-\>header.data) +

340 \_dbus_string_get_length (&message-\>body);

341

342\#ifdef HAVE_UNIX_FD_PASSING

343 message-\>unix_fd_counter_delta = message-\>n_unix_fds;

344\#endif

345

346\#if 0

347 \_dbus_verbose ("message has size %ld\n",

348 message-\>size_counter_delta);

349\#endif

350 }

351

352 \_dbus_list_append_link (&message-\>counters, link);

353

354 \_dbus_counter_adjust_size (link-\>data, message-\>size_counter_delta);

355

356\#ifdef HAVE_UNIX_FD_PASSING

357 \_dbus_counter_adjust_unix_fd (link-\>data, message-\>unix_fd_counter_delta);

358\#endif

359}

360

375dbus_bool_t

376\_dbus_message_add_counter (DBusMessage \*message,

377 DBusCounter \*counter)

378{

379 DBusList \*link;

380

381 link = \_dbus_list_alloc_link (counter);

382 if (link == NULL)

383 return FALSE;

384

385 \_dbus_counter_ref (counter);

386 \_dbus_message_add_counter_link (message, link);

387

388 return TRUE;

389}

390

398void

399\_dbus_message_remove_counter (DBusMessage \*message,

400 DBusCounter \*counter)

401{

402 DBusList \*link;

403

404 link = \_dbus_list_find_last (&message-\>counters,

405 counter);

406 \_dbus_assert (link != NULL);

407

408 \_dbus_list_remove_link (&message-\>counters, link);

409

410 \_dbus_counter_adjust_size (counter, - message-\>size_counter_delta);

411

412\#ifdef HAVE_UNIX_FD_PASSING

413 \_dbus_counter_adjust_unix_fd (counter, - message-\>unix_fd_counter_delta);

414\#endif

415

416 \_dbus_counter_notify (counter);

417 \_dbus_counter_unref (counter);

418}

419

430void

431dbus_message_lock (DBusMessage \*message)

432{

433 if (!message-\>locked)

434 {

435 \_dbus_header_update_lengths (&message-\>header,

436 \_dbus_string_get_length (&message-\>body));

437

438 /\* must have a signature if you have a body \*/

439 \_dbus_assert (\_dbus_string_get_length (&message-\>body) == 0 \|\|

440 dbus_message_get_signature (message) != NULL);

441

442 message-\>locked = TRUE;

443 }

444}

445

446static dbus_bool_t

447set_or_delete_string_field (DBusMessage \*message,

448 int field,

449 int typecode,

450 const char \*value)

451{

452 if (value == NULL)

453 return \_dbus_header_delete_field (&message-\>header, field);

454 else

455 return \_dbus_header_set_field_basic (&message-\>header,

456 field,

457 typecode,

458 &value);

459}

460

461/\* Message Cache

462 \*

463 \* We cache some DBusMessage to reduce the overhead of allocating

464 \* them. In my profiling this consistently made about an 8%

465 \* difference. It avoids the malloc for the message, the malloc for

466 \* the slot list, the malloc for the header string and body string,

467 \* and the associated free() calls. It does introduce another global

468 \* lock which could be a performance issue in certain cases.

469 \*

470 \* For the echo client/server the round trip time goes from around

471 \* .000077 to .000069 with the message cache on my laptop. The sysprof

472 \* change is as follows (numbers are cumulative percentage):

473 \*

474 \* with message cache implemented as array as it is now (0.000069 per):

475 \* new_empty_header 1.46

476 \* mutex_lock 0.56 \# i.e. \_DBUS_LOCK(message_cache)

477 \* mutex_unlock 0.25

478 \* self 0.41

479 \* unref 2.24

480 \* self 0.68

481 \* list_clear 0.43

482 \* mutex_lock 0.33 \# i.e. \_DBUS_LOCK(message_cache)

483 \* mutex_unlock 0.25

484 \*

485 \* with message cache implemented as list (0.000070 per roundtrip):

486 \* new_empty_header 2.72

487 \* list_pop_first 1.88

488 \* unref 3.3

489 \* list_prepend 1.63

490 \*

491 \* without cache (0.000077 per roundtrip):

492 \* new_empty_header 6.7

493 \* string_init_preallocated 3.43

494 \* dbus_malloc 2.43

495 \* dbus_malloc0 2.59

496 \*

497 \* unref 4.02

498 \* string_free 1.82

499 \* dbus_free 1.63

500 \* dbus_free 0.71

501 \*

502 \* If you implement the message_cache with a list, the primary reason

503 \* it's slower is that you add another thread lock (on the DBusList

504 \* mempool).

505 \*/

506

508\#define MAX_MESSAGE_SIZE_TO_CACHE 10 \* \_DBUS_ONE_KILOBYTE

509

511\#define MAX_MESSAGE_CACHE_SIZE 5

512

513/\* Protected by \_DBUS_LOCK (message_cache) \*/

514static DBusMessage \*message_cache\[MAX_MESSAGE_CACHE_SIZE\];

515static int message_cache_count = 0;

516static dbus_bool_t message_cache_shutdown_registered = FALSE;

517

518static void

519dbus_message_cache_shutdown (void \*data)

520{

521 int i;

522

523 if (!\_DBUS_LOCK (message_cache))

524 \_dbus_assert_not_reached ("we would have initialized global locks "

525 "before registering a shutdown function");

526

527 i = 0;

528 while (i \< MAX_MESSAGE_CACHE_SIZE)

529 {

530 if (message_cache\[i\])

531 dbus_message_finalize (message_cache\[i\]);

532

533 ++i;

534 }

535

536 message_cache_count = 0;

537 message_cache_shutdown_registered = FALSE;

538

539 \_DBUS_UNLOCK (message_cache);

540}

541

549static DBusMessage\*

550dbus_message_get_cached (void)

551{

552 DBusMessage \*message;

553 int i;

554

555 message = NULL;

556

557 if (!\_DBUS_LOCK (message_cache))

558 {

559 /\* we'd have initialized global locks before caching anything,

560 \* so there can't be anything in the cache \*/

561 return NULL;

562 }

563

564 \_dbus_assert (message_cache_count \>= 0);

565

566 if (message_cache_count == 0)

567 {

568 \_DBUS_UNLOCK (message_cache);

569 return NULL;

570 }

571

572 /\* This is not necessarily true unless count \> 0, and

573 \* message_cache is uninitialized until the shutdown is

574 \* registered

575 \*/

576 \_dbus_assert (message_cache_shutdown_registered);

577

578 i = 0;

579 while (i \< MAX_MESSAGE_CACHE_SIZE)

580 {

581 if (message_cache\[i\])

582 {

583 message = message_cache\[i\];

584 message_cache\[i\] = NULL;

585 message_cache_count -= 1;

586 break;

587 }

588 ++i;

589 }

590 \_dbus_assert (message_cache_count \>= 0);

591 \_dbus_assert (i \< MAX_MESSAGE_CACHE_SIZE);

592 \_dbus_assert (message != NULL);

593

594 \_dbus_assert (\_dbus_atomic_get (&message-\>refcount) == 0);

595

596 \_dbus_assert (message-\>counters == NULL);

597

598 \_DBUS_UNLOCK (message_cache);

599

600 return message;

601}

602

603\#ifdef HAVE_UNIX_FD_PASSING

604static void

605close_unix_fds(int \*fds, unsigned \*n_fds)

606{

607 DBusError e;

608 unsigned int i;

609

610 if (\*n_fds \<= 0)

611 return;

612

613 dbus_error_init(&e);

614

615 for (i = 0; i \< \*n_fds; i++)

616 {

617 if (!\_dbus_close(fds\[i\], &e))

618 {

619 \_dbus_warn("Failed to close file descriptor: %s", e.message);

620 dbus_error_free(&e);

621 }

622 }

623

624 \*n_fds = 0;

625

626 /\* We don't free the array here, in case we can recycle it later \*/

627}

628\#endif

629

630static void

631free_counter (void \*element,

632 void \*data)

633{

634 DBusCounter \*counter = element;

635 DBusMessage \*message = data;

636

637 \_dbus_counter_adjust_size (counter, - message-\>size_counter_delta);

638\#ifdef HAVE_UNIX_FD_PASSING

639 \_dbus_counter_adjust_unix_fd (counter, - message-\>unix_fd_counter_delta);

640\#endif

641

642 \_dbus_counter_notify (counter);

643 \_dbus_counter_unref (counter);

644}

645

651static void

652dbus_message_cache_or_finalize (DBusMessage \*message)

653{

654 dbus_bool_t was_cached;

655 int i;

656

657 \_dbus_assert (\_dbus_atomic_get (&message-\>refcount) == 0);

658

659 /\* This calls application code and has to be done first thing

660 \* without holding the lock

661 \*/

662 \_dbus_data_slot_list_clear (&message-\>slot_list);

663

664 \_dbus_list_foreach (&message-\>counters,

665 free_counter, message);

666 \_dbus_list_clear (&message-\>counters);

667

668\#ifdef HAVE_UNIX_FD_PASSING

669 close_unix_fds(message-\>unix_fds, &message-\>n_unix_fds);

670\#endif

671

672 was_cached = FALSE;

673

674 if (!\_DBUS_LOCK (message_cache))

675 {

676 /\* The only way to get a non-null message goes through

677 \* dbus_message_get_cached() which takes the lock. \*/

678 \_dbus_assert_not_reached ("we would have initialized global locks "

679 "the first time we constructed a message");

680 }

681

682 if (!message_cache_shutdown_registered)

683 {

684 \_dbus_assert (message_cache_count == 0);

685

686 if (!\_dbus_register_shutdown_func (dbus_message_cache_shutdown, NULL))

687 goto out;

688

689 i = 0;

690 while (i \< MAX_MESSAGE_CACHE_SIZE)

691 {

692 message_cache\[i\] = NULL;

693 ++i;

694 }

695

696 message_cache_shutdown_registered = TRUE;

697 }

698

699 \_dbus_assert (message_cache_count \>= 0);

700

701 if (!\_dbus_enable_message_cache ())

702 goto out;

703

704 if ((\_dbus_string_get_length (&message-\>header.data) +

705 \_dbus_string_get_length (&message-\>body)) \>

706 MAX_MESSAGE_SIZE_TO_CACHE)

707 goto out;

708

709 if (message_cache_count \>= MAX_MESSAGE_CACHE_SIZE)

710 goto out;

711

712 /\* Find empty slot \*/

713 i = 0;

714 while (message_cache\[i\] != NULL)

715 ++i;

716

717 \_dbus_assert (i \< MAX_MESSAGE_CACHE_SIZE);

718

719 \_dbus_assert (message_cache\[i\] == NULL);

720 message_cache\[i\] = message;

721 message_cache_count += 1;

722 was_cached = TRUE;

723\#ifndef DBUS_DISABLE_CHECKS

724 message-\>in_cache = TRUE;

725\#endif

726

727 out:

728 \_dbus_assert (\_dbus_atomic_get (&message-\>refcount) == 0);

729

730 \_DBUS_UNLOCK (message_cache);

731

732 if (!was_cached)

733 dbus_message_finalize (message);

734}

735

736/\*

737 \* Arrange for iter to be something that \_dbus_message_iter_check() would

738 \* reject as not a valid iterator.

739 \*/

740static void

741\_dbus_message_real_iter_zero (DBusMessageRealIter \*iter)

742{

743 \_dbus_assert (iter != NULL);

744 \_DBUS_ZERO (\*iter);

745 /\* NULL is not, strictly speaking, guaranteed to be all-bits-zero \*/

746 iter-\>message = NULL;

747}

748

754void

755dbus_message_iter_init_closed (DBusMessageIter \*iter)

756{

757 \_dbus_return_if_fail (iter != NULL);

758 \_dbus_message_real_iter_zero ((DBusMessageRealIter \*) iter);

759}

760

761static dbus_bool_t

762\_dbus_message_real_iter_is_zeroed (DBusMessageRealIter \*iter)

763{

764 return (iter != NULL && iter-\>message == NULL && iter-\>changed_stamp == 0 &&

765 iter-\>iter_type == 0 && iter-\>sig_refcount == 0);

766}

767

768\#if defined(DBUS_ENABLE_CHECKS) \|\| defined(DBUS_ENABLE_ASSERT)

769static dbus_bool_t

770\_dbus_message_iter_check (DBusMessageRealIter \*iter)

771{

772 char byte_order;

773

774 if (iter == NULL)

775 {

776 \_dbus_warn_check_failed ("dbus message iterator is NULL");

777 return FALSE;

778 }

779

780 if (iter-\>message == NULL \|\| iter-\>iter_type == 0)

781 {

782 \_dbus_warn_check_failed ("dbus message iterator has already been "

783 "closed, or is uninitialized or corrupt");

784 return FALSE;

785 }

786

787 byte_order = \_dbus_header_get_byte_order (&iter-\>message-\>header);

788

789 if (iter-\>iter_type == DBUS_MESSAGE_ITER_TYPE_READER)

790 {

791 if (iter-\>u.reader.byte_order != byte_order)

792 {

793 \_dbus_warn_check_failed ("dbus message changed byte order since iterator was created");

794 return FALSE;

795 }

796 /\* because we swap the message into compiler order when you init an iter \*/

797 \_dbus_assert (iter-\>u.reader.byte_order == DBUS_COMPILER_BYTE_ORDER);

798 }

799 else if (iter-\>iter_type == DBUS_MESSAGE_ITER_TYPE_WRITER)

800 {

801 if (iter-\>u.writer.byte_order != byte_order)

802 {

803 \_dbus_warn_check_failed ("dbus message changed byte order since append iterator was created");

804 return FALSE;

805 }

806 /\* because we swap the message into compiler order when you init an iter \*/

807 \_dbus_assert (iter-\>u.writer.byte_order == DBUS_COMPILER_BYTE_ORDER);

808 }

809 else

810 {

811 \_dbus_warn_check_failed ("dbus message iterator looks uninitialized or corrupted");

812 return FALSE;

813 }

814

815 if (iter-\>changed_stamp != iter-\>message-\>changed_stamp)

816 {

817 \_dbus_warn_check_failed ("dbus message iterator invalid because the message has been modified (or perhaps the iterator is just uninitialized)");

818 return FALSE;

819 }

820

821 return TRUE;

822}

823\#endif /\* DBUS_ENABLE_CHECKS \|\| DBUS_ENABLE_ASSERT \*/

824

837dbus_bool_t

838\_dbus_message_iter_get_args_valist (DBusMessageIter \*iter,

839 DBusError \*error,

840 int first_arg_type,

841 va_list var_args)

842{

843 DBusMessageRealIter \*real = (DBusMessageRealIter \*)iter;

844 int spec_type, msg_type, i, j;

845 dbus_bool_t retval;

846 va_list copy_args;

847

848 \_dbus_assert (\_dbus_message_iter_check (real));

849

850 retval = FALSE;

851

852 spec_type = first_arg_type;

853 i = 0;

854

855 /\* copy var_args first, then we can do another iteration over it to

856 \* free memory and close unix fds if parse failed at some point.

857 \*/

858 va_copy (copy_args, var_args);

859

860 while (spec_type != DBUS_TYPE_INVALID)

861 {

862 msg_type = dbus_message_iter_get_arg_type (iter);

863

864 if (msg_type != spec_type)

865 {

866 dbus_set_error (error, DBUS_ERROR_INVALID_ARGS,

867 "Argument %d is specified to be of type \\%s\\, but "

868 "is actually of type \\%s\\\n", i,

869 \_dbus_type_to_string (spec_type),

870 \_dbus_type_to_string (msg_type));

871

872 goto out;

873 }

874

875 if (spec_type == DBUS_TYPE_UNIX_FD)

876 {

877\#ifdef HAVE_UNIX_FD_PASSING

878 DBusBasicValue idx;

879 int \*pfd, nfd;

880

881 pfd = va_arg (var_args, int\*);

882 \_dbus_assert(pfd);

883

884 \_dbus_type_reader_read_basic(&real-\>u.reader, &idx);

885

886 if (idx.u32 \>= real-\>message-\>n_unix_fds)

887 {

888 dbus_set_error (error, DBUS_ERROR_INCONSISTENT_MESSAGE,

889 "Message refers to file descriptor at index %i,"

890 "but has only %i descriptors attached.\n",

891 idx.u32,

892 real-\>message-\>n_unix_fds);

893 goto out;

894 }

895

896 if ((nfd = \_dbus_dup(real-\>message-\>unix_fds\[idx.u32\], error)) \< 0)

897 goto out;

898

899 \*pfd = nfd;

900\#else

901 dbus_set_error (error, DBUS_ERROR_NOT_SUPPORTED,

902 "Platform does not support file desciptor passing.\n");

903 goto out;

904\#endif

905 }

906 else if (dbus_type_is_basic (spec_type))

907 {

908 void \*ptr;

909

910 ptr = va_arg (var_args, void \*);

911

912 \_dbus_assert (ptr != NULL);

913

914 \_dbus_type_reader_read_basic (&real-\>u.reader,

915 ptr);

916 }

917 else if (spec_type == DBUS_TYPE_ARRAY)

918 {

919 int element_type;

920 int spec_element_type;

921 const void \*\*ptr;

922 int \*n_elements_p;

923 DBusTypeReader array;

924

925 spec_element_type = va_arg (var_args, int);

926 element_type = \_dbus_type_reader_get_element_type (&real-\>u.reader);

927

928 if (spec_element_type != element_type)

929 {

930 dbus_set_error (error, DBUS_ERROR_INVALID_ARGS,

931 "Argument %d is specified to be an array of \\%s\\, but "

932 "is actually an array of \\%s\\\n",

933 i,

934 \_dbus_type_to_string (spec_element_type),

935 \_dbus_type_to_string (element_type));

936

937 goto out;

938 }

939

940 if (dbus_type_is_fixed (spec_element_type) &&

941 element_type != DBUS_TYPE_UNIX_FD)

942 {

943 ptr = va_arg (var_args, const void \*\*);

944 n_elements_p = va_arg (var_args, int\*);

945

946 \_dbus_assert (ptr != NULL);

947 \_dbus_assert (n_elements_p != NULL);

948

949 \_dbus_type_reader_recurse (&real-\>u.reader, &array);

950

951 \_dbus_type_reader_read_fixed_multi (&array, ptr, n_elements_p);

952 }

953 else if (\_DBUS_TYPE_IS_STRINGLIKE (spec_element_type))

954 {

955 char \*\*\*str_array_p;

956 int n_elements;

957 char \*\*str_array;

958

959 str_array_p = va_arg (var_args, char\*\*\*);

960 n_elements_p = va_arg (var_args, int\*);

961

962 \_dbus_assert (str_array_p != NULL);

963 \_dbus_assert (n_elements_p != NULL);

964

965 /\* Count elements in the array \*/

966 \_dbus_type_reader_recurse (&real-\>u.reader, &array);

967

968 n_elements = 0;

969 while (\_dbus_type_reader_get_current_type (&array) != DBUS_TYPE_INVALID)

970 {

971 ++n_elements;

972 \_dbus_type_reader_next (&array);

973 }

974

975 str_array = dbus_new0 (char\*, n_elements + 1);

976 if (str_array == NULL)

977 {

978 \_DBUS_SET_OOM (error);

979 goto out;

980 }

981

982 /\* Now go through and dup each string \*/

983 \_dbus_type_reader_recurse (&real-\>u.reader, &array);

984

985 j = 0;

986 while (j \< n_elements)

987 {

988 const char \*s;

989 \_dbus_type_reader_read_basic (&array,

990 (void \*) &s);

991

992 str_array\[j\] = \_dbus_strdup (s);

993 if (str_array\[j\] == NULL)

994 {

995 dbus_free_string_array (str_array);

996 \_DBUS_SET_OOM (error);

997 goto out;

998 }

999

1000 ++j;

1001

1002 if (!\_dbus_type_reader_next (&array))

1003 \_dbus_assert (j == n_elements);

1004 }

1005

1006 \_dbus_assert (\_dbus_type_reader_get_current_type (&array) == DBUS_TYPE_INVALID);

1007 \_dbus_assert (j == n_elements);

1008 \_dbus_assert (str_array\[j\] == NULL);

1009

1010 \*str_array_p = str_array;

1011 \*n_elements_p = n_elements;

1012 }

1013\#ifndef DBUS_DISABLE_CHECKS

1014 else

1015 {

1016 \_dbus_warn ("you can't read arrays of container types (struct, variant, array) with %s for now",

1017 \_DBUS_FUNCTION_NAME);

1018 goto out;

1019 }

1020\#endif

1021 }

1022\#ifndef DBUS_DISABLE_CHECKS

1023 else

1024 {

1025 \_dbus_warn ("you can only read arrays and basic types with %s for now",

1026 \_DBUS_FUNCTION_NAME);

1027 goto out;

1028 }

1029\#endif

1030

1031 /\* how many arguments already handled \*/

1032 i++;

1033

1034 spec_type = va_arg (var_args, int);

1035 if (!\_dbus_type_reader_next (&real-\>u.reader) && spec_type != DBUS_TYPE_INVALID)

1036 {

1037 dbus_set_error (error, DBUS_ERROR_INVALID_ARGS,

1038 "Message has only %d arguments, but more were expected", i);

1039 goto out;

1040 }

1041 }

1042

1043 retval = TRUE;

1044

1045 out:

1046 /\* there may memory or unix fd leak in the above iteration if parse failed.

1047 \* so we have another iteration over copy_args to free memory and close

1048 \* unix fds.

1049 \*/

1050 if (!retval)

1051 {

1052 spec_type = first_arg_type;

1053 j = 0;

1054

1055 while (j \< i)

1056 {

1057 if (spec_type == DBUS_TYPE_UNIX_FD)

1058 {

1059\#ifdef HAVE_UNIX_FD_PASSING

1060 int \*pfd;

1061

1062 pfd = va_arg (copy_args, int \*);

1063 \_dbus_assert(pfd);

1064 if (\*pfd \>= 0)

1065 {

1066 \_dbus_close (\*pfd, NULL);

1067 \*pfd = -1;

1068 }

1069\#endif

1070 }

1071 else if (dbus_type_is_basic (spec_type))

1072 {

1073 /\* move the index forward \*/

1074 va_arg (copy_args, const void \*);

1075 }

1076 else if (spec_type == DBUS_TYPE_ARRAY)

1077 {

1078 int spec_element_type;

1079

1080 spec_element_type = va_arg (copy_args, int);

1081 if (dbus_type_is_fixed (spec_element_type))

1082 {

1083 /\* move the index forward \*/

1084 va_arg (copy_args, const void \*\*);

1085 va_arg (copy_args, int \*);

1086 }

1087 else if (\_DBUS_TYPE_IS_STRINGLIKE (spec_element_type))

1088 {

1089 char \*\*\*str_array_p;

1090

1091 str_array_p = va_arg (copy_args, char \*\*\*);

1092 /\* move the index forward \*/

1093 va_arg (copy_args, int \*);

1094 \_dbus_assert (str_array_p != NULL);

1095 dbus_free_string_array (\*str_array_p);

1096 \*str_array_p = NULL;

1097 }

1098 }

1099

1100 spec_type = va_arg (copy_args, int);

1101 j++;

1102 }

1103 }

1104

1105 va_end (copy_args);

1106 return retval;

1107}

1108

1167dbus_uint32_t

1168dbus_message_get_serial (DBusMessage \*message)

1169{

1170 \_dbus_return_val_if_fail (message != NULL, 0);

1171

1172 return \_dbus_header_get_serial (&message-\>header);

1173}

1174

1183dbus_bool_t

1184dbus_message_set_reply_serial (DBusMessage \*message,

1185 dbus_uint32_t reply_serial)

1186{

1187 DBusBasicValue value;

1188

1189 \_dbus_return_val_if_fail (message != NULL, FALSE);

1190 \_dbus_return_val_if_fail (!message-\>locked, FALSE);

1191 \_dbus_return_val_if_fail (reply_serial != 0, FALSE); /\* 0 is invalid \*/

1192

1193 value.u32 = reply_serial;

1194

1195 return \_dbus_header_set_field_basic (&message-\>header,

1196 DBUS_HEADER_FIELD_REPLY_SERIAL,

1197 DBUS_TYPE_UINT32,

1198 &value);

1199}

1200

1207dbus_uint32_t

1208dbus_message_get_reply_serial (DBusMessage \*message)

1209{

1210 dbus_uint32_t v_UINT32;

1211

1212 \_dbus_return_val_if_fail (message != NULL, 0);

1213

1214 if (\_dbus_header_get_field_basic (&message-\>header,

1215 DBUS_HEADER_FIELD_REPLY_SERIAL,

1216 DBUS_TYPE_UINT32,

1217 &v_UINT32))

1218 return v_UINT32;

1219 else

1220 return 0;

1221}

1222

1223static void

1224dbus_message_finalize (DBusMessage \*message)

1225{

1226 \_dbus_assert (\_dbus_atomic_get (&message-\>refcount) == 0);

1227

1228 /\* This calls application callbacks! \*/

1229 \_dbus_data_slot_list_free (&message-\>slot_list);

1230

1231 \_dbus_list_foreach (&message-\>counters,

1232 free_counter, message);

1233 \_dbus_list_clear (&message-\>counters);

1234

1235 \_dbus_header_free (&message-\>header);

1236 \_dbus_string_free (&message-\>body);

1237

1238\#ifdef HAVE_UNIX_FD_PASSING

1239 close_unix_fds(message-\>unix_fds, &message-\>n_unix_fds);

1240 dbus_free(message-\>unix_fds);

1241\#endif

1242

1243 \_dbus_assert (\_dbus_atomic_get (&message-\>refcount) == 0);

1244

1245 dbus_free (message);

1246}

1247

1248static DBusMessage\*

1249dbus_message_new_empty_header (void)

1250{

1251 DBusMessage \*message;

1252 dbus_bool_t from_cache;

1253

1254 message = dbus_message_get_cached ();

1255

1256 if (message != NULL)

1257 {

1258 from_cache = TRUE;

1259 }

1260 else

1261 {

1262 from_cache = FALSE;

1263 message = dbus_new0 (DBusMessage, 1);

1264 if (message == NULL)

1265 return NULL;

1266\#ifndef DBUS_DISABLE_CHECKS

1267 message-\>generation = \_dbus_current_generation;

1268\#endif

1269

1270\#ifdef HAVE_UNIX_FD_PASSING

1271 message-\>unix_fds = NULL;

1272 message-\>n_unix_fds_allocated = 0;

1273\#endif

1274 }

1275

1276 \_dbus_atomic_inc (&message-\>refcount);

1277

1278 \_dbus_message_trace_ref (message, 0, 1, "new_empty_header");

1279

1280 message-\>locked = FALSE;

1281\#ifndef DBUS_DISABLE_CHECKS

1282 message-\>in_cache = FALSE;

1283\#endif

1284 message-\>counters = NULL;

1285 message-\>size_counter_delta = 0;

1286 message-\>changed_stamp = 0;

1287

1288\#ifdef HAVE_UNIX_FD_PASSING

1289 message-\>n_unix_fds = 0;

1290 message-\>n_unix_fds_allocated = 0;

1291 message-\>unix_fd_counter_delta = 0;

1292\#endif

1293

1294 if (!from_cache)

1295 \_dbus_data_slot_list_init (&message-\>slot_list);

1296

1297 if (from_cache)

1298 {

1299 \_dbus_header_reinit (&message-\>header);

1300 \_dbus_string_set_length (&message-\>body, 0);

1301 }

1302 else

1303 {

1304 if (!\_dbus_header_init (&message-\>header))

1305 {

1306 dbus_free (message);

1307 return NULL;

1308 }

1309

1310 if (!\_dbus_string_init_preallocated (&message-\>body, 32))

1311 {

1312 \_dbus_header_free (&message-\>header);

1313 dbus_free (message);

1314 return NULL;

1315 }

1316 }

1317

1318 return message;

1319}

1320

1333DBusMessage\*

1334dbus_message_new (int message_type)

1335{

1336 DBusMessage \*message;

1337

1338 \_dbus_return_val_if_fail (message_type != DBUS_MESSAGE_TYPE_INVALID, NULL);

1339

1340 message = dbus_message_new_empty_header ();

1341 if (message == NULL)

1342 return NULL;

1343

1344 if (!\_dbus_header_create (&message-\>header,

1345 DBUS_COMPILER_BYTE_ORDER,

1346 message_type,

1347 NULL, NULL, NULL, NULL, NULL))

1348 {

1349 dbus_message_unref (message);

1350 return NULL;

1351 }

1352

1353 return message;

1354}

1355

1377DBusMessage\*

1378dbus_message_new_method_call (const char \*destination,

1379 const char \*path,

1380 const char \*iface,

1381 const char \*method)

1382{

1383 DBusMessage \*message;

1384

1385 \_dbus_return_val_if_fail (path != NULL, NULL);

1386 \_dbus_return_val_if_fail (method != NULL, NULL);

1387 \_dbus_return_val_if_fail (destination == NULL \|\|

1388 \_dbus_check_is_valid_bus_name (destination), NULL);

1389 \_dbus_return_val_if_fail (\_dbus_check_is_valid_path (path), NULL);

1390 \_dbus_return_val_if_fail (iface == NULL \|\|

1391 \_dbus_check_is_valid_interface (iface), NULL);

1392 \_dbus_return_val_if_fail (\_dbus_check_is_valid_member (method), NULL);

1393

1394 message = dbus_message_new_empty_header ();

1395 if (message == NULL)

1396 return NULL;

1397

1398 if (!\_dbus_header_create (&message-\>header,

1399 DBUS_COMPILER_BYTE_ORDER,

1400 DBUS_MESSAGE_TYPE_METHOD_CALL,

1401 destination, path, iface, method, NULL))

1402 {

1403 dbus_message_unref (message);

1404 return NULL;

1405 }

1406

1407 return message;

1408}

1409

1417DBusMessage\*

1418dbus_message_new_method_return (DBusMessage \*method_call)

1419{

1420 DBusMessage \*message;

1421 const char \*sender;

1422

1423 \_dbus_return_val_if_fail (method_call != NULL, NULL);

1424

1425 sender = dbus_message_get_sender (method_call);

1426

1427 /\* sender is allowed to be null here in peer-to-peer case \*/

1428

1429 message = dbus_message_new_empty_header ();

1430 if (message == NULL)

1431 return NULL;

1432

1433 if (!\_dbus_header_create (&message-\>header,

1434 DBUS_COMPILER_BYTE_ORDER,

1435 DBUS_MESSAGE_TYPE_METHOD_RETURN,

1436 sender, NULL, NULL, NULL, NULL))

1437 {

1438 dbus_message_unref (message);

1439 return NULL;

1440 }

1441

1442 dbus_message_set_no_reply (message, TRUE);

1443

1444 if (!dbus_message_set_reply_serial (message,

1445 dbus_message_get_serial (method_call)))

1446 {

1447 dbus_message_unref (message);

1448 return NULL;

1449 }

1450

1451 return message;

1452}

1453

1468DBusMessage\*

1469dbus_message_new_signal (const char \*path,

1470 const char \*iface,

1471 const char \*name)

1472{

1473 DBusMessage \*message;

1474

1475 \_dbus_return_val_if_fail (path != NULL, NULL);

1476 \_dbus_return_val_if_fail (iface != NULL, NULL);

1477 \_dbus_return_val_if_fail (name != NULL, NULL);

1478 \_dbus_return_val_if_fail (\_dbus_check_is_valid_path (path), NULL);

1479 \_dbus_return_val_if_fail (\_dbus_check_is_valid_interface (iface), NULL);

1480 \_dbus_return_val_if_fail (\_dbus_check_is_valid_member (name), NULL);

1481

1482 message = dbus_message_new_empty_header ();

1483 if (message == NULL)

1484 return NULL;

1485

1486 if (!\_dbus_header_create (&message-\>header,

1487 DBUS_COMPILER_BYTE_ORDER,

1488 DBUS_MESSAGE_TYPE_SIGNAL,

1489 NULL, path, iface, name, NULL))

1490 {

1491 dbus_message_unref (message);

1492 return NULL;

1493 }

1494

1495 dbus_message_set_no_reply (message, TRUE);

1496

1497 return message;

1498}

1499

1514DBusMessage\*

1515dbus_message_new_error (DBusMessage \*reply_to,

1516 const char \*error_name,

1517 const char \*error_message)

1518{

1519 DBusMessage \*message;

1520 const char \*sender;

1521 DBusMessageIter iter;

1522

1523 \_dbus_return_val_if_fail (reply_to != NULL, NULL);

1524 \_dbus_return_val_if_fail (error_name != NULL, NULL);

1525 \_dbus_return_val_if_fail (\_dbus_check_is_valid_error_name (error_name), NULL);

1526

1527 sender = dbus_message_get_sender (reply_to);

1528

1529 /\* sender may be NULL for non-message-bus case or

1530 \* when the message bus is dealing with an unregistered

1531 \* connection.

1532 \*/

1533 message = dbus_message_new_empty_header ();

1534 if (message == NULL)

1535 return NULL;

1536

1537 if (!\_dbus_header_create (&message-\>header,

1538 DBUS_COMPILER_BYTE_ORDER,

1539 DBUS_MESSAGE_TYPE_ERROR,

1540 sender, NULL, NULL, NULL, error_name))

1541 {

1542 dbus_message_unref (message);

1543 return NULL;

1544 }

1545

1546 dbus_message_set_no_reply (message, TRUE);

1547

1548 if (!dbus_message_set_reply_serial (message,

1549 dbus_message_get_serial (reply_to)))

1550 {

1551 dbus_message_unref (message);

1552 return NULL;

1553 }

1554

1555 if (error_message != NULL)

1556 {

1557 dbus_message_iter_init_append (message, &iter);

1558 if (!dbus_message_iter_append_basic (&iter,

1559 DBUS_TYPE_STRING,

1560 &error_message))

1561 {

1562 dbus_message_unref (message);

1563 return NULL;

1564 }

1565 }

1566

1567 return message;

1568}

1569

1586DBusMessage\*

1587dbus_message_new_error_printf (DBusMessage \*reply_to,

1588 const char \*error_name,

1589 const char \*error_format,

1590 ...)

1591{

1592 va_list args;

1593 DBusString str;

1594 DBusMessage \*message;

1595

1596 \_dbus_return_val_if_fail (reply_to != NULL, NULL);

1597 \_dbus_return_val_if_fail (error_name != NULL, NULL);

1598 \_dbus_return_val_if_fail (\_dbus_check_is_valid_error_name (error_name), NULL);

1599

1600 if (!\_dbus_string_init (&str))

1601 return NULL;

1602

1603 va_start (args, error_format);

1604

1605 if (\_dbus_string_append_printf_valist (&str, error_format, args))

1606 message = dbus_message_new_error (reply_to, error_name,

1607 \_dbus_string_get_const_data (&str));

1608 else

1609 message = NULL;

1610

1611 \_dbus_string_free (&str);

1612

1613 va_end (args);

1614

1615 return message;

1616}

1617

1618

1631DBusMessage \*

1632dbus_message_copy (const DBusMessage \*message)

1633{

1634 DBusMessage \*retval;

1635

1636 \_dbus_return_val_if_fail (message != NULL, NULL);

1637

1638 retval = dbus_new0 (DBusMessage, 1);

1639 if (retval == NULL)

1640 return NULL;

1641

1642 \_dbus_atomic_inc (&retval-\>refcount);

1643

1644 retval-\>locked = FALSE;

1645\#ifndef DBUS_DISABLE_CHECKS

1646 retval-\>generation = message-\>generation;

1647\#endif

1648

1649 if (!\_dbus_header_copy (&message-\>header, &retval-\>header))

1650 {

1651 dbus_free (retval);

1652 return NULL;

1653 }

1654

1655 if (!\_dbus_string_init_preallocated (&retval-\>body,

1656 \_dbus_string_get_length (&message-\>body)))

1657 {

1658 \_dbus_header_free (&retval-\>header);

1659 dbus_free (retval);

1660 return NULL;

1661 }

1662

1663 if (!\_dbus_string_copy (&message-\>body, 0,

1664 &retval-\>body, 0))

1665 goto failed_copy;

1666

1667\#ifdef HAVE_UNIX_FD_PASSING

1668 retval-\>unix_fds = dbus_new(int, message-\>n_unix_fds);

1669 if (retval-\>unix_fds == NULL && message-\>n_unix_fds \> 0)

1670 goto failed_copy;

1671

1672 retval-\>n_unix_fds_allocated = message-\>n_unix_fds;

1673

1674 for (retval-\>n_unix_fds = 0;

1675 retval-\>n_unix_fds \< message-\>n_unix_fds;

1676 retval-\>n_unix_fds++)

1677 {

1678 retval-\>unix_fds\[retval-\>n_unix_fds\] = \_dbus_dup(message-\>unix_fds\[retval-\>n_unix_fds\], NULL);

1679

1680 if (retval-\>unix_fds\[retval-\>n_unix_fds\] \< 0)

1681 goto failed_copy;

1682 }

1683

1684\#endif

1685

1686 \_dbus_message_trace_ref (retval, 0, 1, "copy");

1687 return retval;

1688

1689 failed_copy:

1690 \_dbus_header_free (&retval-\>header);

1691 \_dbus_string_free (&retval-\>body);

1692

1693\#ifdef HAVE_UNIX_FD_PASSING

1694 close_unix_fds(retval-\>unix_fds, &retval-\>n_unix_fds);

1695 dbus_free(retval-\>unix_fds);

1696\#endif

1697

1698 dbus_free (retval);

1699

1700 return NULL;

1701}

1702

1703

1711DBusMessage \*

1712dbus_message_ref (DBusMessage \*message)

1713{

1714 dbus_int32_t old_refcount;

1715

1716 \_dbus_return_val_if_fail (message != NULL, NULL);

1717 \_dbus_return_val_if_fail (message-\>generation == \_dbus_current_generation, NULL);

1718 \_dbus_return_val_if_fail (!message-\>in_cache, NULL);

1719

1720 old_refcount = \_dbus_atomic_inc (&message-\>refcount);

1721 \_dbus_assert (old_refcount \>= 1);

1722 \_dbus_message_trace_ref (message, old_refcount, old_refcount + 1, "ref");

1723

1724 return message;

1725}

1726

1734void

1735dbus_message_unref (DBusMessage \*message)

1736{

1737 dbus_int32_t old_refcount;

1738

1739 \_dbus_return_if_fail (message != NULL);

1740 \_dbus_return_if_fail (message-\>generation == \_dbus_current_generation);

1741 \_dbus_return_if_fail (!message-\>in_cache);

1742

1743 old_refcount = \_dbus_atomic_dec (&message-\>refcount);

1744

1745 \_dbus_assert (old_refcount \>= 1);

1746

1747 \_dbus_message_trace_ref (message, old_refcount, old_refcount - 1, "unref");

1748

1749 if (old_refcount == 1)

1750 {

1751 /\* Calls application callbacks! \*/

1752 dbus_message_cache_or_finalize (message);

1753 }

1754}

1755

1766int

1767dbus_message_get_type (DBusMessage \*message)

1768{

1769 \_dbus_return_val_if_fail (message != NULL, DBUS_MESSAGE_TYPE_INVALID);

1770

1771 return \_dbus_header_get_message_type (&message-\>header);

1772}

1773

1842dbus_bool_t

1843dbus_message_append_args (DBusMessage \*message,

1844 int first_arg_type,

1845 ...)

1846{

1847 dbus_bool_t retval;

1848 va_list var_args;

1849

1850 \_dbus_return_val_if_fail (message != NULL, FALSE);

1851

1852 va_start (var_args, first_arg_type);

1853 retval = dbus_message_append_args_valist (message,

1854 first_arg_type,

1855 var_args);

1856 va_end (var_args);

1857

1858 return retval;

1859}

1860

1874dbus_bool_t

1875dbus_message_append_args_valist (DBusMessage \*message,

1876 int first_arg_type,

1877 va_list var_args)

1878{

1879 int type;

1880 DBusMessageIter iter;

1881

1882 \_dbus_return_val_if_fail (message != NULL, FALSE);

1883

1884 type = first_arg_type;

1885

1886 dbus_message_iter_init_append (message, &iter);

1887

1888 while (type != DBUS_TYPE_INVALID)

1889 {

1890 if (dbus_type_is_basic (type))

1891 {

1892 const void \*value;

1893 value = va_arg (var_args, const void \*);

1894

1895 if (!dbus_message_iter_append_basic (&iter,

1896 type,

1897 value))

1898 goto failed;

1899 }

1900 else if (type == DBUS_TYPE_ARRAY)

1901 {

1902 int element_type;

1903 DBusMessageIter array;

1904 char buf\[2\];

1905

1906 element_type = va_arg (var_args, int);

1907

1908 buf\[0\] = element_type;

1909 buf\[1\] = '\0';

1910 if (!dbus_message_iter_open_container (&iter,

1911 DBUS_TYPE_ARRAY,

1912 buf,

1913 &array))

1914 goto failed;

1915

1916 if (dbus_type_is_fixed (element_type) &&

1917 element_type != DBUS_TYPE_UNIX_FD)

1918 {

1919 const void \*\*value;

1920 int n_elements;

1921

1922 value = va_arg (var_args, const void \*\*);

1923 n_elements = va_arg (var_args, int);

1924

1925 if (!dbus_message_iter_append_fixed_array (&array,

1926 element_type,

1927 value,

1928 n_elements)) {

1929 dbus_message_iter_abandon_container (&iter, &array);

1930 goto failed;

1931 }

1932 }

1933 else if (\_DBUS_TYPE_IS_STRINGLIKE (element_type))

1934 {

1935 const char \*\*\*value_p;

1936 const char \*\*value;

1937 int n_elements;

1938 int i;

1939

1940 value_p = va_arg (var_args, const char\*\*\*);

1941 n_elements = va_arg (var_args, int);

1942

1943 value = \*value_p;

1944

1945 i = 0;

1946 while (i \< n_elements)

1947 {

1948 if (!dbus_message_iter_append_basic (&array,

1949 element_type,

1950 &value\[i\])) {

1951 dbus_message_iter_abandon_container (&iter, &array);

1952 goto failed;

1953 }

1954 ++i;

1955 }

1956 }

1957 else

1958 {

1959 \_dbus_warn ("arrays of %s can't be appended with %s for now",

1960 \_dbus_type_to_string (element_type),

1961 \_DBUS_FUNCTION_NAME);

1962 dbus_message_iter_abandon_container (&iter, &array);

1963 goto failed;

1964 }

1965

1966 if (!dbus_message_iter_close_container (&iter, &array))

1967 goto failed;

1968 }

1969\#ifndef DBUS_DISABLE_CHECKS

1970 else

1971 {

1972 \_dbus_warn ("type %s isn't supported yet in %s",

1973 \_dbus_type_to_string (type), \_DBUS_FUNCTION_NAME);

1974 goto failed;

1975 }

1976\#endif

1977

1978 type = va_arg (var_args, int);

1979 }

1980

1981 return TRUE;

1982

1983 failed:

1984 return FALSE;

1985}

1986

2031dbus_bool_t

2032dbus_message_get_args (DBusMessage \*message,

2033 DBusError \*error,

2034 int first_arg_type,

2035 ...)

2036{

2037 dbus_bool_t retval;

2038 va_list var_args;

2039

2040 \_dbus_return_val_if_fail (message != NULL, FALSE);

2041 \_dbus_return_val_if_error_is_set (error, FALSE);

2042

2043 va_start (var_args, first_arg_type);

2044 retval = dbus_message_get_args_valist (message, error, first_arg_type, var_args);

2045 va_end (var_args);

2046

2047 return retval;

2048}

2049

2060dbus_bool_t

2061dbus_message_get_args_valist (DBusMessage \*message,

2062 DBusError \*error,

2063 int first_arg_type,

2064 va_list var_args)

2065{

2066 DBusMessageIter iter;

2067

2068 \_dbus_return_val_if_fail (message != NULL, FALSE);

2069 \_dbus_return_val_if_error_is_set (error, FALSE);

2070

2071 dbus_message_iter_init (message, &iter);

2072 return \_dbus_message_iter_get_args_valist (&iter, error, first_arg_type, var_args);

2073}

2074

2075static void

2076\_dbus_message_iter_init_common (DBusMessage \*message,

2077 DBusMessageRealIter \*real,

2078 int iter_type)

2079{

2080 /\* If these static assertions fail on your platform, report it as a bug. \*/

2081 \_DBUS_STATIC_ASSERT (sizeof (DBusMessageRealIter) \<= sizeof (DBusMessageIter));

2082 \_DBUS_STATIC_ASSERT (\_DBUS_ALIGNOF (DBusMessageRealIter) \<=

2083 \_DBUS_ALIGNOF (DBusMessageIter));

2084\#if CHECK_DBUS_1_10_BINARY_COMPATIBILITY

2085 /\* A failure of these two assertions would indicate that we've broken

2086 \* ABI on this platform since 1.10.0. \*/

2087 \_DBUS_STATIC_ASSERT (sizeof (DBusMessageIter_1_10_0) ==

2088 sizeof (DBusMessageIter));

2089 \_DBUS_STATIC_ASSERT (\_DBUS_ALIGNOF (DBusMessageIter_1_10_0) ==

2090 \_DBUS_ALIGNOF (DBusMessageIter));

2091\#endif

2092 /\* If this static assertion fails, it means the DBusMessageIter struct

2093 \* is not "packed", which might result in "iter = other_iter" not copying

2094 \* every byte. \*/

2095\#if DBUS_SIZEOF_VOID_P \> 8

2096 \_DBUS_STATIC_ASSERT (sizeof (DBusMessageIter) == 16 \* sizeof (void \*));

2097\#else

2098 \_DBUS_STATIC_ASSERT (sizeof (DBusMessageIter) ==

2099 4 \* sizeof (void \*) + sizeof (dbus_uint32_t) + 9 \* sizeof (int));

2100\#endif

2101

2102 /\* Since the iterator will read or write who-knows-what from the

2103 \* message, we need to get in the right byte order

2104 \*/

2105 ensure_byte_order (message);

2106

2107 real-\>message = message;

2108 real-\>changed_stamp = message-\>changed_stamp;

2109 real-\>iter_type = iter_type;

2110 real-\>sig_refcount = 0;

2111}

2112

2135dbus_bool_t

2136dbus_message_iter_init (DBusMessage \*message,

2137 DBusMessageIter \*iter)

2138{

2139 DBusMessageRealIter \*real = (DBusMessageRealIter \*)iter;

2140 const DBusString \*type_str;

2141 int type_pos;

2142

2143 \_dbus_return_val_if_fail (message != NULL, FALSE);

2144 \_dbus_return_val_if_fail (iter != NULL, FALSE);

2145

2146 get_const_signature (&message-\>header, &type_str, &type_pos);

2147

2148 \_dbus_message_iter_init_common (message, real,

2149 DBUS_MESSAGE_ITER_TYPE_READER);

2150

2151 \_dbus_type_reader_init (&real-\>u.reader,

2152 \_dbus_header_get_byte_order (&message-\>header),

2153 type_str, type_pos,

2154 &message-\>body,

2155 0);

2156

2157 return \_dbus_type_reader_get_current_type (&real-\>u.reader) != DBUS_TYPE_INVALID;

2158}

2159

2166dbus_bool_t

2167dbus_message_iter_has_next (DBusMessageIter \*iter)

2168{

2169 DBusMessageRealIter \*real = (DBusMessageRealIter \*)iter;

2170

2171 \_dbus_return_val_if_fail (\_dbus_message_iter_check (real), FALSE);

2172 \_dbus_return_val_if_fail (real-\>iter_type == DBUS_MESSAGE_ITER_TYPE_READER, FALSE);

2173

2174 return \_dbus_type_reader_has_next (&real-\>u.reader);

2175}

2176

2185dbus_bool_t

2186dbus_message_iter_next (DBusMessageIter \*iter)

2187{

2188 DBusMessageRealIter \*real = (DBusMessageRealIter \*)iter;

2189

2190 \_dbus_return_val_if_fail (\_dbus_message_iter_check (real), FALSE);

2191 \_dbus_return_val_if_fail (real-\>iter_type == DBUS_MESSAGE_ITER_TYPE_READER, FALSE);

2192

2193 return \_dbus_type_reader_next (&real-\>u.reader);

2194}

2195

2210int

2211dbus_message_iter_get_arg_type (DBusMessageIter \*iter)

2212{

2213 DBusMessageRealIter \*real = (DBusMessageRealIter \*)iter;

2214

2215 \_dbus_return_val_if_fail (\_dbus_message_iter_check (real), DBUS_TYPE_INVALID);

2216 \_dbus_return_val_if_fail (real-\>iter_type == DBUS_MESSAGE_ITER_TYPE_READER, FALSE);

2217

2218 return \_dbus_type_reader_get_current_type (&real-\>u.reader);

2219}

2220

2229int

2230dbus_message_iter_get_element_type (DBusMessageIter \*iter)

2231{

2232 DBusMessageRealIter \*real = (DBusMessageRealIter \*)iter;

2233

2234 \_dbus_return_val_if_fail (\_dbus_message_iter_check (real), DBUS_TYPE_INVALID);

2235 \_dbus_return_val_if_fail (real-\>iter_type == DBUS_MESSAGE_ITER_TYPE_READER, DBUS_TYPE_INVALID);

2236 \_dbus_return_val_if_fail (dbus_message_iter_get_arg_type (iter) == DBUS_TYPE_ARRAY, DBUS_TYPE_INVALID);

2237

2238 return \_dbus_type_reader_get_element_type (&real-\>u.reader);

2239}

2240

2266void

2267dbus_message_iter_recurse (DBusMessageIter \*iter,

2268 DBusMessageIter \*sub)

2269{

2270 DBusMessageRealIter \*real = (DBusMessageRealIter \*)iter;

2271 DBusMessageRealIter \*real_sub = (DBusMessageRealIter \*)sub;

2272

2273 \_dbus_return_if_fail (\_dbus_message_iter_check (real));

2274 \_dbus_return_if_fail (sub != NULL);

2275

2276 \*real_sub = \*real;

2277 \_dbus_type_reader_recurse (&real-\>u.reader, &real_sub-\>u.reader);

2278}

2279

2291char \*

2292dbus_message_iter_get_signature (DBusMessageIter \*iter)

2293{

2294 const DBusString \*sig;

2295 DBusString retstr;

2296 char \*ret = NULL;

2297 int start, len;

2298 DBusMessageRealIter \*real = (DBusMessageRealIter \*)iter;

2299

2300 \_dbus_return_val_if_fail (\_dbus_message_iter_check (real), NULL);

2301

2302 if (!\_dbus_string_init (&retstr))

2303 return NULL;

2304

2305 \_dbus_type_reader_get_signature (&real-\>u.reader, &sig,

2306 &start, &len);

2307 if (!\_dbus_string_append_len (&retstr,

2308 \_dbus_string_get_const_data (sig) + start,

2309 len))

2310 goto oom;

2311

2312 /\* This is correct whether it succeeds or fails: on success it sets \`ret\`,

2313 \* and on failure it leaves \`ret\` set to NULL. \*/

2314 \_dbus_string_steal_data (&retstr, &ret);

2315

2316oom:

2317 \_dbus_string_free (&retstr);

2318 return ret;

2319}

2320

2368void

2369dbus_message_iter_get_basic (DBusMessageIter \*iter,

2370 void \*value)

2371{

2372 DBusMessageRealIter \*real = (DBusMessageRealIter \*)iter;

2373

2374 \_dbus_return_if_fail (\_dbus_message_iter_check (real));

2375 \_dbus_return_if_fail (value != NULL);

2376

2377 if (dbus_message_iter_get_arg_type (iter) == DBUS_TYPE_UNIX_FD)

2378 {

2379\#ifdef HAVE_UNIX_FD_PASSING

2380 DBusBasicValue idx;

2381

2382 \_dbus_type_reader_read_basic(&real-\>u.reader, &idx);

2383

2384 if (idx.u32 \>= real-\>message-\>n_unix_fds) {

2385 /\* Hmm, we cannot really signal an error here, so let's make

2386 sure to return an invalid fd. \*/

2387 \*((int\*) value) = -1;

2388 return;

2389 }

2390

2391 \*((int\*) value) = \_dbus_dup(real-\>message-\>unix_fds\[idx.u32\], NULL);

2392\#else

2393 \*((int\*) value) = -1;

2394\#endif

2395 }

2396 else

2397 {

2398 \_dbus_type_reader_read_basic (&real-\>u.reader,

2399 value);

2400 }

2401}

2402

2413int

2414dbus_message_iter_get_element_count (DBusMessageIter \*iter)

2415{

2416 DBusMessageRealIter \*real = (DBusMessageRealIter \*)iter;

2417 DBusTypeReader array;

2418 int element_type;

2419 int n_elements = 0;

2420

2421 \_dbus_return_val_if_fail (\_dbus_message_iter_check (real), 0);

2422 \_dbus_return_val_if_fail (\_dbus_type_reader_get_current_type (&real-\>u.reader)

2423 == DBUS_TYPE_ARRAY, 0);

2424

2425 element_type = \_dbus_type_reader_get_element_type (&real-\>u.reader);

2426 \_dbus_type_reader_recurse (&real-\>u.reader, &array);

2427 if (dbus_type_is_fixed (element_type))

2428 {

2429 int alignment = \_dbus_type_get_alignment (element_type);

2430 int total_len = \_dbus_type_reader_get_array_length (&array);

2431 n_elements = total_len / alignment;

2432 }

2433 else

2434 {

2435 while (\_dbus_type_reader_get_current_type (&array) != DBUS_TYPE_INVALID)

2436 {

2437 ++n_elements;

2438 \_dbus_type_reader_next (&array);

2439 }

2440 }

2441

2442 return n_elements;

2443}

2444

2457int

2458dbus_message_iter_get_array_len (DBusMessageIter \*iter)

2459{

2460 DBusMessageRealIter \*real = (DBusMessageRealIter \*)iter;

2461

2462 \_dbus_return_val_if_fail (\_dbus_message_iter_check (real), 0);

2463

2464 return \_dbus_type_reader_get_array_length (&real-\>u.reader);

2465}

2466

2502void

2503dbus_message_iter_get_fixed_array (DBusMessageIter \*iter,

2504 void \*value,

2505 int \*n_elements)

2506{

2507 DBusMessageRealIter \*real = (DBusMessageRealIter \*)iter;

2508\#ifndef DBUS_DISABLE_CHECKS

2509 int subtype = \_dbus_type_reader_get_current_type(&real-\>u.reader);

2510

2511 \_dbus_return_if_fail (\_dbus_message_iter_check (real));

2512 \_dbus_return_if_fail (value != NULL);

2513 \_dbus_return_if_fail ((subtype == DBUS_TYPE_INVALID) \|\|

2514 (dbus_type_is_fixed (subtype) && subtype != DBUS_TYPE_UNIX_FD));

2515\#endif

2516

2517 \_dbus_type_reader_read_fixed_multi (&real-\>u.reader,

2518 value, n_elements);

2519}

2520

2532void

2533dbus_message_iter_init_append (DBusMessage \*message,

2534 DBusMessageIter \*iter)

2535{

2536 DBusMessageRealIter \*real = (DBusMessageRealIter \*)iter;

2537

2538 \_dbus_return_if_fail (message != NULL);

2539 \_dbus_return_if_fail (iter != NULL);

2540

2541 \_dbus_message_iter_init_common (message, real,

2542 DBUS_MESSAGE_ITER_TYPE_WRITER);

2543

2544 /\* We create the signature string and point iterators at it "on demand"

2545 \* when a value is actually appended. That means that init() never fails

2546 \* due to OOM.

2547 \*/

2548 \_dbus_type_writer_init_types_delayed (&real-\>u.writer,

2549 \_dbus_header_get_byte_order (&message-\>header),

2550 &message-\>body,

2551 \_dbus_string_get_length (&message-\>body));

2552}

2553

2562static dbus_bool_t

2563\_dbus_message_iter_open_signature (DBusMessageRealIter \*real)

2564{

2565 DBusString \*str;

2566 const DBusString \*current_sig;

2567 int current_sig_pos;

2568

2569 \_dbus_assert (real-\>iter_type == DBUS_MESSAGE_ITER_TYPE_WRITER);

2570

2571 if (real-\>u.writer.type_str != NULL)

2572 {

2573 \_dbus_assert (real-\>sig_refcount \> 0);

2574 real-\>sig_refcount += 1;

2575 return TRUE;

2576 }

2577

2578 str = dbus_new (DBusString, 1);

2579 if (str == NULL)

2580 return FALSE;

2581

2582 if (!\_dbus_header_get_field_raw (&real-\>message-\>header,

2583 DBUS_HEADER_FIELD_SIGNATURE,

2584 &current_sig, &current_sig_pos))

2585 current_sig = NULL;

2586

2587 if (current_sig)

2588 {

2589 int current_len;

2590

2591 current_len = \_dbus_string_get_byte (current_sig, current_sig_pos);

2592 current_sig_pos += 1; /\* move on to sig data \*/

2593

2594 if (!\_dbus_string_init_preallocated (str, current_len + 4))

2595 {

2596 dbus_free (str);

2597 return FALSE;

2598 }

2599

2600 if (!\_dbus_string_copy_len (current_sig, current_sig_pos, current_len,

2601 str, 0))

2602 {

2603 \_dbus_string_free (str);

2604 dbus_free (str);

2605 return FALSE;

2606 }

2607 }

2608 else

2609 {

2610 if (!\_dbus_string_init_preallocated (str, 4))

2611 {

2612 dbus_free (str);

2613 return FALSE;

2614 }

2615 }

2616

2617 real-\>sig_refcount = 1;

2618

2619 /\* If this assertion failed, then str would be neither stored in u.writer

2620 \* nor freed by this function, resulting in a memory leak. \*/

2621 \_dbus_assert (real-\>u.writer.type_str == NULL);

2622 \_dbus_type_writer_add_types (&real-\>u.writer,

2623 str, \_dbus_string_get_length (str));

2624 return TRUE;

2625}

2626

2636static dbus_bool_t

2637\_dbus_message_iter_close_signature (DBusMessageRealIter \*real)

2638{

2639 DBusString \*str;

2640 const char \*v_STRING;

2641 dbus_bool_t retval;

2642

2643 \_dbus_assert (real-\>iter_type == DBUS_MESSAGE_ITER_TYPE_WRITER);

2644 \_dbus_assert (real-\>u.writer.type_str != NULL);

2645 \_dbus_assert (real-\>sig_refcount \> 0);

2646

2647 real-\>sig_refcount -= 1;

2648

2649 if (real-\>sig_refcount \> 0)

2650 return TRUE;

2651 \_dbus_assert (real-\>sig_refcount == 0);

2652

2653 retval = TRUE;

2654

2655 str = real-\>u.writer.type_str;

2656

2657 v_STRING = \_dbus_string_get_const_data (str);

2658 if (!\_dbus_header_set_field_basic (&real-\>message-\>header,

2659 DBUS_HEADER_FIELD_SIGNATURE,

2660 DBUS_TYPE_SIGNATURE,

2661 &v_STRING))

2662 retval = FALSE;

2663

2664 \_dbus_type_writer_remove_types (&real-\>u.writer);

2665 \_dbus_string_free (str);

2666 dbus_free (str);

2667

2668 return retval;

2669}

2670

2678static void

2679\_dbus_message_iter_abandon_signature (DBusMessageRealIter \*real)

2680{

2681 DBusString \*str;

2682

2683 \_dbus_assert (real-\>iter_type == DBUS_MESSAGE_ITER_TYPE_WRITER);

2684 \_dbus_assert (real-\>u.writer.type_str != NULL);

2685 \_dbus_assert (real-\>sig_refcount \> 0);

2686

2687 real-\>sig_refcount -= 1;

2688

2689 if (real-\>sig_refcount \> 0)

2690 return;

2691 \_dbus_assert (real-\>sig_refcount == 0);

2692

2693 str = real-\>u.writer.type_str;

2694

2695 \_dbus_type_writer_remove_types (&real-\>u.writer);

2696 \_dbus_string_free (str);

2697 dbus_free (str);

2698}

2699

2700\#if defined(DBUS_ENABLE_CHECKS) \|\| defined(DBUS_ENABLE_ASSERT)

2701static dbus_bool_t

2702\_dbus_message_iter_append_check (DBusMessageRealIter \*iter)

2703{

2704 if (!\_dbus_message_iter_check (iter))

2705 return FALSE;

2706

2707 if (iter-\>message-\>locked)

2708 {

2709 \_dbus_warn_check_failed ("dbus append iterator can't be used: message is locked (has already been sent)");

2710 return FALSE;

2711 }

2712

2713 return TRUE;

2714}

2715\#endif

2716

2717\#ifdef HAVE_UNIX_FD_PASSING

2718static int \*

2719expand_fd_array(DBusMessage \*m,

2720 unsigned n)

2721{

2722 \_dbus_assert(m);

2723

2724 /\* This makes space for adding n new fds to the array and returns a

2725 pointer to the place were the first fd should be put. \*/

2726

2727 if (m-\>n_unix_fds + n \> m-\>n_unix_fds_allocated)

2728 {

2729 unsigned k;

2730 int \*p;

2731

2732 /\* Make twice as much space as necessary \*/

2733 k = (m-\>n_unix_fds + n) \* 2;

2734

2735 /\* Allocate at least four \*/

2736 if (k \< 4)

2737 k = 4;

2738

2739 p = dbus_realloc(m-\>unix_fds, k \* sizeof(int));

2740 if (p == NULL)

2741 return NULL;

2742

2743 m-\>unix_fds = p;

2744 m-\>n_unix_fds_allocated = k;

2745 }

2746

2747 return m-\>unix_fds + m-\>n_unix_fds;

2748}

2749\#endif

2750

2770dbus_bool_t

2771dbus_message_iter_append_basic (DBusMessageIter \*iter,

2772 int type,

2773 const void \*value)

2774{

2775 DBusMessageRealIter \*real = (DBusMessageRealIter \*)iter;

2776 dbus_bool_t ret;

2777

2778 \_dbus_return_val_if_fail (\_dbus_message_iter_append_check (real), FALSE);

2779 \_dbus_return_val_if_fail (real-\>iter_type == DBUS_MESSAGE_ITER_TYPE_WRITER, FALSE);

2780 \_dbus_return_val_if_fail (dbus_type_is_basic (type), FALSE);

2781 \_dbus_return_val_if_fail (value != NULL, FALSE);

2782

2783\#ifndef DBUS_DISABLE_CHECKS

2784 switch (type)

2785 {

2786 DBusString str;

2787 DBusValidity signature_validity;

2788 const char \* const \*string_p;

2789 const dbus_bool_t \*bool_p;

2790

2791 case DBUS_TYPE_STRING:

2792 string_p = value;

2793 \_dbus_return_val_if_fail (\_dbus_check_is_valid_utf8 (\*string_p), FALSE);

2794 break;

2795

2796 case DBUS_TYPE_OBJECT_PATH:

2797 string_p = value;

2798 \_dbus_return_val_if_fail (\_dbus_check_is_valid_path (\*string_p), FALSE);

2799 break;

2800

2801 case DBUS_TYPE_SIGNATURE:

2802 string_p = value;

2803 \_dbus_string_init_const (&str, \*string_p);

2804 signature_validity = \_dbus_validate_signature_with_reason (&str,

2805 0,

2806 \_dbus_string_get_length (&str));

2807

2808 if (signature_validity == DBUS_VALIDITY_UNKNOWN_OOM_ERROR)

2809 return FALSE;

2810

2811 \_dbus_return_val_if_fail (signature_validity == DBUS_VALID, FALSE);

2812 break;

2813

2814 case DBUS_TYPE_BOOLEAN:

2815 bool_p = value;

2816 \_dbus_return_val_if_fail (\*bool_p == 0 \|\| \*bool_p == 1, FALSE);

2817 break;

2818

2819 default:

2820 {

2821 /\* nothing to check, all possible values are allowed \*/

2822 }

2823 }

2824\#endif

2825

2826 if (!\_dbus_message_iter_open_signature (real))

2827 return FALSE;

2828

2829 if (type == DBUS_TYPE_UNIX_FD)

2830 {

2831\#ifdef HAVE_UNIX_FD_PASSING

2832 int \*fds;

2833 dbus_uint32_t u;

2834

2835 ret = FALSE;

2836

2837 /\* First step, include the fd in the fd list of this message \*/

2838 if (!(fds = expand_fd_array(real-\>message, 1)))

2839 goto out;

2840

2841 \*fds = \_dbus_dup(\*(int\*) value, NULL);

2842 if (\*fds \< 0)

2843 goto out;

2844

2845 u = real-\>message-\>n_unix_fds;

2846

2847 /\* Second step, write the index to the fd \*/

2848 if (!(ret = \_dbus_type_writer_write_basic (&real-\>u.writer, DBUS_TYPE_UNIX_FD, &u))) {

2849 \_dbus_close(\*fds, NULL);

2850 goto out;

2851 }

2852

2853 real-\>message-\>n_unix_fds += 1;

2854 u += 1;

2855

2856 /\* Final step, update the header accordingly \*/

2857 ret = \_dbus_header_set_field_basic (&real-\>message-\>header,

2858 DBUS_HEADER_FIELD_UNIX_FDS,

2859 DBUS_TYPE_UINT32,

2860 &u);

2861

2862 /\* If any of these operations fail the message is

2863 hosed. However, no memory or fds should be leaked since what

2864 has been added to message has been added to the message, and

2865 can hence be accounted for when the message is being

2866 freed. \*/

2867\#else

2868 ret = FALSE;

2869 /\* This is redundant (we could just fall through), but it avoids

2870 \* -Wunused-label in builds that don't HAVE_UNIX_FD_PASSING \*/

2871 goto out;

2872\#endif

2873 }

2874 else

2875 {

2876 ret = \_dbus_type_writer_write_basic (&real-\>u.writer, type, value);

2877 }

2878

2879out:

2880 if (!\_dbus_message_iter_close_signature (real))

2881 ret = FALSE;

2882

2883 return ret;

2884}

2885

2921dbus_bool_t

2922dbus_message_iter_append_fixed_array (DBusMessageIter \*iter,

2923 int element_type,

2924 const void \*value,

2925 int n_elements)

2926{

2927 DBusMessageRealIter \*real = (DBusMessageRealIter \*)iter;

2928 dbus_bool_t ret;

2929

2930 \_dbus_return_val_if_fail (\_dbus_message_iter_append_check (real), FALSE);

2931 \_dbus_return_val_if_fail (real-\>iter_type == DBUS_MESSAGE_ITER_TYPE_WRITER, FALSE);

2932 \_dbus_return_val_if_fail (dbus_type_is_fixed (element_type) && element_type != DBUS_TYPE_UNIX_FD, FALSE);

2933 \_dbus_return_val_if_fail (real-\>u.writer.container_type == DBUS_TYPE_ARRAY, FALSE);

2934 \_dbus_return_val_if_fail (value != NULL, FALSE);

2935 \_dbus_return_val_if_fail (n_elements \>= 0, FALSE);

2936 \_dbus_return_val_if_fail (n_elements \<=

2937 DBUS_MAXIMUM_ARRAY_LENGTH / \_dbus_type_get_alignment (element_type),

2938 FALSE);

2939

2940\#ifndef DBUS_DISABLE_CHECKS

2941 if (element_type == DBUS_TYPE_BOOLEAN)

2942 {

2943 const dbus_bool_t \* const \*bools = value;

2944 int i;

2945

2946 for (i = 0; i \< n_elements; i++)

2947 {

2948 \_dbus_return_val_if_fail ((\*bools)\[i\] == 0 \|\| (\*bools)\[i\] == 1, FALSE);

2949 }

2950 }

2951\#endif

2952

2953 ret = \_dbus_type_writer_write_fixed_multi (&real-\>u.writer, element_type, value, n_elements);

2954

2955 return ret;

2956}

2957

2985dbus_bool_t

2986dbus_message_iter_open_container (DBusMessageIter \*iter,

2987 int type,

2988 const char \*contained_signature,

2989 DBusMessageIter \*sub)

2990{

2991 DBusMessageRealIter \*real = (DBusMessageRealIter \*)iter;

2992 DBusMessageRealIter \*real_sub = (DBusMessageRealIter \*)sub;

2993 DBusString contained_str;

2994 DBusValidity contained_signature_validity;

2995 dbus_bool_t ret;

2996

2997 \_dbus_return_val_if_fail (sub != NULL, FALSE);

2998 /\* Do our best to make sure the sub-iterator doesn't contain something

2999 \* valid-looking on failure \*/

3000 \_dbus_message_real_iter_zero (real_sub);

3001

3002 \_dbus_return_val_if_fail (\_dbus_message_iter_append_check (real), FALSE);

3003 \_dbus_return_val_if_fail (real-\>iter_type == DBUS_MESSAGE_ITER_TYPE_WRITER, FALSE);

3004 \_dbus_return_val_if_fail (dbus_type_is_container (type), FALSE);

3005 \_dbus_return_val_if_fail ((type == DBUS_TYPE_STRUCT &&

3006 contained_signature == NULL) \|\|

3007 (type == DBUS_TYPE_DICT_ENTRY &&

3008 contained_signature == NULL) \|\|

3009 (type == DBUS_TYPE_VARIANT &&

3010 contained_signature != NULL) \|\|

3011 (type == DBUS_TYPE_ARRAY &&

3012 contained_signature != NULL), FALSE);

3013

3014 /\* this would fail if the contained_signature is a dict entry, since

3015 \* dict entries are invalid signatures standalone (they must be in

3016 \* an array)

3017 \*/

3018 if (contained_signature != NULL)

3019 {

3020 \_dbus_string_init_const (&contained_str, contained_signature);

3021 contained_signature_validity = \_dbus_validate_signature_with_reason (&contained_str,

3022 0,

3023 \_dbus_string_get_length (&contained_str));

3024

3025 if (contained_signature_validity == DBUS_VALIDITY_UNKNOWN_OOM_ERROR)

3026 return FALSE;

3027 }

3028 else

3029 {

3030 /\* just some placeholder value \*/

3031 contained_signature_validity = DBUS_VALID_BUT_INCOMPLETE;

3032 }

3033

3034 \_dbus_return_val_if_fail ((type == DBUS_TYPE_ARRAY && contained_signature && \*contained_signature == DBUS_DICT_ENTRY_BEGIN_CHAR) \|\|

3035 contained_signature == NULL \|\|

3036 contained_signature_validity == DBUS_VALID,

3037 FALSE);

3038

3039 if (!\_dbus_message_iter_open_signature (real))

3040 return FALSE;

3041

3042 ret = FALSE;

3043 \*real_sub = \*real;

3044

3045 if (contained_signature != NULL)

3046 {

3047 \_dbus_string_init_const (&contained_str, contained_signature);

3048

3049 ret = \_dbus_type_writer_recurse (&real-\>u.writer,

3050 type,

3051 &contained_str, 0,

3052 &real_sub-\>u.writer);

3053 }

3054 else

3055 {

3056 ret = \_dbus_type_writer_recurse (&real-\>u.writer,

3057 type,

3058 NULL, 0,

3059 &real_sub-\>u.writer);

3060 }

3061

3062 if (!ret)

3063 \_dbus_message_iter_abandon_signature (real);

3064

3065 return ret;

3066}

3067

3068

3088dbus_bool_t

3089dbus_message_iter_close_container (DBusMessageIter \*iter,

3090 DBusMessageIter \*sub)

3091{

3092 DBusMessageRealIter \*real = (DBusMessageRealIter \*)iter;

3093 DBusMessageRealIter \*real_sub = (DBusMessageRealIter \*)sub;

3094 dbus_bool_t ret;

3095

3096 \_dbus_return_val_if_fail (\_dbus_message_iter_append_check (real), FALSE);

3097 \_dbus_return_val_if_fail (real-\>iter_type == DBUS_MESSAGE_ITER_TYPE_WRITER, FALSE);

3098 \_dbus_return_val_if_fail (\_dbus_message_iter_append_check (real_sub), FALSE);

3099 \_dbus_return_val_if_fail (real_sub-\>iter_type == DBUS_MESSAGE_ITER_TYPE_WRITER, FALSE);

3100

3101 ret = \_dbus_type_writer_unrecurse (&real-\>u.writer,

3102 &real_sub-\>u.writer);

3103 \_dbus_message_real_iter_zero (real_sub);

3104

3105 if (!\_dbus_message_iter_close_signature (real))

3106 ret = FALSE;

3107

3108 return ret;

3109}

3110

3122void

3123dbus_message_iter_abandon_container (DBusMessageIter \*iter,

3124 DBusMessageIter \*sub)

3125{

3126 DBusMessageRealIter \*real = (DBusMessageRealIter \*)iter;

3127 DBusMessageRealIter \*real_sub = (DBusMessageRealIter \*)sub;

3128

3129\#ifndef DBUS_DISABLE_CHECKS

3130 \_dbus_return_if_fail (\_dbus_message_iter_append_check (real));

3131 \_dbus_return_if_fail (real-\>iter_type == DBUS_MESSAGE_ITER_TYPE_WRITER);

3132 \_dbus_return_if_fail (\_dbus_message_iter_append_check (real_sub));

3133 \_dbus_return_if_fail (real_sub-\>iter_type == DBUS_MESSAGE_ITER_TYPE_WRITER);

3134\#endif

3135

3136 \_dbus_message_iter_abandon_signature (real);

3137 \_dbus_message_real_iter_zero (real_sub);

3138}

3139

3181void

3182dbus_message_iter_abandon_container_if_open (DBusMessageIter \*iter,

3183 DBusMessageIter \*sub)

3184{

3185 DBusMessageRealIter \*real = (DBusMessageRealIter \*)iter;

3186 DBusMessageRealIter \*real_sub = (DBusMessageRealIter \*)sub;

3187

3188 /\* If both the parent and the child are zeroed out, then either we didn't

3189 \* even get as far as successfully recursing into the parent, or we already

3190 \* closed both the child and the parent. For example, in the code sample

3191 \* in the doc-comment above, this happens for

3192 \* abandon_container_if_open (&outer, &inner) if the first open_container

3193 \* call failed, or if we reached result = TRUE and fell through. \*/

3194 if (\_dbus_message_real_iter_is_zeroed (real) &&

3195 \_dbus_message_real_iter_is_zeroed (real_sub))

3196 return;

3197

3198\#ifndef DBUS_DISABLE_CHECKS

3199 /\* If the child is not zeroed out, but the parent is, then something has

3200 \* gone horribly wrong (in practice that would probably mean both are

3201 \* uninitialized or corrupt, and the parent happens to have ended up

3202 \* all-bytes-zero). \*/

3203 \_dbus_return_if_fail (\_dbus_message_iter_append_check (real));

3204 \_dbus_return_if_fail (real-\>iter_type == DBUS_MESSAGE_ITER_TYPE_WRITER);

3205\#endif

3206

3207 /\* If the parent is not zeroed out, but the child is, then either we did

3208 \* not successfully open the child, or we already closed the child. This

3209 \* means we do not own a reference to the parent's signature, so it would

3210 \* be wrong to release it; so we must not call abandon_signature() here.

3211 \* In the code sample in the doc-comment above, this happens for

3212 \* abandon_container_if_open (&outer, &inner) if the second open_container

3213 \* call failed, or if the second close_container call failed. \*/

3214 if (\_dbus_message_real_iter_is_zeroed (real_sub))

3215 return;

3216

3217\#ifndef DBUS_DISABLE_CHECKS

3218 \_dbus_return_if_fail (\_dbus_message_iter_append_check (real_sub));

3219 \_dbus_return_if_fail (real_sub-\>iter_type == DBUS_MESSAGE_ITER_TYPE_WRITER);

3220\#endif

3221

3222 /\* If neither the parent nor the child is zeroed out, then we genuinely

3223 \* have an open container; close it. In the code sample in the doc-comment,

3224 \* this happens for abandon_container_if_open (&outer, &inner) if the

3225 \* append_basic call failed. \*/

3226 \_dbus_message_iter_abandon_signature (real);

3227 \_dbus_message_real_iter_zero (real_sub);

3228}

3229

3246void

3247dbus_message_set_no_reply (DBusMessage \*message,

3248 dbus_bool_t no_reply)

3249{

3250 \_dbus_return_if_fail (message != NULL);

3251 \_dbus_return_if_fail (!message-\>locked);

3252

3253 \_dbus_header_toggle_flag (&message-\>header,

3254 DBUS_HEADER_FLAG_NO_REPLY_EXPECTED,

3255 no_reply);

3256}

3257

3265dbus_bool_t

3266dbus_message_get_no_reply (DBusMessage \*message)

3267{

3268 \_dbus_return_val_if_fail (message != NULL, FALSE);

3269

3270 return \_dbus_header_get_flag (&message-\>header,

3271 DBUS_HEADER_FLAG_NO_REPLY_EXPECTED);

3272}

3273

3288void

3289dbus_message_set_auto_start (DBusMessage \*message,

3290 dbus_bool_t auto_start)

3291{

3292 \_dbus_return_if_fail (message != NULL);

3293 \_dbus_return_if_fail (!message-\>locked);

3294

3295 \_dbus_header_toggle_flag (&message-\>header,

3296 DBUS_HEADER_FLAG_NO_AUTO_START,

3297 !auto_start);

3298}

3299

3307dbus_bool_t

3308dbus_message_get_auto_start (DBusMessage \*message)

3309{

3310 \_dbus_return_val_if_fail (message != NULL, FALSE);

3311

3312 return !\_dbus_header_get_flag (&message-\>header,

3313 DBUS_HEADER_FLAG_NO_AUTO_START);

3314}

3315

3316

3329dbus_bool_t

3330dbus_message_set_path (DBusMessage \*message,

3331 const char \*object_path)

3332{

3333 \_dbus_return_val_if_fail (message != NULL, FALSE);

3334 \_dbus_return_val_if_fail (!message-\>locked, FALSE);

3335 \_dbus_return_val_if_fail (object_path == NULL \|\|

3336 \_dbus_check_is_valid_path (object_path),

3337 FALSE);

3338

3339 return set_or_delete_string_field (message,

3340 DBUS_HEADER_FIELD_PATH,

3341 DBUS_TYPE_OBJECT_PATH,

3342 object_path);

3343}

3344

3358const char\*

3359dbus_message_get_path (DBusMessage \*message)

3360{

3361 const char \*v;

3362

3363 \_dbus_return_val_if_fail (message != NULL, NULL);

3364

3365 v = NULL; /\* in case field doesn't exist \*/

3366 \_dbus_header_get_field_basic (&message-\>header,

3367 DBUS_HEADER_FIELD_PATH,

3368 DBUS_TYPE_OBJECT_PATH,

3369 (void \*) &v);

3370 return v;

3371}

3372

3382dbus_bool_t

3383dbus_message_has_path (DBusMessage \*message,

3384 const char \*path)

3385{

3386 const char \*msg_path;

3387 msg_path = dbus_message_get_path (message);

3388

3389 if (msg_path == NULL)

3390 {

3391 if (path == NULL)

3392 return TRUE;

3393 else

3394 return FALSE;

3395 }

3396

3397 if (path == NULL)

3398 return FALSE;

3399

3400 if (strcmp (msg_path, path) == 0)

3401 return TRUE;

3402

3403 return FALSE;

3404}

3405

3426dbus_bool_t

3427dbus_message_get_path_decomposed (DBusMessage \*message,

3428 char \*\*\*path)

3429{

3430 const char \*v;

3431

3432 \_dbus_return_val_if_fail (message != NULL, FALSE);

3433 \_dbus_return_val_if_fail (path != NULL, FALSE);

3434

3435 \*path = NULL;

3436

3437 v = dbus_message_get_path (message);

3438 if (v != NULL)

3439 {

3440 if (!\_dbus_decompose_path (v, strlen (v),

3441 path, NULL))

3442 return FALSE;

3443 }

3444 return TRUE;

3445}

3446

3460dbus_bool_t

3461dbus_message_set_interface (DBusMessage \*message,

3462 const char \*iface)

3463{

3464 \_dbus_return_val_if_fail (message != NULL, FALSE);

3465 \_dbus_return_val_if_fail (!message-\>locked, FALSE);

3466 \_dbus_return_val_if_fail (iface == NULL \|\|

3467 \_dbus_check_is_valid_interface (iface),

3468 FALSE);

3469

3470 return set_or_delete_string_field (message,

3471 DBUS_HEADER_FIELD_INTERFACE,

3472 DBUS_TYPE_STRING,

3473 iface);

3474}

3475

3489const char\*

3490dbus_message_get_interface (DBusMessage \*message)

3491{

3492 const char \*v;

3493

3494 \_dbus_return_val_if_fail (message != NULL, NULL);

3495

3496 v = NULL; /\* in case field doesn't exist \*/

3497 \_dbus_header_get_field_basic (&message-\>header,

3498 DBUS_HEADER_FIELD_INTERFACE,

3499 DBUS_TYPE_STRING,

3500 (void \*) &v);

3501 return v;

3502}

3503

3511dbus_bool_t

3512dbus_message_has_interface (DBusMessage \*message,

3513 const char \*iface)

3514{

3515 const char \*msg_interface;

3516 msg_interface = dbus_message_get_interface (message);

3517

3518 if (msg_interface == NULL)

3519 {

3520 if (iface == NULL)

3521 return TRUE;

3522 else

3523 return FALSE;

3524 }

3525

3526 if (iface == NULL)

3527 return FALSE;

3528

3529 if (strcmp (msg_interface, iface) == 0)

3530 return TRUE;

3531

3532 return FALSE;

3533

3534}

3535

3548dbus_bool_t

3549dbus_message_set_member (DBusMessage \*message,

3550 const char \*member)

3551{

3552 \_dbus_return_val_if_fail (message != NULL, FALSE);

3553 \_dbus_return_val_if_fail (!message-\>locked, FALSE);

3554 \_dbus_return_val_if_fail (member == NULL \|\|

3555 \_dbus_check_is_valid_member (member),

3556 FALSE);

3557

3558 return set_or_delete_string_field (message,

3559 DBUS_HEADER_FIELD_MEMBER,

3560 DBUS_TYPE_STRING,

3561 member);

3562}

3563

3575const char\*

3576dbus_message_get_member (DBusMessage \*message)

3577{

3578 const char \*v;

3579

3580 \_dbus_return_val_if_fail (message != NULL, NULL);

3581

3582 v = NULL; /\* in case field doesn't exist \*/

3583 \_dbus_header_get_field_basic (&message-\>header,

3584 DBUS_HEADER_FIELD_MEMBER,

3585 DBUS_TYPE_STRING,

3586 (void \*) &v);

3587 return v;

3588}

3589

3597dbus_bool_t

3598dbus_message_has_member (DBusMessage \*message,

3599 const char \*member)

3600{

3601 const char \*msg_member;

3602 msg_member = dbus_message_get_member (message);

3603

3604 if (msg_member == NULL)

3605 {

3606 if (member == NULL)

3607 return TRUE;

3608 else

3609 return FALSE;

3610 }

3611

3612 if (member == NULL)

3613 return FALSE;

3614

3615 if (strcmp (msg_member, member) == 0)

3616 return TRUE;

3617

3618 return FALSE;

3619

3620}

3621

3633dbus_bool_t

3634dbus_message_set_error_name (DBusMessage \*message,

3635 const char \*error_name)

3636{

3637 \_dbus_return_val_if_fail (message != NULL, FALSE);

3638 \_dbus_return_val_if_fail (!message-\>locked, FALSE);

3639 \_dbus_return_val_if_fail (error_name == NULL \|\|

3640 \_dbus_check_is_valid_error_name (error_name),

3641 FALSE);

3642

3643 return set_or_delete_string_field (message,

3644 DBUS_HEADER_FIELD_ERROR_NAME,

3645 DBUS_TYPE_STRING,

3646 error_name);

3647}

3648

3659const char\*

3660dbus_message_get_error_name (DBusMessage \*message)

3661{

3662 const char \*v;

3663

3664 \_dbus_return_val_if_fail (message != NULL, NULL);

3665

3666 v = NULL; /\* in case field doesn't exist \*/

3667 \_dbus_header_get_field_basic (&message-\>header,

3668 DBUS_HEADER_FIELD_ERROR_NAME,

3669 DBUS_TYPE_STRING,

3670 (void \*) &v);

3671 return v;

3672}

3673

3687dbus_bool_t

3688dbus_message_set_destination (DBusMessage \*message,

3689 const char \*destination)

3690{

3691 \_dbus_return_val_if_fail (message != NULL, FALSE);

3692 \_dbus_return_val_if_fail (!message-\>locked, FALSE);

3693 \_dbus_return_val_if_fail (destination == NULL \|\|

3694 \_dbus_check_is_valid_bus_name (destination),

3695 FALSE);

3696

3697 return set_or_delete_string_field (message,

3698 DBUS_HEADER_FIELD_DESTINATION,

3699 DBUS_TYPE_STRING,

3700 destination);

3701}

3702

3712const char\*

3713dbus_message_get_destination (DBusMessage \*message)

3714{

3715 const char \*v;

3716

3717 \_dbus_return_val_if_fail (message != NULL, NULL);

3718

3719 v = NULL; /\* in case field doesn't exist \*/

3720 \_dbus_header_get_field_basic (&message-\>header,

3721 DBUS_HEADER_FIELD_DESTINATION,

3722 DBUS_TYPE_STRING,

3723 (void \*) &v);

3724 return v;

3725}

3726

3741dbus_bool_t

3742dbus_message_set_sender (DBusMessage \*message,

3743 const char \*sender)

3744{

3745 \_dbus_return_val_if_fail (message != NULL, FALSE);

3746 \_dbus_return_val_if_fail (!message-\>locked, FALSE);

3747 \_dbus_return_val_if_fail (sender == NULL \|\|

3748 \_dbus_check_is_valid_bus_name (sender),

3749 FALSE);

3750

3751 return set_or_delete_string_field (message,

3752 DBUS_HEADER_FIELD_SENDER,

3753 DBUS_TYPE_STRING,

3754 sender);

3755}

3756

3772const char\*

3773dbus_message_get_sender (DBusMessage \*message)

3774{

3775 const char \*v;

3776

3777 \_dbus_return_val_if_fail (message != NULL, NULL);

3778

3779 v = NULL; /\* in case field doesn't exist \*/

3780 \_dbus_header_get_field_basic (&message-\>header,

3781 DBUS_HEADER_FIELD_SENDER,

3782 DBUS_TYPE_STRING,

3783 (void \*) &v);

3784 return v;

3785}

3786

3805const char\*

3806dbus_message_get_signature (DBusMessage \*message)

3807{

3808 const DBusString \*type_str;

3809 int type_pos;

3810

3811 \_dbus_return_val_if_fail (message != NULL, NULL);

3812

3813 get_const_signature (&message-\>header, &type_str, &type_pos);

3814

3815 return \_dbus_string_get_const_data_len (type_str, type_pos, 0);

3816}

3817

3818static dbus_bool_t

3819\_dbus_message_has_type_interface_member (DBusMessage \*message,

3820 int type,

3821 const char \*iface,

3822 const char \*member)

3823{

3824 const char \*n;

3825

3826 \_dbus_assert (message != NULL);

3827 \_dbus_assert (iface != NULL);

3828 \_dbus_assert (member != NULL);

3829

3830 if (dbus_message_get_type (message) != type)

3831 return FALSE;

3832

3833 /\* Optimize by checking the short member name first

3834 \* instead of the longer interface name

3835 \*/

3836

3837 n = dbus_message_get_member (message);

3838

3839 if (n && strcmp (n, member) == 0)

3840 {

3841 n = dbus_message_get_interface (message);

3842

3843 if (n == NULL \|\| strcmp (n, iface) == 0)

3844 return TRUE;

3845 }

3846

3847 return FALSE;

3848}

3849

3864dbus_bool_t

3865dbus_message_is_method_call (DBusMessage \*message,

3866 const char \*iface,

3867 const char \*method)

3868{

3869 \_dbus_return_val_if_fail (message != NULL, FALSE);

3870 \_dbus_return_val_if_fail (iface != NULL, FALSE);

3871 \_dbus_return_val_if_fail (method != NULL, FALSE);

3872 /\* don't check that interface/method are valid since it would be

3873 \* expensive, and not catch many common errors

3874 \*/

3875

3876 return \_dbus_message_has_type_interface_member (message,

3877 DBUS_MESSAGE_TYPE_METHOD_CALL,

3878 iface, method);

3879}

3880

3892dbus_bool_t

3893dbus_message_is_signal (DBusMessage \*message,

3894 const char \*iface,

3895 const char \*signal_name)

3896{

3897 \_dbus_return_val_if_fail (message != NULL, FALSE);

3898 \_dbus_return_val_if_fail (iface != NULL, FALSE);

3899 \_dbus_return_val_if_fail (signal_name != NULL, FALSE);

3900 /\* don't check that interface/name are valid since it would be

3901 \* expensive, and not catch many common errors

3902 \*/

3903

3904 return \_dbus_message_has_type_interface_member (message,

3905 DBUS_MESSAGE_TYPE_SIGNAL,

3906 iface, signal_name);

3907}

3908

3919dbus_bool_t

3920dbus_message_is_error (DBusMessage \*message,

3921 const char \*error_name)

3922{

3923 const char \*n;

3924

3925 \_dbus_return_val_if_fail (message != NULL, FALSE);

3926 \_dbus_return_val_if_fail (error_name != NULL, FALSE);

3927 /\* don't check that error_name is valid since it would be expensive,

3928 \* and not catch many common errors

3929 \*/

3930

3931 if (dbus_message_get_type (message) != DBUS_MESSAGE_TYPE_ERROR)

3932 return FALSE;

3933

3934 n = dbus_message_get_error_name (message);

3935

3936 if (n && strcmp (n, error_name) == 0)

3937 return TRUE;

3938 else

3939 return FALSE;

3940}

3941

3952dbus_bool_t

3953dbus_message_has_destination (DBusMessage \*message,

3954 const char \*name)

3955{

3956 const char \*s;

3957

3958 \_dbus_return_val_if_fail (message != NULL, FALSE);

3959 \_dbus_return_val_if_fail (name != NULL, FALSE);

3960 /\* don't check that name is valid since it would be expensive, and

3961 \* not catch many common errors

3962 \*/

3963

3964 s = dbus_message_get_destination (message);

3965

3966 if (s && strcmp (s, name) == 0)

3967 return TRUE;

3968 else

3969 return FALSE;

3970}

3971

3987dbus_bool_t

3988dbus_message_has_sender (DBusMessage \*message,

3989 const char \*name)

3990{

3991 const char \*s;

3992

3993 \_dbus_return_val_if_fail (message != NULL, FALSE);

3994 \_dbus_return_val_if_fail (name != NULL, FALSE);

3995 /\* don't check that name is valid since it would be expensive, and

3996 \* not catch many common errors

3997 \*/

3998

3999 s = dbus_message_get_sender (message);

4000

4001 if (s && strcmp (s, name) == 0)

4002 return TRUE;

4003 else

4004 return FALSE;

4005}

4006

4016dbus_bool_t

4017dbus_message_has_signature (DBusMessage \*message,

4018 const char \*signature)

4019{

4020 const char \*s;

4021

4022 \_dbus_return_val_if_fail (message != NULL, FALSE);

4023 \_dbus_return_val_if_fail (signature != NULL, FALSE);

4024 /\* don't check that signature is valid since it would be expensive,

4025 \* and not catch many common errors

4026 \*/

4027

4028 s = dbus_message_get_signature (message);

4029

4030 if (s && strcmp (s, signature) == 0)

4031 return TRUE;

4032 else

4033 return FALSE;

4034}

4035

4058dbus_bool_t

4059dbus_set_error_from_message (DBusError \*error,

4060 DBusMessage \*message)

4061{

4062 const char \*str;

4063

4064 \_dbus_return_val_if_fail (message != NULL, FALSE);

4065 \_dbus_return_val_if_error_is_set (error, FALSE);

4066

4067 if (dbus_message_get_type (message) != DBUS_MESSAGE_TYPE_ERROR)

4068 return FALSE;

4069

4070 str = NULL;

4071 dbus_message_get_args (message, NULL,

4072 DBUS_TYPE_STRING, &str,

4073 DBUS_TYPE_INVALID);

4074

4075 dbus_set_error (error, dbus_message_get_error_name (message),

4076 str ? "%s" : NULL, str);

4077

4078 return TRUE;

4079}

4080

4087dbus_bool_t

4088dbus_message_contains_unix_fds(DBusMessage \*message)

4089{

4090\#ifdef HAVE_UNIX_FD_PASSING

4091 \_dbus_assert(message);

4092

4093 return message-\>n_unix_fds \> 0;

4094\#else

4095 return FALSE;

4096\#endif

4097}

4098

4109dbus_bool_t

4110dbus_message_set_container_instance (DBusMessage \*message,

4111 const char \*object_path)

4112{

4113 \_dbus_return_val_if_fail (message != NULL, FALSE);

4114 \_dbus_return_val_if_fail (!message-\>locked, FALSE);

4115 \_dbus_return_val_if_fail (object_path == NULL \|\|

4116 \_dbus_check_is_valid_path (object_path),

4117 FALSE);

4118

4119 return set_or_delete_string_field (message,

4120 DBUS_HEADER_FIELD_CONTAINER_INSTANCE,

4121 DBUS_TYPE_OBJECT_PATH,

4122 object_path);

4123}

4124

4135const char \*

4136dbus_message_get_container_instance (DBusMessage \*message)

4137{

4138 const char \*v;

4139

4140 \_dbus_return_val_if_fail (message != NULL, NULL);

4141

4142 v = NULL; /\* in case field doesn't exist \*/

4143 \_dbus_header_get_field_basic (&message-\>header,

4144 DBUS_HEADER_FIELD_CONTAINER_INSTANCE,

4145 DBUS_TYPE_OBJECT_PATH,

4146 (void \*) &v);

4147 return v;

4148}

4149

4168\#define INITIAL_LOADER_DATA_LEN 32

4169

4176DBusMessageLoader\*

4177\_dbus_message_loader_new (void)

4178{

4179 DBusMessageLoader \*loader;

4180

4181 loader = dbus_new0 (DBusMessageLoader, 1);

4182 if (loader == NULL)

4183 return NULL;

4184

4185 loader-\>refcount = 1;

4186

4187 loader-\>corrupted = FALSE;

4188 loader-\>corruption_reason = DBUS_VALID;

4189

4190 /\* this can be configured by the app, but defaults to the protocol max \*/

4191 loader-\>max_message_size = DBUS_MAXIMUM_MESSAGE_LENGTH;

4192

4193 /\* We set a very relatively conservative default here since due to how

4194 SCM_RIGHTS works we need to preallocate an fd array of the maximum

4195 number of unix fds we want to receive in advance. A

4196 try-and-reallocate loop is not possible. \*/

4197 loader-\>max_message_unix_fds = DBUS_DEFAULT_MESSAGE_UNIX_FDS;

4198

4199 if (!\_dbus_string_init (&loader-\>data))

4200 {

4201 dbus_free (loader);

4202 return NULL;

4203 }

4204

4205 /\* preallocate the buffer for speed, ignore failure \*/

4206 \_dbus_string_set_length (&loader-\>data, INITIAL_LOADER_DATA_LEN);

4207 \_dbus_string_set_length (&loader-\>data, 0);

4208

4209\#ifdef HAVE_UNIX_FD_PASSING

4210 loader-\>unix_fds = NULL;

4211 loader-\>n_unix_fds = loader-\>n_unix_fds_allocated = 0;

4212 loader-\>unix_fds_outstanding = FALSE;

4213\#endif

4214

4215 return loader;

4216}

4217

4224DBusMessageLoader \*

4225\_dbus_message_loader_ref (DBusMessageLoader \*loader)

4226{

4227 loader-\>refcount += 1;

4228

4229 return loader;

4230}

4231

4238void

4239\_dbus_message_loader_unref (DBusMessageLoader \*loader)

4240{

4241 loader-\>refcount -= 1;

4242 if (loader-\>refcount == 0)

4243 {

4244\#ifdef HAVE_UNIX_FD_PASSING

4245 close_unix_fds(loader-\>unix_fds, &loader-\>n_unix_fds);

4246 dbus_free(loader-\>unix_fds);

4247\#endif

4248 \_dbus_list_clear_full (&loader-\>messages,

4249 (DBusFreeFunction) dbus_message_unref);

4250 \_dbus_string_free (&loader-\>data);

4251 dbus_free (loader);

4252 }

4253}

4254

4273void

4274\_dbus_message_loader_get_buffer (DBusMessageLoader \*loader,

4275 DBusString \*\*buffer,

4276 int \*max_to_read,

4277 dbus_bool_t \*may_read_fds)

4278{

4279 \_dbus_assert (!loader-\>buffer_outstanding);

4280

4281 \*buffer = &loader-\>data;

4282

4283 loader-\>buffer_outstanding = TRUE;

4284

4285 if (max_to_read != NULL)

4286 {

4287\#ifdef HAVE_UNIX_FD_PASSING

4288 int offset = 0;

4289 int remain;

4290 int byte_order;

4291 int fields_array_len;

4292 int header_len;

4293 int body_len;

4294\#endif

4295

4296 \*max_to_read = DBUS_MAXIMUM_MESSAGE_LENGTH;

4297 \*may_read_fds = TRUE;

4298

4299\#ifdef HAVE_UNIX_FD_PASSING

4300 /\* If we aren't holding onto any fds, we can read as much as we want

4301 \* (fast path). \*/

4302 if (loader-\>n_unix_fds == 0)

4303 return;

4304

4305 /\* Slow path: we have a message with some fds in it. We don't want

4306 \* to start on the next message until this one is out of the way;

4307 \* otherwise a legitimate sender can keep us processing messages

4308 \* containing fds, until we disconnect it for having had fds pending

4309 \* for too long, a limit that is in place to stop malicious senders

4310 \* from setting up recursive fd-passing that takes up our quota and

4311 \* will never go away. \*/

4312

4313 remain = \_dbus_string_get_length (&loader-\>data);

4314

4315 while (remain \> 0)

4316 {

4317 DBusValidity validity = DBUS_VALIDITY_UNKNOWN;

4318 int needed;

4319

4320 /\* If 0 \< remain \< DBUS_MINIMUM_HEADER_SIZE, then we've had at

4321 \* least the first byte of a message, but we don't know how

4322 \* much more to read. Only read the rest of the

4323 \* DBUS_MINIMUM_HEADER_SIZE for now; then we'll know. \*/

4324 if (remain \< DBUS_MINIMUM_HEADER_SIZE)

4325 {

4326 \*max_to_read = DBUS_MINIMUM_HEADER_SIZE - remain;

4327 \*may_read_fds = FALSE;

4328 return;

4329 }

4330

4331 if (!\_dbus_header_have_message_untrusted (loader-\>max_message_size,

4332 &validity,

4333 &byte_order,

4334 &fields_array_len,

4335 &header_len,

4336 &body_len,

4337 &loader-\>data,

4338 offset,

4339 remain))

4340 {

4341 /\* If a message in the buffer is invalid, we're going to

4342 \* disconnect the sender anyway, so reading an arbitrary amount

4343 \* is fine. \*/

4344 if (validity != DBUS_VALID)

4345 return;

4346

4347 /\* We have a partial message, with the

4348 \* DBUS_MINIMUM_HEADER_SIZE-byte fixed part of the header (which

4349 \* lets us work out how much more we need), but no more. Read

4350 \* the rest of the message. \*/

4351 needed = header_len + body_len;

4352 \_dbus_assert (needed \> remain);

4353 \*max_to_read = needed - remain;

4354 \*may_read_fds = FALSE;

4355 return;

4356 }

4357

4358 /\* Skip over entire messages until we have less than a message

4359 \* remaining. \*/

4360 needed = header_len + body_len;

4361 \_dbus_assert (needed \> DBUS_MINIMUM_HEADER_SIZE);

4362 \_dbus_assert (remain \>= needed);

4363 remain -= needed;

4364 offset += needed;

4365 }

4366\#endif

4367 }

4368}

4369

4379void

4380\_dbus_message_loader_return_buffer (DBusMessageLoader \*loader,

4381 DBusString \*buffer)

4382{

4383 \_dbus_assert (loader-\>buffer_outstanding);

4384 \_dbus_assert (buffer == &loader-\>data);

4385

4386 loader-\>buffer_outstanding = FALSE;

4387}

4388

4389\#ifdef HAVE_UNIX_FD_PASSING

4400dbus_bool_t

4401\_dbus_message_loader_get_unix_fds(DBusMessageLoader \*loader,

4402 int \*\*fds,

4403 unsigned \*max_n_fds)

4404{

4405 \_dbus_assert (!loader-\>unix_fds_outstanding);

4406

4407 /\* Allocate space where we can put the fds we read. We allocate

4408 space for max_message_unix_fds since this is an

4409 upper limit how many fds can be received within a single

4410 message. Since SCM_RIGHTS doesn't allow a reallocate+retry logic

4411 we are allocating the maximum possible array size right from the

4412 beginning. This sucks a bit, however unless SCM_RIGHTS is fixed

4413 there is no better way. \*/

4414

4415 if (loader-\>n_unix_fds_allocated \< loader-\>max_message_unix_fds)

4416 {

4417 int \*a = dbus_realloc(loader-\>unix_fds,

4418 loader-\>max_message_unix_fds \* sizeof(loader-\>unix_fds\[0\]));

4419

4420 if (!a)

4421 return FALSE;

4422

4423 loader-\>unix_fds = a;

4424 loader-\>n_unix_fds_allocated = loader-\>max_message_unix_fds;

4425 }

4426

4427 \*fds = loader-\>unix_fds + loader-\>n_unix_fds;

4428 \*max_n_fds = loader-\>n_unix_fds_allocated - loader-\>n_unix_fds;

4429

4430 loader-\>unix_fds_outstanding = TRUE;

4431 return TRUE;

4432}

4433

4444void

4445\_dbus_message_loader_return_unix_fds(DBusMessageLoader \*loader,

4446 int \*fds,

4447 unsigned n_fds)

4448{

4449 \_dbus_assert(loader-\>unix_fds_outstanding);

4450 \_dbus_assert(loader-\>unix_fds + loader-\>n_unix_fds == fds);

4451 \_dbus_assert(loader-\>n_unix_fds + n_fds \<= loader-\>n_unix_fds_allocated);

4452

4453 loader-\>n_unix_fds += n_fds;

4454 loader-\>unix_fds_outstanding = FALSE;

4455

4456 if (n_fds && loader-\>unix_fds_change)

4457 loader-\>unix_fds_change (loader-\>unix_fds_change_data);

4458}

4459\#endif

4460

4461/\*

4462 \* FIXME when we move the header out of the buffer, that memmoves all

4463 \* buffered messages. Kind of crappy.

4464 \*

4465 \* Also we copy the header and body, which is kind of crappy. To

4466 \* avoid this, we have to allow header and body to be in a single

4467 \* memory block, which is good for messages we read and bad for

4468 \* messages we are creating. But we could move_len() the buffer into

4469 \* this single memory block, and move_len() will just swap the buffers

4470 \* if you're moving the entire buffer replacing the dest string.

4471 \*

4472 \* We could also have the message loader tell the transport how many

4473 \* bytes to read; so it would first ask for some arbitrary number like

4474 \* 256, then if the message was incomplete it would use the

4475 \* header/body len to ask for exactly the size of the message (or

4476 \* blocks the size of a typical kernel buffer for the socket). That

4477 \* way we don't get trailing bytes in the buffer that have to be

4478 \* memmoved. Though I suppose we also don't have a chance of reading a

4479 \* bunch of small messages at once, so the optimization may be stupid.

4480 \*

4481 \* Another approach would be to keep a "start" index into

4482 \* loader-\>data and only delete it occasionally, instead of after

4483 \* each message is loaded.

4484 \*

4485 \* load_message() returns FALSE if not enough memory OR the loader was corrupted

4486 \*/

4487static dbus_bool_t

4488load_message (DBusMessageLoader \*loader,

4489 DBusMessage \*message,

4490 int byte_order,

4491 int fields_array_len,

4492 int header_len,

4493 int body_len)

4494{

4495 dbus_bool_t oom;

4496 DBusValidity validity;

4497 const DBusString \*type_str;

4498 int type_pos;

4499 DBusValidationMode mode;

4500 dbus_uint32_t n_unix_fds = 0;

4501

4502 mode = DBUS_VALIDATION_MODE_DATA_IS_UNTRUSTED;

4503

4504 oom = FALSE;

4505

4506\#if 0

4507 \_dbus_verbose_bytes_of_string (&loader-\>data, 0, header_len /\* + body_len \*/);

4508\#endif

4509

4510 /\* 1. VALIDATE AND COPY OVER HEADER \*/

4511 \_dbus_assert (\_dbus_string_get_length (&message-\>header.data) == 0);

4512 \_dbus_assert ((header_len + body_len) \<= \_dbus_string_get_length (&loader-\>data));

4513

4514 if (!\_dbus_header_load (&message-\>header,

4515 mode,

4516 &validity,

4517 byte_order,

4518 fields_array_len,

4519 header_len,

4520 body_len,

4521 &loader-\>data))

4522 {

4523 \_dbus_verbose ("Failed to load header for new message code %d\n", validity);

4524

4525 /\* assert here so we can catch any code that still uses DBUS_VALID to indicate

4526 oom errors. They should use DBUS_VALIDITY_UNKNOWN_OOM_ERROR instead \*/

4527 \_dbus_assert (validity != DBUS_VALID);

4528

4529 if (validity == DBUS_VALIDITY_UNKNOWN_OOM_ERROR)

4530 oom = TRUE;

4531 else

4532 {

4533 loader-\>corrupted = TRUE;

4534 loader-\>corruption_reason = validity;

4535 }

4536 goto failed;

4537 }

4538

4539 \_dbus_assert (validity == DBUS_VALID);

4540

4541 /\* 2. VALIDATE BODY \*/

4542 if (mode != DBUS_VALIDATION_MODE_WE_TRUST_THIS_DATA_ABSOLUTELY)

4543 {

4544 get_const_signature (&message-\>header, &type_str, &type_pos);

4545

4546 /\* Because the bytes_remaining arg is NULL, this validates that the

4547 \* body is the right length

4548 \*/

4549 validity = \_dbus_validate_body_with_reason (type_str,

4550 type_pos,

4551 byte_order,

4552 NULL,

4553 &loader-\>data,

4554 header_len,

4555 body_len);

4556 if (validity != DBUS_VALID)

4557 {

4558 \_dbus_verbose ("Failed to validate message body code %d\n", validity);

4559

4560 loader-\>corrupted = TRUE;

4561 loader-\>corruption_reason = validity;

4562

4563 goto failed;

4564 }

4565 }

4566

4567 /\* 3. COPY OVER UNIX FDS \*/

4568 \_dbus_header_get_field_basic(&message-\>header,

4569 DBUS_HEADER_FIELD_UNIX_FDS,

4570 DBUS_TYPE_UINT32,

4571 &n_unix_fds);

4572

4573\#ifdef HAVE_UNIX_FD_PASSING

4574

4575 if (n_unix_fds \> loader-\>n_unix_fds)

4576 {

4577 \_dbus_verbose("Message contains references to more unix fds than were sent %u != %u\n",

4578 n_unix_fds, loader-\>n_unix_fds);

4579

4580 loader-\>corrupted = TRUE;

4581 loader-\>corruption_reason = DBUS_INVALID_MISSING_UNIX_FDS;

4582 goto failed;

4583 }

4584

4585 /\* If this was a recycled message there might still be

4586 some memory allocated for the fds \*/

4587 dbus_free(message-\>unix_fds);

4588

4589 if (n_unix_fds \> 0)

4590 {

4591 message-\>unix_fds = \_dbus_memdup(loader-\>unix_fds, n_unix_fds \* sizeof(message-\>unix_fds\[0\]));

4592 if (message-\>unix_fds == NULL)

4593 {

4594 \_dbus_verbose ("Failed to allocate file descriptor array\n");

4595 oom = TRUE;

4596 goto failed;

4597 }

4598

4599 message-\>n_unix_fds_allocated = message-\>n_unix_fds = n_unix_fds;

4600 loader-\>n_unix_fds -= n_unix_fds;

4601 memmove (loader-\>unix_fds, loader-\>unix_fds + n_unix_fds, loader-\>n_unix_fds \* sizeof (loader-\>unix_fds\[0\]));

4602

4603 if (loader-\>unix_fds_change)

4604 loader-\>unix_fds_change (loader-\>unix_fds_change_data);

4605 }

4606 else

4607 message-\>unix_fds = NULL;

4608

4609\#else

4610

4611 if (n_unix_fds \> 0)

4612 {

4613 \_dbus_verbose ("Hmm, message claims to come with file descriptors "

4614 "but that's not supported on our platform, disconnecting.\n");

4615

4616 loader-\>corrupted = TRUE;

4617 loader-\>corruption_reason = DBUS_INVALID_MISSING_UNIX_FDS;

4618 goto failed;

4619 }

4620

4621\#endif

4622

4623 /\* 3. COPY OVER BODY AND QUEUE MESSAGE \*/

4624

4625 if (!\_dbus_list_append (&loader-\>messages, message))

4626 {

4627 \_dbus_verbose ("Failed to append new message to loader queue\n");

4628 oom = TRUE;

4629 goto failed;

4630 }

4631

4632 \_dbus_assert (\_dbus_string_get_length (&message-\>body) == 0);

4633 \_dbus_assert (\_dbus_string_get_length (&loader-\>data) \>=

4634 (header_len + body_len));

4635

4636 if (!\_dbus_string_copy_len (&loader-\>data, header_len, body_len, &message-\>body, 0))

4637 {

4638 \_dbus_verbose ("Failed to move body into new message\n");

4639 oom = TRUE;

4640 goto failed;

4641 }

4642

4643 \_dbus_string_delete (&loader-\>data, 0, header_len + body_len);

4644

4645 /\* don't waste more than 2k of memory \*/

4646 \_dbus_string_compact (&loader-\>data, 2048);

4647

4648 \_dbus_assert (\_dbus_string_get_length (&message-\>header.data) == header_len);

4649 \_dbus_assert (\_dbus_string_get_length (&message-\>body) == body_len);

4650

4651 \_dbus_verbose ("Loaded message %p\n", message);

4652

4653 \_dbus_assert (!oom);

4654 \_dbus_assert (!loader-\>corrupted);

4655 \_dbus_assert (loader-\>messages != NULL);

4656 \_dbus_assert (\_dbus_list_find_last (&loader-\>messages, message) != NULL);

4657

4658 return TRUE;

4659

4660 failed:

4661

4662 /\* Clean up \*/

4663

4664 /\* does nothing if the message isn't in the list \*/

4665 \_dbus_list_remove_last (&loader-\>messages, message);

4666

4667 if (oom)

4668 \_dbus_assert (!loader-\>corrupted);

4669 else

4670 \_dbus_assert (loader-\>corrupted);

4671

4672 \_dbus_verbose_bytes_of_string (&loader-\>data, 0, \_dbus_string_get_length (&loader-\>data));

4673

4674 return FALSE;

4675}

4676

4691dbus_bool_t

4692\_dbus_message_loader_queue_messages (DBusMessageLoader \*loader)

4693{

4694 while (!loader-\>corrupted &&

4695 \_dbus_string_get_length (&loader-\>data) \>= DBUS_MINIMUM_HEADER_SIZE)

4696 {

4697 DBusValidity validity;

4698 int byte_order, fields_array_len, header_len, body_len;

4699

4700 if (\_dbus_header_have_message_untrusted (loader-\>max_message_size,

4701 &validity,

4702 &byte_order,

4703 &fields_array_len,

4704 &header_len,

4705 &body_len,

4706 &loader-\>data, 0,

4707 \_dbus_string_get_length (&loader-\>data)))

4708 {

4709 DBusMessage \*message;

4710

4711 \_dbus_assert (validity == DBUS_VALID);

4712

4713 message = dbus_message_new_empty_header ();

4714 if (message == NULL)

4715 return FALSE;

4716

4717 if (!load_message (loader, message,

4718 byte_order, fields_array_len,

4719 header_len, body_len))

4720 {

4721 dbus_message_unref (message);

4722 /\* load_message() returns false if corrupted or OOM; if

4723 \* corrupted then return TRUE for not OOM

4724 \*/

4725 return loader-\>corrupted;

4726 }

4727

4728 \_dbus_assert (loader-\>messages != NULL);

4729 \_dbus_assert (\_dbus_list_find_last (&loader-\>messages, message) != NULL);

4730 }

4731 else

4732 {

4733 \_dbus_verbose ("Initial peek at header says we don't have a whole message yet, or data broken with invalid code %d\n",

4734 validity);

4735 if (validity != DBUS_VALID)

4736 {

4737 loader-\>corrupted = TRUE;

4738 loader-\>corruption_reason = validity;

4739 }

4740 return TRUE;

4741 }

4742 }

4743

4744 return TRUE;

4745}

4746

4754DBusMessage\*

4755\_dbus_message_loader_peek_message (DBusMessageLoader \*loader)

4756{

4757 if (loader-\>messages)

4758 return loader-\>messages-\>data;

4759 else

4760 return NULL;

4761}

4762

4771DBusMessage\*

4772\_dbus_message_loader_pop_message (DBusMessageLoader \*loader)

4773{

4774 return \_dbus_list_pop_first (&loader-\>messages);

4775}

4776

4785DBusList\*

4786\_dbus_message_loader_pop_message_link (DBusMessageLoader \*loader)

4787{

4788 return \_dbus_list_pop_first_link (&loader-\>messages);

4789}

4790

4797void

4798\_dbus_message_loader_putback_message_link (DBusMessageLoader \*loader,

4799 DBusList \*link)

4800{

4801 \_dbus_list_prepend_link (&loader-\>messages, link);

4802}

4803

4813dbus_bool_t

4814\_dbus_message_loader_get_is_corrupted (DBusMessageLoader \*loader)

4815{

4816 \_dbus_assert ((loader-\>corrupted && loader-\>corruption_reason != DBUS_VALID) \|\|

4817 (!loader-\>corrupted && loader-\>corruption_reason == DBUS_VALID));

4818 return loader-\>corrupted;

4819}

4820

4827DBusValidity

4828\_dbus_message_loader_get_corruption_reason (DBusMessageLoader \*loader)

4829{

4830 \_dbus_assert ((loader-\>corrupted && loader-\>corruption_reason != DBUS_VALID) \|\|

4831 (!loader-\>corrupted && loader-\>corruption_reason == DBUS_VALID));

4832

4833 return loader-\>corruption_reason;

4834}

4835

4842void

4843\_dbus_message_loader_set_max_message_size (DBusMessageLoader \*loader,

4844 long size)

4845{

4846 if (size \> DBUS_MAXIMUM_MESSAGE_LENGTH)

4847 {

4848 \_dbus_verbose ("clamping requested max message size %ld to %d\n",

4849 size, DBUS_MAXIMUM_MESSAGE_LENGTH);

4850 size = DBUS_MAXIMUM_MESSAGE_LENGTH;

4851 }

4852 loader-\>max_message_size = size;

4853}

4854

4861long

4862\_dbus_message_loader_get_max_message_size (DBusMessageLoader \*loader)

4863{

4864 return loader-\>max_message_size;

4865}

4866

4873void

4874\_dbus_message_loader_set_max_message_unix_fds (DBusMessageLoader \*loader,

4875 long n)

4876{

4877 if (n \> DBUS_MAXIMUM_MESSAGE_UNIX_FDS)

4878 {

4879 \_dbus_verbose ("clamping requested max message unix_fds %ld to %d\n",

4880 n, DBUS_MAXIMUM_MESSAGE_UNIX_FDS);

4881 n = DBUS_MAXIMUM_MESSAGE_UNIX_FDS;

4882 }

4883 loader-\>max_message_unix_fds = n;

4884}

4885

4892long

4893\_dbus_message_loader_get_max_message_unix_fds (DBusMessageLoader \*loader)

4894{

4895 return loader-\>max_message_unix_fds;

4896}

4897

4903int

4904\_dbus_message_loader_get_pending_fds_count (DBusMessageLoader \*loader)

4905{

4906\#ifdef HAVE_UNIX_FD_PASSING

4907 return loader-\>n_unix_fds;

4908\#else

4909 return 0;

4910\#endif

4911}

4912

4921void

4922\_dbus_message_loader_set_pending_fds_function (DBusMessageLoader \*loader,

4923 void (\* callback) (void \*),

4924 void \*data)

4925{

4926\#ifdef HAVE_UNIX_FD_PASSING

4927 loader-\>unix_fds_change = callback;

4928 loader-\>unix_fds_change_data = data;

4929\#endif

4930}

4931

4932static DBusDataSlotAllocator slot_allocator =

4933 \_DBUS_DATA_SLOT_ALLOCATOR_INIT (\_DBUS_LOCK_NAME (message_slots));

4934

4949dbus_bool_t

4950dbus_message_allocate_data_slot (dbus_int32_t \*slot_p)

4951{

4952 return \_dbus_data_slot_allocator_alloc (&slot_allocator,

4953 slot_p);

4954}

4955

4967void

4968dbus_message_free_data_slot (dbus_int32_t \*slot_p)

4969{

4970 \_dbus_return_if_fail (\*slot_p \>= 0);

4971

4972 \_dbus_data_slot_allocator_free (&slot_allocator, slot_p);

4973}

4974

4988dbus_bool_t

4989dbus_message_set_data (DBusMessage \*message,

4990 dbus_int32_t slot,

4991 void \*data,

4992 DBusFreeFunction free_data_func)

4993{

4994 DBusFreeFunction old_free_func;

4995 void \*old_data;

4996 dbus_bool_t retval;

4997

4998 \_dbus_return_val_if_fail (message != NULL, FALSE);

4999 \_dbus_return_val_if_fail (slot \>= 0, FALSE);

5000

5001 retval = \_dbus_data_slot_list_set (&slot_allocator,

5002 &message-\>slot_list,

5003 slot, data, free_data_func,

5004 &old_free_func, &old_data);

5005

5006 if (retval)

5007 {

5008 /\* Do the actual free outside the message lock \*/

5009 if (old_free_func)

5010 (\* old_free_func) (old_data);

5011 }

5012

5013 return retval;

5014}

5015

5024void\*

5025dbus_message_get_data (DBusMessage \*message,

5026 dbus_int32_t slot)

5027{

5028 void \*res;

5029

5030 \_dbus_return_val_if_fail (message != NULL, NULL);

5031

5032 res = \_dbus_data_slot_list_get (&slot_allocator,

5033 &message-\>slot_list,

5034 slot);

5035

5036 return res;

5037}

5038

5052int

5053dbus_message_type_from_string (const char \*type_str)

5054{

5055 if (strcmp (type_str, "method_call") == 0)

5056 return DBUS_MESSAGE_TYPE_METHOD_CALL;

5057 if (strcmp (type_str, "method_return") == 0)

5058 return DBUS_MESSAGE_TYPE_METHOD_RETURN;

5059 else if (strcmp (type_str, "signal") == 0)

5060 return DBUS_MESSAGE_TYPE_SIGNAL;

5061 else if (strcmp (type_str, "error") == 0)

5062 return DBUS_MESSAGE_TYPE_ERROR;

5063 else

5064 return DBUS_MESSAGE_TYPE_INVALID;

5065}

5066

5080const char \*

5081dbus_message_type_to_string (int type)

5082{

5083 switch (type)

5084 {

5085 case DBUS_MESSAGE_TYPE_METHOD_CALL:

5086 return "method_call";

5087 case DBUS_MESSAGE_TYPE_METHOD_RETURN:

5088 return "method_return";

5089 case DBUS_MESSAGE_TYPE_SIGNAL:

5090 return "signal";

5091 case DBUS_MESSAGE_TYPE_ERROR:

5092 return "error";

5093 default:

5094 return "invalid";

5095 }

5096}

5097

5110dbus_bool_t

5111dbus_message_marshal (DBusMessage \*msg,

5112 char \*\*marshalled_data_p,

5113 int \*len_p)

5114{

5115 DBusString tmp;

5116 dbus_bool_t was_locked;

5117

5118 \_dbus_return_val_if_fail (msg != NULL, FALSE);

5119 \_dbus_return_val_if_fail (marshalled_data_p != NULL, FALSE);

5120 \_dbus_return_val_if_fail (len_p != NULL, FALSE);

5121

5122 if (!\_dbus_string_init (&tmp))

5123 return FALSE;

5124

5125 /\* Ensure the message is locked, to ensure the length header is filled in. \*/

5126 was_locked = msg-\>locked;

5127

5128 if (!was_locked)

5129 dbus_message_lock (msg);

5130

5131 if (!\_dbus_string_copy (&(msg-\>header.data), 0, &tmp, 0))

5132 goto fail;

5133

5134 \*len_p = \_dbus_string_get_length (&tmp);

5135

5136 if (!\_dbus_string_copy (&(msg-\>body), 0, &tmp, \*len_p))

5137 goto fail;

5138

5139 \*len_p = \_dbus_string_get_length (&tmp);

5140

5141 if (!\_dbus_string_steal_data (&tmp, marshalled_data_p))

5142 goto fail;

5143

5144 \_dbus_string_free (&tmp);

5145

5146 if (!was_locked)

5147 msg-\>locked = FALSE;

5148

5149 return TRUE;

5150

5151 fail:

5152 \_dbus_string_free (&tmp);

5153

5154 if (!was_locked)

5155 msg-\>locked = FALSE;

5156

5157 return FALSE;

5158}

5159

5172DBusMessage \*

5173dbus_message_demarshal (const char \*str,

5174 int len,

5175 DBusError \*error)

5176{

5177 DBusMessageLoader \*loader = NULL;

5178 DBusString \*buffer;

5179 DBusMessage \*msg;

5180

5181 \_dbus_return_val_if_fail (str != NULL, NULL);

5182

5183 loader = \_dbus_message_loader_new ();

5184

5185 if (loader == NULL)

5186 goto fail_oom;

5187

5188 \_dbus_message_loader_get_buffer (loader, &buffer, NULL, NULL);

5189

5190 if (!\_dbus_string_append_len (buffer, str, len))

5191 goto fail_oom;

5192

5193 \_dbus_message_loader_return_buffer (loader, buffer);

5194

5195 if (!\_dbus_message_loader_queue_messages (loader))

5196 goto fail_oom;

5197

5198 if (\_dbus_message_loader_get_is_corrupted (loader))

5199 goto fail_corrupt;

5200

5201 msg = \_dbus_message_loader_pop_message (loader);

5202

5203 if (!msg)

5204 goto fail_oom;

5205

5206 \_dbus_message_loader_unref (loader);

5207 return msg;

5208

5209 fail_corrupt:

5210 if (loader-\>corruption_reason == DBUS_VALIDITY_UNKNOWN_OOM_ERROR)

5211 goto fail_oom;

5212

5213 dbus_set_error (error, DBUS_ERROR_INVALID_ARGS, "Message is corrupted (%s)",

5214 \_dbus_validity_to_error_message (loader-\>corruption_reason));

5215 \_dbus_message_loader_unref (loader);

5216 return NULL;

5217

5218 fail_oom:

5219 \_DBUS_SET_OOM (error);

5220

5221 if (loader != NULL)

5222 \_dbus_message_loader_unref (loader);

5223

5224 return NULL;

5225}

5226

5239int

5240dbus_message_demarshal_bytes_needed(const char \*buf,

5241 int len)

5242{

5243 DBusString str;

5244 int byte_order, fields_array_len, header_len, body_len;

5245 DBusValidity validity = DBUS_VALID;

5246 int have_message;

5247

5248 if (!buf \|\| len \< DBUS_MINIMUM_HEADER_SIZE)

5249 return 0;

5250

5251 if (len \> DBUS_MAXIMUM_MESSAGE_LENGTH)

5252 len = DBUS_MAXIMUM_MESSAGE_LENGTH;

5253 \_dbus_string_init_const_len (&str, buf, len);

5254

5255 validity = DBUS_VALID;

5256 have_message

5257 = \_dbus_header_have_message_untrusted(DBUS_MAXIMUM_MESSAGE_LENGTH,

5258 &validity, &byte_order,

5259 &fields_array_len,

5260 &header_len,

5261 &body_len,

5262 &str, 0,

5263 len);

5264 \_dbus_string_free (&str);

5265

5266 if (validity == DBUS_VALID)

5267 {

5268 \_dbus_assert (have_message \|\| (header_len + body_len) \> len);

5269 (void) have_message; /\* unused unless asserting \*/

5270 return header_len + body_len;

5271 }

5272 else

5273 {

5274 return -1; /\* broken! \*/

5275 }

5276}

5277

5299void

5300dbus_message_set_allow_interactive_authorization (DBusMessage \*message,

5301 dbus_bool_t allow)

5302{

5303 \_dbus_return_if_fail (message != NULL);

5304 \_dbus_return_if_fail (!message-\>locked);

5305

5306 \_dbus_header_toggle_flag (&message-\>header,

5307 DBUS_HEADER_FLAG_ALLOW_INTERACTIVE_AUTHORIZATION,

5308 allow);

5309}

5310

5317dbus_bool_t

5318dbus_message_get_allow_interactive_authorization (DBusMessage \*message)

5319{

5320 \_dbus_return_val_if_fail (message != NULL, FALSE);

5321

5322 return \_dbus_header_get_flag (&message-\>header,

5323 DBUS_HEADER_FLAG_ALLOW_INTERACTIVE_AUTHORIZATION);

5324}

5325

5332struct DBusVariant

5333{

5334 DBusString data;

5335};

5336

5348DBusVariant \*

5349\_dbus_variant_read (DBusMessageIter \*reader)

5350{

5351 DBusVariant \*self = NULL;

5352 /\* Points to the single item we will read from the reader \*/

5353 DBusMessageRealIter \*real_reader = (DBusMessageRealIter \*) reader;

5354 /\* The position in self at which we will write a single variant

5355 \* (it is position 0) \*/

5356 DBusTypeWriter items_writer;

5357 /\* The position in self at which we will write a copy of reader

5358 \* (it is inside the variant) \*/

5359 DBusTypeWriter variant_writer;

5360 /\* 'v' \*/

5361 DBusString variant_signature;

5362 /\* Whatever is the signature of the item we will copy from the reader \*/

5363 DBusString contained_signature;

5364 /\* TRUE if self-\>data needs to be freed \*/

5365 dbus_bool_t data_inited = FALSE;

5366 /\* The type of the item we will read from the reader \*/

5367 int type;

5368 /\* The string, start position within that string, and length of the signature

5369 \* of the single complete type of the item reader points to \*/

5370 const DBusString \*sig;

5371 int start, len;

5372

5373 \_dbus_assert (\_dbus_message_iter_check (real_reader));

5374 \_dbus_assert (real_reader-\>iter_type == DBUS_MESSAGE_ITER_TYPE_READER);

5375 \_dbus_string_init_const (&variant_signature, DBUS_TYPE_VARIANT_AS_STRING);

5376 type = dbus_message_iter_get_arg_type (reader);

5377 \_dbus_type_reader_get_signature (&real_reader-\>u.reader, &sig, &start, &len);

5378

5379 if (!\_dbus_string_init (&contained_signature))

5380 return NULL;

5381

5382 if (!\_dbus_string_copy_len (sig, start, len, &contained_signature, 0))

5383 goto oom;

5384

5385 self = dbus_new0 (DBusVariant, 1);

5386

5387 if (self == NULL)

5388 goto oom;

5389

5390 if (!\_dbus_string_init (&self-\>data))

5391 goto oom;

5392

5393 data_inited = TRUE;

5394

5395 \_dbus_type_writer_init_values_only (&items_writer, DBUS_COMPILER_BYTE_ORDER,

5396 &variant_signature, 0, &self-\>data, 0);

5397

5398 if (!\_dbus_type_writer_recurse (&items_writer, DBUS_TYPE_VARIANT,

5399 &contained_signature, 0, &variant_writer))

5400 goto oom;

5401

5402 if (type == DBUS_TYPE_ARRAY)

5403 {

5404 /\* Points to each item in turn inside the array we are copying \*/

5405 DBusMessageIter array_reader;

5406 /\* Same as array_reader \*/

5407 DBusMessageRealIter \*real_array_reader = (DBusMessageRealIter \*) &array_reader;

5408 /\* The position inside the copied array at which we will write

5409 \* the copy of array_reader \*/

5410 DBusTypeWriter array_writer;

5411

5412 dbus_message_iter_recurse (reader, &array_reader);

5413

5414 if (!\_dbus_type_writer_recurse (&variant_writer, type,

5415 &contained_signature, 1, &array_writer))

5416 goto oom;

5417

5418 if (!\_dbus_type_writer_write_reader (&array_writer,

5419 &real_array_reader-\>u.reader))

5420 goto oom;

5421

5422 if (!\_dbus_type_writer_unrecurse (&variant_writer, &array_writer))

5423 goto oom;

5424 }

5425 else if (type == DBUS_TYPE_DICT_ENTRY \|\| type == DBUS_TYPE_VARIANT \|\|

5426 type == DBUS_TYPE_STRUCT)

5427 {

5428 /\* Points to each item in turn inside the container we are copying \*/

5429 DBusMessageIter inner_reader;

5430 /\* Same as inner_reader \*/

5431 DBusMessageRealIter \*real_inner_reader = (DBusMessageRealIter \*) &inner_reader;

5432 /\* The position inside the copied container at which we will write the

5433 \* copy of inner_reader \*/

5434 DBusTypeWriter inner_writer;

5435

5436 dbus_message_iter_recurse (reader, &inner_reader);

5437

5438 if (!\_dbus_type_writer_recurse (&variant_writer, type, NULL, 0,

5439 &inner_writer))

5440 goto oom;

5441

5442 if (!\_dbus_type_writer_write_reader (&inner_writer,

5443 &real_inner_reader-\>u.reader))

5444 goto oom;

5445

5446 if (!\_dbus_type_writer_unrecurse (&variant_writer, &inner_writer))

5447 goto oom;

5448 }

5449 else

5450 {

5451 DBusBasicValue value;

5452

5453 /\* We eliminated all the container types above \*/

5454 \_dbus_assert (dbus_type_is_basic (type));

5455

5456 dbus_message_iter_get_basic (reader, &value);

5457

5458 if (!\_dbus_type_writer_write_basic (&variant_writer, type, &value))

5459 goto oom;

5460 }

5461

5462 \_dbus_string_free (&contained_signature);

5463 return self;

5464

5465oom:

5466 if (self != NULL)

5467 {

5468 if (data_inited)

5469 \_dbus_string_free (&self-\>data);

5470

5471 dbus_free (self);

5472 }

5473

5474 \_dbus_string_free (&contained_signature);

5475 return NULL;

5476}

5477

5484const char \*

5485\_dbus_variant_get_signature (DBusVariant \*self)

5486{

5487 const char \*ret;

5488\#ifndef DBUS_DISABLE_ASSERT

5489 unsigned char len;

5490\#endif

5491

5492 \_dbus_assert (self != NULL);

5493

5494\#ifndef DBUS_DISABLE_ASSERT

5495 /\* Here we make use of the fact that the serialization of a variant starts

5496 \* with the 1-byte length, then that many bytes of signature, then \0. \*/

5497 len = \_dbus_string_get_byte (&self-\>data, 0);

5498\#endif

5499 ret = \_dbus_string_get_const_data_len (&self-\>data, 1, len);

5500 \_dbus_assert (strlen (ret) == len);

5501 return ret;

5502}

5503

5515dbus_bool_t

5516\_dbus_variant_write (DBusVariant \*self,

5517 DBusMessageIter \*writer)

5518{

5519 /\* 'v' \*/

5520 DBusString variant_signature;

5521 /\* Points to the single item in self \*/

5522 DBusTypeReader variant_reader;

5523 /\* Points to the single item (of whatever type) inside the variant \*/

5524 DBusTypeReader reader;

5525 /\* The position at which we will copy reader \*/

5526 DBusMessageRealIter \*real_writer = (DBusMessageRealIter \*) writer;

5527 dbus_bool_t ret;

5528

5529 \_dbus_assert (self != NULL);

5530 \_dbus_assert (\_dbus_message_iter_append_check (real_writer));

5531 \_dbus_assert (real_writer-\>iter_type == DBUS_MESSAGE_ITER_TYPE_WRITER);

5532

5533 \_dbus_string_init_const (&variant_signature, DBUS_TYPE_VARIANT_AS_STRING);

5534 \_dbus_type_reader_init (&reader, DBUS_COMPILER_BYTE_ORDER,

5535 &variant_signature, 0, &self-\>data, 0);

5536 \_dbus_type_reader_recurse (&reader, &variant_reader);

5537

5538 if (!\_dbus_message_iter_open_signature (real_writer))

5539 return FALSE;

5540

5541 ret = \_dbus_type_writer_write_reader (&real_writer-\>u.writer,

5542 &variant_reader);

5543

5544 if (!\_dbus_message_iter_close_signature (real_writer))

5545 return FALSE;

5546

5547 return ret;

5548}

5549

5550int

5551\_dbus_variant_get_length (DBusVariant \*self)

5552{

5553 \_dbus_assert (self != NULL);

5554 return \_dbus_string_get_length (&self-\>data);

5555}

5556

5557const DBusString \*

5558\_dbus_variant_peek (DBusVariant \*self)

5559{

5560 \_dbus_assert (self != NULL);

5561 return &self-\>data;

5562}

5563

5564void

5565\_dbus_variant_free (DBusVariant \*self)

5566{

5567 \_dbus_assert (self != NULL);

5568 \_dbus_string_free (&self-\>data);

5569 dbus_free (self);

5570}

5571

5574/\* tests in dbus-message-util.c \*/

\_dbus_data_slot_allocator_free

void \_dbus_data_slot_allocator_free(DBusDataSlotAllocator \*allocator, dbus_int32_t \*slot_id_p)

Deallocates an ID previously allocated with \_dbus_data_slot_allocator_alloc().

**Definition** dbus-dataslot.c:157

\_dbus_data_slot_list_clear

void \_dbus_data_slot_list_clear(DBusDataSlotList \*list)

Frees all data slots contained in the list, calling application-provided free functions if they exist...

**Definition** dbus-dataslot.c:320

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

dbus_error_init

void dbus_error_init(DBusError \*error)

Initializes a DBusError structure.

**Definition** dbus-errors.c:190

dbus_set_error

void dbus_set_error(DBusError \*error, const char \*name, const char \*format,...)

Assigns an error name and message to a DBusError.

**Definition** dbus-errors.c:356

dbus_error_free

void dbus_error_free(DBusError \*error)

Frees an error that's been set (or just initialized), then reinitializes the error as in dbus_error_i...

**Definition** dbus-errors.c:213

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

\_dbus_warn_check_failed

void \_dbus_warn_check_failed(const char \*format,...)

Prints a "critical" warning to stderr when an assertion fails; differs from \_dbus_warn primarily in t...

**Definition** dbus-internals.c:310

\_dbus_strdup

char \* \_dbus_strdup(const char \*str)

Duplicates a string.

**Definition** dbus-internals.c:621

\_dbus_warn

void \_dbus_warn(const char \*format,...)

Prints a warning message to stderr.

**Definition** dbus-internals.c:278

\_DBUS_LOCK_NAME

\#define \_DBUS_LOCK_NAME(name)

Expands to name of a global lock variable.

**Definition** dbus-internals.h:436

\_DBUS_ZERO

\#define \_DBUS_ZERO(object)

Sets all bits in an object to zero.

**Definition** dbus-internals.h:194

\_dbus_memdup

void \* \_dbus_memdup(const void \*mem, size_t n_bytes)

Duplicates a block of memory.

**Definition** dbus-internals.c:649

\_dbus_list_pop_first_link

DBusList \* \_dbus_list_pop_first_link(DBusList \*\*list)

Removes the first link in the list and returns it.

**Definition** dbus-list.c:658

\_dbus_list_append_link

void \_dbus_list_append_link(DBusList \*\*list, DBusList \*link)

Appends a link to the list.

**Definition** dbus-list.c:318

\_dbus_list_clear_full

void \_dbus_list_clear_full(DBusList \*\*list, DBusFreeFunction function)

Free every link and every element in the list.

**Definition** dbus-list.c:570

\_dbus_list_remove_link

void \_dbus_list_remove_link(DBusList \*\*list, DBusList \*link)

Removes a link from the list.

**Definition** dbus-list.c:530

\_dbus_list_find_last

DBusList \* \_dbus_list_find_last(DBusList \*\*list, void \*data)

Finds a value in the list.

**Definition** dbus-list.c:475

\_dbus_list_pop_first

void \* \_dbus_list_pop_first(DBusList \*\*list)

Removes the first value in the list and returns it.

**Definition** dbus-list.c:679

\_dbus_list_foreach

void \_dbus_list_foreach(DBusList \*\*list, DBusForeachFunction function, void \*data)

Calls the given function for each element in the list.

**Definition** dbus-list.c:789

\_dbus_list_clear

void \_dbus_list_clear(DBusList \*\*list)

Frees all links in the list and sets the list head to NULL.

**Definition** dbus-list.c:545

\_dbus_list_prepend_link

void \_dbus_list_prepend_link(DBusList \*\*list, DBusList \*link)

Prepends a link to the list.

**Definition** dbus-list.c:336

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

\_dbus_type_writer_write_basic

dbus_bool_t \_dbus_type_writer_write_basic(DBusTypeWriter \*writer, int type, const void \*value)

Writes out a basic type.

**Definition** dbus-marshal-recursive.c:2310

\_dbus_type_reader_recurse

void \_dbus_type_reader_recurse(DBusTypeReader \*reader, DBusTypeReader \*sub)

Initialize a new reader pointing to the first type and corresponding value that's a child of the curr...

**Definition** dbus-marshal-recursive.c:987

DBusValidity

DBusValidity

This is primarily used in unit testing, so we can verify that each invalid message is invalid for the...

**Definition** dbus-marshal-validate.h:54

\_dbus_header_update_lengths

void \_dbus_header_update_lengths(DBusHeader \*header, int body_len)

Fills in the correct body length.

**Definition** dbus-marshal-header.c:1207

\_dbus_header_copy

dbus_bool_t \_dbus_header_copy(const DBusHeader \*header, DBusHeader \*dest)

Initializes dest with a copy of the given header.

**Definition** dbus-marshal-header.c:495

\_dbus_validate_signature_with_reason

DBusValidity \_dbus_validate_signature_with_reason(const DBusString \*type_str, int type_pos, int len)

Verifies that the range of type_str from type_pos to type_end is a valid signature.

**Definition** dbus-marshal-validate.c:53

\_dbus_type_writer_init_values_only

void \_dbus_type_writer_init_values_only(DBusTypeWriter \*writer, int byte_order, const DBusString \*type_str, int type_pos, DBusString \*value_str, int value_pos)

Like \_dbus_type_writer_init(), except the type string passed in should correspond to an existing sign...

**Definition** dbus-marshal-recursive.c:1583

\_dbus_type_get_alignment

int \_dbus_type_get_alignment(int typecode)

Gets the alignment requirement for the given type; will be 1, 2, 4, or 8.

**Definition** dbus-marshal-basic.c:1244

\_dbus_type_writer_remove_types

void \_dbus_type_writer_remove_types(DBusTypeWriter \*writer)

Removes type string from the writer.

**Definition** dbus-marshal-recursive.c:1562

\_dbus_type_reader_init

void \_dbus_type_reader_init(DBusTypeReader \*reader, int byte_order, const DBusString \*type_str, int type_pos, const DBusString \*value_str, int value_pos)

Initializes a type reader.

**Definition** dbus-marshal-recursive.c:732

\_dbus_verbose_bytes_of_string

DBUS_PRIVATE_EXPORT void \_dbus_verbose_bytes_of_string(const DBusString \*str, int start, int len)

Dump the given part of the string to verbose log.

**Definition** dbus-marshal-basic.c:1428

\_dbus_header_set_field_basic

dbus_bool_t \_dbus_header_set_field_basic(DBusHeader \*header, int field, int type, const void \*value)

Sets the value of a field with basic type.

**Definition** dbus-marshal-header.c:1284

\_dbus_header_get_message_type

int \_dbus_header_get_message_type(DBusHeader \*header)

Gets the type of the message.

**Definition** dbus-marshal-header.c:391

\_dbus_type_reader_get_signature

void \_dbus_type_reader_get_signature(const DBusTypeReader \*reader, const DBusString \*\*str_p, int \*start_p, int \*len_p)

Gets the string and range of said string containing the signature of the current value.

**Definition** dbus-marshal-recursive.c:1124

\_dbus_type_writer_write_reader

dbus_bool_t \_dbus_type_writer_write_reader(DBusTypeWriter \*writer, DBusTypeReader \*reader)

Iterate through all values in the given reader, writing a copy of each value to the writer.

**Definition** dbus-marshal-recursive.c:2730

\_dbus_header_get_field_basic

dbus_bool_t \_dbus_header_get_field_basic(DBusHeader \*header, int field, int type, void \*value)

Gets the value of a field with basic type.

**Definition** dbus-marshal-header.c:1362

\_dbus_type_writer_recurse

dbus_bool_t \_dbus_type_writer_recurse(DBusTypeWriter \*writer, int container_type, const DBusString \*contained_type, int contained_type_start, DBusTypeWriter \*sub)

Opens a new container and writes out the initial information for that container.

**Definition** dbus-marshal-recursive.c:2108

\_dbus_header_get_flag

dbus_bool_t \_dbus_header_get_flag(DBusHeader \*header, dbus_uint32_t flag)

Gets a message flag bit, returning TRUE if the bit is set.

**Definition** dbus-marshal-header.c:1490

\_dbus_marshal_byteswap

void \_dbus_marshal_byteswap(const DBusString \*signature, int signature_start, int old_byte_order, int new_byte_order, DBusString \*value_str, int value_pos)

Byteswaps the marshaled data in the given value_str.

**Definition** dbus-marshal-byteswap.c:224

\_dbus_type_reader_read_fixed_multi

void \_dbus_type_reader_read_fixed_multi(const DBusTypeReader \*reader, const void \*\*value, int \*n_elements)

Reads a block of fixed-length basic values, from the current point in an array to the end of the arra...

**Definition** dbus-marshal-recursive.c:923

\_dbus_header_get_byte_order

char \_dbus_header_get_byte_order(const DBusHeader \*header)

Returns the header's byte order.

**Definition** dbus-marshal-header.c:179

\_dbus_header_have_message_untrusted

dbus_bool_t \_dbus_header_have_message_untrusted(int max_message_length, DBusValidity \*validity, int \*byte_order, int \*fields_array_len, int \*header_len, int \*body_len, const DBusString \*str, int start, int len)

Given data long enough to contain the length of the message body and the fields array,...

**Definition** dbus-marshal-header.c:681

\_dbus_header_reinit

void \_dbus_header_reinit(DBusHeader \*header)

Re-initializes a header that was previously initialized and never freed.

**Definition** dbus-marshal-header.c:448

\_dbus_type_reader_get_element_type

int \_dbus_type_reader_get_element_type(const DBusTypeReader \*reader)

Gets the type of an element of the array the reader is currently pointing to.

**Definition** dbus-marshal-recursive.c:820

\_dbus_type_reader_next

dbus_bool_t \_dbus_type_reader_next(DBusTypeReader \*reader)

Skip to the next value on this "level".

**Definition** dbus-marshal-recursive.c:1053

\_dbus_header_delete_field

dbus_bool_t \_dbus_header_delete_field(DBusHeader \*header, int field)

Deletes a field, if it exists.

**Definition** dbus-marshal-header.c:1427

\_dbus_type_reader_get_array_length

int \_dbus_type_reader_get_array_length(const DBusTypeReader \*reader)

Returns the number of bytes in the array.

**Definition** dbus-marshal-recursive.c:899

\_dbus_header_remove_unknown_fields

dbus_bool_t \_dbus_header_remove_unknown_fields(DBusHeader \*header)

Remove every header field not known to this version of dbus.

**Definition** dbus-marshal-header.c:1532

\_dbus_header_get_serial

dbus_uint32_t \_dbus_header_get_serial(DBusHeader \*header)

See dbus_message_get_serial()

**Definition** dbus-marshal-header.c:432

\_dbus_type_writer_add_types

void \_dbus_type_writer_add_types(DBusTypeWriter \*writer, DBusString \*type_str, int type_pos)

Adds type string to the writer, if it had none.

**Definition** dbus-marshal-recursive.c:1545

\_dbus_type_reader_has_next

dbus_bool_t \_dbus_type_reader_has_next(const DBusTypeReader \*reader)

Check whether there's another value on this "level".

**Definition** dbus-marshal-recursive.c:1093

\_dbus_type_reader_read_basic

void \_dbus_type_reader_read_basic(const DBusTypeReader \*reader, void \*value)

Reads a basic-typed value, as with \_dbus_marshal_read_basic().

**Definition** dbus-marshal-recursive.c:869

\_dbus_type_writer_init_types_delayed

void \_dbus_type_writer_init_types_delayed(DBusTypeWriter \*writer, int byte_order, DBusString \*value_str, int value_pos)

Initialize a write iterator, with the signature to be provided later.

**Definition** dbus-marshal-recursive.c:1527

\_dbus_type_to_string

const char \* \_dbus_type_to_string(int typecode)

Returns a string describing the given type.

**Definition** dbus-marshal-basic.c:1290

\_dbus_validate_body_with_reason

DBusValidity \_dbus_validate_body_with_reason(const DBusString \*expected_signature, int expected_signature_start, int byte_order, int \*bytes_remaining, const DBusString \*value_str, int value_pos, int len)

Verifies that the range of value_str from value_pos to value_end is a legitimate value of type expect...

**Definition** dbus-marshal-validate.c:767

\_dbus_type_reader_get_current_type

int \_dbus_type_reader_get_current_type(const DBusTypeReader \*reader)

Gets the type of the value the reader is currently pointing to; or for a types-only reader gets the t...

**Definition** dbus-marshal-recursive.c:785

\_dbus_header_free

void \_dbus_header_free(DBusHeader \*header)

Frees a header.

**Definition** dbus-marshal-header.c:481

\_dbus_header_init

dbus_bool_t \_dbus_header_init(DBusHeader \*header)

Initializes a header, but doesn't prepare it for use; to make the header valid, you have to call \_dbu...

**Definition** dbus-marshal-header.c:465

\_dbus_header_create

dbus_bool_t \_dbus_header_create(DBusHeader \*header, int byte_order, int message_type, const char \*destination, const char \*path, const char \*interface, const char \*member, const char \*error_name)

Fills in the primary fields of the header, so the header is ready for use.

**Definition** dbus-marshal-header.c:533

\_dbus_type_writer_unrecurse

dbus_bool_t \_dbus_type_writer_unrecurse(DBusTypeWriter \*writer, DBusTypeWriter \*sub)

Closes a container created by \_dbus_type_writer_recurse() and writes any additional information to th...

**Definition** dbus-marshal-recursive.c:2178

\_dbus_type_writer_write_fixed_multi

dbus_bool_t \_dbus_type_writer_write_fixed_multi(DBusTypeWriter \*writer, int element_type, const void \*value, int n_elements)

Writes a block of fixed-length basic values, i.e.

**Definition** dbus-marshal-recursive.c:2358

\_dbus_header_toggle_flag

void \_dbus_header_toggle_flag(DBusHeader \*header, dbus_uint32_t flag, dbus_bool_t value)

Toggles a message flag bit, turning on the bit if value = TRUE and flipping it off if value = FALSE.

**Definition** dbus-marshal-header.c:1468

\_dbus_header_set_serial

void \_dbus_header_set_serial(DBusHeader \*header, dbus_uint32_t serial)

Sets the serial number of a header.

**Definition** dbus-marshal-header.c:409

\_dbus_header_load

dbus_bool_t \_dbus_header_load(DBusHeader \*header, DBusValidationMode mode, DBusValidity \*validity, int byte_order, int fields_array_len, int header_len, int body_len, const DBusString \*str)

Creates a message header from potentially-untrusted data.

**Definition** dbus-marshal-header.c:981

\_dbus_header_byteswap

void \_dbus_header_byteswap(DBusHeader \*header, int new_order)

Swaps the header into the given order if required.

**Definition** dbus-marshal-header.c:1507

\_dbus_header_get_field_raw

dbus_bool_t \_dbus_header_get_field_raw(DBusHeader \*header, int field, const DBusString \*\*str, int \*pos)

Gets the raw marshaled data for a field.

**Definition** dbus-marshal-header.c:1403

DBusValidationMode

DBusValidationMode

This is used rather than a bool for high visibility.

**Definition** dbus-marshal-validate.h:41

DBUS_VALIDITY_UNKNOWN_OOM_ERROR

@ DBUS_VALIDITY_UNKNOWN_OOM_ERROR

can't determine validity due to OOM

**Definition** dbus-marshal-validate.h:56

DBUS_VALID

@ DBUS_VALID

the data is valid

**Definition** dbus-marshal-validate.h:60

\_dbus_current_generation

int \_dbus_current_generation

\_dbus_current_generation is used to track each time that dbus_shutdown() is called,...

**Definition** dbus-memory.c:790

\_dbus_register_shutdown_func

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_register_shutdown_func(DBusShutdownFunction function, void \*data)

Register a cleanup function to be called exactly once the next time dbus_shutdown() is called.

**Definition** dbus-memory.c:819

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

dbus_new

\#define dbus_new(type, count)

Safe macro for using dbus_malloc().

**Definition** dbus-memory.h:59

dbus_new0

\#define dbus_new0(type, count)

Safe macro for using dbus_malloc0().

**Definition** dbus-memory.h:60

dbus_free_string_array

void dbus_free_string_array(char \*\*str_array)

Frees a NULL-terminated array of strings.

**Definition** dbus-memory.c:758

\_dbus_message_loader_set_max_message_size

void \_dbus_message_loader_set_max_message_size(DBusMessageLoader \*loader, long size)

Sets the maximum size message we allow.

**Definition** dbus-message.c:4843

\_dbus_message_remove_unknown_fields

dbus_bool_t \_dbus_message_remove_unknown_fields(DBusMessage \*message)

Remove every header field not known to this version of dbus.

**Definition** dbus-message.c:284

\_dbus_message_iter_get_args_valist

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_message_iter_get_args_valist(DBusMessageIter \*iter, DBusError \*error, int first_arg_type, va_list var_args)

Implementation of the varargs arg-getting functions.

**Definition** dbus-message.c:838

\_dbus_variant_read

DBusVariant \* \_dbus_variant_read(DBusMessageIter \*reader)

Copy a single D-Bus message item from reader into a newly-allocated DBusVariant.

**Definition** dbus-message.c:5349

ensure_byte_order

\#define ensure_byte_order(message)

byte-swap the message if it doesn't match our byte order.

**Definition** dbus-message.c:230

MAX_MESSAGE_SIZE_TO_CACHE

\#define MAX_MESSAGE_SIZE_TO_CACHE

Avoid caching huge messages.

**Definition** dbus-message.c:508

\_dbus_variant_write

dbus_bool_t \_dbus_variant_write(DBusVariant \*self, DBusMessageIter \*writer)

Copy the single D-Bus message item from self into writer.

**Definition** dbus-message.c:5516

dbus_message_iter_init_closed

void dbus_message_iter_init_closed(DBusMessageIter \*iter)

Initialize iter as if with DBUS_MESSAGE_ITER_INIT_CLOSED.

**Definition** dbus-message.c:755

\_dbus_message_loader_get_is_corrupted

dbus_bool_t \_dbus_message_loader_get_is_corrupted(DBusMessageLoader \*loader)

Checks whether the loader is confused due to bad data.

**Definition** dbus-message.c:4814

dbus_message_set_serial

void dbus_message_set_serial(DBusMessage \*message, dbus_uint32_t serial)

Sets the serial number of a message.

**Definition** dbus-message.c:301

dbus_message_lock

void dbus_message_lock(DBusMessage \*message)

Locks a message.

**Definition** dbus-message.c:431

dbus_message_type_from_string

int dbus_message_type_from_string(const char \*type_str)

Utility function to convert a machine-readable (not translated) string into a D-Bus message type.

**Definition** dbus-message.c:5053

\_dbus_message_loader_unref

void \_dbus_message_loader_unref(DBusMessageLoader \*loader)

Decrements the reference count of the loader and finalizes the loader when the count reaches zero.

**Definition** dbus-message.c:4239

dbus_message_allocate_data_slot

dbus_bool_t dbus_message_allocate_data_slot(dbus_int32_t \*slot_p)

Allocates an integer ID to be used for storing application-specific data on any DBusMessage.

**Definition** dbus-message.c:4950

\_dbus_message_get_unix_fds

void \_dbus_message_get_unix_fds(DBusMessage \*message, const int \*\*fds, unsigned \*n_fds)

Gets the unix fds to be sent over the network for this message.

**Definition** dbus-message.c:262

dbus_message_demarshal

DBusMessage \* dbus_message_demarshal(const char \*str, int len, DBusError \*error)

Demarshal a D-Bus message from the format described in the D-Bus specification.

**Definition** dbus-message.c:5173

\_dbus_message_loader_pop_message

DBusMessage \* \_dbus_message_loader_pop_message(DBusMessageLoader \*loader)

Pops a loaded message (passing ownership of the message to the caller).

**Definition** dbus-message.c:4772

\_dbus_message_get_network_data

void \_dbus_message_get_network_data(DBusMessage \*message, const DBusString \*\*header, const DBusString \*\*body)

Gets the data to be sent over the network for this message.

**Definition** dbus-message.c:243

\_dbus_message_loader_set_pending_fds_function

void \_dbus_message_loader_set_pending_fds_function(DBusMessageLoader \*loader, void(\*callback)(void \*), void \*data)

Register a function to be called whenever the number of pending file descriptors in the loader change...

**Definition** dbus-message.c:4922

CHANGED_STAMP_BITS

\#define CHANGED_STAMP_BITS

How many bits are in the changed_stamp used to validate iterators.

**Definition** dbus-message-private.h:92

dbus_message_set_data

dbus_bool_t dbus_message_set_data(DBusMessage \*message, dbus_int32_t slot, void \*data, DBusFreeFunction free_data_func)

Stores a pointer on a DBusMessage, along with an optional function to be used for freeing the data wh...

**Definition** dbus-message.c:4989

\_dbus_message_loader_putback_message_link

void \_dbus_message_loader_putback_message_link(DBusMessageLoader \*loader, DBusList \*link)

Returns a popped message link, used to undo a pop.

**Definition** dbus-message.c:4798

dbus_message_get_data

void \* dbus_message_get_data(DBusMessage \*message, dbus_int32_t slot)

Retrieves data previously set with dbus_message_set_data().

**Definition** dbus-message.c:5025

dbus_message_type_to_string

const char \* dbus_message_type_to_string(int type)

Utility function to convert a D-Bus message type into a machine-readable string (not translated).

**Definition** dbus-message.c:5081

dbus_message_set_allow_interactive_authorization

void dbus_message_set_allow_interactive_authorization(DBusMessage \*message, dbus_bool_t allow)

Sets a flag indicating that the caller of the method is prepared to wait for interactive authorizatio...

**Definition** dbus-message.c:5300

\_dbus_message_loader_get_pending_fds_count

int \_dbus_message_loader_get_pending_fds_count(DBusMessageLoader \*loader)

Return how many file descriptors are pending in the loader.

**Definition** dbus-message.c:4904

\_dbus_variant_get_signature

const char \* \_dbus_variant_get_signature(DBusVariant \*self)

Return the signature of the item stored in self.

**Definition** dbus-message.c:5485

dbus_message_demarshal_bytes_needed

int dbus_message_demarshal_bytes_needed(const char \*buf, int len)

Returns the number of bytes required to be in the buffer to demarshal a D-Bus message.

**Definition** dbus-message.c:5240

\_dbus_message_loader_get_buffer

void \_dbus_message_loader_get_buffer(DBusMessageLoader \*loader, DBusString \*\*buffer, int \*max_to_read, dbus_bool_t \*may_read_fds)

Gets the buffer to use for reading data from the network.

**Definition** dbus-message.c:4274

dbus_message_free_data_slot

void dbus_message_free_data_slot(dbus_int32_t \*slot_p)

Deallocates a global ID for message data slots.

**Definition** dbus-message.c:4968

\_dbus_message_remove_counter

void \_dbus_message_remove_counter(DBusMessage \*message, DBusCounter \*counter)

Removes a counter tracking the size/unix fds of this message, and decrements the counter by the size/...

**Definition** dbus-message.c:399

INITIAL_LOADER_DATA_LEN

\#define INITIAL_LOADER_DATA_LEN

The initial buffer size of the message loader.

**Definition** dbus-message.c:4168

\_dbus_message_add_counter

dbus_bool_t \_dbus_message_add_counter(DBusMessage \*message, DBusCounter \*counter)

Adds a counter to be incremented immediately with the size/unix fds of this message,...

**Definition** dbus-message.c:376

\_dbus_message_loader_peek_message

DBusMessage \* \_dbus_message_loader_peek_message(DBusMessageLoader \*loader)

Peeks at first loaded message, returns NULL if no messages have been queued.

**Definition** dbus-message.c:4755

dbus_message_marshal

dbus_bool_t dbus_message_marshal(DBusMessage \*msg, char \*\*marshalled_data_p, int \*len_p)

Turn a DBusMessage into the marshalled form as described in the D-Bus specification.

**Definition** dbus-message.c:5111

\_dbus_message_loader_set_max_message_unix_fds

void \_dbus_message_loader_set_max_message_unix_fds(DBusMessageLoader \*loader, long n)

Sets the maximum unix fds per message we allow.

**Definition** dbus-message.c:4874

\_dbus_message_loader_get_max_message_size

long \_dbus_message_loader_get_max_message_size(DBusMessageLoader \*loader)

Gets the maximum allowed message size in bytes.

**Definition** dbus-message.c:4862

\_dbus_message_loader_new

DBusMessageLoader \* \_dbus_message_loader_new(void)

Creates a new message loader.

**Definition** dbus-message.c:4177

MAX_MESSAGE_CACHE_SIZE

\#define MAX_MESSAGE_CACHE_SIZE

Avoid caching too many messages.

**Definition** dbus-message.c:511

\_dbus_message_loader_pop_message_link

DBusList \* \_dbus_message_loader_pop_message_link(DBusMessageLoader \*loader)

Pops a loaded message inside a list link (passing ownership of the message and link to the caller).

**Definition** dbus-message.c:4786

\_dbus_message_loader_queue_messages

dbus_bool_t \_dbus_message_loader_queue_messages(DBusMessageLoader \*loader)

Converts buffered data into messages, if we have enough data.

**Definition** dbus-message.c:4692

\_dbus_message_loader_return_buffer

void \_dbus_message_loader_return_buffer(DBusMessageLoader \*loader, DBusString \*buffer)

Returns a buffer obtained from \_dbus_message_loader_get_buffer(), indicating to the loader how many b...

**Definition** dbus-message.c:4380

\_dbus_message_loader_ref

DBusMessageLoader \* \_dbus_message_loader_ref(DBusMessageLoader \*loader)

Increments the reference count of the loader.

**Definition** dbus-message.c:4225

\_dbus_message_loader_get_max_message_unix_fds

long \_dbus_message_loader_get_max_message_unix_fds(DBusMessageLoader \*loader)

Gets the maximum allowed number of unix fds per message.

**Definition** dbus-message.c:4893

\_dbus_message_add_counter_link

void \_dbus_message_add_counter_link(DBusMessage \*message, DBusList \*link)

Adds a counter to be incremented immediately with the size/unix fds of this message,...

**Definition** dbus-message.c:327

\_dbus_message_loader_get_corruption_reason

DBusValidity \_dbus_message_loader_get_corruption_reason(DBusMessageLoader \*loader)

Checks what kind of bad data confused the loader.

**Definition** dbus-message.c:4828

dbus_message_get_allow_interactive_authorization

dbus_bool_t dbus_message_get_allow_interactive_authorization(DBusMessage \*message)

Returns whether the flag controlled by dbus_message_set_allow_interactive_authorization() has been se...

**Definition** dbus-message.c:5318

dbus_message_has_destination

dbus_bool_t dbus_message_has_destination(DBusMessage \*message, const char \*name)

Checks whether the message was sent to the given name.

**Definition** dbus-message.c:3953

dbus_message_set_interface

dbus_bool_t dbus_message_set_interface(DBusMessage \*message, const char \*iface)

Sets the interface this message is being sent to (for DBUS_MESSAGE_TYPE_METHOD_CALL) or the interface...

**Definition** dbus-message.c:3461

dbus_message_has_interface

dbus_bool_t dbus_message_has_interface(DBusMessage \*message, const char \*iface)

Checks if the message has an interface.

**Definition** dbus-message.c:3512

dbus_message_set_no_reply

void dbus_message_set_no_reply(DBusMessage \*message, dbus_bool_t no_reply)

Sets a flag indicating that the message does not want a reply; if this flag is set,...

**Definition** dbus-message.c:3247

dbus_message_append_args_valist

dbus_bool_t dbus_message_append_args_valist(DBusMessage \*message, int first_arg_type, va_list var_args)

Like dbus_message_append_args() but takes a va_list for use by language bindings.

**Definition** dbus-message.c:1875

dbus_message_get_sender

const char \* dbus_message_get_sender(DBusMessage \*message)

Gets the unique name of the connection which originated this message, or NULL if unknown or inapplica...

**Definition** dbus-message.c:3773

dbus_message_set_auto_start

void dbus_message_set_auto_start(DBusMessage \*message, dbus_bool_t auto_start)

Sets a flag indicating that an owner for the destination name will be automatically started before th...

**Definition** dbus-message.c:3289

dbus_message_iter_append_basic

dbus_bool_t dbus_message_iter_append_basic(DBusMessageIter \*iter, int type, const void \*value)

Appends a basic-typed value to the message.

**Definition** dbus-message.c:2771

dbus_message_get_path

const char \* dbus_message_get_path(DBusMessage \*message)

Gets the object path this message is being sent to (for DBUS_MESSAGE_TYPE_METHOD_CALL) or being emitt...

**Definition** dbus-message.c:3359

dbus_message_get_interface

const char \* dbus_message_get_interface(DBusMessage \*message)

Gets the interface this message is being sent to (for DBUS_MESSAGE_TYPE_METHOD_CALL) or being emitted...

**Definition** dbus-message.c:3490

dbus_message_new_error

DBusMessage \* dbus_message_new_error(DBusMessage \*reply_to, const char \*error_name, const char \*error_message)

Creates a new message that is an error reply to another message.

**Definition** dbus-message.c:1515

dbus_message_has_sender

dbus_bool_t dbus_message_has_sender(DBusMessage \*message, const char \*name)

Checks whether the message has the given unique name as its sender.

**Definition** dbus-message.c:3988

dbus_message_get_serial

dbus_uint32_t dbus_message_get_serial(DBusMessage \*message)

Returns the serial of a message or 0 if none has been specified.

**Definition** dbus-message.c:1168

dbus_message_set_member

dbus_bool_t dbus_message_set_member(DBusMessage \*message, const char \*member)

Sets the interface member being invoked (DBUS_MESSAGE_TYPE_METHOD_CALL) or emitted (DBUS_MESSAGE_TYPE...

**Definition** dbus-message.c:3549

dbus_message_iter_get_basic

void dbus_message_iter_get_basic(DBusMessageIter \*iter, void \*value)

Reads a basic-typed value from the message iterator.

**Definition** dbus-message.c:2369

dbus_message_get_type

int dbus_message_get_type(DBusMessage \*message)

Gets the type of a message.

**Definition** dbus-message.c:1767

dbus_message_copy

DBusMessage \* dbus_message_copy(const DBusMessage \*message)

Creates a new message that is an exact replica of the message specified, except that its refcount is ...

**Definition** dbus-message.c:1632

dbus_message_get_error_name

const char \* dbus_message_get_error_name(DBusMessage \*message)

Gets the error name (DBUS_MESSAGE_TYPE_ERROR only) or NULL if none.

**Definition** dbus-message.c:3660

dbus_message_iter_next

dbus_bool_t dbus_message_iter_next(DBusMessageIter \*iter)

Moves the iterator to the next field, if any.

**Definition** dbus-message.c:2186

dbus_message_append_args

dbus_bool_t dbus_message_append_args(DBusMessage \*message, int first_arg_type,...)

Appends fields to a message given a variable argument list.

**Definition** dbus-message.c:1843

dbus_message_iter_get_arg_type

int dbus_message_iter_get_arg_type(DBusMessageIter \*iter)

Returns the argument type of the argument that the message iterator points to.

**Definition** dbus-message.c:2211

dbus_message_get_no_reply

dbus_bool_t dbus_message_get_no_reply(DBusMessage \*message)

Returns TRUE if the message does not expect a reply.

**Definition** dbus-message.c:3266

dbus_message_new_signal

DBusMessage \* dbus_message_new_signal(const char \*path, const char \*iface, const char \*name)

Constructs a new message representing a signal emission.

**Definition** dbus-message.c:1469

dbus_message_iter_append_fixed_array

dbus_bool_t dbus_message_iter_append_fixed_array(DBusMessageIter \*iter, int element_type, const void \*value, int n_elements)

Appends a block of fixed-length values to an array.

**Definition** dbus-message.c:2922

dbus_message_iter_abandon_container

void dbus_message_iter_abandon_container(DBusMessageIter \*iter, DBusMessageIter \*sub)

Abandons creation of a contained-typed value and frees resources created by dbus_message_iter_open_co...

**Definition** dbus-message.c:3123

dbus_message_new_error_printf

DBusMessage \* dbus_message_new_error_printf(DBusMessage \*reply_to, const char \*error_name, const char \*error_format,...)

Creates a new message that is an error reply to another message, allowing you to use printf formattin...

**Definition** dbus-message.c:1587

dbus_message_is_error

dbus_bool_t dbus_message_is_error(DBusMessage \*message, const char \*error_name)

Checks whether the message is an error reply with the given error name.

**Definition** dbus-message.c:3920

dbus_message_contains_unix_fds

dbus_bool_t dbus_message_contains_unix_fds(DBusMessage \*message)

Checks whether a message contains unix fds.

**Definition** dbus-message.c:4088

dbus_message_iter_recurse

void dbus_message_iter_recurse(DBusMessageIter \*iter, DBusMessageIter \*sub)

Recurses into a container value when reading values from a message, initializing a sub-iterator to us...

**Definition** dbus-message.c:2267

dbus_message_ref

DBusMessage \* dbus_message_ref(DBusMessage \*message)

Increments the reference count of a DBusMessage.

**Definition** dbus-message.c:1712

dbus_message_get_auto_start

dbus_bool_t dbus_message_get_auto_start(DBusMessage \*message)

Returns TRUE if the message will cause an owner for destination name to be auto-started.

**Definition** dbus-message.c:3308

dbus_message_iter_get_element_type

int dbus_message_iter_get_element_type(DBusMessageIter \*iter)

Returns the element type of the array that the message iterator points to.

**Definition** dbus-message.c:2230

dbus_message_set_error_name

dbus_bool_t dbus_message_set_error_name(DBusMessage \*message, const char \*error_name)

Sets the name of the error (DBUS_MESSAGE_TYPE_ERROR).

**Definition** dbus-message.c:3634

dbus_message_has_signature

dbus_bool_t dbus_message_has_signature(DBusMessage \*message, const char \*signature)

Checks whether the message has the given signature; see dbus_message_get_signature() for more details...

**Definition** dbus-message.c:4017

dbus_message_iter_open_container

dbus_bool_t dbus_message_iter_open_container(DBusMessageIter \*iter, int type, const char \*contained_signature, DBusMessageIter \*sub)

Appends a container-typed value to the message.

**Definition** dbus-message.c:2986

dbus_message_get_reply_serial

dbus_uint32_t dbus_message_get_reply_serial(DBusMessage \*message)

Returns the serial that the message is a reply to or 0 if none.

**Definition** dbus-message.c:1208

dbus_message_new_method_return

DBusMessage \* dbus_message_new_method_return(DBusMessage \*method_call)

Constructs a message that is a reply to a method call.

**Definition** dbus-message.c:1418

dbus_message_new_method_call

DBusMessage \* dbus_message_new_method_call(const char \*destination, const char \*path, const char \*iface, const char \*method)

Constructs a new message to invoke a method on a remote object.

**Definition** dbus-message.c:1378

dbus_message_iter_init

dbus_bool_t dbus_message_iter_init(DBusMessage \*message, DBusMessageIter \*iter)

Initializes a DBusMessageIter for reading the arguments of the message passed in.

**Definition** dbus-message.c:2136

dbus_message_set_sender

dbus_bool_t dbus_message_set_sender(DBusMessage \*message, const char \*sender)

Sets the message sender.

**Definition** dbus-message.c:3742

dbus_message_iter_abandon_container_if_open

void dbus_message_iter_abandon_container_if_open(DBusMessageIter \*iter, DBusMessageIter \*sub)

Abandons creation of a contained-typed value and frees resources created by dbus_message_iter_open_co...

**Definition** dbus-message.c:3182

dbus_message_get_destination

const char \* dbus_message_get_destination(DBusMessage \*message)

Gets the destination of a message or NULL if there is none set.

**Definition** dbus-message.c:3713

dbus_message_set_path

dbus_bool_t dbus_message_set_path(DBusMessage \*message, const char \*object_path)

Sets the object path this message is being sent to (for DBUS_MESSAGE_TYPE_METHOD_CALL) or the one a s...

**Definition** dbus-message.c:3330

dbus_message_iter_has_next

dbus_bool_t dbus_message_iter_has_next(DBusMessageIter \*iter)

Checks if an iterator has any more fields.

**Definition** dbus-message.c:2167

dbus_message_get_args_valist

dbus_bool_t dbus_message_get_args_valist(DBusMessage \*message, DBusError \*error, int first_arg_type, va_list var_args)

Like dbus_message_get_args but takes a va_list for use by language bindings.

**Definition** dbus-message.c:2061

dbus_message_iter_get_signature

char \* dbus_message_iter_get_signature(DBusMessageIter \*iter)

Returns the current signature of a message iterator.

**Definition** dbus-message.c:2292

dbus_message_unref

void dbus_message_unref(DBusMessage \*message)

Decrements the reference count of a DBusMessage, freeing the message if the count reaches 0.

**Definition** dbus-message.c:1735

dbus_message_iter_get_array_len

int dbus_message_iter_get_array_len(DBusMessageIter \*iter)

Returns the number of bytes in the array as marshaled in the wire protocol.

**Definition** dbus-message.c:2458

dbus_message_new

DBusMessage \* dbus_message_new(int message_type)

Constructs a new message of the given message type.

**Definition** dbus-message.c:1334

dbus_set_error_from_message

dbus_bool_t dbus_set_error_from_message(DBusError \*error, DBusMessage \*message)

Sets a DBusError based on the contents of the given message.

**Definition** dbus-message.c:4059

dbus_message_iter_get_element_count

int dbus_message_iter_get_element_count(DBusMessageIter \*iter)

Returns the number of elements in the array-typed value pointed to by the iterator.

**Definition** dbus-message.c:2414

dbus_message_set_destination

dbus_bool_t dbus_message_set_destination(DBusMessage \*message, const char \*destination)

Sets the message's destination.

**Definition** dbus-message.c:3688

dbus_message_has_path

dbus_bool_t dbus_message_has_path(DBusMessage \*message, const char \*path)

Checks if the message has a particular object path.

**Definition** dbus-message.c:3383

dbus_message_has_member

dbus_bool_t dbus_message_has_member(DBusMessage \*message, const char \*member)

Checks if the message has an interface member.

**Definition** dbus-message.c:3598

dbus_message_get_args

dbus_bool_t dbus_message_get_args(DBusMessage \*message, DBusError \*error, int first_arg_type,...)

Gets arguments from a message given a variable argument list.

**Definition** dbus-message.c:2032

dbus_message_is_method_call

dbus_bool_t dbus_message_is_method_call(DBusMessage \*message, const char \*iface, const char \*method)

Checks whether the message is a method call with the given interface and member fields.

**Definition** dbus-message.c:3865

dbus_message_iter_get_fixed_array

void dbus_message_iter_get_fixed_array(DBusMessageIter \*iter, void \*value, int \*n_elements)

Reads a block of fixed-length values from the message iterator.

**Definition** dbus-message.c:2503

dbus_message_set_reply_serial

dbus_bool_t dbus_message_set_reply_serial(DBusMessage \*message, dbus_uint32_t reply_serial)

Sets the reply serial of a message (the serial of the message this is a reply to).

**Definition** dbus-message.c:1184

dbus_message_is_signal

dbus_bool_t dbus_message_is_signal(DBusMessage \*message, const char \*iface, const char \*signal_name)

Checks whether the message is a signal with the given interface and member fields.

**Definition** dbus-message.c:3893

dbus_message_get_signature

const char \* dbus_message_get_signature(DBusMessage \*message)

Gets the type signature of the message, i.e.

**Definition** dbus-message.c:3806

dbus_message_set_container_instance

dbus_bool_t dbus_message_set_container_instance(DBusMessage \*message, const char \*object_path)

Sets the container instance this message was sent from.

**Definition** dbus-message.c:4110

dbus_message_iter_close_container

dbus_bool_t dbus_message_iter_close_container(DBusMessageIter \*iter, DBusMessageIter \*sub)

Closes a container-typed value appended to the message; may write out more information to the message...

**Definition** dbus-message.c:3089

dbus_message_get_path_decomposed

dbus_bool_t dbus_message_get_path_decomposed(DBusMessage \*message, char \*\*\*path)

Gets the object path this message is being sent to (for DBUS_MESSAGE_TYPE_METHOD_CALL) or being emitt...

**Definition** dbus-message.c:3427

dbus_message_get_member

const char \* dbus_message_get_member(DBusMessage \*message)

Gets the interface member being invoked (DBUS_MESSAGE_TYPE_METHOD_CALL) or emitted (DBUS_MESSAGE_TYPE...

**Definition** dbus-message.c:3576

dbus_message_iter_init_append

void dbus_message_iter_init_append(DBusMessage \*message, DBusMessageIter \*iter)

Initializes a DBusMessageIter for appending arguments to the end of a message.

**Definition** dbus-message.c:2533

dbus_message_get_container_instance

const char \* dbus_message_get_container_instance(DBusMessage \*message)

Gets the container instance this message was sent from, or NULL if none.

**Definition** dbus-message.c:4136

\_dbus_decompose_path

dbus_bool_t \_dbus_decompose_path(const char \*data, int len, char \*\*\*path, int \*path_len)

Decompose an object path.

**Definition** dbus-object-tree.c:1247

DBUS_HEADER_FIELD_UNIX_FDS

\#define DBUS_HEADER_FIELD_UNIX_FDS

Header field code for the number of unix file descriptors associated with this message.

**Definition** dbus-protocol.h:304

DBUS_MESSAGE_TYPE_METHOD_CALL

\#define DBUS_MESSAGE_TYPE_METHOD_CALL

Message type of a method call message, see dbus_message_get_type()

**Definition** dbus-protocol.h:236

DBUS_HEADER_FIELD_PATH

\#define DBUS_HEADER_FIELD_PATH

Header field code for the path - the path is the object emitting a signal or the object receiving a m...

**Definition** dbus-protocol.h:272

DBUS_HEADER_FLAG_NO_REPLY_EXPECTED

\#define DBUS_HEADER_FLAG_NO_REPLY_EXPECTED

If set, this flag means that the sender of a message does not care about getting a reply,...

**Definition** dbus-protocol.h:251

DBUS_HEADER_FIELD_REPLY_SERIAL

\#define DBUS_HEADER_FIELD_REPLY_SERIAL

Header field code for a reply serial, used to match a DBUS_MESSAGE_TYPE_METHOD_RETURN message with th...

**Definition** dbus-protocol.h:286

DBUS_HEADER_FIELD_CONTAINER_INSTANCE

\#define DBUS_HEADER_FIELD_CONTAINER_INSTANCE

Header field code for the container instance that sent this message.

**Definition** dbus-protocol.h:308

DBUS_TYPE_SIGNATURE

\#define DBUS_TYPE_SIGNATURE

Type code marking a D-Bus type signature.

**Definition** dbus-protocol.h:112

DBUS_MAXIMUM_MESSAGE_UNIX_FDS

\#define DBUS_MAXIMUM_MESSAGE_UNIX_FDS

The maximum total number of unix fds in a message.

**Definition** dbus-protocol.h:220

DBUS_MAXIMUM_MESSAGE_LENGTH

\#define DBUS_MAXIMUM_MESSAGE_LENGTH

The maximum total message size including header and body; similar rationale to max array size.

**Definition** dbus-protocol.h:212

DBUS_HEADER_FIELD_INTERFACE

\#define DBUS_HEADER_FIELD_INTERFACE

Header field code for the interface containing a member (method or signal).

**Definition** dbus-protocol.h:276

DBUS_ERROR_INCONSISTENT_MESSAGE

\#define DBUS_ERROR_INCONSISTENT_MESSAGE

The message meta data does not match the payload.

**Definition** dbus-protocol.h:459

DBUS_HEADER_FIELD_MEMBER

\#define DBUS_HEADER_FIELD_MEMBER

Header field code for a member (method or signal).

**Definition** dbus-protocol.h:278

DBUS_MESSAGE_TYPE_ERROR

\#define DBUS_MESSAGE_TYPE_ERROR

Message type of an error reply message, see dbus_message_get_type()

**Definition** dbus-protocol.h:240

DBUS_TYPE_OBJECT_PATH

\#define DBUS_TYPE_OBJECT_PATH

Type code marking a D-Bus object path.

**Definition** dbus-protocol.h:108

DBUS_ERROR_NOT_SUPPORTED

\#define DBUS_ERROR_NOT_SUPPORTED

Requested operation isn't supported (like ENOSYS on UNIX).

**Definition** dbus-protocol.h:375

DBUS_HEADER_FIELD_SENDER

\#define DBUS_HEADER_FIELD_SENDER

Header field code for the sender of a message; usually initialized by the message bus.

**Definition** dbus-protocol.h:295

DBUS_HEADER_FIELD_SIGNATURE

\#define DBUS_HEADER_FIELD_SIGNATURE

Header field code for the type signature of a message.

**Definition** dbus-protocol.h:299

DBUS_MESSAGE_TYPE_METHOD_RETURN

\#define DBUS_MESSAGE_TYPE_METHOD_RETURN

Message type of a method return message, see dbus_message_get_type()

**Definition** dbus-protocol.h:238

DBUS_TYPE_VARIANT

\#define DBUS_TYPE_VARIANT

Type code marking a D-Bus variant type.

**Definition** dbus-protocol.h:126

DBUS_MAXIMUM_ARRAY_LENGTH

\#define DBUS_MAXIMUM_ARRAY_LENGTH

Max length of a marshaled array in bytes (64M, 2^26) We use signed int for lengths so must be INT_MAX...

**Definition** dbus-protocol.h:205

DBUS_TYPE_UNIX_FD

\#define DBUS_TYPE_UNIX_FD

Type code marking a unix file descriptor.

**Definition** dbus-protocol.h:116

DBUS_TYPE_BOOLEAN

\#define DBUS_TYPE_BOOLEAN

Type code marking a boolean.

**Definition** dbus-protocol.h:72

DBUS_MESSAGE_TYPE_SIGNAL

\#define DBUS_MESSAGE_TYPE_SIGNAL

Message type of a signal message, see dbus_message_get_type()

**Definition** dbus-protocol.h:242

DBUS_TYPE_STRING

\#define DBUS_TYPE_STRING

Type code marking a UTF-8 encoded, nul-terminated Unicode string.

**Definition** dbus-protocol.h:104

DBUS_HEADER_FLAG_NO_AUTO_START

\#define DBUS_HEADER_FLAG_NO_AUTO_START

If set, this flag means that even if the message bus knows how to start an owner for the destination ...

**Definition** dbus-protocol.h:258

DBUS_TYPE_ARRAY

\#define DBUS_TYPE_ARRAY

Type code marking a D-Bus array type.

**Definition** dbus-protocol.h:122

DBUS_HEADER_FLAG_ALLOW_INTERACTIVE_AUTHORIZATION

\#define DBUS_HEADER_FLAG_ALLOW_INTERACTIVE_AUTHORIZATION

If set on a method call, this flag means that the caller is prepared to wait for interactive authoriz...

**Definition** dbus-protocol.h:263

DBUS_TYPE_INVALID

\#define DBUS_TYPE_INVALID

Type code that is never equal to a legitimate type code.

**Definition** dbus-protocol.h:62

DBUS_HEADER_FIELD_ERROR_NAME

\#define DBUS_HEADER_FIELD_ERROR_NAME

Header field code for an error name (found in DBUS_MESSAGE_TYPE_ERROR messages).

**Definition** dbus-protocol.h:282

DBUS_TYPE_VARIANT_AS_STRING

\#define DBUS_TYPE_VARIANT_AS_STRING

DBUS_TYPE_VARIANT as a string literal instead of a int literal

**Definition** dbus-protocol.h:128

DBUS_MESSAGE_TYPE_INVALID

\#define DBUS_MESSAGE_TYPE_INVALID

This value is never a valid message type, see dbus_message_get_type()

**Definition** dbus-protocol.h:234

DBUS_ERROR_INVALID_ARGS

\#define DBUS_ERROR_INVALID_ARGS

Invalid arguments passed to a method call.

**Definition** dbus-protocol.h:397

DBUS_TYPE_DICT_ENTRY

\#define DBUS_TYPE_DICT_ENTRY

Type code used to represent a dict entry; however, this type code does not appear in type signatures,...

**Definition** dbus-protocol.h:145

DBUS_DICT_ENTRY_BEGIN_CHAR

\#define DBUS_DICT_ENTRY_BEGIN_CHAR

Code marking the start of a dict entry type in a type signature.

**Definition** dbus-protocol.h:166

DBUS_HEADER_FIELD_DESTINATION

\#define DBUS_HEADER_FIELD_DESTINATION

Header field code for the destination bus name of a message.

**Definition** dbus-protocol.h:290

DBUS_TYPE_STRUCT

\#define DBUS_TYPE_STRUCT

STRUCT and DICT_ENTRY are sort of special since their codes can't appear in a type string,...

**Definition** dbus-protocol.h:138

DBUS_TYPE_UINT32

\#define DBUS_TYPE_UINT32

Type code marking a 32-bit unsigned integer.

**Definition** dbus-protocol.h:88

DBUS_MINIMUM_HEADER_SIZE

\#define DBUS_MINIMUM_HEADER_SIZE

The smallest header size that can occur.

**Definition** dbus-protocol.h:352

\_dbus_counter_unref

void \_dbus_counter_unref(DBusCounter \*counter)

Decrements refcount of the counter and possibly finalizes the counter.

**Definition** dbus-resources.c:138

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

dbus_type_is_basic

dbus_bool_t dbus_type_is_basic(int typecode)

A "basic type" is a somewhat arbitrary concept, but the intent is to include those types that are ful...

**Definition** dbus-signature.c:324

dbus_type_is_fixed

dbus_bool_t dbus_type_is_fixed(int typecode)

Tells you whether values of this type can change length if you set them to some other value.

**Definition** dbus-signature.c:355

dbus_type_is_container

dbus_bool_t dbus_type_is_container(int typecode)

A "container type" can contain basic types, or nested container types.

**Definition** dbus-signature.c:300

\_dbus_string_set_length

dbus_bool_t \_dbus_string_set_length(DBusString \*str, int length)

Sets the length of a string.

**Definition** dbus-string.c:847

\_dbus_string_init

dbus_bool_t \_dbus_string_init(DBusString \*str)

Initializes a string.

**Definition** dbus-string.c:182

\_dbus_string_init_const

void \_dbus_string_init_const(DBusString \*str, const char \*value)

Initializes a constant string.

**Definition** dbus-string.c:197

\_dbus_string_copy

dbus_bool_t \_dbus_string_copy(const DBusString \*source, int start, DBusString \*dest, int insert_at)

Like \_dbus_string_move(), but does not delete the section of the source string that's copied to the d...

**Definition** dbus-string.c:1345

\_dbus_string_steal_data

dbus_bool_t \_dbus_string_steal_data(DBusString \*str, char \*\*data_return)

Like \_dbus_string_get_data(), but removes the gotten data from the original string.

**Definition** dbus-string.c:686

\_dbus_string_init_preallocated

dbus_bool_t \_dbus_string_init_preallocated(DBusString \*str, int allocate_size)

Initializes a string that can be up to the given allocation size before it has to realloc.

**Definition** dbus-string.c:139

\_dbus_string_init_const_len

void \_dbus_string_init_const_len(DBusString \*str, const char \*value, int len)

Initializes a constant string with a length.

**Definition** dbus-string.c:217

\_dbus_string_append_len

dbus_bool_t \_dbus_string_append_len(DBusString \*str, const char \*buffer, int len)

Appends block of bytes with the given length to a DBusString.

**Definition** dbus-string.c:1170

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_string_delete

void \_dbus_string_delete(DBusString \*str, int start, int len)

Deletes a segment of a DBusString with length len starting at start.

**Definition** dbus-string.c:1255

\_dbus_string_append_printf_valist

dbus_bool_t \_dbus_string_append_printf_valist(DBusString \*str, const char \*format, va_list args)

Appends a printf-style formatted string to the DBusString.

**Definition** dbus-string.c:1105

\_dbus_string_get_length

int \_dbus_string_get_length(const DBusString \*str)

Gets the length of a string (not including nul termination).

**Definition** dbus-string.c:784

\_dbus_string_get_const_data_len

const char \* \_dbus_string_get_const_data_len(const DBusString \*str, int start, int len)

const version of \_dbus_string_get_data_len().

**Definition** dbus-string.c:559

\_dbus_string_get_const_data

const char \* \_dbus_string_get_const_data(const DBusString \*str)

Gets the raw character buffer from a const string.

**Definition** dbus-string.c:513

\_dbus_string_get_byte

unsigned char \_dbus_string_get_byte(const DBusString \*str, int start)

Gets the byte at the given position.

**Definition** dbus-string.c:607

\_dbus_string_compact

dbus_bool_t \_dbus_string_compact(DBusString \*str, int max_waste)

Compacts the string to avoid wasted memory.

**Definition** dbus-string.c:420

\_dbus_string_copy_len

dbus_bool_t \_dbus_string_copy_len(const DBusString \*source, int start, int len, DBusString \*dest, int insert_at)

Like \_dbus_string_copy(), but can copy a segment from the middle of the source string.

**Definition** dbus-string.c:1437

\_dbus_close

dbus_bool_t \_dbus_close(int fd, DBusError \*error)

Closes a file descriptor.

**Definition** dbus-sysdeps-unix.c:3727

\_dbus_dup

int \_dbus_dup(int fd, DBusError \*error)

Duplicates a file descriptor.

**Definition** dbus-sysdeps-unix.c:3755

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

\_dbus_atomic_inc

dbus_int32_t \_dbus_atomic_inc(DBusAtomic \*atomic)

Atomically increments an integer.

**Definition** dbus-sysdeps-unix.c:3178

DBusCounter

Internals of DBusCounter.

**Definition** dbus-resources.c:57

DBusDataSlotAllocator

An allocator that tracks a set of slot IDs.

**Definition** dbus-dataslot.h:58

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusError::message

const char \* message

public error message field

**Definition** dbus-errors.h:53

DBusHeader

Message header data and some cached details of it.

**Definition** dbus-marshal-header.h:90

DBusHeader::data

DBusString data

Header network data, stored separately from body so we can independently realloc it.

**Definition** dbus-marshal-header.h:91

DBusList

A node in a linked list.

**Definition** dbus-list.h:37

DBusList::data

void \* data

Data stored at this element.

**Definition** dbus-list.h:40

DBusMessageIter_1_10_0

Layout of a DBusMessageIter on the stack in dbus 1.10.0.

**Definition** dbus-message.c:156

DBusMessageIter

DBusMessageIter struct; contains no public fields.

**Definition** dbus-message.h:64

DBusMessageLoader

Implementation details of DBusMessageLoader.

**Definition** dbus-message-private.h:63

DBusMessageLoader::max_message_size

long max_message_size

Maximum size of a message.

**Definition** dbus-message-private.h:70

DBusMessageLoader::max_message_unix_fds

long max_message_unix_fds

Maximum unix fds in a message.

**Definition** dbus-message-private.h:71

DBusMessageLoader::data

DBusString data

Buffered data.

**Definition** dbus-message-private.h:66

DBusMessageLoader::messages

DBusList \* messages

Complete messages.

**Definition** dbus-message-private.h:68

DBusMessageLoader::corrupted

unsigned int corrupted

We got broken data, and are no longer working.

**Definition** dbus-message-private.h:75

DBusMessageLoader::buffer_outstanding

unsigned int buffer_outstanding

Someone is using the buffer to read.

**Definition** dbus-message-private.h:77

DBusMessageLoader::corruption_reason

DBusValidity corruption_reason

why we were corrupted

**Definition** dbus-message-private.h:73

DBusMessageLoader::refcount

int refcount

Reference count.

**Definition** dbus-message-private.h:64

DBusMessageRealIter

Internals of DBusMessageIter.

**Definition** dbus-message.c:129

DBusMessageRealIter::u

union DBusMessageRealIter::@6 u

the type writer or reader that does all the work

DBusMessageRealIter::message

DBusMessage \* message

Message used.

**Definition** dbus-message.c:130

DBusMessageRealIter::iter_type

dbus_uint32_t iter_type

whether this is a reader or writer iter

**Definition** dbus-message.c:132

DBusMessageRealIter::sig_refcount

dbus_uint32_t sig_refcount

depth of open_signature()

**Definition** dbus-message.c:133

DBusMessageRealIter::writer

DBusTypeWriter writer

writer

**Definition** dbus-message.c:136

DBusMessageRealIter::changed_stamp

dbus_uint32_t changed_stamp

stamp to detect invalid iters

**Definition** dbus-message.c:131

DBusMessageRealIter::reader

DBusTypeReader reader

reader

**Definition** dbus-message.c:137

DBusMessage

Internals of DBusMessage.

**Definition** dbus-message-private.h:102

DBusMessage::header

DBusHeader header

Header network data and associated cache.

**Definition** dbus-message-private.h:105

DBusMessage::body

DBusString body

Body network data.

**Definition** dbus-message-private.h:107

DBusMessage::slot_list

DBusDataSlotList slot_list

Data stored by allocated integer ID.

**Definition** dbus-message-private.h:120

DBusMessage::refcount

DBusAtomic refcount

Reference count.

**Definition** dbus-message-private.h:103

DBusMessage::changed_stamp

dbus_uint32_t changed_stamp

Incremented when iterators are invalidated.

**Definition** dbus-message-private.h:118

DBusMessage::generation

int generation

\_dbus_current_generation when message was created

**Definition** dbus-message-private.h:123

DBusMessage::size_counter_delta

long size_counter_delta

Size we incremented the size counters by.

**Definition** dbus-message-private.h:116

DBusMessage::counters

DBusList \* counters

0-N DBusCounter used to track message size/unix fds.

**Definition** dbus-message-private.h:115

DBusMessage::in_cache

unsigned int in_cache

Has been "freed" since it's in the cache (this is a debug feature)

**Definition** dbus-message-private.h:112

DBusMessage::locked

unsigned int locked

Message being sent, no modifications allowed.

**Definition** dbus-message-private.h:109

DBusString

**Definition** dbus-string.h:47

DBusTypeReader

The type reader is an iterator for reading values from a block of values.

**Definition** dbus-marshal-recursive.h:42

DBusTypeReader::byte_order

dbus_uint32_t byte_order

byte order of the block

**Definition** dbus-marshal-recursive.h:47

DBusTypeWriter

The type writer is an iterator for writing to a block of values.

**Definition** dbus-marshal-recursive.h:68

DBusTypeWriter::byte_order

dbus_uint32_t byte_order

byte order to write values with

**Definition** dbus-marshal-recursive.h:71

DBusTypeWriter::type_str

DBusString \* type_str

where to write typecodes (or read type expectations)

**Definition** dbus-marshal-recursive.h:69

DBusTypeWriter::container_type

dbus_uint32_t container_type

what are we inside? (e.g.

**Definition** dbus-marshal-recursive.h:73

DBusVariant

An opaque data structure containing the serialized form of any single D-Bus message item,...

**Definition** dbus-message.c:5333

DBusBasicValue

A simple value union that lets you access bytes as if they were various types; useful when dealing wi...

**Definition** dbus-types.h:161

DBusBasicValue::u32

dbus_uint32_t u32

as int32

**Definition** dbus-types.h:166
