memory pools

D-Bus secret internal implementation details

DBusMemPool object. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="functions" class="groupheader"> Functions</h2></td>
</tr>
<tr id="r_gaefe0e6db39c0b3e6d0aa6dbd244e37dc" class="memitem:gaefe0e6db39c0b3e6d0aa6dbd244e37dc">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMemPool * </td>
<td class="memItemRight" data-valign="bottom">_dbus_mem_pool_new (int element_size, dbus_bool_t zero_elements)</td>
</tr>
<tr class="memdesc:gaefe0e6db39c0b3e6d0aa6dbd244e37dc">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new memory pool, or returns NULL on failure.<br />
</td>
</tr>
<tr class="separator:gaefe0e6db39c0b3e6d0aa6dbd244e37dc">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga58e4f3def46410d5bb138a2b8f366b1a" class="memitem:ga58e4f3def46410d5bb138a2b8f366b1a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_mem_pool_free (DBusMemPool *pool)</td>
</tr>
<tr class="memdesc:ga58e4f3def46410d5bb138a2b8f366b1a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Frees a memory pool (and all elements allocated from it).<br />
</td>
</tr>
<tr class="separator:ga58e4f3def46410d5bb138a2b8f366b1a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga48dd78eb60041e8e726ca9d14f277c2f" class="memitem:ga48dd78eb60041e8e726ca9d14f277c2f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">_dbus_mem_pool_alloc (DBusMemPool *pool)</td>
</tr>
<tr class="memdesc:ga48dd78eb60041e8e726ca9d14f277c2f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Allocates an object from the memory pool.<br />
</td>
</tr>
<tr class="separator:ga48dd78eb60041e8e726ca9d14f277c2f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4e2feaefee7384ed940059e6c7b0a9d5" class="memitem:ga4e2feaefee7384ed940059e6c7b0a9d5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_mem_pool_dealloc (DBusMemPool *pool, void *element)</td>
</tr>
<tr class="memdesc:ga4e2feaefee7384ed940059e6c7b0a9d5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Deallocates an object previously created with _dbus_mem_pool_alloc().<br />
</td>
</tr>
<tr class="separator:ga4e2feaefee7384ed940059e6c7b0a9d5">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

DBusMemPool object.

Types and functions related to DBusMemPool. A memory pool is used to decrease memory fragmentation/overhead and increase speed for blocks of small uniformly-sized objects. The main point is to avoid the overhead of a malloc block for each small object, speed is secondary.

## Function Documentation

## ◆ \_dbus_mem_pool_alloc()

|                               |     |                 |        |     |     |
|-------------------------------|-----|-----------------|--------|-----|-----|
| void \* \_dbus_mem_pool_alloc | (   | DBusMemPool \*  | *pool* | )   |     |

Allocates an object from the memory pool.

The object must be freed with \_dbus_mem_pool_dealloc().

Parameters  
|      |                 |
|------|-----------------|
| pool | the memory pool |

<!-- -->

Returns  
the allocated object or NULL if no memory.

Definition at line 227 of file dbus-mempool.c.

References \_dbus_assert, \_DBUS_INT_MAX, allocated_elements, block_size, blocks, dbus_malloc(), dbus_malloc0(), element_size, DBusMemBlock::elements, free_elements, DBusFreedElement::next, DBusMemBlock::next, NULL, DBusMemBlock::used_so_far, and zero_elements.

## ◆ \_dbus_mem_pool_dealloc()

|                                     |     |                 |            |
|-------------------------------------|-----|-----------------|------------|
| dbus_bool_t \_dbus_mem_pool_dealloc | (   | DBusMemPool \*  | *pool*,    |
|                                     |     | void \*         | *element*  |
|                                     | )   |                 |            |

Deallocates an object previously created with \_dbus_mem_pool_alloc().

The previous object must have come from this same pool.

Parameters  
|         |                                |
|---------|--------------------------------|
| pool    | the memory pool                |
| element | the element earlier allocated. |

<!-- -->

Returns  
TRUE if there are no remaining allocated elements

Definition at line 366 of file dbus-mempool.c.

References \_dbus_assert, \_dbus_assert_not_reached, allocated_elements, blocks, dbus_free(), DBusMemBlock::elements, FALSE, free_elements, DBusFreedElement::next, DBusMemBlock::next, and NULL.

Referenced by \_dbus_hash_table_free_preallocated_entry().

## ◆ \_dbus_mem_pool_free()

|                           |     |                 |        |     |     |
|---------------------------|-----|-----------------|--------|-----|-----|
| void \_dbus_mem_pool_free | (   | DBusMemPool \*  | *pool* | )   |     |

Frees a memory pool (and all elements allocated from it).

Parameters  
|      |                  |
|------|------------------|
| pool | the memory pool. |

Definition at line 200 of file dbus-mempool.c.

References blocks, dbus_free(), DBusMemBlock::next, and NULL.

Referenced by \_dbus_hash_table_unref().

## ◆ \_dbus_mem_pool_new()

|                                    |     |              |                  |
|------------------------------------|-----|--------------|------------------|
| DBusMemPool \* \_dbus_mem_pool_new | (   | int          | *element_size*,  |
|                                    |     | dbus_bool_t  | *zero_elements*  |
|                                    | )   |              |                  |

Creates a new memory pool, or returns NULL on failure.

Objects in the pool must be at least sizeof(void\*) bytes each, due to the way memory pools work. To avoid creating 64 bit problems, this means at least 8 bytes on all platforms, unless you are 4 bytes on 32-bit and 8 bytes on 64-bit.

Parameters  
|               |                                             |
|---------------|---------------------------------------------|
| element_size  | size of an element allocated from the pool. |
| zero_elements | whether to zero-initialize elements         |

<!-- -->

Returns  
the new pool or NULL

Definition at line 148 of file dbus-mempool.c.

References \_dbus_assert, allocated_elements, block_size, dbus_new0, element_size, FALSE, NULL, and zero_elements.

Referenced by \_dbus_hash_table_new().
