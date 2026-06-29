DBusDataSlot Struct Reference

DBusDataSlot is used to store application data on the connection. More...

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
<tr id="r_a883c8c8946f13b6f5f3cf99f230159fd" class="memitem:a883c8c8946f13b6f5f3cf99f230159fd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">data</td>
</tr>
<tr class="memdesc:a883c8c8946f13b6f5f3cf99f230159fd">
<td class="mdescLeft"> </td>
<td class="mdescRight">The application data.<br />
</td>
</tr>
<tr class="separator:a883c8c8946f13b6f5f3cf99f230159fd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ab899f58869942556fb1b381ca3f3e2b2" class="memitem:ab899f58869942556fb1b381ca3f3e2b2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusFreeFunction </td>
<td class="memItemRight" data-valign="bottom">free_data_func</td>
</tr>
<tr class="memdesc:ab899f58869942556fb1b381ca3f3e2b2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Free the application data.<br />
</td>
</tr>
<tr class="separator:ab899f58869942556fb1b381ca3f3e2b2">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

DBusDataSlot is used to store application data on the connection.

Definition at line 38 of file dbus-dataslot.h.

## Field Documentation

## ◆ data

|                           |
|---------------------------|
| void\* DBusDataSlot::data |

The application data.

Definition at line 40 of file dbus-dataslot.h.

Referenced by \_dbus_data_slot_list_clear(), \_dbus_data_slot_list_get(), and \_dbus_data_slot_list_set().

## ◆ free_data_func

|                                               |
|-----------------------------------------------|
| DBusFreeFunction DBusDataSlot::free_data_func |

Free the application data.

Definition at line 41 of file dbus-dataslot.h.

Referenced by \_dbus_data_slot_list_clear(), and \_dbus_data_slot_list_set().

The documentation for this struct was generated from the following file:

- dbus-dataslot.h
