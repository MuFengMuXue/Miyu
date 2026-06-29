DBusUserInfo Struct Reference

D-Bus secret internal implementation details » UNIX-specific internal API

Information about a UNIX user. More...

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
<tr id="r_aa71802c450c38967363a92bd0e498215" class="memitem:aa71802c450c38967363a92bd0e498215">
<td class="memItemLeft" style="text-align: right;" data-valign="top">size_t </td>
<td class="memItemRight" data-valign="bottom">refcount</td>
</tr>
<tr class="memdesc:aa71802c450c38967363a92bd0e498215">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reference count.<br />
</td>
</tr>
<tr class="separator:aa71802c450c38967363a92bd0e498215">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a2d9c74d29f371e391a79b81162050b2e" class="memitem:a2d9c74d29f371e391a79b81162050b2e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uid_t </td>
<td class="memItemRight" data-valign="bottom">uid</td>
</tr>
<tr class="memdesc:a2d9c74d29f371e391a79b81162050b2e">
<td class="mdescLeft"> </td>
<td class="mdescRight">UID.<br />
</td>
</tr>
<tr class="separator:a2d9c74d29f371e391a79b81162050b2e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ac970de2fac9ea4ba91485e6c37c3bf93" class="memitem:ac970de2fac9ea4ba91485e6c37c3bf93">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_gid_t </td>
<td class="memItemRight" data-valign="bottom">primary_gid</td>
</tr>
<tr class="memdesc:ac970de2fac9ea4ba91485e6c37c3bf93">
<td class="mdescLeft"> </td>
<td class="mdescRight">GID.<br />
</td>
</tr>
<tr class="separator:ac970de2fac9ea4ba91485e6c37c3bf93">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a902af9e0fb7d37c14eefb7d2b016ab11" class="memitem:a902af9e0fb7d37c14eefb7d2b016ab11">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_gid_t * </td>
<td class="memItemRight" data-valign="bottom">group_ids</td>
</tr>
<tr class="memdesc:a902af9e0fb7d37c14eefb7d2b016ab11">
<td class="mdescLeft"> </td>
<td class="mdescRight">Groups IDs, <em>including</em> above primary group.<br />
</td>
</tr>
<tr class="separator:a902af9e0fb7d37c14eefb7d2b016ab11">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a21c07867fbffb1854a97aed265d87c89" class="memitem:a21c07867fbffb1854a97aed265d87c89">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">n_group_ids</td>
</tr>
<tr class="memdesc:a21c07867fbffb1854a97aed265d87c89">
<td class="mdescLeft"> </td>
<td class="mdescRight">Size of group IDs array.<br />
</td>
</tr>
<tr class="separator:a21c07867fbffb1854a97aed265d87c89">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ac6b57db1dc8315eee3f532f4e77912d1" class="memitem:ac6b57db1dc8315eee3f532f4e77912d1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char * </td>
<td class="memItemRight" data-valign="bottom">username</td>
</tr>
<tr class="memdesc:ac6b57db1dc8315eee3f532f4e77912d1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Username.<br />
</td>
</tr>
<tr class="separator:ac6b57db1dc8315eee3f532f4e77912d1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a5235d4d021cd134e1130e1e8e912bc0c" class="memitem:a5235d4d021cd134e1130e1e8e912bc0c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char * </td>
<td class="memItemRight" data-valign="bottom">homedir</td>
</tr>
<tr class="memdesc:a5235d4d021cd134e1130e1e8e912bc0c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Home directory.<br />
</td>
</tr>
<tr class="separator:a5235d4d021cd134e1130e1e8e912bc0c">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Information about a UNIX user.

Definition at line 92 of file dbus-sysdeps-unix.h.

## Field Documentation

## ◆ group_ids

|                                      |
|--------------------------------------|
| dbus_gid_t\* DBusUserInfo::group_ids |

Groups IDs, *including* above primary group.

Definition at line 97 of file dbus-sysdeps-unix.h.

Referenced by \_dbus_groups_from_uid(), and \_dbus_user_info_free().

## ◆ homedir

|                              |
|------------------------------|
| char\* DBusUserInfo::homedir |

Home directory.

Definition at line 100 of file dbus-sysdeps-unix.h.

Referenced by \_dbus_homedir_from_uid(), and \_dbus_user_info_free().

## ◆ n_group_ids

|                               |
|-------------------------------|
| int DBusUserInfo::n_group_ids |

Size of group IDs array.

Definition at line 98 of file dbus-sysdeps-unix.h.

Referenced by \_dbus_groups_from_uid().

## ◆ primary_gid

|                                      |
|--------------------------------------|
| dbus_gid_t DBusUserInfo::primary_gid |

GID.

Definition at line 96 of file dbus-sysdeps-unix.h.

Referenced by \_dbus_get_user_id_and_primary_group().

## ◆ refcount

|                               |
|-------------------------------|
| size_t DBusUserInfo::refcount |

Reference count.

Definition at line 94 of file dbus-sysdeps-unix.h.

Referenced by \_dbus_user_database_lookup(), and \_dbus_user_info_unref().

## ◆ uid

|                              |
|------------------------------|
| dbus_uid_t DBusUserInfo::uid |

UID.

Definition at line 95 of file dbus-sysdeps-unix.h.

Referenced by \_dbus_credentials_add_from_user(), \_dbus_get_user_id_and_primary_group(), \_dbus_groups_from_uid(), and \_dbus_user_database_lookup().

## ◆ username

|                               |
|-------------------------------|
| char\* DBusUserInfo::username |

Username.

Definition at line 99 of file dbus-sysdeps-unix.h.

Referenced by \_dbus_user_database_lookup(), and \_dbus_user_info_free().

The documentation for this struct was generated from the following file:

- dbus-sysdeps-unix.h
