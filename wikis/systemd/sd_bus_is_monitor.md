## Name

sd_bus_set_server, sd_bus_is_server, sd_bus_get_bus_id, sd_bus_set_bus_client, sd_bus_is_bus_client, sd_bus_set_monitor, sd_bus_is_monitor — Configure connection mode for a bus object

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                  |                     |
|----------------------------------|---------------------|
| `int `**`sd_bus_set_server`**`(` | sd_bus \*`bus`,     |
|                                  | int `b`,            |
|                                  | sd_id128_t `id``)`; |

 

|                                 |                    |
|---------------------------------|--------------------|
| `int `**`sd_bus_is_server`**`(` | sd_bus \*`bus``)`; |

 

|                                  |                       |
|----------------------------------|-----------------------|
| `int `**`sd_bus_get_bus_id`**`(` | sd_bus \*`bus`,       |
|                                  | sd_id128_t \*`id``)`; |

 

|                                      |                 |
|--------------------------------------|-----------------|
| `int `**`sd_bus_set_bus_client`**`(` | sd_bus \*`bus`, |
|                                      | int `b``)`;     |

 

|                                     |                    |
|-------------------------------------|--------------------|
| `int `**`sd_bus_is_bus_client`**`(` | sd_bus \*`bus``)`; |

 

|                                   |                 |
|-----------------------------------|-----------------|
| `int `**`sd_bus_set_monitor`**`(` | sd_bus \*`bus`, |
|                                   | int `b``)`;     |

 

|                                  |                    |
|----------------------------------|--------------------|
| `int `**`sd_bus_is_monitor`**`(` | sd_bus \*`bus``)`; |

 

## Description

`sd_bus_set_server()` configures the bus object as a server for direct D-Bus connections. *`b`* enables/disables the server mode. If zero, the server mode is disabled. Otherwise, the server mode is enabled. Configuring a bus object as a server is required to allow establishing direct connections between two peers without going via the D-Bus daemon. *`id`* must contain a 128-bit integer id for the server. If clients add a guid field to their D-Bus address string, the server id must match this guid or the D-Bus authentication handshake will fail. If no specific id is defined for the server, sd_id128_randomize(3) can be used to generate a random id instead.

`sd_bus_is_server()` returns whether the server mode is enabled for the given bus object.

`sd_bus_get_bus_id()` stores the D-Bus server id configured using `sd_bus_set_server()` (for server bus objects) or received during D-Bus authentication (for client bus objects) in *`id`*.

`sd_bus_set_bus_client()` configures the bus object as a D-Bus daemon client. *`b`* enables/disables the client mode. If zero, the client mode is disabled and the bus object should connect directly to a D-Bus server. Otherwise, the client mode is enabled and the bus object should connect to a D-Bus daemon. When connecting to an existing bus using any of the functions in the sd_bus_open(3) family of functions or any of the functions in the sd_bus_default(3) family of functions, the bus object is automatically configured as a bus client. However, when connecting to a D-Bus daemon by calling sd_bus_set_address(3) followed by sd_bus_start(3), the bus object should be manually configured as a bus client using `sd_bus_set_bus_client()`. By default, a bus object is not configured as a D-Bus daemon client.

`sd_bus_is_bus_client()` returns whether the client mode is enabled/disabled for the given bus object.

`sd_bus_set_monitor()` configures the bus object as a D-Bus monitor object. *`b`* enables/disables the monitor mode. If zero, the monitor mode is disabled. If non-zero, the monitor mode is enabled. When the monitor mode is enabled, no messages may be sent via the bus object and it may not expose any objects on the bus. To start monitoring messages, call the `org.freedesktop.DBus.Monitoring.BecomeMonitor` method of the D-Bus daemon and pass a list of matches indicating which messages to intercept. See The D-Bus specification for more information.

`sd_bus_is_monitor()` returns whether the monitor mode is enabled/disabled for the given bus object.

## Return Value

On success, `sd_bus_set_server()`, `sd_bus_get_bus_id()`, `sd_bus_set_bus_client()` and `sd_bus_set_monitor()` return a non-negative integer. On failure, they return a negative errno-style error code.

`sd_bus_is_server()`, `sd_bus_is_bus_client()` and `sd_bus_is_monitor()` return a positive integer when the server or client mode is enabled, respectively. Otherwise, they return zero.

### Errors

Returned errors may indicate the following problems:

`-ECHILD`  
The bus connection has been created in a different process, library or module instance.

Added in version 246.

`-EPERM`  
The bus connection has already been started.

Added in version 246.

`-ENOPKG`  
The bus cannot be resolved.

Added in version 246.

`-EINVAL`  
A required parameter was `NULL` or *`b`* was zero and *`id`* did not equal `SD_ID128_NULL`.

Added in version 246.

`-ENOTCONN`  
The bus is not connected.

Added in version 246.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_set_server()`, `sd_bus_is_server()`, `sd_bus_get_bus_id()`, `sd_bus_set_bus_client()`, `sd_bus_is_bus_client()`, `sd_bus_set_monitor()`, and `sd_bus_is_monitor()` were added in version 246.

## See Also

systemd(1), sd-bus(3)
