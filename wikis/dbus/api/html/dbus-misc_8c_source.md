dbus-misc.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-misc.c A few assorted public functions that don't fit elsewhere

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

25

26\#include \<config.h\>

27\#include "dbus-misc.h"

28\#include "dbus-internals.h"

29\#include "dbus-string.h"

30\#include \<dbus/dbus-test-tap.h\>

31

75char \*

76dbus_try_get_local_machine_id (DBusError \*error)

77{

78 DBusString uuid;

79 char \*s;

80

81 s = NULL;

82

83 if (!\_dbus_string_init (&uuid))

84 {

85 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

86 return NULL;

87 }

88

89 if (!\_dbus_get_local_machine_uuid_encoded (&uuid, error))

90 {

91 \_dbus_string_free (&uuid);

92 return NULL;

93 }

94

95 if (!\_dbus_string_steal_data (&uuid, &s))

96 {

97 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

98 \_dbus_string_free (&uuid);

99 return NULL;

100 }

101 else

102 {

103 \_dbus_string_free (&uuid);

104 return s;

105 }

106

107}

108

124char \*

125dbus_get_local_machine_id (void)

126{

127 DBusError error = DBUS_ERROR_INIT;

128 char \*s;

129

130 s = dbus_try_get_local_machine_id (&error);

131

132 /\* The documentation says dbus_get_local_machine_id() only fails on OOM;

133 \* this can actually also fail if the D-Bus installation is faulty

134 \* (no UUID), but we have no good way to report that. Historically,

135 \* \_dbus_get_local_machine_uuid_encoded was responsible for issuing the

136 \* warning; now we do that here. \*/

137 if (s == NULL)

138 {

139 if (!dbus_error_has_name (&error, DBUS_ERROR_NO_MEMORY))

140 \_dbus_warn_check_failed ("%s", error.message);

141

142 dbus_error_free (&error);

143 return NULL;

144 }

145

146 return s;

147}

148

212void

213dbus_get_version (int \*major_version_p,

214 int \*minor_version_p,

215 int \*micro_version_p)

216{

217 if (major_version_p)

218 \*major_version_p = DBUS_MAJOR_VERSION;

219 if (minor_version_p)

220 \*minor_version_p = DBUS_MINOR_VERSION;

221 if (micro_version_p)

222 \*micro_version_p = DBUS_MICRO_VERSION;

223}

224

225

/\* End of public API \*/

DBUS_ERROR_INIT

\#define DBUS_ERROR_INIT

Expands to a suitable initializer for a DBusError on the stack.

**Definition** dbus-errors.h:64

dbus_error_has_name

dbus_bool_t dbus_error_has_name(const DBusError \*error, const char \*name)

Checks whether the error is set and has the given name.

**Definition** dbus-errors.c:304

dbus_set_error

void dbus_set_error(DBusError \*error, const char \*name, const char \*format,...)

Assigns an error name and message to a DBusError.

**Definition** dbus-errors.c:356

dbus_error_free

void dbus_error_free(DBusError \*error)

Frees an error that's been set (or just initialized), then reinitializes the error as in dbus_error_i...

**Definition** dbus-errors.c:213

\_dbus_warn_check_failed

void \_dbus_warn_check_failed(const char \*format,...)

Prints a "critical" warning to stderr when an assertion fails; differs from \_dbus_warn primarily in t...

**Definition** dbus-internals.c:310

\_dbus_get_local_machine_uuid_encoded

dbus_bool_t \_dbus_get_local_machine_uuid_encoded(DBusString \*uuid_str, DBusError \*error)

Gets the hex-encoded UUID of the machine this function is executed on.

**Definition** dbus-internals.c:983

NULL

\#define NULL

A null pointer, defined appropriately for C or C++.

**Definition** dbus-macros.h:51

dbus_get_local_machine_id

char \* dbus_get_local_machine_id(void)

Obtains the machine UUID of the machine this process is running on.

**Definition** dbus-misc.c:125

DBUS_MICRO_VERSION

\#define DBUS_MICRO_VERSION

The COMPILE TIME micro version of libdbus, that is, the "Z" in "X.Y.Z", as an integer literal.

**Definition** dbus-arch-deps.h:57

dbus_try_get_local_machine_id

char \* dbus_try_get_local_machine_id(DBusError \*error)

Obtains the machine UUID of the machine this process is running on.

**Definition** dbus-misc.c:76

DBUS_MINOR_VERSION

\#define DBUS_MINOR_VERSION

The COMPILE TIME minor version of libdbus, that is, the "Y" in "X.Y.Z", as an integer literal.

**Definition** dbus-arch-deps.h:56

DBUS_MAJOR_VERSION

\#define DBUS_MAJOR_VERSION

The COMPILE TIME major version of libdbus, that is, the "X" in "X.Y.Z", as an integer literal.

**Definition** dbus-arch-deps.h:55

dbus_get_version

void dbus_get_version(int \*major_version_p, int \*minor_version_p, int \*micro_version_p)

Gets the DYNAMICALLY LINKED version of libdbus.

**Definition** dbus-misc.c:213

DBUS_ERROR_NO_MEMORY

\#define DBUS_ERROR_NO_MEMORY

There was not enough memory to complete an operation.

**Definition** dbus-protocol.h:363

\_dbus_string_init

dbus_bool_t \_dbus_string_init(DBusString \*str)

Initializes a string.

**Definition** dbus-string.c:182

\_dbus_string_steal_data

dbus_bool_t \_dbus_string_steal_data(DBusString \*str, char \*\*data_return)

Like \_dbus_string_get_data(), but removes the gotten data from the original string.

**Definition** dbus-string.c:686

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusError::message

const char \* message

public error message field

**Definition** dbus-errors.h:53

DBusString

**Definition** dbus-string.h:47
