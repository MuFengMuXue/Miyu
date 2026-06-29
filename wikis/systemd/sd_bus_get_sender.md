## Name

sd_bus_set_sender, sd_bus_get_sender — Configure default sender for outgoing messages

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                  |                         |
|----------------------------------|-------------------------|
| `int `**`sd_bus_set_sender`**`(` | sd_bus \*`bus`,         |
|                                  | const char\* `name``)`; |

 

|                                  |                           |
|----------------------------------|---------------------------|
| `int `**`sd_bus_get_sender`**`(` | sd_bus \*`bus`,           |
|                                  | const char\*\* `name``)`; |

 

## Description

`sd_bus_set_sender()` configures the default sender service name to use for outgoing messages. The service name specified in the *`name`* parameter is set on all outgoing messages that are sent on the connection and have no sender set yet, for example through sd_bus_message_set_sender(3). Note that this function is only supported on direct connections, i.e. not on connections to a bus broker as the broker will fill in the sender service name automatically anyway. By default, no sender name is configured, and hence messages are sent without sender field set. If the *`name`* parameter is specified as `NULL` the default sender service name is cleared, returning to the default state if a default sender service name was set before. If passed as non-`NULL` the specified name must be a valid unique or well-known service name.

`sd_bus_get_sender()` may be used to query the current default service name for outgoing messages.

## Return Value

On success, these functions return 0 or a positive integer. On failure, they return a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-ECHILD`  
The bus connection has been created in a different process, library or module instance.

`-EPERM`  
The specified bus connection object is a not a direct but a brokered connection.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_set_sender()` and `sd_bus_get_sender()` were added in version 237.

## See Also

systemd(1), sd-bus(3), sd_bus_message_set_sender(3)
