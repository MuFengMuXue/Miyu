## Name

sd_bus_attach_event, sd_bus_detach_event, sd_bus_get_event — Attach a bus connection object to an event loop

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                    |                    |
|------------------------------------|--------------------|
| `int `**`sd_bus_attach_event`**`(` | sd_bus \*`bus`,    |
|                                    | sd_event \*`e`,    |
|                                    | int `priority``)`; |

 

|                                    |                    |
|------------------------------------|--------------------|
| `int `**`sd_bus_detach_event`**`(` | sd_bus \*`bus``)`; |

 

|                                       |                    |
|---------------------------------------|--------------------|
| `sd_event *`**`sd_bus_get_event`**`(` | sd_bus \*`bus``)`; |

 

## Description

`sd_bus_attach_event()` attaches the specified bus connection object to an sd-event(3) event loop object at the specified priority (see sd_event_source_set_priority(3) for details on event loop priorities). When a bus connection object is attached to an event loop incoming messages will be automatically read and processed, and outgoing messages written, whenever the event loop is run. When the event loop is about to terminate, the bus connection is automatically flushed and closed (see sd_bus_set_close_on_exit(3) for details on this). By default, bus connection objects are not attached to any event loop. When a bus connection object is attached to one it is not necessary to invoke sd_bus_wait(3) or sd_bus_process(3) as this functionality is handled automatically by the event loop.

`sd_bus_detach_event()` detaches a bus object from its event loop.

The `sd_bus_get_event()` returns the event loop object the specified bus object is currently attached to, or `NULL` if it is currently not attached to any.

Note that `sd_bus_attach_event()` is only one of three supported ways to implement I/O event handling for bus connections. Alternatively use sd_bus_get_fd(3) for hooking up a bus connection object with external or manual event loops. Or use sd_bus_wait(3) as a simple synchronous, blocking I/O waiting call.

## Return Value

On success, `sd_bus_attach_event()` and `sd_bus_detach_event()` return 0 or a positive integer. On failure, they return a negative errno-style error code.

`sd_bus_get_event()` returns an event loop object or `NULL`.

### Errors

Returned errors may indicate the following problems:

`-ECHILD`  
The bus connection has been created in a different process, library or module instance.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_attach_event()`, `sd_bus_detach_event()`, and `sd_bus_get_event()` were added in version 221.

## See Also

systemd(1), sd-bus(3), sd-event(3), sd_event_source_set_priority(3), sd_bus_set_close_on_exit(3), sd_bus_wait(3), sd_bus_get_fd(3)
