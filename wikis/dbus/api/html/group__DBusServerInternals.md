DBusServer implementation details

D-Bus secret internal implementation details

Implementation details of DBusServer. More...

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
<td class="memItemRight" data-valign="bottom">DBusServer</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Internals of DBusServer object. More...<br />
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
<tr id="r_gacec4220795b4d31e77547dcbcdecdb53" class="memitem:gacec4220795b4d31e77547dcbcdecdb53">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef dbus_bool_t(* </td>
<td class="memItemRight" data-valign="bottom">DBusWatchAddFunction) (DBusWatchList *list, DBusWatch *watch)</td>
</tr>
<tr class="memdesc:gacec4220795b4d31e77547dcbcdecdb53">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to be called in protected_change_watch() with refcount held.<br />
</td>
</tr>
<tr class="separator:gacec4220795b4d31e77547dcbcdecdb53">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3d3f6c25b94c857059e816dcb1f5629e" class="memitem:ga3d3f6c25b94c857059e816dcb1f5629e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef void(* </td>
<td class="memItemRight" data-valign="bottom">DBusWatchRemoveFunction) (DBusWatchList *list, DBusWatch *watch)</td>
</tr>
<tr class="memdesc:ga3d3f6c25b94c857059e816dcb1f5629e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to be called in protected_change_watch() with refcount held.<br />
</td>
</tr>
<tr class="separator:ga3d3f6c25b94c857059e816dcb1f5629e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabd9d6416ed2bb1abc881123249d91b9b" class="memitem:gabd9d6416ed2bb1abc881123249d91b9b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef void(* </td>
<td class="memItemRight" data-valign="bottom">DBusWatchToggleFunction) (DBusWatchList *list, DBusWatch *watch, dbus_bool_t enabled)</td>
</tr>
<tr class="memdesc:gabd9d6416ed2bb1abc881123249d91b9b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to be called in protected_change_watch() with refcount held.<br />
</td>
</tr>
<tr class="separator:gabd9d6416ed2bb1abc881123249d91b9b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaaae2977e5da448c2aa90dcf0b8fc6b2f" class="memitem:gaaae2977e5da448c2aa90dcf0b8fc6b2f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef dbus_bool_t(* </td>
<td class="memItemRight" data-valign="bottom">DBusTimeoutAddFunction) (DBusTimeoutList *list, DBusTimeout *timeout)</td>
</tr>
<tr class="memdesc:gaaae2977e5da448c2aa90dcf0b8fc6b2f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to be called in protected_change_timeout() with refcount held.<br />
</td>
</tr>
<tr class="separator:gaaae2977e5da448c2aa90dcf0b8fc6b2f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7d326b67ddbbf2fdb63cdc13f1cbb129" class="memitem:ga7d326b67ddbbf2fdb63cdc13f1cbb129">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef void(* </td>
<td class="memItemRight" data-valign="bottom">DBusTimeoutRemoveFunction) (DBusTimeoutList *list, DBusTimeout *timeout)</td>
</tr>
<tr class="memdesc:ga7d326b67ddbbf2fdb63cdc13f1cbb129">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to be called in protected_change_timeout() with refcount held.<br />
</td>
</tr>
<tr class="separator:ga7d326b67ddbbf2fdb63cdc13f1cbb129">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga775e02883191ec762f386d0953fd6308" class="memitem:ga775e02883191ec762f386d0953fd6308">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef void(* </td>
<td class="memItemRight" data-valign="bottom">DBusTimeoutToggleFunction) (DBusTimeoutList *list, DBusTimeout *timeout, dbus_bool_t enabled)</td>
</tr>
<tr class="memdesc:ga775e02883191ec762f386d0953fd6308">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to be called in protected_change_timeout() with refcount held.<br />
</td>
</tr>
<tr class="separator:ga775e02883191ec762f386d0953fd6308">
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
<tr id="r_gae9d6174bb5be7a2f422af5389fbb081f" class="memitem:gae9d6174bb5be7a2f422af5389fbb081f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_server_trace_ref (DBusServer *server, int old_refcount, int new_refcount, const char *why)</td>
</tr>
<tr class="separator:gae9d6174bb5be7a2f422af5389fbb081f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga831bfaa0f35aa0ccfcb95030bb343ef5" class="memitem:ga831bfaa0f35aa0ccfcb95030bb343ef5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_server_init_base (DBusServer *server, const DBusServerVTable *vtable, const DBusString *address, DBusError *error)</td>
</tr>
<tr class="memdesc:ga831bfaa0f35aa0ccfcb95030bb343ef5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initializes the members of the DBusServer base class.<br />
</td>
</tr>
<tr class="separator:ga831bfaa0f35aa0ccfcb95030bb343ef5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga93b5bca90e69122d5acbbeef2b4ca03e" class="memitem:ga93b5bca90e69122d5acbbeef2b4ca03e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_server_finalize_base (DBusServer *server)</td>
</tr>
<tr class="memdesc:ga93b5bca90e69122d5acbbeef2b4ca03e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Finalizes the members of the DBusServer base class.<br />
</td>
</tr>
<tr class="separator:ga93b5bca90e69122d5acbbeef2b4ca03e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0866e5b205b8a570c77c8ad787b665fd" class="memitem:ga0866e5b205b8a570c77c8ad787b665fd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_server_add_watch (DBusServer *server, DBusWatch *watch)</td>
</tr>
<tr class="memdesc:ga0866e5b205b8a570c77c8ad787b665fd">
<td class="mdescLeft"> </td>
<td class="mdescRight">Adds a watch for this server, chaining out to application-provided watch handlers.<br />
</td>
</tr>
<tr class="separator:ga0866e5b205b8a570c77c8ad787b665fd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga61cfdbfcc9316d4bae55f83b069f248c" class="memitem:ga61cfdbfcc9316d4bae55f83b069f248c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_server_remove_watch (DBusServer *server, DBusWatch *watch)</td>
</tr>
<tr class="memdesc:ga61cfdbfcc9316d4bae55f83b069f248c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Removes a watch previously added with _dbus_server_remove_watch().<br />
</td>
</tr>
<tr class="separator:ga61cfdbfcc9316d4bae55f83b069f248c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabdc55833c157737f5cb8b3662f8fc0ed" class="memitem:gabdc55833c157737f5cb8b3662f8fc0ed">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_server_toggle_all_watches (DBusServer *server, dbus_bool_t enabled)</td>
</tr>
<tr class="memdesc:gabdc55833c157737f5cb8b3662f8fc0ed">
<td class="mdescLeft"> </td>
<td class="mdescRight">Toggles all watch and notifies app via server's DBusWatchToggledFunction if available.<br />
</td>
</tr>
<tr class="separator:gabdc55833c157737f5cb8b3662f8fc0ed">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7e10a662386fb7f693e0d168161e395b" class="memitem:ga7e10a662386fb7f693e0d168161e395b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_server_add_timeout (DBusServer *server, DBusTimeout *timeout)</td>
</tr>
<tr class="memdesc:ga7e10a662386fb7f693e0d168161e395b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Adds a timeout for this server, chaining out to application-provided timeout handlers.<br />
</td>
</tr>
<tr class="separator:ga7e10a662386fb7f693e0d168161e395b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga69509697f091e354442cedb63886c20e" class="memitem:ga69509697f091e354442cedb63886c20e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_server_remove_timeout (DBusServer *server, DBusTimeout *timeout)</td>
</tr>
<tr class="memdesc:ga69509697f091e354442cedb63886c20e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Removes a timeout previously added with _dbus_server_add_timeout().<br />
</td>
</tr>
<tr class="separator:ga69509697f091e354442cedb63886c20e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga74d2714ce80a089d2607a6fc5763d819" class="memitem:ga74d2714ce80a089d2607a6fc5763d819">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_server_toggle_timeout (DBusServer *server, DBusTimeout *timeout, dbus_bool_t enabled)</td>
</tr>
<tr class="memdesc:ga74d2714ce80a089d2607a6fc5763d819">
<td class="mdescLeft"> </td>
<td class="mdescRight">Toggles a timeout and notifies app via server's DBusTimeoutToggledFunction if available.<br />
</td>
</tr>
<tr class="separator:ga74d2714ce80a089d2607a6fc5763d819">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga987e9bf42ab4e4cededa8e8f65c54e2e" class="memitem:ga987e9bf42ab4e4cededa8e8f65c54e2e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_server_ref_unlocked (DBusServer *server)</td>
</tr>
<tr class="memdesc:ga987e9bf42ab4e4cededa8e8f65c54e2e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Like dbus_server_ref() but does not acquire the lock (must already be held)<br />
</td>
</tr>
<tr class="separator:ga987e9bf42ab4e4cededa8e8f65c54e2e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6e1d0b379c98b0d59ebd19dc9b8a2dbe" class="memitem:ga6e1d0b379c98b0d59ebd19dc9b8a2dbe">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_server_unref_unlocked (DBusServer *server)</td>
</tr>
<tr class="memdesc:ga6e1d0b379c98b0d59ebd19dc9b8a2dbe">
<td class="mdescLeft"> </td>
<td class="mdescRight">Like dbus_server_unref() but does not acquire the lock (must already be held)<br />
</td>
</tr>
<tr class="separator:ga6e1d0b379c98b0d59ebd19dc9b8a2dbe">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Implementation details of DBusServer.

## Typedef Documentation

## ◆ DBusTimeoutAddFunction

|  |
|----|
| typedef dbus_bool_t(\* DBusTimeoutAddFunction) (DBusTimeoutList \*list, DBusTimeout \*timeout) |

Function to be called in protected_change_timeout() with refcount held.

Definition at line 338 of file dbus-server.c.

## ◆ DBusTimeoutRemoveFunction

|  |
|----|
| typedef void(\* DBusTimeoutRemoveFunction) (DBusTimeoutList \*list, DBusTimeout \*timeout) |

Function to be called in protected_change_timeout() with refcount held.

Definition at line 341 of file dbus-server.c.

## ◆ DBusTimeoutToggleFunction

|  |
|----|
| typedef void(\* DBusTimeoutToggleFunction) (DBusTimeoutList \*list, DBusTimeout \*timeout, dbus_bool_t enabled) |

Function to be called in protected_change_timeout() with refcount held.

Definition at line 344 of file dbus-server.c.

## ◆ DBusWatchAddFunction

|  |
|----|
| typedef dbus_bool_t(\* DBusWatchAddFunction) (DBusWatchList \*list, DBusWatch \*watch) |

Function to be called in protected_change_watch() with refcount held.

Definition at line 231 of file dbus-server.c.

## ◆ DBusWatchRemoveFunction

|  |
|----|
| typedef void(\* DBusWatchRemoveFunction) (DBusWatchList \*list, DBusWatch \*watch) |

Function to be called in protected_change_watch() with refcount held.

Definition at line 234 of file dbus-server.c.

## ◆ DBusWatchToggleFunction

|  |
|----|
| typedef void(\* DBusWatchToggleFunction) (DBusWatchList \*list, DBusWatch \*watch, dbus_bool_t enabled) |

Function to be called in protected_change_watch() with refcount held.

Definition at line 237 of file dbus-server.c.

## Function Documentation

## ◆ \_dbus_server_add_timeout()

|                                       |     |                 |            |
|---------------------------------------|-----|-----------------|------------|
| dbus_bool_t \_dbus_server_add_timeout | (   | DBusServer \*   | *server*,  |
|                                       |     | DBusTimeout \*  | *timeout*  |
|                                       | )   |                 |            |

Adds a timeout for this server, chaining out to application-provided timeout handlers.

The timeout should be repeatedly handled with dbus_timeout_handle() at its given interval until it is removed.

Parameters  
|         |                     |
|---------|---------------------|
| server  | the server.         |
| timeout | the timeout to add. |

Definition at line 406 of file dbus-server.c.

References \_dbus_timeout_list_add_timeout(), FALSE, and NULL.

## ◆ \_dbus_server_add_watch()

|                                     |     |                |           |
|-------------------------------------|-----|----------------|-----------|
| dbus_bool_t \_dbus_server_add_watch | (   | DBusServer \*  | *server*, |
|                                     |     | DBusWatch \*   | *watch*   |
|                                     | )   |                |           |

Adds a watch for this server, chaining out to application-provided watch handlers.

Parameters  
|        |                   |
|--------|-------------------|
| server | the server.       |
| watch  | the watch to add. |

Definition at line 297 of file dbus-server.c.

References \_dbus_watch_list_add_watch(), FALSE, and NULL.

Referenced by \_dbus_server_new_for_socket().

## ◆ \_dbus_server_finalize_base()

|                                  |     |                |          |     |     |
|----------------------------------|-----|----------------|----------|-----|-----|
| void \_dbus_server_finalize_base | (   | DBusServer \*  | *server* | )   |     |

Finalizes the members of the DBusServer base class.

Chained up to by subclass finalizers.

Parameters  
|        |             |
|--------|-------------|
| server | the server. |

Definition at line 202 of file dbus-server.c.

References \_dbus_assert, \_dbus_data_slot_list_free(), \_dbus_rmutex_free_at_location(), \_dbus_string_free(), \_dbus_timeout_list_free(), \_dbus_watch_list_free(), DBusServer::address, DBusServer::auth_mechanisms, dbus_free(), dbus_free_string_array(), dbus_server_set_new_connection_function(), DBusServer::disconnected, DBusServer::guid_hex, DBusServer::have_server_lock, DBusServer::mutex, NULL, DBusServer::slot_list, DBusServer::timeouts, and DBusServer::watches.

Referenced by \_dbus_server_new_for_socket().

## ◆ \_dbus_server_init_base()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_server_init_base | ( | DBusServer \*  | *server*, |
|  |  | const DBusServerVTable \*  | *vtable*, |
|  |  | const DBusString \*  | *address*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Initializes the members of the DBusServer base class.

Chained up to by subclass constructors.

Parameters  
|         |                                      |
|---------|--------------------------------------|
| server  | the server.                          |
| vtable  | the vtable for the subclass.         |
| address | the server's address                 |
| error   | location to store reason for failure |

<!-- -->

Returns  
TRUE on success.

Definition at line 113 of file dbus-server.c.

References \_dbus_assert, \_dbus_atomic_inc(), \_dbus_data_slot_list_init(), \_dbus_generate_uuid(), \_dbus_rmutex_free_at_location(), \_dbus_rmutex_new_at_location(), \_dbus_string_free(), \_dbus_string_init(), \_dbus_timeout_list_free(), \_dbus_timeout_list_new(), \_dbus_uuid_encode(), \_dbus_watch_list_free(), \_dbus_watch_list_new(), DBusServer::address, dbus_free(), FALSE, DBusServer::guid, DBusServer::guid_hex, DBusServer::mutex, NULL, DBusServer::published_address, DBusServer::refcount, DBusServer::slot_list, DBusServer::timeouts, TRUE, DBusServer::vtable, and DBusServer::watches.

Referenced by \_dbus_server_new_for_socket().

## ◆ \_dbus_server_ref_unlocked()

|                                 |     |                |          |     |     |
|---------------------------------|-----|----------------|----------|-----|-----|
| void \_dbus_server_ref_unlocked | (   | DBusServer \*  | *server* | )   |     |

Like dbus_server_ref() but does not acquire the lock (must already be held)

Parameters  
|        |             |
|--------|-------------|
| server | the server. |

Definition at line 457 of file dbus-server.c.

References \_dbus_assert, \_dbus_atomic_inc(), NULL, and DBusServer::refcount.

## ◆ \_dbus_server_remove_timeout()

|                                   |     |                 |            |
|-----------------------------------|-----|-----------------|------------|
| void \_dbus_server_remove_timeout | (   | DBusServer \*   | *server*,  |
|                                   |     | DBusTimeout \*  | *timeout*  |
|                                   | )   |                 |            |

Removes a timeout previously added with \_dbus_server_add_timeout().

Parameters  
|         |                        |
|---------|------------------------|
| server  | the server.            |
| timeout | the timeout to remove. |

Definition at line 421 of file dbus-server.c.

References \_dbus_timeout_list_remove_timeout(), FALSE, and NULL.

## ◆ \_dbus_server_remove_watch()

|                                 |     |                |           |
|---------------------------------|-----|----------------|-----------|
| void \_dbus_server_remove_watch | (   | DBusServer \*  | *server*, |
|                                 |     | DBusWatch \*   | *watch*   |
|                                 | )   |                |           |

Removes a watch previously added with \_dbus_server_remove_watch().

Parameters  
|        |                      |
|--------|----------------------|
| server | the server.          |
| watch  | the watch to remove. |

Definition at line 313 of file dbus-server.c.

References \_dbus_watch_list_remove_watch(), FALSE, and NULL.

## ◆ \_dbus_server_toggle_all_watches()

|                                       |     |                |            |
|---------------------------------------|-----|----------------|------------|
| void \_dbus_server_toggle_all_watches | (   | DBusServer \*  | *server*,  |
|                                       |     | dbus_bool_t    | *enabled*  |
|                                       | )   |                |            |

Toggles all watch and notifies app via server's DBusWatchToggledFunction if available.

Parameters  
|         |                              |
|---------|------------------------------|
| server  | the server.                  |
| enabled | whether to enable or disable |

Definition at line 331 of file dbus-server.c.

References \_dbus_watch_list_toggle_all_watches(), and DBusServer::watches.

## ◆ \_dbus_server_toggle_timeout()

|                                   |     |                 |            |
|-----------------------------------|-----|-----------------|------------|
| void \_dbus_server_toggle_timeout | (   | DBusServer \*   | *server*,  |
|                                   |     | DBusTimeout \*  | *timeout*, |
|                                   |     | dbus_bool_t     | *enabled*  |
|                                   | )   |                 |            |

Toggles a timeout and notifies app via server's DBusTimeoutToggledFunction if available.

It's an error to call this function on a timeout that was not previously added.

Parameters  
|         |                              |
|---------|------------------------------|
| server  | the server.                  |
| timeout | the timeout to toggle.       |
| enabled | whether to enable or disable |

Definition at line 440 of file dbus-server.c.

References \_dbus_timeout_list_toggle_timeout(), and NULL.

## ◆ \_dbus_server_trace_ref()

|                              |     |                |                 |
|------------------------------|-----|----------------|-----------------|
| void \_dbus_server_trace_ref | (   | DBusServer \*  | *server*,       |
|                              |     | int            | *old_refcount*, |
|                              |     | int            | *new_refcount*, |
|                              |     | const char \*  | *why*           |
|                              | )   |                |                 |

Definition at line 59 of file dbus-server.c.

## ◆ \_dbus_server_unref_unlocked()

|                                   |     |                |          |     |     |
|-----------------------------------|-----|----------------|----------|-----|-----|
| void \_dbus_server_unref_unlocked | (   | DBusServer \*  | *server* | )   |     |

Like dbus_server_unref() but does not acquire the lock (must already be held)

Parameters  
|        |             |
|--------|-------------|
| server | the server. |

Definition at line 476 of file dbus-server.c.

References \_dbus_assert, \_dbus_atomic_dec(), DBusServer::disconnected, DBusServerVTable::finalize, NULL, DBusServer::refcount, and DBusServer::vtable.
