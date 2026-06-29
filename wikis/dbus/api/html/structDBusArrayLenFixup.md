DBusArrayLenFixup Struct Reference

When modifying an existing block of values, array lengths may need to be adjusted; those adjustments are described by this struct. More...

`#include <``dbus-marshal-recursive.h``>`

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_aad03f6087695c9e9b409817ac34c6e2b" class="memitem:aad03f6087695c9e9b409817ac34c6e2b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">len_pos_in_reader</td>
</tr>
<tr class="memdesc:aad03f6087695c9e9b409817ac34c6e2b">
<td class="mdescLeft"> </td>
<td class="mdescRight">where the length was in the original block<br />
</td>
</tr>
<tr class="separator:aad03f6087695c9e9b409817ac34c6e2b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a97cccea61d89992e6ad3a19bd569dd2f" class="memitem:a97cccea61d89992e6ad3a19bd569dd2f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">new_len</td>
</tr>
<tr class="memdesc:a97cccea61d89992e6ad3a19bd569dd2f">
<td class="mdescLeft"> </td>
<td class="mdescRight">the new value of the length in the written-out block<br />
</td>
</tr>
<tr class="separator:a97cccea61d89992e6ad3a19bd569dd2f">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

When modifying an existing block of values, array lengths may need to be adjusted; those adjustments are described by this struct.

Definition at line 96 of file dbus-marshal-recursive.h.

## Field Documentation

## ◆ len_pos_in_reader

|                                          |
|------------------------------------------|
| int DBusArrayLenFixup::len_pos_in_reader |

where the length was in the original block

Definition at line 98 of file dbus-marshal-recursive.h.

## ◆ new_len

|                                |
|--------------------------------|
| int DBusArrayLenFixup::new_len |

the new value of the length in the written-out block

Definition at line 99 of file dbus-marshal-recursive.h.

The documentation for this struct was generated from the following file:

- dbus-marshal-recursive.h
