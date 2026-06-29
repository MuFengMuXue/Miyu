dbus-spawn-win.c

1\#include \<config.h\>

2

3//#define SPAWN_DEBUG

4

5\#if !defined(SPAWN_DEBUG) \|\| defined(\_MSC_VER)

6\#define PING()

7\#else

8\#define PING() fprintf (stderr, "%s:%s:%d\n", \_\_FILE\_\_, \_DBUS_FUNCTION_NAME, \_\_LINE\_\_); fflush (stderr)

9\#endif

10

11\#include \<stdio.h\>

12

13/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

14/\* dbus-spawn-win32.c Wrapper around g_spawn

15 \*

16 \* Copyright (C) 2002, 2003, 2004 Red Hat, Inc.

17 \* Copyright (C) 2003 CodeFactory AB

18 \* Copyright (C) 2005 Novell, Inc.

19 \*

20 \* SPDX-License-Identifier: AFL-2.1 OR GPL-2.0-or-later

21 \*

22 \* Licensed under the Academic Free License version 2.1

23 \*

24 \* This program is free software; you can redistribute it and/or modify

25 \* it under the terms of the GNU General Public License as published by

26 \* the Free Software Foundation; either version 2 of the License, or

27 \* (at your option) any later version.

28 \*

29 \* This program is distributed in the hope that it will be useful,

30 \* but WITHOUT ANY WARRANTY; without even the implied warranty of

31 \* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the

32 \* GNU General Public License for more details.

33 \*

34 \* You should have received a copy of the GNU General Public License

35 \* along with this program; if not, write to the Free Software

36 \* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

37 \*

38 \*/

39\#include "dbus-spawn.h"

40\#include "dbus-sysdeps.h"

41\#include "dbus-sysdeps-win.h"

42\#include "dbus-internals.h"

43\#include "dbus-test.h"

44\#include "dbus-protocol.h"

45

46\#define WIN32_LEAN_AND_MEAN

47\#include \<windows.h\>

48//#define STRICT

49//#include \<windows.h\>

50//#undef STRICT

51\#include \<winsock2.h\>

52\#undef interface

53

54\#include \<stdlib.h\>

55

56\#ifndef DBUS_WINCE

57\#include \<process.h\>

58\#endif

59

63struct DBusBabysitter

64 {

65 DBusAtomic refcount;

66 char \*log_name;

67

68 HANDLE thread_handle;

69 HANDLE child_handle;

70 DBusSocket socket_to_babysitter; /\* Connection to the babysitter thread \*/

71 DBusSocket socket_to_main;

72

73 DBusWatchList \*watches;

74 DBusWatch \*sitter_watch;

75 DBusBabysitterFinishedFunc finished_cb;

76 void \*finished_data;

77

78 dbus_bool_t have_spawn_errno;

79 int spawn_errno;

80 dbus_bool_t have_child_status;

81 int child_status;

82 };

83

84static void

85\_dbus_babysitter_trace_ref (DBusBabysitter \*sitter,

86 int old_refcount,

87 int new_refcount,

88 const char \*why)

89{

90\#ifdef DBUS_ENABLE_VERBOSE_MODE

91 static int enabled = -1;

92

93 \_dbus_trace_ref ("DBusBabysitter", sitter, old_refcount, new_refcount, why,

94 "DBUS_BABYSITTER_TRACE", &enabled);

95\#endif

96}

97

98static DBusBabysitter\*

99\_dbus_babysitter_new (void)

100{

101 DBusBabysitter \*sitter;

102 dbus_int32_t old_refcount;

103

104 sitter = dbus_new0 (DBusBabysitter, 1);

105 if (sitter == NULL)

106 return NULL;

107

108 old_refcount = \_dbus_atomic_inc (&sitter-\>refcount);

109

110 \_dbus_babysitter_trace_ref (sitter, old_refcount, old_refcount+1, \_DBUS_FUNCTION_NAME);

111

112 sitter-\>child_handle = NULL;

113

114 sitter-\>socket_to_babysitter = sitter-\>socket_to_main = \_dbus_socket_get_invalid ();

115

116 sitter-\>watches = \_dbus_watch_list_new ();

117 if (sitter-\>watches == NULL)

118 {

119 \_dbus_babysitter_unref (sitter);

120 return NULL;

121 }

122

123 sitter-\>have_spawn_errno = FALSE;

124 sitter-\>have_child_status = FALSE;

125

126 return sitter;

127}

128

135DBusBabysitter \*

136\_dbus_babysitter_ref (DBusBabysitter \*sitter)

137{

138 dbus_int32_t old_refcount;

139 PING();

140 \_dbus_assert (sitter != NULL);

141

142 old_refcount = \_dbus_atomic_inc (&sitter-\>refcount);

143 \_dbus_assert (old_refcount \> 0);

144 \_dbus_babysitter_trace_ref (sitter, old_refcount, old_refcount+1, \_DBUS_FUNCTION_NAME);

145

146 return sitter;

147}

148

149static void

150close_socket_to_babysitter (DBusBabysitter \*sitter)

151{

152 \_dbus_verbose ("Closing babysitter\n");

153

154 if (sitter-\>sitter_watch != NULL)

155 {

156 \_dbus_assert (sitter-\>watches != NULL);

157 \_dbus_watch_list_remove_watch (sitter-\>watches, sitter-\>sitter_watch);

158 \_dbus_watch_invalidate (sitter-\>sitter_watch);

159 \_dbus_watch_unref (sitter-\>sitter_watch);

160 sitter-\>sitter_watch = NULL;

161 }

162

163 if (sitter-\>socket_to_babysitter.sock != INVALID_SOCKET)

164 {

165 \_dbus_close_socket (&sitter-\>socket_to_babysitter, NULL);

166 sitter-\>socket_to_babysitter.sock = INVALID_SOCKET;

167 }

168}

169

175void

176\_dbus_babysitter_unref (DBusBabysitter \*sitter)

177{

178 dbus_int32_t old_refcount;

179

180 PING();

181 \_dbus_assert (sitter != NULL);

182

183 old_refcount = \_dbus_atomic_dec (&sitter-\>refcount);

184 \_dbus_assert (old_refcount \> 0);

185 \_dbus_babysitter_trace_ref (sitter, old_refcount, old_refcount-1, \_DBUS_FUNCTION_NAME);

186

187 if (old_refcount == 1)

188 {

189 close_socket_to_babysitter (sitter);

190

191 if (sitter-\>socket_to_main.sock != INVALID_SOCKET)

192 {

193 \_dbus_close_socket (&sitter-\>socket_to_main, NULL);

194 sitter-\>socket_to_main.sock = INVALID_SOCKET;

195 }

196

197 if (sitter-\>child_handle != NULL)

198 {

199 CloseHandle (sitter-\>child_handle);

200 sitter-\>child_handle = NULL;

201 }

202

203 if (sitter-\>sitter_watch)

204 {

205 \_dbus_watch_invalidate (sitter-\>sitter_watch);

206 \_dbus_watch_unref (sitter-\>sitter_watch);

207 sitter-\>sitter_watch = NULL;

208 }

209

210 if (sitter-\>watches)

211 \_dbus_watch_list_free (sitter-\>watches);

212

213 if (sitter-\>thread_handle)

214 {

215 CloseHandle (sitter-\>thread_handle);

216 sitter-\>thread_handle = NULL;

217 }

218

219 dbus_free (sitter-\>log_name);

220

221 dbus_free (sitter);

222 }

223}

224

225void

226\_dbus_babysitter_kill_child (DBusBabysitter \*sitter)

227{

228 PING();

229 if (sitter-\>child_handle == NULL)

230 return; /\* child is already dead, or we're so hosed we'll never recover \*/

231

232 PING();

233 TerminateProcess (sitter-\>child_handle, 12345);

234}

235

241dbus_bool_t

242\_dbus_babysitter_get_child_exited (DBusBabysitter \*sitter)

243{

244 PING();

245 return (sitter-\>child_handle == NULL);

246}

247

260dbus_bool_t

261\_dbus_babysitter_get_child_exit_status (DBusBabysitter \*sitter,

262 int \*status)

263{

264 if (!\_dbus_babysitter_get_child_exited (sitter))

265 \_dbus_assert_not_reached ("Child has not exited");

266

267 if (!sitter-\>have_child_status \|\|

268 sitter-\>child_status == STILL_ACTIVE)

269 return FALSE;

270

271 \*status = sitter-\>child_status;

272 return TRUE;

273}

274

284void

285\_dbus_babysitter_set_child_exit_error (DBusBabysitter \*sitter,

286 DBusError \*error)

287{

288 PING();

289 if (!\_dbus_babysitter_get_child_exited (sitter))

290 return;

291

292 PING();

293 if (sitter-\>have_spawn_errno)

294 {

295 char \*emsg = \_dbus_win_error_string (sitter-\>spawn_errno);

296 dbus_set_error (error, DBUS_ERROR_SPAWN_EXEC_FAILED,

297 "Failed to execute program %s: %s",

298 sitter-\>log_name, emsg);

299 \_dbus_win_free_error_string (emsg);

300 }

301 else if (sitter-\>have_child_status)

302 {

303 PING();

304 dbus_set_error (error, DBUS_ERROR_SPAWN_CHILD_EXITED,

305 "Process %s exited with status %d",

306 sitter-\>log_name, sitter-\>child_status);

307 }

308 else

309 {

310 PING();

311 dbus_set_error (error, DBUS_ERROR_FAILED,

312 "Process %s exited, status unknown",

313 sitter-\>log_name);

314 }

315 PING();

316}

317

318dbus_bool_t

319\_dbus_babysitter_set_watch_functions (DBusBabysitter \*sitter,

320 DBusAddWatchFunction add_function,

321 DBusRemoveWatchFunction remove_function,

322 DBusWatchToggledFunction toggled_function,

323 void \*data,

324 DBusFreeFunction free_data_function)

325{

326 PING();

327 return \_dbus_watch_list_set_functions (sitter-\>watches,

328 add_function,

329 remove_function,

330 toggled_function,

331 data,

332 free_data_function);

333}

334

335static dbus_bool_t

336handle_watch (DBusWatch \*watch,

337 unsigned int condition,

338 void \*data)

339{

340 DBusBabysitter \*sitter = data;

341

342 /\* On Unix dbus-spawn uses a babysitter \*process\*, thus it has to

343 \* actually send the exit statuses, error codes and whatnot through

344 \* sockets and/or pipes. On Win32, the babysitter is jus a thread,

345 \* so it can set the status fields directly in the babysitter struct

346 \* just fine. The socket pipe is used just so we can watch it with

347 \* select(), as soon as anything is written to it we know that the

348 \* babysitter thread has recorded the status in the babysitter

349 \* struct.

350 \*/

351

352 PING();

353 close_socket_to_babysitter (sitter);

354 PING();

355

356 if (\_dbus_babysitter_get_child_exited (sitter) &&

357 sitter-\>finished_cb != NULL)

358 {

359 sitter-\>finished_cb (sitter, sitter-\>finished_data);

360 sitter-\>finished_cb = NULL;

361 }

362

363 return TRUE;

364}

365

366/\* protect_argv lifted from GLib, relicensed by author, Tor Lillqvist \*/

367static int

368protect_argv (char \* const \*argv,

369 char \*\*\*new_argv)

370{

371 int i;

372 int argc = 0;

373 char \*\*args = NULL;

374

375 while (argv\[argc\])

376 ++argc;

377 args = dbus_malloc ((argc + 1) \* sizeof (char \*));

378 if (args == NULL)

379 return -1;

380

381 for (i = 0; i \< argc; i++)

382 (args)\[i\] = NULL;

383

384 /\* Quote each argv element if necessary, so that it will get

385 \* reconstructed correctly in the C runtime startup code. Note that

386 \* the unquoting algorithm in the C runtime is really weird, and

387 \* rather different than what Unix shells do. See stdargv.c in the C

388 \* runtime sources (in the Platform SDK, in src/crt).

389 \*

390 \* Note that an new_argv\[0\] constructed by this function should

391 \* \*not\* be passed as the filename argument to a spawn\* or exec\*

392 \* family function. That argument should be the real file name

393 \* without any quoting.

394 \*/

395 for (i = 0; i \< argc; i++)

396 {

397 const char \*p = argv\[i\];

398 char \*q;

399 int len = 0;

400 int need_dblquotes = FALSE;

401 while (\*p)

402 {

403 if (\*p == ' ' \|\| \*p == '\t')

404 need_dblquotes = TRUE;

405 else if (\*p == '"')

406 len++;

407 else if (\*p == '\\')

408 {

409 const char \*pp = p;

410 while (\*pp && \*pp == '\\')

411 pp++;

412 if (\*pp == '"')

413 len++;

414 }

415 len++;

416 p++;

417 }

418

419 q = args\[i\] = dbus_malloc (len + need_dblquotes\*2 + 1);

420

421 if (q == NULL)

422 {

423 dbus_free_string_array (args);

424 return -1;

425 }

426

427 p = argv\[i\];

428

429 if (need_dblquotes)

430 \*q++ = '"';

431

432 while (\*p)

433 {

434 if (\*p == '"')

435 \*q++ = '\\';

436 else if (\*p == '\\')

437 {

438 const char \*pp = p;

439 while (\*pp && \*pp == '\\')

440 pp++;

441 if (\*pp == '"')

442 \*q++ = '\\';

443 }

444 \*q++ = \*p;

445 p++;

446 }

447

448 if (need_dblquotes)

449 \*q++ = '"';

450 \*q++ = '\0';

451 /\* printf ("argv\[%d\]:%s, need_dblquotes:%s len:%d =\> %s\n", i, argv\[i\], need_dblquotes?"TRUE":"FALSE", len, (args)\[i\]); \*/

452 }

453 args\[argc\] = NULL;

454 \*new_argv = args;

455

456 return argc;

457}

458

459static dbus_bool_t

460build_commandline (char \*\*argv, DBusString \*result)

461{

462 return \_dbus_string_append_strings (result, argv, ' ');

463}

464

465static dbus_bool_t

466build_env_block (char\*\* envp, DBusString \*result)

467{

468 if (!\_dbus_string_append_strings (result, envp, '\0'))

469 return FALSE;

470

471 /\* We need a double \`\0\` to terminate the environment block.

472 \* DBusString provides one \`\0\` after the length-counted data,

473 \* so add one more. \*/

474 if (!\_dbus_string_append_byte (result, '\0'))

475 return FALSE;

476

477 return TRUE;

478}

479

491HANDLE

492\_dbus_spawn_program (const char \*name,

493 char \*\*argv,

494 char \*\*envp,

495 dbus_bool_t inherit_handles,

496 DBusError \*error)

497{

498 PROCESS_INFORMATION pi = { NULL, 0, 0, 0 };

499 STARTUPINFOA si;

500 DBusString arg_string = \_DBUS_STRING_INIT_INVALID;

501 DBusString env_block = \_DBUS_STRING_INIT_INVALID;

502 BOOL result = FALSE;

503 char \*env = NULL;

504

505 if (!\_dbus_string_init (&arg_string) \|\| !\_dbus_string_init (&env_block))

506 {

507 \_DBUS_SET_OOM (error);

508 goto out;

509 }

510

511\#ifdef DBUS_WINCE

512 if (argv && argv\[0\])

513 {

514 if (!build_commandline (argv + 1, &arg_string))

515 \_DBUS_SET_OOM (error);

516 goto out;

517 }

518\#else

519 if (!build_commandline (argv, &arg_string))

520 {

521 \_DBUS_SET_OOM (error);

522 goto out;

523 }

524\#endif

525 if (\_dbus_string_get_length (&arg_string) == 0)

526 {

527 dbus_set_error (error, DBUS_ERROR_FAILED, "No arguments given to start '%s'", name);

528 goto out;

529 }

530

531 if (envp != NULL)

532 {

533 if (!build_env_block (envp, &env_block))

534 {

535 \_DBUS_SET_OOM (error);

536 goto out;

537 }

538 /\* env_block consists of '0' terminated strings \*/

539 env = \_dbus_string_get_data (&env_block);

540 }

541

542 memset (&si, 0, sizeof (si));

543 si.cb = sizeof (si);

544

545\#ifdef DBUS_ENABLE_VERBOSE_MODE

546 {

547 DBusString temp = \_DBUS_STRING_INIT_INVALID;

548

549 if (!\_dbus_string_init (&temp))

550 {

551 \_DBUS_SET_OOM (error);

552 goto out;

553 }

554

555 if (!\_dbus_string_append_strings (&temp, envp, ';'))

556 {

557 \_dbus_string_free (&temp);

558 \_DBUS_SET_OOM (error);

559 goto out;

560 }

561

562 \_dbus_verbose ("spawning '%s'' with args: '%s' env: '%s'\n", name,

563 \_dbus_string_get_const_data (&arg_string),

564 \_dbus_string_get_const_data (&temp));

565 \_dbus_string_free (&temp);

566 }

567\#endif

568

569\#ifdef DBUS_WINCE

570 result = CreateProcessA (name, \_dbus_string_get_const_data (&arg_string), NULL, NULL, FALSE, 0,

571\#else

572 result = CreateProcessA (NULL, /\* no application name \*/

573 \_dbus_string_get_data (&arg_string),

574 NULL, /\* no process attributes \*/

575 NULL, /\* no thread attributes \*/

576 inherit_handles, /\* inherit handles \*/

577 0, /\* flags \*/

578\#endif

579 env, NULL, &si, &pi);

580 if (!result)

581 {

582 \_dbus_win_set_error_from_last_error (error, "Unable to start '%s' with arguments '%s'",

583 name, \_dbus_string_get_const_data (&arg_string));

584 goto out;

585 }

586

587out:

588 \_DBUS_ASSERT_ERROR_XOR_BOOL (error, result);

589

590 \_dbus_string_free (&arg_string);

591 \_dbus_string_free (&env_block);

592

593 if (result)

594 {

595 CloseHandle (pi.hThread);

596 return pi.hProcess;

597 }

598

599 return NULL;

600}

601

602

603static DWORD \_\_stdcall

604babysitter (void \*parameter)

605{

606 int ret = 0;

607 DBusBabysitter \*sitter = (DBusBabysitter \*) parameter;

608

609 PING();

610 if (sitter-\>child_handle != NULL)

611 {

612 DWORD status;

613

614 PING();

615 // wait until process finished

616 WaitForSingleObject (sitter-\>child_handle, INFINITE);

617

618 PING();

619 ret = GetExitCodeProcess (sitter-\>child_handle, &status);

620 if (ret)

621 {

622 sitter-\>child_status = status;

623 sitter-\>have_child_status = TRUE;

624 }

625

626 CloseHandle (sitter-\>child_handle);

627 sitter-\>child_handle = NULL;

628 }

629

630 PING();

631 send (sitter-\>socket_to_main.sock, " ", 1, 0);

632

633 \_dbus_babysitter_unref (sitter);

634

635 return ret ? 0 : 1;

636}

637

638dbus_bool_t

639\_dbus_spawn_async_with_babysitter (DBusBabysitter \*\*sitter_p,

640 const char \*log_name,

641 char \* const \*argv,

642 char \* const \*envp,

643 DBusSpawnFlags flags \_DBUS_GNUC_UNUSED,

644 DBusSpawnChildSetupFunc child_setup \_DBUS_GNUC_UNUSED,

645 void \*user_data \_DBUS_GNUC_UNUSED,

646 DBusError \*error)

647{

648 DBusBabysitter \*sitter;

649 DWORD sitter_thread_id;

650 HANDLE handle;

651 int argc;

652 char \*\*my_argv = NULL;

653 DBusError local_error = DBUS_ERROR_INIT;

654

655 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

656 \_dbus_assert (argv\[0\] != NULL);

657

658 if (sitter_p != NULL)

659 \*sitter_p = NULL;

660

661 PING();

662 sitter = \_dbus_babysitter_new ();

663 if (sitter == NULL)

664 {

665 \_DBUS_SET_OOM (error);

666 return FALSE;

667 }

668

669 sitter-\>log_name = \_dbus_strdup (log_name);

670 if (sitter-\>log_name == NULL && log_name != NULL)

671 {

672 \_DBUS_SET_OOM (error);

673 goto out0;

674 }

675

676 if (sitter-\>log_name == NULL)

677 sitter-\>log_name = \_dbus_strdup (argv\[0\]);

678

679 if (sitter-\>log_name == NULL)

680 {

681 \_DBUS_SET_OOM (error);

682 goto out0;

683 }

684

685 PING();

686 if (!\_dbus_socketpair (&sitter-\>socket_to_babysitter,

687 &sitter-\>socket_to_main,

688 FALSE, error))

689 goto out0;

690

691 sitter-\>sitter_watch = \_dbus_watch_new (sitter-\>socket_to_babysitter,

692 DBUS_WATCH_READABLE,

693 TRUE, handle_watch, sitter, NULL);

694 PING();

695 if (sitter-\>sitter_watch == NULL)

696 {

697 \_DBUS_SET_OOM (error);

698 goto out0;

699 }

700

701 PING();

702 if (!\_dbus_watch_list_add_watch (sitter-\>watches, sitter-\>sitter_watch))

703 {

704 /\* we need to free it early so the destructor won't try to remove it

705 \* without it having been added, which DBusLoop doesn't allow \*/

706 \_dbus_watch_invalidate (sitter-\>sitter_watch);

707 \_dbus_watch_unref (sitter-\>sitter_watch);

708 sitter-\>sitter_watch = NULL;

709

710 \_DBUS_SET_OOM (error);

711 goto out0;

712 }

713

714 argc = protect_argv (argv, &my_argv);

715 if (argc == -1)

716 {

717 \_DBUS_SET_OOM (error);

718 goto out0;

719 }

720

721 \_dbus_verbose ("babysitter: spawn child '%s'\n", my_argv\[0\]);

722

723 PING();

724 handle = \_dbus_spawn_program (sitter-\>log_name, my_argv, (char \*\*) envp, FALSE, &local_error);

725

726 if (my_argv != NULL)

727 {

728 dbus_free_string_array (my_argv);

729 }

730

731 PING();

732 if (handle == NULL)

733 {

734 if (dbus_error_has_name (&local_error, DBUS_ERROR_NO_MEMORY))

735 {

736 sitter-\>child_handle = NULL;

737 sitter-\>have_spawn_errno = TRUE;

738 sitter-\>spawn_errno = ERROR_NOT_ENOUGH_MEMORY;

739 dbus_move_error (&local_error, error);

740 }

741 else

742 {

743 sitter-\>child_handle = NULL;

744 sitter-\>have_spawn_errno = TRUE;

745 sitter-\>spawn_errno = GetLastError();

746 dbus_set_error (error, DBUS_ERROR_SPAWN_EXEC_FAILED,

747 "Failed to spawn child: %s", local_error.message);

748 }

749 dbus_error_free (&local_error);

750 goto out0;

751 }

752 else

753 dbus_error_free (&local_error);

754

755 sitter-\>child_handle = handle;

756

757 PING();

758 sitter-\>thread_handle = (HANDLE) CreateThread (NULL, 0, babysitter,

759 \_dbus_babysitter_ref (sitter), 0, &sitter_thread_id);

760

761 if (sitter-\>thread_handle == NULL)

762 {

763 PING();

764 dbus_set_error_const (error, DBUS_ERROR_SPAWN_FORK_FAILED,

765 "Failed to create new thread");

766 goto out0;

767 }

768

769 PING();

770 if (sitter_p != NULL)

771 \*sitter_p = sitter;

772 else

773 \_dbus_babysitter_unref (sitter);

774

775 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

776

777 PING();

778 return TRUE;

779

780out0:

781 \_dbus_babysitter_unref (sitter);

782

783 return FALSE;

784}

785

786void

787\_dbus_babysitter_set_result_function (DBusBabysitter \*sitter,

788 DBusBabysitterFinishedFunc finished,

789 void \*user_data)

790{

791 sitter-\>finished_cb = finished;

792 sitter-\>finished_data = user_data;

793}

794

795\#define LIVE_CHILDREN(sitter) ((sitter)-\>child_handle != NULL)

796

797void

798\_dbus_babysitter_block_for_child_exit (DBusBabysitter \*sitter)

799{

800 /\* The thread terminates after the child does. We want to wait for the thread,

801 \* not just the child, to avoid data races and ensure that it has freed all

802 \* its memory. \*/

803 WaitForSingleObject (sitter-\>thread_handle, INFINITE);

804}

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

dbus_error_has_name

dbus_bool_t dbus_error_has_name(const DBusError \*error, const char \*name)

Checks whether the error is set and has the given name.

**Definition** dbus-errors.c:304

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

**Definition** dbus-spawn-win.c:261

\_dbus_babysitter_unref

void \_dbus_babysitter_unref(DBusBabysitter \*sitter)

Decrement the reference count on the babysitter object.

**Definition** dbus-spawn-win.c:176

\_dbus_babysitter_get_child_exited

dbus_bool_t \_dbus_babysitter_get_child_exited(DBusBabysitter \*sitter)

Checks whether the child has exited, without blocking.

**Definition** dbus-spawn-win.c:242

\_dbus_babysitter_set_watch_functions

dbus_bool_t \_dbus_babysitter_set_watch_functions(DBusBabysitter \*sitter, DBusAddWatchFunction add_function, DBusRemoveWatchFunction remove_function, DBusWatchToggledFunction toggled_function, void \*data, DBusFreeFunction free_data_function)

Sets watch functions to notify us when the babysitter object needs to read/write file descriptors.

**Definition** dbus-spawn-win.c:319

\_dbus_strdup

char \* \_dbus_strdup(const char \*str)

Duplicates a string.

**Definition** dbus-internals.c:621

\_dbus_babysitter_set_child_exit_error

void \_dbus_babysitter_set_child_exit_error(DBusBabysitter \*sitter, DBusError \*error)

Sets the DBusError with an explanation of why the spawned child process exited (on a signal,...

**Definition** dbus-spawn-win.c:285

\_dbus_babysitter_kill_child

void \_dbus_babysitter_kill_child(DBusBabysitter \*sitter)

Blocks until the babysitter process gives us the PID of the spawned grandchild, then kills the spawne...

**Definition** dbus-spawn-win.c:226

\_dbus_babysitter_ref

DBusBabysitter \* \_dbus_babysitter_ref(DBusBabysitter \*sitter)

Increment the reference count on the babysitter object.

**Definition** dbus-spawn-win.c:136

\_dbus_spawn_async_with_babysitter

dbus_bool_t \_dbus_spawn_async_with_babysitter(DBusBabysitter \*\*sitter_p, const char \*log_name, char \*const \*argv, char \*const \*env, DBusSpawnFlags flags, DBusSpawnChildSetupFunc child_setup, void \*user_data, DBusError \*error)

Spawns a new process.

**Definition** dbus-spawn-unix.c:1279

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

dbus_free_string_array

void dbus_free_string_array(char \*\*str_array)

Frees a NULL-terminated array of strings.

**Definition** dbus-memory.c:758

dbus_malloc

void \* dbus_malloc(size_t bytes)

Allocates the given number of bytes, as with standard malloc().

**Definition** dbus-memory.c:470

DBUS_ERROR_SPAWN_CHILD_EXITED

\#define DBUS_ERROR_SPAWN_CHILD_EXITED

While starting a new process, the child exited with a status code.

**Definition** dbus-protocol.h:426

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

DBUS_ERROR_SPAWN_FORK_FAILED

\#define DBUS_ERROR_SPAWN_FORK_FAILED

While starting a new process, the fork() call failed.

**Definition** dbus-protocol.h:424

\_dbus_string_init

dbus_bool_t \_dbus_string_init(DBusString \*str)

Initializes a string.

**Definition** dbus-string.c:182

\_dbus_string_append_strings

dbus_bool_t \_dbus_string_append_strings(DBusString \*str, char \*\*strings, char separator)

Append vector with strings connected by separator.

**Definition** dbus-string.c:1213

\_dbus_string_get_data

char \* \_dbus_string_get_data(DBusString \*str)

Gets the raw character buffer from the string.

**Definition** dbus-string.c:496

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_string_get_length

int \_dbus_string_get_length(const DBusString \*str)

Gets the length of a string (not including nul termination).

**Definition** dbus-string.c:784

\_dbus_string_append_byte

dbus_bool_t \_dbus_string_append_byte(DBusString \*str, unsigned char byte)

Appends a single byte to the string, returning FALSE if not enough memory.

**Definition** dbus-string.c:1190

\_dbus_string_get_const_data

const char \* \_dbus_string_get_const_data(const DBusString \*str)

Gets the raw character buffer from a const string.

**Definition** dbus-string.c:513

\_dbus_socketpair

dbus_bool_t \_dbus_socketpair(DBusSocket \*fd1, DBusSocket \*fd2, dbus_bool_t blocking, DBusError \*error)

Creates pair of connect sockets (as in socketpair()).

**Definition** dbus-sysdeps-unix.c:3884

\_dbus_atomic_dec

dbus_int32_t \_dbus_atomic_dec(DBusAtomic \*atomic)

Atomically decrement an integer.

**Definition** dbus-sysdeps-unix.c:3205

\_dbus_close_socket

dbus_bool_t \_dbus_close_socket(DBusSocket \*fd, DBusError \*error)

Closes a socket and invalidates it.

**Definition** dbus-sysdeps-unix.c:314

\_dbus_atomic_inc

dbus_int32_t \_dbus_atomic_inc(DBusAtomic \*atomic)

Atomically increments an integer.

**Definition** dbus-sysdeps-unix.c:3178

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

DBusAtomic

An atomic integer safe to increment or decrement from multiple threads.

**Definition** dbus-sysdeps.h:340

DBusBabysitter

Babysitter implementation details.

**Definition** dbus-spawn-unix.c:252

DBusBabysitter::sitter_watch

DBusWatch \* sitter_watch

Sitter pipe watch.

**Definition** dbus-spawn-unix.c:267

DBusBabysitter::socket_to_babysitter

DBusSocket socket_to_babysitter

Connection to the babysitter process.

**Definition** dbus-spawn-unix.c:258

DBusBabysitter::have_child_status

unsigned int have_child_status

True if child status has been reaped.

**Definition** dbus-spawn-unix.c:274

DBusBabysitter::log_name

char \* log_name

the name under which to log messages about this process being spawned

**Definition** dbus-spawn-unix.c:255

DBusBabysitter::refcount

int refcount

Reference count.

**Definition** dbus-spawn-unix.c:253

DBusBabysitter::watches

DBusWatchList \* watches

Watches.

**Definition** dbus-spawn-unix.c:264

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusError::message

const char \* message

public error message field

**Definition** dbus-errors.h:53

DBusSocket

Socket interface.

**Definition** dbus-sysdeps.h:185

DBusString

**Definition** dbus-string.h:47

DBusWatchList

DBusWatchList implementation details.

**Definition** dbus-watch.c:217

DBusWatch

Implementation of DBusWatch.

**Definition** dbus-watch.c:43
