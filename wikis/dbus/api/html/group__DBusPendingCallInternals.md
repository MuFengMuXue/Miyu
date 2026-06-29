DBusPendingCall implementation details

D-Bus secret internal implementation details

DBusPendingCall private implementation details. More...

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
<td class="memItemRight" data-valign="bottom">DBusPendingCall</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Implementation details of DBusPendingCall - all fields are private. More...<br />
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
<tr id="r_ga99fcbae5b8f2ed2cc019cab85f63d4e4" class="memitem:ga99fcbae5b8f2ed2cc019cab85f63d4e4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">CONNECTION_LOCK(connection)   _dbus_connection_lock(connection)</td>
</tr>
<tr class="memdesc:ga99fcbae5b8f2ed2cc019cab85f63d4e4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Internals of DBusPendingCall.<br />
</td>
</tr>
<tr class="separator:ga99fcbae5b8f2ed2cc019cab85f63d4e4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab21a3014fa3cacf2a580e079321abc33" class="memitem:gab21a3014fa3cacf2a580e079321abc33">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">CONNECTION_UNLOCK(connection)   _dbus_connection_unlock(connection)</td>
</tr>
<tr class="memdesc:gab21a3014fa3cacf2a580e079321abc33">
<td class="mdescLeft"> </td>
<td class="mdescRight">shorter and more visible way to write _dbus_connection_unlock()<br />
</td>
</tr>
<tr class="separator:gab21a3014fa3cacf2a580e079321abc33">
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
<tr id="r_ga91a35bfe91681ab523bdcf652e19620d" class="memitem:ga91a35bfe91681ab523bdcf652e19620d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusPendingCall * </td>
<td class="memItemRight" data-valign="bottom">_dbus_pending_call_new_unlocked (DBusConnection *connection, int timeout_milliseconds, DBusTimeoutHandler timeout_handler)</td>
</tr>
<tr class="memdesc:ga91a35bfe91681ab523bdcf652e19620d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new pending reply object.<br />
</td>
</tr>
<tr class="separator:ga91a35bfe91681ab523bdcf652e19620d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4b8cc560549160aecd924037a872009d" class="memitem:ga4b8cc560549160aecd924037a872009d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_pending_call_set_reply_unlocked (DBusPendingCall *pending, DBusMessage *message)</td>
</tr>
<tr class="memdesc:ga4b8cc560549160aecd924037a872009d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the reply of a pending call with the given message, or if the message is NULL, by timing out the pending call.<br />
</td>
</tr>
<tr class="separator:ga4b8cc560549160aecd924037a872009d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad20c017e5810377112dc0ab9db9ebeb2" class="memitem:gad20c017e5810377112dc0ab9db9ebeb2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_pending_call_start_completion_unlocked (DBusPendingCall *pending)</td>
</tr>
<tr class="memdesc:gad20c017e5810377112dc0ab9db9ebeb2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the pending call to completed.<br />
</td>
</tr>
<tr class="separator:gad20c017e5810377112dc0ab9db9ebeb2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga04ada81d6ee6ba81bbfa7abbde440eb5" class="memitem:ga04ada81d6ee6ba81bbfa7abbde440eb5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_pending_call_finish_completion (DBusPendingCall *pending)</td>
</tr>
<tr class="memdesc:ga04ada81d6ee6ba81bbfa7abbde440eb5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Call the notifier function for the pending call.<br />
</td>
</tr>
<tr class="separator:ga04ada81d6ee6ba81bbfa7abbde440eb5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1bc4de7652108d0629522a4e3adffcab" class="memitem:ga1bc4de7652108d0629522a4e3adffcab">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_pending_call_queue_timeout_error_unlocked (DBusPendingCall *pending, DBusConnection *connection)</td>
</tr>
<tr class="memdesc:ga1bc4de7652108d0629522a4e3adffcab">
<td class="mdescLeft"> </td>
<td class="mdescRight">If the pending call hasn't been timed out, add its timeout error reply to the connection's incoming message queue.<br />
</td>
</tr>
<tr class="separator:ga1bc4de7652108d0629522a4e3adffcab">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf1e630b966722af540502329ed028254" class="memitem:gaf1e630b966722af540502329ed028254">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_pending_call_is_timeout_added_unlocked (DBusPendingCall *pending)</td>
</tr>
<tr class="memdesc:gaf1e630b966722af540502329ed028254">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks to see if a timeout has been added.<br />
</td>
</tr>
<tr class="separator:gaf1e630b966722af540502329ed028254">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gafea13f8b9977d341e41201c407adea2a" class="memitem:gafea13f8b9977d341e41201c407adea2a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_pending_call_set_timeout_added_unlocked (DBusPendingCall *pending, dbus_bool_t is_added)</td>
</tr>
<tr class="memdesc:gafea13f8b9977d341e41201c407adea2a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets wether the timeout has been added.<br />
</td>
</tr>
<tr class="separator:gafea13f8b9977d341e41201c407adea2a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gafc74e99e54c9b3c05a399ce0449d4278" class="memitem:gafc74e99e54c9b3c05a399ce0449d4278">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusTimeout * </td>
<td class="memItemRight" data-valign="bottom">_dbus_pending_call_get_timeout_unlocked (DBusPendingCall *pending)</td>
</tr>
<tr class="memdesc:gafc74e99e54c9b3c05a399ce0449d4278">
<td class="mdescLeft"> </td>
<td class="mdescRight">Retrives the timeout.<br />
</td>
</tr>
<tr class="separator:gafc74e99e54c9b3c05a399ce0449d4278">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf5f3df36149bfe55d824eb08d00768fc" class="memitem:gaf5f3df36149bfe55d824eb08d00768fc">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_pending_call_get_reply_serial_unlocked (DBusPendingCall *pending)</td>
</tr>
<tr class="memdesc:gaf5f3df36149bfe55d824eb08d00768fc">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the reply's serial number.<br />
</td>
</tr>
<tr class="separator:gaf5f3df36149bfe55d824eb08d00768fc">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4c0325356df50a5dc103bdab3e7148f3" class="memitem:ga4c0325356df50a5dc103bdab3e7148f3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_pending_call_set_reply_serial_unlocked (DBusPendingCall *pending, dbus_uint32_t serial)</td>
</tr>
<tr class="memdesc:ga4c0325356df50a5dc103bdab3e7148f3">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the reply's serial number.<br />
</td>
</tr>
<tr class="separator:ga4c0325356df50a5dc103bdab3e7148f3">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga104ded51acbeda6c990ed59c9dafc674" class="memitem:ga104ded51acbeda6c990ed59c9dafc674">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusConnection * </td>
<td class="memItemRight" data-valign="bottom">_dbus_pending_call_get_connection_and_lock (DBusPendingCall *pending)</td>
</tr>
<tr class="memdesc:ga104ded51acbeda6c990ed59c9dafc674">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the connection associated with this pending call.<br />
</td>
</tr>
<tr class="separator:ga104ded51acbeda6c990ed59c9dafc674">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gafa9a3acbae039a014a1ac10ce9090d49" class="memitem:gafa9a3acbae039a014a1ac10ce9090d49">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusConnection * </td>
<td class="memItemRight" data-valign="bottom">_dbus_pending_call_get_connection_unlocked (DBusPendingCall *pending)</td>
</tr>
<tr class="memdesc:gafa9a3acbae039a014a1ac10ce9090d49">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the connection associated with this pending call.<br />
</td>
</tr>
<tr class="separator:gafa9a3acbae039a014a1ac10ce9090d49">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9901fc4c5fd2db9bf1ce2dcc9abf55fc" class="memitem:ga9901fc4c5fd2db9bf1ce2dcc9abf55fc">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_pending_call_set_timeout_error_unlocked (DBusPendingCall *pending, DBusMessage *message, dbus_uint32_t serial)</td>
</tr>
<tr class="memdesc:ga9901fc4c5fd2db9bf1ce2dcc9abf55fc">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the reply message associated with the pending call to a timeout error.<br />
</td>
</tr>
<tr class="separator:ga9901fc4c5fd2db9bf1ce2dcc9abf55fc">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga14101a1f571d30bb7273c4ef014764e1" class="memitem:ga14101a1f571d30bb7273c4ef014764e1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusPendingCall * </td>
<td class="memItemRight" data-valign="bottom">_dbus_pending_call_ref_unlocked (DBusPendingCall *pending)</td>
</tr>
<tr class="memdesc:ga14101a1f571d30bb7273c4ef014764e1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Increments the reference count on a pending call, while the lock on its connection is already held.<br />
</td>
</tr>
<tr class="separator:ga14101a1f571d30bb7273c4ef014764e1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga26f09beed0dd6323cca0452abf344567" class="memitem:ga26f09beed0dd6323cca0452abf344567">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_pending_call_unref_and_unlock (DBusPendingCall *pending)</td>
</tr>
<tr class="memdesc:ga26f09beed0dd6323cca0452abf344567">
<td class="mdescLeft"> </td>
<td class="mdescRight">Decrements the reference count on a pending call, freeing it if the count reaches 0.<br />
</td>
</tr>
<tr class="separator:ga26f09beed0dd6323cca0452abf344567">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga37bef4359b3c29629a57f5fe480690a1" class="memitem:ga37bef4359b3c29629a57f5fe480690a1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_pending_call_get_completed_unlocked (DBusPendingCall *pending)</td>
</tr>
<tr class="memdesc:ga37bef4359b3c29629a57f5fe480690a1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks whether the pending call has received a reply yet, or not.<br />
</td>
</tr>
<tr class="separator:ga37bef4359b3c29629a57f5fe480690a1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7d4196ca35b8df842c05a02dbb71c269" class="memitem:ga7d4196ca35b8df842c05a02dbb71c269">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_pending_call_set_data_unlocked (DBusPendingCall *pending, dbus_int32_t slot, void *data, DBusFreeFunction free_data_func)</td>
</tr>
<tr class="memdesc:ga7d4196ca35b8df842c05a02dbb71c269">
<td class="mdescLeft"> </td>
<td class="mdescRight">Stores a pointer on a DBusPendingCall, along with an optional function to be used for freeing the data when the data is set again, or when the pending call is finalized.<br />
</td>
</tr>
<tr class="separator:ga7d4196ca35b8df842c05a02dbb71c269">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

DBusPendingCall private implementation details.

The guts of DBusPendingCall and its methods.

## Macro Definition Documentation

## ◆ CONNECTION_LOCK

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| \#define CONNECTION_LOCK | ( |   | connection | ) |    \_dbus_connection_lock(connection) |

Internals of DBusPendingCall.

Opaque object representing a reply message that we're waiting for. shorter and more visible way to write \_dbus_connection_lock()

Definition at line 55 of file dbus-pending-call.c.

## ◆ CONNECTION_UNLOCK

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| \#define CONNECTION_UNLOCK | ( |   | connection | ) |    \_dbus_connection_unlock(connection) |

shorter and more visible way to write \_dbus_connection_unlock()

Definition at line 59 of file dbus-pending-call.c.

## Function Documentation

## ◆ \_dbus_pending_call_finish_completion()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| void \_dbus_pending_call_finish_completion | ( | DBusPendingCall \*  | *pending* | ) |  |

Call the notifier function for the pending call.

This method must be called after the connection lock has been released, and must be paired with a call to \_dbus_pending_call_start_completion_unlocked().

Parameters  
|         |                  |
|---------|------------------|
| pending | the pending call |

Definition at line 235 of file dbus-pending-call.c.

References \_dbus_assert, DBusPendingCall::completed, dbus_pending_call_get_data(), and DBusPendingCall::function.

## ◆ \_dbus_pending_call_get_completed_unlocked()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_pending_call_get_completed_unlocked | ( | DBusPendingCall \*  | *pending* | ) |  |

Checks whether the pending call has received a reply yet, or not.

Assumes connection lock is held.

Parameters  
|         |                  |
|---------|------------------|
| pending | the pending call |

<!-- -->

Returns  
TRUE if a reply has been received

Definition at line 509 of file dbus-pending-call.c.

References DBusPendingCall::completed.

Referenced by \_dbus_connection_block_pending_call(), and \_dbus_connection_do_iteration_unlocked().

## ◆ \_dbus_pending_call_get_connection_and_lock()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBusConnection \* \_dbus_pending_call_get_connection_and_lock | ( | DBusPendingCall \*  | *pending* | ) |  |

Gets the connection associated with this pending call.

Parameters  
|         |                  |
|---------|------------------|
| pending | the pending_call |

<!-- -->

Returns  
the connection associated with the pending call

Definition at line 352 of file dbus-pending-call.c.

References \_dbus_assert, DBusPendingCall::connection, CONNECTION_LOCK, and NULL.

Referenced by \_dbus_connection_block_pending_call().

## ◆ \_dbus_pending_call_get_connection_unlocked()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBusConnection \* \_dbus_pending_call_get_connection_unlocked | ( | DBusPendingCall \*  | *pending* | ) |  |

Gets the connection associated with this pending call.

Parameters  
|         |                  |
|---------|------------------|
| pending | the pending_call |

<!-- -->

Returns  
the connection associated with the pending call

Definition at line 367 of file dbus-pending-call.c.

References \_dbus_assert, DBusPendingCall::connection, and NULL.

## ◆ \_dbus_pending_call_get_reply_serial_unlocked()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_uint32_t \_dbus_pending_call_get_reply_serial_unlocked | ( | DBusPendingCall \*  | *pending* | ) |  |

Gets the reply's serial number.

Parameters  
|         |                  |
|---------|------------------|
| pending | the pending_call |

<!-- -->

Returns  
a serial number for the reply or 0

Definition at line 322 of file dbus-pending-call.c.

References \_dbus_assert, NULL, and DBusPendingCall::reply_serial.

Referenced by \_dbus_connection_block_pending_call(), and \_dbus_connection_do_iteration_unlocked().

## ◆ \_dbus_pending_call_get_timeout_unlocked()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBusTimeout \* \_dbus_pending_call_get_timeout_unlocked | ( | DBusPendingCall \*  | *pending* | ) |  |

Retrives the timeout.

Parameters  
|         |                  |
|---------|------------------|
| pending | the pending_call |

<!-- -->

Returns  
a timeout object or NULL if call has no timeout

Definition at line 308 of file dbus-pending-call.c.

References \_dbus_assert, NULL, and DBusPendingCall::timeout.

Referenced by \_dbus_connection_block_pending_call(), and \_dbus_connection_queue_received_message_link().

## ◆ \_dbus_pending_call_is_timeout_added_unlocked()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_pending_call_is_timeout_added_unlocked | ( | DBusPendingCall \*  | *pending* | ) |  |

Checks to see if a timeout has been added.

Parameters  
|         |                  |
|---------|------------------|
| pending | the pending_call |

<!-- -->

Returns  
TRUE if there is a timeout or FALSE if not

Definition at line 277 of file dbus-pending-call.c.

References \_dbus_assert, NULL, and DBusPendingCall::timeout_added.

Referenced by \_dbus_connection_queue_received_message_link().

## ◆ \_dbus_pending_call_new_unlocked()

|  |  |  |  |
|----|----|----|----|
| DBusPendingCall \* \_dbus_pending_call_new_unlocked | ( | DBusConnection \*  | *connection*, |
|  |  | int  | *timeout_milliseconds*, |
|  |  | DBusTimeoutHandler  | *timeout_handler*  |
|  | ) |  |  |

Creates a new pending reply object.

Parameters  
|  |  |
|----|----|
| connection | connection where reply will arrive |
| timeout_milliseconds | length of timeout, -1 (or DBUS_TIMEOUT_USE_DEFAULT) for default, DBUS_TIMEOUT_INFINITE for no timeout |
| timeout_handler | timeout handler, takes pending call as data |

<!-- -->

Returns  
a new DBusPendingCall or NULL if no memory.

Definition at line 120 of file dbus-pending-call.c.

References \_dbus_assert, \_dbus_atomic_inc(), \_dbus_connection_ref_unlocked(), \_dbus_data_slot_list_init(), \_dbus_timeout_new(), DBusPendingCall::connection, dbus_free(), dbus_new0, dbus_pending_call_allocate_data_slot(), dbus_pending_call_free_data_slot(), DBUS_TIMEOUT_INFINITE, NULL, DBusPendingCall::refcount, DBusPendingCall::slot_list, and DBusPendingCall::timeout.

Referenced by dbus_connection_send_with_reply().

## ◆ \_dbus_pending_call_queue_timeout_error_unlocked()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_pending_call_queue_timeout_error_unlocked | ( | DBusPendingCall \*  | *pending*, |
|  |  | DBusConnection \*  | *connection*  |
|  | ) |  |  |

If the pending call hasn't been timed out, add its timeout error reply to the connection's incoming message queue.

Parameters  
|            |                                     |
|------------|-------------------------------------|
| pending    | the pending call                    |
| connection | the connection the call was sent to |

Definition at line 257 of file dbus-pending-call.c.

References \_dbus_assert, \_dbus_connection_queue_synthesized_message_link(), DBusPendingCall::connection, NULL, and DBusPendingCall::timeout_link.

## ◆ \_dbus_pending_call_ref_unlocked()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBusPendingCall \* \_dbus_pending_call_ref_unlocked | ( | DBusPendingCall \*  | *pending* | ) |  |

Increments the reference count on a pending call, while the lock on its connection is already held.

Parameters  
|         |                         |
|---------|-------------------------|
| pending | the pending call object |

<!-- -->

Returns  
the pending call object

Definition at line 423 of file dbus-pending-call.c.

References \_dbus_atomic_inc(), and DBusPendingCall::refcount.

## ◆ \_dbus_pending_call_set_data_unlocked()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_pending_call_set_data_unlocked | ( | DBusPendingCall \*  | *pending*, |
|  |  | dbus_int32_t  | *slot*, |
|  |  | void \*  | *data*, |
|  |  | DBusFreeFunction  | *free_data_func*  |
|  | ) |  |  |

Stores a pointer on a DBusPendingCall, along with an optional function to be used for freeing the data when the data is set again, or when the pending call is finalized.

The slot number must have been allocated with dbus_pending_call_allocate_data_slot().

Parameters  
|                |                                 |
|----------------|---------------------------------|
| pending        | the pending_call                |
| slot           | the slot number                 |
| data           | the data to store               |
| free_data_func | finalizer function for the data |

<!-- -->

Returns  
TRUE if there was enough memory to store the data

Definition at line 531 of file dbus-pending-call.c.

References \_dbus_data_slot_list_set(), DBusPendingCall::connection, CONNECTION_LOCK, CONNECTION_UNLOCK, and DBusPendingCall::slot_list.

Referenced by dbus_pending_call_set_data(), and dbus_pending_call_set_notify().

## ◆ \_dbus_pending_call_set_reply_serial_unlocked()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_pending_call_set_reply_serial_unlocked | ( | DBusPendingCall \*  | *pending*, |
|  |  | dbus_uint32_t  | *serial*  |
|  | ) |  |  |

Sets the reply's serial number.

Parameters  
|         |                   |
|---------|-------------------|
| pending | the pending_call  |
| serial  | the serial number |

Definition at line 336 of file dbus-pending-call.c.

References \_dbus_assert, NULL, and DBusPendingCall::reply_serial.

Referenced by \_dbus_pending_call_set_timeout_error_unlocked().

## ◆ \_dbus_pending_call_set_reply_unlocked()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_pending_call_set_reply_unlocked | ( | DBusPendingCall \*  | *pending*, |
|  |  | DBusMessage \*  | *message*  |
|  | ) |  |  |

Sets the reply of a pending call with the given message, or if the message is NULL, by timing out the pending call.

Parameters  
|  |  |
|----|----|
| pending | the pending call |
| message | the message to complete the call with, or NULL to time out the call |

Definition at line 183 of file dbus-pending-call.c.

References \_dbus_assert, \_dbus_list_clear(), DBusList::data, dbus_message_get_reply_serial(), dbus_message_get_type(), dbus_message_ref(), DBUS_MESSAGE_TYPE_ERROR, DBUS_MESSAGE_TYPE_METHOD_RETURN, NULL, DBusPendingCall::reply, DBusPendingCall::reply_serial, and DBusPendingCall::timeout_link.

## ◆ \_dbus_pending_call_set_timeout_added_unlocked()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_pending_call_set_timeout_added_unlocked | ( | DBusPendingCall \*  | *pending*, |
|  |  | dbus_bool_t  | *is_added*  |
|  | ) |  |  |

Sets wether the timeout has been added.

Parameters  
|          |                                   |
|----------|-----------------------------------|
| pending  | the pending_call                  |
| is_added | whether or not a timeout is added |

Definition at line 292 of file dbus-pending-call.c.

References \_dbus_assert, NULL, and DBusPendingCall::timeout_added.

Referenced by \_dbus_connection_queue_received_message_link().

## ◆ \_dbus_pending_call_set_timeout_error_unlocked()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_pending_call_set_timeout_error_unlocked | ( | DBusPendingCall \*  | *pending*, |
|  |  | DBusMessage \*  | *message*, |
|  |  | dbus_uint32_t  | *serial*  |
|  | ) |  |  |

Sets the reply message associated with the pending call to a timeout error.

Parameters  
|         |                                               |
|---------|-----------------------------------------------|
| pending | the pending_call                              |
| message | the message we are sending the error reply to |
| serial  | serial number for the reply                   |

<!-- -->

Returns  
FALSE on OOM

Definition at line 383 of file dbus-pending-call.c.

References \_dbus_list_alloc_link(), \_dbus_pending_call_set_reply_serial_unlocked(), DBUS_ERROR_NO_REPLY, dbus_message_new_error(), dbus_message_unref(), FALSE, NULL, DBusPendingCall::timeout_link, and TRUE.

Referenced by dbus_connection_send_with_reply().

## ◆ \_dbus_pending_call_start_completion_unlocked()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| void \_dbus_pending_call_start_completion_unlocked | ( | DBusPendingCall \*  | *pending* | ) |  |

Sets the pending call to completed.

This method is called with the connection lock held, to protect pending-\>completed. It must be paired with a call to \_dbus_pending_call_finish_completion() after the connection lock has been released.

Parameters  
|         |                  |
|---------|------------------|
| pending | the pending call |

Definition at line 218 of file dbus-pending-call.c.

References \_dbus_assert, DBusPendingCall::completed, and TRUE.

## ◆ \_dbus_pending_call_unref_and_unlock()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| void \_dbus_pending_call_unref_and_unlock | ( | DBusPendingCall \*  | *pending* | ) |  |

Decrements the reference count on a pending call, freeing it if the count reaches 0.

Assumes connection lock is already held.

Parameters  
|         |                         |
|---------|-------------------------|
| pending | the pending call object |

Definition at line 486 of file dbus-pending-call.c.

References \_dbus_assert, \_dbus_atomic_dec(), DBusPendingCall::connection, CONNECTION_UNLOCK, and DBusPendingCall::refcount.
