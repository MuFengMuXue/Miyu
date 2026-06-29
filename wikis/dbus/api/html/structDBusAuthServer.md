DBusAuthServer Struct Reference

D-Bus secret internal implementation details » Authentication implementation details

"Subclass" of DBusAuth for server side. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_ab43e81116262d4dde5e6b923120ac3a0" class="memitem:ab43e81116262d4dde5e6b923120ac3a0">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusAuth </td>
<td class="memItemRight" data-valign="bottom">base</td>
</tr>
<tr class="memdesc:ab43e81116262d4dde5e6b923120ac3a0">
<td class="mdescLeft"> </td>
<td class="mdescRight">Parent class.<br />
</td>
</tr>
<tr class="separator:ab43e81116262d4dde5e6b923120ac3a0">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ac73a6f0760eca6e1b7204b3c8e9c6127" class="memitem:ac73a6f0760eca6e1b7204b3c8e9c6127">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">failures</td>
</tr>
<tr class="memdesc:ac73a6f0760eca6e1b7204b3c8e9c6127">
<td class="mdescLeft"> </td>
<td class="mdescRight">Number of times client has been rejected.<br />
</td>
</tr>
<tr class="separator:ac73a6f0760eca6e1b7204b3c8e9c6127">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a0527732b2f979011cfeb501c8347fda0" class="memitem:a0527732b2f979011cfeb501c8347fda0">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">max_failures</td>
</tr>
<tr class="memdesc:a0527732b2f979011cfeb501c8347fda0">
<td class="mdescLeft"> </td>
<td class="mdescRight">Number of times we reject before disconnect.<br />
</td>
</tr>
<tr class="separator:a0527732b2f979011cfeb501c8347fda0">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a4e5f1bdf9bf827a0d6d370bbad73af1c" class="memitem:a4e5f1bdf9bf827a0d6d370bbad73af1c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusString </td>
<td class="memItemRight" data-valign="bottom">guid</td>
</tr>
<tr class="memdesc:a4e5f1bdf9bf827a0d6d370bbad73af1c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Our globally unique ID in hex encoding.<br />
</td>
</tr>
<tr class="separator:a4e5f1bdf9bf827a0d6d370bbad73af1c">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

"Subclass" of DBusAuth for server side.

Definition at line 214 of file dbus-auth.c.

## Field Documentation

## ◆ base

|                               |
|-------------------------------|
| DBusAuth DBusAuthServer::base |

Parent class.

Definition at line 216 of file dbus-auth.c.

## ◆ failures

|                              |
|------------------------------|
| int DBusAuthServer::failures |

Number of times client has been rejected.

Definition at line 218 of file dbus-auth.c.

Referenced by \_dbus_auth_server_new().

## ◆ guid

|                                 |
|---------------------------------|
| DBusString DBusAuthServer::guid |

Our globally unique ID in hex encoding.

Definition at line 221 of file dbus-auth.c.

Referenced by \_dbus_auth_server_new().

## ◆ max_failures

|                                  |
|----------------------------------|
| int DBusAuthServer::max_failures |

Number of times we reject before disconnect.

Definition at line 219 of file dbus-auth.c.

Referenced by \_dbus_auth_server_new().

The documentation for this struct was generated from the following file:

- dbus-auth.c
