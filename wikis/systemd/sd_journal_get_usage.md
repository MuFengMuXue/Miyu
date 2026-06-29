## Name

sd_journal_get_usage — Journal disk usage

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-journal.h>
```

|                                     |                        |
|-------------------------------------|------------------------|
| `int `**`sd_journal_get_usage`**`(` | sd_journal \*`j`,      |
|                                     | uint64_t \*`bytes``)`; |

 

## Description

`sd_journal_get_usage()` determines the total disk space currently used by journal files (in bytes). If `SD_JOURNAL_LOCAL_ONLY` was passed when opening the journal, this value will only reflect the size of journal files of the local host, otherwise of all hosts.

## Return Value

`sd_journal_get_usage()` returns 0 on success or a negative errno-style error code.

## Notes

All functions listed here are thread-agnostic and only a single thread may operate on a given object at any given time. Different threads may access the same object at different times. Multiple independent objects may be used from different threads in parallel.

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

## History

`sd_journal_get_usage()` was added in version 190.

## See Also

systemd(1), sd-journal(3), sd_journal_open(3)
