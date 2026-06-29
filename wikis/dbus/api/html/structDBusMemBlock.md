DBusMemBlock Struct Reference

D-Bus secret internal implementation details » Memory pool implementation details

DBusMemBlock object represents a single malloc()-returned block that gets chunked up into objects in the memory pool. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a88abbae4b7e92bfab8392c2aad2dae9b" class="memitem:a88abbae4b7e92bfab8392c2aad2dae9b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMemBlock * </td>
<td class="memItemRight" data-valign="bottom">next</td>
</tr>
<tr class="memdesc:a88abbae4b7e92bfab8392c2aad2dae9b">
<td class="mdescLeft"> </td>
<td class="mdescRight">next block in the list, which is already used up; only saved so we can free all the blocks when we free the mem pool.<br />
</td>
</tr>
<tr class="separator:a88abbae4b7e92bfab8392c2aad2dae9b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a4cc37233b0d91aa09e097572206effaf" class="memitem:a4cc37233b0d91aa09e097572206effaf">
<td class="memItemLeft" style="text-align: right;" data-valign="top">size_t </td>
<td class="memItemRight" data-valign="bottom">used_so_far</td>
</tr>
<tr class="memdesc:a4cc37233b0d91aa09e097572206effaf">
<td class="mdescLeft"> </td>
<td class="mdescRight">bytes of this block already allocated as elements.<br />
</td>
</tr>
<tr class="separator:a4cc37233b0d91aa09e097572206effaf">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a64c35ab78a2559bddf9403809630db29" class="memitem:a64c35ab78a2559bddf9403809630db29">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned char </td>
<td class="memItemRight" data-valign="bottom">elements []</td>
</tr>
<tr class="memdesc:a64c35ab78a2559bddf9403809630db29">
<td class="mdescLeft"> </td>
<td class="mdescRight">the block data, actually allocated to required size<br />
</td>
</tr>
<tr class="separator:a64c35ab78a2559bddf9403809630db29">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

DBusMemBlock object represents a single malloc()-returned block that gets chunked up into objects in the memory pool.

Definition at line 80 of file dbus-mempool.c.

## Field Documentation

## ◆ elements

|                                          |
|------------------------------------------|
| unsigned char DBusMemBlock::elements\[\] |

the block data, actually allocated to required size

Definition at line 96 of file dbus-mempool.c.

Referenced by \_dbus_mem_pool_alloc(), and \_dbus_mem_pool_dealloc().

## ◆ next

|                                   |
|-----------------------------------|
| DBusMemBlock\* DBusMemBlock::next |

next block in the list, which is already used up; only saved so we can free all the blocks when we free the mem pool.

Definition at line 82 of file dbus-mempool.c.

Referenced by \_dbus_mem_pool_alloc(), \_dbus_mem_pool_dealloc(), and \_dbus_mem_pool_free().

## ◆ used_so_far

|                                  |
|----------------------------------|
| size_t DBusMemBlock::used_so_far |

bytes of this block already allocated as elements.

Definition at line 87 of file dbus-mempool.c.

Referenced by \_dbus_mem_pool_alloc().

The documentation for this struct was generated from the following file:

- dbus-mempool.c
