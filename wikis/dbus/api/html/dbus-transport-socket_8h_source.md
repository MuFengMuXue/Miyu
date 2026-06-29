dbus-transport-socket.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-transport-socket.h Socket subclasses of DBusTransport

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

25\#ifndef DBUS_TRANSPORT_SOCKET_H

26\#define DBUS_TRANSPORT_SOCKET_H

27

28\#include \<dbus/dbus-transport-protected.h\>

29

30DBUS_BEGIN_DECLS

31

32DBusTransport\* \_dbus_transport_new_for_socket (DBusSocket fd,

33 const DBusString \*server_guid,

34 const DBusString \*address);

35DBusTransport\* \_dbus_transport_new_for_tcp_socket (const char \*host,

36 const char \*port,

37 const char \*family,

38 const char \*noncefile,

39 DBusError \*error);

40DBusTransportOpenResult \_dbus_transport_open_socket (DBusAddressEntry \*entry,

41 DBusTransport \*\*transport_p,

42 DBusError \*error);

43

44DBusTransport\* \_dbus_transport_new_for_domain_socket (const char \*path,

45 dbus_bool_t abstract,

46 DBusError \*error);

47

48DBusTransportOpenResult \_dbus_transport_open_unix_socket (DBusAddressEntry \*entry,

49 DBusTransport \*\*transport_p,

50 DBusError \*error);

51

52DBUS_END_DECLS

53

54\#endif /\* DBUS_TRANSPORT_SOCKET_H \*/

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

\_dbus_transport_open_socket

DBusTransportOpenResult \_dbus_transport_open_socket(DBusAddressEntry \*entry, DBusTransport \*\*transport_p, DBusError \*error)

Opens a TCP socket transport.

**Definition** dbus-transport-socket.c:1457

\_dbus_transport_open_unix_socket

DBusTransportOpenResult \_dbus_transport_open_unix_socket(DBusAddressEntry \*entry, DBusTransport \*\*transport_p, DBusError \*error)

Opens a UNIX socket transport.

**Definition** dbus-transport-socket.c:1584

\_dbus_transport_new_for_tcp_socket

DBusTransport \* \_dbus_transport_new_for_tcp_socket(const char \*host, const char \*port, const char \*family, const char \*noncefile, DBusError \*error)

Creates a new transport for the given hostname and port.

**Definition** dbus-transport-socket.c:1379

\_dbus_transport_new_for_socket

DBusTransport \* \_dbus_transport_new_for_socket(DBusSocket fd, const DBusString \*server_guid, const DBusString \*address)

Creates a new transport for the given socket file descriptor.

**Definition** dbus-transport-socket.c:1295

\_dbus_transport_new_for_domain_socket

DBusTransport \* \_dbus_transport_new_for_domain_socket(const char \*path, dbus_bool_t abstract, DBusError \*error)

Creates a new transport for the given Unix domain socket path.

**Definition** dbus-transport-socket.c:1518

DBusAddressEntry

Internals of DBusAddressEntry.

**Definition** dbus-address.c:49

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusSocket

Socket interface.

**Definition** dbus-sysdeps.h:185

DBusString

**Definition** dbus-string.h:47

DBusTransport

Object representing a transport such as a socket.

**Definition** dbus-transport-protected.h:83
