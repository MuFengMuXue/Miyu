## Name

sd_event_source_set_floating, sd_event_source_get_floating — Set or retrieve 'floating' state of event sources

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-event.h>
```

|                                             |                             |
|---------------------------------------------|-----------------------------|
| `int `**`sd_event_source_set_floating`**`(` | sd_event_source \*`source`, |
|                                             | int `floating``)`;          |

 

|  |  |
|----|----|
| `int `**`sd_event_source_get_floating`**`(` | sd_event_source \*`source``)`; |

 

## Description

`sd_event_source_set_floating()` takes a boolean and sets the 'floating' state of the specified event source object. This is used to change the direction of reference counts for the object and the event loop it is associated with. In non-floating mode, the event source object holds a reference to the event loop object, but not vice versa. The creator of the event source object must hold a reference to it as long as the source should exist. In floating mode, the event loop holds a reference to the source object, and will decrease the reference count when being freed. This means that a reference to the event loop should be held to prevent both from being destroyed.

Various calls that allocate event source objects (i.e. sd_event_add_io(3), sd_event_add_time(3) and similar) will automatically set an event source object to 'floating' mode if the caller passed `NULL` in the parameter used to return a reference to the event source object. Nevertheless, it may be necessary to gain temporary access to the source object, for example to adjust event source properties after allocation (e.g. its priority or description string). In those cases the object may be created in non-floating mode, and the returned reference used to adjust the properties, and the object marked as floating afterwards, and the reference in the caller dropped.

`sd_event_source_get_floating()` may be used to query the current 'floating' state of the event source object *`source`*. It returns zero if 'floating' mode is off, positive if it is on.

## Return Value

On success, `sd_event_source_set_floating()` and `sd_event_source_get_floating()` return a non-negative integer. On failure, they return a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
*`source`* is not a valid pointer to an sd_event_source object.

Added in version 244.

`-ECHILD`  
The event loop has been created in a different process, library or module instance.

Added in version 244.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_event_source_set_floating()` and `sd_event_source_get_floating()` were added in version 244.

## See Also

sd-event(3), sd_event_add_io(3), sd_event_add_time(3), sd_event_add_signal(3), sd_event_add_child(3), sd_event_add_inotify(3), sd_event_add_defer(3), sd_event_source_set_description(3), sd_event_source_set_priority(3)
