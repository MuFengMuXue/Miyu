DBusGUID Union Reference

A globally unique ID ; we have one for each DBusServer, and also one for each machine with libdbus installed on it. More...

`#include <``dbus-internals.h``>`

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a3db114d87644fab561564504a8653e72" class="memitem:a3db114d87644fab561564504a8653e72">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">as_uint32s [DBUS_UUID_LENGTH_WORDS]</td>
</tr>
<tr class="memdesc:a3db114d87644fab561564504a8653e72">
<td class="mdescLeft"> </td>
<td class="mdescRight">guid as four uint32 values<br />
</td>
</tr>
<tr class="separator:a3db114d87644fab561564504a8653e72">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_af45818fb0ae65fdece11aba936af7f09" class="memitem:af45818fb0ae65fdece11aba936af7f09">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char </td>
<td class="memItemRight" data-valign="bottom">as_bytes [DBUS_UUID_LENGTH_BYTES]</td>
</tr>
<tr class="memdesc:af45818fb0ae65fdece11aba936af7f09">
<td class="mdescLeft"> </td>
<td class="mdescRight">guid as 16 single-byte values<br />
</td>
</tr>
<tr class="separator:af45818fb0ae65fdece11aba936af7f09">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

A globally unique ID ; we have one for each DBusServer, and also one for each machine with libdbus installed on it.

Definition at line 457 of file dbus-internals.h.

## Field Documentation

## ◆ as_bytes

|                                                   |
|---------------------------------------------------|
| char DBusGUID::as_bytes\[DBUS_UUID_LENGTH_BYTES\] |

guid as 16 single-byte values

Definition at line 460 of file dbus-internals.h.

Referenced by \_dbus_generate_uuid(), and \_dbus_uuid_encode().

## ◆ as_uint32s

|                                                              |
|--------------------------------------------------------------|
| dbus_uint32_t DBusGUID::as_uint32s\[DBUS_UUID_LENGTH_WORDS\] |

guid as four uint32 values

Definition at line 459 of file dbus-internals.h.

Referenced by \_dbus_generate_uuid(), and \_dbus_read_local_machine_uuid().

The documentation for this union was generated from the following file:

- dbus-internals.h
