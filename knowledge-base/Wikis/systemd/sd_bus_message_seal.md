## Name

sd_bus_message_seal — Prepare a D-Bus message for transmission

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                    |                             |
|------------------------------------|-----------------------------|
| `int `**`sd_bus_message_seal`**`(` | sd_bus_message \*`m`,       |
|                                    | uint64_t `cookie`,          |
|                                    | uint64_t `timeout_usec``)`; |

 

## Description

`sd_bus_message_seal()` finishes the message *`m`* and prepares it for transmission using sd_bus_send(3). *`cookie`* specifies the identifier used to match the message reply to its corresponding request. *`timeout_usec`* specifies the maximum time in microseconds to wait for a reply to arrive.

Note that in most scenarios, it is not necessary to call this function directly. sd_bus_call(3), sd_bus_call_async(3) and sd_bus_send(3) will seal any given messages if they have not been sealed yet.

## Return Value

On success, this function returns a non-negative integer. On failure, it returns a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
The *`m`* parameter is `NULL`.

Added in version 246.

`-EBADMSG`  
The D-Bus message *`m`* has open containers.

Added in version 246.

`-ENOMSG`  
The D-Bus message *`m`* is a reply but its type signature does not match the return type signature of its corresponding member in the object vtable.

Added in version 246.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_message_seal()` was added in version 246.

## See Also

systemd(1), sd-bus(3), sd_bus_call(3), sd_bus_call_async(3), sd_bus_send(3)
