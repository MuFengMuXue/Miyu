DBusBasicValue Union Reference

D-Bus low-level public API » Basic types

A simple value union that lets you access bytes as if they were various types; useful when dealing with basic types via void pointers and varargs. More...

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
<tr id="r_ae22a61c9f193ebba8dc695c19536a4ff" class="memitem:ae22a61c9f193ebba8dc695c19536a4ff">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned char </td>
<td class="memItemRight" data-valign="bottom">bytes [8]</td>
</tr>
<tr class="memdesc:ae22a61c9f193ebba8dc695c19536a4ff">
<td class="mdescLeft"> </td>
<td class="mdescRight">as 8 individual bytes<br />
</td>
</tr>
<tr class="separator:ae22a61c9f193ebba8dc695c19536a4ff">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_abb50966adffc03072dac1a991bf2b878" class="memitem:abb50966adffc03072dac1a991bf2b878">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_int16_t </td>
<td class="memItemRight" data-valign="bottom">i16</td>
</tr>
<tr class="memdesc:abb50966adffc03072dac1a991bf2b878">
<td class="mdescLeft"> </td>
<td class="mdescRight">as int16<br />
</td>
</tr>
<tr class="separator:abb50966adffc03072dac1a991bf2b878">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a96bb883967d05d7c0acceb0d95821aa3" class="memitem:a96bb883967d05d7c0acceb0d95821aa3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint16_t </td>
<td class="memItemRight" data-valign="bottom">u16</td>
</tr>
<tr class="memdesc:a96bb883967d05d7c0acceb0d95821aa3">
<td class="mdescLeft"> </td>
<td class="mdescRight">as int16<br />
</td>
</tr>
<tr class="separator:a96bb883967d05d7c0acceb0d95821aa3">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a084b19510a8cfdb648c9f489a0aa6778" class="memitem:a084b19510a8cfdb648c9f489a0aa6778">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_int32_t </td>
<td class="memItemRight" data-valign="bottom">i32</td>
</tr>
<tr class="memdesc:a084b19510a8cfdb648c9f489a0aa6778">
<td class="mdescLeft"> </td>
<td class="mdescRight">as int32<br />
</td>
</tr>
<tr class="separator:a084b19510a8cfdb648c9f489a0aa6778">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a2501e54560ae240442d9d841b96b086b" class="memitem:a2501e54560ae240442d9d841b96b086b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">u32</td>
</tr>
<tr class="memdesc:a2501e54560ae240442d9d841b96b086b">
<td class="mdescLeft"> </td>
<td class="mdescRight">as int32<br />
</td>
</tr>
<tr class="separator:a2501e54560ae240442d9d841b96b086b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aef567e756e5241c39a16f174809f7b38" class="memitem:aef567e756e5241c39a16f174809f7b38">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">bool_val</td>
</tr>
<tr class="memdesc:aef567e756e5241c39a16f174809f7b38">
<td class="mdescLeft"> </td>
<td class="mdescRight">as boolean<br />
</td>
</tr>
<tr class="separator:aef567e756e5241c39a16f174809f7b38">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a17dbd77e86848f152d8bcde2f955eb92" class="memitem:a17dbd77e86848f152d8bcde2f955eb92">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_int64_t </td>
<td class="memItemRight" data-valign="bottom">i64</td>
</tr>
<tr class="memdesc:a17dbd77e86848f152d8bcde2f955eb92">
<td class="mdescLeft"> </td>
<td class="mdescRight">as int64<br />
</td>
</tr>
<tr class="separator:a17dbd77e86848f152d8bcde2f955eb92">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a675c1684b9f5bedbb5d445eee3594165" class="memitem:a675c1684b9f5bedbb5d445eee3594165">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint64_t </td>
<td class="memItemRight" data-valign="bottom">u64</td>
</tr>
<tr class="memdesc:a675c1684b9f5bedbb5d445eee3594165">
<td class="mdescLeft"> </td>
<td class="mdescRight">as int64<br />
</td>
</tr>
<tr class="separator:a675c1684b9f5bedbb5d445eee3594165">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a8edd92b11787b8caee989745bc97a165" class="memitem:a8edd92b11787b8caee989745bc97a165">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBus8ByteStruct </td>
<td class="memItemRight" data-valign="bottom">eight</td>
</tr>
<tr class="memdesc:a8edd92b11787b8caee989745bc97a165">
<td class="mdescLeft"> </td>
<td class="mdescRight">as 8-byte struct<br />
</td>
</tr>
<tr class="separator:a8edd92b11787b8caee989745bc97a165">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a70daca267bc747c1c3b0a362f0a9bb56" class="memitem:a70daca267bc747c1c3b0a362f0a9bb56">
<td class="memItemLeft" style="text-align: right;" data-valign="top">double </td>
<td class="memItemRight" data-valign="bottom">dbl</td>
</tr>
<tr class="memdesc:a70daca267bc747c1c3b0a362f0a9bb56">
<td class="mdescLeft"> </td>
<td class="mdescRight">as double<br />
</td>
</tr>
<tr class="separator:a70daca267bc747c1c3b0a362f0a9bb56">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aa350d50ad1d1bffa5286f583f4c9d0ba" class="memitem:aa350d50ad1d1bffa5286f583f4c9d0ba">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned char </td>
<td class="memItemRight" data-valign="bottom">byt</td>
</tr>
<tr class="memdesc:aa350d50ad1d1bffa5286f583f4c9d0ba">
<td class="mdescLeft"> </td>
<td class="mdescRight">as byte<br />
</td>
</tr>
<tr class="separator:aa350d50ad1d1bffa5286f583f4c9d0ba">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_acbcb55156f8bee7eb0d88bd5ce46b3d5" class="memitem:acbcb55156f8bee7eb0d88bd5ce46b3d5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char * </td>
<td class="memItemRight" data-valign="bottom">str</td>
</tr>
<tr class="memdesc:acbcb55156f8bee7eb0d88bd5ce46b3d5">
<td class="mdescLeft"> </td>
<td class="mdescRight">as char* (string, object path or signature)<br />
</td>
</tr>
<tr class="separator:acbcb55156f8bee7eb0d88bd5ce46b3d5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a746e33be333899dac37f981e05a512ed" class="memitem:a746e33be333899dac37f981e05a512ed">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">fd</td>
</tr>
<tr class="memdesc:a746e33be333899dac37f981e05a512ed">
<td class="mdescLeft"> </td>
<td class="mdescRight">as Unix file descriptor<br />
</td>
</tr>
<tr class="separator:a746e33be333899dac37f981e05a512ed">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

A simple value union that lets you access bytes as if they were various types; useful when dealing with basic types via void pointers and varargs.

This union also contains a pointer member (which can be used to retrieve a string from dbus_message_iter_get_basic(), for instance), so on future platforms it could conceivably be larger than 8 bytes.

Definition at line 160 of file dbus-types.h.

## Field Documentation

## ◆ bool_val

|                                      |
|--------------------------------------|
| dbus_bool_t DBusBasicValue::bool_val |

as boolean

Definition at line 167 of file dbus-types.h.

## ◆ byt

|                                   |
|-----------------------------------|
| unsigned char DBusBasicValue::byt |

as byte

Definition at line 172 of file dbus-types.h.

## ◆ bytes

|                                          |
|------------------------------------------|
| unsigned char DBusBasicValue::bytes\[8\] |

as 8 individual bytes

Definition at line 162 of file dbus-types.h.

## ◆ dbl

|                            |
|----------------------------|
| double DBusBasicValue::dbl |

as double

Definition at line 171 of file dbus-types.h.

## ◆ eight

|                                       |
|---------------------------------------|
| DBus8ByteStruct DBusBasicValue::eight |

as 8-byte struct

Definition at line 170 of file dbus-types.h.

## ◆ fd

|                        |
|------------------------|
| int DBusBasicValue::fd |

as Unix file descriptor

Definition at line 174 of file dbus-types.h.

## ◆ i16

|                                  |
|----------------------------------|
| dbus_int16_t DBusBasicValue::i16 |

as int16

Definition at line 163 of file dbus-types.h.

## ◆ i32

|                                  |
|----------------------------------|
| dbus_int32_t DBusBasicValue::i32 |

as int32

Definition at line 165 of file dbus-types.h.

## ◆ i64

|                                  |
|----------------------------------|
| dbus_int64_t DBusBasicValue::i64 |

as int64

Definition at line 168 of file dbus-types.h.

## ◆ str

|                            |
|----------------------------|
| char\* DBusBasicValue::str |

as char\* (string, object path or signature)

Definition at line 173 of file dbus-types.h.

## ◆ u16

|                                   |
|-----------------------------------|
| dbus_uint16_t DBusBasicValue::u16 |

as int16

Definition at line 164 of file dbus-types.h.

## ◆ u32

|                                   |
|-----------------------------------|
| dbus_uint32_t DBusBasicValue::u32 |

as int32

Definition at line 166 of file dbus-types.h.

Referenced by \_dbus_message_iter_get_args_valist(), dbus_message_iter_get_basic(), and dbus_message_set_reply_serial().

## ◆ u64

|                                   |
|-----------------------------------|
| dbus_uint64_t DBusBasicValue::u64 |

as int64

Definition at line 169 of file dbus-types.h.

The documentation for this union was generated from the following file:

- dbus-types.h
