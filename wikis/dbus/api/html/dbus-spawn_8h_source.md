dbus-spawn.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-spawn.h Wrapper around fork/exec

3 \*

4 \* Copyright (C) 2002, 2003 Red Hat, Inc.

5 \* Copyright (C) 2003 CodeFactory AB

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

27\#ifndef DBUS_SPAWN_H

28\#define DBUS_SPAWN_H

29

30\#include \<dbus/dbus-string.h\>

31\#include \<dbus/dbus-errors.h\>

32\#include \<dbus/dbus-watch.h\>

33

34DBUS_BEGIN_DECLS

35

36typedef void (\* DBusSpawnChildSetupFunc) (void \*user_data);

37

38typedef struct DBusBabysitter DBusBabysitter;

39

40typedef void (\* DBusBabysitterFinishedFunc) (DBusBabysitter \*sitter,

41 void \*user_data);

42

43typedef enum {

44 DBUS_SPAWN_REDIRECT_OUTPUT = (1 \<\< 0),

45 DBUS_SPAWN_SILENCE_OUTPUT = (1 \<\< 1),

46 DBUS_SPAWN_NONE = 0

47} DBusSpawnFlags;

48

49dbus_bool_t \_dbus_spawn_async_with_babysitter (DBusBabysitter \*\*sitter_p,

50 const char \*log_name,

51 char \* const \*argv,

52 char \* const \*env,

53 DBusSpawnFlags flags,

54 DBusSpawnChildSetupFunc child_setup,

55 void \*user_data,

56 DBusError \*error);

57void \_dbus_babysitter_set_result_function (DBusBabysitter \*sitter,

58 DBusBabysitterFinishedFunc finished,

59 void \*user_data);

60DBusBabysitter\* \_dbus_babysitter_ref (DBusBabysitter \*sitter);

61void \_dbus_babysitter_unref (DBusBabysitter \*sitter);

62void \_dbus_babysitter_kill_child (DBusBabysitter \*sitter);

63dbus_bool_t \_dbus_babysitter_get_child_exited (DBusBabysitter \*sitter);

64void \_dbus_babysitter_set_child_exit_error (DBusBabysitter \*sitter,

65 DBusError \*error);

66dbus_bool_t \_dbus_babysitter_get_child_exit_status (DBusBabysitter \*sitter,

67 int \*status);

68dbus_bool_t \_dbus_babysitter_set_watch_functions (DBusBabysitter \*sitter,

69 DBusAddWatchFunction add_function,

70 DBusRemoveWatchFunction remove_function,

71 DBusWatchToggledFunction toggled_function,

72 void \*data,

73 DBusFreeFunction free_data_function);

74void \_dbus_babysitter_block_for_child_exit (DBusBabysitter \*sitter);

75

76DBUS_END_DECLS

77

78\#endif /\* DBUS_SPAWN_H \*/

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

\_dbus_babysitter_get_child_exit_status

dbus_bool_t \_dbus_babysitter_get_child_exit_status(DBusBabysitter \*sitter, int \*status)

Gets the exit status of the child.

**Definition** dbus-spawn-unix.c:753

\_dbus_babysitter_unref

void \_dbus_babysitter_unref(DBusBabysitter \*sitter)

Decrement the reference count on the babysitter object.

**Definition** dbus-spawn-unix.c:336

\_dbus_babysitter_get_child_exited

dbus_bool_t \_dbus_babysitter_get_child_exited(DBusBabysitter \*sitter)

Checks whether the child has exited, without blocking.

**Definition** dbus-spawn-unix.c:728

\_dbus_babysitter_set_watch_functions

dbus_bool_t \_dbus_babysitter_set_watch_functions(DBusBabysitter \*sitter, DBusAddWatchFunction add_function, DBusRemoveWatchFunction remove_function, DBusWatchToggledFunction toggled_function, void \*data, DBusFreeFunction free_data_function)

Sets watch functions to notify us when the babysitter object needs to read/write file descriptors.

**Definition** dbus-spawn-unix.c:835

\_dbus_babysitter_set_child_exit_error

void \_dbus_babysitter_set_child_exit_error(DBusBabysitter \*sitter, DBusError \*error)

Sets the DBusError with an explanation of why the spawned child process exited (on a signal,...

**Definition** dbus-spawn-unix.c:777

\_dbus_babysitter_kill_child

void \_dbus_babysitter_kill_child(DBusBabysitter \*sitter)

Blocks until the babysitter process gives us the PID of the spawned grandchild, then kills the spawne...

**Definition** dbus-spawn-unix.c:706

\_dbus_babysitter_ref

DBusBabysitter \* \_dbus_babysitter_ref(DBusBabysitter \*sitter)

Increment the reference count on the babysitter object.

**Definition** dbus-spawn-unix.c:314

\_dbus_spawn_async_with_babysitter

dbus_bool_t \_dbus_spawn_async_with_babysitter(DBusBabysitter \*\*sitter_p, const char \*log_name, char \*const \*argv, char \*const \*env, DBusSpawnFlags flags, DBusSpawnChildSetupFunc child_setup, void \*user_data, DBusError \*error)

Spawns a new process.

**Definition** dbus-spawn-unix.c:1279

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

DBusBabysitter

Babysitter implementation details.

**Definition** dbus-spawn-unix.c:252

DBusBabysitter::status

int status

Exit status code.

**Definition** dbus-spawn-unix.c:273

DBusBabysitter::log_name

char \* log_name

the name under which to log messages about this process being spawned

**Definition** dbus-spawn-unix.c:255

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51
