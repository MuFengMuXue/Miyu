DBusHeaderField Struct Reference

Cached information about a header field in the message. More...

`#include <``dbus-marshal-header.h``>`

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_aa9616d127de7488f6d9dc18c4d0c2133" class="memitem:aa9616d127de7488f6d9dc18c4d0c2133">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">value_pos</td>
</tr>
<tr class="memdesc:aa9616d127de7488f6d9dc18c4d0c2133">
<td class="mdescLeft"> </td>
<td class="mdescRight">Position of field value, or -1/-2.<br />
</td>
</tr>
<tr class="separator:aa9616d127de7488f6d9dc18c4d0c2133">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Cached information about a header field in the message.

Definition at line 41 of file dbus-marshal-header.h.

## Field Documentation

## ◆ value_pos

|                                |
|--------------------------------|
| int DBusHeaderField::value_pos |

Position of field value, or -1/-2.

Definition at line 43 of file dbus-marshal-header.h.

Referenced by \_dbus_header_get_field_basic(), \_dbus_header_get_field_raw(), and \_dbus_header_load().

The documentation for this struct was generated from the following file:

- dbus-marshal-header.h
