Data slots

D-Bus secret internal implementation details

Storing data by ID. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="functions" class="groupheader"> Functions</h2></td>
</tr>
<tr id="r_ga49236838eb414100f691a22ad5210cb5" class="memitem:ga49236838eb414100f691a22ad5210cb5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_data_slot_allocator_init (DBusDataSlotAllocator *allocator, DBusGlobalLock lock)</td>
</tr>
<tr class="memdesc:ga49236838eb414100f691a22ad5210cb5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initializes a data slot allocator object, used to assign integer IDs for data slots.<br />
</td>
</tr>
<tr class="separator:ga49236838eb414100f691a22ad5210cb5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf61f2bd0148bace4f67a2d6d97b26ea9" class="memitem:gaf61f2bd0148bace4f67a2d6d97b26ea9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_data_slot_allocator_alloc (DBusDataSlotAllocator *allocator, dbus_int32_t *slot_id_p)</td>
</tr>
<tr class="memdesc:gaf61f2bd0148bace4f67a2d6d97b26ea9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Allocates an integer ID to be used for storing data in a DBusDataSlotList.<br />
</td>
</tr>
<tr class="separator:gaf61f2bd0148bace4f67a2d6d97b26ea9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga059c50a24cd9fc984e918e6159841633" class="memitem:ga059c50a24cd9fc984e918e6159841633">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_data_slot_allocator_free (DBusDataSlotAllocator *allocator, dbus_int32_t *slot_id_p)</td>
</tr>
<tr class="memdesc:ga059c50a24cd9fc984e918e6159841633">
<td class="mdescLeft"> </td>
<td class="mdescRight">Deallocates an ID previously allocated with _dbus_data_slot_allocator_alloc().<br />
</td>
</tr>
<tr class="separator:ga059c50a24cd9fc984e918e6159841633">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6de49b3a1210202215d40a5a19806992" class="memitem:ga6de49b3a1210202215d40a5a19806992">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_data_slot_list_init (DBusDataSlotList *list)</td>
</tr>
<tr class="memdesc:ga6de49b3a1210202215d40a5a19806992">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initializes a slot list.<br />
</td>
</tr>
<tr class="separator:ga6de49b3a1210202215d40a5a19806992">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad2952f9f686d96e7114fc49ab7452e1a" class="memitem:gad2952f9f686d96e7114fc49ab7452e1a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_data_slot_list_set (DBusDataSlotAllocator *allocator, DBusDataSlotList *list, int slot, void *data, DBusFreeFunction free_data_func, DBusFreeFunction *old_free_func, void **old_data)</td>
</tr>
<tr class="memdesc:gad2952f9f686d96e7114fc49ab7452e1a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Stores a pointer in the data slot list, along with an optional function to be used for freeing the data when the data is set again, or when the slot list is finalized.<br />
</td>
</tr>
<tr class="separator:gad2952f9f686d96e7114fc49ab7452e1a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabf16c9dca3685a2e4b19344bee8ba6a7" class="memitem:gabf16c9dca3685a2e4b19344bee8ba6a7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">_dbus_data_slot_list_get (DBusDataSlotAllocator *allocator, DBusDataSlotList *list, int slot)</td>
</tr>
<tr class="memdesc:gabf16c9dca3685a2e4b19344bee8ba6a7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Retrieves data previously set with _dbus_data_slot_list_set_data().<br />
</td>
</tr>
<tr class="separator:gabf16c9dca3685a2e4b19344bee8ba6a7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3c96d2ca263ba397b4da2956a49ae282" class="memitem:ga3c96d2ca263ba397b4da2956a49ae282">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_data_slot_list_clear (DBusDataSlotList *list)</td>
</tr>
<tr class="memdesc:ga3c96d2ca263ba397b4da2956a49ae282">
<td class="mdescLeft"> </td>
<td class="mdescRight">Frees all data slots contained in the list, calling application-provided free functions if they exist.<br />
</td>
</tr>
<tr class="separator:ga3c96d2ca263ba397b4da2956a49ae282">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabc399733376c462c3010271a2d431e73" class="memitem:gabc399733376c462c3010271a2d431e73">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_data_slot_list_free (DBusDataSlotList *list)</td>
</tr>
<tr class="memdesc:gabc399733376c462c3010271a2d431e73">
<td class="mdescLeft"> </td>
<td class="mdescRight">Frees the data slot list and all data slots contained in it, calling application-provided free functions if they exist.<br />
</td>
</tr>
<tr class="separator:gabc399733376c462c3010271a2d431e73">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Storing data by ID.

Types and functions related to storing data by an allocated ID. This is used for dbus_connection_set_data(), dbus_server_set_data(), etc.

## Function Documentation

## ◆ \_dbus_data_slot_allocator_alloc()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_data_slot_allocator_alloc | ( | DBusDataSlotAllocator \*  | *allocator*, |
|  |  | dbus_int32_t \*  | *slot_id_p*  |
|  | ) |  |  |

Allocates an integer ID to be used for storing data in a DBusDataSlotList.

If the value at \*slot_id_p is not -1, this function just increments the refcount for the existing slot ID. If the value is -1, a new slot ID is allocated and stored at \*slot_id_p.

Parameters  
|           |                                  |
|-----------|----------------------------------|
| allocator | the allocator                    |
| slot_id_p | address to fill with the slot ID |

<!-- -->

Returns  
TRUE on success

Definition at line 72 of file dbus-dataslot.c.

References \_dbus_assert, DBusDataSlotAllocator::allocated_slots, dbus_realloc(), FALSE, DBusDataSlotAllocator::lock, DBusDataSlotAllocator::n_allocated_slots, DBusDataSlotAllocator::n_used_slots, NULL, DBusAllocatedSlot::refcount, and DBusAllocatedSlot::slot_id.

Referenced by dbus_connection_allocate_data_slot(), dbus_message_allocate_data_slot(), dbus_pending_call_allocate_data_slot(), and dbus_server_allocate_data_slot().

## ◆ \_dbus_data_slot_allocator_free()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_data_slot_allocator_free | ( | DBusDataSlotAllocator \*  | *allocator*, |
|  |  | dbus_int32_t \*  | *slot_id_p*  |
|  | ) |  |  |

Deallocates an ID previously allocated with \_dbus_data_slot_allocator_alloc().

Existing data stored on existing DBusDataSlotList objects with this ID will be freed when the data list is finalized, but may not be retrieved (and may only be replaced if someone else reallocates the slot). The slot value is reset to -1 if this is the last unref.

Parameters  
|           |                                 |
|-----------|---------------------------------|
| allocator | the allocator                   |
| slot_id_p | address where we store the slot |

Definition at line 157 of file dbus-dataslot.c.

References \_dbus_assert, \_dbus_assert_not_reached, DBusDataSlotAllocator::allocated_slots, dbus_free(), DBusDataSlotAllocator::lock, DBusDataSlotAllocator::n_allocated_slots, DBusDataSlotAllocator::n_used_slots, NULL, DBusAllocatedSlot::refcount, and DBusAllocatedSlot::slot_id.

Referenced by dbus_connection_free_data_slot(), dbus_message_free_data_slot(), dbus_pending_call_free_data_slot(), and dbus_server_free_data_slot().

## ◆ \_dbus_data_slot_allocator_init()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_data_slot_allocator_init | ( | DBusDataSlotAllocator \*  | *allocator*, |
|  |  | DBusGlobalLock  | *lock*  |
|  | ) |  |  |

Initializes a data slot allocator object, used to assign integer IDs for data slots.

Parameters  
|           |                             |
|-----------|-----------------------------|
| allocator | the allocator to initialize |

Definition at line 49 of file dbus-dataslot.c.

References DBusDataSlotAllocator::allocated_slots, DBusDataSlotAllocator::lock, DBusDataSlotAllocator::n_allocated_slots, DBusDataSlotAllocator::n_used_slots, NULL, and TRUE.

## ◆ \_dbus_data_slot_list_clear()

|                                  |     |                      |        |     |     |
|----------------------------------|-----|----------------------|--------|-----|-----|
| void \_dbus_data_slot_list_clear | (   | DBusDataSlotList \*  | *list* | )   |     |

Frees all data slots contained in the list, calling application-provided free functions if they exist.

Parameters  
|      |                   |
|------|-------------------|
| list | the list to clear |

Definition at line 320 of file dbus-dataslot.c.

References data, free_data_func, NULL, and DBusDataSlotList::slots.

Referenced by \_dbus_data_slot_list_free().

## ◆ \_dbus_data_slot_list_free()

|                                 |     |                      |        |     |     |
|---------------------------------|-----|----------------------|--------|-----|-----|
| void \_dbus_data_slot_list_free | (   | DBusDataSlotList \*  | *list* | )   |     |

Frees the data slot list and all data slots contained in it, calling application-provided free functions if they exist.

Parameters  
|      |                  |
|------|------------------|
| list | the list to free |

Definition at line 343 of file dbus-dataslot.c.

References \_dbus_data_slot_list_clear(), dbus_free(), DBusDataSlotList::n_slots, NULL, and DBusDataSlotList::slots.

Referenced by \_dbus_server_finalize_base().

## ◆ \_dbus_data_slot_list_get()

|  |  |  |  |
|----|----|----|----|
| void \* \_dbus_data_slot_list_get | ( | DBusDataSlotAllocator \*  | *allocator*, |
|  |  | DBusDataSlotList \*  | *list*, |
|  |  | int  | *slot*  |
|  | ) |  |  |

Retrieves data previously set with \_dbus_data_slot_list_set_data().

The slot must still be allocated (must not have been freed).

Parameters  
|           |                                       |
|-----------|---------------------------------------|
| allocator | the allocator slot was allocated from |
| list      | the data slot list                    |
| slot      | the slot to get data from             |

<!-- -->

Returns  
the data, or NULL if not found

Definition at line 288 of file dbus-dataslot.c.

References \_dbus_assert, \_dbus_assert_not_reached, DBusDataSlotAllocator::allocated_slots, data, DBusDataSlotAllocator::lock, DBusDataSlotList::n_slots, NULL, DBusAllocatedSlot::slot_id, and DBusDataSlotList::slots.

Referenced by dbus_connection_get_data(), dbus_message_get_data(), dbus_pending_call_get_data(), and dbus_server_get_data().

## ◆ \_dbus_data_slot_list_init()

|                                 |     |                      |        |     |     |
|---------------------------------|-----|----------------------|--------|-----|-----|
| void \_dbus_data_slot_list_init | (   | DBusDataSlotList \*  | *list* | )   |     |

Initializes a slot list.

Parameters  
|      |                         |
|------|-------------------------|
| list | the list to initialize. |

Definition at line 200 of file dbus-dataslot.c.

References DBusDataSlotList::n_slots, NULL, and DBusDataSlotList::slots.

Referenced by \_dbus_connection_new_for_transport(), \_dbus_pending_call_new_unlocked(), and \_dbus_server_init_base().

## ◆ \_dbus_data_slot_list_set()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_data_slot_list_set | ( | DBusDataSlotAllocator \*  | *allocator*, |
|  |  | DBusDataSlotList \*  | *list*, |
|  |  | int  | *slot*, |
|  |  | void \*  | *data*, |
|  |  | DBusFreeFunction  | *free_data_func*, |
|  |  | DBusFreeFunction \*  | *old_free_func*, |
|  |  | void \*\*  | *old_data*  |
|  | ) |  |  |

Stores a pointer in the data slot list, along with an optional function to be used for freeing the data when the data is set again, or when the slot list is finalized.

The slot number must have been allocated with \_dbus_data_slot_allocator_alloc() for the same allocator passed in here. The same allocator has to be used with the slot list every time.

Parameters  
|  |  |
|----|----|
| allocator | the allocator to use |
| list | the data slot list |
| slot | the slot number |
| data | the data to store |
| free_data_func | finalizer function for the data |
| old_free_func | free function for any previously-existing data |
| old_data | previously-existing data, should be freed with old_free_func |

<!-- -->

Returns  
TRUE if there was enough memory to store the data

Definition at line 224 of file dbus-dataslot.c.

References \_dbus_assert, \_dbus_assert_not_reached, DBusDataSlotAllocator::allocated_slots, data, dbus_realloc(), FALSE, free_data_func, DBusDataSlotAllocator::lock, DBusDataSlotList::n_slots, NULL, DBusAllocatedSlot::slot_id, DBusDataSlotList::slots, and TRUE.

Referenced by \_dbus_pending_call_set_data_unlocked(), dbus_connection_set_data(), dbus_message_set_data(), and dbus_server_set_data().
