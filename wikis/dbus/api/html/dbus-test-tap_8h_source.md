dbus-test-tap.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-test-tap — TAP helpers for "embedded tests"

3 \*

4 \* Copyright © 2017 Collabora Ltd.

5 \* SPDX-License-Identifier: MIT

6 \*

7 \* Permission is hereby granted, free of charge, to any person

8 \* obtaining a copy of this software and associated documentation files

9 \* (the "Software"), to deal in the Software without restriction,

10 \* including without limitation the rights to use, copy, modify, merge,

11 \* publish, distribute, sublicense, and/or sell copies of the Software,

12 \* and to permit persons to whom the Software is furnished to do so,

13 \* subject to the following conditions:

14 \*

15 \* The above copyright notice and this permission notice shall be

16 \* included in all copies or substantial portions of the Software.

17 \*

18 \* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,

19 \* EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF

20 \* MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND

21 \* NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS

22 \* BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN

23 \* ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN

24 \* CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE

25 \* SOFTWARE.

26 \*/

27

28\#ifndef DBUS_TEST_TAP_H

29\#define DBUS_TEST_TAP_H

30

31\#include \<dbus/dbus-internals.h\>

32

33DBUS_EMBEDDED_TESTS_EXPORT

34void \_dbus_test_fatal (const char \*format,

35 ...) \_DBUS_GNUC_NORETURN \_DBUS_GNUC_PRINTF (1, 2);

36

37DBUS_EMBEDDED_TESTS_EXPORT

38void \_dbus_test_diag (const char \*format,

39 ...) \_DBUS_GNUC_PRINTF (1, 2);

40

41DBUS_EMBEDDED_TESTS_EXPORT

42void \_dbus_test_skip_all (const char \*format,

43 ...) \_DBUS_GNUC_NORETURN \_DBUS_GNUC_PRINTF (1, 2);

44

45DBUS_EMBEDDED_TESTS_EXPORT

46void \_dbus_test_ok (const char \*format,

47 ...) \_DBUS_GNUC_PRINTF (1, 2);

48DBUS_EMBEDDED_TESTS_EXPORT

49void \_dbus_test_not_ok (const char \*format,

50 ...) \_DBUS_GNUC_PRINTF (1, 2);

51DBUS_EMBEDDED_TESTS_EXPORT

52void \_dbus_test_skip (const char \*format,

53 ...) \_DBUS_GNUC_PRINTF (1, 2);

54

55DBUS_EMBEDDED_TESTS_EXPORT

56void \_dbus_test_check_memleaks (const char \*test_name);

57

58DBUS_EMBEDDED_TESTS_EXPORT

59int \_dbus_test_done_testing (void);

60

61\#define \_dbus_test_check(a) do { \\

62 if (!(a)) \\

63 \_dbus_test_not_ok ("%s:%d - '%s' failed\n", \_\_FILE\_\_, \_\_LINE\_\_, \#a); \\

64 } while (0)

65

66\#endif
