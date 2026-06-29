DBusAuth Struct Reference

D-Bus secret internal implementation details » Authentication implementation details

Internal members of DBusAuth. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_ab91763afd6a9d19f821dffd5930e69a6" class="memitem:ab91763afd6a9d19f821dffd5930e69a6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">refcount</td>
</tr>
<tr class="memdesc:ab91763afd6a9d19f821dffd5930e69a6">
<td class="mdescLeft"> </td>
<td class="mdescRight">reference count<br />
</td>
</tr>
<tr class="separator:ab91763afd6a9d19f821dffd5930e69a6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a8b930cb0d8a76c198914cf4a98192477" class="memitem:a8b930cb0d8a76c198914cf4a98192477">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">side</td>
</tr>
<tr class="memdesc:a8b930cb0d8a76c198914cf4a98192477">
<td class="mdescLeft"> </td>
<td class="mdescRight">Client or server.<br />
</td>
</tr>
<tr class="separator:a8b930cb0d8a76c198914cf4a98192477">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a986a475be9c96ecb9dd9ca5f86f60f10" class="memitem:a986a475be9c96ecb9dd9ca5f86f60f10">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusString </td>
<td class="memItemRight" data-valign="bottom">incoming</td>
</tr>
<tr class="memdesc:a986a475be9c96ecb9dd9ca5f86f60f10">
<td class="mdescLeft"> </td>
<td class="mdescRight">Incoming data buffer.<br />
</td>
</tr>
<tr class="separator:a986a475be9c96ecb9dd9ca5f86f60f10">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ae57f6861636a989dc3bd7a24d6731085" class="memitem:ae57f6861636a989dc3bd7a24d6731085">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusString </td>
<td class="memItemRight" data-valign="bottom">outgoing</td>
</tr>
<tr class="memdesc:ae57f6861636a989dc3bd7a24d6731085">
<td class="mdescLeft"> </td>
<td class="mdescRight">Outgoing data buffer.<br />
</td>
</tr>
<tr class="separator:ae57f6861636a989dc3bd7a24d6731085">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a44bd9f6e01ee93e58aae551bb1a9fb0f" class="memitem:a44bd9f6e01ee93e58aae551bb1a9fb0f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const DBusAuthStateData * </td>
<td class="memItemRight" data-valign="bottom">state</td>
</tr>
<tr class="memdesc:a44bd9f6e01ee93e58aae551bb1a9fb0f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Current protocol state.<br />
</td>
</tr>
<tr class="separator:a44bd9f6e01ee93e58aae551bb1a9fb0f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a1c284d7d38784b7ad81507199f33f848" class="memitem:a1c284d7d38784b7ad81507199f33f848">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const DBusAuthMechanismHandler * </td>
<td class="memItemRight" data-valign="bottom">mech</td>
</tr>
<tr class="memdesc:a1c284d7d38784b7ad81507199f33f848">
<td class="mdescLeft"> </td>
<td class="mdescRight">Current auth mechanism.<br />
</td>
</tr>
<tr class="separator:a1c284d7d38784b7ad81507199f33f848">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a8e70b9e2cc090fe006e1214983d79eed" class="memitem:a8e70b9e2cc090fe006e1214983d79eed">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusString </td>
<td class="memItemRight" data-valign="bottom">identity</td>
</tr>
<tr class="memdesc:a8e70b9e2cc090fe006e1214983d79eed">
<td class="mdescLeft"> </td>
<td class="mdescRight">Current identity we're authorizing as.<br />
</td>
</tr>
<tr class="separator:a8e70b9e2cc090fe006e1214983d79eed">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aed82f21abc1ad5aa8c0db8a43f93bc22" class="memitem:aed82f21abc1ad5aa8c0db8a43f93bc22">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusCredentials * </td>
<td class="memItemRight" data-valign="bottom">credentials</td>
</tr>
<tr class="memdesc:aed82f21abc1ad5aa8c0db8a43f93bc22">
<td class="mdescLeft"> </td>
<td class="mdescRight">Credentials read from socket.<br />
</td>
</tr>
<tr class="separator:aed82f21abc1ad5aa8c0db8a43f93bc22">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_afb4928fcc0f7af56d87fd6a512ad5a0a" class="memitem:afb4928fcc0f7af56d87fd6a512ad5a0a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusCredentials * </td>
<td class="memItemRight" data-valign="bottom">authorized_identity</td>
</tr>
<tr class="memdesc:afb4928fcc0f7af56d87fd6a512ad5a0a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Credentials that are authorized.<br />
</td>
</tr>
<tr class="separator:afb4928fcc0f7af56d87fd6a512ad5a0a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a6cfcba06657099d879b1e08aa886420f" class="memitem:a6cfcba06657099d879b1e08aa886420f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusCredentials * </td>
<td class="memItemRight" data-valign="bottom">desired_identity</td>
</tr>
<tr class="memdesc:a6cfcba06657099d879b1e08aa886420f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Identity client has requested.<br />
</td>
</tr>
<tr class="separator:a6cfcba06657099d879b1e08aa886420f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aedf6904d461a6f6eba2ee21f12f89611" class="memitem:aedf6904d461a6f6eba2ee21f12f89611">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusString </td>
<td class="memItemRight" data-valign="bottom">context</td>
</tr>
<tr class="memdesc:aedf6904d461a6f6eba2ee21f12f89611">
<td class="mdescLeft"> </td>
<td class="mdescRight">Cookie scope.<br />
</td>
</tr>
<tr class="separator:aedf6904d461a6f6eba2ee21f12f89611">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ae1048ad3a586619ce6f3730e99ae2db9" class="memitem:ae1048ad3a586619ce6f3730e99ae2db9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusKeyring * </td>
<td class="memItemRight" data-valign="bottom">keyring</td>
</tr>
<tr class="memdesc:ae1048ad3a586619ce6f3730e99ae2db9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Keyring for cookie mechanism.<br />
</td>
</tr>
<tr class="separator:ae1048ad3a586619ce6f3730e99ae2db9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a43851f8413177b398c63e2045605ae4b" class="memitem:a43851f8413177b398c63e2045605ae4b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">cookie_id</td>
</tr>
<tr class="memdesc:a43851f8413177b398c63e2045605ae4b">
<td class="mdescLeft"> </td>
<td class="mdescRight">ID of cookie to use.<br />
</td>
</tr>
<tr class="separator:a43851f8413177b398c63e2045605ae4b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a4f2f7bfce0a53b41fb165a8854804443" class="memitem:a4f2f7bfce0a53b41fb165a8854804443">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusString </td>
<td class="memItemRight" data-valign="bottom">challenge</td>
</tr>
<tr class="memdesc:a4f2f7bfce0a53b41fb165a8854804443">
<td class="mdescLeft"> </td>
<td class="mdescRight">Challenge sent to client.<br />
</td>
</tr>
<tr class="separator:a4f2f7bfce0a53b41fb165a8854804443">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a234096e729cabc43efcc85ce5094a305" class="memitem:a234096e729cabc43efcc85ce5094a305">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char ** </td>
<td class="memItemRight" data-valign="bottom">allowed_mechs</td>
</tr>
<tr class="memdesc:a234096e729cabc43efcc85ce5094a305">
<td class="mdescLeft"> </td>
<td class="mdescRight">Mechanisms we're allowed to use, or NULL if we can use any.<br />
</td>
</tr>
<tr class="separator:a234096e729cabc43efcc85ce5094a305">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a246a00c89875045268403243c76b5166" class="memitem:a246a00c89875045268403243c76b5166">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">needed_memory: 1</td>
</tr>
<tr class="memdesc:a246a00c89875045268403243c76b5166">
<td class="mdescLeft"> </td>
<td class="mdescRight">We needed memory to continue since last successful getting something done.<br />
</td>
</tr>
<tr class="separator:a246a00c89875045268403243c76b5166">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a027172d9bc452832d4a61df9aec4f04a" class="memitem:a027172d9bc452832d4a61df9aec4f04a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">already_got_mechanisms: 1</td>
</tr>
<tr class="memdesc:a027172d9bc452832d4a61df9aec4f04a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Client already got mech list.<br />
</td>
</tr>
<tr class="separator:a027172d9bc452832d4a61df9aec4f04a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ac216729b05c963c58935727594971739" class="memitem:ac216729b05c963c58935727594971739">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">already_asked_for_initial_response: 1</td>
</tr>
<tr class="memdesc:ac216729b05c963c58935727594971739">
<td class="mdescLeft"> </td>
<td class="mdescRight">Already sent a blank challenge to get an initial response.<br />
</td>
</tr>
<tr class="separator:ac216729b05c963c58935727594971739">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_af9809523776f243d5e8f5f631d24562b" class="memitem:af9809523776f243d5e8f5f631d24562b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">buffer_outstanding: 1</td>
</tr>
<tr class="memdesc:af9809523776f243d5e8f5f631d24562b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Buffer is "checked out" for reading data into.<br />
</td>
</tr>
<tr class="separator:af9809523776f243d5e8f5f631d24562b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a7e5d15e7861774d7b49339c452e2829a" class="memitem:a7e5d15e7861774d7b49339c452e2829a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">unix_fd_possible: 1</td>
</tr>
<tr class="memdesc:a7e5d15e7861774d7b49339c452e2829a">
<td class="mdescLeft"> </td>
<td class="mdescRight">This side could do unix fd passing.<br />
</td>
</tr>
<tr class="separator:a7e5d15e7861774d7b49339c452e2829a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_af363f74ce5f14b2a63ea0ef71b3d3bd3" class="memitem:af363f74ce5f14b2a63ea0ef71b3d3bd3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">unix_fd_negotiated: 1</td>
</tr>
<tr class="memdesc:af363f74ce5f14b2a63ea0ef71b3d3bd3">
<td class="mdescLeft"> </td>
<td class="mdescRight">Unix fd was successfully negotiated.<br />
</td>
</tr>
<tr class="separator:af363f74ce5f14b2a63ea0ef71b3d3bd3">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Internal members of DBusAuth.

Definition at line 155 of file dbus-auth.c.

## Field Documentation

## ◆ allowed_mechs

|                                  |
|----------------------------------|
| char\*\* DBusAuth::allowed_mechs |

Mechanisms we're allowed to use, or NULL if we can use any.

Definition at line 183 of file dbus-auth.c.

Referenced by \_dbus_auth_set_mechanisms(), and \_dbus_auth_unref().

## ◆ already_asked_for_initial_response

|                                                           |
|-----------------------------------------------------------|
| unsigned int DBusAuth::already_asked_for_initial_response |

Already sent a blank challenge to get an initial response.

Definition at line 191 of file dbus-auth.c.

## ◆ already_got_mechanisms

|                                               |
|-----------------------------------------------|
| unsigned int DBusAuth::already_got_mechanisms |

Client already got mech list.

Definition at line 190 of file dbus-auth.c.

## ◆ authorized_identity

|                                                 |
|-------------------------------------------------|
| DBusCredentials\* DBusAuth::authorized_identity |

Credentials that are authorized.

Definition at line 174 of file dbus-auth.c.

Referenced by \_dbus_auth_get_identity(), and \_dbus_auth_unref().

## ◆ buffer_outstanding

|                                           |
|-------------------------------------------|
| unsigned int DBusAuth::buffer_outstanding |

Buffer is "checked out" for reading data into.

Definition at line 192 of file dbus-auth.c.

Referenced by \_dbus_auth_get_buffer(), and \_dbus_auth_return_buffer().

## ◆ challenge

|                                |
|--------------------------------|
| DBusString DBusAuth::challenge |

Challenge sent to client.

Definition at line 181 of file dbus-auth.c.

Referenced by \_dbus_auth_unref().

## ◆ context

|                              |
|------------------------------|
| DBusString DBusAuth::context |

Cookie scope.

Definition at line 178 of file dbus-auth.c.

Referenced by \_dbus_auth_set_context(), and \_dbus_auth_unref().

## ◆ cookie_id

|                         |
|-------------------------|
| int DBusAuth::cookie_id |

ID of cookie to use.

Definition at line 180 of file dbus-auth.c.

## ◆ credentials

|                                         |
|-----------------------------------------|
| DBusCredentials\* DBusAuth::credentials |

Credentials read from socket.

Definition at line 171 of file dbus-auth.c.

Referenced by \_dbus_auth_set_credentials(), and \_dbus_auth_unref().

## ◆ desired_identity

|                                              |
|----------------------------------------------|
| DBusCredentials\* DBusAuth::desired_identity |

Identity client has requested.

Definition at line 176 of file dbus-auth.c.

Referenced by \_dbus_auth_unref().

## ◆ identity

|                               |
|-------------------------------|
| DBusString DBusAuth::identity |

Current identity we're authorizing as.

Definition at line 167 of file dbus-auth.c.

Referenced by \_dbus_auth_unref().

## ◆ incoming

|                               |
|-------------------------------|
| DBusString DBusAuth::incoming |

Incoming data buffer.

Definition at line 160 of file dbus-auth.c.

Referenced by \_dbus_auth_delete_unused_bytes(), \_dbus_auth_do_work(), \_dbus_auth_get_buffer(), \_dbus_auth_get_unused_bytes(), \_dbus_auth_return_buffer(), and \_dbus_auth_unref().

## ◆ keyring

|                                 |
|---------------------------------|
| DBusKeyring\* DBusAuth::keyring |

Keyring for cookie mechanism.

Definition at line 179 of file dbus-auth.c.

Referenced by \_dbus_auth_unref().

## ◆ mech

|                                                 |
|-------------------------------------------------|
| const DBusAuthMechanismHandler\* DBusAuth::mech |

Current auth mechanism.

Definition at line 165 of file dbus-auth.c.

Referenced by \_dbus_auth_decode_data(), \_dbus_auth_encode_data(), \_dbus_auth_needs_decoding(), and \_dbus_auth_needs_encoding().

## ◆ needed_memory

|                                      |
|--------------------------------------|
| unsigned int DBusAuth::needed_memory |

We needed memory to continue since last successful getting something done.

Definition at line 187 of file dbus-auth.c.

Referenced by \_dbus_auth_do_work().

## ◆ outgoing

|                               |
|-------------------------------|
| DBusString DBusAuth::outgoing |

Outgoing data buffer.

Definition at line 161 of file dbus-auth.c.

Referenced by \_dbus_auth_bytes_sent(), \_dbus_auth_do_work(), \_dbus_auth_get_bytes_to_send(), and \_dbus_auth_unref().

## ◆ refcount

|                        |
|------------------------|
| int DBusAuth::refcount |

reference count

Definition at line 157 of file dbus-auth.c.

Referenced by \_dbus_auth_ref(), and \_dbus_auth_unref().

## ◆ side

|                             |
|-----------------------------|
| const char\* DBusAuth::side |

Client or server.

Definition at line 158 of file dbus-auth.c.

Referenced by \_dbus_auth_client_new(), and \_dbus_auth_server_new().

## ◆ state

|                                           |
|-------------------------------------------|
| const DBusAuthStateData\* DBusAuth::state |

Current protocol state.

Definition at line 163 of file dbus-auth.c.

Referenced by \_dbus_auth_client_new(), \_dbus_auth_decode_data(), \_dbus_auth_do_work(), \_dbus_auth_encode_data(), \_dbus_auth_get_guid_from_server(), \_dbus_auth_get_identity(), \_dbus_auth_needs_decoding(), \_dbus_auth_needs_encoding(), and \_dbus_auth_server_new().

## ◆ unix_fd_negotiated

|                                           |
|-------------------------------------------|
| unsigned int DBusAuth::unix_fd_negotiated |

Unix fd was successfully negotiated.

Definition at line 195 of file dbus-auth.c.

Referenced by \_dbus_auth_get_unix_fd_negotiated().

## ◆ unix_fd_possible

|                                         |
|-----------------------------------------|
| unsigned int DBusAuth::unix_fd_possible |

This side could do unix fd passing.

Definition at line 194 of file dbus-auth.c.

Referenced by \_dbus_auth_set_unix_fd_possible().

The documentation for this struct was generated from the following file:

- dbus-auth.c
