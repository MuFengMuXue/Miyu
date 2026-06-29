dbus-mainloop.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-mainloop.c Main loop utility

3 \*

4 \* Copyright © 2003, 2004 Red Hat, Inc.

5 \* Copyright © 2011 Nokia Corporation

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

28\#include "dbus-mainloop.h"

29

30\#ifndef DOXYGEN_SHOULD_SKIP_THIS

31

32\#include \<dbus/dbus-hash.h\>

33\#include \<dbus/dbus-list.h\>

34\#include \<dbus/dbus-pollable-set.h\>

35\#include \<dbus/dbus-timeout.h\>

36\#include \<dbus/dbus-watch.h\>

37

38\#define MAINLOOP_SPEW 0

39

40struct DBusLoop

41{

42 int refcount;

44 DBusHashTable \*watches;

45 DBusPollableSet \*pollable_set;

46 DBusList \*timeouts;

47 int callback_list_serial;

48 int watch_count;

49 int timeout_count;

50 int depth;

51 DBusList \*need_dispatch;

54 unsigned oom_watch_pending : 1;

55};

56

57typedef struct

58{

59 DBusTimeout \*timeout;

60 dbus_int64_t last_tv_sec;

61 long last_tv_usec;

62} TimeoutCallback;

63

64\#define TIMEOUT_CALLBACK(callback) ((TimeoutCallback\*)callback)

65

66static TimeoutCallback\*

67timeout_callback_new (DBusTimeout \*timeout)

68{

69 TimeoutCallback \*cb;

70

71 cb = dbus_new (TimeoutCallback, 1);

72 if (cb == NULL)

73 return NULL;

74

75 cb-\>timeout = timeout;

76 \_dbus_get_monotonic_time (&cb-\>last_tv_sec,

77 &cb-\>last_tv_usec);

78 return cb;

79}

80

81static void

82timeout_callback_free (TimeoutCallback \*cb)

83{

84 dbus_free (cb);

85}

86

87static void

88free_watch_table_entry (void \*data)

89{

90 DBusList \*\*watches = data;

91 DBusWatch \*watch;

92

93 /\* DBusHashTable sometimes calls free_function(NULL) even if you never

94 \* have NULL as a value \*/

95 if (watches == NULL)

96 return;

97

98 for (watch = \_dbus_list_pop_first (watches);

99 watch != NULL;

100 watch = \_dbus_list_pop_first (watches))

101 {

102 \_dbus_watch_unref (watch);

103 }

104

105 \_dbus_assert (\*watches == NULL);

106 dbus_free (watches);

107}

108

109DBusLoop\*

110\_dbus_loop_new (void)

111{

112 DBusLoop \*loop;

113

114 loop = dbus_new0 (DBusLoop, 1);

115 if (loop == NULL)

116 return NULL;

117

118 loop-\>watches = \_dbus_hash_table_new (DBUS_HASH_POLLABLE, NULL,

119 free_watch_table_entry);

120

121 loop-\>pollable_set = \_dbus_pollable_set_new (0);

122

123 if (loop-\>watches == NULL \|\| loop-\>pollable_set == NULL)

124 {

125 if (loop-\>watches != NULL)

126 \_dbus_hash_table_unref (loop-\>watches);

127

128 if (loop-\>pollable_set != NULL)

129 \_dbus_pollable_set_free (loop-\>pollable_set);

130

131 dbus_free (loop);

132 return NULL;

133 }

134

135 loop-\>refcount = 1;

136

137 return loop;

138}

139

140DBusLoop \*

141\_dbus_loop_ref (DBusLoop \*loop)

142{

143 \_dbus_assert (loop != NULL);

144 \_dbus_assert (loop-\>refcount \> 0);

145

146 loop-\>refcount += 1;

147

148 return loop;

149}

150

151void

152\_dbus_loop_unref (DBusLoop \*loop)

153{

154 \_dbus_assert (loop != NULL);

155 \_dbus_assert (loop-\>refcount \> 0);

156

157 loop-\>refcount -= 1;

158 if (loop-\>refcount == 0)

159 {

160 while (loop-\>need_dispatch)

161 {

162 DBusConnection \*connection = \_dbus_list_pop_first (&loop-\>need_dispatch);

163

164 dbus_connection_unref (connection);

165 }

166

167 \_dbus_hash_table_unref (loop-\>watches);

168 \_dbus_pollable_set_free (loop-\>pollable_set);

169 dbus_free (loop);

170 }

171}

172

173static DBusList \*\*

174ensure_watch_table_entry (DBusLoop \*loop,

175 DBusPollable fd)

176{

177 DBusList \*\*watches;

178

179 watches = \_dbus_hash_table_lookup_pollable (loop-\>watches, fd);

180

181 if (watches == NULL)

182 {

183 watches = dbus_new0 (DBusList \*, 1);

184

185 if (watches == NULL)

186 return watches;

187

188 if (!\_dbus_hash_table_insert_pollable (loop-\>watches, fd, watches))

189 {

190 dbus_free (watches);

191 watches = NULL;

192 }

193 }

194

195 return watches;

196}

197

198static void

199cull_watches_for_invalid_fd (DBusLoop \*loop,

200 DBusPollable fd)

201{

202 DBusList \*link;

203 DBusList \*\*watches;

204

205 \_dbus_warn ("invalid request, socket fd %" DBUS_POLLABLE_FORMAT " not open",

206 \_dbus_pollable_printable (fd));

207 watches = \_dbus_hash_table_lookup_pollable (loop-\>watches, fd);

208

209 if (watches != NULL)

210 {

211 for (link = \_dbus_list_get_first_link (watches);

212 link != NULL;

213 link = \_dbus_list_get_next_link (watches, link))

214 \_dbus_watch_invalidate (link-\>data);

215 }

216

217 \_dbus_hash_table_remove_pollable (loop-\>watches, fd);

218}

219

220static dbus_bool_t

221gc_watch_table_entry (DBusLoop \*loop,

222 DBusList \*\*watches,

223 DBusPollable fd)

224{

225 /\* If watches is already NULL we have nothing to do \*/

226 if (watches == NULL)

227 return FALSE;

228

229 /\* We can't GC hash table entries if they're non-empty lists \*/

230 if (\*watches != NULL)

231 return FALSE;

232

233 \_dbus_hash_table_remove_pollable (loop-\>watches, fd);

234 return TRUE;

235}

236

237static void

238refresh_watches_for_fd (DBusLoop \*loop,

239 DBusList \*\*watches,

240 DBusPollable fd)

241{

242 DBusList \*link;

243 unsigned int flags = 0;

244 dbus_bool_t interested = FALSE;

245

246 \_dbus_assert (\_dbus_pollable_is_valid (fd));

247

248 if (watches == NULL)

249 watches = \_dbus_hash_table_lookup_pollable (loop-\>watches, fd);

250

251 /\* we allocated this in the first \_dbus_loop_add_watch for the fd, and keep

252 \* it until there are none left \*/

253 \_dbus_assert (watches != NULL);

254

255 for (link = \_dbus_list_get_first_link (watches);

256 link != NULL;

257 link = \_dbus_list_get_next_link (watches, link))

258 {

259 if (dbus_watch_get_enabled (link-\>data) &&

260 !\_dbus_watch_get_oom_last_time (link-\>data))

261 {

262 flags \|= dbus_watch_get_flags (link-\>data);

263 interested = TRUE;

264 }

265 }

266

267 if (interested)

268 \_dbus_pollable_set_enable (loop-\>pollable_set, fd, flags);

269 else

270 \_dbus_pollable_set_disable (loop-\>pollable_set, fd);

271}

272

273dbus_bool_t

274\_dbus_loop_add_watch (DBusLoop \*loop,

275 DBusWatch \*watch)

276{

277 DBusPollable fd;

278 DBusList \*\*watches;

279

280 fd = \_dbus_watch_get_pollable (watch);

281 \_dbus_assert (\_dbus_pollable_is_valid (fd));

282

283 watches = ensure_watch_table_entry (loop, fd);

284

285 if (watches == NULL)

286 return FALSE;

287

288 if (!\_dbus_list_append (watches, \_dbus_watch_ref (watch)))

289 {

290 \_dbus_watch_unref (watch);

291 gc_watch_table_entry (loop, watches, fd);

292

293 return FALSE;

294 }

295

296 if (\_dbus_list_length_is_one (watches))

297 {

298 if (!\_dbus_pollable_set_add (loop-\>pollable_set, fd,

299 dbus_watch_get_flags (watch),

300 dbus_watch_get_enabled (watch)))

301 {

302 \_dbus_hash_table_remove_pollable (loop-\>watches, fd);

303 return FALSE;

304 }

305 }

306 else

307 {

308 /\* we're modifying, not adding, which can't fail with OOM \*/

309 refresh_watches_for_fd (loop, watches, fd);

310 }

311

312 loop-\>callback_list_serial += 1;

313 loop-\>watch_count += 1;

314 return TRUE;

315}

316

317void

318\_dbus_loop_toggle_watch (DBusLoop \*loop,

319 DBusWatch \*watch)

320{

321 refresh_watches_for_fd (loop, NULL, \_dbus_watch_get_pollable (watch));

322}

323

324void

325\_dbus_loop_remove_watch (DBusLoop \*loop,

326 DBusWatch \*watch)

327{

328 DBusList \*\*watches;

329 DBusList \*link;

330 DBusPollable fd;

331

332 /\* This relies on people removing watches before they invalidate them,

333 \* which has been safe since fd.o \#33336 was fixed. Assert about it

334 \* so we don't regress. \*/

335 fd = \_dbus_watch_get_pollable (watch);

336 \_dbus_assert (\_dbus_pollable_is_valid (fd));

337

338 watches = \_dbus_hash_table_lookup_pollable (loop-\>watches, fd);

339

340 if (watches != NULL)

341 {

342 link = \_dbus_list_get_first_link (watches);

343 while (link != NULL)

344 {

345 DBusList \*next = \_dbus_list_get_next_link (watches, link);

346 DBusWatch \*this = link-\>data;

347

348 if (this == watch)

349 {

350 \_dbus_list_remove_link (watches, link);

351 loop-\>callback_list_serial += 1;

352 loop-\>watch_count -= 1;

353 \_dbus_watch_unref (this);

354

355 /\* if that was the last watch for that fd, drop the hash table

356 \* entry, and stop reserving space for it in the socket set \*/

357 if (gc_watch_table_entry (loop, watches, fd))

358 {

359 \_dbus_pollable_set_remove (loop-\>pollable_set, fd);

360 }

361

362 return;

363 }

364

365 link = next;

366 }

367 }

368

369 \_dbus_warn ("could not find watch %p to remove", watch);

370}

371

372dbus_bool_t

373\_dbus_loop_add_timeout (DBusLoop \*loop,

374 DBusTimeout \*timeout)

375{

376 TimeoutCallback \*tcb;

377

378 tcb = timeout_callback_new (timeout);

379 if (tcb == NULL)

380 return FALSE;

381

382 if (\_dbus_list_append (&loop-\>timeouts, tcb))

383 {

384 loop-\>callback_list_serial += 1;

385 loop-\>timeout_count += 1;

386 }

387 else

388 {

389 timeout_callback_free (tcb);

390 return FALSE;

391 }

392

393 return TRUE;

394}

395

396void

397\_dbus_loop_remove_timeout (DBusLoop \*loop,

398 DBusTimeout \*timeout)

399{

400 DBusList \*link;

401

402 link = \_dbus_list_get_first_link (&loop-\>timeouts);

403 while (link != NULL)

404 {

405 DBusList \*next = \_dbus_list_get_next_link (&loop-\>timeouts, link);

406 TimeoutCallback \*this = link-\>data;

407

408 if (this-\>timeout == timeout)

409 {

410 \_dbus_list_remove_link (&loop-\>timeouts, link);

411 loop-\>callback_list_serial += 1;

412 loop-\>timeout_count -= 1;

413 timeout_callback_free (this);

414

415 return;

416 }

417

418 link = next;

419 }

420

421 \_dbus_warn ("could not find timeout %p to remove", timeout);

422}

423

424/\* Convolutions from GLib, there really must be a better way

425 \* to do this.

426 \*/

427static dbus_bool_t

428check_timeout (dbus_int64_t tv_sec,

429 long tv_usec,

430 TimeoutCallback \*tcb,

431 int \*timeout)

432{

433 dbus_int64_t sec_remaining;

434 long msec_remaining;

435 dbus_int64_t expiration_tv_sec;

436 long expiration_tv_usec;

437 dbus_int64_t interval_seconds;

438 long interval_milliseconds;

439 int interval;

440

441 /\* I'm pretty sure this function could suck (a lot) less \*/

442

443 interval = dbus_timeout_get_interval (tcb-\>timeout);

444

445 interval_seconds = interval / 1000L;

446 interval_milliseconds = interval % 1000L;

447

448 expiration_tv_sec = tcb-\>last_tv_sec + interval_seconds;

449 expiration_tv_usec = tcb-\>last_tv_usec + interval_milliseconds \* 1000;

450 if (expiration_tv_usec \>= 1000000)

451 {

452 expiration_tv_usec -= 1000000;

453 expiration_tv_sec += 1;

454 }

455

456 sec_remaining = expiration_tv_sec - tv_sec;

457 msec_remaining = (expiration_tv_usec - tv_usec) / 1000L;

458

459\#if MAINLOOP_SPEW

460 \_dbus_verbose ("Interval is %ld seconds %ld msecs\n",

461 interval_seconds,

462 interval_milliseconds);

463 \_dbus_verbose ("Now is %lu seconds %lu usecs\n",

464 tv_sec, tv_usec);

465 \_dbus_verbose ("Last is %lu seconds %lu usecs\n",

466 tcb-\>last_tv_sec, tcb-\>last_tv_usec);

467 \_dbus_verbose ("Exp is %lu seconds %lu usecs\n",

468 expiration_tv_sec, expiration_tv_usec);

469 \_dbus_verbose ("Pre-correction, sec_remaining %ld msec_remaining %ld\n",

470 sec_remaining, msec_remaining);

471\#endif

472

473 /\* We do the following in a rather convoluted fashion to deal with

474 \* the fact that we don't have an integral type big enough to hold

475 \* the difference of two timevals in milliseconds.

476 \*/

477 if (sec_remaining \< 0 \|\| (sec_remaining == 0 && msec_remaining \< 0))

478 {

479 \*timeout = 0;

480 }

481 else

482 {

483 if (msec_remaining \< 0)

484 {

485 msec_remaining += 1000;

486 sec_remaining -= 1;

487 }

488

489 if (sec_remaining \> (\_DBUS_INT_MAX / 1000) \|\|

490 msec_remaining \> \_DBUS_INT_MAX)

491 \*timeout = \_DBUS_INT_MAX;

492 else

493 \*timeout = sec_remaining \* 1000 + msec_remaining;

494 }

495

496 if (\*timeout \> interval)

497 {

498 /\* This indicates that the system clock probably moved backward \*/

499 \_dbus_verbose ("System clock set backward! Resetting timeout.\n");

500

501 tcb-\>last_tv_sec = tv_sec;

502 tcb-\>last_tv_usec = tv_usec;

503

504 \*timeout = interval;

505 }

506

507\#if MAINLOOP_SPEW

508 \_dbus_verbose (" timeout expires in %d milliseconds\n", \*timeout);

509\#endif

510

511 return \*timeout == 0;

512}

513

514dbus_bool_t

515\_dbus_loop_dispatch (DBusLoop \*loop)

516{

517

518\#if MAINLOOP_SPEW

519 \_dbus_verbose (" %d connections to dispatch\n", \_dbus_list_get_length (&loop-\>need_dispatch));

520\#endif

521

522 if (loop-\>need_dispatch == NULL)

523 return FALSE;

524

525 next:

526 while (loop-\>need_dispatch != NULL)

527 {

528 DBusConnection \*connection = \_dbus_list_pop_first (&loop-\>need_dispatch);

529

530 while (TRUE)

531 {

532 DBusDispatchStatus status;

533

534 status = dbus_connection_dispatch (connection);

535

536 if (status == DBUS_DISPATCH_COMPLETE)

537 {

538 dbus_connection_unref (connection);

539 goto next;

540 }

541 else

542 {

543 if (status == DBUS_DISPATCH_NEED_MEMORY)

544 \_dbus_wait_for_memory ();

545 }

546 }

547 }

548

549 return TRUE;

550}

551

552dbus_bool_t

553\_dbus_loop_queue_dispatch (DBusLoop \*loop,

554 DBusConnection \*connection)

555{

556 if (\_dbus_list_append (&loop-\>need_dispatch, connection))

557 {

558 dbus_connection_ref (connection);

559 return TRUE;

560 }

561 else

562 return FALSE;

563}

564

565/\* Returns the smaller non-negative number of the two, or the larger negative

566 \* number if both numbers are negative. Poll interprets negative timeout as

567 \* infinity, which makes it longer than any actual timeout.

568 \*/

569static int

570min_poll_timeout (int a,

571 int b)

572{

573 if (a \< b)

574 return a \< 0 ? b : a;

575 else

576 return b \< 0 ? a : b;

577}

578

579/\* Returns TRUE if we invoked any timeouts or have ready file

580 \* descriptors, which is just used in test code as a debug hack

581 \*/

582

583dbus_bool_t

584\_dbus_loop_iterate (DBusLoop \*loop,

585 dbus_bool_t block)

586{

587\#define N_STACK_DESCRIPTORS 64

588 dbus_bool_t retval;

589 DBusPollableEvent ready_fds\[N_STACK_DESCRIPTORS\];

590 int i;

591 DBusList \*link;

592 int n_ready;

593 int initial_serial;

594 int timeout;

595 int orig_depth;

596

597 retval = FALSE;

598

599 orig_depth = loop-\>depth;

600

601\#if MAINLOOP_SPEW

602 \_dbus_verbose ("Iteration block=%d depth=%d timeout_count=%d watch_count=%d\n",

603 block, loop-\>depth, loop-\>timeout_count, loop-\>watch_count);

604\#endif

605

606 if (\_dbus_hash_table_get_n_entries (loop-\>watches) == 0 &&

607 loop-\>timeouts == NULL)

608 goto next_iteration;

609

610 timeout = -1;

611 if (loop-\>timeout_count \> 0)

612 {

613 dbus_int64_t tv_sec;

614 long tv_usec;

615

616 \_dbus_get_monotonic_time (&tv_sec, &tv_usec);

617

618 link = \_dbus_list_get_first_link (&loop-\>timeouts);

619 while (link != NULL)

620 {

621 DBusList \*next = \_dbus_list_get_next_link (&loop-\>timeouts, link);

622 TimeoutCallback \*tcb = link-\>data;

623

624 if (dbus_timeout_get_enabled (tcb-\>timeout))

625 {

626 int msecs_remaining;

627

628 if (\_dbus_timeout_needs_restart (tcb-\>timeout))

629 {

630 tcb-\>last_tv_sec = tv_sec;

631 tcb-\>last_tv_usec = tv_usec;

632 \_dbus_timeout_restarted (tcb-\>timeout);

633 }

634

635 check_timeout (tv_sec, tv_usec, tcb, &msecs_remaining);

636

637 timeout = min_poll_timeout (msecs_remaining, timeout);

638

639\#if MAINLOOP_SPEW

640 \_dbus_verbose (" timeout added, %d remaining, aggregate timeout %ld\n",

641 msecs_remaining, timeout);

642\#endif

643

644 \_dbus_assert (timeout \>= 0);

645 }

646\#if MAINLOOP_SPEW

647 else

648 {

649 \_dbus_verbose (" skipping disabled timeout\n");

650 }

651\#endif

652

653 link = next;

654 }

655 }

656

657 /\* Never block if we have stuff to dispatch \*/

658 if (!block \|\| loop-\>need_dispatch != NULL)

659 {

660 timeout = 0;

661\#if MAINLOOP_SPEW

662 \_dbus_verbose (" timeout is 0 as we aren't blocking\n");

663\#endif

664 }

665

666 /\* if a watch was OOM last time, don't wait longer than the OOM

667 \* wait to re-enable it

668 \*/

669 if (loop-\>oom_watch_pending)

670 timeout = min_poll_timeout (timeout, \_dbus_get_oom_wait ());

671

672\#if MAINLOOP_SPEW

673 \_dbus_verbose (" polling on %d descriptors timeout %ld\n", \_DBUS_N_ELEMENTS (ready_fds), timeout);

674\#endif

675

676 n_ready = \_dbus_pollable_set_poll (loop-\>pollable_set, ready_fds,

677 \_DBUS_N_ELEMENTS (ready_fds), timeout);

678

679 /\* re-enable any watches we skipped this time \*/

680 if (loop-\>oom_watch_pending)

681 {

682 DBusHashIter hash_iter;

683

684 loop-\>oom_watch_pending = FALSE;

685

686 \_dbus_hash_iter_init (loop-\>watches, &hash_iter);

687

688 while (\_dbus_hash_iter_next (&hash_iter))

689 {

690 DBusList \*\*watches;

691 DBusPollable fd;

692 dbus_bool_t changed;

693

694 changed = FALSE;

695 fd = \_dbus_hash_iter_get_pollable_key (&hash_iter);

696 watches = \_dbus_hash_iter_get_value (&hash_iter);

697

698 for (link = \_dbus_list_get_first_link (watches);

699 link != NULL;

700 link = \_dbus_list_get_next_link (watches, link))

701 {

702 DBusWatch \*watch = link-\>data;

703

704 if (\_dbus_watch_get_oom_last_time (watch))

705 {

706 \_dbus_watch_set_oom_last_time (watch, FALSE);

707 changed = TRUE;

708 }

709 }

710

711 if (changed)

712 refresh_watches_for_fd (loop, watches, fd);

713 }

714

715 retval = TRUE; /\* return TRUE here to keep the loop going,

716 \* since we don't know the watch was inactive \*/

717 }

718

719 initial_serial = loop-\>callback_list_serial;

720

721 if (loop-\>timeout_count \> 0)

722 {

723 dbus_int64_t tv_sec;

724 long tv_usec;

725

726 \_dbus_get_monotonic_time (&tv_sec, &tv_usec);

727

728 /\* It'd be nice to avoid this O(n) thingy here \*/

729 link = \_dbus_list_get_first_link (&loop-\>timeouts);

730 while (link != NULL)

731 {

732 DBusList \*next = \_dbus_list_get_next_link (&loop-\>timeouts, link);

733 TimeoutCallback \*tcb = link-\>data;

734

735 if (initial_serial != loop-\>callback_list_serial)

736 goto next_iteration;

737

738 if (loop-\>depth != orig_depth)

739 goto next_iteration;

740

741 if (dbus_timeout_get_enabled (tcb-\>timeout))

742 {

743 int msecs_remaining;

744

745 if (check_timeout (tv_sec, tv_usec,

746 tcb, &msecs_remaining))

747 {

748 /\* Save last callback time and fire this timeout \*/

749 tcb-\>last_tv_sec = tv_sec;

750 tcb-\>last_tv_usec = tv_usec;

751

752\#if MAINLOOP_SPEW

753 \_dbus_verbose (" invoking timeout\n");

754\#endif

755

756 /\* can theoretically return FALSE on OOM, but we just

757 \* let it fire again later - in practice that's what

758 \* every wrapper callback in dbus-daemon used to do \*/

759 dbus_timeout_handle (tcb-\>timeout);

760

761 retval = TRUE;

762 }

763 else

764 {

765\#if MAINLOOP_SPEW

766 \_dbus_verbose (" timeout has not expired\n");

767\#endif

768 }

769 }

770\#if MAINLOOP_SPEW

771 else

772 {

773 \_dbus_verbose (" skipping invocation of disabled timeout\n");

774 }

775\#endif

776

777 link = next;

778 }

779 }

780

781 if (n_ready \> 0)

782 {

783 for (i = 0; i \< n_ready; i++)

784 {

785 DBusList \*\*watches;

786 DBusList \*next;

787 unsigned int condition;

788 dbus_bool_t any_oom;

789

790 /\* FIXME I think this "restart if we change the watches"

791 \* approach could result in starving watches

792 \* toward the end of the list.

793 \*/

794 if (initial_serial != loop-\>callback_list_serial)

795 goto next_iteration;

796

797 if (loop-\>depth != orig_depth)

798 goto next_iteration;

799

800 \_dbus_assert (ready_fds\[i\].flags != 0);

801

802 if (\_DBUS_UNLIKELY (ready_fds\[i\].flags & \_DBUS_WATCH_NVAL))

803 {

804 cull_watches_for_invalid_fd (loop, ready_fds\[i\].fd);

805 goto next_iteration;

806 }

807

808 condition = ready_fds\[i\].flags;

809 \_dbus_assert ((condition & \_DBUS_WATCH_NVAL) == 0);

810

811 /\* condition may still be 0 if we got some

812 \* weird POLLFOO thing like POLLWRBAND

813 \*/

814 if (condition == 0)

815 continue;

816

817 watches = \_dbus_hash_table_lookup_pollable (loop-\>watches,

818 ready_fds\[i\].fd);

819

820 if (watches == NULL)

821 continue;

822

823 any_oom = FALSE;

824

825 for (link = \_dbus_list_get_first_link (watches);

826 link != NULL;

827 link = next)

828 {

829 DBusWatch \*watch = link-\>data;

830

831 next = \_dbus_list_get_next_link (watches, link);

832

833 if (dbus_watch_get_enabled (watch))

834 {

835 dbus_bool_t oom;

836

837 oom = !dbus_watch_handle (watch, condition);

838

839 if (oom)

840 {

841 \_dbus_watch_set_oom_last_time (watch, TRUE);

842 loop-\>oom_watch_pending = TRUE;

843 any_oom = TRUE;

844 }

845

846\#if MAINLOOP_SPEW

847 \_dbus_verbose (" Invoked watch, oom = %d\n", oom);

848\#endif

849 retval = TRUE;

850

851 /\* We re-check this every time, in case the callback

852 \* added/removed watches, which might make our position in

853 \* the linked list invalid. See the FIXME above. \*/

854 if (initial_serial != loop-\>callback_list_serial \|\|

855 loop-\>depth != orig_depth)

856 {

857 if (any_oom)

858 refresh_watches_for_fd (loop, NULL, ready_fds\[i\].fd);

859

860 goto next_iteration;

861 }

862 }

863 }

864

865 if (any_oom)

866 refresh_watches_for_fd (loop, watches, ready_fds\[i\].fd);

867 }

868 }

869

870 next_iteration:

871\#if MAINLOOP_SPEW

872 \_dbus_verbose (" moving to next iteration\n");

873\#endif

874

875 if (\_dbus_loop_dispatch (loop))

876 retval = TRUE;

877

878\#if MAINLOOP_SPEW

879 \_dbus_verbose ("Returning %d\n", retval);

880\#endif

881

882 return retval;

883}

884

885void

886\_dbus_loop_run (DBusLoop \*loop)

887{

888 int our_exit_depth;

889

890 \_dbus_assert (loop-\>depth \>= 0);

891

892 \_dbus_loop_ref (loop);

893

894 our_exit_depth = loop-\>depth;

895 loop-\>depth += 1;

896

897 \_dbus_verbose ("Running main loop, depth %d -\> %d\n",

898 loop-\>depth - 1, loop-\>depth);

899

900 while (loop-\>depth != our_exit_depth)

901 \_dbus_loop_iterate (loop, TRUE);

902

903 \_dbus_loop_unref (loop);

904}

905

906void

907\_dbus_loop_quit (DBusLoop \*loop)

908{

909 \_dbus_assert (loop-\>depth \> 0);

910

911 loop-\>depth -= 1;

912

913 \_dbus_verbose ("Quit main loop, depth %d -\> %d\n",

914 loop-\>depth + 1, loop-\>depth);

915}

916

917int

918\_dbus_get_oom_wait (void)

919{

920\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

921 /\* make tests go fast \*/

922 return 0;

923\#else

924 return 500;

925\#endif

926}

927

928void

929\_dbus_wait_for_memory (void)

930{

931 \_dbus_verbose ("Waiting for more memory\n");

932 \_dbus_sleep_milliseconds (\_dbus_get_oom_wait ());

933}

934

935\#endif /\* !DOXYGEN_SHOULD_SKIP_THIS \*/

dbus_connection_unref

void dbus_connection_unref(DBusConnection \*connection)

Decrements the reference count of a DBusConnection, and finalizes it if the count reaches zero.

**Definition** dbus-connection.c:2832

dbus_connection_dispatch

DBusDispatchStatus dbus_connection_dispatch(DBusConnection \*connection)

Processes any incoming data.

**Definition** dbus-connection.c:4591

DBusDispatchStatus

DBusDispatchStatus

Indicates the status of incoming data on a DBusConnection.

**Definition** dbus-connection.h:83

dbus_connection_ref

DBusConnection \* dbus_connection_ref(DBusConnection \*connection)

Increments the reference count of a DBusConnection.

**Definition** dbus-connection.c:2700

DBUS_DISPATCH_NEED_MEMORY

@ DBUS_DISPATCH_NEED_MEMORY

More memory is needed to continue.

**Definition** dbus-connection.h:86

DBUS_DISPATCH_COMPLETE

@ DBUS_DISPATCH_COMPLETE

All currently available data has been processed.

**Definition** dbus-connection.h:85

\_dbus_hash_table_get_n_entries

int \_dbus_hash_table_get_n_entries(DBusHashTable \*table)

Gets the number of hash entries in a hash table.

**Definition** dbus-hash.c:1461

\_dbus_hash_iter_get_value

void \* \_dbus_hash_iter_get_value(DBusHashIter \*iter)

Gets the value of the current entry.

**Definition** dbus-hash.c:620

\_dbus_hash_table_unref

void \_dbus_hash_table_unref(DBusHashTable \*table)

Decrements the reference count for a hash table, freeing the hash table if the count reaches zero.

**Definition** dbus-hash.c:368

\_dbus_hash_iter_next

dbus_bool_t \_dbus_hash_iter_next(DBusHashIter \*iter)

Move the hash iterator forward one step, to the next hash entry.

**Definition** dbus-hash.c:550

\_dbus_hash_iter_init

void \_dbus_hash_iter_init(DBusHashTable \*table, DBusHashIter \*iter)

Initializes a hash table iterator.

**Definition** dbus-hash.c:524

\_dbus_hash_table_new

DBusHashTable \* \_dbus_hash_table_new(DBusHashType type, DBusFreeFunction key_free_function, DBusFreeFunction value_free_function)

Constructs a new hash table.

**Definition** dbus-hash.c:292

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_DBUS_INT_MAX

\#define \_DBUS_INT_MAX

Maximum value of type "int".

**Definition** dbus-internals.h:327

\_dbus_warn

void \_dbus_warn(const char \*format,...)

Prints a warning message to stderr.

**Definition** dbus-internals.c:278

\_DBUS_N_ELEMENTS

\#define \_DBUS_N_ELEMENTS(array)

Computes the number of elements in a fixed-size array using sizeof().

**Definition** dbus-internals.h:189

\_dbus_list_get_first_link

DBusList \* \_dbus_list_get_first_link(DBusList \*\*list)

Gets the first link in the list.

**Definition** dbus-list.c:597

\_dbus_list_length_is_one

dbus_bool_t \_dbus_list_length_is_one(DBusList \*\*list)

Check whether length is exactly one.

**Definition** dbus-list.c:813

\_dbus_list_remove_link

void \_dbus_list_remove_link(DBusList \*\*list, DBusList \*link)

Removes a link from the list.

**Definition** dbus-list.c:530

\_dbus_list_pop_first

void \* \_dbus_list_pop_first(DBusList \*\*list)

Removes the first value in the list and returns it.

**Definition** dbus-list.c:679

\_dbus_list_get_length

int \_dbus_list_get_length(DBusList \*\*list)

Gets the length of a list.

**Definition** dbus-list.c:760

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

dbus_new

\#define dbus_new(type, count)

Safe macro for using dbus_malloc().

**Definition** dbus-memory.h:59

dbus_new0

\#define dbus_new0(type, count)

Safe macro for using dbus_malloc0().

**Definition** dbus-memory.h:60

\_dbus_get_monotonic_time

void \_dbus_get_monotonic_time(dbus_int64_t \*tv_sec, long \*tv_usec)

Get current time, as in gettimeofday().

**Definition** dbus-sysdeps-unix.c:3381

\_dbus_sleep_milliseconds

void \_dbus_sleep_milliseconds(int milliseconds)

Sleeps the given number of milliseconds.

**Definition** dbus-sysdeps-unix.c:3542

\_dbus_timeout_restarted

void \_dbus_timeout_restarted(DBusTimeout \*timeout)

Mark timeout as restarted (setting timestamps is responsibility of the event loop).

**Definition** dbus-timeout.c:401

\_dbus_timeout_needs_restart

dbus_bool_t \_dbus_timeout_needs_restart(DBusTimeout \*timeout)

Returns whether a timeout needs restart time counting in the event loop.

**Definition** dbus-timeout.c:389

dbus_timeout_handle

DBUS_EXPORT dbus_bool_t dbus_timeout_handle(DBusTimeout \*timeout)

Calls the timeout handler for this timeout.

**Definition** dbus-timeout.c:500

dbus_timeout_get_enabled

DBUS_EXPORT dbus_bool_t dbus_timeout_get_enabled(DBusTimeout \*timeout)

Returns whether a timeout is enabled or not.

**Definition** dbus-timeout.c:514

dbus_timeout_get_interval

DBUS_EXPORT int dbus_timeout_get_interval(DBusTimeout \*timeout)

Gets the timeout interval.

**Definition** dbus-timeout.c:444

\_dbus_watch_ref

DBusWatch \* \_dbus_watch_ref(DBusWatch \*watch)

Increments the reference count of a DBusWatch object.

**Definition** dbus-watch.c:126

\_dbus_watch_unref

void \_dbus_watch_unref(DBusWatch \*watch)

Decrements the reference count of a DBusWatch object and finalizes the object if the count reaches ze...

**Definition** dbus-watch.c:140

\_dbus_watch_invalidate

void \_dbus_watch_invalidate(DBusWatch \*watch)

Clears the file descriptor from a now-invalid watch object so that no one tries to use it.

**Definition** dbus-watch.c:171

dbus_watch_handle

DBUS_EXPORT dbus_bool_t dbus_watch_handle(DBusWatch \*watch, unsigned int flags)

Called to notify the D-Bus library when a previously-added watch is ready for reading or writing,...

**Definition** dbus-watch.c:735

dbus_watch_get_enabled

DBUS_EXPORT dbus_bool_t dbus_watch_get_enabled(DBusWatch \*watch)

Returns whether a watch is enabled or not.

**Definition** dbus-watch.c:704

dbus_watch_get_flags

DBUS_EXPORT unsigned int dbus_watch_get_flags(DBusWatch \*watch)

Gets flags from DBusWatchFlags indicating what conditions should be monitored on the file descriptor.

**Definition** dbus-watch.c:644

DBusConnection

Implementation details of DBusConnection.

**Definition** dbus-connection.c:259

DBusHashIter

Hash iterator object.

**Definition** dbus-hash.h:50

DBusHashTable

Internals of DBusHashTable.

**Definition** dbus-hash.c:175

DBusList

A node in a linked list.

**Definition** dbus-list.h:37

DBusList::data

void \* data

Data stored at this element.

**Definition** dbus-list.h:40

DBusTimeout

Internals of DBusTimeout.

**Definition** dbus-timeout.c:43

DBusWatch

Implementation of DBusWatch.

**Definition** dbus-watch.c:43
