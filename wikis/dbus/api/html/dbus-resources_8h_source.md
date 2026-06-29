dbus-resources.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-resources.h Resource tracking/limits

3 \*

4 \* Copyright (C) 2003 Red Hat Inc.

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

25\#ifndef DBUS_RESOURCES_H

26\#define DBUS_RESOURCES_H

27

28\#include \<dbus/dbus-macros.h\>

29\#include \<dbus/dbus-macros-internal.h\>

30\#include \<dbus/dbus-errors.h\>

31\#include \<dbus/dbus-connection.h\>

32

33DBUS_BEGIN_DECLS

34

35typedef struct DBusCounter DBusCounter;

36

37typedef void (\* DBusCounterNotifyFunction) (DBusCounter \*counter,

38 void \*user_data);

39DBUS_EMBEDDED_TESTS_EXPORT

40DBusCounter\* \_dbus_counter_new (void);

41DBusCounter\* \_dbus_counter_ref (DBusCounter \*counter);

42DBUS_EMBEDDED_TESTS_EXPORT

43void \_dbus_counter_unref (DBusCounter \*counter);

44

45DBUS_EMBEDDED_TESTS_EXPORT

46void \_dbus_counter_adjust_size (DBusCounter \*counter,

47 long delta);

48DBUS_EMBEDDED_TESTS_EXPORT

49void \_dbus_counter_adjust_unix_fd (DBusCounter \*counter,

50 long delta);

51void \_dbus_counter_notify (DBusCounter \*counter);

52DBUS_EMBEDDED_TESTS_EXPORT

53long \_dbus_counter_get_size_value (DBusCounter \*counter);

54DBUS_EMBEDDED_TESTS_EXPORT

55long \_dbus_counter_get_unix_fd_value (DBusCounter \*counter);

56

57void \_dbus_counter_set_notify (DBusCounter \*counter,

58 long size_guard_value,

59 long unix_fd_guard_value,

60 DBusCounterNotifyFunction function,

61 void \*user_data);

62

63/\* if DBUS_ENABLE_STATS \*/

64long \_dbus_counter_get_peak_size_value (DBusCounter \*counter);

65long \_dbus_counter_get_peak_unix_fd_value (DBusCounter \*counter);

66

67DBUS_END_DECLS

68

69\#endif /\* DBUS_RESOURCES_H \*/

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

\_dbus_counter_set_notify

void \_dbus_counter_set_notify(DBusCounter \*counter, long size_guard_value, long unix_fd_guard_value, DBusCounterNotifyFunction function, void \*user_data)

Sets the notify function for this counter; the notify function is called whenever the counter's value...

**Definition** dbus-resources.c:313

\_dbus_counter_new

DBUS_EMBEDDED_TESTS_EXPORT DBusCounter \* \_dbus_counter_new(void)

Creates a new DBusCounter.

**Definition** dbus-resources.c:91

\_dbus_counter_get_unix_fd_value

DBUS_EMBEDDED_TESTS_EXPORT long \_dbus_counter_get_unix_fd_value(DBusCounter \*counter)

Gets the current value of the unix fd counter.

**Definition** dbus-resources.c:292

\_dbus_counter_unref

DBUS_EMBEDDED_TESTS_EXPORT void \_dbus_counter_unref(DBusCounter \*counter)

Decrements refcount of the counter and possibly finalizes the counter.

**Definition** dbus-resources.c:138

\_dbus_counter_get_size_value

DBUS_EMBEDDED_TESTS_EXPORT long \_dbus_counter_get_size_value(DBusCounter \*counter)

Gets the current value of the size counter.

**Definition** dbus-resources.c:276

\_dbus_counter_adjust_unix_fd

DBUS_EMBEDDED_TESTS_EXPORT void \_dbus_counter_adjust_unix_fd(DBusCounter \*counter, long delta)

Adjusts the value of the unix fd counter by the given delta which may be positive or negative.

**Definition** dbus-resources.c:238

\_dbus_counter_notify

void \_dbus_counter_notify(DBusCounter \*counter)

Calls the notify function from \_dbus_counter_set_notify(), if that function has been specified and th...

**Definition** dbus-resources.c:209

\_dbus_counter_ref

DBusCounter \* \_dbus_counter_ref(DBusCounter \*counter)

Increments refcount of the counter.

**Definition** dbus-resources.c:118

\_dbus_counter_adjust_size

DBUS_EMBEDDED_TESTS_EXPORT void \_dbus_counter_adjust_size(DBusCounter \*counter, long delta)

Adjusts the value of the size counter by the given delta which may be positive or negative.

**Definition** dbus-resources.c:169

DBusCounter

Internals of DBusCounter.

**Definition** dbus-resources.c:57
