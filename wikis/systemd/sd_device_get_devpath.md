## Name

sd_device_get_syspath, sd_device_get_devpath, sd_device_get_sysname, sd_device_get_sysnum, sd_device_get_subsystem, sd_device_get_driver_subsystem, sd_device_get_devtype, sd_device_get_devname, sd_device_get_devnum, sd_device_get_ifindex, sd_device_get_driver, sd_device_get_diskseq, sd_device_get_device_id — Returns various fields of device objects

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-device.h>
```

|                                      |                          |
|--------------------------------------|--------------------------|
| `int `**`sd_device_get_syspath`**`(` | sd_device \*`device`,    |
|                                      | const char \*\*`ret``)`; |

 

|                                      |                          |
|--------------------------------------|--------------------------|
| `int `**`sd_device_get_devpath`**`(` | sd_device \*`device`,    |
|                                      | const char \*\*`ret``)`; |

 

|                                      |                          |
|--------------------------------------|--------------------------|
| `int `**`sd_device_get_sysname`**`(` | sd_device \*`device`,    |
|                                      | const char \*\*`ret``)`; |

 

|                                     |                          |
|-------------------------------------|--------------------------|
| `int `**`sd_device_get_sysnum`**`(` | sd_device \*`device`,    |
|                                     | const char \*\*`ret``)`; |

 

|                                        |                          |
|----------------------------------------|--------------------------|
| `int `**`sd_device_get_subsystem`**`(` | sd_device \*`device`,    |
|                                        | const char \*\*`ret``)`; |

 

|                                               |                          |
|-----------------------------------------------|--------------------------|
| `int `**`sd_device_get_driver_subsystem`**`(` | sd_device \*`device`,    |
|                                               | const char \*\*`ret``)`; |

 

|                                      |                          |
|--------------------------------------|--------------------------|
| `int `**`sd_device_get_devtype`**`(` | sd_device \*`device`,    |
|                                      | const char \*\*`ret``)`; |

 

|                                      |                          |
|--------------------------------------|--------------------------|
| `int `**`sd_device_get_devname`**`(` | sd_device \*`device`,    |
|                                      | const char \*\*`ret``)`; |

 

|                                     |                       |
|-------------------------------------|-----------------------|
| `int `**`sd_device_get_devnum`**`(` | sd_device \*`device`, |
|                                     | dev_t \*`ret``)`;     |

 

|                                      |                       |
|--------------------------------------|-----------------------|
| `int `**`sd_device_get_ifindex`**`(` | sd_device \*`device`, |
|                                      | int \*`ret``)`;       |

 

|                                     |                          |
|-------------------------------------|--------------------------|
| `int `**`sd_device_get_driver`**`(` | sd_device \*`device`,    |
|                                     | const char \*\*`ret``)`; |

 

|                                      |                       |
|--------------------------------------|-----------------------|
| `int `**`sd_device_get_diskseq`**`(` | sd_device \*`device`, |
|                                      | uint64_t \*`ret``)`;  |

 

|                                        |                          |
|----------------------------------------|--------------------------|
| `int `**`sd_device_get_device_id`**`(` | sd_device \*`device`,    |
|                                        | const char \*\*`ret``)`; |

 

## Description

`sd_device_get_syspath()` returns the sysfs path of the specified device record, including the `/sys` prefix. Example: `/sys/devices/virtual/tty/tty7`

`sd_device_get_devpath()` returns the sysfs path of the specified device record, excluding the `/sys` prefix. Example: `/devices/virtual/tty/tty7`

`sd_device_get_sysname()` returns the sysfs name of the specified device record, i.e. the last component of the sysfs path. Example: "`tty7`" for the device `/sys/devices/virtual/tty/tty7`

`sd_device_get_sysnum()` returns the sysfs device number of the specified device record, i.e. the numeric suffix of the last component of the sysfs path. Example: "`7`" for the device `/sys/devices/virtual/tty/tty7`

`sd_device_get_subsystem()` returns the kernel subsystem of the specified device record. This is a short string fitting into a filename, and thus does not contain a slash and cannot be empty. Example: "`tty`", "`block`" or "`net`".

`sd_device_get_driver_subsystem()` returns the connected bus type of the devices loaded by the specified driver device record. For example, when "`iwlwifi`" driver device is specified, which is used by the wireless network interfaces connected to PCI bus, this function returns "`pci`". This function only succeeds when `sd_device_get_subsystem()` returns "`drivers`". Example: "`pci`", "`i2c`", or "`hid`".

`sd_device_get_devtype()` returns the device type of the specified device record, if the subsystem manages multiple types of devices. Example: for devices of the "`block`" subsystem this can be "`disk`" or "`partition`"

`sd_device_get_devname()` returns the device node path of the specified device record if the device has a device node. Example: for `/sys/devices/virtual/tty/tty7` the string `/dev/tty7` is typically returned.

`sd_device_get_devnum()` returns the device node major/minor (i.e. dev_t) of the specified device record if the device has a device node (i.e. the one returned by `sd_device_get_devname()`). For devices belonging to the "`block`" subsystem this refers to a block device node, in all other cases to a character device node. Example: for the `/sys/devices/virtual/tty/tty7` device this typically returns the device number with major/minor "`4:7`".

`sd_device_get_ifindex()` returns the network interface index of the specified device record, if the device encapsulates a network interface device, i.e. belongs to the "`net`" subsystem. Example: the "`lo`" interface typically has interface index 1.

`sd_device_get_driver()` returns the kernel driver name attached to the device. Note that the driver field is set on the devices consumed by the driver, not on the device created by it. Example: a PCI device `/sys/bus/pci/devices/0000:00:1f.6` might be attached to a driver "`e1000e`".

`sd_device_get_diskseq()` returns the kernel disk sequence number of the block device. This number monotonically increases whenever a backing medium of a block device changes without the device name changing, and is relevant for block devices encapsulating devices with changing media (e.g. floppy or CD-ROM), or loopback block devices. Only defined for block devices, i.e. those of subsystem "`block`".

`sd_device_get_device_id()` returns the short string that identifies the device record. When the device ID obtained by the function for a specified device record is passed to `sd_device_new_from_device_id()`, a new instance of the same device record will be gained. When a block or character device is specified, which has corresponding device node, this returns "`b`" or "`c`", respectively, followed by the device node major and minor numbers separated with a colon. Example: "`b259:1`" or "`c10:121`". When a network interface device is specified, this returns "`n`" followed by the interface index, which can be obtained by `sd_device_get_ifindex()`. Example: "`n1`". When a device in the "`driver`" subsystem is specified, this returns "`+drivers:`" followed by its driver subsystem and sysfs name separated with a colon. Example: "`+drivers:pci:iwlwifi`" for a driver device record whose driver subsystem is "`pci`" and sysfs name is "`iwlwifi`", When another type of device is specified, this function returns "`+`" followed by its subsystem and sysfs name separated with a colon. Example: "`+acpi:ACPI0003:00`", "`+input:input16`", or "`+pci:0000:00:1f.6`".

## Return Value

On success, these calls return 0 or a positive integer. On failure, they return a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
A specified parameter is invalid.

Added in version 251.

`-ENOENT`  
The requested field is not present in the device record.

Added in version 251.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_device_get_syspath()`, `sd_device_get_devpath()`, `sd_device_get_sysname()`, `sd_device_get_sysnum()`, `sd_device_get_subsystem()`, `sd_device_get_devtype()`, `sd_device_get_devname()`, `sd_device_get_devnum()`, `sd_device_get_ifindex()`, `sd_device_get_driver()`, and `sd_device_get_diskseq()` were added in version 251.

`sd_device_get_driver_subsystem()` and `sd_device_get_device_id()` were added in version 257.

## See Also

systemd(1), sd-device(3)
