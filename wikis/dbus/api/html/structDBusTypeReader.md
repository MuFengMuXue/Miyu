DBusTypeReader Struct Reference

The type reader is an iterator for reading values from a block of values. More...

`#include <``dbus-marshal-recursive.h``>`

<table class="memberdecls">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
<td></td>
</tr>
<tr id="r_a238bd0d5a30d8f59fd9b71c95af25563" class="memitem:a238bd0d5a30d8f59fd9b71c95af25563">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const DBusTypeReaderClass * </td>
<td class="memItemRight" data-valign="bottom">klass</td>
<td></td>
</tr>
<tr class="memdesc:a238bd0d5a30d8f59fd9b71c95af25563">
<td class="mdescLeft"> </td>
<td class="mdescRight">the vtable for the reader<br />
</td>
<td></td>
</tr>
<tr class="separator:a238bd0d5a30d8f59fd9b71c95af25563">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_af52e270ededd0aabb642c6130a3e9e40" class="memitem:af52e270ededd0aabb642c6130a3e9e40">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const DBusString * </td>
<td class="memItemRight" data-valign="bottom">type_str</td>
<td></td>
</tr>
<tr class="memdesc:af52e270ededd0aabb642c6130a3e9e40">
<td class="mdescLeft"> </td>
<td class="mdescRight">string containing signature of block<br />
</td>
<td></td>
</tr>
<tr class="separator:af52e270ededd0aabb642c6130a3e9e40">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_a4065d7775758beb044ee23a71875571f" class="memitem:a4065d7775758beb044ee23a71875571f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const DBusString * </td>
<td class="memItemRight" data-valign="bottom">value_str</td>
<td></td>
</tr>
<tr class="memdesc:a4065d7775758beb044ee23a71875571f">
<td class="mdescLeft"> </td>
<td class="mdescRight">string containing values of block<br />
</td>
<td></td>
</tr>
<tr class="separator:a4065d7775758beb044ee23a71875571f">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_aeb0846d954066f420e1df98b81148702" class="memitem:aeb0846d954066f420e1df98b81148702">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">byte_order: 8</td>
<td></td>
</tr>
<tr class="memdesc:aeb0846d954066f420e1df98b81148702">
<td class="mdescLeft"> </td>
<td class="mdescRight">byte order of the block<br />
</td>
<td></td>
</tr>
<tr class="separator:aeb0846d954066f420e1df98b81148702">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_a551e64ee83df38ebda8c3677a91afe1b" class="memitem:a551e64ee83df38ebda8c3677a91afe1b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">finished: 1</td>
<td></td>
</tr>
<tr class="memdesc:a551e64ee83df38ebda8c3677a91afe1b">
<td class="mdescLeft"> </td>
<td class="mdescRight">marks we're at end iterator for cases where we don't have another way to tell<br />
</td>
<td></td>
</tr>
<tr class="separator:a551e64ee83df38ebda8c3677a91afe1b">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_a930fb8d6c82f269b0a151cfb33df86b3" class="memitem:a930fb8d6c82f269b0a151cfb33df86b3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">array_len_offset: 3</td>
<td></td>
</tr>
<tr class="memdesc:a930fb8d6c82f269b0a151cfb33df86b3">
<td class="mdescLeft"> </td>
<td class="mdescRight">bytes back from start_pos that len ends<br />
</td>
<td></td>
</tr>
<tr class="separator:a930fb8d6c82f269b0a151cfb33df86b3">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_a160a55f9869e297572c5aa5b6ce7bc71" class="memitem:a160a55f9869e297572c5aa5b6ce7bc71">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">type_pos</td>
<td></td>
</tr>
<tr class="memdesc:a160a55f9869e297572c5aa5b6ce7bc71">
<td class="mdescLeft"> </td>
<td class="mdescRight">current position in signature<br />
</td>
<td></td>
</tr>
<tr class="separator:a160a55f9869e297572c5aa5b6ce7bc71">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_ac17280869573f060a945a43e4a5c3ca4" class="memitem:ac17280869573f060a945a43e4a5c3ca4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">value_pos</td>
<td></td>
</tr>
<tr class="memdesc:ac17280869573f060a945a43e4a5c3ca4">
<td class="mdescLeft"> </td>
<td class="mdescRight">current position in values<br />
</td>
<td></td>
</tr>
<tr class="separator:ac17280869573f060a945a43e4a5c3ca4">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_a2950278c4b081b1ec600e8850b3facf0" class="memitem:a2950278c4b081b1ec600e8850b3facf0">
<td class="memItemLeft"> union { </td>
<td class="memItemRight" data-valign="bottom"></td>
<td></td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_aa99cf3dff126296e19a824cb62a9415d" class="memitem:aa99cf3dff126296e19a824cb62a9415d">
<td class="memItemLeft">   struct { </td>
<td class="memItemRight" data-valign="bottom"></td>
<td></td>
</tr>
<tr class="separator:a4f5ef6e2b4b33fcb641c48c6389b71ec">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_a92f9a1914e0efef6917e277b04858746" class="memitem:a92f9a1914e0efef6917e277b04858746">
<td class="memItemLeft">      int   start_pos </td>
<td class="memItemRight" data-valign="bottom"></td>
<td></td>
</tr>
<tr class="memdesc:a92f9a1914e0efef6917e277b04858746">
<td class="mdescLeft"> </td>
<td class="mdescRight">for array readers, the start of the array values More...<br />
</td>
<td></td>
</tr>
<tr class="separator:a92f9a1914e0efef6917e277b04858746">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_aa99cf3dff126296e19a824cb62a9415d" class="memitem:aa99cf3dff126296e19a824cb62a9415d">
<td class="memItemLeft" data-valign="top">   }   <strong>array</strong> </td>
<td class="memItemRight" data-valign="bottom"></td>
<td></td>
</tr>
<tr class="separator:aa99cf3dff126296e19a824cb62a9415d">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_a2950278c4b081b1ec600e8850b3facf0" class="memitem:a2950278c4b081b1ec600e8850b3facf0">
<td class="memItemLeft" data-valign="top">} </td>
<td class="memItemRight" data-valign="bottom"><strong>u</strong> </td>
<td class="memItemRight" data-valign="bottom"></td>
</tr>
<tr class="memdesc:a2950278c4b081b1ec600e8850b3facf0">
<td class="mdescLeft"> </td>
<td class="mdescRight">class-specific data<br />
</td>
<td></td>
</tr>
<tr class="separator:a2950278c4b081b1ec600e8850b3facf0">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
</tbody>
</table>

## Detailed Description

The type reader is an iterator for reading values from a block of values.

Definition at line 41 of file dbus-marshal-recursive.h.

## Field Documentation

## ◆ array_len_offset

|                                                |
|------------------------------------------------|
| dbus_uint32_t DBusTypeReader::array_len_offset |

bytes back from start_pos that len ends

Definition at line 52 of file dbus-marshal-recursive.h.

## ◆ byte_order

|                                          |
|------------------------------------------|
| dbus_uint32_t DBusTypeReader::byte_order |

byte order of the block

Definition at line 47 of file dbus-marshal-recursive.h.

Referenced by \_dbus_type_reader_read_basic().

## ◆ finished

|                                        |
|----------------------------------------|
| dbus_uint32_t DBusTypeReader::finished |

marks we're at end iterator for cases where we don't have another way to tell

Definition at line 49 of file dbus-marshal-recursive.h.

Referenced by \_dbus_type_reader_get_current_type().

## ◆ klass

|                                                   |
|---------------------------------------------------|
| const DBusTypeReaderClass\* DBusTypeReader::klass |

the vtable for the reader

Definition at line 43 of file dbus-marshal-recursive.h.

Referenced by \_dbus_type_reader_delete(), \_dbus_type_reader_get_array_length(), \_dbus_type_reader_get_current_type(), \_dbus_type_reader_init(), \_dbus_type_reader_init_types_only(), \_dbus_type_reader_next(), \_dbus_type_reader_read_basic(), \_dbus_type_reader_read_fixed_multi(), \_dbus_type_reader_read_raw(), \_dbus_type_reader_recurse(), and \_dbus_type_reader_set_basic().

## ◆ start_pos

|                               |
|-------------------------------|
| int DBusTypeReader::start_pos |

for array readers, the start of the array values

Definition at line 59 of file dbus-marshal-recursive.h.

Referenced by \_dbus_type_reader_read_fixed_multi().

## ◆ type_pos

|                              |
|------------------------------|
| int DBusTypeReader::type_pos |

current position in signature

Definition at line 53 of file dbus-marshal-recursive.h.

Referenced by \_dbus_type_reader_get_current_type(), \_dbus_type_reader_get_element_type(), \_dbus_type_reader_get_signature(), \_dbus_type_reader_init(), \_dbus_type_reader_init_types_only(), \_dbus_type_reader_next(), \_dbus_type_reader_read_basic(), \_dbus_type_reader_read_fixed_multi(), \_dbus_type_reader_recurse(), and \_dbus_type_reader_set_basic().

## ◆ type_str

|                                             |
|---------------------------------------------|
| const DBusString\* DBusTypeReader::type_str |

string containing signature of block

Definition at line 44 of file dbus-marshal-recursive.h.

Referenced by \_dbus_type_reader_get_current_type(), \_dbus_type_reader_get_element_type(), \_dbus_type_reader_get_signature(), \_dbus_type_reader_init(), \_dbus_type_reader_init_types_only(), \_dbus_type_reader_next(), \_dbus_type_reader_read_basic(), \_dbus_type_reader_read_fixed_multi(), \_dbus_type_reader_recurse(), and \_dbus_type_reader_set_basic().

## ◆ value_pos

|                               |
|-------------------------------|
| int DBusTypeReader::value_pos |

current position in values

Definition at line 54 of file dbus-marshal-recursive.h.

Referenced by \_dbus_type_reader_get_value_pos(), \_dbus_type_reader_init(), \_dbus_type_reader_next(), \_dbus_type_reader_read_basic(), \_dbus_type_reader_read_fixed_multi(), \_dbus_type_reader_read_raw(), \_dbus_type_reader_recurse(), and \_dbus_type_reader_set_basic().

## ◆ value_str

|                                              |
|----------------------------------------------|
| const DBusString\* DBusTypeReader::value_str |

string containing values of block

Definition at line 45 of file dbus-marshal-recursive.h.

Referenced by \_dbus_type_reader_read_basic(), \_dbus_type_reader_read_fixed_multi(), \_dbus_type_reader_read_raw(), and \_dbus_type_reader_set_basic().

The documentation for this struct was generated from the following file:

- dbus-marshal-recursive.h
