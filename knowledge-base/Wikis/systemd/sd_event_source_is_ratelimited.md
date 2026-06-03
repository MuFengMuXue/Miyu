## Name

sd_event_source_set_ratelimit, sd_event_source_get_ratelimit, sd_event_source_is_ratelimited, sd_event_source_set_ratelimit_expire_callback, sd_event_source_leave_ratelimit — Configure rate limiting on event sources

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-event.h>
```

|                                              |                             |
|----------------------------------------------|-----------------------------|
| `int `**`sd_event_source_set_ratelimit`**`(` | sd_event_source \*`source`, |
|                                              | uint64_t `interval_usec`,   |
|                                              | unsigned `burst``)`;        |

 

|  |  |
|----|----|
| `int `**`sd_event_source_get_ratelimit`**`(` | sd_event_source \*`source`, |
|   | uint64_t\* `ret_interval_usec`, |
|   | unsigned\* `ret_burst``)`; |

 

|  |  |
|----|----|
| `int `**`sd_event_source_is_ratelimited`**`(` | sd_event_source \*`source``)`; |

 

|  |  |
|----|----|
| `int `**`sd_event_source_set_ratelimit_expire_callback`**`(` | sd_event_source \*`source`, |
|   | sd_event_handler_t`callback``)`; |

 

|  |  |
|----|----|
| `int `**`sd_event_source_leave_ratelimit`**`(` | sd_event_source \*`source``)`; |

 

## Description

`sd_event_source_set_ratelimit()` may be used to enforce rate limiting on an event source. When used an event source will be temporarily turned off when it fires more often then a specified burst number within a specified time interval. This is useful as simple mechanism to avoid event source starvation if high priority event sources fire very frequently.

Pass the event source to operate on as first argument, a time interval in microseconds as second argument and a maximum dispatch limit ("burst") as third parameter. Whenever the event source is dispatched more often than the specified burst within the specified interval it is placed in a mode similar to being disabled with sd_event_source_set_enabled(3) and the `SD_EVENT_OFF` parameter. However, it is disabled only temporarily – once the specified interval is over regular operation resumes. It is again disabled temporarily once the specified rate limiting is hit the next time. If either the interval or the burst value are specified as zero, rate limiting is turned off. By default, event sources do not have rate limiting enabled. Note that rate limiting and disabling via `sd_event_source_set_enabled()` are independent of each other, and an event source will only effect event loop wake-ups and is dispatched while it both is enabled and rate limiting is not in effect.

`sd_event_source_get_ratelimit()` may be used to query the current rate limiting parameters set on the event source object *`source`*. The previously set interval and burst vales are returned in the second and third argument.

`sd_event_source_is_ratelimited()` may be used to query whether the event source is currently affected by rate limiting, i.e. it has recently hit the rate limit and is currently temporarily disabled due to that.

`sd_event_source_set_ratelimit_expire_callback()` may be used to set a callback function that is invoked every time the event source leaves rate limited state. Note that function is called in the same event loop iteration in which state transition occurred.

`sd_event_source_leave_ratelimit()` may be used to immediately reenable an event source that was temporarily disabled due to rate limiting. This will reset the ratelimit counters for the current time interval.

Rate limiting is currently implemented for I/O, timer, signal, defer and inotify event sources.

## Return Value

On success, `sd_event_source_set_ratelimit()`, `sd_event_source_set_ratelimit_expire_callback` and `sd_event_source_get_ratelimit()` return a non-negative integer. On failure, they return a negative errno-style error code. `sd_event_source_is_ratelimited()` returns zero if rate limiting is currently not in effect and greater than zero if it is in effect; it returns a negative errno-style error code on failure. `sd_event_source_leave_ratelimit()` returns zero if rate limiting was not in effect on the specified event source, and positive if it was and rate limiting is now turned off again; it returns a negative errno-style error code on failure.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
*`source`* is not a valid pointer to an sd_event_source object.

Added in version 248.

`-ECHILD`  
The event loop has been created in a different process, library or module instance.

Added in version 248.

`-EDOM`  
It was attempted to use the rate limiting feature on an event source type that does not support rate limiting.

Added in version 248.

`-ENOEXEC`  
`sd_event_source_get_ratelimit()` was called on an event source that does not have rate limiting configured.

Added in version 248.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_event_source_set_ratelimit()`, `sd_event_source_get_ratelimit()`, and `sd_event_source_is_ratelimited()` were added in version 248.

`sd_event_source_set_ratelimit_expire_callback()` was added in version 250.

`sd_event_source_leave_ratelimit()` was added in version 254.

## See Also

sd-event(3), sd_event_add_io(3), sd_event_add_time(3), sd_event_add_signal(3), sd_event_add_inotify(3), sd_event_add_defer(3), sd_event_source_set_enabled(3)
