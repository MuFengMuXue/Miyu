DBusServer implementations for SOCKET

D-Bus secret internal implementation details

Implementation details of DBusServer on SOCKET. More...

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
<td class="memItemRight" data-valign="bottom">DBusServerSocket</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Implementation details of DBusServerSocket. More...<br />
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
<tr id="r_gace7aafbe2ae3cdbfbce3b01972dde0ce" class="memitem:gace7aafbe2ae3cdbfbce3b01972dde0ce">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusServerSocket </td>
<td class="memItemRight" data-valign="bottom">DBusServerSocket</td>
</tr>
<tr class="memdesc:gace7aafbe2ae3cdbfbce3b01972dde0ce">
<td class="mdescLeft"> </td>
<td class="mdescRight">Opaque object representing a Socket server implementation.<br />
</td>
</tr>
<tr class="separator:gace7aafbe2ae3cdbfbce3b01972dde0ce">
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
<tr id="r_ga7d4e0a7e1dc583a3f271313ec5e7c12f" class="memitem:ga7d4e0a7e1dc583a3f271313ec5e7c12f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusServer * </td>
<td class="memItemRight" data-valign="bottom">_dbus_server_new_for_socket (DBusSocket *fds, int n_fds, const DBusString *address, DBusNonceFile *noncefile, DBusError *error)</td>
</tr>
<tr class="memdesc:ga7d4e0a7e1dc583a3f271313ec5e7c12f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new server listening on the given file descriptor.<br />
</td>
</tr>
<tr class="separator:ga7d4e0a7e1dc583a3f271313ec5e7c12f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga79594da1dd98e77df1771f13eaab3605" class="memitem:ga79594da1dd98e77df1771f13eaab3605">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusServer * </td>
<td class="memItemRight" data-valign="bottom">_dbus_server_new_for_tcp_socket (const char *host, const char *bind, const char *port, const char *family, DBusError *error, dbus_bool_t use_nonce)</td>
</tr>
<tr class="memdesc:ga79594da1dd98e77df1771f13eaab3605">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new server listening on TCP.<br />
</td>
</tr>
<tr class="separator:ga79594da1dd98e77df1771f13eaab3605">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga90a89943c15760592e5ddce31bf0e021" class="memitem:ga90a89943c15760592e5ddce31bf0e021">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusServerListenResult </td>
<td class="memItemRight" data-valign="bottom">_dbus_server_listen_socket (DBusAddressEntry *entry, DBusServer **server_p, DBusError *error)</td>
</tr>
<tr class="memdesc:ga90a89943c15760592e5ddce31bf0e021">
<td class="mdescLeft"> </td>
<td class="mdescRight">Tries to interpret the address entry for various socket-related addresses (well, currently only tcp and nonce-tcp).<br />
</td>
</tr>
<tr class="separator:ga90a89943c15760592e5ddce31bf0e021">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa9518c980672f1b8dba8f5a981b93fd9" class="memitem:gaa9518c980672f1b8dba8f5a981b93fd9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_server_socket_own_filename (DBusServer *server, char *filename)</td>
</tr>
<tr class="memdesc:gaa9518c980672f1b8dba8f5a981b93fd9">
<td class="mdescLeft"> </td>
<td class="mdescRight">This is a bad hack since it's really unix domain socket specific.<br />
</td>
</tr>
<tr class="separator:gaa9518c980672f1b8dba8f5a981b93fd9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga767843b8ef08ac43583d06f953151780" class="memitem:ga767843b8ef08ac43583d06f953151780">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusServer * </td>
<td class="memItemRight" data-valign="bottom">_dbus_server_new_for_domain_socket (const char *path, dbus_bool_t abstract, DBusError *error)</td>
</tr>
<tr class="memdesc:ga767843b8ef08ac43583d06f953151780">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new server listening on the given Unix domain socket.<br />
</td>
</tr>
<tr class="separator:ga767843b8ef08ac43583d06f953151780">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa9023822a5916784072ce96e4ee1bfbb" class="memitem:gaa9023822a5916784072ce96e4ee1bfbb">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusServerListenResult </td>
<td class="memItemRight" data-valign="bottom">_dbus_server_listen_unix_socket (DBusAddressEntry *entry, DBusServer **server_p, DBusError *error)</td>
</tr>
<tr class="memdesc:gaa9023822a5916784072ce96e4ee1bfbb">
<td class="mdescLeft"> </td>
<td class="mdescRight">Tries to interpret the address entry for UNIX socket addresses.<br />
</td>
</tr>
<tr class="separator:gaa9023822a5916784072ce96e4ee1bfbb">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Implementation details of DBusServer on SOCKET.

## Typedef Documentation

## ◆ DBusServerSocket

|                                                  |
|--------------------------------------------------|
| typedef struct DBusServerSocket DBusServerSocket |

Opaque object representing a Socket server implementation.

Definition at line 46 of file dbus-server-socket.c.

## Function Documentation

## ◆ \_dbus_server_listen_socket()

|  |  |  |  |
|----|----|----|----|
| DBusServerListenResult \_dbus_server_listen_socket | ( | DBusAddressEntry \*  | *entry*, |
|  |  | DBusServer \*\*  | *server_p*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Tries to interpret the address entry for various socket-related addresses (well, currently only tcp and nonce-tcp).

Sets error if the result is not OK.

Parameters  
|          |                                                        |
|----------|--------------------------------------------------------|
| entry    | an address entry                                       |
| server_p | a new DBusServer, or NULL on failure.                  |
| error    | location to store rationale for failure on bad address |

<!-- -->

Returns  
the outcome

Definition at line 540 of file dbus-server-socket.c.

References \_dbus_server_new_for_tcp_socket(), dbus_address_entry_get_method(), dbus_address_entry_get_value(), FALSE, NULL, and TRUE.

## ◆ \_dbus_server_listen_unix_socket()

|  |  |  |  |
|----|----|----|----|
| DBusServerListenResult \_dbus_server_listen_unix_socket | ( | DBusAddressEntry \*  | *entry*, |
|  |  | DBusServer \*\*  | *server_p*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Tries to interpret the address entry for UNIX socket addresses.

Sets error if the result is not OK.

Parameters  
|          |                                                         |
|----------|---------------------------------------------------------|
| entry    | an address entry                                        |
| server_p | location to store a new DBusServer, or NULL on failure. |
| error    | location to store rationale for failure on bad address  |

<!-- -->

Returns  
the outcome

Definition at line 761 of file dbus-server-socket.c.

References \_dbus_concat_dir_and_file(), \_dbus_getenv(), \_dbus_server_new_for_domain_socket(), \_dbus_set_bad_address(), \_dbus_string_append(), \_dbus_string_free(), \_dbus_string_get_const_data(), \_dbus_string_init(), \_dbus_string_init_const(), dbus_address_entry_get_method(), dbus_address_entry_get_value(), DBUS_ERROR_NOT_SUPPORTED, dbus_set_error(), FALSE, NULL, and TRUE.

## ◆ \_dbus_server_new_for_domain_socket()

|  |  |  |  |
|----|----|----|----|
| DBusServer \* \_dbus_server_new_for_domain_socket | ( | const char \*  | *path*, |
|  |  | dbus_bool_t  | *abstract*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Creates a new server listening on the given Unix domain socket.

Parameters  
|          |                                       |
|----------|---------------------------------------|
| path     | the path for the domain socket.       |
| abstract | TRUE to use abstract socket namespace |
| error    | location to store reason for failure. |

<!-- -->

Returns  
the new server, or NULL on failure.

Definition at line 610 of file dbus-server-socket.c.

References \_dbus_address_append_escaped(), \_dbus_close_socket(), \_dbus_listen_unix_socket(), \_dbus_server_new_for_socket(), \_dbus_server_socket_own_filename(), \_dbus_strdup(), \_dbus_string_append(), \_dbus_string_free(), \_dbus_string_init(), \_dbus_string_init_const(), DBUS_ERROR_NO_MEMORY, dbus_free(), dbus_set_error(), and NULL.

Referenced by \_dbus_server_listen_unix_socket().

## ◆ \_dbus_server_new_for_socket()

|  |  |  |  |
|----|----|----|----|
| DBusServer \* \_dbus_server_new_for_socket | ( | DBusSocket \*  | *fds*, |
|  |  | int  | *n_fds*, |
|  |  | const DBusString \*  | *address*, |
|  |  | DBusNonceFile \*  | *noncefile*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Creates a new server listening on the given file descriptor.

The file descriptor should be nonblocking (use \_dbus_set_fd_nonblocking() to make it so). The file descriptor should be listening for connections, that is, listen() should have been successfully invoked on it. The server will use accept() to accept new client connections.

Parameters  
|           |                                                    |
|-----------|----------------------------------------------------|
| fds       | list of file descriptors.                          |
| n_fds     | number of file descriptors                         |
| address   | the server's address                               |
| noncefile | to be used for authentication (NULL if not needed) |
| error     | location to store reason for failure               |

<!-- -->

Returns  
the new server, or NULL on OOM or other error.

Definition at line 288 of file dbus-server-socket.c.

References \_dbus_server_add_watch(), \_dbus_server_finalize_base(), \_dbus_server_init_base(), \_dbus_watch_invalidate(), \_dbus_watch_new(), \_dbus_watch_unref(), base, dbus_error_is_set(), dbus_free(), dbus_new, dbus_new0, DBUS_WATCH_READABLE, fds, n_fds, noncefile, NULL, TRUE, and watch.

Referenced by \_dbus_server_listen_platform_specific(), \_dbus_server_new_for_domain_socket(), \_dbus_server_new_for_launchd(), and \_dbus_server_new_for_tcp_socket().

## ◆ \_dbus_server_new_for_tcp_socket()

|  |  |  |  |
|----|----|----|----|
| DBusServer \* \_dbus_server_new_for_tcp_socket | ( | const char \*  | *host*, |
|  |  | const char \*  | *bind*, |
|  |  | const char \*  | *port*, |
|  |  | const char \*  | *family*, |
|  |  | DBusError \*  | *error*, |
|  |  | dbus_bool_t  | *use_nonce*  |
|  | ) |  |  |

Creates a new server listening on TCP.

If host is NULL, it will default to localhost. If bind is NULL, it will default to the value for the host parameter, and if that is NULL, then localhost If bind is a hostname, it will be resolved and will listen on all returned addresses. If family is NULL, hostname resolution will try all address families, otherwise it can be ipv4 or ipv6 to restrict the addresses considered.

Parameters  
|  |  |
|----|----|
| host | the hostname to report for the listen address |
| bind | the hostname to listen on |
| port | the port to listen on or 0 to let the OS choose |
| family |  |
| error | location to store reason for failure. |
| use_nonce | whether to use a nonce for low-level authentication (nonce-tcp transport) or not (tcp transport) |

<!-- -->

Returns  
the new server, or NULL on failure.

Definition at line 420 of file dbus-server-socket.c.

References \_dbus_address_append_escaped(), \_dbus_close_socket(), \_dbus_listen_tcp_socket(), \_dbus_server_new_for_socket(), \_dbus_string_append(), \_dbus_string_free(), \_dbus_string_get_const_data(), \_dbus_string_init(), \_dbus_string_init_const(), DBUS_ERROR_NO_MEMORY, dbus_free(), dbus_set_error(), and NULL.

Referenced by \_dbus_server_listen_platform_specific(), and \_dbus_server_listen_socket().

## ◆ \_dbus_server_socket_own_filename()

|                                        |     |                |             |
|----------------------------------------|-----|----------------|-------------|
| void \_dbus_server_socket_own_filename | (   | DBusServer \*  | *server*,   |
|                                        |     | char \*        | *filename*  |
|                                        | )   |                |             |

This is a bad hack since it's really unix domain socket specific.

Also, the function weirdly adopts ownership of the passed-in string.

Parameters  
|          |                                  |
|----------|----------------------------------|
| server   | a socket server                  |
| filename | socket filename to report/delete |

Definition at line 593 of file dbus-server-socket.c.

References socket_name.

Referenced by \_dbus_server_new_for_domain_socket().
