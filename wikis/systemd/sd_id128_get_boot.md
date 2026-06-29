## Name

sd_id128_get_machine, sd_id128_get_app_specific, sd_id128_get_machine_app_specific, sd_id128_get_boot, sd_id128_get_boot_app_specific, sd_id128_get_invocation — Retrieve 128-bit IDs

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-id128.h>
```

|                                     |                        |
|-------------------------------------|------------------------|
| `int `**`sd_id128_get_machine`**`(` | sd_id128_t \*`ret``)`; |

 

|                                          |                        |
|------------------------------------------|------------------------|
| `int `**`sd_id128_get_app_specific`**`(` | sd_id128_t `base`,     |
|                                          | sd_id128_t `app_id`,   |
|                                          | sd_id128_t \*`ret``)`; |

 

|                                                  |                        |
|--------------------------------------------------|------------------------|
| `int `**`sd_id128_get_machine_app_specific`**`(` | sd_id128_t `app_id`,   |
|                                                  | sd_id128_t \*`ret``)`; |

 

|                                  |                        |
|----------------------------------|------------------------|
| `int `**`sd_id128_get_boot`**`(` | sd_id128_t \*`ret``)`; |

 

|                                               |                        |
|-----------------------------------------------|------------------------|
| `int `**`sd_id128_get_boot_app_specific`**`(` | sd_id128_t `app_id`,   |
|                                               | sd_id128_t \*`ret``)`; |

 

|                                        |                        |
|----------------------------------------|------------------------|
| `int `**`sd_id128_get_invocation`**`(` | sd_id128_t \*`ret``)`; |

 

|  |  |
|----|----|
| `int `**`sd_id128_get_invocation_app_specific`**`(` | sd_id128_t `app_id`, |
|   | sd_id128_t \*`ret``)`; |

 

## Description

`sd_id128_get_machine()` returns the machine ID of the executing host. This reads and parses the machine-id(5) file. This function caches the machine ID internally to make retrieving the machine ID a cheap operation. This ID may be used wherever a unique identifier for the local system is needed. However, it is recommended to use this ID as-is only in trusted environments. In untrusted environments it is recommended to derive an application specific ID from this machine ID, in an irreversible (cryptographically secure) way. To make this easy `sd_id128_get_machine_app_specific()` is provided, see below.

`sd_id128_get_app_specific()` returns a machine ID that is a combination of the *`base`* and *`app_id`* parameters. Internally, this function calculates HMAC-SHA256 of the *`app_id`* parameter keyed by the *`base`* parameter, and truncates this result to fit in sd_id128_t and turns it into a valid Variant 1 Version 4 UUID, in accordance with RFC 4122. Neither of the two input parameters can be calculated from the output parameter *`ret`*.

`sd_id128_get_machine_app_specific()` is similar to `sd_id128_get_machine()`, but retrieves a machine ID that is specific to the application that is identified by the indicated application ID. It is recommended to use this function instead of `sd_id128_get_machine()` when passing an ID to untrusted environments, in order to make sure that the original machine ID may not be determined externally. This way, the ID used by the application remains stable on a given machine, but cannot be easily correlated with IDs used in other applications on the same machine. The application-specific ID should be generated via a tool like **systemd-id128 new**, and may be compiled into the application. This function will return the same application-specific ID for each combination of machine ID and application ID. Internally, this function calls `sd_id128_get_app_specific()` with the result from `sd_id128_get_machine()` and the *`app_id`* parameter.

`sd_id128_get_boot()` returns the boot ID of the executing kernel. This reads and parses the `/proc/sys/kernel/random/boot_id` file exposed by the kernel. It is randomly generated early at boot and is unique for every running kernel instance. See random(4) for more information. This function also internally caches the returned ID to make this call a cheap operation. It is recommended to use this ID as-is only in trusted environments. In untrusted environments it is recommended to derive an application specific ID using `sd_id128_get_boot_app_specific()`, see below.

`sd_id128_get_boot_app_specific()` is analogous to `sd_id128_get_machine_app_specific()`, but returns an ID that changes between boots. Some machines may be used for a long time without rebooting, hence the boot ID may remain constant for a long time, and has properties similar to the machine ID during that time.

`sd_id128_get_invocation()` returns the invocation ID of the currently executed service. In its current implementation, this tries to read and parse the following:

- The `$INVOCATION_ID` environment variable that the service manager sets when activating a service.

- An entry in the kernel keyring that the system service manager sets when activating a service.

See systemd.exec(5) for details. The ID is cached internally. In future a different mechanism to determine the invocation ID may be added.

`sd_id128_get_invocation_app_specific()` derives an application-specific ID from the invocation ID.

Note that `sd_id128_get_machine_app_specific()`, `sd_id128_get_boot()`, `sd_id128_get_boot_app_specific()`, `sd_id128_get_invocation()` and `sd_id128_get_invocation_app_specific` always return UUID Variant 1 Version 4 compatible IDs. `sd_id128_get_machine()` will also return a UUID Variant 1 Version 4 compatible ID on new installations but might not on older. It is possible to convert the machine ID non-reversibly into a UUID Variant 1 Version 4 compatible one. For more information, see machine-id(5). It is hence guaranteed that these functions will never return the ID consisting of all zero or all one bits (`SD_ID128_NULL`, `SD_ID128_ALLF`) — with the possible exception of `sd_id128_get_machine()`, as mentioned.

For more information about the "`sd_id128_t`" type see sd-id128(3).

## Return Value

Those calls return 0 on success (in which case *`ret`* is filled in), or a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-ENOENT`  
Returned by `sd_id128_get_machine()` and `sd_id128_get_machine_app_specific()` when `/etc/machine-id` is missing.

Added in version 242.

`-ENOMEDIUM`  
Returned by `sd_id128_get_machine()` and `sd_id128_get_machine_app_specific()` when `/etc/machine-id` is empty or all zeros. Also returned by `sd_id128_get_invocation()` when the invocation ID is all zeros.

Added in version 242.

`-ENOPKG`  
Returned by `sd_id128_get_machine()` and `sd_id128_get_machine_app_specific()` when the content of `/etc/machine-id` is "`uninitialized`".

Added in version 253.

`-ENOSYS`  
Returned by `sd_id128_get_boot()` and `sd_id128_get_boot_app_specific()` when `/proc/` is not mounted.

Added in version 253.

`-ENXIO`  
Returned by `sd_id128_get_invocation()` if no invocation ID is set. Also returned by `sd_id128_get_app_specific()`, `sd_id128_get_machine_app_specific()`, and `sd_id128_get_boot_app_specific()` when the *`app_id`* parameter is all zeros.

Added in version 242.

`-EUCLEAN`  
Returned by any of the functions described here when the configured value has invalid format.

Added in version 253.

`-EPERM`  
Requested information could not be retrieved because of insufficient permissions.

Added in version 242.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## Examples

**Example 1. Application-specific machine ID**

First, generate the application ID:

``` programlisting
$ systemd-id128 -p new
As string:
c273277323db454ea63bb96e79b53e97

As UUID:
c2732773-23db-454e-a63b-b96e79b53e97

As man:sd-id128(3) macro:
#define MESSAGE_XYZ SD_ID128_MAKE(c2,73,27,73,23,db,45,4e,a6,3b,b9,6e,79,b5,3e,97)
...
```

Then use the new identifier in an example application:

``` programlisting
/* SPDX-License-Identifier: MIT-0 */

#include <stdio.h>
#include <systemd/sd-id128.h>

#define OUR_APPLICATION_ID SD_ID128_MAKE(c2,73,27,73,23,db,45,4e,a6,3b,b9,6e,79,b5,3e,97)

int main(int argc, char *argv[]) {
  sd_id128_t id;
  sd_id128_get_machine_app_specific(OUR_APPLICATION_ID, &id);
  printf("Our application ID: " SD_ID128_FORMAT_STR "\n", SD_ID128_FORMAT_VAL(id));
  return 0;
}
```

  

## History

`sd_id128_get_machine()` and `sd_id128_get_boot()` were added in version 187.

`sd_id128_get_invocation()` was added in version 232.

`sd_id128_get_machine_app_specific()` was added in version 233.

`sd_id128_get_boot_app_specific()` was added in version 240.

`sd_id128_get_app_specific()` was added in version 255.

`sd_id128_get_invocation_app_specific()` was added in version 256.

## See Also

systemd(1), systemd-id128(1), sd-id128(3), machine-id(5), systemd.exec(5), sd_id128_randomize(3), random(4)
