dbus-sysdeps.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-sysdeps.c Wrappers around system/libc features shared between UNIX and Windows (internal to D-Bus implementation)

3 \*

4 \* Copyright (C) 2002, 2003, 2006 Red Hat, Inc.

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

28\#include "dbus-internals.h"

29\#include "dbus-sysdeps.h"

30\#include "dbus-threads.h"

31\#include "dbus-protocol.h"

32\#include "dbus-string.h"

33\#include "dbus-list.h"

34\#include "dbus-misc.h"

35

36/\* NOTE: If you include any unix/windows-specific headers here, you are probably doing something

37 \* wrong and should be putting some code in dbus-sysdeps-unix.c or dbus-sysdeps-win.c.

38 \*

39 \* These are the standard ANSI C headers...

40 \*/

41\#if HAVE_LOCALE_H

42\#include \<locale.h\>

43\#endif

44\#include \<stdlib.h\>

45\#include \<string.h\>

46\#include \<stdio.h\>

47

48\#ifdef HAVE_ERRNO_H

49\#include \<errno.h\>

50\#endif

51

52\#ifdef DBUS_WIN

53 \#include \<stdlib.h\>

54\#elif (defined \_\_APPLE\_\_)

55\# include \<crt_externs.h\>

56\# define environ (\*\_NSGetEnviron())

57\#elif HAVE_DECL_ENVIRON && defined(HAVE_UNISTD_H)

58\# include \<unistd.h\>

59\#else

60extern char \*\*environ;

61\#endif

62

63\#ifdef DBUS_WIN

64\#include "dbus-sockets-win.h"

65\#else

66\#include \<arpa/inet.h\>

67\#include \<netinet/in.h\>

68\#include \<sys/socket.h\>

69\#endif

70

88void

89\_dbus_abort (void)

90{

91 const char \*s;

92

93 \_dbus_print_backtrace ();

94

95 s = \_dbus_getenv ("DBUS_BLOCK_ON_ABORT");

96 if (s && \*s)

97 {

98 /\* don't use \_dbus_warn here since it can \_dbus_abort() \*/

99 fprintf (stderr, " Process %lu sleeping for gdb attach\n", \_dbus_pid_for_log ());

100 \_dbus_sleep_milliseconds (1000 \* 180);

101 }

102

103 abort ();

104 \_dbus_exit (1); /\* in case someone manages to ignore SIGABRT ? \*/

105}

106

125dbus_bool_t

126dbus_setenv (const char \*varname,

127 const char \*value)

128{

129 \_dbus_assert (varname != NULL);

130

131 if (value == NULL)

132 {

133\#ifdef HAVE_UNSETENV

134 unsetenv (varname);

135 return TRUE;

136\#else

137 char \*putenv_value;

138 size_t len;

139

140 len = strlen (varname);

141

142 /\* Use system malloc to avoid memleaks that dbus_malloc

143 \* will get upset about.

144 \*/

145

146 putenv_value = malloc (len + 2);

147 if (putenv_value == NULL)

148 return FALSE;

149

150 strcpy (putenv_value, varname);

151\#if defined(DBUS_WIN)

152 strcat (putenv_value, "=");

153\#endif

154

155 return (putenv (putenv_value) == 0);

156\#endif

157 }

158 else

159 {

160\#ifdef HAVE_SETENV

161 return (setenv (varname, value, TRUE) == 0);

162\#else

163 char \*putenv_value;

164 size_t len;

165 size_t varname_len;

166 size_t value_len;

167

168 varname_len = strlen (varname);

169 value_len = strlen (value);

170

171 len = varname_len + value_len + 1 /\* '=' \*/ ;

172

173 /\* Use system malloc to avoid memleaks that dbus_malloc

174 \* will get upset about.

175 \*/

176

177 putenv_value = malloc (len + 1);

178 if (putenv_value == NULL)

179 return FALSE;

180

181 strcpy (putenv_value, varname);

182 strcpy (putenv_value + varname_len, "=");

183 strcpy (putenv_value + varname_len + 1, value);

184

185 return (putenv (putenv_value) == 0);

186\#endif

187 }

188}

189

196const char\*

197\_dbus_getenv (const char \*varname)

198{

199 /\* Don't respect any environment variables if the current process is

200 \* setuid. This is the equivalent of glibc's \_\_secure_getenv().

201 \*/

202 if (\_dbus_check_setuid ())

203 return NULL;

204 return getenv (varname);

205}

206

212dbus_bool_t

213\_dbus_clearenv (void)

214{

215 dbus_bool_t rc = TRUE;

216

217\#ifdef HAVE_CLEARENV

218 if (clearenv () != 0)

219 rc = FALSE;

220\#else

221

222 if (environ != NULL)

223 environ\[0\] = NULL;

224\#endif

225

226 return rc;

227}

228

237dbus_bool_t

238\_dbus_split_paths_and_append (DBusString \*dirs,

239 const char \*suffix,

240 DBusList \*\*dir_list)

241{

242 int start;

243 int i;

244 int len;

245 char \*cpath;

246 DBusString file_suffix;

247

248 start = 0;

249 i = 0;

250

251 \_dbus_string_init_const (&file_suffix, suffix);

252

253 len = \_dbus_string_get_length (dirs);

254

255 while (\_dbus_string_find (dirs, start, \_DBUS_PATH_SEPARATOR, &i))

256 {

257 DBusString path;

258

259 if (!\_dbus_string_init (&path))

260 goto oom;

261

262 if (!\_dbus_string_copy_len (dirs,

263 start,

264 i - start,

265 &path,

266 0))

267 {

268 \_dbus_string_free (&path);

269 goto oom;

270 }

271

272 \_dbus_string_chop_white (&path);

273

274 /\* check for an empty path \*/

275 if (\_dbus_string_get_length (&path) == 0)

276 goto next;

277

278 if (!\_dbus_concat_dir_and_file (&path,

279 &file_suffix))

280 {

281 \_dbus_string_free (&path);

282 goto oom;

283 }

284

285 if (!\_dbus_string_copy_data(&path, &cpath))

286 {

287 \_dbus_string_free (&path);

288 goto oom;

289 }

290

291 if (!\_dbus_list_append (dir_list, cpath))

292 {

293 \_dbus_string_free (&path);

294 dbus_free (cpath);

295 goto oom;

296 }

297

298 next:

299 \_dbus_string_free (&path);

300 start = i + 1;

301 }

302

303 if (start != len)

304 {

305 DBusString path;

306

307 if (!\_dbus_string_init (&path))

308 goto oom;

309

310 if (!\_dbus_string_copy_len (dirs,

311 start,

312 len - start,

313 &path,

314 0))

315 {

316 \_dbus_string_free (&path);

317 goto oom;

318 }

319

320 if (!\_dbus_concat_dir_and_file (&path,

321 &file_suffix))

322 {

323 \_dbus_string_free (&path);

324 goto oom;

325 }

326

327 if (!\_dbus_string_copy_data(&path, &cpath))

328 {

329 \_dbus_string_free (&path);

330 goto oom;

331 }

332

333 if (!\_dbus_list_append (dir_list, cpath))

334 {

335 \_dbus_string_free (&path);

336 dbus_free (cpath);

337 goto oom;

338 }

339

340 \_dbus_string_free (&path);

341 }

342

343 return TRUE;

344

345 oom:

346 \_dbus_list_clear_full (dir_list, dbus_free);

347 return FALSE;

348}

349

370dbus_bool_t

371\_dbus_string_parse_int (const DBusString \*str,

372 int start,

373 long \*value_return,

374 int \*end_return)

375{

376 long v;

377 const char \*p;

378 char \*end;

379

380 p = \_dbus_string_get_const_data_len (str, start,

381 \_dbus_string_get_length (str) - start);

382

383 end = NULL;

384 \_dbus_set_errno_to_zero ();

385 v = strtol (p, &end, 0);

386 if (end == NULL \|\| end == p \|\| errno != 0)

387 return FALSE;

388

389 if (value_return)

390 \*value_return = v;

391 if (end_return)

392 \*end_return = start + (end - p);

393

394 return TRUE;

395}

396

409dbus_bool_t

410\_dbus_string_parse_uint (const DBusString \*str,

411 int start,

412 unsigned long \*value_return,

413 int \*end_return)

414{

415 unsigned long v;

416 const char \*p;

417 char \*end;

418

419 p = \_dbus_string_get_const_data_len (str, start,

420 \_dbus_string_get_length (str) - start);

421

422 end = NULL;

423 \_dbus_set_errno_to_zero ();

424 v = strtoul (p, &end, 0);

425 if (end == NULL \|\| end == p \|\| errno != 0)

426 return FALSE;

427

428 if (value_return)

429 \*value_return = v;

430 if (end_return)

431 \*end_return = start + (end - p);

432

433 return TRUE;

434}

435

448dbus_bool_t

449\_dbus_string_parse_int64 (const DBusString \*str,

450 int start,

451 dbus_int64_t \*value_return,

452 int \*end_return)

453{

454 dbus_int64_t v;

455 const char \*p;

456 char \*end;

457

458 p = \_dbus_string_get_const_data_len (str, start,

459 \_dbus_string_get_length (str) - start);

460

461 end = NULL;

462 \_dbus_set_errno_to_zero ();

463 v = strtoll (p, &end, 0);

464 if (end == NULL \|\| end == p \|\| errno != 0)

465 return FALSE;

466

467 if (value_return)

468 \*value_return = v;

469 if (end_return)

470 \*end_return = start + (end - p);

471

472 return TRUE;

473}

474

/\* DBusString group \*/

476

490dbus_bool_t

491\_dbus_generate_random_bytes_buffer (char \*buffer,

492 int n_bytes,

493 DBusError \*error)

494{

495 DBusString str;

496

497 if (!\_dbus_string_init (&str))

498 {

499 \_DBUS_SET_OOM (error);

500 return FALSE;

501 }

502

503 if (!\_dbus_generate_random_bytes (&str, n_bytes, error))

504 {

505 \_dbus_string_free (&str);

506 return FALSE;

507 }

508

509 \_dbus_string_copy_to_buffer (&str, buffer, n_bytes);

510

511 \_dbus_string_free (&str);

512 return TRUE;

513}

514

524dbus_bool_t

525\_dbus_generate_random_ascii (DBusString \*str,

526 int n_bytes,

527 DBusError \*error)

528{

529 static const char letters\[\] =

530 "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz";

531 int i;

532 int len;

533

534 if (!\_dbus_generate_random_bytes (str, n_bytes, error))

535 return FALSE;

536

537 len = \_dbus_string_get_length (str);

538 i = len - n_bytes;

539 while (i \< len)

540 {

541 \_dbus_string_set_byte (str, i,

542 letters\[\_dbus_string_get_byte (str, i) %

543 (sizeof (letters) - 1)\]);

544

545 ++i;

546 }

547

548 \_dbus_assert (\_dbus_string_validate_ascii (str, len - n_bytes,

549 n_bytes));

550

551 return TRUE;

552}

553

564const char\*

565\_dbus_error_from_errno (int error_number)

566{

567 switch (error_number)

568 {

569 case 0:

570 return DBUS_ERROR_FAILED;

571

572\#ifdef EPROTONOSUPPORT

573 case EPROTONOSUPPORT:

574 return DBUS_ERROR_NOT_SUPPORTED;

575\#elif defined(WSAEPROTONOSUPPORT)

576 case WSAEPROTONOSUPPORT:

577 return DBUS_ERROR_NOT_SUPPORTED;

578\#endif

579\#ifdef EAFNOSUPPORT

580 case EAFNOSUPPORT:

581 return DBUS_ERROR_NOT_SUPPORTED;

582\#elif defined(WSAEAFNOSUPPORT)

583 case WSAEAFNOSUPPORT:

584 return DBUS_ERROR_NOT_SUPPORTED;

585\#endif

586\#ifdef ENFILE

587 case ENFILE:

588 return DBUS_ERROR_LIMITS_EXCEEDED; /\* kernel out of memory \*/

589\#endif

590\#ifdef EMFILE

591 case EMFILE:

592 return DBUS_ERROR_LIMITS_EXCEEDED;

593\#endif

594\#ifdef EACCES

595 case EACCES:

596 return DBUS_ERROR_ACCESS_DENIED;

597\#endif

598\#ifdef EPERM

599 case EPERM:

600 return DBUS_ERROR_ACCESS_DENIED;

601\#endif

602\#ifdef ENOBUFS

603 case ENOBUFS:

604 return DBUS_ERROR_NO_MEMORY;

605\#endif

606\#ifdef ENOMEM

607 case ENOMEM:

608 return DBUS_ERROR_NO_MEMORY;

609\#endif

610\#ifdef ECONNREFUSED

611 case ECONNREFUSED:

612 return DBUS_ERROR_NO_SERVER;

613\#elif defined(WSAECONNREFUSED)

614 case WSAECONNREFUSED:

615 return DBUS_ERROR_NO_SERVER;

616\#endif

617\#ifdef ETIMEDOUT

618 case ETIMEDOUT:

619 return DBUS_ERROR_TIMEOUT;

620\#elif defined(WSAETIMEDOUT)

621 case WSAETIMEDOUT:

622 return DBUS_ERROR_TIMEOUT;

623\#endif

624\#ifdef ENETUNREACH

625 case ENETUNREACH:

626 return DBUS_ERROR_NO_NETWORK;

627\#elif defined(WSAENETUNREACH)

628 case WSAENETUNREACH:

629 return DBUS_ERROR_NO_NETWORK;

630\#endif

631\#ifdef EADDRINUSE

632 case EADDRINUSE:

633 return DBUS_ERROR_ADDRESS_IN_USE;

634\#elif defined(WSAEADDRINUSE)

635 case WSAEADDRINUSE:

636 return DBUS_ERROR_ADDRESS_IN_USE;

637\#endif

638\#ifdef EEXIST

639 case EEXIST:

640 return DBUS_ERROR_FILE_EXISTS;

641\#endif

642\#ifdef ENOENT

643 case ENOENT:

644 return DBUS_ERROR_FILE_NOT_FOUND;

645\#endif

646 default:

647 return DBUS_ERROR_FAILED;

648 }

649}

650

656const char\*

657\_dbus_error_from_system_errno (void)

658{

659 return \_dbus_error_from_errno (errno);

660}

661

665void

666\_dbus_set_errno_to_zero (void)

667{

668\#ifdef DBUS_WINCE

669 SetLastError (0);

670\#else

671 errno = 0;

672\#endif

673}

674

679dbus_bool_t

680\_dbus_get_is_errno_enomem (int e)

681{

682 return e == ENOMEM;

683}

684

689dbus_bool_t

690\_dbus_get_is_errno_eintr (int e)

691{

692 return e == EINTR;

693}

694

699dbus_bool_t

700\_dbus_get_is_errno_epipe (int e)

701{

702 return e == EPIPE;

703}

704

709dbus_bool_t

710\_dbus_get_is_errno_etoomanyrefs (int e)

711{

712\#ifdef ETOOMANYREFS

713 return e == ETOOMANYREFS;

714\#else

715 return FALSE;

716\#endif

717}

718

723const char\*

724\_dbus_strerror_from_errno (void)

725{

726 return \_dbus_strerror (errno);

727}

728

735void

736\_dbus_log (DBusSystemLogSeverity severity,

737 const char \*msg,

738 ...)

739{

740 va_list args;

741

742 va_start (args, msg);

743

744 \_dbus_logv (severity, msg, args);

745

746 va_end (args);

747}

748

749/\*

750 \* Try to convert the IPv4 or IPv6 address pointed to by

751 \* sockaddr_pointer into a string.

752 \*

753 \* @param sockaddr_pointer A struct sockaddr_in or struct sockaddr_in6

754 \* @param len The length of the struct pointed to by sockaddr_pointer

755 \* @param string An array to write the address into

756 \* @param string_len Length of string (should usually be at least INET6_ADDRSTRLEN)

757 \* @param family_name Used to return "ipv4" or "ipv6", or NULL to ignore

758 \* @param port Used to return the port number, or NULL to ignore

759 \* @returns \#FALSE with errno set if the address family was not understood

760 \*/

761dbus_bool_t

762\_dbus_inet_sockaddr_to_string (const void \*sockaddr_pointer,

763 size_t len,

764 char \*string,

765 size_t string_len,

766 const char \*\*family_name,

767 dbus_uint16_t \*port,

768 DBusError \*error)

769{

770 union

771 {

772 struct sockaddr sa;

773 struct sockaddr_storage storage;

774 struct sockaddr_in ipv4;

775 struct sockaddr_in6 ipv6;

776 } addr;

777 int saved_errno;

778

779 if (len \> sizeof (addr))

780 return FALSE;

781

782 \_DBUS_ZERO (addr);

783 memcpy (&addr, sockaddr_pointer, len);

784

785 switch (addr.sa.sa_family)

786 {

787 case AF_INET:

788 if (inet_ntop (AF_INET, &addr.ipv4.sin_addr, string, string_len) != NULL)

789 {

790 if (family_name != NULL)

791 \*family_name = "ipv4";

792

793 if (port != NULL)

794 \*port = ntohs (addr.ipv4.sin_port);

795

796 return TRUE;

797 }

798 else

799 {

800 saved_errno = \_dbus_get_low_level_socket_errno ();

801 dbus_set_error (error, \_dbus_error_from_errno (saved_errno),

802 "Failed to get identity of IPv4 socket: %s",

803 \_dbus_strerror (saved_errno));

804 }

805

806 return FALSE;

807

808\#ifdef AF_INET6

809 case AF_INET6:

810 if (inet_ntop (AF_INET6, &addr.ipv6.sin6_addr, string, string_len) != NULL)

811 {

812 if (family_name != NULL)

813 \*family_name = "ipv6";

814

815 if (port != NULL)

816 \*port = ntohs (addr.ipv6.sin6_port);

817

818 return TRUE;

819 }

820 else

821 {

822 saved_errno = \_dbus_get_low_level_socket_errno ();

823 dbus_set_error (error, \_dbus_error_from_errno (saved_errno),

824 "Failed to get identity of IPv6 socket: %s",

825 \_dbus_strerror (saved_errno));

826 }

827

828 return FALSE;

829\#endif

830

831 default:

832 dbus_set_error (error, DBUS_ERROR_FAILED,

833 "Failed to get identity of socket: unknown family");

834 return FALSE;

835 }

836}

837

838/\*

839 \* Format an error appropriate for saved_errno for the IPv4 or IPv6

840 \* address pointed to by sockaddr_pointer of length sockaddr_len.

841 \*

842 \* @param error The error to set

843 \* @param sockaddr_pointer A struct sockaddr_in or struct sockaddr_in6

844 \* @param len The length of the struct pointed to by sockaddr_pointer

845 \* @param description A prefix like "Failed to listen on socket"

846 \* @param saved_errno The OS-level error number to use

847 \*/

848void

849\_dbus_set_error_with_inet_sockaddr (DBusError \*error,

850 const void \*sockaddr_pointer,

851 size_t len,

852 const char \*description,

853 int saved_errno)

854{

855 char string\[INET6_ADDRSTRLEN\];

856 dbus_uint16_t port;

857 const struct sockaddr \*addr = sockaddr_pointer;

858

859 if (\_dbus_inet_sockaddr_to_string (sockaddr_pointer, len,

860 string, sizeof (string), NULL, &port,

861 NULL))

862 {

863 dbus_set_error (error, \_dbus_error_from_errno (saved_errno),

864 "%s \\%s\\ port %u: %s",

865 description, string, port, \_dbus_strerror (saved_errno));

866 }

867 else

868 {

869 dbus_set_error (error, \_dbus_error_from_errno (saved_errno),

870 "%s \<address of unknown family %d\>: %s",

871 description, addr-\>sa_family,

872 \_dbus_strerror (saved_errno));

873 }

874}

875

876void

877\_dbus_combine_tcp_errors (DBusList \*\*sources,

878 const char \*summary,

879 const char \*host,

880 const char \*port,

881 DBusError \*dest)

882{

883 DBusString message = \_DBUS_STRING_INIT_INVALID;

884

885 if (\_dbus_list_length_is_one (sources))

886 {

887 /\* If there was exactly one error, just use it \*/

888 dbus_move_error (\_dbus_list_get_first (sources), dest);

889 }

890 else

891 {

892 DBusList \*iter;

893 const char \*name = NULL;

894

895 /\* If there was more than one error, concatenate all the

896 \* errors' diagnostic messages, and use their common error

897 \* name, or DBUS_ERROR_FAILED if more than one name is

898 \* represented \*/

899 if (!\_dbus_string_init (&message))

900 {

901 \_DBUS_SET_OOM (dest);

902 goto out;

903 }

904

905 for (iter = \_dbus_list_get_first_link (sources);

906 iter != NULL;

907 iter = \_dbus_list_get_next_link (sources, iter))

908 {

909 DBusError \*error = iter-\>data;

910

911 if (name == NULL)

912 {

913 /\* no error names known yet, try to use this one \*/

914 name = error-\>name;

915 }

916 else if (strcmp (name, error-\>name) != 0)

917 {

918 /\* errors of two different names exist, reconcile by

919 \* using FAILED \*/

920 name = DBUS_ERROR_FAILED;

921 }

922

923 if ((\_dbus_string_get_length (&message) \> 0 &&

924 !\_dbus_string_append (&message, "; ")) \|\|

925 !\_dbus_string_append (&message, error-\>message))

926 {

927 \_DBUS_SET_OOM (dest);

928 goto out;

929 }

930 }

931

932 if (name == NULL)

933 name = DBUS_ERROR_FAILED;

934

935 dbus_set_error (dest, name, "%s to \\%s\\:%s (%s)",

936 summary, host ? host : "\*", port ? port : "0",

937 \_dbus_string_get_const_data (&message));

938 }

939

940out:

941 \_dbus_string_free (&message);

942}

943

946/\* tests in dbus-sysdeps-util.c \*/

dbus_move_error

void dbus_move_error(DBusError \*src, DBusError \*dest)

Moves an error src into dest, freeing src and overwriting dest.

**Definition** dbus-errors.c:281

dbus_set_error

void dbus_set_error(DBusError \*error, const char \*name, const char \*format,...)

Assigns an error name and message to a DBusError.

**Definition** dbus-errors.c:356

\_dbus_get_is_errno_epipe

dbus_bool_t \_dbus_get_is_errno_epipe(int e)

See if errno is EPIPE.

**Definition** dbus-sysdeps.c:700

\_dbus_get_is_errno_etoomanyrefs

dbus_bool_t \_dbus_get_is_errno_etoomanyrefs(int e)

See if errno is ETOOMANYREFS.

**Definition** dbus-sysdeps.c:710

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_dbus_log

void \_dbus_log(DBusSystemLogSeverity severity, const char \*msg,...)

Log a message to the system log file (e.g.

**Definition** dbus-sysdeps.c:736

\_dbus_error_from_errno

const char \* \_dbus_error_from_errno(int error_number)

Converts a UNIX errno, or Windows errno or WinSock error value into a DBusError name.

**Definition** dbus-sysdeps.c:565

\_dbus_generate_random_ascii

dbus_bool_t \_dbus_generate_random_ascii(DBusString \*str, int n_bytes, DBusError \*error)

Generates the given number of random bytes, where the bytes are chosen from the alphanumeric ASCII su...

**Definition** dbus-sysdeps.c:525

\_dbus_error_from_system_errno

const char \* \_dbus_error_from_system_errno(void)

Converts the current system errno value into a DBusError name.

**Definition** dbus-sysdeps.c:657

\_dbus_strerror_from_errno

const char \* \_dbus_strerror_from_errno(void)

Get error message from errno.

**Definition** dbus-sysdeps.c:724

\_dbus_get_is_errno_eintr

dbus_bool_t \_dbus_get_is_errno_eintr(int e)

See if errno is EINTR.

**Definition** dbus-sysdeps.c:690

\_DBUS_ZERO

\#define \_DBUS_ZERO(object)

Sets all bits in an object to zero.

**Definition** dbus-internals.h:194

\_dbus_set_errno_to_zero

void \_dbus_set_errno_to_zero(void)

Assign 0 to the global errno variable.

**Definition** dbus-sysdeps.c:666

\_dbus_get_is_errno_enomem

dbus_bool_t \_dbus_get_is_errno_enomem(int e)

See if errno is ENOMEM.

**Definition** dbus-sysdeps.c:680

\_dbus_generate_random_bytes_buffer

dbus_bool_t \_dbus_generate_random_bytes_buffer(char \*buffer, int n_bytes, DBusError \*error)

Fills n_bytes of the given buffer with random bytes.

**Definition** dbus-sysdeps.c:491

\_dbus_list_get_first_link

DBusList \* \_dbus_list_get_first_link(DBusList \*\*list)

Gets the first link in the list.

**Definition** dbus-list.c:597

\_dbus_list_length_is_one

dbus_bool_t \_dbus_list_length_is_one(DBusList \*\*list)

Check whether length is exactly one.

**Definition** dbus-list.c:813

\_dbus_list_clear_full

void \_dbus_list_clear_full(DBusList \*\*list, DBusFreeFunction function)

Free every link and every element in the list.

**Definition** dbus-list.c:570

\_dbus_list_get_first

void \* \_dbus_list_get_first(DBusList \*\*list)

Gets the first data in the list.

**Definition** dbus-list.c:642

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

dbus_setenv

dbus_bool_t dbus_setenv(const char \*varname, const char \*value)

Wrapper for setenv().

**Definition** dbus-sysdeps.c:126

DBUS_ERROR_TIMEOUT

\#define DBUS_ERROR_TIMEOUT

Certain timeout errors, possibly ETIMEDOUT on a socket.

**Definition** dbus-protocol.h:389

DBUS_ERROR_NOT_SUPPORTED

\#define DBUS_ERROR_NOT_SUPPORTED

Requested operation isn't supported (like ENOSYS on UNIX).

**Definition** dbus-protocol.h:375

DBUS_ERROR_ADDRESS_IN_USE

\#define DBUS_ERROR_ADDRESS_IN_USE

Can't bind a socket since its address is in use (i.e.

**Definition** dbus-protocol.h:393

DBUS_ERROR_ACCESS_DENIED

\#define DBUS_ERROR_ACCESS_DENIED

Security restrictions don't allow doing what you're trying to do.

**Definition** dbus-protocol.h:379

DBUS_ERROR_NO_SERVER

\#define DBUS_ERROR_NO_SERVER

Unable to connect to server (probably caused by ECONNREFUSED on a socket).

**Definition** dbus-protocol.h:383

DBUS_ERROR_FILE_EXISTS

\#define DBUS_ERROR_FILE_EXISTS

Existing file and the operation you're using does not silently overwrite.

**Definition** dbus-protocol.h:401

DBUS_ERROR_LIMITS_EXCEEDED

\#define DBUS_ERROR_LIMITS_EXCEEDED

Some limited resource is exhausted.

**Definition** dbus-protocol.h:377

DBUS_ERROR_NO_NETWORK

\#define DBUS_ERROR_NO_NETWORK

No network access (probably ENETUNREACH on a socket).

**Definition** dbus-protocol.h:391

DBUS_ERROR_FAILED

\#define DBUS_ERROR_FAILED

A generic error; "something went wrong" - see the error message for more.

**Definition** dbus-protocol.h:361

DBUS_ERROR_NO_MEMORY

\#define DBUS_ERROR_NO_MEMORY

There was not enough memory to complete an operation.

**Definition** dbus-protocol.h:363

DBUS_ERROR_FILE_NOT_FOUND

\#define DBUS_ERROR_FILE_NOT_FOUND

Missing file.

**Definition** dbus-protocol.h:399

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

\_dbus_string_parse_int64

dbus_bool_t \_dbus_string_parse_int64(const DBusString \*str, int start, dbus_int64_t \*value_return, int \*end_return)

Parses a dbus_int64_t integer contained in a DBusString.

**Definition** dbus-sysdeps.c:449

\_dbus_string_find

dbus_bool_t \_dbus_string_find(const DBusString \*str, int start, const char \*substr, int \*found)

Finds the given substring in the string, returning TRUE and filling in the byte index where the subst...

**Definition** dbus-string.c:1666

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_string_copy_data

dbus_bool_t \_dbus_string_copy_data(const DBusString \*str, char \*\*data_return)

Copies the data from the string into a char\*.

**Definition** dbus-string.c:717

\_dbus_string_parse_uint

dbus_bool_t \_dbus_string_parse_uint(const DBusString \*str, int start, unsigned long \*value_return, int \*end_return)

Parses an unsigned integer contained in a DBusString.

**Definition** dbus-sysdeps.c:410

\_dbus_string_parse_int

dbus_bool_t \_dbus_string_parse_int(const DBusString \*str, int start, long \*value_return, int \*end_return)

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

\_dbus_string_chop_white

void \_dbus_string_chop_white(DBusString \*str)

Deletes leading and trailing whitespace.

**Definition** dbus-string.c:2051

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

\_dbus_string_copy_len

dbus_bool_t \_dbus_string_copy_len(const DBusString \*source, int start, int len, DBusString \*dest, int insert_at)

Like \_dbus_string_copy(), but can copy a segment from the middle of the source string.

**Definition** dbus-string.c:1437

\_dbus_string_copy_to_buffer

void \_dbus_string_copy_to_buffer(const DBusString \*str, char \*buffer, int avail_len)

Copies the contents of a DBusString into a different buffer.

**Definition** dbus-string.c:742

\_dbus_logv

void \_dbus_logv(DBusSystemLogSeverity severity, const char \*msg, va_list args)

Log a message to the system log file (e.g.

**Definition** dbus-sysdeps-unix.c:5208

\_dbus_pid_for_log

unsigned long \_dbus_pid_for_log(void)

The only reason this is separate from \_dbus_getpid() is to allow it on Windows for logging but not fo...

**Definition** dbus-sysdeps-unix.c:3157

\_dbus_clearenv

dbus_bool_t \_dbus_clearenv(void)

Wrapper for clearenv().

**Definition** dbus-sysdeps.c:213

\_dbus_exit

void \_dbus_exit(int code)

Exit the process, returning the given value.

**Definition** dbus-sysdeps-unix.c:3641

\_dbus_getenv

const char \* \_dbus_getenv(const char \*varname)

Wrapper for getenv().

**Definition** dbus-sysdeps.c:197

\_dbus_check_setuid

dbus_bool_t \_dbus_check_setuid(void)

NOTE: If you modify this function, please also consider making the corresponding change in GLib.

**Definition** dbus-sysdeps-unix.c:5002

\_dbus_sleep_milliseconds

void \_dbus_sleep_milliseconds(int milliseconds)

Sleeps the given number of milliseconds.

**Definition** dbus-sysdeps-unix.c:3542

\_dbus_generate_random_bytes

dbus_bool_t \_dbus_generate_random_bytes(DBusString \*str, int n_bytes, DBusError \*error)

Generates the given number of securely random bytes, using the best mechanism we can come up with.

**Definition** dbus-sysdeps-unix.c:3572

\_dbus_abort

void \_dbus_abort(void)

Aborts the program with SIGABRT (dumping core).

**Definition** dbus-sysdeps.c:89

\_dbus_concat_dir_and_file

dbus_bool_t \_dbus_concat_dir_and_file(DBusString \*dir, const DBusString \*next_component)

Appends the given filename to the given directory.

**Definition** dbus-sysdeps-unix.c:3497

\_dbus_split_paths_and_append

dbus_bool_t \_dbus_split_paths_and_append(DBusString \*dirs, const char \*suffix, DBusList \*\*dir_list)

Split paths into a list of char strings.

**Definition** dbus-sysdeps.c:238

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

DBusList

A node in a linked list.

**Definition** dbus-list.h:37

DBusList::data

void \* data

Data stored at this element.

**Definition** dbus-list.h:40

DBusString

**Definition** dbus-string.h:47
