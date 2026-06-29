Message bus APIs internals

D-Bus secret internal implementation details

Internals of functions for communicating with the message bus. More...

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
<td class="memItemRight" data-valign="bottom">BusData</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Block of message-bus-related data we attach to each DBusConnection used with these convenience functions. More...<br />
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
<tr id="r_ga2ae7ac6acf3f48e31fb3809cd038b598" class="memitem:ga2ae7ac6acf3f48e31fb3809cd038b598">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">N_BUS_TYPES   3</td>
</tr>
<tr class="memdesc:ga2ae7ac6acf3f48e31fb3809cd038b598">
<td class="mdescLeft"> </td>
<td class="mdescRight">Number of bus types.<br />
</td>
</tr>
<tr class="separator:ga2ae7ac6acf3f48e31fb3809cd038b598">
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
<tr id="r_ga0e7fe5d0dcaca7ecb4b5a7ace23d6286" class="memitem:ga0e7fe5d0dcaca7ecb4b5a7ace23d6286">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_bus_notify_shared_connection_disconnected_unlocked (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:ga0e7fe5d0dcaca7ecb4b5a7ace23d6286">
<td class="mdescLeft"> </td>
<td class="mdescRight">Internal function that checks to see if this is a shared connection owned by the bus and if it is unref it.<br />
</td>
</tr>
<tr class="separator:ga0e7fe5d0dcaca7ecb4b5a7ace23d6286">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Internals of functions for communicating with the message bus.

## Macro Definition Documentation

## ◆ N_BUS_TYPES

|                          |
|--------------------------|
| \#define N_BUS_TYPES   3 |

Number of bus types.

Definition at line 93 of file dbus-bus.c.

## Function Documentation

## ◆ \_dbus_bus_notify_shared_connection_disconnected_unlocked()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| void \_dbus_bus_notify_shared_connection_disconnected_unlocked | ( | DBusConnection \*  | *connection* | ) |  |

Internal function that checks to see if this is a shared connection owned by the bus and if it is unref it.

Parameters  
|            |                                          |
|------------|------------------------------------------|
| connection | a connection that has been disconnected. |

Definition at line 390 of file dbus-bus.c.

References \_DBUS_LOCK, \_DBUS_UNLOCK, N_BUS_TYPES, and NULL.
