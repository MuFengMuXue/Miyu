## Name

sd_event_source_set_prepare — Set a preparation callback for event sources

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-event.h>
```

|  |  |
|----|----|
| `int `**`sd_event_source_set_prepare`**`(` | sd_event_source \*`source`, |
|   | sd_event_handler_t `callback``)`; |

 

|                                              |                        |
|----------------------------------------------|------------------------|
| `typedef int (*`**`sd_event_handler_t`**`)(` | sd_event_source \*`s`, |
|                                              | void \*`userdata``)`;  |

 

## Description

`sd_event_source_set_prepare()` may be used to set a preparation callback for the event source object specified as *`source`*. The callback function specified as *`callback`* will be invoked immediately before the event loop goes to sleep to wait for incoming events. It is invoked with the user data pointer passed when the event source was created. The event source will be disabled if the callback function returns a negative error code. The callback function may be used to reconfigure the precise events to wait for. If the *`callback`* parameter is passed as `NULL` the callback function is reset.

Event source objects have no preparation callback associated when they are first created with calls such as sd_event_add_io(3), sd_event_add_time(3). Preparation callback functions are supported for all event source types with the exception of those created with sd_event_add_exit(3). Preparation callback functions are dispatched in the order indicated by the event source's priority field, as set with sd_event_source_set_priority(3). Preparation callbacks of disabled event sources (see sd_event_source_set_enabled(3)) are not invoked.

## Return Value

On success, `sd_event_source_set_prepare()` returns a non-negative integer. On failure, it returns a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
*`source`* is not a valid pointer to an sd_event_source object.

`-ESTALE`  
The event loop is already terminated.

`-ENOMEM`  
Not enough memory.

`-ECHILD`  
The event loop has been created in a different process, library or module instance.

`-EDOM`  
The specified event source has been created with sd_event_add_exit(3).

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_event_source_set_prepare()` and `sd_event_handler_t()` were added in version 229.

## See Also

sd-event(3), sd_event_add_io(3), sd_event_add_time(3), sd_event_add_signal(3), sd_event_add_child(3), sd_event_add_inotify(3), sd_event_add_defer(3), sd_event_source_set_enabled(3), sd_event_source_set_priority(3), sd_event_source_set_userdata(3)
