## Name

sd_event_run, sd_event_loop — Run an event loop

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-event.h>
```

|                             |                     |
|-----------------------------|---------------------|
| `int `**`sd_event_run`**`(` | sd_event \*`event`, |
|                             | uint64_t `usec``)`; |

 

|                              |                        |
|------------------------------|------------------------|
| `int `**`sd_event_loop`**`(` | sd_event \*`event``)`; |

 

## Description

`sd_event_run()` may be used to run a single iteration of the event loop specified in the *`event`* parameter. The function waits until an event to process is available, and dispatches the registered handler for it. The *`usec`* parameter specifies the maximum time (in microseconds) to wait for an event. Use `(uint64_t) -1` to specify an infinite timeout.

`sd_event_loop()` invokes `sd_event_run()` in a loop, thus implementing the actual event loop. The call returns as soon as exiting was requested using sd_event_exit(3).

The event loop object *`event`* is created with sd_event_new(3). Events sources to wait for and their handlers may be registered with sd_event_add_io(3), sd_event_add_time(3), sd_event_add_signal(3), sd_event_add_child(3), sd_event_add_defer(3), sd_event_add_post(3) and sd_event_add_exit(3).

For low-level control of event loop execution, use sd_event_prepare(3), sd_event_wait(3) and sd_event_dispatch(3) which are wrapped by `sd_event_run()`. Along with sd_event_get_fd(3), these functions allow integration of an sd-event(3) event loop into foreign event loop implementations.

## Return Value

On failure, these functions return a negative errno-style error code. `sd_event_run()` returns a positive, non-zero integer if an event source was dispatched, and zero when the specified timeout hit before an event source has seen any event, and hence no event source was dispatched. `sd_event_loop()` returns the exit code specified when invoking `sd_event_exit()`.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
The *`event`* parameter is invalid or `NULL`.

`-EBUSY`  
The event loop object is not in the right state (see sd_event_prepare(3) for an explanation of possible states).

`-ESTALE`  
The event loop is already terminated.

`-ECHILD`  
The event loop has been created in a different process, library or module instance.

Other errors are possible, too.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_event_run()` and `sd_event_loop()` were added in version 220.

## See Also

systemd(1), sd-event(3), sd_event_new(3), sd_event_add_io(3), sd_event_add_time(3), sd_event_add_signal(3), sd_event_add_child(3), sd_event_add_inotify(3), sd_event_add_defer(3), sd_event_exit(3), sd_event_get_fd(3), sd_event_wait(3), GLib Main Event Loop
