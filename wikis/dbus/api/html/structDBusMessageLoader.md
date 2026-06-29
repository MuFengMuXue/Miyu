DBusMessageLoader Struct Reference

D-Bus secret internal implementation details » DBusMessage implementation details

Implementation details of DBusMessageLoader. More...

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
<tr id="r_af3372b7d574dab49a7435d8f29ea2258" class="memitem:af3372b7d574dab49a7435d8f29ea2258">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">refcount</td>
</tr>
<tr class="memdesc:af3372b7d574dab49a7435d8f29ea2258">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reference count.<br />
</td>
</tr>
<tr class="separator:af3372b7d574dab49a7435d8f29ea2258">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a33c22d4f64a32a72faefb1df94fcfed1" class="memitem:a33c22d4f64a32a72faefb1df94fcfed1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusString </td>
<td class="memItemRight" data-valign="bottom">data</td>
</tr>
<tr class="memdesc:a33c22d4f64a32a72faefb1df94fcfed1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Buffered data.<br />
</td>
</tr>
<tr class="separator:a33c22d4f64a32a72faefb1df94fcfed1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a5ad667f9a5b58d23f2089e7cea58f6cc" class="memitem:a5ad667f9a5b58d23f2089e7cea58f6cc">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusList * </td>
<td class="memItemRight" data-valign="bottom">messages</td>
</tr>
<tr class="memdesc:a5ad667f9a5b58d23f2089e7cea58f6cc">
<td class="mdescLeft"> </td>
<td class="mdescRight">Complete messages.<br />
</td>
</tr>
<tr class="separator:a5ad667f9a5b58d23f2089e7cea58f6cc">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a174d67695b3aca6ee3bb8e1e5e033334" class="memitem:a174d67695b3aca6ee3bb8e1e5e033334">
<td class="memItemLeft" style="text-align: right;" data-valign="top">long </td>
<td class="memItemRight" data-valign="bottom">max_message_size</td>
</tr>
<tr class="memdesc:a174d67695b3aca6ee3bb8e1e5e033334">
<td class="mdescLeft"> </td>
<td class="mdescRight">Maximum size of a message.<br />
</td>
</tr>
<tr class="separator:a174d67695b3aca6ee3bb8e1e5e033334">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a2134a617c0d631d946adee1f08443851" class="memitem:a2134a617c0d631d946adee1f08443851">
<td class="memItemLeft" style="text-align: right;" data-valign="top">long </td>
<td class="memItemRight" data-valign="bottom">max_message_unix_fds</td>
</tr>
<tr class="memdesc:a2134a617c0d631d946adee1f08443851">
<td class="mdescLeft"> </td>
<td class="mdescRight">Maximum unix fds in a message.<br />
</td>
</tr>
<tr class="separator:a2134a617c0d631d946adee1f08443851">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ac6116f8620094b8ce348b103483c0035" class="memitem:ac6116f8620094b8ce348b103483c0035">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusValidity </td>
<td class="memItemRight" data-valign="bottom">corruption_reason</td>
</tr>
<tr class="memdesc:ac6116f8620094b8ce348b103483c0035">
<td class="mdescLeft"> </td>
<td class="mdescRight">why we were corrupted<br />
</td>
</tr>
<tr class="separator:ac6116f8620094b8ce348b103483c0035">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a7af27694794dc471ed3b251da8d7c62e" class="memitem:a7af27694794dc471ed3b251da8d7c62e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">corrupted: 1</td>
</tr>
<tr class="memdesc:a7af27694794dc471ed3b251da8d7c62e">
<td class="mdescLeft"> </td>
<td class="mdescRight">We got broken data, and are no longer working.<br />
</td>
</tr>
<tr class="separator:a7af27694794dc471ed3b251da8d7c62e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a7fe926ecd87e9ddb37e7481195bc3d67" class="memitem:a7fe926ecd87e9ddb37e7481195bc3d67">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">buffer_outstanding: 1</td>
</tr>
<tr class="memdesc:a7fe926ecd87e9ddb37e7481195bc3d67">
<td class="mdescLeft"> </td>
<td class="mdescRight">Someone is using the buffer to read.<br />
</td>
</tr>
<tr class="separator:a7fe926ecd87e9ddb37e7481195bc3d67">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Implementation details of DBusMessageLoader.

All members are private.

Definition at line 62 of file dbus-message-private.h.

## Field Documentation

## ◆ buffer_outstanding

|                                                    |
|----------------------------------------------------|
| unsigned int DBusMessageLoader::buffer_outstanding |

Someone is using the buffer to read.

Definition at line 77 of file dbus-message-private.h.

Referenced by \_dbus_message_loader_get_buffer(), and \_dbus_message_loader_return_buffer().

## ◆ corrupted

|                                           |
|-------------------------------------------|
| unsigned int DBusMessageLoader::corrupted |

We got broken data, and are no longer working.

Definition at line 75 of file dbus-message-private.h.

Referenced by \_dbus_message_loader_get_corruption_reason(), \_dbus_message_loader_get_is_corrupted(), \_dbus_message_loader_new(), and \_dbus_message_loader_queue_messages().

## ◆ corruption_reason

|                                                   |
|---------------------------------------------------|
| DBusValidity DBusMessageLoader::corruption_reason |

why we were corrupted

Definition at line 73 of file dbus-message-private.h.

Referenced by \_dbus_message_loader_get_corruption_reason(), \_dbus_message_loader_get_is_corrupted(), \_dbus_message_loader_new(), \_dbus_message_loader_queue_messages(), and dbus_message_demarshal().

## ◆ data

|                                    |
|------------------------------------|
| DBusString DBusMessageLoader::data |

Buffered data.

Definition at line 66 of file dbus-message-private.h.

Referenced by \_dbus_message_loader_get_buffer(), \_dbus_message_loader_new(), \_dbus_message_loader_queue_messages(), \_dbus_message_loader_return_buffer(), and \_dbus_message_loader_unref().

## ◆ max_message_size

|                                          |
|------------------------------------------|
| long DBusMessageLoader::max_message_size |

Maximum size of a message.

Definition at line 70 of file dbus-message-private.h.

Referenced by \_dbus_message_loader_get_buffer(), \_dbus_message_loader_get_max_message_size(), \_dbus_message_loader_new(), \_dbus_message_loader_queue_messages(), and \_dbus_message_loader_set_max_message_size().

## ◆ max_message_unix_fds

|                                              |
|----------------------------------------------|
| long DBusMessageLoader::max_message_unix_fds |

Maximum unix fds in a message.

Definition at line 71 of file dbus-message-private.h.

Referenced by \_dbus_message_loader_get_max_message_unix_fds(), \_dbus_message_loader_new(), and \_dbus_message_loader_set_max_message_unix_fds().

## ◆ messages

|                                        |
|----------------------------------------|
| DBusList\* DBusMessageLoader::messages |

Complete messages.

Definition at line 68 of file dbus-message-private.h.

Referenced by \_dbus_message_loader_peek_message(), \_dbus_message_loader_pop_message(), \_dbus_message_loader_pop_message_link(), \_dbus_message_loader_putback_message_link(), \_dbus_message_loader_queue_messages(), and \_dbus_message_loader_unref().

## ◆ refcount

|                                 |
|---------------------------------|
| int DBusMessageLoader::refcount |

Reference count.

Definition at line 64 of file dbus-message-private.h.

Referenced by \_dbus_message_loader_new(), \_dbus_message_loader_ref(), and \_dbus_message_loader_unref().

The documentation for this struct was generated from the following file:

- dbus-message-private.h
