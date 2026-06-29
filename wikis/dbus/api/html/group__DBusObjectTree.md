A hierarchy of objects with container-contained relationship

D-Bus secret internal implementation details

DBusObjectTree is used by DBusConnection to track the object tree. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-structures" class="groupheader"> Data Structures</h2></td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusObjectTree</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Internals of DBusObjectTree. More...<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusObjectSubtree</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Struct representing a single registered subtree handler, or node that's a parent of a registered subtree handler. More...<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="macros" class="groupheader"> Macros</h2></td>
</tr>
<tr id="r_ga7c65e59e0445cd294f82a4fb42e44772" class="memitem:ga7c65e59e0445cd294f82a4fb42e44772">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">VERBOSE_FIND   0</td>
</tr>
<tr class="memdesc:ga7c65e59e0445cd294f82a4fb42e44772">
<td class="mdescLeft"> </td>
<td class="mdescRight">Set to 1 to get a bunch of debug spew about finding the subtree nodes.<br />
</td>
</tr>
<tr class="separator:ga7c65e59e0445cd294f82a4fb42e44772">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9def2cd95c325a4ad26222cddbfed5d5" class="memitem:ga9def2cd95c325a4ad26222cddbfed5d5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">VERBOSE_DECOMPOSE   0</td>
</tr>
<tr class="memdesc:ga9def2cd95c325a4ad26222cddbfed5d5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Set to 1 to get a bunch of spew about disassembling the path string.<br />
</td>
</tr>
<tr class="separator:ga9def2cd95c325a4ad26222cddbfed5d5">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="typedefs" class="groupheader"> Typedefs</h2></td>
</tr>
<tr id="r_ga797595db73034eabb225d933f859fc48" class="memitem:ga797595db73034eabb225d933f859fc48">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusObjectSubtree </td>
<td class="memItemRight" data-valign="bottom">DBusObjectSubtree</td>
</tr>
<tr class="memdesc:ga797595db73034eabb225d933f859fc48">
<td class="mdescLeft"> </td>
<td class="mdescRight">Subnode of the object hierarchy.<br />
</td>
</tr>
<tr class="separator:ga797595db73034eabb225d933f859fc48">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="functions" class="groupheader"> Functions</h2></td>
</tr>
<tr id="r_gaf75bada384a7469b8a1536557e2ac0aa" class="memitem:gaf75bada384a7469b8a1536557e2ac0aa">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusObjectTree * </td>
<td class="memItemRight" data-valign="bottom">_dbus_object_tree_new (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:gaf75bada384a7469b8a1536557e2ac0aa">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new object tree, representing a mapping from paths to handler vtables.<br />
</td>
</tr>
<tr class="separator:gaf75bada384a7469b8a1536557e2ac0aa">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf551b741b702d048b0d309648679e60a" class="memitem:gaf551b741b702d048b0d309648679e60a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusObjectTree * </td>
<td class="memItemRight" data-valign="bottom">_dbus_object_tree_ref (DBusObjectTree *tree)</td>
</tr>
<tr class="memdesc:gaf551b741b702d048b0d309648679e60a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Increment the reference count.<br />
</td>
</tr>
<tr class="separator:gaf551b741b702d048b0d309648679e60a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7639e273ab160c422a7cef0cda60ded5" class="memitem:ga7639e273ab160c422a7cef0cda60ded5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_object_tree_unref (DBusObjectTree *tree)</td>
</tr>
<tr class="memdesc:ga7639e273ab160c422a7cef0cda60ded5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Decrement the reference count.<br />
</td>
</tr>
<tr class="separator:ga7639e273ab160c422a7cef0cda60ded5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab3da15ee1a73d3b26008d1bce20a78a0" class="memitem:gab3da15ee1a73d3b26008d1bce20a78a0">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_object_tree_register (DBusObjectTree *tree, dbus_bool_t fallback, const char **path, const DBusObjectPathVTable *vtable, void *user_data, DBusError *error)</td>
</tr>
<tr class="memdesc:gab3da15ee1a73d3b26008d1bce20a78a0">
<td class="mdescLeft"> </td>
<td class="mdescRight">Registers a new subtree in the global object tree.<br />
</td>
</tr>
<tr class="separator:gab3da15ee1a73d3b26008d1bce20a78a0">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3babe73ed342b6963997ef2efd73ef75" class="memitem:ga3babe73ed342b6963997ef2efd73ef75">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_object_tree_unregister_and_unlock (DBusObjectTree *tree, const char **path)</td>
</tr>
<tr class="memdesc:ga3babe73ed342b6963997ef2efd73ef75">
<td class="mdescLeft"> </td>
<td class="mdescRight">Unregisters an object subtree that was registered with the same path.<br />
</td>
</tr>
<tr class="separator:ga3babe73ed342b6963997ef2efd73ef75">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1c51e43233ce0f3855c128f2555317eb" class="memitem:ga1c51e43233ce0f3855c128f2555317eb">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_object_tree_free_all_unlocked (DBusObjectTree *tree)</td>
</tr>
<tr class="memdesc:ga1c51e43233ce0f3855c128f2555317eb">
<td class="mdescLeft"> </td>
<td class="mdescRight">Free all the handlers in the tree.<br />
</td>
</tr>
<tr class="separator:ga1c51e43233ce0f3855c128f2555317eb">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad660d78a12fa207d891838863dfc6ba7" class="memitem:gad660d78a12fa207d891838863dfc6ba7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusHandlerResult </td>
<td class="memItemRight" data-valign="bottom">_dbus_object_tree_dispatch_and_unlock (DBusObjectTree *tree, DBusMessage *message, dbus_bool_t *found_object)</td>
</tr>
<tr class="memdesc:gad660d78a12fa207d891838863dfc6ba7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Tries to dispatch a message by directing it to handler for the object path listed in the message header, if any.<br />
</td>
</tr>
<tr class="separator:gad660d78a12fa207d891838863dfc6ba7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac7bbb5c8b1086b1de750cd1b12c0f9dc" class="memitem:gac7bbb5c8b1086b1de750cd1b12c0f9dc">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">_dbus_object_tree_get_user_data_unlocked (DBusObjectTree *tree, const char **path)</td>
</tr>
<tr class="memdesc:gac7bbb5c8b1086b1de750cd1b12c0f9dc">
<td class="mdescLeft"> </td>
<td class="mdescRight">Looks up the data passed to _dbus_object_tree_register() for a handler at the given path.<br />
</td>
</tr>
<tr class="separator:gac7bbb5c8b1086b1de750cd1b12c0f9dc">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaab7040bd1bf037d99e9bbb75d0869a2f" class="memitem:gaab7040bd1bf037d99e9bbb75d0869a2f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_object_tree_list_registered_and_unlock (DBusObjectTree *tree, const char **parent_path, char ***child_entries)</td>
</tr>
<tr class="memdesc:gaab7040bd1bf037d99e9bbb75d0869a2f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Lists the registered fallback handlers and object path handlers at the given parent_path.<br />
</td>
</tr>
<tr class="separator:gaab7040bd1bf037d99e9bbb75d0869a2f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab282b916368cd512842d3aaae31e65c7" class="memitem:gab282b916368cd512842d3aaae31e65c7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_decompose_path (const char *data, int len, char ***path, int *path_len)</td>
</tr>
<tr class="memdesc:gab282b916368cd512842d3aaae31e65c7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Decompose an object path.<br />
</td>
</tr>
<tr class="separator:gab282b916368cd512842d3aaae31e65c7">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

DBusObjectTree is used by DBusConnection to track the object tree.

Types and functions related to DBusObjectTree. These are all library-internal.

## Macro Definition Documentation

## ◆ VERBOSE_DECOMPOSE

|                                |
|--------------------------------|
| \#define VERBOSE_DECOMPOSE   0 |

Set to 1 to get a bunch of spew about disassembling the path string.

Definition at line 1234 of file dbus-object-tree.c.

## ◆ VERBOSE_FIND

|                           |
|---------------------------|
| \#define VERBOSE_FIND   0 |

Set to 1 to get a bunch of debug spew about finding the subtree nodes.

Definition at line 163 of file dbus-object-tree.c.

## Typedef Documentation

## ◆ DBusObjectSubtree

|                                                    |
|----------------------------------------------------|
| typedef struct DBusObjectSubtree DBusObjectSubtree |

Subnode of the object hierarchy.

Definition at line 49 of file dbus-object-tree.c.

## Function Documentation

## ◆ \_dbus_decompose_path()

|                                   |     |                |             |
|-----------------------------------|-----|----------------|-------------|
| dbus_bool_t \_dbus_decompose_path | (   | const char \*  | *data*,     |
|                                   |     | int            | *len*,      |
|                                   |     | char \*\*\*    | *path*,     |
|                                   |     | int \*         | *path_len*  |
|                                   | )   |                |             |

Decompose an object path.

A path of just "/" is represented as an empty vector of strings. The path need not be nul terminated.

Parameters  
|          |                                  |
|----------|----------------------------------|
| data     | the path data                    |
| len      | the length of the path string    |
| path     | address to store new object path |
| path_len | length of stored path            |

Definition at line 1247 of file dbus-object-tree.c.

References \_dbus_assert, \_dbus_memdup(), dbus_free_string_array(), dbus_new0, FALSE, NULL, and TRUE.

Referenced by dbus_connection_get_object_path_data(), dbus_connection_list_registered(), dbus_connection_unregister_object_path(), and dbus_message_get_path_decomposed().

## ◆ \_dbus_object_tree_dispatch_and_unlock()

|  |  |  |  |
|----|----|----|----|
| DBusHandlerResult \_dbus_object_tree_dispatch_and_unlock | ( | DBusObjectTree \*  | *tree*, |
|  |  | DBusMessage \*  | *message*, |
|  |  | dbus_bool_t \*  | *found_object*  |
|  | ) |  |  |

Tries to dispatch a message by directing it to handler for the object path listed in the message header, if any.

Messages are dispatched first to the registered handler that matches the largest number of path elements; that is, message to /foo/bar/baz would go to the handler for /foo/bar before the one for /foo.

Parameters  
|              |                                |
|--------------|--------------------------------|
| tree         | the global object tree         |
| message      | the message to dispatch        |
| found_object | return location for the object |

<!-- -->

Returns  
whether message was handled successfully

Definition at line 908 of file dbus-object-tree.c.

References \_dbus_connection_lock(), \_dbus_connection_unlock(), \_dbus_list_append(), \_dbus_list_get_first_link(), \_dbus_list_get_length(), \_dbus_list_get_next_link, \_dbus_list_remove_link(), connection, DBusList::data, dbus_free_string_array(), DBUS_HANDLER_RESULT_NEED_MEMORY, DBUS_HANDLER_RESULT_NOT_YET_HANDLED, dbus_message_get_path_decomposed(), FALSE, DBusObjectSubtree::invoke_as_fallback, DBusObjectSubtree::message_function, NULL, DBusObjectSubtree::parent, and DBusObjectSubtree::user_data.

Referenced by dbus_connection_dispatch().

## ◆ \_dbus_object_tree_free_all_unlocked()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| void \_dbus_object_tree_free_all_unlocked | ( | DBusObjectTree \*  | *tree* | ) |  |

Free all the handlers in the tree.

Lock on tree's connection must not be held.

Parameters  
|      |                 |
|------|-----------------|
| tree | the object tree |

Definition at line 723 of file dbus-object-tree.c.

References connection, NULL, and root.

Referenced by \_dbus_object_tree_unref().

## ◆ \_dbus_object_tree_get_user_data_unlocked()

|  |  |  |  |
|----|----|----|----|
| void \* \_dbus_object_tree_get_user_data_unlocked | ( | DBusObjectTree \*  | *tree*, |
|  |  | const char \*\*  | *path*  |
|  | ) |  |  |

Looks up the data passed to \_dbus_object_tree_register() for a handler at the given path.

Parameters  
|      |                                                               |
|------|---------------------------------------------------------------|
| tree | the global object tree                                        |
| path | NULL-terminated array of path elements giving path to subtree |

<!-- -->

Returns  
the object's user_data or NULL if none found

Definition at line 1080 of file dbus-object-tree.c.

References \_dbus_assert, NULL, and DBusObjectSubtree::user_data.

Referenced by dbus_connection_get_object_path_data().

## ◆ \_dbus_object_tree_list_registered_and_unlock()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_object_tree_list_registered_and_unlock | ( | DBusObjectTree \*  | *tree*, |
|  |  | const char \*\*  | *parent_path*, |
|  |  | char \*\*\*  | *child_entries*  |
|  | ) |  |  |

Lists the registered fallback handlers and object path handlers at the given parent_path.

The returned array should be freed with dbus_free_string_array().

Parameters  
|               |                                           |
|---------------|-------------------------------------------|
| tree          | the object tree                           |
| parent_path   | the path to list the child handlers of    |
| child_entries | returns NULL-terminated array of children |

<!-- -->

Returns  
FALSE if no memory to allocate the child entries

Definition at line 1211 of file dbus-object-tree.c.

References \_dbus_connection_unlock(), and connection.

Referenced by dbus_connection_list_registered().

## ◆ \_dbus_object_tree_new()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBusObjectTree \* \_dbus_object_tree_new | ( | DBusConnection \*  | *connection* | ) |  |

Creates a new object tree, representing a mapping from paths to handler vtables.

Parameters  
|            |                                     |
|------------|-------------------------------------|
| connection | the connection this tree belongs to |

<!-- -->

Returns  
the new tree or NULL if no memory

Definition at line 95 of file dbus-object-tree.c.

References connection, dbus_free(), dbus_new0, DBusObjectSubtree::invoke_as_fallback, NULL, refcount, root, and TRUE.

Referenced by \_dbus_connection_new_for_transport().

## ◆ \_dbus_object_tree_ref()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBusObjectTree \* \_dbus_object_tree_ref | ( | DBusObjectTree \*  | *tree* | ) |  |

Increment the reference count.

Parameters  
|      |                 |
|------|-----------------|
| tree | the object tree |

<!-- -->

Returns  
the object tree

Definition at line 132 of file dbus-object-tree.c.

References \_dbus_assert, and refcount.

## ◆ \_dbus_object_tree_register()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_object_tree_register | ( | DBusObjectTree \*  | *tree*, |
|  |  | dbus_bool_t  | *fallback*, |
|  |  | const char \*\*  | *path*, |
|  |  | const DBusObjectPathVTable \*  | *vtable*, |
|  |  | void \*  | *user_data*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Registers a new subtree in the global object tree.

Parameters  
|           |                                                               |
|-----------|---------------------------------------------------------------|
| tree      | the global object tree                                        |
| fallback  | TRUE to handle messages to children of this path              |
| path      | NULL-terminated array of path elements giving path to subtree |
| vtable    | the vtable used to traverse this subtree                      |
| user_data | user data to pass to methods in the vtable                    |
| error     | address where an error can be returned                        |

<!-- -->

Returns  
FALSE if an error (DBUS_ERROR_NO_MEMORY or DBUS_ERROR_OBJECT_PATH_IN_USE) is reported

Definition at line 396 of file dbus-object-tree.c.

References \_dbus_assert, DBUS_ERROR_OBJECT_PATH_IN_USE, dbus_free(), dbus_set_error(), FALSE, DBusObjectSubtree::invoke_as_fallback, DBusObjectPathVTable::message_function, DBusObjectSubtree::message_function, NULL, TRUE, DBusObjectPathVTable::unregister_function, DBusObjectSubtree::unregister_function, and DBusObjectSubtree::user_data.

## ◆ \_dbus_object_tree_unref()

|                               |     |                    |        |     |     |
|-------------------------------|-----|--------------------|--------|-----|-----|
| void \_dbus_object_tree_unref | (   | DBusObjectTree \*  | *tree* | )   |     |

Decrement the reference count.

Parameters  
|      |                 |
|------|-----------------|
| tree | the object tree |

Definition at line 146 of file dbus-object-tree.c.

References \_dbus_assert, \_dbus_object_tree_free_all_unlocked(), dbus_free(), and refcount.

Referenced by \_dbus_connection_new_for_transport().

## ◆ \_dbus_object_tree_unregister_and_unlock()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_object_tree_unregister_and_unlock | ( | DBusObjectTree \*  | *tree*, |
|  |  | const char \*\*  | *path*  |
|  | ) |  |  |

Unregisters an object subtree that was registered with the same path.

Parameters  
|  |  |
|----|----|
| tree | the global object tree |
| path | path to the subtree (same as the one passed to \_dbus_object_tree_register()) |

Definition at line 628 of file dbus-object-tree.c.

References \_dbus_assert, \_dbus_connection_ref_unlocked(), \_dbus_connection_unlock(), \_dbus_warn(), connection, dbus_connection_unref(), FALSE, NULL, root, and TRUE.

Referenced by dbus_connection_unregister_object_path().
