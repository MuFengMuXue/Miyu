**Resources**

[[]][Home](https://github.com/logrotate/logrotate)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Log_rotation "wikipedia:Log rotation")

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/logrotate)

**Logrotate** is a tool to periodically rotate (archive), delete, and optionally compress and/or mail historic log files. Logrotate ships with, and is typically invoked by a [/etc/cron.daily] cron job.

## Contents

-   [[1] [USE flags]](#USE_flags)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Emerge]](#Emerge)
-   [[3] [Introduction]](#Introduction)
-   [[4] [Configuration]](#Configuration)
    -   [[4.1] [Files]](#Files)
        -   [[4.1.1] [Configure daily rotation]](#Configure_daily_rotation)
        -   [[4.1.2] [Portage logrotate module]](#Portage_logrotate_module)
-   [[5] [Usage]](#Usage)
-   [[6] [See also]](#See_also)

### [USE flags]

### [USE flags for] [app-admin/logrotate](https://packages.gentoo.org/packages/app-admin/logrotate) [[]] [Rotates, compresses, and mails system logs]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`+cron`](https://packages.gentoo.org/useflags/+cron)             Installs cron file
  [`acl`](https://packages.gentoo.org/useflags/acl)                 Add support for Access Control Lists
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-09-02 17:00] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask app-admin/logrotate`

## [Introduction]

Logrotate can be used to ensure logs are retained based on a defined policy. This policy can be based on file age, size, and number of total similar files.

Proper log storage is important, for a variety of reasons:

-   Readability - If logs are disorganized, they become harder to use.
-   Security - Logs are essential for incident responses, poorly organized and incomplete logs can make this more difficult or impossible.
-   Integrity - If logs are managed poorly, data could be lost or overwritten.

## [Configuration]

### [Files]

-   [/etc/logrotate.conf] - The daemon\'s configuration file.
-   [/etc/logrotate.d] - The directory containing configuration files installed by other services.

#### [Configure daily rotation]

By default, [logrotate] is configured to rotate logs weekly, this can be changed to daily rotation with:

[FILE] **`/etc/logrotate.conf`Switch to daily log rotation**

    #weekly
    daily

** Tip**\
The default rotate count is **4**, this should be adjusted if *daily* rotation is used, unless only 4 days of logs are desired.

** Tip**\
To schedule removal of old logs add the line `maxage N` to the config file, where `N` is the number of days after which the log file will be deleted.

** Note**\
Leaving the logrotate script in [/etc/cron.daily] is recommended, as `weekly` configuration will stop [logrotate] from doing anything more than once a week, despite being called more often. This is especially useful when different components need to be rotated more or less often.

#### [Portage logrotate module]

To rotate log files created by portage:

[FILE] **`/etc/logrotate.d/portage`**

    # /etc/logrotate.d/portage

    /var/log/emerge-fetch.log

    /var/log/emerge.log

    /var/log/portage/*.log

** Note**\
This module inherits configuration from [/etc/logrotate.conf].

** Note**\
`copytruncate` will copy the file contents, then empty the file. This is useful when permissions prevent new files from being created.

## [Usage]

Logrotate is typically called by a cron job, but can be manually used with:

`root `[`#`]`logrotate --verbose /etc/logrotate.conf`

** Tip**\
Rotation can be forced with `--force`.

## [See also]

-   [Rsyslog](https://wiki.gentoo.org/wiki/Rsyslog "Rsyslog") --- open source system for high performance log processing.
-   [Sysklogd](https://wiki.gentoo.org/wiki/Sysklogd "Sysklogd") --- utility that reads and logs messages to the system console, logs files, other machines and/or users as specified by its configuration file.
-   [Syslog-ng](https://wiki.gentoo.org/wiki/Syslog-ng "Syslog-ng") --- a powerful, highly configurable monitoring and logging daemon.