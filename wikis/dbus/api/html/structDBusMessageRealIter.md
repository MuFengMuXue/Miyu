DBusMessageRealIter Struct Reference

D-Bus secret internal implementation details » DBusMessage implementation details

Internals of DBusMessageIter. More...

<table class="memberdecls">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
<td></td>
</tr>
<tr id="r_a552cb582c65645ed46d9d1ad38ece3c7" class="memitem:a552cb582c65645ed46d9d1ad38ece3c7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMessage * </td>
<td class="memItemRight" data-valign="bottom">message</td>
<td></td>
</tr>
<tr class="memdesc:a552cb582c65645ed46d9d1ad38ece3c7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Message used.<br />
</td>
<td></td>
</tr>
<tr class="separator:a552cb582c65645ed46d9d1ad38ece3c7">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_ac10324f74497a5c2288eef8fbcd3ae42" class="memitem:ac10324f74497a5c2288eef8fbcd3ae42">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">changed_stamp: CHANGED_STAMP_BITS</td>
<td></td>
</tr>
<tr class="memdesc:ac10324f74497a5c2288eef8fbcd3ae42">
<td class="mdescLeft"> </td>
<td class="mdescRight">stamp to detect invalid iters<br />
</td>
<td></td>
</tr>
<tr class="separator:ac10324f74497a5c2288eef8fbcd3ae42">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_a835b7990b2909beb06fc2dc38b76a089" class="memitem:a835b7990b2909beb06fc2dc38b76a089">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">iter_type: 3</td>
<td></td>
</tr>
<tr class="memdesc:a835b7990b2909beb06fc2dc38b76a089">
<td class="mdescLeft"> </td>
<td class="mdescRight">whether this is a reader or writer iter<br />
</td>
<td></td>
</tr>
<tr class="separator:a835b7990b2909beb06fc2dc38b76a089">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_a93789e6f814d55b5952fee34d286f6d6" class="memitem:a93789e6f814d55b5952fee34d286f6d6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">sig_refcount: 8</td>
<td></td>
</tr>
<tr class="memdesc:a93789e6f814d55b5952fee34d286f6d6">
<td class="mdescLeft"> </td>
<td class="mdescRight">depth of open_signature()<br />
</td>
<td></td>
</tr>
<tr class="separator:a93789e6f814d55b5952fee34d286f6d6">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_a4c2d45134fa4c3846dd0d2e53af230ba" class="memitem:a4c2d45134fa4c3846dd0d2e53af230ba">
<td class="memItemLeft"> union { </td>
<td class="memItemRight" data-valign="bottom"></td>
<td></td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_aff9b1ba7d4b12ee6de871293726178c4" class="memitem:aff9b1ba7d4b12ee6de871293726178c4">
<td class="memItemLeft">   DBusTypeWriter   writer </td>
<td class="memItemRight" data-valign="bottom"></td>
<td></td>
</tr>
<tr class="memdesc:aff9b1ba7d4b12ee6de871293726178c4">
<td class="mdescLeft"> </td>
<td class="mdescRight">writer More...<br />
</td>
<td></td>
</tr>
<tr class="separator:aff9b1ba7d4b12ee6de871293726178c4">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_acb1a47518ae0723dd7062d9ee4b3529b" class="memitem:acb1a47518ae0723dd7062d9ee4b3529b">
<td class="memItemLeft">   DBusTypeReader   reader </td>
<td class="memItemRight" data-valign="bottom"></td>
<td></td>
</tr>
<tr class="memdesc:acb1a47518ae0723dd7062d9ee4b3529b">
<td class="mdescLeft"> </td>
<td class="mdescRight">reader More...<br />
</td>
<td></td>
</tr>
<tr class="separator:acb1a47518ae0723dd7062d9ee4b3529b">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
<tr id="r_a4c2d45134fa4c3846dd0d2e53af230ba" class="memitem:a4c2d45134fa4c3846dd0d2e53af230ba">
<td class="memItemLeft" data-valign="top">} </td>
<td class="memItemRight" data-valign="bottom"><strong>u</strong> </td>
<td class="memItemRight" data-valign="bottom"></td>
</tr>
<tr class="memdesc:a4c2d45134fa4c3846dd0d2e53af230ba">
<td class="mdescLeft"> </td>
<td class="mdescRight">the type writer or reader that does all the work<br />
</td>
<td></td>
</tr>
<tr class="separator:a4c2d45134fa4c3846dd0d2e53af230ba">
<td colspan="2" class="memSeparator"> </td>
<td></td>
</tr>
</tbody>
</table>

## Detailed Description

Internals of DBusMessageIter.

Object representing a position in a message. All fields are internal.

Definition at line 128 of file dbus-message.c.

## Field Documentation

## ◆ changed_stamp

|                                                  |
|--------------------------------------------------|
| dbus_uint32_t DBusMessageRealIter::changed_stamp |

stamp to detect invalid iters

Definition at line 131 of file dbus-message.c.

## ◆ iter_type

|                                              |
|----------------------------------------------|
| dbus_uint32_t DBusMessageRealIter::iter_type |

whether this is a reader or writer iter

Definition at line 132 of file dbus-message.c.

Referenced by \_dbus_variant_read(), \_dbus_variant_write(), dbus_message_iter_abandon_container(), dbus_message_iter_abandon_container_if_open(), dbus_message_iter_append_basic(), dbus_message_iter_append_fixed_array(), dbus_message_iter_close_container(), dbus_message_iter_get_arg_type(), dbus_message_iter_get_element_type(), dbus_message_iter_has_next(), dbus_message_iter_next(), and dbus_message_iter_open_container().

## ◆ message

|                                            |
|--------------------------------------------|
| DBusMessage\* DBusMessageRealIter::message |

Message used.

Definition at line 130 of file dbus-message.c.

Referenced by \_dbus_message_iter_get_args_valist(), dbus_message_iter_append_basic(), and dbus_message_iter_get_basic().

## ◆ reader

|                                            |
|--------------------------------------------|
| DBusTypeReader DBusMessageRealIter::reader |

reader

Definition at line 137 of file dbus-message.c.

Referenced by \_dbus_message_iter_get_args_valist(), \_dbus_variant_read(), dbus_message_iter_get_arg_type(), dbus_message_iter_get_array_len(), dbus_message_iter_get_basic(), dbus_message_iter_get_element_count(), dbus_message_iter_get_element_type(), dbus_message_iter_get_fixed_array(), dbus_message_iter_get_signature(), dbus_message_iter_has_next(), dbus_message_iter_init(), dbus_message_iter_next(), and dbus_message_iter_recurse().

## ◆ sig_refcount

|                                                 |
|-------------------------------------------------|
| dbus_uint32_t DBusMessageRealIter::sig_refcount |

depth of open_signature()

Definition at line 133 of file dbus-message.c.

## ◆ writer

|                                            |
|--------------------------------------------|
| DBusTypeWriter DBusMessageRealIter::writer |

writer

Definition at line 136 of file dbus-message.c.

Referenced by \_dbus_variant_write(), dbus_message_iter_append_basic(), dbus_message_iter_append_fixed_array(), dbus_message_iter_close_container(), dbus_message_iter_init_append(), and dbus_message_iter_open_container().

The documentation for this struct was generated from the following file:

- dbus-message.c
