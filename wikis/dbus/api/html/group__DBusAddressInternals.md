Address parsing

D-Bus secret internal implementation details

Implementation of parsing addresses of D-Bus servers. More...

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
<td class="memItemRight" data-valign="bottom">DBusAddressEntry</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Internals of DBusAddressEntry. More...<br />
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
<tr id="r_ga0e46a8bc37d92810fe3d535019d3bad1" class="memitem:ga0e46a8bc37d92810fe3d535019d3bad1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_DBUS_ADDRESS_OPTIONALLY_ESCAPED_BYTE(b)</td>
</tr>
<tr class="memdesc:ga0e46a8bc37d92810fe3d535019d3bad1">
<td class="mdescLeft"> </td>
<td class="mdescRight">TRUE if the byte need not be escaped when found in a dbus address.<br />
</td>
</tr>
<tr class="separator:ga0e46a8bc37d92810fe3d535019d3bad1">
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
<tr id="r_ga5b6409826263c7d62570c56889f7ddb2" class="memitem:ga5b6409826263c7d62570c56889f7ddb2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_set_bad_address (DBusError *error, const char *address_problem_type, const char *address_problem_field, const char *address_problem_other)</td>
</tr>
<tr class="memdesc:ga5b6409826263c7d62570c56889f7ddb2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets DBUS_ERROR_BAD_ADDRESS.<br />
</td>
</tr>
<tr class="separator:ga5b6409826263c7d62570c56889f7ddb2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1ecc2f460303cd70c34e7667e8b12b37" class="memitem:ga1ecc2f460303cd70c34e7667e8b12b37">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_address_append_escaped (DBusString *escaped, const DBusString *unescaped)</td>
</tr>
<tr class="memdesc:ga1ecc2f460303cd70c34e7667e8b12b37">
<td class="mdescLeft"> </td>
<td class="mdescRight">Appends an escaped version of one string to another string, using the D-Bus address escaping mechanism.<br />
</td>
</tr>
<tr class="separator:ga1ecc2f460303cd70c34e7667e8b12b37">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Implementation of parsing addresses of D-Bus servers.

## Macro Definition Documentation

## ◆ \_DBUS_ADDRESS_OPTIONALLY_ESCAPED_BYTE

|                                                 |     |     |     |     |     |
|-------------------------------------------------|-----|-----|-----|-----|-----|
| \#define \_DBUS_ADDRESS_OPTIONALLY_ESCAPED_BYTE | (   |     | b   | )   |     |

**Value:**

(((b) \>= 'a' && (b) \<= 'z') \|\| \\

((b) \>= 'A' && (b) \<= 'Z') \|\| \\

((b) \>= '0' && (b) \<= '9') \|\| \\

\(b\) == '-' \|\| \\

\(b\) == '\_' \|\| \\

\(b\) == '/' \|\| \\

\(b\) == '\\' \|\| \\

\(b\) == '\*' \|\| \\

\(b\) == '.')

TRUE if the byte need not be escaped when found in a dbus address.

All other bytes are required to be escaped in a valid address.

Definition at line 89 of file dbus-address.c.

## Function Documentation

## ◆ \_dbus_address_append_escaped()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_address_append_escaped | ( | DBusString \*  | *escaped*, |
|  |  | const DBusString \*  | *unescaped*  |
|  | ) |  |  |

Appends an escaped version of one string to another string, using the D-Bus address escaping mechanism.

Parameters  
|           |                         |
|-----------|-------------------------|
| escaped   | the string to append to |
| unescaped | the string to escape    |

<!-- -->

Returns  
FALSE if no memory

Definition at line 109 of file dbus-address.c.

References \_DBUS_ADDRESS_OPTIONALLY_ESCAPED_BYTE, \_dbus_string_append_byte(), \_dbus_string_append_byte_as_hex(), \_dbus_string_get_length(), \_dbus_string_set_length(), FALSE, and TRUE.

Referenced by \_dbus_append_address_from_socket(), \_dbus_server_new_for_domain_socket(), \_dbus_server_new_for_tcp_socket(), \_dbus_transport_new_for_domain_socket(), and dbus_address_escape_value().

## ◆ \_dbus_set_bad_address()

|                             |     |                |                          |
|-----------------------------|-----|----------------|--------------------------|
| void \_dbus_set_bad_address | (   | DBusError \*   | *error*,                 |
|                             |     | const char \*  | *address_problem_type*,  |
|                             |     | const char \*  | *address_problem_field*, |
|                             |     | const char \*  | *address_problem_other*  |
|                             | )   |                |                          |

Sets DBUS_ERROR_BAD_ADDRESS.

If address_problem_type and address_problem_field are not NULL, sets an error message about how the field is no good. Otherwise, sets address_problem_other as the error message.

Parameters  
|                       |                                              |
|-----------------------|----------------------------------------------|
| error                 | the error to set                             |
| address_problem_type  | the address type of the bad address or NULL  |
| address_problem_field | the missing field of the bad address or NULL |
| address_problem_other | any other error message or NULL              |

Definition at line 70 of file dbus-address.c.

References DBUS_ERROR_BAD_ADDRESS, dbus_set_error(), and NULL.

Referenced by \_dbus_server_listen_platform_specific(), \_dbus_server_listen_unix_socket(), \_dbus_transport_open(), \_dbus_transport_open_platform_specific(), \_dbus_transport_open_socket(), and \_dbus_transport_open_unix_socket().
