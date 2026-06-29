## Name

sd_bus_error_add_map, sd_bus_error_map, SD_BUS_ERROR_MAP, SD_BUS_ERROR_END — Additional sd-dbus error mappings

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

``` funcsynopsisinfo
typedef struct {
        const char *name;
        int code;
        …
} sd_bus_error_map;
```

``` funcsynopsisinfo
SD_BUS_ERROR_MAP(name, code)
```

``` funcsynopsisinfo
SD_BUS_ERROR_MAP_END
```

|                                     |                                    |
|-------------------------------------|------------------------------------|
| `int `**`sd_bus_error_add_map`**`(` | const sd_bus_error_map \*`map``)`; |

 

## Description

The `sd_bus_error_add_map()` call may be used to register additional mappings for converting D-Bus errors to Linux `errno`-style errors. The mappings defined with this call are consulted by calls such as sd_bus_error_set(3) or sd_bus_error_get_errno(3). By default, a number of generic, standardized mappings are known, as documented in sd-bus-errors(3). Use this call to add further, application-specific mappings.

The function takes a pointer to an array of sd_bus_error_map structures. A reference to the specified array is added to the lookup tables for error mappings. Note that the structure is not copied, and that it is hence essential that the array stays available and constant during the entire remaining runtime of the process.

The mapping array should be put together with a series of `SD_BUS_ERROR_MAP()` macro invocations that take a literal name string and a (positive) `errno`-style error number. The last entry of the array should be an invocation of the `SD_BUS_ERROR_MAP_END` macro. The array should not be put together without use of these two macros.

Note that the call is idempotent: it is safe to invoke it multiple times with the parameter, which will only add the passed mapping array once.

Note that the memory allocated by this call is not intended to be freed during the lifetime of the process. It should not be freed explicitly.

## Return Value

`sd_bus_error_add_map()` returns a positive value when the new array was added to the lookup tables. It returns zero when the same array was already added before. On error, a negative `errno`-style error code is returned. See below for known error codes.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
The specified mapping array is invalid.

`-ENOMEM`  
Memory allocation failed.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_error_add_map()` was added in version 221.

## See Also

systemd(1), sd-bus(3), sd_bus_error(3), sd-bus-errors(3), errno(3), strerror_r(3)
