## Name

sd_bus_message_get_cookie, sd_bus_message_get_reply_cookie — Returns the transaction cookie of a message

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                          |                             |
|------------------------------------------|-----------------------------|
| `int `**`sd_bus_message_get_cookie`**`(` | sd_bus_message \*`message`, |
|                                          | uint64_t \*`cookie``)`;     |

 

|  |  |
|----|----|
| `int `**`sd_bus_message_get_reply_cookie`**`(` | sd_bus_message \*`message`, |
|   | uint64_t \*`cookie``)`; |

 

## Description

`sd_bus_message_get_cookie()` returns the transaction cookie of a message. The cookie uniquely identifies a message within each bus peer, but is not globally unique. It is assigned when a message is sent.

`sd_bus_message_get_reply_cookie()` returns the transaction cookie of the message the specified message is a response to. When a reply message is generated for a method call message, its cookie is copied over into this field. Note that while every message that is transferred is identified by a cookie, only response messages carry a reply cookie field.

Both functions take a message object as first parameter and a place to store the 64-bit cookie in.

## Return Value

On success, these calls return 0 or a positive integer. On failure, they return a negative errno-style error code.

On success, the cookie/reply cookie is returned in the specified 64-bit unsigned integer variable.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
A specified parameter is invalid.

`-ENODATA`  
No cookie has been assigned to this message. This either indicates that the message has not been sent yet and hence has no cookie assigned, or that the message is not a method response message and hence carries a reply cookie field.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_message_get_cookie()` and `sd_bus_message_get_reply_cookie()` were added in version 209.

## See Also

systemd(1), sd-bus(3), sd_bus_new(3)
