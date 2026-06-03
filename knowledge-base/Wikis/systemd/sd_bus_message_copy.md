## Name

sd_bus_message_copy — Copy the contents of one message to another

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                            |                            |
|----------------------------|----------------------------|
| `int sd_bus_message_copy(` | sd_bus_message \*`m`,      |
|                            | sd_bus_message \*`source`, |
|                            | int `all``)`;              |

 

## Description

`sd_bus_message_copy()` copies the contents from message *`source`* to *`m`*. If *`all`* is false, a single complete type is copied (basic or container). If *`all`* is true, the contents are copied until the end of the currently open container or the end of *`source`*.

## Return Value

On success, this call returns true if anything was copied, and false if there was nothing to copy. On failure, it returns a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
*`source`* or *`m`* are `NULL`.

`-EPERM`  
Message *`m`* has been sealed or *`source`* has *not* been sealed.

`-ESTALE`  
Destination message is in invalid state.

`-ENXIO`  
Destination message cannot be appended to.

`-ENOMEM`  
Memory allocation failed.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## See Also

systemd(1), sd-bus(3), sd_bus_message_append(3)
