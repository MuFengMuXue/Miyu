## Name

sd_bus_set_exit_on_disconnect, sd_bus_get_exit_on_disconnect — Control the exit behavior when the bus object disconnects

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                              |                 |
|----------------------------------------------|-----------------|
| `int `**`sd_bus_set_exit_on_disconnect`**`(` | sd_bus \*`bus`, |
|                                              | int `b``)`;     |

 

|                                              |                    |
|----------------------------------------------|--------------------|
| `int `**`sd_bus_get_exit_on_disconnect`**`(` | sd_bus \*`bus``)`; |

 

## Description

`sd_bus_set_exit_on_disconnect()` may be used to configure the exit behavior when the given bus object disconnects. If *`b`* is zero, no special logic is executed when the bus object disconnects. If *`b`* is non-zero, the behavior on disconnect depends on whether the bus object is attached to an event loop or not. If the bus object is attached to an event loop (see sd_bus_attach_event(3)), the event loop is closed when the bus object disconnects (as if calling sd_event_exit(3)). Otherwise, exit(3) is called. The exit code passed to `sd_event_exit()` and `exit()` is `EXIT_FAILURE`. If the bus object has already disconnected when enabling the exit behavior, the exit behavior is executed immediately. By default, the exit behavior is disabled.

`sd_bus_get_exit_on_disconnect()` returns whether the exit on disconnect behavior is enabled for the given bus object.

## Return Value

On success, `sd_bus_set_exit_on_disconnect()` returns a non-negative integer. On failure, it returns a negative errno-style error code.

`sd_bus_get_exit_on_disconnect()` returns a positive integer if the exit on disconnect behavior is enabled. Otherwise, it returns zero.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
A required parameter was `NULL`.

Added in version 246.

`-ENOPKG`  
The bus object could not be resolved.

Added in version 246.

`-ECHILD`  
The bus connection was created in a different process, library or module instance.

Added in version 246.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_set_exit_on_disconnect()` and `sd_bus_get_exit_on_disconnect()` were added in version 246.

## See Also

systemd(1), sd-bus(3), sd_bus_attach_event(3), sd-event(3), sd_event_exit(3)
