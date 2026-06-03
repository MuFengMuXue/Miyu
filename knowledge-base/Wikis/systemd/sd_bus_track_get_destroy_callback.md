## Name

sd_bus_slot_set_destroy_callback, sd_bus_slot_get_destroy_callback, sd_bus_track_set_destroy_callback, sd_bus_track_get_destroy_callback, sd_bus_destroy_t — Define the callback function for resource cleanup

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                            |                       |
|--------------------------------------------|-----------------------|
| `typedef int (*`**`sd_bus_destroy_t`**`)(` | void \*`userdata``)`; |

 

|  |  |
|----|----|
| `int `**`sd_bus_slot_set_destroy_callback`**`(` | sd_bus_slot \*`slot`, |
|   | sd_bus_destroy_t `callback``)`; |

 

|  |  |
|----|----|
| `int `**`sd_bus_slot_get_destroy_callback`**`(` | sd_bus_slot \*`slot`, |
|   | sd_bus_destroy_t \*`callback``)`; |

 

|  |  |
|----|----|
| `int `**`sd_bus_track_set_destroy_callback`**`(` | sd_bus_track \*`track`, |
|   | sd_bus_destroy_t `callback``)`; |

 

|  |  |
|----|----|
| `int `**`sd_bus_track_get_destroy_callback`**`(` | sd_bus_track \*`track`, |
|   | sd_bus_destroy_t \*`callback``)`; |

 

## Description

`sd_bus_slot_set_destroy_callback()` sets *`callback`* as the callback function to be called right before the bus slot object *`slot`* is deallocated. The *`userdata`* pointer from the slot object will be passed as the *`userdata`* parameter. This pointer can be set by an argument to the constructor functions, see sd_bus_add_match(3), or directly, see sd_bus_slot_set_userdata(3). This callback function is called even if *`userdata`* is `NULL`. Note that this callback is invoked at a time where the bus slot object itself is already invalidated, and executing operations or taking new references to the bus slot object is not permissible.

`sd_bus_slot_get_destroy_callback()` returns the current callback for *`slot`* in the *`callback`* parameter.

`sd_bus_track_set_destroy_callback()` and `sd_bus_track_get_destroy_callback()` provide equivalent functionality for the *`userdata`* pointer associated with bus peer tracking objects. For details about bus peer tracking objects, see sd_bus_track_new(3).

## Return Value

On success, `sd_bus_slot_set_destroy_callback()` and `sd_bus_track_set_destroy_callback()` return 0 or a positive integer. On failure, they return a negative errno-style error code.

`sd_bus_slot_get_destroy_callback()` and `sd_bus_track_get_destroy_callback()` return positive if the destroy callback function is set, 0 if not. On failure, they return a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
The *`slot`* or *`track`* parameter is `NULL`.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_destroy_t()`, `sd_bus_slot_set_destroy_callback()`, `sd_bus_slot_get_destroy_callback()`, `sd_bus_track_set_destroy_callback()`, and `sd_bus_track_get_destroy_callback()` were added in version 239.

## See Also

systemd(1), sd-bus(3), sd_bus_slot_set_floating(3), sd_bus_add_match(3), sd_bus_track_new(3), sd_bus_slot_set_userdata(3), sd_bus_track_set_userdata(3)
