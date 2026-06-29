## Name

sd_bus_message_rewind — Return to beginning of message or current container

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                      |                       |
|--------------------------------------|-----------------------|
| `int `**`sd_bus_message_rewind`**`(` | sd_bus_message \*`m`, |
|                                      | int `complete``)`;    |

 

## Description

`sd_bus_message_rewind()` moves the "read pointer" in the message *`m`* to either the beginning of the message (if *`complete`* is true) or to the beginning of the currently open container. If no container is open, *`complete`* has no effect.

## Return Value

On success, this function returns 0 or a positive integer. The value is zero if the current container or whole message in case no container is open is empty, and positive otherwise. On failure, it returns a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
The *`m`* parameter is `NULL`.

`-EPERM`  
The message *`m`* has not been sealed.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_message_rewind()` was added in version 240.

## See Also

systemd(1), sd-bus(3), sd_bus_message_read(3)
