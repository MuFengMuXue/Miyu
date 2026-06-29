## Name

sd_bus_message_skip — Skip elements in a bus message

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                    |                          |
|------------------------------------|--------------------------|
| `int `**`sd_bus_message_skip`**`(` | sd_bus_message \*`m`,    |
|                                    | const char\* `types``)`; |

 

## Description

`sd_bus_message_skip()` is somewhat similar to sd_bus_message_read(3), but instead of reading the contents of the message, it only moves the "read pointer". Subsequent read operations will read the elements that are after the elements that were skipped.

The *`types`* argument has the same meaning as in `sd_bus_message_read()`. It may also be `NULL`, to skip a single element of any type.

## Return Value

On success, `sd_bus_message_skip()` returns 0 or a positive integer. On failure, it returns a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
The *`m`* parameter is `NULL`.

`-EBADMSG`  
The message cannot be parsed.

`-EPERM`  
The message is not sealed.

`-ENXIO`  
The message end has been reached and the requested elements cannot be read.

`-ENOMEM`  
Memory allocation failed.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_message_skip()` was added in version 240.

## See Also

systemd(1), sd-bus(3), sd_bus_message_read(3), sd_bus_message_read_basic(3)
