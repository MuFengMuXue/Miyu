DBusAuthMechanismHandler Struct Reference

D-Bus secret internal implementation details » Authentication implementation details

Virtual table representing a particular auth mechanism. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a353c8effcb16bdc37c2f225b8dad9415" class="memitem:a353c8effcb16bdc37c2f225b8dad9415">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">mechanism</td>
</tr>
<tr class="memdesc:a353c8effcb16bdc37c2f225b8dad9415">
<td class="mdescLeft"> </td>
<td class="mdescRight">Name of the mechanism.<br />
</td>
</tr>
<tr class="separator:a353c8effcb16bdc37c2f225b8dad9415">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a6fb1fd485bf4f99f4d269cebe4625a8a" class="memitem:a6fb1fd485bf4f99f4d269cebe4625a8a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusAuthDataFunction </td>
<td class="memItemRight" data-valign="bottom">server_data_func</td>
</tr>
<tr class="memdesc:a6fb1fd485bf4f99f4d269cebe4625a8a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function on server side for DATA.<br />
</td>
</tr>
<tr class="separator:a6fb1fd485bf4f99f4d269cebe4625a8a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a7aedf6828bf1f232edb2532616b9a1da" class="memitem:a7aedf6828bf1f232edb2532616b9a1da">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusAuthEncodeFunction </td>
<td class="memItemRight" data-valign="bottom">server_encode_func</td>
</tr>
<tr class="memdesc:a7aedf6828bf1f232edb2532616b9a1da">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function on server side to encode.<br />
</td>
</tr>
<tr class="separator:a7aedf6828bf1f232edb2532616b9a1da">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ac6785768ff465be230d2f127d8099953" class="memitem:ac6785768ff465be230d2f127d8099953">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusAuthDecodeFunction </td>
<td class="memItemRight" data-valign="bottom">server_decode_func</td>
</tr>
<tr class="memdesc:ac6785768ff465be230d2f127d8099953">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function on server side to decode.<br />
</td>
</tr>
<tr class="separator:ac6785768ff465be230d2f127d8099953">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aa6e551c05863b85ee8c138a976497e8e" class="memitem:aa6e551c05863b85ee8c138a976497e8e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusAuthShutdownFunction </td>
<td class="memItemRight" data-valign="bottom">server_shutdown_func</td>
</tr>
<tr class="memdesc:aa6e551c05863b85ee8c138a976497e8e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function on server side to shut down.<br />
</td>
</tr>
<tr class="separator:aa6e551c05863b85ee8c138a976497e8e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a7702073e4e001efcd921b413519646a1" class="memitem:a7702073e4e001efcd921b413519646a1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusInitialResponseFunction </td>
<td class="memItemRight" data-valign="bottom">client_initial_response_func</td>
</tr>
<tr class="memdesc:a7702073e4e001efcd921b413519646a1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function on client side to handle initial response.<br />
</td>
</tr>
<tr class="separator:a7702073e4e001efcd921b413519646a1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a765bf360f3af4a7d418dd4f029cc4c26" class="memitem:a765bf360f3af4a7d418dd4f029cc4c26">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusAuthDataFunction </td>
<td class="memItemRight" data-valign="bottom">client_data_func</td>
</tr>
<tr class="memdesc:a765bf360f3af4a7d418dd4f029cc4c26">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function on client side for DATA.<br />
</td>
</tr>
<tr class="separator:a765bf360f3af4a7d418dd4f029cc4c26">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ae72e69ef3b4513cbc5bdecae43dd380d" class="memitem:ae72e69ef3b4513cbc5bdecae43dd380d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusAuthEncodeFunction </td>
<td class="memItemRight" data-valign="bottom">client_encode_func</td>
</tr>
<tr class="memdesc:ae72e69ef3b4513cbc5bdecae43dd380d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function on client side for encode.<br />
</td>
</tr>
<tr class="separator:ae72e69ef3b4513cbc5bdecae43dd380d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ab1d5c9a8cd146bb9f71f4237be1ca415" class="memitem:ab1d5c9a8cd146bb9f71f4237be1ca415">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusAuthDecodeFunction </td>
<td class="memItemRight" data-valign="bottom">client_decode_func</td>
</tr>
<tr class="memdesc:ab1d5c9a8cd146bb9f71f4237be1ca415">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function on client side for decode.<br />
</td>
</tr>
<tr class="separator:ab1d5c9a8cd146bb9f71f4237be1ca415">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aca0a9e37793ca20ed175b3c008c3494f" class="memitem:aca0a9e37793ca20ed175b3c008c3494f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusAuthShutdownFunction </td>
<td class="memItemRight" data-valign="bottom">client_shutdown_func</td>
</tr>
<tr class="memdesc:aca0a9e37793ca20ed175b3c008c3494f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function on client side for shutdown.<br />
</td>
</tr>
<tr class="separator:aca0a9e37793ca20ed175b3c008c3494f">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Virtual table representing a particular auth mechanism.

Definition at line 104 of file dbus-auth.c.

## Field Documentation

## ◆ client_data_func

|                                                                 |
|-----------------------------------------------------------------|
| DBusAuthDataFunction DBusAuthMechanismHandler::client_data_func |

Function on client side for DATA.

Definition at line 112 of file dbus-auth.c.

## ◆ client_decode_func

|                                                                     |
|---------------------------------------------------------------------|
| DBusAuthDecodeFunction DBusAuthMechanismHandler::client_decode_func |

Function on client side for decode.

Definition at line 114 of file dbus-auth.c.

Referenced by \_dbus_auth_decode_data(), and \_dbus_auth_needs_decoding().

## ◆ client_encode_func

|                                                                     |
|---------------------------------------------------------------------|
| DBusAuthEncodeFunction DBusAuthMechanismHandler::client_encode_func |

Function on client side for encode.

Definition at line 113 of file dbus-auth.c.

Referenced by \_dbus_auth_encode_data(), and \_dbus_auth_needs_encoding().

## ◆ client_initial_response_func

|  |
|----|
| DBusInitialResponseFunction DBusAuthMechanismHandler::client_initial_response_func |

Function on client side to handle initial response.

Definition at line 111 of file dbus-auth.c.

## ◆ client_shutdown_func

|                                                                         |
|-------------------------------------------------------------------------|
| DBusAuthShutdownFunction DBusAuthMechanismHandler::client_shutdown_func |

Function on client side for shutdown.

Definition at line 115 of file dbus-auth.c.

## ◆ mechanism

|                                                  |
|--------------------------------------------------|
| const char\* DBusAuthMechanismHandler::mechanism |

Name of the mechanism.

Definition at line 106 of file dbus-auth.c.

Referenced by \_dbus_auth_dump_supported_mechanisms().

## ◆ server_data_func

|                                                                 |
|-----------------------------------------------------------------|
| DBusAuthDataFunction DBusAuthMechanismHandler::server_data_func |

Function on server side for DATA.

Definition at line 107 of file dbus-auth.c.

## ◆ server_decode_func

|                                                                     |
|---------------------------------------------------------------------|
| DBusAuthDecodeFunction DBusAuthMechanismHandler::server_decode_func |

Function on server side to decode.

Definition at line 109 of file dbus-auth.c.

Referenced by \_dbus_auth_decode_data(), and \_dbus_auth_needs_decoding().

## ◆ server_encode_func

|                                                                     |
|---------------------------------------------------------------------|
| DBusAuthEncodeFunction DBusAuthMechanismHandler::server_encode_func |

Function on server side to encode.

Definition at line 108 of file dbus-auth.c.

Referenced by \_dbus_auth_encode_data(), and \_dbus_auth_needs_encoding().

## ◆ server_shutdown_func

|                                                                         |
|-------------------------------------------------------------------------|
| DBusAuthShutdownFunction DBusAuthMechanismHandler::server_shutdown_func |

Function on server side to shut down.

Definition at line 110 of file dbus-auth.c.

The documentation for this struct was generated from the following file:

- dbus-auth.c
