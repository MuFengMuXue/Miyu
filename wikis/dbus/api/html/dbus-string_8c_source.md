dbus-string.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-string.c String utility class (internal to D-Bus implementation)

3 \*

4 \* Copyright 2002-2007 Red Hat, Inc.

5 \* Copyright 2003 CodeFactory AB

6 \* Copyright 2003 Mark McLoughlin

7 \* Copyright 2004 Michael Meeks

8 \* Copyright 2006-2014 Ralf Habacker \<ralf.habacker@freenet.de\>

9 \* Copyright 2006-2018 Collabora Ltd.

10 \* Copyright 2007 Allison Lortie

11 \* Copyright 2011 Roberto Guido

12 \* Copyright 2013 Chengwei Yang / Intel

13 \*

14 \* SPDX-License-Identifier: AFL-2.1 OR GPL-2.0-or-later

15 \*

16 \* Licensed under the Academic Free License version 2.1

17 \*

18 \* This program is free software; you can redistribute it and/or modify

19 \* it under the terms of the GNU General Public License as published by

20 \* the Free Software Foundation; either version 2 of the License, or

21 \* (at your option) any later version.

22 \*

23 \* This program is distributed in the hope that it will be useful,

24 \* but WITHOUT ANY WARRANTY; without even the implied warranty of

25 \* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the

26 \* GNU General Public License for more details.

27 \*

28 \* You should have received a copy of the GNU General Public License

29 \* along with this program; if not, write to the Free Software

30 \* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

31 \*

32 \*/

33

34\#include \<config.h\>

35\#include "dbus-internals.h"

36\#include "dbus-string.h"

37/\* we allow a system header here, for speed/convenience \*/

38\#include \<string.h\>

39/\* for vsnprintf \*/

40\#include \<stdio.h\>

41\#define DBUS_CAN_USE_DBUS_STRING_PRIVATE 1

42\#include "dbus-string-private.h"

43\#include "dbus-marshal-basic.h" /\* probably should be removed by moving the usage of DBUS_TYPE

44 \* into the marshaling-related files

45 \*/

46

85static void

86fixup_alignment (DBusRealString \*real)

87{

88 unsigned char \*aligned;

89 unsigned char \*real_block;

90 unsigned int old_align_offset;

91

92 /\* we have to have extra space in real-\>allocated for the align offset and nul byte \*/

93 \_dbus_assert (real-\>len \<= real-\>allocated - \_DBUS_STRING_ALLOCATION_PADDING);

94

95 old_align_offset = real-\>align_offset;

96 real_block = real-\>str - old_align_offset;

97

98 aligned = \_DBUS_ALIGN_ADDRESS (real_block, 8);

99

100 real-\>align_offset = aligned - real_block;

101 real-\>str = aligned;

102

103 if (old_align_offset != real-\>align_offset)

104 {

105 /\* Here comes the suck \*/

106 memmove (real_block + real-\>align_offset,

107 real_block + old_align_offset,

108 real-\>len + 1);

109 }

110

111 \_dbus_assert (real-\>align_offset \< 8);

112 \_dbus_assert (\_DBUS_ALIGN_ADDRESS (real-\>str, 8) == real-\>str);

113}

114

115static void

116undo_alignment (DBusRealString \*real)

117{

118 if (real-\>align_offset != 0)

119 {

120 memmove (real-\>str - real-\>align_offset,

121 real-\>str,

122 real-\>len + 1);

123

124 real-\>str = real-\>str - real-\>align_offset;

125 real-\>align_offset = 0;

126 }

127}

128

138dbus_bool_t

139\_dbus_string_init_preallocated (DBusString \*str,

140 int allocate_size)

141{

142 DBusRealString \*real;

143

144 \_DBUS_STATIC_ASSERT (sizeof (DBusString) == sizeof (DBusRealString));

145

146 \_dbus_assert (str != NULL);

147

148 real = (DBusRealString\*) str;

149

150 /\* It's very important not to touch anything

151 \* other than real-\>str if we're going to fail,

152 \* since we also use this function to reset

153 \* an existing string, e.g. in \_dbus_string_steal_data()

154 \*/

155

156 real-\>str = dbus_malloc (\_DBUS_STRING_ALLOCATION_PADDING + allocate_size);

157 if (real-\>str == NULL)

158 return FALSE;

159

160 real-\>allocated = \_DBUS_STRING_ALLOCATION_PADDING + allocate_size;

161 real-\>len = 0;

162 real-\>str\[real-\>len\] = '\0';

163

164 real-\>constant = FALSE;

165 real-\>locked = FALSE;

166 real-\>valid = TRUE;

167 real-\>align_offset = 0;

168

169 fixup_alignment (real);

170

171 return TRUE;

172}

173

181dbus_bool_t

182\_dbus_string_init (DBusString \*str)

183{

184 return \_dbus_string_init_preallocated (str, 0);

185}

186

196void

197\_dbus_string_init_const (DBusString \*str,

198 const char \*value)

199{

200 \_dbus_assert (value != NULL);

201

202 \_dbus_string_init_const_len (str, value,

203 strlen (value));

204}

205

216void

217\_dbus_string_init_const_len (DBusString \*str,

218 const char \*value,

219 int len)

220{

221 DBusRealString \*real;

222

223 \_dbus_assert (str != NULL);

224 \_dbus_assert (len == 0 \|\| value != NULL);

225 \_dbus_assert (len \<= \_DBUS_STRING_MAX_LENGTH);

226 \_dbus_assert (len \>= 0);

227

228 real = (DBusRealString\*) str;

229

230 real-\>str = (unsigned char\*) value;

231 real-\>len = len;

232 real-\>allocated = real-\>len + \_DBUS_STRING_ALLOCATION_PADDING; /\* a lie, just to avoid special-case assertions... \*/

233 real-\>constant = TRUE;

234 real-\>locked = TRUE;

235 real-\>valid = TRUE;

236 real-\>align_offset = 0;

237

238 /\* We don't require const strings to be 8-byte aligned as the

239 \* memory is coming from elsewhere.

240 \*/

241}

242

253dbus_bool_t

254\_dbus_string_init_from_string(DBusString \*str,

255 const DBusString \*from)

256{

257 if (!\_dbus_string_init (str))

258 return FALSE;

259 if (!\_dbus_string_append (str, \_dbus_string_get_const_data (from)))

260 {

261 \_dbus_string_free (str);

262 return FALSE;

263 }

264 return TRUE;

265}

266

277void

278\_dbus_string_free (DBusString \*str)

279{

280 DBusRealString \*real = (DBusRealString\*) str;

281 /\* DBusRealString and DBusString have the same members in the same order,

282 \* just differently-named \*/

283 DBusRealString invalid = \_DBUS_STRING_INIT_INVALID;

284

285 /\* Allow for the \_DBUS_STRING_INIT_INVALID case \*/

286 if (real-\>str == NULL && real-\>len == 0 && real-\>allocated == 0 &&

287 !real-\>constant && !real-\>locked && !real-\>valid &&

288 real-\>align_offset == 0)

289 return;

290

291 DBUS_GENERIC_STRING_PREAMBLE (real);

292

293 if (real-\>constant)

294 goto wipe;

295

296 /\* so it's safe if @p str returned by a failed

297 \* \_dbus_string_init call

298 \* Bug: https://bugs.freedesktop.org/show_bug.cgi?id=65959

299 \*/

300 if (real-\>str == NULL)

301 goto wipe;

302

303 dbus_free (real-\>str - real-\>align_offset);

304

305wipe:

306 \*real = invalid;

307 real-\>valid = FALSE;

308}

309

310static dbus_bool_t

311compact (DBusRealString \*real,

312 int max_waste)

313{

314 unsigned char \*new_str;

315 int new_allocated;

316 int waste;

317

318 waste = real-\>allocated - (real-\>len + \_DBUS_STRING_ALLOCATION_PADDING);

319

320 if (waste \<= max_waste)

321 return TRUE;

322

323 new_allocated = real-\>len + \_DBUS_STRING_ALLOCATION_PADDING;

324

325 new_str = dbus_realloc (real-\>str - real-\>align_offset, new_allocated);

326 if (\_DBUS_UNLIKELY (new_str == NULL))

327 return FALSE;

328

329 real-\>str = new_str + real-\>align_offset;

330 real-\>allocated = new_allocated;

331 fixup_alignment (real);

332

333 return TRUE;

334}

335

336\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

337/\* Not using this feature at the moment,

338 \* so marked DBUS_ENABLE_EMBEDDED_TESTS-only

339 \*/

349void

350\_dbus_string_lock (DBusString \*str)

351{

352 DBUS_LOCKED_STRING_PREAMBLE (str); /\* can lock multiple times \*/

353

354 real-\>locked = TRUE;

355

356 /\* Try to realloc to avoid excess memory usage, since

357 \* we know we won't change the string further

358 \*/

359\#define MAX_WASTE 48

360 compact (real, MAX_WASTE);

361}

362\#endif /\* DBUS_ENABLE_EMBEDDED_TESTS \*/

363

364static dbus_bool_t

365reallocate_for_length (DBusRealString \*real,

366 int new_length)

367{

368 int new_allocated;

369 unsigned char \*new_str;

370

371 /\* at least double our old allocation to avoid O(n), avoiding

372 \* overflow

373 \*/

374 if (real-\>allocated \> (\_DBUS_STRING_MAX_LENGTH + \_DBUS_STRING_ALLOCATION_PADDING) / 2)

375 new_allocated = \_DBUS_STRING_MAX_LENGTH + \_DBUS_STRING_ALLOCATION_PADDING;

376 else

377 new_allocated = real-\>allocated \* 2;

378

379 /\* if you change the code just above here, run the tests without

380 \* the following assert-only hack before you commit

381 \*/

382 /\* This is keyed off asserts in addition to tests so when you

383 \* disable asserts to profile, you don't get this destroyer

384 \* of profiles.

385 \*/

386\#if defined (DBUS_ENABLE_EMBEDDED_TESTS) && !defined (DBUS_DISABLE_ASSERT)

387 new_allocated = 0; /\* ensure a realloc every time so that we go

388 \* through all malloc failure codepaths

389 \*/

390\#endif

391

392 /\* But be sure we always alloc at least space for the new length \*/

393 new_allocated = MAX (new_allocated,

394 new_length + \_DBUS_STRING_ALLOCATION_PADDING);

395

396 \_dbus_assert (new_allocated \>= real-\>allocated); /\* code relies on this \*/

397 new_str = dbus_realloc (real-\>str - real-\>align_offset, new_allocated);

398 if (\_DBUS_UNLIKELY (new_str == NULL))

399 return FALSE;

400

401 real-\>str = new_str + real-\>align_offset;

402 real-\>allocated = new_allocated;

403 fixup_alignment (real);

404

405 return TRUE;

406}

407

419dbus_bool_t

420\_dbus_string_compact (DBusString \*str,

421 int max_waste)

422{

423 DBUS_STRING_PREAMBLE (str);

424

425 return compact (real, max_waste);

426}

427

428static dbus_bool_t

429set_length (DBusRealString \*real,

430 int new_length)

431{

432 /\* Note, we are setting the length not including nul termination \*/

433

434 /\* exceeding max length is the same as failure to allocate memory \*/

435 if (\_DBUS_UNLIKELY (new_length \> \_DBUS_STRING_MAX_LENGTH))

436 return FALSE;

437 else if (new_length \> (real-\>allocated - \_DBUS_STRING_ALLOCATION_PADDING) &&

438 \_DBUS_UNLIKELY (!reallocate_for_length (real, new_length)))

439 return FALSE;

440 else

441 {

442 real-\>len = new_length;

443 real-\>str\[new_length\] = '\0';

444 return TRUE;

445 }

446}

447

448static dbus_bool_t

449open_gap (int len,

450 DBusRealString \*dest,

451 int insert_at)

452{

453 if (len == 0)

454 return TRUE;

455

456 if (len \> \_DBUS_STRING_MAX_LENGTH - dest-\>len)

457 return FALSE; /\* detected overflow of dest-\>len + len below \*/

458

459 if (!set_length (dest, dest-\>len + len))

460 return FALSE;

461

462 memmove (dest-\>str + insert_at + len,

463 dest-\>str + insert_at,

464 dest-\>len - len - insert_at);

465

466 return TRUE;

467}

468

475int

476\_dbus_string_get_allocated_size (const DBusString \*str)

477{

478 DBUS_CONST_STRING_PREAMBLE (str);

479

480 return real-\>allocated;

481}

482

483\#ifndef \_dbus_string_get_data

495char\*

496\_dbus_string_get_data (DBusString \*str)

497{

498 DBUS_STRING_PREAMBLE (str);

499

500 return (char\*) real-\>str;

501}

502\#endif /\* \_dbus_string_get_data \*/

503

504/\* only do the function if we don't have the macro \*/

505\#ifndef \_dbus_string_get_const_data

512const char\*

513\_dbus_string_get_const_data (const DBusString \*str)

514{

515 DBUS_CONST_STRING_PREAMBLE (str);

516

517 return (const char\*) real-\>str;

518}

519\#endif /\* \_dbus_string_get_const_data \*/

520

534char\*

535\_dbus_string_get_data_len (DBusString \*str,

536 int start,

537 int len)

538{

539 DBUS_STRING_PREAMBLE (str);

540 \_dbus_assert (start \>= 0);

541 \_dbus_assert (len \>= 0);

542 \_dbus_assert (start \<= real-\>len);

543 \_dbus_assert (len \<= real-\>len - start);

544

545 return (char\*) real-\>str + start;

546}

547

548/\* only do the function if we don't have the macro \*/

549\#ifndef \_dbus_string_get_const_data_len

558const char\*

559\_dbus_string_get_const_data_len (const DBusString \*str,

560 int start,

561 int len)

562{

563 DBUS_CONST_STRING_PREAMBLE (str);

564 \_dbus_assert (start \>= 0);

565 \_dbus_assert (len \>= 0);

566 \_dbus_assert (start \<= real-\>len);

567 \_dbus_assert (len \<= real-\>len - start);

568

569 return (const char\*) real-\>str + start;

570}

571\#endif /\* \_dbus_string_get_const_data_len \*/

572

573/\* only do the function if we don't have the macro \*/

574\#ifndef \_dbus_string_set_byte

582void

583\_dbus_string_set_byte (DBusString \*str,

584 int i,

585 unsigned char byte)

586{

587 DBUS_STRING_PREAMBLE (str);

588 \_dbus_assert (i \< real-\>len);

589 \_dbus_assert (i \>= 0);

590

591 real-\>str\[i\] = byte;

592}

593\#endif /\* \_dbus_string_set_byte \*/

594

595/\* only have the function if we didn't create a macro \*/

596\#ifndef \_dbus_string_get_byte

606unsigned char

607\_dbus_string_get_byte (const DBusString \*str,

608 int start)

609{

610 DBUS_CONST_STRING_PREAMBLE (str);

611 \_dbus_assert (start \<= real-\>len);

612 \_dbus_assert (start \>= 0);

613

614 return real-\>str\[start\];

615}

616\#endif /\* \_dbus_string_get_byte \*/

617

628dbus_bool_t

629\_dbus_string_insert_bytes (DBusString \*str,

630 int i,

631 int n_bytes,

632 unsigned char byte)

633{

634 DBUS_STRING_PREAMBLE (str);

635 \_dbus_assert (i \<= real-\>len);

636 \_dbus_assert (i \>= 0);

637 \_dbus_assert (n_bytes \>= 0);

638

639 if (n_bytes == 0)

640 return TRUE;

641

642 if (!open_gap (n_bytes, real, i))

643 return FALSE;

644

645 memset (real-\>str + i, byte, n_bytes);

646

647 return TRUE;

648}

649

658dbus_bool_t

659\_dbus_string_insert_byte (DBusString \*str,

660 int i,

661 unsigned char byte)

662{

663 DBUS_STRING_PREAMBLE (str);

664 \_dbus_assert (i \<= real-\>len);

665 \_dbus_assert (i \>= 0);

666

667 if (!open_gap (1, real, i))

668 return FALSE;

669

670 real-\>str\[i\] = byte;

671

672 return TRUE;

673}

674

685dbus_bool_t

686\_dbus_string_steal_data (DBusString \*str,

687 char \*\*data_return)

688{

689 DBUS_STRING_PREAMBLE (str);

690 \_dbus_assert (data_return != NULL);

691

692 undo_alignment (real);

693

694 \*data_return = (char\*) real-\>str;

695

696 /\* reset the string \*/

697 if (!\_dbus_string_init (str))

698 {

699 /\* hrm, put it back then \*/

700 real-\>str = (unsigned char\*) \*data_return;

701 \*data_return = NULL;

702 fixup_alignment (real);

703 return FALSE;

704 }

705

706 return TRUE;

707}

708

716dbus_bool_t

717\_dbus_string_copy_data (const DBusString \*str,

718 char \*\*data_return)

719{

720 DBUS_CONST_STRING_PREAMBLE (str);

721 \_dbus_assert (data_return != NULL);

722

723 \*data_return = dbus_malloc (real-\>len + 1);

724 if (\*data_return == NULL)

725 return FALSE;

726

727 memcpy (\*data_return, real-\>str, real-\>len + 1);

728

729 return TRUE;

730}

731

741void

742\_dbus_string_copy_to_buffer (const DBusString \*str,

743 char \*buffer,

744 int avail_len)

745{

746 DBUS_CONST_STRING_PREAMBLE (str);

747

748 \_dbus_assert (avail_len \>= 0);

749 \_dbus_assert (avail_len \>= real-\>len);

750

751 memcpy (buffer, real-\>str, real-\>len);

752}

753

763void

764\_dbus_string_copy_to_buffer_with_nul (const DBusString \*str,

765 char \*buffer,

766 int avail_len)

767{

768 DBUS_CONST_STRING_PREAMBLE (str);

769

770 \_dbus_assert (avail_len \>= 0);

771 \_dbus_assert (avail_len \> real-\>len);

772

773 memcpy (buffer, real-\>str, real-\>len+1);

774}

775

776/\* Only have the function if we don't have the macro \*/

777\#ifndef \_dbus_string_get_length

783int

784\_dbus_string_get_length (const DBusString \*str)

785{

786 DBUS_CONST_STRING_PREAMBLE (str);

787

788 return real-\>len;

789}

790\#endif /\* !\_dbus_string_get_length \*/

791

804dbus_bool_t

805\_dbus_string_lengthen (DBusString \*str,

806 int additional_length)

807{

808 DBUS_STRING_PREAMBLE (str);

809 \_dbus_assert (additional_length \>= 0);

810

811 if (\_DBUS_UNLIKELY (additional_length \> \_DBUS_STRING_MAX_LENGTH - real-\>len))

812 return FALSE; /\* would overflow \*/

813

814 return set_length (real,

815 real-\>len + additional_length);

816}

817

824void

825\_dbus_string_shorten (DBusString \*str,

826 int length_to_remove)

827{

828 DBUS_STRING_PREAMBLE (str);

829 \_dbus_assert (length_to_remove \>= 0);

830 \_dbus_assert (length_to_remove \<= real-\>len);

831

832 set_length (real,

833 real-\>len - length_to_remove);

834}

835

846dbus_bool_t

847\_dbus_string_set_length (DBusString \*str,

848 int length)

849{

850 DBUS_STRING_PREAMBLE (str);

851 \_dbus_assert (length \>= 0);

852

853 return set_length (real, length);

854}

855

856static dbus_bool_t

857align_insert_point_then_open_gap (DBusString \*str,

858 int \*insert_at_p,

859 int alignment,

860 int gap_size)

861{

862 unsigned long new_len; /\* ulong to avoid \_DBUS_ALIGN_VALUE overflow \*/

863 unsigned long gap_pos;

864 int insert_at;

865 int delta;

866 DBUS_STRING_PREAMBLE (str);

867 \_dbus_assert (alignment \>= 1);

868 \_dbus_assert (alignment \<= 8); /\* it has to be a bug if \> 8 \*/

869

870 insert_at = \*insert_at_p;

871

872 \_dbus_assert (insert_at \<= real-\>len);

873

874 gap_pos = \_DBUS_ALIGN_VALUE (insert_at, alignment);

875 new_len = real-\>len + (gap_pos - insert_at) + gap_size;

876

877 if (\_DBUS_UNLIKELY (new_len \> (unsigned long) \_DBUS_STRING_MAX_LENGTH))

878 return FALSE;

879

880 delta = new_len - real-\>len;

881 \_dbus_assert (delta \>= 0);

882

883 if (delta == 0) /\* only happens if gap_size == 0 and insert_at is aligned already \*/

884 {

885 \_dbus_assert (((unsigned long) \*insert_at_p) == gap_pos);

886 return TRUE;

887 }

888

889 if (\_DBUS_UNLIKELY (!open_gap (new_len - real-\>len,

890 real, insert_at)))

891 return FALSE;

892

893 /\* nul the padding if we had to add any padding \*/

894 if (gap_size \< delta)

895 {

896 memset (&real-\>str\[insert_at\], '\0',

897 gap_pos - insert_at);

898 }

899

900 \*insert_at_p = gap_pos;

901

902 return TRUE;

903}

904

905static dbus_bool_t

906align_length_then_lengthen (DBusString \*str,

907 int alignment,

908 int then_lengthen_by)

909{

910 int insert_at;

911

912 insert_at = \_dbus_string_get_length (str);

913

914 return align_insert_point_then_open_gap (str,

915 &insert_at,

916 alignment, then_lengthen_by);

917}

918

927dbus_bool_t

928\_dbus_string_align_length (DBusString \*str,

929 int alignment)

930{

931 return align_length_then_lengthen (str, alignment, 0);

932}

933

943dbus_bool_t

944\_dbus_string_alloc_space (DBusString \*str,

945 int extra_bytes)

946{

947 if (!\_dbus_string_lengthen (str, extra_bytes))

948 return FALSE;

949 \_dbus_string_shorten (str, extra_bytes);

950

951 return TRUE;

952}

953

954static dbus_bool_t

955append (DBusRealString \*real,

956 const char \*buffer,

957 int buffer_len)

958{

959 if (buffer_len == 0)

960 return TRUE;

961

962 if (!\_dbus_string_lengthen ((DBusString\*)real, buffer_len))

963 return FALSE;

964

965 memcpy (real-\>str + (real-\>len - buffer_len),

966 buffer,

967 buffer_len);

968

969 return TRUE;

970}

971

979dbus_bool_t

980\_dbus_string_append (DBusString \*str,

981 const char \*buffer)

982{

983 unsigned long buffer_len;

984

985 DBUS_STRING_PREAMBLE (str);

986 \_dbus_assert (buffer != NULL);

987

988 buffer_len = strlen (buffer);

989 if (buffer_len \> (unsigned long) \_DBUS_STRING_MAX_LENGTH)

990 return FALSE;

991

992 return append (real, buffer, buffer_len);

993}

994

1004dbus_bool_t

1005\_dbus_string_insert_2_aligned (DBusString \*str,

1006 int insert_at,

1007 const unsigned char octets\[2\])

1008{

1009 DBUS_STRING_PREAMBLE (str);

1010

1011 if (!align_insert_point_then_open_gap (str, &insert_at, 2, 2))

1012 return FALSE;

1013

1014 memcpy (real-\>str + insert_at, octets, 2);

1015

1016 return TRUE;

1017}

1018

1028dbus_bool_t

1029\_dbus_string_insert_4_aligned (DBusString \*str,

1030 int insert_at,

1031 const unsigned char octets\[4\])

1032{

1033 DBUS_STRING_PREAMBLE (str);

1034

1035 if (!align_insert_point_then_open_gap (str, &insert_at, 4, 4))

1036 return FALSE;

1037

1038 memcpy (real-\>str + insert_at, octets, 4);

1039

1040 return TRUE;

1041}

1042

1052dbus_bool_t

1053\_dbus_string_insert_8_aligned (DBusString \*str,

1054 int insert_at,

1055 const unsigned char octets\[8\])

1056{

1057 DBUS_STRING_PREAMBLE (str);

1058

1059 if (!align_insert_point_then_open_gap (str, &insert_at, 8, 8))

1060 return FALSE;

1061

1062 \_dbus_assert (\_DBUS_ALIGN_VALUE (insert_at, 8) == (unsigned) insert_at);

1063

1064 memcpy (real-\>str + insert_at, octets, 8);

1065

1066 return TRUE;

1067}

1068

1069

1080dbus_bool_t

1081\_dbus_string_insert_alignment (DBusString \*str,

1082 int \*insert_at,

1083 int alignment)

1084{

1085 DBUS_STRING_PREAMBLE (str);

1086

1087 if (!align_insert_point_then_open_gap (str, insert_at, alignment, 0))

1088 return FALSE;

1089

1090 \_dbus_assert (\_DBUS_ALIGN_VALUE (\*insert_at, alignment) == (unsigned) \*insert_at);

1091

1092 return TRUE;

1093}

1094

1104dbus_bool_t

1105\_dbus_string_append_printf_valist (DBusString \*str,

1106 const char \*format,

1107 va_list args)

1108{

1109 dbus_bool_t ret = FALSE;

1110 int len;

1111 va_list args_copy;

1112

1113 DBUS_STRING_PREAMBLE (str);

1114

1115 va_copy (args_copy, args);

1116

1117 /\* Measure the message length without terminating nul \*/

1118 len = \_dbus_printf_string_upper_bound (format, args);

1119

1120 if (len \< 0)

1121 goto out;

1122

1123 if (!\_dbus_string_lengthen (str, len))

1124 {

1125 goto out;

1126 }

1127

1128 vsprintf ((char\*) (real-\>str + (real-\>len - len)),

1129 format, args_copy);

1130 ret = TRUE;

1131

1132out:

1133 va_end (args_copy);

1134

1135 return ret;

1136}

1137

1146dbus_bool_t

1147\_dbus_string_append_printf (DBusString \*str,

1148 const char \*format,

1149 ...)

1150{

1151 va_list args;

1152 dbus_bool_t retval;

1153

1154 va_start (args, format);

1155 retval = \_dbus_string_append_printf_valist (str, format, args);

1156 va_end (args);

1157

1158 return retval;

1159}

1160

1169dbus_bool_t

1170\_dbus_string_append_len (DBusString \*str,

1171 const char \*buffer,

1172 int len)

1173{

1174 DBUS_STRING_PREAMBLE (str);

1175 \_dbus_assert (buffer != NULL);

1176 \_dbus_assert (len \>= 0);

1177

1178 return append (real, buffer, len);

1179}

1180

1189dbus_bool_t

1190\_dbus_string_append_byte (DBusString \*str,

1191 unsigned char byte)

1192{

1193 DBUS_STRING_PREAMBLE (str);

1194

1195 if (!set_length (real, real-\>len + 1))

1196 return FALSE;

1197

1198 real-\>str\[real-\>len-1\] = byte;

1199

1200 return TRUE;

1201}

1202

1212dbus_bool_t

1213\_dbus_string_append_strings (DBusString \*str, char \*\*strings, char separator)

1214{

1215 int i;

1216

1217 if (strings == NULL)

1218 return TRUE;

1219

1220 for (i = 0; strings\[i\]; i++)

1221 {

1222 if (i \> 0 && !\_dbus_string_append_byte (str, (unsigned char) separator))

1223 return FALSE;

1224

1225 if (!\_dbus_string_append (str, strings\[i\]))

1226 return FALSE;

1227 }

1228

1229 return TRUE;

1230}

1231

1232static void

1233delete (DBusRealString \*real,

1234 int start,

1235 int len)

1236{

1237 if (len == 0)

1238 return;

1239

1240 memmove (real-\>str + start, real-\>str + start + len, real-\>len - (start + len));

1241 real-\>len -= len;

1242 real-\>str\[real-\>len\] = '\0';

1243}

1244

1254void

1255\_dbus_string_delete (DBusString \*str,

1256 int start,

1257 int len)

1258{

1259 DBUS_STRING_PREAMBLE (str);

1260 \_dbus_assert (start \>= 0);

1261 \_dbus_assert (len \>= 0);

1262 \_dbus_assert (start \<= real-\>len);

1263 \_dbus_assert (len \<= real-\>len - start);

1264

1265 delete (real, start, len);

1266}

1267

1268static dbus_bool_t

1269copy (DBusRealString \*source,

1270 int start,

1271 int len,

1272 DBusRealString \*dest,

1273 int insert_at)

1274{

1275 if (len == 0)

1276 return TRUE;

1277

1278 if (!open_gap (len, dest, insert_at))

1279 return FALSE;

1280

1281 memmove (dest-\>str + insert_at,

1282 source-\>str + start,

1283 len);

1284

1285 return TRUE;

1286}

1287

1297\#define DBUS_STRING_COPY_PREAMBLE(source, start, dest, insert_at) \\

1298 DBusRealString \*real_source = (DBusRealString\*) source; \\

1299 DBusRealString \*real_dest = (DBusRealString\*) dest; \\

1300 \_dbus_assert ((source) != (dest)); \\

1301 DBUS_GENERIC_STRING_PREAMBLE (real_source); \\

1302 DBUS_GENERIC_STRING_PREAMBLE (real_dest); \\

1303 \_dbus_assert (!real_dest-\>constant); \\

1304 \_dbus_assert (!real_dest-\>locked); \\

1305 \_dbus_assert ((start) \>= 0); \\

1306 \_dbus_assert ((start) \<= real_source-\>len); \\

1307 \_dbus_assert ((insert_at) \>= 0); \\

1308 \_dbus_assert ((insert_at) \<= real_dest-\>len)

1309

1320dbus_bool_t

1321\_dbus_string_move (DBusString \*source,

1322 int start,

1323 DBusString \*dest,

1324 int insert_at)

1325{

1326 DBusRealString \*real_source = (DBusRealString\*) source;

1327 \_dbus_assert (start \<= real_source-\>len);

1328

1329 return \_dbus_string_move_len (source, start,

1330 real_source-\>len - start,

1331 dest, insert_at);

1332}

1333

1344dbus_bool_t

1345\_dbus_string_copy (const DBusString \*source,

1346 int start,

1347 DBusString \*dest,

1348 int insert_at)

1349{

1350 DBUS_STRING_COPY_PREAMBLE (source, start, dest, insert_at);

1351

1352 return copy (real_source, start,

1353 real_source-\>len - start,

1354 real_dest,

1355 insert_at);

1356}

1357

1369dbus_bool_t

1370\_dbus_string_move_len (DBusString \*source,

1371 int start,

1372 int len,

1373 DBusString \*dest,

1374 int insert_at)

1375

1376{

1377 DBUS_STRING_COPY_PREAMBLE (source, start, dest, insert_at);

1378 \_dbus_assert (len \>= 0);

1379 \_dbus_assert ((start + len) \<= real_source-\>len);

1380

1381

1382 if (len == 0)

1383 {

1384 return TRUE;

1385 }

1386 else if (start == 0 &&

1387 len == real_source-\>len &&

1388 real_dest-\>len == 0)

1389 {

1390 /\* Short-circuit moving an entire existing string to an empty string

1391 \* by just swapping the buffers.

1392 \*/

1393 /\* we assume -\>constant doesn't matter as you can't have

1394 \* a constant string involved in a move.

1395 \*/

1396\#define ASSIGN_DATA(a, b) do { \\

1397 (a)-\>str = (b)-\>str; \\

1398 (a)-\>len = (b)-\>len; \\

1399 (a)-\>allocated = (b)-\>allocated; \\

1400 (a)-\>align_offset = (b)-\>align_offset; \\

1401 } while (0)

1402

1403 DBusRealString tmp;

1404

1405 ASSIGN_DATA (&tmp, real_source);

1406 ASSIGN_DATA (real_source, real_dest);

1407 ASSIGN_DATA (real_dest, &tmp);

1408

1409 return TRUE;

1410 }

1411 else

1412 {

1413 if (!copy (real_source, start, len,

1414 real_dest,

1415 insert_at))

1416 return FALSE;

1417

1418 delete (real_source, start,

1419 len);

1420

1421 return TRUE;

1422 }

1423}

1424

1436dbus_bool_t

1437\_dbus_string_copy_len (const DBusString \*source,

1438 int start,

1439 int len,

1440 DBusString \*dest,

1441 int insert_at)

1442{

1443 DBUS_STRING_COPY_PREAMBLE (source, start, dest, insert_at);

1444 \_dbus_assert (len \>= 0);

1445 \_dbus_assert (start \<= real_source-\>len);

1446 \_dbus_assert (len \<= real_source-\>len - start);

1447

1448 return copy (real_source, start, len,

1449 real_dest,

1450 insert_at);

1451}

1452

1465dbus_bool_t

1466\_dbus_string_replace_len (const DBusString \*source,

1467 int start,

1468 int len,

1469 DBusString \*dest,

1470 int replace_at,

1471 int replace_len)

1472{

1473 DBUS_STRING_COPY_PREAMBLE (source, start, dest, replace_at);

1474 \_dbus_assert (len \>= 0);

1475 \_dbus_assert (start \<= real_source-\>len);

1476 \_dbus_assert (len \<= real_source-\>len - start);

1477 \_dbus_assert (replace_at \>= 0);

1478 \_dbus_assert (replace_at \<= real_dest-\>len);

1479 \_dbus_assert (replace_len \<= real_dest-\>len - replace_at);

1480

1481 if (len == replace_len)

1482 {

1483 memmove (real_dest-\>str + replace_at,

1484 real_source-\>str + start, len);

1485 }

1486 else if (len \< replace_len)

1487 {

1488 memmove (real_dest-\>str + replace_at,

1489 real_source-\>str + start, len);

1490 delete (real_dest, replace_at + len,

1491 replace_len - len);

1492 }

1493 else

1494 {

1495 int diff;

1496

1497 \_dbus_assert (len \> replace_len);

1498

1499 diff = len - replace_len;

1500

1501 /\* First of all we check if destination string can be enlarged as

1502 \* required, then we overwrite previous bytes

1503 \*/

1504

1505 if (!copy (real_source, start + replace_len, diff,

1506 real_dest, replace_at + replace_len))

1507 return FALSE;

1508

1509 memmove (real_dest-\>str + replace_at,

1510 real_source-\>str + start, replace_len);

1511 }

1512

1513 return TRUE;

1514}

1515

1528dbus_bool_t

1529\_dbus_string_split_on_byte (DBusString \*source,

1530 unsigned char byte,

1531 DBusString \*tail)

1532{

1533 int byte_position;

1534 char byte_string\[2\] = "";

1535 int head_length;

1536 int tail_length;

1537

1538 byte_string\[0\] = (char) byte;

1539

1540 if (!\_dbus_string_find (source, 0, byte_string, &byte_position))

1541 return FALSE;

1542

1543 head_length = byte_position;

1544 tail_length = \_dbus_string_get_length (source) - head_length - 1;

1545

1546 if (!\_dbus_string_move_len (source, byte_position + 1, tail_length,

1547 tail, 0))

1548 return FALSE;

1549

1550 /\* remove the trailing delimiter byte from the head now.

1551 \*/

1552 if (!\_dbus_string_set_length (source, head_length))

1553 return FALSE;

1554

1555 return TRUE;

1556}

1557

1558/\* Unicode macros and utf8_validate() from GLib Owen Taylor, Havoc

1559 \* Pennington, and Tom Tromey are the authors and authorized relicense.

1560 \*/

1561

1567\#define UTF8_COMPUTE(Char, Mask, Len) \\

1568 if (Char \< 128) \\

1569 { \\

1570 Len = 1; \\

1571 Mask = 0x7f; \\

1572 } \\

1573 else if ((Char & 0xe0) == 0xc0) \\

1574 { \\

1575 Len = 2; \\

1576 Mask = 0x1f; \\

1577 } \\

1578 else if ((Char & 0xf0) == 0xe0) \\

1579 { \\

1580 Len = 3; \\

1581 Mask = 0x0f; \\

1582 } \\

1583 else if ((Char & 0xf8) == 0xf0) \\

1584 { \\

1585 Len = 4; \\

1586 Mask = 0x07; \\

1587 } \\

1588 else if ((Char & 0xfc) == 0xf8) \\

1589 { \\

1590 Len = 5; \\

1591 Mask = 0x03; \\

1592 } \\

1593 else if ((Char & 0xfe) == 0xfc) \\

1594 { \\

1595 Len = 6; \\

1596 Mask = 0x01; \\

1597 } \\

1598 else \\

1599 { \\

1600 Len = 0; \\

1601 Mask = 0; \\

1602 }

1603

1608\#define UTF8_LENGTH(Char) \\

1609 ((Char) \< 0x80 ? 1 : \\

1610 ((Char) \< 0x800 ? 2 : \\

1611 ((Char) \< 0x10000 ? 3 : \\

1612 ((Char) \< 0x200000 ? 4 : \\

1613 ((Char) \< 0x4000000 ? 5 : 6)))))

1614

1624\#define UTF8_GET(Result, Chars, Count, Mask, Len) \\

1625 (Result) = (Chars)\[0\] & (Mask); \\

1626 for ((Count) = 1; (Count) \< (Len); ++(Count)) \\

1627 { \\

1628 if (((Chars)\[(Count)\] & 0xc0) != 0x80) \\

1629 { \\

1630 (Result) = -1; \\

1631 break; \\

1632 } \\

1633 (Result) \<\<= 6; \\

1634 (Result) \|= ((Chars)\[(Count)\] & 0x3f); \\

1635 }

1636

1647\#define UNICODE_VALID(Char) \\

1648 ((Char) \< 0x110000 && \\

1649 (((Char) & 0xFFFFF800) != 0xD800))

1650

1665dbus_bool_t

1666\_dbus_string_find (const DBusString \*str,

1667 int start,

1668 const char \*substr,

1669 int \*found)

1670{

1671 return \_dbus_string_find_to (str, start,

1672 ((const DBusRealString\*)str)-\>len,

1673 substr, found);

1674}

1675

1688dbus_bool_t

1689\_dbus_string_find_eol (const DBusString \*str,

1690 int start,

1691 int \*found,

1692 int \*found_len)

1693{

1694 int i;

1695

1696 DBUS_CONST_STRING_PREAMBLE (str);

1697 \_dbus_assert (start \<= real-\>len);

1698 \_dbus_assert (start \>= 0);

1699

1700 i = start;

1701 while (i \< real-\>len)

1702 {

1703 if (real-\>str\[i\] == '\r')

1704 {

1705 if ((i+1) \< real-\>len && real-\>str\[i+1\] == '\n') /\* "\r\n" \*/

1706 {

1707 if (found)

1708 \*found = i;

1709 if (found_len)

1710 \*found_len = 2;

1711 return TRUE;

1712 }

1713 else /\* only "\r" \*/

1714 {

1715 if (found)

1716 \*found = i;

1717 if (found_len)

1718 \*found_len = 1;

1719 return TRUE;

1720 }

1721 }

1722 else if (real-\>str\[i\] == '\n') /\* only "\n" \*/

1723 {

1724 if (found)

1725 \*found = i;

1726 if (found_len)

1727 \*found_len = 1;

1728 return TRUE;

1729 }

1730 ++i;

1731 }

1732

1733 if (found)

1734 \*found = real-\>len;

1735

1736 if (found_len)

1737 \*found_len = 0;

1738

1739 return FALSE;

1740}

1741

1758dbus_bool_t

1759\_dbus_string_find_to (const DBusString \*str,

1760 int start,

1761 int end,

1762 const char \*substr,

1763 int \*found)

1764{

1765 int i;

1766 DBUS_CONST_STRING_PREAMBLE (str);

1767 \_dbus_assert (substr != NULL);

1768 \_dbus_assert (start \<= real-\>len);

1769 \_dbus_assert (start \>= 0);

1770 \_dbus_assert (substr != NULL);

1771 \_dbus_assert (end \<= real-\>len);

1772 \_dbus_assert (start \<= end);

1773

1774 /\* we always "find" an empty string \*/

1775 if (\*substr == '\0')

1776 {

1777 if (found)

1778 \*found = start;

1779 return TRUE;

1780 }

1781

1782 i = start;

1783 while (i \< end)

1784 {

1785 if (real-\>str\[i\] == substr\[0\])

1786 {

1787 int j = i + 1;

1788

1789 while (j \< end)

1790 {

1791 if (substr\[j - i\] == '\0')

1792 break;

1793 else if (real-\>str\[j\] != substr\[j - i\])

1794 break;

1795

1796 ++j;

1797 }

1798

1799 if (substr\[j - i\] == '\0')

1800 {

1801 if (found)

1802 \*found = i;

1803 return TRUE;

1804 }

1805 }

1806

1807 ++i;

1808 }

1809

1810 if (found)

1811 \*found = end;

1812

1813 return FALSE;

1814}

1815

1826dbus_bool_t

1827\_dbus_string_find_blank (const DBusString \*str,

1828 int start,

1829 int \*found)

1830{

1831 int i;

1832 DBUS_CONST_STRING_PREAMBLE (str);

1833 \_dbus_assert (start \<= real-\>len);

1834 \_dbus_assert (start \>= 0);

1835

1836 i = start;

1837 while (i \< real-\>len)

1838 {

1839 if (real-\>str\[i\] == ' ' \|\|

1840 real-\>str\[i\] == '\t')

1841 {

1842 if (found)

1843 \*found = i;

1844 return TRUE;

1845 }

1846

1847 ++i;

1848 }

1849

1850 if (found)

1851 \*found = real-\>len;

1852

1853 return FALSE;

1854}

1855

1864void

1865\_dbus_string_skip_blank (const DBusString \*str,

1866 int start,

1867 int \*end)

1868{

1869 int i;

1870 DBUS_CONST_STRING_PREAMBLE (str);

1871 \_dbus_assert (start \<= real-\>len);

1872 \_dbus_assert (start \>= 0);

1873

1874 i = start;

1875 while (i \< real-\>len)

1876 {

1877 if (!DBUS_IS_ASCII_BLANK (real-\>str\[i\]))

1878 break;

1879

1880 ++i;

1881 }

1882

1883 \_dbus_assert (i == real-\>len \|\| !DBUS_IS_ASCII_BLANK (real-\>str\[i\]));

1884

1885 if (end)

1886 \*end = i;

1887}

1888

1889

1898void

1899\_dbus_string_skip_white (const DBusString \*str,

1900 int start,

1901 int \*end)

1902{

1903 int i;

1904 DBUS_CONST_STRING_PREAMBLE (str);

1905 \_dbus_assert (start \<= real-\>len);

1906 \_dbus_assert (start \>= 0);

1907

1908 i = start;

1909 while (i \< real-\>len)

1910 {

1911 if (!DBUS_IS_ASCII_WHITE (real-\>str\[i\]))

1912 break;

1913

1914 ++i;

1915 }

1916

1917 \_dbus_assert (i == real-\>len \|\| !(DBUS_IS_ASCII_WHITE (real-\>str\[i\])));

1918

1919 if (end)

1920 \*end = i;

1921}

1922

1931void

1932\_dbus_string_skip_white_reverse (const DBusString \*str,

1933 int end,

1934 int \*start)

1935{

1936 int i;

1937 DBUS_CONST_STRING_PREAMBLE (str);

1938 \_dbus_assert (end \<= real-\>len);

1939 \_dbus_assert (end \>= 0);

1940

1941 i = end;

1942 while (i \> 0)

1943 {

1944 if (!DBUS_IS_ASCII_WHITE (real-\>str\[i-1\]))

1945 break;

1946 --i;

1947 }

1948

1949 \_dbus_assert (i \>= 0 && (i == 0 \|\| !(DBUS_IS_ASCII_WHITE (real-\>str\[i-1\]))));

1950

1951 if (start)

1952 \*start = i;

1953}

1954

1970dbus_bool_t

1971\_dbus_string_pop_line (DBusString \*source,

1972 DBusString \*dest)

1973{

1974 int eol, eol_len;

1975

1976 \_dbus_string_set_length (dest, 0);

1977

1978 eol = 0;

1979 eol_len = 0;

1980 if (!\_dbus_string_find_eol (source, 0, &eol, &eol_len))

1981 {

1982 \_dbus_assert (eol == \_dbus_string_get_length (source));

1983 if (eol == 0)

1984 {

1985 /\* If there's no newline and source has zero length, we're done \*/

1986 return FALSE;

1987 }

1988 /\* otherwise, the last line of the file has no eol characters \*/

1989 }

1990

1991 /\* remember eol can be 0 if it's an empty line, but eol_len should not be zero also

1992 \* since find_eol returned TRUE

1993 \*/

1994

1995 if (!\_dbus_string_move_len (source, 0, eol + eol_len, dest, 0))

1996 return FALSE;

1997

1998 /\* remove line ending \*/

1999 if (!\_dbus_string_set_length (dest, eol))

2000 {

2001 \_dbus_assert_not_reached ("out of memory when shortening a string");

2002 return FALSE;

2003 }

2004

2005 return TRUE;

2006}

2007

2008\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

2015void

2016\_dbus_string_delete_first_word (DBusString \*str)

2017{

2018 int i;

2019

2020 if (\_dbus_string_find_blank (str, 0, &i))

2021 \_dbus_string_skip_blank (str, i, &i);

2022

2023 \_dbus_string_delete (str, 0, i);

2024}

2025\#endif

2026

2027\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

2033void

2034\_dbus_string_delete_leading_blanks (DBusString \*str)

2035{

2036 int i;

2037

2038 \_dbus_string_skip_blank (str, 0, &i);

2039

2040 if (i \> 0)

2041 \_dbus_string_delete (str, 0, i);

2042}

2043\#endif

2044

2050void

2051\_dbus_string_chop_white(DBusString \*str)

2052{

2053 int i;

2054

2055 \_dbus_string_skip_white (str, 0, &i);

2056

2057 if (i \> 0)

2058 \_dbus_string_delete (str, 0, i);

2059

2060 \_dbus_string_skip_white_reverse (str, \_dbus_string_get_length (str), &i);

2061

2062 \_dbus_string_set_length (str, i);

2063}

2064

2074dbus_bool_t

2075\_dbus_string_equal (const DBusString \*a,

2076 const DBusString \*b)

2077{

2078 const unsigned char \*ap;

2079 const unsigned char \*bp;

2080 const unsigned char \*a_end;

2081 const DBusRealString \*real_a = (const DBusRealString\*) a;

2082 const DBusRealString \*real_b = (const DBusRealString\*) b;

2083 DBUS_GENERIC_STRING_PREAMBLE (real_a);

2084 DBUS_GENERIC_STRING_PREAMBLE (real_b);

2085

2086 if (real_a-\>len != real_b-\>len)

2087 return FALSE;

2088

2089 ap = real_a-\>str;

2090 bp = real_b-\>str;

2091 a_end = real_a-\>str + real_a-\>len;

2092 while (ap != a_end)

2093 {

2094 if (\*ap != \*bp)

2095 return FALSE;

2096

2097 ++ap;

2098 ++bp;

2099 }

2100

2101 return TRUE;

2102}

2103

2117dbus_bool_t

2118\_dbus_string_equal_len (const DBusString \*a,

2119 const DBusString \*b,

2120 int len)

2121{

2122 const unsigned char \*ap;

2123 const unsigned char \*bp;

2124 const unsigned char \*a_end;

2125 const DBusRealString \*real_a = (const DBusRealString\*) a;

2126 const DBusRealString \*real_b = (const DBusRealString\*) b;

2127 DBUS_GENERIC_STRING_PREAMBLE (real_a);

2128 DBUS_GENERIC_STRING_PREAMBLE (real_b);

2129

2130 if (real_a-\>len != real_b-\>len &&

2131 (real_a-\>len \< len \|\| real_b-\>len \< len))

2132 return FALSE;

2133

2134 ap = real_a-\>str;

2135 bp = real_b-\>str;

2136 a_end = real_a-\>str + MIN (real_a-\>len, len);

2137 while (ap != a_end)

2138 {

2139 if (\*ap != \*bp)

2140 return FALSE;

2141

2142 ++ap;

2143 ++bp;

2144 }

2145

2146 return TRUE;

2147}

2148

2165dbus_bool_t

2166\_dbus_string_equal_substring (const DBusString \*a,

2167 int a_start,

2168 int a_len,

2169 const DBusString \*b,

2170 int b_start)

2171{

2172 const unsigned char \*ap;

2173 const unsigned char \*bp;

2174 const unsigned char \*a_end;

2175 const DBusRealString \*real_a = (const DBusRealString\*) a;

2176 const DBusRealString \*real_b = (const DBusRealString\*) b;

2177 DBUS_GENERIC_STRING_PREAMBLE (real_a);

2178 DBUS_GENERIC_STRING_PREAMBLE (real_b);

2179 \_dbus_assert (a_start \>= 0);

2180 \_dbus_assert (a_len \>= 0);

2181 \_dbus_assert (a_start \<= real_a-\>len);

2182 \_dbus_assert (a_len \<= real_a-\>len - a_start);

2183 \_dbus_assert (b_start \>= 0);

2184 \_dbus_assert (b_start \<= real_b-\>len);

2185

2186 if (a_len \> real_b-\>len - b_start)

2187 return FALSE;

2188

2189 ap = real_a-\>str + a_start;

2190 bp = real_b-\>str + b_start;

2191 a_end = ap + a_len;

2192 while (ap != a_end)

2193 {

2194 if (\*ap != \*bp)

2195 return FALSE;

2196

2197 ++ap;

2198 ++bp;

2199 }

2200

2201 \_dbus_assert (bp \<= (real_b-\>str + real_b-\>len));

2202

2203 return TRUE;

2204}

2205

2213dbus_bool_t

2214\_dbus_string_equal_c_str (const DBusString \*a,

2215 const char \*c_str)

2216{

2217 const unsigned char \*ap;

2218 const unsigned char \*bp;

2219 const unsigned char \*a_end;

2220 const DBusRealString \*real_a = (const DBusRealString\*) a;

2221 DBUS_GENERIC_STRING_PREAMBLE (real_a);

2222 \_dbus_assert (c_str != NULL);

2223

2224 ap = real_a-\>str;

2225 bp = (const unsigned char\*) c_str;

2226 a_end = real_a-\>str + real_a-\>len;

2227 while (ap != a_end && \*bp)

2228 {

2229 if (\*ap != \*bp)

2230 return FALSE;

2231

2232 ++ap;

2233 ++bp;

2234 }

2235

2236 if (ap != a_end \|\| \*bp)

2237 return FALSE;

2238

2239 return TRUE;

2240}

2241

2249dbus_bool_t

2250\_dbus_string_starts_with_c_str (const DBusString \*a,

2251 const char \*c_str)

2252{

2253 const unsigned char \*ap;

2254 const unsigned char \*bp;

2255 const unsigned char \*a_end;

2256 const DBusRealString \*real_a = (const DBusRealString\*) a;

2257 DBUS_GENERIC_STRING_PREAMBLE (real_a);

2258 \_dbus_assert (c_str != NULL);

2259

2260 ap = real_a-\>str;

2261 bp = (const unsigned char\*) c_str;

2262 a_end = real_a-\>str + real_a-\>len;

2263 while (ap != a_end && \*bp)

2264 {

2265 if (\*ap != \*bp)

2266 return FALSE;

2267

2268 ++ap;

2269 ++bp;

2270 }

2271

2272 if (\*bp == '\0')

2273 return TRUE;

2274 else

2275 return FALSE;

2276}

2277

2287dbus_bool_t

2288\_dbus_string_starts_with_words_c_str (const DBusString \*a,

2289 const char \*c_str,

2290 char word_separator)

2291{

2292 char next_char;

2293 const char \*data;

2294 \_dbus_assert (c_str != NULL);

2295

2296 if (!\_dbus_string_starts_with_c_str (a, c_str))

2297 return FALSE;

2298

2299 data = \_dbus_string_get_const_data (a);

2300 next_char = data\[strlen (c_str)\];

2301 return next_char == '\0' \|\| next_char == word_separator;

2302}

2303

2312dbus_bool_t

2313\_dbus_string_append_byte_as_hex (DBusString \*str,

2314 unsigned char byte)

2315{

2316 const char hexdigits\[16\] = {

2317 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',

2318 'a', 'b', 'c', 'd', 'e', 'f'

2319 };

2320

2321 if (!\_dbus_string_append_byte (str,

2322 hexdigits\[(byte \>\> 4)\]))

2323 return FALSE;

2324

2325 if (!\_dbus_string_append_byte (str,

2326 hexdigits\[(byte & 0x0f)\]))

2327 {

2328 \_dbus_string_set_length (str,

2329 \_dbus_string_get_length (str) - 1);

2330 return FALSE;

2331 }

2332

2333 return TRUE;

2334}

2335

2336/\* Currently only used when embedded tests are enabled \*/

2337\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

2348dbus_bool_t

2349\_dbus_string_append_buffer_as_hex (DBusString \*str,

2350 void \*buf,

2351 int size)

2352{

2353 unsigned char \*p;

2354 int i;

2355

2356 \_dbus_assert (size \>= 0);

2357 \_dbus_assert (size == 0 \|\| buf != NULL);

2358

2359 p = (unsigned char \*) buf;

2360

2361 for (i = 0; i \< size; i++)

2362 {

2363 if (!\_dbus_string_append_byte_as_hex (str, p\[i\]))

2364 return FALSE;

2365 }

2366

2367 return TRUE;

2368}

2369\#endif

2370

2381dbus_bool_t

2382\_dbus_string_hex_encode (const DBusString \*source,

2383 int start,

2384 DBusString \*dest,

2385 int insert_at)

2386{

2387 DBusString result;

2388 const unsigned char \*p;

2389 const unsigned char \*end;

2390 dbus_bool_t retval;

2391

2392 \_dbus_assert (start \<= \_dbus_string_get_length (source));

2393

2394 if (!\_dbus_string_init (&result))

2395 return FALSE;

2396

2397 retval = FALSE;

2398

2399 p = (const unsigned char\*) \_dbus_string_get_const_data (source);

2400 end = p + \_dbus_string_get_length (source);

2401 p += start;

2402

2403 while (p != end)

2404 {

2405 if (!\_dbus_string_append_byte_as_hex (&result, \*p))

2406 goto out;

2407

2408 ++p;

2409 }

2410

2411 if (!\_dbus_string_move (&result, 0, dest, insert_at))

2412 goto out;

2413

2414 retval = TRUE;

2415

2416 out:

2417 \_dbus_string_free (&result);

2418 return retval;

2419}

2420

2431dbus_bool_t

2432\_dbus_string_hex_decode (const DBusString \*source,

2433 int start,

2434 int \*end_return,

2435 DBusString \*dest,

2436 int insert_at)

2437{

2438 DBusString result;

2439 const unsigned char \*p;

2440 const unsigned char \*end;

2441 dbus_bool_t retval;

2442 dbus_bool_t high_bits;

2443

2444 \_dbus_assert (start \<= \_dbus_string_get_length (source));

2445

2446 if (!\_dbus_string_init (&result))

2447 return FALSE;

2448

2449 retval = FALSE;

2450

2451 high_bits = TRUE;

2452 p = (const unsigned char\*) \_dbus_string_get_const_data (source);

2453 end = p + \_dbus_string_get_length (source);

2454 p += start;

2455

2456 while (p != end)

2457 {

2458 unsigned int val;

2459

2460 switch (\*p)

2461 {

2462 case '0':

2463 val = 0;

2464 break;

2465 case '1':

2466 val = 1;

2467 break;

2468 case '2':

2469 val = 2;

2470 break;

2471 case '3':

2472 val = 3;

2473 break;

2474 case '4':

2475 val = 4;

2476 break;

2477 case '5':

2478 val = 5;

2479 break;

2480 case '6':

2481 val = 6;

2482 break;

2483 case '7':

2484 val = 7;

2485 break;

2486 case '8':

2487 val = 8;

2488 break;

2489 case '9':

2490 val = 9;

2491 break;

2492 case 'a':

2493 case 'A':

2494 val = 10;

2495 break;

2496 case 'b':

2497 case 'B':

2498 val = 11;

2499 break;

2500 case 'c':

2501 case 'C':

2502 val = 12;

2503 break;

2504 case 'd':

2505 case 'D':

2506 val = 13;

2507 break;

2508 case 'e':

2509 case 'E':

2510 val = 14;

2511 break;

2512 case 'f':

2513 case 'F':

2514 val = 15;

2515 break;

2516 default:

2517 goto done;

2518 }

2519

2520 if (high_bits)

2521 {

2522 if (!\_dbus_string_append_byte (&result,

2523 val \<\< 4))

2524 goto out;

2525 }

2526 else

2527 {

2528 int len;

2529 unsigned char b;

2530

2531 len = \_dbus_string_get_length (&result);

2532

2533 b = \_dbus_string_get_byte (&result, len - 1);

2534

2535 b \|= val;

2536

2537 \_dbus_string_set_byte (&result, len - 1, b);

2538 }

2539

2540 high_bits = !high_bits;

2541

2542 ++p;

2543 }

2544

2545 done:

2546 if (!\_dbus_string_move (&result, 0, dest, insert_at))

2547 goto out;

2548

2549 if (end_return)

2550 \*end_return = p - (const unsigned char\*) \_dbus_string_get_const_data (source);

2551

2552 retval = TRUE;

2553

2554 out:

2555 \_dbus_string_free (&result);

2556 return retval;

2557}

2558

2572dbus_bool_t

2573\_dbus_string_validate_ascii (const DBusString \*str,

2574 int start,

2575 int len)

2576{

2577 const unsigned char \*s;

2578 const unsigned char \*end;

2579 DBUS_CONST_STRING_PREAMBLE (str);

2580 \_dbus_assert (start \>= 0);

2581 \_dbus_assert (start \<= real-\>len);

2582 \_dbus_assert (len \>= 0);

2583

2584 if (len \> real-\>len - start)

2585 return FALSE;

2586

2587 s = real-\>str + start;

2588 end = s + len;

2589 while (s != end)

2590 {

2591 if (\_DBUS_UNLIKELY (!\_DBUS_ISASCII (\*s)))

2592 return FALSE;

2593

2594 ++s;

2595 }

2596

2597 return TRUE;

2598}

2599

2607void

2608\_dbus_string_tolower_ascii (const DBusString \*str,

2609 int start,

2610 int len)

2611{

2612 unsigned char \*s;

2613 unsigned char \*end;

2614 DBUS_STRING_PREAMBLE (str);

2615 \_dbus_assert (start \>= 0);

2616 \_dbus_assert (start \<= real-\>len);

2617 \_dbus_assert (len \>= 0);

2618 \_dbus_assert (len \<= real-\>len - start);

2619

2620 s = real-\>str + start;

2621 end = s + len;

2622

2623 while (s != end)

2624 {

2625 if (\*s \>= 'A' && \*s \<= 'Z')

2626 \*s += 'a' - 'A';

2627 ++s;

2628 }

2629}

2630

2638void

2639\_dbus_string_toupper_ascii (const DBusString \*str,

2640 int start,

2641 int len)

2642{

2643 unsigned char \*s;

2644 unsigned char \*end;

2645 DBUS_STRING_PREAMBLE (str);

2646 \_dbus_assert (start \>= 0);

2647 \_dbus_assert (start \<= real-\>len);

2648 \_dbus_assert (len \>= 0);

2649 \_dbus_assert (len \<= real-\>len - start);

2650

2651 s = real-\>str + start;

2652 end = s + len;

2653

2654 while (s != end)

2655 {

2656 if (\*s \>= 'a' && \*s \<= 'z')

2657 \*s += 'A' - 'a';

2658 ++s;

2659 }

2660}

2661

2677dbus_bool_t

2678\_dbus_string_validate_utf8 (const DBusString \*str,

2679 int start,

2680 int len)

2681{

2682 const unsigned char \*p;

2683 const unsigned char \*end;

2684 DBUS_CONST_STRING_PREAMBLE (str);

2685 \_dbus_assert (start \>= 0);

2686 \_dbus_assert (start \<= real-\>len);

2687 \_dbus_assert (len \>= 0);

2688

2689 /\* we are doing \_DBUS_UNLIKELY() here which might be

2690 \* dubious in a generic library like GLib, but in D-Bus

2691 \* we know we're validating messages and that it would

2692 \* only be evil/broken apps that would have invalid

2693 \* UTF-8. Also, this function seems to be a performance

2694 \* bottleneck in profiles.

2695 \*/

2696

2697 if (\_DBUS_UNLIKELY (len \> real-\>len - start))

2698 return FALSE;

2699

2700 p = real-\>str + start;

2701 end = p + len;

2702

2703 while (p \< end)

2704 {

2705 int i, mask, char_len;

2706 dbus_unichar_t result;

2707

2708 /\* nul bytes considered invalid \*/

2709 if (\*p == '\0')

2710 break;

2711

2712 /\* Special-case ASCII; this makes us go a lot faster in

2713 \* D-Bus profiles where we are typically validating

2714 \* function names and such. We have to know that

2715 \* all following checks will pass for ASCII though,

2716 \* comments follow ...

2717 \*/

2718 if (\*p \< 128)

2719 {

2720 ++p;

2721 continue;

2722 }

2723

2724 UTF8_COMPUTE (\*p, mask, char_len);

2725

2726 if (\_DBUS_UNLIKELY (char_len == 0)) /\* ASCII: char_len == 1 \*/

2727 break;

2728

2729 /\* check that the expected number of bytes exists in the remaining length \*/

2730 if (\_DBUS_UNLIKELY ((end - p) \< char_len)) /\* ASCII: p \< end and char_len == 1 \*/

2731 break;

2732

2733 UTF8_GET (result, p, i, mask, char_len);

2734

2735 /\* Check for overlong UTF-8 \*/

2736 if (\_DBUS_UNLIKELY (UTF8_LENGTH (result) != char_len)) /\* ASCII: UTF8_LENGTH == 1 \*/

2737 break;

2738\#if 0

2739 /\* The UNICODE_VALID check below will catch this \*/

2740 if (\_DBUS_UNLIKELY (result == (dbus_unichar_t)-1)) /\* ASCII: result = ascii value \*/

2741 break;

2742\#endif

2743

2744 if (\_DBUS_UNLIKELY (!UNICODE_VALID (result))) /\* ASCII: always valid \*/

2745 break;

2746

2747 /\* UNICODE_VALID should have caught it \*/

2748 \_dbus_assert (result != (dbus_unichar_t)-1);

2749

2750 p += char_len;

2751 }

2752

2753 /\* See that we covered the entire length if a length was

2754 \* passed in

2755 \*/

2756 if (\_DBUS_UNLIKELY (p != end))

2757 return FALSE;

2758 else

2759 return TRUE;

2760}

2761

2775dbus_bool_t

2776\_dbus_string_validate_nul (const DBusString \*str,

2777 int start,

2778 int len)

2779{

2780 const unsigned char \*s;

2781 const unsigned char \*end;

2782 DBUS_CONST_STRING_PREAMBLE (str);

2783 \_dbus_assert (start \>= 0);

2784 \_dbus_assert (len \>= 0);

2785 \_dbus_assert (start \<= real-\>len);

2786

2787 if (len \> real-\>len - start)

2788 return FALSE;

2789

2790 s = real-\>str + start;

2791 end = s + len;

2792 while (s != end)

2793 {

2794 if (\_DBUS_UNLIKELY (\*s != '\0'))

2795 return FALSE;

2796 ++s;

2797 }

2798

2799 return TRUE;

2800}

2801

2807void

2808\_dbus_string_zero (DBusString \*str)

2809{

2810 DBUS_STRING_PREAMBLE (str);

2811

2812 memset (real-\>str - real-\>align_offset, '\0', real-\>allocated);

2813}

2816/\* tests are in dbus-string-util.c \*/

\_dbus_assert_not_reached

\#define \_dbus_assert_not_reached(explanation)

Aborts with an error message if called.

**Definition** dbus-internals.h:164

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

dbus_malloc

void \* dbus_malloc(size_t bytes)

Allocates the given number of bytes, as with standard malloc().

**Definition** dbus-memory.c:470

\_DBUS_STRING_MAX_LENGTH

\#define \_DBUS_STRING_MAX_LENGTH

The maximum length of a DBusString.

**Definition** dbus-string-private.h:71

DBUS_STRING_PREAMBLE

\#define DBUS_STRING_PREAMBLE(str)

Checks assertions about a string object that needs to be modifiable - may not be locked or const.

**Definition** dbus-string-private.h:95

DBUS_CONST_STRING_PREAMBLE

\#define DBUS_CONST_STRING_PREAMBLE(str)

Checks assertions about a string that may be const or locked.

**Definition** dbus-string-private.h:116

DBUS_GENERIC_STRING_PREAMBLE

\#define DBUS_GENERIC_STRING_PREAMBLE(real)

Checks a bunch of assertions about a string object.

**Definition** dbus-string-private.h:78

DBUS_IS_ASCII_BLANK

\#define DBUS_IS_ASCII_BLANK(c)

Checks for ASCII blank byte.

**Definition** dbus-string-private.h:123

DBUS_IS_ASCII_WHITE

\#define DBUS_IS_ASCII_WHITE(c)

Checks for ASCII whitespace byte.

**Definition** dbus-string-private.h:129

DBUS_LOCKED_STRING_PREAMBLE

\#define DBUS_LOCKED_STRING_PREAMBLE(str)

Checks assertions about a string object that may be locked but can't be const.

**Definition** dbus-string-private.h:107

\_dbus_string_set_length

dbus_bool_t \_dbus_string_set_length(DBusString \*str, int length)

Sets the length of a string.

**Definition** dbus-string.c:847

\_dbus_string_hex_decode

dbus_bool_t \_dbus_string_hex_decode(const DBusString \*source, int start, int \*end_return, DBusString \*dest, int insert_at)

Decodes a string from hex encoding.

**Definition** dbus-string.c:2432

\_dbus_string_append

dbus_bool_t \_dbus_string_append(DBusString \*str, const char \*buffer)

Appends a nul-terminated C-style string to a DBusString.

**Definition** dbus-string.c:980

\_dbus_string_insert_8_aligned

dbus_bool_t \_dbus_string_insert_8_aligned(DBusString \*str, int insert_at, const unsigned char octets\[8\])

Inserts 8 bytes aligned on an 8 byte boundary with any alignment padding initialized to 0.

**Definition** dbus-string.c:1053

\_dbus_string_validate_nul

dbus_bool_t \_dbus_string_validate_nul(const DBusString \*str, int start, int len)

Checks that the given range of the string is all nul bytes.

**Definition** dbus-string.c:2776

\_dbus_string_equal_substring

dbus_bool_t \_dbus_string_equal_substring(const DBusString \*a, int a_start, int a_len, const DBusString \*b, int b_start)

Tests two sub-parts of two DBusString for equality.

**Definition** dbus-string.c:2166

UNICODE_VALID

\#define UNICODE_VALID(Char)

Check whether a Unicode (5.2) char is in a valid range.

**Definition** dbus-string.c:1647

\_dbus_string_insert_alignment

dbus_bool_t \_dbus_string_insert_alignment(DBusString \*str, int \*insert_at, int alignment)

Inserts padding at \*insert_at such to align it to the given boundary.

**Definition** dbus-string.c:1081

UTF8_COMPUTE

\#define UTF8_COMPUTE(Char, Mask, Len)

computes length and mask of a unicode character

**Definition** dbus-string.c:1567

\_dbus_string_init

dbus_bool_t \_dbus_string_init(DBusString \*str)

Initializes a string.

**Definition** dbus-string.c:182

\_dbus_string_append_strings

dbus_bool_t \_dbus_string_append_strings(DBusString \*str, char \*\*strings, char separator)

Append vector with strings connected by separator.

**Definition** dbus-string.c:1213

\_dbus_string_init_const

void \_dbus_string_init_const(DBusString \*str, const char \*value)

Initializes a constant string.

**Definition** dbus-string.c:197

\_dbus_string_copy

dbus_bool_t \_dbus_string_copy(const DBusString \*source, int start, DBusString \*dest, int insert_at)

Like \_dbus_string_move(), but does not delete the section of the source string that's copied to the d...

**Definition** dbus-string.c:1345

\_dbus_string_find_eol

dbus_bool_t \_dbus_string_find_eol(const DBusString \*str, int start, int \*found, int \*found_len)

Finds end of line ("\r\n" or "\n") in the string, returning TRUE and filling in the byte index where ...

**Definition** dbus-string.c:1689

\_dbus_string_starts_with_c_str

dbus_bool_t \_dbus_string_starts_with_c_str(const DBusString \*a, const char \*c_str)

Checks whether a string starts with the given C string.

**Definition** dbus-string.c:2250

\_dbus_string_alloc_space

dbus_bool_t \_dbus_string_alloc_space(DBusString \*str, int extra_bytes)

Preallocate extra_bytes such that a future lengthening of the string by extra_bytes is guaranteed to ...

**Definition** dbus-string.c:944

\_dbus_string_steal_data

dbus_bool_t \_dbus_string_steal_data(DBusString \*str, char \*\*data_return)

Like \_dbus_string_get_data(), but removes the gotten data from the original string.

**Definition** dbus-string.c:686

\_dbus_string_skip_blank

void \_dbus_string_skip_blank(const DBusString \*str, int start, int \*end)

Skips blanks from start, storing the first non-blank in \*end (blank is space or tab).

**Definition** dbus-string.c:1865

\_dbus_string_init_preallocated

dbus_bool_t \_dbus_string_init_preallocated(DBusString \*str, int allocate_size)

Initializes a string that can be up to the given allocation size before it has to realloc.

**Definition** dbus-string.c:139

\_dbus_string_skip_white_reverse

void \_dbus_string_skip_white_reverse(const DBusString \*str, int end, int \*start)

Skips whitespace from end, storing the start index of the trailing whitespace in \*start.

**Definition** dbus-string.c:1932

\_dbus_string_init_from_string

dbus_bool_t \_dbus_string_init_from_string(DBusString \*str, const DBusString \*from)

Initializes a string from another string.

**Definition** dbus-string.c:254

\_dbus_string_split_on_byte

dbus_bool_t \_dbus_string_split_on_byte(DBusString \*source, unsigned char byte, DBusString \*tail)

Looks for the first occurance of a byte, deletes that byte, and moves everything after the byte to th...

**Definition** dbus-string.c:1529

\_dbus_string_find

dbus_bool_t \_dbus_string_find(const DBusString \*str, int start, const char \*substr, int \*found)

Finds the given substring in the string, returning TRUE and filling in the byte index where the subst...

**Definition** dbus-string.c:1666

\_dbus_string_get_data_len

char \* \_dbus_string_get_data_len(DBusString \*str, int start, int len)

Gets a sub-portion of the raw character buffer from the string.

**Definition** dbus-string.c:535

\_dbus_string_validate_utf8

dbus_bool_t \_dbus_string_validate_utf8(const DBusString \*str, int start, int len)

Checks that the given range of the string is valid UTF-8.

**Definition** dbus-string.c:2678

\_dbus_string_find_blank

dbus_bool_t \_dbus_string_find_blank(const DBusString \*str, int start, int \*found)

Finds a blank (space or tab) in the string.

**Definition** dbus-string.c:1827

\_dbus_string_init_const_len

void \_dbus_string_init_const_len(DBusString \*str, const char \*value, int len)

Initializes a constant string with a length.

**Definition** dbus-string.c:217

\_dbus_string_tolower_ascii

void \_dbus_string_tolower_ascii(const DBusString \*str, int start, int len)

Converts the given range of the string to lower case.

**Definition** dbus-string.c:2608

\_dbus_string_append_len

dbus_bool_t \_dbus_string_append_len(DBusString \*str, const char \*buffer, int len)

Appends block of bytes with the given length to a DBusString.

**Definition** dbus-string.c:1170

\_dbus_string_get_data

char \* \_dbus_string_get_data(DBusString \*str)

Gets the raw character buffer from the string.

**Definition** dbus-string.c:496

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_string_shorten

void \_dbus_string_shorten(DBusString \*str, int length_to_remove)

Makes a string shorter by the given number of bytes.

**Definition** dbus-string.c:825

\_dbus_string_delete

void \_dbus_string_delete(DBusString \*str, int start, int len)

Deletes a segment of a DBusString with length len starting at start.

**Definition** dbus-string.c:1255

\_dbus_string_copy_data

dbus_bool_t \_dbus_string_copy_data(const DBusString \*str, char \*\*data_return)

Copies the data from the string into a char\*.

**Definition** dbus-string.c:717

\_dbus_string_equal_c_str

dbus_bool_t \_dbus_string_equal_c_str(const DBusString \*a, const char \*c_str)

Checks whether a string is equal to a C string.

**Definition** dbus-string.c:2214

\_dbus_string_skip_white

void \_dbus_string_skip_white(const DBusString \*str, int start, int \*end)

Skips whitespace from start, storing the first non-whitespace in \*end.

**Definition** dbus-string.c:1899

\_dbus_string_pop_line

dbus_bool_t \_dbus_string_pop_line(DBusString \*source, DBusString \*dest)

Assigns a newline-terminated or \r\n-terminated line from the front of the string to the given dest s...

**Definition** dbus-string.c:1971

\_dbus_string_append_printf_valist

dbus_bool_t \_dbus_string_append_printf_valist(DBusString \*str, const char \*format, va_list args)

Appends a printf-style formatted string to the DBusString.

**Definition** dbus-string.c:1105

\_dbus_string_lengthen

dbus_bool_t \_dbus_string_lengthen(DBusString \*str, int additional_length)

Makes a string longer by the given number of bytes.

**Definition** dbus-string.c:805

\_dbus_string_zero

void \_dbus_string_zero(DBusString \*str)

Clears all allocated bytes in the string to zero.

**Definition** dbus-string.c:2808

UTF8_LENGTH

\#define UTF8_LENGTH(Char)

computes length of a unicode character in UTF-8

**Definition** dbus-string.c:1608

\_dbus_string_toupper_ascii

void \_dbus_string_toupper_ascii(const DBusString \*str, int start, int len)

Converts the given range of the string to upper case.

**Definition** dbus-string.c:2639

\_dbus_string_insert_bytes

dbus_bool_t \_dbus_string_insert_bytes(DBusString \*str, int i, int n_bytes, unsigned char byte)

Inserts a number of bytes of a given value at the given position.

**Definition** dbus-string.c:629

\_dbus_string_validate_ascii

dbus_bool_t \_dbus_string_validate_ascii(const DBusString \*str, int start, int len)

Checks that the given range of the string is valid ASCII with no nul bytes.

**Definition** dbus-string.c:2573

\_dbus_string_get_length

int \_dbus_string_get_length(const DBusString \*str)

Gets the length of a string (not including nul termination).

**Definition** dbus-string.c:784

\_dbus_string_append_byte

dbus_bool_t \_dbus_string_append_byte(DBusString \*str, unsigned char byte)

Appends a single byte to the string, returning FALSE if not enough memory.

**Definition** dbus-string.c:1190

\_dbus_string_chop_white

void \_dbus_string_chop_white(DBusString \*str)

Deletes leading and trailing whitespace.

**Definition** dbus-string.c:2051

\_dbus_string_starts_with_words_c_str

dbus_bool_t \_dbus_string_starts_with_words_c_str(const DBusString \*a, const char \*c_str, char word_separator)

Checks whether a string starts with the given C string, after which it ends or is separated from the ...

**Definition** dbus-string.c:2288

\_dbus_string_hex_encode

dbus_bool_t \_dbus_string_hex_encode(const DBusString \*source, int start, DBusString \*dest, int insert_at)

Encodes a string in hex, the way MD5 and SHA-1 are usually encoded.

**Definition** dbus-string.c:2382

DBUS_STRING_COPY_PREAMBLE

\#define DBUS_STRING_COPY_PREAMBLE(source, start, dest, insert_at)

Checks assertions for two strings we're copying a segment between, and declares real_source/real_dest...

**Definition** dbus-string.c:1297

\_dbus_string_append_printf

dbus_bool_t \_dbus_string_append_printf(DBusString \*str, const char \*format,...)

Appends a printf-style formatted string to the DBusString.

**Definition** dbus-string.c:1147

\_dbus_string_insert_byte

dbus_bool_t \_dbus_string_insert_byte(DBusString \*str, int i, unsigned char byte)

Inserts a single byte at the given position.

**Definition** dbus-string.c:659

UTF8_GET

\#define UTF8_GET(Result, Chars, Count, Mask, Len)

Gets a UTF-8 value.

**Definition** dbus-string.c:1624

\_dbus_string_get_const_data_len

const char \* \_dbus_string_get_const_data_len(const DBusString \*str, int start, int len)

const version of \_dbus_string_get_data_len().

**Definition** dbus-string.c:559

\_dbus_string_set_byte

void \_dbus_string_set_byte(DBusString \*str, int i, unsigned char byte)

Sets the value of the byte at the given position.

**Definition** dbus-string.c:583

\_dbus_string_move_len

dbus_bool_t \_dbus_string_move_len(DBusString \*source, int start, int len, DBusString \*dest, int insert_at)

Like \_dbus_string_move(), but can move a segment from the middle of the source string.

**Definition** dbus-string.c:1370

\_dbus_string_get_const_data

const char \* \_dbus_string_get_const_data(const DBusString \*str)

Gets the raw character buffer from a const string.

**Definition** dbus-string.c:513

\_dbus_string_get_allocated_size

int \_dbus_string_get_allocated_size(const DBusString \*str)

Returns the allocated size of the string.

**Definition** dbus-string.c:476

\_dbus_string_get_byte

unsigned char \_dbus_string_get_byte(const DBusString \*str, int start)

Gets the byte at the given position.

**Definition** dbus-string.c:607

\_dbus_string_copy_to_buffer_with_nul

void \_dbus_string_copy_to_buffer_with_nul(const DBusString \*str, char \*buffer, int avail_len)

Copies the contents of a DBusString into a different buffer.

**Definition** dbus-string.c:764

\_dbus_string_compact

dbus_bool_t \_dbus_string_compact(DBusString \*str, int max_waste)

Compacts the string to avoid wasted memory.

**Definition** dbus-string.c:420

\_dbus_string_equal_len

dbus_bool_t \_dbus_string_equal_len(const DBusString \*a, const DBusString \*b, int len)

Tests two DBusString for equality up to the given length.

**Definition** dbus-string.c:2118

\_dbus_string_move

dbus_bool_t \_dbus_string_move(DBusString \*source, int start, DBusString \*dest, int insert_at)

Moves the end of one string into another string.

**Definition** dbus-string.c:1321

\_dbus_string_equal

dbus_bool_t \_dbus_string_equal(const DBusString \*a, const DBusString \*b)

Tests two DBusString for equality.

**Definition** dbus-string.c:2075

\_dbus_string_insert_4_aligned

dbus_bool_t \_dbus_string_insert_4_aligned(DBusString \*str, int insert_at, const unsigned char octets\[4\])

Inserts 4 bytes aligned on a 4 byte boundary with any alignment padding initialized to 0.

**Definition** dbus-string.c:1029

\_dbus_string_insert_2_aligned

dbus_bool_t \_dbus_string_insert_2_aligned(DBusString \*str, int insert_at, const unsigned char octets\[2\])

Inserts 2 bytes aligned on a 2 byte boundary with any alignment padding initialized to 0.

**Definition** dbus-string.c:1005

\_dbus_string_append_byte_as_hex

dbus_bool_t \_dbus_string_append_byte_as_hex(DBusString \*str, unsigned char byte)

Appends a two-character hex digit to a string, where the hex digit has the value of the given byte.

**Definition** dbus-string.c:2313

\_dbus_string_align_length

dbus_bool_t \_dbus_string_align_length(DBusString \*str, int alignment)

Align the length of a string to a specific alignment (typically 4 or 8) by appending nul bytes to the...

**Definition** dbus-string.c:928

\_dbus_string_find_to

dbus_bool_t \_dbus_string_find_to(const DBusString \*str, int start, int end, const char \*substr, int \*found)

Finds the given substring in the string, up to a certain position, returning TRUE and filling in the ...

**Definition** dbus-string.c:1759

\_dbus_string_copy_len

dbus_bool_t \_dbus_string_copy_len(const DBusString \*source, int start, int len, DBusString \*dest, int insert_at)

Like \_dbus_string_copy(), but can copy a segment from the middle of the source string.

**Definition** dbus-string.c:1437

\_dbus_string_copy_to_buffer

void \_dbus_string_copy_to_buffer(const DBusString \*str, char \*buffer, int avail_len)

Copies the contents of a DBusString into a different buffer.

**Definition** dbus-string.c:742

\_dbus_string_replace_len

dbus_bool_t \_dbus_string_replace_len(const DBusString \*source, int start, int len, DBusString \*dest, int replace_at, int replace_len)

Replaces a segment of dest string with a segment of source string.

**Definition** dbus-string.c:1466

\_dbus_printf_string_upper_bound

int \_dbus_printf_string_upper_bound(const char \*format, va_list args)

Measure the length of the given format string and arguments, not including the terminating nul.

**Definition** dbus-sysdeps-unix.c:3959

DBusRealString

Internals of DBusString.

**Definition** dbus-string-private.h:46

DBusRealString::align_offset

unsigned int align_offset

str - align_offset is the actual malloc block

**Definition** dbus-string-private.h:53

DBusRealString::valid

unsigned int valid

DBusString is valid (initialized and not freed)

**Definition** dbus-string-private.h:52

DBusRealString::constant

unsigned int constant

String data is not owned by DBusString.

**Definition** dbus-string-private.h:50

DBusRealString::locked

unsigned int locked

DBusString has been locked and can't be changed.

**Definition** dbus-string-private.h:51

DBusRealString::str

unsigned char \* str

String data, plus nul termination.

**Definition** dbus-string-private.h:47

DBusRealString::allocated

int allocated

Allocated size of data.

**Definition** dbus-string-private.h:49

DBusRealString::len

int len

Length without nul.

**Definition** dbus-string-private.h:48

DBusString

**Definition** dbus-string.h:47
