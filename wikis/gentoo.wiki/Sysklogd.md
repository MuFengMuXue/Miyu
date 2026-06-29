**Resources**

[[]][Home](https://troglobit.com/sysklogd.html)

[[]][Package information](https://packages.gentoo.org/packages/app-admin/sysklogd)

[[]][Guide](https://wiki.gentoo.org/wiki/Security_Handbook/Logging#Sysklogd.2FGuide "Security Handbook/Logging")

[[]][GitHub](https://github.com/troglobit/sysklogd/)

[[]][Bugs (upstream)](https://github.com/troglobit/sysklogd/issues)

[[]][syslogd(8)](https://man.troglobit.com/man8/syslogd.8.html)

[[]][syslogd.conf(5)](https://man.troglobit.com/man5/syslog.conf.5.html)

[[]][[#troglobit](ircs://irc.libera.chat/#troglobit)] ([[webchat](https://web.libera.chat/#troglobit)])

[[]][Blog](https://troglobit.com/sysklogd.html)

**syslogd** --- log systems messages, utility that reads and logs messages to the system console, logs files, other machines and/or users as specified by its configuration file.

Syslogd supports RFC5424 and RFC3164 style log messages for both local and remote logging using Internet and UNIX domain sockets.

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
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [Troubleshooting]](#Troubleshooting)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [app-admin/sysklogd](https://packages.gentoo.org/packages/app-admin/sysklogd) [[]] [Standard log daemons]

  --------------------------------------------------------------- ---------------------------------------------------------------------------
  [`logger`](https://packages.gentoo.org/useflags/logger)         Build the logger program
  [`logrotate`](https://packages.gentoo.org/useflags/logrotate)   use app-admin/logrotate for rotating logs rather than custom cron scripts
  --------------------------------------------------------------- ---------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-09-02 17:00] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[app-admin/sysklogd]](https://packages.gentoo.org/packages/app-admin/sysklogd)[]]:

`root `[`#`]`emerge --ask app-admin/sysklogd`

** Warning**\
It is a bad idea to run more than one system logger on a physical host. Other local loggers should be removed or disabled.

## [Configuration]

### [Files]

-   [/etc/conf.d/syslogd] - Gentoo\'s config file for /etc/init.d/sysklogd daemon. See man syslogd for options.
-   [/etc/syslog.conf] - Global (system wide) configuration file. See syslog.conf(5) for more information.
-   [/etc/syslog.d/\*.conf] - Conventional sub-directory of .conf files read by syslogd.
-   [/etc/syslog.d/10-remote-logging.conf] - Conventional filename for additional configuration rules.

### [Service]

#### [OpenRC]

Add the sysklog daemon to the default runlevel so that logging starts on system boot:

`root `[`#`]`rc-update add sysklogd default`

Start sysklogd by running:

`root `[`#`]`rc-service sysklogd start`

Verify file [/var/log/messages] for current syslog entries:

`root `[`#`]`tail -f /var/log/messages`

    Mar  6 11:33:59 node syslogd[14000]: syslogd v2.3.0: restart.

#### [runit]

#### [systemd]

Enable sysklogd to start logging on boot:

`root `[`#`]`systemctl enable sysklogd`

Or to start sysklogd immediately:

`root `[`#`]`systemctl start sysklogd`

Verify current syslog entries in [/var/log/messages]:

`root `[`#`]`tail -f /var/log/messages`

    Jan  1 11:11:11 node syslogd[14000]: syslogd v2.3.0: restart.

** Important**\
In case Portage doesn\'t provide service unit file, visit: [systemd custom unit files](https://wiki.gentoo.org/wiki/Systemd#Installing_custom_unit_files "Systemd").

### [Local logging]

Default daemon running options:

-   [-m 0] disable Interval between MARK messages
-   [-s] Operate in secure mode, do not log messages from remote machines. If specified twice, no socket at all will be opened, which also disables support for logging to remote machines.

[FILE] **`/etc/conf.d/sysklogd`Default daemon running options**

    # Config file for /etc/init.d/sysklogd

    SYSLOGD="-m 0 -s -s"

Default syslog.conf configuration file:

[FILE] **`/etc/syslog.conf`Default configuration options**

    auth,authpriv.*                  /var/log/auth.log
    *.*;auth,authpriv.none          -/var/log/syslog

    kern.*                          -/var/log/kern.log
    mail.*                          -/var/log/mail.log

    mail.err                         /var/log/mail.err

    *.=info;*.=notice;*.=warn;\
            auth,authpriv.none;\
            cron,daemon.none;\
            mail,news.none          -/var/log/messages

    *.=emerg                        *

    include /etc/syslog.d/*.conf

At this point the installation is finished and everything will work for local event logging.

### [Remote logging]

Remote logging setup is optional. In the default configuration the sysklogd daemon will not send or receive any syslog messages via IP. Gentoo\'s [/etc/conf.d/sysklogd] configuration file need to be adjusted for the server and client.

#### [Server]

To enable the syslog server to listen for incoming syslog messages edit [/etc/conf.d/sysklogd] as follows:

[FILE] **`/etc/conf.d/sysklogd`Syslog server daemon running options**

    # Config file for /etc/init.d/sysklogd

    SYSLOGD="-m 0 -b 192.0.2.1:514"

The IP `192.0.2.1` address is a local server interface, where sysklogd will bind the service to.

Restart the sysklogd daemon:

`root `[`#`]`rc-service sysklogd restart`

Verify if the service is running and bound to the correct interface by running:

`root `[`#`]`ss -tulpn | grep syslog`

    udp   UNCONN 0      0        192.0.2.1:514      0.0.0.0:*    users:(("syslogd",pid=20175,fd=6))

#### [Client]

To enable the syslog client to send syslog messages, edit [/etc/conf.d/sysklogd] as follows:

[FILE] **`/etc/conf.d/sysklogd`Syslog client daemon running options**

    # Config file for /etc/init.d/sysklogd

    SYSLOGD="-m 0"

Additional client configuration files should be stored in the [/etc/syslog.d/] directory. Files using the `*.conf` suffix get active, after a restart of the sysklogd daemon.

This rule redirects all messages to syslog server `192.0.2.1` using RFC5424 style formatting. Create the following file:

[FILE] **`/etc/syslog.d/10-remote-logging.conf`**

    *.*          @192.0.2.1                    ;RFC5424

This example rule redirects all messages to syslog server `2001:db8::1` using RFC3164 syslog formatting. Create the following file:

[FILE] **`/etc/syslog.d/11-remote-ipv6-logging.conf`**

    *.*          @2001:db8::1                  ;RFC3164

** Note**\
The syslog option which RFC logging format is to be used to send messages, is set by the `;RFC5424` or `;RFC3164`

Restart the sysklogd daemon on the client:

`root `[`#`]`rc-server sysklogd restart`

## [Usage]

For further configuration options read the syslog.conf man page

`user `[`$`]`man syslog.conf`

Further examples regarding the syslog configuration read [Rsyslog](https://wiki.gentoo.org/wiki/Rsyslog "Rsyslog") following sections about Facility, Severity and Filtering. Read the [RFC5424 Section 6.2.1](https://datatracker.ietf.org/doc/html/rfc5424#section-6.2.1).

### [Invocation]

`user `[`$`]`syslogd -?`

    Usage:
      syslogd [-468AdFHKknsTtv?] [-a PEER] [-b NAME] [-f FILE] [-m INTERVAL]
                                 [-P PID_FILE] [-p SOCK_PATH] [-r SIZE[:NUM]]
    Options:
      -4        Force IPv4 only
      -6        Force IPv6 only
      -8        Allow all 8-bit data, e.g. unicode, does not affect control chars
      -A        Send to all addresses in DNS A, or AAAA record
      -a PEER   Allow PEER to use us as a remote syslog sink. Ignored when started
                with -s. Multiple -a options may be specified:
                  ipaddr[/len][:port]   Accept messages from 'ipaddr', which may
                                        be IPv4 or IPv6 if enclosed with '[' and
                                        ']'.  The optional port may be a service
                                        name or a port number
                  domainname[:port]     Accept messages where the reverse address
                                        lookup yields 'domainname' for the sender
                                        address.  'domainname' may contain special
                                        shell-style pattern characters like '*'

      -b NAME   Bind to a specific address and/or port. Multiple -b options may be
                specified. Default is to listen on all interfaces on UDP port 514,
                unless also started with -s:
                  address[:port]        Hostname or IP address, IPv6 addresses
                                        must be enclosed in '[' and ']'
                  :port                 UDP port number, or service name
                                        default: 'syslog', port 514

      -C FILE   File to cache last read kernel seqno, default: /run/syslogd.cache
                Note: syslogd relies on this file being removed at system reboot.
      -d        Enable debug mode, implicitly enables -F to prevent backgrounding
      -F        Run in foreground, required when monitored by init(1)
      -f FILE   Alternate .conf file, default: /etc/syslog.conf
      -H        Use hostname from message instead of address for remote messages
      -K        Disable kernel logging, useful in container use-cases
      -k        Allow logging with facility 'kernel', otherwise remapped to 'user'
      -m MINS   Interval between MARK messages, 0 to disable, default: 20 min
      -n        Disable DNS query for every request
      -P FILE   File to store the process ID, default: /run/syslogd.pid
      -p PATH   Path to UNIX domain socket, multiple -p create multiple sockets.
                Default, if no -p argument is given: /dev/log
      -r S[:R]  Enable log rotation. The size argument (S) takes k/M/G qualifiers,
                e.g. 2M for 2 MiB.  The optional rotations argument default to 5.
                Rotation can also be defined per log file in /etc/syslog.conf
      -s        Operate in secure mode, do not log messages from remote machines.
                If specified twice, no socket at all will be opened, which also
                disables support for logging to remote machines.
      -t        Keep kernel timestamp, even after initial ring buffer emptying
      -T        Use local time and date for messages received from remote hosts
      -?        Show this help text
      -v        Show program version and exit

    Bug report address: https://github.com/troglobit/sysklogd/issues
    Project home page:  https://github.com/troglobit/sysklogd

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-admin/sysklogd`

## [Troubleshooting]

Check if a sysklogd daemon is running :

`user `[`$`]`ps ax | grep syslogd`

    21390 ?        Ss     0:00 /usr/sbin/syslogd -F -m 0

Verify correct network configuration running on the syslog server:

`root `[`#`]`ss -tulpn | grep sys`

    udp   UNCONN 0      0        192.0.2.1:514       0.0.0.0:*    users:(("syslogd",pid=21695,fd=6))

Verify using the command [logger] on the client to send a test syslog message:

`user `[`$`]`logger -t test my syslog-test-message`

Following message will appear in the [/var/log/messages] file, on the syslog server when syslogd is configured properly:

`root `[`#`]`tail /var/log/messages`

    ...
    Mar  6 13:08:20 192.0.2.10 test: my syslog-test-message

## [See also]

-   [Metalog](https://wiki.gentoo.org/wiki/Metalog "Metalog") --- an alternative syslog daemon
-   [Rsyslog](https://wiki.gentoo.org/wiki/Rsyslog "Rsyslog") --- open source system for high performance log processing.
-   [Syslog-ng](https://wiki.gentoo.org/wiki/Syslog-ng "Syslog-ng") --- a powerful, highly configurable monitoring and logging daemon.

## [External resources]

-   [Wikipedia\'s article about the Syslog protocol](https://en.wikipedia.org/wiki/Syslog)
-   [RFC 5424 - The Syslog Protocol](https://tools.ietf.org/html/rfc5424)
-   [RFC 3164 - The BSD syslog Protocol](https://tools.ietf.org/html/rfc3164)