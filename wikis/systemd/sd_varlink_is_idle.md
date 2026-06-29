## Name

sd_varlink_is_connected, sd_varlink_is_idle — Query if a Varlink connection object is currently connected or idle

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-varlink.h>
```

|                                        |                         |
|----------------------------------------|-------------------------|
| `int `**`sd_varlink_is_connected`**`(` | sd_varlink \*`link``)`; |

 

|                                   |                         |
|-----------------------------------|-------------------------|
| `int `**`sd_varlink_is_idle`**`(` | sd_varlink \*`link``)`; |

 

## Description

`sd_varlink_is_connected()` checks whether the specified Varlink connection object is currently connected or whether it has been fully disconnected already.

`sd_varlink_is_idle()` checks whether the specified Varlink connection object is currently connected but idle, i.e. may accept a method call for enqueuing (if client side of a Varlink connection) or is waiting for more incoming method calls to arrive (if server side of a Varlink connection).

## Return Value

If the connection is currently connected `sd_varlink_is_connected()` returns a positive non-zero value. If disconnected it returns 0. If the connection currently is idle `sd_varlink_is_idle()` returns a positive non-zero integer. If not, returns 0. On failure, both functions return a negative `errno` error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
The specified Varlink connection is invalid.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_varlink_is_connected()` was added in version 259.

`sd_varlink_is_idle()` was added in version 257.

## See Also

systemd(1), sd-varlink(3)
