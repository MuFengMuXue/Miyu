## Name

libudev — API for enumerating and introspecting local devices

## Synopsis

``` funcsynopsisinfo
#include <libudev.h>
```

`pkg-config --cflags --libs libudev`

## Description

`libudev.h` provides an API to introspect and enumerate devices on the local system. This library is supported, but should not be used in new projects. Please see sd-device(3) for an equivalent replacement with a more modern API.

All functions require a libudev context to operate. This context can be created via udev_new(3). It is used to track library state and link objects together. No global state is used by libudev, everything is always linked to a udev context.

All functions listed here are thread-agnostic and only a single thread may operate on a given object at any given time. Different threads may access the same object at different times. Multiple independent objects may be used from different threads in parallel.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

To introspect a local device on a system, a udev device object can be created via udev_device_new_from_syspath(3) and friends. The device object allows one to query current state, read and write attributes and lookup properties of the device in question.

To enumerate local devices on the system, an enumeration object can be created via udev_enumerate_new(3).

To monitor the local system for hotplugged or unplugged devices, a monitor can be created via udev_monitor_new_from_netlink(3).

Whenever libudev returns a list of objects, the udev_list_entry(3) API should be used to iterate, access and modify those lists.

Furthermore, libudev also exports legacy APIs that should not be used by new software (and as such are not documented as part of this manual). This includes the hardware database known as `udev_hwdb` (please use the new sd-hwdb(3) API instead) and the `udev_queue` object to query the udev daemon (which should not be used by new software at all).

## See Also

udev_new(3), udev_device_new_from_syspath(3), udev_enumerate_new(3), udev_monitor_new_from_netlink(3), udev_list_entry(3), systemd(1), sd-device(3), sd-hwdb(3), pkg-config(1)
