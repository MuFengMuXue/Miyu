## Name

udev_new, udev_ref, udev_unref — Create, acquire and release a udev context object

## Synopsis

``` funcsynopsisinfo
#include <libudev.h>
```

|                                  |            |
|----------------------------------|------------|
| `struct udev *`**`udev_new`**`(` | `void``)`; |

 

|                                  |                          |
|----------------------------------|--------------------------|
| `struct udev *`**`udev_ref`**`(` | struct udev \*`udev``)`; |

 

|                                    |                          |
|------------------------------------|--------------------------|
| `struct udev *`**`udev_unref`**`(` | struct udev \*`udev``)`; |

 

## Description

`udev_new()` allocates a new udev context object and returns a pointer to it. This object is opaque and must not be accessed by the caller via different means than functions provided by libudev. Initially, the reference count of the context is 1. You can acquire further references, and drop gained references via `udev_ref()` and `udev_unref()`. Once the reference count hits 0, the context object is destroyed and freed.

## Return Value

On success, `udev_new()` returns a pointer to the allocated udev context. On failure, `NULL` is returned. `udev_ref()` returns the argument that it was passed, unmodified. `udev_unref()` always returns `NULL`.

## History

`udev_new()`, `udev_ref()`, and `udev_unref()` were added in version 221.

## See Also

systemd(1), systemd-udevd.service(8)
