## Name

sd_bus_message_append_basic — Attach a single field to a message

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                    |                       |
|------------------------------------|-----------------------|
| `int sd_bus_message_append_basic(` | sd_bus_message \*`m`, |
|                                    | char `type`,          |
|                                    | const void \*`p``)`;  |

 

## Description

`sd_bus_message_append_basic()` appends a single field to the message *`m`*. The parameter *`type`* determines how the pointer *`p`* is interpreted. *`type`* must be one of the basic types as defined by the Basic Types section of the D-Bus specification, and listed in the table below.

**Table 1. Item type specifiers**

| Specifier | Constant | Description | Size | Expected C Type |
|----|----|----|----|----|
| "`y`" | `SD_BUS_TYPE_BYTE` | unsigned integer | 1 byte | uint8_t |
| "`b`" | `SD_BUS_TYPE_BOOLEAN` | boolean | 4 bytes | int |
| "`n`" | `SD_BUS_TYPE_INT16` | signed integer | 2 bytes | int16_t |
| "`q`" | `SD_BUS_TYPE_UINT16` | unsigned integer | 2 bytes | uint16_t |
| "`i`" | `SD_BUS_TYPE_INT32` | signed integer | 4 bytes | int32_t |
| "`u`" | `SD_BUS_TYPE_UINT32` | unsigned integer | 4 bytes | uint32_t |
| "`x`" | `SD_BUS_TYPE_INT64` | signed integer | 8 bytes | int64_t |
| "`t`" | `SD_BUS_TYPE_UINT64` | unsigned integer | 8 bytes | uint64_t |
| "`d`" | `SD_BUS_TYPE_DOUBLE` | floating-point | 8 bytes | double |
| "`s`" | `SD_BUS_TYPE_STRING` | Unicode string | variable | char\[\] |
| "`o`" | `SD_BUS_TYPE_OBJECT_PATH` | object path | variable | char\[\] |
| "`g`" | `SD_BUS_TYPE_SIGNATURE` | signature | variable | char\[\] |
| "`h`" | `SD_BUS_TYPE_UNIX_FD` | UNIX file descriptor | 4 bytes | int |

  

The value of the parameter is copied into a memory area held by the message object, stays in the possession of the caller and may hence be freely changed after this call without affecting the bus message it has been added to. If *`type`* is "`h`" (UNIX file descriptor), the descriptor is duplicated by this call and the passed descriptor stays in possession of the caller.

For types "`s`", "`o`", and "`g`", the parameter *`p`* is interpreted as a pointer to a `NUL`-terminated character sequence. As a special case, a `NULL` pointer is interpreted as an empty string. The string should be valid Unicode string encoded as UTF-8. In case of the two latter types, the additional requirements for a D-Bus object path or type signature should be satisfied. Those requirements should be verified by the recipient of the message.

## Return Value

On success, this call returns 0 or a positive integer. On failure, it returns a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
Specified parameter is invalid.

`-EPERM`  
Message has been sealed.

`-ESTALE`  
Message is in invalid state.

`-ENXIO`  
Message cannot be appended to.

`-ENOMEM`  
Memory allocation failed.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## See Also

systemd(1), sd-bus(3), sd_bus_message_read_basic(3), sd_bus_message_append(3), The D-Bus specification
