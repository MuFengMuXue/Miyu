dbus-string-util.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-string-util.c Would be in dbus-string.c, but not used in libdbus

3 \*

4 \* Copyright 2002-2008 Red Hat, Inc.

5 \* Copyright 2003 CodeFactory AB

6 \* Copyright 2003 Mark McLoughlin

7 \* Copyright 2004 Michael Meeks

8 \* Copyright 2006-2015 Ralf Habacker \<ralf.habacker@freenet.de\>

9 \* Copyright 2007 Allison Lortie

10 \* Copyright 2011 Roberto Guido

11 \* Copyright 2016-2018 Collabora Ltd.

12 \*

13 \* SPDX-License-Identifier: AFL-2.1 OR GPL-2.0-or-later

14 \*

15 \* Licensed under the Academic Free License version 2.1

16 \*

17 \* This program is free software; you can redistribute it and/or modify

18 \* it under the terms of the GNU General Public License as published by

19 \* the Free Software Foundation; either version 2 of the License, or

20 \* (at your option) any later version.

21 \*

22 \* This program is distributed in the hope that it will be useful,

23 \* but WITHOUT ANY WARRANTY; without even the implied warranty of

24 \* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the

25 \* GNU General Public License for more details.

26 \*

27 \* You should have received a copy of the GNU General Public License

28 \* along with this program; if not, write to the Free Software

29 \* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

30 \*

31 \*/

32

33\#include \<config.h\>

34\#include "dbus-internals.h"

35\#include "dbus-string.h"

36\#define DBUS_CAN_USE_DBUS_STRING_PRIVATE 1

37\#include "dbus-string-private.h"

38

53dbus_bool_t

54\_dbus_string_ends_with_c_str (const DBusString \*a,

55 const char \*c_str)

56{

57 const unsigned char \*ap;

58 const unsigned char \*bp;

59 const unsigned char \*a_end;

60 unsigned long c_str_len;

61 const DBusRealString \*real_a = (const DBusRealString\*) a;

62 DBUS_GENERIC_STRING_PREAMBLE (real_a);

63 \_dbus_assert (c_str != NULL);

64

65 c_str_len = strlen (c_str);

66 if (((unsigned long)real_a-\>len) \< c_str_len)

67 return FALSE;

68

69 ap = real_a-\>str + (real_a-\>len - c_str_len);

70 bp = (const unsigned char\*) c_str;

71 a_end = real_a-\>str + real_a-\>len;

72 while (ap != a_end)

73 {

74 if (\*ap != \*bp)

75 return FALSE;

76

77 ++ap;

78 ++bp;

79 }

80

81 \_dbus_assert (\*ap == '\0');

82 \_dbus_assert (\*bp == '\0');

83

84 return TRUE;

85}

86

97dbus_bool_t

98\_dbus_string_find_byte_backward (const DBusString \*str,

99 int start,

100 unsigned char byte,

101 int \*found)

102{

103 int i;

104 DBUS_CONST_STRING_PREAMBLE (str);

105 \_dbus_assert (start \<= real-\>len);

106 \_dbus_assert (start \>= 0);

107 \_dbus_assert (found != NULL);

108

109 i = start - 1;

110 while (i \>= 0)

111 {

112 if (real-\>str\[i\] == byte)

113 break;

114

115 --i;

116 }

117

118 if (found)

119 \*found = i;

120

121 return i \>= 0;

122}

123

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

NULL

\#define NULL

A null pointer, defined appropriately for C or C++.

**Definition** dbus-macros.h:51

TRUE

\#define TRUE

Expands to "1".

**Definition** dbus-macros.h:41

FALSE

\#define FALSE

Expands to "0".

**Definition** dbus-macros.h:44

DBUS_CONST_STRING_PREAMBLE

\#define DBUS_CONST_STRING_PREAMBLE(str)

Checks assertions about a string that may be const or locked.

**Definition** dbus-string-private.h:116

DBUS_GENERIC_STRING_PREAMBLE

\#define DBUS_GENERIC_STRING_PREAMBLE(real)

Checks a bunch of assertions about a string object.

**Definition** dbus-string-private.h:78

\_dbus_string_ends_with_c_str

dbus_bool_t \_dbus_string_ends_with_c_str(const DBusString \*a, const char \*c_str)

Returns whether a string ends with the given suffix.

**Definition** dbus-string-util.c:54

\_dbus_string_find_byte_backward

dbus_bool_t \_dbus_string_find_byte_backward(const DBusString \*str, int start, unsigned char byte, int \*found)

Find the given byte scanning backward from the given start.

**Definition** dbus-string-util.c:98

DBusRealString

Internals of DBusString.

**Definition** dbus-string-private.h:46

DBusRealString::str

unsigned char \* str

String data, plus nul termination.

**Definition** dbus-string-private.h:47

DBusRealString::len

int len

Length without nul.

**Definition** dbus-string-private.h:48

DBusString

**Definition** dbus-string.h:47
