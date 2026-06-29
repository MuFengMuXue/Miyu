## Name

sd_id128_randomize — Generate 128-bit IDs

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-id128.h>
```

|                                   |                        |
|-----------------------------------|------------------------|
| `int `**`sd_id128_randomize`**`(` | sd_id128_t \*`ret``)`; |

 

## Description

`sd_id128_randomize()` generates a new randomized 128-bit ID and returns it in *`ret`*. Every invocation returns a new randomly generated ID. This uses the getrandom(2) kernel random number generator.

Note that `sd_id128_randomize()` always returns a UUID Variant 1 Version 4 compatible ID. It is hence guaranteed that this function will never return the ID consisting of all zero or all one bits (`SD_ID128_NULL`, `SD_ID128_ALLF`).

For more information about the "`sd_id128_t`" type, see sd-id128(3).

systemd-id128(1)'s **new** command may be used as a command line front-end for `sd_id128_randomize()`.

## Return Value

The call returns 0 on success (in which case *`ret`* is filled in), or a negative errno-style error code.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_id128_randomize()` was added in version 187.

## See Also

systemd(1), sd-id128(3), machine-id(5), getrandom(2), random(4), sd_id128_get_machine(3)
