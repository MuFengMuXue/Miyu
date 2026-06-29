DBusMessage Struct Reference

D-Bus secret internal implementation details » DBusMessage implementation details

Internals of DBusMessage. More...

`#include <``dbus-message-private.h``>`

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a324c5377e0be18dd84ac519ab2d23f0d" class="memitem:a324c5377e0be18dd84ac519ab2d23f0d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusAtomic </td>
<td class="memItemRight" data-valign="bottom">refcount</td>
</tr>
<tr class="memdesc:a324c5377e0be18dd84ac519ab2d23f0d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reference count.<br />
</td>
</tr>
<tr class="separator:a324c5377e0be18dd84ac519ab2d23f0d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a00cf6910d9f3bee5d5a82137c8c64a42" class="memitem:a00cf6910d9f3bee5d5a82137c8c64a42">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusHeader </td>
<td class="memItemRight" data-valign="bottom">header</td>
</tr>
<tr class="memdesc:a00cf6910d9f3bee5d5a82137c8c64a42">
<td class="mdescLeft"> </td>
<td class="mdescRight">Header network data and associated cache.<br />
</td>
</tr>
<tr class="separator:a00cf6910d9f3bee5d5a82137c8c64a42">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a0b9d14d6e0529f0ec2e3c0087fe62a9e" class="memitem:a0b9d14d6e0529f0ec2e3c0087fe62a9e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusString </td>
<td class="memItemRight" data-valign="bottom">body</td>
</tr>
<tr class="memdesc:a0b9d14d6e0529f0ec2e3c0087fe62a9e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Body network data.<br />
</td>
</tr>
<tr class="separator:a0b9d14d6e0529f0ec2e3c0087fe62a9e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ac926e7027f22608d75a6dfe18680b9e7" class="memitem:ac926e7027f22608d75a6dfe18680b9e7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">locked: 1</td>
</tr>
<tr class="memdesc:ac926e7027f22608d75a6dfe18680b9e7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Message being sent, no modifications allowed.<br />
</td>
</tr>
<tr class="separator:ac926e7027f22608d75a6dfe18680b9e7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ac71fa5534264093e6af8bc41f15237c8" class="memitem:ac71fa5534264093e6af8bc41f15237c8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">in_cache: 1</td>
</tr>
<tr class="memdesc:ac71fa5534264093e6af8bc41f15237c8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Has been "freed" since it's in the cache (this is a debug feature)<br />
</td>
</tr>
<tr class="separator:ac71fa5534264093e6af8bc41f15237c8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ac6fc05ddffb11ac60b9da046abd2dc52" class="memitem:ac6fc05ddffb11ac60b9da046abd2dc52">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusList * </td>
<td class="memItemRight" data-valign="bottom">counters</td>
</tr>
<tr class="memdesc:ac6fc05ddffb11ac60b9da046abd2dc52">
<td class="mdescLeft"> </td>
<td class="mdescRight">0-N DBusCounter used to track message size/unix fds.<br />
</td>
</tr>
<tr class="separator:ac6fc05ddffb11ac60b9da046abd2dc52">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ab8f43d40fa870f97f1126256568cec61" class="memitem:ab8f43d40fa870f97f1126256568cec61">
<td class="memItemLeft" style="text-align: right;" data-valign="top">long </td>
<td class="memItemRight" data-valign="bottom">size_counter_delta</td>
</tr>
<tr class="memdesc:ab8f43d40fa870f97f1126256568cec61">
<td class="mdescLeft"> </td>
<td class="mdescRight">Size we incremented the size counters by.<br />
</td>
</tr>
<tr class="separator:ab8f43d40fa870f97f1126256568cec61">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a5d102e908f6ff96a5a0aa6a39b4963a8" class="memitem:a5d102e908f6ff96a5a0aa6a39b4963a8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">changed_stamp: CHANGED_STAMP_BITS</td>
</tr>
<tr class="memdesc:a5d102e908f6ff96a5a0aa6a39b4963a8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Incremented when iterators are invalidated.<br />
</td>
</tr>
<tr class="separator:a5d102e908f6ff96a5a0aa6a39b4963a8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a179c446523c6321e04f88a671363be19" class="memitem:a179c446523c6321e04f88a671363be19">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusDataSlotList </td>
<td class="memItemRight" data-valign="bottom">slot_list</td>
</tr>
<tr class="memdesc:a179c446523c6321e04f88a671363be19">
<td class="mdescLeft"> </td>
<td class="mdescRight">Data stored by allocated integer ID.<br />
</td>
</tr>
<tr class="separator:a179c446523c6321e04f88a671363be19">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a96263aa8a777c8c661d2596911c7d592" class="memitem:a96263aa8a777c8c661d2596911c7d592">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">generation</td>
</tr>
<tr class="memdesc:a96263aa8a777c8c661d2596911c7d592">
<td class="mdescLeft"> </td>
<td class="mdescRight">_dbus_current_generation when message was created<br />
</td>
</tr>
<tr class="separator:a96263aa8a777c8c661d2596911c7d592">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Internals of DBusMessage.

Object representing a message received from or to be sent to another application. This is an opaque object, all members are private.

Definition at line 101 of file dbus-message-private.h.

## Field Documentation

## ◆ body

|                              |
|------------------------------|
| DBusString DBusMessage::body |

Body network data.

Definition at line 107 of file dbus-message-private.h.

Referenced by \_dbus_message_add_counter_link(), \_dbus_message_get_network_data(), dbus_message_copy(), dbus_message_iter_init(), dbus_message_iter_init_append(), dbus_message_lock(), and dbus_message_marshal().

## ◆ changed_stamp

|                                          |
|------------------------------------------|
| dbus_uint32_t DBusMessage::changed_stamp |

Incremented when iterators are invalidated.

Definition at line 118 of file dbus-message-private.h.

## ◆ counters

|                                  |
|----------------------------------|
| DBusList\* DBusMessage::counters |

0-N DBusCounter used to track message size/unix fds.

Definition at line 115 of file dbus-message-private.h.

Referenced by \_dbus_message_add_counter_link(), and \_dbus_message_remove_counter().

## ◆ generation

|                             |
|-----------------------------|
| int DBusMessage::generation |

\_dbus_current_generation when message was created

Definition at line 123 of file dbus-message-private.h.

Referenced by dbus_message_copy(), dbus_message_ref(), and dbus_message_unref().

## ◆ header

|                                |
|--------------------------------|
| DBusHeader DBusMessage::header |

Header network data and associated cache.

Definition at line 105 of file dbus-message-private.h.

Referenced by \_dbus_message_add_counter_link(), \_dbus_message_get_network_data(), \_dbus_message_remove_unknown_fields(), dbus_message_copy(), dbus_message_get_allow_interactive_authorization(), dbus_message_get_auto_start(), dbus_message_get_container_instance(), dbus_message_get_destination(), dbus_message_get_error_name(), dbus_message_get_interface(), dbus_message_get_member(), dbus_message_get_no_reply(), dbus_message_get_path(), dbus_message_get_reply_serial(), dbus_message_get_sender(), dbus_message_get_serial(), dbus_message_get_signature(), dbus_message_get_type(), dbus_message_iter_append_basic(), dbus_message_iter_init(), dbus_message_iter_init_append(), dbus_message_lock(), dbus_message_marshal(), dbus_message_new(), dbus_message_new_error(), dbus_message_new_method_call(), dbus_message_new_method_return(), dbus_message_new_signal(), dbus_message_set_allow_interactive_authorization(), dbus_message_set_auto_start(), dbus_message_set_no_reply(), dbus_message_set_reply_serial(), and dbus_message_set_serial().

## ◆ in_cache

|                                    |
|------------------------------------|
| unsigned int DBusMessage::in_cache |

Has been "freed" since it's in the cache (this is a debug feature)

Definition at line 112 of file dbus-message-private.h.

Referenced by dbus_message_ref(), and dbus_message_unref().

## ◆ locked

|                                  |
|----------------------------------|
| unsigned int DBusMessage::locked |

Message being sent, no modifications allowed.

Definition at line 109 of file dbus-message-private.h.

Referenced by \_dbus_message_get_network_data(), \_dbus_message_get_unix_fds(), dbus_message_copy(), dbus_message_lock(), dbus_message_marshal(), dbus_message_set_allow_interactive_authorization(), dbus_message_set_auto_start(), dbus_message_set_container_instance(), dbus_message_set_destination(), dbus_message_set_error_name(), dbus_message_set_interface(), dbus_message_set_member(), dbus_message_set_no_reply(), dbus_message_set_path(), dbus_message_set_reply_serial(), dbus_message_set_sender(), and dbus_message_set_serial().

## ◆ refcount

|                                  |
|----------------------------------|
| DBusAtomic DBusMessage::refcount |

Reference count.

Definition at line 103 of file dbus-message-private.h.

Referenced by dbus_message_copy(), dbus_message_ref(), and dbus_message_unref().

## ◆ size_counter_delta

|                                      |
|--------------------------------------|
| long DBusMessage::size_counter_delta |

Size we incremented the size counters by.

  

Definition at line 116 of file dbus-message-private.h.

Referenced by \_dbus_message_add_counter_link(), and \_dbus_message_remove_counter().

## ◆ slot_list

|                                         |
|-----------------------------------------|
| DBusDataSlotList DBusMessage::slot_list |

Data stored by allocated integer ID.

Definition at line 120 of file dbus-message-private.h.

Referenced by dbus_message_get_data(), and dbus_message_set_data().

The documentation for this struct was generated from the following file:

- dbus-message-private.h
