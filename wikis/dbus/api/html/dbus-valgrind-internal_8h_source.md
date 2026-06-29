dbus-valgrind-internal.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-valgrind-internal.h - valgrind glue

3 \*

4 \* Copyright © 2011 Nokia Corporation

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

22 \* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA

23 \* 02110-1301 USA

24 \*

25 \*/

26

27\#ifndef DBUS_VALGRIND_INTERNAL_H

28\#define DBUS_VALGRIND_INTERNAL_H

29

30\#include "config.h"

31\#include "dbus-internals.h"

32

33\#ifdef WITH_VALGRIND

34\# include \<memcheck.h\>

35\# include \<valgrind.h\>

36\#else

37\# define VALGRIND_CREATE_MEMPOOL(\_1, \_2, \_3) do { } while (0)

38\# define VALGRIND_DESTROY_MEMPOOL(\_1) do { } while (0)

39\# define VALGRIND_MEMPOOL_ALLOC(\_1, \_2, \_3) do { } while (0)

40\# define VALGRIND_MEMPOOL_FREE(\_1, \_2) do { } while (0)

41

42/\* Recent gcc will warn if you have a statement that's just a macro

43 \* expanding to (0), but not if you have an inline stub function that

44 \* always returns 0, so let's do the latter. \*/

45static inline int

46VALGRIND_MAKE_MEM_UNDEFINED (void \*addr,

47 size_t len)

48{

49 return 0;

50}

51

52static inline int

53VALGRIND_PRINTF (const char \*format,

54 ...)

55{

56 return 0;

57}

58

59static inline int

60VALGRIND_PRINTF_BACKTRACE (const char \*format,

61 ...)

62{

63 return 0;

64}

65

66\# define RUNNING_ON_VALGRIND 0

67\#endif /\* WITH_VALGRIND \*/

68

69\#endif /\* header guard \*/
