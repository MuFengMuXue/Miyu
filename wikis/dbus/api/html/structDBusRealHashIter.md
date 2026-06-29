DBusRealHashIter Struct Reference

D-Bus secret internal implementation details » Hash table implementation details

Internals of DBusHashIter. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a0307c2b8fa9384554ceb3cc965b04633" class="memitem:a0307c2b8fa9384554ceb3cc965b04633">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusHashTable * </td>
<td class="memItemRight" data-valign="bottom">table</td>
</tr>
<tr class="memdesc:a0307c2b8fa9384554ceb3cc965b04633">
<td class="mdescLeft"> </td>
<td class="mdescRight">Pointer to table containing entry.<br />
</td>
</tr>
<tr class="separator:a0307c2b8fa9384554ceb3cc965b04633">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ad36967dc68709d676ad591d7f75dd7fa" class="memitem:ad36967dc68709d676ad591d7f75dd7fa">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusHashEntry ** </td>
<td class="memItemRight" data-valign="bottom">bucket</td>
</tr>
<tr class="memdesc:ad36967dc68709d676ad591d7f75dd7fa">
<td class="mdescLeft"> </td>
<td class="mdescRight">Pointer to bucket that points to first entry in this entry's chain: used for deleting the entry.<br />
</td>
</tr>
<tr class="separator:ad36967dc68709d676ad591d7f75dd7fa">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a438db1cb3a9c6db716f8bf35fe3054c7" class="memitem:a438db1cb3a9c6db716f8bf35fe3054c7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusHashEntry * </td>
<td class="memItemRight" data-valign="bottom">entry</td>
</tr>
<tr class="memdesc:a438db1cb3a9c6db716f8bf35fe3054c7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Current hash entry.<br />
</td>
</tr>
<tr class="separator:a438db1cb3a9c6db716f8bf35fe3054c7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a056417c3726f4f98eb94a9d2784a59e0" class="memitem:a056417c3726f4f98eb94a9d2784a59e0">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusHashEntry * </td>
<td class="memItemRight" data-valign="bottom">next_entry</td>
</tr>
<tr class="memdesc:a056417c3726f4f98eb94a9d2784a59e0">
<td class="mdescLeft"> </td>
<td class="mdescRight">Next entry to be iterated onto in current bucket.<br />
</td>
</tr>
<tr class="separator:a056417c3726f4f98eb94a9d2784a59e0">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_adbf758933299ee6305c525ea0fe74824" class="memitem:adbf758933299ee6305c525ea0fe74824">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">next_bucket</td>
</tr>
<tr class="memdesc:adbf758933299ee6305c525ea0fe74824">
<td class="mdescLeft"> </td>
<td class="mdescRight">index of next bucket<br />
</td>
</tr>
<tr class="separator:adbf758933299ee6305c525ea0fe74824">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a84f2a189ee1eb3e51a8089b798a7797a" class="memitem:a84f2a189ee1eb3e51a8089b798a7797a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">n_entries_on_init</td>
</tr>
<tr class="memdesc:a84f2a189ee1eb3e51a8089b798a7797a">
<td class="mdescLeft"> </td>
<td class="mdescRight">used to detect table resize since initialization<br />
</td>
</tr>
<tr class="separator:a84f2a189ee1eb3e51a8089b798a7797a">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Internals of DBusHashIter.

Definition at line 219 of file dbus-hash.c.

## Field Documentation

## ◆ bucket

|                                            |
|--------------------------------------------|
| DBusHashEntry\*\* DBusRealHashIter::bucket |

Pointer to bucket that points to first entry in this entry's chain: used for deleting the entry.

Definition at line 222 of file dbus-hash.c.

Referenced by \_dbus_hash_iter_init(), \_dbus_hash_iter_lookup(), \_dbus_hash_iter_next(), and \_dbus_hash_iter_remove_entry().

## ◆ entry

|                                         |
|-----------------------------------------|
| DBusHashEntry\* DBusRealHashIter::entry |

Current hash entry.

Definition at line 226 of file dbus-hash.c.

Referenced by \_dbus_hash_iter_get_int_key(), \_dbus_hash_iter_get_string_key(), \_dbus_hash_iter_get_uintptr_key(), \_dbus_hash_iter_get_value(), \_dbus_hash_iter_init(), \_dbus_hash_iter_lookup(), \_dbus_hash_iter_next(), \_dbus_hash_iter_remove_entry(), and \_dbus_hash_iter_set_value().

## ◆ n_entries_on_init

|                                         |
|-----------------------------------------|
| int DBusRealHashIter::n_entries_on_init |

used to detect table resize since initialization

Definition at line 229 of file dbus-hash.c.

Referenced by \_dbus_hash_iter_init(), \_dbus_hash_iter_lookup(), and \_dbus_hash_iter_next().

## ◆ next_bucket

|                                   |
|-----------------------------------|
| int DBusRealHashIter::next_bucket |

index of next bucket

Definition at line 228 of file dbus-hash.c.

Referenced by \_dbus_hash_iter_init(), \_dbus_hash_iter_lookup(), and \_dbus_hash_iter_next().

## ◆ next_entry

|                                              |
|----------------------------------------------|
| DBusHashEntry\* DBusRealHashIter::next_entry |

Next entry to be iterated onto in current bucket.

Definition at line 227 of file dbus-hash.c.

Referenced by \_dbus_hash_iter_init(), \_dbus_hash_iter_lookup(), and \_dbus_hash_iter_next().

## ◆ table

|                                         |
|-----------------------------------------|
| DBusHashTable\* DBusRealHashIter::table |

Pointer to table containing entry.

Definition at line 221 of file dbus-hash.c.

Referenced by \_dbus_hash_iter_get_int_key(), \_dbus_hash_iter_get_string_key(), \_dbus_hash_iter_get_uintptr_key(), \_dbus_hash_iter_get_value(), \_dbus_hash_iter_init(), \_dbus_hash_iter_lookup(), \_dbus_hash_iter_next(), \_dbus_hash_iter_remove_entry(), and \_dbus_hash_iter_set_value().

The documentation for this struct was generated from the following file:

- dbus-hash.c
