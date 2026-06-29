dbus-connection-internal.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-connection-internal.h DBusConnection internal interfaces

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

25\#ifndef DBUS_CONNECTION_INTERNAL_H

26\#define DBUS_CONNECTION_INTERNAL_H

27

28\#include \<dbus/dbus-internals.h\>

29\#include \<dbus/dbus-connection.h\>

30\#include \<dbus/dbus-credentials.h\>

31\#include \<dbus/dbus-message.h\>

32\#include \<dbus/dbus-transport.h\>

33\#include \<dbus/dbus-resources.h\>

34\#include \<dbus/dbus-list.h\>

35\#include \<dbus/dbus-timeout.h\>

36\#include \<dbus/dbus-dataslot.h\>

37

38DBUS_BEGIN_DECLS

39

40typedef enum

41{

42 DBUS_ITERATION_DO_WRITING = 1 \<\< 0,

43 DBUS_ITERATION_DO_READING = 1 \<\< 1,

44 DBUS_ITERATION_BLOCK = 1 \<\< 2

45} DBusIterationFlags;

46

48\#define \_DBUS_DEFAULT_TIMEOUT_VALUE (25 \* 1000)

49

50typedef void (\* DBusPendingFdsChangeFunction) (void \*data);

51

52DBUS_PRIVATE_EXPORT

53void \_dbus_connection_lock (DBusConnection \*connection);

54DBUS_PRIVATE_EXPORT

55void \_dbus_connection_unlock (DBusConnection \*connection);

56DBUS_PRIVATE_EXPORT

57DBusConnection \* \_dbus_connection_ref_unlocked (DBusConnection \*connection);

58DBUS_PRIVATE_EXPORT

59void \_dbus_connection_unref_unlocked (DBusConnection \*connection);

60DBUS_PRIVATE_EXPORT

61dbus_uint32_t \_dbus_connection_get_next_client_serial (DBusConnection \*connection);

62void \_dbus_connection_queue_received_message_link (DBusConnection \*connection,

63 DBusList \*link);

64dbus_bool_t \_dbus_connection_has_messages_to_send_unlocked (DBusConnection \*connection);

65DBusMessage\* \_dbus_connection_get_message_to_send (DBusConnection \*connection);

66void \_dbus_connection_message_sent_unlocked (DBusConnection \*connection,

67 DBusMessage \*message);

68dbus_bool_t \_dbus_connection_add_watch_unlocked (DBusConnection \*connection,

69 DBusWatch \*watch);

70void \_dbus_connection_remove_watch_unlocked (DBusConnection \*connection,

71 DBusWatch \*watch);

72void \_dbus_connection_toggle_watch_unlocked (DBusConnection \*connection,

73 DBusWatch \*watch,

74 dbus_bool_t enabled);

75dbus_bool_t \_dbus_connection_handle_watch (DBusWatch \*watch,

76 unsigned int condition,

77 void \*data);

78dbus_bool_t \_dbus_connection_add_timeout_unlocked (DBusConnection \*connection,

79 DBusTimeout \*timeout);

80void \_dbus_connection_remove_timeout_unlocked (DBusConnection \*connection,

81 DBusTimeout \*timeout);

82void \_dbus_connection_toggle_timeout_unlocked (DBusConnection \*connection,

83 DBusTimeout \*timeout,

84 dbus_bool_t enabled);

85DBusConnection\* \_dbus_connection_new_for_transport (DBusTransport \*transport);

86void \_dbus_connection_do_iteration_unlocked (DBusConnection \*connection,

87 DBusPendingCall \*pending,

88 unsigned int flags,

89 int timeout_milliseconds);

90void \_dbus_connection_close_possibly_shared (DBusConnection \*connection);

91void \_dbus_connection_close_if_only_one_ref (DBusConnection \*connection);

92

93DBusPendingCall\* \_dbus_pending_call_new (DBusConnection \*connection,

94 int timeout_milliseconds,

95 DBusTimeoutHandler timeout_handler);

96void \_dbus_pending_call_notify (DBusPendingCall \*pending);

97void \_dbus_connection_remove_pending_call (DBusConnection \*connection,

98 DBusPendingCall \*pending);

99void \_dbus_connection_block_pending_call (DBusPendingCall \*pending);

100void \_dbus_pending_call_complete_and_unlock (DBusPendingCall \*pending,

101 DBusMessage \*message);

102dbus_bool_t \_dbus_connection_send_and_unlock (DBusConnection \*connection,

103 DBusMessage \*message,

104 dbus_uint32_t \*client_serial);

105

106void \_dbus_connection_queue_synthesized_message_link (DBusConnection \*connection,

107 DBusList \*link);

108DBUS_PRIVATE_EXPORT

109void \_dbus_connection_test_get_locks (DBusConnection \*conn,

110 DBusMutex \*\*mutex_loc,

111 DBusMutex \*\*dispatch_mutex_loc,

112 DBusMutex \*\*io_path_mutex_loc,

113 DBusCondVar \*\*dispatch_cond_loc,

114 DBusCondVar \*\*io_path_cond_loc);

115DBUS_PRIVATE_EXPORT

116int \_dbus_connection_get_pending_fds_count (DBusConnection \*connection);

117DBUS_PRIVATE_EXPORT

118void \_dbus_connection_set_pending_fds_function (DBusConnection \*connection,

119 DBusPendingFdsChangeFunction callback,

120 void \*data);

121

122DBUS_PRIVATE_EXPORT

123dbus_bool_t \_dbus_connection_get_linux_security_label (DBusConnection \*connection,

124 char \*\*label_p);

125DBUS_PRIVATE_EXPORT

126DBusCredentials \*\_dbus_connection_get_credentials (DBusConnection \*connection);

127

128/\* if DBUS_ENABLE_STATS \*/

129DBUS_PRIVATE_EXPORT

130void \_dbus_connection_get_stats (DBusConnection \*connection,

131 dbus_uint32_t \*in_messages,

132 dbus_uint32_t \*in_bytes,

133 dbus_uint32_t \*in_fds,

134 dbus_uint32_t \*in_peak_bytes,

135 dbus_uint32_t \*in_peak_fds,

136 dbus_uint32_t \*out_messages,

137 dbus_uint32_t \*out_bytes,

138 dbus_uint32_t \*out_fds,

139 dbus_uint32_t \*out_peak_bytes,

140 dbus_uint32_t \*out_peak_fds);

141

142

143DBUS_EMBEDDED_TESTS_EXPORT

144const char\* \_dbus_connection_get_address (DBusConnection \*connection);

145

146/\* This \_dbus_bus\_\* stuff doesn't really belong here, but dbus-bus-internal.h seems

147 \* silly for one function

148 \*/

154void \_dbus_bus_notify_shared_connection_disconnected_unlocked (DBusConnection \*connection);

155

159DBUS_END_DECLS

160

161\#endif /\* DBUS_CONNECTION_INTERNAL_H \*/

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

\_dbus_connection_unlock

DBUS_PRIVATE_EXPORT void \_dbus_connection_unlock(DBusConnection \*connection)

Releases the connection lock.

**Definition** dbus-connection.c:403

\_dbus_connection_lock

DBUS_PRIVATE_EXPORT void \_dbus_connection_lock(DBusConnection \*connection)

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

DBUS_PRIVATE_EXPORT void \_dbus_connection_unref_unlocked(DBusConnection \*connection)

Decrements the reference count of a DBusConnection.

**Definition** dbus-connection.c:1447

\_dbus_connection_get_message_to_send

DBusMessage \* \_dbus_connection_get_message_to_send(DBusConnection \*connection)

Gets the next outgoing message.

**Definition** dbus-connection.c:613

\_dbus_connection_message_sent_unlocked

void \_dbus_connection_message_sent_unlocked(DBusConnection \*connection, DBusMessage \*message)

Notifies the connection that a message has been sent, so the message can be removed from the outgoing...

**Definition** dbus-connection.c:629

\_dbus_connection_remove_timeout_unlocked

void \_dbus_connection_remove_timeout_unlocked(DBusConnection \*connection, DBusTimeout \*timeout)

Removes a timeout using the connection's DBusRemoveTimeoutFunction if available.

**Definition** dbus-connection.c:889

\_dbus_connection_get_next_client_serial

DBUS_PRIVATE_EXPORT dbus_uint32_t \_dbus_connection_get_next_client_serial(DBusConnection \*connection)

Allocate and return the next non-zero serial number for outgoing messages.

**Definition** dbus-connection.c:1474

\_dbus_connection_queue_received_message_link

void \_dbus_connection_queue_received_message_link(DBusConnection \*connection, DBusList \*link)

Adds a message-containing list link to the incoming message queue, taking ownership of the link and t...

**Definition** dbus-connection.c:484

\_dbus_connection_get_pending_fds_count

DBUS_PRIVATE_EXPORT int \_dbus_connection_get_pending_fds_count(DBusConnection \*connection)

Return how many file descriptors are pending in the loader.

**Definition** dbus-connection.c:2577

\_dbus_connection_set_pending_fds_function

DBUS_PRIVATE_EXPORT void \_dbus_connection_set_pending_fds_function(DBusConnection \*connection, DBusPendingFdsChangeFunction callback, void \*data)

Register a function to be called whenever the number of pending file descriptors in the loader change...

**Definition** dbus-connection.c:2590

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

DBUS_PRIVATE_EXPORT DBusConnection \* \_dbus_connection_ref_unlocked(DBusConnection \*connection)

Increments the reference count of a DBusConnection.

**Definition** dbus-connection.c:1424

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

DBusMutex

struct DBusMutex DBusMutex

An opaque mutex type provided by the DBusThreadFunctions implementation installed by dbus_threads_ini...

**Definition** dbus-threads.h:43

DBusTimeoutHandler

dbus_bool_t(\* DBusTimeoutHandler)(void \*data)

function to run when the timeout is handled

**Definition** dbus-timeout.h:43

DBusCondVar

**Definition** dbus-sysdeps-pthread.c:59

DBusConnection

Implementation details of DBusConnection.

**Definition** dbus-connection.c:259

DBusCredentials

**Definition** dbus-credentials.c:60

DBusList

A node in a linked list.

**Definition** dbus-list.h:37

DBusMessage

Internals of DBusMessage.

**Definition** dbus-message-private.h:102

DBusPendingCall

Implementation details of DBusPendingCall - all fields are private.

**Definition** dbus-pending-call.c:65

DBusTimeout

Internals of DBusTimeout.

**Definition** dbus-timeout.c:43

DBusTransport

Object representing a transport such as a socket.

**Definition** dbus-transport-protected.h:83

DBusWatch

Implementation of DBusWatch.

**Definition** dbus-watch.c:43
