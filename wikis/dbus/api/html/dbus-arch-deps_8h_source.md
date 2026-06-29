dbus-arch-deps.h

1/\* -\*- mode: C; c-file-style: "gnu" -\*- \*/

2/\* dbus-arch-deps.h Header with architecture/compiler specific information, installed to libdir

3 \*

4 \* Copyright (C) 2003 Red Hat, Inc.

5 \* SPDX-License-Identifier: AFL-2.0 OR GPL-2.0-or-later

6 \*

7 \* Licensed under the Academic Free License version 2.0

8 \*

9 \* This program is free software; you can redistribute it and/or modify

10 \* it under the terms of the GNU General Public License as published by

11 \* the Free Software Foundation; either version 2 of the License, or

12 \* (at your option) any later version.

13 \*

14 \* This program is distributed in the hope that it will be useful,

15 \* but WITHOUT ANY WARRANTY; without even the implied warranty of

16 \* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the

17 \* GNU General Public License for more details.

18 \*

19 \* You should have received a copy of the GNU General Public License

20 \* along with this program; if not, write to the Free Software

21 \* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

22 \*

23 \*/

24\#if !defined (DBUS_INSIDE_DBUS_H) && !defined (DBUS_COMPILATION)

25\#error "Only \<dbus/dbus.h\> can be included directly, this file may disappear or change contents."

26\#endif

27

28\#ifndef DBUS_ARCH_DEPS_H

29\#define DBUS_ARCH_DEPS_H

30

31\#include \<dbus/dbus-macros.h\>

32

33DBUS_BEGIN_DECLS

34

35/\* D-Bus no longer supports platforms with no 64-bit integer type. \*/

36\#define DBUS_HAVE_INT64 1

37\_DBUS_GNUC_EXTENSION typedef long dbus_int64_t;

38\_DBUS_GNUC_EXTENSION typedef unsigned long dbus_uint64_t;

39\#define DBUS_INT64_MODIFIER "l"

40

41\#define DBUS_INT64_CONSTANT(val) (\_DBUS_GNUC_EXTENSION (val##L))

42\#define DBUS_UINT64_CONSTANT(val) (\_DBUS_GNUC_EXTENSION (val##UL))

43

44typedef int dbus_int32_t;

45typedef unsigned int dbus_uint32_t;

46

47typedef short dbus_int16_t;

48typedef unsigned short dbus_uint16_t;

49

50\#define DBUS_SIZEOF_VOID_P 8

51

52/\* This is not really arch-dependent, but it's not worth

53 \* creating an additional generated header just for this

54 \*/

55\#define DBUS_MAJOR_VERSION 1

56\#define DBUS_MINOR_VERSION 16

57\#define DBUS_MICRO_VERSION 2

58

59\#define DBUS_VERSION_STRING "1.16.2"

60

61\#define DBUS_VERSION ((1 \<\< 16) \| (16 \<\< 8) \| (2))

62

63DBUS_END_DECLS

64

65\#endif /\* DBUS_ARCH_DEPS_H \*/

\_DBUS_GNUC_EXTENSION

\#define \_DBUS_GNUC_EXTENSION

Tells gcc not to warn about extensions to the C standard in the following expression,...

**Definition** dbus-macros.h:66

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37
