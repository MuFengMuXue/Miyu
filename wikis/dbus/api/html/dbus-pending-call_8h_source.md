dbus-pending-call.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-pending-call.h Object representing a call in progress.

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

29\#ifndef DBUS_PENDING_CALL_H

30\#define DBUS_PENDING_CALL_H

31

32\#include \<dbus/dbus-macros.h\>

33\#include \<dbus/dbus-types.h\>

34\#include \<dbus/dbus-connection.h\>

35

36DBUS_BEGIN_DECLS

37

43\#define DBUS_TIMEOUT_INFINITE ((int) 0x7fffffff)

44\#define DBUS_TIMEOUT_USE_DEFAULT (-1)

45

46DBUS_EXPORT

47DBusPendingCall\* dbus_pending_call_ref (DBusPendingCall \*pending);

48DBUS_EXPORT

49void dbus_pending_call_unref (DBusPendingCall \*pending);

50DBUS_EXPORT

51dbus_bool_t dbus_pending_call_set_notify (DBusPendingCall \*pending,

52 DBusPendingCallNotifyFunction function,

53 void \*user_data,

54 DBusFreeFunction free_user_data);

55DBUS_EXPORT

56void dbus_pending_call_cancel (DBusPendingCall \*pending);

57DBUS_EXPORT

58dbus_bool_t dbus_pending_call_get_completed (DBusPendingCall \*pending);

59DBUS_EXPORT

60DBusMessage\* dbus_pending_call_steal_reply (DBusPendingCall \*pending);

61DBUS_EXPORT

62void dbus_pending_call_block (DBusPendingCall \*pending);

63

64DBUS_EXPORT

65dbus_bool_t dbus_pending_call_allocate_data_slot (dbus_int32_t \*slot_p);

66DBUS_EXPORT

67void dbus_pending_call_free_data_slot (dbus_int32_t \*slot_p);

68DBUS_EXPORT

69dbus_bool_t dbus_pending_call_set_data (DBusPendingCall \*pending,

70 dbus_int32_t slot,

71 void \*data,

72 DBusFreeFunction free_data_func);

73DBUS_EXPORT

74void\* dbus_pending_call_get_data (DBusPendingCall \*pending,

75 dbus_int32_t slot);

76

89static inline void

90dbus_clear_pending_call (DBusPendingCall \*\*pointer_to_pending_call)

91{

92 \_dbus_clear_pointer_impl (DBusPendingCall, pointer_to_pending_call,

93 dbus_pending_call_unref);

94}

95

98DBUS_END_DECLS

99

100\#endif /\* DBUS_PENDING_CALL_H \*/

DBusPendingCallNotifyFunction

void(\* DBusPendingCallNotifyFunction)(DBusPendingCall \*pending, void \*user_data)

Called when a pending call now has a reply available.

**Definition** dbus-connection.h:165

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

dbus_pending_call_set_notify

dbus_bool_t dbus_pending_call_set_notify(DBusPendingCall \*pending, DBusPendingCallNotifyFunction function, void \*user_data, DBusFreeFunction free_user_data)

Sets a notification function to be called when the reply is received or the pending call times out.

**Definition** dbus-pending-call.c:651

dbus_pending_call_free_data_slot

void dbus_pending_call_free_data_slot(dbus_int32_t \*slot_p)

Deallocates a global ID for DBusPendingCall data slots.

**Definition** dbus-pending-call.c:808

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

DBusMessage

Internals of DBusMessage.

**Definition** dbus-message-private.h:102

DBusPendingCall

Implementation details of DBusPendingCall - all fields are private.

**Definition** dbus-pending-call.c:65
