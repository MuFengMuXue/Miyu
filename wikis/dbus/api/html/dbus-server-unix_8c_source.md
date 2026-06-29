dbus-server-unix.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-server-unix.c Server implementation for Unix network protocols.

3 \*

4 \* Copyright (C) 2002, 2003, 2004 Red Hat Inc.

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

28\#include "dbus-server-socket.h"

29\#include "dbus-server-launchd.h"

30\#include "dbus-transport-unix.h"

31\#include "dbus-connection-internal.h"

32\#include "dbus-sysdeps-unix.h"

33\#include "dbus-string.h"

34

54DBusServerListenResult

55\_dbus_server_listen_platform_specific (DBusAddressEntry \*entry,

56 DBusServer \*\*server_p,

57 DBusError \*error)

58{

59 const char \*method;

60

61 \*server_p = NULL;

62

63 method = dbus_address_entry_get_method (entry);

64 if (strcmp (method, "systemd") == 0)

65 {

66 int i, n;

67 DBusSocket \*fds;

68 DBusString address;

69

70 n = \_dbus_listen_systemd_sockets (&fds, error);

71 if (n \< 0)

72 {

73 \_DBUS_ASSERT_ERROR_IS_SET (error);

74 return DBUS_SERVER_LISTEN_DID_NOT_CONNECT;

75 }

76

77 if (!\_dbus_string_init (&address))

78 goto systemd_oom;

79

80 for (i = 0; i \< n; i++)

81 {

82 if (i \> 0)

83 {

84 if (!\_dbus_string_append (&address, ";"))

85 goto systemd_oom;

86 }

87 if (!\_dbus_append_address_from_socket (fds\[i\], &address, error))

88 goto systemd_err;

89 }

90

91 \*server_p = \_dbus_server_new_for_socket (fds, n, &address, NULL, error);

92 if (\*server_p == NULL)

93 goto systemd_err;

94

95 dbus_free (fds);

96 \_dbus_string_free (&address);

97

98 return DBUS_SERVER_LISTEN_OK;

99

100 systemd_oom:

101 \_DBUS_SET_OOM (error);

102 systemd_err:

103 for (i = 0; i \< n; i++)

104 {

105 \_dbus_close_socket (&fds\[i\], NULL);

106 }

107 dbus_free (fds);

108 \_dbus_string_free (&address);

109

110 return DBUS_SERVER_LISTEN_DID_NOT_CONNECT;

111 }

112\#ifdef DBUS_ENABLE_LAUNCHD

113 else if (strcmp (method, "launchd") == 0)

114 {

115 const char \*launchd_env_var = dbus_address_entry_get_value (entry, "env");

116 if (launchd_env_var == NULL)

117 {

118 \_dbus_set_bad_address (error, "launchd", "env", NULL);

119 return DBUS_SERVER_LISTEN_DID_NOT_CONNECT;

120 }

121 \*server_p = \_dbus_server_new_for_launchd (launchd_env_var, error);

122

123 if (\*server_p != NULL)

124 {

125 \_DBUS_ASSERT_ERROR_IS_CLEAR(error);

126 return DBUS_SERVER_LISTEN_OK;

127 }

128 else

129 {

130 \_DBUS_ASSERT_ERROR_IS_SET(error);

131 return DBUS_SERVER_LISTEN_DID_NOT_CONNECT;

132 }

133 }

134\#endif

135 else

136 {

137 /\* If we don't handle the method, we return NULL with the

138 \* error unset

139 \*/

140 \_DBUS_ASSERT_ERROR_IS_CLEAR(error);

141 return DBUS_SERVER_LISTEN_NOT_HANDLED;

142 }

143}

144

\_dbus_set_bad_address

void \_dbus_set_bad_address(DBusError \*error, const char \*address_problem_type, const char \*address_problem_field, const char \*address_problem_other)

Sets DBUS_ERROR_BAD_ADDRESS.

**Definition** dbus-address.c:70

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

dbus_free

void dbus_free(void \*memory)

Frees a block of memory previously allocated by dbus_malloc() or dbus_malloc0().

**Definition** dbus-memory.c:710

\_dbus_server_new_for_launchd

DBusServer \* \_dbus_server_new_for_launchd(const char \*launchd_env_var, DBusError \*error)

Creates a new server from launchd.

**Definition** dbus-server-launchd.c:68

\_dbus_server_new_for_socket

DBusServer \* \_dbus_server_new_for_socket(DBusSocket \*fds, int n_fds, const DBusString \*address, DBusNonceFile \*noncefile, DBusError \*error)

Creates a new server listening on the given file descriptor.

**Definition** dbus-server-socket.c:288

\_dbus_server_listen_platform_specific

DBusServerListenResult \_dbus_server_listen_platform_specific(DBusAddressEntry \*entry, DBusServer \*\*server_p, DBusError \*error)

Tries to interpret the address entry in a platform-specific way, creating a platform-specific server ...

**Definition** dbus-server-unix.c:55

\_dbus_string_append

dbus_bool_t \_dbus_string_append(DBusString \*str, const char \*buffer)

Appends a nul-terminated C-style string to a DBusString.

**Definition** dbus-string.c:980

\_dbus_string_init

dbus_bool_t \_dbus_string_init(DBusString \*str)

Initializes a string.

**Definition** dbus-string.c:182

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_listen_systemd_sockets

int \_dbus_listen_systemd_sockets(DBusSocket \*\*fds, DBusError \*error)

Acquires one or more sockets passed in from systemd.

**Definition** dbus-sysdeps-unix.c:1299

\_dbus_append_address_from_socket

dbus_bool_t \_dbus_append_address_from_socket(DBusSocket fd, DBusString \*address, DBusError \*error)

Read the address from the socket and append it to the string.

**Definition** dbus-sysdeps-unix.c:5055

\_dbus_close_socket

dbus_bool_t \_dbus_close_socket(DBusSocket \*fd, DBusError \*error)

Closes a socket and invalidates it.

**Definition** dbus-sysdeps-unix.c:314

DBusAddressEntry

Internals of DBusAddressEntry.

**Definition** dbus-address.c:49

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusServer

Internals of DBusServer object.

**Definition** dbus-server-protected.h:59

DBusSocket

Socket interface.

**Definition** dbus-sysdeps.h:185

DBusString

**Definition** dbus-string.h:47
