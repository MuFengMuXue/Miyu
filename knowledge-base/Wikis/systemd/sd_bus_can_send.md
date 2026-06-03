## Name

sd_bus_can_send — Check which types can be sent over a bus object

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                |                 |
|--------------------------------|-----------------|
| `int `**`sd_bus_can_send`**`(` | sd_bus \*`bus`, |
|                                | char `type``)`; |

 

## Description

`sd_bus_can_send()` is mostly used for checking if file descriptor passing is available on the given bus. *`type`* can be any of the `SD_BUS_TYPE` constants.

## Return Value

On failure, `sd_bus_can_send()` returns a negative errno-style error code. If values of the given type can be sent over the given bus, it returns a positive integer. Otherwise, it returns zero.

### Errors

Returned errors may indicate the following problems:

`-ENOPKG`  
The bus object *`bus`* could not be resolved.

`-ENOTCONN`  
The input parameter *`bus`* is `NULL` or the bus is not connected.

`-ECHILD`  
The bus object *`bus`* was created in a different process.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_can_send()` was added in version 221.

## See Also

systemd(1), sd-bus(3)
