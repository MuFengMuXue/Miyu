dbus-userdb.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-userdb.h User database abstraction

3 \*

4 \* Copyright (C) 2003 Red Hat, Inc.

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

26\#ifndef DBUS_USERDB_H

27\#define DBUS_USERDB_H

28

29\#include \<dbus/dbus-sysdeps-unix.h\>

30

31\#ifdef DBUS_WIN

32\#error "Don't include this on Windows"

33\#endif

34

35DBUS_BEGIN_DECLS

36

37typedef struct DBusUserDatabase DBusUserDatabase;

38

39\#ifdef DBUS_USERDB_INCLUDES_PRIVATE

40\#include \<dbus/dbus-hash.h\>

41

45struct DBusUserDatabase

46{

47 int refcount;

49 DBusHashTable \*users;

50 DBusHashTable \*groups;

51 DBusHashTable \*users_by_name;

52 DBusHashTable \*groups_by_name;

54};

55

56

57DBusUserDatabase\* \_dbus_user_database_new (void);

58DBusUserDatabase\* \_dbus_user_database_ref (DBusUserDatabase \*db);

59void \_dbus_user_database_flush (DBusUserDatabase \*db);

60void \_dbus_user_database_unref (DBusUserDatabase \*db);

61DBUS_PRIVATE_EXPORT

62dbus_bool_t \_dbus_user_database_get_uid (DBusUserDatabase \*db,

63 dbus_uid_t uid,

64 const DBusUserInfo \*\*info,

65 DBusError \*error);

66DBUS_PRIVATE_EXPORT

67dbus_bool_t \_dbus_user_database_get_username (DBusUserDatabase \*db,

68 const DBusString \*username,

69 const DBusUserInfo \*\*info,

70 DBusError \*error);

71DBUS_PRIVATE_EXPORT

72const DBusUserInfo \*\_dbus_user_database_lookup (DBusUserDatabase \*db,

73 dbus_uid_t uid,

74 const DBusString \*username,

75 DBusError \*error);

76DBUS_PRIVATE_EXPORT

77const DBusGroupInfo\* \_dbus_user_database_lookup_group (DBusUserDatabase \*db,

78 dbus_gid_t gid,

79 const DBusString \*groupname,

80 DBusError \*error);

81

82void \_dbus_user_info_unref (DBusUserInfo \*info);

83DBUS_PRIVATE_EXPORT

84void \_dbus_group_info_unref (DBusGroupInfo \*info);

85\#endif /\* DBUS_USERDB_INCLUDES_PRIVATE \*/

86

87DBUS_PRIVATE_EXPORT

88DBusUserDatabase\* \_dbus_user_database_get_system (void);

89DBUS_PRIVATE_EXPORT \_DBUS_WARN_UNUSED_RESULT

90dbus_bool_t \_dbus_user_database_lock_system (void);

91DBUS_PRIVATE_EXPORT

92void \_dbus_user_database_unlock_system (void);

93void \_dbus_user_database_flush_system (void);

94

95dbus_bool_t \_dbus_get_user_id (const DBusString \*username,

96 dbus_uid_t \*uid);

97dbus_bool_t \_dbus_get_group_id (const DBusString \*group_name,

98 dbus_gid_t \*gid);

99DBUS_PRIVATE_EXPORT

100dbus_bool_t \_dbus_get_user_id_and_primary_group (const DBusString \*username,

101 dbus_uid_t \*uid_p,

102 dbus_gid_t \*gid_p);

103dbus_bool_t \_dbus_groups_from_uid (dbus_uid_t uid,

104 dbus_gid_t \*\*group_ids,

105 int \*n_group_ids,

106 DBusError \*error);

107DBUS_PRIVATE_EXPORT

108dbus_bool_t \_dbus_is_console_user (dbus_uid_t uid,

109 DBusError \*error);

110

111DBUS_PRIVATE_EXPORT

112dbus_bool_t \_dbus_is_a_number (const DBusString \*str,

113 unsigned long \*num);

114

115DBUS_PRIVATE_EXPORT

116dbus_bool_t \_dbus_username_from_current_process (const DBusString \*\*username);

117DBUS_PRIVATE_EXPORT

118dbus_bool_t \_dbus_homedir_from_current_process (const DBusString \*\*homedir);

119dbus_bool_t \_dbus_homedir_from_uid (dbus_uid_t uid,

120 DBusString \*homedir);

121

122DBUS_END_DECLS

123

124\#endif /\* DBUS_USERDB_H \*/

\_dbus_user_database_lock_system

DBUS_PRIVATE_EXPORT \_DBUS_WARN_UNUSED_RESULT dbus_bool_t \_dbus_user_database_lock_system(void)

Locks global system user database.

**Definition** dbus-userdb.c:353

\_dbus_homedir_from_current_process

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_homedir_from_current_process(const DBusString \*\*homedir)

Gets homedir of user owning current process.

**Definition** dbus-userdb.c:442

\_dbus_user_database_new

DBusUserDatabase \* \_dbus_user_database_new(void)

Creates a new user database object used to look up and cache user information.

**Definition** dbus-userdb.c:598

\_dbus_user_database_unlock_system

DBUS_PRIVATE_EXPORT void \_dbus_user_database_unlock_system(void)

Unlocks global system user database.

**Definition** dbus-userdb.c:370

\_dbus_user_database_unref

void \_dbus_user_database_unref(DBusUserDatabase \*db)

Decrements refcount of user database.

**Definition** dbus-userdb.c:671

\_dbus_user_database_get_uid

dbus_bool_t \_dbus_user_database_get_uid(DBusUserDatabase \*db, dbus_uid_t uid, const DBusUserInfo \*\*info, DBusError \*error)

Gets the user information for the given UID, returned user info should not be freed.

**Definition** dbus-userdb.c:705

\_dbus_user_database_flush_system

void \_dbus_user_database_flush_system(void)

Flushes the system global user database;.

**Definition** dbus-userdb.c:396

\_dbus_get_group_id

dbus_bool_t \_dbus_get_group_id(const DBusString \*group_name, dbus_gid_t \*gid)

Gets group ID given groupname.

**Definition** dbus-userdb-util.c:145

\_dbus_group_info_unref

void \_dbus_group_info_unref(DBusGroupInfo \*info)

Decrements the reference count.

**Definition** dbus-userdb.c:87

\_dbus_user_database_lookup

const DBusUserInfo \* \_dbus_user_database_lookup(DBusUserDatabase \*db, dbus_uid_t uid, const DBusString \*username, DBusError \*error)

Looks up a uid or username in the user database.

**Definition** dbus-userdb.c:160

\_dbus_user_info_unref

void \_dbus_user_info_unref(DBusUserInfo \*info)

Decrements the reference count.

**Definition** dbus-userdb.c:64

\_dbus_username_from_current_process

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_username_from_current_process(const DBusString \*\*username)

Gets username of user owning current process.

**Definition** dbus-userdb.c:418

\_dbus_is_console_user

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_is_console_user(dbus_uid_t uid, DBusError \*error)

Checks to see if the UID sent in is the console user.

**Definition** dbus-userdb-util.c:67

\_dbus_user_database_lookup_group

const DBusGroupInfo \* \_dbus_user_database_lookup_group(DBusUserDatabase \*db, dbus_gid_t gid, const DBusString \*groupname, DBusError \*error)

Looks up a gid or group name in the user database.

**Definition** dbus-userdb-util.c:233

\_dbus_user_database_flush

void \_dbus_user_database_flush(DBusUserDatabase \*db)

Flush all information out of the user database.

**Definition** dbus-userdb.c:641

\_dbus_groups_from_uid

dbus_bool_t \_dbus_groups_from_uid(dbus_uid_t uid, dbus_gid_t \*\*group_ids, int \*n_group_ids, DBusError \*error)

Gets all groups corresponding to the given UID.

**Definition** dbus-userdb-util.c:349

\_dbus_homedir_from_uid

dbus_bool_t \_dbus_homedir_from_uid(dbus_uid_t uid, DBusString \*homedir)

Gets the home directory for the given user.

**Definition** dbus-userdb.c:466

\_dbus_get_user_id_and_primary_group

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_get_user_id_and_primary_group(const DBusString \*username, dbus_uid_t \*uid_p, dbus_gid_t \*gid_p)

Gets user ID and primary group given username.

**Definition** dbus-userdb-util.c:186

\_dbus_user_database_get_username

dbus_bool_t \_dbus_user_database_get_username(DBusUserDatabase \*db, const DBusString \*username, const DBusUserInfo \*\*info, DBusError \*error)

Gets the user information for the given username.

**Definition** dbus-userdb.c:724

\_dbus_is_a_number

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_is_a_number(const DBusString \*str, unsigned long \*num)

Checks if a given string is actually a number and converts it if it is.

**Definition** dbus-userdb.c:135

\_dbus_get_user_id

dbus_bool_t \_dbus_get_user_id(const DBusString \*username, dbus_uid_t \*uid)

Gets user ID given username.

**Definition** dbus-userdb-util.c:131

\_dbus_user_database_get_system

DBUS_PRIVATE_EXPORT DBusUserDatabase \* \_dbus_user_database_get_system(void)

Gets the system global user database; must be called with lock held (\_dbus_user_database_lock_system(...

**Definition** dbus-userdb.c:383

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

dbus_uid_t

unsigned long dbus_uid_t

A user ID.

**Definition** dbus-sysdeps.h:141

dbus_gid_t

unsigned long dbus_gid_t

A group ID.

**Definition** dbus-sysdeps.h:143

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusGroupInfo

Information about a UNIX group.

**Definition** dbus-sysdeps-unix.h:107

DBusHashTable

Internals of DBusHashTable.

**Definition** dbus-hash.c:175

DBusString

**Definition** dbus-string.h:47

DBusUserInfo

Information about a UNIX user.

**Definition** dbus-sysdeps-unix.h:93
