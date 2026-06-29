## Name

sd_bus_message_read_strv, sd_bus_message_read_strv_extend — Access an array of strings in a message

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                         |                       |
|-----------------------------------------|-----------------------|
| `int `**`sd_bus_message_read_strv`**`(` | sd_bus_message \*`m`, |
|                                         | char \*\*\*`l``)`;    |

 

|                                                |                       |
|------------------------------------------------|-----------------------|
| `int `**`sd_bus_message_read_strv_extend`**`(` | sd_bus_message \*`m`, |
|                                                | char \*\*\*`l``)`;    |

 

## Description

`sd_bus_message_read_strv()` reads an array of string-like items from the message *`m`*. The "read pointer" in the message must be right before an array of strings (D-Bus type "`as`"), object paths (D-Bus type "`ao`"), or signatures (D-Bus type "`ag`"). On success, a pointer to a `NULL`-terminated array of strings (strv) is returned in the output parameter *`l`*. Note that ownership of this array is transferred to the caller. Hence, the caller is responsible for freeing this array and its contents. Also note that as a matter of optimization, if an empty array is encountered a `NULL` pointer might be returned here, and should be considered equivalent to an array with zero entries.

`sd_bus_message_read_strv_extend()` is similar, but the second parameter is an input-output parameter. If *`*l`* is `NULL`, if behaves identically to `sd_bus_message_read_strv()`. Otherwise, *`*l`* must point to a strv, which will be reallocated and extended with additional strings. This function is particularly useful when combining multiple lists of strings in a message or messages into a single array of strings.

## Return Value

On success, these functions return a non-negative integer. On failure, they return a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
*`m`* or *`l`* are `NULL`.

Added in version 246.

`-EPERM`  
The message is not sealed.

Added in version 246.

`-EBADMSG`  
The message cannot be parsed.

Added in version 246.

`-ENXIO`  
The message "read pointer" is not right before an array of the appropriate type.

Added in version 248.

## History

`sd_bus_message_read_strv()` was added in version 246.

`sd_bus_message_read_strv_extend()` was added in version 252.

## See Also

systemd(1), sd-bus(3), sd_bus_message_read(3)
