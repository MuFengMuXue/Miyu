## Name

sd_bus_message_read_basic — Read a basic type from a message

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                          |                       |
|------------------------------------------|-----------------------|
| `int `**`sd_bus_message_read_basic`**`(` | sd_bus_message \*`m`, |
|                                          | char `type`,          |
|                                          | void \*`p``)`;        |

 

## Description

`sd_bus_message_read_basic()` reads a basic type from a message and advances the read position in the message. The set of basic types and their ascii codes passed in *`type`* are described in the D-Bus Specification.

If *`p`* is not `NULL`, it should contain a pointer to an appropriate object. For example, if *`type`* is `'y'`, the object passed in *`p`* should have type uint8_t \*. If *`type`* is `'s'`, the object passed in *`p`* should have type const char \*\*. Note that, if the basic type is a pointer (e.g., const char \* in the case of a string), the pointer is only borrowed and the contents must be copied if they are to be used after the end of the message's lifetime. Similarly, during the lifetime of such a pointer, the message must not be modified. If *`type`* is `'h'` (UNIX file descriptor), the descriptor is not duplicated by this call and the returned descriptor remains in possession of the message object, and needs to be duplicated by the caller in order to keep an open reference to it after the message object is freed (for example by calling "`fcntl(fd, FD_DUPFD_CLOEXEC, 3)`"). See the table below for a complete list of allowed types.

**Table 1. Item type specifiers**

| Specifier | Constant | Description | Expected C Type |
|----|----|----|----|
| "`y`" | `SD_BUS_TYPE_BYTE` | 8-bit unsigned integer | uint8_t \* |
| "`b`" | `SD_BUS_TYPE_BOOLEAN` | boolean | int \* (NB: not bool \*) |
| "`n`" | `SD_BUS_TYPE_INT16` | 16-bit signed integer | int16_t \* |
| "`q`" | `SD_BUS_TYPE_UINT16` | 16-bit unsigned integer | uint16_t \* |
| "`i`" | `SD_BUS_TYPE_INT32` | 32-bit signed integer | int32_t \* |
| "`u`" | `SD_BUS_TYPE_UINT32` | 32-bit unsigned integer | uint32_t \* |
| "`x`" | `SD_BUS_TYPE_INT64` | 64-bit signed integer | int64_t \* |
| "`t`" | `SD_BUS_TYPE_UINT64` | 64-bit unsigned integer | uint64_t \* |
| "`d`" | `SD_BUS_TYPE_DOUBLE` | IEEE 754 double precision floating-point | double \* |
| "`s`" | `SD_BUS_TYPE_STRING` | UTF-8 string | const char \*\* |
| "`o`" | `SD_BUS_TYPE_OBJECT_PATH` | D-Bus object path string | const char \*\* |
| "`g`" | `SD_BUS_TYPE_SIGNATURE` | D-Bus signature string | const char \*\* |
| "`h`" | `SD_BUS_TYPE_UNIX_FD` | UNIX file descriptor | int \* |

  

If there is no object of the specified type at the current position in the message, an error is returned.

## Return Value

On success, `sd_bus_message_read_basic()` returns a positive integer. If the end of the currently opened array has been reached, it returns 0. On failure, it returns a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
Specified type string is invalid or the message parameter is `NULL`.

`-ENXIO`  
The message does not contain the specified type at current position.

`-EBADMSG`  
The message cannot be parsed.

## History

`sd_bus_message_read_basic()` was added in version 221.

## See Also

systemd(1), sd-bus(3), sd_bus_message_append_basic(3), sd_bus_message_skip(3), sd_bus_message_read(3)
