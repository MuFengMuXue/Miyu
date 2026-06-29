DBusTransport Struct Reference

Object representing a transport such as a socket. More...

`#include <``dbus-transport-protected.h``>`

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a1a6554a692a353f8402c1419cd94e904" class="memitem:a1a6554a692a353f8402c1419cd94e904">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">refcount</td>
</tr>
<tr class="memdesc:a1a6554a692a353f8402c1419cd94e904">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reference count.<br />
</td>
</tr>
<tr class="separator:a1a6554a692a353f8402c1419cd94e904">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a7350850a4e02a7eaa4036eb47d4778e5" class="memitem:a7350850a4e02a7eaa4036eb47d4778e5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const DBusTransportVTable * </td>
<td class="memItemRight" data-valign="bottom">vtable</td>
</tr>
<tr class="memdesc:a7350850a4e02a7eaa4036eb47d4778e5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Virtual methods for this instance.<br />
</td>
</tr>
<tr class="separator:a7350850a4e02a7eaa4036eb47d4778e5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a8abdfc9327aa30550982c83b45354651" class="memitem:a8abdfc9327aa30550982c83b45354651">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusConnection * </td>
<td class="memItemRight" data-valign="bottom">connection</td>
</tr>
<tr class="memdesc:a8abdfc9327aa30550982c83b45354651">
<td class="mdescLeft"> </td>
<td class="mdescRight">Connection owning this transport.<br />
</td>
</tr>
<tr class="separator:a8abdfc9327aa30550982c83b45354651">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aaaba590c281236d176600016b7edab48" class="memitem:aaaba590c281236d176600016b7edab48">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMessageLoader * </td>
<td class="memItemRight" data-valign="bottom">loader</td>
</tr>
<tr class="memdesc:aaaba590c281236d176600016b7edab48">
<td class="mdescLeft"> </td>
<td class="mdescRight">Message-loading buffer.<br />
</td>
</tr>
<tr class="separator:aaaba590c281236d176600016b7edab48">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_acf71c91312f325be13ce6c09298b1eb8" class="memitem:acf71c91312f325be13ce6c09298b1eb8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusAuth * </td>
<td class="memItemRight" data-valign="bottom">auth</td>
</tr>
<tr class="memdesc:acf71c91312f325be13ce6c09298b1eb8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Authentication conversation.<br />
</td>
</tr>
<tr class="separator:acf71c91312f325be13ce6c09298b1eb8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_acb3d5fe913d4c281f3495e95cd450c57" class="memitem:acb3d5fe913d4c281f3495e95cd450c57">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusCredentials * </td>
<td class="memItemRight" data-valign="bottom">credentials</td>
</tr>
<tr class="memdesc:acb3d5fe913d4c281f3495e95cd450c57">
<td class="mdescLeft"> </td>
<td class="mdescRight">Credentials of other end read from the socket.<br />
</td>
</tr>
<tr class="separator:acb3d5fe913d4c281f3495e95cd450c57">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a23e0925741fc1c4ba3a369bac4bca4b6" class="memitem:a23e0925741fc1c4ba3a369bac4bca4b6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">long </td>
<td class="memItemRight" data-valign="bottom">max_live_messages_size</td>
</tr>
<tr class="memdesc:a23e0925741fc1c4ba3a369bac4bca4b6">
<td class="mdescLeft"> </td>
<td class="mdescRight">Max total size of received messages.<br />
</td>
</tr>
<tr class="separator:a23e0925741fc1c4ba3a369bac4bca4b6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a2d96972bbc56b78360cb0cfaa3f30266" class="memitem:a2d96972bbc56b78360cb0cfaa3f30266">
<td class="memItemLeft" style="text-align: right;" data-valign="top">long </td>
<td class="memItemRight" data-valign="bottom">max_live_messages_unix_fds</td>
</tr>
<tr class="memdesc:a2d96972bbc56b78360cb0cfaa3f30266">
<td class="mdescLeft"> </td>
<td class="mdescRight">Max total unix fds of received messages.<br />
</td>
</tr>
<tr class="separator:a2d96972bbc56b78360cb0cfaa3f30266">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_afb19bae6f7cfe595f3f1ae0ce53ccab0" class="memitem:afb19bae6f7cfe595f3f1ae0ce53ccab0">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusCounter * </td>
<td class="memItemRight" data-valign="bottom">live_messages</td>
</tr>
<tr class="memdesc:afb19bae6f7cfe595f3f1ae0ce53ccab0">
<td class="mdescLeft"> </td>
<td class="mdescRight">Counter for size/unix fds of all live messages.<br />
</td>
</tr>
<tr class="separator:afb19bae6f7cfe595f3f1ae0ce53ccab0">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a586180e57d80c428fc81e579d9159cb2" class="memitem:a586180e57d80c428fc81e579d9159cb2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char * </td>
<td class="memItemRight" data-valign="bottom">address</td>
</tr>
<tr class="memdesc:a586180e57d80c428fc81e579d9159cb2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Address of the server we are connecting to (NULL for the server side of a transport)<br />
</td>
</tr>
<tr class="separator:a586180e57d80c428fc81e579d9159cb2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aaad7cb51a3e4ff2dd900ac971cc52b36" class="memitem:aaad7cb51a3e4ff2dd900ac971cc52b36">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char * </td>
<td class="memItemRight" data-valign="bottom">expected_guid</td>
</tr>
<tr class="memdesc:aaad7cb51a3e4ff2dd900ac971cc52b36">
<td class="mdescLeft"> </td>
<td class="mdescRight">GUID we expect the server to have, NULL on server side or if we don't have an expectation.<br />
</td>
</tr>
<tr class="separator:aaad7cb51a3e4ff2dd900ac971cc52b36">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ac83be11f3497da6a21aed51782cd68d0" class="memitem:ac83be11f3497da6a21aed51782cd68d0">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusAllowUnixUserFunction </td>
<td class="memItemRight" data-valign="bottom">unix_user_function</td>
</tr>
<tr class="memdesc:ac83be11f3497da6a21aed51782cd68d0">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function for checking whether a user is authorized.<br />
</td>
</tr>
<tr class="separator:ac83be11f3497da6a21aed51782cd68d0">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a7df35abee6aeef69eff659d65dd430f4" class="memitem:a7df35abee6aeef69eff659d65dd430f4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">unix_user_data</td>
</tr>
<tr class="memdesc:a7df35abee6aeef69eff659d65dd430f4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Data for unix_user_function.<br />
</td>
</tr>
<tr class="separator:a7df35abee6aeef69eff659d65dd430f4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a754f10d16c06f373464fe6bf88a15cdd" class="memitem:a754f10d16c06f373464fe6bf88a15cdd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusFreeFunction </td>
<td class="memItemRight" data-valign="bottom">free_unix_user_data</td>
</tr>
<tr class="memdesc:a754f10d16c06f373464fe6bf88a15cdd">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to free unix_user_data.<br />
</td>
</tr>
<tr class="separator:a754f10d16c06f373464fe6bf88a15cdd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a17403591c2a1d936be5ed13a36e6416a" class="memitem:a17403591c2a1d936be5ed13a36e6416a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusAllowWindowsUserFunction </td>
<td class="memItemRight" data-valign="bottom">windows_user_function</td>
</tr>
<tr class="memdesc:a17403591c2a1d936be5ed13a36e6416a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function for checking whether a user is authorized.<br />
</td>
</tr>
<tr class="separator:a17403591c2a1d936be5ed13a36e6416a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a333c4300fe345d25e9dcb828d20baff7" class="memitem:a333c4300fe345d25e9dcb828d20baff7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">windows_user_data</td>
</tr>
<tr class="memdesc:a333c4300fe345d25e9dcb828d20baff7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Data for windows_user_function.<br />
</td>
</tr>
<tr class="separator:a333c4300fe345d25e9dcb828d20baff7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aab0e5248bd01f31ac4dcdab3c3b7b570" class="memitem:aab0e5248bd01f31ac4dcdab3c3b7b570">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusFreeFunction </td>
<td class="memItemRight" data-valign="bottom">free_windows_user_data</td>
</tr>
<tr class="memdesc:aab0e5248bd01f31ac4dcdab3c3b7b570">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to free windows_user_data.<br />
</td>
</tr>
<tr class="separator:aab0e5248bd01f31ac4dcdab3c3b7b570">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a487a7375e94efba850f8344a252cfa63" class="memitem:a487a7375e94efba850f8344a252cfa63">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">disconnected: 1</td>
</tr>
<tr class="memdesc:a487a7375e94efba850f8344a252cfa63">
<td class="mdescLeft"> </td>
<td class="mdescRight">TRUE if we are disconnected.<br />
</td>
</tr>
<tr class="separator:a487a7375e94efba850f8344a252cfa63">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a12d3052e51b2f0bf398d48e31e5f9da8" class="memitem:a12d3052e51b2f0bf398d48e31e5f9da8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">authenticated: 1</td>
</tr>
<tr class="memdesc:a12d3052e51b2f0bf398d48e31e5f9da8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Cache of auth state; use _dbus_transport_peek_is_authenticated() to query value.<br />
</td>
</tr>
<tr class="separator:a12d3052e51b2f0bf398d48e31e5f9da8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a7d91848b94203022be1090d93dd2cd04" class="memitem:a7d91848b94203022be1090d93dd2cd04">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">send_credentials_pending: 1</td>
</tr>
<tr class="memdesc:a7d91848b94203022be1090d93dd2cd04">
<td class="mdescLeft"> </td>
<td class="mdescRight">TRUE if we need to send credentials<br />
</td>
</tr>
<tr class="separator:a7d91848b94203022be1090d93dd2cd04">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aaa29089fbb1fbdb5b412b3ed18c84b2d" class="memitem:aaa29089fbb1fbdb5b412b3ed18c84b2d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">receive_credentials_pending: 1</td>
</tr>
<tr class="memdesc:aaa29089fbb1fbdb5b412b3ed18c84b2d">
<td class="mdescLeft"> </td>
<td class="mdescRight">TRUE if we need to receive credentials<br />
</td>
</tr>
<tr class="separator:aaa29089fbb1fbdb5b412b3ed18c84b2d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a38fa70b1473eb08a6c871c7791b46d6e" class="memitem:a38fa70b1473eb08a6c871c7791b46d6e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">is_server: 1</td>
</tr>
<tr class="memdesc:a38fa70b1473eb08a6c871c7791b46d6e">
<td class="mdescLeft"> </td>
<td class="mdescRight">TRUE if on the server side<br />
</td>
</tr>
<tr class="separator:a38fa70b1473eb08a6c871c7791b46d6e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a6a546ecc2f6467a51973681d0b816809" class="memitem:a6a546ecc2f6467a51973681d0b816809">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">unused_bytes_recovered: 1</td>
</tr>
<tr class="memdesc:a6a546ecc2f6467a51973681d0b816809">
<td class="mdescLeft"> </td>
<td class="mdescRight">TRUE if we've recovered unused bytes from auth<br />
</td>
</tr>
<tr class="separator:a6a546ecc2f6467a51973681d0b816809">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a30a82ca7826ef4735a5caa4c921ec014" class="memitem:a30a82ca7826ef4735a5caa4c921ec014">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">allow_anonymous: 1</td>
</tr>
<tr class="memdesc:a30a82ca7826ef4735a5caa4c921ec014">
<td class="mdescLeft"> </td>
<td class="mdescRight">TRUE if an anonymous client can connect<br />
</td>
</tr>
<tr class="separator:a30a82ca7826ef4735a5caa4c921ec014">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Object representing a transport such as a socket.

A transport can shuttle messages from point A to point B, and is the backend for a DBusConnection.

Definition at line 82 of file dbus-transport-protected.h.

## Field Documentation

## ◆ address

|                               |
|-------------------------------|
| char\* DBusTransport::address |

Address of the server we are connecting to (NULL for the server side of a transport)

Definition at line 101 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_finalize_base(), \_dbus_transport_get_address(), and \_dbus_transport_init_base().

## ◆ allow_anonymous

|                                             |
|---------------------------------------------|
| unsigned int DBusTransport::allow_anonymous |

TRUE if an anonymous client can connect

Definition at line 121 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_set_allow_anonymous().

## ◆ auth

|                                |
|--------------------------------|
| DBusAuth\* DBusTransport::auth |

Authentication conversation.

Definition at line 92 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_finalize_base(), \_dbus_transport_get_adt_audit_session_data(), \_dbus_transport_get_credentials(), \_dbus_transport_get_dispatch_status(), \_dbus_transport_get_is_anonymous(), \_dbus_transport_get_server_id(), \_dbus_transport_get_unix_process_id(), \_dbus_transport_get_unix_user(), \_dbus_transport_get_windows_user(), \_dbus_transport_init_base(), \_dbus_transport_new_for_socket(), \_dbus_transport_set_auth_mechanisms(), and \_dbus_transport_try_to_authenticate().

## ◆ authenticated

|                                           |
|-------------------------------------------|
| unsigned int DBusTransport::authenticated |

Cache of auth state; use \_dbus_transport_peek_is_authenticated() to query value.

Definition at line 116 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_get_adt_audit_session_data(), \_dbus_transport_get_credentials(), \_dbus_transport_get_is_anonymous(), \_dbus_transport_get_server_id(), \_dbus_transport_get_unix_process_id(), \_dbus_transport_get_unix_user(), \_dbus_transport_get_windows_user(), \_dbus_transport_init_base(), \_dbus_transport_peek_is_authenticated(), and \_dbus_transport_try_to_authenticate().

## ◆ connection

|                                            |
|--------------------------------------------|
| DBusConnection\* DBusTransport::connection |

Connection owning this transport.

Definition at line 88 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_queue_messages(), \_dbus_transport_set_connection(), and \_dbus_transport_try_to_authenticate().

## ◆ credentials

|                                              |
|----------------------------------------------|
| DBusCredentials\* DBusTransport::credentials |

Credentials of other end read from the socket.

Definition at line 94 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_finalize_base(), and \_dbus_transport_init_base().

## ◆ disconnected

|                                          |
|------------------------------------------|
| unsigned int DBusTransport::disconnected |

TRUE if we are disconnected.

Definition at line 115 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_disconnect(), \_dbus_transport_do_iteration(), \_dbus_transport_finalize_base(), \_dbus_transport_get_is_connected(), \_dbus_transport_get_socket_fd(), \_dbus_transport_handle_watch(), \_dbus_transport_init_base(), and \_dbus_transport_try_to_authenticate().

## ◆ expected_guid

|                                     |
|-------------------------------------|
| char\* DBusTransport::expected_guid |

GUID we expect the server to have, NULL on server side or if we don't have an expectation.

Definition at line 103 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_finalize_base(), \_dbus_transport_get_server_id(), \_dbus_transport_init_base(), \_dbus_transport_open(), and \_dbus_transport_try_to_authenticate().

## ◆ free_unix_user_data

|                                                     |
|-----------------------------------------------------|
| DBusFreeFunction DBusTransport::free_unix_user_data |

Function to free unix_user_data.

Definition at line 108 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_finalize_base(), \_dbus_transport_init_base(), and \_dbus_transport_set_unix_user_function().

## ◆ free_windows_user_data

|                                                        |
|--------------------------------------------------------|
| DBusFreeFunction DBusTransport::free_windows_user_data |

Function to free windows_user_data.

Definition at line 113 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_finalize_base(), \_dbus_transport_init_base(), and \_dbus_transport_set_windows_user_function().

## ◆ is_server

|                                       |
|---------------------------------------|
| unsigned int DBusTransport::is_server |

TRUE if on the server side

Definition at line 119 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_get_server_id(), \_dbus_transport_init_base(), and \_dbus_transport_try_to_authenticate().

## ◆ live_messages

|                                            |
|--------------------------------------------|
| DBusCounter\* DBusTransport::live_messages |

Counter for size/unix fds of all live messages.

Definition at line 99 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_finalize_base(), \_dbus_transport_get_dispatch_status(), \_dbus_transport_init_base(), \_dbus_transport_queue_messages(), \_dbus_transport_set_max_received_size(), and \_dbus_transport_set_max_received_unix_fds().

## ◆ loader

|                                           |
|-------------------------------------------|
| DBusMessageLoader\* DBusTransport::loader |

Message-loading buffer.

Definition at line 90 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_finalize_base(), \_dbus_transport_get_dispatch_status(), \_dbus_transport_get_max_message_size(), \_dbus_transport_get_max_message_unix_fds(), \_dbus_transport_get_pending_fds_count(), \_dbus_transport_init_base(), \_dbus_transport_queue_messages(), \_dbus_transport_set_max_message_size(), \_dbus_transport_set_max_message_unix_fds(), and \_dbus_transport_set_pending_fds_function().

## ◆ max_live_messages_size

|                                            |
|--------------------------------------------|
| long DBusTransport::max_live_messages_size |

Max total size of received messages.

Definition at line 96 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_get_dispatch_status(), \_dbus_transport_get_max_received_size(), \_dbus_transport_init_base(), \_dbus_transport_set_max_received_size(), and \_dbus_transport_set_max_received_unix_fds().

## ◆ max_live_messages_unix_fds

|                                                |
|------------------------------------------------|
| long DBusTransport::max_live_messages_unix_fds |

Max total unix fds of received messages.

Definition at line 97 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_get_dispatch_status(), \_dbus_transport_get_max_received_unix_fds(), \_dbus_transport_init_base(), \_dbus_transport_set_max_received_size(), and \_dbus_transport_set_max_received_unix_fds().

## ◆ receive_credentials_pending

|                                                         |
|---------------------------------------------------------|
| unsigned int DBusTransport::receive_credentials_pending |

TRUE if we need to receive credentials

Definition at line 118 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_init_base(), and \_dbus_transport_try_to_authenticate().

## ◆ refcount

|                             |
|-----------------------------|
| int DBusTransport::refcount |

Reference count.

Definition at line 84 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_init_base(), \_dbus_transport_ref(), and \_dbus_transport_unref().

## ◆ send_credentials_pending

|                                                      |
|------------------------------------------------------|
| unsigned int DBusTransport::send_credentials_pending |

TRUE if we need to send credentials

Definition at line 117 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_init_base(), and \_dbus_transport_try_to_authenticate().

## ◆ unix_user_data

|                                      |
|--------------------------------------|
| void\* DBusTransport::unix_user_data |

Data for unix_user_function.

Definition at line 106 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_finalize_base(), \_dbus_transport_init_base(), and \_dbus_transport_set_unix_user_function().

## ◆ unix_user_function

|                                                             |
|-------------------------------------------------------------|
| DBusAllowUnixUserFunction DBusTransport::unix_user_function |

Function for checking whether a user is authorized.

Definition at line 105 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_init_base(), \_dbus_transport_set_unix_user_function(), and \_dbus_transport_try_to_authenticate().

## ◆ unused_bytes_recovered

|                                                    |
|----------------------------------------------------|
| unsigned int DBusTransport::unused_bytes_recovered |

TRUE if we've recovered unused bytes from auth

Definition at line 120 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_get_dispatch_status().

## ◆ vtable

|                                                   |
|---------------------------------------------------|
| const DBusTransportVTable\* DBusTransport::vtable |

Virtual methods for this instance.

Definition at line 86 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_disconnect(), \_dbus_transport_do_iteration(), \_dbus_transport_get_socket_fd(), \_dbus_transport_handle_watch(), \_dbus_transport_init_base(), \_dbus_transport_queue_messages(), \_dbus_transport_set_connection(), and \_dbus_transport_unref().

## ◆ windows_user_data

|                                         |
|-----------------------------------------|
| void\* DBusTransport::windows_user_data |

Data for windows_user_function.

Definition at line 111 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_finalize_base(), \_dbus_transport_init_base(), and \_dbus_transport_set_windows_user_function().

## ◆ windows_user_function

|                                                                   |
|-------------------------------------------------------------------|
| DBusAllowWindowsUserFunction DBusTransport::windows_user_function |

Function for checking whether a user is authorized.

Definition at line 110 of file dbus-transport-protected.h.

Referenced by \_dbus_transport_init_base(), \_dbus_transport_set_windows_user_function(), and \_dbus_transport_try_to_authenticate().

The documentation for this struct was generated from the following file:

- dbus-transport-protected.h
