dbus-server-launchd.h

1/\* dbus-server-launchd.h Server methods for interacting with launchd.

2\* Copyright (C) 2008, Benjamin Reed \<rangerrick@befunk.com\>

3\* SPDX-License-Identifier: MIT

4\*

5\* Permission is hereby granted, free of charge, to any person

6\* obtaining a copy of this software and associated documentation

7\* files (the "Software"), to deal in the Software without

8\* restriction, including without limitation the rights to use, copy,

9\* modify, merge, publish, distribute, sublicense, and/or sell copies

10\* of the Software, and to permit persons to whom the Software is

11\* furnished to do so, subject to the following conditions:

12\*

13\* The above copyright notice and this permission notice shall be

14\* included in all copies or substantial portions of the Software.

15\*

16\* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,

17\* EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF

18\* MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND

19\* NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT

20\* HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,

21\* WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,

22\* OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER

23\* DEALINGS IN THE SOFTWARE.

24\*/

25

26\#ifndef DBUS_SERVER_LAUNCHD_H

27\#define DBUS_SERVER_LAUNCHD_H

28

29\#include \<dbus/dbus-internals.h\>

30\#include \<dbus/dbus-server-protected.h\>

31

32DBUS_BEGIN_DECLS

33

34DBusServer \* \_dbus_server_new_for_launchd (const char \*launchd_env_var, DBusError \* error);

35

36DBUS_END_DECLS

37\#endif /\* DBUS_SERVER_LAUNCHD_H \*/

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

\_dbus_server_new_for_launchd

DBusServer \* \_dbus_server_new_for_launchd(const char \*launchd_env_var, DBusError \*error)

Creates a new server from launchd.

**Definition** dbus-server-launchd.c:68

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusServer

Internals of DBusServer object.

**Definition** dbus-server-protected.h:59
