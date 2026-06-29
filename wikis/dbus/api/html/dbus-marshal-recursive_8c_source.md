dbus-marshal-recursive.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-marshal-recursive.c Marshalling routines for recursive types

3 \*

4 \* Copyright (C) 2004, 2005 Red Hat, Inc.

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

27\#include "dbus-marshal-recursive.h"

28\#include "dbus-marshal-basic.h"

29\#include "dbus-signature.h"

30\#include "dbus-internals.h"

31

37static dbus_bool_t \_dbus_type_reader_greater_than (const DBusTypeReader \*lhs,

38 const DBusTypeReader \*rhs);

39

40static void \_dbus_type_writer_set_enabled (DBusTypeWriter \*writer,

41 dbus_bool_t enabled);

42static dbus_bool_t \_dbus_type_writer_write_reader_partial (DBusTypeWriter \*writer,

43 DBusTypeReader \*reader,

44 const DBusTypeReader \*start_after,

45 int start_after_new_pos,

46 int start_after_new_len,

47 DBusList \*\*fixups);

48

50\#define RECURSIVE_MARSHAL_READ_TRACE 0

51

53\#define RECURSIVE_MARSHAL_WRITE_TRACE 0

54

55static void

56free_fixups (DBusList \*\*fixups)

57{

58 DBusList \*link;

59

60 link = \_dbus_list_get_first_link (fixups);

61 while (link != NULL)

62 {

63 DBusList \*next;

64

65 next = \_dbus_list_get_next_link (fixups, link);

66

67 dbus_free (link-\>data);

68 \_dbus_list_free_link (link);

69

70 link = next;

71 }

72

73 \*fixups = NULL;

74}

75

76static void

77apply_and_free_fixups (DBusList \*\*fixups,

78 DBusTypeReader \*reader)

79{

80 DBusList \*link;

81

82\#if RECURSIVE_MARSHAL_WRITE_TRACE

83 if (\*fixups)

84 \_dbus_verbose (" %d FIXUPS to apply\n",

85 \_dbus_list_get_length (fixups));

86\#endif

87

88 link = \_dbus_list_get_first_link (fixups);

89 while (link != NULL)

90 {

91 DBusList \*next;

92

93 next = \_dbus_list_get_next_link (fixups, link);

94

95 if (reader)

96 {

97 DBusArrayLenFixup \*f;

98

99 f = link-\>data;

100

101\#if RECURSIVE_MARSHAL_WRITE_TRACE

102 \_dbus_verbose (" applying FIXUP to reader %p at pos %d new_len = %d old len %d\n",

103 reader, f-\>len_pos_in_reader, f-\>new_len,

104 \_dbus_marshal_read_uint32 (reader-\>value_str,

105 f-\>len_pos_in_reader,

106 reader-\>byte_order, NULL));

107\#endif

108

109 \_dbus_marshal_set_uint32 ((DBusString\*) reader-\>value_str,

110 f-\>len_pos_in_reader,

111 f-\>new_len,

112 reader-\>byte_order);

113 }

114

115 dbus_free (link-\>data);

116 \_dbus_list_free_link (link);

117

118 link = next;

119 }

120

121 \*fixups = NULL;

122}

123

127struct DBusTypeReaderClass

128{

129 const char \*name;

130 int id;

131 dbus_bool_t types_only;

132 void (\* recurse) (DBusTypeReader \*sub,

133 DBusTypeReader \*parent);

134 dbus_bool_t (\* check_finished) (const DBusTypeReader \*reader);

135 void (\* next) (DBusTypeReader \*reader,

136 int current_type);

137};

138

139static int

140element_type_get_alignment (const DBusString \*str,

141 int pos)

142{

143 return \_dbus_type_get_alignment (\_dbus_first_type_in_signature (str, pos));

144}

145

146static void

147reader_init (DBusTypeReader \*reader,

148 int byte_order,

149 const DBusString \*type_str,

150 int type_pos,

151 const DBusString \*value_str,

152 int value_pos)

153{

154 \_DBUS_ZERO (\*reader);

155 reader-\>byte_order = byte_order;

156 reader-\>finished = FALSE;

157 reader-\>type_str = type_str;

158 reader-\>type_pos = type_pos;

159 reader-\>value_str = value_str;

160 reader-\>value_pos = value_pos;

161}

162

163static void

164base_reader_recurse (DBusTypeReader \*sub,

165 DBusTypeReader \*parent)

166{

167 /\* point subreader at the same place as parent \*/

168 reader_init (sub,

169 parent-\>byte_order,

170 parent-\>type_str,

171 parent-\>type_pos,

172 parent-\>value_str,

173 parent-\>value_pos);

174}

175

176static void

177struct_or_dict_entry_types_only_reader_recurse (DBusTypeReader \*sub,

178 DBusTypeReader \*parent)

179{

180 base_reader_recurse (sub, parent);

181

182 \_dbus_assert (\_dbus_string_get_byte (sub-\>type_str,

183 sub-\>type_pos) == DBUS_STRUCT_BEGIN_CHAR \|\|

184 \_dbus_string_get_byte (sub-\>type_str,

185 sub-\>type_pos) == DBUS_DICT_ENTRY_BEGIN_CHAR);

186

187 sub-\>type_pos += 1;

188}

189

190static void

191struct_or_dict_entry_reader_recurse (DBusTypeReader \*sub,

192 DBusTypeReader \*parent)

193{

194 struct_or_dict_entry_types_only_reader_recurse (sub, parent);

195

196 /\* struct and dict entry have 8 byte alignment \*/

197 sub-\>value_pos = \_DBUS_ALIGN_VALUE (sub-\>value_pos, 8);

198}

199

200static void

201array_types_only_reader_recurse (DBusTypeReader \*sub,

202 DBusTypeReader \*parent)

203{

204 base_reader_recurse (sub, parent);

205

206 /\* point type_pos at the array element type \*/

207 sub-\>type_pos += 1;

208

209 /\* Init with values likely to crash things if misused \*/

210 sub-\>u.array.start_pos = \_DBUS_INT_MAX;

211 sub-\>array_len_offset = 7;

212}

213

216\#define ARRAY_READER_LEN_POS(reader) \\

217 ((reader)-\>u.array.start_pos - ((int)(reader)-\>array_len_offset) - 4)

218

219static int

220array_reader_get_array_len (const DBusTypeReader \*reader)

221{

222 dbus_uint32_t array_len;

223 int len_pos;

224

225 len_pos = ARRAY_READER_LEN_POS (reader);

226

227 \_dbus_assert (\_DBUS_ALIGN_VALUE (len_pos, 4) == (unsigned) len_pos);

228 array_len = \_dbus_unpack_uint32 (reader-\>byte_order,

229 \_dbus_string_get_const_udata_len (reader-\>value_str, len_pos, 4));

230

231\#if RECURSIVE_MARSHAL_READ_TRACE

232 \_dbus_verbose (" reader %p len_pos %d array len %u len_offset %d\n",

233 reader, len_pos, array_len, reader-\>array_len_offset);

234\#endif

235

236 \_dbus_assert (reader-\>u.array.start_pos - len_pos - 4 \< 8);

237

238 return array_len;

239}

240

241static void

242array_reader_recurse (DBusTypeReader \*sub,

243 DBusTypeReader \*parent)

244{

245 int alignment;

246 int len_pos;

247

248 array_types_only_reader_recurse (sub, parent);

249

250 sub-\>value_pos = \_DBUS_ALIGN_VALUE (sub-\>value_pos, 4);

251

252 len_pos = sub-\>value_pos;

253

254 sub-\>value_pos += 4; /\* for the length \*/

255

256 alignment = element_type_get_alignment (sub-\>type_str,

257 sub-\>type_pos);

258

259 sub-\>value_pos = \_DBUS_ALIGN_VALUE (sub-\>value_pos, alignment);

260

261 sub-\>u.array.start_pos = sub-\>value_pos;

262 \_dbus_assert ((sub-\>u.array.start_pos - (len_pos + 4)) \< 8); /\* only 3 bits in array_len_offset \*/

263 sub-\>array_len_offset = sub-\>u.array.start_pos - (len_pos + 4);

264

265\#if RECURSIVE_MARSHAL_READ_TRACE

266 \_dbus_verbose (" type reader %p array start = %d len_offset = %d array len = %d array element type = %s\n",

267 sub,

268 sub-\>u.array.start_pos,

269 sub-\>array_len_offset,

270 array_reader_get_array_len (sub),

271 \_dbus_type_to_string (\_dbus_first_type_in_signature (sub-\>type_str,

272 sub-\>type_pos)));

273\#endif

274}

275

276static void

277variant_reader_recurse (DBusTypeReader \*sub,

278 DBusTypeReader \*parent)

279{

280 int sig_len;

281 int contained_alignment;

282

283 base_reader_recurse (sub, parent);

284

285 /\* Variant is 1 byte sig length (without nul), signature with nul,

286 \* padding to 8-boundary, then values

287 \*/

288

289 sig_len = \_dbus_string_get_byte (sub-\>value_str, sub-\>value_pos);

290

291 sub-\>type_str = sub-\>value_str;

292 sub-\>type_pos = sub-\>value_pos + 1;

293

294 sub-\>value_pos = sub-\>type_pos + sig_len + 1;

295

296 contained_alignment = \_dbus_type_get_alignment (\_dbus_first_type_in_signature (sub-\>type_str,

297 sub-\>type_pos));

298

299 sub-\>value_pos = \_DBUS_ALIGN_VALUE (sub-\>value_pos, contained_alignment);

300

301\#if RECURSIVE_MARSHAL_READ_TRACE

302 \_dbus_verbose (" type reader %p variant containing '%s'\n",

303 sub,

304 \_dbus_string_get_const_data_len (sub-\>type_str,

305 sub-\>type_pos, 0));

306\#endif

307}

308

309/\* return true if no more elements remain \*/

310static dbus_bool_t

311array_reader_check_finished (const DBusTypeReader \*reader)

312{

313 int end_pos;

314

315 end_pos = reader-\>u.array.start_pos + array_reader_get_array_len (reader);

316

317 \_dbus_assert (reader-\>value_pos \<= end_pos);

318 \_dbus_assert (reader-\>value_pos \>= reader-\>u.array.start_pos);

319

320 return reader-\>value_pos == end_pos;

321}

322

323static void

324skip_one_complete_type (const DBusString \*type_str,

325 int \*type_pos)

326{

327 \_dbus_type_signature_next (\_dbus_string_get_const_data (type_str),

328 type_pos);

329}

330

339void

340\_dbus_type_signature_next (const char \*type_str,

341 int \*type_pos)

342{

343 const unsigned char \*p;

344 const unsigned char \*start;

345

346 \_dbus_assert (type_str != NULL);

347 \_dbus_assert (type_pos != NULL);

348

349 start = (const unsigned char \*)type_str;

350 p = start + \*type_pos;

351

352 \_dbus_assert (\*p != DBUS_STRUCT_END_CHAR);

353 \_dbus_assert (\*p != DBUS_DICT_ENTRY_END_CHAR);

354

355 while (\*p == DBUS_TYPE_ARRAY)

356 ++p;

357

358 \_dbus_assert (\*p != DBUS_STRUCT_END_CHAR);

359 \_dbus_assert (\*p != DBUS_DICT_ENTRY_END_CHAR);

360

361 if (\*p == DBUS_STRUCT_BEGIN_CHAR)

362 {

363 int depth;

364

365 depth = 1;

366

367 while (TRUE)

368 {

369 \_dbus_assert (\*p != DBUS_TYPE_INVALID);

370

371 ++p;

372

373 \_dbus_assert (\*p != DBUS_TYPE_INVALID);

374

375 if (\*p == DBUS_STRUCT_BEGIN_CHAR)

376 depth += 1;

377 else if (\*p == DBUS_STRUCT_END_CHAR)

378 {

379 depth -= 1;

380 if (depth == 0)

381 {

382 ++p;

383 break;

384 }

385 }

386 }

387 }

388 else if (\*p == DBUS_DICT_ENTRY_BEGIN_CHAR)

389 {

390 int depth;

391

392 depth = 1;

393

394 while (TRUE)

395 {

396 \_dbus_assert (\*p != DBUS_TYPE_INVALID);

397

398 ++p;

399

400 \_dbus_assert (\*p != DBUS_TYPE_INVALID);

401

402 if (\*p == DBUS_DICT_ENTRY_BEGIN_CHAR)

403 depth += 1;

404 else if (\*p == DBUS_DICT_ENTRY_END_CHAR)

405 {

406 depth -= 1;

407 if (depth == 0)

408 {

409 ++p;

410 break;

411 }

412 }

413 }

414 }

415 else

416 {

417 ++p;

418 }

419

420 \*type_pos = (int) (p - start);

421}

422

423static int

424find_len_of_complete_type (const DBusString \*type_str,

425 int type_pos)

426{

427 int end;

428

429 end = type_pos;

430

431 skip_one_complete_type (type_str, &end);

432

433 return end - type_pos;

434}

435

436static void

437base_reader_next (DBusTypeReader \*reader,

438 int current_type)

439{

440 switch (current_type)

441 {

442 case DBUS_TYPE_DICT_ENTRY:

443 case DBUS_TYPE_STRUCT:

444 case DBUS_TYPE_VARIANT:

445 /\* Scan forward over the entire container contents \*/

446 {

447 DBusTypeReader sub;

448

449 if (reader-\>klass-\>types_only && current_type == DBUS_TYPE_VARIANT)

450 ;

451 else

452 {

453 /\* Recurse into the struct or variant \*/

454 \_dbus_type_reader_recurse (reader, &sub);

455

456 /\* Skip everything in this subreader \*/

457 while (\_dbus_type_reader_next (&sub))

458 {

459 /\* nothing \*/;

460 }

461 }

462 if (!reader-\>klass-\>types_only)

463 reader-\>value_pos = sub.value_pos;

464

465 /\* Now we are at the end of this container; for variants, the

466 \* subreader's type_pos is totally inapplicable (it's in the

467 \* value string) but we know that we increment by one past the

468 \* DBUS_TYPE_VARIANT

469 \*/

470 if (current_type == DBUS_TYPE_VARIANT)

471 reader-\>type_pos += 1;

472 else

473 reader-\>type_pos = sub.type_pos;

474 }

475 break;

476

477 case DBUS_TYPE_ARRAY:

478 {

479 if (!reader-\>klass-\>types_only)

480 \_dbus_marshal_skip_array (reader-\>value_str,

481 \_dbus_first_type_in_signature (reader-\>type_str,

482 reader-\>type_pos + 1),

483 reader-\>byte_order,

484 &reader-\>value_pos);

485

486 skip_one_complete_type (reader-\>type_str, &reader-\>type_pos);

487 }

488 break;

489

490 default:

491 if (!reader-\>klass-\>types_only)

492 \_dbus_marshal_skip_basic (reader-\>value_str,

493 current_type, reader-\>byte_order,

494 &reader-\>value_pos);

495

496 reader-\>type_pos += 1;

497 break;

498 }

499}

500

501static void

502struct_reader_next (DBusTypeReader \*reader,

503 int current_type)

504{

505 int t;

506

507 base_reader_next (reader, current_type);

508

509 /\* for STRUCT containers we return FALSE at the end of the struct,

510 \* for INVALID we return FALSE at the end of the signature.

511 \* In both cases we arrange for get_current_type() to return INVALID

512 \* which is defined to happen iff we're at the end (no more next())

513 \*/

514 t = \_dbus_string_get_byte (reader-\>type_str, reader-\>type_pos);

515 if (t == DBUS_STRUCT_END_CHAR)

516 {

517 reader-\>type_pos += 1;

518 reader-\>finished = TRUE;

519 }

520}

521

522static void

523dict_entry_reader_next (DBusTypeReader \*reader,

524 int current_type)

525{

526 int t;

527

528 base_reader_next (reader, current_type);

529

530 /\* for STRUCT containers we return FALSE at the end of the struct,

531 \* for INVALID we return FALSE at the end of the signature.

532 \* In both cases we arrange for get_current_type() to return INVALID

533 \* which is defined to happen iff we're at the end (no more next())

534 \*/

535 t = \_dbus_string_get_byte (reader-\>type_str, reader-\>type_pos);

536 if (t == DBUS_DICT_ENTRY_END_CHAR)

537 {

538 reader-\>type_pos += 1;

539 reader-\>finished = TRUE;

540 }

541}

542

543static void

544array_types_only_reader_next (DBusTypeReader \*reader,

545 int current_type)

546{

547 /\* We have one "element" to be iterated over

548 \* in each array, which is its element type.

549 \* So the finished flag indicates whether we've

550 \* iterated over it yet or not.

551 \*/

552 reader-\>finished = TRUE;

553}

554

555static void

556array_reader_next (DBusTypeReader \*reader,

557 int current_type)

558{

559 /\* Skip one array element \*/

560 int end_pos;

561

562 end_pos = reader-\>u.array.start_pos + array_reader_get_array_len (reader);

563

564\#if RECURSIVE_MARSHAL_READ_TRACE

565 \_dbus_verbose (" reader %p array next START start_pos = %d end_pos = %d value_pos = %d current_type = %s\n",

566 reader,

567 reader-\>u.array.start_pos,

568 end_pos, reader-\>value_pos,

569 \_dbus_type_to_string (current_type));

570\#endif

571

572 \_dbus_assert (reader-\>value_pos \< end_pos);

573 \_dbus_assert (reader-\>value_pos \>= reader-\>u.array.start_pos);

574

575 switch (\_dbus_first_type_in_signature (reader-\>type_str,

576 reader-\>type_pos))

577 {

578 case DBUS_TYPE_DICT_ENTRY:

579 case DBUS_TYPE_STRUCT:

580 case DBUS_TYPE_VARIANT:

581 {

582 DBusTypeReader sub;

583

584 /\* Recurse into the struct or variant \*/

585 \_dbus_type_reader_recurse (reader, &sub);

586

587 /\* Skip everything in this element \*/

588 while (\_dbus_type_reader_next (&sub))

589 {

590 /\* nothing \*/;

591 }

592

593 /\* Now we are at the end of this element \*/

594 reader-\>value_pos = sub.value_pos;

595 }

596 break;

597

598 case DBUS_TYPE_ARRAY:

599 {

600 \_dbus_marshal_skip_array (reader-\>value_str,

601 \_dbus_first_type_in_signature (reader-\>type_str,

602 reader-\>type_pos + 1),

603 reader-\>byte_order,

604 &reader-\>value_pos);

605 }

606 break;

607

608 default:

609 {

610 \_dbus_marshal_skip_basic (reader-\>value_str,

611 current_type, reader-\>byte_order,

612 &reader-\>value_pos);

613 }

614 break;

615 }

616

617\#if RECURSIVE_MARSHAL_READ_TRACE

618 \_dbus_verbose (" reader %p array next END start_pos = %d end_pos = %d value_pos = %d current_type = %s\n",

619 reader,

620 reader-\>u.array.start_pos,

621 end_pos, reader-\>value_pos,

622 \_dbus_type_to_string (current_type));

623\#endif

624

625 \_dbus_assert (reader-\>value_pos \<= end_pos);

626

627 if (reader-\>value_pos == end_pos)

628 {

629 skip_one_complete_type (reader-\>type_str,

630 &reader-\>type_pos);

631 }

632}

633

634static const DBusTypeReaderClass body_reader_class = {

635 "body", 0,

636 FALSE,

637 NULL, /\* body is always toplevel, so doesn't get recursed into \*/

638 NULL,

639 base_reader_next

640};

641

642static const DBusTypeReaderClass body_types_only_reader_class = {

643 "body types", 1,

644 TRUE,

645 NULL, /\* body is always toplevel, so doesn't get recursed into \*/

646 NULL,

647 base_reader_next

648};

649

650static const DBusTypeReaderClass struct_reader_class = {

651 "struct", 2,

652 FALSE,

653 struct_or_dict_entry_reader_recurse,

654 NULL,

655 struct_reader_next

656};

657

658static const DBusTypeReaderClass struct_types_only_reader_class = {

659 "struct types", 3,

660 TRUE,

661 struct_or_dict_entry_types_only_reader_recurse,

662 NULL,

663 struct_reader_next

664};

665

666static const DBusTypeReaderClass dict_entry_reader_class = {

667 "dict_entry", 4,

668 FALSE,

669 struct_or_dict_entry_reader_recurse,

670 NULL,

671 dict_entry_reader_next

672};

673

674static const DBusTypeReaderClass dict_entry_types_only_reader_class = {

675 "dict_entry types", 5,

676 TRUE,

677 struct_or_dict_entry_types_only_reader_recurse,

678 NULL,

679 dict_entry_reader_next

680};

681

682static const DBusTypeReaderClass array_reader_class = {

683 "array", 6,

684 FALSE,

685 array_reader_recurse,

686 array_reader_check_finished,

687 array_reader_next

688};

689

690static const DBusTypeReaderClass array_types_only_reader_class = {

691 "array types", 7,

692 TRUE,

693 array_types_only_reader_recurse,

694 NULL,

695 array_types_only_reader_next

696};

697

698static const DBusTypeReaderClass variant_reader_class = {

699 "variant", 8,

700 FALSE,

701 variant_reader_recurse,

702 NULL,

703 base_reader_next

704};

705

706\#ifndef DBUS_DISABLE_ASSERT

707static const DBusTypeReaderClass \* const

708all_reader_classes\[\] = {

709 &body_reader_class,

710 &body_types_only_reader_class,

711 &struct_reader_class,

712 &struct_types_only_reader_class,

713 &dict_entry_reader_class,

714 &dict_entry_types_only_reader_class,

715 &array_reader_class,

716 &array_types_only_reader_class,

717 &variant_reader_class

718};

719\#endif

720

731void

732\_dbus_type_reader_init (DBusTypeReader \*reader,

733 int byte_order,

734 const DBusString \*type_str,

735 int type_pos,

736 const DBusString \*value_str,

737 int value_pos)

738{

739 reader_init (reader, byte_order, type_str, type_pos,

740 value_str, value_pos);

741

742 reader-\>klass = &body_reader_class;

743

744\#if RECURSIVE_MARSHAL_READ_TRACE

745 \_dbus_verbose (" type reader %p init type_pos = %d value_pos = %d remaining sig '%s'\n",

746 reader, reader-\>type_pos, reader-\>value_pos,

747 \_dbus_string_get_const_data_len (reader-\>type_str, reader-\>type_pos, 0));

748\#endif

749}

750

759void

760\_dbus_type_reader_init_types_only (DBusTypeReader \*reader,

761 const DBusString \*type_str,

762 int type_pos)

763{

764 reader_init (reader, DBUS_COMPILER_BYTE_ORDER /\* irrelevant \*/,

765 type_str, type_pos, NULL, \_DBUS_INT_MAX /\* crashes if we screw up \*/);

766

767 reader-\>klass = &body_types_only_reader_class;

768

769\#if RECURSIVE_MARSHAL_READ_TRACE

770 \_dbus_verbose (" type reader %p init types only type_pos = %d remaining sig '%s'\n",

771 reader, reader-\>type_pos,

772 \_dbus_string_get_const_data_len (reader-\>type_str, reader-\>type_pos, 0));

773\#endif

774}

775

784int

785\_dbus_type_reader_get_current_type (const DBusTypeReader \*reader)

786{

787 int t;

788

789 if (reader-\>finished \|\|

790 (reader-\>klass-\>check_finished &&

791 (\* reader-\>klass-\>check_finished) (reader)))

792 t = DBUS_TYPE_INVALID;

793 else

794 t = \_dbus_first_type_in_signature (reader-\>type_str,

795 reader-\>type_pos);

796

797 \_dbus_assert (t != DBUS_STRUCT_END_CHAR);

798 \_dbus_assert (t != DBUS_STRUCT_BEGIN_CHAR);

799 \_dbus_assert (t != DBUS_DICT_ENTRY_END_CHAR);

800 \_dbus_assert (t != DBUS_DICT_ENTRY_BEGIN_CHAR);

801

802\#if 0

803 \_dbus_verbose (" type reader %p current type_pos = %d type = %s\n",

804 reader, reader-\>type_pos,

805 \_dbus_type_to_string (t));

806\#endif

807

808 return t;

809}

810

819int

820\_dbus_type_reader_get_element_type (const DBusTypeReader \*reader)

821{

822 int element_type;

823

824 \_dbus_assert (\_dbus_type_reader_get_current_type (reader) == DBUS_TYPE_ARRAY);

825

826 element_type = \_dbus_first_type_in_signature (reader-\>type_str,

827 reader-\>type_pos + 1);

828

829 return element_type;

830}

831

836int

837\_dbus_type_reader_get_value_pos (const DBusTypeReader \*reader)

838{

839 return reader-\>value_pos;

840}

841

851void

852\_dbus_type_reader_read_raw (const DBusTypeReader \*reader,

853 const unsigned char \*\*value_location)

854{

855 \_dbus_assert (!reader-\>klass-\>types_only);

856

857 \*value_location = \_dbus_string_get_const_udata_len (reader-\>value_str,

858 reader-\>value_pos,

859 0);

860}

861

868void

869\_dbus_type_reader_read_basic (const DBusTypeReader \*reader,

870 void \*value)

871{

872 int t;

873

874 \_dbus_assert (!reader-\>klass-\>types_only);

875

876 t = \_dbus_type_reader_get_current_type (reader);

877

878 \_dbus_marshal_read_basic (reader-\>value_str,

879 reader-\>value_pos,

880 t, value,

881 reader-\>byte_order,

882 NULL);

883

884

885\#if RECURSIVE_MARSHAL_READ_TRACE

886 \_dbus_verbose (" type reader %p read basic type_pos = %d value_pos = %d remaining sig '%s'\n",

887 reader, reader-\>type_pos, reader-\>value_pos,

888 \_dbus_string_get_const_data_len (reader-\>type_str, reader-\>type_pos, 0));

889\#endif

890}

891

898int

899\_dbus_type_reader_get_array_length (const DBusTypeReader \*reader)

900{

901 \_dbus_assert (!reader-\>klass-\>types_only);

902 \_dbus_assert (reader-\>klass == &array_reader_class);

903

904 return array_reader_get_array_len (reader);

905}

906

922void

923\_dbus_type_reader_read_fixed_multi (const DBusTypeReader \*reader,

924 const void \*\*value,

925 int \*n_elements)

926{

927 int element_type;

928 int end_pos;

929 int remaining_len;

930 int alignment;

931 int total_len;

932

933 \_dbus_assert (!reader-\>klass-\>types_only);

934 \_dbus_assert (reader-\>klass == &array_reader_class);

935

936 element_type = \_dbus_first_type_in_signature (reader-\>type_str,

937 reader-\>type_pos);

938

939 \_dbus_assert (element_type != DBUS_TYPE_INVALID); /\* why we don't use get_current_type() \*/

940 \_dbus_assert (dbus_type_is_fixed (element_type));

941

942 alignment = \_dbus_type_get_alignment (element_type);

943

944 \_dbus_assert (reader-\>value_pos \>= reader-\>u.array.start_pos);

945

946 total_len = array_reader_get_array_len (reader);

947 end_pos = reader-\>u.array.start_pos + total_len;

948 remaining_len = end_pos - reader-\>value_pos;

949

950\#if RECURSIVE_MARSHAL_READ_TRACE

951 \_dbus_verbose ("end_pos %d total_len %d remaining_len %d value_pos %d\n",

952 end_pos, total_len, remaining_len, reader-\>value_pos);

953\#endif

954

955 \_dbus_assert (remaining_len \<= total_len);

956

957 if (remaining_len == 0)

958 \*value = NULL;

959 else

960 \*value = \_dbus_string_get_const_data_len (reader-\>value_str,

961 reader-\>value_pos,

962 remaining_len);

963

964 \*n_elements = remaining_len / alignment;

965 \_dbus_assert ((remaining_len % alignment) == 0);

966

967\#if RECURSIVE_MARSHAL_READ_TRACE

968 \_dbus_verbose (" type reader %p read fixed array type_pos = %d value_pos = %d remaining sig '%s'\n",

969 reader, reader-\>type_pos, reader-\>value_pos,

970 \_dbus_string_get_const_data_len (reader-\>type_str, reader-\>type_pos, 0));

971\#endif

972}

973

986void

987\_dbus_type_reader_recurse (DBusTypeReader \*reader,

988 DBusTypeReader \*sub)

989{

990 int t;

991 const DBusTypeReaderClass \*klass = NULL;

992

993 t = \_dbus_first_type_in_signature (reader-\>type_str, reader-\>type_pos);

994

995 switch (t)

996 {

997 case DBUS_TYPE_STRUCT:

998 if (reader-\>klass-\>types_only)

999 klass = &struct_types_only_reader_class;

1000 else

1001 klass = &struct_reader_class;

1002 break;

1003 case DBUS_TYPE_DICT_ENTRY:

1004 if (reader-\>klass-\>types_only)

1005 klass = &dict_entry_types_only_reader_class;

1006 else

1007 klass = &dict_entry_reader_class;

1008 break;

1009 case DBUS_TYPE_ARRAY:

1010 if (reader-\>klass-\>types_only)

1011 klass = &array_types_only_reader_class;

1012 else

1013 klass = &array_reader_class;

1014 break;

1015 case DBUS_TYPE_VARIANT:

1016 if (reader-\>klass-\>types_only)

1017 \_dbus_assert_not_reached ("can't recurse into variant typecode");

1018 else

1019 klass = &variant_reader_class;

1020 break;

1021 default:

1022 \_dbus_verbose ("recursing into type %s\n", \_dbus_type_to_string (t));

1023\#ifndef DBUS_DISABLE_CHECKS

1024 if (t == DBUS_TYPE_INVALID)

1025 \_dbus_warn_check_failed ("You can't recurse into an empty array or off the end of a message body");

1026\#endif /\* DBUS_DISABLE_CHECKS \*/

1027

1028 \_dbus_assert_not_reached ("don't yet handle recursing into this type");

1029 }

1030

1031 \_dbus_assert (klass != NULL);

1032 \_dbus_assert (klass == all_reader_classes\[klass-\>id\]);

1033

1034 (\* klass-\>recurse) (sub, reader);

1035 sub-\>klass = klass;

1036

1037\#if RECURSIVE_MARSHAL_READ_TRACE

1038 \_dbus_verbose (" type reader %p RECURSED type_pos = %d value_pos = %d remaining sig '%s'\n",

1039 sub, sub-\>type_pos, sub-\>value_pos,

1040 \_dbus_string_get_const_data_len (sub-\>type_str, sub-\>type_pos, 0));

1041\#endif

1042}

1043

1052dbus_bool_t

1053\_dbus_type_reader_next (DBusTypeReader \*reader)

1054{

1055 int t;

1056

1057 t = \_dbus_type_reader_get_current_type (reader);

1058

1059\#if RECURSIVE_MARSHAL_READ_TRACE

1060 \_dbus_verbose (" type reader %p START next() { type_pos = %d value_pos = %d remaining sig '%s' current_type = %s\n",

1061 reader, reader-\>type_pos, reader-\>value_pos,

1062 \_dbus_string_get_const_data_len (reader-\>type_str, reader-\>type_pos, 0),

1063 \_dbus_type_to_string (t));

1064\#endif

1065

1066 if (t == DBUS_TYPE_INVALID)

1067 return FALSE;

1068

1069 (\* reader-\>klass-\>next) (reader, t);

1070

1071\#if RECURSIVE_MARSHAL_READ_TRACE

1072 \_dbus_verbose (" type reader %p END next() type_pos = %d value_pos = %d remaining sig '%s' current_type = %s\n",

1073 reader, reader-\>type_pos, reader-\>value_pos,

1074 \_dbus_string_get_const_data_len (reader-\>type_str, reader-\>type_pos, 0),

1075 \_dbus_type_to_string (\_dbus_type_reader_get_current_type (reader)));

1076\#endif

1077

1078 return \_dbus_type_reader_get_current_type (reader) != DBUS_TYPE_INVALID;

1079}

1080

1092dbus_bool_t

1093\_dbus_type_reader_has_next (const DBusTypeReader \*reader)

1094{

1095 /\* Not efficient but works for now. \*/

1096 DBusTypeReader copy;

1097

1098 copy = \*reader;

1099 return \_dbus_type_reader_next (&copy);

1100}

1101

1123void

1124\_dbus_type_reader_get_signature (const DBusTypeReader \*reader,

1125 const DBusString \*\*str_p,

1126 int \*start_p,

1127 int \*len_p)

1128{

1129 \*str_p = reader-\>type_str;

1130 \*start_p = reader-\>type_pos;

1131 \*len_p = find_len_of_complete_type (reader-\>type_str, reader-\>type_pos);

1132}

1133

1134typedef struct

1135{

1136 DBusString replacement;

1137 int padding;

1138} ReplacementBlock;

1139

1140static dbus_bool_t

1141replacement_block_init (ReplacementBlock \*block,

1142 DBusTypeReader \*reader)

1143{

1144 if (!\_dbus_string_init (&block-\>replacement))

1145 return FALSE;

1146

1147 /\* % 8 is the padding to have the same align properties in

1148 \* our replacement string as we do at the position being replaced

1149 \*/

1150 block-\>padding = reader-\>value_pos % 8;

1151

1152 if (!\_dbus_string_lengthen (&block-\>replacement, block-\>padding))

1153 goto oom;

1154

1155 return TRUE;

1156

1157 oom:

1158 \_dbus_string_free (&block-\>replacement);

1159 return FALSE;

1160}

1161

1162static dbus_bool_t

1163replacement_block_replace (ReplacementBlock \*block,

1164 DBusTypeReader \*reader,

1165 const DBusTypeReader \*realign_root)

1166{

1167 DBusTypeWriter writer;

1168 DBusTypeReader realign_reader;

1169 DBusList \*fixups;

1170 int orig_len;

1171

1172 \_dbus_assert (realign_root != NULL);

1173

1174 orig_len = \_dbus_string_get_length (&block-\>replacement);

1175

1176 realign_reader = \*realign_root;

1177

1178\#if RECURSIVE_MARSHAL_WRITE_TRACE

1179 \_dbus_verbose ("INITIALIZING replacement block writer %p at value_pos %d\n",

1180 &writer, \_dbus_string_get_length (&block-\>replacement));

1181\#endif

1182 \_dbus_type_writer_init_values_only (&writer,

1183 realign_reader.byte_order,

1184 realign_reader.type_str,

1185 realign_reader.type_pos,

1186 &block-\>replacement,

1187 \_dbus_string_get_length (&block-\>replacement));

1188

1189 \_dbus_assert (realign_reader.value_pos \<= reader-\>value_pos);

1190

1191\#if RECURSIVE_MARSHAL_WRITE_TRACE

1192 \_dbus_verbose ("COPYING from reader at value_pos %d to writer %p starting after value_pos %d\n",

1193 realign_reader.value_pos, &writer, reader-\>value_pos);

1194\#endif

1195 fixups = NULL;

1196 if (!\_dbus_type_writer_write_reader_partial (&writer,

1197 &realign_reader,

1198 reader,

1199 block-\>padding,

1200 \_dbus_string_get_length (&block-\>replacement) - block-\>padding,

1201 &fixups))

1202 goto oom;

1203

1204\#if RECURSIVE_MARSHAL_WRITE_TRACE

1205 \_dbus_verbose ("REPLACEMENT at padding %d len %d\n", block-\>padding,

1206 \_dbus_string_get_length (&block-\>replacement) - block-\>padding);

1207 \_dbus_verbose_bytes_of_string (&block-\>replacement, block-\>padding,

1208 \_dbus_string_get_length (&block-\>replacement) - block-\>padding);

1209 \_dbus_verbose ("TO BE REPLACED at value_pos = %d (align pad %d) len %d realign_reader.value_pos %d\n",

1210 reader-\>value_pos, reader-\>value_pos % 8,

1211 realign_reader.value_pos - reader-\>value_pos,

1212 realign_reader.value_pos);

1213 \_dbus_verbose_bytes_of_string (reader-\>value_str,

1214 reader-\>value_pos,

1215 realign_reader.value_pos - reader-\>value_pos);

1216\#endif

1217

1218 /\* Move the replacement into position

1219 \* (realign_reader should now be at the end of the block to be replaced)

1220 \*/

1221 if (!\_dbus_string_replace_len (&block-\>replacement, block-\>padding,

1222 \_dbus_string_get_length (&block-\>replacement) - block-\>padding,

1223 (DBusString\*) reader-\>value_str,

1224 reader-\>value_pos,

1225 realign_reader.value_pos - reader-\>value_pos))

1226 goto oom;

1227

1228 /\* Process our fixups now that we can't have an OOM error \*/

1229 apply_and_free_fixups (&fixups, reader);

1230

1231 return TRUE;

1232

1233 oom:

1234 \_dbus_string_set_length (&block-\>replacement, orig_len);

1235 free_fixups (&fixups);

1236 return FALSE;

1237}

1238

1239static void

1240replacement_block_free (ReplacementBlock \*block)

1241{

1242 \_dbus_string_free (&block-\>replacement);

1243}

1244

1245/\* In the variable-length case, we have to fix alignment after we insert.

1246 \* The strategy is as follows:

1247 \*

1248 \* - pad a new string to have the same alignment as the

1249 \* start of the current basic value

1250 \* - write the new basic value

1251 \* - copy from the original reader to the new string,

1252 \* which will fix the alignment of types following

1253 \* the new value

1254 \* - this copy has to start at realign_root,

1255 \* but not really write anything until it

1256 \* passes the value being set

1257 \* - as an optimization, we can stop copying

1258 \* when the source and dest values are both

1259 \* on an 8-boundary, since we know all following

1260 \* padding and alignment will be identical

1261 \* - copy the new string back to the original

1262 \* string, replacing the relevant part of the

1263 \* original string

1264 \* - now any arrays in the original string that

1265 \* contained the replaced string may have the

1266 \* wrong length; so we have to fix that

1267 \*/

1268static dbus_bool_t

1269reader_set_basic_variable_length (DBusTypeReader \*reader,

1270 int current_type,

1271 const void \*value,

1272 const DBusTypeReader \*realign_root)

1273{

1274 dbus_bool_t retval;

1275 ReplacementBlock block;

1276 DBusTypeWriter writer;

1277

1278 \_dbus_assert (realign_root != NULL);

1279

1280 retval = FALSE;

1281

1282 if (!replacement_block_init (&block, reader))

1283 return FALSE;

1284

1285 /\* Write the new basic value \*/

1286\#if RECURSIVE_MARSHAL_WRITE_TRACE

1287 \_dbus_verbose ("INITIALIZING writer %p to write basic value at value_pos %d of replacement string\n",

1288 &writer, \_dbus_string_get_length (&block.replacement));

1289\#endif

1290 \_dbus_type_writer_init_values_only (&writer,

1291 reader-\>byte_order,

1292 reader-\>type_str,

1293 reader-\>type_pos,

1294 &block.replacement,

1295 \_dbus_string_get_length (&block.replacement));

1296\#if RECURSIVE_MARSHAL_WRITE_TRACE

1297 \_dbus_verbose ("WRITING basic value to writer %p (replacement string)\n", &writer);

1298\#endif

1299 if (!\_dbus_type_writer_write_basic (&writer, current_type, value))

1300 goto out;

1301

1302 if (!replacement_block_replace (&block,

1303 reader,

1304 realign_root))

1305 goto out;

1306

1307 retval = TRUE;

1308

1309 out:

1310 replacement_block_free (&block);

1311 return retval;

1312}

1313

1314static void

1315reader_set_basic_fixed_length (DBusTypeReader \*reader,

1316 int current_type,

1317 const void \*value)

1318{

1319 \_dbus_marshal_set_basic ((DBusString\*) reader-\>value_str,

1320 reader-\>value_pos,

1321 current_type,

1322 value,

1323 reader-\>byte_order,

1324 NULL, NULL);

1325}

1326

1361dbus_bool_t

1362\_dbus_type_reader_set_basic (DBusTypeReader \*reader,

1363 const void \*value,

1364 const DBusTypeReader \*realign_root)

1365{

1366 int current_type;

1367

1368 \_dbus_assert (!reader-\>klass-\>types_only);

1369 \_dbus_assert (reader-\>value_str == realign_root-\>value_str);

1370 \_dbus_assert (reader-\>value_pos \>= realign_root-\>value_pos);

1371

1372 current_type = \_dbus_type_reader_get_current_type (reader);

1373

1374\#if RECURSIVE_MARSHAL_WRITE_TRACE

1375 \_dbus_verbose (" SET BASIC type reader %p type_pos = %d value_pos = %d remaining sig '%s' realign_root = %p with value_pos %d current_type = %s\n",

1376 reader, reader-\>type_pos, reader-\>value_pos,

1377 \_dbus_string_get_const_data_len (reader-\>type_str, reader-\>type_pos, 0),

1378 realign_root,

1379 realign_root ? realign_root-\>value_pos : -1,

1380 \_dbus_type_to_string (current_type));

1381 \_dbus_verbose_bytes_of_string (realign_root-\>value_str, realign_root-\>value_pos,

1382 \_dbus_string_get_length (realign_root-\>value_str) -

1383 realign_root-\>value_pos);

1384\#endif

1385

1386 \_dbus_assert (dbus_type_is_basic (current_type));

1387

1388 if (dbus_type_is_fixed (current_type))

1389 {

1390 reader_set_basic_fixed_length (reader, current_type, value);

1391 return TRUE;

1392 }

1393 else

1394 {

1395 \_dbus_assert (realign_root != NULL);

1396 return reader_set_basic_variable_length (reader, current_type,

1397 value, realign_root);

1398 }

1399}

1400

1418dbus_bool_t

1419\_dbus_type_reader_delete (DBusTypeReader \*reader,

1420 const DBusTypeReader \*realign_root)

1421{

1422 dbus_bool_t retval;

1423 ReplacementBlock block;

1424

1425 \_dbus_assert (realign_root != NULL);

1426 \_dbus_assert (reader-\>klass == &array_reader_class);

1427

1428 retval = FALSE;

1429

1430 if (!replacement_block_init (&block, reader))

1431 return FALSE;

1432

1433 if (!replacement_block_replace (&block,

1434 reader,

1435 realign_root))

1436 goto out;

1437

1438 retval = TRUE;

1439

1440 out:

1441 replacement_block_free (&block);

1442 return retval;

1443}

1444

1445/\*

1446 \* Compares two readers, which must be iterating over the same value data.

1447 \* Returns \#TRUE if the first parameter is further along than the second parameter.

1448 \*

1449 \* @param lhs left-hand-side (first) parameter

1450 \* @param rhs left-hand-side (first) parameter

1451 \* @returns whether lhs is greater than rhs

1452 \*/

1453static dbus_bool_t

1454\_dbus_type_reader_greater_than (const DBusTypeReader \*lhs,

1455 const DBusTypeReader \*rhs)

1456{

1457 \_dbus_assert (lhs-\>value_str == rhs-\>value_str);

1458

1459 return lhs-\>value_pos \> rhs-\>value_pos;

1460}

1461

1462/\*

1463 \*

1464 \*

1465 \* DBusTypeWriter

1466 \*

1467 \*

1468 \*

1469 \*/

1470

1491void

1492\_dbus_type_writer_init (DBusTypeWriter \*writer,

1493 int byte_order,

1494 DBusString \*type_str,

1495 int type_pos,

1496 DBusString \*value_str,

1497 int value_pos)

1498{

1499 writer-\>byte_order = byte_order;

1500 writer-\>type_str = type_str;

1501 writer-\>type_pos = type_pos;

1502 writer-\>value_str = value_str;

1503 writer-\>value_pos = value_pos;

1504 writer-\>container_type = DBUS_TYPE_INVALID;

1505 writer-\>type_pos_is_expectation = FALSE;

1506 writer-\>enabled = TRUE;

1507

1508\#if RECURSIVE_MARSHAL_WRITE_TRACE

1509 \_dbus_verbose ("writer %p init remaining sig '%s'\n", writer,

1510 writer-\>type_str ?

1511 \_dbus_string_get_const_data_len (writer-\>type_str, writer-\>type_pos, 0) :

1512 "unknown");

1513\#endif

1514}

1515

1526void

1527\_dbus_type_writer_init_types_delayed (DBusTypeWriter \*writer,

1528 int byte_order,

1529 DBusString \*value_str,

1530 int value_pos)

1531{

1532 \_dbus_type_writer_init (writer, byte_order,

1533 NULL, 0, value_str, value_pos);

1534}

1535

1544void

1545\_dbus_type_writer_add_types (DBusTypeWriter \*writer,

1546 DBusString \*type_str,

1547 int type_pos)

1548{

1549 if (writer-\>type_str == NULL) /\* keeps us from using this as setter \*/

1550 {

1551 writer-\>type_str = type_str;

1552 writer-\>type_pos = type_pos;

1553 }

1554}

1555

1561void

1562\_dbus_type_writer_remove_types (DBusTypeWriter \*writer)

1563{

1564 writer-\>type_str = NULL;

1565 writer-\>type_pos = -1;

1566}

1567

1582void

1583\_dbus_type_writer_init_values_only (DBusTypeWriter \*writer,

1584 int byte_order,

1585 const DBusString \*type_str,

1586 int type_pos,

1587 DBusString \*value_str,

1588 int value_pos)

1589{

1590 \_dbus_type_writer_init (writer, byte_order,

1591 (DBusString\*)type_str, type_pos,

1592 value_str, value_pos);

1593

1594 writer-\>type_pos_is_expectation = TRUE;

1595}

1596

1597static dbus_bool_t

1598\_dbus_type_writer_write_basic_no_typecode (DBusTypeWriter \*writer,

1599 int type,

1600 const void \*value)

1601{

1602 if (writer-\>enabled)

1603 return \_dbus_marshal_write_basic (writer-\>value_str,

1604 writer-\>value_pos,

1605 type,

1606 value,

1607 writer-\>byte_order,

1608 &writer-\>value_pos);

1609 else

1610 return TRUE;

1611}

1612

1613/\* If our parent is an array, things are a little bit complicated.

1614 \*

1615 \* The parent must have a complete element type, such as

1616 \* "i" or "aai" or "(ii)" or "a(ii)". There can't be

1617 \* unclosed parens, or an "a" with no following type.

1618 \*

1619 \* To recurse, the only allowed operation is to recurse into the

1620 \* first type in the element type. So for "i" you can't recurse, for

1621 \* "ai" you can recurse into the array, for "(ii)" you can recurse

1622 \* into the struct.

1623 \*

1624 \* If you recurse into the array for "ai", then you must specify

1625 \* "i" for the element type of the array you recurse into.

1626 \*

1627 \* While inside an array at any level, we need to avoid writing to

1628 \* type_str, since the type only appears once for the whole array,

1629 \* it does not appear for each array element.

1630 \*

1631 \* While inside an array type_pos points to the expected next

1632 \* typecode, rather than the next place we could write a typecode.

1633 \*/

1634static void

1635writer_recurse_init_and_check (DBusTypeWriter \*writer,

1636 int container_type,

1637 DBusTypeWriter \*sub)

1638{

1639 \_dbus_type_writer_init (sub,

1640 writer-\>byte_order,

1641 writer-\>type_str,

1642 writer-\>type_pos,

1643 writer-\>value_str,

1644 writer-\>value_pos);

1645

1646 sub-\>container_type = container_type;

1647

1648 if (writer-\>type_pos_is_expectation \|\|

1649 (sub-\>container_type == DBUS_TYPE_ARRAY \|\| sub-\>container_type == DBUS_TYPE_VARIANT))

1650 sub-\>type_pos_is_expectation = TRUE;

1651 else

1652 sub-\>type_pos_is_expectation = FALSE;

1653

1654 sub-\>enabled = writer-\>enabled;

1655

1656\#ifndef DBUS_DISABLE_CHECKS

1657 if (writer-\>type_pos_is_expectation && writer-\>type_str)

1658 {

1659 int expected;

1660

1661 expected = \_dbus_first_type_in_signature (writer-\>type_str, writer-\>type_pos);

1662

1663 if (expected != sub-\>container_type)

1664 {

1665 if (expected != DBUS_TYPE_INVALID)

1666 \_dbus_warn_check_failed ("Writing an element of type %s, but the expected type here is %s\n"

1667 "The overall signature expected here was '%s' and we are on byte %d of that signature.",

1668 \_dbus_type_to_string (sub-\>container_type),

1669 \_dbus_type_to_string (expected),

1670 \_dbus_string_get_const_data (writer-\>type_str), writer-\>type_pos);

1671 else

1672 \_dbus_warn_check_failed ("Writing an element of type %s, but no value is expected here\n"

1673 "The overall signature expected here was '%s' and we are on byte %d of that signature.",

1674 \_dbus_type_to_string (sub-\>container_type),

1675 \_dbus_string_get_const_data (writer-\>type_str), writer-\>type_pos);

1676

1677 \_dbus_assert_not_reached ("bad array element or variant content written");

1678 }

1679 }

1680\#endif /\* DBUS_DISABLE_CHECKS \*/

1681

1682\#if RECURSIVE_MARSHAL_WRITE_TRACE

1683 \_dbus_verbose (" type writer %p recurse parent %s type_pos = %d value_pos = %d is_expectation = %d remaining sig '%s' enabled = %d\n",

1684 writer,

1685 \_dbus_type_to_string (writer-\>container_type),

1686 writer-\>type_pos, writer-\>value_pos, writer-\>type_pos_is_expectation,

1687 writer-\>type_str ?

1688 \_dbus_string_get_const_data_len (writer-\>type_str, writer-\>type_pos, 0) :

1689 "unknown",

1690 writer-\>enabled);

1691 \_dbus_verbose (" type writer %p recurse sub %s type_pos = %d value_pos = %d is_expectation = %d enabled = %d\n",

1692 sub,

1693 \_dbus_type_to_string (sub-\>container_type),

1694 sub-\>type_pos, sub-\>value_pos,

1695 sub-\>type_pos_is_expectation,

1696 sub-\>enabled);

1697\#endif

1698}

1699

1700static dbus_bool_t

1701write_or_verify_typecode (DBusTypeWriter \*writer,

1702 int typecode)

1703{

1704 /\* A subwriter inside an array or variant will have type_pos

1705 \* pointing to the expected typecode; a writer not inside an array

1706 \* or variant has type_pos pointing to the next place to insert a

1707 \* typecode.

1708 \*/

1709\#if RECURSIVE_MARSHAL_WRITE_TRACE

1710 \_dbus_verbose (" type writer %p write_or_verify start type_pos = %d remaining sig '%s' enabled = %d\n",

1711 writer, writer-\>type_pos,

1712 writer-\>type_str ?

1713 \_dbus_string_get_const_data_len (writer-\>type_str, writer-\>type_pos, 0) :

1714 "unknown",

1715 writer-\>enabled);

1716\#endif

1717

1718 if (writer-\>type_str == NULL)

1719 return TRUE;

1720

1721 if (writer-\>type_pos_is_expectation)

1722 {

1723\#ifndef DBUS_DISABLE_CHECKS

1724 {

1725 int expected;

1726

1727 expected = \_dbus_string_get_byte (writer-\>type_str, writer-\>type_pos);

1728

1729 if (expected != typecode)

1730 {

1731 if (expected != DBUS_TYPE_INVALID)

1732 \_dbus_warn_check_failed ("Array or variant type requires that type %s be written, but %s was written.\n"

1733 "The overall signature expected here was '%s' and we are on byte %d of that signature.",

1734 \_dbus_type_to_string (expected), \_dbus_type_to_string (typecode),

1735 \_dbus_string_get_const_data (writer-\>type_str), writer-\>type_pos);

1736 else

1737 \_dbus_warn_check_failed ("Array or variant type wasn't expecting any more values to be written into it, but a value %s was written.\n"

1738 "The overall signature expected here was '%s' and we are on byte %d of that signature.",

1739 \_dbus_type_to_string (typecode),

1740 \_dbus_string_get_const_data (writer-\>type_str), writer-\>type_pos);

1741 \_dbus_assert_not_reached ("bad type inserted somewhere inside an array or variant");

1742 }

1743 }

1744\#endif /\* DBUS_DISABLE_CHECKS \*/

1745

1746 /\* if immediately inside an array we'd always be appending an element,

1747 \* so the expected type doesn't change; if inside a struct or something

1748 \* below an array, we need to move through said struct or something.

1749 \*/

1750 if (writer-\>container_type != DBUS_TYPE_ARRAY)

1751 writer-\>type_pos += 1;

1752 }

1753 else

1754 {

1755 if (!\_dbus_string_insert_byte (writer-\>type_str,

1756 writer-\>type_pos,

1757 typecode))

1758 return FALSE;

1759

1760 writer-\>type_pos += 1;

1761 }

1762

1763\#if RECURSIVE_MARSHAL_WRITE_TRACE

1764 \_dbus_verbose (" type writer %p write_or_verify end type_pos = %d remaining sig '%s'\n",

1765 writer, writer-\>type_pos,

1766 \_dbus_string_get_const_data_len (writer-\>type_str, writer-\>type_pos, 0));

1767\#endif

1768

1769 return TRUE;

1770}

1771

1772static dbus_bool_t

1773writer_recurse_struct_or_dict_entry (DBusTypeWriter \*writer,

1774 int begin_char,

1775 const DBusString \*contained_type,

1776 int contained_type_start,

1777 int contained_type_len,

1778 DBusTypeWriter \*sub)

1779{

1780 /\* FIXME right now contained_type is ignored; we could probably

1781 \* almost trivially fix the code so if it's present we

1782 \* write it out and then set type_pos_is_expectation

1783 \*/

1784

1785 /\* Ensure that we'll be able to add alignment padding and the typecode \*/

1786 if (writer-\>enabled)

1787 {

1788 if (!\_dbus_string_alloc_space (sub-\>value_str, 8))

1789 return FALSE;

1790 }

1791

1792 if (!write_or_verify_typecode (sub, begin_char))

1793 \_dbus_assert_not_reached ("failed to insert struct typecode after prealloc");

1794

1795 if (writer-\>enabled)

1796 {

1797 if (!\_dbus_string_insert_bytes (sub-\>value_str,

1798 sub-\>value_pos,

1799 \_DBUS_ALIGN_VALUE (sub-\>value_pos, 8) - sub-\>value_pos,

1800 '\0'))

1801 \_dbus_assert_not_reached ("should not have failed to insert alignment padding for struct");

1802 sub-\>value_pos = \_DBUS_ALIGN_VALUE (sub-\>value_pos, 8);

1803 }

1804

1805 return TRUE;

1806}

1807

1808

1809static dbus_bool_t

1810writer_recurse_array (DBusTypeWriter \*writer,

1811 const DBusString \*contained_type,

1812 int contained_type_start,

1813 int contained_type_len,

1814 DBusTypeWriter \*sub,

1815 dbus_bool_t is_array_append)

1816{

1817 dbus_uint32_t value = 0;

1818 int alignment;

1819 int aligned;

1820

1821\#ifndef DBUS_DISABLE_CHECKS

1822 if (writer-\>container_type == DBUS_TYPE_ARRAY &&

1823 writer-\>type_str)

1824 {

1825 if (!\_dbus_string_equal_substring (contained_type,

1826 contained_type_start,

1827 contained_type_len,

1828 writer-\>type_str,

1829 writer-\>u.array.element_type_pos + 1))

1830 {

1831 \_dbus_warn_check_failed ("Writing an array of '%s' but this is incompatible with the expected type of elements in the parent array",

1832 \_dbus_string_get_const_data_len (contained_type,

1833 contained_type_start,

1834 contained_type_len));

1835 \_dbus_assert_not_reached ("incompatible type for child array");

1836 }

1837 }

1838\#endif /\* DBUS_DISABLE_CHECKS \*/

1839

1840 if (writer-\>enabled && !is_array_append)

1841 {

1842 /\* 3 pad + 4 bytes for the array length, and 4 bytes possible padding

1843 \* before array values

1844 \*/

1845 if (!\_dbus_string_alloc_space (sub-\>value_str, 3 + 4 + 4))

1846 return FALSE;

1847 }

1848

1849 if (writer-\>type_str != NULL)

1850 {

1851 sub-\>type_pos += 1; /\* move to point to the element type, since type_pos

1852 \* should be the expected type for further writes

1853 \*/

1854 sub-\>u.array.element_type_pos = sub-\>type_pos;

1855 }

1856

1857 if (!writer-\>type_pos_is_expectation)

1858 {

1859 /\* sub is a toplevel/outermost array so we need to write the type data \*/

1860

1861 /\* alloc space for array typecode, element signature \*/

1862 if (!\_dbus_string_alloc_space (writer-\>type_str, 1 + contained_type_len))

1863 return FALSE;

1864

1865 if (!\_dbus_string_insert_byte (writer-\>type_str,

1866 writer-\>type_pos,

1867 DBUS_TYPE_ARRAY))

1868 \_dbus_assert_not_reached ("failed to insert array typecode after prealloc");

1869

1870 if (!\_dbus_string_copy_len (contained_type,

1871 contained_type_start, contained_type_len,

1872 sub-\>type_str,

1873 sub-\>u.array.element_type_pos))

1874 \_dbus_assert_not_reached ("should not have failed to insert array element typecodes");

1875 }

1876

1877 if (writer-\>type_str != NULL)

1878 {

1879 /\* If the parent is an array, we hold type_pos pointing at the array element type;

1880 \* otherwise advance it to reflect the array value we just recursed into

1881 \*/

1882 if (writer-\>container_type != DBUS_TYPE_ARRAY)

1883 writer-\>type_pos += 1 + contained_type_len;

1884 else

1885 \_dbus_assert (writer-\>type_pos_is_expectation); /\* because it's an array \*/

1886 }

1887

1888 if (writer-\>enabled)

1889 {

1890 /\* Write (or jump over, if is_array_append) the length \*/

1891 sub-\>u.array.len_pos = \_DBUS_ALIGN_VALUE (sub-\>value_pos, 4);

1892

1893 if (is_array_append)

1894 {

1895 sub-\>value_pos += 4;

1896 }

1897 else

1898 {

1899 if (!\_dbus_type_writer_write_basic_no_typecode (sub, DBUS_TYPE_UINT32,

1900 &value))

1901 \_dbus_assert_not_reached ("should not have failed to insert array len");

1902 }

1903

1904 \_dbus_assert (sub-\>u.array.len_pos == sub-\>value_pos - 4);

1905

1906 /\* Write alignment padding for array elements

1907 \* Note that we write the padding \*even for empty arrays\*

1908 \* to avoid wonky special cases

1909 \*/

1910 alignment = element_type_get_alignment (contained_type, contained_type_start);

1911

1912 aligned = \_DBUS_ALIGN_VALUE (sub-\>value_pos, alignment);

1913 if (aligned != sub-\>value_pos)

1914 {

1915 if (!is_array_append)

1916 {

1917 if (!\_dbus_string_insert_bytes (sub-\>value_str,

1918 sub-\>value_pos,

1919 aligned - sub-\>value_pos,

1920 '\0'))

1921 \_dbus_assert_not_reached ("should not have failed to insert alignment padding");

1922 }

1923

1924 sub-\>value_pos = aligned;

1925 }

1926

1927 sub-\>u.array.start_pos = sub-\>value_pos;

1928

1929 if (is_array_append)

1930 {

1931 dbus_uint32_t len;

1932

1933 \_dbus_assert (\_DBUS_ALIGN_VALUE (sub-\>u.array.len_pos, 4) ==

1934 (unsigned) sub-\>u.array.len_pos);

1935 len = \_dbus_unpack_uint32 (sub-\>byte_order,

1936 \_dbus_string_get_const_udata_len (sub-\>value_str,

1937 sub-\>u.array.len_pos,

1938 4));

1939

1940 sub-\>value_pos += len;

1941 }

1942 }

1943 else

1944 {

1945 /\* not enabled, so we won't write the len_pos; set it to -1 to so indicate \*/

1946 sub-\>u.array.len_pos = -1;

1947 sub-\>u.array.start_pos = sub-\>value_pos;

1948 }

1949

1950 \_dbus_assert (sub-\>u.array.len_pos \< sub-\>u.array.start_pos);

1951 \_dbus_assert (is_array_append \|\| sub-\>u.array.start_pos == sub-\>value_pos);

1952

1953\#if RECURSIVE_MARSHAL_WRITE_TRACE

1954 \_dbus_verbose (" type writer %p recurse array done remaining sig '%s' array start_pos = %d len_pos = %d value_pos = %d\n", sub,

1955 sub-\>type_str ?

1956 \_dbus_string_get_const_data_len (sub-\>type_str, sub-\>type_pos, 0) :

1957 "unknown",

1958 sub-\>u.array.start_pos, sub-\>u.array.len_pos, sub-\>value_pos);

1959\#endif

1960

1961 return TRUE;

1962}

1963

1964/\* Variant value will normally have:

1965 \* 1 byte signature length not including nul

1966 \* signature typecodes (nul terminated)

1967 \* padding to alignment of contained type

1968 \* body according to signature

1969 \*

1970 \* The signature string can only have a single type

1971 \* in it but that type may be complex/recursive.

1972 \*

1973 \* So a typical variant type with the integer 3 will have these

1974 \* octets:

1975 \* 0x1 'i' '\0' \[1 byte padding to alignment boundary\] 0x0 0x0 0x0 0x3

1976 \*

1977 \* The main world of hurt for writing out a variant is that the type

1978 \* string is the same string as the value string. Which means

1979 \* inserting to the type string will move the value_pos; and it means

1980 \* that inserting to the type string could break type alignment.

1981 \*/

1982static dbus_bool_t

1983writer_recurse_variant (DBusTypeWriter \*writer,

1984 const DBusString \*contained_type,

1985 int contained_type_start,

1986 int contained_type_len,

1987 DBusTypeWriter \*sub)

1988{

1989 int contained_alignment;

1990

1991 if (writer-\>enabled)

1992 {

1993 /\* Allocate space for the worst case, which is 1 byte sig

1994 \* length, nul byte at end of sig, and 7 bytes padding to

1995 \* 8-boundary.

1996 \*/

1997 if (!\_dbus_string_alloc_space (sub-\>value_str, contained_type_len + 9))

1998 return FALSE;

1999 }

2000

2001 /\* write VARIANT typecode to the parent's type string \*/

2002 if (!write_or_verify_typecode (writer, DBUS_TYPE_VARIANT))

2003 return FALSE;

2004

2005 /\* If not enabled, mark that we have no type_str anymore ... \*/

2006

2007 if (!writer-\>enabled)

2008 {

2009 sub-\>type_str = NULL;

2010 sub-\>type_pos = -1;

2011

2012 return TRUE;

2013 }

2014

2015 /\* If we're enabled then continue ... \*/

2016

2017 if (!\_dbus_string_insert_byte (sub-\>value_str,

2018 sub-\>value_pos,

2019 contained_type_len))

2020 \_dbus_assert_not_reached ("should not have failed to insert variant type sig len");

2021

2022 sub-\>value_pos += 1;

2023

2024 /\* Here we switch over to the expected type sig we're about to write \*/

2025 sub-\>type_str = sub-\>value_str;

2026 sub-\>type_pos = sub-\>value_pos;

2027

2028 if (!\_dbus_string_copy_len (contained_type, contained_type_start, contained_type_len,

2029 sub-\>value_str, sub-\>value_pos))

2030 \_dbus_assert_not_reached ("should not have failed to insert variant type sig");

2031

2032 sub-\>value_pos += contained_type_len;

2033

2034 if (!\_dbus_string_insert_byte (sub-\>value_str,

2035 sub-\>value_pos,

2036 DBUS_TYPE_INVALID))

2037 \_dbus_assert_not_reached ("should not have failed to insert variant type nul termination");

2038

2039 sub-\>value_pos += 1;

2040

2041 contained_alignment = \_dbus_type_get_alignment (\_dbus_first_type_in_signature (contained_type, contained_type_start));

2042

2043 if (!\_dbus_string_insert_bytes (sub-\>value_str,

2044 sub-\>value_pos,

2045 \_DBUS_ALIGN_VALUE (sub-\>value_pos, contained_alignment) - sub-\>value_pos,

2046 '\0'))

2047 \_dbus_assert_not_reached ("should not have failed to insert alignment padding for variant body");

2048 sub-\>value_pos = \_DBUS_ALIGN_VALUE (sub-\>value_pos, contained_alignment);

2049

2050 return TRUE;

2051}

2052

2053static dbus_bool_t

2054\_dbus_type_writer_recurse_contained_len (DBusTypeWriter \*writer,

2055 int container_type,

2056 const DBusString \*contained_type,

2057 int contained_type_start,

2058 int contained_type_len,

2059 DBusTypeWriter \*sub,

2060 dbus_bool_t is_array_append)

2061{

2062 writer_recurse_init_and_check (writer, container_type, sub);

2063

2064 switch (container_type)

2065 {

2066 case DBUS_TYPE_STRUCT:

2067 return writer_recurse_struct_or_dict_entry (writer,

2068 DBUS_STRUCT_BEGIN_CHAR,

2069 contained_type,

2070 contained_type_start, contained_type_len,

2071 sub);

2072 break;

2073 case DBUS_TYPE_DICT_ENTRY:

2074 return writer_recurse_struct_or_dict_entry (writer,

2075 DBUS_DICT_ENTRY_BEGIN_CHAR,

2076 contained_type,

2077 contained_type_start, contained_type_len,

2078 sub);

2079 break;

2080 case DBUS_TYPE_ARRAY:

2081 return writer_recurse_array (writer,

2082 contained_type, contained_type_start, contained_type_len,

2083 sub, is_array_append);

2084 break;

2085 case DBUS_TYPE_VARIANT:

2086 return writer_recurse_variant (writer,

2087 contained_type, contained_type_start, contained_type_len,

2088 sub);

2089 break;

2090 default:

2091 \_dbus_assert_not_reached ("tried to recurse into type that doesn't support that");

2092 return FALSE;

2093 break;

2094 }

2095}

2096

2107dbus_bool_t

2108\_dbus_type_writer_recurse (DBusTypeWriter \*writer,

2109 int container_type,

2110 const DBusString \*contained_type,

2111 int contained_type_start,

2112 DBusTypeWriter \*sub)

2113{

2114 int contained_type_len;

2115

2116 if (contained_type)

2117 contained_type_len = find_len_of_complete_type (contained_type, contained_type_start);

2118 else

2119 contained_type_len = 0;

2120

2121 return \_dbus_type_writer_recurse_contained_len (writer, container_type,

2122 contained_type,

2123 contained_type_start,

2124 contained_type_len,

2125 sub,

2126 FALSE);

2127}

2128

2141dbus_bool_t

2142\_dbus_type_writer_append_array (DBusTypeWriter \*writer,

2143 const DBusString \*contained_type,

2144 int contained_type_start,

2145 DBusTypeWriter \*sub)

2146{

2147 int contained_type_len;

2148

2149 if (contained_type)

2150 contained_type_len = find_len_of_complete_type (contained_type, contained_type_start);

2151 else

2152 contained_type_len = 0;

2153

2154 return \_dbus_type_writer_recurse_contained_len (writer, DBUS_TYPE_ARRAY,

2155 contained_type,

2156 contained_type_start,

2157 contained_type_len,

2158 sub,

2159 TRUE);

2160}

2161

2162static int

2163writer_get_array_len (DBusTypeWriter \*writer)

2164{

2165 \_dbus_assert (writer-\>container_type == DBUS_TYPE_ARRAY);

2166 return writer-\>value_pos - writer-\>u.array.start_pos;

2167}

2168

2177dbus_bool_t

2178\_dbus_type_writer_unrecurse (DBusTypeWriter \*writer,

2179 DBusTypeWriter \*sub)

2180{

2181 /\* type_pos_is_expectation never gets unset once set, or we'd get all hosed \*/

2182 \_dbus_assert (!writer-\>type_pos_is_expectation \|\|

2183 (writer-\>type_pos_is_expectation && sub-\>type_pos_is_expectation));

2184

2185\#if RECURSIVE_MARSHAL_WRITE_TRACE

2186 \_dbus_verbose (" type writer %p unrecurse type_pos = %d value_pos = %d is_expectation = %d container_type = %s\n",

2187 writer, writer-\>type_pos, writer-\>value_pos, writer-\>type_pos_is_expectation,

2188 \_dbus_type_to_string (writer-\>container_type));

2189 \_dbus_verbose (" type writer %p unrecurse sub type_pos = %d value_pos = %d is_expectation = %d container_type = %s\n",

2190 sub, sub-\>type_pos, sub-\>value_pos,

2191 sub-\>type_pos_is_expectation,

2192 \_dbus_type_to_string (sub-\>container_type));

2193\#endif

2194

2195 if (sub-\>container_type == DBUS_TYPE_STRUCT)

2196 {

2197 if (!write_or_verify_typecode (sub, DBUS_STRUCT_END_CHAR))

2198 return FALSE;

2199 }

2200 else if (sub-\>container_type == DBUS_TYPE_DICT_ENTRY)

2201 {

2202 if (!write_or_verify_typecode (sub, DBUS_DICT_ENTRY_END_CHAR))

2203 return FALSE;

2204 }

2205 else if (sub-\>container_type == DBUS_TYPE_ARRAY)

2206 {

2207 if (sub-\>u.array.len_pos \>= 0) /\* len_pos == -1 if we weren't enabled when we passed it \*/

2208 {

2209 dbus_uint32_t len;

2210

2211 /\* Set the array length \*/

2212 len = writer_get_array_len (sub);

2213 \_dbus_marshal_set_uint32 (sub-\>value_str,

2214 sub-\>u.array.len_pos,

2215 len,

2216 sub-\>byte_order);

2217\#if RECURSIVE_MARSHAL_WRITE_TRACE

2218 \_dbus_verbose (" filled in sub array len to %u at len_pos %d\n",

2219 len, sub-\>u.array.len_pos);

2220\#endif

2221 }

2222\#if RECURSIVE_MARSHAL_WRITE_TRACE

2223 else

2224 {

2225 \_dbus_verbose (" not filling in sub array len because we were disabled when we passed the len\n");

2226 }

2227\#endif

2228 }

2229

2230 /\* Now get type_pos right for the parent writer. Here are the cases:

2231 \*

2232 \* Cases !writer-\>type_pos_is_expectation:

2233 \* (in these cases we want to update to the new insertion point)

2234 \*

2235 \* - if we recursed into a STRUCT then we didn't know in advance

2236 \* what the types in the struct would be; so we have to fill in

2237 \* that information now.

2238 \* writer-\>type_pos = sub-\>type_pos

2239 \*

2240 \* - if we recursed into anything else, we knew the full array

2241 \* type, or knew the single typecode marking VARIANT, so

2242 \* writer-\>type_pos is already correct.

2243 \* writer-\>type_pos should remain as-is

2244 \*

2245 \* - note that the parent is never an ARRAY or VARIANT, if it were

2246 \* then type_pos_is_expectation would be TRUE. The parent

2247 \* is thus known to be a toplevel or STRUCT.

2248 \*

2249 \* Cases where writer-\>type_pos_is_expectation:

2250 \* (in these cases we want to update to next expected type to write)

2251 \*

2252 \* - we recursed from STRUCT into STRUCT and we didn't increment

2253 \* type_pos in the parent just to stay consistent with the

2254 \* !writer-\>type_pos_is_expectation case (though we could

2255 \* special-case this in recurse_struct instead if we wanted)

2256 \* writer-\>type_pos = sub-\>type_pos

2257 \*

2258 \* - we recursed from STRUCT into ARRAY or VARIANT and type_pos

2259 \* for parent should have been incremented already

2260 \* writer-\>type_pos should remain as-is

2261 \*

2262 \* - we recursed from ARRAY into a sub-element, so type_pos in the

2263 \* parent is the element type and should remain the element type

2264 \* for the benefit of the next child element

2265 \* writer-\>type_pos should remain as-is

2266 \*

2267 \* - we recursed from VARIANT into its value, so type_pos in the

2268 \* parent makes no difference since there's only one value

2269 \* and we just finished writing it and won't use type_pos again

2270 \* writer-\>type_pos should remain as-is

2271 \*

2272 \*

2273 \* For all these, DICT_ENTRY is the same as STRUCT

2274 \*/

2275 if (writer-\>type_str != NULL)

2276 {

2277 if ((sub-\>container_type == DBUS_TYPE_STRUCT \|\|

2278 sub-\>container_type == DBUS_TYPE_DICT_ENTRY) &&

2279 (writer-\>container_type == DBUS_TYPE_STRUCT \|\|

2280 writer-\>container_type == DBUS_TYPE_DICT_ENTRY \|\|

2281 writer-\>container_type == DBUS_TYPE_INVALID))

2282 {

2283 /\* Advance the parent to the next struct field \*/

2284 writer-\>type_pos = sub-\>type_pos;

2285 }

2286 }

2287

2288 writer-\>value_pos = sub-\>value_pos;

2289

2290\#if RECURSIVE_MARSHAL_WRITE_TRACE

2291 \_dbus_verbose (" type writer %p unrecursed type_pos = %d value_pos = %d remaining sig '%s'\n",

2292 writer, writer-\>type_pos, writer-\>value_pos,

2293 writer-\>type_str ?

2294 \_dbus_string_get_const_data_len (writer-\>type_str, writer-\>type_pos, 0) :

2295 "unknown");

2296\#endif

2297

2298 return TRUE;

2299}

2300

2309dbus_bool_t

2310\_dbus_type_writer_write_basic (DBusTypeWriter \*writer,

2311 int type,

2312 const void \*value)

2313{

2314 dbus_bool_t retval;

2315

2316 /\* First ensure that our type realloc will succeed \*/

2317 if (!writer-\>type_pos_is_expectation && writer-\>type_str != NULL)

2318 {

2319 if (!\_dbus_string_alloc_space (writer-\>type_str, 1))

2320 return FALSE;

2321 }

2322

2323 retval = FALSE;

2324

2325 if (!\_dbus_type_writer_write_basic_no_typecode (writer, type, value))

2326 goto out;

2327

2328 if (!write_or_verify_typecode (writer, type))

2329 \_dbus_assert_not_reached ("failed to write typecode after prealloc");

2330

2331 retval = TRUE;

2332

2333 out:

2334\#if RECURSIVE_MARSHAL_WRITE_TRACE

2335 \_dbus_verbose (" type writer %p basic type_pos = %d value_pos = %d is_expectation = %d enabled = %d\n",

2336 writer, writer-\>type_pos, writer-\>value_pos, writer-\>type_pos_is_expectation,

2337 writer-\>enabled);

2338\#endif

2339

2340 return retval;

2341}

2342

2357dbus_bool_t

2358\_dbus_type_writer_write_fixed_multi (DBusTypeWriter \*writer,

2359 int element_type,

2360 const void \*value,

2361 int n_elements)

2362{

2363 \_dbus_assert (writer-\>container_type == DBUS_TYPE_ARRAY);

2364 \_dbus_assert (dbus_type_is_fixed (element_type));

2365 \_dbus_assert (writer-\>type_pos_is_expectation);

2366 \_dbus_assert (n_elements \>= 0);

2367

2368\#if RECURSIVE_MARSHAL_WRITE_TRACE

2369 \_dbus_verbose (" type writer %p entering fixed multi type_pos = %d value_pos = %d n_elements %d\n",

2370 writer, writer-\>type_pos, writer-\>value_pos, n_elements);

2371\#endif

2372

2373 if (!write_or_verify_typecode (writer, element_type))

2374 \_dbus_assert_not_reached ("OOM should not happen if only verifying typecode");

2375

2376 if (writer-\>enabled)

2377 {

2378 if (!\_dbus_marshal_write_fixed_multi (writer-\>value_str,

2379 writer-\>value_pos,

2380 element_type,

2381 value,

2382 n_elements,

2383 writer-\>byte_order,

2384 &writer-\>value_pos))

2385 return FALSE;

2386 }

2387

2388\#if RECURSIVE_MARSHAL_WRITE_TRACE

2389 \_dbus_verbose (" type writer %p fixed multi written new type_pos = %d new value_pos = %d n_elements %d\n",

2390 writer, writer-\>type_pos, writer-\>value_pos, n_elements);

2391\#endif

2392

2393 return TRUE;

2394}

2395

2396static void

2397enable_if_after (DBusTypeWriter \*writer,

2398 DBusTypeReader \*reader,

2399 const DBusTypeReader \*start_after)

2400{

2401 if (start_after)

2402 {

2403 if (!writer-\>enabled && \_dbus_type_reader_greater_than (reader, start_after))

2404 {

2405 \_dbus_type_writer_set_enabled (writer, TRUE);

2406\#if RECURSIVE_MARSHAL_WRITE_TRACE

2407 \_dbus_verbose ("ENABLING writer %p at %d because reader at value_pos %d is after reader at value_pos %d\n",

2408 writer, writer-\>value_pos, reader-\>value_pos, start_after-\>value_pos);

2409\#endif

2410 }

2411

2412 \_dbus_assert ((!writer-\>enabled && !\_dbus_type_reader_greater_than (reader, start_after)) \|\|

2413 (writer-\>enabled && \_dbus_type_reader_greater_than (reader, start_after)));

2414 }

2415}

2416

2417static dbus_bool_t

2418append_fixup (DBusList \*\*fixups,

2419 const DBusArrayLenFixup \*fixup)

2420{

2421 DBusArrayLenFixup \*f;

2422

2423 f = dbus_new (DBusArrayLenFixup, 1);

2424 if (f == NULL)

2425 return FALSE;

2426

2427 \*f = \*fixup;

2428

2429 if (!\_dbus_list_append (fixups, f))

2430 {

2431 dbus_free (f);

2432 return FALSE;

2433 }

2434

2435 \_dbus_assert (f-\>len_pos_in_reader == fixup-\>len_pos_in_reader);

2436 \_dbus_assert (f-\>new_len == fixup-\>new_len);

2437

2438 return TRUE;

2439}

2440

2441/\* This loop is trivial if you ignore all the start_after nonsense,

2442 \* so if you're trying to figure it out, start by ignoring that

2443 \*/

2444static dbus_bool_t

2445writer_write_reader_helper (DBusTypeWriter \*writer,

2446 DBusTypeReader \*reader,

2447 const DBusTypeReader \*start_after,

2448 int start_after_new_pos,

2449 int start_after_new_len,

2450 DBusList \*\*fixups,

2451 dbus_bool_t inside_start_after)

2452{

2453 int current_type;

2454

2455 while ((current_type = \_dbus_type_reader_get_current_type (reader)) != DBUS_TYPE_INVALID)

2456 {

2457 if (dbus_type_is_container (current_type))

2458 {

2459 DBusTypeReader subreader;

2460 DBusTypeWriter subwriter;

2461 const DBusString \*sig_str;

2462 int sig_start;

2463 int sig_len;

2464 dbus_bool_t enabled_at_recurse;

2465 dbus_bool_t past_start_after;

2466 int reader_array_len_pos;

2467 int reader_array_start_pos;

2468 dbus_bool_t this_is_start_after;

2469

2470 /\* type_pos is checked since e.g. in a struct the struct

2471 \* and its first field have the same value_pos.

2472 \* type_str will differ in reader/start_after for variants

2473 \* where type_str is inside the value_str

2474 \*/

2475 if (!inside_start_after && start_after &&

2476 reader-\>value_pos == start_after-\>value_pos &&

2477 reader-\>type_str == start_after-\>type_str &&

2478 reader-\>type_pos == start_after-\>type_pos)

2479 this_is_start_after = TRUE;

2480 else

2481 this_is_start_after = FALSE;

2482

2483 \_dbus_type_reader_recurse (reader, &subreader);

2484

2485 if (current_type == DBUS_TYPE_ARRAY)

2486 {

2487 reader_array_len_pos = ARRAY_READER_LEN_POS (&subreader);

2488 reader_array_start_pos = subreader.u.array.start_pos;

2489 }

2490 else

2491 {

2492 /\* quiet gcc \*/

2493 reader_array_len_pos = -1;

2494 reader_array_start_pos = -1;

2495 }

2496

2497 \_dbus_type_reader_get_signature (&subreader, &sig_str,

2498 &sig_start, &sig_len);

2499

2500\#if RECURSIVE_MARSHAL_WRITE_TRACE

2501 \_dbus_verbose ("about to recurse into %s reader at %d subreader at %d writer at %d start_after reader at %d write target len %d inside_start_after = %d this_is_start_after = %d\n",

2502 \_dbus_type_to_string (current_type),

2503 reader-\>value_pos,

2504 subreader.value_pos,

2505 writer-\>value_pos,

2506 start_after ? start_after-\>value_pos : -1,

2507 \_dbus_string_get_length (writer-\>value_str),

2508 inside_start_after, this_is_start_after);

2509\#endif

2510

2511 if (!inside_start_after && !this_is_start_after)

2512 enable_if_after (writer, &subreader, start_after);

2513 enabled_at_recurse = writer-\>enabled;

2514 if (!\_dbus_type_writer_recurse_contained_len (writer, current_type,

2515 sig_str, sig_start, sig_len,

2516 &subwriter, FALSE))

2517 goto oom;

2518

2519\#if RECURSIVE_MARSHAL_WRITE_TRACE

2520 \_dbus_verbose ("recursed into subwriter at %d write target len %d\n",

2521 subwriter.value_pos,

2522 \_dbus_string_get_length (subwriter.value_str));

2523\#endif

2524

2525 if (!writer_write_reader_helper (&subwriter, &subreader, start_after,

2526 start_after_new_pos, start_after_new_len,

2527 fixups,

2528 inside_start_after \|\|

2529 this_is_start_after))

2530 goto oom;

2531

2532\#if RECURSIVE_MARSHAL_WRITE_TRACE

2533 \_dbus_verbose ("about to unrecurse from %s subreader at %d writer at %d subwriter at %d write target len %d\n",

2534 \_dbus_type_to_string (current_type),

2535 subreader.value_pos,

2536 writer-\>value_pos,

2537 subwriter.value_pos,

2538 \_dbus_string_get_length (writer-\>value_str));

2539\#endif

2540

2541 if (!inside_start_after && !this_is_start_after)

2542 enable_if_after (writer, &subreader, start_after);

2543 past_start_after = writer-\>enabled;

2544 if (!\_dbus_type_writer_unrecurse (writer, &subwriter))

2545 goto oom;

2546

2547 /\* If we weren't enabled when we recursed, we didn't

2548 \* write an array len; if we passed start_after

2549 \* somewhere inside the array, then we need to generate

2550 \* a fixup.

2551 \*/

2552 if (start_after != NULL &&

2553 !enabled_at_recurse && past_start_after &&

2554 current_type == DBUS_TYPE_ARRAY &&

2555 fixups != NULL)

2556 {

2557 DBusArrayLenFixup fixup;

2558 int bytes_written_after_start_after;

2559 int bytes_before_start_after;

2560 int old_len;

2561

2562 /\* this subwriter access is moderately unkosher since we

2563 \* already unrecursed, but it works as long as unrecurse

2564 \* doesn't break us on purpose

2565 \*/

2566 bytes_written_after_start_after = writer_get_array_len (&subwriter);

2567

2568 bytes_before_start_after =

2569 start_after-\>value_pos - reader_array_start_pos;

2570

2571 fixup.len_pos_in_reader = reader_array_len_pos;

2572 fixup.new_len =

2573 bytes_before_start_after +

2574 start_after_new_len +

2575 bytes_written_after_start_after;

2576

2577 \_dbus_assert (\_DBUS_ALIGN_VALUE (fixup.len_pos_in_reader, 4) ==

2578 (unsigned) fixup.len_pos_in_reader);

2579

2580 old_len = \_dbus_unpack_uint32 (reader-\>byte_order,

2581 \_dbus_string_get_const_udata_len (reader-\>value_str,

2582 fixup.len_pos_in_reader, 4));

2583

2584 if (old_len != fixup.new_len && !append_fixup (fixups, &fixup))

2585 goto oom;

2586

2587\#if RECURSIVE_MARSHAL_WRITE_TRACE

2588 \_dbus_verbose ("Generated fixup len_pos_in_reader = %d new_len = %d reader_array_start_pos = %d start_after-\>value_pos = %d bytes_before_start_after = %d start_after_new_len = %d bytes_written_after_start_after = %d\n",

2589 fixup.len_pos_in_reader,

2590 fixup.new_len,

2591 reader_array_start_pos,

2592 start_after-\>value_pos,

2593 bytes_before_start_after,

2594 start_after_new_len,

2595 bytes_written_after_start_after);

2596\#endif

2597 }

2598 }

2599 else

2600 {

2601 DBusBasicValue val;

2602

2603 \_dbus_assert (dbus_type_is_basic (current_type));

2604

2605\#if RECURSIVE_MARSHAL_WRITE_TRACE

2606 \_dbus_verbose ("Reading basic value %s at %d\n",

2607 \_dbus_type_to_string (current_type),

2608 reader-\>value_pos);

2609\#endif

2610

2611 \_dbus_type_reader_read_basic (reader, &val);

2612

2613\#if RECURSIVE_MARSHAL_WRITE_TRACE

2614 \_dbus_verbose ("Writing basic value %s at %d write target len %d inside_start_after = %d\n",

2615 \_dbus_type_to_string (current_type),

2616 writer-\>value_pos,

2617 \_dbus_string_get_length (writer-\>value_str),

2618 inside_start_after);

2619\#endif

2620 if (!inside_start_after)

2621 enable_if_after (writer, reader, start_after);

2622 if (!\_dbus_type_writer_write_basic (writer, current_type, &val))

2623 goto oom;

2624\#if RECURSIVE_MARSHAL_WRITE_TRACE

2625 \_dbus_verbose ("Wrote basic value %s, new value_pos %d write target len %d\n",

2626 \_dbus_type_to_string (current_type),

2627 writer-\>value_pos,

2628 \_dbus_string_get_length (writer-\>value_str));

2629\#endif

2630 }

2631

2632 \_dbus_type_reader_next (reader);

2633 }

2634

2635 return TRUE;

2636

2637 oom:

2638 if (fixups)

2639 apply_and_free_fixups (fixups, NULL); /\* NULL for reader to apply to \*/

2640

2641 return FALSE;

2642}

2643

2644/\*

2645 \* Iterate through all values in the given reader, writing a copy of

2646 \* each value to the writer. The reader will be moved forward to its

2647 \* end position.

2648 \*

2649 \* If a reader start_after is provided, it should be a reader for the

2650 \* same data as the reader to be written. Only values occurring after

2651 \* the value pointed to by start_after will be written to the writer.

2652 \*

2653 \* If start_after is provided, then the copy of the reader will be

2654 \* partial. This means that array lengths will not have been copied.

2655 \* The assumption is that you wrote a new version of the value at

2656 \* start_after to the writer. You have to pass in the start position

2657 \* and length of the new value. (If you are deleting the value

2658 \* at start_after, pass in 0 for the length.)

2659 \*

2660 \* If the fixups parameter is non-#NULL, then any array length that

2661 \* was read but not written due to start_after will be provided

2662 \* as a \#DBusArrayLenFixup. The fixup contains the position of the

2663 \* array length in the source data, and the correct array length

2664 \* assuming you combine the source data before start_after with

2665 \* the written data at start_after and beyond.

2666 \*

2667 \* @param writer the writer to copy to

2668 \* @param reader the reader to copy from

2669 \* @param start_after \#NULL or a reader showing where to start

2670 \* @param start_after_new_pos the position of start_after equivalent in the target data

2671 \* @param start_after_new_len the length of start_after equivalent in the target data

2672 \* @param fixups list to append \#DBusArrayLenFixup if the write was partial

2673 \* @returns \#FALSE if no memory

2674 \*/

2675static dbus_bool_t

2676\_dbus_type_writer_write_reader_partial (DBusTypeWriter \*writer,

2677 DBusTypeReader \*reader,

2678 const DBusTypeReader \*start_after,

2679 int start_after_new_pos,

2680 int start_after_new_len,

2681 DBusList \*\*fixups)

2682{

2683 DBusTypeWriter orig;

2684 int orig_type_len;

2685 int orig_value_len;

2686 int new_bytes;

2687 int orig_enabled;

2688

2689 orig = \*writer;

2690 orig_type_len = \_dbus_string_get_length (writer-\>type_str);

2691 orig_value_len = \_dbus_string_get_length (writer-\>value_str);

2692 orig_enabled = writer-\>enabled;

2693

2694 if (start_after)

2695 \_dbus_type_writer_set_enabled (writer, FALSE);

2696

2697 if (!writer_write_reader_helper (writer, reader, start_after,

2698 start_after_new_pos,

2699 start_after_new_len,

2700 fixups, FALSE))

2701 goto oom;

2702

2703 \_dbus_type_writer_set_enabled (writer, orig_enabled);

2704 return TRUE;

2705

2706 oom:

2707 if (!writer-\>type_pos_is_expectation)

2708 {

2709 new_bytes = \_dbus_string_get_length (writer-\>type_str) - orig_type_len;

2710 \_dbus_string_delete (writer-\>type_str, orig.type_pos, new_bytes);

2711 }

2712 new_bytes = \_dbus_string_get_length (writer-\>value_str) - orig_value_len;

2713 \_dbus_string_delete (writer-\>value_str, orig.value_pos, new_bytes);

2714

2715 \*writer = orig;

2716

2717 return FALSE;

2718}

2719

2729dbus_bool_t

2730\_dbus_type_writer_write_reader (DBusTypeWriter \*writer,

2731 DBusTypeReader \*reader)

2732{

2733 return \_dbus_type_writer_write_reader_partial (writer, reader, NULL, 0, 0, NULL);

2734}

2735

2736/\*

2737 \* If disabled, a writer can still be iterated forward and recursed/unrecursed

2738 \* but won't write any values. Types will still be written unless the

2739 \* writer is a "values only" writer, because the writer needs access to

2740 \* a valid signature to be able to iterate.

2741 \*

2742 \* @param writer the type writer

2743 \* @param enabled \#TRUE if values should be written

2744 \*/

2745static void

2746\_dbus_type_writer_set_enabled (DBusTypeWriter \*writer,

2747 dbus_bool_t enabled)

2748{

2749 writer-\>enabled = enabled != FALSE;

2750}

2751

/\* end of DBusMarshal group \*/

2753

2754/\* tests in dbus-marshal-recursive-util.c \*/

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

\_dbus_warn_check_failed

void \_dbus_warn_check_failed(const char \*format,...)

Prints a "critical" warning to stderr when an assertion fails; differs from \_dbus_warn primarily in t...

**Definition** dbus-internals.c:310

\_DBUS_ZERO

\#define \_DBUS_ZERO(object)

Sets all bits in an object to zero.

**Definition** dbus-internals.h:194

\_dbus_list_get_first_link

DBusList \* \_dbus_list_get_first_link(DBusList \*\*list)

Gets the first link in the list.

**Definition** dbus-list.c:597

\_dbus_list_free_link

void \_dbus_list_free_link(DBusList \*link)

Frees a linked list node allocated with \_dbus_list_alloc_link.

**Definition** dbus-list.c:257

\_dbus_list_get_length

int \_dbus_list_get_length(DBusList \*\*list)

Gets the length of a list.

**Definition** dbus-list.c:760

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

\_dbus_type_writer_write_basic

dbus_bool_t \_dbus_type_writer_write_basic(DBusTypeWriter \*writer, int type, const void \*value)

Writes out a basic type.

**Definition** dbus-marshal-recursive.c:2310

\_dbus_type_reader_recurse

void \_dbus_type_reader_recurse(DBusTypeReader \*reader, DBusTypeReader \*sub)

Initialize a new reader pointing to the first type and corresponding value that's a child of the curr...

**Definition** dbus-marshal-recursive.c:987

\_dbus_type_writer_init_values_only

void \_dbus_type_writer_init_values_only(DBusTypeWriter \*writer, int byte_order, const DBusString \*type_str, int type_pos, DBusString \*value_str, int value_pos)

Like \_dbus_type_writer_init(), except the type string passed in should correspond to an existing sign...

**Definition** dbus-marshal-recursive.c:1583

\_dbus_type_reader_get_value_pos

int \_dbus_type_reader_get_value_pos(const DBusTypeReader \*reader)

Gets the current position in the value block.

**Definition** dbus-marshal-recursive.c:837

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

\_dbus_type_reader_init_types_only

void \_dbus_type_reader_init_types_only(DBusTypeReader \*reader, const DBusString \*type_str, int type_pos)

Like \_dbus_type_reader_init() but the iteration is over the signature, not over values.

**Definition** dbus-marshal-recursive.c:760

\_dbus_type_reader_get_signature

void \_dbus_type_reader_get_signature(const DBusTypeReader \*reader, const DBusString \*\*str_p, int \*start_p, int \*len_p)

Gets the string and range of said string containing the signature of the current value.

**Definition** dbus-marshal-recursive.c:1124

\_dbus_type_writer_write_reader

dbus_bool_t \_dbus_type_writer_write_reader(DBusTypeWriter \*writer, DBusTypeReader \*reader)

Iterate through all values in the given reader, writing a copy of each value to the writer.

**Definition** dbus-marshal-recursive.c:2730

\_dbus_marshal_set_uint32

void \_dbus_marshal_set_uint32(DBusString \*str, int pos, dbus_uint32_t value, int byte_order)

Sets the 4 bytes at the given offset to a marshaled unsigned integer, replacing anything found there ...

**Definition** dbus-marshal-basic.c:260

\_dbus_type_writer_recurse

dbus_bool_t \_dbus_type_writer_recurse(DBusTypeWriter \*writer, int container_type, const DBusString \*contained_type, int contained_type_start, DBusTypeWriter \*sub)

Opens a new container and writes out the initial information for that container.

**Definition** dbus-marshal-recursive.c:2108

\_dbus_unpack_uint32

dbus_uint32_t \_dbus_unpack_uint32(int byte_order, const unsigned char \*data)

Unpacks a 32 bit unsigned integer from a data pointer.

**Definition** dbus-marshal-basic.c:189

\_dbus_marshal_write_basic

dbus_bool_t \_dbus_marshal_write_basic(DBusString \*str, int insert_at, int type, const void \*value, int byte_order, int \*pos_after)

Marshals a basic-typed value.

**Definition** dbus-marshal-basic.c:817

\_dbus_first_type_in_signature

int \_dbus_first_type_in_signature(const DBusString \*str, int pos)

Get the first type in the signature.

**Definition** dbus-marshal-basic.c:1484

\_dbus_type_reader_read_fixed_multi

void \_dbus_type_reader_read_fixed_multi(const DBusTypeReader \*reader, const void \*\*value, int \*n_elements)

Reads a block of fixed-length basic values, from the current point in an array to the end of the arra...

**Definition** dbus-marshal-recursive.c:923

\_dbus_marshal_read_uint32

dbus_uint32_t \_dbus_marshal_read_uint32(const DBusString \*str, int pos, int byte_order, int \*new_pos)

Convenience function to demarshal a 32 bit unsigned integer.

**Definition** dbus-marshal-basic.c:476

\_dbus_type_reader_get_element_type

int \_dbus_type_reader_get_element_type(const DBusTypeReader \*reader)

Gets the type of an element of the array the reader is currently pointing to.

**Definition** dbus-marshal-recursive.c:820

\_dbus_type_reader_next

dbus_bool_t \_dbus_type_reader_next(DBusTypeReader \*reader)

Skip to the next value on this "level".

**Definition** dbus-marshal-recursive.c:1053

\_dbus_type_reader_get_array_length

int \_dbus_type_reader_get_array_length(const DBusTypeReader \*reader)

Returns the number of bytes in the array.

**Definition** dbus-marshal-recursive.c:899

\_dbus_marshal_set_basic

dbus_bool_t \_dbus_marshal_set_basic(DBusString \*str, int pos, int type, const void \*value, int byte_order, int \*old_end_pos, int \*new_end_pos)

Sets an existing basic type value to a new value.

**Definition** dbus-marshal-basic.c:377

\_dbus_type_writer_add_types

void \_dbus_type_writer_add_types(DBusTypeWriter \*writer, DBusString \*type_str, int type_pos)

Adds type string to the writer, if it had none.

**Definition** dbus-marshal-recursive.c:1545

\_dbus_marshal_skip_array

void \_dbus_marshal_skip_array(const DBusString \*str, int element_type, int byte_order, int \*pos)

Skips an array, returning the next position.

**Definition** dbus-marshal-basic.c:1205

\_dbus_type_reader_has_next

dbus_bool_t \_dbus_type_reader_has_next(const DBusTypeReader \*reader)

Check whether there's another value on this "level".

**Definition** dbus-marshal-recursive.c:1093

\_dbus_marshal_write_fixed_multi

dbus_bool_t \_dbus_marshal_write_fixed_multi(DBusString \*str, int insert_at, int element_type, const void \*value, int n_elements, int byte_order, int \*pos_after)

Marshals a block of values of fixed-length type all at once, as an optimization.

**Definition** dbus-marshal-basic.c:1059

\_dbus_type_reader_delete

dbus_bool_t \_dbus_type_reader_delete(DBusTypeReader \*reader, const DBusTypeReader \*realign_root)

Recursively deletes any value pointed to by the reader, leaving the reader valid to continue reading.

**Definition** dbus-marshal-recursive.c:1419

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

\_dbus_type_reader_set_basic

dbus_bool_t \_dbus_type_reader_set_basic(DBusTypeReader \*reader, const void \*value, const DBusTypeReader \*realign_root)

Sets a new value for the basic type value pointed to by the reader, leaving the reader valid to conti...

**Definition** dbus-marshal-recursive.c:1362

\_dbus_marshal_read_basic

void \_dbus_marshal_read_basic(const DBusString \*str, int pos, int type, void \*value, int byte_order, int \*new_pos)

Demarshals a basic-typed value.

**Definition** dbus-marshal-basic.c:514

\_dbus_type_reader_get_current_type

int \_dbus_type_reader_get_current_type(const DBusTypeReader \*reader)

Gets the type of the value the reader is currently pointing to; or for a types-only reader gets the t...

**Definition** dbus-marshal-recursive.c:785

\_dbus_type_reader_read_raw

void \_dbus_type_reader_read_raw(const DBusTypeReader \*reader, const unsigned char \*\*value_location)

Get the address of the marshaled value in the data being read.

**Definition** dbus-marshal-recursive.c:852

\_dbus_type_writer_unrecurse

dbus_bool_t \_dbus_type_writer_unrecurse(DBusTypeWriter \*writer, DBusTypeWriter \*sub)

Closes a container created by \_dbus_type_writer_recurse() and writes any additional information to th...

**Definition** dbus-marshal-recursive.c:2178

\_dbus_type_writer_append_array

dbus_bool_t \_dbus_type_writer_append_array(DBusTypeWriter \*writer, const DBusString \*contained_type, int contained_type_start, DBusTypeWriter \*sub)

Append to an existing array.

**Definition** dbus-marshal-recursive.c:2142

ARRAY_READER_LEN_POS

\#define ARRAY_READER_LEN_POS(reader)

compute position of array length given array_len_offset, which is the offset back from start_pos to e...

**Definition** dbus-marshal-recursive.c:216

\_dbus_type_writer_write_fixed_multi

dbus_bool_t \_dbus_type_writer_write_fixed_multi(DBusTypeWriter \*writer, int element_type, const void \*value, int n_elements)

Writes a block of fixed-length basic values, i.e.

**Definition** dbus-marshal-recursive.c:2358

\_dbus_type_writer_init

void \_dbus_type_writer_init(DBusTypeWriter \*writer, int byte_order, DBusString \*type_str, int type_pos, DBusString \*value_str, int value_pos)

Initialize a write iterator, which is used to write out values in serialized D-Bus format.

**Definition** dbus-marshal-recursive.c:1492

\_dbus_type_signature_next

void \_dbus_type_signature_next(const char \*type_str, int \*type_pos)

Skips to the next "complete" type inside a type signature.

**Definition** dbus-marshal-recursive.c:340

\_dbus_marshal_skip_basic

void \_dbus_marshal_skip_basic(const DBusString \*str, int type, int byte_order, int \*pos)

Skips over a basic-typed value, reporting the following position.

**Definition** dbus-marshal-basic.c:1130

dbus_free

void dbus_free(void \*memory)

Frees a block of memory previously allocated by dbus_malloc() or dbus_malloc0().

**Definition** dbus-memory.c:710

dbus_new

\#define dbus_new(type, count)

Safe macro for using dbus_malloc().

**Definition** dbus-memory.h:59

DBUS_DICT_ENTRY_END_CHAR

\#define DBUS_DICT_ENTRY_END_CHAR

Code marking the end of a dict entry type in a type signature.

**Definition** dbus-protocol.h:170

DBUS_TYPE_VARIANT

\#define DBUS_TYPE_VARIANT

Type code marking a D-Bus variant type.

**Definition** dbus-protocol.h:126

DBUS_STRUCT_BEGIN_CHAR

\#define DBUS_STRUCT_BEGIN_CHAR

Code marking the start of a struct type in a type signature.

**Definition** dbus-protocol.h:158

DBUS_TYPE_ARRAY

\#define DBUS_TYPE_ARRAY

Type code marking a D-Bus array type.

**Definition** dbus-protocol.h:122

DBUS_TYPE_INVALID

\#define DBUS_TYPE_INVALID

Type code that is never equal to a legitimate type code.

**Definition** dbus-protocol.h:62

DBUS_TYPE_DICT_ENTRY

\#define DBUS_TYPE_DICT_ENTRY

Type code used to represent a dict entry; however, this type code does not appear in type signatures,...

**Definition** dbus-protocol.h:145

DBUS_DICT_ENTRY_BEGIN_CHAR

\#define DBUS_DICT_ENTRY_BEGIN_CHAR

Code marking the start of a dict entry type in a type signature.

**Definition** dbus-protocol.h:166

DBUS_TYPE_STRUCT

\#define DBUS_TYPE_STRUCT

STRUCT and DICT_ENTRY are sort of special since their codes can't appear in a type string,...

**Definition** dbus-protocol.h:138

DBUS_STRUCT_END_CHAR

\#define DBUS_STRUCT_END_CHAR

Code marking the end of a struct type in a type signature.

**Definition** dbus-protocol.h:162

DBUS_TYPE_UINT32

\#define DBUS_TYPE_UINT32

Type code marking a 32-bit unsigned integer.

**Definition** dbus-protocol.h:88

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

\_dbus_string_equal_substring

dbus_bool_t \_dbus_string_equal_substring(const DBusString \*a, int a_start, int a_len, const DBusString \*b, int b_start)

Tests two sub-parts of two DBusString for equality.

**Definition** dbus-string.c:2166

\_dbus_string_init

dbus_bool_t \_dbus_string_init(DBusString \*str)

Initializes a string.

**Definition** dbus-string.c:182

\_dbus_string_alloc_space

dbus_bool_t \_dbus_string_alloc_space(DBusString \*str, int extra_bytes)

Preallocate extra_bytes such that a future lengthening of the string by extra_bytes is guaranteed to ...

**Definition** dbus-string.c:944

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_string_delete

void \_dbus_string_delete(DBusString \*str, int start, int len)

Deletes a segment of a DBusString with length len starting at start.

**Definition** dbus-string.c:1255

\_dbus_string_lengthen

dbus_bool_t \_dbus_string_lengthen(DBusString \*str, int additional_length)

Makes a string longer by the given number of bytes.

**Definition** dbus-string.c:805

\_dbus_string_insert_bytes

dbus_bool_t \_dbus_string_insert_bytes(DBusString \*str, int i, int n_bytes, unsigned char byte)

Inserts a number of bytes of a given value at the given position.

**Definition** dbus-string.c:629

\_dbus_string_get_length

int \_dbus_string_get_length(const DBusString \*str)

Gets the length of a string (not including nul termination).

**Definition** dbus-string.c:784

\_dbus_string_insert_byte

dbus_bool_t \_dbus_string_insert_byte(DBusString \*str, int i, unsigned char byte)

Inserts a single byte at the given position.

**Definition** dbus-string.c:659

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

\_dbus_string_copy_len

dbus_bool_t \_dbus_string_copy_len(const DBusString \*source, int start, int len, DBusString \*dest, int insert_at)

Like \_dbus_string_copy(), but can copy a segment from the middle of the source string.

**Definition** dbus-string.c:1437

\_dbus_string_replace_len

dbus_bool_t \_dbus_string_replace_len(const DBusString \*source, int start, int len, DBusString \*dest, int replace_at, int replace_len)

Replaces a segment of dest string with a segment of source string.

**Definition** dbus-string.c:1466

DBusArrayLenFixup

When modifying an existing block of values, array lengths may need to be adjusted; those adjustments ...

**Definition** dbus-marshal-recursive.h:97

DBusArrayLenFixup::new_len

int new_len

the new value of the length in the written-out block

**Definition** dbus-marshal-recursive.h:99

DBusArrayLenFixup::len_pos_in_reader

int len_pos_in_reader

where the length was in the original block

**Definition** dbus-marshal-recursive.h:98

DBusList

A node in a linked list.

**Definition** dbus-list.h:37

DBusList::data

void \* data

Data stored at this element.

**Definition** dbus-list.h:40

DBusString

**Definition** dbus-string.h:47

DBusTypeReaderClass

Virtual table for a type reader.

**Definition** dbus-marshal-recursive.c:128

DBusTypeReaderClass::next

void(\* next)(DBusTypeReader \*reader, int current_type)

go to the next value

**Definition** dbus-marshal-recursive.c:135

DBusTypeReaderClass::id

int id

index in all_reader_classes

**Definition** dbus-marshal-recursive.c:130

DBusTypeReaderClass::check_finished

dbus_bool_t(\* check_finished)(const DBusTypeReader \*reader)

check whether reader is at the end

**Definition** dbus-marshal-recursive.c:134

DBusTypeReaderClass::recurse

void(\* recurse)(DBusTypeReader \*sub, DBusTypeReader \*parent)

recurse with this reader as sub

**Definition** dbus-marshal-recursive.c:132

DBusTypeReaderClass::types_only

dbus_bool_t types_only

only iterates over types, not values

**Definition** dbus-marshal-recursive.c:131

DBusTypeReaderClass::name

const char \* name

name for debugging

**Definition** dbus-marshal-recursive.c:129

DBusTypeReader

The type reader is an iterator for reading values from a block of values.

**Definition** dbus-marshal-recursive.h:42

DBusTypeReader::type_pos

int type_pos

current position in signature

**Definition** dbus-marshal-recursive.h:53

DBusTypeReader::klass

const DBusTypeReaderClass \* klass

the vtable for the reader

**Definition** dbus-marshal-recursive.h:43

DBusTypeReader::u

union DBusTypeReader::@1 u

class-specific data

DBusTypeReader::value_str

const DBusString \* value_str

string containing values of block

**Definition** dbus-marshal-recursive.h:45

DBusTypeReader::finished

dbus_uint32_t finished

marks we're at end iterator for cases where we don't have another way to tell

**Definition** dbus-marshal-recursive.h:49

DBusTypeReader::start_pos

int start_pos

for array readers, the start of the array values

**Definition** dbus-marshal-recursive.h:59

DBusTypeReader::array_len_offset

dbus_uint32_t array_len_offset

bytes back from start_pos that len ends

**Definition** dbus-marshal-recursive.h:52

DBusTypeReader::value_pos

int value_pos

current position in values

**Definition** dbus-marshal-recursive.h:54

DBusTypeReader::byte_order

dbus_uint32_t byte_order

byte order of the block

**Definition** dbus-marshal-recursive.h:47

DBusTypeReader::type_str

const DBusString \* type_str

string containing signature of block

**Definition** dbus-marshal-recursive.h:44

DBusTypeWriter

The type writer is an iterator for writing to a block of values.

**Definition** dbus-marshal-recursive.h:68

DBusTypeWriter::element_type_pos

int element_type_pos

position of array element type in type_str

**Definition** dbus-marshal-recursive.h:87

DBusTypeWriter::start_pos

int start_pos

position of first element in the array

**Definition** dbus-marshal-recursive.h:85

DBusTypeWriter::value_pos

int value_pos

next position to write

**Definition** dbus-marshal-recursive.h:80

DBusTypeWriter::enabled

dbus_uint32_t enabled

whether to write values

**Definition** dbus-marshal-recursive.h:77

DBusTypeWriter::u

union DBusTypeWriter::@3 u

class-specific data

DBusTypeWriter::byte_order

dbus_uint32_t byte_order

byte order to write values with

**Definition** dbus-marshal-recursive.h:71

DBusTypeWriter::type_pos

int type_pos

current pos in type_str

**Definition** dbus-marshal-recursive.h:79

DBusTypeWriter::type_str

DBusString \* type_str

where to write typecodes (or read type expectations)

**Definition** dbus-marshal-recursive.h:69

DBusTypeWriter::len_pos

int len_pos

position of length of the array

**Definition** dbus-marshal-recursive.h:86

DBusTypeWriter::value_str

DBusString \* value_str

where to write values

**Definition** dbus-marshal-recursive.h:70

DBusTypeWriter::container_type

dbus_uint32_t container_type

what are we inside? (e.g.

**Definition** dbus-marshal-recursive.h:73

DBusTypeWriter::type_pos_is_expectation

dbus_uint32_t type_pos_is_expectation

type_pos can be either an insertion point for or an expected next type

**Definition** dbus-marshal-recursive.h:75

ReplacementBlock

**Definition** dbus-marshal-recursive.c:1135

ReplacementBlock::padding

int padding

How much of the replacement block is padding.

**Definition** dbus-marshal-recursive.c:1137

ReplacementBlock::replacement

DBusString replacement

Marshaled value including alignment padding.

**Definition** dbus-marshal-recursive.c:1136

DBusBasicValue

A simple value union that lets you access bytes as if they were various types; useful when dealing wi...

**Definition** dbus-types.h:161
