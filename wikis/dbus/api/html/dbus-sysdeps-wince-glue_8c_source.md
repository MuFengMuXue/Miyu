dbus-sysdeps-wince-glue.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-sysdeps-wince-glue.c Wrappers for Windows CE around system/libc features (internal to D-BUS implementation)

3 \*

4 \* Copyright (C) 2002, 2003 Red Hat, Inc.

5 \* Copyright (C) 2003 CodeFactory AB

6 \* Copyright (C) 2005 Novell, Inc.

7 \* Copyright (C) 2006 Ralf Habacker \<ralf.habacker@freenet.de\>

8 \* Copyright (C) 2006 Peter Kümmel \<syntheticpp@gmx.net\>

9 \* Copyright (C) 2006 Christian Ehrlicher \<ch.ehrlicher@gmx.de\>

10 \*

11 \* SPDX-License-Identifier: AFL-2.1 OR GPL-2.0-or-later

12 \*

13 \* Licensed under the Academic Free License version 2.1

14 \*

15 \* This program is free software; you can redistribute it and/or modify

16 \* it under the terms of the GNU General Public License as published by

17 \* the Free Software Foundation; either version 2 of the License, or

18 \* (at your option) any later version.

19 \*

20 \* This program is distributed in the hope that it will be useful,

21 \* but WITHOUT ANY WARRANTY; without even the implied warranty of

22 \* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the

23 \* GNU General Public License for more details.

24 \*

25 \* You should have received a copy of the GNU General Public License

26 \* along with this program; if not, write to the Free Software

27 \* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

28 \*

29 \*/

30

31\#include \<config.h\>

32\#include "dbus-internals.h"

33\#include "dbus-sysdeps.h"

34\#include "dbus-sysdeps-win.h"

35

36\#include \<windows.h\>

37/\* Including shlobj.h creates trouble on some compilers. Just chicken

38 out here by defining just what we need. \*/

39\#ifndef CSIDL_PERSONAL

40\#define CSIDL_PERSONAL 5

41\#endif

42

43

44/\* Copy SRC to DEST, returning the address of the terminating '\0' in DEST. \*/

45static char \*

46stpcpy (char \*dest, const char \*src)

47{

48 char \*d = dest;

49 const char \*s = src;

50

51 do

52 \*d++ = \*s;

53 while (\*s++ != '\0');

54

55 return d - 1;

56}

57

58

59/\* This is special cased, because we must avoid using many dbus

60 functions (such as memory allocations): Those functions may in turn

61 cause verbose output and check the flag! \*/

62static char \*

63get_verbose_setting()

64{

65 const wchar_t dir\[\] = L"Software\\freedesktop\\DBus";

66 const wchar_t name\[\] = L"Verbose";

67 HKEY root_key;

68 HKEY key_handle;

69 DWORD nbytes;

70 DWORD n1;

71 DWORD type;

72 wchar_t \*result_w = NULL;

73 char \*result;

74 int len;

75

76 root_key = HKEY_LOCAL_MACHINE;

77 if (RegOpenKeyExW (root_key, dir, 0, KEY_READ, &key_handle))

78 return NULL;

79

80 nbytes = 1;

81 if (RegQueryValueExW (key_handle, name, 0, NULL, NULL, &nbytes))

82 {

83 RegCloseKey (key_handle);

84 return NULL;

85 }

86 /\* Round up to multiple of wchar_t, convert to number of wchar_t's, and add 1. \*/

87 n1 = ((nbytes + sizeof(wchar_t) - 1) / sizeof (wchar_t)) + 1;

88 result_w = malloc (n1 \* sizeof (wchar_t));

89 if (!result_w)

90 {

91 RegCloseKey (key_handle);

92 return NULL;

93 }

94 if (RegQueryValueExW (key_handle, name, 0, &type, (LPBYTE) result_w, &nbytes))

95 {

96 RegCloseKey (key_handle);

97 free (result_w);

98 return NULL;

99 }

100 RegCloseKey (key_handle);

101 result_w\[n1 - 1\] = 0; /\* Make sure it is really a string. \*/

102

103 /\* NOTE: REG_MULTI_SZ and REG_EXPAND_SZ not supported, because they

104 are not needed in this module. \*/

105 if (type != REG_SZ)

106 {

107 free (result_w);

108 return NULL;

109 }

110

111 len = WideCharToMultiByte (CP_UTF8, 0, result_w, -1, NULL, 0, NULL, NULL);

112 if (len \< 0)

113 {

114 free (result_w);

115 return NULL;

116 }

117

118 result = malloc (len + 1);

119 if (!result)

120 {

121 free (result_w);

122 return NULL;

123 }

124

125 len = WideCharToMultiByte (CP_UTF8, 0, result_w, -1, result, len, NULL, NULL);

126 free (result_w);

127 if (len \< 0)

128 {

129 free (result);

130 return NULL;

131 }

132 return result;

133}

134

135

136/\* Return a string from the W32 Registry or NULL in case of error.

137 Caller must release the return value. A NULL for root is an alias

138 for HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE in turn. \*/

139static char \*

140read_w32_registry_string (const char \*root, const char \*dir, const char \*name)

141{

142 HKEY root_key, key_handle;

143 DWORD n1, nbytes, type;

144 char \*result = NULL;

145

146 if ( !root )

147 root_key = HKEY_CURRENT_USER;

148 else if ( !strcmp( root, "HKEY_CLASSES_ROOT" ) )

149 root_key = HKEY_CLASSES_ROOT;

150 else if ( !strcmp( root, "HKEY_CURRENT_USER" ) )

151 root_key = HKEY_CURRENT_USER;

152 else if ( !strcmp( root, "HKEY_LOCAL_MACHINE" ) )

153 root_key = HKEY_LOCAL_MACHINE;

154 else if ( !strcmp( root, "HKEY_USERS" ) )

155 root_key = HKEY_USERS;

156 else

157 return NULL;

158

159 if (RegOpenKeyExA (root_key, dir, 0, KEY_READ, &key_handle))

160 {

161 if (root)

162 return NULL; /\* no need for a RegClose, so return direct \*/

163 /\* It seems to be common practise to fall back to HKLM. \*/

164 if (RegOpenKeyExA (HKEY_LOCAL_MACHINE, dir, 0, KEY_READ, &key_handle))

165 return NULL; /\* still no need for a RegClose, so return direct \*/

166 }

167

168 nbytes = 1;

169 if (RegQueryValueExA (key_handle, name, 0, NULL, NULL, &nbytes))

170 {

171 if (root)

172 goto out;

173 /\* Try to fallback to HKLM also for a missing value. \*/

174 RegCloseKey (key_handle);

175 if (RegOpenKeyExA (HKEY_LOCAL_MACHINE, dir, 0, KEY_READ, &key_handle))

176 return NULL; /\* Nope. \*/

177 if (RegQueryValueExA (key_handle, name, 0, NULL, NULL, &nbytes))

178 goto out;

179 }

180 n1 = nbytes + 1;

181 result = malloc (n1);

182 if (!result)

183 goto out;

184 if (RegQueryValueExA (key_handle, name, 0, &type, result, &n1))

185 {

186 free(result);

187 result = NULL;

188 goto out;

189 }

190 result\[nbytes\] = 0; /\* Make sure it is really a string. \*/

191

192 out:

193 RegCloseKey (key_handle);

194 return result;

195}

196

197

198static char \*

199find_inst_dir ()

200{

201 return read_w32_registry_string ("HKEY_LOCAL_MACHINE",

202 "Software\\freedesktop\\DBus",

203 "Install Directory");

204}

205

206

207static char \*

208find_env_in_registry (const char \*name)

209{

210 return read_w32_registry_string ("HKEY_LOCAL_MACHINE",

211 "Software\\freedesktop\\DBus",

212 name);

213}

214

215

216static char \*

217find_program_in_inst_dir (const char \*name)

218{

219 char \*result = NULL;

220 char \*tmp;

221

222 tmp = find_inst_dir ();

223 if (!tmp)

224 return NULL;

225

226 result = malloc (strlen (tmp) + 5 + strlen (name) + 1);

227 if (!result)

228 {

229 free (tmp);

230 return NULL;

231 }

232

233 strcpy (stpcpy (stpcpy (result, tmp), "\\bin\\"), name);

234 free (tmp);

235

236 return result;

237}

238

239

240static char \*

241find_inst_subdir (const char \*name)

242{

243 char \*result = NULL;

244 char \*tmp;

245

246 tmp = find_inst_dir ();

247 if (!tmp)

248 return NULL;

249

250 result = malloc (strlen (tmp) + 1 + strlen (name) + 1);

251 if (!result)

252 {

253 free (tmp);

254 return NULL;

255 }

256

257 strcpy (stpcpy (stpcpy (result, tmp), "\\"), name);

258 free (tmp);

259

260 return result;

261}

262

263

264static char \*

265find_my_documents_folder ()

266{

267 /\* One for safety, just in case. \*/

268 char dir\[MAX_PATH + 1\];

269 char \*result;

270

271 dir\[0\] = '\0';

272 /\* May return false even if successful. \*/

273 SHGetSpecialFolderPathA (0, dir, CSIDL_PERSONAL, 0);

274 if (dir\[0\] == '\0')

275 return NULL;

276

277 result = malloc (strlen (dir) + 1);

278 if (!result)

279 return NULL;

280 strcpy (result, dir);

281 return result;

282}

283

284

285\#define MAX_ENV 30

286

287char \*environ\[MAX_ENV + 1\];

288

289char \*

290getenv (const char \*name)

291{

292 static char \*past_result;

293 char \*\*envp;

294 int idx;

295

296 if (past_result)

297 {

298 free (past_result);

299 past_result = NULL;

300 }

301

302 if (! strcmp (name, "DBUS_VERBOSE"))

303 return past_result = get_verbose_setting ();

304 else if (! strcmp (name, "HOMEPATH"))

305 return past_result = find_my_documents_folder ();

306 else if (! strcmp (name, "DBUS_DATADIR"))

307 return past_result = find_inst_subdir ("share");

308

309 for (envp = environ; \*envp != 0; envp++)

310 {

311 const char \*varp = name;

312 char \*ep = \*envp;

313 int same_name = 0;

314

315 while (\*varp == \*ep && \*varp != '\0')

316 {

317 ++ep;

318 ++varp;

319 };

320

321 if (\*varp == '\0' && \*ep == '=')

322 return ep + 1;

323 }

324

325 return NULL;

326}

327

328

329int

330putenv (char \*str)

331{

332 char \*\*envp;

333 int idx;

334 for (envp = environ; \*envp != 0; envp++)

335 {

336 char \*varp = str;

337 char \*ep = \*envp;

338 int same_name = 0;

339

340 while (\*varp == \*ep && \*varp != '\0')

341 {

342 if (\*varp == '=')

343 same_name = 1;

344 ++ep;

345 ++varp;

346 };

347

348 if (\*varp == \*ep && \*varp == '\0')

349 return 0;

350 if (same_name)

351 {

352 \*envp = str;

353 return 0;

354 }

355 }

356

357 idx = envp - environ;

358 if (idx \> MAX_ENV)

359 {

360 \_dbus_win_set_errno (ENOMEM);

361 return -1;

362 }

363

364 environ\[idx\] = str;

365 return 0;

366}

367

368

369clock_t

370clock (void)

371{

372 return GetTickCount ();

373}

374

375

376void

377abort (void)

378{

379 /\* This is what windows does. \*/

380 exit (3);

381}

382

383

384void

385GetSystemTimeAsFileTime (LPFILETIME ftp)

386{

387 SYSTEMTIME st;

388 GetSystemTime (&st);

389 SystemTimeToFileTime (&st, ftp);

390}

391

392

393unsigned char\*

394\_mbsrchr (const unsigned char\* str, unsigned int ch)

395{

396 /\* FIXME. This is not multi-byte safe. \*/

397 return strrchr (str, ch);

398}

399

400

401HANDLE OpenFileMappingA(DWORD dwDesiredAccess,

402 BOOL bInheritHandle,

403 LPCSTR lpName)

404{

405 DWORD flProtect = 0;

406 HANDLE hMapping;

407

408 if (dwDesiredAccess & FILE_MAP_READ)

409 flProtect \|= PAGE_READONLY;

410

411 if (dwDesiredAccess & FILE_MAP_WRITE)

412 flProtect \|= PAGE_READWRITE;

413

414 SetLastError (0);

415 hMapping = CreateFileMappingA(INVALID_HANDLE_VALUE,

416 NULL, flProtect, 0, 0, lpName);

417 if (hMapping != INVALID_HANDLE_VALUE)

418 {

419 /\* Just in case Windows CE changes its behaviour, we check for

420 the right error value here. \*/

421 if (GetLastError () != ERROR_ALREADY_EXISTS)

422 {

423 CloseHandle(hMapping);

424 hMapping = INVALID_HANDLE_VALUE;

425 }

426 }

427 return hMapping;

428}

429

430

431BOOL

432MoveFileExA (LPCSTR lpExistingFileName, LPCSTR lpNewFileName, DWORD dwFlags)

433{

434 \_dbus_assert (dwFlags == MOVEFILE_REPLACE_EXISTING);

435

436 if (\_dbus_file_exists (lpNewFileName))

437 {

438 BOOL result = DeleteFileA (lpNewFileName);

439 if (result == 0)

440 return FALSE;

441 }

442 return MoveFileA (lpExistingFileName, lpNewFileName);

443}

444

445

446BOOL

447SetHandleInformation (HANDLE hObject, DWORD dwMask, DWORD dwFlags)

448{

449 \_dbus_assert (dwMask == (HANDLE_FLAG_INHERIT \| HANDLE_FLAG_PROTECT_FROM_CLOSE));

450 \_dbus_assert (dwFlags == 0);

451

452 /\* Not supported on Windows CE, and actually the default. So just

453 return overwhelming success. \*/

454 return 1;

455}

456

457

458DWORD

459SearchPathA (LPCSTR lpPath, LPCSTR lpFileName, LPCSTR lpExtension,

460 DWORD nBufferLength, LPSTR lpBuffer, LPSTR\* lpFilePart)

461{

462 char \*filename;

463 char \*filepart;

464 int filename_len;

465

466 \_dbus_assert (lpPath == NULL);

467 \_dbus_assert (lpExtension == NULL);

468

469 filename = find_program_in_inst_dir (lpFileName);

470 if (!filename)

471 {

472 SetLastError (ERROR_FILE_NOT_FOUND);

473 return 0;

474 }

475

476 filename_len = strlen (filename) + 1;

477 if (filename_len \> nBufferLength)

478 {

479 free (filename);

480 return filename_len;

481 }

482

483 strcpy (lpBuffer, filename);

484 free (filename);

485

486 filepart = \_mbsrchr (lpBuffer, '\\');

487 if (!filepart)

488 filepart = lpBuffer;

489 \*lpFilePart = filepart;

490

491 return filename_len - 1;

492}

493

494

499dbus_bool_t

500\_dbus_getsid(char \*\*sid)

501{

502 /\* There is nothing like this on Windows CE, so we fake it. \*/

503 static const char asid\[\] = "S-1-5-21-515967899-920026266-1708537768-1000";

504 char \*buf = LocalAlloc (LMEM_FIXED, sizeof (asid));

505 if (!buf)

506 {

507 \_dbus_win_warn_win_error ("LocalAlloc failed", GetLastError ());

508 return FALSE;

509 }

510

511 memcpy (buf, asid, sizeof (asid));

512 \*sid = buf;

513 return TRUE;

514}

515

516

517BOOL

518LookupAccountNameW (LPCWSTR lpSystemName, LPCWSTR lpAccountName, PSID Sid, PDWORD cbSid,

519 LPWSTR ReferencedDomainName, PDWORD cchReferencedDomainName, PSID_NAME_USE peUse)

520{

521 /\* Currently not needed. \*/

522 return FALSE;

523}

524

525

526BOOL

527IsValidSid (PSID psid)

528{

529 /\* Currently not needed. \*/

530 return FALSE;

531}

532

533

534HANDLE

535CreateFileA (LPCSTR lpFileName, DWORD dwDesiredAccess, DWORD dwSharedMode,

536 LPSECURITY_ATTRIBUTES lpSecurityAttributes,

537 DWORD dwCreationDisposition, DWORD dwFlagsAndAttributes,

538 HANDLE hTemplateFile)

539{

540 wchar_t \*filename;

541 HANDLE result;

542 int err;

543

544 filename = \_dbus_win_utf8_to_utf16 (lpFileName, NULL);

545 if (!filename)

546 return INVALID_HANDLE_VALUE;

547

548 result = CreateFileW (filename, dwDesiredAccess, dwSharedMode,

549 lpSecurityAttributes, dwCreationDisposition,

550 dwFlagsAndAttributes, hTemplateFile);

551

552 err = GetLastError ();

553 dbus_free (filename);

554 SetLastError (err);

555 return result;

556}

557

558

559BOOL

560DeleteFileA (LPCSTR lpFileName)

561{

562 wchar_t \*filename;

563 BOOL result;

564 int err;

565

566 filename = \_dbus_win_utf8_to_utf16 (lpFileName, NULL);

567 if (!filename)

568 return FALSE;

569

570 result = DeleteFileW (filename);

571

572 err = GetLastError ();

573 dbus_free (filename);

574 SetLastError (err);

575 return result;

576}

577

578

579BOOL

580MoveFileA (LPCSTR lpExistingFileName, LPCSTR lpNewFileName)

581{

582 wchar_t \*existing_filename;

583 wchar_t \*new_filename;

584 BOOL result;

585 int err;

586

587 existing_filename = \_dbus_win_utf8_to_utf16 (lpExistingFileName, NULL);

588 if (! existing_filename)

589 return FALSE;

590

591 new_filename = \_dbus_win_utf8_to_utf16 (lpNewFileName, NULL);

592 if (! new_filename)

593 {

594 dbus_free (existing_filename);

595 return FALSE;

596 }

597

598 result = MoveFileW (existing_filename, new_filename);

599

600 err = GetLastError ();

601 dbus_free (existing_filename);

602 dbus_free (new_filename);

603 SetLastError (err);

604 return result;

605}

606

607

608DWORD

609GetFileAttributesA(LPCSTR lpFileName)

610{

611 wchar_t \*filename;

612 DWORD result;

613 int err;

614

615 filename = \_dbus_win_utf8_to_utf16 (lpFileName, NULL);

616 if (!filename)

617 return INVALID_FILE_ATTRIBUTES;

618

619 result = GetFileAttributesW (filename);

620

621 err = GetLastError ();

622 dbus_free (filename);

623 SetLastError (err);

624 return result;

625}

626

627

628BOOL

629GetFileAttributesExA (LPCSTR lpFileName, GET_FILEEX_INFO_LEVELS fInfoLevelId,

630 PVOID lpFileInformation)

631{

632 wchar_t \*filename;

633 DWORD result;

634 int err;

635

636 filename = \_dbus_win_utf8_to_utf16 (lpFileName, NULL);

637 if (!filename)

638 return INVALID_FILE_ATTRIBUTES;

639

640 result = GetFileAttributesExW (filename, fInfoLevelId, lpFileInformation);

641

642 err = GetLastError ();

643 dbus_free (filename);

644 SetLastError (err);

645 return result;

646}

647

648

649HANDLE

650CreateFileMappingA (HANDLE hFile, LPSECURITY_ATTRIBUTES lpAttributes,

651 DWORD flProtect, DWORD dwMaximumSizeHigh,

652 DWORD dwMaximumSizeLow, LPCSTR lpName)

653{

654 wchar_t \*name;

655 HANDLE result;

656 int err;

657

658 if (lpName)

659 {

660 name = \_dbus_win_utf8_to_utf16 (lpName, NULL);

661 if (!name)

662 return INVALID_HANDLE_VALUE;

663 }

664 else

665 name = NULL;

666

667 result = CreateFileMappingW (hFile, lpAttributes, flProtect,

668 dwMaximumSizeHigh, dwMaximumSizeLow,

669 name);

670

671 err = GetLastError ();

672 dbus_free (name);

673 SetLastError (err);

674 return result;

675}

676

677

678BOOL

679CreateDirectoryA (LPCSTR lpPathName, LPSECURITY_ATTRIBUTES lpSecurityAttributes)

680{

681 wchar_t \*pathname;

682 BOOL result;

683 int err;

684

685 pathname = \_dbus_win_utf8_to_utf16 (lpPathName, NULL);

686 if (!pathname)

687 return FALSE;

688

689 result = CreateDirectoryW (pathname, lpSecurityAttributes);

690

691 err = GetLastError ();

692 dbus_free (pathname);

693 SetLastError (err);

694 return result;

695}

696

697

698BOOL

699RemoveDirectoryA (LPCSTR lpPathName)

700{

701 wchar_t \*pathname;

702 BOOL result;

703 int err;

704

705 pathname = \_dbus_win_utf8_to_utf16 (lpPathName, NULL);

706 if (!pathname)

707 return FALSE;

708

709 result = RemoveDirectoryW (pathname);

710

711 err = GetLastError ();

712 dbus_free (pathname);

713 SetLastError (err);

714 return result;

715}

716

717

718static BOOL

719convert_find_data (LPWIN32_FIND_DATAW fdw, LPWIN32_FIND_DATAA fda)

720{

721 char \*filename;

722 int len;

723

724 fda-\>dwFileAttributes = fdw-\>dwFileAttributes;

725 fda-\>ftCreationTime = fdw-\>ftCreationTime;

726 fda-\>ftLastAccessTime = fdw-\>ftLastAccessTime;

727 fda-\>ftLastWriteTime = fdw-\>ftLastWriteTime;

728 fda-\>nFileSizeHigh = fdw-\>nFileSizeHigh;

729 fda-\>nFileSizeLow = fdw-\>nFileSizeLow;

730

731 filename = \_dbus_win_utf16_to_utf8 (fdw-\>cFileName, NULL);

732 if (!filename)

733 return FALSE;

734

735 len = sizeof (fda-\>cFileName);

736 strncpy (fda-\>cFileName, filename, len);

737 fda-\>cFileName\[len - 1\] = '\0';

738

739 return TRUE;

740}

741

742

743HANDLE

744FindFirstFileA (LPCSTR lpFileName, LPWIN32_FIND_DATAA lpFindFileData)

745{

746 wchar_t \*pathname;

747 WIN32_FIND_DATAW find_file_data;

748 HANDLE result;

749 int err;

750

751 pathname = \_dbus_win_utf8_to_utf16 (lpFileName, NULL);

752 if (!pathname)

753 return INVALID_HANDLE_VALUE;

754

755 result = FindFirstFileW (pathname, &find_file_data);

756 if (result != INVALID_HANDLE_VALUE)

757 {

758 BOOL res = convert_find_data (&find_file_data, lpFindFileData);

759 if (! res)

760 {

761 err = GetLastError ();

762 FindClose (result);

763 SetLastError (err);

764 result = INVALID_HANDLE_VALUE;

765 }

766 }

767

768 err = GetLastError ();

769 dbus_free (pathname);

770 SetLastError (err);

771 return result;

772}

773

774

775BOOL

776FindNextFileA (HANDLE hFindFile, LPWIN32_FIND_DATAA lpFindFileData)

777{

778 WIN32_FIND_DATAW find_file_data;

779 BOOL result;

780 int err;

781

782 result = FindNextFileW (hFindFile, &find_file_data);

783 if (result)

784 result = convert_find_data (&find_file_data, lpFindFileData);

785

786 return result;

787}

788

789

790HANDLE

791CreateMutexA (LPSECURITY_ATTRIBUTES lpMutexAttributes, BOOL bInitialOwner,

792 LPCSTR lpName)

793{

794 wchar_t \*name;

795 HANDLE result;

796 int err;

797

798 if (lpName)

799 {

800 name = \_dbus_win_utf8_to_utf16 (lpName, NULL);

801 if (!name)

802 return INVALID_HANDLE_VALUE;

803 }

804 else

805 name = NULL;

806

807 result = CreateMutexW (lpMutexAttributes, bInitialOwner, name);

808

809 err = GetLastError ();

810 dbus_free (name);

811 SetLastError (err);

812 return result;

813}

814

815

816BOOL

817CreateProcessA (LPCSTR pszImageName, LPSTR pszCmdLine,

818 LPSECURITY_ATTRIBUTES psaProcess,

819 LPSECURITY_ATTRIBUTES psaThread, BOOL fInheritHandles,

820 DWORD fdwCreate, PVOID pvEnvironment, LPCSTR pszCurDir,

821 LPSTARTUPINFOA psiStartInfo,

822 LPPROCESS_INFORMATION pProcInfo)

823{

824 wchar_t \*image_name = NULL;

825 wchar_t \*cmd_line = NULL;

826 BOOL result;

827 int err;

828

829 \_dbus_assert (psaProcess == NULL);

830 \_dbus_assert (psaThread == NULL);

831 \_dbus_assert (fInheritHandles == FALSE);

832 \_dbus_assert (pvEnvironment == NULL);

833 \_dbus_assert (pszCurDir == NULL);

834 /\* psiStartInfo is generally not NULL. \*/

835

836 if (pszImageName)

837 {

838 image_name = \_dbus_win_utf8_to_utf16 (pszImageName, NULL);

839 if (!image_name)

840 return 0;

841 }

842 if (pszCmdLine)

843 {

844 cmd_line = \_dbus_win_utf8_to_utf16 (pszCmdLine, NULL);

845 if (!cmd_line)

846 {

847 if (image_name)

848 dbus_free (image_name);

849 return 0;

850 }

851 }

852

853 result = CreateProcessW (image_name, cmd_line, NULL, NULL, FALSE,

854 fdwCreate, NULL, NULL, NULL, pProcInfo);

855

856 err = GetLastError ();

857 dbus_free (image_name);

858 dbus_free (cmd_line);

859 SetLastError (err);

860 return result;

861}

862

863

864LONG

865RegOpenKeyExA (HKEY hKey, LPCSTR lpSubKey, DWORD ulOptions,

866 REGSAM samDesired, PHKEY phkResult)

867{

868 wchar_t \*subkey;

869 LONG result;

870 int err;

871

872 if (lpSubKey)

873 {

874 subkey = \_dbus_win_utf8_to_utf16 (lpSubKey, NULL);

875 if (!subkey)

876 return 0;

877 }

878 else

879 subkey = NULL;

880

881 result = RegOpenKeyEx (hKey, subkey, ulOptions, samDesired, phkResult);

882

883 err = GetLastError ();

884 dbus_free (subkey);

885 SetLastError (err);

886 return result;

887}

888

889

890LONG

891RegQueryValueExA (HKEY hKey, LPCSTR lpValueName, LPDWORD lpReserved,

892 LPDWORD lpType, LPBYTE lpData, LPDWORD lpcbData)

893{

894 wchar_t \*name;

895 LONG err;

896 BYTE \*data;

897 DWORD data_len;

898 DWORD type;

899

900 if (lpValueName)

901 {

902 name = \_dbus_win_utf8_to_utf16 (lpValueName, NULL);

903 if (!name)

904 return GetLastError ();

905 }

906 else

907 name = NULL;

908

909 data_len = 0;

910 err = RegQueryValueExW (hKey, name, lpReserved, lpType, NULL, &data_len);

911 if (err \|\| !lpcbData)

912 {

913 dbus_free (name);

914 return err;

915 }

916

917 data = malloc (data_len + sizeof (wchar_t));

918 if (!data)

919 {

920 dbus_free (name);

921 return ERROR_NOT_ENOUGH_MEMORY;

922 }

923

924 err = RegQueryValueExW (hKey, name, lpReserved, &type, data, &data_len);

925 if (lpType)

926 \*lpType = type;

927 dbus_free (name);

928 /\* If err is ERROR_MORE_DATA, there probably was a race condition.

929 We can punt this to the caller just as well. \*/

930 if (err)

931 {

932 free (data);

933 return err;

934 }

935

936 /\* NOTE: REG_MULTI_SZ and REG_EXPAND_SZ not supported, because they

937 are not needed in this module. \*/

938 if (type == REG_SZ)

939 {

940 char \*data_c;

941 int data_c_len;

942

943 /\* This is valid since we allocated one more above. \*/

944 data\[data_len\] = '\0';

945 data\[data_len + 1\] = '\0';

946

947 /\* The cast is valid because malloc guarantees alignment of

948 basic types. \*/

949 data_c = \_dbus_win_utf16_to_utf8 ((wchar_t\*) data, NULL);

950 if (!data_c)

951 {

952 free (data);

953 return GetLastError();

954 }

955

956 data_c_len = strlen (data_c) + 1;

957 \_dbus_assert (data_c_len \<= data_len + sizeof (wchar_t));

958 memcpy (data, data_c, data_c_len);

959 data_len = data_c_len;

960 dbus_free (data_c);

961 }

962

963 /\* DATA and DATA_LEN now contain the result. \*/

964 if (lpData)

965 {

966 if (data_len \> \*lpcbData)

967 err = ERROR_MORE_DATA;

968 else

969 memcpy (lpData, data, data_len);

970 }

971 free (data);

972 \*lpcbData = data_len;

973 return err;

974}

975

976

977DWORD

978FormatMessageA (DWORD dwFlags, PCVOID lpSource, DWORD dwMessageId,

979 DWORD dwLanguageId, LPSTR lpBuffer, DWORD nSize,

980 va_list\* Arguments)

981{

982 LPWSTR buffer_w = NULL;

983 LPSTR buffer_c;

984 DWORD len;

985 char \*buffer_new;

986 DWORD buffer_new_len;

987 BOOL buffer_w_free;

988

989 len = FormatMessageW (dwFlags \| FORMAT_MESSAGE_ALLOCATE_BUFFER,

990 lpSource, dwMessageId, dwLanguageId,

991 (LPWSTR) &buffer_w, 0, Arguments);

992 if (len == 0)

993 return 0;

994

995 buffer_c = \_dbus_win_utf16_to_utf8 (buffer_w, NULL);

996 if (! buffer_c)

997 {

998 LocalFree (buffer_w);

999 return 0;

1000 }

1001

1002 if (dwFlags & FORMAT_MESSAGE_ALLOCATE_BUFFER)

1003 {

1004 /\* We need to return a buffer that's freeable with LocalFree. \*/

1005 buffer_new = (char \*) buffer_w;

1006 buffer_new_len = sizeof (wchar_t) \* (len + 1);

1007 buffer_w_free = FALSE;

1008 /\* Avoid alignment issue by using memcpy. \*/

1009 memcpy (lpBuffer, &buffer_new, sizeof (buffer_new));

1010 }

1011 else

1012 {

1013 buffer_new = lpBuffer;

1014 buffer_new_len = nSize;

1015 buffer_w_free = TRUE;

1016 }

1017

1018 strncpy (buffer_new, buffer_c, buffer_new_len);

1019 dbus_free (buffer_c);

1020 buffer_new\[buffer_new_len - 1\] = '\0';

1021 if (buffer_w_free)

1022 LocalFree (buffer_w);

1023

1024 /\* strlen is correct (not \_mbstrlen), because we want storage and

1025 not string length. \*/

1026 return strlen (buffer_new);

1027}

1028

1029

1030DWORD

1031GetModuleFileNameA (HINSTANCE hModule, LPSTR lpFilename, DWORD nSize)

1032{

1033 wchar_t \*filename_w;

1034 char \*filename_c;

1035 DWORD len;

1036

1037 if (nSize == 0)

1038 {

1039 /\* Windows XP/2000. \*/

1040 SetLastError (0);

1041 return 0;

1042 }

1043

1044 filename_w = malloc (sizeof (wchar_t) \* nSize);

1045 if (! filename_w)

1046 return 0;

1047

1048 len = GetModuleFileNameW (hModule, filename_w, nSize);

1049 if (len == 0)

1050 {

1051 /\* Note: If we fail with ERROR_INSUFFICIENT_BUFFER, this is still

1052 (approximately) correct. \*/

1053 free (filename_w);

1054 return 0;

1055 }

1056

1057 filename_w\[nSize - 1\] = '\0';

1058 filename_c = \_dbus_win_utf16_to_utf8 (filename_w, NULL);

1059 free (filename_w);

1060 if (! filename_c)

1061 return 0;

1062

1063 strncpy (lpFilename, filename_c, nSize);

1064 dbus_free (filename_c);

1065 lpFilename\[nSize - 1\] = '\0';

1066 /\* strlen is correct (not \_mbstrlen), because we want storage and

1067 not string length. \*/

1068 return strlen (lpFilename);

1069}

1070

1071

1072DWORD

1073GetTempPathA (DWORD nBufferLength, LPSTR lpBuffer)

1074{

1075 wchar_t dummy\[1\];

1076 DWORD len;

1077

1078 len = GetTempPathW (0, dummy);

1079 if (len == 0)

1080 return 0;

1081

1082 \_dbus_assert (len \<= MAX_PATH);

1083

1084 /\* Better be safe than sorry. MSDN doesn't say if len is with or

1085 without terminating 0. \*/

1086 len++;

1087

1088 {

1089 wchar_t \*buffer_w;

1090 DWORD len_w;

1091 char \*buffer_c;

1092 DWORD len_c;

1093

1094 buffer_w = malloc (sizeof (wchar_t) \* len);

1095 if (! buffer_w)

1096 return 0;

1097

1098 len_w = GetTempPathW (len, buffer_w);

1099 /\* Give up if we still can't get at it. \*/

1100 if (len_w == 0 \|\| len_w \>= len)

1101 {

1102 free (buffer_w);

1103 return 0;

1104 }

1105

1106 /\* Better be really safe. \*/

1107 buffer_w\[len_w\] = '\0';

1108

1109 buffer_c = \_dbus_win_utf16_to_utf8 (buffer_w, NULL);

1110 free (buffer_w);

1111 if (! buffer_c)

1112 return 0;

1113

1114 /\* strlen is correct (not \_mbstrlen), because we want storage and

1115 not string length. \*/

1116 len_c = strlen (buffer_c) + 1;

1117 if (len_c \> nBufferLength)

1118 return len_c;

1119

1120 strcpy (lpBuffer, buffer_c);

1121 dbus_free (buffer_c);

1122 return len_c - 1;

1123 }

1124}

1125

1126

1127BOOL

1128SHGetSpecialFolderPathA (HWND hwndOwner, LPSTR lpszPath, int nFolder,

1129 BOOL fCreate)

1130{

1131 wchar_t path\[MAX_PATH\];

1132 char \*path_c;

1133 BOOL result;

1134

1135 path\[0\] = (wchar_t) 0;

1136 result = SHGetSpecialFolderPathW (hwndOwner, path, nFolder, fCreate);

1137 /\* Note: May return false even if succeeds. \*/

1138

1139 path\[MAX_PATH - 1\] = (wchar_t) 0;

1140 path_c = \_dbus_win_utf16_to_utf8 (path, NULL);

1141 if (! path_c)

1142 return 0;

1143

1144 strncpy (lpszPath, path_c, MAX_PATH);

1145 dbus_free (path_c);

1146 lpszPath\[MAX_PATH - 1\] = '\0';

1147 return result;

1148}

1149

1150

1151void

1152OutputDebugStringA (LPCSTR lpOutputString)

1153{

1154 wchar_t \*str;

1155 HANDLE result;

1156 int err;

1157

1158 str = \_dbus_win_utf8_to_utf16 (lpOutputString, NULL);

1159 if (!str)

1160 return;

1161

1162 OutputDebugStringW (str);

1163

1164 err = GetLastError ();

1165 dbus_free (str);

1166 SetLastError (err);

1167}

\_dbus_file_exists

dbus_bool_t \_dbus_file_exists(const char \*file)

File interface.

**Definition** dbus-sysdeps-util-unix.c:564

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

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
