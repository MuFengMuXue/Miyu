dbus-memory.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-memory.h D-Bus memory handling

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

25\#if !defined (DBUS_INSIDE_DBUS_H) && !defined (DBUS_COMPILATION)

26\#error "Only \<dbus/dbus.h\> can be included directly, this file may disappear or change contents."

27\#endif

28

29\#ifndef DBUS_MEMORY_H

30\#define DBUS_MEMORY_H

31

32\#include \<dbus/dbus-macros.h\>

33\#include \<stddef.h\>

34

35DBUS_BEGIN_DECLS

36

42DBUS_EXPORT

43DBUS_MALLOC

44DBUS_ALLOC_SIZE(1)

45void\* dbus_malloc (size_t bytes);

46

47DBUS_EXPORT

48DBUS_MALLOC

49DBUS_ALLOC_SIZE(1)

50void\* dbus_malloc0 (size_t bytes);

51

52DBUS_EXPORT

53DBUS_ALLOC_SIZE(2)

54void\* dbus_realloc (void \*memory,

55 size_t bytes);

56DBUS_EXPORT

57void dbus_free (void \*memory);

58

59\#define dbus_new(type, count) ((type\*)dbus_malloc (sizeof (type) \* (count)))

60\#define dbus_new0(type, count) ((type\*)dbus_malloc0 (sizeof (type) \* (count)))

61

62DBUS_EXPORT

63void dbus_free_string_array (char \*\*str_array);

64

65typedef void (\* DBusFreeFunction) (void \*memory);

66

67DBUS_EXPORT

68void dbus_shutdown (void);

69

72DBUS_END_DECLS

73

74\#endif /\* DBUS_MEMORY_H \*/

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

dbus_shutdown

void dbus_shutdown(void)

Frees all memory allocated internally by libdbus and reverses the effects of dbus_threads_init().

**Definition** dbus-memory.c:906

DBusFreeFunction

void(\* DBusFreeFunction)(void \*memory)

The type of a function which frees a block of memory.

**Definition** dbus-memory.h:65

dbus_free

void dbus_free(void \*memory)

Frees a block of memory previously allocated by dbus_malloc() or dbus_malloc0().

**Definition** dbus-memory.c:710

dbus_realloc

void \* dbus_realloc(void \*memory, size_t bytes)

Resizes a block of memory previously allocated by dbus_malloc() or dbus_malloc0().

**Definition** dbus-memory.c:610

dbus_malloc0

void \* dbus_malloc0(size_t bytes)

Allocates the given number of bytes, as with standard malloc(), but all bytes are initialized to zero...

**Definition** dbus-memory.c:540

dbus_free_string_array

void dbus_free_string_array(char \*\*str_array)

Frees a NULL-terminated array of strings.

**Definition** dbus-memory.c:758

dbus_malloc

void \* dbus_malloc(size_t bytes)

Allocates the given number of bytes, as with standard malloc().

**Definition** dbus-memory.c:470
