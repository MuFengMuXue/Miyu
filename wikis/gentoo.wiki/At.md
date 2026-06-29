[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=At&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[[]][Home](https://packages.qa.debian.org/a/at.html)

[[]][Package information](https://packages.gentoo.org/packages/sys-process/at)

[[]][Wikipedia](https://en.wikipedia.org/wiki/At_(command) "wikipedia:At (command)")

[[]][Bugs (upstream)](https://bugs.debian.org/at)

[[]][Man page](http://man7.org/linux/man-pages/man1/at.1.html)

[[]][Blog](http://blog.calhariz.com/index.php/tag/at)

**[at]** is a tool for running delayed jobs and batching processes. Processes can be scheduled via 12 or 24 hour time in `HH:MM` notation. If that time is already passed, the next day is assumed. It\'s also possible to specify a job\'s time with a few different aliases, notably: *midnight* (00:00), *noon* (12:00), and *teatime* (16:00). Relative times are also acceptable.

It is also possible to schedule a job contingent upon acceptable system load via the [batch] command.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Environment variables]](#Environment_variables)
    -   [[1.4] [Files]](#Files)
    -   [[1.5] [Service]](#Service)
        -   [[1.5.1] [OpenRC]](#OpenRC)
        -   [[1.5.2] [runit]](#runit)
        -   [[1.5.3] [systemd]](#systemd)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [at]](#at)
    -   [[2.2] [atrun]](#atrun)
    -   [[2.3] [atq]](#atq)
    -   [[2.4] [atrm]](#atrm)
    -   [[2.5] [batch]](#batch)
    -   [[2.6] [Invocation]](#Invocation)
-   [[3] [Removal]](#Removal)
    -   [[3.1] [Unmerge]](#Unmerge)
-   [[4] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [sys-process/at](https://packages.gentoo.org/packages/sys-process/at) [[]] [Queues jobs for later execution]

  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`pam`](https://packages.gentoo.org/useflags/pam)           Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`selinux`](https://packages.gentoo.org/useflags/selinux)   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-09-02 17:00] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sys-process/at`

### [Environment variables]

-   `LOGNAME` --- if the user is not logged in at the time of the [at] job\'s scheduled execution, mail is sent to the user account specified in this variable.
-   `SHELL` --- used by [at] at execution time to determine the appropriate shell.

### [Files]

-   [/var/spool/at/atjobs] --- The directory for storing scheduled jobs.
-   [/var/spool/at/atspool] --- The directory for storing the output of completed jobs.
-   [/proc/loadavg] --- The system\'s load average.
-   [/var/run/utmp] --- Account login records.
-   [/etc/at/at.allow] --- The system whitelist for determining who may submit [at] batch jobs.
-   [/etc/at/at.deny] --- The system blacklist for preventing abuse of [at] batch jobs.

### [Service]

The [atd] service is required in order for [at] batch job execution to occur. It can be enabled as follows:

#### [OpenRC]

`root `[`#`]`rc-update add atd default`

`root `[`#`]`rc-service atd start`

#### [runit]

`root `[`#`]`ln -s /etc/sv/atd /var/service/`

`root `[`#`]`sv up atd`

#### [systemd]

`root `[`#`]`systemctl enable atd`

`root `[`#`]`systemctl start atd`

## [Usage]

### [[at]]

List scheduled jobs:

`user `[`$`]`at -l`

    10    Mon Mar 20 08:15:00 2023 a alice
    11  Mon Mar 20 09:45:00 2023 a bob

Pipe a simple command to [at] and have it run in 5 minutes.

`user `[`$`]`echo -e "testing, testing, 1, 2, 3" | at now +5 minutes`

Delete scheduled jobs:

`user `[`$`]`at -r 11`

### [[atrun]]

Define the system load below which scheduled jobs are permitted to run. For example, given a 4 core system running batch jobs with a system load of 3.0 might be far more realistic than the 0.8 default.

`user `[`$`]`atrun -l 3.0`

### [[atq]]

List scheduled jobs:

`user `[`$`]`atq`

    10  Mon Mar 20 08:15:00 2023 a alice
    11  Mon Mar 20 09:45:00 2023 a bob

### [[atrm]]

Delete a scheduled job:

`user `[`$`]`atrm 11`

### [[batch]]

** Note**\
The compile time default for batch is a system load of *0.8*, which may not be what you want on a modern multi-core system. To override this compile-time default use the [atd -l] command.

Run pending batch jobs when the current system load drops below a given threshold.

`user `[`$`]`batch`

### [Invocation]

`user `[`$`]`at -h`

    Usage: at [-V] [-q x] [-f file] [-u username] [-mMlbv] timespec ...
           at [-V] [-q x] [-f file] [-u username] [-mMlbv] -t time
           at -c job ...
           at [-V] -l [-o timeformat] [job ...]
           atq [-V] [-q x] [-o timeformat] [job ...]
           at [ -rd ] job ...
           atrm [-V] job ...
           batch

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose sys-process/at`

## [See also]

-   [cron](https://wiki.gentoo.org/wiki/Cron "Cron") --- how to setup and use **cron** daemons in Gentoo Linux
-   [Systemd#Timer_services](https://wiki.gentoo.org/wiki/Systemd#Timer_services "Systemd")