Utility functions for strings with special syntax

D-Bus low-level public API

Parsing D-Bus type signatures. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="functions" class="groupheader"> Functions</h2></td>
</tr>
<tr id="r_ga16a33f0ef4a9efd8f5e8f231dcf13d37" class="memitem:ga16a33f0ef4a9efd8f5e8f231dcf13d37">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_validate_path (const char *path, DBusError *error)</td>
</tr>
<tr class="memdesc:ga16a33f0ef4a9efd8f5e8f231dcf13d37">
<td class="mdescLeft"> </td>
<td class="mdescRight">Check an object path for validity.<br />
</td>
</tr>
<tr class="separator:ga16a33f0ef4a9efd8f5e8f231dcf13d37">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1023d9c1a44eb2fe05c2b82e23622f98" class="memitem:ga1023d9c1a44eb2fe05c2b82e23622f98">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_validate_interface (const char *name, DBusError *error)</td>
</tr>
<tr class="memdesc:ga1023d9c1a44eb2fe05c2b82e23622f98">
<td class="mdescLeft"> </td>
<td class="mdescRight">Check an interface name for validity.<br />
</td>
</tr>
<tr class="separator:ga1023d9c1a44eb2fe05c2b82e23622f98">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab8540880d62965990957f07630aba700" class="memitem:gab8540880d62965990957f07630aba700">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_validate_member (const char *name, DBusError *error)</td>
</tr>
<tr class="memdesc:gab8540880d62965990957f07630aba700">
<td class="mdescLeft"> </td>
<td class="mdescRight">Check a member (method/signal) name for validity.<br />
</td>
</tr>
<tr class="separator:gab8540880d62965990957f07630aba700">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad1c5b9b2dbdb9f9ade7e497b23cb835f" class="memitem:gad1c5b9b2dbdb9f9ade7e497b23cb835f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_validate_error_name (const char *name, DBusError *error)</td>
</tr>
<tr class="memdesc:gad1c5b9b2dbdb9f9ade7e497b23cb835f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Check an error name for validity.<br />
</td>
</tr>
<tr class="separator:gad1c5b9b2dbdb9f9ade7e497b23cb835f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabedd6f4019fc30bc4bbcd144198f8444" class="memitem:gabedd6f4019fc30bc4bbcd144198f8444">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_validate_bus_name (const char *name, DBusError *error)</td>
</tr>
<tr class="memdesc:gabedd6f4019fc30bc4bbcd144198f8444">
<td class="mdescLeft"> </td>
<td class="mdescRight">Check a bus name for validity.<br />
</td>
</tr>
<tr class="separator:gabedd6f4019fc30bc4bbcd144198f8444">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7d98d5d9af66ff78e74d5dd1d8cd3390" class="memitem:ga7d98d5d9af66ff78e74d5dd1d8cd3390">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_validate_utf8 (const char *alleged_utf8, DBusError *error)</td>
</tr>
<tr class="memdesc:ga7d98d5d9af66ff78e74d5dd1d8cd3390">
<td class="mdescLeft"> </td>
<td class="mdescRight">Check a string for validity.<br />
</td>
</tr>
<tr class="separator:ga7d98d5d9af66ff78e74d5dd1d8cd3390">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Parsing D-Bus type signatures.

## Function Documentation

## ◆ dbus_validate_bus_name()

|                                    |     |                |          |
|------------------------------------|-----|----------------|----------|
| dbus_bool_t dbus_validate_bus_name | (   | const char \*  | *name*,  |
|                                    |     | DBusError \*   | *error*  |
|                                    | )   |                |          |

Check a bus name for validity.

Remember that NULL can always be passed instead of a DBusError \*, if you don't care about having an error name and message.

This function is suitable for validating C strings, but is not suitable for validating untrusted data from a network unless the string's length is also checked, since it assumes that the string ends at the first zero byte according to normal C conventions.

Parameters  
|       |                                                        |
|-------|--------------------------------------------------------|
| name  | a potentially invalid bus name, which must not be NULL |
| error | error return                                           |

<!-- -->

Returns  
TRUE if name is valid

Definition at line 244 of file dbus-syntax.c.

References \_dbus_string_get_length(), \_dbus_string_init_const(), \_dbus_string_validate_utf8(), \_dbus_validate_bus_name(), DBUS_ERROR_INVALID_ARGS, dbus_set_error(), FALSE, NULL, and TRUE.

## ◆ dbus_validate_error_name()

|                                      |     |                |          |
|--------------------------------------|-----|----------------|----------|
| dbus_bool_t dbus_validate_error_name | (   | const char \*  | *name*,  |
|                                      |     | DBusError \*   | *error*  |
|                                      | )   |                |          |

Check an error name for validity.

Remember that NULL can always be passed instead of a DBusError \*, if you don't care about having an error name and message.

This function is suitable for validating C strings, but is not suitable for validating untrusted data from a network unless the string's length is also checked, since it assumes that the string ends at the first zero byte according to normal C conventions.

Parameters  
|       |                                                          |
|-------|----------------------------------------------------------|
| name  | a potentially invalid error name, which must not be NULL |
| error | error return                                             |

<!-- -->

Returns  
TRUE if name is valid

Definition at line 197 of file dbus-syntax.c.

References \_dbus_string_get_length(), \_dbus_string_init_const(), \_dbus_string_validate_utf8(), \_dbus_validate_error_name(), DBUS_ERROR_INVALID_ARGS, dbus_set_error(), FALSE, NULL, and TRUE.

## ◆ dbus_validate_interface()

|                                     |     |                |          |
|-------------------------------------|-----|----------------|----------|
| dbus_bool_t dbus_validate_interface | (   | const char \*  | *name*,  |
|                                     |     | DBusError \*   | *error*  |
|                                     | )   |                |          |

Check an interface name for validity.

Remember that NULL can always be passed instead of a DBusError \*, if you don't care about having an error name and message.

This function is suitable for validating C strings, but is not suitable for validating untrusted data from a network unless the string's length is also checked, since it assumes that the string ends at the first zero byte according to normal C conventions.

Parameters  
|       |                                                              |
|-------|--------------------------------------------------------------|
| name  | a potentially invalid interface name, which must not be NULL |
| error | error return                                                 |

<!-- -->

Returns  
TRUE if name is valid

Definition at line 103 of file dbus-syntax.c.

References \_dbus_string_get_length(), \_dbus_string_init_const(), \_dbus_string_validate_utf8(), \_dbus_validate_interface(), DBUS_ERROR_INVALID_ARGS, dbus_set_error(), FALSE, NULL, and TRUE.

## ◆ dbus_validate_member()

|                                  |     |                |          |
|----------------------------------|-----|----------------|----------|
| dbus_bool_t dbus_validate_member | (   | const char \*  | *name*,  |
|                                  |     | DBusError \*   | *error*  |
|                                  | )   |                |          |

Check a member (method/signal) name for validity.

Remember that NULL can always be passed instead of a DBusError \*, if you don't care about having an error name and message.

This function is suitable for validating C strings, but is not suitable for validating untrusted data from a network unless the string's length is also checked, since it assumes that the string ends at the first zero byte according to normal C conventions.

Parameters  
|       |                                                           |
|-------|-----------------------------------------------------------|
| name  | a potentially invalid member name, which must not be NULL |
| error | error return                                              |

<!-- -->

Returns  
TRUE if name is valid

Definition at line 150 of file dbus-syntax.c.

References \_dbus_string_get_length(), \_dbus_string_init_const(), \_dbus_string_validate_utf8(), \_dbus_validate_member(), DBUS_ERROR_INVALID_ARGS, dbus_set_error(), FALSE, NULL, and TRUE.

## ◆ dbus_validate_path()

|                                |     |                |          |
|--------------------------------|-----|----------------|----------|
| dbus_bool_t dbus_validate_path | (   | const char \*  | *path*,  |
|                                |     | DBusError \*   | *error*  |
|                                | )   |                |          |

Check an object path for validity.

Remember that NULL can always be passed instead of a DBusError \*, if you don't care about having an error name and message.

This function is suitable for validating C strings, but is not suitable for validating untrusted data from a network unless the string's length is also checked, since it assumes that the string ends at the first zero byte according to normal C conventions.

Parameters  
|       |                                                           |
|-------|-----------------------------------------------------------|
| path  | a potentially invalid object path, which must not be NULL |
| error | error return                                              |

<!-- -->

Returns  
TRUE if path is valid

Definition at line 56 of file dbus-syntax.c.

References \_dbus_string_get_length(), \_dbus_string_init_const(), \_dbus_string_validate_utf8(), \_dbus_validate_path(), DBUS_ERROR_INVALID_ARGS, dbus_set_error(), FALSE, NULL, and TRUE.

## ◆ dbus_validate_utf8()

|                                |     |                |                 |
|--------------------------------|-----|----------------|-----------------|
| dbus_bool_t dbus_validate_utf8 | (   | const char \*  | *alleged_utf8*, |
|                                |     | DBusError \*   | *error*         |
|                                | )   |                |                 |

Check a string for validity.

Strings on D-Bus must be valid UTF-8. Remember that NULL can always be passed instead of a DBusError \*, if you don't care about having an error name and message.

This function is suitable for validating C strings, but is not suitable for validating untrusted data from a network unless the string's length is also checked, since it assumes that the string ends at the first zero byte according to normal C conventions.

Parameters  
|              |                                                |
|--------------|------------------------------------------------|
| alleged_utf8 | a string to be checked, which must not be NULL |
| error        | error return                                   |

<!-- -->

Returns  
TRUE if alleged_utf8 is valid UTF-8

Definition at line 291 of file dbus-syntax.c.

References \_dbus_string_get_length(), \_dbus_string_init_const(), \_dbus_string_validate_utf8(), DBUS_ERROR_INVALID_ARGS, dbus_set_error(), FALSE, NULL, and TRUE.
