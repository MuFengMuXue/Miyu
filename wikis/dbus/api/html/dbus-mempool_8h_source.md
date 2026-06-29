dbus-mempool.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-mempool.h Memory pools

3 \*

4 \* Copyright (C) 2002 Red Hat, Inc.

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

25

26\#ifndef DBUS_MEMPOOL_H

27\#define DBUS_MEMPOOL_H

28

29\#include \<dbus/dbus-internals.h\>

30\#include \<dbus/dbus-memory.h\>

31\#include \<dbus/dbus-types.h\>

32

33DBUS_BEGIN_DECLS

34

35typedef struct DBusMemPool DBusMemPool;

36

37DBUS_PRIVATE_EXPORT

38DBusMemPool\* \_dbus_mem_pool_new (int element_size,

39 dbus_bool_t zero_elements);

40DBUS_PRIVATE_EXPORT

41void \_dbus_mem_pool_free (DBusMemPool \*pool);

42DBUS_PRIVATE_EXPORT

43void\* \_dbus_mem_pool_alloc (DBusMemPool \*pool);

44DBUS_PRIVATE_EXPORT

45dbus_bool_t \_dbus_mem_pool_dealloc (DBusMemPool \*pool,

46 void \*element);

47

48/\* if DBUS_ENABLE_STATS \*/

49void \_dbus_mem_pool_get_stats (DBusMemPool \*pool,

50 dbus_uint32_t \*in_use_p,

51 dbus_uint32_t \*in_free_list_p,

52 dbus_uint32_t \*allocated_p);

53

54DBUS_END_DECLS

55

56\#endif /\* DBUS_MEMPOOL_H \*/

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

\_dbus_mem_pool_alloc

DBUS_PRIVATE_EXPORT void \* \_dbus_mem_pool_alloc(DBusMemPool \*pool)

Allocates an object from the memory pool.

**Definition** dbus-mempool.c:227

\_dbus_mem_pool_dealloc

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_mem_pool_dealloc(DBusMemPool \*pool, void \*element)

Deallocates an object previously created with \_dbus_mem_pool_alloc().

**Definition** dbus-mempool.c:366

\_dbus_mem_pool_free

DBUS_PRIVATE_EXPORT void \_dbus_mem_pool_free(DBusMemPool \*pool)

Frees a memory pool (and all elements allocated from it).

**Definition** dbus-mempool.c:200

\_dbus_mem_pool_new

DBUS_PRIVATE_EXPORT DBusMemPool \* \_dbus_mem_pool_new(int element_size, dbus_bool_t zero_elements)

Creates a new memory pool, or returns NULL on failure.

**Definition** dbus-mempool.c:148

DBusMemPool

Internals fields of DBusMemPool.

**Definition** dbus-mempool.c:109

DBusMemPool::zero_elements

unsigned int zero_elements

whether to zero-init allocated elements

**Definition** dbus-mempool.c:112

DBusMemPool::element_size

size_t element_size

size of a single object in the pool

**Definition** dbus-mempool.c:110
