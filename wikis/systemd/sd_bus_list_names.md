## Name

sd_bus_list_names — Retrieve information about registered names on a bus

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                  |                              |
|----------------------------------|------------------------------|
| `int `**`sd_bus_list_names`**`(` | sd_bus \*`bus`,              |
|                                  | char \*\*\*`acquired`,       |
|                                  | char \*\*\*`activatable``)`; |

 

## Description

`sd_bus_list_names()` retrieves information about the registered names on a bus. If *`acquired`* is not `NULL`, this function calls org.freedesktop.DBus.ListNames to retrieve the list of currently-owned names on the bus. If *`acquired`* is not `NULL`, the function calls org.freedesktop.DBus.ListActivableNames to retrieve the list of all names on the bus that can be activated. Note that ownership of the arrays returned by `sd_bus_list_names()` in *`acquired`* and *`activatable`* is transferred to the caller and hence, the caller is responsible for freeing these arrays and their contents.

## Return Value

On success, `sd_bus_list_names()` returns a non-negative integer. On failure, it returns a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
*`bus`* or both *`acquired`* and *`activatable`* were `NULL`.

`-ENOPKG`  
The bus cannot be resolved.

`-ECHILD`  
The bus was created in a different process, library or module instance.

`-ENOMEM`  
Memory allocation failed.

`-ENOTCONN`  
The bus is not connected.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_list_names()` was added in version 221.

## See Also

systemd(1), sd-bus(3)
