dbus-auth.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-auth.c Authentication

3 \*

4 \* Copyright (C) 2002, 2003, 2004 Red Hat Inc.

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

27\#include "dbus-auth.h"

28\#include "dbus-string.h"

29\#include "dbus-list.h"

30\#include "dbus-internals.h"

31\#include "dbus-keyring.h"

32\#include "dbus-sha.h"

33\#include "dbus-protocol.h"

34\#include "dbus-credentials.h"

35

72typedef dbus_bool_t (\* DBusInitialResponseFunction) (DBusAuth \*auth,

73 DBusString \*response);

74

79typedef dbus_bool_t (\* DBusAuthDataFunction) (DBusAuth \*auth,

80 const DBusString \*data);

81

85typedef dbus_bool_t (\* DBusAuthEncodeFunction) (DBusAuth \*auth,

86 const DBusString \*data,

87 DBusString \*encoded);

88

92typedef dbus_bool_t (\* DBusAuthDecodeFunction) (DBusAuth \*auth,

93 const DBusString \*data,

94 DBusString \*decoded);

95

99typedef void (\* DBusAuthShutdownFunction) (DBusAuth \*auth);

100

104typedef struct

105{

106 const char \*mechanism;

107 DBusAuthDataFunction server_data_func;

108 DBusAuthEncodeFunction server_encode_func;

109 DBusAuthDecodeFunction server_decode_func;

110 DBusAuthShutdownFunction server_shutdown_func;

111 DBusInitialResponseFunction client_initial_response_func;

112 DBusAuthDataFunction client_data_func;

113 DBusAuthEncodeFunction client_encode_func;

114 DBusAuthDecodeFunction client_decode_func;

115 DBusAuthShutdownFunction client_shutdown_func;

116} DBusAuthMechanismHandler;

117

121typedef enum {

122 DBUS_AUTH_COMMAND_AUTH,

123 DBUS_AUTH_COMMAND_CANCEL,

124 DBUS_AUTH_COMMAND_DATA,

125 DBUS_AUTH_COMMAND_BEGIN,

126 DBUS_AUTH_COMMAND_REJECTED,

127 DBUS_AUTH_COMMAND_OK,

128 DBUS_AUTH_COMMAND_ERROR,

129 DBUS_AUTH_COMMAND_UNKNOWN,

130 DBUS_AUTH_COMMAND_NEGOTIATE_UNIX_FD,

131 DBUS_AUTH_COMMAND_AGREE_UNIX_FD

132} DBusAuthCommand;

133

139typedef dbus_bool_t (\* DBusAuthStateFunction) (DBusAuth \*auth,

140 DBusAuthCommand command,

141 const DBusString \*args);

142

146typedef struct

147{

148 const char \*name;

149 DBusAuthStateFunction handler;

150} DBusAuthStateData;

151

155struct DBusAuth

156{

157 int refcount;

158 const char \*side;

160 DBusString incoming;

161 DBusString outgoing;

163 const DBusAuthStateData \*state;

165 const DBusAuthMechanismHandler \*mech;

167 DBusString identity;

171 DBusCredentials \*credentials;

174 DBusCredentials \*authorized_identity;

176 DBusCredentials \*desired_identity;

178 DBusString context;

179 DBusKeyring \*keyring;

180 int cookie_id;

181 DBusString challenge;

183 char \*\*allowed_mechs;

187 unsigned int needed_memory : 1;

190 unsigned int already_got_mechanisms : 1;

191 unsigned int already_asked_for_initial_response : 1;

192 unsigned int buffer_outstanding : 1;

194 unsigned int unix_fd_possible : 1;

195 unsigned int unix_fd_negotiated : 1;

196};

197

201typedef struct

202{

203 DBusAuth base;

205 DBusList \*mechs_to_try;

207 DBusString guid_from_server;

209} DBusAuthClient;

210

214typedef struct

215{

216 DBusAuth base;

218 int failures;

219 int max_failures;

221 DBusString guid;

223} DBusAuthServer;

224

225static void goto_state (DBusAuth \*auth,

226 const DBusAuthStateData \*new_state);

227static dbus_bool_t send_auth (DBusAuth \*auth,

228 const DBusAuthMechanismHandler \*mech);

229static dbus_bool_t send_data (DBusAuth \*auth,

230 DBusString \*data);

231static dbus_bool_t send_rejected (DBusAuth \*auth);

232static dbus_bool_t send_error (DBusAuth \*auth,

233 const char \*message);

234static dbus_bool_t send_ok (DBusAuth \*auth);

235static dbus_bool_t send_begin (DBusAuth \*auth);

236static dbus_bool_t send_cancel (DBusAuth \*auth);

237static dbus_bool_t send_negotiate_unix_fd (DBusAuth \*auth);

238static dbus_bool_t send_agree_unix_fd (DBusAuth \*auth);

239

244static dbus_bool_t handle_server_state_waiting_for_auth (DBusAuth \*auth,

245 DBusAuthCommand command,

246 const DBusString \*args);

247static dbus_bool_t handle_server_state_waiting_for_data (DBusAuth \*auth,

248 DBusAuthCommand command,

249 const DBusString \*args);

250static dbus_bool_t handle_server_state_waiting_for_begin (DBusAuth \*auth,

251 DBusAuthCommand command,

252 const DBusString \*args);

253

254static const DBusAuthStateData server_state_waiting_for_auth = {

255 "WaitingForAuth", handle_server_state_waiting_for_auth

256};

257static const DBusAuthStateData server_state_waiting_for_data = {

258 "WaitingForData", handle_server_state_waiting_for_data

259};

260static const DBusAuthStateData server_state_waiting_for_begin = {

261 "WaitingForBegin", handle_server_state_waiting_for_begin

262};

263

268static dbus_bool_t handle_client_state_waiting_for_data (DBusAuth \*auth,

269 DBusAuthCommand command,

270 const DBusString \*args);

271static dbus_bool_t handle_client_state_waiting_for_ok (DBusAuth \*auth,

272 DBusAuthCommand command,

273 const DBusString \*args);

274static dbus_bool_t handle_client_state_waiting_for_reject (DBusAuth \*auth,

275 DBusAuthCommand command,

276 const DBusString \*args);

277static dbus_bool_t handle_client_state_waiting_for_agree_unix_fd (DBusAuth \*auth,

278 DBusAuthCommand command,

279 const DBusString \*args);

280

281static const DBusAuthStateData client_state_need_send_auth = {

282 "NeedSendAuth", NULL

283};

284static const DBusAuthStateData client_state_waiting_for_data = {

285 "WaitingForData", handle_client_state_waiting_for_data

286};

287/\* The WaitingForOK state doesn't appear to be used.

288 \* See https://bugs.freedesktop.org/show_bug.cgi?id=97298 \*/

289\_DBUS_GNUC_UNUSED

290static const DBusAuthStateData client_state_waiting_for_ok = {

291 "WaitingForOK", handle_client_state_waiting_for_ok

292};

293static const DBusAuthStateData client_state_waiting_for_reject = {

294 "WaitingForReject", handle_client_state_waiting_for_reject

295};

296static const DBusAuthStateData client_state_waiting_for_agree_unix_fd = {

297 "WaitingForAgreeUnixFD", handle_client_state_waiting_for_agree_unix_fd

298};

299

304static const DBusAuthStateData common_state_authenticated = {

305 "Authenticated", NULL

306};

307

308static const DBusAuthStateData common_state_need_disconnect = {

309 "NeedDisconnect", NULL

310};

311

312static const char auth_side_client\[\] = "client";

313static const char auth_side_server\[\] = "server";

318\#define DBUS_AUTH_IS_SERVER(auth) ((auth)-\>side == auth_side_server)

323\#define DBUS_AUTH_IS_CLIENT(auth) ((auth)-\>side == auth_side_client)

328\#define DBUS_AUTH_CLIENT(auth) ((DBusAuthClient\*)(auth))

333\#define DBUS_AUTH_SERVER(auth) ((DBusAuthServer\*)(auth))

334

340\#define DBUS_AUTH_NAME(auth) ((auth)-\>side)

341

342static DBusAuth\*

343\_dbus_auth_new (int size)

344{

345 DBusAuth \*auth;

346

347 auth = dbus_malloc0 (size);

348 if (auth == NULL)

349 return NULL;

350

351 auth-\>refcount = 1;

352

353 auth-\>keyring = NULL;

354 auth-\>cookie_id = -1;

355

356 /\* note that we don't use the max string length feature,

357 \* because you can't use that feature if you're going to

358 \* try to recover from out-of-memory (it creates

359 \* what looks like unrecoverable inability to alloc

360 \* more space in the string). But we do handle

361 \* overlong buffers in \_dbus_auth_do_work().

362 \*/

363

364 if (!\_dbus_string_init (&auth-\>incoming))

365 goto enomem_0;

366

367 if (!\_dbus_string_init (&auth-\>outgoing))

368 goto enomem_1;

369

370 if (!\_dbus_string_init (&auth-\>identity))

371 goto enomem_2;

372

373 if (!\_dbus_string_init (&auth-\>context))

374 goto enomem_3;

375

376 if (!\_dbus_string_init (&auth-\>challenge))

377 goto enomem_4;

378

379 /\* default context if none is specified \*/

380 if (!\_dbus_string_append (&auth-\>context, "org_freedesktop_general"))

381 goto enomem_5;

382

383 auth-\>credentials = \_dbus_credentials_new ();

384 if (auth-\>credentials == NULL)

385 goto enomem_6;

386

387 auth-\>authorized_identity = \_dbus_credentials_new ();

388 if (auth-\>authorized_identity == NULL)

389 goto enomem_7;

390

391 auth-\>desired_identity = \_dbus_credentials_new ();

392 if (auth-\>desired_identity == NULL)

393 goto enomem_8;

394

395 return auth;

396

397\#if 0

398 enomem_9:

399 \_dbus_credentials_unref (auth-\>desired_identity);

400\#endif

401 enomem_8:

402 \_dbus_credentials_unref (auth-\>authorized_identity);

403 enomem_7:

404 \_dbus_credentials_unref (auth-\>credentials);

405 enomem_6:

406 /\* last alloc was an append to context, which is freed already below \*/ ;

407 enomem_5:

408 \_dbus_string_free (&auth-\>challenge);

409 enomem_4:

410 \_dbus_string_free (&auth-\>context);

411 enomem_3:

412 \_dbus_string_free (&auth-\>identity);

413 enomem_2:

414 \_dbus_string_free (&auth-\>outgoing);

415 enomem_1:

416 \_dbus_string_free (&auth-\>incoming);

417 enomem_0:

418 dbus_free (auth);

419 return NULL;

420}

421

422static void

423shutdown_mech (DBusAuth \*auth)

424{

425 /\* Cancel any auth \*/

426 auth-\>already_asked_for_initial_response = FALSE;

427 \_dbus_string_set_length (&auth-\>identity, 0);

428

429 \_dbus_credentials_clear (auth-\>authorized_identity);

430 \_dbus_credentials_clear (auth-\>desired_identity);

431

432 if (auth-\>mech != NULL)

433 {

434 \_dbus_verbose ("%s: Shutting down mechanism %s\n",

435 DBUS_AUTH_NAME (auth), auth-\>mech-\>mechanism);

436

437 if (DBUS_AUTH_IS_CLIENT (auth))

438 (\* auth-\>mech-\>client_shutdown_func) (auth);

439 else

440 (\* auth-\>mech-\>server_shutdown_func) (auth);

441

442 auth-\>mech = NULL;

443 }

444}

445

446/\*

447 \* DBUS_COOKIE_SHA1 mechanism

448 \*/

449

450/\* Returns TRUE but with an empty string hash if the

451 \* cookie_id isn't known. As with all this code

452 \* TRUE just means we had enough memory.

453 \*/

454static dbus_bool_t

455sha1_compute_hash (DBusAuth \*auth,

456 int cookie_id,

457 const DBusString \*server_challenge,

458 const DBusString \*client_challenge,

459 DBusString \*hash)

460{

461 DBusString cookie;

462 DBusString to_hash;

463 dbus_bool_t retval;

464

465 \_dbus_assert (auth-\>keyring != NULL);

466

467 retval = FALSE;

468

469 if (!\_dbus_string_init (&cookie))

470 return FALSE;

471

472 if (!\_dbus_keyring_get_hex_key (auth-\>keyring, cookie_id,

473 &cookie))

474 goto out_0;

475

476 if (\_dbus_string_get_length (&cookie) == 0)

477 {

478 retval = TRUE;

479 goto out_0;

480 }

481

482 if (!\_dbus_string_init (&to_hash))

483 goto out_0;

484

485 if (!\_dbus_string_copy (server_challenge, 0,

486 &to_hash, \_dbus_string_get_length (&to_hash)))

487 goto out_1;

488

489 if (!\_dbus_string_append (&to_hash, ":"))

490 goto out_1;

491

492 if (!\_dbus_string_copy (client_challenge, 0,

493 &to_hash, \_dbus_string_get_length (&to_hash)))

494 goto out_1;

495

496 if (!\_dbus_string_append (&to_hash, ":"))

497 goto out_1;

498

499 if (!\_dbus_string_copy (&cookie, 0,

500 &to_hash, \_dbus_string_get_length (&to_hash)))

501 goto out_1;

502

503 if (!\_dbus_sha_compute (&to_hash, hash))

504 goto out_1;

505

506 retval = TRUE;

507

508 out_1:

509 \_dbus_string_zero (&to_hash);

510 \_dbus_string_free (&to_hash);

511 out_0:

512 \_dbus_string_zero (&cookie);

513 \_dbus_string_free (&cookie);

514 return retval;

515}

516

521\#define N_CHALLENGE_BYTES (128/8)

522

523static dbus_bool_t

524sha1_handle_first_client_response (DBusAuth \*auth,

525 const DBusString \*data)

526{

527 /\* We haven't sent a challenge yet, we're expecting a desired

528 \* username from the client.

529 \*/

530 DBusString tmp = \_DBUS_STRING_INIT_INVALID;

531 DBusString tmp2 = \_DBUS_STRING_INIT_INVALID;

532 dbus_bool_t retval = FALSE;

533 DBusError error = DBUS_ERROR_INIT;

534 DBusCredentials \*myself = NULL;

535

536 \_dbus_string_set_length (&auth-\>challenge, 0);

537

538 if (\_dbus_string_get_length (data) \> 0)

539 {

540 if (\_dbus_string_get_length (&auth-\>identity) \> 0)

541 {

542 /\* Tried to send two auth identities, wtf \*/

543 \_dbus_verbose ("%s: client tried to send auth identity, but we already have one\n",

544 DBUS_AUTH_NAME (auth));

545 return send_rejected (auth);

546 }

547 else

548 {

549 /\* this is our auth identity \*/

550 if (!\_dbus_string_copy (data, 0, &auth-\>identity, 0))

551 return FALSE;

552 }

553 }

554

555 if (!\_dbus_credentials_add_from_user (auth-\>desired_identity, data,

556 DBUS_CREDENTIALS_ADD_FLAGS_USER_DATABASE,

557 &error))

558 {

559 if (dbus_error_has_name (&error, DBUS_ERROR_NO_MEMORY))

560 {

561 dbus_error_free (&error);

562 return FALSE;

563 }

564

565 \_dbus_verbose ("%s: Did not get a valid username from client: %s\n",

566 DBUS_AUTH_NAME (auth), error.message);

567 dbus_error_free (&error);

568 return send_rejected (auth);

569 }

570

571 if (!\_dbus_string_init (&tmp))

572 return FALSE;

573

574 if (!\_dbus_string_init (&tmp2))

575 {

576 \_dbus_string_free (&tmp);

577 return FALSE;

578 }

579

580 myself = \_dbus_credentials_new_from_current_process ();

581

582 if (myself == NULL)

583 goto out;

584

585 if (!\_dbus_credentials_same_user (myself, auth-\>desired_identity))

586 {

587 /\*

588 \* DBUS_COOKIE_SHA1 is not suitable for authenticating that the

589 \* client is anyone other than the user owning the process

590 \* containing the DBusServer: we probably aren't allowed to write

591 \* to other users' home directories. Even if we can (for example

592 \* uid 0 on traditional Unix or CAP_DAC_OVERRIDE on Linux), we

593 \* must not, because the other user controls their home directory,

594 \* and could carry out symlink attacks to make us read from or

595 \* write to unintended locations. It's difficult to avoid symlink

596 \* attacks in a portable way, so we just don't try. This isn't a

597 \* regression, because DBUS_COOKIE_SHA1 never worked for other

598 \* users anyway.

599 \*/

600 \_dbus_verbose ("%s: client tried to authenticate as \\%s\\, "

601 "but that doesn't match this process",

602 DBUS_AUTH_NAME (auth),

603 \_dbus_string_get_const_data (data));

604 retval = send_rejected (auth);

605 goto out;

606 }

607

608 /\* we cache the keyring for speed, so here we drop it if it's the

609 \* wrong one. FIXME caching the keyring here is useless since we use

610 \* a different DBusAuth for every connection.

611 \*/

612 if (auth-\>keyring &&

613 !\_dbus_keyring_is_for_credentials (auth-\>keyring,

614 auth-\>desired_identity))

615 {

616 \_dbus_keyring_unref (auth-\>keyring);

617 auth-\>keyring = NULL;

618 }

619

620 if (auth-\>keyring == NULL)

621 {

622 auth-\>keyring = \_dbus_keyring_new_for_credentials (auth-\>desired_identity,

623 &auth-\>context,

624 &error);

625

626 if (auth-\>keyring == NULL)

627 {

628 if (dbus_error_has_name (&error,

629 DBUS_ERROR_NO_MEMORY))

630 {

631 dbus_error_free (&error);

632 goto out;

633 }

634 else

635 {

636 \_DBUS_ASSERT_ERROR_IS_SET (&error);

637 \_dbus_verbose ("%s: Error loading keyring: %s\n",

638 DBUS_AUTH_NAME (auth), error.message);

639 if (send_rejected (auth))

640 retval = TRUE; /\* retval is only about mem \*/

641 dbus_error_free (&error);

642 goto out;

643 }

644 }

645 else

646 {

647 \_dbus_assert (!dbus_error_is_set (&error));

648 }

649 }

650

651 \_dbus_assert (auth-\>keyring != NULL);

652

653 auth-\>cookie_id = \_dbus_keyring_get_best_key (auth-\>keyring, &error);

654 if (auth-\>cookie_id \< 0)

655 {

656 \_DBUS_ASSERT_ERROR_IS_SET (&error);

657 \_dbus_verbose ("%s: Could not get a cookie ID to send to client: %s\n",

658 DBUS_AUTH_NAME (auth), error.message);

659 if (send_rejected (auth))

660 retval = TRUE;

661 dbus_error_free (&error);

662 goto out;

663 }

664 else

665 {

666 \_dbus_assert (!dbus_error_is_set (&error));

667 }

668

669 if (!\_dbus_string_copy (&auth-\>context, 0,

670 &tmp2, \_dbus_string_get_length (&tmp2)))

671 goto out;

672

673 if (!\_dbus_string_append_printf (&tmp2, " %d ", auth-\>cookie_id))

674 goto out;

675

676 if (!\_dbus_generate_random_bytes (&tmp, N_CHALLENGE_BYTES, &error))

677 {

678 if (dbus_error_has_name (&error, DBUS_ERROR_NO_MEMORY))

679 {

680 dbus_error_free (&error);

681 goto out;

682 }

683 else

684 {

685 \_DBUS_ASSERT_ERROR_IS_SET (&error);

686 \_dbus_verbose ("%s: Error generating challenge: %s\n",

687 DBUS_AUTH_NAME (auth), error.message);

688 if (send_rejected (auth))

689 retval = TRUE; /\* retval is only about mem \*/

690

691 dbus_error_free (&error);

692 goto out;

693 }

694 }

695

696 \_dbus_string_set_length (&auth-\>challenge, 0);

697 if (!\_dbus_string_hex_encode (&tmp, 0, &auth-\>challenge, 0))

698 goto out;

699

700 if (!\_dbus_string_hex_encode (&tmp, 0, &tmp2,

701 \_dbus_string_get_length (&tmp2)))

702 goto out;

703

704 if (!send_data (auth, &tmp2))

705 goto out;

706

707 goto_state (auth, &server_state_waiting_for_data);

708 retval = TRUE;

709

710 out:

711 \_dbus_string_zero (&tmp);

712 \_dbus_string_free (&tmp);

713 \_dbus_string_zero (&tmp2);

714 \_dbus_string_free (&tmp2);

715 \_dbus_clear_credentials (&myself);

716

717 return retval;

718}

719

720static dbus_bool_t

721sha1_handle_second_client_response (DBusAuth \*auth,

722 const DBusString \*data)

723{

724 /\* We are expecting a response which is the hex-encoded client

725 \* challenge, space, then SHA-1 hash of the concatenation of our

726 \* challenge, ":", client challenge, ":", secret key, all

727 \* hex-encoded.

728 \*/

729 int i;

730 DBusString client_challenge;

731 DBusString client_hash;

732 dbus_bool_t retval;

733 DBusString correct_hash;

734

735 retval = FALSE;

736

737 if (!\_dbus_string_find_blank (data, 0, &i))

738 {

739 \_dbus_verbose ("%s: no space separator in client response\n",

740 DBUS_AUTH_NAME (auth));

741 return send_rejected (auth);

742 }

743

744 if (!\_dbus_string_init (&client_challenge))

745 goto out_0;

746

747 if (!\_dbus_string_init (&client_hash))

748 goto out_1;

749

750 if (!\_dbus_string_copy_len (data, 0, i, &client_challenge,

751 0))

752 goto out_2;

753

754 \_dbus_string_skip_blank (data, i, &i);

755

756 if (!\_dbus_string_copy_len (data, i,

757 \_dbus_string_get_length (data) - i,

758 &client_hash,

759 0))

760 goto out_2;

761

762 if (\_dbus_string_get_length (&client_challenge) == 0 \|\|

763 \_dbus_string_get_length (&client_hash) == 0)

764 {

765 \_dbus_verbose ("%s: zero-length client challenge or hash\n",

766 DBUS_AUTH_NAME (auth));

767 if (send_rejected (auth))

768 retval = TRUE;

769 goto out_2;

770 }

771

772 if (!\_dbus_string_init (&correct_hash))

773 goto out_2;

774

775 if (!sha1_compute_hash (auth, auth-\>cookie_id,

776 &auth-\>challenge,

777 &client_challenge,

778 &correct_hash))

779 goto out_3;

780

781 /\* if cookie_id was invalid, then we get an empty hash \*/

782 if (\_dbus_string_get_length (&correct_hash) == 0)

783 {

784 if (send_rejected (auth))

785 retval = TRUE;

786 goto out_3;

787 }

788

789 if (!\_dbus_string_equal (&client_hash, &correct_hash))

790 {

791 if (send_rejected (auth))

792 retval = TRUE;

793 goto out_3;

794 }

795

796 if (!\_dbus_credentials_add_credentials (auth-\>authorized_identity,

797 auth-\>desired_identity))

798 goto out_3;

799

800 /\* Copy process ID (and PID FD) from the socket credentials if it's there

801 \*/

802 if (!\_dbus_credentials_add_credential (auth-\>authorized_identity,

803 DBUS_CREDENTIAL_UNIX_PROCESS_FD,

804 auth-\>credentials))

805 goto out_3;

806 if (!\_dbus_credentials_add_credential (auth-\>authorized_identity,

807 DBUS_CREDENTIAL_UNIX_PROCESS_ID,

808 auth-\>credentials))

809 goto out_3;

810

811 if (!send_ok (auth))

812 goto out_3;

813

814 \_dbus_verbose ("%s: authenticated client using DBUS_COOKIE_SHA1\n",

815 DBUS_AUTH_NAME (auth));

816

817 retval = TRUE;

818

819 out_3:

820 \_dbus_string_zero (&correct_hash);

821 \_dbus_string_free (&correct_hash);

822 out_2:

823 \_dbus_string_zero (&client_hash);

824 \_dbus_string_free (&client_hash);

825 out_1:

826 \_dbus_string_free (&client_challenge);

827 out_0:

828 return retval;

829}

830

831static dbus_bool_t

832handle_server_data_cookie_sha1_mech (DBusAuth \*auth,

833 const DBusString \*data)

834{

835 if (auth-\>cookie_id \< 0)

836 return sha1_handle_first_client_response (auth, data);

837 else

838 return sha1_handle_second_client_response (auth, data);

839}

840

841static void

842handle_server_shutdown_cookie_sha1_mech (DBusAuth \*auth)

843{

844 auth-\>cookie_id = -1;

845 \_dbus_string_set_length (&auth-\>challenge, 0);

846}

847

848static dbus_bool_t

849handle_client_initial_response_cookie_sha1_mech (DBusAuth \*auth,

850 DBusString \*response)

851{

852 DBusString username;

853 dbus_bool_t retval;

854

855 retval = FALSE;

856

857 if (!\_dbus_string_init (&username))

858 return FALSE;

859

860 if (!\_dbus_append_user_from_current_process (&username))

861 goto out_0;

862

863 if (!\_dbus_string_hex_encode (&username, 0,

864 response,

865 \_dbus_string_get_length (response)))

866 goto out_0;

867

868 retval = TRUE;

869

870 out_0:

871 \_dbus_string_free (&username);

872

873 return retval;

874}

875

876static dbus_bool_t

877handle_client_data_cookie_sha1_mech (DBusAuth \*auth,

878 const DBusString \*data)

879{

880 /\* The data we get from the server should be the cookie context

881 \* name, the cookie ID, and the server challenge, separated by

882 \* spaces. We send back our challenge string and the correct hash.

883 \*/

884 dbus_bool_t retval = FALSE;

885 DBusString context;

886 DBusString cookie_id_str;

887 DBusString server_challenge;

888 DBusString client_challenge;

889 DBusString correct_hash;

890 DBusString tmp;

891 int i, j;

892 long val;

893 DBusError error = DBUS_ERROR_INIT;

894

895 if (!\_dbus_string_find_blank (data, 0, &i))

896 {

897 if (send_error (auth,

898 "Server did not send context/ID/challenge properly"))

899 retval = TRUE;

900 goto out_0;

901 }

902

903 if (!\_dbus_string_init (&context))

904 goto out_0;

905

906 if (!\_dbus_string_copy_len (data, 0, i,

907 &context, 0))

908 goto out_1;

909

910 \_dbus_string_skip_blank (data, i, &i);

911 if (!\_dbus_string_find_blank (data, i, &j))

912 {

913 if (send_error (auth,

914 "Server did not send context/ID/challenge properly"))

915 retval = TRUE;

916 goto out_1;

917 }

918

919 if (!\_dbus_string_init (&cookie_id_str))

920 goto out_1;

921

922 if (!\_dbus_string_copy_len (data, i, j - i,

923 &cookie_id_str, 0))

924 goto out_2;

925

926 if (!\_dbus_string_init (&server_challenge))

927 goto out_2;

928

929 i = j;

930 \_dbus_string_skip_blank (data, i, &i);

931 j = \_dbus_string_get_length (data);

932

933 if (!\_dbus_string_copy_len (data, i, j - i,

934 &server_challenge, 0))

935 goto out_3;

936

937 if (!\_dbus_keyring_validate_context (&context))

938 {

939 if (send_error (auth, "Server sent invalid cookie context"))

940 retval = TRUE;

941 goto out_3;

942 }

943

944 if (!\_dbus_string_parse_int (&cookie_id_str, 0, &val, NULL))

945 {

946 if (send_error (auth, "Could not parse cookie ID as an integer"))

947 retval = TRUE;

948 goto out_3;

949 }

950

951 if (\_dbus_string_get_length (&server_challenge) == 0)

952 {

953 if (send_error (auth, "Empty server challenge string"))

954 retval = TRUE;

955 goto out_3;

956 }

957

958 if (auth-\>keyring == NULL)

959 {

960 auth-\>keyring = \_dbus_keyring_new_for_credentials (NULL,

961 &context,

962 &error);

963

964 if (auth-\>keyring == NULL)

965 {

966 if (dbus_error_has_name (&error,

967 DBUS_ERROR_NO_MEMORY))

968 {

969 dbus_error_free (&error);

970 goto out_3;

971 }

972 else

973 {

974 \_DBUS_ASSERT_ERROR_IS_SET (&error);

975

976 \_dbus_verbose ("%s: Error loading keyring: %s\n",

977 DBUS_AUTH_NAME (auth), error.message);

978

979 if (send_error (auth, "Could not load cookie file"))

980 retval = TRUE; /\* retval is only about mem \*/

981

982 dbus_error_free (&error);

983 goto out_3;

984 }

985 }

986 else

987 {

988 \_dbus_assert (!dbus_error_is_set (&error));

989 }

990 }

991

992 \_dbus_assert (auth-\>keyring != NULL);

993

994 if (!\_dbus_string_init (&tmp))

995 goto out_3;

996

997 if (!\_dbus_generate_random_bytes (&tmp, N_CHALLENGE_BYTES, &error))

998 {

999 if (dbus_error_has_name (&error, DBUS_ERROR_NO_MEMORY))

1000 {

1001 dbus_error_free (&error);

1002 goto out_4;

1003 }

1004 else

1005 {

1006 \_DBUS_ASSERT_ERROR_IS_SET (&error);

1007

1008 \_dbus_verbose ("%s: Failed to generate challenge: %s\n",

1009 DBUS_AUTH_NAME (auth), error.message);

1010

1011 if (send_error (auth, "Failed to generate challenge"))

1012 retval = TRUE; /\* retval is only about mem \*/

1013

1014 dbus_error_free (&error);

1015 goto out_4;

1016 }

1017 }

1018

1019 if (!\_dbus_string_init (&client_challenge))

1020 goto out_4;

1021

1022 if (!\_dbus_string_hex_encode (&tmp, 0, &client_challenge, 0))

1023 goto out_5;

1024

1025 if (!\_dbus_string_init (&correct_hash))

1026 goto out_5;

1027

1028 if (!sha1_compute_hash (auth, val,

1029 &server_challenge,

1030 &client_challenge,

1031 &correct_hash))

1032 goto out_6;

1033

1034 if (\_dbus_string_get_length (&correct_hash) == 0)

1035 {

1036 /\* couldn't find the cookie ID or something \*/

1037 if (send_error (auth, "Don't have the requested cookie ID"))

1038 retval = TRUE;

1039 goto out_6;

1040 }

1041

1042 \_dbus_string_set_length (&tmp, 0);

1043

1044 if (!\_dbus_string_copy (&client_challenge, 0, &tmp,

1045 \_dbus_string_get_length (&tmp)))

1046 goto out_6;

1047

1048 if (!\_dbus_string_append (&tmp, " "))

1049 goto out_6;

1050

1051 if (!\_dbus_string_copy (&correct_hash, 0, &tmp,

1052 \_dbus_string_get_length (&tmp)))

1053 goto out_6;

1054

1055 if (!send_data (auth, &tmp))

1056 goto out_6;

1057

1058 retval = TRUE;

1059

1060 out_6:

1061 \_dbus_string_zero (&correct_hash);

1062 \_dbus_string_free (&correct_hash);

1063 out_5:

1064 \_dbus_string_free (&client_challenge);

1065 out_4:

1066 \_dbus_string_zero (&tmp);

1067 \_dbus_string_free (&tmp);

1068 out_3:

1069 \_dbus_string_free (&server_challenge);

1070 out_2:

1071 \_dbus_string_free (&cookie_id_str);

1072 out_1:

1073 \_dbus_string_free (&context);

1074 out_0:

1075 return retval;

1076}

1077

1078static void

1079handle_client_shutdown_cookie_sha1_mech (DBusAuth \*auth)

1080{

1081 auth-\>cookie_id = -1;

1082 \_dbus_string_set_length (&auth-\>challenge, 0);

1083}

1084

1085/\*

1086 \* EXTERNAL mechanism

1087 \*/

1088

1089static dbus_bool_t

1090handle_server_data_external_mech (DBusAuth \*auth,

1091 const DBusString \*data)

1092{

1093 if (\_dbus_credentials_are_anonymous (auth-\>credentials))

1094 {

1095 \_dbus_verbose ("%s: no credentials, mechanism EXTERNAL can't authenticate\n",

1096 DBUS_AUTH_NAME (auth));

1097 return send_rejected (auth);

1098 }

1099

1100 if (\_dbus_string_get_length (data) \> 0)

1101 {

1102 if (\_dbus_string_get_length (&auth-\>identity) \> 0)

1103 {

1104 /\* Tried to send two auth identities, wtf \*/

1105 \_dbus_verbose ("%s: client tried to send auth identity, but we already have one\n",

1106 DBUS_AUTH_NAME (auth));

1107 return send_rejected (auth);

1108 }

1109 else

1110 {

1111 /\* this is our auth identity \*/

1112 if (!\_dbus_string_copy (data, 0, &auth-\>identity, 0))

1113 return FALSE;

1114 }

1115 }

1116

1117 /\* Poke client for an auth identity, if none given \*/

1118 if (\_dbus_string_get_length (&auth-\>identity) == 0 &&

1119 !auth-\>already_asked_for_initial_response)

1120 {

1121 if (send_data (auth, NULL))

1122 {

1123 \_dbus_verbose ("%s: sending empty challenge asking client for auth identity\n",

1124 DBUS_AUTH_NAME (auth));

1125 auth-\>already_asked_for_initial_response = TRUE;

1126 goto_state (auth, &server_state_waiting_for_data);

1127 return TRUE;

1128 }

1129 else

1130 return FALSE;

1131 }

1132

1133 \_dbus_credentials_clear (auth-\>desired_identity);

1134

1135 /\* If auth-\>identity is still empty here, then client

1136 \* responded with an empty string after we poked it for

1137 \* an initial response. This means to try to auth the

1138 \* identity provided in the credentials.

1139 \*/

1140 if (\_dbus_string_get_length (&auth-\>identity) == 0)

1141 {

1142 if (!\_dbus_credentials_add_credentials (auth-\>desired_identity,

1143 auth-\>credentials))

1144 {

1145 return FALSE; /\* OOM \*/

1146 }

1147 }

1148 else

1149 {

1150 DBusError error = DBUS_ERROR_INIT;

1151

1152 if (!\_dbus_credentials_add_from_user (auth-\>desired_identity,

1153 &auth-\>identity,

1154 DBUS_CREDENTIALS_ADD_FLAGS_NONE,

1155 &error))

1156 {

1157 if (dbus_error_has_name (&error, DBUS_ERROR_NO_MEMORY))

1158 {

1159 dbus_error_free (&error);

1160 return FALSE;

1161 }

1162

1163 \_dbus_verbose ("%s: could not get credentials from uid string: %s\n",

1164 DBUS_AUTH_NAME (auth), error.message);

1165 dbus_error_free (&error);

1166 return send_rejected (auth);

1167 }

1168 }

1169

1170 if (\_dbus_credentials_are_anonymous (auth-\>desired_identity))

1171 {

1172 \_dbus_verbose ("%s: desired user %s is no good\n",

1173 DBUS_AUTH_NAME (auth),

1174 \_dbus_string_get_const_data (&auth-\>identity));

1175 return send_rejected (auth);

1176 }

1177

1178 if (\_dbus_credentials_are_superset (auth-\>credentials,

1179 auth-\>desired_identity))

1180 {

1181 /\* client has authenticated \*/

1182 if (!\_dbus_credentials_add_credentials (auth-\>authorized_identity,

1183 auth-\>desired_identity))

1184 return FALSE;

1185

1186 /\* also copy misc process info from the socket credentials

1187 \*/

1188 if (!\_dbus_credentials_add_credential (auth-\>authorized_identity,

1189 DBUS_CREDENTIAL_UNIX_PROCESS_FD,

1190 auth-\>credentials))

1191 return FALSE;

1192

1193 if (!\_dbus_credentials_add_credential (auth-\>authorized_identity,

1194 DBUS_CREDENTIAL_UNIX_PROCESS_ID,

1195 auth-\>credentials))

1196 return FALSE;

1197

1198 if (!\_dbus_credentials_add_credential (auth-\>authorized_identity,

1199 DBUS_CREDENTIAL_ADT_AUDIT_DATA_ID,

1200 auth-\>credentials))

1201 return FALSE;

1202

1203 if (!\_dbus_credentials_add_credential (auth-\>authorized_identity,

1204 DBUS_CREDENTIAL_UNIX_GROUP_IDS,

1205 auth-\>credentials))

1206 return FALSE;

1207

1208 if (!\_dbus_credentials_add_credential (auth-\>authorized_identity,

1209 DBUS_CREDENTIAL_LINUX_SECURITY_LABEL,

1210 auth-\>credentials))

1211 return FALSE;

1212

1213 if (!send_ok (auth))

1214 return FALSE;

1215

1216 \_dbus_verbose ("%s: authenticated client based on socket credentials\n",

1217 DBUS_AUTH_NAME (auth));

1218

1219 return TRUE;

1220 }

1221 else

1222 {

1223 \_dbus_verbose ("%s: desired identity not found in socket credentials\n",

1224 DBUS_AUTH_NAME (auth));

1225 return send_rejected (auth);

1226 }

1227}

1228

1229static void

1230handle_server_shutdown_external_mech (DBusAuth \*auth)

1231{

1232

1233}

1234

1235static dbus_bool_t

1236handle_client_initial_response_external_mech (DBusAuth \*auth,

1237 DBusString \*response)

1238{

1239 /\* We always append our UID as an initial response, so the server

1240 \* doesn't have to send back an empty challenge to check whether we

1241 \* want to specify an identity. i.e. this avoids a round trip that

1242 \* the spec for the EXTERNAL mechanism otherwise requires.

1243 \*/

1244 DBusString plaintext;

1245

1246 if (!\_dbus_string_init (&plaintext))

1247 return FALSE;

1248

1249 if (!\_dbus_append_user_from_current_process (&plaintext))

1250 goto failed;

1251

1252 if (!\_dbus_string_hex_encode (&plaintext, 0,

1253 response,

1254 \_dbus_string_get_length (response)))

1255 goto failed;

1256

1257 \_dbus_string_free (&plaintext);

1258

1259 return TRUE;

1260

1261 failed:

1262 \_dbus_string_free (&plaintext);

1263 return FALSE;

1264}

1265

1266static dbus_bool_t

1267handle_client_data_external_mech (DBusAuth \*auth,

1268 const DBusString \*data)

1269{

1270

1271 return TRUE;

1272}

1273

1274static void

1275handle_client_shutdown_external_mech (DBusAuth \*auth)

1276{

1277

1278}

1279

1280/\*

1281 \* ANONYMOUS mechanism

1282 \*/

1283

1284static dbus_bool_t

1285handle_server_data_anonymous_mech (DBusAuth \*auth,

1286 const DBusString \*data)

1287{

1288 if (\_dbus_string_get_length (data) \> 0)

1289 {

1290 /\* Client is allowed to send "trace" data, the only defined

1291 \* meaning is that if it contains '@' it is an email address,

1292 \* and otherwise it is anything else, and it's supposed to be

1293 \* UTF-8

1294 \*/

1295 if (!\_dbus_string_validate_utf8 (data, 0, \_dbus_string_get_length (data)))

1296 {

1297 \_dbus_verbose ("%s: Received invalid UTF-8 trace data from ANONYMOUS client\n",

1298 DBUS_AUTH_NAME (auth));

1299 return send_rejected (auth);

1300 }

1301

1302 \_dbus_verbose ("%s: ANONYMOUS client sent trace string: '%s'\n",

1303 DBUS_AUTH_NAME (auth),

1304 \_dbus_string_get_const_data (data));

1305 }

1306

1307 /\* We want to be anonymous (clear in case some other protocol got midway through I guess) \*/

1308 \_dbus_credentials_clear (auth-\>desired_identity);

1309

1310 /\* Copy process ID (and PID FD) from the socket credentials

1311 \*/

1312 if (!\_dbus_credentials_add_credential (auth-\>authorized_identity,

1313 DBUS_CREDENTIAL_UNIX_PROCESS_FD,

1314 auth-\>credentials))

1315 return FALSE;

1316

1317 if (!\_dbus_credentials_add_credential (auth-\>authorized_identity,

1318 DBUS_CREDENTIAL_UNIX_PROCESS_ID,

1319 auth-\>credentials))

1320 return FALSE;

1321

1322 /\* Anonymous is always allowed \*/

1323 if (!send_ok (auth))

1324 return FALSE;

1325

1326 \_dbus_verbose ("%s: authenticated client as anonymous\n",

1327 DBUS_AUTH_NAME (auth));

1328

1329 return TRUE;

1330}

1331

1332static void

1333handle_server_shutdown_anonymous_mech (DBusAuth \*auth)

1334{

1335

1336}

1337

1338static dbus_bool_t

1339handle_client_initial_response_anonymous_mech (DBusAuth \*auth,

1340 DBusString \*response)

1341{

1342 /\* Our initial response is a "trace" string which must be valid UTF-8

1343 \* and must be an email address if it contains '@'.

1344 \* We just send the dbus implementation info, like a user-agent or

1345 \* something, because... why not. There's nothing guaranteed here

1346 \* though, we could change it later.

1347 \*/

1348 DBusString plaintext;

1349

1350 if (!\_dbus_string_init (&plaintext))

1351 return FALSE;

1352

1353 if (!\_dbus_string_append (&plaintext,

1354 "libdbus " DBUS_VERSION_STRING))

1355 goto failed;

1356

1357 if (!\_dbus_string_hex_encode (&plaintext, 0,

1358 response,

1359 \_dbus_string_get_length (response)))

1360 goto failed;

1361

1362 \_dbus_string_free (&plaintext);

1363

1364 return TRUE;

1365

1366 failed:

1367 \_dbus_string_free (&plaintext);

1368 return FALSE;

1369}

1370

1371static dbus_bool_t

1372handle_client_data_anonymous_mech (DBusAuth \*auth,

1373 const DBusString \*data)

1374{

1375

1376 return TRUE;

1377}

1378

1379static void

1380handle_client_shutdown_anonymous_mech (DBusAuth \*auth)

1381{

1382

1383}

1384

1385/\* Put mechanisms here in order of preference.

1386 \* Right now we have:

1387 \*

1388 \* - EXTERNAL checks socket credentials (or in the future, other info from the OS)

1389 \* - DBUS_COOKIE_SHA1 uses a cookie in the home directory, like xauth or ICE

1390 \* - ANONYMOUS checks nothing but doesn't auth the person as a user

1391 \*

1392 \* We might ideally add a mechanism to chain to Cyrus SASL so we can

1393 \* use its mechanisms as well.

1394 \*

1395 \*/

1396static const DBusAuthMechanismHandler

1397all_mechanisms\[\] = {

1398 { "EXTERNAL",

1399 handle_server_data_external_mech,

1400 NULL, NULL,

1401 handle_server_shutdown_external_mech,

1402 handle_client_initial_response_external_mech,

1403 handle_client_data_external_mech,

1404 NULL, NULL,

1405 handle_client_shutdown_external_mech },

1406 { "DBUS_COOKIE_SHA1",

1407 handle_server_data_cookie_sha1_mech,

1408 NULL, NULL,

1409 handle_server_shutdown_cookie_sha1_mech,

1410 handle_client_initial_response_cookie_sha1_mech,

1411 handle_client_data_cookie_sha1_mech,

1412 NULL, NULL,

1413 handle_client_shutdown_cookie_sha1_mech },

1414 { "ANONYMOUS",

1415 handle_server_data_anonymous_mech,

1416 NULL, NULL,

1417 handle_server_shutdown_anonymous_mech,

1418 handle_client_initial_response_anonymous_mech,

1419 handle_client_data_anonymous_mech,

1420 NULL, NULL,

1421 handle_client_shutdown_anonymous_mech },

1422 { NULL, NULL }

1423};

1424

1425static const DBusAuthMechanismHandler\*

1426find_mech (const DBusString \*name,

1427 char \*\*allowed_mechs)

1428{

1429 int i;

1430

1431 if (allowed_mechs != NULL &&

1432 !\_dbus_string_array_contains ((const char\*\*) allowed_mechs,

1433 \_dbus_string_get_const_data (name)))

1434 return NULL;

1435

1436 i = 0;

1437 while (all_mechanisms\[i\].mechanism != NULL)

1438 {

1439 if (\_dbus_string_equal_c_str (name,

1440 all_mechanisms\[i\].mechanism))

1441

1442 return &all_mechanisms\[i\];

1443

1444 ++i;

1445 }

1446

1447 return NULL;

1448}

1449

1450static dbus_bool_t

1451send_auth (DBusAuth \*auth, const DBusAuthMechanismHandler \*mech)

1452{

1453 DBusString auth_command;

1454

1455 if (!\_dbus_string_init (&auth_command))

1456 return FALSE;

1457

1458 if (!\_dbus_string_append (&auth_command,

1459 "AUTH "))

1460 {

1461 \_dbus_string_free (&auth_command);

1462 return FALSE;

1463 }

1464

1465 if (!\_dbus_string_append (&auth_command,

1466 mech-\>mechanism))

1467 {

1468 \_dbus_string_free (&auth_command);

1469 return FALSE;

1470 }

1471

1472 if (mech-\>client_initial_response_func != NULL)

1473 {

1474 if (!\_dbus_string_append (&auth_command, " "))

1475 {

1476 \_dbus_string_free (&auth_command);

1477 return FALSE;

1478 }

1479

1480 if (!(\* mech-\>client_initial_response_func) (auth, &auth_command))

1481 {

1482 \_dbus_string_free (&auth_command);

1483 return FALSE;

1484 }

1485 }

1486

1487 if (!\_dbus_string_append (&auth_command,

1488 "\r\n"))

1489 {

1490 \_dbus_string_free (&auth_command);

1491 return FALSE;

1492 }

1493

1494 if (!\_dbus_string_copy (&auth_command, 0,

1495 &auth-\>outgoing,

1496 \_dbus_string_get_length (&auth-\>outgoing)))

1497 {

1498 \_dbus_string_free (&auth_command);

1499 return FALSE;

1500 }

1501

1502 \_dbus_string_free (&auth_command);

1503 shutdown_mech (auth);

1504 auth-\>mech = mech;

1505 goto_state (auth, &client_state_waiting_for_data);

1506

1507 return TRUE;

1508}

1509

1510static dbus_bool_t

1511send_data (DBusAuth \*auth, DBusString \*data)

1512{

1513 int old_len;

1514

1515 if (data == NULL \|\| \_dbus_string_get_length (data) == 0)

1516 return \_dbus_string_append (&auth-\>outgoing, "DATA\r\n");

1517 else

1518 {

1519 old_len = \_dbus_string_get_length (&auth-\>outgoing);

1520 if (!\_dbus_string_append (&auth-\>outgoing, "DATA "))

1521 goto out;

1522

1523 if (!\_dbus_string_hex_encode (data, 0, &auth-\>outgoing,

1524 \_dbus_string_get_length (&auth-\>outgoing)))

1525 goto out;

1526

1527 if (!\_dbus_string_append (&auth-\>outgoing, "\r\n"))

1528 goto out;

1529

1530 return TRUE;

1531

1532 out:

1533 \_dbus_string_set_length (&auth-\>outgoing, old_len);

1534

1535 return FALSE;

1536 }

1537}

1538

1539static dbus_bool_t

1540send_rejected (DBusAuth \*auth)

1541{

1542 DBusString command;

1543 DBusAuthServer \*server_auth;

1544 int i;

1545

1546 if (!\_dbus_string_init (&command))

1547 return FALSE;

1548

1549 if (!\_dbus_string_append (&command,

1550 "REJECTED"))

1551 goto nomem;

1552

1553 for (i = 0; all_mechanisms\[i\].mechanism != NULL; i++)

1554 {

1555 /\* skip mechanisms that aren't allowed \*/

1556 if (auth-\>allowed_mechs != NULL &&

1557 !\_dbus_string_array_contains ((const char\*\*)auth-\>allowed_mechs,

1558 all_mechanisms\[i\].mechanism))

1559 continue;

1560

1561 if (!\_dbus_string_append (&command,

1562 " "))

1563 goto nomem;

1564

1565 if (!\_dbus_string_append (&command,

1566 all_mechanisms\[i\].mechanism))

1567 goto nomem;

1568 }

1569

1570 if (!\_dbus_string_append (&command, "\r\n"))

1571 goto nomem;

1572

1573 if (!\_dbus_string_copy (&command, 0, &auth-\>outgoing,

1574 \_dbus_string_get_length (&auth-\>outgoing)))

1575 goto nomem;

1576

1577 shutdown_mech (auth);

1578

1579 \_dbus_assert (DBUS_AUTH_IS_SERVER (auth));

1580 server_auth = DBUS_AUTH_SERVER (auth);

1581 server_auth-\>failures += 1;

1582

1583 if (server_auth-\>failures \>= server_auth-\>max_failures)

1584 goto_state (auth, &common_state_need_disconnect);

1585 else

1586 goto_state (auth, &server_state_waiting_for_auth);

1587

1588 \_dbus_string_free (&command);

1589

1590 return TRUE;

1591

1592 nomem:

1593 \_dbus_string_free (&command);

1594 return FALSE;

1595}

1596

1597static dbus_bool_t

1598send_error (DBusAuth \*auth, const char \*message)

1599{

1600 return \_dbus_string_append_printf (&auth-\>outgoing,

1601 "ERROR \\%s\\\r\n", message);

1602}

1603

1604static dbus_bool_t

1605send_ok (DBusAuth \*auth)

1606{

1607 int orig_len;

1608

1609 orig_len = \_dbus_string_get_length (&auth-\>outgoing);

1610

1611 if (\_dbus_string_append (&auth-\>outgoing, "OK ") &&

1612 \_dbus_string_copy (& DBUS_AUTH_SERVER (auth)-\>guid,

1613 0,

1614 &auth-\>outgoing,

1615 \_dbus_string_get_length (&auth-\>outgoing)) &&

1616 \_dbus_string_append (&auth-\>outgoing, "\r\n"))

1617 {

1618 goto_state (auth, &server_state_waiting_for_begin);

1619 return TRUE;

1620 }

1621 else

1622 {

1623 \_dbus_string_set_length (&auth-\>outgoing, orig_len);

1624 return FALSE;

1625 }

1626}

1627

1628static dbus_bool_t

1629send_begin (DBusAuth \*auth)

1630{

1631

1632 if (!\_dbus_string_append (&auth-\>outgoing,

1633 "BEGIN\r\n"))

1634 return FALSE;

1635

1636 goto_state (auth, &common_state_authenticated);

1637 return TRUE;

1638}

1639

1640static dbus_bool_t

1641process_ok(DBusAuth \*auth,

1642 const DBusString \*args_from_ok) {

1643

1644 int end_of_hex;

1645

1646 /\* "args_from_ok" should be the GUID, whitespace already pulled off the front \*/

1647 \_dbus_assert (\_dbus_string_get_length (& DBUS_AUTH_CLIENT (auth)-\>guid_from_server) == 0);

1648

1649 /\* We decode the hex string to binary, using guid_from_server as scratch... \*/

1650

1651 end_of_hex = 0;

1652 if (!\_dbus_string_hex_decode (args_from_ok, 0, &end_of_hex,

1653 & DBUS_AUTH_CLIENT (auth)-\>guid_from_server, 0))

1654 return FALSE;

1655

1656 /\* now clear out the scratch \*/

1657 \_dbus_string_set_length (& DBUS_AUTH_CLIENT (auth)-\>guid_from_server, 0);

1658

1659 if (end_of_hex != \_dbus_string_get_length (args_from_ok) \|\|

1660 end_of_hex == 0)

1661 {

1662 \_dbus_verbose ("Bad GUID from server, parsed %d bytes and had %d bytes from server\n",

1663 end_of_hex, \_dbus_string_get_length (args_from_ok));

1664 goto_state (auth, &common_state_need_disconnect);

1665 return TRUE;

1666 }

1667

1668 if (!\_dbus_string_copy (args_from_ok, 0, &DBUS_AUTH_CLIENT (auth)-\>guid_from_server, 0)) {

1669 \_dbus_string_set_length (& DBUS_AUTH_CLIENT (auth)-\>guid_from_server, 0);

1670 return FALSE;

1671 }

1672

1673 \_dbus_verbose ("Got GUID '%s' from the server\n",

1674 \_dbus_string_get_const_data (& DBUS_AUTH_CLIENT (auth)-\>guid_from_server));

1675

1676 if (auth-\>unix_fd_possible)

1677 {

1678 if (!send_negotiate_unix_fd (auth))

1679 {

1680 \_dbus_string_set_length (& DBUS_AUTH_CLIENT (auth)-\>guid_from_server, 0);

1681 return FALSE;

1682 }

1683

1684 return TRUE;

1685 }

1686

1687 \_dbus_verbose("Not negotiating unix fd passing, since not possible\n");

1688

1689 if (!send_begin (auth))

1690 {

1691 \_dbus_string_set_length (& DBUS_AUTH_CLIENT (auth)-\>guid_from_server, 0);

1692 return FALSE;

1693 }

1694

1695 return TRUE;

1696}

1697

1698static dbus_bool_t

1699send_cancel (DBusAuth \*auth)

1700{

1701 if (\_dbus_string_append (&auth-\>outgoing, "CANCEL\r\n"))

1702 {

1703 goto_state (auth, &client_state_waiting_for_reject);

1704 return TRUE;

1705 }

1706 else

1707 return FALSE;

1708}

1709

1710static dbus_bool_t

1711process_data (DBusAuth \*auth,

1712 const DBusString \*args,

1713 DBusAuthDataFunction data_func)

1714{

1715 int end;

1716 DBusString decoded;

1717

1718 if (!\_dbus_string_init (&decoded))

1719 return FALSE;

1720

1721 if (!\_dbus_string_hex_decode (args, 0, &end, &decoded, 0))

1722 {

1723 \_dbus_string_free (&decoded);

1724 return FALSE;

1725 }

1726

1727 if (\_dbus_string_get_length (args) != end)

1728 {

1729 \_dbus_string_free (&decoded);

1730 if (!send_error (auth, "Invalid hex encoding"))

1731 return FALSE;

1732

1733 return TRUE;

1734 }

1735

1736\#ifdef DBUS_ENABLE_VERBOSE_MODE

1737 if (\_dbus_string_validate_ascii (&decoded, 0,

1738 \_dbus_string_get_length (&decoded)))

1739 \_dbus_verbose ("%s: data: '%s'\n",

1740 DBUS_AUTH_NAME (auth),

1741 \_dbus_string_get_const_data (&decoded));

1742\#endif

1743

1744 if (!(\* data_func) (auth, &decoded))

1745 {

1746 \_dbus_string_free (&decoded);

1747 return FALSE;

1748 }

1749

1750 \_dbus_string_free (&decoded);

1751 return TRUE;

1752}

1753

1754static dbus_bool_t

1755send_negotiate_unix_fd (DBusAuth \*auth)

1756{

1757 if (!\_dbus_string_append (&auth-\>outgoing,

1758 "NEGOTIATE_UNIX_FD\r\n"))

1759 return FALSE;

1760

1761 goto_state (auth, &client_state_waiting_for_agree_unix_fd);

1762 return TRUE;

1763}

1764

1765static dbus_bool_t

1766send_agree_unix_fd (DBusAuth \*auth)

1767{

1768 \_dbus_assert(auth-\>unix_fd_possible);

1769

1770 auth-\>unix_fd_negotiated = TRUE;

1771 \_dbus_verbose("Agreed to UNIX FD passing\n");

1772

1773 if (!\_dbus_string_append (&auth-\>outgoing,

1774 "AGREE_UNIX_FD\r\n"))

1775 return FALSE;

1776

1777 goto_state (auth, &server_state_waiting_for_begin);

1778 return TRUE;

1779}

1780

1781static dbus_bool_t

1782handle_auth (DBusAuth \*auth, const DBusString \*args)

1783{

1784 if (\_dbus_string_get_length (args) == 0)

1785 {

1786 /\* No args to the auth, send mechanisms \*/

1787 if (!send_rejected (auth))

1788 return FALSE;

1789

1790 return TRUE;

1791 }

1792 else

1793 {

1794 int i;

1795 DBusString mech;

1796 DBusString hex_response;

1797

1798 \_dbus_string_find_blank (args, 0, &i);

1799

1800 if (!\_dbus_string_init (&mech))

1801 return FALSE;

1802

1803 if (!\_dbus_string_init (&hex_response))

1804 {

1805 \_dbus_string_free (&mech);

1806 return FALSE;

1807 }

1808

1809 if (!\_dbus_string_copy_len (args, 0, i, &mech, 0))

1810 goto failed;

1811

1812 \_dbus_string_skip_blank (args, i, &i);

1813 if (!\_dbus_string_copy (args, i, &hex_response, 0))

1814 goto failed;

1815

1816 auth-\>mech = find_mech (&mech, auth-\>allowed_mechs);

1817 if (auth-\>mech != NULL)

1818 {

1819 \_dbus_verbose ("%s: Trying mechanism %s\n",

1820 DBUS_AUTH_NAME (auth),

1821 auth-\>mech-\>mechanism);

1822

1823 if (!process_data (auth, &hex_response,

1824 auth-\>mech-\>server_data_func))

1825 goto failed;

1826 }

1827 else

1828 {

1829 /\* Unsupported mechanism \*/

1830 \_dbus_verbose ("%s: Unsupported mechanism %s\n",

1831 DBUS_AUTH_NAME (auth),

1832 \_dbus_string_get_const_data (&mech));

1833

1834 if (!send_rejected (auth))

1835 goto failed;

1836 }

1837

1838 \_dbus_string_free (&mech);

1839 \_dbus_string_free (&hex_response);

1840

1841 return TRUE;

1842

1843 failed:

1844 auth-\>mech = NULL;

1845 \_dbus_string_free (&mech);

1846 \_dbus_string_free (&hex_response);

1847 return FALSE;

1848 }

1849}

1850

1851static dbus_bool_t

1852handle_server_state_waiting_for_auth (DBusAuth \*auth,

1853 DBusAuthCommand command,

1854 const DBusString \*args)

1855{

1856 switch (command)

1857 {

1858 case DBUS_AUTH_COMMAND_AUTH:

1859 return handle_auth (auth, args);

1860

1861 case DBUS_AUTH_COMMAND_CANCEL:

1862 case DBUS_AUTH_COMMAND_DATA:

1863 return send_error (auth, "Not currently in an auth conversation");

1864

1865 case DBUS_AUTH_COMMAND_BEGIN:

1866 goto_state (auth, &common_state_need_disconnect);

1867 return TRUE;

1868

1869 case DBUS_AUTH_COMMAND_ERROR:

1870 return send_rejected (auth);

1871

1872 case DBUS_AUTH_COMMAND_NEGOTIATE_UNIX_FD:

1873 return send_error (auth, "Need to authenticate first");

1874

1875 case DBUS_AUTH_COMMAND_REJECTED:

1876 case DBUS_AUTH_COMMAND_OK:

1877 case DBUS_AUTH_COMMAND_UNKNOWN:

1878 case DBUS_AUTH_COMMAND_AGREE_UNIX_FD:

1879 default:

1880 return send_error (auth, "Unknown command");

1881 }

1882}

1883

1884static dbus_bool_t

1885handle_server_state_waiting_for_data (DBusAuth \*auth,

1886 DBusAuthCommand command,

1887 const DBusString \*args)

1888{

1889 switch (command)

1890 {

1891 case DBUS_AUTH_COMMAND_AUTH:

1892 return send_error (auth, "Sent AUTH while another AUTH in progress");

1893

1894 case DBUS_AUTH_COMMAND_CANCEL:

1895 case DBUS_AUTH_COMMAND_ERROR:

1896 return send_rejected (auth);

1897

1898 case DBUS_AUTH_COMMAND_DATA:

1899 return process_data (auth, args, auth-\>mech-\>server_data_func);

1900

1901 case DBUS_AUTH_COMMAND_BEGIN:

1902 goto_state (auth, &common_state_need_disconnect);

1903 return TRUE;

1904

1905 case DBUS_AUTH_COMMAND_NEGOTIATE_UNIX_FD:

1906 return send_error (auth, "Need to authenticate first");

1907

1908 case DBUS_AUTH_COMMAND_REJECTED:

1909 case DBUS_AUTH_COMMAND_OK:

1910 case DBUS_AUTH_COMMAND_UNKNOWN:

1911 case DBUS_AUTH_COMMAND_AGREE_UNIX_FD:

1912 default:

1913 return send_error (auth, "Unknown command");

1914 }

1915}

1916

1917static dbus_bool_t

1918handle_server_state_waiting_for_begin (DBusAuth \*auth,

1919 DBusAuthCommand command,

1920 const DBusString \*args)

1921{

1922 switch (command)

1923 {

1924 case DBUS_AUTH_COMMAND_AUTH:

1925 return send_error (auth, "Sent AUTH while expecting BEGIN");

1926

1927 case DBUS_AUTH_COMMAND_DATA:

1928 return send_error (auth, "Sent DATA while expecting BEGIN");

1929

1930 case DBUS_AUTH_COMMAND_BEGIN:

1931 goto_state (auth, &common_state_authenticated);

1932 return TRUE;

1933

1934 case DBUS_AUTH_COMMAND_NEGOTIATE_UNIX_FD:

1935 if (auth-\>unix_fd_possible)

1936 return send_agree_unix_fd(auth);

1937 else

1938 return send_error(auth, "Unix FD passing not supported, not authenticated or otherwise not possible");

1939

1940 case DBUS_AUTH_COMMAND_REJECTED:

1941 case DBUS_AUTH_COMMAND_OK:

1942 case DBUS_AUTH_COMMAND_UNKNOWN:

1943 case DBUS_AUTH_COMMAND_AGREE_UNIX_FD:

1944 default:

1945 return send_error (auth, "Unknown command");

1946

1947 case DBUS_AUTH_COMMAND_CANCEL:

1948 case DBUS_AUTH_COMMAND_ERROR:

1949 return send_rejected (auth);

1950 }

1951}

1952

1953/\* return FALSE if no memory, TRUE if all OK \*/

1954static dbus_bool_t

1955get_word (const DBusString \*str,

1956 int \*start,

1957 DBusString \*word)

1958{

1959 int i;

1960

1961 \_dbus_string_skip_blank (str, \*start, start);

1962 \_dbus_string_find_blank (str, \*start, &i);

1963

1964 if (i \> \*start)

1965 {

1966 if (!\_dbus_string_copy_len (str, \*start, i - \*start, word, 0))

1967 return FALSE;

1968

1969 \*start = i;

1970 }

1971

1972 return TRUE;

1973}

1974

1975static dbus_bool_t

1976record_mechanisms (DBusAuth \*auth,

1977 const DBusString \*args)

1978{

1979 int next;

1980 int len;

1981

1982 if (auth-\>already_got_mechanisms)

1983 return TRUE;

1984

1985 len = \_dbus_string_get_length (args);

1986

1987 next = 0;

1988 while (next \< len)

1989 {

1990 DBusString m;

1991 const DBusAuthMechanismHandler \*mech;

1992

1993 if (!\_dbus_string_init (&m))

1994 goto nomem;

1995

1996 if (!get_word (args, &next, &m))

1997 {

1998 \_dbus_string_free (&m);

1999 goto nomem;

2000 }

2001

2002 mech = find_mech (&m, auth-\>allowed_mechs);

2003

2004 if (mech != NULL)

2005 {

2006 /\* FIXME right now we try mechanisms in the order

2007 \* the server lists them; should we do them in

2008 \* some more deterministic order?

2009 \*

2010 \* Probably in all_mechanisms order, our order of

2011 \* preference. Of course when the server is us,

2012 \* it lists things in that order anyhow.

2013 \*/

2014

2015 if (mech != &all_mechanisms\[0\])

2016 {

2017 \_dbus_verbose ("%s: Adding mechanism %s to list we will try\n",

2018 DBUS_AUTH_NAME (auth), mech-\>mechanism);

2019

2020 if (!\_dbus_list_append (& DBUS_AUTH_CLIENT (auth)-\>mechs_to_try,

2021 (void\*) mech))

2022 {

2023 \_dbus_string_free (&m);

2024 goto nomem;

2025 }

2026 }

2027 else

2028 {

2029 \_dbus_verbose ("%s: Already tried mechanism %s; not adding to list we will try\n",

2030 DBUS_AUTH_NAME (auth), mech-\>mechanism);

2031 }

2032 }

2033 else

2034 {

2035 \_dbus_verbose ("%s: Server offered mechanism \\%s\\ that we don't know how to use\n",

2036 DBUS_AUTH_NAME (auth),

2037 \_dbus_string_get_const_data (&m));

2038 }

2039

2040 \_dbus_string_free (&m);

2041 }

2042

2043 auth-\>already_got_mechanisms = TRUE;

2044

2045 return TRUE;

2046

2047 nomem:

2048 \_dbus_list_clear (& DBUS_AUTH_CLIENT (auth)-\>mechs_to_try);

2049

2050 return FALSE;

2051}

2052

2053static dbus_bool_t

2054process_rejected (DBusAuth \*auth, const DBusString \*args)

2055{

2056 const DBusAuthMechanismHandler \*mech;

2057 DBusAuthClient \*client;

2058

2059 client = DBUS_AUTH_CLIENT (auth);

2060

2061 if (!auth-\>already_got_mechanisms)

2062 {

2063 if (!record_mechanisms (auth, args))

2064 return FALSE;

2065 }

2066

2067 if (DBUS_AUTH_CLIENT (auth)-\>mechs_to_try != NULL)

2068 {

2069 mech = client-\>mechs_to_try-\>data;

2070

2071 if (!send_auth (auth, mech))

2072 return FALSE;

2073

2074 \_dbus_list_pop_first (&client-\>mechs_to_try);

2075

2076 \_dbus_verbose ("%s: Trying mechanism %s\n",

2077 DBUS_AUTH_NAME (auth),

2078 mech-\>mechanism);

2079 }

2080 else

2081 {

2082 /\* Give up \*/

2083 \_dbus_verbose ("%s: Disconnecting because we are out of mechanisms to try using\n",

2084 DBUS_AUTH_NAME (auth));

2085 goto_state (auth, &common_state_need_disconnect);

2086 }

2087

2088 return TRUE;

2089}

2090

2091

2092static dbus_bool_t

2093handle_client_state_waiting_for_data (DBusAuth \*auth,

2094 DBusAuthCommand command,

2095 const DBusString \*args)

2096{

2097 \_dbus_assert (auth-\>mech != NULL);

2098

2099 switch (command)

2100 {

2101 case DBUS_AUTH_COMMAND_DATA:

2102 return process_data (auth, args, auth-\>mech-\>client_data_func);

2103

2104 case DBUS_AUTH_COMMAND_REJECTED:

2105 return process_rejected (auth, args);

2106

2107 case DBUS_AUTH_COMMAND_OK:

2108 return process_ok(auth, args);

2109

2110 case DBUS_AUTH_COMMAND_ERROR:

2111 return send_cancel (auth);

2112

2113 case DBUS_AUTH_COMMAND_AUTH:

2114 case DBUS_AUTH_COMMAND_CANCEL:

2115 case DBUS_AUTH_COMMAND_BEGIN:

2116 case DBUS_AUTH_COMMAND_UNKNOWN:

2117 case DBUS_AUTH_COMMAND_NEGOTIATE_UNIX_FD:

2118 case DBUS_AUTH_COMMAND_AGREE_UNIX_FD:

2119 default:

2120 return send_error (auth, "Unknown command");

2121 }

2122}

2123

2124static dbus_bool_t

2125handle_client_state_waiting_for_ok (DBusAuth \*auth,

2126 DBusAuthCommand command,

2127 const DBusString \*args)

2128{

2129 switch (command)

2130 {

2131 case DBUS_AUTH_COMMAND_REJECTED:

2132 return process_rejected (auth, args);

2133

2134 case DBUS_AUTH_COMMAND_OK:

2135 return process_ok(auth, args);

2136

2137 case DBUS_AUTH_COMMAND_DATA:

2138 case DBUS_AUTH_COMMAND_ERROR:

2139 return send_cancel (auth);

2140

2141 case DBUS_AUTH_COMMAND_AUTH:

2142 case DBUS_AUTH_COMMAND_CANCEL:

2143 case DBUS_AUTH_COMMAND_BEGIN:

2144 case DBUS_AUTH_COMMAND_UNKNOWN:

2145 case DBUS_AUTH_COMMAND_NEGOTIATE_UNIX_FD:

2146 case DBUS_AUTH_COMMAND_AGREE_UNIX_FD:

2147 default:

2148 return send_error (auth, "Unknown command");

2149 }

2150}

2151

2152static dbus_bool_t

2153handle_client_state_waiting_for_reject (DBusAuth \*auth,

2154 DBusAuthCommand command,

2155 const DBusString \*args)

2156{

2157 switch (command)

2158 {

2159 case DBUS_AUTH_COMMAND_REJECTED:

2160 return process_rejected (auth, args);

2161

2162 case DBUS_AUTH_COMMAND_AUTH:

2163 case DBUS_AUTH_COMMAND_CANCEL:

2164 case DBUS_AUTH_COMMAND_DATA:

2165 case DBUS_AUTH_COMMAND_BEGIN:

2166 case DBUS_AUTH_COMMAND_OK:

2167 case DBUS_AUTH_COMMAND_ERROR:

2168 case DBUS_AUTH_COMMAND_UNKNOWN:

2169 case DBUS_AUTH_COMMAND_NEGOTIATE_UNIX_FD:

2170 case DBUS_AUTH_COMMAND_AGREE_UNIX_FD:

2171 default:

2172 goto_state (auth, &common_state_need_disconnect);

2173 return TRUE;

2174 }

2175}

2176

2177static dbus_bool_t

2178handle_client_state_waiting_for_agree_unix_fd(DBusAuth \*auth,

2179 DBusAuthCommand command,

2180 const DBusString \*args)

2181{

2182 switch (command)

2183 {

2184 case DBUS_AUTH_COMMAND_AGREE_UNIX_FD:

2185 \_dbus_assert(auth-\>unix_fd_possible);

2186 auth-\>unix_fd_negotiated = TRUE;

2187 \_dbus_verbose("Successfully negotiated UNIX FD passing\n");

2188 return send_begin (auth);

2189

2190 case DBUS_AUTH_COMMAND_ERROR:

2191 \_dbus_assert(auth-\>unix_fd_possible);

2192 auth-\>unix_fd_negotiated = FALSE;

2193 \_dbus_verbose("Failed to negotiate UNIX FD passing\n");

2194 return send_begin (auth);

2195

2196 case DBUS_AUTH_COMMAND_OK:

2197 case DBUS_AUTH_COMMAND_DATA:

2198 case DBUS_AUTH_COMMAND_REJECTED:

2199 case DBUS_AUTH_COMMAND_AUTH:

2200 case DBUS_AUTH_COMMAND_CANCEL:

2201 case DBUS_AUTH_COMMAND_BEGIN:

2202 case DBUS_AUTH_COMMAND_UNKNOWN:

2203 case DBUS_AUTH_COMMAND_NEGOTIATE_UNIX_FD:

2204 default:

2205 return send_error (auth, "Unknown command");

2206 }

2207}

2208

2212typedef struct {

2213 const char \*name;

2214 DBusAuthCommand command;

2215} DBusAuthCommandName;

2216

2217static const DBusAuthCommandName auth_command_names\[\] = {

2218 { "AUTH", DBUS_AUTH_COMMAND_AUTH },

2219 { "CANCEL", DBUS_AUTH_COMMAND_CANCEL },

2220 { "DATA", DBUS_AUTH_COMMAND_DATA },

2221 { "BEGIN", DBUS_AUTH_COMMAND_BEGIN },

2222 { "REJECTED", DBUS_AUTH_COMMAND_REJECTED },

2223 { "OK", DBUS_AUTH_COMMAND_OK },

2224 { "ERROR", DBUS_AUTH_COMMAND_ERROR },

2225 { "NEGOTIATE_UNIX_FD", DBUS_AUTH_COMMAND_NEGOTIATE_UNIX_FD },

2226 { "AGREE_UNIX_FD", DBUS_AUTH_COMMAND_AGREE_UNIX_FD }

2227};

2228

2229static DBusAuthCommand

2230lookup_command_from_name (DBusString \*command)

2231{

2232 int i;

2233

2234 for (i = 0; i \< \_DBUS_N_ELEMENTS (auth_command_names); i++)

2235 {

2236 if (\_dbus_string_equal_c_str (command,

2237 auth_command_names\[i\].name))

2238 return auth_command_names\[i\].command;

2239 }

2240

2241 return DBUS_AUTH_COMMAND_UNKNOWN;

2242}

2243

2244static void

2245goto_state (DBusAuth \*auth,

2246 const DBusAuthStateData \*state)

2247{

2248 \_dbus_verbose ("%s: going from state %s to state %s\n",

2249 DBUS_AUTH_NAME (auth),

2250 auth-\>state-\>name,

2251 state-\>name);

2252

2253 auth-\>state = state;

2254}

2255

2256/\* returns whether to call it again right away \*/

2257static dbus_bool_t

2258process_command (DBusAuth \*auth)

2259{

2260 DBusAuthCommand command;

2261 DBusString line;

2262 DBusString args;

2263 int eol;

2264 int i, j;

2265 dbus_bool_t retval;

2266

2267 /\* \_dbus_verbose ("%s: trying process_command()\n"); \*/

2268

2269 retval = FALSE;

2270

2271 eol = 0;

2272 if (!\_dbus_string_find (&auth-\>incoming, 0, "\r\n", &eol))

2273 return FALSE;

2274

2275 if (!\_dbus_string_init (&line))

2276 {

2277 auth-\>needed_memory = TRUE;

2278 return FALSE;

2279 }

2280

2281 if (!\_dbus_string_init (&args))

2282 {

2283 \_dbus_string_free (&line);

2284 auth-\>needed_memory = TRUE;

2285 return FALSE;

2286 }

2287

2288 if (!\_dbus_string_copy_len (&auth-\>incoming, 0, eol, &line, 0))

2289 goto out;

2290

2291 if (!\_dbus_string_validate_ascii (&line, 0,

2292 \_dbus_string_get_length (&line)))

2293 {

2294 \_dbus_verbose ("%s: Command contained non-ASCII chars or embedded nul\n",

2295 DBUS_AUTH_NAME (auth));

2296 if (!send_error (auth, "Command contained non-ASCII"))

2297 goto out;

2298 else

2299 goto next_command;

2300 }

2301

2302 \_dbus_verbose ("%s: got command \\%s\\\n",

2303 DBUS_AUTH_NAME (auth),

2304 \_dbus_string_get_const_data (&line));

2305

2306 \_dbus_string_find_blank (&line, 0, &i);

2307 \_dbus_string_skip_blank (&line, i, &j);

2308

2309 if (j \> i)

2310 \_dbus_string_delete (&line, i, j - i);

2311

2312 if (!\_dbus_string_move (&line, i, &args, 0))

2313 goto out;

2314

2315 /\* FIXME 1.0 we should probably validate that only the allowed

2316 \* chars are in the command name

2317 \*/

2318

2319 command = lookup_command_from_name (&line);

2320 if (!(\* auth-\>state-\>handler) (auth, command, &args))

2321 goto out;

2322

2323 next_command:

2324

2325 /\* We've succeeded in processing the whole command so drop it out

2326 \* of the incoming buffer and return TRUE to try another command.

2327 \*/

2328

2329 \_dbus_string_delete (&auth-\>incoming, 0, eol);

2330

2331 /\* kill the \r\n \*/

2332 \_dbus_string_delete (&auth-\>incoming, 0, 2);

2333

2334 retval = TRUE;

2335

2336 out:

2337 \_dbus_string_free (&args);

2338 \_dbus_string_free (&line);

2339

2340 if (!retval)

2341 auth-\>needed_memory = TRUE;

2342 else

2343 auth-\>needed_memory = FALSE;

2344

2345 return retval;

2346}

2347

2348

2363DBusAuth\*

2364\_dbus_auth_server_new (const DBusString \*guid)

2365{

2366 DBusAuth \*auth;

2367 DBusAuthServer \*server_auth;

2368 DBusString guid_copy;

2369

2370 if (!\_dbus_string_init (&guid_copy))

2371 return NULL;

2372

2373 if (!\_dbus_string_copy (guid, 0, &guid_copy, 0))

2374 {

2375 \_dbus_string_free (&guid_copy);

2376 return NULL;

2377 }

2378

2379 auth = \_dbus_auth_new (sizeof (DBusAuthServer));

2380 if (auth == NULL)

2381 {

2382 \_dbus_string_free (&guid_copy);

2383 return NULL;

2384 }

2385

2386 auth-\>side = auth_side_server;

2387 auth-\>state = &server_state_waiting_for_auth;

2388

2389 server_auth = DBUS_AUTH_SERVER (auth);

2390

2391 server_auth-\>guid = guid_copy;

2392

2393 /\* perhaps this should be per-mechanism with a lower

2394 \* max

2395 \*/

2396 server_auth-\>failures = 0;

2397 server_auth-\>max_failures = 6;

2398

2399 return auth;

2400}

2401

2409DBusAuth\*

2410\_dbus_auth_client_new (void)

2411{

2412 DBusAuth \*auth;

2413 DBusString guid_str;

2414

2415 if (!\_dbus_string_init (&guid_str))

2416 return NULL;

2417

2418 auth = \_dbus_auth_new (sizeof (DBusAuthClient));

2419 if (auth == NULL)

2420 {

2421 \_dbus_string_free (&guid_str);

2422 return NULL;

2423 }

2424

2425 DBUS_AUTH_CLIENT (auth)-\>guid_from_server = guid_str;

2426

2427 auth-\>side = auth_side_client;

2428 auth-\>state = &client_state_need_send_auth;

2429

2430 /\* Start the auth conversation by sending AUTH for our default

2431 \* mechanism \*/

2432 if (!send_auth (auth, &all_mechanisms\[0\]))

2433 {

2434 \_dbus_auth_unref (auth);

2435 return NULL;

2436 }

2437

2438 return auth;

2439}

2440

2447DBusAuth \*

2448\_dbus_auth_ref (DBusAuth \*auth)

2449{

2450 \_dbus_assert (auth != NULL);

2451

2452 auth-\>refcount += 1;

2453

2454 return auth;

2455}

2456

2462void

2463\_dbus_auth_unref (DBusAuth \*auth)

2464{

2465 \_dbus_assert (auth != NULL);

2466 \_dbus_assert (auth-\>refcount \> 0);

2467

2468 auth-\>refcount -= 1;

2469 if (auth-\>refcount == 0)

2470 {

2471 shutdown_mech (auth);

2472

2473 if (DBUS_AUTH_IS_CLIENT (auth))

2474 {

2475 \_dbus_string_free (& DBUS_AUTH_CLIENT (auth)-\>guid_from_server);

2476 \_dbus_list_clear (& DBUS_AUTH_CLIENT (auth)-\>mechs_to_try);

2477 }

2478 else

2479 {

2480 \_dbus_assert (DBUS_AUTH_IS_SERVER (auth));

2481

2482 \_dbus_string_free (& DBUS_AUTH_SERVER (auth)-\>guid);

2483 }

2484

2485 if (auth-\>keyring)

2486 \_dbus_keyring_unref (auth-\>keyring);

2487

2488 \_dbus_string_free (&auth-\>context);

2489 \_dbus_string_free (&auth-\>challenge);

2490 \_dbus_string_free (&auth-\>identity);

2491 \_dbus_string_free (&auth-\>incoming);

2492 \_dbus_string_free (&auth-\>outgoing);

2493

2494 dbus_free_string_array (auth-\>allowed_mechs);

2495

2496 \_dbus_credentials_unref (auth-\>credentials);

2497 \_dbus_credentials_unref (auth-\>authorized_identity);

2498 \_dbus_credentials_unref (auth-\>desired_identity);

2499

2500 dbus_free (auth);

2501 }

2502}

2503

2512dbus_bool_t

2513\_dbus_auth_set_mechanisms (DBusAuth \*auth,

2514 const char \*\*mechanisms)

2515{

2516 char \*\*copy;

2517

2518 if (mechanisms != NULL)

2519 {

2520 copy = \_dbus_dup_string_array (mechanisms);

2521 if (copy == NULL)

2522 return FALSE;

2523 }

2524 else

2525 copy = NULL;

2526

2527 dbus_free_string_array (auth-\>allowed_mechs);

2528

2529 auth-\>allowed_mechs = copy;

2530

2531 return TRUE;

2532}

2533

2538\#define DBUS_AUTH_IN_END_STATE(auth) ((auth)-\>state-\>handler == NULL)

2539

2547DBusAuthState

2548\_dbus_auth_do_work (DBusAuth \*auth)

2549{

2550 auth-\>needed_memory = FALSE;

2551

2552 /\* Max amount we'll buffer up before deciding someone's on crack \*/

2553\#define MAX_BUFFER (16 \* \_DBUS_ONE_KILOBYTE)

2554

2555 do

2556 {

2557 if (DBUS_AUTH_IN_END_STATE (auth))

2558 break;

2559

2560 if (\_dbus_string_get_length (&auth-\>incoming) \> MAX_BUFFER \|\|

2561 \_dbus_string_get_length (&auth-\>outgoing) \> MAX_BUFFER)

2562 {

2563 goto_state (auth, &common_state_need_disconnect);

2564 \_dbus_verbose ("%s: Disconnecting due to excessive data buffered in auth phase\n",

2565 DBUS_AUTH_NAME (auth));

2566 break;

2567 }

2568 }

2569 while (process_command (auth));

2570

2571 if (auth-\>needed_memory)

2572 return DBUS_AUTH_STATE_WAITING_FOR_MEMORY;

2573 else if (\_dbus_string_get_length (&auth-\>outgoing) \> 0)

2574 return DBUS_AUTH_STATE_HAVE_BYTES_TO_SEND;

2575 else if (auth-\>state == &common_state_need_disconnect)

2576 return DBUS_AUTH_STATE_NEED_DISCONNECT;

2577 else if (auth-\>state == &common_state_authenticated)

2578 return DBUS_AUTH_STATE_AUTHENTICATED;

2579 else return DBUS_AUTH_STATE_WAITING_FOR_INPUT;

2580}

2581

2591dbus_bool_t

2592\_dbus_auth_get_bytes_to_send (DBusAuth \*auth,

2593 const DBusString \*\*str)

2594{

2595 \_dbus_assert (auth != NULL);

2596 \_dbus_assert (str != NULL);

2597

2598 \*str = NULL;

2599

2600 if (\_dbus_string_get_length (&auth-\>outgoing) == 0)

2601 return FALSE;

2602

2603 \*str = &auth-\>outgoing;

2604

2605 return TRUE;

2606}

2607

2616void

2617\_dbus_auth_bytes_sent (DBusAuth \*auth,

2618 int bytes_sent)

2619{

2620 \_dbus_verbose ("%s: Sent %d bytes of: %s\n",

2621 DBUS_AUTH_NAME (auth),

2622 bytes_sent,

2623 \_dbus_string_get_const_data (&auth-\>outgoing));

2624

2625 \_dbus_string_delete (&auth-\>outgoing,

2626 0, bytes_sent);

2627}

2628

2636void

2637\_dbus_auth_get_buffer (DBusAuth \*auth,

2638 DBusString \*\*buffer)

2639{

2640 \_dbus_assert (auth != NULL);

2641 \_dbus_assert (!auth-\>buffer_outstanding);

2642

2643 \*buffer = &auth-\>incoming;

2644

2645 auth-\>buffer_outstanding = TRUE;

2646}

2647

2654void

2655\_dbus_auth_return_buffer (DBusAuth \*auth,

2656 DBusString \*buffer)

2657{

2658 \_dbus_assert (buffer == &auth-\>incoming);

2659 \_dbus_assert (auth-\>buffer_outstanding);

2660

2661 auth-\>buffer_outstanding = FALSE;

2662}

2663

2673void

2674\_dbus_auth_get_unused_bytes (DBusAuth \*auth,

2675 const DBusString \*\*str)

2676{

2677 if (!DBUS_AUTH_IN_END_STATE (auth))

2678 return;

2679

2680 \*str = &auth-\>incoming;

2681}

2682

2683

2690void

2691\_dbus_auth_delete_unused_bytes (DBusAuth \*auth)

2692{

2693 if (!DBUS_AUTH_IN_END_STATE (auth))

2694 return;

2695

2696 \_dbus_string_set_length (&auth-\>incoming, 0);

2697}

2698

2707dbus_bool_t

2708\_dbus_auth_needs_encoding (DBusAuth \*auth)

2709{

2710 if (auth-\>state != &common_state_authenticated)

2711 return FALSE;

2712

2713 if (auth-\>mech != NULL)

2714 {

2715 if (DBUS_AUTH_IS_CLIENT (auth))

2716 return auth-\>mech-\>client_encode_func != NULL;

2717 else

2718 return auth-\>mech-\>server_encode_func != NULL;

2719 }

2720 else

2721 return FALSE;

2722}

2723

2734dbus_bool_t

2735\_dbus_auth_encode_data (DBusAuth \*auth,

2736 const DBusString \*plaintext,

2737 DBusString \*encoded)

2738{

2739 \_dbus_assert (plaintext != encoded);

2740

2741 if (auth-\>state != &common_state_authenticated)

2742 return FALSE;

2743

2744 if (\_dbus_auth_needs_encoding (auth))

2745 {

2746 if (DBUS_AUTH_IS_CLIENT (auth))

2747 return (\* auth-\>mech-\>client_encode_func) (auth, plaintext, encoded);

2748 else

2749 return (\* auth-\>mech-\>server_encode_func) (auth, plaintext, encoded);

2750 }

2751 else

2752 {

2753 return \_dbus_string_copy (plaintext, 0, encoded,

2754 \_dbus_string_get_length (encoded));

2755 }

2756}

2757

2766dbus_bool_t

2767\_dbus_auth_needs_decoding (DBusAuth \*auth)

2768{

2769 if (auth-\>state != &common_state_authenticated)

2770 return FALSE;

2771

2772 if (auth-\>mech != NULL)

2773 {

2774 if (DBUS_AUTH_IS_CLIENT (auth))

2775 return auth-\>mech-\>client_decode_func != NULL;

2776 else

2777 return auth-\>mech-\>server_decode_func != NULL;

2778 }

2779 else

2780 return FALSE;

2781}

2782

2783

2797dbus_bool_t

2798\_dbus_auth_decode_data (DBusAuth \*auth,

2799 const DBusString \*encoded,

2800 DBusString \*plaintext)

2801{

2802 \_dbus_assert (plaintext != encoded);

2803

2804 if (auth-\>state != &common_state_authenticated)

2805 return FALSE;

2806

2807 if (\_dbus_auth_needs_decoding (auth))

2808 {

2809 if (DBUS_AUTH_IS_CLIENT (auth))

2810 return (\* auth-\>mech-\>client_decode_func) (auth, encoded, plaintext);

2811 else

2812 return (\* auth-\>mech-\>server_decode_func) (auth, encoded, plaintext);

2813 }

2814 else

2815 {

2816 return \_dbus_string_copy (encoded, 0, plaintext,

2817 \_dbus_string_get_length (plaintext));

2818 }

2819}

2820

2829dbus_bool_t

2830\_dbus_auth_set_credentials (DBusAuth \*auth,

2831 DBusCredentials \*credentials)

2832{

2833 \_dbus_credentials_clear (auth-\>credentials);

2834 return \_dbus_credentials_add_credentials (auth-\>credentials,

2835 credentials);

2836}

2837

2847DBusCredentials\*

2848\_dbus_auth_get_identity (DBusAuth \*auth)

2849{

2850 if (auth-\>state == &common_state_authenticated)

2851 {

2852 return auth-\>authorized_identity;

2853 }

2854 else

2855 {

2856 /\* FIXME instead of this, keep an empty credential around that

2857 \* doesn't require allocation or something

2858 \*/

2859 /\* return empty credentials \*/

2860 \_dbus_assert (\_dbus_credentials_are_empty (auth-\>authorized_identity));

2861 return auth-\>authorized_identity;

2862 }

2863}

2864

2871const char\*

2872\_dbus_auth_get_guid_from_server (DBusAuth \*auth)

2873{

2874 \_dbus_assert (DBUS_AUTH_IS_CLIENT (auth));

2875

2876 if (auth-\>state == &common_state_authenticated)

2877 return \_dbus_string_get_const_data (& DBUS_AUTH_CLIENT (auth)-\>guid_from_server);

2878 else

2879 return NULL;

2880}

2881

2890dbus_bool_t

2891\_dbus_auth_set_context (DBusAuth \*auth,

2892 const DBusString \*context)

2893{

2894 return \_dbus_string_replace_len (context, 0, \_dbus_string_get_length (context),

2895 &auth-\>context, 0, \_dbus_string_get_length (context));

2896}

2897

2905void

2906\_dbus_auth_set_unix_fd_possible(DBusAuth \*auth, dbus_bool_t b)

2907{

2908 auth-\>unix_fd_possible = b;

2909}

2910

2917dbus_bool_t

2918\_dbus_auth_get_unix_fd_negotiated(DBusAuth \*auth)

2919{

2920 return auth-\>unix_fd_negotiated;

2921}

2922

2929dbus_bool_t

2930\_dbus_auth_is_supported_mechanism (DBusString \*name)

2931{

2932 \_dbus_assert (name != NULL);

2933

2934 return find_mech (name, NULL) != NULL;

2935}

2936

2943dbus_bool_t

2944\_dbus_auth_dump_supported_mechanisms (DBusString \*buffer)

2945{

2946 unsigned int i;

2947 \_dbus_assert (buffer != NULL);

2948

2949 for (i = 0; all_mechanisms\[i\].mechanism != NULL; i++)

2950 {

2951 if (i \> 0)

2952 {

2953 if (!\_dbus_string_append (buffer, ", "))

2954 return FALSE;

2955 }

2956 if (!\_dbus_string_append (buffer, all_mechanisms\[i\].mechanism))

2957 return FALSE;

2958 }

2959 return TRUE;

2960}

2961

2964/\* tests in dbus-auth-util.c \*/

DBusAuthEncodeFunction

dbus_bool_t(\* DBusAuthEncodeFunction)(DBusAuth \*auth, const DBusString \*data, DBusString \*encoded)

This function encodes a block of data from the peer.

**Definition** dbus-auth.c:85

DBusAuthDecodeFunction

dbus_bool_t(\* DBusAuthDecodeFunction)(DBusAuth \*auth, const DBusString \*data, DBusString \*decoded)

This function decodes a block of data from the peer.

**Definition** dbus-auth.c:92

DBUS_AUTH_SERVER

\#define DBUS_AUTH_SERVER(auth)

**Definition** dbus-auth.c:333

DBUS_AUTH_IS_SERVER

\#define DBUS_AUTH_IS_SERVER(auth)

**Definition** dbus-auth.c:318

DBUS_AUTH_NAME

\#define DBUS_AUTH_NAME(auth)

The name of the auth ("client" or "server")

**Definition** dbus-auth.c:340

DBUS_AUTH_CLIENT

\#define DBUS_AUTH_CLIENT(auth)

**Definition** dbus-auth.c:328

DBUS_AUTH_IS_CLIENT

\#define DBUS_AUTH_IS_CLIENT(auth)

**Definition** dbus-auth.c:323

DBusAuthStateFunction

dbus_bool_t(\* DBusAuthStateFunction)(DBusAuth \*auth, DBusAuthCommand command, const DBusString \*args)

Auth state function, determines the reaction to incoming events for a particular state.

**Definition** dbus-auth.c:139

DBusAuthShutdownFunction

void(\* DBusAuthShutdownFunction)(DBusAuth \*auth)

This function is called when the mechanism is abandoned.

**Definition** dbus-auth.c:99

DBusInitialResponseFunction

dbus_bool_t(\* DBusInitialResponseFunction)(DBusAuth \*auth, DBusString \*response)

This function appends an initial client response to the given string.

**Definition** dbus-auth.c:72

DBusAuthCommand

DBusAuthCommand

Enumeration for the known authentication commands.

**Definition** dbus-auth.c:121

DBusAuthDataFunction

dbus_bool_t(\* DBusAuthDataFunction)(DBusAuth \*auth, const DBusString \*data)

This function processes a block of data received from the peer.

**Definition** dbus-auth.c:79

N_CHALLENGE_BYTES

\#define N_CHALLENGE_BYTES

http://www.ietf.org/rfc/rfc2831.txt suggests at least 64 bits of entropy, we use 128.

**Definition** dbus-auth.c:521

\_dbus_auth_do_work

DBusAuthState \_dbus_auth_do_work(DBusAuth \*auth)

Analyzes buffered input and moves the auth conversation forward, returning the new state of the auth ...

**Definition** dbus-auth.c:2548

\_dbus_auth_encode_data

dbus_bool_t \_dbus_auth_encode_data(DBusAuth \*auth, const DBusString \*plaintext, DBusString \*encoded)

Called post-authentication, encodes a block of bytes for sending to the peer.

**Definition** dbus-auth.c:2735

\_dbus_auth_dump_supported_mechanisms

dbus_bool_t \_dbus_auth_dump_supported_mechanisms(DBusString \*buffer)

Return a human-readable string containing all supported auth mechanisms.

**Definition** dbus-auth.c:2944

\_dbus_auth_needs_encoding

dbus_bool_t \_dbus_auth_needs_encoding(DBusAuth \*auth)

Called post-authentication, indicates whether we need to encode the message stream with \_dbus_auth_en...

**Definition** dbus-auth.c:2708

\_dbus_auth_set_credentials

dbus_bool_t \_dbus_auth_set_credentials(DBusAuth \*auth, DBusCredentials \*credentials)

Sets credentials received via reliable means from the operating system.

**Definition** dbus-auth.c:2830

\_dbus_auth_get_unix_fd_negotiated

dbus_bool_t \_dbus_auth_get_unix_fd_negotiated(DBusAuth \*auth)

Queries whether unix fd passing was successfully negotiated.

**Definition** dbus-auth.c:2918

\_dbus_auth_ref

DBusAuth \* \_dbus_auth_ref(DBusAuth \*auth)

Increments the refcount of an auth object.

**Definition** dbus-auth.c:2448

\_dbus_auth_is_supported_mechanism

dbus_bool_t \_dbus_auth_is_supported_mechanism(DBusString \*name)

Queries whether the given auth mechanism is supported.

**Definition** dbus-auth.c:2930

\_dbus_auth_get_identity

DBusCredentials \* \_dbus_auth_get_identity(DBusAuth \*auth)

Gets the identity we authorized the client as.

**Definition** dbus-auth.c:2848

\_dbus_auth_get_bytes_to_send

dbus_bool_t \_dbus_auth_get_bytes_to_send(DBusAuth \*auth, const DBusString \*\*str)

Gets bytes that need to be sent to the peer we're conversing with.

**Definition** dbus-auth.c:2592

\_dbus_auth_decode_data

dbus_bool_t \_dbus_auth_decode_data(DBusAuth \*auth, const DBusString \*encoded, DBusString \*plaintext)

Called post-authentication, decodes a block of bytes received from the peer.

**Definition** dbus-auth.c:2798

\_dbus_auth_unref

void \_dbus_auth_unref(DBusAuth \*auth)

Decrements the refcount of an auth object.

**Definition** dbus-auth.c:2463

\_dbus_auth_set_unix_fd_possible

void \_dbus_auth_set_unix_fd_possible(DBusAuth \*auth, dbus_bool_t b)

Sets whether unix fd passing is potentially on the transport and hence shall be negotiated.

**Definition** dbus-auth.c:2906

\_dbus_auth_return_buffer

void \_dbus_auth_return_buffer(DBusAuth \*auth, DBusString \*buffer)

Returns a buffer with new data read into it.

**Definition** dbus-auth.c:2655

\_dbus_auth_set_mechanisms

dbus_bool_t \_dbus_auth_set_mechanisms(DBusAuth \*auth, const char \*\*mechanisms)

Sets an array of authentication mechanism names that we are willing to use.

**Definition** dbus-auth.c:2513

\_dbus_auth_delete_unused_bytes

void \_dbus_auth_delete_unused_bytes(DBusAuth \*auth)

Gets rid of unused bytes returned by \_dbus_auth_get_unused_bytes() after we've gotten them and succes...

**Definition** dbus-auth.c:2691

\_dbus_auth_get_guid_from_server

const char \* \_dbus_auth_get_guid_from_server(DBusAuth \*auth)

Gets the GUID from the server if we've authenticated; gets NULL otherwise.

**Definition** dbus-auth.c:2872

\_dbus_auth_get_buffer

void \_dbus_auth_get_buffer(DBusAuth \*auth, DBusString \*\*buffer)

Get a buffer to be used for reading bytes from the peer we're conversing with.

**Definition** dbus-auth.c:2637

\_dbus_auth_needs_decoding

dbus_bool_t \_dbus_auth_needs_decoding(DBusAuth \*auth)

Called post-authentication, indicates whether we need to decode the message stream with \_dbus_auth_de...

**Definition** dbus-auth.c:2767

\_dbus_auth_set_context

dbus_bool_t \_dbus_auth_set_context(DBusAuth \*auth, const DBusString \*context)

Sets the "authentication context" which scopes cookies with the DBUS_COOKIE_SHA1 auth mechanism for e...

**Definition** dbus-auth.c:2891

\_dbus_auth_bytes_sent

void \_dbus_auth_bytes_sent(DBusAuth \*auth, int bytes_sent)

Notifies the auth conversation object that the given number of bytes of the outgoing buffer have been...

**Definition** dbus-auth.c:2617

DBUS_AUTH_IN_END_STATE

\#define DBUS_AUTH_IN_END_STATE(auth)

**Definition** dbus-auth.c:2538

\_dbus_auth_client_new

DBusAuth \* \_dbus_auth_client_new(void)

Creates a new auth conversation object for the client side.

**Definition** dbus-auth.c:2410

\_dbus_auth_server_new

DBusAuth \* \_dbus_auth_server_new(const DBusString \*guid)

Creates a new auth conversation object for the server side.

**Definition** dbus-auth.c:2364

\_dbus_auth_get_unused_bytes

void \_dbus_auth_get_unused_bytes(DBusAuth \*auth, const DBusString \*\*str)

Returns leftover bytes that were not used as part of the auth conversation.

**Definition** dbus-auth.c:2674

\_dbus_credentials_are_superset

dbus_bool_t \_dbus_credentials_are_superset(DBusCredentials \*credentials, DBusCredentials \*possible_subset)

Checks whether the first credentials object contains all the credentials found in the second credenti...

**Definition** dbus-credentials.c:506

\_dbus_credentials_same_user

dbus_bool_t \_dbus_credentials_same_user(DBusCredentials \*credentials, DBusCredentials \*other_credentials)

Check whether the user-identifying credentials in two credentials objects are identical.

**Definition** dbus-credentials.c:747

\_dbus_credentials_clear

void \_dbus_credentials_clear(DBusCredentials \*credentials)

Clear all credentials in the object.

**Definition** dbus-credentials.c:688

\_dbus_credentials_new_from_current_process

DBusCredentials \* \_dbus_credentials_new_from_current_process(void)

Creates a new object with the most important credentials (user ID and process ID) from the current pr...

**Definition** dbus-credentials.c:113

\_dbus_credentials_new

DBusCredentials \* \_dbus_credentials_new(void)

Creates a new credentials object.

**Definition** dbus-credentials.c:86

\_dbus_credentials_add_credentials

dbus_bool_t \_dbus_credentials_add_credentials(DBusCredentials \*credentials, DBusCredentials \*other_credentials)

Merge all credentials found in the second object into the first object, overwriting the first object ...

**Definition** dbus-credentials.c:574

\_dbus_credentials_unref

void \_dbus_credentials_unref(DBusCredentials \*credentials)

Decrement refcount on credentials.

**Definition** dbus-credentials.c:148

\_dbus_credentials_are_empty

dbus_bool_t \_dbus_credentials_are_empty(DBusCredentials \*credentials)

Checks whether a credentials object contains anything.

**Definition** dbus-credentials.c:538

\_dbus_credentials_add_credential

dbus_bool_t \_dbus_credentials_add_credential(DBusCredentials \*credentials, DBusCredentialType which, DBusCredentials \*other_credentials)

Merge the given credential found in the second object into the first object, overwriting the first ob...

**Definition** dbus-credentials.c:614

\_dbus_credentials_are_anonymous

dbus_bool_t \_dbus_credentials_are_anonymous(DBusCredentials \*credentials)

Checks whether a credentials object contains a user identity.

**Definition** dbus-credentials.c:558

DBUS_ERROR_INIT

\#define DBUS_ERROR_INIT

Expands to a suitable initializer for a DBusError on the stack.

**Definition** dbus-errors.h:64

dbus_error_has_name

dbus_bool_t dbus_error_has_name(const DBusError \*error, const char \*name)

Checks whether the error is set and has the given name.

**Definition** dbus-errors.c:304

dbus_error_free

void dbus_error_free(DBusError \*error)

Frees an error that's been set (or just initialized), then reinitializes the error as in dbus_error_i...

**Definition** dbus-errors.c:213

dbus_error_is_set

dbus_bool_t dbus_error_is_set(const DBusError \*error)

Checks whether an error occurred (the error is set).

**Definition** dbus-errors.c:331

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_dbus_string_array_contains

dbus_bool_t \_dbus_string_array_contains(const char \*\*array, const char \*str)

Checks whether a string array contains the given string.

**Definition** dbus-internals.c:712

\_DBUS_N_ELEMENTS

\#define \_DBUS_N_ELEMENTS(array)

Computes the number of elements in a fixed-size array using sizeof().

**Definition** dbus-internals.h:189

\_dbus_dup_string_array

char \*\* \_dbus_dup_string_array(const char \*\*array)

Duplicates a string array.

**Definition** dbus-internals.c:672

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

\_dbus_keyring_unref

void \_dbus_keyring_unref(DBusKeyring \*keyring)

Decrements refcount and finalizes if it reaches zero.

**Definition** dbus-keyring.c:665

\_dbus_list_pop_first

void \* \_dbus_list_pop_first(DBusList \*\*list)

Removes the first value in the list and returns it.

**Definition** dbus-list.c:679

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

dbus_free

void dbus_free(void \*memory)

Frees a block of memory previously allocated by dbus_malloc() or dbus_malloc0().

**Definition** dbus-memory.c:710

dbus_malloc0

void \* dbus_malloc0(size_t bytes)

Allocates the given number of bytes, as with standard malloc(), but all bytes are initialized to zero...

**Definition** dbus-memory.c:540

dbus_free_string_array

void dbus_free_string_array(char \*\*str_array)

Frees a NULL-terminated array of strings.

**Definition** dbus-memory.c:758

DBUS_VERSION_STRING

\#define DBUS_VERSION_STRING

The COMPILE TIME version of libdbus, as a string "X.Y.Z".

**Definition** dbus-arch-deps.h:59

DBUS_ERROR_NO_MEMORY

\#define DBUS_ERROR_NO_MEMORY

There was not enough memory to complete an operation.

**Definition** dbus-protocol.h:363

\_dbus_sha_compute

dbus_bool_t \_dbus_sha_compute(const DBusString \*data, DBusString \*ascii_output)

Computes the ASCII hex-encoded shasum of the given data and appends it to the output string.

**Definition** dbus-sha.c:484

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

\_dbus_string_copy

dbus_bool_t \_dbus_string_copy(const DBusString \*source, int start, DBusString \*dest, int insert_at)

Like \_dbus_string_move(), but does not delete the section of the source string that's copied to the d...

**Definition** dbus-string.c:1345

\_dbus_string_skip_blank

void \_dbus_string_skip_blank(const DBusString \*str, int start, int \*end)

Skips blanks from start, storing the first non-blank in \*end (blank is space or tab).

**Definition** dbus-string.c:1865

\_dbus_string_find

dbus_bool_t \_dbus_string_find(const DBusString \*str, int start, const char \*substr, int \*found)

Finds the given substring in the string, returning TRUE and filling in the byte index where the subst...

**Definition** dbus-string.c:1666

\_dbus_string_validate_utf8

dbus_bool_t \_dbus_string_validate_utf8(const DBusString \*str, int start, int len)

Checks that the given range of the string is valid UTF-8.

**Definition** dbus-string.c:2678

\_dbus_string_find_blank

dbus_bool_t \_dbus_string_find_blank(const DBusString \*str, int start, int \*found)

Finds a blank (space or tab) in the string.

**Definition** dbus-string.c:1827

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_string_delete

void \_dbus_string_delete(DBusString \*str, int start, int len)

Deletes a segment of a DBusString with length len starting at start.

**Definition** dbus-string.c:1255

\_dbus_string_equal_c_str

dbus_bool_t \_dbus_string_equal_c_str(const DBusString \*a, const char \*c_str)

Checks whether a string is equal to a C string.

**Definition** dbus-string.c:2214

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

\_dbus_string_copy_len

dbus_bool_t \_dbus_string_copy_len(const DBusString \*source, int start, int len, DBusString \*dest, int insert_at)

Like \_dbus_string_copy(), but can copy a segment from the middle of the source string.

**Definition** dbus-string.c:1437

\_dbus_string_replace_len

dbus_bool_t \_dbus_string_replace_len(const DBusString \*source, int start, int len, DBusString \*dest, int replace_at, int replace_len)

Replaces a segment of dest string with a segment of source string.

**Definition** dbus-string.c:1466

\_dbus_credentials_add_from_user

dbus_bool_t \_dbus_credentials_add_from_user(DBusCredentials \*credentials, const DBusString \*username, DBusCredentialsAddFlags flags, DBusError \*error)

Adds the credentials corresponding to the given username.

**Definition** dbus-sysdeps-win.c:2314

\_dbus_generate_random_bytes

dbus_bool_t \_dbus_generate_random_bytes(DBusString \*str, int n_bytes, DBusError \*error)

Generates the given number of securely random bytes, using the best mechanism we can come up with.

**Definition** dbus-sysdeps-unix.c:3572

\_dbus_append_user_from_current_process

dbus_bool_t \_dbus_append_user_from_current_process(DBusString \*str)

Append to the string the identity we would like to have when we authenticate, on UNIX this is the cur...

**Definition** dbus-sysdeps-unix.c:3117

DBusAuthClient

"Subclass" of DBusAuth for client side

**Definition** dbus-auth.c:202

DBusAuthClient::mechs_to_try

DBusList \* mechs_to_try

Mechanisms we got from the server that we're going to try using.

**Definition** dbus-auth.c:205

DBusAuthClient::base

DBusAuth base

Parent class.

**Definition** dbus-auth.c:203

DBusAuthClient::guid_from_server

DBusString guid_from_server

GUID received from server.

**Definition** dbus-auth.c:207

DBusAuthCommandName

Mapping from command name to enum.

**Definition** dbus-auth.c:2212

DBusAuthCommandName::command

DBusAuthCommand command

Corresponding enum.

**Definition** dbus-auth.c:2214

DBusAuthCommandName::name

const char \* name

Name of the command.

**Definition** dbus-auth.c:2213

DBusAuthMechanismHandler

Virtual table representing a particular auth mechanism.

**Definition** dbus-auth.c:105

DBusAuthMechanismHandler::mechanism

const char \* mechanism

Name of the mechanism.

**Definition** dbus-auth.c:106

DBusAuthMechanismHandler::server_data_func

DBusAuthDataFunction server_data_func

Function on server side for DATA.

**Definition** dbus-auth.c:107

DBusAuthMechanismHandler::client_data_func

DBusAuthDataFunction client_data_func

Function on client side for DATA.

**Definition** dbus-auth.c:112

DBusAuthMechanismHandler::client_initial_response_func

DBusInitialResponseFunction client_initial_response_func

Function on client side to handle initial response.

**Definition** dbus-auth.c:111

DBusAuthMechanismHandler::server_encode_func

DBusAuthEncodeFunction server_encode_func

Function on server side to encode.

**Definition** dbus-auth.c:108

DBusAuthMechanismHandler::server_shutdown_func

DBusAuthShutdownFunction server_shutdown_func

Function on server side to shut down.

**Definition** dbus-auth.c:110

DBusAuthMechanismHandler::client_decode_func

DBusAuthDecodeFunction client_decode_func

Function on client side for decode.

**Definition** dbus-auth.c:114

DBusAuthMechanismHandler::server_decode_func

DBusAuthDecodeFunction server_decode_func

Function on server side to decode.

**Definition** dbus-auth.c:109

DBusAuthMechanismHandler::client_shutdown_func

DBusAuthShutdownFunction client_shutdown_func

Function on client side for shutdown.

**Definition** dbus-auth.c:115

DBusAuthMechanismHandler::client_encode_func

DBusAuthEncodeFunction client_encode_func

Function on client side for encode.

**Definition** dbus-auth.c:113

DBusAuthServer

"Subclass" of DBusAuth for server side.

**Definition** dbus-auth.c:215

DBusAuthServer::max_failures

int max_failures

Number of times we reject before disconnect.

**Definition** dbus-auth.c:219

DBusAuthServer::guid

DBusString guid

Our globally unique ID in hex encoding.

**Definition** dbus-auth.c:221

DBusAuthServer::base

DBusAuth base

Parent class.

**Definition** dbus-auth.c:216

DBusAuthServer::failures

int failures

Number of times client has been rejected.

**Definition** dbus-auth.c:218

DBusAuthStateData

Information about a auth state.

**Definition** dbus-auth.c:147

DBusAuthStateData::handler

DBusAuthStateFunction handler

State function for this state.

**Definition** dbus-auth.c:149

DBusAuthStateData::name

const char \* name

Name of the state.

**Definition** dbus-auth.c:148

DBusAuth

Internal members of DBusAuth.

**Definition** dbus-auth.c:156

DBusAuth::already_got_mechanisms

unsigned int already_got_mechanisms

Client already got mech list.

**Definition** dbus-auth.c:190

DBusAuth::mech

const DBusAuthMechanismHandler \* mech

Current auth mechanism.

**Definition** dbus-auth.c:165

DBusAuth::allowed_mechs

char \*\* allowed_mechs

Mechanisms we're allowed to use, or NULL if we can use any.

**Definition** dbus-auth.c:183

DBusAuth::needed_memory

unsigned int needed_memory

We needed memory to continue since last successful getting something done.

**Definition** dbus-auth.c:187

DBusAuth::cookie_id

int cookie_id

ID of cookie to use.

**Definition** dbus-auth.c:180

DBusAuth::state

const DBusAuthStateData \* state

Current protocol state.

**Definition** dbus-auth.c:163

DBusAuth::challenge

DBusString challenge

Challenge sent to client.

**Definition** dbus-auth.c:181

DBusAuth::desired_identity

DBusCredentials \* desired_identity

Identity client has requested.

**Definition** dbus-auth.c:176

DBusAuth::unix_fd_possible

unsigned int unix_fd_possible

This side could do unix fd passing.

**Definition** dbus-auth.c:194

DBusAuth::side

const char \* side

Client or server.

**Definition** dbus-auth.c:158

DBusAuth::identity

DBusString identity

Current identity we're authorizing as.

**Definition** dbus-auth.c:167

DBusAuth::incoming

DBusString incoming

Incoming data buffer.

**Definition** dbus-auth.c:160

DBusAuth::refcount

int refcount

reference count

**Definition** dbus-auth.c:157

DBusAuth::already_asked_for_initial_response

unsigned int already_asked_for_initial_response

Already sent a blank challenge to get an initial response.

**Definition** dbus-auth.c:191

DBusAuth::keyring

DBusKeyring \* keyring

Keyring for cookie mechanism.

**Definition** dbus-auth.c:179

DBusAuth::outgoing

DBusString outgoing

Outgoing data buffer.

**Definition** dbus-auth.c:161

DBusAuth::credentials

DBusCredentials \* credentials

Credentials read from socket.

**Definition** dbus-auth.c:171

DBusAuth::context

DBusString context

Cookie scope.

**Definition** dbus-auth.c:178

DBusAuth::unix_fd_negotiated

unsigned int unix_fd_negotiated

Unix fd was successfully negotiated.

**Definition** dbus-auth.c:195

DBusAuth::buffer_outstanding

unsigned int buffer_outstanding

Buffer is "checked out" for reading data into.

**Definition** dbus-auth.c:192

DBusAuth::authorized_identity

DBusCredentials \* authorized_identity

Credentials that are authorized.

**Definition** dbus-auth.c:174

DBusCredentials

**Definition** dbus-credentials.c:60

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusError::message

const char \* message

public error message field

**Definition** dbus-errors.h:53

DBusKeyring

Internals of DBusKeyring.

**Definition** dbus-keyring.c:112

DBusList

A node in a linked list.

**Definition** dbus-list.h:37

DBusList::data

void \* data

Data stored at this element.

**Definition** dbus-list.h:40

DBusString

**Definition** dbus-string.h:47
