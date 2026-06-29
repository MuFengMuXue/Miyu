dbus-marshal-validate.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-marshal-validate.c Validation routines for marshaled data

3 \*

4 \* Copyright (C) 2005 Red Hat, Inc.

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

28\#include "dbus-marshal-validate.h"

29\#include "dbus-marshal-recursive.h"

30\#include "dbus-marshal-basic.h"

31\#include "dbus-signature.h"

32\#include "dbus-string.h"

33

52DBusValidity

53\_dbus_validate_signature_with_reason (const DBusString \*type_str,

54 int type_pos,

55 int len)

56{

57 const unsigned char \*p;

58 const unsigned char \*end;

59 int last;

60 int struct_depth;

61 int array_depth;

62 int dict_entry_depth;

63 DBusValidity result;

64

65 int element_count;

66 DBusList \*element_count_stack;

67 char opened_brackets\[DBUS_MAXIMUM_TYPE_RECURSION_DEPTH \* 2 + 1\] = { '\0' };

68 char last_bracket;

69

70 result = DBUS_VALID;

71 element_count_stack = NULL;

72

73 if (!\_dbus_list_append (&element_count_stack, \_DBUS_INT_TO_POINTER (0)))

74 {

75 result = DBUS_VALIDITY_UNKNOWN_OOM_ERROR;

76 goto out;

77 }

78

79 \_dbus_assert (type_str != NULL);

80 \_dbus_assert (type_pos \< \_DBUS_INT32_MAX - len);

81 \_dbus_assert (len \>= 0);

82 \_dbus_assert (type_pos \>= 0);

83

84 if (len \> DBUS_MAXIMUM_SIGNATURE_LENGTH)

85 {

86 result = DBUS_INVALID_SIGNATURE_TOO_LONG;

87 goto out;

88 }

89

90 p = \_dbus_string_get_const_udata_len (type_str, type_pos, 0);

91

92 end = \_dbus_string_get_const_udata_len (type_str, type_pos + len, 0);

93 struct_depth = 0;

94 array_depth = 0;

95 dict_entry_depth = 0;

96 last = DBUS_TYPE_INVALID;

97

98 while (p != end)

99 {

100 \_dbus_assert (struct_depth + dict_entry_depth \>= 0);

101 \_dbus_assert (struct_depth + dict_entry_depth \< \_DBUS_N_ELEMENTS (opened_brackets));

102 \_dbus_assert (opened_brackets\[struct_depth + dict_entry_depth\] == '\0');

103

104 switch (\*p)

105 {

106 case DBUS_TYPE_BYTE:

107 case DBUS_TYPE_BOOLEAN:

108 case DBUS_TYPE_INT16:

109 case DBUS_TYPE_UINT16:

110 case DBUS_TYPE_INT32:

111 case DBUS_TYPE_UINT32:

112 case DBUS_TYPE_UNIX_FD:

113 case DBUS_TYPE_INT64:

114 case DBUS_TYPE_UINT64:

115 case DBUS_TYPE_DOUBLE:

116 case DBUS_TYPE_STRING:

117 case DBUS_TYPE_OBJECT_PATH:

118 case DBUS_TYPE_SIGNATURE:

119 case DBUS_TYPE_VARIANT:

120 break;

121

122 case DBUS_TYPE_ARRAY:

123 array_depth += 1;

124 if (array_depth \> DBUS_MAXIMUM_TYPE_RECURSION_DEPTH)

125 {

126 result = DBUS_INVALID_EXCEEDED_MAXIMUM_ARRAY_RECURSION;

127 goto out;

128 }

129 break;

130

131 case DBUS_STRUCT_BEGIN_CHAR:

132 struct_depth += 1;

133

134 if (struct_depth \> DBUS_MAXIMUM_TYPE_RECURSION_DEPTH)

135 {

136 result = DBUS_INVALID_EXCEEDED_MAXIMUM_STRUCT_RECURSION;

137 goto out;

138 }

139

140 if (!\_dbus_list_append (&element_count_stack,

141 \_DBUS_INT_TO_POINTER (0)))

142 {

143 result = DBUS_VALIDITY_UNKNOWN_OOM_ERROR;

144 goto out;

145 }

146

147 \_dbus_assert (struct_depth + dict_entry_depth \>= 1);

148 \_dbus_assert (struct_depth + dict_entry_depth \< \_DBUS_N_ELEMENTS (opened_brackets));

149 \_dbus_assert (opened_brackets\[struct_depth + dict_entry_depth - 1\] == '\0');

150 opened_brackets\[struct_depth + dict_entry_depth - 1\] = DBUS_STRUCT_BEGIN_CHAR;

151 break;

152

153 case DBUS_STRUCT_END_CHAR:

154 if (struct_depth == 0)

155 {

156 result = DBUS_INVALID_STRUCT_ENDED_BUT_NOT_STARTED;

157 goto out;

158 }

159

160 if (last == DBUS_STRUCT_BEGIN_CHAR)

161 {

162 result = DBUS_INVALID_STRUCT_HAS_NO_FIELDS;

163 goto out;

164 }

165

166 \_dbus_assert (struct_depth + dict_entry_depth \>= 1);

167 \_dbus_assert (struct_depth + dict_entry_depth \< \_DBUS_N_ELEMENTS (opened_brackets));

168 last_bracket = opened_brackets\[struct_depth + dict_entry_depth - 1\];

169

170 if (last_bracket != DBUS_STRUCT_BEGIN_CHAR)

171 {

172 result = DBUS_INVALID_STRUCT_ENDED_BUT_NOT_STARTED;

173 goto out;

174 }

175

176 \_dbus_list_pop_last (&element_count_stack);

177

178 struct_depth -= 1;

179 opened_brackets\[struct_depth + dict_entry_depth\] = '\0';

180 break;

181

182 case DBUS_DICT_ENTRY_BEGIN_CHAR:

183 if (last != DBUS_TYPE_ARRAY)

184 {

185 result = DBUS_INVALID_DICT_ENTRY_NOT_INSIDE_ARRAY;

186 goto out;

187 }

188

189 dict_entry_depth += 1;

190

191 if (dict_entry_depth \> DBUS_MAXIMUM_TYPE_RECURSION_DEPTH)

192 {

193 result = DBUS_INVALID_EXCEEDED_MAXIMUM_DICT_ENTRY_RECURSION;

194 goto out;

195 }

196

197 if (!\_dbus_list_append (&element_count_stack,

198 \_DBUS_INT_TO_POINTER (0)))

199 {

200 result = DBUS_VALIDITY_UNKNOWN_OOM_ERROR;

201 goto out;

202 }

203

204 \_dbus_assert (struct_depth + dict_entry_depth \>= 1);

205 \_dbus_assert (struct_depth + dict_entry_depth \< \_DBUS_N_ELEMENTS (opened_brackets));

206 \_dbus_assert (opened_brackets\[struct_depth + dict_entry_depth - 1\] == '\0');

207 opened_brackets\[struct_depth + dict_entry_depth - 1\] = DBUS_DICT_ENTRY_BEGIN_CHAR;

208 break;

209

210 case DBUS_DICT_ENTRY_END_CHAR:

211 if (dict_entry_depth == 0)

212 {

213 result = DBUS_INVALID_DICT_ENTRY_ENDED_BUT_NOT_STARTED;

214 goto out;

215 }

216

217 \_dbus_assert (struct_depth + dict_entry_depth \>= 1);

218 \_dbus_assert (struct_depth + dict_entry_depth \< \_DBUS_N_ELEMENTS (opened_brackets));

219 last_bracket = opened_brackets\[struct_depth + dict_entry_depth - 1\];

220

221 if (last_bracket != DBUS_DICT_ENTRY_BEGIN_CHAR)

222 {

223 result = DBUS_INVALID_DICT_ENTRY_ENDED_BUT_NOT_STARTED;

224 goto out;

225 }

226

227 dict_entry_depth -= 1;

228 opened_brackets\[struct_depth + dict_entry_depth\] = '\0';

229

230 element_count =

231 \_DBUS_POINTER_TO_INT (\_dbus_list_pop_last (&element_count_stack));

232

233 if (element_count != 2)

234 {

235 if (element_count == 0)

236 result = DBUS_INVALID_DICT_ENTRY_HAS_NO_FIELDS;

237 else if (element_count == 1)

238 result = DBUS_INVALID_DICT_ENTRY_HAS_ONLY_ONE_FIELD;

239 else

240 result = DBUS_INVALID_DICT_ENTRY_HAS_TOO_MANY_FIELDS;

241

242 goto out;

243 }

244 break;

245

246 case DBUS_TYPE_STRUCT: /\* doesn't appear in signatures \*/

247 case DBUS_TYPE_DICT_ENTRY: /\* ditto \*/

248 default:

249 result = DBUS_INVALID_UNKNOWN_TYPECODE;

250 goto out;

251 }

252

253 if (\*p != DBUS_TYPE_ARRAY &&

254 \*p != DBUS_DICT_ENTRY_BEGIN_CHAR &&

255 \*p != DBUS_STRUCT_BEGIN_CHAR)

256 {

257 element_count =

258 \_DBUS_POINTER_TO_INT (\_dbus_list_pop_last (&element_count_stack));

259

260 ++element_count;

261

262 if (!\_dbus_list_append (&element_count_stack,

263 \_DBUS_INT_TO_POINTER (element_count)))

264 {

265 result = DBUS_VALIDITY_UNKNOWN_OOM_ERROR;

266 goto out;

267 }

268 }

269

270 if (array_depth \> 0)

271 {

272 if (\*p == DBUS_TYPE_ARRAY && p != end)

273 {

274 const unsigned char \*p1;

275 p1 = p + 1;

276 if (\*p1 == DBUS_STRUCT_END_CHAR \|\|

277 \*p1 == DBUS_DICT_ENTRY_END_CHAR)

278 {

279 result = DBUS_INVALID_MISSING_ARRAY_ELEMENT_TYPE;

280 goto out;

281 }

282 }

283 else

284 {

285 array_depth = 0;

286 }

287 }

288

289 if (last == DBUS_DICT_ENTRY_BEGIN_CHAR)

290 {

291 if (!(dbus_type_is_valid (\*p) && dbus_type_is_basic (\*p)))

292 {

293 result = DBUS_INVALID_DICT_KEY_MUST_BE_BASIC_TYPE;

294 goto out;

295 }

296 }

297

298 last = \*p;

299 ++p;

300 }

301

302

303 if (array_depth \> 0)

304 {

305 result = DBUS_INVALID_MISSING_ARRAY_ELEMENT_TYPE;

306 goto out;

307 }

308

309 if (struct_depth \> 0)

310 {

311 result = DBUS_INVALID_STRUCT_STARTED_BUT_NOT_ENDED;

312 goto out;

313 }

314

315 if (dict_entry_depth \> 0)

316 {

317 result = DBUS_INVALID_DICT_ENTRY_STARTED_BUT_NOT_ENDED;

318 goto out;

319 }

320

321 \_dbus_assert (last != DBUS_TYPE_ARRAY);

322 \_dbus_assert (last != DBUS_STRUCT_BEGIN_CHAR);

323 \_dbus_assert (last != DBUS_DICT_ENTRY_BEGIN_CHAR);

324

325 result = DBUS_VALID;

326

327out:

328 \_dbus_list_clear (&element_count_stack);

329 return result;

330}

331

332/\* note: this function is also used to validate the header's values,

333 \* since the header is a valid body with a particular signature.

334 \*/

335static DBusValidity

336validate_body_helper (DBusTypeReader \*reader,

337 int byte_order,

338 dbus_bool_t walk_reader_to_end,

339 int total_depth,

340 const unsigned char \*p,

341 const unsigned char \*end,

342 const unsigned char \*\*new_p)

343{

344 int current_type;

345

346 /\* The spec allows arrays and structs to each nest 32, for total

347 \* nesting of 2\*32. We want to impose the same limit on "dynamic"

348 \* value nesting (not visible in the signature) which is introduced

349 \* by DBUS_TYPE_VARIANT.

350 \*/

351 if (total_depth \> (DBUS_MAXIMUM_TYPE_RECURSION_DEPTH \* 2))

352 {

353 return DBUS_INVALID_NESTED_TOO_DEEPLY;

354 }

355

356 while ((current_type = \_dbus_type_reader_get_current_type (reader)) != DBUS_TYPE_INVALID)

357 {

358 const unsigned char \*a;

359 int alignment;

360

361\#if 0

362 \_dbus_verbose (" validating value of type %s type reader %p type_pos %d p %p end %p %d remain\n",

363 \_dbus_type_to_string (current_type), reader, reader-\>type_pos, p, end,

364 (int) (end - p));

365\#endif

366

367 /\* Guarantee that p has one byte to look at \*/

368 if (p == end)

369 return DBUS_INVALID_NOT_ENOUGH_DATA;

370

371 switch (current_type)

372 {

373 /\* Special case of fixed-length types: every byte is valid \*/

374 case DBUS_TYPE_BYTE:

375 ++p;

376 break;

377

378 /\* Multi-byte fixed-length types require padding to their alignment \*/

379 case DBUS_TYPE_BOOLEAN:

380 case DBUS_TYPE_INT16:

381 case DBUS_TYPE_UINT16:

382 case DBUS_TYPE_INT32:

383 case DBUS_TYPE_UINT32:

384 case DBUS_TYPE_UNIX_FD:

385 case DBUS_TYPE_INT64:

386 case DBUS_TYPE_UINT64:

387 case DBUS_TYPE_DOUBLE:

388 alignment = \_dbus_type_get_alignment (current_type);

389 a = \_DBUS_ALIGN_ADDRESS (p, alignment);

390 if (a \>= end)

391 return DBUS_INVALID_NOT_ENOUGH_DATA;

392 while (p != a)

393 {

394 if (\*p != '\0')

395 return DBUS_INVALID_ALIGNMENT_PADDING_NOT_NUL;

396 ++p;

397 }

398

399 if (current_type == DBUS_TYPE_BOOLEAN)

400 {

401 dbus_uint32_t v;

402

403 if (p + 4 \> end)

404 return DBUS_INVALID_NOT_ENOUGH_DATA;

405

406 v = \_dbus_unpack_uint32 (byte_order, p);

407

408 if (!(v == 0 \|\| v == 1))

409 return DBUS_INVALID_BOOLEAN_NOT_ZERO_OR_ONE;

410 }

411

412 p += alignment;

413 break;

414

415 /\* Types that start with a 4-byte length \*/

416 case DBUS_TYPE_ARRAY:

417 case DBUS_TYPE_STRING:

418 case DBUS_TYPE_OBJECT_PATH:

419 {

420 dbus_uint32_t claimed_len;

421

422 a = \_DBUS_ALIGN_ADDRESS (p, 4);

423 if (a + 4 \> end)

424 return DBUS_INVALID_NOT_ENOUGH_DATA;

425 while (p != a)

426 {

427 if (\*p != '\0')

428 return DBUS_INVALID_ALIGNMENT_PADDING_NOT_NUL;

429 ++p;

430 }

431

432 claimed_len = \_dbus_unpack_uint32 (byte_order, p);

433 p += 4;

434

435 /\* p may now be == end \*/

436 \_dbus_assert (p \<= end);

437

438 /\* Arrays have padding between the length and the first

439 \* array item, if it's necessary for the array's element type.

440 \* This padding is not counted as part of the length

441 \* claimed_len. \*/

442 if (current_type == DBUS_TYPE_ARRAY)

443 {

444 int array_elem_type = \_dbus_type_reader_get_element_type (reader);

445

446 if (!dbus_type_is_valid (array_elem_type))

447 {

448 return DBUS_INVALID_UNKNOWN_TYPECODE;

449 }

450

451 alignment = \_dbus_type_get_alignment (array_elem_type);

452

453 a = \_DBUS_ALIGN_ADDRESS (p, alignment);

454

455 /\* a may now be == end \*/

456 if (a \> end)

457 return DBUS_INVALID_NOT_ENOUGH_DATA;

458

459 while (p != a)

460 {

461 if (\*p != '\0')

462 return DBUS_INVALID_ALIGNMENT_PADDING_NOT_NUL;

463 ++p;

464 }

465 }

466

467 if (claimed_len \> (unsigned long) (end - p))

468 return DBUS_INVALID_LENGTH_OUT_OF_BOUNDS;

469

470 if (current_type == DBUS_TYPE_OBJECT_PATH)

471 {

472 DBusString str;

473 \_dbus_string_init_const_len (&str, (const char \*) p, claimed_len);

474 if (!\_dbus_validate_path (&str, 0,

475 \_dbus_string_get_length (&str)))

476 return DBUS_INVALID_BAD_PATH;

477

478 p += claimed_len;

479 }

480 else if (current_type == DBUS_TYPE_STRING)

481 {

482 DBusString str;

483 \_dbus_string_init_const_len (&str, (const char \*) p, claimed_len);

484 if (!\_dbus_string_validate_utf8 (&str, 0,

485 \_dbus_string_get_length (&str)))

486 return DBUS_INVALID_BAD_UTF8_IN_STRING;

487

488 p += claimed_len;

489 }

490 else if (current_type == DBUS_TYPE_ARRAY && claimed_len \> 0)

491 {

492 DBusTypeReader sub;

493 DBusValidity validity;

494 const unsigned char \*array_end;

495 int array_elem_type;

496

497 if (claimed_len \> DBUS_MAXIMUM_ARRAY_LENGTH)

498 return DBUS_INVALID_ARRAY_LENGTH_EXCEEDS_MAXIMUM;

499

500 /\* Remember that the reader is types only, so we can't

501 \* use it to iterate over elements. It stays the same

502 \* for all elements.

503 \*/

504 \_dbus_type_reader_recurse (reader, &sub);

505

506 array_end = p + claimed_len;

507 /\* We effectively already checked this, by checking that

508 \* claimed_len \<= (end - p) \*/

509 \_dbus_assert (array_end \<= end);

510

511 array_elem_type = \_dbus_type_reader_get_element_type (reader);

512

513 /\* avoid recursive call to validate_body_helper if this is an array

514 \* of fixed-size elements

515 \*/

516 if (dbus_type_is_fixed (array_elem_type))

517 {

518 /\* Note that fixed-size types all have sizes equal to

519 \* their alignments, so this is really the item size. \*/

520 alignment = \_dbus_type_get_alignment (array_elem_type);

521 \_dbus_assert (alignment == 1 \|\| alignment == 2 \|\|

522 alignment == 4 \|\| alignment == 8);

523

524 /\* Because the alignment is a power of 2, this is

525 \* equivalent to: (claimed_len % alignment) != 0,

526 \* but avoids slower integer division \*/

527 if ((claimed_len & (alignment - 1)) != 0)

528 return DBUS_INVALID_ARRAY_LENGTH_INCORRECT;

529

530 /\* bools need to be handled differently, because they can

531 \* have an invalid value

532 \*/

533 if (array_elem_type == DBUS_TYPE_BOOLEAN)

534 {

535 dbus_uint32_t v;

536

537 while (p \< array_end)

538 {

539 v = \_dbus_unpack_uint32 (byte_order, p);

540

541 if (!(v == 0 \|\| v == 1))

542 return DBUS_INVALID_BOOLEAN_NOT_ZERO_OR_ONE;

543

544 p += alignment;

545 }

546 }

547

548 else

549 {

550 p = array_end;

551 }

552 }

553

554 else

555 {

556 while (p \< array_end)

557 {

558 validity = validate_body_helper (&sub, byte_order, FALSE,

559 total_depth + 1,

560 p, end, &p);

561 if (validity != DBUS_VALID)

562 return validity;

563 }

564 }

565

566 if (p != array_end)

567 return DBUS_INVALID_ARRAY_LENGTH_INCORRECT;

568 }

569

570 /\* check nul termination \*/

571 if (current_type != DBUS_TYPE_ARRAY)

572 {

573 if (p == end)

574 return DBUS_INVALID_NOT_ENOUGH_DATA;

575

576 if (\*p != '\0')

577 return DBUS_INVALID_STRING_MISSING_NUL;

578 ++p;

579 }

580 }

581 break;

582

583 case DBUS_TYPE_SIGNATURE:

584 {

585 dbus_uint32_t claimed_len;

586 DBusString str;

587 DBusValidity validity;

588

589 claimed_len = \*p;

590 ++p;

591

592 /\* 1 is for nul termination \*/

593 if (claimed_len + 1 \> (unsigned long) (end - p))

594 return DBUS_INVALID_SIGNATURE_LENGTH_OUT_OF_BOUNDS;

595

596 \_dbus_string_init_const_len (&str, (const char \*) p, claimed_len);

597 validity =

598 \_dbus_validate_signature_with_reason (&str, 0,

599 \_dbus_string_get_length (&str));

600

601 if (validity != DBUS_VALID)

602 return validity;

603

604 p += claimed_len;

605

606 \_dbus_assert (p \< end);

607 if (\*p != DBUS_TYPE_INVALID)

608 return DBUS_INVALID_SIGNATURE_MISSING_NUL;

609

610 ++p;

611

612 \_dbus_verbose ("p = %p end = %p claimed_len %u\n", p, end, claimed_len);

613 }

614 break;

615

616 case DBUS_TYPE_VARIANT:

617 {

618 /\* 1 byte sig len, sig typecodes, align to

619 \* contained-type-boundary, values.

620 \*/

621

622 /\* In addition to normal signature validation, we need to be sure

623 \* the signature contains only a single (possibly container) type.

624 \*/

625 dbus_uint32_t claimed_len;

626 DBusString sig;

627 DBusTypeReader sub;

628 DBusValidity validity;

629 int contained_alignment;

630 int contained_type;

631 DBusValidity reason;

632

633 claimed_len = \*p;

634 ++p;

635

636 /\* + 1 for nul \*/

637 if (claimed_len + 1 \> (unsigned long) (end - p))

638 return DBUS_INVALID_VARIANT_SIGNATURE_LENGTH_OUT_OF_BOUNDS;

639

640 \_dbus_string_init_const_len (&sig, (const char \*) p, claimed_len);

641 reason = \_dbus_validate_signature_with_reason (&sig, 0,

642 \_dbus_string_get_length (&sig));

643 if (!(reason == DBUS_VALID))

644 {

645 if (reason == DBUS_VALIDITY_UNKNOWN_OOM_ERROR)

646 return reason;

647 else

648 return DBUS_INVALID_VARIANT_SIGNATURE_BAD;

649 }

650

651 p += claimed_len;

652

653 if (\*p != DBUS_TYPE_INVALID)

654 return DBUS_INVALID_VARIANT_SIGNATURE_MISSING_NUL;

655 ++p;

656

657 contained_type = \_dbus_first_type_in_signature (&sig, 0);

658 if (contained_type == DBUS_TYPE_INVALID)

659 return DBUS_INVALID_VARIANT_SIGNATURE_EMPTY;

660

661 contained_alignment = \_dbus_type_get_alignment (contained_type);

662

663 a = \_DBUS_ALIGN_ADDRESS (p, contained_alignment);

664 if (a \> end)

665 return DBUS_INVALID_NOT_ENOUGH_DATA;

666 while (p != a)

667 {

668 if (\*p != '\0')

669 return DBUS_INVALID_ALIGNMENT_PADDING_NOT_NUL;

670 ++p;

671 }

672

673 \_dbus_type_reader_init_types_only (&sub, &sig, 0);

674

675 \_dbus_assert (\_dbus_type_reader_get_current_type (&sub) != DBUS_TYPE_INVALID);

676

677 validity = validate_body_helper (&sub, byte_order, FALSE,

678 total_depth + 1,

679 p, end, &p);

680 if (validity != DBUS_VALID)

681 return validity;

682

683 if (\_dbus_type_reader_next (&sub))

684 return DBUS_INVALID_VARIANT_SIGNATURE_SPECIFIES_MULTIPLE_VALUES;

685

686 \_dbus_assert (\_dbus_type_reader_get_current_type (&sub) == DBUS_TYPE_INVALID);

687 }

688 break;

689

690 case DBUS_TYPE_DICT_ENTRY:

691 case DBUS_TYPE_STRUCT:

692 {

693 DBusTypeReader sub;

694 DBusValidity validity;

695

696 a = \_DBUS_ALIGN_ADDRESS (p, 8);

697 if (a \> end)

698 return DBUS_INVALID_NOT_ENOUGH_DATA;

699 while (p != a)

700 {

701 if (\*p != '\0')

702 return DBUS_INVALID_ALIGNMENT_PADDING_NOT_NUL;

703 ++p;

704 }

705

706 \_dbus_type_reader_recurse (reader, &sub);

707

708 validity = validate_body_helper (&sub, byte_order, TRUE,

709 total_depth + 1,

710 p, end, &p);

711 if (validity != DBUS_VALID)

712 return validity;

713 }

714 break;

715

716 default:

717 \_dbus_assert_not_reached ("invalid typecode in supposedly-validated signature");

718 break;

719 }

720

721\#if 0

722 \_dbus_verbose (" validated value of type %s type reader %p type_pos %d p %p end %p %d remain\n",

723 \_dbus_type_to_string (current_type), reader, reader-\>type_pos, p, end,

724 (int) (end - p));

725\#endif

726

727 if (p \> end)

728 {

729 \_dbus_verbose ("not enough data!!! p = %p end = %p end-p = %d\n",

730 p, end, (int) (end - p));

731 return DBUS_INVALID_NOT_ENOUGH_DATA;

732 }

733

734 if (walk_reader_to_end)

735 \_dbus_type_reader_next (reader);

736 else

737 break;

738 }

739

740 if (new_p)

741 \*new_p = p;

742

743 return DBUS_VALID;

744}

745

766DBusValidity

767\_dbus_validate_body_with_reason (const DBusString \*expected_signature,

768 int expected_signature_start,

769 int byte_order,

770 int \*bytes_remaining,

771 const DBusString \*value_str,

772 int value_pos,

773 int len)

774{

775 DBusTypeReader reader;

776 const unsigned char \*p;

777 const unsigned char \*end;

778 DBusValidity validity;

779

780 \_dbus_assert (len \>= 0);

781 \_dbus_assert (value_pos \>= 0);

782 \_dbus_assert (value_pos \<= \_dbus_string_get_length (value_str) - len);

783

784 \_dbus_verbose ("validating body from pos %d len %d sig '%s'\n",

785 value_pos, len, \_dbus_string_get_const_data_len (expected_signature,

786 expected_signature_start,

787 0));

788

789 \_dbus_type_reader_init_types_only (&reader,

790 expected_signature, expected_signature_start);

791

792 p = \_dbus_string_get_const_udata_len (value_str, value_pos, len);

793 end = p + len;

794

795 validity = validate_body_helper (&reader, byte_order, TRUE, 0, p, end, &p);

796 if (validity != DBUS_VALID)

797 return validity;

798

799 if (bytes_remaining)

800 {

801 \*bytes_remaining = end - p;

802 return DBUS_VALID;

803 }

804 else if (p \< end)

805 return DBUS_INVALID_TOO_MUCH_DATA;

806 else

807 {

808 \_dbus_assert (p == end);

809 return DBUS_VALID;

810 }

811}

812

817\#define VALID_INITIAL_NAME_CHARACTER(c) \\

818 ( ((c) \>= 'A' && (c) \<= 'Z') \|\| \\

819 ((c) \>= 'a' && (c) \<= 'z') \|\| \\

820 ((c) == '\_') )

821

826\#define VALID_NAME_CHARACTER(c) \\

827 ( ((c) \>= '0' && (c) \<= '9') \|\| \\

828 ((c) \>= 'A' && (c) \<= 'Z') \|\| \\

829 ((c) \>= 'a' && (c) \<= 'z') \|\| \\

830 ((c) == '\_') )

831

848dbus_bool_t

849\_dbus_validate_path (const DBusString \*str,

850 int start,

851 int len)

852{

853 const unsigned char \*s;

854 const unsigned char \*end;

855 const unsigned char \*last_slash;

856

857 \_dbus_assert (start \>= 0);

858 \_dbus_assert (len \>= 0);

859 \_dbus_assert (start \<= \_dbus_string_get_length (str));

860

861 if (len \> \_dbus_string_get_length (str) - start)

862 return FALSE;

863

864 if (len == 0)

865 return FALSE;

866

867 s = \_dbus_string_get_const_udata (str) + start;

868 end = s + len;

869

870 if (\*s != '/')

871 return FALSE;

872 last_slash = s;

873 ++s;

874

875 while (s != end)

876 {

877 if (\*s == '/')

878 {

879 if ((s - last_slash) \< 2)

880 return FALSE; /\* no empty path components allowed \*/

881

882 last_slash = s;

883 }

884 else

885 {

886 if (\_DBUS_UNLIKELY (!VALID_NAME_CHARACTER (\*s)))

887 return FALSE;

888 }

889

890 ++s;

891 }

892

893 if ((end - last_slash) \< 2 &&

894 len \> 1)

895 return FALSE; /\* trailing slash not allowed unless the string is "/" \*/

896

897 return TRUE;

898}

899

900const char \*

901\_dbus_validity_to_error_message (DBusValidity validity)

902{

903 switch (validity)

904 {

905 case DBUS_VALIDITY_UNKNOWN_OOM_ERROR: return "Out of memory";

906 case DBUS_INVALID_FOR_UNKNOWN_REASON: return "Unknown reason";

907 case DBUS_VALID_BUT_INCOMPLETE: return "Valid but incomplete";

908 case DBUS_VALIDITY_UNKNOWN: return "Validity unknown";

909 case DBUS_VALID: return "Valid";

910 case DBUS_INVALID_UNKNOWN_TYPECODE: return "Unknown typecode";

911 case DBUS_INVALID_MISSING_ARRAY_ELEMENT_TYPE: return "Missing array element type";

912 case DBUS_INVALID_SIGNATURE_TOO_LONG: return "Signature is too long";

913 case DBUS_INVALID_EXCEEDED_MAXIMUM_ARRAY_RECURSION: return "Exceeded maximum array recursion";

914 case DBUS_INVALID_EXCEEDED_MAXIMUM_STRUCT_RECURSION: return "Exceeded maximum struct recursion";

915 case DBUS_INVALID_STRUCT_ENDED_BUT_NOT_STARTED: return "Struct ended but not started";

916 case DBUS_INVALID_STRUCT_STARTED_BUT_NOT_ENDED: return "Struct started but not ended";

917 case DBUS_INVALID_STRUCT_HAS_NO_FIELDS: return "Struct has no fields";

918 case DBUS_INVALID_ALIGNMENT_PADDING_NOT_NUL: return "Alignment padding not null";

919 case DBUS_INVALID_BOOLEAN_NOT_ZERO_OR_ONE: return "Boolean is not zero or one";

920 case DBUS_INVALID_NOT_ENOUGH_DATA: return "Not enough data";

921 case DBUS_INVALID_TOO_MUCH_DATA: return "Too much data";

922 case DBUS_INVALID_BAD_BYTE_ORDER: return "Bad byte order";

923 case DBUS_INVALID_BAD_PROTOCOL_VERSION: return "Bad protocol version";

924 case DBUS_INVALID_BAD_MESSAGE_TYPE: return "Bad message type";

925 case DBUS_INVALID_BAD_SERIAL: return "Bad serial";

926 case DBUS_INVALID_INSANE_FIELDS_ARRAY_LENGTH: return "Insane fields array length";

927 case DBUS_INVALID_INSANE_BODY_LENGTH: return "Insane body length";

928 case DBUS_INVALID_MESSAGE_TOO_LONG: return "Message too long";

929 case DBUS_INVALID_HEADER_FIELD_CODE: return "Header field code";

930 case DBUS_INVALID_HEADER_FIELD_HAS_WRONG_TYPE: return "Header field has wrong type";

931 case DBUS_INVALID_USES_LOCAL_INTERFACE: return "Uses local interface";

932 case DBUS_INVALID_USES_LOCAL_PATH: return "Uses local path";

933 case DBUS_INVALID_HEADER_FIELD_APPEARS_TWICE: return "Header field appears twice";

934 case DBUS_INVALID_BAD_DESTINATION: return "Bad destination";

935 case DBUS_INVALID_BAD_INTERFACE: return "Bad interface";

936 case DBUS_INVALID_BAD_MEMBER: return "Bad member";

937 case DBUS_INVALID_BAD_ERROR_NAME: return "Bad error name";

938 case DBUS_INVALID_BAD_SENDER: return "Bad sender";

939 case DBUS_INVALID_MISSING_PATH: return "Missing path";

940 case DBUS_INVALID_MISSING_INTERFACE: return "Missing interface";

941 case DBUS_INVALID_MISSING_MEMBER: return "Missing member";

942 case DBUS_INVALID_MISSING_ERROR_NAME: return "Missing error name";

943 case DBUS_INVALID_MISSING_REPLY_SERIAL: return "Missing reply serial";

944 case DBUS_INVALID_LENGTH_OUT_OF_BOUNDS: return "Length out of bounds";

945 case DBUS_INVALID_ARRAY_LENGTH_EXCEEDS_MAXIMUM: return "Array length exceeds maximum";

946 case DBUS_INVALID_BAD_PATH: return "Bad path";

947 case DBUS_INVALID_SIGNATURE_LENGTH_OUT_OF_BOUNDS: return "Signature length out of bounds";

948 case DBUS_INVALID_BAD_UTF8_IN_STRING: return "Bad utf8 in string";

949 case DBUS_INVALID_ARRAY_LENGTH_INCORRECT: return "Array length incorrect";

950 case DBUS_INVALID_VARIANT_SIGNATURE_LENGTH_OUT_OF_BOUNDS: return "Variant signature length out of bounds";

951 case DBUS_INVALID_VARIANT_SIGNATURE_BAD: return "Variant signature bad";

952 case DBUS_INVALID_VARIANT_SIGNATURE_EMPTY: return "Variant signature empty";

953 case DBUS_INVALID_VARIANT_SIGNATURE_SPECIFIES_MULTIPLE_VALUES: return "Variant signature specifies multiple values";

954 case DBUS_INVALID_VARIANT_SIGNATURE_MISSING_NUL: return "Variant signature missing nul";

955 case DBUS_INVALID_STRING_MISSING_NUL: return "String missing nul";

956 case DBUS_INVALID_SIGNATURE_MISSING_NUL: return "Signature missing nul";

957 case DBUS_INVALID_EXCEEDED_MAXIMUM_DICT_ENTRY_RECURSION: return "Exceeded maximum dict entry recursion";

958 case DBUS_INVALID_DICT_ENTRY_ENDED_BUT_NOT_STARTED: return "Dict entry ended but not started";

959 case DBUS_INVALID_DICT_ENTRY_STARTED_BUT_NOT_ENDED: return "Dict entry started but not ended";

960 case DBUS_INVALID_DICT_ENTRY_HAS_NO_FIELDS: return "Dict entry has no fields";

961 case DBUS_INVALID_DICT_ENTRY_HAS_ONLY_ONE_FIELD: return "Dict entry has only one field";

962 case DBUS_INVALID_DICT_ENTRY_HAS_TOO_MANY_FIELDS: return "Dict entry has too many fields";

963 case DBUS_INVALID_DICT_ENTRY_NOT_INSIDE_ARRAY: return "Dict entry not inside array";

964 case DBUS_INVALID_DICT_KEY_MUST_BE_BASIC_TYPE: return "Dict key must be basic type";

965 case DBUS_INVALID_MISSING_UNIX_FDS: return "Unix file descriptor missing";

966 case DBUS_INVALID_NESTED_TOO_DEEPLY: return "Variants cannot be used to create a hugely recursive tree of values";

967 case DBUS_VALIDITY_LAST:

968 default:

969 return "Invalid";

970 }

971}

972

986dbus_bool_t

987\_dbus_validate_interface (const DBusString \*str,

988 int start,

989 int len)

990{

991 const unsigned char \*s;

992 const unsigned char \*end;

993 const unsigned char \*iface;

994 const unsigned char \*last_dot;

995

996 \_dbus_assert (start \>= 0);

997 \_dbus_assert (len \>= 0);

998 \_dbus_assert (start \<= \_dbus_string_get_length (str));

999

1000 if (len \> \_dbus_string_get_length (str) - start)

1001 return FALSE;

1002

1003 if (len \> DBUS_MAXIMUM_NAME_LENGTH)

1004 return FALSE;

1005

1006 if (len == 0)

1007 return FALSE;

1008

1009 last_dot = NULL;

1010 iface = \_dbus_string_get_const_udata (str) + start;

1011 end = iface + len;

1012 s = iface;

1013

1014 /\* check special cases of first char so it doesn't have to be done

1015 \* in the loop. Note we know len \> 0

1016 \*/

1017 if (\_DBUS_UNLIKELY (\*s == '.')) /\* disallow starting with a . \*/

1018 return FALSE;

1019 else if (\_DBUS_UNLIKELY (!VALID_INITIAL_NAME_CHARACTER (\*s)))

1020 return FALSE;

1021 else

1022 ++s;

1023

1024 while (s != end)

1025 {

1026 if (\*s == '.')

1027 {

1028 if (\_DBUS_UNLIKELY ((s + 1) == end))

1029 return FALSE;

1030 else if (\_DBUS_UNLIKELY (!VALID_INITIAL_NAME_CHARACTER (\*(s + 1))))

1031 return FALSE;

1032 last_dot = s;

1033 ++s; /\* we just validated the next char, so skip two \*/

1034 }

1035 else if (\_DBUS_UNLIKELY (!VALID_NAME_CHARACTER (\*s)))

1036 {

1037 return FALSE;

1038 }

1039

1040 ++s;

1041 }

1042

1043 if (\_DBUS_UNLIKELY (last_dot == NULL))

1044 return FALSE;

1045

1046 return TRUE;

1047}

1048

1062dbus_bool_t

1063\_dbus_validate_member (const DBusString \*str,

1064 int start,

1065 int len)

1066{

1067 const unsigned char \*s;

1068 const unsigned char \*end;

1069 const unsigned char \*member;

1070

1071 \_dbus_assert (start \>= 0);

1072 \_dbus_assert (len \>= 0);

1073 \_dbus_assert (start \<= \_dbus_string_get_length (str));

1074

1075 if (len \> \_dbus_string_get_length (str) - start)

1076 return FALSE;

1077

1078 if (len \> DBUS_MAXIMUM_NAME_LENGTH)

1079 return FALSE;

1080

1081 if (len == 0)

1082 return FALSE;

1083

1084 member = \_dbus_string_get_const_udata (str) + start;

1085 end = member + len;

1086 s = member;

1087

1088 /\* check special cases of first char so it doesn't have to be done

1089 \* in the loop. Note we know len \> 0

1090 \*/

1091

1092 if (\_DBUS_UNLIKELY (!VALID_INITIAL_NAME_CHARACTER (\*s)))

1093 return FALSE;

1094 else

1095 ++s;

1096

1097 while (s != end)

1098 {

1099 if (\_DBUS_UNLIKELY (!VALID_NAME_CHARACTER (\*s)))

1100 {

1101 return FALSE;

1102 }

1103

1104 ++s;

1105 }

1106

1107 return TRUE;

1108}

1109

1123dbus_bool_t

1124\_dbus_validate_error_name (const DBusString \*str,

1125 int start,

1126 int len)

1127{

1128 /\* Same restrictions as interface name at the moment \*/

1129 return \_dbus_validate_interface (str, start, len);

1130}

1131

1136\#define VALID_INITIAL_BUS_NAME_CHARACTER(c) \\

1137 ( ((c) \>= 'A' && (c) \<= 'Z') \|\| \\

1138 ((c) \>= 'a' && (c) \<= 'z') \|\| \\

1139 ((c) == '\_') \|\| ((c) == '-'))

1140

1145\#define VALID_BUS_NAME_CHARACTER(c) \\

1146 ( ((c) \>= '0' && (c) \<= '9') \|\| \\

1147 ((c) \>= 'A' && (c) \<= 'Z') \|\| \\

1148 ((c) \>= 'a' && (c) \<= 'z') \|\| \\

1149 ((c) == '\_') \|\| ((c) == '-'))

1150

1151static dbus_bool_t

1152\_dbus_validate_bus_name_full (const DBusString \*str,

1153 int start,

1154 int len,

1155 dbus_bool_t is_namespace)

1156{

1157 const unsigned char \*s;

1158 const unsigned char \*end;

1159 const unsigned char \*iface;

1160 const unsigned char \*last_dot;

1161

1162 \_dbus_assert (start \>= 0);

1163 \_dbus_assert (len \>= 0);

1164 \_dbus_assert (start \<= \_dbus_string_get_length (str));

1165

1166 if (len \> \_dbus_string_get_length (str) - start)

1167 return FALSE;

1168

1169 if (len \> DBUS_MAXIMUM_NAME_LENGTH)

1170 return FALSE;

1171

1172 if (len == 0)

1173 return FALSE;

1174

1175 last_dot = NULL;

1176 iface = \_dbus_string_get_const_udata (str) + start;

1177 end = iface + len;

1178 s = iface;

1179

1180 /\* check special cases of first char so it doesn't have to be done

1181 \* in the loop. Note we know len \> 0

1182 \*/

1183 if (\*s == ':')

1184 {

1185 /\* unique name \*/

1186 ++s;

1187 while (s != end)

1188 {

1189 if (\*s == '.')

1190 {

1191 if (\_DBUS_UNLIKELY ((s + 1) == end))

1192 return FALSE;

1193 if (\_DBUS_UNLIKELY (!VALID_BUS_NAME_CHARACTER (\*(s + 1))))

1194 return FALSE;

1195 ++s; /\* we just validated the next char, so skip two \*/

1196 }

1197 else if (\_DBUS_UNLIKELY (!VALID_BUS_NAME_CHARACTER (\*s)))

1198 {

1199 return FALSE;

1200 }

1201

1202 ++s;

1203 }

1204

1205 return TRUE;

1206 }

1207 else if (\_DBUS_UNLIKELY (\*s == '.')) /\* disallow starting with a . \*/

1208 return FALSE;

1209 else if (\_DBUS_UNLIKELY (!VALID_INITIAL_BUS_NAME_CHARACTER (\*s)))

1210 return FALSE;

1211 else

1212 ++s;

1213

1214 while (s != end)

1215 {

1216 if (\*s == '.')

1217 {

1218 if (\_DBUS_UNLIKELY ((s + 1) == end))

1219 return FALSE;

1220 else if (\_DBUS_UNLIKELY (!VALID_INITIAL_BUS_NAME_CHARACTER (\*(s + 1))))

1221 return FALSE;

1222 last_dot = s;

1223 ++s; /\* we just validated the next char, so skip two \*/

1224 }

1225 else if (\_DBUS_UNLIKELY (!VALID_BUS_NAME_CHARACTER (\*s)))

1226 {

1227 return FALSE;

1228 }

1229

1230 ++s;

1231 }

1232

1233 if (!is_namespace && \_DBUS_UNLIKELY (last_dot == NULL))

1234 return FALSE;

1235

1236 return TRUE;

1237}

1238

1252dbus_bool_t

1253\_dbus_validate_bus_name (const DBusString \*str,

1254 int start,

1255 int len)

1256{

1257 return \_dbus_validate_bus_name_full (str, start, len, FALSE);

1258}

1259

1273dbus_bool_t

1274\_dbus_validate_bus_namespace (const DBusString \*str,

1275 int start,

1276 int len)

1277{

1278 return \_dbus_validate_bus_name_full (str, start, len, TRUE);

1279}

1280

1282DEFINE_DBUS_NAME_CHECK(path)

1284DEFINE_DBUS_NAME_CHECK(interface)

1286DEFINE_DBUS_NAME_CHECK(member)

1288DEFINE_DBUS_NAME_CHECK(error_name)

1290DEFINE_DBUS_NAME_CHECK(bus_name)

1292DEFINE_DBUS_NAME_CHECK(utf8)

1293

1294

1296/\* tests in dbus-marshal-validate-util.c \*/

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

\_DBUS_N_ELEMENTS

\#define \_DBUS_N_ELEMENTS(array)

Computes the number of elements in a fixed-size array using sizeof().

**Definition** dbus-internals.h:189

\_DBUS_INT32_MAX

\#define \_DBUS_INT32_MAX

Maximum value of type "int32".

**Definition** dbus-internals.h:323

\_dbus_list_pop_last

void \* \_dbus_list_pop_last(DBusList \*\*list)

Removes the last value in the list and returns it.

**Definition** dbus-list.c:702

\_dbus_list_clear

void \_dbus_list_clear(DBusList \*\*list)

Frees all links in the list and sets the list head to NULL.

**Definition** dbus-list.c:545

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

\_dbus_type_reader_recurse

void \_dbus_type_reader_recurse(DBusTypeReader \*reader, DBusTypeReader \*sub)

Initialize a new reader pointing to the first type and corresponding value that's a child of the curr...

**Definition** dbus-marshal-recursive.c:987

DBusValidity

DBusValidity

This is primarily used in unit testing, so we can verify that each invalid message is invalid for the...

**Definition** dbus-marshal-validate.h:54

\_dbus_validate_signature_with_reason

DBusValidity \_dbus_validate_signature_with_reason(const DBusString \*type_str, int type_pos, int len)

Verifies that the range of type_str from type_pos to type_end is a valid signature.

**Definition** dbus-marshal-validate.c:53

VALID_NAME_CHARACTER

\#define VALID_NAME_CHARACTER(c)

Determine wether the given character is valid as a second or later character in a name.

**Definition** dbus-marshal-validate.c:826

VALID_INITIAL_BUS_NAME_CHARACTER

\#define VALID_INITIAL_BUS_NAME_CHARACTER(c)

Determine wether the given character is valid as the first character in a bus name.

**Definition** dbus-marshal-validate.c:1136

VALID_BUS_NAME_CHARACTER

\#define VALID_BUS_NAME_CHARACTER(c)

Determine wether the given character is valid as a second or later character in a bus name.

**Definition** dbus-marshal-validate.c:1145

\_dbus_type_get_alignment

int \_dbus_type_get_alignment(int typecode)

Gets the alignment requirement for the given type; will be 1, 2, 4, or 8.

**Definition** dbus-marshal-basic.c:1244

DEFINE_DBUS_NAME_CHECK

\#define DEFINE_DBUS_NAME_CHECK(what)

Define a name check to be used in \_dbus_return_if_fail() statements.

**Definition** dbus-marshal-validate.h:183

\_dbus_type_reader_init_types_only

void \_dbus_type_reader_init_types_only(DBusTypeReader \*reader, const DBusString \*type_str, int type_pos)

Like \_dbus_type_reader_init() but the iteration is over the signature, not over values.

**Definition** dbus-marshal-recursive.c:760

\_dbus_validate_error_name

dbus_bool_t \_dbus_validate_error_name(const DBusString \*str, int start, int len)

Checks that the given range of the string is a valid error name in the D-Bus protocol.

**Definition** dbus-marshal-validate.c:1124

\_dbus_unpack_uint32

dbus_uint32_t \_dbus_unpack_uint32(int byte_order, const unsigned char \*data)

Unpacks a 32 bit unsigned integer from a data pointer.

**Definition** dbus-marshal-basic.c:189

\_dbus_first_type_in_signature

int \_dbus_first_type_in_signature(const DBusString \*str, int pos)

Get the first type in the signature.

**Definition** dbus-marshal-basic.c:1484

\_dbus_type_reader_get_element_type

int \_dbus_type_reader_get_element_type(const DBusTypeReader \*reader)

Gets the type of an element of the array the reader is currently pointing to.

**Definition** dbus-marshal-recursive.c:820

\_dbus_validate_member

dbus_bool_t \_dbus_validate_member(const DBusString \*str, int start, int len)

Checks that the given range of the string is a valid member name in the D-Bus protocol.

**Definition** dbus-marshal-validate.c:1063

\_dbus_type_reader_next

dbus_bool_t \_dbus_type_reader_next(DBusTypeReader \*reader)

Skip to the next value on this "level".

**Definition** dbus-marshal-recursive.c:1053

\_dbus_validate_bus_namespace

dbus_bool_t \_dbus_validate_bus_namespace(const DBusString \*str, int start, int len)

Checks that the given range of the string is a prefix of a valid bus name in the D-Bus protocol.

**Definition** dbus-marshal-validate.c:1274

VALID_INITIAL_NAME_CHARACTER

\#define VALID_INITIAL_NAME_CHARACTER(c)

Determine wether the given character is valid as the first character in a name.

**Definition** dbus-marshal-validate.c:817

\_dbus_validate_path

dbus_bool_t \_dbus_validate_path(const DBusString \*str, int start, int len)

Checks that the given range of the string is a valid object path name in the D-Bus protocol.

**Definition** dbus-marshal-validate.c:849

\_dbus_validate_interface

dbus_bool_t \_dbus_validate_interface(const DBusString \*str, int start, int len)

Checks that the given range of the string is a valid interface name in the D-Bus protocol.

**Definition** dbus-marshal-validate.c:987

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

\_dbus_validate_bus_name

dbus_bool_t \_dbus_validate_bus_name(const DBusString \*str, int start, int len)

Checks that the given range of the string is a valid bus name in the D-Bus protocol.

**Definition** dbus-marshal-validate.c:1253

DBUS_VALIDITY_UNKNOWN_OOM_ERROR

@ DBUS_VALIDITY_UNKNOWN_OOM_ERROR

can't determine validity due to OOM

**Definition** dbus-marshal-validate.h:56

DBUS_INVALID_TOO_MUCH_DATA

@ DBUS_INVALID_TOO_MUCH_DATA

trailing junk makes it invalid

**Definition** dbus-marshal-validate.h:74

DBUS_VALID

@ DBUS_VALID

the data is valid

**Definition** dbus-marshal-validate.h:60

DBUS_TYPE_SIGNATURE

\#define DBUS_TYPE_SIGNATURE

Type code marking a D-Bus type signature.

**Definition** dbus-protocol.h:112

DBUS_MAXIMUM_SIGNATURE_LENGTH

\#define DBUS_MAXIMUM_SIGNATURE_LENGTH

This one is 255 so it fits in a byte.

**Definition** dbus-protocol.h:183

DBUS_DICT_ENTRY_END_CHAR

\#define DBUS_DICT_ENTRY_END_CHAR

Code marking the end of a dict entry type in a type signature.

**Definition** dbus-protocol.h:170

DBUS_TYPE_OBJECT_PATH

\#define DBUS_TYPE_OBJECT_PATH

Type code marking a D-Bus object path.

**Definition** dbus-protocol.h:108

DBUS_TYPE_BYTE

\#define DBUS_TYPE_BYTE

Type code marking an 8-bit unsigned integer.

**Definition** dbus-protocol.h:68

DBUS_TYPE_INT16

\#define DBUS_TYPE_INT16

Type code marking a 16-bit signed integer.

**Definition** dbus-protocol.h:76

DBUS_TYPE_VARIANT

\#define DBUS_TYPE_VARIANT

Type code marking a D-Bus variant type.

**Definition** dbus-protocol.h:126

DBUS_MAXIMUM_ARRAY_LENGTH

\#define DBUS_MAXIMUM_ARRAY_LENGTH

Max length of a marshaled array in bytes (64M, 2^26) We use signed int for lengths so must be INT_MAX...

**Definition** dbus-protocol.h:205

DBUS_TYPE_INT32

\#define DBUS_TYPE_INT32

Type code marking a 32-bit signed integer.

**Definition** dbus-protocol.h:84

DBUS_TYPE_UNIX_FD

\#define DBUS_TYPE_UNIX_FD

Type code marking a unix file descriptor.

**Definition** dbus-protocol.h:116

DBUS_TYPE_BOOLEAN

\#define DBUS_TYPE_BOOLEAN

Type code marking a boolean.

**Definition** dbus-protocol.h:72

DBUS_STRUCT_BEGIN_CHAR

\#define DBUS_STRUCT_BEGIN_CHAR

Code marking the start of a struct type in a type signature.

**Definition** dbus-protocol.h:158

DBUS_TYPE_STRING

\#define DBUS_TYPE_STRING

Type code marking a UTF-8 encoded, nul-terminated Unicode string.

**Definition** dbus-protocol.h:104

DBUS_MAXIMUM_NAME_LENGTH

\#define DBUS_MAXIMUM_NAME_LENGTH

Max length in bytes of a bus name, interface, or member (not object path, paths are unlimited).

**Definition** dbus-protocol.h:180

DBUS_TYPE_ARRAY

\#define DBUS_TYPE_ARRAY

Type code marking a D-Bus array type.

**Definition** dbus-protocol.h:122

DBUS_TYPE_INVALID

\#define DBUS_TYPE_INVALID

Type code that is never equal to a legitimate type code.

**Definition** dbus-protocol.h:62

DBUS_MAXIMUM_TYPE_RECURSION_DEPTH

\#define DBUS_MAXIMUM_TYPE_RECURSION_DEPTH

Depth of recursion in the type tree.

**Definition** dbus-protocol.h:229

DBUS_TYPE_INT64

\#define DBUS_TYPE_INT64

Type code marking a 64-bit signed integer.

**Definition** dbus-protocol.h:92

DBUS_TYPE_DOUBLE

\#define DBUS_TYPE_DOUBLE

Type code marking an 8-byte double in IEEE 754 format.

**Definition** dbus-protocol.h:100

DBUS_TYPE_UINT64

\#define DBUS_TYPE_UINT64

Type code marking a 64-bit unsigned integer.

**Definition** dbus-protocol.h:96

DBUS_TYPE_DICT_ENTRY

\#define DBUS_TYPE_DICT_ENTRY

Type code used to represent a dict entry; however, this type code does not appear in type signatures,...

**Definition** dbus-protocol.h:145

DBUS_DICT_ENTRY_BEGIN_CHAR

\#define DBUS_DICT_ENTRY_BEGIN_CHAR

Code marking the start of a dict entry type in a type signature.

**Definition** dbus-protocol.h:166

DBUS_TYPE_UINT16

\#define DBUS_TYPE_UINT16

Type code marking a 16-bit unsigned integer.

**Definition** dbus-protocol.h:80

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

dbus_type_is_valid

dbus_bool_t dbus_type_is_valid(int typecode)

Return TRUE if the argument is a valid typecode.

**Definition** dbus-signature.c:389

\_dbus_string_validate_utf8

dbus_bool_t \_dbus_string_validate_utf8(const DBusString \*str, int start, int len)

Checks that the given range of the string is valid UTF-8.

**Definition** dbus-string.c:2678

\_dbus_string_init_const_len

void \_dbus_string_init_const_len(DBusString \*str, const char \*value, int len)

Initializes a constant string with a length.

**Definition** dbus-string.c:217

\_dbus_string_get_length

int \_dbus_string_get_length(const DBusString \*str)

Gets the length of a string (not including nul termination).

**Definition** dbus-string.c:784

\_dbus_string_get_const_data_len

const char \* \_dbus_string_get_const_data_len(const DBusString \*str, int start, int len)

const version of \_dbus_string_get_data_len().

**Definition** dbus-string.c:559

DBusList

A node in a linked list.

**Definition** dbus-list.h:37

DBusString

**Definition** dbus-string.h:47

DBusTypeReader

The type reader is an iterator for reading values from a block of values.

**Definition** dbus-marshal-recursive.h:42

DBusTypeReader::type_pos

int type_pos

current position in signature

**Definition** dbus-marshal-recursive.h:53
