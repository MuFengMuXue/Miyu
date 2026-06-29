Memory Allocation

D-Bus low-level public API

dbus_malloc(), dbus_free(), etc. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="macros" class="groupheader"> Macros</h2></td>
</tr>
<tr id="r_ga54ccb556e7964112a825a7f46c156ca0" class="memitem:ga54ccb556e7964112a825a7f46c156ca0">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">dbus_new(type, count)   ((type*)dbus_malloc (sizeof (type) * (count)))</td>
</tr>
<tr class="memdesc:ga54ccb556e7964112a825a7f46c156ca0">
<td class="mdescLeft"> </td>
<td class="mdescRight">Safe macro for using dbus_malloc().<br />
</td>
</tr>
<tr class="separator:ga54ccb556e7964112a825a7f46c156ca0">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaba9d823abda7f4cadbaf5177d3b8b793" class="memitem:gaba9d823abda7f4cadbaf5177d3b8b793">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">dbus_new0(type, count)   ((type*)dbus_malloc0 (sizeof (type) * (count)))</td>
</tr>
<tr class="memdesc:gaba9d823abda7f4cadbaf5177d3b8b793">
<td class="mdescLeft"> </td>
<td class="mdescRight">Safe macro for using dbus_malloc0().<br />
</td>
</tr>
<tr class="separator:gaba9d823abda7f4cadbaf5177d3b8b793">
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
<tr id="r_ga061bcded226d76c7d7de35beaa165cb5" class="memitem:ga061bcded226d76c7d7de35beaa165cb5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef void(* </td>
<td class="memItemRight" data-valign="bottom">DBusFreeFunction) (void *memory)</td>
</tr>
<tr class="memdesc:ga061bcded226d76c7d7de35beaa165cb5">
<td class="mdescLeft"> </td>
<td class="mdescRight">The type of a function which frees a block of memory.<br />
</td>
</tr>
<tr class="separator:ga061bcded226d76c7d7de35beaa165cb5">
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
<tr id="r_gaf6e588659067a854c3cca7ebe8ae5084" class="memitem:gaf6e588659067a854c3cca7ebe8ae5084">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">dbus_malloc (size_t bytes)</td>
</tr>
<tr class="memdesc:gaf6e588659067a854c3cca7ebe8ae5084">
<td class="mdescLeft"> </td>
<td class="mdescRight">Allocates the given number of bytes, as with standard malloc().<br />
</td>
</tr>
<tr class="separator:gaf6e588659067a854c3cca7ebe8ae5084">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa02722b030a091f6c14c4cb11a593623" class="memitem:gaa02722b030a091f6c14c4cb11a593623">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">dbus_malloc0 (size_t bytes)</td>
</tr>
<tr class="memdesc:gaa02722b030a091f6c14c4cb11a593623">
<td class="mdescLeft"> </td>
<td class="mdescRight">Allocates the given number of bytes, as with standard malloc(), but all bytes are initialized to zero as with calloc().<br />
</td>
</tr>
<tr class="separator:gaa02722b030a091f6c14c4cb11a593623">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga472f43a4ff4a97848bf4e0bff4af5b18" class="memitem:ga472f43a4ff4a97848bf4e0bff4af5b18">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">dbus_realloc (void *memory, size_t bytes)</td>
</tr>
<tr class="memdesc:ga472f43a4ff4a97848bf4e0bff4af5b18">
<td class="mdescLeft"> </td>
<td class="mdescRight">Resizes a block of memory previously allocated by dbus_malloc() or dbus_malloc0().<br />
</td>
</tr>
<tr class="separator:ga472f43a4ff4a97848bf4e0bff4af5b18">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga34e666b19b015035a9a31e53da84b39a" class="memitem:ga34e666b19b015035a9a31e53da84b39a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_free (void *memory)</td>
</tr>
<tr class="memdesc:ga34e666b19b015035a9a31e53da84b39a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Frees a block of memory previously allocated by dbus_malloc() or dbus_malloc0().<br />
</td>
</tr>
<tr class="separator:ga34e666b19b015035a9a31e53da84b39a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac200b2dbc8b3f6ecac4d42426fb97b40" class="memitem:gac200b2dbc8b3f6ecac4d42426fb97b40">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_free_string_array (char **str_array)</td>
</tr>
<tr class="memdesc:gac200b2dbc8b3f6ecac4d42426fb97b40">
<td class="mdescLeft"> </td>
<td class="mdescRight">Frees a NULL-terminated array of strings.<br />
</td>
</tr>
<tr class="separator:gac200b2dbc8b3f6ecac4d42426fb97b40">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga01912903e39428872920d861ef565bac" class="memitem:ga01912903e39428872920d861ef565bac">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_shutdown (void)</td>
</tr>
<tr class="memdesc:ga01912903e39428872920d861ef565bac">
<td class="mdescLeft"> </td>
<td class="mdescRight">Frees all memory allocated internally by libdbus and reverses the effects of dbus_threads_init().<br />
</td>
</tr>
<tr class="separator:ga01912903e39428872920d861ef565bac">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

dbus_malloc(), dbus_free(), etc.

Functions and macros related to allocating and releasing blocks of memory.

## Macro Definition Documentation

## ◆ dbus_new

|  |  |  |  |
|----|----|----|----|
| \#define dbus_new | ( |   | type, |
|  |  |   | count  |
|  | ) |  |    ((type\*)dbus_malloc (sizeof (type) \* (count))) |

Safe macro for using dbus_malloc().

Accepts the type to allocate and the number of type instances to allocate as arguments, and returns a memory block cast to the desired type, instead of as a void\*.

Parameters  
|       |                                            |
|-------|--------------------------------------------|
| type  | type name to allocate                      |
| count | number of instances in the allocated array |

<!-- -->

Returns  
the new memory block or NULL on failure

Definition at line 59 of file dbus-memory.h.

## ◆ dbus_new0

|  |  |  |  |
|----|----|----|----|
| \#define dbus_new0 | ( |   | type, |
|  |  |   | count  |
|  | ) |  |    ((type\*)dbus_malloc0 (sizeof (type) \* (count))) |

Safe macro for using dbus_malloc0().

Accepts the type to allocate and the number of type instances to allocate as arguments, and returns a memory block cast to the desired type, instead of as a void\*. The allocated array is initialized to all-bits-zero.

Parameters  
|       |                                            |
|-------|--------------------------------------------|
| type  | type name to allocate                      |
| count | number of instances in the allocated array |

<!-- -->

Returns  
the new memory block or NULL on failure

Definition at line 60 of file dbus-memory.h.

## Typedef Documentation

## ◆ DBusFreeFunction

|                  |
|------------------|
| DBusFreeFunction |

The type of a function which frees a block of memory.

Parameters  
|        |                    |
|--------|--------------------|
| memory | the memory to free |

Definition at line 65 of file dbus-memory.h.

## Function Documentation

## ◆ dbus_free()

|                            |     |          |          |     |     |
|----------------------------|-----|----------|----------|-----|-----|
| DBUS_EXPORT void dbus_free | (   | void \*  | *memory* | )   |     |

Frees a block of memory previously allocated by dbus_malloc() or dbus_malloc0().

If passed NULL, does nothing.

Parameters  
|        |                   |
|--------|-------------------|
| memory | block to be freed |

Definition at line 710 of file dbus-memory.c.

References \_dbus_assert, \_dbus_atomic_dec(), and TRUE.

Referenced by \_dbus_auth_unref(), \_dbus_babysitter_unref(), \_dbus_connection_new_for_transport(), \_dbus_counter_new(), \_dbus_counter_unref(), \_dbus_credentials_add_adt_audit_data(), \_dbus_credentials_add_linux_security_label(), \_dbus_credentials_add_windows_sid(), \_dbus_credentials_clear(), \_dbus_credentials_take_unix_gids(), \_dbus_credentials_unref(), \_dbus_data_slot_allocator_free(), \_dbus_data_slot_list_free(), \_dbus_directory_close(), \_dbus_directory_open(), \_dbus_group_info_free(), \_dbus_group_info_unref(), \_dbus_hash_table_new(), \_dbus_hash_table_unref(), \_dbus_keyring_unref(), \_dbus_listen_systemd_sockets(), \_dbus_listen_tcp_socket(), \_dbus_mem_pool_dealloc(), \_dbus_mem_pool_free(), \_dbus_message_loader_new(), \_dbus_message_loader_unref(), \_dbus_object_tree_new(), \_dbus_object_tree_register(), \_dbus_object_tree_unref(), \_dbus_pending_call_new_unlocked(), \_dbus_printf_string_upper_bound(), \_dbus_server_finalize_base(), \_dbus_server_init_base(), \_dbus_server_listen_platform_specific(), \_dbus_server_new_for_domain_socket(), \_dbus_server_new_for_socket(), \_dbus_server_new_for_tcp_socket(), \_dbus_set_up_transient_session_servicedirs(), \_dbus_split_paths_and_append(), \_dbus_string_free(), \_dbus_timeout_list_free(), \_dbus_timeout_unref(), \_dbus_transport_finalize_base(), \_dbus_transport_new_for_socket(), \_dbus_transport_open(), \_dbus_user_database_unref(), \_dbus_user_info_free(), \_dbus_user_info_unref(), \_dbus_variant_read(), \_dbus_watch_list_free(), \_dbus_watch_unref(), dbus_address_entries_free(), dbus_connection_free_preallocated_send(), dbus_error_free(), dbus_free_string_array(), dbus_message_copy(), dbus_parse_address(), dbus_realloc(), and dbus_shutdown().

## ◆ dbus_free_string_array()

|                                         |     |            |             |     |     |
|-----------------------------------------|-----|------------|-------------|-----|-----|
| DBUS_EXPORT void dbus_free_string_array | (   | char \*\*  | *str_array* | )   |     |

Frees a NULL-terminated array of strings.

If passed NULL, does nothing.

Parameters  
|           |                       |
|-----------|-----------------------|
| str_array | the array to be freed |

Definition at line 758 of file dbus-memory.c.

References dbus_free().

Referenced by \_dbus_auth_set_mechanisms(), \_dbus_auth_unref(), \_dbus_decompose_path(), \_dbus_dup_string_array(), \_dbus_get_environment(), \_dbus_hash_table_to_array(), \_dbus_message_iter_get_args_valist(), \_dbus_object_tree_dispatch_and_unlock(), \_dbus_server_finalize_base(), dbus_connection_get_object_path_data(), dbus_connection_list_registered(), dbus_connection_unregister_object_path(), and dbus_server_set_auth_mechanisms().

## ◆ dbus_malloc()

|                                             |     |         |         |     |     |
|---------------------------------------------|-----|---------|---------|-----|-----|
| DBUS_EXPORT DBUS_MALLOC void \* dbus_malloc | (   | size_t  | *bytes* | )   |     |

Allocates the given number of bytes, as with standard malloc().

Guaranteed to return NULL if bytes is zero on all platforms. Returns NULL if the allocation fails. The memory must be released with dbus_free().

dbus_malloc() memory is NOT safe to free with regular free() from the C library. Free it with dbus_free() only.

Parameters  
|       |                             |
|-------|-----------------------------|
| bytes | number of bytes to allocate |

<!-- -->

Returns  
allocated memory, or NULL if the allocation fails.

Definition at line 470 of file dbus-memory.c.

References \_dbus_abort(), \_dbus_atomic_inc(), \_dbus_warn(), and NULL.

Referenced by \_dbus_mem_pool_alloc(), \_dbus_memdup(), \_dbus_printf_string_upper_bound(), \_dbus_strdup(), \_dbus_string_copy_data(), and \_dbus_string_init_preallocated().

## ◆ dbus_malloc0()

|                                              |     |         |         |     |     |
|----------------------------------------------|-----|---------|---------|-----|-----|
| DBUS_EXPORT DBUS_MALLOC void \* dbus_malloc0 | (   | size_t  | *bytes* | )   |     |

Allocates the given number of bytes, as with standard malloc(), but all bytes are initialized to zero as with calloc().

Guaranteed to return NULL if bytes is zero on all platforms. Returns NULL if the allocation fails. The memory must be released with dbus_free().

dbus_malloc0() memory is NOT safe to free with regular free() from the C library. Free it with dbus_free() only.

Parameters  
|       |                             |
|-------|-----------------------------|
| bytes | number of bytes to allocate |

<!-- -->

Returns  
allocated memory, or NULL if the allocation fails.

Definition at line 540 of file dbus-memory.c.

References \_dbus_abort(), \_dbus_atomic_inc(), \_dbus_warn(), and NULL.

Referenced by \_dbus_mem_pool_alloc().

## ◆ dbus_realloc()

|                                  |     |          |           |
|----------------------------------|-----|----------|-----------|
| DBUS_EXPORT void \* dbus_realloc | (   | void \*  | *memory*, |
|                                  |     | size_t   | *bytes*   |
|                                  | )   |          |           |

Resizes a block of memory previously allocated by dbus_malloc() or dbus_malloc0().

Guaranteed to free the memory and return NULL if bytes is zero on all platforms. Returns NULL if the resize fails. If the resize fails, the memory is not freed.

Parameters  
|        |                              |
|--------|------------------------------|
| memory | block to be resized          |
| bytes  | new size of the memory block |

<!-- -->

Returns  
allocated memory, or NULL if the resize fails.

Definition at line 610 of file dbus-memory.c.

References \_dbus_abort(), \_dbus_atomic_inc(), \_dbus_warn(), dbus_free(), FALSE, and NULL.

Referenced by \_dbus_data_slot_allocator_alloc(), \_dbus_data_slot_list_set(), and \_dbus_listen_tcp_socket().

## ◆ dbus_shutdown()

|                                |     |       |     |     |     |
|--------------------------------|-----|-------|-----|-----|-----|
| DBUS_EXPORT void dbus_shutdown | (   | void  |     | )   |     |

Frees all memory allocated internally by libdbus and reverses the effects of dbus_threads_init().

libdbus keeps internal global variables, for example caches and thread locks, and it can be useful to free these internal data structures.

dbus_shutdown() does NOT free memory that was returned to the application. It only frees libdbus-internal data structures.

You MUST free all memory and release all reference counts returned to you by libdbus prior to calling dbus_shutdown().

If a shared connection is open, calling dbus_shutdown() will drain its queue of messages and disconnect it. In particular, this will result in processing of the special Disconnected signal, which may result in a call to \_exit(), unless you have used dbus_connection_set_exit_on_disconnect() to disable that behaviour.

You can't continue to use any D-Bus objects, such as connections, that were allocated prior to dbus_shutdown(). You can, however, start over; call dbus_threads_init() again, create new connections, and so forth.

WARNING: dbus_shutdown() is NOT thread safe, it must be called while NO other threads are using D-Bus. (Remember, you have to free all D-Bus objects and memory before you call dbus_shutdown(), so no thread can be using libdbus.)

The purpose of dbus_shutdown() is to allow applications to get clean output from memory leak checkers. dbus_shutdown() may also be useful if you want to dlopen() libdbus instead of linking to it, and want to be able to unload the library again.

There is absolutely no requirement to call dbus_shutdown() - in fact, most applications won't bother and should not feel guilty.

You have to know that nobody is using libdbus in your application's process before you can call dbus_shutdown(). One implication of this is that calling dbus_shutdown() from a library is almost certainly wrong, since you don't know what the rest of the app is up to.

Definition at line 906 of file dbus-memory.c.

References \_dbus_current_generation, \_dbus_threads_lock_platform_specific(), \_dbus_threads_unlock_platform_specific(), ShutdownClosure::data, dbus_free(), ShutdownClosure::func, ShutdownClosure::next, and NULL.
