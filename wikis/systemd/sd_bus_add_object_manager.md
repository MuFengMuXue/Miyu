## Name

sd_bus_add_object_manager — Add a D-Bus object manager for a D-Bus object sub-tree

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                          |                         |
|------------------------------------------|-------------------------|
| `int `**`sd_bus_add_object_manager`**`(` | sd_bus \*`bus`,         |
|                                          | sd_bus_slot \*\*`slot`, |
|                                          | const char \*`path``)`; |

 

## Description

`sd_bus_add_object_manager()` installs a handler for the given path that implements the `GetManagedObjects()` method of the `org.freedesktop.DBus.ObjectManager` interface. See org.freedesktop.DBus.ObjectManager for more information.

To implement the `InterfacesAdded` and `InterfacesRemoved` signals of the `org.freedesktop.DBus.ObjectManager` interface, call sd_bus_emit_interfaces_added(3) and sd_bus_emit_interfaces_removed(3) whenever interfaces are added or removed from the sub-tree, respectively.

When `sd_bus_add_object_manager()` succeeds, a slot is created internally. If the output parameter *`slot`* is `NULL`, a "floating" slot object is created, see sd_bus_slot_set_floating(3). Otherwise, a pointer to the slot object is returned. In that case, the reference to the slot object should be dropped when the object manager is not needed anymore, see sd_bus_slot_unref(3).

## Return Value

On success, `sd_bus_add_object_manager()` returns a non-negative integer. On failure, it returns a negative errno-style error code.

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

`sd_bus_add_object_manager()` was added in version 221.

## See Also

sd-bus(3), busctl(1), sd_bus_add_object_vtable(3), sd_bus_emit_interfaces_added(3), sd_bus_slot_unref(3)
