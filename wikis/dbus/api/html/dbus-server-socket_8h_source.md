dbus-server-socket.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-server-socket.h Server implementation for sockets

3 \*

4 \* Copyright (C) 2002, 2006 Red Hat Inc.

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

25\#ifndef DBUS_SERVER_SOCKET_H

26\#define DBUS_SERVER_SOCKET_H

27

28\#include \<dbus/dbus-internals.h\>

29\#include \<dbus/dbus-server-protected.h\>

30\#include \<dbus/dbus-nonce.h\>

31

32DBUS_BEGIN_DECLS

33

34DBusServer\* \_dbus_server_new_for_socket (DBusSocket \*fds,

35 int n_fds,

36 const DBusString \*address,

37 DBusNonceFile \*noncefile,

38 DBusError \*error);

39DBusServer\* \_dbus_server_new_for_autolaunch (const DBusString \*address,

40 DBusError \*error);

41DBUS_PRIVATE_EXPORT

42DBusServer\* \_dbus_server_new_for_tcp_socket (const char \*host,

43 const char \*bind,

44 const char \*port,

45 const char \*family,

46 DBusError \*error,

47 dbus_bool_t use_nonce);

48DBusServerListenResult \_dbus_server_listen_socket (DBusAddressEntry \*entry,

49 DBusServer \*\*server_p,

50 DBusError \*error);

51

52

53void \_dbus_server_socket_own_filename (DBusServer \*server,

54 char \*filename);

55

56DBusServer\* \_dbus_server_new_for_domain_socket (const char \*path,

57 dbus_bool_t abstract,

58 DBusError \*error);

59DBUS_END_DECLS

60

61\#endif /\* DBUS_SERVER_SOCKET_H \*/

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

\_dbus_server_new_for_domain_socket

DBusServer \* \_dbus_server_new_for_domain_socket(const char \*path, dbus_bool_t abstract, DBusError \*error)

Creates a new server listening on the given Unix domain socket.

**Definition** dbus-server-socket.c:610

\_dbus_server_new_for_tcp_socket

DBUS_PRIVATE_EXPORT DBusServer \* \_dbus_server_new_for_tcp_socket(const char \*host, const char \*bind, const char \*port, const char \*family, DBusError \*error, dbus_bool_t use_nonce)

Creates a new server listening on TCP.

**Definition** dbus-server-socket.c:420

\_dbus_server_new_for_socket

DBusServer \* \_dbus_server_new_for_socket(DBusSocket \*fds, int n_fds, const DBusString \*address, DBusNonceFile \*noncefile, DBusError \*error)

Creates a new server listening on the given file descriptor.

**Definition** dbus-server-socket.c:288

\_dbus_server_listen_socket

DBusServerListenResult \_dbus_server_listen_socket(DBusAddressEntry \*entry, DBusServer \*\*server_p, DBusError \*error)

Tries to interpret the address entry for various socket-related addresses (well, currently only tcp a...

**Definition** dbus-server-socket.c:540

\_dbus_server_socket_own_filename

void \_dbus_server_socket_own_filename(DBusServer \*server, char \*filename)

This is a bad hack since it's really unix domain socket specific.

**Definition** dbus-server-socket.c:593

DBusAddressEntry

Internals of DBusAddressEntry.

**Definition** dbus-address.c:49

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusNonceFile

**Definition** dbus-nonce.c:36

DBusServer

Internals of DBusServer object.

**Definition** dbus-server-protected.h:59

DBusSocket

Socket interface.

**Definition** dbus-sysdeps.h:185

DBusString

**Definition** dbus-string.h:47
