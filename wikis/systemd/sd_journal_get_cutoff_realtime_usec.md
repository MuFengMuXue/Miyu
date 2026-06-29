## Name

sd_journal_get_cutoff_realtime_usec, sd_journal_get_cutoff_monotonic_usec — Read cut-off timestamps from the current journal entry

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-journal.h>
```

|                                                    |                     |
|----------------------------------------------------|---------------------|
| `int `**`sd_journal_get_cutoff_realtime_usec`**`(` | sd_journal \*`j`,   |
|                                                    | uint64_t \*`from`,  |
|                                                    | uint64_t \*`to``)`; |

 

|                                                     |                       |
|-----------------------------------------------------|-----------------------|
| `int `**`sd_journal_get_cutoff_monotonic_usec`**`(` | sd_journal \*`j`,     |
|                                                     | sd_id128_t `boot_id`, |
|                                                     | uint64_t \*`from`,    |
|                                                     | uint64_t \*`to``)`;   |

 

## Description

`sd_journal_get_cutoff_realtime_usec()` retrieves the realtime (wallclock) timestamps of the first and last entries accessible in the journal. It takes three arguments: the journal context object *`j`* and two pointers *`from`* and *`to`* pointing at 64-bit unsigned integers to store the timestamps in. The timestamps are in microseconds since the epoch, i.e. `CLOCK_REALTIME`. Either one of the two timestamp arguments may be passed as `NULL` in case the timestamp is not needed, but not both.

`sd_journal_get_cutoff_monotonic_usec()` retrieves the monotonic timestamps of the first and last entries accessible in the journal. It takes three arguments: the journal context object *`j`*, a 128-bit identifier for the boot *`boot_id`*, and two pointers to 64-bit unsigned integers to store the timestamps, *`from`* and *`to`*. The timestamps are in microseconds since boot-up of the specific boot, i.e. `CLOCK_MONOTONIC`. Since the monotonic clock begins new with every reboot it only defines a well-defined point in time when used together with an identifier identifying the boot, see sd_id128_get_boot(3) for more information. The function will return the timestamps for the boot identified by the passed boot ID. Either one of the two timestamp arguments may be passed as `NULL` in case the timestamp is not needed, but not both.

## Return Value

`sd_journal_get_cutoff_realtime_usec()` and `sd_journal_get_cutoff_monotonic_usec()` return 1 on success, 0 if not suitable entries are in the journal or a negative errno-style error code.

Locations pointed to by parameters *`from`* and *`to`* will be set only if the return value is positive, and obviously, the parameters are non-null.

## Notes

All functions listed here are thread-agnostic and only a single thread may operate on a given object at any given time. Different threads may access the same object at different times. Multiple independent objects may be used from different threads in parallel.

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

## History

`sd_journal_get_cutoff_realtime_usec()` and `sd_journal_get_cutoff_monotonic_usec()` were added in version 187.

## See Also

systemd(1), sd-journal(3), sd_journal_open(3), sd_journal_get_realtime_usec(3), sd_id128_get_boot(3), clock_gettime(2)
