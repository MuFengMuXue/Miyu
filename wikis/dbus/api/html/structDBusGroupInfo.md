DBusGroupInfo Struct Reference

D-Bus secret internal implementation details » UNIX-specific internal API

Information about a UNIX group. More...

`#include <``dbus-sysdeps-unix.h``>`

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_afb90c03715c7a5e606e36a47c07a3431" class="memitem:afb90c03715c7a5e606e36a47c07a3431">
<td class="memItemLeft" style="text-align: right;" data-valign="top">size_t </td>
<td class="memItemRight" data-valign="bottom">refcount</td>
</tr>
<tr class="memdesc:afb90c03715c7a5e606e36a47c07a3431">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reference count.<br />
</td>
</tr>
<tr class="separator:afb90c03715c7a5e606e36a47c07a3431">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a583e8d6d421fa85fb1d43789efae4b75" class="memitem:a583e8d6d421fa85fb1d43789efae4b75">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_gid_t </td>
<td class="memItemRight" data-valign="bottom">gid</td>
</tr>
<tr class="memdesc:a583e8d6d421fa85fb1d43789efae4b75">
<td class="mdescLeft"> </td>
<td class="mdescRight">GID.<br />
</td>
</tr>
<tr class="separator:a583e8d6d421fa85fb1d43789efae4b75">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_af1a4b925663336f64c62cfcab40571c6" class="memitem:af1a4b925663336f64c62cfcab40571c6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char * </td>
<td class="memItemRight" data-valign="bottom">groupname</td>
</tr>
<tr class="memdesc:af1a4b925663336f64c62cfcab40571c6">
<td class="mdescLeft"> </td>
<td class="mdescRight">Group name.<br />
</td>
</tr>
<tr class="separator:af1a4b925663336f64c62cfcab40571c6">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Information about a UNIX group.

Definition at line 106 of file dbus-sysdeps-unix.h.

## Field Documentation

## ◆ gid

|                               |
|-------------------------------|
| dbus_gid_t DBusGroupInfo::gid |

GID.

Definition at line 109 of file dbus-sysdeps-unix.h.

Referenced by \_dbus_get_group_id(), and \_dbus_user_database_lookup_group().

## ◆ groupname

|                                 |
|---------------------------------|
| char\* DBusGroupInfo::groupname |

Group name.

Definition at line 110 of file dbus-sysdeps-unix.h.

Referenced by \_dbus_group_info_free(), and \_dbus_user_database_lookup_group().

## ◆ refcount

|                                |
|--------------------------------|
| size_t DBusGroupInfo::refcount |

Reference count.

Definition at line 108 of file dbus-sysdeps-unix.h.

Referenced by \_dbus_group_info_unref(), and \_dbus_user_database_lookup_group().

The documentation for this struct was generated from the following file:

- dbus-sysdeps-unix.h
