## Name

sd_bus_pending_method_calls — Return the number of currently pending, outgoing method calls

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                            |                    |
|--------------------------------------------|--------------------|
| `int `**`sd_bus_pending_method_calls`**`(` | sd_bus \*`bus``)`; |

 

## Description

`sd_bus_pending_method_calls()` returns the number of currently pending outgoing method calls, i.e. method calls enqueued with sd_bus_call_async(3) for which no reply has been received yet, and which have not reached a timeout yet.

The *`bus`* argument may be `NULL`, in which case zero is returned.

## Return Value

This function returns 0 if there are no pending method calls, or a `NULL` bus object was specified. On failure, a negative errno-style error code is returned.

### Errors

Returned errors may indicate the following problems:

`-ECHILD`  
The bus connection has been created in a different process, library or module instance.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_pending_method_calls()` was added in version 257.

## See Also

systemd(1), sd-bus(3), sd_bus_call_async(3)
