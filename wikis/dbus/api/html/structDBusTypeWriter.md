DBusTypeWriter Struct Reference

The type writer is an iterator for writing to a block of values. More...

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
<tr id="r_a95204ef3a9cf29ee31687032b142b836" class="memitem:a95204ef3a9cf29ee31687032b142b836">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusString * </td>
<td class="memItemRight" data-valign="bottom">type_str</td>
<td></td>
</tr>
<tr class="memdesc:a95204ef3a9cf29ee31687032b142b836">
<td class="mdescLeft"> </td>
<td class="mdescRight">where to write typecodes (or read type expectations)<br />
</td>
<td></td>
</tr>
<tr class="separator:a95204ef3a9cf29ee31687032b142b836">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_aa4e4b3af31fd7a93d0e54d10882bcc07" class="memitem:aa4e4b3af31fd7a93d0e54d10882bcc07">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusString * </td>
<td class="memItemRight" data-valign="bottom">value_str</td>
<td></td>
</tr>
<tr class="memdesc:aa4e4b3af31fd7a93d0e54d10882bcc07">
<td class="mdescLeft"> </td>
<td class="mdescRight">where to write values<br />
</td>
<td></td>
</tr>
<tr class="separator:aa4e4b3af31fd7a93d0e54d10882bcc07">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_a6c4baf0b7148cf3f76924b654dada148" class="memitem:a6c4baf0b7148cf3f76924b654dada148">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">byte_order: 8</td>
<td></td>
</tr>
<tr class="memdesc:a6c4baf0b7148cf3f76924b654dada148">
<td class="mdescLeft"> </td>
<td class="mdescRight">byte order to write values with<br />
</td>
<td></td>
</tr>
<tr class="separator:a6c4baf0b7148cf3f76924b654dada148">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_ad0953035070c7c7d21b044b7b2f0f491" class="memitem:ad0953035070c7c7d21b044b7b2f0f491">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">container_type: 8</td>
<td></td>
</tr>
<tr class="memdesc:ad0953035070c7c7d21b044b7b2f0f491">
<td class="mdescLeft"> </td>
<td class="mdescRight">what are we inside? (e.g.<br />
</td>
<td></td>
</tr>
<tr class="separator:ad0953035070c7c7d21b044b7b2f0f491">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_ae6db89e9a3adcd52678dc089810cfb0b" class="memitem:ae6db89e9a3adcd52678dc089810cfb0b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">type_pos_is_expectation: 1</td>
<td></td>
</tr>
<tr class="memdesc:ae6db89e9a3adcd52678dc089810cfb0b">
<td class="mdescLeft"> </td>
<td class="mdescRight">type_pos can be either an insertion point for or an expected next type<br />
</td>
<td></td>
</tr>
<tr class="separator:ae6db89e9a3adcd52678dc089810cfb0b">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_a52c8617918c108d36b947cbdfc99c6ea" class="memitem:a52c8617918c108d36b947cbdfc99c6ea">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">enabled: 1</td>
<td></td>
</tr>
<tr class="memdesc:a52c8617918c108d36b947cbdfc99c6ea">
<td class="mdescLeft"> </td>
<td class="mdescRight">whether to write values<br />
</td>
<td></td>
</tr>
<tr class="separator:a52c8617918c108d36b947cbdfc99c6ea">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_a77c19debc0427372f368cfe7188951f8" class="memitem:a77c19debc0427372f368cfe7188951f8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">type_pos</td>
<td></td>
</tr>
<tr class="memdesc:a77c19debc0427372f368cfe7188951f8">
<td class="mdescLeft"> </td>
<td class="mdescRight">current pos in type_str<br />
</td>
<td></td>
</tr>
<tr class="separator:a77c19debc0427372f368cfe7188951f8">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_a27c0475eedd90be65f90a799e5210947" class="memitem:a27c0475eedd90be65f90a799e5210947">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">value_pos</td>
<td></td>
</tr>
<tr class="memdesc:a27c0475eedd90be65f90a799e5210947">
<td class="mdescLeft"> </td>
<td class="mdescRight">next position to write<br />
</td>
<td></td>
</tr>
<tr class="separator:a27c0475eedd90be65f90a799e5210947">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_a6ba3a4afe7a5e0dc557cb4f747975977" class="memitem:a6ba3a4afe7a5e0dc557cb4f747975977">
<td class="memItemLeft"> union { </td>
<td class="memItemRight" data-valign="bottom"></td>
<td></td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_a93995f5a40fe37fdc6272f3ef9495796" class="memitem:a93995f5a40fe37fdc6272f3ef9495796">
<td class="memItemLeft">   struct { </td>
<td class="memItemRight" data-valign="bottom"></td>
<td></td>
</tr>
<tr class="separator:a3418315620dd1ae8170ecc2f3d14829f">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_a116c231e4fb2c392f39663ba32c61168" class="memitem:a116c231e4fb2c392f39663ba32c61168">
<td class="memItemLeft">      int   start_pos </td>
<td class="memItemRight" data-valign="bottom"></td>
<td></td>
</tr>
<tr class="memdesc:a116c231e4fb2c392f39663ba32c61168">
<td class="mdescLeft"> </td>
<td class="mdescRight">position of first element in the array More...<br />
</td>
<td></td>
</tr>
<tr class="separator:a116c231e4fb2c392f39663ba32c61168">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_a6ab5a357b194f98982112522b5502ba4" class="memitem:a6ab5a357b194f98982112522b5502ba4">
<td class="memItemLeft">      int   len_pos </td>
<td class="memItemRight" data-valign="bottom"></td>
<td></td>
</tr>
<tr class="memdesc:a6ab5a357b194f98982112522b5502ba4">
<td class="mdescLeft"> </td>
<td class="mdescRight">position of length of the array More...<br />
</td>
<td></td>
</tr>
<tr class="separator:a6ab5a357b194f98982112522b5502ba4">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_a1533116254d85d68f274eb49be0c2842" class="memitem:a1533116254d85d68f274eb49be0c2842">
<td class="memItemLeft">      int   element_type_pos </td>
<td class="memItemRight" data-valign="bottom"></td>
<td></td>
</tr>
<tr class="memdesc:a1533116254d85d68f274eb49be0c2842">
<td class="mdescLeft"> </td>
<td class="mdescRight">position of array element type in type_str More...<br />
</td>
<td></td>
</tr>
<tr class="separator:a1533116254d85d68f274eb49be0c2842">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_a93995f5a40fe37fdc6272f3ef9495796" class="memitem:a93995f5a40fe37fdc6272f3ef9495796">
<td class="memItemLeft" data-valign="top">   }   <strong>array</strong> </td>
<td class="memItemRight" data-valign="bottom"></td>
<td></td>
</tr>
<tr class="separator:a93995f5a40fe37fdc6272f3ef9495796">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_a6ba3a4afe7a5e0dc557cb4f747975977" class="memitem:a6ba3a4afe7a5e0dc557cb4f747975977">
<td class="memItemLeft" data-valign="top">} </td>
<td class="memItemRight" data-valign="bottom"><strong>u</strong> </td>
<td class="memItemRight" data-valign="bottom"></td>
</tr>
<tr class="memdesc:a6ba3a4afe7a5e0dc557cb4f747975977">
<td class="mdescLeft"> </td>
<td class="mdescRight">class-specific data<br />
</td>
<td></td>
</tr>
<tr class="separator:a6ba3a4afe7a5e0dc557cb4f747975977">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
</tbody>
</table>

## Detailed Description

The type writer is an iterator for writing to a block of values.

Definition at line 67 of file dbus-marshal-recursive.h.

## Field Documentation

## ◆ byte_order

|                                          |
|------------------------------------------|
| dbus_uint32_t DBusTypeWriter::byte_order |

byte order to write values with

Definition at line 71 of file dbus-marshal-recursive.h.

Referenced by \_dbus_type_writer_init(), \_dbus_type_writer_unrecurse(), and \_dbus_type_writer_write_fixed_multi().

## ◆ container_type

|                                              |
|----------------------------------------------|
| dbus_uint32_t DBusTypeWriter::container_type |

what are we inside? (e.g.

struct, variant, array)

Definition at line 73 of file dbus-marshal-recursive.h.

Referenced by \_dbus_type_writer_init(), \_dbus_type_writer_unrecurse(), \_dbus_type_writer_write_fixed_multi(), and dbus_message_iter_append_fixed_array().

## ◆ element_type_pos

|                                      |
|--------------------------------------|
| int DBusTypeWriter::element_type_pos |

position of array element type in type_str

Definition at line 87 of file dbus-marshal-recursive.h.

## ◆ enabled

|                                       |
|---------------------------------------|
| dbus_uint32_t DBusTypeWriter::enabled |

whether to write values

Definition at line 77 of file dbus-marshal-recursive.h.

Referenced by \_dbus_type_writer_init(), \_dbus_type_writer_write_basic(), and \_dbus_type_writer_write_fixed_multi().

## ◆ len_pos

|                             |
|-----------------------------|
| int DBusTypeWriter::len_pos |

position of length of the array

Definition at line 86 of file dbus-marshal-recursive.h.

Referenced by \_dbus_header_set_field_basic(), and \_dbus_type_writer_unrecurse().

## ◆ start_pos

|                               |
|-------------------------------|
| int DBusTypeWriter::start_pos |

position of first element in the array

Definition at line 85 of file dbus-marshal-recursive.h.

Referenced by \_dbus_header_set_field_basic().

## ◆ type_pos

|                              |
|------------------------------|
| int DBusTypeWriter::type_pos |

current pos in type_str

Definition at line 79 of file dbus-marshal-recursive.h.

Referenced by \_dbus_type_writer_add_types(), \_dbus_type_writer_init(), \_dbus_type_writer_remove_types(), \_dbus_type_writer_unrecurse(), \_dbus_type_writer_write_basic(), and \_dbus_type_writer_write_fixed_multi().

## ◆ type_pos_is_expectation

|                                                       |
|-------------------------------------------------------|
| dbus_uint32_t DBusTypeWriter::type_pos_is_expectation |

type_pos can be either an insertion point for or an expected next type

Definition at line 75 of file dbus-marshal-recursive.h.

Referenced by \_dbus_type_writer_init(), \_dbus_type_writer_init_values_only(), \_dbus_type_writer_unrecurse(), \_dbus_type_writer_write_basic(), and \_dbus_type_writer_write_fixed_multi().

## ◆ type_str

|                                       |
|---------------------------------------|
| DBusString\* DBusTypeWriter::type_str |

where to write typecodes (or read type expectations)

Definition at line 69 of file dbus-marshal-recursive.h.

Referenced by \_dbus_type_writer_add_types(), \_dbus_type_writer_init(), \_dbus_type_writer_remove_types(), \_dbus_type_writer_unrecurse(), and \_dbus_type_writer_write_basic().

## ◆ value_pos

|                               |
|-------------------------------|
| int DBusTypeWriter::value_pos |

next position to write

Definition at line 80 of file dbus-marshal-recursive.h.

Referenced by \_dbus_header_set_field_basic(), \_dbus_type_writer_init(), \_dbus_type_writer_unrecurse(), \_dbus_type_writer_write_basic(), and \_dbus_type_writer_write_fixed_multi().

## ◆ value_str

|                                        |
|----------------------------------------|
| DBusString\* DBusTypeWriter::value_str |

where to write values

Definition at line 70 of file dbus-marshal-recursive.h.

Referenced by \_dbus_type_writer_init(), \_dbus_type_writer_unrecurse(), and \_dbus_type_writer_write_fixed_multi().

The documentation for this struct was generated from the following file:

- dbus-marshal-recursive.h
