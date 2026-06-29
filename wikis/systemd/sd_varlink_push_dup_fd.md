## Name

sd_varlink_push_fd, sd_varlink_push_dup_fd — Submit a file descriptor to send along with the next outgoing Varlink message

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-varlink.h>
```

|                                   |                      |
|-----------------------------------|----------------------|
| `int `**`sd_varlink_push_fd`**`(` | sd_varlink \*`link`, |
|                                   | int `fd``)`;         |

 

|                                       |                      |
|---------------------------------------|----------------------|
| `int `**`sd_varlink_push_dup_fd`**`(` | sd_varlink \*`link`, |
|                                       | int `fd``)`;         |

 

## Description

`sd_varlink_push_fd()` submits a file descriptor to send along with the next outgoing Varlink message. Takes a Varlink connection object and a file descriptor as parameter. The file descriptor is not duplicated, and hence ownership of the file descriptor is passed to the Varlink connection object (only on success; on failure the caller retains ownership). Once the file descriptor has been written to the underlying transport socket it is automatically closed. The calling application code should not touch the file descriptor or close it on its own, otherwise it will interfere with the Varlink protocol implementation. This call is only supported if the backing transport supports file descriptor passing (effectively this means the functionality is supported on local `AF_UNIX` only), and the concept is not part of the Varlink protocol, but simply a feature of the underlying transport.

`sd_varlink_push_dup_fd()` is identical to `sd_varlink_push_fd()`, except that the file descriptor is duplicated automatically, and the calling application code hence retains ownership of the provided file descriptor, and must close it on its own.

Note that file descriptor passing is only permitted after a call to `sd_varlink_set_allow_fd_passing_output()` that enables it, otherwise these calls will fail with `-EPERM`.

Note that on Linux a maximum of 253 file descriptors may be enqueued on `AF_UNIX` sockets at once. Attempting to enqueue more on a single Varlink message will fail with `-ENOBUFS`.

## Return Value

On success, `sd_varlink_push_fd()` and `sd_varlink_push_dup_fd()` return a non-negative integer. On failure, they return a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
An argument is invalid.

`-EBADF`  
The provided file descriptor is not valid.

`-EPERM`  
File descriptor passing has not been enabled via `sd_varlink_set_allow_fd_passing_output()`.

`-ENOBUFS`  
The maximum of 253 file descriptors have already been submitted for the next outgoing Varlink message, no further descriptors may be enqueued for this message.

`-ENOMEM`  
Memory allocation failed.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_varlink_push_fd()` and `sd_varlink_push_dup_fd()` were added in version 257.

## See Also

systemd(1), sd-varlink(3)
