dbus-errors.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-errors.h Error reporting

3 \*

4 \* Copyright (C) 2002 Red Hat Inc.

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

26\#if !defined (DBUS_INSIDE_DBUS_H) && !defined (DBUS_COMPILATION)

27\#error "Only \<dbus/dbus.h\> can be included directly, this file may disappear or change contents."

28\#endif

29

30\#ifndef DBUS_ERROR_H

31\#define DBUS_ERROR_H

32

33\#include \<dbus/dbus-macros.h\>

34\#include \<dbus/dbus-types.h\>

35\#include \<dbus/dbus-protocol.h\>

36

37DBUS_BEGIN_DECLS

38

45typedef struct DBusError DBusError;

46

50struct DBusError

51{

52 const char \*name;

53 const char \*message;

55 unsigned int dummy1 : 1;

56 unsigned int dummy2 : 1;

57 unsigned int dummy3 : 1;

58 unsigned int dummy4 : 1;

59 unsigned int dummy5 : 1;

61 void \*padding1;

62};

63

64\#define DBUS_ERROR_INIT { NULL, NULL, TRUE, 0, 0, 0, 0, NULL }

65

66DBUS_EXPORT

67void dbus_error_init (DBusError \*error);

68DBUS_EXPORT

69void dbus_error_free (DBusError \*error);

70DBUS_EXPORT

71void dbus_set_error (DBusError \*error,

72 const char \*name,

73 const char \*message,

74 ...) \_DBUS_GNUC_PRINTF (3, 4);

75DBUS_EXPORT

76void dbus_set_error_const (DBusError \*error,

77 const char \*name,

78 const char \*message);

79DBUS_EXPORT

80void dbus_move_error (DBusError \*src,

81 DBusError \*dest);

82DBUS_EXPORT

83dbus_bool_t dbus_error_has_name (const DBusError \*error,

84 const char \*name);

85DBUS_EXPORT

86dbus_bool_t dbus_error_is_set (const DBusError \*error);

87

90DBUS_END_DECLS

91

92\#endif /\* DBUS_ERROR_H \*/

dbus_move_error

void dbus_move_error(DBusError \*src, DBusError \*dest)

Moves an error src into dest, freeing src and overwriting dest.

**Definition** dbus-errors.c:281

dbus_set_error_const

void dbus_set_error_const(DBusError \*error, const char \*name, const char \*message)

Assigns an error name and message to a DBusError.

**Definition** dbus-errors.c:245

dbus_error_has_name

dbus_bool_t dbus_error_has_name(const DBusError \*error, const char \*name)

Checks whether the error is set and has the given name.

**Definition** dbus-errors.c:304

dbus_error_init

void dbus_error_init(DBusError \*error)

Initializes a DBusError structure.

**Definition** dbus-errors.c:190

dbus_set_error

void dbus_set_error(DBusError \*error, const char \*name, const char \*format,...)

Assigns an error name and message to a DBusError.

**Definition** dbus-errors.c:356

dbus_error_free

void dbus_error_free(DBusError \*error)

Frees an error that's been set (or just initialized), then reinitializes the error as in dbus_error_i...

**Definition** dbus-errors.c:213

dbus_error_is_set

dbus_bool_t dbus_error_is_set(const DBusError \*error)

Checks whether an error occurred (the error is set).

**Definition** dbus-errors.c:331

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusError::name

const char \* name

public error name field

**Definition** dbus-errors.h:52

DBusError::dummy2

unsigned int dummy2

placeholder

**Definition** dbus-errors.h:56

DBusError::dummy4

unsigned int dummy4

placeholder

**Definition** dbus-errors.h:58

DBusError::dummy3

unsigned int dummy3

placeholder

**Definition** dbus-errors.h:57

DBusError::dummy5

unsigned int dummy5

placeholder

**Definition** dbus-errors.h:59

DBusError::dummy1

unsigned int dummy1

placeholder

**Definition** dbus-errors.h:55

DBusError::padding1

void \* padding1

placeholder

**Definition** dbus-errors.h:61

DBusError::message

const char \* message

public error message field

**Definition** dbus-errors.h:53
