DBusHashTable Struct Reference

D-Bus secret internal implementation details » Hash table implementation details

Internals of DBusHashTable. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_acb2b7bcba65da77f7ecf67da355ff770" class="memitem:acb2b7bcba65da77f7ecf67da355ff770">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">refcount</td>
</tr>
<tr class="memdesc:acb2b7bcba65da77f7ecf67da355ff770">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reference count.<br />
</td>
</tr>
<tr class="separator:acb2b7bcba65da77f7ecf67da355ff770">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a1f974e2cb3038685b3edf493406ad99d" class="memitem:a1f974e2cb3038685b3edf493406ad99d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusHashEntry ** </td>
<td class="memItemRight" data-valign="bottom">buckets</td>
</tr>
<tr class="memdesc:a1f974e2cb3038685b3edf493406ad99d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Pointer to bucket array.<br />
</td>
</tr>
<tr class="separator:a1f974e2cb3038685b3edf493406ad99d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_af71877d64657c34a783caf6b82b016e9" class="memitem:af71877d64657c34a783caf6b82b016e9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusHashEntry * </td>
<td class="memItemRight" data-valign="bottom">static_buckets [DBUS_SMALL_HASH_TABLE]</td>
</tr>
<tr class="memdesc:af71877d64657c34a783caf6b82b016e9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Bucket array used for small tables (to avoid mallocs and frees).<br />
</td>
</tr>
<tr class="separator:af71877d64657c34a783caf6b82b016e9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a2dd2b9389d65d30e31e596dd786a9aa7" class="memitem:a2dd2b9389d65d30e31e596dd786a9aa7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">n_buckets</td>
</tr>
<tr class="memdesc:a2dd2b9389d65d30e31e596dd786a9aa7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Total number of buckets allocated at **buckets.<br />
</td>
</tr>
<tr class="separator:a2dd2b9389d65d30e31e596dd786a9aa7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_affbf11a9c3dd72d55b7976891f7b4650" class="memitem:affbf11a9c3dd72d55b7976891f7b4650">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">n_entries</td>
</tr>
<tr class="memdesc:affbf11a9c3dd72d55b7976891f7b4650">
<td class="mdescLeft"> </td>
<td class="mdescRight">Total number of entries present in table.<br />
</td>
</tr>
<tr class="separator:affbf11a9c3dd72d55b7976891f7b4650">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a29c408110c0d189d89b60c6c01cfb0cf" class="memitem:a29c408110c0d189d89b60c6c01cfb0cf">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">hi_rebuild_size</td>
</tr>
<tr class="memdesc:a29c408110c0d189d89b60c6c01cfb0cf">
<td class="mdescLeft"> </td>
<td class="mdescRight">Enlarge table when n_entries gets to be this large.<br />
</td>
</tr>
<tr class="separator:a29c408110c0d189d89b60c6c01cfb0cf">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aae6ea7cb15d618866854b2b6bd468419" class="memitem:aae6ea7cb15d618866854b2b6bd468419">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">lo_rebuild_size</td>
</tr>
<tr class="memdesc:aae6ea7cb15d618866854b2b6bd468419">
<td class="mdescLeft"> </td>
<td class="mdescRight">Shrink table when n_entries gets below this.<br />
</td>
</tr>
<tr class="separator:aae6ea7cb15d618866854b2b6bd468419">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a2e7e7b92bb9633ab95cfaa592b89025c" class="memitem:a2e7e7b92bb9633ab95cfaa592b89025c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">down_shift</td>
</tr>
<tr class="memdesc:a2e7e7b92bb9633ab95cfaa592b89025c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Shift count used in hashing function.<br />
</td>
</tr>
<tr class="separator:a2e7e7b92bb9633ab95cfaa592b89025c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aec1230eebce3d256ca9ceebe372647e9" class="memitem:aec1230eebce3d256ca9ceebe372647e9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">mask</td>
</tr>
<tr class="memdesc:aec1230eebce3d256ca9ceebe372647e9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Mask value used in hashing function.<br />
</td>
</tr>
<tr class="separator:aec1230eebce3d256ca9ceebe372647e9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a28f326a2947b6be0b0b852db376a1092" class="memitem:a28f326a2947b6be0b0b852db376a1092">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusHashType </td>
<td class="memItemRight" data-valign="bottom">key_type</td>
</tr>
<tr class="memdesc:a28f326a2947b6be0b0b852db376a1092">
<td class="mdescLeft"> </td>
<td class="mdescRight">Type of keys used in this table.<br />
</td>
</tr>
<tr class="separator:a28f326a2947b6be0b0b852db376a1092">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ab98bafddf1b1ce1dad01c5595e278e35" class="memitem:ab98bafddf1b1ce1dad01c5595e278e35">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusFindEntryFunction </td>
<td class="memItemRight" data-valign="bottom">find_function</td>
</tr>
<tr class="memdesc:ab98bafddf1b1ce1dad01c5595e278e35">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function for finding entries.<br />
</td>
</tr>
<tr class="separator:ab98bafddf1b1ce1dad01c5595e278e35">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a5f6541574ea8e6bedd80773dce8e52a6" class="memitem:a5f6541574ea8e6bedd80773dce8e52a6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusFreeFunction </td>
<td class="memItemRight" data-valign="bottom">free_key_function</td>
</tr>
<tr class="memdesc:a5f6541574ea8e6bedd80773dce8e52a6">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to free keys.<br />
</td>
</tr>
<tr class="separator:a5f6541574ea8e6bedd80773dce8e52a6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_afbb42b5326b9c79352b168eace1687ca" class="memitem:afbb42b5326b9c79352b168eace1687ca">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusFreeFunction </td>
<td class="memItemRight" data-valign="bottom">free_value_function</td>
</tr>
<tr class="memdesc:afbb42b5326b9c79352b168eace1687ca">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to free values.<br />
</td>
</tr>
<tr class="separator:afbb42b5326b9c79352b168eace1687ca">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ad1224e6c3c632afb265b78f8f6e30f97" class="memitem:ad1224e6c3c632afb265b78f8f6e30f97">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMemPool * </td>
<td class="memItemRight" data-valign="bottom">entry_pool</td>
</tr>
<tr class="memdesc:ad1224e6c3c632afb265b78f8f6e30f97">
<td class="mdescLeft"> </td>
<td class="mdescRight">Memory pool for hash entries.<br />
</td>
</tr>
<tr class="separator:ad1224e6c3c632afb265b78f8f6e30f97">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Internals of DBusHashTable.

Hash table internals. Hash tables are opaque objects, they must be used via accessor functions.

Definition at line 175 of file dbus-hash.c.

## Field Documentation

## ◆ buckets

|                                          |
|------------------------------------------|
| DBusHashEntry\*\* DBusHashTable::buckets |

Pointer to bucket array.

Each element points to first entry in bucket's hash chain, or NULL.

Definition at line 178 of file dbus-hash.c.

Referenced by \_dbus_hash_iter_lookup(), \_dbus_hash_iter_next(), \_dbus_hash_table_new(), and \_dbus_hash_table_unref().

## ◆ down_shift

|                               |
|-------------------------------|
| int DBusHashTable::down_shift |

Shift count used in hashing function.

Designed to use high- order bits of randomized keys.

Definition at line 198 of file dbus-hash.c.

Referenced by \_dbus_hash_table_new().

## ◆ entry_pool

|                                         |
|-----------------------------------------|
| DBusMemPool\* DBusHashTable::entry_pool |

Memory pool for hash entries.

Definition at line 213 of file dbus-hash.c.

Referenced by \_dbus_hash_table_free_preallocated_entry(), \_dbus_hash_table_new(), and \_dbus_hash_table_unref().

## ◆ find_function

|                                                    |
|----------------------------------------------------|
| DBusFindEntryFunction DBusHashTable::find_function |

Function for finding entries.

Definition at line 208 of file dbus-hash.c.

Referenced by \_dbus_hash_iter_lookup(), \_dbus_hash_table_insert_int(), \_dbus_hash_table_insert_string_preallocated(), \_dbus_hash_table_insert_uintptr(), \_dbus_hash_table_lookup_int(), \_dbus_hash_table_lookup_string(), \_dbus_hash_table_lookup_uintptr(), \_dbus_hash_table_new(), \_dbus_hash_table_remove_int(), \_dbus_hash_table_remove_string(), and \_dbus_hash_table_remove_uintptr().

## ◆ free_key_function

|                                                   |
|---------------------------------------------------|
| DBusFreeFunction DBusHashTable::free_key_function |

Function to free keys.

Definition at line 210 of file dbus-hash.c.

Referenced by \_dbus_hash_iter_lookup(), \_dbus_hash_table_insert_int(), \_dbus_hash_table_insert_string_preallocated(), \_dbus_hash_table_insert_uintptr(), and \_dbus_hash_table_new().

## ◆ free_value_function

|                                                     |
|-----------------------------------------------------|
| DBusFreeFunction DBusHashTable::free_value_function |

Function to free values.

Definition at line 211 of file dbus-hash.c.

Referenced by \_dbus_hash_iter_set_value(), \_dbus_hash_table_insert_int(), \_dbus_hash_table_insert_string_preallocated(), \_dbus_hash_table_insert_uintptr(), and \_dbus_hash_table_new().

## ◆ hi_rebuild_size

|                                    |
|------------------------------------|
| int DBusHashTable::hi_rebuild_size |

Enlarge table when n_entries gets to be this large.

Definition at line 192 of file dbus-hash.c.

Referenced by \_dbus_hash_table_new().

## ◆ key_type

|                                      |
|--------------------------------------|
| DBusHashType DBusHashTable::key_type |

Type of keys used in this table.

Definition at line 205 of file dbus-hash.c.

Referenced by \_dbus_hash_table_insert_int(), \_dbus_hash_table_insert_string(), \_dbus_hash_table_insert_string_preallocated(), \_dbus_hash_table_insert_uintptr(), \_dbus_hash_table_lookup_int(), \_dbus_hash_table_lookup_string(), \_dbus_hash_table_lookup_uintptr(), \_dbus_hash_table_new(), \_dbus_hash_table_remove_int(), \_dbus_hash_table_remove_string(), and \_dbus_hash_table_remove_uintptr().

## ◆ lo_rebuild_size

|                                    |
|------------------------------------|
| int DBusHashTable::lo_rebuild_size |

Shrink table when n_entries gets below this.

Definition at line 195 of file dbus-hash.c.

Referenced by \_dbus_hash_table_new().

## ◆ mask

|                         |
|-------------------------|
| int DBusHashTable::mask |

Mask value used in hashing function.

Definition at line 202 of file dbus-hash.c.

Referenced by \_dbus_hash_table_new().

## ◆ n_buckets

|                              |
|------------------------------|
| int DBusHashTable::n_buckets |

Total number of buckets allocated at \*\*buckets.

Definition at line 186 of file dbus-hash.c.

Referenced by \_dbus_hash_iter_lookup(), \_dbus_hash_iter_next(), \_dbus_hash_table_new(), and \_dbus_hash_table_unref().

## ◆ n_entries

|                              |
|------------------------------|
| int DBusHashTable::n_entries |

Total number of entries present in table.

Definition at line 189 of file dbus-hash.c.

Referenced by \_dbus_hash_iter_init(), \_dbus_hash_iter_lookup(), \_dbus_hash_iter_next(), \_dbus_hash_table_get_n_entries(), and \_dbus_hash_table_new().

## ◆ refcount

|                             |
|-----------------------------|
| int DBusHashTable::refcount |

Reference count.

Definition at line 176 of file dbus-hash.c.

Referenced by \_dbus_hash_table_new(), \_dbus_hash_table_ref(), and \_dbus_hash_table_unref().

## ◆ static_buckets

|                                                                        |
|------------------------------------------------------------------------|
| DBusHashEntry\* DBusHashTable::static_buckets\[DBUS_SMALL_HASH_TABLE\] |

Bucket array used for small tables (to avoid mallocs and frees).

Definition at line 182 of file dbus-hash.c.

Referenced by \_dbus_hash_table_new(), and \_dbus_hash_table_unref().

The documentation for this struct was generated from the following file:

- dbus-hash.c
