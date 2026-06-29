**Resources**

[[]][Home](http://metalog.sourceforge.net/)

[[]][Official documentation](http://metalog.sourceforge.net/README)

[[]][Package information](https://packages.gentoo.org/packages/app-admin/metalog)

[[]][GitHub](https://github.com/hvisage/metalog)

[[]][Bugs (upstream)](https://github.com/hvisage/metalog/issues)

**Metalog** is an alternative syslog daemon, which is simple to configure, accepts an unlimited number of rules, and has (switchable) memory bufferization for maximal performance.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Service]](#Service)
        -   [[2.2.1] [OpenRC]](#OpenRC)
        -   [[2.2.2] [runit]](#runit)
        -   [[2.2.3] [systemd]](#systemd)
    -   [[2.3] [Local logging]](#Local_logging)
    -   [[2.4] [Remote logging]](#Remote_logging)
        -   [[2.4.1] [Server]](#Server)
        -   [[2.4.2] [Client]](#Client)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Filtering]](#Filtering)
    -   [[3.2] [Invocation]](#Invocation)
-   [[4] [Caveats]](#Caveats)
-   [[5] [Troubleshooting]](#Troubleshooting)
-   [[6] [Removal]](#Removal)
    -   [[6.1] [Unmerge]](#Unmerge)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)
-   [[9] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [app-admin/metalog](https://packages.gentoo.org/packages/app-admin/metalog) [[]] [Highly configurable replacement for syslogd/klogd]

  ----------------------------------------------------------- ----------------------------------
  [`unicode`](https://packages.gentoo.org/useflags/unicode)   Add support for Unicode
  [`zlib`](https://packages.gentoo.org/useflags/zlib)         Add support for zlib compression
  ----------------------------------------------------------- ----------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-05 07:37] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[app-admin/metalog]](https://packages.gentoo.org/packages/app-admin/metalog)[]]:

`root `[`#`]`emerge --ask app-admin/metalog`

** Warning**\
It is a bad idea to run more than one system logger on a physical host. Other local loggers should be removed or disabled.

## [Configuration]

Metalog documentation:

    [...]
    A configuration file should be installed. Its default location is
    /etc/metalog.conf (unless you tweaked --with-sysconfdir) . You can find a
    sample file in this directory, but it's certainly not perfect for your system
    and your needs. So read on.
    [...]

### [Files]

-   [/etc/conf.d/metalog] - Gentoo\'s config file for /etc/init.d/metalog daemon. Refer to the [[[metalog(8)]](https://man.archlinux.org/man/metalog.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page for running options.
-   [/etc/metalog.conf] - Global (system wide) configuration file. Refer to the [[[metalog.conf(5)]](https://man.archlinux.org/man/metalog.conf.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page for more information.

### [Service]

#### [OpenRC]

Add the metalog daemon to the default runlevel so that logging starts on system boot:

`root `[`#`]`rc-update add metalog default`

Start metalog by running:

`root `[`#`]`rc-service metalog start`

Verify [/var/log/everything/current] for recent syslog entries:

`root `[`#`]`tail -f /var/log/everything/current`

#### [runit]

#### [systemd]

### [Local logging]

Shortest catchall one file logging example. Verify the logfile definitions at the beginning:

-   logfile maximal filesize **maxsize**
-   logfile rotation frequency **maxtime** f.e. daily, weekly,
-   logfile maximal count of files within logging directory **maxfiles**

[FILE] **`/etc/metalog.conf`Most simple metalog confguration example.**

    # Most simple Metalog configuration file:
    maxsize  = 1048576  # size in bytes (1048576 = 1 megabyte)
    maxtime  = 86400    # time in seconds (86400 = 1 day)
    maxfiles = 5        # num files per directory

    Everything important :

        facility = "*"
        minimum  = 7
        logdir   = "/var/log/everything"

### [Remote logging]

#### [Server]

Using app-admin/metalog-20220214 version:

** Note**\
No option to run metalog server listening for incoming syslog messages from sending clients.

#### [Client]

To enable sending syslog messages to remote syslog server add following entries to the [/etc/metalog] configuration file:

    remote_host=192.0.2.1
    remote_port=514

This rule sends all messages to remote syslog server `192.0.2.1` using target port `514`.

[FILE] **`/etc/metalog.conf`Remote syslog server messages sending example.**

    # Most simple Metalog configuration file:
    maxsize  = 1048576  # size in bytes (1048576 = 1 megabyte)
    maxtime  = 86400    # time in seconds (86400 = 1 day)
    maxfiles = 5        # num files per directory

    # Configure sending syslog messages to a remote syslog server
    remote_host = 192.0.2.1
    remote_port = 514

    # Catchall syslog messages
    Everything important :

        facility = "*"
        minimum  = 7
        logdir   = "/var/log/everything"

## [Usage]

All syslog messages are stored in the [/var/log/everything/current] file.

### [Filtering]

** Note**\
Read the [RFC5424 Section 6.2.1](https://datatracker.ietf.org/doc/html/rfc5424#section-6.2.1). about Facility and Severity

Incoming syslog messages can be filtered using following criteria:

-   facilities f.e.: (*local0, kernel*)
-   urgency levels, this is called **severity** in the syslog RFC\'s f.e: (*0-7*)
-   program names f.e.: (*\^httpd*)
-   regular expressions f.e.: (*simple regex example needed*)

An incoming message will pass through all filters. If **all** conditions match, actions defined for the section are performed.

To write matched syslog messages to its logfile only, without additionally writing in the catch-all syslog file use following at the end of the filter definition:

     break = 1

Simple filter example configuration using the syslog facility to sort incoming messages to dedicated directories:

-   **auth** facility to [/var/log/auth] directory only
-   **kern** facility to [/var/log/kern] directory only
-   **mail** facility to [/var/log/mail] directory only
-   everything else not matched to [/var/log/everything] directory

The resulting metalog configuration file:

[FILE] **`/etc/metalog.conf`Simple filtering example using facilities**

    # Most simple Metalog configuration file:
    maxsize  = 1048576  # size in bytes (1048576 = 1 megabyte)
    maxtime  = 86400    # time in seconds (86400 = 1 day)
    maxfiles = 5        # num files per directory

    # matched on the authentication facility to the auth directory
    Authentication:

        facility = "auth"
        logdir   = "/var/log/auth"
        break    = 1

    # matched on the kernel facility to the kern directory
    Kernel:
        facility = "kern"
        logdir   = "/var/log/kern"
        break    = 1

    # matched on the mail facility to the mail directory
    Mail:
        facility = "mail"
        logdir   = "/var/log/mail"
        break    = 1

    #  matched on all facilities, with all severities save to the everything directoy
    Everything important :

        facility = "*"
        minimum  = 7
        logdir   = "/var/log/everything"

### [Invocation]

`user `[`$`]`metalog --help`

    metalog version 4

    Options:
       -a, --async
       -B, --daemonize
       -c, --consolelevel <opt>
       -C, --configfile <opt>
       -g, --group <opt>
       -h, --help
       -N, --no-kernel
       -p, --pidfile <opt>
       -s, --synchronous
       -s, --sync
       -v, --verbose
       -V, --version

## [Caveats]

Though metalog provides for log rotation, this facility does not deal with the unowned files [/var/log/wtmp] or [/var/log/btmp] (used to keep track of all logins and logouts to a system). To deal with such files, see [[[app-admin/logrotate]](https://packages.gentoo.org/packages/app-admin/logrotate)[]].

## [Troubleshooting]

Check if a metalog daemon is running :

`user `[`$`]`ps ax | grep metalog`

     7753 ?        Ss     0:00 metalog [MASTER]
     7754 ?        S      0:00 metalog [KERNEL]

Verify using the command [logger] on the client to send a test syslog message:

`user `[`$`]`logger -t test my syslog-test-message`

Following message will appear in the [/var/log/everything/current] file, on the syslog server when metalog is configured properly:

`root `[`#`]`tail /var/log/everything/current`

    ...
    Jun 17 20:22:46 [test] my syslog-test-message

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-admin/metalog`

## [See also]

-   [Logging](https://wiki.gentoo.org/wiki/Logging "Logging") --- the process by which systems record notable events to provide users and administrators with a view of what is happening while a machine is running.
-   [Metalog (Security Handbook)](https://wiki.gentoo.org/wiki/Security_Handbook/Logging#Metalog "Security Handbook/Logging") - The system logging with Metalog is covered in the [Security Handbook](https://wiki.gentoo.org/wiki/Security_Handbook "Security Handbook").
-   [Rsyslog](https://wiki.gentoo.org/wiki/Rsyslog "Rsyslog") --- open source system for high performance log processing.
-   [Sysklogd](https://wiki.gentoo.org/wiki/Sysklogd "Sysklogd") --- utility that reads and logs messages to the system console, logs files, other machines and/or users as specified by its configuration file.
-   [Syslog-ng](https://wiki.gentoo.org/wiki/Syslog-ng "Syslog-ng") --- a powerful, highly configurable monitoring and logging daemon.

## [External resources]

## [References]