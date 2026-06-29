## Name

sd_bus_set_property, sd_bus_set_propertyv, sd_bus_get_property, sd_bus_get_property_trivial, sd_bus_get_property_string, sd_bus_get_property_strv — Set or query D-Bus service properties

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                    |                             |
|------------------------------------|-----------------------------|
| `int `**`sd_bus_set_property`**`(` | sd_bus \*`bus`,             |
|                                    | const char \*`destination`, |
|                                    | const char \*`path`,        |
|                                    | const char \*`interface`,   |
|                                    | const char \*`member`,      |
|                                    | sd_bus_error \*`ret_error`, |
|                                    | const char \*`type`,        |
|                                    | ...`)`;                     |

 

|                                     |                             |
|-------------------------------------|-----------------------------|
| `int `**`sd_bus_set_propertyv`**`(` | sd_bus \*`bus`,             |
|                                     | const char \*`destination`, |
|                                     | const char \*`path`,        |
|                                     | const char \*`interface`,   |
|                                     | const char \*`member`,      |
|                                     | sd_bus_error \*`ret_error`, |
|                                     | const char \*`type`,        |
|                                     | va_list `ap``)`;            |

 

|                                    |                             |
|------------------------------------|-----------------------------|
| `int `**`sd_bus_get_property`**`(` | sd_bus \*`bus`,             |
|                                    | const char \*`destination`, |
|                                    | const char \*`path`,        |
|                                    | const char \*`interface`,   |
|                                    | const char \*`member`,      |
|                                    | sd_bus_error \*`ret_error`, |
|                                    | sd_bus_message \*\*`reply`, |
|                                    | const char \*`type``)`;     |

 

|                                            |                             |
|--------------------------------------------|-----------------------------|
| `int `**`sd_bus_get_property_trivial`**`(` | sd_bus \*`bus`,             |
|                                            | const char \*`destination`, |
|                                            | const char \*`path`,        |
|                                            | const char \*`interface`,   |
|                                            | const char \*`member`,      |
|                                            | sd_bus_error \*`ret_error`, |
|                                            | char `type`,                |
|                                            | void \*`ret_ptr``)`;        |

 

|                                           |                             |
|-------------------------------------------|-----------------------------|
| `int `**`sd_bus_get_property_string`**`(` | sd_bus \*`bus`,             |
|                                           | const char \*`destination`, |
|                                           | const char \*`path`,        |
|                                           | const char \*`interface`,   |
|                                           | const char \*`member`,      |
|                                           | sd_bus_error \*`ret_error`, |
|                                           | char \*\*`ret``)`;          |

 

|                                         |                             |
|-----------------------------------------|-----------------------------|
| `int `**`sd_bus_get_property_strv`**`(` | sd_bus \*`bus`,             |
|                                         | const char \*`destination`, |
|                                         | const char \*`path`,        |
|                                         | const char \*`interface`,   |
|                                         | const char \*`member`,      |
|                                         | sd_bus_error \*`ret_error`, |
|                                         | char \*\*\*`ret``)`;        |

 

## Description

These functions set or query D-Bus properties. D-Bus properties are service fields exposed via the `org.freedesktop.DBus.Properties` interface. Under the hood, these functions call methods of the `org.freedesktop.DBus.Properties` interface and as a result their semantics are similar to sd_bus_call_method(3).

`sd_bus_set_property()` sets a D-Bus property. If setting the property fails or an internal error occurs, an error is returned and an extended description of the error is optionally stored in *`ret_error`* if it is not `NULL`. *`type`* and the arguments that follow it describe the new value of the property and must follow the format described in sd_bus_message_append(3).

`sd_bus_set_propertyv()` is equivalent to `sd_bus_set_property()`, except that it is called with a "`va_list`" instead of a variable number of arguments.

`sd_bus_get_property()` queries a D-Bus property. If retrieving the property fails or an internal error occurs, an error is returned and an extended description of the error is optionally stored in *`ret_error`* if it is not `NULL`. On success, the property is stored in *`reply`*. *`type`* describes the property type and must follow the format described in sd_bus_message_append(3).

`sd_bus_get_property_trivial()`, `sd_bus_get_property_string()` and `sd_bus_get_property_strv()` are shorthands for `sd_bus_get_property()` that are used to query basic, string and string vector properties respectively. The caller is responsible for freeing the string and string vector results stored in *`ret`* by `sd_bus_get_property_string()` and `sd_bus_get_property_strv()`.

## Return Value

On success, these functions return a non-negative integer. On failure, they return a negative errno-style error code.

### Errors

See the sd_bus_call_method(3) man page for a list of possible errors.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_set_property()`, `sd_bus_set_propertyv()`, `sd_bus_get_property()`, `sd_bus_get_property_trivial()`, `sd_bus_get_property_string()`, and `sd_bus_get_property_strv()` were added in version 246.

## See Also

systemd(1), sd-bus(3), sd_bus_call_method(3)
