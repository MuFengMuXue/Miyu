dbus-sha.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-sha.h SHA-1 implementation

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

25\#ifndef DBUS_SHA_H

26\#define DBUS_SHA_H

27

28\#include \<dbus/dbus-macros.h\>

29\#include \<dbus/dbus-errors.h\>

30\#include \<dbus/dbus-string.h\>

31

32DBUS_BEGIN_DECLS

33

34typedef struct DBusSHAContext DBusSHAContext;

35

39struct DBusSHAContext

40{

41 dbus_uint32_t digest\[5\];

42 dbus_uint32_t count_lo;

43 dbus_uint32_t count_hi;

44 dbus_uint32_t data\[16\];

45};

46

47void \_dbus_sha_init (DBusSHAContext \*context);

48void \_dbus_sha_update (DBusSHAContext \*context,

49 const DBusString \*data);

50dbus_bool_t \_dbus_sha_final (DBusSHAContext \*context,

51 DBusString \*results);

52DBUS_EMBEDDED_TESTS_EXPORT

53dbus_bool_t \_dbus_sha_compute (const DBusString \*data,

54 DBusString \*ascii_output);

55

56DBUS_END_DECLS

57

58\#endif /\* DBUS_SHA_H \*/

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

\_dbus_sha_compute

DBUS_EMBEDDED_TESTS_EXPORT dbus_bool_t \_dbus_sha_compute(const DBusString \*data, DBusString \*ascii_output)

Computes the ASCII hex-encoded shasum of the given data and appends it to the output string.

**Definition** dbus-sha.c:484

\_dbus_sha_init

void \_dbus_sha_init(DBusSHAContext \*context)

Initializes the SHA context.

**Definition** dbus-sha.c:421

\_dbus_sha_update

void \_dbus_sha_update(DBusSHAContext \*context, const DBusString \*data)

Feeds more data into an existing shasum computation.

**Definition** dbus-sha.c:433

\_dbus_sha_final

dbus_bool_t \_dbus_sha_final(DBusSHAContext \*context, DBusString \*results)

SHA finalization.

**Definition** dbus-sha.c:457

DBusSHAContext

Struct storing state of the SHA algorithm.

**Definition** dbus-sha.h:40

DBusSHAContext::digest

dbus_uint32_t digest\[5\]

Message digest.

**Definition** dbus-sha.h:41

DBusSHAContext::data

dbus_uint32_t data\[16\]

SHA data buffer.

**Definition** dbus-sha.h:44

DBusSHAContext::count_lo

dbus_uint32_t count_lo

64-bit bit count

**Definition** dbus-sha.h:42

DBusSHAContext::count_hi

dbus_uint32_t count_hi

No clue.

**Definition** dbus-sha.h:43

DBusString

**Definition** dbus-string.h:47
