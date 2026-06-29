DBusWatch implementation details

D-Bus secret internal implementation details

implementation details for DBusWatch More...

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
<td class="memItemRight" data-valign="bottom">DBusWatch</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Implementation of DBusWatch. More...<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusWatchList</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">DBusWatchList implementation details. More...<br />
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
<td colspan="2"><h2 id="macros" class="groupheader"> Macros</h2></td>
</tr>
<tr id="r_ga524db7211d877eb100dbb48ab469f2af" class="memitem:ga524db7211d877eb100dbb48ab469f2af">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_DBUS_WATCH_NVAL   (1&lt;&lt;4)</td>
</tr>
<tr class="separator:ga524db7211d877eb100dbb48ab469f2af">
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
<tr id="r_gafc9f312d7d92039a381a753b7e024391" class="memitem:gafc9f312d7d92039a381a753b7e024391">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusWatchList </td>
<td class="memItemRight" data-valign="bottom">DBusWatchList</td>
</tr>
<tr class="memdesc:gafc9f312d7d92039a381a753b7e024391">
<td class="mdescLeft"> </td>
<td class="mdescRight">Opaque data type representing a list of watches and a set of DBusAddWatchFunction/DBusRemoveWatchFunction.<br />
</td>
</tr>
<tr class="separator:gafc9f312d7d92039a381a753b7e024391">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gacde57228cb3e9e6bb3ceb665fc121e33" class="memitem:gacde57228cb3e9e6bb3ceb665fc121e33">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef dbus_bool_t(* </td>
<td class="memItemRight" data-valign="bottom">DBusWatchHandler) (DBusWatch *watch, unsigned int flags, void *data)</td>
</tr>
<tr class="memdesc:gacde57228cb3e9e6bb3ceb665fc121e33">
<td class="mdescLeft"> </td>
<td class="mdescRight">function to run when the watch is handled<br />
</td>
</tr>
<tr class="separator:gacde57228cb3e9e6bb3ceb665fc121e33">
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
<tr id="r_ga7dcad11a2e5588c0a36e43a599bc9f4d" class="memitem:ga7dcad11a2e5588c0a36e43a599bc9f4d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_watch_get_enabled (DBusWatch *watch)</td>
</tr>
<tr class="separator:ga7dcad11a2e5588c0a36e43a599bc9f4d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga71767cd6825b87386b955c2fae95ab76" class="memitem:ga71767cd6825b87386b955c2fae95ab76">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_watch_get_oom_last_time (DBusWatch *watch)</td>
</tr>
<tr class="separator:ga71767cd6825b87386b955c2fae95ab76">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga662f1a85094dcabde932f623afff8a75" class="memitem:ga662f1a85094dcabde932f623afff8a75">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_watch_set_oom_last_time (DBusWatch *watch, dbus_bool_t oom)</td>
</tr>
<tr class="separator:ga662f1a85094dcabde932f623afff8a75">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac4ff38c7e9e6cc21f79aa2bc4fa67d3d" class="memitem:gac4ff38c7e9e6cc21f79aa2bc4fa67d3d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusWatch * </td>
<td class="memItemRight" data-valign="bottom">_dbus_watch_new (DBusPollable fd, unsigned int flags, dbus_bool_t enabled, DBusWatchHandler handler, void *data, DBusFreeFunction free_data_function)</td>
</tr>
<tr class="memdesc:gac4ff38c7e9e6cc21f79aa2bc4fa67d3d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new DBusWatch.<br />
</td>
</tr>
<tr class="separator:gac4ff38c7e9e6cc21f79aa2bc4fa67d3d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaceda03acdda228e66a5cfe96126a919b" class="memitem:gaceda03acdda228e66a5cfe96126a919b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusWatch * </td>
<td class="memItemRight" data-valign="bottom">_dbus_watch_ref (DBusWatch *watch)</td>
</tr>
<tr class="memdesc:gaceda03acdda228e66a5cfe96126a919b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Increments the reference count of a DBusWatch object.<br />
</td>
</tr>
<tr class="separator:gaceda03acdda228e66a5cfe96126a919b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gadd0e6a682b67e470bdb77f2c8da5baea" class="memitem:gadd0e6a682b67e470bdb77f2c8da5baea">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_watch_unref (DBusWatch *watch)</td>
</tr>
<tr class="memdesc:gadd0e6a682b67e470bdb77f2c8da5baea">
<td class="mdescLeft"> </td>
<td class="mdescRight">Decrements the reference count of a DBusWatch object and finalizes the object if the count reaches zero.<br />
</td>
</tr>
<tr class="separator:gadd0e6a682b67e470bdb77f2c8da5baea">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaed53379a4f88fdb7025f0c6d0bcb76f5" class="memitem:gaed53379a4f88fdb7025f0c6d0bcb76f5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_watch_invalidate (DBusWatch *watch)</td>
</tr>
<tr class="memdesc:gaed53379a4f88fdb7025f0c6d0bcb76f5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Clears the file descriptor from a now-invalid watch object so that no one tries to use it.<br />
</td>
</tr>
<tr class="separator:gaed53379a4f88fdb7025f0c6d0bcb76f5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab8f49926fe9ee56cb4ae7c1c8071cca3" class="memitem:gab8f49926fe9ee56cb4ae7c1c8071cca3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_watch_sanitize_condition (DBusWatch *watch, unsigned int *condition)</td>
</tr>
<tr class="memdesc:gab8f49926fe9ee56cb4ae7c1c8071cca3">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sanitizes the given condition so that it only contains flags that the DBusWatch requested.<br />
</td>
</tr>
<tr class="separator:gab8f49926fe9ee56cb4ae7c1c8071cca3">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga19c761997dbbf753c826389c7950d3eb" class="memitem:ga19c761997dbbf753c826389c7950d3eb">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusWatchList * </td>
<td class="memItemRight" data-valign="bottom">_dbus_watch_list_new (void)</td>
</tr>
<tr class="memdesc:ga19c761997dbbf753c826389c7950d3eb">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new watch list.<br />
</td>
</tr>
<tr class="separator:ga19c761997dbbf753c826389c7950d3eb">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1fe225c4194c30dfe54be322e8519da5" class="memitem:ga1fe225c4194c30dfe54be322e8519da5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_watch_list_free (DBusWatchList *watch_list)</td>
</tr>
<tr class="memdesc:ga1fe225c4194c30dfe54be322e8519da5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Frees a DBusWatchList.<br />
</td>
</tr>
<tr class="separator:ga1fe225c4194c30dfe54be322e8519da5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga68093be43e77210613abc4024ed5100e" class="memitem:ga68093be43e77210613abc4024ed5100e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_watch_list_set_functions (DBusWatchList *watch_list, DBusAddWatchFunction add_function, DBusRemoveWatchFunction remove_function, DBusWatchToggledFunction toggled_function, void *data, DBusFreeFunction free_data_function)</td>
</tr>
<tr class="memdesc:ga68093be43e77210613abc4024ed5100e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the watch functions.<br />
</td>
</tr>
<tr class="separator:ga68093be43e77210613abc4024ed5100e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga01401847e0596226eab39f1c1e2f929e" class="memitem:ga01401847e0596226eab39f1c1e2f929e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_watch_list_add_watch (DBusWatchList *watch_list, DBusWatch *watch)</td>
</tr>
<tr class="memdesc:ga01401847e0596226eab39f1c1e2f929e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Adds a new watch to the watch list, invoking the application DBusAddWatchFunction if appropriate.<br />
</td>
</tr>
<tr class="separator:ga01401847e0596226eab39f1c1e2f929e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaea34537c3e5604b89fbb3f0d4c07aa9b" class="memitem:gaea34537c3e5604b89fbb3f0d4c07aa9b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_watch_list_remove_watch (DBusWatchList *watch_list, DBusWatch *watch)</td>
</tr>
<tr class="memdesc:gaea34537c3e5604b89fbb3f0d4c07aa9b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Removes a watch from the watch list, invoking the application's DBusRemoveWatchFunction if appropriate.<br />
</td>
</tr>
<tr class="separator:gaea34537c3e5604b89fbb3f0d4c07aa9b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga14bb50e8663a1d9d3960b4f73c09c097" class="memitem:ga14bb50e8663a1d9d3960b4f73c09c097">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_watch_list_toggle_watch (DBusWatchList *watch_list, DBusWatch *watch, dbus_bool_t enabled)</td>
</tr>
<tr class="memdesc:ga14bb50e8663a1d9d3960b4f73c09c097">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets a watch to the given enabled state, invoking the application's DBusWatchToggledFunction if appropriate.<br />
</td>
</tr>
<tr class="separator:ga14bb50e8663a1d9d3960b4f73c09c097">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga935ba95d94a14aee79d80abe970eae53" class="memitem:ga935ba95d94a14aee79d80abe970eae53">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_watch_list_toggle_all_watches (DBusWatchList *watch_list, dbus_bool_t enabled)</td>
</tr>
<tr class="memdesc:ga935ba95d94a14aee79d80abe970eae53">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets all watches to the given enabled state, invoking the application's DBusWatchToggledFunction if appropriate.<br />
</td>
</tr>
<tr class="separator:ga935ba95d94a14aee79d80abe970eae53">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga75620808f4d2245914012a41e3b82f3c" class="memitem:ga75620808f4d2245914012a41e3b82f3c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_watch_set_handler (DBusWatch *watch, DBusWatchHandler handler, void *data, DBusFreeFunction free_data_function)</td>
</tr>
<tr class="memdesc:ga75620808f4d2245914012a41e3b82f3c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the handler for the watch.<br />
</td>
</tr>
<tr class="separator:ga75620808f4d2245914012a41e3b82f3c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3f4fb8107cc01941d91d4c4914dda115" class="memitem:ga3f4fb8107cc01941d91d4c4914dda115">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusSocket </td>
<td class="memItemRight" data-valign="bottom">_dbus_watch_get_socket (DBusWatch *watch)</td>
</tr>
<tr class="separator:ga3f4fb8107cc01941d91d4c4914dda115">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga552f23dc081fc9e9b2bf34956171cd71" class="memitem:ga552f23dc081fc9e9b2bf34956171cd71">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT DBusPollable </td>
<td class="memItemRight" data-valign="bottom">_dbus_watch_get_pollable (DBusWatch *watch)</td>
</tr>
<tr class="separator:ga552f23dc081fc9e9b2bf34956171cd71">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

implementation details for DBusWatch

## Macro Definition Documentation

## ◆ \_DBUS_WATCH_NVAL

|                                       |
|---------------------------------------|
| \#define \_DBUS_WATCH_NVAL   (1\<\<4) |

Definition at line 42 of file dbus-watch.h.

## Typedef Documentation

## ◆ DBusWatchHandler

|  |
|----|
| typedef dbus_bool_t(\* DBusWatchHandler) (DBusWatch \*watch, unsigned int flags, void \*data) |

function to run when the watch is handled

Definition at line 45 of file dbus-watch.h.

## ◆ DBusWatchList

|               |
|---------------|
| DBusWatchList |

Opaque data type representing a list of watches and a set of DBusAddWatchFunction/DBusRemoveWatchFunction.

Automatically handles removing/re-adding watches when the DBusAddWatchFunction is updated or changed. Holds a reference count to each watch.

Used in the implementation of both DBusServer and DBusClient.

Definition at line 40 of file dbus-watch.h.

## Function Documentation

## ◆ \_dbus_watch_get_enabled()

|                                      |     |               |         |     |     |
|--------------------------------------|-----|---------------|---------|-----|-----|
| dbus_bool_t \_dbus_watch_get_enabled | (   | DBusWatch \*  | *watch* | )   |     |

Definition at line 59 of file dbus-watch.c.

## ◆ \_dbus_watch_get_oom_last_time()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_watch_get_oom_last_time | ( | DBusWatch \*  | *watch* | ) |  |

Definition at line 65 of file dbus-watch.c.

## ◆ \_dbus_watch_get_pollable()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT DBusPollable \_dbus_watch_get_pollable | ( | DBusWatch \*  | *watch* | ) |  |

Definition at line 623 of file dbus-watch.c.

## ◆ \_dbus_watch_get_socket()

|                                    |     |               |         |     |     |
|------------------------------------|-----|---------------|---------|-----|-----|
| DBusSocket \_dbus_watch_get_socket | (   | DBusWatch \*  | *watch* | )   |     |

Definition at line 607 of file dbus-watch.c.

## ◆ \_dbus_watch_invalidate()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT void \_dbus_watch_invalidate | ( | DBusWatch \*  | *watch* | ) |  |

Clears the file descriptor from a now-invalid watch object so that no one tries to use it.

This is because a watch may stay alive due to reference counts after the file descriptor is closed. Invalidation makes it easier to catch bugs. It also keeps people from doing dorky things like assuming file descriptors are unique (never recycled).

Parameters  
|       |                   |
|-------|-------------------|
| watch | the watch object. |

Definition at line 171 of file dbus-watch.c.

References DBusWatch::fd, and DBusWatch::flags.

Referenced by \_dbus_babysitter_unref(), \_dbus_server_new_for_socket(), \_dbus_spawn_async_with_babysitter(), and \_dbus_transport_new_for_socket().

## ◆ \_dbus_watch_list_add_watch()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_watch_list_add_watch | ( | DBusWatchList \*  | *watch_list*, |
|  |  | DBusWatch \*  | *watch*  |
|  | ) |  |  |

Adds a new watch to the watch list, invoking the application DBusAddWatchFunction if appropriate.

Parameters  
|            |                   |
|------------|-------------------|
| watch_list | the watch list.   |
| watch      | the watch to add. |

<!-- -->

Returns  
TRUE on success, FALSE if no memory.

Definition at line 383 of file dbus-watch.c.

References \_dbus_list_append(), \_dbus_list_remove_last(), \_dbus_watch_ref(), \_dbus_watch_unref(), DBusWatchList::add_watch_function, FALSE, DBusWatch::fd, NULL, TRUE, DBusWatchList::watch_data, and DBusWatchList::watches.

Referenced by \_dbus_connection_add_watch_unlocked(), \_dbus_server_add_watch(), and \_dbus_spawn_async_with_babysitter().

## ◆ \_dbus_watch_list_free()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT void \_dbus_watch_list_free | ( | DBusWatchList \*  | *watch_list* | ) |  |

Frees a DBusWatchList.

Parameters  
|            |                 |
|------------|-----------------|
| watch_list | the watch list. |

Definition at line 251 of file dbus-watch.c.

References \_dbus_list_clear_full(), \_dbus_watch_list_set_functions(), \_dbus_watch_unref(), dbus_free(), NULL, and DBusWatchList::watches.

Referenced by \_dbus_babysitter_unref(), \_dbus_connection_new_for_transport(), \_dbus_server_finalize_base(), and \_dbus_server_init_base().

## ◆ \_dbus_watch_list_new()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT DBusWatchList \* \_dbus_watch_list_new | ( | void  |  | ) |  |

Creates a new watch list.

Returns NULL if insufficient memory exists.

Returns  
the new watch list, or NULL on failure.

Definition at line 234 of file dbus-watch.c.

References dbus_new0, and NULL.

Referenced by \_dbus_connection_new_for_transport(), and \_dbus_server_init_base().

## ◆ \_dbus_watch_list_remove_watch()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT void \_dbus_watch_list_remove_watch | ( | DBusWatchList \*  | *watch_list*, |
|  |  | DBusWatch \*  | *watch*  |
|  | ) |  |  |

Removes a watch from the watch list, invoking the application's DBusRemoveWatchFunction if appropriate.

Parameters  
|            |                      |
|------------|----------------------|
| watch_list | the watch list.      |
| watch      | the watch to remove. |

Definition at line 416 of file dbus-watch.c.

References \_dbus_assert_not_reached, \_dbus_list_remove(), \_dbus_watch_unref(), DBusWatch::fd, NULL, DBusWatchList::remove_watch_function, DBusWatchList::watch_data, and DBusWatchList::watches.

Referenced by \_dbus_connection_remove_watch_unlocked(), and \_dbus_server_remove_watch().

## ◆ \_dbus_watch_list_set_functions()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_watch_list_set_functions | ( | DBusWatchList \*  | *watch_list*, |
|  |  | DBusAddWatchFunction  | *add_function*, |
|  |  | DBusRemoveWatchFunction  | *remove_function*, |
|  |  | DBusWatchToggledFunction  | *toggled_function*, |
|  |  | void \*  | *data*, |
|  |  | DBusFreeFunction  | *free_data_function*  |
|  | ) |  |  |

Sets the watch functions.

This function is the "backend" for dbus_connection_set_watch_functions() and dbus_server_set_watch_functions().

Parameters  
|                    |                                            |
|--------------------|--------------------------------------------|
| watch_list         | the watch list.                            |
| add_function       | the add watch function.                    |
| remove_function    | the remove watch function.                 |
| toggled_function   | function on toggling enabled flag, or NULL |
| data               | the data for those functions.              |
| free_data_function | the function to free the data.             |

<!-- -->

Returns  
FALSE if not enough memory

Definition at line 297 of file dbus-watch.c.

References \_dbus_list_foreach(), \_dbus_list_get_first_link(), \_dbus_list_get_next_link, DBusWatchList::add_watch_function, DBusList::data, dbus_watch_get_flags(), FALSE, DBusWatch::fd, NULL, DBusWatchList::remove_watch_function, TRUE, DBusWatchList::watch_data, DBusWatchList::watch_free_data_function, DBusWatchList::watch_toggled_function, and DBusWatchList::watches.

Referenced by \_dbus_babysitter_set_watch_functions(), \_dbus_watch_list_free(), dbus_connection_set_watch_functions(), and dbus_server_set_watch_functions().

## ◆ \_dbus_watch_list_toggle_all_watches()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_watch_list_toggle_all_watches | ( | DBusWatchList \*  | *watch_list*, |
|  |  | dbus_bool_t  | *enabled*  |
|  | ) |  |  |

Sets all watches to the given enabled state, invoking the application's DBusWatchToggledFunction if appropriate.

Parameters  
|            |                 |
|------------|-----------------|
| watch_list | the watch list. |
| enabled    | TRUE to enable  |

Definition at line 474 of file dbus-watch.c.

References \_dbus_list_get_first_link(), \_dbus_list_get_next_link, \_dbus_watch_list_toggle_watch(), DBusList::data, NULL, and DBusWatchList::watches.

Referenced by \_dbus_server_toggle_all_watches().

## ◆ \_dbus_watch_list_toggle_watch()

|                                     |     |                   |               |
|-------------------------------------|-----|-------------------|---------------|
| void \_dbus_watch_list_toggle_watch | (   | DBusWatchList \*  | *watch_list*, |
|                                     |     | DBusWatch \*      | *watch*,      |
|                                     |     | dbus_bool_t       | *enabled*     |
|                                     | )   |                   |               |

Sets a watch to the given enabled state, invoking the application's DBusWatchToggledFunction if appropriate.

Parameters  
|            |                      |
|------------|----------------------|
| watch_list | the watch list.      |
| watch      | the watch to toggle. |
| enabled    | TRUE to enable       |

Definition at line 443 of file dbus-watch.c.

References DBusWatch::enabled, DBusWatch::fd, NULL, DBusWatchList::watch_data, and DBusWatchList::watch_toggled_function.

Referenced by \_dbus_connection_toggle_watch_unlocked(), and \_dbus_watch_list_toggle_all_watches().

## ◆ \_dbus_watch_new()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT DBusWatch \* \_dbus_watch_new | ( | DBusPollable  | *fd*, |
|  |  | unsigned int  | *flags*, |
|  |  | dbus_bool_t  | *enabled*, |
|  |  | DBusWatchHandler  | *handler*, |
|  |  | void \*  | *data*, |
|  |  | DBusFreeFunction  | *free_data_function*  |
|  | ) |  |  |

Creates a new DBusWatch.

Used to add a file descriptor to be polled by a main loop.

Parameters  
|                    |                                                |
|--------------------|------------------------------------------------|
| fd                 | the file descriptor to be watched.             |
| flags              | the conditions to watch for on the descriptor. |
| enabled            | the initial enabled state                      |
| handler            | the handler function                           |
| data               | data for handler function                      |
| free_data_function | function to free the data                      |

<!-- -->

Returns  
the new DBusWatch object.

Definition at line 90 of file dbus-watch.c.

References \_dbus_assert, dbus_new0, DBusWatch::enabled, DBusWatch::fd, DBusWatch::flags, DBusWatch::free_handler_data_function, DBusWatch::handler, DBusWatch::handler_data, NULL, and DBusWatch::refcount.

Referenced by \_dbus_server_new_for_socket(), \_dbus_spawn_async_with_babysitter(), and \_dbus_transport_new_for_socket().

## ◆ \_dbus_watch_ref()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT DBusWatch \* \_dbus_watch_ref | ( | DBusWatch \*  | *watch* | ) |  |

Increments the reference count of a DBusWatch object.

Parameters  
|       |                   |
|-------|-------------------|
| watch | the watch object. |

<!-- -->

Returns  
the watch object.

Definition at line 126 of file dbus-watch.c.

References DBusWatch::refcount.

Referenced by \_dbus_transport_handle_watch(), and \_dbus_watch_list_add_watch().

## ◆ \_dbus_watch_sanitize_condition()

|                                      |     |                  |              |
|--------------------------------------|-----|------------------|--------------|
| void \_dbus_watch_sanitize_condition | (   | DBusWatch \*     | *watch*,     |
|                                      |     | unsigned int \*  | *condition*  |
|                                      | )   |                  |              |

Sanitizes the given condition so that it only contains flags that the DBusWatch requested.

e.g. if the watch is a DBUS_WATCH_READABLE watch then DBUS_WATCH_WRITABLE will be stripped from the condition.

Parameters  
|           |                                       |
|-----------|---------------------------------------|
| watch     | the watch object.                     |
| condition | address of the condition to sanitize. |

Definition at line 187 of file dbus-watch.c.

References DBUS_WATCH_READABLE, DBUS_WATCH_WRITABLE, and DBusWatch::flags.

Referenced by \_dbus_transport_handle_watch(), and dbus_watch_handle().

## ◆ \_dbus_watch_set_handler()

|                               |     |                   |                       |
|-------------------------------|-----|-------------------|-----------------------|
| void \_dbus_watch_set_handler | (   | DBusWatch \*      | *watch*,              |
|                               |     | DBusWatchHandler  | *handler*,            |
|                               |     | void \*           | *data*,               |
|                               |     | DBusFreeFunction  | *free_data_function*  |
|                               | )   |                   |                       |

Sets the handler for the watch.

Parameters  
|                    |                     |
|--------------------|---------------------|
| watch              | the watch           |
| handler            | the new handler     |
| data               | the data            |
| free_data_function | free data with this |

Definition at line 500 of file dbus-watch.c.

References DBusWatch::free_handler_data_function, DBusWatch::handler, and DBusWatch::handler_data.

## ◆ \_dbus_watch_set_oom_last_time()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT void \_dbus_watch_set_oom_last_time | ( | DBusWatch \*  | *watch*, |
|  |  | dbus_bool_t  | *oom*  |
|  | ) |  |  |

Definition at line 71 of file dbus-watch.c.

## ◆ \_dbus_watch_unref()

|                                             |     |               |         |     |     |
|---------------------------------------------|-----|---------------|---------|-----|-----|
| DBUS_PRIVATE_EXPORT void \_dbus_watch_unref | (   | DBusWatch \*  | *watch* | )   |     |

Decrements the reference count of a DBusWatch object and finalizes the object if the count reaches zero.

Parameters  
|       |                   |
|-------|-------------------|
| watch | the watch object. |

Definition at line 140 of file dbus-watch.c.

References \_dbus_assert, \_dbus_warn(), dbus_free(), dbus_watch_set_data(), DBusWatch::fd, DBusWatch::free_handler_data_function, DBusWatch::handler_data, NULL, and DBusWatch::refcount.

Referenced by \_dbus_babysitter_unref(), \_dbus_server_new_for_socket(), \_dbus_spawn_async_with_babysitter(), \_dbus_transport_handle_watch(), \_dbus_transport_new_for_socket(), \_dbus_watch_list_add_watch(), \_dbus_watch_list_free(), and \_dbus_watch_list_remove_watch().
