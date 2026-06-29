DBusHashEntry Struct Reference

D-Bus secret internal implementation details » Hash table implementation details

Internal representation of a hash entry. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_ae986e25c0b24237f9848ff43aa1d8501" class="memitem:ae986e25c0b24237f9848ff43aa1d8501">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusHashEntry * </td>
<td class="memItemRight" data-valign="bottom">next</td>
</tr>
<tr class="memdesc:ae986e25c0b24237f9848ff43aa1d8501">
<td class="mdescLeft"> </td>
<td class="mdescRight">Pointer to next entry in this hash bucket, or NULL for end of chain.<br />
</td>
</tr>
<tr class="separator:ae986e25c0b24237f9848ff43aa1d8501">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aefd9bbdcbc7d15c906e2c289c8d2e894" class="memitem:aefd9bbdcbc7d15c906e2c289c8d2e894">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">key</td>
</tr>
<tr class="memdesc:aefd9bbdcbc7d15c906e2c289c8d2e894">
<td class="mdescLeft"> </td>
<td class="mdescRight">Hash key.<br />
</td>
</tr>
<tr class="separator:aefd9bbdcbc7d15c906e2c289c8d2e894">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ad792e9c81cc3a23859b2c60b3b00af3e" class="memitem:ad792e9c81cc3a23859b2c60b3b00af3e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">value</td>
</tr>
<tr class="memdesc:ad792e9c81cc3a23859b2c60b3b00af3e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Hash value.<br />
</td>
</tr>
<tr class="separator:ad792e9c81cc3a23859b2c60b3b00af3e">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Internal representation of a hash entry.

A single entry (key-value pair) in the hash table. Internal to hash table implementation.

Definition at line 150 of file dbus-hash.c.

## Field Documentation

## ◆ key

|                           |
|---------------------------|
| void\* DBusHashEntry::key |

Hash key.

Definition at line 156 of file dbus-hash.c.

Referenced by \_dbus_hash_iter_get_int_key(), \_dbus_hash_iter_get_string_key(), \_dbus_hash_iter_get_uintptr_key(), \_dbus_hash_iter_lookup(), \_dbus_hash_table_insert_int(), \_dbus_hash_table_insert_string_preallocated(), and \_dbus_hash_table_insert_uintptr().

## ◆ next

|                                     |
|-------------------------------------|
| DBusHashEntry\* DBusHashEntry::next |

Pointer to next entry in this hash bucket, or NULL for end of chain.

Definition at line 152 of file dbus-hash.c.

Referenced by \_dbus_hash_iter_lookup(), \_dbus_hash_iter_next(), and \_dbus_hash_table_unref().

## ◆ value

|                             |
|-----------------------------|
| void\* DBusHashEntry::value |

Hash value.

Definition at line 157 of file dbus-hash.c.

Referenced by \_dbus_hash_iter_get_value(), \_dbus_hash_iter_set_value(), \_dbus_hash_table_insert_int(), \_dbus_hash_table_insert_string_preallocated(), \_dbus_hash_table_insert_uintptr(), \_dbus_hash_table_lookup_int(), \_dbus_hash_table_lookup_string(), and \_dbus_hash_table_lookup_uintptr().

The documentation for this struct was generated from the following file:

- dbus-hash.c
