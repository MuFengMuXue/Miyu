## Name

sd_bus_message_set_destination, sd_bus_message_get_destination, sd_bus_message_get_path, sd_bus_message_get_interface, sd_bus_message_get_member, sd_bus_message_set_sender, sd_bus_message_get_sender — Set and query bus message addressing information

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|  |  |
|----|----|
| `int `**`sd_bus_message_set_destination`**`(` | sd_bus_message \*`message`, |
|   | const char \*`destination``)`; |

 

|  |  |
|----|----|
| `const char* `**`sd_bus_message_get_destination`**`(` | sd_bus_message \*`message``)`; |

 

|  |  |
|----|----|
| `const char* `**`sd_bus_message_get_path`**`(` | sd_bus_message \*`message``)`; |

 

|  |  |
|----|----|
| `const char* `**`sd_bus_message_get_interface`**`(` | sd_bus_message \*`message``)`; |

 

|  |  |
|----|----|
| `const char* `**`sd_bus_message_get_member`**`(` | sd_bus_message \*`message``)`; |

 

|                                          |                             |
|------------------------------------------|-----------------------------|
| `int `**`sd_bus_message_set_sender`**`(` | sd_bus_message \*`message`, |
|                                          | const char \*`sender``)`;   |

 

|  |  |
|----|----|
| `const char* `**`sd_bus_message_get_sender`**`(` | sd_bus_message \*`message``)`; |

 

## Description

`sd_bus_message_set_destination()` sets the destination service name for the specified bus message object. The specified name must be a valid unique or well-known service name.

`sd_bus_message_get_destination()`, `sd_bus_message_get_path()`, `sd_bus_message_get_interface()`, and `sd_bus_message_get_member()` return the destination, path, interface, and member fields from *`message`* header. The return value will be `NULL` is *`message`* is `NULL` or the message is of a type that does not use those fields or the message does not have them set. See sd_bus_message_new_method_call(3) and sd_bus_message_set_destination(3) for more discussion of those values.

`sd_bus_message_set_sender()` sets the sender service name for the specified bus message object. The specified name must be a valid unique or well-known service name. This function is useful only for messages to send on direct connections as for connections to bus brokers the broker will fill in the destination field anyway, and the sender field set by original sender is ignored.

`sd_bus_message_get_sender()` returns the sender field from *`message`*.

When a string is returned, it is a pointer to internal storage, and may not be modified or freed. It is only valid as long as the *`message`* remains referenced and this field has not been changed by a different call.

## Return Value

On success, these calls return 0 or a positive integer. On failure, these calls return a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
The *`message`* parameter or the output parameter are `NULL`.

`-EPERM`  
For `sd_bus_message_set_destination()` and `sd_bus_message_set_sender()`, the message is already sealed.

`-EEXIST`  
The message already has a destination or sender field set.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_message_set_destination()` and `sd_bus_message_set_sender()` were added in version 237.

`sd_bus_message_get_destination()`, `sd_bus_message_get_path()`, `sd_bus_message_get_interface()`, `sd_bus_message_get_member()`, and `sd_bus_message_get_sender()` were added in version 240.

## See Also

systemd(1), sd-bus(3), sd_bus_new(3), sd_bus_set_sender(3)
