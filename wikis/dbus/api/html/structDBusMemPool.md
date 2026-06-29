DBusMemPool Struct Reference

D-Bus secret internal implementation details » Memory pool implementation details

Internals fields of DBusMemPool. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a4b30a8b4de08e7f3e314f0334208c7fa" class="memitem:a4b30a8b4de08e7f3e314f0334208c7fa">
<td class="memItemLeft" style="text-align: right;" data-valign="top">size_t </td>
<td class="memItemRight" data-valign="bottom">element_size</td>
</tr>
<tr class="memdesc:a4b30a8b4de08e7f3e314f0334208c7fa">
<td class="mdescLeft"> </td>
<td class="mdescRight">size of a single object in the pool<br />
</td>
</tr>
<tr class="separator:a4b30a8b4de08e7f3e314f0334208c7fa">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a358b5e7dec353e606d18f93ef74b94cf" class="memitem:a358b5e7dec353e606d18f93ef74b94cf">
<td class="memItemLeft" style="text-align: right;" data-valign="top">size_t </td>
<td class="memItemRight" data-valign="bottom">block_size</td>
</tr>
<tr class="memdesc:a358b5e7dec353e606d18f93ef74b94cf">
<td class="mdescLeft"> </td>
<td class="mdescRight">size of most recently allocated block<br />
</td>
</tr>
<tr class="separator:a358b5e7dec353e606d18f93ef74b94cf">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a2ebffd5d3e0eb209b1d0fa5779609818" class="memitem:a2ebffd5d3e0eb209b1d0fa5779609818">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">zero_elements: 1</td>
</tr>
<tr class="memdesc:a2ebffd5d3e0eb209b1d0fa5779609818">
<td class="mdescLeft"> </td>
<td class="mdescRight">whether to zero-init allocated elements<br />
</td>
</tr>
<tr class="separator:a2ebffd5d3e0eb209b1d0fa5779609818">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_af02ff4ac188a7a04a02ab140e568886b" class="memitem:af02ff4ac188a7a04a02ab140e568886b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusFreedElement * </td>
<td class="memItemRight" data-valign="bottom">free_elements</td>
</tr>
<tr class="memdesc:af02ff4ac188a7a04a02ab140e568886b">
<td class="mdescLeft"> </td>
<td class="mdescRight">a free list of elements to recycle<br />
</td>
</tr>
<tr class="separator:af02ff4ac188a7a04a02ab140e568886b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a4682e065e26ee0dc4d2a17023cb41b8b" class="memitem:a4682e065e26ee0dc4d2a17023cb41b8b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMemBlock * </td>
<td class="memItemRight" data-valign="bottom">blocks</td>
</tr>
<tr class="memdesc:a4682e065e26ee0dc4d2a17023cb41b8b">
<td class="mdescLeft"> </td>
<td class="mdescRight">blocks of memory from malloc()<br />
</td>
</tr>
<tr class="separator:a4682e065e26ee0dc4d2a17023cb41b8b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a23cd8af3ecb8cd88074b1934b1d7597c" class="memitem:a23cd8af3ecb8cd88074b1934b1d7597c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">allocated_elements</td>
</tr>
<tr class="memdesc:a23cd8af3ecb8cd88074b1934b1d7597c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Count of outstanding allocated elements.<br />
</td>
</tr>
<tr class="separator:a23cd8af3ecb8cd88074b1934b1d7597c">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Internals fields of DBusMemPool.

Definition at line 108 of file dbus-mempool.c.

## Field Documentation

## ◆ allocated_elements

|                                     |
|-------------------------------------|
| int DBusMemPool::allocated_elements |

Count of outstanding allocated elements.

Definition at line 116 of file dbus-mempool.c.

Referenced by \_dbus_mem_pool_alloc(), \_dbus_mem_pool_dealloc(), and \_dbus_mem_pool_new().

## ◆ block_size

|                                |
|--------------------------------|
| size_t DBusMemPool::block_size |

size of most recently allocated block

Definition at line 111 of file dbus-mempool.c.

Referenced by \_dbus_mem_pool_alloc(), and \_dbus_mem_pool_new().

## ◆ blocks

|                                    |
|------------------------------------|
| DBusMemBlock\* DBusMemPool::blocks |

blocks of memory from malloc()

Definition at line 115 of file dbus-mempool.c.

Referenced by \_dbus_mem_pool_alloc(), \_dbus_mem_pool_dealloc(), and \_dbus_mem_pool_free().

## ◆ element_size

|                                  |
|----------------------------------|
| size_t DBusMemPool::element_size |

size of a single object in the pool

Definition at line 110 of file dbus-mempool.c.

Referenced by \_dbus_mem_pool_alloc(), and \_dbus_mem_pool_new().

## ◆ free_elements

|                                               |
|-----------------------------------------------|
| DBusFreedElement\* DBusMemPool::free_elements |

a free list of elements to recycle

Definition at line 114 of file dbus-mempool.c.

Referenced by \_dbus_mem_pool_alloc(), and \_dbus_mem_pool_dealloc().

## ◆ zero_elements

|                                         |
|-----------------------------------------|
| unsigned int DBusMemPool::zero_elements |

whether to zero-init allocated elements

Definition at line 112 of file dbus-mempool.c.

Referenced by \_dbus_mem_pool_alloc(), and \_dbus_mem_pool_new().

The documentation for this struct was generated from the following file:

- dbus-mempool.c
