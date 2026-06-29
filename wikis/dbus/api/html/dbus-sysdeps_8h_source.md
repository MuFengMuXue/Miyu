dbus-sysdeps.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-sysdeps.h Wrappers around system/libc features (internal to D-Bus implementation)

3 \*

4 \* Copyright (C) 2002, 2003 Red Hat, Inc.

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

27\#ifndef DBUS_SYSDEPS_H

28\#define DBUS_SYSDEPS_H

29

30\#ifndef VERSION

31\#warning Please include config.h before dbus-sysdeps.h

32\#include "config.h"

33\#endif

34

35\#include \<stdint.h\>

36

37\#ifdef HAVE_INTTYPES_H

38\#include \<inttypes.h\>

39\#endif

40

41\#ifdef HAVE_STDATOMIC_H

42\#include \<stdatomic.h\>

43\#endif

44

45\#include \<dbus/dbus-errors.h\>

46\#include \<dbus/dbus-file.h\>

47\#include \<dbus/dbus-string.h\>

48

49/\* this is perhaps bogus, but strcmp() etc. are faster if we use the

50 \* stuff straight out of string.h, so have this here for now.

51 \*/

52\#include \<string.h\>

53\#include \<stdarg.h\>

54

55\#if !defined(BROKEN_POLL) && (defined(\_\_APPLE\_\_) \|\| defined(\_\_INTERIX))

56 /\* Following libcurl's example, we blacklist poll() on Darwin

57 \* (macOS, iOS, etc.) and Interix due to a history of implementation

58 \* issues.

59 \* https://github.com/curl/curl/blob/master/m4/curl-functions.m4

60 \*

61 \* On unspecified older macOS versions, poll() failed if given a

62 \* device node to poll.

63 \*

64 \* On macOS \< 10.9, poll() with nfds=0 failed instead of waiting for

65 \* the timeout and then succeeding.

66 \*

67 \* On macOS \>= 10.12, poll() with nfds=0 succeeded immediately

68 \* instead of waiting for the timeout, resulting in busy-looping.

69 \*

70 \* On Interix, poll() apparently only works for files in /proc.

71 \*

72 \* The "legacy" build flavour in our CI machinery defines BROKEN_POLL

73 \* on whatever platform is in use (normally Linux) to force use of the

74 \* same select()-based poll() emulation that we use for macOS, Interix,

75 \* and any platform that lacks a real poll(), so that we can test it

76 \* more regularly.

77 \*/

78\# define BROKEN_POLL

79\#endif

80

81/\* Normally we'd only include this in dbus-sysdeps-unix.c.

82 \* However, the member names in DBusPollFD are (deliberately) the same as

83 \* in POSIX struct pollfd, and AIX's poll() implementation is known to

84 \* do things like "#define events reqevents", which would break that approach.

85 \* Defend against that by ensuring that if it's renamed anywhere, it's renamed

86 \* everywhere.

87 \*/

88\#ifdef HAVE_POLL

89\#include \<poll.h\>

90\#endif

91

92\#ifdef DBUS_WINCE

93/\* Windows CE lacks some system functions (such as errno and clock).

94 We bring them in here. \*/

95\#include "dbus-sysdeps-wince-glue.h"

96\#endif

97

98\#ifdef DBUS_WIN

99\#include \<ws2tcpip.h\>

100\#endif

101

102DBUS_BEGIN_DECLS

103

104\#ifdef DBUS_WIN

105\#define \_DBUS_PATH_SEPARATOR ";"

106\#else

107\#define \_DBUS_PATH_SEPARATOR ":"

108\#endif

109

110/\* Forward declarations \*/

111

112

114typedef struct DBusList DBusList;

115

117typedef struct DBusCredentials DBusCredentials;

118

120typedef struct DBusPipe DBusPipe;

121

128DBUS_PRIVATE_EXPORT

129void \_dbus_abort (void) \_DBUS_GNUC_NORETURN;

130

131dbus_bool_t \_dbus_check_setuid (void);

132DBUS_PRIVATE_EXPORT

133const char\* \_dbus_getenv (const char \*varname);

134DBUS_PRIVATE_EXPORT

135dbus_bool_t \_dbus_clearenv (void);

136char \*\* \_dbus_get_environment (void);

137

139typedef unsigned long dbus_pid_t;

141typedef unsigned long dbus_uid_t;

143typedef unsigned long dbus_gid_t;

144

146\#define DBUS_PID_UNSET ((dbus_pid_t) -1)

148\#define DBUS_UID_UNSET ((dbus_uid_t) -1)

150\#define DBUS_GID_UNSET ((dbus_gid_t) -1)

151

153\#define DBUS_PID_FORMAT "%lu"

155\#define DBUS_UID_FORMAT "%lu"

157\#define DBUS_GID_FORMAT "%lu"

158

162\#ifdef DBUS_WIN

163

164typedef struct { SOCKET sock; } DBusSocket;

165\# define DBUS_SOCKET_FORMAT "Iu"

166\# define DBUS_SOCKET_INIT { INVALID_SOCKET }

167

168\_DBUS_WARN_UNUSED_RESULT

169static inline SOCKET

170\_dbus_socket_printable (DBusSocket s) { return s.sock; }

171

172\_DBUS_WARN_UNUSED_RESULT

173static inline dbus_bool_t

174\_dbus_socket_is_valid (DBusSocket s) { return s.sock != INVALID_SOCKET; }

175

176static inline void

177\_dbus_socket_invalidate (DBusSocket \*s) { s-\>sock = INVALID_SOCKET; }

178

179\_DBUS_WARN_UNUSED_RESULT

180static inline int

181\_dbus_socket_get_int (DBusSocket s) { return (int)s.sock; }

182

183\#else /\* not DBUS_WIN \*/

184

185typedef struct { int fd; } DBusSocket;

186\# define DBUS_SOCKET_FORMAT "d"

187\# define DBUS_SOCKET_INIT { -1 }

188

189\_DBUS_WARN_UNUSED_RESULT

190static inline int

191\_dbus_socket_printable (DBusSocket s) { return s.fd; }

192

193\_DBUS_WARN_UNUSED_RESULT

194static inline dbus_bool_t

195\_dbus_socket_is_valid (DBusSocket s) { return s.fd \>= 0; }

196

197static inline void

198\_dbus_socket_invalidate (DBusSocket \*s) { s-\>fd = -1; }

199

200\_DBUS_WARN_UNUSED_RESULT

201static inline int

202\_dbus_socket_get_int (DBusSocket s) { return s.fd; }

203

204\#endif /\* not DBUS_WIN \*/

205

206\_DBUS_WARN_UNUSED_RESULT

207static inline DBusSocket

208\_dbus_socket_get_invalid (void)

209{

210 DBusSocket s = DBUS_SOCKET_INIT;

211

212 return s;

213}

214

215dbus_bool_t \_dbus_set_socket_nonblocking (DBusSocket fd,

216 DBusError \*error);

217

218DBUS_PRIVATE_EXPORT

219dbus_bool_t \_dbus_close_socket (DBusSocket \*fd,

220 DBusError \*error);

221DBUS_PRIVATE_EXPORT

222int \_dbus_read_socket (DBusSocket fd,

223 DBusString \*buffer,

224 int count);

225DBUS_PRIVATE_EXPORT

226int \_dbus_write_socket (DBusSocket fd,

227 const DBusString \*buffer,

228 int start,

229 int len);

230int \_dbus_write_socket_two (DBusSocket fd,

231 const DBusString \*buffer1,

232 int start1,

233 int len1,

234 const DBusString \*buffer2,

235 int start2,

236 int len2);

237

238int \_dbus_read_socket_with_unix_fds (DBusSocket fd,

239 DBusString \*buffer,

240 int count,

241 int \*fds,

242 unsigned int \*n_fds);

243DBUS_PRIVATE_EXPORT

244int \_dbus_write_socket_with_unix_fds (DBusSocket fd,

245 const DBusString \*buffer,

246 int start,

247 int len,

248 const int \*fds,

249 int n_fds);

250int \_dbus_write_socket_with_unix_fds_two (DBusSocket fd,

251 const DBusString \*buffer1,

252 int start1,

253 int len1,

254 const DBusString \*buffer2,

255 int start2,

256 int len2,

257 const int \*fds,

258 int n_fds);

259

260DBusSocket \_dbus_connect_tcp_socket (const char \*host,

261 const char \*port,

262 const char \*family,

263 DBusError \*error);

264DBusSocket \_dbus_connect_tcp_socket_with_nonce (const char \*host,

265 const char \*port,

266 const char \*family,

267 const char \*noncefile,

268 DBusError \*error);

269int \_dbus_listen_tcp_socket (const char \*host,

270 const char \*port,

271 const char \*family,

272 DBusString \*retport,

273 const char \*\*retfamily,

274 DBusSocket \*\*fds_p,

275 DBusError \*error);

276DBusSocket \_dbus_accept (DBusSocket listen_fd);

277

278dbus_bool_t \_dbus_read_credentials_socket (DBusSocket client_fd,

279 DBusCredentials \*credentials,

280 DBusError \*error);

281dbus_bool_t \_dbus_send_credentials_socket (DBusSocket server_fd,

282 DBusError \*error);

283

284typedef enum

285{

286 DBUS_CREDENTIALS_ADD_FLAGS_USER_DATABASE = (1 \<\< 0),

287 DBUS_CREDENTIALS_ADD_FLAGS_NONE = 0

288} DBusCredentialsAddFlags;

289

290dbus_bool_t \_dbus_credentials_add_from_user (DBusCredentials \*credentials,

291 const DBusString \*username,

292 DBusCredentialsAddFlags flags,

293 DBusError \*error);

294

295dbus_bool_t \_dbus_credentials_add_from_current_process (DBusCredentials \*credentials);

296DBUS_PRIVATE_EXPORT

297dbus_bool_t \_dbus_append_user_from_current_process (DBusString \*str);

298

299dbus_bool_t \_dbus_parse_unix_user_from_config (const DBusString \*username,

300 dbus_uid_t \*uid_p);

301dbus_bool_t \_dbus_parse_unix_group_from_config (const DBusString \*groupname,

302 dbus_gid_t \*gid_p);

303dbus_bool_t \_dbus_unix_groups_from_uid (dbus_uid_t uid,

304 dbus_gid_t \*\*group_ids,

305 int \*n_group_ids,

306 DBusError \*error);

307dbus_bool_t \_dbus_unix_user_is_at_console (dbus_uid_t uid,

308 DBusError \*error);

309dbus_bool_t \_dbus_unix_user_is_process_owner (dbus_uid_t uid);

310dbus_bool_t \_dbus_windows_user_is_process_owner (const char \*windows_sid);

311

312dbus_bool_t \_dbus_append_keyring_directory_for_credentials (DBusString \*directory,

313 DBusCredentials \*credentials);

314

315dbus_bool_t \_dbus_daemon_unpublish_session_bus_address (void);

316

317dbus_bool_t \_dbus_socket_can_pass_unix_fd(DBusSocket fd);

318

319/\* PID FDs are Linux-specific. \*/

320\#ifdef DBUS_WIN

321static inline dbus_pid_t \_dbus_resolve_pid_fd (int pid_fd)

322{

323 return DBUS_PID_UNSET;

324}

325

326\#else

327DBUS_PRIVATE_EXPORT

328dbus_pid_t \_dbus_resolve_pid_fd (int pid_fd);

329\#endif

330

334typedef struct DBusAtomic DBusAtomic;

335

339struct DBusAtomic

340{

341\#ifdef HAVE_STDATOMIC_H

342 atomic_int value;

343\#elif defined(DBUS_WIN)

344 volatile long value;

345\#else

346 volatile dbus_int32_t value;

347\#endif

348};

349

350DBUS_PRIVATE_EXPORT

351dbus_int32_t \_dbus_atomic_inc (DBusAtomic \*atomic);

352DBUS_PRIVATE_EXPORT

353dbus_int32_t \_dbus_atomic_dec (DBusAtomic \*atomic);

354DBUS_PRIVATE_EXPORT

355dbus_int32_t \_dbus_atomic_get (DBusAtomic \*atomic);

356DBUS_PRIVATE_EXPORT

357void \_dbus_atomic_set_zero (DBusAtomic \*atomic);

358DBUS_PRIVATE_EXPORT

359void \_dbus_atomic_set_nonzero (DBusAtomic \*atomic);

360

361\#ifdef DBUS_WIN

362

363/\* On Windows, you can only poll sockets. We emulate Unix poll() using

364 \* select(), so it doesn't matter what precise type we put in DBusPollFD;

365 \* use DBusSocket so that the compiler can check we are doing it right.

366 \*/

367typedef DBusSocket DBusPollable;

368\# define DBUS_POLLABLE_FORMAT "Iu"

369

370static inline DBusPollable

371\_dbus_socket_get_pollable (DBusSocket s) { return s; }

372

373static inline SOCKET

374\_dbus_pollable_printable (DBusPollable p) { return p.sock; }

375

376static inline dbus_bool_t

377\_dbus_pollable_is_valid (DBusPollable p) { return \_dbus_socket_is_valid (p); }

378

379static inline void

380\_dbus_pollable_invalidate (DBusPollable \*p) { \_dbus_socket_invalidate (p); }

381

382static inline dbus_bool_t

383\_dbus_pollable_equals (DBusPollable a, DBusPollable b) { return a.sock == b.sock; }

384

385\#else /\* !DBUS_WIN \*/

386

387/\* On Unix, you can poll sockets, pipes, etc., and we must put exactly

388 \* "int" in DBusPollFD because we're relying on its layout exactly matching

389 \* struct pollfd. (This is silly, and one day we should use a better

390 \* abstraction.)

391 \*/

392typedef int DBusPollable;

393\# define DBUS_POLLABLE_FORMAT "d"

394

395static inline DBusPollable

396\_dbus_socket_get_pollable (DBusSocket s) { return s.fd; }

397

398static inline int

399\_dbus_pollable_printable (DBusPollable p) { return p; }

400

401static inline dbus_bool_t

402\_dbus_pollable_is_valid (DBusPollable p) { return p \>= 0; }

403

404static inline void

405\_dbus_pollable_invalidate (DBusPollable \*p) { \*p = -1; }

406

407static inline dbus_bool_t

408\_dbus_pollable_equals (DBusPollable a, DBusPollable b) { return a == b; }

409

410\#endif /\* !DBUS_WIN \*/

411

412\#if defined(HAVE_POLL) && !defined(BROKEN_POLL)

417typedef struct pollfd DBusPollFD;

418

420\#define \_DBUS_POLLIN POLLIN

422\#define \_DBUS_POLLPRI POLLPRI

424\#define \_DBUS_POLLOUT POLLOUT

426\#define \_DBUS_POLLERR POLLERR

428\#define \_DBUS_POLLHUP POLLHUP

430\#define \_DBUS_POLLNVAL POLLNVAL

431\#else

432/\* Emulate poll() via select(). Because we aren't really going to call

433 \* poll(), any similarly-shaped struct is acceptable, and any power of 2

434 \* will do for the events/revents; these values happen to match Linux

435 \* and \*BSD. \*/

436typedef struct

437{

438 DBusPollable fd;

439 short events;

440 short revents;

441} DBusPollFD;

442

444\#define \_DBUS_POLLIN 0x0001

446\#define \_DBUS_POLLPRI 0x0002

448\#define \_DBUS_POLLOUT 0x0004

450\#define \_DBUS_POLLERR 0x0008

452\#define \_DBUS_POLLHUP 0x0010

454\#define \_DBUS_POLLNVAL 0x0020

455\#endif

456

457DBUS_PRIVATE_EXPORT

458int \_dbus_poll (DBusPollFD \*fds,

459 int n_fds,

460 int timeout_milliseconds);

461

462DBUS_PRIVATE_EXPORT

463void \_dbus_sleep_milliseconds (int milliseconds);

464

465DBUS_PRIVATE_EXPORT

466void \_dbus_get_monotonic_time (dbus_int64_t \*tv_sec,

467 long \*tv_usec);

468

469DBUS_PRIVATE_EXPORT

470void \_dbus_get_real_time (dbus_int64_t \*tv_sec,

471 long \*tv_usec);

472

476DBUS_PRIVATE_EXPORT

477dbus_bool_t \_dbus_create_directory (const DBusString \*filename,

478 DBusError \*error);

479DBUS_PRIVATE_EXPORT

480dbus_bool_t \_dbus_ensure_directory (const DBusString \*filename,

481 DBusError \*error);

482DBUS_PRIVATE_EXPORT

483dbus_bool_t \_dbus_delete_directory (const DBusString \*filename,

484 DBusError \*error);

485

486DBUS_PRIVATE_EXPORT

487dbus_bool_t \_dbus_concat_dir_and_file (DBusString \*dir,

488 const DBusString \*next_component);

489dbus_bool_t \_dbus_string_get_dirname (const DBusString \*filename,

490 DBusString \*dirname);

491DBUS_PRIVATE_EXPORT

492dbus_bool_t \_dbus_path_is_absolute (const DBusString \*filename);

493

494dbus_bool_t \_dbus_get_standard_session_servicedirs (DBusList \*\*dirs);

495dbus_bool_t \_dbus_get_standard_system_servicedirs (DBusList \*\*dirs);

496dbus_bool_t \_dbus_get_local_system_servicedirs (DBusList \*\*dirs);

497dbus_bool_t \_dbus_set_up_transient_session_servicedirs (DBusList \*\*dirs,

498 DBusError \*error);

499

500dbus_bool_t \_dbus_get_system_config_file (DBusString \*str);

501dbus_bool_t \_dbus_get_session_config_file (DBusString \*str);

502

504typedef struct DBusDirIter DBusDirIter;

505

506DBusDirIter\* \_dbus_directory_open (const DBusString \*filename,

507 DBusError \*error);

508dbus_bool_t \_dbus_directory_get_next_file (DBusDirIter \*iter,

509 DBusString \*filename,

510 DBusError \*error);

511void \_dbus_directory_close (DBusDirIter \*iter);

512

513dbus_bool_t \_dbus_check_dir_is_private_to_user (DBusString \*dir,

514 DBusError \*error);

515

516DBUS_PRIVATE_EXPORT

517const char\* \_dbus_get_tmpdir (void);

518

522\_DBUS_WARN_UNUSED_RESULT

523dbus_bool_t \_dbus_generate_random_bytes_buffer (char \*buffer,

524 int n_bytes,

525 DBusError \*error);

526dbus_bool_t \_dbus_generate_random_bytes (DBusString \*str,

527 int n_bytes,

528 DBusError \*error);

529DBUS_PRIVATE_EXPORT

530dbus_bool_t \_dbus_generate_random_ascii (DBusString \*str,

531 int n_bytes,

532 DBusError \*error);

533

534DBUS_PRIVATE_EXPORT

535const char\* \_dbus_error_from_errno (int error_number);

536DBUS_PRIVATE_EXPORT

537const char\* \_dbus_error_from_system_errno (void);

538

539int \_dbus_get_low_level_socket_errno (void);

540

541int \_dbus_save_socket_errno (void);

542void \_dbus_restore_socket_errno (int saved_errno);

543void \_dbus_set_errno_to_zero (void);

544dbus_bool_t \_dbus_get_is_errno_eagain_or_ewouldblock (int e);

545dbus_bool_t \_dbus_get_is_errno_enomem (int e);

546dbus_bool_t \_dbus_get_is_errno_eintr (int e);

547dbus_bool_t \_dbus_get_is_errno_epipe (int e);

548dbus_bool_t \_dbus_get_is_errno_etoomanyrefs (int e);

549DBUS_PRIVATE_EXPORT

550const char\* \_dbus_strerror_from_errno (void);

551

552void \_dbus_disable_sigpipe (void);

553

554DBUS_PRIVATE_EXPORT

555void \_dbus_exit (int code) \_DBUS_GNUC_NORETURN;

556

557DBUS_PRIVATE_EXPORT

558int \_dbus_printf_string_upper_bound (const char \*format,

559 va_list args) \_DBUS_GNUC_PRINTF (1, 0);

560

561\#ifdef DBUS_ENABLE_VERBOSE_MODE

562DBUS_PRIVATE_EXPORT

563void \_dbus_print_thread (void);

564\#endif

565

569typedef struct

570{

571 unsigned long mode;

572 unsigned long nlink;

573 dbus_uid_t uid;

574 dbus_gid_t gid;

575 unsigned long size;

576 unsigned long atime;

577 unsigned long mtime;

578 unsigned long ctime;

579} DBusStat;

580

581dbus_bool_t \_dbus_stat (const DBusString \*filename,

582 DBusStat \*statbuf,

583 DBusError \*error);

584

585DBusSocket \_dbus_connect_unix_socket (const char \*path,

586 dbus_bool_t abstract,

587 DBusError \*error);

588DBusSocket \_dbus_listen_unix_socket (const char \*path,

589 dbus_bool_t abstract,

590 DBusError \*error);

591

592DBusSocket \_dbus_connect_exec (const char \*path,

593 char \*const argv\[\],

594 DBusError \*error);

595

596DBUS_PRIVATE_EXPORT

597dbus_bool_t \_dbus_socketpair (DBusSocket \*fd1,

598 DBusSocket \*fd2,

599 dbus_bool_t blocking,

600 DBusError \*error);

601

602DBUS_PRIVATE_EXPORT

603void \_dbus_print_backtrace (void);

604

605dbus_bool_t \_dbus_become_daemon (const DBusString \*pidfile,

606 DBusPipe \*print_pid_pipe,

607 DBusError \*error,

608 dbus_bool_t keep_umask);

609

610dbus_bool_t \_dbus_verify_daemon_user (const char \*user);

611dbus_bool_t \_dbus_change_to_daemon_user (const char \*user,

612 DBusError \*error);

613

614dbus_bool_t \_dbus_write_pid_to_file_and_pipe (const DBusString \*pidfile,

615 DBusPipe \*print_pid_pipe,

616 dbus_pid_t pid_to_write,

617 DBusError \*error);

618

619dbus_bool_t \_dbus_command_for_pid (unsigned long pid,

620 DBusString \*str,

621 int max_len,

622 DBusError \*error);

623

624typedef enum {

625 DBUS_LOG_FLAGS_STDERR = (1 \<\< 0),

626 DBUS_LOG_FLAGS_SYSTEM_LOG = (1 \<\< 1)

627} DBusLogFlags;

628

629DBUS_PRIVATE_EXPORT

630void \_dbus_init_system_log (const char \*tag,

631 DBusLogFlags flags);

632

633typedef enum {

634 DBUS_SYSTEM_LOG_INFO,

635 DBUS_SYSTEM_LOG_WARNING,

636 DBUS_SYSTEM_LOG_SECURITY,

637 DBUS_SYSTEM_LOG_ERROR

638} DBusSystemLogSeverity;

639

640DBUS_PRIVATE_EXPORT

641void \_dbus_log (DBusSystemLogSeverity severity,

642 const char \*msg,

643 ...) \_DBUS_GNUC_PRINTF (2, 3);

644DBUS_PRIVATE_EXPORT

645void \_dbus_logv (DBusSystemLogSeverity severity,

646 const char \*msg,

647 va_list args) \_DBUS_GNUC_PRINTF (2, 0);

648

654\#define \_DBUS_DOUBLES_BITWISE_EQUAL(a, b) (memcmp (&(a), &(b), sizeof (double)) == 0)

655

656dbus_bool_t \_dbus_get_autolaunch_address (const char \*scope,

657 DBusString \*address,

658 DBusError \*error);

659

660DBUS_PRIVATE_EXPORT

661dbus_bool_t \_dbus_lookup_session_address (dbus_bool_t \*supported,

662 DBusString \*address,

663 DBusError \*error);

664

668typedef union DBusGUID DBusGUID;

669

670DBUS_PRIVATE_EXPORT

671dbus_bool_t \_dbus_read_local_machine_uuid (DBusGUID \*machine_id,

672 dbus_bool_t create_if_not_found,

673 DBusError \*error);

674

680dbus_bool_t \_dbus_threads_init_platform_specific (void);

681

685void \_dbus_threads_lock_platform_specific (void);

686

690void \_dbus_threads_unlock_platform_specific (void);

691

692DBUS_PRIVATE_EXPORT

693dbus_bool_t \_dbus_split_paths_and_append (DBusString \*dirs,

694 const char \*suffix,

695 DBusList \*\*dir_list);

696

697unsigned long \_dbus_pid_for_log (void);

698

699/\* FIXME move back to dbus-sysdeps-unix.h probably -

700 \* the PID file handling just needs a little more abstraction

701 \* in the bus daemon first.

702 \*/

703DBUS_PRIVATE_EXPORT

704dbus_pid_t \_dbus_getpid (void);

705

706DBUS_PRIVATE_EXPORT

707dbus_uid_t \_dbus_getuid (void);

708

709DBUS_PRIVATE_EXPORT

710void \_dbus_flush_caches (void);

711

712dbus_bool_t \_dbus_replace_install_prefix (DBusString \*path);

713

714/\* Do not set this too high: it is a denial-of-service risk.

715 \* See \<https://bugs.freedesktop.org/show_bug.cgi?id=82820\>

716 \*

717 \* (This needs to be in the non-Unix-specific header so that

718 \* the config-parser can use it.)

719 \*/

720\#define DBUS_DEFAULT_MESSAGE_UNIX_FDS 16

721

722typedef struct DBusRLimit DBusRLimit;

723

724DBusRLimit \*\_dbus_rlimit_save_fd_limit (DBusError \*error);

725dbus_bool_t \_dbus_rlimit_raise_fd_limit (DBusError \*error);

726dbus_bool_t \_dbus_rlimit_restore_fd_limit (DBusRLimit \*saved,

727 DBusError \*error);

728void \_dbus_rlimit_free (DBusRLimit \*lim);

729

730void \_dbus_daemon_report_ready (void);

731void \_dbus_daemon_report_reloading (void);

732void \_dbus_daemon_report_reloaded (void);

733void \_dbus_daemon_report_stopping (void);

734

735dbus_bool_t \_dbus_inet_sockaddr_to_string (const void \*sockaddr_pointer,

736 size_t len,

737 char \*string,

738 size_t string_len,

739 const char \*\*family_name,

740 dbus_uint16_t \*port,

741 DBusError \*error);

742void \_dbus_set_error_with_inet_sockaddr (DBusError \*error,

743 const void \*sockaddr_pointer,

744 size_t len,

745 const char \*description,

746 int saved_errno);

747void \_dbus_combine_tcp_errors (DBusList \*\*sources,

748 const char \*summary,

749 const char \*host,

750 const char \*port,

751 DBusError \*dest);

752

765\#define \_DBUS_MAX_SUN_PATH_LENGTH 99

766

769DBUS_END_DECLS

770

771

772\#ifdef DBUS_WIN

773\#include "dbus-sysdeps-win.h"

774\#endif

775

776\#endif /\* DBUS_SYSDEPS_H \*/

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

\_dbus_logv

DBUS_PRIVATE_EXPORT void \_dbus_logv(DBusSystemLogSeverity severity, const char \*msg, va_list args)

Log a message to the system log file (e.g.

**Definition** dbus-sysdeps-unix.c:5208

\_dbus_stat

dbus_bool_t \_dbus_stat(const DBusString \*filename, DBusStat \*statbuf, DBusError \*error)

stat() wrapper.

**Definition** dbus-sysdeps-util-unix.c:593

\_dbus_get_monotonic_time

DBUS_PRIVATE_EXPORT void \_dbus_get_monotonic_time(dbus_int64_t \*tv_sec, long \*tv_usec)

Get current time, as in gettimeofday().

**Definition** dbus-sysdeps-unix.c:3381

\_dbus_read_local_machine_uuid

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_read_local_machine_uuid(DBusGUID \*machine_id, dbus_bool_t create_if_not_found, DBusError \*error)

Reads the uuid of the machine we're running on from the dbus configuration.

**Definition** dbus-sysdeps-unix.c:4421

\_dbus_get_standard_session_servicedirs

dbus_bool_t \_dbus_get_standard_session_servicedirs(DBusList \*\*dirs)

Returns the standard directories for a session bus to look for service activation files.

**Definition** dbus-sysdeps-util-unix.c:1364

\_dbus_get_is_errno_epipe

dbus_bool_t \_dbus_get_is_errno_epipe(int e)

See if errno is EPIPE.

**Definition** dbus-sysdeps.c:700

\_dbus_daemon_report_ready

void \_dbus_daemon_report_ready(void)

Report to a service manager that the daemon calling this function is ready for use.

**Definition** dbus-sysdeps-util-unix.c:1544

\_dbus_get_is_errno_etoomanyrefs

dbus_bool_t \_dbus_get_is_errno_etoomanyrefs(int e)

See if errno is ETOOMANYREFS.

**Definition** dbus-sysdeps.c:710

\_dbus_write_pid_to_file_and_pipe

dbus_bool_t \_dbus_write_pid_to_file_and_pipe(const DBusString \*pidfile, DBusPipe \*print_pid_pipe, dbus_pid_t pid_to_write, DBusError \*error)

Writes the given pid_to_write to a pidfile (if non-NULL) and/or to a pipe (if non-NULL).

**Definition** dbus-sysdeps-util-unix.c:240

\_dbus_directory_close

void \_dbus_directory_close(DBusDirIter \*iter)

Closes a directory iteration.

**Definition** dbus-sysdeps-util-unix.c:737

dbus_uid_t

unsigned long dbus_uid_t

A user ID.

**Definition** dbus-sysdeps.h:141

\_dbus_get_is_errno_eagain_or_ewouldblock

dbus_bool_t \_dbus_get_is_errno_eagain_or_ewouldblock(int e)

See if errno is EAGAIN or EWOULDBLOCK (this has to be done differently for Winsock so is abstracted)

**Definition** dbus-sysdeps-unix.c:4801

\_dbus_generate_random_bytes_buffer

\_DBUS_WARN_UNUSED_RESULT dbus_bool_t \_dbus_generate_random_bytes_buffer(char \*buffer, int n_bytes, DBusError \*error)

Random numbers.

**Definition** dbus-sysdeps.c:491

\_dbus_pid_for_log

unsigned long \_dbus_pid_for_log(void)

The only reason this is separate from \_dbus_getpid() is to allow it on Windows for logging but not fo...

**Definition** dbus-sysdeps-unix.c:3157

\_dbus_get_session_config_file

dbus_bool_t \_dbus_get_session_config_file(DBusString \*str)

Get the absolute path of the session.conf file.

**Definition** dbus-sysdeps-util-unix.c:1532

\_dbus_clearenv

dbus_bool_t \_dbus_clearenv(void)

Wrapper for clearenv().

**Definition** dbus-sysdeps.c:213

dbus_pid_t

unsigned long dbus_pid_t

A process ID.

**Definition** dbus-sysdeps.h:139

\_dbus_read_socket

DBUS_PRIVATE_EXPORT int \_dbus_read_socket(DBusSocket fd, DBusString \*buffer, int count)

Like \_dbus_read(), but only works on sockets so is available on Windows.

**Definition** dbus-sysdeps-unix.c:338

\_dbus_daemon_report_reloading

void \_dbus_daemon_report_reloading(void)

Report to a service manager that the daemon calling this function is reloading configuration.

**Definition** dbus-sysdeps-util-unix.c:1556

\_dbus_exit

DBUS_PRIVATE_EXPORT void \_dbus_exit(int code) \_DBUS_GNUC_NORETURN

Exit the process, returning the given value.

**Definition** dbus-sysdeps-unix.c:3641

\_dbus_socket_can_pass_unix_fd

dbus_bool_t \_dbus_socket_can_pass_unix_fd(DBusSocket fd)

Checks whether file descriptors may be passed via the socket.

**Definition** dbus-sysdeps-unix.c:4850

\_dbus_write_socket

DBUS_PRIVATE_EXPORT int \_dbus_write_socket(DBusSocket fd, const DBusString \*buffer, int start, int len)

Like \_dbus_write(), but only supports sockets and is thus available on Windows.

**Definition** dbus-sysdeps-unix.c:356

\_dbus_atomic_set_nonzero

DBUS_PRIVATE_EXPORT void \_dbus_atomic_set_nonzero(DBusAtomic \*atomic)

Atomically set the value of an integer to something nonzero.

**Definition** dbus-sysdeps-unix.c:3279

\_dbus_socketpair

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_socketpair(DBusSocket \*fd1, DBusSocket \*fd2, dbus_bool_t blocking, DBusError \*error)

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

\_dbus_command_for_pid

dbus_bool_t \_dbus_command_for_pid(unsigned long pid, DBusString \*str, int max_len, DBusError \*error)

Get a printable string describing the command used to execute the process with pid.

**Definition** dbus-sysdeps-util-unix.c:1109

\_dbus_get_system_config_file

dbus_bool_t \_dbus_get_system_config_file(DBusString \*str)

Get the absolute path of the system.conf file (there is no system bus on Windows so this can just ret...

**Definition** dbus-sysdeps-util-unix.c:1518

\_dbus_directory_open

DBusDirIter \* \_dbus_directory_open(const DBusString \*filename, DBusError \*error)

Open a directory to iterate over.

**Definition** dbus-sysdeps-util-unix.c:641

\_dbus_set_up_transient_session_servicedirs

dbus_bool_t \_dbus_set_up_transient_session_servicedirs(DBusList \*\*dirs, DBusError \*error)

Returns the standard directories for a session bus to look for transient service activation files.

**Definition** dbus-sysdeps-util-unix.c:1267

\_dbus_append_keyring_directory_for_credentials

dbus_bool_t \_dbus_append_keyring_directory_for_credentials(DBusString \*directory, DBusCredentials \*credentials)

Appends the directory in which a keyring for the given credentials should be stored.

**Definition** dbus-sysdeps-unix.c:4721

\_dbus_get_environment

char \*\* \_dbus_get_environment(void)

Gets a NULL-terminated list of key=value pairs from the environment.

**Definition** dbus-sysdeps-util.c:55

\_dbus_parse_unix_user_from_config

dbus_bool_t \_dbus_parse_unix_user_from_config(const DBusString \*username, dbus_uid_t \*uid_p)

Parse a UNIX user from the bus config file.

**Definition** dbus-sysdeps-util-unix.c:919

\_dbus_atomic_dec

DBUS_PRIVATE_EXPORT dbus_int32_t \_dbus_atomic_dec(DBusAtomic \*atomic)

Atomically decrement an integer.

**Definition** dbus-sysdeps-unix.c:3205

\_dbus_verify_daemon_user

dbus_bool_t \_dbus_verify_daemon_user(const char \*user)

Verify that after the fork we can successfully change to this user.

**Definition** dbus-sysdeps-util-unix.c:313

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

\_dbus_get_standard_system_servicedirs

dbus_bool_t \_dbus_get_standard_system_servicedirs(DBusList \*\*dirs)

Returns the standard directories for a system bus to look for service activation files.

**Definition** dbus-sysdeps-util-unix.c:1456

\_dbus_get_local_system_servicedirs

dbus_bool_t \_dbus_get_local_system_servicedirs(DBusList \*\*dirs)

Returns the local admin directories for a system bus to look for service activation files.

**Definition** dbus-sysdeps-util-unix.c:1495

\_dbus_getpid

DBUS_PRIVATE_EXPORT dbus_pid_t \_dbus_getpid(void)

Gets our process ID.

**Definition** dbus-sysdeps-unix.c:3127

\_dbus_atomic_get

DBUS_PRIVATE_EXPORT dbus_int32_t \_dbus_atomic_get(DBusAtomic \*atomic)

Atomically get the value of an integer.

**Definition** dbus-sysdeps-unix.c:3233

\_dbus_set_socket_nonblocking

dbus_bool_t \_dbus_set_socket_nonblocking(DBusSocket fd, DBusError \*error)

Sets a file descriptor to be nonblocking.

**Definition** dbus-sysdeps-unix.c:3797

\_dbus_lookup_session_address

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_lookup_session_address(dbus_bool_t \*supported, DBusString \*address, DBusError \*error)

Determines the address of the session bus by querying a platform-specific method.

**Definition** dbus-sysdeps-unix.c:4670

\_dbus_error_from_system_errno

DBUS_PRIVATE_EXPORT const char \* \_dbus_error_from_system_errno(void)

Converts the current system errno value into a DBusError name.

**Definition** dbus-sysdeps.c:657

\_dbus_credentials_add_from_user

dbus_bool_t \_dbus_credentials_add_from_user(DBusCredentials \*credentials, const DBusString \*username, DBusCredentialsAddFlags flags, DBusError \*error)

Adds the credentials corresponding to the given username.

**Definition** dbus-sysdeps-win.c:2314

\_dbus_connect_tcp_socket

DBusSocket \_dbus_connect_tcp_socket(const char \*host, const char \*port, const char \*family, DBusError \*error)

Creates a socket and connects to a socket at the given host and port.

**Definition** dbus-sysdeps-unix.c:1449

\_dbus_threads_lock_platform_specific

void \_dbus_threads_lock_platform_specific(void)

Lock a static mutex used to protect \_dbus_threads_init_platform_specific().

**Definition** dbus-sysdeps-pthread.c:296

\_dbus_disable_sigpipe

void \_dbus_disable_sigpipe(void)

signal (SIGPIPE, SIG_IGN);

**Definition** dbus-sysdeps-unix.c:3670

\_dbus_check_setuid

dbus_bool_t \_dbus_check_setuid(void)

NOTE: If you modify this function, please also consider making the corresponding change in GLib.

**Definition** dbus-sysdeps-unix.c:5002

\_dbus_daemon_report_reloaded

void \_dbus_daemon_report_reloaded(void)

Report to a service manager that the daemon calling this function is reloading configuration.

**Definition** dbus-sysdeps-util-unix.c:1568

\_dbus_sleep_milliseconds

DBUS_PRIVATE_EXPORT void \_dbus_sleep_milliseconds(int milliseconds)

Sleeps the given number of milliseconds.

**Definition** dbus-sysdeps-unix.c:3542

\_dbus_resolve_pid_fd

DBUS_PRIVATE_EXPORT dbus_pid_t \_dbus_resolve_pid_fd(int pid_fd)

Resolve the PID from the PID FD, if any.

**Definition** dbus-sysdeps-unix.c:3045

\_dbus_change_to_daemon_user

dbus_bool_t \_dbus_change_to_daemon_user(const char \*user, DBusError \*error)

Changes the user and group the bus is running as.

**Definition** dbus-sysdeps-util-unix.c:333

\_dbus_unix_user_is_process_owner

dbus_bool_t \_dbus_unix_user_is_process_owner(dbus_uid_t uid)

Checks to see if the UNIX user ID matches the UID of the process.

**Definition** dbus-sysdeps-util-unix.c:986

\_dbus_strerror_from_errno

DBUS_PRIVATE_EXPORT const char \* \_dbus_strerror_from_errno(void)

Get error message from errno.

**Definition** dbus-sysdeps.c:724

\_dbus_check_dir_is_private_to_user

dbus_bool_t \_dbus_check_dir_is_private_to_user(DBusString \*dir, DBusError \*error)

Checks to make sure the given directory is private to the user.

**Definition** dbus-sysdeps-unix.c:2644

\_dbus_log

DBUS_PRIVATE_EXPORT void \_dbus_log(DBusSystemLogSeverity severity, const char \*msg,...)

Log a message to the system log file (e.g.

**Definition** dbus-sysdeps.c:736

\_dbus_windows_user_is_process_owner

dbus_bool_t \_dbus_windows_user_is_process_owner(const char \*windows_sid)

Checks to see if the Windows user SID matches the owner of the process.

**Definition** dbus-sysdeps-util-unix.c:999

\_dbus_daemon_unpublish_session_bus_address

dbus_bool_t \_dbus_daemon_unpublish_session_bus_address(void)

Clear the platform-specific centralized location where the session bus address is published.

**Definition** dbus-sysdeps-unix.c:4789

\_dbus_parse_unix_group_from_config

dbus_bool_t \_dbus_parse_unix_group_from_config(const DBusString \*groupname, dbus_gid_t \*gid_p)

Parse a UNIX group from the bus config file.

**Definition** dbus-sysdeps-util-unix.c:935

\_dbus_listen_tcp_socket

int \_dbus_listen_tcp_socket(const char \*host, const char \*port, const char \*family, DBusString \*retport, const char \*\*retfamily, DBusSocket \*\*fds_p, DBusError \*error)

Creates a socket and binds it to the given path, then listens on the socket.

**Definition** dbus-sysdeps-unix.c:1606

\_dbus_threads_unlock_platform_specific

void \_dbus_threads_unlock_platform_specific(void)

Undo \_dbus_threads_lock_platform_specific().

**Definition** dbus-sysdeps-pthread.c:302

\_dbus_send_credentials_socket

dbus_bool_t \_dbus_send_credentials_socket(DBusSocket server_fd, DBusError \*error)

Sends a single nul byte with our UNIX credentials as ancillary data.

**Definition** dbus-sysdeps-unix.c:2568

\_dbus_unix_groups_from_uid

dbus_bool_t \_dbus_unix_groups_from_uid(dbus_uid_t uid, dbus_gid_t \*\*group_ids, int \*n_group_ids, DBusError \*error)

Gets all groups corresponding to the given UNIX user ID.

**Definition** dbus-sysdeps-util-unix.c:953

\_dbus_getuid

DBUS_PRIVATE_EXPORT dbus_uid_t \_dbus_getuid(void)

Gets our UID.

**Definition** dbus-sysdeps-unix.c:3136

\_dbus_credentials_add_from_current_process

dbus_bool_t \_dbus_credentials_add_from_current_process(DBusCredentials \*credentials)

Adds the most important credentials of the current process (the uid and pid) to the passed-in credent...

**Definition** dbus-sysdeps-unix.c:3005

\_dbus_daemon_report_stopping

void \_dbus_daemon_report_stopping(void)

Report to a service manager that the daemon calling this function is shutting down.

**Definition** dbus-sysdeps-util-unix.c:1581

\_dbus_close_socket

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_close_socket(DBusSocket \*fd, DBusError \*error)

Closes a socket and invalidates it.

**Definition** dbus-sysdeps-unix.c:314

\_dbus_connect_unix_socket

DBusSocket \_dbus_connect_unix_socket(const char \*path, dbus_bool_t abstract, DBusError \*error)

Creates a socket and connects it to the UNIX domain socket at the given path.

**Definition** dbus-sysdeps-unix.c:957

\_dbus_atomic_set_zero

DBUS_PRIVATE_EXPORT void \_dbus_atomic_set_zero(DBusAtomic \*atomic)

Atomically set the value of an integer to 0.

**Definition** dbus-sysdeps-unix.c:3258

\_dbus_atomic_inc

DBUS_PRIVATE_EXPORT dbus_int32_t \_dbus_atomic_inc(DBusAtomic \*atomic)

Atomically increments an integer.

**Definition** dbus-sysdeps-unix.c:3178

\_dbus_generate_random_bytes

dbus_bool_t \_dbus_generate_random_bytes(DBusString \*str, int n_bytes, DBusError \*error)

Generates the given number of securely random bytes, using the best mechanism we can come up with.

**Definition** dbus-sysdeps-unix.c:3572

\_dbus_printf_string_upper_bound

DBUS_PRIVATE_EXPORT int \_dbus_printf_string_upper_bound(const char \*format, va_list args)

Measure the length of the given format string and arguments, not including the terminating nul.

**Definition** dbus-sysdeps-unix.c:3959

\_dbus_delete_directory

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_delete_directory(const DBusString \*filename, DBusError \*error)

Removes a directory; Directory must be empty.

**Definition** dbus-sysdeps-unix.c:4822

\_dbus_error_from_errno

DBUS_PRIVATE_EXPORT const char \* \_dbus_error_from_errno(int error_number)

Converts a UNIX errno, or Windows errno or WinSock error value into a DBusError name.

**Definition** dbus-sysdeps.c:565

\_dbus_abort

void \_dbus_abort(void)

Aborts the program with SIGABRT (dumping core).

**Definition** dbus-sysdeps.c:89

\_dbus_directory_get_next_file

dbus_bool_t \_dbus_directory_get_next_file(DBusDirIter \*iter, DBusString \*filename, DBusError \*error)

Get next file in the directory.

**Definition** dbus-sysdeps-util-unix.c:689

\_dbus_poll

DBUS_PRIVATE_EXPORT int \_dbus_poll(DBusPollFD \*fds, int n_fds, int timeout_milliseconds)

Wrapper for poll().

**Definition** dbus-sysdeps-unix.c:3303

\_dbus_generate_random_ascii

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_generate_random_ascii(DBusString \*str, int n_bytes, DBusError \*error)

Generates the given number of random bytes, where the bytes are chosen from the alphanumeric ASCII su...

**Definition** dbus-sysdeps.c:525

\_dbus_get_autolaunch_address

dbus_bool_t \_dbus_get_autolaunch_address(const char \*scope, DBusString \*address, DBusError \*error)

Returns the address of a new session bus.

**Definition** dbus-sysdeps-unix.c:4299

\_dbus_write_socket_two

int \_dbus_write_socket_two(DBusSocket fd, const DBusString \*buffer1, int start1, int len1, const DBusString \*buffer2, int start2, int len2)

Like \_dbus_write_two() but only works on sockets and is thus available on Windows.

**Definition** dbus-sysdeps-unix.c:694

\_dbus_concat_dir_and_file

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_concat_dir_and_file(DBusString \*dir, const DBusString \*next_component)

Appends the given filename to the given directory.

**Definition** dbus-sysdeps-unix.c:3497

\_dbus_become_daemon

dbus_bool_t \_dbus_become_daemon(const DBusString \*pidfile, DBusPipe \*print_pid_pipe, DBusError \*error, dbus_bool_t keep_umask)

Does the chdir, fork, setsid, etc.

**Definition** dbus-sysdeps-util-unix.c:86

\_dbus_connect_exec

DBusSocket \_dbus_connect_exec(const char \*path, char \*const argv\[\], DBusError \*error)

Creates a UNIX domain socket and connects it to the specified process to execute.

**Definition** dbus-sysdeps-unix.c:1054

\_dbus_split_paths_and_append

dbus_bool_t \_dbus_split_paths_and_append(DBusString \*dirs, const char \*suffix, DBusList \*\*dir_list)

Split paths into a list of char strings.

**Definition** dbus-sysdeps.c:238

\_dbus_print_backtrace

DBUS_PRIVATE_EXPORT void \_dbus_print_backtrace(void)

On GNU libc systems, print a crude backtrace to stderr.

**Definition** dbus-backtrace-win.c:204

\_dbus_get_real_time

DBUS_PRIVATE_EXPORT void \_dbus_get_real_time(dbus_int64_t \*tv_sec, long \*tv_usec)

Get current time, as in gettimeofday().

**Definition** dbus-sysdeps-unix.c:3412

\_dbus_init_system_log

DBUS_PRIVATE_EXPORT void \_dbus_init_system_log(const char \*tag, DBusLogFlags flags)

Initialize the system log.

**Definition** dbus-sysdeps-unix.c:5183

\_dbus_replace_install_prefix

dbus_bool_t \_dbus_replace_install_prefix(DBusString \*path)

Replace the DBUS_PREFIX in the given path, in-place, by the current D-Bus installation directory.

**Definition** dbus-sysdeps-util-unix.c:1185

\_dbus_accept

DBusSocket \_dbus_accept(DBusSocket listen_fd)

Accepts a connection on a listening socket.

**Definition** dbus-sysdeps-unix.c:2589

\_dbus_append_user_from_current_process

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_append_user_from_current_process(DBusString \*str)

Append to the string the identity we would like to have when we authenticate, on UNIX this is the cur...

**Definition** dbus-sysdeps-unix.c:3117

\_dbus_flush_caches

DBUS_PRIVATE_EXPORT void \_dbus_flush_caches(void)

Called when the bus daemon is signaled to reload its configuration; any caches should be nuked.

**Definition** dbus-sysdeps-unix.c:4702

\_dbus_get_is_errno_eintr

dbus_bool_t \_dbus_get_is_errno_eintr(int e)

See if errno is EINTR.

**Definition** dbus-sysdeps.c:690

\_dbus_threads_init_platform_specific

dbus_bool_t \_dbus_threads_init_platform_specific(void)

Initialize threads as in dbus_threads_init_default(), appropriately for the platform.

**Definition** dbus-sysdeps-pthread.c:281

\_dbus_unix_user_is_at_console

dbus_bool_t \_dbus_unix_user_is_at_console(dbus_uid_t uid, DBusError \*error)

Checks to see if the UNIX user ID is at the console.

**Definition** dbus-sysdeps-util-unix.c:971

\_dbus_set_errno_to_zero

void \_dbus_set_errno_to_zero(void)

Assign 0 to the global errno variable.

**Definition** dbus-sysdeps.c:666

\_dbus_get_tmpdir

DBUS_PRIVATE_EXPORT const char \* \_dbus_get_tmpdir(void)

Gets the temporary files directory by inspecting the environment variables TMPDIR,...

**Definition** dbus-sysdeps-unix.c:4029

\_dbus_ensure_directory

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_ensure_directory(const DBusString \*filename, DBusError \*error)

Creates a directory; succeeds if the directory is created or already existed.

**Definition** dbus-sysdeps-unix.c:3434

\_dbus_get_is_errno_enomem

dbus_bool_t \_dbus_get_is_errno_enomem(int e)

See if errno is ENOMEM.

**Definition** dbus-sysdeps.c:680

\_dbus_string_get_dirname

dbus_bool_t \_dbus_string_get_dirname(const DBusString \*filename, DBusString \*dirname)

Get the directory name from a complete filename.

**Definition** dbus-sysdeps-util-unix.c:1018

\_dbus_path_is_absolute

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_path_is_absolute(const DBusString \*filename)

Checks whether the filename is an absolute path.

**Definition** dbus-sysdeps-util-unix.c:576

\_dbus_create_directory

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_create_directory(const DBusString \*filename, DBusError \*error)

directory interface

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

DBusGUID

A globally unique ID ; we have one for each DBusServer, and also one for each machine with libdbus in...

**Definition** dbus-internals.h:458
