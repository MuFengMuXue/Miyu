dbus-sysdeps-util-unix.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-sysdeps-util-unix.c Would be in dbus-sysdeps-unix.c, but not used in libdbus

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

28\#include "dbus-sysdeps.h"

29\#include "dbus-sysdeps-unix.h"

30\#include "dbus-internals.h"

31\#include "dbus-list.h"

32\#include "dbus-pipe.h"

33\#include "dbus-protocol.h"

34\#include "dbus-string.h"

35\#define DBUS_USERDB_INCLUDES_PRIVATE 1

36\#include "dbus-userdb.h"

37\#include "dbus-test.h"

38

39\#include \<sys/types.h\>

40\#include \<stdio.h\>

41\#include \<stdlib.h\>

42\#include \<string.h\>

43\#include \<signal.h\>

44\#include \<unistd.h\>

45\#include \<stdio.h\>

46\#include \<errno.h\>

47\#include \<fcntl.h\>

48\#include \<limits.h\>

49\#include \<sys/stat.h\>

50\#ifdef HAVE_SYS_RESOURCE_H

51\#include \<sys/resource.h\>

52\#endif

53\#include \<grp.h\>

54\#include \<sys/socket.h\>

55\#include \<dirent.h\>

56\#include \<sys/un.h\>

57

58\#ifdef HAVE_SYS_PRCTL_H

59\#include \<sys/prctl.h\>

60\#endif

61

62\#ifdef HAVE_SYSTEMD

63\#include \<systemd/sd-daemon.h\>

64\#endif

65

66\#ifndef O_BINARY

67\#define O_BINARY 0

68\#endif

69

85dbus_bool_t

86\_dbus_become_daemon (const DBusString \*pidfile,

87 DBusPipe \*print_pid_pipe,

88 DBusError \*error,

89 dbus_bool_t keep_umask)

90{

91 const char \*s;

92 pid_t child_pid;

93 DBusEnsureStandardFdsFlags flags;

94

95 \_dbus_verbose ("Becoming a daemon...\n");

96

97 \_dbus_verbose ("chdir to /\n");

98 if (chdir ("/") \< 0)

99 {

100 dbus_set_error (error, DBUS_ERROR_FAILED,

101 "Could not chdir() to root directory");

102 return FALSE;

103 }

104

105 \_dbus_verbose ("forking...\n");

106

107 /\* Make sure our output buffers aren't redundantly printed by both the

108 \* parent and the child \*/

109 fflush (stdout);

110 fflush (stderr);

111

112 switch ((child_pid = fork ()))

113 {

114 case -1:

115 \_dbus_verbose ("fork failed\n");

116 dbus_set_error (error, \_dbus_error_from_errno (errno),

117 "Failed to fork daemon: %s", \_dbus_strerror (errno));

118 return FALSE;

119 break;

120

121 case 0:

122 \_dbus_verbose ("in child, closing std file descriptors\n");

123

124 flags = DBUS_FORCE_STDIN_NULL \| DBUS_FORCE_STDOUT_NULL;

125 s = \_dbus_getenv ("DBUS_DEBUG_OUTPUT");

126

127 if (s == NULL \|\| \*s == '\0')

128 flags \|= DBUS_FORCE_STDERR_NULL;

129 else

130 \_dbus_verbose ("keeping stderr open due to DBUS_DEBUG_OUTPUT\n");

131

132 if (!\_dbus_ensure_standard_fds (flags, &s))

133 {

134 \_dbus_warn ("%s: %s", s, \_dbus_strerror (errno));

135 \_exit (1);

136 }

137

138 if (!keep_umask)

139 {

140 /\* Get a predictable umask \*/

141 \_dbus_verbose ("setting umask\n");

142 umask (022);

143 }

144

145 \_dbus_verbose ("calling setsid()\n");

146 if (setsid () == -1)

147 \_dbus_assert_not_reached ("setsid() failed");

148

149 break;

150

151 default:

152 if (!\_dbus_write_pid_to_file_and_pipe (pidfile, print_pid_pipe,

153 child_pid, error))

154 {

155 \_dbus_verbose ("pid file or pipe write failed: %s\n",

156 error-\>message);

157 kill (child_pid, SIGTERM);

158 return FALSE;

159 }

160

161 \_dbus_verbose ("parent exiting\n");

162 \_exit (0);

163 break;

164 }

165

166 return TRUE;

167}

168

169

178static dbus_bool_t

179\_dbus_write_pid_file (const DBusString \*filename,

180 unsigned long pid,

181 DBusError \*error)

182{

183 const char \*cfilename;

184 int fd;

185 FILE \*f;

186

187 cfilename = \_dbus_string_get_const_data (filename);

188

189 fd = open (cfilename, O_WRONLY\|O_CREAT\|O_EXCL\|O_BINARY, 0644);

190

191 if (fd \< 0)

192 {

193 dbus_set_error (error, \_dbus_error_from_errno (errno),

194 "Failed to open \\%s\\: %s", cfilename,

195 \_dbus_strerror (errno));

196 return FALSE;

197 }

198

199 if ((f = fdopen (fd, "w")) == NULL)

200 {

201 dbus_set_error (error, \_dbus_error_from_errno (errno),

202 "Failed to fdopen fd %d: %s", fd, \_dbus_strerror (errno));

203 \_dbus_close (fd, NULL);

204 return FALSE;

205 }

206

207 if (fprintf (f, "%lu\n", pid) \< 0)

208 {

209 dbus_set_error (error, \_dbus_error_from_errno (errno),

210 "Failed to write to \\%s\\: %s", cfilename,

211 \_dbus_strerror (errno));

212

213 fclose (f);

214 return FALSE;

215 }

216

217 if (fclose (f) == EOF)

218 {

219 dbus_set_error (error, \_dbus_error_from_errno (errno),

220 "Failed to close \\%s\\: %s", cfilename,

221 \_dbus_strerror (errno));

222 return FALSE;

223 }

224

225 return TRUE;

226}

227

239dbus_bool_t

240\_dbus_write_pid_to_file_and_pipe (const DBusString \*pidfile,

241 DBusPipe \*print_pid_pipe,

242 dbus_pid_t pid_to_write,

243 DBusError \*error)

244{

245 if (pidfile)

246 {

247 \_dbus_verbose ("writing pid file %s\n", \_dbus_string_get_const_data (pidfile));

248 if (!\_dbus_write_pid_file (pidfile,

249 pid_to_write,

250 error))

251 {

252 \_dbus_verbose ("pid file write failed\n");

253 \_DBUS_ASSERT_ERROR_IS_SET(error);

254 return FALSE;

255 }

256 }

257 else

258 {

259 \_dbus_verbose ("No pid file requested\n");

260 }

261

262 if (print_pid_pipe != NULL && \_dbus_pipe_is_valid (print_pid_pipe))

263 {

264 DBusString pid;

265 int bytes;

266

267 \_dbus_verbose ("writing our pid to pipe %d\n",

268 print_pid_pipe-\>fd);

269

270 if (!\_dbus_string_init (&pid))

271 {

272 \_DBUS_SET_OOM (error);

273 return FALSE;

274 }

275

276 if (!\_dbus_string_append_printf (&pid, DBUS_PID_FORMAT "\n", pid_to_write))

277 {

278 \_dbus_string_free (&pid);

279 \_DBUS_SET_OOM (error);

280 return FALSE;

281 }

282

283 bytes = \_dbus_string_get_length (&pid);

284 if (\_dbus_pipe_write (print_pid_pipe, &pid, 0, bytes, error) != bytes)

285 {

286 /\* \_dbus_pipe_write sets error only on failure, not short write \*/

287 if (error != NULL && !dbus_error_is_set(error))

288 {

289 dbus_set_error (error, DBUS_ERROR_FAILED,

290 "Printing message bus PID: did not write enough bytes\n");

291 }

292 \_dbus_string_free (&pid);

293 return FALSE;

294 }

295

296 \_dbus_string_free (&pid);

297 }

298 else

299 {

300 \_dbus_verbose ("No pid pipe to write to\n");

301 }

302

303 return TRUE;

304}

305

312dbus_bool_t

313\_dbus_verify_daemon_user (const char \*user)

314{

315 DBusString u;

316

317 \_dbus_string_init_const (&u, user);

318

319 return \_dbus_get_user_id_and_primary_group (&u, NULL, NULL);

320}

321

322

323/\* The HAVE_LIBAUDIT case lives in selinux.c \*/

324\#ifndef HAVE_LIBAUDIT

332dbus_bool_t

333\_dbus_change_to_daemon_user (const char \*user,

334 DBusError \*error)

335{

336 dbus_uid_t uid;

337 dbus_gid_t gid;

338 DBusString u;

339

340 \_dbus_string_init_const (&u, user);

341

342 if (!\_dbus_get_user_id_and_primary_group (&u, &uid, &gid))

343 {

344 dbus_set_error (error, DBUS_ERROR_FAILED,

345 "User '%s' does not appear to exist?",

346 user);

347 return FALSE;

348 }

349

350 /\* setgroups() only works if we are a privileged process,

351 \* so we don't return error on failure; the only possible

352 \* failure is that we don't have perms to do it.

353 \*

354 \* not sure this is right, maybe if setuid()

355 \* is going to work then setgroups() should also work.

356 \*/

357 if (setgroups (0, NULL) \< 0)

358 \_dbus_warn ("Failed to drop supplementary groups: %s",

359 \_dbus_strerror (errno));

360

361 /\* Set GID first, or the setuid may remove our permission

362 \* to change the GID

363 \*/

364 if (setgid (gid) \< 0)

365 {

366 dbus_set_error (error, \_dbus_error_from_errno (errno),

367 "Failed to set GID to %lu: %s", gid,

368 \_dbus_strerror (errno));

369 return FALSE;

370 }

371

372 if (setuid (uid) \< 0)

373 {

374 dbus_set_error (error, \_dbus_error_from_errno (errno),

375 "Failed to set UID to %lu: %s", uid,

376 \_dbus_strerror (errno));

377 return FALSE;

378 }

379

380 return TRUE;

381}

382\#endif /\* !HAVE_LIBAUDIT \*/

383

384\#ifdef HAVE_SETRLIMIT

385

386/\* We assume that if we have setrlimit, we also have getrlimit and

387 \* struct rlimit.

388 \*/

389

390struct DBusRLimit {

391 struct rlimit lim;

392};

393

394DBusRLimit \*

395\_dbus_rlimit_save_fd_limit (DBusError \*error)

396{

397 DBusRLimit \*self;

398

399 self = dbus_new0 (DBusRLimit, 1);

400

401 if (self == NULL)

402 {

403 \_DBUS_SET_OOM (error);

404 return NULL;

405 }

406

407 if (getrlimit (RLIMIT_NOFILE, &self-\>lim) \< 0)

408 {

409 dbus_set_error (error, \_dbus_error_from_errno (errno),

410 "Failed to get fd limit: %s", \_dbus_strerror (errno));

411 dbus_free (self);

412 return NULL;

413 }

414

415 return self;

416}

417

418/\* Enough fds that we shouldn't run out, even if several uids work

419 \* together to carry out a denial-of-service attack. This happens to be

420 \* the same number that systemd \< 234 would normally use. \*/

421\#define ENOUGH_FDS 65536

422

423dbus_bool_t

424\_dbus_rlimit_raise_fd_limit (DBusError \*error)

425{

426 struct rlimit old, lim;

427

428 if (getrlimit (RLIMIT_NOFILE, &lim) \< 0)

429 {

430 dbus_set_error (error, \_dbus_error_from_errno (errno),

431 "Failed to get fd limit: %s", \_dbus_strerror (errno));

432 return FALSE;

433 }

434

435 old = lim;

436

437 if (getuid () == 0)

438 {

439 /\* We are privileged, so raise the soft limit to at least

440 \* ENOUGH_FDS, and the hard limit to at least the desired soft

441 \* limit. This assumes we can exercise CAP_SYS_RESOURCE on Linux,

442 \* or other OSs' equivalents. \*/

443 if (lim.rlim_cur != RLIM_INFINITY &&

444 lim.rlim_cur \< ENOUGH_FDS)

445 lim.rlim_cur = ENOUGH_FDS;

446

447 if (lim.rlim_max != RLIM_INFINITY &&

448 lim.rlim_max \< lim.rlim_cur)

449 lim.rlim_max = lim.rlim_cur;

450 }

451

452 /\* Raise the soft limit to match the hard limit, which we can do even

453 \* if we are unprivileged. In particular, systemd \>= 240 will normally

454 \* set rlim_cur to 1024 and rlim_max to 512\*1024, recent Debian

455 \* versions end up setting rlim_cur to 1024 and rlim_max to 1024\*1024,

456 \* and older and non-systemd Linux systems would typically set rlim_cur

457 \* to 1024 and rlim_max to 4096. \*/

458 if (lim.rlim_max == RLIM_INFINITY \|\| lim.rlim_cur \< lim.rlim_max)

459 {

460\#if defined(\_\_APPLE\_\_) && defined(\_\_MACH\_\_)

461 /\* macOS 10.5 and above no longer allows RLIM_INFINITY for rlim_cur \*/

462 lim.rlim_cur = MIN (OPEN_MAX, lim.rlim_max);

463\#else

464 lim.rlim_cur = lim.rlim_max;

465\#endif

466 }

467

468 /\* Early-return if there is nothing to do. \*/

469 if (lim.rlim_max == old.rlim_max &&

470 lim.rlim_cur == old.rlim_cur)

471 return TRUE;

472

473 if (setrlimit (RLIMIT_NOFILE, &lim) \< 0)

474 {

475 dbus_set_error (error, \_dbus_error_from_errno (errno),

476 "Failed to set fd limit to %lu: %s",

477 (unsigned long) lim.rlim_cur,

478 \_dbus_strerror (errno));

479 return FALSE;

480 }

481

482 return TRUE;

483}

484

485dbus_bool_t

486\_dbus_rlimit_restore_fd_limit (DBusRLimit \*saved,

487 DBusError \*error)

488{

489 if (setrlimit (RLIMIT_NOFILE, &saved-\>lim) \< 0)

490 {

491 dbus_set_error (error, \_dbus_error_from_errno (errno),

492 "Failed to restore old fd limit: %s",

493 \_dbus_strerror (errno));

494 return FALSE;

495 }

496

497 return TRUE;

498}

499

500\#else /\* !HAVE_SETRLIMIT \*/

501

502static void

503fd_limit_not_supported (DBusError \*error)

504{

505 dbus_set_error (error, DBUS_ERROR_NOT_SUPPORTED,

506 "cannot change fd limit on this platform");

507}

508

509DBusRLimit \*

510\_dbus_rlimit_save_fd_limit (DBusError \*error)

511{

512 fd_limit_not_supported (error);

513 return NULL;

514}

515

516dbus_bool_t

517\_dbus_rlimit_raise_fd_limit (DBusError \*error)

518{

519 fd_limit_not_supported (error);

520 return FALSE;

521}

522

523dbus_bool_t

524\_dbus_rlimit_restore_fd_limit (DBusRLimit \*saved,

525 DBusError \*error)

526{

527 fd_limit_not_supported (error);

528 return FALSE;

529}

530

531\#endif

532

533void

534\_dbus_rlimit_free (DBusRLimit \*lim)

535{

536 dbus_free (lim);

537}

538

544void

545\_dbus_set_signal_handler (int sig,

546 DBusSignalHandler handler)

547{

548 struct sigaction act;

549 sigset_t empty_mask;

550

551 sigemptyset (&empty_mask);

552 act.sa_handler = handler;

553 act.sa_mask = empty_mask;

554 act.sa_flags = 0;

555 sigaction (sig, &act, NULL);

556}

557

563dbus_bool_t

564\_dbus_file_exists (const char \*file)

565{

566 return (access (file, F_OK) == 0);

567}

568

575dbus_bool_t

576\_dbus_path_is_absolute (const DBusString \*filename)

577{

578 if (\_dbus_string_get_length (filename) \> 0)

579 return \_dbus_string_get_byte (filename, 0) == '/';

580 else

581 return FALSE;

582}

583

592dbus_bool_t

593\_dbus_stat (const DBusString \*filename,

594 DBusStat \*statbuf,

595 DBusError \*error)

596{

597 const char \*filename_c;

598 struct stat sb;

599

600 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

601

602 filename_c = \_dbus_string_get_const_data (filename);

603

604 if (stat (filename_c, &sb) \< 0)

605 {

606 dbus_set_error (error, \_dbus_error_from_errno (errno),

607 "%s", \_dbus_strerror (errno));

608 return FALSE;

609 }

610

611 statbuf-\>mode = sb.st_mode;

612 statbuf-\>nlink = sb.st_nlink;

613 statbuf-\>uid = sb.st_uid;

614 statbuf-\>gid = sb.st_gid;

615 statbuf-\>size = sb.st_size;

616 statbuf-\>atime = sb.st_atime;

617 statbuf-\>mtime = sb.st_mtime;

618 statbuf-\>ctime = sb.st_ctime;

619

620 return TRUE;

621}

622

623

627struct DBusDirIter

628{

629 DIR \*d;

631};

632

640DBusDirIter\*

641\_dbus_directory_open (const DBusString \*filename,

642 DBusError \*error)

643{

644 DIR \*d;

645 DBusDirIter \*iter;

646 const char \*filename_c;

647

648 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

649

650 filename_c = \_dbus_string_get_const_data (filename);

651

652 d = opendir (filename_c);

653 if (d == NULL)

654 {

655 dbus_set_error (error, \_dbus_error_from_errno (errno),

656 "Failed to read directory \\%s\\: %s",

657 filename_c,

658 \_dbus_strerror (errno));

659 return NULL;

660 }

661 iter = dbus_new0 (DBusDirIter, 1);

662 if (iter == NULL)

663 {

664 closedir (d);

665 dbus_set_error (error, DBUS_ERROR_NO_MEMORY,

666 "Could not allocate memory for directory iterator");

667 return NULL;

668 }

669

670 iter-\>d = d;

671

672 return iter;

673}

674

688dbus_bool_t

689\_dbus_directory_get_next_file (DBusDirIter \*iter,

690 DBusString \*filename,

691 DBusError \*error)

692{

693 struct dirent \*ent;

694 int err;

695

696 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

697

698 again:

699 errno = 0;

700 ent = readdir (iter-\>d);

701

702 if (!ent)

703 {

704 err = errno;

705

706 if (err != 0)

707 dbus_set_error (error,

708 \_dbus_error_from_errno (err),

709 "%s", \_dbus_strerror (err));

710

711 return FALSE;

712 }

713 else if (ent-\>d_name\[0\] == '.' &&

714 (ent-\>d_name\[1\] == '\0' \|\|

715 (ent-\>d_name\[1\] == '.' && ent-\>d_name\[2\] == '\0')))

716 goto again;

717 else

718 {

719 \_dbus_string_set_length (filename, 0);

720 if (!\_dbus_string_append (filename, ent-\>d_name))

721 {

722 dbus_set_error (error, DBUS_ERROR_NO_MEMORY,

723 "No memory to read directory entry");

724 return FALSE;

725 }

726 else

727 {

728 return TRUE;

729 }

730 }

731}

732

736void

737\_dbus_directory_close (DBusDirIter \*iter)

738{

739 closedir (iter-\>d);

740 dbus_free (iter);

741}

742

743static dbus_bool_t

744fill_user_info_from_group (struct group \*g,

745 DBusGroupInfo \*info,

746 DBusError \*error)

747{

748 \_dbus_assert (g-\>gr_name != NULL);

749

750 info-\>gid = g-\>gr_gid;

751 info-\>groupname = \_dbus_strdup (g-\>gr_name);

752

753 /\* info-\>members = dbus_strdupv (g-\>gr_mem) \*/

754

755 if (info-\>groupname == NULL)

756 {

757 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

758 return FALSE;

759 }

760

761 return TRUE;

762}

763

764static dbus_bool_t

765fill_group_info (DBusGroupInfo \*info,

766 dbus_gid_t gid,

767 const DBusString \*groupname,

768 DBusError \*error)

769{

770 const char \*group_c_str;

771

772 \_dbus_assert (groupname != NULL \|\| gid != DBUS_GID_UNSET);

773 \_dbus_assert (groupname == NULL \|\| gid == DBUS_GID_UNSET);

774

775 if (groupname)

776 group_c_str = \_dbus_string_get_const_data (groupname);

777 else

778 group_c_str = NULL;

779

780 /\* For now assuming that the getgrnam() and getgrgid() flavors

781 \* always correspond to the pwnam flavors, if not we have

782 \* to add more configure checks.

783 \*/

784

785\#ifdef HAVE_GETPWNAM_R

786 {

787 struct group \*g;

788 int result;

789 size_t buflen;

790 char \*buf;

791 struct group g_str;

792 dbus_bool_t b;

793

794 /\* retrieve maximum needed size for buf \*/

795 buflen = sysconf (\_SC_GETGR_R_SIZE_MAX);

796

797 /\* sysconf actually returns a long, but everything else expects size_t,

798 \* so just recast here.

799 \* https://bugs.freedesktop.org/show_bug.cgi?id=17061

800 \*/

801 if ((long) buflen \<= 0)

802 buflen = 1024;

803

804 result = -1;

805 while (1)

806 {

807 buf = dbus_malloc (buflen);

808 if (buf == NULL)

809 {

810 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

811 return FALSE;

812 }

813

814 g = NULL;

815 if (group_c_str)

816 result = getgrnam_r (group_c_str, &g_str, buf, buflen,

817 &g);

818 else

819 result = getgrgid_r (gid, &g_str, buf, buflen,

820 &g);

821 /\* Try a bigger buffer if ERANGE was returned:

822 https://bugs.freedesktop.org/show_bug.cgi?id=16727

823 \*/

824 if (result == ERANGE && buflen \< 512 \* 1024)

825 {

826 dbus_free (buf);

827 buflen \*= 2;

828 }

829 else

830 {

831 break;

832 }

833 }

834

835 if (result == 0 && g == &g_str)

836 {

837 b = fill_user_info_from_group (g, info, error);

838 dbus_free (buf);

839 return b;

840 }

841 else

842 {

843 dbus_set_error (error, \_dbus_error_from_errno (errno),

844 "Group %s unknown or failed to look it up\n",

845 group_c_str ? group_c_str : "???");

846 dbus_free (buf);

847 return FALSE;

848 }

849 }

850\#else /\* ! HAVE_GETPWNAM_R \*/

851 {

852 /\* I guess we're screwed on thread safety here \*/

853 struct group \*g;

854

855\#warning getpwnam_r() not available, please report this to the dbus maintainers with details of your OS

856

857 g = getgrnam (group_c_str);

858

859 if (g != NULL)

860 {

861 return fill_user_info_from_group (g, info, error);

862 }

863 else

864 {

865 dbus_set_error (error, \_dbus_error_from_errno (errno),

866 "Group %s unknown or failed to look it up\n",

867 group_c_str ? group_c_str : "???");

868 return FALSE;

869 }

870 }

871\#endif /\* ! HAVE_GETPWNAM_R \*/

872}

873

883dbus_bool_t

884\_dbus_group_info_fill (DBusGroupInfo \*info,

885 const DBusString \*groupname,

886 DBusError \*error)

887{

888 return fill_group_info (info, DBUS_GID_UNSET,

889 groupname, error);

890

891}

892

902dbus_bool_t

903\_dbus_group_info_fill_gid (DBusGroupInfo \*info,

904 dbus_gid_t gid,

905 DBusError \*error)

906{

907 return fill_group_info (info, gid, NULL, error);

908}

909

918dbus_bool_t

919\_dbus_parse_unix_user_from_config (const DBusString \*username,

920 dbus_uid_t \*uid_p)

921{

922 return \_dbus_get_user_id (username, uid_p);

923

924}

925

934dbus_bool_t

935\_dbus_parse_unix_group_from_config (const DBusString \*groupname,

936 dbus_gid_t \*gid_p)

937{

938 return \_dbus_get_group_id (groupname, gid_p);

939}

940

952dbus_bool_t

953\_dbus_unix_groups_from_uid (dbus_uid_t uid,

954 dbus_gid_t \*\*group_ids,

955 int \*n_group_ids,

956 DBusError \*error)

957{

958 return \_dbus_groups_from_uid (uid, group_ids, n_group_ids, error);

959}

960

970dbus_bool_t

971\_dbus_unix_user_is_at_console (dbus_uid_t uid,

972 DBusError \*error)

973{

974 return \_dbus_is_console_user (uid, error);

975

976}

977

985dbus_bool_t

986\_dbus_unix_user_is_process_owner (dbus_uid_t uid)

987{

988 return uid == \_dbus_geteuid ();

989}

990

998dbus_bool_t

999\_dbus_windows_user_is_process_owner (const char \*windows_sid)

1000{

1001 return FALSE;

1002}

1003

/\* End of DBusInternalsUtils functions \*/

1005

1017dbus_bool_t

1018\_dbus_string_get_dirname (const DBusString \*filename,

1019 DBusString \*dirname)

1020{

1021 int sep;

1022

1023 \_dbus_assert (filename != dirname);

1024 \_dbus_assert (filename != NULL);

1025 \_dbus_assert (dirname != NULL);

1026

1027 /\* Ignore any separators on the end \*/

1028 sep = \_dbus_string_get_length (filename);

1029 if (sep == 0)

1030 return \_dbus_string_append (dirname, "."); /\* empty string passed in \*/

1031

1032 while (sep \> 0 && \_dbus_string_get_byte (filename, sep - 1) == '/')

1033 --sep;

1034

1035 \_dbus_assert (sep \>= 0);

1036

1037 if (sep == 0)

1038 return \_dbus_string_append (dirname, "/");

1039

1040 /\* Now find the previous separator \*/

1041 \_dbus_string_find_byte_backward (filename, sep, '/', &sep);

1042 if (sep \< 0)

1043 return \_dbus_string_append (dirname, ".");

1044

1045 /\* skip multiple separators \*/

1046 while (sep \> 0 && \_dbus_string_get_byte (filename, sep - 1) == '/')

1047 --sep;

1048

1049 \_dbus_assert (sep \>= 0);

1050

1051 if (sep == 0 &&

1052 \_dbus_string_get_byte (filename, 0) == '/')

1053 return \_dbus_string_append (dirname, "/");

1054 else

1055 return \_dbus_string_copy_len (filename, 0, sep - 0,

1056 dirname, \_dbus_string_get_length (dirname));

1057}

/\* DBusString stuff \*/

1059

1060static void

1061string_squash_nonprintable (DBusString \*str)

1062{

1063 unsigned char \*buf;

1064 int i, len;

1065

1066 buf = \_dbus_string_get_udata (str);

1067 len = \_dbus_string_get_length (str);

1068

1069 /\* /proc/\$pid/cmdline is a sequence of \0-terminated words, but we

1070 \* want a sequence of space-separated words, with no extra trailing

1071 \* space:

1072 \* "/bin/sleep" "\0" "60" "\0"

1073 \* -\> "/bin/sleep" "\0" "60"

1074 \* -\> "/bin/sleep" " " "60"

1075 \*

1076 \* so chop off the trailing NUL before cleaning up unprintable

1077 \* characters. \*/

1078 if (len \> 0 && buf\[len - 1\] == '\0')

1079 {

1080 \_dbus_string_shorten (str, 1);

1081 len--;

1082 }

1083

1084 for (i = 0; i \< len; i++)

1085 {

1086 unsigned char c = (unsigned char) buf\[i\];

1087 if (c == '\0')

1088 buf\[i\] = ' ';

1089 else if (c \< 0x20 \|\| c \> 127)

1090 buf\[i\] = '?';

1091 }

1092}

1093

1108dbus_bool_t

1109\_dbus_command_for_pid (unsigned long pid,

1110 DBusString \*str,

1111 int max_len,

1112 DBusError \*error)

1113{

1114 /\* This is all Linux-specific for now \*/

1115 DBusString path;

1116 DBusString cmdline;

1117 int fd;

1118

1119 if (!\_dbus_string_init (&path))

1120 {

1121 \_DBUS_SET_OOM (error);

1122 return FALSE;

1123 }

1124

1125 if (!\_dbus_string_init (&cmdline))

1126 {

1127 \_DBUS_SET_OOM (error);

1128 \_dbus_string_free (&path);

1129 return FALSE;

1130 }

1131

1132 if (!\_dbus_string_append_printf (&path, "/proc/%ld/cmdline", pid))

1133 goto oom;

1134

1135 fd = open (\_dbus_string_get_const_data (&path), O_RDONLY);

1136 if (fd \< 0)

1137 {

1138 dbus_set_error (error,

1139 \_dbus_error_from_errno (errno),

1140 "Failed to open \\%s\\: %s",

1141 \_dbus_string_get_const_data (&path),

1142 \_dbus_strerror (errno));

1143 goto fail;

1144 }

1145

1146 if (!\_dbus_read (fd, &cmdline, max_len))

1147 {

1148 dbus_set_error (error,

1149 \_dbus_error_from_errno (errno),

1150 "Failed to read from \\%s\\: %s",

1151 \_dbus_string_get_const_data (&path),

1152 \_dbus_strerror (errno));

1153 \_dbus_close (fd, NULL);

1154 goto fail;

1155 }

1156

1157 if (!\_dbus_close (fd, error))

1158 goto fail;

1159

1160 string_squash_nonprintable (&cmdline);

1161

1162 if (!\_dbus_string_copy (&cmdline, 0, str, \_dbus_string_get_length (str)))

1163 goto oom;

1164

1165 \_dbus_string_free (&cmdline);

1166 \_dbus_string_free (&path);

1167 return TRUE;

1168oom:

1169 \_DBUS_SET_OOM (error);

1170fail:

1171 \_dbus_string_free (&cmdline);

1172 \_dbus_string_free (&path);

1173 return FALSE;

1174}

1175

1184dbus_bool_t

1185\_dbus_replace_install_prefix (DBusString \*path)

1186{

1187 return TRUE;

1188}

1189

1190static dbus_bool_t

1191ensure_owned_directory (const char \*label,

1192 const DBusString \*string,

1193 dbus_bool_t create,

1194 DBusError \*error)

1195{

1196 const char \*dir = \_dbus_string_get_const_data (string);

1197 struct stat buf;

1198

1199 if (create && !\_dbus_ensure_directory (string, error))

1200 return FALSE;

1201

1202 /\*

1203 \* The stat()-based checks in this function are to protect against

1204 \* mistakes, not malice. We are working in a directory that is meant

1205 \* to be trusted; but if a user has used \`su\` or similar to escalate

1206 \* their privileges without correctly clearing the environment, the

1207 \* XDG_RUNTIME_DIR in the environment might still be the user's

1208 \* and not root's. We don't want to write root-owned files into that

1209 \* directory, so just warn and don't provide support for transient

1210 \* services in that case.

1211 \*

1212 \* In particular, we use stat() and not lstat() so that if we later

1213 \* decide to use a different directory name for transient services,

1214 \* we can drop in a compatibility symlink without breaking older

1215 \* libdbus.

1216 \*/

1217

1218 if (stat (dir, &buf) != 0)

1219 {

1220 int saved_errno = errno;

1221

1222 dbus_set_error (error, \_dbus_error_from_errno (saved_errno),

1223 "%s \\%s\\ not available: %s", label, dir,

1224 \_dbus_strerror (saved_errno));

1225 return FALSE;

1226 }

1227

1228 if (!S_ISDIR (buf.st_mode))

1229 {

1230 dbus_set_error (error, DBUS_ERROR_FAILED, "%s \\%s\\ is not a directory",

1231 label, dir);

1232 return FALSE;

1233 }

1234

1235 if (buf.st_uid != geteuid ())

1236 {

1237 dbus_set_error (error, DBUS_ERROR_FAILED,

1238 "%s \\%s\\ is owned by uid %ld, not our uid %ld",

1239 label, dir, (long) buf.st_uid, (long) geteuid ());

1240 return FALSE;

1241 }

1242

1243 /\* This is just because we have the stat() results already, so we might

1244 \* as well check opportunistically. \*/

1245 if ((S_IWOTH \| S_IWGRP) & buf.st_mode)

1246 {

1247 dbus_set_error (error, DBUS_ERROR_FAILED,

1248 "%s \\%s\\ can be written by others (mode 0%o)",

1249 label, dir, buf.st_mode);

1250 return FALSE;

1251 }

1252

1253 return TRUE;

1254}

1255

1256\#define DBUS_UNIX_STANDARD_SESSION_SERVICEDIR "/dbus-1/services"

1257\#define DBUS_UNIX_STANDARD_SYSTEM_SERVICEDIR "/dbus-1/system-services"

1258

1266dbus_bool_t

1267\_dbus_set_up_transient_session_servicedirs (DBusList \*\*dirs,

1268 DBusError \*error)

1269{

1270 const char \*xdg_runtime_dir;

1271 DBusString services;

1272 DBusString dbus1;

1273 DBusString xrd;

1274 dbus_bool_t ret = FALSE;

1275 char \*data = NULL;

1276

1277 if (!\_dbus_string_init (&dbus1))

1278 {

1279 \_DBUS_SET_OOM (error);

1280 return FALSE;

1281 }

1282

1283 if (!\_dbus_string_init (&services))

1284 {

1285 \_dbus_string_free (&dbus1);

1286 \_DBUS_SET_OOM (error);

1287 return FALSE;

1288 }

1289

1290 if (!\_dbus_string_init (&xrd))

1291 {

1292 \_dbus_string_free (&dbus1);

1293 \_dbus_string_free (&services);

1294 \_DBUS_SET_OOM (error);

1295 return FALSE;

1296 }

1297

1298 xdg_runtime_dir = \_dbus_getenv ("XDG_RUNTIME_DIR");

1299

1300 /\* Not an error, we just can't have transient session services \*/

1301 if (xdg_runtime_dir == NULL)

1302 {

1303 \_dbus_verbose ("XDG_RUNTIME_DIR is unset: transient session services "

1304 "not available here\n");

1305 ret = TRUE;

1306 goto out;

1307 }

1308

1309 if (!\_dbus_string_append (&xrd, xdg_runtime_dir) \|\|

1310 !\_dbus_string_append_printf (&dbus1, "%s/dbus-1",

1311 xdg_runtime_dir) \|\|

1312 !\_dbus_string_append_printf (&services, "%s/dbus-1/services",

1313 xdg_runtime_dir))

1314 {

1315 \_DBUS_SET_OOM (error);

1316 goto out;

1317 }

1318

1319 if (!ensure_owned_directory ("XDG_RUNTIME_DIR", &xrd, FALSE, error) \|\|

1320 !ensure_owned_directory ("XDG_RUNTIME_DIR subdirectory", &dbus1, TRUE,

1321 error) \|\|

1322 !ensure_owned_directory ("XDG_RUNTIME_DIR subdirectory", &services,

1323 TRUE, error))

1324 goto out;

1325

1326 if (!\_dbus_string_steal_data (&services, &data) \|\|

1327 !\_dbus_list_append (dirs, data))

1328 {

1329 \_DBUS_SET_OOM (error);

1330 goto out;

1331 }

1332

1333 \_dbus_verbose ("Transient service directory is %s\n", data);

1334 /\* Ownership was transferred to @dirs \*/

1335 data = NULL;

1336 ret = TRUE;

1337

1338out:

1339 \_dbus_string_free (&dbus1);

1340 \_dbus_string_free (&services);

1341 \_dbus_string_free (&xrd);

1342 dbus_free (data);

1343 return ret;

1344}

1345

1363dbus_bool_t

1364\_dbus_get_standard_session_servicedirs (DBusList \*\*dirs)

1365{

1366 const char \*xdg_data_home;

1367 const char \*xdg_data_dirs;

1368 DBusString servicedir_path;

1369

1370 if (!\_dbus_string_init (&servicedir_path))

1371 return FALSE;

1372

1373 xdg_data_home = \_dbus_getenv ("XDG_DATA_HOME");

1374 xdg_data_dirs = \_dbus_getenv ("XDG_DATA_DIRS");

1375

1376 if (xdg_data_home != NULL)

1377 {

1378 if (!\_dbus_string_append (&servicedir_path, xdg_data_home))

1379 goto oom;

1380 }

1381 else

1382 {

1383 const DBusString \*homedir;

1384 DBusString local_share;

1385

1386 if (!\_dbus_homedir_from_current_process (&homedir))

1387 goto oom;

1388

1389 if (!\_dbus_string_append (&servicedir_path, \_dbus_string_get_const_data (homedir)))

1390 goto oom;

1391

1392 \_dbus_string_init_const (&local_share, "/.local/share");

1393 if (!\_dbus_concat_dir_and_file (&servicedir_path, &local_share))

1394 goto oom;

1395 }

1396

1397 if (!\_dbus_string_append (&servicedir_path, ":"))

1398 goto oom;

1399

1400 if (xdg_data_dirs != NULL)

1401 {

1402 if (!\_dbus_string_append (&servicedir_path, xdg_data_dirs))

1403 goto oom;

1404

1405 if (!\_dbus_string_append (&servicedir_path, ":"))

1406 goto oom;

1407 }

1408 else

1409 {

1410 if (!\_dbus_string_append (&servicedir_path, "/usr/local/share:/usr/share:"))

1411 goto oom;

1412 }

1413

1414 /\*

1415 \* add configured datadir to defaults

1416 \* this may be the same as an xdg dir

1417 \* however the config parser should take

1418 \* care of duplicates

1419 \*/

1420 if (!\_dbus_string_append (&servicedir_path, DBUS_DATADIR))

1421 goto oom;

1422

1423 if (!\_dbus_split_paths_and_append (&servicedir_path,

1424 DBUS_UNIX_STANDARD_SESSION_SERVICEDIR,

1425 dirs))

1426 goto oom;

1427

1428 \_dbus_string_free (&servicedir_path);

1429 return TRUE;

1430

1431 oom:

1432 \_dbus_string_free (&servicedir_path);

1433 return FALSE;

1434}

1435

1436

1455dbus_bool_t

1456\_dbus_get_standard_system_servicedirs (DBusList \*\*dirs)

1457{

1458 /\*

1459 \* DBUS_DATADIR may be the same as one of the standard directories. However,

1460 \* the config parser should take care of the duplicates.

1461 \*

1462 \* Also, append /lib as counterpart of /usr/share on the root

1463 \* directory (the root directory does not know /share), in order to

1464 \* facilitate early boot system bus activation where /usr might not

1465 \* be available.

1466 \*/

1467 static const char standard_search_path\[\] =

1468 "/usr/local/share:"

1469 "/usr/share:"

1470 DBUS_DATADIR ":"

1471 "/lib";

1472 DBusString servicedir_path;

1473

1474 \_dbus_string_init_const (&servicedir_path, standard_search_path);

1475

1476 return \_dbus_split_paths_and_append (&servicedir_path,

1477 DBUS_UNIX_STANDARD_SYSTEM_SERVICEDIR,

1478 dirs);

1479}

1480

1481

1494dbus_bool_t

1495\_dbus_get_local_system_servicedirs (DBusList \*\*dirs)

1496{

1497 static const char standard_search_path\[\] =

1498 "/etc:"

1499 "/run";

1500 DBusString servicedir_path;

1501

1502 \_dbus_string_init_const (&servicedir_path, standard_search_path);

1503

1504 return \_dbus_split_paths_and_append (&servicedir_path,

1505 DBUS_UNIX_STANDARD_SYSTEM_SERVICEDIR,

1506 dirs);

1507}

1508

1517dbus_bool_t

1518\_dbus_get_system_config_file (DBusString \*str)

1519{

1520 \_dbus_assert (\_dbus_string_get_length (str) == 0);

1521

1522 return \_dbus_string_append (str, DBUS_SYSTEM_CONFIG_FILE);

1523}

1524

1531dbus_bool_t

1532\_dbus_get_session_config_file (DBusString \*str)

1533{

1534 \_dbus_assert (\_dbus_string_get_length (str) == 0);

1535

1536 return \_dbus_string_append (str, DBUS_SESSION_CONFIG_FILE);

1537}

1538

1543void

1544\_dbus_daemon_report_ready (void)

1545{

1546\#ifdef HAVE_SYSTEMD

1547 sd_notify (0, "READY=1");

1548\#endif

1549}

1550

1555void

1556\_dbus_daemon_report_reloading (void)

1557{

1558\#ifdef HAVE_SYSTEMD

1559 sd_notify (0, "RELOADING=1");

1560\#endif

1561}

1562

1567void

1568\_dbus_daemon_report_reloaded (void)

1569{

1570\#ifdef HAVE_SYSTEMD

1571 /\* For systemd, this is the same code \*/

1572 \_dbus_daemon_report_ready ();

1573\#endif

1574}

1575

1580void

1581\_dbus_daemon_report_stopping (void)

1582{

1583\#ifdef HAVE_SYSTEMD

1584 sd_notify (0, "STOPPING=1");

1585\#endif

1586}

1587

1601dbus_bool_t

1602\_dbus_reset_oom_score_adj (const char \*\*error_str_p)

1603{

1604\#ifdef \_\_linux\_\_

1605 int fd = -1;

1606 dbus_bool_t ret = FALSE;

1607 int saved_errno = 0;

1608 const char \*error_str = NULL;

1609

1610\#ifdef O_CLOEXEC

1611 fd = open ("/proc/self/oom_score_adj", O_RDONLY \| O_CLOEXEC);

1612\#endif

1613

1614 if (fd \< 0)

1615 {

1616 fd = open ("/proc/self/oom_score_adj", O_RDONLY);

1617 if (fd \>= 0)

1618 \_dbus_fd_set_close_on_exec (fd);

1619 }

1620

1621 if (fd \>= 0)

1622 {

1623 ssize_t read_result = -1;

1624 /\* It doesn't actually matter whether we read the whole file,

1625 \* as long as we get the presence or absence of the minus sign \*/

1626 char first_char = '\0';

1627

1628 read_result = read (fd, &first_char, 1);

1629

1630 if (read_result \< 0)

1631 {

1632 /\* This probably can't actually happen in practice: if we can

1633 \* open it, then we can hopefully read from it \*/

1634 ret = FALSE;

1635 error_str = "failed to read from /proc/self/oom_score_adj";

1636 saved_errno = errno;

1637 goto out;

1638 }

1639

1640 /\* If we are running with protection from the OOM killer

1641 \* (typical for the system dbus-daemon under systemd), then

1642 \* oom_score_adj will be negative. Drop that protection,

1643 \* returning to oom_score_adj = 0.

1644 \*

1645 \* Conversely, if we are running with increased susceptibility

1646 \* to the OOM killer (as user sessions typically do in

1647 \* systemd \>= 250), oom_score_adj will be strictly positive,

1648 \* and we are not allowed to decrease it to 0 without privileges.

1649 \*

1650 \* If it's exactly 0 (typical for non-systemd systems, and

1651 \* user processes on older systemd) then there's no need to

1652 \* alter it.

1653 \*

1654 \* We shouldn't get an empty result, but if we do, assume it

1655 \* means zero and don't try to change it. \*/

1656 if (read_result == 0 \|\| first_char != '-')

1657 {

1658 /\* Nothing needs to be done: the OOM score adjustment is

1659 \* non-negative \*/

1660 ret = TRUE;

1661 goto out;

1662 }

1663

1664 close (fd);

1665\#ifdef O_CLOEXEC

1666 fd = open ("/proc/self/oom_score_adj", O_WRONLY \| O_CLOEXEC);

1667

1668 if (fd \< 0)

1669\#endif

1670 {

1671 fd = open ("/proc/self/oom_score_adj", O_WRONLY);

1672 if (fd \>= 0)

1673 \_dbus_fd_set_close_on_exec (fd);

1674 }

1675

1676 if (fd \< 0)

1677 {

1678 ret = FALSE;

1679 error_str = "open(/proc/self/oom_score_adj) for writing";

1680 saved_errno = errno;

1681 goto out;

1682 }

1683

1684 if (pwrite (fd, "0", sizeof (char), 0) \< 0)

1685 {

1686 ret = FALSE;

1687 error_str = "writing oom_score_adj error";

1688 saved_errno = errno;

1689 goto out;

1690 }

1691

1692 /\* Success \*/

1693 ret = TRUE;

1694 }

1695 else if (errno == ENOENT)

1696 {

1697 /\* If /proc/self/oom_score_adj doesn't exist, assume the kernel

1698 \* doesn't support this feature and ignore it. \*/

1699 ret = TRUE;

1700 }

1701 else

1702 {

1703 ret = FALSE;

1704 error_str = "open(/proc/self/oom_score_adj) for reading";

1705 saved_errno = errno;

1706 goto out;

1707 }

1708

1709out:

1710 if (fd \>= 0)

1711 \_dbus_close (fd, NULL);

1712

1713 if (error_str_p != NULL)

1714 \*error_str_p = error_str;

1715

1716 errno = saved_errno;

1717 return ret;

1718\#else

1719 /\* nothing to do on this platform \*/

1720 return TRUE;

1721\#endif

1722}

dbus_set_error

void dbus_set_error(DBusError \*error, const char \*name, const char \*format,...)

Assigns an error name and message to a DBusError.

**Definition** dbus-errors.c:356

dbus_error_is_set

dbus_bool_t dbus_error_is_set(const DBusError \*error)

Checks whether an error occurred (the error is set).

**Definition** dbus-errors.c:331

\_dbus_stat

dbus_bool_t \_dbus_stat(const DBusString \*filename, DBusStat \*statbuf, DBusError \*error)

stat() wrapper.

**Definition** dbus-sysdeps-util-unix.c:593

\_dbus_assert_not_reached

\#define \_dbus_assert_not_reached(explanation)

Aborts with an error message if called.

**Definition** dbus-internals.h:164

\_dbus_write_pid_to_file_and_pipe

dbus_bool_t \_dbus_write_pid_to_file_and_pipe(const DBusString \*pidfile, DBusPipe \*print_pid_pipe, dbus_pid_t pid_to_write, DBusError \*error)

Writes the given pid_to_write to a pidfile (if non-NULL) and/or to a pipe (if non-NULL).

**Definition** dbus-sysdeps-util-unix.c:240

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_dbus_file_exists

dbus_bool_t \_dbus_file_exists(const char \*file)

Checks if a file exists.

**Definition** dbus-sysdeps-util-unix.c:564

\_dbus_homedir_from_current_process

dbus_bool_t \_dbus_homedir_from_current_process(const DBusString \*\*homedir)

Gets homedir of user owning current process.

**Definition** dbus-userdb.c:442

\_dbus_directory_close

void \_dbus_directory_close(DBusDirIter \*iter)

Closes a directory iteration.

**Definition** dbus-sysdeps-util-unix.c:737

\_dbus_group_info_fill

dbus_bool_t \_dbus_group_info_fill(DBusGroupInfo \*info, const DBusString \*groupname, DBusError \*error)

Initializes the given DBusGroupInfo struct with information about the given group name.

**Definition** dbus-sysdeps-util-unix.c:884

\_dbus_directory_open

DBusDirIter \* \_dbus_directory_open(const DBusString \*filename, DBusError \*error)

Open a directory to iterate over.

**Definition** dbus-sysdeps-util-unix.c:641

\_dbus_parse_unix_user_from_config

dbus_bool_t \_dbus_parse_unix_user_from_config(const DBusString \*username, dbus_uid_t \*uid_p)

Parse a UNIX user from the bus config file.

**Definition** dbus-sysdeps-util-unix.c:919

\_dbus_verify_daemon_user

dbus_bool_t \_dbus_verify_daemon_user(const char \*user)

Verify that after the fork we can successfully change to this user.

**Definition** dbus-sysdeps-util-unix.c:313

\_dbus_error_from_errno

const char \* \_dbus_error_from_errno(int error_number)

Converts a UNIX errno, or Windows errno or WinSock error value into a DBusError name.

**Definition** dbus-sysdeps.c:565

\_dbus_set_signal_handler

void \_dbus_set_signal_handler(int sig, DBusSignalHandler handler)

Installs a UNIX signal handler.

**Definition** dbus-sysdeps-util-unix.c:545

\_dbus_path_is_absolute

dbus_bool_t \_dbus_path_is_absolute(const DBusString \*filename)

Checks whether the filename is an absolute path.

**Definition** dbus-sysdeps-util-unix.c:576

\_dbus_strdup

char \* \_dbus_strdup(const char \*str)

Duplicates a string.

**Definition** dbus-internals.c:621

\_dbus_change_to_daemon_user

dbus_bool_t \_dbus_change_to_daemon_user(const char \*user, DBusError \*error)

Changes the user and group the bus is running as.

**Definition** dbus-sysdeps-util-unix.c:333

\_dbus_unix_user_is_process_owner

dbus_bool_t \_dbus_unix_user_is_process_owner(dbus_uid_t uid)

Checks to see if the UNIX user ID matches the UID of the process.

**Definition** dbus-sysdeps-util-unix.c:986

\_dbus_get_group_id

dbus_bool_t \_dbus_get_group_id(const DBusString \*groupname, dbus_gid_t \*gid)

Gets group ID given groupname.

**Definition** dbus-userdb-util.c:145

\_dbus_windows_user_is_process_owner

dbus_bool_t \_dbus_windows_user_is_process_owner(const char \*windows_sid)

Checks to see if the Windows user SID matches the owner of the process.

**Definition** dbus-sysdeps-util-unix.c:999

\_dbus_parse_unix_group_from_config

dbus_bool_t \_dbus_parse_unix_group_from_config(const DBusString \*groupname, dbus_gid_t \*gid_p)

Parse a UNIX group from the bus config file.

**Definition** dbus-sysdeps-util-unix.c:935

\_dbus_unix_groups_from_uid

dbus_bool_t \_dbus_unix_groups_from_uid(dbus_uid_t uid, dbus_gid_t \*\*group_ids, int \*n_group_ids, DBusError \*error)

Gets all groups corresponding to the given UNIX user ID.

**Definition** dbus-sysdeps-util-unix.c:953

\_dbus_is_console_user

dbus_bool_t \_dbus_is_console_user(dbus_uid_t uid, DBusError \*error)

Checks to see if the UID sent in is the console user.

**Definition** dbus-userdb-util.c:67

\_dbus_groups_from_uid

dbus_bool_t \_dbus_groups_from_uid(dbus_uid_t uid, dbus_gid_t \*\*group_ids, int \*n_group_ids, DBusError \*error)

Gets all groups corresponding to the given UID.

**Definition** dbus-userdb-util.c:349

\_dbus_directory_get_next_file

dbus_bool_t \_dbus_directory_get_next_file(DBusDirIter \*iter, DBusString \*filename, DBusError \*error)

Get next file in the directory.

**Definition** dbus-sysdeps-util-unix.c:689

\_dbus_warn

void \_dbus_warn(const char \*format,...)

Prints a warning message to stderr.

**Definition** dbus-internals.c:278

\_dbus_get_user_id_and_primary_group

dbus_bool_t \_dbus_get_user_id_and_primary_group(const DBusString \*username, dbus_uid_t \*uid_p, dbus_gid_t \*gid_p)

Gets user ID and primary group given username.

**Definition** dbus-userdb-util.c:186

\_dbus_become_daemon

dbus_bool_t \_dbus_become_daemon(const DBusString \*pidfile, DBusPipe \*print_pid_pipe, DBusError \*error, dbus_bool_t keep_umask)

Does the chdir, fork, setsid, etc.

**Definition** dbus-sysdeps-util-unix.c:86

\_dbus_group_info_fill_gid

dbus_bool_t \_dbus_group_info_fill_gid(DBusGroupInfo \*info, dbus_gid_t gid, DBusError \*error)

Initializes the given DBusGroupInfo struct with information about the given group ID.

**Definition** dbus-sysdeps-util-unix.c:903

\_dbus_unix_user_is_at_console

dbus_bool_t \_dbus_unix_user_is_at_console(dbus_uid_t uid, DBusError \*error)

Checks to see if the UNIX user ID is at the console.

**Definition** dbus-sysdeps-util-unix.c:971

\_dbus_get_user_id

dbus_bool_t \_dbus_get_user_id(const DBusString \*username, dbus_uid_t \*uid)

Gets user ID given username.

**Definition** dbus-userdb-util.c:131

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

dbus_new0

\#define dbus_new0(type, count)

Safe macro for using dbus_malloc0().

**Definition** dbus-memory.h:60

dbus_malloc

void \* dbus_malloc(size_t bytes)

Allocates the given number of bytes, as with standard malloc().

**Definition** dbus-memory.c:470

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

\_dbus_string_copy

dbus_bool_t \_dbus_string_copy(const DBusString \*source, int start, DBusString \*dest, int insert_at)

Like \_dbus_string_move(), but does not delete the section of the source string that's copied to the d...

**Definition** dbus-string.c:1345

\_dbus_string_steal_data

dbus_bool_t \_dbus_string_steal_data(DBusString \*str, char \*\*data_return)

Like \_dbus_string_get_data(), but removes the gotten data from the original string.

**Definition** dbus-string.c:686

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_string_shorten

void \_dbus_string_shorten(DBusString \*str, int length_to_remove)

Makes a string shorter by the given number of bytes.

**Definition** dbus-string.c:825

\_dbus_string_find_byte_backward

dbus_bool_t \_dbus_string_find_byte_backward(const DBusString \*str, int start, unsigned char byte, int \*found)

Find the given byte scanning backward from the given start.

**Definition** dbus-string-util.c:98

\_dbus_string_get_length

int \_dbus_string_get_length(const DBusString \*str)

Gets the length of a string (not including nul termination).

**Definition** dbus-string.c:784

\_dbus_string_append_printf

dbus_bool_t \_dbus_string_append_printf(DBusString \*str, const char \*format,...)

Appends a printf-style formatted string to the DBusString.

**Definition** dbus-string.c:1147

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

\_dbus_string_get_dirname

dbus_bool_t \_dbus_string_get_dirname(const DBusString \*filename, DBusString \*dirname)

Get the directory name from a complete filename.

**Definition** dbus-sysdeps-util-unix.c:1018

\_dbus_reset_oom_score_adj

dbus_bool_t \_dbus_reset_oom_score_adj(const char \*\*error_str_p)

If the current process has been protected from the Linux OOM killer (the oom_score_adj process parame...

**Definition** dbus-sysdeps-util-unix.c:1602

\_dbus_close

dbus_bool_t \_dbus_close(int fd, DBusError \*error)

Closes a file descriptor.

**Definition** dbus-sysdeps-unix.c:3727

DBusSignalHandler

void(\* DBusSignalHandler)(int sig)

A UNIX signal handler.

**Definition** dbus-sysdeps-unix.h:158

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

\_dbus_get_standard_session_servicedirs

dbus_bool_t \_dbus_get_standard_session_servicedirs(DBusList \*\*dirs)

Returns the standard directories for a session bus to look for service activation files.

**Definition** dbus-sysdeps-util-unix.c:1364

\_dbus_daemon_report_ready

void \_dbus_daemon_report_ready(void)

Report to a service manager that the daemon calling this function is ready for use.

**Definition** dbus-sysdeps-util-unix.c:1544

dbus_uid_t

unsigned long dbus_uid_t

A user ID.

**Definition** dbus-sysdeps.h:141

\_dbus_get_session_config_file

dbus_bool_t \_dbus_get_session_config_file(DBusString \*str)

Get the absolute path of the session.conf file.

**Definition** dbus-sysdeps-util-unix.c:1532

dbus_pid_t

unsigned long dbus_pid_t

A process ID.

**Definition** dbus-sysdeps.h:139

\_dbus_daemon_report_reloading

void \_dbus_daemon_report_reloading(void)

Report to a service manager that the daemon calling this function is reloading configuration.

**Definition** dbus-sysdeps-util-unix.c:1556

dbus_gid_t

unsigned long dbus_gid_t

A group ID.

**Definition** dbus-sysdeps.h:143

\_dbus_command_for_pid

dbus_bool_t \_dbus_command_for_pid(unsigned long pid, DBusString \*str, int max_len, DBusError \*error)

Get a printable string describing the command used to execute the process with pid.

**Definition** dbus-sysdeps-util-unix.c:1109

\_dbus_get_system_config_file

dbus_bool_t \_dbus_get_system_config_file(DBusString \*str)

Get the absolute path of the system.conf file (there is no system bus on Windows so this can just ret...

**Definition** dbus-sysdeps-util-unix.c:1518

\_dbus_set_up_transient_session_servicedirs

dbus_bool_t \_dbus_set_up_transient_session_servicedirs(DBusList \*\*dirs, DBusError \*error)

Returns the standard directories for a session bus to look for transient service activation files.

**Definition** dbus-sysdeps-util-unix.c:1267

\_dbus_getenv

const char \* \_dbus_getenv(const char \*varname)

Wrapper for getenv().

**Definition** dbus-sysdeps.c:197

\_dbus_get_standard_system_servicedirs

dbus_bool_t \_dbus_get_standard_system_servicedirs(DBusList \*\*dirs)

Returns the standard directories for a system bus to look for service activation files.

**Definition** dbus-sysdeps-util-unix.c:1456

\_dbus_get_local_system_servicedirs

dbus_bool_t \_dbus_get_local_system_servicedirs(DBusList \*\*dirs)

Returns the local admin directories for a system bus to look for service activation files.

**Definition** dbus-sysdeps-util-unix.c:1495

\_dbus_daemon_report_reloaded

void \_dbus_daemon_report_reloaded(void)

Report to a service manager that the daemon calling this function is reloading configuration.

**Definition** dbus-sysdeps-util-unix.c:1568

DBUS_GID_UNSET

\#define DBUS_GID_UNSET

an invalid GID used to represent an uninitialized dbus_gid_t field

**Definition** dbus-sysdeps.h:150

\_dbus_daemon_report_stopping

void \_dbus_daemon_report_stopping(void)

Report to a service manager that the daemon calling this function is shutting down.

**Definition** dbus-sysdeps-util-unix.c:1581

\_dbus_concat_dir_and_file

dbus_bool_t \_dbus_concat_dir_and_file(DBusString \*dir, const DBusString \*next_component)

Appends the given filename to the given directory.

**Definition** dbus-sysdeps-unix.c:3497

\_dbus_split_paths_and_append

dbus_bool_t \_dbus_split_paths_and_append(DBusString \*dirs, const char \*suffix, DBusList \*\*dir_list)

Split paths into a list of char strings.

**Definition** dbus-sysdeps.c:238

\_dbus_replace_install_prefix

dbus_bool_t \_dbus_replace_install_prefix(DBusString \*path)

Replace the DBUS_PREFIX in the given path, in-place, by the current D-Bus installation directory.

**Definition** dbus-sysdeps-util-unix.c:1185

DBUS_PID_FORMAT

\#define DBUS_PID_FORMAT

an appropriate printf format for dbus_pid_t

**Definition** dbus-sysdeps.h:153

\_dbus_ensure_directory

dbus_bool_t \_dbus_ensure_directory(const DBusString \*filename, DBusError \*error)

Creates a directory; succeeds if the directory is created or already existed.

**Definition** dbus-sysdeps-unix.c:3434

DBusDirIter

Internals of directory iterator.

**Definition** dbus-sysdeps-util-unix.c:628

DBusDirIter::d

DIR \* d

The DIR\* from opendir()

**Definition** dbus-sysdeps-util-unix.c:629

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusError::message

const char \* message

public error message field

**Definition** dbus-errors.h:53

DBusGroupInfo

Information about a UNIX group.

**Definition** dbus-sysdeps-unix.h:107

DBusGroupInfo::gid

dbus_gid_t gid

GID.

**Definition** dbus-sysdeps-unix.h:109

DBusGroupInfo::groupname

char \* groupname

Group name.

**Definition** dbus-sysdeps-unix.h:110

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
