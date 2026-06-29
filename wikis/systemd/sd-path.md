## Name

sd-path — APIs to query file system paths

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-path.h>
```

`pkg-config --cflags --libs libsystemd`

## Description

`sd-path.h` is part of libsystemd(3) and provides APIs to query file system paths. This functionality is similar to the command-line functionality provided by systemd-path(1).

See sd_path_lookup(3) for information about the functions available.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## See Also

systemd(1), systemd-path(1), pkg-config(1)
