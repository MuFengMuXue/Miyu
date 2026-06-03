## Name

sd_device_enumerator_get_device_first, sd_device_enumerator_get_device_next, sd_device_enumerator_get_subsystem_first, sd_device_enumerator_get_subsystem_next — Enumerates devices and get the first or next device.

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-device.h>
```

|  |  |
|----|----|
| `sd_device *`**`sd_device_enumerator_get_device_first`**`(` | sd_device_enumerator \*`enumerator``)`; |

 

|  |  |
|----|----|
| `sd_device *`**`sd_device_enumerator_get_device_next`**`(` | sd_device_enumerator \*`enumerator``)`; |

 

|  |  |
|----|----|
| `sd_device *`**`sd_device_enumerator_get_subsystem_first`**`(` | sd_device_enumerator \*`enumerator``)`; |

 

|  |  |
|----|----|
| `sd_device *`**`sd_device_enumerator_get_subsystem_next`**`(` | sd_device_enumerator \*`enumerator``)`; |

 

## Description

The `sd_device_enumerator_get_device_first()` function enumerates all matching devices under `/sys/bus/`*`SUBSYSTEM`*`/devices/` and `/sys/class/`*`SUBSYSTEM`*`/devices/`, and returns a pointer to the first sd_device object. If no devices are found, `NULL` is returned.

The `sd_device_enumerator_get_device_next()` function returns the pointer to the next sd_device from the *`enumerator`*. It should be called after `sd_device_enumerator_get_device_first()` or after a previous call to this function. If no more devices are available, `NULL` is returned.

The `sd_device_enumerator_get_subsystem_first()` function enumerates all matching subsystem devices in `/sys/module/`, `/sys/bus/`, and `/sys/bus/`*`SUBSYSTEM`*`/drivers/` (such as `/sys/bus/pci/drivers/`). It returns a pointer to the first sd_device object. If no devices are found `NULL` is returned. Note that this does *not* enumerate devices provided by `sd_device_enumerator_get_device_first/next()`. Hence, e.g. `/sys/bus/pci/`, `/sys/bus/pci/drivers/ahci/` and so on are enumerated, but `/sys/bus/pci/devices/0000:00:00.0/` and so on are not.

The `sd_device_enumerator_get_subsystem_next()` function returns the next subsystem device from the enumerator. It should be called after `sd_device_enumerator_get_subsystem_first()` or after a previous call to this function. If no more subsystem devices are available, `NULL` is returned.

## Return Value

On success, these functions return a pointer to an sd_device object. On failure or when no more devices are available, `NULL` is returned. The returned pointers are owned by the enumerator and should not be freed by the caller.

## History

`sd_device_enumerator_get_device_first()`, `sd_device_enumerator_get_device_next()`, `sd_device_enumerator_get_subsystem_first()`, and `sd_device_enumerator_get_subsystem_next()` were introduced in systemd version 240.

## See Also

sd_device_enumerator_new(3), sd_device_enumerator_add_match_parent(3), sd_device_ref(3)
