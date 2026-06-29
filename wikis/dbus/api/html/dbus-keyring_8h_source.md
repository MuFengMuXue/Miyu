dbus-keyring.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-keyring.h Store secret cookies in your homedir

3 \*

4 \* Copyright (C) 2003 Red Hat Inc.

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

25\#ifndef DBUS_KEYRING_H

26\#define DBUS_KEYRING_H

27

28\#include \<dbus/dbus-macros.h\>

29\#include \<dbus/dbus-errors.h\>

30\#include \<dbus/dbus-string.h\>

31\#include \<dbus/dbus-credentials.h\>

32

33DBUS_BEGIN_DECLS

34

35typedef struct DBusKeyring DBusKeyring;

36

37DBusKeyring\* \_dbus_keyring_new_for_credentials (DBusCredentials \*credentials,

38 const DBusString \*context,

39 DBusError \*error);

40DBusKeyring\* \_dbus_keyring_ref (DBusKeyring \*keyring);

41void \_dbus_keyring_unref (DBusKeyring \*keyring);

42dbus_bool_t \_dbus_keyring_validate_context (const DBusString \*context);

43int \_dbus_keyring_get_best_key (DBusKeyring \*keyring,

44 DBusError \*error);

45dbus_bool_t \_dbus_keyring_is_for_credentials (DBusKeyring \*keyring,

46 DBusCredentials \*credentials);

47dbus_bool_t \_dbus_keyring_get_hex_key (DBusKeyring \*keyring,

48 int key_id,

49 DBusString \*hex_key);

50

51

52DBUS_END_DECLS

53

54\#endif /\* DBUS_KEYRING_H \*/

\_dbus_keyring_get_best_key

int \_dbus_keyring_get_best_key(DBusKeyring \*keyring, DBusError \*error)

Gets a recent key to use for authentication.

**Definition** dbus-keyring.c:934

\_dbus_keyring_validate_context

dbus_bool_t \_dbus_keyring_validate_context(const DBusString \*context)

Checks whether the context is a valid context.

**Definition** dbus-keyring.c:837

\_dbus_keyring_is_for_credentials

dbus_bool_t \_dbus_keyring_is_for_credentials(DBusKeyring \*keyring, DBusCredentials \*credentials)

Checks whether the keyring is for the same user as the given credentials.

**Definition** dbus-keyring.c:973

\_dbus_keyring_new_for_credentials

DBusKeyring \* \_dbus_keyring_new_for_credentials(DBusCredentials \*credentials, const DBusString \*context, DBusError \*error)

Creates a new keyring that lives in the ~/.dbus-keyrings directory of the user represented by credent...

**Definition** dbus-keyring.c:693

\_dbus_keyring_get_hex_key

dbus_bool_t \_dbus_keyring_get_hex_key(DBusKeyring \*keyring, int key_id, DBusString \*hex_key)

Gets the hex-encoded secret key for the given ID.

**Definition** dbus-keyring.c:992

\_dbus_keyring_ref

DBusKeyring \* \_dbus_keyring_ref(DBusKeyring \*keyring)

Increments reference count of the keyring.

**Definition** dbus-keyring.c:651

\_dbus_keyring_unref

void \_dbus_keyring_unref(DBusKeyring \*keyring)

Decrements refcount and finalizes if it reaches zero.

**Definition** dbus-keyring.c:665

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

DBusCredentials

**Definition** dbus-credentials.c:60

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusKeyring

Internals of DBusKeyring.

**Definition** dbus-keyring.c:112

DBusKeyring::credentials

DBusCredentials \* credentials

Credentials containing user the keyring is for.

**Definition** dbus-keyring.c:119

DBusString

**Definition** dbus-string.h:47
