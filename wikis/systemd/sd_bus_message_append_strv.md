## Name

sd_bus_message_append_strv — Attach an array of strings to a message

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                   |                       |
|-----------------------------------|-----------------------|
| `int sd_bus_message_append_strv(` | sd_bus_message \*`m`, |
|                                   | char \*\*`l``)`;      |

 

## Description

The `sd_bus_message_append()` function can be used to append an array of strings to message *`m`*. The parameter *`l`* shall point to a `NULL`-terminated array of pointers to `NUL`-terminated strings. Each string must satisfy the same constraints as described for the "`s`" type in sd_bus_message_append_basic(3).

The memory pointed at by *`p`* and the contents of the strings themselves are copied into the memory area containing the message and may be changed after this call. Note that the signature of *`l`* parameter is to be treated as const char \*const \*, and the contents will not be modified.

## Return Value

On success, this call returns 0 or a positive integer. On failure, a negative errno-style error code is returned.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
Specified parameter is invalid.

`-EPERM`  
Message has been sealed.

`-ESTALE`  
Message is in invalid state.

`-ENXIO`  
Message cannot be appended to.

`-ENOMEM`  
Memory allocation failed.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## See Also

systemd(1), sd-bus(3), sd_bus_message_append(3), sd_bus_message_append_array(3), The D-Bus specification
