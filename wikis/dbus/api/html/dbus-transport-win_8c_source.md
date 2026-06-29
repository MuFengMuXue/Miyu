dbus-transport-win.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-transport-win.c Windows socket subclasses of DBusTransport

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

29\#include "dbus-connection-internal.h"

30\#include "dbus-transport-socket.h"

31\#include "dbus-transport-protected.h"

32\#include "dbus-watch.h"

33\#include "dbus-sysdeps-win.h"

34

51DBusTransportOpenResult

52\_dbus_transport_open_platform_specific (DBusAddressEntry \*entry,

53 DBusTransport \*\*transport_p,

54 DBusError \*error)

55{

56 /\* currently no Windows-specific transports \*/

57 return DBUS_TRANSPORT_OPEN_NOT_HANDLED;

58}

59

\_dbus_transport_open_platform_specific

DBusTransportOpenResult \_dbus_transport_open_platform_specific(DBusAddressEntry \*entry, DBusTransport \*\*transport_p, DBusError \*error)

Opens platform specific transport types.

**Definition** dbus-transport-unix.c:248

DBusAddressEntry

Internals of DBusAddressEntry.

**Definition** dbus-address.c:49

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusTransport

Object representing a transport such as a socket.

**Definition** dbus-transport-protected.h:83
