## Name

sd_event_now — Retrieve current event loop iteration timestamp

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-event.h>
```

|                             |                      |
|-----------------------------|----------------------|
| `int `**`sd_event_now`**`(` | sd_event \*`event`,  |
|                             | clockid_t `clock`,   |
|                             | uint64_t \*`ret``)`; |

 

## Description

`sd_event_now()` returns the time when the most recent event loop iteration began. A timestamp is taken right after returning from the event sleep, and before dispatching any event sources. The *`event`* parameter specifies the event loop object to retrieve the timestamp from. The *`clock`* parameter specifies the clock to retrieve the timestamp for, and is one of `CLOCK_REALTIME` (or equivalently `CLOCK_REALTIME_ALARM`), `CLOCK_MONOTONIC`, or `CLOCK_BOOTTIME` (or equivalently `CLOCK_BOOTTIME_ALARM`), see clock_gettime(2) for more information on the various clocks. The retrieved timestamp is stored in the *`ret`* parameter, in μs since the clock's epoch. If this function is invoked before the first event loop iteration, the current time is returned, as reported by `clock_gettime()`. To distinguish this case from a regular invocation the return value will be positive, and zero when the returned timestamp refers to an actual event loop iteration.

## Return Value

If the first event loop iteration has not run yet `sd_event_now()` writes current time to *`ret`* and returns a positive return value. Otherwise, it will write the requested timestamp to *`ret`* and return 0. On failure, the call returns a negative errno-style error code.

### Errors

Returned values may indicate the following problems:

`-EINVAL`  
An invalid parameter was passed.

`-EOPNOTSUPP`  
Unsupported clock type.

`-ECHILD`  
The event loop object was created in a different process, library or module instance.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_event_now()` was added in version 229.

## See Also

systemd(1), sd-event(3), sd_event_new(3), sd_event_add_time(3), clock_gettime(2)
