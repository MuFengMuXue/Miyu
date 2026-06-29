## Name

sd_bus_get_name_creds, sd_bus_get_owner_creds — Query bus client credentials

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                      |                              |
|--------------------------------------|------------------------------|
| `int `**`sd_bus_get_name_creds`**`(` | sd_bus \*`bus`,              |
|                                      | const char \*`name`,         |
|                                      | uint64_t `mask`,             |
|                                      | sd_bus_creds \*\*`creds``)`; |

 

|                                       |                              |
|---------------------------------------|------------------------------|
| `int `**`sd_bus_get_owner_creds`**`(` | sd_bus \*`bus`,              |
|                                       | uint64_t `mask`,             |
|                                       | sd_bus_creds \*\*`creds``)`; |

 

## Description

`sd_bus_get_name_creds()` queries the credentials of the bus client identified by *`name`*. The *`mask`* parameter is a combo of `SD_BUS_CREDS_*` flags that indicate which credential info the caller is interested in. See sd_bus_creds_new_from_pid(3) for a list of possible flags. On success, *`creds`* contains a new sd_bus_creds instance with the requested information. Ownership of this instance belongs to the caller and it should be freed once no longer needed by calling sd_bus_creds_unref(3).

`sd_bus_get_owner_creds()` queries the credentials of the creator of the given bus. The *`mask`* and *`creds`* parameters behave the same as in `sd_bus_get_name_creds()`.

## Return Value

On success, these functions return a non-negative integer. On failure, they return a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
An argument is invalid.

`-ENOPKG`  
The bus cannot be resolved.

`-EPERM`  
The bus has already been started.

`-ECHILD`  
The bus was created in a different process, library or module instance.

`-ENOMEM`  
Memory allocation failed.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_get_name_creds()` and `sd_bus_get_owner_creds()` were added in version 221.

## See Also

systemd(1), sd-bus(3), sd_bus_creds_unref(3)
