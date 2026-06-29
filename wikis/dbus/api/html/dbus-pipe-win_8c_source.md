dbus-pipe-win.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-pipe-win.c windows related pipe implementation

3 \*

4 \* Copyright (C) 2002, 2003, 2006 Red Hat, Inc.

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

27\#include \<config.h\>

28\#include "dbus-protocol.h"

29\#include "dbus-string.h"

30\#include "dbus-internals.h"

31\#include "dbus-pipe.h"

32

33\#include \<windows.h\>

34\#include \<io.h\>

35

46int

47\_dbus_pipe_write (DBusPipe \*pipe,

48 const DBusString \*buffer,

49 int start,

50 int len,

51 DBusError \*error)

52{

53 const char \*buffer_c = \_dbus_string_get_const_data (buffer);

54 int written;

55

56 written = \_write (pipe-\>fd, buffer_c + start, len);

57

58 if (written \>= 0)

59 return written;

60

61 dbus_set_error (error, \_dbus_error_from_system_errno (),

62 "Writing to pipe: %s",

63 \_dbus_strerror_from_errno ());

64 return -1;

65}

66

74int

75\_dbus_pipe_close (DBusPipe \*pipe,

76 DBusError \*error)

77{

78 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

79

80 if (\_close (pipe-\>fd) != 0)

81 {

82 dbus_set_error (error, \_dbus_error_from_system_errno (),

83 "Could not close pipe fd %d: %s", pipe-\>fd,

84 \_dbus_strerror_from_errno ());

85 return -1;

86 }

87 else

88 {

89 \_dbus_pipe_invalidate (pipe);

90 return 0;

91 }

92}

dbus_set_error

void dbus_set_error(DBusError \*error, const char \*name, const char \*format,...)

Assigns an error name and message to a DBusError.

**Definition** dbus-errors.c:356

\_dbus_error_from_system_errno

const char \* \_dbus_error_from_system_errno(void)

Converts the current system errno value into a DBusError name.

**Definition** dbus-sysdeps.c:657

\_dbus_strerror_from_errno

const char \* \_dbus_strerror_from_errno(void)

Get error message from errno.

**Definition** dbus-sysdeps.c:724

\_dbus_string_get_const_data

const char \* \_dbus_string_get_const_data(const DBusString \*str)

Gets the raw character buffer from a const string.

**Definition** dbus-string.c:513

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusPipe

**Definition** dbus-pipe.h:41

DBusString

**Definition** dbus-string.h:47
