DBusPreallocatedSend Struct Reference

D-Bus secret internal implementation details » DBusConnection implementation details

Internals of DBusPreallocatedSend. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a465af3647772c89500df0b46f43d035b" class="memitem:a465af3647772c89500df0b46f43d035b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusConnection * </td>
<td class="memItemRight" data-valign="bottom">connection</td>
</tr>
<tr class="memdesc:a465af3647772c89500df0b46f43d035b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Connection we'd send the message to.<br />
</td>
</tr>
<tr class="separator:a465af3647772c89500df0b46f43d035b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ae164fe13f866bebbd714b526104c5bff" class="memitem:ae164fe13f866bebbd714b526104c5bff">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusList * </td>
<td class="memItemRight" data-valign="bottom">queue_link</td>
</tr>
<tr class="memdesc:ae164fe13f866bebbd714b526104c5bff">
<td class="mdescLeft"> </td>
<td class="mdescRight">Preallocated link in the queue.<br />
</td>
</tr>
<tr class="separator:ae164fe13f866bebbd714b526104c5bff">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aae6c1bd98f78491482d5f59b6ef138d4" class="memitem:aae6c1bd98f78491482d5f59b6ef138d4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusList * </td>
<td class="memItemRight" data-valign="bottom">counter_link</td>
</tr>
<tr class="memdesc:aae6c1bd98f78491482d5f59b6ef138d4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Preallocated link in the resource counter.<br />
</td>
</tr>
<tr class="separator:aae6c1bd98f78491482d5f59b6ef138d4">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Internals of DBusPreallocatedSend.

Definition at line 242 of file dbus-connection.c.

## Field Documentation

## ◆ connection

|                                                   |
|---------------------------------------------------|
| DBusConnection\* DBusPreallocatedSend::connection |

Connection we'd send the message to.

Definition at line 244 of file dbus-connection.c.

Referenced by dbus_connection_free_preallocated_send(), and dbus_connection_send_preallocated().

## ◆ counter_link

|                                               |
|-----------------------------------------------|
| DBusList\* DBusPreallocatedSend::counter_link |

Preallocated link in the resource counter.

Definition at line 246 of file dbus-connection.c.

Referenced by dbus_connection_free_preallocated_send().

## ◆ queue_link

|                                             |
|---------------------------------------------|
| DBusList\* DBusPreallocatedSend::queue_link |

Preallocated link in the queue.

Definition at line 245 of file dbus-connection.c.

Referenced by dbus_connection_free_preallocated_send().

The documentation for this struct was generated from the following file:

- dbus-connection.c
