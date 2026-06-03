## Name

sd_event_add_memory_pressure, sd_event_source_set_memory_pressure_type, sd_event_source_set_memory_pressure_period, sd_event_trim_memory — Add and configure an event source run as result of memory pressure

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-event.h>
```

``` funcsynopsisinfo
typedef struct sd_event_source sd_event_source;
```

|  |  |
|----|----|
| `int `**`sd_event_add_memory_pressure`**`(` | sd_event \*`event`, |
|   | sd_event_source \*\*`ret_source`, |
|   | sd_event_handler_t `handler`, |
|   | void \*`userdata``)`; |

 

|  |  |
|----|----|
| `int `**`sd_event_source_set_memory_pressure_type`**`(` | sd_event_source \*`source`, |
|   | const char \*`type``)`; |

 

|  |  |
|----|----|
| `int `**`sd_event_source_set_memory_pressure_period`**`(` | sd_event_source \*`source`, |
|   | uint64_t `threshold_usec`, |
|   | uint64_t `window_usec``)`; |

 

|                                     |          |
|-------------------------------------|----------|
| `int `**`sd_event_trim_memory`**`(` | void`)`; |

 

## Description

`sd_event_add_memory_pressure()` adds a new event source that is triggered whenever memory pressure is seen. This functionality is built around the Linux kernel's Pressure Stall Information (PSI) logic.

Expects an event loop object as first parameter, and returns the allocated event source object in the second parameter, on success. The *`handler`* parameter is a function to call when memory pressure is seen, or `NULL`. The handler function will be passed the *`userdata`* pointer, which may be chosen freely by the caller. The handler may return negative to signal an error (see below), other return values are ignored. If *`handler`* is `NULL`, a default handler that compacts allocation caches maintained by `libsystemd` as well as glibc (via malloc_trim(3)) will be used.

To destroy an event source object use sd_event_source_unref(3), but note that the event source is only removed from the event loop when all references to the event source are dropped. To make sure an event source does not fire anymore, even if it is still referenced, disable the event source using sd_event_source_set_enabled(3) with `SD_EVENT_OFF`.

If the second parameter of `sd_event_add_memory_pressure()` is `NULL` no reference to the event source object is returned. In this case, the event source is considered "floating", and will be destroyed implicitly when the event loop itself is destroyed.

The event source will fire according to the following logic:

1.  If the `$MEMORY_PRESSURE_WATCH`/`$MEMORY_PRESSURE_WRITE` environment variables are set at the time the event source is established, it will watch the file, FIFO or AF_UNIX socket specified via `$MEMORY_PRESSURE_WATCH` (which must contain an absolute path name) for `POLLPRI` (in case it is a regular file) or `POLLIN` events (otherwise). After opening the inode, it will write the (decoded) Base64 data provided via `$MEMORY_PRESSURE_WRITE` into it before it starts polling on it (the variable may be unset in which case this is skipped). Typically, if used, `$MEMORY_PRESSURE_WATCH` will contain a path such as `/proc/pressure/memory` or a path to a specific `memory.pressure` file in the control group file system (cgroupfs).

2.  If these environment variables are not set, the local PSI interface file `memory.pressure` of the control group the invoking process is running in is used.

3.  If that file does not exist, the system-wide PSI interface file `/proc/pressure/memory` is watched instead.

Or in other words: preferably any explicit configuration passed in by an invoking service manager (or similar) is used as notification source, before falling back to local notifications of the service, and finally to global notifications of the system.

Well-behaving services and applications are recommended to react to memory pressure events by executing one or more of the following operations, in order to ensure optimal behaviour even on loaded and resource-constrained systems:

- Release allocation caches such as `malloc_trim()` or similar, both implemented in the libraries consumed by the program and in private allocation caches of the program itself.

- Release any other form of in-memory caches that can easily be recovered if needed (e.g. browser caches).

- Terminate idle worker threads or processes, or similar.

- Even exit entirely from the program if it is idle and can be automatically started when needed (for example via socket or bus activation).

Any of the suggested operations should help easing memory pressure situations and allowing the system to make progress by reclaiming the memory for other purposes.

This event source typically fires on memory pressure stalls, i.e. when operational latency above a configured threshold already has been seen. This should be taken into consideration when discussing whether later latency to re-acquire any released resources is acceptable: it is usually more important to think of the latencies that already happened than those coming up in future.

The `sd_event_source_set_memory_pressure_type()` and `sd_event_source_set_memory_pressure_period()` functions can be used to fine-tune the PSI parameters for pressure notifications. The former takes either "`some`", "`full`" as second parameter, the latter takes threshold and period times in microseconds as parameters. For details about these three parameters see the PSI documentation. Note that these two calls must be invoked immediately after allocating the event source, as they must be configured before polling begins. Also note that these calls will fail if memory pressure parameterization has been passed in via the `$MEMORY_PRESSURE_WATCH`/`$MEMORY_PRESSURE_WRITE` environment variables (or in other words: configuration supplied by a service manager wins over internal settings).

The `sd_event_trim_memory()` function releases various internal allocation caches maintained by `libsystemd` and then invokes glibc's malloc_trim(3). This makes the operation executed when the handler function parameter of `sd_event_add_memory_pressure` is passed as `NULL` directly accessible for invocation at any time (see above). This function will log a structured log message at `LOG_DEBUG` level (with message ID f9b0be465ad540d0850ad32172d57c21) about the memory pressure operation.

For further details see Memory Pressure Handling in systemd.

## Return Value

On success, these functions return 0 or a positive integer. On failure, they return a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-ENOMEM`  
Not enough memory to allocate an object.

Added in version 254.

`-EINVAL`  
An invalid argument has been passed.

Added in version 254.

`-EHOSTDOWN`  
The `$MEMORY_PRESSURE_WATCH` variable has been set to the literal string `/dev/null`, in order to explicitly disable memory pressure handling.

Added in version 254.

`-EBADMSG`  
The `$MEMORY_PRESSURE_WATCH` variable has been set to an invalid string, for example a relative rather than an absolute path.

Added in version 254.

`-ENOTTY`  
The `$MEMORY_PRESSURE_WATCH` variable points to a regular file outside of the procfs or cgroupfs file systems.

Added in version 254.

`-EOPNOTSUPP`  
No configuration via `$MEMORY_PRESSURE_WATCH` has been specified and the local kernel does not support the PSI interface.

Added in version 254.

`-EBUSY`  
This is returned by `sd_event_source_set_memory_pressure_type()` and `sd_event_source_set_memory_pressure_period()` if invoked on event sources at a time later than immediately after allocating them.

Added in version 254.

`-ESTALE`  
The event loop is already terminated.

Added in version 254.

`-ECHILD`  
The event loop has been created in a different process, library or module instance.

Added in version 254.

`-EDOM`  
The passed event source is not a signal event source.

Added in version 254.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_event_add_memory_pressure()`, `sd_event_source_set_memory_pressure_type()`, `sd_event_source_set_memory_pressure_period()`, and `sd_event_trim_memory()` were added in version 254.

## See Also

systemd(1), sd-event(3), sd_event_new(3), sd_event_add_io(3), sd_event_add_time(3), sd_event_add_child(3), sd_event_add_inotify(3), sd_event_add_defer(3), sd_event_source_set_enabled(3), sd_event_source_set_description(3), sd_event_source_set_userdata(3), sd_event_source_set_floating(3)
