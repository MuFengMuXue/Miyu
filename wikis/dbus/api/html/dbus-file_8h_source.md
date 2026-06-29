dbus-file.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-file.h dbus file related stuff (internal to D-Bus implementation)

3 \*

4 \* Copyright (C) 2002, 2003 Red Hat, Inc.

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

27\#ifndef DBUS_FILE_H

28\#define DBUS_FILE_H

29

30//#include \<dbus/dbus-types.h\>

31\#include \<dbus/dbus-string.h\>

32\#include \<dbus/dbus-errors.h\>

33

34DBUS_BEGIN_DECLS

35

44dbus_bool_t \_dbus_file_exists (const char \*file);

45DBUS_PRIVATE_EXPORT

46dbus_bool_t \_dbus_file_get_contents (DBusString \*str,

47 const DBusString \*filename,

48 DBusError \*error);

49dbus_bool_t \_dbus_string_save_to_file (const DBusString \*str,

50 const DBusString \*filename,

51 dbus_bool_t world_readable,

52 DBusError \*error);

53

54dbus_bool_t \_dbus_make_file_world_readable (const DBusString \*filename,

55 DBusError \*error);

56

57dbus_bool_t \_dbus_create_file_exclusively (const DBusString \*filename,

58 DBusError \*error);

59DBUS_PRIVATE_EXPORT

60dbus_bool_t \_dbus_delete_file (const DBusString \*filename,

61 DBusError \*error);

62

65DBUS_END_DECLS

66

67\#endif

\_dbus_file_exists

dbus_bool_t \_dbus_file_exists(const char \*file)

File interface.

**Definition** dbus-sysdeps-util-unix.c:564

\_dbus_delete_file

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_delete_file(const DBusString \*filename, DBusError \*error)

Deletes the given file.

**Definition** dbus-file-unix.c:441

\_dbus_create_file_exclusively

dbus_bool_t \_dbus_create_file_exclusively(const DBusString \*filename, DBusError \*error)

Creates the given file, failing if the file already exists.

**Definition** dbus-file-unix.c:395

\_dbus_string_save_to_file

dbus_bool_t \_dbus_string_save_to_file(const DBusString \*str, const DBusString \*filename, dbus_bool_t world_readable, DBusError \*error)

Writes a string out to a file.

**Definition** dbus-file-unix.c:208

\_dbus_make_file_world_readable

dbus_bool_t \_dbus_make_file_world_readable(const DBusString \*filename, DBusError \*error)

Makes the file readable by every user in the system.

**Definition** dbus-file-unix.c:368

\_dbus_file_get_contents

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_file_get_contents(DBusString \*str, const DBusString \*filename, DBusError \*error)

Appends the contents of the given file to the string, returning error code.

**Definition** dbus-file-unix.c:63

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusString

**Definition** dbus-string.h:47
