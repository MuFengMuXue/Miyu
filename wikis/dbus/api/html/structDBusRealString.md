DBusRealString Struct Reference

Internals of DBusString. More...

`#include <``dbus-string-private.h``>`

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_ad60d27edba516b0a179ce1ead1e74725" class="memitem:ad60d27edba516b0a179ce1ead1e74725">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned char * </td>
<td class="memItemRight" data-valign="bottom">str</td>
</tr>
<tr class="memdesc:ad60d27edba516b0a179ce1ead1e74725">
<td class="mdescLeft"> </td>
<td class="mdescRight">String data, plus nul termination.<br />
</td>
</tr>
<tr class="separator:ad60d27edba516b0a179ce1ead1e74725">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aed6f543f7b748c4f5cf92b9aedd5f68d" class="memitem:aed6f543f7b748c4f5cf92b9aedd5f68d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">len</td>
</tr>
<tr class="memdesc:aed6f543f7b748c4f5cf92b9aedd5f68d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Length without nul.<br />
</td>
</tr>
<tr class="separator:aed6f543f7b748c4f5cf92b9aedd5f68d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ae12ec58c271e47f3f89fae1410b7c5e5" class="memitem:ae12ec58c271e47f3f89fae1410b7c5e5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">allocated</td>
</tr>
<tr class="memdesc:ae12ec58c271e47f3f89fae1410b7c5e5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Allocated size of data.<br />
</td>
</tr>
<tr class="separator:ae12ec58c271e47f3f89fae1410b7c5e5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a79675cfbe443cc779e3c668fbcb99578" class="memitem:a79675cfbe443cc779e3c668fbcb99578">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">constant: 1</td>
</tr>
<tr class="memdesc:a79675cfbe443cc779e3c668fbcb99578">
<td class="mdescLeft"> </td>
<td class="mdescRight">String data is not owned by DBusString.<br />
</td>
</tr>
<tr class="separator:a79675cfbe443cc779e3c668fbcb99578">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a865d892d7cacedd598b828c15c5815c5" class="memitem:a865d892d7cacedd598b828c15c5815c5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">locked: 1</td>
</tr>
<tr class="memdesc:a865d892d7cacedd598b828c15c5815c5">
<td class="mdescLeft"> </td>
<td class="mdescRight">DBusString has been locked and can't be changed.<br />
</td>
</tr>
<tr class="separator:a865d892d7cacedd598b828c15c5815c5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a4807c39b3e75da922502cda5f07ef7a5" class="memitem:a4807c39b3e75da922502cda5f07ef7a5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">valid: 1</td>
</tr>
<tr class="memdesc:a4807c39b3e75da922502cda5f07ef7a5">
<td class="mdescLeft"> </td>
<td class="mdescRight">DBusString is valid (initialized and not freed)<br />
</td>
</tr>
<tr class="separator:a4807c39b3e75da922502cda5f07ef7a5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a21fb373a65e36646787392a3dfe62443" class="memitem:a21fb373a65e36646787392a3dfe62443">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">align_offset: 3</td>
</tr>
<tr class="memdesc:a21fb373a65e36646787392a3dfe62443">
<td class="mdescLeft"> </td>
<td class="mdescRight">str - align_offset is the actual malloc block<br />
</td>
</tr>
<tr class="separator:a21fb373a65e36646787392a3dfe62443">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Internals of DBusString.

DBusString internals. DBusString is an opaque objects, it must be used via accessor functions.

Definition at line 45 of file dbus-string-private.h.

## Field Documentation

## ◆ align_offset

|                                           |
|-------------------------------------------|
| unsigned int DBusRealString::align_offset |

str - align_offset is the actual malloc block

Definition at line 53 of file dbus-string-private.h.

Referenced by \_dbus_string_free(), \_dbus_string_init_const_len(), \_dbus_string_init_preallocated(), and \_dbus_string_zero().

## ◆ allocated

|                               |
|-------------------------------|
| int DBusRealString::allocated |

Allocated size of data.

Definition at line 49 of file dbus-string-private.h.

Referenced by \_dbus_string_free(), \_dbus_string_get_allocated_size(), \_dbus_string_init_const_len(), \_dbus_string_init_preallocated(), and \_dbus_string_zero().

## ◆ constant

|                                       |
|---------------------------------------|
| unsigned int DBusRealString::constant |

String data is not owned by DBusString.

Definition at line 50 of file dbus-string-private.h.

Referenced by \_dbus_string_free(), \_dbus_string_init_const_len(), and \_dbus_string_init_preallocated().

## ◆ len

|                         |
|-------------------------|
| int DBusRealString::len |

Length without nul.

Definition at line 48 of file dbus-string-private.h.

Referenced by \_dbus_string_append_byte(), \_dbus_string_append_printf_valist(), \_dbus_string_copy_data(), \_dbus_string_copy_to_buffer(), \_dbus_string_copy_to_buffer_with_nul(), \_dbus_string_ends_with_c_str(), \_dbus_string_equal(), \_dbus_string_equal_c_str(), \_dbus_string_equal_len(), \_dbus_string_equal_substring(), \_dbus_string_find_blank(), \_dbus_string_find_eol(), \_dbus_string_free(), \_dbus_string_get_length(), \_dbus_string_init_const_len(), \_dbus_string_init_preallocated(), \_dbus_string_lengthen(), \_dbus_string_move(), \_dbus_string_shorten(), \_dbus_string_skip_blank(), \_dbus_string_skip_white(), \_dbus_string_starts_with_c_str(), \_dbus_string_validate_ascii(), \_dbus_string_validate_nul(), and \_dbus_string_validate_utf8().

## ◆ locked

|                                     |
|-------------------------------------|
| unsigned int DBusRealString::locked |

DBusString has been locked and can't be changed.

Definition at line 51 of file dbus-string-private.h.

Referenced by \_dbus_string_free(), \_dbus_string_init_const_len(), and \_dbus_string_init_preallocated().

## ◆ str

|                                     |
|-------------------------------------|
| unsigned char\* DBusRealString::str |

String data, plus nul termination.

Definition at line 47 of file dbus-string-private.h.

Referenced by \_dbus_string_append_byte(), \_dbus_string_append_printf_valist(), \_dbus_string_copy_data(), \_dbus_string_copy_to_buffer(), \_dbus_string_copy_to_buffer_with_nul(), \_dbus_string_ends_with_c_str(), \_dbus_string_equal(), \_dbus_string_equal_c_str(), \_dbus_string_equal_len(), \_dbus_string_equal_substring(), \_dbus_string_find_blank(), \_dbus_string_find_eol(), \_dbus_string_find_to(), \_dbus_string_free(), \_dbus_string_get_byte(), \_dbus_string_get_const_data(), \_dbus_string_get_const_data_len(), \_dbus_string_get_data(), \_dbus_string_get_data_len(), \_dbus_string_init_const_len(), \_dbus_string_init_preallocated(), \_dbus_string_insert_2_aligned(), \_dbus_string_insert_4_aligned(), \_dbus_string_insert_8_aligned(), \_dbus_string_insert_byte(), \_dbus_string_insert_bytes(), \_dbus_string_set_byte(), \_dbus_string_skip_blank(), \_dbus_string_skip_white(), \_dbus_string_skip_white_reverse(), \_dbus_string_starts_with_c_str(), \_dbus_string_steal_data(), \_dbus_string_tolower_ascii(), \_dbus_string_toupper_ascii(), \_dbus_string_validate_ascii(), \_dbus_string_validate_nul(), \_dbus_string_validate_utf8(), and \_dbus_string_zero().

## ◆ valid

|                                    |
|------------------------------------|
| unsigned int DBusRealString::valid |

DBusString is valid (initialized and not freed)

Definition at line 52 of file dbus-string-private.h.

Referenced by \_dbus_string_free(), \_dbus_string_init_const_len(), and \_dbus_string_init_preallocated().

The documentation for this struct was generated from the following file:

- dbus-string-private.h
