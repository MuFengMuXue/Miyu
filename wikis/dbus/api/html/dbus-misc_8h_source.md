dbus-misc.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-misc.h A few assorted public functions that don't fit elsewhere

3 \*

4 \* Copyright (C) 2006 Red Hat, Inc.

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

29\#ifndef DBUS_MISC_H

30\#define DBUS_MISC_H

31

32\#include \<dbus/dbus-types.h\>

33\#include \<dbus/dbus-errors.h\>

34

35DBUS_BEGIN_DECLS

36

41DBUS_EXPORT

42char\* dbus_get_local_machine_id (void);

43

44DBUS_EXPORT

45void dbus_get_version (int \*major_version_p,

46 int \*minor_version_p,

47 int \*micro_version_p);

48

49DBUS_EXPORT

50dbus_bool_t dbus_setenv (const char \*variable,

51 const char \*value);

52

53DBUS_EXPORT

54char \*dbus_try_get_local_machine_id (DBusError \*error);

55

58DBUS_END_DECLS

59

60\#endif /\* DBUS_MISC_H \*/

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

dbus_get_local_machine_id

char \* dbus_get_local_machine_id(void)

Obtains the machine UUID of the machine this process is running on.

**Definition** dbus-misc.c:125

dbus_try_get_local_machine_id

char \* dbus_try_get_local_machine_id(DBusError \*error)

Obtains the machine UUID of the machine this process is running on.

**Definition** dbus-misc.c:76

dbus_setenv

DBUS_EXPORT dbus_bool_t dbus_setenv(const char \*variable, const char \*value)

Wrapper for setenv().

**Definition** dbus-sysdeps.c:126

dbus_get_version

void dbus_get_version(int \*major_version_p, int \*minor_version_p, int \*micro_version_p)

Gets the DYNAMICALLY LINKED version of libdbus.

**Definition** dbus-misc.c:213

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51
