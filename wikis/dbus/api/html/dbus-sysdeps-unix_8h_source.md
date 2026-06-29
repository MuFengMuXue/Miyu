dbus-sysdeps-unix.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-sysdeps-unix.h UNIX-specific wrappers around system/libc features (internal to D-Bus implementation)

3 \*

4 \* Copyright (C) 2002, 2003, 2006 Red Hat, Inc.

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

26

27\#ifndef DBUS_SYSDEPS_UNIX_H

28\#define DBUS_SYSDEPS_UNIX_H

29

30\#include \<dbus/dbus-sysdeps.h\>

31

32\#ifdef DBUS_WIN

33\#error "Don't include this on Windows"

34\#endif

35

36DBUS_BEGIN_DECLS

37

45DBUS_PRIVATE_EXPORT

46dbus_bool_t

47\_dbus_close (int fd,

48 DBusError \*error);

49DBUS_PRIVATE_EXPORT

50int \_dbus_dup (int fd,

51 DBusError \*error);

52DBUS_PRIVATE_EXPORT

53int

54\_dbus_read (int fd,

55 DBusString \*buffer,

56 int count);

57int

58\_dbus_write (int fd,

59 const DBusString \*buffer,

60 int start,

61 int len);

62int

63\_dbus_write_two (int fd,

64 const DBusString \*buffer1,

65 int start1,

66 int len1,

67 const DBusString \*buffer2,

68 int start2,

69 int len2);

70

71int \_dbus_listen_systemd_sockets (DBusSocket \*\*fd,

72 DBusError \*error);

73

74dbus_bool_t \_dbus_read_credentials (int client_fd,

75 DBusCredentials \*credentials,

76 DBusError \*error);

77dbus_bool_t \_dbus_send_credentials (int server_fd,

78 DBusError \*error);

79

80dbus_bool_t \_dbus_lookup_launchd_socket (DBusString \*socket_path,

81 const char \*launchd_env_var,

82 DBusError \*error);

83

85typedef struct DBusUserInfo DBusUserInfo;

87typedef struct DBusGroupInfo DBusGroupInfo;

88

92struct DBusUserInfo

93{

94 size_t refcount;

95 dbus_uid_t uid;

96 dbus_gid_t primary_gid;

97 dbus_gid_t \*group_ids;

98 int n_group_ids;

99 char \*username;

100 char \*homedir;

101};

102

106struct DBusGroupInfo

107{

108 size_t refcount;

109 dbus_gid_t gid;

110 char \*groupname;

111};

112

113dbus_bool_t \_dbus_user_info_fill (DBusUserInfo \*info,

114 const DBusString \*username,

115 DBusError \*error);

116dbus_bool_t \_dbus_user_info_fill_uid (DBusUserInfo \*info,

117 dbus_uid_t uid,

118 DBusError \*error);

119void \_dbus_user_info_free (DBusUserInfo \*info);

120

121dbus_bool_t \_dbus_group_info_fill (DBusGroupInfo \*info,

122 const DBusString \*groupname,

123 DBusError \*error);

124dbus_bool_t \_dbus_group_info_fill_gid (DBusGroupInfo \*info,

125 dbus_gid_t gid,

126 DBusError \*error);

127void \_dbus_group_info_free (DBusGroupInfo \*info);

128

129DBUS_PRIVATE_EXPORT

130dbus_uid_t \_dbus_geteuid (void);

131

132DBUS_PRIVATE_EXPORT

133void \_dbus_close_all (void);

134DBUS_PRIVATE_EXPORT

135void \_dbus_fd_set_all_close_on_exec (void);

136DBUS_PRIVATE_EXPORT

137void \_dbus_fd_clear_close_on_exec (int fd);

138

139dbus_bool_t \_dbus_append_address_from_socket (DBusSocket fd,

140 DBusString \*address,

141 DBusError \*error);

142

143DBUS_PRIVATE_EXPORT

144void \_dbus_fd_set_close_on_exec (int fd);

145

146typedef enum

147{

148 DBUS_FORCE_STDIN_NULL = (1 \<\< 0),

149 DBUS_FORCE_STDOUT_NULL = (1 \<\< 1),

150 DBUS_FORCE_STDERR_NULL = (1 \<\< 2)

151} DBusEnsureStandardFdsFlags;

152

153DBUS_PRIVATE_EXPORT

154dbus_bool_t \_dbus_ensure_standard_fds (DBusEnsureStandardFdsFlags flags,

155 const char \*\*error_str_p);

156

158typedef void (\* DBusSignalHandler) (int sig);

159

160void \_dbus_set_signal_handler (int sig,

161 DBusSignalHandler handler);

162

163dbus_bool_t \_dbus_reset_oom_score_adj (const char \*\*error_str_p);

164

167DBUS_END_DECLS

168

169\#endif /\* DBUS_SYSDEPS_UNIX_H \*/

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

\_dbus_fd_clear_close_on_exec

DBUS_PRIVATE_EXPORT void \_dbus_fd_clear_close_on_exec(int fd)

Sets the file descriptor to not be close-on-exec.

**Definition** dbus-sysdeps-unix.c:3705

\_dbus_reset_oom_score_adj

dbus_bool_t \_dbus_reset_oom_score_adj(const char \*\*error_str_p)

If the current process has been protected from the Linux OOM killer (the oom_score_adj process parame...

**Definition** dbus-sysdeps-util-unix.c:1602

\_dbus_group_info_fill

dbus_bool_t \_dbus_group_info_fill(DBusGroupInfo \*info, const DBusString \*groupname, DBusError \*error)

Initializes the given DBusGroupInfo struct with information about the given group name.

**Definition** dbus-sysdeps-util-unix.c:884

\_dbus_fd_set_all_close_on_exec

DBUS_PRIVATE_EXPORT void \_dbus_fd_set_all_close_on_exec(void)

Sets all file descriptors except the first three (i.e.

**Definition** dbus-sysdeps-unix.c:4982

\_dbus_close

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_close(int fd, DBusError \*error)

Closes a file descriptor.

**Definition** dbus-sysdeps-unix.c:3727

\_dbus_write

int \_dbus_write(int fd, const DBusString \*buffer, int start, int len)

Thin wrapper around the write() system call that writes a part of a DBusString and handles EINTR for ...

**Definition** dbus-sysdeps-unix.c:827

DBusSignalHandler

void(\* DBusSignalHandler)(int sig)

A UNIX signal handler.

**Definition** dbus-sysdeps-unix.h:158

\_dbus_set_signal_handler

void \_dbus_set_signal_handler(int sig, DBusSignalHandler handler)

Installs a UNIX signal handler.

**Definition** dbus-sysdeps-util-unix.c:545

\_dbus_write_two

int \_dbus_write_two(int fd, const DBusString \*buffer1, int start1, int len1, const DBusString \*buffer2, int start2, int len2)

Like \_dbus_write() but will use writev() if possible to write both buffers in sequence.

**Definition** dbus-sysdeps-unix.c:873

\_dbus_lookup_launchd_socket

dbus_bool_t \_dbus_lookup_launchd_socket(DBusString \*socket_path, const char \*launchd_env_var, DBusError \*error)

quries launchd for a specific env var which holds the socket path.

**Definition** dbus-sysdeps-unix.c:4486

\_dbus_listen_systemd_sockets

int \_dbus_listen_systemd_sockets(DBusSocket \*\*fd, DBusError \*error)

Acquires one or more sockets passed in from systemd.

**Definition** dbus-sysdeps-unix.c:1299

\_dbus_append_address_from_socket

dbus_bool_t \_dbus_append_address_from_socket(DBusSocket fd, DBusString \*address, DBusError \*error)

Read the address from the socket and append it to the string.

**Definition** dbus-sysdeps-unix.c:5055

\_dbus_user_info_fill

dbus_bool_t \_dbus_user_info_fill(DBusUserInfo \*info, const DBusString \*username, DBusError \*error)

Gets user info for the given username.

**Definition** dbus-sysdeps-unix.c:2966

\_dbus_user_info_free

void \_dbus_user_info_free(DBusUserInfo \*info)

Frees the members of info (but not info itself)

**Definition** dbus-userdb.c:108

\_dbus_group_info_free

void \_dbus_group_info_free(DBusGroupInfo \*info)

Frees the members of info (but not info itself).

**Definition** dbus-userdb.c:121

\_dbus_close_all

DBUS_PRIVATE_EXPORT void \_dbus_close_all(void)

Closes all file descriptors except the first three (i.e.

**Definition** dbus-sysdeps-unix.c:4963

\_dbus_group_info_fill_gid

dbus_bool_t \_dbus_group_info_fill_gid(DBusGroupInfo \*info, dbus_gid_t gid, DBusError \*error)

Initializes the given DBusGroupInfo struct with information about the given group ID.

**Definition** dbus-sysdeps-util-unix.c:903

\_dbus_dup

DBUS_PRIVATE_EXPORT int \_dbus_dup(int fd, DBusError \*error)

Duplicates a file descriptor.

**Definition** dbus-sysdeps-unix.c:3755

\_dbus_fd_set_close_on_exec

DBUS_PRIVATE_EXPORT void \_dbus_fd_set_close_on_exec(int fd)

Sets the file descriptor to be close on exec.

**Definition** dbus-sysdeps-unix.c:3683

\_dbus_read

DBUS_PRIVATE_EXPORT int \_dbus_read(int fd, DBusString \*buffer, int count)

Thin wrapper around the read() system call that appends the data it reads to the DBusString buffer.

**Definition** dbus-sysdeps-unix.c:767

\_dbus_ensure_standard_fds

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_ensure_standard_fds(DBusEnsureStandardFdsFlags flags, const char \*\*error_str_p)

Ensure that the standard file descriptors stdin, stdout and stderr are open, by opening /dev/null if ...

**Definition** dbus-sysdeps-unix.c:179

\_dbus_geteuid

DBUS_PRIVATE_EXPORT dbus_uid_t \_dbus_geteuid(void)

Gets our effective UID.

**Definition** dbus-sysdeps-unix.c:3145

\_dbus_user_info_fill_uid

dbus_bool_t \_dbus_user_info_fill_uid(DBusUserInfo \*info, dbus_uid_t uid, DBusError \*error)

Gets user info for the given user ID.

**Definition** dbus-sysdeps-unix.c:2983

dbus_uid_t

unsigned long dbus_uid_t

A user ID.

**Definition** dbus-sysdeps.h:141

dbus_gid_t

unsigned long dbus_gid_t

A group ID.

**Definition** dbus-sysdeps.h:143

DBusCredentials

**Definition** dbus-credentials.c:60

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusGroupInfo

Information about a UNIX group.

**Definition** dbus-sysdeps-unix.h:107

DBusGroupInfo::gid

dbus_gid_t gid

GID.

**Definition** dbus-sysdeps-unix.h:109

DBusGroupInfo::groupname

char \* groupname

Group name.

**Definition** dbus-sysdeps-unix.h:110

DBusGroupInfo::refcount

size_t refcount

Reference count.

**Definition** dbus-sysdeps-unix.h:108

DBusSocket

Socket interface.

**Definition** dbus-sysdeps.h:185

DBusString

**Definition** dbus-string.h:47

DBusUserInfo

Information about a UNIX user.

**Definition** dbus-sysdeps-unix.h:93

DBusUserInfo::n_group_ids

int n_group_ids

Size of group IDs array.

**Definition** dbus-sysdeps-unix.h:98

DBusUserInfo::uid

dbus_uid_t uid

UID.

**Definition** dbus-sysdeps-unix.h:95

DBusUserInfo::homedir

char \* homedir

Home directory.

**Definition** dbus-sysdeps-unix.h:100

DBusUserInfo::group_ids

dbus_gid_t \* group_ids

Groups IDs, including above primary group.

**Definition** dbus-sysdeps-unix.h:97

DBusUserInfo::refcount

size_t refcount

Reference count.

**Definition** dbus-sysdeps-unix.h:94

DBusUserInfo::username

char \* username

Username.

**Definition** dbus-sysdeps-unix.h:99

DBusUserInfo::primary_gid

dbus_gid_t primary_gid

GID.

**Definition** dbus-sysdeps-unix.h:96
