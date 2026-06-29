## Name

sd_bus_slot_set_description, sd_bus_slot_get_description — Set or query the description of bus slot objects

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                            |                                |
|--------------------------------------------|--------------------------------|
| `int `**`sd_bus_slot_set_description`**`(` | sd_bus_slot\* `slot`,          |
|                                            | const char \*`description``)`; |

 

|  |  |
|----|----|
| `int `**`sd_bus_slot_get_description`**`(` | sd_bus_slot\* `bus`, |
|   | const char \*\*`description``)`; |

 

## Description

`sd_bus_slot_set_description()` sets the description string that is used in logging to the specified string. The string is copied internally and freed when the bus slot object is deallocated. The *`description`* argument may be `NULL`, in which case the description is unset.

`sd_bus_slot_get_description()` returns a description string in *`description`*. If the string is not set, e.g. with `sd_bus_slot_set_description()`, and the slot is a bus match callback slot, the match string will be returned. Otherwise, `-ENXIO` is returned.

## Return Value

On success, these functions return 0 or a positive integer. On failure, they return a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
An required argument is `NULL`.

`-ENXIO`  
The bus slot object has no description.

`-ENOMEM`  
Memory allocation failed.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_slot_set_description()` and `sd_bus_slot_get_description()` were added in version 240.

## See Also

systemd(1), sd-bus(3), sd_bus_slot_ref(3), sd_bus_slot_set_userdata(3)
