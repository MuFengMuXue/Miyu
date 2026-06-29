## Name

sd_bus_slot_ref, sd_bus_slot_unref, sd_bus_slot_unrefp — Create and destroy references to a bus slot object

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                         |                          |
|-----------------------------------------|--------------------------|
| `sd_bus_slot *`**`sd_bus_slot_ref`**`(` | sd_bus_slot \*`slot``)`; |

 

|                                           |                          |
|-------------------------------------------|--------------------------|
| `sd_bus_slot *`**`sd_bus_slot_unref`**`(` | sd_bus_slot \*`slot``)`; |

 

|                                    |                             |
|------------------------------------|-----------------------------|
| `void `**`sd_bus_slot_unrefp`**`(` | sd_bus_slot \*\*`slotp``)`; |

 

## Description

`sd_bus_slot_ref()` increases the internal reference counter of *`slot`* by one.

`sd_bus_slot_unref()` decreases the internal reference counter of *`slot`* by one. Once the reference count has dropped to zero, slot object is destroyed and cannot be used anymore, so further calls to `sd_bus_slot_ref()` or `sd_bus_slot_unref()` are illegal.

`sd_bus_slot_unrefp()` is similar to `sd_bus_slot_unref()` but takes a pointer to a pointer to an sd_bus_slot object. This call is useful in conjunction with GCC's and LLVM's Clean-up Variable Attribute. See sd_bus_new(3) for an example how to use the cleanup attribute.

`sd_bus_slot_ref()` and `sd_bus_slot_unref()` execute no operation if the passed in bus object address is `NULL`. `sd_bus_slot_unrefp()` will first dereference its argument, which must not be `NULL`, and will execute no operation if *that* is `NULL`.

## Return Value

`sd_bus_slot_ref()` always returns the argument.

`sd_bus_slot_unref()` always returns `NULL`.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_slot_ref()`, `sd_bus_slot_unref()`, and `sd_bus_slot_unrefp()` were added in version 240.

## See Also

systemd(1), sd-bus(3), sd_bus_new(3), sd_bus_message_new(3), sd_bus_call_method_async(3)
