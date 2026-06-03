## Name

sd_get_seats, sd_get_sessions, sd_get_uids, sd_get_machine_names — Determine available seats, sessions, logged in users and virtual machines/containers

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-login.h>
```

|                             |                        |
|-----------------------------|------------------------|
| `int `**`sd_get_seats`**`(` | char \*\*\*`seats``)`; |

 

|                                |                           |
|--------------------------------|---------------------------|
| `int `**`sd_get_sessions`**`(` | char \*\*\*`sessions``)`; |

 

|                            |                       |
|----------------------------|-----------------------|
| `int `**`sd_get_uids`**`(` | uid_t \*\*`users``)`; |

 

|                                     |                           |
|-------------------------------------|---------------------------|
| `int `**`sd_get_machine_names`**`(` | char \*\*\*`machines``)`; |

 

## Description

`sd_get_seats()` may be used to determine all currently available local seats. Returns the number of seat identifiers and if the input pointer is non-`NULL`, a `NULL`-terminated array of seat identifiers is stored at the address. The returned array and all strings it references need to be freed with the libc free(3) call after use. Note that instead of an empty array `NULL` may be returned and should be considered equivalent to an empty array.

Similarly, `sd_get_sessions()` may be used to determine all current login sessions.

Similarly, `sd_get_uids()` may be used to determine all Unix users who currently have login sessions.

Similarly, `sd_get_machine_names()` may be used to determine all current virtual machines and containers on the system.

Note that the returned lists are not sorted and in an undefined order.

## Return Value

On success, `sd_get_seats()`, `sd_get_sessions()`, `sd_get_uids()` and `sd_get_machine_names()` return the number of entries in the arrays. On failure, these calls return a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-ENOMEM`  
Memory allocation failed.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_get_machine_names()` was added in version 203.

## See Also

systemd(1), sd-login(3), sd_session_get_seat(3)
