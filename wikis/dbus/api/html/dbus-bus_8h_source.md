dbus-bus.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-bus.h Convenience functions for communicating with the bus.

3 \*

4 \* Copyright (C) 2003 CodeFactory AB

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

29\#ifndef DBUS_BUS_H

30\#define DBUS_BUS_H

31

32\#include \<dbus/dbus-connection.h\>

33

34DBUS_BEGIN_DECLS

35

41DBUS_EXPORT

42DBusConnection \*dbus_bus_get (DBusBusType type,

43 DBusError \*error);

44DBUS_EXPORT

45DBusConnection \*dbus_bus_get_private (DBusBusType type,

46 DBusError \*error);

47

48DBUS_EXPORT

49dbus_bool_t dbus_bus_register (DBusConnection \*connection,

50 DBusError \*error);

51DBUS_EXPORT

52dbus_bool_t dbus_bus_set_unique_name (DBusConnection \*connection,

53 const char \*unique_name);

54DBUS_EXPORT

55const char\* dbus_bus_get_unique_name (DBusConnection \*connection);

56DBUS_EXPORT

57unsigned long dbus_bus_get_unix_user (DBusConnection \*connection,

58 const char \*name,

59 DBusError \*error);

60DBUS_EXPORT

61char\* dbus_bus_get_id (DBusConnection \*connection,

62 DBusError \*error);

63DBUS_EXPORT

64int dbus_bus_request_name (DBusConnection \*connection,

65 const char \*name,

66 unsigned int flags,

67 DBusError \*error);

68DBUS_EXPORT

69int dbus_bus_release_name (DBusConnection \*connection,

70 const char \*name,

71 DBusError \*error);

72DBUS_EXPORT

73dbus_bool_t dbus_bus_name_has_owner (DBusConnection \*connection,

74 const char \*name,

75 DBusError \*error);

76

77DBUS_EXPORT

78dbus_bool_t dbus_bus_start_service_by_name (DBusConnection \*connection,

79 const char \*name,

80 dbus_uint32_t flags,

81 dbus_uint32_t \*reply,

82 DBusError \*error);

83

84DBUS_EXPORT

85void dbus_bus_add_match (DBusConnection \*connection,

86 const char \*rule,

87 DBusError \*error);

88DBUS_EXPORT

89void dbus_bus_remove_match (DBusConnection \*connection,

90 const char \*rule,

91 DBusError \*error);

92

95DBUS_END_DECLS

96

97\#endif /\* DBUS_BUS_H \*/

dbus_bus_set_unique_name

dbus_bool_t dbus_bus_set_unique_name(DBusConnection \*connection, const char \*unique_name)

Sets the unique name of the connection, as assigned by the message bus.

**Definition** dbus-bus.c:769

dbus_bus_register

dbus_bool_t dbus_bus_register(DBusConnection \*connection, DBusError \*error)

Registers a connection with the bus.

**Definition** dbus-bus.c:649

dbus_bus_get_id

char \* dbus_bus_get_id(DBusConnection \*connection, DBusError \*error)

Asks the bus to return its globally unique ID, as described in the D-Bus specification.

**Definition** dbus-bus.c:951

dbus_bus_get_unix_user

unsigned long dbus_bus_get_unix_user(DBusConnection \*connection, const char \*name, DBusError \*error)

Asks the bus to return the UID the named connection authenticated as, if any.

**Definition** dbus-bus.c:868

dbus_bus_add_match

void dbus_bus_add_match(DBusConnection \*connection, const char \*rule, DBusError \*error)

Adds a match rule to match messages going through the message bus.

**Definition** dbus-bus.c:1529

dbus_bus_name_has_owner

dbus_bool_t dbus_bus_name_has_owner(DBusConnection \*connection, const char \*name, DBusError \*error)

Asks the bus whether a certain name has an owner.

**Definition** dbus-bus.c:1283

dbus_bus_remove_match

void dbus_bus_remove_match(DBusConnection \*connection, const char \*rule, DBusError \*error)

Removes a previously-added match rule "by value" (the most recently-added identical rule gets removed...

**Definition** dbus-bus.c:1579

dbus_bus_get

DBusConnection \* dbus_bus_get(DBusBusType type, DBusError \*error)

Connects to a bus daemon and registers the client with it.

**Definition** dbus-bus.c:561

dbus_bus_start_service_by_name

dbus_bool_t dbus_bus_start_service_by_name(DBusConnection \*connection, const char \*name, dbus_uint32_t flags, dbus_uint32_t \*result, DBusError \*error)

Starts a service that will request ownership of the given name.

**Definition** dbus-bus.c:1359

dbus_bus_request_name

int dbus_bus_request_name(DBusConnection \*connection, const char \*name, unsigned int flags, DBusError \*error)

Asks the bus to assign the given name to this connection by invoking the RequestName method on the bu...

**Definition** dbus-bus.c:1115

dbus_bus_get_unique_name

const char \* dbus_bus_get_unique_name(DBusConnection \*connection)

Gets the unique name of the connection as assigned by the message bus.

**Definition** dbus-bus.c:818

dbus_bus_get_private

DBusConnection \* dbus_bus_get_private(DBusBusType type, DBusError \*error)

Connects to a bus daemon and registers the client with it as with dbus_bus_register().

**Definition** dbus-bus.c:593

dbus_bus_release_name

int dbus_bus_release_name(DBusConnection \*connection, const char \*name, DBusError \*error)

Asks the bus to unassign the given name from this connection by invoking the ReleaseName method on th...

**Definition** dbus-bus.c:1201

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

DBusBusType

DBusBusType

Well-known bus types.

**Definition** dbus-shared.h:59

DBusConnection

Implementation details of DBusConnection.

**Definition** dbus-connection.c:259

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51
