DBusFreedElement Struct Reference

D-Bus secret internal implementation details » Memory pool implementation details

struct representing an element on the free list. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_ac4819bebce960943155f9fbd4ab6e6c5" class="memitem:ac4819bebce960943155f9fbd4ab6e6c5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusFreedElement * </td>
<td class="memItemRight" data-valign="bottom">next</td>
</tr>
<tr class="memdesc:ac4819bebce960943155f9fbd4ab6e6c5">
<td class="mdescLeft"> </td>
<td class="mdescRight">next element of the free list<br />
</td>
</tr>
<tr class="separator:ac4819bebce960943155f9fbd4ab6e6c5">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

struct representing an element on the free list.

We just cast freed elements to this so we can make a list out of them.

Definition at line 65 of file dbus-mempool.c.

## Field Documentation

## ◆ next

|                                           |
|-------------------------------------------|
| DBusFreedElement\* DBusFreedElement::next |

next element of the free list

Definition at line 67 of file dbus-mempool.c.

Referenced by \_dbus_mem_pool_alloc(), and \_dbus_mem_pool_dealloc().

The documentation for this struct was generated from the following file:

- dbus-mempool.c
