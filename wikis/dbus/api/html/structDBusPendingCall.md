DBusPendingCall Struct Reference

D-Bus secret internal implementation details » DBusPendingCall implementation details

Implementation details of DBusPendingCall - all fields are private. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a952e3c744db112d49bbaffe0fe45048d" class="memitem:a952e3c744db112d49bbaffe0fe45048d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusAtomic </td>
<td class="memItemRight" data-valign="bottom">refcount</td>
</tr>
<tr class="memdesc:a952e3c744db112d49bbaffe0fe45048d">
<td class="mdescLeft"> </td>
<td class="mdescRight">reference count<br />
</td>
</tr>
<tr class="separator:a952e3c744db112d49bbaffe0fe45048d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ad1b1c044ae4f9f94b05b4a5eb2f3917a" class="memitem:ad1b1c044ae4f9f94b05b4a5eb2f3917a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusDataSlotList </td>
<td class="memItemRight" data-valign="bottom">slot_list</td>
</tr>
<tr class="memdesc:ad1b1c044ae4f9f94b05b4a5eb2f3917a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Data stored by allocated integer ID.<br />
</td>
</tr>
<tr class="separator:ad1b1c044ae4f9f94b05b4a5eb2f3917a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a057527b236383b2f3436f4ed5ddc2d4b" class="memitem:a057527b236383b2f3436f4ed5ddc2d4b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusPendingCallNotifyFunction </td>
<td class="memItemRight" data-valign="bottom">function</td>
</tr>
<tr class="memdesc:a057527b236383b2f3436f4ed5ddc2d4b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Notifier when reply arrives.<br />
</td>
</tr>
<tr class="separator:a057527b236383b2f3436f4ed5ddc2d4b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_adaee5e70f04e503f25b8c4202fd4747f" class="memitem:adaee5e70f04e503f25b8c4202fd4747f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusConnection * </td>
<td class="memItemRight" data-valign="bottom">connection</td>
</tr>
<tr class="memdesc:adaee5e70f04e503f25b8c4202fd4747f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Connections we're associated with.<br />
</td>
</tr>
<tr class="separator:adaee5e70f04e503f25b8c4202fd4747f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a30c043b7cc468ab01fce6596dac1da57" class="memitem:a30c043b7cc468ab01fce6596dac1da57">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMessage * </td>
<td class="memItemRight" data-valign="bottom">reply</td>
</tr>
<tr class="memdesc:a30c043b7cc468ab01fce6596dac1da57">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reply (after we've received it)<br />
</td>
</tr>
<tr class="separator:a30c043b7cc468ab01fce6596dac1da57">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_af9dea193bf4ab249c280ff6abcb743f8" class="memitem:af9dea193bf4ab249c280ff6abcb743f8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusTimeout * </td>
<td class="memItemRight" data-valign="bottom">timeout</td>
</tr>
<tr class="memdesc:af9dea193bf4ab249c280ff6abcb743f8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Timeout.<br />
</td>
</tr>
<tr class="separator:af9dea193bf4ab249c280ff6abcb743f8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a85252a169617a86f80462bfb53ca2f7c" class="memitem:a85252a169617a86f80462bfb53ca2f7c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusList * </td>
<td class="memItemRight" data-valign="bottom">timeout_link</td>
</tr>
<tr class="memdesc:a85252a169617a86f80462bfb53ca2f7c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Preallocated timeout response.<br />
</td>
</tr>
<tr class="separator:a85252a169617a86f80462bfb53ca2f7c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ab6234d38b3f3ca8ff5de2d3cce8c3100" class="memitem:ab6234d38b3f3ca8ff5de2d3cce8c3100">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">reply_serial</td>
</tr>
<tr class="memdesc:ab6234d38b3f3ca8ff5de2d3cce8c3100">
<td class="mdescLeft"> </td>
<td class="mdescRight">Expected serial of reply.<br />
</td>
</tr>
<tr class="separator:ab6234d38b3f3ca8ff5de2d3cce8c3100">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ac9b0b400f7d555e4e2b3eb1e5f4c26aa" class="memitem:ac9b0b400f7d555e4e2b3eb1e5f4c26aa">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">completed: 1</td>
</tr>
<tr class="memdesc:ac9b0b400f7d555e4e2b3eb1e5f4c26aa">
<td class="mdescLeft"> </td>
<td class="mdescRight">TRUE if some thread has taken responsibility for completing this pending call: either the pending call has completed, or it is about to be completed.<br />
</td>
</tr>
<tr class="separator:ac9b0b400f7d555e4e2b3eb1e5f4c26aa">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a9e1230f62e6ada8af3903d299f2ff0b4" class="memitem:a9e1230f62e6ada8af3903d299f2ff0b4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">timeout_added: 1</td>
</tr>
<tr class="memdesc:a9e1230f62e6ada8af3903d299f2ff0b4">
<td class="mdescLeft"> </td>
<td class="mdescRight">TRUE if we have added the timeout.<br />
</td>
</tr>
<tr class="separator:a9e1230f62e6ada8af3903d299f2ff0b4">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Implementation details of DBusPendingCall - all fields are private.

Definition at line 64 of file dbus-pending-call.c.

## Field Documentation

## ◆ completed

|                                         |
|-----------------------------------------|
| unsigned int DBusPendingCall::completed |

TRUE if some thread has taken responsibility for completing this pending call: either the pending call has completed, or it is about to be completed.

Protected by the connection lock.

Definition at line 85 of file dbus-pending-call.c.

Referenced by \_dbus_pending_call_finish_completion(), \_dbus_pending_call_get_completed_unlocked(), \_dbus_pending_call_start_completion_unlocked(), dbus_pending_call_get_completed(), and dbus_pending_call_steal_reply().

## ◆ connection

|                                              |
|----------------------------------------------|
| DBusConnection\* DBusPendingCall::connection |

Connections we're associated with.

Definition at line 72 of file dbus-pending-call.c.

Referenced by \_dbus_pending_call_get_connection_and_lock(), \_dbus_pending_call_get_connection_unlocked(), \_dbus_pending_call_new_unlocked(), \_dbus_pending_call_queue_timeout_error_unlocked(), \_dbus_pending_call_set_data_unlocked(), \_dbus_pending_call_unref_and_unlock(), dbus_pending_call_cancel(), dbus_pending_call_get_completed(), dbus_pending_call_get_data(), dbus_pending_call_set_data(), dbus_pending_call_set_notify(), and dbus_pending_call_steal_reply().

## ◆ function

|                                                         |
|---------------------------------------------------------|
| DBusPendingCallNotifyFunction DBusPendingCall::function |

Notifier when reply arrives.

Definition at line 70 of file dbus-pending-call.c.

Referenced by \_dbus_pending_call_finish_completion(), and dbus_pending_call_set_notify().

## ◆ refcount

|                                      |
|--------------------------------------|
| DBusAtomic DBusPendingCall::refcount |

reference count

Definition at line 66 of file dbus-pending-call.c.

Referenced by \_dbus_pending_call_new_unlocked(), \_dbus_pending_call_ref_unlocked(), \_dbus_pending_call_unref_and_unlock(), dbus_pending_call_ref(), and dbus_pending_call_unref().

## ◆ reply

|                                      |
|--------------------------------------|
| DBusMessage\* DBusPendingCall::reply |

Reply (after we've received it)

Definition at line 73 of file dbus-pending-call.c.

Referenced by \_dbus_pending_call_set_reply_unlocked(), and dbus_pending_call_steal_reply().

## ◆ reply_serial

|                                             |
|---------------------------------------------|
| dbus_uint32_t DBusPendingCall::reply_serial |

Expected serial of reply.

Definition at line 78 of file dbus-pending-call.c.

Referenced by \_dbus_pending_call_get_reply_serial_unlocked(), \_dbus_pending_call_set_reply_serial_unlocked(), and \_dbus_pending_call_set_reply_unlocked().

## ◆ slot_list

|                                             |
|---------------------------------------------|
| DBusDataSlotList DBusPendingCall::slot_list |

Data stored by allocated integer ID.

Definition at line 68 of file dbus-pending-call.c.

Referenced by \_dbus_pending_call_new_unlocked(), \_dbus_pending_call_set_data_unlocked(), and dbus_pending_call_get_data().

## ◆ timeout

|                                        |
|----------------------------------------|
| DBusTimeout\* DBusPendingCall::timeout |

Timeout.

Definition at line 74 of file dbus-pending-call.c.

Referenced by \_dbus_pending_call_get_timeout_unlocked(), and \_dbus_pending_call_new_unlocked().

## ◆ timeout_added

|                                             |
|---------------------------------------------|
| unsigned int DBusPendingCall::timeout_added |

TRUE if we have added the timeout.

Protected by the connection lock.

Definition at line 89 of file dbus-pending-call.c.

Referenced by \_dbus_pending_call_is_timeout_added_unlocked(), and \_dbus_pending_call_set_timeout_added_unlocked().

## ◆ timeout_link

|                                          |
|------------------------------------------|
| DBusList\* DBusPendingCall::timeout_link |

Preallocated timeout response.

Definition at line 76 of file dbus-pending-call.c.

Referenced by \_dbus_pending_call_queue_timeout_error_unlocked(), \_dbus_pending_call_set_reply_unlocked(), and \_dbus_pending_call_set_timeout_error_unlocked().

The documentation for this struct was generated from the following file:

- dbus-pending-call.c
