**supervise-daemon**

[[]][Home](https://github.com/OpenRC/openrc/blob/master/supervise-daemon-guide.md)

[[]][Man page](http://manpages.org/supervise-daemon/8)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/openrc)

Supervise-daemon is OpenRC\'s daemon supervisor. It can start, stop and restart system processes when they terminate unexpectedly.

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [General recipe]](#General_recipe)
-   [[3] [Instructions per service]](#Instructions_per_service)
    -   [[3.1] [acpid]](#acpid)
    -   [[3.2] [avahi-daemon]](#avahi-daemon)
    -   [[3.3] [bluetoothd]](#bluetoothd)
    -   [[3.4] [cronie]](#cronie)
    -   [[3.5] [cupsd]](#cupsd)
    -   [[3.6] [cups-browsed]](#cups-browsed)
    -   [[3.7] [dbus-daemon]](#dbus-daemon)
    -   [[3.8] [dhcpcd]](#dhcpcd)
    -   [[3.9] [dnsmasq]](#dnsmasq)
    -   [[3.10] [fancontrol]](#fancontrol)
    -   [[3.11] [fcron]](#fcron)
    -   [[3.12] [gerbera]](#gerbera)
    -   [[3.13] [irqbalance]](#irqbalance)
    -   [[3.14] [iwd]](#iwd)
    -   [[3.15] [metalog]](#metalog)
    -   [[3.16] [mpd]](#mpd)
    -   [[3.17] [ntpd]](#ntpd)
    -   [[3.18] [rngd]](#rngd)
    -   [[3.19] [sshd]](#sshd)
    -   [[3.20] [syslog-ng]](#syslog-ng)
    -   [[3.21] [tor]](#tor)
    -   [[3.22] [vixie-cron]](#vixie-cron)
-   [[4] [Services which won\'t run under a supervisor]](#Services_which_won.27t_run_under_a_supervisor)
    -   [[4.1] [One shot services]](#One_shot_services)
    -   [[4.2] [netifrc]](#netifrc)
    -   [[4.3] [dcron]](#dcron)
    -   [[4.4] [libvirtd]](#libvirtd)
-   [[5] [Tips \'n tricks]](#Tips_.27n_tricks)
    -   [[5.1] [rc-status]](#rc-status)
-   [[6] [External resources]](#External_resources)

## [Introduction]

OpenRC traditionally uses [start-stop-daemon], often abbreviated to **s-s-d** for starting and stopping programs. When s-s-d starts a process it saves the process\' PID somewhere on permanent storage (typically under [/run/]), and backgrounds (daemonizes) the process it started. When the time comes to stop, kill, or signal the daemon process s-s-d will use the saved PID file to find the right process.

Supervising on the other hand usually keeps the started daemon as a child process of the supervisor. Backgrounding the daemon is therefore not needed, and not desired. Pidfiles are still used however. They will store the PID of the supervisor process so that it can receive start/stop signals.

Supervising daemon process has a few major advantages:

1.  If and when a daemon process dies (crashes) then its supervisor will notice it and try to restart it.
2.  Any terminal output sent by the daemon process to stdout and stderr can be caught by the supervisor, and then sent to the system logger or to a file.

This article aims to provide help how to bring services under its supervision.

## [General recipe]

Currently, standard Gentoo init files do not use process supervision with supervise-daemon yet: it is left to users to make these modifications to the init files.

The general recipe to bring a service under the control of supervise-daemon is to adapt its init file in [/etc/init.d] as follows:

-   always add `supervisor="supervise-daemon"`
-   remove any pidfile reference that the command would create. supervise-daemon needs a pidfile for itself. e.g. :
    -   change `command_args="-p $ $"` into `command_args="$" command_args_background="-p $"`
-   make sure the daemon will run in foreground by applying one of the following methods:
    -   if the daemon forks itself to the background (daemonizes itself) then pass the appropriate daemon command line option, e.g. `command_args_foreground="--foreground"`. Note that the command line option to prevent daemonizing is different per service, and some services might not even provide this option.
    -   if there is a command line parameter for the daemon process to make it daemonize itself, then move it to `command_args_background`
-   replace calls to `start-stop-daemon`and if needed with calls to `$` as appropriate.

## [Instructions per service]

This chapter contains some examples on how to bring a service\' daemon process under supervision.

### [acpid]

Reviewing the man page of [acpid] reveals:

-   *.. will run as background process ..*
-   *.. -f, \--foreground .. keeps acpid in the foreground by not forking at startup, and makes it log to stderr instead of syslog.*

Edit [/etc/init.d/acpid] as follows to make acpid run under supervise-daemon:

-   add the supervisor definition
-   add the arguments to make acpid run in foreground
-   rewrite the s-s-d command to a supervisor-daemon command
-   Add a pidfile for supervise-daemon to track the service

At the top of the file:

[FILE] **`/etc/init.d/acpid`**

    supervisor="supervise-daemon"
    command_args_foreground="--foreground"
    pidfile="/run/acpid.pid"

At the end of the file:

[FILE] **`/etc/init.d/acpid`**

    reload()  $ --signal HUP --pidfile "$"
            eend $?
    }

Start up the service:

`root `[`#`]`rc-service acpid start`

    acpid                  | * Starting acpid ...                           [ ok ]

Verify if acpid is now running under supervise-daemon:

`root `[`#`]`ps -ef | grep acpid `

    root      7450     1  0 15:32 ?        00:00:00 supervise-daemon acpid --start /usr/sbin/acpid -- --foreground
    root      7454  7450  0 15:32 ?        00:00:01 /usr/sbin/acpid --foreground

Check the logs as well:

`root `[`#`]`tail /var/log/messages`

    Jun 10 09:10:27 [supervise-daemon] Supervisor command line: supervise-daemon acpid --start /usr/sbin/acpid -- --foreground
    Jun 10 09:10:27 [supervise-daemon] Child command line: /usr/sbin/acpid --foreground

And when you create an acpid event, it will be logged:

`root `[`#`]`tail /var/log/messages`

    Jun 10 09:15:08 [user] ACPI event unhandled: button/mute MUTE 00000080 00000000 K

Lastly, check if supervise-daemon will restart acpid when it terminates:

`root `[`#`]`kill 7454 `

`root `[`#`]`tail /var/log/messages`

    Jun 10 09:54:20 [supervise-daemon] /usr/sbin/acpid, pid 7454, exited with return code 0
    Jun 10 09:54:20 [supervise-daemon] Child command line: /usr/sbin/acpid --foreground

`root `[`#`]`ps -ef | grep acpid `

    root      7450     1  0 15:32 ?        00:00:00 supervise-daemon acpid --start /usr/sbin/acpid -- --foreground
    root      8931  7450  0 15:32 ?        00:00:01 /usr/sbin/acpid --foreground

Notice the different PID.

### [avahi-daemon]

[[[net-dns/avahi]](https://packages.gentoo.org/packages/net-dns/avahi)[]] contains a service *avahi-daemon* for service discovery. Its init file [/etc/init.d/avahi-daemon] does not make use of s-s-d, but calls the binary [/usr/sbin/avahi-daemon] directly and gives it the instruction to daemonize: `/usr/sbin/avahi-daemon -D` on startup. This can be simply adjusted by defining the command variable as `command="/usr/sbin/avahi-daemon"`, and removing the start and stop functions from the file. Of course it is also needed to specify the supervisor.

Edit [/etc/init.d/avahi-daemon] as follows:

[FILE] **`/etc/init.d/avahi-daemon`**

    #!/sbin/openrc-run
    # Copyright 1999-2016 Gentoo Foundation
    # Distributed under the terms of the GNU General Public License v2

    extra_started_commands="reload"
    command="/usr/sbin/avahi-daemon"
    supervisor="supervise-daemon"

    depend()

    #start()
    #
    #stop()

    reload()  -r
           eend $?
    }

Start the service back up:

`root `[`#`]`rc-service avahi-daemon start`

    avahi-daemon           | * Caching service dependencies ...                              [ ok ]
    avahi-daemon           | * Starting avahi-daemon ...                                     [ ok ]

Verify that the service is now supervised:

`root `[`#`]`ps -ef | grep avahi`

    root     27390     1  0 10:30 ?        00:00:00 supervise-daemon avahi-daemon --start /usr/sbin/avahi-daemon --
    avahi    27392 27390  0 10:30 ?        00:00:00 avahi-daemon: running [e485.local]
    avahi    27397 27392  0 10:30 ?        00:00:00 avahi-daemon: chroot helper

### [bluetoothd]

[[[net-wireless/bluez]](https://packages.gentoo.org/packages/net-wireless/bluez)[]] provides [Bluetooth](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth") services. The recipe to bring it under supervise-daemon is as follows:

The existing service is written to easily switch supervisors. Define the supervisor in conf.d

Edit [/etc/conf.d/bluetooth] as follows:

[FILE] **`/etc/conf.d/bluetooth`**

    supervisor="supervise-daemon"

### [cronie]

[[[sys-process/cronie]](https://packages.gentoo.org/packages/sys-process/cronie)[]] is a [Cron](https://wiki.gentoo.org/wiki/Cron "Cron") and anacron implementation.

The existing service is written to easily switch supervisors. Define the supervisor in conf.d and run it in foreground mode

[FILE] **`/etc/conf.d/cronie`**

    supervisor="supervise-daemon"
    CRONDARGS="-f"

### [cupsd]

[CUPS](https://wiki.gentoo.org/wiki/CUPS "CUPS") is the well known printing system of Linux. Its daemon *cupsd* is provided by [[[net-print/cups]](https://packages.gentoo.org/packages/net-print/cups)[]].

The existing service is written to easily switch supervisors. Define the supervisor in conf.d:

[FILE] **`/etc/conf.d/cupsd`**

    supervisor="supervise-daemon"

### [cups-browsed]

Cups-browsed is a daemon for browsing the Bonjour broadcasts of shared, remote CUPS printers.

The existing service is written to easily switch supervisors. Define the supervisor in conf.d:

[FILE] **`/etc/conf.d/cups-browsed`**

    supervisor="supervise-daemon"

### [dbus-daemon]

[D-Bus](https://wiki.gentoo.org/wiki/D-Bus "D-Bus") is a message bus system, a simple way for applications to talk to one another. It can be brought under supervise-daemon like any other service.

** Warning**\
When D-BUS is stopped the system or desktop may become unstable. Best to restart the system after editing the init file.

Edit [/etc/conf.d/dbus] as follows:

[FILE] **`/etc/conf.d/dbus`**

    supervisor="supervise-daemon"
    command_args_foreground="--nofork --nopidfile"

### [dhcpcd]

DHCPCD, the Dynamic Host Configuration Protocol Client Daemon is a popular DHCP client capable of handling both IPv4 and IPv6 configurations.

Take the following steps to have it run under supervise daemon:

-   pass the dhcpcd process option `--nobackground` to prevent it from backgrounding.

Edit [/etc/conf.d/dhcpcd] as follows:

[FILE] **`/etc/conf.d/dhcpcd`**

    supervisor="supervise-daemon"
    command_args_foreground="--nobackground"

### [dnsmasq]

[Dnsmasq](https://wiki.gentoo.org/wiki/Dnsmasq "Dnsmasq"), provided by package [[[net-dns/dnsmasq]](https://packages.gentoo.org/packages/net-dns/dnsmasq)[]], is a lightweight DHCP and caching DNS server. Dnsmasq\'s init file contains references to s-s-d. The daemon needs to be configured to run in foreground.

Edit [/etc/init.d/dnsmasq] as follows:

[FILE] **`/etc/init.d/dnsmasq`**

    pidfile="/var/run/dnsmasq.pid"
    command="/usr/sbin/dnsmasq"
    command_args_background="-x $"
    command_args="$"
    command_args_foreground="--keep-in-foreground"
    supervisor="supervise-daemon"
    retry="TERM/3/TERM/5"

    depend()

    start_pre()

    reload() "
    #       start-stop-daemon --signal HUP --pidfile "$"
            $ $ --signal HUP --pidfile "$"
            eend $?
    }

    rotate()  log file"
    #       start-stop-daemon --signal USR2 --pidfile "$"
            $ $ --signal USR2 --pidfile "$"
            eend $?
    }

### [fancontrol]

Fancontrol is a bash script provided by [[[sys-apps/lm-sensors]](https://packages.gentoo.org/packages/sys-apps/lm-sensors)[]] to control the fan speed. It can be run as a service under supervision by editing [/etc/conf.d/fancontrol]:

The existing service is written to easily switch supervisors. Define the supervisor in conf.d:

[FILE] **`/etc/conf.d/fancontrol`**

    supervisor="supervise-daemon"

\

### [fcron]

[[[sys-process/fcron]](https://packages.gentoo.org/packages/sys-process/fcron)[]] is a cron daemon implementation. To get it supervised it is needed to:

-   define the supervisor
-   tell the supervisor how to get the daemon to run in foreground
-   change the reload function to use supervise-daemon instead of s-s-d.

Edit [/etc/init.d/fcron] as follows:

[FILE] **`/etc/init.d/fcron`**

    command="/usr/libexec/fcron"
    command_args="-c \"$\" $"
    start_stop_daemon_args=$
    pidfile="$(getconfig pidfile /run/fcron.pid)"
    fcrontabs="$(getconfig fcrontabs /var/spool/fcron)"
    fifofile="$(getconfig fifofile /run/fcron.fifo)"
    required_files="$"
    supervisor="supervise-daemon"
    command_args_foreground="--foreground"

    extra_started_commands="reload"

    reload() "
             $ "$" --signal HUP --pidfile "$"
    }

### [gerbera]

[[[net-misc/gerbera]](https://packages.gentoo.org/packages/net-misc/gerbera)[]] provides provides a UPnP MediaServer.

The existing service is written to easily switch supervisors. Define the supervisor in conf.d:

[FILE] **`/etc/conf.d/gerbera`**

    supervisor="supervise-daemon"

### [irqbalance]

[[[sys-apps/irqbalance]](https://packages.gentoo.org/packages/sys-apps/irqbalance)[]] requires some changes in conf.d:

[FILE] **`/etc/conf.d/irqbalance`**

    supervisor="supervise-daemon"
    IRQBALANCE_OPTS="-f"

### [iwd]

iwd (iNet wireless daemon) is provided by [[[net-wireless/iwd]](https://packages.gentoo.org/packages/net-wireless/iwd)[]] and aims to replace [[[net-wireless/wpa_supplicant]](https://packages.gentoo.org/packages/net-wireless/wpa_supplicant)[]].

The existing service is written to easily switch supervisors. Define the supervisor in conf.d:

[FILE] **`/etc/conf.d/iwd`**

    supervisor="supervise-daemon"

### [metalog]

[[[app-admin/metalog]](https://packages.gentoo.org/packages/app-admin/metalog)[]] comes with good init scripts that only require some basic modifications to become supervised, however there are a few quirks:

First, metalog will create its pidfile at a compiled-in default location even if the [\--pidfile] option is not specified. If the `pidfile` variable happens to be set to this same path, then metalog will overwrite it with the wrong pid, and OpenRC won\'t be able to stop the daemon. This can be fixed by specifying a pidfile at some other path that won\'t do any harm e.g. [/run/metametalog.pid].

**Note:** [/dev/null] should not be used as the pidfile because metalog will delete and re-create the file if it exists. As an alternative, the default pidfile could be left alone, and the pidfile location passed to supervise-daemon could be changed.

Second, under certain conditions it is possible for the metalog process to inherit the current tty as its [stdout]/[stderr]. Since metalog is programmed to always write the log messages to [stdout]/[stderr] in addition to the configured log files, this can result in a user\'s terminal filling up with system log messages. This can be fixed by telling `supervise-daemon` to redirect [stdout] and [stderr].

[FILE] **`/etc/init.d/metalog`**

    # Enable supervise-daemon
    supervisor="supervise-daemon"

    # Redirect stdout and stderr so log messages don't get routed to a tty
    supervise_daemon_args="--stdout /dev/null --stderr /dev/null"

    # Move daemonize and pidfile options out of the 'command_args' variable
    command_args="$"

    # Set pidfile depending on whether the daemon runs in foreground or background
    command_args_foreground="--pidfile /run/metametalog.pid"
    command_args_background="--daemonize --pidfile $"

Finally, ensure all calls to `start-stop-daemon` are replaced with calls to `$`

[FILE] **`/etc/init.d/metalog`**

    $ "$" --signal x --pidfile "$"

### [mpd]

Package [[[media-sound/mpd]](https://packages.gentoo.org/packages/media-sound/mpd)[]] provides a music player daemon. It can be brought under supervision by:

-   providing the foreground parameter \--no-daemon
-   declaring the supervisor
-   updating the reload function to use the supervior instead of the PID.

Edit [/etc/init.d/mpd] as follows:

[FILE] **`/etc/init.d/mpd`**

    extra_started_commands='reload'
    command=/usr/bin/mpd
    command_args=$
    required_files=$
    pidfile=$(get_config pid_file)
    description="Music Player Daemon"
    command_args_foreground="--no-daemon"
    supervisor="supervise-daemon"

    reload() "
    #      start-stop-daemon --pidfile $ --signal HUP
          $ $ --signal HUP --pidfile "$"
          eend $?
      }

### [ntpd]

The network time protocol daemon *ntpd*, from package [[[net-misc/ntp]](https://packages.gentoo.org/packages/net-misc/ntp)[]]. can be brought under supervision by editing the init file to:

-   prevent forking to background by adding \"-n\" to the command line to of the ntpd daemon,
-   remove the s-s-d instruction,
-   define the supervisor.

[FILE] **`/etc/init.d/ntpd`**

    pidfile="/var/run/ntpd.pid"
    command="/usr/sbin/ntpd"
    command_args_background="-p $"
    command_args="$"
    #start_stop_daemon_args="--pidfile $"
    supervisor="supervise-daemon"
    command_args_foreground="-n"

### [rngd]

Rngd is the daemon belonging to [[[sys-apps/rng-tools]](https://packages.gentoo.org/packages/sys-apps/rng-tools)[]]. It is meant to check and feed random data from a hardware device to the kernel random device.

Edit [/etc/conf.d/rngd] to bring it under supervision as follows:

[FILE] **`/etc/conf.d/rngd`**

    supervisor="supervise-daemon"
    command_args_foreground="--foreground"

### [sshd]

sshd (Secure Shell Daemon) does not have a specific command-line option to run in foreground, instead it is needed to use the `-D` debug option. There may be some more text logged.

Edit [/etc/init.d/sshd] at the beginning of the file as follows:

[FILE] **`/etc/init.d/sshd`**

    pidfile="$"
    command_args_background="-o PidFile=$"
    command_args="$ -f $"
    command_args_foreground="-D"
    supervisor="supervise-daemon"

    # Wait one second (length chosen arbitrarily) to see if sshd actually
    # creates a PID file, or if it crashes for some reason like not being
    # able to bind to the address in ListenAddress (bug 617596).
    #: $
    start_stop_daemon_args="$"

All the way at the bottom of the file there is the reload function in which the s-s-d instruction should be changed to a supervise-daemon instruction:

[FILE] **`/etc/init.d/sshd`**

    reload() "
    #       start-stop-daemon --signal HUP --pidfile "$"
            $ $ --signal HUP --pidfile "$"
            eend $?
    }

### [syslog-ng]

[[[app-admin/syslog-ng]](https://packages.gentoo.org/packages/app-admin/syslog-ng)[]] is an interesting case. Without any change, running syslog-ng under s-s-d it looks like this:

`root `[`#`]`ps -ef | grep syslog-ng`

    root      7800     1  0 09:16 ?        00:00:00 supervising syslog-ng
    root      7802  7800  4 09:16 ?        00:03:56 /usr/sbin/syslog-ng --cfgfile /etc/syslog-ng/syslog-ng.conf --control /run/syslog-ng.ctl --persist-file /var/lib/syslog-ng/syslog-ng.persist --pidfile /run/syslog-ng.pid

There is a process with in this case PID 7800 \'supervising syslog-ng\' with a parent-PID (PPID) of 1, which means its parent is the init process. There is also the process with PID 7802, which looks more like what we might expect, referencing the binary. This process\' PPID is 7800, i.e. the supervising process.

The *supervising syslog-ng* process is actually also the same binary of syslog-ng:

`root `[`#`]`pgrep -lf syslog `

    7800 syslog-ng
    7802 syslog-ng

Syslog-ng appears to be supervising itself. What it does after startup is:

-   fork, to become a background daemon process (PID 7800) and get it to be adopted by the init process (PID 1);
-   fork again to create the worker process (PID 7802) as it\'s child process;
-   rename the process (PID 7800) to \"supervise syslog-ng\", in the parent process, and supervise its child (PID 7802).

If and when \"supervise syslog-ng\" detects that it\'s worker process (PID 7802) has terminated it will restart it. Syslog-ng calls this process mode \"safe-background\".

In order to get syslog-ng to work well under supervise-daemon it needs to run in the foreground though. There are two commandline options that will make that happen `--foreground` and `--process-mode=foreground`.

With the standard init scripts syslog-ng writes a pid file. This interferes with the operation of supervise-daemon so will have to be removed. Edit [/etc/init.d/syslog-ng] to remove the \--pidfile option in the command_args, and comment out the pidfile variable:

[FILE] **`/etc/init.d/syslog-ng`**

    command_args_background="--pidfile \"$\""
    command_args="--cfgfile \"$\" --control \"$\" --persist-file \"$\" $"
    supervisor="supervise-daemon"
    extra_commands="checkconfig"
    extra_started_commands="reload"
    pidfile="$"
    description="Syslog-ng is a syslog replacement with advanced filtering features."
    description_checkconfig="Check the configuration file that will be used by \"start\""
    description_reload="Reload the configuration without exiting"
    required_files="$"
    required_dirs="$"
    command_args_foreground="--foreground --process-mode=foreground"
    command_user="$:$"

At the end of the file, the reload function needs to be changed to use the supervisor instead of s-s-d:

[FILE] **`/etc/init.d/syslog-ng`**

    reload() "
            $ $ --signal HUP --pidfile "$"
            eend $?
    }

### [tor]

The [[[net-vpn/tor]](https://packages.gentoo.org/packages/net-vpn/tor)[]] service requires multiple edits, but each is trivial. It can be brought into the foreground by changing the logical value passed with *\--runasdaemon*. The *pidfile* assignment is to be deleted. Then *command_args* must be split into *command_args* and *command_args_background* as the general recipe explains. Finally replace any mentions of **s-s-d** with **supervise-daemon**.

[FILE] **`/etc/init.d/tor`**

    #!/sbin/openrc-run
    supervisor="supervise-daemon"
    command=/usr/bin/tor
    #pidfile=/run/tor/tor.pid
    command_args_background="-p $"
    command_args="--hush --runasdaemon 0"
    retry=$
    stopsig=INT
    command_progress=yes
    extra_commands="checkconfig"
    extra_started_commands="reload"
    description="Anonymizing overlay network for TCP"
    description_checkconfig="Check for valid config file"
    description_reload="Reload the configuration"

    checkconfig()  --verify-config --hush > /dev/null 2>&1
        if [ $? -ne 0 ] ; then
            eerror "Tor configuration (/etc/tor/torrc) is not valid."
            eerror "Example is in /etc/tor/torrc.sample"
            return 1
        fi
    }

    start_pre()

    reload()
        $ -s HUP --pidfile $
        eend $?
    }

### [vixie-cron]

The cron implementation offered by [[[sys-process/vixie-cron]](https://packages.gentoo.org/packages/sys-process/vixie-cron)[]] can be brought under supervision by editing [/etc/conf.d/vixie-cron] to pass it *-n* to make it run in foreground:

[FILE] **`/etc/conf.d/vixie-cron`**

    supervisor="supervise-daemon"
    command_args_foreground="-n"

## [][Services which won\'t run under a supervisor]

Unfortunately not all services are easy to run under supervisor-daemon, or other supervisors. The requirement that the daemon needs to run in foreground is not satisfied with all daemons, or it simply does not work. Sometimes there are alternatives available.

### [One shot services]

Some of the scripts in [/etc/init.d/] that are started by OpenRC, do not start daemons. Instead they run a program that terminates when it has performed its function, or they do a configuration setting.

Examples of such, with the action at boot / shutdown, are:

-   alsasound: loads / saves volume settings for audio
-   localmount: mounts / unmounts file systems as per [/etc/fstab]
-   loopback: creates the loopback interface
-   swap: activates / deactivates swap devices
-   urandom: loads random seed and initializes [/dev/urandom] / saves random seed
-   zram-init: creates / destroys zram devices.

There is no need to run such services under a supervisor.

### [netifrc]

The default Gentoo networking scripts belonging to [[[net-misc/netifrc]](https://packages.gentoo.org/packages/net-misc/netifrc)[]] call s-s-d from under the hood. The scripts can start/stop services like dhcpcd, dhclient, pppd, wpa_supplicant when needed, and they use s-s-d for it.

** Warning**\
Be careful not to mix and match different network management methodes because the results are unpredictable

### [dcron]

[[[sys-process/dcron]](https://packages.gentoo.org/packages/sys-process/dcron)[]] version 4.5-r1 crashes without an error message when it is run under a supervisor. Consider an alternative like [[[sys-process/fcron]](https://packages.gentoo.org/packages/sys-process/fcron)[]].

### [libvirtd]

Libvirtd, the server side daemon component of the [libvirt](//libvirt.org) also crashes without error message when it is run under supervise-daemon.

## [][Tips \'n tricks]

A system under openrc-init and supervise-daemon behaves a little different. This chapter shows some of the differences and how to take advantage of it.

### [rc-status]

rc-status shows the time when supervised services were started, and the number of restarts:

`root `[`#`]`rc-status`

    Runlevel: default
     device-mapper                                                   [  started  ]
     syslog-ng                                           [  started 18:22:43 (0) ]
     dnsmasq                                             [  started 18:22:42 (0) ]
     sshd                                                [  started 00:00:27 (1) ]
     dbus                                                            [  started  ]
     alsasound                                                       [  started  ]
     bluetooth                                           [  started 18:09:29 (0) ]
     ntpd                                                [  started 17:06:48 (0) ]
     acpid                                               [  started 11:53:26 (0) ]
     avahi-daemon                                        [  started 11:51:00 (0) ]
     zram-init                                                       [  started  ]
     cupsd                                                           [  stopped  ]
     laptop_mode                                                     [  started  ]
     libvirtd                                                        [  started  ]
     libvirt-guests                                                  [  started  ]
     distccd                                                         [  started  ]
     busybox-httpd                                                   [  started  ]
     lxc-bridge                                                      [  started  ]
     fcron                                               [  started 18:22:42 (0) ]
     iwd                                                 [  started 18:22:42 (0) ]
     netmount                                                        [  started  ]
     local                                                           [  started  ]
     agetty.tty2                                         [  started 18:22:41 (0) ]
     agetty.tty3                                         [  started 18:22:41 (0) ]
     agetty.tty4                                         [  started 18:22:41 (0) ]
     agetty.tty5                                         [  started 18:22:41 (0) ]
     agetty.tty6                                         [  started 18:22:41 (0) ]
     agetty-autologin.tty1                               [  started 18:22:41 (0) ]
    Dynamic Runlevel: hotplugged
    Dynamic Runlevel: needed/wanted
     dhcpcd                                                          [  started  ]
     virtlogd                                                        [  started  ]
    Dynamic Runlevel: manual

Note the line for sshd, which shows that it was recently restarted by its supervisor. With [rc-status -S] only supervised services are displayed.

\

## [External resources]

-   [Mistakes to avoid when designing Unix dæmon programs](https://jdebp.eu/FGA/unix-daemon-design-mistakes-to-avoid.html)
-   [How to make daemons that will maximize sysadmin hatred](http://cloud9.hedgee.com./scribbles/daemon)