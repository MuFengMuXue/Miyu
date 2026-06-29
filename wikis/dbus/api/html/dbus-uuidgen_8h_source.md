dbus-uuidgen.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-uuidgen.h The guts of the dbus-uuidgen binary live in libdbus, in this file.

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

25\#ifdef DBUS_INSIDE_DBUS_H

26\#error "You can't include dbus-uuidgen.h in the public header dbus.h"

27\#endif

28

29\#ifndef DBUS_UUIDGEN_H

30\#define DBUS_UUIDGEN_H

31

32\#include \<dbus/dbus-macros-internal.h\>

33\#include \<dbus/dbus-types.h\>

34\#include \<dbus/dbus-errors.h\>

35

36DBUS_BEGIN_DECLS

37

38DBUS_PRIVATE_EXPORT

39dbus_bool_t \_dbus_get_uuid (const char \*filename,

40 char \*\*uuid_p,

41 dbus_bool_t create_if_not_found,

42 DBusError \*error);

43DBUS_PRIVATE_EXPORT

44dbus_bool_t \_dbus_create_uuid (char \*\*uuid_p,

45 DBusError \*error);

46

47DBUS_END_DECLS

48

49\#endif /\* DBUS_UUIDGEN_H \*/

\_dbus_create_uuid

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_create_uuid(char \*\*uuid_p, DBusError \*error)

**Definition** dbus-uuidgen.c:121

\_dbus_get_uuid

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_get_uuid(const char \*filename, char \*\*uuid_p, dbus_bool_t create_if_not_found, DBusError \*error)

For use by the dbus-uuidgen binary ONLY, do not call this.

**Definition** dbus-uuidgen.c:85

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
