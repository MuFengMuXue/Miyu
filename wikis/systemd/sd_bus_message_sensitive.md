## Name

sd_bus_message_sensitive — Mark a message object as containing sensitive data

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                         |                                |
|-----------------------------------------|--------------------------------|
| `int `**`sd_bus_message_sensitive`**`(` | sd_bus_message \*`message``)`; |

 

## Description

`sd_bus_message_sensitive()` marks an allocated bus message as containing sensitive data. This ensures that the message data is carefully removed from memory (specifically, overwritten with zero bytes) when released. It is recommended to mark all incoming and outgoing messages like this that contain security credentials and similar data that should be dealt with carefully. Note that it is not possible to unmark messages like this, it is a one way operation. If a message is already marked sensitive and then marked sensitive a second time the message remains marked so and no further operation is executed.

As a safety precaution all messages that are created as reply to messages that are marked sensitive are also implicitly marked so.

## Return Value

On success, this functions return 0 or a positive integer. On failure, it returns a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
The *`message`* parameter is `NULL`.

Added in version 245.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_message_sensitive()` was added in version 245.

## See Also

systemd(1), sd-bus(3), sd_bus_message_new_method_call(3)
