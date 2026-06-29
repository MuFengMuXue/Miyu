dbus-list.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-list.h Generic linked list utility (internal to D-Bus implementation)

3 \*

4 \* Copyright (C) 2002, 2003 Red Hat, Inc.

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

26\#ifndef DBUS_LIST_H

27\#define DBUS_LIST_H

28

29\#include \<dbus/dbus-internals.h\>

30\#include \<dbus/dbus-memory.h\>

31\#include \<dbus/dbus-types.h\>

32\#include \<dbus/dbus-sysdeps.h\>

33

34DBUS_BEGIN_DECLS

35

36struct DBusList

37{

38 DBusList \*prev;

39 DBusList \*next;

40 void \*data;

41};

42DBUS_PRIVATE_EXPORT

43dbus_bool_t \_dbus_list_append (DBusList \*\*list,

44 void \*data);

45DBUS_PRIVATE_EXPORT

46dbus_bool_t \_dbus_list_prepend (DBusList \*\*list,

47 void \*data);

48dbus_bool_t \_dbus_list_insert_before (DBusList \*\*list,

49 DBusList \*before_this_link,

50 void \*data);

51DBUS_PRIVATE_EXPORT

52dbus_bool_t \_dbus_list_insert_after (DBusList \*\*list,

53 DBusList \*after_this_link,

54 void \*data);

55DBUS_PRIVATE_EXPORT

56void \_dbus_list_insert_before_link (DBusList \*\*list,

57 DBusList \*before_this_link,

58 DBusList \*link);

59DBUS_PRIVATE_EXPORT

60void \_dbus_list_insert_after_link (DBusList \*\*list,

61 DBusList \*after_this_link,

62 DBusList \*link);

63DBUS_PRIVATE_EXPORT

64dbus_bool_t \_dbus_list_remove (DBusList \*\*list,

65 void \*data);

66DBUS_PRIVATE_EXPORT

67dbus_bool_t \_dbus_list_remove_last (DBusList \*\*list,

68 void \*data);

69DBUS_PRIVATE_EXPORT

70void \_dbus_list_remove_link (DBusList \*\*list,

71 DBusList \*link);

72DBUS_PRIVATE_EXPORT

73DBusList\* \_dbus_list_find_last (DBusList \*\*list,

74 void \*data);

75DBUS_PRIVATE_EXPORT

76void \_dbus_list_clear (DBusList \*\*list);

77DBUS_PRIVATE_EXPORT

78void \_dbus_list_clear_full (DBusList \*\*list,

79 DBusFreeFunction function);

80DBUS_PRIVATE_EXPORT

81DBusList\* \_dbus_list_get_first_link (DBusList \*\*list);

82DBUS_PRIVATE_EXPORT

83DBusList\* \_dbus_list_get_last_link (DBusList \*\*list);

84DBUS_PRIVATE_EXPORT

85void\* \_dbus_list_get_last (DBusList \*\*list);

86DBUS_PRIVATE_EXPORT

87void\* \_dbus_list_get_first (DBusList \*\*list);

88DBUS_PRIVATE_EXPORT

89void\* \_dbus_list_pop_first (DBusList \*\*list);

90DBUS_PRIVATE_EXPORT

91void\* \_dbus_list_pop_last (DBusList \*\*list);

92DBUS_PRIVATE_EXPORT

93DBusList\* \_dbus_list_pop_first_link (DBusList \*\*list);

94DBUS_PRIVATE_EXPORT

95dbus_bool_t \_dbus_list_copy (DBusList \*\*list,

96 DBusList \*\*dest);

97DBUS_PRIVATE_EXPORT

98int \_dbus_list_get_length (DBusList \*\*list);

99DBUS_PRIVATE_EXPORT

100DBusList\* \_dbus_list_alloc_link (void \*data);

101DBUS_PRIVATE_EXPORT

102void \_dbus_list_free_link (DBusList \*link);

103DBUS_PRIVATE_EXPORT

104void \_dbus_list_unlink (DBusList \*\*list,

105 DBusList \*link);

106DBUS_PRIVATE_EXPORT

107void \_dbus_list_append_link (DBusList \*\*list,

108 DBusList \*link);

109DBUS_PRIVATE_EXPORT

110void \_dbus_list_prepend_link (DBusList \*\*list,

111 DBusList \*link);

112DBUS_PRIVATE_EXPORT

113dbus_bool_t \_dbus_list_length_is_one (DBusList \*\*list);

114

115

116DBUS_PRIVATE_EXPORT

117void \_dbus_list_foreach (DBusList \*\*list,

118 DBusForeachFunction function,

119 void \*data);

120

121\#define \_dbus_list_get_next_link(list, link) ((link)-\>next == \*(list) ? NULL : (link)-\>next)

122\#define \_dbus_list_get_prev_link(list, link) ((link) == \*(list) ? NULL : (link)-\>prev)

123

124/\* if DBUS_ENABLE_STATS \*/

125DBUS_PRIVATE_EXPORT

126void \_dbus_list_get_stats (dbus_uint32_t \*in_use_p,

127 dbus_uint32_t \*in_free_list_p,

128 dbus_uint32_t \*allocated_p);

129

130DBUS_END_DECLS

131

132\#endif /\* DBUS_LIST_H \*/

\_dbus_list_get_first_link

DBUS_PRIVATE_EXPORT DBusList \* \_dbus_list_get_first_link(DBusList \*\*list)

Gets the first link in the list.

**Definition** dbus-list.c:597

\_dbus_list_insert_before_link

DBUS_PRIVATE_EXPORT void \_dbus_list_insert_before_link(DBusList \*\*list, DBusList \*before_this_link, DBusList \*link)

Inserts a link into the list before the given existing link.

**Definition** dbus-list.c:379

\_dbus_list_copy

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_list_copy(DBusList \*\*list, DBusList \*\*dest)

Copies a list.

**Definition** dbus-list.c:727

\_dbus_list_pop_first_link

DBUS_PRIVATE_EXPORT DBusList \* \_dbus_list_pop_first_link(DBusList \*\*list)

Removes the first link in the list and returns it.

**Definition** dbus-list.c:658

\_dbus_list_length_is_one

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_list_length_is_one(DBusList \*\*list)

Check whether length is exactly one.

**Definition** dbus-list.c:813

\_dbus_list_get_last

DBUS_PRIVATE_EXPORT void \* \_dbus_list_get_last(DBusList \*\*list)

Gets the last data in the list.

**Definition** dbus-list.c:626

\_dbus_list_remove

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_list_remove(DBusList \*\*list, void \*data)

Removes a value from the list.

**Definition** dbus-list.c:418

\_dbus_list_append_link

DBUS_PRIVATE_EXPORT void \_dbus_list_append_link(DBusList \*\*list, DBusList \*link)

Appends a link to the list.

**Definition** dbus-list.c:318

\_dbus_list_insert_after_link

DBUS_PRIVATE_EXPORT void \_dbus_list_insert_after_link(DBusList \*\*list, DBusList \*after_this_link, DBusList \*link)

Inserts a link into the list after the given existing link.

**Definition** dbus-list.c:397

\_dbus_list_clear_full

DBUS_PRIVATE_EXPORT void \_dbus_list_clear_full(DBusList \*\*list, DBusFreeFunction function)

Free every link and every element in the list.

**Definition** dbus-list.c:570

\_dbus_list_insert_after

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_list_insert_after(DBusList \*\*list, DBusList \*after_this_link, void \*data)

Inserts data into the list after the given existing link.

**Definition** dbus-list.c:351

\_dbus_list_remove_link

DBUS_PRIVATE_EXPORT void \_dbus_list_remove_link(DBusList \*\*list, DBusList \*link)

Removes a link from the list.

**Definition** dbus-list.c:530

\_dbus_list_get_first

DBUS_PRIVATE_EXPORT void \* \_dbus_list_get_first(DBusList \*\*list)

Gets the first data in the list.

**Definition** dbus-list.c:642

\_dbus_list_get_last_link

DBUS_PRIVATE_EXPORT DBusList \* \_dbus_list_get_last_link(DBusList \*\*list)

Gets the last link in the list.

**Definition** dbus-list.c:610

\_dbus_list_unlink

DBUS_PRIVATE_EXPORT void \_dbus_list_unlink(DBusList \*\*list, DBusList \*link)

Removes the given link from the list, but doesn't free it.

**Definition** dbus-list.c:502

\_dbus_list_find_last

DBUS_PRIVATE_EXPORT DBusList \* \_dbus_list_find_last(DBusList \*\*list, void \*data)

Finds a value in the list.

**Definition** dbus-list.c:475

\_dbus_list_pop_last

DBUS_PRIVATE_EXPORT void \* \_dbus_list_pop_last(DBusList \*\*list)

Removes the last value in the list and returns it.

**Definition** dbus-list.c:702

\_dbus_list_free_link

DBUS_PRIVATE_EXPORT void \_dbus_list_free_link(DBusList \*link)

Frees a linked list node allocated with \_dbus_list_alloc_link.

**Definition** dbus-list.c:257

\_dbus_list_pop_first

DBUS_PRIVATE_EXPORT void \* \_dbus_list_pop_first(DBusList \*\*list)

Removes the first value in the list and returns it.

**Definition** dbus-list.c:679

\_dbus_list_foreach

DBUS_PRIVATE_EXPORT void \_dbus_list_foreach(DBusList \*\*list, DBusForeachFunction function, void \*data)

Calls the given function for each element in the list.

**Definition** dbus-list.c:789

\_dbus_list_get_length

DBUS_PRIVATE_EXPORT int \_dbus_list_get_length(DBusList \*\*list)

Gets the length of a list.

**Definition** dbus-list.c:760

\_dbus_list_clear

DBUS_PRIVATE_EXPORT void \_dbus_list_clear(DBusList \*\*list)

Frees all links in the list and sets the list head to NULL.

**Definition** dbus-list.c:545

\_dbus_list_prepend_link

DBUS_PRIVATE_EXPORT void \_dbus_list_prepend_link(DBusList \*\*list, DBusList \*link)

Prepends a link to the list.

**Definition** dbus-list.c:336

\_dbus_list_prepend

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_list_prepend(DBusList \*\*list, void \*data)

Prepends a value to the list.

**Definition** dbus-list.c:295

\_dbus_list_alloc_link

DBUS_PRIVATE_EXPORT DBusList \* \_dbus_list_alloc_link(void \*data)

Allocates a linked list node.

**Definition** dbus-list.c:245

\_dbus_list_remove_last

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_list_remove_last(DBusList \*\*list, void \*data)

Removes a value from the list.

**Definition** dbus-list.c:449

\_dbus_list_append

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_list_append(DBusList \*\*list, void \*data)

Appends a value to the list.

**Definition** dbus-list.c:273

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

DBusList

A node in a linked list.

**Definition** dbus-list.h:37

DBusList::data

void \* data

Data stored at this element.

**Definition** dbus-list.h:40

DBusList::next

DBusList \* next

Next list node.

**Definition** dbus-list.h:39

DBusList::prev

DBusList \* prev

Previous list node.

**Definition** dbus-list.h:38
