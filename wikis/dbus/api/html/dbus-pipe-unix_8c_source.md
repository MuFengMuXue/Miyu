dbus-pipe-unix.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-pipe-unix.c unix related pipe implementation

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

32\#include "dbus-sysdeps-unix.h"

33

34\#include \<errno.h\>

35

46int

47\_dbus_pipe_write (DBusPipe \*pipe,

48 const DBusString \*buffer,

49 int start,

50 int len,

51 DBusError \*error)

52{

53 int written;

54

55 written = \_dbus_write (pipe-\>fd, buffer, start, len);

56 if (written \< 0)

57 {

58 dbus_set_error (error, DBUS_ERROR_FAILED,

59 "Writing to pipe: %s\n",

60 \_dbus_strerror (errno));

61 }

62 return written;

63}

64

72int

73\_dbus_pipe_close (DBusPipe \*pipe,

74 DBusError \*error)

75{

76 if (!\_dbus_close (pipe-\>fd, error))

77 {

78 return -1;

79 }

80 else

81 {

82 \_dbus_pipe_invalidate (pipe);

83 return 0;

84 }

85}

dbus_set_error

void dbus_set_error(DBusError \*error, const char \*name, const char \*format,...)

Assigns an error name and message to a DBusError.

**Definition** dbus-errors.c:356

DBUS_ERROR_FAILED

\#define DBUS_ERROR_FAILED

A generic error; "something went wrong" - see the error message for more.

**Definition** dbus-protocol.h:361

\_dbus_close

dbus_bool_t \_dbus_close(int fd, DBusError \*error)

Closes a file descriptor.

**Definition** dbus-sysdeps-unix.c:3727

\_dbus_write

int \_dbus_write(int fd, const DBusString \*buffer, int start, int len)

Thin wrapper around the write() system call that writes a part of a DBusString and handles EINTR for ...

**Definition** dbus-sysdeps-unix.c:827

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusPipe

**Definition** dbus-pipe.h:41

DBusString

**Definition** dbus-string.h:47
