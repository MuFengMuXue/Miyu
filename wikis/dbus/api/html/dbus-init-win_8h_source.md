dbus-init-win.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\*

3 \* Copyright © 2013 Intel Corporation

4 \* SPDX-License-Identifier: AFL-2.1 OR GPL-2.0-or-later

5 \*

6 \* Do not include other private headers in this one, particularly

7 \* dbus-sysdeps.h: it gets included into C++ code which is not

8 \* compatible with our use of \<stdatomic.h\>.

9 \*/

10

11\#ifndef DBUS_INIT_WIN_H

12\#define DBUS_INIT_WIN_H

13

14void \_dbus_threads_windows_init_global (void);

15void \_dbus_threads_windows_ensure_ctor_linked (void);

16

17\#endif
