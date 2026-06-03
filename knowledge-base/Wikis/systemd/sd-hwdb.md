## Name

sd-hwdb — Read-only access to the hardware description database

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-hwdb.h>
```

`pkg-config --cflags --libs libsystemd`

## Description

`sd-hwdb.h` is part of libsystemd(3) and allows read-only access the systemd database of hardware properties. See hwdb(7) and systemd-hwdb(8) for more information about the database.

See sd_hwdb_new(3) and sd_hwdb_get(3) for information about the functions available.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## See Also

systemd(1), systemd-udevd.service(8)
