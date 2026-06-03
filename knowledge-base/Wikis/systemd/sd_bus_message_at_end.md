## Name

sd_bus_message_at_end — Check if a message has been fully read

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                      |                       |
|--------------------------------------|-----------------------|
| `int `**`sd_bus_message_at_end`**`(` | sd_bus_message \*`m`, |
|                                      | int `complete``)`;    |

 

## Description

`sd_bus_message_at_end()` returns whether all data from the currently opened container in *`m`* or all data from all containers in *`m`* has been read. If *`complete`* is zero, this function returns whether all data from the currently opened container has been read. If *`complete`* is non-zero, this function returns whether all data from all containers in *`m`* has been read.

## Return Value

If all data from all containers or the current container (depending on the value of *`complete`*) has been read, `sd_bus_message_at_end()` returns a positive integer. If there is still data left to be read, it returns zero. On failure, it returns a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
The *`m`* parameter is `NULL`.

Added in version 246.

`-EPERM`  
The message is not sealed.

Added in version 246.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_message_at_end()` was added in version 246.

## See Also

systemd(1), sd-bus(3), sd_bus_message_read(3)
