## Name

sd_varlink_set_relative_timeout — Set method call time-out

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-varlink.h>
```

|                                                |                      |
|------------------------------------------------|----------------------|
| `int `**`sd_varlink_set_relative_timeout`**`(` | sd_varlink \*`link`, |
|                                                | uint64_t `usec``)`;  |

 

## Description

`sd_varlink_set_relative_timeout()` sets the relative timeout in µs to enforce on Varlink method calls. A default time-out of 45s (currently) applies, which may be changed with this call. Set to `UINT64_MAX` to disable the time-out, and to 0 to revert to revert back to the default time-out. The time-out begins whenever a method call is started, and if no response is received by the time the time-out elapses a synthetic `io.systemd.TimedOut` error is raised as client-generated reply to the method call.

This call is particularly useful for method calls issued via `sd_varlink_observe()` that shall remain open continuously for a long time.

## Return Value

On success, `sd_varlink_set_relative_timeout()` returns a non-negative integer. On failure, it returns a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
An argument is invalid.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_varlink_set_relative_timeout()` was added in version 257.

## See Also

systemd(1), sd-varlink(3)
