Memory allocation implementation details

D-Bus secret internal implementation details

internals of dbus_malloc() etc. More...

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
<td class="memItemRight" data-valign="bottom">ShutdownClosure</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">This struct represents a function to be called on shutdown. More...<br />
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
<tr id="r_ga719c469fe616ee7148e826e6ebf3c3e4" class="memitem:ga719c469fe616ee7148e826e6ebf3c3e4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct ShutdownClosure </td>
<td class="memItemRight" data-valign="bottom">ShutdownClosure</td>
</tr>
<tr class="memdesc:ga719c469fe616ee7148e826e6ebf3c3e4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Represents a function to be called on shutdown.<br />
</td>
</tr>
<tr class="separator:ga719c469fe616ee7148e826e6ebf3c3e4">
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
<tr id="r_ga8dc6d5dd0a0e7901ab793da7403ee734" class="memitem:ga8dc6d5dd0a0e7901ab793da7403ee734">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_register_shutdown_func (DBusShutdownFunction func, void *data)</td>
</tr>
<tr class="memdesc:ga8dc6d5dd0a0e7901ab793da7403ee734">
<td class="mdescLeft"> </td>
<td class="mdescRight">Register a cleanup function to be called exactly once the next time dbus_shutdown() is called.<br />
</td>
</tr>
<tr class="separator:ga8dc6d5dd0a0e7901ab793da7403ee734">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gade7c064966b2e3f9004099337b40b0f4" class="memitem:gade7c064966b2e3f9004099337b40b0f4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_register_shutdown_func_unlocked (DBusShutdownFunction func, void *data)</td>
</tr>
<tr class="separator:gade7c064966b2e3f9004099337b40b0f4">
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
<td colspan="2"><h2 id="variables" class="groupheader"> Variables</h2></td>
</tr>
<tr id="r_ga7c224d82013e2bdc181c1d85dcb6f295" class="memitem:ga7c224d82013e2bdc181c1d85dcb6f295">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_current_generation = 1</td>
</tr>
<tr class="memdesc:ga7c224d82013e2bdc181c1d85dcb6f295">
<td class="mdescLeft"> </td>
<td class="mdescRight">_dbus_current_generation is used to track each time that dbus_shutdown() is called, so we can reinit things after it's been called.<br />
</td>
</tr>
<tr class="separator:ga7c224d82013e2bdc181c1d85dcb6f295">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

internals of dbus_malloc() etc.

Implementation details related to allocating and releasing blocks of memory.

## Typedef Documentation

## ◆ ShutdownClosure

|                                                |
|------------------------------------------------|
| typedef struct ShutdownClosure ShutdownClosure |

Represents a function to be called on shutdown.

Definition at line 795 of file dbus-memory.c.

## Function Documentation

## ◆ \_dbus_register_shutdown_func()

|                                           |     |                       |         |
|-------------------------------------------|-----|-----------------------|---------|
| dbus_bool_t \_dbus_register_shutdown_func | (   | DBusShutdownFunction  | *func*, |
|                                           |     | void \*               | *data*  |
|                                           | )   |                       |         |

Register a cleanup function to be called exactly once the next time dbus_shutdown() is called.

Parameters  
|      |                              |
|------|------------------------------|
| func | the function                 |
| data | data to pass to the function |

<!-- -->

Returns  
FALSE on not enough memory

Definition at line 819 of file dbus-memory.c.

References \_DBUS_LOCK, \_DBUS_UNLOCK, and FALSE.

## ◆ \_dbus_register_shutdown_func_unlocked()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_register_shutdown_func_unlocked | ( | DBusShutdownFunction  | *func*, |
|  |  | void \*  | *data*  |
|  | ) |  |  |

Definition at line 833 of file dbus-memory.c.

## Variable Documentation

## ◆ \_dbus_current_generation

|                                   |
|-----------------------------------|
| int \_dbus_current_generation = 1 |

\_dbus_current_generation is used to track each time that dbus_shutdown() is called, so we can reinit things after it's been called.

It is simply incremented each time we shut down.

Definition at line 790 of file dbus-memory.c.

Referenced by \_dbus_connection_close_possibly_shared(), \_dbus_connection_new_for_transport(), \_dbus_connection_ref_unlocked(), \_dbus_get_local_machine_uuid_encoded(), dbus_connection_close(), dbus_connection_ref(), dbus_connection_unref(), dbus_message_ref(), dbus_message_unref(), dbus_shutdown(), and dbus_threads_init().
