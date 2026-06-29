dbus-marshal-basic.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-marshal-basic.c Marshalling routines for basic (primitive) types

3 \*

4 \* Copyright (C) 2002 CodeFactory AB

5 \* Copyright (C) 2003, 2004, 2005 Red Hat, Inc.

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

29\#include "dbus-marshal-basic.h"

30\#include "dbus-signature.h"

31\#include \<dbus/dbus-test-tap.h\>

32

33\#include \<string.h\>

34

35\#define \_DBUS_ASSERT_ALIGNMENT(type, op, val) \\

36 \_DBUS_STATIC_ASSERT (\_DBUS_ALIGNOF (type) op val)

37\#define \_DBUS_ASSERT_CMP_ALIGNMENT(left, op, right) \\

38 \_DBUS_STATIC_ASSERT (\_DBUS_ALIGNOF (left) op \_DBUS_ALIGNOF (right))

39

40/\* True by definition, but just for completeness... \*/

41\_DBUS_STATIC_ASSERT (sizeof (char) == 1);

42\_DBUS_ASSERT_ALIGNMENT (char, ==, 1);

43

44\_DBUS_STATIC_ASSERT (sizeof (dbus_int16_t) == 2);

45\_DBUS_ASSERT_ALIGNMENT (dbus_int16_t, \<=, 2);

46\_DBUS_STATIC_ASSERT (sizeof (dbus_uint16_t) == 2);

47\_DBUS_ASSERT_ALIGNMENT (dbus_uint16_t, \<=, 2);

48\_DBUS_ASSERT_CMP_ALIGNMENT (dbus_uint16_t, ==, dbus_int16_t);

49

50\_DBUS_STATIC_ASSERT (sizeof (dbus_int32_t) == 4);

51\_DBUS_ASSERT_ALIGNMENT (dbus_int32_t, \<=, 4);

52\_DBUS_STATIC_ASSERT (sizeof (dbus_uint32_t) == 4);

53\_DBUS_ASSERT_ALIGNMENT (dbus_uint32_t, \<=, 4);

54\_DBUS_ASSERT_CMP_ALIGNMENT (dbus_uint32_t, ==, dbus_int32_t);

55\_DBUS_STATIC_ASSERT (sizeof (dbus_bool_t) == 4);

56\_DBUS_ASSERT_ALIGNMENT (dbus_bool_t, \<=, 4);

57\_DBUS_ASSERT_CMP_ALIGNMENT (dbus_uint32_t, ==, dbus_bool_t);

58

59\_DBUS_STATIC_ASSERT (sizeof (double) == 8);

60\_DBUS_ASSERT_ALIGNMENT (double, \<=, 8);

61/\* Doubles might sometimes be more strictly aligned than int64, but we

62 \* assume they are no less strictly aligned. This means every (double \*)

63 \* has enough alignment to be treated as though it was a

64 \* (dbus_uint64_t \*). \*/

65\_DBUS_ASSERT_CMP_ALIGNMENT (dbus_uint64_t, \<=, double);

66

67\_DBUS_STATIC_ASSERT (sizeof (dbus_int64_t) == 8);

68\_DBUS_ASSERT_ALIGNMENT (dbus_int64_t, \<=, 8);

69\_DBUS_STATIC_ASSERT (sizeof (dbus_uint64_t) == 8);

70\_DBUS_ASSERT_ALIGNMENT (dbus_uint64_t, \<=, 8);

71\_DBUS_ASSERT_CMP_ALIGNMENT (dbus_uint64_t, ==, dbus_int64_t);

72

73\_DBUS_STATIC_ASSERT (sizeof (DBusBasicValue) \>= 8);

74/\* The alignment of a DBusBasicValue might conceivably be \> 8 because of the

75 \* pointer, so we don't assert about it \*/

76

77\_DBUS_STATIC_ASSERT (sizeof (DBus8ByteStruct) == 8);

78\_DBUS_ASSERT_ALIGNMENT (DBus8ByteStruct, \<=, 8);

79

95static void

96pack_2_octets (dbus_uint16_t value,

97 int byte_order,

98 void \*data)

99{

100 \_dbus_assert (\_DBUS_ALIGN_ADDRESS (data, 2) == data);

101

102 if ((byte_order) == DBUS_LITTLE_ENDIAN)

103 \*((dbus_uint16_t\*)(data)) = DBUS_UINT16_TO_LE (value);

104 else

105 \*((dbus_uint16_t\*)(data)) = DBUS_UINT16_TO_BE (value);

106}

107

108static void

109pack_4_octets (dbus_uint32_t value,

110 int byte_order,

111 void \*data)

112{

113 \_dbus_assert (\_DBUS_ALIGN_ADDRESS (data, 4) == data);

114

115 if ((byte_order) == DBUS_LITTLE_ENDIAN)

116 \*((dbus_uint32_t\*)(data)) = DBUS_UINT32_TO_LE (value);

117 else

118 \*((dbus_uint32_t\*)(data)) = DBUS_UINT32_TO_BE (value);

119}

120

121static void

122pack_8_octets (dbus_uint64_t value,

123 int byte_order,

124 void \*data)

125{

126 \_dbus_assert (\_DBUS_ALIGN_ADDRESS (data, 8) == data);

127

128 if ((byte_order) == DBUS_LITTLE_ENDIAN)

129 \*((dbus_uint64_t\*)(data)) = DBUS_UINT64_TO_LE (value);

130 else

131 \*((dbus_uint64_t\*)(data)) = DBUS_UINT64_TO_BE (value);

132}

133

141void

142\_dbus_pack_uint32 (dbus_uint32_t value,

143 int byte_order,

144 unsigned char \*data)

145{

146 pack_4_octets (value, byte_order, data);

147}

148

149static void

150swap_8_octets (dbus_uint64_t \*value,

151 int byte_order)

152{

153 if (byte_order != DBUS_COMPILER_BYTE_ORDER)

154 {

155 \*value = DBUS_UINT64_SWAP_LE_BE (\*value);

156 }

157}

158

159\#ifndef \_dbus_unpack_uint16

167dbus_uint16_t

168\_dbus_unpack_uint16 (int byte_order,

169 const unsigned char \*data)

170{

171 \_dbus_assert (\_DBUS_ALIGN_ADDRESS (data, 2) == data);

172

173 if (byte_order == DBUS_LITTLE_ENDIAN)

174 return DBUS_UINT16_FROM_LE (\*(dbus_uint16_t \*) (void \*) data);

175 else

176 return DBUS_UINT16_FROM_BE (\*(dbus_uint16_t \*) (void \*) data);

177}

178\#endif /\* \_dbus_unpack_uint16 \*/

179

180\#ifndef \_dbus_unpack_uint32

188dbus_uint32_t

189\_dbus_unpack_uint32 (int byte_order,

190 const unsigned char \*data)

191{

192 \_dbus_assert (\_DBUS_ALIGN_ADDRESS (data, 4) == data);

193

194 if (byte_order == DBUS_LITTLE_ENDIAN)

195 return DBUS_UINT32_FROM_LE (\*(dbus_uint32_t \*) (void \*) data);

196 else

197 return DBUS_UINT32_FROM_BE (\*(dbus_uint32_t \*) (void \*) data);

198}

199\#endif /\* \_dbus_unpack_uint32 \*/

200

201static void

202set_2_octets (DBusString \*str,

203 int offset,

204 dbus_uint16_t value,

205 int byte_order)

206{

207 char \*data;

208

209 \_dbus_assert (byte_order == DBUS_LITTLE_ENDIAN \|\|

210 byte_order == DBUS_BIG_ENDIAN);

211

212 data = \_dbus_string_get_data_len (str, offset, 2);

213

214 pack_2_octets (value, byte_order, (unsigned char \*) data);

215}

216

217static void

218set_4_octets (DBusString \*str,

219 int offset,

220 dbus_uint32_t value,

221 int byte_order)

222{

223 char \*data;

224

225 \_dbus_assert (byte_order == DBUS_LITTLE_ENDIAN \|\|

226 byte_order == DBUS_BIG_ENDIAN);

227

228 data = \_dbus_string_get_data_len (str, offset, 4);

229

230 pack_4_octets (value, byte_order, (unsigned char \*) data);

231}

232

233static void

234set_8_octets (DBusString \*str,

235 int offset,

236 dbus_uint64_t value,

237 int byte_order)

238{

239 char \*data;

240

241 \_dbus_assert (byte_order == DBUS_LITTLE_ENDIAN \|\|

242 byte_order == DBUS_BIG_ENDIAN);

243

244 data = \_dbus_string_get_data_len (str, offset, 8);

245

246 pack_8_octets (value, byte_order, (unsigned char \*) data);

247}

248

259void

260\_dbus_marshal_set_uint32 (DBusString \*str,

261 int pos,

262 dbus_uint32_t value,

263 int byte_order)

264{

265 set_4_octets (str, pos, value, byte_order);

266}

267

287static dbus_bool_t

288set_string (DBusString \*str,

289 int pos,

290 const char \*value,

291 int byte_order,

292 int \*old_end_pos,

293 int \*new_end_pos)

294{

295 int old_len, new_len;

296 DBusString dstr;

297

298 \_dbus_string_init_const (&dstr, value);

299

300 \_dbus_assert (\_DBUS_ALIGN_VALUE (pos, 4) == (unsigned) pos);

301 old_len = \_dbus_unpack_uint32 (byte_order,

302 \_dbus_string_get_const_udata_len (str, pos, 4));

303

304 new_len = \_dbus_string_get_length (&dstr);

305

306 if (!\_dbus_string_replace_len (&dstr, 0, new_len,

307 str, pos + 4, old_len))

308 return FALSE;

309

310 \_dbus_marshal_set_uint32 (str, pos, new_len, byte_order);

311

312 if (old_end_pos)

313 \*old_end_pos = pos + 4 + old_len + 1;

314 if (new_end_pos)

315 \*new_end_pos = pos + 4 + new_len + 1;

316

317 return TRUE;

318}

319

333static dbus_bool_t

334set_signature (DBusString \*str,

335 int pos,

336 const char \*value,

337 int byte_order,

338 int \*old_end_pos,

339 int \*new_end_pos)

340{

341 int old_len, new_len;

342 DBusString dstr;

343

344 \_dbus_string_init_const (&dstr, value);

345

346 old_len = \_dbus_string_get_byte (str, pos);

347 new_len = \_dbus_string_get_length (&dstr);

348

349 if (!\_dbus_string_replace_len (&dstr, 0, new_len,

350 str, pos + 1, old_len))

351 return FALSE;

352

353 \_dbus_string_set_byte (str, pos, new_len);

354

355 if (old_end_pos)

356 \*old_end_pos = pos + 1 + old_len + 1;

357 if (new_end_pos)

358 \*new_end_pos = pos + 1 + new_len + 1;

359

360 return TRUE;

361}

362

376dbus_bool_t

377\_dbus_marshal_set_basic (DBusString \*str,

378 int pos,

379 int type,

380 const void \*value,

381 int byte_order,

382 int \*old_end_pos,

383 int \*new_end_pos)

384{

385 /\* Static assertions near the top of this file assert that signed and

386 \* unsigned 16- and 32-bit quantities have the same alignment, and that

387 \* doubles have alignment at least as strict as unsigned int64, so we

388 \* don't have to distinguish further: every (double \*)

389 \* has strong enough alignment to be treated as though it was a

390 \* (dbus_uint64_t \*). Going via a (void \*) means the compiler should

391 \* know that pointers can alias each other. \*/

392 const unsigned char \*u8_p;

393 const dbus_uint16_t \*u16_p;

394 const dbus_uint32_t \*u32_p;

395 const dbus_uint64_t \*u64_p;

396 const char \* const \*string_p;

397

398 switch (type)

399 {

400 case DBUS_TYPE_BYTE:

401 u8_p = value;

402 \_dbus_string_set_byte (str, pos, \*u8_p);

403 if (old_end_pos)

404 \*old_end_pos = pos + 1;

405 if (new_end_pos)

406 \*new_end_pos = pos + 1;

407 return TRUE;

408 break;

409 case DBUS_TYPE_INT16:

410 case DBUS_TYPE_UINT16:

411 u16_p = value;

412 pos = \_DBUS_ALIGN_VALUE (pos, 2);

413 set_2_octets (str, pos, \*u16_p, byte_order);

414 if (old_end_pos)

415 \*old_end_pos = pos + 2;

416 if (new_end_pos)

417 \*new_end_pos = pos + 2;

418 return TRUE;

419 break;

420 case DBUS_TYPE_BOOLEAN:

421 case DBUS_TYPE_INT32:

422 case DBUS_TYPE_UINT32:

423 case DBUS_TYPE_UNIX_FD:

424 u32_p = value;

425 pos = \_DBUS_ALIGN_VALUE (pos, 4);

426 set_4_octets (str, pos, \*u32_p, byte_order);

427 if (old_end_pos)

428 \*old_end_pos = pos + 4;

429 if (new_end_pos)

430 \*new_end_pos = pos + 4;

431 return TRUE;

432 break;

433 case DBUS_TYPE_INT64:

434 case DBUS_TYPE_UINT64:

435 case DBUS_TYPE_DOUBLE:

436 u64_p = value;

437 pos = \_DBUS_ALIGN_VALUE (pos, 8);

438 set_8_octets (str, pos, \*u64_p, byte_order);

439 if (old_end_pos)

440 \*old_end_pos = pos + 8;

441 if (new_end_pos)

442 \*new_end_pos = pos + 8;

443 return TRUE;

444 break;

445 case DBUS_TYPE_STRING:

446 case DBUS_TYPE_OBJECT_PATH:

447 string_p = value;

448 pos = \_DBUS_ALIGN_VALUE (pos, 4);

449 \_dbus_assert (\*string_p != NULL);

450 return set_string (str, pos, \*string_p, byte_order,

451 old_end_pos, new_end_pos);

452 break;

453 case DBUS_TYPE_SIGNATURE:

454 string_p = value;

455 \_dbus_assert (\*string_p != NULL);

456 return set_signature (str, pos, \*string_p, byte_order,

457 old_end_pos, new_end_pos);

458 break;

459 default:

460 \_dbus_assert_not_reached ("not a basic type");

461 return FALSE;

462 break;

463 }

464}

465

475dbus_uint32_t

476\_dbus_marshal_read_uint32 (const DBusString \*str,

477 int pos,

478 int byte_order,

479 int \*new_pos)

480{

481 pos = \_DBUS_ALIGN_VALUE (pos, 4);

482

483 if (new_pos)

484 \*new_pos = pos + 4;

485

486 \_dbus_assert (pos + 4 \<= \_dbus_string_get_length (str));

487

488 return \_dbus_unpack_uint32 (byte_order,

489 \_dbus_string_get_const_udata (str) + pos);

490}

491

513void

514\_dbus_marshal_read_basic (const DBusString \*str,

515 int pos,

516 int type,

517 void \*value,

518 int byte_order,

519 int \*new_pos)

520{

521 const char \*str_data;

522

523 \_dbus_assert (dbus_type_is_basic (type));

524

525 str_data = \_dbus_string_get_const_data (str);

526

527 /\* Below we volatile types to avoid aliasing issues;

528 \* see http://bugs.freedesktop.org/show_bug.cgi?id=20137

529 \*/

530

531 switch (type)

532 {

533 case DBUS_TYPE_BYTE:

534 {

535 volatile unsigned char \*vp = value;

536 \*vp = (unsigned char) \_dbus_string_get_byte (str, pos);

537 (pos)++;

538 }

539 break;

540 case DBUS_TYPE_INT16:

541 case DBUS_TYPE_UINT16:

542 {

543 volatile dbus_uint16_t \*vp = value;

544 pos = \_DBUS_ALIGN_VALUE (pos, 2);

545 \*vp = \*(dbus_uint16_t \*) (void \*) (str_data + pos);

546 if (byte_order != DBUS_COMPILER_BYTE_ORDER)

547 \*vp = DBUS_UINT16_SWAP_LE_BE (\*vp);

548 pos += 2;

549 }

550 break;

551 case DBUS_TYPE_INT32:

552 case DBUS_TYPE_UINT32:

553 case DBUS_TYPE_BOOLEAN:

554 case DBUS_TYPE_UNIX_FD:

555 {

556 volatile dbus_uint32_t \*vp = value;

557 pos = \_DBUS_ALIGN_VALUE (pos, 4);

558 \*vp = \*(dbus_uint32_t \*) (void \*) (str_data + pos);

559 if (byte_order != DBUS_COMPILER_BYTE_ORDER)

560 \*vp = DBUS_UINT32_SWAP_LE_BE (\*vp);

561 pos += 4;

562 }

563 break;

564 case DBUS_TYPE_INT64:

565 case DBUS_TYPE_UINT64:

566 case DBUS_TYPE_DOUBLE:

567 {

568 volatile dbus_uint64_t \*vp = value;

569 pos = \_DBUS_ALIGN_VALUE (pos, 8);

570 if (byte_order != DBUS_COMPILER_BYTE_ORDER)

571 \*vp = DBUS_UINT64_SWAP_LE_BE (

572 \*(dbus_uint64_t \*) (void \*) (str_data + pos));

573 else

574 \*vp = \*(dbus_uint64_t \*) (void \*) (str_data + pos);

575 pos += 8;

576 }

577 break;

578 case DBUS_TYPE_STRING:

579 case DBUS_TYPE_OBJECT_PATH:

580 {

581 int len;

582 volatile char \*\*vp = value;

583

584 len = \_dbus_marshal_read_uint32 (str, pos, byte_order, &pos);

585

586 \*vp = (char\*) str_data + pos;

587

588 pos += len + 1; /\* length plus nul \*/

589 }

590 break;

591 case DBUS_TYPE_SIGNATURE:

592 {

593 int len;

594 volatile char \*\*vp = value;

595

596 len = \_dbus_string_get_byte (str, pos);

597 pos += 1;

598

599 \*vp = (char\*) str_data + pos;

600

601 pos += len + 1; /\* length plus nul \*/

602 }

603 break;

604 default:

605 \_dbus_warn_check_failed ("type %s %d not a basic type",

606 \_dbus_type_to_string (type), type);

607 \_dbus_assert_not_reached ("not a basic type");

608 break;

609 }

610

611 if (new_pos)

612 \*new_pos = pos;

613}

614

615static dbus_bool_t

616marshal_2_octets (DBusString \*str,

617 int insert_at,

618 dbus_uint16_t value,

619 int byte_order,

620 int \*pos_after)

621{

622 dbus_bool_t retval;

623 int orig_len;

624

625 \_DBUS_STATIC_ASSERT (sizeof (value) == 2);

626

627 if (byte_order != DBUS_COMPILER_BYTE_ORDER)

628 value = DBUS_UINT16_SWAP_LE_BE (value);

629

630 orig_len = \_dbus_string_get_length (str);

631

632 retval = \_dbus_string_insert_2_aligned (str, insert_at,

633 (const unsigned char \*)&value);

634

635 if (pos_after)

636 {

637 \*pos_after = insert_at + (\_dbus_string_get_length (str) - orig_len);

638 \_dbus_assert (\*pos_after \<= \_dbus_string_get_length (str));

639 }

640

641 return retval;

642}

643

644static dbus_bool_t

645marshal_4_octets (DBusString \*str,

646 int insert_at,

647 dbus_uint32_t value,

648 int byte_order,

649 int \*pos_after)

650{

651 dbus_bool_t retval;

652 int orig_len;

653

654 \_DBUS_STATIC_ASSERT (sizeof (value) == 4);

655

656 if (byte_order != DBUS_COMPILER_BYTE_ORDER)

657 value = DBUS_UINT32_SWAP_LE_BE (value);

658

659 orig_len = \_dbus_string_get_length (str);

660

661 retval = \_dbus_string_insert_4_aligned (str, insert_at,

662 (const unsigned char \*)&value);

663

664 if (pos_after)

665 {

666 \*pos_after = insert_at + (\_dbus_string_get_length (str) - orig_len);

667 \_dbus_assert (\*pos_after \<= \_dbus_string_get_length (str));

668 }

669

670 return retval;

671}

672

673static dbus_bool_t

674marshal_8_octets (DBusString \*str,

675 int insert_at,

676 dbus_uint64_t value,

677 int byte_order,

678 int \*pos_after)

679{

680 dbus_bool_t retval;

681 int orig_len;

682

683 \_DBUS_STATIC_ASSERT (sizeof (value) == 8);

684

685 swap_8_octets (&value, byte_order);

686

687 orig_len = \_dbus_string_get_length (str);

688

689 retval = \_dbus_string_insert_8_aligned (str, insert_at,

690 (const unsigned char \*)&value);

691

692 if (pos_after)

693 \*pos_after = insert_at + \_dbus_string_get_length (str) - orig_len;

694

695 return retval;

696}

697

698enum

699 {

700 MARSHAL_AS_STRING,

701 MARSHAL_AS_SIGNATURE,

702 MARSHAL_AS_BYTE_ARRAY

703 };

704

705static dbus_bool_t

706marshal_len_followed_by_bytes (int marshal_as,

707 DBusString \*str,

708 int insert_at,

709 const unsigned char \*value,

710 int data_len, /\* doesn't include nul if any \*/

711 int byte_order,

712 int \*pos_after)

713{

714 int pos;

715 DBusString value_str;

716 int value_len;

717

718 \_dbus_assert (byte_order == DBUS_LITTLE_ENDIAN \|\| byte_order == DBUS_BIG_ENDIAN);

719 if (insert_at \> \_dbus_string_get_length (str))

720 \_dbus_warn ("insert_at = %d string len = %d data_len = %d",

721 insert_at, \_dbus_string_get_length (str), data_len);

722

723 if (marshal_as == MARSHAL_AS_BYTE_ARRAY)

724 value_len = data_len;

725 else

726 value_len = data_len + 1; /\* value has a nul \*/

727

728 \_dbus_string_init_const_len (&value_str, (const char \*) value, value_len);

729

730 pos = insert_at;

731

732 if (marshal_as == MARSHAL_AS_SIGNATURE)

733 {

734 \_dbus_assert (data_len \<= DBUS_MAXIMUM_SIGNATURE_LENGTH);

735 \_dbus_assert (data_len \<= 255); /\* same as max sig len right now \*/

736

737 if (!\_dbus_string_insert_byte (str, pos, data_len))

738 goto oom;

739

740 pos += 1;

741 }

742 else

743 {

744 if (!marshal_4_octets (str, pos, data_len,

745 byte_order, &pos))

746 goto oom;

747 }

748

749 if (!\_dbus_string_copy_len (&value_str, 0, value_len,

750 str, pos))

751 goto oom;

752

753\#if 0

754 /\* too expensive \*/

755 \_dbus_assert (\_dbus_string_equal_substring (&value_str, 0, value_len,

756 str, pos));

757 \_dbus_verbose_bytes_of_string (str, pos, value_len);

758\#endif

759

760 pos += value_len;

761

762 if (pos_after)

763 \*pos_after = pos;

764

765 return TRUE;

766

767 oom:

768 /\* Delete what we've inserted \*/

769 \_dbus_string_delete (str, insert_at, pos - insert_at);

770

771 return FALSE;

772}

773

774static dbus_bool_t

775marshal_string (DBusString \*str,

776 int insert_at,

777 const char \*value,

778 int byte_order,

779 int \*pos_after)

780{

781 return marshal_len_followed_by_bytes (MARSHAL_AS_STRING,

782 str, insert_at, (const unsigned char \*) value,

783 strlen (value),

784 byte_order, pos_after);

785}

786

787static dbus_bool_t

788marshal_signature (DBusString \*str,

789 int insert_at,

790 const char \*value,

791 int \*pos_after)

792{

793 return marshal_len_followed_by_bytes (MARSHAL_AS_SIGNATURE,

794 str, insert_at, (const unsigned char \*) value,

795 strlen (value),

796 DBUS_COMPILER_BYTE_ORDER, /\* irrelevant \*/

797 pos_after);

798}

799

816dbus_bool_t

817\_dbus_marshal_write_basic (DBusString \*str,

818 int insert_at,

819 int type,

820 const void \*value,

821 int byte_order,

822 int \*pos_after)

823{

824 /\* Static assertions near the top of this file assert that signed and

825 \* unsigned 16- and 32-bit quantities have the same alignment, and that

826 \* doubles have alignment at least as strict as unsigned int64, so we

827 \* don't have to distinguish further: every (double \*)

828 \* has strong enough alignment to be treated as though it was a

829 \* (dbus_uint64_t \*). Going via a (void \*) means the compiler should

830 \* know that pointers can alias each other. \*/

831 const unsigned char \*u8_p;

832 const dbus_uint16_t \*u16_p;

833 const dbus_uint32_t \*u32_p;

834 const dbus_uint64_t \*u64_p;

835 const char \* const \*string_p;

836

837 \_dbus_assert (dbus_type_is_basic (type));

838

839 switch (type)

840 {

841 case DBUS_TYPE_BYTE:

842 u8_p = value;

843 if (!\_dbus_string_insert_byte (str, insert_at, \*u8_p))

844 return FALSE;

845 if (pos_after)

846 \*pos_after = insert_at + 1;

847 return TRUE;

848 break;

849 case DBUS_TYPE_INT16:

850 case DBUS_TYPE_UINT16:

851 u16_p = value;

852 return marshal_2_octets (str, insert_at, \*u16_p,

853 byte_order, pos_after);

854 break;

855 case DBUS_TYPE_BOOLEAN:

856 u32_p = value;

857 return marshal_4_octets (str, insert_at, (\*u32_p != FALSE),

858 byte_order, pos_after);

859 break;

860 case DBUS_TYPE_INT32:

861 case DBUS_TYPE_UINT32:

862 case DBUS_TYPE_UNIX_FD:

863 u32_p = value;

864 return marshal_4_octets (str, insert_at, \*u32_p,

865 byte_order, pos_after);

866 break;

867 case DBUS_TYPE_INT64:

868 case DBUS_TYPE_UINT64:

869 case DBUS_TYPE_DOUBLE:

870 u64_p = value;

871 return marshal_8_octets (str, insert_at, \*u64_p, byte_order, pos_after);

872 break;

873

874 case DBUS_TYPE_STRING:

875 case DBUS_TYPE_OBJECT_PATH:

876 string_p = value;

877 \_dbus_assert (\*string_p != NULL);

878 return marshal_string (str, insert_at, \*string_p, byte_order, pos_after);

879 break;

880 case DBUS_TYPE_SIGNATURE:

881 string_p = value;

882 \_dbus_assert (\*string_p != NULL);

883 return marshal_signature (str, insert_at, \*string_p, pos_after);

884 break;

885 default:

886 \_dbus_assert_not_reached ("not a basic type");

887 return FALSE;

888 break;

889 }

890}

891

892static dbus_bool_t

893marshal_1_octets_array (DBusString \*str,

894 int insert_at,

895 const unsigned char \*value,

896 int n_elements,

897 int byte_order,

898 int \*pos_after)

899{

900 int pos;

901 DBusString value_str;

902

903 \_dbus_string_init_const_len (&value_str, (const char \*) value, n_elements);

904

905 pos = insert_at;

906

907 if (!\_dbus_string_copy_len (&value_str, 0, n_elements,

908 str, pos))

909 return FALSE;

910

911 pos += n_elements;

912

913 if (pos_after)

914 \*pos_after = pos;

915

916 return TRUE;

917}

918

926void

927\_dbus_swap_array (unsigned char \*data,

928 int n_elements,

929 int alignment)

930{

931 void \*d;

932 void \*end;

933

934 \_dbus_assert (\_DBUS_ALIGN_ADDRESS (data, alignment) == data);

935

936 /\* we use const_data and cast it off so DBusString can be a const string

937 \* for the unit tests. don't ask.

938 \*/

939 d = data;

940 end = data + (n_elements \* alignment);

941

942 if (alignment == 8)

943 {

944 while (d != end)

945 {

946 \*((dbus_uint64_t\*)d) = DBUS_UINT64_SWAP_LE_BE (\*((dbus_uint64_t\*)d));

947 d = ((unsigned char \*) d) + 8;

948 }

949 }

950 else if (alignment == 4)

951 {

952 while (d != end)

953 {

954 \*((dbus_uint32_t\*)d) = DBUS_UINT32_SWAP_LE_BE (\*((dbus_uint32_t\*)d));

955 d = ((unsigned char \*) d) + 4;

956 }

957 }

958 else

959 {

960 \_dbus_assert (alignment == 2);

961

962 while (d != end)

963 {

964 \*((dbus_uint16_t\*)d) = DBUS_UINT16_SWAP_LE_BE (\*((dbus_uint16_t\*)d));

965 d = ((unsigned char \*) d) + 2;

966 }

967 }

968}

969

970static void

971swap_array (DBusString \*str,

972 int array_start,

973 int n_elements,

974 int byte_order,

975 int alignment)

976{

977 \_dbus_assert (\_DBUS_ALIGN_VALUE (array_start, alignment) == (unsigned) array_start);

978

979 if (byte_order != DBUS_COMPILER_BYTE_ORDER)

980 {

981 /\* we use const_data and cast it off so DBusString can be a const string

982 \* for the unit tests. don't ask.

983 \*/

984 \_dbus_swap_array ((unsigned char\*) (\_dbus_string_get_const_data (str) + array_start),

985 n_elements, alignment);

986 }

987}

988

989static dbus_bool_t

990marshal_fixed_multi (DBusString \*str,

991 int insert_at,

992 const void \*value,

993 int n_elements,

994 int byte_order,

995 int alignment,

996 int \*pos_after)

997{

998 int old_string_len;

999 int array_start;

1000 DBusString t;

1001 int len_in_bytes;

1002

1003 \_dbus_assert (n_elements \<= DBUS_MAXIMUM_ARRAY_LENGTH / alignment);

1004

1005 old_string_len = \_dbus_string_get_length (str);

1006

1007 len_in_bytes = n_elements \* alignment;

1008 array_start = insert_at;

1009

1010 /\* Note that we do alignment padding unconditionally

1011 \* even if the array is empty; this means that

1012 \* padding + len is always equal to the number of bytes

1013 \* in the array.

1014 \*/

1015

1016 if (!\_dbus_string_insert_alignment (str, &array_start, alignment))

1017 goto error;

1018

1019 \_dbus_string_init_const_len (&t,

1020 (const char \*) value,

1021 len_in_bytes);

1022

1023 if (!\_dbus_string_copy (&t, 0,

1024 str, array_start))

1025 goto error;

1026

1027 swap_array (str, array_start, n_elements, byte_order, alignment);

1028

1029 if (pos_after)

1030 \*pos_after = array_start + len_in_bytes;

1031

1032 return TRUE;

1033

1034 error:

1035 \_dbus_string_delete (str, insert_at,

1036 \_dbus_string_get_length (str) - old_string_len);

1037

1038 return FALSE;

1039}

1040

1058dbus_bool_t

1059\_dbus_marshal_write_fixed_multi (DBusString \*str,

1060 int insert_at,

1061 int element_type,

1062 const void \*value,

1063 int n_elements,

1064 int byte_order,

1065 int \*pos_after)

1066{

1067 /\* Static assertions near the top of this file assert that signed and

1068 \* unsigned 16- and 32-bit quantities have the same alignment, and that

1069 \* doubles have alignment at least as strict as unsigned int64, so we

1070 \* don't have to distinguish further: every (double \*)

1071 \* has strong enough alignment to be treated as though it was a

1072 \* (dbus_uint64_t \*). Going via a (void \*) means the compiler should

1073 \* know that pointers can alias each other. \*/

1074 const unsigned char \* const \*u8_pp;

1075 const dbus_uint16_t \* const \*u16_pp;

1076 const dbus_uint32_t \* const \*u32_pp;

1077 const dbus_uint64_t \* const \*u64_pp;

1078

1079 \_dbus_assert (dbus_type_is_fixed (element_type));

1080 \_dbus_assert (n_elements \>= 0);

1081

1082\#if 0

1083 \_dbus_verbose ("writing %d elements of %s\n",

1084 n_elements, \_dbus_type_to_string (element_type));

1085\#endif

1086

1087 switch (element_type)

1088 {

1089 case DBUS_TYPE_BYTE:

1090 u8_pp = value;

1091 return marshal_1_octets_array (str, insert_at, \*u8_pp, n_elements, byte_order, pos_after);

1092 break;

1093 case DBUS_TYPE_INT16:

1094 case DBUS_TYPE_UINT16:

1095 u16_pp = value;

1096 return marshal_fixed_multi (str, insert_at, \*u16_pp, n_elements, byte_order, 2, pos_after);

1097 case DBUS_TYPE_BOOLEAN:

1098 case DBUS_TYPE_INT32:

1099 case DBUS_TYPE_UINT32:

1100 case DBUS_TYPE_UNIX_FD:

1101 u32_pp = value;

1102 return marshal_fixed_multi (str, insert_at, \*u32_pp, n_elements, byte_order, 4, pos_after);

1103 break;

1104 case DBUS_TYPE_INT64:

1105 case DBUS_TYPE_UINT64:

1106 case DBUS_TYPE_DOUBLE:

1107 u64_pp = value;

1108 return marshal_fixed_multi (str, insert_at, \*u64_pp, n_elements, byte_order, 8, pos_after);

1109 break;

1110

1111 default:

1112 \_dbus_assert_not_reached ("non fixed type in array write");

1113 break;

1114 }

1115

1116 return FALSE;

1117}

1118

1119

1129void

1130\_dbus_marshal_skip_basic (const DBusString \*str,

1131 int type,

1132 int byte_order,

1133 int \*pos)

1134{

1135 \_dbus_assert (byte_order == DBUS_LITTLE_ENDIAN \|\|

1136 byte_order == DBUS_BIG_ENDIAN);

1137

1138 switch (type)

1139 {

1140 case DBUS_TYPE_BYTE:

1141 (\*pos)++;

1142 break;

1143 case DBUS_TYPE_INT16:

1144 case DBUS_TYPE_UINT16:

1145 /\* Advance to the next suitably-aligned position \>= \*pos \*/

1146 \*pos = \_DBUS_ALIGN_VALUE (\*pos, 2);

1147 \*pos += 2;

1148 break;

1149 case DBUS_TYPE_BOOLEAN:

1150 case DBUS_TYPE_INT32:

1151 case DBUS_TYPE_UINT32:

1152 case DBUS_TYPE_UNIX_FD:

1153 \*pos = \_DBUS_ALIGN_VALUE (\*pos, 4);

1154 \*pos += 4;

1155 break;

1156 case DBUS_TYPE_INT64:

1157 case DBUS_TYPE_UINT64:

1158 case DBUS_TYPE_DOUBLE:

1159 \*pos = \_DBUS_ALIGN_VALUE (\*pos, 8);

1160 \*pos += 8;

1161 break;

1162 case DBUS_TYPE_STRING:

1163 case DBUS_TYPE_OBJECT_PATH:

1164 {

1165 int len;

1166

1167 /\* Let len be the number of bytes of string data, and advance

1168 \* \*pos to just after the length \*/

1169 len = \_dbus_marshal_read_uint32 (str, \*pos, byte_order, pos);

1170

1171 \*pos += len + 1; /\* length plus nul \*/

1172 }

1173 break;

1174 case DBUS_TYPE_SIGNATURE:

1175 {

1176 int len;

1177

1178 len = \_dbus_string_get_byte (str, \*pos);

1179

1180 \*pos += len + 2; /\* length byte plus length plus nul \*/

1181 }

1182 break;

1183 default:

1184 \_dbus_warn ("type %s not a basic type",

1185 \_dbus_type_to_string (type));

1186 \_dbus_assert_not_reached ("not a basic type");

1187 break;

1188 }

1189

1190 /\* We had better still be in-bounds at this point (pointing either into

1191 \* the content of the string, or 1 past the logical length of the string) \*/

1192 \_dbus_assert (\*pos \<= \_dbus_string_get_length (str));

1193}

1194

1204void

1205\_dbus_marshal_skip_array (const DBusString \*str,

1206 int element_type,

1207 int byte_order,

1208 int \*pos)

1209{

1210 dbus_uint32_t array_len;

1211 int i;

1212 int alignment;

1213

1214 /\* Advance to the next 4-byte-aligned position \>= \*pos \*/

1215 i = \_DBUS_ALIGN_VALUE (\*pos, 4);

1216

1217 /\* Let array_len be the number of bytes of array data, and advance

1218 \* i to just after the length \*/

1219 array_len = \_dbus_marshal_read_uint32 (str, i, byte_order, &i);

1220

1221 /\* If the element type is more strictly-aligned than the length,

1222 \* advance i to the next suitably-aligned position

1223 \* (in other words, skip the padding) \*/

1224 alignment = \_dbus_type_get_alignment (element_type);

1225

1226 i = \_DBUS_ALIGN_VALUE (i, alignment);

1227

1228 /\* Skip the actual array data \*/

1229 \*pos = i + array_len;

1230

1231 /\* We had better still be in-bounds at this point (pointing either into

1232 \* the content of the string, or 1 past the logical length of the string) \*/

1233 \_dbus_assert (\*pos \<= \_dbus_string_get_length (str));

1234}

1235

1243int

1244\_dbus_type_get_alignment (int typecode)

1245{

1246 switch (typecode)

1247 {

1248 case DBUS_TYPE_BYTE:

1249 case DBUS_TYPE_VARIANT:

1250 case DBUS_TYPE_SIGNATURE:

1251 return 1;

1252 case DBUS_TYPE_INT16:

1253 case DBUS_TYPE_UINT16:

1254 return 2;

1255 case DBUS_TYPE_BOOLEAN:

1256 case DBUS_TYPE_INT32:

1257 case DBUS_TYPE_UINT32:

1258 case DBUS_TYPE_UNIX_FD:

1259 /\* this stuff is 4 since it starts with a length \*/

1260 case DBUS_TYPE_STRING:

1261 case DBUS_TYPE_OBJECT_PATH:

1262 case DBUS_TYPE_ARRAY:

1263 return 4;

1264 case DBUS_TYPE_INT64:

1265 case DBUS_TYPE_UINT64:

1266 case DBUS_TYPE_DOUBLE:

1267 /\* struct is 8 since it could contain an 8-aligned item

1268 \* and it's simpler to just always align structs to 8;

1269 \* we want the amount of padding in a struct of a given

1270 \* type to be predictable, not location-dependent.

1271 \* DICT_ENTRY is always the same as struct.

1272 \*/

1273 case DBUS_TYPE_STRUCT:

1274 case DBUS_TYPE_DICT_ENTRY:

1275 return 8;

1276

1277 default:

1278 \_dbus_assert_not_reached ("unknown typecode in \_dbus_type_get_alignment()");

1279 return 0;

1280 }

1281}

1282

1289const char \*

1290\_dbus_type_to_string (int typecode)

1291{

1292 switch (typecode)

1293 {

1294 case DBUS_TYPE_INVALID:

1295 return "invalid";

1296 case DBUS_TYPE_BOOLEAN:

1297 return "boolean";

1298 case DBUS_TYPE_BYTE:

1299 return "byte";

1300 case DBUS_TYPE_INT16:

1301 return "int16";

1302 case DBUS_TYPE_UINT16:

1303 return "uint16";

1304 case DBUS_TYPE_INT32:

1305 return "int32";

1306 case DBUS_TYPE_UINT32:

1307 return "uint32";

1308 case DBUS_TYPE_INT64:

1309 return "int64";

1310 case DBUS_TYPE_UINT64:

1311 return "uint64";

1312 case DBUS_TYPE_DOUBLE:

1313 return "double";

1314 case DBUS_TYPE_STRING:

1315 return "string";

1316 case DBUS_TYPE_OBJECT_PATH:

1317 return "object_path";

1318 case DBUS_TYPE_SIGNATURE:

1319 return "signature";

1320 case DBUS_TYPE_STRUCT:

1321 return "struct";

1322 case DBUS_TYPE_DICT_ENTRY:

1323 return "dict_entry";

1324 case DBUS_TYPE_ARRAY:

1325 return "array";

1326 case DBUS_TYPE_VARIANT:

1327 return "variant";

1328 case DBUS_STRUCT_BEGIN_CHAR:

1329 return "begin_struct";

1330 case DBUS_STRUCT_END_CHAR:

1331 return "end_struct";

1332 case DBUS_DICT_ENTRY_BEGIN_CHAR:

1333 return "begin_dict_entry";

1334 case DBUS_DICT_ENTRY_END_CHAR:

1335 return "end_dict_entry";

1336 case DBUS_TYPE_UNIX_FD:

1337 return "unix_fd";

1338 default:

1339 return "unknown";

1340 }

1341}

1342

1350void

1351\_dbus_verbose_bytes (const unsigned char \*data,

1352 int len,

1353 int offset)

1354{

1355 int i;

1356 const unsigned char \*aligned;

1357

1358 \_dbus_assert (len \>= 0);

1359

1360 if (!\_dbus_is_verbose())

1361 return;

1362

1363 /\* Print blanks on first row if appropriate \*/

1364 aligned = \_DBUS_ALIGN_ADDRESS (data, 4);

1365 if (aligned \> data)

1366 aligned -= 4;

1367 \_dbus_assert (aligned \<= data);

1368

1369 if (aligned != data)

1370 {

1371 \_dbus_verbose ("%4ld\t%p: ", - (long)(data - aligned), aligned);

1372 while (aligned != data)

1373 {

1374 \_dbus_verbose (" ");

1375 ++aligned;

1376 }

1377 }

1378

1379 /\* now print the bytes \*/

1380 i = 0;

1381 while (i \< len)

1382 {

1383 if (\_DBUS_ALIGN_ADDRESS (&data\[i\], 4) == &data\[i\])

1384 {

1385 \_dbus_verbose ("%4d\t%p: ",

1386 offset + i, &data\[i\]);

1387 }

1388

1389 if (data\[i\] \>= 32 &&

1390 data\[i\] \<= 126)

1391 \_dbus_verbose (" '%c' ", data\[i\]);

1392 else

1393 \_dbus_verbose ("0x%s%x ",

1394 data\[i\] \<= 0xf ? "0" : "", data\[i\]);

1395

1396 ++i;

1397

1398 if (\_DBUS_ALIGN_ADDRESS (&data\[i\], 4) == &data\[i\])

1399 {

1400 if (i \> 3)

1401 \_dbus_verbose ("BE: %d LE: %d",

1402 \_dbus_unpack_uint32 (DBUS_BIG_ENDIAN, &data\[i-4\]),

1403 \_dbus_unpack_uint32 (DBUS_LITTLE_ENDIAN, &data\[i-4\]));

1404

1405 if (i \> 7 &&

1406 \_DBUS_ALIGN_ADDRESS (&data\[i\], 8) == &data\[i\])

1407 {

1408 \_dbus_verbose (" u64: 0x%" DBUS_INT64_MODIFIER "x",

1409 \*(dbus_uint64_t \*) (void \*) &data\[i - 8\]);

1410 \_dbus_verbose (" dbl: %g", \*(double \*) (void \*) &data\[i - 8\]);

1411 }

1412

1413 \_dbus_verbose ("\n");

1414 }

1415 }

1416

1417 \_dbus_verbose ("\n");

1418}

1419

1427void

1428\_dbus_verbose_bytes_of_string (const DBusString \*str,

1429 int start,

1430 int len)

1431{

1432 const char \*d;

1433 int real_len;

1434

1435 real_len = \_dbus_string_get_length (str);

1436

1437 \_dbus_assert (start \>= 0);

1438

1439 if (start \> real_len)

1440 {

1441 \_dbus_verbose (" \[%d,%d) is not inside string of length %d\n",

1442 start, len, real_len);

1443 return;

1444 }

1445

1446 if ((start + len) \> real_len)

1447 {

1448 \_dbus_verbose (" \[%d,%d) extends outside string of length %d\n",

1449 start, len, real_len);

1450 len = real_len - start;

1451 }

1452

1453 d = \_dbus_string_get_const_data_len (str, start, len);

1454

1455 \_dbus_verbose_bytes ((const unsigned char \*) d, len, start);

1456}

1457

1458static int

1459map_type_char_to_type (int t)

1460{

1461 if (t == DBUS_STRUCT_BEGIN_CHAR)

1462 return DBUS_TYPE_STRUCT;

1463 else if (t == DBUS_DICT_ENTRY_BEGIN_CHAR)

1464 return DBUS_TYPE_DICT_ENTRY;

1465 else

1466 {

1467 \_dbus_assert (t != DBUS_STRUCT_END_CHAR);

1468 \_dbus_assert (t != DBUS_DICT_ENTRY_END_CHAR);

1469 return t;

1470 }

1471}

1472

1483int

1484\_dbus_first_type_in_signature (const DBusString \*str,

1485 int pos)

1486{

1487 return map_type_char_to_type (\_dbus_string_get_byte (str, pos));

1488}

1489

1498int

1499\_dbus_first_type_in_signature_c_str (const char \*str,

1500 int pos)

1501{

1502 return map_type_char_to_type (str\[pos\]);

1503}

1504

1507\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

1508\#include "dbus-test.h"

1509\#include \<stdio.h\>

1510

1529void

1530\_dbus_marshal_read_fixed_multi (const DBusString \*str,

1531 int pos,

1532 int element_type,

1533 const void \*\*value,

1534 int n_elements,

1535 int byte_order,

1536 int \*new_pos)

1537{

1538 int array_len;

1539 int alignment;

1540

1541 \_dbus_assert (dbus_type_is_fixed (element_type));

1542 \_dbus_assert (dbus_type_is_basic (element_type));

1543

1544\#if 0

1545 \_dbus_verbose ("reading %d elements of %s\n",

1546 n_elements, \_dbus_type_to_string (element_type));

1547\#endif

1548

1549 alignment = \_dbus_type_get_alignment (element_type);

1550

1551 pos = \_DBUS_ALIGN_VALUE (pos, alignment);

1552

1553 array_len = n_elements \* alignment;

1554

1555 \*value = \_dbus_string_get_const_data_len (str, pos, array_len);

1556 if (new_pos)

1557 \*new_pos = pos + array_len;

1558}

1559

1560static void

1561swap_test_array (void \*array,

1562 int len_bytes,

1563 int byte_order,

1564 int alignment)

1565{

1566 DBusString t;

1567

1568 if (alignment == 1)

1569 return;

1570

1571 \_dbus_string_init_const_len (&t, array, len_bytes);

1572 swap_array (&t, 0, len_bytes / alignment, byte_order, alignment);

1573}

1574

1575\#define MARSHAL_BASIC(typename, byte_order, literal) \\

1576 do { \\

1577 v\_##typename = literal; \\

1578 if (!\_dbus_marshal_write_basic (&str, pos, DBUS_TYPE\_##typename, \\

1579 &v\_##typename, \\

1580 byte_order, NULL)) \\

1581 \_dbus_test_fatal ("no memory"); \\

1582 } while (0)

1583

1584\#define DEMARSHAL_BASIC(typename, byte_order) \\

1585 do { \\

1586 \_dbus_marshal_read_basic (&str, pos, DBUS_TYPE\_##typename, &v\_##typename, \\

1587 byte_order, &pos); \\

1588 } while (0)

1589

1590\#define DEMARSHAL_BASIC_AND_CHECK(typename, byte_order, literal) \\

1591 do { \\

1592 DEMARSHAL_BASIC (typename, byte_order); \\

1593 if (literal != v\_##typename) \\

1594 { \\

1595 \_dbus_verbose_bytes_of_string (&str, dump_pos, \\

1596 \_dbus_string_get_length (&str) - dump_pos); \\

1597 \_dbus_test_fatal ("demarshaled wrong value"); \\

1598 } \\

1599 } while (0)

1600

1601\#define MARSHAL_TEST(typename, byte_order, literal) \\

1602 do { \\

1603 MARSHAL_BASIC (typename, byte_order, literal); \\

1604 dump_pos = pos; \\

1605 DEMARSHAL_BASIC_AND_CHECK (typename, byte_order, literal); \\

1606 } while (0)

1607

1608\#define MARSHAL_TEST_STRCMP(typename, byte_order, literal) \\

1609 do { \\

1610 MARSHAL_BASIC (typename, byte_order, literal); \\

1611 dump_pos = pos; \\

1612 DEMARSHAL_BASIC (typename, byte_order); \\

1613 if (strcmp (literal, v\_##typename) != 0) \\

1614 { \\

1615 \_dbus_verbose_bytes_of_string (&str, dump_pos, \\

1616 \_dbus_string_get_length (&str) - dump_pos); \\

1617 \_dbus_warn ("literal '%s'\nvalue '%s'", literal, v\_##typename); \\

1618 \_dbus_test_fatal ("demarshaled wrong value"); \\

1619 } \\

1620 } while (0)

1621

1622\#define MARSHAL_FIXED_ARRAY(typename, byte_order, literal) \\

1623 do { \\

1624 int next; \\

1625 v_UINT32 = sizeof(literal); \\

1626 if (!\_dbus_marshal_write_basic (&str, pos, DBUS_TYPE_UINT32, &v_UINT32, \\

1627 byte_order, &next)) \\

1628 \_dbus_test_fatal ("no memory"); \\

1629 v_ARRAY\_##typename = literal; \\

1630 if (!\_dbus_marshal_write_fixed_multi (&str, next, DBUS_TYPE\_##typename, \\

1631 &v_ARRAY\_##typename, \_DBUS_N_ELEMENTS(literal), \\

1632 byte_order, NULL)) \\

1633 \_dbus_test_fatal ("no memory"); \\

1634 } while (0)

1635

1636\#define DEMARSHAL_FIXED_ARRAY(typename, byte_order) \\

1637 do { \\

1638 int next; \\

1639 alignment = \_dbus_type_get_alignment (DBUS_TYPE\_##typename); \\

1640 v_UINT32 = \_dbus_marshal_read_uint32 (&str, dump_pos, byte_order, &next); \\

1641 \_dbus_marshal_read_fixed_multi (&str, next, DBUS_TYPE\_##typename, \\

1642 (const void \*\*) &v_ARRAY\_##typename, \\

1643 v_UINT32/alignment, \\

1644 byte_order, NULL); \\

1645 swap_test_array (v_ARRAY\_##typename, v_UINT32, \\

1646 byte_order, alignment); \\

1647 } while (0)

1648

1649\#define DEMARSHAL_FIXED_ARRAY_AND_CHECK(typename, byte_order, literal) \\

1650 do { \\

1651 DEMARSHAL_FIXED_ARRAY (typename, byte_order); \\

1652 if (memcmp (literal, v_ARRAY\_##typename, sizeof (literal)) != 0) \\

1653 { \\

1654 \_dbus_verbose ("MARSHALED DATA\n"); \\

1655 \_dbus_verbose_bytes_of_string (&str, dump_pos, \\

1656 \_dbus_string_get_length (&str) - dump_pos); \\

1657 \_dbus_verbose ("LITERAL DATA\n"); \\

1658 \_dbus_verbose_bytes ((const unsigned char \*) literal, sizeof (literal), 0); \\

1659 \_dbus_verbose ("READ DATA\n"); \\

1660 \_dbus_verbose_bytes ((const unsigned char \*) v_ARRAY\_##typename, sizeof (literal), 0); \\

1661 \_dbus_test_fatal ("demarshaled wrong fixed array value"); \\

1662 } \\

1663 } while (0)

1664

1665\#define MARSHAL_TEST_FIXED_ARRAY(typename, byte_order, literal) \\

1666 do { \\

1667 MARSHAL_FIXED_ARRAY (typename, byte_order, literal); \\

1668 dump_pos = pos; \\

1669 DEMARSHAL_FIXED_ARRAY_AND_CHECK (typename, byte_order, literal); \\

1670 } while (0)

1671

1672dbus_bool_t

1673\_dbus_marshal_test (const char \*test_data_dir \_DBUS_GNUC_UNUSED)

1674{

1675 int alignment;

1676 DBusString str;

1677 int pos, dump_pos;

1678 unsigned char array1\[5\] = { 3, 4, 0, 1, 9 };

1679 dbus_int16_t array2\[3\] = { 124, 457, 780 };

1680 dbus_uint16_t array2u\[3\] = { 124, 457, 780 };

1681 dbus_int32_t array4\[3\] = { 123, 456, 789 };

1682 dbus_uint32_t array4u\[3\] = { 123, 456, 789 };

1683 dbus_int64_t array8\[3\] = { DBUS_INT64_CONSTANT (0x123ffffffff),

1684 DBUS_INT64_CONSTANT (0x456ffffffff),

1685 DBUS_INT64_CONSTANT (0x789ffffffff) };

1686 dbus_int64_t \*v_ARRAY_INT64;

1687 unsigned char \*v_ARRAY_BYTE;

1688 dbus_int16_t \*v_ARRAY_INT16;

1689 dbus_uint16_t \*v_ARRAY_UINT16;

1690 dbus_int32_t \*v_ARRAY_INT32;

1691 dbus_uint32_t \*v_ARRAY_UINT32;

1692 DBusString t;

1693 double v_DOUBLE;

1694 double t_DOUBLE;

1695 dbus_int16_t v_INT16;

1696 dbus_uint16_t v_UINT16;

1697 dbus_int32_t v_INT32;

1698 dbus_uint32_t v_UINT32;

1699 dbus_int64_t v_INT64;

1700 dbus_uint64_t v_UINT64;

1701 unsigned char v_BYTE;

1702 dbus_bool_t v_BOOLEAN;

1703 const char \*v_STRING;

1704 const char \*v_SIGNATURE;

1705 const char \*v_OBJECT_PATH;

1706 int byte_order;

1707

1708 if (!\_dbus_string_init (&str))

1709 \_dbus_test_fatal ("failed to init string");

1710

1711 pos = 0;

1712

1713 /\* Marshal doubles \*/

1714 MARSHAL_BASIC (DOUBLE, DBUS_BIG_ENDIAN, 3.14);

1715 DEMARSHAL_BASIC (DOUBLE, DBUS_BIG_ENDIAN);

1716 t_DOUBLE = 3.14;

1717 if (!\_DBUS_DOUBLES_BITWISE_EQUAL (t_DOUBLE, v_DOUBLE))

1718 \_dbus_test_fatal ("got wrong double value");

1719

1720 MARSHAL_BASIC (DOUBLE, DBUS_LITTLE_ENDIAN, 3.14);

1721 DEMARSHAL_BASIC (DOUBLE, DBUS_LITTLE_ENDIAN);

1722 t_DOUBLE = 3.14;

1723 if (!\_DBUS_DOUBLES_BITWISE_EQUAL (t_DOUBLE, v_DOUBLE))

1724 \_dbus_test_fatal ("got wrong double value");

1725

1726 /\* Marshal signed 16 integers \*/

1727 MARSHAL_TEST (INT16, DBUS_BIG_ENDIAN, -12345);

1728 MARSHAL_TEST (INT16, DBUS_LITTLE_ENDIAN, -12345);

1729

1730 /\* Marshal unsigned 16 integers \*/

1731 MARSHAL_TEST (UINT16, DBUS_BIG_ENDIAN, 0x1234);

1732 MARSHAL_TEST (UINT16, DBUS_LITTLE_ENDIAN, 0x1234);

1733

1734 /\* Marshal signed integers \*/

1735 MARSHAL_TEST (INT32, DBUS_BIG_ENDIAN, -12345678);

1736 MARSHAL_TEST (INT32, DBUS_LITTLE_ENDIAN, -12345678);

1737

1738 /\* Marshal unsigned integers \*/

1739 MARSHAL_TEST (UINT32, DBUS_BIG_ENDIAN, 0x12345678);

1740 MARSHAL_TEST (UINT32, DBUS_LITTLE_ENDIAN, 0x12345678);

1741

1742 /\* Marshal signed integers \*/

1743 MARSHAL_TEST (INT64, DBUS_BIG_ENDIAN, DBUS_INT64_CONSTANT (-0x123456789abc7));

1744 MARSHAL_TEST (INT64, DBUS_LITTLE_ENDIAN, DBUS_INT64_CONSTANT (-0x123456789abc7));

1745

1746 /\* Marshal unsigned integers \*/

1747 MARSHAL_TEST (UINT64, DBUS_BIG_ENDIAN, DBUS_UINT64_CONSTANT (0x123456789abc7));

1748 MARSHAL_TEST (UINT64, DBUS_LITTLE_ENDIAN, DBUS_UINT64_CONSTANT (0x123456789abc7));

1749

1750 /\* Marshal byte \*/

1751 MARSHAL_TEST (BYTE, DBUS_BIG_ENDIAN, 5);

1752 MARSHAL_TEST (BYTE, DBUS_LITTLE_ENDIAN, 5);

1753

1754 /\* Marshal all possible bools! \*/

1755 MARSHAL_TEST (BOOLEAN, DBUS_BIG_ENDIAN, FALSE);

1756 MARSHAL_TEST (BOOLEAN, DBUS_LITTLE_ENDIAN, FALSE);

1757 MARSHAL_TEST (BOOLEAN, DBUS_BIG_ENDIAN, TRUE);

1758 MARSHAL_TEST (BOOLEAN, DBUS_LITTLE_ENDIAN, TRUE);

1759

1760 /\* Marshal strings \*/

1761 MARSHAL_TEST_STRCMP (STRING, DBUS_BIG_ENDIAN, "");

1762 MARSHAL_TEST_STRCMP (STRING, DBUS_LITTLE_ENDIAN, "");

1763 MARSHAL_TEST_STRCMP (STRING, DBUS_BIG_ENDIAN, "This is the dbus test string");

1764 MARSHAL_TEST_STRCMP (STRING, DBUS_LITTLE_ENDIAN, "This is the dbus test string");

1765

1766 /\* object paths \*/

1767 MARSHAL_TEST_STRCMP (OBJECT_PATH, DBUS_BIG_ENDIAN, "/a/b/c");

1768 MARSHAL_TEST_STRCMP (OBJECT_PATH, DBUS_LITTLE_ENDIAN, "/a/b/c");

1769

1770 /\* signatures \*/

1771 MARSHAL_TEST_STRCMP (SIGNATURE, DBUS_BIG_ENDIAN, "");

1772 MARSHAL_TEST_STRCMP (SIGNATURE, DBUS_LITTLE_ENDIAN, "");

1773 MARSHAL_TEST_STRCMP (SIGNATURE, DBUS_BIG_ENDIAN, "a(ii)");

1774 MARSHAL_TEST_STRCMP (SIGNATURE, DBUS_LITTLE_ENDIAN, "a(ii)");

1775

1776 /\* Arrays \*/

1777 MARSHAL_TEST_FIXED_ARRAY (INT16, DBUS_BIG_ENDIAN, array2);

1778 MARSHAL_TEST_FIXED_ARRAY (INT16, DBUS_LITTLE_ENDIAN, array2);

1779 MARSHAL_TEST_FIXED_ARRAY (UINT16, DBUS_BIG_ENDIAN, array2u);

1780 MARSHAL_TEST_FIXED_ARRAY (UINT16, DBUS_LITTLE_ENDIAN, array2u);

1781

1782 MARSHAL_TEST_FIXED_ARRAY (INT32, DBUS_BIG_ENDIAN, array4);

1783 MARSHAL_TEST_FIXED_ARRAY (INT32, DBUS_LITTLE_ENDIAN, array4);

1784 MARSHAL_TEST_FIXED_ARRAY (UINT32, DBUS_BIG_ENDIAN, array4u);

1785 MARSHAL_TEST_FIXED_ARRAY (UINT32, DBUS_LITTLE_ENDIAN, array4u);

1786

1787 MARSHAL_TEST_FIXED_ARRAY (BYTE, DBUS_BIG_ENDIAN, array1);

1788 MARSHAL_TEST_FIXED_ARRAY (BYTE, DBUS_LITTLE_ENDIAN, array1);

1789

1790 MARSHAL_TEST_FIXED_ARRAY (INT64, DBUS_BIG_ENDIAN, array8);

1791 MARSHAL_TEST_FIXED_ARRAY (INT64, DBUS_LITTLE_ENDIAN, array8);

1792

1793\#if 0

1794

1795 /\*

1796 \* FIXME restore the set/pack tests

1797 \*/

1798

1799 /\* set/pack 64-bit integers \*/

1800 \_dbus_string_set_length (&str, 8);

1801

1802 /\* signed little \*/

1803 \_dbus_marshal_set_int64 (&str, DBUS_LITTLE_ENDIAN,

1804 0, DBUS_INT64_CONSTANT (-0x123456789abc7));

1805

1806 \_dbus_assert (DBUS_INT64_CONSTANT (-0x123456789abc7) ==

1807 \_dbus_unpack_int64 (DBUS_LITTLE_ENDIAN,

1808 \_dbus_string_get_const_data (&str)));

1809

1810 /\* signed big \*/

1811 \_dbus_marshal_set_int64 (&str, DBUS_BIG_ENDIAN,

1812 0, DBUS_INT64_CONSTANT (-0x123456789abc7));

1813

1814 \_dbus_assert (DBUS_INT64_CONSTANT (-0x123456789abc7) ==

1815 \_dbus_unpack_int64 (DBUS_BIG_ENDIAN,

1816 \_dbus_string_get_const_data (&str)));

1817

1818 /\* signed little pack \*/

1819 \_dbus_pack_int64 (DBUS_INT64_CONSTANT (-0x123456789abc7),

1820 DBUS_LITTLE_ENDIAN,

1821 \_dbus_string_get_data (&str));

1822

1823 \_dbus_assert (DBUS_INT64_CONSTANT (-0x123456789abc7) ==

1824 \_dbus_unpack_int64 (DBUS_LITTLE_ENDIAN,

1825 \_dbus_string_get_const_data (&str)));

1826

1827 /\* signed big pack \*/

1828 \_dbus_pack_int64 (DBUS_INT64_CONSTANT (-0x123456789abc7),

1829 DBUS_BIG_ENDIAN,

1830 \_dbus_string_get_data (&str));

1831

1832 \_dbus_assert (DBUS_INT64_CONSTANT (-0x123456789abc7) ==

1833 \_dbus_unpack_int64 (DBUS_BIG_ENDIAN,

1834 \_dbus_string_get_const_data (&str)));

1835

1836 /\* unsigned little \*/

1837 \_dbus_marshal_set_uint64 (&str, DBUS_LITTLE_ENDIAN,

1838 0, DBUS_UINT64_CONSTANT (0x123456789abc7));

1839

1840 \_dbus_assert (DBUS_UINT64_CONSTANT (0x123456789abc7) ==

1841 \_dbus_unpack_uint64 (DBUS_LITTLE_ENDIAN,

1842 \_dbus_string_get_const_data (&str)));

1843

1844 /\* unsigned big \*/

1845 \_dbus_marshal_set_uint64 (&str, DBUS_BIG_ENDIAN,

1846 0, DBUS_UINT64_CONSTANT (0x123456789abc7));

1847

1848 \_dbus_assert (DBUS_UINT64_CONSTANT (0x123456789abc7) ==

1849 \_dbus_unpack_uint64 (DBUS_BIG_ENDIAN,

1850 \_dbus_string_get_const_data (&str)));

1851

1852 /\* unsigned little pack \*/

1853 \_dbus_pack_uint64 (DBUS_UINT64_CONSTANT (0x123456789abc7),

1854 DBUS_LITTLE_ENDIAN,

1855 \_dbus_string_get_data (&str));

1856

1857 \_dbus_assert (DBUS_UINT64_CONSTANT (0x123456789abc7) ==

1858 \_dbus_unpack_uint64 (DBUS_LITTLE_ENDIAN,

1859 \_dbus_string_get_const_data (&str)));

1860

1861 /\* unsigned big pack \*/

1862 \_dbus_pack_uint64 (DBUS_UINT64_CONSTANT (0x123456789abc7),

1863 DBUS_BIG_ENDIAN,

1864 \_dbus_string_get_data (&str));

1865

1866 \_dbus_assert (DBUS_UINT64_CONSTANT (0x123456789abc7) ==

1867 \_dbus_unpack_uint64 (DBUS_BIG_ENDIAN,

1868 \_dbus_string_get_const_data (&str)));

1869

1870 /\* set/pack 32-bit integers \*/

1871 \_dbus_string_set_length (&str, 4);

1872

1873 /\* signed little \*/

1874 \_dbus_marshal_set_int32 (&str, DBUS_LITTLE_ENDIAN,

1875 0, -0x123456);

1876

1877 \_dbus_assert (-0x123456 ==

1878 \_dbus_unpack_int32 (DBUS_LITTLE_ENDIAN,

1879 \_dbus_string_get_const_data (&str)));

1880

1881 /\* signed big \*/

1882 \_dbus_marshal_set_int32 (&str, DBUS_BIG_ENDIAN,

1883 0, -0x123456);

1884

1885 \_dbus_assert (-0x123456 ==

1886 \_dbus_unpack_int32 (DBUS_BIG_ENDIAN,

1887 \_dbus_string_get_const_data (&str)));

1888

1889 /\* signed little pack \*/

1890 \_dbus_pack_int32 (-0x123456,

1891 DBUS_LITTLE_ENDIAN,

1892 \_dbus_string_get_data (&str));

1893

1894 \_dbus_assert (-0x123456 ==

1895 \_dbus_unpack_int32 (DBUS_LITTLE_ENDIAN,

1896 \_dbus_string_get_const_data (&str)));

1897

1898 /\* signed big pack \*/

1899 \_dbus_pack_int32 (-0x123456,

1900 DBUS_BIG_ENDIAN,

1901 \_dbus_string_get_data (&str));

1902

1903 \_dbus_assert (-0x123456 ==

1904 \_dbus_unpack_int32 (DBUS_BIG_ENDIAN,

1905 \_dbus_string_get_const_data (&str)));

1906

1907 /\* unsigned little \*/

1908 \_dbus_marshal_set_uint32 (&str,

1909 0, 0x123456,

1910 DBUS_LITTLE_ENDIAN);

1911

1912 \_dbus_assert (0x123456 ==

1913 \_dbus_unpack_uint32 (DBUS_LITTLE_ENDIAN,

1914 \_dbus_string_get_const_data (&str)));

1915

1916 /\* unsigned big \*/

1917 \_dbus_marshal_set_uint32 (&str,

1918 0, 0x123456,

1919 DBUS_BIG_ENDIAN);

1920

1921 \_dbus_assert (0x123456 ==

1922 \_dbus_unpack_uint32 (DBUS_BIG_ENDIAN,

1923 \_dbus_string_get_const_data (&str)));

1924

1925 /\* unsigned little pack \*/

1926 \_dbus_pack_uint32 (0x123456,

1927 DBUS_LITTLE_ENDIAN,

1928 \_dbus_string_get_data (&str));

1929

1930 \_dbus_assert (0x123456 ==

1931 \_dbus_unpack_uint32 (DBUS_LITTLE_ENDIAN,

1932 \_dbus_string_get_const_data (&str)));

1933

1934 /\* unsigned big pack \*/

1935 \_dbus_pack_uint32 (0x123456,

1936 DBUS_BIG_ENDIAN,

1937 \_dbus_string_get_data (&str));

1938

1939 \_dbus_assert (0x123456 ==

1940 \_dbus_unpack_uint32 (DBUS_BIG_ENDIAN,

1941 \_dbus_string_get_const_data (&str)));

1942

1943\#endif /\* set/pack tests for integers \*/

1944

1945 /\* Strings in-place set \*/

1946 byte_order = DBUS_LITTLE_ENDIAN;

1947 while (TRUE)

1948 {

1949 /\* Init a string \*/

1950 \_dbus_string_set_length (&str, 0);

1951

1952 /\* reset pos for the macros \*/

1953 pos = 0;

1954

1955 MARSHAL_TEST_STRCMP (STRING, byte_order, "Hello world");

1956

1957 /\* Set it to something longer \*/

1958 \_dbus_string_init_const (&t, "Hello world foo");

1959

1960 v_STRING = \_dbus_string_get_const_data (&t);

1961 \_dbus_marshal_set_basic (&str, 0, DBUS_TYPE_STRING,

1962 &v_STRING, byte_order, NULL, NULL);

1963

1964 \_dbus_marshal_read_basic (&str, 0, DBUS_TYPE_STRING,

1965 &v_STRING, byte_order,

1966 NULL);

1967 \_dbus_assert (strcmp (v_STRING, "Hello world foo") == 0);

1968

1969 /\* Set it to something shorter \*/

1970 \_dbus_string_init_const (&t, "Hello");

1971

1972 v_STRING = \_dbus_string_get_const_data (&t);

1973 \_dbus_marshal_set_basic (&str, 0, DBUS_TYPE_STRING,

1974 &v_STRING, byte_order, NULL, NULL);

1975 \_dbus_marshal_read_basic (&str, 0, DBUS_TYPE_STRING,

1976 &v_STRING, byte_order,

1977 NULL);

1978 \_dbus_assert (strcmp (v_STRING, "Hello") == 0);

1979

1980 /\* Do the other byte order \*/

1981 if (byte_order == DBUS_LITTLE_ENDIAN)

1982 byte_order = DBUS_BIG_ENDIAN;

1983 else

1984 break;

1985 }

1986

1987 /\* Clean up \*/

1988 \_dbus_string_free (&str);

1989

1990 return TRUE;

1991}

1992

1993\#endif /\* DBUS_ENABLE_EMBEDDED_TESTS \*/

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

\_dbus_unpack_uint16

dbus_uint16_t \_dbus_unpack_uint16(int byte_order, const unsigned char \*data)

Unpacks a 16 bit unsigned integer from a data pointer.

**Definition** dbus-marshal-basic.c:168

\_dbus_type_get_alignment

int \_dbus_type_get_alignment(int typecode)

Gets the alignment requirement for the given type; will be 1, 2, 4, or 8.

**Definition** dbus-marshal-basic.c:1244

\_dbus_verbose_bytes_of_string

void \_dbus_verbose_bytes_of_string(const DBusString \*str, int start, int len)

Dump the given part of the string to verbose log.

**Definition** dbus-marshal-basic.c:1428

\_dbus_pack_uint32

void \_dbus_pack_uint32(dbus_uint32_t value, int byte_order, unsigned char \*data)

Packs a 32 bit unsigned integer into a data pointer.

**Definition** dbus-marshal-basic.c:142

\_dbus_marshal_set_uint32

void \_dbus_marshal_set_uint32(DBusString \*str, int pos, dbus_uint32_t value, int byte_order)

Sets the 4 bytes at the given offset to a marshaled unsigned integer, replacing anything found there ...

**Definition** dbus-marshal-basic.c:260

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

\_dbus_first_type_in_signature_c_str

int \_dbus_first_type_in_signature_c_str(const char \*str, int pos)

Similar to \_dbus_first_type_in_signature, but operates on a C string buffer.

**Definition** dbus-marshal-basic.c:1499

\_dbus_marshal_read_uint32

dbus_uint32_t \_dbus_marshal_read_uint32(const DBusString \*str, int pos, int byte_order, int \*new_pos)

Convenience function to demarshal a 32 bit unsigned integer.

**Definition** dbus-marshal-basic.c:476

\_dbus_verbose_bytes

void \_dbus_verbose_bytes(const unsigned char \*data, int len, int offset)

If in verbose mode, print a block of binary data.

**Definition** dbus-marshal-basic.c:1351

\_dbus_marshal_set_basic

dbus_bool_t \_dbus_marshal_set_basic(DBusString \*str, int pos, int type, const void \*value, int byte_order, int \*old_end_pos, int \*new_end_pos)

Sets an existing basic type value to a new value.

**Definition** dbus-marshal-basic.c:377

\_dbus_marshal_skip_array

void \_dbus_marshal_skip_array(const DBusString \*str, int element_type, int byte_order, int \*pos)

Skips an array, returning the next position.

**Definition** dbus-marshal-basic.c:1205

\_dbus_marshal_write_fixed_multi

dbus_bool_t \_dbus_marshal_write_fixed_multi(DBusString \*str, int insert_at, int element_type, const void \*value, int n_elements, int byte_order, int \*pos_after)

Marshals a block of values of fixed-length type all at once, as an optimization.

**Definition** dbus-marshal-basic.c:1059

\_dbus_type_to_string

const char \* \_dbus_type_to_string(int typecode)

Returns a string describing the given type.

**Definition** dbus-marshal-basic.c:1290

\_dbus_marshal_read_basic

void \_dbus_marshal_read_basic(const DBusString \*str, int pos, int type, void \*value, int byte_order, int \*new_pos)

Demarshals a basic-typed value.

**Definition** dbus-marshal-basic.c:514

\_dbus_swap_array

void \_dbus_swap_array(unsigned char \*data, int n_elements, int alignment)

Swaps the elements of an array to the opposite byte order.

**Definition** dbus-marshal-basic.c:927

\_dbus_marshal_skip_basic

void \_dbus_marshal_skip_basic(const DBusString \*str, int type, int byte_order, int \*pos)

Skips over a basic-typed value, reporting the following position.

**Definition** dbus-marshal-basic.c:1130

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

DBUS_TYPE_ARRAY

\#define DBUS_TYPE_ARRAY

Type code marking a D-Bus array type.

**Definition** dbus-protocol.h:122

DBUS_TYPE_INVALID

\#define DBUS_TYPE_INVALID

Type code that is never equal to a legitimate type code.

**Definition** dbus-protocol.h:62

DBUS_LITTLE_ENDIAN

\#define DBUS_LITTLE_ENDIAN

Code marking LSB-first byte order in the wire protocol.

**Definition** dbus-protocol.h:55

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

DBUS_BIG_ENDIAN

\#define DBUS_BIG_ENDIAN

Code marking MSB-first byte order in the wire protocol.

**Definition** dbus-protocol.h:56

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

\_dbus_string_set_length

dbus_bool_t \_dbus_string_set_length(DBusString \*str, int length)

Sets the length of a string.

**Definition** dbus-string.c:847

\_dbus_string_insert_8_aligned

dbus_bool_t \_dbus_string_insert_8_aligned(DBusString \*str, int insert_at, const unsigned char octets\[8\])

Inserts 8 bytes aligned on an 8 byte boundary with any alignment padding initialized to 0.

**Definition** dbus-string.c:1053

\_dbus_string_equal_substring

dbus_bool_t \_dbus_string_equal_substring(const DBusString \*a, int a_start, int a_len, const DBusString \*b, int b_start)

Tests two sub-parts of two DBusString for equality.

**Definition** dbus-string.c:2166

\_dbus_string_insert_alignment

dbus_bool_t \_dbus_string_insert_alignment(DBusString \*str, int \*insert_at, int alignment)

Inserts padding at \*insert_at such to align it to the given boundary.

**Definition** dbus-string.c:1081

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

\_dbus_string_get_data_len

char \* \_dbus_string_get_data_len(DBusString \*str, int start, int len)

Gets a sub-portion of the raw character buffer from the string.

**Definition** dbus-string.c:535

\_dbus_string_init_const_len

void \_dbus_string_init_const_len(DBusString \*str, const char \*value, int len)

Initializes a constant string with a length.

**Definition** dbus-string.c:217

\_dbus_string_get_data

char \* \_dbus_string_get_data(DBusString \*str)

Gets the raw character buffer from the string.

**Definition** dbus-string.c:496

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_string_delete

void \_dbus_string_delete(DBusString \*str, int start, int len)

Deletes a segment of a DBusString with length len starting at start.

**Definition** dbus-string.c:1255

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

\_dbus_string_set_byte

void \_dbus_string_set_byte(DBusString \*str, int i, unsigned char byte)

Sets the value of the byte at the given position.

**Definition** dbus-string.c:583

\_dbus_string_get_const_data

const char \* \_dbus_string_get_const_data(const DBusString \*str)

Gets the raw character buffer from a const string.

**Definition** dbus-string.c:513

\_dbus_string_get_byte

unsigned char \_dbus_string_get_byte(const DBusString \*str, int start)

Gets the byte at the given position.

**Definition** dbus-string.c:607

\_dbus_string_insert_4_aligned

dbus_bool_t \_dbus_string_insert_4_aligned(DBusString \*str, int insert_at, const unsigned char octets\[4\])

Inserts 4 bytes aligned on a 4 byte boundary with any alignment padding initialized to 0.

**Definition** dbus-string.c:1029

\_dbus_string_insert_2_aligned

dbus_bool_t \_dbus_string_insert_2_aligned(DBusString \*str, int insert_at, const unsigned char octets\[2\])

Inserts 2 bytes aligned on a 2 byte boundary with any alignment padding initialized to 0.

**Definition** dbus-string.c:1005

\_dbus_string_copy_len

dbus_bool_t \_dbus_string_copy_len(const DBusString \*source, int start, int len, DBusString \*dest, int insert_at)

Like \_dbus_string_copy(), but can copy a segment from the middle of the source string.

**Definition** dbus-string.c:1437

\_dbus_string_replace_len

dbus_bool_t \_dbus_string_replace_len(const DBusString \*source, int start, int len, DBusString \*dest, int replace_at, int replace_len)

Replaces a segment of dest string with a segment of source string.

**Definition** dbus-string.c:1466

\_DBUS_DOUBLES_BITWISE_EQUAL

\#define \_DBUS_DOUBLES_BITWISE_EQUAL(a, b)

On x86 there is an 80-bit FPU, and if you do "a == b" it may have a or b in an 80-bit register,...

**Definition** dbus-sysdeps.h:654

DBUS_UINT64_CONSTANT

\#define DBUS_UINT64_CONSTANT(val)

Declare a 64-bit unsigned integer constant.

**Definition** dbus-arch-deps.h:42

DBUS_INT64_MODIFIER

\#define DBUS_INT64_MODIFIER

A string literal for a length modifier that is appropriate to print the dbus_int64_t and dbus_uint64\_...

**Definition** dbus-arch-deps.h:39

DBUS_INT64_CONSTANT

\#define DBUS_INT64_CONSTANT(val)

Declare a 64-bit signed integer constant.

**Definition** dbus-arch-deps.h:41

DBus8ByteStruct

An 8-byte struct you could use to access int64 without having int64 support.

**Definition** dbus-types.h:145

DBusString

**Definition** dbus-string.h:47

DBusBasicValue

A simple value union that lets you access bytes as if they were various types; useful when dealing wi...

**Definition** dbus-types.h:161
