## Name

sd_hwdb_new, sd_hwdb_new_from_path, sd_hwdb_ref, sd_hwdb_unref — Create a new hwdb object and create or destroy references to it

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-hwdb.h>
```

|                            |                        |
|----------------------------|------------------------|
| `int `**`sd_hwdb_new`**`(` | sd_hwdb \*\*`hwdb``)`; |

 

|                                      |                        |
|--------------------------------------|------------------------|
| `int `**`sd_hwdb_new_from_path`**`(` | const char \*`path`,   |
|                                      | sd_hwdb \*\*`hwdb``)`; |

 

|                                 |                      |
|---------------------------------|----------------------|
| `sd_hwdb* `**`sd_hwdb_ref`**`(` | sd_hwdb \*`hwdb``)`; |

 

|                                   |                      |
|-----------------------------------|----------------------|
| `sd_hwdb* `**`sd_hwdb_unref`**`(` | sd_hwdb \*`hwdb``)`; |

 

## Description

`sd_hwdb_new()` creates a new hwdb object to access the binary hwdb database. Upon initialization, the file containing the binary representation of the hardware database is located and opened. The new object is returned in *`hwdb`*.

`sd_hwdb_new_from_path()` may be used to specify the path from which the binary hardware database should be opened.

The *`hwdb`* object is reference counted. `sd_hwdb_ref()` and `sd_hwdb_unref()` may be used to get a new reference or destroy an existing reference to an object. The caller must dispose of the reference acquired with `sd_hwdb_new()` by calling `sd_hwdb_unref()` when done with the object.

Use sd_hwdb_seek(3), sd_hwdb_get(3), and sd_hwdb_enumerate(3) to access entries.

## Return Value

On success, `sd_hwdb_new()` and `sd_hwdb_new_from_path()` return a non-negative integer. On failure, a negative errno-style error code is returned.

`sd_hwdb_ref()` always returns the argument.

`sd_hwdb_unref()` always returns `NULL`.

### Errors

Returned errors may indicate the following problems:

`-ENOENT`  
The binary hardware database file could not be located. See systemd-hwdb(8) for more information.

Added in version 246.

`-EINVAL`  
The located binary hardware database file is in an incompatible format.

Added in version 246.

`-ENOMEM`  
Memory allocation failed.

Added in version 246.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_hwdb_new()`, `sd_hwdb_ref()`, and `sd_hwdb_unref()` were added in version 246.

`sd_hwdb_new_from_path()` was added in version 252.

## See Also

systemd(1), systemd-udevd.service(8), sd-hwdb(3), systemd-hwdb(8)
