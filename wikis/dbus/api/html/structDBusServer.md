DBusServer Struct Reference

D-Bus secret internal implementation details » DBusServer implementation details

Internals of DBusServer object. More...

`#include <``dbus-server-protected.h``>`

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a7578bd99fc8aee641cbb5198cb2e7004" class="memitem:a7578bd99fc8aee641cbb5198cb2e7004">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusAtomic </td>
<td class="memItemRight" data-valign="bottom">refcount</td>
</tr>
<tr class="memdesc:a7578bd99fc8aee641cbb5198cb2e7004">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reference count.<br />
</td>
</tr>
<tr class="separator:a7578bd99fc8aee641cbb5198cb2e7004">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aa5068890fea8c7e7261b600e7256e009" class="memitem:aa5068890fea8c7e7261b600e7256e009">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const DBusServerVTable * </td>
<td class="memItemRight" data-valign="bottom">vtable</td>
</tr>
<tr class="memdesc:aa5068890fea8c7e7261b600e7256e009">
<td class="mdescLeft"> </td>
<td class="mdescRight">Virtual methods for this instance.<br />
</td>
</tr>
<tr class="separator:aa5068890fea8c7e7261b600e7256e009">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a89c4751e61ed16591254b00cb9db1661" class="memitem:a89c4751e61ed16591254b00cb9db1661">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusRMutex * </td>
<td class="memItemRight" data-valign="bottom">mutex</td>
</tr>
<tr class="memdesc:a89c4751e61ed16591254b00cb9db1661">
<td class="mdescLeft"> </td>
<td class="mdescRight">Lock on the server object.<br />
</td>
</tr>
<tr class="separator:a89c4751e61ed16591254b00cb9db1661">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a799a94be0e3078f2e636f322f57d66f9" class="memitem:a799a94be0e3078f2e636f322f57d66f9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusGUID </td>
<td class="memItemRight" data-valign="bottom">guid</td>
</tr>
<tr class="memdesc:a799a94be0e3078f2e636f322f57d66f9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Globally unique ID of server.<br />
</td>
</tr>
<tr class="separator:a799a94be0e3078f2e636f322f57d66f9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a79cd5d1b25412d56b7fd41902d575794" class="memitem:a79cd5d1b25412d56b7fd41902d575794">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusString </td>
<td class="memItemRight" data-valign="bottom">guid_hex</td>
</tr>
<tr class="memdesc:a79cd5d1b25412d56b7fd41902d575794">
<td class="mdescLeft"> </td>
<td class="mdescRight">Hex-encoded version of GUID.<br />
</td>
</tr>
<tr class="separator:a79cd5d1b25412d56b7fd41902d575794">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a7955050967aeaf09679f8ba1f2941880" class="memitem:a7955050967aeaf09679f8ba1f2941880">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusWatchList * </td>
<td class="memItemRight" data-valign="bottom">watches</td>
</tr>
<tr class="memdesc:a7955050967aeaf09679f8ba1f2941880">
<td class="mdescLeft"> </td>
<td class="mdescRight">Our watches.<br />
</td>
</tr>
<tr class="separator:a7955050967aeaf09679f8ba1f2941880">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_afcaccd00f2392a390616c47e425bae85" class="memitem:afcaccd00f2392a390616c47e425bae85">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusTimeoutList * </td>
<td class="memItemRight" data-valign="bottom">timeouts</td>
</tr>
<tr class="memdesc:afcaccd00f2392a390616c47e425bae85">
<td class="mdescLeft"> </td>
<td class="mdescRight">Our timeouts.<br />
</td>
</tr>
<tr class="separator:afcaccd00f2392a390616c47e425bae85">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a359852bf33b3051180a9477da4d89acd" class="memitem:a359852bf33b3051180a9477da4d89acd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char * </td>
<td class="memItemRight" data-valign="bottom">address</td>
</tr>
<tr class="memdesc:a359852bf33b3051180a9477da4d89acd">
<td class="mdescLeft"> </td>
<td class="mdescRight">Address this server is listening on.<br />
</td>
</tr>
<tr class="separator:a359852bf33b3051180a9477da4d89acd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a01a6dbb2573ce35f639873cd4dd85b4d" class="memitem:a01a6dbb2573ce35f639873cd4dd85b4d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">published_address</td>
</tr>
<tr class="memdesc:a01a6dbb2573ce35f639873cd4dd85b4d">
<td class="mdescLeft"> </td>
<td class="mdescRight">flag which indicates that server has published its bus address.<br />
</td>
</tr>
<tr class="separator:a01a6dbb2573ce35f639873cd4dd85b4d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a8f0fac02d4c6f9e5ff353cf696b6d991" class="memitem:a8f0fac02d4c6f9e5ff353cf696b6d991">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">max_connections</td>
</tr>
<tr class="memdesc:a8f0fac02d4c6f9e5ff353cf696b6d991">
<td class="mdescLeft"> </td>
<td class="mdescRight">Max number of connections allowed at once.<br />
</td>
</tr>
<tr class="separator:a8f0fac02d4c6f9e5ff353cf696b6d991">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a0601cca8307ba17d4a8bcebe48b08362" class="memitem:a0601cca8307ba17d4a8bcebe48b08362">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusDataSlotList </td>
<td class="memItemRight" data-valign="bottom">slot_list</td>
</tr>
<tr class="memdesc:a0601cca8307ba17d4a8bcebe48b08362">
<td class="mdescLeft"> </td>
<td class="mdescRight">Data stored by allocated integer ID.<br />
</td>
</tr>
<tr class="separator:a0601cca8307ba17d4a8bcebe48b08362">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a964ff125a29a7dac02f81e1a26233ff6" class="memitem:a964ff125a29a7dac02f81e1a26233ff6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusNewConnectionFunction </td>
<td class="memItemRight" data-valign="bottom">new_connection_function</td>
</tr>
<tr class="memdesc:a964ff125a29a7dac02f81e1a26233ff6">
<td class="mdescLeft"> </td>
<td class="mdescRight">Callback to invoke when a new connection is created.<br />
</td>
</tr>
<tr class="separator:a964ff125a29a7dac02f81e1a26233ff6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_acfba406ae6f288887feaccc3d621d094" class="memitem:acfba406ae6f288887feaccc3d621d094">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">new_connection_data</td>
</tr>
<tr class="memdesc:acfba406ae6f288887feaccc3d621d094">
<td class="mdescLeft"> </td>
<td class="mdescRight">Data for new connection callback.<br />
</td>
</tr>
<tr class="separator:acfba406ae6f288887feaccc3d621d094">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a5d5b68a92cf47a3eb50e5e6ec7d2ca3a" class="memitem:a5d5b68a92cf47a3eb50e5e6ec7d2ca3a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusFreeFunction </td>
<td class="memItemRight" data-valign="bottom">new_connection_free_data_function</td>
</tr>
<tr class="memdesc:a5d5b68a92cf47a3eb50e5e6ec7d2ca3a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Callback to invoke to free new_connection_data when server is finalized or data is replaced.<br />
</td>
</tr>
<tr class="separator:a5d5b68a92cf47a3eb50e5e6ec7d2ca3a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_adc1032bbed41413e5d0e01578f2bfffc" class="memitem:adc1032bbed41413e5d0e01578f2bfffc">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char ** </td>
<td class="memItemRight" data-valign="bottom">auth_mechanisms</td>
</tr>
<tr class="memdesc:adc1032bbed41413e5d0e01578f2bfffc">
<td class="mdescLeft"> </td>
<td class="mdescRight">Array of allowed authentication mechanisms.<br />
</td>
</tr>
<tr class="separator:adc1032bbed41413e5d0e01578f2bfffc">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a7dabb30cdc09d6102810029fb56b8dfe" class="memitem:a7dabb30cdc09d6102810029fb56b8dfe">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">disconnected: 1</td>
</tr>
<tr class="memdesc:a7dabb30cdc09d6102810029fb56b8dfe">
<td class="mdescLeft"> </td>
<td class="mdescRight">TRUE if we are disconnected.<br />
</td>
</tr>
<tr class="separator:a7dabb30cdc09d6102810029fb56b8dfe">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_adba8dd016471a800525a42926f9ee061" class="memitem:adba8dd016471a800525a42926f9ee061">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">have_server_lock: 1</td>
</tr>
<tr class="memdesc:adba8dd016471a800525a42926f9ee061">
<td class="mdescLeft"> </td>
<td class="mdescRight">Does someone have the server mutex locked.<br />
</td>
</tr>
<tr class="separator:adba8dd016471a800525a42926f9ee061">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Internals of DBusServer object.

Definition at line 58 of file dbus-server-protected.h.

## Field Documentation

## ◆ address

|                            |
|----------------------------|
| char\* DBusServer::address |

Address this server is listening on.

Definition at line 71 of file dbus-server-protected.h.

Referenced by \_dbus_server_finalize_base(), \_dbus_server_init_base(), and dbus_server_get_address().

## ◆ auth_mechanisms

|                                      |
|--------------------------------------|
| char\*\* DBusServer::auth_mechanisms |

Array of allowed authentication mechanisms.

Definition at line 87 of file dbus-server-protected.h.

Referenced by \_dbus_server_finalize_base(), and dbus_server_set_auth_mechanisms().

## ◆ disconnected

|                                       |
|---------------------------------------|
| unsigned int DBusServer::disconnected |

TRUE if we are disconnected.

Definition at line 89 of file dbus-server-protected.h.

Referenced by \_dbus_server_finalize_base(), \_dbus_server_unref_unlocked(), dbus_server_get_is_connected(), and dbus_server_unref().

## ◆ guid

|                           |
|---------------------------|
| DBusGUID DBusServer::guid |

Globally unique ID of server.

Definition at line 64 of file dbus-server-protected.h.

Referenced by \_dbus_server_init_base().

## ◆ guid_hex

|                                 |
|---------------------------------|
| DBusString DBusServer::guid_hex |

Hex-encoded version of GUID.

Definition at line 66 of file dbus-server-protected.h.

Referenced by \_dbus_server_finalize_base(), \_dbus_server_init_base(), and dbus_server_get_id().

## ◆ have_server_lock

|                                           |
|-------------------------------------------|
| unsigned int DBusServer::have_server_lock |

Does someone have the server mutex locked.

Definition at line 92 of file dbus-server-protected.h.

Referenced by \_dbus_server_finalize_base().

## ◆ max_connections

|                                 |
|---------------------------------|
| int DBusServer::max_connections |

Max number of connections allowed at once.

Definition at line 74 of file dbus-server-protected.h.

## ◆ mutex

|                                |
|--------------------------------|
| DBusRMutex\* DBusServer::mutex |

Lock on the server object.

Definition at line 62 of file dbus-server-protected.h.

Referenced by \_dbus_server_finalize_base(), and \_dbus_server_init_base().

## ◆ new_connection_data

|                                        |
|----------------------------------------|
| void\* DBusServer::new_connection_data |

Data for new connection callback.

Definition at line 80 of file dbus-server-protected.h.

Referenced by dbus_server_set_new_connection_function().

## ◆ new_connection_free_data_function

|                                                                |
|----------------------------------------------------------------|
| DBusFreeFunction DBusServer::new_connection_free_data_function |

Callback to invoke to free new_connection_data when server is finalized or data is replaced.

Definition at line 82 of file dbus-server-protected.h.

Referenced by dbus_server_set_new_connection_function().

## ◆ new_connection_function

|                                                               |
|---------------------------------------------------------------|
| DBusNewConnectionFunction DBusServer::new_connection_function |

Callback to invoke when a new connection is created.

Definition at line 78 of file dbus-server-protected.h.

Referenced by dbus_server_set_new_connection_function().

## ◆ published_address

|                                           |
|-------------------------------------------|
| dbus_bool_t DBusServer::published_address |

flag which indicates that server has published its bus address.

Definition at line 72 of file dbus-server-protected.h.

Referenced by \_dbus_server_init_base().

## ◆ refcount

|                                 |
|---------------------------------|
| DBusAtomic DBusServer::refcount |

Reference count.

Definition at line 60 of file dbus-server-protected.h.

Referenced by \_dbus_server_init_base(), \_dbus_server_ref_unlocked(), \_dbus_server_unref_unlocked(), dbus_server_ref(), and dbus_server_unref().

## ◆ slot_list

|                                        |
|----------------------------------------|
| DBusDataSlotList DBusServer::slot_list |

Data stored by allocated integer ID.

Definition at line 76 of file dbus-server-protected.h.

Referenced by \_dbus_server_finalize_base(), \_dbus_server_init_base(), dbus_server_get_data(), and dbus_server_set_data().

## ◆ timeouts

|                                        |
|----------------------------------------|
| DBusTimeoutList\* DBusServer::timeouts |

Our timeouts.

Definition at line 69 of file dbus-server-protected.h.

Referenced by \_dbus_server_finalize_base(), \_dbus_server_init_base(), and dbus_server_set_timeout_functions().

## ◆ vtable

|                                             |
|---------------------------------------------|
| const DBusServerVTable\* DBusServer::vtable |

Virtual methods for this instance.

Definition at line 61 of file dbus-server-protected.h.

Referenced by \_dbus_server_init_base(), \_dbus_server_unref_unlocked(), and dbus_server_unref().

## ◆ watches

|                                     |
|-------------------------------------|
| DBusWatchList\* DBusServer::watches |

Our watches.

Definition at line 68 of file dbus-server-protected.h.

Referenced by \_dbus_server_finalize_base(), \_dbus_server_init_base(), \_dbus_server_toggle_all_watches(), and dbus_server_set_watch_functions().

The documentation for this struct was generated from the following file:

- dbus-server-protected.h
