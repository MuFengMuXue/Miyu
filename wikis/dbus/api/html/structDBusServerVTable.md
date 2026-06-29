DBusServerVTable Struct Reference

Virtual table to be implemented by all server "subclasses". More...

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
<tr id="r_afc522ca130f064c199c380e41dec87c5" class="memitem:afc522ca130f064c199c380e41dec87c5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void(* </td>
<td class="memItemRight" data-valign="bottom">finalize )(DBusServer *server)</td>
</tr>
<tr class="memdesc:afc522ca130f064c199c380e41dec87c5">
<td class="mdescLeft"> </td>
<td class="mdescRight">The finalize method must free the server.<br />
</td>
</tr>
<tr class="separator:afc522ca130f064c199c380e41dec87c5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a05c263c7b87cdedf9a3bcaac8898f9b4" class="memitem:a05c263c7b87cdedf9a3bcaac8898f9b4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void(* </td>
<td class="memItemRight" data-valign="bottom">disconnect )(DBusServer *server)</td>
</tr>
<tr class="memdesc:a05c263c7b87cdedf9a3bcaac8898f9b4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Disconnect this server.<br />
</td>
</tr>
<tr class="separator:a05c263c7b87cdedf9a3bcaac8898f9b4">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Virtual table to be implemented by all server "subclasses".

Definition at line 45 of file dbus-server-protected.h.

## Field Documentation

## ◆ disconnect

|                                                             |
|-------------------------------------------------------------|
| void(\* DBusServerVTable::disconnect) (DBusServer \*server) |

Disconnect this server.

Definition at line 50 of file dbus-server-protected.h.

## ◆ finalize

|                                                           |
|-----------------------------------------------------------|
| void(\* DBusServerVTable::finalize) (DBusServer \*server) |

The finalize method must free the server.

Definition at line 47 of file dbus-server-protected.h.

Referenced by \_dbus_server_unref_unlocked(), and dbus_server_unref().

The documentation for this struct was generated from the following file:

- dbus-server-protected.h
