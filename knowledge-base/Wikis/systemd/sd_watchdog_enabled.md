## Name

sd_watchdog_enabled — Check whether the service manager expects watchdog keep-alive notifications from a service

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-daemon.h>
```

|                                    |                          |
|------------------------------------|--------------------------|
| `int `**`sd_watchdog_enabled`**`(` | int `unset_environment`, |
|                                    | uint64_t \*`usec``)`;    |

 

## Description

`sd_watchdog_enabled()` may be called by a service to detect whether the service manager expects regular keep-alive watchdog notification events from it, and the timeout after which the manager will act on the service if it did not get such a notification.

If the `$WATCHDOG_USEC` environment variable is set, and the `$WATCHDOG_PID` variable is unset or set to the PID of the current process, the service manager expects notifications from this process. The manager will usually terminate a service when it does not get a notification message within the specified time after startup and after each previous message. It is recommended that a daemon sends a keep-alive notification message to the service manager every half of the time returned here. Notification messages may be sent with sd_notify(3) with a message string of "`WATCHDOG=1`".

If the *`unset_environment`* parameter is non-zero, `sd_watchdog_enabled()` will unset the `$WATCHDOG_USEC` and `$WATCHDOG_PID` environment variables before returning (regardless of whether the function call itself succeeded or not). Those variables are no longer inherited by child processes. Further calls to `sd_watchdog_enabled()` will also return with zero.

If the *`usec`* parameter is non-`NULL`, `sd_watchdog_enabled()` will write the timeout in μs for the watchdog logic to it.

To enable service supervision with the watchdog logic, use `WatchdogSec=` in service files. See systemd.service(5) for details.

Use sd_event_set_watchdog(3) to enable automatic watchdog support in sd-event(3)-based event loops.

## Return Value

On failure, this call returns a negative errno-style error code. If the service manager expects watchdog keep-alive notification messages to be sent, \> 0 is returned, otherwise 0 is returned. Only if the return value is \> 0, the *`usec`* parameter is valid after the call.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

Internally, this function parses the `$WATCHDOG_PID` and `$WATCHDOG_USEC` environment variable. The call will ignore these variables if `$WATCHDOG_PID` does not contain the PID of the current process, under the assumption that in that case, the variables were set for a different process further up the process tree.

## Environment

`$WATCHDOG_PID`  
Set by the system manager for supervised process for which watchdog support is enabled, and contains the PID of that process. See above for details.

Added in version 209.

`$WATCHDOG_USEC`  
Set by the system manager for supervised process for which watchdog support is enabled, and contains the watchdog timeout in μs. See above for details.

Added in version 209.

## History

`sd_watchdog_enabled()` was added in version 209.

## See Also

systemd(1), sd-daemon(3), daemon(7), systemd.service(5), sd_notify(3), sd_event_set_watchdog(3)
