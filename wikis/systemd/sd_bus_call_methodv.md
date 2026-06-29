## Name

sd_bus_call_method, sd_bus_call_methodv, sd_bus_call_method_async, sd_bus_call_method_asyncv — Initialize a bus message object and invoke the corresponding D-Bus method call

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|  |  |
|----|----|
| `typedef int (*`**`sd_bus_message_handler_t`**`)(` | sd_bus_message \*`m`, |
|   | void \*`userdata`, |
|   | sd_bus_error \*`ret_error``)`; |

 

|                                   |                             |
|-----------------------------------|-----------------------------|
| `int `**`sd_bus_call_method`**`(` | sd_bus \*`bus`,             |
|                                   | const char \*`destination`, |
|                                   | const char \*`path`,        |
|                                   | const char \*`interface`,   |
|                                   | const char \*`member`,      |
|                                   | sd_bus_error \*`ret_error`, |
|                                   | sd_bus_message \*\*`reply`, |
|                                   | const char \*`types`,       |
|                                   | ...`)`;                     |

 

|                                    |                             |
|------------------------------------|-----------------------------|
| `int `**`sd_bus_call_methodv`**`(` | sd_bus \*`bus`,             |
|                                    | const char \*`destination`, |
|                                    | const char \*`path`,        |
|                                    | const char \*`interface`,   |
|                                    | const char \*`member`,      |
|                                    | sd_bus_error \*`ret_error`, |
|                                    | sd_bus_message \*\*`reply`, |
|                                    | const char \*`types`,       |
|                                    | va_list `ap``)`;            |

 

|  |  |
|----|----|
| `int `**`sd_bus_call_method_async`**`(` | sd_bus \*`bus`, |
|   | sd_bus_slot \*\*`slot`, |
|   | const char \*`destination`, |
|   | const char \*`path`, |
|   | const char \*`interface`, |
|   | const char \*`member`, |
|   | sd_bus_message_handler_t `callback`, |
|   | void \*`userdata`, |
|   | const char \*`types`, |
|   | ...`)`; |

 

|  |  |
|----|----|
| `int `**`sd_bus_call_method_asyncv`**`(` | sd_bus \*`bus`, |
|   | sd_bus_slot \*\*`slot`, |
|   | const char \*`destination`, |
|   | const char \*`path`, |
|   | const char \*`interface`, |
|   | const char \*`member`, |
|   | sd_bus_message_handler_t `callback`, |
|   | void \*`userdata`, |
|   | const char \*`types`, |
|   | va_list `ap``)`; |

 

## Description

`sd_bus_call_method()` is a convenience function for initializing a bus message object and calling the corresponding D-Bus method. It combines the sd_bus_message_new_method_call(3), sd_bus_message_append(3) and sd_bus_call(3) functions into a single function call.

`sd_bus_call_method_async()` is a convenience function for initializing a bus message object and calling the corresponding D-Bus method asynchronously. It combines the sd_bus_message_new_method_call(3), sd_bus_message_append(3) and sd_bus_call_async(3) functions into a single function call.

## Return Value

On success, these functions return a non-negative integer. On failure, they return a negative errno-style error code.

### Errors

See the man pages of sd_bus_message_new_method_call(3), sd_bus_message_append(3), sd_bus_call(3) and sd_bus_call_async(3) for a list of possible errors.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## Examples

**Example 1. Make a call to a D-Bus method that takes a single parameter**

``` programlisting
/* SPDX-License-Identifier: MIT-0 */

/* This is equivalent to:
 * busctl call org.freedesktop.systemd1 /org/freedesktop/systemd1 \
 *       org.freedesktop.systemd1.Manager GetUnitByPID $$
 *
 * Compile with 'cc print-unit-path-call-method.c -lsystemd'
 */

#include <errno.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

#include <systemd/sd-bus.h>

#define _cleanup_(f) __attribute__((cleanup(f)))
#define DESTINATION "org.freedesktop.systemd1"
#define PATH        "/org/freedesktop/systemd1"
#define INTERFACE   "org.freedesktop.systemd1.Manager"
#define MEMBER      "GetUnitByPID"

static int log_error(int error, const char *message) {
  fprintf(stderr, "%s: %s\n", message, strerror(-error));
  return error;
}

int main(int argc, char **argv) {
  _cleanup_(sd_bus_flush_close_unrefp) sd_bus *bus = NULL;
  _cleanup_(sd_bus_error_free) sd_bus_error error = SD_BUS_ERROR_NULL;
  _cleanup_(sd_bus_message_unrefp) sd_bus_message *reply = NULL;
  int r;

  r = sd_bus_open_system(&bus);
  if (r < 0)
    return log_error(r, "Failed to acquire bus");

  r = sd_bus_call_method(bus, DESTINATION, PATH, INTERFACE, MEMBER, &error, &reply, "u", (unsigned) getpid());
  if (r < 0)
    return log_error(r, MEMBER " call failed");

  const char *ans;
  r = sd_bus_message_read(reply, "o", &ans);
  if (r < 0)
    return log_error(r, "Failed to read reply");

  printf("Unit path is \"%s\".\n", ans);

  return 0;
}
```

This defines a minimally useful program that will open a connection to the bus, call a method, wait for the reply, and finally extract and print the answer. It does error handling and proper memory management.

  

## History

`sd_bus_call_method()`, and `sd_bus_call_method_async()` were added in version 221.

`sd_bus_call_methodv()`, `sd_bus_call_method_asyncv()` were added in version 246.

## See Also

systemd(1), sd-bus(3), sd_bus_message_new_method_call(3), sd_bus_message_append(3), sd_bus_call(3), sd_bus_set_property(3), sd_bus_emit_signal(3)
