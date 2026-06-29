dbus-threads-internal.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-threads-internal.h D-Bus thread primitives

3 \*

4 \* Copyright (C) 2002, 2005 Red Hat Inc.

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

25\#ifndef DBUS_THREADS_INTERNAL_H

26\#define DBUS_THREADS_INTERNAL_H

27

28\#include \<dbus/dbus-macros.h\>

29\#include \<dbus/dbus-types.h\>

30\#include \<dbus/dbus-threads.h\>

31

41typedef struct DBusRMutex DBusRMutex;

42

47typedef struct DBusCMutex DBusCMutex;

48

51DBUS_BEGIN_DECLS

52

53DBUS_PRIVATE_EXPORT

54void \_dbus_rmutex_lock (DBusRMutex \*mutex);

55DBUS_PRIVATE_EXPORT

56void \_dbus_rmutex_unlock (DBusRMutex \*mutex);

57void \_dbus_rmutex_new_at_location (DBusRMutex \*\*location_p);

58void \_dbus_rmutex_free_at_location (DBusRMutex \*\*location_p);

59

60void \_dbus_cmutex_lock (DBusCMutex \*mutex);

61void \_dbus_cmutex_unlock (DBusCMutex \*mutex);

62void \_dbus_cmutex_new_at_location (DBusCMutex \*\*location_p);

63void \_dbus_cmutex_free_at_location (DBusCMutex \*\*location_p);

64

65DBusCondVar\* \_dbus_condvar_new (void);

66void \_dbus_condvar_free (DBusCondVar \*cond);

67void \_dbus_condvar_wait (DBusCondVar \*cond,

68 DBusCMutex \*mutex);

69dbus_bool_t \_dbus_condvar_wait_timeout (DBusCondVar \*cond,

70 DBusCMutex \*mutex,

71 int timeout_milliseconds);

72void \_dbus_condvar_wake_one (DBusCondVar \*cond);

73void \_dbus_condvar_new_at_location (DBusCondVar \*\*location_p);

74void \_dbus_condvar_free_at_location (DBusCondVar \*\*location_p);

75

76/\* Private to threading implementations and dbus-threads.c \*/

77

86DBUS_EMBEDDED_TESTS_EXPORT

87DBusRMutex \*\_dbus_platform_rmutex_new (void);

88

94DBUS_EMBEDDED_TESTS_EXPORT

95void \_dbus_platform_rmutex_free (DBusRMutex \*mutex);

96

107DBUS_EMBEDDED_TESTS_EXPORT

108void \_dbus_platform_rmutex_lock (DBusRMutex \*mutex);

109

115DBUS_EMBEDDED_TESTS_EXPORT

116void \_dbus_platform_rmutex_unlock (DBusRMutex \*mutex);

117

123DBUS_EMBEDDED_TESTS_EXPORT

124DBusCMutex \*\_dbus_platform_cmutex_new (void);

125

130DBUS_EMBEDDED_TESTS_EXPORT

131void \_dbus_platform_cmutex_free (DBusCMutex \*mutex);

132

146DBUS_EMBEDDED_TESTS_EXPORT

147void \_dbus_platform_cmutex_lock (DBusCMutex \*mutex);

148

154DBUS_EMBEDDED_TESTS_EXPORT

155void \_dbus_platform_cmutex_unlock (DBusCMutex \*mutex);

156

157DBusCondVar\* \_dbus_platform_condvar_new (void);

158void \_dbus_platform_condvar_free (DBusCondVar \*cond);

159void \_dbus_platform_condvar_wait (DBusCondVar \*cond,

160 DBusCMutex \*mutex);

161dbus_bool_t \_dbus_platform_condvar_wait_timeout (DBusCondVar \*cond,

162 DBusCMutex \*mutex,

163 int timeout_milliseconds);

164void \_dbus_platform_condvar_wake_one (DBusCondVar \*cond);

165

166DBUS_END_DECLS

167

168\#endif /\* DBUS_THREADS_INTERNAL_H \*/

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

\_dbus_rmutex_new_at_location

void \_dbus_rmutex_new_at_location(DBusRMutex \*\*location_p)

Creates a new mutex or creates a no-op mutex if threads are not initialized.

**Definition** dbus-threads.c:56

\_dbus_cmutex_free_at_location

void \_dbus_cmutex_free_at_location(DBusCMutex \*\*location_p)

Frees a DBusCMutex; does nothing if passed a NULL pointer.

**Definition** dbus-threads.c:110

\_dbus_condvar_new

DBusCondVar \* \_dbus_condvar_new(void)

Creates a new condition variable using the function supplied to dbus_threads_init(),...

**Definition** dbus-threads.c:184

\_dbus_condvar_free_at_location

void \_dbus_condvar_free_at_location(DBusCondVar \*\*location_p)

Frees a condition variable; does nothing if passed a NULL pointer.

**Definition** dbus-threads.c:227

\_dbus_rmutex_unlock

DBUS_PRIVATE_EXPORT void \_dbus_rmutex_unlock(DBusRMutex \*mutex)

Unlocks a mutex.

**Definition** dbus-threads.c:153

\_dbus_condvar_wait

void \_dbus_condvar_wait(DBusCondVar \*cond, DBusCMutex \*mutex)

Atomically unlocks the mutex and waits for the conditions variable to be signalled.

**Definition** dbus-threads.c:243

\_dbus_condvar_new_at_location

void \_dbus_condvar_new_at_location(DBusCondVar \*\*location_p)

This does the same thing as \_dbus_condvar_new.

**Definition** dbus-threads.c:202

\_dbus_cmutex_new_at_location

void \_dbus_cmutex_new_at_location(DBusCMutex \*\*location_p)

Creates a new mutex or creates a no-op mutex if threads are not initialized.

**Definition** dbus-threads.c:80

\_dbus_condvar_wake_one

void \_dbus_condvar_wake_one(DBusCondVar \*cond)

If there are threads waiting on the condition variable, wake up exactly one.

**Definition** dbus-threads.c:281

\_dbus_condvar_wait_timeout

dbus_bool_t \_dbus_condvar_wait_timeout(DBusCondVar \*cond, DBusCMutex \*mutex, int timeout_milliseconds)

Atomically unlocks the mutex and waits for the conditions variable to be signalled,...

**Definition** dbus-threads.c:264

\_dbus_cmutex_lock

void \_dbus_cmutex_lock(DBusCMutex \*mutex)

Locks a mutex.

**Definition** dbus-threads.c:139

\_dbus_cmutex_unlock

void \_dbus_cmutex_unlock(DBusCMutex \*mutex)

Unlocks a mutex.

**Definition** dbus-threads.c:167

\_dbus_rmutex_free_at_location

void \_dbus_rmutex_free_at_location(DBusRMutex \*\*location_p)

Frees a DBusRMutex; does nothing if passed a NULL pointer.

**Definition** dbus-threads.c:97

\_dbus_rmutex_lock

DBUS_PRIVATE_EXPORT void \_dbus_rmutex_lock(DBusRMutex \*mutex)

Locks a mutex.

**Definition** dbus-threads.c:125

\_dbus_condvar_free

void \_dbus_condvar_free(DBusCondVar \*cond)

Frees a conditional variable created with dbus_condvar_new(); does nothing if passed a NULL pointer.

**Definition** dbus-threads.c:215

DBusCMutex

**Definition** dbus-sysdeps-pthread.c:55

DBusCondVar

**Definition** dbus-sysdeps-pthread.c:59

DBusRMutex

**Definition** dbus-sysdeps-pthread.c:51
