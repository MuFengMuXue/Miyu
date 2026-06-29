dbus-pollable-set.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\*

3 \* dbus-pollable-set.h - a set of pollable objects (file descriptors, sockets or handles)

4 \*

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

23 \* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,

24 \* MA 02110-1301 USA

25 \*

26 \*/

27

28\#ifndef DBUS_POLLABLE_SET_H

29\#define DBUS_POLLABLE_SET_H

30

31\#ifndef DOXYGEN_SHOULD_SKIP_THIS

32

33\#include \<dbus/dbus.h\>

34\#include \<dbus/dbus-sysdeps.h\>

35

36typedef struct {

37 DBusPollable fd;

38 unsigned int flags;

39} DBusPollableEvent;

40

41typedef struct DBusPollableSet DBusPollableSet;

42

43typedef struct DBusPollableSetClass DBusPollableSetClass;

44struct DBusPollableSetClass {

45 void (\*free) (DBusPollableSet \*self);

46 dbus_bool_t (\*add) (DBusPollableSet \*self,

47 DBusPollable fd,

48 unsigned int flags,

49 dbus_bool_t enabled);

50 void (\*remove) (DBusPollableSet \*self,

51 DBusPollable fd);

52 void (\*enable) (DBusPollableSet \*self,

53 DBusPollable fd,

54 unsigned int flags);

55 void (\*disable) (DBusPollableSet \*self,

56 DBusPollable fd);

57 int (\*poll) (DBusPollableSet \*self,

58 DBusPollableEvent \*revents,

59 int max_events,

60 int timeout_ms);

61};

62

63struct DBusPollableSet {

64 DBusPollableSetClass \*cls;

65};

66

67DBusPollableSet \*\_dbus_pollable_set_new (int size_hint);

68

69static inline void

70\_dbus_pollable_set_free (DBusPollableSet \*self)

71{

72 (self-\>cls-\>free) (self);

73}

74

75static inline dbus_bool_t

76\_dbus_pollable_set_add (DBusPollableSet \*self,

77 DBusPollable fd,

78 unsigned int flags,

79 dbus_bool_t enabled)

80{

81 return (self-\>cls-\>add) (self, fd, flags, enabled);

82}

83

84static inline void

85\_dbus_pollable_set_remove (DBusPollableSet \*self,

86 DBusPollable fd)

87{

88 (self-\>cls-\>remove) (self, fd);

89}

90

91static inline void

92\_dbus_pollable_set_enable (DBusPollableSet \*self,

93 DBusPollable fd,

94 unsigned int flags)

95{

96 (self-\>cls-\>enable) (self, fd, flags);

97}

98

99static inline void

100\_dbus_pollable_set_disable (DBusPollableSet \*self,

101 DBusPollable fd)

102{

103 (self-\>cls-\>disable) (self, fd);

104}

105

106

107static inline int

108\_dbus_pollable_set_poll (DBusPollableSet \*self,

109 DBusPollableEvent \*revents,

110 int max_events,

111 int timeout_ms)

112{

113 return (self-\>cls-\>poll) (self, revents, max_events, timeout_ms);

114}

115

116/\* concrete implementations, not necessarily built on all platforms \*/

117

118extern DBusPollableSetClass \_dbus_pollable_set_poll_class;

119extern DBusPollableSetClass \_dbus_pollable_set_epoll_class;

120

121DBusPollableSet \*\_dbus_pollable_set_poll_new (int size_hint);

122DBusPollableSet \*\_dbus_pollable_set_epoll_new (void);

123

124\#endif /\* !DOXYGEN_SHOULD_SKIP_THIS \*/

125\#endif /\* multiple-inclusion guard \*/
