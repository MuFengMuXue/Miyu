Authentication

D-Bus secret internal implementation details

DBusAuth object. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="macros" class="groupheader"> Macros</h2></td>
</tr>
<tr id="r_gaef3b2bcbcd611b935955eaf82ce238e2" class="memitem:gaef3b2bcbcd611b935955eaf82ce238e2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_AUTH_IN_END_STATE(auth)   ((auth)-&gt;state-&gt;handler == NULL)</td>
</tr>
<tr class="separator:gaef3b2bcbcd611b935955eaf82ce238e2">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="functions" class="groupheader"> Functions</h2></td>
</tr>
<tr id="r_gaf7669227ac9d745ebfe7a26ec6fc2af2" class="memitem:gaf7669227ac9d745ebfe7a26ec6fc2af2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusAuth * </td>
<td class="memItemRight" data-valign="bottom">_dbus_auth_server_new (const DBusString *guid)</td>
</tr>
<tr class="memdesc:gaf7669227ac9d745ebfe7a26ec6fc2af2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new auth conversation object for the server side.<br />
</td>
</tr>
<tr class="separator:gaf7669227ac9d745ebfe7a26ec6fc2af2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf50cc07d13b44317ef9b2c46e037d92b" class="memitem:gaf50cc07d13b44317ef9b2c46e037d92b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusAuth * </td>
<td class="memItemRight" data-valign="bottom">_dbus_auth_client_new (void)</td>
</tr>
<tr class="memdesc:gaf50cc07d13b44317ef9b2c46e037d92b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new auth conversation object for the client side.<br />
</td>
</tr>
<tr class="separator:gaf50cc07d13b44317ef9b2c46e037d92b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga372383001327e6cf79ca7df086ddfc3c" class="memitem:ga372383001327e6cf79ca7df086ddfc3c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusAuth * </td>
<td class="memItemRight" data-valign="bottom">_dbus_auth_ref (DBusAuth *auth)</td>
</tr>
<tr class="memdesc:ga372383001327e6cf79ca7df086ddfc3c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Increments the refcount of an auth object.<br />
</td>
</tr>
<tr class="separator:ga372383001327e6cf79ca7df086ddfc3c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7fb648be9d6d451917195a0e43eeece0" class="memitem:ga7fb648be9d6d451917195a0e43eeece0">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_auth_unref (DBusAuth *auth)</td>
</tr>
<tr class="memdesc:ga7fb648be9d6d451917195a0e43eeece0">
<td class="mdescLeft"> </td>
<td class="mdescRight">Decrements the refcount of an auth object.<br />
</td>
</tr>
<tr class="separator:ga7fb648be9d6d451917195a0e43eeece0">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9454e2c512b4e2ea54d47cff6acaa4db" class="memitem:ga9454e2c512b4e2ea54d47cff6acaa4db">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_auth_set_mechanisms (DBusAuth *auth, const char **mechanisms)</td>
</tr>
<tr class="memdesc:ga9454e2c512b4e2ea54d47cff6acaa4db">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets an array of authentication mechanism names that we are willing to use.<br />
</td>
</tr>
<tr class="separator:ga9454e2c512b4e2ea54d47cff6acaa4db">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga097c71f7f20b749275c6b31cd98623f5" class="memitem:ga097c71f7f20b749275c6b31cd98623f5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusAuthState </td>
<td class="memItemRight" data-valign="bottom">_dbus_auth_do_work (DBusAuth *auth)</td>
</tr>
<tr class="memdesc:ga097c71f7f20b749275c6b31cd98623f5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Analyzes buffered input and moves the auth conversation forward, returning the new state of the auth conversation.<br />
</td>
</tr>
<tr class="separator:ga097c71f7f20b749275c6b31cd98623f5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7befc68c815fe31d7fa556b699ef67de" class="memitem:ga7befc68c815fe31d7fa556b699ef67de">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_auth_get_bytes_to_send (DBusAuth *auth, const DBusString **str)</td>
</tr>
<tr class="memdesc:ga7befc68c815fe31d7fa556b699ef67de">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets bytes that need to be sent to the peer we're conversing with.<br />
</td>
</tr>
<tr class="separator:ga7befc68c815fe31d7fa556b699ef67de">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaed9f7f1d3289a0ae2fea2204729ac01f" class="memitem:gaed9f7f1d3289a0ae2fea2204729ac01f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_auth_bytes_sent (DBusAuth *auth, int bytes_sent)</td>
</tr>
<tr class="memdesc:gaed9f7f1d3289a0ae2fea2204729ac01f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Notifies the auth conversation object that the given number of bytes of the outgoing buffer have been written out.<br />
</td>
</tr>
<tr class="separator:gaed9f7f1d3289a0ae2fea2204729ac01f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac0fc38d8d0d139e4d52787881a324c05" class="memitem:gac0fc38d8d0d139e4d52787881a324c05">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_auth_get_buffer (DBusAuth *auth, DBusString **buffer)</td>
</tr>
<tr class="memdesc:gac0fc38d8d0d139e4d52787881a324c05">
<td class="mdescLeft"> </td>
<td class="mdescRight">Get a buffer to be used for reading bytes from the peer we're conversing with.<br />
</td>
</tr>
<tr class="separator:gac0fc38d8d0d139e4d52787881a324c05">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga842c246877d16cb9a75cc9828a5433c2" class="memitem:ga842c246877d16cb9a75cc9828a5433c2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_auth_return_buffer (DBusAuth *auth, DBusString *buffer)</td>
</tr>
<tr class="memdesc:ga842c246877d16cb9a75cc9828a5433c2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns a buffer with new data read into it.<br />
</td>
</tr>
<tr class="separator:ga842c246877d16cb9a75cc9828a5433c2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf9e2ab67f2ddd26eeb7deeb8b0af7817" class="memitem:gaf9e2ab67f2ddd26eeb7deeb8b0af7817">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_auth_get_unused_bytes (DBusAuth *auth, const DBusString **str)</td>
</tr>
<tr class="memdesc:gaf9e2ab67f2ddd26eeb7deeb8b0af7817">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns leftover bytes that were not used as part of the auth conversation.<br />
</td>
</tr>
<tr class="separator:gaf9e2ab67f2ddd26eeb7deeb8b0af7817">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabbe8cf9e5958357c49a190ca259aa9b3" class="memitem:gabbe8cf9e5958357c49a190ca259aa9b3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_auth_delete_unused_bytes (DBusAuth *auth)</td>
</tr>
<tr class="memdesc:gabbe8cf9e5958357c49a190ca259aa9b3">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets rid of unused bytes returned by _dbus_auth_get_unused_bytes() after we've gotten them and successfully moved them elsewhere.<br />
</td>
</tr>
<tr class="separator:gabbe8cf9e5958357c49a190ca259aa9b3">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga22ddfb5e12cba3d047dc1d1302c23490" class="memitem:ga22ddfb5e12cba3d047dc1d1302c23490">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_auth_needs_encoding (DBusAuth *auth)</td>
</tr>
<tr class="memdesc:ga22ddfb5e12cba3d047dc1d1302c23490">
<td class="mdescLeft"> </td>
<td class="mdescRight">Called post-authentication, indicates whether we need to encode the message stream with _dbus_auth_encode_data() prior to sending it to the peer.<br />
</td>
</tr>
<tr class="separator:ga22ddfb5e12cba3d047dc1d1302c23490">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0d59bcf62c098cdfb95f610cdfd12690" class="memitem:ga0d59bcf62c098cdfb95f610cdfd12690">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_auth_encode_data (DBusAuth *auth, const DBusString *plaintext, DBusString *encoded)</td>
</tr>
<tr class="memdesc:ga0d59bcf62c098cdfb95f610cdfd12690">
<td class="mdescLeft"> </td>
<td class="mdescRight">Called post-authentication, encodes a block of bytes for sending to the peer.<br />
</td>
</tr>
<tr class="separator:ga0d59bcf62c098cdfb95f610cdfd12690">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac6e9dc07335a6291842374d834e95ad2" class="memitem:gac6e9dc07335a6291842374d834e95ad2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_auth_needs_decoding (DBusAuth *auth)</td>
</tr>
<tr class="memdesc:gac6e9dc07335a6291842374d834e95ad2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Called post-authentication, indicates whether we need to decode the message stream with _dbus_auth_decode_data() after receiving it from the peer.<br />
</td>
</tr>
<tr class="separator:gac6e9dc07335a6291842374d834e95ad2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7eb40f71c0ede79f954bcb2c001c8502" class="memitem:ga7eb40f71c0ede79f954bcb2c001c8502">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_auth_decode_data (DBusAuth *auth, const DBusString *encoded, DBusString *plaintext)</td>
</tr>
<tr class="memdesc:ga7eb40f71c0ede79f954bcb2c001c8502">
<td class="mdescLeft"> </td>
<td class="mdescRight">Called post-authentication, decodes a block of bytes received from the peer.<br />
</td>
</tr>
<tr class="separator:ga7eb40f71c0ede79f954bcb2c001c8502">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2bb917d44b44b1a2813f60dec03731cd" class="memitem:ga2bb917d44b44b1a2813f60dec03731cd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_auth_set_credentials (DBusAuth *auth, DBusCredentials *credentials)</td>
</tr>
<tr class="memdesc:ga2bb917d44b44b1a2813f60dec03731cd">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets credentials received via reliable means from the operating system.<br />
</td>
</tr>
<tr class="separator:ga2bb917d44b44b1a2813f60dec03731cd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3d6dca89784398c367eb16d70a0d4017" class="memitem:ga3d6dca89784398c367eb16d70a0d4017">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusCredentials * </td>
<td class="memItemRight" data-valign="bottom">_dbus_auth_get_identity (DBusAuth *auth)</td>
</tr>
<tr class="memdesc:ga3d6dca89784398c367eb16d70a0d4017">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the identity we authorized the client as.<br />
</td>
</tr>
<tr class="separator:ga3d6dca89784398c367eb16d70a0d4017">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabec34ddffeedb9c50d3373c1ed73cc0f" class="memitem:gabec34ddffeedb9c50d3373c1ed73cc0f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">_dbus_auth_get_guid_from_server (DBusAuth *auth)</td>
</tr>
<tr class="memdesc:gabec34ddffeedb9c50d3373c1ed73cc0f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the GUID from the server if we've authenticated; gets NULL otherwise.<br />
</td>
</tr>
<tr class="separator:gabec34ddffeedb9c50d3373c1ed73cc0f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad6d64040b2cf1c91f808a1f31f7ff2f0" class="memitem:gad6d64040b2cf1c91f808a1f31f7ff2f0">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_auth_set_context (DBusAuth *auth, const DBusString *context)</td>
</tr>
<tr class="memdesc:gad6d64040b2cf1c91f808a1f31f7ff2f0">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the "authentication context" which scopes cookies with the DBUS_COOKIE_SHA1 auth mechanism for example.<br />
</td>
</tr>
<tr class="separator:gad6d64040b2cf1c91f808a1f31f7ff2f0">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga831cbd78b6c7f382840e4094f02efdb5" class="memitem:ga831cbd78b6c7f382840e4094f02efdb5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_auth_set_unix_fd_possible (DBusAuth *auth, dbus_bool_t b)</td>
</tr>
<tr class="memdesc:ga831cbd78b6c7f382840e4094f02efdb5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets whether unix fd passing is potentially on the transport and hence shall be negotiated.<br />
</td>
</tr>
<tr class="separator:ga831cbd78b6c7f382840e4094f02efdb5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2d9119a45123f6b513a60391fb617d5c" class="memitem:ga2d9119a45123f6b513a60391fb617d5c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_auth_get_unix_fd_negotiated (DBusAuth *auth)</td>
</tr>
<tr class="memdesc:ga2d9119a45123f6b513a60391fb617d5c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Queries whether unix fd passing was successfully negotiated.<br />
</td>
</tr>
<tr class="separator:ga2d9119a45123f6b513a60391fb617d5c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3d18faa864d838d6664ecfe58e4c0e98" class="memitem:ga3d18faa864d838d6664ecfe58e4c0e98">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_auth_is_supported_mechanism (DBusString *name)</td>
</tr>
<tr class="memdesc:ga3d18faa864d838d6664ecfe58e4c0e98">
<td class="mdescLeft"> </td>
<td class="mdescRight">Queries whether the given auth mechanism is supported.<br />
</td>
</tr>
<tr class="separator:ga3d18faa864d838d6664ecfe58e4c0e98">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1e90a2ecc6e1731ad9282bae2634b0e7" class="memitem:ga1e90a2ecc6e1731ad9282bae2634b0e7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_auth_dump_supported_mechanisms (DBusString *buffer)</td>
</tr>
<tr class="memdesc:ga1e90a2ecc6e1731ad9282bae2634b0e7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Return a human-readable string containing all supported auth mechanisms.<br />
</td>
</tr>
<tr class="separator:ga1e90a2ecc6e1731ad9282bae2634b0e7">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

DBusAuth object.

DBusAuth manages the authentication negotiation when a connection is first established, and also manages any encryption used over a connection.

## Macro Definition Documentation

## ◆ DBUS_AUTH_IN_END_STATE

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| \#define DBUS_AUTH_IN_END_STATE | ( |   | auth | ) |    ((auth)-\>state-\>handler == NULL) |

Parameters  
|      |                              |
|------|------------------------------|
| auth | the auth conversation object |

<!-- -->

Returns  
TRUE if we're in a final state

Definition at line 2538 of file dbus-auth.c.

## Function Documentation

## ◆ \_dbus_auth_bytes_sent()

|                             |     |              |               |
|-----------------------------|-----|--------------|---------------|
| void \_dbus_auth_bytes_sent | (   | DBusAuth \*  | *auth*,       |
|                             |     | int          | *bytes_sent*  |
|                             | )   |              |               |

Notifies the auth conversation object that the given number of bytes of the outgoing buffer have been written out.

Parameters  
|            |                             |
|------------|-----------------------------|
| auth       | the auth conversation       |
| bytes_sent | number of bytes written out |

Definition at line 2617 of file dbus-auth.c.

References \_dbus_string_delete(), \_dbus_string_get_const_data(), DBUS_AUTH_NAME, and outgoing.

## ◆ \_dbus_auth_client_new()

|                                    |     |       |     |     |     |
|------------------------------------|-----|-------|-----|-----|-----|
| DBusAuth \* \_dbus_auth_client_new | (   | void  |     | )   |     |

Creates a new auth conversation object for the client side.

See http://dbus.freedesktop.org/doc/dbus-specification.html#auth-protocol for full details on what this object does.

Returns  
the new object or NULL if no memory

Definition at line 2410 of file dbus-auth.c.

References \_dbus_auth_unref(), \_dbus_string_free(), \_dbus_string_init(), DBUS_AUTH_CLIENT, NULL, side, and state.

Referenced by \_dbus_transport_init_base().

## ◆ \_dbus_auth_decode_data()

|                                     |     |                      |              |
|-------------------------------------|-----|----------------------|--------------|
| dbus_bool_t \_dbus_auth_decode_data | (   | DBusAuth \*          | *auth*,      |
|                                     |     | const DBusString \*  | *encoded*,   |
|                                     |     | DBusString \*        | *plaintext*  |
|                                     | )   |                      |              |

Called post-authentication, decodes a block of bytes received from the peer.

If no encoding was negotiated, just copies the bytes (you can avoid this by checking \_dbus_auth_needs_decoding()).

Parameters  
|           |                                                   |
|-----------|---------------------------------------------------|
| auth      | the auth conversation                             |
| encoded   | the encoded data                                  |
| plaintext | initialized string where decoded data is appended |

<!-- -->

Returns  
TRUE if we had enough memory and successfully decoded

Definition at line 2798 of file dbus-auth.c.

References \_dbus_assert, \_dbus_auth_needs_decoding(), \_dbus_string_copy(), \_dbus_string_get_length(), DBusAuthMechanismHandler::client_decode_func, DBUS_AUTH_IS_CLIENT, FALSE, mech, DBusAuthMechanismHandler::server_decode_func, and state.

## ◆ \_dbus_auth_delete_unused_bytes()

|                                      |     |              |        |     |     |
|--------------------------------------|-----|--------------|--------|-----|-----|
| void \_dbus_auth_delete_unused_bytes | (   | DBusAuth \*  | *auth* | )   |     |

Gets rid of unused bytes returned by \_dbus_auth_get_unused_bytes() after we've gotten them and successfully moved them elsewhere.

Parameters  
|      |                       |
|------|-----------------------|
| auth | the auth conversation |

Definition at line 2691 of file dbus-auth.c.

References \_dbus_string_set_length(), DBUS_AUTH_IN_END_STATE, and incoming.

## ◆ \_dbus_auth_do_work()

|                                   |     |              |        |     |     |
|-----------------------------------|-----|--------------|--------|-----|-----|
| DBusAuthState \_dbus_auth_do_work | (   | DBusAuth \*  | *auth* | )   |     |

Analyzes buffered input and moves the auth conversation forward, returning the new state of the auth conversation.

Parameters  
|      |                       |
|------|-----------------------|
| auth | the auth conversation |

<!-- -->

Returns  
the new state

Definition at line 2548 of file dbus-auth.c.

References \_dbus_string_get_length(), DBUS_AUTH_IN_END_STATE, DBUS_AUTH_NAME, FALSE, incoming, needed_memory, outgoing, and state.

Referenced by \_dbus_transport_get_dispatch_status(), and \_dbus_transport_try_to_authenticate().

## ◆ \_dbus_auth_dump_supported_mechanisms()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_auth_dump_supported_mechanisms | ( | DBusString \*  | *buffer* | ) |  |

Return a human-readable string containing all supported auth mechanisms.

Parameters  
|        |                                       |
|--------|---------------------------------------|
| string | to hold the supported auth mechanisms |

<!-- -->

Returns  
FALSE on oom

Definition at line 2944 of file dbus-auth.c.

References \_dbus_assert, \_dbus_string_append(), FALSE, DBusAuthMechanismHandler::mechanism, NULL, and TRUE.

## ◆ \_dbus_auth_encode_data()

|                                     |     |                      |              |
|-------------------------------------|-----|----------------------|--------------|
| dbus_bool_t \_dbus_auth_encode_data | (   | DBusAuth \*          | *auth*,      |
|                                     |     | const DBusString \*  | *plaintext*, |
|                                     |     | DBusString \*        | *encoded*    |
|                                     | )   |                      |              |

Called post-authentication, encodes a block of bytes for sending to the peer.

If no encoding was negotiated, just copies the bytes (you can avoid this by checking \_dbus_auth_needs_encoding()).

Parameters  
|           |                                                      |
|-----------|------------------------------------------------------|
| auth      | the auth conversation                                |
| plaintext | the plain text data                                  |
| encoded   | initialized string to where encoded data is appended |

<!-- -->

Returns  
TRUE if we had enough memory and successfully encoded

Definition at line 2735 of file dbus-auth.c.

References \_dbus_assert, \_dbus_auth_needs_encoding(), \_dbus_string_copy(), \_dbus_string_get_length(), DBusAuthMechanismHandler::client_encode_func, DBUS_AUTH_IS_CLIENT, FALSE, mech, DBusAuthMechanismHandler::server_encode_func, and state.

## ◆ \_dbus_auth_get_buffer()

|                             |     |                  |           |
|-----------------------------|-----|------------------|-----------|
| void \_dbus_auth_get_buffer | (   | DBusAuth \*      | *auth*,   |
|                             |     | DBusString \*\*  | *buffer*  |
|                             | )   |                  |           |

Get a buffer to be used for reading bytes from the peer we're conversing with.

Bytes should be appended to this buffer.

Parameters  
|        |                                               |
|--------|-----------------------------------------------|
| auth   | the auth conversation                         |
| buffer | return location for buffer to append bytes to |

Definition at line 2637 of file dbus-auth.c.

References \_dbus_assert, buffer_outstanding, incoming, NULL, and TRUE.

## ◆ \_dbus_auth_get_bytes_to_send()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_auth_get_bytes_to_send | ( | DBusAuth \*  | *auth*, |
|  |  | const DBusString \*\*  | *str*  |
|  | ) |  |  |

Gets bytes that need to be sent to the peer we're conversing with.

After writing some bytes, \_dbus_auth_bytes_sent() must be called to notify the auth object that they were written.

Parameters  
|      |                                                 |
|------|-------------------------------------------------|
| auth | the auth conversation                           |
| str  | return location for a ref to the buffer to send |

<!-- -->

Returns  
FALSE if nothing to send

Definition at line 2592 of file dbus-auth.c.

References \_dbus_assert, \_dbus_string_get_length(), FALSE, NULL, outgoing, and TRUE.

## ◆ \_dbus_auth_get_guid_from_server()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| const char \* \_dbus_auth_get_guid_from_server | ( | DBusAuth \*  | *auth* | ) |  |

Gets the GUID from the server if we've authenticated; gets NULL otherwise.

Parameters  
|      |                 |
|------|-----------------|
| auth | the auth object |

<!-- -->

Returns  
the GUID in ASCII hex format

Definition at line 2872 of file dbus-auth.c.

References \_dbus_assert, \_dbus_string_get_const_data(), DBUS_AUTH_CLIENT, DBUS_AUTH_IS_CLIENT, NULL, and state.

Referenced by \_dbus_transport_get_server_id(), and \_dbus_transport_try_to_authenticate().

## ◆ \_dbus_auth_get_identity()

|                                             |     |              |        |     |     |
|---------------------------------------------|-----|--------------|--------|-----|-----|
| DBusCredentials \* \_dbus_auth_get_identity | (   | DBusAuth \*  | *auth* | )   |     |

Gets the identity we authorized the client as.

Apps may have different policies as to what identities they allow.

Returned credentials are not a copy and should not be modified

Parameters  
|      |                       |
|------|-----------------------|
| auth | the auth conversation |

<!-- -->

Returns  
the credentials we've authorized BY REFERENCE do not modify

Definition at line 2848 of file dbus-auth.c.

References \_dbus_assert, \_dbus_credentials_are_empty(), authorized_identity, and state.

Referenced by \_dbus_transport_get_adt_audit_session_data(), \_dbus_transport_get_credentials(), \_dbus_transport_get_is_anonymous(), \_dbus_transport_get_unix_process_id(), \_dbus_transport_get_unix_user(), \_dbus_transport_get_windows_user(), and \_dbus_transport_try_to_authenticate().

## ◆ \_dbus_auth_get_unix_fd_negotiated()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_auth_get_unix_fd_negotiated | ( | DBusAuth \*  | *auth* | ) |  |

Queries whether unix fd passing was successfully negotiated.

Parameters  
|      |                     |
|------|---------------------|
| auth | the auth conversion |

<!-- -->

Returns  
TRUE when unix fd passing was negotiated.

Definition at line 2918 of file dbus-auth.c.

References unix_fd_negotiated.

## ◆ \_dbus_auth_get_unused_bytes()

|                                   |     |                        |         |
|-----------------------------------|-----|------------------------|---------|
| void \_dbus_auth_get_unused_bytes | (   | DBusAuth \*            | *auth*, |
|                                   |     | const DBusString \*\*  | *str*   |
|                                   | )   |                        |         |

Returns leftover bytes that were not used as part of the auth conversation.

These bytes will be part of the message stream instead. This function may not be called until authentication has succeeded.

Parameters  
|      |                                                       |
|------|-------------------------------------------------------|
| auth | the auth conversation                                 |
| str  | return location for pointer to string of unused bytes |

Definition at line 2674 of file dbus-auth.c.

References DBUS_AUTH_IN_END_STATE, and incoming.

## ◆ \_dbus_auth_is_supported_mechanism()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_auth_is_supported_mechanism | ( | DBusString \*  | *name* | ) |  |

Queries whether the given auth mechanism is supported.

Parameters  
|      |                                 |
|------|---------------------------------|
| auth | the auth mechanism to query for |

<!-- -->

Returns  
TRUE when auth mechanism is supported

Definition at line 2930 of file dbus-auth.c.

References \_dbus_assert, and NULL.

## ◆ \_dbus_auth_needs_decoding()

|                                        |     |              |        |     |     |
|----------------------------------------|-----|--------------|--------|-----|-----|
| dbus_bool_t \_dbus_auth_needs_decoding | (   | DBusAuth \*  | *auth* | )   |     |

Called post-authentication, indicates whether we need to decode the message stream with \_dbus_auth_decode_data() after receiving it from the peer.

Parameters  
|      |                       |
|------|-----------------------|
| auth | the auth conversation |

<!-- -->

Returns  
TRUE if we need to encode the stream

Definition at line 2767 of file dbus-auth.c.

References DBusAuthMechanismHandler::client_decode_func, DBUS_AUTH_IS_CLIENT, FALSE, mech, NULL, DBusAuthMechanismHandler::server_decode_func, and state.

Referenced by \_dbus_auth_decode_data().

## ◆ \_dbus_auth_needs_encoding()

|                                        |     |              |        |     |     |
|----------------------------------------|-----|--------------|--------|-----|-----|
| dbus_bool_t \_dbus_auth_needs_encoding | (   | DBusAuth \*  | *auth* | )   |     |

Called post-authentication, indicates whether we need to encode the message stream with \_dbus_auth_encode_data() prior to sending it to the peer.

Parameters  
|      |                       |
|------|-----------------------|
| auth | the auth conversation |

<!-- -->

Returns  
TRUE if we need to encode the stream

Definition at line 2708 of file dbus-auth.c.

References DBusAuthMechanismHandler::client_encode_func, DBUS_AUTH_IS_CLIENT, FALSE, mech, NULL, DBusAuthMechanismHandler::server_encode_func, and state.

Referenced by \_dbus_auth_encode_data().

## ◆ \_dbus_auth_ref()

|                             |     |              |        |     |     |
|-----------------------------|-----|--------------|--------|-----|-----|
| DBusAuth \* \_dbus_auth_ref | (   | DBusAuth \*  | *auth* | )   |     |

Increments the refcount of an auth object.

Parameters  
|      |                       |
|------|-----------------------|
| auth | the auth conversation |

<!-- -->

Returns  
the auth conversation

Definition at line 2448 of file dbus-auth.c.

References \_dbus_assert, NULL, and refcount.

## ◆ \_dbus_auth_return_buffer()

|                                |     |                |           |
|--------------------------------|-----|----------------|-----------|
| void \_dbus_auth_return_buffer | (   | DBusAuth \*    | *auth*,   |
|                                |     | DBusString \*  | *buffer*  |
|                                | )   |                |           |

Returns a buffer with new data read into it.

Parameters  
|        |                           |
|--------|---------------------------|
| auth   | the auth conversation     |
| buffer | the buffer being returned |

Definition at line 2655 of file dbus-auth.c.

References \_dbus_assert, buffer_outstanding, FALSE, and incoming.

## ◆ \_dbus_auth_server_new()

|                                    |     |                      |        |     |     |
|------------------------------------|-----|----------------------|--------|-----|-----|
| DBusAuth \* \_dbus_auth_server_new | (   | const DBusString \*  | *guid* | )   |     |

Creates a new auth conversation object for the server side.

See http://dbus.freedesktop.org/doc/dbus-specification.html#auth-protocol for full details on what this object does.

Returns  
the new object or NULL if no memory

Definition at line 2364 of file dbus-auth.c.

References \_dbus_string_copy(), \_dbus_string_free(), \_dbus_string_init(), DBUS_AUTH_SERVER, DBusAuthServer::failures, DBusAuthServer::guid, DBusAuthServer::max_failures, NULL, side, and state.

Referenced by \_dbus_transport_init_base().

## ◆ \_dbus_auth_set_context()

|                                     |     |                      |            |
|-------------------------------------|-----|----------------------|------------|
| dbus_bool_t \_dbus_auth_set_context | (   | DBusAuth \*          | *auth*,    |
|                                     |     | const DBusString \*  | *context*  |
|                                     | )   |                      |            |

Sets the "authentication context" which scopes cookies with the DBUS_COOKIE_SHA1 auth mechanism for example.

Parameters  
|         |                       |
|---------|-----------------------|
| auth    | the auth conversation |
| context | the context           |

<!-- -->

Returns  
FALSE if no memory

Definition at line 2891 of file dbus-auth.c.

References \_dbus_string_get_length(), \_dbus_string_replace_len(), and context.

## ◆ \_dbus_auth_set_credentials()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_auth_set_credentials | ( | DBusAuth \*  | *auth*, |
|  |  | DBusCredentials \*  | *credentials*  |
|  | ) |  |  |

Sets credentials received via reliable means from the operating system.

Parameters  
|             |                          |
|-------------|--------------------------|
| auth        | the auth conversation    |
| credentials | the credentials received |

<!-- -->

Returns  
FALSE on OOM

Definition at line 2830 of file dbus-auth.c.

References \_dbus_credentials_add_credentials(), \_dbus_credentials_clear(), and credentials.

## ◆ \_dbus_auth_set_mechanisms()

|                                        |     |                  |               |
|----------------------------------------|-----|------------------|---------------|
| dbus_bool_t \_dbus_auth_set_mechanisms | (   | DBusAuth \*      | *auth*,       |
|                                        |     | const char \*\*  | *mechanisms*  |
|                                        | )   |                  |               |

Sets an array of authentication mechanism names that we are willing to use.

Parameters  
|            |                                          |
|------------|------------------------------------------|
| auth       | the auth conversation                    |
| mechanisms | NULL-terminated array of mechanism names |

<!-- -->

Returns  
FALSE if no memory

Definition at line 2513 of file dbus-auth.c.

References \_dbus_dup_string_array(), allowed_mechs, dbus_free_string_array(), FALSE, NULL, and TRUE.

Referenced by \_dbus_transport_set_auth_mechanisms().

## ◆ \_dbus_auth_set_unix_fd_possible()

|                                       |     |              |         |
|---------------------------------------|-----|--------------|---------|
| void \_dbus_auth_set_unix_fd_possible | (   | DBusAuth \*  | *auth*, |
|                                       |     | dbus_bool_t  | *b*     |
|                                       | )   |              |         |

Sets whether unix fd passing is potentially on the transport and hence shall be negotiated.

Parameters  
|      |                                                                |
|------|----------------------------------------------------------------|
| auth | the auth conversation                                          |
| b    | TRUE when unix fd passing shall be negotiated, otherwise FALSE |

Definition at line 2906 of file dbus-auth.c.

References unix_fd_possible.

Referenced by \_dbus_transport_new_for_socket().

## ◆ \_dbus_auth_unref()

|                        |     |              |        |     |     |
|------------------------|-----|--------------|--------|-----|-----|
| void \_dbus_auth_unref | (   | DBusAuth \*  | *auth* | )   |     |

Decrements the refcount of an auth object.

Parameters  
|      |                       |
|------|-----------------------|
| auth | the auth conversation |

Definition at line 2463 of file dbus-auth.c.

References \_dbus_assert, \_dbus_credentials_unref(), \_dbus_keyring_unref(), \_dbus_list_clear(), \_dbus_string_free(), allowed_mechs, authorized_identity, challenge, context, credentials, DBUS_AUTH_CLIENT, DBUS_AUTH_IS_CLIENT, DBUS_AUTH_IS_SERVER, DBUS_AUTH_SERVER, dbus_free(), dbus_free_string_array(), desired_identity, identity, incoming, keyring, NULL, outgoing, and refcount.

Referenced by \_dbus_auth_client_new(), \_dbus_transport_finalize_base(), and \_dbus_transport_init_base().
