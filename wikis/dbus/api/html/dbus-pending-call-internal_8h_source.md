dbus-pending-call-internal.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-pending-call-internal.h DBusPendingCall internal interfaces

3 \*

4 \* Copyright (C) 2002 Red Hat Inc.

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

25\#ifndef DBUS_PENDING_CALL_INTERNAL_H

26\#define DBUS_PENDING_CALL_INTERNAL_H

27

28

29\#include \<dbus/dbus-internals.h\>

30\#include \<dbus/dbus-message.h\>

31\#include \<dbus/dbus-connection.h\>

32\#include \<dbus/dbus-list.h\>

33

34DBUS_BEGIN_DECLS

35

36dbus_bool_t \_dbus_pending_call_is_timeout_added_unlocked (DBusPendingCall \*pending);

37void \_dbus_pending_call_set_timeout_added_unlocked (DBusPendingCall \*pending,

38 dbus_bool_t is_added);

39DBusTimeout \* \_dbus_pending_call_get_timeout_unlocked (DBusPendingCall \*pending);

40dbus_uint32_t \_dbus_pending_call_get_reply_serial_unlocked (DBusPendingCall \*pending);

41void \_dbus_pending_call_set_reply_serial_unlocked (DBusPendingCall \*pending,

42 dbus_uint32_t serial);

43DBusConnection \* \_dbus_pending_call_get_connection_and_lock (DBusPendingCall \*pending);

44DBusConnection \* \_dbus_pending_call_get_connection_unlocked (DBusPendingCall \*pending);

45dbus_bool_t \_dbus_pending_call_get_completed_unlocked (DBusPendingCall \*pending);

46

47void \_dbus_pending_call_start_completion_unlocked (DBusPendingCall \*pending);

48void \_dbus_pending_call_finish_completion (DBusPendingCall \*pending);

49

50void \_dbus_pending_call_set_reply_unlocked (DBusPendingCall \*pending,

51 DBusMessage \*message);

52void \_dbus_pending_call_queue_timeout_error_unlocked (DBusPendingCall \*pending,

53 DBusConnection \*connection);

54dbus_bool_t \_dbus_pending_call_set_timeout_error_unlocked (DBusPendingCall \*pending,

55 DBusMessage \*message,

56 dbus_uint32_t serial);

57DBUS_PRIVATE_EXPORT

58DBusPendingCall\* \_dbus_pending_call_new_unlocked (DBusConnection \*connection,

59 int timeout_milliseconds,

60 DBusTimeoutHandler timeout_handler);

61DBUS_PRIVATE_EXPORT

62DBusPendingCall\* \_dbus_pending_call_ref_unlocked (DBusPendingCall \*pending);

63DBUS_PRIVATE_EXPORT

64void \_dbus_pending_call_unref_and_unlock (DBusPendingCall \*pending);

65dbus_bool_t \_dbus_pending_call_set_data_unlocked (DBusPendingCall \*pending,

66 dbus_int32_t slot,

67 void \*data,

68 DBusFreeFunction free_data_func);

69

70

71DBUS_END_DECLS

72

73\#endif /\* DBUS_PENDING_CALL_INTERNAL_H \*/

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

\_dbus_pending_call_set_reply_serial_unlocked

void \_dbus_pending_call_set_reply_serial_unlocked(DBusPendingCall \*pending, dbus_uint32_t serial)

Sets the reply's serial number.

**Definition** dbus-pending-call.c:336

\_dbus_pending_call_set_data_unlocked

dbus_bool_t \_dbus_pending_call_set_data_unlocked(DBusPendingCall \*pending, dbus_int32_t slot, void \*data, DBusFreeFunction free_data_func)

Stores a pointer on a DBusPendingCall, along with an optional function to be used for freeing the dat...

**Definition** dbus-pending-call.c:531

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

DBusTimeoutHandler

dbus_bool_t(\* DBusTimeoutHandler)(void \*data)

function to run when the timeout is handled

**Definition** dbus-timeout.h:43

DBusConnection

Implementation details of DBusConnection.

**Definition** dbus-connection.c:259

DBusMessage

Internals of DBusMessage.

**Definition** dbus-message-private.h:102

DBusPendingCall

Implementation details of DBusPendingCall - all fields are private.

**Definition** dbus-pending-call.c:65

DBusTimeout

Internals of DBusTimeout.

**Definition** dbus-timeout.c:43
