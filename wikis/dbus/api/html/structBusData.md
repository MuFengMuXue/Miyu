BusData Struct Reference

D-Bus secret internal implementation details » Message bus APIs internals

Block of message-bus-related data we attach to each DBusConnection used with these convenience functions. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a3c78791306fb4810779fe498a1067f46" class="memitem:a3c78791306fb4810779fe498a1067f46">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusConnection * </td>
<td class="memItemRight" data-valign="bottom">connection</td>
</tr>
<tr class="memdesc:a3c78791306fb4810779fe498a1067f46">
<td class="mdescLeft"> </td>
<td class="mdescRight">Connection we're associated with.<br />
</td>
</tr>
<tr class="separator:a3c78791306fb4810779fe498a1067f46">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aaba673d2a99c4ca76fada7384942dfc9" class="memitem:aaba673d2a99c4ca76fada7384942dfc9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char * </td>
<td class="memItemRight" data-valign="bottom">unique_name</td>
</tr>
<tr class="memdesc:aaba673d2a99c4ca76fada7384942dfc9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Unique name of this connection.<br />
</td>
</tr>
<tr class="separator:aaba673d2a99c4ca76fada7384942dfc9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a0efe71943560d7c5f9eba63618852db2" class="memitem:a0efe71943560d7c5f9eba63618852db2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">is_well_known: 1</td>
</tr>
<tr class="memdesc:a0efe71943560d7c5f9eba63618852db2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Is one of the well-known connections in our global array.<br />
</td>
</tr>
<tr class="separator:a0efe71943560d7c5f9eba63618852db2">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Block of message-bus-related data we attach to each DBusConnection used with these convenience functions.

Definition at line 79 of file dbus-bus.c.

## Field Documentation

## ◆ connection

|                                      |
|--------------------------------------|
| DBusConnection\* BusData::connection |

Connection we're associated with.

Definition at line 81 of file dbus-bus.c.

## ◆ is_well_known

|                                     |
|-------------------------------------|
| unsigned int BusData::is_well_known |

Is one of the well-known connections in our global array.

Definition at line 84 of file dbus-bus.c.

## ◆ unique_name

|                             |
|-----------------------------|
| char\* BusData::unique_name |

Unique name of this connection.

Definition at line 82 of file dbus-bus.c.

Referenced by dbus_bus_get_unique_name(), dbus_bus_register(), and dbus_bus_set_unique_name().

The documentation for this struct was generated from the following file:

- dbus-bus.c
