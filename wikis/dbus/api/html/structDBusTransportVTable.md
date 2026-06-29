DBusTransportVTable Struct Reference

The virtual table that must be implemented to create a new kind of transport. More...

`#include <``dbus-transport-protected.h``>`

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a9bbe617a905faabcb6cfbdd03c614f2f" class="memitem:a9bbe617a905faabcb6cfbdd03c614f2f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void(* </td>
<td class="memItemRight" data-valign="bottom">finalize )(DBusTransport *transport)</td>
</tr>
<tr class="memdesc:a9bbe617a905faabcb6cfbdd03c614f2f">
<td class="mdescLeft"> </td>
<td class="mdescRight">The finalize method must free the transport.<br />
</td>
</tr>
<tr class="separator:a9bbe617a905faabcb6cfbdd03c614f2f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a74cde1923f193922094d862b82272bb9" class="memitem:a74cde1923f193922094d862b82272bb9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t(* </td>
<td class="memItemRight" data-valign="bottom">handle_watch )(DBusTransport *transport, DBusWatch *watch, unsigned int flags)</td>
</tr>
<tr class="memdesc:a74cde1923f193922094d862b82272bb9">
<td class="mdescLeft"> </td>
<td class="mdescRight">The handle_watch method handles reading/writing data as indicated by the flags.<br />
</td>
</tr>
<tr class="separator:a74cde1923f193922094d862b82272bb9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a4026d799445410dff8d65e28f04ab13a" class="memitem:a4026d799445410dff8d65e28f04ab13a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void(* </td>
<td class="memItemRight" data-valign="bottom">disconnect )(DBusTransport *transport)</td>
</tr>
<tr class="memdesc:a4026d799445410dff8d65e28f04ab13a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Disconnect this transport.<br />
</td>
</tr>
<tr class="separator:a4026d799445410dff8d65e28f04ab13a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aa9b0084556577b5a3d7bd25f0ff5878e" class="memitem:aa9b0084556577b5a3d7bd25f0ff5878e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t(* </td>
<td class="memItemRight" data-valign="bottom">connection_set )(DBusTransport *transport)</td>
</tr>
<tr class="memdesc:aa9b0084556577b5a3d7bd25f0ff5878e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Called when transport-&gt;connection has been filled in.<br />
</td>
</tr>
<tr class="separator:aa9b0084556577b5a3d7bd25f0ff5878e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a55fa4b2141b5945c70aeb062fbcd6419" class="memitem:a55fa4b2141b5945c70aeb062fbcd6419">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void(* </td>
<td class="memItemRight" data-valign="bottom">do_iteration )(DBusTransport *transport, unsigned int flags, int timeout_milliseconds)</td>
</tr>
<tr class="memdesc:a55fa4b2141b5945c70aeb062fbcd6419">
<td class="mdescLeft"> </td>
<td class="mdescRight">Called to do a single "iteration" (block on select/poll followed by reading or writing data).<br />
</td>
</tr>
<tr class="separator:a55fa4b2141b5945c70aeb062fbcd6419">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a47f3ece7ffd13e2f9b3fdeb0c6876643" class="memitem:a47f3ece7ffd13e2f9b3fdeb0c6876643">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void(* </td>
<td class="memItemRight" data-valign="bottom">live_messages_changed )(DBusTransport *transport)</td>
</tr>
<tr class="memdesc:a47f3ece7ffd13e2f9b3fdeb0c6876643">
<td class="mdescLeft"> </td>
<td class="mdescRight">Outstanding messages counter changed.<br />
</td>
</tr>
<tr class="separator:a47f3ece7ffd13e2f9b3fdeb0c6876643">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a1200d967d9adca2e3bdcd0f02512cc0a" class="memitem:a1200d967d9adca2e3bdcd0f02512cc0a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t(* </td>
<td class="memItemRight" data-valign="bottom">get_socket_fd )(DBusTransport *transport, DBusSocket *fd_p)</td>
</tr>
<tr class="memdesc:a1200d967d9adca2e3bdcd0f02512cc0a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Get socket file descriptor.<br />
</td>
</tr>
<tr class="separator:a1200d967d9adca2e3bdcd0f02512cc0a">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

The virtual table that must be implemented to create a new kind of transport.

Definition at line 43 of file dbus-transport-protected.h.

## Field Documentation

## ◆ connection_set

|  |
|----|
| dbus_bool_t(\* DBusTransportVTable::connection_set) (DBusTransport \*transport) |

Called when transport-\>connection has been filled in.

Definition at line 58 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_set_connection().

## ◆ disconnect

|                                                                      |
|----------------------------------------------------------------------|
| void(\* DBusTransportVTable::disconnect) (DBusTransport \*transport) |

Disconnect this transport.

Definition at line 55 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_disconnect().

## ◆ do_iteration

|  |
|----|
| void(\* DBusTransportVTable::do_iteration) (DBusTransport \*transport, unsigned int flags, int timeout_milliseconds) |

Called to do a single "iteration" (block on select/poll followed by reading or writing data).

Definition at line 61 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_do_iteration().

## ◆ finalize

|                                                                    |
|--------------------------------------------------------------------|
| void(\* DBusTransportVTable::finalize) (DBusTransport \*transport) |

The finalize method must free the transport.

Definition at line 45 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_unref().

## ◆ get_socket_fd

|  |
|----|
| dbus_bool_t(\* DBusTransportVTable::get_socket_fd) (DBusTransport \*transport, DBusSocket \*fd_p) |

Get socket file descriptor.

Definition at line 71 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_get_socket_fd().

## ◆ handle_watch

|  |
|----|
| dbus_bool_t(\* DBusTransportVTable::handle_watch) (DBusTransport \*transport, DBusWatch \*watch, unsigned int flags) |

The handle_watch method handles reading/writing data as indicated by the flags.

Definition at line 48 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_handle_watch().

## ◆ live_messages_changed

|  |
|----|
| void(\* DBusTransportVTable::live_messages_changed) (DBusTransport \*transport) |

Outstanding messages counter changed.

Definition at line 68 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_queue_messages().

The documentation for this struct was generated from the following file:

- dbus-transport-protected.h
