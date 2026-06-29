dbus-pipe.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-pipe.c pipe implementation (internal to D-Bus implementation)

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

28\#include "dbus-pipe.h"

29

30/\*

31 \* init a pipe instance.

32 \*

33 \* @param pipe the pipe

34 \* @param fd the file descriptor to init from

35 \*/

36void

37\_dbus_pipe_init (DBusPipe \*pipe,

38 int fd)

39{

40 pipe-\>fd = fd;

41}

42

48void

49\_dbus_pipe_init_stdout (DBusPipe \*pipe)

50{

51 \_dbus_pipe_init (pipe, 1);

52}

53

61dbus_bool_t

62\_dbus_pipe_is_valid(DBusPipe \*pipe)

63{

64 return pipe-\>fd \>= 0;

65}

66

73dbus_bool_t

74\_dbus_pipe_is_stdout_or_stderr (DBusPipe \*pipe)

75{

76 return pipe-\>fd == 1 \|\| pipe-\>fd == 2;

77}

78

83void

84\_dbus_pipe_invalidate (DBusPipe \*pipe)

85{

86 pipe-\>fd = -1;

87}

DBusPipe

**Definition** dbus-pipe.h:41
