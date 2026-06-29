## Name

sd_bus_message_open_container, sd_bus_message_close_container, sd_bus_message_enter_container, sd_bus_message_exit_container — Create and move between containers in D-Bus messages

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                      |                             |
|--------------------------------------|-----------------------------|
| `int sd_bus_message_open_container(` | sd_bus_message \*`m`,       |
|                                      | char `type`,                |
|                                      | const char \*`contents``)`; |

 

|                                       |                          |
|---------------------------------------|--------------------------|
| `int sd_bus_message_close_container(` | sd_bus_message \*`m``)`; |

 

|                                       |                             |
|---------------------------------------|-----------------------------|
| `int sd_bus_message_enter_container(` | sd_bus_message \*`m`,       |
|                                       | char `type`,                |
|                                       | const char \*`contents``)`; |

 

|                                      |                          |
|--------------------------------------|--------------------------|
| `int sd_bus_message_exit_container(` | sd_bus_message \*`m``)`; |

 

## Description

`sd_bus_message_open_container()` appends a new container to the message *`m`*. After opening a new container, it can be filled with content using sd_bus_message_append(3) and similar functions. Containers behave like a stack. To nest containers inside each other, call `sd_bus_message_open_container()` multiple times without calling `sd_bus_message_close_container()` in between. Each container will be nested inside the previous container. *`type`* represents the container type and should be one of "`r`", "`a`", "`v`" or "`e`" as described in sd_bus_message_append(3). Instead of literals, the corresponding constants `SD_BUS_TYPE_STRUCT`, `SD_BUS_TYPE_ARRAY`, `SD_BUS_TYPE_VARIANT` or `SD_BUS_TYPE_DICT_ENTRY` can also be used. *`contents`* describes the type of the container's elements and should be a D-Bus type string following the rules described in sd_bus_message_append(3).

`sd_bus_message_close_container()` closes the last container opened with `sd_bus_message_open_container()`. On success, the write pointer of the message *`m`* is positioned after the closed container in its parent container or in *`m`* itself if there is no parent container.

`sd_bus_message_enter_container()` enters the next container of the message *`m`* for reading. It behaves mostly the same as `sd_bus_message_open_container()`. Entering a container allows reading its contents with sd_bus_message_read(3) and similar functions. *`type`* and *`contents`* are the same as in `sd_bus_message_open_container()`.

`sd_bus_message_exit_container()` exits the scope of the last container entered with `sd_bus_message_enter_container()`. It behaves mostly the same as `sd_bus_message_close_container()`. Note that `sd_bus_message_exit_container()` may only be called after iterating through all members of the container, i.e. reading or skipping over them. Use sd_bus_message_skip(3) to skip over fields of a container in order to be able to exit the container with `sd_bus_message_exit_container()` without reading all members.

## Return Value

On success, these functions return a non-negative integer. `sd_bus_message_open_container()` and `sd_bus_message_close_container()` return 0. `sd_bus_message_enter_container()` returns 1 if it successfully opened a new container, and 0 if that was not possible because the end of the currently open container or message was reached. `sd_bus_message_exit_container()` returns 1 on success. On failure, all of these functions return a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
*`m`* or *`contents`* are `NULL` or *`type`* is invalid.

Added in version 246.

`-EBADMSG`  
Message *`m`* has invalid structure.

Added in version 254.

`-ENXIO`  
Message *`m`* does not have a container of type *`type`* at the current position, or the contents do not match *`contents`*.

Added in version 254.

`-EPERM`  
The message *`m`* is already sealed.

Added in version 246.

`-ESTALE`  
The message *`m`* is in an invalid state.

Added in version 246.

`-ENOMEM`  
Memory allocation failed.

Added in version 246.

`-EBUSY`  
`sd_bus_message_exit_container()` was called but there are unread members left in the container.

Added in version 247.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## Examples

**Example 1. Append an array of strings to a message**

``` programlisting
/* SPDX-License-Identifier: MIT-0 */

#include <systemd/sd-bus.h>

int append_strings_to_message(sd_bus_message *m, const char *const *arr) {
  const char *s;
  int r;

  r = sd_bus_message_open_container(m, 'a', "s");
  if (r < 0)
    return r;

  for (s = *arr; *s; s++) {
    r = sd_bus_message_append(m, "s", s);
    if (r < 0)
      return r;
  }

  return sd_bus_message_close_container(m);
}
```

  

**Example 2. Read an array of strings from a message**

``` programlisting
/* SPDX-License-Identifier: MIT-0 */

#include <stdio.h>

#include <systemd/sd-bus.h>

int read_strings_from_message(sd_bus_message *m) {
  int r;

  r = sd_bus_message_enter_container(m, 'a', "s");
  if (r < 0)
    return r;

  for (;;) {
    const char *s;

    r = sd_bus_message_read(m, "s", &s);
    if (r < 0)
      return r;
    if (r == 0)
      break;

    printf("%s\n", s);
  }

  return sd_bus_message_exit_container(m);
}
```

  

## See Also

systemd(1), sd-bus(3), sd_bus_message_append(3), sd_bus_message_read(3), sd_bus_message_skip(3), The D-Bus specification
