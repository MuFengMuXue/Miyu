## Name

sd_bus_process — Drive the connection

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                               |                              |
|-------------------------------|------------------------------|
| `int `**`sd_bus_process`**`(` | sd_bus \*`bus`,              |
|                               | sd_bus_message \*\*`ret``)`; |

 

## Description

`sd_bus_process()` drives the connection between the client and the message bus. That is, it handles connecting, authentication, and processing of messages. When invoked, pending I/O work is executed, and queued incoming messages are dispatched to registered callbacks. Each time it is invoked a single operation is executed. It returns zero when no operations were pending and positive if a message was processed. When zero is returned the caller should poll for I/O events before calling into `sd_bus_process()` again. For that either use the simple, blocking sd_bus_wait(3) call, or hook up the bus connection object to an external or manual event loop using sd_bus_get_fd(3).

`sd_bus_process()` processes at most one incoming message per call. If the parameter *`ret`* is not `NULL` and the call processed a message, *`*ret`* is set to this message. The caller owns a reference to this message and should call sd_bus_message_unref(3) when the message is no longer needed. If *`ret`* is not `NULL` and progress was made, but no message was processed, *`*ret`* is set to `NULL`. Note that only messages not already handled by the various types of registered message handlers (i.e. by filters registered via sd_bus_add_filter(3), object handlers registered via sd_bus_add_object(3), matches registered via sd_bus_add_match(3), and related) will be returned through this parameter. Also note that if such a message handler returns a zero return value (as opposed to some value \> 0) an incoming message will not be considered handled, and be passed to other suitable handlers (until one returns \> \> 0), or returned by `sd_bus_process()` (in case none returns \> 0).

If the bus object is connected to an sd-event(3) event loop (with sd_bus_attach_event(3)), it is not necessary to call `sd_bus_process()` directly as it is invoked automatically when necessary.

## Return Value

If progress was made, a positive integer is returned. If no progress was made, 0 is returned. If an error occurs, a negative `errno`-style error code is returned.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
An invalid bus object was passed.

`-ECHILD`  
The bus connection was allocated in a parent process and is being reused in a child process after `fork()`.

`-ENOTCONN`  
The bus connection has been terminated already.

`-ECONNRESET`  
The bus connection has been terminated just now.

`-EBUSY`  
This function is already being called, i.e. `sd_bus_process()` has been called from a callback function that itself was called by `sd_bus_process()`.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_process()` was added in version 221.

## See Also

systemd(1), sd-bus(3), sd_bus_wait(3), sd_bus_get_fd(3), sd_bus_message_unref(3), sd-event(3), sd_bus_attach_event(3)
