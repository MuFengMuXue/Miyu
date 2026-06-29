DBusPendingCall

D-Bus low-level public API

Pending reply to a method call message. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="macros" class="groupheader"> Macros</h2></td>
</tr>
<tr id="r_ga21384c9c5b0da54f7d0a92012522f213" class="memitem:ga21384c9c5b0da54f7d0a92012522f213">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TIMEOUT_INFINITE   ((int) 0x7fffffff)</td>
</tr>
<tr class="memdesc:ga21384c9c5b0da54f7d0a92012522f213">
<td class="mdescLeft"> </td>
<td class="mdescRight">An integer constant representing an infinite timeout.<br />
</td>
</tr>
<tr class="separator:ga21384c9c5b0da54f7d0a92012522f213">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabdc138a303699e88756d6c5988a16b05" class="memitem:gabdc138a303699e88756d6c5988a16b05">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TIMEOUT_USE_DEFAULT   (-1)</td>
</tr>
<tr class="memdesc:gabdc138a303699e88756d6c5988a16b05">
<td class="mdescLeft"> </td>
<td class="mdescRight">An integer constant representing a request to use the default timeout.<br />
</td>
</tr>
<tr class="separator:gabdc138a303699e88756d6c5988a16b05">
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
<tr id="r_ga334f6c6621583e15fdaf1a3f93dd2221" class="memitem:ga334f6c6621583e15fdaf1a3f93dd2221">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusPendingCall * </td>
<td class="memItemRight" data-valign="bottom">dbus_pending_call_ref (DBusPendingCall *pending)</td>
</tr>
<tr class="memdesc:ga334f6c6621583e15fdaf1a3f93dd2221">
<td class="mdescLeft"> </td>
<td class="mdescRight">Increments the reference count on a pending call.<br />
</td>
</tr>
<tr class="separator:ga334f6c6621583e15fdaf1a3f93dd2221">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gadaba15a74ba4925cdef52d4791cd3147" class="memitem:gadaba15a74ba4925cdef52d4791cd3147">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_pending_call_unref (DBusPendingCall *pending)</td>
</tr>
<tr class="memdesc:gadaba15a74ba4925cdef52d4791cd3147">
<td class="mdescLeft"> </td>
<td class="mdescRight">Decrements the reference count on a pending call, freeing it if the count reaches 0.<br />
</td>
</tr>
<tr class="separator:gadaba15a74ba4925cdef52d4791cd3147">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga16b67b418b1dc27cfdda6b20f7447670" class="memitem:ga16b67b418b1dc27cfdda6b20f7447670">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_pending_call_set_notify (DBusPendingCall *pending, DBusPendingCallNotifyFunction function, void *user_data, DBusFreeFunction free_user_data)</td>
</tr>
<tr class="memdesc:ga16b67b418b1dc27cfdda6b20f7447670">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets a notification function to be called when the reply is received or the pending call times out.<br />
</td>
</tr>
<tr class="separator:ga16b67b418b1dc27cfdda6b20f7447670">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6530d18f891d3ca5f5df87ea7c2b155c" class="memitem:ga6530d18f891d3ca5f5df87ea7c2b155c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_pending_call_cancel (DBusPendingCall *pending)</td>
</tr>
<tr class="memdesc:ga6530d18f891d3ca5f5df87ea7c2b155c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Cancels the pending call, such that any reply or error received will just be ignored.<br />
</td>
</tr>
<tr class="separator:ga6530d18f891d3ca5f5df87ea7c2b155c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gacbf33ae8a1cc125628f9ea44d175c159" class="memitem:gacbf33ae8a1cc125628f9ea44d175c159">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_pending_call_get_completed (DBusPendingCall *pending)</td>
</tr>
<tr class="memdesc:gacbf33ae8a1cc125628f9ea44d175c159">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks whether the pending call has received a reply yet, or not.<br />
</td>
</tr>
<tr class="separator:gacbf33ae8a1cc125628f9ea44d175c159">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5a738928c2369fef093ce00658903d06" class="memitem:ga5a738928c2369fef093ce00658903d06">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMessage * </td>
<td class="memItemRight" data-valign="bottom">dbus_pending_call_steal_reply (DBusPendingCall *pending)</td>
</tr>
<tr class="memdesc:ga5a738928c2369fef093ce00658903d06">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the reply, or returns NULL if none has been received yet.<br />
</td>
</tr>
<tr class="separator:ga5a738928c2369fef093ce00658903d06">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga67b99f749a7f477c7b5d70f2acee5452" class="memitem:ga67b99f749a7f477c7b5d70f2acee5452">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_pending_call_block (DBusPendingCall *pending)</td>
</tr>
<tr class="memdesc:ga67b99f749a7f477c7b5d70f2acee5452">
<td class="mdescLeft"> </td>
<td class="mdescRight">Block until the pending call is completed.<br />
</td>
</tr>
<tr class="separator:ga67b99f749a7f477c7b5d70f2acee5452">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga95614dad0ada70e3a20d9878339e3109" class="memitem:ga95614dad0ada70e3a20d9878339e3109">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_pending_call_allocate_data_slot (dbus_int32_t *slot_p)</td>
</tr>
<tr class="memdesc:ga95614dad0ada70e3a20d9878339e3109">
<td class="mdescLeft"> </td>
<td class="mdescRight">Allocates an integer ID to be used for storing application-specific data on any DBusPendingCall.<br />
</td>
</tr>
<tr class="separator:ga95614dad0ada70e3a20d9878339e3109">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1eb6f342bba71b01266629f80be84617" class="memitem:ga1eb6f342bba71b01266629f80be84617">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_pending_call_free_data_slot (dbus_int32_t *slot_p)</td>
</tr>
<tr class="memdesc:ga1eb6f342bba71b01266629f80be84617">
<td class="mdescLeft"> </td>
<td class="mdescRight">Deallocates a global ID for DBusPendingCall data slots.<br />
</td>
</tr>
<tr class="separator:ga1eb6f342bba71b01266629f80be84617">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9295e7e602c41c6501b69bc995907e1b" class="memitem:ga9295e7e602c41c6501b69bc995907e1b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_pending_call_set_data (DBusPendingCall *pending, dbus_int32_t slot, void *data, DBusFreeFunction free_data_func)</td>
</tr>
<tr class="memdesc:ga9295e7e602c41c6501b69bc995907e1b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Stores a pointer on a DBusPendingCall, along with an optional function to be used for freeing the data when the data is set again, or when the pending call is finalized.<br />
</td>
</tr>
<tr class="separator:ga9295e7e602c41c6501b69bc995907e1b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5749f73b7ec7a8fe4f2e6a839e292806" class="memitem:ga5749f73b7ec7a8fe4f2e6a839e292806">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">dbus_pending_call_get_data (DBusPendingCall *pending, dbus_int32_t slot)</td>
</tr>
<tr class="memdesc:ga5749f73b7ec7a8fe4f2e6a839e292806">
<td class="mdescLeft"> </td>
<td class="mdescRight">Retrieves data previously set with dbus_pending_call_set_data().<br />
</td>
</tr>
<tr class="separator:ga5749f73b7ec7a8fe4f2e6a839e292806">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Pending reply to a method call message.

A DBusPendingCall is an object representing an expected reply. A DBusPendingCall can be created when you send a message that should have a reply.

## Macro Definition Documentation

## ◆ DBUS_TIMEOUT_INFINITE

|                                                     |
|-----------------------------------------------------|
| \#define DBUS_TIMEOUT_INFINITE   ((int) 0x7fffffff) |

An integer constant representing an infinite timeout.

This has the numeric value 0x7fffffff (the largest 32-bit signed integer).

For source compatibility with D-Bus versions earlier than 1.4.12, use 0x7fffffff, or INT32_MAX (assuming your platform has it).

Definition at line 43 of file dbus-pending-call.h.

## ◆ DBUS_TIMEOUT_USE_DEFAULT

|                                          |
|------------------------------------------|
| \#define DBUS_TIMEOUT_USE_DEFAULT   (-1) |

An integer constant representing a request to use the default timeout.

This has numeric value -1.

For source compatibility with D-Bus versions earlier than 1.4.12, use a literal -1.

Definition at line 44 of file dbus-pending-call.h.

## Function Documentation

## ◆ dbus_pending_call_allocate_data_slot()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_pending_call_allocate_data_slot | ( | dbus_int32_t \*  | *slot_p* | ) |  |

Allocates an integer ID to be used for storing application-specific data on any DBusPendingCall.

The allocated ID may then be used with dbus_pending_call_set_data() and dbus_pending_call_get_data(). The passed-in slot must be initialized to -1, and is filled in with the slot ID. If the passed-in slot is not -1, it's assumed to be already allocated, and its refcount is incremented.

The allocated slot is global, i.e. all DBusPendingCall objects will have a slot with the given integer ID reserved.

Parameters  
|        |                                               |
|--------|-----------------------------------------------|
| slot_p | address of a global variable storing the slot |

<!-- -->

Returns  
FALSE on failure (no memory)

Definition at line 788 of file dbus-pending-call.c.

References \_dbus_data_slot_allocator_alloc(), FALSE, and NULL.

Referenced by \_dbus_pending_call_new_unlocked().

## ◆ dbus_pending_call_block()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT void dbus_pending_call_block | ( | DBusPendingCall \*  | *pending* | ) |  |

Block until the pending call is completed.

The blocking is as with dbus_connection_send_with_reply_and_block(); it does not enter the main loop or process other messages, it simply waits for the reply in question.

If the pending call is already completed, this function returns immediately.

Parameters  
|         |                  |
|---------|------------------|
| pending | the pending call |

Definition at line 766 of file dbus-pending-call.c.

References \_dbus_connection_block_pending_call(), and NULL.

Referenced by dbus_connection_send_with_reply_and_block().

## ◆ dbus_pending_call_cancel()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT void dbus_pending_call_cancel | ( | DBusPendingCall \*  | *pending* | ) |  |

Cancels the pending call, such that any reply or error received will just be ignored.

Drops the dbus library's internal reference to the DBusPendingCall so will free the call if nobody else is holding a reference. However you usually get a reference from dbus_connection_send_with_reply() so probably your app owns a ref also.

Note that canceling a pending call will *not* simulate a timed-out call; if a call times out, then a timeout error reply is received. If you cancel the call, no reply is received unless the the reply was already received before you canceled.

Parameters  
|         |                  |
|---------|------------------|
| pending | the pending call |

Definition at line 692 of file dbus-pending-call.c.

References \_dbus_connection_remove_pending_call(), connection, and NULL.

## ◆ dbus_pending_call_free_data_slot()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT void dbus_pending_call_free_data_slot | ( | dbus_int32_t \*  | *slot_p* | ) |  |

Deallocates a global ID for DBusPendingCall data slots.

dbus_pending_call_get_data() and dbus_pending_call_set_data() may no longer be used with this slot. Existing data stored on existing DBusPendingCall objects will be freed when the DBusPendingCall is finalized, but may not be retrieved (and may only be replaced if someone else reallocates the slot). When the refcount on the passed-in slot reaches 0, it is set to -1.

Parameters  
|        |                                        |
|--------|----------------------------------------|
| slot_p | address storing the slot to deallocate |

Definition at line 808 of file dbus-pending-call.c.

References \_dbus_data_slot_allocator_free(), and NULL.

Referenced by \_dbus_pending_call_new_unlocked().

## ◆ dbus_pending_call_get_completed()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_pending_call_get_completed | ( | DBusPendingCall \*  | *pending* | ) |  |

Checks whether the pending call has received a reply yet, or not.

Parameters  
|         |                  |
|---------|------------------|
| pending | the pending call |

<!-- -->

Returns  
TRUE if a reply has been received

Definition at line 708 of file dbus-pending-call.c.

References completed, connection, CONNECTION_LOCK, CONNECTION_UNLOCK, FALSE, and NULL.

Referenced by \_dbus_connection_block_pending_call().

## ◆ dbus_pending_call_get_data()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT void \* dbus_pending_call_get_data | ( | DBusPendingCall \*  | *pending*, |
|  |  | dbus_int32_t  | *slot*  |
|  | ) |  |  |

Retrieves data previously set with dbus_pending_call_set_data().

The slot must still be allocated (must not have been freed).

Parameters  
|         |                           |
|---------|---------------------------|
| pending | the pending_call          |
| slot    | the slot to get data from |

<!-- -->

Returns  
the data, or NULL if not found

Definition at line 856 of file dbus-pending-call.c.

References \_dbus_data_slot_list_get(), connection, CONNECTION_LOCK, CONNECTION_UNLOCK, NULL, and slot_list.

Referenced by \_dbus_pending_call_finish_completion().

## ◆ dbus_pending_call_ref()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT DBusPendingCall \* dbus_pending_call_ref | ( | DBusPendingCall \*  | *pending* | ) |  |

Increments the reference count on a pending call.

Parameters  
|         |                         |
|---------|-------------------------|
| pending | the pending call object |

<!-- -->

Returns  
the pending call object

Definition at line 606 of file dbus-pending-call.c.

References \_dbus_atomic_inc(), NULL, and refcount.

Referenced by \_dbus_connection_block_pending_call().

## ◆ dbus_pending_call_set_data()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_pending_call_set_data | ( | DBusPendingCall \*  | *pending*, |
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

Definition at line 830 of file dbus-pending-call.c.

References \_dbus_pending_call_set_data_unlocked(), connection, CONNECTION_LOCK, CONNECTION_UNLOCK, FALSE, and NULL.

## ◆ dbus_pending_call_set_notify()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_pending_call_set_notify | ( | DBusPendingCall \*  | *pending*, |
|  |  | DBusPendingCallNotifyFunction  | *function*, |
|  |  | void \*  | *user_data*, |
|  |  | DBusFreeFunction  | *free_user_data*  |
|  | ) |  |  |

Sets a notification function to be called when the reply is received or the pending call times out.

Parameters  
|                |                                   |
|----------------|-----------------------------------|
| pending        | the pending call                  |
| function       | notifier function                 |
| user_data      | data to pass to notifier function |
| free_user_data | function to free the user data    |

<!-- -->

Returns  
FALSE if not enough memory

Definition at line 651 of file dbus-pending-call.c.

References \_dbus_pending_call_set_data_unlocked(), connection, CONNECTION_LOCK, CONNECTION_UNLOCK, FALSE, function, NULL, and TRUE.

## ◆ dbus_pending_call_steal_reply()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT DBusMessage \* dbus_pending_call_steal_reply | ( | DBusPendingCall \*  | *pending* | ) |  |

Gets the reply, or returns NULL if none has been received yet.

Ownership of the reply message passes to the caller. This function can only be called once per pending call, since the reply message is tranferred to the caller.

Parameters  
|         |                  |
|---------|------------------|
| pending | the pending call |

<!-- -->

Returns  
the reply message or NULL.

Definition at line 731 of file dbus-pending-call.c.

References completed, connection, CONNECTION_LOCK, CONNECTION_UNLOCK, NULL, and reply.

Referenced by dbus_connection_send_with_reply_and_block().

## ◆ dbus_pending_call_unref()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT void dbus_pending_call_unref | ( | DBusPendingCall \*  | *pending* | ) |  |

Decrements the reference count on a pending call, freeing it if the count reaches 0.

Parameters  
|         |                         |
|---------|-------------------------|
| pending | the pending call object |

Definition at line 626 of file dbus-pending-call.c.

References \_dbus_atomic_dec(), NULL, and refcount.

Referenced by \_dbus_connection_block_pending_call(), dbus_connection_send_with_reply(), and dbus_connection_send_with_reply_and_block().
