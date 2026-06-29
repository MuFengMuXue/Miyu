dbus-pending-call.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-pending-call.c Object representing a call in progress.

3 \*

4 \* Copyright (C) 2002, 2003 Red Hat Inc.

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

27\#include "dbus-internals.h"

28\#include "dbus-connection-internal.h"

29\#include "dbus-message-internal.h"

30\#include "dbus-pending-call-internal.h"

31\#include "dbus-pending-call.h"

32\#include "dbus-list.h"

33\#include "dbus-threads.h"

34\#include "dbus-test.h"

35

55\#define CONNECTION_LOCK(connection) \_dbus_connection_lock(connection)

59\#define CONNECTION_UNLOCK(connection) \_dbus_connection_unlock(connection)

60

64struct DBusPendingCall

65{

66 DBusAtomic refcount;

68 DBusDataSlotList slot_list;

70 DBusPendingCallNotifyFunction function;

72 DBusConnection \*connection;

73 DBusMessage \*reply;

74 DBusTimeout \*timeout;

76 DBusList \*timeout_link;

78 dbus_uint32_t reply_serial;

85 unsigned int completed : 1;

89 unsigned int timeout_added : 1;

90};

91

92static void

93\_dbus_pending_call_trace_ref (DBusPendingCall \*pending_call,

94 int old_refcount,

95 int new_refcount,

96 const char \*why)

97{

98\#ifdef DBUS_ENABLE_VERBOSE_MODE

99 static int enabled = -1;

100

101 \_dbus_trace_ref ("DBusPendingCall", pending_call, old_refcount,

102 new_refcount, why, "DBUS_PENDING_CALL_TRACE", &enabled);

103\#endif

104}

105

106/\* protected by \_DBUS_LOCK_pending_call_slots \*/

107static dbus_int32_t notify_user_data_slot = -1;

108

119DBusPendingCall\*

120\_dbus_pending_call_new_unlocked (DBusConnection \*connection,

121 int timeout_milliseconds,

122 DBusTimeoutHandler timeout_handler)

123{

124 DBusPendingCall \*pending;

125 DBusTimeout \*timeout;

126

127 \_dbus_assert (timeout_milliseconds \>= 0 \|\| timeout_milliseconds == -1);

128

129 if (timeout_milliseconds == -1)

130 timeout_milliseconds = \_DBUS_DEFAULT_TIMEOUT_VALUE;

131

132 if (!dbus_pending_call_allocate_data_slot (&notify_user_data_slot))

133 return NULL;

134

135 pending = dbus_new0 (DBusPendingCall, 1);

136

137 if (pending == NULL)

138 {

139 dbus_pending_call_free_data_slot (&notify_user_data_slot);

140 return NULL;

141 }

142

143 if (timeout_milliseconds != DBUS_TIMEOUT_INFINITE)

144 {

145 timeout = \_dbus_timeout_new (timeout_milliseconds,

146 timeout_handler,

147 pending, NULL);

148

149 if (timeout == NULL)

150 {

151 dbus_pending_call_free_data_slot (&notify_user_data_slot);

152 dbus_free (pending);

153 return NULL;

154 }

155

156 pending-\>timeout = timeout;

157 }

158 else

159 {

160 pending-\>timeout = NULL;

161 }

162

163 \_dbus_atomic_inc (&pending-\>refcount);

164 pending-\>connection = connection;

165 \_dbus_connection_ref_unlocked (pending-\>connection);

166

167 \_dbus_data_slot_list_init (&pending-\>slot_list);

168

169 \_dbus_pending_call_trace_ref (pending, 0, 1, "new_unlocked");

170

171 return pending;

172}

173

182void

183\_dbus_pending_call_set_reply_unlocked (DBusPendingCall \*pending,

184 DBusMessage \*message)

185{

186 if (message == NULL)

187 {

188 message = pending-\>timeout_link-\>data;

189 \_dbus_list_clear (&pending-\>timeout_link);

190 }

191 else

192 dbus_message_ref (message);

193

194 \_dbus_verbose (" handing message %p (%s) to pending call serial %u\n",

195 message,

196 dbus_message_get_type (message) == DBUS_MESSAGE_TYPE_METHOD_RETURN ?

197 "method return" :

198 dbus_message_get_type (message) == DBUS_MESSAGE_TYPE_ERROR ?

199 "error" : "other type",

200 pending-\>reply_serial);

201

202 \_dbus_assert (pending-\>reply == NULL);

203 \_dbus_assert (pending-\>reply_serial == dbus_message_get_reply_serial (message));

204 pending-\>reply = message;

205}

206

217void

218\_dbus_pending_call_start_completion_unlocked (DBusPendingCall \*pending)

219{

220 \_dbus_assert (!pending-\>completed);

221

222 pending-\>completed = TRUE;

223}

224

234void

235\_dbus_pending_call_finish_completion (DBusPendingCall \*pending)

236{

237 \_dbus_assert (pending-\>completed);

238

239 if (pending-\>function)

240 {

241 void \*user_data;

242 user_data = dbus_pending_call_get_data (pending,

243 notify_user_data_slot);

244

245 (\* pending-\>function) (pending, user_data);

246 }

247}

248

256void

257\_dbus_pending_call_queue_timeout_error_unlocked (DBusPendingCall \*pending,

258 DBusConnection \*connection)

259{

260 \_dbus_assert (connection == pending-\>connection);

261

262 if (pending-\>timeout_link)

263 {

264 \_dbus_connection_queue_synthesized_message_link (connection,

265 pending-\>timeout_link);

266 pending-\>timeout_link = NULL;

267 }

268}

269

276dbus_bool_t

277\_dbus_pending_call_is_timeout_added_unlocked (DBusPendingCall \*pending)

278{

279 \_dbus_assert (pending != NULL);

280

281 return pending-\>timeout_added;

282}

283

284

291void

292\_dbus_pending_call_set_timeout_added_unlocked (DBusPendingCall \*pending,

293 dbus_bool_t is_added)

294{

295 \_dbus_assert (pending != NULL);

296

297 pending-\>timeout_added = is_added;

298}

299

300

307DBusTimeout \*

308\_dbus_pending_call_get_timeout_unlocked (DBusPendingCall \*pending)

309{

310 \_dbus_assert (pending != NULL);

311

312 return pending-\>timeout;

313}

314

321dbus_uint32_t

322\_dbus_pending_call_get_reply_serial_unlocked (DBusPendingCall \*pending)

323{

324 \_dbus_assert (pending != NULL);

325

326 return pending-\>reply_serial;

327}

328

335void

336\_dbus_pending_call_set_reply_serial_unlocked (DBusPendingCall \*pending,

337 dbus_uint32_t serial)

338{

339 \_dbus_assert (pending != NULL);

340 \_dbus_assert (pending-\>reply_serial == 0);

341

342 pending-\>reply_serial = serial;

343}

344

351DBusConnection \*

352\_dbus_pending_call_get_connection_and_lock (DBusPendingCall \*pending)

353{

354 \_dbus_assert (pending != NULL);

355

356 CONNECTION_LOCK (pending-\>connection);

357 return pending-\>connection;

358}

359

366DBusConnection \*

367\_dbus_pending_call_get_connection_unlocked (DBusPendingCall \*pending)

368{

369 \_dbus_assert (pending != NULL);

370

371 return pending-\>connection;

372}

373

382dbus_bool_t

383\_dbus_pending_call_set_timeout_error_unlocked (DBusPendingCall \*pending,

384 DBusMessage \*message,

385 dbus_uint32_t serial)

386{

387 DBusList \*reply_link;

388 DBusMessage \*reply;

389

390 reply = dbus_message_new_error (message, DBUS_ERROR_NO_REPLY,

391 "Did not receive a reply. Possible causes include: "

392 "the remote application did not send a reply, "

393 "the message bus security policy blocked the reply, "

394 "the reply timeout expired, or "

395 "the network connection was broken.");

396 if (reply == NULL)

397 return FALSE;

398

399 reply_link = \_dbus_list_alloc_link (reply);

400 if (reply_link == NULL)

401 {

402 /\* it's OK to unref this, nothing that could have attached a callback

403 \* has ever seen it \*/

404 dbus_message_unref (reply);

405 return FALSE;

406 }

407

408 pending-\>timeout_link = reply_link;

409

410 \_dbus_pending_call_set_reply_serial_unlocked (pending, serial);

411

412 return TRUE;

413}

414

422DBusPendingCall \*

423\_dbus_pending_call_ref_unlocked (DBusPendingCall \*pending)

424{

425 dbus_int32_t old_refcount;

426

427 old_refcount = \_dbus_atomic_inc (&pending-\>refcount);

428 \_dbus_pending_call_trace_ref (pending, old_refcount, old_refcount + 1,

429 "ref_unlocked");

430

431 return pending;

432}

433

434

435static void

436\_dbus_pending_call_last_unref (DBusPendingCall \*pending)

437{

438 DBusConnection \*connection;

439

440 /\* If we get here, we should be already detached

441 \* from the connection, or never attached.

442 \*/

443 \_dbus_assert (!pending-\>timeout_added);

444

445 connection = pending-\>connection;

446

447 /\* this assumes we aren't holding connection lock... \*/

448 \_dbus_data_slot_list_free (&pending-\>slot_list);

449

450 if (pending-\>timeout != NULL)

451 \_dbus_timeout_unref (pending-\>timeout);

452

453 if (pending-\>timeout_link)

454 {

455 dbus_message_unref ((DBusMessage \*)pending-\>timeout_link-\>data);

456 \_dbus_list_free_link (pending-\>timeout_link);

457 pending-\>timeout_link = NULL;

458 }

459

460 if (pending-\>reply)

461 {

462 dbus_message_unref (pending-\>reply);

463 pending-\>reply = NULL;

464 }

465

466 dbus_free (pending);

467

468 dbus_pending_call_free_data_slot (&notify_user_data_slot);

469

470 /\* connection lock should not be held. \*/

471 /\* Free the connection last to avoid a weird state while

472 \* calling out to application code where the pending exists

473 \* but not the connection.

474 \*/

475 dbus_connection_unref (connection);

476}

477

485void

486\_dbus_pending_call_unref_and_unlock (DBusPendingCall \*pending)

487{

488 dbus_int32_t old_refcount;

489

490 old_refcount = \_dbus_atomic_dec (&pending-\>refcount);

491 \_dbus_assert (old_refcount \> 0);

492 \_dbus_pending_call_trace_ref (pending, old_refcount,

493 old_refcount - 1, "unref_and_unlock");

494

495 CONNECTION_UNLOCK (pending-\>connection);

496

497 if (old_refcount == 1)

498 \_dbus_pending_call_last_unref (pending);

499}

500

508dbus_bool_t

509\_dbus_pending_call_get_completed_unlocked (DBusPendingCall \*pending)

510{

511 return pending-\>completed;

512}

513

514static DBusDataSlotAllocator slot_allocator =

515 \_DBUS_DATA_SLOT_ALLOCATOR_INIT (\_DBUS_LOCK_NAME (pending_call_slots));

516

530dbus_bool_t

531\_dbus_pending_call_set_data_unlocked (DBusPendingCall \*pending,

532 dbus_int32_t slot,

533 void \*data,

534 DBusFreeFunction free_data_func)

535{

536 DBusFreeFunction old_free_func;

537 void \*old_data;

538 dbus_bool_t retval;

539

540 retval = \_dbus_data_slot_list_set (&slot_allocator,

541 &pending-\>slot_list,

542 slot, data, free_data_func,

543 &old_free_func, &old_data);

544

545 /\* Drop locks to call out to app code \*/

546 CONNECTION_UNLOCK (pending-\>connection);

547

548 if (retval)

549 {

550 if (old_free_func)

551 (\* old_free_func) (old_data);

552 }

553

554 CONNECTION_LOCK (pending-\>connection);

555

556 return retval;

557}

558

605DBusPendingCall \*

606dbus_pending_call_ref (DBusPendingCall \*pending)

607{

608 dbus_int32_t old_refcount;

609

610 \_dbus_return_val_if_fail (pending != NULL, NULL);

611

612 old_refcount = \_dbus_atomic_inc (&pending-\>refcount);

613 \_dbus_pending_call_trace_ref (pending, old_refcount, old_refcount + 1,

614 "ref");

615

616 return pending;

617}

618

625void

626dbus_pending_call_unref (DBusPendingCall \*pending)

627{

628 dbus_int32_t old_refcount;

629

630 \_dbus_return_if_fail (pending != NULL);

631

632 old_refcount = \_dbus_atomic_dec (&pending-\>refcount);

633 \_dbus_pending_call_trace_ref (pending, old_refcount, old_refcount - 1,

634 "unref");

635

636 if (old_refcount == 1)

637 \_dbus_pending_call_last_unref(pending);

638}

639

650dbus_bool_t

651dbus_pending_call_set_notify (DBusPendingCall \*pending,

652 DBusPendingCallNotifyFunction function,

653 void \*user_data,

654 DBusFreeFunction free_user_data)

655{

656 dbus_bool_t ret = FALSE;

657

658 \_dbus_return_val_if_fail (pending != NULL, FALSE);

659

660 CONNECTION_LOCK (pending-\>connection);

661

662 /\* could invoke application code! \*/

663 if (!\_dbus_pending_call_set_data_unlocked (pending, notify_user_data_slot,

664 user_data, free_user_data))

665 goto out;

666

667 pending-\>function = function;

668 ret = TRUE;

669

670out:

671 CONNECTION_UNLOCK (pending-\>connection);

672

673 return ret;

674}

675

691void

692dbus_pending_call_cancel (DBusPendingCall \*pending)

693{

694 \_dbus_return_if_fail (pending != NULL);

695

696 \_dbus_connection_remove_pending_call (pending-\>connection,

697 pending);

698}

699

707dbus_bool_t

708dbus_pending_call_get_completed (DBusPendingCall \*pending)

709{

710 dbus_bool_t completed;

711

712 \_dbus_return_val_if_fail (pending != NULL, FALSE);

713

714 CONNECTION_LOCK (pending-\>connection);

715 completed = pending-\>completed;

716 CONNECTION_UNLOCK (pending-\>connection);

717

718 return completed;

719}

720

730DBusMessage\*

731dbus_pending_call_steal_reply (DBusPendingCall \*pending)

732{

733 DBusMessage \*message;

734

735 \_dbus_return_val_if_fail (pending != NULL, NULL);

736 \_dbus_return_val_if_fail (pending-\>completed, NULL);

737 \_dbus_return_val_if_fail (pending-\>reply != NULL, NULL);

738

739 CONNECTION_LOCK (pending-\>connection);

740

741 message = pending-\>reply;

742 pending-\>reply = NULL;

743

744 CONNECTION_UNLOCK (pending-\>connection);

745

746 \_dbus_message_trace_ref (message, -1, -1, "dbus_pending_call_steal_reply");

747 return message;

748}

749

765void

766dbus_pending_call_block (DBusPendingCall \*pending)

767{

768 \_dbus_return_if_fail (pending != NULL);

769

770 \_dbus_connection_block_pending_call (pending);

771}

772

787dbus_bool_t

788dbus_pending_call_allocate_data_slot (dbus_int32_t \*slot_p)

789{

790 \_dbus_return_val_if_fail (slot_p != NULL, FALSE);

791

792 return \_dbus_data_slot_allocator_alloc (&slot_allocator,

793 slot_p);

794}

795

807void

808dbus_pending_call_free_data_slot (dbus_int32_t \*slot_p)

809{

810 \_dbus_return_if_fail (slot_p != NULL);

811 \_dbus_return_if_fail (\*slot_p \>= 0);

812

813 \_dbus_data_slot_allocator_free (&slot_allocator, slot_p);

814}

815

829dbus_bool_t

830dbus_pending_call_set_data (DBusPendingCall \*pending,

831 dbus_int32_t slot,

832 void \*data,

833 DBusFreeFunction free_data_func)

834{

835 dbus_bool_t retval;

836

837 \_dbus_return_val_if_fail (pending != NULL, FALSE);

838 \_dbus_return_val_if_fail (slot \>= 0, FALSE);

839

840

841 CONNECTION_LOCK (pending-\>connection);

842 retval = \_dbus_pending_call_set_data_unlocked (pending, slot, data, free_data_func);

843 CONNECTION_UNLOCK (pending-\>connection);

844 return retval;

845}

846

855void\*

856dbus_pending_call_get_data (DBusPendingCall \*pending,

857 dbus_int32_t slot)

858{

859 void \*res;

860

861 \_dbus_return_val_if_fail (pending != NULL, NULL);

862

863 CONNECTION_LOCK (pending-\>connection);

864 res = \_dbus_data_slot_list_get (&slot_allocator,

865 &pending-\>slot_list,

866 slot);

867 CONNECTION_UNLOCK (pending-\>connection);

868

869 return res;

870}

871

\_dbus_connection_remove_pending_call

void \_dbus_connection_remove_pending_call(DBusConnection \*connection, DBusPendingCall \*pending)

Removes a pending call from the connection, such that the pending reply will be ignored.

**Definition** dbus-connection.c:1048

\_dbus_connection_block_pending_call

void \_dbus_connection_block_pending_call(DBusPendingCall \*pending)

Blocks until a pending call times out or gets a reply.

**Definition** dbus-connection.c:2394

\_dbus_connection_queue_synthesized_message_link

void \_dbus_connection_queue_synthesized_message_link(DBusConnection \*connection, DBusList \*link)

Adds a link + message to the incoming message queue.

**Definition** dbus-connection.c:549

\_dbus_connection_ref_unlocked

DBUS_PRIVATE_EXPORT DBusConnection \* \_dbus_connection_ref_unlocked(DBusConnection \*connection)

Increments the reference count of a DBusConnection.

**Definition** dbus-connection.c:1424

dbus_connection_unref

void dbus_connection_unref(DBusConnection \*connection)

Decrements the reference count of a DBusConnection, and finalizes it if the count reaches zero.

**Definition** dbus-connection.c:2832

DBusPendingCallNotifyFunction

void(\* DBusPendingCallNotifyFunction)(DBusPendingCall \*pending, void \*user_data)

Called when a pending call now has a reply available.

**Definition** dbus-connection.h:165

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

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_DBUS_LOCK_NAME

\#define \_DBUS_LOCK_NAME(name)

Expands to name of a global lock variable.

**Definition** dbus-internals.h:436

\_dbus_list_free_link

void \_dbus_list_free_link(DBusList \*link)

Frees a linked list node allocated with \_dbus_list_alloc_link.

**Definition** dbus-list.c:257

\_dbus_list_clear

void \_dbus_list_clear(DBusList \*\*list)

Frees all links in the list and sets the list head to NULL.

**Definition** dbus-list.c:545

\_dbus_list_alloc_link

DBusList \* \_dbus_list_alloc_link(void \*data)

Allocates a linked list node.

**Definition** dbus-list.c:245

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

dbus_message_new_error

DBusMessage \* dbus_message_new_error(DBusMessage \*reply_to, const char \*error_name, const char \*error_message)

Creates a new message that is an error reply to another message.

**Definition** dbus-message.c:1515

dbus_message_get_type

int dbus_message_get_type(DBusMessage \*message)

Gets the type of a message.

**Definition** dbus-message.c:1767

dbus_message_ref

DBusMessage \* dbus_message_ref(DBusMessage \*message)

Increments the reference count of a DBusMessage.

**Definition** dbus-message.c:1712

dbus_message_get_reply_serial

dbus_uint32_t dbus_message_get_reply_serial(DBusMessage \*message)

Returns the serial that the message is a reply to or 0 if none.

**Definition** dbus-message.c:1208

dbus_message_unref

void dbus_message_unref(DBusMessage \*message)

Decrements the reference count of a DBusMessage, freeing the message if the count reaches 0.

**Definition** dbus-message.c:1735

\_dbus_pending_call_finish_completion

void \_dbus_pending_call_finish_completion(DBusPendingCall \*pending)

Call the notifier function for the pending call.

**Definition** dbus-pending-call.c:235

\_dbus_pending_call_get_connection_and_lock

DBusConnection \* \_dbus_pending_call_get_connection_and_lock(DBusPendingCall \*pending)

Gets the connection associated with this pending call.

**Definition** dbus-pending-call.c:352

\_dbus_pending_call_ref_unlocked

DBusPendingCall \* \_dbus_pending_call_ref_unlocked(DBusPendingCall \*pending)

Increments the reference count on a pending call, while the lock on its connection is already held.

**Definition** dbus-pending-call.c:423

\_dbus_pending_call_queue_timeout_error_unlocked

void \_dbus_pending_call_queue_timeout_error_unlocked(DBusPendingCall \*pending, DBusConnection \*connection)

If the pending call hasn't been timed out, add its timeout error reply to the connection's incoming m...

**Definition** dbus-pending-call.c:257

\_dbus_pending_call_unref_and_unlock

void \_dbus_pending_call_unref_and_unlock(DBusPendingCall \*pending)

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

\_dbus_pending_call_set_reply_serial_unlocked

void \_dbus_pending_call_set_reply_serial_unlocked(DBusPendingCall \*pending, dbus_uint32_t serial)

Sets the reply's serial number.

**Definition** dbus-pending-call.c:336

\_dbus_pending_call_set_data_unlocked

dbus_bool_t \_dbus_pending_call_set_data_unlocked(DBusPendingCall \*pending, dbus_int32_t slot, void \*data, DBusFreeFunction free_data_func)

Stores a pointer on a DBusPendingCall, along with an optional function to be used for freeing the dat...

**Definition** dbus-pending-call.c:531

\_dbus_pending_call_new_unlocked

DBusPendingCall \* \_dbus_pending_call_new_unlocked(DBusConnection \*connection, int timeout_milliseconds, DBusTimeoutHandler timeout_handler)

Creates a new pending reply object.

**Definition** dbus-pending-call.c:120

\_dbus_pending_call_set_timeout_error_unlocked

dbus_bool_t \_dbus_pending_call_set_timeout_error_unlocked(DBusPendingCall \*pending, DBusMessage \*message, dbus_uint32_t serial)

Sets the reply message associated with the pending call to a timeout error.

**Definition** dbus-pending-call.c:383

CONNECTION_LOCK

\#define CONNECTION_LOCK(connection)

Internals of DBusPendingCall.

**Definition** dbus-pending-call.c:55

CONNECTION_UNLOCK

\#define CONNECTION_UNLOCK(connection)

shorter and more visible way to write \_dbus_connection_unlock()

**Definition** dbus-pending-call.c:59

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

dbus_pending_call_set_notify

dbus_bool_t dbus_pending_call_set_notify(DBusPendingCall \*pending, DBusPendingCallNotifyFunction function, void \*user_data, DBusFreeFunction free_user_data)

Sets a notification function to be called when the reply is received or the pending call times out.

**Definition** dbus-pending-call.c:651

dbus_pending_call_free_data_slot

void dbus_pending_call_free_data_slot(dbus_int32_t \*slot_p)

Deallocates a global ID for DBusPendingCall data slots.

**Definition** dbus-pending-call.c:808

DBUS_TIMEOUT_INFINITE

\#define DBUS_TIMEOUT_INFINITE

An integer constant representing an infinite timeout.

**Definition** dbus-pending-call.h:43

dbus_pending_call_ref

DBusPendingCall \* dbus_pending_call_ref(DBusPendingCall \*pending)

Increments the reference count on a pending call.

**Definition** dbus-pending-call.c:606

dbus_pending_call_get_data

void \* dbus_pending_call_get_data(DBusPendingCall \*pending, dbus_int32_t slot)

Retrieves data previously set with dbus_pending_call_set_data().

**Definition** dbus-pending-call.c:856

dbus_pending_call_steal_reply

DBusMessage \* dbus_pending_call_steal_reply(DBusPendingCall \*pending)

Gets the reply, or returns NULL if none has been received yet.

**Definition** dbus-pending-call.c:731

dbus_pending_call_cancel

void dbus_pending_call_cancel(DBusPendingCall \*pending)

Cancels the pending call, such that any reply or error received will just be ignored.

**Definition** dbus-pending-call.c:692

dbus_pending_call_block

void dbus_pending_call_block(DBusPendingCall \*pending)

Block until the pending call is completed.

**Definition** dbus-pending-call.c:766

dbus_pending_call_set_data

dbus_bool_t dbus_pending_call_set_data(DBusPendingCall \*pending, dbus_int32_t slot, void \*data, DBusFreeFunction free_data_func)

Stores a pointer on a DBusPendingCall, along with an optional function to be used for freeing the dat...

**Definition** dbus-pending-call.c:830

dbus_pending_call_allocate_data_slot

dbus_bool_t dbus_pending_call_allocate_data_slot(dbus_int32_t \*slot_p)

Allocates an integer ID to be used for storing application-specific data on any DBusPendingCall.

**Definition** dbus-pending-call.c:788

dbus_pending_call_get_completed

dbus_bool_t dbus_pending_call_get_completed(DBusPendingCall \*pending)

Checks whether the pending call has received a reply yet, or not.

**Definition** dbus-pending-call.c:708

dbus_pending_call_unref

void dbus_pending_call_unref(DBusPendingCall \*pending)

Decrements the reference count on a pending call, freeing it if the count reaches 0.

**Definition** dbus-pending-call.c:626

DBUS_MESSAGE_TYPE_ERROR

\#define DBUS_MESSAGE_TYPE_ERROR

Message type of an error reply message, see dbus_message_get_type()

**Definition** dbus-protocol.h:240

DBUS_MESSAGE_TYPE_METHOD_RETURN

\#define DBUS_MESSAGE_TYPE_METHOD_RETURN

Message type of a method return message, see dbus_message_get_type()

**Definition** dbus-protocol.h:238

DBUS_ERROR_NO_REPLY

\#define DBUS_ERROR_NO_REPLY

No reply to a message expecting one, usually means a timeout occurred.

**Definition** dbus-protocol.h:369

\_dbus_atomic_dec

dbus_int32_t \_dbus_atomic_dec(DBusAtomic \*atomic)

Atomically decrement an integer.

**Definition** dbus-sysdeps-unix.c:3205

\_dbus_atomic_inc

dbus_int32_t \_dbus_atomic_inc(DBusAtomic \*atomic)

Atomically increments an integer.

**Definition** dbus-sysdeps-unix.c:3178

\_dbus_timeout_unref

void \_dbus_timeout_unref(DBusTimeout \*timeout)

Decrements the reference count of a DBusTimeout object and finalizes the object if the count reaches ...

**Definition** dbus-timeout.c:111

\_dbus_timeout_new

DBusTimeout \* \_dbus_timeout_new(int interval, DBusTimeoutHandler handler, void \*data, DBusFreeFunction free_data_function)

Creates a new DBusTimeout, enabled by default.

**Definition** dbus-timeout.c:66

DBusTimeoutHandler

dbus_bool_t(\* DBusTimeoutHandler)(void \*data)

function to run when the timeout is handled

**Definition** dbus-timeout.h:43

DBusAtomic

An atomic integer safe to increment or decrement from multiple threads.

**Definition** dbus-sysdeps.h:340

DBusConnection

Implementation details of DBusConnection.

**Definition** dbus-connection.c:259

DBusDataSlotAllocator

An allocator that tracks a set of slot IDs.

**Definition** dbus-dataslot.h:58

DBusDataSlotList

Data structure that stores the actual user data set at a given slot.

**Definition** dbus-dataslot.h:72

DBusList

A node in a linked list.

**Definition** dbus-list.h:37

DBusList::data

void \* data

Data stored at this element.

**Definition** dbus-list.h:40

DBusMessage

Internals of DBusMessage.

**Definition** dbus-message-private.h:102

DBusPendingCall

Implementation details of DBusPendingCall - all fields are private.

**Definition** dbus-pending-call.c:65

DBusPendingCall::function

DBusPendingCallNotifyFunction function

Notifier when reply arrives.

**Definition** dbus-pending-call.c:70

DBusPendingCall::reply

DBusMessage \* reply

Reply (after we've received it)

**Definition** dbus-pending-call.c:73

DBusPendingCall::timeout_link

DBusList \* timeout_link

Preallocated timeout response.

**Definition** dbus-pending-call.c:76

DBusPendingCall::refcount

DBusAtomic refcount

reference count

**Definition** dbus-pending-call.c:66

DBusPendingCall::timeout_added

unsigned int timeout_added

TRUE if we have added the timeout.

**Definition** dbus-pending-call.c:89

DBusPendingCall::reply_serial

dbus_uint32_t reply_serial

Expected serial of reply.

**Definition** dbus-pending-call.c:78

DBusPendingCall::completed

unsigned int completed

TRUE if some thread has taken responsibility for completing this pending call: either the pending cal...

**Definition** dbus-pending-call.c:85

DBusPendingCall::slot_list

DBusDataSlotList slot_list

Data stored by allocated integer ID.

**Definition** dbus-pending-call.c:68

DBusPendingCall::connection

DBusConnection \* connection

Connections we're associated with.

**Definition** dbus-pending-call.c:72

DBusPendingCall::timeout

DBusTimeout \* timeout

Timeout.

**Definition** dbus-pending-call.c:74

DBusTimeout

Internals of DBusTimeout.

**Definition** dbus-timeout.c:43
