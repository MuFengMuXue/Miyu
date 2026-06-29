ReplacementBlock Struct Reference

D-Bus secret internal implementation details » marshaling and unmarshaling

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a562018cd2a0870abe3897b289bdd8488" class="memitem:a562018cd2a0870abe3897b289bdd8488">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusString </td>
<td class="memItemRight" data-valign="bottom">replacement</td>
</tr>
<tr class="memdesc:a562018cd2a0870abe3897b289bdd8488">
<td class="mdescLeft"> </td>
<td class="mdescRight">Marshaled value including alignment padding.<br />
</td>
</tr>
<tr class="separator:a562018cd2a0870abe3897b289bdd8488">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a2aa3220ac139545f4fa2ddec2c36d5de" class="memitem:a2aa3220ac139545f4fa2ddec2c36d5de">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">padding</td>
</tr>
<tr class="memdesc:a2aa3220ac139545f4fa2ddec2c36d5de">
<td class="mdescLeft"> </td>
<td class="mdescRight">How much of the replacement block is padding.<br />
</td>
</tr>
<tr class="separator:a2aa3220ac139545f4fa2ddec2c36d5de">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Definition at line 1134 of file dbus-marshal-recursive.c.

## Field Documentation

## ◆ padding

|                               |
|-------------------------------|
| int ReplacementBlock::padding |

How much of the replacement block is padding.

Definition at line 1137 of file dbus-marshal-recursive.c.

## ◆ replacement

|                                          |
|------------------------------------------|
| DBusString ReplacementBlock::replacement |

Marshaled value including alignment padding.

Definition at line 1136 of file dbus-marshal-recursive.c.

The documentation for this struct was generated from the following file:

- dbus-marshal-recursive.c
