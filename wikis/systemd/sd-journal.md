## Name

sd-journal — APIs for submitting and querying log entries to and from the journal

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-journal.h>
```

`pkg-config --cflags --libs libsystemd`

## Description

`sd-journal.h` is part of libsystemd(3) and provides APIs to submit and query log entries. The APIs exposed act both as client for the systemd-journald.service(8) journal service and as parser for the journal files on disk.

See sd_journal_print(3), sd_journal_stream_fd(3), sd_journal_open(3), sd_journal_next(3), sd_journal_get_realtime_usec(3), sd_journal_add_match(3), sd_journal_seek_head(3), sd_journal_enumerate_fields(3), sd_journal_get_cursor(3), sd_journal_get_cutoff_realtime_usec(3), sd_journal_get_cutoff_monotonic_usec(3), sd_journal_get_usage(3), sd_journal_get_catalog(3), sd_journal_get_fd(3), sd_journal_has_runtime_files(3) and sd_journal_has_persistent_files(3) for more information about the functions implemented.

Command line access for submitting entries to the journal is available with the systemd-cat(1) tool. Command line access for querying entries from the journal is available with the journalctl(1) tool.

## Thread safety

Functions that operate on sd_journal objects are thread agnostic — a given sd_journal pointer may only be used from one thread at a time, but multiple independent threads may use multiple objects concurrently. Some functions — those that are used to send entries to the journal, like sd_journal_print(3) and similar, or those that are used to retrieve global information like sd_journal_stream_fd(3) and sd_journal_get_catalog_for_message_id(3) — are fully thread-safe and may be called from multiple threads in parallel.

## Optional dependencies

Depending on which build-time options are enabled, functions that operate on sd_journal objects might cause optional shared libraries to be dynamically loaded via dlopen(3), such as decompression libraries (xz, lz4, zstd) or cryptographic libraries (gcrypt).

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## See Also

systemd(1), sd_journal_print(3), sd_journal_stream_fd(3), sd_journal_open(3), sd_journal_next(3), sd_journal_get_data(3), sd_journal_get_realtime_usec(3), sd_journal_add_match(3), sd_journal_seek_head(3), sd_journal_enumerate_fields(3), sd_journal_get_cursor(3), sd_journal_get_cutoff_realtime_usec(3), sd_journal_get_cutoff_monotonic_usec(3), sd_journal_get_usage(3), sd_journal_get_fd(3), sd_journal_query_unique(3), sd_journal_get_catalog(3), sd_journal_has_runtime_files(3), sd_journal_has_persistent_files(3), journalctl(1), sd-id128(3), pkg-config(1)
