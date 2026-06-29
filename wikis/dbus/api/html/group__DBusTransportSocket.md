DBusTransport implementations for sockets

D-Bus secret internal implementation details

Implementation details of DBusTransport on sockets. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-structures" class="groupheader"> Data Structures</h2></td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusTransportSocket</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Implementation details of DBusTransportSocket. More...<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="typedefs" class="groupheader"> Typedefs</h2></td>
</tr>
<tr id="r_ga762346435786136b694d19a9bc5bce37" class="memitem:ga762346435786136b694d19a9bc5bce37">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusTransportSocket </td>
<td class="memItemRight" data-valign="bottom">DBusTransportSocket</td>
</tr>
<tr class="memdesc:ga762346435786136b694d19a9bc5bce37">
<td class="mdescLeft"> </td>
<td class="mdescRight">Opaque object representing a socket file descriptor transport.<br />
</td>
</tr>
<tr class="separator:ga762346435786136b694d19a9bc5bce37">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="functions" class="groupheader"> Functions</h2></td>
</tr>
<tr id="r_gac4861cb0529a0b30f981e2ad85ae0995" class="memitem:gac4861cb0529a0b30f981e2ad85ae0995">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusTransport * </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_new_for_socket (DBusSocket fd, const DBusString *server_guid, const DBusString *address)</td>
</tr>
<tr class="memdesc:gac4861cb0529a0b30f981e2ad85ae0995">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new transport for the given socket file descriptor.<br />
</td>
</tr>
<tr class="separator:gac4861cb0529a0b30f981e2ad85ae0995">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa04018619d0315f8db86abc4b72ee5c6" class="memitem:gaa04018619d0315f8db86abc4b72ee5c6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusTransport * </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_new_for_tcp_socket (const char *host, const char *port, const char *family, const char *noncefile, DBusError *error)</td>
</tr>
<tr class="memdesc:gaa04018619d0315f8db86abc4b72ee5c6">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new transport for the given hostname and port.<br />
</td>
</tr>
<tr class="separator:gaa04018619d0315f8db86abc4b72ee5c6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1bb28d9c6b0aa2b7efdf63f97116bb85" class="memitem:ga1bb28d9c6b0aa2b7efdf63f97116bb85">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusTransportOpenResult </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_open_socket (DBusAddressEntry *entry, DBusTransport **transport_p, DBusError *error)</td>
</tr>
<tr class="memdesc:ga1bb28d9c6b0aa2b7efdf63f97116bb85">
<td class="mdescLeft"> </td>
<td class="mdescRight">Opens a TCP socket transport.<br />
</td>
</tr>
<tr class="separator:ga1bb28d9c6b0aa2b7efdf63f97116bb85">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae6c21e64ede513857c2b18fc34574fc4" class="memitem:gae6c21e64ede513857c2b18fc34574fc4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusTransport * </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_new_for_domain_socket (const char *path, dbus_bool_t abstract, DBusError *error)</td>
</tr>
<tr class="memdesc:gae6c21e64ede513857c2b18fc34574fc4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new transport for the given Unix domain socket path.<br />
</td>
</tr>
<tr class="separator:gae6c21e64ede513857c2b18fc34574fc4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga68647e36ca70548a464bc8e5543bcf88" class="memitem:ga68647e36ca70548a464bc8e5543bcf88">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusTransportOpenResult </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_open_unix_socket (DBusAddressEntry *entry, DBusTransport **transport_p, DBusError *error)</td>
</tr>
<tr class="memdesc:ga68647e36ca70548a464bc8e5543bcf88">
<td class="mdescLeft"> </td>
<td class="mdescRight">Opens a UNIX socket transport.<br />
</td>
</tr>
<tr class="separator:ga68647e36ca70548a464bc8e5543bcf88">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Implementation details of DBusTransport on sockets.

## Typedef Documentation

## ◆ DBusTransportSocket

|                                                        |
|--------------------------------------------------------|
| typedef struct DBusTransportSocket DBusTransportSocket |

Opaque object representing a socket file descriptor transport.

Definition at line 49 of file dbus-transport-socket.c.

## Function Documentation

## ◆ \_dbus_transport_new_for_domain_socket()

|  |  |  |  |
|----|----|----|----|
| DBusTransport \* \_dbus_transport_new_for_domain_socket | ( | const char \*  | *path*, |
|  |  | dbus_bool_t  | *abstract*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Creates a new transport for the given Unix domain socket path.

This creates a client-side of a transport.

Parameters  
|          |                                         |
|----------|-----------------------------------------|
| path     | the path to the domain socket.          |
| abstract | TRUE to use abstract socket namespace   |
| error    | address where an error can be returned. |

<!-- -->

Returns  
a new transport, or NULL on failure.

Definition at line 1518 of file dbus-transport-socket.c.

References \_dbus_address_append_escaped(), \_dbus_close_socket(), \_dbus_connect_unix_socket(), \_dbus_string_append(), \_dbus_string_free(), \_dbus_string_init(), \_dbus_string_init_const(), \_dbus_transport_new_for_socket(), DBUS_ERROR_NO_MEMORY, dbus_set_error(), and NULL.

Referenced by \_dbus_transport_open_platform_specific(), and \_dbus_transport_open_unix_socket().

## ◆ \_dbus_transport_new_for_socket()

|  |  |  |  |
|----|----|----|----|
| DBusTransport \* \_dbus_transport_new_for_socket | ( | DBusSocket  | *fd*, |
|  |  | const DBusString \*  | *server_guid*, |
|  |  | const DBusString \*  | *address*  |
|  | ) |  |  |

Creates a new transport for the given socket file descriptor.

The file descriptor must be nonblocking (use \_dbus_set_fd_nonblocking() to make it so). This function is shared by various transports that boil down to a full duplex file descriptor.

Parameters  
|  |  |
|----|----|
| fd | the file descriptor. |
| server_guid | non-NULL if this transport is on the server side of a connection |
| address | the transport's address |

<!-- -->

Returns  
the new transport, or NULL if no memory.

Definition at line 1295 of file dbus-transport-socket.c.

References \_dbus_auth_set_unix_fd_possible(), \_dbus_socket_can_pass_unix_fd(), \_dbus_string_free(), \_dbus_string_init(), \_dbus_transport_init_base(), \_dbus_watch_invalidate(), \_dbus_watch_new(), \_dbus_watch_unref(), DBusTransport::auth, base, dbus_free(), dbus_new0, DBUS_WATCH_READABLE, DBUS_WATCH_WRITABLE, encoded_incoming, encoded_outgoing, FALSE, fd, max_bytes_read_per_iteration, max_bytes_written_per_iteration, message_bytes_written, NULL, read_watch, and write_watch.

Referenced by \_dbus_transport_new_for_domain_socket(), and \_dbus_transport_new_for_tcp_socket().

## ◆ \_dbus_transport_new_for_tcp_socket()

|  |  |  |  |
|----|----|----|----|
| DBusTransport \* \_dbus_transport_new_for_tcp_socket | ( | const char \*  | *host*, |
|  |  | const char \*  | *port*, |
|  |  | const char \*  | *family*, |
|  |  | const char \*  | *noncefile*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Creates a new transport for the given hostname and port.

If host is NULL, it will default to localhost

Parameters  
|           |                                       |
|-----------|---------------------------------------|
| host      | the host to connect to                |
| port      | the port to connect to                |
| family    | the address family to connect to      |
| noncefile | path to nonce file                    |
| error     | location to store reason for failure. |

<!-- -->

Returns  
a new transport, or NULL on failure.

Definition at line 1379 of file dbus-transport-socket.c.

References \_dbus_close_socket(), \_dbus_string_append(), \_dbus_string_free(), \_dbus_string_init(), \_dbus_transport_new_for_socket(), DBUS_ERROR_NO_MEMORY, dbus_set_error(), and NULL.

Referenced by \_dbus_transport_open_socket().

## ◆ \_dbus_transport_open_socket()

|  |  |  |  |
|----|----|----|----|
| DBusTransportOpenResult \_dbus_transport_open_socket | ( | DBusAddressEntry \*  | *entry*, |
|  |  | DBusTransport \*\*  | *transport_p*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Opens a TCP socket transport.

Parameters  
|             |                                                      |
|-------------|------------------------------------------------------|
| entry       | the address entry to try opening as a tcp transport. |
| transport_p | return location for the opened transport             |
| error       | error to be set                                      |

<!-- -->

Returns  
result of the attempt

Definition at line 1457 of file dbus-transport-socket.c.

References \_dbus_assert, \_dbus_set_bad_address(), \_dbus_transport_new_for_tcp_socket(), dbus_address_entry_get_method(), dbus_address_entry_get_value(), NULL, and TRUE.

## ◆ \_dbus_transport_open_unix_socket()

|  |  |  |  |
|----|----|----|----|
| DBusTransportOpenResult \_dbus_transport_open_unix_socket | ( | DBusAddressEntry \*  | *entry*, |
|  |  | DBusTransport \*\*  | *transport_p*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Opens a UNIX socket transport.

Parameters  
|             |                                                       |
|-------------|-------------------------------------------------------|
| entry       | the address entry to try opening as a unix transport. |
| transport_p | return location for the opened transport              |
| error       | error to be set                                       |

<!-- -->

Returns  
result of the attempt

Definition at line 1584 of file dbus-transport-socket.c.

References \_dbus_assert, \_dbus_set_bad_address(), \_dbus_transport_new_for_domain_socket(), dbus_address_entry_get_method(), dbus_address_entry_get_value(), FALSE, NULL, and TRUE.
