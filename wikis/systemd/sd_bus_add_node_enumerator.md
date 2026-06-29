## Name

sd_bus_add_node_enumerator — Add a node enumerator for a D-Bus object path prefix

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|  |  |
|----|----|
| `typedef int (*`**`sd_bus_node_enumerator_t`**`)(` | sd_bus \*`bus`, |
|   | const char \*`prefix`, |
|   | void \*`userdata`, |
|   | char \*\*\*`ret_nodes`, |
|   | sd_bus_error \*`ret_error``)`; |

 

|  |  |
|----|----|
| `int `**`sd_bus_add_node_enumerator`**`(` | sd_bus \*`bus`, |
|   | sd_bus_slot \*\*`slot`, |
|   | const char \*`path`, |
|   | sd_bus_node_enumerator_t `callback`, |
|   | void \*`userdata``)`; |

 

## Description

`sd_bus_add_node_enumerator()` adds a D-Bus node enumerator for the given path prefix. The given callback is called to enumerate all the available objects with the given path prefix when required (e.g. when `org.freedesktop.DBus.Introspectable.Introspect` or `org.freedesktop.DBus.ObjectManager.GetManagedObjects` are called on a D-Bus service managed by sd-bus).

*`callback`* is called with the path and userdata pointer registered with `sd_bus_add_node_enumerator()`. When called, it should store all the child object paths of the given path prefix in *`ret_nodes`* with a NULL terminator item. The callback should return a non-negative value on success. If an error occurs, it can either return a negative integer, set *`ret_error`* to a non-empty error or do both. Any errors returned by the callback are encoded as D-Bus errors and sent back to the caller. Errors in *`ret_error`* take priority over negative return values.

Note that a node enumerator callback will only ever be called for a single path prefix and hence, for normal operation, *`prefix`* can be ignored. Also, a node enumerator is only used to enumerate the available child objects under a given prefix. To install a handler for a set of dynamic child objects, use sd_bus_add_fallback_vtable(3).

When `sd_bus_add_node_enumerator()` succeeds, a slot is created internally. If the output parameter *`slot`* is `NULL`, a "floating" slot object is created, see sd_bus_slot_set_floating(3). Otherwise, a pointer to the slot object is returned. In that case, the reference to the slot object should be dropped when the node enumerator is not needed anymore, see sd_bus_slot_unref(3).

## Return Value

On success, `sd_bus_add_node_enumerator()` returns a non-negative integer. On failure, it returns a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
One of the required parameters is `NULL` or *`path`* is not a valid object path.

`-ENOPKG`  
The bus cannot be resolved.

`-ECHILD`  
The bus was created in a different process, library or module instance.

`-ENOMEM`  
Memory allocation failed.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_node_enumerator_t()` and `sd_bus_add_node_enumerator()` were added in version 221.

## See Also

sd-bus(3), busctl(1), sd_bus_add_fallback_vtable(3), sd_bus_slot_unref(3)
