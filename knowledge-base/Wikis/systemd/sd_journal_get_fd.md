## Name

sd_journal_get_fd, sd_journal_get_events, sd_journal_get_timeout, sd_journal_process, sd_journal_wait, sd_journal_reliable_fd, SD_JOURNAL_NOP, SD_JOURNAL_APPEND, SD_JOURNAL_INVALIDATE — Journal change notification interface

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-journal.h>
```

|                                  |                      |
|----------------------------------|----------------------|
| `int `**`sd_journal_get_fd`**`(` | sd_journal \*`j``)`; |

 

|                                      |                      |
|--------------------------------------|----------------------|
| `int `**`sd_journal_get_events`**`(` | sd_journal \*`j``)`; |

 

|                                       |                               |
|---------------------------------------|-------------------------------|
| `int `**`sd_journal_get_timeout`**`(` | sd_journal \*`j`,             |
|                                       | uint64_t \*`timeout_usec``)`; |

 

|                                   |                      |
|-----------------------------------|----------------------|
| `int `**`sd_journal_process`**`(` | sd_journal \*`j``)`; |

 

|                                |                             |
|--------------------------------|-----------------------------|
| `int `**`sd_journal_wait`**`(` | sd_journal \*`j`,           |
|                                | uint64_t `timeout_usec``)`; |

 

|                                       |                      |
|---------------------------------------|----------------------|
| `int `**`sd_journal_reliable_fd`**`(` | sd_journal \*`j``)`; |

 

## Description

`sd_journal_get_fd()` returns a file descriptor that may be asynchronously polled in an external event loop and is signaled as soon as the journal changes, because new entries or files were added, rotation took place, or files have been deleted, and similar. The file descriptor is suitable for usage in poll(2). Use `sd_journal_get_events()` for an events mask to watch for. The call takes one argument: the journal context object. Note that not all file systems are capable of generating the necessary events for wakeups from this file descriptor for changes to be noticed immediately. In particular network files systems do not generate suitable file change events in all cases. Cases like this can be detected with `sd_journal_reliable_fd()`, below. `sd_journal_get_timeout()` will ensure in these cases that wake-ups happen frequently enough for changes to be noticed, although with a certain latency.

`sd_journal_get_events()` will return the `poll()` mask to wait for. This function will return a combination of `POLLIN` and `POLLOUT` and similar to fill into the "`.events`" field of `struct pollfd`.

`sd_journal_get_timeout()` will return a timeout value for usage in `poll()`. This returns a value in microseconds since the epoch of `CLOCK_MONOTONIC` for timing out `poll()` in `timeout_usec`. See clock_gettime(2) for details about `CLOCK_MONOTONIC`. If there is no timeout to wait for, this will fill in `(uint64_t) -1` instead. Note that `poll()` takes a relative timeout in milliseconds rather than an absolute timeout in microseconds. To convert the absolute 'us' timeout into relative 'ms', use code like the following:

``` programlisting
uint64_t t;
int msec;
sd_journal_get_timeout(m, &t);
if (t == (uint64_t) -1)
  msec = -1;
else {
  struct timespec ts;
  uint64_t n;
  clock_gettime(CLOCK_MONOTONIC, &ts);
  n = (uint64_t) ts.tv_sec * 1000000 + ts.tv_nsec / 1000;
  msec = t > n ? (int) ((t - n + 999) / 1000) : 0;
}
```

The code above does not do any error checking for brevity's sake. The calculated `msec` integer can be passed directly as `poll()`'s timeout parameter.

After each `poll()` wake-up `sd_journal_process()` needs to be called to process events. This call will also indicate what kind of change has been detected (see below; note that spurious wake-ups are possible).

A synchronous alternative for using `sd_journal_get_fd()`, `sd_journal_get_events()`, `sd_journal_get_timeout()` and `sd_journal_process()` is `sd_journal_wait()`. It will synchronously wait until the journal gets changed. The maximum time this call sleeps may be controlled with the *`timeout_usec`* parameter. Pass `(uint64_t) -1` to wait indefinitely. Internally this call simply combines `sd_journal_get_fd()`, `sd_journal_get_events()`, `sd_journal_get_timeout()`, `poll()` and `sd_journal_process()` into one.

`sd_journal_reliable_fd()` may be used to check whether the wake-up events from the file descriptor returned by `sd_journal_get_fd()` are known to be quickly triggered. On certain file systems where file change events from the OS are not available (such as NFS) changes need to be polled for repeatedly, and hence are detected only with a considerable latency. This call will return a positive value if the journal changes are detected quickly and zero when they need to be polled for. Note that there is usually no need to invoke this function directly as `sd_journal_get_timeout()` will request appropriate timeouts anyway.

Note that all of the above change notification interfaces do not report changes instantly. Latencies are introduced for multiple reasons: as mentioned certain storage backends require time-based polling, in other cases wake-ups are optimized by coalescing events, and the OS introduces additional IO/CPU scheduling latencies.

## Return Value

`sd_journal_get_fd()` returns a valid file descriptor on success or a negative errno-style error code.

`sd_journal_get_events()` returns a combination of `POLLIN`, `POLLOUT` and suchlike on success or a negative errno-style error code.

`sd_journal_reliable_fd()` returns a positive integer if the file descriptor returned by `sd_journal_get_fd()` will generate wake-ups immediately for all journal changes. Returns 0 if there might be a latency involved.

`sd_journal_process()` and `sd_journal_wait()` return a negative errno-style error code, or one of `SD_JOURNAL_NOP`, `SD_JOURNAL_APPEND` or `SD_JOURNAL_INVALIDATE` on success:

- If `SD_JOURNAL_NOP` is returned, the journal did not change since the last invocation.

- If `SD_JOURNAL_APPEND` is returned, new entries have been appended to the end of the journal. In this case, it is sufficient to simply continue reading at the previous end location of the journal, to read the newly added entries.

- If `SD_JOURNAL_INVALIDATE`, journal files were added to or removed from the set of journal files watched (e.g. due to rotation or vacuuming), and thus entries might have appeared or disappeared at arbitrary places in the log stream, possibly before or after the previous end of the log stream. If `SD_JOURNAL_INVALIDATE` is returned, live-view UIs that want to reflect on screen the precise state of the log data on disk should probably refresh their entire display (relative to the cursor of the log entry on the top of the screen). Programs only interested in a strictly sequential stream of log data may treat `SD_JOURNAL_INVALIDATE` the same way as `SD_JOURNAL_APPEND`, thus ignoring any changes to the log view earlier than the old end of the log stream.

## Signal safety

In general, `sd_journal_get_fd()`, `sd_journal_get_events()`, and `sd_journal_get_timeout()` are *not* "async signal safe" in the meaning of signal-safety(7). Nevertheless, only the first call to any of those three functions performs unsafe operations, so subsequent calls *are* safe.

`sd_journal_process()` and `sd_journal_wait()` are not safe. `sd_journal_reliable_fd()` is safe.

## Notes

All functions listed here are thread-agnostic and only a single thread may operate on a given object at any given time. Different threads may access the same object at different times. Multiple independent objects may be used from different threads in parallel.

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

## Examples

Iterating through the journal, in a live view tracking all changes:

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

  for (;;)  {
    const void *d;
    size_t l;
    r = sd_journal_next(j);
    if (r < 0) {
      fprintf(stderr, "Failed to iterate to next entry: %s\n", strerror(-r));
      break;
    }
    if (r == 0) {
      /* Reached the end, let's wait for changes, and try again */
      r = sd_journal_wait(j, (uint64_t) -1);
      if (r < 0) {
        fprintf(stderr, "Failed to wait for changes: %s\n", strerror(-r));
        break;
      }
      continue;
    }
    r = sd_journal_get_data(j, "MESSAGE", &d, &l);
    if (r < 0) {
      fprintf(stderr, "Failed to read message field: %s\n", strerror(-r));
      continue;
    }
    printf("%.*s\n", (int) l, (const char*) d);
  }

  sd_journal_close(j);
  return 0;
}
```

Waiting with `poll()` (this example lacks all error checking for the sake of simplicity):

``` programlisting
/* SPDX-License-Identifier: MIT-0 */

#define _GNU_SOURCE 1
#include <poll.h>
#include <time.h>
#include <systemd/sd-journal.h>

int wait_for_changes(sd_journal *j) {
  uint64_t t;
  int msec;
  struct pollfd pollfd;

  sd_journal_get_timeout(j, &t);
  if (t == (uint64_t) -1)
    msec = -1;
  else {
    struct timespec ts;
    uint64_t n;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    n = (uint64_t) ts.tv_sec * 1000000 + ts.tv_nsec / 1000;
    msec = t > n ? (int) ((t - n + 999) / 1000) : 0;
  }

  pollfd.fd = sd_journal_get_fd(j);
  pollfd.events = sd_journal_get_events(j);
  poll(&pollfd, 1, msec);
  return sd_journal_process(j);
}
```

## History

`sd_journal_get_fd()`, `sd_journal_process()`, and `sd_journal_wait()` were added in version 187.

`sd_journal_reliable_fd()` was added in version 196.

`sd_journal_get_events()` and `sd_journal_get_timeout()` were added in version 201.

## See Also

systemd(1), sd-journal(3), sd_journal_open(3), sd_journal_next(3), poll(2), clock_gettime(2)
