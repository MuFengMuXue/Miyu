DBusObjectTree Struct Reference

D-Bus secret internal implementation details » A hierarchy of objects with container-contained relationship

Internals of DBusObjectTree. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a7d7a4cd85c747b162723a121029d9580" class="memitem:a7d7a4cd85c747b162723a121029d9580">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">refcount</td>
</tr>
<tr class="memdesc:a7d7a4cd85c747b162723a121029d9580">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reference count.<br />
</td>
</tr>
<tr class="separator:a7d7a4cd85c747b162723a121029d9580">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a65b58bdaad2e5d09d8366d286e46b100" class="memitem:a65b58bdaad2e5d09d8366d286e46b100">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusConnection * </td>
<td class="memItemRight" data-valign="bottom">connection</td>
</tr>
<tr class="memdesc:a65b58bdaad2e5d09d8366d286e46b100">
<td class="mdescLeft"> </td>
<td class="mdescRight">Connection this tree belongs to.<br />
</td>
</tr>
<tr class="separator:a65b58bdaad2e5d09d8366d286e46b100">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a8d8b8d9801bb51c1f178074881249c26" class="memitem:a8d8b8d9801bb51c1f178074881249c26">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusObjectSubtree * </td>
<td class="memItemRight" data-valign="bottom">root</td>
</tr>
<tr class="memdesc:a8d8b8d9801bb51c1f178074881249c26">
<td class="mdescLeft"> </td>
<td class="mdescRight">Root of the tree ("/" node)<br />
</td>
</tr>
<tr class="separator:a8d8b8d9801bb51c1f178074881249c26">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Internals of DBusObjectTree.

Definition at line 60 of file dbus-object-tree.c.

## Field Documentation

## ◆ connection

|                                             |
|---------------------------------------------|
| DBusConnection\* DBusObjectTree::connection |

Connection this tree belongs to.

Definition at line 63 of file dbus-object-tree.c.

Referenced by \_dbus_object_tree_dispatch_and_unlock(), \_dbus_object_tree_free_all_unlocked(), \_dbus_object_tree_list_registered_and_unlock(), \_dbus_object_tree_new(), and \_dbus_object_tree_unregister_and_unlock().

## ◆ refcount

|                              |
|------------------------------|
| int DBusObjectTree::refcount |

Reference count.

Definition at line 62 of file dbus-object-tree.c.

Referenced by \_dbus_object_tree_new(), \_dbus_object_tree_ref(), and \_dbus_object_tree_unref().

## ◆ root

|                                          |
|------------------------------------------|
| DBusObjectSubtree\* DBusObjectTree::root |

Root of the tree ("/" node)

Definition at line 65 of file dbus-object-tree.c.

Referenced by \_dbus_object_tree_free_all_unlocked(), \_dbus_object_tree_new(), and \_dbus_object_tree_unregister_and_unlock().

The documentation for this struct was generated from the following file:

- dbus-object-tree.c
