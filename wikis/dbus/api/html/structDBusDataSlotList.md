DBusDataSlotList Struct Reference

Data structure that stores the actual user data set at a given slot. More...

`#include <``dbus-dataslot.h``>`

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a4dd0fc6cc10b9c48dd53f34335abd08e" class="memitem:a4dd0fc6cc10b9c48dd53f34335abd08e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusDataSlot * </td>
<td class="memItemRight" data-valign="bottom">slots</td>
</tr>
<tr class="memdesc:a4dd0fc6cc10b9c48dd53f34335abd08e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Data slots.<br />
</td>
</tr>
<tr class="separator:a4dd0fc6cc10b9c48dd53f34335abd08e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a2d6cb7670a940bc886c99cb892b44502" class="memitem:a2d6cb7670a940bc886c99cb892b44502">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">n_slots</td>
</tr>
<tr class="memdesc:a2d6cb7670a940bc886c99cb892b44502">
<td class="mdescLeft"> </td>
<td class="mdescRight">Slots we have storage for in data_slots.<br />
</td>
</tr>
<tr class="separator:a2d6cb7670a940bc886c99cb892b44502">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Data structure that stores the actual user data set at a given slot.

Definition at line 71 of file dbus-dataslot.h.

## Field Documentation

## ◆ n_slots

|                               |
|-------------------------------|
| int DBusDataSlotList::n_slots |

Slots we have storage for in data_slots.

Definition at line 74 of file dbus-dataslot.h.

Referenced by \_dbus_data_slot_list_free(), \_dbus_data_slot_list_get(), \_dbus_data_slot_list_init(), and \_dbus_data_slot_list_set().

## ◆ slots

|                                        |
|----------------------------------------|
| DBusDataSlot\* DBusDataSlotList::slots |

Data slots.

Definition at line 73 of file dbus-dataslot.h.

Referenced by \_dbus_data_slot_list_clear(), \_dbus_data_slot_list_free(), \_dbus_data_slot_list_get(), \_dbus_data_slot_list_init(), and \_dbus_data_slot_list_set().

The documentation for this struct was generated from the following file:

- dbus-dataslot.h
