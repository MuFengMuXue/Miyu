dbus-timeout.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-timeout.h DBusTimeout internal interfaces

3 \*

4 \* Copyright (C) 2003 CodeFactory AB

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

25\#ifndef DBUS_TIMEOUT_H

26\#define DBUS_TIMEOUT_H

27

28\#include \<dbus/dbus-connection.h\>

29\#include \<dbus/dbus-internals.h\>

30

31DBUS_BEGIN_DECLS

32

38/\* Public methods on DBusTimeout are in dbus-connection.h \*/

39

40typedef struct DBusTimeoutList DBusTimeoutList;

41

43typedef dbus_bool_t (\* DBusTimeoutHandler) (void \*data);

44

45DBUS_PRIVATE_EXPORT

46DBusTimeout\* \_dbus_timeout_new (int interval,

47 DBusTimeoutHandler handler,

48 void \*data,

49 DBusFreeFunction free_data_function);

50DBusTimeout\* \_dbus_timeout_ref (DBusTimeout \*timeout);

51DBUS_PRIVATE_EXPORT

52void \_dbus_timeout_unref (DBusTimeout \*timeout);

53DBUS_PRIVATE_EXPORT

54void \_dbus_timeout_restart (DBusTimeout \*timeout,

55 int interval);

56DBUS_PRIVATE_EXPORT

57void \_dbus_timeout_disable (DBusTimeout \*timeout);

58

59DBusTimeoutList \*\_dbus_timeout_list_new (void);

60void \_dbus_timeout_list_free (DBusTimeoutList \*timeout_list);

61dbus_bool_t \_dbus_timeout_list_set_functions (DBusTimeoutList \*timeout_list,

62 DBusAddTimeoutFunction add_function,

63 DBusRemoveTimeoutFunction remove_function,

64 DBusTimeoutToggledFunction toggled_function,

65 void \*data,

66 DBusFreeFunction free_data_function);

67dbus_bool_t \_dbus_timeout_list_add_timeout (DBusTimeoutList \*timeout_list,

68 DBusTimeout \*timeout);

69void \_dbus_timeout_list_remove_timeout (DBusTimeoutList \*timeout_list,

70 DBusTimeout \*timeout);

71void \_dbus_timeout_list_toggle_timeout (DBusTimeoutList \*timeout_list,

72 DBusTimeout \*timeout,

73 dbus_bool_t enabled);

74

75DBUS_PRIVATE_EXPORT

76dbus_bool_t \_dbus_timeout_needs_restart (DBusTimeout \*timeout);

77DBUS_PRIVATE_EXPORT

78void \_dbus_timeout_restarted (DBusTimeout \*timeout);

79

82DBUS_END_DECLS

83

84\#endif /\* DBUS_TIMEOUT_H \*/

DBusTimeoutToggledFunction

void(\* DBusTimeoutToggledFunction)(DBusTimeout \*timeout, void \*data)

Called when dbus_timeout_get_enabled() may return a different value than it did before.

**Definition** dbus-connection.h:120

DBusAddTimeoutFunction

dbus_bool_t(\* DBusAddTimeoutFunction)(DBusTimeout \*timeout, void \*data)

Called when libdbus needs a new timeout to be monitored by the main loop.

**Definition** dbus-connection.h:113

DBusRemoveTimeoutFunction

void(\* DBusRemoveTimeoutFunction)(DBusTimeout \*timeout, void \*data)

Called when libdbus no longer needs a timeout to be monitored by the main loop.

**Definition** dbus-connection.h:126

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

DBusFreeFunction

void(\* DBusFreeFunction)(void \*memory)

The type of a function which frees a block of memory.

**Definition** dbus-memory.h:65

\_dbus_timeout_list_add_timeout

dbus_bool_t \_dbus_timeout_list_add_timeout(DBusTimeoutList \*timeout_list, DBusTimeout \*timeout)

Adds a new timeout to the timeout list, invoking the application DBusAddTimeoutFunction if appropriat...

**Definition** dbus-timeout.c:314

\_dbus_timeout_list_free

void \_dbus_timeout_list_free(DBusTimeoutList \*timeout_list)

Frees a DBusTimeoutList.

**Definition** dbus-timeout.c:217

\_dbus_timeout_list_toggle_timeout

void \_dbus_timeout_list_toggle_timeout(DBusTimeoutList \*timeout_list, DBusTimeout \*timeout, dbus_bool_t enabled)

Sets a timeout to the given enabled state, invoking the application's DBusTimeoutToggledFunction if a...

**Definition** dbus-timeout.c:366

\_dbus_timeout_list_new

DBusTimeoutList \* \_dbus_timeout_list_new(void)

Creates a new timeout list.

**Definition** dbus-timeout.c:200

\_dbus_timeout_unref

void \_dbus_timeout_unref(DBusTimeout \*timeout)

Decrements the reference count of a DBusTimeout object and finalizes the object if the count reaches ...

**Definition** dbus-timeout.c:111

\_dbus_timeout_list_set_functions

dbus_bool_t \_dbus_timeout_list_set_functions(DBusTimeoutList \*timeout_list, DBusAddTimeoutFunction add_function, DBusRemoveTimeoutFunction remove_function, DBusTimeoutToggledFunction toggled_function, void \*data, DBusFreeFunction free_data_function)

Sets the timeout functions.

**Definition** dbus-timeout.c:243

\_dbus_timeout_disable

void \_dbus_timeout_disable(DBusTimeout \*timeout)

Disable the timeout.

**Definition** dbus-timeout.c:161

\_dbus_timeout_new

DBusTimeout \* \_dbus_timeout_new(int interval, DBusTimeoutHandler handler, void \*data, DBusFreeFunction free_data_function)

Creates a new DBusTimeout, enabled by default.

**Definition** dbus-timeout.c:66

\_dbus_timeout_restart

void \_dbus_timeout_restart(DBusTimeout \*timeout, int interval)

Change the timeout interval to be interval milliseconds from now (forgetting when the timeout was ini...

**Definition** dbus-timeout.c:140

DBusTimeoutHandler

dbus_bool_t(\* DBusTimeoutHandler)(void \*data)

function to run when the timeout is handled

**Definition** dbus-timeout.h:43

\_dbus_timeout_ref

DBusTimeout \* \_dbus_timeout_ref(DBusTimeout \*timeout)

Increments the reference count of a DBusTimeout object.

**Definition** dbus-timeout.c:97

\_dbus_timeout_restarted

void \_dbus_timeout_restarted(DBusTimeout \*timeout)

Mark timeout as restarted (setting timestamps is responsibility of the event loop).

**Definition** dbus-timeout.c:401

\_dbus_timeout_list_remove_timeout

void \_dbus_timeout_list_remove_timeout(DBusTimeoutList \*timeout_list, DBusTimeout \*timeout)

Removes a timeout from the timeout list, invoking the application's DBusRemoveTimeoutFunction if appr...

**Definition** dbus-timeout.c:344

\_dbus_timeout_needs_restart

dbus_bool_t \_dbus_timeout_needs_restart(DBusTimeout \*timeout)

Returns whether a timeout needs restart time counting in the event loop.

**Definition** dbus-timeout.c:389

DBusTimeoutList

DBusTimeoutList implementation details.

**Definition** dbus-timeout.c:183

DBusTimeout

Internals of DBusTimeout.

**Definition** dbus-timeout.c:43
