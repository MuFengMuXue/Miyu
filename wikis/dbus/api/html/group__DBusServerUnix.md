DBusServer implementations for UNIX

D-Bus secret internal implementation details

Implementation details of DBusServer on UNIX. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="functions" class="groupheader"> Functions</h2></td>
</tr>
<tr id="r_gaec00cdf4977b9bd33621df684406a779" class="memitem:gaec00cdf4977b9bd33621df684406a779">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusServerListenResult </td>
<td class="memItemRight" data-valign="bottom">_dbus_server_listen_platform_specific (DBusAddressEntry *entry, DBusServer **server_p, DBusError *error)</td>
</tr>
<tr class="memdesc:gaec00cdf4977b9bd33621df684406a779">
<td class="mdescLeft"> </td>
<td class="mdescRight">Tries to interpret the address entry in a platform-specific way, creating a platform-specific server type if appropriate.<br />
</td>
</tr>
<tr class="separator:gaec00cdf4977b9bd33621df684406a779">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Implementation details of DBusServer on UNIX.

## Function Documentation

## ◆ \_dbus_server_listen_platform_specific()

|  |  |  |  |
|----|----|----|----|
| DBusServerListenResult \_dbus_server_listen_platform_specific | ( | DBusAddressEntry \*  | *entry*, |
|  |  | DBusServer \*\*  | *server_p*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Tries to interpret the address entry in a platform-specific way, creating a platform-specific server type if appropriate.

Sets error if the result is not OK.

Parameters  
|          |                                                         |
|----------|---------------------------------------------------------|
| entry    | an address entry                                        |
| server_p | location to store a new DBusServer, or NULL on failure. |
| error    | location to store rationale for failure on bad address  |

<!-- -->

Returns  
the outcome

Definition at line 55 of file dbus-server-unix.c.
