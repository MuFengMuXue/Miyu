Memory pool implementation details

D-Bus secret internal implementation details

DBusMemPool implementation details. More...

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
<td class="memItemRight" data-valign="bottom">DBusFreedElement</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">struct representing an element on the free list. More...<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusMemBlock</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">DBusMemBlock object represents a single malloc()-returned block that gets chunked up into objects in the memory pool. More...<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusMemPool</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Internals fields of DBusMemPool. More...<br />
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
<td colspan="2"><h2 id="typedefs" class="groupheader"> Typedefs</h2></td>
</tr>
<tr id="r_ga4210a89e140e1cccaba27cfabd254eb1" class="memitem:ga4210a89e140e1cccaba27cfabd254eb1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusFreedElement </td>
<td class="memItemRight" data-valign="bottom">DBusFreedElement</td>
</tr>
<tr class="memdesc:ga4210a89e140e1cccaba27cfabd254eb1">
<td class="mdescLeft"> </td>
<td class="mdescRight">typedef so DBusFreedElement struct can refer to itself.<br />
</td>
</tr>
<tr class="separator:ga4210a89e140e1cccaba27cfabd254eb1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gadc586003d38772dd8336c4e103844a12" class="memitem:gadc586003d38772dd8336c4e103844a12">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusMemBlock </td>
<td class="memItemRight" data-valign="bottom">DBusMemBlock</td>
</tr>
<tr class="memdesc:gadc586003d38772dd8336c4e103844a12">
<td class="mdescLeft"> </td>
<td class="mdescRight">Typedef for DBusMemBlock so the struct can recursively point to itself.<br />
</td>
</tr>
<tr class="separator:gadc586003d38772dd8336c4e103844a12">
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
<tr id="r_gaf40dbdec03c8120f04f4b6dddef612aa" class="memitem:gaf40dbdec03c8120f04f4b6dddef612aa">
<td class="memItemLeft" style="text-align: right;" data-valign="top">  </td>
<td class="memItemRight" data-valign="bottom"><strong>_DBUS_STATIC_ASSERT</strong> (_DBUS_IS_ALIGNED(sizeof(struct DBusMemBlock), _DBUS_ALIGNOF(dbus_max_align_t)))</td>
</tr>
<tr class="separator:gaf40dbdec03c8120f04f4b6dddef612aa">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga63cd5ba649822082b1a612f7ee7bf8a5" class="memitem:ga63cd5ba649822082b1a612f7ee7bf8a5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">  </td>
<td class="memItemRight" data-valign="bottom"><strong>_DBUS_STATIC_ASSERT</strong> (_DBUS_IS_ALIGNED(offsetof(struct DBusMemBlock, elements), _DBUS_ALIGNOF(dbus_max_align_t)))</td>
</tr>
<tr class="separator:ga63cd5ba649822082b1a612f7ee7bf8a5">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

DBusMemPool implementation details.

The guts of DBusMemPool.

## Typedef Documentation

## ◆ DBusFreedElement

|                                                  |
|--------------------------------------------------|
| typedef struct DBusFreedElement DBusFreedElement |

typedef so DBusFreedElement struct can refer to itself.

Definition at line 58 of file dbus-mempool.c.

## ◆ DBusMemBlock

|                                          |
|------------------------------------------|
| typedef struct DBusMemBlock DBusMemBlock |

Typedef for DBusMemBlock so the struct can recursively point to itself.

Definition at line 74 of file dbus-mempool.c.
