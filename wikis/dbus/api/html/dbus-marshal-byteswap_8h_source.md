dbus-marshal-byteswap.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-marshal-byteswap.h Swap a block of marshaled data

3 \*

4 \* Copyright (C) 2005 Red Hat, Inc.

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

26\#ifndef DBUS_MARSHAL_BYTESWAP_H

27\#define DBUS_MARSHAL_BYTESWAP_H

28

29\#include \<dbus/dbus-protocol.h\>

30\#include \<dbus/dbus-marshal-recursive.h\>

31

32DBUS_PRIVATE_EXPORT

33void \_dbus_marshal_byteswap (const DBusString \*signature,

34 int signature_start,

35 int old_byte_order,

36 int new_byte_order,

37 DBusString \*value_str,

38 int value_pos);

39

40\#endif /\* DBUS_MARSHAL_BYTESWAP_H \*/

\_dbus_marshal_byteswap

DBUS_PRIVATE_EXPORT void \_dbus_marshal_byteswap(const DBusString \*signature, int signature_start, int old_byte_order, int new_byte_order, DBusString \*value_str, int value_pos)

Byteswaps the marshaled data in the given value_str.

**Definition** dbus-marshal-byteswap.c:224

DBusString

**Definition** dbus-string.h:47
