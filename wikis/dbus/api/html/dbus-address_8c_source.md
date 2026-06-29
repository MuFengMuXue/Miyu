dbus-address.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-address.c Server address parser.

3 \*

4 \* Copyright (C) 2003 CodeFactory AB

5 \* Copyright (C) 2004-2007 Red Hat, Inc.

6 \* Copyright (C) 2007 Ralf Habacker

7 \* Copyright (C) 2013 Chengwei Yang / Intel

8 \*

9 \* SPDX-License-Identifier: AFL-2.1 OR GPL-2.0-or-later

10 \*

11 \* Licensed under the Academic Free License version 2.1

12 \*

13 \* This program is free software; you can redistribute it and/or modify

14 \* it under the terms of the GNU General Public License as published by

15 \* the Free Software Foundation; either version 2 of the License, or

16 \* (at your option) any later version.

17 \*

18 \* This program is distributed in the hope that it will be useful,

19 \* but WITHOUT ANY WARRANTY; without even the implied warranty of

20 \* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the

21 \* GNU General Public License for more details.

22 \*

23 \* You should have received a copy of the GNU General Public License

24 \* along with this program; if not, write to the Free Software

25 \* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

26 \*

27 \*/

28

29\#include \<config.h\>

30\#include "dbus-address.h"

31\#include "dbus-internals.h"

32\#include "dbus-list.h"

33\#include "dbus-string.h"

34\#include "dbus-protocol.h"

35\#include \<dbus/dbus-test-tap.h\>

36

48struct DBusAddressEntry

49{

50 DBusString method;

52 DBusList \*keys;

53 DBusList \*values;

54};

55

56

69void

70\_dbus_set_bad_address (DBusError \*error,

71 const char \*address_problem_type,

72 const char \*address_problem_field,

73 const char \*address_problem_other)

74{

75 if (address_problem_type != NULL)

76 dbus_set_error (error, DBUS_ERROR_BAD_ADDRESS,

77 "Server address of type %s was missing argument %s",

78 address_problem_type, address_problem_field);

79 else

80 dbus_set_error (error, DBUS_ERROR_BAD_ADDRESS,

81 "Could not parse server address: %s",

82 address_problem_other);

83}

84

89\#define \_DBUS_ADDRESS_OPTIONALLY_ESCAPED_BYTE(b) \\

90 (((b) \>= 'a' && (b) \<= 'z') \|\| \\

91 ((b) \>= 'A' && (b) \<= 'Z') \|\| \\

92 ((b) \>= '0' && (b) \<= '9') \|\| \\

93 (b) == '-' \|\| \\

94 (b) == '\_' \|\| \\

95 (b) == '/' \|\| \\

96 (b) == '\\' \|\| \\

97 (b) == '\*' \|\| \\

98 (b) == '.')

99

108dbus_bool_t

109\_dbus_address_append_escaped (DBusString \*escaped,

110 const DBusString \*unescaped)

111{

112 const unsigned char \*p;

113 const unsigned char \*end;

114 dbus_bool_t ret;

115 int orig_len;

116

117 ret = FALSE;

118

119 orig_len = \_dbus_string_get_length (escaped);

120 p = \_dbus_string_get_const_udata (unescaped);

121 end = p + \_dbus_string_get_length (unescaped);

122 while (p != end)

123 {

124 if (\_DBUS_ADDRESS_OPTIONALLY_ESCAPED_BYTE (\*p))

125 {

126 if (!\_dbus_string_append_byte (escaped, \*p))

127 goto out;

128 }

129 else

130 {

131 if (!\_dbus_string_append_byte (escaped, '%'))

132 goto out;

133 if (!\_dbus_string_append_byte_as_hex (escaped, \*p))

134 goto out;

135 }

136

137 ++p;

138 }

139

140 ret = TRUE;

141

142 out:

143 if (!ret)

144 \_dbus_string_set_length (escaped, orig_len);

145 return ret;

146}

147

/\* End of internals \*/

149

150static void

151dbus_address_entry_free (DBusAddressEntry \*entry)

152{

153 DBusList \*link;

154

155 \_dbus_string_free (&entry-\>method);

156

157 link = \_dbus_list_get_first_link (&entry-\>keys);

158 while (link != NULL)

159 {

160 \_dbus_string_free (link-\>data);

161 dbus_free (link-\>data);

162

163 link = \_dbus_list_get_next_link (&entry-\>keys, link);

164 }

165 \_dbus_list_clear (&entry-\>keys);

166

167 link = \_dbus_list_get_first_link (&entry-\>values);

168 while (link != NULL)

169 {

170 \_dbus_string_free (link-\>data);

171 dbus_free (link-\>data);

172

173 link = \_dbus_list_get_next_link (&entry-\>values, link);

174 }

175 \_dbus_list_clear (&entry-\>values);

176

177 dbus_free (entry);

178}

179

193void

194dbus_address_entries_free (DBusAddressEntry \*\*entries)

195{

196 int i;

197

198 for (i = 0; entries\[i\] != NULL; i++)

199 dbus_address_entry_free (entries\[i\]);

200 dbus_free (entries);

201}

202

203static DBusAddressEntry \*

204create_entry (void)

205{

206 DBusAddressEntry \*entry;

207

208 entry = dbus_new0 (DBusAddressEntry, 1);

209

210 if (entry == NULL)

211 return NULL;

212

213 if (!\_dbus_string_init (&entry-\>method))

214 {

215 dbus_free (entry);

216 return NULL;

217 }

218

219 return entry;

220}

221

231const char \*

232dbus_address_entry_get_method (DBusAddressEntry \*entry)

233{

234 return \_dbus_string_get_const_data (&entry-\>method);

235}

236

248const char \*

249dbus_address_entry_get_value (DBusAddressEntry \*entry,

250 const char \*key)

251{

252 DBusList \*values, \*keys;

253

254 keys = \_dbus_list_get_first_link (&entry-\>keys);

255 values = \_dbus_list_get_first_link (&entry-\>values);

256

257 while (keys != NULL)

258 {

259 \_dbus_assert (values != NULL);

260

261 if (\_dbus_string_equal_c_str (keys-\>data, key))

262 return \_dbus_string_get_const_data (values-\>data);

263

264 keys = \_dbus_list_get_next_link (&entry-\>keys, keys);

265 values = \_dbus_list_get_next_link (&entry-\>values, values);

266 }

267

268 return NULL;

269}

270

271static dbus_bool_t

272append_unescaped_value (DBusString \*unescaped,

273 const DBusString \*escaped,

274 int escaped_start,

275 int escaped_len,

276 DBusError \*error)

277{

278 const char \*p;

279 const char \*end;

280 dbus_bool_t ret;

281

282 ret = FALSE;

283

284 p = \_dbus_string_get_const_data (escaped) + escaped_start;

285 end = p + escaped_len;

286 while (p != end)

287 {

288 if (\_DBUS_ADDRESS_OPTIONALLY_ESCAPED_BYTE (\*p))

289 {

290 if (!\_dbus_string_append_byte (unescaped, \*p))

291 goto out;

292 }

293 else if (\*p == '%')

294 {

295 /\* Efficiency is king \*/

296 char buf\[3\];

297 DBusString hex;

298 int hex_end;

299

300 ++p;

301

302 if ((p + 2) \> end)

303 {

304 dbus_set_error (error, DBUS_ERROR_BAD_ADDRESS,

305 "In D-Bus address, percent character was not followed by two hex digits");

306 goto out;

307 }

308

309 buf\[0\] = \*p;

310 ++p;

311 buf\[1\] = \*p;

312 buf\[2\] = '\0';

313

314 \_dbus_string_init_const (&hex, buf);

315

316 if (!\_dbus_string_hex_decode (&hex, 0, &hex_end,

317 unescaped,

318 \_dbus_string_get_length (unescaped)))

319 goto out;

320

321 if (hex_end != 2)

322 {

323 dbus_set_error (error, DBUS_ERROR_BAD_ADDRESS,

324 "In D-Bus address, percent character was followed by characters other than hex digits");

325 goto out;

326 }

327 }

328 else

329 {

330 /\* Error, should have been escaped \*/

331 dbus_set_error (error, DBUS_ERROR_BAD_ADDRESS,

332 "In D-Bus address, character '%c' should have been escaped\n",

333 \*p);

334 goto out;

335 }

336

337 ++p;

338 }

339

340 ret = TRUE;

341

342 out:

343 if (!ret && error && !dbus_error_is_set (error))

344 \_DBUS_SET_OOM (error);

345

346 \_dbus_assert (ret \|\| error == NULL \|\| dbus_error_is_set (error));

347

348 return ret;

349}

350

367dbus_bool_t

368dbus_parse_address (const char \*address,

369 DBusAddressEntry \*\*\*entry_result,

370 int \*array_len,

371 DBusError \*error)

372{

373 DBusString str;

374 int pos, end_pos, len, i;

375 DBusList \*entries, \*link;

376 DBusAddressEntry \*\*entry_array;

377

378 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

379

380 \_dbus_string_init_const (&str, address);

381

382 entries = NULL;

383 pos = 0;

384 len = \_dbus_string_get_length (&str);

385

386 if (len == 0)

387 {

388 dbus_set_error (error, DBUS_ERROR_BAD_ADDRESS,

389 "Empty address '%s'", address);

390 goto error;

391 }

392

393 while (pos \< len)

394 {

395 DBusAddressEntry \*entry;

396

397 int found_pos;

398

399 entry = create_entry ();

400 if (!entry)

401 {

402 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

403

404 goto error;

405 }

406

407 /\* Append the entry \*/

408 if (!\_dbus_list_append (&entries, entry))

409 {

410 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

411 dbus_address_entry_free (entry);

412 goto error;

413 }

414

415 /\* Look for a semi-colon \*/

416 if (!\_dbus_string_find (&str, pos, ";", &end_pos))

417 end_pos = len;

418

419 /\* Look for the colon : \*/

420 if (!\_dbus_string_find_to (&str, pos, end_pos, ":", &found_pos))

421 {

422 dbus_set_error (error, DBUS_ERROR_BAD_ADDRESS, "Address does not contain a colon");

423 goto error;

424 }

425

426 if (!\_dbus_string_copy_len (&str, pos, found_pos - pos, &entry-\>method, 0))

427 {

428 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

429 goto error;

430 }

431

432 pos = found_pos + 1;

433

434 while (pos \< end_pos)

435 {

436 int comma_pos, equals_pos;

437

438 if (!\_dbus_string_find_to (&str, pos, end_pos, ",", &comma_pos))

439 comma_pos = end_pos;

440

441 if (!\_dbus_string_find_to (&str, pos, comma_pos, "=", &equals_pos) \|\|

442 equals_pos == pos \|\| equals_pos + 1 == comma_pos)

443 {

444 dbus_set_error (error, DBUS_ERROR_BAD_ADDRESS,

445 "'=' character not found or has no value following it");

446 goto error;

447 }

448 else

449 {

450 DBusString \*key;

451 DBusString \*value;

452

453 key = dbus_new0 (DBusString, 1);

454

455 if (!key)

456 {

457 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

458 goto error;

459 }

460

461 value = dbus_new0 (DBusString, 1);

462 if (!value)

463 {

464 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

465 dbus_free (key);

466 goto error;

467 }

468

469 if (!\_dbus_string_init (key))

470 {

471 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

472 dbus_free (key);

473 dbus_free (value);

474

475 goto error;

476 }

477

478 if (!\_dbus_string_init (value))

479 {

480 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

481 \_dbus_string_free (key);

482

483 dbus_free (key);

484 dbus_free (value);

485 goto error;

486 }

487

488 if (!\_dbus_string_copy_len (&str, pos, equals_pos - pos, key, 0))

489 {

490 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

491 \_dbus_string_free (key);

492 \_dbus_string_free (value);

493

494 dbus_free (key);

495 dbus_free (value);

496 goto error;

497 }

498

499 if (!append_unescaped_value (value, &str, equals_pos + 1,

500 comma_pos - equals_pos - 1, error))

501 {

502 \_dbus_assert (error == NULL \|\| dbus_error_is_set (error));

503 \_dbus_string_free (key);

504 \_dbus_string_free (value);

505

506 dbus_free (key);

507 dbus_free (value);

508 goto error;

509 }

510

511 if (!\_dbus_list_append (&entry-\>keys, key))

512 {

513 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

514 \_dbus_string_free (key);

515 \_dbus_string_free (value);

516

517 dbus_free (key);

518 dbus_free (value);

519 goto error;

520 }

521

522 if (!\_dbus_list_append (&entry-\>values, value))

523 {

524 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

525 \_dbus_string_free (value);

526

527 dbus_free (value);

528 goto error;

529 }

530 }

531

532 pos = comma_pos + 1;

533 }

534

535 pos = end_pos + 1;

536 }

537

538 \*array_len = \_dbus_list_get_length (&entries);

539

540 entry_array = dbus_new (DBusAddressEntry \*, \*array_len + 1);

541

542 if (!entry_array)

543 {

544 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

545

546 goto error;

547 }

548

549 entry_array \[\*array_len\] = NULL;

550

551 link = \_dbus_list_get_first_link (&entries);

552 i = 0;

553 while (link != NULL)

554 {

555 entry_array\[i\] = link-\>data;

556 i++;

557 link = \_dbus_list_get_next_link (&entries, link);

558 }

559

560 \_dbus_list_clear (&entries);

561 \*entry_result = entry_array;

562

563 return TRUE;

564

565 error:

566

567 link = \_dbus_list_get_first_link (&entries);

568 while (link != NULL)

569 {

570 dbus_address_entry_free (link-\>data);

571 link = \_dbus_list_get_next_link (&entries, link);

572 }

573

574 \_dbus_list_clear (&entries);

575

576 return FALSE;

577

578}

579

587char\*

588dbus_address_escape_value (const char \*value)

589{

590 DBusString escaped;

591 DBusString unescaped;

592 char \*ret;

593

594 ret = NULL;

595

596 \_dbus_string_init_const (&unescaped, value);

597

598 if (!\_dbus_string_init (&escaped))

599 return NULL;

600

601 if (!\_dbus_address_append_escaped (&escaped, &unescaped))

602 goto out;

603

604 if (!\_dbus_string_steal_data (&escaped, &ret))

605 goto out;

606

607 out:

608 \_dbus_string_free (&escaped);

609 return ret;

610}

611

621char\*

622dbus_address_unescape_value (const char \*value,

623 DBusError \*error)

624{

625 DBusString unescaped;

626 DBusString escaped;

627 char \*ret;

628

629 ret = NULL;

630

631 \_dbus_string_init_const (&escaped, value);

632

633 if (!\_dbus_string_init (&unescaped))

634 return NULL;

635

636 if (!append_unescaped_value (&unescaped, &escaped,

637 0, \_dbus_string_get_length (&escaped),

638 error))

639 goto out;

640

641 if (!\_dbus_string_steal_data (&unescaped, &ret))

642 goto out;

643

644 out:

645 if (ret == NULL && error && !dbus_error_is_set (error))

646 \_DBUS_SET_OOM (error);

647

648 \_dbus_assert (ret != NULL \|\| error == NULL \|\| dbus_error_is_set (error));

649

650 \_dbus_string_free (&unescaped);

651 return ret;

652}

653

/\* End of public API \*/

\_DBUS_ADDRESS_OPTIONALLY_ESCAPED_BYTE

\#define \_DBUS_ADDRESS_OPTIONALLY_ESCAPED_BYTE(b)

TRUE if the byte need not be escaped when found in a dbus address.

**Definition** dbus-address.c:89

\_dbus_address_append_escaped

dbus_bool_t \_dbus_address_append_escaped(DBusString \*escaped, const DBusString \*unescaped)

Appends an escaped version of one string to another string, using the D-Bus address escaping mechanis...

**Definition** dbus-address.c:109

\_dbus_set_bad_address

void \_dbus_set_bad_address(DBusError \*error, const char \*address_problem_type, const char \*address_problem_field, const char \*address_problem_other)

Sets DBUS_ERROR_BAD_ADDRESS.

**Definition** dbus-address.c:70

dbus_address_entries_free

void dbus_address_entries_free(DBusAddressEntry \*\*entries)

Frees a NULL-terminated array of address entries.

**Definition** dbus-address.c:194

dbus_parse_address

dbus_bool_t dbus_parse_address(const char \*address, DBusAddressEntry \*\*\*entry_result, int \*array_len, DBusError \*error)

Parses an address string of the form:

**Definition** dbus-address.c:368

dbus_address_entry_get_method

const char \* dbus_address_entry_get_method(DBusAddressEntry \*entry)

Returns the method string of an address entry.

**Definition** dbus-address.c:232

dbus_address_unescape_value

char \* dbus_address_unescape_value(const char \*value, DBusError \*error)

Unescapes the given string as a value in a key=value pair for a D-Bus address.

**Definition** dbus-address.c:622

dbus_address_escape_value

char \* dbus_address_escape_value(const char \*value)

Escapes the given string as a value in a key=value pair for a D-Bus address.

**Definition** dbus-address.c:588

dbus_address_entry_get_value

const char \* dbus_address_entry_get_value(DBusAddressEntry \*entry, const char \*key)

Returns a value from a key of an entry.

**Definition** dbus-address.c:249

dbus_set_error

void dbus_set_error(DBusError \*error, const char \*name, const char \*format,...)

Assigns an error name and message to a DBusError.

**Definition** dbus-errors.c:356

dbus_error_is_set

dbus_bool_t dbus_error_is_set(const DBusError \*error)

Checks whether an error occurred (the error is set).

**Definition** dbus-errors.c:331

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_dbus_list_get_first_link

DBusList \* \_dbus_list_get_first_link(DBusList \*\*list)

Gets the first link in the list.

**Definition** dbus-list.c:597

\_dbus_list_get_length

int \_dbus_list_get_length(DBusList \*\*list)

Gets the length of a list.

**Definition** dbus-list.c:760

\_dbus_list_clear

void \_dbus_list_clear(DBusList \*\*list)

Frees all links in the list and sets the list head to NULL.

**Definition** dbus-list.c:545

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

dbus_free

void dbus_free(void \*memory)

Frees a block of memory previously allocated by dbus_malloc() or dbus_malloc0().

**Definition** dbus-memory.c:710

dbus_new

\#define dbus_new(type, count)

Safe macro for using dbus_malloc().

**Definition** dbus-memory.h:59

dbus_new0

\#define dbus_new0(type, count)

Safe macro for using dbus_malloc0().

**Definition** dbus-memory.h:60

DBUS_ERROR_BAD_ADDRESS

\#define DBUS_ERROR_BAD_ADDRESS

A D-Bus bus address was malformed.

**Definition** dbus-protocol.h:373

DBUS_ERROR_NO_MEMORY

\#define DBUS_ERROR_NO_MEMORY

There was not enough memory to complete an operation.

**Definition** dbus-protocol.h:363

\_dbus_string_set_length

dbus_bool_t \_dbus_string_set_length(DBusString \*str, int length)

Sets the length of a string.

**Definition** dbus-string.c:847

\_dbus_string_hex_decode

dbus_bool_t \_dbus_string_hex_decode(const DBusString \*source, int start, int \*end_return, DBusString \*dest, int insert_at)

Decodes a string from hex encoding.

**Definition** dbus-string.c:2432

\_dbus_string_init

dbus_bool_t \_dbus_string_init(DBusString \*str)

Initializes a string.

**Definition** dbus-string.c:182

\_dbus_string_init_const

void \_dbus_string_init_const(DBusString \*str, const char \*value)

Initializes a constant string.

**Definition** dbus-string.c:197

\_dbus_string_steal_data

dbus_bool_t \_dbus_string_steal_data(DBusString \*str, char \*\*data_return)

Like \_dbus_string_get_data(), but removes the gotten data from the original string.

**Definition** dbus-string.c:686

\_dbus_string_find

dbus_bool_t \_dbus_string_find(const DBusString \*str, int start, const char \*substr, int \*found)

Finds the given substring in the string, returning TRUE and filling in the byte index where the subst...

**Definition** dbus-string.c:1666

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_string_equal_c_str

dbus_bool_t \_dbus_string_equal_c_str(const DBusString \*a, const char \*c_str)

Checks whether a string is equal to a C string.

**Definition** dbus-string.c:2214

\_dbus_string_get_length

int \_dbus_string_get_length(const DBusString \*str)

Gets the length of a string (not including nul termination).

**Definition** dbus-string.c:784

\_dbus_string_append_byte

dbus_bool_t \_dbus_string_append_byte(DBusString \*str, unsigned char byte)

Appends a single byte to the string, returning FALSE if not enough memory.

**Definition** dbus-string.c:1190

\_dbus_string_get_const_data

const char \* \_dbus_string_get_const_data(const DBusString \*str)

Gets the raw character buffer from a const string.

**Definition** dbus-string.c:513

\_dbus_string_append_byte_as_hex

dbus_bool_t \_dbus_string_append_byte_as_hex(DBusString \*str, unsigned char byte)

Appends a two-character hex digit to a string, where the hex digit has the value of the given byte.

**Definition** dbus-string.c:2313

\_dbus_string_find_to

dbus_bool_t \_dbus_string_find_to(const DBusString \*str, int start, int end, const char \*substr, int \*found)

Finds the given substring in the string, up to a certain position, returning TRUE and filling in the ...

**Definition** dbus-string.c:1759

\_dbus_string_copy_len

dbus_bool_t \_dbus_string_copy_len(const DBusString \*source, int start, int len, DBusString \*dest, int insert_at)

Like \_dbus_string_copy(), but can copy a segment from the middle of the source string.

**Definition** dbus-string.c:1437

DBusAddressEntry

Internals of DBusAddressEntry.

**Definition** dbus-address.c:49

DBusAddressEntry::method

DBusString method

The address type (unix, tcp, etc.)

**Definition** dbus-address.c:50

DBusAddressEntry::values

DBusList \* values

List of values.

**Definition** dbus-address.c:53

DBusAddressEntry::keys

DBusList \* keys

List of keys.

**Definition** dbus-address.c:52

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusList

A node in a linked list.

**Definition** dbus-list.h:37

DBusList::data

void \* data

Data stored at this element.

**Definition** dbus-list.h:40

DBusString

**Definition** dbus-string.h:47
