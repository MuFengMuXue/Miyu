DBusServerSocket Struct Reference

D-Bus secret internal implementation details » DBusServer implementations for SOCKET

Implementation details of DBusServerSocket. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_ad811bada4239e72eaf91efdb2de9b5e9" class="memitem:ad811bada4239e72eaf91efdb2de9b5e9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusServer </td>
<td class="memItemRight" data-valign="bottom">base</td>
</tr>
<tr class="memdesc:ad811bada4239e72eaf91efdb2de9b5e9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Parent class members.<br />
</td>
</tr>
<tr class="separator:ad811bada4239e72eaf91efdb2de9b5e9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a0585f7f6633ec428ab4a0863cbf4ffb1" class="memitem:a0585f7f6633ec428ab4a0863cbf4ffb1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">n_fds</td>
</tr>
<tr class="memdesc:a0585f7f6633ec428ab4a0863cbf4ffb1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Number of active file handles.<br />
</td>
</tr>
<tr class="separator:a0585f7f6633ec428ab4a0863cbf4ffb1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a6e6ab384583041a83e5783d2d3fab054" class="memitem:a6e6ab384583041a83e5783d2d3fab054">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusSocket * </td>
<td class="memItemRight" data-valign="bottom">fds</td>
</tr>
<tr class="memdesc:a6e6ab384583041a83e5783d2d3fab054">
<td class="mdescLeft"> </td>
<td class="mdescRight">File descriptor or DBUS_SOCKET_INVALID if disconnected.<br />
</td>
</tr>
<tr class="separator:a6e6ab384583041a83e5783d2d3fab054">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a9b0b7c50962dc70abf9f712369761522" class="memitem:a9b0b7c50962dc70abf9f712369761522">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusWatch ** </td>
<td class="memItemRight" data-valign="bottom">watch</td>
</tr>
<tr class="memdesc:a9b0b7c50962dc70abf9f712369761522">
<td class="mdescLeft"> </td>
<td class="mdescRight">File descriptor watch.<br />
</td>
</tr>
<tr class="separator:a9b0b7c50962dc70abf9f712369761522">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ad9467f2872fbf623e72642650af7feb0" class="memitem:ad9467f2872fbf623e72642650af7feb0">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char * </td>
<td class="memItemRight" data-valign="bottom">socket_name</td>
</tr>
<tr class="memdesc:ad9467f2872fbf623e72642650af7feb0">
<td class="mdescLeft"> </td>
<td class="mdescRight">Name of domain socket, to unlink if appropriate.<br />
</td>
</tr>
<tr class="separator:ad9467f2872fbf623e72642650af7feb0">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a6ea3eebf42eba2469bf64eb0f91e1f97" class="memitem:a6ea3eebf42eba2469bf64eb0f91e1f97">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusNonceFile * </td>
<td class="memItemRight" data-valign="bottom">noncefile</td>
</tr>
<tr class="memdesc:a6ea3eebf42eba2469bf64eb0f91e1f97">
<td class="mdescLeft"> </td>
<td class="mdescRight">Nonce file used to authenticate clients.<br />
</td>
</tr>
<tr class="separator:a6ea3eebf42eba2469bf64eb0f91e1f97">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Implementation details of DBusServerSocket.

All members are private.

Definition at line 52 of file dbus-server-socket.c.

## Field Documentation

## ◆ base

|                                   |
|-----------------------------------|
| DBusServer DBusServerSocket::base |

Parent class members.

Definition at line 54 of file dbus-server-socket.c.

Referenced by \_dbus_server_new_for_socket().

## ◆ fds

|                                    |
|------------------------------------|
| DBusSocket\* DBusServerSocket::fds |

File descriptor or DBUS_SOCKET_INVALID if disconnected.

Definition at line 56 of file dbus-server-socket.c.

Referenced by \_dbus_server_new_for_socket().

## ◆ n_fds

|                             |
|-----------------------------|
| int DBusServerSocket::n_fds |

Number of active file handles.

Definition at line 55 of file dbus-server-socket.c.

Referenced by \_dbus_server_new_for_socket().

## ◆ noncefile

|                                             |
|---------------------------------------------|
| DBusNonceFile\* DBusServerSocket::noncefile |

Nonce file used to authenticate clients.

Definition at line 59 of file dbus-server-socket.c.

Referenced by \_dbus_server_new_for_socket().

## ◆ socket_name

|                                      |
|--------------------------------------|
| char\* DBusServerSocket::socket_name |

Name of domain socket, to unlink if appropriate.

Definition at line 58 of file dbus-server-socket.c.

Referenced by \_dbus_server_socket_own_filename().

## ◆ watch

|                                       |
|---------------------------------------|
| DBusWatch\*\* DBusServerSocket::watch |

File descriptor watch.

Definition at line 57 of file dbus-server-socket.c.

Referenced by \_dbus_server_new_for_socket().

The documentation for this struct was generated from the following file:

- dbus-server-socket.c
