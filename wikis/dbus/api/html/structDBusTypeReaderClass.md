DBusTypeReaderClass Struct Reference

D-Bus secret internal implementation details » marshaling and unmarshaling

Virtual table for a type reader. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_afd813c32ff4b8b96266efe392dc25a89" class="memitem:afd813c32ff4b8b96266efe392dc25a89">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">name</td>
</tr>
<tr class="memdesc:afd813c32ff4b8b96266efe392dc25a89">
<td class="mdescLeft"> </td>
<td class="mdescRight">name for debugging<br />
</td>
</tr>
<tr class="separator:afd813c32ff4b8b96266efe392dc25a89">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a7cd297c0e03c5204bc41bf305c7688c9" class="memitem:a7cd297c0e03c5204bc41bf305c7688c9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">id</td>
</tr>
<tr class="memdesc:a7cd297c0e03c5204bc41bf305c7688c9">
<td class="mdescLeft"> </td>
<td class="mdescRight">index in all_reader_classes<br />
</td>
</tr>
<tr class="separator:a7cd297c0e03c5204bc41bf305c7688c9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ad886037cd736e6f5cdbefb834b0bd5e7" class="memitem:ad886037cd736e6f5cdbefb834b0bd5e7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">types_only</td>
</tr>
<tr class="memdesc:ad886037cd736e6f5cdbefb834b0bd5e7">
<td class="mdescLeft"> </td>
<td class="mdescRight">only iterates over types, not values<br />
</td>
</tr>
<tr class="separator:ad886037cd736e6f5cdbefb834b0bd5e7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aaf42cdbcd74f4d5cf1ae10d439d4b979" class="memitem:aaf42cdbcd74f4d5cf1ae10d439d4b979">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void(* </td>
<td class="memItemRight" data-valign="bottom">recurse )(DBusTypeReader *sub, DBusTypeReader *parent)</td>
</tr>
<tr class="memdesc:aaf42cdbcd74f4d5cf1ae10d439d4b979">
<td class="mdescLeft"> </td>
<td class="mdescRight">recurse with this reader as sub<br />
</td>
</tr>
<tr class="separator:aaf42cdbcd74f4d5cf1ae10d439d4b979">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a8f8c7594971fbb43ce1369109549e760" class="memitem:a8f8c7594971fbb43ce1369109549e760">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t(* </td>
<td class="memItemRight" data-valign="bottom">check_finished )(const DBusTypeReader *reader)</td>
</tr>
<tr class="memdesc:a8f8c7594971fbb43ce1369109549e760">
<td class="mdescLeft"> </td>
<td class="mdescRight">check whether reader is at the end<br />
</td>
</tr>
<tr class="separator:a8f8c7594971fbb43ce1369109549e760">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a78a7bc50971abd8fd54d53109a5058cc" class="memitem:a78a7bc50971abd8fd54d53109a5058cc">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void(* </td>
<td class="memItemRight" data-valign="bottom">next )(DBusTypeReader *reader, int current_type)</td>
</tr>
<tr class="memdesc:a78a7bc50971abd8fd54d53109a5058cc">
<td class="mdescLeft"> </td>
<td class="mdescRight">go to the next value<br />
</td>
</tr>
<tr class="separator:a78a7bc50971abd8fd54d53109a5058cc">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Virtual table for a type reader.

Definition at line 127 of file dbus-marshal-recursive.c.

## Field Documentation

## ◆ check_finished

|  |
|----|
| dbus_bool_t(\* DBusTypeReaderClass::check_finished) (const DBusTypeReader \*reader) |

check whether reader is at the end

Definition at line 134 of file dbus-marshal-recursive.c.

Referenced by \_dbus_type_reader_get_current_type().

## ◆ id

|                             |
|-----------------------------|
| int DBusTypeReaderClass::id |

index in all_reader_classes

Definition at line 130 of file dbus-marshal-recursive.c.

Referenced by \_dbus_type_reader_recurse().

## ◆ name

|                                        |
|----------------------------------------|
| const char\* DBusTypeReaderClass::name |

name for debugging

Definition at line 129 of file dbus-marshal-recursive.c.

## ◆ next

|  |
|----|
| void(\* DBusTypeReaderClass::next) (DBusTypeReader \*reader, int current_type) |

go to the next value

Definition at line 135 of file dbus-marshal-recursive.c.

Referenced by \_dbus_type_reader_next().

## ◆ recurse

|  |
|----|
| void(\* DBusTypeReaderClass::recurse) (DBusTypeReader \*sub, DBusTypeReader \*parent) |

recurse with this reader as sub

Definition at line 132 of file dbus-marshal-recursive.c.

Referenced by \_dbus_type_reader_recurse().

## ◆ types_only

|                                             |
|---------------------------------------------|
| dbus_bool_t DBusTypeReaderClass::types_only |

only iterates over types, not values

Definition at line 131 of file dbus-marshal-recursive.c.

Referenced by \_dbus_type_reader_get_array_length(), \_dbus_type_reader_read_basic(), \_dbus_type_reader_read_fixed_multi(), \_dbus_type_reader_read_raw(), \_dbus_type_reader_recurse(), and \_dbus_type_reader_set_basic().

The documentation for this struct was generated from the following file:

- dbus-marshal-recursive.c
