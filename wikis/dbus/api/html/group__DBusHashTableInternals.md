Hash table implementation details

D-Bus secret internal implementation details

DBusHashTable implementation details. More...

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
<td class="memItemRight" data-valign="bottom">DBusHashEntry</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Internal representation of a hash entry. More...<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusHashTable</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Internals of DBusHashTable. More...<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusRealHashIter</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Internals of DBusHashIter. More...<br />
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
<tr id="r_ga8c6d6296d450e37074dbd8c15638b499" class="memitem:ga8c6d6296d450e37074dbd8c15638b499">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">REBUILD_MULTIPLIER   3</td>
</tr>
<tr class="memdesc:ga8c6d6296d450e37074dbd8c15638b499">
<td class="mdescLeft"> </td>
<td class="mdescRight">When there are this many entries per bucket, on average, rebuild the hash table to make it larger.<br />
</td>
</tr>
<tr class="separator:ga8c6d6296d450e37074dbd8c15638b499">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9dc8fd5a9e25bd2b229366a683ff78f9" class="memitem:ga9dc8fd5a9e25bd2b229366a683ff78f9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">RANDOM_INDEX(table, i)    (((((uintptr_t) (i))*1103515245) &gt;&gt; (table)-&gt;down_shift) &amp; (table)-&gt;mask)</td>
</tr>
<tr class="memdesc:ga9dc8fd5a9e25bd2b229366a683ff78f9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Takes a preliminary integer hash value and produces an index into a hash tables bucket list.<br />
</td>
</tr>
<tr class="separator:ga9dc8fd5a9e25bd2b229366a683ff78f9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4518324f3c3caacf5694065f4f6071d8" class="memitem:ga4518324f3c3caacf5694065f4f6071d8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_SMALL_HASH_TABLE   4</td>
</tr>
<tr class="memdesc:ga4518324f3c3caacf5694065f4f6071d8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initial number of buckets in hash table (hash table statically allocates its buckets for this size and below).<br />
</td>
</tr>
<tr class="separator:ga4518324f3c3caacf5694065f4f6071d8">
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
<tr id="r_gad7d2d7c568541eeeb86104138d64a9f3" class="memitem:gad7d2d7c568541eeeb86104138d64a9f3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusHashEntry </td>
<td class="memItemRight" data-valign="bottom">DBusHashEntry</td>
</tr>
<tr class="memdesc:gad7d2d7c568541eeeb86104138d64a9f3">
<td class="mdescLeft"> </td>
<td class="mdescRight">Typedef for DBusHashEntry.<br />
</td>
</tr>
<tr class="separator:gad7d2d7c568541eeeb86104138d64a9f3">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab56dcf62b846460fa595886ec91af0ca" class="memitem:gab56dcf62b846460fa595886ec91af0ca">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef DBusHashEntry *(* </td>
<td class="memItemRight" data-valign="bottom">DBusFindEntryFunction) (DBusHashTable *table, void *key, dbus_bool_t create_if_not_found, DBusHashEntry ***bucket, DBusPreallocatedHash *preallocated)</td>
</tr>
<tr class="memdesc:gab56dcf62b846460fa595886ec91af0ca">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function used to find and optionally create a hash entry.<br />
</td>
</tr>
<tr class="separator:gab56dcf62b846460fa595886ec91af0ca">
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
<tr id="r_gab7d4017620f34489bca6ab3117c13bfd" class="memitem:gab7d4017620f34489bca6ab3117c13bfd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">  </td>
<td class="memItemRight" data-valign="bottom"><strong>_DBUS_STATIC_ASSERT</strong> (sizeof(DBusRealHashIter)==sizeof(DBusHashIter))</td>
</tr>
<tr class="separator:gab7d4017620f34489bca6ab3117c13bfd">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

DBusHashTable implementation details.

The guts of DBusHashTable.

## Macro Definition Documentation

## ◆ DBUS_SMALL_HASH_TABLE

|                                    |
|------------------------------------|
| \#define DBUS_SMALL_HASH_TABLE   4 |

Initial number of buckets in hash table (hash table statically allocates its buckets for this size and below).

The initial mask has to be synced to this.

Definition at line 137 of file dbus-hash.c.

## ◆ RANDOM_INDEX

|  |  |  |  |
|----|----|----|----|
| \#define RANDOM_INDEX | ( |   | table, |
|  |  |   | i  |
|  | ) |  |     (((((uintptr_t) (i))\*1103515245) \>\> (table)-\>down_shift) & (table)-\>mask) |

Takes a preliminary integer hash value and produces an index into a hash tables bucket list.

The idea is to make it so that preliminary values that are arbitrarily similar will end up in different buckets. The hash function was taken from a random-number generator. (This is used to hash integers.)

The down_shift drops off the high bits of the hash index, and decreases as we increase the number of hash buckets (to keep more range in the hash index). The mask also strips high bits and strips fewer high bits as the number of hash buckets increases. I don't understand two things: why is the initial downshift 28 to keep 4 bits when the initial mask is 011 to keep 2 bits, and why do we have both a mask and a downshift?

Definition at line 129 of file dbus-hash.c.

## ◆ REBUILD_MULTIPLIER

|                                 |
|---------------------------------|
| \#define REBUILD_MULTIPLIER   3 |

When there are this many entries per bucket, on average, rebuild the hash table to make it larger.

Definition at line 111 of file dbus-hash.c.

## Typedef Documentation

## ◆ DBusFindEntryFunction

|  |
|----|
| typedef DBusHashEntry \*(\* DBusFindEntryFunction) (DBusHashTable \*table, void \*key, dbus_bool_t create_if_not_found, DBusHashEntry \*\*\*bucket, DBusPreallocatedHash \*preallocated) |

Function used to find and optionally create a hash entry.

Definition at line 163 of file dbus-hash.c.

## ◆ DBusHashEntry

|                                            |
|--------------------------------------------|
| typedef struct DBusHashEntry DBusHashEntry |

Typedef for DBusHashEntry.

Definition at line 142 of file dbus-hash.c.
