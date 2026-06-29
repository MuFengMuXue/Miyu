dbus-sysdeps-util-win.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-sysdeps-util.c Would be in dbus-sysdeps.c, but not used in libdbus

3 \*

4 \* Copyright (C) 2002, 2003, 2004, 2005 Red Hat, Inc.

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

28

29\#define STRSAFE_NO_DEPRECATE

30

31\#include "dbus-sysdeps.h"

32\#include "dbus-internals.h"

33\#include "dbus-protocol.h"

34\#include "dbus-string.h"

35\#include "dbus-sysdeps.h"

36\#include "dbus-sysdeps-win.h"

37\#include "dbus-sockets-win.h"

38\#include "dbus-memory.h"

39\#include "dbus-pipe.h"

40

41\#include \<stdio.h\>

42\#include \<stdlib.h\>

43\#if HAVE_ERRNO_H

44\#include \<errno.h\>

45\#endif

46\#include \<winsock2.h\> // WSA error codes

47

48\#ifndef DBUS_WINCE

49\#include \<io.h\>

50\#include \<lm.h\>

51\#include \<sys/stat.h\>

52\#endif

53

54

64dbus_bool_t

65\_dbus_become_daemon (const DBusString \*pidfile,

66 DBusPipe \*print_pid_pipe,

67 DBusError \*error,

68 dbus_bool_t keep_umask)

69{

70 dbus_set_error (error, DBUS_ERROR_NOT_SUPPORTED,

71 "Cannot daemonize on Windows");

72 return FALSE;

73}

74

83static dbus_bool_t

84\_dbus_write_pid_file (const DBusString \*filename,

85 unsigned long pid,

86 DBusError \*error)

87{

88 const char \*cfilename;

89 HANDLE hnd;

90 char pidstr\[20\];

91 int total;

92 int bytes_to_write;

93

94 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

95

96 cfilename = \_dbus_string_get_const_data (filename);

97

98 hnd = CreateFileA (cfilename, GENERIC_WRITE,

99 FILE_SHARE_READ \| FILE_SHARE_WRITE,

100 NULL, CREATE_NEW, FILE_ATTRIBUTE_NORMAL,

101 INVALID_HANDLE_VALUE);

102 if (hnd == INVALID_HANDLE_VALUE)

103 {

104 char \*emsg = \_dbus_win_error_string (GetLastError ());

105 dbus_set_error (error, \_dbus_win_error_from_last_error (),

106 "Could not create PID file %s: %s",

107 cfilename, emsg);

108 \_dbus_win_free_error_string (emsg);

109 return FALSE;

110 }

111

112 if (snprintf (pidstr, sizeof (pidstr), "%lu\n", pid) \< 0)

113 {

114 dbus_set_error (error, \_dbus_error_from_system_errno (),

115 "Failed to format PID for \\%s\\: %s", cfilename,

116 \_dbus_strerror_from_errno ());

117 CloseHandle (hnd);

118 return FALSE;

119 }

120

121 total = 0;

122 bytes_to_write = strlen (pidstr);;

123

124 while (total \< bytes_to_write)

125 {

126 DWORD bytes_written;

127 BOOL res;

128

129 res = WriteFile (hnd, pidstr + total, bytes_to_write - total,

130 &bytes_written, NULL);

131

132 if (res == 0 \|\| bytes_written \<= 0)

133 {

134 char \*emsg = \_dbus_win_error_string (GetLastError ());

135 dbus_set_error (error, \_dbus_win_error_from_last_error (),

136 "Could not write to %s: %s", cfilename, emsg);

137 \_dbus_win_free_error_string (emsg);

138 CloseHandle (hnd);

139 return FALSE;

140 }

141

142 total += bytes_written;

143 }

144

145 if (CloseHandle (hnd) == 0)

146 {

147 char \*emsg = \_dbus_win_error_string (GetLastError ());

148 dbus_set_error (error, \_dbus_win_error_from_last_error (),

149 "Could not close file %s: %s",

150 cfilename, emsg);

151 \_dbus_win_free_error_string (emsg);

152

153 return FALSE;

154 }

155

156 return TRUE;

157}

158

170dbus_bool_t

171\_dbus_write_pid_to_file_and_pipe (const DBusString \*pidfile,

172 DBusPipe \*print_pid_pipe,

173 dbus_pid_t pid_to_write,

174 DBusError \*error)

175{

176 if (pidfile)

177 {

178 \_dbus_verbose ("writing pid file %s\n", \_dbus_string_get_const_data (pidfile));

179 if (!\_dbus_write_pid_file (pidfile,

180 pid_to_write,

181 error))

182 {

183 \_dbus_verbose ("pid file write failed\n");

184 \_DBUS_ASSERT_ERROR_IS_SET(error);

185 return FALSE;

186 }

187 }

188 else

189 {

190 \_dbus_verbose ("No pid file requested\n");

191 }

192

193 if (print_pid_pipe != NULL && \_dbus_pipe_is_valid (print_pid_pipe))

194 {

195 DBusString pid;

196 int bytes;

197

198 \_dbus_verbose ("writing our pid to pipe %d\n", print_pid_pipe-\>fd);

199

200 if (!\_dbus_string_init (&pid))

201 {

202 \_DBUS_SET_OOM (error);

203 return FALSE;

204 }

205

206 if (!\_dbus_string_append_printf (&pid, DBUS_PID_FORMAT "\n", pid_to_write))

207 {

208 \_dbus_string_free (&pid);

209 \_DBUS_SET_OOM (error);

210 return FALSE;

211 }

212

213 bytes = \_dbus_string_get_length (&pid);

214 if (\_dbus_pipe_write (print_pid_pipe, &pid, 0, bytes, error) != bytes)

215 {

216 /\* \_dbus_pipe_write sets error only on failure, not short write \*/

217 if (error != NULL && !dbus_error_is_set(error))

218 {

219 dbus_set_error (error, DBUS_ERROR_FAILED,

220 "Printing message bus PID: did not write enough bytes\n");

221 }

222 \_dbus_string_free (&pid);

223 return FALSE;

224 }

225

226 \_dbus_string_free (&pid);

227 }

228 else

229 {

230 \_dbus_verbose ("No pid pipe to write to\n");

231 }

232

233 return TRUE;

234}

235

242dbus_bool_t

243\_dbus_verify_daemon_user (const char \*user)

244{

245 return TRUE;

246}

247

255dbus_bool_t

256\_dbus_change_to_daemon_user (const char \*user,

257 DBusError \*error)

258{

259 return TRUE;

260}

261

262static void

263fd_limit_not_supported (DBusError \*error)

264{

265 dbus_set_error (error, DBUS_ERROR_NOT_SUPPORTED,

266 "cannot change fd limit on this platform");

267}

268

269DBusRLimit \*

270\_dbus_rlimit_save_fd_limit (DBusError \*error)

271{

272 fd_limit_not_supported (error);

273 return NULL;

274}

275

276dbus_bool_t

277\_dbus_rlimit_raise_fd_limit (DBusError \*error)

278{

279 fd_limit_not_supported (error);

280 return FALSE;

281}

282

283dbus_bool_t

284\_dbus_rlimit_restore_fd_limit (DBusRLimit \*saved,

285 DBusError \*error)

286{

287 fd_limit_not_supported (error);

288 return FALSE;

289}

290

291void

292\_dbus_rlimit_free (DBusRLimit \*lim)

293{

294 /\* \_dbus_rlimit_save_fd_limit() cannot return non-NULL on Windows

295 \* so there cannot be anything to free \*/

296 \_dbus_assert (lim == NULL);

297}

298

307dbus_bool_t

308\_dbus_stat(const DBusString \*filename,

309 DBusStat \*statbuf,

310 DBusError \*error)

311{

312 const char \*filename_c;

313 WIN32_FILE_ATTRIBUTE_DATA wfad;

314 char \*lastdot;

315

316 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

317

318 filename_c = \_dbus_string_get_const_data (filename);

319

320 if (!GetFileAttributesExA (filename_c, GetFileExInfoStandard, &wfad))

321 {

322 \_dbus_win_set_error_from_win_error (error, GetLastError ());

323 return FALSE;

324 }

325

326 if (wfad.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)

327 statbuf-\>mode = \_S_IFDIR;

328 else

329 statbuf-\>mode = \_S_IFREG;

330

331 statbuf-\>mode \|= \_S_IREAD;

332 if (wfad.dwFileAttributes & FILE_ATTRIBUTE_READONLY)

333 statbuf-\>mode \|= \_S_IWRITE;

334

335 lastdot = strrchr (filename_c, '.');

336 if (lastdot && stricmp (lastdot, ".exe") == 0)

337 statbuf-\>mode \|= \_S_IEXEC;

338

339 statbuf-\>mode \|= (statbuf-\>mode & 0700) \>\> 3;

340 statbuf-\>mode \|= (statbuf-\>mode & 0700) \>\> 6;

341

342 statbuf-\>nlink = 1;

343

344\#ifdef ENABLE_UID_TO_SID

345 {

346 PSID owner_sid, group_sid;

347 PSECURITY_DESCRIPTOR sd;

348

349 sd = NULL;

350 rc = GetNamedSecurityInfo ((char \*) filename_c, SE_FILE_OBJECT,

351 OWNER_SECURITY_INFORMATION \|

352 GROUP_SECURITY_INFORMATION,

353 &owner_sid, &group_sid,

354 NULL, NULL,

355 &sd);

356 if (rc != ERROR_SUCCESS)

357 {

358 \_dbus_win_set_error_from_win_error (error, rc);

359 if (sd != NULL)

360 LocalFree (sd);

361 return FALSE;

362 }

363

364 /\* FIXME \*/

365 statbuf-\>uid = \_dbus_win_sid_to_uid_t (owner_sid);

366 statbuf-\>gid = \_dbus_win_sid_to_uid_t (group_sid);

367

368 LocalFree (sd);

369 }

370\#else

371 statbuf-\>uid = DBUS_UID_UNSET;

372 statbuf-\>gid = DBUS_GID_UNSET;

373\#endif

374

375 statbuf-\>size = ((dbus_int64_t) wfad.nFileSizeHigh \<\< 32) + wfad.nFileSizeLow;

376

377 statbuf-\>atime =

378 (((dbus_int64_t) wfad.ftLastAccessTime.dwHighDateTime \<\< 32) +

379 wfad.ftLastAccessTime.dwLowDateTime) / 10000000 - DBUS_INT64_CONSTANT (116444736000000000);

380

381 statbuf-\>mtime =

382 (((dbus_int64_t) wfad.ftLastWriteTime.dwHighDateTime \<\< 32) +

383 wfad.ftLastWriteTime.dwLowDateTime) / 10000000 - DBUS_INT64_CONSTANT (116444736000000000);

384

385 statbuf-\>ctime =

386 (((dbus_int64_t) wfad.ftCreationTime.dwHighDateTime \<\< 32) +

387 wfad.ftCreationTime.dwLowDateTime) / 10000000 - DBUS_INT64_CONSTANT (116444736000000000);

388

389 return TRUE;

390}

391

395struct DBusDirIter

396 {

397 HANDLE handle;

398 WIN32_FIND_DATAA fileinfo; /\* from FindFirst/FindNext \*/

399 dbus_bool_t finished; /\* true if there are no more entries \*/

400 int offset;

401 };

402

410DBusDirIter\*

411\_dbus_directory_open (const DBusString \*filename,

412 DBusError \*error)

413{

414 DBusDirIter \*iter;

415 DBusString filespec;

416

417 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

418

419 if (!\_dbus_string_init_from_string (&filespec, filename))

420 {

421 dbus_set_error (error, DBUS_ERROR_NO_MEMORY,

422 "Could not allocate memory for directory filename copy");

423 return NULL;

424 }

425

426 if (\_dbus_string_ends_with_c_str (&filespec, "/") \|\| \_dbus_string_ends_with_c_str (&filespec, "\\") )

427 {

428 if (!\_dbus_string_append (&filespec, "\*"))

429 {

430 \_dbus_string_free (&filespec);

431 dbus_set_error (error, DBUS_ERROR_NO_MEMORY,

432 "Could not append filename wildcard");

433 return NULL;

434 }

435 }

436 else if (!\_dbus_string_ends_with_c_str (&filespec, "\*"))

437 {

438 if (!\_dbus_string_append (&filespec, "\\\*"))

439 {

440 \_dbus_string_free (&filespec);

441 dbus_set_error (error, DBUS_ERROR_NO_MEMORY,

442 "Could not append filename wildcard 2");

443 return NULL;

444 }

445 }

446

447 iter = dbus_new0 (DBusDirIter, 1);

448 if (iter == NULL)

449 {

450 \_dbus_string_free (&filespec);

451 dbus_set_error (error, DBUS_ERROR_NO_MEMORY,

452 "Could not allocate memory for directory iterator");

453 return NULL;

454 }

455

456 iter-\>finished = FALSE;

457 iter-\>offset = 0;

458 iter-\>handle = FindFirstFileA (\_dbus_string_get_const_data (&filespec), &(iter-\>fileinfo));

459 if (iter-\>handle == INVALID_HANDLE_VALUE)

460 {

461 if (GetLastError () == ERROR_NO_MORE_FILES)

462 iter-\>finished = TRUE;

463 else

464 {

465 char \*emsg = \_dbus_win_error_string (GetLastError ());

466 dbus_set_error (error, \_dbus_win_error_from_last_error (),

467 "Failed to read directory \\%s\\: %s",

468 \_dbus_string_get_const_data (filename), emsg);

469 \_dbus_win_free_error_string (emsg);

470 dbus_free (iter);

471 \_dbus_string_free (&filespec);

472 return NULL;

473 }

474 }

475 \_dbus_string_free (&filespec);

476 return iter;

477}

478

489dbus_bool_t

490\_dbus_directory_get_next_file (DBusDirIter \*iter,

491 DBusString \*filename,

492 DBusError \*error)

493{

494 int saved_err = GetLastError();

495

496 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

497

498again:

499 SetLastError (0);

500

501 if (!iter \|\| iter-\>finished)

502 return FALSE;

503

504 if (iter-\>offset \> 0)

505 {

506 if (FindNextFileA (iter-\>handle, &(iter-\>fileinfo)) == 0)

507 {

508 if (GetLastError() == ERROR_NO_MORE_FILES)

509 {

510 SetLastError(saved_err);

511 iter-\>finished = 1;

512 }

513 else

514 {

515 char \*emsg = \_dbus_win_error_string (GetLastError ());

516 dbus_set_error (error, \_dbus_win_error_from_last_error (),

517 "Failed to get next in directory: %s", emsg);

518 \_dbus_win_free_error_string (emsg);

519 return FALSE;

520 }

521 }

522 }

523

524 iter-\>offset++;

525

526 if (iter-\>finished)

527 return FALSE;

528

529 if (iter-\>fileinfo.cFileName\[0\] == '.' &&

530 (iter-\>fileinfo.cFileName\[1\] == '\0' \|\|

531 (iter-\>fileinfo.cFileName\[1\] == '.' && iter-\>fileinfo.cFileName\[2\] == '\0')))

532 goto again;

533

534 \_dbus_string_set_length (filename, 0);

535 if (!\_dbus_string_append (filename, iter-\>fileinfo.cFileName))

536 {

537 dbus_set_error (error, DBUS_ERROR_NO_MEMORY,

538 "No memory to read directory entry");

539 return FALSE;

540 }

541

542 return TRUE;

543}

544

548void

549\_dbus_directory_close (DBusDirIter \*iter)

550{

551 if (!iter)

552 return;

553 FindClose(iter-\>handle);

554 dbus_free (iter);

555}

556

/\* End of DBusInternalsUtils functions \*/

558

570dbus_bool_t

571\_dbus_string_get_dirname(const DBusString \*filename,

572 DBusString \*dirname)

573{

574 int sep;

575

576 \_dbus_assert (filename != dirname);

577 \_dbus_assert (filename != NULL);

578 \_dbus_assert (dirname != NULL);

579

580 /\* Ignore any separators on the end \*/

581 sep = \_dbus_string_get_length (filename);

582 if (sep == 0)

583 return \_dbus_string_append (dirname, "."); /\* empty string passed in \*/

584

585 while (sep \> 0 &&

586 (\_dbus_string_get_byte (filename, sep - 1) == '/' \|\|

587 \_dbus_string_get_byte (filename, sep - 1) == '\\'))

588 --sep;

589

590 \_dbus_assert (sep \>= 0);

591

592 if (sep == 0 \|\|

593 (sep == 2 &&

594 \_dbus_string_get_byte (filename, 1) == ':' &&

595 isalpha (\_dbus_string_get_byte (filename, 0))))

596 return \_dbus_string_copy_len (filename, 0, sep + 1,

597 dirname, \_dbus_string_get_length (dirname));

598

599 {

600 int sep1, sep2;

601 \_dbus_string_find_byte_backward (filename, sep, '/', &sep1);

602 \_dbus_string_find_byte_backward (filename, sep, '\\', &sep2);

603

604 sep = MAX (sep1, sep2);

605 }

606 if (sep \< 0)

607 return \_dbus_string_append (dirname, ".");

608

609 while (sep \> 0 &&

610 (\_dbus_string_get_byte (filename, sep - 1) == '/' \|\|

611 \_dbus_string_get_byte (filename, sep - 1) == '\\'))

612 --sep;

613

614 \_dbus_assert (sep \>= 0);

615

616 if ((sep == 0 \|\|

617 (sep == 2 &&

618 \_dbus_string_get_byte (filename, 1) == ':' &&

619 isalpha (\_dbus_string_get_byte (filename, 0))))

620 &&

621 (\_dbus_string_get_byte (filename, sep) == '/' \|\|

622 \_dbus_string_get_byte (filename, sep) == '\\'))

623 return \_dbus_string_copy_len (filename, 0, sep + 1,

624 dirname, \_dbus_string_get_length (dirname));

625 else

626 return \_dbus_string_copy_len (filename, 0, sep - 0,

627 dirname, \_dbus_string_get_length (dirname));

628}

629

630

638dbus_bool_t

639\_dbus_unix_user_is_process_owner (dbus_uid_t uid)

640{

641 return FALSE;

642}

643

644dbus_bool_t \_dbus_windows_user_is_process_owner (const char \*windows_sid)

645{

646 return TRUE;

647}

648

649/\*=====================================================================

650 unix emulation functions - should be removed sometime in the future

651 =====================================================================\*/

652

653static void

654set_unix_uid_unsupported (DBusError \*error)

655{

656 dbus_set_error (error, DBUS_ERROR_NOT_SUPPORTED,

657 "UNIX user IDs not supported on Windows");

658}

659

669dbus_bool_t

670\_dbus_unix_user_is_at_console (dbus_uid_t uid,

671 DBusError \*error)

672{

673 set_unix_uid_unsupported (error);

674 return FALSE;

675}

676

677

686dbus_bool_t

687\_dbus_parse_unix_group_from_config (const DBusString \*groupname,

688 dbus_gid_t \*gid_p)

689{

690 return FALSE;

691}

692

701dbus_bool_t

702\_dbus_parse_unix_user_from_config (const DBusString \*username,

703 dbus_uid_t \*uid_p)

704{

705 return FALSE;

706}

707

708

720dbus_bool_t

721\_dbus_unix_groups_from_uid (dbus_uid_t uid,

722 dbus_gid_t \*\*group_ids,

723 int \*n_group_ids,

724 DBusError \*error)

725{

726 set_unix_uid_unsupported (error);

727 return FALSE;

728}

729

730

731

/\* DBusString stuff \*/

733

734/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

735

736 error handling

737

738 \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

739

740

741

742

743

744/\* lan manager error codes \*/

745const char\*

746\_dbus_lm_strerror(int error_number)

747{

748\#ifdef DBUS_WINCE

749 // TODO

750 return "unknown";

751\#else

752 const char \*msg;

753 switch (error_number)

754 {

755 case NERR_NetNotStarted:

756 return "The workstation driver is not installed.";

757 case NERR_UnknownServer:

758 return "The server could not be located.";

759 case NERR_ShareMem:

760 return "An internal error occurred. The network cannot access a shared memory segment.";

761 case NERR_NoNetworkResource:

762 return "A network resource shortage occurred.";

763 case NERR_RemoteOnly:

764 return "This operation is not supported on workstations.";

765 case NERR_DevNotRedirected:

766 return "The device is not connected.";

767 case NERR_ServerNotStarted:

768 return "The Server service is not started.";

769 case NERR_ItemNotFound:

770 return "The queue is empty.";

771 case NERR_UnknownDevDir:

772 return "The device or directory does not exist.";

773 case NERR_RedirectedPath:

774 return "The operation is invalid on a redirected resource.";

775 case NERR_DuplicateShare:

776 return "The name has already been shared.";

777 case NERR_NoRoom:

778 return "The server is currently out of the requested resource.";

779 case NERR_TooManyItems:

780 return "Requested addition of items exceeds the maximum allowed.";

781 case NERR_InvalidMaxUsers:

782 return "The Peer service supports only two simultaneous users.";

783 case NERR_BufTooSmall:

784 return "The API return buffer is too small.";

785 case NERR_RemoteErr:

786 return "A remote API error occurred.";

787 case NERR_LanmanIniError:

788 return "An error occurred when opening or reading the configuration file.";

789 case NERR_NetworkError:

790 return "A general network error occurred.";

791 case NERR_WkstaInconsistentState:

792 return "The Workstation service is in an inconsistent state. Restart the computer before restarting the Workstation service.";

793 case NERR_WkstaNotStarted:

794 return "The Workstation service has not been started.";

795 case NERR_BrowserNotStarted:

796 return "The requested information is not available.";

797 case NERR_InternalError:

798 return "An internal error occurred.";

799 case NERR_BadTransactConfig:

800 return "The server is not configured for transactions.";

801 case NERR_InvalidAPI:

802 return "The requested API is not supported on the remote server.";

803 case NERR_BadEventName:

804 return "The event name is invalid.";

805 case NERR_DupNameReboot:

806 return "The computer name already exists on the network. Change it and restart the computer.";

807 case NERR_CfgCompNotFound:

808 return "The specified component could not be found in the configuration information.";

809 case NERR_CfgParamNotFound:

810 return "The specified parameter could not be found in the configuration information.";

811 case NERR_LineTooLong:

812 return "A line in the configuration file is too long.";

813 case NERR_QNotFound:

814 return "The printer does not exist.";

815 case NERR_JobNotFound:

816 return "The print job does not exist.";

817 case NERR_DestNotFound:

818 return "The printer destination cannot be found.";

819 case NERR_DestExists:

820 return "The printer destination already exists.";

821 case NERR_QExists:

822 return "The printer queue already exists.";

823 case NERR_QNoRoom:

824 return "No more printers can be added.";

825 case NERR_JobNoRoom:

826 return "No more print jobs can be added.";

827 case NERR_DestNoRoom:

828 return "No more printer destinations can be added.";

829 case NERR_DestIdle:

830 return "This printer destination is idle and cannot accept control operations.";

831 case NERR_DestInvalidOp:

832 return "This printer destination request contains an invalid control function.";

833 case NERR_ProcNoRespond:

834 return "The print processor is not responding.";

835 case NERR_SpoolerNotLoaded:

836 return "The spooler is not running.";

837 case NERR_DestInvalidState:

838 return "This operation cannot be performed on the print destination in its current state.";

839 case NERR_QInvalidState:

840 return "This operation cannot be performed on the printer queue in its current state.";

841 case NERR_JobInvalidState:

842 return "This operation cannot be performed on the print job in its current state.";

843 case NERR_SpoolNoMemory:

844 return "A spooler memory allocation failure occurred.";

845 case NERR_DriverNotFound:

846 return "The device driver does not exist.";

847 case NERR_DataTypeInvalid:

848 return "The data type is not supported by the print processor.";

849 case NERR_ProcNotFound:

850 return "The print processor is not installed.";

851 case NERR_ServiceTableLocked:

852 return "The service database is locked.";

853 case NERR_ServiceTableFull:

854 return "The service table is full.";

855 case NERR_ServiceInstalled:

856 return "The requested service has already been started.";

857 case NERR_ServiceEntryLocked:

858 return "The service does not respond to control actions.";

859 case NERR_ServiceNotInstalled:

860 return "The service has not been started.";

861 case NERR_BadServiceName:

862 return "The service name is invalid.";

863 case NERR_ServiceCtlTimeout:

864 return "The service is not responding to the control function.";

865 case NERR_ServiceCtlBusy:

866 return "The service control is busy.";

867 case NERR_BadServiceProgName:

868 return "The configuration file contains an invalid service program name.";

869 case NERR_ServiceNotCtrl:

870 return "The service could not be controlled in its present state.";

871 case NERR_ServiceKillProc:

872 return "The service ended abnormally.";

873 case NERR_ServiceCtlNotValid:

874 return "The requested pause or stop is not valid for this service.";

875 case NERR_NotInDispatchTbl:

876 return "The service control dispatcher could not find the service name in the dispatch table.";

877 case NERR_BadControlRecv:

878 return "The service control dispatcher pipe read failed.";

879 case NERR_ServiceNotStarting:

880 return "A thread for the new service could not be created.";

881 case NERR_AlreadyLoggedOn:

882 return "This workstation is already logged on to the local-area network.";

883 case NERR_NotLoggedOn:

884 return "The workstation is not logged on to the local-area network.";

885 case NERR_BadUsername:

886 return "The user name or group name parameter is invalid.";

887 case NERR_BadPassword:

888 return "The password parameter is invalid.";

889 case NERR_UnableToAddName_W:

890 return "@W The logon processor did not add the message alias.";

891 case NERR_UnableToAddName_F:

892 return "The logon processor did not add the message alias.";

893 case NERR_UnableToDelName_W:

894 return "@W The logoff processor did not delete the message alias.";

895 case NERR_UnableToDelName_F:

896 return "The logoff processor did not delete the message alias.";

897 case NERR_LogonsPaused:

898 return "Network logons are paused.";

899 case NERR_LogonServerConflict:

900 return "A centralized logon-server conflict occurred.";

901 case NERR_LogonNoUserPath:

902 return "The server is configured without a valid user path.";

903 case NERR_LogonScriptError:

904 return "An error occurred while loading or running the logon script.";

905 case NERR_StandaloneLogon:

906 return "The logon server was not specified. Your computer will be logged on as STANDALONE.";

907 case NERR_LogonServerNotFound:

908 return "The logon server could not be found.";

909 case NERR_LogonDomainExists:

910 return "There is already a logon domain for this computer.";

911 case NERR_NonValidatedLogon:

912 return "The logon server could not validate the logon.";

913 case NERR_ACFNotFound:

914 return "The security database could not be found.";

915 case NERR_GroupNotFound:

916 return "The group name could not be found.";

917 case NERR_UserNotFound:

918 return "The user name could not be found.";

919 case NERR_ResourceNotFound:

920 return "The resource name could not be found.";

921 case NERR_GroupExists:

922 return "The group already exists.";

923 case NERR_UserExists:

924 return "The user account already exists.";

925 case NERR_ResourceExists:

926 return "The resource permission list already exists.";

927 case NERR_NotPrimary:

928 return "This operation is only allowed on the primary domain controller of the domain.";

929 case NERR_ACFNotLoaded:

930 return "The security database has not been started.";

931 case NERR_ACFNoRoom:

932 return "There are too many names in the user accounts database.";

933 case NERR_ACFFileIOFail:

934 return "A disk I/O failure occurred.";

935 case NERR_ACFTooManyLists:

936 return "The limit of 64 entries per resource was exceeded.";

937 case NERR_UserLogon:

938 return "Deleting a user with a session is not allowed.";

939 case NERR_ACFNoParent:

940 return "The parent directory could not be located.";

941 case NERR_CanNotGrowSegment:

942 return "Unable to add to the security database session cache segment.";

943 case NERR_SpeGroupOp:

944 return "This operation is not allowed on this special group.";

945 case NERR_NotInCache:

946 return "This user is not cached in user accounts database session cache.";

947 case NERR_UserInGroup:

948 return "The user already belongs to this group.";

949 case NERR_UserNotInGroup:

950 return "The user does not belong to this group.";

951 case NERR_AccountUndefined:

952 return "This user account is undefined.";

953 case NERR_AccountExpired:

954 return "This user account has expired.";

955 case NERR_InvalidWorkstation:

956 return "The user is not allowed to log on from this workstation.";

957 case NERR_InvalidLogonHours:

958 return "The user is not allowed to log on at this time.";

959 case NERR_PasswordExpired:

960 return "The password of this user has expired.";

961 case NERR_PasswordCantChange:

962 return "The password of this user cannot change.";

963 case NERR_PasswordHistConflict:

964 return "This password cannot be used now.";

965 case NERR_PasswordTooShort:

966 return "The password does not meet the password policy requirements. Check the minimum password length, password complexity and password history requirements.";

967 case NERR_PasswordTooRecent:

968 return "The password of this user is too recent to change.";

969 case NERR_InvalidDatabase:

970 return "The security database is corrupted.";

971 case NERR_DatabaseUpToDate:

972 return "No updates are necessary to this replicant network/local security database.";

973 case NERR_SyncRequired:

974 return "This replicant database is outdated; synchronization is required.";

975 case NERR_UseNotFound:

976 return "The network connection could not be found.";

977 case NERR_BadAsgType:

978 return "This asg_type is invalid.";

979 case NERR_DeviceIsShared:

980 return "This device is currently being shared.";

981 case NERR_NoComputerName:

982 return "The computer name could not be added as a message alias. The name may already exist on the network.";

983 case NERR_MsgAlreadyStarted:

984 return "The Messenger service is already started.";

985 case NERR_MsgInitFailed:

986 return "The Messenger service failed to start.";

987 case NERR_NameNotFound:

988 return "The message alias could not be found on the network.";

989 case NERR_AlreadyForwarded:

990 return "This message alias has already been forwarded.";

991 case NERR_AddForwarded:

992 return "This message alias has been added but is still forwarded.";

993 case NERR_AlreadyExists:

994 return "This message alias already exists locally.";

995 case NERR_TooManyNames:

996 return "The maximum number of added message aliases has been exceeded.";

997 case NERR_DelComputerName:

998 return "The computer name could not be deleted.";

999 case NERR_LocalForward:

1000 return "Messages cannot be forwarded back to the same workstation.";

1001 case NERR_GrpMsgProcessor:

1002 return "An error occurred in the domain message processor.";

1003 case NERR_PausedRemote:

1004 return "The message was sent, but the recipient has paused the Messenger service.";

1005 case NERR_BadReceive:

1006 return "The message was sent but not received.";

1007 case NERR_NameInUse:

1008 return "The message alias is currently in use. Try again later.";

1009 case NERR_MsgNotStarted:

1010 return "The Messenger service has not been started.";

1011 case NERR_NotLocalName:

1012 return "The name is not on the local computer.";

1013 case NERR_NoForwardName:

1014 return "The forwarded message alias could not be found on the network.";

1015 case NERR_RemoteFull:

1016 return "The message alias table on the remote station is full.";

1017 case NERR_NameNotForwarded:

1018 return "Messages for this alias are not currently being forwarded.";

1019 case NERR_TruncatedBroadcast:

1020 return "The broadcast message was truncated.";

1021 case NERR_InvalidDevice:

1022 return "This is an invalid device name.";

1023 case NERR_WriteFault:

1024 return "A write fault occurred.";

1025 case NERR_DuplicateName:

1026 return "A duplicate message alias exists on the network.";

1027 case NERR_DeleteLater:

1028 return "@W This message alias will be deleted later.";

1029 case NERR_IncompleteDel:

1030 return "The message alias was not successfully deleted from all networks.";

1031 case NERR_MultipleNets:

1032 return "This operation is not supported on computers with multiple networks.";

1033 case NERR_NetNameNotFound:

1034 return "This shared resource does not exist.";

1035 case NERR_DeviceNotShared:

1036 return "This device is not shared.";

1037 case NERR_ClientNameNotFound:

1038 return "A session does not exist with that computer name.";

1039 case NERR_FileIdNotFound:

1040 return "There is not an open file with that identification number.";

1041 case NERR_ExecFailure:

1042 return "A failure occurred when executing a remote administration command.";

1043 case NERR_TmpFile:

1044 return "A failure occurred when opening a remote temporary file.";

1045 case NERR_TooMuchData:

1046 return "The data returned from a remote administration command has been truncated to 64K.";

1047 case NERR_DeviceShareConflict:

1048 return "This device cannot be shared as both a spooled and a non-spooled resource.";

1049 case NERR_BrowserTableIncomplete:

1050 return "The information in the list of servers may be incorrect.";

1051 case NERR_NotLocalDomain:

1052 return "The computer is not active in this domain.";

1053\#ifdef NERR_IsDfsShare

1054

1055 case NERR_IsDfsShare:

1056 return "The share must be removed from the Distributed File System before it can be deleted.";

1057\#endif

1058

1059 case NERR_DevInvalidOpCode:

1060 return "The operation is invalid for this device.";

1061 case NERR_DevNotFound:

1062 return "This device cannot be shared.";

1063 case NERR_DevNotOpen:

1064 return "This device was not open.";

1065 case NERR_BadQueueDevString:

1066 return "This device name list is invalid.";

1067 case NERR_BadQueuePriority:

1068 return "The queue priority is invalid.";

1069 case NERR_NoCommDevs:

1070 return "There are no shared communication devices.";

1071 case NERR_QueueNotFound:

1072 return "The queue you specified does not exist.";

1073 case NERR_BadDevString:

1074 return "This list of devices is invalid.";

1075 case NERR_BadDev:

1076 return "The requested device is invalid.";

1077 case NERR_InUseBySpooler:

1078 return "This device is already in use by the spooler.";

1079 case NERR_CommDevInUse:

1080 return "This device is already in use as a communication device.";

1081 case NERR_InvalidComputer:

1082 return "This computer name is invalid.";

1083 case NERR_MaxLenExceeded:

1084 return "The string and prefix specified are too long.";

1085 case NERR_BadComponent:

1086 return "This path component is invalid.";

1087 case NERR_CantType:

1088 return "Could not determine the type of input.";

1089 case NERR_TooManyEntries:

1090 return "The buffer for types is not big enough.";

1091 case NERR_ProfileFileTooBig:

1092 return "Profile files cannot exceed 64K.";

1093 case NERR_ProfileOffset:

1094 return "The start offset is out of range.";

1095 case NERR_ProfileCleanup:

1096 return "The system cannot delete current connections to network resources.";

1097 case NERR_ProfileUnknownCmd:

1098 return "The system was unable to parse the command line in this file.";

1099 case NERR_ProfileLoadErr:

1100 return "An error occurred while loading the profile file.";

1101 case NERR_ProfileSaveErr:

1102 return "@W Errors occurred while saving the profile file. The profile was partially saved.";

1103 case NERR_LogOverflow:

1104 return "Log file %1 is full.";

1105 case NERR_LogFileChanged:

1106 return "This log file has changed between reads.";

1107 case NERR_LogFileCorrupt:

1108 return "Log file %1 is corrupt.";

1109 case NERR_SourceIsDir:

1110 return "The source path cannot be a directory.";

1111 case NERR_BadSource:

1112 return "The source path is illegal.";

1113 case NERR_BadDest:

1114 return "The destination path is illegal.";

1115 case NERR_DifferentServers:

1116 return "The source and destination paths are on different servers.";

1117 case NERR_RunSrvPaused:

1118 return "The Run server you requested is paused.";

1119 case NERR_ErrCommRunSrv:

1120 return "An error occurred when communicating with a Run server.";

1121 case NERR_ErrorExecingGhost:

1122 return "An error occurred when starting a background process.";

1123 case NERR_ShareNotFound:

1124 return "The shared resource you are connected to could not be found.";

1125 case NERR_InvalidLana:

1126 return "The LAN adapter number is invalid.";

1127 case NERR_OpenFiles:

1128 return "There are open files on the connection.";

1129 case NERR_ActiveConns:

1130 return "Active connections still exist.";

1131 case NERR_BadPasswordCore:

1132 return "This share name or password is invalid.";

1133 case NERR_DevInUse:

1134 return "The device is being accessed by an active process.";

1135 case NERR_LocalDrive:

1136 return "The drive letter is in use locally.";

1137 case NERR_AlertExists:

1138 return "The specified client is already registered for the specified event.";

1139 case NERR_TooManyAlerts:

1140 return "The alert table is full.";

1141 case NERR_NoSuchAlert:

1142 return "An invalid or nonexistent alert name was raised.";

1143 case NERR_BadRecipient:

1144 return "The alert recipient is invalid.";

1145 case NERR_AcctLimitExceeded:

1146 return "A user's session with this server has been deleted.";

1147 case NERR_InvalidLogSeek:

1148 return "The log file does not contain the requested record number.";

1149 case NERR_BadUasConfig:

1150 return "The user accounts database is not configured correctly.";

1151 case NERR_InvalidUASOp:

1152 return "This operation is not permitted when the Netlogon service is running.";

1153 case NERR_LastAdmin:

1154 return "This operation is not allowed on the last administrative account.";

1155 case NERR_DCNotFound:

1156 return "Could not find domain controller for this domain.";

1157 case NERR_LogonTrackingError:

1158 return "Could not set logon information for this user.";

1159 case NERR_NetlogonNotStarted:

1160 return "The Netlogon service has not been started.";

1161 case NERR_CanNotGrowUASFile:

1162 return "Unable to add to the user accounts database.";

1163 case NERR_TimeDiffAtDC:

1164 return "This server's clock is not synchronized with the primary domain controller's clock.";

1165 case NERR_PasswordMismatch:

1166 return "A password mismatch has been detected.";

1167 case NERR_NoSuchServer:

1168 return "The server identification does not specify a valid server.";

1169 case NERR_NoSuchSession:

1170 return "The session identification does not specify a valid session.";

1171 case NERR_NoSuchConnection:

1172 return "The connection identification does not specify a valid connection.";

1173 case NERR_TooManyServers:

1174 return "There is no space for another entry in the table of available servers.";

1175 case NERR_TooManySessions:

1176 return "The server has reached the maximum number of sessions it supports.";

1177 case NERR_TooManyConnections:

1178 return "The server has reached the maximum number of connections it supports.";

1179 case NERR_TooManyFiles:

1180 return "The server cannot open more files because it has reached its maximum number.";

1181 case NERR_NoAlternateServers:

1182 return "There are no alternate servers registered on this server.";

1183 case NERR_TryDownLevel:

1184 return "Try down-level (remote admin protocol) version of API instead.";

1185 case NERR_UPSDriverNotStarted:

1186 return "The UPS driver could not be accessed by the UPS service.";

1187 case NERR_UPSInvalidConfig:

1188 return "The UPS service is not configured correctly.";

1189 case NERR_UPSInvalidCommPort:

1190 return "The UPS service could not access the specified Comm Port.";

1191 case NERR_UPSSignalAsserted:

1192 return "The UPS indicated a line fail or low battery situation. Service not started.";

1193 case NERR_UPSShutdownFailed:

1194 return "The UPS service failed to perform a system shut down.";

1195 case NERR_BadDosRetCode:

1196 return "The program below returned an MS-DOS error code:";

1197 case NERR_ProgNeedsExtraMem:

1198 return "The program below needs more memory:";

1199 case NERR_BadDosFunction:

1200 return "The program below called an unsupported MS-DOS function:";

1201 case NERR_RemoteBootFailed:

1202 return "The workstation failed to boot.";

1203 case NERR_BadFileCheckSum:

1204 return "The file below is corrupt.";

1205 case NERR_NoRplBootSystem:

1206 return "No loader is specified in the boot-block definition file.";

1207 case NERR_RplLoadrNetBiosErr:

1208 return "NetBIOS returned an error: The NCB and SMB are dumped above.";

1209 case NERR_RplLoadrDiskErr:

1210 return "A disk I/O error occurred.";

1211 case NERR_ImageParamErr:

1212 return "Image parameter substitution failed.";

1213 case NERR_TooManyImageParams:

1214 return "Too many image parameters cross disk sector boundaries.";

1215 case NERR_NonDosFloppyUsed:

1216 return "The image was not generated from an MS-DOS diskette formatted with /S.";

1217 case NERR_RplBootRestart:

1218 return "Remote boot will be restarted later.";

1219 case NERR_RplSrvrCallFailed:

1220 return "The call to the Remoteboot server failed.";

1221 case NERR_CantConnectRplSrvr:

1222 return "Cannot connect to the Remoteboot server.";

1223 case NERR_CantOpenImageFile:

1224 return "Cannot open image file on the Remoteboot server.";

1225 case NERR_CallingRplSrvr:

1226 return "Connecting to the Remoteboot server...";

1227 case NERR_StartingRplBoot:

1228 return "Connecting to the Remoteboot server...";

1229 case NERR_RplBootServiceTerm:

1230 return "Remote boot service was stopped; check the error log for the cause of the problem.";

1231 case NERR_RplBootStartFailed:

1232 return "Remote boot startup failed; check the error log for the cause of the problem.";

1233 case NERR_RPL_CONNECTED:

1234 return "A second connection to a Remoteboot resource is not allowed.";

1235 case NERR_BrowserConfiguredToNotRun:

1236 return "The browser service was configured with MaintainServerList=No.";

1237 case NERR_RplNoAdaptersStarted:

1238 return "Service failed to start since none of the network adapters started with this service.";

1239 case NERR_RplBadRegistry:

1240 return "Service failed to start due to bad startup information in the registry.";

1241 case NERR_RplBadDatabase:

1242 return "Service failed to start because its database is absent or corrupt.";

1243 case NERR_RplRplfilesShare:

1244 return "Service failed to start because RPLFILES share is absent.";

1245 case NERR_RplNotRplServer:

1246 return "Service failed to start because RPLUSER group is absent.";

1247 case NERR_RplCannotEnum:

1248 return "Cannot enumerate service records.";

1249 case NERR_RplWkstaInfoCorrupted:

1250 return "Workstation record information has been corrupted.";

1251 case NERR_RplWkstaNotFound:

1252 return "Workstation record was not found.";

1253 case NERR_RplWkstaNameUnavailable:

1254 return "Workstation name is in use by some other workstation.";

1255 case NERR_RplProfileInfoCorrupted:

1256 return "Profile record information has been corrupted.";

1257 case NERR_RplProfileNotFound:

1258 return "Profile record was not found.";

1259 case NERR_RplProfileNameUnavailable:

1260 return "Profile name is in use by some other profile.";

1261 case NERR_RplProfileNotEmpty:

1262 return "There are workstations using this profile.";

1263 case NERR_RplConfigInfoCorrupted:

1264 return "Configuration record information has been corrupted.";

1265 case NERR_RplConfigNotFound:

1266 return "Configuration record was not found.";

1267 case NERR_RplAdapterInfoCorrupted:

1268 return "Adapter ID record information has been corrupted.";

1269 case NERR_RplInternal:

1270 return "An internal service error has occurred.";

1271 case NERR_RplVendorInfoCorrupted:

1272 return "Vendor ID record information has been corrupted.";

1273 case NERR_RplBootInfoCorrupted:

1274 return "Boot block record information has been corrupted.";

1275 case NERR_RplWkstaNeedsUserAcct:

1276 return "The user account for this workstation record is missing.";

1277 case NERR_RplNeedsRPLUSERAcct:

1278 return "The RPLUSER local group could not be found.";

1279 case NERR_RplBootNotFound:

1280 return "Boot block record was not found.";

1281 case NERR_RplIncompatibleProfile:

1282 return "Chosen profile is incompatible with this workstation.";

1283 case NERR_RplAdapterNameUnavailable:

1284 return "Chosen network adapter ID is in use by some other workstation.";

1285 case NERR_RplConfigNotEmpty:

1286 return "There are profiles using this configuration.";

1287 case NERR_RplBootInUse:

1288 return "There are workstations, profiles, or configurations using this boot block.";

1289 case NERR_RplBackupDatabase:

1290 return "Service failed to backup Remoteboot database.";

1291 case NERR_RplAdapterNotFound:

1292 return "Adapter record was not found.";

1293 case NERR_RplVendorNotFound:

1294 return "Vendor record was not found.";

1295 case NERR_RplVendorNameUnavailable:

1296 return "Vendor name is in use by some other vendor record.";

1297 case NERR_RplBootNameUnavailable:

1298 return "(boot name, vendor ID) is in use by some other boot block record.";

1299 case NERR_RplConfigNameUnavailable:

1300 return "Configuration name is in use by some other configuration.";

1301 case NERR_DfsInternalCorruption:

1302 return "The internal database maintained by the Dfs service is corrupt.";

1303 case NERR_DfsVolumeDataCorrupt:

1304 return "One of the records in the internal Dfs database is corrupt.";

1305 case NERR_DfsNoSuchVolume:

1306 return "There is no DFS name whose entry path matches the input Entry Path.";

1307 case NERR_DfsVolumeAlreadyExists:

1308 return "A root or link with the given name already exists.";

1309 case NERR_DfsAlreadyShared:

1310 return "The server share specified is already shared in the Dfs.";

1311 case NERR_DfsNoSuchShare:

1312 return "The indicated server share does not support the indicated DFS namespace.";

1313 case NERR_DfsNotALeafVolume:

1314 return "The operation is not valid on this portion of the namespace.";

1315 case NERR_DfsLeafVolume:

1316 return "The operation is not valid on this portion of the namespace.";

1317 case NERR_DfsVolumeHasMultipleServers:

1318 return "The operation is ambiguous because the link has multiple servers.";

1319 case NERR_DfsCantCreateJunctionPoint:

1320 return "Unable to create a link.";

1321 case NERR_DfsServerNotDfsAware:

1322 return "The server is not Dfs Aware.";

1323 case NERR_DfsBadRenamePath:

1324 return "The specified rename target path is invalid.";

1325 case NERR_DfsVolumeIsOffline:

1326 return "The specified DFS link is offline.";

1327 case NERR_DfsNoSuchServer:

1328 return "The specified server is not a server for this link.";

1329 case NERR_DfsCyclicalName:

1330 return "A cycle in the Dfs name was detected.";

1331 case NERR_DfsNotSupportedInServerDfs:

1332 return "The operation is not supported on a server-based Dfs.";

1333 case NERR_DfsDuplicateService:

1334 return "This link is already supported by the specified server-share.";

1335 case NERR_DfsCantRemoveLastServerShare:

1336 return "Can't remove the last server-share supporting this root or link.";

1337 case NERR_DfsVolumeIsInterDfs:

1338 return "The operation is not supported for an Inter-DFS link.";

1339 case NERR_DfsInconsistent:

1340 return "The internal state of the Dfs Service has become inconsistent.";

1341 case NERR_DfsServerUpgraded:

1342 return "The Dfs Service has been installed on the specified server.";

1343 case NERR_DfsDataIsIdentical:

1344 return "The Dfs data being reconciled is identical.";

1345 case NERR_DfsCantRemoveDfsRoot:

1346 return "The DFS root cannot be deleted. Uninstall DFS if required.";

1347 case NERR_DfsChildOrParentInDfs:

1348 return "A child or parent directory of the share is already in a Dfs.";

1349 case NERR_DfsInternalError:

1350 return "Dfs internal error.";

1351 /\* the following are not defined in mingw \*/

1352\#if 0

1353

1354 case NERR_SetupAlreadyJoined:

1355 return "This machine is already joined to a domain.";

1356 case NERR_SetupNotJoined:

1357 return "This machine is not currently joined to a domain.";

1358 case NERR_SetupDomainController:

1359 return "This machine is a domain controller and cannot be unjoined from a domain.";

1360 case NERR_DefaultJoinRequired:

1361 return "The destination domain controller does not support creating machine accounts in OUs.";

1362 case NERR_InvalidWorkgroupName:

1363 return "The specified workgroup name is invalid.";

1364 case NERR_NameUsesIncompatibleCodePage:

1365 return "The specified computer name is incompatible with the default language used on the domain controller.";

1366 case NERR_ComputerAccountNotFound:

1367 return "The specified computer account could not be found.";

1368 case NERR_PersonalSku:

1369 return "This version of Windows cannot be joined to a domain.";

1370 case NERR_PasswordMustChange:

1371 return "The password must change at the next logon.";

1372 case NERR_AccountLockedOut:

1373 return "The account is locked out.";

1374 case NERR_PasswordTooLong:

1375 return "The password is too long.";

1376 case NERR_PasswordNotComplexEnough:

1377 return "The password does not meet the complexity policy.";

1378 case NERR_PasswordFilterError:

1379 return "The password does not meet the requirements of the password filter DLLs.";

1380\#endif

1381

1382 default:

1383 msg = strerror (error_number);

1384

1385 if (msg == NULL)

1386 msg = "unknown";

1387

1388 return msg;

1389 }

1390\#endif //DBUS_WINCE

1391}

1392

1407dbus_bool_t

1408\_dbus_command_for_pid (unsigned long pid,

1409 DBusString \*str,

1410 int max_len,

1411 DBusError \*error)

1412{

1413 dbus_set_error (error, DBUS_ERROR_NOT_SUPPORTED,

1414 "\_dbus_command_for_pid() not implemented on Windows");

1415 return FALSE;

1416}

1417

1426dbus_bool_t

1427\_dbus_replace_install_prefix (DBusString \*path)

1428{

1429\#ifndef DBUS_PREFIX

1430 /\* leave path unchanged \*/

1431 return TRUE;

1432\#else

1433 DBusString runtime_prefix;

1434 int i;

1435

1436 if (!\_dbus_string_init (&runtime_prefix))

1437 return FALSE;

1438

1439 if (!\_dbus_get_install_root (&runtime_prefix))

1440 {

1441 \_dbus_string_free (&runtime_prefix);

1442 return FALSE;

1443 }

1444

1445 if (\_dbus_string_get_length (&runtime_prefix) == 0)

1446 {

1447 /\* cannot determine install root, leave path unchanged \*/

1448 \_dbus_string_free (&runtime_prefix);

1449 return TRUE;

1450 }

1451

1452 if (\_dbus_string_starts_with_c_str (path, DBUS_PREFIX "/"))

1453 {

1454 /\* Replace DBUS_PREFIX "/" with runtime_prefix.

1455 \* Note unusual calling convention: source is first, then dest \*/

1456 if (!\_dbus_string_replace_len (

1457 &runtime_prefix, 0, \_dbus_string_get_length (&runtime_prefix),

1458 path, 0, strlen (DBUS_PREFIX) + 1))

1459 {

1460 \_dbus_string_free (&runtime_prefix);

1461 return FALSE;

1462 }

1463 }

1464

1465 /\* Somehow, in some situations, backslashes get collapsed in the string.

1466 \* Since windows C library accepts both forward and backslashes as

1467 \* path separators, convert all backslashes to forward slashes.

1468 \*/

1469

1470 for (i = 0; i \< \_dbus_string_get_length (path); i++)

1471 {

1472 if (\_dbus_string_get_byte (path, i) == '\\')

1473 \_dbus_string_set_byte (path, i, '/');

1474 }

1475

1476 \_dbus_string_free (&runtime_prefix);

1477 return TRUE;

1478\#endif

1479}

1480

1481\#define DBUS_STANDARD_SESSION_SERVICEDIR "/dbus-1/services"

1482\#define DBUS_STANDARD_SYSTEM_SERVICEDIR "/dbus-1/system-services"

1483

1491dbus_bool_t

1492\_dbus_set_up_transient_session_servicedirs (DBusList \*\*dirs,

1493 DBusError \*error)

1494{

1495 /\* Not an error, we just don't have transient session services on Windows \*/

1496 return TRUE;

1497}

1498

1515dbus_bool_t

1516\_dbus_get_standard_session_servicedirs (DBusList \*\*dirs)

1517{

1518 const char \*common_progs;

1519 DBusString servicedir_path;

1520

1521 if (!\_dbus_string_init (&servicedir_path))

1522 return FALSE;

1523

1524\#ifdef DBUS_WINCE

1525 {

1526 /\* On Windows CE, we adjust datadir dynamically to installation location. \*/

1527 const char \*data_dir = \_dbus_getenv ("DBUS_DATADIR");

1528

1529 if (data_dir != NULL)

1530 {

1531 if (!\_dbus_string_append (&servicedir_path, data_dir))

1532 goto oom;

1533

1534 if (!\_dbus_string_append (&servicedir_path, \_DBUS_PATH_SEPARATOR))

1535 goto oom;

1536 }

1537 }

1538\#else

1539 {

1540 DBusString p;

1541

1542 if (!\_dbus_string_init (&p))

1543 goto oom;

1544

1545 /\* DBUS_DATADIR is assumed to be absolute; the build systems should

1546 \* ensure that. \*/

1547 if (!\_dbus_string_append (&p, DBUS_DATADIR) \|\|

1548 !\_dbus_replace_install_prefix (&p))

1549 {

1550 \_dbus_string_free (&p);

1551 goto oom;

1552 }

1553

1554 if (!\_dbus_string_append (&servicedir_path,

1555 \_dbus_string_get_const_data (&p)))

1556 {

1557 \_dbus_string_free (&p);

1558 goto oom;

1559 }

1560

1561 \_dbus_string_free (&p);

1562 }

1563

1564 if (!\_dbus_string_append (&servicedir_path, \_DBUS_PATH_SEPARATOR))

1565 goto oom;

1566\#endif

1567

1568 common_progs = \_dbus_getenv ("CommonProgramFiles");

1569

1570 if (common_progs != NULL)

1571 {

1572 if (!\_dbus_string_append (&servicedir_path, common_progs))

1573 goto oom;

1574

1575 if (!\_dbus_string_append (&servicedir_path, \_DBUS_PATH_SEPARATOR))

1576 goto oom;

1577 }

1578

1579 if (!\_dbus_split_paths_and_append (&servicedir_path,

1580 DBUS_STANDARD_SESSION_SERVICEDIR,

1581 dirs))

1582 goto oom;

1583

1584 \_dbus_string_free (&servicedir_path);

1585 return TRUE;

1586

1587 oom:

1588 \_dbus_string_free (&servicedir_path);

1589 return FALSE;

1590}

1591

1610dbus_bool_t

1611\_dbus_get_standard_system_servicedirs (DBusList \*\*dirs)

1612{

1613 \*dirs = NULL;

1614 return TRUE;

1615}

1616

1617

1630dbus_bool_t

1631\_dbus_get_local_system_servicedirs (DBusList \*\*dirs)

1632{

1633 \*dirs = NULL;

1634 return TRUE;

1635}

1636

1637static dbus_bool_t

1638\_dbus_get_config_file_name (DBusString \*str,

1639 const char \*basename)

1640{

1641 DBusString tmp;

1642

1643 if (!\_dbus_string_append (str, DBUS_DATADIR) \|\|

1644 !\_dbus_replace_install_prefix (str))

1645 return FALSE;

1646

1647 \_dbus_string_init_const (&tmp, "dbus-1");

1648

1649 if (!\_dbus_concat_dir_and_file (str, &tmp))

1650 return FALSE;

1651

1652 \_dbus_string_init_const (&tmp, basename);

1653

1654 if (!\_dbus_concat_dir_and_file (str, &tmp))

1655 return FALSE;

1656

1657 return TRUE;

1658}

1659

1668dbus_bool_t

1669\_dbus_get_system_config_file (DBusString \*str)

1670{

1671 \_dbus_assert (\_dbus_string_get_length (str) == 0);

1672

1673 return \_dbus_get_config_file_name(str, "system.conf");

1674}

1675

1682dbus_bool_t

1683\_dbus_get_session_config_file (DBusString \*str)

1684{

1685 \_dbus_assert (\_dbus_string_get_length (str) == 0);

1686

1687 return \_dbus_get_config_file_name(str, "session.conf");

1688}

1689

1690void

1691\_dbus_daemon_report_ready (void)

1692{

1693}

1694

1695void

1696\_dbus_daemon_report_reloading (void)

1697{

1698}

1699

1700void

1701\_dbus_daemon_report_reloaded (void)

1702{

1703}

1704

1705void

1706\_dbus_daemon_report_stopping (void)

1707{

1708}

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

\_dbus_error_from_system_errno

const char \* \_dbus_error_from_system_errno(void)

Converts the current system errno value into a DBusError name.

**Definition** dbus-sysdeps.c:657

\_dbus_strerror_from_errno

const char \* \_dbus_strerror_from_errno(void)

Get error message from errno.

**Definition** dbus-sysdeps.c:724

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

\_dbus_parse_unix_user_from_config

dbus_bool_t \_dbus_parse_unix_user_from_config(const DBusString \*username, dbus_uid_t \*uid_p)

Parse a UNIX user from the bus config file.

**Definition** dbus-sysdeps-util-win.c:702

\_dbus_string_ends_with_c_str

dbus_bool_t \_dbus_string_ends_with_c_str(const DBusString \*a, const char \*c_str)

Returns whether a string ends with the given suffix.

**Definition** dbus-string-util.c:54

\_dbus_string_starts_with_c_str

dbus_bool_t \_dbus_string_starts_with_c_str(const DBusString \*a, const char \*c_str)

Checks whether a string starts with the given C string.

**Definition** dbus-string.c:2250

\_dbus_string_init_from_string

dbus_bool_t \_dbus_string_init_from_string(DBusString \*str, const DBusString \*from)

Initializes a string from another string.

**Definition** dbus-string.c:254

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_unix_user_is_process_owner

dbus_bool_t \_dbus_unix_user_is_process_owner(dbus_uid_t uid)

Checks to see if the UNIX user ID matches the UID of the process.

**Definition** dbus-sysdeps-util-win.c:639

\_dbus_string_find_byte_backward

dbus_bool_t \_dbus_string_find_byte_backward(const DBusString \*str, int start, unsigned char byte, int \*found)

Find the given byte scanning backward from the given start.

**Definition** dbus-string-util.c:98

\_dbus_windows_user_is_process_owner

dbus_bool_t \_dbus_windows_user_is_process_owner(const char \*windows_sid)

Checks to see if the Windows user SID matches the owner of the process.

**Definition** dbus-sysdeps-util-win.c:644

\_dbus_parse_unix_group_from_config

dbus_bool_t \_dbus_parse_unix_group_from_config(const DBusString \*groupname, dbus_gid_t \*gid_p)

Parse a UNIX group from the bus config file.

**Definition** dbus-sysdeps-util-win.c:687

\_dbus_unix_groups_from_uid

dbus_bool_t \_dbus_unix_groups_from_uid(dbus_uid_t uid, dbus_gid_t \*\*group_ids, int \*n_group_ids, DBusError \*error)

Gets all groups corresponding to the given UNIX user ID.

**Definition** dbus-sysdeps-util-win.c:721

\_dbus_string_get_length

int \_dbus_string_get_length(const DBusString \*str)

Gets the length of a string (not including nul termination).

**Definition** dbus-string.c:784

\_dbus_string_append_printf

dbus_bool_t \_dbus_string_append_printf(DBusString \*str, const char \*format,...)

Appends a printf-style formatted string to the DBusString.

**Definition** dbus-string.c:1147

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

\_dbus_unix_user_is_at_console

dbus_bool_t \_dbus_unix_user_is_at_console(dbus_uid_t uid, DBusError \*error)

Checks to see if the UNIX user ID is at the console.

**Definition** dbus-sysdeps-util-win.c:670

\_dbus_string_copy_len

dbus_bool_t \_dbus_string_copy_len(const DBusString \*source, int start, int len, DBusString \*dest, int insert_at)

Like \_dbus_string_copy(), but can copy a segment from the middle of the source string.

**Definition** dbus-string.c:1437

\_dbus_string_get_dirname

dbus_bool_t \_dbus_string_get_dirname(const DBusString \*filename, DBusString \*dirname)

Get the directory name from a complete filename.

**Definition** dbus-sysdeps-util-unix.c:1018

\_dbus_string_replace_len

dbus_bool_t \_dbus_string_replace_len(const DBusString \*source, int start, int len, DBusString \*dest, int replace_at, int replace_len)

Replaces a segment of dest string with a segment of source string.

**Definition** dbus-string.c:1466

\_dbus_stat

dbus_bool_t \_dbus_stat(const DBusString \*filename, DBusStat \*statbuf, DBusError \*error)

stat() wrapper.

**Definition** dbus-sysdeps-util-win.c:308

\_dbus_get_standard_session_servicedirs

dbus_bool_t \_dbus_get_standard_session_servicedirs(DBusList \*\*dirs)

Returns the standard directories for a session bus to look for service activation files.

**Definition** dbus-sysdeps-util-win.c:1516

\_dbus_daemon_report_ready

void \_dbus_daemon_report_ready(void)

Report to a service manager that the daemon calling this function is ready for use.

**Definition** dbus-sysdeps-util-win.c:1691

\_dbus_write_pid_to_file_and_pipe

dbus_bool_t \_dbus_write_pid_to_file_and_pipe(const DBusString \*pidfile, DBusPipe \*print_pid_pipe, dbus_pid_t pid_to_write, DBusError \*error)

Writes the given pid_to_write to a pidfile (if non-NULL) and/or to a pipe (if non-NULL).

**Definition** dbus-sysdeps-util-win.c:171

\_dbus_directory_close

void \_dbus_directory_close(DBusDirIter \*iter)

Closes a directory iteration.

**Definition** dbus-sysdeps-util-win.c:549

dbus_uid_t

unsigned long dbus_uid_t

A user ID.

**Definition** dbus-sysdeps.h:141

\_dbus_get_session_config_file

dbus_bool_t \_dbus_get_session_config_file(DBusString \*str)

Get the absolute path of the session.conf file.

**Definition** dbus-sysdeps-util-win.c:1683

dbus_pid_t

unsigned long dbus_pid_t

A process ID.

**Definition** dbus-sysdeps.h:139

\_dbus_daemon_report_reloading

void \_dbus_daemon_report_reloading(void)

Report to a service manager that the daemon calling this function is reloading configuration.

**Definition** dbus-sysdeps-util-win.c:1696

dbus_gid_t

unsigned long dbus_gid_t

A group ID.

**Definition** dbus-sysdeps.h:143

\_dbus_command_for_pid

dbus_bool_t \_dbus_command_for_pid(unsigned long pid, DBusString \*str, int max_len, DBusError \*error)

Get a printable string describing the command used to execute the process with pid.

**Definition** dbus-sysdeps-util-win.c:1408

\_dbus_get_system_config_file

dbus_bool_t \_dbus_get_system_config_file(DBusString \*str)

Get the absolute path of the system.conf file (there is no system bus on Windows so this can just ret...

**Definition** dbus-sysdeps-util-win.c:1669

\_dbus_directory_open

DBusDirIter \* \_dbus_directory_open(const DBusString \*filename, DBusError \*error)

Open a directory to iterate over.

**Definition** dbus-sysdeps-util-win.c:411

\_dbus_set_up_transient_session_servicedirs

dbus_bool_t \_dbus_set_up_transient_session_servicedirs(DBusList \*\*dirs, DBusError \*error)

Returns the standard directories for a session bus to look for transient service activation files.

**Definition** dbus-sysdeps-util-win.c:1492

DBUS_UID_UNSET

\#define DBUS_UID_UNSET

an invalid UID used to represent an uninitialized dbus_uid_t field

**Definition** dbus-sysdeps.h:148

\_dbus_verify_daemon_user

dbus_bool_t \_dbus_verify_daemon_user(const char \*user)

Verify that after the fork we can successfully change to this user.

**Definition** dbus-sysdeps-util-win.c:243

\_dbus_getenv

const char \* \_dbus_getenv(const char \*varname)

Wrapper for getenv().

**Definition** dbus-sysdeps.c:197

\_dbus_get_standard_system_servicedirs

dbus_bool_t \_dbus_get_standard_system_servicedirs(DBusList \*\*dirs)

Returns the standard directories for a system bus to look for service activation files.

**Definition** dbus-sysdeps-util-win.c:1611

\_dbus_get_local_system_servicedirs

dbus_bool_t \_dbus_get_local_system_servicedirs(DBusList \*\*dirs)

Returns the local admin directories for a system bus to look for service activation files.

**Definition** dbus-sysdeps-util-win.c:1631

\_dbus_daemon_report_reloaded

void \_dbus_daemon_report_reloaded(void)

Report to a service manager that the daemon calling this function is reloading configuration.

**Definition** dbus-sysdeps-util-win.c:1701

DBUS_GID_UNSET

\#define DBUS_GID_UNSET

an invalid GID used to represent an uninitialized dbus_gid_t field

**Definition** dbus-sysdeps.h:150

\_dbus_change_to_daemon_user

dbus_bool_t \_dbus_change_to_daemon_user(const char \*user, DBusError \*error)

Changes the user and group the bus is running as.

**Definition** dbus-sysdeps-util-win.c:256

\_dbus_daemon_report_stopping

void \_dbus_daemon_report_stopping(void)

Report to a service manager that the daemon calling this function is shutting down.

**Definition** dbus-sysdeps-util-win.c:1706

\_dbus_directory_get_next_file

dbus_bool_t \_dbus_directory_get_next_file(DBusDirIter \*iter, DBusString \*filename, DBusError \*error)

Get next file in the directory.

**Definition** dbus-sysdeps-util-win.c:490

\_dbus_concat_dir_and_file

dbus_bool_t \_dbus_concat_dir_and_file(DBusString \*dir, const DBusString \*next_component)

Appends the given filename to the given directory.

**Definition** dbus-sysdeps-unix.c:3497

\_dbus_become_daemon

dbus_bool_t \_dbus_become_daemon(const DBusString \*pidfile, DBusPipe \*print_pid_pipe, DBusError \*error, dbus_bool_t keep_umask)

Does the chdir, fork, setsid, etc.

**Definition** dbus-sysdeps-util-win.c:65

\_dbus_split_paths_and_append

dbus_bool_t \_dbus_split_paths_and_append(DBusString \*dirs, const char \*suffix, DBusList \*\*dir_list)

Split paths into a list of char strings.

**Definition** dbus-sysdeps.c:238

\_dbus_replace_install_prefix

dbus_bool_t \_dbus_replace_install_prefix(DBusString \*path)

Replace the DBUS_PREFIX in the given path, in-place, by the current D-Bus installation directory.

**Definition** dbus-sysdeps-util-win.c:1427

DBUS_PID_FORMAT

\#define DBUS_PID_FORMAT

an appropriate printf format for dbus_pid_t

**Definition** dbus-sysdeps.h:153

DBUS_INT64_CONSTANT

\#define DBUS_INT64_CONSTANT(val)

Declare a 64-bit signed integer constant.

**Definition** dbus-arch-deps.h:41

DBusDirIter

Internals of directory iterator.

**Definition** dbus-sysdeps-util-unix.c:628

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusList

A node in a linked list.

**Definition** dbus-list.h:37

DBusPipe

**Definition** dbus-pipe.h:41

DBusStat

Portable struct with stat() results.

**Definition** dbus-sysdeps.h:570

DBusStat::nlink

unsigned long nlink

Number of hard links.

**Definition** dbus-sysdeps.h:572

DBusStat::size

unsigned long size

Size of file.

**Definition** dbus-sysdeps.h:575

DBusStat::uid

dbus_uid_t uid

User owning file.

**Definition** dbus-sysdeps.h:573

DBusStat::mode

unsigned long mode

File mode.

**Definition** dbus-sysdeps.h:571

DBusStat::gid

dbus_gid_t gid

Group owning file.

**Definition** dbus-sysdeps.h:574

DBusStat::atime

unsigned long atime

Access time.

**Definition** dbus-sysdeps.h:576

DBusStat::ctime

unsigned long ctime

Creation time.

**Definition** dbus-sysdeps.h:578

DBusStat::mtime

unsigned long mtime

Modify time.

**Definition** dbus-sysdeps.h:577

DBusString

**Definition** dbus-string.h:47
