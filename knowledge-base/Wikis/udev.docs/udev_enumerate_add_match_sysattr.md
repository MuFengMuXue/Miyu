## Name

udev_enumerate_add_match_subsystem, udev_enumerate_add_nomatch_subsystem, udev_enumerate_add_match_sysattr, udev_enumerate_add_nomatch_sysattr, udev_enumerate_add_match_property, udev_enumerate_add_match_sysname, udev_enumerate_add_match_tag, udev_enumerate_add_match_parent, udev_enumerate_add_match_is_initialized — Modify filters

## Synopsis

``` funcsynopsisinfo
#include <libudev.h>
```

|  |  |
|----|----|
| `int `**`udev_enumerate_add_match_subsystem`**`(` | struct udev_enumerate \*`udev_enumerate`, |
|   | const char \*`subsystem``)`; |

 

|  |  |
|----|----|
| `int `**`udev_enumerate_add_nomatch_subsystem`**`(` | struct udev_enumerate \*`udev_enumerate`, |
|   | const char \*`subsystem``)`; |

 

|  |  |
|----|----|
| `int `**`udev_enumerate_add_match_sysattr`**`(` | struct udev_enumerate \*`udev_enumerate`, |
|   | const char \*`sysattr`, |
|   | const char \*`value``)`; |

 

|  |  |
|----|----|
| `int `**`udev_enumerate_add_nomatch_sysattr`**`(` | struct udev_enumerate \*`udev_enumerate`, |
|   | const char \*`sysattr`, |
|   | const char \*`value``)`; |

 

|  |  |
|----|----|
| `int `**`udev_enumerate_add_match_property`**`(` | struct udev_enumerate \*`udev_enumerate`, |
|   | const char \*`property`, |
|   | const char \*`value``)`; |

 

|  |  |
|----|----|
| `int `**`udev_enumerate_add_match_sysname`**`(` | struct udev_enumerate \*`udev_enumerate`, |
|   | const char \*`sysname``)`; |

 

|  |  |
|----|----|
| `int `**`udev_enumerate_add_match_tag`**`(` | struct udev_enumerate \*`udev_enumerate`, |
|   | const char \*`tag``)`; |

 

|  |  |
|----|----|
| `int `**`udev_enumerate_add_match_parent`**`(` | struct udev_enumerate \*`udev_enumerate`, |
|   | struct udev_device \*`parent``)`; |

 

|  |  |
|----|----|
| `int `**`udev_enumerate_add_match_is_initialized`**`(` | struct udev_enumerate \*`udev_enumerate``)`; |

 

## Return Value

On success, `udev_enumerate_add_match_subsystem()`, `udev_enumerate_add_nomatch_subsystem()`, `udev_enumerate_add_match_sysattr()`, `udev_enumerate_add_nomatch_sysattr()`, `udev_enumerate_add_match_property()`, `udev_enumerate_add_match_sysname()`, `udev_enumerate_add_match_tag()`, `udev_enumerate_add_match_parent()` and `udev_enumerate_add_match_is_initialized()` return an integer greater than, or equal to, `0`.

## History

`udev_enumerate_add_match_subsystem()`, `udev_enumerate_add_nomatch_subsystem()`, `udev_enumerate_add_match_sysattr()`, `udev_enumerate_add_nomatch_sysattr()`, `udev_enumerate_add_match_property()`, `udev_enumerate_add_match_sysname()`, `udev_enumerate_add_match_tag()`, `udev_enumerate_add_match_parent()`, and `udev_enumerate_add_match_is_initialized()` were added in version 221.

## See Also

udev_new(3), udev_device_new_from_syspath(3), udev_enumerate_new(3), udev_enumerate_scan_devices(3), udev_monitor_new_from_netlink(3), udev_list_entry(3), systemd(1)
