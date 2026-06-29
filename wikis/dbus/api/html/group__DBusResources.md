Resource limits related code

D-Bus secret internal implementation details

DBusCounter and other stuff related to resource limits. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="functions" class="groupheader"> Functions</h2></td>
</tr>
<tr id="r_ga25274abd582b862f9e1232c33c508eaa" class="memitem:ga25274abd582b862f9e1232c33c508eaa">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusCounter * </td>
<td class="memItemRight" data-valign="bottom">_dbus_counter_new (void)</td>
</tr>
<tr class="memdesc:ga25274abd582b862f9e1232c33c508eaa">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new DBusCounter.<br />
</td>
</tr>
<tr class="separator:ga25274abd582b862f9e1232c33c508eaa">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gadd6bebfca480eeae52a0dbce6a10f15d" class="memitem:gadd6bebfca480eeae52a0dbce6a10f15d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusCounter * </td>
<td class="memItemRight" data-valign="bottom">_dbus_counter_ref (DBusCounter *counter)</td>
</tr>
<tr class="memdesc:gadd6bebfca480eeae52a0dbce6a10f15d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Increments refcount of the counter.<br />
</td>
</tr>
<tr class="separator:gadd6bebfca480eeae52a0dbce6a10f15d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga48d9b53d1a395ab3c4f1846ca569ef3f" class="memitem:ga48d9b53d1a395ab3c4f1846ca569ef3f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_counter_unref (DBusCounter *counter)</td>
</tr>
<tr class="memdesc:ga48d9b53d1a395ab3c4f1846ca569ef3f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Decrements refcount of the counter and possibly finalizes the counter.<br />
</td>
</tr>
<tr class="separator:ga48d9b53d1a395ab3c4f1846ca569ef3f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae37410c196947675c2a222a7979e9dee" class="memitem:gae37410c196947675c2a222a7979e9dee">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_counter_adjust_size (DBusCounter *counter, long delta)</td>
</tr>
<tr class="memdesc:gae37410c196947675c2a222a7979e9dee">
<td class="mdescLeft"> </td>
<td class="mdescRight">Adjusts the value of the size counter by the given delta which may be positive or negative.<br />
</td>
</tr>
<tr class="separator:gae37410c196947675c2a222a7979e9dee">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab8c0e970e0c3b4696ba06723639d8239" class="memitem:gab8c0e970e0c3b4696ba06723639d8239">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_counter_notify (DBusCounter *counter)</td>
</tr>
<tr class="memdesc:gab8c0e970e0c3b4696ba06723639d8239">
<td class="mdescLeft"> </td>
<td class="mdescRight">Calls the notify function from _dbus_counter_set_notify(), if that function has been specified and the counter has crossed the guard value (in either direction) since the last call to this function.<br />
</td>
</tr>
<tr class="separator:gab8c0e970e0c3b4696ba06723639d8239">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7d9411d27b337289ab5648beb148cde6" class="memitem:ga7d9411d27b337289ab5648beb148cde6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_counter_adjust_unix_fd (DBusCounter *counter, long delta)</td>
</tr>
<tr class="memdesc:ga7d9411d27b337289ab5648beb148cde6">
<td class="mdescLeft"> </td>
<td class="mdescRight">Adjusts the value of the unix fd counter by the given delta which may be positive or negative.<br />
</td>
</tr>
<tr class="separator:ga7d9411d27b337289ab5648beb148cde6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga49de078fb626aff30f273933ad5c8b2a" class="memitem:ga49de078fb626aff30f273933ad5c8b2a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">long </td>
<td class="memItemRight" data-valign="bottom">_dbus_counter_get_size_value (DBusCounter *counter)</td>
</tr>
<tr class="memdesc:ga49de078fb626aff30f273933ad5c8b2a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the current value of the size counter.<br />
</td>
</tr>
<tr class="separator:ga49de078fb626aff30f273933ad5c8b2a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga25b2d12b9dc4d3525df2b8401f4ce56d" class="memitem:ga25b2d12b9dc4d3525df2b8401f4ce56d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">long </td>
<td class="memItemRight" data-valign="bottom">_dbus_counter_get_unix_fd_value (DBusCounter *counter)</td>
</tr>
<tr class="memdesc:ga25b2d12b9dc4d3525df2b8401f4ce56d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the current value of the unix fd counter.<br />
</td>
</tr>
<tr class="separator:ga25b2d12b9dc4d3525df2b8401f4ce56d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga240bddfe384b32a8703a328a638219e1" class="memitem:ga240bddfe384b32a8703a328a638219e1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_counter_set_notify (DBusCounter *counter, long size_guard_value, long unix_fd_guard_value, DBusCounterNotifyFunction function, void *user_data)</td>
</tr>
<tr class="memdesc:ga240bddfe384b32a8703a328a638219e1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the notify function for this counter; the notify function is called whenever the counter's values cross the guard values in either direction (moving up, or moving down).<br />
</td>
</tr>
<tr class="separator:ga240bddfe384b32a8703a328a638219e1">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

DBusCounter and other stuff related to resource limits.

Types and functions related to tracking resource limits, such as the maximum amount of memory/unix fds a connection can use for messages, etc.

## Function Documentation

## ◆ \_dbus_counter_adjust_size()

|                                 |     |                 |            |
|---------------------------------|-----|-----------------|------------|
| void \_dbus_counter_adjust_size | (   | DBusCounter \*  | *counter*, |
|                                 |     | long            | *delta*    |
|                                 | )   |                 |            |

Adjusts the value of the size counter by the given delta which may be positive or negative.

This function may be called with locks held. After calling it, when any relevant locks are no longer held you must call \_dbus_counter_notify().

Parameters  
|         |                                                  |
|---------|--------------------------------------------------|
| counter | the counter                                      |
| delta   | value to add to the size counter's current value |

Definition at line 169 of file dbus-resources.c.

References \_dbus_rmutex_lock(), \_dbus_rmutex_unlock(), DBusCounter::mutex, DBusCounter::notify_function, DBusCounter::notify_pending, DBusCounter::notify_size_guard_value, NULL, DBusCounter::size_value, and TRUE.

Referenced by \_dbus_message_add_counter_link(), and \_dbus_message_remove_counter().

## ◆ \_dbus_counter_adjust_unix_fd()

|                                    |     |                 |            |
|------------------------------------|-----|-----------------|------------|
| void \_dbus_counter_adjust_unix_fd | (   | DBusCounter \*  | *counter*, |
|                                    |     | long            | *delta*    |
|                                    | )   |                 |            |

Adjusts the value of the unix fd counter by the given delta which may be positive or negative.

This function may be called with locks held. After calling it, when any relevant locks are no longer held you must call \_dbus_counter_notify().

Parameters  
|         |                                                      |
|---------|------------------------------------------------------|
| counter | the counter                                          |
| delta   | value to add to the unix fds counter's current value |

Definition at line 238 of file dbus-resources.c.

References \_dbus_rmutex_lock(), \_dbus_rmutex_unlock(), DBusCounter::mutex, DBusCounter::notify_function, DBusCounter::notify_pending, DBusCounter::notify_unix_fd_guard_value, NULL, TRUE, and DBusCounter::unix_fd_value.

Referenced by \_dbus_message_add_counter_link(), and \_dbus_message_remove_counter().

## ◆ \_dbus_counter_get_size_value()

|                                    |     |                 |           |     |     |
|------------------------------------|-----|-----------------|-----------|-----|-----|
| long \_dbus_counter_get_size_value | (   | DBusCounter \*  | *counter* | )   |     |

Gets the current value of the size counter.

Parameters  
|         |             |
|---------|-------------|
| counter | the counter |

<!-- -->

Returns  
its current size value

Definition at line 276 of file dbus-resources.c.

References \_dbus_rmutex_lock(), \_dbus_rmutex_unlock(), DBusCounter::mutex, and DBusCounter::size_value.

Referenced by \_dbus_transport_get_dispatch_status(), and dbus_connection_get_outgoing_size().

## ◆ \_dbus_counter_get_unix_fd_value()

|                                       |     |                 |           |     |     |
|---------------------------------------|-----|-----------------|-----------|-----|-----|
| long \_dbus_counter_get_unix_fd_value | (   | DBusCounter \*  | *counter* | )   |     |

Gets the current value of the unix fd counter.

Parameters  
|         |             |
|---------|-------------|
| counter | the counter |

<!-- -->

Returns  
its current unix fd value

Definition at line 292 of file dbus-resources.c.

References \_dbus_rmutex_lock(), \_dbus_rmutex_unlock(), DBusCounter::mutex, and DBusCounter::unix_fd_value.

Referenced by \_dbus_transport_get_dispatch_status(), and dbus_connection_get_outgoing_unix_fds().

## ◆ \_dbus_counter_new()

|                                   |     |       |     |     |     |
|-----------------------------------|-----|-------|-----|-----|-----|
| DBusCounter \* \_dbus_counter_new | (   | void  |     | )   |     |

Creates a new DBusCounter.

DBusCounter is used to count usage of some resource such as memory.

Returns  
new counter or NULL on failure

Definition at line 91 of file dbus-resources.c.

References \_dbus_rmutex_new_at_location(), dbus_free(), dbus_new0, DBusCounter::mutex, NULL, and DBusCounter::refcount.

Referenced by \_dbus_connection_new_for_transport(), and \_dbus_transport_init_base().

## ◆ \_dbus_counter_notify()

|                            |     |                 |           |     |     |
|----------------------------|-----|-----------------|-----------|-----|-----|
| void \_dbus_counter_notify | (   | DBusCounter \*  | *counter* | )   |     |

Calls the notify function from \_dbus_counter_set_notify(), if that function has been specified and the counter has crossed the guard value (in either direction) since the last call to this function.

This function must not be called with locks held, since it can call out to user code.

Definition at line 209 of file dbus-resources.c.

References \_dbus_rmutex_lock(), \_dbus_rmutex_unlock(), FALSE, DBusCounter::mutex, DBusCounter::notify_data, DBusCounter::notify_function, DBusCounter::notify_pending, and NULL.

Referenced by \_dbus_message_remove_counter().

## ◆ \_dbus_counter_ref()

|                                   |     |                 |           |     |     |
|-----------------------------------|-----|-----------------|-----------|-----|-----|
| DBusCounter \* \_dbus_counter_ref | (   | DBusCounter \*  | *counter* | )   |     |

Increments refcount of the counter.

Parameters  
|         |             |
|---------|-------------|
| counter | the counter |

<!-- -->

Returns  
the counter

Definition at line 118 of file dbus-resources.c.

References \_dbus_assert, \_dbus_rmutex_lock(), \_dbus_rmutex_unlock(), DBusCounter::mutex, and DBusCounter::refcount.

Referenced by \_dbus_message_add_counter().

## ◆ \_dbus_counter_set_notify()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_counter_set_notify | ( | DBusCounter \*  | *counter*, |
|  |  | long  | *size_guard_value*, |
|  |  | long  | *unix_fd_guard_value*, |
|  |  | DBusCounterNotifyFunction  | *function*, |
|  |  | void \*  | *user_data*  |
|  | ) |  |  |

Sets the notify function for this counter; the notify function is called whenever the counter's values cross the guard values in either direction (moving up, or moving down).

Parameters  
|  |  |
|----|----|
| counter | the counter |
| size_guard_value | the value we're notified if the size counter crosses |
| unix_fd_guard_value | the value we're notified if the unix fd counter crosses |
| function | function to call in order to notify |
| user_data | data to pass to the function |

Definition at line 313 of file dbus-resources.c.

References \_dbus_rmutex_lock(), \_dbus_rmutex_unlock(), FALSE, DBusCounter::mutex, DBusCounter::notify_data, DBusCounter::notify_function, DBusCounter::notify_pending, DBusCounter::notify_size_guard_value, and DBusCounter::notify_unix_fd_guard_value.

Referenced by \_dbus_transport_finalize_base(), \_dbus_transport_init_base(), \_dbus_transport_set_max_received_size(), and \_dbus_transport_set_max_received_unix_fds().

## ◆ \_dbus_counter_unref()

|                           |     |                 |           |     |     |
|---------------------------|-----|-----------------|-----------|-----|-----|
| void \_dbus_counter_unref | (   | DBusCounter \*  | *counter* | )   |     |

Decrements refcount of the counter and possibly finalizes the counter.

Parameters  
|         |             |
|---------|-------------|
| counter | the counter |

Definition at line 138 of file dbus-resources.c.

References \_dbus_assert, \_dbus_rmutex_free_at_location(), \_dbus_rmutex_lock(), \_dbus_rmutex_unlock(), dbus_free(), FALSE, DBusCounter::mutex, and DBusCounter::refcount.

Referenced by \_dbus_connection_new_for_transport(), \_dbus_message_remove_counter(), \_dbus_transport_finalize_base(), \_dbus_transport_init_base(), and dbus_connection_free_preallocated_send().
