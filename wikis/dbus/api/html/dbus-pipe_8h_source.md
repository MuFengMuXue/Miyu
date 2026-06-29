dbus-pipe.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-sysdeps.h Wrappers around system/libc features (internal to D-Bus implementation)

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

27\#ifndef DBUS_PIPE_H

28\#define DBUS_PIPE_H

29

30\#include \<stdint.h\>

31

32\#ifdef HAVE_INTTYPES_H

33\#include \<inttypes.h\>

34\#endif

35

36\#include \<dbus/dbus-types.h\>

37\#include \<dbus/dbus-errors.h\>

38\#include \<dbus/dbus-string.h\>

39\#include \<dbus/dbus-sysdeps.h\>

40

41struct DBusPipe {

42 int fd;

43};

44

45DBUS_PRIVATE_EXPORT

46void \_dbus_pipe_init (DBusPipe \*pipe,

47 int fd);

48DBUS_PRIVATE_EXPORT

49void \_dbus_pipe_init_stdout (DBusPipe \*pipe);

50DBUS_PRIVATE_EXPORT

51int \_dbus_pipe_write (DBusPipe \*pipe,

52 const DBusString \*buffer,

53 int start,

54 int len,

55 DBusError \*error);

56DBUS_PRIVATE_EXPORT

57int \_dbus_pipe_close (DBusPipe \*pipe,

58 DBusError \*error);

59DBUS_PRIVATE_EXPORT

60dbus_bool_t \_dbus_pipe_is_valid (DBusPipe \*pipe);

61DBUS_PRIVATE_EXPORT

62void \_dbus_pipe_invalidate (DBusPipe \*pipe);

63DBUS_PRIVATE_EXPORT

64dbus_bool_t \_dbus_pipe_is_stdout_or_stderr (DBusPipe \*pipe);

65

66\#endif

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusPipe

**Definition** dbus-pipe.h:41

DBusString

**Definition** dbus-string.h:47
