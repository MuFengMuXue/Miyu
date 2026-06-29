dbus-asv-util.h

1/\* dbus-asv-util.h - utility functions for a{sv}

2 \*

3 \* Copyright © 2011-2012 Nokia Corporation

4 \* Copyright © 2012-2013 Collabora Ltd.

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

22 \* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA

23 \* 02110-1301 USA

24 \*/

25

26\#ifndef DBUS_ASV_UTIL_H

27\#define DBUS_ASV_UTIL_H

28

29\#include \<dbus/dbus-internals.h\>

30

31DBUS_BEGIN_DECLS

32

33DBusMessage \*\_dbus_asv_new_method_return (DBusMessage \*message,

34 DBusMessageIter \*iter,

35 DBusMessageIter \*arr_iter);

36dbus_bool_t \_dbus_asv_close (DBusMessageIter \*iter,

37 DBusMessageIter \*arr_iter);

38void \_dbus_asv_abandon (DBusMessageIter \*iter,

39 DBusMessageIter \*arr_iter);

40

41dbus_bool_t \_dbus_asv_add_uint32 (DBusMessageIter \*arr_iter,

42 const char \*key,

43 dbus_uint32_t value);

44dbus_bool_t \_dbus_asv_add_string (DBusMessageIter \*arr_iter,

45 const char \*key,

46 const char \*value);

47dbus_bool_t \_dbus_asv_add_object_path (DBusMessageIter \*arr_iter,

48 const char \*key,

49 const char \*value);

50dbus_bool_t \_dbus_asv_add_fixed_array (DBusMessageIter \*arr_iter,

51 const char \*key,

52 char element_type,

53 const void \*value,

54 int n_elements);

55dbus_bool_t \_dbus_asv_add_byte_array (DBusMessageIter \*arr_iter,

56 const char \*key,

57 const void \*value,

58 int n_elements);

59dbus_bool_t \_dbus_asv_open_entry (DBusMessageIter \*arr_iter,

60 DBusMessageIter \*entry_iter,

61 const char \*key,

62 const char \*type,

63 DBusMessageIter \*var_iter);

64dbus_bool_t \_dbus_asv_close_entry (DBusMessageIter \*arr_iter,

65 DBusMessageIter \*entry_iter,

66 DBusMessageIter \*var_iter);

67void \_dbus_asv_abandon_entry (DBusMessageIter \*arr_iter,

68 DBusMessageIter \*entry_iter,

69 DBusMessageIter \*var_iter);

70dbus_bool_t \_dbus_asv_add_unix_fd (DBusMessageIter \*arr_iter,

71 const char \*key,

72 int value);

73

74\#endif

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBusMessageIter

DBusMessageIter struct; contains no public fields.

**Definition** dbus-message.h:64

DBusMessage

Internals of DBusMessage.

**Definition** dbus-message-private.h:102
