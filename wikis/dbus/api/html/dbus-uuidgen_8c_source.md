dbus-uuidgen.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-uuidgen.c The guts of the dbus-uuidgen binary live in libdbus, in this file.

3 \*

4 \* Copyright (C) 2006 Red Hat, Inc.

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

25\#include \<config.h\>

26\#include "dbus-uuidgen.h"

27\#include "dbus-internals.h"

28\#include "dbus-string.h"

29\#include "dbus-protocol.h"

30

31\#ifdef DBUS_WIN

32\#error "dbus-uuidgen should not be needed on Windows"

33\#endif

34

46static dbus_bool_t

47return_uuid (DBusGUID \*uuid,

48 char \*\*uuid_p,

49 DBusError \*error)

50{

51 if (uuid_p)

52 {

53 DBusString encoded;

54

55 if (!\_dbus_string_init (&encoded))

56 {

57 \_DBUS_SET_OOM (error);

58 return FALSE;

59 }

60

61 if (!\_dbus_uuid_encode (uuid, &encoded) \|\|

62 !\_dbus_string_steal_data (&encoded, uuid_p))

63 {

64 \_DBUS_SET_OOM (error);

65 \_dbus_string_free (&encoded);

66 return FALSE;

67 }

68 \_dbus_string_free (&encoded);

69 }

70 return TRUE;

71}

72

84dbus_bool_t

85\_dbus_get_uuid (const char \*filename,

86 char \*\*uuid_p,

87 dbus_bool_t create_if_not_found,

88 DBusError \*error)

89{

90 DBusGUID uuid;

91

92 if (filename)

93 {

94 DBusString filename_str;

95 \_dbus_string_init_const (&filename_str, filename);

96 if (!\_dbus_read_uuid_file (&filename_str, &uuid, create_if_not_found, error))

97 goto error;

98 }

99 else

100 {

101 if (!\_dbus_read_local_machine_uuid (&uuid, create_if_not_found, error))

102 goto error;

103 }

104

105 if (!return_uuid(&uuid, uuid_p, error))

106 goto error;

107

108 return TRUE;

109

110 error:

111 \_DBUS_ASSERT_ERROR_IS_SET (error);

112 return FALSE;

113}

114

120dbus_bool_t

121\_dbus_create_uuid (char \*\*uuid_p,

122 DBusError \*error)

123{

124 DBusGUID uuid;

125

126 if (!\_dbus_generate_uuid (&uuid, error))

127 return FALSE;

128

129 return return_uuid (&uuid, uuid_p, error);

130}

131

\_dbus_generate_uuid

dbus_bool_t \_dbus_generate_uuid(DBusGUID \*uuid, DBusError \*error)

Generates a new UUID.

**Definition** dbus-internals.c:752

\_dbus_read_uuid_file

dbus_bool_t \_dbus_read_uuid_file(const DBusString \*filename, DBusGUID \*uuid, dbus_bool_t create_if_not_found, DBusError \*error)

Reads (and optionally writes) a uuid to a file.

**Definition** dbus-internals.c:931

\_dbus_uuid_encode

dbus_bool_t \_dbus_uuid_encode(const DBusGUID \*uuid, DBusString \*encoded)

Hex-encode a UUID.

**Definition** dbus-internals.c:788

\_dbus_create_uuid

dbus_bool_t \_dbus_create_uuid(char \*\*uuid_p, DBusError \*error)

**Definition** dbus-uuidgen.c:121

\_dbus_get_uuid

dbus_bool_t \_dbus_get_uuid(const char \*filename, char \*\*uuid_p, dbus_bool_t create_if_not_found, DBusError \*error)

For use by the dbus-uuidgen binary ONLY, do not call this.

**Definition** dbus-uuidgen.c:85

TRUE

\#define TRUE

Expands to "1".

**Definition** dbus-macros.h:41

FALSE

\#define FALSE

Expands to "0".

**Definition** dbus-macros.h:44

\_dbus_string_init

dbus_bool_t \_dbus_string_init(DBusString \*str)

Initializes a string.

**Definition** dbus-string.c:182

\_dbus_string_init_const

void \_dbus_string_init_const(DBusString \*str, const char \*value)

Initializes a constant string.

**Definition** dbus-string.c:197

\_dbus_string_steal_data

dbus_bool_t \_dbus_string_steal_data(DBusString \*str, char \*\*data_return)

Like \_dbus_string_get_data(), but removes the gotten data from the original string.

**Definition** dbus-string.c:686

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_read_local_machine_uuid

dbus_bool_t \_dbus_read_local_machine_uuid(DBusGUID \*machine_id, dbus_bool_t create_if_not_found, DBusError \*error)

Reads the uuid of the machine we're running on from the dbus configuration.

**Definition** dbus-sysdeps-unix.c:4421

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusString

**Definition** dbus-string.h:47

DBusGUID

A globally unique ID ; we have one for each DBusServer, and also one for each machine with libdbus in...

**Definition** dbus-internals.h:458
