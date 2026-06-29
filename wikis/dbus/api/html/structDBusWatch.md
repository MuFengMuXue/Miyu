DBusWatch Struct Reference

D-Bus secret internal implementation details » DBusWatch implementation details

Implementation of DBusWatch. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a3984cbcb64ed76d2f0c1182c386f7978" class="memitem:a3984cbcb64ed76d2f0c1182c386f7978">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">refcount</td>
</tr>
<tr class="memdesc:a3984cbcb64ed76d2f0c1182c386f7978">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reference count.<br />
</td>
</tr>
<tr class="separator:a3984cbcb64ed76d2f0c1182c386f7978">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a7c3796e9aec318ef800080eab3598cc9" class="memitem:a7c3796e9aec318ef800080eab3598cc9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusPollable </td>
<td class="memItemRight" data-valign="bottom">fd</td>
</tr>
<tr class="memdesc:a7c3796e9aec318ef800080eab3598cc9">
<td class="mdescLeft"> </td>
<td class="mdescRight">File descriptor.<br />
</td>
</tr>
<tr class="separator:a7c3796e9aec318ef800080eab3598cc9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a7f1c2c609410f58a2328681c2893f70a" class="memitem:a7f1c2c609410f58a2328681c2893f70a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">flags</td>
</tr>
<tr class="memdesc:a7f1c2c609410f58a2328681c2893f70a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Conditions to watch.<br />
</td>
</tr>
<tr class="separator:a7f1c2c609410f58a2328681c2893f70a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aad3fb97da0ad7e5897611930f7a1c3e9" class="memitem:aad3fb97da0ad7e5897611930f7a1c3e9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusWatchHandler </td>
<td class="memItemRight" data-valign="bottom">handler</td>
</tr>
<tr class="memdesc:aad3fb97da0ad7e5897611930f7a1c3e9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Watch handler.<br />
</td>
</tr>
<tr class="separator:aad3fb97da0ad7e5897611930f7a1c3e9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ae906b28caa8a4323f85c882abe901e87" class="memitem:ae906b28caa8a4323f85c882abe901e87">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">handler_data</td>
</tr>
<tr class="memdesc:ae906b28caa8a4323f85c882abe901e87">
<td class="mdescLeft"> </td>
<td class="mdescRight">Watch handler data.<br />
</td>
</tr>
<tr class="separator:ae906b28caa8a4323f85c882abe901e87">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a64eaf9b88cebfc640bc85d0fd37184c8" class="memitem:a64eaf9b88cebfc640bc85d0fd37184c8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusFreeFunction </td>
<td class="memItemRight" data-valign="bottom">free_handler_data_function</td>
</tr>
<tr class="memdesc:a64eaf9b88cebfc640bc85d0fd37184c8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Free the watch handler data.<br />
</td>
</tr>
<tr class="separator:a64eaf9b88cebfc640bc85d0fd37184c8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a71877a39d8c2a7d533c0c6f280648d53" class="memitem:a71877a39d8c2a7d533c0c6f280648d53">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">data</td>
</tr>
<tr class="memdesc:a71877a39d8c2a7d533c0c6f280648d53">
<td class="mdescLeft"> </td>
<td class="mdescRight">Application data.<br />
</td>
</tr>
<tr class="separator:a71877a39d8c2a7d533c0c6f280648d53">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ad848cbd636518fd346039d0d771ba021" class="memitem:ad848cbd636518fd346039d0d771ba021">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusFreeFunction </td>
<td class="memItemRight" data-valign="bottom">free_data_function</td>
</tr>
<tr class="memdesc:ad848cbd636518fd346039d0d771ba021">
<td class="mdescLeft"> </td>
<td class="mdescRight">Free the application data.<br />
</td>
</tr>
<tr class="separator:ad848cbd636518fd346039d0d771ba021">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a010564b43e0c7dd438b9ac4b0c1dbe64" class="memitem:a010564b43e0c7dd438b9ac4b0c1dbe64">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">enabled: 1</td>
</tr>
<tr class="memdesc:a010564b43e0c7dd438b9ac4b0c1dbe64">
<td class="mdescLeft"> </td>
<td class="mdescRight">Whether it's enabled.<br />
</td>
</tr>
<tr class="separator:a010564b43e0c7dd438b9ac4b0c1dbe64">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a1020150c9fd9764ac85919d2c48bb6e1" class="memitem:a1020150c9fd9764ac85919d2c48bb6e1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">oom_last_time: 1</td>
</tr>
<tr class="memdesc:a1020150c9fd9764ac85919d2c48bb6e1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Whether it was OOM last time.<br />
</td>
</tr>
<tr class="separator:a1020150c9fd9764ac85919d2c48bb6e1">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Implementation of DBusWatch.

Definition at line 42 of file dbus-watch.c.

## Field Documentation

## ◆ data

|                        |
|------------------------|
| void\* DBusWatch::data |

Application data.

Definition at line 52 of file dbus-watch.c.

Referenced by dbus_watch_get_data(), and dbus_watch_set_data().

## ◆ enabled

|                                 |
|---------------------------------|
| unsigned int DBusWatch::enabled |

Whether it's enabled.

Definition at line 54 of file dbus-watch.c.

Referenced by \_dbus_watch_list_toggle_watch(), \_dbus_watch_new(), and dbus_watch_get_enabled().

## ◆ fd

|                            |
|----------------------------|
| DBusPollable DBusWatch::fd |

File descriptor.

Definition at line 45 of file dbus-watch.c.

Referenced by \_dbus_watch_invalidate(), \_dbus_watch_list_add_watch(), \_dbus_watch_list_remove_watch(), \_dbus_watch_list_set_functions(), \_dbus_watch_list_toggle_watch(), \_dbus_watch_new(), \_dbus_watch_unref(), dbus_watch_get_socket(), dbus_watch_get_unix_fd(), dbus_watch_handle(), and dbus_watch_set_data().

## ◆ flags

|                               |
|-------------------------------|
| unsigned int DBusWatch::flags |

Conditions to watch.

Definition at line 46 of file dbus-watch.c.

Referenced by \_dbus_watch_invalidate(), \_dbus_watch_new(), \_dbus_watch_sanitize_condition(), dbus_watch_get_flags(), and dbus_watch_handle().

## ◆ free_data_function

|                                                |
|------------------------------------------------|
| DBusFreeFunction DBusWatch::free_data_function |

Free the application data.

Definition at line 53 of file dbus-watch.c.

Referenced by dbus_watch_set_data().

## ◆ free_handler_data_function

|                                                        |
|--------------------------------------------------------|
| DBusFreeFunction DBusWatch::free_handler_data_function |

Free the watch handler data.

Definition at line 50 of file dbus-watch.c.

Referenced by \_dbus_watch_new(), \_dbus_watch_set_handler(), and \_dbus_watch_unref().

## ◆ handler

|                                     |
|-------------------------------------|
| DBusWatchHandler DBusWatch::handler |

Watch handler.

Definition at line 48 of file dbus-watch.c.

Referenced by \_dbus_watch_new(), \_dbus_watch_set_handler(), and dbus_watch_handle().

## ◆ handler_data

|                                |
|--------------------------------|
| void\* DBusWatch::handler_data |

Watch handler data.

Definition at line 49 of file dbus-watch.c.

Referenced by \_dbus_watch_new(), \_dbus_watch_set_handler(), \_dbus_watch_unref(), and dbus_watch_handle().

## ◆ oom_last_time

|                                       |
|---------------------------------------|
| unsigned int DBusWatch::oom_last_time |

Whether it was OOM last time.

Definition at line 55 of file dbus-watch.c.

## ◆ refcount

|                         |
|-------------------------|
| int DBusWatch::refcount |

Reference count.

Definition at line 44 of file dbus-watch.c.

Referenced by \_dbus_watch_new(), \_dbus_watch_ref(), and \_dbus_watch_unref().

The documentation for this struct was generated from the following file:

- dbus-watch.c
