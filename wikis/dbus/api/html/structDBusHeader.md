DBusHeader Struct Reference

Message header data and some cached details of it. More...

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
<tr id="r_a67df8bff43c10e2d4f6ae36b56ee5814" class="memitem:a67df8bff43c10e2d4f6ae36b56ee5814">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusString </td>
<td class="memItemRight" data-valign="bottom">data</td>
</tr>
<tr class="memdesc:a67df8bff43c10e2d4f6ae36b56ee5814">
<td class="mdescLeft"> </td>
<td class="mdescRight">Header network data, stored separately from body so we can independently realloc it.<br />
</td>
</tr>
<tr class="separator:a67df8bff43c10e2d4f6ae36b56ee5814">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ac58a309593d0dc7e8d5a02f3b3442384" class="memitem:ac58a309593d0dc7e8d5a02f3b3442384">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusHeaderField </td>
<td class="memItemRight" data-valign="bottom">fields [DBUS_HEADER_FIELD_LAST+1]</td>
</tr>
<tr class="memdesc:ac58a309593d0dc7e8d5a02f3b3442384">
<td class="mdescLeft"> </td>
<td class="mdescRight">Track the location of each field in header.<br />
</td>
</tr>
<tr class="separator:ac58a309593d0dc7e8d5a02f3b3442384">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aa22a8d00f061310e12716f656b4d9b8f" class="memitem:aa22a8d00f061310e12716f656b4d9b8f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">padding: 3</td>
</tr>
<tr class="memdesc:aa22a8d00f061310e12716f656b4d9b8f">
<td class="mdescLeft"> </td>
<td class="mdescRight">0-7 bytes of alignment in header, the distance from [B] to [C]<br />
</td>
</tr>
<tr class="separator:aa22a8d00f061310e12716f656b4d9b8f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_abb64abdf3c7f3fbf77c511ccf1f07aa1" class="memitem:abb64abdf3c7f3fbf77c511ccf1f07aa1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">byte_order: 8</td>
</tr>
<tr class="memdesc:abb64abdf3c7f3fbf77c511ccf1f07aa1">
<td class="mdescLeft"> </td>
<td class="mdescRight">byte order of header (must always match the content of byte 0)<br />
</td>
</tr>
<tr class="separator:abb64abdf3c7f3fbf77c511ccf1f07aa1">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Message header data and some cached details of it.

A message looks like this:

\| 0 \| 1 \| 2 \| 3 \| 4 \| 5 \| 6 \| 7 \| \<- index % 8

\|-------\|-------\|-------\|------\|-----\|-----\|-----\|-----\|

\| Order \| Type \| Flags \| Vers \| Body length \|

\| Serial \| Fields array length \[A\]

\[A\] Code \|Sig.len\| Signature + \0 \| Content...\| \<- first field

\| Content ... \| Pad to 8-byte boundary\|

\| Code \|Sig.len\| Signature + \0 \| Content... \| \<- second field

...

\| Code \|Sig.len\| Signature \| Content... \| \<- last field

\| Content ... \[B\] Padding to 8-byte boundary \[C\]

\[C\] Body ... \|

...

\| Body ... \[D\] \<- no padding after natural length

DBusHeader::padding

dbus_uint32_t padding

0-7 bytes of alignment in header, the distance from \[B\] to \[C\]

**Definition** dbus-marshal-header.h:106

Each field is a struct\<byte,variant\>. All structs have 8-byte alignment, so each field is preceded by 0-7 bytes of padding to an 8-byte boundary (for the first field it happens to be 0 bytes). The overall header is followed by 0-7 bytes of padding to align the body.

Key to content, with variable name references for \_dbus_header_load():

Order: byte order, currently 'l' or 'B' (byte_order) Type: message type such as DBUS_MESSAGE_TYPE_METHOD_CALL Flags: message flags such as DBUS_HEADER_FLAG_NO_REPLY_EXPECTED Vers: D-Bus wire protocol version, currently always 1 Body length: Distance from \[C\] to \[D\] Serial: Message serial number Fields array length: Distance from \[A\] to \[B\] (fields_array_len)

To understand \_dbus_header_load():

\[A\] is FIRST_FIELD_OFFSET. header_len is from 0 to \[C\]. padding_start is \[B\]. padding_len is the padding from \[B\] to \[C\].

Definition at line 89 of file dbus-marshal-header.h.

## Field Documentation

## ◆ byte_order

|                                      |
|--------------------------------------|
| dbus_uint32_t DBusHeader::byte_order |

byte order of header (must always match the content of byte 0)

Definition at line 108 of file dbus-marshal-header.h.

## ◆ data

|                             |
|-----------------------------|
| DBusString DBusHeader::data |

Header network data, stored separately from body so we can independently realloc it.

Its length includes up to 8 bytes of padding to align the body to an 8-byte boundary.

In a steady state, this has length \[C\]. During editing, it is temporarily extended to have the maximum possible padding.

Definition at line 91 of file dbus-marshal-header.h.

Referenced by \_dbus_header_byteswap(), \_dbus_header_copy(), \_dbus_header_create(), \_dbus_header_free(), \_dbus_header_get_byte_order(), \_dbus_header_get_field_basic(), \_dbus_header_get_field_raw(), \_dbus_header_get_flag(), \_dbus_header_get_message_type(), \_dbus_header_get_serial(), \_dbus_header_init(), \_dbus_header_load(), \_dbus_header_reinit(), \_dbus_header_remove_unknown_fields(), \_dbus_header_set_field_basic(), \_dbus_header_set_serial(), \_dbus_header_toggle_flag(), \_dbus_header_update_lengths(), \_dbus_message_add_counter_link(), \_dbus_message_get_network_data(), and dbus_message_marshal().

## ◆ fields

|                                                                |
|----------------------------------------------------------------|
| DBusHeaderField DBusHeader::fields\[DBUS_HEADER_FIELD_LAST+1\] |

Track the location of each field in header.

Definition at line 102 of file dbus-marshal-header.h.

Referenced by \_dbus_header_get_field_basic(), \_dbus_header_get_field_raw(), and \_dbus_header_load().

## ◆ padding

|                                   |
|-----------------------------------|
| dbus_uint32_t DBusHeader::padding |

0-7 bytes of alignment in header, the distance from \[B\] to \[C\]

Definition at line 106 of file dbus-marshal-header.h.

Referenced by \_dbus_header_create(), \_dbus_header_load(), and \_dbus_header_reinit().

The documentation for this struct was generated from the following file:

- dbus-marshal-header.h
