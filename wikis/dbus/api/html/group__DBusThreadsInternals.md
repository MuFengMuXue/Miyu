Thread functions

D-Bus secret internal implementation details

\_dbus_rmutex_lock(), etc. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="typedefs" class="groupheader"> Typedefs</h2></td>
</tr>
<tr id="r_ga5317a58c6ec622c81615dcf2d87aa92b" class="memitem:ga5317a58c6ec622c81615dcf2d87aa92b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusRMutex </td>
<td class="memItemRight" data-valign="bottom">DBusRMutex</td>
</tr>
<tr class="memdesc:ga5317a58c6ec622c81615dcf2d87aa92b">
<td class="mdescLeft"> </td>
<td class="mdescRight">A mutex which is recursive if possible, else non-recursive.<br />
</td>
</tr>
<tr class="separator:ga5317a58c6ec622c81615dcf2d87aa92b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3ab2e6d6f2aa71121ee5d7913cc4c4e9" class="memitem:ga3ab2e6d6f2aa71121ee5d7913cc4c4e9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusCMutex </td>
<td class="memItemRight" data-valign="bottom">DBusCMutex</td>
</tr>
<tr class="memdesc:ga3ab2e6d6f2aa71121ee5d7913cc4c4e9">
<td class="mdescLeft"> </td>
<td class="mdescRight">A mutex suitable for use with condition variables.<br />
</td>
</tr>
<tr class="separator:ga3ab2e6d6f2aa71121ee5d7913cc4c4e9">
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
<tr id="r_ga191deedb97c76fae82bdbc8e1559a849" class="memitem:ga191deedb97c76fae82bdbc8e1559a849">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_rmutex_new_at_location (DBusRMutex **location_p)</td>
</tr>
<tr class="memdesc:ga191deedb97c76fae82bdbc8e1559a849">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new mutex or creates a no-op mutex if threads are not initialized.<br />
</td>
</tr>
<tr class="separator:ga191deedb97c76fae82bdbc8e1559a849">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga89495162caac2ace36c6b9c2031bc962" class="memitem:ga89495162caac2ace36c6b9c2031bc962">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_cmutex_new_at_location (DBusCMutex **location_p)</td>
</tr>
<tr class="memdesc:ga89495162caac2ace36c6b9c2031bc962">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new mutex or creates a no-op mutex if threads are not initialized.<br />
</td>
</tr>
<tr class="separator:ga89495162caac2ace36c6b9c2031bc962">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae1c95a3f47bcc78d32fc0a5a8ed37c91" class="memitem:gae1c95a3f47bcc78d32fc0a5a8ed37c91">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_rmutex_free_at_location (DBusRMutex **location_p)</td>
</tr>
<tr class="memdesc:gae1c95a3f47bcc78d32fc0a5a8ed37c91">
<td class="mdescLeft"> </td>
<td class="mdescRight">Frees a DBusRMutex; does nothing if passed a NULL pointer.<br />
</td>
</tr>
<tr class="separator:gae1c95a3f47bcc78d32fc0a5a8ed37c91">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga20ec8aeb88b1f65445a4d3c1c0bd0048" class="memitem:ga20ec8aeb88b1f65445a4d3c1c0bd0048">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_cmutex_free_at_location (DBusCMutex **location_p)</td>
</tr>
<tr class="memdesc:ga20ec8aeb88b1f65445a4d3c1c0bd0048">
<td class="mdescLeft"> </td>
<td class="mdescRight">Frees a DBusCMutex; does nothing if passed a NULL pointer.<br />
</td>
</tr>
<tr class="separator:ga20ec8aeb88b1f65445a4d3c1c0bd0048">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaeb20c411a096aaf067918eb574f121d5" class="memitem:gaeb20c411a096aaf067918eb574f121d5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_rmutex_lock (DBusRMutex *mutex)</td>
</tr>
<tr class="memdesc:gaeb20c411a096aaf067918eb574f121d5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Locks a mutex.<br />
</td>
</tr>
<tr class="separator:gaeb20c411a096aaf067918eb574f121d5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabea1bdc19c155bca909839090c05eee2" class="memitem:gabea1bdc19c155bca909839090c05eee2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_cmutex_lock (DBusCMutex *mutex)</td>
</tr>
<tr class="memdesc:gabea1bdc19c155bca909839090c05eee2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Locks a mutex.<br />
</td>
</tr>
<tr class="separator:gabea1bdc19c155bca909839090c05eee2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5946b9a5ea3e12a81a798b575b45c62f" class="memitem:ga5946b9a5ea3e12a81a798b575b45c62f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_rmutex_unlock (DBusRMutex *mutex)</td>
</tr>
<tr class="memdesc:ga5946b9a5ea3e12a81a798b575b45c62f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Unlocks a mutex.<br />
</td>
</tr>
<tr class="separator:ga5946b9a5ea3e12a81a798b575b45c62f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad199edcd1bb88cfd2e9dcfb47cbc732f" class="memitem:gad199edcd1bb88cfd2e9dcfb47cbc732f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_cmutex_unlock (DBusCMutex *mutex)</td>
</tr>
<tr class="memdesc:gad199edcd1bb88cfd2e9dcfb47cbc732f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Unlocks a mutex.<br />
</td>
</tr>
<tr class="separator:gad199edcd1bb88cfd2e9dcfb47cbc732f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga282455cbb556e37fa47ee829fd9d2fad" class="memitem:ga282455cbb556e37fa47ee829fd9d2fad">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusCondVar * </td>
<td class="memItemRight" data-valign="bottom">_dbus_condvar_new (void)</td>
</tr>
<tr class="memdesc:ga282455cbb556e37fa47ee829fd9d2fad">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new condition variable using the function supplied to dbus_threads_init(), or creates a no-op condition variable if threads are not initialized.<br />
</td>
</tr>
<tr class="separator:ga282455cbb556e37fa47ee829fd9d2fad">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga859c5830e3c212323c1d6dafee3858a1" class="memitem:ga859c5830e3c212323c1d6dafee3858a1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_condvar_new_at_location (DBusCondVar **location_p)</td>
</tr>
<tr class="memdesc:ga859c5830e3c212323c1d6dafee3858a1">
<td class="mdescLeft"> </td>
<td class="mdescRight">This does the same thing as _dbus_condvar_new.<br />
</td>
</tr>
<tr class="separator:ga859c5830e3c212323c1d6dafee3858a1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaff04b7377b6ab0cc22fee6a2811dde84" class="memitem:gaff04b7377b6ab0cc22fee6a2811dde84">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_condvar_free (DBusCondVar *cond)</td>
</tr>
<tr class="memdesc:gaff04b7377b6ab0cc22fee6a2811dde84">
<td class="mdescLeft"> </td>
<td class="mdescRight">Frees a conditional variable created with dbus_condvar_new(); does nothing if passed a NULL pointer.<br />
</td>
</tr>
<tr class="separator:gaff04b7377b6ab0cc22fee6a2811dde84">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga29444a34b569fca22fac48067832aacd" class="memitem:ga29444a34b569fca22fac48067832aacd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_condvar_free_at_location (DBusCondVar **location_p)</td>
</tr>
<tr class="memdesc:ga29444a34b569fca22fac48067832aacd">
<td class="mdescLeft"> </td>
<td class="mdescRight">Frees a condition variable; does nothing if passed a NULL pointer.<br />
</td>
</tr>
<tr class="separator:ga29444a34b569fca22fac48067832aacd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6938b8a4547ce48290615990f64bd3bb" class="memitem:ga6938b8a4547ce48290615990f64bd3bb">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_condvar_wait (DBusCondVar *cond, DBusCMutex *mutex)</td>
</tr>
<tr class="memdesc:ga6938b8a4547ce48290615990f64bd3bb">
<td class="mdescLeft"> </td>
<td class="mdescRight">Atomically unlocks the mutex and waits for the conditions variable to be signalled.<br />
</td>
</tr>
<tr class="separator:ga6938b8a4547ce48290615990f64bd3bb">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga918e53c2abc48ff496f3c75566ba8bd3" class="memitem:ga918e53c2abc48ff496f3c75566ba8bd3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_condvar_wait_timeout (DBusCondVar *cond, DBusCMutex *mutex, int timeout_milliseconds)</td>
</tr>
<tr class="memdesc:ga918e53c2abc48ff496f3c75566ba8bd3">
<td class="mdescLeft"> </td>
<td class="mdescRight">Atomically unlocks the mutex and waits for the conditions variable to be signalled, or for a timeout.<br />
</td>
</tr>
<tr class="separator:ga918e53c2abc48ff496f3c75566ba8bd3">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8af2fd84773022e7e7ce1f21f0126203" class="memitem:ga8af2fd84773022e7e7ce1f21f0126203">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_condvar_wake_one (DBusCondVar *cond)</td>
</tr>
<tr class="memdesc:ga8af2fd84773022e7e7ce1f21f0126203">
<td class="mdescLeft"> </td>
<td class="mdescRight">If there are threads waiting on the condition variable, wake up exactly one.<br />
</td>
</tr>
<tr class="separator:ga8af2fd84773022e7e7ce1f21f0126203">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1703349138323e4dbb947ab2a73c943b" class="memitem:ga1703349138323e4dbb947ab2a73c943b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_lock (DBusGlobalLock lock)</td>
</tr>
<tr class="separator:ga1703349138323e4dbb947ab2a73c943b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga82891a341a3b79f3228b8dd2dd1b0e30" class="memitem:ga82891a341a3b79f3228b8dd2dd1b0e30">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_unlock (DBusGlobalLock lock)</td>
</tr>
<tr class="separator:ga82891a341a3b79f3228b8dd2dd1b0e30">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

\_dbus_rmutex_lock(), etc.

Functions and macros related to threads and thread locks.

## Typedef Documentation

## ◆ DBusCMutex

|                                      |
|--------------------------------------|
| typedef struct DBusCMutex DBusCMutex |

A mutex suitable for use with condition variables.

This is typically non-recursive.

Definition at line 47 of file dbus-threads-internal.h.

## ◆ DBusRMutex

|                                      |
|--------------------------------------|
| typedef struct DBusRMutex DBusRMutex |

A mutex which is recursive if possible, else non-recursive.

This is typically recursive, but that cannot be relied upon.

Definition at line 41 of file dbus-threads-internal.h.

## Function Documentation

## ◆ \_dbus_cmutex_free_at_location()

|                                     |     |                  |              |     |     |
|-------------------------------------|-----|------------------|--------------|-----|-----|
| void \_dbus_cmutex_free_at_location | (   | DBusCMutex \*\*  | *location_p* | )   |     |

Frees a DBusCMutex; does nothing if passed a NULL pointer.

Definition at line 110 of file dbus-threads.c.

References NULL.

Referenced by \_dbus_connection_new_for_transport().

## ◆ \_dbus_cmutex_lock()

|                         |     |                |         |     |     |
|-------------------------|-----|----------------|---------|-----|-----|
| void \_dbus_cmutex_lock | (   | DBusCMutex \*  | *mutex* | )   |     |

Locks a mutex.

Does nothing if passed a NULL pointer. Locks may be recursive if threading implementation initialized recursive locks.

Definition at line 139 of file dbus-threads.c.

References NULL.

## ◆ \_dbus_cmutex_new_at_location()

|                                    |     |                  |              |     |     |
|------------------------------------|-----|------------------|--------------|-----|-----|
| void \_dbus_cmutex_new_at_location | (   | DBusCMutex \*\*  | *location_p* | )   |     |

Creates a new mutex or creates a no-op mutex if threads are not initialized.

May return NULL even if threads are initialized, indicating out-of-memory.

The returned mutex is suitable for use with condition variables.

Parameters  
|            |                                                       |
|------------|-------------------------------------------------------|
| location_p | the location of the new mutex, can return NULL on OOM |

Definition at line 80 of file dbus-threads.c.

References \_dbus_assert, dbus_threads_init_default(), and NULL.

Referenced by \_dbus_connection_new_for_transport().

## ◆ \_dbus_cmutex_unlock()

|                           |     |                |         |     |     |
|---------------------------|-----|----------------|---------|-----|-----|
| void \_dbus_cmutex_unlock | (   | DBusCMutex \*  | *mutex* | )   |     |

Unlocks a mutex.

Does nothing if passed a NULL pointer.

Returns  
TRUE on success

Definition at line 167 of file dbus-threads.c.

References NULL.

## ◆ \_dbus_condvar_free()

|                          |     |                 |        |     |     |
|--------------------------|-----|-----------------|--------|-----|-----|
| void \_dbus_condvar_free | (   | DBusCondVar \*  | *cond* | )   |     |

Frees a conditional variable created with dbus_condvar_new(); does nothing if passed a NULL pointer.

Definition at line 215 of file dbus-threads.c.

References NULL.

## ◆ \_dbus_condvar_free_at_location()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| void \_dbus_condvar_free_at_location | ( | DBusCondVar \*\*  | *location_p* | ) |  |

Frees a condition variable; does nothing if passed a NULL pointer.

Definition at line 227 of file dbus-threads.c.

References NULL.

Referenced by \_dbus_connection_new_for_transport().

## ◆ \_dbus_condvar_new()

|                                   |     |       |     |     |     |
|-----------------------------------|-----|-------|-----|-----|-----|
| DBusCondVar \* \_dbus_condvar_new | (   | void  |     | )   |     |

Creates a new condition variable using the function supplied to dbus_threads_init(), or creates a no-op condition variable if threads are not initialized.

May return NULL even if threads are initialized, indicating out-of-memory.

Returns  
new mutex or NULL

Definition at line 184 of file dbus-threads.c.

References dbus_threads_init_default(), and NULL.

Referenced by \_dbus_condvar_new_at_location().

## ◆ \_dbus_condvar_new_at_location()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| void \_dbus_condvar_new_at_location | ( | DBusCondVar \*\*  | *location_p* | ) |  |

This does the same thing as \_dbus_condvar_new.

It however gives another level of indirection by allocating a pointer to point to the condvar location; this used to be useful.

Returns  
the location of a new condvar or NULL on OOM

Definition at line 202 of file dbus-threads.c.

References \_dbus_assert, \_dbus_condvar_new(), and NULL.

Referenced by \_dbus_connection_new_for_transport().

## ◆ \_dbus_condvar_wait()

|                          |     |                 |          |
|--------------------------|-----|-----------------|----------|
| void \_dbus_condvar_wait | (   | DBusCondVar \*  | *cond*,  |
|                          |     | DBusCMutex \*   | *mutex*  |
|                          | )   |                 |          |

Atomically unlocks the mutex and waits for the conditions variable to be signalled.

Locks the mutex again before returning. Does nothing if passed a NULL pointer.

Definition at line 243 of file dbus-threads.c.

References NULL.

## ◆ \_dbus_condvar_wait_timeout()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_condvar_wait_timeout | ( | DBusCondVar \*  | *cond*, |
|  |  | DBusCMutex \*  | *mutex*, |
|  |  | int  | *timeout_milliseconds*  |
|  | ) |  |  |

Atomically unlocks the mutex and waits for the conditions variable to be signalled, or for a timeout.

Locks the mutex again before returning. Does nothing if passed a NULL pointer. Return value is FALSE if we timed out, TRUE otherwise.

Parameters  
|                      |                          |
|----------------------|--------------------------|
| cond                 | the condition variable   |
| mutex                | the mutex                |
| timeout_milliseconds | the maximum time to wait |

<!-- -->

Returns  
FALSE if the timeout occurred, TRUE if not

Definition at line 264 of file dbus-threads.c.

References NULL, and TRUE.

## ◆ \_dbus_condvar_wake_one()

|                              |     |                 |        |     |     |
|------------------------------|-----|-----------------|--------|-----|-----|
| void \_dbus_condvar_wake_one | (   | DBusCondVar \*  | *cond* | )   |     |

If there are threads waiting on the condition variable, wake up exactly one.

Does nothing if passed a NULL pointer.

Definition at line 281 of file dbus-threads.c.

References NULL.

## ◆ \_dbus_lock()

|                         |     |                 |        |     |     |
|-------------------------|-----|-----------------|--------|-----|-----|
| dbus_bool_t \_dbus_lock | (   | DBusGlobalLock  | *lock* | )   |     |

Definition at line 341 of file dbus-threads.c.

## ◆ \_dbus_rmutex_free_at_location()

|                                     |     |                  |              |     |     |
|-------------------------------------|-----|------------------|--------------|-----|-----|
| void \_dbus_rmutex_free_at_location | (   | DBusRMutex \*\*  | *location_p* | )   |     |

Frees a DBusRMutex; does nothing if passed a NULL pointer.

Definition at line 97 of file dbus-threads.c.

References NULL.

Referenced by \_dbus_connection_new_for_transport(), \_dbus_counter_unref(), \_dbus_server_finalize_base(), and \_dbus_server_init_base().

## ◆ \_dbus_rmutex_lock()

|                         |     |                |         |     |     |
|-------------------------|-----|----------------|---------|-----|-----|
| void \_dbus_rmutex_lock | (   | DBusRMutex \*  | *mutex* | )   |     |

Locks a mutex.

Does nothing if passed a NULL pointer. Locks may be recursive if threading implementation initialized recursive locks.

Definition at line 125 of file dbus-threads.c.

References NULL.

Referenced by \_dbus_counter_adjust_size(), \_dbus_counter_adjust_unix_fd(), \_dbus_counter_get_size_value(), \_dbus_counter_get_unix_fd_value(), \_dbus_counter_notify(), \_dbus_counter_ref(), \_dbus_counter_set_notify(), and \_dbus_counter_unref().

## ◆ \_dbus_rmutex_new_at_location()

|                                    |     |                  |              |     |     |
|------------------------------------|-----|------------------|--------------|-----|-----|
| void \_dbus_rmutex_new_at_location | (   | DBusRMutex \*\*  | *location_p* | )   |     |

Creates a new mutex or creates a no-op mutex if threads are not initialized.

May return NULL even if threads are initialized, indicating out-of-memory.

If possible, the mutex returned by this function is recursive, to avoid deadlocks. However, that cannot be relied on.

Parameters  
|            |                                                       |
|------------|-------------------------------------------------------|
| location_p | the location of the new mutex, can return NULL on OOM |

Definition at line 56 of file dbus-threads.c.

References \_dbus_assert, dbus_threads_init_default(), and NULL.

Referenced by \_dbus_connection_new_for_transport(), \_dbus_counter_new(), and \_dbus_server_init_base().

## ◆ \_dbus_rmutex_unlock()

|                           |     |                |         |     |     |
|---------------------------|-----|----------------|---------|-----|-----|
| void \_dbus_rmutex_unlock | (   | DBusRMutex \*  | *mutex* | )   |     |

Unlocks a mutex.

Does nothing if passed a NULL pointer.

Returns  
TRUE on success

Definition at line 153 of file dbus-threads.c.

References NULL.

Referenced by \_dbus_connection_unlock(), \_dbus_counter_adjust_size(), \_dbus_counter_adjust_unix_fd(), \_dbus_counter_get_size_value(), \_dbus_counter_get_unix_fd_value(), \_dbus_counter_notify(), \_dbus_counter_ref(), \_dbus_counter_set_notify(), and \_dbus_counter_unref().

## ◆ \_dbus_unlock()

|                    |     |                 |        |     |     |
|--------------------|-----|-----------------|--------|-----|-----|
| void \_dbus_unlock | (   | DBusGlobalLock  | *lock* | )   |     |

Definition at line 355 of file dbus-threads.c.
