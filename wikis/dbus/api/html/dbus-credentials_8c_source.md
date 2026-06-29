dbus-credentials.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-credentials.c Credentials provable through authentication

3 \*

4 \* Copyright (C) 2007 Red Hat Inc.

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

25\#include \<config.h\>

26\#include \<stdlib.h\>

27\#include \<string.h\>

28\#ifdef HAVE_UNISTD_H

29\#include \<unistd.h\>

30\#endif

31\#ifdef HAVE_SYS_SYSCALL_H

32\#include \<sys/syscall.h\>

33\#endif

34\#include "dbus-credentials.h"

35\#include "dbus-internals.h"

36\#ifdef DBUS_UNIX

37\#include "dbus-sysdeps-unix.h"

38\#endif

39

60struct DBusCredentials {

61 int refcount;

62 dbus_uid_t unix_uid;

63 dbus_gid_t \*unix_gids;

64 size_t n_unix_gids;

65 dbus_pid_t pid;

66 int pid_fd;

67 char \*windows_sid;

68 char \*linux_security_label;

69 void \*adt_audit_data;

70 dbus_int32_t adt_audit_data_size;

71};

72

85DBusCredentials\*

86\_dbus_credentials_new (void)

87{

88 DBusCredentials \*creds;

89

90 creds = dbus_new (DBusCredentials, 1);

91 if (creds == NULL)

92 return NULL;

93

94 creds-\>refcount = 1;

95 creds-\>unix_uid = DBUS_UID_UNSET;

96 creds-\>unix_gids = NULL;

97 creds-\>n_unix_gids = 0;

98 creds-\>pid = DBUS_PID_UNSET;

99 creds-\>pid_fd = -1;

100 creds-\>windows_sid = NULL;

101 creds-\>linux_security_label = NULL;

102 creds-\>adt_audit_data = NULL;

103 creds-\>adt_audit_data_size = 0;

104

105 return creds;

106}

107

112DBusCredentials\*

113\_dbus_credentials_new_from_current_process (void)

114{

115 DBusCredentials \*creds;

116

117 creds = \_dbus_credentials_new ();

118 if (creds == NULL)

119 return NULL;

120

121 if (!\_dbus_credentials_add_from_current_process (creds))

122 {

123 \_dbus_credentials_unref (creds);

124 return NULL;

125 }

126

127 return creds;

128}

129

135void

136\_dbus_credentials_ref (DBusCredentials \*credentials)

137{

138 \_dbus_assert (credentials-\>refcount \> 0);

139 credentials-\>refcount += 1;

140}

141

147void

148\_dbus_credentials_unref (DBusCredentials \*credentials)

149{

150 \_dbus_assert (credentials-\>refcount \> 0);

151

152 credentials-\>refcount -= 1;

153 if (credentials-\>refcount == 0)

154 {

155 dbus_free (credentials-\>unix_gids);

156 dbus_free (credentials-\>windows_sid);

157 dbus_free (credentials-\>linux_security_label);

158 dbus_free (credentials-\>adt_audit_data);

159\#ifdef DBUS_UNIX

160 if (credentials-\>pid_fd \>= 0)

161 {

162 close (credentials-\>pid_fd);

163 credentials-\>pid_fd = -1;

164 }

165\#endif

166 dbus_free (credentials);

167 }

168}

169

180dbus_bool_t

181\_dbus_credentials_add_pid (DBusCredentials \*credentials,

182 dbus_pid_t pid)

183{

184 credentials-\>pid = pid;

185 return TRUE;

186}

187

196\#ifndef DBUS_UNIX

197\_DBUS_GNUC_NORETURN

198\#endif

199void

200\_dbus_credentials_take_pid_fd (DBusCredentials \*credentials,

201 int pid_fd)

202{

203\#ifdef DBUS_UNIX

204 if (credentials-\>pid_fd \>= 0)

205 close (credentials-\>pid_fd);

206 credentials-\>pid_fd = pid_fd;

207\#else

208 \_dbus_assert_not_reached ("pidfd never set on non-Unix");

209\#endif

210}

211

219dbus_bool_t

220\_dbus_credentials_add_unix_uid(DBusCredentials \*credentials,

221 dbus_uid_t uid)

222{

223 credentials-\>unix_uid = uid;

224 return TRUE;

225

226}

227

228static int

229cmp_gidp (const void \*a\_, const void \*b\_)

230{

231 const dbus_gid_t \*a = a\_;

232 const dbus_gid_t \*b = b\_;

233

234 if (\*a \< \*b)

235 return -1;

236

237 if (\*a \> \*b)

238 return 1;

239

240 return 0;

241}

242

251void

252\_dbus_credentials_take_unix_gids (DBusCredentials \*credentials,

253 dbus_gid_t \*gids,

254 size_t n_gids)

255{

256 /\* So we can compare arrays via a simple memcmp \*/

257 qsort (gids, n_gids, sizeof (dbus_gid_t), cmp_gidp);

258

259 dbus_free (credentials-\>unix_gids);

260 credentials-\>unix_gids = gids;

261 credentials-\>n_unix_gids = n_gids;

262}

263

271dbus_bool_t

272\_dbus_credentials_get_unix_gids (DBusCredentials \*credentials,

273 const dbus_gid_t \*\*gids,

274 size_t \*n_gids)

275{

276 if (gids != NULL)

277 \*gids = credentials-\>unix_gids;

278

279 if (n_gids != NULL)

280 \*n_gids = credentials-\>n_unix_gids;

281

282 return (credentials-\>unix_gids != NULL);

283}

284

292dbus_bool_t

293\_dbus_credentials_add_windows_sid (DBusCredentials \*credentials,

294 const char \*windows_sid)

295{

296 char \*copy;

297

298 copy = \_dbus_strdup (windows_sid);

299 if (copy == NULL)

300 return FALSE;

301

302 dbus_free (credentials-\>windows_sid);

303 credentials-\>windows_sid = copy;

304

305 return TRUE;

306}

307

316dbus_bool_t

317\_dbus_credentials_add_linux_security_label (DBusCredentials \*credentials,

318 const char \*label)

319{

320 char \*copy;

321

322 copy = \_dbus_strdup (label);

323 if (copy == NULL)

324 return FALSE;

325

326 dbus_free (credentials-\>linux_security_label);

327 credentials-\>linux_security_label = copy;

328

329 return TRUE;

330}

331

340dbus_bool_t

341\_dbus_credentials_add_adt_audit_data (DBusCredentials \*credentials,

342 void \*audit_data,

343 dbus_int32_t size)

344{

345 void \*copy;

346 copy = \_dbus_memdup (audit_data, size);

347 if (copy == NULL)

348 return FALSE;

349

350 dbus_free (credentials-\>adt_audit_data);

351 credentials-\>adt_audit_data = copy;

352 credentials-\>adt_audit_data_size = size;

353

354 return TRUE;

355}

356

364dbus_bool_t

365\_dbus_credentials_include (DBusCredentials \*credentials,

366 DBusCredentialType type)

367{

368 switch (type)

369 {

370 case DBUS_CREDENTIAL_UNIX_PROCESS_ID:

371 return credentials-\>pid != DBUS_PID_UNSET \|\|

372 credentials-\>pid_fd \>= 0;

373 case DBUS_CREDENTIAL_UNIX_PROCESS_FD:

374 return credentials-\>pid_fd \>= 0;

375 case DBUS_CREDENTIAL_UNIX_USER_ID:

376 return credentials-\>unix_uid != DBUS_UID_UNSET;

377 case DBUS_CREDENTIAL_UNIX_GROUP_IDS:

378 return credentials-\>unix_gids != NULL;

379 case DBUS_CREDENTIAL_WINDOWS_SID:

380 return credentials-\>windows_sid != NULL;

381 case DBUS_CREDENTIAL_LINUX_SECURITY_LABEL:

382 return credentials-\>linux_security_label != NULL;

383 case DBUS_CREDENTIAL_ADT_AUDIT_DATA_ID:

384 return credentials-\>adt_audit_data != NULL;

385 default:

386 \_dbus_assert_not_reached ("Unknown credential enum value");

387 return FALSE;

388 }

389}

390

400dbus_pid_t

401\_dbus_credentials_get_pid (DBusCredentials \*credentials)

402{

403\#ifdef DBUS_UNIX

404 dbus_pid_t pid;

405

406 if (credentials-\>pid_fd \>= 0)

407 {

408 pid = \_dbus_resolve_pid_fd (credentials-\>pid_fd);

409 if (pid \> 0)

410 return pid;

411 }

412\#endif

413

414 return credentials-\>pid;

415}

416

426int

427\_dbus_credentials_get_pid_fd (DBusCredentials \*credentials)

428{

429 return credentials-\>pid_fd;

430}

431

439dbus_uid_t

440\_dbus_credentials_get_unix_uid (DBusCredentials \*credentials)

441{

442 return credentials-\>unix_uid;

443}

444

452const char\*

453\_dbus_credentials_get_windows_sid (DBusCredentials \*credentials)

454{

455 return credentials-\>windows_sid;

456}

457

465const char \*

466\_dbus_credentials_get_linux_security_label (DBusCredentials \*credentials)

467{

468 return credentials-\>linux_security_label;

469}

470

478void \*

479\_dbus_credentials_get_adt_audit_data (DBusCredentials \*credentials)

480{

481 return credentials-\>adt_audit_data;

482}

483

491dbus_int32_t

492\_dbus_credentials_get_adt_audit_data_size (DBusCredentials \*credentials)

493{

494 return credentials-\>adt_audit_data_size;

495}

496

505dbus_bool_t

506\_dbus_credentials_are_superset (DBusCredentials \*credentials,

507 DBusCredentials \*possible_subset)

508{

509 return

510 (possible_subset-\>pid == DBUS_PID_UNSET \|\|

511 possible_subset-\>pid == credentials-\>pid) &&

512 (possible_subset-\>unix_uid == DBUS_UID_UNSET \|\|

513 possible_subset-\>unix_uid == credentials-\>unix_uid) &&

514 (possible_subset-\>unix_gids == NULL \|\|

515 (possible_subset-\>n_unix_gids == credentials-\>n_unix_gids &&

516 memcmp (possible_subset-\>unix_gids, credentials-\>unix_gids,

517 sizeof (dbus_gid_t) \* credentials-\>n_unix_gids) == 0)) &&

518 (possible_subset-\>windows_sid == NULL \|\|

519 (credentials-\>windows_sid && strcmp (possible_subset-\>windows_sid,

520 credentials-\>windows_sid) == 0)) &&

521 (possible_subset-\>linux_security_label == NULL \|\|

522 (credentials-\>linux_security_label != NULL &&

523 strcmp (possible_subset-\>linux_security_label,

524 credentials-\>linux_security_label) == 0)) &&

525 (possible_subset-\>adt_audit_data == NULL \|\|

526 (credentials-\>adt_audit_data && memcmp (possible_subset-\>adt_audit_data,

527 credentials-\>adt_audit_data,

528 credentials-\>adt_audit_data_size) == 0));

529}

530

537dbus_bool_t

538\_dbus_credentials_are_empty (DBusCredentials \*credentials)

539{

540 return

541 credentials-\>pid == DBUS_PID_UNSET &&

542 credentials-\>pid_fd == -1 &&

543 credentials-\>unix_uid == DBUS_UID_UNSET &&

544 credentials-\>unix_gids == NULL &&

545 credentials-\>n_unix_gids == 0 &&

546 credentials-\>windows_sid == NULL &&

547 credentials-\>linux_security_label == NULL &&

548 credentials-\>adt_audit_data == NULL;

549}

550

557dbus_bool_t

558\_dbus_credentials_are_anonymous (DBusCredentials \*credentials)

559{

560 return

561 credentials-\>unix_uid == DBUS_UID_UNSET &&

562 credentials-\>windows_sid == NULL;

563}

564

573dbus_bool_t

574\_dbus_credentials_add_credentials (DBusCredentials \*credentials,

575 DBusCredentials \*other_credentials)

576{

577 return

578 \_dbus_credentials_add_credential (credentials,

579 DBUS_CREDENTIAL_UNIX_PROCESS_FD,

580 other_credentials) &&

581 \_dbus_credentials_add_credential (credentials,

582 DBUS_CREDENTIAL_UNIX_PROCESS_ID,

583 other_credentials) &&

584 \_dbus_credentials_add_credential (credentials,

585 DBUS_CREDENTIAL_UNIX_USER_ID,

586 other_credentials) &&

587 \_dbus_credentials_add_credential (credentials,

588 DBUS_CREDENTIAL_UNIX_GROUP_IDS,

589 other_credentials) &&

590 \_dbus_credentials_add_credential (credentials,

591 DBUS_CREDENTIAL_ADT_AUDIT_DATA_ID,

592 other_credentials) &&

593 \_dbus_credentials_add_credential (credentials,

594 DBUS_CREDENTIAL_LINUX_SECURITY_LABEL,

595 other_credentials) &&

596 \_dbus_credentials_add_credential (credentials,

597 DBUS_CREDENTIAL_WINDOWS_SID,

598 other_credentials);

599}

600

613dbus_bool_t

614\_dbus_credentials_add_credential (DBusCredentials \*credentials,

615 DBusCredentialType which,

616 DBusCredentials \*other_credentials)

617{

618 if (which == DBUS_CREDENTIAL_UNIX_PROCESS_ID &&

619 other_credentials-\>pid != DBUS_PID_UNSET)

620 {

621 if (!\_dbus_credentials_add_pid (credentials, other_credentials-\>pid))

622 return FALSE;

623 }

624 else if (which == DBUS_CREDENTIAL_UNIX_USER_ID &&

625 other_credentials-\>unix_uid != DBUS_UID_UNSET)

626 {

627 if (!\_dbus_credentials_add_unix_uid (credentials, other_credentials-\>unix_uid))

628 return FALSE;

629 }

630 else if (which == DBUS_CREDENTIAL_UNIX_GROUP_IDS &&

631 other_credentials-\>unix_gids != NULL)

632 {

633 dbus_gid_t \*gids;

634

635 gids = dbus_new (dbus_gid_t, other_credentials-\>n_unix_gids);

636

637 if (gids == NULL)

638 return FALSE;

639

640 memcpy (gids, other_credentials-\>unix_gids,

641 sizeof (dbus_gid_t) \* other_credentials-\>n_unix_gids);

642

643 \_dbus_credentials_take_unix_gids (credentials, gids,

644 other_credentials-\>n_unix_gids);

645 }

646 else if (which == DBUS_CREDENTIAL_WINDOWS_SID &&

647 other_credentials-\>windows_sid != NULL)

648 {

649 if (!\_dbus_credentials_add_windows_sid (credentials, other_credentials-\>windows_sid))

650 return FALSE;

651 }

652 else if (which == DBUS_CREDENTIAL_LINUX_SECURITY_LABEL &&

653 other_credentials-\>linux_security_label != NULL)

654 {

655 if (!\_dbus_credentials_add_linux_security_label (credentials,

656 other_credentials-\>linux_security_label))

657 return FALSE;

658 }

659 else if (which == DBUS_CREDENTIAL_ADT_AUDIT_DATA_ID &&

660 other_credentials-\>adt_audit_data != NULL)

661 {

662 if (!\_dbus_credentials_add_adt_audit_data (credentials, other_credentials-\>adt_audit_data, other_credentials-\>adt_audit_data_size))

663 return FALSE;

664 }

665 /\* \_dbus_dup() is only available on UNIX platforms. \*/

666\#ifdef DBUS_UNIX

667 else if (which == DBUS_CREDENTIAL_UNIX_PROCESS_FD &&

668 other_credentials-\>pid_fd \>= 0)

669 {

670 int pid_fd = \_dbus_dup (other_credentials-\>pid_fd, NULL);

671

672 if (pid_fd \< 0)

673 return FALSE;

674

675 \_dbus_credentials_take_pid_fd (credentials, pid_fd);

676 }

677\#endif

678

679 return TRUE;

680}

681

687void

688\_dbus_credentials_clear (DBusCredentials \*credentials)

689{

690 credentials-\>pid = DBUS_PID_UNSET;

691\#ifdef DBUS_UNIX

692 if (credentials-\>pid_fd \>= 0)

693 {

694 close (credentials-\>pid_fd);

695 credentials-\>pid_fd = -1;

696 }

697\#endif

698 credentials-\>unix_uid = DBUS_UID_UNSET;

699 dbus_free (credentials-\>unix_gids);

700 credentials-\>unix_gids = NULL;

701 credentials-\>n_unix_gids = 0;

702 dbus_free (credentials-\>windows_sid);

703 credentials-\>windows_sid = NULL;

704 dbus_free (credentials-\>linux_security_label);

705 credentials-\>linux_security_label = NULL;

706 dbus_free (credentials-\>adt_audit_data);

707 credentials-\>adt_audit_data = NULL;

708 credentials-\>adt_audit_data_size = 0;

709}

710

717DBusCredentials\*

718\_dbus_credentials_copy (DBusCredentials \*credentials)

719{

720 DBusCredentials \*copy;

721

722 copy = \_dbus_credentials_new ();

723 if (copy == NULL)

724 return NULL;

725

726 if (!\_dbus_credentials_add_credentials (copy, credentials))

727 {

728 \_dbus_credentials_unref (copy);

729 return NULL;

730 }

731

732 return copy;

733}

734

746dbus_bool_t

747\_dbus_credentials_same_user (DBusCredentials \*credentials,

748 DBusCredentials \*other_credentials)

749{

750 /\* both windows and unix user must be the same (though pretty much

751 \* in all conceivable cases, one will be unset)

752 \*/

753 return credentials-\>unix_uid == other_credentials-\>unix_uid &&

754 ((!(credentials-\>windows_sid \|\| other_credentials-\>windows_sid)) \|\|

755 (credentials-\>windows_sid && other_credentials-\>windows_sid &&

756 strcmp (credentials-\>windows_sid, other_credentials-\>windows_sid) == 0));

757}

758

767dbus_bool_t

768\_dbus_credentials_to_string_append (DBusCredentials \*credentials,

769 DBusString \*string)

770{

771 dbus_bool_t join;

772

773 join = FALSE;

774 if (credentials-\>unix_uid != DBUS_UID_UNSET)

775 {

776 if (!\_dbus_string_append_printf (string, "uid=" DBUS_UID_FORMAT, credentials-\>unix_uid))

777 goto oom;

778 join = TRUE;

779 }

780 if (credentials-\>pid != DBUS_PID_UNSET \|\| credentials-\>pid_fd \>= 0)

781 {

782 if (!\_dbus_string_append_printf (string,

783 "%spid=" DBUS_PID_FORMAT,

784 join ? " " : "",

785 \_dbus_credentials_get_pid (credentials)))

786 goto oom;

787 join = TRUE;

788 }

789

790 if (credentials-\>unix_gids != NULL)

791 {

792 size_t i;

793

794 for (i = 0; i \< credentials-\>n_unix_gids; i++)

795 {

796 if (!\_dbus_string_append_printf (string, "%sgid=" DBUS_GID_FORMAT,

797 join ? " " : "",

798 credentials-\>unix_gids\[i\]))

799 goto oom;

800

801 join = TRUE;

802 }

803 }

804

805 if (credentials-\>windows_sid != NULL)

806 {

807 if (!\_dbus_string_append_printf (string, "%ssid=%s", join ? " " : "", credentials-\>windows_sid))

808 goto oom;

809 join = TRUE;

810 }

811

812 if (credentials-\>linux_security_label != NULL)

813 {

814 if (!\_dbus_string_append_printf (string, "%slsm='%s'",

815 join ? " " : "",

816 credentials-\>linux_security_label))

817 goto oom;

818 join = TRUE;

819 }

820

821 if (credentials-\>pid_fd \>= 0)

822 {

823 if (!\_dbus_string_append_printf (string, "%spidfd=%d", join ? " " : "", credentials-\>pid_fd))

824 goto oom;

825 join = TRUE;

826 }

827

828 return TRUE;

829oom:

830 return FALSE;

831}

832

835/\* tests in dbus-credentials-util.c \*/

\_dbus_credentials_ref

void \_dbus_credentials_ref(DBusCredentials \*credentials)

Increment refcount on credentials.

**Definition** dbus-credentials.c:136

\_dbus_credentials_include

dbus_bool_t \_dbus_credentials_include(DBusCredentials \*credentials, DBusCredentialType type)

Checks whether the given credential is present.

**Definition** dbus-credentials.c:365

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

\_dbus_credentials_get_unix_uid

dbus_uid_t \_dbus_credentials_get_unix_uid(DBusCredentials \*credentials)

Gets the UNIX user ID in the credentials, or DBUS_UID_UNSET if the credentials object doesn't contain...

**Definition** dbus-credentials.c:440

\_dbus_credentials_copy

DBusCredentials \* \_dbus_credentials_copy(DBusCredentials \*credentials)

Copy a credentials object.

**Definition** dbus-credentials.c:718

\_dbus_credentials_new_from_current_process

DBusCredentials \* \_dbus_credentials_new_from_current_process(void)

Creates a new object with the most important credentials (user ID and process ID) from the current pr...

**Definition** dbus-credentials.c:113

\_dbus_credentials_to_string_append

dbus_bool_t \_dbus_credentials_to_string_append(DBusCredentials \*credentials, DBusString \*string)

Convert the credentials in this object to a human-readable string format, and append to the given str...

**Definition** dbus-credentials.c:768

\_dbus_credentials_new

DBusCredentials \* \_dbus_credentials_new(void)

Creates a new credentials object.

**Definition** dbus-credentials.c:86

\_dbus_credentials_get_adt_audit_data

void \* \_dbus_credentials_get_adt_audit_data(DBusCredentials \*credentials)

Gets the ADT audit data in the credentials, or NULL if the credentials object doesn't contain ADT aud...

**Definition** dbus-credentials.c:479

\_dbus_credentials_take_pid_fd

\_DBUS_GNUC_NORETURN void \_dbus_credentials_take_pid_fd(DBusCredentials \*credentials, int pid_fd)

Add a UNIX process ID FD to the credentials.

**Definition** dbus-credentials.c:200

\_dbus_credentials_add_linux_security_label

dbus_bool_t \_dbus_credentials_add_linux_security_label(DBusCredentials \*credentials, const char \*label)

Add a Linux security label, as used by LSMs such as SELinux, Smack and AppArmor, to the credentials.

**Definition** dbus-credentials.c:317

\_dbus_credentials_add_credentials

dbus_bool_t \_dbus_credentials_add_credentials(DBusCredentials \*credentials, DBusCredentials \*other_credentials)

Merge all credentials found in the second object into the first object, overwriting the first object ...

**Definition** dbus-credentials.c:574

\_dbus_credentials_get_linux_security_label

const char \* \_dbus_credentials_get_linux_security_label(DBusCredentials \*credentials)

Gets the Linux security label (as used by LSMs) from the credentials, or NULL if the credentials obje...

**Definition** dbus-credentials.c:466

\_dbus_credentials_take_unix_gids

void \_dbus_credentials_take_unix_gids(DBusCredentials \*credentials, dbus_gid_t \*gids, size_t n_gids)

Add UNIX group IDs to the credentials, replacing any group IDs that might already have been present.

**Definition** dbus-credentials.c:252

\_dbus_credentials_unref

void \_dbus_credentials_unref(DBusCredentials \*credentials)

Decrement refcount on credentials.

**Definition** dbus-credentials.c:148

\_dbus_credentials_get_unix_gids

dbus_bool_t \_dbus_credentials_get_unix_gids(DBusCredentials \*credentials, const dbus_gid_t \*\*gids, size_t \*n_gids)

Get the Unix group IDs.

**Definition** dbus-credentials.c:272

\_dbus_credentials_are_empty

dbus_bool_t \_dbus_credentials_are_empty(DBusCredentials \*credentials)

Checks whether a credentials object contains anything.

**Definition** dbus-credentials.c:538

\_dbus_credentials_add_unix_uid

dbus_bool_t \_dbus_credentials_add_unix_uid(DBusCredentials \*credentials, dbus_uid_t uid)

Add a UNIX user ID to the credentials.

**Definition** dbus-credentials.c:220

\_dbus_credentials_add_windows_sid

dbus_bool_t \_dbus_credentials_add_windows_sid(DBusCredentials \*credentials, const char \*windows_sid)

Add a Windows user SID to the credentials.

**Definition** dbus-credentials.c:293

\_dbus_credentials_add_pid

dbus_bool_t \_dbus_credentials_add_pid(DBusCredentials \*credentials, dbus_pid_t pid)

Add a UNIX process ID to the credentials.

**Definition** dbus-credentials.c:181

\_dbus_credentials_get_pid

dbus_pid_t \_dbus_credentials_get_pid(DBusCredentials \*credentials)

Gets the UNIX process ID in the credentials, or DBUS_PID_UNSET if the credentials object doesn't cont...

**Definition** dbus-credentials.c:401

\_dbus_credentials_add_adt_audit_data

dbus_bool_t \_dbus_credentials_add_adt_audit_data(DBusCredentials \*credentials, void \*audit_data, dbus_int32_t size)

Add ADT audit data to the credentials.

**Definition** dbus-credentials.c:341

\_dbus_credentials_get_adt_audit_data_size

dbus_int32_t \_dbus_credentials_get_adt_audit_data_size(DBusCredentials \*credentials)

Gets the ADT audit data size in the credentials, or 0 if the credentials object doesn't contain ADT a...

**Definition** dbus-credentials.c:492

\_dbus_credentials_get_windows_sid

const char \* \_dbus_credentials_get_windows_sid(DBusCredentials \*credentials)

Gets the Windows user SID in the credentials, or NULL if the credentials object doesn't contain a Win...

**Definition** dbus-credentials.c:453

\_dbus_credentials_add_credential

dbus_bool_t \_dbus_credentials_add_credential(DBusCredentials \*credentials, DBusCredentialType which, DBusCredentials \*other_credentials)

Merge the given credential found in the second object into the first object, overwriting the first ob...

**Definition** dbus-credentials.c:614

\_dbus_credentials_are_anonymous

dbus_bool_t \_dbus_credentials_are_anonymous(DBusCredentials \*credentials)

Checks whether a credentials object contains a user identity.

**Definition** dbus-credentials.c:558

\_dbus_credentials_get_pid_fd

int \_dbus_credentials_get_pid_fd(DBusCredentials \*credentials)

Gets the UNIX process ID FD in the credentials as obtained by 'safe' means (e.g.: Linux's SO_PEERPIDF...

**Definition** dbus-credentials.c:427

\_dbus_assert_not_reached

\#define \_dbus_assert_not_reached(explanation)

Aborts with an error message if called.

**Definition** dbus-internals.h:164

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_dbus_strdup

char \* \_dbus_strdup(const char \*str)

Duplicates a string.

**Definition** dbus-internals.c:621

\_dbus_memdup

void \* \_dbus_memdup(const void \*mem, size_t n_bytes)

Duplicates a block of memory.

**Definition** dbus-internals.c:649

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

\_dbus_string_append_printf

dbus_bool_t \_dbus_string_append_printf(DBusString \*str, const char \*format,...)

Appends a printf-style formatted string to the DBusString.

**Definition** dbus-string.c:1147

\_dbus_dup

int \_dbus_dup(int fd, DBusError \*error)

Duplicates a file descriptor.

**Definition** dbus-sysdeps-unix.c:3755

dbus_uid_t

unsigned long dbus_uid_t

A user ID.

**Definition** dbus-sysdeps.h:141

dbus_pid_t

unsigned long dbus_pid_t

A process ID.

**Definition** dbus-sysdeps.h:139

dbus_gid_t

unsigned long dbus_gid_t

A group ID.

**Definition** dbus-sysdeps.h:143

DBUS_UID_UNSET

\#define DBUS_UID_UNSET

an invalid UID used to represent an uninitialized dbus_uid_t field

**Definition** dbus-sysdeps.h:148

DBUS_PID_UNSET

\#define DBUS_PID_UNSET

an invalid PID used to represent an uninitialized dbus_pid_t field

**Definition** dbus-sysdeps.h:146

\_dbus_resolve_pid_fd

dbus_pid_t \_dbus_resolve_pid_fd(int pid_fd)

Resolve the PID from the PID FD, if any.

**Definition** dbus-sysdeps-unix.c:3045

\_dbus_credentials_add_from_current_process

dbus_bool_t \_dbus_credentials_add_from_current_process(DBusCredentials \*credentials)

Adds the most important credentials of the current process (the uid and pid) to the passed-in credent...

**Definition** dbus-sysdeps-unix.c:3005

DBUS_GID_FORMAT

\#define DBUS_GID_FORMAT

an appropriate printf format for dbus_gid_t

**Definition** dbus-sysdeps.h:157

DBUS_UID_FORMAT

\#define DBUS_UID_FORMAT

an appropriate printf format for dbus_uid_t

**Definition** dbus-sysdeps.h:155

DBUS_PID_FORMAT

\#define DBUS_PID_FORMAT

an appropriate printf format for dbus_pid_t

**Definition** dbus-sysdeps.h:153

DBusCredentials

**Definition** dbus-credentials.c:60

DBusString

**Definition** dbus-string.h:47
