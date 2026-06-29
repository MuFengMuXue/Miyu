dbus-server-win.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-server-win.c Server implementation for WIN network protocols.

3 \*

4 \* Copyright (C) 2002, 2003, 2004 Red Hat Inc.

5 \* Copyright (C) 2007 Ralf Habacker \<ralf.habacker@freenet.de\>

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

28\#include "dbus-internals.h"

29\#include "dbus-server-win.h"

30\#include "dbus-server-socket.h"

31

51DBusServerListenResult

52\_dbus_server_listen_platform_specific (DBusAddressEntry \*entry,

53 DBusServer \*\*server_p,

54 DBusError \*error)

55{

56 const char \*method;

57

58 \*server_p = NULL;

59

60 method = dbus_address_entry_get_method (entry);

61

62 if (strcmp (method, "autolaunch") == 0)

63 {

64 const char \*host = "localhost";

65 const char \*bind = "localhost";

66 const char \*port = "0";

67 const char \*family = "ipv4";

68 const char \*scope = dbus_address_entry_get_value (entry, "scope");

69

70 if (\_dbus_daemon_is_session_bus_address_published (scope))

71 return DBUS_SERVER_LISTEN_ADDRESS_ALREADY_USED;

72

73 \*server_p = \_dbus_server_new_for_tcp_socket (host, bind, port,

74 family, error, FALSE);

75 if (\*server_p)

76 {

77 \_DBUS_ASSERT_ERROR_IS_CLEAR(error);

78 (\*server_p)-\>published_address =

79 \_dbus_daemon_publish_session_bus_address ((\*server_p)-\>address, scope);

80 return DBUS_SERVER_LISTEN_OK;

81 }

82 else

83 {

84 // make sure no handle is open

85 \_dbus_daemon_unpublish_session_bus_address ();

86 \_DBUS_ASSERT_ERROR_IS_SET(error);

87 return DBUS_SERVER_LISTEN_DID_NOT_CONNECT;

88 }

89 }

90 else

91 {

92 \_DBUS_ASSERT_ERROR_IS_CLEAR(error);

93 return DBUS_SERVER_LISTEN_NOT_HANDLED;

94 }

95}

96

dbus_address_entry_get_method

const char \* dbus_address_entry_get_method(DBusAddressEntry \*entry)

Returns the method string of an address entry.

**Definition** dbus-address.c:232

dbus_address_entry_get_value

const char \* dbus_address_entry_get_value(DBusAddressEntry \*entry, const char \*key)

Returns a value from a key of an entry.

**Definition** dbus-address.c:249

NULL

\#define NULL

A null pointer, defined appropriately for C or C++.

**Definition** dbus-macros.h:51

FALSE

\#define FALSE

Expands to "0".

**Definition** dbus-macros.h:44

\_dbus_server_new_for_tcp_socket

DBusServer \* \_dbus_server_new_for_tcp_socket(const char \*host, const char \*bind, const char \*port, const char \*family, DBusError \*error, dbus_bool_t use_nonce)

Creates a new server listening on TCP.

**Definition** dbus-server-socket.c:420

\_dbus_server_listen_platform_specific

DBusServerListenResult \_dbus_server_listen_platform_specific(DBusAddressEntry \*entry, DBusServer \*\*server_p, DBusError \*error)

Tries to interpret the address entry in a platform-specific way, creating a platform-specific server ...

**Definition** dbus-server-win.c:52

DBusAddressEntry

Internals of DBusAddressEntry.

**Definition** dbus-address.c:49

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusServer

Internals of DBusServer object.

**Definition** dbus-server-protected.h:59
