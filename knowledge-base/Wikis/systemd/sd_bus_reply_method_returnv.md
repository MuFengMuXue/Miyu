## Name

sd_bus_reply_method_return, sd_bus_reply_method_returnv — Reply to a D-Bus method call

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                   |                          |
|-----------------------------------|--------------------------|
| `int sd_bus_reply_method_return(` | sd_bus_message \*`call`, |
|                                   | const char \*`types`,    |
|                                   | ...`)`;                  |

 

|                                    |                          |
|------------------------------------|--------------------------|
| `int sd_bus_reply_method_returnv(` | sd_bus_message \*`call`, |
|                                    | const char \*`types`,    |
|                                    | va_list `ap``)`;         |

 

## Description

`sd_bus_reply_method_return()` sends a reply to the *`call`* message. The type string *`types`* and the arguments that follow it must adhere to the format described in sd_bus_message_append(3). If no reply is expected to *`call`*, this function succeeds without sending a reply.

## Return Value

On success, this function returns a non-negative integer. On failure, it returns a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
The input parameter *`call`* is `NULL`.

Message *`call`* is not a method call message.

Message *`call`* is not attached to a bus.

Message *`m`* is not a method reply message.

Added in version 246.

`-EPERM`  
Message *`call`* has been sealed.

Added in version 246.

`-ENOTCONN`  
The bus to which message *`call`* is attached is not connected.

Added in version 246.

`-ENOMEM`  
Memory allocation failed.

Added in version 246.

In addition, any error returned by sd_bus_send(3) may be returned.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## See Also

systemd(1), sd-bus(3), sd_bus_message_new_method_return(3)
