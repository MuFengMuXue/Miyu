dbus-auth.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-auth.h Authentication

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

25\#ifndef DBUS_AUTH_H

26\#define DBUS_AUTH_H

27

28\#include \<dbus/dbus-macros.h\>

29\#include \<dbus/dbus-errors.h\>

30\#include \<dbus/dbus-string.h\>

31\#include \<dbus/dbus-sysdeps.h\>

32

33DBUS_BEGIN_DECLS

34

35typedef struct DBusAuth DBusAuth;

36

37typedef enum

38{

39 DBUS_AUTH_STATE_WAITING_FOR_INPUT,

40 DBUS_AUTH_STATE_WAITING_FOR_MEMORY,

41 DBUS_AUTH_STATE_HAVE_BYTES_TO_SEND,

42 DBUS_AUTH_STATE_NEED_DISCONNECT,

43 DBUS_AUTH_STATE_AUTHENTICATED,

44 DBUS_AUTH_STATE_INVALID = -1

45} DBusAuthState;

46

47DBUS_PRIVATE_EXPORT

48DBusAuth\* \_dbus_auth_server_new (const DBusString \*guid);

49DBUS_PRIVATE_EXPORT

50DBusAuth\* \_dbus_auth_client_new (void);

51DBUS_PRIVATE_EXPORT

52DBusAuth\* \_dbus_auth_ref (DBusAuth \*auth);

53DBUS_PRIVATE_EXPORT

54void \_dbus_auth_unref (DBusAuth \*auth);

55DBUS_PRIVATE_EXPORT

56dbus_bool_t \_dbus_auth_set_mechanisms (DBusAuth \*auth,

57 const char \*\*mechanisms);

58DBUS_PRIVATE_EXPORT

59DBusAuthState \_dbus_auth_do_work (DBusAuth \*auth);

60DBUS_PRIVATE_EXPORT

61dbus_bool_t \_dbus_auth_get_bytes_to_send (DBusAuth \*auth,

62 const DBusString \*\*str);

63DBUS_PRIVATE_EXPORT

64void \_dbus_auth_bytes_sent (DBusAuth \*auth,

65 int bytes_sent);

66DBUS_PRIVATE_EXPORT

67void \_dbus_auth_get_buffer (DBusAuth \*auth,

68 DBusString \*\*buffer);

69DBUS_PRIVATE_EXPORT

70void \_dbus_auth_return_buffer (DBusAuth \*auth,

71 DBusString \*buffer);

72DBUS_PRIVATE_EXPORT

73void \_dbus_auth_get_unused_bytes (DBusAuth \*auth,

74 const DBusString \*\*str);

75DBUS_PRIVATE_EXPORT

76void \_dbus_auth_delete_unused_bytes (DBusAuth \*auth);

77dbus_bool_t \_dbus_auth_needs_encoding (DBusAuth \*auth);

78dbus_bool_t \_dbus_auth_encode_data (DBusAuth \*auth,

79 const DBusString \*plaintext,

80 DBusString \*encoded);

81dbus_bool_t \_dbus_auth_needs_decoding (DBusAuth \*auth);

82dbus_bool_t \_dbus_auth_decode_data (DBusAuth \*auth,

83 const DBusString \*encoded,

84 DBusString \*plaintext);

85DBUS_PRIVATE_EXPORT

86dbus_bool_t \_dbus_auth_set_credentials (DBusAuth \*auth,

87 DBusCredentials \*credentials);

88DBUS_PRIVATE_EXPORT

89DBusCredentials\* \_dbus_auth_get_identity (DBusAuth \*auth);

90DBUS_PRIVATE_EXPORT

91dbus_bool_t \_dbus_auth_set_context (DBusAuth \*auth,

92 const DBusString \*context);

93const char\* \_dbus_auth_get_guid_from_server(DBusAuth \*auth);

94

95void \_dbus_auth_set_unix_fd_possible(DBusAuth \*auth, dbus_bool_t b);

96dbus_bool_t \_dbus_auth_get_unix_fd_negotiated(DBusAuth \*auth);

97DBUS_PRIVATE_EXPORT

98dbus_bool_t \_dbus_auth_is_supported_mechanism(DBusString \*name);

99DBUS_PRIVATE_EXPORT

100dbus_bool_t \_dbus_auth_dump_supported_mechanisms(DBusString \*buffer);

101

102DBUS_END_DECLS

103

104\#endif /\* DBUS_AUTH_H \*/

\_dbus_auth_do_work

DBUS_PRIVATE_EXPORT DBusAuthState \_dbus_auth_do_work(DBusAuth \*auth)

Analyzes buffered input and moves the auth conversation forward, returning the new state of the auth ...

**Definition** dbus-auth.c:2548

\_dbus_auth_encode_data

dbus_bool_t \_dbus_auth_encode_data(DBusAuth \*auth, const DBusString \*plaintext, DBusString \*encoded)

Called post-authentication, encodes a block of bytes for sending to the peer.

**Definition** dbus-auth.c:2735

\_dbus_auth_dump_supported_mechanisms

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_auth_dump_supported_mechanisms(DBusString \*buffer)

Return a human-readable string containing all supported auth mechanisms.

**Definition** dbus-auth.c:2944

\_dbus_auth_needs_encoding

dbus_bool_t \_dbus_auth_needs_encoding(DBusAuth \*auth)

Called post-authentication, indicates whether we need to encode the message stream with \_dbus_auth_en...

**Definition** dbus-auth.c:2708

\_dbus_auth_set_credentials

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_auth_set_credentials(DBusAuth \*auth, DBusCredentials \*credentials)

Sets credentials received via reliable means from the operating system.

**Definition** dbus-auth.c:2830

\_dbus_auth_get_unix_fd_negotiated

dbus_bool_t \_dbus_auth_get_unix_fd_negotiated(DBusAuth \*auth)

Queries whether unix fd passing was successfully negotiated.

**Definition** dbus-auth.c:2918

\_dbus_auth_ref

DBUS_PRIVATE_EXPORT DBusAuth \* \_dbus_auth_ref(DBusAuth \*auth)

Increments the refcount of an auth object.

**Definition** dbus-auth.c:2448

\_dbus_auth_is_supported_mechanism

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_auth_is_supported_mechanism(DBusString \*name)

Queries whether the given auth mechanism is supported.

**Definition** dbus-auth.c:2930

\_dbus_auth_get_identity

DBUS_PRIVATE_EXPORT DBusCredentials \* \_dbus_auth_get_identity(DBusAuth \*auth)

Gets the identity we authorized the client as.

**Definition** dbus-auth.c:2848

\_dbus_auth_get_bytes_to_send

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_auth_get_bytes_to_send(DBusAuth \*auth, const DBusString \*\*str)

Gets bytes that need to be sent to the peer we're conversing with.

**Definition** dbus-auth.c:2592

\_dbus_auth_decode_data

dbus_bool_t \_dbus_auth_decode_data(DBusAuth \*auth, const DBusString \*encoded, DBusString \*plaintext)

Called post-authentication, decodes a block of bytes received from the peer.

**Definition** dbus-auth.c:2798

\_dbus_auth_unref

DBUS_PRIVATE_EXPORT void \_dbus_auth_unref(DBusAuth \*auth)

Decrements the refcount of an auth object.

**Definition** dbus-auth.c:2463

\_dbus_auth_set_unix_fd_possible

void \_dbus_auth_set_unix_fd_possible(DBusAuth \*auth, dbus_bool_t b)

Sets whether unix fd passing is potentially on the transport and hence shall be negotiated.

**Definition** dbus-auth.c:2906

\_dbus_auth_return_buffer

DBUS_PRIVATE_EXPORT void \_dbus_auth_return_buffer(DBusAuth \*auth, DBusString \*buffer)

Returns a buffer with new data read into it.

**Definition** dbus-auth.c:2655

\_dbus_auth_set_mechanisms

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_auth_set_mechanisms(DBusAuth \*auth, const char \*\*mechanisms)

Sets an array of authentication mechanism names that we are willing to use.

**Definition** dbus-auth.c:2513

\_dbus_auth_delete_unused_bytes

DBUS_PRIVATE_EXPORT void \_dbus_auth_delete_unused_bytes(DBusAuth \*auth)

Gets rid of unused bytes returned by \_dbus_auth_get_unused_bytes() after we've gotten them and succes...

**Definition** dbus-auth.c:2691

\_dbus_auth_get_guid_from_server

const char \* \_dbus_auth_get_guid_from_server(DBusAuth \*auth)

Gets the GUID from the server if we've authenticated; gets NULL otherwise.

**Definition** dbus-auth.c:2872

\_dbus_auth_get_buffer

DBUS_PRIVATE_EXPORT void \_dbus_auth_get_buffer(DBusAuth \*auth, DBusString \*\*buffer)

Get a buffer to be used for reading bytes from the peer we're conversing with.

**Definition** dbus-auth.c:2637

\_dbus_auth_needs_decoding

dbus_bool_t \_dbus_auth_needs_decoding(DBusAuth \*auth)

Called post-authentication, indicates whether we need to decode the message stream with \_dbus_auth_de...

**Definition** dbus-auth.c:2767

\_dbus_auth_set_context

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_auth_set_context(DBusAuth \*auth, const DBusString \*context)

Sets the "authentication context" which scopes cookies with the DBUS_COOKIE_SHA1 auth mechanism for e...

**Definition** dbus-auth.c:2891

\_dbus_auth_bytes_sent

DBUS_PRIVATE_EXPORT void \_dbus_auth_bytes_sent(DBusAuth \*auth, int bytes_sent)

Notifies the auth conversation object that the given number of bytes of the outgoing buffer have been...

**Definition** dbus-auth.c:2617

\_dbus_auth_client_new

DBUS_PRIVATE_EXPORT DBusAuth \* \_dbus_auth_client_new(void)

Creates a new auth conversation object for the client side.

**Definition** dbus-auth.c:2410

\_dbus_auth_server_new

DBUS_PRIVATE_EXPORT DBusAuth \* \_dbus_auth_server_new(const DBusString \*guid)

Creates a new auth conversation object for the server side.

**Definition** dbus-auth.c:2364

\_dbus_auth_get_unused_bytes

DBUS_PRIVATE_EXPORT void \_dbus_auth_get_unused_bytes(DBusAuth \*auth, const DBusString \*\*str)

Returns leftover bytes that were not used as part of the auth conversation.

**Definition** dbus-auth.c:2674

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

DBusAuth

Internal members of DBusAuth.

**Definition** dbus-auth.c:156

DBusAuth::credentials

DBusCredentials \* credentials

Credentials read from socket.

**Definition** dbus-auth.c:171

DBusAuth::context

DBusString context

Cookie scope.

**Definition** dbus-auth.c:178

DBusCredentials

**Definition** dbus-credentials.c:60

DBusString

**Definition** dbus-string.h:47
