dbus-watch.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-watch.h DBusWatch internal interfaces

3 \*

4 \* Copyright (C) 2002 Red Hat Inc.

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

25\#ifndef DBUS_WATCH_H

26\#define DBUS_WATCH_H

27

28\#include \<dbus/dbus-internals.h\>

29\#include \<dbus/dbus-connection.h\>

30

31DBUS_BEGIN_DECLS

32

38/\* Public methods on DBusWatch are in dbus-connection.h \*/

39

40typedef struct DBusWatchList DBusWatchList;

41

42\#define \_DBUS_WATCH_NVAL (1\<\<4)

43

45typedef dbus_bool_t (\* DBusWatchHandler) (DBusWatch \*watch,

46 unsigned int flags,

47 void \*data);

48

49DBUS_PRIVATE_EXPORT

50DBusWatch\* \_dbus_watch_new (DBusPollable fd,

51 unsigned int flags,

52 dbus_bool_t enabled,

53 DBusWatchHandler handler,

54 void \*data,

55 DBusFreeFunction free_data_function);

56DBUS_PRIVATE_EXPORT

57DBusWatch\* \_dbus_watch_ref (DBusWatch \*watch);

58DBUS_PRIVATE_EXPORT

59void \_dbus_watch_unref (DBusWatch \*watch);

60DBUS_PRIVATE_EXPORT

61void \_dbus_watch_invalidate (DBusWatch \*watch);

62void \_dbus_watch_sanitize_condition (DBusWatch \*watch,

63 unsigned int \*condition);

64void \_dbus_watch_set_handler (DBusWatch \*watch,

65 DBusWatchHandler handler,

66 void \*data,

67 DBusFreeFunction free_data_function);

68

69

70DBUS_PRIVATE_EXPORT

71DBusWatchList\* \_dbus_watch_list_new (void);

72DBUS_PRIVATE_EXPORT

73void \_dbus_watch_list_free (DBusWatchList \*watch_list);

74DBUS_PRIVATE_EXPORT

75dbus_bool_t \_dbus_watch_list_set_functions (DBusWatchList \*watch_list,

76 DBusAddWatchFunction add_function,

77 DBusRemoveWatchFunction remove_function,

78 DBusWatchToggledFunction toggled_function,

79 void \*data,

80 DBusFreeFunction free_data_function);

81DBUS_PRIVATE_EXPORT

82dbus_bool_t \_dbus_watch_list_add_watch (DBusWatchList \*watch_list,

83 DBusWatch \*watch);

84DBUS_PRIVATE_EXPORT

85void \_dbus_watch_list_remove_watch (DBusWatchList \*watch_list,

86 DBusWatch \*watch);

87void \_dbus_watch_list_toggle_watch (DBusWatchList \*watch_list,

88 DBusWatch \*watch,

89 dbus_bool_t enabled);

90void \_dbus_watch_list_toggle_all_watches (DBusWatchList \*watch_list,

91 dbus_bool_t enabled);

92dbus_bool_t \_dbus_watch_get_enabled (DBusWatch \*watch);

93

94DBUS_PRIVATE_EXPORT

95dbus_bool_t \_dbus_watch_get_oom_last_time (DBusWatch \*watch);

96DBUS_PRIVATE_EXPORT

97void \_dbus_watch_set_oom_last_time (DBusWatch \*watch,

98 dbus_bool_t oom);

99

100DBusSocket \_dbus_watch_get_socket (DBusWatch \*watch);

101DBUS_PRIVATE_EXPORT

102DBusPollable \_dbus_watch_get_pollable (DBusWatch \*watch);

103

104static inline void

105\_dbus_clear_watch (DBusWatch \*\*pointer_to_watch)

106{

107 \_dbus_clear_pointer_impl (DBusWatch, pointer_to_watch,

108 \_dbus_watch_unref);

109}

110

113DBUS_END_DECLS

114

115\#endif /\* DBUS_WATCH_H \*/

DBusWatchToggledFunction

void(\* DBusWatchToggledFunction)(DBusWatch \*watch, void \*data)

Called when dbus_watch_get_enabled() may return a different value than it did before.

**Definition** dbus-connection.h:100

DBusAddWatchFunction

dbus_bool_t(\* DBusAddWatchFunction)(DBusWatch \*watch, void \*data)

Called when libdbus needs a new watch to be monitored by the main loop.

**Definition** dbus-connection.h:94

DBusRemoveWatchFunction

void(\* DBusRemoveWatchFunction)(DBusWatch \*watch, void \*data)

Called when libdbus no longer needs a watch to be monitored by the main loop.

**Definition** dbus-connection.h:106

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

\_dbus_watch_list_add_watch

dbus_bool_t \_dbus_watch_list_add_watch(DBusWatchList \*watch_list, DBusWatch \*watch)

Adds a new watch to the watch list, invoking the application DBusAddWatchFunction if appropriate.

**Definition** dbus-watch.c:383

\_dbus_watch_list_toggle_watch

void \_dbus_watch_list_toggle_watch(DBusWatchList \*watch_list, DBusWatch \*watch, dbus_bool_t enabled)

Sets a watch to the given enabled state, invoking the application's DBusWatchToggledFunction if appro...

**Definition** dbus-watch.c:443

\_dbus_watch_list_new

DBusWatchList \* \_dbus_watch_list_new(void)

Creates a new watch list.

**Definition** dbus-watch.c:234

\_dbus_watch_list_free

void \_dbus_watch_list_free(DBusWatchList \*watch_list)

Frees a DBusWatchList.

**Definition** dbus-watch.c:251

\_dbus_watch_list_set_functions

dbus_bool_t \_dbus_watch_list_set_functions(DBusWatchList \*watch_list, DBusAddWatchFunction add_function, DBusRemoveWatchFunction remove_function, DBusWatchToggledFunction toggled_function, void \*data, DBusFreeFunction free_data_function)

Sets the watch functions.

**Definition** dbus-watch.c:297

\_dbus_watch_set_handler

void \_dbus_watch_set_handler(DBusWatch \*watch, DBusWatchHandler handler, void \*data, DBusFreeFunction free_data_function)

Sets the handler for the watch.

**Definition** dbus-watch.c:500

\_dbus_watch_list_toggle_all_watches

void \_dbus_watch_list_toggle_all_watches(DBusWatchList \*watch_list, dbus_bool_t enabled)

Sets all watches to the given enabled state, invoking the application's DBusWatchToggledFunction if a...

**Definition** dbus-watch.c:474

\_dbus_watch_sanitize_condition

void \_dbus_watch_sanitize_condition(DBusWatch \*watch, unsigned int \*condition)

Sanitizes the given condition so that it only contains flags that the DBusWatch requested.

**Definition** dbus-watch.c:187

\_dbus_watch_new

DBusWatch \* \_dbus_watch_new(DBusPollable fd, unsigned int flags, dbus_bool_t enabled, DBusWatchHandler handler, void \*data, DBusFreeFunction free_data_function)

Creates a new DBusWatch.

**Definition** dbus-watch.c:90

DBusWatchHandler

dbus_bool_t(\* DBusWatchHandler)(DBusWatch \*watch, unsigned int flags, void \*data)

function to run when the watch is handled

**Definition** dbus-watch.h:45

\_dbus_watch_ref

DBusWatch \* \_dbus_watch_ref(DBusWatch \*watch)

Increments the reference count of a DBusWatch object.

**Definition** dbus-watch.c:126

\_dbus_watch_unref

void \_dbus_watch_unref(DBusWatch \*watch)

Decrements the reference count of a DBusWatch object and finalizes the object if the count reaches ze...

**Definition** dbus-watch.c:140

\_dbus_watch_list_remove_watch

void \_dbus_watch_list_remove_watch(DBusWatchList \*watch_list, DBusWatch \*watch)

Removes a watch from the watch list, invoking the application's DBusRemoveWatchFunction if appropriat...

**Definition** dbus-watch.c:416

\_dbus_watch_invalidate

void \_dbus_watch_invalidate(DBusWatch \*watch)

Clears the file descriptor from a now-invalid watch object so that no one tries to use it.

**Definition** dbus-watch.c:171

DBusSocket

Socket interface.

**Definition** dbus-sysdeps.h:185

DBusWatchList

DBusWatchList implementation details.

**Definition** dbus-watch.c:217

DBusWatch

Implementation of DBusWatch.

**Definition** dbus-watch.c:43
