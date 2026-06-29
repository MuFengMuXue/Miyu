**Resources**

[[]][Home](http://sebastien.godard.pagesperso-orange.fr/)

[[]][Package information](https://packages.gentoo.org/packages/app-admin/sysstat)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Systat_(tool) "wikipedia:Systat (tool)")

The sysstat (**sys**tem **stat**istics) utilities are a collection of performance monitoring tools for Linux. They function as front ends to the kernel\'s [/proc] filesystem making statistics easy to access. Sysstat was written by Sebastien Godard.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Statistics Collection and Aggregation]](#Statistics_Collection_and_Aggregation)
        -   [[2.1.1] [/etc/cron.]](#.2Fetc.2Fcron..7Bhourly.2Cdaily.2Cmonthly.2Cweekly.7D)
        -   [[2.1.2] [crontab(5)]](#crontab.285.29)
-   [[3] [Usage]](#Usage)
-   [[4] [Examples]](#Examples)
-   [[5] [See Also]](#See_Also)
-   [[6] [External Resources]](#External_Resources)
-   [[7] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [app-admin/sysstat](https://packages.gentoo.org/packages/app-admin/sysstat) [[]] [System performance tools for Linux]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`dcron`](https://packages.gentoo.org/useflags/dcron)             Adjust cronjobs to work properly under sys-process/dcron
  [`debug`](https://packages.gentoo.org/useflags/debug)             Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`lm-sensors`](https://packages.gentoo.org/useflags/lm-sensors)   Add linux lm-sensors (hardware sensors) support
  [`nls`](https://packages.gentoo.org/useflags/nls)                 Add Native Language Support (using gettext - GNU locale utilities)
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`systemd`](https://packages.gentoo.org/useflags/systemd)         Enable use of systemd-specific libraries and features like socket activation or session tracking
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-09-02 17:00] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

Add or remove the desired flags to [/etc/portage/package.use] or [/etc/portage/make.conf]:

[FILE] **`/etc/portage/package.use`Sysstat package.use example**

    ...
    app-admin/sysstat lm-sensors nls
    ...

### [Emerge]

Emerge [[[app-admin/sysstat]](https://packages.gentoo.org/packages/app-admin/sysstat)[]]:

`root `[`#`]`emerge --ask app-admin/sysstat`

## [Configuration]

The [/etc/sysstat] file influences the behavior of [/usr/lib/sa/sa1] and ([sadc(8)](http://man7.org/linux/man-pages/man8/sadc.8.html)) [/usr/lib/sa/sa2] ([sar(1)](http://man7.org/linux/man-pages/man1/sar.1.html)). This file sourced from [/bin/sh] and it\'s syntax should thus conform to [IEEE Std 1003.1](https://en.wikipedia.org/wiki/IEEE_Std_1003.1 "wikipedia:IEEE Std 1003.1").

The following variables will have some effect:

+----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------------+
| Variable                   | Description                                                                                                                             | Suggested Value | Affected Commands |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------------+
| `HISTORY`       | How long to keep log files (in days). If value is greater than 28, then log files are kept in multiple directories, one for each month. | `365`           | `sa1`             |
|                            |                                                                                                                                         |                 |                   |
|                            |                                                                                                                                         |                 | `sa2`             |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------------+
| `COMPRESSAFTER` | Compress (using gzip or bzip2) sa and sar files older than (in days)                                                                    | `10`            | `sa2`             |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------------+
| `SADC_OPTIONS`  | Parameters for the system activity data collector (see sadc manual page) which are used for the generation of log files.                | `-S XALL`       | `sa1`             |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------------+

### [Statistics Collection and Aggregation]

Statistics collection can be achieved by periodical execution of [/usr/lib/sa/sa1] (which invokes [sadc]) and [/usr/lib/sa/sa2] (which invokes [sar]).

The common approach is to use [crontab(5)] or [/etc/cron..

#### []}[[/etc/cron.]

** Note**\
The `cron` USE flag installs the files show below.

[FILE] **`/etc/cron.hourly/sysstat`Setting cron to run an accounting job**

    #!/bin/sh
    # Run system activity accounting tool every 10 minutes
    /usr/lib/sa/sa1 600 6 &

[FILE] **`/etc/cron.daily/sysstat`**

    #!/bin/sh
    # Generate a daily summary of process accounting. Since this will probably
    # get kicked off in the morning, it would probably be better to run against
    # the previous days data.
    /usr/lib/sa/sa2 -A &

#### [][[crontab(5)]]

** Note**\
Ensure that the `cron` USE flag is **not** set when this method is used.

`root `[`#`]`crontab -l`

    ...
    # app-admin/sysstat : collect system statistics every 10 minutes
    */10    *       *       *       *       /usr/lib/sa/sa1 1 1
    # app-admin/sysstat : aggregate system statistics every day at 23h00
    0   23  *   *   *   /usr/lib/sa/sa2 -A &
    ...

## [Usage]

The following tools are included with sysstat on Gentoo:^[\[1\]](#cite_note-1)^

  --------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Command               Description
  `cifsiostat`          Reports CIFS statistics.
  `iostat`              Reports CPU statistics and input/output statistics for devices, partitions and network filesystems.
  `mpstat`              Reports individual or combined processor related statistics.e
  `nfsiostat-sysstat`   Reports input/output statistics for network filesystems (NFS).
  `pidstat`             Reports statistics for Linux tasks (processes): I/O, CPU, memory, etc.
  `sadf`                Displays data collected by `sar` in multiple formats (CSV, XML, etc.) Useful to load performance data into a database, or import them to spreadsheets to make graphs.
  `sar`                 Collects, reports and saves system activity information (CPU, memory, disks, interrupts, network interfaces, TTY, kernel tables, etc.)
  --------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [Examples]

Use `iostat` to watch the input/output of data to attached drives, display the output in megabytes:

`user `[`$`]`watch iostat -m`

## [See Also]

-   [Iotop](https://wiki.gentoo.org/wiki/Iotop "Iotop") --- a top-like utility that monitors system **i**nput/**o**utput.
-   [Atop](https://wiki.gentoo.org/index.php?title=Atop&action=edit&redlink=1 "Atop (page does not exist)")
-   [Htop](https://wiki.gentoo.org/wiki/Htop "Htop") --- a cross-platform interactive process viewer. It is a text-mode application (for console or X terminals) and requires ncurses.

## [External Resources]

-   The Sysstat source code repository [on GitHub](https://github.com/sysstat/sysstat).
-   Official tutorials on [how to use Sysstat](http://sebastien.godard.pagesperso-orange.fr/tutorial.html).
-   [Official Sysstat documentation](http://sebastien.godard.pagesperso-orange.fr/documentation.html).

** Note**\
Local man pages will only be available if the `doc` USE was enabled at build time.

-   The cifsiostat man page locally ([man cifsiostat]) or [online](http://man7.org/linux/man-pages/man1/cifsiostat.1.html).
-   The iostat man page locally ([man iostat]) or [online](http://man7.org/linux/man-pages/man1/iostat.1.html).
-   The mpstat man page locally ([man mpstat]) or [online](http://man7.org/linux/man-pages/man1/mpstat.1.html).
-   The pidstatman page locally ([man pidstat]) or [online](http://man7.org/linux/man-pages/man1/pidstat.1.html).
-   The sadf man page locally ([man sadf]) or [online](http://man7.org/linux/man-pages/man1/sadf.1.html).
-   The sar man page locally ([man sar]) or [online](http://man7.org/linux/man-pages/man1/sar.1.html).
-   The sysstat man page locally ([man sysstat]) or [online](http://man7.org/linux/man-pages/man5/sysstat.5.html).
-   The sa1 man page locally ([man sa1]) or [online](http://man7.org/linux/man-pages/man8/sa1.8.html).
-   The sa2 man page locally ([man sa2]) or [online](http://man7.org/linux/man-pages/man8/sa2.8.html).
-   The sadc man page locally ([man sadc]) or [online](http://man7.org/linux/man-pages/man8/sadc.8.html).

## [References]

1.  [[[↑](#cite_ref-1)] [[http://sebastien.godard.pagesperso-orange.fr/documentation.html](http://sebastien.godard.pagesperso-orange.fr/documentation.html)]]