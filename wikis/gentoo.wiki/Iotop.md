[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Iotop&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](http://guichaz.free.fr/iotop/)

[[]][GitWeb](http://repo.or.cz/w/iotop.git)

**iotop** is a top-like utility that monitors system **i**nput/**o**utput.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Installation]

### [Kernel]

The `CONFIG_TASK_IO_ACCOUNTING` variable must be enabled in the Linux kernel for the [iotop] command to work properly. It can be found at this location:

[KERNEL] **Kernel configuration for iotop**

General setup -\> CPU/Task time and stats accounting

      [*]   Enable per-task delay accounting Search for <code>CONFIG_TASK_DELAY_ACCT</code> to find this item.
      [*]   Enable extended accounting over taskstats Search for <code>CONFIG_TASK_XACCT</code> to find this item.
      [*]     Enable per-task storage I/O accounting Search for <code>CONFIG_TASK_IO_ACCOUNTING</code> to find this item.
      [*] Enable VM event counters for /proc/vmstat (EXPERT)

Additionally, \"delayacct\" must be added to the kernel command-line such as `GRUB_CMDLINE_LINUX` for grub.

### [Emerge]

Install the package:

`root `[`#`]`emerge --ask sys-process/iotop`

## [Usage]

### [Invocation]

`root `[`#`]`iotop --help`

    Usage: iotop [OPTIONS]

    DISK READ and DISK WRITE are the block I/O bandwidth used during the sampling
    period. SWAPIN and IO are the percentages of time the thread spent respectively
    while swapping in and waiting on I/O more generally. PRIO is the I/O priority at
    which the thread is running (set using the ionice command).

    Controls: left and right arrows to change the sorting column, r to invert the
    sorting order, o to toggle the --only option, p to toggle the --processes
    option, a to toggle the --accumulated option, i to change I/O priority, q to
    quit, any other key to force a refresh.

    Options:
      --version             show program's version number and exit
      -h, --help            show this help message and exit
      -o, --only            only show processes or threads actually doing I/O
      -b, --batch           non-interactive mode
      -n NUM, --iter=NUM    number of iterations before ending [infinite]
      -d SEC, --delay=SEC   delay between iterations [1 second]
      -p PID, --pid=PID     processes/threads to monitor [all]
      -u USER, --user=USER  users to monitor [all]
      -P, --processes       only show processes, not all threads
      -a, --accumulated     show accumulated I/O instead of bandwidth
      -k, --kilobytes       use kilobytes instead of a human friendly unit
      -t, --time            add a timestamp on each line (implies --batch)
      -q, --quiet           suppress some lines of header (implies --batch)

## [See also]

-   [[top](https://wiki.gentoo.org/index.php?title=Top&action=edit&redlink=1 "Top (page does not exist)")] - A utility that displays Linux processes.
-   [[atop](https://wiki.gentoo.org/index.php?title=Atop&action=edit&redlink=1 "Atop (page does not exist)")] - A [top]-like interactive monitor that displays load on the Linux system.
-   [[htop](https://wiki.gentoo.org/wiki/Htop "Htop")] - Another [top]-like clone that displays Linux processes.
-   [Nload](https://wiki.gentoo.org/wiki/Nload "Nload") --- a super simple, command-line network interface monitoring tool.

## [External resources]

-   [iotop on Freecode.com](http://freecode.com/projects/iotop/)
-   [Slicehost article on iotop](http://articles.slicehost.com/2010/11/12/using-iotop-to-check-i-o-and-swap)