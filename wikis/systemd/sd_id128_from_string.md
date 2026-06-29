## Name

sd_id128_to_string, SD_ID128_TO_STRING, SD_ID128_STRING_MAX, sd_id128_to_uuid_string, SD_ID128_TO_UUID_STRING, SD_ID128_UUID_STRING_MAX, sd_id128_from_string — Format or parse 128-bit IDs as strings

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-id128.h>
```

``` funcsynopsisinfo
#define SD_ID128_STRING_MAX 33U
```

``` funcsynopsisinfo
#define SD_ID128_UUID_STRING_MAX 37U
```

``` funcsynopsisinfo
#define SD_ID128_TO_STRING(id) …
```

``` funcsynopsisinfo
#define SD_ID128_TO_UUID_STRING(id) …
```

|  |  |
|----|----|
| `char *`**`sd_id128_to_string`**`(` | sd_id128_t `id`, char `s`\[static SD_ID128_STRING_MAX\]`)`; |

 

|  |  |
|----|----|
| `char *`**`sd_id128_to_uuid_string`**`(` | sd_id128_t `id`, char `s`\[static SD_ID128_UUID_STRING_MAX\]`)`; |

 

|  |  |
|----|----|
| `int `**`sd_id128_from_string`**`(` | const char \*`s`, sd_id128_t \*`ret``)`; |

 

## Description

`sd_id128_to_string()` formats a 128-bit ID as a character string. It expects the ID and a string array capable of storing 33 characters (`SD_ID128_STRING_MAX`). The ID will be formatted as 32 lowercase hexadecimal digits and be terminated by a `NUL` byte.

`SD_ID128_TO_STRING()` is a macro that wraps `sd_id128_to_string()` and passes an appropriately sized buffer as second argument, allocated as C99 compound literal. Each use will thus implicitly acquire a suitable buffer on the stack which remains valid until the end of the current code block. This is usually the simplest way to acquire a string representation of a 128-bit ID in a buffer that is valid in the current code block.

`sd_id128_to_uuid_string()` and `SD_ID128_TO_UUID_STRING()` are similar to these two functions/macros, but format the 128-bit values as RFC4122 UUIDs, i.e. a series of 36 lowercase hexadeciaml digits and dashes, terminated by a `NUL` byte.

`sd_id128_from_string()` implements the reverse operation: it takes a 33 character string with 32 hexadecimal digits (either lowercase or uppercase, terminated by `NUL`) and parses them back into a 128-bit ID returned in *`ret`*. Alternatively, this call can also parse a 37-character string with a 128-bit ID formatted as RFC UUID. If *`ret`* is passed as `NULL` the function will validate the passed ID string, but not actually return it in parsed form.

Note that when formatting and parsing 36 character UUIDs this is done strictly in Big Endian byte order, i.e. according to RFC4122 Variant 1 rules, even if the UUID encodes a different variant. This matches behaviour in various other Linux userspace tools. It's probably wise to avoid UUIDs of other variant types.

For more information about the "`sd_id128_t`" type see sd-id128(3). Note that these calls operate the same way on all architectures, i.e. the results do not depend on endianness.

When formatting a 128-bit ID into a string, it is often easier to use a format string for printf(3). This is easily done using the `SD_ID128_FORMAT_STR` and `SD_ID128_FORMAT_VAL()` macros. For more information see sd-id128(3).

## Return Value

`sd_id128_to_string()` always succeeds and returns a pointer to the string array passed in. `sd_id128_from_string()` returns 0 on success, in which case *`ret`* is filled in, or a negative errno-style error code.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_id128_to_string()` and `sd_id128_from_string()` were added in version 187.

`sd_id128_to_uuid_string()` was added in version 251.

## See Also

systemd(1), sd-id128(3), printf(3)
