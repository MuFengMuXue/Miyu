dbus-shell.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-shell.c Shell command line utility functions.

3 \*

4 \* Copyright (C) 2002, 2003 Red Hat, Inc.

5 \* Copyright (C) 2003 CodeFactory AB

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

28\#include \<string.h\>

29\#include "dbus-internals.h"

30\#include "dbus-list.h"

31\#include "dbus-memory.h"

32\#include "dbus-protocol.h"

33\#include "dbus-shell.h"

34\#include "dbus-string.h"

35

36/\* Single quotes preserve the literal string exactly. escape

37 \* sequences are not allowed; not even \\ - if you want a '

38 \* in the quoted text, you have to do something like 'foo'\\'bar'

39 \*

40 \* Double quotes allow \$ \` " \\ and newline to be escaped with backslash.

41 \* Otherwise double quotes preserve things literally.

42 \*/

43

44static dbus_bool_t

45unquote_string_inplace (char\* str, char\*\* end)

46{

47 char\* dest;

48 char\* s;

49 char quote_char;

50

51 dest = s = str;

52

53 quote_char = \*s;

54

55 if (!(\*s == '"' \|\| \*s == '\\'))

56 {

57 \*end = str;

58 return FALSE;

59 }

60

61 /\* Skip the initial quote mark \*/

62 ++s;

63

64 if (quote_char == '"')

65 {

66 while (\*s)

67 {

68 \_dbus_assert(s \> dest); /\* loop invariant \*/

69

70 switch (\*s)

71 {

72 case '"':

73 /\* End of the string, return now \*/

74 \*dest = '\0';

75 ++s;

76 \*end = s;

77 return TRUE;

78

79 case '\\':

80 /\* Possible escaped quote or \\ \*/

81 ++s;

82 switch (\*s)

83 {

84 case '"':

85 case '\\':

86 case '\`':

87 case '\$':

88 case '\n':

89 \*dest = \*s;

90 ++s;

91 ++dest;

92 break;

93

94 default:

95 /\* not an escaped char \*/

96 \*dest = '\\';

97 ++dest;

98 /\* ++s already done. \*/

99 break;

100 }

101 break;

102

103 default:

104 \*dest = \*s;

105 ++dest;

106 ++s;

107 break;

108 }

109

110 \_dbus_assert(s \> dest); /\* loop invariant \*/

111 }

112 }

113 else

114 {

115 while (\*s)

116 {

117 \_dbus_assert(s \> dest); /\* loop invariant \*/

118

119 if (\*s == '\\')

120 {

121 /\* End of the string, return now \*/

122 \*dest = '\0';

123 ++s;

124 \*end = s;

125 return TRUE;

126 }

127 else

128 {

129 \*dest = \*s;

130 ++dest;

131 ++s;

132 }

133

134 \_dbus_assert(s \> dest); /\* loop invariant \*/

135 }

136 }

137

138 /\* If we reach here this means the close quote was never encountered \*/

139

140 \*dest = '\0';

141

142 \*end = s;

143 return FALSE;

144}

145

170char\*

171\_dbus_shell_unquote (const char \*quoted_string)

172{

173 char \*unquoted;

174 char \*end;

175 char \*start;

176 char \*ret;

177 DBusString retval;

178

179 unquoted = \_dbus_strdup (quoted_string);

180 if (unquoted == NULL)

181 return NULL;

182

183 start = unquoted;

184 end = unquoted;

185 if (!\_dbus_string_init (&retval))

186 {

187 dbus_free (unquoted);

188 return NULL;

189 }

190

191 /\* The loop allows cases such as

192 \* "foo"blah blah'bar'woo foo"baz"la la la\\\\'foo'

193 \*/

194 while (\*start)

195 {

196 /\* Append all non-quoted chars, honoring backslash escape

197 \*/

198

199 while (\*start && !(\*start == '"' \|\| \*start == '\\'))

200 {

201 if (\*start == '\\')

202 {

203 /\* all characters can get escaped by backslash,

204 \* except newline, which is removed if it follows

205 \* a backslash outside of quotes

206 \*/

207

208 ++start;

209 if (\*start)

210 {

211 if (\*start != '\n')

212 {

213 if (!\_dbus_string_append_byte (&retval, \*start))

214 goto error;

215 }

216 ++start;

217 }

218 }

219 else

220 {

221 if (!\_dbus_string_append_byte (&retval, \*start))

222 goto error;

223 ++start;

224 }

225 }

226

227 if (\*start)

228 {

229 if (!unquote_string_inplace (start, &end))

230 goto error;

231 else

232 {

233 if (!\_dbus_string_append (&retval, start))

234 goto error;

235 start = end;

236 }

237 }

238 }

239

240 ret = \_dbus_strdup (\_dbus_string_get_data (&retval));

241 if (!ret)

242 goto error;

243

244 dbus_free (unquoted);

245 \_dbus_string_free (&retval);

246

247 return ret;

248

249 error:

250 dbus_free (unquoted);

251 \_dbus_string_free (&retval);

252 return NULL;

253}

254

255/\* \_dbus_shell_parse_argv() does a semi-arbitrary weird subset of the way

256 \* the shell parses a command line. We don't do variable expansion,

257 \* don't understand that operators are tokens, don't do tilde expansion,

258 \* don't do command substitution, no arithmetic expansion, IFS gets ignored,

259 \* don't do filename globs, don't remove redirection stuff, etc.

260 \*

261 \* READ THE UNIX98 SPEC on "Shell Command Language" before changing

262 \* the behavior of this code.

263 \*

264 \* Steps to parsing the argv string:

265 \*

266 \* - tokenize the string (but since we ignore operators,

267 \* our tokenization may diverge from what the shell would do)

268 \* note that tokenization ignores the internals of a quoted

269 \* word and it always splits on spaces, not on IFS even

270 \* if we used IFS. We also ignore "end of input indicator"

271 \* (I guess this is control-D?)

272 \*

273 \* Tokenization steps, from UNIX98 with operator stuff removed,

274 \* are:

275 \*

276 \* 1) "If the current character is backslash, single-quote or

277 \* double-quote (\\ ' or ") and it is not quoted, it will affect

278 \* quoting for subsequent characters up to the end of the quoted

279 \* text. The rules for quoting are as described in Quoting

280 \* . During token recognition no substitutions will be actually

281 \* performed, and the result token will contain exactly the

282 \* characters that appear in the input (except for newline

283 \* character joining), unmodified, including any embedded or

284 \* enclosing quotes or substitution operators, between the quote

285 \* mark and the end of the quoted text. The token will not be

286 \* delimited by the end of the quoted field."

287 \*

288 \* 2) "If the current character is an unquoted newline character,

289 \* the current token will be delimited."

290 \*

291 \* 3) "If the current character is an unquoted blank character, any

292 \* token containing the previous character is delimited and the

293 \* current character will be discarded."

294 \*

295 \* 4) "If the previous character was part of a word, the current

296 \* character will be appended to that word."

297 \*

298 \* 5) "If the current character is a "#", it and all subsequent

299 \* characters up to, but excluding, the next newline character

300 \* will be discarded as a comment. The newline character that

301 \* ends the line is not considered part of the comment. The

302 \* "#" starts a comment only when it is at the beginning of a

303 \* token. Since the search for the end-of-comment does not

304 \* consider an escaped newline character specially, a comment

305 \* cannot be continued to the next line."

306 \*

307 \* 6) "The current character will be used as the start of a new word."

308 \*

309 \*

310 \* - for each token (word), perform portions of word expansion, namely

311 \* field splitting (using default whitespace IFS) and quote

312 \* removal. Field splitting may increase the number of words.

313 \* Quote removal does not increase the number of words.

314 \*

315 \* "If the complete expansion appropriate for a word results in an

316 \* empty field, that empty field will be deleted from the list of

317 \* fields that form the completely expanded command, unless the

318 \* original word contained single-quote or double-quote characters."

319 \* - UNIX98 spec

320 \*

321 \*

322 \*/

323

324static dbus_bool_t

325delimit_token (DBusString \*token,

326 DBusList \*\*retval,

327 DBusError \*error)

328{

329 char \*str;

330

331 str = \_dbus_strdup (\_dbus_string_get_data (token));

332 if (!str)

333 {

334 \_DBUS_SET_OOM (error);

335 return FALSE;

336 }

337

338 if (!\_dbus_list_append (retval, str))

339 {

340 dbus_free (str);

341 \_DBUS_SET_OOM (error);

342 return FALSE;

343 }

344

345 return TRUE;

346}

347

348static DBusList\*

349tokenize_command_line (const char \*command_line, DBusError \*error)

350{

351 char current_quote;

352 const char \*p;

353 DBusString current_token;

354 DBusList \*retval = NULL;

355 dbus_bool_t quoted;;

356

357 current_quote = '\0';

358 quoted = FALSE;

359 p = command_line;

360

361 if (!\_dbus_string_init (&current_token))

362 {

363 \_DBUS_SET_OOM (error);

364 return NULL;

365 }

366

367 while (\*p)

368 {

369 if (current_quote == '\\')

370 {

371 if (\*p == '\n')

372 {

373 /\* we append nothing; backslash-newline become nothing \*/

374 }

375 else

376 {

377 if (!\_dbus_string_append_byte (&current_token, '\\') \|\|

378 !\_dbus_string_append_byte (&current_token, \*p))

379 {

380 \_DBUS_SET_OOM (error);

381 goto error;

382 }

383 }

384

385 current_quote = '\0';

386 }

387 else if (current_quote == '#')

388 {

389 /\* Discard up to and including next newline \*/

390 while (\*p && \*p != '\n')

391 ++p;

392

393 current_quote = '\0';

394

395 if (\*p == '\0')

396 break;

397 }

398 else if (current_quote)

399 {

400 if (\*p == current_quote &&

401 /\* check that it isn't an escaped double quote \*/

402 !(current_quote == '"' && quoted))

403 {

404 /\* close the quote \*/

405 current_quote = '\0';

406 }

407

408 /\* Everything inside quotes, and the close quote,

409 \* gets appended literally.

410 \*/

411

412 if (!\_dbus_string_append_byte (&current_token, \*p))

413 {

414 \_DBUS_SET_OOM (error);

415 goto error;

416 }

417 }

418 else

419 {

420 switch (\*p)

421 {

422 case '\n':

423 if (!delimit_token (&current_token, &retval, error))

424 goto error;

425

426 \_dbus_string_free (&current_token);

427

428 if (!\_dbus_string_init (&current_token))

429 {

430 \_DBUS_SET_OOM (error);

431 goto init_error;

432 }

433

434 break;

435

436 case ' ':

437 case '\t':

438 /\* If the current token contains the previous char, delimit

439 \* the current token. A nonzero length

440 \* token should always contain the previous char.

441 \*/

442 if (\_dbus_string_get_length (&current_token) \> 0)

443 {

444 if (!delimit_token (&current_token, &retval, error))

445 goto error;

446

447 \_dbus_string_free (&current_token);

448

449 if (!\_dbus_string_init (&current_token))

450 {

451 \_DBUS_SET_OOM (error);

452 goto init_error;

453 }

454

455 }

456

457 /\* discard all unquoted blanks (don't add them to a token) \*/

458 break;

459

460

461 /\* single/double quotes are appended to the token,

462 \* escapes are maybe appended next time through the loop,

463 \* comment chars are never appended.

464 \*/

465

466 case '\\':

467 case '"':

468 if (!\_dbus_string_append_byte (&current_token, \*p))

469 {

470 \_DBUS_SET_OOM (error);

471 goto error;

472 }

473

474 /\* FALL THRU \*/

475

476 case '#':

477 case '\\':

478 current_quote = \*p;

479 break;

480

481 default:

482 /\* Combines rules 4) and 6) - if we have a token, append to it,

483 \* otherwise create a new token.

484 \*/

485 if (!\_dbus_string_append_byte (&current_token, \*p))

486 {

487 \_DBUS_SET_OOM (error);

488 goto error;

489 }

490 break;

491 }

492 }

493

494 /\* We need to count consecutive backslashes mod 2,

495 \* to detect escaped doublequotes.

496 \*/

497 if (\*p != '\\')

498 quoted = FALSE;

499 else

500 quoted = !quoted;

501

502 ++p;

503 }

504

505 if (!delimit_token (&current_token, &retval, error))

506 goto error;

507

508 if (current_quote)

509 {

510 dbus_set_error_const (error, DBUS_ERROR_INVALID_ARGS, "Unclosed quotes in command line");

511 goto error;

512 }

513

514 if (retval == NULL)

515 {

516 dbus_set_error_const (error, DBUS_ERROR_INVALID_ARGS, "No tokens found in command line");

517 goto error;

518 }

519

520 \_dbus_string_free (&current_token);

521

522 return retval;

523

524 error:

525 \_dbus_string_free (&current_token);

526

527 init_error:

528 \_dbus_list_clear_full (&retval, dbus_free);

529 return NULL;

530}

531

549dbus_bool_t

550\_dbus_shell_parse_argv (const char \*command_line,

551 int \*argcp,

552 char \*\*\*argvp,

553 DBusError \*error)

554{

555 /\* Code based on poptParseArgvString() from libpopt \*/

556 int argc = 0;

557 char \*\*argv = NULL;

558 DBusList \*tokens = NULL;

559 int i;

560 DBusList \*tmp_list;

561

562 if (!command_line)

563 {

564 \_dbus_verbose ("Command line is NULL\n");

565 return FALSE;

566 }

567

568 tokens = tokenize_command_line (command_line, error);

569 if (tokens == NULL)

570 {

571 \_dbus_verbose ("No tokens for command line '%s'\n", command_line);

572 return FALSE;

573 }

574

575 /\* Because we can't have introduced any new blank space into the

576 \* tokens (we didn't do any new expansions), we don't need to

577 \* perform field splitting. If we were going to honor IFS or do any

578 \* expansions, we would have to do field splitting on each word

579 \* here. Also, if we were going to do any expansion we would need to

580 \* remove any zero-length words that didn't contain quotes

581 \* originally; but since there's no expansion we know all words have

582 \* nonzero length, unless they contain quotes.

583 \*

584 \* So, we simply remove quotes, and don't do any field splitting or

585 \* empty word removal, since we know there was no way to introduce

586 \* such things.

587 \*/

588

589 argc = \_dbus_list_get_length (&tokens);

590 argv = dbus_new (char \*, argc + 1);

591 if (!argv)

592 {

593 \_DBUS_SET_OOM (error);

594 goto error;

595 }

596

597 i = 0;

598 tmp_list = tokens;

599 while (tmp_list)

600 {

601 argv\[i\] = \_dbus_shell_unquote (tmp_list-\>data);

602

603 if (!argv\[i\])

604 {

605 int j;

606 for (j = 0; j \< i; j++)

607 dbus_free(argv\[j\]);

608

609 dbus_free (argv);

610 \_DBUS_SET_OOM (error);

611 goto error;

612 }

613

614 tmp_list = \_dbus_list_get_next_link (&tokens, tmp_list);

615 ++i;

616 }

617 argv\[argc\] = NULL;

618

619 \_dbus_list_clear_full (&tokens, dbus_free);

620

621 if (argcp)

622 \*argcp = argc;

623

624 if (argvp)

625 \*argvp = argv;

626 else

627 dbus_free_string_array (argv);

628

629 return TRUE;

630

631 error:

632 \_dbus_list_clear_full (&tokens, dbus_free);

633

634 return FALSE;

635

636}

dbus_set_error_const

void dbus_set_error_const(DBusError \*error, const char \*name, const char \*message)

Assigns an error name and message to a DBusError.

**Definition** dbus-errors.c:245

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_dbus_strdup

char \* \_dbus_strdup(const char \*str)

Duplicates a string.

**Definition** dbus-internals.c:621

\_dbus_list_clear_full

void \_dbus_list_clear_full(DBusList \*\*list, DBusFreeFunction function)

Free every link and every element in the list.

**Definition** dbus-list.c:570

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

dbus_free

void dbus_free(void \*memory)

Frees a block of memory previously allocated by dbus_malloc() or dbus_malloc0().

**Definition** dbus-memory.c:710

dbus_new

\#define dbus_new(type, count)

Safe macro for using dbus_malloc().

**Definition** dbus-memory.h:59

dbus_free_string_array

void dbus_free_string_array(char \*\*str_array)

Frees a NULL-terminated array of strings.

**Definition** dbus-memory.c:758

DBUS_ERROR_INVALID_ARGS

\#define DBUS_ERROR_INVALID_ARGS

Invalid arguments passed to a method call.

**Definition** dbus-protocol.h:397

\_dbus_string_append

dbus_bool_t \_dbus_string_append(DBusString \*str, const char \*buffer)

Appends a nul-terminated C-style string to a DBusString.

**Definition** dbus-string.c:980

\_dbus_string_init

dbus_bool_t \_dbus_string_init(DBusString \*str)

Initializes a string.

**Definition** dbus-string.c:182

\_dbus_string_get_data

char \* \_dbus_string_get_data(DBusString \*str)

Gets the raw character buffer from the string.

**Definition** dbus-string.c:496

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_string_get_length

int \_dbus_string_get_length(const DBusString \*str)

Gets the length of a string (not including nul termination).

**Definition** dbus-string.c:784

\_dbus_string_append_byte

dbus_bool_t \_dbus_string_append_byte(DBusString \*str, unsigned char byte)

Appends a single byte to the string, returning FALSE if not enough memory.

**Definition** dbus-string.c:1190

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
