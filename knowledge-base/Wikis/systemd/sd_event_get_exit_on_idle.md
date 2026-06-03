## Name

sd_event_set_exit_on_idle, sd_event_get_exit_on_idle — Enable event loop exit-on-idle support

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-event.h>
```

|                                          |                     |
|------------------------------------------|---------------------|
| `int `**`sd_event_set_exit_on_idle`**`(` | sd_event \*`event`, |
|                                          | int b`)`;           |

 

|                                          |                        |
|------------------------------------------|------------------------|
| `int `**`sd_event_get_exit_on_idle`**`(` | sd_event \*`event``)`; |

 

## Description

`sd_event_set_exit_on_idle()` may be used to enable or disable the exit-on-idle support in the event loop object specified in the *`event`* parameter. If enabled, the event loop will exit with a zero exit code there are no more enabled (`SD_EVENT_ON`, `SD_EVENT_ONESHOT`), non-exit, non-post event sources.

`sd_event_get_exit_on_idle()` may be used to determine whether exit-on-idle support was previously requested by a call to `sd_event_set_exit_on_idle()` with a true *`b`* parameter and successfully enabled.

## Return Value

On success, `sd_event_set_exit_on_idle()` and `sd_event_get_exit_on_idle()` return a non-zero positive integer if the exit-on-idle support was successfully enabled. They return zero if the exit-on-idle support was explicitly disabled with a false *`b`* parameter. On failure, they return a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-ECHILD`  
The event loop has been created in a different process, library or module instance.

`-EINVAL`  
The passed event loop object was invalid.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_event_set_exit_on_idle()` and `sd_event_get_exit_on_idle()` were added in version 259.

## See Also

systemd(1), sd-event(3), sd_event_new(3), sd_event_add_io(3), sd_event_add_time(3), sd_event_add_signal(3), sd_event_add_child(3), sd_event_add_inotify(3), sd_event_add_defer(3), systemd.service(5)
