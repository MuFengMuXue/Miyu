dbus-sysdeps-util.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-sysdeps-util.c Tests for dbus-sysdeps.h API

3 \*

4 \* Copyright 2002-2008 Red Hat, Inc.

5 \* Copyright 2003 CodeFactory AB

6 \* Copyright 2006 Ralf Habacker

7 \* Copyright 2006 Sjoerd Simons

8 \* Copyright 2016-2018 Collabora Ltd.

9 \*

10 \* SPDX-License-Identifier: AFL-2.1 OR GPL-2.0-or-later

11 \*

12 \* Licensed under the Academic Free License version 2.1

13 \*

14 \* This program is free software; you can redistribute it and/or modify

15 \* it under the terms of the GNU General Public License as published by

16 \* the Free Software Foundation; either version 2 of the License, or

17 \* (at your option) any later version.

18 \*

19 \* This program is distributed in the hope that it will be useful,

20 \* but WITHOUT ANY WARRANTY; without even the implied warranty of

21 \* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the

22 \* GNU General Public License for more details.

23 \*

24 \* You should have received a copy of the GNU General Public License

25 \* along with this program; if not, write to the Free Software

26 \* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

27 \*

28 \*/

29

30\#include \<config.h\>

31\#include "dbus-sysdeps.h"

32\#include "dbus-internals.h"

33\#include "dbus-string.h"

34

35\#include \<stdlib.h\>

36

37\#ifdef DBUS_WIN

38 /\* do nothing, it's in stdlib.h \*/

39\#elif (defined \_\_APPLE\_\_)

40\# include \<crt_externs.h\>

41\# define environ (\*\_NSGetEnviron())

42\#elif HAVE_DECL_ENVIRON && defined(HAVE_UNISTD_H)

43\# include \<unistd.h\>

44\#else

45extern char \*\*environ;

46\#endif

47

54char \*\*

55\_dbus_get_environment (void)

56{

57 int i, length;

58 char \*\*environment;

59

60 \_dbus_assert (environ != NULL);

61

62 for (length = 0; environ\[length\] != NULL; length++);

63

64 /\* Add one for NULL \*/

65 length++;

66

67 environment = dbus_new0 (char \*, length);

68

69 if (environment == NULL)

70 return NULL;

71

72 for (i = 0; environ\[i\] != NULL; i++)

73 {

74 environment\[i\] = \_dbus_strdup (environ\[i\]);

75

76 if (environment\[i\] == NULL)

77 break;

78 }

79

80 if (environ\[i\] != NULL)

81 {

82 dbus_free_string_array (environment);

83 environment = NULL;

84 }

85

86 return environment;

87}

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_dbus_strdup

char \* \_dbus_strdup(const char \*str)

Duplicates a string.

**Definition** dbus-internals.c:621

NULL

\#define NULL

A null pointer, defined appropriately for C or C++.

**Definition** dbus-macros.h:51

dbus_new0

\#define dbus_new0(type, count)

Safe macro for using dbus_malloc0().

**Definition** dbus-memory.h:60

dbus_free_string_array

void dbus_free_string_array(char \*\*str_array)

Frees a NULL-terminated array of strings.

**Definition** dbus-memory.c:758

\_dbus_get_environment

char \*\* \_dbus_get_environment(void)

Gets a NULL-terminated list of key=value pairs from the environment.

**Definition** dbus-sysdeps-util.c:55
