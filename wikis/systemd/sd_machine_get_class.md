## Name

sd_machine_get_class, sd_machine_get_ifindices — Determine the class and network interface indices of a locally running virtual machine or container

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-login.h>
```

|                                     |                         |
|-------------------------------------|-------------------------|
| `int `**`sd_machine_get_class`**`(` | const char\* `machine`, |
|                                     | char \*\*`class``)`;    |

 

|                                         |                             |
|-----------------------------------------|-----------------------------|
| `int `**`sd_machine_get_ifindices`**`(` | const char\* `machine`,     |
|                                         | int \*\*`ret_ifindices``)`; |

 

## Description

`sd_machine_get_class()` may be used to determine the class of a locally running virtual machine or container that is registered with systemd-machined.service(8). The string returned is either "`vm`" or "`container`". The returned string needs to be freed with the libc free(3) call after use.

`sd_machine_get_ifindices()` may be used to determine the numeric indices of the network interfaces on the host that are pointing towards the specified locally running virtual machine or container. The vm or container must be registered with systemd-machined.service(8). The output parameter *`ret_ifindices`* may be passed as `NULL` when the output value is not needed. The returned array needs to be freed with the libc free(3) call after use.

## Return Value

On success, these functions return a non-negative integer. `sd_machine_get_ifindices()` returns the number of the relevant network interfaces. On failure, these calls return a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-ENXIO`  
The specified machine does not exist or is currently not running.

`-EINVAL`  
An input parameter was invalid (out of range, or `NULL`, where that is not accepted).

`-ENOMEM`  
Memory allocation failed.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_machine_get_class()` and `sd_machine_get_ifindices()` were added in version 217.

## See Also

systemd(1), sd-login(3), systemd-machined.service(8), sd_pid_get_machine_name(3)
