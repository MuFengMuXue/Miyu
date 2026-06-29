## Name

sd-daemon, SD_EMERG, SD_ALERT, SD_CRIT, SD_ERR, SD_WARNING, SD_NOTICE, SD_INFO, SD_DEBUG — APIs for new-style daemons

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-daemon.h>
```

`pkg-config --cflags --libs libsystemd`

## Description

`sd-daemon.h` is part of libsystemd(3) and provides APIs for new-style daemons, as implemented by the systemd(1) service manager.

See sd_listen_fds(3), sd_notify(3), sd_booted(3), sd_is_fifo(3), sd_watchdog_enabled(3), and sd_pidfd_get_inode_id(3) for more information about the functions implemented. In addition to these functions, a couple of logging prefixes are defined as macros:

``` programlisting
#define SD_EMERG   "<0>"  /* system is unusable */
#define SD_ALERT   "<1>"  /* action must be taken immediately */
#define SD_CRIT    "<2>"  /* critical conditions */
#define SD_ERR     "<3>"  /* error conditions */
#define SD_WARNING "<4>"  /* warning conditions */
#define SD_NOTICE  "<5>"  /* normal but significant condition */
#define SD_INFO    "<6>"  /* informational */
#define SD_DEBUG   "<7>"  /* debug-level messages */
```

These prefixes are intended to be used in conjunction with stderr-based logging (or stdout-based logging) as implemented by systemd. If a systemd service definition file is configured with `StandardError=journal` or `StandardError=kmsg` (and similar with `StandardOutput=`), these prefixes can be used to encode a log level in lines printed. This is similar to the kernel `printk()`-style logging. See klogctl(2) for more information.

The log levels are identical to syslog(3)'s log level system. To use these prefixes simply prefix every line with one of these strings. A line that is not prefixed will be logged at the default log level SD_INFO.

**Example 1. Hello World**

A daemon may log with the log level NOTICE by issuing this call:

``` programlisting
fprintf(stderr, SD_NOTICE "Hello World!\n");
```

  

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## See Also

systemd(1), sd_listen_fds(3), sd_notify(3), sd_booted(3), sd_is_fifo(3), sd_watchdog_enabled(3), sd_pidfd_get_inode_id(3), daemon(7), systemd.service(5), systemd.socket(5), fprintf(3), pkg-config(1)
