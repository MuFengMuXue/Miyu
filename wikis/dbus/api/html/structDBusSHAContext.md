DBusSHAContext Struct Reference

Struct storing state of the SHA algorithm. More...

`#include <``dbus-sha.h``>`

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a4fe941dec79829ea0f0695ede84bcad2" class="memitem:a4fe941dec79829ea0f0695ede84bcad2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">digest [5]</td>
</tr>
<tr class="memdesc:a4fe941dec79829ea0f0695ede84bcad2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Message digest.<br />
</td>
</tr>
<tr class="separator:a4fe941dec79829ea0f0695ede84bcad2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ae2b4ae8398c5964afc95ba9917a57d4b" class="memitem:ae2b4ae8398c5964afc95ba9917a57d4b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">count_lo</td>
</tr>
<tr class="memdesc:ae2b4ae8398c5964afc95ba9917a57d4b">
<td class="mdescLeft"> </td>
<td class="mdescRight">64-bit bit count<br />
</td>
</tr>
<tr class="separator:ae2b4ae8398c5964afc95ba9917a57d4b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aeca9b10f90c5c1e0e52a82b801ac4ab5" class="memitem:aeca9b10f90c5c1e0e52a82b801ac4ab5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">count_hi</td>
</tr>
<tr class="memdesc:aeca9b10f90c5c1e0e52a82b801ac4ab5">
<td class="mdescLeft"> </td>
<td class="mdescRight">No clue.<br />
</td>
</tr>
<tr class="separator:aeca9b10f90c5c1e0e52a82b801ac4ab5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ae1e37d926014364a9e5ca569bf4fe798" class="memitem:ae1e37d926014364a9e5ca569bf4fe798">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">data [16]</td>
</tr>
<tr class="memdesc:ae1e37d926014364a9e5ca569bf4fe798">
<td class="mdescLeft"> </td>
<td class="mdescRight">SHA data buffer.<br />
</td>
</tr>
<tr class="separator:ae1e37d926014364a9e5ca569bf4fe798">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Struct storing state of the SHA algorithm.

Definition at line 39 of file dbus-sha.h.

## Field Documentation

## ◆ count_hi

|                                        |
|----------------------------------------|
| dbus_uint32_t DBusSHAContext::count_hi |

No clue.

Definition at line 43 of file dbus-sha.h.

## ◆ count_lo

|                                        |
|----------------------------------------|
| dbus_uint32_t DBusSHAContext::count_lo |

64-bit bit count

Definition at line 42 of file dbus-sha.h.

## ◆ data

|                                          |
|------------------------------------------|
| dbus_uint32_t DBusSHAContext::data\[16\] |

SHA data buffer.

Definition at line 44 of file dbus-sha.h.

## ◆ digest

|                                           |
|-------------------------------------------|
| dbus_uint32_t DBusSHAContext::digest\[5\] |

Message digest.

Definition at line 41 of file dbus-sha.h.

The documentation for this struct was generated from the following file:

- dbus-sha.h
