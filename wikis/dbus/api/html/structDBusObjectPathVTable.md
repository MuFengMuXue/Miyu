DBusObjectPathVTable Struct Reference

D-Bus low-level public API » DBusConnection

Virtual table that must be implemented to handle a portion of the object path hierarchy. More...

`#include <``dbus-connection.h``>`

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_abb6c084f345051b9649615b91ec654d4" class="memitem:abb6c084f345051b9649615b91ec654d4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusObjectPathUnregisterFunction </td>
<td class="memItemRight" data-valign="bottom">unregister_function</td>
</tr>
<tr class="memdesc:abb6c084f345051b9649615b91ec654d4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to unregister this handler.<br />
</td>
</tr>
<tr class="separator:abb6c084f345051b9649615b91ec654d4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a83464b6b8b66fb7adebd8e3bf8ff1b70" class="memitem:a83464b6b8b66fb7adebd8e3bf8ff1b70">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusObjectPathMessageFunction </td>
<td class="memItemRight" data-valign="bottom">message_function</td>
</tr>
<tr class="memdesc:a83464b6b8b66fb7adebd8e3bf8ff1b70">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to handle messages.<br />
</td>
</tr>
<tr class="separator:a83464b6b8b66fb7adebd8e3bf8ff1b70">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a128f315f08f1cf862c8c7b0ee34015ec" class="memitem:a128f315f08f1cf862c8c7b0ee34015ec">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void(* </td>
<td class="memItemRight" data-valign="bottom">dbus_internal_pad1 )(void *)</td>
</tr>
<tr class="memdesc:a128f315f08f1cf862c8c7b0ee34015ec">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reserved for future expansion.<br />
</td>
</tr>
<tr class="separator:a128f315f08f1cf862c8c7b0ee34015ec">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a284c58e29009e2a47204937e1394047f" class="memitem:a284c58e29009e2a47204937e1394047f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void(* </td>
<td class="memItemRight" data-valign="bottom">dbus_internal_pad2 )(void *)</td>
</tr>
<tr class="memdesc:a284c58e29009e2a47204937e1394047f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reserved for future expansion.<br />
</td>
</tr>
<tr class="separator:a284c58e29009e2a47204937e1394047f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a73e608ee20849dc5b8a68926d171c3dd" class="memitem:a73e608ee20849dc5b8a68926d171c3dd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void(* </td>
<td class="memItemRight" data-valign="bottom">dbus_internal_pad3 )(void *)</td>
</tr>
<tr class="memdesc:a73e608ee20849dc5b8a68926d171c3dd">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reserved for future expansion.<br />
</td>
</tr>
<tr class="separator:a73e608ee20849dc5b8a68926d171c3dd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ada2da205919b2a6a4d42b8a3366c4de9" class="memitem:ada2da205919b2a6a4d42b8a3366c4de9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void(* </td>
<td class="memItemRight" data-valign="bottom">dbus_internal_pad4 )(void *)</td>
</tr>
<tr class="memdesc:ada2da205919b2a6a4d42b8a3366c4de9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reserved for future expansion.<br />
</td>
</tr>
<tr class="separator:ada2da205919b2a6a4d42b8a3366c4de9">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Virtual table that must be implemented to handle a portion of the object path hierarchy.

Attach the vtable to a particular path using dbus_connection_register_object_path() or dbus_connection_register_fallback().

Definition at line 390 of file dbus-connection.h.

## Field Documentation

## ◆ dbus_internal_pad1

|                                                             |
|-------------------------------------------------------------|
| void(\* DBusObjectPathVTable::dbus_internal_pad1) (void \*) |

Reserved for future expansion.

Definition at line 395 of file dbus-connection.h.

## ◆ dbus_internal_pad2

|                                                             |
|-------------------------------------------------------------|
| void(\* DBusObjectPathVTable::dbus_internal_pad2) (void \*) |

Reserved for future expansion.

Definition at line 396 of file dbus-connection.h.

## ◆ dbus_internal_pad3

|                                                             |
|-------------------------------------------------------------|
| void(\* DBusObjectPathVTable::dbus_internal_pad3) (void \*) |

Reserved for future expansion.

Definition at line 397 of file dbus-connection.h.

## ◆ dbus_internal_pad4

|                                                             |
|-------------------------------------------------------------|
| void(\* DBusObjectPathVTable::dbus_internal_pad4) (void \*) |

Reserved for future expansion.

Definition at line 398 of file dbus-connection.h.

## ◆ message_function

|                                                                      |
|----------------------------------------------------------------------|
| DBusObjectPathMessageFunction DBusObjectPathVTable::message_function |

Function to handle messages.

Definition at line 393 of file dbus-connection.h.

Referenced by \_dbus_object_tree_register().

## ◆ unregister_function

|  |
|----|
| DBusObjectPathUnregisterFunction DBusObjectPathVTable::unregister_function |

Function to unregister this handler.

Definition at line 392 of file dbus-connection.h.

Referenced by \_dbus_object_tree_register().

The documentation for this struct was generated from the following file:

- dbus-connection.h
