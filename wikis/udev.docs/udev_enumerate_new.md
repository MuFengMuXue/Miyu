## Name

udev_enumerate_new, udev_enumerate_ref, udev_enumerate_unref — Create, acquire and release a udev enumerate object

## Synopsis

``` funcsynopsisinfo
#include <libudev.h>
```

|  |  |
|----|----|
| `struct udev_enumerate *`**`udev_enumerate_new`**`(` | struct udev \*`udev``)`; |

 

|  |  |
|----|----|
| `struct udev_enumerate *`**`udev_enumerate_ref`**`(` | struct udev_enumerate \*`udev_enumerate``)`; |

 

|  |  |
|----|----|
| `struct udev_enumerate *`**`udev_enumerate_unref`**`(` | struct udev_enumerate \*`udev_enumerate``)`; |

 

## Description

`udev_enumerate_new()` creates an enumeration context to scan `/sys/`.

`udev_enumerate_ref()` takes a reference of an enumeration context.

`udev_enumerate_unref()` drops a reference of an enumeration context. If the refcount reaches zero, all resources of the enumeration context will be released.

## Return Value

On success, `udev_enumerate_new()` returns a pointer to the allocated enumeration object. On failure, `NULL` is returned. `udev_enumerate_ref()` returns the argument that it was passed, unmodified. `udev_enumerate_unref()` always returns `NULL`.

## History

`udev_enumerate_new()`, `udev_enumerate_ref()`, and `udev_enumerate_unref()` were added in version 221.

## See Also

udev_new(3), udev_device_new_from_syspath(3), udev_enumerate_add_match_subsystem(3), udev_enumerate_scan_devices(3), udev_monitor_new_from_netlink(3), udev_list_entry(3), systemd(1)
