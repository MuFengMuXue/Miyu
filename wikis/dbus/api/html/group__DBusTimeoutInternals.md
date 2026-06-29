DBusTimeout implementation details

D-Bus secret internal implementation details

implementation details for DBusTimeout More...

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
<td class="memItemRight" data-valign="bottom">DBusTimeout</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Internals of DBusTimeout. More...<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusTimeoutList</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">DBusTimeoutList implementation details. More...<br />
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
<tr id="r_gabc3cb66aa2ec450d298fe7ec3b480fa1" class="memitem:gabc3cb66aa2ec450d298fe7ec3b480fa1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusTimeoutList </td>
<td class="memItemRight" data-valign="bottom">DBusTimeoutList</td>
</tr>
<tr class="memdesc:gabc3cb66aa2ec450d298fe7ec3b480fa1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Opaque data type representing a list of timeouts and a set of DBusAddTimeoutFunction/DBusRemoveTimeoutFunction.<br />
</td>
</tr>
<tr class="separator:gabc3cb66aa2ec450d298fe7ec3b480fa1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gacf1fe8b6d7f524f1a3581519594a5563" class="memitem:gacf1fe8b6d7f524f1a3581519594a5563">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef dbus_bool_t(* </td>
<td class="memItemRight" data-valign="bottom">DBusTimeoutHandler) (void *data)</td>
</tr>
<tr class="memdesc:gacf1fe8b6d7f524f1a3581519594a5563">
<td class="mdescLeft"> </td>
<td class="mdescRight">function to run when the timeout is handled<br />
</td>
</tr>
<tr class="separator:gacf1fe8b6d7f524f1a3581519594a5563">
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
<tr id="r_gaa3a12ccc1e6772d7bc143ce8edfa886b" class="memitem:gaa3a12ccc1e6772d7bc143ce8edfa886b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusTimeout * </td>
<td class="memItemRight" data-valign="bottom">_dbus_timeout_new (int interval, DBusTimeoutHandler handler, void *data, DBusFreeFunction free_data_function)</td>
</tr>
<tr class="memdesc:gaa3a12ccc1e6772d7bc143ce8edfa886b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new DBusTimeout, enabled by default.<br />
</td>
</tr>
<tr class="separator:gaa3a12ccc1e6772d7bc143ce8edfa886b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gadf014caa89efb09ae72c300ae5c4fda5" class="memitem:gadf014caa89efb09ae72c300ae5c4fda5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusTimeout * </td>
<td class="memItemRight" data-valign="bottom">_dbus_timeout_ref (DBusTimeout *timeout)</td>
</tr>
<tr class="memdesc:gadf014caa89efb09ae72c300ae5c4fda5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Increments the reference count of a DBusTimeout object.<br />
</td>
</tr>
<tr class="separator:gadf014caa89efb09ae72c300ae5c4fda5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6527af11feecf5d50fd9d5b674f94406" class="memitem:ga6527af11feecf5d50fd9d5b674f94406">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_timeout_unref (DBusTimeout *timeout)</td>
</tr>
<tr class="memdesc:ga6527af11feecf5d50fd9d5b674f94406">
<td class="mdescLeft"> </td>
<td class="mdescRight">Decrements the reference count of a DBusTimeout object and finalizes the object if the count reaches zero.<br />
</td>
</tr>
<tr class="separator:ga6527af11feecf5d50fd9d5b674f94406">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabcbd7aa3550ea81acf7817a4add54987" class="memitem:gabcbd7aa3550ea81acf7817a4add54987">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_timeout_restart (DBusTimeout *timeout, int interval)</td>
</tr>
<tr class="memdesc:gabcbd7aa3550ea81acf7817a4add54987">
<td class="mdescLeft"> </td>
<td class="mdescRight">Change the timeout interval to be interval milliseconds from now (forgetting when the timeout was initially started), and enable it.<br />
</td>
</tr>
<tr class="separator:gabcbd7aa3550ea81acf7817a4add54987">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8fc851ddb765ef5eb6980c5729520d65" class="memitem:ga8fc851ddb765ef5eb6980c5729520d65">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_timeout_disable (DBusTimeout *timeout)</td>
</tr>
<tr class="memdesc:ga8fc851ddb765ef5eb6980c5729520d65">
<td class="mdescLeft"> </td>
<td class="mdescRight">Disable the timeout.<br />
</td>
</tr>
<tr class="separator:ga8fc851ddb765ef5eb6980c5729520d65">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5b122b35cdb3926b7dc2d084ddff9d62" class="memitem:ga5b122b35cdb3926b7dc2d084ddff9d62">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusTimeoutList * </td>
<td class="memItemRight" data-valign="bottom">_dbus_timeout_list_new (void)</td>
</tr>
<tr class="memdesc:ga5b122b35cdb3926b7dc2d084ddff9d62">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new timeout list.<br />
</td>
</tr>
<tr class="separator:ga5b122b35cdb3926b7dc2d084ddff9d62">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1b399ef2d7f128e59bb32dbb5b590e1b" class="memitem:ga1b399ef2d7f128e59bb32dbb5b590e1b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_timeout_list_free (DBusTimeoutList *timeout_list)</td>
</tr>
<tr class="memdesc:ga1b399ef2d7f128e59bb32dbb5b590e1b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Frees a DBusTimeoutList.<br />
</td>
</tr>
<tr class="separator:ga1b399ef2d7f128e59bb32dbb5b590e1b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6760d1963b870b45f855501e38b49fd9" class="memitem:ga6760d1963b870b45f855501e38b49fd9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_timeout_list_set_functions (DBusTimeoutList *timeout_list, DBusAddTimeoutFunction add_function, DBusRemoveTimeoutFunction remove_function, DBusTimeoutToggledFunction toggled_function, void *data, DBusFreeFunction free_data_function)</td>
</tr>
<tr class="memdesc:ga6760d1963b870b45f855501e38b49fd9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the timeout functions.<br />
</td>
</tr>
<tr class="separator:ga6760d1963b870b45f855501e38b49fd9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga14955f061551ece122808b9e6ddc0757" class="memitem:ga14955f061551ece122808b9e6ddc0757">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_timeout_list_add_timeout (DBusTimeoutList *timeout_list, DBusTimeout *timeout)</td>
</tr>
<tr class="memdesc:ga14955f061551ece122808b9e6ddc0757">
<td class="mdescLeft"> </td>
<td class="mdescRight">Adds a new timeout to the timeout list, invoking the application DBusAddTimeoutFunction if appropriate.<br />
</td>
</tr>
<tr class="separator:ga14955f061551ece122808b9e6ddc0757">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaec0ffafdcac87f23878a2ddded044822" class="memitem:gaec0ffafdcac87f23878a2ddded044822">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_timeout_list_remove_timeout (DBusTimeoutList *timeout_list, DBusTimeout *timeout)</td>
</tr>
<tr class="memdesc:gaec0ffafdcac87f23878a2ddded044822">
<td class="mdescLeft"> </td>
<td class="mdescRight">Removes a timeout from the timeout list, invoking the application's DBusRemoveTimeoutFunction if appropriate.<br />
</td>
</tr>
<tr class="separator:gaec0ffafdcac87f23878a2ddded044822">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3d1ee0968a47651c5428ebf48711b217" class="memitem:ga3d1ee0968a47651c5428ebf48711b217">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_timeout_list_toggle_timeout (DBusTimeoutList *timeout_list, DBusTimeout *timeout, dbus_bool_t enabled)</td>
</tr>
<tr class="memdesc:ga3d1ee0968a47651c5428ebf48711b217">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets a timeout to the given enabled state, invoking the application's DBusTimeoutToggledFunction if appropriate.<br />
</td>
</tr>
<tr class="separator:ga3d1ee0968a47651c5428ebf48711b217">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf05e9d9352e8c9782a784519385c312c" class="memitem:gaf05e9d9352e8c9782a784519385c312c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_timeout_needs_restart (DBusTimeout *timeout)</td>
</tr>
<tr class="memdesc:gaf05e9d9352e8c9782a784519385c312c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns whether a timeout needs restart time counting in the event loop.<br />
</td>
</tr>
<tr class="separator:gaf05e9d9352e8c9782a784519385c312c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae3b64e7a954866a941d3b24682527b01" class="memitem:gae3b64e7a954866a941d3b24682527b01">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_timeout_restarted (DBusTimeout *timeout)</td>
</tr>
<tr class="memdesc:gae3b64e7a954866a941d3b24682527b01">
<td class="mdescLeft"> </td>
<td class="mdescRight">Mark timeout as restarted (setting timestamps is responsibility of the event loop).<br />
</td>
</tr>
<tr class="separator:gae3b64e7a954866a941d3b24682527b01">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

implementation details for DBusTimeout

## Typedef Documentation

## ◆ DBusTimeoutHandler

|                                                          |
|----------------------------------------------------------|
| typedef dbus_bool_t(\* DBusTimeoutHandler) (void \*data) |

function to run when the timeout is handled

Definition at line 43 of file dbus-timeout.h.

## ◆ DBusTimeoutList

|                 |
|-----------------|
| DBusTimeoutList |

Opaque data type representing a list of timeouts and a set of DBusAddTimeoutFunction/DBusRemoveTimeoutFunction.

Automatically handles removing/re-adding timeouts when the DBusAddTimeoutFunction is updated or changed. Holds a reference count to each timeout.

Definition at line 40 of file dbus-timeout.h.

## Function Documentation

## ◆ \_dbus_timeout_disable()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT void \_dbus_timeout_disable | ( | DBusTimeout \*  | *timeout* | ) |  |

Disable the timeout.

Note that you should use \_dbus_connection_toggle_timeout_unlocked() etc. instead, if the timeout is passed out to an application main loop. i.e. you can't use this function in the D-Bus library, it's only used in the message bus daemon implementation.

Parameters  
|         |                                    |
|---------|------------------------------------|
| timeout | the timeout                        |
| enabled | TRUE if timeout should be enabled. |

Definition at line 161 of file dbus-timeout.c.

References DBusTimeout::enabled, and FALSE.

## ◆ \_dbus_timeout_list_add_timeout()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_timeout_list_add_timeout | ( | DBusTimeoutList \*  | *timeout_list*, |
|  |  | DBusTimeout \*  | *timeout*  |
|  | ) |  |  |

Adds a new timeout to the timeout list, invoking the application DBusAddTimeoutFunction if appropriate.

Parameters  
|              |                     |
|--------------|---------------------|
| timeout_list | the timeout list.   |
| timeout      | the timeout to add. |

<!-- -->

Returns  
TRUE on success, FALSE If no memory.

Definition at line 314 of file dbus-timeout.c.

References \_dbus_list_append(), \_dbus_list_remove_last(), \_dbus_timeout_ref(), \_dbus_timeout_unref(), DBusTimeoutList::add_timeout_function, FALSE, NULL, DBusTimeoutList::timeout_data, DBusTimeoutList::timeouts, and TRUE.

Referenced by \_dbus_connection_add_timeout_unlocked(), and \_dbus_server_add_timeout().

## ◆ \_dbus_timeout_list_free()

|                               |     |                     |                |     |     |
|-------------------------------|-----|---------------------|----------------|-----|-----|
| void \_dbus_timeout_list_free | (   | DBusTimeoutList \*  | *timeout_list* | )   |     |

Frees a DBusTimeoutList.

Parameters  
|              |                   |
|--------------|-------------------|
| timeout_list | the timeout list. |

Definition at line 217 of file dbus-timeout.c.

References \_dbus_list_clear_full(), \_dbus_timeout_list_set_functions(), \_dbus_timeout_unref(), dbus_free(), NULL, and DBusTimeoutList::timeouts.

Referenced by \_dbus_connection_new_for_transport(), \_dbus_server_finalize_base(), and \_dbus_server_init_base().

## ◆ \_dbus_timeout_list_new()

|                                            |     |       |     |     |     |
|--------------------------------------------|-----|-------|-----|-----|-----|
| DBusTimeoutList \* \_dbus_timeout_list_new | (   | void  |     | )   |     |

Creates a new timeout list.

Returns NULL if insufficient memory exists.

Returns  
the new timeout list, or NULL on failure.

Definition at line 200 of file dbus-timeout.c.

References dbus_new0, and NULL.

Referenced by \_dbus_connection_new_for_transport(), and \_dbus_server_init_base().

## ◆ \_dbus_timeout_list_remove_timeout()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_timeout_list_remove_timeout | ( | DBusTimeoutList \*  | *timeout_list*, |
|  |  | DBusTimeout \*  | *timeout*  |
|  | ) |  |  |

Removes a timeout from the timeout list, invoking the application's DBusRemoveTimeoutFunction if appropriate.

Parameters  
|              |                        |
|--------------|------------------------|
| timeout_list | the timeout list.      |
| timeout      | the timeout to remove. |

Definition at line 344 of file dbus-timeout.c.

References \_dbus_assert_not_reached, \_dbus_list_remove(), \_dbus_timeout_unref(), NULL, DBusTimeoutList::remove_timeout_function, DBusTimeoutList::timeout_data, and DBusTimeoutList::timeouts.

Referenced by \_dbus_connection_remove_timeout_unlocked(), and \_dbus_server_remove_timeout().

## ◆ \_dbus_timeout_list_set_functions()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_timeout_list_set_functions | ( | DBusTimeoutList \*  | *timeout_list*, |
|  |  | DBusAddTimeoutFunction  | *add_function*, |
|  |  | DBusRemoveTimeoutFunction  | *remove_function*, |
|  |  | DBusTimeoutToggledFunction  | *toggled_function*, |
|  |  | void \*  | *data*, |
|  |  | DBusFreeFunction  | *free_data_function*  |
|  | ) |  |  |

Sets the timeout functions.

This function is the "backend" for dbus_connection_set_timeout_functions().

Parameters  
|                    |                                 |
|--------------------|---------------------------------|
| timeout_list       | the timeout list                |
| add_function       | the add timeout function.       |
| remove_function    | the remove timeout function.    |
| toggled_function   | toggle notify function, or NULL |
| data               | the data for those functions.   |
| free_data_function | the function to free the data.  |

<!-- -->

Returns  
FALSE if no memory

Definition at line 243 of file dbus-timeout.c.

References \_dbus_list_foreach(), \_dbus_list_get_first_link(), \_dbus_list_get_next_link, DBusTimeoutList::add_timeout_function, DBusList::data, FALSE, NULL, DBusTimeoutList::remove_timeout_function, DBusTimeoutList::timeout_data, DBusTimeoutList::timeout_free_data_function, DBusTimeoutList::timeout_toggled_function, DBusTimeoutList::timeouts, and TRUE.

Referenced by \_dbus_timeout_list_free(), dbus_connection_set_timeout_functions(), and dbus_server_set_timeout_functions().

## ◆ \_dbus_timeout_list_toggle_timeout()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_timeout_list_toggle_timeout | ( | DBusTimeoutList \*  | *timeout_list*, |
|  |  | DBusTimeout \*  | *timeout*, |
|  |  | dbus_bool_t  | *enabled*  |
|  | ) |  |  |

Sets a timeout to the given enabled state, invoking the application's DBusTimeoutToggledFunction if appropriate.

Parameters  
|              |                        |
|--------------|------------------------|
| timeout_list | the timeout list.      |
| timeout      | the timeout to toggle. |
| enabled      | TRUE to enable         |

Definition at line 366 of file dbus-timeout.c.

References DBusTimeout::enabled, NULL, DBusTimeoutList::timeout_data, and DBusTimeoutList::timeout_toggled_function.

Referenced by \_dbus_connection_toggle_timeout_unlocked(), and \_dbus_server_toggle_timeout().

## ◆ \_dbus_timeout_needs_restart()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_timeout_needs_restart | ( | DBusTimeout \*  | *timeout* | ) |  |

Returns whether a timeout needs restart time counting in the event loop.

Parameters  
|         |                        |
|---------|------------------------|
| timeout | the DBusTimeout object |

<!-- -->

Returns  
TRUE if restart is needed

Definition at line 389 of file dbus-timeout.c.

References DBusTimeout::needs_restart.

## ◆ \_dbus_timeout_new()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT DBusTimeout \* \_dbus_timeout_new | ( | int  | *interval*, |
|  |  | DBusTimeoutHandler  | *handler*, |
|  |  | void \*  | *data*, |
|  |  | DBusFreeFunction  | *free_data_function*  |
|  | ) |  |  |

Creates a new DBusTimeout, enabled by default.

Parameters  
|                    |                                           |
|--------------------|-------------------------------------------|
| interval           | the timeout interval in milliseconds.     |
| handler            | function to call when the timeout occurs. |
| data               | data to pass to the handler               |
| free_data_function | function to be called to free the data.   |

<!-- -->

Returns  
the new DBusTimeout object,

Definition at line 66 of file dbus-timeout.c.

References dbus_new0, DBusTimeout::enabled, FALSE, DBusTimeout::free_handler_data_function, DBusTimeout::handler, DBusTimeout::handler_data, DBusTimeout::interval, DBusTimeout::needs_restart, NULL, DBusTimeout::refcount, and TRUE.

Referenced by \_dbus_pending_call_new_unlocked().

## ◆ \_dbus_timeout_ref()

|                                   |     |                 |           |     |     |
|-----------------------------------|-----|-----------------|-----------|-----|-----|
| DBusTimeout \* \_dbus_timeout_ref | (   | DBusTimeout \*  | *timeout* | )   |     |

Increments the reference count of a DBusTimeout object.

Parameters  
|         |                     |
|---------|---------------------|
| timeout | the timeout object. |

<!-- -->

Returns  
the timeout object.

Definition at line 97 of file dbus-timeout.c.

References DBusTimeout::refcount.

Referenced by \_dbus_timeout_list_add_timeout().

## ◆ \_dbus_timeout_restart()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT void \_dbus_timeout_restart | ( | DBusTimeout \*  | *timeout*, |
|  |  | int  | *interval*  |
|  | ) |  |  |

Change the timeout interval to be interval milliseconds from now (forgetting when the timeout was initially started), and enable it.

This function is only valid when used in conjunction with DBusLoop: it can be used in the message bus daemon implementation or in unit tests, but it cannot be used in conjunction with an application main loop.

Parameters  
|          |                  |
|----------|------------------|
| timeout  | the timeout      |
| interval | the new interval |

Definition at line 140 of file dbus-timeout.c.

References \_dbus_assert, DBusTimeout::enabled, DBusTimeout::interval, DBusTimeout::needs_restart, and TRUE.

## ◆ \_dbus_timeout_restarted()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT void \_dbus_timeout_restarted | ( | DBusTimeout \*  | *timeout* | ) |  |

Mark timeout as restarted (setting timestamps is responsibility of the event loop).

Parameters  
|         |                        |
|---------|------------------------|
| timeout | the DBusTimeout object |

Definition at line 401 of file dbus-timeout.c.

References FALSE, and DBusTimeout::needs_restart.

## ◆ \_dbus_timeout_unref()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT void \_dbus_timeout_unref | ( | DBusTimeout \*  | *timeout* | ) |  |

Decrements the reference count of a DBusTimeout object and finalizes the object if the count reaches zero.

Parameters  
|         |                     |
|---------|---------------------|
| timeout | the timeout object. |

Definition at line 111 of file dbus-timeout.c.

References \_dbus_assert, dbus_free(), dbus_timeout_set_data(), DBusTimeout::free_handler_data_function, DBusTimeout::handler_data, NULL, and DBusTimeout::refcount.

Referenced by \_dbus_timeout_list_add_timeout(), \_dbus_timeout_list_free(), and \_dbus_timeout_list_remove_timeout().
