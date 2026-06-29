## Name

sd_journal_has_runtime_files, sd_journal_has_persistent_files — Query availability of runtime or persistent journal files

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-journal.h>
```

|                                             |                      |
|---------------------------------------------|----------------------|
| `int `**`sd_journal_has_runtime_files`**`(` | sd_journal \*`j``)`; |

 

|                                                |                      |
|------------------------------------------------|----------------------|
| `int `**`sd_journal_has_persistent_files`**`(` | sd_journal \*`j``)`; |

 

## Description

`sd_journal_has_runtime_files()` returns a positive value if runtime journal files (present in /run/systemd/journal/) have been found. Otherwise, returns 0.

`sd_journal_has_persistent_files()` returns a positive value if persistent journal files (present in /var/log/journal/) have been found. Otherwise, returns 0.

## Return value

Both `sd_journal_has_runtime_files()` and `sd_journal_has_persistent_files()` return -EINVAL if their argument is `NULL`.

## Notes

All functions listed here are thread-agnostic and only a single thread may operate on a given object at any given time. Different threads may access the same object at different times. Multiple independent objects may be used from different threads in parallel.

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

## History

`sd_journal_has_runtime_files()` and `sd_journal_has_persistent_files()` were added in version 229.

## See Also

systemd(1), sd-journal(3)
