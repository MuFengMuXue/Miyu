DBusDirIter Struct Reference

D-Bus secret internal implementation details » Utilities and portability

Internals of directory iterator. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a9b713ab1d8b9b0b621e7555a33def70f" class="memitem:a9b713ab1d8b9b0b621e7555a33def70f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DIR * </td>
<td class="memItemRight" data-valign="bottom">d</td>
</tr>
<tr class="memdesc:a9b713ab1d8b9b0b621e7555a33def70f">
<td class="mdescLeft"> </td>
<td class="mdescRight">The DIR* from opendir()<br />
</td>
</tr>
<tr class="separator:a9b713ab1d8b9b0b621e7555a33def70f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_abcb381a2a55f9e95ac058725442e314a" class="memitem:abcb381a2a55f9e95ac058725442e314a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">HANDLE </td>
<td class="memItemRight" data-valign="bottom">handle</td>
</tr>
<tr class="separator:abcb381a2a55f9e95ac058725442e314a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a12e6b3a0dbf346e35fee53dd93cf8a75" class="memitem:a12e6b3a0dbf346e35fee53dd93cf8a75">
<td class="memItemLeft" style="text-align: right;" data-valign="top">WIN32_FIND_DATAA </td>
<td class="memItemRight" data-valign="bottom">fileinfo</td>
</tr>
<tr class="separator:a12e6b3a0dbf346e35fee53dd93cf8a75">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a0a288f7ba80a9a4e8926a7b043529e56" class="memitem:a0a288f7ba80a9a4e8926a7b043529e56">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">finished</td>
</tr>
<tr class="separator:a0a288f7ba80a9a4e8926a7b043529e56">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aac8bca93fec3a6302fa9d833ebd23539" class="memitem:aac8bca93fec3a6302fa9d833ebd23539">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">offset</td>
</tr>
<tr class="separator:aac8bca93fec3a6302fa9d833ebd23539">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Internals of directory iterator.

Definition at line 627 of file dbus-sysdeps-util-unix.c.

## Field Documentation

## ◆ d

|                      |
|----------------------|
| DIR\* DBusDirIter::d |

The DIR\* from opendir()

Definition at line 629 of file dbus-sysdeps-util-unix.c.

Referenced by \_dbus_directory_close(), \_dbus_directory_get_next_file(), and \_dbus_directory_open().

## ◆ fileinfo

|                                        |
|----------------------------------------|
| WIN32_FIND_DATAA DBusDirIter::fileinfo |

Definition at line 398 of file dbus-sysdeps-util-win.c.

## ◆ finished

|                                   |
|-----------------------------------|
| dbus_bool_t DBusDirIter::finished |

Definition at line 399 of file dbus-sysdeps-util-win.c.

## ◆ handle

|                            |
|----------------------------|
| HANDLE DBusDirIter::handle |

Definition at line 397 of file dbus-sysdeps-util-win.c.

## ◆ offset

|                         |
|-------------------------|
| int DBusDirIter::offset |

Definition at line 400 of file dbus-sysdeps-util-win.c.

The documentation for this struct was generated from the following files:

- dbus-sysdeps-util-unix.c
- dbus-sysdeps-util-win.c
