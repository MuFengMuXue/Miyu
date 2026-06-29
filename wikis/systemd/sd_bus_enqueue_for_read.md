## Name

sd_bus_enqueue_for_read — Re-enqueue a bus message on a bus connection, for reading

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                        |                                |
|----------------------------------------|--------------------------------|
| `int `**`sd_bus_enqueue_for_read`**`(` | sd_bus \*`bus`,                |
|                                        | sd_bus_message \*`message``)`; |

 

## Description

`sd_bus_enqueue_for_read()` may be used to re-enqueue an incoming bus message on the local read queue, so that it is processed and dispatched locally again, similarly to how an incoming message from the peer is processed. Takes a bus connection object and the message to enqueue. A reference is taken of the message and the caller's reference thus remains in possession of the caller. The message is enqueued at the end of the queue, thus will be dispatched after all other already queued messages are dispatched.

This call is primarily useful for dealing with incoming method calls that may be processed only after an additional asynchronous operation completes. One example are PolicyKit authorization requests that are determined to be necessary to authorize a newly incoming method call: when the PolicyKit response is received the original method call may be re-enqueued to process it again, this time with the authorization result known.

## Return Value

On success, this function return 0 or a positive integer. On failure, it returns a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-ECHILD`  
The bus connection has been created in a different process, library or module instance.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_enqueue_for_read()` was added in version 245.

## See Also

systemd(1), sd-bus(3), sd_bus_send(3)
