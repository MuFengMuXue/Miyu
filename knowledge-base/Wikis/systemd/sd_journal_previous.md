## Name

sd_journal_next, sd_journal_previous, sd_journal_step_one, sd_journal_next_skip, sd_journal_previous_skip, SD_JOURNAL_FOREACH, SD_JOURNAL_FOREACH_BACKWARDS — Advance or set back the read pointer in the journal

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-journal.h>
```

|                                |                      |
|--------------------------------|----------------------|
| `int `**`sd_journal_next`**`(` | sd_journal \*`j``)`; |

 

|                                    |                      |
|------------------------------------|----------------------|
| `int `**`sd_journal_previous`**`(` | sd_journal \*`j``)`; |

 

|                                    |                    |
|------------------------------------|--------------------|
| `int `**`sd_journal_step_one`**`(` | sd_journal \*`j`,  |
|                                    | int `advanced``)`; |

 

|                                     |                     |
|-------------------------------------|---------------------|
| `int `**`sd_journal_next_skip`**`(` | sd_journal \*`j`,   |
|                                     | uint64_t `skip``)`; |

 

|                                         |                     |
|-----------------------------------------|---------------------|
| `int `**`sd_journal_previous_skip`**`(` | sd_journal \*`j`,   |
|                                         | uint64_t `skip``)`; |

 

|                             |                      |
|-----------------------------|----------------------|
| **`SD_JOURNAL_FOREACH`**`(` | sd_journal \*`j``)`; |

 

|                                       |                      |
|---------------------------------------|----------------------|
| **`SD_JOURNAL_FOREACH_BACKWARDS`**`(` | sd_journal \*`j``)`; |

 

## Description

`sd_journal_next()` advances the read pointer into the journal by one entry. The only argument taken is a journal context object as allocated via sd_journal_open(3). After successful invocation the entry may be read with functions such as sd_journal_get_data(3).

Similarly, `sd_journal_previous()` sets the read pointer back one entry.

`sd_journal_step_one()` also moves the read pointer. If the current location is the head of the journal, e.g. when this is called following `sd_journal_seek_head()`, then this is equivalent to `sd_journal_next()`, and the argument `advanced` will be ignored. Similarly, if the current location is the tail of the journal, e.g. when this is called following `sd_journal_seek_tail()`, then this is equivalent to `sd_journal_previous()`, and `advanced` will be ignored. Otherwise, this is equivalent to `sd_journal_next()` when `advanced` is non-zero, and `sd_journal_previous()` when `advanced` is zero.

`sd_journal_next_skip()` and `sd_journal_previous_skip()` advance/set back the read pointer by multiple entries at once, as specified in the `skip` parameter. The `skip` parameter must be less than or equal to 2147483647 (2³¹-1).

The journal is strictly ordered by reception time, and hence advancing to the next entry guarantees that the entry then pointing to is later in time than then previous one, or has the same timestamp.

Note that sd_journal_get_data(3) and related calls will fail unless `sd_journal_next()` has been invoked at least once in order to position the read pointer on a journal entry.

Note that the `SD_JOURNAL_FOREACH()` macro may be used as a wrapper around sd_journal_seek_head(3) and `sd_journal_next()` in order to make iterating through the journal easier. See below for an example. Similarly, `SD_JOURNAL_FOREACH_BACKWARDS()` may be used for iterating the journal in reverse order.

## Return Value

The four calls return the number of entries advanced/set back on success or a negative errno-style error code. When the end or beginning of the journal is reached, a number smaller than requested is returned. More specifically, if `sd_journal_next()` or `sd_journal_previous()` reach the end/beginning of the journal they will return 0, instead of 1 when they are successful. This should be considered an EOF marker.

## Notes

All functions listed here are thread-agnostic and only a single thread may operate on a given object at any given time. Different threads may access the same object at different times. Multiple independent objects may be used from different threads in parallel.

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

## Examples

Iterating through the journal:

``` programlisting
/* SPDX-License-Identifier: MIT-0 */

#include <errno.h>
#include <stdio.h>
#include <systemd/sd-journal.h>

int main(int argc, char *argv[]) {
  int r;
  sd_journal *j;

  r = sd_journal_open(&j, SD_JOURNAL_LOCAL_ONLY);
  if (r < 0) {
    fprintf(stderr, "Failed to open journal: %s\n", strerror(-r));
    return 1;
  }
  SD_JOURNAL_FOREACH(j) {
    const char *d;
    size_t l;

    r = sd_journal_get_data(j, "MESSAGE", (const void **)&d, &l);
    if (r < 0) {
      fprintf(stderr, "Failed to read message field: %s\n", strerror(-r));
      continue;
    }

    printf("%.*s\n", (int) l, d);
  }
  sd_journal_close(j);
  return 0;
}
```

## History

`sd_journal_next()`, `sd_journal_previous()`, `sd_journal_next_skip()`, `sd_journal_previous_skip()`, `SD_JOURNAL_FOREACH()`, and `SD_JOURNAL_FOREACH_BACKWARDS()` were added in version 187.

`sd_journal_step_one()` was added in version 254.

## See Also

systemd(1), sd-journal(3), sd_journal_open(3), sd_journal_get_data(3), sd_journal_get_realtime_usec(3), sd_journal_get_cursor(3)
