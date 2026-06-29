dbus-nonce.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-nonce.h Nonce handling functions used by nonce-tcp (internal to D-Bus implementation)

3 \*

4 \* Copyright (C) 2009 Klaralvdalens Datakonsult AB, a KDAB Group company, info@kdab.net

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

22 \* Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

23 \*

24 \*/

25\#ifndef DBUS_NONCE_H

26\#define DBUS_NONCE_H

27

28\#include \<dbus/dbus-macros.h\>

29\#include \<dbus/dbus-types.h\>

30\#include \<dbus/dbus-errors.h\>

31\#include \<dbus/dbus-string.h\>

32\#include \<dbus/dbus-sysdeps.h\>

33

34DBUS_BEGIN_DECLS

35

36typedef struct DBusNonceFile DBusNonceFile;

37

38// server

39

40dbus_bool_t \_dbus_noncefile_create (DBusNonceFile \*\*noncefile_out,

41 DBusError \*error);

42

43dbus_bool_t \_dbus_noncefile_delete (DBusNonceFile \*\*noncefile_location,

44 DBusError \*error);

45

46dbus_bool_t \_dbus_noncefile_check_nonce (DBusSocket fd,

47 const DBusNonceFile \*noncefile,

48 DBusError \*error);

49

50const DBusString\* \_dbus_noncefile_get_path (const DBusNonceFile \*noncefile);

51

52DBusSocket \_dbus_accept_with_noncefile(DBusSocket listen_fd,

53 const DBusNonceFile \*noncefile);

54

55// shared

56

57dbus_bool_t \_dbus_read_nonce (const DBusString \*fname,

58 DBusString \*nonce,

59 DBusError \*error);

60

61// client

62

63dbus_bool_t \_dbus_send_nonce (DBusSocket fd,

64 const DBusString \*noncefile,

65 DBusError \*error);

66

67DBUS_END_DECLS

68

69\#endif /\* DBUS_NONCE_H \*/

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

DBusNonceFile

**Definition** dbus-nonce.c:36

DBusSocket

Socket interface.

**Definition** dbus-sysdeps.h:185

DBusString

**Definition** dbus-string.h:47
