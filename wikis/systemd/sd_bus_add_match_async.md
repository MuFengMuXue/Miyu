## Name

sd_bus_add_match, sd_bus_add_match_async, sd_bus_match_signal, sd_bus_match_signal_async — Add a match rule for incoming message dispatching

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|  |  |
|----|----|
| `typedef int (*`**`sd_bus_message_handler_t`**`)(` | sd_bus_message \*`m`, |
|   | void \*`userdata`, |
|   | sd_bus_error \*`ret_error``)`; |

 

|                                 |                                      |
|---------------------------------|--------------------------------------|
| `int `**`sd_bus_add_match`**`(` | sd_bus \*`bus`,                      |
|                                 | sd_bus_slot \*\*`slot`,              |
|                                 | const char \*`match`,                |
|                                 | sd_bus_message_handler_t `callback`, |
|                                 | void \*`userdata``)`;                |

 

|  |  |
|----|----|
| `int `**`sd_bus_add_match_async`**`(` | sd_bus \*`bus`, |
|   | sd_bus_slot \*\*`slot`, |
|   | const char \*`match`, |
|   | sd_bus_message_handler_t `callback`, |
|   | sd_bus_message_handler_t `install_callback`, |
|   | void \*`userdata``)`; |

 

|                                    |                                      |
|------------------------------------|--------------------------------------|
| `int `**`sd_bus_match_signal`**`(` | sd_bus \*`bus`,                      |
|                                    | sd_bus_slot \*\*`slot`,              |
|                                    | const char \*`sender`,               |
|                                    | const char \*`path`,                 |
|                                    | const char \*`interface`,            |
|                                    | const char \*`member`,               |
|                                    | sd_bus_message_handler_t `callback`, |
|                                    | void \*`userdata``)`;                |

 

|  |  |
|----|----|
| `int `**`sd_bus_match_signal_async`**`(` | sd_bus \*`bus`, |
|   | sd_bus_slot \*\*`slot`, |
|   | const char \*`sender`, |
|   | const char \*`path`, |
|   | const char \*`interface`, |
|   | const char \*`member`, |
|   | sd_bus_message_handler_t `callback`, |
|   | sd_bus_message_handler_t `install_callback`, |
|   | void \*`userdata``)`; |

 

## Description

`sd_bus_add_match()` installs a match rule for messages received on the specified bus connection object *`bus`*. The syntax of the match rule expression passed in *`match`* is described in the D-Bus Specification. The specified handler function *`callback`* is called for each incoming message matching the specified expression, the *`userdata`* parameter is passed as-is to the callback function. The match is installed synchronously when connected to a bus broker, i.e. the call sends a control message requested the match to be added to the broker and waits until the broker confirms the match has been installed successfully.

`sd_bus_add_match_async()` operates very similarly to `sd_bus_add_match()`, however it installs the match asynchronously, in a non-blocking fashion: a request is sent to the broker, but the call does not wait for a response. The *`install_callback`* function is called when the response is later received, with the response message from the broker as parameter. If this function is specified as `NULL` a default implementation is used that terminates the bus connection should installing the match fail.

`sd_bus_match_signal()` is very similar to `sd_bus_add_match()`, but only matches signals, and instead of a match expression accepts four parameters: *`sender`* (the service name of the sender), *`path`* (the object path of the emitting object), *`interface`* (the interface the signal belongs to), *`member`* (the signal name), from which the match string is internally generated. Optionally, these parameters may be specified as `NULL` in which case the relevant field of incoming signals is not tested.

`sd_bus_match_signal_async()` combines the signal matching logic of `sd_bus_match_signal()` with the asynchronous behaviour of `sd_bus_add_match_async()`.

On success, and if non-`NULL`, the *`slot`* return parameter will be set to a slot object that may be used as a reference to the installed match, and may be utilized to remove it again at a later time with sd_bus_slot_unref(3). If specified as `NULL` the lifetime of the match is bound to the lifetime of the bus object itself, and the match is generally not removed independently. See sd_bus_slot_set_floating(3) for details.

The message *`m`* passed to the callback is only borrowed, that is, the callback should not call sd_bus_message_unref(3) on it. If the callback wants to hold on to the message beyond the lifetime of the callback, it needs to call sd_bus_message_ref(3) to create a new reference.

If an error occurs during the callback invocation, the callback should return a negative error number (optionally, a more precise error may be returned in *`ret_error`*, as well). If it wants other callbacks that match the same rule to be called, it should return 0. Otherwise, it should return a positive integer.

If the *`bus`* refers to a direct connection (i.e. not a bus connection, as set with sd_bus_set_bus_client(3)) the match is only installed on the client side, and the synchronous and asynchronous functions operate the same.

## Return Value

On success, `sd_bus_add_match()` and the other calls return 0 or a positive integer. On failure, they return a negative errno-style error code.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_add_match()` and `sd_bus_message_handler_t()` were added in version 221.

`sd_bus_add_match_async()`, `sd_bus_match_signal()`, and `sd_bus_match_signal_async()` were added in version 237.

## See Also

systemd(1), sd-bus(3), sd_bus_slot_unref(3), sd_bus_message_ref(3), sd_bus_set_bus_client(3), sd_bus_slot_set_floating(3)
