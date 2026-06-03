## Name

sd_bus_get_current_handler, sd_bus_get_current_message, sd_bus_get_current_slot, sd_bus_get_current_userdata — Query information of the callback a bus object is currently running

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|  |  |
|----|----|
| `typedef int (*`**`sd_bus_message_handler_t`**`)(` | sd_bus_message \*`m`, |
|   | void \*`userdata`, |
|   | sd_bus_error \*`ret_error``)`; |

 

|  |  |
|----|----|
| `sd_bus_message_handler_t `**`sd_bus_get_current_handler`**`(` | sd_bus \*`bus``)`; |

 

|                                                       |                    |
|-------------------------------------------------------|--------------------|
| `sd_bus_message* `**`sd_bus_get_current_message`**`(` | sd_bus \*`bus``)`; |

 

|                                                 |                    |
|-------------------------------------------------|--------------------|
| `sd_bus_slot* `**`sd_bus_get_current_slot`**`(` | sd_bus \*`bus``)`; |

 

|                                              |                    |
|----------------------------------------------|--------------------|
| `void* `**`sd_bus_get_current_userdata`**`(` | sd_bus \*`bus``)`; |

 

## Description

Whenever sd-bus is about to invoke a user-supplied callback function, it stores the current callback, D-Bus message, slot and userdata pointer and allows these to be queried via `sd_bus_get_current_handler()`, `sd_bus_get_current_message()`, `sd_bus_get_current_slot()` and `sd_bus_get_current_userdata()`, respectively. If *`bus`* cannot be resolved or if execution does not reside in a user-supplied callback of *`bus`*, these functions return `NULL`.

## Return Value

On success, these functions return the requested object. On failure, they return `NULL`.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_get_current_handler()`, `sd_bus_get_current_message()`, `sd_bus_get_current_slot()`, and `sd_bus_get_current_userdata()` were added in version 221.

## See Also

systemd(1), sd-bus(3)
