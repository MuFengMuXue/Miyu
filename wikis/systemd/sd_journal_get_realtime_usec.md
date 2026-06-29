## Name

sd_journal_get_realtime_usec, sd_journal_get_monotonic_usec — Read timestamps from the current journal entry

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-journal.h>
```

|                                             |                       |
|---------------------------------------------|-----------------------|
| `int `**`sd_journal_get_realtime_usec`**`(` | sd_journal \*`j`,     |
|                                             | uint64_t \*`usec``)`; |

 

|                                              |                            |
|----------------------------------------------|----------------------------|
| `int `**`sd_journal_get_monotonic_usec`**`(` | sd_journal \*`j`,          |
|                                              | uint64_t \*`usec`,         |
|                                              | sd_id128_t \*`boot_id``)`; |

 

## Description

`sd_journal_get_realtime_usec()` gets the realtime (wallclock) timestamp of the current journal entry. It takes two arguments: the journal context object and a pointer to a 64-bit unsigned integer to store the timestamp in. The timestamp is in microseconds since the epoch, i.e. `CLOCK_REALTIME`.

`sd_journal_get_monotonic_usec()` gets the monotonic timestamp of the current journal entry. It takes three arguments: the journal context object, a pointer to a 64-bit unsigned integer to store the timestamp in, as well as a 128-bit ID buffer to store the boot ID of the monotonic timestamp. The timestamp is in microseconds since boot-up of the specific boot, i.e. `CLOCK_MONOTONIC`. Since the monotonic clock begins new with every reboot, it only defines a well-defined point in time when used together with an identifier identifying the boot. See sd_id128_get_boot(3) for more information. If the boot ID parameter is passed `NULL`, the function will fail if the monotonic timestamp of the current entry is not of the current system boot.

Note that these functions will not work before sd_journal_next(3) (or related call) has been called at least once, in order to position the read pointer at a valid entry.

## Return Value

`sd_journal_get_realtime_usec()` and `sd_journal_get_monotonic_usec()` returns 0 on success or a negative errno-style error code. If the boot ID parameter was passed `NULL` and the monotonic timestamp of the current journal entry is not of the current system boot, `-ESTALE` is returned by `sd_journal_get_monotonic_usec()`.

## Notes

All functions listed here are thread-agnostic and only a single thread may operate on a given object at any given time. Different threads may access the same object at different times. Multiple independent objects may be used from different threads in parallel.

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

## History

`sd_journal_get_realtime_usec()` and `sd_journal_get_monotonic_usec()` were added in version 187.

## See Also

systemd(1), sd-journal(3), sd_journal_open(3), sd_journal_next(3), sd_journal_get_data(3), sd_journal_get_seqnum(3), sd_id128_get_boot(3), clock_gettime(2), sd_journal_get_cutoff_realtime_usec(3)
