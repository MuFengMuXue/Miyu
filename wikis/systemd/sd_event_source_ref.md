## Name

sd_event_source_unref, sd_event_source_unrefp, sd_event_source_ref, sd_event_source_disable_unref, sd_event_source_disable_unrefp — Increase or decrease event source reference counters

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-event.h>
```

|  |  |
|----|----|
| `sd_event_source* `**`sd_event_source_unref`**`(` | sd_event_source \*`source``)`; |

 

|                                        |                                  |
|----------------------------------------|----------------------------------|
| `void `**`sd_event_source_unrefp`**`(` | sd_event_source \*\*`source``)`; |

 

|  |  |
|----|----|
| `sd_event_source* `**`sd_event_source_ref`**`(` | sd_event_source \*`source``)`; |

 

|  |  |
|----|----|
| `sd_event_source* `**`sd_event_source_disable_unref`**`(` | sd_event_source \*`source``)`; |

 

|  |  |
|----|----|
| `void `**`sd_event_source_disable_unrefp`**`(` | sd_event_source \*\*`source``)`; |

 

## Description

`sd_event_source_unref()` may be used to decrement by one the internal reference counter of the event source object specified as *`source`*. The reference counter is initially set to one, when the event source is created with calls such as sd_event_add_io(3) or sd_event_add_time(3). When the reference counter reaches zero, the object is detached from the event loop object and destroyed.

`sd_event_source_unrefp()` is similar to `sd_event_source_unref()` but takes a pointer to a pointer to an sd_event_source object. This call is useful in conjunction with GCC's and LLVM's Clean-up Variable Attribute. Note that this function is defined as inline function.

`sd_event_source_ref()` may be used to increase by one the internal reference counter of the event source object specified as *`source`*.

`sd_event_source_unref()`, `sd_bus_creds_unrefp()` and `sd_bus_creds_ref()` execute no operation if the passed event source object is `NULL`.

Note that event source objects stay alive and may be dispatched as long as they have a reference counter greater than zero. In order to drop a reference of an event source and make sure the associated event source handler function is not called anymore it is recommended to combine a call of `sd_event_source_unref()` with a prior call to `sd_event_source_set_enabled()` with `SD_EVENT_OFF` or call `sd_event_source_disable_unref()`, see below.

`sd_event_source_disable_unref()` combines a call to `sd_event_source_set_enabled()` with `SD_EVENT_OFF` with `sd_event_source_unref()`. This ensures that the source is disabled before the local reference to it is lost. The *`source`* parameter is allowed to be `NULL`.

`sd_event_source_disable_unrefp()` is similar to `sd_event_source_unrefp()`, but in addition disables the source first. This call is useful in conjunction with GCC's and LLVM's Clean-up Variable Attribute. Note that this function is defined as inline function.

## Return Value

`sd_event_source_unref()` and `sd_event_source_disable_unref()` always return `NULL`. `sd_event_source_ref()` always returns the event source object passed in.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_event_source_unref()`, `sd_event_source_unrefp()`, and `sd_event_source_ref()` were added in version 229.

`sd_event_source_disable_unref()` and `sd_event_source_disable_unrefp()` were added in version 243.

## See Also

sd-event(3), sd_event_add_io(3), sd_event_add_time(3), sd_event_add_signal(3), sd_event_add_child(3), sd_event_add_inotify(3), sd_event_add_defer(3), sd_event_source_set_enabled(3)
