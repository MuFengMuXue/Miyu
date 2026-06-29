dbus-macros-internal.h

1/\*

2 \* Copyright © 2010-2015 Ralf Habacker

3 \* Copyright © 2015-2019 Collabora Ltd.

4 \*

5 \* SPDX-License-Identifier: AFL-2.1 OR GPL-2.0-or-later

6 \*

7 \* Licensed under the Academic Free License version 2.1

8 \*

9 \* This program is free software; you can redistribute it and/or modify

10 \* it under the terms of the GNU General Public License as published by

11 \* the Free Software Foundation; either version 2 of the License, or

12 \* (at your option) any later version.

13 \*

14 \* This program is distributed in the hope that it will be useful,

15 \* but WITHOUT ANY WARRANTY; without even the implied warranty of

16 \* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the

17 \* GNU General Public License for more details.

18 \*

19 \* You should have received a copy of the GNU General Public License along

20 \* with this program. If not, see \<https://www.gnu.org/licenses/\>.

21 \*/

22

23\#ifdef DBUS_INSIDE_DBUS_H

24\#error "You can't include dbus-macros-internal.h in the public header dbus.h"

25\#endif

26

27\#ifndef DBUS_MACROS_INTERNAL_H

28\#define DBUS_MACROS_INTERNAL_H

29

30\#include \<dbus/dbus-macros.h\>

31

32\#ifdef DBUS_ENABLE_INTRUSIVE_TESTS

33\# define DBUS_INTRUSIVE_TESTS_EXPORT DBUS_PRIVATE_EXPORT

34\#else

35\# define DBUS_INTRUSIVE_TESTS_EXPORT /\* nothing \*/

36\#endif

37\#define DBUS_EMBEDDED_TESTS_EXPORT DBUS_INTRUSIVE_TESTS_EXPORT

38

39\#if defined(DBUS_PRIVATE_EXPORT)

40 /\* value forced by compiler command line, don't redefine \*/

41\#elif defined(\_WIN32)

42\# if defined(DBUS_STATIC_BUILD)

43\# define DBUS_PRIVATE_EXPORT /\* no decoration \*/

44\# elif defined(dbus_1_EXPORTS)

45\# define DBUS_PRIVATE_EXPORT \_\_declspec(dllexport)

46\# else

47\# define DBUS_PRIVATE_EXPORT \_\_declspec(dllimport)

48\# endif

49\#elif defined(\_\_GNUC\_\_) && \_\_GNUC\_\_ \>= 4

50\# define DBUS_PRIVATE_EXPORT \_\_attribute\_\_ ((\_\_visibility\_\_ ("default")))

51\#else

52\# define DBUS_PRIVATE_EXPORT /\* no decoration \*/

53\#endif

54

55\#endif
