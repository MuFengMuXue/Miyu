Hash table

D-Bus secret internal implementation details

DBusHashTable data structure. More...

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
<td class="memItemRight" data-valign="bottom">DBusHashIter</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Hash iterator object. More...<br />
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
<tr id="r_ga81d2f0358c7a2430fcc12640bcd46cb1" class="memitem:ga81d2f0358c7a2430fcc12640bcd46cb1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_HASH_POLLABLE   DBUS_HASH_INT</td>
</tr>
<tr class="separator:ga81d2f0358c7a2430fcc12640bcd46cb1">
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
<tr id="r_ga5c3932408f662678562bee5f5c7b4e31" class="memitem:ga5c3932408f662678562bee5f5c7b4e31">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef int(* </td>
<td class="memItemRight" data-valign="bottom">KeyCompareFunc) (const void *key_a, const void *key_b)</td>
</tr>
<tr class="memdesc:ga5c3932408f662678562bee5f5c7b4e31">
<td class="mdescLeft"> </td>
<td class="mdescRight">Key comparison function.<br />
</td>
</tr>
<tr class="separator:ga5c3932408f662678562bee5f5c7b4e31">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae11437504d2f1ec62272264214968988" class="memitem:gae11437504d2f1ec62272264214968988">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusHashTable </td>
<td class="memItemRight" data-valign="bottom">DBusHashTable</td>
</tr>
<tr class="memdesc:gae11437504d2f1ec62272264214968988">
<td class="mdescLeft"> </td>
<td class="mdescRight">Public opaque hash table object.<br />
</td>
</tr>
<tr class="separator:gae11437504d2f1ec62272264214968988">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae8ee983d1bea5d9c49dab9714bc91a68" class="memitem:gae8ee983d1bea5d9c49dab9714bc91a68">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusHashIter </td>
<td class="memItemRight" data-valign="bottom">DBusHashIter</td>
</tr>
<tr class="memdesc:gae8ee983d1bea5d9c49dab9714bc91a68">
<td class="mdescLeft"> </td>
<td class="mdescRight">Public opaque hash table iterator object.<br />
</td>
</tr>
<tr class="separator:gae8ee983d1bea5d9c49dab9714bc91a68">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga175dc6ab841ed32bb6acf6e4c0df36a8" class="memitem:ga175dc6ab841ed32bb6acf6e4c0df36a8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusPreallocatedHash </td>
<td class="memItemRight" data-valign="bottom">DBusPreallocatedHash</td>
</tr>
<tr class="memdesc:ga175dc6ab841ed32bb6acf6e4c0df36a8">
<td class="mdescLeft"> </td>
<td class="mdescRight">A preallocated hash entry.<br />
</td>
</tr>
<tr class="separator:ga175dc6ab841ed32bb6acf6e4c0df36a8">
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
<tr id="r_gab0ab9767ffa5b6720a13b3d741630852" class="memitem:gab0ab9767ffa5b6720a13b3d741630852">
<td class="memItemLeft" style="text-align: right;" data-valign="top">enum  </td>
<td class="memItemRight" data-valign="bottom">DBusHashType { DBUS_HASH_STRING , DBUS_HASH_INT , DBUS_HASH_UINTPTR }</td>
</tr>
<tr class="memdesc:gab0ab9767ffa5b6720a13b3d741630852">
<td class="mdescLeft"> </td>
<td class="mdescRight">Indicates the type of a key in the hash table. More...<br />
</td>
</tr>
<tr class="separator:gab0ab9767ffa5b6720a13b3d741630852">
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
<td colspan="2"><h2 id="functions" class="groupheader"> Functions</h2></td>
</tr>
<tr id="r_ga7aa7b6054c5fbf8852bad79d372580dd" class="memitem:ga7aa7b6054c5fbf8852bad79d372580dd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusHashTable * </td>
<td class="memItemRight" data-valign="bottom">_dbus_hash_table_new (DBusHashType type, DBusFreeFunction key_free_function, DBusFreeFunction value_free_function)</td>
</tr>
<tr class="memdesc:ga7aa7b6054c5fbf8852bad79d372580dd">
<td class="mdescLeft"> </td>
<td class="mdescRight">Constructs a new hash table.<br />
</td>
</tr>
<tr class="separator:ga7aa7b6054c5fbf8852bad79d372580dd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0839248434c1aeda49e6495134bcded1" class="memitem:ga0839248434c1aeda49e6495134bcded1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusHashTable * </td>
<td class="memItemRight" data-valign="bottom">_dbus_hash_table_ref (DBusHashTable *table)</td>
</tr>
<tr class="memdesc:ga0839248434c1aeda49e6495134bcded1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Increments the reference count for a hash table.<br />
</td>
</tr>
<tr class="separator:ga0839248434c1aeda49e6495134bcded1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5ba600e4a4ea0dac1ab3f2bbf9e1665e" class="memitem:ga5ba600e4a4ea0dac1ab3f2bbf9e1665e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_hash_table_unref (DBusHashTable *table)</td>
</tr>
<tr class="memdesc:ga5ba600e4a4ea0dac1ab3f2bbf9e1665e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Decrements the reference count for a hash table, freeing the hash table if the count reaches zero.<br />
</td>
</tr>
<tr class="separator:ga5ba600e4a4ea0dac1ab3f2bbf9e1665e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad169f3790ca67f8a0adafcdc88ef7188" class="memitem:gad169f3790ca67f8a0adafcdc88ef7188">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_hash_table_remove_all (DBusHashTable *table)</td>
</tr>
<tr class="memdesc:gad169f3790ca67f8a0adafcdc88ef7188">
<td class="mdescLeft"> </td>
<td class="mdescRight">Removed all entries from a hash table.<br />
</td>
</tr>
<tr class="separator:gad169f3790ca67f8a0adafcdc88ef7188">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7572541c8385e86824db78459621bbc7" class="memitem:ga7572541c8385e86824db78459621bbc7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_hash_iter_init (DBusHashTable *table, DBusHashIter *iter)</td>
</tr>
<tr class="memdesc:ga7572541c8385e86824db78459621bbc7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initializes a hash table iterator.<br />
</td>
</tr>
<tr class="separator:ga7572541c8385e86824db78459621bbc7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga64bdce3eb1c543dfb162faada65f4b78" class="memitem:ga64bdce3eb1c543dfb162faada65f4b78">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_hash_iter_next (DBusHashIter *iter)</td>
</tr>
<tr class="memdesc:ga64bdce3eb1c543dfb162faada65f4b78">
<td class="mdescLeft"> </td>
<td class="mdescRight">Move the hash iterator forward one step, to the next hash entry.<br />
</td>
</tr>
<tr class="separator:ga64bdce3eb1c543dfb162faada65f4b78">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf189e7e9933cb0326b7e2c7b9a3a03b5" class="memitem:gaf189e7e9933cb0326b7e2c7b9a3a03b5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_hash_iter_remove_entry (DBusHashIter *iter)</td>
</tr>
<tr class="memdesc:gaf189e7e9933cb0326b7e2c7b9a3a03b5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Removes the current entry from the hash table.<br />
</td>
</tr>
<tr class="separator:gaf189e7e9933cb0326b7e2c7b9a3a03b5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0b774bd61c68c0e9d53ea9f187595e6b" class="memitem:ga0b774bd61c68c0e9d53ea9f187595e6b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">_dbus_hash_iter_get_value (DBusHashIter *iter)</td>
</tr>
<tr class="memdesc:ga0b774bd61c68c0e9d53ea9f187595e6b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the value of the current entry.<br />
</td>
</tr>
<tr class="separator:ga0b774bd61c68c0e9d53ea9f187595e6b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa9abeaca1aed3a1a8eaba55f6af0c818" class="memitem:gaa9abeaca1aed3a1a8eaba55f6af0c818">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_hash_iter_set_value (DBusHashIter *iter, void *value)</td>
</tr>
<tr class="memdesc:gaa9abeaca1aed3a1a8eaba55f6af0c818">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the value of the current entry.<br />
</td>
</tr>
<tr class="separator:gaa9abeaca1aed3a1a8eaba55f6af0c818">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga747442b12362dab8efab975f6c595266" class="memitem:ga747442b12362dab8efab975f6c595266">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_hash_iter_get_int_key (DBusHashIter *iter)</td>
</tr>
<tr class="memdesc:ga747442b12362dab8efab975f6c595266">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the key for the current entry.<br />
</td>
</tr>
<tr class="separator:ga747442b12362dab8efab975f6c595266">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4df55654e028b405994d2e4d64107a27" class="memitem:ga4df55654e028b405994d2e4d64107a27">
<td class="memItemLeft" style="text-align: right;" data-valign="top">uintptr_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_hash_iter_get_uintptr_key (DBusHashIter *iter)</td>
</tr>
<tr class="memdesc:ga4df55654e028b405994d2e4d64107a27">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the key for the current entry.<br />
</td>
</tr>
<tr class="separator:ga4df55654e028b405994d2e4d64107a27">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gadc314f126076580dae3bd4f7f83824ca" class="memitem:gadc314f126076580dae3bd4f7f83824ca">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">_dbus_hash_iter_get_string_key (DBusHashIter *iter)</td>
</tr>
<tr class="memdesc:gadc314f126076580dae3bd4f7f83824ca">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the key for the current entry.<br />
</td>
</tr>
<tr class="separator:gadc314f126076580dae3bd4f7f83824ca">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad109be9d42f1c29385a44d368b89d889" class="memitem:gad109be9d42f1c29385a44d368b89d889">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_hash_iter_lookup (DBusHashTable *table, void *key, dbus_bool_t create_if_not_found, DBusHashIter *iter)</td>
</tr>
<tr class="memdesc:gad109be9d42f1c29385a44d368b89d889">
<td class="mdescLeft"> </td>
<td class="mdescRight">A low-level but efficient interface for manipulating the hash table.<br />
</td>
</tr>
<tr class="separator:gad109be9d42f1c29385a44d368b89d889">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gacfadc6796f8652a5b66333800b019d30" class="memitem:gacfadc6796f8652a5b66333800b019d30">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">_dbus_hash_table_lookup_string (DBusHashTable *table, const char *key)</td>
</tr>
<tr class="memdesc:gacfadc6796f8652a5b66333800b019d30">
<td class="mdescLeft"> </td>
<td class="mdescRight">Looks up the value for a given string in a hash table of type DBUS_HASH_STRING.<br />
</td>
</tr>
<tr class="separator:gacfadc6796f8652a5b66333800b019d30">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gafdd731ccadca43757061f9486ca8c216" class="memitem:gafdd731ccadca43757061f9486ca8c216">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">_dbus_hash_table_lookup_int (DBusHashTable *table, int key)</td>
</tr>
<tr class="memdesc:gafdd731ccadca43757061f9486ca8c216">
<td class="mdescLeft"> </td>
<td class="mdescRight">Looks up the value for a given integer in a hash table of type DBUS_HASH_INT.<br />
</td>
</tr>
<tr class="separator:gafdd731ccadca43757061f9486ca8c216">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5ad1c4ccc1405b449d22b69d70b67860" class="memitem:ga5ad1c4ccc1405b449d22b69d70b67860">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">_dbus_hash_table_lookup_uintptr (DBusHashTable *table, uintptr_t key)</td>
</tr>
<tr class="memdesc:ga5ad1c4ccc1405b449d22b69d70b67860">
<td class="mdescLeft"> </td>
<td class="mdescRight">Looks up the value for a given integer in a hash table of type DBUS_HASH_UINTPTR.<br />
</td>
</tr>
<tr class="separator:ga5ad1c4ccc1405b449d22b69d70b67860">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga96ef91a7d982e77ef17a42be6acc177b" class="memitem:ga96ef91a7d982e77ef17a42be6acc177b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_hash_table_remove_string (DBusHashTable *table, const char *key)</td>
</tr>
<tr class="memdesc:ga96ef91a7d982e77ef17a42be6acc177b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Removes the hash entry for the given key.<br />
</td>
</tr>
<tr class="separator:ga96ef91a7d982e77ef17a42be6acc177b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8b9306c318909ec6a36459b9de6a77cb" class="memitem:ga8b9306c318909ec6a36459b9de6a77cb">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_hash_table_remove_int (DBusHashTable *table, int key)</td>
</tr>
<tr class="memdesc:ga8b9306c318909ec6a36459b9de6a77cb">
<td class="mdescLeft"> </td>
<td class="mdescRight">Removes the hash entry for the given key.<br />
</td>
</tr>
<tr class="separator:ga8b9306c318909ec6a36459b9de6a77cb">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0854d0a66204f075f5a1a9f7dbca799a" class="memitem:ga0854d0a66204f075f5a1a9f7dbca799a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_hash_table_remove_uintptr (DBusHashTable *table, uintptr_t key)</td>
</tr>
<tr class="memdesc:ga0854d0a66204f075f5a1a9f7dbca799a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Removes the hash entry for the given key.<br />
</td>
</tr>
<tr class="separator:ga0854d0a66204f075f5a1a9f7dbca799a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2b38eb4cc88efa57435a66f70331b0b4" class="memitem:ga2b38eb4cc88efa57435a66f70331b0b4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_hash_table_insert_string (DBusHashTable *table, char *key, void *value)</td>
</tr>
<tr class="memdesc:ga2b38eb4cc88efa57435a66f70331b0b4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a hash entry with the given key and value.<br />
</td>
</tr>
<tr class="separator:ga2b38eb4cc88efa57435a66f70331b0b4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2065297d8e8e3590d2235acf7f00a6d2" class="memitem:ga2065297d8e8e3590d2235acf7f00a6d2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_hash_table_insert_int (DBusHashTable *table, int key, void *value)</td>
</tr>
<tr class="memdesc:ga2065297d8e8e3590d2235acf7f00a6d2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a hash entry with the given key and value.<br />
</td>
</tr>
<tr class="separator:ga2065297d8e8e3590d2235acf7f00a6d2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaed7365623dcb72434f890feed28e9e42" class="memitem:gaed7365623dcb72434f890feed28e9e42">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_hash_table_insert_uintptr (DBusHashTable *table, uintptr_t key, void *value)</td>
</tr>
<tr class="memdesc:gaed7365623dcb72434f890feed28e9e42">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a hash entry with the given key and value.<br />
</td>
</tr>
<tr class="separator:gaed7365623dcb72434f890feed28e9e42">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8bc6ac0897eff9ef72b7616a89a79b49" class="memitem:ga8bc6ac0897eff9ef72b7616a89a79b49">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusPreallocatedHash * </td>
<td class="memItemRight" data-valign="bottom">_dbus_hash_table_preallocate_entry (DBusHashTable *table)</td>
</tr>
<tr class="memdesc:ga8bc6ac0897eff9ef72b7616a89a79b49">
<td class="mdescLeft"> </td>
<td class="mdescRight">Preallocate an opaque data blob that allows us to insert into the hash table at a later time without allocating any memory.<br />
</td>
</tr>
<tr class="separator:ga8bc6ac0897eff9ef72b7616a89a79b49">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga762aa8cbc471e727036b3ace47cf213b" class="memitem:ga762aa8cbc471e727036b3ace47cf213b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_hash_table_free_preallocated_entry (DBusHashTable *table, DBusPreallocatedHash *preallocated)</td>
</tr>
<tr class="memdesc:ga762aa8cbc471e727036b3ace47cf213b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Frees an opaque DBusPreallocatedHash that was <em>not</em> used in order to insert into the hash table.<br />
</td>
</tr>
<tr class="separator:ga762aa8cbc471e727036b3ace47cf213b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf1cba5e6765de02d2ee29acae72b985b" class="memitem:gaf1cba5e6765de02d2ee29acae72b985b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_hash_table_insert_string_preallocated (DBusHashTable *table, DBusPreallocatedHash *preallocated, char *key, void *value)</td>
</tr>
<tr class="memdesc:gaf1cba5e6765de02d2ee29acae72b985b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Inserts a string-keyed entry into the hash table, using a preallocated data block from _dbus_hash_table_preallocate_entry().<br />
</td>
</tr>
<tr class="separator:gaf1cba5e6765de02d2ee29acae72b985b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga06555357f633c4020bbb5b78f701b39d" class="memitem:ga06555357f633c4020bbb5b78f701b39d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_hash_table_get_n_entries (DBusHashTable *table)</td>
</tr>
<tr class="memdesc:ga06555357f633c4020bbb5b78f701b39d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the number of hash entries in a hash table.<br />
</td>
</tr>
<tr class="separator:ga06555357f633c4020bbb5b78f701b39d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3a515d729ae2f59db5841d04111fc032" class="memitem:ga3a515d729ae2f59db5841d04111fc032">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_hash_table_from_array (DBusHashTable *table, char **array, char delimiter)</td>
</tr>
<tr class="memdesc:ga3a515d729ae2f59db5841d04111fc032">
<td class="mdescLeft"> </td>
<td class="mdescRight">Imports a string array into a hash table The hash table needs to be initialized with string keys, and dbus_free() as both key and value free-function.<br />
</td>
</tr>
<tr class="separator:ga3a515d729ae2f59db5841d04111fc032">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9f5972b3dac3a40876e9be4492f81adc" class="memitem:ga9f5972b3dac3a40876e9be4492f81adc">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char ** </td>
<td class="memItemRight" data-valign="bottom">_dbus_hash_table_to_array (DBusHashTable *table, char delimiter)</td>
</tr>
<tr class="memdesc:ga9f5972b3dac3a40876e9be4492f81adc">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a string array from a hash table.<br />
</td>
</tr>
<tr class="separator:ga9f5972b3dac3a40876e9be4492f81adc">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

DBusHashTable data structure.

Types and functions related to DBusHashTable.

## Macro Definition Documentation

## ◆ DBUS_HASH_POLLABLE

|                                             |
|---------------------------------------------|
| \#define DBUS_HASH_POLLABLE   DBUS_HASH_INT |

Definition at line 166 of file dbus-hash.h.

## Typedef Documentation

## ◆ DBusHashIter

|              |
|--------------|
| DBusHashIter |

Public opaque hash table iterator object.

Definition at line 60 of file dbus-hash.h.

## ◆ DBusHashTable

|               |
|---------------|
| DBusHashTable |

Public opaque hash table object.

Definition at line 59 of file dbus-hash.h.

## ◆ DBusPreallocatedHash

|                                                          |
|----------------------------------------------------------|
| typedef struct DBusPreallocatedHash DBusPreallocatedHash |

A preallocated hash entry.

Definition at line 150 of file dbus-hash.h.

## ◆ KeyCompareFunc

|                                                                         |
|-------------------------------------------------------------------------|
| typedef int(\* KeyCompareFunc) (const void \*key_a, const void \*key_b) |

Key comparison function.

Definition at line 895 of file dbus-hash.c.

## Enumeration Type Documentation

## ◆ DBusHashType

|                   |
|-------------------|
| enum DBusHashType |

Indicates the type of a key in the hash table.

| Enumerator         |                                                  |
|--------------------|--------------------------------------------------|
| DBUS_HASH_STRING   | Hash keys are strings.                           |
| DBUS_HASH_INT      | Hash keys are integers.                          |
| DBUS_HASH_UINTPTR  | Hash keys are integer capable to hold a pointer. |

Definition at line 67 of file dbus-hash.h.

## Function Documentation

## ◆ \_dbus_hash_iter_get_int_key()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT int \_dbus_hash_iter_get_int_key | ( | DBusHashIter \*  | *iter* | ) |  |

Gets the key for the current entry.

Only works for hash tables of type DBUS_HASH_INT.

Parameters  
|      |                          |
|------|--------------------------|
| iter | the hash table iterator. |

Definition at line 666 of file dbus-hash.c.

References \_dbus_assert, \_DBUS_POINTER_TO_INT, DBusRealHashIter::entry, DBusHashEntry::key, NULL, and DBusRealHashIter::table.

## ◆ \_dbus_hash_iter_get_string_key()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT const char \* \_dbus_hash_iter_get_string_key | ( | DBusHashIter \*  | *iter* | ) |  |

Gets the key for the current entry.

Only works for hash tables of type DBUS_HASH_STRING

Parameters  
|      |                          |
|------|--------------------------|
| iter | the hash table iterator. |

Definition at line 703 of file dbus-hash.c.

References \_dbus_assert, DBusRealHashIter::entry, DBusHashEntry::key, NULL, and DBusRealHashIter::table.

Referenced by \_dbus_hash_table_to_array().

## ◆ \_dbus_hash_iter_get_uintptr_key()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT uintptr_t \_dbus_hash_iter_get_uintptr_key | ( | DBusHashIter \*  | *iter* | ) |  |

Gets the key for the current entry.

Only works for hash tables of type DBUS_HASH_UINTPTR.

Parameters  
|      |                          |
|------|--------------------------|
| iter | the hash table iterator. |

Definition at line 685 of file dbus-hash.c.

References \_dbus_assert, DBusRealHashIter::entry, DBusHashEntry::key, NULL, and DBusRealHashIter::table.

## ◆ \_dbus_hash_iter_get_value()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT void \* \_dbus_hash_iter_get_value | ( | DBusHashIter \*  | *iter* | ) |  |

Gets the value of the current entry.

Parameters  
|      |                          |
|------|--------------------------|
| iter | the hash table iterator. |

Definition at line 620 of file dbus-hash.c.

References \_dbus_assert, DBusRealHashIter::entry, NULL, DBusRealHashIter::table, and DBusHashEntry::value.

Referenced by \_dbus_hash_table_to_array().

## ◆ \_dbus_hash_iter_init()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT void \_dbus_hash_iter_init | ( | DBusHashTable \*  | *table*, |
|  |  | DBusHashIter \*  | *iter*  |
|  | ) |  |  |

Initializes a hash table iterator.

To iterate over all entries in a hash table, use the following code (the printf assumes a hash from strings to strings obviously):

DBusHashIter iter;

\_dbus_hash_iter_init (table, &iter);

while (\_dbus_hash_iter_next (&iter))

{

printf ("The first key is %s and value is %s\n",

\_dbus_hash_iter_get_string_key (&iter),

\_dbus_hash_iter_get_value (&iter));

}

\_dbus_hash_iter_get_value

void \* \_dbus_hash_iter_get_value(DBusHashIter \*iter)

Gets the value of the current entry.

**Definition** dbus-hash.c:620

\_dbus_hash_iter_next

dbus_bool_t \_dbus_hash_iter_next(DBusHashIter \*iter)

Move the hash iterator forward one step, to the next hash entry.

**Definition** dbus-hash.c:550

\_dbus_hash_iter_init

void \_dbus_hash_iter_init(DBusHashTable \*table, DBusHashIter \*iter)

Initializes a hash table iterator.

**Definition** dbus-hash.c:524

\_dbus_hash_iter_get_string_key

const char \* \_dbus_hash_iter_get_string_key(DBusHashIter \*iter)

Gets the key for the current entry.

**Definition** dbus-hash.c:703

DBusHashIter

Hash iterator object.

**Definition** dbus-hash.h:50

The iterator is initialized pointing "one before" the first hash entry. The first call to \_dbus_hash_iter_next() moves it onto the first valid entry or returns FALSE if the hash table is empty. Subsequent calls move to the next valid entry or return FALSE if there are no more entries.

Note that it is guaranteed to be safe to remove a hash entry during iteration, but it is not safe to add a hash entry.

Parameters  
|       |                                 |
|-------|---------------------------------|
| table | the hash table to iterate over. |
| iter  | the iterator to initialize.     |

Definition at line 524 of file dbus-hash.c.

References DBusRealHashIter::bucket, DBusRealHashIter::entry, n_entries, DBusRealHashIter::n_entries_on_init, DBusRealHashIter::next_bucket, DBusRealHashIter::next_entry, NULL, and DBusRealHashIter::table.

Referenced by \_dbus_hash_table_remove_all(), and \_dbus_hash_table_to_array().

## ◆ \_dbus_hash_iter_lookup()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_hash_iter_lookup | ( | DBusHashTable \*  | *table*, |
|  |  | void \*  | *key*, |
|  |  | dbus_bool_t  | *create_if_not_found*, |
|  |  | DBusHashIter \*  | *iter*  |
|  | ) |  |  |

A low-level but efficient interface for manipulating the hash table.

It's efficient because you can get, set, and optionally create the hash entry while only running the hash function one time.

Note that while calling \_dbus_hash_iter_next() on the iterator filled in by this function may work, it's completely undefined which entries are after this iter and which are before it. So it would be silly to iterate using this iterator.

If the hash entry is created, its value will be initialized to all bits zero.

FALSE may be returned due to memory allocation failure, or because create_if_not_found was FALSE and the entry did not exist.

If create_if_not_found is TRUE, the hash table takes ownership of the key that's passed in (either using it to create the entry, or freeing it immediately).

For a hash table of type DBUS_HASH_INT, cast the int key to the key parameter using \_DBUS_INT_TO_POINTER().

Parameters  
|                     |                                               |
|---------------------|-----------------------------------------------|
| table               | the hash table.                               |
| key                 | the hash key.                                 |
| create_if_not_found | if TRUE, create the entry if it didn't exist. |
| iter                | the iterator to initialize.                   |

<!-- -->

Returns  
TRUE if the hash entry now exists (and the iterator is thus valid).

Definition at line 748 of file dbus-hash.c.

References \_dbus_assert, DBusRealHashIter::bucket, buckets, DBusRealHashIter::entry, FALSE, find_function, free_key_function, DBusHashEntry::key, n_buckets, n_entries, DBusRealHashIter::n_entries_on_init, DBusHashEntry::next, DBusRealHashIter::next_bucket, DBusRealHashIter::next_entry, NULL, DBusRealHashIter::table, and TRUE.

## ◆ \_dbus_hash_iter_next()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_hash_iter_next | ( | DBusHashIter \*  | *iter* | ) |  |

Move the hash iterator forward one step, to the next hash entry.

The documentation for \_dbus_hash_iter_init() explains in more detail.

Parameters  
|      |                               |
|------|-------------------------------|
| iter | the iterator to move forward. |

<!-- -->

Returns  
FALSE if there are no more entries to move to.

Definition at line 550 of file dbus-hash.c.

References \_dbus_assert, DBusRealHashIter::bucket, buckets, DBusRealHashIter::entry, FALSE, n_buckets, n_entries, DBusRealHashIter::n_entries_on_init, DBusHashEntry::next, DBusRealHashIter::next_bucket, DBusRealHashIter::next_entry, NULL, DBusRealHashIter::table, and TRUE.

Referenced by \_dbus_hash_table_remove_all(), and \_dbus_hash_table_to_array().

## ◆ \_dbus_hash_iter_remove_entry()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT void \_dbus_hash_iter_remove_entry | ( | DBusHashIter \*  | *iter* | ) |  |

Removes the current entry from the hash table.

If a key_free_function or value_free_function was provided to \_dbus_hash_table_new(), frees the key and/or value for this entry.

Parameters  
|      |                          |
|------|--------------------------|
| iter | the hash table iterator. |

Definition at line 599 of file dbus-hash.c.

References \_dbus_assert, DBusRealHashIter::bucket, DBusRealHashIter::entry, NULL, and DBusRealHashIter::table.

Referenced by \_dbus_hash_table_remove_all().

## ◆ \_dbus_hash_iter_set_value()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT void \_dbus_hash_iter_set_value | ( | DBusHashIter \*  | *iter*, |
|  |  | void \*  | *value*  |
|  | ) |  |  |

Sets the value of the current entry.

If the hash table has a value_free_function it will be used to free the previous value. The hash table will own the passed-in value (it will not be copied).

Parameters  
|       |                          |
|-------|--------------------------|
| iter  | the hash table iterator. |
| value | the new value.           |

Definition at line 643 of file dbus-hash.c.

References \_dbus_assert, DBusRealHashIter::entry, free_value_function, NULL, DBusRealHashIter::table, and DBusHashEntry::value.

## ◆ \_dbus_hash_table_free_preallocated_entry()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT void \_dbus_hash_table_free_preallocated_entry | ( | DBusHashTable \*  | *table*, |
|  |  | DBusPreallocatedHash \*  | *preallocated*  |
|  | ) |  |  |

Frees an opaque DBusPreallocatedHash that was *not* used in order to insert into the hash table.

Parameters  
|              |                       |
|--------------|-----------------------|
| table        | the hash table        |
| preallocated | the preallocated data |

Definition at line 1403 of file dbus-hash.c.

References \_dbus_assert, \_dbus_mem_pool_dealloc(), entry_pool, and NULL.

## ◆ \_dbus_hash_table_from_array()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_hash_table_from_array | ( | DBusHashTable \*  | *table*, |
|  |  | char \*\*  | *array*, |
|  |  | char  | *delimiter*  |
|  | ) |  |  |

Imports a string array into a hash table The hash table needs to be initialized with string keys, and dbus_free() as both key and value free-function.

Parameters  
|           |                                         |
|-----------|-----------------------------------------|
| table     | the hash table                          |
| array     | the string array to import              |
| delimiter | the delimiter to separate key and value |

<!-- -->

Returns  
TRUE on success.

FALSE if not enough memory.

Definition at line 1479 of file dbus-hash.c.

References \_dbus_assert, \_dbus_hash_table_insert_string(), \_dbus_string_append(), \_dbus_string_free(), \_dbus_string_init(), \_dbus_string_set_length(), \_dbus_string_split_on_byte(), \_dbus_string_steal_data(), FALSE, NULL, and TRUE.

## ◆ \_dbus_hash_table_get_n_entries()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT int \_dbus_hash_table_get_n_entries | ( | DBusHashTable \*  | *table* | ) |  |

Gets the number of hash entries in a hash table.

Parameters  
|       |                 |
|-------|-----------------|
| table | the hash table. |

<!-- -->

Returns  
the number of entries in the table.

Definition at line 1461 of file dbus-hash.c.

References n_entries.

Referenced by \_dbus_hash_table_to_array().

## ◆ \_dbus_hash_table_insert_int()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_hash_table_insert_int | ( | DBusHashTable \*  | *table*, |
|  |  | int  | *key*, |
|  |  | void \*  | *value*  |
|  | ) |  |  |

Creates a hash entry with the given key and value.

The key and value are not copied; they are stored in the hash table by reference. If an entry with the given key already exists, the previous key and value are overwritten (and freed if the hash table has a key_free_function and/or value_free_function).

Returns FALSE if memory for the new hash entry can't be allocated.

Parameters  
|       |                       |
|-------|-----------------------|
| table | the hash table.       |
| key   | the hash entry key.   |
| value | the hash entry value. |

Definition at line 1312 of file dbus-hash.c.

References \_dbus_assert, \_DBUS_INT_TO_POINTER, DBUS_HASH_INT, FALSE, find_function, free_key_function, free_value_function, DBusHashEntry::key, key_type, NULL, TRUE, and DBusHashEntry::value.

## ◆ \_dbus_hash_table_insert_string()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_hash_table_insert_string | ( | DBusHashTable \*  | *table*, |
|  |  | char \*  | *key*, |
|  |  | void \*  | *value*  |
|  | ) |  |  |

Creates a hash entry with the given key and value.

The key and value are not copied; they are stored in the hash table by reference. If an entry with the given key already exists, the previous key and value are overwritten (and freed if the hash table has a key_free_function and/or value_free_function).

Returns FALSE if memory for the new hash entry can't be allocated.

Parameters  
|       |                       |
|-------|-----------------------|
| table | the hash table.       |
| key   | the hash entry key.   |
| value | the hash entry value. |

Definition at line 1278 of file dbus-hash.c.

References \_dbus_assert, \_dbus_hash_table_insert_string_preallocated(), \_dbus_hash_table_preallocate_entry(), DBUS_HASH_STRING, FALSE, key_type, NULL, and TRUE.

Referenced by \_dbus_hash_table_from_array(), \_dbus_user_database_lookup(), and \_dbus_user_database_lookup_group().

## ◆ \_dbus_hash_table_insert_string_preallocated()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT void \_dbus_hash_table_insert_string_preallocated | ( | DBusHashTable \*  | *table*, |
|  |  | DBusPreallocatedHash \*  | *preallocated*, |
|  |  | char \*  | *key*, |
|  |  | void \*  | *value*  |
|  | ) |  |  |

Inserts a string-keyed entry into the hash table, using a preallocated data block from \_dbus_hash_table_preallocate_entry().

This function cannot fail due to lack of memory. The DBusPreallocatedHash object is consumed and should not be reused or freed. Otherwise this function works just like \_dbus_hash_table_insert_string().

Parameters  
|              |                       |
|--------------|-----------------------|
| table        | the hash table        |
| preallocated | the preallocated data |
| key          | the hash key          |
| value        | the value             |

Definition at line 1430 of file dbus-hash.c.

References \_dbus_assert, DBUS_HASH_STRING, find_function, free_key_function, free_value_function, DBusHashEntry::key, key_type, NULL, TRUE, and DBusHashEntry::value.

Referenced by \_dbus_hash_table_insert_string().

## ◆ \_dbus_hash_table_insert_uintptr()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_hash_table_insert_uintptr | ( | DBusHashTable \*  | *table*, |
|  |  | uintptr_t  | *key*, |
|  |  | void \*  | *value*  |
|  | ) |  |  |

Creates a hash entry with the given key and value.

The key and value are not copied; they are stored in the hash table by reference. If an entry with the given key already exists, the previous key and value are overwritten (and freed if the hash table has a key_free_function and/or value_free_function).

Returns FALSE if memory for the new hash entry can't be allocated.

Parameters  
|       |                       |
|-------|-----------------------|
| table | the hash table.       |
| key   | the hash entry key.   |
| value | the hash entry value. |

Definition at line 1353 of file dbus-hash.c.

References \_dbus_assert, DBUS_HASH_UINTPTR, FALSE, find_function, free_key_function, free_value_function, DBusHashEntry::key, key_type, NULL, TRUE, and DBusHashEntry::value.

Referenced by \_dbus_user_database_lookup(), and \_dbus_user_database_lookup_group().

## ◆ \_dbus_hash_table_lookup_int()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT void \* \_dbus_hash_table_lookup_int | ( | DBusHashTable \*  | *table*, |
|  |  | int  | *key*  |
|  | ) |  |  |

Looks up the value for a given integer in a hash table of type DBUS_HASH_INT.

Returns NULL if the value is not present. (A not-present entry is indistinguishable from an entry with a value of NULL.)

Parameters  
|       |                         |
|-------|-------------------------|
| table | the hash table.         |
| key   | the integer to look up. |

<!-- -->

Returns  
the value of the hash entry.

Definition at line 1138 of file dbus-hash.c.

References \_dbus_assert, \_DBUS_INT_TO_POINTER, DBUS_HASH_INT, FALSE, find_function, key_type, NULL, and DBusHashEntry::value.

Referenced by \_dbus_connection_queue_received_message_link(), and dbus_connection_dispatch().

## ◆ \_dbus_hash_table_lookup_string()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT void \* \_dbus_hash_table_lookup_string | ( | DBusHashTable \*  | *table*, |
|  |  | const char \*  | *key*  |
|  | ) |  |  |

Looks up the value for a given string in a hash table of type DBUS_HASH_STRING.

Returns NULL if the value is not present. (A not-present entry is indistinguishable from an entry with a value of NULL.)

Parameters  
|       |                        |
|-------|------------------------|
| table | the hash table.        |
| key   | the string to look up. |

<!-- -->

Returns  
the value of the hash entry.

Definition at line 1113 of file dbus-hash.c.

References \_dbus_assert, DBUS_HASH_STRING, FALSE, find_function, key_type, NULL, and DBusHashEntry::value.

Referenced by \_dbus_user_database_lookup(), and \_dbus_user_database_lookup_group().

## ◆ \_dbus_hash_table_lookup_uintptr()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT void \* \_dbus_hash_table_lookup_uintptr | ( | DBusHashTable \*  | *table*, |
|  |  | uintptr_t  | *key*  |
|  | ) |  |  |

Looks up the value for a given integer in a hash table of type DBUS_HASH_UINTPTR.

Returns NULL if the value is not present. (A not-present entry is indistinguishable from an entry with a value of NULL.)

Parameters  
|       |                         |
|-------|-------------------------|
| table | the hash table.         |
| key   | the integer to look up. |

<!-- -->

Returns  
the value of the hash entry.

Definition at line 1163 of file dbus-hash.c.

References \_dbus_assert, DBUS_HASH_UINTPTR, FALSE, find_function, key_type, NULL, and DBusHashEntry::value.

Referenced by \_dbus_user_database_lookup(), and \_dbus_user_database_lookup_group().

## ◆ \_dbus_hash_table_new()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT DBusHashTable \* \_dbus_hash_table_new | ( | DBusHashType  | *type*, |
|  |  | DBusFreeFunction  | *key_free_function*, |
|  |  | DBusFreeFunction  | *value_free_function*  |
|  | ) |  |  |

Constructs a new hash table.

Should be freed with \_dbus_hash_table_unref(). If memory cannot be allocated for the hash table, returns NULL.

Parameters  
|                     |                               |
|---------------------|-------------------------------|
| type                | the type of hash key to use.  |
| key_free_function   | function to free hash keys.   |
| value_free_function | function to free hash values. |

<!-- -->

Returns  
a new DBusHashTable or NULL if no memory.

Definition at line 292 of file dbus-hash.c.

References \_dbus_assert, \_dbus_assert_not_reached, \_dbus_mem_pool_new(), \_DBUS_N_ELEMENTS, buckets, dbus_free(), DBUS_HASH_INT, DBUS_HASH_STRING, DBUS_HASH_UINTPTR, dbus_new0, DBUS_SMALL_HASH_TABLE, down_shift, entry_pool, find_function, free_key_function, free_value_function, hi_rebuild_size, key_type, lo_rebuild_size, mask, n_buckets, n_entries, NULL, REBUILD_MULTIPLIER, refcount, static_buckets, and TRUE.

Referenced by \_dbus_connection_new_for_transport(), and \_dbus_user_database_new().

## ◆ \_dbus_hash_table_preallocate_entry()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT DBusPreallocatedHash \* \_dbus_hash_table_preallocate_entry | ( | DBusHashTable \*  | *table* | ) |  |

Preallocate an opaque data blob that allows us to insert into the hash table at a later time without allocating any memory.

Parameters  
|       |                |
|-------|----------------|
| table | the hash table |

<!-- -->

Returns  
the preallocated data, or NULL if no memory

Definition at line 1386 of file dbus-hash.c.

Referenced by \_dbus_hash_table_insert_string().

## ◆ \_dbus_hash_table_ref()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT DBusHashTable \* \_dbus_hash_table_ref | ( | DBusHashTable \*  | *table* | ) |  |

Increments the reference count for a hash table.

Parameters  
|       |                                       |
|-------|---------------------------------------|
| table | the hash table to add a reference to. |

<!-- -->

Returns  
the hash table.

Definition at line 354 of file dbus-hash.c.

References refcount.

## ◆ \_dbus_hash_table_remove_all()

|                                   |     |                   |         |     |     |
|-----------------------------------|-----|-------------------|---------|-----|-----|
| void \_dbus_hash_table_remove_all | (   | DBusHashTable \*  | *table* | )   |     |

Removed all entries from a hash table.

Parameters  
|       |                                            |
|-------|--------------------------------------------|
| table | the hash table to remove all entries from. |

Definition at line 425 of file dbus-hash.c.

References \_dbus_hash_iter_init(), \_dbus_hash_iter_next(), and \_dbus_hash_iter_remove_entry().

Referenced by \_dbus_user_database_flush().

## ◆ \_dbus_hash_table_remove_int()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_hash_table_remove_int | ( | DBusHashTable \*  | *table*, |
|  |  | int  | *key*  |
|  | ) |  |  |

Removes the hash entry for the given key.

If no hash entry for the key exists, does nothing.

Parameters  
|       |                 |
|-------|-----------------|
| table | the hash table. |
| key   | the hash key.   |

<!-- -->

Returns  
TRUE if the entry existed

Definition at line 1215 of file dbus-hash.c.

References \_dbus_assert, \_DBUS_INT_TO_POINTER, DBUS_HASH_INT, FALSE, find_function, key_type, NULL, and TRUE.

## ◆ \_dbus_hash_table_remove_string()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_hash_table_remove_string | ( | DBusHashTable \*  | *table*, |
|  |  | const char \*  | *key*  |
|  | ) |  |  |

Removes the hash entry for the given key.

If no hash entry for the key exists, does nothing.

Parameters  
|       |                 |
|-------|-----------------|
| table | the hash table. |
| key   | the hash key.   |

<!-- -->

Returns  
TRUE if the entry existed

Definition at line 1187 of file dbus-hash.c.

References \_dbus_assert, DBUS_HASH_STRING, FALSE, find_function, key_type, NULL, and TRUE.

## ◆ \_dbus_hash_table_remove_uintptr()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_hash_table_remove_uintptr | ( | DBusHashTable \*  | *table*, |
|  |  | uintptr_t  | *key*  |
|  | ) |  |  |

Removes the hash entry for the given key.

If no hash entry for the key exists, does nothing.

Parameters  
|       |                 |
|-------|-----------------|
| table | the hash table. |
| key   | the hash key.   |

<!-- -->

Returns  
TRUE if the entry existed

Definition at line 1243 of file dbus-hash.c.

References \_dbus_assert, DBUS_HASH_UINTPTR, FALSE, find_function, key_type, NULL, and TRUE.

Referenced by \_dbus_user_database_lookup(), and \_dbus_user_database_lookup_group().

## ◆ \_dbus_hash_table_to_array()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT char \*\* \_dbus_hash_table_to_array | ( | DBusHashTable \*  | *table*, |
|  |  | char  | *delimiter*  |
|  | ) |  |  |

Creates a string array from a hash table.

Parameters  
|           |                                     |
|-----------|-------------------------------------|
| table     | the hash table                      |
| delimiter | the delimiter to join key and value |

<!-- -->

Returns  
pointer to created string array (free with dbus_free_string_array)

FALSE if not enough memory.

Definition at line 1544 of file dbus-hash.c.

References \_dbus_assert, \_dbus_hash_iter_get_string_key(), \_dbus_hash_iter_get_value(), \_dbus_hash_iter_init(), \_dbus_hash_iter_next(), \_dbus_hash_table_get_n_entries(), \_dbus_string_append_printf(), \_dbus_string_free(), \_dbus_string_init(), \_dbus_string_steal_data(), dbus_free_string_array(), dbus_new0, and NULL.

## ◆ \_dbus_hash_table_unref()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT void \_dbus_hash_table_unref | ( | DBusHashTable \*  | *table* | ) |  |

Decrements the reference count for a hash table, freeing the hash table if the count reaches zero.

Parameters  
|       |                                            |
|-------|--------------------------------------------|
| table | the hash table to remove a reference from. |

Definition at line 368 of file dbus-hash.c.

References \_dbus_mem_pool_free(), buckets, dbus_free(), entry_pool, n_buckets, DBusHashEntry::next, NULL, refcount, and static_buckets.

Referenced by \_dbus_connection_new_for_transport(), and \_dbus_user_database_unref().
