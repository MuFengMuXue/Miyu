## Name

sd_bus_set_fd — Set the file descriptors to use for bus communication

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                              |                     |
|------------------------------|---------------------|
| `int `**`sd_bus_set_fd`**`(` | sd_bus \*`bus`,     |
|                              | int `input_fd`,     |
|                              | int `output_fd``)`; |

 

## Description

`sd_bus_set_fd()` sets the file descriptors used to communicate by a bus connection object. Both *`input_fd`* and *`output_fd`* must be valid file descriptors, referring to stream-based file objects (e.g. a stream socket, a pair of pipes or FIFOs, or even a TTY device). *`input_fd`* must be readable, and *`output_fd`* must be writable. The same file descriptor may be used (and typically is used) as both the input and the output file descriptor. This function must be called before the bus connection is started via sd_bus_start(3).

The bus connection object will take possession of the passed file descriptors and will close them automatically when it is freed. Use sd_bus_set_close_on_exit(3) to turn off this behaviour.

## Return Value

On success, `sd_bus_set_fd()` returns a non-negative integer. On failure, it returns a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
An invalid bus object was passed.

Added in version 248.

`-ECHILD`  
The bus connection was allocated in a parent process and is being reused in a child process after `fork()`.

Added in version 248.

`-EBADF`  
An invalid file descriptor was passed to `sd_bus_set_fd()`.

Added in version 248.

`-ENOPKG`  
The bus cannot be resolved.

Added in version 248.

`-EPERM`  
The bus connection has already been started.

Added in version 248.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_set_fd()` was added in version 248.

## See Also

systemd(1), sd-bus(3), sd_bus_get_fd(3), sd_bus_start(3)
