## Name

sd_event_source_set_exit_on_failure, sd_event_source_get_exit_on_failure — Set or retrieve the exit-on-failure feature of event sources

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-event.h>
```

|  |  |
|----|----|
| `int `**`sd_event_source_set_exit_on_failure`**`(` | sd_event_source \*`source`, |
|   | int `b``)`; |

 

|  |  |
|----|----|
| `int `**`sd_event_source_get_exit_on_failure`**`(` | sd_event_source \*`source``)`; |

 

## Description

`sd_event_source_set_exit_on_failure()` may be used to set/unset the exit-on-failure flag of the event source object specified as *`source`*. The flag defaults to off. If on and the callback function set for the event source returns a failure code (i.e. a negative value) the event loop is exited too, using the callback return code as the exit code for sd_event_exit(3). If off, the event source is disabled but the event loop continues to run. Setting this flag is useful for "dominant" event sources that define the purpose and reason for the event loop, and whose failure hence should propagate to the event loop itself — as opposed to "auxiliary" event sources whose failures should remain local and affect the event source, but not propagate further.

`sd_event_source_get_exit_on_failure()` may be used to query the flag currently set for the event source object *`source`*.

## Return Value

On success, `sd_event_source_set_exit_on_failure()` returns a non-negative integer. `sd_event_source_get_exit_on_failure()` returns 0 if the flag is off, \> 0 if the flag is on. On failure, both return a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
*`source`* is not a valid pointer to an sd_event_source object.

Added in version 247.

`-EDOM`  
The event source refers to an exit event source (as created with sd_event_add_exit(3)), for which this functionality is not supported.

Added in version 247.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_event_source_set_exit_on_failure()` and `sd_event_source_get_exit_on_failure()` were added in version 247.

## See Also

sd-event(3), sd_event_add_io(3), sd_event_add_time(3), sd_event_add_signal(3), sd_event_add_child(3), sd_event_add_inotify(3), sd_event_add_defer(3)
