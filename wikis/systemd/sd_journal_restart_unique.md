## Name

sd_journal_query_unique, sd_journal_enumerate_unique, sd_journal_enumerate_available_unique, sd_journal_restart_unique, SD_JOURNAL_FOREACH_UNIQUE — Read unique data fields from the journal

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-journal.h>
```

|                                        |                          |
|----------------------------------------|--------------------------|
| `int `**`sd_journal_query_unique`**`(` | sd_journal \*`j`,        |
|                                        | const char \*`field``)`; |

 

|  |  |
|----|----|
| `int `**`sd_journal_enumerate_available_unique`**`(` | sd_journal \*`j`, |
|   | const void \*\*`data`, |
|   | size_t \*`length``)`; |

 

|                                            |                        |
|--------------------------------------------|------------------------|
| `int `**`sd_journal_enumerate_unique`**`(` | sd_journal \*`j`,      |
|                                            | const void \*\*`data`, |
|                                            | size_t \*`length``)`;  |

 

|                                           |                      |
|-------------------------------------------|----------------------|
| `void `**`sd_journal_restart_unique`**`(` | sd_journal \*`j``)`; |

 

|                                    |                      |
|------------------------------------|----------------------|
| **`SD_JOURNAL_FOREACH_UNIQUE`**`(` | sd_journal \*`j`,    |
|                                    | const void \*`data`, |
|                                    | size_t `length``)`;  |

 

## Description

`sd_journal_query_unique()` queries the journal for all unique values the specified field can take. It takes two arguments: the journal to query and the field name to look for. Well-known field names are listed on systemd.journal-fields(7), but any field can be specified. Field names must be specified without a trailing "`=`". After this function has been executed successfully the field values may be queried using `sd_journal_enumerate_unique()` and `sd_journal_enumerate_available_unique()`. Invoking one of those calls will change the field name being queried and reset the enumeration index to the first field value that matches.

`sd_journal_enumerate_unique()` may be used to iterate through all data fields which match the previously selected field name as set with `sd_journal_query_unique()`. On each invocation the next field data matching the field name is returned. The order of the returned data fields is not defined. It takes three arguments: the journal object, plus a pair of pointers to pointer/size variables where the data object and its size shall be stored. The returned data is in a read-only memory map and is only valid until the next invocation of `sd_journal_enumerate_unique()`. Note that the data returned will be prefixed with the field name and "`=`". Note that this call is subject to the data field size threshold as controlled by `sd_journal_set_data_threshold()` and only the initial part of the field up to the threshold is returned. An error is returned for fields which cannot be retrieved. See the error list below for details.

`sd_journal_enumerate_available_unique()` is similar to `sd_journal_enumerate_unique()`, but silently skips any fields which may be valid, but are too large or not supported by current implementation.

`sd_journal_restart_unique()` resets the data enumeration index to the beginning of the list. The next invocation of `sd_journal_enumerate_unique()` will return the first field data matching the field name again.

Note that the `SD_JOURNAL_FOREACH_UNIQUE()` macro may be used as a handy wrapper around `sd_journal_restart_unique()` and `sd_journal_enumerate_available_unique()`.

Note that these functions currently are not influenced by matches set with `sd_journal_add_match()` but this might change in a later version of this software.

To enumerate all field names currently in use (and thus all suitable field parameters for `sd_journal_query_unique()`), use the sd_journal_enumerate_fields(3) call.

## Return Value

`sd_journal_query_unique()` returns 0 on success or a negative errno-style error code. `sd_journal_enumerate_unique()` and `sd_journal_query_available_unique()` return a positive integer if the next field data has been read, 0 when no more fields remain, or a negative errno-style error code. `sd_journal_restart_unique()` does not return anything.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
One of the required parameters is `NULL` or invalid.

Added in version 246.

`-ECHILD`  
The journal object was created in a different process, library or module instance.

Added in version 246.

`-EADDRNOTAVAIL`  
The read pointer is not positioned at a valid entry; sd_journal_next(3) or a related call has not been called at least once.

Added in version 246.

`-ENOENT`  
The current entry does not include the specified field.

Added in version 246.

`-ENOBUFS`  
A compressed entry is too large.

Added in version 246.

`-E2BIG`  
The data field is too large for this computer architecture (e.g. above 4 GB on a 32-bit architecture).

Added in version 246.

`-EPROTONOSUPPORT`  
The journal is compressed with an unsupported method or the journal uses an unsupported feature.

Added in version 246.

`-EBADMSG`  
The journal is corrupted (possibly just the entry being iterated over).

Added in version 246.

`-EIO`  
An I/O error was reported by the kernel.

Added in version 246.

## Notes

All functions listed here are thread-agnostic and only a single thread may operate on a given object at any given time. Different threads may access the same object at different times. Multiple independent objects may be used from different threads in parallel.

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

## Examples

Use the `SD_JOURNAL_FOREACH_UNIQUE()` macro to iterate through all values a field of the journal can take (and which can be accessed on the given architecture and are not compressed with an unsupported mechanism). The following example lists all unit names referenced in the journal:

``` programlisting
/* SPDX-License-Identifier: MIT-0 */

#include <errno.h>
#include <stdio.h>
#include <systemd/sd-journal.h>

int main(int argc, char *argv[]) {
  sd_journal *j;
  const void *d;
  size_t l;
  int r;

  r = sd_journal_open(&j, SD_JOURNAL_LOCAL_ONLY);
  if (r < 0) {
    fprintf(stderr, "Failed to open journal: %s\n", strerror(-r));
    return 1;
  }
  r = sd_journal_query_unique(j, "_SYSTEMD_UNIT");
  if (r < 0) {
    fprintf(stderr, "Failed to query journal: %s\n", strerror(-r));
    return 1;
  }
  SD_JOURNAL_FOREACH_UNIQUE(j, d, l)
    printf("%.*s\n", (int) l, (const char*) d);
  sd_journal_close(j);
  return 0;
}
```

## History

`sd_journal_query_unique()`, `sd_journal_enumerate_unique()`, `sd_journal_restart_unique()`, and `SD_JOURNAL_FOREACH_UNIQUE()` were added in version 195.

`sd_journal_enumerate_available_unique()` was added in version 246.

## See Also

systemd(1), systemd.journal-fields(7), sd-journal(3), sd_journal_open(3), sd_journal_enumerate_fields(3), sd_journal_get_data(3), sd_journal_add_match(3)
