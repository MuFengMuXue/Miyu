DBusServer implementations for Launchd

D-Bus secret internal implementation details

Implementation details of DBusServer with Launchd support. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="functions" class="groupheader"> Functions</h2></td>
</tr>
<tr id="r_gaba3e206fb352c984fbfe808c7b176540" class="memitem:gaba3e206fb352c984fbfe808c7b176540">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusServer * </td>
<td class="memItemRight" data-valign="bottom">_dbus_server_new_for_launchd (const char *launchd_env_var, DBusError *error)</td>
</tr>
<tr class="memdesc:gaba3e206fb352c984fbfe808c7b176540">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new server from launchd.<br />
</td>
</tr>
<tr class="separator:gaba3e206fb352c984fbfe808c7b176540">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Implementation details of DBusServer with Launchd support.

## Function Documentation

## ◆ \_dbus_server_new_for_launchd()

|  |  |  |  |
|----|----|----|----|
| DBusServer \* \_dbus_server_new_for_launchd | ( | const char \*  | *launchd_env_var*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Creates a new server from launchd.

launchd has allocaed a socket for us. We now query launchd for the file descriptor of this socket and create a server on it. In addition we inherit launchd's environment which holds a variable containing the path to the socket. This is used to init the server's address which is passed to autolaunched services.

Parameters  
|  |  |
|----|----|
| launchd_env_var | the environment variable which holds the unix path to the socket |
| error | location to store reason for failure. |

<!-- -->

Returns  
the new server, or NULL on failure.

Definition at line 68 of file dbus-server-launchd.c.

References \_dbus_fd_set_close_on_exec(), \_dbus_getenv(), \_dbus_server_new_for_socket(), \_dbus_string_append(), \_dbus_string_free(), \_dbus_string_init(), \_dbus_warn(), DBUS_ERROR_BAD_ADDRESS, DBUS_ERROR_FAILED, DBUS_ERROR_IO_ERROR, DBUS_ERROR_LIMITS_EXCEEDED, DBUS_ERROR_NO_MEMORY, dbus_set_error(), dbus_setenv(), and NULL.

Referenced by \_dbus_server_listen_platform_specific().
