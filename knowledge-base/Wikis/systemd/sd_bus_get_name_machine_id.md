## Name

sd_bus_get_name_machine_id — Retrieve a bus client's machine identity

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                           |                            |
|-------------------------------------------|----------------------------|
| `int `**`sd_bus_get_name_machine_id`**`(` | sd_bus \*`bus`,            |
|                                           | const char \*`name`,       |
|                                           | sd_id128_t \*`machine``)`; |

 

## Description

`sd_bus_get_name_machine_id()` retrieves the D-Bus machine identity of the machine that the bus client identified by *`name`* is running on. Internally, it calls the `GetMachineId` method of the `org.freedesktop.DBus.Peer` interface. The D-Bus machine identity is a 128-bit UUID. On Linux systems running systemd, this corresponds to the contents of `/etc/machine-id`. On success, the machine identity is stored in *`machine`*.

## Return Value

On success, this function returns a non-negative integer. On failure, it returns a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
An argument is invalid.

`-ENOPKG`  
The bus cannot be resolved.

`-ECHILD`  
The bus was created in a different process, library or module instance.

`-ENOMEM`  
Memory allocation failed.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_get_name_machine_id()` was added in version 221.

## See Also

systemd(1), sd-bus(3)
