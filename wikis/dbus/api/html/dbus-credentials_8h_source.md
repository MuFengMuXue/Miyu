dbus-credentials.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-credentials.h Credentials provable through authentication

3 \*

4 \* Copyright (C) 2007 Red Hat Inc.

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

25\#ifndef DBUS_CREDENTIALS_H

26\#define DBUS_CREDENTIALS_H

27

28\#include \<dbus/dbus-macros.h\>

29\#include \<dbus/dbus-errors.h\>

30\#include \<dbus/dbus-string.h\>

31\#include \<dbus/dbus-sysdeps.h\>

32

33DBUS_BEGIN_DECLS

34

35typedef enum {

36 DBUS_CREDENTIAL_UNIX_PROCESS_ID,

37 DBUS_CREDENTIAL_UNIX_USER_ID,

38 DBUS_CREDENTIAL_UNIX_GROUP_IDS,

39 DBUS_CREDENTIAL_ADT_AUDIT_DATA_ID,

40 DBUS_CREDENTIAL_LINUX_SECURITY_LABEL,

41 DBUS_CREDENTIAL_WINDOWS_SID,

42 DBUS_CREDENTIAL_UNIX_PROCESS_FD,

43} DBusCredentialType;

44

45DBUS_PRIVATE_EXPORT

46DBusCredentials\* \_dbus_credentials_new_from_current_process (void);

47DBUS_PRIVATE_EXPORT

48DBusCredentials\* \_dbus_credentials_new (void);

49DBUS_PRIVATE_EXPORT

50void \_dbus_credentials_ref (DBusCredentials \*credentials);

51DBUS_PRIVATE_EXPORT

52void \_dbus_credentials_unref (DBusCredentials \*credentials);

53DBUS_PRIVATE_EXPORT

54dbus_bool_t \_dbus_credentials_add_pid (DBusCredentials \*credentials,

55 dbus_pid_t pid);

56DBUS_PRIVATE_EXPORT

57void \_dbus_credentials_take_pid_fd (DBusCredentials \*credentials,

58 int pid_fd);

59DBUS_PRIVATE_EXPORT

60dbus_bool_t \_dbus_credentials_add_unix_uid (DBusCredentials \*credentials,

61 dbus_uid_t uid);

62DBUS_PRIVATE_EXPORT

63void \_dbus_credentials_take_unix_gids (DBusCredentials \*credentials,

64 dbus_gid_t \*gids,

65 size_t n_gids);

66DBUS_PRIVATE_EXPORT

67dbus_bool_t \_dbus_credentials_add_windows_sid (DBusCredentials \*credentials,

68 const char \*windows_sid);

69dbus_bool_t \_dbus_credentials_add_linux_security_label (DBusCredentials \*credentials,

70 const char \*label);

71dbus_bool_t \_dbus_credentials_add_adt_audit_data (DBusCredentials \*credentials,

72 void \*audit_data,

73 dbus_int32_t size);

74DBUS_PRIVATE_EXPORT

75dbus_bool_t \_dbus_credentials_include (DBusCredentials \*credentials,

76 DBusCredentialType type);

77DBUS_PRIVATE_EXPORT

78dbus_pid_t \_dbus_credentials_get_pid (DBusCredentials \*credentials);

79DBUS_PRIVATE_EXPORT

80int \_dbus_credentials_get_pid_fd (DBusCredentials \*credentials);

81DBUS_PRIVATE_EXPORT

82dbus_uid_t \_dbus_credentials_get_unix_uid (DBusCredentials \*credentials);

83DBUS_PRIVATE_EXPORT

84dbus_bool_t \_dbus_credentials_get_unix_gids (DBusCredentials \*credentials,

85 const dbus_gid_t \*\*gids,

86 size_t \*n_gids);

87DBUS_PRIVATE_EXPORT

88const char\* \_dbus_credentials_get_windows_sid (DBusCredentials \*credentials);

89DBUS_PRIVATE_EXPORT

90const char \* \_dbus_credentials_get_linux_security_label (DBusCredentials \*credentials);

91void \* \_dbus_credentials_get_adt_audit_data (DBusCredentials \*credentials);

92dbus_int32_t \_dbus_credentials_get_adt_audit_data_size (DBusCredentials \*credentials);

93DBUS_PRIVATE_EXPORT

94dbus_bool_t \_dbus_credentials_are_superset (DBusCredentials \*credentials,

95 DBusCredentials \*possible_subset);

96DBUS_PRIVATE_EXPORT

97dbus_bool_t \_dbus_credentials_are_empty (DBusCredentials \*credentials);

98DBUS_PRIVATE_EXPORT

99dbus_bool_t \_dbus_credentials_are_anonymous (DBusCredentials \*credentials);

100dbus_bool_t \_dbus_credentials_add_credentials (DBusCredentials \*credentials,

101 DBusCredentials \*other_credentials);

102/\* must silently allow 'which' to not exist \*/

103dbus_bool_t \_dbus_credentials_add_credential (DBusCredentials \*credentials,

104 DBusCredentialType which,

105 DBusCredentials \*other_credentials);

106DBUS_PRIVATE_EXPORT

107void \_dbus_credentials_clear (DBusCredentials \*credentials);

108DBUS_PRIVATE_EXPORT

109DBusCredentials\* \_dbus_credentials_copy (DBusCredentials \*credentials);

110DBUS_PRIVATE_EXPORT

111dbus_bool_t \_dbus_credentials_same_user (DBusCredentials \*credentials,

112 DBusCredentials \*other_credentials);

113DBUS_PRIVATE_EXPORT

114dbus_bool_t \_dbus_credentials_to_string_append (DBusCredentials \*credentials,

115 DBusString \*string);

116

117static inline void

118\_dbus_clear_credentials (DBusCredentials \*\*pointer_to_creds)

119{

120 \_dbus_clear_pointer_impl (DBusCredentials, pointer_to_creds,

121 \_dbus_credentials_unref);

122}

123

124DBUS_END_DECLS

125

126\#endif /\* DBUS_CREDENTIALS_H \*/

\_dbus_credentials_ref

DBUS_PRIVATE_EXPORT void \_dbus_credentials_ref(DBusCredentials \*credentials)

Increment refcount on credentials.

**Definition** dbus-credentials.c:136

\_dbus_credentials_include

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_credentials_include(DBusCredentials \*credentials, DBusCredentialType type)

Checks whether the given credential is present.

**Definition** dbus-credentials.c:365

\_dbus_credentials_are_superset

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_credentials_are_superset(DBusCredentials \*credentials, DBusCredentials \*possible_subset)

Checks whether the first credentials object contains all the credentials found in the second credenti...

**Definition** dbus-credentials.c:506

\_dbus_credentials_same_user

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_credentials_same_user(DBusCredentials \*credentials, DBusCredentials \*other_credentials)

Check whether the user-identifying credentials in two credentials objects are identical.

**Definition** dbus-credentials.c:747

\_dbus_credentials_clear

DBUS_PRIVATE_EXPORT void \_dbus_credentials_clear(DBusCredentials \*credentials)

Clear all credentials in the object.

**Definition** dbus-credentials.c:688

\_dbus_credentials_get_unix_uid

DBUS_PRIVATE_EXPORT dbus_uid_t \_dbus_credentials_get_unix_uid(DBusCredentials \*credentials)

Gets the UNIX user ID in the credentials, or DBUS_UID_UNSET if the credentials object doesn't contain...

**Definition** dbus-credentials.c:440

\_dbus_credentials_copy

DBUS_PRIVATE_EXPORT DBusCredentials \* \_dbus_credentials_copy(DBusCredentials \*credentials)

Copy a credentials object.

**Definition** dbus-credentials.c:718

\_dbus_credentials_new_from_current_process

DBUS_PRIVATE_EXPORT DBusCredentials \* \_dbus_credentials_new_from_current_process(void)

Creates a new object with the most important credentials (user ID and process ID) from the current pr...

**Definition** dbus-credentials.c:113

\_dbus_credentials_to_string_append

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_credentials_to_string_append(DBusCredentials \*credentials, DBusString \*string)

Convert the credentials in this object to a human-readable string format, and append to the given str...

**Definition** dbus-credentials.c:768

\_dbus_credentials_new

DBUS_PRIVATE_EXPORT DBusCredentials \* \_dbus_credentials_new(void)

Creates a new credentials object.

**Definition** dbus-credentials.c:86

\_dbus_credentials_get_adt_audit_data

void \* \_dbus_credentials_get_adt_audit_data(DBusCredentials \*credentials)

Gets the ADT audit data in the credentials, or NULL if the credentials object doesn't contain ADT aud...

**Definition** dbus-credentials.c:479

\_dbus_credentials_take_pid_fd

DBUS_PRIVATE_EXPORT void \_dbus_credentials_take_pid_fd(DBusCredentials \*credentials, int pid_fd)

Add a UNIX process ID FD to the credentials.

**Definition** dbus-credentials.c:200

\_dbus_credentials_add_linux_security_label

dbus_bool_t \_dbus_credentials_add_linux_security_label(DBusCredentials \*credentials, const char \*label)

Add a Linux security label, as used by LSMs such as SELinux, Smack and AppArmor, to the credentials.

**Definition** dbus-credentials.c:317

\_dbus_credentials_add_credentials

dbus_bool_t \_dbus_credentials_add_credentials(DBusCredentials \*credentials, DBusCredentials \*other_credentials)

Merge all credentials found in the second object into the first object, overwriting the first object ...

**Definition** dbus-credentials.c:574

\_dbus_credentials_get_linux_security_label

DBUS_PRIVATE_EXPORT const char \* \_dbus_credentials_get_linux_security_label(DBusCredentials \*credentials)

Gets the Linux security label (as used by LSMs) from the credentials, or NULL if the credentials obje...

**Definition** dbus-credentials.c:466

\_dbus_credentials_take_unix_gids

DBUS_PRIVATE_EXPORT void \_dbus_credentials_take_unix_gids(DBusCredentials \*credentials, dbus_gid_t \*gids, size_t n_gids)

Add UNIX group IDs to the credentials, replacing any group IDs that might already have been present.

**Definition** dbus-credentials.c:252

\_dbus_credentials_unref

DBUS_PRIVATE_EXPORT void \_dbus_credentials_unref(DBusCredentials \*credentials)

Decrement refcount on credentials.

**Definition** dbus-credentials.c:148

\_dbus_credentials_get_unix_gids

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_credentials_get_unix_gids(DBusCredentials \*credentials, const dbus_gid_t \*\*gids, size_t \*n_gids)

Get the Unix group IDs.

**Definition** dbus-credentials.c:272

\_dbus_credentials_are_empty

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_credentials_are_empty(DBusCredentials \*credentials)

Checks whether a credentials object contains anything.

**Definition** dbus-credentials.c:538

\_dbus_credentials_add_unix_uid

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_credentials_add_unix_uid(DBusCredentials \*credentials, dbus_uid_t uid)

Add a UNIX user ID to the credentials.

**Definition** dbus-credentials.c:220

\_dbus_credentials_add_windows_sid

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_credentials_add_windows_sid(DBusCredentials \*credentials, const char \*windows_sid)

Add a Windows user SID to the credentials.

**Definition** dbus-credentials.c:293

\_dbus_credentials_add_pid

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_credentials_add_pid(DBusCredentials \*credentials, dbus_pid_t pid)

Add a UNIX process ID to the credentials.

**Definition** dbus-credentials.c:181

\_dbus_credentials_get_pid

DBUS_PRIVATE_EXPORT dbus_pid_t \_dbus_credentials_get_pid(DBusCredentials \*credentials)

Gets the UNIX process ID in the credentials, or DBUS_PID_UNSET if the credentials object doesn't cont...

**Definition** dbus-credentials.c:401

\_dbus_credentials_add_adt_audit_data

dbus_bool_t \_dbus_credentials_add_adt_audit_data(DBusCredentials \*credentials, void \*audit_data, dbus_int32_t size)

Add ADT audit data to the credentials.

**Definition** dbus-credentials.c:341

\_dbus_credentials_get_adt_audit_data_size

dbus_int32_t \_dbus_credentials_get_adt_audit_data_size(DBusCredentials \*credentials)

Gets the ADT audit data size in the credentials, or 0 if the credentials object doesn't contain ADT a...

**Definition** dbus-credentials.c:492

\_dbus_credentials_get_windows_sid

DBUS_PRIVATE_EXPORT const char \* \_dbus_credentials_get_windows_sid(DBusCredentials \*credentials)

Gets the Windows user SID in the credentials, or NULL if the credentials object doesn't contain a Win...

**Definition** dbus-credentials.c:453

\_dbus_credentials_add_credential

dbus_bool_t \_dbus_credentials_add_credential(DBusCredentials \*credentials, DBusCredentialType which, DBusCredentials \*other_credentials)

Merge the given credential found in the second object into the first object, overwriting the first ob...

**Definition** dbus-credentials.c:614

\_dbus_credentials_are_anonymous

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_credentials_are_anonymous(DBusCredentials \*credentials)

Checks whether a credentials object contains a user identity.

**Definition** dbus-credentials.c:558

\_dbus_credentials_get_pid_fd

DBUS_PRIVATE_EXPORT int \_dbus_credentials_get_pid_fd(DBusCredentials \*credentials)

Gets the UNIX process ID FD in the credentials as obtained by 'safe' means (e.g.: Linux's SO_PEERPIDF...

**Definition** dbus-credentials.c:427

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

dbus_pid_t

unsigned long dbus_pid_t

A process ID.

**Definition** dbus-sysdeps.h:139

dbus_gid_t

unsigned long dbus_gid_t

A group ID.

**Definition** dbus-sysdeps.h:143

DBusCredentials

**Definition** dbus-credentials.c:60

DBusString

**Definition** dbus-string.h:47
