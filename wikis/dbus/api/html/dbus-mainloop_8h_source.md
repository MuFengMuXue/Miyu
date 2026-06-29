dbus-mainloop.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-mainloop.h Main loop utility

3 \*

4 \* Copyright (C) 2003 Red Hat, Inc.

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

26\#ifndef DBUS_MAINLOOP_H

27\#define DBUS_MAINLOOP_H

28

29\#ifndef DOXYGEN_SHOULD_SKIP_THIS

30

31\#include \<dbus/dbus.h\>

32

33typedef struct DBusLoop DBusLoop;

34

35typedef dbus_bool_t (\* DBusWatchFunction) (DBusWatch \*watch,

36 unsigned int condition,

37 void \*data);

38

39DBusLoop\* \_dbus_loop_new (void);

40DBusLoop\* \_dbus_loop_ref (DBusLoop \*loop);

41void \_dbus_loop_unref (DBusLoop \*loop);

42dbus_bool_t \_dbus_loop_add_watch (DBusLoop \*loop,

43 DBusWatch \*watch);

44void \_dbus_loop_remove_watch (DBusLoop \*loop,

45 DBusWatch \*watch);

46void \_dbus_loop_toggle_watch (DBusLoop \*loop,

47 DBusWatch \*watch);

48dbus_bool_t \_dbus_loop_add_timeout (DBusLoop \*loop,

49 DBusTimeout \*timeout);

50void \_dbus_loop_remove_timeout (DBusLoop \*loop,

51 DBusTimeout \*timeout);

52

53dbus_bool_t \_dbus_loop_queue_dispatch (DBusLoop \*loop,

54 DBusConnection \*connection);

55

56void \_dbus_loop_run (DBusLoop \*loop);

57void \_dbus_loop_quit (DBusLoop \*loop);

58dbus_bool_t \_dbus_loop_iterate (DBusLoop \*loop,

59 dbus_bool_t block);

60dbus_bool_t \_dbus_loop_dispatch (DBusLoop \*loop);

61

62int \_dbus_get_oom_wait (void);

63void \_dbus_wait_for_memory (void);

64

65static inline void

66\_dbus_clear_loop (DBusLoop \*\*pointer_to_loop)

67{

68 \_dbus_clear_pointer_impl (DBusLoop, pointer_to_loop,

69 \_dbus_loop_unref);

70}

71

72\#endif /\* !DOXYGEN_SHOULD_SKIP_THIS \*/

73

74\#endif /\* DBUS_MAINLOOP_H \*/

DBusConnection

Implementation details of DBusConnection.

**Definition** dbus-connection.c:259

DBusTimeout

Internals of DBusTimeout.

**Definition** dbus-timeout.c:43

DBusWatch

Implementation of DBusWatch.

**Definition** dbus-watch.c:43
