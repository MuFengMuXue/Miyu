## Name

sd_hwdb_get, sd_hwdb_seek, sd_hwdb_enumerate, SD_HWDB_FOREACH_PROPERTY — Seek to a location in hwdb or access entries

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-hwdb.h>
```

|                            |                            |
|----------------------------|----------------------------|
| `int `**`sd_hwdb_get`**`(` | sd_hwdb \*`hwdb`,          |
|                            | const char \*`modalias`,   |
|                            | const char \*`key`,        |
|                            | const char \*\*`value``)`; |

 

|                             |                             |
|-----------------------------|-----------------------------|
| `int `**`sd_hwdb_seek`**`(` | sd_hwdb \*`hwdb`,           |
|                             | const char \*`modalias``)`; |

 

|                                  |                            |
|----------------------------------|----------------------------|
| `int `**`sd_hwdb_enumerate`**`(` | sd_hwdb \*`hwdb`,          |
|                                  | const char \*\*`key`,      |
|                                  | const char \*\*`value``)`; |

 

|                                   |           |
|-----------------------------------|-----------|
| **`SD_HWDB_FOREACH_PROPERTY`**`(` | hwdb,     |
|                                   | modalias, |
|                                   | key,      |
|                                   | value`)`; |

 

## Description

`sd_hwdb_get()` queries the *`hwdb`* object created earlier with sd_hwdb_new(3) for entries matching the specified string *`modalias`*, and returns the value corresponding to the key *`key`*. The value is returned as a `NUL`-terminated string in *`value`*. It must not be modified by the caller and is valid as long as a reference to *`hwdb`* is kept. When multiple patterns in the database match *`modalias`*, the one with the highest priority is used. See hwdb(7) for details.

`sd_hwdb_seek()` selects entries matching the specified string *`modalias`*. Subsequent queries with `sd_hwdb_enumerate()` will access the key-value pairs for that string.

`sd_hwdb_enumerate()` returns (in turn) all the key-value pairs defined for the string used with `sd_hwdb_seek()`. Each pair is returned as `NUL`-terminated strings in *`key`* and *`value`*. The strings must not be modified by the caller and are valid as long as a reference to *`hwdb`* is kept. When multiple patterns in the database match *`modalias`*, the combination of all matching key-value pairs is used. See hwdb(7) for details.

The `SD_HWDB_FOREACH_PROPERTY()` macro combines `sd_hwdb_seek()` and `sd_hwdb_enumerate()`. No error handling is performed and iteration simply stops on error. See the example below.

## Return Value

On success, `sd_hwdb_get()` and `sd_hwdb_seek()` return a non-negative integer. On failure, they return a negative errno-style error code.

`sd_hwdb_enumerate()` returns a positive integer if another key-value pair was found or zero if all entries have already been enumerated. On failure, it returns a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
A parameter is `NULL`.

Added in version 246.

`-ENOENT`  
An entry for the specified *`modalias`* was not found.

Added in version 246.

`-EAGAIN`  
`sd_hwdb_seek()` was not called before `sd_hwdb_enumerate()`.

Added in version 246.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## Examples

**Example 1. Look up hwdb entries for a USB device**

``` programlisting
/* SPDX-License-Identifier: MIT-0 */

#define _GNU_SOURCE 1
#include <stdio.h>
#include <stdint.h>
#include <systemd/sd-hwdb.h>

int print_usb_properties(uint16_t vid, uint16_t pid) {
  char match[128];
  sd_hwdb *hwdb;
  const char *key, *value;
  int r;

  /* Match this USB vendor and product ID combination */
  snprintf(match, sizeof match, "usb:v%04Xp%04X", vid, pid);

  r = sd_hwdb_new(&hwdb);
  if (r < 0)
    return r;

  SD_HWDB_FOREACH_PROPERTY(hwdb, match, key, value)
    printf("%s: \"%s\" → \"%s\"\n", match, key, value);

  sd_hwdb_unref(hwdb);
  return 0;
}

int main(int argc, char **argv) {
  print_usb_properties(0x046D, 0xC534);
  return 0;
}
```

The effect is similar to calling **systemd-hwdb query usb:v046DpC534**.

  

## History

`sd_hwdb_get()`, `sd_hwdb_seek()`, `sd_hwdb_enumerate()`, and `SD_HWDB_FOREACH_PROPERTY()` were added in version 246.

## See Also

systemd(1), systemd-udevd.service(8), sd-hwdb(3), systemd-hwdb(8)
