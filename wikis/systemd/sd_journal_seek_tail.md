## Name

sd_journal_seek_head, sd_journal_seek_tail, sd_journal_seek_monotonic_usec, sd_journal_seek_realtime_usec, sd_journal_seek_cursor — Seek to a position in the journal

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-journal.h>
```

|                                     |                      |
|-------------------------------------|----------------------|
| `int `**`sd_journal_seek_head`**`(` | sd_journal \*`j``)`; |

 

|                                     |                      |
|-------------------------------------|----------------------|
| `int `**`sd_journal_seek_tail`**`(` | sd_journal \*`j``)`; |

 

|                                               |                       |
|-----------------------------------------------|-----------------------|
| `int `**`sd_journal_seek_monotonic_usec`**`(` | sd_journal \*`j`,     |
|                                               | sd_id128_t `boot_id`, |
|                                               | uint64_t `usec``)`;   |

 

|                                              |                     |
|----------------------------------------------|---------------------|
| `int `**`sd_journal_seek_realtime_usec`**`(` | sd_journal \*`j`,   |
|                                              | uint64_t `usec``)`; |

 

|                                       |                           |
|---------------------------------------|---------------------------|
| `int `**`sd_journal_seek_cursor`**`(` | sd_journal \*`j`,         |
|                                       | const char \*`cursor``)`; |

 

## Description

`sd_journal_seek_head()` seeks to the beginning of the journal, i.e. to the position before the oldest available entry.

Similarly, `sd_journal_seek_tail()` may be used to seek to the end of the journal, i.e. the position after the most recent available entry.

`sd_journal_seek_monotonic_usec()` seeks to a position with the specified monotonic timestamp, i.e. `CLOCK_MONOTONIC`. Since monotonic time restarts on every reboot a boot ID needs to be specified as well.

`sd_journal_seek_realtime_usec()` seeks to a position with the specified realtime (wallclock) timestamp, i.e. `CLOCK_REALTIME`. Note that the realtime clock is not necessarily monotonic. If a realtime timestamp is ambiguous, it is not defined which position is sought to.

`sd_journal_seek_cursor()` seeks to the position at the specified cursor string. For details on cursors, see sd_journal_get_cursor(3). If no entry matching the specified cursor is found the call will seek to the next closest entry (in terms of time) instead.

Note that these calls do not actually make any entry the new current entry, this needs to be done in a separate step with a subsequent sd_journal_next(3) invocation (or a similar call). Only then, entry data may be retrieved via sd_journal_get_data(3) or an entry cursor be retrieved via sd_journal_get_cursor(3). If no entry exists that matches exactly the specified seek address, the next closest is sought to. If sd_journal_next(3) is used, the closest following entry will be sought to, if sd_journal_previous(3) is used the closest preceding entry is sought to.

After the seek is done, and sd_journal_next(3) or a similar call has been made, sd_journal_test_cursor(3) may be used to verify whether the newly selected entry actually matches the cursor.

## Return Value

The functions return 0 on success or a negative errno-style error code.

## Notes

All functions listed here are thread-agnostic and only a single thread may operate on a given object at any given time. Different threads may access the same object at different times. Multiple independent objects may be used from different threads in parallel.

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

## History

`sd_journal_seek_head()`, `sd_journal_seek_tail()`, `sd_journal_seek_monotonic_usec()`, `sd_journal_seek_realtime_usec()`, and `sd_journal_seek_cursor()` were added in version 187.

## See Also

systemd(1), sd-journal(3), sd_journal_open(3), sd_journal_next(3), sd_journal_get_data(3), sd_journal_get_cursor(3), sd_journal_get_realtime_usec(3)
