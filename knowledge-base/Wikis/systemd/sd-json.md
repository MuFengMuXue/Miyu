## Name

sd-json — APIs for Dealing with JSON Objects

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-json.h>
```

`pkg-config --cflags --libs libsystemd`

## Description

`sd-json.h` is part of libsystemd(3) and provides APIs to parse, generate, format and otherwise operate with JSON objects.

The API's central data structure is JsonVariant which encapsulates a JSON object, array, string, boolean, number or null value. These data structures are mostly considered immutable after construction (i.e. their contents will not change, but some meta-data might, such as reference counters).

The APIs broadly fall into five categories:

- APIs to directly operate with JsonVariant objects, in the `sd_json_variant*` namespace.

- APIs to construct complex JSON objects, in the `sd_json_build*` namespace.

- APIs to map JsonVariant objects and their fields to matching fields in C structures, in the `sd_json_dispatch*` namespace.

- APIs to convert a string representation of a JSON object into a JsonVariant object, in the `sd_json_parse*` namespace.

- APIs to convert an JsonVariant object into its string representation, in the `sd_json_format*` namespace.

This JSON library will internally encode JSON integer numbers in the range `INT64_MIN`…`UINT64_MAX` into native 64bit signed or unsigned integers, and will reproduce them without loss of precision. Non-integer numbers are stored in 64bit IEEE floating point numbers.

If the functions return string arrays, these are generally `NULL` terminated and need to be freed by the caller with the libc free(3) call after use, including the strings referenced therein. Similarly, individual strings returned need to be freed, as well.

As a special exception, instead of an empty string array `NULL` may be returned, which should be treated equivalent to an empty string array.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## See Also

systemd(1), sd-varlink(3), pkg-config(1)
