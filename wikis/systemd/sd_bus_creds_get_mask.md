## Name

sd_bus_creds_new_from_pid, sd_bus_creds_new_from_pidfd, sd_bus_creds_get_mask, sd_bus_creds_get_augmented_mask, sd_bus_creds_ref, sd_bus_creds_unref, sd_bus_creds_unrefp — Retrieve credentials object for the specified PID

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                          |                            |
|------------------------------------------|----------------------------|
| `int `**`sd_bus_creds_new_from_pid`**`(` | pid_t `pid`,               |
|                                          | uint64_t `creds_mask`,     |
|                                          | sd_bus_creds \*\*`ret``)`; |

 

|                                            |                            |
|--------------------------------------------|----------------------------|
| `int `**`sd_bus_creds_new_from_pidfd`**`(` | int `pidfd`,               |
|                                            | uint64_t `creds_mask`,     |
|                                            | sd_bus_creds \*\*`ret``)`; |

 

|                                           |                        |
|-------------------------------------------|------------------------|
| `uint64_t `**`sd_bus_creds_get_mask`**`(` | sd_bus_creds \*`c``)`; |

 

|  |  |
|----|----|
| `uint64_t `**`sd_bus_creds_get_augmented_mask`**`(` | sd_bus_creds \*`c``)`; |

 

|                                           |                        |
|-------------------------------------------|------------------------|
| `sd_bus_creds *`**`sd_bus_creds_ref`**`(` | sd_bus_creds \*`c``)`; |

 

|                                             |                        |
|---------------------------------------------|------------------------|
| `sd_bus_creds *`**`sd_bus_creds_unref`**`(` | sd_bus_creds \*`c``)`; |

 

|                                     |                          |
|-------------------------------------|--------------------------|
| `void `**`sd_bus_creds_unrefp`**`(` | sd_bus_creds \*\*`c``)`; |

 

`SD_BUS_CREDS_PID`, `SD_BUS_CREDS_PPID`, `SD_BUS_CREDS_TID`, `SD_BUS_CREDS_UID`, `SD_BUS_CREDS_EUID`, `SD_BUS_CREDS_SUID`, `SD_BUS_CREDS_FSUID`, `SD_BUS_CREDS_GID`, `SD_BUS_CREDS_EGID`, `SD_BUS_CREDS_SGID`, `SD_BUS_CREDS_FSGID`, `SD_BUS_CREDS_SUPPLEMENTARY_GIDS`, `SD_BUS_CREDS_COMM`, `SD_BUS_CREDS_TID_COMM`, `SD_BUS_CREDS_EXE`, `SD_BUS_CREDS_CMDLINE`, `SD_BUS_CREDS_CGROUP`, `SD_BUS_CREDS_UNIT`, `SD_BUS_CREDS_SLICE`, `SD_BUS_CREDS_USER_UNIT`, `SD_BUS_CREDS_USER_SLICE`, `SD_BUS_CREDS_SESSION`, `SD_BUS_CREDS_OWNER_UID`, `SD_BUS_CREDS_EFFECTIVE_CAPS`, `SD_BUS_CREDS_PERMITTED_CAPS`, `SD_BUS_CREDS_INHERITABLE_CAPS`, `SD_BUS_CREDS_BOUNDING_CAPS`, `SD_BUS_CREDS_SELINUX_CONTEXT`, `SD_BUS_CREDS_AUDIT_SESSION_ID`, `SD_BUS_CREDS_AUDIT_LOGIN_UID`, `SD_BUS_CREDS_TTY`, `SD_BUS_CREDS_UNIQUE_NAME`, `SD_BUS_CREDS_WELL_KNOWN_NAMES`, `SD_BUS_CREDS_DESCRIPTION`, `SD_BUS_CREDS_PIDFD`, `SD_BUS_CREDS_AUGMENT`, `_SD_BUS_CREDS_ALL`

## Description

`sd_bus_creds_new_from_pid()` creates a new credentials object and fills it with information about the process *`pid`*. The pointer to this object will be stored in the *`ret`* pointer. Note that credential objects may also be created and retrieved via sd_bus_get_name_creds(3), sd_bus_get_owner_creds(3) and sd_bus_message_get_creds(3).

`sd_bus_creds_new_from_pidfd()` is identical to `sd_bus_creds_new_from_pid()`, but takes a PID file descriptor rather than a numeric PID as reference to the process. See pidfd_open(2).

The information that will be stored is determined by *`creds_mask`*. It may contain a subset of ORed constants `SD_BUS_CREDS_PID`, `SD_BUS_CREDS_PPID`, `SD_BUS_CREDS_TID`, `SD_BUS_CREDS_UID`, `SD_BUS_CREDS_EUID`, `SD_BUS_CREDS_SUID`, `SD_BUS_CREDS_FSUID`, `SD_BUS_CREDS_GID`, `SD_BUS_CREDS_EGID`, `SD_BUS_CREDS_SGID`, `SD_BUS_CREDS_FSGID`, `SD_BUS_CREDS_SUPPLEMENTARY_GIDS`, `SD_BUS_CREDS_COMM`, `SD_BUS_CREDS_TID_COMM`, `SD_BUS_CREDS_EXE`, `SD_BUS_CREDS_CMDLINE`, `SD_BUS_CREDS_CGROUP`, `SD_BUS_CREDS_UNIT`, `SD_BUS_CREDS_SLICE`, `SD_BUS_CREDS_USER_UNIT`, `SD_BUS_CREDS_USER_SLICE`, `SD_BUS_CREDS_SESSION`, `SD_BUS_CREDS_OWNER_UID`, `SD_BUS_CREDS_EFFECTIVE_CAPS`, `SD_BUS_CREDS_PERMITTED_CAPS`, `SD_BUS_CREDS_INHERITABLE_CAPS`, `SD_BUS_CREDS_BOUNDING_CAPS`, `SD_BUS_CREDS_SELINUX_CONTEXT`, `SD_BUS_CREDS_AUDIT_SESSION_ID`, `SD_BUS_CREDS_AUDIT_LOGIN_UID`, `SD_BUS_CREDS_TTY`, `SD_BUS_CREDS_UNIQUE_NAME`, `SD_BUS_CREDS_WELL_KNOWN_NAMES`, `SD_BUS_CREDS_DESCRIPTION`, and `SD_BUS_CREDS_PIDFD`. Use the special value `_SD_BUS_CREDS_ALL` to request all supported fields. The `SD_BUS_CREDS_AUGMENT` constant may not be ORed into the mask for invocations of `sd_bus_creds_new_from_pid()` or `sd_bus_creds_new_from_pidfd()`.

Fields can be retrieved from the credentials object using sd_bus_creds_get_pid(3) and other functions which correspond directly to the constants listed above.

A mask of fields which were actually successfully retrieved can be retrieved with `sd_bus_creds_get_mask()`. If the credentials object was created with `sd_bus_creds_new_from_pid()` or `sd_bus_creds_new_from_pidfd()`, this will be a subset of fields requested in *`creds_mask`*.

Similar to `sd_bus_creds_get_mask()`, the function `sd_bus_creds_get_augmented_mask()` returns a bitmask of field constants. The mask indicates which credential fields have been retrieved in a non-atomic fashion. For credential objects created via `sd_bus_creds_new_from_pid()` or `sd_bus_creds_new_from_pidfd()`, this mask will be identical to the mask returned by `sd_bus_creds_get_mask()`. However, for credential objects retrieved via `sd_bus_get_name_creds()`, this mask will be set for the credential fields that could not be determined atomically at peer connection time, and which were later added by reading augmenting credential data from `/proc/`. Similarly, for credential objects retrieved via `sd_bus_get_owner_creds()`, the mask is set for the fields that could not be determined atomically at bus creation time, but have been augmented. Similarly, for credential objects retrieved via `sd_bus_message_get_creds()`, the mask is set for the fields that could not be determined atomically at message sending time, but have been augmented. The mask returned by `sd_bus_creds_get_augmented_mask()` is always a subset of (or identical to) the mask returned by `sd_bus_creds_get_mask()` for the same object. The latter call hence returns all credential fields available in the credential object, the former then marks the subset of those that have been augmented. Note that augmented fields are unsuitable for authorization decisions, as they may be retrieved at different times, thus being subject to races. Hence, augmented fields should be used exclusively for informational purposes.

`sd_bus_creds_ref()` creates a new reference to the credentials object *`c`*. This object will not be destroyed until `sd_bus_creds_unref()` has been called as many times plus once more. Once the reference count has dropped to zero, *`c`* cannot be used anymore, so further calls to `sd_bus_creds_ref(c)` or `sd_bus_creds_unref(c)` are illegal.

`sd_bus_creds_unref()` destroys a reference to *`c`*.

`sd_bus_creds_unrefp()` is similar to `sd_bus_creds_unref()` but takes a pointer to a pointer to an sd_bus_creds object. This call is useful in conjunction with GCC's and LLVM's Clean-up Variable Attribute. Note that this function is defined as inline function.

`sd_bus_creds_ref()`, `sd_bus_creds_unref()` and `sd_bus_creds_unrefp()` execute no operation if the passed in bus credentials object is `NULL`.

## Return Value

On success, `sd_bus_creds_new_from_pid()` and `sd_bus_creds_new_from_pidfd()` return 0 or a positive integer. On failure, they return a negative errno-style error code.

`sd_bus_creds_get_mask()` returns the mask of successfully acquired fields.

`sd_bus_creds_get_augmented_mask()` returns the mask of fields that have been augmented from data in `/proc/`, and are thus not suitable for authorization decisions.

`sd_bus_creds_ref()` always returns the argument.

`sd_bus_creds_unref()` always returns `NULL`.

## Reference ownership

The functions `sd_bus_creds_new_from_pid()` and `sd_bus_creds_new_from_pidfd()` create a new object and the caller owns the sole reference. When not needed anymore, this reference should be destroyed with sd_bus_creds_unref(3).

### Errors

Returned errors may indicate the following problems:

`-ESRCH`  
Specified *`pid`* could not be found.

`-EINVAL`  
Specified parameter is invalid (`NULL` in case of output parameters).

`-ENOMEM`  
Memory allocation failed.

`-EOPNOTSUPP`  
One of the requested fields is unknown to the local system.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_creds_new_from_pid()`, `sd_bus_creds_get_mask()`, `sd_bus_creds_ref()`, `sd_bus_creds_unref()`, and `sd_bus_creds_get_augmented_mask()` were added in version 221.

`sd_bus_creds_unrefp()` was added in version 229.

`sd_bus_creds_new_from_pidfd()` was added in version 256.

## See Also

systemd(1), sd-bus(3), sd_bus_creds_get_pid(3), sd_bus_get_name_creds(3), sd_bus_get_owner_creds(3), sd_bus_message_get_creds(3)
