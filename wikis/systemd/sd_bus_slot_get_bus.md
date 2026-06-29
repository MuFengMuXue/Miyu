## Name

sd_bus_slot_get_bus, sd_bus_slot_get_current_handler, sd_bus_slot_get_current_message, sd_bus_slot_get_current_userdata — Query information attached to a bus slot object

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|  |  |
|----|----|
| `typedef int (*`**`sd_bus_message_handler_t`**`)(` | sd_bus_message \*`m`, |
|   | void \*`userdata`, |
|   | sd_bus_error \*`ret_error``)`; |

 

|                                        |                          |
|----------------------------------------|--------------------------|
| `sd_bus *`**`sd_bus_slot_get_bus`**`(` | sd_bus_slot \*`slot``)`; |

 

|  |  |
|----|----|
| `sd_bus_message_handler_t `**`sd_bus_slot_get_current_handler`**` (` | sd_bus_slot \*`slot``)`; |

 

|  |  |
|----|----|
| `sd_bus_message *`**`sd_bus_slot_get_current_message`**`(` | sd_bus_slot \*`slot``)`; |

 

|  |  |
|----|----|
| `void *`**`sd_bus_slot_get_current_userdata`**`(` | sd_bus_slot \*`slot``)`; |

 

## Description

`sd_bus_slot_get_bus()` returns the bus object that message *`slot`* is attached to.

`sd_bus_slot_get_current_handler()`, `sd_bus_slot_get_current_message()` and `sd_bus_slot_get_current_userdata()` return the current handler, message and userdata respectively of the bus *`slot`* is attached to if we're currently executing the callback associated with *`slot`*.

## Return Value

`sd_bus_slot_get_bus()` always returns the bus object.

On success, `sd_bus_slot_get_current_handler()`, `sd_bus_slot_get_current_message()` and `sd_bus_slot_get_current_userdata()` return the requested object. On failure, they return `NULL`.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_slot_get_bus()`, `sd_bus_slot_get_current_handler()`, `sd_bus_slot_get_current_message()`, and `sd_bus_slot_get_current_userdata()` were added in version 246.

## See Also

systemd(1), sd-bus(3)
