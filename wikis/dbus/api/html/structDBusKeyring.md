DBusKeyring Struct Reference

D-Bus secret internal implementation details » DBusKeyring implementation details

Internals of DBusKeyring. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_abd3bb1b915d602c6d8b6c582f55d1590" class="memitem:abd3bb1b915d602c6d8b6c582f55d1590">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">refcount</td>
</tr>
<tr class="memdesc:abd3bb1b915d602c6d8b6c582f55d1590">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reference count.<br />
</td>
</tr>
<tr class="separator:abd3bb1b915d602c6d8b6c582f55d1590">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ac7274d864db3f2239b2c4ec734da94da" class="memitem:ac7274d864db3f2239b2c4ec734da94da">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusString </td>
<td class="memItemRight" data-valign="bottom">directory</td>
</tr>
<tr class="memdesc:ac7274d864db3f2239b2c4ec734da94da">
<td class="mdescLeft"> </td>
<td class="mdescRight">Directory the below two items are inside.<br />
</td>
</tr>
<tr class="separator:ac7274d864db3f2239b2c4ec734da94da">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a38b402331379977ffd151d327b66dc1f" class="memitem:a38b402331379977ffd151d327b66dc1f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusString </td>
<td class="memItemRight" data-valign="bottom">filename</td>
</tr>
<tr class="memdesc:a38b402331379977ffd151d327b66dc1f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Keyring filename.<br />
</td>
</tr>
<tr class="separator:a38b402331379977ffd151d327b66dc1f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ad4ac7b540d393d588c44aaa2c2f79056" class="memitem:ad4ac7b540d393d588c44aaa2c2f79056">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusString </td>
<td class="memItemRight" data-valign="bottom">filename_lock</td>
</tr>
<tr class="memdesc:ad4ac7b540d393d588c44aaa2c2f79056">
<td class="mdescLeft"> </td>
<td class="mdescRight">Name of lockfile.<br />
</td>
</tr>
<tr class="separator:ad4ac7b540d393d588c44aaa2c2f79056">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a2f415a81a41f5827df7ecffbfdbd13cf" class="memitem:a2f415a81a41f5827df7ecffbfdbd13cf">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusKey * </td>
<td class="memItemRight" data-valign="bottom">keys</td>
</tr>
<tr class="memdesc:a2f415a81a41f5827df7ecffbfdbd13cf">
<td class="mdescLeft"> </td>
<td class="mdescRight">Keys loaded from the file.<br />
</td>
</tr>
<tr class="separator:a2f415a81a41f5827df7ecffbfdbd13cf">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a82dbc0da13a4f11d831f448a1d2ada1f" class="memitem:a82dbc0da13a4f11d831f448a1d2ada1f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">n_keys</td>
</tr>
<tr class="memdesc:a82dbc0da13a4f11d831f448a1d2ada1f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Number of keys.<br />
</td>
</tr>
<tr class="separator:a82dbc0da13a4f11d831f448a1d2ada1f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a5fce1fd5f4255b922caeda643ecb69cc" class="memitem:a5fce1fd5f4255b922caeda643ecb69cc">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusCredentials * </td>
<td class="memItemRight" data-valign="bottom">credentials</td>
</tr>
<tr class="memdesc:a5fce1fd5f4255b922caeda643ecb69cc">
<td class="mdescLeft"> </td>
<td class="mdescRight">Credentials containing user the keyring is for.<br />
</td>
</tr>
<tr class="separator:a5fce1fd5f4255b922caeda643ecb69cc">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Internals of DBusKeyring.

DBusKeyring internals. DBusKeyring is an opaque object, it must be used via accessor functions.

Definition at line 111 of file dbus-keyring.c.

## Field Documentation

## ◆ credentials

|                                            |
|--------------------------------------------|
| DBusCredentials\* DBusKeyring::credentials |

Credentials containing user the keyring is for.

Definition at line 119 of file dbus-keyring.c.

Referenced by \_dbus_keyring_is_for_credentials(), \_dbus_keyring_new_for_credentials(), and \_dbus_keyring_unref().

## ◆ directory

|                                   |
|-----------------------------------|
| DBusString DBusKeyring::directory |

Directory the below two items are inside.

Definition at line 114 of file dbus-keyring.c.

Referenced by \_dbus_keyring_new_for_credentials(), and \_dbus_keyring_unref().

## ◆ filename

|                                  |
|----------------------------------|
| DBusString DBusKeyring::filename |

Keyring filename.

Definition at line 115 of file dbus-keyring.c.

Referenced by \_dbus_keyring_new_for_credentials(), and \_dbus_keyring_unref().

## ◆ filename_lock

|                                       |
|---------------------------------------|
| DBusString DBusKeyring::filename_lock |

Name of lockfile.

Definition at line 116 of file dbus-keyring.c.

Referenced by \_dbus_keyring_new_for_credentials(), and \_dbus_keyring_unref().

## ◆ keys

|                             |
|-----------------------------|
| DBusKey\* DBusKeyring::keys |

Keys loaded from the file.

Definition at line 117 of file dbus-keyring.c.

Referenced by \_dbus_keyring_get_hex_key(), and \_dbus_keyring_unref().

## ◆ n_keys

|                         |
|-------------------------|
| int DBusKeyring::n_keys |

Number of keys.

Definition at line 118 of file dbus-keyring.c.

Referenced by \_dbus_keyring_get_hex_key(), and \_dbus_keyring_unref().

## ◆ refcount

|                           |
|---------------------------|
| int DBusKeyring::refcount |

Reference count.

Definition at line 113 of file dbus-keyring.c.

Referenced by \_dbus_keyring_ref(), and \_dbus_keyring_unref().

The documentation for this struct was generated from the following file:

- dbus-keyring.c
