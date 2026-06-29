dbus-spawn-unix.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-spawn-unix.c — Wrapper around fork/exec

3 \*

4 \* Copyright (C) 2002, 2003, 2004 Red Hat, Inc.

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

29\#if defined(DBUS_WIN) \|\| !defined(DBUS_UNIX)

30\#error "This file only makes sense on Unix OSs"

31\#endif

32

33\#include "dbus-spawn.h"

34\#include "dbus-sysdeps-unix.h"

35\#include "dbus-internals.h"

36\#include "dbus-test.h"

37\#include "dbus-protocol.h"

38

39\#include \<unistd.h\>

40\#include \<fcntl.h\>

41\#include \<signal.h\>

42\#include \<sys/wait.h\>

43\#include \<stdio.h\>

44\#include \<stdlib.h\>

45\#ifdef HAVE_ERRNO_H

46\#include \<errno.h\>

47\#endif

48\#ifdef HAVE_SYSTEMD

49\#ifdef HAVE_SYSLOG_H

50\#include \<syslog.h\>

51\#endif

52\#include \<systemd/sd-journal.h\>

53\#endif

54

55\#if defined(\_\_APPLE\_\_)

56\# include \<crt_externs.h\>

57\# define environ (\*\_NSGetEnviron ())

58\#elif !HAVE_DECL_ENVIRON

59extern char \*\*environ;

60\#endif

61

67/\*

68 \* I'm pretty sure this whole spawn file could be made simpler,

69 \* if you thought about it a bit.

70 \*/

71

75typedef enum

76{

77 READ_STATUS_OK,

78 READ_STATUS_ERROR,

79 READ_STATUS_EOF

80} ReadStatus;

81

82static ReadStatus

83read_ints (int fd,

84 int \*buf,

85 int n_ints_in_buf,

86 int \*n_ints_read,

87 DBusError \*error)

88{

89 size_t bytes = 0;

90 ReadStatus retval;

91

92 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

93

94 retval = READ_STATUS_OK;

95

96 while (TRUE)

97 {

98 ssize_t chunk;

99 size_t to_read;

100

101 to_read = sizeof (int) \* n_ints_in_buf - bytes;

102

103 if (to_read == 0)

104 break;

105

106 again:

107

108 chunk = read (fd,

109 ((char\*)buf) + bytes,

110 to_read);

111

112 if (chunk \< 0 && errno == EINTR)

113 goto again;

114

115 if (chunk \< 0)

116 {

117 dbus_set_error (error,

118 DBUS_ERROR_SPAWN_FAILED,

119 "Failed to read from child pipe (%s)",

120 \_dbus_strerror (errno));

121

122 retval = READ_STATUS_ERROR;

123 break;

124 }

125 else if (chunk == 0)

126 {

127 retval = READ_STATUS_EOF;

128 break; /\* EOF \*/

129 }

130 else /\* chunk \> 0 \*/

131 bytes += chunk;

132 }

133

134 \*n_ints_read = (int)(bytes / sizeof(int));

135

136 return retval;

137}

138

139static ReadStatus

140read_pid (int fd,

141 pid_t \*buf,

142 DBusError \*error)

143{

144 size_t bytes = 0;

145 ReadStatus retval;

146

147 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

148

149 retval = READ_STATUS_OK;

150

151 while (TRUE)

152 {

153 ssize_t chunk;

154 size_t to_read;

155

156 to_read = sizeof (pid_t) - bytes;

157

158 if (to_read == 0)

159 break;

160

161 again:

162

163 chunk = read (fd,

164 ((char\*)buf) + bytes,

165 to_read);

166 if (chunk \< 0 && errno == EINTR)

167 goto again;

168

169 if (chunk \< 0)

170 {

171 dbus_set_error (error,

172 DBUS_ERROR_SPAWN_FAILED,

173 "Failed to read from child pipe (%s)",

174 \_dbus_strerror (errno));

175

176 retval = READ_STATUS_ERROR;

177 break;

178 }

179 else if (chunk == 0)

180 {

181 retval = READ_STATUS_EOF;

182 break; /\* EOF \*/

183 }

184 else /\* chunk \> 0 \*/

185 bytes += chunk;

186 }

187

188 return retval;

189}

190

191/\* The implementation uses an intermediate child between the main process

192 \* and the grandchild. The grandchild is our spawned process. The intermediate

193 \* child is a babysitter process; it keeps track of when the grandchild

194 \* exits/crashes, and reaps the grandchild.

195 \*

196 \* We automatically reap the babysitter process, killing it if necessary,

197 \* when the DBusBabysitter's refcount goes to zero.

198 \*

199 \* Processes:

200 \*

201 \* main process

202 \* \| fork() A

203 \* \\ babysitter

204 \* \| fork () B

205 \* \\ grandchild --\> exec --\> spawned process

206 \*

207 \* IPC:

208 \* child_err_report_pipe

209 \* /-----------\<---------\<--------------\\

210 \* \| ^

211 \* v \|

212 \* main process babysitter grandchild

213 \* ^ ^

214 \* v v

215 \* \\------\<-\>-------/

216 \* babysitter_pipe

217 \*

218 \* child_err_report_pipe is genuinely a pipe.

219 \* The READ_END (also called error_pipe_from_child) is used in the main

220 \* process. The WRITE_END (also called child_err_report_fd) is used in

221 \* the grandchild process.

222 \*

223 \* On failure, the grandchild process sends CHILD_EXEC_FAILED + errno.

224 \* On success, the pipe just closes (because it's close-on-exec) without

225 \* sending any bytes.

226 \*

227 \* babysitter_pipe is mis-named: it's really a bidirectional socketpair.

228 \* The \[0\] end (also called socket_to_babysitter) is used in the main

229 \* process, the \[1\] end (also called parent_pipe) is used in the babysitter.

230 \*

231 \* If the fork() labelled B in the diagram above fails, the babysitter sends

232 \* CHILD_FORK_FAILED + errno.

233 \* On success, the babysitter sends CHILD_PID + the grandchild's pid.

234 \* On SIGCHLD, the babysitter sends CHILD_EXITED + the exit status.

235 \* The main process doesn't explicitly send anything, but when it exits,

236 \* the babysitter gets POLLHUP or POLLERR.

237 \*/

238

239/\* Messages from children to parents \*/

240enum

241{

242 CHILD_EXITED, /\* This message is followed by the exit status int \*/

243 CHILD_FORK_FAILED, /\* Followed by errno \*/

244 CHILD_EXEC_FAILED, /\* Followed by errno \*/

245 CHILD_PID /\* Followed by pid_t \*/

246};

247

251struct DBusBabysitter

252{

253 int refcount;

255 char \*log_name;

258 DBusSocket socket_to_babysitter;

259 int error_pipe_from_child;

261 pid_t sitter_pid;

262 pid_t grandchild_pid;

264 DBusWatchList \*watches;

266 DBusWatch \*error_watch;

267 DBusWatch \*sitter_watch;

269 DBusBabysitterFinishedFunc finished_cb;

270 void \*finished_data;

271

272 int errnum;

273 int status;

274 unsigned int have_child_status : 1;

275 unsigned int have_fork_errnum : 1;

276 unsigned int have_exec_errnum : 1;

277};

278

279static DBusBabysitter\*

280\_dbus_babysitter_new (void)

281{

282 DBusBabysitter \*sitter;

283

284 sitter = dbus_new0 (DBusBabysitter, 1);

285 if (sitter == NULL)

286 return NULL;

287

288 sitter-\>refcount = 1;

289

290 sitter-\>socket_to_babysitter.fd = -1;

291 sitter-\>error_pipe_from_child = -1;

292

293 sitter-\>sitter_pid = -1;

294 sitter-\>grandchild_pid = -1;

295

296 sitter-\>watches = \_dbus_watch_list_new ();

297 if (sitter-\>watches == NULL)

298 goto failed;

299

300 return sitter;

301

302 failed:

303 \_dbus_babysitter_unref (sitter);

304 return NULL;

305}

306

313DBusBabysitter \*

314\_dbus_babysitter_ref (DBusBabysitter \*sitter)

315{

316 \_dbus_assert (sitter != NULL);

317 \_dbus_assert (sitter-\>refcount \> 0);

318

319 sitter-\>refcount += 1;

320

321 return sitter;

322}

323

324static void close_socket_to_babysitter (DBusBabysitter \*sitter);

325static void close_error_pipe_from_child (DBusBabysitter \*sitter);

326

335void

336\_dbus_babysitter_unref (DBusBabysitter \*sitter)

337{

338 \_dbus_assert (sitter != NULL);

339 \_dbus_assert (sitter-\>refcount \> 0);

340

341 sitter-\>refcount -= 1;

342 if (sitter-\>refcount == 0)

343 {

344 /\* If we haven't forked other babysitters

345 \* since this babysitter and socket were

346 \* created then this close will cause the

347 \* babysitter to wake up from poll with

348 \* a hangup and then the babysitter will

349 \* quit itself.

350 \*/

351 close_socket_to_babysitter (sitter);

352

353 close_error_pipe_from_child (sitter);

354

355 if (sitter-\>sitter_pid \> 0)

356 {

357 int status;

358 int ret;

359

360 /\* It's possible the babysitter died on its own above

361 \* from the close, or was killed randomly

362 \* by some other process, so first try to reap it

363 \*/

364 ret = waitpid (sitter-\>sitter_pid, &status, WNOHANG);

365

366 /\* If we couldn't reap the child then kill it, and

367 \* try again

368 \*/

369 if (ret == 0)

370 kill (sitter-\>sitter_pid, SIGKILL);

371

372 if (ret == 0)

373 {

374 do

375 {

376 ret = waitpid (sitter-\>sitter_pid, &status, 0);

377 }

378 while (\_DBUS_UNLIKELY (ret \< 0 && errno == EINTR));

379 }

380

381 if (ret \< 0)

382 {

383 if (errno == ECHILD)

384 \_dbus_warn ("Babysitter process not available to be reaped; should not happen");

385 else

386 \_dbus_warn ("Unexpected error %d in waitpid() for babysitter: %s",

387 errno, \_dbus_strerror (errno));

388 }

389 else

390 {

391 \_dbus_verbose ("Reaped %ld, waiting for babysitter %ld\n",

392 (long) ret, (long) sitter-\>sitter_pid);

393

394 if (WIFEXITED (sitter-\>status))

395 \_dbus_verbose ("Babysitter exited with status %d\n",

396 WEXITSTATUS (sitter-\>status));

397 else if (WIFSIGNALED (sitter-\>status))

398 \_dbus_verbose ("Babysitter received signal %d\n",

399 WTERMSIG (sitter-\>status));

400 else

401 \_dbus_verbose ("Babysitter exited abnormally\n");

402 }

403

404 sitter-\>sitter_pid = -1;

405 }

406

407 if (sitter-\>watches)

408 \_dbus_watch_list_free (sitter-\>watches);

409

410 dbus_free (sitter-\>log_name);

411

412 dbus_free (sitter);

413 }

414}

415

416static ReadStatus

417read_data (DBusBabysitter \*sitter,

418 int fd)

419{

420 int what;

421 int got;

422 DBusError error = DBUS_ERROR_INIT;

423 ReadStatus r;

424

425 r = read_ints (fd, &what, 1, &got, &error);

426

427 switch (r)

428 {

429 case READ_STATUS_ERROR:

430 \_dbus_warn ("Failed to read data from fd %d: %s", fd, error.message);

431 dbus_error_free (&error);

432 return r;

433

434 case READ_STATUS_EOF:

435 return r;

436

437 case READ_STATUS_OK:

438 break;

439

440 default:

441 \_dbus_assert_not_reached ("invalid ReadStatus");

442 break;

443 }

444

445 if (got == 1)

446 {

447 switch (what)

448 {

449 case CHILD_EXITED:

450 case CHILD_FORK_FAILED:

451 case CHILD_EXEC_FAILED:

452 {

453 int arg;

454

455 r = read_ints (fd, &arg, 1, &got, &error);

456

457 switch (r)

458 {

459 case READ_STATUS_ERROR:

460 \_dbus_warn ("Failed to read arg from fd %d: %s", fd, error.message);

461 dbus_error_free (&error);

462 return r;

463 case READ_STATUS_EOF:

464 return r;

465 case READ_STATUS_OK:

466 break;

467 default:

468 \_dbus_assert_not_reached ("invalid ReadStatus");

469 break;

470 }

471

472 if (got == 1)

473 {

474 if (what == CHILD_EXITED)

475 {

476 /\* Do not reset sitter-\>errnum to 0 here. We get here if

477 \* the babysitter reports that the grandchild process has

478 \* exited, and there are two ways that can happen:

479 \*

480 \* 1. grandchild successfully exec()s the desired process,

481 \* but then the desired process exits or is terminated

482 \* by a signal. The babysitter observes this and reports

483 \* CHILD_EXITED.

484 \*

485 \* 2. grandchild fails to exec() the desired process,

486 \* attempts to report the exec() failure (which

487 \* we will receive as CHILD_EXEC_FAILED), and then

488 \* exits itself (which will prompt the babysitter to

489 \* send CHILD_EXITED). We want the CHILD_EXEC_FAILED

490 \* to take precedence (and have its errno logged),

491 \* which \_dbus_babysitter_set_child_exit_error() does.

492 \*/

493 sitter-\>have_child_status = TRUE;

494 sitter-\>status = arg;

495 \_dbus_verbose ("recorded child status exited = %d signaled = %d exitstatus = %d termsig = %d\n",

496 WIFEXITED (sitter-\>status), WIFSIGNALED (sitter-\>status),

497 WEXITSTATUS (sitter-\>status), WTERMSIG (sitter-\>status));

498 }

499 else if (what == CHILD_FORK_FAILED)

500 {

501 sitter-\>have_fork_errnum = TRUE;

502 sitter-\>errnum = arg;

503 \_dbus_verbose ("recorded fork errnum %d\n", sitter-\>errnum);

504 }

505 else if (what == CHILD_EXEC_FAILED)

506 {

507 sitter-\>have_exec_errnum = TRUE;

508 sitter-\>errnum = arg;

509 \_dbus_verbose ("recorded exec errnum %d\n", sitter-\>errnum);

510 }

511 }

512 }

513 break;

514 case CHILD_PID:

515 {

516 pid_t pid = -1;

517

518 r = read_pid (fd, &pid, &error);

519

520 switch (r)

521 {

522 case READ_STATUS_ERROR:

523 \_dbus_warn ("Failed to read PID from fd %d: %s", fd, error.message);

524 dbus_error_free (&error);

525 return r;

526 case READ_STATUS_EOF:

527 return r;

528 case READ_STATUS_OK:

529 break;

530 default:

531 \_dbus_assert_not_reached ("invalid ReadStatus");

532 break;

533 }

534

535 sitter-\>grandchild_pid = pid;

536

537 \_dbus_verbose ("recorded grandchild pid %d\n", sitter-\>grandchild_pid);

538 }

539 break;

540 default:

541 \_dbus_warn ("Unknown message received from babysitter process");

542 break;

543 }

544 }

545

546 return r;

547}

548

549static void

550close_socket_to_babysitter (DBusBabysitter \*sitter)

551{

552 \_dbus_verbose ("Closing babysitter\n");

553

554 if (sitter-\>sitter_watch != NULL)

555 {

556 \_dbus_assert (sitter-\>watches != NULL);

557 \_dbus_watch_list_remove_watch (sitter-\>watches, sitter-\>sitter_watch);

558 \_dbus_watch_invalidate (sitter-\>sitter_watch);

559 \_dbus_watch_unref (sitter-\>sitter_watch);

560 sitter-\>sitter_watch = NULL;

561 }

562

563 if (sitter-\>socket_to_babysitter.fd \>= 0)

564 {

565 \_dbus_close_socket (&sitter-\>socket_to_babysitter, NULL);

566 sitter-\>socket_to_babysitter.fd = -1;

567 }

568}

569

570static void

571close_error_pipe_from_child (DBusBabysitter \*sitter)

572{

573 \_dbus_verbose ("Closing child error\n");

574

575 if (sitter-\>error_watch != NULL)

576 {

577 \_dbus_assert (sitter-\>watches != NULL);

578 \_dbus_watch_list_remove_watch (sitter-\>watches, sitter-\>error_watch);

579 \_dbus_watch_invalidate (sitter-\>error_watch);

580 \_dbus_watch_unref (sitter-\>error_watch);

581 sitter-\>error_watch = NULL;

582 }

583

584 if (sitter-\>error_pipe_from_child \>= 0)

585 {

586 \_dbus_close (sitter-\>error_pipe_from_child, NULL);

587 sitter-\>error_pipe_from_child = -1;

588 }

589}

590

591static void

592handle_babysitter_socket (DBusBabysitter \*sitter,

593 int revents)

594{

595 /\* Even if we have POLLHUP, we want to keep reading

596 \* data until POLLIN goes away; so this function only

597 \* looks at HUP/ERR if no IN is set.

598 \*/

599 if (revents & \_DBUS_POLLIN)

600 {

601 \_dbus_verbose ("Reading data from babysitter\n");

602 if (read_data (sitter, sitter-\>socket_to_babysitter.fd) != READ_STATUS_OK)

603 close_socket_to_babysitter (sitter);

604 }

605 else if (revents & (\_DBUS_POLLERR \| \_DBUS_POLLHUP))

606 {

607 close_socket_to_babysitter (sitter);

608 }

609}

610

611static void

612handle_error_pipe (DBusBabysitter \*sitter,

613 int revents)

614{

615 if (revents & \_DBUS_POLLIN)

616 {

617 \_dbus_verbose ("Reading data from child error\n");

618 if (read_data (sitter, sitter-\>error_pipe_from_child) != READ_STATUS_OK)

619 close_error_pipe_from_child (sitter);

620 }

621 else if (revents & (\_DBUS_POLLERR \| \_DBUS_POLLHUP))

622 {

623 close_error_pipe_from_child (sitter);

624 }

625}

626

627/\* returns whether there were any poll events handled \*/

628static dbus_bool_t

629babysitter_iteration (DBusBabysitter \*sitter,

630 dbus_bool_t block)

631{

632 DBusPollFD fds\[2\];

633 int i;

634 dbus_bool_t descriptors_ready;

635

636 descriptors_ready = FALSE;

637

638 i = 0;

639

640 if (sitter-\>error_pipe_from_child \>= 0)

641 {

642 fds\[i\].fd = sitter-\>error_pipe_from_child;

643 fds\[i\].events = \_DBUS_POLLIN;

644 fds\[i\].revents = 0;

645 ++i;

646 }

647

648 if (sitter-\>socket_to_babysitter.fd \>= 0)

649 {

650 fds\[i\].fd = sitter-\>socket_to_babysitter.fd;

651 fds\[i\].events = \_DBUS_POLLIN;

652 fds\[i\].revents = 0;

653 ++i;

654 }

655

656 if (i \> 0)

657 {

658 int ret;

659

660 do

661 {

662 ret = \_dbus_poll (fds, i, 0);

663 }

664 while (ret \< 0 && errno == EINTR);

665

666 if (ret == 0 && block)

667 {

668 do

669 {

670 ret = \_dbus_poll (fds, i, -1);

671 }

672 while (ret \< 0 && errno == EINTR);

673 }

674

675 if (ret \> 0)

676 {

677 descriptors_ready = TRUE;

678

679 while (i \> 0)

680 {

681 --i;

682 if (fds\[i\].fd == sitter-\>error_pipe_from_child)

683 handle_error_pipe (sitter, fds\[i\].revents);

684 else if (fds\[i\].fd == sitter-\>socket_to_babysitter.fd)

685 handle_babysitter_socket (sitter, fds\[i\].revents);

686 }

687 }

688 }

689

690 return descriptors_ready;

691}

692

697\#define LIVE_CHILDREN(sitter) ((sitter)-\>socket_to_babysitter.fd \>= 0 \|\| (sitter)-\>error_pipe_from_child \>= 0)

698

705void

706\_dbus_babysitter_kill_child (DBusBabysitter \*sitter)

707{

708 /\* be sure we have the PID of the child \*/

709 while (LIVE_CHILDREN (sitter) &&

710 sitter-\>grandchild_pid == -1)

711 babysitter_iteration (sitter, TRUE);

712

713 \_dbus_verbose ("Got child PID %ld for killing\n",

714 (long) sitter-\>grandchild_pid);

715

716 if (sitter-\>grandchild_pid == -1)

717 return; /\* child is already dead, or we're so hosed we'll never recover \*/

718

719 kill (sitter-\>grandchild_pid, SIGKILL);

720}

721

727dbus_bool_t

728\_dbus_babysitter_get_child_exited (DBusBabysitter \*sitter)

729{

730

731 /\* Be sure we're up-to-date \*/

732 while (LIVE_CHILDREN (sitter) &&

733 babysitter_iteration (sitter, FALSE))

734 ;

735

736 /\* We will have exited the babysitter when the child has exited \*/

737 return sitter-\>socket_to_babysitter.fd \< 0;

738}

739

752dbus_bool_t

753\_dbus_babysitter_get_child_exit_status (DBusBabysitter \*sitter,

754 int \*status)

755{

756 if (!\_dbus_babysitter_get_child_exited (sitter))

757 \_dbus_assert_not_reached ("Child has not exited");

758

759 if (!sitter-\>have_child_status \|\|

760 !(WIFEXITED (sitter-\>status)))

761 return FALSE;

762

763 \*status = WEXITSTATUS (sitter-\>status);

764 return TRUE;

765}

766

776void

777\_dbus_babysitter_set_child_exit_error (DBusBabysitter \*sitter,

778 DBusError \*error)

779{

780 if (!\_dbus_babysitter_get_child_exited (sitter))

781 return;

782

783 /\* Note that if exec fails, we will also get a child status

784 \* from the babysitter saying the child exited,

785 \* so we need to give priority to the exec error

786 \*/

787 if (sitter-\>have_exec_errnum)

788 {

789 dbus_set_error (error, DBUS_ERROR_SPAWN_EXEC_FAILED,

790 "Failed to execute program %s: %s",

791 sitter-\>log_name, \_dbus_strerror (sitter-\>errnum));

792 }

793 else if (sitter-\>have_fork_errnum)

794 {

795 dbus_set_error (error, DBUS_ERROR_NO_MEMORY,

796 "Failed to fork a new process %s: %s",

797 sitter-\>log_name, \_dbus_strerror (sitter-\>errnum));

798 }

799 else if (sitter-\>have_child_status)

800 {

801 if (WIFEXITED (sitter-\>status))

802 dbus_set_error (error, DBUS_ERROR_SPAWN_CHILD_EXITED,

803 "Process %s exited with status %d",

804 sitter-\>log_name, WEXITSTATUS (sitter-\>status));

805 else if (WIFSIGNALED (sitter-\>status))

806 dbus_set_error (error, DBUS_ERROR_SPAWN_CHILD_SIGNALED,

807 "Process %s received signal %d",

808 sitter-\>log_name, WTERMSIG (sitter-\>status));

809 else

810 dbus_set_error (error, DBUS_ERROR_FAILED,

811 "Process %s exited abnormally",

812 sitter-\>log_name);

813 }

814 else

815 {

816 dbus_set_error (error, DBUS_ERROR_FAILED,

817 "Process %s exited, reason unknown",

818 sitter-\>log_name);

819 }

820}

821

834dbus_bool_t

835\_dbus_babysitter_set_watch_functions (DBusBabysitter \*sitter,

836 DBusAddWatchFunction add_function,

837 DBusRemoveWatchFunction remove_function,

838 DBusWatchToggledFunction toggled_function,

839 void \*data,

840 DBusFreeFunction free_data_function)

841{

842 return \_dbus_watch_list_set_functions (sitter-\>watches,

843 add_function,

844 remove_function,

845 toggled_function,

846 data,

847 free_data_function);

848}

849

850static dbus_bool_t

851handle_watch (DBusWatch \*watch,

852 unsigned int condition,

853 void \*data)

854{

855 DBusBabysitter \*sitter = \_dbus_babysitter_ref (data);

856 int revents;

857 int fd;

858

859 revents = 0;

860 if (condition & DBUS_WATCH_READABLE)

861 revents \|= \_DBUS_POLLIN;

862 if (condition & DBUS_WATCH_ERROR)

863 revents \|= \_DBUS_POLLERR;

864 if (condition & DBUS_WATCH_HANGUP)

865 revents \|= \_DBUS_POLLHUP;

866

867 fd = dbus_watch_get_socket (watch);

868

869 if (fd == sitter-\>error_pipe_from_child)

870 handle_error_pipe (sitter, revents);

871 else if (fd == sitter-\>socket_to_babysitter.fd)

872 handle_babysitter_socket (sitter, revents);

873

874 while (LIVE_CHILDREN (sitter) &&

875 babysitter_iteration (sitter, FALSE))

876 ;

877

878 /\* fd.o \#32992: if the handle\_\* methods closed their sockets, they previously

879 \* didn't always remove the watches. Check that we don't regress. \*/

880 \_dbus_assert (sitter-\>socket_to_babysitter.fd != -1 \|\| sitter-\>sitter_watch == NULL);

881 \_dbus_assert (sitter-\>error_pipe_from_child != -1 \|\| sitter-\>error_watch == NULL);

882

883 if (\_dbus_babysitter_get_child_exited (sitter) &&

884 sitter-\>finished_cb != NULL)

885 {

886 sitter-\>finished_cb (sitter, sitter-\>finished_data);

887 sitter-\>finished_cb = NULL;

888 }

889

890 \_dbus_babysitter_unref (sitter);

891 return TRUE;

892}

893

895\#define READ_END 0

897\#define WRITE_END 1

898

899

900/\* Avoids a danger in re-entrant situations (calling close()

901 \* on a file descriptor twice, and another module has

902 \* re-opened it since the first close).

903 \*

904 \* This previously claimed to be relevant for threaded situations, but by

905 \* trivial inspection, it is not thread-safe. It doesn't actually

906 \* matter, since this module is only used in the -util variant of the

907 \* library, which is only used in single-threaded situations.

908 \*/

909static int

910close_and_invalidate (int \*fd)

911{

912 int ret;

913

914 if (\*fd \< 0)

915 return -1;

916 else

917 {

918 ret = \_dbus_close (\*fd, NULL);

919 \*fd = -1;

920 }

921

922 return ret;

923}

924

925static dbus_bool_t

926make_pipe (int p\[2\],

927 DBusError \*error)

928{

929 int retval;

930

931\#ifdef HAVE_PIPE2

932 dbus_bool_t cloexec_done;

933

934 retval = pipe2 (p, O_CLOEXEC);

935 cloexec_done = retval \>= 0;

936

937 /\* Check if kernel seems to be too old to know pipe2(). We assume

938 that if pipe2 is available, O_CLOEXEC is too. \*/

939 if (retval \< 0 && errno == ENOSYS)

940\#endif

941 {

942 retval = pipe(p);

943 }

944

945 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

946

947 if (retval \< 0)

948 {

949 dbus_set_error (error,

950 DBUS_ERROR_SPAWN_FAILED,

951 "Failed to create pipe for communicating with child process (%s)",

952 \_dbus_strerror (errno));

953 return FALSE;

954 }

955

956\#ifdef HAVE_PIPE2

957 if (!cloexec_done)

958\#endif

959 {

960 \_dbus_fd_set_close_on_exec (p\[0\]);

961 \_dbus_fd_set_close_on_exec (p\[1\]);

962 }

963

964 return TRUE;

965}

966

967static void

968do_write (int fd, const void \*buf, size_t count)

969{

970 size_t bytes_written;

971 int ret;

972

973 bytes_written = 0;

974

975 again:

976

977 ret = write (fd, ((const char\*)buf) + bytes_written, count - bytes_written);

978

979 if (ret \< 0)

980 {

981 if (errno == EINTR)

982 goto again;

983 else

984 {

985 \_dbus_warn ("Failed to write data to pipe!");

986 exit (1); /\* give up, we suck \*/

987 }

988 }

989 else

990 bytes_written += ret;

991

992 if (bytes_written \< count)

993 goto again;

994}

995

996static void write_err_and_exit (int fd, int msg) \_DBUS_GNUC_NORETURN;

997

998static void

999write_err_and_exit (int fd, int msg)

1000{

1001 int en = errno;

1002

1003 do_write (fd, &msg, sizeof (msg));

1004 do_write (fd, &en, sizeof (en));

1005

1006 exit (1);

1007}

1008

1009static void

1010write_pid (int fd, pid_t pid)

1011{

1012 int msg = CHILD_PID;

1013

1014 do_write (fd, &msg, sizeof (msg));

1015 do_write (fd, &pid, sizeof (pid));

1016}

1017

1018static void write_status_and_exit (int fd, int status) \_DBUS_GNUC_NORETURN;

1019

1020static void

1021write_status_and_exit (int fd, int status)

1022{

1023 int msg = CHILD_EXITED;

1024

1025 do_write (fd, &msg, sizeof (msg));

1026 do_write (fd, &status, sizeof (status));

1027

1028 exit (0);

1029}

1030

1031static void do_exec (int child_err_report_fd,

1032 char \* const \*argv,

1033 char \* const \*envp,

1034 DBusSpawnChildSetupFunc child_setup,

1035 void \*user_data) \_DBUS_GNUC_NORETURN;

1036

1037static void

1038do_exec (int child_err_report_fd,

1039 char \* const \*argv,

1040 char \* const \*envp,

1041 DBusSpawnChildSetupFunc child_setup,

1042 void \*user_data)

1043{

1044\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

1045 int i, max_open;

1046\#endif

1047

1048 \_dbus_verbose_reset ();

1049 \_dbus_verbose ("Child process has PID " DBUS_PID_FORMAT "\n",

1050 \_dbus_getpid ());

1051

1052 if (child_setup)

1053 (\* child_setup) (user_data);

1054

1055\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

1056 max_open = sysconf (\_SC_OPEN_MAX);

1057

1058 /\* Because fds are allocated as numerically small as possible, we don't

1059 \* need to check the entire fd space, which can be prohibitively slow if

1060 \* the fd limit is very high. \*/

1061 if (max_open \> 1024)

1062 max_open = 1024;

1063

1064 for (i = 3; i \< max_open; i++)

1065 {

1066 int retval;

1067

1068 if (i == child_err_report_fd)

1069 continue;

1070

1071 retval = fcntl (i, F_GETFD);

1072

1073 if (retval != -1 && !(retval & FD_CLOEXEC))

1074 {

1075 char description\[256\] = { 0 };

1076 char proc_self_fd\[256\] = { 0 };

1077 size_t description_length = sizeof (description) - 1;

1078

1079 snprintf (proc_self_fd, sizeof (proc_self_fd) - 1,

1080 "/proc/self/fd/%d", i);

1081 proc_self_fd\[sizeof (proc_self_fd) - 1\] = '\0';

1082

1083 if (readlink (proc_self_fd, description, description_length) \<= 0)

1084 snprintf (description, sizeof (description) - 1, "(unknown)");

1085

1086 description\[sizeof (description) - 1\] = '\0';

1087 \_dbus_warn ("Fd %d \\%s\\ did not have the close-on-exec flag set!",

1088 i, description);

1089 }

1090 }

1091\#endif

1092

1093 if (envp == NULL)

1094 {

1095 \_dbus_assert (environ != NULL);

1096

1097 envp = environ;

1098 }

1099

1100 execve (argv\[0\], argv, envp);

1101

1102 /\* Exec failed \*/

1103 write_err_and_exit (child_err_report_fd,

1104 CHILD_EXEC_FAILED);

1105}

1106

1107static void

1108check_babysit_events (pid_t grandchild_pid,

1109 int parent_pipe,

1110 int revents)

1111{

1112 pid_t ret;

1113 int status;

1114

1115 do

1116 {

1117 ret = waitpid (grandchild_pid, &status, WNOHANG);

1118 /\* The man page says EINTR can't happen with WNOHANG,

1119 \* but there are reports of it (maybe only with valgrind?)

1120 \*/

1121 }

1122 while (ret \< 0 && errno == EINTR);

1123

1124 if (ret == 0)

1125 {

1126 \_dbus_verbose ("no child exited\n");

1127

1128 ; /\* no child exited \*/

1129 }

1130 else if (ret \< 0)

1131 {

1132 /\* This isn't supposed to happen. \*/

1133 \_dbus_warn ("unexpected waitpid() failure in check_babysit_events(): %s",

1134 \_dbus_strerror (errno));

1135 exit (1);

1136 }

1137 else if (ret == grandchild_pid)

1138 {

1139 /\* Child exited \*/

1140 \_dbus_verbose ("reaped child pid %ld\n", (long) ret);

1141

1142 write_status_and_exit (parent_pipe, status);

1143 }

1144 else

1145 {

1146 \_dbus_warn ("waitpid() reaped pid %d that we've never heard of",

1147 (int) ret);

1148 exit (1);

1149 }

1150

1151 if (revents & \_DBUS_POLLIN)

1152 {

1153 \_dbus_verbose ("babysitter got POLLIN from parent pipe\n");

1154 }

1155

1156 if (revents & (\_DBUS_POLLERR \| \_DBUS_POLLHUP))

1157 {

1158 /\* Parent is gone, so we just exit \*/

1159 \_dbus_verbose ("babysitter got POLLERR or POLLHUP from parent\n");

1160 exit (0);

1161 }

1162}

1163

1164/\* Only used in a single-threaded child process, does not need to be

1165 \* thread-safe \*/

1166static int babysit_sigchld_pipe = -1;

1167

1168static void

1169babysit_signal_handler (int signo)

1170{

1171 /\* Signal handlers that might set errno must save and restore the errno

1172 \* that the interrupted function might have been relying on. \*/

1173 int saved_errno = errno;

1174 char b = '\0';

1175

1176 again:

1177 if (write (babysit_sigchld_pipe, &b, 1) \<= 0)

1178 if (errno == EINTR)

1179 goto again;

1180

1181 errno = saved_errno;

1182}

1183

1184static void babysit (pid_t grandchild_pid,

1185 int parent_pipe) \_DBUS_GNUC_NORETURN;

1186

1187static void

1188babysit (pid_t grandchild_pid,

1189 int parent_pipe)

1190{

1191 int sigchld_pipe\[2\];

1192

1193 /\* We don't exec, so we keep parent state, such as the pid that

1194 \* \_dbus_verbose() uses. Reset the pid here.

1195 \*/

1196 \_dbus_verbose_reset ();

1197

1198 /\* I thought SIGCHLD would just wake up the poll, but

1199 \* that didn't seem to work, so added this pipe.

1200 \* Probably the pipe is more likely to work on busted

1201 \* operating systems anyhow.

1202 \*/

1203 if (pipe (sigchld_pipe) \< 0)

1204 {

1205 \_dbus_warn ("Not enough file descriptors to create pipe in babysitter process");

1206 exit (1);

1207 }

1208

1209 babysit_sigchld_pipe = sigchld_pipe\[WRITE_END\];

1210

1211 \_dbus_set_signal_handler (SIGCHLD, babysit_signal_handler);

1212

1213 write_pid (parent_pipe, grandchild_pid);

1214

1215 check_babysit_events (grandchild_pid, parent_pipe, 0);

1216

1217 while (TRUE)

1218 {

1219 DBusPollFD pfds\[2\];

1220

1221 pfds\[0\].fd = parent_pipe;

1222 pfds\[0\].events = \_DBUS_POLLIN;

1223 pfds\[0\].revents = 0;

1224

1225 pfds\[1\].fd = sigchld_pipe\[READ_END\];

1226 pfds\[1\].events = \_DBUS_POLLIN;

1227 pfds\[1\].revents = 0;

1228

1229 if (\_dbus_poll (pfds, \_DBUS_N_ELEMENTS (pfds), -1) \< 0 && errno != EINTR)

1230 {

1231 \_dbus_warn ("\_dbus_poll() error: %s", strerror (errno));

1232 exit (1);

1233 }

1234

1235 if (pfds\[0\].revents != 0)

1236 {

1237 check_babysit_events (grandchild_pid, parent_pipe, pfds\[0\].revents);

1238 }

1239 else if (pfds\[1\].revents & \_DBUS_POLLIN)

1240 {

1241 char b;

1242 if (read (sigchld_pipe\[READ_END\], &b, 1) == -1)

1243 {

1244 /\* ignore \*/

1245 }

1246 /\* do waitpid check \*/

1247 check_babysit_events (grandchild_pid, parent_pipe, 0);

1248 }

1249 }

1250

1251 exit (1);

1252}

1253

1278dbus_bool_t

1279\_dbus_spawn_async_with_babysitter (DBusBabysitter \*\*sitter_p,

1280 const char \*log_name,

1281 char \* const \*argv,

1282 char \* const \*env,

1283 DBusSpawnFlags flags,

1284 DBusSpawnChildSetupFunc child_setup,

1285 void \*user_data,

1286 DBusError \*error)

1287{

1288 DBusBabysitter \*sitter;

1289 int child_err_report_pipe\[2\] = { -1, -1 };

1290 DBusSocket babysitter_pipe\[2\] = { DBUS_SOCKET_INIT, DBUS_SOCKET_INIT };

1291 pid_t pid;

1292 int fd_out = -1;

1293 int fd_err = -1;

1294

1295 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

1296 \_dbus_assert (argv\[0\] != NULL);

1297

1298 if (sitter_p != NULL)

1299 \*sitter_p = NULL;

1300

1301 sitter = NULL;

1302

1303 sitter = \_dbus_babysitter_new ();

1304 if (sitter == NULL)

1305 {

1306 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

1307 return FALSE;

1308 }

1309

1310 sitter-\>log_name = \_dbus_strdup (log_name);

1311 if (sitter-\>log_name == NULL && log_name != NULL)

1312 {

1313 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

1314 goto cleanup_and_fail;

1315 }

1316

1317 if (sitter-\>log_name == NULL)

1318 sitter-\>log_name = \_dbus_strdup (argv\[0\]);

1319

1320 if (sitter-\>log_name == NULL)

1321 {

1322 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

1323 goto cleanup_and_fail;

1324 }

1325

1326 if (!make_pipe (child_err_report_pipe, error))

1327 goto cleanup_and_fail;

1328

1329 if (!\_dbus_socketpair (&babysitter_pipe\[0\], &babysitter_pipe\[1\], TRUE, error))

1330 goto cleanup_and_fail;

1331

1332 /\* Setting up the babysitter is only useful in the parent,

1333 \* but we don't want to run out of memory and fail

1334 \* after we've already forked, since then we'd leak

1335 \* child processes everywhere.

1336 \*/

1337 sitter-\>error_watch = \_dbus_watch_new (child_err_report_pipe\[READ_END\],

1338 DBUS_WATCH_READABLE,

1339 TRUE, handle_watch, sitter, NULL);

1340 if (sitter-\>error_watch == NULL)

1341 {

1342 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

1343 goto cleanup_and_fail;

1344 }

1345

1346 if (!\_dbus_watch_list_add_watch (sitter-\>watches, sitter-\>error_watch))

1347 {

1348 /\* we need to free it early so the destructor won't try to remove it

1349 \* without it having been added, which DBusLoop doesn't allow \*/

1350 \_dbus_watch_invalidate (sitter-\>error_watch);

1351 \_dbus_watch_unref (sitter-\>error_watch);

1352 sitter-\>error_watch = NULL;

1353

1354 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

1355 goto cleanup_and_fail;

1356 }

1357

1358 sitter-\>sitter_watch = \_dbus_watch_new (babysitter_pipe\[0\].fd,

1359 DBUS_WATCH_READABLE,

1360 TRUE, handle_watch, sitter, NULL);

1361 if (sitter-\>sitter_watch == NULL)

1362 {

1363 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

1364 goto cleanup_and_fail;

1365 }

1366

1367 if (!\_dbus_watch_list_add_watch (sitter-\>watches, sitter-\>sitter_watch))

1368 {

1369 /\* we need to free it early so the destructor won't try to remove it

1370 \* without it having been added, which DBusLoop doesn't allow \*/

1371 \_dbus_watch_invalidate (sitter-\>sitter_watch);

1372 \_dbus_watch_unref (sitter-\>sitter_watch);

1373 sitter-\>sitter_watch = NULL;

1374

1375 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

1376 goto cleanup_and_fail;

1377 }

1378

1379 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

1380

1381 if (flags & DBUS_SPAWN_SILENCE_OUTPUT)

1382 {

1383 fd_out = open ("/dev/null", O_RDONLY);

1384

1385 if (fd_out \< 0)

1386 {

1387 dbus_set_error (error, \_dbus_error_from_errno (errno),

1388 "Failed to open /dev/null: %s",

1389 \_dbus_strerror (errno));

1390 goto cleanup_and_fail;

1391 }

1392

1393 \_dbus_fd_set_close_on_exec (fd_out);

1394

1395 fd_err = \_dbus_dup (fd_out, error);

1396

1397 if (fd_err \< 0)

1398 goto cleanup_and_fail;

1399 }

1400\#ifdef HAVE_SYSTEMD

1401 else if (flags & DBUS_SPAWN_REDIRECT_OUTPUT)

1402 {

1403 /\* This may fail, but it's not critical.

1404 \* In particular, if we were compiled with journald support but are now

1405 \* running on a non-systemd system, this is going to fail, so we

1406 \* have to cope gracefully. \*/

1407 fd_out = sd_journal_stream_fd (sitter-\>log_name, LOG_INFO, FALSE);

1408 fd_err = sd_journal_stream_fd (sitter-\>log_name, LOG_WARNING, FALSE);

1409 }

1410\#endif

1411

1412 /\* Make sure our output buffers aren't redundantly printed by both the

1413 \* parent and the child \*/

1414 fflush (stdout);

1415 fflush (stderr);

1416

1417 pid = fork ();

1418

1419 if (pid \< 0)

1420 {

1421 dbus_set_error (error,

1422 DBUS_ERROR_SPAWN_FORK_FAILED,

1423 "Failed to fork (%s)",

1424 \_dbus_strerror (errno));

1425 goto cleanup_and_fail;

1426 }

1427 else if (pid == 0)

1428 {

1429 /\* Immediate child, this is the babysitter process. \*/

1430 int grandchild_pid;

1431

1432 /\* Be sure we crash if the parent exits

1433 \* and we write to the err_report_pipe

1434 \*/

1435 signal (SIGPIPE, SIG_DFL);

1436

1437 /\* Close the parent's end of the pipes. \*/

1438 close_and_invalidate (&child_err_report_pipe\[READ_END\]);

1439 close_and_invalidate (&babysitter_pipe\[0\].fd);

1440

1441 fflush (stdout);

1442 fflush (stderr);

1443

1444 /\* Create the child that will exec () \*/

1445 grandchild_pid = fork ();

1446

1447 if (grandchild_pid \< 0)

1448 {

1449 write_err_and_exit (babysitter_pipe\[1\].fd,

1450 CHILD_FORK_FAILED);

1451 \_dbus_assert_not_reached ("Got to code after write_err_and_exit()");

1452 }

1453 else if (grandchild_pid == 0)

1454 {

1455 /\* This might not succeed in a dbus-daemon that started as root

1456 \* and dropped privileges, so don't log an error on failure.

1457 \* (Also, we can't safely log errors here anyway, because logging

1458 \* is not async-signal safe). \*/

1459 \_dbus_reset_oom_score_adj (NULL);

1460

1461 /\* Go back to ignoring SIGPIPE, since it's evil

1462 \*/

1463 signal (SIGPIPE, SIG_IGN);

1464

1465 close_and_invalidate (&babysitter_pipe\[1\].fd);

1466

1467 /\* Redirect stdout, stderr to systemd Journal or /dev/null

1468 \* as requested, if possible \*/

1469 if (fd_out \>= 0)

1470 dup2 (fd_out, STDOUT_FILENO);

1471 if (fd_err \>= 0)

1472 dup2 (fd_err, STDERR_FILENO);

1473 close_and_invalidate (&fd_out);

1474 close_and_invalidate (&fd_err);

1475

1476 do_exec (child_err_report_pipe\[WRITE_END\],

1477 argv,

1478 env,

1479 child_setup, user_data);

1480 \_dbus_assert_not_reached ("Got to code after exec() - should have exited on error");

1481 }

1482 else

1483 {

1484 close_and_invalidate (&child_err_report_pipe\[WRITE_END\]);

1485 close_and_invalidate (&fd_out);

1486 close_and_invalidate (&fd_err);

1487 babysit (grandchild_pid, babysitter_pipe\[1\].fd);

1488 \_dbus_assert_not_reached ("Got to code after babysit()");

1489 }

1490 }

1491 else

1492 {

1493 /\* Close the uncared-about ends of the pipes \*/

1494 close_and_invalidate (&child_err_report_pipe\[WRITE_END\]);

1495 close_and_invalidate (&babysitter_pipe\[1\].fd);

1496 close_and_invalidate (&fd_out);

1497 close_and_invalidate (&fd_err);

1498

1499 sitter-\>socket_to_babysitter = babysitter_pipe\[0\];

1500 babysitter_pipe\[0\].fd = -1;

1501

1502 sitter-\>error_pipe_from_child = child_err_report_pipe\[READ_END\];

1503 child_err_report_pipe\[READ_END\] = -1;

1504

1505 sitter-\>sitter_pid = pid;

1506

1507 if (sitter_p != NULL)

1508 \*sitter_p = sitter;

1509 else

1510 \_dbus_babysitter_unref (sitter);

1511

1512 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

1513

1514 return TRUE;

1515 }

1516

1517 cleanup_and_fail:

1518

1519 \_DBUS_ASSERT_ERROR_IS_SET (error);

1520

1521 close_and_invalidate (&child_err_report_pipe\[READ_END\]);

1522 close_and_invalidate (&child_err_report_pipe\[WRITE_END\]);

1523 close_and_invalidate (&babysitter_pipe\[0\].fd);

1524 close_and_invalidate (&babysitter_pipe\[1\].fd);

1525 close_and_invalidate (&fd_out);

1526 close_and_invalidate (&fd_err);

1527

1528 if (sitter != NULL)

1529 \_dbus_babysitter_unref (sitter);

1530

1531 return FALSE;

1532}

1533

1534void

1535\_dbus_babysitter_set_result_function (DBusBabysitter \*sitter,

1536 DBusBabysitterFinishedFunc finished,

1537 void \*user_data)

1538{

1539 sitter-\>finished_cb = finished;

1540 sitter-\>finished_data = user_data;

1541}

1542

1545void

1546\_dbus_babysitter_block_for_child_exit (DBusBabysitter \*sitter)

1547{

1548 while (LIVE_CHILDREN (sitter))

1549 babysitter_iteration (sitter, TRUE);

1550}

DBusWatchToggledFunction

void(\* DBusWatchToggledFunction)(DBusWatch \*watch, void \*data)

Called when dbus_watch_get_enabled() may return a different value than it did before.

**Definition** dbus-connection.h:100

DBusAddWatchFunction

dbus_bool_t(\* DBusAddWatchFunction)(DBusWatch \*watch, void \*data)

Called when libdbus needs a new watch to be monitored by the main loop.

**Definition** dbus-connection.h:94

DBusRemoveWatchFunction

void(\* DBusRemoveWatchFunction)(DBusWatch \*watch, void \*data)

Called when libdbus no longer needs a watch to be monitored by the main loop.

**Definition** dbus-connection.h:106

DBUS_WATCH_READABLE

@ DBUS_WATCH_READABLE

As in POLLIN.

**Definition** dbus-connection.h:63

DBUS_WATCH_HANGUP

@ DBUS_WATCH_HANGUP

As in POLLHUP (can't watch for it, but can be present in current state passed to dbus_watch_handle())...

**Definition** dbus-connection.h:70

DBUS_WATCH_ERROR

@ DBUS_WATCH_ERROR

As in POLLERR (can't watch for this, but can be present in current state passed to dbus_watch_handle(...

**Definition** dbus-connection.h:65

DBUS_ERROR_INIT

\#define DBUS_ERROR_INIT

Expands to a suitable initializer for a DBusError on the stack.

**Definition** dbus-errors.h:64

dbus_set_error

void dbus_set_error(DBusError \*error, const char \*name, const char \*format,...)

Assigns an error name and message to a DBusError.

**Definition** dbus-errors.c:356

dbus_error_free

void dbus_error_free(DBusError \*error)

Frees an error that's been set (or just initialized), then reinitializes the error as in dbus_error_i...

**Definition** dbus-errors.c:213

\_dbus_assert_not_reached

\#define \_dbus_assert_not_reached(explanation)

Aborts with an error message if called.

**Definition** dbus-internals.h:164

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_dbus_babysitter_get_child_exit_status

dbus_bool_t \_dbus_babysitter_get_child_exit_status(DBusBabysitter \*sitter, int \*status)

Gets the exit status of the child.

**Definition** dbus-spawn-unix.c:753

READ_END

\#define READ_END

Helps remember which end of the pipe is which.

**Definition** dbus-spawn-unix.c:895

WRITE_END

\#define WRITE_END

Helps remember which end of the pipe is which.

**Definition** dbus-spawn-unix.c:897

\_dbus_babysitter_unref

void \_dbus_babysitter_unref(DBusBabysitter \*sitter)

Decrement the reference count on the babysitter object.

**Definition** dbus-spawn-unix.c:336

\_dbus_error_from_errno

const char \* \_dbus_error_from_errno(int error_number)

Converts a UNIX errno, or Windows errno or WinSock error value into a DBusError name.

**Definition** dbus-sysdeps.c:565

\_dbus_babysitter_get_child_exited

dbus_bool_t \_dbus_babysitter_get_child_exited(DBusBabysitter \*sitter)

Checks whether the child has exited, without blocking.

**Definition** dbus-spawn-unix.c:728

\_dbus_babysitter_set_watch_functions

dbus_bool_t \_dbus_babysitter_set_watch_functions(DBusBabysitter \*sitter, DBusAddWatchFunction add_function, DBusRemoveWatchFunction remove_function, DBusWatchToggledFunction toggled_function, void \*data, DBusFreeFunction free_data_function)

Sets watch functions to notify us when the babysitter object needs to read/write file descriptors.

**Definition** dbus-spawn-unix.c:835

\_dbus_strdup

char \* \_dbus_strdup(const char \*str)

Duplicates a string.

**Definition** dbus-internals.c:621

\_dbus_babysitter_set_child_exit_error

void \_dbus_babysitter_set_child_exit_error(DBusBabysitter \*sitter, DBusError \*error)

Sets the DBusError with an explanation of why the spawned child process exited (on a signal,...

**Definition** dbus-spawn-unix.c:777

ReadStatus

ReadStatus

Enumeration for status of a read()

**Definition** dbus-spawn-unix.c:76

\_dbus_warn

void \_dbus_warn(const char \*format,...)

Prints a warning message to stderr.

**Definition** dbus-internals.c:278

\_DBUS_N_ELEMENTS

\#define \_DBUS_N_ELEMENTS(array)

Computes the number of elements in a fixed-size array using sizeof().

**Definition** dbus-internals.h:189

\_dbus_babysitter_kill_child

void \_dbus_babysitter_kill_child(DBusBabysitter \*sitter)

Blocks until the babysitter process gives us the PID of the spawned grandchild, then kills the spawne...

**Definition** dbus-spawn-unix.c:706

\_dbus_babysitter_ref

DBusBabysitter \* \_dbus_babysitter_ref(DBusBabysitter \*sitter)

Increment the reference count on the babysitter object.

**Definition** dbus-spawn-unix.c:314

\_dbus_spawn_async_with_babysitter

dbus_bool_t \_dbus_spawn_async_with_babysitter(DBusBabysitter \*\*sitter_p, const char \*log_name, char \*const \*argv, char \*const \*env, DBusSpawnFlags flags, DBusSpawnChildSetupFunc child_setup, void \*user_data, DBusError \*error)

Spawns a new process.

**Definition** dbus-spawn-unix.c:1279

LIVE_CHILDREN

\#define LIVE_CHILDREN(sitter)

Macro returns TRUE if the babysitter still has live sockets open to the babysitter child or the grand...

**Definition** dbus-spawn-unix.c:697

READ_STATUS_OK

@ READ_STATUS_OK

Read succeeded.

**Definition** dbus-spawn-unix.c:77

READ_STATUS_EOF

@ READ_STATUS_EOF

EOF returned.

**Definition** dbus-spawn-unix.c:79

READ_STATUS_ERROR

@ READ_STATUS_ERROR

Some kind of error.

**Definition** dbus-spawn-unix.c:78

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

DBusFreeFunction

void(\* DBusFreeFunction)(void \*memory)

The type of a function which frees a block of memory.

**Definition** dbus-memory.h:65

dbus_free

void dbus_free(void \*memory)

Frees a block of memory previously allocated by dbus_malloc() or dbus_malloc0().

**Definition** dbus-memory.c:710

dbus_new0

\#define dbus_new0(type, count)

Safe macro for using dbus_malloc0().

**Definition** dbus-memory.h:60

DBUS_ERROR_SPAWN_CHILD_EXITED

\#define DBUS_ERROR_SPAWN_CHILD_EXITED

While starting a new process, the child exited with a status code.

**Definition** dbus-protocol.h:426

DBUS_ERROR_SPAWN_CHILD_SIGNALED

\#define DBUS_ERROR_SPAWN_CHILD_SIGNALED

While starting a new process, the child exited on a signal.

**Definition** dbus-protocol.h:428

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

DBUS_ERROR_SPAWN_FAILED

\#define DBUS_ERROR_SPAWN_FAILED

While starting a new process, something went wrong.

**Definition** dbus-protocol.h:430

DBUS_ERROR_SPAWN_FORK_FAILED

\#define DBUS_ERROR_SPAWN_FORK_FAILED

While starting a new process, the fork() call failed.

**Definition** dbus-protocol.h:424

\_dbus_reset_oom_score_adj

dbus_bool_t \_dbus_reset_oom_score_adj(const char \*\*error_str_p)

If the current process has been protected from the Linux OOM killer (the oom_score_adj process parame...

**Definition** dbus-sysdeps-util-unix.c:1602

\_dbus_close

dbus_bool_t \_dbus_close(int fd, DBusError \*error)

Closes a file descriptor.

**Definition** dbus-sysdeps-unix.c:3727

\_dbus_set_signal_handler

void \_dbus_set_signal_handler(int sig, DBusSignalHandler handler)

Installs a UNIX signal handler.

**Definition** dbus-sysdeps-util-unix.c:545

\_dbus_dup

int \_dbus_dup(int fd, DBusError \*error)

Duplicates a file descriptor.

**Definition** dbus-sysdeps-unix.c:3755

\_dbus_fd_set_close_on_exec

void \_dbus_fd_set_close_on_exec(int fd)

Sets the file descriptor to be close on exec.

**Definition** dbus-sysdeps-unix.c:3683

\_DBUS_POLLERR

\#define \_DBUS_POLLERR

Error condition.

**Definition** dbus-sysdeps.h:450

\_dbus_socketpair

dbus_bool_t \_dbus_socketpair(DBusSocket \*fd1, DBusSocket \*fd2, dbus_bool_t blocking, DBusError \*error)

Creates pair of connect sockets (as in socketpair()).

**Definition** dbus-sysdeps-unix.c:3884

\_dbus_getpid

dbus_pid_t \_dbus_getpid(void)

Gets our process ID.

**Definition** dbus-sysdeps-unix.c:3127

\_DBUS_POLLHUP

\#define \_DBUS_POLLHUP

Hung up.

**Definition** dbus-sysdeps.h:452

\_DBUS_POLLIN

\#define \_DBUS_POLLIN

There is data to read.

**Definition** dbus-sysdeps.h:444

\_dbus_close_socket

dbus_bool_t \_dbus_close_socket(DBusSocket \*fd, DBusError \*error)

Closes a socket and invalidates it.

**Definition** dbus-sysdeps-unix.c:314

\_dbus_poll

int \_dbus_poll(DBusPollFD \*fds, int n_fds, int timeout_milliseconds)

Wrapper for poll().

**Definition** dbus-sysdeps-unix.c:3303

DBUS_PID_FORMAT

\#define DBUS_PID_FORMAT

an appropriate printf format for dbus_pid_t

**Definition** dbus-sysdeps.h:153

\_dbus_watch_list_add_watch

dbus_bool_t \_dbus_watch_list_add_watch(DBusWatchList \*watch_list, DBusWatch \*watch)

Adds a new watch to the watch list, invoking the application DBusAddWatchFunction if appropriate.

**Definition** dbus-watch.c:383

\_dbus_watch_list_new

DBusWatchList \* \_dbus_watch_list_new(void)

Creates a new watch list.

**Definition** dbus-watch.c:234

\_dbus_watch_list_free

void \_dbus_watch_list_free(DBusWatchList \*watch_list)

Frees a DBusWatchList.

**Definition** dbus-watch.c:251

\_dbus_watch_list_set_functions

dbus_bool_t \_dbus_watch_list_set_functions(DBusWatchList \*watch_list, DBusAddWatchFunction add_function, DBusRemoveWatchFunction remove_function, DBusWatchToggledFunction toggled_function, void \*data, DBusFreeFunction free_data_function)

Sets the watch functions.

**Definition** dbus-watch.c:297

\_dbus_watch_new

DBusWatch \* \_dbus_watch_new(DBusPollable fd, unsigned int flags, dbus_bool_t enabled, DBusWatchHandler handler, void \*data, DBusFreeFunction free_data_function)

Creates a new DBusWatch.

**Definition** dbus-watch.c:90

\_dbus_watch_unref

void \_dbus_watch_unref(DBusWatch \*watch)

Decrements the reference count of a DBusWatch object and finalizes the object if the count reaches ze...

**Definition** dbus-watch.c:140

\_dbus_watch_list_remove_watch

void \_dbus_watch_list_remove_watch(DBusWatchList \*watch_list, DBusWatch \*watch)

Removes a watch from the watch list, invoking the application's DBusRemoveWatchFunction if appropriat...

**Definition** dbus-watch.c:416

\_dbus_watch_invalidate

void \_dbus_watch_invalidate(DBusWatch \*watch)

Clears the file descriptor from a now-invalid watch object so that no one tries to use it.

**Definition** dbus-watch.c:171

dbus_watch_get_socket

DBUS_EXPORT int dbus_watch_get_socket(DBusWatch \*watch)

Returns a socket to be watched, on UNIX this will return -1 if our transport is not socket-based so d...

**Definition** dbus-watch.c:595

DBusBabysitter

Babysitter implementation details.

**Definition** dbus-spawn-unix.c:252

DBusBabysitter::sitter_watch

DBusWatch \* sitter_watch

Sitter pipe watch.

**Definition** dbus-spawn-unix.c:267

DBusBabysitter::have_exec_errnum

unsigned int have_exec_errnum

True if we have an error code from exec()

**Definition** dbus-spawn-unix.c:276

DBusBabysitter::socket_to_babysitter

DBusSocket socket_to_babysitter

Connection to the babysitter process.

**Definition** dbus-spawn-unix.c:258

DBusBabysitter::status

int status

Exit status code.

**Definition** dbus-spawn-unix.c:273

DBusBabysitter::have_child_status

unsigned int have_child_status

True if child status has been reaped.

**Definition** dbus-spawn-unix.c:274

DBusBabysitter::log_name

char \* log_name

the name under which to log messages about this process being spawned

**Definition** dbus-spawn-unix.c:255

DBusBabysitter::sitter_pid

pid_t sitter_pid

PID Of the babysitter.

**Definition** dbus-spawn-unix.c:261

DBusBabysitter::errnum

int errnum

Error number.

**Definition** dbus-spawn-unix.c:272

DBusBabysitter::error_pipe_from_child

int error_pipe_from_child

Connection to the process that does the exec()

**Definition** dbus-spawn-unix.c:259

DBusBabysitter::refcount

int refcount

Reference count.

**Definition** dbus-spawn-unix.c:253

DBusBabysitter::watches

DBusWatchList \* watches

Watches.

**Definition** dbus-spawn-unix.c:264

DBusBabysitter::error_watch

DBusWatch \* error_watch

Error pipe watch.

**Definition** dbus-spawn-unix.c:266

DBusBabysitter::grandchild_pid

pid_t grandchild_pid

PID of the grandchild.

**Definition** dbus-spawn-unix.c:262

DBusBabysitter::have_fork_errnum

unsigned int have_fork_errnum

True if we have an error code from fork()

**Definition** dbus-spawn-unix.c:275

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusError::message

const char \* message

public error message field

**Definition** dbus-errors.h:53

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

DBusWatchList

DBusWatchList implementation details.

**Definition** dbus-watch.c:217

DBusWatch

Implementation of DBusWatch.

**Definition** dbus-watch.c:43
