Authentication implementation details

D-Bus secret internal implementation details

DBusAuth implementation details. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-structures" class="groupheader"> Data Structures</h2></td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusAuthMechanismHandler</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Virtual table representing a particular auth mechanism. More...<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusAuthStateData</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Information about a auth state. More...<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusAuth</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Internal members of DBusAuth. More...<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusAuthClient</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">"Subclass" of DBusAuth for client side More...<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusAuthServer</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">"Subclass" of DBusAuth for server side. More...<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusAuthCommandName</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Mapping from command name to enum. More...<br />
</td>
</tr>
<tr class="separator:">
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
<td colspan="2"><h2 id="macros" class="groupheader"> Macros</h2></td>
</tr>
<tr id="r_ga4211a12320d0b32bb2fbf0b56d6752a1" class="memitem:ga4211a12320d0b32bb2fbf0b56d6752a1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_AUTH_IS_SERVER(auth)   ((auth)-&gt;side == auth_side_server)</td>
</tr>
<tr class="separator:ga4211a12320d0b32bb2fbf0b56d6752a1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga74120265335a7f6a84041541c19074c9" class="memitem:ga74120265335a7f6a84041541c19074c9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_AUTH_IS_CLIENT(auth)   ((auth)-&gt;side == auth_side_client)</td>
</tr>
<tr class="separator:ga74120265335a7f6a84041541c19074c9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6c2966c96fefbc8b40106d6b5235c854" class="memitem:ga6c2966c96fefbc8b40106d6b5235c854">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_AUTH_CLIENT(auth)   ((DBusAuthClient*)(auth))</td>
</tr>
<tr class="separator:ga6c2966c96fefbc8b40106d6b5235c854">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3d476942b91b7b5825a914c2ae743717" class="memitem:ga3d476942b91b7b5825a914c2ae743717">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_AUTH_SERVER(auth)   ((DBusAuthServer*)(auth))</td>
</tr>
<tr class="separator:ga3d476942b91b7b5825a914c2ae743717">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga533f0d915e592df54a97401b597441b8" class="memitem:ga533f0d915e592df54a97401b597441b8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_AUTH_NAME(auth)   ((auth)-&gt;side)</td>
</tr>
<tr class="memdesc:ga533f0d915e592df54a97401b597441b8">
<td class="mdescLeft"> </td>
<td class="mdescRight">The name of the auth ("client" or "server")<br />
</td>
</tr>
<tr class="separator:ga533f0d915e592df54a97401b597441b8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae379752f3a8ebb11e727e75d87a35554" class="memitem:gae379752f3a8ebb11e727e75d87a35554">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">N_CHALLENGE_BYTES   (128/8)</td>
</tr>
<tr class="memdesc:gae379752f3a8ebb11e727e75d87a35554">
<td class="mdescLeft"> </td>
<td class="mdescRight">http://www.ietf.org/rfc/rfc2831.txt suggests at least 64 bits of entropy, we use 128.<br />
</td>
</tr>
<tr class="separator:gae379752f3a8ebb11e727e75d87a35554">
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
<td colspan="2"><h2 id="typedefs" class="groupheader"> Typedefs</h2></td>
</tr>
<tr id="r_ga9f23dc18079053baf32a1066cd13a20e" class="memitem:ga9f23dc18079053baf32a1066cd13a20e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef dbus_bool_t(* </td>
<td class="memItemRight" data-valign="bottom">DBusInitialResponseFunction) (DBusAuth *auth, DBusString *response)</td>
</tr>
<tr class="memdesc:ga9f23dc18079053baf32a1066cd13a20e">
<td class="mdescLeft"> </td>
<td class="mdescRight">This function appends an initial client response to the given string.<br />
</td>
</tr>
<tr class="separator:ga9f23dc18079053baf32a1066cd13a20e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac04ad7d16cc5a2331a5f2cc415f11cde" class="memitem:gac04ad7d16cc5a2331a5f2cc415f11cde">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef dbus_bool_t(* </td>
<td class="memItemRight" data-valign="bottom">DBusAuthDataFunction) (DBusAuth *auth, const DBusString *data)</td>
</tr>
<tr class="memdesc:gac04ad7d16cc5a2331a5f2cc415f11cde">
<td class="mdescLeft"> </td>
<td class="mdescRight">This function processes a block of data received from the peer.<br />
</td>
</tr>
<tr class="separator:gac04ad7d16cc5a2331a5f2cc415f11cde">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga29cb493be96e2e3d111c8601dbf47b79" class="memitem:ga29cb493be96e2e3d111c8601dbf47b79">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef dbus_bool_t(* </td>
<td class="memItemRight" data-valign="bottom">DBusAuthEncodeFunction) (DBusAuth *auth, const DBusString *data, DBusString *encoded)</td>
</tr>
<tr class="memdesc:ga29cb493be96e2e3d111c8601dbf47b79">
<td class="mdescLeft"> </td>
<td class="mdescRight">This function encodes a block of data from the peer.<br />
</td>
</tr>
<tr class="separator:ga29cb493be96e2e3d111c8601dbf47b79">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga38d65327047fdc3cb6af1a852257cab8" class="memitem:ga38d65327047fdc3cb6af1a852257cab8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef dbus_bool_t(* </td>
<td class="memItemRight" data-valign="bottom">DBusAuthDecodeFunction) (DBusAuth *auth, const DBusString *data, DBusString *decoded)</td>
</tr>
<tr class="memdesc:ga38d65327047fdc3cb6af1a852257cab8">
<td class="mdescLeft"> </td>
<td class="mdescRight">This function decodes a block of data from the peer.<br />
</td>
</tr>
<tr class="separator:ga38d65327047fdc3cb6af1a852257cab8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9dd06d93c552624769d701d07f41d1db" class="memitem:ga9dd06d93c552624769d701d07f41d1db">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef void(* </td>
<td class="memItemRight" data-valign="bottom">DBusAuthShutdownFunction) (DBusAuth *auth)</td>
</tr>
<tr class="memdesc:ga9dd06d93c552624769d701d07f41d1db">
<td class="mdescLeft"> </td>
<td class="mdescRight">This function is called when the mechanism is abandoned.<br />
</td>
</tr>
<tr class="separator:ga9dd06d93c552624769d701d07f41d1db">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9881820c5f1d4449027b667ef545fde1" class="memitem:ga9881820c5f1d4449027b667ef545fde1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef dbus_bool_t(* </td>
<td class="memItemRight" data-valign="bottom">DBusAuthStateFunction) (DBusAuth *auth, DBusAuthCommand command, const DBusString *args)</td>
</tr>
<tr class="memdesc:ga9881820c5f1d4449027b667ef545fde1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Auth state function, determines the reaction to incoming events for a particular state.<br />
</td>
</tr>
<tr class="separator:ga9881820c5f1d4449027b667ef545fde1">
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
<td colspan="2"><h2 id="enumerations" class="groupheader"> Enumerations</h2></td>
</tr>
<tr id="r_gabb6518f15bcdde0584166353ba8dca3b" class="memitem:gabb6518f15bcdde0584166353ba8dca3b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">enum  </td>
<td class="memItemRight" data-valign="bottom">DBusAuthCommand {<br />
  <strong>DBUS_AUTH_COMMAND_AUTH</strong> , <strong>DBUS_AUTH_COMMAND_CANCEL</strong> , <strong>DBUS_AUTH_COMMAND_DATA</strong> , <strong>DBUS_AUTH_COMMAND_BEGIN</strong> ,<br />
  <strong>DBUS_AUTH_COMMAND_REJECTED</strong> , <strong>DBUS_AUTH_COMMAND_OK</strong> , <strong>DBUS_AUTH_COMMAND_ERROR</strong> , <strong>DBUS_AUTH_COMMAND_UNKNOWN</strong> ,<br />
  <strong>DBUS_AUTH_COMMAND_NEGOTIATE_UNIX_FD</strong> , <strong>DBUS_AUTH_COMMAND_AGREE_UNIX_FD</strong><br />
}</td>
</tr>
<tr class="memdesc:gabb6518f15bcdde0584166353ba8dca3b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Enumeration for the known authentication commands. More...<br />
</td>
</tr>
<tr class="separator:gabb6518f15bcdde0584166353ba8dca3b">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

DBusAuth implementation details.

Private details of authentication code.

## Macro Definition Documentation

## ◆ DBUS_AUTH_CLIENT

|                           |     |     |      |     |                               |
|---------------------------|-----|-----|------|-----|-------------------------------|
| \#define DBUS_AUTH_CLIENT | (   |     | auth | )   |    ((DBusAuthClient\*)(auth)) |

Parameters  
|      |                       |
|------|-----------------------|
| auth | the auth conversation |

<!-- -->

Returns  
auth cast to DBusAuthClient

Definition at line 328 of file dbus-auth.c.

## ◆ DBUS_AUTH_IS_CLIENT

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| \#define DBUS_AUTH_IS_CLIENT | ( |   | auth | ) |    ((auth)-\>side == auth_side_client) |

Parameters  
|      |                       |
|------|-----------------------|
| auth | the auth conversation |

<!-- -->

Returns  
TRUE if the conversation is the client side

Definition at line 323 of file dbus-auth.c.

## ◆ DBUS_AUTH_IS_SERVER

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| \#define DBUS_AUTH_IS_SERVER | ( |   | auth | ) |    ((auth)-\>side == auth_side_server) |

Parameters  
|      |                       |
|------|-----------------------|
| auth | the auth conversation |

<!-- -->

Returns  
TRUE if the conversation is the server side

Definition at line 318 of file dbus-auth.c.

## ◆ DBUS_AUTH_NAME

|                         |     |     |      |     |                    |
|-------------------------|-----|-----|------|-----|--------------------|
| \#define DBUS_AUTH_NAME | (   |     | auth | )   |    ((auth)-\>side) |

The name of the auth ("client" or "server")

Parameters  
|      |                       |
|------|-----------------------|
| auth | the auth conversation |

<!-- -->

Returns  
a string

Definition at line 340 of file dbus-auth.c.

## ◆ DBUS_AUTH_SERVER

|                           |     |     |      |     |                               |
|---------------------------|-----|-----|------|-----|-------------------------------|
| \#define DBUS_AUTH_SERVER | (   |     | auth | )   |    ((DBusAuthServer\*)(auth)) |

Parameters  
|      |                       |
|------|-----------------------|
| auth | the auth conversation |

<!-- -->

Returns  
auth cast to DBusAuthServer

Definition at line 333 of file dbus-auth.c.

## ◆ N_CHALLENGE_BYTES

|                                      |
|--------------------------------------|
| \#define N_CHALLENGE_BYTES   (128/8) |

http://www.ietf.org/rfc/rfc2831.txt suggests at least 64 bits of entropy, we use 128.

This is the number of bytes in the random challenge.

Definition at line 521 of file dbus-auth.c.

## Typedef Documentation

## ◆ DBusAuthDataFunction

|  |
|----|
| typedef dbus_bool_t(\* DBusAuthDataFunction) (DBusAuth \*auth, const DBusString \*data) |

This function processes a block of data received from the peer.

i.e. handles a DATA command.

Definition at line 79 of file dbus-auth.c.

## ◆ DBusAuthDecodeFunction

|  |
|----|
| typedef dbus_bool_t(\* DBusAuthDecodeFunction) (DBusAuth \*auth, const DBusString \*data, DBusString \*decoded) |

This function decodes a block of data from the peer.

Definition at line 92 of file dbus-auth.c.

## ◆ DBusAuthEncodeFunction

|  |
|----|
| typedef dbus_bool_t(\* DBusAuthEncodeFunction) (DBusAuth \*auth, const DBusString \*data, DBusString \*encoded) |

This function encodes a block of data from the peer.

Definition at line 85 of file dbus-auth.c.

## ◆ DBusAuthShutdownFunction

|                                                             |
|-------------------------------------------------------------|
| typedef void(\* DBusAuthShutdownFunction) (DBusAuth \*auth) |

This function is called when the mechanism is abandoned.

Definition at line 99 of file dbus-auth.c.

## ◆ DBusAuthStateFunction

|  |
|----|
| typedef dbus_bool_t(\* DBusAuthStateFunction) (DBusAuth \*auth, DBusAuthCommand command, const DBusString \*args) |

Auth state function, determines the reaction to incoming events for a particular state.

Returns whether we had enough memory to complete the operation.

Definition at line 139 of file dbus-auth.c.

## ◆ DBusInitialResponseFunction

|  |
|----|
| typedef dbus_bool_t(\* DBusInitialResponseFunction) (DBusAuth \*auth, DBusString \*response) |

This function appends an initial client response to the given string.

Definition at line 72 of file dbus-auth.c.

## Enumeration Type Documentation

## ◆ DBusAuthCommand

|                      |
|----------------------|
| enum DBusAuthCommand |

Enumeration for the known authentication commands.

Definition at line 121 of file dbus-auth.c.
