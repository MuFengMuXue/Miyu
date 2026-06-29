dbus-keyring.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-keyring.c Store secret cookies in your homedir

3 \*

4 \* Copyright (C) 2003, 2004 Red Hat Inc.

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

27\#include "dbus-keyring.h"

28\#include "dbus-protocol.h"

29\#include \<dbus/dbus-string.h\>

30\#include \<dbus/dbus-list.h\>

31\#include \<dbus/dbus-sysdeps.h\>

32\#include \<dbus/dbus-test-tap.h\>

33

70\#define NEW_KEY_TIMEOUT_SECONDS (60\*5)

76\#define EXPIRE_KEYS_TIMEOUT_SECONDS (NEW_KEY_TIMEOUT_SECONDS + (60\*2))

80\#define MAX_TIME_TRAVEL_SECONDS (60\*5)

81

86\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

87\#define MAX_KEYS_IN_FILE 10

88\#else

89\#define MAX_KEYS_IN_FILE 256

90\#endif

91

95typedef struct

96{

97 dbus_int32_t id;

99 dbus_int64_t creation_time;

101 DBusString secret;

103} DBusKey;

104

111struct DBusKeyring

112{

113 int refcount;

114 DBusString directory;

115 DBusString filename;

116 DBusString filename_lock;

117 DBusKey \*keys;

118 int n_keys;

119 DBusCredentials \*credentials;

120};

121

122static DBusKeyring\*

123\_dbus_keyring_new (void)

124{

125 DBusKeyring \*keyring;

126

127 keyring = dbus_new0 (DBusKeyring, 1);

128 if (keyring == NULL)

129 goto out_0;

130

131 if (!\_dbus_string_init (&keyring-\>directory))

132 goto out_1;

133

134 if (!\_dbus_string_init (&keyring-\>filename))

135 goto out_2;

136

137 if (!\_dbus_string_init (&keyring-\>filename_lock))

138 goto out_3;

139

140 keyring-\>refcount = 1;

141 keyring-\>keys = NULL;

142 keyring-\>n_keys = 0;

143

144 return keyring;

145

146 out_3:

147 \_dbus_string_free (&keyring-\>filename);

148 out_2:

149 \_dbus_string_free (&keyring-\>directory);

150 out_1:

151 dbus_free (keyring);

152 out_0:

153 return NULL;

154}

155

156static void

157free_keys (DBusKey \*keys,

158 int n_keys)

159{

160 int i;

161

162 /\* should be safe for args NULL, 0 \*/

163

164 i = 0;

165 while (i \< n_keys)

166 {

167 \_dbus_string_free (&keys\[i\].secret);

168 ++i;

169 }

170

171 dbus_free (keys);

172}

173

174/\* Our locking scheme is highly unreliable. However, there is

175 \* unfortunately no reliable locking scheme in user home directories;

176 \* between bugs in Linux NFS, people using Tru64 or other total crap

177 \* NFS, AFS, random-file-system-of-the-week, and so forth, fcntl() in

178 \* homedirs simply generates tons of bug reports. This has been

179 \* learned through hard experience with GConf, unfortunately.

180 \*

181 \* This bad hack might work better for the kind of lock we have here,

182 \* which we don't expect to hold for any length of time. Crashing

183 \* while we hold it should be unlikely, and timing out such that we

184 \* delete a stale lock should also be unlikely except when the

185 \* filesystem is running really slowly. Stuff might break in corner

186 \* cases but as long as it's not a security-level breakage it should

187 \* be OK.

188 \*/

189

191\#define MAX_LOCK_TIMEOUTS 32

193\#define LOCK_TIMEOUT_MILLISECONDS 250

194

195static dbus_bool_t

196\_dbus_keyring_lock (DBusKeyring \*keyring)

197{

198 int n_timeouts;

199

200 n_timeouts = 0;

201 while (n_timeouts \< MAX_LOCK_TIMEOUTS)

202 {

203 DBusError error = DBUS_ERROR_INIT;

204

205 if (\_dbus_create_file_exclusively (&keyring-\>filename_lock,

206 &error))

207 break;

208

209 \_dbus_verbose ("Did not get lock file, sleeping %d milliseconds (%s)\n",

210 LOCK_TIMEOUT_MILLISECONDS, error.message);

211 dbus_error_free (&error);

212

213 \_dbus_sleep_milliseconds (LOCK_TIMEOUT_MILLISECONDS);

214

215 ++n_timeouts;

216 }

217

218 if (n_timeouts == MAX_LOCK_TIMEOUTS)

219 {

220 DBusError error = DBUS_ERROR_INIT;

221

222 \_dbus_verbose ("Lock file timed out %d times, assuming stale\n",

223 n_timeouts);

224

225 if (!\_dbus_delete_file (&keyring-\>filename_lock, &error))

226 {

227 \_dbus_verbose ("Couldn't delete old lock file: %s\n",

228 error.message);

229 dbus_error_free (&error);

230 return FALSE;

231 }

232

233 if (!\_dbus_create_file_exclusively (&keyring-\>filename_lock,

234 &error))

235 {

236 \_dbus_verbose ("Couldn't create lock file after deleting stale one: %s\n",

237 error.message);

238 dbus_error_free (&error);

239 return FALSE;

240 }

241 }

242

243 return TRUE;

244}

245

246static void

247\_dbus_keyring_unlock (DBusKeyring \*keyring)

248{

249 DBusError error = DBUS_ERROR_INIT;

250

251 if (!\_dbus_delete_file (&keyring-\>filename_lock, &error))

252 {

253 \_dbus_warn ("Failed to delete lock file: %s",

254 error.message);

255 dbus_error_free (&error);

256 }

257}

258

259static DBusKey\*

260find_key_by_id (DBusKey \*keys,

261 int n_keys,

262 int id)

263{

264 int i;

265

266 i = 0;

267 while (i \< n_keys)

268 {

269 if (keys\[i\].id == id)

270 return &keys\[i\];

271

272 ++i;

273 }

274

275 return NULL;

276}

277

278static dbus_bool_t

279add_new_key (DBusKey \*\*keys_p,

280 int \*n_keys_p,

281 DBusError \*error)

282{

283 DBusKey \*new;

284 DBusString bytes;

285 int id;

286 dbus_int64_t timestamp;

287 const unsigned char \*s;

288 dbus_bool_t retval;

289 DBusKey \*keys;

290 int n_keys;

291

292 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

293

294 if (!\_dbus_string_init (&bytes))

295 {

296 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

297 return FALSE;

298 }

299

300 keys = \*keys_p;

301 n_keys = \*n_keys_p;

302 retval = FALSE;

303

304 /\* Generate an integer ID and then the actual key. \*/

305 retry:

306

307 if (!\_dbus_generate_random_bytes (&bytes, 4, error))

308 goto out;

309

310 s = (const unsigned char\*) \_dbus_string_get_const_data (&bytes);

311

312 id = s\[0\] \| (s\[1\] \<\< 8) \| (s\[2\] \<\< 16) \| ((s\[3\] & 0x7f) \<\< 24);

313 \_dbus_assert (id \>= 0);

314

315 if (find_key_by_id (keys, n_keys, id) != NULL)

316 {

317 \_dbus_string_set_length (&bytes, 0);

318 \_dbus_verbose ("Key ID %d already existed, trying another one\n",

319 id);

320 goto retry;

321 }

322

323 \_dbus_verbose ("Creating key with ID %d\n", id);

324

325\#define KEY_LENGTH_BYTES 24

326 \_dbus_string_set_length (&bytes, 0);

327 if (!\_dbus_generate_random_bytes (&bytes, KEY_LENGTH_BYTES, error))

328 {

329 goto out;

330 }

331

332 new = dbus_realloc (keys, sizeof (DBusKey) \* (n_keys + 1));

333 if (new == NULL)

334 {

335 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

336 goto out;

337 }

338

339 keys = new;

340 \*keys_p = keys; /\* otherwise \*keys_p ends up invalid \*/

341 n_keys += 1;

342

343 if (!\_dbus_string_init (&keys\[n_keys-1\].secret))

344 {

345 n_keys -= 1; /\* we don't want to free the one we didn't init \*/

346 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

347 goto out;

348 }

349

350 \_dbus_get_real_time (&timestamp, NULL);

351

352 keys\[n_keys-1\].id = id;

353 keys\[n_keys-1\].creation_time = timestamp;

354 if (!\_dbus_string_move (&bytes, 0,

355 &keys\[n_keys-1\].secret,

356 0))

357 {

358 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

359 \_dbus_string_free (&keys\[n_keys-1\].secret);

360 n_keys -= 1;

361 goto out;

362 }

363

364 retval = TRUE;

365

366 out:

367 \*n_keys_p = n_keys;

368

369 \_dbus_string_free (&bytes);

370 return retval;

371}

372

387static dbus_bool_t

388\_dbus_keyring_reload (DBusKeyring \*keyring,

389 dbus_bool_t add_new,

390 DBusError \*error)

391{

392 DBusString contents;

393 DBusString line;

394 dbus_bool_t retval;

395 dbus_bool_t have_lock;

396 DBusKey \*keys;

397 int n_keys;

398 int i;

399 dbus_int64_t now;

400 DBusError tmp_error;

401

402 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

403

404 if (!\_dbus_check_dir_is_private_to_user (&keyring-\>directory, error))

405 return FALSE;

406

407 if (!\_dbus_string_init (&contents))

408 {

409 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

410 return FALSE;

411 }

412

413 if (!\_dbus_string_init (&line))

414 {

415 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

416 \_dbus_string_free (&contents);

417 return FALSE;

418 }

419

420 keys = NULL;

421 n_keys = 0;

422 retval = FALSE;

423 have_lock = FALSE;

424

425 \_dbus_get_real_time (&now, NULL);

426

427 if (add_new)

428 {

429 if (!\_dbus_keyring_lock (keyring))

430 {

431 dbus_set_error (error, DBUS_ERROR_FAILED,

432 "Could not lock keyring file to add to it");

433 goto out;

434 }

435

436 have_lock = TRUE;

437 }

438

439 dbus_error_init (&tmp_error);

440 if (!\_dbus_file_get_contents (&contents,

441 &keyring-\>filename,

442 &tmp_error))

443 {

444 \_dbus_verbose ("Failed to load keyring file: %s\n",

445 tmp_error.message);

446 /\* continue with empty keyring file, so we recreate it \*/

447 dbus_error_free (&tmp_error);

448 }

449

450 if (!\_dbus_string_validate_ascii (&contents, 0,

451 \_dbus_string_get_length (&contents)))

452 {

453 \_dbus_warn ("Secret keyring file contains non-ASCII! Ignoring existing contents");

454 \_dbus_string_set_length (&contents, 0);

455 }

456

457 /\* FIXME this is badly inefficient for large keyring files

458 \* (not that large keyring files exist outside of test suites)

459 \*/

460 while (\_dbus_string_pop_line (&contents, &line))

461 {

462 int next;

463 long val;

464 int id;

465 dbus_int64_t timestamp;

466 int len;

467 int end;

468 DBusKey \*new;

469

470 /\* Don't load more than the max. \*/

471 if (n_keys \>= (add_new ? MAX_KEYS_IN_FILE - 1 : MAX_KEYS_IN_FILE))

472 break;

473

474 next = 0;

475 if (!\_dbus_string_parse_int (&line, 0, &val, &next))

476 {

477 \_dbus_verbose ("could not parse secret key ID at start of line\n");

478 continue;

479 }

480

481 if (val \> \_DBUS_INT32_MAX \|\| val \< 0)

482 {

483 \_dbus_verbose ("invalid secret key ID at start of line\n");

484 continue;

485 }

486

487 id = val;

488

489 \_dbus_string_skip_blank (&line, next, &next);

490

491 if (!\_dbus_string_parse_int64 (&line, next, &timestamp, &next))

492 {

493 \_dbus_verbose ("could not parse secret key timestamp\n");

494 continue;

495 }

496

497 if (timestamp \< 0 \|\|

498 (now + MAX_TIME_TRAVEL_SECONDS) \< timestamp \|\|

499 (now - EXPIRE_KEYS_TIMEOUT_SECONDS) \> timestamp)

500 {

501 \_dbus_verbose ("dropping/ignoring %" DBUS_INT64_MODIFIER "d-seconds old key with timestamp %" DBUS_INT64_MODIFIER "d as current time is %" DBUS_INT64_MODIFIER "d\n",

502 now - timestamp, timestamp, now);

503 continue;

504 }

505

506 \_dbus_string_skip_blank (&line, next, &next);

507

508 len = \_dbus_string_get_length (&line);

509

510 if ((len - next) == 0)

511 {

512 \_dbus_verbose ("no secret key after ID and timestamp\n");

513 continue;

514 }

515

516 /\* We have all three parts \*/

517 new = dbus_realloc (keys, sizeof (DBusKey) \* (n_keys + 1));

518 if (new == NULL)

519 {

520 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

521 goto out;

522 }

523

524 keys = new;

525 n_keys += 1;

526

527 if (!\_dbus_string_init (&keys\[n_keys-1\].secret))

528 {

529 n_keys -= 1; /\* we don't want to free the one we didn't init \*/

530 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

531 goto out;

532 }

533

534 keys\[n_keys-1\].id = id;

535 keys\[n_keys-1\].creation_time = timestamp;

536 if (!\_dbus_string_hex_decode (&line, next, &end,

537 &keys\[n_keys-1\].secret, 0))

538 {

539 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

540 goto out;

541 }

542

543 if (\_dbus_string_get_length (&line) != end)

544 {

545 \_dbus_verbose ("invalid hex encoding in keyring file\n");

546 \_dbus_string_free (&keys\[n_keys - 1\].secret);

547 n_keys -= 1;

548 continue;

549 }

550 }

551

552 \_dbus_verbose ("Successfully loaded %d existing keys\n",

553 n_keys);

554

555 if (add_new)

556 {

557 if (!add_new_key (&keys, &n_keys, error))

558 {

559 \_dbus_verbose ("Failed to generate new key: %s\n",

560 error ? error-\>message : "(unknown)");

561 goto out;

562 }

563

564 \_dbus_string_set_length (&contents, 0);

565

566 i = 0;

567 while (i \< n_keys)

568 {

569 if (!\_dbus_string_append_printf (&contents, "%d %" DBUS_INT64_MODIFIER "d ",

570 keys\[i\].id, keys\[i\].creation_time))

571 goto nomem;

572

573 if (!\_dbus_string_hex_encode (&keys\[i\].secret, 0,

574 &contents,

575 \_dbus_string_get_length (&contents)))

576 goto nomem;

577

578 if (!\_dbus_string_append_byte (&contents, '\n'))

579 goto nomem;

580

581 ++i;

582 continue;

583

584 nomem:

585 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

586 goto out;

587 }

588

589 if (!\_dbus_string_save_to_file (&contents, &keyring-\>filename,

590 FALSE, error))

591 goto out;

592 }

593

594 if (keyring-\>keys)

595 free_keys (keyring-\>keys, keyring-\>n_keys);

596 keyring-\>keys = keys;

597 keyring-\>n_keys = n_keys;

598 keys = NULL;

599 n_keys = 0;

600

601 retval = TRUE;

602

603 out:

604 if (have_lock)

605 \_dbus_keyring_unlock (keyring);

606

607 if (! ((retval == TRUE && (error == NULL \|\| error-\>name == NULL)) \|\|

608 (retval == FALSE && (error == NULL \|\| error-\>name != NULL))))

609 {

610 if (error && error-\>name)

611 \_dbus_verbose ("error is %s: %s\n", error-\>name, error-\>message);

612 \_dbus_warn ("returning %d but error pointer %p name %s",

613 retval, error, error-\>name ? error-\>name : "(none)");

614 \_dbus_assert_not_reached ("didn't handle errors properly");

615 }

616

617 if (keys != NULL)

618 {

619 i = 0;

620 while (i \< n_keys)

621 {

622 \_dbus_string_zero (&keys\[i\].secret);

623 \_dbus_string_free (&keys\[i\].secret);

624 ++i;

625 }

626

627 dbus_free (keys);

628 }

629

630 \_dbus_string_free (&contents);

631 \_dbus_string_free (&line);

632

633 return retval;

634}

635

/\* end of internals \*/

637

650DBusKeyring \*

651\_dbus_keyring_ref (DBusKeyring \*keyring)

652{

653 keyring-\>refcount += 1;

654

655 return keyring;

656}

657

664void

665\_dbus_keyring_unref (DBusKeyring \*keyring)

666{

667 keyring-\>refcount -= 1;

668

669 if (keyring-\>refcount == 0)

670 {

671 if (keyring-\>credentials)

672 \_dbus_credentials_unref (keyring-\>credentials);

673

674 \_dbus_string_free (&keyring-\>filename);

675 \_dbus_string_free (&keyring-\>filename_lock);

676 \_dbus_string_free (&keyring-\>directory);

677 free_keys (keyring-\>keys, keyring-\>n_keys);

678 dbus_free (keyring);

679 }

680}

681

692DBusKeyring\*

693\_dbus_keyring_new_for_credentials (DBusCredentials \*credentials,

694 const DBusString \*context,

695 DBusError \*error)

696{

697 DBusString ringdir;

698 DBusKeyring \*keyring;

699 dbus_bool_t error_set;

700 DBusError tmp_error;

701 DBusCredentials \*our_credentials;

702

703 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

704

705 if (\_dbus_check_setuid ())

706 {

707 dbus_set_error_const (error, DBUS_ERROR_NOT_SUPPORTED,

708 "Unable to create DBus keyring when setuid");

709 return NULL;

710 }

711

712 keyring = NULL;

713 error_set = FALSE;

714 our_credentials = NULL;

715

716 if (!\_dbus_string_init (&ringdir))

717 {

718 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

719 return NULL;

720 }

721

722 if (credentials != NULL)

723 {

724 our_credentials = \_dbus_credentials_copy (credentials);

725 }

726 else

727 {

728 our_credentials = \_dbus_credentials_new_from_current_process ();

729 }

730

731 if (our_credentials == NULL)

732 goto failed;

733

734 if (\_dbus_credentials_are_anonymous (our_credentials))

735 {

736 if (!\_dbus_credentials_add_from_current_process (our_credentials))

737 goto failed;

738 }

739

740 if (!\_dbus_append_keyring_directory_for_credentials (&ringdir,

741 our_credentials))

742 goto failed;

743

744 keyring = \_dbus_keyring_new ();

745 if (keyring == NULL)

746 goto failed;

747

748 \_dbus_assert (keyring-\>credentials == NULL);

749 keyring-\>credentials = our_credentials;

750 our_credentials = NULL; /\* so we don't unref it again later \*/

751

752 /\* should have been validated already, but paranoia check here \*/

753 if (!\_dbus_keyring_validate_context (context))

754 {

755 error_set = TRUE;

756 dbus_set_error_const (error,

757 DBUS_ERROR_FAILED,

758 "Invalid context in keyring creation");

759 goto failed;

760 }

761

762 /\* Save keyring dir in the keyring object \*/

763 if (!\_dbus_string_copy (&ringdir, 0,

764 &keyring-\>directory, 0))

765 goto failed;

766

767 /\* Create keyring-\>filename based on keyring dir and context \*/

768 if (!\_dbus_string_copy (&keyring-\>directory, 0,

769 &keyring-\>filename, 0))

770 goto failed;

771

772 if (!\_dbus_concat_dir_and_file (&keyring-\>filename,

773 context))

774 goto failed;

775

776 /\* Create lockfile name \*/

777 if (!\_dbus_string_copy (&keyring-\>filename, 0,

778 &keyring-\>filename_lock, 0))

779 goto failed;

780

781 if (!\_dbus_string_append (&keyring-\>filename_lock, ".lock"))

782 goto failed;

783

784 /\* Reload keyring \*/

785 dbus_error_init (&tmp_error);

786 if (!\_dbus_keyring_reload (keyring, FALSE, &tmp_error))

787 {

788 \_dbus_verbose ("didn't load an existing keyring: %s\n",

789 tmp_error.message);

790 dbus_error_free (&tmp_error);

791 }

792

793 /\* We don't fail fatally if we can't create the directory,

794 \* but the keyring will probably always be empty

795 \* unless someone else manages to create it

796 \*/

797 dbus_error_init (&tmp_error);

798 if (!\_dbus_ensure_directory (&keyring-\>directory,

799 &tmp_error))

800 {

801 \_dbus_verbose ("Creating keyring directory: %s\n",

802 tmp_error.message);

803 dbus_error_free (&tmp_error);

804 }

805

806 \_dbus_string_free (&ringdir);

807

808 return keyring;

809

810 failed:

811 if (!error_set)

812 dbus_set_error_const (error,

813 DBUS_ERROR_NO_MEMORY,

814 NULL);

815 if (our_credentials)

816 \_dbus_credentials_unref (our_credentials);

817 if (keyring)

818 \_dbus_keyring_unref (keyring);

819 \_dbus_string_free (&ringdir);

820 return NULL;

821

822}

823

836dbus_bool_t

837\_dbus_keyring_validate_context (const DBusString \*context)

838{

839 if (\_dbus_string_get_length (context) == 0)

840 {

841 \_dbus_verbose ("context is zero-length\n");

842 return FALSE;

843 }

844

845 if (!\_dbus_string_validate_ascii (context, 0,

846 \_dbus_string_get_length (context)))

847 {

848 \_dbus_verbose ("context not valid ascii\n");

849 return FALSE;

850 }

851

852 /\* no directory separators \*/

853 if (\_dbus_string_find (context, 0, "/", NULL))

854 {

855 \_dbus_verbose ("context contains a slash\n");

856 return FALSE;

857 }

858

859 if (\_dbus_string_find (context, 0, "\\", NULL))

860 {

861 \_dbus_verbose ("context contains a backslash\n");

862 return FALSE;

863 }

864

865 /\* prevent attempts to use dotfiles or ".." or ".lock"

866 \* all of which might allow some kind of attack

867 \*/

868 if (\_dbus_string_find (context, 0, ".", NULL))

869 {

870 \_dbus_verbose ("context contains a dot\n");

871 return FALSE;

872 }

873

874 /\* no spaces/tabs, those are used for separators in the protocol \*/

875 if (\_dbus_string_find_blank (context, 0, NULL))

876 {

877 \_dbus_verbose ("context contains a blank\n");

878 return FALSE;

879 }

880

881 if (\_dbus_string_find (context, 0, "\n", NULL))

882 {

883 \_dbus_verbose ("context contains a newline\n");

884 return FALSE;

885 }

886

887 if (\_dbus_string_find (context, 0, "\r", NULL))

888 {

889 \_dbus_verbose ("context contains a carriage return\n");

890 return FALSE;

891 }

892

893 return TRUE;

894}

895

896static DBusKey\*

897find_recent_key (DBusKeyring \*keyring)

898{

899 int i;

900 dbus_int64_t tv_sec;

901 long tv_usec;

902

903 \_dbus_get_real_time (&tv_sec, &tv_usec);

904

905 i = 0;

906 while (i \< keyring-\>n_keys)

907 {

908 DBusKey \*key = &keyring-\>keys\[i\];

909

910 \_dbus_verbose ("Key %d is %" DBUS_INT64_MODIFIER "d seconds old\n",

911 i, tv_sec - key-\>creation_time);

912

913 if ((tv_sec - NEW_KEY_TIMEOUT_SECONDS) \< key-\>creation_time)

914 return key;

915

916 ++i;

917 }

918

919 return NULL;

920}

921

933int

934\_dbus_keyring_get_best_key (DBusKeyring \*keyring,

935 DBusError \*error)

936{

937 DBusKey \*key;

938

939 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

940

941 key = find_recent_key (keyring);

942 if (key)

943 return key-\>id;

944

945 /\* All our keys are too old, or we've never loaded the

946 \* keyring. Create a new one.

947 \*/

948 if (!\_dbus_keyring_reload (keyring, TRUE,

949 error))

950 return -1;

951

952 key = find_recent_key (keyring);

953 if (key)

954 return key-\>id;

955 else

956 {

957 dbus_set_error_const (error,

958 DBUS_ERROR_FAILED,

959 "No recent-enough key found in keyring, and unable to create a new key");

960 return -1;

961 }

962}

963

972dbus_bool_t

973\_dbus_keyring_is_for_credentials (DBusKeyring \*keyring,

974 DBusCredentials \*credentials)

975{

976 return \_dbus_credentials_same_user (keyring-\>credentials,

977 credentials);

978}

979

991dbus_bool_t

992\_dbus_keyring_get_hex_key (DBusKeyring \*keyring,

993 int key_id,

994 DBusString \*hex_key)

995{

996 DBusKey \*key;

997

998 key = find_key_by_id (keyring-\>keys,

999 keyring-\>n_keys,

1000 key_id);

1001 if (key == NULL)

1002 return TRUE; /\* had enough memory, so TRUE \*/

1003

1004 return \_dbus_string_hex_encode (&key-\>secret, 0,

1005 hex_key,

1006 \_dbus_string_get_length (hex_key));

1007}

1008

/\* end of exposed API \*/

1010

1011\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

1012\#include "dbus-test.h"

1013\#include \<stdio.h\>

1014

1015dbus_bool_t

1016\_dbus_keyring_test (const char \*test_data_dir \_DBUS_GNUC_UNUSED)

1017{

1018 DBusString context;

1019 DBusKeyring \*ring1;

1020 DBusKeyring \*ring2;

1021 int id;

1022 DBusError error;

1023 int i;

1024

1025 ring1 = NULL;

1026 ring2 = NULL;

1027

1028 /\* Context validation \*/

1029

1030 \_dbus_string_init_const (&context, "foo");

1031 \_dbus_assert (\_dbus_keyring_validate_context (&context));

1032 \_dbus_string_init_const (&context, "org_freedesktop_blah");

1033 \_dbus_assert (\_dbus_keyring_validate_context (&context));

1034

1035 \_dbus_string_init_const (&context, "");

1036 \_dbus_assert (!\_dbus_keyring_validate_context (&context));

1037 \_dbus_string_init_const (&context, ".foo");

1038 \_dbus_assert (!\_dbus_keyring_validate_context (&context));

1039 \_dbus_string_init_const (&context, "bar.foo");

1040 \_dbus_assert (!\_dbus_keyring_validate_context (&context));

1041 \_dbus_string_init_const (&context, "bar/foo");

1042 \_dbus_assert (!\_dbus_keyring_validate_context (&context));

1043 \_dbus_string_init_const (&context, "bar\\foo");

1044 \_dbus_assert (!\_dbus_keyring_validate_context (&context));

1045 \_dbus_string_init_const (&context, "foo\xfa\xf0");

1046 \_dbus_assert (!\_dbus_keyring_validate_context (&context));

1047 \_dbus_string_init_const (&context, "foo\x80");

1048 \_dbus_assert (!\_dbus_keyring_validate_context (&context));

1049 \_dbus_string_init_const (&context, "foo\x7f");

1050 \_dbus_assert (\_dbus_keyring_validate_context (&context));

1051 \_dbus_string_init_const (&context, "foo bar");

1052 \_dbus_assert (!\_dbus_keyring_validate_context (&context));

1053

1054 if (!\_dbus_string_init (&context))

1055 \_dbus_test_fatal ("no memory");

1056 if (!\_dbus_string_append_byte (&context, '\0'))

1057 \_dbus_test_fatal ("no memory");

1058 \_dbus_assert (!\_dbus_keyring_validate_context (&context));

1059 \_dbus_string_free (&context);

1060

1061 /\* Now verify that if we create a key in keyring 1,

1062 \* it is properly loaded in keyring 2

1063 \*/

1064

1065 \_dbus_string_init_const (&context, "org_freedesktop_dbus_testsuite");

1066 dbus_error_init (&error);

1067 ring1 = \_dbus_keyring_new_for_credentials (NULL, &context,

1068 &error);

1069 \_dbus_assert (ring1 != NULL);

1070 \_dbus_assert (error.name == NULL);

1071

1072 id = \_dbus_keyring_get_best_key (ring1, &error);

1073 if (id \< 0)

1074 {

1075 fprintf (stderr, "Could not load keyring: %s\n", error.message);

1076 dbus_error_free (&error);

1077 goto failure;

1078 }

1079

1080 ring2 = \_dbus_keyring_new_for_credentials (NULL, &context, &error);

1081 \_dbus_assert (ring2 != NULL);

1082 \_dbus_assert (error.name == NULL);

1083

1084 if (ring1-\>n_keys != ring2-\>n_keys)

1085 {

1086 fprintf (stderr, "Different number of keys in keyrings\n");

1087 goto failure;

1088 }

1089

1090 /\* We guarantee we load and save keeping keys in a fixed

1091 \* order

1092 \*/

1093 i = 0;

1094 while (i \< ring1-\>n_keys)

1095 {

1096 if (ring1-\>keys\[i\].id != ring2-\>keys\[i\].id)

1097 {

1098 fprintf (stderr, "Keyring 1 has first key ID %d and keyring 2 has %d\n",

1099 ring1-\>keys\[i\].id, ring2-\>keys\[i\].id);

1100 goto failure;

1101 }

1102

1103 if (ring1-\>keys\[i\].creation_time != ring2-\>keys\[i\].creation_time)

1104 {

1105 fprintf (stderr, "Keyring 1 has first key time %" DBUS_INT64_MODIFIER "d and keyring 2 has %" DBUS_INT64_MODIFIER "d\n",

1106 ring1-\>keys\[i\].creation_time, ring2-\>keys\[i\].creation_time);

1107 goto failure;

1108 }

1109

1110 if (!\_dbus_string_equal (&ring1-\>keys\[i\].secret,

1111 &ring2-\>keys\[i\].secret))

1112 {

1113 fprintf (stderr, "Keyrings 1 and 2 have different secrets for same ID/timestamp\n");

1114 goto failure;

1115 }

1116

1117 ++i;

1118 }

1119

1120 \_dbus_test_diag (" %d keys in test", ring1-\>n_keys);

1121

1122 /\* Test ref/unref \*/

1123 \_dbus_keyring_ref (ring1);

1124 \_dbus_keyring_ref (ring2);

1125 \_dbus_keyring_unref (ring1);

1126 \_dbus_keyring_unref (ring2);

1127

1128

1129 /\* really unref \*/

1130 \_dbus_keyring_unref (ring1);

1131 \_dbus_keyring_unref (ring2);

1132

1133 return TRUE;

1134

1135 failure:

1136 if (ring1)

1137 \_dbus_keyring_unref (ring1);

1138 if (ring2)

1139 \_dbus_keyring_unref (ring2);

1140

1141 return FALSE;

1142}

1143

1144\#endif /\* DBUS_ENABLE_EMBEDDED_TESTS \*/

1145

\_dbus_credentials_same_user

dbus_bool_t \_dbus_credentials_same_user(DBusCredentials \*credentials, DBusCredentials \*other_credentials)

Check whether the user-identifying credentials in two credentials objects are identical.

**Definition** dbus-credentials.c:747

\_dbus_credentials_copy

DBusCredentials \* \_dbus_credentials_copy(DBusCredentials \*credentials)

Copy a credentials object.

**Definition** dbus-credentials.c:718

\_dbus_credentials_new_from_current_process

DBusCredentials \* \_dbus_credentials_new_from_current_process(void)

Creates a new object with the most important credentials (user ID and process ID) from the current pr...

**Definition** dbus-credentials.c:113

\_dbus_credentials_unref

void \_dbus_credentials_unref(DBusCredentials \*credentials)

Decrement refcount on credentials.

**Definition** dbus-credentials.c:148

\_dbus_credentials_are_anonymous

dbus_bool_t \_dbus_credentials_are_anonymous(DBusCredentials \*credentials)

Checks whether a credentials object contains a user identity.

**Definition** dbus-credentials.c:558

DBUS_ERROR_INIT

\#define DBUS_ERROR_INIT

Expands to a suitable initializer for a DBusError on the stack.

**Definition** dbus-errors.h:64

dbus_set_error_const

void dbus_set_error_const(DBusError \*error, const char \*name, const char \*message)

Assigns an error name and message to a DBusError.

**Definition** dbus-errors.c:245

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

\_dbus_delete_file

dbus_bool_t \_dbus_delete_file(const DBusString \*filename, DBusError \*error)

Deletes the given file.

**Definition** dbus-file-unix.c:441

\_dbus_create_file_exclusively

dbus_bool_t \_dbus_create_file_exclusively(const DBusString \*filename, DBusError \*error)

Creates the given file, failing if the file already exists.

**Definition** dbus-file-unix.c:395

\_dbus_string_save_to_file

dbus_bool_t \_dbus_string_save_to_file(const DBusString \*str, const DBusString \*filename, dbus_bool_t world_readable, DBusError \*error)

Writes a string out to a file.

**Definition** dbus-file-unix.c:208

\_dbus_file_get_contents

dbus_bool_t \_dbus_file_get_contents(DBusString \*str, const DBusString \*filename, DBusError \*error)

Appends the contents of the given file to the string, returning error code.

**Definition** dbus-file-unix.c:63

\_dbus_assert_not_reached

\#define \_dbus_assert_not_reached(explanation)

Aborts with an error message if called.

**Definition** dbus-internals.h:164

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_dbus_warn

void \_dbus_warn(const char \*format,...)

Prints a warning message to stderr.

**Definition** dbus-internals.c:278

\_DBUS_INT32_MAX

\#define \_DBUS_INT32_MAX

Maximum value of type "int32".

**Definition** dbus-internals.h:323

LOCK_TIMEOUT_MILLISECONDS

\#define LOCK_TIMEOUT_MILLISECONDS

Length of each timeout while waiting for a lock.

**Definition** dbus-keyring.c:193

MAX_TIME_TRAVEL_SECONDS

\#define MAX_TIME_TRAVEL_SECONDS

The maximum amount of time a key can be in the future.

**Definition** dbus-keyring.c:80

NEW_KEY_TIMEOUT_SECONDS

\#define NEW_KEY_TIMEOUT_SECONDS

The maximum age of a key before we create a new key to use in challenges.

**Definition** dbus-keyring.c:70

MAX_KEYS_IN_FILE

\#define MAX_KEYS_IN_FILE

Maximum number of keys in the keyring before we just ignore the rest.

**Definition** dbus-keyring.c:89

MAX_LOCK_TIMEOUTS

\#define MAX_LOCK_TIMEOUTS

Maximum number of timeouts waiting for lock before we decide it's stale.

**Definition** dbus-keyring.c:191

EXPIRE_KEYS_TIMEOUT_SECONDS

\#define EXPIRE_KEYS_TIMEOUT_SECONDS

The time after which we drop a key from the secrets file.

**Definition** dbus-keyring.c:76

\_dbus_keyring_get_best_key

int \_dbus_keyring_get_best_key(DBusKeyring \*keyring, DBusError \*error)

Gets a recent key to use for authentication.

**Definition** dbus-keyring.c:934

\_dbus_keyring_validate_context

dbus_bool_t \_dbus_keyring_validate_context(const DBusString \*context)

Checks whether the context is a valid context.

**Definition** dbus-keyring.c:837

\_dbus_keyring_is_for_credentials

dbus_bool_t \_dbus_keyring_is_for_credentials(DBusKeyring \*keyring, DBusCredentials \*credentials)

Checks whether the keyring is for the same user as the given credentials.

**Definition** dbus-keyring.c:973

\_dbus_keyring_new_for_credentials

DBusKeyring \* \_dbus_keyring_new_for_credentials(DBusCredentials \*credentials, const DBusString \*context, DBusError \*error)

Creates a new keyring that lives in the ~/.dbus-keyrings directory of the user represented by credent...

**Definition** dbus-keyring.c:693

\_dbus_keyring_get_hex_key

dbus_bool_t \_dbus_keyring_get_hex_key(DBusKeyring \*keyring, int key_id, DBusString \*hex_key)

Gets the hex-encoded secret key for the given ID.

**Definition** dbus-keyring.c:992

\_dbus_keyring_ref

DBusKeyring \* \_dbus_keyring_ref(DBusKeyring \*keyring)

Increments reference count of the keyring.

**Definition** dbus-keyring.c:651

\_dbus_keyring_unref

void \_dbus_keyring_unref(DBusKeyring \*keyring)

Decrements refcount and finalizes if it reaches zero.

**Definition** dbus-keyring.c:665

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

dbus_new0

\#define dbus_new0(type, count)

Safe macro for using dbus_malloc0().

**Definition** dbus-memory.h:60

DBUS_ERROR_NOT_SUPPORTED

\#define DBUS_ERROR_NOT_SUPPORTED

Requested operation isn't supported (like ENOSYS on UNIX).

**Definition** dbus-protocol.h:375

DBUS_ERROR_FAILED

\#define DBUS_ERROR_FAILED

A generic error; "something went wrong" - see the error message for more.

**Definition** dbus-protocol.h:361

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

\_dbus_string_append

dbus_bool_t \_dbus_string_append(DBusString \*str, const char \*buffer)

Appends a nul-terminated C-style string to a DBusString.

**Definition** dbus-string.c:980

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

\_dbus_string_parse_int64

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_parse_int64(const DBusString \*str, int start, dbus_int64_t \*value_return, int \*end_return)

Parses a dbus_int64_t integer contained in a DBusString.

**Definition** dbus-sysdeps.c:449

\_dbus_string_skip_blank

void \_dbus_string_skip_blank(const DBusString \*str, int start, int \*end)

Skips blanks from start, storing the first non-blank in \*end (blank is space or tab).

**Definition** dbus-string.c:1865

\_dbus_string_find

dbus_bool_t \_dbus_string_find(const DBusString \*str, int start, const char \*substr, int \*found)

Finds the given substring in the string, returning TRUE and filling in the byte index where the subst...

**Definition** dbus-string.c:1666

\_dbus_string_find_blank

dbus_bool_t \_dbus_string_find_blank(const DBusString \*str, int start, int \*found)

Finds a blank (space or tab) in the string.

**Definition** dbus-string.c:1827

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_string_pop_line

dbus_bool_t \_dbus_string_pop_line(DBusString \*source, DBusString \*dest)

Assigns a newline-terminated or \r\n-terminated line from the front of the string to the given dest s...

**Definition** dbus-string.c:1971

\_dbus_string_zero

void \_dbus_string_zero(DBusString \*str)

Clears all allocated bytes in the string to zero.

**Definition** dbus-string.c:2808

\_dbus_string_parse_int

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_parse_int(const DBusString \*str, int start, long \*value_return, int \*end_return)

Parses an integer contained in a DBusString.

**Definition** dbus-sysdeps.c:371

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

\_dbus_string_hex_encode

dbus_bool_t \_dbus_string_hex_encode(const DBusString \*source, int start, DBusString \*dest, int insert_at)

Encodes a string in hex, the way MD5 and SHA-1 are usually encoded.

**Definition** dbus-string.c:2382

\_dbus_string_append_printf

dbus_bool_t \_dbus_string_append_printf(DBusString \*str, const char \*format,...)

Appends a printf-style formatted string to the DBusString.

**Definition** dbus-string.c:1147

\_dbus_string_get_const_data

const char \* \_dbus_string_get_const_data(const DBusString \*str)

Gets the raw character buffer from a const string.

**Definition** dbus-string.c:513

\_dbus_string_move

dbus_bool_t \_dbus_string_move(DBusString \*source, int start, DBusString \*dest, int insert_at)

Moves the end of one string into another string.

**Definition** dbus-string.c:1321

\_dbus_string_equal

dbus_bool_t \_dbus_string_equal(const DBusString \*a, const DBusString \*b)

Tests two DBusString for equality.

**Definition** dbus-string.c:2075

\_dbus_append_keyring_directory_for_credentials

dbus_bool_t \_dbus_append_keyring_directory_for_credentials(DBusString \*directory, DBusCredentials \*credentials)

Appends the directory in which a keyring for the given credentials should be stored.

**Definition** dbus-sysdeps-unix.c:4721

\_dbus_check_setuid

dbus_bool_t \_dbus_check_setuid(void)

NOTE: If you modify this function, please also consider making the corresponding change in GLib.

**Definition** dbus-sysdeps-unix.c:5002

\_dbus_sleep_milliseconds

void \_dbus_sleep_milliseconds(int milliseconds)

Sleeps the given number of milliseconds.

**Definition** dbus-sysdeps-unix.c:3542

\_dbus_check_dir_is_private_to_user

dbus_bool_t \_dbus_check_dir_is_private_to_user(DBusString \*dir, DBusError \*error)

Checks to make sure the given directory is private to the user.

**Definition** dbus-sysdeps-unix.c:2644

\_dbus_credentials_add_from_current_process

dbus_bool_t \_dbus_credentials_add_from_current_process(DBusCredentials \*credentials)

Adds the most important credentials of the current process (the uid and pid) to the passed-in credent...

**Definition** dbus-sysdeps-unix.c:3005

\_dbus_generate_random_bytes

dbus_bool_t \_dbus_generate_random_bytes(DBusString \*str, int n_bytes, DBusError \*error)

Generates the given number of securely random bytes, using the best mechanism we can come up with.

**Definition** dbus-sysdeps-unix.c:3572

\_dbus_concat_dir_and_file

dbus_bool_t \_dbus_concat_dir_and_file(DBusString \*dir, const DBusString \*next_component)

Appends the given filename to the given directory.

**Definition** dbus-sysdeps-unix.c:3497

\_dbus_get_real_time

void \_dbus_get_real_time(dbus_int64_t \*tv_sec, long \*tv_usec)

Get current time, as in gettimeofday().

**Definition** dbus-sysdeps-unix.c:3412

\_dbus_ensure_directory

dbus_bool_t \_dbus_ensure_directory(const DBusString \*filename, DBusError \*error)

Creates a directory; succeeds if the directory is created or already existed.

**Definition** dbus-sysdeps-unix.c:3434

DBUS_INT64_MODIFIER

\#define DBUS_INT64_MODIFIER

A string literal for a length modifier that is appropriate to print the dbus_int64_t and dbus_uint64\_...

**Definition** dbus-arch-deps.h:39

DBusCredentials

**Definition** dbus-credentials.c:60

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusError::name

const char \* name

public error name field

**Definition** dbus-errors.h:52

DBusError::message

const char \* message

public error message field

**Definition** dbus-errors.h:53

DBusKey

A single key from the cookie file.

**Definition** dbus-keyring.c:96

DBusKey::secret

DBusString secret

the actual key

**Definition** dbus-keyring.c:101

DBusKey::id

dbus_int32_t id

identifier used to refer to the key

**Definition** dbus-keyring.c:97

DBusKey::creation_time

dbus_int64_t creation_time

when the key was generated, in seconds since 1970-01-01

**Definition** dbus-keyring.c:99

DBusKeyring

Internals of DBusKeyring.

**Definition** dbus-keyring.c:112

DBusKeyring::keys

DBusKey \* keys

Keys loaded from the file.

**Definition** dbus-keyring.c:117

DBusKeyring::filename

DBusString filename

Keyring filename.

**Definition** dbus-keyring.c:115

DBusKeyring::credentials

DBusCredentials \* credentials

Credentials containing user the keyring is for.

**Definition** dbus-keyring.c:119

DBusKeyring::n_keys

int n_keys

Number of keys.

**Definition** dbus-keyring.c:118

DBusKeyring::refcount

int refcount

Reference count.

**Definition** dbus-keyring.c:113

DBusKeyring::directory

DBusString directory

Directory the below two items are inside.

**Definition** dbus-keyring.c:114

DBusKeyring::filename_lock

DBusString filename_lock

Name of lockfile.

**Definition** dbus-keyring.c:116

DBusString

**Definition** dbus-string.h:47
