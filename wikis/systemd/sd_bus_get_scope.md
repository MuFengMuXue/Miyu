## Name

sd_bus_set_description, sd_bus_get_description, sd_bus_set_anonymous, sd_bus_is_anonymous, sd_bus_set_trusted, sd_bus_is_trusted, sd_bus_set_allow_interactive_authorization, sd_bus_get_allow_interactive_authorization, sd_bus_get_scope, sd_bus_get_tid, sd_bus_get_unique_name — Set or query properties of a bus object

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                       |                                |
|---------------------------------------|--------------------------------|
| `int `**`sd_bus_set_description`**`(` | sd_bus \*`bus`,                |
|                                       | const char \*`description``)`; |

 

|                                       |                                  |
|---------------------------------------|----------------------------------|
| `int `**`sd_bus_get_description`**`(` | sd_bus \*`bus`,                  |
|                                       | const char \*\*`description``)`; |

 

|                                     |                 |
|-------------------------------------|-----------------|
| `int `**`sd_bus_set_anonymous`**`(` | sd_bus \*`bus`, |
|                                     | int `b``)`;     |

 

|                                    |                    |
|------------------------------------|--------------------|
| `int `**`sd_bus_is_anonymous`**`(` | sd_bus \*`bus``)`; |

 

|                                   |                 |
|-----------------------------------|-----------------|
| `int `**`sd_bus_set_trusted`**`(` | sd_bus \*`bus`, |
|                                   | int `b``)`;     |

 

|                                  |                    |
|----------------------------------|--------------------|
| `int `**`sd_bus_is_trusted`**`(` | sd_bus \*`bus``)`; |

 

|                                                           |                 |
|-----------------------------------------------------------|-----------------|
| `int `**`sd_bus_set_allow_interactive_authorization`**`(` | sd_bus \*`bus`, |
|                                                           | int `b``)`;     |

 

|  |  |
|----|----|
| `int `**`sd_bus_get_allow_interactive_authorization`**`(` | sd_bus \*`bus``)`; |

 

|                                 |                            |
|---------------------------------|----------------------------|
| `int `**`sd_bus_get_scope`**`(` | sd_bus \*`bus`,            |
|                                 | const char \*\*`scope``)`; |

 

|                               |                   |
|-------------------------------|-------------------|
| `int `**`sd_bus_get_tid`**`(` | sd_bus \*`bus`,   |
|                               | pid_t \*`tid``)`; |

 

|                                       |                             |
|---------------------------------------|-----------------------------|
| `int `**`sd_bus_get_unique_name`**`(` | sd_bus \*`bus`,             |
|                                       | const char \*\*`unique``)`; |

 

## Description

`sd_bus_set_description()` sets the description string that is used in logging to the specified string. The string is copied internally and freed when the bus object is deallocated. The *`description`* argument may be `NULL`, in which case the description is unset. This function must be called before the bus is started.

`sd_bus_get_description()` returns a description string in *`description`*. This string may have been previously set with `sd_bus_set_description()` or sd_bus_open_with_description(3) or similar. If not set this way, a default string like "`system`" or "`user`" will be returned for the system or user buses, and `-ENXIO` otherwise.

`sd_bus_set_anonymous()` enables or disables "anonymous authentication", i.e. lack of authentication, of the bus peer. This function must be called before the bus is started. See the D-Bus Authentication Mechanisms section of the D-Bus specification for details.

`sd_bus_is_anonymous()` returns true if the bus connection allows anonymous authentication (in the sense described in previous paragraph).

`sd_bus_set_trusted()` sets the "trusted" state on the *`bus`* object. If true, all connections on the bus are trusted and access to all privileged and unprivileged methods is granted. This function must be called before the bus is started.

`sd_bus_is_trusted()` returns true if the bus connection is trusted (in the sense described in previous paragraph).

`sd_bus_set_allow_interactive_authorization()` enables or disables interactive authorization for method calls. If true, messages are marked with the `ALLOW_INTERACTIVE_AUTHORIZATION` flag specified by the D-Bus specification, informing the receiving side that the caller is prepared to wait for interactive authorization, which might take a considerable time to complete. If this flag is set, the user may be queried for passwords or confirmation via polkit or a similar framework.

`sd_bus_get_allow_interactive_authorization()` returns true if interactive authorization is allowed and false if not.

`sd_bus_get_scope()` stores the scope of the given bus object in *`scope`*. The scope of the system bus is "`system`". The scope of a user session bus is "`user`". If the given bus object is not the system or a user session bus, `sd_bus_get_scope()` returns an error.

`sd_bus_get_tid()` stores the kernel thread id of the thread associated with the given bus object in *`tid`*. If *`bus`* is a default bus object obtained by calling one of the functions of the sd_bus_default(3) family of functions, it stores the thread id of the thread the bus object was created in. Otherwise, if the bus object is attached to an event loop, it stores the thread id of the thread the event loop object was created in. If *`bus`* is not a default bus object and is not attached to an event loop, `sd_bus_get_tid()` returns an error.

`sd_bus_get_unique_name()` stores the unique name of the bus object on the bus in *`unique`*. See The D-Bus specification for more information on bus names. Note that the caller does not own the string stored in *`unique`* and should not free it.

## Return Value

On success, these functions return a non-negative integer. On failure, they return a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
An argument is invalid.

`-ENOPKG`  
The bus cannot be resolved.

`-EPERM`  
The bus has already been started.

`-ECHILD`  
The bus was created in a different process, library or module instance.

`-ENOMEM`  
Memory allocation failed.

`-ENODATA`  
The bus object passed to `sd_bus_get_scope()` was not a system or user session bus.

Added in version 246.

`-ENXIO`  
The bus object passed to `sd_bus_get_tid()` was not a default bus object and is not attached to an event loop.

The bus object passed to `sd_bus_get_description()` did not have a *`description`*.

Added in version 246.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_set_description()`, `sd_bus_get_description()`, `sd_bus_set_anonymous()`, `sd_bus_set_trusted()`, `sd_bus_set_allow_interactive_authorization()`, and `sd_bus_get_allow_interactive_authorization()` were added in version 240.

`sd_bus_is_anonymous()`, `sd_bus_is_trusted()`, `sd_bus_get_scope()`, `sd_bus_get_tid()`, and `sd_bus_get_unique_name()` were added in version 246.

## See Also

systemd(1), sd-bus(3), sd_bus_default_user(3), sd_bus_default_system(3), sd_bus_open_user(3), sd_bus_open_system(3)
