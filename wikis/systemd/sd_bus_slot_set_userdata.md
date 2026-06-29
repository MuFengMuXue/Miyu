## Name

sd_bus_slot_set_userdata, sd_bus_slot_get_userdata — Set and query the value in the "userdata" field

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                           |                       |
|-------------------------------------------|-----------------------|
| `void* `**`sd_bus_slot_set_userdata`**`(` | sd_bus_slot\* `slot`, |
|                                           | void\* `userdata``)`; |

 

|                                           |                          |
|-------------------------------------------|--------------------------|
| `void* `**`sd_bus_slot_get_userdata`**`(` | sd_bus_slot\* `slot``)`; |

 

## Description

The userdata pointer allows data to be passed between the point where a callback is registered, for example when a filter is added using sd_bus_add_filter(3) or an asynchronous function call is made using sd_bus_call_async(3), and the point where the callback is called, without having any global state. The pointer has type void\* and is not used by the sd-bus functions in any way, except to pass to the callback function.

Usually, the userdata field is set when the slot object is initially registered. `sd_bus_slot_set_userdata()` may be used to change it later for the bus slot object *`slot`*. Previous value of the field is returned. The argument and returned value may be `NULL`. It will be passed as the *`userdata`* argument to the callback function attached to the slot.

`sd_bus_slot_set_userdata()` gets the value of the userdata field in the bus slot object *`slot`*.

## Return Value

On success, these functions return the value of the userdata field before the function call. If the *`slot`* object is `NULL`, `NULL` will be returned to signify an error, but this is not distinguishable from the userdata field value being `NULL`.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_slot_set_userdata()` and `sd_bus_slot_get_userdata()` were added in version 240.

## See Also

systemd(1), sd-bus(3), sd_bus_slot_set_destroy_callback(3), sd_bus_add_match(3), sd_bus_slot_get_current_userdata(3)
