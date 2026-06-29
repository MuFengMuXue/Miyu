Error reporting

D-Bus low-level public API

Error reporting. More...

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
<td class="memItemRight" data-valign="bottom">DBusError</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Object representing an exception. More...<br />
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
<td colspan="2"><h2 id="typedefs" class="groupheader"> Typedefs</h2></td>
</tr>
<tr id="r_ga568b785040bdbff30312e71811907f4b" class="memitem:ga568b785040bdbff30312e71811907f4b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusError </td>
<td class="memItemRight" data-valign="bottom">DBusError</td>
</tr>
<tr class="memdesc:ga568b785040bdbff30312e71811907f4b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Mostly-opaque type representing an error that occurred.<br />
</td>
</tr>
<tr class="separator:ga568b785040bdbff30312e71811907f4b">
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
<tr id="r_ga8937f0b7cdf8554fa6305158ce453fbe" class="memitem:ga8937f0b7cdf8554fa6305158ce453fbe">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_error_init (DBusError *error)</td>
</tr>
<tr class="memdesc:ga8937f0b7cdf8554fa6305158ce453fbe">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initializes a DBusError structure.<br />
</td>
</tr>
<tr class="separator:ga8937f0b7cdf8554fa6305158ce453fbe">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaac6c14ead14829ee4e090f39de6a7568" class="memitem:gaac6c14ead14829ee4e090f39de6a7568">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_error_free (DBusError *error)</td>
</tr>
<tr class="memdesc:gaac6c14ead14829ee4e090f39de6a7568">
<td class="mdescLeft"> </td>
<td class="mdescRight">Frees an error that's been set (or just initialized), then reinitializes the error as in dbus_error_init().<br />
</td>
</tr>
<tr class="separator:gaac6c14ead14829ee4e090f39de6a7568">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3cc15cc37bcd3aaca87aa4d791c124f5" class="memitem:ga3cc15cc37bcd3aaca87aa4d791c124f5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_set_error_const (DBusError *error, const char *name, const char *message)</td>
</tr>
<tr class="memdesc:ga3cc15cc37bcd3aaca87aa4d791c124f5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Assigns an error name and message to a DBusError.<br />
</td>
</tr>
<tr class="separator:ga3cc15cc37bcd3aaca87aa4d791c124f5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0a27fb9f1af0c2bfd105d7e8622b93f4" class="memitem:ga0a27fb9f1af0c2bfd105d7e8622b93f4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_move_error (DBusError *src, DBusError *dest)</td>
</tr>
<tr class="memdesc:ga0a27fb9f1af0c2bfd105d7e8622b93f4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Moves an error src into dest, freeing src and overwriting dest.<br />
</td>
</tr>
<tr class="separator:ga0a27fb9f1af0c2bfd105d7e8622b93f4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga48515c580199514026542fe053ef1887" class="memitem:ga48515c580199514026542fe053ef1887">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_error_has_name (const DBusError *error, const char *name)</td>
</tr>
<tr class="memdesc:ga48515c580199514026542fe053ef1887">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks whether the error is set and has the given name.<br />
</td>
</tr>
<tr class="separator:ga48515c580199514026542fe053ef1887">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab0ed62e9fc2685897eb2d41467c89405" class="memitem:gab0ed62e9fc2685897eb2d41467c89405">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_error_is_set (const DBusError *error)</td>
</tr>
<tr class="memdesc:gab0ed62e9fc2685897eb2d41467c89405">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks whether an error occurred (the error is set).<br />
</td>
</tr>
<tr class="separator:gab0ed62e9fc2685897eb2d41467c89405">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga89d2ad4bde21f9e0057fac07a79885e3" class="memitem:ga89d2ad4bde21f9e0057fac07a79885e3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_set_error (DBusError *error, const char *name, const char *format,...)</td>
</tr>
<tr class="memdesc:ga89d2ad4bde21f9e0057fac07a79885e3">
<td class="mdescLeft"> </td>
<td class="mdescRight">Assigns an error name and message to a DBusError.<br />
</td>
</tr>
<tr class="separator:ga89d2ad4bde21f9e0057fac07a79885e3">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac851d8d26d52aa02fe862014f18992b6" class="memitem:gac851d8d26d52aa02fe862014f18992b6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_set_error_valist (DBusError *error, const char *name, const char *format, va_list args)</td>
</tr>
<tr class="separator:gac851d8d26d52aa02fe862014f18992b6">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Error reporting.

Types and functions related to reporting errors.

In essence D-Bus error reporting works as follows:

DBusError error;

dbus_error_init (&error);

dbus_some_function (arg1, arg2, &error);

if (dbus_error_is_set (&error))

{

fprintf (stderr, "an error occurred: %s\n", error.message);

dbus_error_free (&error);

}

dbus_error_init

void dbus_error_init(DBusError \*error)

Initializes a DBusError structure.

**Definition** dbus-errors.c:190

dbus_error_free

void dbus_error_free(DBusError \*error)

Frees an error that's been set (or just initialized), then reinitializes the error as in dbus_error_i...

**Definition** dbus-errors.c:213

dbus_error_is_set

dbus_bool_t dbus_error_is_set(const DBusError \*error)

Checks whether an error occurred (the error is set).

**Definition** dbus-errors.c:331

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusError::message

const char \* message

public error message field

**Definition** dbus-errors.h:53

By convention, all functions allow NULL instead of a DBusError\*, so callers who don't care about the error can ignore it.

There are some rules. An error passed to a D-Bus function must always be unset; you can't pass in an error that's already set. If a function has a return code indicating whether an error occurred, and also a DBusError parameter, then the error will always be set if and only if the return code indicates an error occurred. i.e. the return code and the error are never going to disagree.

An error only needs to be freed if it's been set, not if it's merely been initialized.

You can check the specific error that occurred using dbus_error_has_name().

Errors will not be set for programming errors, such as passing invalid arguments to the libdbus API. Instead, libdbus will print warnings, exit on a failed assertion, or even crash in those cases (in other words, incorrect use of the API results in undefined behavior, possibly accompanied by helpful debugging output if you're lucky).

## Typedef Documentation

## ◆ DBusError

|                                    |
|------------------------------------|
| typedef struct DBusError DBusError |

Mostly-opaque type representing an error that occurred.

Definition at line 45 of file dbus-errors.h.

## Function Documentation

## ◆ \_dbus_set_error_valist()

|                              |     |                |           |
|------------------------------|-----|----------------|-----------|
| void \_dbus_set_error_valist | (   | DBusError \*   | *error*,  |
|                              |     | const char \*  | *name*,   |
|                              |     | const char \*  | *format*, |
|                              |     | va_list        | *args*    |
|                              | )   |                |           |

Definition at line 376 of file dbus-errors.c.

## ◆ dbus_error_free()

|                                  |     |               |         |     |     |
|----------------------------------|-----|---------------|---------|-----|-----|
| DBUS_EXPORT void dbus_error_free | (   | DBusError \*  | *error* | )   |     |

Frees an error that's been set (or just initialized), then reinitializes the error as in dbus_error_init().

Parameters  
|       |                                   |
|-------|-----------------------------------|
| error | memory where the error is stored. |

Definition at line 213 of file dbus-errors.c.

References DBusRealError::const_message, dbus_error_init(), dbus_free(), DBusRealError::message, DBusRealError::name, and NULL.

Referenced by \_dbus_generate_uuid(), \_dbus_keyring_new_for_credentials(), \_dbus_listen_tcp_socket(), \_dbus_read_local_machine_uuid(), \_dbus_read_uuid_file(), \_dbus_resolve_pid_fd(), \_dbus_transport_open_platform_specific(), dbus_connection_register_fallback(), dbus_connection_register_object_path(), dbus_get_local_machine_id(), dbus_move_error(), and dbus_server_listen().

## ◆ dbus_error_has_name()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_error_has_name | ( | const DBusError \*  | *error*, |
|  |  | const char \*  | *name*  |
|  | ) |  |  |

Checks whether the error is set and has the given name.

Parameters  
|       |           |
|-------|-----------|
| error | the error |
| name  | the name  |

<!-- -->

Returns  
TRUE if the given named error occurred

Definition at line 304 of file dbus-errors.c.

References \_dbus_assert, \_dbus_string_equal(), \_dbus_string_init_const(), FALSE, DBusError::message, DBusError::name, and NULL.

Referenced by \_dbus_read_uuid_file(), dbus_connection_register_fallback(), dbus_connection_register_object_path(), and dbus_get_local_machine_id().

## ◆ dbus_error_init()

|                                  |     |               |         |     |     |
|----------------------------------|-----|---------------|---------|-----|-----|
| DBUS_EXPORT void dbus_error_init | (   | DBusError \*  | *error* | )   |     |

Initializes a DBusError structure.

Does not allocate any memory; the error only needs to be freed if it is set at some point.

Parameters  
|       |                |
|-------|----------------|
| error | the DBusError. |

Definition at line 190 of file dbus-errors.c.

References DBusRealError::const_message, DBusRealError::message, DBusRealError::name, NULL, and TRUE.

Referenced by \_dbus_generate_uuid(), \_dbus_keyring_new_for_credentials(), \_dbus_listen_tcp_socket(), dbus_error_free(), and dbus_move_error().

## ◆ dbus_error_is_set()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_error_is_set | ( | const DBusError \*  | *error* | ) |  |

Checks whether an error occurred (the error is set).

Parameters  
|       |                  |
|-------|------------------|
| error | the error object |

<!-- -->

Returns  
TRUE if an error occurred

Definition at line 331 of file dbus-errors.c.

References \_dbus_assert, FALSE, DBusError::message, DBusError::name, and NULL.

Referenced by \_dbus_read_credentials_socket(), \_dbus_server_new_for_socket(), \_dbus_transport_open(), \_dbus_transport_open_platform_specific(), \_dbus_write_pid_to_file_and_pipe(), dbus_address_unescape_value(), dbus_parse_address(), and dbus_server_listen().

## ◆ dbus_move_error()

|                                  |     |               |         |
|----------------------------------|-----|---------------|---------|
| DBUS_EXPORT void dbus_move_error | (   | DBusError \*  | *src*,  |
|                                  |     | DBusError \*  | *dest*  |
|                                  | )   |               |         |

Moves an error src into dest, freeing src and overwriting dest.

Both src and dest must be initialized. src is reinitialized to an empty error. dest may not contain an existing error. If the destination is NULL, just frees and reinits the source error.

Parameters  
|      |                               |
|------|-------------------------------|
| src  | the source error              |
| dest | the destination error or NULL |

Definition at line 281 of file dbus-errors.c.

References dbus_error_free(), and dbus_error_init().

Referenced by \_dbus_read_uuid_file(), \_dbus_transport_open(), \_dbus_transport_open_platform_specific(), and dbus_server_listen().

## ◆ dbus_set_error()

|                                 |     |                |           |
|---------------------------------|-----|----------------|-----------|
| DBUS_EXPORT void dbus_set_error | (   | DBusError \*   | *error*,  |
|                                 |     | const char \*  | *name*,   |
|                                 |     | const char \*  | *format*, |
|                                 |     |                | *...*     |
|                                 | )   |                |           |

Assigns an error name and message to a DBusError.

Does nothing if error is NULL.

The format may be NULL, which means a (pretty much useless) default message will be deduced from the name. This is not a good idea, just go ahead and provide a useful error message. It won't hurt you.

If no memory can be allocated for the error message, an out-of-memory error message will be set instead.

Parameters  
|        |                             |
|--------|-----------------------------|
| error  | the error.or NULL           |
| name   | the error name              |
| format | printf-style format string. |

Definition at line 356 of file dbus-errors.c.

References NULL.

Referenced by \_dbus_append_address_from_socket(), \_dbus_babysitter_set_child_exit_error(), \_dbus_become_daemon(), \_dbus_change_to_daemon_user(), \_dbus_check_dir_is_private_to_user(), \_dbus_close(), \_dbus_close_socket(), \_dbus_command_for_pid(), \_dbus_connect_exec(), \_dbus_connect_unix_socket(), \_dbus_create_directory(), \_dbus_create_file_exclusively(), \_dbus_credentials_add_from_user(), \_dbus_delete_directory(), \_dbus_delete_file(), \_dbus_directory_get_next_file(), \_dbus_directory_open(), \_dbus_dup(), \_dbus_ensure_directory(), \_dbus_file_get_contents(), \_dbus_generate_random_bytes(), \_dbus_generate_uuid(), \_dbus_get_autolaunch_address(), \_dbus_is_console_user(), \_dbus_keyring_new_for_credentials(), \_dbus_listen_systemd_sockets(), \_dbus_listen_tcp_socket(), \_dbus_listen_unix_socket(), \_dbus_lookup_launchd_socket(), \_dbus_make_file_world_readable(), \_dbus_message_iter_get_args_valist(), \_dbus_object_tree_register(), \_dbus_read_credentials_socket(), \_dbus_read_local_machine_uuid(), \_dbus_send_credentials_socket(), \_dbus_server_listen_unix_socket(), \_dbus_server_new_for_domain_socket(), \_dbus_server_new_for_launchd(), \_dbus_server_new_for_tcp_socket(), \_dbus_set_bad_address(), \_dbus_set_socket_nonblocking(), \_dbus_socketpair(), \_dbus_spawn_async_with_babysitter(), \_dbus_stat(), \_dbus_string_save_to_file(), \_dbus_transport_new_for_domain_socket(), \_dbus_transport_new_for_tcp_socket(), \_dbus_transport_open_platform_specific(), \_dbus_user_database_lookup(), \_dbus_user_database_lookup_group(), \_dbus_write_pid_to_file_and_pipe(), dbus_connection_send_with_reply_and_block(), dbus_message_demarshal(), dbus_parse_address(), dbus_server_listen(), dbus_set_error_from_message(), dbus_signature_validate(), dbus_signature_validate_single(), dbus_try_get_local_machine_id(), dbus_validate_bus_name(), dbus_validate_error_name(), dbus_validate_interface(), dbus_validate_member(), dbus_validate_path(), and dbus_validate_utf8().

## ◆ dbus_set_error_const()

|                                       |     |                |            |
|---------------------------------------|-----|----------------|------------|
| DBUS_EXPORT void dbus_set_error_const | (   | DBusError \*   | *error*,   |
|                                       |     | const char \*  | *name*,    |
|                                       |     | const char \*  | *message*  |
|                                       | )   |                |            |

Assigns an error name and message to a DBusError.

Does nothing if error is NULL. The message may be NULL, which means a default message will be deduced from the name. The default message will be totally useless, though, so using a NULL message is not recommended.

Because this function does not copy the error name or message, you must ensure the name and message are global data that won't be freed. You probably want dbus_set_error() instead, in most cases.

Parameters  
|         |                                   |
|---------|-----------------------------------|
| error   | the error or NULL                 |
| name    | the error name (not copied!!!)    |
| message | the error message (not copied!!!) |

Definition at line 245 of file dbus-errors.c.

References \_dbus_assert, DBusRealError::const_message, DBusRealError::message, DBusError::message, DBusRealError::name, DBusError::name, NULL, and TRUE.

Referenced by \_dbus_get_autolaunch_address(), \_dbus_keyring_get_best_key(), \_dbus_keyring_new_for_credentials(), \_dbus_listen_systemd_sockets(), and \_dbus_lookup_launchd_socket().
