## Name

sd_bus_set_connected_signal, sd_bus_get_connected_signal — Control emission of local connection establishment signal on bus connections

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                            |                 |
|--------------------------------------------|-----------------|
| `int `**`sd_bus_set_connected_signal`**`(` | sd_bus \*`bus`, |
|                                            | int `b``)`;     |

 

|                                            |                    |
|--------------------------------------------|--------------------|
| `int `**`sd_bus_get_connected_signal`**`(` | sd_bus \*`bus``)`; |

 

## Description

`sd_bus_set_connected_signal()` may be used to control whether a local, synthetic `Connected()` signal message shall be generated and enqueued for dispatching when the connection is fully established. If the *`b`* parameter is zero the message is not generated (the default), otherwise it is generated.

`sd_bus_get_connected_signal()` may be used to query whether this feature is enabled. It returns zero if not, positive otherwise.

The `Connected()` signal message is generated from the "`org.freedesktop.DBus.Local`" service and interface, and "`/org/freedesktop/DBus/Local`" object path. Use sd_bus_match_signal_async(3) to match on this signal.

This message is particularly useful on slow transports where connections take a long time to be established. This is especially the case when sd_bus_set_watch_bind(3) is used. The signal is generated when the sd_bus_is_ready(3) returns positive for the first time.

The `Connected()` signal corresponds with the `Disconnected()` signal that is synthesized locally when the connection is terminated. The latter is generated unconditionally however, unlike the former which needs to be enabled explicitly before it is generated, with `sd_bus_set_connected_signal()`.

## Return Value

On success, these functions return 0 or a positive integer. On failure, they return a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-ECHILD`  
The bus connection has been created in a different process, library or module instance.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_set_connected_signal()` and `sd_bus_get_connected_signal()` were added in version 237.

## See Also

systemd(1), sd-bus(3), sd_bus_match_signal_async(3), sd_bus_set_watch_bind(3), sd_bus_is_ready(3)
