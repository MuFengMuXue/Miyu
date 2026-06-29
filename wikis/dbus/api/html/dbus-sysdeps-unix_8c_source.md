dbus-sysdeps-unix.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-sysdeps-unix.c Wrappers around UNIX system/libc features (internal to D-Bus implementation)

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

28

29\#include "dbus-internals.h"

30\#include "dbus-sysdeps.h"

31\#include "dbus-sysdeps-unix.h"

32\#include "dbus-threads.h"

33\#include "dbus-protocol.h"

34\#include "dbus-file.h"

35\#include "dbus-transport.h"

36\#include "dbus-string.h"

37\#include "dbus-userdb.h"

38\#include "dbus-list.h"

39\#include "dbus-credentials.h"

40\#include "dbus-nonce.h"

41

42\#include \<limits.h\>

43\#include \<sys/types.h\>

44\#include \<stdlib.h\>

45\#include \<string.h\>

46\#include \<signal.h\>

47\#include \<unistd.h\>

48\#include \<stdio.h\>

49\#include \<fcntl.h\>

50\#include \<sys/socket.h\>

51\#include \<dirent.h\>

52\#include \<sys/un.h\>

53\#include \<pwd.h\>

54\#include \<time.h\>

55\#include \<locale.h\>

56\#include \<sys/time.h\>

57\#include \<sys/stat.h\>

58\#include \<sys/wait.h\>

59\#include \<netinet/in.h\>

60\#include \<netinet/tcp.h\>

61\#include \<netdb.h\>

62\#include \<grp.h\>

63\#include \<arpa/inet.h\>

64

65\#ifdef HAVE_ERRNO_H

66\#include \<errno.h\>

67\#endif

68\#ifdef HAVE_LINUX_CLOSE_RANGE_H

69\#include \<linux/close_range.h\>

70\#endif

71\#ifdef HAVE_SYSLOG_H

72\#include \<syslog.h\>

73\#endif

74\#ifdef HAVE_WRITEV

75\#include \<sys/uio.h\>

76\#endif

77\#ifdef HAVE_BACKTRACE

78\#include \<execinfo.h\>

79\#endif

80\#ifdef HAVE_GETPEERUCRED

81\#include \<ucred.h\>

82\#endif

83\#ifdef HAVE_ALLOCA_H

84\#include \<alloca.h\>

85\#endif

86\#ifdef HAVE_SYS_RANDOM_H

87\#include \<sys/random.h\>

88\#endif

89\#ifdef HAVE_SYS_SYSCALL_H

90\#include \<sys/syscall.h\>

91\#endif

92

93\#ifdef HAVE_ADT

94\#include \<bsm/adt.h\>

95\#endif

96

97\#ifdef HAVE_SYSTEMD

98\#include \<systemd/sd-daemon.h\>

99\#endif

100

101\#if !defined(HAVE_STDATOMIC_H) && !DBUS_USE_SYNC

102\#include \<pthread.h\>

103\#endif

104

105\#ifndef O_BINARY

106\#define O_BINARY 0

107\#endif

108

109\#ifndef AI_ADDRCONFIG

110\#define AI_ADDRCONFIG 0

111\#endif

112

113\#ifndef HAVE_SOCKLEN_T

114\#define socklen_t int

115\#endif

116

117\#if defined (\_\_sun) \|\| defined (\_\_sun\_\_)

118/\*

119 \* CMS_SPACE etc. definitions for Solaris \< 10, based on

120 \* http://mailman.videolan.org/pipermail/vlc-devel/2006-May/024402.html

121 \* via

122 \* http://wiki.opencsw.org/porting-faq#toc10

123 \*

124 \* These are only redefined for Solaris, for now: if your OS needs these too,

125 \* please file a bug. (Or preferably, improve your OS so they're not needed.)

126 \*/

127

128\# ifndef CMSG_ALIGN

129\# ifdef \_\_sun\_\_

130\# define CMSG_ALIGN(len) \_CMSG_DATA_ALIGN (len)

131\# else

132 /\* aligning to sizeof (long) is assumed to be portable (fd.o#40235) \*/

133\# define CMSG_ALIGN(len) (((len) + sizeof (long) - 1) & \\

134 ~(sizeof (long) - 1))

135\# endif

136\# endif

137

138\# ifndef CMSG_SPACE

139\# define CMSG_SPACE(len) (CMSG_ALIGN (sizeof (struct cmsghdr)) + \\

140 CMSG_ALIGN (len))

141\# endif

142

143\# ifndef CMSG_LEN

144\# define CMSG_LEN(len) (CMSG_ALIGN (sizeof (struct cmsghdr)) + (len))

145\# endif

146

147\#endif /\* Solaris \*/

148

149\#if defined(\_\_linux\_\_) && defined(\_\_NR_close_range) && !defined(HAVE_CLOSE_RANGE)

150/\* The kernel headers are new enough to have the close_range syscall,

151 \* but glibc isn't new enough to have the syscall wrapper, so call the

152 \* syscall directly. \*/

153static inline int

154close_range (unsigned int first,

155 unsigned int last,

156 int flags)

157{

158 return syscall (\_\_NR_close_range, first, last, flags);

159}

160/\* Now we can call that inline wrapper as though it was provided by glibc. \*/

161\#define HAVE_CLOSE_RANGE

162\#endif

163

178dbus_bool_t

179\_dbus_ensure_standard_fds (DBusEnsureStandardFdsFlags flags,

180 const char \*\*error_str_p)

181{

182 static int const relevant_flag\[\] = { DBUS_FORCE_STDIN_NULL,

183 DBUS_FORCE_STDOUT_NULL,

184 DBUS_FORCE_STDERR_NULL };

185 /\* Should always get replaced with the real error before use \*/

186 const char \*error_str = "Failed mysteriously";

187 int devnull = -1;

188 int saved_errno;

189 /\* This function relies on the standard fds having their POSIX values. \*/

190 \_DBUS_STATIC_ASSERT (STDIN_FILENO == 0);

191 \_DBUS_STATIC_ASSERT (STDOUT_FILENO == 1);

192 \_DBUS_STATIC_ASSERT (STDERR_FILENO == 2);

193 int i;

194

195 for (i = STDIN_FILENO; i \<= STDERR_FILENO; i++)

196 {

197 /\* Because we rely on being single-threaded, and we want the

198 \* standard fds to not be close-on-exec, we don't set it

199 \* close-on-exec. \*/

200 if (devnull \< i)

201 devnull = open ("/dev/null", O_RDWR);

202

203 if (devnull \< 0)

204 {

205 error_str = "Failed to open /dev/null";

206 goto out;

207 }

208

209 /\* We already opened all fds \< i, so the only way this assertion

210 \* could fail is if another thread closed one, and we document

211 \* this function as not safe for multi-threading. \*/

212 \_dbus_assert (devnull \>= i);

213

214 if (devnull != i && (flags & relevant_flag\[i\]) != 0)

215 {

216 if (dup2 (devnull, i) \< 0)

217 {

218 error_str = "Failed to dup2 /dev/null onto a standard fd";

219 goto out;

220 }

221 }

222 }

223

224 error_str = NULL;

225

226out:

227 saved_errno = errno;

228

229 if (devnull \> STDERR_FILENO)

230 close (devnull);

231

232 if (error_str_p != NULL)

233 \*error_str_p = error_str;

234

235 errno = saved_errno;

236 return (error_str == NULL);

237}

238

239static dbus_bool_t \_dbus_set_fd_nonblocking (int fd,

240 DBusError \*error);

241

242static dbus_bool_t

243\_dbus_open_socket (int \*fd_p,

244 int domain,

245 int type,

246 int protocol,

247 DBusError \*error)

248{

249\#ifdef SOCK_CLOEXEC

250 dbus_bool_t cloexec_done;

251

252 \*fd_p = socket (domain, type \| SOCK_CLOEXEC, protocol);

253 cloexec_done = \*fd_p \>= 0;

254

255 /\* Check if kernel seems to be too old to know SOCK_CLOEXEC \*/

256 if (\*fd_p \< 0 && (errno == EINVAL \|\| errno == EPROTOTYPE))

257\#endif

258 {

259 \*fd_p = socket (domain, type, protocol);

260 }

261

262 if (\*fd_p \>= 0)

263 {

264\#ifdef SOCK_CLOEXEC

265 if (!cloexec_done)

266\#endif

267 {

268 \_dbus_fd_set_close_on_exec(\*fd_p);

269 }

270

271 \_dbus_verbose ("socket fd %d opened\n", \*fd_p);

272 return TRUE;

273 }

274 else

275 {

276 dbus_set_error(error,

277 \_dbus_error_from_errno (errno),

278 "Failed to open socket: %s",

279 \_dbus_strerror (errno));

280 return FALSE;

281 }

282}

283

294static dbus_bool_t

295\_dbus_open_unix_socket (int \*fd,

296 DBusError \*error)

297{

298 return \_dbus_open_socket(fd, AF_UNIX, SOCK_STREAM, 0, error);

299}

300

313dbus_bool_t

314\_dbus_close_socket (DBusSocket \*fd,

315 DBusError \*error)

316{

317 dbus_bool_t rv;

318

319 \_dbus_assert (fd != NULL);

320 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

321

322 rv = \_dbus_close (fd-\>fd, error);

323 \_dbus_socket_invalidate (fd);

324

325 return rv;

326}

327

337int

338\_dbus_read_socket (DBusSocket fd,

339 DBusString \*buffer,

340 int count)

341{

342 return \_dbus_read (fd.fd, buffer, count);

343}

344

355int

356\_dbus_write_socket (DBusSocket fd,

357 const DBusString \*buffer,

358 int start,

359 int len)

360{

361\#if HAVE_DECL_MSG_NOSIGNAL

362 const char \*data;

363 int bytes_written;

364

365 data = \_dbus_string_get_const_data_len (buffer, start, len);

366

367 again:

368

369 bytes_written = send (fd.fd, data, len, MSG_NOSIGNAL);

370

371 if (bytes_written \< 0 && errno == EINTR)

372 goto again;

373

374 return bytes_written;

375

376\#else

377 return \_dbus_write (fd.fd, buffer, start, len);

378\#endif

379}

380

393int

394\_dbus_read_socket_with_unix_fds (DBusSocket fd,

395 DBusString \*buffer,

396 int count,

397 int \*fds,

398 unsigned int \*n_fds) {

399\#ifndef HAVE_UNIX_FD_PASSING

400 int r;

401

402 if ((r = \_dbus_read_socket(fd, buffer, count)) \< 0)

403 return r;

404

405 \*n_fds = 0;

406 return r;

407

408\#else

409 int bytes_read;

410 int start;

411 struct msghdr m;

412 struct iovec iov;

413

414 \_dbus_assert (count \>= 0);

415 \_dbus_assert (\*n_fds \<= DBUS_MAXIMUM_MESSAGE_UNIX_FDS);

416

417 start = \_dbus_string_get_length (buffer);

418

419 if (!\_dbus_string_lengthen (buffer, count))

420 {

421 errno = ENOMEM;

422 return -1;

423 }

424

425 \_DBUS_ZERO(iov);

426 iov.iov_base = \_dbus_string_get_data_len (buffer, start, count);

427 iov.iov_len = count;

428

429 \_DBUS_ZERO(m);

430 m.msg_iov = &iov;

431 m.msg_iovlen = 1;

432

433 /\* Hmm, we have no clue how long the control data will actually be

434 that is queued for us. The least we can do is assume that the

435 caller knows. Hence let's make space for the number of fds that

436 we shall read at max plus the cmsg header. \*/

437 m.msg_controllen = CMSG_SPACE(\*n_fds \* sizeof(int));

438

439 /\* It's probably safe to assume that systems with SCM_RIGHTS also

440 know alloca() \*/

441 m.msg_control = alloca(m.msg_controllen);

442 memset(m.msg_control, 0, m.msg_controllen);

443

444 /\* Do not include the padding at the end when we tell the kernel

445 \* how much we're willing to receive. This avoids getting

446 \* the padding filled with additional fds that we weren't expecting,

447 \* if a (potentially malicious) sender included them. (fd.o \#83622) \*/

448 m.msg_controllen = CMSG_LEN (\*n_fds \* sizeof(int));

449

450 again:

451

452 bytes_read = recvmsg (fd.fd, &m, 0

453\#ifdef MSG_CMSG_CLOEXEC

454 \|MSG_CMSG_CLOEXEC

455\#endif

456 );

457

458 if (bytes_read \< 0)

459 {

460 if (errno == EINTR)

461 goto again;

462 else

463 {

464 /\* put length back (note that this doesn't actually realloc anything) \*/

465 \_dbus_string_set_length (buffer, start);

466 return -1;

467 }

468 }

469 else

470 {

471 struct cmsghdr \*cm;

472 dbus_bool_t found = FALSE;

473

474 for (cm = CMSG_FIRSTHDR(&m); cm; cm = CMSG_NXTHDR(&m, cm))

475 if (cm-\>cmsg_level == SOL_SOCKET && cm-\>cmsg_type == SCM_RIGHTS)

476 {

477 size_t i;

478 int \*payload = (int \*) (void \*) CMSG_DATA (cm);

479 size_t payload_len_bytes = (cm-\>cmsg_len - CMSG_LEN (0));

480 size_t payload_len_fds;

481 size_t fds_to_use;

482

483 /\* Every unsigned int fits in a size_t without truncation, so

484 \* casting (size_t) \*n_fds is OK \*/

485 \_DBUS_STATIC_ASSERT (sizeof (size_t) \>= sizeof (unsigned int));

486

487 if ((m.msg_flags & MSG_CTRUNC) && CMSG_NXTHDR(&m, cm) == NULL &&

488 (char \*) payload + payload_len_bytes \>

489 (char \*) m.msg_control + m.msg_controllen)

490 {

491 /\* This is the last cmsg in a truncated message and using

492 \* cmsg_len would apparently overrun the allocated buffer.

493 \* Some operating systems (illumos and Solaris are known) do

494 \* not adjust cmsg_len in the last cmsg when truncation occurs.

495 \* Adjust the payload length here. The calculation for

496 \* payload_len_fds below will discard any trailing bytes that

497 \* belong to an incomplete file descriptor - the kernel will

498 \* have already closed that (at least for illumos and Solaris)

499 \*/

500 payload_len_bytes = m.msg_controllen -

501 ((char \*) payload - (char \*) m.msg_control);

502 }

503

504 payload_len_fds = payload_len_bytes / sizeof (int);

505

506 if (\_DBUS_LIKELY (payload_len_fds \<= (size_t) \*n_fds))

507 {

508 /\* The fds in the payload will fit in our buffer \*/

509 fds_to_use = payload_len_fds;

510 }

511 else

512 {

513 /\* Too many fds in the payload. This shouldn't happen

514 \* any more because we're setting m.msg_controllen to

515 \* the exact number we can accept, but be safe and

516 \* truncate. \*/

517 fds_to_use = (size_t) \*n_fds;

518

519 /\* Close the excess fds to avoid DoS: if they stayed open,

520 \* someone could send us an extra fd per message

521 \* and we'd eventually run out. \*/

522 for (i = fds_to_use; i \< payload_len_fds; i++)

523 {

524 close (payload\[i\]);

525 }

526 }

527

528 memcpy (fds, payload, fds_to_use \* sizeof (int));

529 found = TRUE;

530 /\* This narrowing cast from size_t to unsigned int cannot

531 \* overflow because we have chosen fds_to_use

532 \* to be \<= \*n_fds \*/

533 \*n_fds = (unsigned int) fds_to_use;

534

535 /\* Linux doesn't tell us whether MSG_CMSG_CLOEXEC actually

536 worked, hence we need to go through this list and set

537 CLOEXEC everywhere in any case \*/

538 for (i = 0; i \< fds_to_use; i++)

539 \_dbus_fd_set_close_on_exec(fds\[i\]);

540

541 break;

542 }

543

544 if (!found)

545 \*n_fds = 0;

546

547 if (m.msg_flags & MSG_CTRUNC)

548 {

549 unsigned int i;

550

551 /\* Hmm, apparently the control data was truncated. The bad

552 thing is that we might have completely lost a couple of fds

553 without chance to recover them. Hence let's treat this as a

554 serious error. \*/

555

556 /\* We still need to close whatever fds we \*did\* receive,

557 \* otherwise they'll never get closed. (CVE-2020-12049) \*/

558 for (i = 0; i \< \*n_fds; i++)

559 close (fds\[i\]);

560

561 \*n_fds = 0;

562 errno = ENOSPC;

563 \_dbus_string_set_length (buffer, start);

564 return -1;

565 }

566

567 /\* put length back (doesn't actually realloc) \*/

568 \_dbus_string_set_length (buffer, start + bytes_read);

569

570\#if 0

571 if (bytes_read \> 0)

572 \_dbus_verbose_bytes_of_string (buffer, start, bytes_read);

573\#endif

574

575 return bytes_read;

576 }

577\#endif

578}

579

580int

581\_dbus_write_socket_with_unix_fds(DBusSocket fd,

582 const DBusString \*buffer,

583 int start,

584 int len,

585 const int \*fds,

586 int n_fds) {

587

588\#ifndef HAVE_UNIX_FD_PASSING

589

590 if (n_fds \> 0) {

591 errno = ENOTSUP;

592 return -1;

593 }

594

595 return \_dbus_write_socket(fd, buffer, start, len);

596\#else

597 return \_dbus_write_socket_with_unix_fds_two(fd, buffer, start, len, NULL, 0, 0, fds, n_fds);

598\#endif

599}

600

601int

602\_dbus_write_socket_with_unix_fds_two(DBusSocket fd,

603 const DBusString \*buffer1,

604 int start1,

605 int len1,

606 const DBusString \*buffer2,

607 int start2,

608 int len2,

609 const int \*fds,

610 int n_fds) {

611

612\#ifndef HAVE_UNIX_FD_PASSING

613

614 if (n_fds \> 0) {

615 errno = ENOTSUP;

616 return -1;

617 }

618

619 return \_dbus_write_socket_two(fd,

620 buffer1, start1, len1,

621 buffer2, start2, len2);

622\#else

623

624 struct msghdr m;

625 struct cmsghdr \*cm;

626 struct iovec iov\[2\];

627 int bytes_written;

628

629 \_dbus_assert (len1 \>= 0);

630 \_dbus_assert (len2 \>= 0);

631 \_dbus_assert (n_fds \>= 0);

632

633 \_DBUS_ZERO(iov);

634 iov\[0\].iov_base = (char\*) \_dbus_string_get_const_data_len (buffer1, start1, len1);

635 iov\[0\].iov_len = len1;

636

637 if (buffer2)

638 {

639 iov\[1\].iov_base = (char\*) \_dbus_string_get_const_data_len (buffer2, start2, len2);

640 iov\[1\].iov_len = len2;

641 }

642

643 \_DBUS_ZERO(m);

644 m.msg_iov = iov;

645 m.msg_iovlen = buffer2 ? 2 : 1;

646

647 if (n_fds \> 0)

648 {

649 m.msg_controllen = CMSG_SPACE(n_fds \* sizeof(int));

650 m.msg_control = alloca(m.msg_controllen);

651 memset(m.msg_control, 0, m.msg_controllen);

652

653 cm = CMSG_FIRSTHDR(&m);

654 cm-\>cmsg_level = SOL_SOCKET;

655 cm-\>cmsg_type = SCM_RIGHTS;

656 cm-\>cmsg_len = CMSG_LEN(n_fds \* sizeof(int));

657 memcpy(CMSG_DATA(cm), fds, n_fds \* sizeof(int));

658 }

659

660 again:

661

662 bytes_written = sendmsg (fd.fd, &m, 0

663\#if HAVE_DECL_MSG_NOSIGNAL

664 \|MSG_NOSIGNAL

665\#endif

666 );

667

668 if (bytes_written \< 0 && errno == EINTR)

669 goto again;

670

671\#if 0

672 if (bytes_written \> 0)

673 \_dbus_verbose_bytes_of_string (buffer, start, bytes_written);

674\#endif

675

676 return bytes_written;

677\#endif

678}

679

693int

694\_dbus_write_socket_two (DBusSocket fd,

695 const DBusString \*buffer1,

696 int start1,

697 int len1,

698 const DBusString \*buffer2,

699 int start2,

700 int len2)

701{

702\#if HAVE_DECL_MSG_NOSIGNAL

703 struct iovec vectors\[2\];

704 const char \*data1;

705 const char \*data2;

706 int bytes_written;

707 struct msghdr m;

708

709 \_dbus_assert (buffer1 != NULL);

710 \_dbus_assert (start1 \>= 0);

711 \_dbus_assert (start2 \>= 0);

712 \_dbus_assert (len1 \>= 0);

713 \_dbus_assert (len2 \>= 0);

714

715 data1 = \_dbus_string_get_const_data_len (buffer1, start1, len1);

716

717 if (buffer2 != NULL)

718 data2 = \_dbus_string_get_const_data_len (buffer2, start2, len2);

719 else

720 {

721 data2 = NULL;

722 start2 = 0;

723 len2 = 0;

724 }

725

726 vectors\[0\].iov_base = (char\*) data1;

727 vectors\[0\].iov_len = len1;

728 vectors\[1\].iov_base = (char\*) data2;

729 vectors\[1\].iov_len = len2;

730

731 \_DBUS_ZERO(m);

732 m.msg_iov = vectors;

733 m.msg_iovlen = data2 ? 2 : 1;

734

735 again:

736

737 bytes_written = sendmsg (fd.fd, &m, MSG_NOSIGNAL);

738

739 if (bytes_written \< 0 && errno == EINTR)

740 goto again;

741

742 return bytes_written;

743

744\#else

745 return \_dbus_write_two (fd.fd, buffer1, start1, len1,

746 buffer2, start2, len2);

747\#endif

748}

749

766int

767\_dbus_read (int fd,

768 DBusString \*buffer,

769 int count)

770{

771 int bytes_read;

772 int start;

773 char \*data;

774

775 \_dbus_assert (count \>= 0);

776

777 start = \_dbus_string_get_length (buffer);

778

779 if (!\_dbus_string_lengthen (buffer, count))

780 {

781 errno = ENOMEM;

782 return -1;

783 }

784

785 data = \_dbus_string_get_data_len (buffer, start, count);

786

787 again:

788

789 bytes_read = read (fd, data, count);

790

791 if (bytes_read \< 0)

792 {

793 if (errno == EINTR)

794 goto again;

795 else

796 {

797 /\* put length back (note that this doesn't actually realloc anything) \*/

798 \_dbus_string_set_length (buffer, start);

799 return -1;

800 }

801 }

802 else

803 {

804 /\* put length back (doesn't actually realloc) \*/

805 \_dbus_string_set_length (buffer, start + bytes_read);

806

807\#if 0

808 if (bytes_read \> 0)

809 \_dbus_verbose_bytes_of_string (buffer, start, bytes_read);

810\#endif

811

812 return bytes_read;

813 }

814}

815

826int

827\_dbus_write (int fd,

828 const DBusString \*buffer,

829 int start,

830 int len)

831{

832 const char \*data;

833 int bytes_written;

834

835 data = \_dbus_string_get_const_data_len (buffer, start, len);

836

837 again:

838

839 bytes_written = write (fd, data, len);

840

841 if (bytes_written \< 0 && errno == EINTR)

842 goto again;

843

844\#if 0

845 if (bytes_written \> 0)

846 \_dbus_verbose_bytes_of_string (buffer, start, bytes_written);

847\#endif

848

849 return bytes_written;

850}

851

872int

873\_dbus_write_two (int fd,

874 const DBusString \*buffer1,

875 int start1,

876 int len1,

877 const DBusString \*buffer2,

878 int start2,

879 int len2)

880{

881 \_dbus_assert (buffer1 != NULL);

882 \_dbus_assert (start1 \>= 0);

883 \_dbus_assert (start2 \>= 0);

884 \_dbus_assert (len1 \>= 0);

885 \_dbus_assert (len2 \>= 0);

886

887\#ifdef HAVE_WRITEV

888 {

889 struct iovec vectors\[2\];

890 const char \*data1;

891 const char \*data2;

892 int bytes_written;

893

894 data1 = \_dbus_string_get_const_data_len (buffer1, start1, len1);

895

896 if (buffer2 != NULL)

897 data2 = \_dbus_string_get_const_data_len (buffer2, start2, len2);

898 else

899 {

900 data2 = NULL;

901 start2 = 0;

902 len2 = 0;

903 }

904

905 vectors\[0\].iov_base = (char\*) data1;

906 vectors\[0\].iov_len = len1;

907 vectors\[1\].iov_base = (char\*) data2;

908 vectors\[1\].iov_len = len2;

909

910 again:

911

912 bytes_written = writev (fd,

913 vectors,

914 data2 ? 2 : 1);

915

916 if (bytes_written \< 0 && errno == EINTR)

917 goto again;

918

919 return bytes_written;

920 }

921\#else /\* HAVE_WRITEV \*/

922 {

923 int ret1, ret2;

924

925 ret1 = \_dbus_write (fd, buffer1, start1, len1);

926 if (ret1 == len1 && buffer2 != NULL)

927 {

928 ret2 = \_dbus_write (fd, buffer2, start2, len2);

929 if (ret2 \< 0)

930 ret2 = 0; /\* we can't report an error as the first write was OK \*/

931

932 return ret1 + ret2;

933 }

934 else

935 return ret1;

936 }

937\#endif /\* !HAVE_WRITEV \*/

938}

939

956DBusSocket

957\_dbus_connect_unix_socket (const char \*path,

958 dbus_bool_t abstract,

959 DBusError \*error)

960{

961 DBusSocket fd = DBUS_SOCKET_INIT;

962 size_t path_len;

963 struct sockaddr_un addr;

964 \_DBUS_STATIC_ASSERT (sizeof (addr.sun_path) \> \_DBUS_MAX_SUN_PATH_LENGTH);

965

966 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

967

968 \_dbus_verbose ("connecting to unix socket %s abstract=%d\n",

969 path, abstract);

970

971

972 if (!\_dbus_open_unix_socket (&fd.fd, error))

973 {

974 \_DBUS_ASSERT_ERROR_IS_SET(error);

975 return fd;

976 }

977 \_DBUS_ASSERT_ERROR_IS_CLEAR(error);

978

979 \_DBUS_ZERO (addr);

980 addr.sun_family = AF_UNIX;

981 path_len = strlen (path);

982

983 if (abstract)

984 {

985\#ifdef \_\_linux\_\_

986 addr.sun_path\[0\] = '\0'; /\* this is what says "use abstract" \*/

987 path_len++; /\* Account for the extra nul byte added to the start of sun_path \*/

988

989 if (path_len \> \_DBUS_MAX_SUN_PATH_LENGTH)

990 {

991 dbus_set_error (error, DBUS_ERROR_BAD_ADDRESS,

992 "Abstract socket name too long\n");

993 \_dbus_close_socket (&fd, NULL);

994 return fd;

995 }

996

997 strncpy (&addr.sun_path\[1\], path, sizeof (addr.sun_path) - 2);

998 /\* \_dbus_verbose_bytes (addr.sun_path, sizeof (addr.sun_path)); \*/

999\#else /\* !\_\_linux\_\_ \*/

1000 dbus_set_error (error, DBUS_ERROR_NOT_SUPPORTED,

1001 "Operating system does not support abstract socket namespace\n");

1002 \_dbus_close_socket (&fd, NULL);

1003 return fd;

1004\#endif /\* !\_\_linux\_\_ \*/

1005 }

1006 else

1007 {

1008 if (path_len \> \_DBUS_MAX_SUN_PATH_LENGTH)

1009 {

1010 dbus_set_error (error, DBUS_ERROR_BAD_ADDRESS,

1011 "Socket name too long\n");

1012 \_dbus_close_socket (&fd, NULL);

1013 return fd;

1014 }

1015

1016 strncpy (addr.sun_path, path, sizeof (addr.sun_path) - 1);

1017 }

1018

1019 if (connect (fd.fd, (struct sockaddr\*) &addr, \_DBUS_STRUCT_OFFSET (struct sockaddr_un, sun_path) + path_len) \< 0)

1020 {

1021 dbus_set_error (error,

1022 \_dbus_error_from_errno (errno),

1023 "Failed to connect to socket %s: %s",

1024 path, \_dbus_strerror (errno));

1025

1026 \_dbus_close_socket (&fd, NULL);

1027 return fd;

1028 }

1029

1030 if (!\_dbus_set_fd_nonblocking (fd.fd, error))

1031 {

1032 \_DBUS_ASSERT_ERROR_IS_SET (error);

1033

1034 \_dbus_close_socket (&fd, NULL);

1035 return fd;

1036 }

1037

1038 return fd;

1039}

1040

1053DBusSocket

1054\_dbus_connect_exec (const char \*path,

1055 char \*const argv\[\],

1056 DBusError \*error)

1057{

1058 DBusSocket s = DBUS_SOCKET_INIT;

1059 int fds\[2\];

1060 pid_t pid;

1061 int retval;

1062 dbus_bool_t cloexec_done = 0;

1063

1064 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

1065

1066 \_dbus_verbose ("connecting to process %s\n", path);

1067

1068\#ifdef SOCK_CLOEXEC

1069 retval = socketpair (AF_UNIX, SOCK_STREAM\|SOCK_CLOEXEC, 0, fds);

1070 cloexec_done = (retval \>= 0);

1071

1072 if (retval \< 0 && (errno == EINVAL \|\| errno == EPROTOTYPE))

1073\#endif

1074 {

1075 retval = socketpair (AF_UNIX, SOCK_STREAM, 0, fds);

1076 }

1077

1078 if (retval \< 0)

1079 {

1080 dbus_set_error (error,

1081 \_dbus_error_from_errno (errno),

1082 "Failed to create socket pair: %s",

1083 \_dbus_strerror (errno));

1084 \_dbus_assert (!\_dbus_socket_is_valid (s));

1085 return s;

1086 }

1087

1088 if (!cloexec_done)

1089 {

1090 \_dbus_fd_set_close_on_exec (fds\[0\]);

1091 \_dbus_fd_set_close_on_exec (fds\[1\]);

1092 }

1093

1094 /\* Make sure our output buffers aren't redundantly printed by both the

1095 \* parent and the child \*/

1096 fflush (stdout);

1097 fflush (stderr);

1098

1099 pid = fork ();

1100 if (pid \< 0)

1101 {

1102 dbus_set_error (error,

1103 \_dbus_error_from_errno (errno),

1104 "Failed to fork() to call %s: %s",

1105 path, \_dbus_strerror (errno));

1106 close (fds\[0\]);

1107 close (fds\[1\]);

1108 \_dbus_assert (!\_dbus_socket_is_valid (s));

1109 return s;

1110 }

1111

1112 if (pid == 0)

1113 {

1114 /\* child \*/

1115 close (fds\[0\]);

1116

1117 dup2 (fds\[1\], STDIN_FILENO);

1118 dup2 (fds\[1\], STDOUT_FILENO);

1119

1120 if (fds\[1\] != STDIN_FILENO &&

1121 fds\[1\] != STDOUT_FILENO)

1122 close (fds\[1\]);

1123

1124 /\* Inherit STDERR and the controlling terminal from the

1125 parent \*/

1126

1127 \_dbus_close_all ();

1128

1129 execvp (path, (char \* const \*) argv);

1130

1131 fprintf (stderr, "Failed to execute process %s: %s\n", path, \_dbus_strerror (errno));

1132

1133 \_exit(1);

1134 }

1135

1136 /\* parent \*/

1137 close (fds\[1\]);

1138

1139 if (!\_dbus_set_fd_nonblocking (fds\[0\], error))

1140 {

1141 \_DBUS_ASSERT_ERROR_IS_SET (error);

1142

1143 close (fds\[0\]);

1144 \_dbus_assert (!\_dbus_socket_is_valid (s));

1145 return s;

1146 }

1147

1148 s.fd = fds\[0\];

1149 return s;

1150}

1151

1169DBusSocket

1170\_dbus_listen_unix_socket (const char \*path,

1171 dbus_bool_t abstract,

1172 DBusError \*error)

1173{

1174 DBusSocket s = DBUS_SOCKET_INIT;

1175 int listen_fd;

1176 struct sockaddr_un addr;

1177 size_t path_len;

1178 \_DBUS_STATIC_ASSERT (sizeof (addr.sun_path) \> \_DBUS_MAX_SUN_PATH_LENGTH);

1179

1180 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

1181

1182 \_dbus_verbose ("listening on unix socket %s abstract=%d\n",

1183 path, abstract);

1184

1185 if (!\_dbus_open_unix_socket (&listen_fd, error))

1186 {

1187 \_DBUS_ASSERT_ERROR_IS_SET(error);

1188 return s;

1189 }

1190 \_DBUS_ASSERT_ERROR_IS_CLEAR(error);

1191

1192 \_DBUS_ZERO (addr);

1193 addr.sun_family = AF_UNIX;

1194 path_len = strlen (path);

1195

1196 if (abstract)

1197 {

1198\#ifdef \_\_linux\_\_

1199 /\* remember that abstract names aren't nul-terminated so we rely

1200 \* on sun_path being filled in with zeroes above.

1201 \*/

1202 addr.sun_path\[0\] = '\0'; /\* this is what says "use abstract" \*/

1203 path_len++; /\* Account for the extra nul byte added to the start of sun_path \*/

1204

1205 if (path_len \> \_DBUS_MAX_SUN_PATH_LENGTH)

1206 {

1207 dbus_set_error (error, DBUS_ERROR_BAD_ADDRESS,

1208 "Abstract socket name too long\n");

1209 \_dbus_close (listen_fd, NULL);

1210 return s;

1211 }

1212

1213 strncpy (&addr.sun_path\[1\], path, sizeof (addr.sun_path) - 2);

1214 /\* \_dbus_verbose_bytes (addr.sun_path, sizeof (addr.sun_path)); \*/

1215\#else /\* !\_\_linux\_\_ \*/

1216 dbus_set_error (error, DBUS_ERROR_NOT_SUPPORTED,

1217 "Operating system does not support abstract socket namespace\n");

1218 \_dbus_close (listen_fd, NULL);

1219 return s;

1220\#endif /\* !\_\_linux\_\_ \*/

1221 }

1222 else

1223 {

1224 /\* Discussed security implications of this with Nalin,

1225 \* and we couldn't think of where it would kick our ass, but

1226 \* it still seems a bit sucky. It also has non-security suckage;

1227 \* really we'd prefer to exit if the socket is already in use.

1228 \* But there doesn't seem to be a good way to do this.

1229 \*

1230 \* Just to be extra careful, I threw in the stat() - clearly

1231 \* the stat() can't \*fix\* any security issue, but it at least

1232 \* avoids inadvertent/accidental data loss.

1233 \*/

1234 {

1235 struct stat sb;

1236

1237 if (stat (path, &sb) == 0 &&

1238 S_ISSOCK (sb.st_mode))

1239 unlink (path);

1240 }

1241

1242 if (path_len \> \_DBUS_MAX_SUN_PATH_LENGTH)

1243 {

1244 dbus_set_error (error, DBUS_ERROR_BAD_ADDRESS,

1245 "Socket name too long\n");

1246 \_dbus_close (listen_fd, NULL);

1247 return s;

1248 }

1249

1250 strncpy (addr.sun_path, path, sizeof (addr.sun_path) - 1);

1251 }

1252

1253 if (bind (listen_fd, (struct sockaddr\*) &addr, \_DBUS_STRUCT_OFFSET (struct sockaddr_un, sun_path) + path_len) \< 0)

1254 {

1255 dbus_set_error (error, \_dbus_error_from_errno (errno),

1256 "Failed to bind socket \\%s\\: %s",

1257 path, \_dbus_strerror (errno));

1258 \_dbus_close (listen_fd, NULL);

1259 return s;

1260 }

1261

1262 if (listen (listen_fd, SOMAXCONN /\* backlog \*/) \< 0)

1263 {

1264 dbus_set_error (error, \_dbus_error_from_errno (errno),

1265 "Failed to listen on socket \\%s\\: %s",

1266 path, \_dbus_strerror (errno));

1267 \_dbus_close (listen_fd, NULL);

1268 return s;

1269 }

1270

1271 if (!\_dbus_set_fd_nonblocking (listen_fd, error))

1272 {

1273 \_DBUS_ASSERT_ERROR_IS_SET (error);

1274 \_dbus_close (listen_fd, NULL);

1275 return s;

1276 }

1277

1278 /\* Try opening up the permissions, but if we can't, just go ahead

1279 \* and continue, maybe it will be good enough.

1280 \*/

1281 if (!abstract && chmod (path, 0777) \< 0)

1282 \_dbus_warn ("Could not set mode 0777 on socket %s", path);

1283

1284 s.fd = listen_fd;

1285 return s;

1286}

1287

1298int

1299\_dbus_listen_systemd_sockets (DBusSocket \*\*fds,

1300 DBusError \*error)

1301{

1302\#ifdef HAVE_SYSTEMD

1303 int r, n;

1304 int fd;

1305 DBusSocket \*new_fds;

1306

1307 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

1308

1309 n = sd_listen_fds (TRUE);

1310 if (n \< 0)

1311 {

1312 dbus_set_error (error, \_dbus_error_from_errno (-n),

1313 "Failed to acquire systemd socket: %s",

1314 \_dbus_strerror (-n));

1315 return -1;

1316 }

1317

1318 if (n \<= 0)

1319 {

1320 dbus_set_error (error, DBUS_ERROR_BAD_ADDRESS,

1321 "No socket received.");

1322 return -1;

1323 }

1324

1325 for (fd = SD_LISTEN_FDS_START; fd \< SD_LISTEN_FDS_START + n; fd ++)

1326 {

1327 r = sd_is_socket (fd, AF_UNSPEC, SOCK_STREAM, 1);

1328 if (r \< 0)

1329 {

1330 dbus_set_error (error, \_dbus_error_from_errno (-r),

1331 "Failed to verify systemd socket type: %s",

1332 \_dbus_strerror (-r));

1333 return -1;

1334 }

1335

1336 if (!r)

1337 {

1338 dbus_set_error (error, DBUS_ERROR_BAD_ADDRESS,

1339 "Passed socket has wrong type.");

1340 return -1;

1341 }

1342 }

1343

1344 /\* OK, the file descriptors are all good, so let's take posession of

1345 them then. \*/

1346

1347 new_fds = dbus_new (DBusSocket, n);

1348 if (!new_fds)

1349 {

1350 dbus_set_error (error, DBUS_ERROR_NO_MEMORY,

1351 "Failed to allocate file handle array.");

1352 goto fail;

1353 }

1354

1355 for (fd = SD_LISTEN_FDS_START; fd \< SD_LISTEN_FDS_START + n; fd ++)

1356 {

1357 if (!\_dbus_set_fd_nonblocking (fd, error))

1358 {

1359 \_DBUS_ASSERT_ERROR_IS_SET (error);

1360 goto fail;

1361 }

1362

1363 new_fds\[fd - SD_LISTEN_FDS_START\].fd = fd;

1364 }

1365

1366 \*fds = new_fds;

1367 return n;

1368

1369 fail:

1370

1371 for (fd = SD_LISTEN_FDS_START; fd \< SD_LISTEN_FDS_START + n; fd ++)

1372 {

1373 \_dbus_close (fd, NULL);

1374 }

1375

1376 dbus_free (new_fds);

1377 return -1;

1378\#else

1379 dbus_set_error_const (error, DBUS_ERROR_NOT_SUPPORTED,

1380 "dbus was compiled without systemd support");

1381 return -1;

1382\#endif

1383}

1384

1385/\* Convert an error code from getaddrinfo() or getnameinfo() into

1386 \* a D-Bus error name. \*/

1387static const char \*

1388\_dbus_error_from_gai (int gai_res,

1389 int saved_errno)

1390{

1391 switch (gai_res)

1392 {

1393\#ifdef EAI_FAMILY

1394 case EAI_FAMILY:

1395 /\* ai_family not supported (at all) \*/

1396 return DBUS_ERROR_NOT_SUPPORTED;

1397\#endif

1398

1399\#ifdef EAI_SOCKTYPE

1400 case EAI_SOCKTYPE:

1401 /\* ai_socktype not supported (at all) \*/

1402 return DBUS_ERROR_NOT_SUPPORTED;

1403\#endif

1404

1405\#ifdef EAI_MEMORY

1406 case EAI_MEMORY:

1407 /\* Out of memory \*/

1408 return DBUS_ERROR_NO_MEMORY;

1409\#endif

1410

1411\#ifdef EAI_SYSTEM

1412 case EAI_SYSTEM:

1413 /\* Unspecified system error, details in errno \*/

1414 return \_dbus_error_from_errno (saved_errno);

1415\#endif

1416

1417 case 0:

1418 /\* It succeeded, but we didn't get any addresses? \*/

1419 return DBUS_ERROR_FAILED;

1420

1421 /\* EAI_AGAIN: Transient failure \*/

1422 /\* EAI_BADFLAGS: invalid ai_flags (programming error) \*/

1423 /\* EAI_FAIL: Non-recoverable failure \*/

1424 /\* EAI_NODATA: host exists but has no addresses \*/

1425 /\* EAI_NONAME: host does not exist \*/

1426 /\* EAI_OVERFLOW: argument buffer overflow \*/

1427 /\* EAI_SERVICE: service not available for specified socket

1428 \* type (we should never see this because we use numeric

1429 \* ports) \*/

1430 default:

1431 return DBUS_ERROR_FAILED;

1432 }

1433}

1434

1448DBusSocket

1449\_dbus_connect_tcp_socket (const char \*host,

1450 const char \*port,

1451 const char \*family,

1452 DBusError \*error)

1453{

1454 return \_dbus_connect_tcp_socket_with_nonce (host, port, family, (const char\*)NULL, error);

1455}

1456

1457DBusSocket

1458\_dbus_connect_tcp_socket_with_nonce (const char \*host,

1459 const char \*port,

1460 const char \*family,

1461 const char \*noncefile,

1462 DBusError \*error)

1463{

1464 int saved_errno = 0;

1465 DBusList \*connect_errors = NULL;

1466 DBusSocket fd = DBUS_SOCKET_INIT;

1467 int res;

1468 struct addrinfo hints;

1469 struct addrinfo \*ai = NULL;

1470 const struct addrinfo \*tmp;

1471 DBusError \*connect_error;

1472

1473 \_DBUS_ASSERT_ERROR_IS_CLEAR(error);

1474

1475 \_DBUS_ZERO (hints);

1476

1477 if (!family)

1478 hints.ai_family = AF_UNSPEC;

1479 else if (!strcmp(family, "ipv4"))

1480 hints.ai_family = AF_INET;

1481 else if (!strcmp(family, "ipv6"))

1482 hints.ai_family = AF_INET6;

1483 else

1484 {

1485 dbus_set_error (error,

1486 DBUS_ERROR_BAD_ADDRESS,

1487 "Unknown address family %s", family);

1488 return \_dbus_socket_get_invalid ();

1489 }

1490 hints.ai_protocol = IPPROTO_TCP;

1491 hints.ai_socktype = SOCK_STREAM;

1492 hints.ai_flags = AI_ADDRCONFIG;

1493

1494 if ((res = getaddrinfo(host, port, &hints, &ai)) != 0)

1495 {

1496 dbus_set_error (error,

1497 \_dbus_error_from_gai (res, errno),

1498 "Failed to lookup host/port: \\%s:%s\\: %s (%d)",

1499 host, port, gai_strerror(res), res);

1500 goto out;

1501 }

1502

1503 tmp = ai;

1504 while (tmp)

1505 {

1506 if (!\_dbus_open_socket (&fd.fd, tmp-\>ai_family, SOCK_STREAM, 0, error))

1507 {

1508 \_DBUS_ASSERT_ERROR_IS_SET(error);

1509 \_dbus_socket_invalidate (&fd);

1510 goto out;

1511 }

1512 \_DBUS_ASSERT_ERROR_IS_CLEAR(error);

1513

1514 if (connect (fd.fd, (struct sockaddr\*) tmp-\>ai_addr, tmp-\>ai_addrlen) \< 0)

1515 {

1516 saved_errno = errno;

1517 \_dbus_close_socket (&fd, NULL);

1518

1519 connect_error = dbus_new0 (DBusError, 1);

1520

1521 if (connect_error == NULL)

1522 {

1523 \_DBUS_SET_OOM (error);

1524 goto out;

1525 }

1526

1527 dbus_error_init (connect_error);

1528 \_dbus_set_error_with_inet_sockaddr (connect_error,

1529 tmp-\>ai_addr, tmp-\>ai_addrlen,

1530 "Failed to connect to socket",

1531 saved_errno);

1532

1533 if (!\_dbus_list_append (&connect_errors, connect_error))

1534 {

1535 dbus_error_free (connect_error);

1536 dbus_free (connect_error);

1537 \_DBUS_SET_OOM (error);

1538 goto out;

1539 }

1540

1541 tmp = tmp-\>ai_next;

1542 continue;

1543 }

1544

1545 break;

1546 }

1547

1548 if (!\_dbus_socket_is_valid (fd))

1549 {

1550 \_dbus_combine_tcp_errors (&connect_errors, "Failed to connect",

1551 host, port, error);

1552 goto out;

1553 }

1554

1555 if (noncefile != NULL)

1556 {

1557 DBusString noncefileStr;

1558 dbus_bool_t ret;

1559 \_dbus_string_init_const (&noncefileStr, noncefile);

1560 ret = \_dbus_send_nonce (fd, &noncefileStr, error);

1561

1562 if (!ret)

1563 {

1564 \_dbus_close_socket (&fd, NULL);

1565 goto out;

1566 }

1567 }

1568

1569 if (!\_dbus_set_fd_nonblocking (fd.fd, error))

1570 {

1571 \_dbus_close_socket (&fd, NULL);

1572 goto out;

1573 }

1574

1575out:

1576 if (ai != NULL)

1577 freeaddrinfo (ai);

1578

1579 while ((connect_error = \_dbus_list_pop_first (&connect_errors)))

1580 {

1581 dbus_error_free (connect_error);

1582 dbus_free (connect_error);

1583 }

1584

1585 return fd;

1586}

1587

1605int

1606\_dbus_listen_tcp_socket (const char \*host,

1607 const char \*port,

1608 const char \*family,

1609 DBusString \*retport,

1610 const char \*\*retfamily,

1611 DBusSocket \*\*fds_p,

1612 DBusError \*error)

1613{

1614 int saved_errno;

1615 int nlisten_fd = 0, res, i;

1616 DBusList \*bind_errors = NULL;

1617 DBusError \*bind_error = NULL;

1618 DBusSocket \*listen_fd = NULL;

1619 struct addrinfo hints;

1620 struct addrinfo \*ai, \*tmp;

1621 unsigned int reuseaddr;

1622 dbus_bool_t have_ipv4 = FALSE;

1623 dbus_bool_t have_ipv6 = FALSE;

1624

1625 \*fds_p = NULL;

1626 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

1627

1628 \_DBUS_ZERO (hints);

1629

1630 if (!family)

1631 hints.ai_family = AF_UNSPEC;

1632 else if (!strcmp(family, "ipv4"))

1633 hints.ai_family = AF_INET;

1634 else if (!strcmp(family, "ipv6"))

1635 hints.ai_family = AF_INET6;

1636 else

1637 {

1638 dbus_set_error (error,

1639 DBUS_ERROR_BAD_ADDRESS,

1640 "Unknown address family %s", family);

1641 return -1;

1642 }

1643

1644 hints.ai_protocol = IPPROTO_TCP;

1645 hints.ai_socktype = SOCK_STREAM;

1646 hints.ai_flags = AI_ADDRCONFIG \| AI_PASSIVE;

1647

1648 redo_lookup_with_port:

1649 ai = NULL;

1650 if ((res = getaddrinfo(host, port, &hints, &ai)) != 0 \|\| !ai)

1651 {

1652 dbus_set_error (error,

1653 \_dbus_error_from_gai (res, errno),

1654 "Failed to lookup host/port: \\%s:%s\\: %s (%d)",

1655 host ? host : "\*", port ? port : "0", gai_strerror(res), res);

1656 goto failed;

1657 }

1658

1659 tmp = ai;

1660 while (tmp)

1661 {

1662 int fd = -1, tcp_nodelay_on;

1663 DBusSocket \*newlisten_fd;

1664

1665 if (!\_dbus_open_socket (&fd, tmp-\>ai_family, SOCK_STREAM, 0, error))

1666 {

1667 \_DBUS_ASSERT_ERROR_IS_SET(error);

1668 goto failed;

1669 }

1670 \_DBUS_ASSERT_ERROR_IS_CLEAR(error);

1671

1672 reuseaddr = 1;

1673 if (setsockopt (fd, SOL_SOCKET, SO_REUSEADDR, &reuseaddr, sizeof(reuseaddr))==-1)

1674 {

1675 \_dbus_warn ("Failed to set socket option \\%s:%s\\: %s",

1676 host ? host : "\*", port ? port : "0", \_dbus_strerror (errno));

1677 }

1678

1679 /\* Nagle's algorithm imposes a huge delay on the initial messages

1680 going over TCP. \*/

1681 tcp_nodelay_on = 1;

1682 if (setsockopt (fd, IPPROTO_TCP, TCP_NODELAY, &tcp_nodelay_on, sizeof (tcp_nodelay_on)) == -1)

1683 {

1684 \_dbus_warn ("Failed to set TCP_NODELAY socket option \\%s:%s\\: %s",

1685 host ? host : "\*", port ? port : "0", \_dbus_strerror (errno));

1686 }

1687

1688 if (bind (fd, (struct sockaddr\*) tmp-\>ai_addr, tmp-\>ai_addrlen) \< 0)

1689 {

1690 saved_errno = errno;

1691 \_dbus_close(fd, NULL);

1692

1693 /\*

1694 \* We don't treat this as a fatal error, because there might be

1695 \* other addresses that we can listen on. In particular:

1696 \*

1697 \* - If saved_errno is EADDRINUSE after we

1698 \* "goto redo_lookup_with_port" after binding a port on one of the

1699 \* possible addresses, we will try to bind that same port on

1700 \* every address, including the same address again for a second

1701 \* time, which will fail with EADDRINUSE.

1702 \*

1703 \* - If saved_errno is EADDRINUSE, it might be because binding to

1704 \* an IPv6 address implicitly binds to a corresponding IPv4

1705 \* address or vice versa (e.g. Linux with bindv6only=0).

1706 \*

1707 \* - If saved_errno is EADDRNOTAVAIL when we asked for family

1708 \* AF_UNSPEC, it might be because IPv6 is disabled for this

1709 \* particular interface (e.g. Linux with

1710 \* /proc/sys/net/ipv6/conf/lo/disable_ipv6).

1711 \*/

1712 bind_error = dbus_new0 (DBusError, 1);

1713

1714 if (bind_error == NULL)

1715 {

1716 \_DBUS_SET_OOM (error);

1717 goto failed;

1718 }

1719

1720 dbus_error_init (bind_error);

1721 \_dbus_set_error_with_inet_sockaddr (bind_error, tmp-\>ai_addr, tmp-\>ai_addrlen,

1722 "Failed to bind socket",

1723 saved_errno);

1724

1725 if (!\_dbus_list_append (&bind_errors, bind_error))

1726 {

1727 dbus_error_free (bind_error);

1728 dbus_free (bind_error);

1729 \_DBUS_SET_OOM (error);

1730 goto failed;

1731 }

1732

1733 /\* Try the next address, maybe it will work better \*/

1734 tmp = tmp-\>ai_next;

1735 continue;

1736 }

1737

1738 if (listen (fd, 30 /\* backlog \*/) \< 0)

1739 {

1740 saved_errno = errno;

1741 \_dbus_close (fd, NULL);

1742 \_dbus_set_error_with_inet_sockaddr (error, tmp-\>ai_addr, tmp-\>ai_addrlen,

1743 "Failed to listen on socket",

1744 saved_errno);

1745 goto failed;

1746 }

1747

1748 newlisten_fd = dbus_realloc(listen_fd, sizeof(DBusSocket)\*(nlisten_fd+1));

1749 if (!newlisten_fd)

1750 {

1751 \_dbus_close (fd, NULL);

1752 dbus_set_error (error, DBUS_ERROR_NO_MEMORY,

1753 "Failed to allocate file handle array");

1754 goto failed;

1755 }

1756 listen_fd = newlisten_fd;

1757 listen_fd\[nlisten_fd\].fd = fd;

1758 nlisten_fd++;

1759

1760 if (tmp-\>ai_addr-\>sa_family == AF_INET)

1761 have_ipv4 = TRUE;

1762 else if (tmp-\>ai_addr-\>sa_family == AF_INET6)

1763 have_ipv6 = TRUE;

1764

1765 if (!\_dbus_string_get_length(retport))

1766 {

1767 /\* If the user didn't specify a port, or used 0, then

1768 the kernel chooses a port. After the first address

1769 is bound to, we need to force all remaining addresses

1770 to use the same port \*/

1771 if (!port \|\| !strcmp(port, "0"))

1772 {

1773 int result;

1774 struct sockaddr_storage addr;

1775 socklen_t addrlen;

1776 char portbuf\[50\];

1777

1778 addrlen = sizeof(addr);

1779 result = getsockname(fd, (struct sockaddr\*) &addr, &addrlen);

1780

1781 if (result == -1)

1782 {

1783 saved_errno = errno;

1784 dbus_set_error (error, \_dbus_error_from_errno (saved_errno),

1785 "Failed to retrieve socket name for \\%s:%s\\: %s",

1786 host ? host : "\*", port ? port : "0", \_dbus_strerror (saved_errno));

1787 goto failed;

1788 }

1789

1790 if ((res = getnameinfo ((struct sockaddr\*)&addr, addrlen, NULL, 0,

1791 portbuf, sizeof(portbuf),

1792 NI_NUMERICHOST \| NI_NUMERICSERV)) != 0)

1793 {

1794 saved_errno = errno;

1795 dbus_set_error (error, \_dbus_error_from_gai (res, saved_errno),

1796 "Failed to resolve port \\%s:%s\\: %s (%d)",

1797 host ? host : "\*", port ? port : "0", gai_strerror(res), res);

1798 goto failed;

1799 }

1800

1801 if (!\_dbus_string_append(retport, portbuf))

1802 {

1803 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

1804 goto failed;

1805 }

1806

1807 /\* Release current address list & redo lookup \*/

1808 port = \_dbus_string_get_const_data(retport);

1809 freeaddrinfo(ai);

1810 goto redo_lookup_with_port;

1811 }

1812 else

1813 {

1814 if (!\_dbus_string_append(retport, port))

1815 {

1816 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

1817 goto failed;

1818 }

1819 }

1820 }

1821

1822 tmp = tmp-\>ai_next;

1823 }

1824 freeaddrinfo(ai);

1825 ai = NULL;

1826

1827 if (!nlisten_fd)

1828 {

1829 \_dbus_combine_tcp_errors (&bind_errors, "Failed to bind", host,

1830 port, error);

1831 goto failed;

1832 }

1833

1834 if (have_ipv4 && !have_ipv6)

1835 \*retfamily = "ipv4";

1836 else if (!have_ipv4 && have_ipv6)

1837 \*retfamily = "ipv6";

1838

1839 for (i = 0 ; i \< nlisten_fd ; i++)

1840 {

1841 if (!\_dbus_set_fd_nonblocking (listen_fd\[i\].fd, error))

1842 {

1843 goto failed;

1844 }

1845 }

1846

1847 \*fds_p = listen_fd;

1848

1849 /\* This list might be non-empty even on success, because we might be

1850 \* ignoring EADDRINUSE or EADDRNOTAVAIL \*/

1851 while ((bind_error = \_dbus_list_pop_first (&bind_errors)))

1852 {

1853 dbus_error_free (bind_error);

1854 dbus_free (bind_error);

1855 }

1856

1857 return nlisten_fd;

1858

1859 failed:

1860 if (ai)

1861 freeaddrinfo(ai);

1862 for (i = 0 ; i \< nlisten_fd ; i++)

1863 \_dbus_close(listen_fd\[i\].fd, NULL);

1864

1865 while ((bind_error = \_dbus_list_pop_first (&bind_errors)))

1866 {

1867 dbus_error_free (bind_error);

1868 dbus_free (bind_error);

1869 }

1870

1871 dbus_free(listen_fd);

1872 return -1;

1873}

1874

1875static dbus_bool_t

1876write_credentials_byte (int server_fd,

1877 DBusError \*error)

1878{

1879 int bytes_written;

1880 char buf\[1\] = { '\0' };

1881\#if defined(HAVE_CMSGCRED)

1882 union {

1883 struct cmsghdr hdr;

1884 char cred\[CMSG_SPACE (sizeof (struct cmsgcred))\];

1885 } cmsg;

1886 struct iovec iov;

1887 struct msghdr msg;

1888 iov.iov_base = buf;

1889 iov.iov_len = 1;

1890

1891 \_DBUS_ZERO(msg);

1892 msg.msg_iov = &iov;

1893 msg.msg_iovlen = 1;

1894

1895 msg.msg_control = (caddr_t) &cmsg;

1896 msg.msg_controllen = CMSG_SPACE (sizeof (struct cmsgcred));

1897 \_DBUS_ZERO(cmsg);

1898 cmsg.hdr.cmsg_len = CMSG_LEN (sizeof (struct cmsgcred));

1899 cmsg.hdr.cmsg_level = SOL_SOCKET;

1900 cmsg.hdr.cmsg_type = SCM_CREDS;

1901\#endif

1902

1903 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

1904

1905 again:

1906

1907\#if defined(HAVE_CMSGCRED)

1908 bytes_written = sendmsg (server_fd, &msg, 0

1909\#if HAVE_DECL_MSG_NOSIGNAL

1910 \|MSG_NOSIGNAL

1911\#endif

1912 );

1913

1914 /\* If we HAVE_CMSGCRED, the OS still might not let us sendmsg()

1915 \* with a SOL_SOCKET/SCM_CREDS message - for instance, FreeBSD

1916 \* only allows that on AF_UNIX. Try just doing a send() instead. \*/

1917 if (bytes_written \< 0 && errno == EINVAL)

1918\#endif

1919 {

1920 bytes_written = send (server_fd, buf, 1, 0

1921\#if HAVE_DECL_MSG_NOSIGNAL

1922 \|MSG_NOSIGNAL

1923\#endif

1924 );

1925 }

1926

1927 if (bytes_written \< 0 && errno == EINTR)

1928 goto again;

1929

1930 if (bytes_written \< 0)

1931 {

1932 dbus_set_error (error, \_dbus_error_from_errno (errno),

1933 "Failed to write credentials byte: %s",

1934 \_dbus_strerror (errno));

1935 return FALSE;

1936 }

1937 else if (bytes_written == 0)

1938 {

1939 dbus_set_error (error, DBUS_ERROR_IO_ERROR,

1940 "wrote zero bytes writing credentials byte");

1941 return FALSE;

1942 }

1943 else

1944 {

1945 \_dbus_assert (bytes_written == 1);

1946 \_dbus_verbose ("wrote credentials byte\n");

1947 return TRUE;

1948 }

1949}

1950

1951/\* return FALSE on OOM, TRUE otherwise, even if no groups were found \*/

1952static dbus_bool_t

1953add_groups_to_credentials (int client_fd,

1954 DBusCredentials \*credentials,

1955 dbus_gid_t primary)

1956{

1957\#if defined(\_\_linux\_\_) && defined(SO_PEERGROUPS)

1958 \_DBUS_STATIC_ASSERT (sizeof (gid_t) \<= sizeof (dbus_gid_t));

1959 /\* This function assumes socklen_t is unsigned, which is true on Linux \*/

1960 \_DBUS_STATIC_ASSERT (((socklen_t) -1) \> 0);

1961 gid_t \*buf = NULL;

1962 socklen_t len = 1024;

1963 dbus_bool_t oom = FALSE;

1964 /\* libdbus has a different representation of group IDs just to annoy you \*/

1965 dbus_gid_t \*converted_gids = NULL;

1966 dbus_bool_t need_primary = TRUE;

1967 size_t n_gids;

1968 size_t i;

1969

1970 n_gids = ((size_t) len) / sizeof (gid_t);

1971 buf = dbus_new (gid_t, n_gids);

1972

1973 if (buf == NULL)

1974 return FALSE;

1975

1976 while (getsockopt (client_fd, SOL_SOCKET, SO_PEERGROUPS, buf, &len) \< 0)

1977 {

1978 int e = errno;

1979 gid_t \*replacement;

1980

1981 \_dbus_verbose ("getsockopt failed with %s, len now %lu\n",

1982 \_dbus_strerror (e), (unsigned long) len);

1983

1984 if (e != ERANGE \|\| (size_t) len \<= n_gids \* sizeof (gid_t))

1985 {

1986 \_dbus_verbose ("Failed to getsockopt(SO_PEERGROUPS): %s\n",

1987 \_dbus_strerror (e));

1988 goto out;

1989 }

1990

1991 /\* If not enough space, len is updated to be enough.

1992 \* Try again with a large enough buffer. \*/

1993 n_gids = ((size_t) len) / sizeof (gid_t);

1994 replacement = dbus_realloc (buf, len);

1995

1996 if (replacement == NULL)

1997 {

1998 oom = TRUE;

1999 goto out;

2000 }

2001

2002 buf = replacement;

2003 \_dbus_verbose ("will try again with %lu\n", (unsigned long) len);

2004 }

2005

2006 if (len \> n_gids \* sizeof (gid_t))

2007 {

2008 \_dbus_verbose ("%lu \> %zu", (unsigned long) len, n_gids \* sizeof (gid_t));

2009 \_dbus_assert_not_reached ("getsockopt(SO_PEERGROUPS) overflowed");

2010 }

2011

2012 if (len % sizeof (gid_t) != 0)

2013 {

2014 \_dbus_verbose ("getsockopt(SO_PEERGROUPS) did not return an "

2015 "integer multiple of sizeof(gid_t): %lu should be "

2016 "divisible by %zu",

2017 (unsigned long) len, sizeof (gid_t));

2018 goto out;

2019 }

2020

2021 /\* Allocate an extra space for the primary group ID \*/

2022 n_gids = ((size_t) len) / sizeof (gid_t);

2023

2024 /\* If n_gids is less than this, then (n_gids + 1) certainly doesn't

2025 \* overflow, and neither does multiplying that by sizeof(dbus_gid_t).

2026 \* This is using \_DBUS_INT32_MAX as a conservative lower bound for

2027 \* the maximum size_t. \*/

2028 if (n_gids \>= (\_DBUS_INT32_MAX / sizeof (dbus_gid_t)) - 1)

2029 {

2030 \_dbus_verbose ("getsockopt(SO_PEERGROUPS) returned a huge number "

2031 "of groups (%lu bytes), ignoring",

2032 (unsigned long) len);

2033 goto out;

2034 }

2035

2036 converted_gids = dbus_new (dbus_gid_t, n_gids + 1);

2037

2038 if (converted_gids == NULL)

2039 {

2040 oom = TRUE;

2041 goto out;

2042 }

2043

2044 for (i = 0; i \< n_gids; i++)

2045 {

2046 converted_gids\[i\] = (dbus_gid_t) buf\[i\];

2047

2048 if (converted_gids\[i\] == primary)

2049 need_primary = FALSE;

2050 }

2051

2052 if (need_primary && primary != DBUS_GID_UNSET)

2053 {

2054 converted_gids\[n_gids\] = primary;

2055 n_gids++;

2056 }

2057

2058 \_dbus_credentials_take_unix_gids (credentials, converted_gids, n_gids);

2059

2060out:

2061 dbus_free (buf);

2062 return !oom;

2063\#else

2064 /\* no error \*/

2065 return TRUE;

2066\#endif

2067}

2068

2069/\* return FALSE on OOM, TRUE otherwise, even if no credentials were found \*/

2070static dbus_bool_t

2071add_linux_security_label_to_credentials (int client_fd,

2072 DBusCredentials \*credentials)

2073{

2074\#if defined(\_\_linux\_\_) && defined(SO_PEERSEC)

2075 DBusString buf;

2076 socklen_t len = 1024;

2077 dbus_bool_t oom = FALSE;

2078

2079 if (!\_dbus_string_init_preallocated (&buf, len) \|\|

2080 !\_dbus_string_set_length (&buf, len))

2081 return FALSE;

2082

2083 while (getsockopt (client_fd, SOL_SOCKET, SO_PEERSEC,

2084 \_dbus_string_get_data (&buf), &len) \< 0)

2085 {

2086 int e = errno;

2087

2088 \_dbus_verbose ("getsockopt failed with %s, len now %lu\n",

2089 \_dbus_strerror (e), (unsigned long) len);

2090

2091 if (e != ERANGE \|\| len \<= \_dbus_string_get_length_uint (&buf))

2092 {

2093 \_dbus_verbose ("Failed to getsockopt(SO_PEERSEC): %s\n",

2094 \_dbus_strerror (e));

2095 goto out;

2096 }

2097

2098 /\* If not enough space, len is updated to be enough.

2099 \* Try again with a large enough buffer. \*/

2100 if (!\_dbus_string_set_length (&buf, len))

2101 {

2102 oom = TRUE;

2103 goto out;

2104 }

2105

2106 \_dbus_verbose ("will try again with %lu\n", (unsigned long) len);

2107 }

2108

2109 if (len \<= 0)

2110 {

2111 \_dbus_verbose ("getsockopt(SO_PEERSEC) yielded \<= 0 bytes: %lu\n",

2112 (unsigned long) len);

2113 goto out;

2114 }

2115

2116 if (len \> \_dbus_string_get_length_uint (&buf))

2117 {

2118 \_dbus_verbose ("%lu \> %u", (unsigned long) len,

2119 \_dbus_string_get_length_uint (&buf));

2120 \_dbus_assert_not_reached ("getsockopt(SO_PEERSEC) overflowed");

2121 }

2122

2123 if (\_dbus_string_get_byte (&buf, len - 1) == 0)

2124 {

2125 /\* the kernel included the trailing \0 in its count,

2126 \* but DBusString always has an extra \0 after the data anyway \*/

2127 \_dbus_verbose ("subtracting trailing \\0\n");

2128 len--;

2129 }

2130

2131 if (!\_dbus_string_set_length (&buf, len))

2132 {

2133 \_dbus_assert_not_reached ("shortening string should not lead to OOM");

2134 oom = TRUE;

2135 goto out;

2136 }

2137

2138 if (strlen (\_dbus_string_get_const_data (&buf)) != len)

2139 {

2140 /\* LSM people on the linux-security-module@ mailing list say this

2141 \* should never happen: the label should be a bytestring with

2142 \* an optional trailing \0 \*/

2143 \_dbus_verbose ("security label from kernel had an embedded \\0, "

2144 "ignoring it\n");

2145 goto out;

2146 }

2147

2148 \_dbus_verbose ("getsockopt(SO_PEERSEC): %lu bytes excluding \\0: %s\n",

2149 (unsigned long) len,

2150 \_dbus_string_get_const_data (&buf));

2151

2152 if (!\_dbus_credentials_add_linux_security_label (credentials,

2153 \_dbus_string_get_const_data (&buf)))

2154 {

2155 oom = TRUE;

2156 goto out;

2157 }

2158

2159out:

2160 \_dbus_string_free (&buf);

2161 return !oom;

2162\#else

2163 /\* no error \*/

2164 return TRUE;

2165\#endif

2166}

2167

2208dbus_bool_t

2209\_dbus_read_credentials_socket (DBusSocket client_fd,

2210 DBusCredentials \*credentials,

2211 DBusError \*error)

2212{

2213 struct msghdr msg;

2214 struct iovec iov;

2215 char buf;

2216 dbus_uid_t uid_read;

2217 dbus_gid_t primary_gid_read;

2218 dbus_pid_t pid_read;

2219 int bytes_read;

2220 int pid_fd_read;

2221

2222\#ifdef HAVE_CMSGCRED

2223 union {

2224 struct cmsghdr hdr;

2225 char cred\[CMSG_SPACE (sizeof (struct cmsgcred))\];

2226 } cmsg;

2227\#endif

2228

2229 /\* The POSIX spec certainly doesn't promise this, but

2230 \* we need these assertions to fail as soon as we're wrong about

2231 \* it so we can do the porting fixups

2232 \*/

2233 \_DBUS_STATIC_ASSERT (sizeof (pid_t) \<= sizeof (dbus_pid_t));

2234 \_DBUS_STATIC_ASSERT (sizeof (uid_t) \<= sizeof (dbus_uid_t));

2235 \_DBUS_STATIC_ASSERT (sizeof (gid_t) \<= sizeof (dbus_gid_t));

2236

2237 uid_read = DBUS_UID_UNSET;

2238 primary_gid_read = DBUS_GID_UNSET;

2239 pid_read = DBUS_PID_UNSET;

2240 pid_fd_read = -1;

2241

2242 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

2243

2244 \_dbus_credentials_clear (credentials);

2245

2246 iov.iov_base = &buf;

2247 iov.iov_len = 1;

2248

2249 \_DBUS_ZERO(msg);

2250 msg.msg_iov = &iov;

2251 msg.msg_iovlen = 1;

2252

2253\#if defined(HAVE_CMSGCRED)

2254 \_DBUS_ZERO(cmsg);

2255 msg.msg_control = (caddr_t) &cmsg;

2256 msg.msg_controllen = CMSG_SPACE (sizeof (struct cmsgcred));

2257\#endif

2258

2259 again:

2260 bytes_read = recvmsg (client_fd.fd, &msg, 0);

2261

2262 if (bytes_read \< 0)

2263 {

2264 if (errno == EINTR)

2265 goto again;

2266

2267 /\* EAGAIN or EWOULDBLOCK would be unexpected here since we would

2268 \* normally only call read_credentials if the socket was ready

2269 \* for reading

2270 \*/

2271

2272 dbus_set_error (error, \_dbus_error_from_errno (errno),

2273 "Failed to read credentials byte: %s",

2274 \_dbus_strerror (errno));

2275 return FALSE;

2276 }

2277 else if (bytes_read == 0)

2278 {

2279 /\* this should not happen unless we are using recvmsg wrong,

2280 \* so is essentially here for paranoia

2281 \*/

2282 dbus_set_error (error, DBUS_ERROR_FAILED,

2283 "Failed to read credentials byte (zero-length read)");

2284 return FALSE;

2285 }

2286 else if (buf != '\0')

2287 {

2288 dbus_set_error (error, DBUS_ERROR_FAILED,

2289 "Credentials byte was not nul");

2290 return FALSE;

2291 }

2292

2293 \_dbus_verbose ("read credentials byte\n");

2294

2295 {

2296\#ifdef SO_PEERCRED

2297 /\* Supported by at least Linux and OpenBSD, with minor differences.

2298 \*

2299 \* This mechanism passes the process ID through and does not require

2300 \* the peer's cooperation, so we prefer it over all others. Notably,

2301 \* Linux also supports SCM_CREDENTIALS, which is similar to FreeBSD

2302 \* SCM_CREDS; it's implemented in GIO, but we don't use it in dbus at all,

2303 \* because this is much less fragile.

2304 \*/

2305\#ifdef \_\_OpenBSD\_\_

2306 struct sockpeercred cr;

2307\#else

2308 struct ucred cr;

2309\#endif

2310 socklen_t cr_len = sizeof (cr);

2311

2312 if (getsockopt (client_fd.fd, SOL_SOCKET, SO_PEERCRED, &cr, &cr_len) != 0)

2313 {

2314 \_dbus_verbose ("Failed to getsockopt(SO_PEERCRED): %s\n",

2315 \_dbus_strerror (errno));

2316 }

2317 else if (cr_len != sizeof (cr))

2318 {

2319 \_dbus_verbose ("Failed to getsockopt(SO_PEERCRED), returned %d bytes, expected %d\n",

2320 cr_len, (int) sizeof (cr));

2321 }

2322 else

2323 {

2324 if (cr.pid != 0)

2325 pid_read = cr.pid;

2326

2327 if (cr.uid != (uid_t)-1)

2328 uid_read = cr.uid;

2329\#ifdef \_\_linux\_\_

2330 /\* Do other platforms have cr.gid? (Not that it really matters,

2331 \* because the gid is useless to us unless we know the complete

2332 \* group vector, which we only know on Linux.) \*/

2333 if (cr.gid != (gid_t)-1)

2334 primary_gid_read = cr.gid;

2335\#endif

2336 }

2337

2338\#ifdef SO_PEERPIDFD

2339 /\* If we have SO_PEERCRED we might also have SO_PEERPIDFD, which

2340 \* allows to pin the process ID, and is available on Linux since v6.5. \*/

2341 cr_len = sizeof (int);

2342

2343 if (getsockopt (client_fd.fd, SOL_SOCKET, SO_PEERPIDFD, &pid_fd_read, &cr_len) != 0)

2344 {

2345 \_dbus_verbose ("Failed to getsockopt(SO_PEERPIDFD): %s\n",

2346 \_dbus_strerror (errno));

2347 }

2348 else if (cr_len != sizeof (int))

2349 {

2350 \_dbus_verbose ("Failed to getsockopt(SO_PEERPIDFD), returned %d bytes, expected %d\n",

2351 cr_len, (int) sizeof (int));

2352 }

2353\#endif

2354

2355\#elif defined(HAVE_UNPCBID) && defined(LOCAL_PEEREID)

2356 /\* Another variant of the above - used on NetBSD

2357 \*/

2358 struct unpcbid cr;

2359 socklen_t cr_len = sizeof (cr);

2360

2361 if (getsockopt (client_fd.fd, 0, LOCAL_PEEREID, &cr, &cr_len) != 0)

2362 {

2363 \_dbus_verbose ("Failed to getsockopt(LOCAL_PEEREID): %s\n",

2364 \_dbus_strerror (errno));

2365 }

2366 else if (cr_len != sizeof (cr))

2367 {

2368 \_dbus_verbose ("Failed to getsockopt(LOCAL_PEEREID), returned %d bytes, expected %d\n",

2369 cr_len, (int) sizeof (cr));

2370 }

2371 else

2372 {

2373 pid_read = cr.unp_pid;

2374 uid_read = cr.unp_euid;

2375 }

2376\#elif defined(HAVE_CMSGCRED)

2377 /\* We only check for HAVE_CMSGCRED, but we're really assuming that the

2378 \* presence of that struct implies SCM_CREDS. Supported by at least

2379 \* FreeBSD and DragonflyBSD.

2380 \*

2381 \* This mechanism requires the peer to help us (it has to send us a

2382 \* SCM_CREDS message) but it does pass the process ID through,

2383 \* which makes it better than getpeereid().

2384 \*/

2385 struct cmsgcred \*cred;

2386 struct cmsghdr \*cmsgp;

2387

2388 for (cmsgp = CMSG_FIRSTHDR (&msg);

2389 cmsgp != NULL;

2390 cmsgp = CMSG_NXTHDR (&msg, cmsgp))

2391 {

2392 if (cmsgp-\>cmsg_type == SCM_CREDS &&

2393 cmsgp-\>cmsg_level == SOL_SOCKET &&

2394 cmsgp-\>cmsg_len \>= CMSG_LEN (sizeof (struct cmsgcred)))

2395 {

2396 cred = (struct cmsgcred \*) (void \*) CMSG_DATA (cmsgp);

2397 pid_read = cred-\>cmcred_pid;

2398 uid_read = cred-\>cmcred_euid;

2399 break;

2400 }

2401 }

2402

2403\#elif defined(HAVE_GETPEERUCRED)

2404 /\* Supported in at least Solaris \>= 10. It should probably be higher

2405 \* up this list, because it carries the pid and we use this code path

2406 \* for audit data. \*/

2407 ucred_t \* ucred = NULL;

2408 if (getpeerucred (client_fd.fd, &ucred) == 0)

2409 {

2410\#ifdef HAVE_ADT

2411 adt_session_data_t \*adth = NULL;

2412\#endif

2413 pid_read = ucred_getpid (ucred);

2414 uid_read = ucred_geteuid (ucred);

2415\#ifdef HAVE_ADT

2416 /\* generate audit session data based on socket ucred \*/

2417 if (adt_start_session (&adth, NULL, 0) \|\| (adth == NULL))

2418 {

2419 \_dbus_verbose ("Failed to adt_start_session(): %s\n", \_dbus_strerror (errno));

2420 }

2421 else

2422 {

2423 if (adt_set_from_ucred (adth, ucred, ADT_NEW))

2424 {

2425 \_dbus_verbose ("Failed to adt_set_from_ucred(): %s\n", \_dbus_strerror (errno));

2426 }

2427 else

2428 {

2429 adt_export_data_t \*data = NULL;

2430 size_t size = adt_export_session_data (adth, &data);

2431 if (size \<= 0)

2432 {

2433 \_dbus_verbose ("Failed to adt_export_session_data(): %s\n", \_dbus_strerror (errno));

2434 }

2435 else

2436 {

2437 \_dbus_credentials_add_adt_audit_data (credentials, data, size);

2438 free (data);

2439 }

2440 }

2441 (void) adt_end_session (adth);

2442 }

2443\#endif /\* HAVE_ADT \*/

2444 }

2445 else

2446 {

2447 \_dbus_verbose ("Failed to getpeerucred() credentials: %s\n", \_dbus_strerror (errno));

2448 }

2449 if (ucred != NULL)

2450 ucred_free (ucred);

2451

2452 /\* ----------------------------------------------------------------

2453 \* When adding new mechanisms, please add them above this point

2454 \* if they support passing the process ID through, or below if not.

2455 \* ---------------------------------------------------------------- \*/

2456

2457\#elif defined(HAVE_GETPEEREID)

2458 /\* getpeereid() originates from D.J. Bernstein and is fairly

2459 \* widely-supported. According to a web search, it might be present in

2460 \* any/all of:

2461 \*

2462 \* - AIX?

2463 \* - Blackberry?

2464 \* - Cygwin

2465 \* - FreeBSD 4.6+ (but we prefer SCM_CREDS: it carries the pid)

2466 \* - Mac OS X

2467 \* - Minix 3.1.8+

2468 \* - MirBSD?

2469 \* - NetBSD 5.0+ (but LOCAL_PEEREID would be better: it carries the pid)

2470 \* - OpenBSD 3.0+ (but we prefer SO_PEERCRED: it carries the pid)

2471 \* - QNX?

2472 \*/

2473 uid_t euid;

2474 gid_t egid;

2475 if (getpeereid (client_fd.fd, &euid, &egid) == 0)

2476 {

2477 uid_read = euid;

2478 }

2479 else

2480 {

2481 \_dbus_verbose ("Failed to getpeereid() credentials: %s\n", \_dbus_strerror (errno));

2482 }

2483\#else /\* no supported mechanism \*/

2484

2485\#warning Socket credentials not supported on this Unix OS

2486\#warning Please tell https://gitlab.freedesktop.org/dbus/dbus/-/issues/new

2487

2488 /\* Please add other operating systems known to support at least one of

2489 \* the mechanisms above to this list, keeping alphabetical order.

2490 \* Everything not in this list is best-effort.

2491 \*/

2492\#if defined(\_\_FreeBSD\_\_) \|\| defined(\_\_FreeBSD_kernel\_\_) \|\| \\

2493 defined(\_\_linux\_\_) \|\| \\

2494 defined(\_\_OpenBSD\_\_) \|\| \\

2495 defined(\_\_NetBSD\_\_)

2496\# error Credentials passing not working on this OS is a regression!

2497\#endif

2498

2499 \_dbus_verbose ("Socket credentials not supported on this OS\n");

2500\#endif

2501 }

2502

2503 \_dbus_verbose ("Credentials:"

2504 " pid "DBUS_PID_FORMAT

2505 " uid "DBUS_UID_FORMAT

2506 "\n",

2507 pid_read,

2508 uid_read);

2509

2510 /\* Assign this first, so we don't have to close it manually in case one of

2511 \* the next steps fails. \*/

2512 if (pid_fd_read \>= 0)

2513 \_dbus_credentials_take_pid_fd (credentials, pid_fd_read);

2514

2515 if (pid_read != DBUS_PID_UNSET)

2516 {

2517 if (!\_dbus_credentials_add_pid (credentials, pid_read))

2518 {

2519 \_DBUS_SET_OOM (error);

2520 return FALSE;

2521 }

2522 }

2523

2524 if (uid_read != DBUS_UID_UNSET)

2525 {

2526 if (!\_dbus_credentials_add_unix_uid (credentials, uid_read))

2527 {

2528 \_DBUS_SET_OOM (error);

2529 return FALSE;

2530 }

2531 }

2532

2533 if (!add_linux_security_label_to_credentials (client_fd.fd, credentials))

2534 {

2535 \_DBUS_SET_OOM (error);

2536 return FALSE;

2537 }

2538

2539 /\* We don't put any groups in the credentials unless we can put them

2540 \* all there. \*/

2541 if (!add_groups_to_credentials (client_fd.fd, credentials, primary_gid_read))

2542 {

2543 \_DBUS_SET_OOM (error);

2544 return FALSE;

2545 }

2546

2547 return TRUE;

2548}

2549

2567dbus_bool_t

2568\_dbus_send_credentials_socket (DBusSocket server_fd,

2569 DBusError \*error)

2570{

2571 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

2572

2573 if (write_credentials_byte (server_fd.fd, error))

2574 return TRUE;

2575 else

2576 return FALSE;

2577}

2578

2588DBusSocket

2589\_dbus_accept (DBusSocket listen_fd)

2590{

2591 DBusSocket client_fd;

2592 struct sockaddr addr;

2593 socklen_t addrlen;

2594\#ifdef HAVE_ACCEPT4

2595 dbus_bool_t cloexec_done;

2596\#endif

2597

2598 addrlen = sizeof (addr);

2599

2600 retry:

2601

2602\#ifdef HAVE_ACCEPT4

2603 /\*

2604 \* At compile-time, we assume that if accept4() is available in

2605 \* libc headers, SOCK_CLOEXEC is too. At runtime, it is still

2606 \* not necessarily true that either is supported by the running kernel.

2607 \*/

2608 client_fd.fd = accept4 (listen_fd.fd, &addr, &addrlen, SOCK_CLOEXEC);

2609 cloexec_done = client_fd.fd \>= 0;

2610

2611 if (client_fd.fd \< 0 && (errno == ENOSYS \|\| errno == EINVAL))

2612\#endif

2613 {

2614 client_fd.fd = accept (listen_fd.fd, &addr, &addrlen);

2615 }

2616

2617 if (client_fd.fd \< 0)

2618 {

2619 if (errno == EINTR)

2620 goto retry;

2621 }

2622

2623 \_dbus_verbose ("client fd %d accepted\n", client_fd.fd);

2624

2625\#ifdef HAVE_ACCEPT4

2626 if (!cloexec_done)

2627\#endif

2628 {

2629 \_dbus_fd_set_close_on_exec(client_fd.fd);

2630 }

2631

2632 return client_fd;

2633}

2634

2643dbus_bool_t

2644\_dbus_check_dir_is_private_to_user (DBusString \*dir, DBusError \*error)

2645{

2646 const char \*directory;

2647 struct stat sb;

2648

2649 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

2650

2651 directory = \_dbus_string_get_const_data (dir);

2652

2653 if (stat (directory, &sb) \< 0)

2654 {

2655 dbus_set_error (error, \_dbus_error_from_errno (errno),

2656 "%s", \_dbus_strerror (errno));

2657

2658 return FALSE;

2659 }

2660

2661 if (sb.st_uid != geteuid ())

2662 {

2663 dbus_set_error (error, DBUS_ERROR_FAILED,

2664 "%s directory is owned by user %lu, not %lu",

2665 directory,

2666 (unsigned long) sb.st_uid,

2667 (unsigned long) geteuid ());

2668 return FALSE;

2669 }

2670

2671 if ((S_IROTH & sb.st_mode) \|\| (S_IWOTH & sb.st_mode) \|\|

2672 (S_IRGRP & sb.st_mode) \|\| (S_IWGRP & sb.st_mode))

2673 {

2674 dbus_set_error (error, DBUS_ERROR_FAILED,

2675 "%s directory is not private to the user", directory);

2676 return FALSE;

2677 }

2678

2679 return TRUE;

2680}

2681

2682static dbus_bool_t

2683fill_user_info_from_passwd (struct passwd \*p,

2684 DBusUserInfo \*info,

2685 DBusError \*error)

2686{

2687 \_dbus_assert (p-\>pw_name != NULL);

2688 \_dbus_assert (p-\>pw_dir != NULL);

2689

2690 info-\>uid = p-\>pw_uid;

2691 info-\>primary_gid = p-\>pw_gid;

2692 info-\>username = \_dbus_strdup (p-\>pw_name);

2693 info-\>homedir = \_dbus_strdup (p-\>pw_dir);

2694

2695 if (info-\>username == NULL \|\|

2696 info-\>homedir == NULL)

2697 {

2698 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

2699 return FALSE;

2700 }

2701

2702 return TRUE;

2703}

2704

2705static dbus_bool_t

2706fill_user_info (DBusUserInfo \*info,

2707 dbus_uid_t uid,

2708 const DBusString \*username,

2709 DBusError \*error)

2710{

2711 const char \*username_c;

2712

2713 /\* exactly one of username/uid provided \*/

2714 \_dbus_assert (username != NULL \|\| uid != DBUS_UID_UNSET);

2715 \_dbus_assert (username == NULL \|\| uid == DBUS_UID_UNSET);

2716

2717 info-\>uid = DBUS_UID_UNSET;

2718 info-\>primary_gid = DBUS_GID_UNSET;

2719 info-\>group_ids = NULL;

2720 info-\>n_group_ids = 0;

2721 info-\>username = NULL;

2722 info-\>homedir = NULL;

2723

2724 if (username != NULL)

2725 username_c = \_dbus_string_get_const_data (username);

2726 else

2727 username_c = NULL;

2728

2729 /\* For now assuming that the getpwnam() and getpwuid() flavors

2730 \* are always symmetrical, if not we have to add more configure

2731 \* checks

2732 \*/

2733

2734 {

2735 struct passwd \*p;

2736 char \*buf = NULL;

2737 int result;

2738\#ifdef HAVE_GETPWNAM_R

2739 size_t buflen;

2740 struct passwd p_str;

2741

2742 /\* retrieve maximum needed size for buf \*/

2743 buflen = sysconf (\_SC_GETPW_R_SIZE_MAX);

2744

2745 /\* sysconf actually returns a long, but everything else expects size_t,

2746 \* so just recast here.

2747 \* https://bugs.freedesktop.org/show_bug.cgi?id=17061

2748 \*/

2749 if ((long) buflen \<= 0)

2750 buflen = 1024;

2751

2752 result = -1;

2753 while (1)

2754 {

2755 buf = dbus_malloc (buflen);

2756 if (buf == NULL)

2757 {

2758 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

2759 return FALSE;

2760 }

2761

2762 p = NULL;

2763 if (uid != DBUS_UID_UNSET)

2764 result = getpwuid_r (uid, &p_str, buf, buflen,

2765 &p);

2766 else

2767 result = getpwnam_r (username_c, &p_str, buf, buflen,

2768 &p);

2769 //Try a bigger buffer if ERANGE was returned

2770 if (result == ERANGE && buflen \< 512 \* 1024)

2771 {

2772 dbus_free (buf);

2773 buflen \*= 2;

2774 }

2775 else

2776 {

2777 break;

2778 }

2779 }

2780

2781 /\* There are three possibilities:

2782 \* - an error: result is a nonzero error code, p should be NULL

2783 \* - name or uid not found: result is 0, p is NULL

2784 \* - success: result is 0, p should be &p_str

2785 \*

2786 \* Ensure that in all failure cases, p is set to NULL, matching the

2787 \* getpwuid/getpwnam interface. \*/

2788 if (result != 0 \|\| p != &p_str)

2789 p = NULL;

2790

2791\#else /\* ! HAVE_GETPWNAM_R \*/

2792 /\* I guess we're screwed on thread safety here \*/

2793\#warning getpwnam_r() not available, please report this to the dbus maintainers with details of your OS

2794

2795 /\* It is unspecified whether "failed to find" counts as an error,

2796 \* or whether it's reported as p == NULL without touching errno.

2797 \* Reset errno so we can distinguish. \*/

2798 errno = 0;

2799

2800 if (uid != DBUS_UID_UNSET)

2801 p = getpwuid (uid);

2802 else

2803 p = getpwnam (username_c);

2804

2805 /\* Always initialized, but only meaningful if p is NULL \*/

2806 result = errno;

2807\#endif /\* ! HAVE_GETPWNAM_R \*/

2808

2809 if (p != NULL)

2810 {

2811 if (!fill_user_info_from_passwd (p, info, error))

2812 {

2813 dbus_free (buf);

2814 return FALSE;

2815 }

2816 dbus_free (buf);

2817 }

2818 else

2819 {

2820 DBusError local_error = DBUS_ERROR_INIT;

2821 const char \*error_str;

2822

2823 if (result == 0)

2824 error_str = "not found";

2825 else

2826 error_str = \_dbus_strerror (result);

2827

2828 if (uid != DBUS_UID_UNSET)

2829 dbus_set_error (&local_error, \_dbus_error_from_errno (result),

2830 "Looking up user ID " DBUS_UID_FORMAT ": %s",

2831 uid, error_str);

2832 else

2833 dbus_set_error (&local_error, \_dbus_error_from_errno (result),

2834 "Looking up user \\%s\\: %s",

2835 username_c ? username_c : "???", error_str);

2836

2837 \_dbus_verbose ("%s", local_error.message);

2838 dbus_move_error (&local_error, error);

2839 dbus_free (buf);

2840 return FALSE;

2841 }

2842 }

2843

2844 /\* Fill this in so we can use it to get groups \*/

2845 username_c = info-\>username;

2846

2847\#ifdef HAVE_GETGROUPLIST

2848 {

2849 gid_t \*buf;

2850 int buf_count;

2851 int i;

2852 int initial_buf_count;

2853

2854 initial_buf_count = 17;

2855 buf_count = initial_buf_count;

2856 buf = dbus_new (gid_t, buf_count);

2857 if (buf == NULL)

2858 {

2859 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

2860 goto failed;

2861 }

2862

2863 if (getgrouplist (username_c,

2864 info-\>primary_gid,

2865 buf, &buf_count) \< 0)

2866 {

2867 gid_t \*new;

2868 /\* Presumed cause of negative return code: buf has insufficient

2869 entries to hold the entire group list. The Linux behavior in this

2870 case is to pass back the actual number of groups in buf_count, but

2871 on Mac OS X 10.5, buf_count is unhelpfully left alone.

2872 So as a hack, try to help out a bit by guessing a larger

2873 number of groups, within reason.. might still fail, of course,

2874 but we can at least print a more informative message. I looked up

2875 the "right way" to do this by downloading Apple's own source code

2876 for the "id" command, and it turns out that they use an

2877 undocumented library function getgrouplist_2 (!) which is not

2878 declared in any header in /usr/include (!!). That did not seem

2879 like the way to go here.

2880 \*/

2881 if (buf_count == initial_buf_count)

2882 {

2883 buf_count \*= 16; /\* Retry with an arbitrarily scaled-up array \*/

2884 }

2885 new = dbus_realloc (buf, buf_count \* sizeof (buf\[0\]));

2886 if (new == NULL)

2887 {

2888 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

2889 dbus_free (buf);

2890 goto failed;

2891 }

2892

2893 buf = new;

2894

2895 errno = 0;

2896 if (getgrouplist (username_c, info-\>primary_gid, buf, &buf_count) \< 0)

2897 {

2898 if (errno == 0)

2899 {

2900 \_dbus_warn ("It appears that username \\%s\\ is in more than %d groups.\nProceeding with just the first %d groups.",

2901 username_c, buf_count, buf_count);

2902 }

2903 else

2904 {

2905 dbus_set_error (error,

2906 \_dbus_error_from_errno (errno),

2907 "Failed to get groups for username \\%s\\ primary GID "

2908 DBUS_GID_FORMAT ": %s\n",

2909 username_c, info-\>primary_gid,

2910 \_dbus_strerror (errno));

2911 dbus_free (buf);

2912 goto failed;

2913 }

2914 }

2915 }

2916

2917 info-\>group_ids = dbus_new (dbus_gid_t, buf_count);

2918 if (info-\>group_ids == NULL)

2919 {

2920 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

2921 dbus_free (buf);

2922 goto failed;

2923 }

2924

2925 for (i = 0; i \< buf_count; ++i)

2926 info-\>group_ids\[i\] = buf\[i\];

2927

2928 info-\>n_group_ids = buf_count;

2929

2930 dbus_free (buf);

2931 }

2932\#else /\* HAVE_GETGROUPLIST \*/

2933 {

2934 /\* We just get the one group ID \*/

2935 info-\>group_ids = dbus_new (dbus_gid_t, 1);

2936 if (info-\>group_ids == NULL)

2937 {

2938 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

2939 goto failed;

2940 }

2941

2942 info-\>n_group_ids = 1;

2943

2944 (info-\>group_ids)\[0\] = info-\>primary_gid;

2945 }

2946\#endif /\* HAVE_GETGROUPLIST \*/

2947

2948 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

2949

2950 return TRUE;

2951

2952 failed:

2953 \_DBUS_ASSERT_ERROR_IS_SET (error);

2954 return FALSE;

2955}

2956

2965dbus_bool_t

2966\_dbus_user_info_fill (DBusUserInfo \*info,

2967 const DBusString \*username,

2968 DBusError \*error)

2969{

2970 return fill_user_info (info, DBUS_UID_UNSET,

2971 username, error);

2972}

2973

2982dbus_bool_t

2983\_dbus_user_info_fill_uid (DBusUserInfo \*info,

2984 dbus_uid_t uid,

2985 DBusError \*error)

2986{

2987 return fill_user_info (info, uid,

2988 NULL, error);

2989}

2990

3004dbus_bool_t

3005\_dbus_credentials_add_from_current_process (DBusCredentials \*credentials)

3006{

3007 dbus_pid_t pid = \_dbus_getpid ();

3008

3009 /\* The POSIX spec certainly doesn't promise this, but

3010 \* we need these assertions to fail as soon as we're wrong about

3011 \* it so we can do the porting fixups

3012 \*/

3013 \_DBUS_STATIC_ASSERT (sizeof (pid_t) \<= sizeof (dbus_pid_t));

3014 \_DBUS_STATIC_ASSERT (sizeof (uid_t) \<= sizeof (dbus_uid_t));

3015 \_DBUS_STATIC_ASSERT (sizeof (gid_t) \<= sizeof (dbus_gid_t));

3016

3017\#if HAVE_DECL_SYS_PIDFD_OPEN

3018 /\* Normally this syscall would have a race condition, but we can trust

3019 \* that our own process isn't going to exit, so the pid won't get reused. \*/

3020 int pid_fd = (int) syscall (SYS_pidfd_open, pid, 0);

3021 if (pid_fd \>= 0)

3022 \_dbus_credentials_take_pid_fd (credentials, pid_fd);

3023\#endif

3024 if (!\_dbus_credentials_add_pid (credentials, pid))

3025 return FALSE;

3026 if (!\_dbus_credentials_add_unix_uid(credentials, \_dbus_geteuid()))

3027 return FALSE;

3028

3029 return TRUE;

3030}

3031

3044dbus_pid_t

3045\_dbus_resolve_pid_fd (int pid_fd)

3046{

3047\#ifdef \_\_linux\_\_

3048 DBusError error = DBUS_ERROR_INIT;

3049 DBusString content = \_DBUS_STRING_INIT_INVALID;

3050 DBusString filename = \_DBUS_STRING_INIT_INVALID;

3051 dbus_pid_t result = DBUS_PID_UNSET;

3052 int pid_index;

3053

3054 if (pid_fd \< 0)

3055 goto out;

3056

3057 if (!\_dbus_string_init (&content))

3058 goto out;

3059

3060 if (!\_dbus_string_init (&filename))

3061 goto out;

3062

3063 if (!\_dbus_string_append_printf (&filename, "/proc/self/fdinfo/%d", pid_fd))

3064 goto out;

3065

3066 if (!\_dbus_file_get_contents (&content, &filename, &error))

3067 {

3068 \_dbus_verbose ("Cannot read '/proc/self/fdinfo/%d', unable to resolve PID, %s: %s\n",

3069 pid_fd, error.name, error.message);

3070 goto out;

3071 }

3072

3073 /\* Ensure we are not reading PPid, either it's the first line of the file or

3074 \* there's a newline before it. \*/

3075 if (!\_dbus_string_find (&content, 0, "Pid:", &pid_index) \|\|

3076 (pid_index \> 0 && \_dbus_string_get_byte (&content, pid_index - 1) != '\n'))

3077 {

3078 \_dbus_verbose ("Cannot find 'Pid:' in '/proc/self/fdinfo/%d', unable to resolve PID\n",

3079 pid_fd);

3080 goto out;

3081 }

3082

3083 if (!\_dbus_string_parse_uint (&content, pid_index + strlen ("Pid:"), &result, NULL))

3084 {

3085 \_dbus_verbose ("Cannot parse 'Pid:' from '/proc/self/fdinfo/%d', unable to resolve PID\n",

3086 pid_fd);

3087 goto out;

3088 }

3089

3090out:

3091 \_dbus_string_free (&content);

3092 \_dbus_string_free (&filename);

3093 dbus_error_free (&error);

3094

3095 if (result \<= 0)

3096 return DBUS_PID_UNSET;

3097

3098 return result;

3099\#else

3100 return DBUS_PID_UNSET;

3101\#endif

3102

3103}

3104

3116dbus_bool_t

3117\_dbus_append_user_from_current_process (DBusString \*str)

3118{

3119 return \_dbus_string_append_printf (str, DBUS_UID_FORMAT, \_dbus_geteuid ());

3120}

3121

3126dbus_pid_t

3127\_dbus_getpid (void)

3128{

3129 return getpid ();

3130}

3131

3135dbus_uid_t

3136\_dbus_getuid (void)

3137{

3138 return getuid ();

3139}

3140

3144dbus_uid_t

3145\_dbus_geteuid (void)

3146{

3147 return geteuid ();

3148}

3149

3156unsigned long

3157\_dbus_pid_for_log (void)

3158{

3159 return getpid ();

3160}

3161

3162\#if !defined(HAVE_STDATOMIC_H) && !DBUS_USE_SYNC

3163/\* To be thread-safe by default on platforms that don't necessarily have

3164 \* atomic operations (notably Debian armel, which is armv4t), we must

3165 \* use a mutex that can be initialized statically, like this.

3166 \* GLib \>= 2.32 uses a similar system.

3167 \*/

3168static pthread_mutex_t atomic_mutex = PTHREAD_MUTEX_INITIALIZER;

3169\#endif

3170

3177dbus_int32_t

3178\_dbus_atomic_inc (DBusAtomic \*atomic)

3179{

3180\#ifdef HAVE_STDATOMIC_H

3181 /\* Atomic version of "old = \*atomic; \*atomic += 1; return old" \*/

3182 return atomic_fetch_add (&atomic-\>value, 1);

3183\#elif DBUS_USE_SYNC

3184 /\* Atomic version of "\*atomic += 1; return \*atomic - 1" \*/

3185 return \_\_sync_add_and_fetch(&atomic-\>value, 1)-1;

3186\#else

3187 dbus_int32_t res;

3188

3189 pthread_mutex_lock (&atomic_mutex);

3190 res = atomic-\>value;

3191 atomic-\>value += 1;

3192 pthread_mutex_unlock (&atomic_mutex);

3193

3194 return res;

3195\#endif

3196}

3197

3204dbus_int32_t

3205\_dbus_atomic_dec (DBusAtomic \*atomic)

3206{

3207\#ifdef HAVE_STDATOMIC_H

3208 /\* Atomic version of "old = \*atomic; \*atomic -= 1; return old" \*/

3209 return atomic_fetch_sub (&atomic-\>value, 1);

3210\#elif DBUS_USE_SYNC

3211 /\* Atomic version of "\*atomic -= 1; return \*atomic + 1" \*/

3212 return \_\_sync_sub_and_fetch(&atomic-\>value, 1)+1;

3213\#else

3214 dbus_int32_t res;

3215

3216 pthread_mutex_lock (&atomic_mutex);

3217 res = atomic-\>value;

3218 atomic-\>value -= 1;

3219 pthread_mutex_unlock (&atomic_mutex);

3220

3221 return res;

3222\#endif

3223}

3224

3232dbus_int32_t

3233\_dbus_atomic_get (DBusAtomic \*atomic)

3234{

3235\#ifdef HAVE_STDATOMIC_H

3236 /\* Atomic version of "return \*atomic" \*/

3237 return atomic_load (&atomic-\>value);

3238\#elif DBUS_USE_SYNC

3239 \_\_sync_synchronize ();

3240 return atomic-\>value;

3241\#else

3242 dbus_int32_t res;

3243

3244 pthread_mutex_lock (&atomic_mutex);

3245 res = atomic-\>value;

3246 pthread_mutex_unlock (&atomic_mutex);

3247

3248 return res;

3249\#endif

3250}

3251

3257void

3258\_dbus_atomic_set_zero (DBusAtomic \*atomic)

3259{

3260\#ifdef HAVE_STDATOMIC_H

3261 /\* Atomic version of "\*atomic = 0" \*/

3262 atomic_store (&atomic-\>value, 0);

3263\#elif DBUS_USE_SYNC

3264 /\* Atomic version of "\*atomic &= 0; return \*atomic" \*/

3265 \_\_sync_and_and_fetch (&atomic-\>value, 0);

3266\#else

3267 pthread_mutex_lock (&atomic_mutex);

3268 atomic-\>value = 0;

3269 pthread_mutex_unlock (&atomic_mutex);

3270\#endif

3271}

3272

3278void

3279\_dbus_atomic_set_nonzero (DBusAtomic \*atomic)

3280{

3281\#ifdef HAVE_STDATOMIC_H

3282 /\* Atomic version of "\*atomic = 1" \*/

3283 atomic_store (&atomic-\>value, 1);

3284\#elif DBUS_USE_SYNC

3285 /\* Atomic version of "\*atomic \|= 1; return \*atomic" \*/

3286 \_\_sync_or_and_fetch (&atomic-\>value, 1);

3287\#else

3288 pthread_mutex_lock (&atomic_mutex);

3289 atomic-\>value = 1;

3290 pthread_mutex_unlock (&atomic_mutex);

3291\#endif

3292}

3293

3302int

3303\_dbus_poll (DBusPollFD \*fds,

3304 int n_fds,

3305 int timeout_milliseconds)

3306{

3307\#if defined(HAVE_POLL) && !defined(BROKEN_POLL)

3308 /\* DBusPollFD is a struct pollfd in this code path, so we can just poll() \*/

3309 if (timeout_milliseconds \< -1)

3310 {

3311 timeout_milliseconds = -1;

3312 }

3313

3314 return poll (fds,

3315 n_fds,

3316 timeout_milliseconds);

3317\#else /\* ! HAVE_POLL \*/

3318 /\* Emulate poll() in terms of select() \*/

3319 fd_set read_set, write_set, err_set;

3320 int max_fd = 0;

3321 int i;

3322 struct timeval tv;

3323 int ready;

3324

3325 FD_ZERO (&read_set);

3326 FD_ZERO (&write_set);

3327 FD_ZERO (&err_set);

3328

3329 for (i = 0; i \< n_fds; i++)

3330 {

3331 DBusPollFD \*fdp = &fds\[i\];

3332

3333 if (fdp-\>events & \_DBUS_POLLIN)

3334 FD_SET (fdp-\>fd, &read_set);

3335

3336 if (fdp-\>events & \_DBUS_POLLOUT)

3337 FD_SET (fdp-\>fd, &write_set);

3338

3339 FD_SET (fdp-\>fd, &err_set);

3340

3341 max_fd = MAX (max_fd, fdp-\>fd);

3342 }

3343

3344 tv.tv_sec = timeout_milliseconds / 1000;

3345 tv.tv_usec = (timeout_milliseconds % 1000) \* 1000;

3346

3347 ready = select (max_fd + 1, &read_set, &write_set, &err_set,

3348 timeout_milliseconds \< 0 ? NULL : &tv);

3349

3350 if (ready \> 0)

3351 {

3352 for (i = 0; i \< n_fds; i++)

3353 {

3354 DBusPollFD \*fdp = &fds\[i\];

3355

3356 fdp-\>revents = 0;

3357

3358 if (FD_ISSET (fdp-\>fd, &read_set))

3359 fdp-\>revents \|= \_DBUS_POLLIN;

3360

3361 if (FD_ISSET (fdp-\>fd, &write_set))

3362 fdp-\>revents \|= \_DBUS_POLLOUT;

3363

3364 if (FD_ISSET (fdp-\>fd, &err_set))

3365 fdp-\>revents \|= \_DBUS_POLLERR;

3366 }

3367 }

3368

3369 return ready;

3370\#endif

3371}

3372

3380void

3381\_dbus_get_monotonic_time (dbus_int64_t \*tv_sec,

3382 long \*tv_usec)

3383{

3384\#ifdef HAVE_MONOTONIC_CLOCK

3385 struct timespec ts;

3386 clock_gettime (CLOCK_MONOTONIC, &ts);

3387

3388 if (tv_sec)

3389 \*tv_sec = ts.tv_sec;

3390 if (tv_usec)

3391 \*tv_usec = ts.tv_nsec / 1000;

3392\#else

3393 struct timeval t;

3394

3395 gettimeofday (&t, NULL);

3396

3397 if (tv_sec)

3398 \*tv_sec = t.tv_sec;

3399 if (tv_usec)

3400 \*tv_usec = t.tv_usec;

3401\#endif

3402}

3403

3411void

3412\_dbus_get_real_time (dbus_int64_t \*tv_sec,

3413 long \*tv_usec)

3414{

3415 struct timeval t;

3416

3417 gettimeofday (&t, NULL);

3418

3419 if (tv_sec)

3420 \*tv_sec = t.tv_sec;

3421 if (tv_usec)

3422 \*tv_usec = t.tv_usec;

3423}

3424

3433dbus_bool_t

3434\_dbus_ensure_directory (const DBusString \*filename,

3435 DBusError \*error)

3436{

3437 const char \*filename_c;

3438

3439 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

3440

3441 filename_c = \_dbus_string_get_const_data (filename);

3442

3443 if (mkdir (filename_c, 0700) \< 0)

3444 {

3445 if (errno == EEXIST)

3446 return TRUE;

3447

3448 dbus_set_error (error, DBUS_ERROR_FAILED,

3449 "Failed to create directory %s: %s\n",

3450 filename_c, \_dbus_strerror (errno));

3451 return FALSE;

3452 }

3453 else

3454 return TRUE;

3455}

3456

3465dbus_bool_t

3466\_dbus_create_directory (const DBusString \*filename,

3467 DBusError \*error)

3468{

3469 const char \*filename_c;

3470

3471 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

3472

3473 filename_c = \_dbus_string_get_const_data (filename);

3474

3475 if (mkdir (filename_c, 0700) \< 0)

3476 {

3477 dbus_set_error (error, DBUS_ERROR_FAILED,

3478 "Failed to create directory %s: %s\n",

3479 filename_c, \_dbus_strerror (errno));

3480 return FALSE;

3481 }

3482 else

3483 return TRUE;

3484}

3485

3496dbus_bool_t

3497\_dbus_concat_dir_and_file (DBusString \*dir,

3498 const DBusString \*next_component)

3499{

3500 dbus_bool_t dir_ends_in_slash;

3501 dbus_bool_t file_starts_with_slash;

3502

3503 if (\_dbus_string_get_length (dir) == 0 \|\|

3504 \_dbus_string_get_length (next_component) == 0)

3505 return TRUE;

3506

3507 dir_ends_in_slash = '/' == \_dbus_string_get_byte (dir,

3508 \_dbus_string_get_length (dir) - 1);

3509

3510 file_starts_with_slash = '/' == \_dbus_string_get_byte (next_component, 0);

3511

3512 if (dir_ends_in_slash && file_starts_with_slash)

3513 {

3514 \_dbus_string_shorten (dir, 1);

3515 }

3516 else if (!(dir_ends_in_slash \|\| file_starts_with_slash))

3517 {

3518 if (!\_dbus_string_append_byte (dir, '/'))

3519 return FALSE;

3520 }

3521

3522 return \_dbus_string_copy (next_component, 0, dir,

3523 \_dbus_string_get_length (dir));

3524}

3525

3527\#define NANOSECONDS_PER_SECOND 1000000000

3529\#define MICROSECONDS_PER_SECOND 1000000

3531\#define MILLISECONDS_PER_SECOND 1000

3533\#define NANOSECONDS_PER_MILLISECOND 1000000

3535\#define MICROSECONDS_PER_MILLISECOND 1000

3536

3541void

3542\_dbus_sleep_milliseconds (int milliseconds)

3543{

3544\#ifdef HAVE_NANOSLEEP

3545 struct timespec req;

3546 struct timespec rem;

3547

3548 req.tv_sec = milliseconds / MILLISECONDS_PER_SECOND;

3549 req.tv_nsec = (milliseconds % MILLISECONDS_PER_SECOND) \* NANOSECONDS_PER_MILLISECOND;

3550 rem.tv_sec = 0;

3551 rem.tv_nsec = 0;

3552

3553 while (nanosleep (&req, &rem) \< 0 && errno == EINTR)

3554 req = rem;

3555\#elif defined (HAVE_USLEEP)

3556 usleep (milliseconds \* MICROSECONDS_PER_MILLISECOND);

3557\#else /\* ! HAVE_USLEEP \*/

3558 sleep (MAX (milliseconds / 1000, 1));

3559\#endif

3560}

3561

3571dbus_bool_t

3572\_dbus_generate_random_bytes (DBusString \*str,

3573 int n_bytes,

3574 DBusError \*error)

3575{

3576 int old_len = \_dbus_string_get_length (str);

3577 int fd;

3578 int result;

3579\#ifdef HAVE_GETRANDOM

3580 char \*buffer;

3581

3582 if (!\_dbus_string_lengthen (str, n_bytes))

3583 {

3584 \_DBUS_SET_OOM (error);

3585 return FALSE;

3586 }

3587

3588 buffer = \_dbus_string_get_data_len (str, old_len, n_bytes);

3589 result = getrandom (buffer, n_bytes, GRND_NONBLOCK);

3590

3591 if (result == n_bytes)

3592 return TRUE;

3593

3594 \_dbus_string_set_length (str, old_len);

3595\#endif

3596

3597 /\* note, urandom on linux will fall back to pseudorandom \*/

3598 fd = open ("/dev/urandom", O_RDONLY);

3599

3600 if (fd \< 0)

3601 {

3602 dbus_set_error (error, \_dbus_error_from_errno (errno),

3603 "Could not open /dev/urandom: %s",

3604 \_dbus_strerror (errno));

3605 return FALSE;

3606 }

3607

3608 \_dbus_verbose ("/dev/urandom fd %d opened\n", fd);

3609

3610 result = \_dbus_read (fd, str, n_bytes);

3611

3612 if (result != n_bytes)

3613 {

3614 if (result \< 0)

3615 dbus_set_error (error, \_dbus_error_from_errno (errno),

3616 "Could not read /dev/urandom: %s",

3617 \_dbus_strerror (errno));

3618 else

3619 dbus_set_error (error, DBUS_ERROR_IO_ERROR,

3620 "Short read from /dev/urandom");

3621

3622 \_dbus_close (fd, NULL);

3623 \_dbus_string_set_length (str, old_len);

3624 return FALSE;

3625 }

3626

3627 \_dbus_verbose ("Read %d bytes from /dev/urandom\n",

3628 n_bytes);

3629

3630 \_dbus_close (fd, NULL);

3631

3632 return TRUE;

3633}

3634

3640void

3641\_dbus_exit (int code)

3642{

3643 \_exit (code);

3644}

3645

3654const char\*

3655\_dbus_strerror (int error_number)

3656{

3657 const char \*msg;

3658

3659 msg = strerror (error_number);

3660 if (msg == NULL)

3661 msg = "unknown";

3662

3663 return msg;

3664}

3665

3669void

3670\_dbus_disable_sigpipe (void)

3671{

3672 signal (SIGPIPE, SIG_IGN);

3673}

3674

3682void

3683\_dbus_fd_set_close_on_exec (int fd)

3684{

3685 int val;

3686

3687 val = fcntl (fd, F_GETFD, 0);

3688

3689 if (val \< 0)

3690 return;

3691

3692 val \|= FD_CLOEXEC;

3693

3694 fcntl (fd, F_SETFD, val);

3695}

3696

3704void

3705\_dbus_fd_clear_close_on_exec (int fd)

3706{

3707 int val;

3708

3709 val = fcntl (fd, F_GETFD, 0);

3710

3711 if (val \< 0)

3712 return;

3713

3714 val &= ~FD_CLOEXEC;

3715

3716 fcntl (fd, F_SETFD, val);

3717}

3718

3726dbus_bool_t

3727\_dbus_close (int fd,

3728 DBusError \*error)

3729{

3730 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

3731

3732 again:

3733 if (close (fd) \< 0)

3734 {

3735 if (errno == EINTR)

3736 goto again;

3737

3738 dbus_set_error (error, \_dbus_error_from_errno (errno),

3739 "Could not close fd %d", fd);

3740 return FALSE;

3741 }

3742

3743 return TRUE;

3744}

3745

3754int

3755\_dbus_dup(int fd,

3756 DBusError \*error)

3757{

3758 int new_fd;

3759

3760\#ifdef F_DUPFD_CLOEXEC

3761 dbus_bool_t cloexec_done;

3762

3763 new_fd = fcntl(fd, F_DUPFD_CLOEXEC, 3);

3764 cloexec_done = new_fd \>= 0;

3765

3766 if (new_fd \< 0 && errno == EINVAL)

3767\#endif

3768 {

3769 new_fd = fcntl(fd, F_DUPFD, 3);

3770 }

3771

3772 if (new_fd \< 0) {

3773

3774 dbus_set_error (error, \_dbus_error_from_errno (errno),

3775 "Could not duplicate fd %d", fd);

3776 return -1;

3777 }

3778

3779\#ifdef F_DUPFD_CLOEXEC

3780 if (!cloexec_done)

3781\#endif

3782 {

3783 \_dbus_fd_set_close_on_exec(new_fd);

3784 }

3785

3786 return new_fd;

3787}

3788

3796dbus_bool_t

3797\_dbus_set_socket_nonblocking (DBusSocket fd,

3798 DBusError \*error)

3799{

3800 return \_dbus_set_fd_nonblocking (fd.fd, error);

3801}

3802

3803static dbus_bool_t

3804\_dbus_set_fd_nonblocking (int fd,

3805 DBusError \*error)

3806{

3807 int val;

3808

3809 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

3810

3811 val = fcntl (fd, F_GETFL, 0);

3812 if (val \< 0)

3813 {

3814 dbus_set_error (error, \_dbus_error_from_errno (errno),

3815 "Failed to get flags from file descriptor %d: %s",

3816 fd, \_dbus_strerror (errno));

3817 \_dbus_verbose ("Failed to get flags for fd %d: %s\n", fd,

3818 \_dbus_strerror (errno));

3819 return FALSE;

3820 }

3821

3822 if (fcntl (fd, F_SETFL, val \| O_NONBLOCK) \< 0)

3823 {

3824 dbus_set_error (error, \_dbus_error_from_errno (errno),

3825 "Failed to set nonblocking flag of file descriptor %d: %s",

3826 fd, \_dbus_strerror (errno));

3827 \_dbus_verbose ("Failed to set fd %d nonblocking: %s\n",

3828 fd, \_dbus_strerror (errno));

3829

3830 return FALSE;

3831 }

3832

3833 return TRUE;

3834}

3835

3841void

3842\_dbus_print_backtrace (void)

3843{

3844\#if defined (HAVE_BACKTRACE) && defined (DBUS_BUILT_R_DYNAMIC)

3845 void \*bt\[500\];

3846 int bt_size;

3847 int i;

3848 char \*\*syms;

3849

3850 bt_size = backtrace (bt, 500);

3851

3852 syms = backtrace_symbols (bt, bt_size);

3853

3854 i = 0;

3855 while (i \< bt_size)

3856 {

3857 /\* don't use dbus_warn since it can \_dbus_abort() \*/

3858 fprintf (stderr, " %s\n", syms\[i\]);

3859 ++i;

3860 }

3861 fflush (stderr);

3862

3863 free (syms);

3864\#elif defined (HAVE_BACKTRACE) && ! defined (DBUS_BUILT_R_DYNAMIC)

3865 fprintf (stderr, " D-Bus not built with -rdynamic so unable to print a backtrace\n");

3866\#else

3867 fprintf (stderr, " D-Bus not compiled with backtrace support so unable to print a backtrace\n");

3868\#endif

3869}

3870

3883dbus_bool_t

3884\_dbus_socketpair (DBusSocket \*fd1,

3885 DBusSocket \*fd2,

3886 dbus_bool_t blocking,

3887 DBusError \*error)

3888{

3889\#ifdef HAVE_SOCKETPAIR

3890 int fds\[2\];

3891 int retval;

3892

3893\#ifdef SOCK_CLOEXEC

3894 dbus_bool_t cloexec_done;

3895

3896 retval = socketpair(AF_UNIX, SOCK_STREAM\|SOCK_CLOEXEC, 0, fds);

3897 cloexec_done = retval \>= 0;

3898

3899 if (retval \< 0 && (errno == EINVAL \|\| errno == EPROTOTYPE))

3900\#endif

3901 {

3902 retval = socketpair(AF_UNIX, SOCK_STREAM, 0, fds);

3903 }

3904

3905 if (retval \< 0)

3906 {

3907 dbus_set_error (error, \_dbus_error_from_errno (errno),

3908 "Could not create full-duplex pipe");

3909 return FALSE;

3910 }

3911

3912 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

3913

3914\#ifdef SOCK_CLOEXEC

3915 if (!cloexec_done)

3916\#endif

3917 {

3918 \_dbus_fd_set_close_on_exec (fds\[0\]);

3919 \_dbus_fd_set_close_on_exec (fds\[1\]);

3920 }

3921

3922 if (!blocking &&

3923 (!\_dbus_set_fd_nonblocking (fds\[0\], NULL) \|\|

3924 !\_dbus_set_fd_nonblocking (fds\[1\], NULL)))

3925 {

3926 dbus_set_error (error, \_dbus_error_from_errno (errno),

3927 "Could not set full-duplex pipe nonblocking");

3928

3929 \_dbus_close (fds\[0\], NULL);

3930 \_dbus_close (fds\[1\], NULL);

3931

3932 return FALSE;

3933 }

3934

3935 fd1-\>fd = fds\[0\];

3936 fd2-\>fd = fds\[1\];

3937

3938 \_dbus_verbose ("full-duplex pipe %d \<-\> %d\n",

3939 fd1-\>fd, fd2-\>fd);

3940

3941 return TRUE;

3942\#else

3943 \_dbus_warn ("\_dbus_socketpair() not implemented on this OS");

3944 dbus_set_error (error, DBUS_ERROR_FAILED,

3945 "\_dbus_socketpair() not implemented on this OS");

3946 return FALSE;

3947\#endif

3948}

3949

3958int

3959\_dbus_printf_string_upper_bound (const char \*format,

3960 va_list args)

3961{

3962 char static_buf\[1024\];

3963 int bufsize = sizeof (static_buf);

3964 int len;

3965 va_list args_copy;

3966

3967 va_copy (args_copy, args);

3968 len = vsnprintf (static_buf, bufsize, format, args_copy);

3969 va_end (args_copy);

3970

3971 /\* If vsnprintf() returned non-negative, then either the string fits in

3972 \* static_buf, or this OS has the POSIX and C99 behaviour where vsnprintf

3973 \* returns the number of characters that were needed, or this OS returns the

3974 \* truncated length.

3975 \*

3976 \* We ignore the possibility that snprintf might just ignore the length and

3977 \* overrun the buffer (64-bit Solaris 7), because that's pathological.

3978 \* If your libc is really that bad, come back when you have a better one. \*/

3979 if (len == bufsize)

3980 {

3981 /\* This could be the truncated length (Tru64 and IRIX have this bug),

3982 \* or the real length could be coincidentally the same. Which is it?

3983 \* If vsnprintf returns the truncated length, we'll go to the slow

3984 \* path. \*/

3985 va_copy (args_copy, args);

3986

3987 if (vsnprintf (static_buf, 1, format, args_copy) == 1)

3988 len = -1;

3989

3990 va_end (args_copy);

3991 }

3992

3993 /\* If vsnprintf() returned negative, we have to do more work.

3994 \* HP-UX returns negative. \*/

3995 while (len \< 0)

3996 {

3997 char \*buf;

3998

3999 bufsize \*= 2;

4000

4001 buf = dbus_malloc (bufsize);

4002

4003 if (buf == NULL)

4004 return -1;

4005

4006 va_copy (args_copy, args);

4007 len = vsnprintf (buf, bufsize, format, args_copy);

4008 va_end (args_copy);

4009

4010 dbus_free (buf);

4011

4012 /\* If the reported length is exactly the buffer size, round up to the

4013 \* next size, in case vsnprintf has been returning the truncated

4014 \* length \*/

4015 if (len == bufsize)

4016 len = -1;

4017 }

4018

4019 return len;

4020}

4021

4028const char\*

4029\_dbus_get_tmpdir(void)

4030{

4031 /\* Protected by \_DBUS_LOCK_sysdeps \*/

4032 static const char\* tmpdir = NULL;

4033

4034 if (!\_DBUS_LOCK (sysdeps))

4035 return NULL;

4036

4037 if (tmpdir == NULL)

4038 {

4039 /\* TMPDIR is what glibc uses, then

4040 \* glibc falls back to the P_tmpdir macro which

4041 \* just expands to "/tmp"

4042 \*/

4043 if (tmpdir == NULL)

4044 tmpdir = getenv("TMPDIR");

4045

4046 /\* These two env variables are probably

4047 \* broken, but maybe some OS uses them?

4048 \*/

4049 if (tmpdir == NULL)

4050 tmpdir = getenv("TMP");

4051 if (tmpdir == NULL)

4052 tmpdir = getenv("TEMP");

4053

4054 /\* And this is the sane fallback. \*/

4055 if (tmpdir == NULL)

4056 tmpdir = "/tmp";

4057 }

4058

4059 \_DBUS_UNLOCK (sysdeps);

4060

4061 \_dbus_assert(tmpdir != NULL);

4062

4063 return tmpdir;

4064}

4065

4066\#if defined(DBUS_ENABLE_X11_AUTOLAUNCH) \|\| defined(DBUS_ENABLE_LAUNCHD)

4086static dbus_bool_t

4087\_read_subprocess_line_argv (const char \*progpath,

4088 dbus_bool_t path_fallback,

4089 const char \* const \*argv,

4090 DBusString \*result,

4091 DBusError \*error)

4092{

4093 int result_pipe\[2\] = { -1, -1 };

4094 int errors_pipe\[2\] = { -1, -1 };

4095 pid_t pid;

4096 int ret;

4097 int status;

4098 int orig_len;

4099

4100 dbus_bool_t retval;

4101 sigset_t new_set, old_set;

4102

4103 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

4104 retval = FALSE;

4105

4106 /\* We need to block any existing handlers for SIGCHLD temporarily; they

4107 \* will cause waitpid() below to fail.

4108 \* https://bugs.freedesktop.org/show_bug.cgi?id=21347

4109 \*/

4110 sigemptyset (&new_set);

4111 sigaddset (&new_set, SIGCHLD);

4112 sigprocmask (SIG_BLOCK, &new_set, &old_set);

4113

4114 orig_len = \_dbus_string_get_length (result);

4115

4116\#define READ_END 0

4117\#define WRITE_END 1

4118 if (pipe (result_pipe) \< 0)

4119 {

4120 dbus_set_error (error, \_dbus_error_from_errno (errno),

4121 "Failed to create a pipe to call %s: %s",

4122 progpath, \_dbus_strerror (errno));

4123 \_dbus_verbose ("Failed to create a pipe to call %s: %s\n",

4124 progpath, \_dbus_strerror (errno));

4125 goto out;

4126 }

4127 if (pipe (errors_pipe) \< 0)

4128 {

4129 dbus_set_error (error, \_dbus_error_from_errno (errno),

4130 "Failed to create a pipe to call %s: %s",

4131 progpath, \_dbus_strerror (errno));

4132 \_dbus_verbose ("Failed to create a pipe to call %s: %s\n",

4133 progpath, \_dbus_strerror (errno));

4134 goto out;

4135 }

4136

4137 /\* Make sure our output buffers aren't redundantly printed by both the

4138 \* parent and the child \*/

4139 fflush (stdout);

4140 fflush (stderr);

4141

4142 pid = fork ();

4143 if (pid \< 0)

4144 {

4145 dbus_set_error (error, \_dbus_error_from_errno (errno),

4146 "Failed to fork() to call %s: %s",

4147 progpath, \_dbus_strerror (errno));

4148 \_dbus_verbose ("Failed to fork() to call %s: %s\n",

4149 progpath, \_dbus_strerror (errno));

4150 goto out;

4151 }

4152

4153 if (pid == 0)

4154 {

4155 /\* child process \*/

4156 const char \*error_str;

4157

4158 if (!\_dbus_ensure_standard_fds (DBUS_FORCE_STDIN_NULL, &error_str))

4159 {

4160 int saved_errno = errno;

4161

4162 /\* Try to write details into the pipe, but don't bother

4163 \* trying too hard (no retry loop). \*/

4164

4165 if (write (errors_pipe\[WRITE_END\], error_str, strlen (error_str)) \< 0 \|\|

4166 write (errors_pipe\[WRITE_END\], ": ", 2) \< 0)

4167 {

4168 /\* ignore, not much we can do \*/

4169 }

4170

4171 error_str = \_dbus_strerror (saved_errno);

4172

4173 if (write (errors_pipe\[WRITE_END\], error_str, strlen (error_str)) \< 0)

4174 {

4175 /\* ignore, not much we can do \*/

4176 }

4177

4178 \_exit (1);

4179 }

4180

4181 /\* set-up stdXXX \*/

4182 close (result_pipe\[READ_END\]);

4183 close (errors_pipe\[READ_END\]);

4184

4185 if (dup2 (result_pipe\[WRITE_END\], 1) == -1) /\* setup stdout \*/

4186 \_exit (1);

4187 if (dup2 (errors_pipe\[WRITE_END\], 2) == -1) /\* setup stderr \*/

4188 \_exit (1);

4189

4190 \_dbus_close_all ();

4191

4192 sigprocmask (SIG_SETMASK, &old_set, NULL);

4193

4194 /\* If it looks fully-qualified, try execv first \*/

4195 if (progpath\[0\] == '/')

4196 {

4197 execv (progpath, (char \* const \*) argv);

4198 /\* Ok, that failed. Now if path_fallback is given, let's

4199 \* try unqualified. This is mostly a hack to work

4200 \* around systems which ship dbus-launch in /usr/bin

4201 \* but everything else in /bin (because dbus-launch

4202 \* depends on X11).

4203 \*/

4204 if (path_fallback)

4205 /\* We must have a slash, because we checked above \*/

4206 execvp (strrchr (progpath, '/')+1, (char \* const \*) argv);

4207 }

4208 else

4209 execvp (progpath, (char \* const \*) argv);

4210

4211 /\* still nothing, we failed \*/

4212 \_exit (1);

4213 }

4214

4215 /\* parent process \*/

4216 close (result_pipe\[WRITE_END\]);

4217 close (errors_pipe\[WRITE_END\]);

4218 result_pipe\[WRITE_END\] = -1;

4219 errors_pipe\[WRITE_END\] = -1;

4220

4221 ret = 0;

4222 do

4223 {

4224 ret = \_dbus_read (result_pipe\[READ_END\], result, 1024);

4225 }

4226 while (ret \> 0);

4227

4228 /\* reap the child process to avoid it lingering as zombie \*/

4229 do

4230 {

4231 ret = waitpid (pid, &status, 0);

4232 }

4233 while (ret == -1 && errno == EINTR);

4234

4235 /\* We succeeded if the process exited with status 0 and

4236 anything was read \*/

4237 if (!WIFEXITED (status) \|\| WEXITSTATUS (status) != 0 )

4238 {

4239 /\* The process ended with error \*/

4240 DBusString error_message;

4241 if (!\_dbus_string_init (&error_message))

4242 {

4243 \_DBUS_SET_OOM (error);

4244 goto out;

4245 }

4246

4247 ret = 0;

4248 do

4249 {

4250 ret = \_dbus_read (errors_pipe\[READ_END\], &error_message, 1024);

4251 }

4252 while (ret \> 0);

4253

4254 \_dbus_string_set_length (result, orig_len);

4255 if (\_dbus_string_get_length (&error_message) \> 0)

4256 dbus_set_error (error, DBUS_ERROR_SPAWN_EXEC_FAILED,

4257 "%s terminated abnormally with the following error: %s",

4258 progpath, \_dbus_string_get_data (&error_message));

4259 else

4260 dbus_set_error (error, DBUS_ERROR_SPAWN_EXEC_FAILED,

4261 "%s terminated abnormally without any error message",

4262 progpath);

4263 goto out;

4264 }

4265

4266 retval = TRUE;

4267

4268 out:

4269 sigprocmask (SIG_SETMASK, &old_set, NULL);

4270

4271 \_DBUS_ASSERT_ERROR_XOR_BOOL (error, retval);

4272

4273 if (result_pipe\[0\] != -1)

4274 close (result_pipe\[0\]);

4275 if (result_pipe\[1\] != -1)

4276 close (result_pipe\[1\]);

4277 if (errors_pipe\[0\] != -1)

4278 close (errors_pipe\[0\]);

4279 if (errors_pipe\[1\] != -1)

4280 close (errors_pipe\[1\]);

4281

4282 return retval;

4283}

4284\#endif

4285

4298dbus_bool_t

4299\_dbus_get_autolaunch_address (const char \*scope,

4300 DBusString \*address,

4301 DBusError \*error)

4302{

4303\#ifdef DBUS_ENABLE_X11_AUTOLAUNCH

4304 static const char arg_dbus_launch\[\] = "dbus-launch";

4305 static const char arg_autolaunch\[\] = "--autolaunch";

4306 static const char arg_binary_syntax\[\] = "--binary-syntax";

4307 static const char arg_close_stderr\[\] = "--close-stderr";

4308

4309 /\* Perform X11-based autolaunch. (We also support launchd-based autolaunch,

4310 \* but that's done elsewhere, and if it worked, this function wouldn't

4311 \* be called.) \*/

4312 const char \*display;

4313 const char \*progpath;

4314 const char \*argv\[6\];

4315 int i;

4316 DBusString uuid;

4317 dbus_bool_t retval;

4318

4319 if (\_dbus_check_setuid ())

4320 {

4321 dbus_set_error_const (error, DBUS_ERROR_NOT_SUPPORTED,

4322 "Unable to autolaunch when setuid");

4323 return FALSE;

4324 }

4325

4326 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

4327 retval = FALSE;

4328

4329 /\* fd.o \#19997: if \$DISPLAY isn't set to something useful, then

4330 \* dbus-launch-x11 is just going to fail. Rather than trying to

4331 \* run it, we might as well bail out early with a nice error.

4332 \*

4333 \* This is not strictly true in a world where the user bus exists,

4334 \* because dbus-launch --autolaunch knows how to connect to that -

4335 \* but if we were going to connect to the user bus, we'd have done

4336 \* so before trying autolaunch: in any case. \*/

4337 display = \_dbus_getenv ("DISPLAY");

4338

4339 if (display == NULL \|\| display\[0\] == '\0')

4340 {

4341 dbus_set_error_const (error, DBUS_ERROR_NOT_SUPPORTED,

4342 "Unable to autolaunch a dbus-daemon without a \$DISPLAY for X11");

4343 return FALSE;

4344 }

4345

4346 if (!\_dbus_string_init (&uuid))

4347 {

4348 \_DBUS_SET_OOM (error);

4349 return FALSE;

4350 }

4351

4352 if (!\_dbus_get_local_machine_uuid_encoded (&uuid, error))

4353 {

4354 goto out;

4355 }

4356

4357\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

4358 progpath = \_dbus_getenv ("DBUS_TEST_DBUS_LAUNCH");

4359

4360 if (progpath == NULL)

4361\#endif

4362 progpath = DBUS_BINDIR "/dbus-launch";

4363 /\*

4364 \* argv\[0\] is always dbus-launch, that's the name what we'll

4365 \* get from /proc, or ps(1), regardless what the progpath is,

4366 \* see fd.o#69716

4367 \*/

4368 i = 0;

4369 argv\[i\] = arg_dbus_launch;

4370 ++i;

4371 argv\[i\] = arg_autolaunch;

4372 ++i;

4373 argv\[i\] = \_dbus_string_get_data (&uuid);

4374 ++i;

4375 argv\[i\] = arg_binary_syntax;

4376 ++i;

4377 argv\[i\] = arg_close_stderr;

4378 ++i;

4379 argv\[i\] = NULL;

4380 ++i;

4381

4382 \_dbus_assert (i == \_DBUS_N_ELEMENTS (argv));

4383

4384 retval = \_read_subprocess_line_argv (progpath,

4385 TRUE,

4386 argv, address, error);

4387

4388 out:

4389 \_dbus_string_free (&uuid);

4390 return retval;

4391\#else

4392 dbus_set_error_const (error, DBUS_ERROR_NOT_SUPPORTED,

4393 "Using X11 for dbus-daemon autolaunch was disabled at compile time, "

4394\#ifdef DBUS_ENABLE_LAUNCHD

4395 "verify that org.freedesktop.dbus-session.plist is loaded or "

4396\#endif

4397 "set your DBUS_SESSION_BUS_ADDRESS instead");

4398 return FALSE;

4399\#endif

4400}

4401

4420dbus_bool_t

4421\_dbus_read_local_machine_uuid (DBusGUID \*machine_id,

4422 dbus_bool_t create_if_not_found,

4423 DBusError \*error)

4424{

4425 DBusError our_error = DBUS_ERROR_INIT;

4426 DBusError etc_error = DBUS_ERROR_INIT;

4427 DBusString filename;

4428 dbus_bool_t b;

4429

4430 \_dbus_string_init_const (&filename, DBUS_MACHINE_UUID_FILE);

4431

4432 b = \_dbus_read_uuid_file (&filename, machine_id, FALSE, &our_error);

4433 if (b)

4434 return TRUE;

4435

4436 /\* Fallback to the system machine ID \*/

4437 \_dbus_string_init_const (&filename, "/etc/machine-id");

4438 b = \_dbus_read_uuid_file (&filename, machine_id, FALSE, &etc_error);

4439

4440 if (b)

4441 {

4442 if (create_if_not_found)

4443 {

4444 /\* try to copy it to the DBUS_MACHINE_UUID_FILE, but do not

4445 \* complain if that isn't possible for whatever reason \*/

4446 \_dbus_string_init_const (&filename, DBUS_MACHINE_UUID_FILE);

4447 \_dbus_write_uuid_file (&filename, machine_id, NULL);

4448 }

4449

4450 dbus_error_free (&our_error);

4451 return TRUE;

4452 }

4453

4454 if (!create_if_not_found)

4455 {

4456 dbus_set_error (error, etc_error.name,

4457 "D-Bus library appears to be incorrectly set up: "

4458 "see the manual page for dbus-uuidgen to correct "

4459 "this issue. (%s; %s)",

4460 our_error.message, etc_error.message);

4461 dbus_error_free (&our_error);

4462 dbus_error_free (&etc_error);

4463 return FALSE;

4464 }

4465

4466 dbus_error_free (&our_error);

4467 dbus_error_free (&etc_error);

4468

4469 /\* if none found, try to make a new one \*/

4470 \_dbus_string_init_const (&filename, DBUS_MACHINE_UUID_FILE);

4471

4472 if (!\_dbus_generate_uuid (machine_id, error))

4473 return FALSE;

4474

4475 return \_dbus_write_uuid_file (&filename, machine_id, error);

4476}

4477

4485dbus_bool_t

4486\_dbus_lookup_launchd_socket (DBusString \*socket_path,

4487 const char \*launchd_env_var,

4488 DBusError \*error)

4489{

4490\#ifdef DBUS_ENABLE_LAUNCHD

4491 char \*argv\[4\];

4492 int i;

4493

4494 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

4495

4496 if (\_dbus_check_setuid ())

4497 {

4498 dbus_set_error_const (error, DBUS_ERROR_NOT_SUPPORTED,

4499 "Unable to find launchd socket when setuid");

4500 return FALSE;

4501 }

4502

4503 i = 0;

4504 argv\[i\] = "launchctl";

4505 ++i;

4506 argv\[i\] = "getenv";

4507 ++i;

4508 argv\[i\] = (char\*)launchd_env_var;

4509 ++i;

4510 argv\[i\] = NULL;

4511 ++i;

4512

4513 \_dbus_assert (i == \_DBUS_N_ELEMENTS (argv));

4514

4515 if (!\_read_subprocess_line_argv(argv\[0\], TRUE, argv, socket_path, error))

4516 {

4517 return FALSE;

4518 }

4519

4520 /\* no error, but no result either \*/

4521 if (\_dbus_string_get_length(socket_path) == 0)

4522 {

4523 return FALSE;

4524 }

4525

4526 /\* strip the carriage-return \*/

4527 \_dbus_string_shorten(socket_path, 1);

4528 return TRUE;

4529\#else /\* DBUS_ENABLE_LAUNCHD \*/

4530 dbus_set_error(error, DBUS_ERROR_NOT_SUPPORTED,

4531 "can't lookup socket from launchd; launchd support not compiled in");

4532 return FALSE;

4533\#endif

4534}

4535

4536\#ifdef DBUS_ENABLE_LAUNCHD

4537static dbus_bool_t

4538\_dbus_lookup_session_address_launchd (dbus_bool_t \*supported,

4539 DBusString \*address,

4540 DBusError \*error)

4541{

4542 dbus_bool_t valid_socket;

4543 DBusString socket_path;

4544

4545 if (!\_dbus_string_init (&socket_path))

4546 {

4547 \_DBUS_SET_OOM (error);

4548 return FALSE;

4549 }

4550

4551 valid_socket = \_dbus_lookup_launchd_socket (&socket_path, "DBUS_LAUNCHD_SESSION_BUS_SOCKET", NULL);

4552

4553 if (!valid_socket)

4554 {

4555 \_dbus_verbose ("launchd did not provide a socket path");

4556 \_dbus_string_free(&socket_path);

4557 \*supported = FALSE;

4558 return TRUE; /\* Cannot use it, but not an error \*/

4559 }

4560 if (!\_dbus_string_append (address, "unix:path="))

4561 {

4562 \_DBUS_SET_OOM (error);

4563 \_dbus_string_free(&socket_path);

4564 return FALSE;

4565 }

4566 if (!\_dbus_string_copy (&socket_path, 0, address,

4567 \_dbus_string_get_length (address)))

4568 {

4569 \_DBUS_SET_OOM (error);

4570 \_dbus_string_free(&socket_path);

4571 return FALSE;

4572 }

4573

4574 \_dbus_string_free(&socket_path);

4575 return TRUE;

4576}

4577\#endif

4578

4579static dbus_bool_t

4580\_dbus_lookup_user_bus (dbus_bool_t \*supported,

4581 DBusString \*address,

4582 DBusError \*error)

4583{

4584 const char \*runtime_dir = \_dbus_getenv ("XDG_RUNTIME_DIR");

4585 dbus_bool_t ret = FALSE;

4586 struct stat stbuf;

4587 DBusString user_bus_path;

4588

4589 if (runtime_dir == NULL)

4590 {

4591 \_dbus_verbose ("XDG_RUNTIME_DIR not found in environment");

4592 \*supported = FALSE;

4593 return TRUE; /\* Cannot use it, but not an error \*/

4594 }

4595

4596 if (!\_dbus_string_init (&user_bus_path))

4597 {

4598 \_DBUS_SET_OOM (error);

4599 return FALSE;

4600 }

4601

4602 if (!\_dbus_string_append_printf (&user_bus_path, "%s/bus", runtime_dir))

4603 {

4604 \_DBUS_SET_OOM (error);

4605 goto out;

4606 }

4607

4608 if (lstat (\_dbus_string_get_const_data (&user_bus_path), &stbuf) == -1)

4609 {

4610 \_dbus_verbose ("XDG_RUNTIME_DIR/bus not available: %s",

4611 \_dbus_strerror (errno));

4612 \*supported = FALSE;

4613 ret = TRUE; /\* Cannot use it, but not an error \*/

4614 goto out;

4615 }

4616

4617 if (stbuf.st_uid != getuid ())

4618 {

4619 \_dbus_verbose ("XDG_RUNTIME_DIR/bus owned by uid %ld, not our uid %ld",

4620 (long) stbuf.st_uid, (long) getuid ());

4621 \*supported = FALSE;

4622 ret = TRUE; /\* Cannot use it, but not an error \*/

4623 goto out;

4624 }

4625

4626 if ((stbuf.st_mode & S_IFMT) != S_IFSOCK)

4627 {

4628 \_dbus_verbose ("XDG_RUNTIME_DIR/bus is not a socket: st_mode = 0o%lo",

4629 (long) stbuf.st_mode);

4630 \*supported = FALSE;

4631 ret = TRUE; /\* Cannot use it, but not an error \*/

4632 goto out;

4633 }

4634

4635 if (!\_dbus_string_append (address, "unix:path=") \|\|

4636 !\_dbus_address_append_escaped (address, &user_bus_path))

4637 {

4638 \_DBUS_SET_OOM (error);

4639 goto out;

4640 }

4641

4642 \*supported = TRUE;

4643 ret = TRUE;

4644

4645out:

4646 \_dbus_string_free (&user_bus_path);

4647 return ret;

4648}

4649

4669dbus_bool_t

4670\_dbus_lookup_session_address (dbus_bool_t \*supported,

4671 DBusString \*address,

4672 DBusError \*error)

4673{

4674\#ifdef DBUS_ENABLE_LAUNCHD

4675 \*supported = TRUE;

4676 return \_dbus_lookup_session_address_launchd (supported, address, error);

4677\#else

4678 \*supported = FALSE;

4679

4680 if (!\_dbus_lookup_user_bus (supported, address, error))

4681 return FALSE;

4682 else if (\*supported)

4683 return TRUE;

4684

4685 /\* On non-Mac Unix platforms, if the session address isn't already

4686 \* set in DBUS_SESSION_BUS_ADDRESS environment variable and the

4687 \* \$XDG_RUNTIME_DIR/bus can't be used, we punt and fall back to the

4688 \* autolaunch: global default; see init_session_address in

4689 \* dbus/dbus-bus.c. \*/

4690 return TRUE;

4691\#endif

4692}

4693

4701void

4702\_dbus_flush_caches (void)

4703{

4704 \_dbus_user_database_flush_system ();

4705}

4706

4720dbus_bool_t

4721\_dbus_append_keyring_directory_for_credentials (DBusString \*directory,

4722 DBusCredentials \*credentials)

4723{

4724 DBusString homedir;

4725 DBusString dotdir;

4726 dbus_uid_t uid;

4727

4728 \_dbus_assert (credentials != NULL);

4729 \_dbus_assert (!\_dbus_credentials_are_anonymous (credentials));

4730

4731 if (!\_dbus_string_init (&homedir))

4732 return FALSE;

4733

4734 uid = \_dbus_credentials_get_unix_uid (credentials);

4735 \_dbus_assert (uid != DBUS_UID_UNSET);

4736

4737 if (!\_dbus_homedir_from_uid (uid, &homedir))

4738 goto failed;

4739

4740\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

4741 {

4742 const char \*override;

4743

4744 override = \_dbus_getenv ("DBUS_TEST_HOMEDIR");

4745 if (override != NULL && \*override != '\0')

4746 {

4747 \_dbus_string_set_length (&homedir, 0);

4748 if (!\_dbus_string_append (&homedir, override))

4749 goto failed;

4750

4751 \_dbus_verbose ("Using fake homedir for testing: %s\n",

4752 \_dbus_string_get_const_data (&homedir));

4753 }

4754 else

4755 {

4756 /\* Not strictly thread-safe, but if we fail at thread-safety here,

4757 \* the worst that will happen is some extra warnings. \*/

4758 static dbus_bool_t already_warned = FALSE;

4759 if (!already_warned)

4760 {

4761 \_dbus_warn ("Using %s for testing, set DBUS_TEST_HOMEDIR to avoid",

4762 \_dbus_string_get_const_data (&homedir));

4763 already_warned = TRUE;

4764 }

4765 }

4766 }

4767\#endif

4768

4769 \_dbus_string_init_const (&dotdir, ".dbus-keyrings");

4770 if (!\_dbus_concat_dir_and_file (&homedir,

4771 &dotdir))

4772 goto failed;

4773

4774 if (!\_dbus_string_copy (&homedir, 0,

4775 directory, \_dbus_string_get_length (directory))) {

4776 goto failed;

4777 }

4778

4779 \_dbus_string_free (&homedir);

4780 return TRUE;

4781

4782 failed:

4783 \_dbus_string_free (&homedir);

4784 return FALSE;

4785}

4786

4787/\* Documented in dbus-sysdeps-win.c, does nothing on Unix \*/

4788dbus_bool_t

4789\_dbus_daemon_unpublish_session_bus_address (void)

4790{

4791 return TRUE;

4792}

4793

4800dbus_bool_t

4801\_dbus_get_is_errno_eagain_or_ewouldblock (int e)

4802{

4803 /\* Avoid the -Wlogical-op GCC warning, which can be triggered when EAGAIN and

4804 \* EWOULDBLOCK are numerically equal, which is permitted as described by

4805 \* errno(3).

4806 \*/

4807\#if EAGAIN == EWOULDBLOCK

4808 return e == EAGAIN;

4809\#else

4810 return e == EAGAIN \|\| e == EWOULDBLOCK;

4811\#endif

4812}

4813

4821dbus_bool_t

4822\_dbus_delete_directory (const DBusString \*filename,

4823 DBusError \*error)

4824{

4825 const char \*filename_c;

4826

4827 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

4828

4829 filename_c = \_dbus_string_get_const_data (filename);

4830

4831 if (rmdir (filename_c) != 0)

4832 {

4833 dbus_set_error (error, DBUS_ERROR_FAILED,

4834 "Failed to remove directory %s: %s\n",

4835 filename_c, \_dbus_strerror (errno));

4836 return FALSE;

4837 }

4838

4839 return TRUE;

4840}

4841

4849dbus_bool_t

4850\_dbus_socket_can_pass_unix_fd (DBusSocket fd)

4851{

4852\#ifdef SCM_RIGHTS

4853 union {

4854 struct sockaddr sa;

4855 struct sockaddr_storage storage;

4856 struct sockaddr_un un;

4857 } sa_buf;

4858

4859 socklen_t sa_len = sizeof(sa_buf);

4860

4861 \_DBUS_ZERO(sa_buf);

4862

4863 if (getsockname(fd.fd, &sa_buf.sa, &sa_len) \< 0)

4864 return FALSE;

4865

4866 return sa_buf.sa.sa_family == AF_UNIX;

4867

4868\#else

4869 return FALSE;

4870

4871\#endif

4872}

4873

4874/\*

4875 \* Similar to Solaris fdwalk(3), but without the ability to stop iteration,

4876 \* and may call func for integers that are not actually valid fds.

4877 \*/

4878static void

4879act_on_fds_3_and_up (void (\*func) (int fd))

4880{

4881 int maxfds, i;

4882

4883\#if defined(\_\_linux\_\_) && defined(\_\_GLIBC\_\_)

4884 DIR \*d;

4885

4886 /\* On Linux we can optimize this a bit if /proc is available. If it

4887 isn't available, fall back to the brute force way. \*/

4888

4889 d = opendir ("/proc/self/fd");

4890 if (d)

4891 {

4892 for (;;)

4893 {

4894 struct dirent \*de;

4895 int fd;

4896 long l;

4897 char \*e = NULL;

4898

4899 de = readdir (d);

4900 if (!de)

4901 break;

4902

4903 if (de-\>d_name\[0\] == '.')

4904 continue;

4905

4906 errno = 0;

4907 l = strtol (de-\>d_name, &e, 10);

4908 if (errno != 0 \|\| e == NULL \|\| \*e != '\0')

4909 continue;

4910

4911 fd = (int) l;

4912 if (fd \< 3)

4913 continue;

4914

4915 if (fd == dirfd (d))

4916 continue;

4917

4918 func (fd);

4919 }

4920

4921 closedir (d);

4922 return;

4923 }

4924\#endif

4925

4926 maxfds = sysconf (\_SC_OPEN_MAX);

4927

4928 /\* Pick something reasonable if for some reason sysconf says

4929 \* unlimited.

4930 \*/

4931 if (maxfds \< 0)

4932 maxfds = 1024;

4933

4934 /\* close all inherited fds \*/

4935 for (i = 3; i \< maxfds; i++)

4936 func (i);

4937}

4938

4939/\* Some library implementations of closefrom() are not async-signal-safe,

4940 \* and we call \_dbus_close_all() after forking, so we only do this on

4941 \* operating systems where we know that closefrom() is a system call \*/

4942\#if defined(HAVE_CLOSEFROM) && ( \\

4943 defined(\_\_FreeBSD\_\_) \|\| \\

4944 defined(\_\_NetBSD\_\_) \|\| \\

4945 defined(\_\_OpenBSD\_\_) \|\| \\

4946 defined(\_\_sun\_\_) && defined(F_CLOSEFROM) \\

4947)

4948\#define CLOSEFROM_SIGNAL_SAFE 1

4949\#else

4950\#define CLOSEFROM_SIGNAL_SAFE 0

4951static void

4952close_ignore_error (int fd)

4953{

4954 close (fd);

4955}

4956\#endif

4957

4962void

4963\_dbus_close_all (void)

4964{

4965\#ifdef HAVE_CLOSE_RANGE

4966 if (close_range (3, INT_MAX, 0) == 0)

4967 return;

4968\#endif

4969

4970\#if CLOSEFROM_SIGNAL_SAFE

4971 closefrom (3);

4972\#else

4973 act_on_fds_3_and_up (close_ignore_error);

4974\#endif

4975}

4976

4981void

4982\_dbus_fd_set_all_close_on_exec (void)

4983{

4984\#if defined(HAVE_CLOSE_RANGE) && defined(CLOSE_RANGE_CLOEXEC)

4985 if (close_range (3, INT_MAX, CLOSE_RANGE_CLOEXEC) == 0)

4986 return;

4987\#endif

4988

4989 act_on_fds_3_and_up (\_dbus_fd_set_close_on_exec);

4990}

4991

5001dbus_bool_t

5002\_dbus_check_setuid (void)

5003{

5004 /\* TODO: get \_\_libc_enable_secure exported from glibc.

5005 \* See http://www.openwall.com/lists/owl-dev/2012/08/14/1

5006 \*/

5007\#if 0 && defined(HAVE_LIBC_ENABLE_SECURE)

5008 {

5009 /\* See glibc/include/unistd.h \*/

5010 extern int \_\_libc_enable_secure;

5011 return \_\_libc_enable_secure;

5012 }

5013\#elif defined(HAVE_ISSETUGID)

5014 /\* BSD: http://www.freebsd.org/cgi/man.cgi?query=issetugid&sektion=2 \*/

5015 return issetugid ();

5016\#else

5017 uid_t ruid, euid, suid; /\* Real, effective and saved user ID's \*/

5018 gid_t rgid, egid, sgid; /\* Real, effective and saved group ID's \*/

5019

5020 /\* We call into this function from \_dbus_threads_init_platform_specific()

5021 \* to make sure these are initialized before we start threading. \*/

5022 static dbus_bool_t check_setuid_initialised;

5023 static dbus_bool_t is_setuid;

5024

5025 if (\_DBUS_UNLIKELY (!check_setuid_initialised))

5026 {

5027\#ifdef HAVE_GETRESUID

5028 if (getresuid (&ruid, &euid, &suid) != 0 \|\|

5029 getresgid (&rgid, &egid, &sgid) != 0)

5030\#endif /\* HAVE_GETRESUID \*/

5031 {

5032 suid = ruid = getuid ();

5033 sgid = rgid = getgid ();

5034 euid = geteuid ();

5035 egid = getegid ();

5036 }

5037

5038 check_setuid_initialised = TRUE;

5039 is_setuid = (ruid != euid \|\| ruid != suid \|\|

5040 rgid != egid \|\| rgid != sgid);

5041

5042 }

5043 return is_setuid;

5044\#endif

5045}

5046

5054dbus_bool_t

5055\_dbus_append_address_from_socket (DBusSocket fd,

5056 DBusString \*address,

5057 DBusError \*error)

5058{

5059 union {

5060 struct sockaddr sa;

5061 struct sockaddr_storage storage;

5062 struct sockaddr_un un;

5063 struct sockaddr_in ipv4;

5064 struct sockaddr_in6 ipv6;

5065 } socket;

5066 char hostip\[INET6_ADDRSTRLEN\];

5067 socklen_t size = sizeof (socket);

5068 DBusString path_str;

5069 const char \*family_name = NULL;

5070 dbus_uint16_t port;

5071

5072 if (getsockname (fd.fd, &socket.sa, &size))

5073 goto err;

5074

5075 switch (socket.sa.sa_family)

5076 {

5077 case AF_UNIX:

5078 if (socket.un.sun_path\[0\]=='\0')

5079 {

5080 \_dbus_string_init_const (&path_str, &(socket.un.sun_path\[1\]));

5081 if (\_dbus_string_append (address, "unix:abstract=") &&

5082 \_dbus_address_append_escaped (address, &path_str))

5083 {

5084 return TRUE;

5085 }

5086 else

5087 {

5088 \_DBUS_SET_OOM (error);

5089 return FALSE;

5090 }

5091 }

5092 else

5093 {

5094 \_dbus_string_init_const (&path_str, socket.un.sun_path);

5095 if (\_dbus_string_append (address, "unix:path=") &&

5096 \_dbus_address_append_escaped (address, &path_str))

5097 {

5098 return TRUE;

5099 }

5100 else

5101 {

5102 \_DBUS_SET_OOM (error);

5103 return FALSE;

5104 }

5105 }

5106 /\* not reached \*/

5107 break;

5108

5109 case AF_INET:

5110\#ifdef AF_INET6

5111 case AF_INET6:

5112\#endif

5113 \_dbus_string_init_const (&path_str, hostip);

5114

5115 if (\_dbus_inet_sockaddr_to_string (&socket, size, hostip, sizeof (hostip),

5116 &family_name, &port, error))

5117 {

5118 if (\_dbus_string_append_printf (address, "tcp:family=%s,port=%u,host=",

5119 family_name, port) &&

5120 \_dbus_address_append_escaped (address, &path_str))

5121 {

5122 return TRUE;

5123 }

5124 else

5125 {

5126 \_DBUS_SET_OOM (error);

5127 return FALSE;

5128 }

5129 }

5130 else

5131 {

5132 return FALSE;

5133 }

5134 /\* not reached \*/

5135 break;

5136

5137 default:

5138 dbus_set_error (error,

5139 \_dbus_error_from_errno (EINVAL),

5140 "Failed to read address from socket: Unknown socket type.");

5141 return FALSE;

5142 }

5143 err:

5144 dbus_set_error (error,

5145 \_dbus_error_from_errno (errno),

5146 "Failed to read address from socket: %s",

5147 \_dbus_strerror (errno));

5148 return FALSE;

5149}

5150

5151int

5152\_dbus_save_socket_errno (void)

5153{

5154 return errno;

5155}

5156

5157void

5158\_dbus_restore_socket_errno (int saved_errno)

5159{

5160 errno = saved_errno;

5161}

5162

5163static const char \*syslog_tag = "dbus";

5164\#ifdef HAVE_SYSLOG_H

5165static DBusLogFlags log_flags = DBUS_LOG_FLAGS_STDERR;

5166\#endif

5167

5182void

5183\_dbus_init_system_log (const char \*tag,

5184 DBusLogFlags flags)

5185{

5186 /\* We never want to turn off logging completely \*/

5187 \_dbus_assert (

5188 (flags & (DBUS_LOG_FLAGS_STDERR \| DBUS_LOG_FLAGS_SYSTEM_LOG)) != 0);

5189

5190 syslog_tag = tag;

5191

5192\#ifdef HAVE_SYSLOG_H

5193 log_flags = flags;

5194

5195 if (log_flags & DBUS_LOG_FLAGS_SYSTEM_LOG)

5196 openlog (tag, LOG_PID, LOG_DAEMON);

5197\#endif

5198}

5199

5207void

5208\_dbus_logv (DBusSystemLogSeverity severity,

5209 const char \*msg,

5210 va_list args)

5211{

5212 va_list tmp;

5213\#ifdef HAVE_SYSLOG_H

5214 if (log_flags & DBUS_LOG_FLAGS_SYSTEM_LOG)

5215 {

5216 int flags = LOG_DAEMON \| LOG_WARNING;

5217 switch (severity)

5218 {

5219 case DBUS_SYSTEM_LOG_INFO:

5220 flags = LOG_DAEMON \| LOG_INFO;

5221 break;

5222 case DBUS_SYSTEM_LOG_WARNING:

5223 flags = LOG_DAEMON \| LOG_WARNING;

5224 break;

5225 case DBUS_SYSTEM_LOG_SECURITY:

5226 flags = LOG_AUTH \| LOG_NOTICE;

5227 break;

5228 case DBUS_SYSTEM_LOG_ERROR:

5229 flags = LOG_DAEMON\|LOG_CRIT;

5230 break;

5231 default:

5232 \_dbus_assert_not_reached ("invalid log severity");

5233 }

5234

5235 va_copy (tmp, args);

5236 vsyslog (flags, msg, tmp);

5237 va_end (tmp);

5238 }

5239

5240 /\* If we don't have syslog.h, we always behave as though stderr was in

5241 \* the flags \*/

5242 if (log_flags & DBUS_LOG_FLAGS_STDERR)

5243\#endif

5244 {

5245 va_copy (tmp, args);

5246 fprintf (stderr, "%s\[" DBUS_PID_FORMAT "\]: ", syslog_tag, \_dbus_getpid ());

5247 vfprintf (stderr, msg, tmp);

5248 fputc ('\n', stderr);

5249 va_end (tmp);

5250 }

5251}

5252

5253/\*

5254 \* Return the low-level representation of a socket error, as used by

5255 \* cross-platform socket APIs like inet_ntop(), send() and recv(). This

5256 \* is the standard errno on Unix, but is WSAGetLastError() on Windows.

5257 \*

5258 \* Some libdbus internal functions copy this into errno, but with

5259 \* hindsight that was probably a design flaw.

5260 \*/

5261int

5262\_dbus_get_low_level_socket_errno (void)

5263{

5264 return errno;

5265}

5266

5267/\* tests in dbus-sysdeps-util.c \*/

\_dbus_address_append_escaped

dbus_bool_t \_dbus_address_append_escaped(DBusString \*escaped, const DBusString \*unescaped)

Appends an escaped version of one string to another string, using the D-Bus address escaping mechanis...

**Definition** dbus-address.c:109

\_dbus_credentials_clear

void \_dbus_credentials_clear(DBusCredentials \*credentials)

Clear all credentials in the object.

**Definition** dbus-credentials.c:688

\_dbus_credentials_get_unix_uid

dbus_uid_t \_dbus_credentials_get_unix_uid(DBusCredentials \*credentials)

Gets the UNIX user ID in the credentials, or DBUS_UID_UNSET if the credentials object doesn't contain...

**Definition** dbus-credentials.c:440

\_dbus_credentials_take_pid_fd

\_DBUS_GNUC_NORETURN void \_dbus_credentials_take_pid_fd(DBusCredentials \*credentials, int pid_fd)

Add a UNIX process ID FD to the credentials.

**Definition** dbus-credentials.c:200

\_dbus_credentials_add_linux_security_label

dbus_bool_t \_dbus_credentials_add_linux_security_label(DBusCredentials \*credentials, const char \*label)

Add a Linux security label, as used by LSMs such as SELinux, Smack and AppArmor, to the credentials.

**Definition** dbus-credentials.c:317

\_dbus_credentials_take_unix_gids

void \_dbus_credentials_take_unix_gids(DBusCredentials \*credentials, dbus_gid_t \*gids, size_t n_gids)

Add UNIX group IDs to the credentials, replacing any group IDs that might already have been present.

**Definition** dbus-credentials.c:252

\_dbus_credentials_add_unix_uid

dbus_bool_t \_dbus_credentials_add_unix_uid(DBusCredentials \*credentials, dbus_uid_t uid)

Add a UNIX user ID to the credentials.

**Definition** dbus-credentials.c:220

\_dbus_credentials_add_pid

dbus_bool_t \_dbus_credentials_add_pid(DBusCredentials \*credentials, dbus_pid_t pid)

Add a UNIX process ID to the credentials.

**Definition** dbus-credentials.c:181

\_dbus_credentials_add_adt_audit_data

dbus_bool_t \_dbus_credentials_add_adt_audit_data(DBusCredentials \*credentials, void \*audit_data, dbus_int32_t size)

Add ADT audit data to the credentials.

**Definition** dbus-credentials.c:341

\_dbus_credentials_are_anonymous

dbus_bool_t \_dbus_credentials_are_anonymous(DBusCredentials \*credentials)

Checks whether a credentials object contains a user identity.

**Definition** dbus-credentials.c:558

DBUS_ERROR_INIT

\#define DBUS_ERROR_INIT

Expands to a suitable initializer for a DBusError on the stack.

**Definition** dbus-errors.h:64

dbus_move_error

void dbus_move_error(DBusError \*src, DBusError \*dest)

Moves an error src into dest, freeing src and overwriting dest.

**Definition** dbus-errors.c:281

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

\_DBUS_UNLOCK

\#define \_DBUS_UNLOCK(name)

Unlocks a global lock.

**Definition** dbus-internals.h:438

READ_END

\#define READ_END

Helps remember which end of the pipe is which.

**Definition** dbus-spawn-unix.c:895

WRITE_END

\#define WRITE_END

Helps remember which end of the pipe is which.

**Definition** dbus-spawn-unix.c:897

\_DBUS_LOCK

\#define \_DBUS_LOCK(name)

Locks a global lock, initializing it first if necessary.

**Definition** dbus-internals.h:437

\_dbus_error_from_errno

const char \* \_dbus_error_from_errno(int error_number)

Converts a UNIX errno, or Windows errno or WinSock error value into a DBusError name.

**Definition** dbus-sysdeps.c:565

\_dbus_generate_uuid

dbus_bool_t \_dbus_generate_uuid(DBusGUID \*uuid, DBusError \*error)

Generates a new UUID.

**Definition** dbus-internals.c:752

\_dbus_strdup

char \* \_dbus_strdup(const char \*str)

Duplicates a string.

**Definition** dbus-internals.c:621

\_dbus_read_uuid_file

dbus_bool_t \_dbus_read_uuid_file(const DBusString \*filename, DBusGUID \*uuid, dbus_bool_t create_if_not_found, DBusError \*error)

Reads (and optionally writes) a uuid to a file.

**Definition** dbus-internals.c:931

\_dbus_user_database_flush_system

void \_dbus_user_database_flush_system(void)

Flushes the system global user database;.

**Definition** dbus-userdb.c:396

\_dbus_get_local_machine_uuid_encoded

dbus_bool_t \_dbus_get_local_machine_uuid_encoded(DBusString \*uuid_str, DBusError \*error)

Gets the hex-encoded UUID of the machine this function is executed on.

**Definition** dbus-internals.c:983

\_dbus_write_uuid_file

dbus_bool_t \_dbus_write_uuid_file(const DBusString \*filename, const DBusGUID \*uuid, DBusError \*error)

Write the give UUID to a file.

**Definition** dbus-internals.c:882

\_dbus_homedir_from_uid

dbus_bool_t \_dbus_homedir_from_uid(dbus_uid_t uid, DBusString \*homedir)

Gets the home directory for the given user.

**Definition** dbus-userdb.c:466

\_dbus_warn

void \_dbus_warn(const char \*format,...)

Prints a warning message to stderr.

**Definition** dbus-internals.c:278

\_DBUS_N_ELEMENTS

\#define \_DBUS_N_ELEMENTS(array)

Computes the number of elements in a fixed-size array using sizeof().

**Definition** dbus-internals.h:189

\_DBUS_ZERO

\#define \_DBUS_ZERO(object)

Sets all bits in an object to zero.

**Definition** dbus-internals.h:194

\_DBUS_INT32_MAX

\#define \_DBUS_INT32_MAX

Maximum value of type "int32".

**Definition** dbus-internals.h:323

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

DBUS_MAXIMUM_MESSAGE_UNIX_FDS

\#define DBUS_MAXIMUM_MESSAGE_UNIX_FDS

The maximum total number of unix fds in a message.

**Definition** dbus-protocol.h:220

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

DBUS_ERROR_FAILED

\#define DBUS_ERROR_FAILED

A generic error; "something went wrong" - see the error message for more.

**Definition** dbus-protocol.h:361

DBUS_ERROR_SPAWN_EXEC_FAILED

\#define DBUS_ERROR_SPAWN_EXEC_FAILED

While starting a new process, the exec() call failed.

**Definition** dbus-protocol.h:422

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

\_dbus_string_copy

dbus_bool_t \_dbus_string_copy(const DBusString \*source, int start, DBusString \*dest, int insert_at)

Like \_dbus_string_move(), but does not delete the section of the source string that's copied to the d...

**Definition** dbus-string.c:1345

\_dbus_string_init_preallocated

dbus_bool_t \_dbus_string_init_preallocated(DBusString \*str, int allocate_size)

Initializes a string that can be up to the given allocation size before it has to realloc.

**Definition** dbus-string.c:139

\_dbus_string_find

dbus_bool_t \_dbus_string_find(const DBusString \*str, int start, const char \*substr, int \*found)

Finds the given substring in the string, returning TRUE and filling in the byte index where the subst...

**Definition** dbus-string.c:1666

\_dbus_string_get_data_len

char \* \_dbus_string_get_data_len(DBusString \*str, int start, int len)

Gets a sub-portion of the raw character buffer from the string.

**Definition** dbus-string.c:535

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

\_dbus_string_parse_uint

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_parse_uint(const DBusString \*str, int start, unsigned long \*value_return, int \*end_return)

Parses an unsigned integer contained in a DBusString.

**Definition** dbus-sysdeps.c:410

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

\_dbus_fd_clear_close_on_exec

void \_dbus_fd_clear_close_on_exec(int fd)

Sets the file descriptor to not be close-on-exec.

**Definition** dbus-sysdeps-unix.c:3705

\_dbus_fd_set_all_close_on_exec

void \_dbus_fd_set_all_close_on_exec(void)

Sets all file descriptors except the first three (i.e.

**Definition** dbus-sysdeps-unix.c:4982

\_dbus_close

dbus_bool_t \_dbus_close(int fd, DBusError \*error)

Closes a file descriptor.

**Definition** dbus-sysdeps-unix.c:3727

\_dbus_write

int \_dbus_write(int fd, const DBusString \*buffer, int start, int len)

Thin wrapper around the write() system call that writes a part of a DBusString and handles EINTR for ...

**Definition** dbus-sysdeps-unix.c:827

\_dbus_write_two

int \_dbus_write_two(int fd, const DBusString \*buffer1, int start1, int len1, const DBusString \*buffer2, int start2, int len2)

Like \_dbus_write() but will use writev() if possible to write both buffers in sequence.

**Definition** dbus-sysdeps-unix.c:873

\_dbus_lookup_launchd_socket

dbus_bool_t \_dbus_lookup_launchd_socket(DBusString \*socket_path, const char \*launchd_env_var, DBusError \*error)

quries launchd for a specific env var which holds the socket path.

**Definition** dbus-sysdeps-unix.c:4486

\_dbus_listen_systemd_sockets

int \_dbus_listen_systemd_sockets(DBusSocket \*\*fds, DBusError \*error)

Acquires one or more sockets passed in from systemd.

**Definition** dbus-sysdeps-unix.c:1299

\_dbus_append_address_from_socket

dbus_bool_t \_dbus_append_address_from_socket(DBusSocket fd, DBusString \*address, DBusError \*error)

Read the address from the socket and append it to the string.

**Definition** dbus-sysdeps-unix.c:5055

\_dbus_user_info_fill

dbus_bool_t \_dbus_user_info_fill(DBusUserInfo \*info, const DBusString \*username, DBusError \*error)

Gets user info for the given username.

**Definition** dbus-sysdeps-unix.c:2966

\_dbus_close_all

void \_dbus_close_all(void)

Closes all file descriptors except the first three (i.e.

**Definition** dbus-sysdeps-unix.c:4963

\_dbus_dup

int \_dbus_dup(int fd, DBusError \*error)

Duplicates a file descriptor.

**Definition** dbus-sysdeps-unix.c:3755

\_dbus_fd_set_close_on_exec

void \_dbus_fd_set_close_on_exec(int fd)

Sets the file descriptor to be close on exec.

**Definition** dbus-sysdeps-unix.c:3683

\_dbus_read

int \_dbus_read(int fd, DBusString \*buffer, int count)

Thin wrapper around the read() system call that appends the data it reads to the DBusString buffer.

**Definition** dbus-sysdeps-unix.c:767

\_dbus_ensure_standard_fds

dbus_bool_t \_dbus_ensure_standard_fds(DBusEnsureStandardFdsFlags flags, const char \*\*error_str_p)

Ensure that the standard file descriptors stdin, stdout and stderr are open, by opening /dev/null if ...

**Definition** dbus-sysdeps-unix.c:179

\_dbus_geteuid

dbus_uid_t \_dbus_geteuid(void)

Gets our effective UID.

**Definition** dbus-sysdeps-unix.c:3145

\_dbus_user_info_fill_uid

dbus_bool_t \_dbus_user_info_fill_uid(DBusUserInfo \*info, dbus_uid_t uid, DBusError \*error)

Gets user info for the given user ID.

**Definition** dbus-sysdeps-unix.c:2983

\_dbus_logv

void \_dbus_logv(DBusSystemLogSeverity severity, const char \*msg, va_list args)

Log a message to the system log file (e.g.

**Definition** dbus-sysdeps-unix.c:5208

\_dbus_get_monotonic_time

void \_dbus_get_monotonic_time(dbus_int64_t \*tv_sec, long \*tv_usec)

Get current time, as in gettimeofday().

**Definition** dbus-sysdeps-unix.c:3381

\_dbus_read_local_machine_uuid

dbus_bool_t \_dbus_read_local_machine_uuid(DBusGUID \*machine_id, dbus_bool_t create_if_not_found, DBusError \*error)

Reads the uuid of the machine we're running on from the dbus configuration.

**Definition** dbus-sysdeps-unix.c:4421

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

**Definition** dbus-sysdeps-unix.c:4801

\_dbus_pid_for_log

unsigned long \_dbus_pid_for_log(void)

The only reason this is separate from \_dbus_getpid() is to allow it on Windows for logging but not fo...

**Definition** dbus-sysdeps-unix.c:3157

dbus_pid_t

unsigned long dbus_pid_t

A process ID.

**Definition** dbus-sysdeps.h:139

\_dbus_read_socket

int \_dbus_read_socket(DBusSocket fd, DBusString \*buffer, int count)

Like \_dbus_read(), but only works on sockets so is available on Windows.

**Definition** dbus-sysdeps-unix.c:338

\_dbus_exit

void \_dbus_exit(int code)

Exit the process, returning the given value.

**Definition** dbus-sysdeps-unix.c:3641

\_DBUS_POLLERR

\#define \_DBUS_POLLERR

Error condition.

**Definition** dbus-sysdeps.h:450

\_dbus_socket_can_pass_unix_fd

dbus_bool_t \_dbus_socket_can_pass_unix_fd(DBusSocket fd)

Checks whether file descriptors may be passed via the socket.

**Definition** dbus-sysdeps-unix.c:4850

\_dbus_write_socket

int \_dbus_write_socket(DBusSocket fd, const DBusString \*buffer, int start, int len)

Like \_dbus_write(), but only supports sockets and is thus available on Windows.

**Definition** dbus-sysdeps-unix.c:356

\_dbus_atomic_set_nonzero

void \_dbus_atomic_set_nonzero(DBusAtomic \*atomic)

Atomically set the value of an integer to something nonzero.

**Definition** dbus-sysdeps-unix.c:3279

\_dbus_socketpair

dbus_bool_t \_dbus_socketpair(DBusSocket \*fd1, DBusSocket \*fd2, dbus_bool_t blocking, DBusError \*error)

Creates pair of connect sockets (as in socketpair()).

**Definition** dbus-sysdeps-unix.c:3884

dbus_gid_t

unsigned long dbus_gid_t

A group ID.

**Definition** dbus-sysdeps.h:143

\_dbus_read_socket_with_unix_fds

int \_dbus_read_socket_with_unix_fds(DBusSocket fd, DBusString \*buffer, int count, int \*fds, unsigned int \*n_fds)

Like \_dbus_read_socket() but also tries to read unix fds from the socket.

**Definition** dbus-sysdeps-unix.c:394

\_dbus_append_keyring_directory_for_credentials

dbus_bool_t \_dbus_append_keyring_directory_for_credentials(DBusString \*directory, DBusCredentials \*credentials)

Appends the directory in which a keyring for the given credentials should be stored.

**Definition** dbus-sysdeps-unix.c:4721

DBUS_UID_UNSET

\#define DBUS_UID_UNSET

an invalid UID used to represent an uninitialized dbus_uid_t field

**Definition** dbus-sysdeps.h:148

\_dbus_atomic_dec

dbus_int32_t \_dbus_atomic_dec(DBusAtomic \*atomic)

Atomically decrement an integer.

**Definition** dbus-sysdeps-unix.c:3205

\_dbus_read_credentials_socket

dbus_bool_t \_dbus_read_credentials_socket(DBusSocket client_fd, DBusCredentials \*credentials, DBusError \*error)

Reads a single byte which must be nul (an error occurs otherwise), and reads unix credentials if avai...

**Definition** dbus-sysdeps-unix.c:2209

DBUS_PID_UNSET

\#define DBUS_PID_UNSET

an invalid PID used to represent an uninitialized dbus_pid_t field

**Definition** dbus-sysdeps.h:146

\_dbus_getenv

const char \* \_dbus_getenv(const char \*varname)

Wrapper for getenv().

**Definition** dbus-sysdeps.c:197

\_dbus_listen_unix_socket

DBusSocket \_dbus_listen_unix_socket(const char \*path, dbus_bool_t abstract, DBusError \*error)

Creates a socket and binds it to the given path, then listens on the socket.

**Definition** dbus-sysdeps-unix.c:1170

\_dbus_getpid

dbus_pid_t \_dbus_getpid(void)

Gets our process ID.

**Definition** dbus-sysdeps-unix.c:3127

\_dbus_atomic_get

dbus_int32_t \_dbus_atomic_get(DBusAtomic \*atomic)

Atomically get the value of an integer.

**Definition** dbus-sysdeps-unix.c:3233

\_dbus_set_socket_nonblocking

dbus_bool_t \_dbus_set_socket_nonblocking(DBusSocket fd, DBusError \*error)

Sets a file descriptor to be nonblocking.

**Definition** dbus-sysdeps-unix.c:3797

\_dbus_lookup_session_address

dbus_bool_t \_dbus_lookup_session_address(dbus_bool_t \*supported, DBusString \*address, DBusError \*error)

Determines the address of the session bus by querying a platform-specific method.

**Definition** dbus-sysdeps-unix.c:4670

\_dbus_connect_tcp_socket

DBusSocket \_dbus_connect_tcp_socket(const char \*host, const char \*port, const char \*family, DBusError \*error)

Creates a socket and connects to a socket at the given host and port.

**Definition** dbus-sysdeps-unix.c:1449

\_dbus_disable_sigpipe

void \_dbus_disable_sigpipe(void)

signal (SIGPIPE, SIG_IGN);

**Definition** dbus-sysdeps-unix.c:3670

\_dbus_check_setuid

dbus_bool_t \_dbus_check_setuid(void)

NOTE: If you modify this function, please also consider making the corresponding change in GLib.

**Definition** dbus-sysdeps-unix.c:5002

\_dbus_sleep_milliseconds

void \_dbus_sleep_milliseconds(int milliseconds)

Sleeps the given number of milliseconds.

**Definition** dbus-sysdeps-unix.c:3542

DBUS_GID_UNSET

\#define DBUS_GID_UNSET

an invalid GID used to represent an uninitialized dbus_gid_t field

**Definition** dbus-sysdeps.h:150

\_dbus_resolve_pid_fd

dbus_pid_t \_dbus_resolve_pid_fd(int pid_fd)

Resolve the PID from the PID FD, if any.

**Definition** dbus-sysdeps-unix.c:3045

\_dbus_check_dir_is_private_to_user

dbus_bool_t \_dbus_check_dir_is_private_to_user(DBusString \*dir, DBusError \*error)

Checks to make sure the given directory is private to the user.

**Definition** dbus-sysdeps-unix.c:2644

\_DBUS_POLLIN

\#define \_DBUS_POLLIN

There is data to read.

**Definition** dbus-sysdeps.h:444

\_dbus_listen_tcp_socket

int \_dbus_listen_tcp_socket(const char \*host, const char \*port, const char \*family, DBusString \*retport, const char \*\*retfamily, DBusSocket \*\*fds_p, DBusError \*error)

Creates a socket and binds it to the given path, then listens on the socket.

**Definition** dbus-sysdeps-unix.c:1606

\_dbus_send_credentials_socket

dbus_bool_t \_dbus_send_credentials_socket(DBusSocket server_fd, DBusError \*error)

Sends a single nul byte with our UNIX credentials as ancillary data.

**Definition** dbus-sysdeps-unix.c:2568

\_dbus_getuid

dbus_uid_t \_dbus_getuid(void)

Gets our UID.

**Definition** dbus-sysdeps-unix.c:3136

\_dbus_credentials_add_from_current_process

dbus_bool_t \_dbus_credentials_add_from_current_process(DBusCredentials \*credentials)

Adds the most important credentials of the current process (the uid and pid) to the passed-in credent...

**Definition** dbus-sysdeps-unix.c:3005

\_dbus_close_socket

dbus_bool_t \_dbus_close_socket(DBusSocket \*fd, DBusError \*error)

Closes a socket and invalidates it.

**Definition** dbus-sysdeps-unix.c:314

\_dbus_connect_unix_socket

DBusSocket \_dbus_connect_unix_socket(const char \*path, dbus_bool_t abstract, DBusError \*error)

Creates a socket and connects it to the UNIX domain socket at the given path.

**Definition** dbus-sysdeps-unix.c:957

\_dbus_atomic_set_zero

void \_dbus_atomic_set_zero(DBusAtomic \*atomic)

Atomically set the value of an integer to 0.

**Definition** dbus-sysdeps-unix.c:3258

\_dbus_atomic_inc

dbus_int32_t \_dbus_atomic_inc(DBusAtomic \*atomic)

Atomically increments an integer.

**Definition** dbus-sysdeps-unix.c:3178

\_dbus_generate_random_bytes

dbus_bool_t \_dbus_generate_random_bytes(DBusString \*str, int n_bytes, DBusError \*error)

Generates the given number of securely random bytes, using the best mechanism we can come up with.

**Definition** dbus-sysdeps-unix.c:3572

DBUS_GID_FORMAT

\#define DBUS_GID_FORMAT

an appropriate printf format for dbus_gid_t

**Definition** dbus-sysdeps.h:157

\_dbus_printf_string_upper_bound

int \_dbus_printf_string_upper_bound(const char \*format, va_list args)

Measure the length of the given format string and arguments, not including the terminating nul.

**Definition** dbus-sysdeps-unix.c:3959

\_dbus_delete_directory

dbus_bool_t \_dbus_delete_directory(const DBusString \*filename, DBusError \*error)

Removes a directory; Directory must be empty.

**Definition** dbus-sysdeps-unix.c:4822

DBUS_UID_FORMAT

\#define DBUS_UID_FORMAT

an appropriate printf format for dbus_uid_t

**Definition** dbus-sysdeps.h:155

\_dbus_poll

int \_dbus_poll(DBusPollFD \*fds, int n_fds, int timeout_milliseconds)

Wrapper for poll().

**Definition** dbus-sysdeps-unix.c:3303

\_dbus_get_autolaunch_address

dbus_bool_t \_dbus_get_autolaunch_address(const char \*scope, DBusString \*address, DBusError \*error)

Returns the address of a new session bus.

**Definition** dbus-sysdeps-unix.c:4299

\_dbus_write_socket_two

int \_dbus_write_socket_two(DBusSocket fd, const DBusString \*buffer1, int start1, int len1, const DBusString \*buffer2, int start2, int len2)

Like \_dbus_write_two() but only works on sockets and is thus available on Windows.

**Definition** dbus-sysdeps-unix.c:694

\_dbus_concat_dir_and_file

dbus_bool_t \_dbus_concat_dir_and_file(DBusString \*dir, const DBusString \*next_component)

Appends the given filename to the given directory.

**Definition** dbus-sysdeps-unix.c:3497

\_dbus_connect_exec

DBusSocket \_dbus_connect_exec(const char \*path, char \*const argv\[\], DBusError \*error)

Creates a UNIX domain socket and connects it to the specified process to execute.

**Definition** dbus-sysdeps-unix.c:1054

\_dbus_print_backtrace

void \_dbus_print_backtrace(void)

On GNU libc systems, print a crude backtrace to stderr.

**Definition** dbus-sysdeps-unix.c:3842

\_dbus_get_real_time

void \_dbus_get_real_time(dbus_int64_t \*tv_sec, long \*tv_usec)

Get current time, as in gettimeofday().

**Definition** dbus-sysdeps-unix.c:3412

\_dbus_init_system_log

void \_dbus_init_system_log(const char \*tag, DBusLogFlags flags)

Initialize the system log.

**Definition** dbus-sysdeps-unix.c:5183

\_dbus_accept

DBusSocket \_dbus_accept(DBusSocket listen_fd)

Accepts a connection on a listening socket.

**Definition** dbus-sysdeps-unix.c:2589

\_DBUS_MAX_SUN_PATH_LENGTH

\#define \_DBUS_MAX_SUN_PATH_LENGTH

Maximum length of the path to a UNIX domain socket, sockaddr_un::sun_path member.

**Definition** dbus-sysdeps.h:765

\_dbus_append_user_from_current_process

dbus_bool_t \_dbus_append_user_from_current_process(DBusString \*str)

Append to the string the identity we would like to have when we authenticate, on UNIX this is the cur...

**Definition** dbus-sysdeps-unix.c:3117

\_dbus_flush_caches

void \_dbus_flush_caches(void)

Called when the bus daemon is signaled to reload its configuration; any caches should be nuked.

**Definition** dbus-sysdeps-unix.c:4702

\_dbus_get_tmpdir

const char \* \_dbus_get_tmpdir(void)

Gets the temporary files directory by inspecting the environment variables TMPDIR,...

**Definition** dbus-sysdeps-unix.c:4029

DBUS_PID_FORMAT

\#define DBUS_PID_FORMAT

an appropriate printf format for dbus_pid_t

**Definition** dbus-sysdeps.h:153

\_dbus_ensure_directory

dbus_bool_t \_dbus_ensure_directory(const DBusString \*filename, DBusError \*error)

Creates a directory; succeeds if the directory is created or already existed.

**Definition** dbus-sysdeps-unix.c:3434

\_dbus_create_directory

dbus_bool_t \_dbus_create_directory(const DBusString \*filename, DBusError \*error)

Creates a directory.

**Definition** dbus-sysdeps-unix.c:3466

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

DBusSocket

Socket interface.

**Definition** dbus-sysdeps.h:185

DBusString

**Definition** dbus-string.h:47

DBusUserInfo

Information about a UNIX user.

**Definition** dbus-sysdeps-unix.h:93

DBusUserInfo::n_group_ids

int n_group_ids

Size of group IDs array.

**Definition** dbus-sysdeps-unix.h:98

DBusUserInfo::uid

dbus_uid_t uid

UID.

**Definition** dbus-sysdeps-unix.h:95

DBusUserInfo::homedir

char \* homedir

Home directory.

**Definition** dbus-sysdeps-unix.h:100

DBusUserInfo::group_ids

dbus_gid_t \* group_ids

Groups IDs, including above primary group.

**Definition** dbus-sysdeps-unix.h:97

DBusUserInfo::username

char \* username

Username.

**Definition** dbus-sysdeps-unix.h:99

DBusUserInfo::primary_gid

dbus_gid_t primary_gid

GID.

**Definition** dbus-sysdeps-unix.h:96

DBusGUID

A globally unique ID ; we have one for each DBusServer, and also one for each machine with libdbus in...

**Definition** dbus-internals.h:458
