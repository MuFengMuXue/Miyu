## Name

sd_bus_message_new_method_call, sd_bus_message_new_method_return — Create a method call message

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                               |                             |
|-----------------------------------------------|-----------------------------|
| `int `**`sd_bus_message_new_method_call`**`(` | sd_bus \*`bus`,             |
|                                               | sd_bus_message \*\*`m`,     |
|                                               | const char \*`destination`, |
|                                               | const char \*`path`,        |
|                                               | const char \*`interface`,   |
|                                               | const char \*`member``)`;   |

 

|  |  |
|----|----|
| `int `**`sd_bus_message_new_method_return`**`(` | sd_bus_message \*`call`, |
|   | sd_bus_message \*\*`m``)`; |

 

## Description

The `sd_bus_message_new_method_call()` function creates a new bus message object that encapsulates a D-Bus method call, and returns it in the *`m`* output parameter. The call will be made on the destination *`destination`*, path *`path`*, on the interface *`interface`*, member *`member`*.

Briefly, the *destination* is a dot-separated name that identifies a service connected to the bus. The *path* is a slash-separated identifier of an object within the destination that resembles a file system path. The meaning of this path is defined by the destination. The *interface* is a dot-separated name that resembles a Java interface name that identifies a group of methods and signals supported by the object identified by path. Methods and signals are collectively called *members* and are identified by a simple name composed of ASCII letters, numbers, and underscores. See the D-Bus Tutorial for an in-depth explanation.

The *`destination`* parameter may be `NULL`. The *`interface`* parameter may be `NULL`, if the destination has only a single member with the given name and there is no ambiguity if the interface name is omitted.

Note that this is a low level interface. See sd_bus_call_method(3) for a more convenient way of calling D-Bus methods.

The `sd_bus_message_new_method_return()` function creates a new bus message object that is a reply to the method call *`call`* and returns it in the *`m`* output parameter. The *`call`* parameter must be a method call message. The sender of *`call`* is used as the destination.

## Return Value

On success, these functions return a non-negative integer. On failure, they return a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
The output parameter *`m`* is `NULL`.

The *`destination`* parameter is non-null and is not a valid D-Bus service name ("`org.somewhere.Something`"), the *`path`* parameter is not a valid D-Bus path ("`/an/object/path`"), the *`interface`* parameter is non-null and is not a valid D-Bus interface name ("`an.interface.name`"), or the *`member`* parameter is not a valid D-Bus member ("`Name`").

The *`call`* parameter is not a method call object.

`-ENOTCONN`  
The bus parameter *`bus`* is `NULL` or the bus is not connected.

`-ENOMEM`  
Memory allocation failed.

`-EPERM`  
The *`call`* parameter is not sealed.

`-EOPNOTSUPP`  
The *`call`* message does not have a cookie.

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
 * Compile with 'cc print-unit-path.c -lsystemd'
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
  _cleanup_(sd_bus_message_unrefp) sd_bus_message *reply = NULL, *m = NULL;
  int r;

  r = sd_bus_open_system(&bus);
  if (r < 0)
    return log_error(r, "Failed to acquire bus");

  r = sd_bus_message_new_method_call(bus, &m,
                                     DESTINATION, PATH, INTERFACE, MEMBER);
  if (r < 0)
    return log_error(r, "Failed to create bus message");

  r = sd_bus_message_append(m, "u", (unsigned) getpid());
  if (r < 0)
    return log_error(r, "Failed to append to bus message");

  r = sd_bus_call(bus, m, -1, &error, &reply);
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

This defines a minimally useful program that will open a connection to the bus, create a message object, send it, wait for the reply, and finally extract and print the answer. It does error handling and proper memory management.

  

## History

`sd_bus_message_new_method_call()` and `sd_bus_message_new_method_return()` were added in version 246.

## See Also

systemd(1), sd-bus(3), sd_bus_call(3), sd_bus_call_method(3), sd_bus_path_encode(3)
