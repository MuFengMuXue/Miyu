dbus-sysdeps-win.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-sysdeps.c Wrappers around system/libc features (internal to D-BUS implementation)

3 \*

4 \* Copyright (C) 2002, 2003 Red Hat, Inc.

5 \* Copyright (C) 2003 CodeFactory AB

6 \* Copyright (C) 2005 Novell, Inc.

7 \* Copyright (C) 2006 Peter Kümmel \<syntheticpp@gmx.net\>

8 \* Copyright (C) 2006 Christian Ehrlicher \<ch.ehrlicher@gmx.de\>

9 \* Copyright (C) 2006-2021 Ralf Habacker \<ralf.habacker@freenet.de\>

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

28 \*/

29

30\#include \<config.h\>

31

32\#define STRSAFE_NO_DEPRECATE

33

34\#include "dbus-internals.h"

35\#include "dbus-sha.h"

36\#include "dbus-sysdeps.h"

37\#include "dbus-threads.h"

38\#include "dbus-protocol.h"

39\#include "dbus-string.h"

40\#include "dbus-sysdeps.h"

41\#include "dbus-sysdeps-win.h"

42\#include "dbus-protocol.h"

43\#include "dbus-hash.h"

44\#include "dbus-sockets-win.h"

45\#include "dbus-list.h"

46\#include "dbus-nonce.h"

47\#include "dbus-credentials.h"

48

49\#include \<windows.h\>

50\#include \<wincrypt.h\>

51\#include \<iphlpapi.h\>

52\#ifdef HAVE_AFUNIX_H

53\#include \<afunix.h\>

54\#endif

55

56/\* Declarations missing in mingw's and windows sdk 7.0 headers \*/

57extern BOOL WINAPI ConvertStringSidToSidA (LPCSTR StringSid, PSID \*Sid);

58extern BOOL WINAPI ConvertSidToStringSidA (PSID Sid, LPSTR \*StringSid);

59

60\#include \<stdio.h\>

61\#include \<stdlib.h\>

62

63\#include \<string.h\>

64\#if HAVE_ERRNO_H

65\#include \<errno.h\>

66\#endif

67\#ifndef DBUS_WINCE

68\#include \<mbstring.h\>

69\#include \<sys/stat.h\>

70\#include \<sys/types.h\>

71\#endif

72

73\#ifdef HAVE_WS2TCPIP_H

74/\* getaddrinfo for Windows CE (and Windows). \*/

75\#include \<ws2tcpip.h\>

76\#endif

77

78\#ifndef O_BINARY

79\#define O_BINARY 0

80\#endif

81

82\#ifndef PROCESS_QUERY_LIMITED_INFORMATION

83/\* MinGW32 \< 4 does not define this value in its headers \*/

84\#define PROCESS_QUERY_LIMITED_INFORMATION (0x1000)

85\#endif

86

87typedef int socklen_t;

88

89/\* uncomment to enable windows event based poll implementation \*/

90//#define USE_CHRIS_IMPL

91

92void

93\_dbus_win_set_errno (int err)

94{

95\#ifdef DBUS_WINCE

96 SetLastError (err);

97\#else

98 errno = err;

99\#endif

100}

101

102static BOOL is_winxp_sp3_or_lower (void);

103

104/\*

105 \* \_MIB_TCPROW_EX and friends are not available in system headers

106 \* and are mapped to attribute identical ...OWNER_PID typedefs.

107 \*/

108typedef MIB_TCPROW_OWNER_PID \_MIB_TCPROW_EX;

109typedef MIB_TCPTABLE_OWNER_PID MIB_TCPTABLE_EX;

110typedef PMIB_TCPTABLE_OWNER_PID PMIB_TCPTABLE_EX;

111typedef DWORD (WINAPI \*ProcAllocateAndGetTcpExtTableFromStack)(PMIB_TCPTABLE_EX\*,BOOL,HANDLE,DWORD,DWORD);

112

113/\* Not protected by a lock, but if we miss a write, all that

114 \* happens is that the lazy initialization will happen in two threads

115 \* concurrently - it results in the same value either way so that's OK \*/

116static ProcAllocateAndGetTcpExtTableFromStack lpfnAllocateAndGetTcpExTableFromStack = NULL;

117

123static BOOL

124load_ex_ip_helper_procedures(void)

125{

126 HMODULE hModule = LoadLibrary ("iphlpapi.dll");

127 if (hModule == NULL)

128 {

129 \_dbus_verbose ("could not load iphlpapi.dll\n");

130 return FALSE;

131 }

132

133 lpfnAllocateAndGetTcpExTableFromStack = (ProcAllocateAndGetTcpExtTableFromStack) (void (\*)(void))GetProcAddress (hModule, "AllocateAndGetTcpExTableFromStack");

134 if (lpfnAllocateAndGetTcpExTableFromStack == NULL)

135 {

136 \_dbus_verbose ("could not find function AllocateAndGetTcpExTableFromStack in iphlpapi.dll\n");

137 return FALSE;

138 }

139 return TRUE;

140}

141

148static dbus_pid_t

149get_pid_from_extended_tcp_table(int peer_port)

150{

151 dbus_pid_t result;

152 DWORD errorCode, size = 0, i;

153 MIB_TCPTABLE_OWNER_PID \*tcp_table;

154

155 if ((errorCode =

156 GetExtendedTcpTable (NULL, &size, TRUE, AF_INET, TCP_TABLE_OWNER_PID_ALL, 0)) == ERROR_INSUFFICIENT_BUFFER)

157 {

158 tcp_table = (MIB_TCPTABLE_OWNER_PID \*) dbus_malloc (size);

159 if (tcp_table == NULL)

160 {

161 \_dbus_verbose ("Error allocating memory\n");

162 return 0;

163 }

164 }

165 else

166 {

167 \_dbus_win_warn_win_error ("unexpected error returned from GetExtendedTcpTable", errorCode);

168 return 0;

169 }

170

171 if ((errorCode = GetExtendedTcpTable (tcp_table, &size, TRUE, AF_INET, TCP_TABLE_OWNER_PID_ALL, 0)) != NO_ERROR)

172 {

173 \_dbus_verbose ("Error fetching tcp table %d\n", (int)errorCode);

174 dbus_free (tcp_table);

175 return 0;

176 }

177

178 result = 0;

179 for (i = 0; i \< tcp_table-\>dwNumEntries; i++)

180 {

181 MIB_TCPROW_OWNER_PID \*p = &tcp_table-\>table\[i\];

182 int local_address = ntohl (p-\>dwLocalAddr);

183 int local_port = ntohs (p-\>dwLocalPort);

184 if (p-\>dwState == MIB_TCP_STATE_ESTAB

185 && local_address == INADDR_LOOPBACK && local_port == peer_port)

186 result = p-\>dwOwningPid;

187 }

188

189 dbus_free (tcp_table);

190 \_dbus_verbose ("got pid %lu\n", result);

191 return result;

192}

193

201static dbus_pid_t

202get_pid_from_tcp_ex_table(int peer_port)

203{

204 dbus_pid_t result;

205 DWORD errorCode, i;

206 PMIB_TCPTABLE_EX tcp_table = NULL;

207

208 if (!load_ex_ip_helper_procedures ())

209 {

210 \_dbus_verbose

211 ("Error not been able to load iphelper procedures\n");

212 return 0;

213 }

214

215 errorCode = lpfnAllocateAndGetTcpExTableFromStack (&tcp_table, TRUE, GetProcessHeap(), 0, 2);

216

217 if (errorCode != NO_ERROR)

218 {

219 \_dbus_verbose

220 ("Error not been able to call AllocateAndGetTcpExTableFromStack()\n");

221 return 0;

222 }

223

224 result = 0;

225 for (i = 0; i \< tcp_table-\>dwNumEntries; i++)

226 {

227 \_MIB_TCPROW_EX \*p = &tcp_table-\>table\[i\];

228 int local_port = ntohs (p-\>dwLocalPort);

229 int local_address = ntohl (p-\>dwLocalAddr);

230 if (local_address == INADDR_LOOPBACK && local_port == peer_port)

231 {

232 result = p-\>dwOwningPid;

233 break;

234 }

235 }

236

237 HeapFree (GetProcessHeap(), 0, tcp_table);

238 \_dbus_verbose ("got pid %lu\n", result);

239 return result;

240}

241

247static dbus_pid_t

248\_dbus_get_peer_pid_from_tcp_handle (int handle)

249{

250 struct sockaddr_storage addr;

251 socklen_t len = sizeof (addr);

252 int peer_port;

253

254 dbus_pid_t result;

255 dbus_bool_t is_localhost = FALSE;

256

257 getpeername (handle, (struct sockaddr \*) &addr, &len);

258

259 if (addr.ss_family == AF_INET)

260 {

261 struct sockaddr_in \*s = (struct sockaddr_in \*) &addr;

262 peer_port = ntohs (s-\>sin_port);

263 is_localhost = (ntohl (s-\>sin_addr.s_addr) == INADDR_LOOPBACK);

264 }

265 else if (addr.ss_family == AF_INET6)

266 {

267 \_dbus_verbose ("FIXME \[61922\]: IPV6 support not working on windows\n");

268 return 0;

269 /\*

270 struct sockaddr_in6 \*s = (struct sockaddr_in6 \* )&addr;

271 peer_port = ntohs (s-\>sin6_port);

272 is_localhost = (memcmp(s-\>sin6_addr.s6_addr, in6addr_loopback.s6_addr, 16) == 0);

273 \_dbus_verbose ("IPV6 %08x %08x\n", s-\>sin6_addr.s6_addr, in6addr_loopback.s6_addr);

274 \*/

275 }

276 else

277 {

278 \_dbus_verbose ("no idea what address family %d is\n", addr.ss_family);

279 return 0;

280 }

281

282 if (!is_localhost)

283 {

284 \_dbus_verbose ("could not fetch process id from remote process\n");

285 return 0;

286 }

287

288 if (peer_port == 0)

289 {

290 \_dbus_verbose

291 ("Error not been able to fetch tcp peer port from connection\n");

292 return 0;

293 }

294

295 \_dbus_verbose ("trying to get peer's pid\n");

296

297 result = get_pid_from_extended_tcp_table (peer_port);

298 if (result \> 0)

299 return result;

300 result = get_pid_from_tcp_ex_table (peer_port);

301 return result;

302}

303

304/\* Convert GetLastError() to a dbus error. \*/

305const char\*

306\_dbus_win_error_from_last_error (void)

307{

308 switch (GetLastError())

309 {

310 case 0:

311 return DBUS_ERROR_FAILED;

312

313 case ERROR_NO_MORE_FILES:

314 case ERROR_TOO_MANY_OPEN_FILES:

315 return DBUS_ERROR_LIMITS_EXCEEDED; /\* kernel out of memory \*/

316

317 case ERROR_ACCESS_DENIED:

318 case ERROR_CANNOT_MAKE:

319 return DBUS_ERROR_ACCESS_DENIED;

320

321 case ERROR_NOT_ENOUGH_MEMORY:

322 return DBUS_ERROR_NO_MEMORY;

323

324 case ERROR_FILE_EXISTS:

325 return DBUS_ERROR_FILE_EXISTS;

326

327 case ERROR_FILE_NOT_FOUND:

328 case ERROR_PATH_NOT_FOUND:

329 return DBUS_ERROR_FILE_NOT_FOUND;

330

331 default:

332 return DBUS_ERROR_FAILED;

333 }

334}

335

336

337char\*

338\_dbus_win_error_string (int error_number)

339{

340 char \*msg;

341

342 FormatMessageA (FORMAT_MESSAGE_ALLOCATE_BUFFER \|

343 FORMAT_MESSAGE_IGNORE_INSERTS \|

344 FORMAT_MESSAGE_FROM_SYSTEM,

345 NULL, error_number, 0,

346 (LPSTR) &msg, 0, NULL);

347

348 if (msg\[strlen (msg) - 1\] == '\n')

349 msg\[strlen (msg) - 1\] = '\0';

350 if (msg\[strlen (msg) - 1\] == '\r')

351 msg\[strlen (msg) - 1\] = '\0';

352

353 return msg;

354}

355

356void

357\_dbus_win_free_error_string (char \*string)

358{

359 LocalFree (string);

360}

361

382int

383\_dbus_read_socket (DBusSocket fd,

384 DBusString \*buffer,

385 int count)

386{

387 int bytes_read;

388 int start;

389 char \*data;

390

391 \_dbus_assert (count \>= 0);

392

393 start = \_dbus_string_get_length (buffer);

394

395 if (!\_dbus_string_lengthen (buffer, count))

396 {

397 \_dbus_win_set_errno (ENOMEM);

398 return -1;

399 }

400

401 data = \_dbus_string_get_data_len (buffer, start, count);

402

403 again:

404

405 \_dbus_verbose ("recv: count=%d fd=%Iu\n", count, fd.sock);

406 bytes_read = recv (fd.sock, data, count, 0);

407

408 if (bytes_read == SOCKET_ERROR)

409 {

410 DBUS_SOCKET_SET_ERRNO();

411 \_dbus_verbose ("recv: failed: %s (%d)\n", \_dbus_strerror (errno), errno);

412 bytes_read = -1;

413 }

414 else

415 \_dbus_verbose ("recv: = %d\n", bytes_read);

416

417 if (bytes_read \< 0)

418 {

419 if (errno == EINTR)

420 goto again;

421 else

422 {

423 /\* put length back (note that this doesn't actually realloc anything) \*/

424 \_dbus_string_set_length (buffer, start);

425 return -1;

426 }

427 }

428 else

429 {

430 /\* put length back (doesn't actually realloc) \*/

431 \_dbus_string_set_length (buffer, start + bytes_read);

432

433\#if 0

434 if (bytes_read \> 0)

435 \_dbus_verbose_bytes_of_string (buffer, start, bytes_read);

436\#endif

437

438 return bytes_read;

439 }

440}

441

452int

453\_dbus_write_socket (DBusSocket fd,

454 const DBusString \*buffer,

455 int start,

456 int len)

457{

458 const char \*data;

459 int bytes_written;

460

461 data = \_dbus_string_get_const_data_len (buffer, start, len);

462

463 again:

464

465 \_dbus_verbose ("send: len=%d fd=%Iu\n", len, fd.sock);

466 bytes_written = send (fd.sock, data, len, 0);

467

468 if (bytes_written == SOCKET_ERROR)

469 {

470 DBUS_SOCKET_SET_ERRNO();

471 \_dbus_verbose ("send: failed: %s\n", \_dbus_strerror_from_errno ());

472 bytes_written = -1;

473 }

474 else

475 \_dbus_verbose ("send: = %d\n", bytes_written);

476

477 if (bytes_written \< 0 && errno == EINTR)

478 goto again;

479

480\#if 0

481 if (bytes_written \> 0)

482 \_dbus_verbose_bytes_of_string (buffer, start, bytes_written);

483\#endif

484

485 return bytes_written;

486}

487

488

496dbus_bool_t

497\_dbus_close_socket (DBusSocket \*fd,

498 DBusError \*error)

499{

500 \_dbus_assert (fd != NULL);

501 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

502

503 again:

504 if (closesocket (fd-\>sock) == SOCKET_ERROR)

505 {

506 DBUS_SOCKET_SET_ERRNO ();

507

508 if (errno == EINTR)

509 goto again;

510

511 dbus_set_error (error, \_dbus_error_from_errno (errno),

512 "Could not close socket: socket=%Iu, , %s",

513 fd-\>sock, \_dbus_strerror_from_errno ());

514 \_dbus_socket_invalidate (fd);

515 return FALSE;

516 }

517 \_dbus_verbose ("socket=%Iu, \n", fd-\>sock);

518

519 \_dbus_socket_invalidate (fd);

520 return TRUE;

521}

522

530static void

531\_dbus_win_handle_set_close_on_exec (HANDLE handle)

532{

533 if ( !SetHandleInformation( (HANDLE) handle,

534 HANDLE_FLAG_INHERIT \| HANDLE_FLAG_PROTECT_FROM_CLOSE,

535 0 /\*disable both flags\*/ ) )

536 {

537 \_dbus_win_warn_win_error ("Disabling socket handle inheritance failed:", GetLastError());

538 }

539}

540

548dbus_bool_t

549\_dbus_set_socket_nonblocking (DBusSocket handle,

550 DBusError \*error)

551{

552 u_long one = 1;

553

554 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

555

556 if (ioctlsocket (handle.sock, FIONBIO, &one) == SOCKET_ERROR)

557 {

558 DBUS_SOCKET_SET_ERRNO ();

559 dbus_set_error (error, \_dbus_error_from_errno (errno),

560 "Failed to set socket %Iu to nonblocking: %s",

561 handle.sock, \_dbus_strerror_from_errno ());

562 return FALSE;

563 }

564

565 return TRUE;

566}

567

568

589int

590\_dbus_write_socket_two (DBusSocket fd,

591 const DBusString \*buffer1,

592 int start1,

593 int len1,

594 const DBusString \*buffer2,

595 int start2,

596 int len2)

597{

598 WSABUF vectors\[2\];

599 const char \*data1;

600 const char \*data2;

601 int rc;

602 DWORD bytes_written;

603

604 \_dbus_assert (buffer1 != NULL);

605 \_dbus_assert (start1 \>= 0);

606 \_dbus_assert (start2 \>= 0);

607 \_dbus_assert (len1 \>= 0);

608 \_dbus_assert (len2 \>= 0);

609

610

611 data1 = \_dbus_string_get_const_data_len (buffer1, start1, len1);

612

613 if (buffer2 != NULL)

614 data2 = \_dbus_string_get_const_data_len (buffer2, start2, len2);

615 else

616 {

617 data2 = NULL;

618 start2 = 0;

619 len2 = 0;

620 }

621

622 vectors\[0\].buf = (char\*) data1;

623 vectors\[0\].len = len1;

624 vectors\[1\].buf = (char\*) data2;

625 vectors\[1\].len = len2;

626

627 again:

628

629 \_dbus_verbose ("WSASend: len1+2=%d+%d fd=%Iu\n", len1, len2, fd.sock);

630 rc = WSASend (fd.sock,

631 vectors,

632 data2 ? 2 : 1,

633 &bytes_written,

634 0,

635 NULL,

636 NULL);

637

638 if (rc == SOCKET_ERROR)

639 {

640 DBUS_SOCKET_SET_ERRNO ();

641 \_dbus_verbose ("WSASend: failed: %s\n", \_dbus_strerror_from_errno ());

642 bytes_written = (DWORD) -1;

643 }

644 else

645 \_dbus_verbose ("WSASend: = %ld\n", bytes_written);

646

647 if (bytes_written == (DWORD) -1 && errno == EINTR)

648 goto again;

649

650 return bytes_written;

651}

652

653\#if 0

654

663int

664\_dbus_connect_named_pipe (const char \*path,

665 DBusError \*error)

666{

667 \_dbus_assert_not_reached ("not implemented");

668}

669

670\#endif

671

675dbus_bool_t

676\_dbus_win_startup_winsock (void)

677{

678 /\* Straight from MSDN, deuglified \*/

679

680 /\* Protected by \_DBUS_LOCK_sysdeps \*/

681 static dbus_bool_t beenhere = FALSE;

682

683 WORD wVersionRequested;

684 WSADATA wsaData;

685 int err;

686

687 if (!\_DBUS_LOCK (sysdeps))

688 return FALSE;

689

690 if (beenhere)

691 goto out;

692

693 wVersionRequested = MAKEWORD (2, 0);

694

695 err = WSAStartup (wVersionRequested, &wsaData);

696 if (err != 0)

697 {

698 \_dbus_assert_not_reached ("Could not initialize WinSock");

699 \_dbus_abort ();

700 }

701

702 /\* Confirm that the WinSock DLL supports 2.0. Note that if the DLL

703 \* supports versions greater than 2.0 in addition to 2.0, it will

704 \* still return 2.0 in wVersion since that is the version we

705 \* requested.

706 \*/

707 if (LOBYTE (wsaData.wVersion) != 2 \|\|

708 HIBYTE (wsaData.wVersion) != 0)

709 {

710 \_dbus_assert_not_reached ("No usable WinSock found");

711 \_dbus_abort ();

712 }

713

714 beenhere = TRUE;

715

716out:

717 \_DBUS_UNLOCK (sysdeps);

718 return TRUE;

719}

720

721

722

723

724

725

726

727

728

729/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

730

731 UTF / string code

732

733 \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

734

738int \_dbus_printf_string_upper_bound (const char \*format,

739 va_list args)

740{

741 /\* MSVCRT's vsnprintf semantics are a bit different \*/

742 char buf\[1024\];

743 int bufsize;

744 int len;

745 va_list args_copy;

746

747 bufsize = sizeof (buf);

748 va_copy (args_copy, args);

749 len = \_vsnprintf (buf, bufsize - 1, format, args_copy);

750 va_end (args_copy);

751

752 while (len == -1) /\* try again \*/

753 {

754 char \*p;

755

756 bufsize \*= 2;

757

758 p = malloc (bufsize);

759

760 if (p == NULL)

761 return -1;

762

763 va_copy (args_copy, args);

764 len = \_vsnprintf (p, bufsize - 1, format, args_copy);

765 va_end (args_copy);

766 free (p);

767 }

768

769 return len;

770}

771

772

780wchar_t \*

781\_dbus_win_utf8_to_utf16 (const char \*str,

782 DBusError \*error)

783{

784 DBusString s;

785 int n;

786 wchar_t \*retval;

787

788 \_dbus_string_init_const (&s, str);

789

790 if (!\_dbus_string_validate_utf8 (&s, 0, \_dbus_string_get_length (&s)))

791 {

792 dbus_set_error_const (error, DBUS_ERROR_FAILED, "Invalid UTF-8");

793 return NULL;

794 }

795

796 n = MultiByteToWideChar (CP_UTF8, 0, str, -1, NULL, 0);

797

798 if (n == 0)

799 {

800 \_dbus_win_set_error_from_win_error (error, GetLastError ());

801 return NULL;

802 }

803

804 retval = dbus_new (wchar_t, n);

805

806 if (!retval)

807 {

808 \_DBUS_SET_OOM (error);

809 return NULL;

810 }

811

812 if (MultiByteToWideChar (CP_UTF8, 0, str, -1, retval, n) != n)

813 {

814 dbus_free (retval);

815 dbus_set_error_const (error, DBUS_ERROR_FAILED, "MultiByteToWideChar inconsistency");

816 return NULL;

817 }

818

819 return retval;

820}

821

829char \*

830\_dbus_win_utf16_to_utf8 (const wchar_t \*str,

831 DBusError \*error)

832{

833 int n;

834 char \*retval;

835

836 n = WideCharToMultiByte (CP_UTF8, 0, str, -1, NULL, 0, NULL, NULL);

837

838 if (n == 0)

839 {

840 \_dbus_win_set_error_from_win_error (error, GetLastError ());

841 return NULL;

842 }

843

844 retval = dbus_malloc (n);

845

846 if (!retval)

847 {

848 \_DBUS_SET_OOM (error);

849 return NULL;

850 }

851

852 if (WideCharToMultiByte (CP_UTF8, 0, str, -1, retval, n, NULL, NULL) != n)

853 {

854 dbus_free (retval);

855 dbus_set_error_const (error, DBUS_ERROR_FAILED, "WideCharToMultiByte inconsistency");

856 return NULL;

857 }

858

859 return retval;

860}

861

862

863

864

865

866

867/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

868

869

870 \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

871

872dbus_bool_t

873\_dbus_win_account_to_sid (const wchar_t \*waccount,

874 void \*\*ppsid,

875 DBusError \*error)

876{

877 dbus_bool_t retval = FALSE;

878 DWORD sid_length, wdomain_length;

879 SID_NAME_USE use;

880 wchar_t \*wdomain;

881

882 \*ppsid = NULL;

883

884 sid_length = 0;

885 wdomain_length = 0;

886 if (!LookupAccountNameW (NULL, waccount, NULL, &sid_length,

887 NULL, &wdomain_length, &use) &&

888 GetLastError () != ERROR_INSUFFICIENT_BUFFER)

889 {

890 \_dbus_win_set_error_from_win_error (error, GetLastError ());

891 return FALSE;

892 }

893

894 \*ppsid = dbus_malloc (sid_length);

895 if (!\*ppsid)

896 {

897 \_DBUS_SET_OOM (error);

898 return FALSE;

899 }

900

901 wdomain = dbus_new (wchar_t, wdomain_length);

902 if (!wdomain)

903 {

904 \_DBUS_SET_OOM (error);

905 goto out1;

906 }

907

908 if (!LookupAccountNameW (NULL, waccount, (PSID) \*ppsid, &sid_length,

909 wdomain, &wdomain_length, &use))

910 {

911 \_dbus_win_set_error_from_win_error (error, GetLastError ());

912 goto out2;

913 }

914

915 if (!IsValidSid ((PSID) \*ppsid))

916 {

917 dbus_set_error_const (error, DBUS_ERROR_FAILED, "Invalid SID");

918 goto out2;

919 }

920

921 retval = TRUE;

922

923out2:

924 dbus_free (wdomain);

925out1:

926 if (!retval)

927 {

928 dbus_free (\*ppsid);

929 \*ppsid = NULL;

930 }

931

932 return retval;

933}

934

944unsigned long

945\_dbus_pid_for_log (void)

946{

947 return \_dbus_getpid ();

948}

949

950\#ifndef DBUS_WINCE

951

952static BOOL

953is_winxp_sp3_or_lower (void)

954{

955 OSVERSIONINFOEX osvi;

956 DWORDLONG dwlConditionMask = 0;

957 int op=VER_LESS_EQUAL;

958

959 // Initialize the OSVERSIONINFOEX structure.

960

961 ZeroMemory(&osvi, sizeof(OSVERSIONINFOEX));

962 osvi.dwOSVersionInfoSize = sizeof(OSVERSIONINFOEX);

963 osvi.dwMajorVersion = 5;

964 osvi.dwMinorVersion = 1;

965 osvi.wServicePackMajor = 3;

966 osvi.wServicePackMinor = 0;

967

968 // Initialize the condition mask.

969

970 VER_SET_CONDITION (dwlConditionMask, VER_MAJORVERSION, op);

971 VER_SET_CONDITION (dwlConditionMask, VER_MINORVERSION, op);

972 VER_SET_CONDITION (dwlConditionMask, VER_SERVICEPACKMAJOR, op);

973 VER_SET_CONDITION (dwlConditionMask, VER_SERVICEPACKMINOR, op);

974

975 // Perform the test.

976

977 return VerifyVersionInfo(

978 &osvi,

979 VER_MAJORVERSION \| VER_MINORVERSION \|

980 VER_SERVICEPACKMAJOR \| VER_SERVICEPACKMINOR,

981 dwlConditionMask);

982}

983

989dbus_bool_t

990\_dbus_getsid(char \*\*sid, dbus_pid_t process_id)

991{

992 HANDLE process_token = INVALID_HANDLE_VALUE;

993 TOKEN_USER \*token_user = NULL;

994 DWORD n;

995 PSID psid;

996 int retval = FALSE;

997

998 HANDLE process_handle;

999 if (process_id == 0)

1000 process_handle = GetCurrentProcess();

1001 else if (is_winxp_sp3_or_lower())

1002 process_handle = OpenProcess(PROCESS_QUERY_INFORMATION, FALSE, process_id);

1003 else

1004 process_handle = OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION, FALSE, process_id);

1005

1006 if (!OpenProcessToken (process_handle, TOKEN_QUERY, &process_token))

1007 {

1008 \_dbus_win_warn_win_error ("OpenProcessToken failed", GetLastError ());

1009 goto failed;

1010 }

1011 if ((!GetTokenInformation (process_token, TokenUser, NULL, 0, &n)

1012 && GetLastError () != ERROR_INSUFFICIENT_BUFFER)

1013 \|\| (token_user = alloca (n)) == NULL

1014 \|\| !GetTokenInformation (process_token, TokenUser, token_user, n, &n))

1015 {

1016 \_dbus_win_warn_win_error ("GetTokenInformation failed", GetLastError ());

1017 goto failed;

1018 }

1019 psid = token_user-\>User.Sid;

1020 if (!IsValidSid (psid))

1021 {

1022 \_dbus_verbose("invalid sid\n");

1023 goto failed;

1024 }

1025 if (!ConvertSidToStringSidA (psid, sid))

1026 {

1027 \_dbus_verbose("invalid sid\n");

1028 goto failed;

1029 }

1030//okay:

1031 retval = TRUE;

1032

1033failed:

1034 CloseHandle (process_handle);

1035 if (process_token != INVALID_HANDLE_VALUE)

1036 CloseHandle (process_token);

1037

1038 \_dbus_verbose("\_dbus_getsid() got '%s' and returns %d\n", \*sid, retval);

1039 return retval;

1040}

1041\#endif

1042

1043/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

1044

1045 pipes

1046

1047 \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

1048

1061dbus_bool_t

1062\_dbus_socketpair (DBusSocket \*fd1,

1063 DBusSocket \*fd2,

1064 dbus_bool_t blocking,

1065 DBusError \*error)

1066{

1067 SOCKET temp, socket1 = -1, socket2 = -1;

1068 struct sockaddr_in saddr;

1069 int len;

1070 u_long arg;

1071

1072 if (!\_dbus_win_startup_winsock ())

1073 {

1074 \_DBUS_SET_OOM (error);

1075 return FALSE;

1076 }

1077

1078 temp = socket (AF_INET, SOCK_STREAM, 0);

1079 if (temp == INVALID_SOCKET)

1080 {

1081 DBUS_SOCKET_SET_ERRNO ();

1082 goto out0;

1083 }

1084

1085 \_DBUS_ZERO (saddr);

1086 saddr.sin_family = AF_INET;

1087 saddr.sin_port = 0;

1088 saddr.sin_addr.s_addr = htonl (INADDR_LOOPBACK);

1089

1090 if (bind (temp, (struct sockaddr \*)&saddr, sizeof (saddr)) == SOCKET_ERROR)

1091 {

1092 DBUS_SOCKET_SET_ERRNO ();

1093 goto out0;

1094 }

1095

1096 if (listen (temp, 1) == SOCKET_ERROR)

1097 {

1098 DBUS_SOCKET_SET_ERRNO ();

1099 goto out0;

1100 }

1101

1102 len = sizeof (saddr);

1103 if (getsockname (temp, (struct sockaddr \*)&saddr, &len) == SOCKET_ERROR)

1104 {

1105 DBUS_SOCKET_SET_ERRNO ();

1106 goto out0;

1107 }

1108

1109 socket1 = socket (AF_INET, SOCK_STREAM, 0);

1110 if (socket1 == INVALID_SOCKET)

1111 {

1112 DBUS_SOCKET_SET_ERRNO ();

1113 goto out0;

1114 }

1115

1116 if (connect (socket1, (struct sockaddr \*)&saddr, len) == SOCKET_ERROR)

1117 {

1118 DBUS_SOCKET_SET_ERRNO ();

1119 goto out1;

1120 }

1121

1122 socket2 = accept (temp, (struct sockaddr \*) &saddr, &len);

1123 if (socket2 == INVALID_SOCKET)

1124 {

1125 DBUS_SOCKET_SET_ERRNO ();

1126 goto out1;

1127 }

1128

1129 if (!blocking)

1130 {

1131 arg = 1;

1132 if (ioctlsocket (socket1, FIONBIO, &arg) == SOCKET_ERROR)

1133 {

1134 DBUS_SOCKET_SET_ERRNO ();

1135 goto out2;

1136 }

1137

1138 arg = 1;

1139 if (ioctlsocket (socket2, FIONBIO, &arg) == SOCKET_ERROR)

1140 {

1141 DBUS_SOCKET_SET_ERRNO ();

1142 goto out2;

1143 }

1144 }

1145

1146 fd1-\>sock = socket1;

1147 fd2-\>sock = socket2;

1148

1149 \_dbus_verbose ("full-duplex pipe %Iu:%Iu \<-\> %Iu:%Iu\n",

1150 fd1-\>sock, socket1, fd2-\>sock, socket2);

1151

1152 closesocket (temp);

1153

1154 return TRUE;

1155

1156out2:

1157 closesocket (socket2);

1158out1:

1159 closesocket (socket1);

1160out0:

1161 closesocket (temp);

1162

1163 dbus_set_error (error, \_dbus_error_from_errno (errno),

1164 "Could not setup socket pair: %s",

1165 \_dbus_strerror_from_errno ());

1166

1167 return FALSE;

1168}

1169

1170\#ifdef DBUS_ENABLE_VERBOSE_MODE

1171static dbus_bool_t

1172\_dbus_dump_fd_events (DBusPollFD \*fds, int n_fds)

1173{

1174 DBusString msg = \_DBUS_STRING_INIT_INVALID;

1175 dbus_bool_t result = FALSE;

1176 int i;

1177

1178 if (!\_dbus_string_init (&msg))

1179 goto oom;

1180

1181 for (i = 0; i \< n_fds; i++)

1182 {

1183 DBusPollFD \*fdp = &fds\[i\];

1184 if (!\_dbus_string_append (&msg, i \> 0 ? "\n\t" : "\t"))

1185 goto oom;

1186

1187 if ((fdp-\>events & \_DBUS_POLLIN) &&

1188 !\_dbus_string_append_printf (&msg, "R:%Iu ", fdp-\>fd.sock))

1189 goto oom;

1190

1191 if ((fdp-\>events & \_DBUS_POLLOUT) &&

1192 !\_dbus_string_append_printf (&msg, "W:%Iu ", fdp-\>fd.sock))

1193 goto oom;

1194

1195 if (!\_dbus_string_append_printf (&msg, "E:%Iu", fdp-\>fd.sock))

1196 goto oom;

1197 }

1198

1199 \_dbus_verbose ("%s\n", \_dbus_string_get_const_data (&msg));

1200 result = TRUE;

1201oom:

1202 \_dbus_string_free (&msg);

1203 return result;

1204}

1205

1206\#ifdef USE_CHRIS_IMPL

1207static dbus_bool_t

1208\_dbus_dump_fd_revents (DBusPollFD \*fds, int n_fds)

1209{

1210 DBusString msg = \_DBUS_STRING_INIT_INVALID;

1211 dbus_bool_t result = FALSE;

1212 int i;

1213

1214 if (!\_dbus_string_init (&msg))

1215 goto oom;

1216

1217 for (i = 0; i \< n_fds; i++)

1218 {

1219 DBusPollFD \*fdp = &fds\[i\];

1220 if (!\_dbus_string_append (&msg, i \> 0 ? "\n\t" : "\t"))

1221 goto oom;

1222

1223 if ((fdp-\>revents & \_DBUS_POLLIN) &&

1224 !\_dbus_string_append_printf (&msg, "R:%Iu ", fdp-\>fd.sock))

1225 goto oom;

1226

1227 if ((fdp-\>revents & \_DBUS_POLLOUT) &&

1228 !\_dbus_string_append_printf (&msg, "W:%Iu ", fdp-\>fd.sock))

1229 goto oom;

1230

1231 if ((fdp-\>revents & \_DBUS_POLLERR) &&

1232 !\_dbus_string_append_printf (&msg, "E:%Iu", fdp-\>fd.sock))

1233 goto oom;

1234 }

1235

1236 \_dbus_verbose ("%s\n", \_dbus_string_get_const_data (&msg));

1237 result = TRUE;

1238oom:

1239 \_dbus_string_free (&msg);

1240 return result;

1241}

1242\#else

1243static dbus_bool_t

1244\_dbus_dump_fdset (DBusPollFD \*fds, int n_fds, fd_set \*read_set, fd_set \*write_set, fd_set \*err_set)

1245{

1246 DBusString msg = \_DBUS_STRING_INIT_INVALID;

1247 dbus_bool_t result = FALSE;

1248 int i;

1249

1250 if (!\_dbus_string_init (&msg))

1251 goto oom;

1252

1253 for (i = 0; i \< n_fds; i++)

1254 {

1255 DBusPollFD \*fdp = &fds\[i\];

1256

1257 if (!\_dbus_string_append (&msg, i \> 0 ? "\n\t" : "\t"))

1258 goto oom;

1259

1260 if (FD_ISSET (fdp-\>fd.sock, read_set) &&

1261 !\_dbus_string_append_printf (&msg, "R:%Iu ", fdp-\>fd.sock))

1262 goto oom;

1263

1264 if (FD_ISSET (fdp-\>fd.sock, write_set) &&

1265 !\_dbus_string_append_printf (&msg, "W:%Iu ", fdp-\>fd.sock))

1266 goto oom;

1267

1268 if (FD_ISSET (fdp-\>fd.sock, err_set) &&

1269 !\_dbus_string_append_printf (&msg, "E:%Iu", fdp-\>fd.sock))

1270 goto oom;

1271 }

1272 \_dbus_verbose ("%s\n", \_dbus_string_get_const_data (&msg));

1273 result = TRUE;

1274oom:

1275 \_dbus_string_free (&msg);

1276 return result;

1277}

1278\#endif

1279\#endif

1280

1281\#ifdef USE_CHRIS_IMPL

1290static int

1291\_dbus_poll_events (DBusPollFD \*fds,

1292 int n_fds,

1293 int timeout_milliseconds)

1294{

1295 int ret = 0;

1296 int i;

1297 DWORD ready;

1298

1299\#define DBUS_STACK_WSAEVENTS 256

1300 WSAEVENT eventsOnStack\[DBUS_STACK_WSAEVENTS\];

1301 WSAEVENT \*pEvents = NULL;

1302 if (n_fds \> DBUS_STACK_WSAEVENTS)

1303 pEvents = calloc(sizeof(WSAEVENT), n_fds);

1304 else

1305 pEvents = eventsOnStack;

1306

1307 if (pEvents == NULL)

1308 {

1309 \_dbus_win_set_errno (ENOMEM);

1310 ret = -1;

1311 goto oom;

1312 }

1313

1314\#ifdef DBUS_ENABLE_VERBOSE_MODE

1315 \_dbus_verbose ("\_dbus_poll: to=%d", timeout_milliseconds);

1316 if (!\_dbus_dump_fd_events (fds, n_fds))

1317 {

1318 \_dbus_win_set_errno (ENOMEM);

1319 ret = -1;

1320 goto oom;

1321 }

1322\#endif

1323

1324 for (i = 0; i \< n_fds; i++)

1325 pEvents\[i\] = WSA_INVALID_EVENT;

1326

1327 for (i = 0; i \< n_fds; i++)

1328 {

1329 DBusPollFD \*fdp = &fds\[i\];

1330 WSAEVENT ev;

1331 long lNetworkEvents = FD_OOB;

1332

1333 ev = WSACreateEvent();

1334

1335 if (fdp-\>events & \_DBUS_POLLIN)

1336 lNetworkEvents \|= FD_READ \| FD_ACCEPT \| FD_CLOSE;

1337

1338 if (fdp-\>events & \_DBUS_POLLOUT)

1339 lNetworkEvents \|= FD_WRITE \| FD_CONNECT;

1340

1341 WSAEventSelect (fdp-\>fd.sock, ev, lNetworkEvents);

1342

1343 pEvents\[i\] = ev;

1344 }

1345

1346 ready = WSAWaitForMultipleEvents (n_fds, pEvents, FALSE, timeout_milliseconds, FALSE);

1347

1348 if (ready == WSA_WAIT_FAILED)

1349 {

1350 DBUS_SOCKET_SET_ERRNO ();

1351 if (errno != WSAEWOULDBLOCK)

1352 \_dbus_verbose ("WSAWaitForMultipleEvents: failed: %s\n", \_dbus_strerror_from_errno ());

1353 ret = -1;

1354 }

1355 else if (ready == WSA_WAIT_TIMEOUT)

1356 {

1357 \_dbus_verbose ("WSAWaitForMultipleEvents: WSA_WAIT_TIMEOUT\n");

1358 ret = 0;

1359 }

1360 else if (ready \< (WSA_WAIT_EVENT_0 + n_fds))

1361 {

1362 for (i = 0; i \< n_fds; i++)

1363 {

1364 DBusPollFD \*fdp = &fds\[i\];

1365 WSANETWORKEVENTS ne;

1366

1367 fdp-\>revents = 0;

1368

1369 WSAEnumNetworkEvents (fdp-\>fd.sock, pEvents\[i\], &ne);

1370

1371 if (ne.lNetworkEvents & (FD_READ \| FD_ACCEPT \| FD_CLOSE))

1372 fdp-\>revents \|= \_DBUS_POLLIN;

1373

1374 if (ne.lNetworkEvents & (FD_WRITE \| FD_CONNECT))

1375 fdp-\>revents \|= \_DBUS_POLLOUT;

1376

1377 if (ne.lNetworkEvents & (FD_OOB))

1378 fdp-\>revents \|= \_DBUS_POLLERR;

1379

1380 if(ne.lNetworkEvents)

1381 ret++;

1382

1383 WSAEventSelect (fdp-\>fd.sock, pEvents\[i\], 0);

1384 }

1385\#ifdef DBUS_ENABLE_VERBOSE_MODE

1386 \_dbus_verbose ("\_dbus_poll: to=%d", timeout_milliseconds);

1387 if (!\_dbus_dump_fd_revents (fds, n_fds))

1388 {

1389 \_dbus_win_set_errno (ENOMEM);

1390 ret = -1;

1391 goto oom;

1392 }

1393\#endif

1394 }

1395 else

1396 {

1397 \_dbus_verbose ("WSAWaitForMultipleEvents: failed for unknown reason!");

1398 ret = -1;

1399 }

1400

1401oom:

1402 if (pEvents != NULL)

1403 {

1404 for (i = 0; i \< n_fds; i++)

1405 {

1406 if (pEvents\[i\] != WSA_INVALID_EVENT)

1407 WSACloseEvent (pEvents\[i\]);

1408 }

1409 if (n_fds \> DBUS_STACK_WSAEVENTS)

1410 free (pEvents);

1411 }

1412

1413 return ret;

1414}

1415\#else

1424static int

1425\_dbus_poll_select (DBusPollFD \*fds,

1426 int n_fds,

1427 int timeout_milliseconds)

1428{

1429 fd_set read_set, write_set, err_set;

1430 SOCKET max_fd = 0;

1431 int i;

1432 struct timeval tv;

1433 int ready;

1434

1435 FD_ZERO (&read_set);

1436 FD_ZERO (&write_set);

1437 FD_ZERO (&err_set);

1438\#ifdef DBUS_ENABLE_VERBOSE_MODE

1439 \_dbus_verbose("\_dbus_poll: to=%d\n", timeout_milliseconds);

1440 if (!\_dbus_dump_fd_events (fds, n_fds))

1441 return -1;

1442\#endif

1443

1444 for (i = 0; i \< n_fds; i++)

1445 {

1446 DBusPollFD \*fdp = &fds\[i\];

1447

1448 if (fdp-\>events & \_DBUS_POLLIN)

1449 FD_SET (fdp-\>fd.sock, &read_set);

1450

1451 if (fdp-\>events & \_DBUS_POLLOUT)

1452 FD_SET (fdp-\>fd.sock, &write_set);

1453

1454 FD_SET (fdp-\>fd.sock, &err_set);

1455

1456 max_fd = MAX (max_fd, fdp-\>fd.sock);

1457 }

1458

1459 // Avoid random lockups with send(), for lack of a better solution so far

1460 tv.tv_sec = timeout_milliseconds \< 0 ? 1 : timeout_milliseconds / 1000;

1461 tv.tv_usec = timeout_milliseconds \< 0 ? 0 : (timeout_milliseconds % 1000) \* 1000;

1462

1463 ready = select (max_fd + 1, &read_set, &write_set, &err_set, &tv);

1464

1465 if (DBUS_SOCKET_API_RETURNS_ERROR (ready))

1466 {

1467 DBUS_SOCKET_SET_ERRNO ();

1468 if (errno != WSAEWOULDBLOCK)

1469 \_dbus_verbose ("select: failed: %s\n", \_dbus_strerror_from_errno ());

1470 }

1471 else if (ready == 0)

1472 \_dbus_verbose ("select: = 0\n");

1473 else

1474 if (ready \> 0)

1475 {

1476\#ifdef DBUS_ENABLE_VERBOSE_MODE

1477 \_dbus_verbose ("select: to=%d\n", ready);

1478 if (!\_dbus_dump_fdset (fds, n_fds, &read_set, &write_set, &err_set))

1479 {

1480 \_dbus_win_set_errno (ENOMEM);

1481 return -1;

1482 }

1483\#endif

1484 for (i = 0; i \< n_fds; i++)

1485 {

1486 DBusPollFD \*fdp = &fds\[i\];

1487

1488 fdp-\>revents = 0;

1489

1490 if (FD_ISSET (fdp-\>fd.sock, &read_set))

1491 fdp-\>revents \|= \_DBUS_POLLIN;

1492

1493 if (FD_ISSET (fdp-\>fd.sock, &write_set))

1494 fdp-\>revents \|= \_DBUS_POLLOUT;

1495

1496 if (FD_ISSET (fdp-\>fd.sock, &err_set))

1497 fdp-\>revents \|= \_DBUS_POLLERR;

1498 }

1499 }

1500 return ready;

1501}

1502\#endif

1503

1512int

1513\_dbus_poll (DBusPollFD \*fds,

1514 int n_fds,

1515 int timeout_milliseconds)

1516{

1517\#ifdef USE_CHRIS_IMPL

1518 return \_dbus_poll_events (fds, n_fds, timeout_milliseconds);

1519\#else

1520 return \_dbus_poll_select (fds, n_fds, timeout_milliseconds);

1521\#endif

1522}

1523

1524/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

1525

1526Original CVS version of dbus-sysdeps.c

1527

1528\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

1529/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

1530/\* dbus-sysdeps.c Wrappers around system/libc features (internal to D-Bus implementation)

1531 \*

1532 \* Copyright (C) 2002, 2003 Red Hat, Inc.

1533 \* Copyright (C) 2003 CodeFactory AB

1534 \* Copyright (C) 2005 Novell, Inc.

1535 \*

1536 \* Licensed under the Academic Free License version 2.1

1537 \*

1538 \* This program is free software; you can redistribute it and/or modify

1539 \* it under the terms of the GNU General Public License as published by

1540 \* the Free Software Foundation; either version 2 of the License, or

1541 \* (at your option) any later version.

1542 \*

1543 \* This program is distributed in the hope that it will be useful,

1544 \* but WITHOUT ANY WARRANTY; without even the implied warranty of

1545 \* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the

1546 \* GNU General Public License for more details.

1547 \*

1548 \* You should have received a copy of the GNU General Public License

1549 \* along with this program; if not, write to the Free Software

1550 \* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

1551 \*

1552 \*/

1553

1554

1560void

1561\_dbus_exit (int code)

1562{

1563 \_exit (code);

1564}

1565

1577DBusSocket

1578\_dbus_connect_tcp_socket (const char \*host,

1579 const char \*port,

1580 const char \*family,

1581 DBusError \*error)

1582{

1583 return \_dbus_connect_tcp_socket_with_nonce (host, port, family, (const char\*)NULL, error);

1584}

1585

1586DBusSocket

1587\_dbus_connect_tcp_socket_with_nonce (const char \*host,

1588 const char \*port,

1589 const char \*family,

1590 const char \*noncefile,

1591 DBusError \*error)

1592{

1593 int saved_errno = 0;

1594 DBusList \*connect_errors = NULL;

1595 DBusSocket fd = DBUS_SOCKET_INIT;

1596 int res;

1597 struct addrinfo hints;

1598 struct addrinfo \*ai = NULL;

1599 const struct addrinfo \*tmp;

1600 DBusError \*connect_error;

1601

1602 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

1603

1604 if (!\_dbus_win_startup_winsock ())

1605 {

1606 \_DBUS_SET_OOM (error);

1607 return \_dbus_socket_get_invalid ();

1608 }

1609

1610 \_DBUS_ZERO (hints);

1611

1612 if (!family)

1613 hints.ai_family = AF_UNSPEC;

1614 else if (!strcmp(family, "ipv4"))

1615 hints.ai_family = AF_INET;

1616 else if (!strcmp(family, "ipv6"))

1617 hints.ai_family = AF_INET6;

1618 else

1619 {

1620 dbus_set_error (error,

1621 DBUS_ERROR_BAD_ADDRESS,

1622 "Unknown address family %s", family);

1623 return \_dbus_socket_get_invalid ();

1624 }

1625 hints.ai_protocol = IPPROTO_TCP;

1626 hints.ai_socktype = SOCK_STREAM;

1627\#ifdef AI_ADDRCONFIG

1628 hints.ai_flags = AI_ADDRCONFIG;

1629\#else

1630 hints.ai_flags = 0;

1631\#endif

1632

1633 if ((res = getaddrinfo(host, port, &hints, &ai)) != 0 \|\| !ai)

1634 {

1635 dbus_set_error (error,

1636 \_dbus_error_from_errno (res),

1637 "Failed to lookup host/port: \\%s:%s\\: %s (%d)",

1638 host, port, \_dbus_strerror (res), res);

1639 goto out;

1640 }

1641

1642 tmp = ai;

1643 while (tmp)

1644 {

1645 if ((fd.sock = socket (tmp-\>ai_family, SOCK_STREAM, 0)) == INVALID_SOCKET)

1646 {

1647 saved_errno = \_dbus_get_low_level_socket_errno ();

1648 dbus_set_error (error,

1649 \_dbus_error_from_errno (saved_errno),

1650 "Failed to open socket: %s",

1651 \_dbus_strerror (saved_errno));

1652 \_dbus_assert (!\_dbus_socket_is_valid (fd));

1653 goto out;

1654 }

1655 \_DBUS_ASSERT_ERROR_IS_CLEAR(error);

1656

1657 if (connect (fd.sock, (struct sockaddr\*) tmp-\>ai_addr, tmp-\>ai_addrlen) == SOCKET_ERROR)

1658 {

1659 saved_errno = \_dbus_get_low_level_socket_errno ();

1660 \_dbus_close_socket (&fd, NULL);

1661

1662 connect_error = dbus_new0 (DBusError, 1);

1663

1664 if (connect_error == NULL)

1665 {

1666 \_DBUS_SET_OOM (error);

1667 goto out;

1668 }

1669

1670 dbus_error_init (connect_error);

1671 \_dbus_set_error_with_inet_sockaddr (connect_error,

1672 tmp-\>ai_addr, tmp-\>ai_addrlen,

1673 "Failed to connect to socket",

1674 saved_errno);

1675

1676 if (!\_dbus_list_append (&connect_errors, connect_error))

1677 {

1678 dbus_error_free (connect_error);

1679 dbus_free (connect_error);

1680 \_DBUS_SET_OOM (error);

1681 goto out;

1682 }

1683

1684 tmp = tmp-\>ai_next;

1685 continue;

1686 }

1687

1688 break;

1689 }

1690

1691 if (!\_dbus_socket_is_valid (fd))

1692 {

1693 \_dbus_combine_tcp_errors (&connect_errors, "Failed to connect",

1694 host, port, error);

1695 goto out;

1696 }

1697

1698 if (noncefile != NULL)

1699 {

1700 DBusString noncefileStr;

1701 dbus_bool_t ret;

1702 \_dbus_string_init_const (&noncefileStr, noncefile);

1703 ret = \_dbus_send_nonce (fd, &noncefileStr, error);

1704

1705 if (!ret)

1706 {

1707 \_dbus_close_socket (&fd, NULL);

1708 goto out;

1709 }

1710 }

1711

1712 /\* Every SOCKET is also a HANDLE. \*/

1713 \_dbus_win_handle_set_close_on_exec ((HANDLE) fd.sock);

1714

1715 if (!\_dbus_set_socket_nonblocking (fd, error))

1716 {

1717 \_dbus_close_socket (&fd, NULL);

1718 goto out;

1719 }

1720

1721out:

1722 if (ai != NULL)

1723 freeaddrinfo (ai);

1724

1725 while ((connect_error = \_dbus_list_pop_first (&connect_errors)))

1726 {

1727 dbus_error_free (connect_error);

1728 dbus_free (connect_error);

1729 }

1730

1731 return fd;

1732}

1733

1749int

1750\_dbus_listen_tcp_socket (const char \*host,

1751 const char \*port,

1752 const char \*family,

1753 DBusString \*retport,

1754 const char \*\*retfamily,

1755 DBusSocket \*\*fds_p,

1756 DBusError \*error)

1757{

1758 int saved_errno;

1759 int nlisten_fd = 0, res, i, port_num = -1;

1760 DBusList \*bind_errors = NULL;

1761 DBusError \*bind_error = NULL;

1762 DBusSocket \*listen_fd = NULL;

1763 struct addrinfo hints;

1764 struct addrinfo \*ai, \*tmp;

1765 dbus_bool_t have_ipv4 = FALSE;

1766 dbus_bool_t have_ipv6 = FALSE;

1767

1768 // On Vista, sockaddr_gen must be a sockaddr_in6, and not a sockaddr_in6_old

1769 //That's required for family == IPv6(which is the default on Vista if family is not given)

1770 //So we use our own union instead of sockaddr_gen:

1771

1772 typedef union {

1773 struct sockaddr Address;

1774 struct sockaddr_in AddressIn;

1775 struct sockaddr_in6 AddressIn6;

1776 } mysockaddr_gen;

1777

1778 \*fds_p = NULL;

1779 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

1780

1781 if (!\_dbus_win_startup_winsock ())

1782 {

1783 \_DBUS_SET_OOM (error);

1784 return -1;

1785 }

1786

1787 \_DBUS_ZERO (hints);

1788

1789 if (!family)

1790 hints.ai_family = AF_UNSPEC;

1791 else if (!strcmp(family, "ipv4"))

1792 hints.ai_family = AF_INET;

1793 else if (!strcmp(family, "ipv6"))

1794 hints.ai_family = AF_INET6;

1795 else

1796 {

1797 dbus_set_error (error,

1798 DBUS_ERROR_INVALID_ARGS,

1799 "Unknown address family %s", family);

1800 return -1;

1801 }

1802

1803 hints.ai_protocol = IPPROTO_TCP;

1804 hints.ai_socktype = SOCK_STREAM;

1805\#ifdef AI_ADDRCONFIG

1806 hints.ai_flags = AI_ADDRCONFIG \| AI_PASSIVE;

1807\#else

1808 hints.ai_flags = AI_PASSIVE;

1809\#endif

1810

1811 redo_lookup_with_port:

1812 ai = NULL;

1813 if ((res = getaddrinfo(host, port, &hints, &ai)) != 0 \|\| !ai)

1814 {

1815 dbus_set_error (error,

1816 \_dbus_error_from_errno (res),

1817 "Failed to lookup host/port: \\%s:%s\\: %s (%d)",

1818 host ? host : "\*", port, \_dbus_strerror(res), res);

1819 return -1;

1820 }

1821

1822 tmp = ai;

1823 while (tmp)

1824 {

1825 const int reuseaddr = 1, tcp_nodelay_on = 1;

1826 DBusSocket fd = DBUS_SOCKET_INIT, \*newlisten_fd;

1827

1828 if ((fd.sock = socket (tmp-\>ai_family, SOCK_STREAM, 0)) == INVALID_SOCKET)

1829 {

1830 saved_errno = \_dbus_get_low_level_socket_errno ();

1831 dbus_set_error (error,

1832 \_dbus_error_from_errno (saved_errno),

1833 "Failed to open socket: %s",

1834 \_dbus_strerror (saved_errno));

1835 \_dbus_assert (!\_dbus_socket_is_valid (fd));

1836 goto failed;

1837 }

1838 \_DBUS_ASSERT_ERROR_IS_CLEAR(error);

1839

1840 if (setsockopt (fd.sock, SOL_SOCKET, SO_REUSEADDR, (const char \*)&reuseaddr, sizeof(reuseaddr)) == SOCKET_ERROR)

1841 {

1842 saved_errno = \_dbus_get_low_level_socket_errno ();

1843 \_dbus_warn ("Failed to set socket option \\%s:%s\\: %s",

1844 host ? host : "\*", port, \_dbus_strerror (saved_errno));

1845 }

1846

1847 /\* Nagle's algorithm imposes a huge delay on the initial messages

1848 going over TCP. \*/

1849 if (setsockopt (fd.sock, IPPROTO_TCP, TCP_NODELAY, (const char \*)&tcp_nodelay_on, sizeof (tcp_nodelay_on)) == SOCKET_ERROR)

1850 {

1851 saved_errno = \_dbus_get_low_level_socket_errno ();

1852 \_dbus_warn ("Failed to set TCP_NODELAY socket option \\%s:%s\\: %s",

1853 host ? host : "\*", port, \_dbus_strerror (saved_errno));

1854 }

1855

1856 if (bind (fd.sock, (struct sockaddr \*) tmp-\>ai_addr, tmp-\>ai_addrlen) == SOCKET_ERROR)

1857 {

1858 saved_errno = \_dbus_get_low_level_socket_errno ();

1859 closesocket (fd.sock);

1860

1861 /\*

1862 \* We don't treat this as a fatal error, because there might be

1863 \* other addresses that we can listen on. In particular:

1864 \*

1865 \* - If saved_errno is WSAEADDRINUSE after we

1866 \* "goto redo_lookup_with_port" after binding a port on one of the

1867 \* possible addresses, we will try to bind that same port on

1868 \* every address, including the same address again for a second

1869 \* time, which will fail with WSAEADDRINUSE .

1870 \*

1871 \* - If saved_errno is WSAEADDRINUSE, it might be because binding to

1872 \* an IPv6 address implicitly binds to a corresponding IPv4

1873 \* address or vice versa.

1874 \*

1875 \* - If saved_errno is WSAEADDRNOTAVAIL when we asked for family

1876 \* AF_UNSPEC, it might be because IPv6 is disabled for this

1877 \* particular interface.

1878 \*/

1879 bind_error = dbus_new0 (DBusError, 1);

1880

1881 if (bind_error == NULL)

1882 {

1883 \_DBUS_SET_OOM (error);

1884 goto failed;

1885 }

1886

1887 dbus_error_init (bind_error);

1888 \_dbus_set_error_with_inet_sockaddr (bind_error, tmp-\>ai_addr, tmp-\>ai_addrlen,

1889 "Failed to bind socket",

1890 saved_errno);

1891

1892 if (!\_dbus_list_append (&bind_errors, bind_error))

1893 {

1894 dbus_error_free (bind_error);

1895 dbus_free (bind_error);

1896 \_DBUS_SET_OOM (error);

1897 goto failed;

1898 }

1899

1900 /\* Try the next address, maybe it will work better \*/

1901 tmp = tmp-\>ai_next;

1902 continue;

1903 }

1904

1905 if (listen (fd.sock, 30 /\* backlog \*/) == SOCKET_ERROR)

1906 {

1907 saved_errno = \_dbus_get_low_level_socket_errno ();

1908 closesocket (fd.sock);

1909 \_dbus_set_error_with_inet_sockaddr (error, tmp-\>ai_addr, tmp-\>ai_addrlen,

1910 "Failed to listen on socket",

1911 saved_errno);

1912 goto failed;

1913 }

1914

1915 newlisten_fd = dbus_realloc(listen_fd, sizeof(DBusSocket)\*(nlisten_fd+1));

1916 if (!newlisten_fd)

1917 {

1918 closesocket (fd.sock);

1919 dbus_set_error (error, DBUS_ERROR_NO_MEMORY,

1920 "Failed to allocate file handle array");

1921 goto failed;

1922 }

1923 listen_fd = newlisten_fd;

1924 listen_fd\[nlisten_fd\] = fd;

1925 nlisten_fd++;

1926

1927 if (tmp-\>ai_addr-\>sa_family == AF_INET)

1928 have_ipv4 = TRUE;

1929 else if (tmp-\>ai_addr-\>sa_family == AF_INET6)

1930 have_ipv6 = TRUE;

1931

1932 if (!\_dbus_string_get_length(retport))

1933 {

1934 /\* If the user didn't specify a port, or used 0, then

1935 the kernel chooses a port. After the first address

1936 is bound to, we need to force all remaining addresses

1937 to use the same port \*/

1938 if (!port \|\| !strcmp(port, "0"))

1939 {

1940 mysockaddr_gen addr;

1941 socklen_t addrlen = sizeof(addr);

1942 char portbuf\[NI_MAXSERV\];

1943

1944 if (getsockname (fd.sock, &addr.Address, &addrlen) == SOCKET_ERROR \|\|

1945 (res = getnameinfo (&addr.Address, addrlen, NULL, 0,

1946 portbuf, sizeof(portbuf),

1947 NI_NUMERICSERV)) != 0)

1948 {

1949 saved_errno = \_dbus_get_low_level_socket_errno ();

1950 dbus_set_error (error, \_dbus_error_from_errno (saved_errno),

1951 "Failed to resolve port \\%s:%s\\: %s",

1952 host ? host : "\*", port, \_dbus_strerror (saved_errno));

1953 goto failed;

1954 }

1955 if (!\_dbus_string_append(retport, portbuf))

1956 {

1957 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

1958 goto failed;

1959 }

1960

1961 /\* Release current address list & redo lookup \*/

1962 port = \_dbus_string_get_const_data(retport);

1963 freeaddrinfo(ai);

1964 goto redo_lookup_with_port;

1965 }

1966 else

1967 {

1968 if (!\_dbus_string_append(retport, port))

1969 {

1970 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

1971 goto failed;

1972 }

1973 }

1974 }

1975

1976 tmp = tmp-\>ai_next;

1977 }

1978 freeaddrinfo(ai);

1979 ai = NULL;

1980

1981 if (!nlisten_fd)

1982 {

1983 \_dbus_combine_tcp_errors (&bind_errors, "Failed to bind", host, port, error);

1984 goto failed;

1985 }

1986

1987 if (have_ipv4 && !have_ipv6)

1988 \*retfamily = "ipv4";

1989 else if (!have_ipv4 && have_ipv6)

1990 \*retfamily = "ipv6";

1991

1992 sscanf(\_dbus_string_get_const_data(retport), "%d", &port_num);

1993

1994 for (i = 0 ; i \< nlisten_fd ; i++)

1995 {

1996 \_dbus_win_handle_set_close_on_exec ((HANDLE) listen_fd\[i\].sock);

1997 if (!\_dbus_set_socket_nonblocking (listen_fd\[i\], error))

1998 {

1999 goto failed;

2000 }

2001 }

2002

2003 \*fds_p = listen_fd;

2004

2005 /\* This list might be non-empty even on success, because we might be

2006 \* ignoring WSAEADDRINUSE or WSAEADDRNOTAVAIL \*/

2007 while ((bind_error = \_dbus_list_pop_first (&bind_errors)))

2008 {

2009 dbus_error_free (bind_error);

2010 dbus_free (bind_error);

2011 }

2012 return nlisten_fd;

2013

2014 failed:

2015 if (ai)

2016 freeaddrinfo(ai);

2017 for (i = 0 ; i \< nlisten_fd ; i++)

2018 closesocket (listen_fd\[i\].sock);

2019

2020 while ((bind_error = \_dbus_list_pop_first (&bind_errors)))

2021 {

2022 dbus_error_free (bind_error);

2023 dbus_free (bind_error);

2024 }

2025

2026 dbus_free(listen_fd);

2027 return -1;

2028}

2029

2030

2038DBusSocket

2039\_dbus_accept (DBusSocket listen_fd)

2040{

2041 DBusSocket client_fd;

2042

2043 retry:

2044 client_fd.sock = accept (listen_fd.sock, NULL, NULL);

2045

2046 if (!\_dbus_socket_is_valid (client_fd))

2047 {

2048 DBUS_SOCKET_SET_ERRNO ();

2049 if (errno == EINTR)

2050 goto retry;

2051 }

2052

2053 \_dbus_verbose ("client fd %Iu accepted\n", client_fd.sock);

2054

2055 return client_fd;

2056}

2057

2058

2059

2060

2061dbus_bool_t

2062\_dbus_send_credentials_socket (DBusSocket handle,

2063 DBusError \*error)

2064{

2065/\* FIXME: for the session bus credentials shouldn't matter (?), but

2066 \* for the system bus they are presumably essential. A rough outline

2067 \* of a way to implement the credential transfer would be this:

2068 \*

2069 \* client waits to \*read\* a byte.

2070 \*

2071 \* server creates a named pipe with a random name, sends a byte

2072 \* contining its length, and its name.

2073 \*

2074 \* client reads the name, connects to it (using Win32 API).

2075 \*

2076 \* server waits for connection to the named pipe, then calls

2077 \* ImpersonateNamedPipeClient(), notes its now-current credentials,

2078 \* calls RevertToSelf(), closes its handles to the named pipe, and

2079 \* is done. (Maybe there is some other way to get the SID of a named

2080 \* pipe client without having to use impersonation?)

2081 \*

2082 \* client closes its handles and is done.

2083 \*

2084 \* Ralf: Why not sending credentials over the given this connection ?

2085 \* Using named pipes makes it impossible to be connected from a unix client.

2086 \*

2087 \*/

2088 int bytes_written;

2089 DBusString buf;

2090

2091 \_dbus_string_init_const_len (&buf, "\0", 1);

2092again:

2093 bytes_written = \_dbus_write_socket (handle, &buf, 0, 1 );

2094

2095 if (bytes_written \< 0 && errno == EINTR)

2096 goto again;

2097

2098 if (bytes_written \< 0)

2099 {

2100 dbus_set_error (error, \_dbus_error_from_errno (errno),

2101 "Failed to write credentials byte: %s",

2102 \_dbus_strerror_from_errno ());

2103 return FALSE;

2104 }

2105 else if (bytes_written == 0)

2106 {

2107 dbus_set_error (error, DBUS_ERROR_IO_ERROR,

2108 "wrote zero bytes writing credentials byte");

2109 return FALSE;

2110 }

2111 else

2112 {

2113 \_dbus_assert (bytes_written == 1);

2114 \_dbus_verbose ("wrote 1 zero byte, credential sending isn't implemented yet\n");

2115 return TRUE;

2116 }

2117 return TRUE;

2118}

2119

2120\#ifdef HAVE_AFUNIX_H

2121/\*

2122 \* Returns false with no error set if the socket is non-AF_UNIX

2123 \* (contrary to our usual convention).

2124 \*

2125 \* Returns false with an error set on failure to identify it.

2126 \*/

2127static dbus_bool_t

2128\_dbus_socket_is_af_unix (DBusSocket s,

2129 DBusError \*error)

2130{

2131 struct sockaddr_un saddr;

2132 int len;

2133

2134 len = sizeof (saddr);

2135 if (getsockname (s.sock, (struct sockaddr \*)&saddr, &len) == SOCKET_ERROR)

2136 {

2137 DBUS_SOCKET_SET_ERRNO ();

2138 dbus_set_error (error, \_dbus_error_from_errno (errno),

2139 "Failed to getsockname: %s",

2140 \_dbus_strerror_from_errno ());

2141 return FALSE;

2142 }

2143

2144 return saddr.sun_family == AF_UNIX;

2145}

2146

2152static dbus_pid_t

2153\_dbus_get_peer_pid_from_uds_handle (int handle)

2154{

2155 DWORD pid, drc;

2156

2157 if (WSAIoctl (handle, SIO_AF_UNIX_GETPEERPID,

2158 NULL, 0U,

2159 &pid, sizeof (pid), &drc,

2160 NULL, NULL) == SOCKET_ERROR)

2161 {

2162 \_dbus_verbose ("failed to get peer's pid\n");

2163 return 0;

2164 }

2165

2166 return pid;

2167}

2168\#endif

2169

2188dbus_bool_t

2189\_dbus_read_credentials_socket (DBusSocket handle,

2190 DBusCredentials \*credentials,

2191 DBusError \*error)

2192{

2193 int bytes_read = 0;

2194 DBusString buf;

2195\#ifdef HAVE_AFUNIX_H

2196 dbus_bool_t uds = FALSE;

2197\#endif

2198

2199 char \*sid = NULL;

2200 dbus_pid_t pid;

2201 int retval = FALSE;

2202

2203 // could fail due too OOM

2204 if (\_dbus_string_init (&buf))

2205 {

2206 bytes_read = \_dbus_read_socket (handle, &buf, 1 );

2207

2208 if (bytes_read \> 0)

2209 \_dbus_verbose ("got one zero byte from server\n");

2210

2211 \_dbus_string_free (&buf);

2212 }

2213

2214\#ifdef HAVE_AFUNIX_H

2215 uds = \_dbus_socket_is_af_unix (handle, error);

2216 if (dbus_error_is_set (error))

2217 return FALSE;

2218

2219 if (uds)

2220 pid = \_dbus_get_peer_pid_from_uds_handle (handle.sock);

2221 else

2222\#endif

2223 pid = \_dbus_get_peer_pid_from_tcp_handle (handle.sock);

2224 if (pid == 0)

2225 return TRUE;

2226

2227 \_dbus_credentials_add_pid (credentials, pid);

2228

2229 if (\_dbus_getsid (&sid, pid))

2230 {

2231 if (!\_dbus_credentials_add_windows_sid (credentials, sid))

2232 goto out;

2233 }

2234

2235 retval = TRUE;

2236

2237out:

2238 if (sid)

2239 LocalFree (sid);

2240

2241 return retval;

2242}

2243

2252dbus_bool_t

2253\_dbus_check_dir_is_private_to_user (DBusString \*dir, DBusError \*error)

2254{

2255 /\* TODO \*/

2256 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

2257 return TRUE;

2258}

2259

2260

2271dbus_bool_t

2272\_dbus_concat_dir_and_file (DBusString \*dir,

2273 const DBusString \*next_component)

2274{

2275 dbus_bool_t dir_ends_in_slash;

2276 dbus_bool_t file_starts_with_slash;

2277

2278 if (\_dbus_string_get_length (dir) == 0 \|\|

2279 \_dbus_string_get_length (next_component) == 0)

2280 return TRUE;

2281

2282 dir_ends_in_slash =

2283 ('/' == \_dbus_string_get_byte (dir, \_dbus_string_get_length (dir) - 1) \|\|

2284 '\\' == \_dbus_string_get_byte (dir, \_dbus_string_get_length (dir) - 1));

2285

2286 file_starts_with_slash =

2287 ('/' == \_dbus_string_get_byte (next_component, 0) \|\|

2288 '\\' == \_dbus_string_get_byte (next_component, 0));

2289

2290 if (dir_ends_in_slash && file_starts_with_slash)

2291 {

2292 \_dbus_string_shorten (dir, 1);

2293 }

2294 else if (!(dir_ends_in_slash \|\| file_starts_with_slash))

2295 {

2296 if (!\_dbus_string_append_byte (dir, '\\'))

2297 return FALSE;

2298 }

2299

2300 return \_dbus_string_copy (next_component, 0, dir,

2301 \_dbus_string_get_length (dir));

2302}

2303

2304/\*---------------- DBusCredentials ----------------------------------\*/

2305

2313dbus_bool_t

2314\_dbus_credentials_add_from_user (DBusCredentials \*credentials,

2315 const DBusString \*username,

2316 DBusCredentialsAddFlags flags,

2317 DBusError \*error)

2318{

2319 if (!\_dbus_credentials_add_windows_sid (credentials,

2320 \_dbus_string_get_const_data (username)))

2321 {

2322 \_DBUS_SET_OOM (error);

2323 return FALSE;

2324 }

2325

2326 return TRUE;

2327}

2328

2337dbus_bool_t

2338\_dbus_credentials_add_from_current_process (DBusCredentials \*credentials)

2339{

2340 dbus_bool_t retval = FALSE;

2341 char \*sid = NULL;

2342

2343 if (!\_dbus_getsid(&sid, \_dbus_getpid()))

2344 goto failed;

2345

2346 if (!\_dbus_credentials_add_pid (credentials, \_dbus_getpid()))

2347 goto failed;

2348

2349 if (!\_dbus_credentials_add_windows_sid (credentials,sid))

2350 goto failed;

2351

2352 retval = TRUE;

2353 goto end;

2354failed:

2355 retval = FALSE;

2356end:

2357 if (sid)

2358 LocalFree(sid);

2359

2360 return retval;

2361}

2362

2375dbus_bool_t

2376\_dbus_append_user_from_current_process (DBusString \*str)

2377{

2378 dbus_bool_t retval = FALSE;

2379 char \*sid = NULL;

2380

2381 if (!\_dbus_getsid(&sid, \_dbus_getpid()))

2382 return FALSE;

2383

2384 retval = \_dbus_string_append (str,sid);

2385

2386 LocalFree(sid);

2387 return retval;

2388}

2389

2394dbus_pid_t

2395\_dbus_getpid (void)

2396{

2397 return GetCurrentProcessId ();

2398}

2399

2403dbus_uid_t

2404\_dbus_getuid (void)

2405{

2406 return DBUS_UID_UNSET;

2407}

2408

2410\#define NANOSECONDS_PER_SECOND 1000000000

2412\#define MICROSECONDS_PER_SECOND 1000000

2414\#define MILLISECONDS_PER_SECOND 1000

2416\#define NANOSECONDS_PER_MILLISECOND 1000000

2418\#define MICROSECONDS_PER_MILLISECOND 1000

2419

2424void

2425\_dbus_sleep_milliseconds (int milliseconds)

2426{

2427 Sleep (milliseconds);

2428}

2429

2430

2438void

2439\_dbus_get_real_time (dbus_int64_t \*tv_sec,

2440 long \*tv_usec)

2441{

2442 FILETIME ft;

2443 dbus_uint64_t time64;

2444

2445 GetSystemTimeAsFileTime (&ft);

2446

2447 memcpy (&time64, &ft, sizeof (time64));

2448

2449 /\* Convert from 100s of nanoseconds since 1601-01-01

2450 \* to Unix epoch. Yes, this is Y2038 unsafe.

2451 \*/

2452 time64 -= DBUS_INT64_CONSTANT (116444736000000000);

2453 time64 /= 10;

2454

2455 if (tv_sec)

2456 \*tv_sec = time64 / 1000000;

2457

2458 if (tv_usec)

2459 \*tv_usec = time64 % 1000000;

2460}

2461

2469void

2470\_dbus_get_monotonic_time (dbus_int64_t \*tv_sec,

2471 long \*tv_usec)

2472{

2473 /\* no implementation yet, fall back to wall-clock time \*/

2474 \_dbus_get_real_time (tv_sec, tv_usec);

2475}

2476

2480void

2481\_dbus_disable_sigpipe (void)

2482{

2483}

2484

2493dbus_bool_t

2494\_dbus_create_directory (const DBusString \*filename,

2495 DBusError \*error)

2496{

2497 const char \*filename_c;

2498

2499 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

2500

2501 filename_c = \_dbus_string_get_const_data (filename);

2502

2503 if (!CreateDirectoryA (filename_c, NULL))

2504 {

2505 dbus_set_error (error, DBUS_ERROR_FAILED,

2506 "Failed to create directory %s: %s\n",

2507 filename_c, \_dbus_strerror_from_errno ());

2508 return FALSE;

2509 }

2510 else

2511 return TRUE;

2512}

2513

2522dbus_bool_t

2523\_dbus_ensure_directory (const DBusString \*filename,

2524 DBusError \*error)

2525{

2526 const char \*filename_c;

2527

2528 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

2529

2530 filename_c = \_dbus_string_get_const_data (filename);

2531

2532 if (!CreateDirectoryA (filename_c, NULL))

2533 {

2534 if (GetLastError () == ERROR_ALREADY_EXISTS)

2535 return TRUE;

2536

2537 dbus_set_error (error, DBUS_ERROR_FAILED,

2538 "Failed to create directory %s: %s\n",

2539 filename_c, \_dbus_strerror_from_errno ());

2540 return FALSE;

2541 }

2542 else

2543 return TRUE;

2544}

2545

2546

2556dbus_bool_t

2557\_dbus_generate_random_bytes (DBusString \*str,

2558 int n_bytes,

2559 DBusError \*error)

2560{

2561 int old_len;

2562 unsigned char \*p;

2563 HCRYPTPROV hprov;

2564

2565 old_len = \_dbus_string_get_length (str);

2566

2567 if (!\_dbus_string_lengthen (str, n_bytes))

2568 {

2569 \_DBUS_SET_OOM (error);

2570 return FALSE;

2571 }

2572

2573 p = \_dbus_string_get_udata_len (str, old_len, n_bytes);

2574

2575 if (!CryptAcquireContext (&hprov, NULL, NULL, PROV_RSA_FULL, CRYPT_VERIFYCONTEXT))

2576 {

2577 \_DBUS_SET_OOM (error);

2578 return FALSE;

2579 }

2580

2581 if (!CryptGenRandom (hprov, n_bytes, p))

2582 {

2583 \_DBUS_SET_OOM (error);

2584 CryptReleaseContext (hprov, 0);

2585 return FALSE;

2586 }

2587

2588 CryptReleaseContext (hprov, 0);

2589

2590 return TRUE;

2591}

2592

2598const char\*

2599\_dbus_get_tmpdir(void)

2600{

2601 /\* Protected by \_DBUS_LOCK_sysdeps \*/

2602 static const char\* tmpdir = NULL;

2603 static char buf\[1000\];

2604

2605 if (!\_DBUS_LOCK (sysdeps))

2606 return NULL;

2607

2608 if (tmpdir == NULL)

2609 {

2610 unsigned char \*last_slash;

2611 unsigned char \*p = (unsigned char \*)buf;

2612

2613 if (!GetTempPathA (sizeof (buf), buf))

2614 {

2615 \_dbus_warn ("GetTempPath failed");

2616 \_dbus_abort ();

2617 }

2618

2619 /\* Drop terminating backslash or slash \*/

2620 last_slash = \_mbsrchr (p, '\\');

2621 if (last_slash \> p && last_slash\[1\] == '\0')

2622 last_slash\[0\] = '\0';

2623 last_slash = \_mbsrchr (p, '/');

2624 if (last_slash \> p && last_slash\[1\] == '\0')

2625 last_slash\[0\] = '\0';

2626

2627 tmpdir = buf;

2628 }

2629

2630 \_DBUS_UNLOCK (sysdeps);

2631

2632 \_dbus_assert(tmpdir != NULL);

2633

2634 return tmpdir;

2635}

2636

2637

2646dbus_bool_t

2647\_dbus_delete_file (const DBusString \*filename,

2648 DBusError \*error)

2649{

2650 const char \*filename_c;

2651

2652 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

2653

2654 filename_c = \_dbus_string_get_const_data (filename);

2655

2656 if (DeleteFileA (filename_c) == 0)

2657 {

2658 dbus_set_error (error, DBUS_ERROR_FAILED,

2659 "Failed to delete file %s: %s\n",

2660 filename_c, \_dbus_strerror_from_errno ());

2661 return FALSE;

2662 }

2663 else

2664 return TRUE;

2665}

2666

2667static dbus_uint32_t fromAscii(char ascii)

2668{

2669 if(ascii \>= '0' && ascii \<= '9')

2670 return ascii - '0';

2671 if(ascii \>= 'A' && ascii \<= 'F')

2672 return ascii - 'A' + 10;

2673 if(ascii \>= 'a' && ascii \<= 'f')

2674 return ascii - 'a' + 10;

2675 return 0;

2676}

2677

2678dbus_bool_t \_dbus_read_local_machine_uuid (DBusGUID \*machine_id,

2679 dbus_bool_t create_if_not_found,

2680 DBusError \*error)

2681{

2682\#ifdef DBUS_WINCE

2683 return TRUE;

2684 // TODO

2685\#else

2686 HW_PROFILE_INFOA info;

2687 char \*lpc = &info.szHwProfileGuid\[0\];

2688 dbus_uint32_t u;

2689

2690 // the hw-profile guid lives long enough

2691 if(!GetCurrentHwProfileA(&info))

2692 {

2693 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL); // FIXME

2694 return FALSE;

2695 }

2696

2697 // Form: {12340001-4980-1920-6788-123456789012}

2698 lpc++;

2699 // 12340001

2700 u = ((fromAscii(lpc\[0\]) \<\< 0) \|

2701 (fromAscii(lpc\[1\]) \<\< 4) \|

2702 (fromAscii(lpc\[2\]) \<\< 8) \|

2703 (fromAscii(lpc\[3\]) \<\< 12) \|

2704 (fromAscii(lpc\[4\]) \<\< 16) \|

2705 (fromAscii(lpc\[5\]) \<\< 20) \|

2706 (fromAscii(lpc\[6\]) \<\< 24) \|

2707 (fromAscii(lpc\[7\]) \<\< 28));

2708 machine_id-\>as_uint32s\[0\] = u;

2709

2710 lpc += 9;

2711 // 4980-1920

2712 u = ((fromAscii(lpc\[0\]) \<\< 0) \|

2713 (fromAscii(lpc\[1\]) \<\< 4) \|

2714 (fromAscii(lpc\[2\]) \<\< 8) \|

2715 (fromAscii(lpc\[3\]) \<\< 12) \|

2716 (fromAscii(lpc\[5\]) \<\< 16) \|

2717 (fromAscii(lpc\[6\]) \<\< 20) \|

2718 (fromAscii(lpc\[7\]) \<\< 24) \|

2719 (fromAscii(lpc\[8\]) \<\< 28));

2720 machine_id-\>as_uint32s\[1\] = u;

2721

2722 lpc += 10;

2723 // 6788-1234

2724 u = ((fromAscii(lpc\[0\]) \<\< 0) \|

2725 (fromAscii(lpc\[1\]) \<\< 4) \|

2726 (fromAscii(lpc\[2\]) \<\< 8) \|

2727 (fromAscii(lpc\[3\]) \<\< 12) \|

2728 (fromAscii(lpc\[5\]) \<\< 16) \|

2729 (fromAscii(lpc\[6\]) \<\< 20) \|

2730 (fromAscii(lpc\[7\]) \<\< 24) \|

2731 (fromAscii(lpc\[8\]) \<\< 28));

2732 machine_id-\>as_uint32s\[2\] = u;

2733

2734 lpc += 9;

2735 // 56789012

2736 u = ((fromAscii(lpc\[0\]) \<\< 0) \|

2737 (fromAscii(lpc\[1\]) \<\< 4) \|

2738 (fromAscii(lpc\[2\]) \<\< 8) \|

2739 (fromAscii(lpc\[3\]) \<\< 12) \|

2740 (fromAscii(lpc\[4\]) \<\< 16) \|

2741 (fromAscii(lpc\[5\]) \<\< 20) \|

2742 (fromAscii(lpc\[6\]) \<\< 24) \|

2743 (fromAscii(lpc\[7\]) \<\< 28));

2744 machine_id-\>as_uint32s\[3\] = u;

2745\#endif

2746 return TRUE;

2747}

2748

2749// for proper cleanup in dbus-daemon

2750static HANDLE hDBusDaemonMutex = NULL;

2751static HANDLE hDBusSharedMem = NULL;

2752// sync \_dbus_daemon_publish_session_bus_address, \_dbus_daemon_unpublish_session_bus_address and \_dbus_daemon_already_runs

2753static const char \*cUniqueDBusInitMutex = "UniqueDBusInitMutex";

2754// sync \_dbus_get_autolaunch_address

2755static const char \*cDBusAutolaunchMutex = "DBusAutolaunchMutex";

2756// mutex to determine if dbus-daemon is already started (per user)

2757static const char \*cDBusDaemonMutex = "DBusDaemonMutex";

2758// named shm for dbus adress info (per user)

2759static const char \*cDBusDaemonAddressInfo = "DBusDaemonAddressInfo";

2760

2761/\* custom command line parameter for autolaunching daemon \*/

2762static const char \*autolaunch_custom_command_line_parameter = NULL;

2763

2776void \_dbus_test_win_autolaunch_set_command_line_parameter (const char \*path)

2777{

2778 autolaunch_custom_command_line_parameter = path;

2779}

2780

2781static HANDLE \*autolaunch_handle_location;

2782

2793void

2794\_dbus_test_win_set_autolaunch_handle_location (HANDLE \*location)

2795{

2796 autolaunch_handle_location = location;

2797}

2798

2809static dbus_bool_t

2810\_dbus_get_install_root_as_hash (DBusString \*out)

2811{

2812 DBusString install_path;

2813 dbus_bool_t retval = FALSE;

2814 \_dbus_assert (out != NULL);

2815

2816 if (!\_dbus_string_init (&install_path))

2817 return FALSE;

2818

2819 if (!\_dbus_get_install_root (&install_path))

2820 goto out;

2821

2822 /\* the install path can't be determined \*/

2823 if (\_dbus_string_get_length (&install_path) == 0)

2824 {

2825 \_dbus_string_set_length (out, 0);

2826 retval = TRUE;

2827 goto out;

2828 }

2829

2830 \_dbus_string_tolower_ascii (&install_path, 0, \_dbus_string_get_length (&install_path));

2831

2832 if (!\_dbus_sha_compute (&install_path, out))

2833 goto out;

2834

2835 retval = TRUE;

2836

2837out:

2838 \_dbus_string_free (&install_path);

2839 return retval;

2840}

2841

2860static dbus_bool_t

2861\_dbus_get_address_string (DBusString \*out, const char \*basestring, const char \*scope)

2862{

2863 \_dbus_assert (out != NULL);

2864

2865 if (!scope \|\| strlen (scope) == 0)

2866 {

2867 return \_dbus_string_append (out, basestring);

2868 }

2869 else if (strcmp (scope, "\*install-path") == 0

2870 // for 1.3 compatibility

2871 \|\| strcmp (scope, "install-path") == 0)

2872 {

2873 DBusString temp;

2874 dbus_bool_t retval = FALSE;

2875

2876 if (!\_dbus_string_init (&temp))

2877 return FALSE;

2878

2879 if (!\_dbus_get_install_root_as_hash (&temp))

2880 goto out;

2881

2882 if (\_dbus_string_get_length (&temp) == 0)

2883 {

2884 \_dbus_string_set_length (out, 0);

2885 retval = TRUE;

2886 goto out;

2887 }

2888

2889 if (!\_dbus_string_append_printf (out, "%s-%s", basestring, \_dbus_string_get_const_data (&temp)))

2890 goto out;

2891

2892 retval = TRUE;

2893out:

2894 \_dbus_string_free (&temp);

2895 return retval;

2896 }

2897 else if (strcmp (scope, "\*user") == 0)

2898 {

2899 char \*sid = NULL;

2900 dbus_bool_t retval;

2901

2902 if (!\_dbus_getsid (&sid, \_dbus_getpid()))

2903 return FALSE;

2904

2905 retval = \_dbus_string_append_printf (out, "%s-%s", basestring, sid);

2906

2907 LocalFree(sid);

2908

2909 return retval;

2910 }

2911 else /\* strlen(scope) \> 0 \*/

2912 {

2913 return \_dbus_string_append_printf (out, "%s-%s", basestring, scope);

2914 }

2915}

2916

2925static dbus_bool_t

2926\_dbus_get_shm_name (DBusString \*out,const char \*scope)

2927{

2928 return \_dbus_get_address_string (out, cDBusDaemonAddressInfo, scope);

2929}

2930

2940static dbus_bool_t

2941\_dbus_get_mutex_name (DBusString \*out, const char \*scope)

2942{

2943 return \_dbus_get_address_string (out, cDBusDaemonMutex, scope);

2944}

2945

2946dbus_bool_t

2947\_dbus_daemon_is_session_bus_address_published (const char \*scope)

2948{

2949 DBusRMutex \*lock = NULL;

2950 DBusString mutex_name;

2951

2952 if (!\_dbus_string_init (&mutex_name))

2953 return FALSE;

2954

2955 \_dbus_verbose ("scope:%s\n", scope);

2956 if (!\_dbus_get_mutex_name (&mutex_name, scope) \|\|

2957 /\* not determinable \*/

2958 \_dbus_string_get_length (&mutex_name) == 0)

2959 {

2960 \_dbus_string_free (&mutex_name);

2961 return FALSE;

2962 }

2963

2964 if (hDBusDaemonMutex)

2965 {

2966 \_dbus_verbose ("(scope:%s) -\> yes\n", scope);

2967 return TRUE;

2968 }

2969 lock = \_dbus_win_rmutex_named_new (cUniqueDBusInitMutex);

2970 if (!lock)

2971 return FALSE;

2972

2973 // sync \_dbus_daemon_publish_session_bus_address, \_dbus_daemon_unpublish_session_bus_address and \_dbus_daemon_already_runs

2974 \_dbus_platform_rmutex_lock (lock);

2975

2976 // we use CreateMutex instead of OpenMutex because of possible race conditions,

2977 // see http://msdn.microsoft.com/en-us/library/ms684315%28VS.85%29.aspx

2978 hDBusDaemonMutex = CreateMutexA (NULL, FALSE, \_dbus_string_get_const_data(&mutex_name));

2979

2980 /\* The client uses mutex ownership to detect a running server, so the server should do so too.

2981 Fortunally the client deletes the mutex in the lock protected area, so checking presence

2982 will work too. \*/

2983

2984 \_dbus_platform_rmutex_unlock (lock);

2985 \_dbus_platform_rmutex_free (lock);

2986

2987 \_dbus_string_free (&mutex_name);

2988

2989 if (hDBusDaemonMutex == NULL)

2990 {

2991 \_dbus_verbose ("(scope:%s) -\> no\n", scope);

2992 return FALSE;

2993 }

2994 if (GetLastError() == ERROR_ALREADY_EXISTS)

2995 {

2996 CloseHandle(hDBusDaemonMutex);

2997 hDBusDaemonMutex = NULL;

2998 \_dbus_verbose ("(scope:%s) -\> yes\n", scope);

2999 return TRUE;

3000 }

3001 // mutex wasn't created before, so return false.

3002 // We leave the mutex name allocated for later reusage

3003 // in \_dbus_daemon_publish_session_bus_address.

3004 \_dbus_verbose ("(scope:%s) -\> no\n", scope);

3005 return FALSE;

3006}

3007

3008dbus_bool_t

3009\_dbus_daemon_publish_session_bus_address (const char\* address, const char \*scope)

3010{

3011 DBusRMutex \*lock = NULL;

3012 char \*shared_addr = NULL;

3013 DBusString shm_name = \_DBUS_STRING_INIT_INVALID;

3014 DBusString mutex_name;

3015 dbus_uint64_t len;

3016 dbus_bool_t retval = FALSE;

3017

3018 \_dbus_assert (address);

3019

3020 if (!\_dbus_string_init (&mutex_name))

3021 return FALSE;

3022

3023 \_dbus_verbose ("address:%s scope:%s\n", address, scope);

3024 if (!\_dbus_get_mutex_name (&mutex_name, scope) \|\|

3025 /\* not determinable \*/

3026 \_dbus_string_get_length (&mutex_name) == 0)

3027 {

3028 \_dbus_string_free (&mutex_name);

3029 return FALSE;

3030 }

3031

3032 // sync \_dbus_daemon_publish_session_bus_address, \_dbus_daemon_unpublish_session_bus_address and \_dbus_daemon_already_runs

3033 lock = \_dbus_win_rmutex_named_new (cUniqueDBusInitMutex);

3034 if (lock == NULL)

3035 {

3036 \_dbus_string_free (&mutex_name);

3037 return FALSE;

3038 }

3039

3040 \_dbus_platform_rmutex_lock (lock);

3041

3042 if (!hDBusDaemonMutex)

3043 {

3044 hDBusDaemonMutex = CreateMutexA (NULL, FALSE, \_dbus_string_get_const_data(&mutex_name));

3045 }

3046 \_dbus_string_free (&mutex_name);

3047

3048 // acquire the mutex

3049 if (WaitForSingleObject (hDBusDaemonMutex, 10) != WAIT_OBJECT_0)

3050 {

3051 CloseHandle (hDBusDaemonMutex);

3052 goto out;

3053 }

3054

3055 if (!\_dbus_string_init (&shm_name))

3056 {

3057 goto out;

3058 }

3059

3060 if (!\_dbus_get_shm_name (&shm_name, scope) \|\|

3061 /\* not determinable \*/

3062 \_dbus_string_get_length (&shm_name) == 0)

3063 {

3064 goto out;

3065 }

3066

3067 // create shm

3068 len = strlen (address) + 1;

3069

3070 hDBusSharedMem = CreateFileMappingA ( INVALID_HANDLE_VALUE, NULL, PAGE_READWRITE,

3071 len \>\> 32, len & 0xffffffffu,

3072 \_dbus_string_get_const_data (&shm_name) );

3073 \_dbus_assert (hDBusSharedMem);

3074

3075 shared_addr = MapViewOfFile (hDBusSharedMem, FILE_MAP_WRITE, 0, 0, 0);

3076

3077 \_dbus_assert (shared_addr);

3078

3079 strcpy(shared_addr, address);

3080

3081 // cleanup

3082 UnmapViewOfFile (shared_addr);

3083

3084 \_dbus_verbose ("published session bus address at %s\n",\_dbus_string_get_const_data (&shm_name));

3085 retval = TRUE;

3086

3087out:

3088 \_dbus_platform_rmutex_unlock (lock);

3089 \_dbus_platform_rmutex_free (lock);

3090 \_dbus_string_free (&shm_name);

3091 return retval;

3092}

3093

3111dbus_bool_t

3112\_dbus_daemon_unpublish_session_bus_address (void)

3113{

3114 DBusRMutex \*lock = NULL;

3115

3116 \_dbus_verbose ("\n");

3117 // sync \_dbus_daemon_publish_session_bus_address, \_dbus_daemon_unpublish_session_bus_address and \_dbus_daemon_already_runs

3118 lock = \_dbus_win_rmutex_named_new (cUniqueDBusInitMutex);

3119 if (lock == NULL)

3120 return FALSE;

3121

3122 \_dbus_platform_rmutex_lock (lock);

3123

3124 CloseHandle (hDBusSharedMem);

3125

3126 hDBusSharedMem = NULL;

3127

3128 ReleaseMutex (hDBusDaemonMutex);

3129

3130 CloseHandle (hDBusDaemonMutex);

3131

3132 hDBusDaemonMutex = NULL;

3133

3134 \_dbus_platform_rmutex_unlock (lock);

3135 \_dbus_platform_rmutex_free (lock);

3136 return TRUE;

3137}

3138

3148static dbus_bool_t

3149\_dbus_get_autolaunch_shm (DBusString \*address, DBusString \*shm_name, dbus_bool_t wait)

3150{

3151 HANDLE sharedMem = NULL;

3152 char \*shared_addr;

3153 int i;

3154 int max = 20; /\* max 2 seconds \*/

3155 dbus_bool_t retval = FALSE;

3156

3157 if (!wait)

3158 max = 1;

3159

3160 // read shm

3161 for (i = 0; i \< max; ++i)

3162 {

3163 // we know that dbus-daemon is available, so we wait until shm is available

3164 sharedMem = OpenFileMappingA (FILE_MAP_READ, FALSE, \_dbus_string_get_const_data (shm_name));

3165 if (sharedMem == 0)

3166 Sleep (100);

3167 if (sharedMem != 0)

3168 break;

3169 }

3170

3171 if (sharedMem == 0)

3172 return FALSE;

3173

3174 shared_addr = MapViewOfFile (sharedMem, FILE_MAP_READ, 0, 0, 0);

3175

3176 if (!shared_addr)

3177 goto out;

3178

3179 retval = \_dbus_string_append (address, shared_addr);

3180

3181 UnmapViewOfFile (shared_addr);

3182

3183out:

3184 CloseHandle (sharedMem);

3185 return retval;

3186}

3187

3188static dbus_bool_t

3189\_dbus_daemon_already_runs (DBusString \*address, DBusString \*shm_name, const char \*scope)

3190{

3191 DBusRMutex \*lock = NULL;

3192 HANDLE daemon;

3193 DBusString mutex_name;

3194 dbus_bool_t retval = FALSE;

3195

3196 if (!\_dbus_string_init (&mutex_name))

3197 return FALSE;

3198

3199 if (!\_dbus_get_mutex_name (&mutex_name, scope) \|\|

3200 /\* not determinable \*/

3201 \_dbus_string_get_length (&mutex_name) == 0)

3202 {

3203 \_dbus_string_free (&mutex_name);

3204 return FALSE;

3205 }

3206

3207 // sync \_dbus_daemon_publish_session_bus_address, \_dbus_daemon_unpublish_session_bus_address and \_dbus_daemon_already_runs

3208 lock = \_dbus_win_rmutex_named_new (cUniqueDBusInitMutex);

3209 if (lock == NULL)

3210 return FALSE;

3211

3212 \_dbus_platform_rmutex_lock (lock);

3213

3214 // do checks

3215 daemon = CreateMutexA (NULL, FALSE, \_dbus_string_get_const_data (&mutex_name));

3216 if (WaitForSingleObject (daemon, 10) != WAIT_TIMEOUT)

3217 {

3218 ReleaseMutex (daemon);

3219 CloseHandle (daemon);

3220 goto out;

3221 }

3222

3223 // read shm, wait max 2 seconds

3224 retval = \_dbus_get_autolaunch_shm (address, shm_name, TRUE);

3225

3226 // cleanup

3227 CloseHandle (daemon);

3228

3229out:

3230 \_dbus_platform_rmutex_unlock (lock);

3231 \_dbus_platform_rmutex_free (lock);

3232 \_dbus_string_free (&mutex_name);

3233

3234 return retval;

3235}

3236

3237dbus_bool_t

3238\_dbus_get_autolaunch_address (const char \*scope,

3239 DBusString \*address,

3240 DBusError \*error)

3241{

3242 DBusRMutex \*lock = NULL;

3243 STARTUPINFOA si;

3244 PROCESS_INFORMATION pi;

3245 dbus_bool_t retval = FALSE;

3246 LPSTR lpFile;

3247 char dbus_exe_path\[MAX_PATH\];

3248 DBusString dbus_args = \_DBUS_STRING_INIT_INVALID;

3249 const char \*daemon_name = DBUS_DAEMON_NAME ".exe";

3250 DBusString shm_name;

3251 HANDLE ready_event_handle = NULL;

3252

3253 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

3254

3255 if (!\_dbus_string_init (&shm_name))

3256 {

3257 \_DBUS_SET_OOM (error);

3258 return FALSE;

3259 }

3260

3261 if (!\_dbus_get_shm_name (&shm_name, scope) \|\|

3262 /\* not determinable \*/

3263 \_dbus_string_get_length (&shm_name) == 0)

3264 {

3265 dbus_set_error_const (error, DBUS_ERROR_FAILED, "could not determine shm name");

3266 goto out;

3267 }

3268

3269 lock = \_dbus_win_rmutex_named_new (cDBusAutolaunchMutex);

3270 if (lock == NULL)

3271 {

3272 dbus_set_error (error, DBUS_ERROR_FAILED, "Could not lock '%s'", cDBusAutolaunchMutex);

3273 \_dbus_string_free (&shm_name);

3274 return FALSE;

3275 }

3276

3277 \_dbus_platform_rmutex_lock (lock);

3278

3279 if (\_dbus_daemon_already_runs (address, &shm_name, scope))

3280 {

3281 \_dbus_verbose ("found running dbus daemon for scope '%s' at %s\n",

3282 scope ? scope : "", \_dbus_string_get_const_data (&shm_name));

3283 retval = TRUE;

3284 goto out;

3285 }

3286

3287 if (!SearchPathA (NULL, daemon_name, NULL, sizeof (dbus_exe_path), dbus_exe_path, &lpFile))

3288 {

3289 // Look in directory containing dbus shared library

3290 HMODULE hmod;

3291 char dbus_module_path\[MAX_PATH\];

3292 DWORD rc;

3293

3294 \_dbus_verbose ("did not found dbus daemon executable on default search path, "

3295 "trying path where dbus shared library is located");

3296

3297 hmod = \_dbus_win_get_dll_hmodule ();

3298 rc = GetModuleFileNameA (hmod, dbus_module_path, sizeof (dbus_module_path));

3299 if (rc \<= 0)

3300 {

3301 dbus_set_error_const (error, DBUS_ERROR_FAILED, "could not retrieve dbus shared library file name");

3302 retval = FALSE;

3303 goto out;

3304 }

3305 else

3306 {

3307 char \*ext_idx = strrchr (dbus_module_path, '\\');

3308 if (ext_idx)

3309 \*ext_idx = '\0';

3310 if (!SearchPathA (dbus_module_path, daemon_name, NULL, sizeof (dbus_exe_path), dbus_exe_path, &lpFile))

3311 {

3312 dbus_set_error (error, DBUS_ERROR_FAILED,

3313 "Could not find dbus-daemon executable. "

3314 "Please add the path to %s to your PATH "

3315 "environment variable or start the daemon manually",

3316 daemon_name);

3317 retval = FALSE;

3318 goto out;

3319 }

3320 \_dbus_verbose ("found dbus daemon executable at %s", dbus_module_path);

3321 }

3322 }

3323

3324 // Create process

3325 ZeroMemory (&si, sizeof (si));

3326 si.cb = sizeof (si);

3327 ZeroMemory (&pi, sizeof (pi));

3328

3329 if (!\_dbus_string_init (&dbus_args))

3330 {

3331 dbus_set_error_const (error, DBUS_ERROR_NO_MEMORY, "Failed to initialize argument buffer");

3332 retval = FALSE;

3333 goto out;

3334 }

3335

3336 if (!\_dbus_string_append_printf (&dbus_args, "\\%s\\ %s", dbus_exe_path,

3337 autolaunch_custom_command_line_parameter ? autolaunch_custom_command_line_parameter : "--session"))

3338 {

3339 \_DBUS_SET_OOM (error);

3340 retval = FALSE;

3341 goto out;

3342 }

3343

3344 ready_event_handle = \_dbus_win_event_create_inheritable (error);

3345 if (ready_event_handle == NULL)

3346 goto out;

3347

3348 \_dbus_verbose ("Creating connection readiness event: handle=%p\n", ready_event_handle);

3349 if (!\_dbus_string_append_printf (&dbus_args, " \\--ready-event-handle=%p\\", ready_event_handle))

3350 {

3351 \_DBUS_SET_OOM (error);

3352 goto out;

3353 }

3354

3355 \_dbus_verbose ("Starting dbus daemon with args: '%s'\n", \_dbus_string_get_const_data (&dbus_args));

3356 if (CreateProcessA (dbus_exe_path, \_dbus_string_get_data (&dbus_args), NULL, NULL, TRUE, CREATE_NO_WINDOW, NULL, NULL, &si, &pi))

3357 {

3358 DWORD status;

3359 HANDLE events\[2\];

3360

3361 CloseHandle (pi.hThread);

3362

3363 \_dbus_verbose ("Wait until dbus-daemon is ready for connections (event handle %p)\n", ready_event_handle);

3364

3365 events\[0\] = ready_event_handle;

3366 events\[1\] = pi.hProcess;

3367 status = WaitForMultipleObjects (2, events, FALSE, 30000);

3368

3369 switch (status)

3370 {

3371 case WAIT_OBJECT_0:

3372 /\* ready event signalled, everything is okay \*/

3373 retval = TRUE;

3374 break;

3375

3376 case WAIT_OBJECT_0 + 1:

3377 /\* dbus-daemon process has exited \*/

3378 dbus_set_error (error, DBUS_ERROR_SPAWN_CHILD_EXITED, "dbus-daemon exited before signalling ready");

3379 goto out;

3380

3381 case WAIT_FAILED:

3382 \_dbus_win_set_error_from_last_error (error, "Unable to wait for server readiness (handle %p)", ready_event_handle);

3383 goto out;

3384

3385 case WAIT_TIMEOUT:

3386 /\* GetLastError() is not set \*/

3387 dbus_set_error (error, DBUS_ERROR_TIMEOUT, "Timed out waiting for server readiness or exit (handle %p)", ready_event_handle);

3388 goto out;

3389

3390 default:

3391 /\* GetLastError() is probably not set? \*/

3392 dbus_set_error (error, DBUS_ERROR_FAILED, "Unknown result '%lu' while waiting for server readiness (handle %p)", status, ready_event_handle);

3393 goto out;

3394 }

3395 \_dbus_verbose ("Got signal that dbus-daemon with process id '%ld' is ready for connections\n", GetProcessId (pi.hProcess));

3396

3397 if (autolaunch_handle_location != NULL)

3398 {

3399 \*autolaunch_handle_location = pi.hProcess;

3400 \_dbus_verbose ("Returning process handle of started server (handle=%p)\n", pi.hProcess);

3401 }

3402 else

3403 {

3404 CloseHandle (pi.hProcess);

3405 }

3406

3407 /\* do not wait for the appearance of shm, we can assume that it is present \*/

3408 retval = \_dbus_get_autolaunch_shm (address, &shm_name, FALSE);

3409 if (retval == FALSE)

3410 dbus_set_error_const (error, DBUS_ERROR_FAILED, "Failed to get autolaunch address from launched dbus-daemon");

3411 }

3412 else

3413 {

3414 dbus_set_error_const (error, DBUS_ERROR_FAILED, "Failed to launch dbus-daemon");

3415 retval = FALSE;

3416 }

3417

3418out:

3419 \_DBUS_ASSERT_ERROR_XOR_BOOL (error, retval);

3420 \_dbus_platform_rmutex_unlock (lock);

3421 \_dbus_platform_rmutex_free (lock);

3422 \_dbus_string_free (&shm_name);

3423 \_dbus_string_free (&dbus_args);

3424 if (ready_event_handle)

3425 \_dbus_win_event_free (ready_event_handle, NULL);

3426

3427 \_DBUS_ASSERT_ERROR_XOR_BOOL (error, retval);

3428 return retval;

3429}

3430

3437dbus_bool_t

3438\_dbus_make_file_world_readable(const DBusString \*filename,

3439 DBusError \*error)

3440{

3441 // TODO

3442 return TRUE;

3443}

3444

3452dbus_int32_t

3453\_dbus_atomic_inc (DBusAtomic \*atomic)

3454{

3455\#ifdef HAVE_STDATOMIC_H

3456 /\* Atomic version of "old = \*atomic; \*atomic += 1; return old" \*/

3457 return atomic_fetch_add (&atomic-\>value, 1);

3458\#else

3459 /\* Atomic version of "\*atomic += 1; return \*atomic - 1" \*/

3460 return InterlockedIncrement (&atomic-\>value) - 1;

3461\#endif

3462}

3463

3471dbus_int32_t

3472\_dbus_atomic_dec (DBusAtomic \*atomic)

3473{

3474\#ifdef HAVE_STDATOMIC_H

3475 /\* Atomic version of "old = \*atomic; \*atomic -= 1; return old" \*/

3476 return atomic_fetch_sub (&atomic-\>value, 1);

3477\#else

3478 /\* Atomic version of "\*atomic -= 1; return \*atomic + 1" \*/

3479 return InterlockedDecrement (&atomic-\>value) + 1;

3480\#endif

3481}

3482

3490dbus_int32_t

3491\_dbus_atomic_get (DBusAtomic \*atomic)

3492{

3493\#ifdef HAVE_STDATOMIC_H

3494 /\* Atomic version of "return \*atomic" \*/

3495 return atomic_load (&atomic-\>value);

3496\#else

3497 /\* In this situation, GLib issues a MemoryBarrier() and then returns

3498 \* atomic-\>value. However, mingw from mingw.org (not to be confused with

3499 \* mingw-w64 from mingw-w64.sf.net) does not have MemoryBarrier in its

3500 \* headers, so we have to get a memory barrier some other way.

3501 \*

3502 \* InterlockedIncrement is older, and is documented on MSDN to be a full

3503 \* memory barrier, so let's use that.

3504 \*/

3505 long dummy = 0;

3506

3507 InterlockedExchange (&dummy, 1);

3508

3509 return atomic-\>value;

3510\#endif

3511}

3512

3518void

3519\_dbus_atomic_set_zero (DBusAtomic \*atomic)

3520{

3521\#ifdef HAVE_STDATOMIC_H

3522 /\* Atomic version of "\*atomic = 0" \*/

3523 atomic_store (&atomic-\>value, 0);

3524\#else

3525 InterlockedExchange (&atomic-\>value, 0);

3526\#endif

3527}

3528

3534void

3535\_dbus_atomic_set_nonzero (DBusAtomic \*atomic)

3536{

3537\#ifdef HAVE_STDATOMIC_H

3538 /\* Atomic version of "\*atomic = 1" \*/

3539 atomic_store (&atomic-\>value, 1);

3540\#else

3541 InterlockedExchange (&atomic-\>value, 1);

3542\#endif

3543}

3544

3552void

3553\_dbus_flush_caches (void)

3554{

3555}

3556

3563dbus_bool_t

3564\_dbus_get_is_errno_eagain_or_ewouldblock (int e)

3565{

3566 return e == WSAEWOULDBLOCK;

3567}

3568

3576dbus_bool_t

3577\_dbus_get_install_root (DBusString \*str)

3578{

3579 /\* this is just an initial guess \*/

3580 DWORD pathLength = MAX_PATH;

3581 unsigned char \*lastSlash;

3582 unsigned char \*prefix;

3583

3584 do

3585 {

3586 /\* allocate enough space for our best guess at the length \*/

3587 if (!\_dbus_string_set_length (str, pathLength))

3588 {

3589 \_dbus_string_set_length (str, 0);

3590 return FALSE;

3591 }

3592

3593 SetLastError (0);

3594 pathLength = GetModuleFileNameA (\_dbus_win_get_dll_hmodule (),

3595 \_dbus_string_get_data (str), \_dbus_string_get_length (str));

3596

3597 if (pathLength == 0 \|\| GetLastError () != 0)

3598 {

3599 /\* failed, but not OOM \*/

3600 \_dbus_string_set_length (str, 0);

3601 return TRUE;

3602 }

3603

3604 /\* if the return is strictly less than the buffer size, it has

3605 \* not been truncated, so we can continue \*/

3606 if (pathLength \< (DWORD) \_dbus_string_get_length (str))

3607 {

3608 /\* reduce the length to match what Windows filled in \*/

3609 if (!\_dbus_string_set_length (str, pathLength))

3610 {

3611 \_dbus_string_set_length (str, 0);

3612 return FALSE;

3613 }

3614

3615 break;

3616 }

3617

3618 /\* else it may have been truncated; try with a larger buffer \*/

3619 pathLength \*= 2;

3620 }

3621 while (TRUE);

3622

3623 /\* the rest of this function works by direct byte manipulation of the

3624 \* underlying buffer \*/

3625 prefix = \_dbus_string_get_udata (str);

3626

3627 lastSlash = \_mbsrchr (prefix, '\\');

3628 if (lastSlash == NULL) {

3629 /\* failed, but not OOM \*/

3630 \_dbus_string_set_length (str, 0);

3631 return TRUE;

3632 }

3633 //cut off binary name

3634 lastSlash\[1\] = 0;

3635

3636 //cut possible "\\bin"

3637 //this fails if we are in a double-byte system codepage and the

3638 //folder's name happens to end with the \*bytes\*

3639 //"\\bin"... (I.e. the second byte of some Han character and then

3640 //the Latin "bin", but that is not likely I think...

3641 if (lastSlash - prefix \>= 4 && \_mbsnicmp (lastSlash - 4, (const unsigned char \*)"\\bin", 4) == 0)

3642 lastSlash\[-3\] = 0;

3643 else if (lastSlash - prefix \>= 10 && \_mbsnicmp (lastSlash - 10, (const unsigned char \*)"\\bin\\debug", 10) == 0)

3644 lastSlash\[-9\] = 0;

3645 else if (lastSlash - prefix \>= 12 && \_mbsnicmp (lastSlash - 12, (const unsigned char \*)"\\bin\\release", 12) == 0)

3646 lastSlash\[-11\] = 0;

3647

3648 /\* fix up the length to match the byte-manipulation \*/

3649 \_dbus_string_set_length (str, strlen ((char \*) prefix));

3650

3651 return TRUE;

3652}

3653

3654/\* See comment in dbus-sysdeps-unix.c \*/

3655dbus_bool_t

3656\_dbus_lookup_session_address (dbus_bool_t \*supported,

3657 DBusString \*address,

3658 DBusError \*error)

3659{

3660 /\* Probably fill this in with something based on COM? \*/

3661 \*supported = FALSE;

3662 return TRUE;

3663}

3664

3678dbus_bool_t

3679\_dbus_append_keyring_directory_for_credentials (DBusString \*directory,

3680 DBusCredentials \*credentials)

3681{

3682 DBusString homedir;

3683 DBusString dotdir;

3684 const char \*homepath;

3685 const char \*homedrive;

3686

3687 \_dbus_assert (credentials != NULL);

3688 \_dbus_assert (!\_dbus_credentials_are_anonymous (credentials));

3689

3690 if (!\_dbus_string_init (&homedir))

3691 return FALSE;

3692

3693 homedrive = \_dbus_getenv("HOMEDRIVE");

3694 if (homedrive != NULL && \*homedrive != '\0')

3695 {

3696 \_dbus_string_append(&homedir,homedrive);

3697 }

3698

3699 homepath = \_dbus_getenv("HOMEPATH");

3700 if (homepath != NULL && \*homepath != '\0')

3701 {

3702 \_dbus_string_append(&homedir,homepath);

3703 }

3704

3705\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

3706 {

3707 const char \*override;

3708

3709 override = \_dbus_getenv ("DBUS_TEST_HOMEDIR");

3710 if (override != NULL && \*override != '\0')

3711 {

3712 \_dbus_string_set_length (&homedir, 0);

3713 if (!\_dbus_string_append (&homedir, override))

3714 goto failed;

3715

3716 \_dbus_verbose ("Using fake homedir for testing: %s\n",

3717 \_dbus_string_get_const_data (&homedir));

3718 }

3719 else

3720 {

3721 /\* Not strictly thread-safe, but if we fail at thread-safety here,

3722 \* the worst that will happen is some extra warnings. \*/

3723 static dbus_bool_t already_warned = FALSE;

3724 if (!already_warned)

3725 {

3726 \_dbus_warn ("Using your real home directory for testing, set DBUS_TEST_HOMEDIR to avoid");

3727 already_warned = TRUE;

3728 }

3729 }

3730 }

3731\#endif

3732

3733\#ifdef DBUS_WINCE

3734 /\* It's not possible to create a .something directory in Windows CE

3735 using the file explorer. \*/

3736\#define KEYRING_DIR "dbus-keyrings"

3737\#else

3738\#define KEYRING_DIR ".dbus-keyrings"

3739\#endif

3740

3741 \_dbus_string_init_const (&dotdir, KEYRING_DIR);

3742 if (!\_dbus_concat_dir_and_file (&homedir,

3743 &dotdir))

3744 goto failed;

3745

3746 if (!\_dbus_string_copy (&homedir, 0,

3747 directory, \_dbus_string_get_length (directory))) {

3748 goto failed;

3749 }

3750

3751 \_dbus_string_free (&homedir);

3752 return TRUE;

3753

3754 failed:

3755 \_dbus_string_free (&homedir);

3756 return FALSE;

3757}

3758

3764dbus_bool_t

3765\_dbus_file_exists (const char \*file)

3766{

3767 DWORD attributes = GetFileAttributesA (file);

3768

3769 if (attributes != INVALID_FILE_ATTRIBUTES && GetLastError() != ERROR_PATH_NOT_FOUND)

3770 return TRUE;

3771 else

3772 return FALSE;

3773}

3774

3782const char\*

3783\_dbus_strerror (int error_number)

3784{

3785\#ifdef DBUS_WINCE

3786 // TODO

3787 return "unknown";

3788\#else

3789 const char \*msg;

3790

3791 switch (error_number)

3792 {

3793 case WSAEINTR:

3794 return "Interrupted function call";

3795 case WSAEACCES:

3796 return "Permission denied";

3797 case WSAEFAULT:

3798 return "Bad address";

3799 case WSAEINVAL:

3800 return "Invalid argument";

3801 case WSAEMFILE:

3802 return "Too many open files";

3803 case WSAEWOULDBLOCK:

3804 return "Resource temporarily unavailable";

3805 case WSAEINPROGRESS:

3806 return "Operation now in progress";

3807 case WSAEALREADY:

3808 return "Operation already in progress";

3809 case WSAENOTSOCK:

3810 return "Socket operation on nonsocket";

3811 case WSAEDESTADDRREQ:

3812 return "Destination address required";

3813 case WSAEMSGSIZE:

3814 return "Message too long";

3815 case WSAEPROTOTYPE:

3816 return "Protocol wrong type for socket";

3817 case WSAENOPROTOOPT:

3818 return "Bad protocol option";

3819 case WSAEPROTONOSUPPORT:

3820 return "Protocol not supported";

3821 case WSAESOCKTNOSUPPORT:

3822 return "Socket type not supported";

3823 case WSAEOPNOTSUPP:

3824 return "Operation not supported";

3825 case WSAEPFNOSUPPORT:

3826 return "Protocol family not supported";

3827 case WSAEAFNOSUPPORT:

3828 return "Address family not supported by protocol family";

3829 case WSAEADDRINUSE:

3830 return "Address already in use";

3831 case WSAEADDRNOTAVAIL:

3832 return "Cannot assign requested address";

3833 case WSAENETDOWN:

3834 return "Network is down";

3835 case WSAENETUNREACH:

3836 return "Network is unreachable";

3837 case WSAENETRESET:

3838 return "Network dropped connection on reset";

3839 case WSAECONNABORTED:

3840 return "Software caused connection abort";

3841 case WSAECONNRESET:

3842 return "Connection reset by peer";

3843 case WSAENOBUFS:

3844 return "No buffer space available";

3845 case WSAEISCONN:

3846 return "Socket is already connected";

3847 case WSAENOTCONN:

3848 return "Socket is not connected";

3849 case WSAESHUTDOWN:

3850 return "Cannot send after socket shutdown";

3851 case WSAETIMEDOUT:

3852 return "Connection timed out";

3853 case WSAECONNREFUSED:

3854 return "Connection refused";

3855 case WSAEHOSTDOWN:

3856 return "Host is down";

3857 case WSAEHOSTUNREACH:

3858 return "No route to host";

3859 case WSAEPROCLIM:

3860 return "Too many processes";

3861 case WSAEDISCON:

3862 return "Graceful shutdown in progress";

3863 case WSATYPE_NOT_FOUND:

3864 return "Class type not found";

3865 case WSAHOST_NOT_FOUND:

3866 return "Host not found";

3867 case WSATRY_AGAIN:

3868 return "Nonauthoritative host not found";

3869 case WSANO_RECOVERY:

3870 return "This is a nonrecoverable error";

3871 case WSANO_DATA:

3872 return "Valid name, no data record of requested type";

3873 case WSA_INVALID_HANDLE:

3874 return "Specified event object handle is invalid";

3875 case WSA_INVALID_PARAMETER:

3876 return "One or more parameters are invalid";

3877 case WSA_IO_INCOMPLETE:

3878 return "Overlapped I/O event object not in signaled state";

3879 case WSA_IO_PENDING:

3880 return "Overlapped operations will complete later";

3881 case WSA_NOT_ENOUGH_MEMORY:

3882 return "Insufficient memory available";

3883 case WSA_OPERATION_ABORTED:

3884 return "Overlapped operation aborted";

3885\#ifdef WSAINVALIDPROCTABLE

3886

3887 case WSAINVALIDPROCTABLE:

3888 return "Invalid procedure table from service provider";

3889\#endif

3890\#ifdef WSAINVALIDPROVIDER

3891

3892 case WSAINVALIDPROVIDER:

3893 return "Invalid service provider version number";

3894\#endif

3895\#ifdef WSAPROVIDERFAILEDINIT

3896

3897 case WSAPROVIDERFAILEDINIT:

3898 return "Unable to initialize a service provider";

3899\#endif

3900

3901 case WSASYSCALLFAILURE:

3902 return "System call failure";

3903

3904 default:

3905 msg = strerror (error_number);

3906

3907 if (msg == NULL)

3908 msg = "unknown";

3909

3910 return msg;

3911 }

3912\#endif //DBUS_WINCE

3913}

3914

3922void

3923\_dbus_win_set_error_from_win_error (DBusError \*error,

3924 int code)

3925{

3926 char \*msg;

3927

3928 /\* As we want the English message, use the A API \*/

3929 FormatMessageA (FORMAT_MESSAGE_ALLOCATE_BUFFER \|

3930 FORMAT_MESSAGE_IGNORE_INSERTS \|

3931 FORMAT_MESSAGE_FROM_SYSTEM,

3932 NULL, code, MAKELANGID (LANG_ENGLISH, SUBLANG_ENGLISH_US),

3933 (LPSTR) &msg, 0, NULL);

3934 if (msg)

3935 {

3936 dbus_set_error (error, "win32.error", "%s", msg);

3937 LocalFree (msg);

3938 }

3939 else

3940 dbus_set_error (error, "win32.error", "Unknown error code %d or FormatMessage failed", code);

3941}

3942

3943void

3944\_dbus_win_warn_win_error (const char \*message,

3945 unsigned long code)

3946{

3947 DBusError error;

3948

3949 dbus_error_init (&error);

3950 \_dbus_win_set_error_from_win_error (&error, code);

3951 \_dbus_warn ("%s: %s", message, error.message);

3952 dbus_error_free (&error);

3953}

3954

3962dbus_bool_t

3963\_dbus_delete_directory (const DBusString \*filename,

3964 DBusError \*error)

3965{

3966 const char \*filename_c;

3967

3968 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

3969

3970 filename_c = \_dbus_string_get_const_data (filename);

3971

3972 if (RemoveDirectoryA (filename_c) == 0)

3973 {

3974 char \*emsg = \_dbus_win_error_string (GetLastError ());

3975 dbus_set_error (error, \_dbus_win_error_from_last_error (),

3976 "Failed to remove directory %s: %s",

3977 filename_c, emsg);

3978 \_dbus_win_free_error_string (emsg);

3979 return FALSE;

3980 }

3981

3982 return TRUE;

3983}

3984

3991dbus_bool_t

3992\_dbus_path_is_absolute (const DBusString \*filename)

3993{

3994 if (\_dbus_string_get_length (filename) \> 0)

3995 return \_dbus_string_get_byte (filename, 1) == ':'

3996 \|\| \_dbus_string_get_byte (filename, 0) == '\\'

3997 \|\| \_dbus_string_get_byte (filename, 0) == '/';

3998 else

3999 return FALSE;

4000}

4001

4002dbus_bool_t

4003\_dbus_check_setuid (void)

4004{

4005 return FALSE;

4006}

4007

4008int

4009\_dbus_save_socket_errno (void)

4010{

4011 return errno;

4012}

4013

4014void

4015\_dbus_restore_socket_errno (int saved_errno)

4016{

4017 \_dbus_win_set_errno (saved_errno);

4018}

4019

4020static const char \*log_tag = "dbus";

4021static DBusLogFlags log_flags = DBUS_LOG_FLAGS_STDERR;

4022

4033void

4034\_dbus_init_system_log (const char \*tag,

4035 DBusLogFlags flags)

4036{

4037 /\* We never want to turn off logging completely \*/

4038 \_dbus_assert (

4039 (flags & (DBUS_LOG_FLAGS_STDERR \| DBUS_LOG_FLAGS_SYSTEM_LOG)) != 0);

4040

4041 log_tag = tag;

4042 log_flags = flags;

4043}

4044

4052void

4053\_dbus_logv (DBusSystemLogSeverity severity,

4054 const char \*msg,

4055 va_list args)

4056{

4057 const char \*s = "";

4058 va_list tmp;

4059

4060 switch(severity)

4061 {

4062 case DBUS_SYSTEM_LOG_INFO: s = "info"; break;

4063 case DBUS_SYSTEM_LOG_WARNING: s = "warning"; break;

4064 case DBUS_SYSTEM_LOG_SECURITY: s = "security"; break;

4065 case DBUS_SYSTEM_LOG_ERROR: s = "error"; break;

4066 default: \_dbus_assert_not_reached ("invalid log severity");

4067 }

4068

4069 if (log_flags & DBUS_LOG_FLAGS_SYSTEM_LOG)

4070 {

4071 DBusString out = \_DBUS_STRING_INIT_INVALID;

4072 const char \*message = NULL;

4073 va_copy (tmp, args);

4074

4075 if (!\_dbus_string_init (&out))

4076 goto out;

4077 if (!\_dbus_string_append_printf (&out, "%s: ", s))

4078 goto out;

4079 if (!\_dbus_string_append_printf_valist (&out, msg, tmp))

4080 goto out;

4081 message = \_dbus_string_get_const_data (&out);

4082out:

4083 if (message != NULL)

4084 {

4085 OutputDebugStringA (message);

4086 }

4087 else

4088 {

4089 OutputDebugStringA ("Out of memory while formatting message: '''");

4090 OutputDebugStringA (msg);

4091 OutputDebugStringA ("'''");

4092 }

4093

4094 va_end (tmp);

4095 \_dbus_string_free (&out);

4096 }

4097

4098 if (log_flags & DBUS_LOG_FLAGS_STDERR)

4099 {

4100 va_copy (tmp, args);

4101 fprintf (stderr, "%s\[%lu\]: %s: ", log_tag, \_dbus_pid_for_log (), s);

4102 vfprintf (stderr, msg, tmp);

4103 fprintf (stderr, "\n");

4104 va_end (tmp);

4105 }

4106}

4107

4108/\*

4109 \* Return the low-level representation of a socket error, as used by

4110 \* cross-platform socket APIs like inet_ntop(), send() and recv(). This

4111 \* is the standard errno on Unix, but is WSAGetLastError() on Windows.

4112 \*

4113 \* Some libdbus internal functions copy this into errno, but with

4114 \* hindsight that was probably a design flaw.

4115 \*/

4116int

4117\_dbus_get_low_level_socket_errno (void)

4118{

4119 return WSAGetLastError ();

4120}

4121

4122void

4123\_dbus_win_set_error_from_last_error (DBusError \*error,

4124 const char \*format,

4125 ...)

4126{

4127 const char \*name;

4128 char \*message = NULL;

4129

4130 if (error == NULL)

4131 return;

4132

4133 /\* make sure to do this first, in case subsequent library calls overwrite GetLastError() \*/

4134 name = \_dbus_win_error_from_last_error ();

4135 message = \_dbus_win_error_string (GetLastError ());

4136

4137 if (format != NULL)

4138 {

4139 DBusString str;

4140 va_list args;

4141 dbus_bool_t retval;

4142

4143 if (!\_dbus_string_init (&str))

4144 {

4145 \_DBUS_SET_OOM (error);

4146 goto out;

4147 }

4148

4149 va_start (args, format);

4150 retval = \_dbus_string_append_printf_valist (&str, format, args);

4151 va_end (args);

4152 if (!retval)

4153 {

4154 \_DBUS_SET_OOM (error);

4155 \_dbus_string_free (&str);

4156 goto out;

4157 }

4158

4159 dbus_set_error (error, name, "%s: %s", \_dbus_string_get_const_data (&str), message);

4160 \_dbus_string_free (&str);

4161 }

4162 else

4163 {

4164 dbus_set_error (error, name, "%s", message);

4165 }

4166

4167out:

4168 if (message != NULL)

4169 \_dbus_win_free_error_string (message);

4170

4171 \_DBUS_ASSERT_ERROR_IS_SET (error);

4172}

4173

4185HANDLE

4186\_dbus_win_event_create_inheritable (DBusError \*error)

4187{

4188 HANDLE handle;

4189

4190 handle = CreateEvent (NULL, TRUE, FALSE, NULL);

4191 if (handle == NULL)

4192 {

4193 \_dbus_win_set_error_from_last_error (error, "Could not create event");

4194 return NULL;

4195 }

4196 else if (GetLastError () == ERROR_ALREADY_EXISTS)

4197 {

4198 \_dbus_win_set_error_from_last_error (error, "Event already exists");

4199 return NULL;

4200 }

4201

4202 if (!SetHandleInformation (handle, HANDLE_FLAG_INHERIT, HANDLE_FLAG_INHERIT))

4203 {

4204 \_dbus_win_set_error_from_last_error (error, "Could not set inheritance for event %p", handle);

4205 CloseHandle (handle);

4206 return NULL;

4207 }

4208 return handle;

4209}

4210

4218dbus_bool_t

4219\_dbus_win_event_set (HANDLE handle, DBusError \*error)

4220{

4221 \_dbus_assert (handle != NULL);

4222

4223 if (!SetEvent (handle))

4224 {

4225 \_dbus_win_set_error_from_last_error (error, "Could not trigger event (handle %p)", handle);

4226 return FALSE;

4227 }

4228 return TRUE;

4229}

4230

4241dbus_bool_t

4242\_dbus_win_event_wait (HANDLE handle, int timeout, DBusError \*error)

4243{

4244 DWORD status;

4245

4246 \_dbus_assert (handle != NULL);

4247

4248 status = WaitForSingleObject (handle, timeout);

4249 switch (status)

4250 {

4251 case WAIT_OBJECT_0:

4252 return TRUE;

4253

4254 case WAIT_FAILED:

4255 {

4256 \_dbus_win_set_error_from_last_error (error, "Unable to wait for event (handle %p)", handle);

4257 return FALSE;

4258 }

4259

4260 case WAIT_TIMEOUT:

4261 /\* GetLastError() is not set \*/

4262 dbus_set_error (error, DBUS_ERROR_TIMEOUT, "Timed out waiting for event (handle %p)", handle);

4263 return FALSE;

4264

4265 default:

4266 /\* GetLastError() is probably not set? \*/

4267 dbus_set_error (error, DBUS_ERROR_FAILED, "Unknown result '%lu' while waiting for event (handle %p)", status, handle);

4268 return FALSE;

4269 }

4270}

4271

4280dbus_bool_t

4281\_dbus_win_event_free (HANDLE handle, DBusError \*error)

4282{

4283 if (handle == NULL \|\| handle == INVALID_HANDLE_VALUE)

4284 return TRUE;

4285

4286 if (CloseHandle (handle))

4287 return TRUE;

4288

4289 /\* the handle may already be closed \*/

4290 if (GetLastError () == ERROR_INVALID_HANDLE)

4291 return TRUE;

4292

4293 \_dbus_win_set_error_from_last_error (error, "Could not close event (handle %p)", handle);

4294 return FALSE;

4295}

4296

4297\#ifdef HAVE_AFUNIX_H

4298static dbus_bool_t

4299\_dbus_open_socket (SOCKET \*socket_p,

4300 int domain,

4301 int type,

4302 int protocol,

4303 DBusError \*error)

4304{

4305 if (!\_dbus_win_startup_winsock ())

4306 {

4307 \_DBUS_SET_OOM (error);

4308 return FALSE;

4309 }

4310

4311 \*socket_p = socket (domain, type, protocol);

4312 if (\*socket_p == INVALID_SOCKET)

4313 {

4314 DBUS_SOCKET_SET_ERRNO ();

4315 dbus_set_error (error, \_dbus_error_from_errno (errno),

4316 "Failed to open socket: %s",

4317 \_dbus_strerror_from_errno ());

4318 return FALSE;

4319 }

4320

4321 \_dbus_win_handle_set_close_on_exec ((HANDLE) \*socket_p);

4322 return TRUE;

4323}

4324

4335static dbus_bool_t

4336\_dbus_open_unix_socket (SOCKET \*socket,

4337 DBusError \*error)

4338{

4339 return \_dbus_open_socket (socket, AF_UNIX, SOCK_STREAM, 0, error);

4340}

4341\#endif /\* HAVE_AFUNIX_H \*/

4342

4357DBusSocket

4358\_dbus_connect_unix_socket (const char \*path,

4359 dbus_bool_t abstract,

4360 DBusError \*error)

4361{

4362 DBusSocket s = DBUS_SOCKET_INIT;

4363

4364\#ifdef HAVE_AFUNIX_H

4365 struct sockaddr_un addr;

4366 size_t path_len;

4367

4368 \_DBUS_STATIC_ASSERT (sizeof (addr.sun_path) \> \_DBUS_MAX_SUN_PATH_LENGTH);

4369 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

4370

4371 \_dbus_verbose ("connecting to unix socket %s abstract=%d\n",

4372 path, abstract);

4373

4374 if (abstract)

4375 {

4376 dbus_set_error (error, DBUS_ERROR_NOT_SUPPORTED,

4377 "Failed to connect: UNIX abstract socket is not supported on this system");

4378 return s;

4379 }

4380

4381 path_len = strlen (path);

4382 if (path_len \> \_DBUS_MAX_SUN_PATH_LENGTH)

4383 {

4384 dbus_set_error (error, DBUS_ERROR_BAD_ADDRESS,

4385 "Failed to connect: socket name too long");

4386 return s;

4387 }

4388

4389 if (!\_dbus_open_unix_socket (&s.sock, error))

4390 {

4391 \_DBUS_ASSERT_ERROR_IS_SET (error);

4392 return s;

4393 }

4394 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

4395

4396 \_DBUS_ZERO (addr);

4397 addr.sun_family = AF_UNIX;

4398 strncpy (addr.sun_path, path, sizeof (addr.sun_path) - 1);

4399

4400 if (connect (s.sock, (struct sockaddr \*) &addr, \_DBUS_STRUCT_OFFSET (struct sockaddr_un, sun_path) + path_len) \< 0)

4401 {

4402 DBUS_SOCKET_SET_ERRNO ();

4403 dbus_set_error (error,

4404 \_dbus_error_from_errno (errno),

4405 "Failed to connect to socket %s: %s",

4406 path, \_dbus_strerror (errno));

4407

4408 \_dbus_close_socket (&s, NULL);

4409 return s;

4410 }

4411

4412 if (!\_dbus_set_socket_nonblocking (s, error))

4413 \_dbus_close_socket (&s, NULL);

4414

4415\#else

4416 dbus_set_error (error, DBUS_ERROR_NOT_SUPPORTED,

4417 "Failed to connect: UNIX socket is not supported with this build");

4418\#endif

4419

4420 return s;

4421}

4422

4437DBusSocket

4438\_dbus_listen_unix_socket (const char \*path,

4439 dbus_bool_t abstract,

4440 DBusError \*error)

4441{

4442 DBusSocket s = DBUS_SOCKET_INIT;

4443

4444\#ifdef HAVE_AFUNIX_H

4445 struct sockaddr_un addr;

4446 size_t path_len;

4447 \_DBUS_STATIC_ASSERT (sizeof (addr.sun_path) \> \_DBUS_MAX_SUN_PATH_LENGTH);

4448

4449 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

4450

4451 \_dbus_verbose ("listening on unix socket %s abstract=%d\n",

4452 path, abstract);

4453

4454 if (abstract)

4455 {

4456 dbus_set_error (error, DBUS_ERROR_NOT_SUPPORTED,

4457 "Failed to listen: UNIX abstract socket is not supported on this system");

4458 return s;

4459 }

4460

4461 if (!\_dbus_open_unix_socket (&s.sock, error))

4462 {

4463 \_DBUS_ASSERT_ERROR_IS_SET (error);

4464 return s;

4465 }

4466 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

4467

4468 \_DBUS_ZERO (addr);

4469 addr.sun_family = AF_UNIX;

4470 path_len = strlen (path);

4471

4472 /\* see related comment in dbus-sysdeps-unix.c \*/

4473 /\* there is no S_ISSOCK on windows yet, so just unlink the path \*/

4474 unlink (path);

4475

4476 if (path_len \> \_DBUS_MAX_SUN_PATH_LENGTH)

4477 {

4478 dbus_set_error (error, DBUS_ERROR_BAD_ADDRESS,

4479 "Failed to listen: socket name too long");

4480 \_dbus_close_socket (&s, NULL);

4481 return s;

4482 }

4483

4484 strncpy (addr.sun_path, path, sizeof (addr.sun_path) - 1);

4485

4486 if (bind (s.sock, (struct sockaddr \*) &addr, \_DBUS_STRUCT_OFFSET (struct sockaddr_un, sun_path) + path_len) \< 0)

4487 {

4488 DBUS_SOCKET_SET_ERRNO ();

4489 dbus_set_error (error, \_dbus_error_from_errno (errno),

4490 "Failed to bind socket \\%s\\: %s",

4491 path, \_dbus_strerror (errno));

4492 \_dbus_close_socket (&s, NULL);

4493 return s;

4494 }

4495

4496 if (listen (s.sock, SOMAXCONN /\* backlog \*/) \< 0)

4497 {

4498 DBUS_SOCKET_SET_ERRNO ();

4499 dbus_set_error (error, \_dbus_error_from_errno (errno),

4500 "Failed to listen on socket \\%s\\: %s",

4501 path, \_dbus_strerror (errno));

4502 \_dbus_close_socket (&s, NULL);

4503 return s;

4504 }

4505

4506 if (!\_dbus_set_socket_nonblocking (s, error))

4507 {

4508 \_DBUS_ASSERT_ERROR_IS_SET (error);

4509 \_dbus_close_socket (&s, NULL);

4510 return s;

4511 }

4512\#else

4513 dbus_set_error (error, DBUS_ERROR_NOT_SUPPORTED,

4514 "Failed to listen: UNIX socket is not supported with this build");

4515\#endif

4516

4517 return s;

4518}

4519

4521/\* tests in dbus-sysdeps-util.c \*/

\_dbus_credentials_add_windows_sid

dbus_bool_t \_dbus_credentials_add_windows_sid(DBusCredentials \*credentials, const char \*windows_sid)

Add a Windows user SID to the credentials.

**Definition** dbus-credentials.c:293

\_dbus_credentials_add_pid

dbus_bool_t \_dbus_credentials_add_pid(DBusCredentials \*credentials, dbus_pid_t pid)

Add a UNIX process ID to the credentials.

**Definition** dbus-credentials.c:181

\_dbus_credentials_are_anonymous

dbus_bool_t \_dbus_credentials_are_anonymous(DBusCredentials \*credentials)

Checks whether a credentials object contains a user identity.

**Definition** dbus-credentials.c:558

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

dbus_error_is_set

dbus_bool_t dbus_error_is_set(const DBusError \*error)

Checks whether an error occurred (the error is set).

**Definition** dbus-errors.c:331

\_dbus_file_exists

dbus_bool_t \_dbus_file_exists(const char \*file)

Checks if a file exists.

**Definition** dbus-sysdeps-win.c:3765

\_dbus_delete_file

dbus_bool_t \_dbus_delete_file(const DBusString \*filename, DBusError \*error)

Deletes the given file.

**Definition** dbus-sysdeps-win.c:2647

\_dbus_make_file_world_readable

dbus_bool_t \_dbus_make_file_world_readable(const DBusString \*filename, DBusError \*error)

Makes the file readable by every user in the system.

**Definition** dbus-sysdeps-win.c:3438

\_dbus_assert_not_reached

\#define \_dbus_assert_not_reached(explanation)

Aborts with an error message if called.

**Definition** dbus-internals.h:164

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_DBUS_UNLOCK

\#define \_DBUS_UNLOCK(name)

Unlocks a global lock.

**Definition** dbus-internals.h:438

\_DBUS_LOCK

\#define \_DBUS_LOCK(name)

Locks a global lock, initializing it first if necessary.

**Definition** dbus-internals.h:437

\_dbus_error_from_errno

const char \* \_dbus_error_from_errno(int error_number)

Converts a UNIX errno, or Windows errno or WinSock error value into a DBusError name.

**Definition** dbus-sysdeps.c:565

\_dbus_strerror_from_errno

const char \* \_dbus_strerror_from_errno(void)

Get error message from errno.

**Definition** dbus-sysdeps.c:724

\_dbus_warn

void \_dbus_warn(const char \*format,...)

Prints a warning message to stderr.

**Definition** dbus-internals.c:278

\_DBUS_ZERO

\#define \_DBUS_ZERO(object)

Sets all bits in an object to zero.

**Definition** dbus-internals.h:194

\_dbus_list_pop_first

void \* \_dbus_list_pop_first(DBusList \*\*list)

Removes the first value in the list and returns it.

**Definition** dbus-list.c:679

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

\_dbus_verbose_bytes_of_string

DBUS_PRIVATE_EXPORT void \_dbus_verbose_bytes_of_string(const DBusString \*str, int start, int len)

Dump the given part of the string to verbose log.

**Definition** dbus-marshal-basic.c:1428

dbus_free

void dbus_free(void \*memory)

Frees a block of memory previously allocated by dbus_malloc() or dbus_malloc0().

**Definition** dbus-memory.c:710

dbus_realloc

void \* dbus_realloc(void \*memory, size_t bytes)

Resizes a block of memory previously allocated by dbus_malloc() or dbus_malloc0().

**Definition** dbus-memory.c:610

dbus_new

\#define dbus_new(type, count)

Safe macro for using dbus_malloc().

**Definition** dbus-memory.h:59

dbus_new0

\#define dbus_new0(type, count)

Safe macro for using dbus_malloc0().

**Definition** dbus-memory.h:60

dbus_malloc

void \* dbus_malloc(size_t bytes)

Allocates the given number of bytes, as with standard malloc().

**Definition** dbus-memory.c:470

DBUS_ERROR_TIMEOUT

\#define DBUS_ERROR_TIMEOUT

Certain timeout errors, possibly ETIMEDOUT on a socket.

**Definition** dbus-protocol.h:389

DBUS_ERROR_NOT_SUPPORTED

\#define DBUS_ERROR_NOT_SUPPORTED

Requested operation isn't supported (like ENOSYS on UNIX).

**Definition** dbus-protocol.h:375

DBUS_ERROR_BAD_ADDRESS

\#define DBUS_ERROR_BAD_ADDRESS

A D-Bus bus address was malformed.

**Definition** dbus-protocol.h:373

DBUS_ERROR_IO_ERROR

\#define DBUS_ERROR_IO_ERROR

Something went wrong reading or writing to a socket, for example.

**Definition** dbus-protocol.h:371

DBUS_ERROR_SPAWN_CHILD_EXITED

\#define DBUS_ERROR_SPAWN_CHILD_EXITED

While starting a new process, the child exited with a status code.

**Definition** dbus-protocol.h:426

DBUS_ERROR_ACCESS_DENIED

\#define DBUS_ERROR_ACCESS_DENIED

Security restrictions don't allow doing what you're trying to do.

**Definition** dbus-protocol.h:379

DBUS_ERROR_FILE_EXISTS

\#define DBUS_ERROR_FILE_EXISTS

Existing file and the operation you're using does not silently overwrite.

**Definition** dbus-protocol.h:401

DBUS_ERROR_LIMITS_EXCEEDED

\#define DBUS_ERROR_LIMITS_EXCEEDED

Some limited resource is exhausted.

**Definition** dbus-protocol.h:377

DBUS_ERROR_FAILED

\#define DBUS_ERROR_FAILED

A generic error; "something went wrong" - see the error message for more.

**Definition** dbus-protocol.h:361

DBUS_ERROR_NO_MEMORY

\#define DBUS_ERROR_NO_MEMORY

There was not enough memory to complete an operation.

**Definition** dbus-protocol.h:363

DBUS_ERROR_INVALID_ARGS

\#define DBUS_ERROR_INVALID_ARGS

Invalid arguments passed to a method call.

**Definition** dbus-protocol.h:397

DBUS_ERROR_FILE_NOT_FOUND

\#define DBUS_ERROR_FILE_NOT_FOUND

Missing file.

**Definition** dbus-protocol.h:399

\_dbus_sha_compute

dbus_bool_t \_dbus_sha_compute(const DBusString \*data, DBusString \*ascii_output)

Computes the ASCII hex-encoded shasum of the given data and appends it to the output string.

**Definition** dbus-sha.c:484

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

\_dbus_string_copy

dbus_bool_t \_dbus_string_copy(const DBusString \*source, int start, DBusString \*dest, int insert_at)

Like \_dbus_string_move(), but does not delete the section of the source string that's copied to the d...

**Definition** dbus-string.c:1345

\_dbus_string_get_data_len

char \* \_dbus_string_get_data_len(DBusString \*str, int start, int len)

Gets a sub-portion of the raw character buffer from the string.

**Definition** dbus-string.c:535

\_dbus_string_validate_utf8

dbus_bool_t \_dbus_string_validate_utf8(const DBusString \*str, int start, int len)

Checks that the given range of the string is valid UTF-8.

**Definition** dbus-string.c:2678

\_dbus_string_init_const_len

void \_dbus_string_init_const_len(DBusString \*str, const char \*value, int len)

Initializes a constant string with a length.

**Definition** dbus-string.c:217

\_dbus_string_tolower_ascii

void \_dbus_string_tolower_ascii(const DBusString \*str, int start, int len)

Converts the given range of the string to lower case.

**Definition** dbus-string.c:2608

\_dbus_string_get_data

char \* \_dbus_string_get_data(DBusString \*str)

Gets the raw character buffer from the string.

**Definition** dbus-string.c:496

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_string_shorten

void \_dbus_string_shorten(DBusString \*str, int length_to_remove)

Makes a string shorter by the given number of bytes.

**Definition** dbus-string.c:825

\_dbus_string_append_printf_valist

dbus_bool_t \_dbus_string_append_printf_valist(DBusString \*str, const char \*format, va_list args)

Appends a printf-style formatted string to the DBusString.

**Definition** dbus-string.c:1105

\_dbus_string_lengthen

dbus_bool_t \_dbus_string_lengthen(DBusString \*str, int additional_length)

Makes a string longer by the given number of bytes.

**Definition** dbus-string.c:805

\_dbus_string_get_length

int \_dbus_string_get_length(const DBusString \*str)

Gets the length of a string (not including nul termination).

**Definition** dbus-string.c:784

\_dbus_string_append_byte

dbus_bool_t \_dbus_string_append_byte(DBusString \*str, unsigned char byte)

Appends a single byte to the string, returning FALSE if not enough memory.

**Definition** dbus-string.c:1190

\_dbus_string_append_printf

dbus_bool_t \_dbus_string_append_printf(DBusString \*str, const char \*format,...)

Appends a printf-style formatted string to the DBusString.

**Definition** dbus-string.c:1147

\_dbus_string_get_const_data_len

const char \* \_dbus_string_get_const_data_len(const DBusString \*str, int start, int len)

const version of \_dbus_string_get_data_len().

**Definition** dbus-string.c:559

\_dbus_string_get_const_data

const char \* \_dbus_string_get_const_data(const DBusString \*str)

Gets the raw character buffer from a const string.

**Definition** dbus-string.c:513

\_dbus_string_get_byte

unsigned char \_dbus_string_get_byte(const DBusString \*str, int start)

Gets the byte at the given position.

**Definition** dbus-string.c:607

\_dbus_logv

void \_dbus_logv(DBusSystemLogSeverity severity, const char \*msg, va_list args)

Log a message to the system log file (e.g.

**Definition** dbus-sysdeps-win.c:4053

\_dbus_get_monotonic_time

void \_dbus_get_monotonic_time(dbus_int64_t \*tv_sec, long \*tv_usec)

Get current time, as in gettimeofday().

**Definition** dbus-sysdeps-win.c:2470

\_dbus_read_local_machine_uuid

dbus_bool_t \_dbus_read_local_machine_uuid(DBusGUID \*machine_id, dbus_bool_t create_if_not_found, DBusError \*error)

Reads the uuid of the machine we're running on from the dbus configuration.

**Definition** dbus-sysdeps-win.c:2678

\_DBUS_POLLOUT

\#define \_DBUS_POLLOUT

Writing now will not block.

**Definition** dbus-sysdeps.h:448

dbus_uid_t

unsigned long dbus_uid_t

A user ID.

**Definition** dbus-sysdeps.h:141

\_dbus_get_is_errno_eagain_or_ewouldblock

dbus_bool_t \_dbus_get_is_errno_eagain_or_ewouldblock(int e)

See if errno is EAGAIN or EWOULDBLOCK (this has to be done differently for Winsock so is abstracted)

**Definition** dbus-sysdeps-win.c:3564

\_dbus_pid_for_log

unsigned long \_dbus_pid_for_log(void)

The only reason this is separate from \_dbus_getpid() is to allow it on Windows for logging but not fo...

**Definition** dbus-sysdeps-win.c:945

dbus_pid_t

unsigned long dbus_pid_t

A process ID.

**Definition** dbus-sysdeps.h:139

\_dbus_read_socket

int \_dbus_read_socket(DBusSocket fd, DBusString \*buffer, int count)

Socket interface.

**Definition** dbus-sysdeps-win.c:383

\_dbus_exit

void \_dbus_exit(int code)

Exit the process, returning the given value.

**Definition** dbus-sysdeps-win.c:1561

\_DBUS_POLLERR

\#define \_DBUS_POLLERR

Error condition.

**Definition** dbus-sysdeps.h:450

\_dbus_write_socket

int \_dbus_write_socket(DBusSocket fd, const DBusString \*buffer, int start, int len)

Thin wrapper around the write() system call that writes a part of a DBusString and handles EINTR for ...

**Definition** dbus-sysdeps-win.c:453

\_dbus_atomic_set_nonzero

void \_dbus_atomic_set_nonzero(DBusAtomic \*atomic)

Atomically set the value of an integer to something nonzero.

**Definition** dbus-sysdeps-win.c:3535

\_dbus_socketpair

dbus_bool_t \_dbus_socketpair(DBusSocket \*fd1, DBusSocket \*fd2, dbus_bool_t blocking, DBusError \*error)

Creates pair of connect sockets (as in socketpair()).

**Definition** dbus-sysdeps-win.c:1062

\_dbus_append_keyring_directory_for_credentials

dbus_bool_t \_dbus_append_keyring_directory_for_credentials(DBusString \*directory, DBusCredentials \*credentials)

Appends the directory in which a keyring for the given credentials should be stored.

**Definition** dbus-sysdeps-win.c:3679

DBUS_UID_UNSET

\#define DBUS_UID_UNSET

an invalid UID used to represent an uninitialized dbus_uid_t field

**Definition** dbus-sysdeps.h:148

\_dbus_atomic_dec

dbus_int32_t \_dbus_atomic_dec(DBusAtomic \*atomic)

Atomically decrement an integer.

**Definition** dbus-sysdeps-win.c:3472

\_dbus_read_credentials_socket

dbus_bool_t \_dbus_read_credentials_socket(DBusSocket handle, DBusCredentials \*credentials, DBusError \*error)

Reads a single byte which must be nul (an error occurs otherwise), and reads unix credentials if avai...

**Definition** dbus-sysdeps-win.c:2189

\_dbus_getenv

const char \* \_dbus_getenv(const char \*varname)

Wrapper for getenv().

**Definition** dbus-sysdeps.c:197

\_dbus_listen_unix_socket

DBusSocket \_dbus_listen_unix_socket(const char \*path, dbus_bool_t abstract, DBusError \*error)

Creates a socket and binds it to the given path, then listens on the socket.

**Definition** dbus-sysdeps-win.c:4438

\_dbus_getpid

dbus_pid_t \_dbus_getpid(void)

Gets our process ID.

**Definition** dbus-sysdeps-win.c:2395

\_dbus_atomic_get

dbus_int32_t \_dbus_atomic_get(DBusAtomic \*atomic)

Atomically get the value of an integer.

**Definition** dbus-sysdeps-win.c:3491

\_dbus_set_socket_nonblocking

dbus_bool_t \_dbus_set_socket_nonblocking(DBusSocket handle, DBusError \*error)

Sets a file descriptor to be nonblocking.

**Definition** dbus-sysdeps-win.c:549

\_dbus_lookup_session_address

dbus_bool_t \_dbus_lookup_session_address(dbus_bool_t \*supported, DBusString \*address, DBusError \*error)

Determines the address of the session bus by querying a platform-specific method.

**Definition** dbus-sysdeps-win.c:3656

\_dbus_credentials_add_from_user

dbus_bool_t \_dbus_credentials_add_from_user(DBusCredentials \*credentials, const DBusString \*username, DBusCredentialsAddFlags flags, DBusError \*error)

Adds the credentials corresponding to the given username.

**Definition** dbus-sysdeps-win.c:2314

\_dbus_connect_tcp_socket

DBusSocket \_dbus_connect_tcp_socket(const char \*host, const char \*port, const char \*family, DBusError \*error)

Creates a socket and connects to a socket at the given host and port.

**Definition** dbus-sysdeps-win.c:1578

\_dbus_disable_sigpipe

void \_dbus_disable_sigpipe(void)

signal (SIGPIPE, SIG_IGN);

**Definition** dbus-sysdeps-win.c:2481

\_dbus_check_setuid

dbus_bool_t \_dbus_check_setuid(void)

NOTE: If you modify this function, please also consider making the corresponding change in GLib.

**Definition** dbus-sysdeps-win.c:4003

\_dbus_sleep_milliseconds

void \_dbus_sleep_milliseconds(int milliseconds)

Sleeps the given number of milliseconds.

**Definition** dbus-sysdeps-win.c:2425

\_dbus_check_dir_is_private_to_user

dbus_bool_t \_dbus_check_dir_is_private_to_user(DBusString \*dir, DBusError \*error)

Checks to make sure the given directory is private to the user.

**Definition** dbus-sysdeps-win.c:2253

\_dbus_daemon_unpublish_session_bus_address

dbus_bool_t \_dbus_daemon_unpublish_session_bus_address(void)

Clear the platform-specific centralized location where the session bus address is published.

**Definition** dbus-sysdeps-win.c:3112

\_DBUS_POLLIN

\#define \_DBUS_POLLIN

There is data to read.

**Definition** dbus-sysdeps.h:444

\_dbus_listen_tcp_socket

int \_dbus_listen_tcp_socket(const char \*host, const char \*port, const char \*family, DBusString \*retport, const char \*\*retfamily, DBusSocket \*\*fds_p, DBusError \*error)

Creates a socket and binds it to the given path, then listens on the socket.

**Definition** dbus-sysdeps-win.c:1750

\_dbus_send_credentials_socket

dbus_bool_t \_dbus_send_credentials_socket(DBusSocket handle, DBusError \*error)

Sends a single nul byte with our UNIX credentials as ancillary data.

**Definition** dbus-sysdeps-win.c:2062

\_dbus_getuid

dbus_uid_t \_dbus_getuid(void)

Gets our Unix UID.

**Definition** dbus-sysdeps-win.c:2404

\_dbus_credentials_add_from_current_process

dbus_bool_t \_dbus_credentials_add_from_current_process(DBusCredentials \*credentials)

Adds the credentials of the current process to the passed-in credentials object.

**Definition** dbus-sysdeps-win.c:2338

\_dbus_close_socket

dbus_bool_t \_dbus_close_socket(DBusSocket \*fd, DBusError \*error)

Closes a socket and invalidates it.

**Definition** dbus-sysdeps-win.c:497

\_dbus_connect_unix_socket

DBusSocket \_dbus_connect_unix_socket(const char \*path, dbus_bool_t abstract, DBusError \*error)

Creates a socket and connects it to the UNIX domain socket at the given path.

**Definition** dbus-sysdeps-win.c:4358

\_dbus_atomic_set_zero

void \_dbus_atomic_set_zero(DBusAtomic \*atomic)

Atomically set the value of an integer to 0.

**Definition** dbus-sysdeps-win.c:3519

\_dbus_atomic_inc

dbus_int32_t \_dbus_atomic_inc(DBusAtomic \*atomic)

Atomically increments an integer.

**Definition** dbus-sysdeps-win.c:3453

\_dbus_generate_random_bytes

dbus_bool_t \_dbus_generate_random_bytes(DBusString \*str, int n_bytes, DBusError \*error)

Generates the given number of random bytes, using the best mechanism we can come up with.

**Definition** dbus-sysdeps-win.c:2557

\_dbus_printf_string_upper_bound

int \_dbus_printf_string_upper_bound(const char \*format, va_list args)

Measure the message length without terminating nul.

**Definition** dbus-sysdeps-win.c:738

\_dbus_delete_directory

dbus_bool_t \_dbus_delete_directory(const DBusString \*filename, DBusError \*error)

Removes a directory; Directory must be empty.

**Definition** dbus-sysdeps-win.c:3963

\_dbus_abort

void \_dbus_abort(void)

Aborts the program with SIGABRT (dumping core).

**Definition** dbus-sysdeps.c:89

\_dbus_poll

int \_dbus_poll(DBusPollFD \*fds, int n_fds, int timeout_milliseconds)

Wrapper for poll().

**Definition** dbus-sysdeps-win.c:1513

\_dbus_get_autolaunch_address

dbus_bool_t \_dbus_get_autolaunch_address(const char \*scope, DBusString \*address, DBusError \*error)

Returns the address of a new session bus.

**Definition** dbus-sysdeps-win.c:3238

\_dbus_write_socket_two

int \_dbus_write_socket_two(DBusSocket fd, const DBusString \*buffer1, int start1, int len1, const DBusString \*buffer2, int start2, int len2)

Like \_dbus_write() but will use writev() if possible to write both buffers in sequence.

**Definition** dbus-sysdeps-win.c:590

\_dbus_concat_dir_and_file

dbus_bool_t \_dbus_concat_dir_and_file(DBusString \*dir, const DBusString \*next_component)

Appends the given filename to the given directory.

**Definition** dbus-sysdeps-win.c:2272

\_dbus_get_real_time

void \_dbus_get_real_time(dbus_int64_t \*tv_sec, long \*tv_usec)

Get current time, as in gettimeofday().

**Definition** dbus-sysdeps-win.c:2439

\_dbus_init_system_log

void \_dbus_init_system_log(const char \*tag, DBusLogFlags flags)

Initialize the system log.

**Definition** dbus-sysdeps-win.c:4034

\_dbus_accept

DBusSocket \_dbus_accept(DBusSocket listen_fd)

Accepts a connection on a listening socket.

**Definition** dbus-sysdeps-win.c:2039

\_DBUS_MAX_SUN_PATH_LENGTH

\#define \_DBUS_MAX_SUN_PATH_LENGTH

Maximum length of the path to a UNIX domain socket, sockaddr_un::sun_path member.

**Definition** dbus-sysdeps.h:765

\_dbus_append_user_from_current_process

dbus_bool_t \_dbus_append_user_from_current_process(DBusString \*str)

Append to the string the identity we would like to have when we authenticate, on UNIX this is the cur...

**Definition** dbus-sysdeps-win.c:2376

\_dbus_flush_caches

void \_dbus_flush_caches(void)

Called when the bus daemon is signaled to reload its configuration; any caches should be nuked.

**Definition** dbus-sysdeps-win.c:3553

\_dbus_get_tmpdir

const char \* \_dbus_get_tmpdir(void)

Gets the temporary files directory, using GetTempPath()

**Definition** dbus-sysdeps-win.c:2599

\_dbus_ensure_directory

dbus_bool_t \_dbus_ensure_directory(const DBusString \*filename, DBusError \*error)

Creates a directory; succeeds if the directory is created or already existed.

**Definition** dbus-sysdeps-win.c:2523

\_dbus_path_is_absolute

dbus_bool_t \_dbus_path_is_absolute(const DBusString \*filename)

Checks whether the filename is an absolute path.

**Definition** dbus-sysdeps-win.c:3992

\_dbus_create_directory

dbus_bool_t \_dbus_create_directory(const DBusString \*filename, DBusError \*error)

Creates a directory.

**Definition** dbus-sysdeps-win.c:2494

DBUS_INT64_CONSTANT

\#define DBUS_INT64_CONSTANT(val)

Declare a 64-bit signed integer constant.

**Definition** dbus-arch-deps.h:41

DBusAtomic

An atomic integer safe to increment or decrement from multiple threads.

**Definition** dbus-sysdeps.h:340

DBusAtomic::value

volatile dbus_int32_t value

Value of the atomic integer.

**Definition** dbus-sysdeps.h:346

DBusCredentials

**Definition** dbus-credentials.c:60

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusError::message

const char \* message

public error message field

**Definition** dbus-errors.h:53

DBusList

A node in a linked list.

**Definition** dbus-list.h:37

DBusPollFD

**Definition** dbus-sysdeps.h:437

DBusPollFD::events

short events

Events to poll for.

**Definition** dbus-sysdeps.h:439

DBusPollFD::revents

short revents

Events that occurred.

**Definition** dbus-sysdeps.h:440

DBusPollFD::fd

DBusPollable fd

File descriptor.

**Definition** dbus-sysdeps.h:438

DBusRMutex

**Definition** dbus-sysdeps-pthread.c:51

DBusSocket

Socket interface.

**Definition** dbus-sysdeps.h:185

DBusString

**Definition** dbus-string.h:47

DBusGUID

A globally unique ID ; we have one for each DBusServer, and also one for each machine with libdbus in...

**Definition** dbus-internals.h:458

DBusGUID::as_uint32s

dbus_uint32_t as_uint32s\[DBUS_UUID_LENGTH_WORDS\]

guid as four uint32 values

**Definition** dbus-internals.h:459
