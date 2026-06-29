DBusAddressEntry Struct Reference

D-Bus secret internal implementation details » Address parsing

Internals of DBusAddressEntry. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a2d88ca4208738ec7024655013373505f" class="memitem:a2d88ca4208738ec7024655013373505f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusString </td>
<td class="memItemRight" data-valign="bottom">method</td>
</tr>
<tr class="memdesc:a2d88ca4208738ec7024655013373505f">
<td class="mdescLeft"> </td>
<td class="mdescRight">The address type (unix, tcp, etc.)<br />
</td>
</tr>
<tr class="separator:a2d88ca4208738ec7024655013373505f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a62999fb785b591efa6356b7d97729846" class="memitem:a62999fb785b591efa6356b7d97729846">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusList * </td>
<td class="memItemRight" data-valign="bottom">keys</td>
</tr>
<tr class="memdesc:a62999fb785b591efa6356b7d97729846">
<td class="mdescLeft"> </td>
<td class="mdescRight">List of keys.<br />
</td>
</tr>
<tr class="separator:a62999fb785b591efa6356b7d97729846">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a504d8c6e3d3b6f94a9be32a1d6ab54e8" class="memitem:a504d8c6e3d3b6f94a9be32a1d6ab54e8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusList * </td>
<td class="memItemRight" data-valign="bottom">values</td>
</tr>
<tr class="memdesc:a504d8c6e3d3b6f94a9be32a1d6ab54e8">
<td class="mdescLeft"> </td>
<td class="mdescRight">List of values.<br />
</td>
</tr>
<tr class="separator:a504d8c6e3d3b6f94a9be32a1d6ab54e8">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Internals of DBusAddressEntry.

Definition at line 48 of file dbus-address.c.

## Field Documentation

## ◆ keys

|                                   |
|-----------------------------------|
| DBusList\* DBusAddressEntry::keys |

List of keys.

Definition at line 52 of file dbus-address.c.

Referenced by dbus_address_entry_get_value(), and dbus_parse_address().

## ◆ method

|                                     |
|-------------------------------------|
| DBusString DBusAddressEntry::method |

The address type (unix, tcp, etc.)

Definition at line 50 of file dbus-address.c.

Referenced by dbus_address_entry_get_method(), and dbus_parse_address().

## ◆ values

|                                     |
|-------------------------------------|
| DBusList\* DBusAddressEntry::values |

List of values.

Definition at line 53 of file dbus-address.c.

Referenced by dbus_address_entry_get_value(), and dbus_parse_address().

The documentation for this struct was generated from the following file:

- dbus-address.c
