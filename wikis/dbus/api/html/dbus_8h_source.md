dbus.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus.h Convenience header including all other headers

3 \*

4 \* Copyright (C) 2002, 2003 Red Hat Inc.

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

26\#ifndef DBUS_H

27\#define DBUS_H

28

29\#define DBUS_INSIDE_DBUS_H 1

30

31\#include \<dbus/dbus-arch-deps.h\>

32\#include \<dbus/dbus-address.h\>

33\#include \<dbus/dbus-bus.h\>

34\#include \<dbus/dbus-connection.h\>

35\#include \<dbus/dbus-errors.h\>

36\#include \<dbus/dbus-macros.h\>

37\#include \<dbus/dbus-message.h\>

38\#include \<dbus/dbus-misc.h\>

39\#include \<dbus/dbus-pending-call.h\>

40\#include \<dbus/dbus-protocol.h\>

41\#include \<dbus/dbus-server.h\>

42\#include \<dbus/dbus-shared.h\>

43\#include \<dbus/dbus-signature.h\>

44\#include \<dbus/dbus-syntax.h\>

45\#include \<dbus/dbus-threads.h\>

46\#include \<dbus/dbus-types.h\>

47

48\#undef DBUS_INSIDE_DBUS_H

49

106\#endif /\* DBUS_H \*/
