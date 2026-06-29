DBusTransport implementations for UNIX

D-Bus secret internal implementation details

Implementation details of DBusTransport on UNIX. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="functions" class="groupheader"> Functions</h2></td>
</tr>
<tr id="r_ga00a2b78c927666e324acdb07126f0245" class="memitem:ga00a2b78c927666e324acdb07126f0245">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusTransportOpenResult </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_open_unixexec (DBusAddressEntry *entry, DBusTransport **transport_p, DBusError *error)</td>
</tr>
<tr class="separator:ga00a2b78c927666e324acdb07126f0245">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gafd694944860033155276df9162bdf72e" class="memitem:gafd694944860033155276df9162bdf72e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusTransportOpenResult </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_open_platform_specific (DBusAddressEntry *entry, DBusTransport **transport_p, DBusError *error)</td>
</tr>
<tr class="memdesc:gafd694944860033155276df9162bdf72e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Opens platform specific transport types.<br />
</td>
</tr>
<tr class="separator:gafd694944860033155276df9162bdf72e">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Implementation details of DBusTransport on UNIX.

## Function Documentation

## ◆ \_dbus_transport_open_platform_specific()

|  |  |  |  |
|----|----|----|----|
| DBusTransportOpenResult \_dbus_transport_open_platform_specific | ( | DBusAddressEntry \*  | *entry*, |
|  |  | DBusTransport \*\*  | *transport_p*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Opens platform specific transport types.

Parameters  
|             |                                          |
|-------------|------------------------------------------|
| entry       | the address entry to try opening         |
| transport_p | return location for the opened transport |
| error       | error to be set                          |

<!-- -->

Returns  
result of the attempt

Definition at line 248 of file dbus-transport-unix.c.

References \_dbus_assert, \_dbus_lookup_launchd_socket(), \_dbus_set_bad_address(), \_dbus_string_free(), \_dbus_string_get_const_data(), \_dbus_string_init(), \_dbus_transport_new_for_domain_socket(), dbus_address_entry_get_method(), dbus_address_entry_get_value(), DBUS_ERROR_BAD_ADDRESS, dbus_error_free(), DBUS_ERROR_INIT, dbus_error_is_set(), dbus_move_error(), dbus_set_error(), FALSE, and NULL.

## ◆ \_dbus_transport_open_unixexec()

|  |  |  |  |
|----|----|----|----|
| DBusTransportOpenResult \_dbus_transport_open_unixexec | ( | DBusAddressEntry \*  | *entry*, |
|  |  | DBusTransport \*\*  | *transport_p*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Definition at line 149 of file dbus-transport-unix.c.
