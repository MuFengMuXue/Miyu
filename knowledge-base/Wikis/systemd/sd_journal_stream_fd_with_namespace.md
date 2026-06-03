## Name

sd_journal_stream_fd, sd_journal_stream_fd_with_namespace — Create log stream file descriptor to the journal

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-journal.h>
```

|                                     |                            |
|-------------------------------------|----------------------------|
| `int `**`sd_journal_stream_fd`**`(` | const char \*`identifier`, |
|                                     | int `priority`,            |
|                                     | int `level_prefix``)`;     |

 

|  |  |
|----|----|
| `int `**`sd_journal_stream_fd_with_namespace`**`(` | const char \*`name_space`, |
|   | const char \*`identifier`, |
|   | int `priority`, |
|   | int `level_prefix``)`; |

 

## Description

`sd_journal_stream_fd()` may be used to create a log stream file descriptor. Log messages written to this file descriptor as simple newline-separated text strings are written to the journal. This file descriptor can be used internally by applications or be made standard output or standard error of other processes executed.

`sd_journal_stream_fd()` takes a short program identifier string as first argument, which will be written to the journal as SYSLOG_IDENTIFIER= field for each log entry (see systemd.journal-fields(7) for more information). The second argument shall be the default priority level for all messages. The priority level is one of `LOG_EMERG`, `LOG_ALERT`, `LOG_CRIT`, `LOG_ERR`, `LOG_WARNING`, `LOG_NOTICE`, `LOG_INFO`, `LOG_DEBUG`, as defined in `syslog.h`, see syslog(3) for details. The third argument is a boolean: if true kernel-style log level prefixes (such as `SD_WARNING`) are interpreted, see sd-daemon(3) for more information.

`sd_journal_stream_fd_with_namespace()` is similar to `sd_journal_stream_fd()`, but takes an additional *`name_space`* parameter that specifies which journal namespace to operate on. If specified as `NULL` the call is identical to `sd_journal_stream_fd()`. For details about journal namespaces, see systemd-journald.service(8).

It is recommended that applications log UTF-8 messages only with this API, but this is not enforced.

Each invocation of these functions allocates a new log stream file descriptor, that is not shared with prior or later invocations. The file descriptor is write-only (its reading direction is shut down), and `O_NONBLOCK` is turned off initially.

## Return Value

The call returns a valid write-only file descriptor on success or a negative errno-style error code.

## Signal safety

`sd_journal_stream_fd()` and `sd_journal_stream_fd_with_namespace()` are "async signal safe" in the meaning of signal-safety(7).

## Notes

All functions listed here are thread-safe and may be called in parallel from multiple threads.

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

## Examples

Creating a log stream suitable for fprintf(3):

``` programlisting
/* SPDX-License-Identifier: MIT-0 */

#define _GNU_SOURCE 1
#include <errno.h>
#include <syslog.h>
#include <stdio.h>
#include <unistd.h>
#include <systemd/sd-journal.h>
#include <systemd/sd-daemon.h>

int main(int argc, char *argv[]) {
  int fd;
  FILE *log;

  fd = sd_journal_stream_fd("test", LOG_INFO, 1);
  if (fd < 0) {
    fprintf(stderr, "Failed to create stream fd: %s\n", strerror(-fd));
    return 1;
  }

  log = fdopen(fd, "w");
  if (!log) {
    fprintf(stderr, "Failed to create file object: %s\n", strerror(errno));
    close(fd);
    return 1;
  }
  fprintf(log, "Hello World!\n");
  fprintf(log, SD_WARNING "This is a warning!\n");
  fclose(log);
  return 0;
}
```

## History

`sd_journal_stream_fd()` was added in version 187.

`sd_journal_stream_fd_with_namespace()` was added in version 256.

## See Also

systemd(1), sd-journal(3), sd-daemon(3), sd_journal_print(3), syslog(3), fprintf(3), systemd.journal-fields(7)
