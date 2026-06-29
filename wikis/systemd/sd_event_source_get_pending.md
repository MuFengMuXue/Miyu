## Name

sd_event_source_get_pending — Determine pending state of event sources

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-event.h>
```

|                                            |                                |
|--------------------------------------------|--------------------------------|
| `int `**`sd_event_source_get_pending`**`(` | sd_event_source \*`source``)`; |

 

## Description

`sd_event_source_get_pending()` may be used to determine whether the event source object specified as *`source`* has seen events but has not been dispatched yet (and thus is marked "pending").

Event source objects initially are not marked pending, when they are created with calls such as sd_event_add_io(3), sd_event_add_time(3), with the exception of those created with sd_event_add_defer(3) which are immediately marked pending, and sd_event_add_exit(3) for which the "pending" concept is not defined. For details see the respective manual pages.

In each event loop iteration one event source of those marked pending is dispatched, in the order defined by the event source priority, as set with sd_event_source_set_priority(3).

For I/O event sources, as created with sd_event_add_io(3), the call sd_event_source_get_io_revents(3) may be used to query the type of event pending in more detail.

## Return Value

On success, `sd_event_source_get_pending()` returns an integer greater than zero when the event source is marked pending, and zero when the event source is not marked pending. On failure, it returns a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
*`source`* is not a valid pointer to an sd_event_source object.

`-EDOM`  
*`source`* refers to an event source object created with sd_event_add_exit(3).

`-ENOMEM`  
Not enough memory.

`-ESTALE`  
The event loop is already terminated.

`-ECHILD`  
The event loop has been created in a different process, library or module instance.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_event_source_get_pending()` was added in version 229.

## See Also

sd-event(3), sd_event_add_io(3), sd_event_add_time(3), sd_event_add_signal(3), sd_event_add_child(3), sd_event_add_inotify(3), sd_event_add_defer(3), sd_event_source_unref(3)
