dbus-message-util.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-message-util.c Would be in dbus-message.c, but only used by bus/tests

3 \*

4 \* Copyright 2017 Collabora Ltd.

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

27

28\#include "dbus-message-private.h"

29

41unsigned int

42\_dbus_message_get_n_unix_fds (DBusMessage \*message)

43{

44\#ifdef HAVE_UNIX_FD_PASSING

45 return message-\>n_unix_fds;

46\#else

47 return 0;

48\#endif

49}

50

\_dbus_message_get_n_unix_fds

unsigned int \_dbus_message_get_n_unix_fds(DBusMessage \*message)

Gets the number of unix fds attached to this message.

**Definition** dbus-message-util.c:42

DBusMessage

Internals of DBusMessage.

**Definition** dbus-message-private.h:102
