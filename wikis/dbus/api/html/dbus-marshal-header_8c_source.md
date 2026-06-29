dbus-marshal-header.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-marshal-header.c Managing marshaling/demarshaling of message headers

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

27\#include "dbus/dbus-shared.h"

28\#include "dbus-marshal-header.h"

29\#include "dbus-marshal-recursive.h"

30\#include "dbus-marshal-byteswap.h"

31

39/\* Not thread locked, but strictly const/read-only so should be OK

40 \*/

42\_DBUS_STRING_DEFINE_STATIC(\_dbus_header_signature_str, DBUS_HEADER_SIGNATURE);

44\_DBUS_STRING_DEFINE_STATIC(\_dbus_local_interface_str, DBUS_INTERFACE_LOCAL);

46\_DBUS_STRING_DEFINE_STATIC(\_dbus_local_path_str, DBUS_PATH_LOCAL);

47

49\#define FIELDS_ARRAY_SIGNATURE_OFFSET 6

51\#define FIELDS_ARRAY_ELEMENT_SIGNATURE_OFFSET 7

52

53

55\#define BYTE_ORDER_OFFSET 0

57\#define TYPE_OFFSET 1

59\#define FLAGS_OFFSET 2

61\#define VERSION_OFFSET 3

63\#define BODY_LENGTH_OFFSET 4

65\#define SERIAL_OFFSET 8

67\#define FIELDS_ARRAY_LENGTH_OFFSET 12

69\#define FIRST_FIELD_OFFSET 16

70

71typedef struct

72{

73 unsigned char code;

74 unsigned char type;

75} HeaderFieldType;

76

77static const HeaderFieldType

78\_dbus_header_field_types\[DBUS_HEADER_FIELD_LAST+1\] = {

79 { DBUS_HEADER_FIELD_INVALID, DBUS_TYPE_INVALID },

80 { DBUS_HEADER_FIELD_PATH, DBUS_TYPE_OBJECT_PATH },

81 { DBUS_HEADER_FIELD_INTERFACE, DBUS_TYPE_STRING },

82 { DBUS_HEADER_FIELD_MEMBER, DBUS_TYPE_STRING },

83 { DBUS_HEADER_FIELD_ERROR_NAME, DBUS_TYPE_STRING },

84 { DBUS_HEADER_FIELD_REPLY_SERIAL, DBUS_TYPE_UINT32 },

85 { DBUS_HEADER_FIELD_DESTINATION, DBUS_TYPE_STRING },

86 { DBUS_HEADER_FIELD_SENDER, DBUS_TYPE_STRING },

87 { DBUS_HEADER_FIELD_SIGNATURE, DBUS_TYPE_SIGNATURE },

88 { DBUS_HEADER_FIELD_UNIX_FDS, DBUS_TYPE_UINT32 },

89 { DBUS_HEADER_FIELD_CONTAINER_INSTANCE, DBUS_TYPE_OBJECT_PATH }

90};

91

93\#define EXPECTED_TYPE_OF_FIELD(field) (\_dbus_header_field_types\[field\].type)

94

96\#define MAX_POSSIBLE_HEADER_PADDING 7

97static dbus_bool_t

98reserve_header_padding (DBusHeader \*header)

99{

100 \_dbus_assert (header-\>padding \<= MAX_POSSIBLE_HEADER_PADDING);

101

102 if (!\_dbus_string_lengthen (&header-\>data,

103 MAX_POSSIBLE_HEADER_PADDING - header-\>padding))

104 return FALSE;

105 header-\>padding = MAX_POSSIBLE_HEADER_PADDING;

106 return TRUE;

107}

108

109static void

110correct_header_padding (DBusHeader \*header)

111{

112 int unpadded_len;

113

114 \_dbus_assert (header-\>padding == 7);

115

116 \_dbus_string_shorten (&header-\>data, header-\>padding);

117 unpadded_len = \_dbus_string_get_length (&header-\>data);

118

119 if (!\_dbus_string_align_length (&header-\>data, 8))

120 \_dbus_assert_not_reached ("couldn't pad header though enough padding was preallocated");

121

122 header-\>padding = \_dbus_string_get_length (&header-\>data) - unpadded_len;

123}

124

128\#define HEADER_END_BEFORE_PADDING(header) \\

129 (\_dbus_string_get_length (&(header)-\>data) - (header)-\>padding)

130

138static void

139\_dbus_header_cache_invalidate_all (DBusHeader \*header)

140{

141 int i;

142

143 i = 0;

144 while (i \<= DBUS_HEADER_FIELD_LAST)

145 {

146 header-\>fields\[i\].value_pos = \_DBUS_HEADER_FIELD_VALUE_UNKNOWN;

147 ++i;

148 }

149}

150

158static void

159\_dbus_header_cache_one (DBusHeader \*header,

160 int field_code,

161 DBusTypeReader \*variant_reader)

162{

163 header-\>fields\[field_code\].value_pos =

164 \_dbus_type_reader_get_value_pos (variant_reader);

165

166\#if 0

167 \_dbus_verbose ("cached value_pos %d for field %d\n",

168 header-\>fields\[field_code\].value_pos, field_code)

169\#endif

170}

171

178char

179\_dbus_header_get_byte_order (const DBusHeader \*header)

180{

181 \_dbus_assert (\_dbus_string_get_length (&header-\>data) \> BYTE_ORDER_OFFSET);

182

183 return (char) \_dbus_string_get_byte (&header-\>data, BYTE_ORDER_OFFSET);

184}

185

191static void

192\_dbus_header_cache_revalidate (DBusHeader \*header)

193{

194 DBusTypeReader array;

195 DBusTypeReader reader;

196 int i;

197

198 i = 0;

199 while (i \<= DBUS_HEADER_FIELD_LAST)

200 {

201 header-\>fields\[i\].value_pos = \_DBUS_HEADER_FIELD_VALUE_NONEXISTENT;

202 ++i;

203 }

204

205 \_dbus_type_reader_init (&reader,

206 \_dbus_header_get_byte_order (header),

207 &\_dbus_header_signature_str,

208 FIELDS_ARRAY_SIGNATURE_OFFSET,

209 &header-\>data,

210 FIELDS_ARRAY_LENGTH_OFFSET);

211

212 \_dbus_type_reader_recurse (&reader, &array);

213

214 while (\_dbus_type_reader_get_current_type (&array) != DBUS_TYPE_INVALID)

215 {

216 DBusTypeReader sub;

217 DBusTypeReader variant;

218 unsigned char field_code;

219

220 \_dbus_type_reader_recurse (&array, &sub);

221

222 \_dbus_assert (\_dbus_type_reader_get_current_type (&sub) == DBUS_TYPE_BYTE);

223 \_dbus_type_reader_read_basic (&sub, &field_code);

224

225 /\* Unknown fields should be ignored \*/

226 if (field_code \> DBUS_HEADER_FIELD_LAST)

227 goto next_field;

228

229 \_dbus_type_reader_next (&sub);

230

231 \_dbus_assert (\_dbus_type_reader_get_current_type (&sub) == DBUS_TYPE_VARIANT);

232 \_dbus_type_reader_recurse (&sub, &variant);

233

234 \_dbus_header_cache_one (header, field_code, &variant);

235

236 next_field:

237 \_dbus_type_reader_next (&array);

238 }

239}

240

248static dbus_bool_t

249\_dbus_header_cache_check (DBusHeader \*header,

250 int field)

251{

252 \_dbus_assert (field \<= DBUS_HEADER_FIELD_LAST);

253

254 if (header-\>fields\[field\].value_pos == \_DBUS_HEADER_FIELD_VALUE_UNKNOWN)

255 \_dbus_header_cache_revalidate (header);

256

257 if (header-\>fields\[field\].value_pos == \_DBUS_HEADER_FIELD_VALUE_NONEXISTENT)

258 return FALSE;

259

260 return TRUE;

261}

262

271static dbus_bool_t

272\_dbus_header_cache_known_nonexistent (DBusHeader \*header,

273 int field)

274{

275 \_dbus_assert (field \<= DBUS_HEADER_FIELD_LAST);

276

277 return (header-\>fields\[field\].value_pos == \_DBUS_HEADER_FIELD_VALUE_NONEXISTENT);

278}

279

289static dbus_bool_t

290write_basic_field (DBusTypeWriter \*writer,

291 int field,

292 int type,

293 const void \*value)

294{

295 DBusTypeWriter sub;

296 DBusTypeWriter variant;

297 int start;

298 int padding;

299 unsigned char field_byte;

300 DBusString contained_type;

301 char buf\[2\];

302

303 start = writer-\>value_pos;

304 padding = \_dbus_string_get_length (writer-\>value_str) - start;

305

306 if (!\_dbus_type_writer_recurse (writer, DBUS_TYPE_STRUCT,

307 NULL, 0, &sub))

308 goto append_failed;

309

310 field_byte = field;

311 if (!\_dbus_type_writer_write_basic (&sub, DBUS_TYPE_BYTE,

312 &field_byte))

313 goto append_failed;

314

315 buf\[0\] = type;

316 buf\[1\] = '\0';

317 \_dbus_string_init_const_len (&contained_type, buf, 1);

318

319 if (!\_dbus_type_writer_recurse (&sub, DBUS_TYPE_VARIANT,

320 &contained_type, 0, &variant))

321 goto append_failed;

322

323 if (!\_dbus_type_writer_write_basic (&variant, type, value))

324 goto append_failed;

325

326 if (!\_dbus_type_writer_unrecurse (&sub, &variant))

327 goto append_failed;

328

329 if (!\_dbus_type_writer_unrecurse (writer, &sub))

330 goto append_failed;

331

332 return TRUE;

333

334 append_failed:

335 \_dbus_string_delete (writer-\>value_str,

336 start,

337 \_dbus_string_get_length (writer-\>value_str) - start - padding);

338 return FALSE;

339}

340

351static dbus_bool_t

352set_basic_field (DBusTypeReader \*reader,

353 int field,

354 int type,

355 const void \*value,

356 const DBusTypeReader \*realign_root)

357{

358 DBusTypeReader sub;

359 DBusTypeReader variant;

360

361 \_dbus_type_reader_recurse (reader, &sub);

362

363 \_dbus_assert (\_dbus_type_reader_get_current_type (&sub) == DBUS_TYPE_BYTE);

364\#ifndef DBUS_DISABLE_ASSERT

365 {

366 unsigned char v_BYTE;

367 \_dbus_type_reader_read_basic (&sub, &v_BYTE);

368 \_dbus_assert (((int) v_BYTE) == field);

369 }

370\#endif

371

372 if (!\_dbus_type_reader_next (&sub))

373 \_dbus_assert_not_reached ("no variant field?");

374

375 \_dbus_type_reader_recurse (&sub, &variant);

376 \_dbus_assert (\_dbus_type_reader_get_current_type (&variant) == type);

377

378 if (!\_dbus_type_reader_set_basic (&variant, value, realign_root))

379 return FALSE;

380

381 return TRUE;

382}

383

390int

391\_dbus_header_get_message_type (DBusHeader \*header)

392{

393 int type;

394

395 type = \_dbus_string_get_byte (&header-\>data, TYPE_OFFSET);

396 \_dbus_assert (type != DBUS_MESSAGE_TYPE_INVALID);

397

398 return type;

399}

400

408void

409\_dbus_header_set_serial (DBusHeader \*header,

410 dbus_uint32_t serial)

411{

412 /\* we use this function to set the serial on outgoing

413 \* messages, and to reset the serial in dbus_message_copy;

414 \* this assertion should catch a double-set on outgoing.

415 \*/

416 \_dbus_assert (\_dbus_header_get_serial (header) == 0 \|\|

417 serial == 0);

418

419 \_dbus_marshal_set_uint32 (&header-\>data,

420 SERIAL_OFFSET,

421 serial,

422 \_dbus_header_get_byte_order (header));

423}

424

431dbus_uint32_t

432\_dbus_header_get_serial (DBusHeader \*header)

433{

434 return \_dbus_marshal_read_uint32 (&header-\>data,

435 SERIAL_OFFSET,

436 \_dbus_header_get_byte_order (header),

437 NULL);

438}

439

447void

448\_dbus_header_reinit (DBusHeader \*header)

449{

450 \_dbus_string_set_length (&header-\>data, 0);

451

452 header-\>padding = 0;

453

454 \_dbus_header_cache_invalidate_all (header);

455}

456

464dbus_bool_t

465\_dbus_header_init (DBusHeader \*header)

466{

467 if (!\_dbus_string_init_preallocated (&header-\>data, 32))

468 return FALSE;

469

470 \_dbus_header_reinit (header);

471

472 return TRUE;

473}

474

480void

481\_dbus_header_free (DBusHeader \*header)

482{

483 \_dbus_string_free (&header-\>data);

484}

485

494dbus_bool_t

495\_dbus_header_copy (const DBusHeader \*header,

496 DBusHeader \*dest)

497{

498 \*dest = \*header;

499

500 if (!\_dbus_string_init_preallocated (&dest-\>data,

501 \_dbus_string_get_length (&header-\>data)))

502 return FALSE;

503

504 if (!\_dbus_string_copy (&header-\>data, 0, &dest-\>data, 0))

505 {

506 \_dbus_string_free (&dest-\>data);

507 return FALSE;

508 }

509

510 /\* Reset the serial \*/

511 \_dbus_header_set_serial (dest, 0);

512

513 return TRUE;

514}

515

532dbus_bool_t

533\_dbus_header_create (DBusHeader \*header,

534 int byte_order,

535 int message_type,

536 const char \*destination,

537 const char \*path,

538 const char \*interface,

539 const char \*member,

540 const char \*error_name)

541{

542 unsigned char v_BYTE;

543 dbus_uint32_t v_UINT32;

544 DBusTypeWriter writer;

545 DBusTypeWriter array;

546

547 \_dbus_assert (byte_order == DBUS_LITTLE_ENDIAN \|\|

548 byte_order == DBUS_BIG_ENDIAN);

549 \_dbus_assert (((interface \|\| message_type != DBUS_MESSAGE_TYPE_SIGNAL) && member) \|\|

550 (error_name) \|\|

551 !(interface \|\| member \|\| error_name));

552 \_dbus_assert (\_dbus_string_get_length (&header-\>data) == 0);

553

554 if (!reserve_header_padding (header))

555 return FALSE;

556

557 \_dbus_type_writer_init_values_only (&writer, byte_order,

558 &\_dbus_header_signature_str, 0,

559 &header-\>data,

560 HEADER_END_BEFORE_PADDING (header));

561

562 v_BYTE = byte_order;

563 if (!\_dbus_type_writer_write_basic (&writer, DBUS_TYPE_BYTE,

564 &v_BYTE))

565 goto oom;

566

567 v_BYTE = message_type;

568 if (!\_dbus_type_writer_write_basic (&writer, DBUS_TYPE_BYTE,

569 &v_BYTE))

570 goto oom;

571

572 v_BYTE = 0; /\* flags \*/

573 if (!\_dbus_type_writer_write_basic (&writer, DBUS_TYPE_BYTE,

574 &v_BYTE))

575 goto oom;

576

577 v_BYTE = DBUS_MAJOR_PROTOCOL_VERSION;

578 if (!\_dbus_type_writer_write_basic (&writer, DBUS_TYPE_BYTE,

579 &v_BYTE))

580 goto oom;

581

582 v_UINT32 = 0; /\* body length \*/

583 if (!\_dbus_type_writer_write_basic (&writer, DBUS_TYPE_UINT32,

584 &v_UINT32))

585 goto oom;

586

587 v_UINT32 = 0; /\* serial \*/

588 if (!\_dbus_type_writer_write_basic (&writer, DBUS_TYPE_UINT32,

589 &v_UINT32))

590 goto oom;

591

592 if (!\_dbus_type_writer_recurse (&writer, DBUS_TYPE_ARRAY,

593 &\_dbus_header_signature_str,

594 FIELDS_ARRAY_SIGNATURE_OFFSET,

595 &array))

596 goto oom;

597

598 /\* Marshal all the fields (Marshall Fields?) \*/

599

600 if (path != NULL)

601 {

602 if (!write_basic_field (&array,

603 DBUS_HEADER_FIELD_PATH,

604 DBUS_TYPE_OBJECT_PATH,

605 &path))

606 goto oom;

607 }

608

609 if (destination != NULL)

610 {

611 if (!write_basic_field (&array,

612 DBUS_HEADER_FIELD_DESTINATION,

613 DBUS_TYPE_STRING,

614 &destination))

615 goto oom;

616 }

617

618 /\* Note that test/message.c relies on this being in the middle of the

619 \* message: if you change the order of serialization here (but why

620 \* would you?), please find some other way to retain test coverage. \*/

621 if (interface != NULL)

622 {

623 if (!write_basic_field (&array,

624 DBUS_HEADER_FIELD_INTERFACE,

625 DBUS_TYPE_STRING,

626 &interface))

627 goto oom;

628 }

629

630 if (member != NULL)

631 {

632 if (!write_basic_field (&array,

633 DBUS_HEADER_FIELD_MEMBER,

634 DBUS_TYPE_STRING,

635 &member))

636 goto oom;

637 }

638

639 if (error_name != NULL)

640 {

641 if (!write_basic_field (&array,

642 DBUS_HEADER_FIELD_ERROR_NAME,

643 DBUS_TYPE_STRING,

644 &error_name))

645 goto oom;

646 }

647

648 if (!\_dbus_type_writer_unrecurse (&writer, &array))

649 goto oom;

650

651 correct_header_padding (header);

652

653 return TRUE;

654

655 oom:

656 \_dbus_string_delete (&header-\>data, 0,

657 \_dbus_string_get_length (&header-\>data) - header-\>padding);

658 correct_header_padding (header);

659

660 return FALSE;

661}

662

680dbus_bool_t

681\_dbus_header_have_message_untrusted (int max_message_length,

682 DBusValidity \*validity,

683 int \*byte_order,

684 int \*fields_array_len,

685 int \*header_len,

686 int \*body_len,

687 const DBusString \*str,

688 int start,

689 int len)

690

691{

692 dbus_uint32_t header_len_unsigned;

693 dbus_uint32_t fields_array_len_unsigned;

694 dbus_uint32_t body_len_unsigned;

695

696 \_dbus_assert (start \>= 0);

697 \_dbus_assert (start \< \_DBUS_INT32_MAX / 2);

698 \_dbus_assert (len \>= 0);

699

700 \_dbus_assert (start == (int) \_DBUS_ALIGN_VALUE (start, 8));

701

702 \*byte_order = \_dbus_string_get_byte (str, start + BYTE_ORDER_OFFSET);

703

704 if (\*byte_order != DBUS_LITTLE_ENDIAN && \*byte_order != DBUS_BIG_ENDIAN)

705 {

706 \*validity = DBUS_INVALID_BAD_BYTE_ORDER;

707 return FALSE;

708 }

709

710 \_dbus_assert (FIELDS_ARRAY_LENGTH_OFFSET + 4 \<= len);

711 fields_array_len_unsigned = \_dbus_marshal_read_uint32 (str, start + FIELDS_ARRAY_LENGTH_OFFSET,

712 \*byte_order, NULL);

713

714 if (fields_array_len_unsigned \> (unsigned) max_message_length)

715 {

716 \*validity = DBUS_INVALID_INSANE_FIELDS_ARRAY_LENGTH;

717 return FALSE;

718 }

719

720 \_dbus_assert (BODY_LENGTH_OFFSET + 4 \< len);

721 body_len_unsigned = \_dbus_marshal_read_uint32 (str, start + BODY_LENGTH_OFFSET,

722 \*byte_order, NULL);

723

724 if (body_len_unsigned \> (unsigned) max_message_length)

725 {

726 \*validity = DBUS_INVALID_INSANE_BODY_LENGTH;

727 return FALSE;

728 }

729

730 header_len_unsigned = FIRST_FIELD_OFFSET + fields_array_len_unsigned;

731 header_len_unsigned = \_DBUS_ALIGN_VALUE (header_len_unsigned, 8);

732

733 /\* overflow should be impossible since the lengths aren't allowed to

734 \* be huge.

735 \*/

736 \_dbus_assert (max_message_length \< \_DBUS_INT32_MAX / 2);

737 if (body_len_unsigned + header_len_unsigned \> (unsigned) max_message_length)

738 {

739 \*validity = DBUS_INVALID_MESSAGE_TOO_LONG;

740 return FALSE;

741 }

742

743 \_dbus_assert (body_len_unsigned \< (unsigned) \_DBUS_INT32_MAX);

744 \_dbus_assert (fields_array_len_unsigned \< (unsigned) \_DBUS_INT32_MAX);

745 \_dbus_assert (header_len_unsigned \< (unsigned) \_DBUS_INT32_MAX);

746

747 \*body_len = body_len_unsigned;

748 \*fields_array_len = fields_array_len_unsigned;

749 \*header_len = header_len_unsigned;

750

751 \*validity = DBUS_VALID;

752

753 \_dbus_verbose ("have %d bytes, need body %u + header %u = %u\n",

754 len, body_len_unsigned, header_len_unsigned,

755 body_len_unsigned + header_len_unsigned);

756

757 return (body_len_unsigned + header_len_unsigned) \<= (unsigned) len;

758}

759

760static DBusValidity

761check_mandatory_fields (DBusHeader \*header)

762{

763\#define REQUIRE_FIELD(name) do { if (header-\>fields\[DBUS_HEADER_FIELD\_##name\].value_pos \< 0) return DBUS_INVALID_MISSING\_##name; } while (0)

764

765 switch (\_dbus_header_get_message_type (header))

766 {

767 case DBUS_MESSAGE_TYPE_SIGNAL:

768 REQUIRE_FIELD (INTERFACE);

769 /\* FALL THRU - signals also require the path and member \*/

770 case DBUS_MESSAGE_TYPE_METHOD_CALL:

771 REQUIRE_FIELD (PATH);

772 REQUIRE_FIELD (MEMBER);

773 break;

774 case DBUS_MESSAGE_TYPE_ERROR:

775 REQUIRE_FIELD (ERROR_NAME);

776 REQUIRE_FIELD (REPLY_SERIAL);

777 break;

778 case DBUS_MESSAGE_TYPE_METHOD_RETURN:

779 REQUIRE_FIELD (REPLY_SERIAL);

780 break;

781 default:

782 /\* other message types allowed but ignored \*/

783 break;

784 }

785

786 return DBUS_VALID;

787}

788

789static DBusValidity

790load_and_validate_field (DBusHeader \*header,

791 int field,

792 DBusTypeReader \*variant_reader)

793{

794 int type;

795 int expected_type;

796 const DBusString \*value_str;

797 int value_pos;

798 int str_data_pos;

799 dbus_uint32_t v_UINT32;

800 int bad_string_code;

801 dbus_bool_t (\* string_validation_func) (const DBusString \*str,

802 int start, int len);

803

804 /\* Supposed to have been checked already \*/

805 \_dbus_assert (field \<= DBUS_HEADER_FIELD_LAST);

806 \_dbus_assert (field != DBUS_HEADER_FIELD_INVALID);

807

808 /\* Before we can cache a field, we need to know it has the right type \*/

809 type = \_dbus_type_reader_get_current_type (variant_reader);

810

811 \_dbus_assert (\_dbus_header_field_types\[field\].code == field);

812

813 expected_type = EXPECTED_TYPE_OF_FIELD (field);

814 if (type != expected_type)

815 {

816 \_dbus_verbose ("Field %d should have type %d but has %d\n",

817 field, expected_type, type);

818 return DBUS_INVALID_HEADER_FIELD_HAS_WRONG_TYPE;

819 }

820

821 /\* If the field was provided twice, we aren't happy \*/

822 if (header-\>fields\[field\].value_pos \>= 0)

823 {

824 \_dbus_verbose ("Header field %d seen a second time\n", field);

825 return DBUS_INVALID_HEADER_FIELD_APPEARS_TWICE;

826 }

827

828 /\* Now we can cache and look at the field content \*/

829 \_dbus_verbose ("initially caching field %d\n", field);

830 \_dbus_header_cache_one (header, field, variant_reader);

831

832 string_validation_func = NULL;

833

834 /\* make compiler happy that all this is initialized \*/

835 v_UINT32 = 0;

836 value_str = NULL;

837 value_pos = -1;

838 str_data_pos = -1;

839 bad_string_code = DBUS_VALID;

840

841 if (expected_type == DBUS_TYPE_UINT32)

842 {

843 \_dbus_header_get_field_basic (header, field, expected_type,

844 &v_UINT32);

845 }

846 else if (expected_type == DBUS_TYPE_STRING \|\|

847 expected_type == DBUS_TYPE_OBJECT_PATH \|\|

848 expected_type == DBUS_TYPE_SIGNATURE)

849 {

850 \_dbus_header_get_field_raw (header, field,

851 &value_str, &value_pos);

852 str_data_pos = \_DBUS_ALIGN_VALUE (value_pos, 4) + 4;

853 }

854 else

855 {

856 \_dbus_assert_not_reached ("none of the known fields should have this type");

857 }

858

859 switch (field)

860 {

861 case DBUS_HEADER_FIELD_DESTINATION:

862 string_validation_func = \_dbus_validate_bus_name;

863 bad_string_code = DBUS_INVALID_BAD_DESTINATION;

864 break;

865 case DBUS_HEADER_FIELD_INTERFACE:

866 string_validation_func = \_dbus_validate_interface;

867 bad_string_code = DBUS_INVALID_BAD_INTERFACE;

868

869 if (\_dbus_string_equal_substring (&\_dbus_local_interface_str,

870 0,

871 \_dbus_string_get_length (&\_dbus_local_interface_str),

872 value_str, str_data_pos))

873 {

874 \_dbus_verbose ("Message is on the local interface\n");

875 return DBUS_INVALID_USES_LOCAL_INTERFACE;

876 }

877 break;

878

879 case DBUS_HEADER_FIELD_MEMBER:

880 string_validation_func = \_dbus_validate_member;

881 bad_string_code = DBUS_INVALID_BAD_MEMBER;

882 break;

883

884 case DBUS_HEADER_FIELD_ERROR_NAME:

885 string_validation_func = \_dbus_validate_error_name;

886 bad_string_code = DBUS_INVALID_BAD_ERROR_NAME;

887 break;

888

889 case DBUS_HEADER_FIELD_SENDER:

890 string_validation_func = \_dbus_validate_bus_name;

891 bad_string_code = DBUS_INVALID_BAD_SENDER;

892 break;

893

894 case DBUS_HEADER_FIELD_PATH:

895 /\* OBJECT_PATH was validated generically due to its type \*/

896 string_validation_func = NULL;

897

898 if (\_dbus_string_equal_substring (&\_dbus_local_path_str,

899 0,

900 \_dbus_string_get_length (&\_dbus_local_path_str),

901 value_str, str_data_pos))

902 {

903 \_dbus_verbose ("Message is from the local path\n");

904 return DBUS_INVALID_USES_LOCAL_PATH;

905 }

906 break;

907

908 case DBUS_HEADER_FIELD_REPLY_SERIAL:

909 /\* Can't be 0 \*/

910 if (v_UINT32 == 0)

911 {

912 return DBUS_INVALID_BAD_SERIAL;

913 }

914 break;

915

916 case DBUS_HEADER_FIELD_UNIX_FDS:

917 /\* Every value makes sense \*/

918 break;

919

920 case DBUS_HEADER_FIELD_SIGNATURE:

921 /\* SIGNATURE validated generically due to its type \*/

922 string_validation_func = NULL;

923 break;

924

925 case DBUS_HEADER_FIELD_CONTAINER_INSTANCE:

926 /\* OBJECT_PATH was validated generically due to its type \*/

927 string_validation_func = NULL;

928 break;

929

930 default:

931 \_dbus_assert_not_reached ("unknown field shouldn't be seen here");

932 break;

933 }

934

935 if (string_validation_func)

936 {

937 dbus_uint32_t len;

938

939 \_dbus_assert (bad_string_code != DBUS_VALID);

940

941 len = \_dbus_marshal_read_uint32 (value_str, value_pos,

942 \_dbus_header_get_byte_order (header),

943 NULL);

944

945\#if 0

946 \_dbus_verbose ("Validating string header field; code %d if fails\n",

947 bad_string_code);

948\#endif

949 if (!(\*string_validation_func) (value_str, str_data_pos, len))

950 return bad_string_code;

951 }

952

953 return DBUS_VALID;

954}

955

980dbus_bool_t

981\_dbus_header_load (DBusHeader \*header,

982 DBusValidationMode mode,

983 DBusValidity \*validity,

984 int byte_order,

985 int fields_array_len,

986 int header_len,

987 int body_len,

988 const DBusString \*str)

989{

990 int leftover;

991 DBusValidity v;

992 DBusTypeReader reader;

993 DBusTypeReader array_reader;

994 unsigned char v_byte;

995 dbus_uint32_t v_uint32;

996 dbus_uint32_t serial;

997 int padding_start;

998 int padding_len;

999 int i;

1000 int len;

1001

1002 len = \_dbus_string_get_length (str);

1003

1004 \_dbus_assert (header_len \<= len);

1005 \_dbus_assert (\_dbus_string_get_length (&header-\>data) == 0);

1006

1007 if (!\_dbus_string_copy_len (str, 0, header_len, &header-\>data, 0))

1008 {

1009 \_dbus_verbose ("Failed to copy buffer into new header\n");

1010 \*validity = DBUS_VALIDITY_UNKNOWN_OOM_ERROR;

1011 return FALSE;

1012 }

1013

1014 if (mode == DBUS_VALIDATION_MODE_WE_TRUST_THIS_DATA_ABSOLUTELY)

1015 {

1016 leftover = len - header_len - body_len;

1017 }

1018 else

1019 {

1020 v = \_dbus_validate_body_with_reason (&\_dbus_header_signature_str, 0,

1021 byte_order,

1022 &leftover,

1023 str, 0, len);

1024

1025 if (v != DBUS_VALID)

1026 {

1027 \*validity = v;

1028 goto invalid;

1029 }

1030 }

1031

1032 \_dbus_assert (leftover \< len);

1033

1034 padding_len = header_len - (FIRST_FIELD_OFFSET + fields_array_len);

1035 padding_start = FIRST_FIELD_OFFSET + fields_array_len;

1036 \_dbus_assert (header_len == (int) \_DBUS_ALIGN_VALUE (padding_start, 8));

1037 \_dbus_assert (header_len == padding_start + padding_len);

1038

1039 if (mode != DBUS_VALIDATION_MODE_WE_TRUST_THIS_DATA_ABSOLUTELY)

1040 {

1041 if (!\_dbus_string_validate_nul (str, padding_start, padding_len))

1042 {

1043 \*validity = DBUS_INVALID_ALIGNMENT_PADDING_NOT_NUL;

1044 goto invalid;

1045 }

1046 }

1047

1048 header-\>padding = padding_len;

1049

1050 if (mode == DBUS_VALIDATION_MODE_WE_TRUST_THIS_DATA_ABSOLUTELY)

1051 {

1052 \*validity = DBUS_VALID;

1053 return TRUE;

1054 }

1055

1056 /\* We now know the data is well-formed, but we have to check that

1057 \* it's valid.

1058 \*/

1059

1060 \_dbus_type_reader_init (&reader,

1061 byte_order,

1062 &\_dbus_header_signature_str, 0,

1063 str, 0);

1064

1065 /\* BYTE ORDER \*/

1066 \_dbus_assert (\_dbus_type_reader_get_current_type (&reader) == DBUS_TYPE_BYTE);

1067 \_dbus_assert (\_dbus_type_reader_get_value_pos (&reader) == BYTE_ORDER_OFFSET);

1068 \_dbus_type_reader_read_basic (&reader, &v_byte);

1069 \_dbus_type_reader_next (&reader);

1070

1071 \_dbus_assert (v_byte == byte_order);

1072

1073 /\* MESSAGE TYPE \*/

1074 \_dbus_assert (\_dbus_type_reader_get_current_type (&reader) == DBUS_TYPE_BYTE);

1075 \_dbus_assert (\_dbus_type_reader_get_value_pos (&reader) == TYPE_OFFSET);

1076 \_dbus_type_reader_read_basic (&reader, &v_byte);

1077 \_dbus_type_reader_next (&reader);

1078

1079 /\* unknown message types are supposed to be ignored, so only validation here is

1080 \* that it isn't invalid

1081 \*/

1082 if (v_byte == DBUS_MESSAGE_TYPE_INVALID)

1083 {

1084 \*validity = DBUS_INVALID_BAD_MESSAGE_TYPE;

1085 goto invalid;

1086 }

1087

1088 /\* FLAGS \*/

1089 \_dbus_assert (\_dbus_type_reader_get_current_type (&reader) == DBUS_TYPE_BYTE);

1090 \_dbus_assert (\_dbus_type_reader_get_value_pos (&reader) == FLAGS_OFFSET);

1091 \_dbus_type_reader_read_basic (&reader, &v_byte);

1092 \_dbus_type_reader_next (&reader);

1093

1094 /\* unknown flags should be ignored \*/

1095

1096 /\* PROTOCOL VERSION \*/

1097 \_dbus_assert (\_dbus_type_reader_get_current_type (&reader) == DBUS_TYPE_BYTE);

1098 \_dbus_assert (\_dbus_type_reader_get_value_pos (&reader) == VERSION_OFFSET);

1099 \_dbus_type_reader_read_basic (&reader, &v_byte);

1100 \_dbus_type_reader_next (&reader);

1101

1102 if (v_byte != DBUS_MAJOR_PROTOCOL_VERSION)

1103 {

1104 \*validity = DBUS_INVALID_BAD_PROTOCOL_VERSION;

1105 goto invalid;

1106 }

1107

1108 /\* BODY LENGTH \*/

1109 \_dbus_assert (\_dbus_type_reader_get_current_type (&reader) == DBUS_TYPE_UINT32);

1110 \_dbus_assert (\_dbus_type_reader_get_value_pos (&reader) == BODY_LENGTH_OFFSET);

1111 \_dbus_type_reader_read_basic (&reader, &v_uint32);

1112 \_dbus_type_reader_next (&reader);

1113

1114 \_dbus_assert (body_len == (signed) v_uint32);

1115

1116 /\* SERIAL \*/

1117 \_dbus_assert (\_dbus_type_reader_get_current_type (&reader) == DBUS_TYPE_UINT32);

1118 \_dbus_assert (\_dbus_type_reader_get_value_pos (&reader) == SERIAL_OFFSET);

1119 \_dbus_type_reader_read_basic (&reader, &serial);

1120 \_dbus_type_reader_next (&reader);

1121

1122 if (serial == 0)

1123 {

1124 \*validity = DBUS_INVALID_BAD_SERIAL;

1125 goto invalid;

1126 }

1127

1128 \_dbus_assert (\_dbus_type_reader_get_current_type (&reader) == DBUS_TYPE_ARRAY);

1129 \_dbus_assert (\_dbus_type_reader_get_value_pos (&reader) == FIELDS_ARRAY_LENGTH_OFFSET);

1130

1131 \_dbus_type_reader_recurse (&reader, &array_reader);

1132 while (\_dbus_type_reader_get_current_type (&array_reader) != DBUS_TYPE_INVALID)

1133 {

1134 DBusTypeReader struct_reader;

1135 DBusTypeReader variant_reader;

1136 unsigned char field_code;

1137

1138 \_dbus_assert (\_dbus_type_reader_get_current_type (&array_reader) == DBUS_TYPE_STRUCT);

1139

1140 \_dbus_type_reader_recurse (&array_reader, &struct_reader);

1141

1142 \_dbus_assert (\_dbus_type_reader_get_current_type (&struct_reader) == DBUS_TYPE_BYTE);

1143 \_dbus_type_reader_read_basic (&struct_reader, &field_code);

1144 \_dbus_type_reader_next (&struct_reader);

1145

1146 if (field_code == DBUS_HEADER_FIELD_INVALID)

1147 {

1148 \_dbus_verbose ("invalid header field code\n");

1149 \*validity = DBUS_INVALID_HEADER_FIELD_CODE;

1150 goto invalid;

1151 }

1152

1153 if (field_code \> DBUS_HEADER_FIELD_LAST)

1154 {

1155 \_dbus_verbose ("unknown header field code %d, skipping\n",

1156 field_code);

1157 goto next_field;

1158 }

1159

1160 \_dbus_assert (\_dbus_type_reader_get_current_type (&struct_reader) == DBUS_TYPE_VARIANT);

1161 \_dbus_type_reader_recurse (&struct_reader, &variant_reader);

1162

1163 v = load_and_validate_field (header, field_code, &variant_reader);

1164 if (v != DBUS_VALID)

1165 {

1166 \_dbus_verbose ("Field %d was invalid\n", field_code);

1167 \*validity = v;

1168 goto invalid;

1169 }

1170

1171 next_field:

1172 \_dbus_type_reader_next (&array_reader);

1173 }

1174

1175 /\* Anything we didn't fill in is now known not to exist \*/

1176 i = 0;

1177 while (i \<= DBUS_HEADER_FIELD_LAST)

1178 {

1179 if (header-\>fields\[i\].value_pos == \_DBUS_HEADER_FIELD_VALUE_UNKNOWN)

1180 header-\>fields\[i\].value_pos = \_DBUS_HEADER_FIELD_VALUE_NONEXISTENT;

1181 ++i;

1182 }

1183

1184 v = check_mandatory_fields (header);

1185 if (v != DBUS_VALID)

1186 {

1187 \_dbus_verbose ("Mandatory fields were missing, code %d\n", v);

1188 \*validity = v;

1189 goto invalid;

1190 }

1191

1192 \*validity = DBUS_VALID;

1193 return TRUE;

1194

1195 invalid:

1196 \_dbus_string_set_length (&header-\>data, 0);

1197 return FALSE;

1198}

1199

1206void

1207\_dbus_header_update_lengths (DBusHeader \*header,

1208 int body_len)

1209{

1210 \_dbus_marshal_set_uint32 (&header-\>data,

1211 BODY_LENGTH_OFFSET,

1212 body_len,

1213 \_dbus_header_get_byte_order (header));

1214}

1215

1229static dbus_bool_t

1230find_field_for_modification (DBusHeader \*header,

1231 int field,

1232 DBusTypeReader \*reader,

1233 DBusTypeReader \*realign_root)

1234{

1235 dbus_bool_t retval;

1236

1237 retval = FALSE;

1238

1239 \_dbus_type_reader_init (realign_root,

1240 \_dbus_header_get_byte_order (header),

1241 &\_dbus_header_signature_str,

1242 FIELDS_ARRAY_SIGNATURE_OFFSET,

1243 &header-\>data,

1244 FIELDS_ARRAY_LENGTH_OFFSET);

1245

1246 \_dbus_type_reader_recurse (realign_root, reader);

1247

1248 while (\_dbus_type_reader_get_current_type (reader) != DBUS_TYPE_INVALID)

1249 {

1250 DBusTypeReader sub;

1251 unsigned char field_code;

1252

1253 \_dbus_type_reader_recurse (reader, &sub);

1254

1255 \_dbus_assert (\_dbus_type_reader_get_current_type (&sub) == DBUS_TYPE_BYTE);

1256 \_dbus_type_reader_read_basic (&sub, &field_code);

1257

1258 if (field_code == (unsigned) field)

1259 {

1260 \_dbus_assert (\_dbus_type_reader_get_current_type (reader) == DBUS_TYPE_STRUCT);

1261 retval = TRUE;

1262 goto done;

1263 }

1264

1265 \_dbus_type_reader_next (reader);

1266 }

1267

1268 done:

1269 return retval;

1270}

1271

1283dbus_bool_t

1284\_dbus_header_set_field_basic (DBusHeader \*header,

1285 int field,

1286 int type,

1287 const void \*value)

1288{

1289 \_dbus_assert (field \<= DBUS_HEADER_FIELD_LAST);

1290

1291 if (!reserve_header_padding (header))

1292 return FALSE;

1293

1294 /\* If the field exists we set, otherwise we append \*/

1295 if (\_dbus_header_cache_check (header, field))

1296 {

1297 DBusTypeReader reader;

1298 DBusTypeReader realign_root;

1299

1300 if (!find_field_for_modification (header, field,

1301 &reader, &realign_root))

1302 \_dbus_assert_not_reached ("field was marked present in cache but wasn't found");

1303

1304 if (!set_basic_field (&reader, field, type, value, &realign_root))

1305 return FALSE;

1306 }

1307 else

1308 {

1309 DBusTypeWriter writer;

1310 DBusTypeWriter array;

1311

1312 \_dbus_type_writer_init_values_only (&writer,

1313 \_dbus_header_get_byte_order (header),

1314 &\_dbus_header_signature_str,

1315 FIELDS_ARRAY_SIGNATURE_OFFSET,

1316 &header-\>data,

1317 FIELDS_ARRAY_LENGTH_OFFSET);

1318

1319 /\* recurse into array without creating a new length, and jump to

1320 \* end of array.

1321 \*/

1322 if (!\_dbus_type_writer_append_array (&writer,

1323 &\_dbus_header_signature_str,

1324 FIELDS_ARRAY_ELEMENT_SIGNATURE_OFFSET,

1325 &array))

1326 \_dbus_assert_not_reached ("recurse into ARRAY should not have used memory");

1327

1328 \_dbus_assert (array.u.array.len_pos == FIELDS_ARRAY_LENGTH_OFFSET);

1329 \_dbus_assert (array.u.array.start_pos == FIRST_FIELD_OFFSET);

1330 \_dbus_assert (array.value_pos == HEADER_END_BEFORE_PADDING (header));

1331

1332 if (!write_basic_field (&array,

1333 field, type, value))

1334 return FALSE;

1335

1336 if (!\_dbus_type_writer_unrecurse (&writer, &array))

1337 \_dbus_assert_not_reached ("unrecurse from ARRAY should not have used memory");

1338 }

1339

1340 correct_header_padding (header);

1341

1342 /\* We could be smarter about this (only invalidate fields after the

1343 \* one we modified, or even only if the one we modified changed

1344 \* length). But this hack is a start.

1345 \*/

1346 \_dbus_header_cache_invalidate_all (header);

1347

1348 return TRUE;

1349}

1350

1361dbus_bool_t

1362\_dbus_header_get_field_basic (DBusHeader \*header,

1363 int field,

1364 int type,

1365 void \*value)

1366{

1367 \_dbus_assert (field != DBUS_HEADER_FIELD_INVALID);

1368 \_dbus_assert (field \<= DBUS_HEADER_FIELD_LAST);

1369 \_dbus_assert (\_dbus_header_field_types\[field\].code == field);

1370 /\* in light of this you might ask why the type is passed in;

1371 \* the only rationale I can think of is so the caller has

1372 \* to specify its expectation and breaks if we change it

1373 \*/

1374 \_dbus_assert (type == EXPECTED_TYPE_OF_FIELD (field));

1375

1376 if (!\_dbus_header_cache_check (header, field))

1377 return FALSE;

1378

1379 \_dbus_assert (header-\>fields\[field\].value_pos \>= 0);

1380

1381 \_dbus_marshal_read_basic (&header-\>data,

1382 header-\>fields\[field\].value_pos,

1383 type, value, \_dbus_header_get_byte_order (header),

1384 NULL);

1385

1386 return TRUE;

1387}

1388

1402dbus_bool_t

1403\_dbus_header_get_field_raw (DBusHeader \*header,

1404 int field,

1405 const DBusString \*\*str,

1406 int \*pos)

1407{

1408 if (!\_dbus_header_cache_check (header, field))

1409 return FALSE;

1410

1411 if (str)

1412 \*str = &header-\>data;

1413 if (pos)

1414 \*pos = header-\>fields\[field\].value_pos;

1415

1416 return TRUE;

1417}

1418

1426dbus_bool_t

1427\_dbus_header_delete_field (DBusHeader \*header,

1428 int field)

1429{

1430 DBusTypeReader reader;

1431 DBusTypeReader realign_root;

1432

1433 if (\_dbus_header_cache_known_nonexistent (header, field))

1434 return TRUE; /\* nothing to do \*/

1435

1436 /\* Scan to the field we want, delete and realign, reappend

1437 \* padding. Field may turn out not to exist.

1438 \*/

1439 if (!find_field_for_modification (header, field,

1440 &reader, &realign_root))

1441 return TRUE; /\* nothing to do \*/

1442

1443 if (!reserve_header_padding (header))

1444 return FALSE;

1445

1446 if (!\_dbus_type_reader_delete (&reader,

1447 &realign_root))

1448 return FALSE;

1449

1450 correct_header_padding (header);

1451

1452 \_dbus_header_cache_invalidate_all (header);

1453

1454 \_dbus_assert (!\_dbus_header_cache_check (header, field)); /\* Expensive assertion ... \*/

1455

1456 return TRUE;

1457}

1458

1467void

1468\_dbus_header_toggle_flag (DBusHeader \*header,

1469 dbus_uint32_t flag,

1470 dbus_bool_t value)

1471{

1472 unsigned char \*flags_p;

1473

1474 flags_p = \_dbus_string_get_udata_len (&header-\>data, FLAGS_OFFSET, 1);

1475

1476 if (value)

1477 \*flags_p \|= flag;

1478 else

1479 \*flags_p &= ~flag;

1480}

1481

1489dbus_bool_t

1490\_dbus_header_get_flag (DBusHeader \*header,

1491 dbus_uint32_t flag)

1492{

1493 const unsigned char \*flags_p;

1494

1495 flags_p = \_dbus_string_get_const_udata_len (&header-\>data, FLAGS_OFFSET, 1);

1496

1497 return (\*flags_p & flag) != 0;

1498}

1499

1506void

1507\_dbus_header_byteswap (DBusHeader \*header,

1508 int new_order)

1509{

1510 char byte_order;

1511

1512 byte_order = \_dbus_header_get_byte_order (header);

1513

1514 if (byte_order == new_order)

1515 return;

1516

1517 \_dbus_marshal_byteswap (&\_dbus_header_signature_str,

1518 0, byte_order,

1519 new_order,

1520 &header-\>data, 0);

1521

1522 \_dbus_string_set_byte (&header-\>data, BYTE_ORDER_OFFSET, new_order);

1523}

1524

1531dbus_bool_t

1532\_dbus_header_remove_unknown_fields (DBusHeader \*header)

1533{

1534 DBusTypeReader array;

1535 DBusTypeReader fields_reader;

1536

1537 \_dbus_type_reader_init (&fields_reader,

1538 \_dbus_header_get_byte_order (header),

1539 &\_dbus_header_signature_str,

1540 FIELDS_ARRAY_SIGNATURE_OFFSET,

1541 &header-\>data,

1542 FIELDS_ARRAY_LENGTH_OFFSET);

1543

1544 \_dbus_type_reader_recurse (&fields_reader, &array);

1545

1546 while (\_dbus_type_reader_get_current_type (&array) != DBUS_TYPE_INVALID)

1547 {

1548 DBusTypeReader sub;

1549 unsigned char field_code;

1550

1551 \_dbus_type_reader_recurse (&array, &sub);

1552

1553 \_dbus_assert (\_dbus_type_reader_get_current_type (&sub) == DBUS_TYPE_BYTE);

1554 \_dbus_type_reader_read_basic (&sub, &field_code);

1555

1556 if (field_code \> DBUS_HEADER_FIELD_LAST)

1557 {

1558 if (!reserve_header_padding (header))

1559 return FALSE;

1560

1561 if (!\_dbus_type_reader_delete (&array, &fields_reader))

1562 return FALSE;

1563

1564 correct_header_padding (header);

1565 \_dbus_header_cache_invalidate_all (header);

1566 }

1567 else

1568 {

1569 \_dbus_type_reader_next (&array);

1570 }

1571 }

1572

1573 return TRUE;

1574}

1575

\_dbus_assert_not_reached

\#define \_dbus_assert_not_reached(explanation)

Aborts with an error message if called.

**Definition** dbus-internals.h:164

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_DBUS_INT32_MAX

\#define \_DBUS_INT32_MAX

Maximum value of type "int32".

**Definition** dbus-internals.h:323

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

BODY_LENGTH_OFFSET

\#define BODY_LENGTH_OFFSET

Offset to body length from start of header.

**Definition** dbus-marshal-header.c:63

\_dbus_type_writer_init_values_only

void \_dbus_type_writer_init_values_only(DBusTypeWriter \*writer, int byte_order, const DBusString \*type_str, int type_pos, DBusString \*value_str, int value_pos)

Like \_dbus_type_writer_init(), except the type string passed in should correspond to an existing sign...

**Definition** dbus-marshal-recursive.c:1583

\_dbus_type_reader_get_value_pos

int \_dbus_type_reader_get_value_pos(const DBusTypeReader \*reader)

Gets the current position in the value block.

**Definition** dbus-marshal-recursive.c:837

\_dbus_type_reader_init

void \_dbus_type_reader_init(DBusTypeReader \*reader, int byte_order, const DBusString \*type_str, int type_pos, const DBusString \*value_str, int value_pos)

Initializes a type reader.

**Definition** dbus-marshal-recursive.c:732

EXPECTED_TYPE_OF_FIELD

\#define EXPECTED_TYPE_OF_FIELD(field)

Macro to look up the correct type for a field.

**Definition** dbus-marshal-header.c:93

\_dbus_validate_error_name

dbus_bool_t \_dbus_validate_error_name(const DBusString \*str, int start, int len)

Checks that the given range of the string is a valid error name in the D-Bus protocol.

**Definition** dbus-marshal-validate.c:1124

\_dbus_header_set_field_basic

dbus_bool_t \_dbus_header_set_field_basic(DBusHeader \*header, int field, int type, const void \*value)

Sets the value of a field with basic type.

**Definition** dbus-marshal-header.c:1284

\_dbus_header_get_message_type

int \_dbus_header_get_message_type(DBusHeader \*header)

Gets the type of the message.

**Definition** dbus-marshal-header.c:391

\_dbus_header_get_field_basic

dbus_bool_t \_dbus_header_get_field_basic(DBusHeader \*header, int field, int type, void \*value)

Gets the value of a field with basic type.

**Definition** dbus-marshal-header.c:1362

SERIAL_OFFSET

\#define SERIAL_OFFSET

Offset to client serial from start of header.

**Definition** dbus-marshal-header.c:65

\_dbus_marshal_set_uint32

void \_dbus_marshal_set_uint32(DBusString \*str, int pos, dbus_uint32_t value, int byte_order)

Sets the 4 bytes at the given offset to a marshaled unsigned integer, replacing anything found there ...

**Definition** dbus-marshal-basic.c:260

\_dbus_type_writer_recurse

dbus_bool_t \_dbus_type_writer_recurse(DBusTypeWriter \*writer, int container_type, const DBusString \*contained_type, int contained_type_start, DBusTypeWriter \*sub)

Opens a new container and writes out the initial information for that container.

**Definition** dbus-marshal-recursive.c:2108

VERSION_OFFSET

\#define VERSION_OFFSET

Offset to version from start of header.

**Definition** dbus-marshal-header.c:61

\_dbus_header_get_flag

dbus_bool_t \_dbus_header_get_flag(DBusHeader \*header, dbus_uint32_t flag)

Gets a message flag bit, returning TRUE if the bit is set.

**Definition** dbus-marshal-header.c:1490

\_dbus_marshal_byteswap

void \_dbus_marshal_byteswap(const DBusString \*signature, int signature_start, int old_byte_order, int new_byte_order, DBusString \*value_str, int value_pos)

Byteswaps the marshaled data in the given value_str.

**Definition** dbus-marshal-byteswap.c:224

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

\_dbus_marshal_read_uint32

dbus_uint32_t \_dbus_marshal_read_uint32(const DBusString \*str, int pos, int byte_order, int \*new_pos)

Convenience function to demarshal a 32 bit unsigned integer.

**Definition** dbus-marshal-basic.c:476

\_dbus_validate_member

dbus_bool_t \_dbus_validate_member(const DBusString \*str, int start, int len)

Checks that the given range of the string is a valid member name in the D-Bus protocol.

**Definition** dbus-marshal-validate.c:1063

\_dbus_type_reader_next

dbus_bool_t \_dbus_type_reader_next(DBusTypeReader \*reader)

Skip to the next value on this "level".

**Definition** dbus-marshal-recursive.c:1053

\_dbus_header_delete_field

dbus_bool_t \_dbus_header_delete_field(DBusHeader \*header, int field)

Deletes a field, if it exists.

**Definition** dbus-marshal-header.c:1427

\_dbus_header_remove_unknown_fields

dbus_bool_t \_dbus_header_remove_unknown_fields(DBusHeader \*header)

Remove every header field not known to this version of dbus.

**Definition** dbus-marshal-header.c:1532

\_dbus_header_get_serial

dbus_uint32_t \_dbus_header_get_serial(DBusHeader \*header)

See dbus_message_get_serial()

**Definition** dbus-marshal-header.c:432

FLAGS_OFFSET

\#define FLAGS_OFFSET

Offset to flags from start of header.

**Definition** dbus-marshal-header.c:59

FIELDS_ARRAY_SIGNATURE_OFFSET

\#define FIELDS_ARRAY_SIGNATURE_OFFSET

Offset from start of \_dbus_header_signature_str to the signature of the fields array.

**Definition** dbus-marshal-header.c:49

MAX_POSSIBLE_HEADER_PADDING

\#define MAX_POSSIBLE_HEADER_PADDING

The most padding we could ever need for a header.

**Definition** dbus-marshal-header.c:96

\_dbus_type_reader_delete

dbus_bool_t \_dbus_type_reader_delete(DBusTypeReader \*reader, const DBusTypeReader \*realign_root)

Recursively deletes any value pointed to by the reader, leaving the reader valid to continue reading.

**Definition** dbus-marshal-recursive.c:1419

\_dbus_type_reader_read_basic

void \_dbus_type_reader_read_basic(const DBusTypeReader \*reader, void \*value)

Reads a basic-typed value, as with \_dbus_marshal_read_basic().

**Definition** dbus-marshal-recursive.c:869

BYTE_ORDER_OFFSET

\#define BYTE_ORDER_OFFSET

Offset to byte order from start of header.

**Definition** dbus-marshal-header.c:55

FIRST_FIELD_OFFSET

\#define FIRST_FIELD_OFFSET

Offset to first field in header.

**Definition** dbus-marshal-header.c:69

\_dbus_validate_interface

dbus_bool_t \_dbus_validate_interface(const DBusString \*str, int start, int len)

Checks that the given range of the string is a valid interface name in the D-Bus protocol.

**Definition** dbus-marshal-validate.c:987

\_dbus_type_reader_set_basic

dbus_bool_t \_dbus_type_reader_set_basic(DBusTypeReader \*reader, const void \*value, const DBusTypeReader \*realign_root)

Sets a new value for the basic type value pointed to by the reader, leaving the reader valid to conti...

**Definition** dbus-marshal-recursive.c:1362

\_dbus_validate_body_with_reason

DBusValidity \_dbus_validate_body_with_reason(const DBusString \*expected_signature, int expected_signature_start, int byte_order, int \*bytes_remaining, const DBusString \*value_str, int value_pos, int len)

Verifies that the range of value_str from value_pos to value_end is a legitimate value of type expect...

**Definition** dbus-marshal-validate.c:767

\_dbus_marshal_read_basic

void \_dbus_marshal_read_basic(const DBusString \*str, int pos, int type, void \*value, int byte_order, int \*new_pos)

Demarshals a basic-typed value.

**Definition** dbus-marshal-basic.c:514

\_dbus_type_reader_get_current_type

int \_dbus_type_reader_get_current_type(const DBusTypeReader \*reader)

Gets the type of the value the reader is currently pointing to; or for a types-only reader gets the t...

**Definition** dbus-marshal-recursive.c:785

\_dbus_header_free

void \_dbus_header_free(DBusHeader \*header)

Frees a header.

**Definition** dbus-marshal-header.c:481

\_dbus_validate_bus_name

dbus_bool_t \_dbus_validate_bus_name(const DBusString \*str, int start, int len)

Checks that the given range of the string is a valid bus name in the D-Bus protocol.

**Definition** dbus-marshal-validate.c:1253

\_dbus_header_init

dbus_bool_t \_dbus_header_init(DBusHeader \*header)

Initializes a header, but doesn't prepare it for use; to make the header valid, you have to call \_dbu...

**Definition** dbus-marshal-header.c:465

\_dbus_header_create

dbus_bool_t \_dbus_header_create(DBusHeader \*header, int byte_order, int message_type, const char \*destination, const char \*path, const char \*interface, const char \*member, const char \*error_name)

Fills in the primary fields of the header, so the header is ready for use.

**Definition** dbus-marshal-header.c:533

FIELDS_ARRAY_ELEMENT_SIGNATURE_OFFSET

\#define FIELDS_ARRAY_ELEMENT_SIGNATURE_OFFSET

Offset from start of \_dbus_header_signature_str to the signature of an element of the fields array.

**Definition** dbus-marshal-header.c:51

\_dbus_type_writer_unrecurse

dbus_bool_t \_dbus_type_writer_unrecurse(DBusTypeWriter \*writer, DBusTypeWriter \*sub)

Closes a container created by \_dbus_type_writer_recurse() and writes any additional information to th...

**Definition** dbus-marshal-recursive.c:2178

\_dbus_type_writer_append_array

dbus_bool_t \_dbus_type_writer_append_array(DBusTypeWriter \*writer, const DBusString \*contained_type, int contained_type_start, DBusTypeWriter \*sub)

Append to an existing array.

**Definition** dbus-marshal-recursive.c:2142

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

FIELDS_ARRAY_LENGTH_OFFSET

\#define FIELDS_ARRAY_LENGTH_OFFSET

Offset to fields array length from start of header.

**Definition** dbus-marshal-header.c:67

HEADER_END_BEFORE_PADDING

\#define HEADER_END_BEFORE_PADDING(header)

Compute the end of the header, ignoring padding.

**Definition** dbus-marshal-header.c:128

\_dbus_header_get_field_raw

dbus_bool_t \_dbus_header_get_field_raw(DBusHeader \*header, int field, const DBusString \*\*str, int \*pos)

Gets the raw marshaled data for a field.

**Definition** dbus-marshal-header.c:1403

TYPE_OFFSET

\#define TYPE_OFFSET

Offset to type from start of header.

**Definition** dbus-marshal-header.c:57

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

DBUS_HEADER_FIELD_UNIX_FDS

\#define DBUS_HEADER_FIELD_UNIX_FDS

Header field code for the number of unix file descriptors associated with this message.

**Definition** dbus-protocol.h:304

DBUS_HEADER_FIELD_INVALID

\#define DBUS_HEADER_FIELD_INVALID

Not equal to any valid header field code.

**Definition** dbus-protocol.h:268

DBUS_MESSAGE_TYPE_METHOD_CALL

\#define DBUS_MESSAGE_TYPE_METHOD_CALL

Message type of a method call message, see dbus_message_get_type()

**Definition** dbus-protocol.h:236

DBUS_HEADER_FIELD_PATH

\#define DBUS_HEADER_FIELD_PATH

Header field code for the path - the path is the object emitting a signal or the object receiving a m...

**Definition** dbus-protocol.h:272

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

DBUS_HEADER_FIELD_INTERFACE

\#define DBUS_HEADER_FIELD_INTERFACE

Header field code for the interface containing a member (method or signal).

**Definition** dbus-protocol.h:276

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

DBUS_TYPE_BYTE

\#define DBUS_TYPE_BYTE

Type code marking an 8-bit unsigned integer.

**Definition** dbus-protocol.h:68

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

DBUS_MESSAGE_TYPE_SIGNAL

\#define DBUS_MESSAGE_TYPE_SIGNAL

Message type of a signal message, see dbus_message_get_type()

**Definition** dbus-protocol.h:242

DBUS_TYPE_STRING

\#define DBUS_TYPE_STRING

Type code marking a UTF-8 encoded, nul-terminated Unicode string.

**Definition** dbus-protocol.h:104

DBUS_HEADER_SIGNATURE

\#define DBUS_HEADER_SIGNATURE

Header format is defined as a signature: byte byte order byte message type ID byte flags byte protoco...

**Definition** dbus-protocol.h:332

DBUS_TYPE_ARRAY

\#define DBUS_TYPE_ARRAY

Type code marking a D-Bus array type.

**Definition** dbus-protocol.h:122

DBUS_HEADER_FIELD_LAST

\#define DBUS_HEADER_FIELD_LAST

Value of the highest-numbered header field code, can be used to determine the size of an array indexe...

**Definition** dbus-protocol.h:317

DBUS_TYPE_INVALID

\#define DBUS_TYPE_INVALID

Type code that is never equal to a legitimate type code.

**Definition** dbus-protocol.h:62

DBUS_LITTLE_ENDIAN

\#define DBUS_LITTLE_ENDIAN

Code marking LSB-first byte order in the wire protocol.

**Definition** dbus-protocol.h:55

DBUS_HEADER_FIELD_ERROR_NAME

\#define DBUS_HEADER_FIELD_ERROR_NAME

Header field code for an error name (found in DBUS_MESSAGE_TYPE_ERROR messages).

**Definition** dbus-protocol.h:282

DBUS_MESSAGE_TYPE_INVALID

\#define DBUS_MESSAGE_TYPE_INVALID

This value is never a valid message type, see dbus_message_get_type()

**Definition** dbus-protocol.h:234

DBUS_HEADER_FIELD_DESTINATION

\#define DBUS_HEADER_FIELD_DESTINATION

Header field code for the destination bus name of a message.

**Definition** dbus-protocol.h:290

DBUS_MAJOR_PROTOCOL_VERSION

\#define DBUS_MAJOR_PROTOCOL_VERSION

Protocol version.

**Definition** dbus-protocol.h:59

DBUS_TYPE_STRUCT

\#define DBUS_TYPE_STRUCT

STRUCT and DICT_ENTRY are sort of special since their codes can't appear in a type string,...

**Definition** dbus-protocol.h:138

DBUS_BIG_ENDIAN

\#define DBUS_BIG_ENDIAN

Code marking MSB-first byte order in the wire protocol.

**Definition** dbus-protocol.h:56

DBUS_TYPE_UINT32

\#define DBUS_TYPE_UINT32

Type code marking a 32-bit unsigned integer.

**Definition** dbus-protocol.h:88

DBUS_PATH_LOCAL

\#define DBUS_PATH_LOCAL

The object path used in local/in-process-generated messages.

**Definition** dbus-shared.h:84

DBUS_INTERFACE_LOCAL

\#define DBUS_INTERFACE_LOCAL

This is a special interface whose methods can only be invoked by the local implementation (messages f...

**Definition** dbus-shared.h:107

\_dbus_string_set_length

dbus_bool_t \_dbus_string_set_length(DBusString \*str, int length)

Sets the length of a string.

**Definition** dbus-string.c:847

\_dbus_string_validate_nul

dbus_bool_t \_dbus_string_validate_nul(const DBusString \*str, int start, int len)

Checks that the given range of the string is all nul bytes.

**Definition** dbus-string.c:2776

\_dbus_string_equal_substring

dbus_bool_t \_dbus_string_equal_substring(const DBusString \*a, int a_start, int a_len, const DBusString \*b, int b_start)

Tests two sub-parts of two DBusString for equality.

**Definition** dbus-string.c:2166

\_dbus_string_copy

dbus_bool_t \_dbus_string_copy(const DBusString \*source, int start, DBusString \*dest, int insert_at)

Like \_dbus_string_move(), but does not delete the section of the source string that's copied to the d...

**Definition** dbus-string.c:1345

\_dbus_string_init_preallocated

dbus_bool_t \_dbus_string_init_preallocated(DBusString \*str, int allocate_size)

Initializes a string that can be up to the given allocation size before it has to realloc.

**Definition** dbus-string.c:139

\_dbus_string_init_const_len

void \_dbus_string_init_const_len(DBusString \*str, const char \*value, int len)

Initializes a constant string with a length.

**Definition** dbus-string.c:217

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

\_dbus_string_lengthen

dbus_bool_t \_dbus_string_lengthen(DBusString \*str, int additional_length)

Makes a string longer by the given number of bytes.

**Definition** dbus-string.c:805

\_dbus_string_get_length

int \_dbus_string_get_length(const DBusString \*str)

Gets the length of a string (not including nul termination).

**Definition** dbus-string.c:784

\_dbus_string_set_byte

void \_dbus_string_set_byte(DBusString \*str, int i, unsigned char byte)

Sets the value of the byte at the given position.

**Definition** dbus-string.c:583

\_dbus_string_get_byte

unsigned char \_dbus_string_get_byte(const DBusString \*str, int start)

Gets the byte at the given position.

**Definition** dbus-string.c:607

\_dbus_string_align_length

dbus_bool_t \_dbus_string_align_length(DBusString \*str, int alignment)

Align the length of a string to a specific alignment (typically 4 or 8) by appending nul bytes to the...

**Definition** dbus-string.c:928

\_dbus_string_copy_len

dbus_bool_t \_dbus_string_copy_len(const DBusString \*source, int start, int len, DBusString \*dest, int insert_at)

Like \_dbus_string_copy(), but can copy a segment from the middle of the source string.

**Definition** dbus-string.c:1437

DBusHeaderField::value_pos

int value_pos

Position of field value, or -1/-2.

**Definition** dbus-marshal-header.h:43

DBusHeader

Message header data and some cached details of it.

**Definition** dbus-marshal-header.h:90

DBusHeader::data

DBusString data

Header network data, stored separately from body so we can independently realloc it.

**Definition** dbus-marshal-header.h:91

DBusHeader::padding

dbus_uint32_t padding

0-7 bytes of alignment in header, the distance from \[B\] to \[C\]

**Definition** dbus-marshal-header.h:106

DBusHeader::fields

DBusHeaderField fields\[DBUS_HEADER_FIELD_LAST+1\]

Track the location of each field in header.

**Definition** dbus-marshal-header.h:102

DBusString

**Definition** dbus-string.h:47

DBusTypeReader

The type reader is an iterator for reading values from a block of values.

**Definition** dbus-marshal-recursive.h:42

DBusTypeWriter

The type writer is an iterator for writing to a block of values.

**Definition** dbus-marshal-recursive.h:68

DBusTypeWriter::start_pos

int start_pos

position of first element in the array

**Definition** dbus-marshal-recursive.h:85

DBusTypeWriter::value_pos

int value_pos

next position to write

**Definition** dbus-marshal-recursive.h:80

DBusTypeWriter::u

union DBusTypeWriter::@3 u

class-specific data

DBusTypeWriter::len_pos

int len_pos

position of length of the array

**Definition** dbus-marshal-recursive.h:86

DBusTypeWriter::value_str

DBusString \* value_str

where to write values

**Definition** dbus-marshal-recursive.h:70

HeaderFieldType

**Definition** dbus-marshal-header.c:72

HeaderFieldType::type

unsigned char type

the value type

**Definition** dbus-marshal-header.c:74

HeaderFieldType::code

unsigned char code

the field code

**Definition** dbus-marshal-header.c:73
