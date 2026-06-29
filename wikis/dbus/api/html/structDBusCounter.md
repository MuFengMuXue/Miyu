DBusCounter Struct Reference

D-Bus secret internal implementation details » Resource limits implementation details

Internals of DBusCounter. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a42ef245097a0b221b58bf200a0a187b0" class="memitem:a42ef245097a0b221b58bf200a0a187b0">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">refcount</td>
</tr>
<tr class="memdesc:a42ef245097a0b221b58bf200a0a187b0">
<td class="mdescLeft"> </td>
<td class="mdescRight">reference count<br />
</td>
</tr>
<tr class="separator:a42ef245097a0b221b58bf200a0a187b0">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aadf8f12634aab55166d694320c545f8e" class="memitem:aadf8f12634aab55166d694320c545f8e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">long </td>
<td class="memItemRight" data-valign="bottom">size_value</td>
</tr>
<tr class="memdesc:aadf8f12634aab55166d694320c545f8e">
<td class="mdescLeft"> </td>
<td class="mdescRight">current size counter value<br />
</td>
</tr>
<tr class="separator:aadf8f12634aab55166d694320c545f8e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_af23298e36b579cc511f00d03ce3ff823" class="memitem:af23298e36b579cc511f00d03ce3ff823">
<td class="memItemLeft" style="text-align: right;" data-valign="top">long </td>
<td class="memItemRight" data-valign="bottom">unix_fd_value</td>
</tr>
<tr class="memdesc:af23298e36b579cc511f00d03ce3ff823">
<td class="mdescLeft"> </td>
<td class="mdescRight">current unix fd counter value<br />
</td>
</tr>
<tr class="separator:af23298e36b579cc511f00d03ce3ff823">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_af73ade097f3dfad1035361867b9f7064" class="memitem:af73ade097f3dfad1035361867b9f7064">
<td class="memItemLeft" style="text-align: right;" data-valign="top">long </td>
<td class="memItemRight" data-valign="bottom">notify_size_guard_value</td>
</tr>
<tr class="memdesc:af73ade097f3dfad1035361867b9f7064">
<td class="mdescLeft"> </td>
<td class="mdescRight">call notify function when crossing this size value<br />
</td>
</tr>
<tr class="separator:af73ade097f3dfad1035361867b9f7064">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a85157c4d3c445e41f58dc6941b23814c" class="memitem:a85157c4d3c445e41f58dc6941b23814c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">long </td>
<td class="memItemRight" data-valign="bottom">notify_unix_fd_guard_value</td>
</tr>
<tr class="memdesc:a85157c4d3c445e41f58dc6941b23814c">
<td class="mdescLeft"> </td>
<td class="mdescRight">call notify function when crossing this unix fd value<br />
</td>
</tr>
<tr class="separator:a85157c4d3c445e41f58dc6941b23814c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a626238ea91d2cf0c93a6eb958f7199b8" class="memitem:a626238ea91d2cf0c93a6eb958f7199b8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusCounterNotifyFunction </td>
<td class="memItemRight" data-valign="bottom">notify_function</td>
</tr>
<tr class="memdesc:a626238ea91d2cf0c93a6eb958f7199b8">
<td class="mdescLeft"> </td>
<td class="mdescRight">notify function<br />
</td>
</tr>
<tr class="separator:a626238ea91d2cf0c93a6eb958f7199b8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a592288b6cf62431b3a26aaa6d7c3fb05" class="memitem:a592288b6cf62431b3a26aaa6d7c3fb05">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">notify_data</td>
</tr>
<tr class="memdesc:a592288b6cf62431b3a26aaa6d7c3fb05">
<td class="mdescLeft"> </td>
<td class="mdescRight">data for notify function<br />
</td>
</tr>
<tr class="separator:a592288b6cf62431b3a26aaa6d7c3fb05">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a9c26dcd74f700959b0b920ec2bf1fd17" class="memitem:a9c26dcd74f700959b0b920ec2bf1fd17">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">notify_pending: 1</td>
</tr>
<tr class="memdesc:a9c26dcd74f700959b0b920ec2bf1fd17">
<td class="mdescLeft"> </td>
<td class="mdescRight">TRUE if the guard value has been crossed.<br />
</td>
</tr>
<tr class="separator:a9c26dcd74f700959b0b920ec2bf1fd17">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ae99efa36b9a41e9c103f454a102bfced" class="memitem:ae99efa36b9a41e9c103f454a102bfced">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusRMutex * </td>
<td class="memItemRight" data-valign="bottom">mutex</td>
</tr>
<tr class="memdesc:ae99efa36b9a41e9c103f454a102bfced">
<td class="mdescLeft"> </td>
<td class="mdescRight">Lock on the entire DBusCounter.<br />
</td>
</tr>
<tr class="separator:ae99efa36b9a41e9c103f454a102bfced">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Internals of DBusCounter.

DBusCounter internals. DBusCounter is an opaque object, it must be used via accessor functions.

Definition at line 56 of file dbus-resources.c.

## Field Documentation

## ◆ mutex

|                                 |
|---------------------------------|
| DBusRMutex\* DBusCounter::mutex |

Lock on the entire DBusCounter.

Definition at line 74 of file dbus-resources.c.

Referenced by \_dbus_counter_adjust_size(), \_dbus_counter_adjust_unix_fd(), \_dbus_counter_get_size_value(), \_dbus_counter_get_unix_fd_value(), \_dbus_counter_new(), \_dbus_counter_notify(), \_dbus_counter_ref(), \_dbus_counter_set_notify(), and \_dbus_counter_unref().

## ◆ notify_data

|                                 |
|---------------------------------|
| void\* DBusCounter::notify_data |

data for notify function

Definition at line 72 of file dbus-resources.c.

Referenced by \_dbus_counter_notify(), and \_dbus_counter_set_notify().

## ◆ notify_function

|                                                        |
|--------------------------------------------------------|
| DBusCounterNotifyFunction DBusCounter::notify_function |

notify function

Definition at line 71 of file dbus-resources.c.

Referenced by \_dbus_counter_adjust_size(), \_dbus_counter_adjust_unix_fd(), \_dbus_counter_notify(), and \_dbus_counter_set_notify().

## ◆ notify_pending

|                                         |
|-----------------------------------------|
| dbus_bool_t DBusCounter::notify_pending |

TRUE if the guard value has been crossed.

Definition at line 73 of file dbus-resources.c.

Referenced by \_dbus_counter_adjust_size(), \_dbus_counter_adjust_unix_fd(), \_dbus_counter_notify(), and \_dbus_counter_set_notify().

## ◆ notify_size_guard_value

|                                           |
|-------------------------------------------|
| long DBusCounter::notify_size_guard_value |

call notify function when crossing this size value

Definition at line 68 of file dbus-resources.c.

Referenced by \_dbus_counter_adjust_size(), and \_dbus_counter_set_notify().

## ◆ notify_unix_fd_guard_value

|                                              |
|----------------------------------------------|
| long DBusCounter::notify_unix_fd_guard_value |

call notify function when crossing this unix fd value

Definition at line 69 of file dbus-resources.c.

Referenced by \_dbus_counter_adjust_unix_fd(), and \_dbus_counter_set_notify().

## ◆ refcount

|                           |
|---------------------------|
| int DBusCounter::refcount |

reference count

Definition at line 58 of file dbus-resources.c.

Referenced by \_dbus_counter_new(), \_dbus_counter_ref(), and \_dbus_counter_unref().

## ◆ size_value

|                              |
|------------------------------|
| long DBusCounter::size_value |

current size counter value

Definition at line 60 of file dbus-resources.c.

Referenced by \_dbus_counter_adjust_size(), and \_dbus_counter_get_size_value().

## ◆ unix_fd_value

|                                 |
|---------------------------------|
| long DBusCounter::unix_fd_value |

current unix fd counter value

Definition at line 61 of file dbus-resources.c.

Referenced by \_dbus_counter_adjust_unix_fd(), and \_dbus_counter_get_unix_fd_value().

The documentation for this struct was generated from the following file:

- dbus-resources.c
