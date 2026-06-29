dbus-connection.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-connection.h DBusConnection object

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

25\#if !defined (DBUS_INSIDE_DBUS_H) && !defined (DBUS_COMPILATION)

26\#error "Only \<dbus/dbus.h\> can be included directly, this file may disappear or change contents."

27\#endif

28

29\#ifndef DBUS_CONNECTION_H

30\#define DBUS_CONNECTION_H

31

32\#include \<dbus/dbus-errors.h\>

33\#include \<dbus/dbus-macros.h\>

34\#include \<dbus/dbus-memory.h\>

35\#include \<dbus/dbus-message.h\>

36\#include \<dbus/dbus-shared.h\>

37

38DBUS_BEGIN_DECLS

39

45/\* documented in dbus-watch.c \*/

46typedef struct DBusWatch DBusWatch;

47/\* documented in dbus-timeout.c \*/

48typedef struct DBusTimeout DBusTimeout;

50typedef struct DBusPreallocatedSend DBusPreallocatedSend;

52typedef struct DBusPendingCall DBusPendingCall;

54typedef struct DBusConnection DBusConnection;

56typedef struct DBusObjectPathVTable DBusObjectPathVTable;

57

61typedef enum

62{

63 DBUS_WATCH_READABLE = 1 \<\< 0,

64 DBUS_WATCH_WRITABLE = 1 \<\< 1,

65 DBUS_WATCH_ERROR = 1 \<\< 2,

70 DBUS_WATCH_HANGUP = 1 \<\< 3

75 /\* Internal to libdbus, there is also \_DBUS_WATCH_NVAL in dbus-watch.h \*/

76} DBusWatchFlags;

77

82typedef enum

83{

84 DBUS_DISPATCH_DATA_REMAINS,

85 DBUS_DISPATCH_COMPLETE,

86 DBUS_DISPATCH_NEED_MEMORY

87} DBusDispatchStatus;

88

94typedef dbus_bool_t (\* DBusAddWatchFunction) (DBusWatch \*watch,

95 void \*data);

100typedef void (\* DBusWatchToggledFunction) (DBusWatch \*watch,

101 void \*data);

106typedef void (\* DBusRemoveWatchFunction) (DBusWatch \*watch,

107 void \*data);

113typedef dbus_bool_t (\* DBusAddTimeoutFunction) (DBusTimeout \*timeout,

114 void \*data);

120typedef void (\* DBusTimeoutToggledFunction) (DBusTimeout \*timeout,

121 void \*data);

126typedef void (\* DBusRemoveTimeoutFunction) (DBusTimeout \*timeout,

127 void \*data);

131typedef void (\* DBusDispatchStatusFunction) (DBusConnection \*connection,

132 DBusDispatchStatus new_status,

133 void \*data);

138typedef void (\* DBusWakeupMainFunction) (void \*data);

139

146typedef dbus_bool_t (\* DBusAllowUnixUserFunction) (DBusConnection \*connection,

147 unsigned long uid,

148 void \*data);

149

156typedef dbus_bool_t (\* DBusAllowWindowsUserFunction) (DBusConnection \*connection,

157 const char \*user_sid,

158 void \*data);

159

160

165typedef void (\* DBusPendingCallNotifyFunction) (DBusPendingCall \*pending,

166 void \*user_data);

167

172typedef DBusHandlerResult (\* DBusHandleMessageFunction) (DBusConnection \*connection,

173 DBusMessage \*message,

174 void \*user_data);

175DBUS_EXPORT

176DBusConnection\* dbus_connection_open (const char \*address,

177 DBusError \*error);

178DBUS_EXPORT

179DBusConnection\* dbus_connection_open_private (const char \*address,

180 DBusError \*error);

181DBUS_EXPORT

182DBusConnection\* dbus_connection_ref (DBusConnection \*connection);

183DBUS_EXPORT

184void dbus_connection_unref (DBusConnection \*connection);

185DBUS_EXPORT

186void dbus_connection_close (DBusConnection \*connection);

187DBUS_EXPORT

188dbus_bool_t dbus_connection_get_is_connected (DBusConnection \*connection);

189DBUS_EXPORT

190dbus_bool_t dbus_connection_get_is_authenticated (DBusConnection \*connection);

191DBUS_EXPORT

192dbus_bool_t dbus_connection_get_is_anonymous (DBusConnection \*connection);

193DBUS_EXPORT

194char\* dbus_connection_get_server_id (DBusConnection \*connection);

195DBUS_EXPORT

196dbus_bool_t dbus_connection_can_send_type (DBusConnection \*connection,

197 int type);

198

199DBUS_EXPORT

200void dbus_connection_set_exit_on_disconnect (DBusConnection \*connection,

201 dbus_bool_t exit_on_disconnect);

202DBUS_EXPORT

203void dbus_connection_flush (DBusConnection \*connection);

204DBUS_EXPORT

205dbus_bool_t dbus_connection_read_write_dispatch (DBusConnection \*connection,

206 int timeout_milliseconds);

207DBUS_EXPORT

208dbus_bool_t dbus_connection_read_write (DBusConnection \*connection,

209 int timeout_milliseconds);

210DBUS_EXPORT

211DBusMessage\* dbus_connection_borrow_message (DBusConnection \*connection);

212DBUS_EXPORT

213void dbus_connection_return_message (DBusConnection \*connection,

214 DBusMessage \*message);

215DBUS_EXPORT

216void dbus_connection_steal_borrowed_message (DBusConnection \*connection,

217 DBusMessage \*message);

218DBUS_EXPORT

219DBusMessage\* dbus_connection_pop_message (DBusConnection \*connection);

220DBUS_EXPORT

221DBusDispatchStatus dbus_connection_get_dispatch_status (DBusConnection \*connection);

222DBUS_EXPORT

223DBusDispatchStatus dbus_connection_dispatch (DBusConnection \*connection);

224DBUS_EXPORT

225dbus_bool_t dbus_connection_has_messages_to_send (DBusConnection \*connection);

226DBUS_EXPORT

227dbus_bool_t dbus_connection_send (DBusConnection \*connection,

228 DBusMessage \*message,

229 dbus_uint32_t \*client_serial);

230DBUS_EXPORT

231dbus_bool_t dbus_connection_send_with_reply (DBusConnection \*connection,

232 DBusMessage \*message,

233 DBusPendingCall \*\*pending_return,

234 int timeout_milliseconds);

235DBUS_EXPORT

236DBusMessage \* dbus_connection_send_with_reply_and_block (DBusConnection \*connection,

237 DBusMessage \*message,

238 int timeout_milliseconds,

239 DBusError \*error);

240DBUS_EXPORT

241dbus_bool_t dbus_connection_set_watch_functions (DBusConnection \*connection,

242 DBusAddWatchFunction add_function,

243 DBusRemoveWatchFunction remove_function,

244 DBusWatchToggledFunction toggled_function,

245 void \*data,

246 DBusFreeFunction free_data_function);

247DBUS_EXPORT

248dbus_bool_t dbus_connection_set_timeout_functions (DBusConnection \*connection,

249 DBusAddTimeoutFunction add_function,

250 DBusRemoveTimeoutFunction remove_function,

251 DBusTimeoutToggledFunction toggled_function,

252 void \*data,

253 DBusFreeFunction free_data_function);

254DBUS_EXPORT

255void dbus_connection_set_wakeup_main_function (DBusConnection \*connection,

256 DBusWakeupMainFunction wakeup_main_function,

257 void \*data,

258 DBusFreeFunction free_data_function);

259DBUS_EXPORT

260void dbus_connection_set_dispatch_status_function (DBusConnection \*connection,

261 DBusDispatchStatusFunction function,

262 void \*data,

263 DBusFreeFunction free_data_function);

264DBUS_EXPORT

265dbus_bool_t dbus_connection_get_unix_user (DBusConnection \*connection,

266 unsigned long \*uid);

267DBUS_EXPORT

268dbus_bool_t dbus_connection_get_unix_process_id (DBusConnection \*connection,

269 unsigned long \*pid);

270DBUS_EXPORT

271dbus_bool_t dbus_connection_get_adt_audit_session_data (DBusConnection \*connection,

272 void \*\*data,

273 dbus_int32_t \*data_size);

274DBUS_EXPORT

275void dbus_connection_set_unix_user_function (DBusConnection \*connection,

276 DBusAllowUnixUserFunction function,

277 void \*data,

278 DBusFreeFunction free_data_function);

279DBUS_EXPORT

280dbus_bool_t dbus_connection_get_windows_user (DBusConnection \*connection,

281 char \*\*windows_sid_p);

282DBUS_EXPORT

283void dbus_connection_set_windows_user_function (DBusConnection \*connection,

284 DBusAllowWindowsUserFunction function,

285 void \*data,

286 DBusFreeFunction free_data_function);

287DBUS_EXPORT

288void dbus_connection_set_allow_anonymous (DBusConnection \*connection,

289 dbus_bool_t value);

290DBUS_EXPORT

291void dbus_connection_set_builtin_filters_enabled (DBusConnection \*connection,

292 dbus_bool_t value);

293DBUS_EXPORT

294void dbus_connection_set_route_peer_messages (DBusConnection \*connection,

295 dbus_bool_t value);

296

297

298/\* Filters \*/

299

300DBUS_EXPORT

301dbus_bool_t dbus_connection_add_filter (DBusConnection \*connection,

302 DBusHandleMessageFunction function,

303 void \*user_data,

304 DBusFreeFunction free_data_function);

305DBUS_EXPORT

306void dbus_connection_remove_filter (DBusConnection \*connection,

307 DBusHandleMessageFunction function,

308 void \*user_data);

309

310

311/\* Other \*/

312DBUS_EXPORT

313dbus_bool_t dbus_connection_allocate_data_slot (dbus_int32_t \*slot_p);

314DBUS_EXPORT

315void dbus_connection_free_data_slot (dbus_int32_t \*slot_p);

316DBUS_EXPORT

317dbus_bool_t dbus_connection_set_data (DBusConnection \*connection,

318 dbus_int32_t slot,

319 void \*data,

320 DBusFreeFunction free_data_func);

321DBUS_EXPORT

322void\* dbus_connection_get_data (DBusConnection \*connection,

323 dbus_int32_t slot);

324

325DBUS_EXPORT

326void dbus_connection_set_change_sigpipe (dbus_bool_t will_modify_sigpipe);

327

328DBUS_EXPORT

329void dbus_connection_set_max_message_size (DBusConnection \*connection,

330 long size);

331DBUS_EXPORT

332long dbus_connection_get_max_message_size (DBusConnection \*connection);

333DBUS_EXPORT

334void dbus_connection_set_max_received_size (DBusConnection \*connection,

335 long size);

336DBUS_EXPORT

337long dbus_connection_get_max_received_size (DBusConnection \*connection);

338

339DBUS_EXPORT

340void dbus_connection_set_max_message_unix_fds (DBusConnection \*connection,

341 long n);

342DBUS_EXPORT

343long dbus_connection_get_max_message_unix_fds (DBusConnection \*connection);

344DBUS_EXPORT

345void dbus_connection_set_max_received_unix_fds(DBusConnection \*connection,

346 long n);

347DBUS_EXPORT

348long dbus_connection_get_max_received_unix_fds(DBusConnection \*connection);

349

350DBUS_EXPORT

351long dbus_connection_get_outgoing_size (DBusConnection \*connection);

352DBUS_EXPORT

353long dbus_connection_get_outgoing_unix_fds (DBusConnection \*connection);

354

355DBUS_EXPORT

356DBusPreallocatedSend\* dbus_connection_preallocate_send (DBusConnection \*connection);

357DBUS_EXPORT

358void dbus_connection_free_preallocated_send (DBusConnection \*connection,

359 DBusPreallocatedSend \*preallocated);

360DBUS_EXPORT

361void dbus_connection_send_preallocated (DBusConnection \*connection,

362 DBusPreallocatedSend \*preallocated,

363 DBusMessage \*message,

364 dbus_uint32_t \*client_serial);

365

366

367/\* Object tree functionality \*/

368

373typedef void (\* DBusObjectPathUnregisterFunction) (DBusConnection \*connection,

374 void \*user_data);

380typedef DBusHandlerResult (\* DBusObjectPathMessageFunction) (DBusConnection \*connection,

381 DBusMessage \*message,

382 void \*user_data);

383

390struct DBusObjectPathVTable

391{

392 DBusObjectPathUnregisterFunction unregister_function;

393 DBusObjectPathMessageFunction message_function;

395 void (\* dbus_internal_pad1) (void \*);

396 void (\* dbus_internal_pad2) (void \*);

397 void (\* dbus_internal_pad3) (void \*);

398 void (\* dbus_internal_pad4) (void \*);

399};

400

401DBUS_EXPORT

402dbus_bool_t dbus_connection_try_register_object_path (DBusConnection \*connection,

403 const char \*path,

404 const DBusObjectPathVTable \*vtable,

405 void \*user_data,

406 DBusError \*error);

407

408DBUS_EXPORT

409dbus_bool_t dbus_connection_register_object_path (DBusConnection \*connection,

410 const char \*path,

411 const DBusObjectPathVTable \*vtable,

412 void \*user_data);

413

414DBUS_EXPORT

415dbus_bool_t dbus_connection_try_register_fallback (DBusConnection \*connection,

416 const char \*path,

417 const DBusObjectPathVTable \*vtable,

418 void \*user_data,

419 DBusError \*error);

420

421DBUS_EXPORT

422dbus_bool_t dbus_connection_register_fallback (DBusConnection \*connection,

423 const char \*path,

424 const DBusObjectPathVTable \*vtable,

425 void \*user_data);

426DBUS_EXPORT

427dbus_bool_t dbus_connection_unregister_object_path (DBusConnection \*connection,

428 const char \*path);

429

430DBUS_EXPORT

431dbus_bool_t dbus_connection_get_object_path_data (DBusConnection \*connection,

432 const char \*path,

433 void \*\*data_p);

434

435DBUS_EXPORT

436dbus_bool_t dbus_connection_list_registered (DBusConnection \*connection,

437 const char \*parent_path,

438 char \*\*\*child_entries);

439

440DBUS_EXPORT

441dbus_bool_t dbus_connection_get_unix_fd (DBusConnection \*connection,

442 int \*fd);

443DBUS_EXPORT

444dbus_bool_t dbus_connection_get_socket (DBusConnection \*connection,

445 int \*fd);

446

469static inline void

470dbus_clear_connection (DBusConnection \*\*pointer_to_connection)

471{

472 \_dbus_clear_pointer_impl (DBusConnection, pointer_to_connection,

473 dbus_connection_unref);

474}

475

484\#ifndef DBUS_DISABLE_DEPRECATED

485DBUS_EXPORT

486DBUS_DEPRECATED int dbus_watch_get_fd (DBusWatch \*watch);

487\#endif

488

489DBUS_EXPORT

490int dbus_watch_get_unix_fd (DBusWatch \*watch);

491DBUS_EXPORT

492int dbus_watch_get_socket (DBusWatch \*watch);

493DBUS_EXPORT

494unsigned int dbus_watch_get_flags (DBusWatch \*watch);

495DBUS_EXPORT

496void\* dbus_watch_get_data (DBusWatch \*watch);

497DBUS_EXPORT

498void dbus_watch_set_data (DBusWatch \*watch,

499 void \*data,

500 DBusFreeFunction free_data_function);

501DBUS_EXPORT

502dbus_bool_t dbus_watch_handle (DBusWatch \*watch,

503 unsigned int flags);

504DBUS_EXPORT

505dbus_bool_t dbus_watch_get_enabled (DBusWatch \*watch);

506

514DBUS_EXPORT

515int dbus_timeout_get_interval (DBusTimeout \*timeout);

516DBUS_EXPORT

517void\* dbus_timeout_get_data (DBusTimeout \*timeout);

518DBUS_EXPORT

519void dbus_timeout_set_data (DBusTimeout \*timeout,

520 void \*data,

521 DBusFreeFunction free_data_function);

522DBUS_EXPORT

523dbus_bool_t dbus_timeout_handle (DBusTimeout \*timeout);

524DBUS_EXPORT

525dbus_bool_t dbus_timeout_get_enabled (DBusTimeout \*timeout);

526

529DBUS_END_DECLS

530

531\#endif /\* DBUS_CONNECTION_H \*/

DBusWatchFlags

DBusWatchFlags

Indicates the status of a DBusWatch.

**Definition** dbus-connection.h:62

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

DBusObjectPathMessageFunction

DBusHandlerResult(\* DBusObjectPathMessageFunction)(DBusConnection \*connection, DBusMessage \*message, void \*user_data)

Called when a message is sent to a registered object path.

**Definition** dbus-connection.h:380

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

DBusObjectPathUnregisterFunction

void(\* DBusObjectPathUnregisterFunction)(DBusConnection \*connection, void \*user_data)

Called when a DBusObjectPathVTable is unregistered (or its connection is freed).

**Definition** dbus-connection.h:373

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

DBusPendingCallNotifyFunction

void(\* DBusPendingCallNotifyFunction)(DBusPendingCall \*pending, void \*user_data)

Called when a pending call now has a reply available.

**Definition** dbus-connection.h:165

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

dbus_connection_has_messages_to_send

DBUS_EXPORT dbus_bool_t dbus_connection_has_messages_to_send(DBusConnection \*connection)

Checks whether there are messages in the outgoing message queue.

**Definition** dbus-connection.c:592

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

DBUS_WATCH_READABLE

@ DBUS_WATCH_READABLE

As in POLLIN.

**Definition** dbus-connection.h:63

DBUS_WATCH_WRITABLE

@ DBUS_WATCH_WRITABLE

As in POLLOUT.

**Definition** dbus-connection.h:64

DBUS_WATCH_HANGUP

@ DBUS_WATCH_HANGUP

As in POLLHUP (can't watch for it, but can be present in current state passed to dbus_watch_handle())...

**Definition** dbus-connection.h:70

DBUS_WATCH_ERROR

@ DBUS_WATCH_ERROR

As in POLLERR (can't watch for this, but can be present in current state passed to dbus_watch_handle(...

**Definition** dbus-connection.h:65

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

DBUS_DEPRECATED

\#define DBUS_DEPRECATED

Tells the compiler to warn about a function or type if it's used.

**Definition** dbus-macros.h:60

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

DBusFreeFunction

void(\* DBusFreeFunction)(void \*memory)

The type of a function which frees a block of memory.

**Definition** dbus-memory.h:65

DBusHandlerResult

DBusHandlerResult

Results that a message handler can return.

**Definition** dbus-shared.h:69

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

dbus_timeout_get_data

DBUS_EXPORT void \* dbus_timeout_get_data(DBusTimeout \*timeout)

Gets data previously set with dbus_timeout_set_data() or NULL if none.

**Definition** dbus-timeout.c:457

dbus_timeout_set_data

DBUS_EXPORT void dbus_timeout_set_data(DBusTimeout \*timeout, void \*data, DBusFreeFunction free_data_function)

Sets data which can be retrieved with dbus_timeout_get_data().

**Definition** dbus-timeout.c:474

dbus_watch_get_unix_fd

DBUS_EXPORT int dbus_watch_get_unix_fd(DBusWatch \*watch)

Returns a UNIX file descriptor to be watched, which may be a pipe, socket, or other type of descripto...

**Definition** dbus-watch.c:566

dbus_watch_set_data

DBUS_EXPORT void dbus_watch_set_data(DBusWatch \*watch, void \*data, DBusFreeFunction free_data_function)

Sets data which can be retrieved with dbus_watch_get_data().

**Definition** dbus-watch.c:679

dbus_watch_get_fd

DBUS_EXPORT DBUS_DEPRECATED int dbus_watch_get_fd(DBusWatch \*watch)

Deprecated former name of dbus_watch_get_unix_fd().

**Definition** dbus-watch.c:545

dbus_watch_get_data

DBUS_EXPORT void \* dbus_watch_get_data(DBusWatch \*watch)

Gets data previously set with dbus_watch_set_data() or NULL if none.

**Definition** dbus-watch.c:660

dbus_watch_get_socket

DBUS_EXPORT int dbus_watch_get_socket(DBusWatch \*watch)

Returns a socket to be watched, on UNIX this will return -1 if our transport is not socket-based so d...

**Definition** dbus-watch.c:595

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

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusMessage

Internals of DBusMessage.

**Definition** dbus-message-private.h:102

DBusObjectPathVTable

Virtual table that must be implemented to handle a portion of the object path hierarchy.

**Definition** dbus-connection.h:391

DBusObjectPathVTable::dbus_internal_pad1

void(\* dbus_internal_pad1)(void \*)

Reserved for future expansion.

**Definition** dbus-connection.h:395

DBusObjectPathVTable::dbus_internal_pad2

void(\* dbus_internal_pad2)(void \*)

Reserved for future expansion.

**Definition** dbus-connection.h:396

DBusObjectPathVTable::dbus_internal_pad3

void(\* dbus_internal_pad3)(void \*)

Reserved for future expansion.

**Definition** dbus-connection.h:397

DBusObjectPathVTable::message_function

DBusObjectPathMessageFunction message_function

Function to handle messages.

**Definition** dbus-connection.h:393

DBusObjectPathVTable::unregister_function

DBusObjectPathUnregisterFunction unregister_function

Function to unregister this handler.

**Definition** dbus-connection.h:392

DBusObjectPathVTable::dbus_internal_pad4

void(\* dbus_internal_pad4)(void \*)

Reserved for future expansion.

**Definition** dbus-connection.h:398

DBusPendingCall

Implementation details of DBusPendingCall - all fields are private.

**Definition** dbus-pending-call.c:65

DBusPreallocatedSend

Internals of DBusPreallocatedSend.

**Definition** dbus-connection.c:243

DBusTimeout

Internals of DBusTimeout.

**Definition** dbus-timeout.c:43

DBusWatch

Implementation of DBusWatch.

**Definition** dbus-watch.c:43
