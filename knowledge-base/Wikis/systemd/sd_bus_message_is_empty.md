## Name

sd_bus_message_get_signature, sd_bus_message_is_empty, sd_bus_message_has_signature — Query bus message signature

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|  |  |
|----|----|
| `const char* `**`sd_bus_message_get_signature`**`(` | sd_bus_message \*`message`, |
|   | int `complete``)`; |

 

|                                        |                                |
|----------------------------------------|--------------------------------|
| `int `**`sd_bus_message_is_empty`**`(` | sd_bus_message \*`message``)`; |

 

|                                             |                              |
|---------------------------------------------|------------------------------|
| `int `**`sd_bus_message_has_signature`**`(` | sd_bus_message \*`message`,  |
|                                             | const char \*`signature``)`; |

 

## Description

`sd_bus_message_get_signature()` returns the signature of message *`message`*. If *`complete`* is true, the signature of the whole message is returned, and just the signature of the currently open container otherwise.

`sd_bus_message_is_empty()` returns true if the message is empty, i.e. when its signature is empty.

`sd_bus_message_has_signature()` returns true if the signature of the message *`message`* matches given *`signature`*. Parameter *`signature`* may be `NULL`, this is treated the same as an empty string, which is equivalent to calling `sd_bus_message_is_empty()`.

## Return Value

On success, `sd_bus_message_get_signature()` returns the signature, and `NULL` on error.

The other functions return 0 or a positive integer on success. On failure, they return a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
The *`message`* parameter is `NULL`.

`NULL`  
The *`message`* parameter is `NULL`.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_message_get_signature()`, `sd_bus_message_is_empty()`, and `sd_bus_message_has_signature()` were added in version 240.

## See Also

systemd(1), sd-bus(3), sd_bus_message_new(3)
