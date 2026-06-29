DBusAtomic Struct Reference

D-Bus secret internal implementation details » Internal system-dependent API

An atomic integer safe to increment or decrement from multiple threads. More...

`#include <``dbus-sysdeps.h``>`

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_aef100f17856a635a9d0f3cae7a7f6bf8" class="memitem:aef100f17856a635a9d0f3cae7a7f6bf8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">volatile dbus_int32_t </td>
<td class="memItemRight" data-valign="bottom">value</td>
</tr>
<tr class="memdesc:aef100f17856a635a9d0f3cae7a7f6bf8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Value of the atomic integer.<br />
</td>
</tr>
<tr class="separator:aef100f17856a635a9d0f3cae7a7f6bf8">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

An atomic integer safe to increment or decrement from multiple threads.

Definition at line 339 of file dbus-sysdeps.h.

## Field Documentation

## ◆ value

|                                         |
|-----------------------------------------|
| volatile dbus_int32_t DBusAtomic::value |

Value of the atomic integer.

Definition at line 346 of file dbus-sysdeps.h.

Referenced by \_dbus_atomic_dec(), \_dbus_atomic_get(), \_dbus_atomic_inc(), \_dbus_atomic_set_nonzero(), and \_dbus_atomic_set_zero().

The documentation for this struct was generated from the following file:

- dbus-sysdeps.h
