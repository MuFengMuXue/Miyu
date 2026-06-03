## Name

sd_event_set_signal_exit — Automatically leave event loop on `SIGINT` and `SIGTERM`

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-event.h>
```

|                                         |                     |
|-----------------------------------------|---------------------|
| `int `**`sd_event_set_signal_exit`**`(` | sd_event \*`event`, |
|                                         | int b`)`;           |

 

## Description

`sd_event_set_signal_exit()` may be used to ensure the event loop terminates once a `SIGINT` or `SIGTERM` signal is received. It is a convenience wrapper around invocations of sd_event_add_signal(3) for both signals. The two signals are automatically added to the calling thread's signal mask (if a program is multi-threaded care should be taken to either invoke this function before the first thread is started or to manually block the two signals process-wide first).

If the parameter *`b`* is specified as true, the event loop will terminate on `SIGINT` and `SIGTERM`. If specified as false, it will no longer. When this functionality is turned off the calling thread's signal mask is restored to match the state before it was turned on, for the two signals. By default, the two signals are not handled by the event loop, and Linux' default signal handling for them is in effect.

It is customary for UNIX programs to exit on either of these two signals, hence it is typically a good idea to enable this functionality for the main event loop of a program.

## Return Value

`sd_event_set_signal_exit()` returns a positive non-zero value when the setting was successfully changed. It returns a zero when the specified setting was already in effect. On failure, it returns a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-ECHILD`  
The event loop has been created in a different process, library or module instance.

Added in version 252.

`-EINVAL`  
The passed event loop object was invalid.

Added in version 252.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_event_set_signal_exit()` was added in version 252.

## See Also

systemd(1), sd-event(3), sd_event_new(3), sd_event_add_signal(3)
