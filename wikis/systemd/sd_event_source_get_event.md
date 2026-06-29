## Name

sd_event_source_get_event — Retrieve the event loop of an event source

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-event.h>
```

|  |  |
|----|----|
| `sd_event* `**`sd_event_source_get_event`**`(` | sd_event_source \*`source``)`; |

 

## Description

`sd_event_source_get_event()` may be used to retrieve the event loop object the event source object specified as *`source`* is associated with. The event loop object is specified when creating an event source object with calls such as sd_event_add_io(3) or sd_event_add_time(3).

## Return Value

On success, `sd_event_source_get_event()` returns the associated event loop object. On failure, it returns `NULL`.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_event_source_get_event()` was added in version 229.

## See Also

sd-event(3), sd_event_add_io(3), sd_event_add_time(3), sd_event_add_signal(3), sd_event_add_child(3), sd_event_add_inotify(3), sd_event_add_defer(3), sd_event_source_set_userdata(3)
