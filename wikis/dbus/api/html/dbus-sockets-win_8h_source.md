dbus-sockets-win.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-sockets.h Wrappers around socket features (internal to D-BUS implementation)

3 \*

4 \* Copyright (C) 2005 Novell, Inc.

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

26\#ifndef DBUS_SOCKETS_H

27\#define DBUS_SOCKETS_H

28

29\#if defined(DBUS_WIN) \|\| defined(DBUS_WINCE)

30

31

32

33\#ifndef STRICT

34\#define STRICT

35\#include \<winsock2.h\>

36\#undef STRICT

37\#endif

38\#include \<winsock2.h\>

39

40\#undef interface

41

42\#if HAVE_ERRNO_H

43\#include \<errno.h\>

44\#endif

45

46\#define DBUS_SOCKET_API_RETURNS_ERROR(n) ((n) == SOCKET_ERROR)

47\#define DBUS_SOCKET_SET_ERRNO() (\_dbus_win_set_errno (WSAGetLastError()))

48

49\#else

50

51\#error "dbus-sockets-win.h should not be included on non-Windows"

52

53\#endif /\* !Win32 \*/

54

55\#endif /\* DBUS_SOCKETS_H \*/
