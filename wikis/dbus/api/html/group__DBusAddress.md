Address parsing

D-Bus low-level public API

Parsing addresses of D-Bus servers. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="typedefs" class="groupheader"> Typedefs</h2></td>
</tr>
<tr id="r_ga6875129b8255f5d177335d117e30effd" class="memitem:ga6875129b8255f5d177335d117e30effd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusAddressEntry </td>
<td class="memItemRight" data-valign="bottom">DBusAddressEntry</td>
</tr>
<tr class="memdesc:ga6875129b8255f5d177335d117e30effd">
<td class="mdescLeft"> </td>
<td class="mdescRight">Opaque type representing one of the semicolon-separated items in an address.<br />
</td>
</tr>
<tr class="separator:ga6875129b8255f5d177335d117e30effd">
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
<tr id="r_ga37a7009b07cf991ff07f3e86d71bf352" class="memitem:ga37a7009b07cf991ff07f3e86d71bf352">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_address_entries_free (DBusAddressEntry **entries)</td>
</tr>
<tr class="memdesc:ga37a7009b07cf991ff07f3e86d71bf352">
<td class="mdescLeft"> </td>
<td class="mdescRight">Frees a NULL-terminated array of address entries.<br />
</td>
</tr>
<tr class="separator:ga37a7009b07cf991ff07f3e86d71bf352">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7e6b2572d6e637826acada01377b5487" class="memitem:ga7e6b2572d6e637826acada01377b5487">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">dbus_address_entry_get_method (DBusAddressEntry *entry)</td>
</tr>
<tr class="memdesc:ga7e6b2572d6e637826acada01377b5487">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns the method string of an address entry.<br />
</td>
</tr>
<tr class="separator:ga7e6b2572d6e637826acada01377b5487">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae6f014689b49099e835b1f97d032034e" class="memitem:gae6f014689b49099e835b1f97d032034e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">dbus_address_entry_get_value (DBusAddressEntry *entry, const char *key)</td>
</tr>
<tr class="memdesc:gae6f014689b49099e835b1f97d032034e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns a value from a key of an entry.<br />
</td>
</tr>
<tr class="separator:gae6f014689b49099e835b1f97d032034e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga761e9c17a9a79244434ad57dda3080b3" class="memitem:ga761e9c17a9a79244434ad57dda3080b3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_parse_address (const char *address, DBusAddressEntry ***entry_result, int *array_len, DBusError *error)</td>
</tr>
<tr class="memdesc:ga761e9c17a9a79244434ad57dda3080b3">
<td class="mdescLeft"> </td>
<td class="mdescRight">Parses an address string of the form:<br />
</td>
</tr>
<tr class="separator:ga761e9c17a9a79244434ad57dda3080b3">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga818e79423595cd2a306ec1b4dc1ab7f5" class="memitem:ga818e79423595cd2a306ec1b4dc1ab7f5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char * </td>
<td class="memItemRight" data-valign="bottom">dbus_address_escape_value (const char *value)</td>
</tr>
<tr class="memdesc:ga818e79423595cd2a306ec1b4dc1ab7f5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Escapes the given string as a value in a key=value pair for a D-Bus address.<br />
</td>
</tr>
<tr class="separator:ga818e79423595cd2a306ec1b4dc1ab7f5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga80d4e20206f8f1e9bbd2607e9f4bbb44" class="memitem:ga80d4e20206f8f1e9bbd2607e9f4bbb44">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char * </td>
<td class="memItemRight" data-valign="bottom">dbus_address_unescape_value (const char *value, DBusError *error)</td>
</tr>
<tr class="memdesc:ga80d4e20206f8f1e9bbd2607e9f4bbb44">
<td class="mdescLeft"> </td>
<td class="mdescRight">Unescapes the given string as a value in a key=value pair for a D-Bus address.<br />
</td>
</tr>
<tr class="separator:ga80d4e20206f8f1e9bbd2607e9f4bbb44">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Parsing addresses of D-Bus servers.

## Typedef Documentation

## ◆ DBusAddressEntry

|                                                  |
|--------------------------------------------------|
| typedef struct DBusAddressEntry DBusAddressEntry |

Opaque type representing one of the semicolon-separated items in an address.

Definition at line 43 of file dbus-address.h.

## Function Documentation

## ◆ dbus_address_entries_free()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT void dbus_address_entries_free | ( | DBusAddressEntry \*\*  | *entries* | ) |  |

Frees a NULL-terminated array of address entries.

Parameters  
|         |            |
|---------|------------|
| entries | the array. |

Definition at line 194 of file dbus-address.c.

References dbus_free(), and NULL.

Referenced by dbus_server_listen().

## ◆ dbus_address_entry_get_method()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT const char \* dbus_address_entry_get_method | ( | DBusAddressEntry \*  | *entry* | ) |  |

Returns the method string of an address entry.

For example, given the address entry "tcp:host=example.com" it would return the string "tcp"

Parameters  
|       |            |
|-------|------------|
| entry | the entry. |

<!-- -->

Returns  
a string describing the method. This string must not be freed.

Definition at line 232 of file dbus-address.c.

References \_dbus_string_get_const_data(), and DBusAddressEntry::method.

Referenced by \_dbus_server_listen_platform_specific(), \_dbus_server_listen_socket(), \_dbus_server_listen_unix_socket(), \_dbus_transport_open_platform_specific(), \_dbus_transport_open_socket(), \_dbus_transport_open_unix_socket(), and dbus_server_listen().

## ◆ dbus_address_entry_get_value()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT const char \* dbus_address_entry_get_value | ( | DBusAddressEntry \*  | *entry*, |
|  |  | const char \*  | *key*  |
|  | ) |  |  |

Returns a value from a key of an entry.

For example, given the address "tcp:host=example.com,port=8073" if you asked for the key "host" you would get the value "example.com"

The returned value is already unescaped.

Parameters  
|       |            |
|-------|------------|
| entry | the entry. |
| key   | the key.   |

<!-- -->

Returns  
the key value. This string must not be freed.

Definition at line 249 of file dbus-address.c.

References \_dbus_assert, \_dbus_list_get_first_link(), \_dbus_list_get_next_link, \_dbus_string_equal_c_str(), \_dbus_string_get_const_data(), DBusList::data, DBusAddressEntry::keys, NULL, and DBusAddressEntry::values.

Referenced by \_dbus_server_listen_platform_specific(), \_dbus_server_listen_socket(), \_dbus_server_listen_unix_socket(), \_dbus_transport_open(), \_dbus_transport_open_platform_specific(), \_dbus_transport_open_socket(), and \_dbus_transport_open_unix_socket().

## ◆ dbus_address_escape_value()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT char \* dbus_address_escape_value | ( | const char \*  | *value* | ) |  |

Escapes the given string as a value in a key=value pair for a D-Bus address.

Parameters  
|       |                     |
|-------|---------------------|
| value | the unescaped value |

<!-- -->

Returns  
newly-allocated escaped value or NULL if no memory

Definition at line 588 of file dbus-address.c.

References \_dbus_address_append_escaped(), \_dbus_string_free(), \_dbus_string_init(), \_dbus_string_init_const(), \_dbus_string_steal_data(), and NULL.

## ◆ dbus_address_unescape_value()

|                                                 |     |                |          |
|-------------------------------------------------|-----|----------------|----------|
| DBUS_EXPORT char \* dbus_address_unescape_value | (   | const char \*  | *value*, |
|                                                 |     | DBusError \*   | *error*  |
|                                                 | )   |                |          |

Unescapes the given string as a value in a key=value pair for a D-Bus address.

Note that dbus_address_entry_get_value() returns an already-unescaped value.

Parameters  
|       |                                      |
|-------|--------------------------------------|
| value | the escaped value                    |
| error | error to set if the unescaping fails |

<!-- -->

Returns  
newly-allocated unescaped value or NULL if no memory

Definition at line 622 of file dbus-address.c.

References \_dbus_assert, \_dbus_string_free(), \_dbus_string_get_length(), \_dbus_string_init(), \_dbus_string_init_const(), \_dbus_string_steal_data(), dbus_error_is_set(), and NULL.

## ◆ dbus_parse_address()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_parse_address | ( | const char \*  | *address*, |
|  |  | DBusAddressEntry \*\*\*  | *entry_result*, |
|  |  | int \*  | *array_len*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Parses an address string of the form:

method:key=value,key=value;method:key=value

See the D-Bus specification for complete docs on the format.

When connecting to an address, the first address entries in the semicolon-separated list should be tried first.

Parameters  
|              |                                         |
|--------------|-----------------------------------------|
| address      | the address.                            |
| entry_result | return location to an array of entries. |
| array_len    | return location for array length.       |
| error        | address where an error can be returned. |

<!-- -->

Returns  
TRUE on success, FALSE otherwise.

Definition at line 368 of file dbus-address.c.

References \_dbus_assert, \_dbus_list_append(), \_dbus_list_clear(), \_dbus_list_get_first_link(), \_dbus_list_get_length(), \_dbus_list_get_next_link, \_dbus_string_copy_len(), \_dbus_string_find(), \_dbus_string_find_to(), \_dbus_string_free(), \_dbus_string_get_length(), \_dbus_string_init(), \_dbus_string_init_const(), DBusList::data, DBUS_ERROR_BAD_ADDRESS, dbus_error_is_set(), DBUS_ERROR_NO_MEMORY, dbus_free(), dbus_new, dbus_new0, dbus_set_error(), FALSE, DBusAddressEntry::keys, DBusAddressEntry::method, NULL, TRUE, and DBusAddressEntry::values.

Referenced by dbus_server_listen().
