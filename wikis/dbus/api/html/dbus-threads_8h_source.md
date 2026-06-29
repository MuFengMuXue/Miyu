dbus-threads.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-threads.h D-Bus threads handling

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

25\#if !defined (DBUS_INSIDE_DBUS_H) && !defined (DBUS_COMPILATION)

26\#error "Only \<dbus/dbus.h\> can be included directly, this file may disappear or change contents."

27\#endif

28

29\#ifndef DBUS_THREADS_H

30\#define DBUS_THREADS_H

31

32\#include \<dbus/dbus-macros.h\>

33\#include \<dbus/dbus-types.h\>

34

35DBUS_BEGIN_DECLS

36

43typedef struct DBusMutex DBusMutex;

45typedef struct DBusCondVar DBusCondVar;

46

48typedef DBusMutex\* (\* DBusMutexNewFunction) (void);

50typedef void (\* DBusMutexFreeFunction) (DBusMutex \*mutex);

52typedef dbus_bool_t (\* DBusMutexLockFunction) (DBusMutex \*mutex);

54typedef dbus_bool_t (\* DBusMutexUnlockFunction) (DBusMutex \*mutex);

55

63typedef DBusMutex\* (\* DBusRecursiveMutexNewFunction) (void);

66typedef void (\* DBusRecursiveMutexFreeFunction) (DBusMutex \*mutex);

70typedef void (\* DBusRecursiveMutexLockFunction) (DBusMutex \*mutex);

74typedef void (\* DBusRecursiveMutexUnlockFunction) (DBusMutex \*mutex);

75

79typedef DBusCondVar\* (\* DBusCondVarNewFunction) (void);

82typedef void (\* DBusCondVarFreeFunction) (DBusCondVar \*cond);

83

94typedef void (\* DBusCondVarWaitFunction) (DBusCondVar \*cond,

95 DBusMutex \*mutex);

96

103typedef dbus_bool_t (\* DBusCondVarWaitTimeoutFunction) (DBusCondVar \*cond,

104 DBusMutex \*mutex,

105 int timeout_milliseconds);

110typedef void (\* DBusCondVarWakeOneFunction) (DBusCondVar \*cond);

111

116typedef void (\* DBusCondVarWakeAllFunction) (DBusCondVar \*cond);

117

123typedef enum

124{

125 DBUS_THREAD_FUNCTIONS_MUTEX_NEW_MASK = 1 \<\< 0,

126 DBUS_THREAD_FUNCTIONS_MUTEX_FREE_MASK = 1 \<\< 1,

127 DBUS_THREAD_FUNCTIONS_MUTEX_LOCK_MASK = 1 \<\< 2,

128 DBUS_THREAD_FUNCTIONS_MUTEX_UNLOCK_MASK = 1 \<\< 3,

129 DBUS_THREAD_FUNCTIONS_CONDVAR_NEW_MASK = 1 \<\< 4,

130 DBUS_THREAD_FUNCTIONS_CONDVAR_FREE_MASK = 1 \<\< 5,

131 DBUS_THREAD_FUNCTIONS_CONDVAR_WAIT_MASK = 1 \<\< 6,

132 DBUS_THREAD_FUNCTIONS_CONDVAR_WAIT_TIMEOUT_MASK = 1 \<\< 7,

133 DBUS_THREAD_FUNCTIONS_CONDVAR_WAKE_ONE_MASK = 1 \<\< 8,

134 DBUS_THREAD_FUNCTIONS_CONDVAR_WAKE_ALL_MASK = 1 \<\< 9,

135 DBUS_THREAD_FUNCTIONS_RECURSIVE_MUTEX_NEW_MASK = 1 \<\< 10,

136 DBUS_THREAD_FUNCTIONS_RECURSIVE_MUTEX_FREE_MASK = 1 \<\< 11,

137 DBUS_THREAD_FUNCTIONS_RECURSIVE_MUTEX_LOCK_MASK = 1 \<\< 12,

138 DBUS_THREAD_FUNCTIONS_RECURSIVE_MUTEX_UNLOCK_MASK = 1 \<\< 13,

139 DBUS_THREAD_FUNCTIONS_ALL_MASK = (1 \<\< 14) - 1

140} DBusThreadFunctionsMask;

141

154typedef struct

155{

156 unsigned int mask;

158 DBusMutexNewFunction mutex_new;

159 DBusMutexFreeFunction mutex_free;

160 DBusMutexLockFunction mutex_lock;

161 DBusMutexUnlockFunction mutex_unlock;

163 DBusCondVarNewFunction condvar_new;

164 DBusCondVarFreeFunction condvar_free;

165 DBusCondVarWaitFunction condvar_wait;

166 DBusCondVarWaitTimeoutFunction condvar_wait_timeout;

167 DBusCondVarWakeOneFunction condvar_wake_one;

168 DBusCondVarWakeAllFunction condvar_wake_all;

170 DBusRecursiveMutexNewFunction recursive_mutex_new;

171 DBusRecursiveMutexFreeFunction recursive_mutex_free;

172 DBusRecursiveMutexLockFunction recursive_mutex_lock;

173 DBusRecursiveMutexUnlockFunction recursive_mutex_unlock;

175 void (\* padding1) (void);

176 void (\* padding2) (void);

177 void (\* padding3) (void);

178 void (\* padding4) (void);

180} DBusThreadFunctions;

181

182DBUS_EXPORT

183dbus_bool_t dbus_threads_init (const DBusThreadFunctions \*functions);

184DBUS_EXPORT

185dbus_bool_t dbus_threads_init_default (void);

186

189DBUS_END_DECLS

190

191\#endif /\* DBUS_THREADS_H \*/

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

DBusCondVarWaitTimeoutFunction

dbus_bool_t(\* DBusCondVarWaitTimeoutFunction)(DBusCondVar \*cond, DBusMutex \*mutex, int timeout_milliseconds)

Waits on a condition variable with a timeout.

**Definition** dbus-threads.h:103

DBusCondVarWakeOneFunction

void(\* DBusCondVarWakeOneFunction)(DBusCondVar \*cond)

Wakes one waiting thread on a condition variable.

**Definition** dbus-threads.h:110

DBusMutexNewFunction

DBusMutex \*(\* DBusMutexNewFunction)(void)

Deprecated, provide DBusRecursiveMutexNewFunction instead.

**Definition** dbus-threads.h:48

DBusMutexLockFunction

dbus_bool_t(\* DBusMutexLockFunction)(DBusMutex \*mutex)

Deprecated, provide DBusRecursiveMutexLockFunction instead.

**Definition** dbus-threads.h:52

DBusRecursiveMutexNewFunction

DBusMutex \*(\* DBusRecursiveMutexNewFunction)(void)

Creates a new recursively-lockable mutex, or returns NULL if not enough memory.

**Definition** dbus-threads.h:63

dbus_threads_init_default

dbus_bool_t dbus_threads_init_default(void)

Initializes threads.

**Definition** dbus-threads.c:442

DBusMutexUnlockFunction

dbus_bool_t(\* DBusMutexUnlockFunction)(DBusMutex \*mutex)

Deprecated, provide DBusRecursiveMutexUnlockFunction instead.

**Definition** dbus-threads.h:54

DBusMutex

struct DBusMutex DBusMutex

An opaque mutex type provided by the DBusThreadFunctions implementation installed by dbus_threads_ini...

**Definition** dbus-threads.h:43

DBusRecursiveMutexFreeFunction

void(\* DBusRecursiveMutexFreeFunction)(DBusMutex \*mutex)

Frees a recursively-lockable mutex.

**Definition** dbus-threads.h:66

DBusCondVarWakeAllFunction

void(\* DBusCondVarWakeAllFunction)(DBusCondVar \*cond)

Wakes all waiting threads on a condition variable.

**Definition** dbus-threads.h:116

DBusRecursiveMutexUnlockFunction

void(\* DBusRecursiveMutexUnlockFunction)(DBusMutex \*mutex)

Unlocks a recursively-lockable mutex.

**Definition** dbus-threads.h:74

DBusCondVarWaitFunction

void(\* DBusCondVarWaitFunction)(DBusCondVar \*cond, DBusMutex \*mutex)

Waits on a condition variable.

**Definition** dbus-threads.h:94

DBusCondVarNewFunction

DBusCondVar \*(\* DBusCondVarNewFunction)(void)

Creates a new condition variable.

**Definition** dbus-threads.h:79

DBusCondVarFreeFunction

void(\* DBusCondVarFreeFunction)(DBusCondVar \*cond)

Frees a condition variable.

**Definition** dbus-threads.h:82

DBusRecursiveMutexLockFunction

void(\* DBusRecursiveMutexLockFunction)(DBusMutex \*mutex)

Locks a recursively-lockable mutex.

**Definition** dbus-threads.h:70

dbus_threads_init

dbus_bool_t dbus_threads_init(const DBusThreadFunctions \*functions)

Initializes threads, like dbus_threads_init_default().

**Definition** dbus-threads.c:395

DBusMutexFreeFunction

void(\* DBusMutexFreeFunction)(DBusMutex \*mutex)

Deprecated, provide DBusRecursiveMutexFreeFunction instead.

**Definition** dbus-threads.h:50

DBusThreadFunctionsMask

DBusThreadFunctionsMask

Flags indicating which functions are present in DBusThreadFunctions.

**Definition** dbus-threads.h:124

DBusCondVar

**Definition** dbus-sysdeps-pthread.c:59

DBusCondVar::cond

pthread_cond_t cond

the condition

**Definition** dbus-sysdeps-pthread.c:60

DBusThreadFunctions

Functions that must be implemented to make the D-Bus library thread-aware.

**Definition** dbus-threads.h:155

DBusThreadFunctions::mutex_free

DBusMutexFreeFunction mutex_free

Function to free a mutex; optional and deprecated.

**Definition** dbus-threads.h:159

DBusThreadFunctions::recursive_mutex_unlock

DBusRecursiveMutexUnlockFunction recursive_mutex_unlock

Function to unlock a recursive mutex.

**Definition** dbus-threads.h:173

DBusThreadFunctions::condvar_wake_all

DBusCondVarWakeAllFunction condvar_wake_all

Function to wake all threads waiting on the condition.

**Definition** dbus-threads.h:168

DBusThreadFunctions::condvar_new

DBusCondVarNewFunction condvar_new

Function to create a condition variable.

**Definition** dbus-threads.h:163

DBusThreadFunctions::mutex_lock

DBusMutexLockFunction mutex_lock

Function to lock a mutex; optional and deprecated.

**Definition** dbus-threads.h:160

DBusThreadFunctions::mutex_unlock

DBusMutexUnlockFunction mutex_unlock

Function to unlock a mutex; optional and deprecated.

**Definition** dbus-threads.h:161

DBusThreadFunctions::mutex_new

DBusMutexNewFunction mutex_new

Function to create a mutex; optional and deprecated.

**Definition** dbus-threads.h:158

DBusThreadFunctions::condvar_wake_one

DBusCondVarWakeOneFunction condvar_wake_one

Function to wake one thread waiting on the condition.

**Definition** dbus-threads.h:167

DBusThreadFunctions::condvar_wait_timeout

DBusCondVarWaitTimeoutFunction condvar_wait_timeout

Function to wait on a condition with a timeout.

**Definition** dbus-threads.h:166

DBusThreadFunctions::recursive_mutex_free

DBusRecursiveMutexFreeFunction recursive_mutex_free

Function to free a recursive mutex.

**Definition** dbus-threads.h:171

DBusThreadFunctions::mask

unsigned int mask

Mask indicating which functions are present.

**Definition** dbus-threads.h:156

DBusThreadFunctions::condvar_free

DBusCondVarFreeFunction condvar_free

Function to free a condition variable.

**Definition** dbus-threads.h:164

DBusThreadFunctions::condvar_wait

DBusCondVarWaitFunction condvar_wait

Function to wait on a condition.

**Definition** dbus-threads.h:165

DBusThreadFunctions::recursive_mutex_lock

DBusRecursiveMutexLockFunction recursive_mutex_lock

Function to lock a recursive mutex.

**Definition** dbus-threads.h:172

DBusThreadFunctions::recursive_mutex_new

DBusRecursiveMutexNewFunction recursive_mutex_new

Function to create a recursive mutex.

**Definition** dbus-threads.h:170
