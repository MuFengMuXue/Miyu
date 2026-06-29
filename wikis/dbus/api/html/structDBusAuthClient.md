DBusAuthClient Struct Reference

D-Bus secret internal implementation details » Authentication implementation details

"Subclass" of DBusAuth for client side More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a7aaf0c9832007ece465ac5289e5d7a8b" class="memitem:a7aaf0c9832007ece465ac5289e5d7a8b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusAuth </td>
<td class="memItemRight" data-valign="bottom">base</td>
</tr>
<tr class="memdesc:a7aaf0c9832007ece465ac5289e5d7a8b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Parent class.<br />
</td>
</tr>
<tr class="separator:a7aaf0c9832007ece465ac5289e5d7a8b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a646ae1e39e617ec3e3dd097fc18372eb" class="memitem:a646ae1e39e617ec3e3dd097fc18372eb">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusList * </td>
<td class="memItemRight" data-valign="bottom">mechs_to_try</td>
</tr>
<tr class="memdesc:a646ae1e39e617ec3e3dd097fc18372eb">
<td class="mdescLeft"> </td>
<td class="mdescRight">Mechanisms we got from the server that we're going to try using.<br />
</td>
</tr>
<tr class="separator:a646ae1e39e617ec3e3dd097fc18372eb">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a91607b9958e0eaf7da388d9b9a347f08" class="memitem:a91607b9958e0eaf7da388d9b9a347f08">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusString </td>
<td class="memItemRight" data-valign="bottom">guid_from_server</td>
</tr>
<tr class="memdesc:a91607b9958e0eaf7da388d9b9a347f08">
<td class="mdescLeft"> </td>
<td class="mdescRight">GUID received from server.<br />
</td>
</tr>
<tr class="separator:a91607b9958e0eaf7da388d9b9a347f08">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

"Subclass" of DBusAuth for client side

Definition at line 201 of file dbus-auth.c.

## Field Documentation

## ◆ base

|                               |
|-------------------------------|
| DBusAuth DBusAuthClient::base |

Parent class.

Definition at line 203 of file dbus-auth.c.

## ◆ guid_from_server

|                                             |
|---------------------------------------------|
| DBusString DBusAuthClient::guid_from_server |

GUID received from server.

Definition at line 207 of file dbus-auth.c.

## ◆ mechs_to_try

|                                         |
|-----------------------------------------|
| DBusList\* DBusAuthClient::mechs_to_try |

Mechanisms we got from the server that we're going to try using.

Definition at line 205 of file dbus-auth.c.

The documentation for this struct was generated from the following file:

- dbus-auth.c
