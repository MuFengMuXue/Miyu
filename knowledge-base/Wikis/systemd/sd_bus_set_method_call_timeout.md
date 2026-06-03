## Name

sd_bus_set_method_call_timeout, sd_bus_get_method_call_timeout — Set or query the default D-Bus method call timeout of a bus object

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                               |                     |
|-----------------------------------------------|---------------------|
| `int `**`sd_bus_set_method_call_timeout`**`(` | sd_bus \*`bus`,     |
|                                               | uint64_t `usec``)`; |

 

|                                               |                      |
|-----------------------------------------------|----------------------|
| `int `**`sd_bus_get_method_call_timeout`**`(` | sd_bus \*`bus`,      |
|                                               | uint64_t \*`ret``)`; |

 

## Description

`sd_bus_set_method_call_timeout()` sets the default D-Bus method call timeout of *`bus`* to *`usec`* microseconds.

`sd_bus_get_method_call_timeout()` queries the default D-Bus method call timeout of *`bus`*. If no method call timeout was set using `sd_bus_set_method_call_timeout()`, the timeout is read from the `$SYSTEMD_BUS_TIMEOUT` environment variable. If this environment variable is unset or does not contain a valid timeout, the implementation falls back to a predefined method call timeout of 25 seconds. Note that `$SYSTEMD_BUS_TIMEOUT` is read once and cached so callers should not rely on being able to change the default method call timeout at runtime by changing the value of `$SYSTEMD_BUS_TIMEOUT`. Instead, call `sd_bus_set_method_call_timeout()` to change the default method call timeout.

## Return Value

On success, these functions return a non-negative integer. On failure, they return a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
The parameters *`bus`* or *`ret`* are `NULL`.

Added in version 246.

`-ENOPKG`  
Bus object *`bus`* could not be resolved.

Added in version 246.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_set_method_call_timeout()` and `sd_bus_get_method_call_timeout()` were added in version 246.

## See Also

systemd(1), sd-bus(3), sd_bus_call(3)
