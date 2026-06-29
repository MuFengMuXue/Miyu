dbus-dataslot.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-dataslot.h storing data on objects

3 \*

4 \* Copyright (C) 2003 Red Hat, Inc.

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

25\#ifndef DBUS_DATASLOT_H

26\#define DBUS_DATASLOT_H

27

28\#include \<dbus/dbus-internals.h\>

29

30DBUS_BEGIN_DECLS

31

32typedef struct DBusDataSlotAllocator DBusDataSlotAllocator;

33typedef struct DBusDataSlotList DBusDataSlotList;

34

36typedef struct DBusDataSlot DBusDataSlot;

38struct DBusDataSlot

39{

40 void \*data;

41 DBusFreeFunction free_data_func;

42};

43

44typedef struct DBusAllocatedSlot DBusAllocatedSlot;

45

48struct DBusAllocatedSlot

49{

50 dbus_int32_t slot_id;

51 int refcount;

52};

53

57struct DBusDataSlotAllocator

58{

59 DBusAllocatedSlot \*allocated_slots;

60 int n_allocated_slots;

61 int n_used_slots;

62 DBusGlobalLock lock;

63};

64

65\#define \_DBUS_DATA_SLOT_ALLOCATOR_INIT(x) { NULL, 0, 0, x }

66

71struct DBusDataSlotList

72{

73 DBusDataSlot \*slots;

74 int n_slots;

75};

76

77dbus_bool_t \_dbus_data_slot_allocator_init (DBusDataSlotAllocator \*allocator,

78 DBusGlobalLock lock);

79dbus_bool_t \_dbus_data_slot_allocator_alloc (DBusDataSlotAllocator \*allocator,

80 int \*slot_id_p);

81void \_dbus_data_slot_allocator_free (DBusDataSlotAllocator \*allocator,

82 int \*slot_id_p);

83void \_dbus_data_slot_list_init (DBusDataSlotList \*list);

84dbus_bool_t \_dbus_data_slot_list_set (DBusDataSlotAllocator \*allocator,

85 DBusDataSlotList \*list,

86 int slot,

87 void \*data,

88 DBusFreeFunction free_data_func,

89 DBusFreeFunction \*old_free_func,

90 void \*\*old_data);

91void\* \_dbus_data_slot_list_get (DBusDataSlotAllocator \*allocator,

92 DBusDataSlotList \*list,

93 int slot);

94void \_dbus_data_slot_list_clear (DBusDataSlotList \*list);

95void \_dbus_data_slot_list_free (DBusDataSlotList \*list);

96

97

98DBUS_END_DECLS

99

100\#endif /\* DBUS_DATASLOT_H \*/

\_dbus_data_slot_allocator_free

void \_dbus_data_slot_allocator_free(DBusDataSlotAllocator \*allocator, int \*slot_id_p)

Deallocates an ID previously allocated with \_dbus_data_slot_allocator_alloc().

**Definition** dbus-dataslot.c:157

\_dbus_data_slot_list_clear

void \_dbus_data_slot_list_clear(DBusDataSlotList \*list)

Frees all data slots contained in the list, calling application-provided free functions if they exist...

**Definition** dbus-dataslot.c:320

\_dbus_data_slot_allocator_init

dbus_bool_t \_dbus_data_slot_allocator_init(DBusDataSlotAllocator \*allocator, DBusGlobalLock lock)

Initializes a data slot allocator object, used to assign integer IDs for data slots.

**Definition** dbus-dataslot.c:49

\_dbus_data_slot_list_init

void \_dbus_data_slot_list_init(DBusDataSlotList \*list)

Initializes a slot list.

**Definition** dbus-dataslot.c:200

\_dbus_data_slot_list_free

void \_dbus_data_slot_list_free(DBusDataSlotList \*list)

Frees the data slot list and all data slots contained in it, calling application-provided free functi...

**Definition** dbus-dataslot.c:343

\_dbus_data_slot_list_get

void \* \_dbus_data_slot_list_get(DBusDataSlotAllocator \*allocator, DBusDataSlotList \*list, int slot)

Retrieves data previously set with \_dbus_data_slot_list_set_data().

**Definition** dbus-dataslot.c:288

\_dbus_data_slot_list_set

dbus_bool_t \_dbus_data_slot_list_set(DBusDataSlotAllocator \*allocator, DBusDataSlotList \*list, int slot, void \*data, DBusFreeFunction free_data_func, DBusFreeFunction \*old_free_func, void \*\*old_data)

Stores a pointer in the data slot list, along with an optional function to be used for freeing the da...

**Definition** dbus-dataslot.c:224

\_dbus_data_slot_allocator_alloc

dbus_bool_t \_dbus_data_slot_allocator_alloc(DBusDataSlotAllocator \*allocator, int \*slot_id_p)

Allocates an integer ID to be used for storing data in a DBusDataSlotList.

**Definition** dbus-dataslot.c:72

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

DBusFreeFunction

void(\* DBusFreeFunction)(void \*memory)

The type of a function which frees a block of memory.

**Definition** dbus-memory.h:65

DBusAllocatedSlot

An allocated slot for storing data.

**Definition** dbus-dataslot.h:49

DBusAllocatedSlot::refcount

int refcount

Number of uses of the slot.

**Definition** dbus-dataslot.h:51

DBusAllocatedSlot::slot_id

dbus_int32_t slot_id

ID of this slot.

**Definition** dbus-dataslot.h:50

DBusDataSlotAllocator

An allocator that tracks a set of slot IDs.

**Definition** dbus-dataslot.h:58

DBusDataSlotAllocator::allocated_slots

DBusAllocatedSlot \* allocated_slots

Allocated slots.

**Definition** dbus-dataslot.h:59

DBusDataSlotAllocator::n_allocated_slots

int n_allocated_slots

number of slots malloc'd

**Definition** dbus-dataslot.h:60

DBusDataSlotAllocator::lock

DBusGlobalLock lock

index of thread lock

**Definition** dbus-dataslot.h:62

DBusDataSlotAllocator::n_used_slots

int n_used_slots

number of slots used

**Definition** dbus-dataslot.h:61

DBusDataSlotList

Data structure that stores the actual user data set at a given slot.

**Definition** dbus-dataslot.h:72

DBusDataSlotList::n_slots

int n_slots

Slots we have storage for in data_slots.

**Definition** dbus-dataslot.h:74

DBusDataSlotList::slots

DBusDataSlot \* slots

Data slots.

**Definition** dbus-dataslot.h:73

DBusDataSlot

DBusDataSlot is used to store application data on the connection.

**Definition** dbus-dataslot.h:39

DBusDataSlot::data

void \* data

The application data.

**Definition** dbus-dataslot.h:40

DBusDataSlot::free_data_func

DBusFreeFunction free_data_func

Free the application data.

**Definition** dbus-dataslot.h:41
