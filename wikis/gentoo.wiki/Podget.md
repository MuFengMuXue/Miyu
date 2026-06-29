[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Podget&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](http://podget.sourceforge.net/)

[[]][Official documentation](http://podget.sourceforge.net/docs.php)

[[]][Package information](https://packages.gentoo.org/packages/media-sound/podget)

[[]][GitHub](https://github.com/dvehrs/podget)

[[]][Bugs (upstream)](https://github.com/dvehrs/podget/issues)

[podget] is a simple [podcast](https://en.wikipedia.org/wiki/podcast "wikipedia:podcast") aggregator optimized for running as a scheduled job written in [Bash](https://wiki.gentoo.org/wiki/Bash "Bash"). Despite its size and complexity podget only has two significant dependencies: [[wget](https://wiki.gentoo.org/wiki/Wget "Wget")] and [[iconv](https://wiki.gentoo.org/index.php?title=Iconv&action=edit&redlink=1 "Iconv (page does not exist)")]. It supports downloading media from the following feed types:

-   RSS.
-   ATOM.
-   iTunes PCAST.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Scheduled Task]](#Scheduled_Task)
        -   [[3.1.1] [cron]](#cron)
        -   [[3.1.2] [systemd]](#systemd)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)

## [Installation]

### [Emerge]

Install [[[media-sound/podget]](https://packages.gentoo.org/packages/media-sound/podget)[]]:

`root `[`#`]`emerge --ask media-sound/podget`

## [Configuration]

Configuration is mostly handled through the [podgetrc] and [serverlist] files located in the user\'s home directory. It\'s also possible to override the defaults set in these files via command line switches at runtime.

### [Files]

-   [\~/.podget/podgetrc] --- the configuration file location for podget.
-   [\~/.podget/serverlist] --- the list of podcast feeds by URL, category, and podcast name.
-   [\~/POD/] --- the default location where podget drops fetched podcast media.

Unfortunately, podget does not obey [XDG](https://wiki.gentoo.org/wiki/XDG "XDG") paths by default. For the configuration file, it\'s possible to fake support for XDG paths by passing [podget \--config \$/podget/podgetrc]; assuming the file already exists. In order to redirect podget to do the same with the [serverlist] file, the option `config_serverlist`=`$/podget/serverlist` must be set the [podgetrc] file.

## [Usage]

Typically [podget] is run in the background via task scheduler such as a [[cron](https://wiki.gentoo.org/wiki/Cron "Cron")] task or [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") timer.

### [Scheduled Task]

#### [cron]

A typical [crontab] file to periodically run podget might include something like this:

[FILE] **`/etc/crontab`Example crontab entry**

    [...]
    # Get podcasts daily
    02 15 * * * /usr/bin/podget --silent

The above fetches podcast media files at 02:15. The `--silent` option is required to suppress output.

#### [systemd]

The first step is to create a unit file to tell systemd what to run:

[FILE] **`podget.service`**

    [Unit]
    Description=A service for fetching podcast media.

    [Service]
    Type=simple
    ExecStart=/usr/bin/podget --silent

    [Install]
    WantedBy=default.target

With the unit file created it\'s time to create the timer file to tell systemd when to run the podget service.

[FILE] **`podget.timer`**

    [Unit]
    Description=Fetch podcast media once per day.

    [Timer]
    Persistent=true
    OnCalendar=*-*-* 02:15:00
    Unit=podget.service

    [Install]
    WantedBy=timers.target

Similar to the cron example the above systemd example fetches podcast media at 02:15. If the server is not online at 02:15 then the media is fetched the next time the server comes up.

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose media-sound/podget`

## [See also]

-   [wget](https://wiki.gentoo.org/wiki/Wget "Wget") --- a robust non-interactive [HTTP](https://en.wikipedia.org/wiki/HTTP "wikipedia:HTTP"), [HTTPS](https://en.wikipedia.org/wiki/HTTPS "wikipedia:HTTPS"), and [FTP](https://en.wikipedia.org/wiki/FTP "wikipedia:FTP") client