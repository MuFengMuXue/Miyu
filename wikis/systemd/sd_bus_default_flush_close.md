## Name

sd_bus_close, sd_bus_flush, sd_bus_default_flush_close — Close and flush a bus connection

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                              |                    |
|------------------------------|--------------------|
| `void `**`sd_bus_close`**`(` | sd_bus \*`bus``)`; |

 

|                             |                    |
|-----------------------------|--------------------|
| `int `**`sd_bus_flush`**`(` | sd_bus \*`bus``)`; |

 

|                                            |          |
|--------------------------------------------|----------|
| `void `**`sd_bus_default_flush_close`**`(` | void`)`; |

 

## Description

`sd_bus_close()` disconnects the specified bus connection. When this call is invoked and the specified bus object refers to an active connection it is immediately terminated. No further messages may be sent or received on it. Any messages queued in the bus object (both incoming and outgoing) are released. If invoked on `NULL` bus object or when the bus connection is already closed this function executes no operation. This call does not free or unreference the bus object itself. Use sd_bus_unref(3) for that.

`sd_bus_flush()` synchronously writes out all outgoing queued message on a bus connection if there are any. This function call may block if the peer is not processing bus messages quickly.

Before a program exits it is usually a good idea to flush any pending messages with `sd_bus_flush()` and then close connections with `sd_bus_close()` to ensure that no unwritten messages are lost, no further messages may be queued and all incoming but unprocessed messages are released. After both operations have been done, it is a good idea to also drop any remaining references to the bus object so that it may be freed. Since these three operations are frequently done together a helper call sd_bus_flush_close_unref(3) is provided that combines them into one.

`sd_bus_default_flush_close()` is similar to `sd_bus_flush_close_unref()`, but does not take a bus pointer argument and instead iterates over any of the "default" buses opened by sd_bus_default(3), sd_bus_default_user(3), sd_bus_default_system(3), and similar calls. `sd_bus_default_flush_close()` is particularly useful to clean up any buses opened using those calls before the program exits.

## Return Value

On success, `sd_bus_flush()` returns a non-negative integer. On failure, it returns a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-ECHILD`  
The bus connection has been created in a different process, library or module instance.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_close()` and `sd_bus_flush()` were added in version 221.

`sd_bus_default_flush_close()` was added in version 227.

## See Also

systemd(1), sd-bus(3), sd_bus_unref(3), sd_bus_set_close_on_exit(3)
