## Name

sd_journal_enumerate_fields, sd_journal_restart_fields, SD_JOURNAL_FOREACH_FIELD — Read used field names from the journal

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-journal.h>
```

|                                            |                            |
|--------------------------------------------|----------------------------|
| `int `**`sd_journal_enumerate_fields`**`(` | sd_journal \*`j`,          |
|                                            | const char \*\*`field``)`; |

 

|                                           |                      |
|-------------------------------------------|----------------------|
| `void `**`sd_journal_restart_fields`**`(` | sd_journal \*`j``)`; |

 

|                                   |                          |
|-----------------------------------|--------------------------|
| **`SD_JOURNAL_FOREACH_FIELD`**`(` | sd_journal \*`j`,        |
|                                   | const char \*`field``)`; |

 

## Description

`sd_journal_enumerate_fields()` may be used to iterate through all field names used in the opened journal files. On each invocation the next field name is returned. The order of the returned field names is not defined. It takes two arguments: the journal context object, plus a pointer to a constant string pointer where the field name is stored in. The returned data is in a read-only memory map and is only valid until the next invocation of `sd_journal_enumerate_fields()`. Note that this call is subject to the data field size threshold as controlled by `sd_journal_set_data_threshold()`.

`sd_journal_restart_fields()` resets the field name enumeration index to the beginning of the list. The next invocation of `sd_journal_enumerate_fields()` will return the first field name again.

The `SD_JOURNAL_FOREACH_FIELD()` macro may be used as a handy wrapper around `sd_journal_restart_fields()` and `sd_journal_enumerate_fields()`.

These functions currently are not influenced by matches set with `sd_journal_add_match()` but this might change in a later version of this software.

To retrieve the possible values a specific field can take use sd_journal_query_unique(3).

## Return Value

`sd_journal_enumerate_fields()` returns a positive integer if the next field name has been read, 0 when no more field names are known, or a negative errno-style error code. `sd_journal_restart_fields()` returns nothing.

## Notes

All functions listed here are thread-agnostic and only a single thread may operate on a given object at any given time. Different threads may access the same object at different times. Multiple independent objects may be used from different threads in parallel.

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

## Examples

Use the `SD_JOURNAL_FOREACH_FIELD()` macro to iterate through all field names in use in the current journal.

``` programlisting
/* SPDX-License-Identifier: MIT-0 */

#include <errno.h>
#include <stdio.h>
#include <systemd/sd-journal.h>

int main(int argc, char *argv[]) {
  sd_journal *j;
  const char *field;
  int r;

  r = sd_journal_open(&j, SD_JOURNAL_LOCAL_ONLY);
  if (r < 0) {
    fprintf(stderr, "Failed to open journal: %s\n", strerror(-r));
    return 1;
  }
  SD_JOURNAL_FOREACH_FIELD(j, field)
    printf("%s\n", field);
  sd_journal_close(j);
  return 0;
}
```

## History

`sd_journal_enumerate_fields()`, `sd_journal_restart_fields()`, and `SD_JOURNAL_FOREACH_FIELD()` were added in version 229.

## See Also

systemd(1), systemd.journal-fields(7), sd-journal(3), sd_journal_open(3), sd_journal_query_unique(3), sd_journal_get_data(3), sd_journal_add_match(3)
