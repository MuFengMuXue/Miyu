dbus-uuidgen implementation

D-Bus secret internal implementation details

Functions for dbus-uuidgen binary. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="functions" class="groupheader"> Functions</h2></td>
</tr>
<tr id="r_ga239a51668da136c7e80a7bae01b1934d" class="memitem:ga239a51668da136c7e80a7bae01b1934d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_get_uuid (const char *filename, char **uuid_p, dbus_bool_t create_if_not_found, DBusError *error)</td>
</tr>
<tr class="memdesc:ga239a51668da136c7e80a7bae01b1934d">
<td class="mdescLeft"> </td>
<td class="mdescRight">For use by the dbus-uuidgen binary ONLY, do not call this.<br />
</td>
</tr>
<tr class="separator:ga239a51668da136c7e80a7bae01b1934d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga080b95280aa7e8dd06ee418a3b28d233" class="memitem:ga080b95280aa7e8dd06ee418a3b28d233">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_create_uuid (char **uuid_p, DBusError *error)</td>
</tr>
<tr class="separator:ga080b95280aa7e8dd06ee418a3b28d233">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Functions for dbus-uuidgen binary.

These are not considered part of the ABI, and if you call them you will get screwed by future changes.

## Function Documentation

## ◆ \_dbus_create_uuid()

|                                |     |               |           |
|--------------------------------|-----|---------------|-----------|
| dbus_bool_t \_dbus_create_uuid | (   | char \*\*     | *uuid_p*, |
|                                |     | DBusError \*  | *error*   |
|                                | )   |               |           |

Parameters  
|        |                                      |
|--------|--------------------------------------|
| uuid_p | out param to return the uuid         |
| error  | location to store reason for failure |

<!-- -->

Returns  
TRUE on success

Definition at line 121 of file dbus-uuidgen.c.

References \_dbus_generate_uuid(), and FALSE.

## ◆ \_dbus_get_uuid()

|                             |     |                |                        |
|-----------------------------|-----|----------------|------------------------|
| dbus_bool_t \_dbus_get_uuid | (   | const char \*  | *filename*,            |
|                             |     | char \*\*      | *uuid_p*,              |
|                             |     | dbus_bool_t    | *create_if_not_found*, |
|                             |     | DBusError \*   | *error*                |
|                             | )   |                |                        |

For use by the dbus-uuidgen binary ONLY, do not call this.

We can and will change this function without modifying the libdbus soname.

Parameters  
|                     |                                           |
|---------------------|-------------------------------------------|
| filename            | the file or NULL for the machine ID file  |
| uuid_p              | out param to return the uuid              |
| create_if_not_found | whether to create it if not already there |
| error               | error return                              |

<!-- -->

Returns  
FALSE if error is set

Definition at line 85 of file dbus-uuidgen.c.

References \_dbus_read_local_machine_uuid(), \_dbus_read_uuid_file(), \_dbus_string_init_const(), FALSE, and TRUE.
