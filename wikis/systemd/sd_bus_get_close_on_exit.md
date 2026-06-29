## Name

sd_bus_set_close_on_exit, sd_bus_get_close_on_exit — Control whether to close the bus connection during the event loop exit phase

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                         |                 |
|-----------------------------------------|-----------------|
| `int `**`sd_bus_set_close_on_exit`**`(` | sd_bus \*`bus`, |
|                                         | int `b``)`;     |

 

|                                         |                    |
|-----------------------------------------|--------------------|
| `int `**`sd_bus_get_close_on_exit`**`(` | sd_bus \*`bus``)`; |

 

## Description

`sd_bus_set_close_on_exit()` may be used to enable or disable whether the bus connection is automatically flushed (as in sd_bus_flush(3)) and closed (as in sd_bus_close(3)) during the exit phase of the event loop. This logic only applies to bus connections that are attached to an sd-event(3) event loop, see sd_bus_attach_event(3). By default, this mechanism is enabled and makes sure that any pending messages that have not been written to the bus connection are written out when the event loop is shutting down. In some cases this behaviour is not desirable, for example when the bus connection shall remain usable until after the event loop exited. If *`b`* is true, the feature is enabled (which is the default), otherwise disabled.

`sd_bus_get_close_on_exit()` may be used to query the current setting of this feature. It returns zero when the feature is disabled, and positive if enabled.

## Return Value

On success, `sd_bus_set_close_on_exit()` returns a non-negative integer. On failure, it returns a negative errno-style error code.

`sd_bus_get_close_on_exit()` returns 0 if the feature is currently disabled or a positive integer if it is enabled. On failure, it returns a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-ECHILD`  
The bus connection was created in a different process, library or module instance.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_set_close_on_exit()` and `sd_bus_get_close_on_exit()` were added in version 240.

## See Also

systemd(1), sd-bus(3), sd_bus_flush(3), sd_bus_attach_event(3), sd-event(3), sd_event_add_exit(3)
