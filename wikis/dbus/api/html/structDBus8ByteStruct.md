DBus8ByteStruct Struct Reference

D-Bus low-level public API » Basic types

An 8-byte struct you could use to access int64 without having int64 support. More...

`#include <``dbus-types.h``>`

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_af61431a112f5e81964c0870c5428bb45" class="memitem:af61431a112f5e81964c0870c5428bb45">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">first32</td>
</tr>
<tr class="memdesc:af61431a112f5e81964c0870c5428bb45">
<td class="mdescLeft"> </td>
<td class="mdescRight">first 32 bits in the 8 bytes (beware endian issues)<br />
</td>
</tr>
<tr class="separator:af61431a112f5e81964c0870c5428bb45">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a9e4350ba5ff3dae28710f2cb0dcc0c06" class="memitem:a9e4350ba5ff3dae28710f2cb0dcc0c06">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">second32</td>
</tr>
<tr class="memdesc:a9e4350ba5ff3dae28710f2cb0dcc0c06">
<td class="mdescLeft"> </td>
<td class="mdescRight">second 32 bits in the 8 bytes (beware endian issues)<br />
</td>
</tr>
<tr class="separator:a9e4350ba5ff3dae28710f2cb0dcc0c06">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

An 8-byte struct you could use to access int64 without having int64 support.

Use dbus_int64_t or dbus_uint64_t instead.

Definition at line 144 of file dbus-types.h.

## Field Documentation

## ◆ first32

|                                        |
|----------------------------------------|
| dbus_uint32_t DBus8ByteStruct::first32 |

first 32 bits in the 8 bytes (beware endian issues)

Definition at line 146 of file dbus-types.h.

## ◆ second32

|                                         |
|-----------------------------------------|
| dbus_uint32_t DBus8ByteStruct::second32 |

second 32 bits in the 8 bytes (beware endian issues)

Definition at line 147 of file dbus-types.h.

The documentation for this struct was generated from the following file:

- dbus-types.h
