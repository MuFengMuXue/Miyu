## Name

sd_bus_interface_name_is_valid, sd_bus_service_name_is_valid, sd_bus_member_name_is_valid, sd_bus_object_path_is_valid — Check if a string is a valid bus name or object path

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                               |                      |
|-----------------------------------------------|----------------------|
| `int `**`sd_bus_interface_name_is_valid`**`(` | const char\* `p``)`; |

 

|                                             |                      |
|---------------------------------------------|----------------------|
| `int `**`sd_bus_service_name_is_valid`**`(` | const char\* `p``)`; |

 

|                                            |                      |
|--------------------------------------------|----------------------|
| `int `**`sd_bus_member_name_is_valid`**`(` | const char\* `p``)`; |

 

|                                            |                      |
|--------------------------------------------|----------------------|
| `int `**`sd_bus_object_path_is_valid`**`(` | const char\* `p``)`; |

 

## Description

`sd_bus_interface_name_is_valid()` checks if a given string *`p`* is a syntactically valid bus interface name. Similarly, `sd_bus_service_name_is_valid()` checks if the argument is a valid bus service name, `sd_bus_member_name_is_valid()` checks if the argument is a valid bus interface member name, and `sd_bus_object_path_is_valid()` checks if the argument is a valid bus object path. Those functions generally check that only allowed characters are used and that the length of the string is within limits.

## Return Value

Those functions return 1 if the argument is a valid interface / service / member name or object path, and 0 if it is not. If the argument is `NULL`, an error is returned.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
The *`p`* parameter is `NULL`.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_interface_name_is_valid()`, `sd_bus_service_name_is_valid()`, `sd_bus_member_name_is_valid()`, and `sd_bus_object_path_is_valid()` were added in version 246.

## See Also

systemd(1), sd-bus(3), sd_bus_call_method(3)
