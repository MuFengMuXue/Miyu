DBusTimeout Struct Reference

D-Bus secret internal implementation details » DBusTimeout implementation details

Internals of DBusTimeout. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a1b2b2eadd3e162b213384cbd6d1e941e" class="memitem:a1b2b2eadd3e162b213384cbd6d1e941e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">refcount</td>
</tr>
<tr class="memdesc:a1b2b2eadd3e162b213384cbd6d1e941e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reference count.<br />
</td>
</tr>
<tr class="separator:a1b2b2eadd3e162b213384cbd6d1e941e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a8772f07a4695be987e7d0fea1b80ba16" class="memitem:a8772f07a4695be987e7d0fea1b80ba16">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">interval</td>
</tr>
<tr class="memdesc:a8772f07a4695be987e7d0fea1b80ba16">
<td class="mdescLeft"> </td>
<td class="mdescRight">Timeout interval in milliseconds.<br />
</td>
</tr>
<tr class="separator:a8772f07a4695be987e7d0fea1b80ba16">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a362a61722d3fae5c18c93654a57aa377" class="memitem:a362a61722d3fae5c18c93654a57aa377">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusTimeoutHandler </td>
<td class="memItemRight" data-valign="bottom">handler</td>
</tr>
<tr class="memdesc:a362a61722d3fae5c18c93654a57aa377">
<td class="mdescLeft"> </td>
<td class="mdescRight">Timeout handler.<br />
</td>
</tr>
<tr class="separator:a362a61722d3fae5c18c93654a57aa377">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a58a22bfb2f7f0543745c2d56fa9f63a1" class="memitem:a58a22bfb2f7f0543745c2d56fa9f63a1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">handler_data</td>
</tr>
<tr class="memdesc:a58a22bfb2f7f0543745c2d56fa9f63a1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Timeout handler data.<br />
</td>
</tr>
<tr class="separator:a58a22bfb2f7f0543745c2d56fa9f63a1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aadd5adfcf8896e0529df439548f351cc" class="memitem:aadd5adfcf8896e0529df439548f351cc">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusFreeFunction </td>
<td class="memItemRight" data-valign="bottom">free_handler_data_function</td>
</tr>
<tr class="memdesc:aadd5adfcf8896e0529df439548f351cc">
<td class="mdescLeft"> </td>
<td class="mdescRight">Free the timeout handler data.<br />
</td>
</tr>
<tr class="separator:aadd5adfcf8896e0529df439548f351cc">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a16cb374453e70f3951d02bcba73c1845" class="memitem:a16cb374453e70f3951d02bcba73c1845">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">data</td>
</tr>
<tr class="memdesc:a16cb374453e70f3951d02bcba73c1845">
<td class="mdescLeft"> </td>
<td class="mdescRight">Application data.<br />
</td>
</tr>
<tr class="separator:a16cb374453e70f3951d02bcba73c1845">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_af7ff88e58a10f4ed49a0838e0c930be0" class="memitem:af7ff88e58a10f4ed49a0838e0c930be0">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusFreeFunction </td>
<td class="memItemRight" data-valign="bottom">free_data_function</td>
</tr>
<tr class="memdesc:af7ff88e58a10f4ed49a0838e0c930be0">
<td class="mdescLeft"> </td>
<td class="mdescRight">Free the application data.<br />
</td>
</tr>
<tr class="separator:af7ff88e58a10f4ed49a0838e0c930be0">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a35ac546656105d0fe1929d4e3d224503" class="memitem:a35ac546656105d0fe1929d4e3d224503">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">enabled: 1</td>
</tr>
<tr class="memdesc:a35ac546656105d0fe1929d4e3d224503">
<td class="mdescLeft"> </td>
<td class="mdescRight">True if timeout is active.<br />
</td>
</tr>
<tr class="separator:a35ac546656105d0fe1929d4e3d224503">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a9afba7d221ad0ead2769fabcfd9cc070" class="memitem:a9afba7d221ad0ead2769fabcfd9cc070">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">needs_restart: 1</td>
</tr>
<tr class="memdesc:a9afba7d221ad0ead2769fabcfd9cc070">
<td class="mdescLeft"> </td>
<td class="mdescRight">Flag that timeout should be restarted after re-enabling.<br />
</td>
</tr>
<tr class="separator:a9afba7d221ad0ead2769fabcfd9cc070">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Internals of DBusTimeout.

Definition at line 42 of file dbus-timeout.c.

## Field Documentation

## ◆ data

|                          |
|--------------------------|
| void\* DBusTimeout::data |

Application data.

Definition at line 51 of file dbus-timeout.c.

Referenced by dbus_timeout_get_data(), and dbus_timeout_set_data().

## ◆ enabled

|                                   |
|-----------------------------------|
| unsigned int DBusTimeout::enabled |

True if timeout is active.

Definition at line 53 of file dbus-timeout.c.

Referenced by \_dbus_timeout_disable(), \_dbus_timeout_list_toggle_timeout(), \_dbus_timeout_new(), \_dbus_timeout_restart(), and dbus_timeout_get_enabled().

## ◆ free_data_function

|                                                  |
|--------------------------------------------------|
| DBusFreeFunction DBusTimeout::free_data_function |

Free the application data.

Definition at line 52 of file dbus-timeout.c.

Referenced by dbus_timeout_set_data().

## ◆ free_handler_data_function

|                                                          |
|----------------------------------------------------------|
| DBusFreeFunction DBusTimeout::free_handler_data_function |

Free the timeout handler data.

Definition at line 49 of file dbus-timeout.c.

Referenced by \_dbus_timeout_new(), and \_dbus_timeout_unref().

## ◆ handler

|                                         |
|-----------------------------------------|
| DBusTimeoutHandler DBusTimeout::handler |

Timeout handler.

Definition at line 47 of file dbus-timeout.c.

Referenced by \_dbus_timeout_new(), and dbus_timeout_handle().

## ◆ handler_data

|                                  |
|----------------------------------|
| void\* DBusTimeout::handler_data |

Timeout handler data.

Definition at line 48 of file dbus-timeout.c.

Referenced by \_dbus_timeout_new(), \_dbus_timeout_unref(), and dbus_timeout_handle().

## ◆ interval

|                           |
|---------------------------|
| int DBusTimeout::interval |

Timeout interval in milliseconds.

Definition at line 45 of file dbus-timeout.c.

Referenced by \_dbus_timeout_new(), \_dbus_timeout_restart(), and dbus_timeout_get_interval().

## ◆ needs_restart

|                                         |
|-----------------------------------------|
| unsigned int DBusTimeout::needs_restart |

Flag that timeout should be restarted after re-enabling.

Definition at line 54 of file dbus-timeout.c.

Referenced by \_dbus_timeout_needs_restart(), \_dbus_timeout_new(), \_dbus_timeout_restart(), and \_dbus_timeout_restarted().

## ◆ refcount

|                           |
|---------------------------|
| int DBusTimeout::refcount |

Reference count.

Definition at line 44 of file dbus-timeout.c.

Referenced by \_dbus_timeout_new(), \_dbus_timeout_ref(), and \_dbus_timeout_unref().

The documentation for this struct was generated from the following file:

- dbus-timeout.c
