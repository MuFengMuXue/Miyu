## Name

sd_bus_message_new_signal, sd_bus_message_new_signal_to — Create a signal message

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                  |                           |
|----------------------------------|---------------------------|
| `int sd_bus_message_new_signal(` | sd_bus \*`bus`,           |
|                                  | sd_bus_message \*\*`m`,   |
|                                  | const char \*`path`,      |
|                                  | const char \*`interface`, |
|                                  | const char \*`member``)`; |

 

|                                     |                             |
|-------------------------------------|-----------------------------|
| `int sd_bus_message_new_signal_to(` | sd_bus \*`bus`,             |
|                                     | sd_bus_message \*\*`m`,     |
|                                     | const char \*`destination`, |
|                                     | const char \*`path`,        |
|                                     | const char \*`interface`,   |
|                                     | const char \*`member``)`;   |

 

## Description

The `sd_bus_message_new_signal()` function creates a new bus message object that encapsulates a D-Bus signal, and returns it in the *`m`* output parameter. The signal will be sent to path *`path`*, on the interface *`interface`*, member *`member`*. When this message is sent, no reply is expected. See sd_bus_message_new_method_call(3) for a short description of the meaning of the *`path`*, *`interface`*, and *`member`* parameters.

`sd_bus_message_new_signal_to()` is a shorthand for creating a new bus message to a specific destination. It's behavior is similar to calling `sd_bus_message_new_signal()` followed by calling sd_bus_message_set_destination(3).

## Return Value

This function returns 0 if the message object was successfully created, and a negative errno-style error code otherwise.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
The output parameter *`m`* is `NULL`.

The *`path`* parameter is not a valid D-Bus path ("`/an/object/path`"), the *`interface`* parameter is not a valid D-Bus interface name ("`an.interface.name`"), or the *`member`* parameter is not a valid D-Bus member ("`Name`").

`-ENOTCONN`  
The bus parameter *`bus`* is `NULL` or the bus is not connected.

`-ENOMEM`  
Memory allocation failed.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## Examples

**Example 1. Send a simple signal**

``` programlisting
/* SPDX-License-Identifier: MIT-0 */

#include <systemd/sd-bus.h>
#define _cleanup_(f) __attribute__((cleanup(f)))

int send_unit_files_changed(sd_bus *bus) {
  _cleanup_(sd_bus_message_unrefp) sd_bus_message *message = NULL;
  int r;

  r = sd_bus_message_new_signal(bus, &message,
                                "/org/freedesktop/systemd1",
                                "org.freedesktop.systemd1.Manager",
                                "UnitFilesChanged");
  if (r < 0)
    return r;

  return sd_bus_send(bus, message, NULL);
}
```

This function in systemd sources is used to emit the "`UnitFilesChanged`" signal when the unit files have been changed.

  

## See Also

systemd(1), sd-bus(3), sd_bus_emit_signal(3), sd_bus_message_set_destination(3)
