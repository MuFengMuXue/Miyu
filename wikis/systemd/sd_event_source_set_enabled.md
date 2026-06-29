## Name

sd_event_source_set_enabled, sd_event_source_get_enabled, SD_EVENT_ON, SD_EVENT_OFF, SD_EVENT_ONESHOT — Enable or disable event sources

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-event.h>
```

``` funcsynopsisinfo
enum {
        SD_EVENT_OFF = 0,
        SD_EVENT_ON = 1,
        SD_EVENT_ONESHOT = -1,
};
```

|                                            |                             |
|--------------------------------------------|-----------------------------|
| `int `**`sd_event_source_set_enabled`**`(` | sd_event_source \*`source`, |
|                                            | int `enabled``)`;           |

 

|                                            |                             |
|--------------------------------------------|-----------------------------|
| `int `**`sd_event_source_get_enabled`**`(` | sd_event_source \*`source`, |
|                                            | int \*`ret``)`;             |

 

## Description

`sd_event_source_set_enabled()` may be used to enable or disable the event source object specified as *`source`*. The *`enabled`* parameter takes one of `SD_EVENT_ON` (to enable), `SD_EVENT_OFF` (to disable) or `SD_EVENT_ONESHOT`. If invoked with `SD_EVENT_ONESHOT` the event source will be enabled but automatically reset to `SD_EVENT_OFF` after one dispatch. For `SD_EVENT_OFF`, the event source *`source`* may be `NULL`, in which case the function does nothing. Otherwise, *`source`* must be a valid pointer to an sd_event_source object.

Event sources that are disabled will not result in event loop wakeups and will not be dispatched, until they are enabled again.

`sd_event_source_get_enabled()` may be used to query whether the event source object *`source`* is currently enabled or not. If both the *`source`* and the output parameter *`ret`* are `NULL`, this function returns false. Otherwise, *`source`* must be a valid pointer to an sd_event_source object. If the output parameter *`ret`* is not `NULL`, it is set to the enablement state (one of `SD_EVENT_ON`, `SD_EVENT_OFF`, `SD_EVENT_ONESHOT`). The function also returns true if the event source is not disabled.

Event source objects are enabled when they are first created with calls such as sd_event_add_io(3), sd_event_add_time(3). However, depending on the event source type they are enabled continuously (`SD_EVENT_ON`) or only for a single invocation of the event source handler (`SD_EVENT_ONESHOT`). For details see the respective manual pages.

As event source objects stay active and may be dispatched as long as there is at least one reference to them, in many cases it is a good idea to combine a call to sd_event_source_unref(3) with a prior call to `sd_event_source_set_enabled()` with `SD_EVENT_OFF`, to ensure the event source is not dispatched again until all other remaining references are dropped.

## Return Value

On success, `sd_event_source_set_enabled()` returns a non-negative integer. `sd_event_source_get_enabled()` returns zero if the source is disabled (`SD_EVENT_OFF`) and a positive integer otherwise. On failure, they return a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
*`source`* is not a valid pointer to an sd_event_source object.

`-ENOMEM`  
Not enough memory.

`-ECHILD`  
The event loop has been created in a different process, library or module instance.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_event_source_set_enabled()` and `sd_event_source_get_enabled()` were added in version 229.

## See Also

sd-event(3), sd_event_add_io(3), sd_event_add_time(3), sd_event_add_signal(3), sd_event_add_child(3), sd_event_add_inotify(3), sd_event_add_defer(3), sd_event_source_unref(3), sd_event_source_set_ratelimit(3)
