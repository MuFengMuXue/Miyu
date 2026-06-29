dbus-connection.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-connection.c DBusConnection object

3 \*

4 \* Copyright (C) 2002-2006 Red Hat Inc.

5 \*

6 \* SPDX-License-Identifier: AFL-2.1 OR GPL-2.0-or-later

7 \*

8 \* Licensed under the Academic Free License version 2.1

9 \*

10 \* This program is free software; you can redistribute it and/or modify

11 \* it under the terms of the GNU General Public License as published by

12 \* the Free Software Foundation; either version 2 of the License, or

13 \* (at your option) any later version.

14 \*

15 \* This program is distributed in the hope that it will be useful,

16 \* but WITHOUT ANY WARRANTY; without even the implied warranty of

17 \* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the

18 \* GNU General Public License for more details.

19 \*

20 \* You should have received a copy of the GNU General Public License

21 \* along with this program; if not, write to the Free Software

22 \* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

23 \*

24 \*/

25

26\#include \<config.h\>

27\#include "dbus-shared.h"

28\#include "dbus-connection.h"

29\#include "dbus-list.h"

30\#include "dbus-timeout.h"

31\#include "dbus-transport.h"

32\#include "dbus-watch.h"

33\#include "dbus-connection-internal.h"

34\#include "dbus-pending-call-internal.h"

35\#include "dbus-list.h"

36\#include "dbus-hash.h"

37\#include "dbus-message-internal.h"

38\#include "dbus-message-private.h"

39\#include "dbus-threads.h"

40\#include "dbus-protocol.h"

41\#include "dbus-dataslot.h"

42\#include "dbus-string.h"

43\#include "dbus-signature.h"

44\#include "dbus-pending-call.h"

45\#include "dbus-object-tree.h"

46\#include "dbus-threads-internal.h"

47\#include "dbus-bus.h"

48\#include "dbus-marshal-basic.h"

49

50\#ifdef DBUS_DISABLE_CHECKS

51\#define TOOK_LOCK_CHECK(connection)

52\#define RELEASING_LOCK_CHECK(connection)

53\#define HAVE_LOCK_CHECK(connection)

54\#else

55\#define TOOK_LOCK_CHECK(connection) do { \\

56 \_dbus_assert (!(connection)-\>have_connection_lock); \\

57 (connection)-\>have_connection_lock = TRUE; \\

58 } while (0)

59\#define RELEASING_LOCK_CHECK(connection) do { \\

60 \_dbus_assert ((connection)-\>have_connection_lock); \\

61 (connection)-\>have_connection_lock = FALSE; \\

62 } while (0)

63\#define HAVE_LOCK_CHECK(connection) \_dbus_assert ((connection)-\>have_connection_lock)

64/\* A "DO_NOT_HAVE_LOCK_CHECK" is impossible since we need the lock to check the flag \*/

65\#endif

66

67\#define TRACE_LOCKS 1

68

69\#define CONNECTION_LOCK(connection) do { \\

70 if (TRACE_LOCKS) { \_dbus_verbose ("LOCK\n"); } \\

71 \_dbus_rmutex_lock ((connection)-\>mutex); \\

72 TOOK_LOCK_CHECK (connection); \\

73 } while (0)

74

75\#define CONNECTION_UNLOCK(connection) \_dbus_connection_unlock (connection)

76

77\#define SLOTS_LOCK(connection) do { \\

78 \_dbus_rmutex_lock ((connection)-\>slot_mutex); \\

79 } while (0)

80

81\#define SLOTS_UNLOCK(connection) do { \\

82 \_dbus_rmutex_unlock ((connection)-\>slot_mutex); \\

83 } while (0)

84

85\#define DISPATCH_STATUS_NAME(s) \\

86 ((s) == DBUS_DISPATCH_COMPLETE ? "complete" : \\

87 (s) == DBUS_DISPATCH_DATA_REMAINS ? "data remains" : \\

88 (s) == DBUS_DISPATCH_NEED_MEMORY ? "need memory" : \\

89 "???")

90

208static void

209\_dbus_connection_trace_ref (DBusConnection \*connection,

210 int old_refcount,

211 int new_refcount,

212 const char \*why)

213{

214\#ifdef DBUS_ENABLE_VERBOSE_MODE

215 static int enabled = -1;

216

217 \_dbus_trace_ref ("DBusConnection", connection, old_refcount, new_refcount,

218 why, "DBUS_CONNECTION_TRACE", &enabled);

219\#endif

220}

221

225typedef struct DBusMessageFilter DBusMessageFilter;

226

230struct DBusMessageFilter

231{

232 DBusAtomic refcount;

233 DBusHandleMessageFunction function;

234 void \*user_data;

235 DBusFreeFunction free_user_data_function;

236};

237

238

242struct DBusPreallocatedSend

243{

244 DBusConnection \*connection;

245 DBusList \*queue_link;

246 DBusList \*counter_link;

247};

248

249\#if HAVE_DECL_MSG_NOSIGNAL

250static DBusAtomic \_dbus_modify_sigpipe = { FALSE };

251\#else

252static DBusAtomic \_dbus_modify_sigpipe = { TRUE };

253\#endif

254

258struct DBusConnection

259{

260 DBusAtomic refcount;

262 DBusRMutex \*mutex;

264 DBusCMutex \*dispatch_mutex;

265 DBusCondVar \*dispatch_cond;

266 DBusCMutex \*io_path_mutex;

267 DBusCondVar \*io_path_cond;

269 DBusList \*outgoing_messages;

270 DBusList \*incoming_messages;

271 DBusList \*expired_messages;

273 DBusMessage \*message_borrowed;

277 int n_outgoing;

278 int n_incoming;

280 DBusCounter \*outgoing_counter;

282 DBusTransport \*transport;

283 DBusWatchList \*watches;

284 DBusTimeoutList \*timeouts;

286 DBusList \*filter_list;

288 DBusRMutex \*slot_mutex;

289 DBusDataSlotList slot_list;

291 DBusHashTable \*pending_replies;

293 dbus_uint32_t client_serial;

294 DBusList \*disconnect_message_link;

296 DBusWakeupMainFunction wakeup_main_function;

297 void \*wakeup_main_data;

298 DBusFreeFunction free_wakeup_main_data;

300 DBusDispatchStatusFunction dispatch_status_function;

301 void \*dispatch_status_data;

302 DBusFreeFunction free_dispatch_status_data;

304 DBusDispatchStatus last_dispatch_status;

306 DBusObjectTree \*objects;

308 char \*server_guid;

310 /\* These two MUST be bools and not bitfields, because they are protected by a separate lock

311 \* from connection-\>mutex and all bitfields in a word have to be read/written together.

312 \* So you can't have a different lock for different bitfields in the same word.

313 \*/

314 dbus_bool_t dispatch_acquired;

315 dbus_bool_t io_path_acquired;

317 unsigned int shareable : 1;

319 unsigned int exit_on_disconnect : 1;

321 unsigned int builtin_filters_enabled : 1;

323 unsigned int route_peer_messages : 1;

325 unsigned int disconnected_message_arrived : 1;

329 unsigned int disconnected_message_processed : 1;

333\#ifndef DBUS_DISABLE_CHECKS

334 unsigned int have_connection_lock : 1;

335\#endif

336

337\#if defined(DBUS_ENABLE_CHECKS) \|\| defined(DBUS_ENABLE_ASSERT)

338 int generation;

339\#endif

340};

341

342static DBusDispatchStatus \_dbus_connection_get_dispatch_status_unlocked (DBusConnection \*connection);

343static void \_dbus_connection_update_dispatch_status_and_unlock (DBusConnection \*connection,

344 DBusDispatchStatus new_status);

345static void \_dbus_connection_last_unref (DBusConnection \*connection);

346static void \_dbus_connection_acquire_dispatch (DBusConnection \*connection);

347static void \_dbus_connection_release_dispatch (DBusConnection \*connection);

348static DBusDispatchStatus \_dbus_connection_flush_unlocked (DBusConnection \*connection);

349static void \_dbus_connection_close_possibly_shared_and_unlock (DBusConnection \*connection);

350static dbus_bool_t \_dbus_connection_get_is_connected_unlocked (DBusConnection \*connection);

351static dbus_bool_t \_dbus_connection_peek_for_reply_unlocked (DBusConnection \*connection,

352 dbus_uint32_t client_serial);

353

354static DBusMessageFilter \*

355\_dbus_message_filter_ref (DBusMessageFilter \*filter)

356{

357\#ifdef DBUS_DISABLE_ASSERT

358 \_dbus_atomic_inc (&filter-\>refcount);

359\#else

360 dbus_int32_t old_value;

361

362 old_value = \_dbus_atomic_inc (&filter-\>refcount);

363 \_dbus_assert (old_value \> 0);

364\#endif

365

366 return filter;

367}

368

369static void

370\_dbus_message_filter_unref (DBusMessageFilter \*filter)

371{

372 dbus_int32_t old_value;

373

374 old_value = \_dbus_atomic_dec (&filter-\>refcount);

375 \_dbus_assert (old_value \> 0);

376

377 if (old_value == 1)

378 {

379 if (filter-\>free_user_data_function)

380 (\* filter-\>free_user_data_function) (filter-\>user_data);

381

382 dbus_free (filter);

383 }

384}

385

391void

392\_dbus_connection_lock (DBusConnection \*connection)

393{

394 CONNECTION_LOCK (connection);

395}

396

402void

403\_dbus_connection_unlock (DBusConnection \*connection)

404{

405 DBusList \*expired_messages;

406 DBusList \*iter;

407

408 if (TRACE_LOCKS)

409 {

410 \_dbus_verbose ("UNLOCK\n");

411 }

412

413 /\* If we had messages that expired (fell off the incoming or outgoing

414 \* queues) while we were locked, actually release them now \*/

415 expired_messages = connection-\>expired_messages;

416 connection-\>expired_messages = NULL;

417

418 RELEASING_LOCK_CHECK (connection);

419 \_dbus_rmutex_unlock (connection-\>mutex);

420

421 for (iter = \_dbus_list_pop_first_link (&expired_messages);

422 iter != NULL;

423 iter = \_dbus_list_pop_first_link (&expired_messages))

424 {

425 DBusMessage \*message = iter-\>data;

426

427 dbus_message_unref (message);

428 \_dbus_list_free_link (iter);

429 }

430}

431

439static void

440\_dbus_connection_wakeup_mainloop (DBusConnection \*connection)

441{

442 if (connection-\>wakeup_main_function)

443 (\*connection-\>wakeup_main_function) (connection-\>wakeup_main_data);

444}

445

446\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

459void

460\_dbus_connection_test_get_locks (DBusConnection \*connection,

461 DBusMutex \*\*mutex_loc,

462 DBusMutex \*\*dispatch_mutex_loc,

463 DBusMutex \*\*io_path_mutex_loc,

464 DBusCondVar \*\*dispatch_cond_loc,

465 DBusCondVar \*\*io_path_cond_loc)

466{

467 \*mutex_loc = (DBusMutex \*) connection-\>mutex;

468 \*dispatch_mutex_loc = (DBusMutex \*) connection-\>dispatch_mutex;

469 \*io_path_mutex_loc = (DBusMutex \*) connection-\>io_path_mutex;

470 \*dispatch_cond_loc = connection-\>dispatch_cond;

471 \*io_path_cond_loc = connection-\>io_path_cond;

472}

473\#endif

474

483void

484\_dbus_connection_queue_received_message_link (DBusConnection \*connection,

485 DBusList \*link)

486{

487 DBusPendingCall \*pending;

488 dbus_uint32_t reply_serial;

489 DBusMessage \*message;

490

491 \_dbus_assert (\_dbus_transport_peek_is_authenticated (connection-\>transport));

492

493 \_dbus_list_append_link (&connection-\>incoming_messages,

494 link);

495 message = link-\>data;

496

497 /\* If this is a reply we're waiting on, remove timeout for it \*/

498 reply_serial = dbus_message_get_reply_serial (message);

499 if (reply_serial != 0)

500 {

501 pending = \_dbus_hash_table_lookup_int (connection-\>pending_replies,

502 reply_serial);

503 if (pending != NULL)

504 {

505 if (\_dbus_pending_call_is_timeout_added_unlocked (pending))

506 \_dbus_connection_remove_timeout_unlocked (connection,

507 \_dbus_pending_call_get_timeout_unlocked (pending));

508

509 \_dbus_pending_call_set_timeout_added_unlocked (pending, FALSE);

510 }

511 }

512

513

514

515 connection-\>n_incoming += 1;

516

517 \_dbus_connection_wakeup_mainloop (connection);

518

519 \_dbus_verbose ("Message %p (%s %s %s %s '%s' reply to %u) added to incoming queue %p, %d incoming\n",

520 message,

521 dbus_message_type_to_string (dbus_message_get_type (message)),

522 dbus_message_get_path (message) ?

523 dbus_message_get_path (message) :

524 "no path",

525 dbus_message_get_interface (message) ?

526 dbus_message_get_interface (message) :

527 "no interface",

528 dbus_message_get_member (message) ?

529 dbus_message_get_member (message) :

530 "no member",

531 dbus_message_get_signature (message),

532 dbus_message_get_reply_serial (message),

533 connection,

534 connection-\>n_incoming);

535

536 \_dbus_message_trace_ref (message, -1, -1,

537 "\_dbus_conection_queue_received_message_link");

538}

539

548void

549\_dbus_connection_queue_synthesized_message_link (DBusConnection \*connection,

550 DBusList \*link)

551{

552 HAVE_LOCK_CHECK (connection);

553

554 \_dbus_list_append_link (&connection-\>incoming_messages, link);

555

556 connection-\>n_incoming += 1;

557

558 \_dbus_connection_wakeup_mainloop (connection);

559

560 \_dbus_message_trace_ref (link-\>data, -1, -1,

561 "\_dbus_connection_queue_synthesized_message_link");

562

563 \_dbus_verbose ("Synthesized message %p added to incoming queue %p, %d incoming\n",

564 link-\>data, connection, connection-\>n_incoming);

565}

566

567

575dbus_bool_t

576\_dbus_connection_has_messages_to_send_unlocked (DBusConnection \*connection)

577{

578 HAVE_LOCK_CHECK (connection);

579 return connection-\>outgoing_messages != NULL;

580}

581

591dbus_bool_t

592dbus_connection_has_messages_to_send (DBusConnection \*connection)

593{

594 dbus_bool_t v;

595

596 \_dbus_return_val_if_fail (connection != NULL, FALSE);

597

598 CONNECTION_LOCK (connection);

599 v = \_dbus_connection_has_messages_to_send_unlocked (connection);

600 CONNECTION_UNLOCK (connection);

601

602 return v;

603}

604

612DBusMessage\*

613\_dbus_connection_get_message_to_send (DBusConnection \*connection)

614{

615 HAVE_LOCK_CHECK (connection);

616

617 return \_dbus_list_get_last (&connection-\>outgoing_messages);

618}

619

628void

629\_dbus_connection_message_sent_unlocked (DBusConnection \*connection,

630 DBusMessage \*message)

631{

632 DBusList \*link;

633

634 HAVE_LOCK_CHECK (connection);

635

636 /\* This can be called before we even complete authentication, since

637 \* it's called on disconnect to clean up the outgoing queue.

638 \* It's also called as we successfully send each message.

639 \*/

640

641 link = \_dbus_list_get_last_link (&connection-\>outgoing_messages);

642 \_dbus_assert (link != NULL);

643 \_dbus_assert (link-\>data == message);

644

645 \_dbus_list_unlink (&connection-\>outgoing_messages,

646 link);

647 \_dbus_list_prepend_link (&connection-\>expired_messages, link);

648

649 connection-\>n_outgoing -= 1;

650

651 \_dbus_verbose ("Message %p (%s %s %s %s '%s') removed from outgoing queue %p, %d left to send\n",

652 message,

653 dbus_message_type_to_string (dbus_message_get_type (message)),

654 dbus_message_get_path (message) ?

655 dbus_message_get_path (message) :

656 "no path",

657 dbus_message_get_interface (message) ?

658 dbus_message_get_interface (message) :

659 "no interface",

660 dbus_message_get_member (message) ?

661 dbus_message_get_member (message) :

662 "no member",

663 dbus_message_get_signature (message),

664 connection, connection-\>n_outgoing);

665

666 /\* It's OK that in principle we call the notify function, because for the

667 \* outgoing limit, there isn't one \*/

668 \_dbus_message_remove_counter (message, connection-\>outgoing_counter);

669

670 /\* The message will actually be unreffed when we unlock \*/

671}

672

674typedef dbus_bool_t (\* DBusWatchAddFunction) (DBusWatchList \*list,

675 DBusWatch \*watch);

677typedef void (\* DBusWatchRemoveFunction) (DBusWatchList \*list,

678 DBusWatch \*watch);

680typedef void (\* DBusWatchToggleFunction) (DBusWatchList \*list,

681 DBusWatch \*watch,

682 dbus_bool_t enabled);

683

684static dbus_bool_t

685protected_change_watch (DBusConnection \*connection,

686 DBusWatch \*watch,

687 DBusWatchAddFunction add_function,

688 DBusWatchRemoveFunction remove_function,

689 DBusWatchToggleFunction toggle_function,

690 dbus_bool_t enabled)

691{

692 dbus_bool_t retval;

693

694 HAVE_LOCK_CHECK (connection);

695

696 /\* The original purpose of protected_change_watch() was to hold a

697 \* ref on the connection while dropping the connection lock, then

698 \* calling out to the app. This was a broken hack that did not

699 \* work, since the connection was in a hosed state (no WatchList

700 \* field) while calling out.

701 \*

702 \* So for now we'll just keep the lock while calling out. This means

703 \* apps are not allowed to call DBusConnection methods inside a

704 \* watch function or they will deadlock.

705 \*

706 \* The "real fix" is to use the \_and_unlock() pattern found

707 \* elsewhere in the code, to defer calling out to the app until

708 \* we're about to drop locks and return flow of control to the app

709 \* anyway.

710 \*

711 \* See http://lists.freedesktop.org/archives/dbus/2007-July/thread.html#8144

712 \*/

713

714 if (connection-\>watches)

715 {

716 if (add_function)

717 retval = (\* add_function) (connection-\>watches, watch);

718 else if (remove_function)

719 {

720 retval = TRUE;

721 (\* remove_function) (connection-\>watches, watch);

722 }

723 else

724 {

725 retval = TRUE;

726 (\* toggle_function) (connection-\>watches, watch, enabled);

727 }

728 return retval;

729 }

730 else

731 return FALSE;

732}

733

734

746dbus_bool_t

747\_dbus_connection_add_watch_unlocked (DBusConnection \*connection,

748 DBusWatch \*watch)

749{

750 return protected_change_watch (connection, watch,

751 \_dbus_watch_list_add_watch,

752 NULL, NULL, FALSE);

753}

754

764void

765\_dbus_connection_remove_watch_unlocked (DBusConnection \*connection,

766 DBusWatch \*watch)

767{

768 protected_change_watch (connection, watch,

769 NULL,

770 \_dbus_watch_list_remove_watch,

771 NULL, FALSE);

772}

773

784void

785\_dbus_connection_toggle_watch_unlocked (DBusConnection \*connection,

786 DBusWatch \*watch,

787 dbus_bool_t enabled)

788{

789 \_dbus_assert (watch != NULL);

790

791 protected_change_watch (connection, watch,

792 NULL, NULL,

793 \_dbus_watch_list_toggle_watch,

794 enabled);

795}

796

798typedef dbus_bool_t (\* DBusTimeoutAddFunction) (DBusTimeoutList \*list,

799 DBusTimeout \*timeout);

801typedef void (\* DBusTimeoutRemoveFunction) (DBusTimeoutList \*list,

802 DBusTimeout \*timeout);

804typedef void (\* DBusTimeoutToggleFunction) (DBusTimeoutList \*list,

805 DBusTimeout \*timeout,

806 dbus_bool_t enabled);

807

808static dbus_bool_t

809protected_change_timeout (DBusConnection \*connection,

810 DBusTimeout \*timeout,

811 DBusTimeoutAddFunction add_function,

812 DBusTimeoutRemoveFunction remove_function,

813 DBusTimeoutToggleFunction toggle_function,

814 dbus_bool_t enabled)

815{

816 dbus_bool_t retval;

817

818 HAVE_LOCK_CHECK (connection);

819

820 /\* The original purpose of protected_change_timeout() was to hold a

821 \* ref on the connection while dropping the connection lock, then

822 \* calling out to the app. This was a broken hack that did not

823 \* work, since the connection was in a hosed state (no TimeoutList

824 \* field) while calling out.

825 \*

826 \* So for now we'll just keep the lock while calling out. This means

827 \* apps are not allowed to call DBusConnection methods inside a

828 \* timeout function or they will deadlock.

829 \*

830 \* The "real fix" is to use the \_and_unlock() pattern found

831 \* elsewhere in the code, to defer calling out to the app until

832 \* we're about to drop locks and return flow of control to the app

833 \* anyway.

834 \*

835 \* See http://lists.freedesktop.org/archives/dbus/2007-July/thread.html#8144

836 \*/

837

838 if (connection-\>timeouts)

839 {

840 if (add_function)

841 retval = (\* add_function) (connection-\>timeouts, timeout);

842 else if (remove_function)

843 {

844 retval = TRUE;

845 (\* remove_function) (connection-\>timeouts, timeout);

846 }

847 else

848 {

849 retval = TRUE;

850 (\* toggle_function) (connection-\>timeouts, timeout, enabled);

851 }

852 return retval;

853 }

854 else

855 return FALSE;

856}

857

870dbus_bool_t

871\_dbus_connection_add_timeout_unlocked (DBusConnection \*connection,

872 DBusTimeout \*timeout)

873{

874 return protected_change_timeout (connection, timeout,

875 \_dbus_timeout_list_add_timeout,

876 NULL, NULL, FALSE);

877}

878

888void

889\_dbus_connection_remove_timeout_unlocked (DBusConnection \*connection,

890 DBusTimeout \*timeout)

891{

892 protected_change_timeout (connection, timeout,

893 NULL,

894 \_dbus_timeout_list_remove_timeout,

895 NULL, FALSE);

896}

897

908void

909\_dbus_connection_toggle_timeout_unlocked (DBusConnection \*connection,

910 DBusTimeout \*timeout,

911 dbus_bool_t enabled)

912{

913 protected_change_timeout (connection, timeout,

914 NULL, NULL,

915 \_dbus_timeout_list_toggle_timeout,

916 enabled);

917}

918

919static dbus_bool_t

920\_dbus_connection_attach_pending_call_unlocked (DBusConnection \*connection,

921 DBusPendingCall \*pending)

922{

923 dbus_uint32_t reply_serial;

924 DBusTimeout \*timeout;

925

926 HAVE_LOCK_CHECK (connection);

927

928 reply_serial = \_dbus_pending_call_get_reply_serial_unlocked (pending);

929

930 \_dbus_assert (reply_serial != 0);

931

932 timeout = \_dbus_pending_call_get_timeout_unlocked (pending);

933

934 if (timeout)

935 {

936 if (!\_dbus_connection_add_timeout_unlocked (connection, timeout))

937 return FALSE;

938

939 if (!\_dbus_hash_table_insert_int (connection-\>pending_replies,

940 reply_serial,

941 pending))

942 {

943 \_dbus_connection_remove_timeout_unlocked (connection, timeout);

944

945 \_dbus_pending_call_set_timeout_added_unlocked (pending, FALSE);

946 HAVE_LOCK_CHECK (connection);

947 return FALSE;

948 }

949

950 \_dbus_pending_call_set_timeout_added_unlocked (pending, TRUE);

951 }

952 else

953 {

954 if (!\_dbus_hash_table_insert_int (connection-\>pending_replies,

955 reply_serial,

956 pending))

957 {

958 HAVE_LOCK_CHECK (connection);

959 return FALSE;

960 }

961 }

962

963 \_dbus_pending_call_ref_unlocked (pending);

964

965 HAVE_LOCK_CHECK (connection);

966

967 return TRUE;

968}

969

970static void

971free_pending_call_on_hash_removal (void \*data)

972{

973 DBusPendingCall \*pending;

974 DBusConnection \*connection;

975

976 if (data == NULL)

977 return;

978

979 pending = data;

980

981 connection = \_dbus_pending_call_get_connection_unlocked (pending);

982

983 HAVE_LOCK_CHECK (connection);

984

985 if (\_dbus_pending_call_is_timeout_added_unlocked (pending))

986 {

987 \_dbus_connection_remove_timeout_unlocked (connection,

988 \_dbus_pending_call_get_timeout_unlocked (pending));

989

990 \_dbus_pending_call_set_timeout_added_unlocked (pending, FALSE);

991 }

992

993 /\* FIXME 1.0? this is sort of dangerous and undesirable to drop the lock

994 \* here, but the pending call finalizer could in principle call out to

995 \* application code so we pretty much have to... some larger code reorg

996 \* might be needed.

997 \*/

998 \_dbus_connection_ref_unlocked (connection);

999 \_dbus_pending_call_unref_and_unlock (pending);

1000 CONNECTION_LOCK (connection);

1001 \_dbus_connection_unref_unlocked (connection);

1002}

1003

1004static void

1005\_dbus_connection_detach_pending_call_unlocked (DBusConnection \*connection,

1006 DBusPendingCall \*pending)

1007{

1008 /\* This ends up unlocking to call the pending call finalizer, which is unexpected to

1009 \* say the least.

1010 \*/

1011 \_dbus_hash_table_remove_int (connection-\>pending_replies,

1012 \_dbus_pending_call_get_reply_serial_unlocked (pending));

1013}

1014

1015static void

1016\_dbus_connection_detach_pending_call_and_unlock (DBusConnection \*connection,

1017 DBusPendingCall \*pending)

1018{

1019 /\* The idea here is to avoid finalizing the pending call

1020 \* with the lock held, since there's a destroy notifier

1021 \* in pending call that goes out to application code.

1022 \*

1023 \* There's an extra unlock inside the hash table

1024 \* "free pending call" function FIXME...

1025 \*/

1026 \_dbus_pending_call_ref_unlocked (pending);

1027 \_dbus_hash_table_remove_int (connection-\>pending_replies,

1028 \_dbus_pending_call_get_reply_serial_unlocked (pending));

1029

1030 if (\_dbus_pending_call_is_timeout_added_unlocked (pending))

1031 \_dbus_connection_remove_timeout_unlocked (connection,

1032 \_dbus_pending_call_get_timeout_unlocked (pending));

1033

1034 \_dbus_pending_call_set_timeout_added_unlocked (pending, FALSE);

1035

1036 \_dbus_pending_call_unref_and_unlock (pending);

1037}

1038

1047void

1048\_dbus_connection_remove_pending_call (DBusConnection \*connection,

1049 DBusPendingCall \*pending)

1050{

1051 CONNECTION_LOCK (connection);

1052 \_dbus_connection_detach_pending_call_and_unlock (connection, pending);

1053}

1054

1064static dbus_bool_t

1065\_dbus_connection_acquire_io_path (DBusConnection \*connection,

1066 int timeout_milliseconds)

1067{

1068 dbus_bool_t we_acquired;

1069

1070 HAVE_LOCK_CHECK (connection);

1071

1072 /\* We don't want the connection to vanish \*/

1073 \_dbus_connection_ref_unlocked (connection);

1074

1075 /\* We will only touch io_path_acquired which is protected by our mutex \*/

1076 CONNECTION_UNLOCK (connection);

1077

1078 \_dbus_verbose ("locking io_path_mutex\n");

1079 \_dbus_cmutex_lock (connection-\>io_path_mutex);

1080

1081 \_dbus_verbose ("start connection-\>io_path_acquired = %d timeout = %d\n",

1082 connection-\>io_path_acquired, timeout_milliseconds);

1083

1084 we_acquired = FALSE;

1085

1086 if (connection-\>io_path_acquired)

1087 {

1088 if (timeout_milliseconds != -1)

1089 {

1090 \_dbus_verbose ("waiting %d for IO path to be acquirable\n",

1091 timeout_milliseconds);

1092

1093 if (!\_dbus_condvar_wait_timeout (connection-\>io_path_cond,

1094 connection-\>io_path_mutex,

1095 timeout_milliseconds))

1096 {

1097 /\* We timed out before anyone signaled. \*/

1098 /\* (writing the loop to handle the !timedout case by

1099 \* waiting longer if needed is a pain since dbus

1100 \* wraps pthread_cond_timedwait to take a relative

1101 \* time instead of absolute, something kind of stupid

1102 \* on our part. for now it doesn't matter, we will just

1103 \* end up back here eventually.)

1104 \*/

1105 }

1106 }

1107 else

1108 {

1109 while (connection-\>io_path_acquired)

1110 {

1111 \_dbus_verbose ("waiting for IO path to be acquirable\n");

1112 \_dbus_condvar_wait (connection-\>io_path_cond,

1113 connection-\>io_path_mutex);

1114 }

1115 }

1116 }

1117

1118 if (!connection-\>io_path_acquired)

1119 {

1120 we_acquired = TRUE;

1121 connection-\>io_path_acquired = TRUE;

1122 }

1123

1124 \_dbus_verbose ("end connection-\>io_path_acquired = %d we_acquired = %d\n",

1125 connection-\>io_path_acquired, we_acquired);

1126

1127 \_dbus_verbose ("unlocking io_path_mutex\n");

1128 \_dbus_cmutex_unlock (connection-\>io_path_mutex);

1129

1130 CONNECTION_LOCK (connection);

1131

1132 HAVE_LOCK_CHECK (connection);

1133

1134 \_dbus_connection_unref_unlocked (connection);

1135

1136 return we_acquired;

1137}

1138

1146static void

1147\_dbus_connection_release_io_path (DBusConnection \*connection)

1148{

1149 HAVE_LOCK_CHECK (connection);

1150

1151 \_dbus_verbose ("locking io_path_mutex\n");

1152 \_dbus_cmutex_lock (connection-\>io_path_mutex);

1153

1154 \_dbus_assert (connection-\>io_path_acquired);

1155

1156 \_dbus_verbose ("start connection-\>io_path_acquired = %d\n",

1157 connection-\>io_path_acquired);

1158

1159 connection-\>io_path_acquired = FALSE;

1160 \_dbus_condvar_wake_one (connection-\>io_path_cond);

1161

1162 \_dbus_verbose ("unlocking io_path_mutex\n");

1163 \_dbus_cmutex_unlock (connection-\>io_path_mutex);

1164}

1165

1201void

1202\_dbus_connection_do_iteration_unlocked (DBusConnection \*connection,

1203 DBusPendingCall \*pending,

1204 unsigned int flags,

1205 int timeout_milliseconds)

1206{

1207 \_dbus_verbose ("start\n");

1208

1209 HAVE_LOCK_CHECK (connection);

1210

1211 if (connection-\>n_outgoing == 0)

1212 flags &= ~DBUS_ITERATION_DO_WRITING;

1213

1214 if (\_dbus_connection_acquire_io_path (connection,

1215 (flags & DBUS_ITERATION_BLOCK) ? timeout_milliseconds : 0))

1216 {

1217 HAVE_LOCK_CHECK (connection);

1218

1219 if ( (pending != NULL) && \_dbus_pending_call_get_completed_unlocked(pending))

1220 {

1221 \_dbus_verbose ("pending call completed while acquiring I/O path");

1222 }

1223 else if ( (pending != NULL) &&

1224 \_dbus_connection_peek_for_reply_unlocked (connection,

1225 \_dbus_pending_call_get_reply_serial_unlocked (pending)))

1226 {

1227 \_dbus_verbose ("pending call completed while acquiring I/O path (reply found in queue)");

1228 }

1229 else

1230 {

1231 \_dbus_transport_do_iteration (connection-\>transport,

1232 flags, timeout_milliseconds);

1233 }

1234

1235 \_dbus_connection_release_io_path (connection);

1236 }

1237

1238 HAVE_LOCK_CHECK (connection);

1239

1240 \_dbus_verbose ("end\n");

1241}

1242

1252DBusConnection\*

1253\_dbus_connection_new_for_transport (DBusTransport \*transport)

1254{

1255 DBusConnection \*connection;

1256 DBusWatchList \*watch_list;

1257 DBusTimeoutList \*timeout_list;

1258 DBusHashTable \*pending_replies;

1259 DBusList \*disconnect_link;

1260 DBusMessage \*disconnect_message;

1261 DBusCounter \*outgoing_counter;

1262 DBusObjectTree \*objects;

1263

1264 watch_list = NULL;

1265 connection = NULL;

1266 pending_replies = NULL;

1267 timeout_list = NULL;

1268 disconnect_link = NULL;

1269 disconnect_message = NULL;

1270 outgoing_counter = NULL;

1271 objects = NULL;

1272

1273 watch_list = \_dbus_watch_list_new ();

1274 if (watch_list == NULL)

1275 goto error;

1276

1277 timeout_list = \_dbus_timeout_list_new ();

1278 if (timeout_list == NULL)

1279 goto error;

1280

1281 pending_replies =

1282 \_dbus_hash_table_new (DBUS_HASH_INT,

1283 NULL,

1284 (DBusFreeFunction)free_pending_call_on_hash_removal);

1285 if (pending_replies == NULL)

1286 goto error;

1287

1288 connection = dbus_new0 (DBusConnection, 1);

1289 if (connection == NULL)

1290 goto error;

1291

1292 \_dbus_rmutex_new_at_location (&connection-\>mutex);

1293 if (connection-\>mutex == NULL)

1294 goto error;

1295

1296 \_dbus_cmutex_new_at_location (&connection-\>io_path_mutex);

1297 if (connection-\>io_path_mutex == NULL)

1298 goto error;

1299

1300 \_dbus_cmutex_new_at_location (&connection-\>dispatch_mutex);

1301 if (connection-\>dispatch_mutex == NULL)

1302 goto error;

1303

1304 \_dbus_condvar_new_at_location (&connection-\>dispatch_cond);

1305 if (connection-\>dispatch_cond == NULL)

1306 goto error;

1307

1308 \_dbus_condvar_new_at_location (&connection-\>io_path_cond);

1309 if (connection-\>io_path_cond == NULL)

1310 goto error;

1311

1312 \_dbus_rmutex_new_at_location (&connection-\>slot_mutex);

1313 if (connection-\>slot_mutex == NULL)

1314 goto error;

1315

1316 disconnect_message = dbus_message_new_signal (DBUS_PATH_LOCAL,

1317 DBUS_INTERFACE_LOCAL,

1318 "Disconnected");

1319

1320 if (disconnect_message == NULL)

1321 goto error;

1322

1323 disconnect_link = \_dbus_list_alloc_link (disconnect_message);

1324 if (disconnect_link == NULL)

1325 goto error;

1326

1327 outgoing_counter = \_dbus_counter_new ();

1328 if (outgoing_counter == NULL)

1329 goto error;

1330

1331 objects = \_dbus_object_tree_new (connection);

1332 if (objects == NULL)

1333 goto error;

1334

1335 if (\_dbus_atomic_get (&\_dbus_modify_sigpipe) != 0)

1336 \_dbus_disable_sigpipe ();

1337

1338 /\* initialized to 0: use atomic op to avoid mixing atomic and non-atomic \*/

1339 \_dbus_atomic_inc (&connection-\>refcount);

1340 connection-\>transport = transport;

1341 connection-\>watches = watch_list;

1342 connection-\>timeouts = timeout_list;

1343 connection-\>pending_replies = pending_replies;

1344 connection-\>outgoing_counter = outgoing_counter;

1345 connection-\>filter_list = NULL;

1346 connection-\>last_dispatch_status = DBUS_DISPATCH_COMPLETE; /\* so we're notified first time there's data \*/

1347 connection-\>objects = objects;

1348 connection-\>exit_on_disconnect = FALSE;

1349 connection-\>shareable = FALSE;

1350 connection-\>builtin_filters_enabled = TRUE;

1351 connection-\>route_peer_messages = FALSE;

1352 connection-\>disconnected_message_arrived = FALSE;

1353 connection-\>disconnected_message_processed = FALSE;

1354

1355\#if defined(DBUS_ENABLE_CHECKS) \|\| defined(DBUS_ENABLE_ASSERT)

1356 connection-\>generation = \_dbus_current_generation;

1357\#endif

1358

1359 \_dbus_data_slot_list_init (&connection-\>slot_list);

1360

1361 connection-\>client_serial = 1;

1362

1363 connection-\>disconnect_message_link = disconnect_link;

1364

1365 CONNECTION_LOCK (connection);

1366

1367 if (!\_dbus_transport_set_connection (transport, connection))

1368 {

1369 CONNECTION_UNLOCK (connection);

1370

1371 goto error;

1372 }

1373

1374 \_dbus_transport_ref (transport);

1375

1376 CONNECTION_UNLOCK (connection);

1377

1378 \_dbus_connection_trace_ref (connection, 0, 1, "new_for_transport");

1379 return connection;

1380

1381 error:

1382 if (disconnect_message != NULL)

1383 dbus_message_unref (disconnect_message);

1384

1385 if (disconnect_link != NULL)

1386 \_dbus_list_free_link (disconnect_link);

1387

1388 if (connection != NULL)

1389 {

1390 \_dbus_condvar_free_at_location (&connection-\>io_path_cond);

1391 \_dbus_condvar_free_at_location (&connection-\>dispatch_cond);

1392 \_dbus_rmutex_free_at_location (&connection-\>mutex);

1393 \_dbus_cmutex_free_at_location (&connection-\>io_path_mutex);

1394 \_dbus_cmutex_free_at_location (&connection-\>dispatch_mutex);

1395 \_dbus_rmutex_free_at_location (&connection-\>slot_mutex);

1396 dbus_free (connection);

1397 }

1398 if (pending_replies)

1399 \_dbus_hash_table_unref (pending_replies);

1400

1401 if (watch_list)

1402 \_dbus_watch_list_free (watch_list);

1403

1404 if (timeout_list)

1405 \_dbus_timeout_list_free (timeout_list);

1406

1407 if (outgoing_counter)

1408 \_dbus_counter_unref (outgoing_counter);

1409

1410 if (objects)

1411 \_dbus_object_tree_unref (objects);

1412

1413 return NULL;

1414}

1415

1423DBusConnection \*

1424\_dbus_connection_ref_unlocked (DBusConnection \*connection)

1425{

1426 dbus_int32_t old_refcount;

1427

1428 \_dbus_assert (connection != NULL);

1429 \_dbus_assert (connection-\>generation == \_dbus_current_generation);

1430

1431 HAVE_LOCK_CHECK (connection);

1432

1433 old_refcount = \_dbus_atomic_inc (&connection-\>refcount);

1434 \_dbus_connection_trace_ref (connection, old_refcount, old_refcount + 1,

1435 "ref_unlocked");

1436

1437 return connection;

1438}

1439

1446void

1447\_dbus_connection_unref_unlocked (DBusConnection \*connection)

1448{

1449 dbus_int32_t old_refcount;

1450

1451 HAVE_LOCK_CHECK (connection);

1452

1453 \_dbus_assert (connection != NULL);

1454

1455 old_refcount = \_dbus_atomic_dec (&connection-\>refcount);

1456

1457 \_dbus_connection_trace_ref (connection, old_refcount, old_refcount - 1,

1458 "unref_unlocked");

1459

1460 if (old_refcount == 1)

1461 \_dbus_connection_last_unref (connection);

1462}

1463

1473dbus_uint32_t

1474\_dbus_connection_get_next_client_serial (DBusConnection \*connection)

1475{

1476 dbus_uint32_t serial;

1477

1478 serial = connection-\>client_serial++;

1479

1480 if (connection-\>client_serial == 0)

1481 connection-\>client_serial = 1;

1482

1483 return serial;

1484}

1485

1499dbus_bool_t

1500\_dbus_connection_handle_watch (DBusWatch \*watch,

1501 unsigned int condition,

1502 void \*data)

1503{

1504 DBusConnection \*connection;

1505 dbus_bool_t retval;

1506 DBusDispatchStatus status;

1507

1508 connection = data;

1509

1510 \_dbus_verbose ("start\n");

1511

1512 CONNECTION_LOCK (connection);

1513

1514 if (!\_dbus_connection_acquire_io_path (connection, 1))

1515 {

1516 /\* another thread is handling the message \*/

1517 CONNECTION_UNLOCK (connection);

1518 return TRUE;

1519 }

1520

1521 HAVE_LOCK_CHECK (connection);

1522 retval = \_dbus_transport_handle_watch (connection-\>transport,

1523 watch, condition);

1524

1525 \_dbus_connection_release_io_path (connection);

1526

1527 HAVE_LOCK_CHECK (connection);

1528

1529 \_dbus_verbose ("middle\n");

1530

1531 status = \_dbus_connection_get_dispatch_status_unlocked (connection);

1532

1533 /\* this calls out to user code \*/

1534 \_dbus_connection_update_dispatch_status_and_unlock (connection, status);

1535

1536 \_dbus_verbose ("end\n");

1537

1538 return retval;

1539}

1540

1541/\* Protected by \_DBUS_LOCK (shared_connections) \*/

1542static DBusHashTable \*shared_connections = NULL;

1543static DBusList \*shared_connections_no_guid = NULL;

1544

1545static void

1546close_connection_on_shutdown (DBusConnection \*connection)

1547{

1548 DBusMessage \*message;

1549

1550 dbus_connection_ref (connection);

1551 \_dbus_connection_close_possibly_shared (connection);

1552

1553 /\* Churn through to the Disconnected message \*/

1554 while ((message = dbus_connection_pop_message (connection)))

1555 {

1556 dbus_message_unref (message);

1557 }

1558 dbus_connection_unref (connection);

1559}

1560

1561static void

1562shared_connections_shutdown (void \*data)

1563{

1564 int n_entries;

1565

1566 if (!\_DBUS_LOCK (shared_connections))

1567 {

1568 /\* We'd have initialized locks before adding anything, so there

1569 \* can't be anything there. \*/

1570 return;

1571 }

1572

1573 /\* This is a little bit unpleasant... better ideas? \*/

1574 while ((n_entries = \_dbus_hash_table_get_n_entries (shared_connections)) \> 0)

1575 {

1576 DBusConnection \*connection;

1577 DBusHashIter iter;

1578

1579 \_dbus_hash_iter_init (shared_connections, &iter);

1580 \_dbus_hash_iter_next (&iter);

1581

1582 connection = \_dbus_hash_iter_get_value (&iter);

1583

1584 \_DBUS_UNLOCK (shared_connections);

1585 close_connection_on_shutdown (connection);

1586 if (!\_DBUS_LOCK (shared_connections))

1587 \_dbus_assert_not_reached ("global locks were already initialized");

1588

1589 /\* The connection should now be dead and not in our hash ... \*/

1590 \_dbus_assert (\_dbus_hash_table_get_n_entries (shared_connections) \< n_entries);

1591 }

1592

1593 \_dbus_assert (\_dbus_hash_table_get_n_entries (shared_connections) == 0);

1594

1595 \_dbus_hash_table_unref (shared_connections);

1596 shared_connections = NULL;

1597

1598 if (shared_connections_no_guid != NULL)

1599 {

1600 DBusConnection \*connection;

1601 connection = \_dbus_list_pop_first (&shared_connections_no_guid);

1602 while (connection != NULL)

1603 {

1604 \_DBUS_UNLOCK (shared_connections);

1605 close_connection_on_shutdown (connection);

1606 if (!\_DBUS_LOCK (shared_connections))

1607 \_dbus_assert_not_reached ("global locks were already initialized");

1608 connection = \_dbus_list_pop_first (&shared_connections_no_guid);

1609 }

1610 }

1611

1612 shared_connections_no_guid = NULL;

1613

1614 \_DBUS_UNLOCK (shared_connections);

1615}

1616

1617static dbus_bool_t

1618connection_lookup_shared (DBusAddressEntry \*entry,

1619 DBusConnection \*\*result)

1620{

1621 \_dbus_verbose ("checking for existing connection\n");

1622

1623 \*result = NULL;

1624

1625 if (!\_DBUS_LOCK (shared_connections))

1626 {

1627 /\* If it was shared, we'd have initialized global locks when we put

1628 \* it in shared_connections. \*/

1629 return FALSE;

1630 }

1631

1632 if (shared_connections == NULL)

1633 {

1634 \_dbus_verbose ("creating shared_connections hash table\n");

1635

1636 shared_connections = \_dbus_hash_table_new (DBUS_HASH_STRING,

1637 dbus_free,

1638 NULL);

1639 if (shared_connections == NULL)

1640 {

1641 \_DBUS_UNLOCK (shared_connections);

1642 return FALSE;

1643 }

1644

1645 if (!\_dbus_register_shutdown_func (shared_connections_shutdown, NULL))

1646 {

1647 \_dbus_hash_table_unref (shared_connections);

1648 shared_connections = NULL;

1649 \_DBUS_UNLOCK (shared_connections);

1650 return FALSE;

1651 }

1652

1653 \_dbus_verbose (" successfully created shared_connections\n");

1654

1655 \_DBUS_UNLOCK (shared_connections);

1656 return TRUE; /\* no point looking up in the hash we just made \*/

1657 }

1658 else

1659 {

1660 const char \*guid;

1661

1662 guid = dbus_address_entry_get_value (entry, "guid");

1663

1664 if (guid != NULL)

1665 {

1666 DBusConnection \*connection;

1667

1668 connection = \_dbus_hash_table_lookup_string (shared_connections,

1669 guid);

1670

1671 if (connection)

1672 {

1673 /\* The DBusConnection can't be finalized without taking

1674 \* the shared_connections lock to remove it from the

1675 \* hash. So it's safe to ref the connection here.

1676 \* However, it may be disconnected if the Disconnected

1677 \* message hasn't been processed yet, in which case we

1678 \* want to pretend it isn't in the hash and avoid

1679 \* returning it.

1680 \*

1681 \* The idea is to avoid ever returning a disconnected connection

1682 \* from dbus_connection_open(). We could just synchronously

1683 \* drop our shared ref to the connection on connection disconnect,

1684 \* and then assert here that the connection is connected, but

1685 \* that causes reentrancy headaches.

1686 \*/

1687 CONNECTION_LOCK (connection);

1688 if (\_dbus_connection_get_is_connected_unlocked (connection))

1689 {

1690 \_dbus_connection_ref_unlocked (connection);

1691 \*result = connection;

1692 \_dbus_verbose ("looked up existing connection to server guid %s\n",

1693 guid);

1694 }

1695 else

1696 {

1697 \_dbus_verbose ("looked up existing connection to server guid %s but it was disconnected so ignoring it\n",

1698 guid);

1699 }

1700 CONNECTION_UNLOCK (connection);

1701 }

1702 }

1703

1704 \_DBUS_UNLOCK (shared_connections);

1705 return TRUE;

1706 }

1707}

1708

1709static dbus_bool_t

1710connection_record_shared_unlocked (DBusConnection \*connection,

1711 const char \*guid)

1712{

1713 char \*guid_key;

1714 char \*guid_in_connection;

1715

1716 HAVE_LOCK_CHECK (connection);

1717 \_dbus_assert (connection-\>server_guid == NULL);

1718 \_dbus_assert (connection-\>shareable);

1719

1720 /\* get a hard ref on this connection, even if

1721 \* we won't in fact store it in the hash, we still

1722 \* need to hold a ref on it until it's disconnected.

1723 \*/

1724 \_dbus_connection_ref_unlocked (connection);

1725

1726 if (guid == NULL)

1727 {

1728 if (!\_DBUS_LOCK (shared_connections))

1729 return FALSE;

1730

1731 if (!\_dbus_list_prepend (&shared_connections_no_guid, connection))

1732 {

1733 \_DBUS_UNLOCK (shared_connections);

1734 return FALSE;

1735 }

1736

1737 \_DBUS_UNLOCK (shared_connections);

1738 return TRUE; /\* don't store in the hash \*/

1739 }

1740

1741 /\* A separate copy of the key is required in the hash table, because

1742 \* we don't have a lock on the connection when we are doing a hash

1743 \* lookup.

1744 \*/

1745

1746 guid_key = \_dbus_strdup (guid);

1747 if (guid_key == NULL)

1748 return FALSE;

1749

1750 guid_in_connection = \_dbus_strdup (guid);

1751 if (guid_in_connection == NULL)

1752 {

1753 dbus_free (guid_key);

1754 return FALSE;

1755 }

1756

1757 if (!\_DBUS_LOCK (shared_connections))

1758 {

1759 dbus_free (guid_in_connection);

1760 dbus_free (guid_key);

1761 return FALSE;

1762 }

1763

1764 \_dbus_assert (shared_connections != NULL);

1765

1766 if (!\_dbus_hash_table_insert_string (shared_connections,

1767 guid_key, connection))

1768 {

1769 dbus_free (guid_key);

1770 dbus_free (guid_in_connection);

1771 \_DBUS_UNLOCK (shared_connections);

1772 return FALSE;

1773 }

1774

1775 connection-\>server_guid = guid_in_connection;

1776

1777 \_dbus_verbose ("stored connection to %s to be shared\n",

1778 connection-\>server_guid);

1779

1780 \_DBUS_UNLOCK (shared_connections);

1781

1782 \_dbus_assert (connection-\>server_guid != NULL);

1783

1784 return TRUE;

1785}

1786

1787static void

1788connection_forget_shared_unlocked (DBusConnection \*connection)

1789{

1790 HAVE_LOCK_CHECK (connection);

1791

1792 if (!connection-\>shareable)

1793 return;

1794

1795 if (!\_DBUS_LOCK (shared_connections))

1796 {

1797 /\* If it was shared, we'd have initialized global locks when we put

1798 \* it in the table; so it can't be there. \*/

1799 return;

1800 }

1801

1802 if (connection-\>server_guid != NULL)

1803 {

1804 \_dbus_verbose ("dropping connection to %s out of the shared table\n",

1805 connection-\>server_guid);

1806

1807 if (!\_dbus_hash_table_remove_string (shared_connections,

1808 connection-\>server_guid))

1809 \_dbus_assert_not_reached ("connection was not in the shared table");

1810

1811 dbus_free (connection-\>server_guid);

1812 connection-\>server_guid = NULL;

1813 }

1814 else

1815 {

1816 \_dbus_list_remove (&shared_connections_no_guid, connection);

1817 }

1818

1819 \_DBUS_UNLOCK (shared_connections);

1820

1821 /\* remove our reference held on all shareable connections \*/

1822 \_dbus_connection_unref_unlocked (connection);

1823}

1824

1825static DBusConnection\*

1826connection_try_from_address_entry (DBusAddressEntry \*entry,

1827 DBusError \*error)

1828{

1829 DBusTransport \*transport;

1830 DBusConnection \*connection;

1831

1832 transport = \_dbus_transport_open (entry, error);

1833

1834 if (transport == NULL)

1835 {

1836 \_DBUS_ASSERT_ERROR_IS_SET (error);

1837 return NULL;

1838 }

1839

1840 connection = \_dbus_connection_new_for_transport (transport);

1841

1842 \_dbus_transport_unref (transport);

1843

1844 if (connection == NULL)

1845 {

1846 \_DBUS_SET_OOM (error);

1847 return NULL;

1848 }

1849

1850\#ifndef DBUS_DISABLE_CHECKS

1851 \_dbus_assert (!connection-\>have_connection_lock);

1852\#endif

1853 return connection;

1854}

1855

1856/\*

1857 \* If the shared parameter is true, then any existing connection will

1858 \* be used (and if a new connection is created, it will be available

1859 \* for use by others). If the shared parameter is false, a new

1860 \* connection will always be created, and the new connection will

1861 \* never be returned to other callers.

1862 \*

1863 \* @param address the address

1864 \* @param shared whether the connection is shared or private

1865 \* @param error error return

1866 \* @returns the connection or \#NULL on error

1867 \*/

1868static DBusConnection\*

1869\_dbus_connection_open_internal (const char \*address,

1870 dbus_bool_t shared,

1871 DBusError \*error)

1872{

1873 DBusConnection \*connection;

1874 DBusAddressEntry \*\*entries;

1875 DBusError tmp_error = DBUS_ERROR_INIT;

1876 DBusError first_error = DBUS_ERROR_INIT;

1877 int len, i;

1878

1879 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

1880

1881 \_dbus_verbose ("opening %s connection to: %s\n",

1882 shared ? "shared" : "private", address);

1883

1884 if (!dbus_parse_address (address, &entries, &len, error))

1885 return NULL;

1886

1887 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

1888

1889 connection = NULL;

1890

1891 for (i = 0; i \< len; i++)

1892 {

1893 if (shared)

1894 {

1895 if (!connection_lookup_shared (entries\[i\], &connection))

1896 \_DBUS_SET_OOM (&tmp_error);

1897 }

1898

1899 if (connection == NULL)

1900 {

1901 connection = connection_try_from_address_entry (entries\[i\],

1902 &tmp_error);

1903

1904 if (connection != NULL && shared)

1905 {

1906 const char \*guid;

1907

1908 connection-\>shareable = TRUE;

1909

1910 /\* guid may be NULL \*/

1911 guid = dbus_address_entry_get_value (entries\[i\], "guid");

1912

1913 CONNECTION_LOCK (connection);

1914

1915 if (!connection_record_shared_unlocked (connection, guid))

1916 {

1917 \_DBUS_SET_OOM (&tmp_error);

1918 \_dbus_connection_close_possibly_shared_and_unlock (connection);

1919 dbus_connection_unref (connection);

1920 connection = NULL;

1921 }

1922 else

1923 CONNECTION_UNLOCK (connection);

1924 }

1925 }

1926

1927 if (connection)

1928 break;

1929

1930 \_DBUS_ASSERT_ERROR_IS_SET (&tmp_error);

1931

1932 if (i == 0)

1933 dbus_move_error (&tmp_error, &first_error);

1934 else

1935 dbus_error_free (&tmp_error);

1936 }

1937

1938 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

1939 \_DBUS_ASSERT_ERROR_IS_CLEAR (&tmp_error);

1940

1941 if (connection == NULL)

1942 {

1943 \_DBUS_ASSERT_ERROR_IS_SET (&first_error);

1944 dbus_move_error (&first_error, error);

1945 }

1946 else

1947 dbus_error_free (&first_error);

1948

1949 dbus_address_entries_free (entries);

1950 return connection;

1951}

1952

1961void

1962\_dbus_connection_close_possibly_shared (DBusConnection \*connection)

1963{

1964 \_dbus_assert (connection != NULL);

1965 \_dbus_assert (connection-\>generation == \_dbus_current_generation);

1966

1967 CONNECTION_LOCK (connection);

1968 \_dbus_connection_close_possibly_shared_and_unlock (connection);

1969}

1970

1971static DBusPreallocatedSend\*

1972\_dbus_connection_preallocate_send_unlocked (DBusConnection \*connection)

1973{

1974 DBusPreallocatedSend \*preallocated;

1975

1976 HAVE_LOCK_CHECK (connection);

1977

1978 \_dbus_assert (connection != NULL);

1979

1980 preallocated = dbus_new (DBusPreallocatedSend, 1);

1981 if (preallocated == NULL)

1982 return NULL;

1983

1984 preallocated-\>queue_link = \_dbus_list_alloc_link (NULL);

1985 if (preallocated-\>queue_link == NULL)

1986 goto failed_0;

1987

1988 preallocated-\>counter_link = \_dbus_list_alloc_link (connection-\>outgoing_counter);

1989 if (preallocated-\>counter_link == NULL)

1990 goto failed_1;

1991

1992 \_dbus_counter_ref (preallocated-\>counter_link-\>data);

1993

1994 preallocated-\>connection = connection;

1995

1996 return preallocated;

1997

1998 failed_1:

1999 \_dbus_list_free_link (preallocated-\>queue_link);

2000 failed_0:

2001 dbus_free (preallocated);

2002

2003 return NULL;

2004}

2005

2006/\* Called with lock held, does not update dispatch status \*/

2007static void

2008\_dbus_connection_send_preallocated_unlocked_no_update (DBusConnection \*connection,

2009 DBusPreallocatedSend \*preallocated,

2010 DBusMessage \*message,

2011 dbus_uint32_t \*client_serial)

2012{

2013 dbus_uint32_t serial;

2014

2015 preallocated-\>queue_link-\>data = message;

2016 \_dbus_list_prepend_link (&connection-\>outgoing_messages,

2017 preallocated-\>queue_link);

2018

2019 /\* It's OK that we'll never call the notify function, because for the

2020 \* outgoing limit, there isn't one \*/

2021 \_dbus_message_add_counter_link (message,

2022 preallocated-\>counter_link);

2023

2024 dbus_free (preallocated);

2025 preallocated = NULL;

2026

2027 dbus_message_ref (message);

2028

2029 connection-\>n_outgoing += 1;

2030

2031 \_dbus_verbose ("Message %p (%s %s %s %s '%s') for %s added to outgoing queue %p, %d pending to send\n",

2032 message,

2033 dbus_message_type_to_string (dbus_message_get_type (message)),

2034 dbus_message_get_path (message) ?

2035 dbus_message_get_path (message) :

2036 "no path",

2037 dbus_message_get_interface (message) ?

2038 dbus_message_get_interface (message) :

2039 "no interface",

2040 dbus_message_get_member (message) ?

2041 dbus_message_get_member (message) :

2042 "no member",

2043 dbus_message_get_signature (message),

2044 dbus_message_get_destination (message) ?

2045 dbus_message_get_destination (message) :

2046 "null",

2047 connection,

2048 connection-\>n_outgoing);

2049

2050 if (dbus_message_get_serial (message) == 0)

2051 {

2052 serial = \_dbus_connection_get_next_client_serial (connection);

2053 dbus_message_set_serial (message, serial);

2054 if (client_serial)

2055 \*client_serial = serial;

2056 }

2057 else

2058 {

2059 if (client_serial)

2060 \*client_serial = dbus_message_get_serial (message);

2061 }

2062

2063 \_dbus_verbose ("Message %p serial is %u\n",

2064 message, dbus_message_get_serial (message));

2065

2066 dbus_message_lock (message);

2067

2068 /\* Now we need to run an iteration to hopefully just write the messages

2069 \* out immediately, and otherwise get them queued up

2070 \*/

2071 \_dbus_connection_do_iteration_unlocked (connection,

2072 NULL,

2073 DBUS_ITERATION_DO_WRITING,

2074 -1);

2075

2076 /\* If stuff is still queued up, be sure we wake up the main loop \*/

2077 if (connection-\>n_outgoing \> 0)

2078 \_dbus_connection_wakeup_mainloop (connection);

2079}

2080

2081static void

2082\_dbus_connection_send_preallocated_and_unlock (DBusConnection \*connection,

2083 DBusPreallocatedSend \*preallocated,

2084 DBusMessage \*message,

2085 dbus_uint32_t \*client_serial)

2086{

2087 DBusDispatchStatus status;

2088

2089 HAVE_LOCK_CHECK (connection);

2090

2091 \_dbus_connection_send_preallocated_unlocked_no_update (connection,

2092 preallocated,

2093 message, client_serial);

2094

2095 \_dbus_verbose ("middle\n");

2096 status = \_dbus_connection_get_dispatch_status_unlocked (connection);

2097

2098 /\* this calls out to user code \*/

2099 \_dbus_connection_update_dispatch_status_and_unlock (connection, status);

2100}

2101

2111dbus_bool_t

2112\_dbus_connection_send_and_unlock (DBusConnection \*connection,

2113 DBusMessage \*message,

2114 dbus_uint32_t \*client_serial)

2115{

2116 DBusPreallocatedSend \*preallocated;

2117

2118 \_dbus_assert (connection != NULL);

2119 \_dbus_assert (message != NULL);

2120

2121 preallocated = \_dbus_connection_preallocate_send_unlocked (connection);

2122 if (preallocated == NULL)

2123 {

2124 CONNECTION_UNLOCK (connection);

2125 return FALSE;

2126 }

2127

2128 \_dbus_connection_send_preallocated_and_unlock (connection,

2129 preallocated,

2130 message,

2131 client_serial);

2132 return TRUE;

2133}

2134

2159void

2160\_dbus_connection_close_if_only_one_ref (DBusConnection \*connection)

2161{

2162 dbus_int32_t refcount;

2163

2164 CONNECTION_LOCK (connection);

2165

2166 refcount = \_dbus_atomic_get (&connection-\>refcount);

2167 /\* The caller should have at least one ref \*/

2168 \_dbus_assert (refcount \>= 1);

2169

2170 if (refcount == 1)

2171 \_dbus_connection_close_possibly_shared_and_unlock (connection);

2172 else

2173 CONNECTION_UNLOCK (connection);

2174}

2175

2176

2186static void

2187\_dbus_memory_pause_based_on_timeout (int timeout_milliseconds)

2188{

2189 if (timeout_milliseconds == -1)

2190 \_dbus_sleep_milliseconds (1000);

2191 else if (timeout_milliseconds \< 100)

2192 ; /\* just busy loop \*/

2193 else if (timeout_milliseconds \<= 1000)

2194 \_dbus_sleep_milliseconds (timeout_milliseconds / 3);

2195 else

2196 \_dbus_sleep_milliseconds (1000);

2197}

2198

2199static DBusMessage \*

2200generate_local_error_message (dbus_uint32_t serial,

2201 const char \*error_name,

2202 const char \*error_msg)

2203{

2204 DBusMessage \*message;

2205 message = dbus_message_new (DBUS_MESSAGE_TYPE_ERROR);

2206 if (!message)

2207 goto out;

2208

2209 if (!dbus_message_set_error_name (message, error_name))

2210 {

2211 dbus_message_unref (message);

2212 message = NULL;

2213 goto out;

2214 }

2215

2216 dbus_message_set_no_reply (message, TRUE);

2217

2218 if (!dbus_message_set_reply_serial (message,

2219 serial))

2220 {

2221 dbus_message_unref (message);

2222 message = NULL;

2223 goto out;

2224 }

2225

2226 if (error_msg != NULL)

2227 {

2228 DBusMessageIter iter;

2229

2230 dbus_message_iter_init_append (message, &iter);

2231 if (!dbus_message_iter_append_basic (&iter,

2232 DBUS_TYPE_STRING,

2233 &error_msg))

2234 {

2235 dbus_message_unref (message);

2236 message = NULL;

2237 goto out;

2238 }

2239 }

2240

2241 out:

2242 return message;

2243}

2244

2245/\*

2246 \* Peek the incoming queue to see if we got reply for a specific serial

2247 \*/

2248static dbus_bool_t

2249\_dbus_connection_peek_for_reply_unlocked (DBusConnection \*connection,

2250 dbus_uint32_t client_serial)

2251{

2252 DBusList \*link;

2253 HAVE_LOCK_CHECK (connection);

2254

2255 link = \_dbus_list_get_first_link (&connection-\>incoming_messages);

2256

2257 while (link != NULL)

2258 {

2259 DBusMessage \*reply = link-\>data;

2260

2261 if (dbus_message_get_reply_serial (reply) == client_serial)

2262 {

2263 \_dbus_verbose ("%s reply to %d found in queue\n", \_DBUS_FUNCTION_NAME, client_serial);

2264 return TRUE;

2265 }

2266 link = \_dbus_list_get_next_link (&connection-\>incoming_messages, link);

2267 }

2268

2269 return FALSE;

2270}

2271

2272/\* This is slightly strange since we can pop a message here without

2273 \* the dispatch lock.

2274 \*/

2275static DBusMessage\*

2276check_for_reply_unlocked (DBusConnection \*connection,

2277 dbus_uint32_t client_serial)

2278{

2279 DBusList \*link;

2280

2281 HAVE_LOCK_CHECK (connection);

2282

2283 link = \_dbus_list_get_first_link (&connection-\>incoming_messages);

2284

2285 while (link != NULL)

2286 {

2287 DBusMessage \*reply = link-\>data;

2288

2289 if (dbus_message_get_reply_serial (reply) == client_serial)

2290 {

2291 \_dbus_list_remove_link (&connection-\>incoming_messages, link);

2292 connection-\>n_incoming -= 1;

2293 return reply;

2294 }

2295 link = \_dbus_list_get_next_link (&connection-\>incoming_messages, link);

2296 }

2297

2298 return NULL;

2299}

2300

2301static void

2302connection_timeout_and_complete_all_pending_calls_unlocked (DBusConnection \*connection)

2303{

2304 /\* We can't iterate over the hash in the normal way since we'll be

2305 \* dropping the lock for each item. So we restart the

2306 \* iter each time as we drain the hash table.

2307 \*/

2308

2309 while (\_dbus_hash_table_get_n_entries (connection-\>pending_replies) \> 0)

2310 {

2311 DBusPendingCall \*pending;

2312 DBusHashIter iter;

2313

2314 \_dbus_hash_iter_init (connection-\>pending_replies, &iter);

2315 \_dbus_hash_iter_next (&iter);

2316

2317 pending = \_dbus_hash_iter_get_value (&iter);

2318 \_dbus_pending_call_ref_unlocked (pending);

2319

2320 \_dbus_pending_call_queue_timeout_error_unlocked (pending,

2321 connection);

2322

2323 if (\_dbus_pending_call_is_timeout_added_unlocked (pending))

2324 \_dbus_connection_remove_timeout_unlocked (connection,

2325 \_dbus_pending_call_get_timeout_unlocked (pending));

2326 \_dbus_pending_call_set_timeout_added_unlocked (pending, FALSE);

2327 \_dbus_hash_iter_remove_entry (&iter);

2328

2329 \_dbus_pending_call_unref_and_unlock (pending);

2330 CONNECTION_LOCK (connection);

2331 }

2332 HAVE_LOCK_CHECK (connection);

2333}

2334

2335static void

2336complete_pending_call_and_unlock (DBusConnection \*connection,

2337 DBusPendingCall \*pending,

2338 DBusMessage \*message)

2339{

2340 \_dbus_pending_call_set_reply_unlocked (pending, message);

2341 \_dbus_pending_call_ref_unlocked (pending); /\* in case there's no app with a ref held \*/

2342 \_dbus_pending_call_start_completion_unlocked(pending);

2343 \_dbus_connection_detach_pending_call_and_unlock (connection, pending);

2344

2345 /\* Must be called unlocked since it invokes app callback \*/

2346 \_dbus_pending_call_finish_completion (pending);

2347 dbus_pending_call_unref (pending);

2348}

2349

2350static dbus_bool_t

2351check_for_reply_and_update_dispatch_unlocked (DBusConnection \*connection,

2352 DBusPendingCall \*pending)

2353{

2354 DBusMessage \*reply;

2355 DBusDispatchStatus status;

2356

2357 reply = check_for_reply_unlocked (connection,

2358 \_dbus_pending_call_get_reply_serial_unlocked (pending));

2359 if (reply != NULL)

2360 {

2361 \_dbus_verbose ("checked for reply\n");

2362

2363 \_dbus_verbose ("dbus_connection_send_with_reply_and_block(): got reply\n");

2364

2365 complete_pending_call_and_unlock (connection, pending, reply);

2366 dbus_message_unref (reply);

2367

2368 CONNECTION_LOCK (connection);

2369 status = \_dbus_connection_get_dispatch_status_unlocked (connection);

2370 \_dbus_connection_update_dispatch_status_and_unlock (connection, status);

2371 dbus_pending_call_unref (pending);

2372

2373 return TRUE;

2374 }

2375

2376 return FALSE;

2377}

2378

2393void

2394\_dbus_connection_block_pending_call (DBusPendingCall \*pending)

2395{

2396 dbus_int64_t start_tv_sec;

2397 long start_tv_usec;

2398 dbus_int64_t tv_sec;

2399 long tv_usec;

2400 DBusDispatchStatus status;

2401 DBusConnection \*connection;

2402 dbus_uint32_t client_serial;

2403 DBusTimeout \*timeout;

2404 int timeout_milliseconds, elapsed_milliseconds;

2405

2406 \_dbus_assert (pending != NULL);

2407

2408 if (dbus_pending_call_get_completed (pending))

2409 return;

2410

2411 dbus_pending_call_ref (pending); /\* necessary because the call could be canceled \*/

2412

2413 connection = \_dbus_pending_call_get_connection_and_lock (pending);

2414

2415 /\* Flush message queue - note, can affect dispatch status \*/

2416 \_dbus_connection_flush_unlocked (connection);

2417

2418 client_serial = \_dbus_pending_call_get_reply_serial_unlocked (pending);

2419

2420 /\* note that timeout_milliseconds is limited to a smallish value

2421 \* in \_dbus_pending_call_new() so overflows aren't possible

2422 \* below

2423 \*/

2424 timeout = \_dbus_pending_call_get_timeout_unlocked (pending);

2425 \_dbus_get_monotonic_time (&start_tv_sec, &start_tv_usec);

2426 if (timeout)

2427 {

2428 timeout_milliseconds = dbus_timeout_get_interval (timeout);

2429

2430 \_dbus_verbose ("dbus_connection_send_with_reply_and_block(): will block %d milliseconds for reply serial %u from %" DBUS_INT64_MODIFIER "d sec %ld usec\n",

2431 timeout_milliseconds,

2432 client_serial,

2433 start_tv_sec, start_tv_usec);

2434 }

2435 else

2436 {

2437 timeout_milliseconds = -1;

2438

2439 \_dbus_verbose ("dbus_connection_send_with_reply_and_block(): will block for reply serial %u\n", client_serial);

2440 }

2441

2442 /\* check to see if we already got the data off the socket \*/

2443 /\* from another blocked pending call \*/

2444 if (check_for_reply_and_update_dispatch_unlocked (connection, pending))

2445 return;

2446

2447 /\* Now we wait... \*/

2448 /\* always block at least once as we know we don't have the reply yet \*/

2449 \_dbus_connection_do_iteration_unlocked (connection,

2450 pending,

2451 DBUS_ITERATION_DO_READING \|

2452 DBUS_ITERATION_BLOCK,

2453 timeout_milliseconds);

2454

2455 recheck_status:

2456

2457 \_dbus_verbose ("top of recheck\n");

2458

2459 HAVE_LOCK_CHECK (connection);

2460

2461 /\* queue messages and get status \*/

2462

2463 status = \_dbus_connection_get_dispatch_status_unlocked (connection);

2464

2465 /\* the get_completed() is in case a dispatch() while we were blocking

2466 \* got the reply instead of us.

2467 \*/

2468 if (\_dbus_pending_call_get_completed_unlocked (pending))

2469 {

2470 \_dbus_verbose ("Pending call completed by dispatch\n");

2471 \_dbus_connection_update_dispatch_status_and_unlock (connection, status);

2472 dbus_pending_call_unref (pending);

2473 return;

2474 }

2475

2476 if (status == DBUS_DISPATCH_DATA_REMAINS)

2477 {

2478 if (check_for_reply_and_update_dispatch_unlocked (connection, pending))

2479 return;

2480 }

2481

2482 \_dbus_get_monotonic_time (&tv_sec, &tv_usec);

2483 elapsed_milliseconds = (tv_sec - start_tv_sec) \* 1000 +

2484 (tv_usec - start_tv_usec) / 1000;

2485

2486 if (!\_dbus_connection_get_is_connected_unlocked (connection))

2487 {

2488 DBusMessage \*error_msg;

2489

2490 error_msg = generate_local_error_message (client_serial,

2491 DBUS_ERROR_DISCONNECTED,

2492 "Connection was disconnected before a reply was received");

2493

2494 /\* on OOM error_msg is set to NULL \*/

2495 complete_pending_call_and_unlock (connection, pending, error_msg);

2496 if (error_msg != NULL)

2497 dbus_message_unref (error_msg);

2498 dbus_pending_call_unref (pending);

2499 return;

2500 }

2501 else if (connection-\>disconnect_message_link == NULL)

2502 \_dbus_verbose ("dbus_connection_send_with_reply_and_block(): disconnected\n");

2503 else if (timeout == NULL)

2504 {

2505 if (status == DBUS_DISPATCH_NEED_MEMORY)

2506 {

2507 /\* Try sleeping a bit, as we aren't sure we need to block for reading,

2508 \* we may already have a reply in the buffer and just can't process

2509 \* it.

2510 \*/

2511 \_dbus_verbose ("dbus_connection_send_with_reply_and_block() waiting for more memory\n");

2512

2513 \_dbus_memory_pause_based_on_timeout (timeout_milliseconds - elapsed_milliseconds);

2514 }

2515 else

2516 {

2517 /\* block again, we don't have the reply buffered yet. \*/

2518 \_dbus_connection_do_iteration_unlocked (connection,

2519 pending,

2520 DBUS_ITERATION_DO_READING \|

2521 DBUS_ITERATION_BLOCK,

2522 timeout_milliseconds - elapsed_milliseconds);

2523 }

2524

2525 goto recheck_status;

2526 }

2527 else if (tv_sec \< start_tv_sec)

2528 \_dbus_verbose ("dbus_connection_send_with_reply_and_block(): clock set backward\n");

2529 else if (elapsed_milliseconds \< timeout_milliseconds)

2530 {

2531 \_dbus_verbose ("dbus_connection_send_with_reply_and_block(): %d milliseconds remain\n", timeout_milliseconds - elapsed_milliseconds);

2532

2533 if (status == DBUS_DISPATCH_NEED_MEMORY)

2534 {

2535 /\* Try sleeping a bit, as we aren't sure we need to block for reading,

2536 \* we may already have a reply in the buffer and just can't process

2537 \* it.

2538 \*/

2539 \_dbus_verbose ("dbus_connection_send_with_reply_and_block() waiting for more memory\n");

2540

2541 \_dbus_memory_pause_based_on_timeout (timeout_milliseconds - elapsed_milliseconds);

2542 }

2543 else

2544 {

2545 /\* block again, we don't have the reply buffered yet. \*/

2546 \_dbus_connection_do_iteration_unlocked (connection,

2547 pending,

2548 DBUS_ITERATION_DO_READING \|

2549 DBUS_ITERATION_BLOCK,

2550 timeout_milliseconds - elapsed_milliseconds);

2551 }

2552

2553 goto recheck_status;

2554 }

2555

2556 \_dbus_verbose ("dbus_connection_send_with_reply_and_block(): Waited %d milliseconds and got no reply\n",

2557 elapsed_milliseconds);

2558

2559 \_dbus_assert (!\_dbus_pending_call_get_completed_unlocked (pending));

2560

2561 /\* unlock and call user code \*/

2562 complete_pending_call_and_unlock (connection, pending, NULL);

2563

2564 /\* update user code on dispatch status \*/

2565 CONNECTION_LOCK (connection);

2566 status = \_dbus_connection_get_dispatch_status_unlocked (connection);

2567 \_dbus_connection_update_dispatch_status_and_unlock (connection, status);

2568 dbus_pending_call_unref (pending);

2569}

2570

2576int

2577\_dbus_connection_get_pending_fds_count (DBusConnection \*connection)

2578{

2579 return \_dbus_transport_get_pending_fds_count (connection-\>transport);

2580}

2581

2589void

2590\_dbus_connection_set_pending_fds_function (DBusConnection \*connection,

2591 DBusPendingFdsChangeFunction callback,

2592 void \*data)

2593{

2594 \_dbus_transport_set_pending_fds_function (connection-\>transport,

2595 callback, data);

2596}

2597

2634DBusConnection\*

2635dbus_connection_open (const char \*address,

2636 DBusError \*error)

2637{

2638 DBusConnection \*connection;

2639

2640 \_dbus_return_val_if_fail (address != NULL, NULL);

2641 \_dbus_return_val_if_error_is_set (error, NULL);

2642

2643 connection = \_dbus_connection_open_internal (address,

2644 TRUE,

2645 error);

2646

2647 return connection;

2648}

2649

2677DBusConnection\*

2678dbus_connection_open_private (const char \*address,

2679 DBusError \*error)

2680{

2681 DBusConnection \*connection;

2682

2683 \_dbus_return_val_if_fail (address != NULL, NULL);

2684 \_dbus_return_val_if_error_is_set (error, NULL);

2685

2686 connection = \_dbus_connection_open_internal (address,

2687 FALSE,

2688 error);

2689

2690 return connection;

2691}

2692

2699DBusConnection \*

2700dbus_connection_ref (DBusConnection \*connection)

2701{

2702 dbus_int32_t old_refcount;

2703

2704 \_dbus_return_val_if_fail (connection != NULL, NULL);

2705 \_dbus_return_val_if_fail (connection-\>generation == \_dbus_current_generation, NULL);

2706 old_refcount = \_dbus_atomic_inc (&connection-\>refcount);

2707 \_dbus_connection_trace_ref (connection, old_refcount, old_refcount + 1,

2708 "ref");

2709

2710 return connection;

2711}

2712

2713static void

2714free_outgoing_message (void \*element,

2715 void \*data)

2716{

2717 DBusMessage \*message = element;

2718 DBusConnection \*connection = data;

2719

2720 \_dbus_message_remove_counter (message, connection-\>outgoing_counter);

2721 dbus_message_unref (message);

2722}

2723

2724/\* This is run without the mutex held, but after the last reference

2725 \* to the connection has been dropped we should have no thread-related

2726 \* problems

2727 \*/

2728static void

2729\_dbus_connection_last_unref (DBusConnection \*connection)

2730{

2731 DBusList \*link;

2732

2733 \_dbus_verbose ("Finalizing connection %p\n", connection);

2734

2735 \_dbus_assert (\_dbus_atomic_get (&connection-\>refcount) == 0);

2736

2737 /\* You have to disconnect the connection before unref:ing it. Otherwise

2738 \* you won't get the disconnected message.

2739 \*/

2740 \_dbus_assert (!\_dbus_transport_get_is_connected (connection-\>transport));

2741 \_dbus_assert (connection-\>server_guid == NULL);

2742

2743 /\* ---- We're going to call various application callbacks here, hope it doesn't break anything... \*/

2744 \_dbus_object_tree_free_all_unlocked (connection-\>objects);

2745

2746 dbus_connection_set_dispatch_status_function (connection, NULL, NULL, NULL);

2747 dbus_connection_set_wakeup_main_function (connection, NULL, NULL, NULL);

2748 dbus_connection_set_unix_user_function (connection, NULL, NULL, NULL);

2749 dbus_connection_set_windows_user_function (connection, NULL, NULL, NULL);

2750

2751 \_dbus_watch_list_free (connection-\>watches);

2752 connection-\>watches = NULL;

2753

2754 \_dbus_timeout_list_free (connection-\>timeouts);

2755 connection-\>timeouts = NULL;

2756

2757 \_dbus_data_slot_list_free (&connection-\>slot_list);

2758

2759 link = \_dbus_list_get_first_link (&connection-\>filter_list);

2760 while (link != NULL)

2761 {

2762 DBusMessageFilter \*filter = link-\>data;

2763 DBusList \*next = \_dbus_list_get_next_link (&connection-\>filter_list, link);

2764

2765 filter-\>function = NULL;

2766 \_dbus_message_filter_unref (filter); /\* calls app callback \*/

2767 link-\>data = NULL;

2768

2769 link = next;

2770 }

2771 \_dbus_list_clear (&connection-\>filter_list);

2772

2773 /\* ---- Done with stuff that invokes application callbacks \*/

2774

2775 \_dbus_object_tree_unref (connection-\>objects);

2776

2777 \_dbus_hash_table_unref (connection-\>pending_replies);

2778 connection-\>pending_replies = NULL;

2779

2780 \_dbus_list_foreach (&connection-\>outgoing_messages,

2781 free_outgoing_message,

2782 connection);

2783 \_dbus_list_clear (&connection-\>outgoing_messages);

2784

2785 \_dbus_list_clear_full (&connection-\>incoming_messages,

2786 (DBusFreeFunction) dbus_message_unref);

2787

2788 \_dbus_counter_unref (connection-\>outgoing_counter);

2789

2790 \_dbus_transport_unref (connection-\>transport);

2791

2792 if (connection-\>disconnect_message_link)

2793 {

2794 DBusMessage \*message = connection-\>disconnect_message_link-\>data;

2795 dbus_message_unref (message);

2796 \_dbus_list_free_link (connection-\>disconnect_message_link);

2797 }

2798

2799 \_dbus_condvar_free_at_location (&connection-\>dispatch_cond);

2800 \_dbus_condvar_free_at_location (&connection-\>io_path_cond);

2801

2802 \_dbus_cmutex_free_at_location (&connection-\>io_path_mutex);

2803 \_dbus_cmutex_free_at_location (&connection-\>dispatch_mutex);

2804

2805 \_dbus_rmutex_free_at_location (&connection-\>slot_mutex);

2806

2807 \_dbus_rmutex_free_at_location (&connection-\>mutex);

2808

2809 dbus_free (connection);

2810}

2811

2831void

2832dbus_connection_unref (DBusConnection \*connection)

2833{

2834 dbus_int32_t old_refcount;

2835

2836 \_dbus_return_if_fail (connection != NULL);

2837 \_dbus_return_if_fail (connection-\>generation == \_dbus_current_generation);

2838

2839 old_refcount = \_dbus_atomic_dec (&connection-\>refcount);

2840

2841 \_dbus_connection_trace_ref (connection, old_refcount, old_refcount - 1,

2842 "unref");

2843

2844 if (old_refcount == 1)

2845 {

2846\#ifndef DBUS_DISABLE_CHECKS

2847 if (\_dbus_transport_get_is_connected (connection-\>transport))

2848 {

2849 \_dbus_warn_check_failed ("The last reference on a connection was dropped without closing the connection. This is a bug in an application. See dbus_connection_unref() documentation for details.\n%s",

2850 connection-\>shareable ?

2851 "Most likely, the application called unref() too many times and removed a reference belonging to libdbus, since this is a shared connection." :

2852 "Most likely, the application was supposed to call dbus_connection_close(), since this is a private connection.");

2853 return;

2854 }

2855\#endif

2856 \_dbus_connection_last_unref (connection);

2857 }

2858}

2859

2860/\*

2861 \* Note that the transport can disconnect itself (other end drops us)

2862 \* and in that case this function never runs. So this function must

2863 \* not do anything more than disconnect the transport and update the

2864 \* dispatch status.

2865 \*

2866 \* If the transport self-disconnects, then we assume someone will

2867 \* dispatch the connection to cause the dispatch status update.

2868 \*/

2869static void

2870\_dbus_connection_close_possibly_shared_and_unlock (DBusConnection \*connection)

2871{

2872 DBusDispatchStatus status;

2873

2874 HAVE_LOCK_CHECK (connection);

2875

2876 \_dbus_verbose ("Disconnecting %p\n", connection);

2877

2878 /\* We need to ref because update_dispatch_status_and_unlock will unref

2879 \* the connection if it was shared and libdbus was the only remaining

2880 \* refcount holder.

2881 \*/

2882 \_dbus_connection_ref_unlocked (connection);

2883

2884 \_dbus_transport_disconnect (connection-\>transport);

2885

2886 /\* This has the side effect of queuing the disconnect message link

2887 \* (unless we don't have enough memory, possibly, so don't assert it).

2888 \* After the disconnect message link is queued, dbus_bus_get/dbus_connection_open

2889 \* should never again return the newly-disconnected connection.

2890 \*

2891 \* However, we only unref the shared connection and exit_on_disconnect when

2892 \* the disconnect message reaches the head of the message queue,

2893 \* NOT when it's first queued.

2894 \*/

2895 status = \_dbus_connection_get_dispatch_status_unlocked (connection);

2896

2897 /\* This calls out to user code \*/

2898 \_dbus_connection_update_dispatch_status_and_unlock (connection, status);

2899

2900 /\* Could also call out to user code \*/

2901 dbus_connection_unref (connection);

2902}

2903

2946void

2947dbus_connection_close (DBusConnection \*connection)

2948{

2949 \_dbus_return_if_fail (connection != NULL);

2950 \_dbus_return_if_fail (connection-\>generation == \_dbus_current_generation);

2951

2952 CONNECTION_LOCK (connection);

2953

2954\#ifndef DBUS_DISABLE_CHECKS

2955 if (connection-\>shareable)

2956 {

2957 CONNECTION_UNLOCK (connection);

2958

2959 \_dbus_warn_check_failed ("Applications must not close shared connections - see dbus_connection_close() docs. This is a bug in the application.");

2960 return;

2961 }

2962\#endif

2963

2964 \_dbus_connection_close_possibly_shared_and_unlock (connection);

2965}

2966

2967static dbus_bool_t

2968\_dbus_connection_get_is_connected_unlocked (DBusConnection \*connection)

2969{

2970 HAVE_LOCK_CHECK (connection);

2971 return \_dbus_transport_get_is_connected (connection-\>transport);

2972}

2973

2987dbus_bool_t

2988dbus_connection_get_is_connected (DBusConnection \*connection)

2989{

2990 dbus_bool_t res;

2991

2992 \_dbus_return_val_if_fail (connection != NULL, FALSE);

2993

2994 CONNECTION_LOCK (connection);

2995 res = \_dbus_connection_get_is_connected_unlocked (connection);

2996 CONNECTION_UNLOCK (connection);

2997

2998 return res;

2999}

3000

3009dbus_bool_t

3010dbus_connection_get_is_authenticated (DBusConnection \*connection)

3011{

3012 dbus_bool_t res;

3013

3014 \_dbus_return_val_if_fail (connection != NULL, FALSE);

3015

3016 CONNECTION_LOCK (connection);

3017 res = \_dbus_transport_try_to_authenticate (connection-\>transport);

3018 CONNECTION_UNLOCK (connection);

3019

3020 return res;

3021}

3022

3043dbus_bool_t

3044dbus_connection_get_is_anonymous (DBusConnection \*connection)

3045{

3046 dbus_bool_t res;

3047

3048 \_dbus_return_val_if_fail (connection != NULL, FALSE);

3049

3050 CONNECTION_LOCK (connection);

3051 res = \_dbus_transport_get_is_anonymous (connection-\>transport);

3052 CONNECTION_UNLOCK (connection);

3053

3054 return res;

3055}

3056

3088char\*

3089dbus_connection_get_server_id (DBusConnection \*connection)

3090{

3091 char \*id;

3092

3093 \_dbus_return_val_if_fail (connection != NULL, NULL);

3094

3095 CONNECTION_LOCK (connection);

3096 id = \_dbus_strdup (\_dbus_transport_get_server_id (connection-\>transport));

3097 CONNECTION_UNLOCK (connection);

3098

3099 return id;

3100}

3101

3119dbus_bool_t

3120dbus_connection_can_send_type(DBusConnection \*connection,

3121 int type)

3122{

3123 \_dbus_return_val_if_fail (connection != NULL, FALSE);

3124

3125 if (!dbus_type_is_valid (type))

3126 return FALSE;

3127

3128 if (type != DBUS_TYPE_UNIX_FD)

3129 return TRUE;

3130

3131\#ifdef HAVE_UNIX_FD_PASSING

3132 {

3133 dbus_bool_t b;

3134

3135 CONNECTION_LOCK(connection);

3136 b = \_dbus_transport_can_pass_unix_fd(connection-\>transport);

3137 CONNECTION_UNLOCK(connection);

3138

3139 return b;

3140 }

3141\#endif

3142

3143 return FALSE;

3144}

3145

3159void

3160dbus_connection_set_exit_on_disconnect (DBusConnection \*connection,

3161 dbus_bool_t exit_on_disconnect)

3162{

3163 \_dbus_return_if_fail (connection != NULL);

3164

3165 CONNECTION_LOCK (connection);

3166 connection-\>exit_on_disconnect = exit_on_disconnect != FALSE;

3167 CONNECTION_UNLOCK (connection);

3168}

3169

3179DBusPreallocatedSend\*

3180dbus_connection_preallocate_send (DBusConnection \*connection)

3181{

3182 DBusPreallocatedSend \*preallocated;

3183

3184 \_dbus_return_val_if_fail (connection != NULL, NULL);

3185

3186 CONNECTION_LOCK (connection);

3187

3188 preallocated =

3189 \_dbus_connection_preallocate_send_unlocked (connection);

3190

3191 CONNECTION_UNLOCK (connection);

3192

3193 return preallocated;

3194}

3195

3205void

3206dbus_connection_free_preallocated_send (DBusConnection \*connection,

3207 DBusPreallocatedSend \*preallocated)

3208{

3209 \_dbus_return_if_fail (connection != NULL);

3210 \_dbus_return_if_fail (preallocated != NULL);

3211 \_dbus_return_if_fail (connection == preallocated-\>connection);

3212

3213 \_dbus_list_free_link (preallocated-\>queue_link);

3214 \_dbus_counter_unref (preallocated-\>counter_link-\>data);

3215 \_dbus_list_free_link (preallocated-\>counter_link);

3216 dbus_free (preallocated);

3217}

3218

3231void

3232dbus_connection_send_preallocated (DBusConnection \*connection,

3233 DBusPreallocatedSend \*preallocated,

3234 DBusMessage \*message,

3235 dbus_uint32_t \*client_serial)

3236{

3237 \_dbus_return_if_fail (connection != NULL);

3238 \_dbus_return_if_fail (preallocated != NULL);

3239 \_dbus_return_if_fail (message != NULL);

3240 \_dbus_return_if_fail (preallocated-\>connection == connection);

3241 \_dbus_return_if_fail (dbus_message_get_type (message) != DBUS_MESSAGE_TYPE_METHOD_CALL \|\|

3242 dbus_message_get_member (message) != NULL);

3243 \_dbus_return_if_fail (dbus_message_get_type (message) != DBUS_MESSAGE_TYPE_SIGNAL \|\|

3244 (dbus_message_get_interface (message) != NULL &&

3245 dbus_message_get_member (message) != NULL));

3246

3247 CONNECTION_LOCK (connection);

3248

3249\#ifdef HAVE_UNIX_FD_PASSING

3250

3251 if (!\_dbus_transport_can_pass_unix_fd(connection-\>transport) &&

3252 message-\>n_unix_fds \> 0)

3253 {

3254 /\* Refuse to send fds on a connection that cannot handle

3255 them. Unfortunately we cannot return a proper error here, so

3256 the best we can is just return. \*/

3257 CONNECTION_UNLOCK (connection);

3258 return;

3259 }

3260

3261\#endif

3262

3263 \_dbus_connection_send_preallocated_and_unlock (connection,

3264 preallocated,

3265 message, client_serial);

3266}

3267

3268static dbus_bool_t

3269\_dbus_connection_send_unlocked_no_update (DBusConnection \*connection,

3270 DBusMessage \*message,

3271 dbus_uint32_t \*client_serial)

3272{

3273 DBusPreallocatedSend \*preallocated;

3274

3275 \_dbus_assert (connection != NULL);

3276 \_dbus_assert (message != NULL);

3277

3278 preallocated = \_dbus_connection_preallocate_send_unlocked (connection);

3279 if (preallocated == NULL)

3280 return FALSE;

3281

3282 \_dbus_connection_send_preallocated_unlocked_no_update (connection,

3283 preallocated,

3284 message,

3285 client_serial);

3286 return TRUE;

3287}

3288

3316dbus_bool_t

3317dbus_connection_send (DBusConnection \*connection,

3318 DBusMessage \*message,

3319 dbus_uint32_t \*serial)

3320{

3321 \_dbus_return_val_if_fail (connection != NULL, FALSE);

3322 \_dbus_return_val_if_fail (message != NULL, FALSE);

3323

3324 CONNECTION_LOCK (connection);

3325

3326\#ifdef HAVE_UNIX_FD_PASSING

3327

3328 if (!\_dbus_transport_can_pass_unix_fd(connection-\>transport) &&

3329 message-\>n_unix_fds \> 0)

3330 {

3331 /\* Refuse to send fds on a connection that cannot handle

3332 them. Unfortunately we cannot return a proper error here, so

3333 the best we can is just return. \*/

3334 CONNECTION_UNLOCK (connection);

3335 return FALSE;

3336 }

3337

3338\#endif

3339

3340 return \_dbus_connection_send_and_unlock (connection,

3341 message,

3342 serial);

3343}

3344

3345static dbus_bool_t

3346reply_handler_timeout (void \*data)

3347{

3348 DBusConnection \*connection;

3349 DBusDispatchStatus status;

3350 DBusPendingCall \*pending = data;

3351

3352 connection = \_dbus_pending_call_get_connection_and_lock (pending);

3353 \_dbus_connection_ref_unlocked (connection);

3354

3355 \_dbus_pending_call_queue_timeout_error_unlocked (pending,

3356 connection);

3357 \_dbus_connection_remove_timeout_unlocked (connection,

3358 \_dbus_pending_call_get_timeout_unlocked (pending));

3359 \_dbus_pending_call_set_timeout_added_unlocked (pending, FALSE);

3360

3361 \_dbus_verbose ("middle\n");

3362 status = \_dbus_connection_get_dispatch_status_unlocked (connection);

3363

3364 /\* Unlocks, and calls out to user code \*/

3365 \_dbus_connection_update_dispatch_status_and_unlock (connection, status);

3366 dbus_connection_unref (connection);

3367

3368 return TRUE;

3369}

3370

3414dbus_bool_t

3415dbus_connection_send_with_reply (DBusConnection \*connection,

3416 DBusMessage \*message,

3417 DBusPendingCall \*\*pending_return,

3418 int timeout_milliseconds)

3419{

3420 DBusPendingCall \*pending;

3421 dbus_int32_t serial = -1;

3422 DBusDispatchStatus status;

3423

3424 \_dbus_return_val_if_fail (connection != NULL, FALSE);

3425 \_dbus_return_val_if_fail (message != NULL, FALSE);

3426 \_dbus_return_val_if_fail (timeout_milliseconds \>= 0 \|\| timeout_milliseconds == -1, FALSE);

3427

3428 if (pending_return)

3429 \*pending_return = NULL;

3430

3431 CONNECTION_LOCK (connection);

3432

3433\#ifdef HAVE_UNIX_FD_PASSING

3434

3435 if (!\_dbus_transport_can_pass_unix_fd(connection-\>transport) &&

3436 message-\>n_unix_fds \> 0)

3437 {

3438 /\* Refuse to send fds on a connection that cannot handle

3439 them. Unfortunately we cannot return a proper error here, so

3440 the best we can do is return TRUE but leave \*pending_return

3441 as NULL. \*/

3442 CONNECTION_UNLOCK (connection);

3443 return TRUE;

3444 }

3445

3446\#endif

3447

3448 if (!\_dbus_connection_get_is_connected_unlocked (connection))

3449 {

3450 CONNECTION_UNLOCK (connection);

3451

3452 return TRUE;

3453 }

3454

3455 pending = \_dbus_pending_call_new_unlocked (connection,

3456 timeout_milliseconds,

3457 reply_handler_timeout);

3458

3459 if (pending == NULL)

3460 {

3461 CONNECTION_UNLOCK (connection);

3462 return FALSE;

3463 }

3464

3465 /\* Assign a serial to the message \*/

3466 serial = dbus_message_get_serial (message);

3467 if (serial == 0)

3468 {

3469 serial = \_dbus_connection_get_next_client_serial (connection);

3470 dbus_message_set_serial (message, serial);

3471 }

3472

3473 if (!\_dbus_pending_call_set_timeout_error_unlocked (pending, message, serial))

3474 goto error;

3475

3476 /\* Insert the serial in the pending replies hash;

3477 \* hash takes a refcount on DBusPendingCall.

3478 \* Also, add the timeout.

3479 \*/

3480 if (!\_dbus_connection_attach_pending_call_unlocked (connection,

3481 pending))

3482 goto error;

3483

3484 if (!\_dbus_connection_send_unlocked_no_update (connection, message, NULL))

3485 {

3486 \_dbus_connection_detach_pending_call_and_unlock (connection,

3487 pending);

3488 goto error_unlocked;

3489 }

3490

3491 if (pending_return)

3492 \*pending_return = pending; /\* hand off refcount \*/

3493 else

3494 {

3495 \_dbus_connection_detach_pending_call_unlocked (connection, pending);

3496 /\* we still have a ref to the pending call in this case, we unref

3497 \* after unlocking, below

3498 \*/

3499 }

3500

3501 status = \_dbus_connection_get_dispatch_status_unlocked (connection);

3502

3503 /\* this calls out to user code \*/

3504 \_dbus_connection_update_dispatch_status_and_unlock (connection, status);

3505

3506 if (pending_return == NULL)

3507 dbus_pending_call_unref (pending);

3508

3509 return TRUE;

3510

3511 error:

3512 CONNECTION_UNLOCK (connection);

3513 error_unlocked:

3514 dbus_pending_call_unref (pending);

3515 return FALSE;

3516}

3517

3550DBusMessage\*

3551dbus_connection_send_with_reply_and_block (DBusConnection \*connection,

3552 DBusMessage \*message,

3553 int timeout_milliseconds,

3554 DBusError \*error)

3555{

3556 DBusMessage \*reply;

3557 DBusPendingCall \*pending;

3558

3559 \_dbus_return_val_if_fail (connection != NULL, NULL);

3560 \_dbus_return_val_if_fail (message != NULL, NULL);

3561 \_dbus_return_val_if_fail (timeout_milliseconds \>= 0 \|\| timeout_milliseconds == -1, NULL);

3562 \_dbus_return_val_if_error_is_set (error, NULL);

3563

3564\#ifdef HAVE_UNIX_FD_PASSING

3565

3566 CONNECTION_LOCK (connection);

3567 if (!\_dbus_transport_can_pass_unix_fd(connection-\>transport) &&

3568 message-\>n_unix_fds \> 0)

3569 {

3570 CONNECTION_UNLOCK (connection);

3571 dbus_set_error(error, DBUS_ERROR_FAILED, "Cannot send file descriptors on this connection.");

3572 return NULL;

3573 }

3574 CONNECTION_UNLOCK (connection);

3575

3576\#endif

3577

3578 if (!dbus_connection_send_with_reply (connection, message,

3579 &pending, timeout_milliseconds))

3580 {

3581 \_DBUS_SET_OOM (error);

3582 return NULL;

3583 }

3584

3585 if (pending == NULL)

3586 {

3587 dbus_set_error (error, DBUS_ERROR_DISCONNECTED, "Connection is closed");

3588 return NULL;

3589 }

3590

3591 dbus_pending_call_block (pending);

3592

3593 reply = dbus_pending_call_steal_reply (pending);

3594 dbus_pending_call_unref (pending);

3595

3596 /\* call_complete_and_unlock() called from pending_call_block() should

3597 \* always fill this in.

3598 \*/

3599 \_dbus_assert (reply != NULL);

3600

3601 if (dbus_set_error_from_message (error, reply))

3602 {

3603 dbus_message_unref (reply);

3604 return NULL;

3605 }

3606 else

3607 return reply;

3608}

3609

3618static DBusDispatchStatus

3619\_dbus_connection_flush_unlocked (DBusConnection \*connection)

3620{

3621 /\* We have to specify DBUS_ITERATION_DO_READING here because

3622 \* otherwise we could have two apps deadlock if they are both doing

3623 \* a flush(), and the kernel buffers fill up. This could change the

3624 \* dispatch status.

3625 \*/

3626 DBusDispatchStatus status;

3627

3628 HAVE_LOCK_CHECK (connection);

3629

3630 while (connection-\>n_outgoing \> 0 &&

3631 \_dbus_connection_get_is_connected_unlocked (connection))

3632 {

3633 \_dbus_verbose ("doing iteration in\n");

3634 HAVE_LOCK_CHECK (connection);

3635 \_dbus_connection_do_iteration_unlocked (connection,

3636 NULL,

3637 DBUS_ITERATION_DO_READING \|

3638 DBUS_ITERATION_DO_WRITING \|

3639 DBUS_ITERATION_BLOCK,

3640 -1);

3641 }

3642

3643 HAVE_LOCK_CHECK (connection);

3644 \_dbus_verbose ("middle\n");

3645 status = \_dbus_connection_get_dispatch_status_unlocked (connection);

3646

3647 HAVE_LOCK_CHECK (connection);

3648 return status;

3649}

3650

3656void

3657dbus_connection_flush (DBusConnection \*connection)

3658{

3659 /\* We have to specify DBUS_ITERATION_DO_READING here because

3660 \* otherwise we could have two apps deadlock if they are both doing

3661 \* a flush(), and the kernel buffers fill up. This could change the

3662 \* dispatch status.

3663 \*/

3664 DBusDispatchStatus status;

3665

3666 \_dbus_return_if_fail (connection != NULL);

3667

3668 CONNECTION_LOCK (connection);

3669

3670 status = \_dbus_connection_flush_unlocked (connection);

3671

3672 HAVE_LOCK_CHECK (connection);

3673 /\* Unlocks and calls out to user code \*/

3674 \_dbus_connection_update_dispatch_status_and_unlock (connection, status);

3675

3676 \_dbus_verbose ("end\n");

3677}

3678

3689static dbus_bool_t

3690\_dbus_connection_read_write_dispatch (DBusConnection \*connection,

3691 int timeout_milliseconds,

3692 dbus_bool_t dispatch)

3693{

3694 DBusDispatchStatus dstatus;

3695 dbus_bool_t progress_possible;

3696

3697 /\* Need to grab a ref here in case we're a private connection and

3698 \* the user drops the last ref in a handler we call; see bug

3699 \* https://bugs.freedesktop.org/show_bug.cgi?id=15635

3700 \*/

3701 dbus_connection_ref (connection);

3702 dstatus = dbus_connection_get_dispatch_status (connection);

3703

3704 if (dispatch && dstatus == DBUS_DISPATCH_DATA_REMAINS)

3705 {

3706 \_dbus_verbose ("doing dispatch\n");

3707 dbus_connection_dispatch (connection);

3708 CONNECTION_LOCK (connection);

3709 }

3710 else if (dstatus == DBUS_DISPATCH_NEED_MEMORY)

3711 {

3712 \_dbus_verbose ("pausing for memory\n");

3713 \_dbus_memory_pause_based_on_timeout (timeout_milliseconds);

3714 CONNECTION_LOCK (connection);

3715 }

3716 else

3717 {

3718 CONNECTION_LOCK (connection);

3719 if (\_dbus_connection_get_is_connected_unlocked (connection))

3720 {

3721 \_dbus_verbose ("doing iteration\n");

3722 \_dbus_connection_do_iteration_unlocked (connection,

3723 NULL,

3724 DBUS_ITERATION_DO_READING \|

3725 DBUS_ITERATION_DO_WRITING \|

3726 DBUS_ITERATION_BLOCK,

3727 timeout_milliseconds);

3728 }

3729 }

3730

3731 HAVE_LOCK_CHECK (connection);

3732 /\* If we can dispatch, we can make progress until the Disconnected message

3733 \* has been processed; if we can only read/write, we can make progress

3734 \* as long as the transport is open.

3735 \*/

3736 if (dispatch)

3737 progress_possible = connection-\>n_incoming != 0 \|\|

3738 connection-\>disconnect_message_link != NULL;

3739 else

3740 progress_possible = \_dbus_connection_get_is_connected_unlocked (connection);

3741

3742 CONNECTION_UNLOCK (connection);

3743

3744 dbus_connection_unref (connection);

3745

3746 return progress_possible; /\* TRUE if we can make more progress \*/

3747}

3748

3749

3784dbus_bool_t

3785dbus_connection_read_write_dispatch (DBusConnection \*connection,

3786 int timeout_milliseconds)

3787{

3788 \_dbus_return_val_if_fail (connection != NULL, FALSE);

3789 \_dbus_return_val_if_fail (timeout_milliseconds \>= 0 \|\| timeout_milliseconds == -1, FALSE);

3790 return \_dbus_connection_read_write_dispatch(connection, timeout_milliseconds, TRUE);

3791}

3792

3816dbus_bool_t

3817dbus_connection_read_write (DBusConnection \*connection,

3818 int timeout_milliseconds)

3819{

3820 \_dbus_return_val_if_fail (connection != NULL, FALSE);

3821 \_dbus_return_val_if_fail (timeout_milliseconds \>= 0 \|\| timeout_milliseconds == -1, FALSE);

3822 return \_dbus_connection_read_write_dispatch(connection, timeout_milliseconds, FALSE);

3823}

3824

3825/\* We need to call this anytime we pop the head of the queue, and then

3826 \* update_dispatch_status_and_unlock needs to be called afterward

3827 \* which will "process" the disconnected message and set

3828 \* disconnected_message_processed.

3829 \*/

3830static void

3831check_disconnected_message_arrived_unlocked (DBusConnection \*connection,

3832 DBusMessage \*head_of_queue)

3833{

3834 HAVE_LOCK_CHECK (connection);

3835

3836 /\* checking that the link is NULL is an optimization to avoid the is_signal call \*/

3837 if (connection-\>disconnect_message_link == NULL &&

3838 dbus_message_is_signal (head_of_queue,

3839 DBUS_INTERFACE_LOCAL,

3840 "Disconnected"))

3841 {

3842 connection-\>disconnected_message_arrived = TRUE;

3843 }

3844}

3845

3865DBusMessage\*

3866dbus_connection_borrow_message (DBusConnection \*connection)

3867{

3868 DBusDispatchStatus status;

3869 DBusMessage \*message;

3870

3871 \_dbus_return_val_if_fail (connection != NULL, NULL);

3872

3873 \_dbus_verbose ("start\n");

3874

3875 /\* this is called for the side effect that it queues

3876 \* up any messages from the transport

3877 \*/

3878 status = dbus_connection_get_dispatch_status (connection);

3879 if (status != DBUS_DISPATCH_DATA_REMAINS)

3880 return NULL;

3881

3882 CONNECTION_LOCK (connection);

3883

3884 \_dbus_connection_acquire_dispatch (connection);

3885

3886 /\* While a message is outstanding, the dispatch lock is held \*/

3887 \_dbus_assert (connection-\>message_borrowed == NULL);

3888

3889 connection-\>message_borrowed = \_dbus_list_get_first (&connection-\>incoming_messages);

3890

3891 message = connection-\>message_borrowed;

3892

3893 check_disconnected_message_arrived_unlocked (connection, message);

3894

3895 /\* Note that we KEEP the dispatch lock until the message is returned \*/

3896 if (message == NULL)

3897 \_dbus_connection_release_dispatch (connection);

3898

3899 CONNECTION_UNLOCK (connection);

3900

3901 \_dbus_message_trace_ref (message, -1, -1, "dbus_connection_borrow_message");

3902

3903 /\* We don't update dispatch status until it's returned or stolen \*/

3904

3905 return message;

3906}

3907

3916void

3917dbus_connection_return_message (DBusConnection \*connection,

3918 DBusMessage \*message)

3919{

3920 DBusDispatchStatus status;

3921

3922 \_dbus_return_if_fail (connection != NULL);

3923 \_dbus_return_if_fail (message != NULL);

3924 \_dbus_return_if_fail (message == connection-\>message_borrowed);

3925 \_dbus_return_if_fail (connection-\>dispatch_acquired);

3926

3927 CONNECTION_LOCK (connection);

3928

3929 \_dbus_assert (message == connection-\>message_borrowed);

3930

3931 connection-\>message_borrowed = NULL;

3932

3933 \_dbus_connection_release_dispatch (connection);

3934

3935 status = \_dbus_connection_get_dispatch_status_unlocked (connection);

3936 \_dbus_connection_update_dispatch_status_and_unlock (connection, status);

3937

3938 \_dbus_message_trace_ref (message, -1, -1, "dbus_connection_return_message");

3939}

3940

3950void

3951dbus_connection_steal_borrowed_message (DBusConnection \*connection,

3952 DBusMessage \*message)

3953{

3954 DBusMessage \*pop_message;

3955 DBusDispatchStatus status;

3956

3957 \_dbus_return_if_fail (connection != NULL);

3958 \_dbus_return_if_fail (message != NULL);

3959 \_dbus_return_if_fail (message == connection-\>message_borrowed);

3960 \_dbus_return_if_fail (connection-\>dispatch_acquired);

3961

3962 CONNECTION_LOCK (connection);

3963

3964 \_dbus_assert (message == connection-\>message_borrowed);

3965

3966 pop_message = \_dbus_list_pop_first (&connection-\>incoming_messages);

3967 \_dbus_assert (message == pop_message);

3968 (void) pop_message; /\* unused unless asserting \*/

3969

3970 connection-\>n_incoming -= 1;

3971

3972 \_dbus_verbose ("Incoming message %p stolen from queue, %d incoming\n",

3973 message, connection-\>n_incoming);

3974

3975 connection-\>message_borrowed = NULL;

3976

3977 \_dbus_connection_release_dispatch (connection);

3978

3979 status = \_dbus_connection_get_dispatch_status_unlocked (connection);

3980 \_dbus_connection_update_dispatch_status_and_unlock (connection, status);

3981 \_dbus_message_trace_ref (message, -1, -1,

3982 "dbus_connection_steal_borrowed_message");

3983}

3984

3985/\* See dbus_connection_pop_message, but requires the caller to own

3986 \* the lock before calling. May drop the lock while running.

3987 \*/

3988static DBusList\*

3989\_dbus_connection_pop_message_link_unlocked (DBusConnection \*connection)

3990{

3991 HAVE_LOCK_CHECK (connection);

3992

3993 \_dbus_assert (connection-\>message_borrowed == NULL);

3994

3995 if (connection-\>n_incoming \> 0)

3996 {

3997 DBusList \*link;

3998

3999 link = \_dbus_list_pop_first_link (&connection-\>incoming_messages);

4000 connection-\>n_incoming -= 1;

4001

4002 \_dbus_verbose ("Message %p (%s %s %s %s sig:'%s' serial:%u) removed from incoming queue %p, %d incoming\n",

4003 link-\>data,

4004 dbus_message_type_to_string (dbus_message_get_type (link-\>data)),

4005 dbus_message_get_path (link-\>data) ?

4006 dbus_message_get_path (link-\>data) :

4007 "no path",

4008 dbus_message_get_interface (link-\>data) ?

4009 dbus_message_get_interface (link-\>data) :

4010 "no interface",

4011 dbus_message_get_member (link-\>data) ?

4012 dbus_message_get_member (link-\>data) :

4013 "no member",

4014 dbus_message_get_signature (link-\>data),

4015 dbus_message_get_serial (link-\>data),

4016 connection, connection-\>n_incoming);

4017

4018 \_dbus_message_trace_ref (link-\>data, -1, -1,

4019 "\_dbus_connection_pop_message_link_unlocked");

4020

4021 check_disconnected_message_arrived_unlocked (connection, link-\>data);

4022

4023 return link;

4024 }

4025 else

4026 return NULL;

4027}

4028

4029/\* See dbus_connection_pop_message, but requires the caller to own

4030 \* the lock before calling. May drop the lock while running.

4031 \*/

4032static DBusMessage\*

4033\_dbus_connection_pop_message_unlocked (DBusConnection \*connection)

4034{

4035 DBusList \*link;

4036

4037 HAVE_LOCK_CHECK (connection);

4038

4039 link = \_dbus_connection_pop_message_link_unlocked (connection);

4040

4041 if (link != NULL)

4042 {

4043 DBusMessage \*message;

4044

4045 message = link-\>data;

4046

4047 \_dbus_list_free_link (link);

4048

4049 return message;

4050 }

4051 else

4052 return NULL;

4053}

4054

4055static void

4056\_dbus_connection_putback_message_link_unlocked (DBusConnection \*connection,

4057 DBusList \*message_link)

4058{

4059 HAVE_LOCK_CHECK (connection);

4060

4061 \_dbus_assert (message_link != NULL);

4062 /\* You can't borrow a message while a link is outstanding \*/

4063 \_dbus_assert (connection-\>message_borrowed == NULL);

4064 /\* We had to have the dispatch lock across the pop/putback \*/

4065 \_dbus_assert (connection-\>dispatch_acquired);

4066

4067 \_dbus_list_prepend_link (&connection-\>incoming_messages,

4068 message_link);

4069 connection-\>n_incoming += 1;

4070

4071 \_dbus_verbose ("Message %p (%s %s %s '%s') put back into queue %p, %d incoming\n",

4072 message_link-\>data,

4073 dbus_message_type_to_string (dbus_message_get_type (message_link-\>data)),

4074 dbus_message_get_interface (message_link-\>data) ?

4075 dbus_message_get_interface (message_link-\>data) :

4076 "no interface",

4077 dbus_message_get_member (message_link-\>data) ?

4078 dbus_message_get_member (message_link-\>data) :

4079 "no member",

4080 dbus_message_get_signature (message_link-\>data),

4081 connection, connection-\>n_incoming);

4082

4083 \_dbus_message_trace_ref (message_link-\>data, -1, -1,

4084 "\_dbus_connection_putback_message_link_unlocked");

4085}

4086

4106DBusMessage\*

4107dbus_connection_pop_message (DBusConnection \*connection)

4108{

4109 DBusMessage \*message;

4110 DBusDispatchStatus status;

4111

4112 \_dbus_verbose ("start\n");

4113

4114 /\* this is called for the side effect that it queues

4115 \* up any messages from the transport

4116 \*/

4117 status = dbus_connection_get_dispatch_status (connection);

4118 if (status != DBUS_DISPATCH_DATA_REMAINS)

4119 return NULL;

4120

4121 CONNECTION_LOCK (connection);

4122 \_dbus_connection_acquire_dispatch (connection);

4123 HAVE_LOCK_CHECK (connection);

4124

4125 message = \_dbus_connection_pop_message_unlocked (connection);

4126

4127 \_dbus_verbose ("Returning popped message %p\n", message);

4128

4129 \_dbus_connection_release_dispatch (connection);

4130

4131 status = \_dbus_connection_get_dispatch_status_unlocked (connection);

4132 \_dbus_connection_update_dispatch_status_and_unlock (connection, status);

4133

4134 return message;

4135}

4136

4144static void

4145\_dbus_connection_acquire_dispatch (DBusConnection \*connection)

4146{

4147 HAVE_LOCK_CHECK (connection);

4148

4149 \_dbus_connection_ref_unlocked (connection);

4150 CONNECTION_UNLOCK (connection);

4151

4152 \_dbus_verbose ("locking dispatch_mutex\n");

4153 \_dbus_cmutex_lock (connection-\>dispatch_mutex);

4154

4155 while (connection-\>dispatch_acquired)

4156 {

4157 \_dbus_verbose ("waiting for dispatch to be acquirable\n");

4158 \_dbus_condvar_wait (connection-\>dispatch_cond,

4159 connection-\>dispatch_mutex);

4160 }

4161

4162 \_dbus_assert (!connection-\>dispatch_acquired);

4163

4164 connection-\>dispatch_acquired = TRUE;

4165

4166 \_dbus_verbose ("unlocking dispatch_mutex\n");

4167 \_dbus_cmutex_unlock (connection-\>dispatch_mutex);

4168

4169 CONNECTION_LOCK (connection);

4170 \_dbus_connection_unref_unlocked (connection);

4171}

4172

4180static void

4181\_dbus_connection_release_dispatch (DBusConnection \*connection)

4182{

4183 HAVE_LOCK_CHECK (connection);

4184

4185 \_dbus_verbose ("locking dispatch_mutex\n");

4186 \_dbus_cmutex_lock (connection-\>dispatch_mutex);

4187

4188 \_dbus_assert (connection-\>dispatch_acquired);

4189

4190 connection-\>dispatch_acquired = FALSE;

4191 \_dbus_condvar_wake_one (connection-\>dispatch_cond);

4192

4193 \_dbus_verbose ("unlocking dispatch_mutex\n");

4194 \_dbus_cmutex_unlock (connection-\>dispatch_mutex);

4195}

4196

4197static void

4198\_dbus_connection_failed_pop (DBusConnection \*connection,

4199 DBusList \*message_link)

4200{

4201 \_dbus_list_prepend_link (&connection-\>incoming_messages,

4202 message_link);

4203 connection-\>n_incoming += 1;

4204}

4205

4206/\* Note this may be called multiple times since we don't track whether we already did it \*/

4207static void

4208notify_disconnected_unlocked (DBusConnection \*connection)

4209{

4210 HAVE_LOCK_CHECK (connection);

4211

4212 /\* Set the weakref in dbus-bus.c to NULL, so nobody will get a disconnected

4213 \* connection from dbus_bus_get(). We make the same guarantee for

4214 \* dbus_connection_open() but in a different way since we don't want to

4215 \* unref right here; we instead check for connectedness before returning

4216 \* the connection from the hash.

4217 \*/

4218 \_dbus_bus_notify_shared_connection_disconnected_unlocked (connection);

4219

4220 /\* Dump the outgoing queue, we aren't going to be able to

4221 \* send it now, and we'd like accessors like

4222 \* dbus_connection_get_outgoing_size() to be accurate.

4223 \*/

4224 if (connection-\>n_outgoing \> 0)

4225 {

4226 DBusList \*link;

4227

4228 \_dbus_verbose ("Dropping %d outgoing messages since we're disconnected\n",

4229 connection-\>n_outgoing);

4230

4231 while ((link = \_dbus_list_get_last_link (&connection-\>outgoing_messages)))

4232 {

4233 \_dbus_connection_message_sent_unlocked (connection, link-\>data);

4234 }

4235 }

4236}

4237

4238/\* Note this may be called multiple times since we don't track whether we already did it \*/

4239static DBusDispatchStatus

4240notify_disconnected_and_dispatch_complete_unlocked (DBusConnection \*connection)

4241{

4242 HAVE_LOCK_CHECK (connection);

4243

4244 if (connection-\>disconnect_message_link != NULL)

4245 {

4246 \_dbus_verbose ("Sending disconnect message\n");

4247

4248 /\* If we have pending calls, queue their timeouts - we want the Disconnected

4249 \* to be the last message, after these timeouts.

4250 \*/

4251 connection_timeout_and_complete_all_pending_calls_unlocked (connection);

4252

4253 /\* We haven't sent the disconnect message already,

4254 \* and all real messages have been queued up.

4255 \*/

4256 \_dbus_connection_queue_synthesized_message_link (connection,

4257 connection-\>disconnect_message_link);

4258 connection-\>disconnect_message_link = NULL;

4259

4260 return DBUS_DISPATCH_DATA_REMAINS;

4261 }

4262

4263 return DBUS_DISPATCH_COMPLETE;

4264}

4265

4266static DBusDispatchStatus

4267\_dbus_connection_get_dispatch_status_unlocked (DBusConnection \*connection)

4268{

4269 HAVE_LOCK_CHECK (connection);

4270

4271 if (connection-\>n_incoming \> 0)

4272 return DBUS_DISPATCH_DATA_REMAINS;

4273 else if (!\_dbus_transport_queue_messages (connection-\>transport))

4274 return DBUS_DISPATCH_NEED_MEMORY;

4275 else

4276 {

4277 DBusDispatchStatus status;

4278 dbus_bool_t is_connected;

4279

4280 status = \_dbus_transport_get_dispatch_status (connection-\>transport);

4281 is_connected = \_dbus_transport_get_is_connected (connection-\>transport);

4282

4283 \_dbus_verbose ("dispatch status = %s is_connected = %d\n",

4284 DISPATCH_STATUS_NAME (status), is_connected);

4285

4286 if (!is_connected)

4287 {

4288 /\* It's possible this would be better done by having an explicit

4289 \* notification from \_dbus_transport_disconnect() that would

4290 \* synchronously do this, instead of waiting for the next dispatch

4291 \* status check. However, probably not good to change until it causes

4292 \* a problem.

4293 \*/

4294 notify_disconnected_unlocked (connection);

4295

4296 /\* I'm not sure this is needed; the idea is that we want to

4297 \* queue the Disconnected only after we've read all the

4298 \* messages, but if we're disconnected maybe we are guaranteed

4299 \* to have read them all ?

4300 \*/

4301 if (status == DBUS_DISPATCH_COMPLETE)

4302 status = notify_disconnected_and_dispatch_complete_unlocked (connection);

4303 }

4304

4305 if (status != DBUS_DISPATCH_COMPLETE)

4306 return status;

4307 else if (connection-\>n_incoming \> 0)

4308 return DBUS_DISPATCH_DATA_REMAINS;

4309 else

4310 return DBUS_DISPATCH_COMPLETE;

4311 }

4312}

4313

4314static void

4315\_dbus_connection_update_dispatch_status_and_unlock (DBusConnection \*connection,

4316 DBusDispatchStatus new_status)

4317{

4318 dbus_bool_t changed;

4319 DBusDispatchStatusFunction function;

4320 void \*data;

4321

4322 HAVE_LOCK_CHECK (connection);

4323

4324 \_dbus_connection_ref_unlocked (connection);

4325

4326 changed = new_status != connection-\>last_dispatch_status;

4327

4328 connection-\>last_dispatch_status = new_status;

4329

4330 function = connection-\>dispatch_status_function;

4331 data = connection-\>dispatch_status_data;

4332

4333 if (connection-\>disconnected_message_arrived &&

4334 !connection-\>disconnected_message_processed)

4335 {

4336 connection-\>disconnected_message_processed = TRUE;

4337

4338 /\* this does an unref, but we have a ref

4339 \* so we should not run the finalizer here

4340 \* inside the lock.

4341 \*/

4342 connection_forget_shared_unlocked (connection);

4343

4344 if (connection-\>exit_on_disconnect)

4345 {

4346 CONNECTION_UNLOCK (connection);

4347

4348 \_dbus_verbose ("Exiting on Disconnected signal\n");

4349 \_dbus_exit (1);

4350 \_dbus_assert_not_reached ("Call to exit() returned");

4351 }

4352 }

4353

4354 /\* We drop the lock \*/

4355 CONNECTION_UNLOCK (connection);

4356

4357 if (changed && function)

4358 {

4359 \_dbus_verbose ("Notifying of change to dispatch status of %p now %d (%s)\n",

4360 connection, new_status,

4361 DISPATCH_STATUS_NAME (new_status));

4362 (\* function) (connection, new_status, data);

4363 }

4364

4365 dbus_connection_unref (connection);

4366}

4367

4393DBusDispatchStatus

4394dbus_connection_get_dispatch_status (DBusConnection \*connection)

4395{

4396 DBusDispatchStatus status;

4397

4398 \_dbus_return_val_if_fail (connection != NULL, DBUS_DISPATCH_COMPLETE);

4399

4400 \_dbus_verbose ("start\n");

4401

4402 CONNECTION_LOCK (connection);

4403

4404 status = \_dbus_connection_get_dispatch_status_unlocked (connection);

4405

4406 CONNECTION_UNLOCK (connection);

4407

4408 return status;

4409}

4410

4414static DBusHandlerResult

4415\_dbus_connection_peer_filter_unlocked_no_update (DBusConnection \*connection,

4416 DBusMessage \*message)

4417{

4418 dbus_bool_t sent = FALSE;

4419 DBusMessage \*ret = NULL;

4420 DBusList \*expire_link;

4421

4422 if (connection-\>route_peer_messages && dbus_message_get_destination (message) != NULL)

4423 {

4424 /\* This means we're letting the bus route this message \*/

4425 return DBUS_HANDLER_RESULT_NOT_YET_HANDLED;

4426 }

4427

4428 if (!dbus_message_has_interface (message, DBUS_INTERFACE_PEER))

4429 {

4430 return DBUS_HANDLER_RESULT_NOT_YET_HANDLED;

4431 }

4432

4433 /\* Preallocate a linked-list link, so that if we need to dispose of a

4434 \* message, we can attach it to the expired list \*/

4435 expire_link = \_dbus_list_alloc_link (NULL);

4436

4437 if (!expire_link)

4438 return DBUS_HANDLER_RESULT_NEED_MEMORY;

4439

4440 if (dbus_message_is_method_call (message,

4441 DBUS_INTERFACE_PEER,

4442 "Ping"))

4443 {

4444 ret = dbus_message_new_method_return (message);

4445 if (ret == NULL)

4446 goto out;

4447

4448 sent = \_dbus_connection_send_unlocked_no_update (connection, ret, NULL);

4449 }

4450 else if (dbus_message_is_method_call (message,

4451 DBUS_INTERFACE_PEER,

4452 "GetMachineId"))

4453 {

4454 DBusString uuid;

4455 DBusError error = DBUS_ERROR_INIT;

4456

4457 if (!\_dbus_string_init (&uuid))

4458 goto out;

4459

4460 if (\_dbus_get_local_machine_uuid_encoded (&uuid, &error))

4461 {

4462 const char \*v_STRING;

4463

4464 ret = dbus_message_new_method_return (message);

4465

4466 if (ret == NULL)

4467 {

4468 \_dbus_string_free (&uuid);

4469 goto out;

4470 }

4471

4472 v_STRING = \_dbus_string_get_const_data (&uuid);

4473 if (dbus_message_append_args (ret,

4474 DBUS_TYPE_STRING, &v_STRING,

4475 DBUS_TYPE_INVALID))

4476 {

4477 sent = \_dbus_connection_send_unlocked_no_update (connection, ret, NULL);

4478 }

4479 }

4480 else if (dbus_error_has_name (&error, DBUS_ERROR_NO_MEMORY))

4481 {

4482 dbus_error_free (&error);

4483 goto out;

4484 }

4485 else

4486 {

4487 ret = dbus_message_new_error (message, error.name, error.message);

4488 dbus_error_free (&error);

4489

4490 if (ret == NULL)

4491 goto out;

4492

4493 sent = \_dbus_connection_send_unlocked_no_update (connection, ret,

4494 NULL);

4495 }

4496

4497 \_dbus_string_free (&uuid);

4498 }

4499 else

4500 {

4501 /\* We need to bounce anything else with this interface, otherwise apps

4502 \* could start extending the interface and when we added extensions

4503 \* here to DBusConnection we'd break those apps.

4504 \*/

4505 ret = dbus_message_new_error (message,

4506 DBUS_ERROR_UNKNOWN_METHOD,

4507 "Unknown method invoked on org.freedesktop.DBus.Peer interface");

4508 if (ret == NULL)

4509 goto out;

4510

4511 sent = \_dbus_connection_send_unlocked_no_update (connection, ret, NULL);

4512 }

4513

4514out:

4515 if (ret == NULL)

4516 {

4517 \_dbus_list_free_link (expire_link);

4518 }

4519 else

4520 {

4521 /\* It'll be safe to unref the reply when we unlock \*/

4522 expire_link-\>data = ret;

4523 \_dbus_list_prepend_link (&connection-\>expired_messages, expire_link);

4524 }

4525

4526 if (!sent)

4527 return DBUS_HANDLER_RESULT_NEED_MEMORY;

4528

4529 return DBUS_HANDLER_RESULT_HANDLED;

4530}

4531

4538static DBusHandlerResult

4539\_dbus_connection_run_builtin_filters_unlocked_no_update (DBusConnection \*connection,

4540 DBusMessage \*message)

4541{

4542 /\* We just run one filter for now but have the option to run more

4543 if the spec calls for it in the future \*/

4544

4545 return \_dbus_connection_peer_filter_unlocked_no_update (connection, message);

4546}

4547

4590DBusDispatchStatus

4591dbus_connection_dispatch (DBusConnection \*connection)

4592{

4593 DBusMessage \*message;

4594 DBusList \*link, \*filter_list_copy, \*message_link;

4595 DBusHandlerResult result;

4596 DBusPendingCall \*pending;

4597 dbus_int32_t reply_serial;

4598 DBusDispatchStatus status;

4599 dbus_bool_t found_object;

4600

4601 \_dbus_return_val_if_fail (connection != NULL, DBUS_DISPATCH_COMPLETE);

4602

4603 \_dbus_verbose ("\n");

4604

4605 CONNECTION_LOCK (connection);

4606 status = \_dbus_connection_get_dispatch_status_unlocked (connection);

4607 if (status != DBUS_DISPATCH_DATA_REMAINS)

4608 {

4609 /\* unlocks and calls out to user code \*/

4610 \_dbus_connection_update_dispatch_status_and_unlock (connection, status);

4611 return status;

4612 }

4613

4614 /\* We need to ref the connection since the callback could potentially

4615 \* drop the last ref to it

4616 \*/

4617 \_dbus_connection_ref_unlocked (connection);

4618

4619 \_dbus_connection_acquire_dispatch (connection);

4620 HAVE_LOCK_CHECK (connection);

4621

4622 message_link = \_dbus_connection_pop_message_link_unlocked (connection);

4623 if (message_link == NULL)

4624 {

4625 /\* another thread dispatched our stuff \*/

4626

4627 \_dbus_verbose ("another thread dispatched message (during acquire_dispatch above)\n");

4628

4629 \_dbus_connection_release_dispatch (connection);

4630

4631 status = \_dbus_connection_get_dispatch_status_unlocked (connection);

4632

4633 \_dbus_connection_update_dispatch_status_and_unlock (connection, status);

4634

4635 dbus_connection_unref (connection);

4636

4637 return status;

4638 }

4639

4640 message = message_link-\>data;

4641

4642 \_dbus_verbose (" dispatching message %p (%s %s %s '%s')\n",

4643 message,

4644 dbus_message_type_to_string (dbus_message_get_type (message)),

4645 dbus_message_get_interface (message) ?

4646 dbus_message_get_interface (message) :

4647 "no interface",

4648 dbus_message_get_member (message) ?

4649 dbus_message_get_member (message) :

4650 "no member",

4651 dbus_message_get_signature (message));

4652

4653 result = DBUS_HANDLER_RESULT_NOT_YET_HANDLED;

4654

4655 /\* Pending call handling must be first, because if you do

4656 \* dbus_connection_send_with_reply_and_block() or

4657 \* dbus_pending_call_block() then no handlers/filters will be run on

4658 \* the reply. We want consistent semantics in the case where we

4659 \* dbus_connection_dispatch() the reply.

4660 \*/

4661

4662 reply_serial = dbus_message_get_reply_serial (message);

4663 pending = \_dbus_hash_table_lookup_int (connection-\>pending_replies,

4664 reply_serial);

4665 if (pending)

4666 {

4667 \_dbus_verbose ("Dispatching a pending reply\n");

4668 complete_pending_call_and_unlock (connection, pending, message);

4669 pending = NULL; /\* it's probably unref'd \*/

4670

4671 CONNECTION_LOCK (connection);

4672 \_dbus_verbose ("pending call completed in dispatch\n");

4673 result = DBUS_HANDLER_RESULT_HANDLED;

4674 goto out;

4675 }

4676

4677 /\* If skipping builtin filters, we are probably a monitor. \*/

4678 if (connection-\>builtin_filters_enabled)

4679 {

4680 result = \_dbus_connection_run_builtin_filters_unlocked_no_update (connection, message);

4681 if (result != DBUS_HANDLER_RESULT_NOT_YET_HANDLED)

4682 goto out;

4683 }

4684

4685 if (!\_dbus_list_copy (&connection-\>filter_list, &filter_list_copy))

4686 {

4687 \_dbus_connection_release_dispatch (connection);

4688 HAVE_LOCK_CHECK (connection);

4689

4690 \_dbus_connection_failed_pop (connection, message_link);

4691

4692 /\* unlocks and calls user code \*/

4693 \_dbus_connection_update_dispatch_status_and_unlock (connection,

4694 DBUS_DISPATCH_NEED_MEMORY);

4695 dbus_connection_unref (connection);

4696

4697 return DBUS_DISPATCH_NEED_MEMORY;

4698 }

4699

4700 for (link = \_dbus_list_get_first_link (&filter_list_copy);

4701 link != NULL;

4702 link = \_dbus_list_get_next_link (&filter_list_copy, link))

4703 \_dbus_message_filter_ref (link-\>data);

4704

4705 /\* We're still protected from dispatch() reentrancy here

4706 \* since we acquired the dispatcher

4707 \*/

4708 CONNECTION_UNLOCK (connection);

4709

4710 link = \_dbus_list_get_first_link (&filter_list_copy);

4711 while (link != NULL)

4712 {

4713 DBusMessageFilter \*filter = link-\>data;

4714 DBusList \*next = \_dbus_list_get_next_link (&filter_list_copy, link);

4715

4716 if (filter-\>function == NULL)

4717 {

4718 \_dbus_verbose (" filter was removed in a callback function\n");

4719 link = next;

4720 continue;

4721 }

4722

4723 \_dbus_verbose (" running filter on message %p\n", message);

4724 result = (\* filter-\>function) (connection, message, filter-\>user_data);

4725

4726 if (result != DBUS_HANDLER_RESULT_NOT_YET_HANDLED)

4727 break;

4728

4729 link = next;

4730 }

4731

4732 \_dbus_list_clear_full (&filter_list_copy,

4733 (DBusFreeFunction) \_dbus_message_filter_unref);

4734

4735 CONNECTION_LOCK (connection);

4736

4737 if (result == DBUS_HANDLER_RESULT_NEED_MEMORY)

4738 {

4739 \_dbus_verbose ("No memory\n");

4740 goto out;

4741 }

4742 else if (result == DBUS_HANDLER_RESULT_HANDLED)

4743 {

4744 \_dbus_verbose ("filter handled message in dispatch\n");

4745 goto out;

4746 }

4747

4748 /\* We're still protected from dispatch() reentrancy here

4749 \* since we acquired the dispatcher

4750 \*/

4751 \_dbus_verbose (" running object path dispatch on message %p (%s %s %s '%s')\n",

4752 message,

4753 dbus_message_type_to_string (dbus_message_get_type (message)),

4754 dbus_message_get_interface (message) ?

4755 dbus_message_get_interface (message) :

4756 "no interface",

4757 dbus_message_get_member (message) ?

4758 dbus_message_get_member (message) :

4759 "no member",

4760 dbus_message_get_signature (message));

4761

4762 HAVE_LOCK_CHECK (connection);

4763 result = \_dbus_object_tree_dispatch_and_unlock (connection-\>objects,

4764 message,

4765 &found_object);

4766

4767 CONNECTION_LOCK (connection);

4768

4769 if (result != DBUS_HANDLER_RESULT_NOT_YET_HANDLED)

4770 {

4771 \_dbus_verbose ("object tree handled message in dispatch\n");

4772 goto out;

4773 }

4774

4775 if (dbus_message_get_type (message) == DBUS_MESSAGE_TYPE_METHOD_CALL)

4776 {

4777 DBusMessage \*reply;

4778 DBusString str;

4779 DBusPreallocatedSend \*preallocated;

4780 DBusList \*expire_link;

4781

4782 \_dbus_verbose (" sending error %s\n",

4783 DBUS_ERROR_UNKNOWN_METHOD);

4784

4785 if (!\_dbus_string_init (&str))

4786 {

4787 result = DBUS_HANDLER_RESULT_NEED_MEMORY;

4788 \_dbus_verbose ("no memory for error string in dispatch\n");

4789 goto out;

4790 }

4791

4792 if (!\_dbus_string_append_printf (&str,

4793 "Method \\%s\\ with signature \\%s\\ on interface \\%s\\ doesn't exist\n",

4794 dbus_message_get_member (message),

4795 dbus_message_get_signature (message),

4796 dbus_message_get_interface (message)))

4797 {

4798 \_dbus_string_free (&str);

4799 result = DBUS_HANDLER_RESULT_NEED_MEMORY;

4800 \_dbus_verbose ("no memory for error string in dispatch\n");

4801 goto out;

4802 }

4803

4804 reply = dbus_message_new_error (message,

4805 found_object ? DBUS_ERROR_UNKNOWN_METHOD : DBUS_ERROR_UNKNOWN_OBJECT,

4806 \_dbus_string_get_const_data (&str));

4807 \_dbus_string_free (&str);

4808

4809 if (reply == NULL)

4810 {

4811 result = DBUS_HANDLER_RESULT_NEED_MEMORY;

4812 \_dbus_verbose ("no memory for error reply in dispatch\n");

4813 goto out;

4814 }

4815

4816 expire_link = \_dbus_list_alloc_link (reply);

4817

4818 if (expire_link == NULL)

4819 {

4820 dbus_message_unref (reply);

4821 result = DBUS_HANDLER_RESULT_NEED_MEMORY;

4822 \_dbus_verbose ("no memory for error send in dispatch\n");

4823 goto out;

4824 }

4825

4826 preallocated = \_dbus_connection_preallocate_send_unlocked (connection);

4827

4828 if (preallocated == NULL)

4829 {

4830 \_dbus_list_free_link (expire_link);

4831 /\* It's OK that this is finalized, because it hasn't been seen by

4832 \* anything that could attach user callbacks \*/

4833 dbus_message_unref (reply);

4834 result = DBUS_HANDLER_RESULT_NEED_MEMORY;

4835 \_dbus_verbose ("no memory for error send in dispatch\n");

4836 goto out;

4837 }

4838

4839 \_dbus_connection_send_preallocated_unlocked_no_update (connection, preallocated,

4840 reply, NULL);

4841 /\* reply will be freed when we release the lock \*/

4842 \_dbus_list_prepend_link (&connection-\>expired_messages, expire_link);

4843

4844 result = DBUS_HANDLER_RESULT_HANDLED;

4845 }

4846

4847 \_dbus_verbose (" done dispatching %p (%s %s %s '%s') on connection %p\n", message,

4848 dbus_message_type_to_string (dbus_message_get_type (message)),

4849 dbus_message_get_interface (message) ?

4850 dbus_message_get_interface (message) :

4851 "no interface",

4852 dbus_message_get_member (message) ?

4853 dbus_message_get_member (message) :

4854 "no member",

4855 dbus_message_get_signature (message),

4856 connection);

4857

4858 out:

4859 if (result == DBUS_HANDLER_RESULT_NEED_MEMORY)

4860 {

4861 \_dbus_verbose ("out of memory\n");

4862

4863 /\* Put message back, and we'll start over.

4864 \* Yes this means handlers must be idempotent if they

4865 \* don't return HANDLED; c'est la vie.

4866 \*/

4867 \_dbus_connection_putback_message_link_unlocked (connection,

4868 message_link);

4869 /\* now we don't want to free them \*/

4870 message_link = NULL;

4871 message = NULL;

4872 }

4873 else

4874 {

4875 \_dbus_verbose (" ... done dispatching\n");

4876 }

4877

4878 \_dbus_connection_release_dispatch (connection);

4879 HAVE_LOCK_CHECK (connection);

4880

4881 if (message != NULL)

4882 {

4883 /\* We don't want this message to count in maximum message limits when

4884 \* computing the dispatch status, below. We have to drop the lock

4885 \* temporarily, because finalizing a message can trigger callbacks.

4886 \*

4887 \* We have a reference to the connection, and we don't use any cached

4888 \* pointers to the connection's internals below this point, so it should

4889 \* be safe to drop the lock and take it back. \*/

4890 CONNECTION_UNLOCK (connection);

4891 dbus_message_unref (message);

4892 CONNECTION_LOCK (connection);

4893 }

4894

4895 if (message_link != NULL)

4896 \_dbus_list_free_link (message_link);

4897

4898 \_dbus_verbose ("before final status update\n");

4899 status = \_dbus_connection_get_dispatch_status_unlocked (connection);

4900

4901 /\* unlocks and calls user code \*/

4902 \_dbus_connection_update_dispatch_status_and_unlock (connection, status);

4903

4904 dbus_connection_unref (connection);

4905

4906 return status;

4907}

4908

4970dbus_bool_t

4971dbus_connection_set_watch_functions (DBusConnection \*connection,

4972 DBusAddWatchFunction add_function,

4973 DBusRemoveWatchFunction remove_function,

4974 DBusWatchToggledFunction toggled_function,

4975 void \*data,

4976 DBusFreeFunction free_data_function)

4977{

4978 dbus_bool_t retval;

4979

4980 \_dbus_return_val_if_fail (connection != NULL, FALSE);

4981

4982 CONNECTION_LOCK (connection);

4983

4984 retval = \_dbus_watch_list_set_functions (connection-\>watches,

4985 add_function, remove_function,

4986 toggled_function,

4987 data, free_data_function);

4988

4989 CONNECTION_UNLOCK (connection);

4990

4991 return retval;

4992}

4993

5033dbus_bool_t

5034dbus_connection_set_timeout_functions (DBusConnection \*connection,

5035 DBusAddTimeoutFunction add_function,

5036 DBusRemoveTimeoutFunction remove_function,

5037 DBusTimeoutToggledFunction toggled_function,

5038 void \*data,

5039 DBusFreeFunction free_data_function)

5040{

5041 dbus_bool_t retval;

5042

5043 \_dbus_return_val_if_fail (connection != NULL, FALSE);

5044

5045 CONNECTION_LOCK (connection);

5046

5047 retval = \_dbus_timeout_list_set_functions (connection-\>timeouts,

5048 add_function, remove_function,

5049 toggled_function,

5050 data, free_data_function);

5051

5052 CONNECTION_UNLOCK (connection);

5053

5054 return retval;

5055}

5056

5071void

5072dbus_connection_set_wakeup_main_function (DBusConnection \*connection,

5073 DBusWakeupMainFunction wakeup_main_function,

5074 void \*data,

5075 DBusFreeFunction free_data_function)

5076{

5077 void \*old_data;

5078 DBusFreeFunction old_free_data;

5079

5080 \_dbus_return_if_fail (connection != NULL);

5081

5082 CONNECTION_LOCK (connection);

5083 old_data = connection-\>wakeup_main_data;

5084 old_free_data = connection-\>free_wakeup_main_data;

5085

5086 connection-\>wakeup_main_function = wakeup_main_function;

5087 connection-\>wakeup_main_data = data;

5088 connection-\>free_wakeup_main_data = free_data_function;

5089

5090 CONNECTION_UNLOCK (connection);

5091

5092 /\* Callback outside the lock \*/

5093 if (old_free_data)

5094 (\*old_free_data) (old_data);

5095}

5096

5117void

5118dbus_connection_set_dispatch_status_function (DBusConnection \*connection,

5119 DBusDispatchStatusFunction function,

5120 void \*data,

5121 DBusFreeFunction free_data_function)

5122{

5123 void \*old_data;

5124 DBusFreeFunction old_free_data;

5125

5126 \_dbus_return_if_fail (connection != NULL);

5127

5128 CONNECTION_LOCK (connection);

5129 old_data = connection-\>dispatch_status_data;

5130 old_free_data = connection-\>free_dispatch_status_data;

5131

5132 connection-\>dispatch_status_function = function;

5133 connection-\>dispatch_status_data = data;

5134 connection-\>free_dispatch_status_data = free_data_function;

5135

5136 CONNECTION_UNLOCK (connection);

5137

5138 /\* Callback outside the lock \*/

5139 if (old_free_data)

5140 (\*old_free_data) (old_data);

5141}

5142

5162dbus_bool_t

5163dbus_connection_get_unix_fd (DBusConnection \*connection,

5164 int \*fd)

5165{

5166 \_dbus_return_val_if_fail (connection != NULL, FALSE);

5167 \_dbus_return_val_if_fail (connection-\>transport != NULL, FALSE);

5168

5169\#ifdef DBUS_WIN

5170 /\* FIXME do this on a lower level \*/

5171 return FALSE;

5172\#endif

5173

5174 return dbus_connection_get_socket(connection, fd);

5175}

5176

5192dbus_bool_t

5193dbus_connection_get_socket(DBusConnection \*connection,

5194 int \*fd)

5195{

5196 dbus_bool_t retval;

5197 DBusSocket s = DBUS_SOCKET_INIT;

5198

5199 \_dbus_return_val_if_fail (connection != NULL, FALSE);

5200 \_dbus_return_val_if_fail (connection-\>transport != NULL, FALSE);

5201

5202 CONNECTION_LOCK (connection);

5203

5204 retval = \_dbus_transport_get_socket_fd (connection-\>transport, &s);

5205

5206 if (retval)

5207 {

5208 \*fd = \_dbus_socket_get_int (s);

5209 }

5210

5211 CONNECTION_UNLOCK (connection);

5212

5213 return retval;

5214}

5215

5216

5239dbus_bool_t

5240dbus_connection_get_unix_user (DBusConnection \*connection,

5241 unsigned long \*uid)

5242{

5243 dbus_bool_t result;

5244

5245 \_dbus_return_val_if_fail (connection != NULL, FALSE);

5246 \_dbus_return_val_if_fail (uid != NULL, FALSE);

5247

5248 CONNECTION_LOCK (connection);

5249

5250 if (!\_dbus_transport_try_to_authenticate (connection-\>transport))

5251 result = FALSE;

5252 else

5253 result = \_dbus_transport_get_unix_user (connection-\>transport,

5254 uid);

5255

5256\#ifdef DBUS_WIN

5257 \_dbus_assert (!result);

5258\#endif

5259

5260 CONNECTION_UNLOCK (connection);

5261

5262 return result;

5263}

5264

5275dbus_bool_t

5276dbus_connection_get_unix_process_id (DBusConnection \*connection,

5277 unsigned long \*pid)

5278{

5279 dbus_bool_t result;

5280

5281 \_dbus_return_val_if_fail (connection != NULL, FALSE);

5282 \_dbus_return_val_if_fail (pid != NULL, FALSE);

5283

5284 CONNECTION_LOCK (connection);

5285

5286 if (!\_dbus_transport_try_to_authenticate (connection-\>transport))

5287 result = FALSE;

5288 else

5289 result = \_dbus_transport_get_unix_process_id (connection-\>transport,

5290 pid);

5291

5292 CONNECTION_UNLOCK (connection);

5293

5294 return result;

5295}

5296

5308dbus_bool_t

5309dbus_connection_get_adt_audit_session_data (DBusConnection \*connection,

5310 void \*\*data,

5311 dbus_int32_t \*data_size)

5312{

5313 dbus_bool_t result;

5314

5315 \_dbus_return_val_if_fail (connection != NULL, FALSE);

5316 \_dbus_return_val_if_fail (data != NULL, FALSE);

5317 \_dbus_return_val_if_fail (data_size != NULL, FALSE);

5318

5319 CONNECTION_LOCK (connection);

5320

5321 if (!\_dbus_transport_try_to_authenticate (connection-\>transport))

5322 result = FALSE;

5323 else

5324 result = \_dbus_transport_get_adt_audit_session_data (connection-\>transport,

5325 data,

5326 data_size);

5327 CONNECTION_UNLOCK (connection);

5328

5329 return result;

5330}

5331

5354void

5355dbus_connection_set_unix_user_function (DBusConnection \*connection,

5356 DBusAllowUnixUserFunction function,

5357 void \*data,

5358 DBusFreeFunction free_data_function)

5359{

5360 void \*old_data = NULL;

5361 DBusFreeFunction old_free_function = NULL;

5362

5363 \_dbus_return_if_fail (connection != NULL);

5364

5365 CONNECTION_LOCK (connection);

5366 \_dbus_transport_set_unix_user_function (connection-\>transport,

5367 function, data, free_data_function,

5368 &old_data, &old_free_function);

5369 CONNECTION_UNLOCK (connection);

5370

5371 if (old_free_function != NULL)

5372 (\* old_free_function) (old_data);

5373}

5374

5375/\* Same calling convention as dbus_connection_get_windows_user \*/

5376dbus_bool_t

5377\_dbus_connection_get_linux_security_label (DBusConnection \*connection,

5378 char \*\*label_p)

5379{

5380 dbus_bool_t result;

5381

5382 \_dbus_assert (connection != NULL);

5383 \_dbus_assert (label_p != NULL);

5384

5385 CONNECTION_LOCK (connection);

5386

5387 if (!\_dbus_transport_try_to_authenticate (connection-\>transport))

5388 result = FALSE;

5389 else

5390 result = \_dbus_transport_get_linux_security_label (connection-\>transport,

5391 label_p);

5392\#ifndef \_\_linux\_\_

5393 \_dbus_assert (!result);

5394\#endif

5395

5396 CONNECTION_UNLOCK (connection);

5397

5398 return result;

5399}

5400

5401DBusCredentials \*

5402\_dbus_connection_get_credentials (DBusConnection \*connection)

5403{

5404 DBusCredentials \*result;

5405

5406 \_dbus_assert (connection != NULL);

5407

5408 CONNECTION_LOCK (connection);

5409

5410 if (!\_dbus_transport_try_to_authenticate (connection-\>transport))

5411 result = NULL;

5412 else

5413 result = \_dbus_transport_get_credentials (connection-\>transport);

5414

5415 CONNECTION_UNLOCK (connection);

5416

5417 return result;

5418}

5419

5451dbus_bool_t

5452dbus_connection_get_windows_user (DBusConnection \*connection,

5453 char \*\*windows_sid_p)

5454{

5455 dbus_bool_t result;

5456

5457 \_dbus_return_val_if_fail (connection != NULL, FALSE);

5458 \_dbus_return_val_if_fail (windows_sid_p != NULL, FALSE);

5459

5460 CONNECTION_LOCK (connection);

5461

5462 if (!\_dbus_transport_try_to_authenticate (connection-\>transport))

5463 result = FALSE;

5464 else

5465 result = \_dbus_transport_get_windows_user (connection-\>transport,

5466 windows_sid_p);

5467

5468\#ifdef DBUS_UNIX

5469 \_dbus_assert (!result);

5470\#endif

5471

5472 CONNECTION_UNLOCK (connection);

5473

5474 return result;

5475}

5476

5498void

5499dbus_connection_set_windows_user_function (DBusConnection \*connection,

5500 DBusAllowWindowsUserFunction function,

5501 void \*data,

5502 DBusFreeFunction free_data_function)

5503{

5504 void \*old_data = NULL;

5505 DBusFreeFunction old_free_function = NULL;

5506

5507 \_dbus_return_if_fail (connection != NULL);

5508

5509 CONNECTION_LOCK (connection);

5510 \_dbus_transport_set_windows_user_function (connection-\>transport,

5511 function, data, free_data_function,

5512 &old_data, &old_free_function);

5513 CONNECTION_UNLOCK (connection);

5514

5515 if (old_free_function != NULL)

5516 (\* old_free_function) (old_data);

5517}

5518

5545void

5546dbus_connection_set_allow_anonymous (DBusConnection \*connection,

5547 dbus_bool_t value)

5548{

5549 \_dbus_return_if_fail (connection != NULL);

5550

5551 CONNECTION_LOCK (connection);

5552 \_dbus_transport_set_allow_anonymous (connection-\>transport, value);

5553 CONNECTION_UNLOCK (connection);

5554}

5555

5577void

5578dbus_connection_set_builtin_filters_enabled (DBusConnection \*connection,

5579 dbus_bool_t value)

5580{

5581 \_dbus_return_if_fail (connection != NULL);

5582

5583 CONNECTION_LOCK (connection);

5584 connection-\>builtin_filters_enabled = value;

5585 CONNECTION_UNLOCK (connection);

5586}

5587

5605void

5606dbus_connection_set_route_peer_messages (DBusConnection \*connection,

5607 dbus_bool_t value)

5608{

5609 \_dbus_return_if_fail (connection != NULL);

5610

5611 CONNECTION_LOCK (connection);

5612 connection-\>route_peer_messages = value;

5613 CONNECTION_UNLOCK (connection);

5614}

5615

5637dbus_bool_t

5638dbus_connection_add_filter (DBusConnection \*connection,

5639 DBusHandleMessageFunction function,

5640 void \*user_data,

5641 DBusFreeFunction free_data_function)

5642{

5643 DBusMessageFilter \*filter;

5644

5645 \_dbus_return_val_if_fail (connection != NULL, FALSE);

5646 \_dbus_return_val_if_fail (function != NULL, FALSE);

5647

5648 filter = dbus_new0 (DBusMessageFilter, 1);

5649 if (filter == NULL)

5650 return FALSE;

5651

5652 \_dbus_atomic_inc (&filter-\>refcount);

5653

5654 CONNECTION_LOCK (connection);

5655

5656 if (!\_dbus_list_append (&connection-\>filter_list,

5657 filter))

5658 {

5659 \_dbus_message_filter_unref (filter);

5660 CONNECTION_UNLOCK (connection);

5661 return FALSE;

5662 }

5663

5664 /\* Fill in filter after all memory allocated,

5665 \* so we don't run the free_user_data_function

5666 \* if the add_filter() fails

5667 \*/

5668

5669 filter-\>function = function;

5670 filter-\>user_data = user_data;

5671 filter-\>free_user_data_function = free_data_function;

5672

5673 CONNECTION_UNLOCK (connection);

5674 return TRUE;

5675}

5676

5689void

5690dbus_connection_remove_filter (DBusConnection \*connection,

5691 DBusHandleMessageFunction function,

5692 void \*user_data)

5693{

5694 DBusList \*link;

5695 DBusMessageFilter \*filter;

5696

5697 \_dbus_return_if_fail (connection != NULL);

5698 \_dbus_return_if_fail (function != NULL);

5699

5700 CONNECTION_LOCK (connection);

5701

5702 filter = NULL;

5703

5704 link = \_dbus_list_get_last_link (&connection-\>filter_list);

5705 while (link != NULL)

5706 {

5707 filter = link-\>data;

5708

5709 if (filter-\>function == function &&

5710 filter-\>user_data == user_data)

5711 {

5712 \_dbus_list_remove_link (&connection-\>filter_list, link);

5713 filter-\>function = NULL;

5714

5715 break;

5716 }

5717

5718 link = \_dbus_list_get_prev_link (&connection-\>filter_list, link);

5719 filter = NULL;

5720 }

5721

5722 CONNECTION_UNLOCK (connection);

5723

5724\#ifndef DBUS_DISABLE_CHECKS

5725 if (filter == NULL)

5726 {

5727 \_dbus_warn_check_failed ("Attempt to remove filter function %p user data %p, but no such filter has been added",

5728 function, user_data);

5729 return;

5730 }

5731\#endif

5732

5733 /\* Call application code \*/

5734 if (filter-\>free_user_data_function)

5735 (\* filter-\>free_user_data_function) (filter-\>user_data);

5736

5737 filter-\>free_user_data_function = NULL;

5738 filter-\>user_data = NULL;

5739

5740 \_dbus_message_filter_unref (filter);

5741}

5742

5758static dbus_bool_t

5759\_dbus_connection_register_object_path (DBusConnection \*connection,

5760 dbus_bool_t fallback,

5761 const char \*path,

5762 const DBusObjectPathVTable \*vtable,

5763 void \*user_data,

5764 DBusError \*error)

5765{

5766 char \*\*decomposed_path;

5767 dbus_bool_t retval;

5768

5769 if (!\_dbus_decompose_path (path, strlen (path), &decomposed_path, NULL))

5770 return FALSE;

5771

5772 CONNECTION_LOCK (connection);

5773

5774 retval = \_dbus_object_tree_register (connection-\>objects,

5775 fallback,

5776 (const char \*\*) decomposed_path, vtable,

5777 user_data, error);

5778

5779 CONNECTION_UNLOCK (connection);

5780

5781 dbus_free_string_array (decomposed_path);

5782

5783 return retval;

5784}

5785

5798dbus_bool_t

5799dbus_connection_try_register_object_path (DBusConnection \*connection,

5800 const char \*path,

5801 const DBusObjectPathVTable \*vtable,

5802 void \*user_data,

5803 DBusError \*error)

5804{

5805 \_dbus_return_val_if_fail (connection != NULL, FALSE);

5806 \_dbus_return_val_if_fail (path != NULL, FALSE);

5807 \_dbus_return_val_if_fail (path\[0\] == '/', FALSE);

5808 \_dbus_return_val_if_fail (vtable != NULL, FALSE);

5809

5810 return \_dbus_connection_register_object_path (connection, FALSE, path, vtable, user_data, error);

5811}

5812

5828dbus_bool_t

5829dbus_connection_register_object_path (DBusConnection \*connection,

5830 const char \*path,

5831 const DBusObjectPathVTable \*vtable,

5832 void \*user_data)

5833{

5834 dbus_bool_t retval;

5835 DBusError error = DBUS_ERROR_INIT;

5836

5837 \_dbus_return_val_if_fail (connection != NULL, FALSE);

5838 \_dbus_return_val_if_fail (path != NULL, FALSE);

5839 \_dbus_return_val_if_fail (path\[0\] == '/', FALSE);

5840 \_dbus_return_val_if_fail (vtable != NULL, FALSE);

5841

5842 retval = \_dbus_connection_register_object_path (connection, FALSE, path, vtable, user_data, &error);

5843

5844 if (dbus_error_has_name (&error, DBUS_ERROR_OBJECT_PATH_IN_USE))

5845 {

5846 \_dbus_warn ("%s", error.message);

5847 dbus_error_free (&error);

5848 return FALSE;

5849 }

5850

5851 return retval;

5852}

5853

5868dbus_bool_t

5869dbus_connection_try_register_fallback (DBusConnection \*connection,

5870 const char \*path,

5871 const DBusObjectPathVTable \*vtable,

5872 void \*user_data,

5873 DBusError \*error)

5874{

5875 \_dbus_return_val_if_fail (connection != NULL, FALSE);

5876 \_dbus_return_val_if_fail (path != NULL, FALSE);

5877 \_dbus_return_val_if_fail (path\[0\] == '/', FALSE);

5878 \_dbus_return_val_if_fail (vtable != NULL, FALSE);

5879

5880 return \_dbus_connection_register_object_path (connection, TRUE, path, vtable, user_data, error);

5881}

5882

5900dbus_bool_t

5901dbus_connection_register_fallback (DBusConnection \*connection,

5902 const char \*path,

5903 const DBusObjectPathVTable \*vtable,

5904 void \*user_data)

5905{

5906 dbus_bool_t retval;

5907 DBusError error = DBUS_ERROR_INIT;

5908

5909 \_dbus_return_val_if_fail (connection != NULL, FALSE);

5910 \_dbus_return_val_if_fail (path != NULL, FALSE);

5911 \_dbus_return_val_if_fail (path\[0\] == '/', FALSE);

5912 \_dbus_return_val_if_fail (vtable != NULL, FALSE);

5913

5914 retval = \_dbus_connection_register_object_path (connection, TRUE, path, vtable, user_data, &error);

5915

5916 if (dbus_error_has_name (&error, DBUS_ERROR_OBJECT_PATH_IN_USE))

5917 {

5918 \_dbus_warn ("%s", error.message);

5919 dbus_error_free (&error);

5920 return FALSE;

5921 }

5922

5923 return retval;

5924}

5925

5935dbus_bool_t

5936dbus_connection_unregister_object_path (DBusConnection \*connection,

5937 const char \*path)

5938{

5939 char \*\*decomposed_path;

5940

5941 \_dbus_return_val_if_fail (connection != NULL, FALSE);

5942 \_dbus_return_val_if_fail (path != NULL, FALSE);

5943 \_dbus_return_val_if_fail (path\[0\] == '/', FALSE);

5944

5945 if (!\_dbus_decompose_path (path, strlen (path), &decomposed_path, NULL))

5946 return FALSE;

5947

5948 CONNECTION_LOCK (connection);

5949

5950 \_dbus_object_tree_unregister_and_unlock (connection-\>objects, (const char \*\*) decomposed_path);

5951

5952 dbus_free_string_array (decomposed_path);

5953

5954 return TRUE;

5955}

5956

5967dbus_bool_t

5968dbus_connection_get_object_path_data (DBusConnection \*connection,

5969 const char \*path,

5970 void \*\*data_p)

5971{

5972 char \*\*decomposed_path;

5973

5974 \_dbus_return_val_if_fail (connection != NULL, FALSE);

5975 \_dbus_return_val_if_fail (path != NULL, FALSE);

5976 \_dbus_return_val_if_fail (data_p != NULL, FALSE);

5977

5978 \*data_p = NULL;

5979

5980 if (!\_dbus_decompose_path (path, strlen (path), &decomposed_path, NULL))

5981 return FALSE;

5982

5983 CONNECTION_LOCK (connection);

5984

5985 \*data_p = \_dbus_object_tree_get_user_data_unlocked (connection-\>objects, (const char\*\*) decomposed_path);

5986

5987 CONNECTION_UNLOCK (connection);

5988

5989 dbus_free_string_array (decomposed_path);

5990

5991 return TRUE;

5992}

5993

6004dbus_bool_t

6005dbus_connection_list_registered (DBusConnection \*connection,

6006 const char \*parent_path,

6007 char \*\*\*child_entries)

6008{

6009 char \*\*decomposed_path;

6010 dbus_bool_t retval;

6011 \_dbus_return_val_if_fail (connection != NULL, FALSE);

6012 \_dbus_return_val_if_fail (parent_path != NULL, FALSE);

6013 \_dbus_return_val_if_fail (parent_path\[0\] == '/', FALSE);

6014 \_dbus_return_val_if_fail (child_entries != NULL, FALSE);

6015

6016 if (!\_dbus_decompose_path (parent_path, strlen (parent_path), &decomposed_path, NULL))

6017 return FALSE;

6018

6019 CONNECTION_LOCK (connection);

6020

6021 retval = \_dbus_object_tree_list_registered_and_unlock (connection-\>objects,

6022 (const char \*\*) decomposed_path,

6023 child_entries);

6024 dbus_free_string_array (decomposed_path);

6025

6026 return retval;

6027}

6028

6029static DBusDataSlotAllocator slot_allocator =

6030 \_DBUS_DATA_SLOT_ALLOCATOR_INIT (\_DBUS_LOCK_NAME (connection_slots));

6031

6046dbus_bool_t

6047dbus_connection_allocate_data_slot (dbus_int32_t \*slot_p)

6048{

6049 return \_dbus_data_slot_allocator_alloc (&slot_allocator,

6050 slot_p);

6051}

6052

6064void

6065dbus_connection_free_data_slot (dbus_int32_t \*slot_p)

6066{

6067 \_dbus_return_if_fail (\*slot_p \>= 0);

6068

6069 \_dbus_data_slot_allocator_free (&slot_allocator, slot_p);

6070}

6071

6094dbus_bool_t

6095dbus_connection_set_data (DBusConnection \*connection,

6096 dbus_int32_t slot,

6097 void \*data,

6098 DBusFreeFunction free_data_func)

6099{

6100 DBusFreeFunction old_free_func;

6101 void \*old_data;

6102 dbus_bool_t retval;

6103

6104 \_dbus_return_val_if_fail (connection != NULL, FALSE);

6105 \_dbus_return_val_if_fail (slot \>= 0, FALSE);

6106

6107 SLOTS_LOCK (connection);

6108

6109 retval = \_dbus_data_slot_list_set (&slot_allocator,

6110 &connection-\>slot_list,

6111 slot, data, free_data_func,

6112 &old_free_func, &old_data);

6113

6114 SLOTS_UNLOCK (connection);

6115

6116 if (retval)

6117 {

6118 /\* Do the actual free outside the connection lock \*/

6119 if (old_free_func)

6120 (\* old_free_func) (old_data);

6121 }

6122

6123 return retval;

6124}

6125

6143void\*

6144dbus_connection_get_data (DBusConnection \*connection,

6145 dbus_int32_t slot)

6146{

6147 void \*res;

6148

6149 \_dbus_return_val_if_fail (connection != NULL, NULL);

6150 \_dbus_return_val_if_fail (slot \>= 0, NULL);

6151

6152 SLOTS_LOCK (connection);

6153

6154 res = \_dbus_data_slot_list_get (&slot_allocator,

6155 &connection-\>slot_list,

6156 slot);

6157

6158 SLOTS_UNLOCK (connection);

6159

6160 return res;

6161}

6162

6169void

6170dbus_connection_set_change_sigpipe (dbus_bool_t will_modify_sigpipe)

6171{

6172 if (will_modify_sigpipe)

6173 \_dbus_atomic_set_nonzero (&\_dbus_modify_sigpipe);

6174 else

6175 \_dbus_atomic_set_zero (&\_dbus_modify_sigpipe);

6176}

6177

6186void

6187dbus_connection_set_max_message_size (DBusConnection \*connection,

6188 long size)

6189{

6190 \_dbus_return_if_fail (connection != NULL);

6191

6192 CONNECTION_LOCK (connection);

6193 \_dbus_transport_set_max_message_size (connection-\>transport,

6194 size);

6195 CONNECTION_UNLOCK (connection);

6196}

6197

6204long

6205dbus_connection_get_max_message_size (DBusConnection \*connection)

6206{

6207 long res;

6208

6209 \_dbus_return_val_if_fail (connection != NULL, 0);

6210

6211 CONNECTION_LOCK (connection);

6212 res = \_dbus_transport_get_max_message_size (connection-\>transport);

6213 CONNECTION_UNLOCK (connection);

6214 return res;

6215}

6216

6225void

6226dbus_connection_set_max_message_unix_fds (DBusConnection \*connection,

6227 long n)

6228{

6229 \_dbus_return_if_fail (connection != NULL);

6230

6231 CONNECTION_LOCK (connection);

6232 \_dbus_transport_set_max_message_unix_fds (connection-\>transport,

6233 n);

6234 CONNECTION_UNLOCK (connection);

6235}

6236

6243long

6244dbus_connection_get_max_message_unix_fds (DBusConnection \*connection)

6245{

6246 long res;

6247

6248 \_dbus_return_val_if_fail (connection != NULL, 0);

6249

6250 CONNECTION_LOCK (connection);

6251 res = \_dbus_transport_get_max_message_unix_fds (connection-\>transport);

6252 CONNECTION_UNLOCK (connection);

6253 return res;

6254}

6255

6281void

6282dbus_connection_set_max_received_size (DBusConnection \*connection,

6283 long size)

6284{

6285 \_dbus_return_if_fail (connection != NULL);

6286

6287 CONNECTION_LOCK (connection);

6288 \_dbus_transport_set_max_received_size (connection-\>transport,

6289 size);

6290 CONNECTION_UNLOCK (connection);

6291}

6292

6299long

6300dbus_connection_get_max_received_size (DBusConnection \*connection)

6301{

6302 long res;

6303

6304 \_dbus_return_val_if_fail (connection != NULL, 0);

6305

6306 CONNECTION_LOCK (connection);

6307 res = \_dbus_transport_get_max_received_size (connection-\>transport);

6308 CONNECTION_UNLOCK (connection);

6309 return res;

6310}

6311

6323void

6324dbus_connection_set_max_received_unix_fds (DBusConnection \*connection,

6325 long n)

6326{

6327 \_dbus_return_if_fail (connection != NULL);

6328

6329 CONNECTION_LOCK (connection);

6330 \_dbus_transport_set_max_received_unix_fds (connection-\>transport,

6331 n);

6332 CONNECTION_UNLOCK (connection);

6333}

6334

6341long

6342dbus_connection_get_max_received_unix_fds (DBusConnection \*connection)

6343{

6344 long res;

6345

6346 \_dbus_return_val_if_fail (connection != NULL, 0);

6347

6348 CONNECTION_LOCK (connection);

6349 res = \_dbus_transport_get_max_received_unix_fds (connection-\>transport);

6350 CONNECTION_UNLOCK (connection);

6351 return res;

6352}

6353

6364long

6365dbus_connection_get_outgoing_size (DBusConnection \*connection)

6366{

6367 long res;

6368

6369 \_dbus_return_val_if_fail (connection != NULL, 0);

6370

6371 CONNECTION_LOCK (connection);

6372 res = \_dbus_counter_get_size_value (connection-\>outgoing_counter);

6373 CONNECTION_UNLOCK (connection);

6374 return res;

6375}

6376

6377\#ifdef DBUS_ENABLE_STATS

6378void

6379\_dbus_connection_get_stats (DBusConnection \*connection,

6380 dbus_uint32_t \*in_messages,

6381 dbus_uint32_t \*in_bytes,

6382 dbus_uint32_t \*in_fds,

6383 dbus_uint32_t \*in_peak_bytes,

6384 dbus_uint32_t \*in_peak_fds,

6385 dbus_uint32_t \*out_messages,

6386 dbus_uint32_t \*out_bytes,

6387 dbus_uint32_t \*out_fds,

6388 dbus_uint32_t \*out_peak_bytes,

6389 dbus_uint32_t \*out_peak_fds)

6390{

6391 CONNECTION_LOCK (connection);

6392

6393 if (in_messages != NULL)

6394 \*in_messages = connection-\>n_incoming;

6395

6396 \_dbus_transport_get_stats (connection-\>transport,

6397 in_bytes, in_fds, in_peak_bytes, in_peak_fds);

6398

6399 if (out_messages != NULL)

6400 \*out_messages = connection-\>n_outgoing;

6401

6402 if (out_bytes != NULL)

6403 \*out_bytes = \_dbus_counter_get_size_value (connection-\>outgoing_counter);

6404

6405 if (out_fds != NULL)

6406 \*out_fds = \_dbus_counter_get_unix_fd_value (connection-\>outgoing_counter);

6407

6408 if (out_peak_bytes != NULL)

6409 \*out_peak_bytes = \_dbus_counter_get_peak_size_value (connection-\>outgoing_counter);

6410

6411 if (out_peak_fds != NULL)

6412 \*out_peak_fds = \_dbus_counter_get_peak_unix_fd_value (connection-\>outgoing_counter);

6413

6414 CONNECTION_UNLOCK (connection);

6415}

6416\#endif /\* DBUS_ENABLE_STATS \*/

6417

6425long

6426dbus_connection_get_outgoing_unix_fds (DBusConnection \*connection)

6427{

6428 long res;

6429

6430 \_dbus_return_val_if_fail (connection != NULL, 0);

6431

6432 CONNECTION_LOCK (connection);

6433 res = \_dbus_counter_get_unix_fd_value (connection-\>outgoing_counter);

6434 CONNECTION_UNLOCK (connection);

6435 return res;

6436}

6437

6438\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

6445const char\*

6446\_dbus_connection_get_address (DBusConnection \*connection)

6447{

6448 return \_dbus_transport_get_address (connection-\>transport);

6449}

6450\#endif

6451

dbus_address_entries_free

void dbus_address_entries_free(DBusAddressEntry \*\*entries)

Frees a NULL-terminated array of address entries.

**Definition** dbus-address.c:194

dbus_parse_address

dbus_bool_t dbus_parse_address(const char \*address, DBusAddressEntry \*\*\*entry_result, int \*array_len, DBusError \*error)

Parses an address string of the form:

**Definition** dbus-address.c:368

dbus_address_entry_get_value

const char \* dbus_address_entry_get_value(DBusAddressEntry \*entry, const char \*key)

Returns a value from a key of an entry.

**Definition** dbus-address.c:249

\_dbus_bus_notify_shared_connection_disconnected_unlocked

void \_dbus_bus_notify_shared_connection_disconnected_unlocked(DBusConnection \*connection)

Internal function that checks to see if this is a shared connection owned by the bus and if it is unr...

**Definition** dbus-bus.c:390

\_dbus_connection_handle_watch

dbus_bool_t \_dbus_connection_handle_watch(DBusWatch \*watch, unsigned int condition, void \*data)

A callback for use with dbus_watch_new() to create a DBusWatch.

**Definition** dbus-connection.c:1500

\_dbus_connection_toggle_timeout_unlocked

void \_dbus_connection_toggle_timeout_unlocked(DBusConnection \*connection, DBusTimeout \*timeout, dbus_bool_t enabled)

Toggles a timeout and notifies app via connection's DBusTimeoutToggledFunction if available.

**Definition** dbus-connection.c:909

dbus_connection_has_messages_to_send

dbus_bool_t dbus_connection_has_messages_to_send(DBusConnection \*connection)

Checks whether there are messages in the outgoing message queue.

**Definition** dbus-connection.c:592

\_dbus_connection_do_iteration_unlocked

void \_dbus_connection_do_iteration_unlocked(DBusConnection \*connection, DBusPendingCall \*pending, unsigned int flags, int timeout_milliseconds)

Queues incoming messages and sends outgoing messages for this connection, optionally blocking in the ...

**Definition** dbus-connection.c:1202

\_dbus_connection_send_and_unlock

dbus_bool_t \_dbus_connection_send_and_unlock(DBusConnection \*connection, DBusMessage \*message, dbus_uint32_t \*client_serial)

Like dbus_connection_send(), but assumes the connection is already locked on function entry,...

**Definition** dbus-connection.c:2112

\_dbus_connection_new_for_transport

DBusConnection \* \_dbus_connection_new_for_transport(DBusTransport \*transport)

Creates a new connection for the given transport.

**Definition** dbus-connection.c:1253

\_dbus_connection_has_messages_to_send_unlocked

dbus_bool_t \_dbus_connection_has_messages_to_send_unlocked(DBusConnection \*connection)

Checks whether there are messages in the outgoing message queue.

**Definition** dbus-connection.c:576

DBusWatchRemoveFunction

void(\* DBusWatchRemoveFunction)(DBusWatchList \*list, DBusWatch \*watch)

Function to be called in protected_change_watch() with refcount held.

**Definition** dbus-connection.c:677

\_dbus_connection_unlock

void \_dbus_connection_unlock(DBusConnection \*connection)

Releases the connection lock.

**Definition** dbus-connection.c:403

\_dbus_connection_lock

void \_dbus_connection_lock(DBusConnection \*connection)

Acquires the connection lock.

**Definition** dbus-connection.c:392

\_dbus_connection_remove_watch_unlocked

void \_dbus_connection_remove_watch_unlocked(DBusConnection \*connection, DBusWatch \*watch)

Removes a watch using the connection's DBusRemoveWatchFunction if available.

**Definition** dbus-connection.c:765

\_dbus_connection_add_timeout_unlocked

dbus_bool_t \_dbus_connection_add_timeout_unlocked(DBusConnection \*connection, DBusTimeout \*timeout)

Adds a timeout using the connection's DBusAddTimeoutFunction if available.

**Definition** dbus-connection.c:871

\_dbus_connection_toggle_watch_unlocked

void \_dbus_connection_toggle_watch_unlocked(DBusConnection \*connection, DBusWatch \*watch, dbus_bool_t enabled)

Toggles a watch and notifies app via connection's DBusWatchToggledFunction if available.

**Definition** dbus-connection.c:785

DBusTimeoutToggleFunction

void(\* DBusTimeoutToggleFunction)(DBusTimeoutList \*list, DBusTimeout \*timeout, dbus_bool_t enabled)

Function to be called in protected_change_timeout() with refcount held.

**Definition** dbus-connection.c:804

DBusTimeoutRemoveFunction

void(\* DBusTimeoutRemoveFunction)(DBusTimeoutList \*list, DBusTimeout \*timeout)

Function to be called in protected_change_timeout() with refcount held.

**Definition** dbus-connection.c:801

\_dbus_connection_add_watch_unlocked

dbus_bool_t \_dbus_connection_add_watch_unlocked(DBusConnection \*connection, DBusWatch \*watch)

Adds a watch using the connection's DBusAddWatchFunction if available.

**Definition** dbus-connection.c:747

\_dbus_connection_remove_pending_call

void \_dbus_connection_remove_pending_call(DBusConnection \*connection, DBusPendingCall \*pending)

Removes a pending call from the connection, such that the pending reply will be ignored.

**Definition** dbus-connection.c:1048

\_dbus_connection_close_if_only_one_ref

void \_dbus_connection_close_if_only_one_ref(DBusConnection \*connection)

Used internally to handle the semantics of dbus_server_set_new_connection_function().

**Definition** dbus-connection.c:2160

\_dbus_connection_unref_unlocked

void \_dbus_connection_unref_unlocked(DBusConnection \*connection)

Decrements the reference count of a DBusConnection.

**Definition** dbus-connection.c:1447

\_dbus_connection_get_message_to_send

DBusMessage \* \_dbus_connection_get_message_to_send(DBusConnection \*connection)

Gets the next outgoing message.

**Definition** dbus-connection.c:613

DBusTimeoutAddFunction

dbus_bool_t(\* DBusTimeoutAddFunction)(DBusTimeoutList \*list, DBusTimeout \*timeout)

Function to be called in protected_change_timeout() with refcount held.

**Definition** dbus-connection.c:798

\_dbus_connection_message_sent_unlocked

void \_dbus_connection_message_sent_unlocked(DBusConnection \*connection, DBusMessage \*message)

Notifies the connection that a message has been sent, so the message can be removed from the outgoing...

**Definition** dbus-connection.c:629

\_dbus_connection_remove_timeout_unlocked

void \_dbus_connection_remove_timeout_unlocked(DBusConnection \*connection, DBusTimeout \*timeout)

Removes a timeout using the connection's DBusRemoveTimeoutFunction if available.

**Definition** dbus-connection.c:889

\_dbus_connection_get_next_client_serial

dbus_uint32_t \_dbus_connection_get_next_client_serial(DBusConnection \*connection)

Allocate and return the next non-zero serial number for outgoing messages.

**Definition** dbus-connection.c:1474

DBusWatchToggleFunction

void(\* DBusWatchToggleFunction)(DBusWatchList \*list, DBusWatch \*watch, dbus_bool_t enabled)

Function to be called in protected_change_watch() with refcount held.

**Definition** dbus-connection.c:680

\_dbus_connection_queue_received_message_link

void \_dbus_connection_queue_received_message_link(DBusConnection \*connection, DBusList \*link)

Adds a message-containing list link to the incoming message queue, taking ownership of the link and t...

**Definition** dbus-connection.c:484

\_dbus_connection_get_pending_fds_count

int \_dbus_connection_get_pending_fds_count(DBusConnection \*connection)

Return how many file descriptors are pending in the loader.

**Definition** dbus-connection.c:2577

\_dbus_connection_set_pending_fds_function

void \_dbus_connection_set_pending_fds_function(DBusConnection \*connection, DBusPendingFdsChangeFunction callback, void \*data)

Register a function to be called whenever the number of pending file descriptors in the loader change...

**Definition** dbus-connection.c:2590

DBusWatchAddFunction

dbus_bool_t(\* DBusWatchAddFunction)(DBusWatchList \*list, DBusWatch \*watch)

Function to be called in protected_change_watch() with refcount held.

**Definition** dbus-connection.c:674

\_dbus_connection_block_pending_call

void \_dbus_connection_block_pending_call(DBusPendingCall \*pending)

Blocks until a pending call times out or gets a reply.

**Definition** dbus-connection.c:2394

\_dbus_connection_queue_synthesized_message_link

void \_dbus_connection_queue_synthesized_message_link(DBusConnection \*connection, DBusList \*link)

Adds a link + message to the incoming message queue.

**Definition** dbus-connection.c:549

\_dbus_connection_close_possibly_shared

void \_dbus_connection_close_possibly_shared(DBusConnection \*connection)

Closes a shared OR private connection, while dbus_connection_close() can only be used on private conn...

**Definition** dbus-connection.c:1962

\_dbus_connection_ref_unlocked

DBusConnection \* \_dbus_connection_ref_unlocked(DBusConnection \*connection)

Increments the reference count of a DBusConnection.

**Definition** dbus-connection.c:1424

dbus_connection_return_message

void dbus_connection_return_message(DBusConnection \*connection, DBusMessage \*message)

Used to return a message after peeking at it using dbus_connection_borrow_message().

**Definition** dbus-connection.c:3917

DBusWatchToggledFunction

void(\* DBusWatchToggledFunction)(DBusWatch \*watch, void \*data)

Called when dbus_watch_get_enabled() may return a different value than it did before.

**Definition** dbus-connection.h:100

dbus_connection_get_object_path_data

dbus_bool_t dbus_connection_get_object_path_data(DBusConnection \*connection, const char \*path, void \*\*data_p)

Gets the user data passed to dbus_connection_register_object_path() or dbus_connection_register_fallb...

**Definition** dbus-connection.c:5968

dbus_connection_set_max_message_size

void dbus_connection_set_max_message_size(DBusConnection \*connection, long size)

Specifies the maximum size message this connection is allowed to receive.

**Definition** dbus-connection.c:6187

dbus_connection_flush

void dbus_connection_flush(DBusConnection \*connection)

Blocks until the outgoing message queue is empty.

**Definition** dbus-connection.c:3657

dbus_connection_get_max_message_unix_fds

long dbus_connection_get_max_message_unix_fds(DBusConnection \*connection)

Gets the value set by dbus_connection_set_max_message_unix_fds().

**Definition** dbus-connection.c:6244

dbus_connection_set_exit_on_disconnect

void dbus_connection_set_exit_on_disconnect(DBusConnection \*connection, dbus_bool_t exit_on_disconnect)

Set whether \_exit() should be called when the connection receives a disconnect signal.

**Definition** dbus-connection.c:3160

dbus_connection_get_socket

dbus_bool_t dbus_connection_get_socket(DBusConnection \*connection, int \*fd)

Gets the underlying Windows or UNIX socket file descriptor of the connection, if any.

**Definition** dbus-connection.c:5193

dbus_connection_pop_message

DBusMessage \* dbus_connection_pop_message(DBusConnection \*connection)

Returns the first-received message from the incoming message queue, removing it from the queue.

**Definition** dbus-connection.c:4107

dbus_connection_get_max_received_unix_fds

long dbus_connection_get_max_received_unix_fds(DBusConnection \*connection)

Gets the value set by dbus_connection_set_max_received_unix_fds().

**Definition** dbus-connection.c:6342

dbus_connection_register_object_path

dbus_bool_t dbus_connection_register_object_path(DBusConnection \*connection, const char \*path, const DBusObjectPathVTable \*vtable, void \*user_data)

Registers a handler for a given path in the object hierarchy.

**Definition** dbus-connection.c:5829

dbus_connection_close

void dbus_connection_close(DBusConnection \*connection)

Closes a private connection, so no further data can be sent or received.

**Definition** dbus-connection.c:2947

dbus_connection_set_max_message_unix_fds

void dbus_connection_set_max_message_unix_fds(DBusConnection \*connection, long n)

Specifies the maximum number of unix fds a message on this connection is allowed to receive.

**Definition** dbus-connection.c:6226

dbus_connection_set_wakeup_main_function

void dbus_connection_set_wakeup_main_function(DBusConnection \*connection, DBusWakeupMainFunction wakeup_main_function, void \*data, DBusFreeFunction free_data_function)

Sets the mainloop wakeup function for the connection.

**Definition** dbus-connection.c:5072

dbus_connection_get_windows_user

dbus_bool_t dbus_connection_get_windows_user(DBusConnection \*connection, char \*\*windows_sid_p)

Gets the Windows user SID of the connection if known.

**Definition** dbus-connection.c:5452

dbus_connection_get_is_authenticated

dbus_bool_t dbus_connection_get_is_authenticated(DBusConnection \*connection)

Gets whether the connection was authenticated.

**Definition** dbus-connection.c:3010

dbus_connection_send_preallocated

void dbus_connection_send_preallocated(DBusConnection \*connection, DBusPreallocatedSend \*preallocated, DBusMessage \*message, dbus_uint32_t \*client_serial)

Sends a message using preallocated resources.

**Definition** dbus-connection.c:3232

dbus_connection_read_write

dbus_bool_t dbus_connection_read_write(DBusConnection \*connection, int timeout_milliseconds)

This function is intended for use with applications that don't want to write a main loop and deal wit...

**Definition** dbus-connection.c:3817

dbus_connection_get_max_received_size

long dbus_connection_get_max_received_size(DBusConnection \*connection)

Gets the value set by dbus_connection_set_max_received_size().

**Definition** dbus-connection.c:6300

dbus_connection_get_unix_fd

dbus_bool_t dbus_connection_get_unix_fd(DBusConnection \*connection, int \*fd)

Get the UNIX file descriptor of the connection, if any.

**Definition** dbus-connection.c:5163

DBusDispatchStatusFunction

void(\* DBusDispatchStatusFunction)(DBusConnection \*connection, DBusDispatchStatus new_status, void \*data)

Called when the return value of dbus_connection_get_dispatch_status() may have changed.

**Definition** dbus-connection.h:131

dbus_connection_can_send_type

dbus_bool_t dbus_connection_can_send_type(DBusConnection \*connection, int type)

Tests whether a certain type can be send via the connection.

**Definition** dbus-connection.c:3120

dbus_connection_list_registered

dbus_bool_t dbus_connection_list_registered(DBusConnection \*connection, const char \*parent_path, char \*\*\*child_entries)

Lists the registered fallback handlers and object path handlers at the given parent_path.

**Definition** dbus-connection.c:6005

dbus_connection_get_data

void \* dbus_connection_get_data(DBusConnection \*connection, dbus_int32_t slot)

Retrieves data previously set with dbus_connection_set_data().

**Definition** dbus-connection.c:6144

dbus_connection_open_private

DBusConnection \* dbus_connection_open_private(const char \*address, DBusError \*error)

Opens a new, dedicated connection to a remote address.

**Definition** dbus-connection.c:2678

dbus_connection_get_outgoing_size

long dbus_connection_get_outgoing_size(DBusConnection \*connection)

Gets the approximate size in bytes of all messages in the outgoing message queue.

**Definition** dbus-connection.c:6365

dbus_connection_set_dispatch_status_function

void dbus_connection_set_dispatch_status_function(DBusConnection \*connection, DBusDispatchStatusFunction function, void \*data, DBusFreeFunction free_data_function)

Set a function to be invoked when the dispatch status changes.

**Definition** dbus-connection.c:5118

dbus_connection_read_write_dispatch

dbus_bool_t dbus_connection_read_write_dispatch(DBusConnection \*connection, int timeout_milliseconds)

This function is intended for use with applications that don't want to write a main loop and deal wit...

**Definition** dbus-connection.c:3785

DBusHandleMessageFunction

DBusHandlerResult(\* DBusHandleMessageFunction)(DBusConnection \*connection, DBusMessage \*message, void \*user_data)

Called when a message needs to be handled.

**Definition** dbus-connection.h:172

dbus_connection_remove_filter

void dbus_connection_remove_filter(DBusConnection \*connection, DBusHandleMessageFunction function, void \*user_data)

Removes a previously-added message filter.

**Definition** dbus-connection.c:5690

dbus_connection_get_is_connected

dbus_bool_t dbus_connection_get_is_connected(DBusConnection \*connection)

Gets whether the connection is currently open.

**Definition** dbus-connection.c:2988

dbus_connection_preallocate_send

DBusPreallocatedSend \* dbus_connection_preallocate_send(DBusConnection \*connection)

Preallocates resources needed to send a message, allowing the message to be sent without the possibil...

**Definition** dbus-connection.c:3180

DBusAddWatchFunction

dbus_bool_t(\* DBusAddWatchFunction)(DBusWatch \*watch, void \*data)

Called when libdbus needs a new watch to be monitored by the main loop.

**Definition** dbus-connection.h:94

dbus_connection_unref

void dbus_connection_unref(DBusConnection \*connection)

Decrements the reference count of a DBusConnection, and finalizes it if the count reaches zero.

**Definition** dbus-connection.c:2832

dbus_connection_set_max_received_size

void dbus_connection_set_max_received_size(DBusConnection \*connection, long size)

Sets the maximum total number of bytes that can be used for all messages received on this connection.

**Definition** dbus-connection.c:6282

DBusTimeoutToggledFunction

void(\* DBusTimeoutToggledFunction)(DBusTimeout \*timeout, void \*data)

Called when dbus_timeout_get_enabled() may return a different value than it did before.

**Definition** dbus-connection.h:120

dbus_connection_dispatch

DBusDispatchStatus dbus_connection_dispatch(DBusConnection \*connection)

Processes any incoming data.

**Definition** dbus-connection.c:4591

dbus_connection_unregister_object_path

dbus_bool_t dbus_connection_unregister_object_path(DBusConnection \*connection, const char \*path)

Unregisters the handler registered with exactly the given path.

**Definition** dbus-connection.c:5936

dbus_connection_set_unix_user_function

void dbus_connection_set_unix_user_function(DBusConnection \*connection, DBusAllowUnixUserFunction function, void \*data, DBusFreeFunction free_data_function)

Sets a predicate function used to determine whether a given user ID is allowed to connect.

**Definition** dbus-connection.c:5355

dbus_connection_try_register_object_path

dbus_bool_t dbus_connection_try_register_object_path(DBusConnection \*connection, const char \*path, const DBusObjectPathVTable \*vtable, void \*user_data, DBusError \*error)

Registers a handler for a given path in the object hierarchy.

**Definition** dbus-connection.c:5799

dbus_connection_steal_borrowed_message

void dbus_connection_steal_borrowed_message(DBusConnection \*connection, DBusMessage \*message)

Used to keep a message after peeking at it using dbus_connection_borrow_message().

**Definition** dbus-connection.c:3951

dbus_connection_allocate_data_slot

dbus_bool_t dbus_connection_allocate_data_slot(dbus_int32_t \*slot_p)

Allocates an integer ID to be used for storing application-specific data on any DBusConnection.

**Definition** dbus-connection.c:6047

dbus_connection_set_change_sigpipe

void dbus_connection_set_change_sigpipe(dbus_bool_t will_modify_sigpipe)

This function sets a global flag for whether dbus_connection_new() will set SIGPIPE behavior to SIG_I...

**Definition** dbus-connection.c:6170

dbus_connection_get_max_message_size

long dbus_connection_get_max_message_size(DBusConnection \*connection)

Gets the value set by dbus_connection_set_max_message_size().

**Definition** dbus-connection.c:6205

dbus_connection_free_data_slot

void dbus_connection_free_data_slot(dbus_int32_t \*slot_p)

Deallocates a global ID for connection data slots.

**Definition** dbus-connection.c:6065

DBusAddTimeoutFunction

dbus_bool_t(\* DBusAddTimeoutFunction)(DBusTimeout \*timeout, void \*data)

Called when libdbus needs a new timeout to be monitored by the main loop.

**Definition** dbus-connection.h:113

dbus_connection_set_max_received_unix_fds

void dbus_connection_set_max_received_unix_fds(DBusConnection \*connection, long n)

Sets the maximum total number of unix fds that can be used for all messages received on this connecti...

**Definition** dbus-connection.c:6324

dbus_connection_set_data

dbus_bool_t dbus_connection_set_data(DBusConnection \*connection, dbus_int32_t slot, void \*data, DBusFreeFunction free_data_func)

Stores a pointer on a DBusConnection, along with an optional function to be used for freeing the data...

**Definition** dbus-connection.c:6095

dbus_connection_get_dispatch_status

DBusDispatchStatus dbus_connection_get_dispatch_status(DBusConnection \*connection)

Gets the current state of the incoming message queue.

**Definition** dbus-connection.c:4394

dbus_connection_send_with_reply_and_block

DBusMessage \* dbus_connection_send_with_reply_and_block(DBusConnection \*connection, DBusMessage \*message, int timeout_milliseconds, DBusError \*error)

Sends a message and blocks a certain time period while waiting for a reply.

**Definition** dbus-connection.c:3551

dbus_connection_try_register_fallback

dbus_bool_t dbus_connection_try_register_fallback(DBusConnection \*connection, const char \*path, const DBusObjectPathVTable \*vtable, void \*user_data, DBusError \*error)

Registers a fallback handler for a given subsection of the object hierarchy.

**Definition** dbus-connection.c:5869

dbus_connection_get_adt_audit_session_data

dbus_bool_t dbus_connection_get_adt_audit_session_data(DBusConnection \*connection, void \*\*data, dbus_int32_t \*data_size)

Gets the ADT audit data of the connection if any.

**Definition** dbus-connection.c:5309

dbus_connection_borrow_message

DBusMessage \* dbus_connection_borrow_message(DBusConnection \*connection)

Returns the first-received message from the incoming message queue, leaving it in the queue.

**Definition** dbus-connection.c:3866

dbus_connection_send_with_reply

dbus_bool_t dbus_connection_send_with_reply(DBusConnection \*connection, DBusMessage \*message, DBusPendingCall \*\*pending_return, int timeout_milliseconds)

Queues a message to send, as with dbus_connection_send(), but also returns a DBusPendingCall used to ...

**Definition** dbus-connection.c:3415

dbus_connection_set_windows_user_function

void dbus_connection_set_windows_user_function(DBusConnection \*connection, DBusAllowWindowsUserFunction function, void \*data, DBusFreeFunction free_data_function)

Sets a predicate function used to determine whether a given user ID is allowed to connect.

**Definition** dbus-connection.c:5499

dbus_connection_get_is_anonymous

dbus_bool_t dbus_connection_get_is_anonymous(DBusConnection \*connection)

Gets whether the connection is not authenticated as a specific user.

**Definition** dbus-connection.c:3044

dbus_connection_set_timeout_functions

dbus_bool_t dbus_connection_set_timeout_functions(DBusConnection \*connection, DBusAddTimeoutFunction add_function, DBusRemoveTimeoutFunction remove_function, DBusTimeoutToggledFunction toggled_function, void \*data, DBusFreeFunction free_data_function)

Sets the timeout functions for the connection.

**Definition** dbus-connection.c:5034

DBusRemoveWatchFunction

void(\* DBusRemoveWatchFunction)(DBusWatch \*watch, void \*data)

Called when libdbus no longer needs a watch to be monitored by the main loop.

**Definition** dbus-connection.h:106

DBusAllowUnixUserFunction

dbus_bool_t(\* DBusAllowUnixUserFunction)(DBusConnection \*connection, unsigned long uid, void \*data)

Called during authentication to check whether the given UNIX user ID is allowed to connect,...

**Definition** dbus-connection.h:146

DBusDispatchStatus

DBusDispatchStatus

Indicates the status of incoming data on a DBusConnection.

**Definition** dbus-connection.h:83

dbus_connection_register_fallback

dbus_bool_t dbus_connection_register_fallback(DBusConnection \*connection, const char \*path, const DBusObjectPathVTable \*vtable, void \*user_data)

Registers a fallback handler for a given subsection of the object hierarchy.

**Definition** dbus-connection.c:5901

dbus_connection_open

DBusConnection \* dbus_connection_open(const char \*address, DBusError \*error)

Gets a connection to a remote address.

**Definition** dbus-connection.c:2635

dbus_connection_free_preallocated_send

void dbus_connection_free_preallocated_send(DBusConnection \*connection, DBusPreallocatedSend \*preallocated)

Frees preallocated message-sending resources from dbus_connection_preallocate_send().

**Definition** dbus-connection.c:3206

dbus_connection_get_outgoing_unix_fds

long dbus_connection_get_outgoing_unix_fds(DBusConnection \*connection)

Gets the approximate number of uni fds of all messages in the outgoing message queue.

**Definition** dbus-connection.c:6426

DBusWakeupMainFunction

void(\* DBusWakeupMainFunction)(void \*data)

Called when the main loop's thread should be notified that there's now work to do.

**Definition** dbus-connection.h:138

dbus_connection_set_allow_anonymous

void dbus_connection_set_allow_anonymous(DBusConnection \*connection, dbus_bool_t value)

This function must be called on the server side of a connection when the connection is first seen in ...

**Definition** dbus-connection.c:5546

dbus_connection_add_filter

dbus_bool_t dbus_connection_add_filter(DBusConnection \*connection, DBusHandleMessageFunction function, void \*user_data, DBusFreeFunction free_data_function)

Adds a message filter.

**Definition** dbus-connection.c:5638

dbus_connection_send

dbus_bool_t dbus_connection_send(DBusConnection \*connection, DBusMessage \*message, dbus_uint32_t \*serial)

Adds a message to the outgoing message queue.

**Definition** dbus-connection.c:3317

dbus_connection_ref

DBusConnection \* dbus_connection_ref(DBusConnection \*connection)

Increments the reference count of a DBusConnection.

**Definition** dbus-connection.c:2700

dbus_connection_set_builtin_filters_enabled

void dbus_connection_set_builtin_filters_enabled(DBusConnection \*connection, dbus_bool_t value)

Enables the builtin filtering of messages.

**Definition** dbus-connection.c:5578

dbus_connection_get_server_id

char \* dbus_connection_get_server_id(DBusConnection \*connection)

Gets the ID of the server address we are authenticated to, if this connection is on the client side.

**Definition** dbus-connection.c:3089

DBusAllowWindowsUserFunction

dbus_bool_t(\* DBusAllowWindowsUserFunction)(DBusConnection \*connection, const char \*user_sid, void \*data)

Called during authentication to check whether the given Windows user ID is allowed to connect,...

**Definition** dbus-connection.h:156

dbus_connection_set_watch_functions

dbus_bool_t dbus_connection_set_watch_functions(DBusConnection \*connection, DBusAddWatchFunction add_function, DBusRemoveWatchFunction remove_function, DBusWatchToggledFunction toggled_function, void \*data, DBusFreeFunction free_data_function)

Sets the watch functions for the connection.

**Definition** dbus-connection.c:4971

DBusRemoveTimeoutFunction

void(\* DBusRemoveTimeoutFunction)(DBusTimeout \*timeout, void \*data)

Called when libdbus no longer needs a timeout to be monitored by the main loop.

**Definition** dbus-connection.h:126

dbus_connection_get_unix_process_id

dbus_bool_t dbus_connection_get_unix_process_id(DBusConnection \*connection, unsigned long \*pid)

Gets the process ID of the connection if any.

**Definition** dbus-connection.c:5276

dbus_connection_get_unix_user

dbus_bool_t dbus_connection_get_unix_user(DBusConnection \*connection, unsigned long \*uid)

Gets the UNIX user ID of the connection if known.

**Definition** dbus-connection.c:5240

dbus_connection_set_route_peer_messages

void dbus_connection_set_route_peer_messages(DBusConnection \*connection, dbus_bool_t value)

Normally DBusConnection automatically handles all messages to the org.freedesktop....

**Definition** dbus-connection.c:5606

DBUS_DISPATCH_NEED_MEMORY

@ DBUS_DISPATCH_NEED_MEMORY

More memory is needed to continue.

**Definition** dbus-connection.h:86

DBUS_DISPATCH_COMPLETE

@ DBUS_DISPATCH_COMPLETE

All currently available data has been processed.

**Definition** dbus-connection.h:85

DBUS_DISPATCH_DATA_REMAINS

@ DBUS_DISPATCH_DATA_REMAINS

There is more data to potentially convert to messages.

**Definition** dbus-connection.h:84

\_dbus_data_slot_allocator_free

void \_dbus_data_slot_allocator_free(DBusDataSlotAllocator \*allocator, dbus_int32_t \*slot_id_p)

Deallocates an ID previously allocated with \_dbus_data_slot_allocator_alloc().

**Definition** dbus-dataslot.c:157

\_dbus_data_slot_list_init

void \_dbus_data_slot_list_init(DBusDataSlotList \*list)

Initializes a slot list.

**Definition** dbus-dataslot.c:200

\_dbus_data_slot_list_free

void \_dbus_data_slot_list_free(DBusDataSlotList \*list)

Frees the data slot list and all data slots contained in it, calling application-provided free functi...

**Definition** dbus-dataslot.c:343

\_dbus_data_slot_list_get

void \* \_dbus_data_slot_list_get(DBusDataSlotAllocator \*allocator, DBusDataSlotList \*list, int slot)

Retrieves data previously set with \_dbus_data_slot_list_set_data().

**Definition** dbus-dataslot.c:288

\_dbus_data_slot_list_set

dbus_bool_t \_dbus_data_slot_list_set(DBusDataSlotAllocator \*allocator, DBusDataSlotList \*list, int slot, void \*data, DBusFreeFunction free_data_func, DBusFreeFunction \*old_free_func, void \*\*old_data)

Stores a pointer in the data slot list, along with an optional function to be used for freeing the da...

**Definition** dbus-dataslot.c:224

\_dbus_data_slot_allocator_alloc

dbus_bool_t \_dbus_data_slot_allocator_alloc(DBusDataSlotAllocator \*allocator, dbus_int32_t \*slot_id_p)

Allocates an integer ID to be used for storing data in a DBusDataSlotList.

**Definition** dbus-dataslot.c:72

DBUS_ERROR_INIT

\#define DBUS_ERROR_INIT

Expands to a suitable initializer for a DBusError on the stack.

**Definition** dbus-errors.h:64

dbus_move_error

void dbus_move_error(DBusError \*src, DBusError \*dest)

Moves an error src into dest, freeing src and overwriting dest.

**Definition** dbus-errors.c:281

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

\_dbus_hash_table_get_n_entries

int \_dbus_hash_table_get_n_entries(DBusHashTable \*table)

Gets the number of hash entries in a hash table.

**Definition** dbus-hash.c:1461

\_dbus_hash_iter_get_value

void \* \_dbus_hash_iter_get_value(DBusHashIter \*iter)

Gets the value of the current entry.

**Definition** dbus-hash.c:620

\_dbus_hash_table_insert_int

dbus_bool_t \_dbus_hash_table_insert_int(DBusHashTable \*table, int key, void \*value)

Creates a hash entry with the given key and value.

**Definition** dbus-hash.c:1312

\_dbus_hash_table_insert_string

dbus_bool_t \_dbus_hash_table_insert_string(DBusHashTable \*table, char \*key, void \*value)

Creates a hash entry with the given key and value.

**Definition** dbus-hash.c:1278

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

\_dbus_hash_table_remove_int

dbus_bool_t \_dbus_hash_table_remove_int(DBusHashTable \*table, int key)

Removes the hash entry for the given key.

**Definition** dbus-hash.c:1215

\_dbus_hash_table_remove_string

dbus_bool_t \_dbus_hash_table_remove_string(DBusHashTable \*table, const char \*key)

Removes the hash entry for the given key.

**Definition** dbus-hash.c:1187

\_dbus_hash_table_lookup_string

void \* \_dbus_hash_table_lookup_string(DBusHashTable \*table, const char \*key)

Looks up the value for a given string in a hash table of type DBUS_HASH_STRING.

**Definition** dbus-hash.c:1113

\_dbus_hash_iter_remove_entry

void \_dbus_hash_iter_remove_entry(DBusHashIter \*iter)

Removes the current entry from the hash table.

**Definition** dbus-hash.c:599

\_dbus_hash_table_lookup_int

void \* \_dbus_hash_table_lookup_int(DBusHashTable \*table, int key)

Looks up the value for a given integer in a hash table of type DBUS_HASH_INT.

**Definition** dbus-hash.c:1138

DBUS_HASH_INT

@ DBUS_HASH_INT

Hash keys are integers.

**Definition** dbus-hash.h:70

DBUS_HASH_STRING

@ DBUS_HASH_STRING

Hash keys are strings.

**Definition** dbus-hash.h:69

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

\_dbus_warn_check_failed

void \_dbus_warn_check_failed(const char \*format,...)

Prints a "critical" warning to stderr when an assertion fails; differs from \_dbus_warn primarily in t...

**Definition** dbus-internals.c:310

\_dbus_strdup

char \* \_dbus_strdup(const char \*str)

Duplicates a string.

**Definition** dbus-internals.c:621

\_dbus_get_local_machine_uuid_encoded

dbus_bool_t \_dbus_get_local_machine_uuid_encoded(DBusString \*uuid_str, DBusError \*error)

Gets the hex-encoded UUID of the machine this function is executed on.

**Definition** dbus-internals.c:983

\_dbus_warn

void \_dbus_warn(const char \*format,...)

Prints a warning message to stderr.

**Definition** dbus-internals.c:278

\_DBUS_LOCK_NAME

\#define \_DBUS_LOCK_NAME(name)

Expands to name of a global lock variable.

**Definition** dbus-internals.h:436

\_dbus_list_get_first_link

DBusList \* \_dbus_list_get_first_link(DBusList \*\*list)

Gets the first link in the list.

**Definition** dbus-list.c:597

\_dbus_list_copy

dbus_bool_t \_dbus_list_copy(DBusList \*\*list, DBusList \*\*dest)

Copies a list.

**Definition** dbus-list.c:727

\_dbus_list_pop_first_link

DBusList \* \_dbus_list_pop_first_link(DBusList \*\*list)

Removes the first link in the list and returns it.

**Definition** dbus-list.c:658

\_dbus_list_get_last

void \* \_dbus_list_get_last(DBusList \*\*list)

Gets the last data in the list.

**Definition** dbus-list.c:626

\_dbus_list_remove

dbus_bool_t \_dbus_list_remove(DBusList \*\*list, void \*data)

Removes a value from the list.

**Definition** dbus-list.c:418

\_dbus_list_append_link

void \_dbus_list_append_link(DBusList \*\*list, DBusList \*link)

Appends a link to the list.

**Definition** dbus-list.c:318

\_dbus_list_clear_full

void \_dbus_list_clear_full(DBusList \*\*list, DBusFreeFunction function)

Free every link and every element in the list.

**Definition** dbus-list.c:570

\_dbus_list_remove_link

void \_dbus_list_remove_link(DBusList \*\*list, DBusList \*link)

Removes a link from the list.

**Definition** dbus-list.c:530

\_dbus_list_get_first

void \* \_dbus_list_get_first(DBusList \*\*list)

Gets the first data in the list.

**Definition** dbus-list.c:642

\_dbus_list_get_last_link

DBusList \* \_dbus_list_get_last_link(DBusList \*\*list)

Gets the last link in the list.

**Definition** dbus-list.c:610

\_dbus_list_unlink

void \_dbus_list_unlink(DBusList \*\*list, DBusList \*link)

Removes the given link from the list, but doesn't free it.

**Definition** dbus-list.c:502

\_dbus_list_get_prev_link

\#define \_dbus_list_get_prev_link(list, link)

Gets the previous link in the list, or NULL if there are no more links.

**Definition** dbus-list.h:122

\_dbus_list_free_link

void \_dbus_list_free_link(DBusList \*link)

Frees a linked list node allocated with \_dbus_list_alloc_link.

**Definition** dbus-list.c:257

\_dbus_list_pop_first

void \* \_dbus_list_pop_first(DBusList \*\*list)

Removes the first value in the list and returns it.

**Definition** dbus-list.c:679

\_dbus_list_foreach

void \_dbus_list_foreach(DBusList \*\*list, DBusForeachFunction function, void \*data)

Calls the given function for each element in the list.

**Definition** dbus-list.c:789

\_dbus_list_clear

void \_dbus_list_clear(DBusList \*\*list)

Frees all links in the list and sets the list head to NULL.

**Definition** dbus-list.c:545

\_dbus_list_prepend_link

void \_dbus_list_prepend_link(DBusList \*\*list, DBusList \*link)

Prepends a link to the list.

**Definition** dbus-list.c:336

\_dbus_list_prepend

dbus_bool_t \_dbus_list_prepend(DBusList \*\*list, void \*data)

Prepends a value to the list.

**Definition** dbus-list.c:295

\_dbus_list_alloc_link

DBusList \* \_dbus_list_alloc_link(void \*data)

Allocates a linked list node.

**Definition** dbus-list.c:245

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

\_dbus_current_generation

int \_dbus_current_generation

\_dbus_current_generation is used to track each time that dbus_shutdown() is called,...

**Definition** dbus-memory.c:790

\_dbus_register_shutdown_func

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_register_shutdown_func(DBusShutdownFunction function, void \*data)

Register a cleanup function to be called exactly once the next time dbus_shutdown() is called.

**Definition** dbus-memory.c:819

DBusFreeFunction

void(\* DBusFreeFunction)(void \*memory)

The type of a function which frees a block of memory.

**Definition** dbus-memory.h:65

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

dbus_free_string_array

void dbus_free_string_array(char \*\*str_array)

Frees a NULL-terminated array of strings.

**Definition** dbus-memory.c:758

dbus_message_set_serial

void dbus_message_set_serial(DBusMessage \*message, dbus_uint32_t serial)

Sets the serial number of a message.

**Definition** dbus-message.c:301

dbus_message_lock

void dbus_message_lock(DBusMessage \*message)

Locks a message.

**Definition** dbus-message.c:431

dbus_message_type_to_string

const char \* dbus_message_type_to_string(int type)

Utility function to convert a D-Bus message type into a machine-readable string (not translated).

**Definition** dbus-message.c:5081

\_dbus_message_remove_counter

void \_dbus_message_remove_counter(DBusMessage \*message, DBusCounter \*counter)

Removes a counter tracking the size/unix fds of this message, and decrements the counter by the size/...

**Definition** dbus-message.c:399

\_dbus_message_add_counter_link

void \_dbus_message_add_counter_link(DBusMessage \*message, DBusList \*link)

Adds a counter to be incremented immediately with the size/unix fds of this message,...

**Definition** dbus-message.c:327

dbus_message_has_interface

dbus_bool_t dbus_message_has_interface(DBusMessage \*message, const char \*iface)

Checks if the message has an interface.

**Definition** dbus-message.c:3512

dbus_message_set_no_reply

void dbus_message_set_no_reply(DBusMessage \*message, dbus_bool_t no_reply)

Sets a flag indicating that the message does not want a reply; if this flag is set,...

**Definition** dbus-message.c:3247

dbus_message_iter_append_basic

dbus_bool_t dbus_message_iter_append_basic(DBusMessageIter \*iter, int type, const void \*value)

Appends a basic-typed value to the message.

**Definition** dbus-message.c:2771

dbus_message_get_path

const char \* dbus_message_get_path(DBusMessage \*message)

Gets the object path this message is being sent to (for DBUS_MESSAGE_TYPE_METHOD_CALL) or being emitt...

**Definition** dbus-message.c:3359

dbus_message_get_interface

const char \* dbus_message_get_interface(DBusMessage \*message)

Gets the interface this message is being sent to (for DBUS_MESSAGE_TYPE_METHOD_CALL) or being emitted...

**Definition** dbus-message.c:3490

dbus_message_new_error

DBusMessage \* dbus_message_new_error(DBusMessage \*reply_to, const char \*error_name, const char \*error_message)

Creates a new message that is an error reply to another message.

**Definition** dbus-message.c:1515

dbus_message_get_serial

dbus_uint32_t dbus_message_get_serial(DBusMessage \*message)

Returns the serial of a message or 0 if none has been specified.

**Definition** dbus-message.c:1168

dbus_message_get_type

int dbus_message_get_type(DBusMessage \*message)

Gets the type of a message.

**Definition** dbus-message.c:1767

dbus_message_append_args

dbus_bool_t dbus_message_append_args(DBusMessage \*message, int first_arg_type,...)

Appends fields to a message given a variable argument list.

**Definition** dbus-message.c:1843

dbus_message_new_signal

DBusMessage \* dbus_message_new_signal(const char \*path, const char \*iface, const char \*name)

Constructs a new message representing a signal emission.

**Definition** dbus-message.c:1469

dbus_message_ref

DBusMessage \* dbus_message_ref(DBusMessage \*message)

Increments the reference count of a DBusMessage.

**Definition** dbus-message.c:1712

dbus_message_set_error_name

dbus_bool_t dbus_message_set_error_name(DBusMessage \*message, const char \*error_name)

Sets the name of the error (DBUS_MESSAGE_TYPE_ERROR).

**Definition** dbus-message.c:3634

dbus_message_get_reply_serial

dbus_uint32_t dbus_message_get_reply_serial(DBusMessage \*message)

Returns the serial that the message is a reply to or 0 if none.

**Definition** dbus-message.c:1208

dbus_message_new_method_return

DBusMessage \* dbus_message_new_method_return(DBusMessage \*method_call)

Constructs a message that is a reply to a method call.

**Definition** dbus-message.c:1418

dbus_message_get_destination

const char \* dbus_message_get_destination(DBusMessage \*message)

Gets the destination of a message or NULL if there is none set.

**Definition** dbus-message.c:3713

dbus_message_unref

void dbus_message_unref(DBusMessage \*message)

Decrements the reference count of a DBusMessage, freeing the message if the count reaches 0.

**Definition** dbus-message.c:1735

dbus_message_new

DBusMessage \* dbus_message_new(int message_type)

Constructs a new message of the given message type.

**Definition** dbus-message.c:1334

dbus_set_error_from_message

dbus_bool_t dbus_set_error_from_message(DBusError \*error, DBusMessage \*message)

Sets a DBusError based on the contents of the given message.

**Definition** dbus-message.c:4059

dbus_message_is_method_call

dbus_bool_t dbus_message_is_method_call(DBusMessage \*message, const char \*iface, const char \*method)

Checks whether the message is a method call with the given interface and member fields.

**Definition** dbus-message.c:3865

dbus_message_set_reply_serial

dbus_bool_t dbus_message_set_reply_serial(DBusMessage \*message, dbus_uint32_t reply_serial)

Sets the reply serial of a message (the serial of the message this is a reply to).

**Definition** dbus-message.c:1184

dbus_message_is_signal

dbus_bool_t dbus_message_is_signal(DBusMessage \*message, const char \*iface, const char \*signal_name)

Checks whether the message is a signal with the given interface and member fields.

**Definition** dbus-message.c:3893

dbus_message_get_signature

const char \* dbus_message_get_signature(DBusMessage \*message)

Gets the type signature of the message, i.e.

**Definition** dbus-message.c:3806

dbus_message_get_member

const char \* dbus_message_get_member(DBusMessage \*message)

Gets the interface member being invoked (DBUS_MESSAGE_TYPE_METHOD_CALL) or emitted (DBUS_MESSAGE_TYPE...

**Definition** dbus-message.c:3576

dbus_message_iter_init_append

void dbus_message_iter_init_append(DBusMessage \*message, DBusMessageIter \*iter)

Initializes a DBusMessageIter for appending arguments to the end of a message.

**Definition** dbus-message.c:2533

\_dbus_object_tree_free_all_unlocked

void \_dbus_object_tree_free_all_unlocked(DBusObjectTree \*tree)

Free all the handlers in the tree.

**Definition** dbus-object-tree.c:723

\_dbus_object_tree_unregister_and_unlock

void \_dbus_object_tree_unregister_and_unlock(DBusObjectTree \*tree, const char \*\*path)

Unregisters an object subtree that was registered with the same path.

**Definition** dbus-object-tree.c:628

\_dbus_object_tree_unref

void \_dbus_object_tree_unref(DBusObjectTree \*tree)

Decrement the reference count.

**Definition** dbus-object-tree.c:146

\_dbus_object_tree_list_registered_and_unlock

dbus_bool_t \_dbus_object_tree_list_registered_and_unlock(DBusObjectTree \*tree, const char \*\*parent_path, char \*\*\*child_entries)

Lists the registered fallback handlers and object path handlers at the given parent_path.

**Definition** dbus-object-tree.c:1211

\_dbus_decompose_path

dbus_bool_t \_dbus_decompose_path(const char \*data, int len, char \*\*\*path, int \*path_len)

Decompose an object path.

**Definition** dbus-object-tree.c:1247

\_dbus_object_tree_register

dbus_bool_t \_dbus_object_tree_register(DBusObjectTree \*tree, dbus_bool_t fallback, const char \*\*path, const DBusObjectPathVTable \*vtable, void \*user_data, DBusError \*error)

Registers a new subtree in the global object tree.

**Definition** dbus-object-tree.c:396

\_dbus_object_tree_get_user_data_unlocked

void \* \_dbus_object_tree_get_user_data_unlocked(DBusObjectTree \*tree, const char \*\*path)

Looks up the data passed to \_dbus_object_tree_register() for a handler at the given path.

**Definition** dbus-object-tree.c:1080

\_dbus_object_tree_dispatch_and_unlock

DBusHandlerResult \_dbus_object_tree_dispatch_and_unlock(DBusObjectTree \*tree, DBusMessage \*message, dbus_bool_t \*found_object)

Tries to dispatch a message by directing it to handler for the object path listed in the message head...

**Definition** dbus-object-tree.c:908

\_dbus_object_tree_new

DBusObjectTree \* \_dbus_object_tree_new(DBusConnection \*connection)

Creates a new object tree, representing a mapping from paths to handler vtables.

**Definition** dbus-object-tree.c:95

\_dbus_pending_call_finish_completion

void \_dbus_pending_call_finish_completion(DBusPendingCall \*pending)

Call the notifier function for the pending call.

**Definition** dbus-pending-call.c:235

\_dbus_pending_call_get_connection_and_lock

DBusConnection \* \_dbus_pending_call_get_connection_and_lock(DBusPendingCall \*pending)

Gets the connection associated with this pending call.

**Definition** dbus-pending-call.c:352

\_dbus_pending_call_ref_unlocked

DBUS_PRIVATE_EXPORT DBusPendingCall \* \_dbus_pending_call_ref_unlocked(DBusPendingCall \*pending)

Increments the reference count on a pending call, while the lock on its connection is already held.

**Definition** dbus-pending-call.c:423

\_dbus_pending_call_queue_timeout_error_unlocked

void \_dbus_pending_call_queue_timeout_error_unlocked(DBusPendingCall \*pending, DBusConnection \*connection)

If the pending call hasn't been timed out, add its timeout error reply to the connection's incoming m...

**Definition** dbus-pending-call.c:257

\_dbus_pending_call_unref_and_unlock

DBUS_PRIVATE_EXPORT void \_dbus_pending_call_unref_and_unlock(DBusPendingCall \*pending)

Decrements the reference count on a pending call, freeing it if the count reaches 0.

**Definition** dbus-pending-call.c:486

\_dbus_pending_call_get_completed_unlocked

dbus_bool_t \_dbus_pending_call_get_completed_unlocked(DBusPendingCall \*pending)

Checks whether the pending call has received a reply yet, or not.

**Definition** dbus-pending-call.c:509

\_dbus_pending_call_set_reply_unlocked

void \_dbus_pending_call_set_reply_unlocked(DBusPendingCall \*pending, DBusMessage \*message)

Sets the reply of a pending call with the given message, or if the message is NULL,...

**Definition** dbus-pending-call.c:183

\_dbus_pending_call_new_unlocked

DBUS_PRIVATE_EXPORT DBusPendingCall \* \_dbus_pending_call_new_unlocked(DBusConnection \*connection, int timeout_milliseconds, DBusTimeoutHandler timeout_handler)

Creates a new pending reply object.

**Definition** dbus-pending-call.c:120

\_dbus_pending_call_set_timeout_error_unlocked

dbus_bool_t \_dbus_pending_call_set_timeout_error_unlocked(DBusPendingCall \*pending, DBusMessage \*message, dbus_uint32_t serial)

Sets the reply message associated with the pending call to a timeout error.

**Definition** dbus-pending-call.c:383

\_dbus_pending_call_start_completion_unlocked

void \_dbus_pending_call_start_completion_unlocked(DBusPendingCall \*pending)

Sets the pending call to completed.

**Definition** dbus-pending-call.c:218

\_dbus_pending_call_is_timeout_added_unlocked

dbus_bool_t \_dbus_pending_call_is_timeout_added_unlocked(DBusPendingCall \*pending)

Checks to see if a timeout has been added.

**Definition** dbus-pending-call.c:277

\_dbus_pending_call_get_reply_serial_unlocked

dbus_uint32_t \_dbus_pending_call_get_reply_serial_unlocked(DBusPendingCall \*pending)

Gets the reply's serial number.

**Definition** dbus-pending-call.c:322

\_dbus_pending_call_get_connection_unlocked

DBusConnection \* \_dbus_pending_call_get_connection_unlocked(DBusPendingCall \*pending)

Gets the connection associated with this pending call.

**Definition** dbus-pending-call.c:367

\_dbus_pending_call_get_timeout_unlocked

DBusTimeout \* \_dbus_pending_call_get_timeout_unlocked(DBusPendingCall \*pending)

Retrives the timeout.

**Definition** dbus-pending-call.c:308

\_dbus_pending_call_set_timeout_added_unlocked

void \_dbus_pending_call_set_timeout_added_unlocked(DBusPendingCall \*pending, dbus_bool_t is_added)

Sets wether the timeout has been added.

**Definition** dbus-pending-call.c:292

dbus_pending_call_ref

DBusPendingCall \* dbus_pending_call_ref(DBusPendingCall \*pending)

Increments the reference count on a pending call.

**Definition** dbus-pending-call.c:606

dbus_pending_call_steal_reply

DBusMessage \* dbus_pending_call_steal_reply(DBusPendingCall \*pending)

Gets the reply, or returns NULL if none has been received yet.

**Definition** dbus-pending-call.c:731

dbus_pending_call_block

void dbus_pending_call_block(DBusPendingCall \*pending)

Block until the pending call is completed.

**Definition** dbus-pending-call.c:766

dbus_pending_call_get_completed

dbus_bool_t dbus_pending_call_get_completed(DBusPendingCall \*pending)

Checks whether the pending call has received a reply yet, or not.

**Definition** dbus-pending-call.c:708

dbus_pending_call_unref

void dbus_pending_call_unref(DBusPendingCall \*pending)

Decrements the reference count on a pending call, freeing it if the count reaches 0.

**Definition** dbus-pending-call.c:626

DBUS_MESSAGE_TYPE_METHOD_CALL

\#define DBUS_MESSAGE_TYPE_METHOD_CALL

Message type of a method call message, see dbus_message_get_type()

**Definition** dbus-protocol.h:236

DBUS_MESSAGE_TYPE_ERROR

\#define DBUS_MESSAGE_TYPE_ERROR

Message type of an error reply message, see dbus_message_get_type()

**Definition** dbus-protocol.h:240

DBUS_ERROR_UNKNOWN_METHOD

\#define DBUS_ERROR_UNKNOWN_METHOD

Method name you invoked isn't known by the object you invoked it on.

**Definition** dbus-protocol.h:403

DBUS_TYPE_UNIX_FD

\#define DBUS_TYPE_UNIX_FD

Type code marking a unix file descriptor.

**Definition** dbus-protocol.h:116

DBUS_ERROR_OBJECT_PATH_IN_USE

\#define DBUS_ERROR_OBJECT_PATH_IN_USE

There's already an object with the requested object path.

**Definition** dbus-protocol.h:456

DBUS_MESSAGE_TYPE_SIGNAL

\#define DBUS_MESSAGE_TYPE_SIGNAL

Message type of a signal message, see dbus_message_get_type()

**Definition** dbus-protocol.h:242

DBUS_TYPE_STRING

\#define DBUS_TYPE_STRING

Type code marking a UTF-8 encoded, nul-terminated Unicode string.

**Definition** dbus-protocol.h:104

DBUS_ERROR_UNKNOWN_OBJECT

\#define DBUS_ERROR_UNKNOWN_OBJECT

Object you invoked a method on isn't known.

**Definition** dbus-protocol.h:405

DBUS_TYPE_INVALID

\#define DBUS_TYPE_INVALID

Type code that is never equal to a legitimate type code.

**Definition** dbus-protocol.h:62

DBUS_ERROR_FAILED

\#define DBUS_ERROR_FAILED

A generic error; "something went wrong" - see the error message for more.

**Definition** dbus-protocol.h:361

DBUS_ERROR_NO_MEMORY

\#define DBUS_ERROR_NO_MEMORY

There was not enough memory to complete an operation.

**Definition** dbus-protocol.h:363

DBUS_ERROR_DISCONNECTED

\#define DBUS_ERROR_DISCONNECTED

The connection is disconnected and you're trying to use it.

**Definition** dbus-protocol.h:395

\_dbus_counter_new

DBusCounter \* \_dbus_counter_new(void)

Creates a new DBusCounter.

**Definition** dbus-resources.c:91

\_dbus_counter_get_unix_fd_value

long \_dbus_counter_get_unix_fd_value(DBusCounter \*counter)

Gets the current value of the unix fd counter.

**Definition** dbus-resources.c:292

\_dbus_counter_unref

void \_dbus_counter_unref(DBusCounter \*counter)

Decrements refcount of the counter and possibly finalizes the counter.

**Definition** dbus-resources.c:138

\_dbus_counter_get_size_value

long \_dbus_counter_get_size_value(DBusCounter \*counter)

Gets the current value of the size counter.

**Definition** dbus-resources.c:276

\_dbus_counter_ref

DBusCounter \* \_dbus_counter_ref(DBusCounter \*counter)

Increments refcount of the counter.

**Definition** dbus-resources.c:118

DBusHandlerResult

DBusHandlerResult

Results that a message handler can return.

**Definition** dbus-shared.h:69

DBUS_PATH_LOCAL

\#define DBUS_PATH_LOCAL

The object path used in local/in-process-generated messages.

**Definition** dbus-shared.h:84

DBUS_INTERFACE_LOCAL

\#define DBUS_INTERFACE_LOCAL

This is a special interface whose methods can only be invoked by the local implementation (messages f...

**Definition** dbus-shared.h:107

DBUS_INTERFACE_PEER

\#define DBUS_INTERFACE_PEER

The interface supported by most dbus peers.

**Definition** dbus-shared.h:101

DBUS_HANDLER_RESULT_NEED_MEMORY

@ DBUS_HANDLER_RESULT_NEED_MEMORY

Need more memory in order to return DBUS_HANDLER_RESULT_HANDLED or DBUS_HANDLER_RESULT_NOT_YET_HANDLE...

**Definition** dbus-shared.h:72

DBUS_HANDLER_RESULT_HANDLED

@ DBUS_HANDLER_RESULT_HANDLED

Message has had its effect - no need to run more handlers.

**Definition** dbus-shared.h:70

DBUS_HANDLER_RESULT_NOT_YET_HANDLED

@ DBUS_HANDLER_RESULT_NOT_YET_HANDLED

Message has not had any effect - see if other handlers want it.

**Definition** dbus-shared.h:71

dbus_type_is_valid

dbus_bool_t dbus_type_is_valid(int typecode)

Return TRUE if the argument is a valid typecode.

**Definition** dbus-signature.c:389

\_dbus_string_init

dbus_bool_t \_dbus_string_init(DBusString \*str)

Initializes a string.

**Definition** dbus-string.c:182

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_string_append_printf

dbus_bool_t \_dbus_string_append_printf(DBusString \*str, const char \*format,...)

Appends a printf-style formatted string to the DBusString.

**Definition** dbus-string.c:1147

\_dbus_string_get_const_data

const char \* \_dbus_string_get_const_data(const DBusString \*str)

Gets the raw character buffer from a const string.

**Definition** dbus-string.c:513

\_dbus_get_monotonic_time

void \_dbus_get_monotonic_time(dbus_int64_t \*tv_sec, long \*tv_usec)

Get current time, as in gettimeofday().

**Definition** dbus-sysdeps-unix.c:3381

\_dbus_exit

void \_dbus_exit(int code)

Exit the process, returning the given value.

**Definition** dbus-sysdeps-unix.c:3641

\_dbus_atomic_set_nonzero

void \_dbus_atomic_set_nonzero(DBusAtomic \*atomic)

Atomically set the value of an integer to something nonzero.

**Definition** dbus-sysdeps-unix.c:3279

\_dbus_atomic_dec

dbus_int32_t \_dbus_atomic_dec(DBusAtomic \*atomic)

Atomically decrement an integer.

**Definition** dbus-sysdeps-unix.c:3205

\_dbus_atomic_get

dbus_int32_t \_dbus_atomic_get(DBusAtomic \*atomic)

Atomically get the value of an integer.

**Definition** dbus-sysdeps-unix.c:3233

\_dbus_disable_sigpipe

void \_dbus_disable_sigpipe(void)

signal (SIGPIPE, SIG_IGN);

**Definition** dbus-sysdeps-unix.c:3670

\_dbus_sleep_milliseconds

void \_dbus_sleep_milliseconds(int milliseconds)

Sleeps the given number of milliseconds.

**Definition** dbus-sysdeps-unix.c:3542

\_dbus_atomic_set_zero

void \_dbus_atomic_set_zero(DBusAtomic \*atomic)

Atomically set the value of an integer to 0.

**Definition** dbus-sysdeps-unix.c:3258

\_dbus_atomic_inc

dbus_int32_t \_dbus_atomic_inc(DBusAtomic \*atomic)

Atomically increments an integer.

**Definition** dbus-sysdeps-unix.c:3178

\_dbus_rmutex_new_at_location

void \_dbus_rmutex_new_at_location(DBusRMutex \*\*location_p)

Creates a new mutex or creates a no-op mutex if threads are not initialized.

**Definition** dbus-threads.c:56

\_dbus_cmutex_free_at_location

void \_dbus_cmutex_free_at_location(DBusCMutex \*\*location_p)

Frees a DBusCMutex; does nothing if passed a NULL pointer.

**Definition** dbus-threads.c:110

\_dbus_condvar_free_at_location

void \_dbus_condvar_free_at_location(DBusCondVar \*\*location_p)

Frees a condition variable; does nothing if passed a NULL pointer.

**Definition** dbus-threads.c:227

\_dbus_rmutex_unlock

DBUS_PRIVATE_EXPORT void \_dbus_rmutex_unlock(DBusRMutex \*mutex)

Unlocks a mutex.

**Definition** dbus-threads.c:153

\_dbus_condvar_wait

void \_dbus_condvar_wait(DBusCondVar \*cond, DBusCMutex \*mutex)

Atomically unlocks the mutex and waits for the conditions variable to be signalled.

**Definition** dbus-threads.c:243

\_dbus_condvar_new_at_location

void \_dbus_condvar_new_at_location(DBusCondVar \*\*location_p)

This does the same thing as \_dbus_condvar_new.

**Definition** dbus-threads.c:202

\_dbus_cmutex_new_at_location

void \_dbus_cmutex_new_at_location(DBusCMutex \*\*location_p)

Creates a new mutex or creates a no-op mutex if threads are not initialized.

**Definition** dbus-threads.c:80

\_dbus_condvar_wake_one

void \_dbus_condvar_wake_one(DBusCondVar \*cond)

If there are threads waiting on the condition variable, wake up exactly one.

**Definition** dbus-threads.c:281

\_dbus_condvar_wait_timeout

dbus_bool_t \_dbus_condvar_wait_timeout(DBusCondVar \*cond, DBusCMutex \*mutex, int timeout_milliseconds)

Atomically unlocks the mutex and waits for the conditions variable to be signalled,...

**Definition** dbus-threads.c:264

\_dbus_cmutex_lock

void \_dbus_cmutex_lock(DBusCMutex \*mutex)

Locks a mutex.

**Definition** dbus-threads.c:139

\_dbus_cmutex_unlock

void \_dbus_cmutex_unlock(DBusCMutex \*mutex)

Unlocks a mutex.

**Definition** dbus-threads.c:167

\_dbus_rmutex_free_at_location

void \_dbus_rmutex_free_at_location(DBusRMutex \*\*location_p)

Frees a DBusRMutex; does nothing if passed a NULL pointer.

**Definition** dbus-threads.c:97

DBusMutex

struct DBusMutex DBusMutex

An opaque mutex type provided by the DBusThreadFunctions implementation installed by dbus_threads_ini...

**Definition** dbus-threads.h:43

\_dbus_timeout_list_add_timeout

dbus_bool_t \_dbus_timeout_list_add_timeout(DBusTimeoutList \*timeout_list, DBusTimeout \*timeout)

Adds a new timeout to the timeout list, invoking the application DBusAddTimeoutFunction if appropriat...

**Definition** dbus-timeout.c:314

\_dbus_timeout_list_free

void \_dbus_timeout_list_free(DBusTimeoutList \*timeout_list)

Frees a DBusTimeoutList.

**Definition** dbus-timeout.c:217

\_dbus_timeout_list_toggle_timeout

void \_dbus_timeout_list_toggle_timeout(DBusTimeoutList \*timeout_list, DBusTimeout \*timeout, dbus_bool_t enabled)

Sets a timeout to the given enabled state, invoking the application's DBusTimeoutToggledFunction if a...

**Definition** dbus-timeout.c:366

\_dbus_timeout_list_new

DBusTimeoutList \* \_dbus_timeout_list_new(void)

Creates a new timeout list.

**Definition** dbus-timeout.c:200

\_dbus_timeout_list_set_functions

dbus_bool_t \_dbus_timeout_list_set_functions(DBusTimeoutList \*timeout_list, DBusAddTimeoutFunction add_function, DBusRemoveTimeoutFunction remove_function, DBusTimeoutToggledFunction toggled_function, void \*data, DBusFreeFunction free_data_function)

Sets the timeout functions.

**Definition** dbus-timeout.c:243

\_dbus_timeout_list_remove_timeout

void \_dbus_timeout_list_remove_timeout(DBusTimeoutList \*timeout_list, DBusTimeout \*timeout)

Removes a timeout from the timeout list, invoking the application's DBusRemoveTimeoutFunction if appr...

**Definition** dbus-timeout.c:344

dbus_timeout_get_interval

DBUS_EXPORT int dbus_timeout_get_interval(DBusTimeout \*timeout)

Gets the timeout interval.

**Definition** dbus-timeout.c:444

\_dbus_transport_set_max_message_size

void \_dbus_transport_set_max_message_size(DBusTransport \*transport, long size)

See dbus_connection_set_max_message_size().

**Definition** dbus-transport.c:1225

\_dbus_transport_set_max_received_size

void \_dbus_transport_set_max_received_size(DBusTransport \*transport, long size)

See dbus_connection_set_max_received_size().

**Definition** dbus-transport.c:1275

\_dbus_transport_get_dispatch_status

DBusDispatchStatus \_dbus_transport_get_dispatch_status(DBusTransport \*transport)

Reports our current dispatch status (whether there's buffered data to be queued as messages,...

**Definition** dbus-transport.c:1127

\_dbus_transport_get_pending_fds_count

int \_dbus_transport_get_pending_fds_count(DBusTransport \*transport)

Return how many file descriptors are pending in the loader.

**Definition** dbus-transport.c:1590

\_dbus_transport_get_adt_audit_session_data

dbus_bool_t \_dbus_transport_get_adt_audit_session_data(DBusTransport \*transport, void \*\*data, int \*data_size)

See dbus_connection_get_adt_audit_session_data().

**Definition** dbus-transport.c:1403

\_dbus_transport_get_windows_user

dbus_bool_t \_dbus_transport_get_windows_user(DBusTransport \*transport, char \*\*windows_sid_p)

See dbus_connection_get_windows_user().

**Definition** dbus-transport.c:1505

\_dbus_transport_queue_messages

dbus_bool_t \_dbus_transport_queue_messages(DBusTransport \*transport)

Processes data we've read while handling a watch, potentially converting some of it to messages and q...

**Definition** dbus-transport.c:1166

\_dbus_transport_get_socket_fd

dbus_bool_t \_dbus_transport_get_socket_fd(DBusTransport \*transport, DBusSocket \*fd_p)

Get the socket file descriptor, if any.

**Definition** dbus-transport.c:969

\_dbus_transport_get_address

const char \* \_dbus_transport_get_address(DBusTransport \*transport)

Gets the address of a transport.

**Definition** dbus-transport.c:874

\_dbus_transport_handle_watch

dbus_bool_t \_dbus_transport_handle_watch(DBusTransport \*transport, DBusWatch \*watch, unsigned int condition)

Handles a watch by reading data, writing data, or disconnecting the transport, as appropriate for the...

**Definition** dbus-transport.c:907

\_dbus_transport_ref

DBusTransport \* \_dbus_transport_ref(DBusTransport \*transport)

Increments the reference count for the transport.

**Definition** dbus-transport.c:469

\_dbus_transport_peek_is_authenticated

dbus_bool_t \_dbus_transport_peek_is_authenticated(DBusTransport \*transport)

Returns TRUE if we have been authenticated.

**Definition** dbus-transport.c:710

\_dbus_transport_set_allow_anonymous

void \_dbus_transport_set_allow_anonymous(DBusTransport \*transport, dbus_bool_t value)

See dbus_connection_set_allow_anonymous()

**Definition** dbus-transport.c:1578

\_dbus_transport_disconnect

void \_dbus_transport_disconnect(DBusTransport \*transport)

Closes our end of the connection to a remote application.

**Definition** dbus-transport.c:511

\_dbus_transport_get_max_received_size

long \_dbus_transport_get_max_received_size(DBusTransport \*transport)

See dbus_connection_get_max_received_size().

**Definition** dbus-transport.c:1311

\_dbus_transport_get_credentials

DBusCredentials \* \_dbus_transport_get_credentials(DBusTransport \*transport)

If the transport has already been authenticated, return its credentials.

**Definition** dbus-transport.c:1489

\_dbus_transport_set_connection

dbus_bool_t \_dbus_transport_set_connection(DBusTransport \*transport, DBusConnection \*connection)

Sets the connection using this transport.

**Definition** dbus-transport.c:945

\_dbus_transport_set_unix_user_function

void \_dbus_transport_set_unix_user_function(DBusTransport \*transport, DBusAllowUnixUserFunction function, void \*data, DBusFreeFunction free_data_function, void \*\*old_data, DBusFreeFunction \*old_free_data_function)

See dbus_connection_set_unix_user_function().

**Definition** dbus-transport.c:1439

\_dbus_transport_get_max_message_unix_fds

long \_dbus_transport_get_max_message_unix_fds(DBusTransport \*transport)

See dbus_connection_get_max_message_unix_fds().

**Definition** dbus-transport.c:1263

\_dbus_transport_set_max_received_unix_fds

void \_dbus_transport_set_max_received_unix_fds(DBusTransport \*transport, long n)

See dbus_connection_set_max_received_unix_fds().

**Definition** dbus-transport.c:1293

\_dbus_transport_unref

void \_dbus_transport_unref(DBusTransport \*transport)

Decrements the reference count for the transport.

**Definition** dbus-transport.c:486

\_dbus_transport_can_pass_unix_fd

dbus_bool_t \_dbus_transport_can_pass_unix_fd(DBusTransport \*transport)

Returns TRUE if the transport supports sending unix fds.

**Definition** dbus-transport.c:861

\_dbus_transport_try_to_authenticate

dbus_bool_t \_dbus_transport_try_to_authenticate(DBusTransport \*transport)

Returns TRUE if we have been authenticated.

**Definition** dbus-transport.c:733

\_dbus_transport_do_iteration

void \_dbus_transport_do_iteration(DBusTransport \*transport, unsigned int flags, int timeout_milliseconds)

Performs a single poll()/select() on the transport's file descriptors and then reads/writes data as a...

**Definition** dbus-transport.c:1002

\_dbus_transport_get_max_received_unix_fds

long \_dbus_transport_get_max_received_unix_fds(DBusTransport \*transport)

See dbus_connection_set_max_received_unix_fds().

**Definition** dbus-transport.c:1323

\_dbus_transport_get_is_connected

dbus_bool_t \_dbus_transport_get_is_connected(DBusTransport \*transport)

Returns TRUE if the transport has not been disconnected.

**Definition** dbus-transport.c:536

\_dbus_transport_set_max_message_unix_fds

void \_dbus_transport_set_max_message_unix_fds(DBusTransport \*transport, long n)

See dbus_connection_set_max_message_unix_fds().

**Definition** dbus-transport.c:1238

\_dbus_transport_set_pending_fds_function

void \_dbus_transport_set_pending_fds_function(DBusTransport \*transport, void(\*callback)(void \*), void \*data)

Register a function to be called whenever the number of pending file descriptors in the loader change...

**Definition** dbus-transport.c:1603

\_dbus_transport_set_windows_user_function

void \_dbus_transport_set_windows_user_function(DBusTransport \*transport, DBusAllowWindowsUserFunction function, void \*data, DBusFreeFunction free_data_function, void \*\*old_data, DBusFreeFunction \*old_free_data_function)

See dbus_connection_set_windows_user_function().

**Definition** dbus-transport.c:1541

\_dbus_transport_get_max_message_size

long \_dbus_transport_get_max_message_size(DBusTransport \*transport)

See dbus_connection_get_max_message_size().

**Definition** dbus-transport.c:1251

\_dbus_transport_get_unix_process_id

dbus_bool_t \_dbus_transport_get_unix_process_id(DBusTransport \*transport, unsigned long \*pid)

See dbus_connection_get_unix_process_id().

**Definition** dbus-transport.c:1369

\_dbus_transport_open

DBusTransport \* \_dbus_transport_open(DBusAddressEntry \*entry, DBusError \*error)

Try to open a new transport for the given address entry.

**Definition** dbus-transport.c:373

\_dbus_transport_get_server_id

const char \* \_dbus_transport_get_server_id(DBusTransport \*transport)

Gets the id of the server we are connected to (see dbus_server_get_id()).

**Definition** dbus-transport.c:887

\_dbus_transport_get_is_anonymous

dbus_bool_t \_dbus_transport_get_is_anonymous(DBusTransport \*transport)

See dbus_connection_get_is_anonymous().

**Definition** dbus-transport.c:839

\_dbus_transport_get_unix_user

dbus_bool_t \_dbus_transport_get_unix_user(DBusTransport \*transport, unsigned long \*uid)

See dbus_connection_get_unix_user().

**Definition** dbus-transport.c:1336

DBUS_INT64_MODIFIER

\#define DBUS_INT64_MODIFIER

A string literal for a length modifier that is appropriate to print the dbus_int64_t and dbus_uint64\_...

**Definition** dbus-arch-deps.h:39

\_dbus_watch_list_add_watch

dbus_bool_t \_dbus_watch_list_add_watch(DBusWatchList \*watch_list, DBusWatch \*watch)

Adds a new watch to the watch list, invoking the application DBusAddWatchFunction if appropriate.

**Definition** dbus-watch.c:383

\_dbus_watch_list_toggle_watch

void \_dbus_watch_list_toggle_watch(DBusWatchList \*watch_list, DBusWatch \*watch, dbus_bool_t enabled)

Sets a watch to the given enabled state, invoking the application's DBusWatchToggledFunction if appro...

**Definition** dbus-watch.c:443

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

\_dbus_watch_list_remove_watch

void \_dbus_watch_list_remove_watch(DBusWatchList \*watch_list, DBusWatch \*watch)

Removes a watch from the watch list, invoking the application's DBusRemoveWatchFunction if appropriat...

**Definition** dbus-watch.c:416

DBusAddressEntry

Internals of DBusAddressEntry.

**Definition** dbus-address.c:49

DBusAtomic

An atomic integer safe to increment or decrement from multiple threads.

**Definition** dbus-sysdeps.h:340

DBusCMutex

**Definition** dbus-sysdeps-pthread.c:55

DBusCondVar

**Definition** dbus-sysdeps-pthread.c:59

DBusConnection

Implementation details of DBusConnection.

**Definition** dbus-connection.c:259

DBusConnection::dispatch_status_data

void \* dispatch_status_data

Application data for dispatch_status_function.

**Definition** dbus-connection.c:301

DBusConnection::n_outgoing

int n_outgoing

Length of outgoing queue.

**Definition** dbus-connection.c:277

DBusConnection::slot_list

DBusDataSlotList slot_list

Data stored by allocated integer ID.

**Definition** dbus-connection.c:289

DBusConnection::dispatch_acquired

dbus_bool_t dispatch_acquired

Someone has dispatch path (can drain incoming queue)

**Definition** dbus-connection.c:314

DBusConnection::dispatch_cond

DBusCondVar \* dispatch_cond

Notify when dispatch_acquired is available.

**Definition** dbus-connection.c:265

DBusConnection::wakeup_main_function

DBusWakeupMainFunction wakeup_main_function

Function to wake up the mainloop

**Definition** dbus-connection.c:296

DBusConnection::exit_on_disconnect

unsigned int exit_on_disconnect

If TRUE, exit after handling disconnect signal.

**Definition** dbus-connection.c:319

DBusConnection::filter_list

DBusList \* filter_list

List of filters.

**Definition** dbus-connection.c:286

DBusConnection::have_connection_lock

unsigned int have_connection_lock

Used to check locking.

**Definition** dbus-connection.c:334

DBusConnection::disconnected_message_processed

unsigned int disconnected_message_processed

We did our default handling of the disconnected message, such as closing the connection.

**Definition** dbus-connection.c:329

DBusConnection::client_serial

dbus_uint32_t client_serial

Client serial.

**Definition** dbus-connection.c:293

DBusConnection::disconnected_message_arrived

unsigned int disconnected_message_arrived

We popped or are dispatching the disconnected message.

**Definition** dbus-connection.c:325

DBusConnection::outgoing_counter

DBusCounter \* outgoing_counter

Counts size of outgoing messages.

**Definition** dbus-connection.c:280

DBusConnection::builtin_filters_enabled

unsigned int builtin_filters_enabled

If TRUE, handle org.freedesktop.DBus.Peer messages automatically, whether they have a bus name or not...

**Definition** dbus-connection.c:321

DBusConnection::io_path_cond

DBusCondVar \* io_path_cond

Notify when io_path_acquired is available.

**Definition** dbus-connection.c:267

DBusConnection::refcount

DBusAtomic refcount

Reference count.

**Definition** dbus-connection.c:260

DBusConnection::outgoing_messages

DBusList \* outgoing_messages

Queue of messages we need to send, send the end of the list first.

**Definition** dbus-connection.c:269

DBusConnection::free_dispatch_status_data

DBusFreeFunction free_dispatch_status_data

free dispatch_status_data

**Definition** dbus-connection.c:302

DBusConnection::slot_mutex

DBusRMutex \* slot_mutex

Lock on slot_list so overall connection lock need not be taken.

**Definition** dbus-connection.c:288

DBusConnection::free_wakeup_main_data

DBusFreeFunction free_wakeup_main_data

free wakeup_main_data

**Definition** dbus-connection.c:298

DBusConnection::transport

DBusTransport \* transport

Object that sends/receives messages over network.

**Definition** dbus-connection.c:282

DBusConnection::mutex

DBusRMutex \* mutex

Lock on the entire DBusConnection.

**Definition** dbus-connection.c:262

DBusConnection::n_incoming

int n_incoming

Length of incoming queue.

**Definition** dbus-connection.c:278

DBusConnection::io_path_acquired

dbus_bool_t io_path_acquired

Someone has transport io path (can use the transport to read/write messages)

**Definition** dbus-connection.c:315

DBusConnection::disconnect_message_link

DBusList \* disconnect_message_link

Preallocated list node for queueing the disconnection message.

**Definition** dbus-connection.c:294

DBusConnection::io_path_mutex

DBusCMutex \* io_path_mutex

Protects io_path_acquired.

**Definition** dbus-connection.c:266

DBusConnection::incoming_messages

DBusList \* incoming_messages

Queue of messages we have received, end of the list received most recently.

**Definition** dbus-connection.c:270

DBusConnection::shareable

unsigned int shareable

TRUE if libdbus owns a reference to the connection and can return it from dbus_connection_open() more...

**Definition** dbus-connection.c:317

DBusConnection::route_peer_messages

unsigned int route_peer_messages

If TRUE, if org.freedesktop.DBus.Peer messages have a bus name, don't handle them automatically.

**Definition** dbus-connection.c:323

DBusConnection::watches

DBusWatchList \* watches

Stores active watches.

**Definition** dbus-connection.c:283

DBusConnection::wakeup_main_data

void \* wakeup_main_data

Application data for wakeup_main_function.

**Definition** dbus-connection.c:297

DBusConnection::objects

DBusObjectTree \* objects

Object path handlers registered with this connection.

**Definition** dbus-connection.c:306

DBusConnection::server_guid

char \* server_guid

GUID of server if we are in shared_connections, NULL if server GUID is unknown or connection is priva...

**Definition** dbus-connection.c:308

DBusConnection::pending_replies

DBusHashTable \* pending_replies

Hash of message serials to DBusPendingCall.

**Definition** dbus-connection.c:291

DBusConnection::dispatch_mutex

DBusCMutex \* dispatch_mutex

Protects dispatch_acquired.

**Definition** dbus-connection.c:264

DBusConnection::message_borrowed

DBusMessage \* message_borrowed

Filled in if the first incoming message has been borrowed; dispatch_acquired will be set by the borro...

**Definition** dbus-connection.c:273

DBusConnection::timeouts

DBusTimeoutList \* timeouts

Stores active timeouts.

**Definition** dbus-connection.c:284

DBusConnection::last_dispatch_status

DBusDispatchStatus last_dispatch_status

The last dispatch status we reported to the application.

**Definition** dbus-connection.c:304

DBusConnection::dispatch_status_function

DBusDispatchStatusFunction dispatch_status_function

Function on dispatch status changes

**Definition** dbus-connection.c:300

DBusConnection::expired_messages

DBusList \* expired_messages

Messages that will be released when we next unlock.

**Definition** dbus-connection.c:271

DBusCounter

Internals of DBusCounter.

**Definition** dbus-resources.c:57

DBusCredentials

**Definition** dbus-credentials.c:60

DBusDataSlotAllocator

An allocator that tracks a set of slot IDs.

**Definition** dbus-dataslot.h:58

DBusDataSlotList

Data structure that stores the actual user data set at a given slot.

**Definition** dbus-dataslot.h:72

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

DBusMessageFilter

Internal struct representing a message filter function.

**Definition** dbus-connection.c:231

DBusMessageFilter::refcount

DBusAtomic refcount

Reference count.

**Definition** dbus-connection.c:232

DBusMessageFilter::function

DBusHandleMessageFunction function

Function to call to filter.

**Definition** dbus-connection.c:233

DBusMessageFilter::user_data

void \* user_data

User data for the function.

**Definition** dbus-connection.c:234

DBusMessageFilter::free_user_data_function

DBusFreeFunction free_user_data_function

Function to free the user data.

**Definition** dbus-connection.c:235

DBusMessageIter

DBusMessageIter struct; contains no public fields.

**Definition** dbus-message.h:64

DBusMessage

Internals of DBusMessage.

**Definition** dbus-message-private.h:102

DBusObjectPathVTable

Virtual table that must be implemented to handle a portion of the object path hierarchy.

**Definition** dbus-connection.h:391

DBusObjectTree

Internals of DBusObjectTree.

**Definition** dbus-object-tree.c:61

DBusPendingCall

Implementation details of DBusPendingCall - all fields are private.

**Definition** dbus-pending-call.c:65

DBusPreallocatedSend

Internals of DBusPreallocatedSend.

**Definition** dbus-connection.c:243

DBusPreallocatedSend::connection

DBusConnection \* connection

Connection we'd send the message to.

**Definition** dbus-connection.c:244

DBusPreallocatedSend::counter_link

DBusList \* counter_link

Preallocated link in the resource counter.

**Definition** dbus-connection.c:246

DBusPreallocatedSend::queue_link

DBusList \* queue_link

Preallocated link in the queue.

**Definition** dbus-connection.c:245

DBusRMutex

**Definition** dbus-sysdeps-pthread.c:51

DBusSocket

Socket interface.

**Definition** dbus-sysdeps.h:185

DBusString

**Definition** dbus-string.h:47

DBusTimeoutList

DBusTimeoutList implementation details.

**Definition** dbus-timeout.c:183

DBusTimeout

Internals of DBusTimeout.

**Definition** dbus-timeout.c:43

DBusTransport

Object representing a transport such as a socket.

**Definition** dbus-transport-protected.h:83

DBusWatchList

DBusWatchList implementation details.

**Definition** dbus-watch.c:217

DBusWatch

Implementation of DBusWatch.

**Definition** dbus-watch.c:43
