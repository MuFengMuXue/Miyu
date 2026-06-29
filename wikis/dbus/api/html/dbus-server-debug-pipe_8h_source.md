dbus-server-debug-pipe.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-server-debug-pipe.h In-proc debug server implementation

3 \*

4 \* Copyright (C) 2003 CodeFactory AB

5 \* Copyright (C) 2003 Red Hat, Inc.

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

26\#ifndef DBUS_SERVER_DEBUG_PIPE_H

27\#define DBUS_SERVER_DEBUG_PIPE_H

28

29\#include \<dbus/dbus-internals.h\>

30\#include \<dbus/dbus-server-protected.h\>

31\#include \<dbus/dbus-transport-protected.h\>

32

33DBUS_BEGIN_DECLS

34

35DBusServer\* \_dbus_server_debug_pipe_new (const char \*server_name,

36 DBusError \*error);

37DBusTransport\* \_dbus_transport_debug_pipe_new (const char \*server_name,

38 DBusError \*error);

39DBusServerListenResult \_dbus_server_listen_debug_pipe (DBusAddressEntry \*entry,

40 DBusServer \*\*server_p,

41 DBusError \*error);

42DBusTransportOpenResult \_dbus_transport_open_debug_pipe (DBusAddressEntry \*entry,

43 DBusTransport \*\*transport_p,

44 DBusError \*error);

45

46

47DBUS_END_DECLS

48

49\#endif /\* DBUS_SERVER_DEBUG_PIPE_H \*/

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

DBusAddressEntry

Internals of DBusAddressEntry.

**Definition** dbus-address.c:49

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusServer

Internals of DBusServer object.

**Definition** dbus-server-protected.h:59

DBusTransport

Object representing a transport such as a socket.

**Definition** dbus-transport-protected.h:83
