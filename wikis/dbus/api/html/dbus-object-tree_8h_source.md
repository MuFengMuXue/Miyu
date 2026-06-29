dbus-object-tree.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-object-tree.h DBusObjectTree (internals of DBusConnection)

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

25\#ifndef DBUS_OBJECT_TREE_H

26\#define DBUS_OBJECT_TREE_H

27

28\#include \<dbus/dbus-connection.h\>

29

30DBUS_BEGIN_DECLS

31

32typedef struct DBusObjectTree DBusObjectTree;

33

34DBusObjectTree\* \_dbus_object_tree_new (DBusConnection \*connection);

35DBusObjectTree\* \_dbus_object_tree_ref (DBusObjectTree \*tree);

36void \_dbus_object_tree_unref (DBusObjectTree \*tree);

37

38dbus_bool_t \_dbus_object_tree_register (DBusObjectTree \*tree,

39 dbus_bool_t fallback,

40 const char \*\*path,

41 const DBusObjectPathVTable \*vtable,

42 void \*user_data,

43 DBusError \*error);

44void \_dbus_object_tree_unregister_and_unlock (DBusObjectTree \*tree,

45 const char \*\*path);

46DBusHandlerResult \_dbus_object_tree_dispatch_and_unlock (DBusObjectTree \*tree,

47 DBusMessage \*message,

48 dbus_bool_t \*found_object);

49void\* \_dbus_object_tree_get_user_data_unlocked (DBusObjectTree \*tree,

50 const char \*\*path);

51void \_dbus_object_tree_free_all_unlocked (DBusObjectTree \*tree);

52

53

54dbus_bool_t \_dbus_object_tree_list_registered_and_unlock (DBusObjectTree \*tree,

55 const char \*\*parent_path,

56 char \*\*\*child_entries);

57

58dbus_bool_t \_dbus_decompose_path (const char \*data,

59 int len,

60 char \*\*\*path,

61 int \*path_len);

62

63DBUS_END_DECLS

64

65\#endif /\* DBUS_OBJECT_TREE_H \*/

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

\_dbus_object_tree_free_all_unlocked

void \_dbus_object_tree_free_all_unlocked(DBusObjectTree \*tree)

Free all the handlers in the tree.

**Definition** dbus-object-tree.c:723

\_dbus_object_tree_unregister_and_unlock

void \_dbus_object_tree_unregister_and_unlock(DBusObjectTree \*tree, const char \*\*path)

Unregisters an object subtree that was registered with the same path.

**Definition** dbus-object-tree.c:628

\_dbus_object_tree_unref

void \_dbus_object_tree_unref(DBusObjectTree \*tree)

Decrement the reference count.

**Definition** dbus-object-tree.c:146

\_dbus_object_tree_list_registered_and_unlock

dbus_bool_t \_dbus_object_tree_list_registered_and_unlock(DBusObjectTree \*tree, const char \*\*parent_path, char \*\*\*child_entries)

Lists the registered fallback handlers and object path handlers at the given parent_path.

**Definition** dbus-object-tree.c:1211

\_dbus_decompose_path

dbus_bool_t \_dbus_decompose_path(const char \*data, int len, char \*\*\*path, int \*path_len)

Decompose an object path.

**Definition** dbus-object-tree.c:1247

\_dbus_object_tree_register

dbus_bool_t \_dbus_object_tree_register(DBusObjectTree \*tree, dbus_bool_t fallback, const char \*\*path, const DBusObjectPathVTable \*vtable, void \*user_data, DBusError \*error)

Registers a new subtree in the global object tree.

**Definition** dbus-object-tree.c:396

\_dbus_object_tree_get_user_data_unlocked

void \* \_dbus_object_tree_get_user_data_unlocked(DBusObjectTree \*tree, const char \*\*path)

Looks up the data passed to \_dbus_object_tree_register() for a handler at the given path.

**Definition** dbus-object-tree.c:1080

\_dbus_object_tree_dispatch_and_unlock

DBusHandlerResult \_dbus_object_tree_dispatch_and_unlock(DBusObjectTree \*tree, DBusMessage \*message, dbus_bool_t \*found_object)

Tries to dispatch a message by directing it to handler for the object path listed in the message head...

**Definition** dbus-object-tree.c:908

\_dbus_object_tree_ref

DBusObjectTree \* \_dbus_object_tree_ref(DBusObjectTree \*tree)

Increment the reference count.

**Definition** dbus-object-tree.c:132

\_dbus_object_tree_new

DBusObjectTree \* \_dbus_object_tree_new(DBusConnection \*connection)

Creates a new object tree, representing a mapping from paths to handler vtables.

**Definition** dbus-object-tree.c:95

DBusHandlerResult

DBusHandlerResult

Results that a message handler can return.

**Definition** dbus-shared.h:69

DBusConnection

Implementation details of DBusConnection.

**Definition** dbus-connection.c:259

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusMessage

Internals of DBusMessage.

**Definition** dbus-message-private.h:102

DBusObjectPathVTable

Virtual table that must be implemented to handle a portion of the object path hierarchy.

**Definition** dbus-connection.h:391

DBusObjectTree

Internals of DBusObjectTree.

**Definition** dbus-object-tree.c:61

DBusObjectTree::connection

DBusConnection \* connection

Connection this tree belongs to.

**Definition** dbus-object-tree.c:63
