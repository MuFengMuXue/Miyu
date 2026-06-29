dbus-string-private.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-string-private.h String utility class (internal to D-Bus implementation)

3 \*

4 \* Copyright (C) 2002, 2003 Red Hat, Inc.

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

25

26\#ifndef DBUS_STRING_PRIVATE_H

27\#define DBUS_STRING_PRIVATE_H

28

29\#include \<dbus/dbus-internals.h\>

30\#include \<dbus/dbus-memory.h\>

31\#include \<dbus/dbus-types.h\>

32

33\#ifndef DBUS_CAN_USE_DBUS_STRING_PRIVATE

34\#error "Don't go including dbus-string-private.h for no good reason"

35\#endif

36

37DBUS_BEGIN_DECLS

38

45typedef struct

46{

47 unsigned char \*str;

48 int len;

49 int allocated;

50 unsigned int constant : 1;

51 unsigned int locked : 1;

52 unsigned int valid : 1;

53 unsigned int align_offset : 3;

54} DBusRealString;

55

56\_DBUS_STATIC_ASSERT (sizeof (DBusRealString) == sizeof (DBusString));

57

71\#define \_DBUS_STRING_MAX_LENGTH (\_DBUS_INT32_MAX - \_DBUS_STRING_ALLOCATION_PADDING)

72

78\#define DBUS_GENERIC_STRING_PREAMBLE(real) \\

79 do { \\

80 (void) real; /\* might be unused unless asserting \*/ \\

81 \_dbus_assert ((real) != NULL); \\

82 \_dbus_assert ((real)-\>valid); \\

83 \_dbus_assert ((real)-\>len \>= 0); \\

84 \_dbus_assert ((real)-\>allocated \>= 0); \\

85 \_dbus_assert ((real)-\>len \<= ((real)-\>allocated - \_DBUS_STRING_ALLOCATION_PADDING)); \\

86 \_dbus_assert ((real)-\>len \<= \_DBUS_STRING_MAX_LENGTH); \\

87 } while (0)

88

95\#define DBUS_STRING_PREAMBLE(str) DBusRealString \*real = (DBusRealString\*) str; \\

96 DBUS_GENERIC_STRING_PREAMBLE (real); \\

97 \_dbus_assert (!(real)-\>constant); \\

98 \_dbus_assert (!(real)-\>locked)

99

107\#define DBUS_LOCKED_STRING_PREAMBLE(str) DBusRealString \*real = (DBusRealString\*) str; \\

108 DBUS_GENERIC_STRING_PREAMBLE (real); \\

109 \_dbus_assert (!(real)-\>constant)

110

116\#define DBUS_CONST_STRING_PREAMBLE(str) const DBusRealString \*real = (DBusRealString\*) str; \\

117 DBUS_GENERIC_STRING_PREAMBLE (real)

118

123\#define DBUS_IS_ASCII_BLANK(c) ((c) == ' ' \|\| (c) == '\t')

124

129\#define DBUS_IS_ASCII_WHITE(c) ((c) == ' ' \|\| (c) == '\t' \|\| (c) == '\n' \|\| (c) == '\r')

130

133DBUS_END_DECLS

134

135\#endif /\* DBUS_STRING_PRIVATE_H \*/

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

DBusRealString

Internals of DBusString.

**Definition** dbus-string-private.h:46

DBusRealString::align_offset

unsigned int align_offset

str - align_offset is the actual malloc block

**Definition** dbus-string-private.h:53

DBusRealString::valid

unsigned int valid

DBusString is valid (initialized and not freed)

**Definition** dbus-string-private.h:52

DBusRealString::constant

unsigned int constant

String data is not owned by DBusString.

**Definition** dbus-string-private.h:50

DBusRealString::locked

unsigned int locked

DBusString has been locked and can't be changed.

**Definition** dbus-string-private.h:51

DBusRealString::str

unsigned char \* str

String data, plus nul termination.

**Definition** dbus-string-private.h:47

DBusRealString::allocated

int allocated

Allocated size of data.

**Definition** dbus-string-private.h:49

DBusRealString::len

int len

Length without nul.

**Definition** dbus-string-private.h:48

DBusString

**Definition** dbus-string.h:47
