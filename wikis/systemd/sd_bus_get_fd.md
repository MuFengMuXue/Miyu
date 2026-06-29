## Name

sd_bus_get_fd, sd_bus_get_events, sd_bus_get_timeout — Get the file descriptor, I/O events and timeout to wait for from a message bus object

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                              |                    |
|------------------------------|--------------------|
| `int `**`sd_bus_get_fd`**`(` | sd_bus \*`bus``)`; |

 

|                                  |                    |
|----------------------------------|--------------------|
| `int `**`sd_bus_get_events`**`(` | sd_bus \*`bus``)`; |

 

|                                   |                               |
|-----------------------------------|-------------------------------|
| `int `**`sd_bus_get_timeout`**`(` | sd_bus \*`bus`,               |
|                                   | uint64_t \*`timeout_usec``)`; |

 

## Description

`sd_bus_get_fd()` returns the file descriptor used to communicate from a message bus object. This descriptor can be used with poll(3) or a similar function to wait for I/O events on the specified bus connection object. If the bus object was configured with the `sd_bus_set_fd()` function, then the *`input_fd`* file descriptor used in that call is returned.

`sd_bus_get_events()` returns the I/O events to wait for, suitable for passing to `poll()` or a similar call. Returns a combination of `POLLIN`, `POLLOUT`, … events, or negative on error.

`sd_bus_get_timeout()` returns the *absolute* timeout in μs, from which the relative timeout to pass to `poll()` (or a similar call) can be derived, when waiting for events on the specified bus connection. The returned timeout may be zero, in which case a subsequent I/O polling call should be invoked in non-blocking mode. The returned timeout may be `UINT64_MAX` in which case the I/O polling call may block indefinitely, without any applied timeout. Note that the returned timeout should be considered only a maximum sleeping time. It is permissible (and even expected) that shorter timeouts are used by the calling program, in case other event sources are polled in the same event loop. Note that the returned time-value is absolute, based of `CLOCK_MONOTONIC` and specified in microseconds. When converting this value in order to pass it as third argument to `poll()` (which expects relative milliseconds), care should be taken to convert to a relative time and use a division that rounds up to ensure the I/O polling operation does not sleep for shorter than necessary, which might result in unintended busy looping (alternatively, use ppoll(2) instead of plain `poll()`, which understands timeouts with nano-second granularity).

These three functions are useful to hook up a bus connection object with an external or manual event loop involving `poll()` or a similar I/O polling call. Before each invocation of the I/O polling call, all three functions should be invoked: the file descriptor returned by `sd_bus_get_fd()` should be polled for the events indicated by `sd_bus_get_events()`, and the I/O call should block for that up to the timeout returned by `sd_bus_get_timeout()`. After each I/O polling call the bus connection needs to process incoming or outgoing data, by invoking sd_bus_process(3).

Note that these functions are only one of three supported ways to implement I/O event handling for bus connections. Alternatively use sd_bus_attach_event(3) to attach a bus connection to an sd-event(3) event loop. Or use sd_bus_wait(3) as a simple synchronous, blocking I/O waiting call.

## Return Value

On success, `sd_bus_get_fd()` returns the file descriptor used for communication. On failure, it returns a negative errno-style error code.

On success, `sd_bus_get_events()` returns the I/O event mask to use for I/O event watching. On failure, it returns a negative errno-style error code.

On success, `sd_bus_get_timeout()` returns a non-negative integer. On failure, it returns a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
An invalid bus object was passed.

`-ECHILD`  
The bus connection was allocated in a parent process and is being reused in a child process after `fork()`.

`-ENOTCONN`  
The bus connection has been terminated.

`-EPERM`  
Two distinct file descriptors were passed for input and output using `sd_bus_set_fd()`, which `sd_bus_get_fd()` cannot return.

`-ENOPKG`  
The bus cannot be resolved.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_get_fd()`, `sd_bus_get_events()`, and `sd_bus_get_timeout()` were added in version 221.

## See Also

systemd(1), sd-bus(3), sd_bus_process(3), sd_bus_attach_event(3), sd_bus_wait(3), sd_bus_set_fd(3), poll(3)
