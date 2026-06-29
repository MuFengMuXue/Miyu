dbus-transport.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-transport.h DBusTransport object (internal to D-BUS implementation)

3 \*

4 \* Copyright (C) 2002, 2004 Red Hat Inc.

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

25\#ifndef DBUS_TRANSPORT_H

26\#define DBUS_TRANSPORT_H

27

28\#include \<dbus/dbus-internals.h\>

29\#include \<dbus/dbus-connection.h\>

30\#include \<dbus/dbus-credentials.h\>

31\#include \<dbus/dbus-protocol.h\>

32\#include \<dbus/dbus-address.h\>

33

34DBUS_BEGIN_DECLS

35

36typedef struct DBusTransport DBusTransport;

37

38DBusTransport\* \_dbus_transport_open (DBusAddressEntry \*entry,

39 DBusError \*error);

40DBusTransport\* \_dbus_transport_ref (DBusTransport \*transport);

41void \_dbus_transport_unref (DBusTransport \*transport);

42void \_dbus_transport_disconnect (DBusTransport \*transport);

43dbus_bool_t \_dbus_transport_get_is_connected (DBusTransport \*transport);

44dbus_bool_t \_dbus_transport_peek_is_authenticated (DBusTransport \*transport);

45dbus_bool_t \_dbus_transport_try_to_authenticate (DBusTransport \*transport);

46dbus_bool_t \_dbus_transport_get_is_anonymous (DBusTransport \*transport);

47dbus_bool_t \_dbus_transport_can_pass_unix_fd (DBusTransport \*transport);

48

49const char\* \_dbus_transport_get_address (DBusTransport \*transport);

50const char\* \_dbus_transport_get_server_id (DBusTransport \*transport);

51dbus_bool_t \_dbus_transport_handle_watch (DBusTransport \*transport,

52 DBusWatch \*watch,

53 unsigned int condition);

54dbus_bool_t \_dbus_transport_set_connection (DBusTransport \*transport,

55 DBusConnection \*connection);

56void \_dbus_transport_do_iteration (DBusTransport \*transport,

57 unsigned int flags,

58 int timeout_milliseconds);

59DBusDispatchStatus \_dbus_transport_get_dispatch_status (DBusTransport \*transport);

60dbus_bool_t \_dbus_transport_queue_messages (DBusTransport \*transport);

61

62void \_dbus_transport_set_max_message_size (DBusTransport \*transport,

63 long size);

64long \_dbus_transport_get_max_message_size (DBusTransport \*transport);

65void \_dbus_transport_set_max_received_size (DBusTransport \*transport,

66 long size);

67long \_dbus_transport_get_max_received_size (DBusTransport \*transport);

68

69void \_dbus_transport_set_max_message_unix_fds (DBusTransport \*transport,

70 long n);

71long \_dbus_transport_get_max_message_unix_fds (DBusTransport \*transport);

72void \_dbus_transport_set_max_received_unix_fds(DBusTransport \*transport,

73 long n);

74long \_dbus_transport_get_max_received_unix_fds(DBusTransport \*transport);

75

76dbus_bool_t \_dbus_transport_get_socket_fd (DBusTransport \*transport,

77 DBusSocket \*fd_p);

78dbus_bool_t \_dbus_transport_get_unix_user (DBusTransport \*transport,

79 unsigned long \*uid);

80dbus_bool_t \_dbus_transport_get_unix_process_id (DBusTransport \*transport,

81 unsigned long \*pid);

82dbus_bool_t \_dbus_transport_get_adt_audit_session_data (DBusTransport \*transport,

83 void \*\*data,

84 int \*data_size);

85void \_dbus_transport_set_unix_user_function (DBusTransport \*transport,

86 DBusAllowUnixUserFunction function,

87 void \*data,

88 DBusFreeFunction free_data_function,

89 void \*\*old_data,

90 DBusFreeFunction \*old_free_data_function);

91dbus_bool_t \_dbus_transport_get_windows_user (DBusTransport \*transport,

92 char \*\*windows_sid_p);

93dbus_bool_t \_dbus_transport_get_linux_security_label (DBusTransport \*transport,

94 char \*\*label_p);

95DBusCredentials \*\_dbus_transport_get_credentials (DBusTransport \*transport);

96

97void \_dbus_transport_set_windows_user_function (DBusTransport \*transport,

98 DBusAllowWindowsUserFunction function,

99 void \*data,

100 DBusFreeFunction free_data_function,

101 void \*\*old_data,

102 DBusFreeFunction \*old_free_data_function);

103dbus_bool_t \_dbus_transport_set_auth_mechanisms (DBusTransport \*transport,

104 const char \*\*mechanisms);

105void \_dbus_transport_set_allow_anonymous (DBusTransport \*transport,

106 dbus_bool_t value);

107int \_dbus_transport_get_pending_fds_count (DBusTransport \*transport);

108void \_dbus_transport_set_pending_fds_function (DBusTransport \*transport,

109 void (\* callback) (void \*),

110 void \*data);

111

112/\* if DBUS_ENABLE_STATS \*/

113void \_dbus_transport_get_stats (DBusTransport \*transport,

114 dbus_uint32_t \*queue_bytes,

115 dbus_uint32_t \*queue_fds,

116 dbus_uint32_t \*peak_queue_bytes,

117 dbus_uint32_t \*peak_queue_fds);

118

119DBUS_END_DECLS

120

121\#endif /\* DBUS_TRANSPORT_H \*/

DBusAllowUnixUserFunction

dbus_bool_t(\* DBusAllowUnixUserFunction)(DBusConnection \*connection, unsigned long uid, void \*data)

Called during authentication to check whether the given UNIX user ID is allowed to connect,...

**Definition** dbus-connection.h:146

DBusDispatchStatus

DBusDispatchStatus

Indicates the status of incoming data on a DBusConnection.

**Definition** dbus-connection.h:83

DBusAllowWindowsUserFunction

dbus_bool_t(\* DBusAllowWindowsUserFunction)(DBusConnection \*connection, const char \*user_sid, void \*data)

Called during authentication to check whether the given Windows user ID is allowed to connect,...

**Definition** dbus-connection.h:156

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

\_dbus_transport_set_auth_mechanisms

dbus_bool_t \_dbus_transport_set_auth_mechanisms(DBusTransport \*transport, const char \*\*mechanisms)

Sets the SASL authentication mechanisms supported by this transport.

**Definition** dbus-transport.c:1565

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

DBusAddressEntry

Internals of DBusAddressEntry.

**Definition** dbus-address.c:49

DBusConnection

Implementation details of DBusConnection.

**Definition** dbus-connection.c:259

DBusCredentials

**Definition** dbus-credentials.c:60

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusSocket

Socket interface.

**Definition** dbus-sysdeps.h:185

DBusTransport

Object representing a transport such as a socket.

**Definition** dbus-transport-protected.h:83

DBusTransport::connection

DBusConnection \* connection

Connection owning this transport.

**Definition** dbus-transport-protected.h:88

DBusWatch

Implementation of DBusWatch.

**Definition** dbus-watch.c:43
