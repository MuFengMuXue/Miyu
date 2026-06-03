## Name

udev_monitor_filter_update, udev_monitor_filter_remove, udev_monitor_filter_add_match_subsystem_devtype, udev_monitor_filter_add_match_tag — Modify filters

## Synopsis

``` funcsynopsisinfo
#include <libudev.h>
```

|  |  |
|----|----|
| `int `**`udev_monitor_filter_update`**`(` | struct udev_monitor \*`udev_monitor``)`; |

 

|  |  |
|----|----|
| `int `**`udev_monitor_filter_remove`**`(` | struct udev_monitor \*`udev_monitor``)`; |

 

|  |  |
|----|----|
| `int `**`udev_monitor_filter_add_match_subsystem_devtype`**`(` | struct udev_monitor \*`udev_monitor`, |
|   | const char \*`subsystem`, |
|   | const char \*`devtype``)`; |

 

|  |  |
|----|----|
| `int `**`udev_monitor_filter_add_match_tag`**`(` | struct udev_monitor \*`udev_monitor`, |
|   | const char \*`tag``)`; |

 

## Return Value

On success, `udev_monitor_filter_update()`, `udev_monitor_filter_remove()`, `udev_monitor_filter_add_match_subsystem_devtype()` and `udev_monitor_filter_add_match_tag()` return an integer greater than, or equal to, `0`. On failure, a negative error code is returned.

## History

`udev_monitor_filter_update()`, `udev_monitor_filter_remove()`, `udev_monitor_filter_add_match_subsystem_devtype()`, and `udev_monitor_filter_add_match_tag()` were added in version 221.

## See Also

udev_new(3), udev_device_new_from_syspath(3), udev_enumerate_new(3), udev_monitor_new_from_netlink(3), udev_monitor_receive_device(3), udev_list_entry(3), systemd(1)
