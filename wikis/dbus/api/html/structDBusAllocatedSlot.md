DBusAllocatedSlot Struct Reference

An allocated slot for storing data. More...

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
<tr id="r_a849e5f8d951d159c45172ce825fb3a1e" class="memitem:a849e5f8d951d159c45172ce825fb3a1e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_int32_t </td>
<td class="memItemRight" data-valign="bottom">slot_id</td>
</tr>
<tr class="memdesc:a849e5f8d951d159c45172ce825fb3a1e">
<td class="mdescLeft"> </td>
<td class="mdescRight">ID of this slot.<br />
</td>
</tr>
<tr class="separator:a849e5f8d951d159c45172ce825fb3a1e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a554eaffc3334a90a86f618eaa713410c" class="memitem:a554eaffc3334a90a86f618eaa713410c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">refcount</td>
</tr>
<tr class="memdesc:a554eaffc3334a90a86f618eaa713410c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Number of uses of the slot.<br />
</td>
</tr>
<tr class="separator:a554eaffc3334a90a86f618eaa713410c">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

An allocated slot for storing data.

Definition at line 48 of file dbus-dataslot.h.

## Field Documentation

## ◆ refcount

|                                 |
|---------------------------------|
| int DBusAllocatedSlot::refcount |

Number of uses of the slot.

Definition at line 51 of file dbus-dataslot.h.

Referenced by \_dbus_data_slot_allocator_alloc(), and \_dbus_data_slot_allocator_free().

## ◆ slot_id

|                                         |
|-----------------------------------------|
| dbus_int32_t DBusAllocatedSlot::slot_id |

ID of this slot.

Definition at line 50 of file dbus-dataslot.h.

Referenced by \_dbus_data_slot_allocator_alloc(), \_dbus_data_slot_allocator_free(), \_dbus_data_slot_list_get(), and \_dbus_data_slot_list_set().

The documentation for this struct was generated from the following file:

- dbus-dataslot.h
