## Name

sd_bus_message_verify_type — Check if the message has specified type at the current location

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                   |                             |
|-----------------------------------|-----------------------------|
| `int sd_bus_message_verify_type(` | sd_bus_message \*`m`,       |
|                                   | char `type`,                |
|                                   | const char\* `contents``)`; |

 

## Description

`sd_bus_message_verify_type()` checks if the complete type at the current location in the message *`m`* matches the specified *`type`* and *`contents`*. If non-zero, parameter *`type`* must be one of the types specified in sd_bus_message_append(3). If non-null, parameter *`contents`* must be a valid sequence of complete types. If both *`type`* and *`contents`* are specified *`type`* must be a container type.

If *`type`* is specified, the type in the message must match. If *`contents`* is specified, the type in the message must be a container type with this signature.

## Return Value

On success, this call returns true if the type matches and zero if not (the message *`m`* contains different data or the end of the message has been reached). On failure, it returns a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
*`m`* or both *`type`* and *`contents`* are `NULL`.

Arguments do not satisfy other constraints listed above.

`-EPERM`  
Message *`m`* is not sealed.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## See Also

systemd(1), sd-bus(3), sd_bus_message_append(3)
