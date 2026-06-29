DBusDataSlotAllocator Struct Reference

An allocator that tracks a set of slot IDs. More...

`#include <``dbus-dataslot.h``>`

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a290fc1a48efc181da4e54dae572306b5" class="memitem:a290fc1a48efc181da4e54dae572306b5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusAllocatedSlot * </td>
<td class="memItemRight" data-valign="bottom">allocated_slots</td>
</tr>
<tr class="memdesc:a290fc1a48efc181da4e54dae572306b5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Allocated slots.<br />
</td>
</tr>
<tr class="separator:a290fc1a48efc181da4e54dae572306b5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a57702eaf2d6558cc15f12205aca90dda" class="memitem:a57702eaf2d6558cc15f12205aca90dda">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">n_allocated_slots</td>
</tr>
<tr class="memdesc:a57702eaf2d6558cc15f12205aca90dda">
<td class="mdescLeft"> </td>
<td class="mdescRight">number of slots malloc'd<br />
</td>
</tr>
<tr class="separator:a57702eaf2d6558cc15f12205aca90dda">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ad68b0989a821eb266983052f8a402a4a" class="memitem:ad68b0989a821eb266983052f8a402a4a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">n_used_slots</td>
</tr>
<tr class="memdesc:ad68b0989a821eb266983052f8a402a4a">
<td class="mdescLeft"> </td>
<td class="mdescRight">number of slots used<br />
</td>
</tr>
<tr class="separator:ad68b0989a821eb266983052f8a402a4a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a5908a6f2e17e5feec5b77a2cfbc81dbd" class="memitem:a5908a6f2e17e5feec5b77a2cfbc81dbd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusGlobalLock </td>
<td class="memItemRight" data-valign="bottom">lock</td>
</tr>
<tr class="memdesc:a5908a6f2e17e5feec5b77a2cfbc81dbd">
<td class="mdescLeft"> </td>
<td class="mdescRight">index of thread lock<br />
</td>
</tr>
<tr class="separator:a5908a6f2e17e5feec5b77a2cfbc81dbd">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

An allocator that tracks a set of slot IDs.

Definition at line 57 of file dbus-dataslot.h.

## Field Documentation

## ◆ allocated_slots

|                                                            |
|------------------------------------------------------------|
| DBusAllocatedSlot\* DBusDataSlotAllocator::allocated_slots |

Allocated slots.

Definition at line 59 of file dbus-dataslot.h.

Referenced by \_dbus_data_slot_allocator_alloc(), \_dbus_data_slot_allocator_free(), \_dbus_data_slot_allocator_init(), \_dbus_data_slot_list_get(), and \_dbus_data_slot_list_set().

## ◆ lock

|                                            |
|--------------------------------------------|
| DBusGlobalLock DBusDataSlotAllocator::lock |

index of thread lock

Definition at line 62 of file dbus-dataslot.h.

Referenced by \_dbus_data_slot_allocator_alloc(), \_dbus_data_slot_allocator_free(), \_dbus_data_slot_allocator_init(), \_dbus_data_slot_list_get(), and \_dbus_data_slot_list_set().

## ◆ n_allocated_slots

|                                              |
|----------------------------------------------|
| int DBusDataSlotAllocator::n_allocated_slots |

number of slots malloc'd

Definition at line 60 of file dbus-dataslot.h.

Referenced by \_dbus_data_slot_allocator_alloc(), \_dbus_data_slot_allocator_free(), and \_dbus_data_slot_allocator_init().

## ◆ n_used_slots

|                                         |
|-----------------------------------------|
| int DBusDataSlotAllocator::n_used_slots |

number of slots used

Definition at line 61 of file dbus-dataslot.h.

Referenced by \_dbus_data_slot_allocator_alloc(), \_dbus_data_slot_allocator_free(), and \_dbus_data_slot_allocator_init().

The documentation for this struct was generated from the following file:

- dbus-dataslot.h
