## Name

sd_bus_message_get_type, sd_bus_message_get_error, sd_bus_message_get_errno, sd_bus_message_get_creds, sd_bus_message_is_signal, sd_bus_message_is_method_call, sd_bus_message_is_method_error — Query bus message addressing/credentials metadata

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                        |                       |
|----------------------------------------|-----------------------|
| `int `**`sd_bus_message_get_type`**`(` | sd_bus_message \*`m`, |
|                                        | uint8_t \*`type``)`;  |

 

|  |  |
|----|----|
| `sd_bus_error* `**`sd_bus_message_get_error`**`(` | sd_bus_message \*`m``)`; |

 

|                                         |                          |
|-----------------------------------------|--------------------------|
| `int `**`sd_bus_message_get_errno`**`(` | sd_bus_message \*`m``)`; |

 

|  |  |
|----|----|
| `sd_bus_creds* `**`sd_bus_message_get_creds`**`(` | sd_bus_message \*`m``)`; |

 

|                                         |                           |
|-----------------------------------------|---------------------------|
| `int `**`sd_bus_message_is_signal`**`(` | sd_bus_message \*`m`,     |
|                                         | const char \*`interface`, |
|                                         | const char \*`member``)`; |

 

|                                              |                           |
|----------------------------------------------|---------------------------|
| `int `**`sd_bus_message_is_method_call`**`(` | sd_bus_message \*`m`,     |
|                                              | const char \*`interface`, |
|                                              | const char \*`member``)`; |

 

|                                               |                         |
|-----------------------------------------------|-------------------------|
| `int `**`sd_bus_message_is_method_error`**`(` | sd_bus_message \*`m`,   |
|                                               | const char \*`name``)`; |

 

## Description

`sd_bus_message_get_type()` returns the type of a message in the output parameter *`type`*, one of `SD_BUS_MESSAGE_METHOD_CALL`, `SD_BUS_MESSAGE_METHOD_RETURN`, `SD_BUS_MESSAGE_METHOD_ERROR`, `SD_BUS_MESSAGE_SIGNAL`. This type is either specified as a parameter when the message is created using sd_bus_message_new(3), or is set automatically when the message is created using sd_bus_message_new_signal(3), sd_bus_message_new_method_call(3), sd_bus_message_new_method_error(3) and similar functions.

`sd_bus_message_get_error()` returns the error stored in the message *`m`*, if there is any. Otherwise, it returns `NULL`. `sd_bus_message_get_errno()` returns the error stored in the message *`m`* as a positive errno-style value, if there is any. Otherwise, it returns zero. Errors are mapped to errno values according to the default and any additional registered error mappings. See sd-bus-errors(3) and sd_bus_error_add_map(3).

`sd_bus_message_get_creds()` returns the message credentials attached to the message *`m`*. If no credentials are attached to the message, it returns `NULL`. Ownership of the credentials instance is not transferred to the caller and hence should not be freed.

`sd_bus_message_is_signal()` checks if message *`m`* is a signal message. If *`interface`* is non-null, it also checks if the message has the same interface set. If *`member`* is non-null, it also checks if the message has the same member set. Also see sd_bus_message_new_signal(3). It returns true when all checks pass.

`sd_bus_message_is_method_call()` checks if message *`m`* is a method call message. If *`interface`* is non-null, it also checks if the message has the same interface set. If *`member`* is non-null, it also checks if the message has the same member set. Also see sd_bus_message_new_method_call(3). It returns true when all checks pass.

`sd_bus_message_is_method_error()` checks if message *`m`* is an error reply message. If *`name`* is non-null, it also checks if the message has the same error identifier set. Also see sd_bus_message_new_method_error(3). It returns true when all checks pass.

## Return Value

On success, these functions (except `sd_bus_message_get_error()` and `sd_bus_message_get_creds()`) return a non-negative integer. On failure, they return a negative errno-style error code. `sd_bus_message_get_errno()` always returns a non-negative integer, even on failure.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
The message parameter *`m`* or an output parameter is `NULL`.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_message_get_type()`, `sd_bus_message_is_signal()`, `sd_bus_message_is_method_call()`, and `sd_bus_message_is_method_error()` were added in version 240.

`sd_bus_message_get_error()`, `sd_bus_message_get_errno()`, and `sd_bus_message_get_creds()` were added in version 246.

## See Also

systemd(1), sd-bus(3), sd_bus_message_new(3), sd_bus_message_set_destination(3), sd-bus-errors(3), sd_bus_error_add_map(3)
