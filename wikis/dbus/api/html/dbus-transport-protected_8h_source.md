dbus-transport-protected.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-transport-protected.h Used by subclasses of DBusTransport object (internal to D-Bus implementation)

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

25\#ifndef DBUS_TRANSPORT_PROTECTED_H

26\#define DBUS_TRANSPORT_PROTECTED_H

27

28\#include \<dbus/dbus-internals.h\>

29\#include \<dbus/dbus-errors.h\>

30\#include \<dbus/dbus-transport.h\>

31\#include \<dbus/dbus-message-internal.h\>

32\#include \<dbus/dbus-auth.h\>

33\#include \<dbus/dbus-resources.h\>

34

35DBUS_BEGIN_DECLS

36

37typedef struct DBusTransportVTable DBusTransportVTable;

38

43struct DBusTransportVTable

44{

45 void (\* finalize) (DBusTransport \*transport);

48 dbus_bool_t (\* handle_watch) (DBusTransport \*transport,

49 DBusWatch \*watch,

50 unsigned int flags);

55 void (\* disconnect) (DBusTransport \*transport);

58 dbus_bool_t (\* connection_set) (DBusTransport \*transport);

61 void (\* do_iteration) (DBusTransport \*transport,

62 unsigned int flags,

63 int timeout_milliseconds);

68 void (\* live_messages_changed) (DBusTransport \*transport);

71 dbus_bool_t (\* get_socket_fd) (DBusTransport \*transport,

72 DBusSocket \*fd_p);

74};

75

82struct DBusTransport

83{

84 int refcount;

86 const DBusTransportVTable \*vtable;

88 DBusConnection \*connection;

90 DBusMessageLoader \*loader;

92 DBusAuth \*auth;

94 DBusCredentials \*credentials;

96 long max_live_messages_size;

97 long max_live_messages_unix_fds;

99 DBusCounter \*live_messages;

101 char \*address;

103 char \*expected_guid;

105 DBusAllowUnixUserFunction unix_user_function;

106 void \*unix_user_data;

108 DBusFreeFunction free_unix_user_data;

110 DBusAllowWindowsUserFunction windows_user_function;

111 void \*windows_user_data;

113 DBusFreeFunction free_windows_user_data;

115 unsigned int disconnected : 1;

116 unsigned int authenticated : 1;

117 unsigned int send_credentials_pending : 1;

118 unsigned int receive_credentials_pending : 1;

119 unsigned int is_server : 1;

120 unsigned int unused_bytes_recovered : 1;

121 unsigned int allow_anonymous : 1;

122};

123

124dbus_bool_t \_dbus_transport_init_base (DBusTransport \*transport,

125 const DBusTransportVTable \*vtable,

126 const DBusString \*server_guid,

127 const DBusString \*address);

128void \_dbus_transport_finalize_base (DBusTransport \*transport);

129

130

131typedef enum

132{

133 DBUS_TRANSPORT_OPEN_NOT_HANDLED,

134 DBUS_TRANSPORT_OPEN_OK,

135 DBUS_TRANSPORT_OPEN_BAD_ADDRESS,

136 DBUS_TRANSPORT_OPEN_DID_NOT_CONNECT

137} DBusTransportOpenResult;

138

139DBusTransportOpenResult \_dbus_transport_open_platform_specific (DBusAddressEntry \*entry,

140 DBusTransport \*\*transport_p,

141 DBusError \*error);

142

143\#define DBUS_TRANSPORT_CAN_SEND_UNIX_FD(x) \\

144 \_dbus_auth_get_unix_fd_negotiated((x)-\>auth)

145

146DBUS_END_DECLS

147

148\#endif /\* DBUS_TRANSPORT_PROTECTED_H \*/

DBusAllowUnixUserFunction

dbus_bool_t(\* DBusAllowUnixUserFunction)(DBusConnection \*connection, unsigned long uid, void \*data)

Called during authentication to check whether the given UNIX user ID is allowed to connect,...

**Definition** dbus-connection.h:146

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

\_dbus_transport_open_platform_specific

DBusTransportOpenResult \_dbus_transport_open_platform_specific(DBusAddressEntry \*entry, DBusTransport \*\*transport_p, DBusError \*error)

Opens platform specific transport types.

**Definition** dbus-transport-unix.c:248

\_dbus_transport_init_base

dbus_bool_t \_dbus_transport_init_base(DBusTransport \*transport, const DBusTransportVTable \*vtable, const DBusString \*server_guid, const DBusString \*address)

Initializes the base class members of DBusTransport.

**Definition** dbus-transport.c:104

\_dbus_transport_finalize_base

void \_dbus_transport_finalize_base(DBusTransport \*transport)

Finalizes base class members of DBusTransport.

**Definition** dbus-transport.c:218

DBusAddressEntry

Internals of DBusAddressEntry.

**Definition** dbus-address.c:49

DBusAuth

Internal members of DBusAuth.

**Definition** dbus-auth.c:156

DBusConnection

Implementation details of DBusConnection.

**Definition** dbus-connection.c:259

DBusCounter

Internals of DBusCounter.

**Definition** dbus-resources.c:57

DBusCredentials

**Definition** dbus-credentials.c:60

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusMessageLoader

Implementation details of DBusMessageLoader.

**Definition** dbus-message-private.h:63

DBusSocket

Socket interface.

**Definition** dbus-sysdeps.h:185

DBusString

**Definition** dbus-string.h:47

DBusTransportVTable

The virtual table that must be implemented to create a new kind of transport.

**Definition** dbus-transport-protected.h:44

DBusTransportVTable::get_socket_fd

dbus_bool_t(\* get_socket_fd)(DBusTransport \*transport, DBusSocket \*fd_p)

Get socket file descriptor.

**Definition** dbus-transport-protected.h:71

DBusTransportVTable::disconnect

void(\* disconnect)(DBusTransport \*transport)

Disconnect this transport.

**Definition** dbus-transport-protected.h:55

DBusTransportVTable::live_messages_changed

void(\* live_messages_changed)(DBusTransport \*transport)

Outstanding messages counter changed.

**Definition** dbus-transport-protected.h:68

DBusTransportVTable::do_iteration

void(\* do_iteration)(DBusTransport \*transport, unsigned int flags, int timeout_milliseconds)

Called to do a single "iteration" (block on select/poll followed by reading or writing data).

**Definition** dbus-transport-protected.h:61

DBusTransportVTable::handle_watch

dbus_bool_t(\* handle_watch)(DBusTransport \*transport, DBusWatch \*watch, unsigned int flags)

The handle_watch method handles reading/writing data as indicated by the flags.

**Definition** dbus-transport-protected.h:48

DBusTransportVTable::finalize

void(\* finalize)(DBusTransport \*transport)

The finalize method must free the transport.

**Definition** dbus-transport-protected.h:45

DBusTransportVTable::connection_set

dbus_bool_t(\* connection_set)(DBusTransport \*transport)

Called when transport-\>connection has been filled in.

**Definition** dbus-transport-protected.h:58

DBusTransport

Object representing a transport such as a socket.

**Definition** dbus-transport-protected.h:83

DBusTransport::authenticated

unsigned int authenticated

Cache of auth state; use \_dbus_transport_peek_is_authenticated() to query value.

**Definition** dbus-transport-protected.h:116

DBusTransport::windows_user_function

DBusAllowWindowsUserFunction windows_user_function

Function for checking whether a user is authorized.

**Definition** dbus-transport-protected.h:110

DBusTransport::refcount

int refcount

Reference count.

**Definition** dbus-transport-protected.h:84

DBusTransport::max_live_messages_size

long max_live_messages_size

Max total size of received messages.

**Definition** dbus-transport-protected.h:96

DBusTransport::max_live_messages_unix_fds

long max_live_messages_unix_fds

Max total unix fds of received messages.

**Definition** dbus-transport-protected.h:97

DBusTransport::allow_anonymous

unsigned int allow_anonymous

TRUE if an anonymous client can connect

**Definition** dbus-transport-protected.h:121

DBusTransport::windows_user_data

void \* windows_user_data

Data for windows_user_function.

**Definition** dbus-transport-protected.h:111

DBusTransport::is_server

unsigned int is_server

TRUE if on the server side

**Definition** dbus-transport-protected.h:119

DBusTransport::disconnected

unsigned int disconnected

TRUE if we are disconnected.

**Definition** dbus-transport-protected.h:115

DBusTransport::address

char \* address

Address of the server we are connecting to (NULL for the server side of a transport)

**Definition** dbus-transport-protected.h:101

DBusTransport::unused_bytes_recovered

unsigned int unused_bytes_recovered

TRUE if we've recovered unused bytes from auth

**Definition** dbus-transport-protected.h:120

DBusTransport::vtable

const DBusTransportVTable \* vtable

Virtual methods for this instance.

**Definition** dbus-transport-protected.h:86

DBusTransport::free_unix_user_data

DBusFreeFunction free_unix_user_data

Function to free unix_user_data.

**Definition** dbus-transport-protected.h:108

DBusTransport::send_credentials_pending

unsigned int send_credentials_pending

TRUE if we need to send credentials

**Definition** dbus-transport-protected.h:117

DBusTransport::unix_user_data

void \* unix_user_data

Data for unix_user_function.

**Definition** dbus-transport-protected.h:106

DBusTransport::connection

DBusConnection \* connection

Connection owning this transport.

**Definition** dbus-transport-protected.h:88

DBusTransport::receive_credentials_pending

unsigned int receive_credentials_pending

TRUE if we need to receive credentials

**Definition** dbus-transport-protected.h:118

DBusTransport::loader

DBusMessageLoader \* loader

Message-loading buffer.

**Definition** dbus-transport-protected.h:90

DBusTransport::expected_guid

char \* expected_guid

GUID we expect the server to have, NULL on server side or if we don't have an expectation.

**Definition** dbus-transport-protected.h:103

DBusTransport::free_windows_user_data

DBusFreeFunction free_windows_user_data

Function to free windows_user_data.

**Definition** dbus-transport-protected.h:113

DBusTransport::unix_user_function

DBusAllowUnixUserFunction unix_user_function

Function for checking whether a user is authorized.

**Definition** dbus-transport-protected.h:105

DBusTransport::credentials

DBusCredentials \* credentials

Credentials of other end read from the socket.

**Definition** dbus-transport-protected.h:94

DBusTransport::auth

DBusAuth \* auth

Authentication conversation.

**Definition** dbus-transport-protected.h:92

DBusTransport::live_messages

DBusCounter \* live_messages

Counter for size/unix fds of all live messages.

**Definition** dbus-transport-protected.h:99

DBusWatch

Implementation of DBusWatch.

**Definition** dbus-watch.c:43
