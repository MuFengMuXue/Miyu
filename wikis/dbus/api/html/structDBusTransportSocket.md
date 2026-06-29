DBusTransportSocket Struct Reference

D-Bus secret internal implementation details » DBusTransport implementations for sockets

Implementation details of DBusTransportSocket. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_ab820e51211635434c40ffa812d8013e5" class="memitem:ab820e51211635434c40ffa812d8013e5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusTransport </td>
<td class="memItemRight" data-valign="bottom">base</td>
</tr>
<tr class="memdesc:ab820e51211635434c40ffa812d8013e5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Parent instance.<br />
</td>
</tr>
<tr class="separator:ab820e51211635434c40ffa812d8013e5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aa800b2aade80ee151e4c1589320920bf" class="memitem:aa800b2aade80ee151e4c1589320920bf">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusSocket </td>
<td class="memItemRight" data-valign="bottom">fd</td>
</tr>
<tr class="memdesc:aa800b2aade80ee151e4c1589320920bf">
<td class="mdescLeft"> </td>
<td class="mdescRight">File descriptor.<br />
</td>
</tr>
<tr class="separator:aa800b2aade80ee151e4c1589320920bf">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aba60b33603091a87f7cbd2a8e76cd8f6" class="memitem:aba60b33603091a87f7cbd2a8e76cd8f6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusWatch * </td>
<td class="memItemRight" data-valign="bottom">read_watch</td>
</tr>
<tr class="memdesc:aba60b33603091a87f7cbd2a8e76cd8f6">
<td class="mdescLeft"> </td>
<td class="mdescRight">Watch for readability.<br />
</td>
</tr>
<tr class="separator:aba60b33603091a87f7cbd2a8e76cd8f6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a0134735f074583b16a91d7f54bfcccb9" class="memitem:a0134735f074583b16a91d7f54bfcccb9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusWatch * </td>
<td class="memItemRight" data-valign="bottom">write_watch</td>
</tr>
<tr class="memdesc:a0134735f074583b16a91d7f54bfcccb9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Watch for writability.<br />
</td>
</tr>
<tr class="separator:a0134735f074583b16a91d7f54bfcccb9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ac70dd065b0e2805198432d93f5f4f5dc" class="memitem:ac70dd065b0e2805198432d93f5f4f5dc">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">max_bytes_read_per_iteration</td>
</tr>
<tr class="memdesc:ac70dd065b0e2805198432d93f5f4f5dc">
<td class="mdescLeft"> </td>
<td class="mdescRight">To avoid blocking too long.<br />
</td>
</tr>
<tr class="separator:ac70dd065b0e2805198432d93f5f4f5dc">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a5e8631812d429f8567974836627ab3de" class="memitem:a5e8631812d429f8567974836627ab3de">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">max_bytes_written_per_iteration</td>
</tr>
<tr class="memdesc:a5e8631812d429f8567974836627ab3de">
<td class="mdescLeft"> </td>
<td class="mdescRight">To avoid blocking too long.<br />
</td>
</tr>
<tr class="separator:a5e8631812d429f8567974836627ab3de">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a5304711c08da21ef109e3c736a8bcfe7" class="memitem:a5304711c08da21ef109e3c736a8bcfe7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">message_bytes_written</td>
</tr>
<tr class="memdesc:a5304711c08da21ef109e3c736a8bcfe7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Number of bytes of current outgoing message that have been written.<br />
</td>
</tr>
<tr class="separator:a5304711c08da21ef109e3c736a8bcfe7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a88925e2ff68a30457c0fee211812c5d6" class="memitem:a88925e2ff68a30457c0fee211812c5d6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusString </td>
<td class="memItemRight" data-valign="bottom">encoded_outgoing</td>
</tr>
<tr class="memdesc:a88925e2ff68a30457c0fee211812c5d6">
<td class="mdescLeft"> </td>
<td class="mdescRight">Encoded version of current outgoing message.<br />
</td>
</tr>
<tr class="separator:a88925e2ff68a30457c0fee211812c5d6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a840f1a09f5256b5c737e3e45beb47966" class="memitem:a840f1a09f5256b5c737e3e45beb47966">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusString </td>
<td class="memItemRight" data-valign="bottom">encoded_incoming</td>
</tr>
<tr class="memdesc:a840f1a09f5256b5c737e3e45beb47966">
<td class="mdescLeft"> </td>
<td class="mdescRight">Encoded version of current incoming data.<br />
</td>
</tr>
<tr class="separator:a840f1a09f5256b5c737e3e45beb47966">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Implementation details of DBusTransportSocket.

All members are private.

Definition at line 54 of file dbus-transport-socket.c.

## Field Documentation

## ◆ base

|                                         |
|-----------------------------------------|
| DBusTransport DBusTransportSocket::base |

Parent instance.

Definition at line 56 of file dbus-transport-socket.c.

Referenced by \_dbus_transport_new_for_socket().

## ◆ encoded_incoming

|                                                  |
|--------------------------------------------------|
| DBusString DBusTransportSocket::encoded_incoming |

Encoded version of current incoming data.

Definition at line 71 of file dbus-transport-socket.c.

Referenced by \_dbus_transport_new_for_socket().

## ◆ encoded_outgoing

|                                                  |
|--------------------------------------------------|
| DBusString DBusTransportSocket::encoded_outgoing |

Encoded version of current outgoing message.

Definition at line 68 of file dbus-transport-socket.c.

Referenced by \_dbus_transport_new_for_socket().

## ◆ fd

|                                    |
|------------------------------------|
| DBusSocket DBusTransportSocket::fd |

File descriptor.

Definition at line 57 of file dbus-transport-socket.c.

Referenced by \_dbus_transport_new_for_socket().

## ◆ max_bytes_read_per_iteration

|                                                       |
|-------------------------------------------------------|
| int DBusTransportSocket::max_bytes_read_per_iteration |

To avoid blocking too long.

Definition at line 61 of file dbus-transport-socket.c.

Referenced by \_dbus_transport_new_for_socket().

## ◆ max_bytes_written_per_iteration

|                                                          |
|----------------------------------------------------------|
| int DBusTransportSocket::max_bytes_written_per_iteration |

To avoid blocking too long.

Definition at line 62 of file dbus-transport-socket.c.

Referenced by \_dbus_transport_new_for_socket().

## ◆ message_bytes_written

|                                                |
|------------------------------------------------|
| int DBusTransportSocket::message_bytes_written |

Number of bytes of current outgoing message that have been written.

Definition at line 64 of file dbus-transport-socket.c.

Referenced by \_dbus_transport_new_for_socket().

## ◆ read_watch

|                                             |
|---------------------------------------------|
| DBusWatch\* DBusTransportSocket::read_watch |

Watch for readability.

Definition at line 58 of file dbus-transport-socket.c.

Referenced by \_dbus_transport_new_for_socket().

## ◆ write_watch

|                                              |
|----------------------------------------------|
| DBusWatch\* DBusTransportSocket::write_watch |

Watch for writability.

Definition at line 59 of file dbus-transport-socket.c.

Referenced by \_dbus_transport_new_for_socket().

The documentation for this struct was generated from the following file:

- dbus-transport-socket.c
