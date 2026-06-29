## Name

sd-device — API for enumerating and introspecting local devices

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-device.h>
```

`pkg-config --cflags --libs libsystemd`

## Description

`sd-device.h` is part of libsystemd(3) and provides an API to introspect and enumerate devices on the local system. It provides a programmatic interface to the database of devices and their properties mananaged by systemd-udevd.service(8). This API is a replacement for libudev(3) and `libudev.h`.

See

|                           |
|---------------------------|
| sd_device_get_syspath(3), |
| sd_device_ref(3)          |

for more information about the functions available.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## See Also

systemd(1), sd-event(3), udevadm(8)
