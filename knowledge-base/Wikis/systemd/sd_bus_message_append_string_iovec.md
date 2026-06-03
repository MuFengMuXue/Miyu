## Name

sd_bus_message_append_string_memfd, sd_bus_message_append_string_iovec, sd_bus_message_append_string_space — Attach a string to a message

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                           |                       |
|-------------------------------------------|-----------------------|
| `int sd_bus_message_append_string_memfd(` | sd_bus_message \*`m`, |
|                                           | int `memfd``)`;       |

 

|                                           |                             |
|-------------------------------------------|-----------------------------|
| `int sd_bus_message_append_string_iovec(` | sd_bus_message \*`m`,       |
|                                           | const struct iovec \*`iov`, |
|                                           | unsigned `n``)`;            |

 

|                                           |                       |
|-------------------------------------------|-----------------------|
| `int sd_bus_message_append_string_space(` | sd_bus_message \*`m`, |
|                                           | size_t `size`,        |
|                                           | char \*\*`s``)`;      |

 

## Description

The functions `sd_bus_message_append_string_memfd()` and `sd_bus_message_append_string_iovec()` can be used to append a single string (item of type "`s`") to message *`m`*.

In case of `sd_bus_message_append_string_memfd()`, the contents of *`memfd`* are the string. They must satisfy the same constraints as described for the "`s`" type in sd_bus_message_append_basic(3).

In case of `sd_bus_message_append_string_iovec()`, the payload of *`iov`* is the string. It must satisfy the same constraints as described for the "`s`" type in sd_bus_message_append_basic(3).

The *`iov`* argument must point to *`n`* struct iovec structures. Each structure may have the iov_base field set, in which case the memory pointed to will be copied into the message, or unset, in which case a block of spaces (ASCII 32) of length iov_len will be inserted. The memory pointed at by *`iov`* may be changed after this call.

The `sd_bus_message_append_string_space()` function appends space for a string to message *`m`*. It behaves similar to `sd_bus_message_append_basic()` with type "`s`", but instead of copying a string into the message, it returns a pointer to the destination area to the caller in pointer *`p`*. Space for the string of length *`size`* plus the terminating `NUL` is allocated.

## Return Value

On success, those calls return 0 or a positive integer. On failure, they return a negative errno-style error code.

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

systemd(1), sd-bus(3), sd_bus_message_append_basic(3), The D-Bus specification
