## Name

udev_list_entry, udev_list_entry_get_next, udev_list_entry_get_by_name, udev_list_entry_get_name, udev_list_entry_get_value — Iterate and access udev lists

## Synopsis

``` funcsynopsisinfo
#include <libudev.h>
```

|  |  |
|----|----|
| `struct udev_list_entry *`**`udev_list_entry_get_next`**`(` | struct udev_list_entry \*`list_entry``)`; |

 

|  |  |
|----|----|
| `struct udev_list_entry *`**`udev_list_entry_get_by_name`**`(` | struct udev_list_entry \*`list_entry`, |
|   | const char \*`name``)`; |

 

|  |  |
|----|----|
| `const char *`**`udev_list_entry_get_name`**`(` | struct udev_list_entry \*`list_entry``)`; |

 

|  |  |
|----|----|
| `const char *`**`udev_list_entry_get_value`**`(` | struct udev_list_entry \*`list_entry``)`; |

 

## Return Value

On success, `udev_list_entry_get_next()` and `udev_list_entry_get_by_name()` return a pointer to the requested list entry. If no such entry can be found, or on failure, `NULL` is returned.

On success, `udev_list_entry_get_name()` and `udev_list_entry_get_value()` return a pointer to a constant string representing the requested value. The string is bound to the lifetime of the list entry itself. On failure, `NULL` is returned.

## History

`udev_list_entry_get_next()`, `udev_list_entry_get_by_name()`, `udev_list_entry_get_name()`, and `udev_list_entry_get_value()` were added in version 221.

## See Also

udev_new(3), udev_device_new_from_syspath(3), udev_enumerate_new(3), udev_monitor_new_from_netlink(3), systemd(1)
