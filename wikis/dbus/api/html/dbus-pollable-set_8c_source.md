dbus-pollable-set.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\*

3 \* dbus-pollable-set.c - a set of pollable objects (file descriptors, sockets or handles)

4 \*

5 \* Copyright © 2011 Nokia Corporation

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

23 \* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,

24 \* MA 02110-1301 USA

25 \*

26 \*/

27

28\#include \<config.h\>

29\#include \<dbus/dbus-pollable-set.h\>

30

31DBusPollableSet \*

32\_dbus_pollable_set_new (int size_hint)

33{

34 DBusPollableSet \*ret;

35

36\#ifdef DBUS_HAVE_LINUX_EPOLL

37 ret = \_dbus_pollable_set_epoll_new ();

38

39 if (ret != NULL)

40 return ret;

41\#endif

42

43 ret = \_dbus_pollable_set_poll_new (size_hint);

44

45 if (ret != NULL)

46 return ret;

47

48 return NULL;

49}

NULL

\#define NULL

A null pointer, defined appropriately for C or C++.

**Definition** dbus-macros.h:51
