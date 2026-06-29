DBusObjectSubtree Struct Reference

D-Bus secret internal implementation details » A hierarchy of objects with container-contained relationship

Struct representing a single registered subtree handler, or node that's a parent of a registered subtree handler. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a45c6566f866ca45d48817f64f7f08fa6" class="memitem:a45c6566f866ca45d48817f64f7f08fa6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusAtomic </td>
<td class="memItemRight" data-valign="bottom">refcount</td>
</tr>
<tr class="memdesc:a45c6566f866ca45d48817f64f7f08fa6">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reference count.<br />
</td>
</tr>
<tr class="separator:a45c6566f866ca45d48817f64f7f08fa6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a352044a5ca8e29df149b248b0d988d96" class="memitem:a352044a5ca8e29df149b248b0d988d96">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusObjectSubtree * </td>
<td class="memItemRight" data-valign="bottom">parent</td>
</tr>
<tr class="memdesc:a352044a5ca8e29df149b248b0d988d96">
<td class="mdescLeft"> </td>
<td class="mdescRight">Parent node.<br />
</td>
</tr>
<tr class="separator:a352044a5ca8e29df149b248b0d988d96">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a7038595dfd005eeb9a9e2dad07cdc9c6" class="memitem:a7038595dfd005eeb9a9e2dad07cdc9c6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusObjectPathUnregisterFunction </td>
<td class="memItemRight" data-valign="bottom">unregister_function</td>
</tr>
<tr class="memdesc:a7038595dfd005eeb9a9e2dad07cdc9c6">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to call on unregister.<br />
</td>
</tr>
<tr class="separator:a7038595dfd005eeb9a9e2dad07cdc9c6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a6be63f07c500936dde058024ccbd30d4" class="memitem:a6be63f07c500936dde058024ccbd30d4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusObjectPathMessageFunction </td>
<td class="memItemRight" data-valign="bottom">message_function</td>
</tr>
<tr class="memdesc:a6be63f07c500936dde058024ccbd30d4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to handle messages.<br />
</td>
</tr>
<tr class="separator:a6be63f07c500936dde058024ccbd30d4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ac879ddd02ff982b7ba6d014562b85807" class="memitem:ac879ddd02ff982b7ba6d014562b85807">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">user_data</td>
</tr>
<tr class="memdesc:ac879ddd02ff982b7ba6d014562b85807">
<td class="mdescLeft"> </td>
<td class="mdescRight">Data for functions.<br />
</td>
</tr>
<tr class="separator:ac879ddd02ff982b7ba6d014562b85807">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ade77f6089c08d212eda0b4223ab66915" class="memitem:ade77f6089c08d212eda0b4223ab66915">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusObjectSubtree ** </td>
<td class="memItemRight" data-valign="bottom">subtrees</td>
</tr>
<tr class="memdesc:ade77f6089c08d212eda0b4223ab66915">
<td class="mdescLeft"> </td>
<td class="mdescRight">Child nodes.<br />
</td>
</tr>
<tr class="separator:ade77f6089c08d212eda0b4223ab66915">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a9972c279dd920fc5b69fc63886c880ed" class="memitem:a9972c279dd920fc5b69fc63886c880ed">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">n_subtrees</td>
</tr>
<tr class="memdesc:a9972c279dd920fc5b69fc63886c880ed">
<td class="mdescLeft"> </td>
<td class="mdescRight">Number of child nodes.<br />
</td>
</tr>
<tr class="separator:a9972c279dd920fc5b69fc63886c880ed">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ac5be3a80fa3547cea2ac7535865123c7" class="memitem:ac5be3a80fa3547cea2ac7535865123c7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">max_subtrees</td>
</tr>
<tr class="memdesc:ac5be3a80fa3547cea2ac7535865123c7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Number of allocated entries in subtrees.<br />
</td>
</tr>
<tr class="separator:ac5be3a80fa3547cea2ac7535865123c7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ab29370bdbfa87f8e6f718a3f4a20b652" class="memitem:ab29370bdbfa87f8e6f718a3f4a20b652">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">invoke_as_fallback: 1</td>
</tr>
<tr class="memdesc:ab29370bdbfa87f8e6f718a3f4a20b652">
<td class="mdescLeft"> </td>
<td class="mdescRight">Whether to invoke message_function when child nodes don't handle the message.<br />
</td>
</tr>
<tr class="separator:ab29370bdbfa87f8e6f718a3f4a20b652">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_add05785d7c8572e28254c47d50a3c914" class="memitem:add05785d7c8572e28254c47d50a3c914">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char </td>
<td class="memItemRight" data-valign="bottom">name [1]</td>
</tr>
<tr class="memdesc:add05785d7c8572e28254c47d50a3c914">
<td class="mdescLeft"> </td>
<td class="mdescRight">Allocated as large as necessary.<br />
</td>
</tr>
<tr class="separator:add05785d7c8572e28254c47d50a3c914">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Struct representing a single registered subtree handler, or node that's a parent of a registered subtree handler.

If message_function != NULL there's actually a handler at this node.

Definition at line 73 of file dbus-object-tree.c.

## Field Documentation

## ◆ invoke_as_fallback

|                                                    |
|----------------------------------------------------|
| unsigned int DBusObjectSubtree::invoke_as_fallback |

Whether to invoke message_function when child nodes don't handle the message.

Definition at line 83 of file dbus-object-tree.c.

Referenced by \_dbus_object_tree_dispatch_and_unlock(), \_dbus_object_tree_new(), and \_dbus_object_tree_register().

## ◆ max_subtrees

|                                     |
|-------------------------------------|
| int DBusObjectSubtree::max_subtrees |

Number of allocated entries in subtrees.

Definition at line 82 of file dbus-object-tree.c.

## ◆ message_function

|                                                                   |
|-------------------------------------------------------------------|
| DBusObjectPathMessageFunction DBusObjectSubtree::message_function |

Function to handle messages.

Definition at line 78 of file dbus-object-tree.c.

Referenced by \_dbus_object_tree_dispatch_and_unlock(), and \_dbus_object_tree_register().

## ◆ n_subtrees

|                                   |
|-----------------------------------|
| int DBusObjectSubtree::n_subtrees |

Number of child nodes.

Definition at line 81 of file dbus-object-tree.c.

## ◆ name

|                                   |
|-----------------------------------|
| char DBusObjectSubtree::name\[1\] |

Allocated as large as necessary.

Definition at line 84 of file dbus-object-tree.c.

## ◆ parent

|                                               |
|-----------------------------------------------|
| DBusObjectSubtree\* DBusObjectSubtree::parent |

Parent node.

Definition at line 76 of file dbus-object-tree.c.

Referenced by \_dbus_object_tree_dispatch_and_unlock().

## ◆ refcount

|                                        |
|----------------------------------------|
| DBusAtomic DBusObjectSubtree::refcount |

Reference count.

Definition at line 75 of file dbus-object-tree.c.

## ◆ subtrees

|                                                   |
|---------------------------------------------------|
| DBusObjectSubtree\*\* DBusObjectSubtree::subtrees |

Child nodes.

Definition at line 80 of file dbus-object-tree.c.

## ◆ unregister_function

|                                                                         |
|-------------------------------------------------------------------------|
| DBusObjectPathUnregisterFunction DBusObjectSubtree::unregister_function |

Function to call on unregister.

Definition at line 77 of file dbus-object-tree.c.

Referenced by \_dbus_object_tree_register().

## ◆ user_data

|                                     |
|-------------------------------------|
| void\* DBusObjectSubtree::user_data |

Data for functions.

Definition at line 79 of file dbus-object-tree.c.

Referenced by \_dbus_object_tree_dispatch_and_unlock(), \_dbus_object_tree_get_user_data_unlocked(), and \_dbus_object_tree_register().

The documentation for this struct was generated from the following file:

- dbus-object-tree.c
