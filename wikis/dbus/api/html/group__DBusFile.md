DBusFile

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="functions" class="groupheader"> Functions</h2></td>
</tr>
<tr id="r_ga13a527e32c05b63e8b32a63d728e20e8" class="memitem:ga13a527e32c05b63e8b32a63d728e20e8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_file_exists (const char *file)</td>
</tr>
<tr class="memdesc:ga13a527e32c05b63e8b32a63d728e20e8">
<td class="mdescLeft"> </td>
<td class="mdescRight">File interface.<br />
</td>
</tr>
<tr class="separator:ga13a527e32c05b63e8b32a63d728e20e8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac3e1528df1b668ce17375af0913936cd" class="memitem:gac3e1528df1b668ce17375af0913936cd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_file_get_contents (DBusString *str, const DBusString *filename, DBusError *error)</td>
</tr>
<tr class="memdesc:gac3e1528df1b668ce17375af0913936cd">
<td class="mdescLeft"> </td>
<td class="mdescRight">Appends the contents of the given file to the string, returning error code.<br />
</td>
</tr>
<tr class="separator:gac3e1528df1b668ce17375af0913936cd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2adba123fde18c9d1d9eaf1347980d57" class="memitem:ga2adba123fde18c9d1d9eaf1347980d57">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_save_to_file (const DBusString *str, const DBusString *filename, dbus_bool_t world_readable, DBusError *error)</td>
</tr>
<tr class="memdesc:ga2adba123fde18c9d1d9eaf1347980d57">
<td class="mdescLeft"> </td>
<td class="mdescRight">Writes a string out to a file.<br />
</td>
</tr>
<tr class="separator:ga2adba123fde18c9d1d9eaf1347980d57">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7c83e2e20811330d1d1b2f6249dbe66c" class="memitem:ga7c83e2e20811330d1d1b2f6249dbe66c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_make_file_world_readable (const DBusString *filename, DBusError *error)</td>
</tr>
<tr class="memdesc:ga7c83e2e20811330d1d1b2f6249dbe66c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Makes the file readable by every user in the system.<br />
</td>
</tr>
<tr class="separator:ga7c83e2e20811330d1d1b2f6249dbe66c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga22665c6d5899c913e03930f90d144f46" class="memitem:ga22665c6d5899c913e03930f90d144f46">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_create_file_exclusively (const DBusString *filename, DBusError *error)</td>
</tr>
<tr class="memdesc:ga22665c6d5899c913e03930f90d144f46">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates the given file, failing if the file already exists.<br />
</td>
</tr>
<tr class="separator:ga22665c6d5899c913e03930f90d144f46">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga17a2449bc1864a9cb4a3666ac2c4fe78" class="memitem:ga17a2449bc1864a9cb4a3666ac2c4fe78">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_delete_file (const DBusString *filename, DBusError *error)</td>
</tr>
<tr class="memdesc:ga17a2449bc1864a9cb4a3666ac2c4fe78">
<td class="mdescLeft"> </td>
<td class="mdescRight">Deletes the given file.<br />
</td>
</tr>
<tr class="separator:ga17a2449bc1864a9cb4a3666ac2c4fe78">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

## Function Documentation

## ◆ \_dbus_create_file_exclusively()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_create_file_exclusively | ( | const DBusString \*  | *filename*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Creates the given file, failing if the file already exists.

Parameters  
|          |                |
|----------|----------------|
| filename | the filename   |
| error    | error location |

<!-- -->

Returns  
TRUE if we created the file and it didn't exist

Definition at line 395 of file dbus-file-unix.c.

References \_dbus_close(), \_dbus_string_get_const_data(), DBUS_ERROR_FAILED, dbus_set_error(), FALSE, NULL, and TRUE.

## ◆ \_dbus_delete_file()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_delete_file | ( | const DBusString \*  | *filename*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Deletes the given file.

Parameters  
|          |                |
|----------|----------------|
| filename | the filename   |
| error    | error location |

<!-- -->

Returns  
TRUE if unlink() succeeded

Definition at line 441 of file dbus-file-unix.c.

References \_dbus_strerror_from_errno(), \_dbus_string_get_const_data(), DBUS_ERROR_FAILED, dbus_set_error(), FALSE, and TRUE.

## ◆ \_dbus_file_exists()

|                                |     |                |        |     |     |
|--------------------------------|-----|----------------|--------|-----|-----|
| dbus_bool_t \_dbus_file_exists | (   | const char \*  | *file* | )   |     |

File interface.

File interface.

Parameters  
|      |                       |
|------|-----------------------|
| file | full path to the file |

<!-- -->

Returns  
TRUE if file exists

Definition at line 564 of file dbus-sysdeps-util-unix.c.

References FALSE, and TRUE.

## ◆ \_dbus_file_get_contents()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_file_get_contents | ( | DBusString \*  | *str*, |
|  |  | const DBusString \*  | *filename*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Appends the contents of the given file to the string, returning error code.

At the moment, won't open a file more than a megabyte in size.

Parameters  
|          |                         |
|----------|-------------------------|
| str      | the string to append to |
| filename | filename to load        |
| error    | place to set an error   |

<!-- -->

Returns  
FALSE if error was set

Definition at line 63 of file dbus-file-unix.c.

References \_dbus_close(), \_dbus_error_from_errno(), \_dbus_read(), \_dbus_string_get_const_data(), \_dbus_string_get_length(), \_dbus_string_set_length(), DBUS_ERROR_FAILED, dbus_set_error(), FALSE, NULL, and TRUE.

Referenced by \_dbus_resolve_pid_fd().

## ◆ \_dbus_make_file_world_readable()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_make_file_world_readable | ( | const DBusString \*  | *filename*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Makes the file readable by every user in the system.

Parameters  
|          |                |
|----------|----------------|
| filename | the filename   |
| error    | error location |

<!-- -->

Returns  
TRUE if the file's permissions could be changed.

Definition at line 368 of file dbus-file-unix.c.

References \_dbus_string_get_const_data(), DBUS_ERROR_FAILED, dbus_set_error(), FALSE, and TRUE.

Referenced by \_dbus_string_save_to_file().

## ◆ \_dbus_string_save_to_file()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_string_save_to_file | ( | const DBusString \*  | *str*, |
|  |  | const DBusString \*  | *filename*, |
|  |  | dbus_bool_t  | *world_readable*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Writes a string out to a file.

If the file exists, it will be atomically overwritten by the new data.

Parameters  
|                |                                           |
|----------------|-------------------------------------------|
| str            | the string to write out                   |
| filename       | the file to save string to                |
| world_readable | If set, ensure the file is world readable |
| error          | error to be filled in on failure          |

<!-- -->

Returns  
FALSE on failure

If the file exists, it will be atomically overwritten by the new data.

Parameters  
|                |                                        |
|----------------|----------------------------------------|
| str            | the string to write out                |
| filename       | the file to save string to             |
| world_readable | if true, ensure file is world readable |
| error          | error to be filled in on failure       |

<!-- -->

Returns  
FALSE on failure

Definition at line 208 of file dbus-file-unix.c.

References \_dbus_close(), \_dbus_error_from_errno(), \_dbus_generate_random_ascii(), \_dbus_make_file_world_readable(), \_dbus_string_append(), \_dbus_string_copy(), \_dbus_string_free(), \_dbus_string_get_const_data(), \_dbus_string_get_length(), \_dbus_string_init(), \_dbus_write(), DBUS_ERROR_NO_MEMORY, dbus_set_error(), FALSE, NULL, and TRUE.

Referenced by \_dbus_write_uuid_file().
