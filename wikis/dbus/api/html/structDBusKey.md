DBusKey Struct Reference

D-Bus secret internal implementation details » DBusKeyring implementation details

A single key from the cookie file. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_ac9fd0e664b5e21c63c97f3ade3349c70" class="memitem:ac9fd0e664b5e21c63c97f3ade3349c70">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_int32_t </td>
<td class="memItemRight" data-valign="bottom">id</td>
</tr>
<tr class="memdesc:ac9fd0e664b5e21c63c97f3ade3349c70">
<td class="mdescLeft"> </td>
<td class="mdescRight">identifier used to refer to the key<br />
</td>
</tr>
<tr class="separator:ac9fd0e664b5e21c63c97f3ade3349c70">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_af45bfd721fbf5ec564edc8390c7ba6af" class="memitem:af45bfd721fbf5ec564edc8390c7ba6af">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_int64_t </td>
<td class="memItemRight" data-valign="bottom">creation_time</td>
</tr>
<tr class="memdesc:af45bfd721fbf5ec564edc8390c7ba6af">
<td class="mdescLeft"> </td>
<td class="mdescRight">when the key was generated, in seconds since 1970-01-01<br />
</td>
</tr>
<tr class="separator:af45bfd721fbf5ec564edc8390c7ba6af">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a444e3f33c387af833dc78ba96b6a9ea6" class="memitem:a444e3f33c387af833dc78ba96b6a9ea6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusString </td>
<td class="memItemRight" data-valign="bottom">secret</td>
</tr>
<tr class="memdesc:a444e3f33c387af833dc78ba96b6a9ea6">
<td class="mdescLeft"> </td>
<td class="mdescRight">the actual key<br />
</td>
</tr>
<tr class="separator:a444e3f33c387af833dc78ba96b6a9ea6">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

A single key from the cookie file.

Definition at line 95 of file dbus-keyring.c.

## Field Documentation

## ◆ creation_time

|                                     |
|-------------------------------------|
| dbus_int64_t DBusKey::creation_time |

when the key was generated, in seconds since 1970-01-01

Definition at line 99 of file dbus-keyring.c.

## ◆ id

|                          |
|--------------------------|
| dbus_int32_t DBusKey::id |

identifier used to refer to the key

Definition at line 97 of file dbus-keyring.c.

Referenced by \_dbus_keyring_get_best_key().

## ◆ secret

|                            |
|----------------------------|
| DBusString DBusKey::secret |

the actual key

Definition at line 101 of file dbus-keyring.c.

Referenced by \_dbus_keyring_get_hex_key().

The documentation for this struct was generated from the following file:

- dbus-keyring.c
