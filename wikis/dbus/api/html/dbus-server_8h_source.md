dbus-server.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-server.h DBusServer object

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

29\#ifndef DBUS_SERVER_H

30\#define DBUS_SERVER_H

31

32\#include \<dbus/dbus-errors.h\>

33\#include \<dbus/dbus-macros.h\>

34\#include \<dbus/dbus-message.h\>

35\#include \<dbus/dbus-connection.h\>

36\#include \<dbus/dbus-protocol.h\>

37

38DBUS_BEGIN_DECLS

39

45typedef struct DBusServer DBusServer;

46

50typedef void (\* DBusNewConnectionFunction) (DBusServer \*server,

51 DBusConnection \*new_connection,

52 void \*data);

53

54DBUS_EXPORT

55DBusServer\* dbus_server_listen (const char \*address,

56 DBusError \*error);

57DBUS_EXPORT

58DBusServer\* dbus_server_ref (DBusServer \*server);

59DBUS_EXPORT

60void dbus_server_unref (DBusServer \*server);

61DBUS_EXPORT

62void dbus_server_disconnect (DBusServer \*server);

63DBUS_EXPORT

64dbus_bool_t dbus_server_get_is_connected (DBusServer \*server);

65DBUS_EXPORT

66char\* dbus_server_get_address (DBusServer \*server);

67DBUS_EXPORT

68char\* dbus_server_get_id (DBusServer \*server);

69DBUS_EXPORT

70void dbus_server_set_new_connection_function (DBusServer \*server,

71 DBusNewConnectionFunction function,

72 void \*data,

73 DBusFreeFunction free_data_function);

74DBUS_EXPORT

75dbus_bool_t dbus_server_set_watch_functions (DBusServer \*server,

76 DBusAddWatchFunction add_function,

77 DBusRemoveWatchFunction remove_function,

78 DBusWatchToggledFunction toggled_function,

79 void \*data,

80 DBusFreeFunction free_data_function);

81DBUS_EXPORT

82dbus_bool_t dbus_server_set_timeout_functions (DBusServer \*server,

83 DBusAddTimeoutFunction add_function,

84 DBusRemoveTimeoutFunction remove_function,

85 DBusTimeoutToggledFunction toggled_function,

86 void \*data,

87 DBusFreeFunction free_data_function);

88DBUS_EXPORT

89dbus_bool_t dbus_server_set_auth_mechanisms (DBusServer \*server,

90 const char \*\*mechanisms);

91

92DBUS_EXPORT

93dbus_bool_t dbus_server_allocate_data_slot (dbus_int32_t \*slot_p);

94DBUS_EXPORT

95void dbus_server_free_data_slot (dbus_int32_t \*slot_p);

96DBUS_EXPORT

97dbus_bool_t dbus_server_set_data (DBusServer \*server,

98 int slot,

99 void \*data,

100 DBusFreeFunction free_data_func);

101DBUS_EXPORT

102void\* dbus_server_get_data (DBusServer \*server,

103 int slot);

104

117static inline void

118dbus_clear_server (DBusServer \*\*pointer_to_server)

119{

120 \_dbus_clear_pointer_impl (DBusServer, pointer_to_server, dbus_server_unref);

121}

122

125DBUS_END_DECLS

126

127\#endif /\* DBUS_SERVER_H \*/

DBusWatchToggledFunction

void(\* DBusWatchToggledFunction)(DBusWatch \*watch, void \*data)

Called when dbus_watch_get_enabled() may return a different value than it did before.

**Definition** dbus-connection.h:100

DBusAddWatchFunction

dbus_bool_t(\* DBusAddWatchFunction)(DBusWatch \*watch, void \*data)

Called when libdbus needs a new watch to be monitored by the main loop.

**Definition** dbus-connection.h:94

DBusTimeoutToggledFunction

void(\* DBusTimeoutToggledFunction)(DBusTimeout \*timeout, void \*data)

Called when dbus_timeout_get_enabled() may return a different value than it did before.

**Definition** dbus-connection.h:120

DBusAddTimeoutFunction

dbus_bool_t(\* DBusAddTimeoutFunction)(DBusTimeout \*timeout, void \*data)

Called when libdbus needs a new timeout to be monitored by the main loop.

**Definition** dbus-connection.h:113

DBusRemoveWatchFunction

void(\* DBusRemoveWatchFunction)(DBusWatch \*watch, void \*data)

Called when libdbus no longer needs a watch to be monitored by the main loop.

**Definition** dbus-connection.h:106

DBusRemoveTimeoutFunction

void(\* DBusRemoveTimeoutFunction)(DBusTimeout \*timeout, void \*data)

Called when libdbus no longer needs a timeout to be monitored by the main loop.

**Definition** dbus-connection.h:126

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

dbus_server_allocate_data_slot

dbus_bool_t dbus_server_allocate_data_slot(dbus_int32_t \*slot_p)

Allocates an integer ID to be used for storing application-specific data on any DBusServer.

**Definition** dbus-server.c:1100

dbus_server_disconnect

void dbus_server_disconnect(DBusServer \*server)

Releases the server's address and stops listening for new clients.

**Definition** dbus-server.c:798

dbus_server_set_auth_mechanisms

dbus_bool_t dbus_server_set_auth_mechanisms(DBusServer \*server, const char \*\*mechanisms)

Sets the authentication mechanisms that this server offers to clients, as a NULL-terminated array of ...

**Definition** dbus-server.c:1053

dbus_server_get_id

char \* dbus_server_get_id(DBusServer \*server)

Returns the unique ID of the server, as a newly-allocated string which must be freed by the caller.

**Definition** dbus-server.c:874

dbus_server_listen

DBusServer \* dbus_server_listen(const char \*address, DBusError \*error)

Listens for new connections on the given address.

**Definition** dbus-server.c:559

dbus_server_get_address

char \* dbus_server_get_address(DBusServer \*server)

Returns the address of the server, as a newly-allocated string which must be freed by the caller.

**Definition** dbus-server.c:838

dbus_server_get_is_connected

dbus_bool_t dbus_server_get_is_connected(DBusServer \*server)

Returns TRUE if the server is still listening for new connections.

**Definition** dbus-server.c:817

dbus_server_unref

void dbus_server_unref(DBusServer \*server)

Decrements the reference count of a DBusServer.

**Definition** dbus-server.c:735

dbus_server_set_new_connection_function

void dbus_server_set_new_connection_function(DBusServer \*server, DBusNewConnectionFunction function, void \*data, DBusFreeFunction free_data_function)

Sets a function to be used for handling new connections.

**Definition** dbus-server.c:909

dbus_server_set_watch_functions

dbus_bool_t dbus_server_set_watch_functions(DBusServer \*server, DBusAddWatchFunction add_function, DBusRemoveWatchFunction remove_function, DBusWatchToggledFunction toggled_function, void \*data, DBusFreeFunction free_data_function)

Sets the watch functions for the server.

**Definition** dbus-server.c:949

dbus_server_set_data

dbus_bool_t dbus_server_set_data(DBusServer \*server, int slot, void \*data, DBusFreeFunction free_data_func)

Stores a pointer on a DBusServer, along with an optional function to be used for freeing the data whe...

**Definition** dbus-server.c:1139

dbus_server_ref

DBusServer \* dbus_server_ref(DBusServer \*server)

Increments the reference count of a DBusServer.

**Definition** dbus-server.c:703

dbus_server_get_data

void \* dbus_server_get_data(DBusServer \*server, int slot)

Retrieves data previously set with dbus_server_set_data().

**Definition** dbus-server.c:1179

dbus_server_free_data_slot

void dbus_server_free_data_slot(dbus_int32_t \*slot_p)

Deallocates a global ID for server data slots.

**Definition** dbus-server.c:1118

dbus_server_set_timeout_functions

dbus_bool_t dbus_server_set_timeout_functions(DBusServer \*server, DBusAddTimeoutFunction add_function, DBusRemoveTimeoutFunction remove_function, DBusTimeoutToggledFunction toggled_function, void \*data, DBusFreeFunction free_data_function)

Sets the timeout functions for the server.

**Definition** dbus-server.c:1002

DBusNewConnectionFunction

void(\* DBusNewConnectionFunction)(DBusServer \*server, DBusConnection \*new_connection, void \*data)

Called when a new connection to the server is available.

**Definition** dbus-server.h:50

DBusConnection

Implementation details of DBusConnection.

**Definition** dbus-connection.c:259

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusServer

Internals of DBusServer object.

**Definition** dbus-server-protected.h:59

DBusServer::address

char \* address

Address this server is listening on.

**Definition** dbus-server-protected.h:71
