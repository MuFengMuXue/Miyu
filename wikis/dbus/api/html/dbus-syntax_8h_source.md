dbus-syntax.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-syntax.h - utility functions for strings with special syntax

3 \*

4 \* Author: Simon McVittie \<simon.mcvittie@collabora.co.uk\>

5 \* Copyright © 2011 Nokia Corporation

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

26\#if !defined (DBUS_INSIDE_DBUS_H) && !defined (DBUS_COMPILATION)

27\#error "Only \<dbus/dbus.h\> can be included directly, this file may disappear or change contents."

28\#endif

29

30\#ifndef DBUS_SYNTAX_H

31\#define DBUS_SYNTAX_H

32

33\#include \<dbus/dbus-macros.h\>

34\#include \<dbus/dbus-types.h\>

35\#include \<dbus/dbus-errors.h\>

36

37DBUS_BEGIN_DECLS

38

39DBUS_EXPORT

40dbus_bool_t dbus_validate_path (const char \*path,

41 DBusError \*error);

42DBUS_EXPORT

43dbus_bool_t dbus_validate_interface (const char \*name,

44 DBusError \*error);

45DBUS_EXPORT

46dbus_bool_t dbus_validate_member (const char \*name,

47 DBusError \*error);

48DBUS_EXPORT

49dbus_bool_t dbus_validate_error_name (const char \*name,

50 DBusError \*error);

51DBUS_EXPORT

52dbus_bool_t dbus_validate_bus_name (const char \*name,

53 DBusError \*error);

54DBUS_EXPORT

55dbus_bool_t dbus_validate_utf8 (const char \*alleged_utf8,

56 DBusError \*error);

57

58DBUS_END_DECLS

59

60\#endif /\* multiple-inclusion guard \*/

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

dbus_validate_interface

DBUS_EXPORT dbus_bool_t dbus_validate_interface(const char \*name, DBusError \*error)

Check an interface name for validity.

**Definition** dbus-syntax.c:103

dbus_validate_path

DBUS_EXPORT dbus_bool_t dbus_validate_path(const char \*path, DBusError \*error)

Check an object path for validity.

**Definition** dbus-syntax.c:56

dbus_validate_utf8

DBUS_EXPORT dbus_bool_t dbus_validate_utf8(const char \*alleged_utf8, DBusError \*error)

Check a string for validity.

**Definition** dbus-syntax.c:291

dbus_validate_member

DBUS_EXPORT dbus_bool_t dbus_validate_member(const char \*name, DBusError \*error)

Check a member (method/signal) name for validity.

**Definition** dbus-syntax.c:150

dbus_validate_bus_name

DBUS_EXPORT dbus_bool_t dbus_validate_bus_name(const char \*name, DBusError \*error)

Check a bus name for validity.

**Definition** dbus-syntax.c:244

dbus_validate_error_name

DBUS_EXPORT dbus_bool_t dbus_validate_error_name(const char \*name, DBusError \*error)

Check an error name for validity.

**Definition** dbus-syntax.c:197

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51
