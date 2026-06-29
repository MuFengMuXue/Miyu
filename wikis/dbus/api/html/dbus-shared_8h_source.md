dbus-shared.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-shared.h Stuff used by both dbus/dbus.h low-level and C/C++ binding APIs

3 \*

4 \* Copyright (C) 2004 Red Hat, Inc.

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

26\#ifndef DBUS_SHARED_H

27\#define DBUS_SHARED_H

28

29/\* Don't include anything in here from anywhere else. It's

30 \* intended for use by any random library.

31 \*/

32

33\#ifdef \_\_cplusplus

34extern "C" {

35\#if 0

36} /\* avoids confusing emacs indentation \*/

37\#endif

38\#endif

39

40/\* Normally docs are in .c files, but there isn't a .c file for this. \*/

58typedef enum

59{

60 DBUS_BUS_SESSION,

61 DBUS_BUS_SYSTEM,

62 DBUS_BUS_STARTER

63} DBusBusType;

64

68typedef enum

69{

70 DBUS_HANDLER_RESULT_HANDLED,

71 DBUS_HANDLER_RESULT_NOT_YET_HANDLED,

72 DBUS_HANDLER_RESULT_NEED_MEMORY

73} DBusHandlerResult;

74

75/\* Bus names \*/

76

78\#define DBUS_SERVICE_DBUS "org.freedesktop.DBus"

79

80/\* Paths \*/

82\#define DBUS_PATH_DBUS "/org/freedesktop/DBus"

84\#define DBUS_PATH_LOCAL "/org/freedesktop/DBus/Local"

85

86/\* Interfaces, these \#define don't do much other than

87 \* catch typos at compile time

88 \*/

90\#define DBUS_INTERFACE_DBUS "org.freedesktop.DBus"

92\#define DBUS_INTERFACE_MONITORING "org.freedesktop.DBus.Monitoring"

93

95\#define DBUS_INTERFACE_VERBOSE "org.freedesktop.DBus.Verbose"

97\#define DBUS_INTERFACE_INTROSPECTABLE "org.freedesktop.DBus.Introspectable"

99\#define DBUS_INTERFACE_PROPERTIES "org.freedesktop.DBus.Properties"

101\#define DBUS_INTERFACE_PEER "org.freedesktop.DBus.Peer"

102

107\#define DBUS_INTERFACE_LOCAL "org.freedesktop.DBus.Local"

108

109/\* Owner flags \*/

110\#define DBUS_NAME_FLAG_ALLOW_REPLACEMENT 0x1

111\#define DBUS_NAME_FLAG_REPLACE_EXISTING 0x2

112\#define DBUS_NAME_FLAG_DO_NOT_QUEUE 0x4

114/\* Replies to request for a name \*/

115\#define DBUS_REQUEST_NAME_REPLY_PRIMARY_OWNER 1

116\#define DBUS_REQUEST_NAME_REPLY_IN_QUEUE 2

117\#define DBUS_REQUEST_NAME_REPLY_EXISTS 3

118\#define DBUS_REQUEST_NAME_REPLY_ALREADY_OWNER 4

120/\* Replies to releasing a name \*/

121\#define DBUS_RELEASE_NAME_REPLY_RELEASED 1

122\#define DBUS_RELEASE_NAME_REPLY_NON_EXISTENT 2

123\#define DBUS_RELEASE_NAME_REPLY_NOT_OWNER 3

125/\* Replies to service starts \*/

126\#define DBUS_START_REPLY_SUCCESS 1

127\#define DBUS_START_REPLY_ALREADY_RUNNING 2

131\#ifdef \_\_cplusplus

132\#if 0

133{ /\* avoids confusing emacs indentation \*/

134\#endif

135}

136\#endif

137

138\#endif /\* DBUS_SHARED_H \*/

DBusHandlerResult

DBusHandlerResult

Results that a message handler can return.

**Definition** dbus-shared.h:69

DBusBusType

DBusBusType

Well-known bus types.

**Definition** dbus-shared.h:59

DBUS_HANDLER_RESULT_NEED_MEMORY

@ DBUS_HANDLER_RESULT_NEED_MEMORY

Need more memory in order to return DBUS_HANDLER_RESULT_HANDLED or DBUS_HANDLER_RESULT_NOT_YET_HANDLE...

**Definition** dbus-shared.h:72

DBUS_HANDLER_RESULT_HANDLED

@ DBUS_HANDLER_RESULT_HANDLED

Message has had its effect - no need to run more handlers.

**Definition** dbus-shared.h:70

DBUS_HANDLER_RESULT_NOT_YET_HANDLED

@ DBUS_HANDLER_RESULT_NOT_YET_HANDLED

Message has not had any effect - see if other handlers want it.

**Definition** dbus-shared.h:71

DBUS_BUS_SESSION

@ DBUS_BUS_SESSION

The login session bus.

**Definition** dbus-shared.h:60

DBUS_BUS_STARTER

@ DBUS_BUS_STARTER

The bus that started us, if any.

**Definition** dbus-shared.h:62

DBUS_BUS_SYSTEM

@ DBUS_BUS_SYSTEM

The systemwide bus.

**Definition** dbus-shared.h:61
