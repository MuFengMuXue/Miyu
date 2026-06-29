DBusTimeout

D-Bus low-level public API

Object representing a timeout. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="functions" class="groupheader"> Functions</h2></td>
</tr>
<tr id="r_ga67ba21b6189438875c6007ee79da5e37" class="memitem:ga67ba21b6189438875c6007ee79da5e37">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_EXPORT int </td>
<td class="memItemRight" data-valign="bottom">dbus_timeout_get_interval (DBusTimeout *timeout)</td>
</tr>
<tr class="memdesc:ga67ba21b6189438875c6007ee79da5e37">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the timeout interval.<br />
</td>
</tr>
<tr class="separator:ga67ba21b6189438875c6007ee79da5e37">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7c561ec66daa2f53a274485f10c827c7" class="memitem:ga7c561ec66daa2f53a274485f10c827c7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_EXPORT void * </td>
<td class="memItemRight" data-valign="bottom">dbus_timeout_get_data (DBusTimeout *timeout)</td>
</tr>
<tr class="memdesc:ga7c561ec66daa2f53a274485f10c827c7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets data previously set with dbus_timeout_set_data() or NULL if none.<br />
</td>
</tr>
<tr class="separator:ga7c561ec66daa2f53a274485f10c827c7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga88712006f7772174504a0fba0a0ddd60" class="memitem:ga88712006f7772174504a0fba0a0ddd60">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_EXPORT void </td>
<td class="memItemRight" data-valign="bottom">dbus_timeout_set_data (DBusTimeout *timeout, void *data, DBusFreeFunction free_data_function)</td>
</tr>
<tr class="memdesc:ga88712006f7772174504a0fba0a0ddd60">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets data which can be retrieved with dbus_timeout_get_data().<br />
</td>
</tr>
<tr class="separator:ga88712006f7772174504a0fba0a0ddd60">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga038b67c8d3db2624a1e4a8bc45f25d12" class="memitem:ga038b67c8d3db2624a1e4a8bc45f25d12">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_EXPORT dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_timeout_handle (DBusTimeout *timeout)</td>
</tr>
<tr class="memdesc:ga038b67c8d3db2624a1e4a8bc45f25d12">
<td class="mdescLeft"> </td>
<td class="mdescRight">Calls the timeout handler for this timeout.<br />
</td>
</tr>
<tr class="separator:ga038b67c8d3db2624a1e4a8bc45f25d12">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga58954b2edb45ec1632529d35525ea45c" class="memitem:ga58954b2edb45ec1632529d35525ea45c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_EXPORT dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_timeout_get_enabled (DBusTimeout *timeout)</td>
</tr>
<tr class="memdesc:ga58954b2edb45ec1632529d35525ea45c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns whether a timeout is enabled or not.<br />
</td>
</tr>
<tr class="separator:ga58954b2edb45ec1632529d35525ea45c">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Object representing a timeout.

Types and functions related to DBusTimeout. A timeout represents a timeout that the main loop needs to monitor, as in Qt's QTimer or GLib's g_timeout_add().

Use dbus_connection_set_timeout_functions() or dbus_server_set_timeout_functions() to be notified when libdbus needs to add or remove timeouts.

## Function Documentation

## ◆ dbus_timeout_get_data()

|                               |     |                 |           |     |     |
|-------------------------------|-----|-----------------|-----------|-----|-----|
| void \* dbus_timeout_get_data | (   | DBusTimeout \*  | *timeout* | )   |     |

Gets data previously set with dbus_timeout_set_data() or NULL if none.

Parameters  
|         |                         |
|---------|-------------------------|
| timeout | the DBusTimeout object. |

<!-- -->

Returns  
previously-set data.

Definition at line 457 of file dbus-timeout.c.

References data.

## ◆ dbus_timeout_get_enabled()

|                                      |     |                 |           |     |     |
|--------------------------------------|-----|-----------------|-----------|-----|-----|
| dbus_bool_t dbus_timeout_get_enabled | (   | DBusTimeout \*  | *timeout* | )   |     |

Returns whether a timeout is enabled or not.

If not enabled, it should not be polled by the main loop.

Parameters  
|         |                        |
|---------|------------------------|
| timeout | the DBusTimeout object |

<!-- -->

Returns  
TRUE if the timeout is enabled

Definition at line 514 of file dbus-timeout.c.

References enabled.

## ◆ dbus_timeout_get_interval()

|                               |     |                 |           |     |     |
|-------------------------------|-----|-----------------|-----------|-----|-----|
| int dbus_timeout_get_interval | (   | DBusTimeout \*  | *timeout* | )   |     |

Gets the timeout interval.

The dbus_timeout_handle() should be called each time this interval elapses, starting after it elapses once.

The interval may change during the life of the timeout; if so, the timeout will be disabled and re-enabled (calling the "timeout toggled function") to notify you of the change.

Parameters  
|         |                         |
|---------|-------------------------|
| timeout | the DBusTimeout object. |

<!-- -->

Returns  
the interval in milliseconds.

Definition at line 444 of file dbus-timeout.c.

References interval.

Referenced by \_dbus_connection_block_pending_call().

## ◆ dbus_timeout_handle()

|                                 |     |                 |           |     |     |
|---------------------------------|-----|-----------------|-----------|-----|-----|
| dbus_bool_t dbus_timeout_handle | (   | DBusTimeout \*  | *timeout* | )   |     |

Calls the timeout handler for this timeout.

This function should be called when the timeout occurs.

If this function returns FALSE, then there wasn't enough memory to handle the timeout. Typically just letting the timeout fire again next time it naturally times out is an adequate response to that problem, but you could try to do more if you wanted.

Parameters  
|         |                         |
|---------|-------------------------|
| timeout | the DBusTimeout object. |

<!-- -->

Returns  
FALSE if there wasn't enough memory

Definition at line 500 of file dbus-timeout.c.

References handler, and handler_data.

## ◆ dbus_timeout_set_data()

|                            |     |                   |                       |
|----------------------------|-----|-------------------|-----------------------|
| void dbus_timeout_set_data | (   | DBusTimeout \*    | *timeout*,            |
|                            |     | void \*           | *data*,               |
|                            |     | DBusFreeFunction  | *free_data_function*  |
|                            | )   |                   |                       |

Sets data which can be retrieved with dbus_timeout_get_data().

Intended for use by the DBusAddTimeoutFunction and DBusRemoveTimeoutFunction to store their own data. For example with Qt you might store the QTimer for this timeout and with GLib you might store a g_timeout_add result id.

Parameters  
|                    |                                         |
|--------------------|-----------------------------------------|
| timeout            | the DBusTimeout object.                 |
| data               | the data.                               |
| free_data_function | function to be called to free the data. |

Definition at line 474 of file dbus-timeout.c.

References data, free_data_function, and NULL.

Referenced by \_dbus_timeout_unref().
