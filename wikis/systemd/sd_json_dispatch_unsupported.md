## Name

sd_json_dispatch_string, sd_json_dispatch_const_string, sd_json_dispatch_strv, sd_json_dispatch_stdbool, sd_json_dispatch_intbool, sd_json_dispatch_tristate, sd_json_dispatch_variant, sd_json_dispatch_variant_noref, sd_json_dispatch_int64, sd_json_dispatch_int32, sd_json_dispatch_int16, sd_json_dispatch_int8, sd_json_dispatch_uint64, sd_json_dispatch_uint32, sd_json_dispatch_uint16, sd_json_dispatch_uint8, sd_json_dispatch_double, sd_json_dispatch_uid_gid, sd_json_dispatch_id128, sd_json_dispatch_signal, sd_json_dispatch_unsupported — Decode JSON variant values and write them to the specified memory

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-varlink.h>
```

|                                        |                              |
|----------------------------------------|------------------------------|
| `int `**`sd_json_dispatch_string`**`(` | const char \*`name`,         |
|                                        | sd_json_variant \*`variant`, |
|                                        | sd_dispatch_flags `flags`,   |
|                                        | void \*`userdata``)`;        |

 

|                                              |                              |
|----------------------------------------------|------------------------------|
| `int `**`sd_json_dispatch_const_string`**`(` | const char \*`name`,         |
|                                              | sd_json_variant \*`variant`, |
|                                              | sd_dispatch_flags `flags`,   |
|                                              | void \*`userdata``)`;        |

 

|                                      |                              |
|--------------------------------------|------------------------------|
| `int `**`sd_json_dispatch_strv`**`(` | const char \*`name`,         |
|                                      | sd_json_variant \*`variant`, |
|                                      | sd_dispatch_flags `flags`,   |
|                                      | void \*`userdata``)`;        |

 

|                                         |                              |
|-----------------------------------------|------------------------------|
| `int `**`sd_json_dispatch_stdbool`**`(` | const char \*`name`,         |
|                                         | sd_json_variant \*`variant`, |
|                                         | sd_dispatch_flags `flags`,   |
|                                         | void \*`userdata``)`;        |

 

|                                         |                              |
|-----------------------------------------|------------------------------|
| `int `**`sd_json_dispatch_intbool`**`(` | const char \*`name`,         |
|                                         | sd_json_variant \*`variant`, |
|                                         | sd_dispatch_flags `flags`,   |
|                                         | void \*`userdata``)`;        |

 

|                                          |                              |
|------------------------------------------|------------------------------|
| `int `**`sd_json_dispatch_tristate`**`(` | const char \*`name`,         |
|                                          | sd_json_variant \*`variant`, |
|                                          | sd_dispatch_flags `flags`,   |
|                                          | void \*`userdata``)`;        |

 

|                                         |                              |
|-----------------------------------------|------------------------------|
| `int `**`sd_json_dispatch_variant`**`(` | const char \*`name`,         |
|                                         | sd_json_variant \*`variant`, |
|                                         | sd_dispatch_flags `flags`,   |
|                                         | void \*`userdata``)`;        |

 

|  |  |
|----|----|
| `int `**`sd_json_dispatch_variant_noref`**`(` | const char \*`name`, |
|   | sd_json_variant \*`variant`, |
|   | sd_dispatch_flags `flags`, |
|   | void \*`userdata``)`; |

 

|                                       |                              |
|---------------------------------------|------------------------------|
| `int `**`sd_json_dispatch_int64`**`(` | const char \*`name`,         |
|                                       | sd_json_variant \*`variant`, |
|                                       | sd_dispatch_flags `flags`,   |
|                                       | void \*`userdata``)`;        |

 

|                                       |                              |
|---------------------------------------|------------------------------|
| `int `**`sd_json_dispatch_int32`**`(` | const char \*`name`,         |
|                                       | sd_json_variant \*`variant`, |
|                                       | sd_dispatch_flags `flags`,   |
|                                       | void \*`userdata``)`;        |

 

|                                       |                              |
|---------------------------------------|------------------------------|
| `int `**`sd_json_dispatch_int16`**`(` | const char \*`name`,         |
|                                       | sd_json_variant \*`variant`, |
|                                       | sd_dispatch_flags `flags`,   |
|                                       | void \*`userdata``)`;        |

 

|                                      |                              |
|--------------------------------------|------------------------------|
| `int `**`sd_json_dispatch_int8`**`(` | const char \*`name`,         |
|                                      | sd_json_variant \*`variant`, |
|                                      | sd_dispatch_flags `flags`,   |
|                                      | void \*`userdata``)`;        |

 

|                                        |                              |
|----------------------------------------|------------------------------|
| `int `**`sd_json_dispatch_uint64`**`(` | const char \*`name`,         |
|                                        | sd_json_variant \*`variant`, |
|                                        | sd_dispatch_flags `flags`,   |
|                                        | void \*`userdata``)`;        |

 

|                                        |                              |
|----------------------------------------|------------------------------|
| `int `**`sd_json_dispatch_uint32`**`(` | const char \*`name`,         |
|                                        | sd_json_variant \*`variant`, |
|                                        | sd_dispatch_flags `flags`,   |
|                                        | void \*`userdata``)`;        |

 

|                                        |                              |
|----------------------------------------|------------------------------|
| `int `**`sd_json_dispatch_uint16`**`(` | const char \*`name`,         |
|                                        | sd_json_variant \*`variant`, |
|                                        | sd_dispatch_flags `flags`,   |
|                                        | void \*`userdata``)`;        |

 

|                                       |                              |
|---------------------------------------|------------------------------|
| `int `**`sd_json_dispatch_uint8`**`(` | const char \*`name`,         |
|                                       | sd_json_variant \*`variant`, |
|                                       | sd_dispatch_flags `flags`,   |
|                                       | void \*`userdata``)`;        |

 

|                                        |                              |
|----------------------------------------|------------------------------|
| `int `**`sd_json_dispatch_double`**`(` | const char \*`name`,         |
|                                        | sd_json_variant \*`variant`, |
|                                        | sd_dispatch_flags `flags`,   |
|                                        | void \*`userdata``)`;        |

 

|                                         |                              |
|-----------------------------------------|------------------------------|
| `int `**`sd_json_dispatch_uid_gid`**`(` | const char \*`name`,         |
|                                         | sd_json_variant \*`variant`, |
|                                         | sd_dispatch_flags `flags`,   |
|                                         | void \*`userdata``)`;        |

 

|                                       |                              |
|---------------------------------------|------------------------------|
| `int `**`sd_json_dispatch_id128`**`(` | const char \*`name`,         |
|                                       | sd_json_variant \*`variant`, |
|                                       | sd_dispatch_flags `flags`,   |
|                                       | void \*`userdata``)`;        |

 

|                                        |                              |
|----------------------------------------|------------------------------|
| `int `**`sd_json_dispatch_signal`**`(` | const char \*`name`,         |
|                                        | sd_json_variant \*`variant`, |
|                                        | sd_dispatch_flags `flags`,   |
|                                        | void \*`userdata``)`;        |

 

|                                             |                              |
|---------------------------------------------|------------------------------|
| `int `**`sd_json_dispatch_unsupported`**`(` | const char \*`name`,         |
|                                             | sd_json_variant \*`variant`, |
|                                             | sd_dispatch_flags `flags`,   |
|                                             | void \*`userdata``)`;        |

 

## Description

The various functions described here are intended for use in the sd_json_dispatch_field structure arrays the sd_json_dispatch(3) and sd_varlink_dispatch(3) functions accept; they decode the provided JSON variant object's value, and write it to the memory indicated by the *`userdata`* pointer. The *`name`* parameter contains the field name (in the JSON object it is contained in) of the value being decoded. For details on the *`flags`* parameter see the `sd_json_dispatch()` documentation.

Note that all these functions not only accept the native JSON type they are intended for, but also accept null JSON values, in which case they assign an appropriate invalid/unset/null value, as appropriate for the type (for details see below).

`sd_json_dispatch_string()` decodes a JSON string value, and allocates a `NUL` terminated copy in dynamic memory. The *`userdata`* pointer must point to a pointer to a string, which is freed if non-`NULL`, and then replaced by the newly allocated one. If a JSON null value is passed, the existing string is freed and `NULL` is assigned.

`sd_json_dispatch_const_string()` is very similar to `sd_json_dispatch_string()`, but does not allocate a string in dynamic memory. Instead, it just writes a pointer into the JSON object into the indicated memory (or `NULL` in case a JSON null object is passed). The memory remains valid only as long as the indicated variant object is kept allocated (which can happen via direct reference, or via an indirect one via an object that references the specified variant). The memory *`userdata`* points to on input is *not* freed before the new value is assigned.

`sd_json_dispatch_stdbool()` and `sd_json_dispatch_intbool()` decode JSON boolean values and write them to the indicated memory. The former expects a variable of the C99 bool type in the indicated memory, the latter an int (which will only receive the values 0 and 1). The JSON null value is treated equivalent to a JSON false.

`sd_json_dispatch_tristate()` is very similar to`sd_json_dispatch_intbool()`, but will assign -1 if a JSON null value is passed. Or in other words, the integer will have a value \> 0, == 0 or \< 0, for the cases true, false or invalid/unset/null.

`sd_json_dispatch_variant()` takes an additional reference to the passed JSON object (via `sd_json_variant_ref()`) and writes the pointer to the indicated memory. No decoding is done. If the indicated pointer is non-`NULL` on input it is freed (via `sd_json_variant_unref()`) before the new pointer is written.

`sd_json_dispatch_variant_noref()` is similar, but does *not* take a new reference to the JSON variant object. The pointer hence only remains valid as long as the original object stays referenced. If the indicated pointer is non-`NULL` on input it is *not* freed before the new pointer is written.

The `sd_json_dispatch_int64()`, `sd_json_dispatch_int32()`, `sd_json_dispatch_int16()`, `sd_json_dispatch_int8()`, `sd_json_dispatch_uint64()`, `sd_json_dispatch_uint32()`, `sd_json_dispatch_uint16()` and `sd_json_dispatch_uint8()` functions decode a JSON integer value, and write the value to the indicated memory. The function names indicate the word width and signedness of the integers being parsed. If the JSON null value is passed the functions for the unsigned integer types will assign the maximum value the type takes (i.e. `UINT64_MAX`, `UINT32_MAX` …), and the signed versions assign -1. Instead of a JSON integer value these functions also accept JSON strings that contain formatted decimal numbers, in order to improve compatibility for encoding integer values that cannot be represented in 64bit double precision floating point numbers in other programming languages that encode JSON numerals this way.

The `sd_json_dispatch_double()` function decodes a 64bit double precision floating point number. If a JSON null value is passed, assigns NaN.

The `sd_json_dispatch_uid_gid()` function is similar to `sd_json_dispatch_uint32()`, and is intended to decode 32bit UNIX UID/GID numbers, as used on Linux. It will decode a JSON null value as 4294967295 (i.e. "`(uid_t) -1`"), and will refuse the values 65535 and 4294967295 when passed as JSON numerals (i.e. both the 16bit and 32bit "invalid" UID/GID, as these values have special meaning for various UNIX syscalls, on different OSes and file systems).

`sd_json_dispatch_id128()` decodes a 128bit ID formatted as a JSON string. It supports both RFC9562 UUID formatting, as well as 64 hexadecimal characters without separators, the same way as sd_id128_from_string(3). If the JSON null value is passed, the all-zero ID is assigned.

`sd_json_dispatch_signal()` decodes a UNIX process signal specification. It expects either an JSON string containing a signal name such as "`SIGINT`" or "`SIGTERM`", or an unsigned JSON integer value with the signal number (in the Linux definition). The indicated memory must point to an int variable to write the signal number to. If the JSON null value is passed a negative value will be written to the memory.

`sd_json_dispatch_unsupported()` will always fail with the -`EINVAL` error.

## Return Value

On success, these functions return a non-negative integer. On failure, they return a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
An argument is invalid.

`-ENOMEM`  
Memory allocation failed.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_json_dispatch_string()`, `sd_json_dispatch_const_string()`, `sd_json_dispatch_strv()`, `sd_json_dispatch_stdbool()`, `sd_json_dispatch_intbool()`, `sd_json_dispatch_tristate()`, `sd_json_dispatch_variant()`, `sd_json_dispatch_variant_noref()`, `sd_json_dispatch_int64()`, `sd_json_dispatch_int32()`, `sd_json_dispatch_int16()`, `sd_json_dispatch_int8()`, `sd_json_dispatch_uint64()`, `sd_json_dispatch_uint32()`, `sd_json_dispatch_uint16()`, `sd_json_dispatch_uint8()`, `sd_json_dispatch_double()`, `sd_json_dispatch_uid_gid()`, `sd_json_dispatch_id128()`, `sd_json_dispatch_signal()`, `sd_json_dispatch_unsupported()` were added in version 257.

## See Also

systemd(1), sd-json(3), sd-varlink(3), sd_json_dispatch(3), sd_variant_dispatch(3)
