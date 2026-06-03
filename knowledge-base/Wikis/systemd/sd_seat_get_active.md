## Name

sd_seat_get_active, sd_seat_get_sessions, sd_seat_can_tty, sd_seat_can_graphical — Determine state of a specific seat

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-login.h>
```

|                                   |                      |
|-----------------------------------|----------------------|
| `int `**`sd_seat_get_active`**`(` | const char \*`seat`, |
|                                   | char \*\*`session`,  |
|                                   | uid_t \*`uid``)`;    |

 

|                                     |                                 |
|-------------------------------------|---------------------------------|
| `int `**`sd_seat_get_sessions`**`(` | const char \*`seat`,            |
|                                     | char \*\*\*`ret_sessions`,      |
|                                     | uid_t \*\*`ret_uids`,           |
|                                     | unsigned int \*`ret_n_uids``)`; |

 

|                                |                         |
|--------------------------------|-------------------------|
| `int `**`sd_seat_can_tty`**`(` | const char \*`seat``)`; |

 

|                                      |                         |
|--------------------------------------|-------------------------|
| `int `**`sd_seat_can_graphical`**`(` | const char \*`seat``)`; |

 

## Description

`sd_seat_get_active()` may be used to determine which session is currently active on a seat, if there is any. Returns the session identifier and the user identifier of the Unix user the session is belonging to. Either the session or the user identifier parameter can be passed `NULL`, in case only one of the parameters shall be queried. The returned string needs to be freed with the libc free(3) call after use.

`sd_seat_get_sessions()` may be used to determine all sessions on the specified seat. Returns two arrays, one (`NULL` terminated) with the session identifiers of the sessions and one with the user identifiers of the Unix users the sessions belong to. An additional parameter may be used to return the number of entries in the latter array. This value is the same as the return value if the return value is nonnegative. The output parameters may be passed as `NULL` in case these output values are not needed. The arrays and the strings referenced by them need to be freed with the libc free(3) call after use. Note that instead of an empty array `NULL` may be returned and should be considered equivalent to an empty array.

`sd_seat_can_tty()` may be used to determine whether a specific seat provides TTY functionality, i.e. is useful as a text console.

`sd_seat_can_graphical()` may be used to determine whether a specific seat provides graphics functionality, i.e. is useful as a graphics display.

If the `seat` parameter of any of these functions is passed as `NULL`, the operation is executed for the seat of the session of the calling process, if there is any.

## Return Value

On success, `sd_seat_get_active()` returns 0 or a positive integer. On success, `sd_seat_get_sessions()` returns the number of entries in the session identifier array. If the test succeeds, `sd_seat_can_tty()` and `sd_seat_can_graphical()` return a positive integer, if it fails 0. On failure, these calls return a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-ENODATA`  
The given field is not specified for the described seat.

`-ENXIO`  
The specified seat is unknown.

`-EINVAL`  
An input parameter was invalid (out of range, or `NULL`, where that is not accepted).

`-ENOMEM`  
Memory allocation failed.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_seat_can_tty()` and `sd_seat_can_graphical()` were added in version 186.

## See Also

systemd(1), sd-login(3), sd_session_get_seat(3)
