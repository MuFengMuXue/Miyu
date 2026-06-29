## Name

sd_session_is_active, sd_session_is_remote, sd_session_get_state, sd_session_get_uid, sd_session_get_username, sd_session_get_seat, sd_session_get_start_time, sd_session_get_service, sd_session_get_type, sd_session_get_class, sd_session_get_desktop, sd_session_get_display, sd_session_get_tty, sd_session_get_vt, sd_session_get_remote_host, sd_session_get_remote_user, sd_session_get_leader, sd_session_get_extra_device_access — Determine state of a specific session

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-login.h>
```

|                                     |                            |
|-------------------------------------|----------------------------|
| `int `**`sd_session_is_active`**`(` | const char \*`session``)`; |

 

|                                     |                            |
|-------------------------------------|----------------------------|
| `int `**`sd_session_is_remote`**`(` | const char \*`session``)`; |

 

|                                     |                         |
|-------------------------------------|-------------------------|
| `int `**`sd_session_get_state`**`(` | const char \*`session`, |
|                                     | char \*\*`state``)`;    |

 

|                                   |                         |
|-----------------------------------|-------------------------|
| `int `**`sd_session_get_uid`**`(` | const char \*`session`, |
|                                   | uid_t \*`uid``)`;       |

 

|                                        |                         |
|----------------------------------------|-------------------------|
| `int `**`sd_session_get_username`**`(` | const char \*`session`, |
|                                        | char \*\*`username``)`; |

 

|                                    |                         |
|------------------------------------|-------------------------|
| `int `**`sd_session_get_seat`**`(` | const char \*`session`, |
|                                    | char \*\*`seat``)`;     |

 

|                                          |                         |
|------------------------------------------|-------------------------|
| `int `**`sd_session_get_start_time`**`(` | const char \*`session`, |
|                                          | uint64_t \*`usec``)`;   |

 

|                                       |                         |
|---------------------------------------|-------------------------|
| `int `**`sd_session_get_service`**`(` | const char \*`session`, |
|                                       | char \*\*`service``)`;  |

 

|                                    |                         |
|------------------------------------|-------------------------|
| `int `**`sd_session_get_type`**`(` | const char \*`session`, |
|                                    | char \*\*`type``)`;     |

 

|                                     |                         |
|-------------------------------------|-------------------------|
| `int `**`sd_session_get_class`**`(` | const char \*`session`, |
|                                     | char \*\*`class``)`;    |

 

|                                       |                         |
|---------------------------------------|-------------------------|
| `int `**`sd_session_get_desktop`**`(` | const char \*`session`, |
|                                       | char \*\*`desktop``)`;  |

 

|                                       |                         |
|---------------------------------------|-------------------------|
| `int `**`sd_session_get_display`**`(` | const char \*`session`, |
|                                       | char \*\*`display``)`;  |

 

|                                      |                         |
|--------------------------------------|-------------------------|
| `int `**`sd_session_get_leader`**`(` | const char \*`session`, |
|                                      | pid_t \*`leader``)`;    |

 

|                                           |                            |
|-------------------------------------------|----------------------------|
| `int `**`sd_session_get_remote_host`**`(` | const char \*`session`,    |
|                                           | char \*\*`remote_host``)`; |

 

|                                           |                            |
|-------------------------------------------|----------------------------|
| `int `**`sd_session_get_remote_user`**`(` | const char \*`session`,    |
|                                           | char \*\*`remote_user``)`; |

 

|                                   |                         |
|-----------------------------------|-------------------------|
| `int `**`sd_session_get_tty`**`(` | const char \*`session`, |
|                                   | char \*\*`tty``)`;      |

 

|                                  |                         |
|----------------------------------|-------------------------|
| `int `**`sd_session_get_vt`**`(` | const char \*`session`, |
|                                  | unsigned int \*`vt``)`; |

 

|  |  |
|----|----|
| `int `**`sd_session_get_extra_device_access`**`(` | const char \*`session`, |
|   | char \*\*\*`ret_ids``)`; |

 

## Description

`sd_session_is_active()` may be used to determine whether the session identified by the specified session identifier is currently active (i.e. currently in the foreground and available for user input) or not.

`sd_session_is_remote()` may be used to determine whether the session identified by the specified session identifier is a remote session (i.e. its remote host is known) or not.

`sd_session_get_state()` may be used to determine the state of the session identified by the specified session identifier. The following states are currently known: "`online`" (session logged in, but session not active, i.e. not in the foreground), "`active`" (session logged in and active, i.e. in the foreground), "`closing`" (session nominally logged out, but some processes belonging to it are still around). In the future additional states might be defined, client code should be written to be robust in regards to additional state strings being returned. This function is a more generic version of `sd_session_is_active()`. The returned string needs to be freed with the libc free(3) call after use.

`sd_session_get_uid()` may be used to determine the user identifier of the Unix user the session identified by the specified session identifier belongs to.

`sd_session_get_username()` may be used to determine the name of the Unix user the session identified by the specified session identifier belongs to. The returned string needs to be freed with the libc free(3) call after use.

`sd_session_get_seat()` may be used to determine the seat identifier of the seat the session identified by the specified session identifier belongs to. Note that not all sessions are attached to a seat, this call will fail (returning `-ENODATA`) for them. The returned string needs to be freed with the libc free(3) call after use.

`sd_session_get_start_time()` may be used to determine the start time of the session identified by the specified session identifier belongs to. The *`usec`* is in microseconds since the epoch (`CLOCK_REALTIME`).

`sd_session_get_service()` may be used to determine the name of the service (as passed during PAM session setup) that registered the session identified by the specified session identifier. The returned string needs to be freed with the libc free(3) call after use.

`sd_session_get_type()` may be used to determine the type of the session identified by the specified session identifier. The returned string is one of "`x11`", "`wayland`", "`tty`", "`mir`" or "`unspecified`" and needs to be freed with the libc free(3) call after use.

`sd_session_get_class()` may be used to determine the class of the session identified by the specified session identifier. The returned string is one of "`user`", "`user-early`", "`user-light`", "`user-early-light`", "`user-incomplete`", "`greeter`", "`lock-screen`", "`background`", "`background-light`", "`manager`" or "`manager-early`" and needs to be freed with the libc free(3) call after use.

`sd_session_get_desktop()` may be used to determine the brand of the desktop running on the session identified by the specified session identifier. This field can be set freely by desktop environments and does not follow any special formatting. However, desktops are strongly recommended to use the same identifiers and capitalization as for `$XDG_CURRENT_DESKTOP`, as defined by the Desktop Entry Specification. The returned string needs to be freed with the libc free(3) call after use.

`sd_session_get_display()` may be used to determine the X11 display of the session identified by the specified session identifier. The returned string needs to be freed with the libc free(3) call after use.

`sd_session_get_leader()` may be used to determine the PID of the leader of the session identified by the specified session identifier.

`sd_session_get_remote_host()` may be used to determine the remote hostname of the session identified by the specified session identifier. The returned string needs to be freed with the libc free(3) call after use.

`sd_session_get_remote_user()` may be used to determine the remote username of the session identified by the specified session identifier. The returned string needs to be freed with the libc free(3) call after use. Note that this value is rarely known to the system, and even then should not be relied on.

`sd_session_get_tty()` may be used to determine the TTY device of the session identified by the specified session identifier. The returned string needs to be freed with the libc free(3) call after use.

`sd_session_get_vt()` may be used to determine the VT number of the session identified by the specified session identifier. This function will return an error if the seat does not support VTs.

`sd_session_get_extra_device_access()` may be used to determine which additional hardware devices the session is granted access to. For every "*`ID`*" in the list, the session is granted access to all devices tagged with "`xaccess-`*`ID`*" in udev.

If the `session` parameter of any of these functions is passed as `NULL`, the operation is executed for the session the calling process is a member of, if there is any.

## Return Value

If the test succeeds, `sd_session_is_active()` and `sd_session_is_remote()` return a positive integer; if it fails, 0. On success, `sd_session_get_state()`, `sd_session_get_uid()`, `sd_session_get_username()`, `sd_session_get_seat()`, `sd_session_get_service()`, `sd_session_get_type()`, `sd_session_get_class()`, `sd_session_get_display()`, `sd_session_get_leader()`, `sd_session_get_remote_user()`, `sd_session_get_remote_host()`, `sd_session_get_tty()`, and `sd_session_get_extra_device_access()` return 0 or a positive integer. On failure, these calls return a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-ENXIO`  
The specified session does not exist.

`-ENODATA`  
The given field is not specified for the described session.

`-EINVAL`  
An input parameter was invalid (out of range, or `NULL`, where that is not accepted).

`-ENOMEM`  
Memory allocation failed.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_session_get_state()` was added in version 186.

`sd_session_get_tty()` was added in version 198.

`sd_session_get_vt()` was added in version 207.

`sd_session_is_remote()`, `sd_session_get_remote_host()`, and `sd_session_get_remote_user()` were added in version 209.

`sd_session_get_desktop()` was added in version 217.

`sd_session_get_username()`, `sd_session_get_start_time()`, and `sd_session_get_leader()` were added in version 254.

`sd_session_get_extra_device_access()` was added in version 260.

## See Also

systemd(1), sd-login(3), sd_pid_get_session(3)
