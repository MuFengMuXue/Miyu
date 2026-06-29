## Name

sd_bus_slot_set_floating, sd_bus_slot_get_floating — Control whether a bus slot object is "floating"

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                         |                       |
|-----------------------------------------|-----------------------|
| `int `**`sd_bus_slot_set_floating`**`(` | sd_bus_slot \*`slot`, |
|                                         | int `b``)`;           |

 

|                                         |                          |
|-----------------------------------------|--------------------------|
| `int `**`sd_bus_slot_get_floating`**`(` | sd_bus_slot \*`slot``)`; |

 

## Description

`sd_bus_slot_set_floating()` controls whether the specified bus slot object *`slot`* shall be "floating" or not. A floating bus slot object's lifetime is bound to the lifetime of the bus object it is associated with, meaning that it remains allocated as long as the bus object itself and is freed automatically when the bus object is freed. Regular (i.e. non-floating) bus slot objects keep the bus referenced, hence the bus object remains allocated at least as long as there remains at least one referenced bus slot object around. The floating state hence controls the direction of referencing between the bus object and the bus slot objects: if floating the bus pins the bus slot, and otherwise the bus slot pins the bus objects. Use `sd_bus_slot_set_floating()` to switch between both modes: if the *`b`* parameter is zero, the slot object is made into a regular (non-floating) slot object, otherwise it is made into a floating slot object.

Bus slot objects may be allocated with calls such as sd_bus_add_match(3). If the *`slot`* of these functions is non-`NULL` the slot object will be of the regular kind (i.e. non-floating), otherwise it will be created floating. With `sd_bus_slot_set_floating()` a bus slot object allocated as regular can be converted into a floating object and back. This is particularly useful for creating a bus slot object, then changing parameters of it, and then turning it into a floating object, whose lifecycle is managed by the bus object.

`sd_bus_slot_get_floating()` returns the current floating state of the specified bus slot object. It returns negative on error, zero if the bus slot object is a regular (non-floating) object and positive otherwise.

## Return Value

On success, these functions return 0 or a positive integer. On failure, they return a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
The *`slot`* parameter is `NULL`.

`-ECHILD`  
The bus connection has been created in a different process, library or module instance.

`-ESTALE`  
The bus object the specified bus slot object is associated with has already been freed, and hence no change in the floating state can be made anymore.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_slot_set_floating()` and `sd_bus_slot_get_floating()` were added in version 239.

## See Also

systemd(1), sd-bus(3), sd_bus_slot_set_destroy_callback(3), sd_bus_add_match(3)
