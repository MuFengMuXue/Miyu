DBusStat Struct Reference

D-Bus secret internal implementation details » Internal system-dependent API

Portable struct with stat() results. More...

`#include <``dbus-sysdeps.h``>`

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a722ec64f90cf29e0b8bafaea55b90d27" class="memitem:a722ec64f90cf29e0b8bafaea55b90d27">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned long </td>
<td class="memItemRight" data-valign="bottom">mode</td>
</tr>
<tr class="memdesc:a722ec64f90cf29e0b8bafaea55b90d27">
<td class="mdescLeft"> </td>
<td class="mdescRight">File mode.<br />
</td>
</tr>
<tr class="separator:a722ec64f90cf29e0b8bafaea55b90d27">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a1b5ef4ce7f46c798d4b222c61f8912f7" class="memitem:a1b5ef4ce7f46c798d4b222c61f8912f7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned long </td>
<td class="memItemRight" data-valign="bottom">nlink</td>
</tr>
<tr class="memdesc:a1b5ef4ce7f46c798d4b222c61f8912f7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Number of hard links.<br />
</td>
</tr>
<tr class="separator:a1b5ef4ce7f46c798d4b222c61f8912f7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a300fac914534803bcfacdd87b15e1a8d" class="memitem:a300fac914534803bcfacdd87b15e1a8d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uid_t </td>
<td class="memItemRight" data-valign="bottom">uid</td>
</tr>
<tr class="memdesc:a300fac914534803bcfacdd87b15e1a8d">
<td class="mdescLeft"> </td>
<td class="mdescRight">User owning file.<br />
</td>
</tr>
<tr class="separator:a300fac914534803bcfacdd87b15e1a8d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a98dd4c45ffc8488b399cb3feb57ef48c" class="memitem:a98dd4c45ffc8488b399cb3feb57ef48c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_gid_t </td>
<td class="memItemRight" data-valign="bottom">gid</td>
</tr>
<tr class="memdesc:a98dd4c45ffc8488b399cb3feb57ef48c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Group owning file.<br />
</td>
</tr>
<tr class="separator:a98dd4c45ffc8488b399cb3feb57ef48c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a1b8b518248d41601766ae955bdca0de2" class="memitem:a1b8b518248d41601766ae955bdca0de2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned long </td>
<td class="memItemRight" data-valign="bottom">size</td>
</tr>
<tr class="memdesc:a1b8b518248d41601766ae955bdca0de2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Size of file.<br />
</td>
</tr>
<tr class="separator:a1b8b518248d41601766ae955bdca0de2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a9c68f29816af750a47d80177a23d6cf1" class="memitem:a9c68f29816af750a47d80177a23d6cf1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned long </td>
<td class="memItemRight" data-valign="bottom">atime</td>
</tr>
<tr class="memdesc:a9c68f29816af750a47d80177a23d6cf1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Access time.<br />
</td>
</tr>
<tr class="separator:a9c68f29816af750a47d80177a23d6cf1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_acf4750b66ccb06b49c7eaf2405d8c417" class="memitem:acf4750b66ccb06b49c7eaf2405d8c417">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned long </td>
<td class="memItemRight" data-valign="bottom">mtime</td>
</tr>
<tr class="memdesc:acf4750b66ccb06b49c7eaf2405d8c417">
<td class="mdescLeft"> </td>
<td class="mdescRight">Modify time.<br />
</td>
</tr>
<tr class="separator:acf4750b66ccb06b49c7eaf2405d8c417">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aceb3c4a3230d1a9063baee27c140fbb3" class="memitem:aceb3c4a3230d1a9063baee27c140fbb3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned long </td>
<td class="memItemRight" data-valign="bottom">ctime</td>
</tr>
<tr class="memdesc:aceb3c4a3230d1a9063baee27c140fbb3">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creation time.<br />
</td>
</tr>
<tr class="separator:aceb3c4a3230d1a9063baee27c140fbb3">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Portable struct with stat() results.

Definition at line 569 of file dbus-sysdeps.h.

## Field Documentation

## ◆ atime

|                               |
|-------------------------------|
| unsigned long DBusStat::atime |

Access time.

Definition at line 576 of file dbus-sysdeps.h.

Referenced by \_dbus_stat().

## ◆ ctime

|                               |
|-------------------------------|
| unsigned long DBusStat::ctime |

Creation time.

Definition at line 578 of file dbus-sysdeps.h.

Referenced by \_dbus_stat().

## ◆ gid

|                          |
|--------------------------|
| dbus_gid_t DBusStat::gid |

Group owning file.

Definition at line 574 of file dbus-sysdeps.h.

Referenced by \_dbus_stat().

## ◆ mode

|                              |
|------------------------------|
| unsigned long DBusStat::mode |

File mode.

Definition at line 571 of file dbus-sysdeps.h.

Referenced by \_dbus_stat().

## ◆ mtime

|                               |
|-------------------------------|
| unsigned long DBusStat::mtime |

Modify time.

Definition at line 577 of file dbus-sysdeps.h.

Referenced by \_dbus_stat().

## ◆ nlink

|                               |
|-------------------------------|
| unsigned long DBusStat::nlink |

Number of hard links.

Definition at line 572 of file dbus-sysdeps.h.

Referenced by \_dbus_stat().

## ◆ size

|                              |
|------------------------------|
| unsigned long DBusStat::size |

Size of file.

Definition at line 575 of file dbus-sysdeps.h.

Referenced by \_dbus_stat().

## ◆ uid

|                          |
|--------------------------|
| dbus_uid_t DBusStat::uid |

User owning file.

Definition at line 573 of file dbus-sysdeps.h.

Referenced by \_dbus_is_console_user(), and \_dbus_stat().

The documentation for this struct was generated from the following file:

- dbus-sysdeps.h
