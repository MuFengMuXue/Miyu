DBusList Struct Reference

D-Bus secret internal implementation details » Linked list

A node in a linked list. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_aaeb8ce69b141da1f04621ae81eed3388" class="memitem:aaeb8ce69b141da1f04621ae81eed3388">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusList * </td>
<td class="memItemRight" data-valign="bottom">prev</td>
</tr>
<tr class="memdesc:aaeb8ce69b141da1f04621ae81eed3388">
<td class="mdescLeft"> </td>
<td class="mdescRight">Previous list node.<br />
</td>
</tr>
<tr class="separator:aaeb8ce69b141da1f04621ae81eed3388">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a83180142180c856b2a02778e155cb044" class="memitem:a83180142180c856b2a02778e155cb044">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusList * </td>
<td class="memItemRight" data-valign="bottom">next</td>
</tr>
<tr class="memdesc:a83180142180c856b2a02778e155cb044">
<td class="mdescLeft"> </td>
<td class="mdescRight">Next list node.<br />
</td>
</tr>
<tr class="separator:a83180142180c856b2a02778e155cb044">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a29ab457bcf9092252bb0c4282c727055" class="memitem:a29ab457bcf9092252bb0c4282c727055">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">data</td>
</tr>
<tr class="memdesc:a29ab457bcf9092252bb0c4282c727055">
<td class="mdescLeft"> </td>
<td class="mdescRight">Data stored at this element.<br />
</td>
</tr>
<tr class="separator:a29ab457bcf9092252bb0c4282c727055">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

A node in a linked list.

DBusList is a circular list; that is, the tail of the list points back to the head of the list. The empty list is represented by a NULL pointer.

Definition at line 36 of file dbus-list.h.

## Field Documentation

## ◆ data

|                       |
|-----------------------|
| void\* DBusList::data |

Data stored at this element.

Definition at line 40 of file dbus-list.h.

Referenced by \_dbus_connection_message_sent_unlocked(), \_dbus_connection_queue_received_message_link(), \_dbus_connection_queue_synthesized_message_link(), \_dbus_connection_unlock(), \_dbus_list_clear_full(), \_dbus_list_copy(), \_dbus_list_find_last(), \_dbus_list_foreach(), \_dbus_list_pop_first(), \_dbus_list_pop_last(), \_dbus_list_remove(), \_dbus_message_add_counter_link(), \_dbus_message_loader_peek_message(), \_dbus_object_tree_dispatch_and_unlock(), \_dbus_pending_call_set_reply_unlocked(), \_dbus_timeout_list_set_functions(), \_dbus_transport_queue_messages(), \_dbus_watch_list_set_functions(), \_dbus_watch_list_toggle_all_watches(), dbus_address_entry_get_value(), dbus_connection_dispatch(), dbus_connection_free_preallocated_send(), dbus_connection_remove_filter(), and dbus_parse_address().

## ◆ next

|                           |
|---------------------------|
| DBusList\* DBusList::next |

Next list node.

Definition at line 39 of file dbus-list.h.

Referenced by \_dbus_list_append(), \_dbus_list_append_link(), \_dbus_list_length_is_one(), and \_dbus_list_unlink().

## ◆ prev

|                           |
|---------------------------|
| DBusList\* DBusList::prev |

Previous list node.

Definition at line 38 of file dbus-list.h.

Referenced by \_dbus_list_get_last_link(), and \_dbus_list_unlink().

The documentation for this struct was generated from the following file:

- dbus-list.h
