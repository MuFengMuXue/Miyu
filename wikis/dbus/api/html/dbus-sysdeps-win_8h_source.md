dbus-sysdeps-win.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-sysdeps.c Wrappers around system/libc features (internal to D-BUS implementation)

3 \*

4 \* Copyright (C) 2002, 2003 Red Hat, Inc.

5 \* Copyright (C) 2003 CodeFactory AB

6 \* Copyright (C) 2005 Novell, Inc.

7 \*

8 \* SPDX-License-Identifier: AFL-2.1 OR GPL-2.0-or-later

9 \*

10 \* Licensed under the Academic Free License version 2.1

11 \*

12 \* This program is free software; you can redistribute it and/or modify

13 \* it under the terms of the GNU General Public License as published by

14 \* the Free Software Foundation; either version 2 of the License, or

15 \* (at your option) any later version.

16 \*

17 \* This program is distributed in the hope that it will be useful,

18 \* but WITHOUT ANY WARRANTY; without even the implied warranty of

19 \* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the

20 \* GNU General Public License for more details.

21 \*

22 \* You should have received a copy of the GNU General Public License

23 \* along with this program; if not, write to the Free Software

24 \* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

25 \*

26 \*/

27

28\#ifndef DBUS_SYSDEPS_WIN_H

29\#define DBUS_SYSDEPS_WIN_H

30

31extern void \*\_dbus_win_get_dll_hmodule (void);

32\#define WIN32_LEAN_AND_MEAN

33

34\#include "dbus-hash.h"

35\#include "dbus-string.h"

36\#include "dbus-threads-internal.h"

37\#include \<ctype.h\>

38\#include \<malloc.h\>

39\#include \<windows.h\>

40\#undef interface

41

42\#define DBUS_CONSOLE_DIR "/var/run/console/"

43

44

45void \_dbus_win_set_errno (int err);

46DBUS_PRIVATE_EXPORT

47const char\* \_dbus_win_error_from_last_error (void);

48

49dbus_bool_t \_dbus_win_startup_winsock (void);

50void \_dbus_win_warn_win_error (const char \*message,

51 unsigned long code);

52DBUS_PRIVATE_EXPORT

53char \* \_dbus_win_error_string (int error_number);

54DBUS_PRIVATE_EXPORT

55void \_dbus_win_free_error_string (char \*string);

56

57extern const char\* \_dbus_lm_strerror (int error_number);

58

59

60dbus_bool_t \_dbus_win_account_to_sid (const wchar_t \*waccount,

61 void \*\*ppsid,

62 DBusError \*error);

63

64dbus_bool_t

65\_dbus_win32_sid_to_name_and_domain (dbus_uid_t uid,

66 wchar_t \*\*wname,

67 wchar_t \*\*wdomain,

68 DBusError \*error);

69

70

71/\* Don't define DBUS_CONSOLE_DIR on Win32 \*/

72

73wchar_t \*\_dbus_win_utf8_to_utf16 (const char \*str,

74 DBusError \*error);

75char \*\_dbus_win_utf16_to_utf8 (const wchar_t \*str,

76 DBusError \*error);

77

78DBUS_PRIVATE_EXPORT

79void \_dbus_win_set_error_from_win_error (DBusError \*error, int code);

80

81dbus_bool_t

82\_dbus_win_sid_to_name_and_domain (dbus_uid_t uid,

83 wchar_t \*\*wname,

84 wchar_t \*\*wdomain,

85 DBusError \*error);

86

87DBUS_PRIVATE_EXPORT

88dbus_bool_t \_dbus_get_install_root (DBusString \*str);

89

90DBUS_PRIVATE_EXPORT

91dbus_bool_t \_dbus_getsid(char \*\*sid, dbus_pid_t process_id);

92

93HANDLE \_dbus_spawn_program (const char \*name,

94 char \*\*argv,

95 char \*\*envp,

96 dbus_bool_t inherit_handles,

97 DBusError \*error);

98

99DBUS_PRIVATE_EXPORT

100void \_dbus_win_set_error_from_last_error (DBusError \*error,

101 const char \*format,

102 ...) \_DBUS_GNUC_PRINTF (2, 3);

103

104DBUS_PRIVATE_EXPORT

105HANDLE \_dbus_win_event_create_inheritable (DBusError \*error);

106DBUS_PRIVATE_EXPORT

107dbus_bool_t \_dbus_win_event_set (HANDLE handle, DBusError \*error);

108DBUS_PRIVATE_EXPORT

109dbus_bool_t \_dbus_win_event_wait (HANDLE handle, int timeout, DBusError \*error);

110DBUS_PRIVATE_EXPORT

111dbus_bool_t \_dbus_win_event_free (HANDLE handle, DBusError \*error);

112

113dbus_bool_t \_dbus_daemon_is_session_bus_address_published (const char \*scope);

114dbus_bool_t \_dbus_daemon_publish_session_bus_address (const char \*address,

115 const char \*shm_name);

116DBUS_PRIVATE_EXPORT

117DBusRMutex \*\_dbus_win_rmutex_named_new (const char\* name);

118

119DBUS_PRIVATE_EXPORT

120void \_dbus_test_win_autolaunch_set_command_line_parameter (const char \*path);

121DBUS_PRIVATE_EXPORT

122void \_dbus_test_win_set_autolaunch_handle_location (HANDLE \*location);

123\#endif

124

dbus_uid_t

unsigned long dbus_uid_t

A user ID.

**Definition** dbus-sysdeps.h:141

dbus_pid_t

unsigned long dbus_pid_t

A process ID.

**Definition** dbus-sysdeps.h:139

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusRMutex

**Definition** dbus-sysdeps-pthread.c:51

DBusString

**Definition** dbus-string.h:47
