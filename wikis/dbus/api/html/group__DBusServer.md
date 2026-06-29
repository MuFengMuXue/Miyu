DBusServer

D-Bus low-level public API

Server that listens for new connections. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="typedefs" class="groupheader"> Typedefs</h2></td>
</tr>
<tr id="r_ga39dc10dc2cbe727cf312c51b25b4341e" class="memitem:ga39dc10dc2cbe727cf312c51b25b4341e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusServer </td>
<td class="memItemRight" data-valign="bottom">DBusServer</td>
</tr>
<tr class="memdesc:ga39dc10dc2cbe727cf312c51b25b4341e">
<td class="mdescLeft"> </td>
<td class="mdescRight">An opaque object representing a server that listens for connections from other applications.<br />
</td>
</tr>
<tr class="separator:ga39dc10dc2cbe727cf312c51b25b4341e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf32eebe096bf1d0771cc3fd1d18718c3" class="memitem:gaf32eebe096bf1d0771cc3fd1d18718c3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef void(* </td>
<td class="memItemRight" data-valign="bottom">DBusNewConnectionFunction) (DBusServer *server, DBusConnection *new_connection, void *data)</td>
</tr>
<tr class="memdesc:gaf32eebe096bf1d0771cc3fd1d18718c3">
<td class="mdescLeft"> </td>
<td class="mdescRight">Called when a new connection to the server is available.<br />
</td>
</tr>
<tr class="separator:gaf32eebe096bf1d0771cc3fd1d18718c3">
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
<tr id="r_ga4c83cf9f2c186afa97decdc25ac163d8" class="memitem:ga4c83cf9f2c186afa97decdc25ac163d8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusServer * </td>
<td class="memItemRight" data-valign="bottom">dbus_server_listen (const char *address, DBusError *error)</td>
</tr>
<tr class="memdesc:ga4c83cf9f2c186afa97decdc25ac163d8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Listens for new connections on the given address.<br />
</td>
</tr>
<tr class="separator:ga4c83cf9f2c186afa97decdc25ac163d8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabe1c14264ef6bf3e5fe446ab9bf8b913" class="memitem:gabe1c14264ef6bf3e5fe446ab9bf8b913">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusServer * </td>
<td class="memItemRight" data-valign="bottom">dbus_server_ref (DBusServer *server)</td>
</tr>
<tr class="memdesc:gabe1c14264ef6bf3e5fe446ab9bf8b913">
<td class="mdescLeft"> </td>
<td class="mdescRight">Increments the reference count of a DBusServer.<br />
</td>
</tr>
<tr class="separator:gabe1c14264ef6bf3e5fe446ab9bf8b913">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga95d0b6cb9795b4919aa08f667807c555" class="memitem:ga95d0b6cb9795b4919aa08f667807c555">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_server_unref (DBusServer *server)</td>
</tr>
<tr class="memdesc:ga95d0b6cb9795b4919aa08f667807c555">
<td class="mdescLeft"> </td>
<td class="mdescRight">Decrements the reference count of a DBusServer.<br />
</td>
</tr>
<tr class="separator:ga95d0b6cb9795b4919aa08f667807c555">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gadbbfdcaebb7003777b5284da21cc76ae" class="memitem:gadbbfdcaebb7003777b5284da21cc76ae">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_server_disconnect_unlocked (DBusServer *server)</td>
</tr>
<tr class="separator:gadbbfdcaebb7003777b5284da21cc76ae">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1ff306fbaaa608306b0619ba5c0029a1" class="memitem:ga1ff306fbaaa608306b0619ba5c0029a1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_server_disconnect (DBusServer *server)</td>
</tr>
<tr class="memdesc:ga1ff306fbaaa608306b0619ba5c0029a1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Releases the server's address and stops listening for new clients.<br />
</td>
</tr>
<tr class="separator:ga1ff306fbaaa608306b0619ba5c0029a1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga93c36d8b42a3f2a4f3706a0c3609b3d1" class="memitem:ga93c36d8b42a3f2a4f3706a0c3609b3d1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_server_get_is_connected (DBusServer *server)</td>
</tr>
<tr class="memdesc:ga93c36d8b42a3f2a4f3706a0c3609b3d1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns TRUE if the server is still listening for new connections.<br />
</td>
</tr>
<tr class="separator:ga93c36d8b42a3f2a4f3706a0c3609b3d1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga63a133dc2786afed48c87127baa96927" class="memitem:ga63a133dc2786afed48c87127baa96927">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char * </td>
<td class="memItemRight" data-valign="bottom">dbus_server_get_address (DBusServer *server)</td>
</tr>
<tr class="memdesc:ga63a133dc2786afed48c87127baa96927">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns the address of the server, as a newly-allocated string which must be freed by the caller.<br />
</td>
</tr>
<tr class="separator:ga63a133dc2786afed48c87127baa96927">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3b2920b3c65836113781d9dd00d1e139" class="memitem:ga3b2920b3c65836113781d9dd00d1e139">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char * </td>
<td class="memItemRight" data-valign="bottom">dbus_server_get_id (DBusServer *server)</td>
</tr>
<tr class="memdesc:ga3b2920b3c65836113781d9dd00d1e139">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns the unique ID of the server, as a newly-allocated string which must be freed by the caller.<br />
</td>
</tr>
<tr class="separator:ga3b2920b3c65836113781d9dd00d1e139">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa14d9109e04adccffd9a40460c28c53b" class="memitem:gaa14d9109e04adccffd9a40460c28c53b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_server_set_new_connection_function (DBusServer *server, DBusNewConnectionFunction function, void *data, DBusFreeFunction free_data_function)</td>
</tr>
<tr class="memdesc:gaa14d9109e04adccffd9a40460c28c53b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets a function to be used for handling new connections.<br />
</td>
</tr>
<tr class="separator:gaa14d9109e04adccffd9a40460c28c53b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa5723810ea52e9f1815062fd91395892" class="memitem:gaa5723810ea52e9f1815062fd91395892">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_server_set_watch_functions (DBusServer *server, DBusAddWatchFunction add_function, DBusRemoveWatchFunction remove_function, DBusWatchToggledFunction toggled_function, void *data, DBusFreeFunction free_data_function)</td>
</tr>
<tr class="memdesc:gaa5723810ea52e9f1815062fd91395892">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the watch functions for the server.<br />
</td>
</tr>
<tr class="separator:gaa5723810ea52e9f1815062fd91395892">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gacafa42ffc063a7386db40a975c32d530" class="memitem:gacafa42ffc063a7386db40a975c32d530">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_server_set_timeout_functions (DBusServer *server, DBusAddTimeoutFunction add_function, DBusRemoveTimeoutFunction remove_function, DBusTimeoutToggledFunction toggled_function, void *data, DBusFreeFunction free_data_function)</td>
</tr>
<tr class="memdesc:gacafa42ffc063a7386db40a975c32d530">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the timeout functions for the server.<br />
</td>
</tr>
<tr class="separator:gacafa42ffc063a7386db40a975c32d530">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga309e5f1510c74c4b221d12d874d53341" class="memitem:ga309e5f1510c74c4b221d12d874d53341">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_server_set_auth_mechanisms (DBusServer *server, const char **mechanisms)</td>
</tr>
<tr class="memdesc:ga309e5f1510c74c4b221d12d874d53341">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the authentication mechanisms that this server offers to clients, as a NULL-terminated array of mechanism names.<br />
</td>
</tr>
<tr class="separator:ga309e5f1510c74c4b221d12d874d53341">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga05d280cd92ea5bb0d49bbe5b1fb1d5c2" class="memitem:ga05d280cd92ea5bb0d49bbe5b1fb1d5c2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_server_allocate_data_slot (dbus_int32_t *slot_p)</td>
</tr>
<tr class="memdesc:ga05d280cd92ea5bb0d49bbe5b1fb1d5c2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Allocates an integer ID to be used for storing application-specific data on any DBusServer.<br />
</td>
</tr>
<tr class="separator:ga05d280cd92ea5bb0d49bbe5b1fb1d5c2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac6ebc6105e32ab38ef0ac60dec6d5bc8" class="memitem:gac6ebc6105e32ab38ef0ac60dec6d5bc8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_server_free_data_slot (dbus_int32_t *slot_p)</td>
</tr>
<tr class="memdesc:gac6ebc6105e32ab38ef0ac60dec6d5bc8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Deallocates a global ID for server data slots.<br />
</td>
</tr>
<tr class="separator:gac6ebc6105e32ab38ef0ac60dec6d5bc8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab9ecb216dc9c40b0c7d370673fb9b269" class="memitem:gab9ecb216dc9c40b0c7d370673fb9b269">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_server_set_data (DBusServer *server, int slot, void *data, DBusFreeFunction free_data_func)</td>
</tr>
<tr class="memdesc:gab9ecb216dc9c40b0c7d370673fb9b269">
<td class="mdescLeft"> </td>
<td class="mdescRight">Stores a pointer on a DBusServer, along with an optional function to be used for freeing the data when the data is set again, or when the server is finalized.<br />
</td>
</tr>
<tr class="separator:gab9ecb216dc9c40b0c7d370673fb9b269">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac2bfa9f2e06c4347fefe537b233660d3" class="memitem:gac2bfa9f2e06c4347fefe537b233660d3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">dbus_server_get_data (DBusServer *server, int slot)</td>
</tr>
<tr class="memdesc:gac2bfa9f2e06c4347fefe537b233660d3">
<td class="mdescLeft"> </td>
<td class="mdescRight">Retrieves data previously set with dbus_server_set_data().<br />
</td>
</tr>
<tr class="separator:gac2bfa9f2e06c4347fefe537b233660d3">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Server that listens for new connections.

A DBusServer represents a server that other applications can connect to. Each connection from another application is represented by a DBusConnection.

## Typedef Documentation

## ◆ DBusNewConnectionFunction

|  |
|----|
| typedef void(\* DBusNewConnectionFunction) (DBusServer \*server, DBusConnection \*new_connection, void \*data) |

Called when a new connection to the server is available.

Must reference and save the new connection, or close the new connection. Set with dbus_server_set_new_connection_function().

Definition at line 50 of file dbus-server.h.

## ◆ DBusServer

|            |
|------------|
| DBusServer |

An opaque object representing a server that listens for connections from other applications.

Each time a connection is made, a new DBusConnection is created and made available via an application-provided DBusNewConnectionFunction. The DBusNewConnectionFunction is provided with dbus_server_set_new_connection_function().

Definition at line 45 of file dbus-server.h.

## Function Documentation

## ◆ \_dbus_server_disconnect_unlocked()

|                                        |     |                |          |     |     |
|----------------------------------------|-----|----------------|----------|-----|-----|
| void \_dbus_server_disconnect_unlocked | (   | DBusServer \*  | *server* | )   |     |

Definition at line 776 of file dbus-server.c.

## ◆ dbus_server_allocate_data_slot()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_server_allocate_data_slot | ( | dbus_int32_t \*  | *slot_p* | ) |  |

Allocates an integer ID to be used for storing application-specific data on any DBusServer.

The allocated ID may then be used with dbus_server_set_data() and dbus_server_get_data(). The slot must be initialized with -1. If a nonnegative slot is passed in, the refcount is incremented on that slot, rather than creating a new slot.

The allocated slot is global, i.e. all DBusServer objects will have a slot with the given integer ID reserved.

Parameters  
|        |                                                |
|--------|------------------------------------------------|
| slot_p | address of global variable storing the slot ID |

<!-- -->

Returns  
FALSE on no memory

Definition at line 1100 of file dbus-server.c.

References \_dbus_data_slot_allocator_alloc().

## ◆ dbus_server_disconnect()

|                                         |     |                |          |     |     |
|-----------------------------------------|-----|----------------|----------|-----|-----|
| DBUS_EXPORT void dbus_server_disconnect | (   | DBusServer \*  | *server* | )   |     |

Releases the server's address and stops listening for new clients.

If called more than once, only the first call has an effect. Does not modify the server's reference count.

Parameters  
|        |             |
|--------|-------------|
| server | the server. |

Definition at line 798 of file dbus-server.c.

References dbus_server_ref(), dbus_server_unref(), and NULL.

## ◆ dbus_server_free_data_slot()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT void dbus_server_free_data_slot | ( | dbus_int32_t \*  | *slot_p* | ) |  |

Deallocates a global ID for server data slots.

dbus_server_get_data() and dbus_server_set_data() may no longer be used with this slot. Existing data stored on existing DBusServer objects will be freed when the server is finalized, but may not be retrieved (and may only be replaced if someone else reallocates the slot).

Parameters  
|        |                                   |
|--------|-----------------------------------|
| slot_p | address of the slot to deallocate |

Definition at line 1118 of file dbus-server.c.

References \_dbus_data_slot_allocator_free().

## ◆ dbus_server_get_address()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT char \* dbus_server_get_address | ( | DBusServer \*  | *server* | ) |  |

Returns the address of the server, as a newly-allocated string which must be freed by the caller.

Parameters  
|        |            |
|--------|------------|
| server | the server |

<!-- -->

Returns  
the address or NULL if no memory

Definition at line 838 of file dbus-server.c.

References \_dbus_strdup(), address, and NULL.

## ◆ dbus_server_get_data()

|                                          |     |                |           |
|------------------------------------------|-----|----------------|-----------|
| DBUS_EXPORT void \* dbus_server_get_data | (   | DBusServer \*  | *server*, |
|                                          |     | int            | *slot*    |
|                                          | )   |                |           |

Retrieves data previously set with dbus_server_set_data().

The slot must still be allocated (must not have been freed).

Parameters  
|        |                           |
|--------|---------------------------|
| server | the server                |
| slot   | the slot to get data from |

<!-- -->

Returns  
the data, or NULL if not found

Definition at line 1179 of file dbus-server.c.

References \_dbus_data_slot_list_get(), NULL, and slot_list.

## ◆ dbus_server_get_id()

|                                        |     |                |          |     |     |
|----------------------------------------|-----|----------------|----------|-----|-----|
| DBUS_EXPORT char \* dbus_server_get_id | (   | DBusServer \*  | *server* | )   |     |

Returns the unique ID of the server, as a newly-allocated string which must be freed by the caller.

This ID is normally used by clients to tell when two DBusConnection would be equivalent (because the server address passed to dbus_connection_open() will have the same guid in the two cases). dbus_connection_open() can re-use an existing connection with the same ID instead of opening a new connection.

This is an ID unique to each DBusServer. Remember that a DBusServer represents only one mode of connecting, so e.g. a bus daemon can listen on multiple addresses which will mean it has multiple DBusServer each with their own ID.

The ID is not a UUID in the sense of RFC4122; the details are explained in the D-Bus specification.

Parameters  
|        |            |
|--------|------------|
| server | the server |

<!-- -->

Returns  
the id of the server or NULL if no memory

Definition at line 874 of file dbus-server.c.

References \_dbus_string_copy_data(), guid_hex, and NULL.

## ◆ dbus_server_get_is_connected()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_server_get_is_connected | ( | DBusServer \*  | *server* | ) |  |

Returns TRUE if the server is still listening for new connections.

Parameters  
|        |             |
|--------|-------------|
| server | the server. |

Definition at line 817 of file dbus-server.c.

References disconnected, FALSE, and NULL.

## ◆ dbus_server_listen()

|                                              |     |                |            |
|----------------------------------------------|-----|----------------|------------|
| DBUS_EXPORT DBusServer \* dbus_server_listen | (   | const char \*  | *address*, |
|                                              |     | DBusError \*   | *error*    |
|                                              | )   |                |            |

Listens for new connections on the given address.

If there are multiple semicolon-separated address entries in the address, tries each one and listens on the first one that works.

Returns NULL and sets error if listening fails for any reason. Otherwise returns a new DBusServer. dbus_server_set_new_connection_function(), dbus_server_set_watch_functions(), and dbus_server_set_timeout_functions() should be called immediately to render the server fully functional.

To free the server, applications must call first dbus_server_disconnect() and then dbus_server_unref().

Parameters  
|         |                                       |
|---------|---------------------------------------|
| address | the address of this server.           |
| error   | location to store reason for failure. |

<!-- -->

Returns  
a new DBusServer, or NULL on failure.

Definition at line 559 of file dbus-server.c.

References \_dbus_assert, \_dbus_assert_not_reached, \_DBUS_N_ELEMENTS, dbus_address_entries_free(), dbus_address_entry_get_method(), DBUS_ERROR_ADDRESS_IN_USE, DBUS_ERROR_BAD_ADDRESS, dbus_error_free(), DBUS_ERROR_INIT, dbus_error_is_set(), dbus_move_error(), dbus_parse_address(), dbus_set_error(), FALSE, NULL, and TRUE.

## ◆ dbus_server_ref()

|                                           |     |                |          |     |     |
|-------------------------------------------|-----|----------------|----------|-----|-----|
| DBUS_EXPORT DBusServer \* dbus_server_ref | (   | DBusServer \*  | *server* | )   |     |

Increments the reference count of a DBusServer.

Parameters  
|        |             |
|--------|-------------|
| server | the server. |

<!-- -->

Returns  
the server

Definition at line 703 of file dbus-server.c.

References \_dbus_atomic_dec(), \_dbus_atomic_inc(), NULL, and refcount.

Referenced by dbus_server_disconnect().

## ◆ dbus_server_set_auth_mechanisms()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_server_set_auth_mechanisms | ( | DBusServer \*  | *server*, |
|  |  | const char \*\*  | *mechanisms*  |
|  | ) |  |  |

Sets the authentication mechanisms that this server offers to clients, as a NULL-terminated array of mechanism names.

This function only affects connections created *after* it is called. Pass NULL instead of an array to use all available mechanisms (this is the default behavior).

The D-Bus specification describes some of the supported mechanisms.

Parameters  
|            |                                     |
|------------|-------------------------------------|
| server     | the server                          |
| mechanisms | NULL-terminated array of mechanisms |

<!-- -->

Returns  
FALSE if no memory

Definition at line 1053 of file dbus-server.c.

References \_dbus_dup_string_array(), auth_mechanisms, dbus_free_string_array(), FALSE, NULL, and TRUE.

## ◆ dbus_server_set_data()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_server_set_data | ( | DBusServer \*  | *server*, |
|  |  | int  | *slot*, |
|  |  | void \*  | *data*, |
|  |  | DBusFreeFunction  | *free_data_func*  |
|  | ) |  |  |

Stores a pointer on a DBusServer, along with an optional function to be used for freeing the data when the data is set again, or when the server is finalized.

The slot number must have been allocated with dbus_server_allocate_data_slot().

Parameters  
|                |                                 |
|----------------|---------------------------------|
| server         | the server                      |
| slot           | the slot number                 |
| data           | the data to store               |
| free_data_func | finalizer function for the data |

<!-- -->

Returns  
TRUE if there was enough memory to store the data

Definition at line 1139 of file dbus-server.c.

References \_dbus_data_slot_list_set(), FALSE, NULL, and slot_list.

## ◆ dbus_server_set_new_connection_function()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT void dbus_server_set_new_connection_function | ( | DBusServer \*  | *server*, |
|  |  | DBusNewConnectionFunction  | *function*, |
|  |  | void \*  | *data*, |
|  |  | DBusFreeFunction  | *free_data_function*  |
|  | ) |  |  |

Sets a function to be used for handling new connections.

The given function is passed each new connection as the connection is created. If the new connection function increments the connection's reference count, the connection will stay alive. Otherwise, the connection will be unreferenced and closed. The new connection function may also close the connection itself, which is considered good form if the connection is not wanted.

The connection here is private in the sense of dbus_connection_open_private(), so if the new connection function keeps a reference it must arrange for the connection to be closed. i.e. libdbus does not own this connection once the new connection function takes a reference.

Parameters  
|                    |                                             |
|--------------------|---------------------------------------------|
| server             | the server.                                 |
| function           | a function to handle new connections.       |
| data               | data to pass to the new connection handler. |
| free_data_function | function to free the data.                  |

Definition at line 909 of file dbus-server.c.

References new_connection_data, new_connection_free_data_function, new_connection_function, and NULL.

Referenced by \_dbus_server_finalize_base().

## ◆ dbus_server_set_timeout_functions()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_server_set_timeout_functions | ( | DBusServer \*  | *server*, |
|  |  | DBusAddTimeoutFunction  | *add_function*, |
|  |  | DBusRemoveTimeoutFunction  | *remove_function*, |
|  |  | DBusTimeoutToggledFunction  | *toggled_function*, |
|  |  | void \*  | *data*, |
|  |  | DBusFreeFunction  | *free_data_function*  |
|  | ) |  |  |

Sets the timeout functions for the server.

These functions are responsible for making the application's main loop aware of timeouts.

This function behaves exactly like dbus_connection_set_timeout_functions(); see the documentation for that routine.

Parameters  
|  |  |
|----|----|
| server | the server. |
| add_function | function to add a timeout. |
| remove_function | function to remove a timeout. |
| toggled_function | function to notify when the timeout is enabled/disabled |
| data | data to pass to add_function and remove_function. |
| free_data_function | function to be called to free the data. |

<!-- -->

Returns  
FALSE on failure (no memory)

Definition at line 1002 of file dbus-server.c.

References \_dbus_timeout_list_set_functions(), \_dbus_warn_check_failed(), FALSE, NULL, and timeouts.

## ◆ dbus_server_set_watch_functions()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_server_set_watch_functions | ( | DBusServer \*  | *server*, |
|  |  | DBusAddWatchFunction  | *add_function*, |
|  |  | DBusRemoveWatchFunction  | *remove_function*, |
|  |  | DBusWatchToggledFunction  | *toggled_function*, |
|  |  | void \*  | *data*, |
|  |  | DBusFreeFunction  | *free_data_function*  |
|  | ) |  |  |

Sets the watch functions for the server.

These functions are responsible for making the application's main loop aware of file descriptors that need to be monitored for events.

This function behaves exactly like dbus_connection_set_watch_functions(); see the documentation for that routine.

Parameters  
|                    |                                                       |
|--------------------|-------------------------------------------------------|
| server             | the server.                                           |
| add_function       | function to begin monitoring a new descriptor.        |
| remove_function    | function to stop monitoring a descriptor.             |
| toggled_function   | function to notify when the watch is enabled/disabled |
| data               | data to pass to add_function and remove_function.     |
| free_data_function | function to be called to free the data.               |

<!-- -->

Returns  
FALSE on failure (no memory)

Definition at line 949 of file dbus-server.c.

References \_dbus_warn_check_failed(), \_dbus_watch_list_set_functions(), FALSE, NULL, and watches.

## ◆ dbus_server_unref()

|                                    |     |                |          |     |     |
|------------------------------------|-----|----------------|----------|-----|-----|
| DBUS_EXPORT void dbus_server_unref | (   | DBusServer \*  | *server* | )   |     |

Decrements the reference count of a DBusServer.

Finalizes the server if the reference count reaches zero.

The server must be disconnected before the refcount reaches zero.

Parameters  
|        |             |
|--------|-------------|
| server | the server. |

Definition at line 735 of file dbus-server.c.

References \_dbus_assert, \_dbus_atomic_dec(), \_dbus_atomic_inc(), disconnected, DBusServerVTable::finalize, NULL, refcount, and vtable.

Referenced by dbus_server_disconnect().

## Variable Documentation

## ◆ \[\]

|  |
|----|
| DBusServerListenResult(\* { ... } ::func) (DBusAddressEntry \*entry, DBusServer \*\*server_p, DBusError \*error) |

Definition at line 526 of file dbus-server.c.
