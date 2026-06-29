dbus-test.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-test.h Declarations of test functions.

3 \*

4 \* Copyright (C) 2002 Red Hat Inc.

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

26\#ifndef DBUS_TEST_H

27\#define DBUS_TEST_H

28

29\#include \<dbus/dbus-types.h\>

30\#include \<dbus/dbus-string.h\>

31\#include \<dbus/dbus-marshal-validate.h\>

32

33/\* Only things that are in libdbus-1.la and used from libdbus-internal.la

34 \* need to have DBUS_PRIVATE_EXPORT. If you get

35 \*

36 \* warning: 'foo' redeclared without dllimport attribute: previous

37 \* dllimport ignored \[-Wattributes\]

38 \*

39 \* then you have added too many.

40 \*/

41

42DBUS_PRIVATE_EXPORT

43dbus_bool_t \_dbus_marshal_test (const char \*test_data_dir);

44

45DBUS_PRIVATE_EXPORT

46dbus_bool_t \_dbus_keyring_test (const char \*test_data_dir);

47

48DBUS_PRIVATE_EXPORT

49dbus_bool_t \_dbus_data_slot_test (const char \*test_data_dir);

50

51DBUS_PRIVATE_EXPORT

52dbus_bool_t \_dbus_memory_test (const char \*test_data_dir);

53

54DBUS_PRIVATE_EXPORT

55dbus_bool_t \_dbus_object_tree_test (const char \*test_data_dir);

56

57\#endif /\* DBUS_TEST_H \*/
