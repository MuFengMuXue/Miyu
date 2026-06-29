## Name

sd_varlink_set_description, sd_varlink_get_description — Set or query description of a Varlink connection object

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-varlink.h>
```

|                                           |                                |
|-------------------------------------------|--------------------------------|
| `int `**`sd_varlink_set_description`**`(` | sd_varlink \*`link`,           |
|                                           | const char \*`description``)`; |

 

|                                                   |                         |
|---------------------------------------------------|-------------------------|
| `const char* `**`sd_varlink_get_description`**`(` | sd_varlink \*`link``)`; |

 

## Description

`sd_varlink_set_description()` sets the description string that is used in logging to the specified string. The string is copied internally and freed when the Varlink connection object is deallocated. The *`description`* argument may be `NULL`, in which case the description is unset.

`sd_varlink_get_description()` returns a description string for the specified Varlink connection. This string may have been previously set with `sd_varlink_set_description()`. If not set this way, a default string or `NULL` may be returned, depending how the connection was allocated and set up.

## Return Value

On success, `sd_varlink_set_description()` returns a non-negative integer. On failure, it returns a negative errno-style error code. `sd_varlink_get_description()` returns either `NULL` or a pointer to the description string.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
An argument is invalid.

`-ENOMEM`  
Memory allocation failed.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_varlink_set_description()` was added in version 257.

`sd_varlink_get_description()` was added in version 258.

## See Also

systemd(1), sd-varlink(3)
