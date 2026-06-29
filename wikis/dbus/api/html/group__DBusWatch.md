DBusWatch

D-Bus low-level public API

Object representing a file descriptor to be watched. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="functions" class="groupheader"> Functions</h2></td>
</tr>
<tr id="r_ga62d7e86fe386ed48fb90d443b3a2ce7a" class="memitem:ga62d7e86fe386ed48fb90d443b3a2ce7a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_EXPORT DBUS_DEPRECATED int </td>
<td class="memItemRight" data-valign="bottom">dbus_watch_get_fd (DBusWatch *watch)</td>
</tr>
<tr class="memdesc:ga62d7e86fe386ed48fb90d443b3a2ce7a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Deprecated former name of dbus_watch_get_unix_fd().<br />
</td>
</tr>
<tr class="separator:ga62d7e86fe386ed48fb90d443b3a2ce7a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga15df7f6120ead3e09bec8a70d3c43c0d" class="memitem:ga15df7f6120ead3e09bec8a70d3c43c0d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_EXPORT int </td>
<td class="memItemRight" data-valign="bottom">dbus_watch_get_unix_fd (DBusWatch *watch)</td>
</tr>
<tr class="memdesc:ga15df7f6120ead3e09bec8a70d3c43c0d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns a UNIX file descriptor to be watched, which may be a pipe, socket, or other type of descriptor.<br />
</td>
</tr>
<tr class="separator:ga15df7f6120ead3e09bec8a70d3c43c0d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga91308f393d41b31babda17c83833517f" class="memitem:ga91308f393d41b31babda17c83833517f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_EXPORT int </td>
<td class="memItemRight" data-valign="bottom">dbus_watch_get_socket (DBusWatch *watch)</td>
</tr>
<tr class="memdesc:ga91308f393d41b31babda17c83833517f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns a socket to be watched, on UNIX this will return -1 if our transport is not socket-based so dbus_watch_get_unix_fd() is preferred.<br />
</td>
</tr>
<tr class="separator:ga91308f393d41b31babda17c83833517f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf172a2b1d1f82333e67cec8d99c9204a" class="memitem:gaf172a2b1d1f82333e67cec8d99c9204a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_EXPORT unsigned int </td>
<td class="memItemRight" data-valign="bottom">dbus_watch_get_flags (DBusWatch *watch)</td>
</tr>
<tr class="memdesc:gaf172a2b1d1f82333e67cec8d99c9204a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets flags from DBusWatchFlags indicating what conditions should be monitored on the file descriptor.<br />
</td>
</tr>
<tr class="separator:gaf172a2b1d1f82333e67cec8d99c9204a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8dcdbd07f15a56207af4a36cb005da77" class="memitem:ga8dcdbd07f15a56207af4a36cb005da77">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_EXPORT void * </td>
<td class="memItemRight" data-valign="bottom">dbus_watch_get_data (DBusWatch *watch)</td>
</tr>
<tr class="memdesc:ga8dcdbd07f15a56207af4a36cb005da77">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets data previously set with dbus_watch_set_data() or NULL if none.<br />
</td>
</tr>
<tr class="separator:ga8dcdbd07f15a56207af4a36cb005da77">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5c75a65cf0680956cc0188d86a05cfae" class="memitem:ga5c75a65cf0680956cc0188d86a05cfae">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_EXPORT void </td>
<td class="memItemRight" data-valign="bottom">dbus_watch_set_data (DBusWatch *watch, void *data, DBusFreeFunction free_data_function)</td>
</tr>
<tr class="memdesc:ga5c75a65cf0680956cc0188d86a05cfae">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets data which can be retrieved with dbus_watch_get_data().<br />
</td>
</tr>
<tr class="separator:ga5c75a65cf0680956cc0188d86a05cfae">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac2acdb1794450ac01a43ec4c3e07ebf7" class="memitem:gac2acdb1794450ac01a43ec4c3e07ebf7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_EXPORT dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_watch_handle (DBusWatch *watch, unsigned int flags)</td>
</tr>
<tr class="memdesc:gac2acdb1794450ac01a43ec4c3e07ebf7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Called to notify the D-Bus library when a previously-added watch is ready for reading or writing, or has an exception such as a hangup.<br />
</td>
</tr>
<tr class="separator:gac2acdb1794450ac01a43ec4c3e07ebf7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae7a91e6d4d1bc187419c47c522e33a8f" class="memitem:gae7a91e6d4d1bc187419c47c522e33a8f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_EXPORT dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_watch_get_enabled (DBusWatch *watch)</td>
</tr>
<tr class="memdesc:gae7a91e6d4d1bc187419c47c522e33a8f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns whether a watch is enabled or not.<br />
</td>
</tr>
<tr class="separator:gae7a91e6d4d1bc187419c47c522e33a8f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3f4fb8107cc01941d91d4c4914dda115" class="memitem:ga3f4fb8107cc01941d91d4c4914dda115">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusSocket </td>
<td class="memItemRight" data-valign="bottom">_dbus_watch_get_socket (DBusWatch *watch)</td>
</tr>
<tr class="separator:ga3f4fb8107cc01941d91d4c4914dda115">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gafa9065410068af4275c1db0ff777c18a" class="memitem:gafa9065410068af4275c1db0ff777c18a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusPollable </td>
<td class="memItemRight" data-valign="bottom">_dbus_watch_get_pollable (DBusWatch *watch)</td>
</tr>
<tr class="separator:gafa9065410068af4275c1db0ff777c18a">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Object representing a file descriptor to be watched.

Types and functions related to DBusWatch. A watch represents a file descriptor that the main loop needs to monitor, as in Qt's QSocketNotifier or GLib's g_io_add_watch().

Use dbus_connection_set_watch_functions() or dbus_server_set_watch_functions() to be notified when libdbus needs to add or remove watches.

## Function Documentation

## ◆ \_dbus_watch_get_pollable()

|                                        |     |               |         |     |     |
|----------------------------------------|-----|---------------|---------|-----|-----|
| DBusPollable \_dbus_watch_get_pollable | (   | DBusWatch \*  | *watch* | )   |     |

Definition at line 623 of file dbus-watch.c.

## ◆ \_dbus_watch_get_socket()

|                                    |     |               |         |     |     |
|------------------------------------|-----|---------------|---------|-----|-----|
| DBusSocket \_dbus_watch_get_socket | (   | DBusWatch \*  | *watch* | )   |     |

Definition at line 607 of file dbus-watch.c.

## ◆ dbus_watch_get_data()

|                             |     |               |         |     |     |
|-----------------------------|-----|---------------|---------|-----|-----|
| void \* dbus_watch_get_data | (   | DBusWatch \*  | *watch* | )   |     |

Gets data previously set with dbus_watch_set_data() or NULL if none.

Parameters  
|       |                       |
|-------|-----------------------|
| watch | the DBusWatch object. |

<!-- -->

Returns  
previously-set data.

Definition at line 660 of file dbus-watch.c.

References data, and NULL.

## ◆ dbus_watch_get_enabled()

|                                    |     |               |         |     |     |
|------------------------------------|-----|---------------|---------|-----|-----|
| dbus_bool_t dbus_watch_get_enabled | (   | DBusWatch \*  | *watch* | )   |     |

Returns whether a watch is enabled or not.

If not enabled, it should not be polled by the main loop.

Parameters  
|       |                      |
|-------|----------------------|
| watch | the DBusWatch object |

<!-- -->

Returns  
TRUE if the watch is enabled

Definition at line 704 of file dbus-watch.c.

References enabled, FALSE, and NULL.

## ◆ dbus_watch_get_fd()

|                       |     |               |         |     |     |
|-----------------------|-----|---------------|---------|-----|-----|
| int dbus_watch_get_fd | (   | DBusWatch \*  | *watch* | )   |     |

Deprecated former name of dbus_watch_get_unix_fd().

Parameters  
|       |                       |
|-------|-----------------------|
| watch | the DBusWatch object. |

<!-- -->

Returns  
the file descriptor to watch.

Definition at line 545 of file dbus-watch.c.

References dbus_watch_get_unix_fd(), and NULL.

## ◆ dbus_watch_get_flags()

|                                   |     |               |         |     |     |
|-----------------------------------|-----|---------------|---------|-----|-----|
| unsigned int dbus_watch_get_flags | (   | DBusWatch \*  | *watch* | )   |     |

Gets flags from DBusWatchFlags indicating what conditions should be monitored on the file descriptor.

The flags returned will only contain DBUS_WATCH_READABLE and DBUS_WATCH_WRITABLE, never DBUS_WATCH_HANGUP or DBUS_WATCH_ERROR; all watches implicitly include a watch for hangups, errors, and other exceptional conditions.

Parameters  
|       |                       |
|-------|-----------------------|
| watch | the DBusWatch object. |

<!-- -->

Returns  
the conditions to watch.

Definition at line 644 of file dbus-watch.c.

References \_dbus_assert, flags, and NULL.

Referenced by \_dbus_watch_list_set_functions().

## ◆ dbus_watch_get_socket()

|                           |     |               |         |     |     |
|---------------------------|-----|---------------|---------|-----|-----|
| int dbus_watch_get_socket | (   | DBusWatch \*  | *watch* | )   |     |

Returns a socket to be watched, on UNIX this will return -1 if our transport is not socket-based so dbus_watch_get_unix_fd() is preferred.

On Windows, dbus_watch_get_unix_fd() returns -1 but this function returns a Winsock socket (assuming the transport is socket-based, as it always is for now).

Parameters  
|       |                       |
|-------|-----------------------|
| watch | the DBusWatch object. |

<!-- -->

Returns  
the socket to watch.

Definition at line 595 of file dbus-watch.c.

References fd, and NULL.

Referenced by \_dbus_transport_handle_watch(), and dbus_watch_get_unix_fd().

## ◆ dbus_watch_get_unix_fd()

|                            |     |               |         |     |     |
|----------------------------|-----|---------------|---------|-----|-----|
| int dbus_watch_get_unix_fd | (   | DBusWatch \*  | *watch* | )   |     |

Returns a UNIX file descriptor to be watched, which may be a pipe, socket, or other type of descriptor.

On UNIX this is preferred to dbus_watch_get_socket() since it works with more kinds of DBusWatch.

Always returns -1 on Windows. On Windows you use dbus_watch_get_socket() to get a Winsock socket to watch.

Parameters  
|       |                       |
|-------|-----------------------|
| watch | the DBusWatch object. |

<!-- -->

Returns  
the file descriptor to watch.

Definition at line 566 of file dbus-watch.c.

References dbus_watch_get_socket(), fd, and NULL.

Referenced by dbus_watch_get_fd().

## ◆ dbus_watch_handle()

|                               |     |               |          |
|-------------------------------|-----|---------------|----------|
| dbus_bool_t dbus_watch_handle | (   | DBusWatch \*  | *watch*, |
|                               |     | unsigned int  | *flags*  |
|                               | )   |               |          |

Called to notify the D-Bus library when a previously-added watch is ready for reading or writing, or has an exception such as a hangup.

If this function returns FALSE, then the file descriptor may still be ready for reading or writing, but more memory is needed in order to do the reading or writing. If you ignore the FALSE return, your application may spin in a busy loop on the file descriptor until memory becomes available, but nothing more catastrophic should happen.

dbus_watch_handle() cannot be called during the DBusAddWatchFunction, as the connection will not be ready to handle that watch yet.

It is not allowed to reference a DBusWatch after it has been passed to remove_function.

Parameters  
|       |                                                |
|-------|------------------------------------------------|
| watch | the DBusWatch object.                          |
| flags | the poll condition using DBusWatchFlags values |

<!-- -->

Returns  
FALSE if there wasn't enough memory

Definition at line 735 of file dbus-watch.c.

References \_dbus_warn_check_failed(), \_dbus_watch_sanitize_condition(), FALSE, fd, flags, handler, handler_data, NULL, and TRUE.

## ◆ dbus_watch_set_data()

|                          |     |                   |                       |
|--------------------------|-----|-------------------|-----------------------|
| void dbus_watch_set_data | (   | DBusWatch \*      | *watch*,              |
|                          |     | void \*           | *data*,               |
|                          |     | DBusFreeFunction  | *free_data_function*  |
|                          | )   |                   |                       |

Sets data which can be retrieved with dbus_watch_get_data().

Intended for use by the DBusAddWatchFunction and DBusRemoveWatchFunction to store their own data. For example with Qt you might store the QSocketNotifier for this watch and with GLib you might store a GSource.

Parameters  
|                    |                                         |
|--------------------|-----------------------------------------|
| watch              | the DBusWatch object.                   |
| data               | the data.                               |
| free_data_function | function to be called to free the data. |

Definition at line 679 of file dbus-watch.c.

References data, fd, free_data_function, and NULL.

Referenced by \_dbus_watch_unref().
