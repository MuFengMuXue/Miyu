## Name

sd_event_source_set_userdata, sd_event_source_get_userdata — Set or retrieve user data pointer of event sources

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-event.h>
```

|                                               |                             |
|-----------------------------------------------|-----------------------------|
| `void* `**`sd_event_source_set_userdata`**`(` | sd_event_source \*`source`, |
|                                               | void \*`userdata``)`;       |

 

|  |  |
|----|----|
| `void* `**`sd_event_source_get_userdata`**`(` | sd_event_source \*`source``)`; |

 

## Description

`sd_event_source_set_userdata()` may be used to set an arbitrary user data pointer for the event source object specified as *`source`*. The user data pointer is usually specified when creating an event source object with calls such as sd_event_add_io(3) or sd_event_add_time(3), and may be updated with this call. The user data pointer is also passed to all handler callback functions associated with the event source. The *`userdata`* parameter specifies the new user data pointer to set, the function returns the previous user data pointer. Note that `NULL` is a valid user data pointer.

`sd_event_source_get_userdata()` may be used to query the current user data pointer assigned to the event source object *`source`*.

## Return Value

On success, `sd_event_source_set_userdata()` and `sd_event_source_get_userdata()` return the previously set user data pointer. On failure, they return `NULL`.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_event_source_set_userdata()` and `sd_event_source_get_userdata()` were added in version 229.

## See Also

sd-event(3), sd_event_add_io(3), sd_event_add_time(3), sd_event_add_signal(3), sd_event_add_child(3), sd_event_add_inotify(3), sd_event_add_defer(3), sd_event_source_set_description(3)
