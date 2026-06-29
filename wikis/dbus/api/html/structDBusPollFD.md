DBusPollFD Struct Reference

D-Bus secret internal implementation details » Internal system-dependent API

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_abf790977358a9f52ae77347ca125162a" class="memitem:abf790977358a9f52ae77347ca125162a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusPollable </td>
<td class="memItemRight" data-valign="bottom">fd</td>
</tr>
<tr class="memdesc:abf790977358a9f52ae77347ca125162a">
<td class="mdescLeft"> </td>
<td class="mdescRight">File descriptor.<br />
</td>
</tr>
<tr class="separator:abf790977358a9f52ae77347ca125162a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a10e65e6721451e92361497b2efaa758f" class="memitem:a10e65e6721451e92361497b2efaa758f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">short </td>
<td class="memItemRight" data-valign="bottom">events</td>
</tr>
<tr class="memdesc:a10e65e6721451e92361497b2efaa758f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Events to poll for.<br />
</td>
</tr>
<tr class="separator:a10e65e6721451e92361497b2efaa758f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a24bc29c766b8bbddc5da052e7a46bc9e" class="memitem:a24bc29c766b8bbddc5da052e7a46bc9e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">short </td>
<td class="memItemRight" data-valign="bottom">revents</td>
</tr>
<tr class="memdesc:a24bc29c766b8bbddc5da052e7a46bc9e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Events that occurred.<br />
</td>
</tr>
<tr class="separator:a24bc29c766b8bbddc5da052e7a46bc9e">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Definition at line 436 of file dbus-sysdeps.h.

## Field Documentation

## ◆ events

|                          |
|--------------------------|
| short DBusPollFD::events |

Events to poll for.

Definition at line 439 of file dbus-sysdeps.h.

Referenced by \_dbus_poll().

## ◆ fd

|                             |
|-----------------------------|
| DBusPollable DBusPollFD::fd |

File descriptor.

Definition at line 438 of file dbus-sysdeps.h.

Referenced by \_dbus_poll().

## ◆ revents

|                           |
|---------------------------|
| short DBusPollFD::revents |

Events that occurred.

Definition at line 440 of file dbus-sysdeps.h.

Referenced by \_dbus_poll().

The documentation for this struct was generated from the following file:

- dbus-sysdeps.h
