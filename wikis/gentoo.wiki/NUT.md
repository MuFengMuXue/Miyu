**Resources**

[[]][Home](https://networkupstools.org/)

[[]][Package information](https://packages.gentoo.org/packages/sys-power/nut)

[[]][GitHub](https://github.com/networkupstools/nut)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Network_UPS_Tools "wikipedia:Network UPS Tools")

**NUT** provides control and monitoring features for uninterruptible power supplies, power distribution units, automatic transfer switches, and solar controllers.

Do you have a UPS? Do you want to have you system gracefully shutdown in case of a power outage? This guide will show how you can make the most out of your UPS by using NUT from the [Network UPS Tools](https://www.networkupstools.org/) project

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flag]](#USE_flag)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration standalone]](#Configuration_standalone)
    -   [[2.1] [Files]](#Files)
        -   [[2.1.1] [/etc/nut/nut.conf]](#.2Fetc.2Fnut.2Fnut.conf)
        -   [[2.1.2] [/etc/nut/ups.conf]](#.2Fetc.2Fnut.2Fups.conf)
        -   [[2.1.3] [/etc/nut/upsd.users]](#.2Fetc.2Fnut.2Fupsd.users)
        -   [[2.1.4] [/etc/nut/upsmon.conf]](#.2Fetc.2Fnut.2Fupsmon.conf)
        -   [[2.1.5] [/etc/nut/upssched.conf]](#.2Fetc.2Fnut.2Fupssched.conf)
        -   [[2.1.6] [/usr/bin/upssched-cmd]](#.2Fusr.2Fbin.2Fupssched-cmd)
    -   [[2.2] [Services]](#Services)
        -   [[2.2.1] [OpenRC]](#OpenRC)
-   [[3] [LAN client/server configuration]](#LAN_client.2Fserver_configuration)
    -   [[3.1] [Server configuration]](#Server_configuration)
        -   [[3.1.1] [Server files]](#Server_files)
            -   [[3.1.1.1] [/etc/nut/nut.conf]](#.2Fetc.2Fnut.2Fnut.conf_2)
            -   [[3.1.1.2] [/etc/nut/upsd.conf]](#.2Fetc.2Fnut.2Fupsd.conf)
            -   [[3.1.1.3] [/etc/nut/upsd.users]](#.2Fetc.2Fnut.2Fupsd.users_2)
    -   [[3.2] [Client configuration]](#Client_configuration)
        -   [[3.2.1] [Client files]](#Client_files)
            -   [[3.2.1.1] [/etc/nut/nut.conf]](#.2Fetc.2Fnut.2Fnut.conf_3)
            -   [[3.2.1.2] [/etc/nut/ups.conf]](#.2Fetc.2Fnut.2Fups.conf_2)
            -   [[3.2.1.3] [/etc/nut/upsd.conf]](#.2Fetc.2Fnut.2Fupsd.conf_2)
            -   [[3.2.1.4] [/etc/nut/upsd.users]](#.2Fetc.2Fnut.2Fupsd.users_3)
            -   [[3.2.1.5] [/etc/nut/upsmon.conf]](#.2Fetc.2Fnut.2Fupsmon.conf_2)
            -   [[3.2.1.6] [/etc/nut/upssched.conf]](#.2Fetc.2Fnut.2Fupssched.conf_2)
            -   [[3.2.1.7] [/usr/bin/upssched-cmd]](#.2Fusr.2Fbin.2Fupssched-cmd_2)
        -   [[3.2.2] [Client services]](#Client_services)
-   [[4] [External resources]](#External_resources)

## [Installation]

### [USE flag]

To connect a UPS via USB, make sure to set the `usb` USE flag:

### [USE flags for] [sys-power/nut](https://packages.gentoo.org/packages/sys-power/nut) [[]] [Network-UPS Tools]

  ------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+man`](https://packages.gentoo.org/useflags/+man)           Build and install man pages
  [`+usb`](https://packages.gentoo.org/useflags/+usb)           Includes all UPS drivers that use USB.
  [`cgi`](https://packages.gentoo.org/useflags/cgi)             Add CGI script support
  [`doc`](https://packages.gentoo.org/useflags/doc)             Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`gpio`](https://packages.gentoo.org/useflags/gpio)           Includes all UPS drivers that use GPIO.
  [`i2c`](https://packages.gentoo.org/useflags/i2c)             Includes all UPS drivers that use I2C.
  [`ipmi`](https://packages.gentoo.org/useflags/ipmi)           Includes all UPS drivers that use ipmi.
  [`modbus`](https://packages.gentoo.org/useflags/modbus)       Includes all UPS drivers that use MODBUS.
  [`monitor`](https://packages.gentoo.org/useflags/monitor)     Add a Qt6 gui monitor.
  [`python`](https://packages.gentoo.org/useflags/python)       Add optional support/bindings for the Python language
  [`selinux`](https://packages.gentoo.org/useflags/selinux)     !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`serial`](https://packages.gentoo.org/useflags/serial)       Includes all UPS drivers that use SERIAL.
  [`snmp`](https://packages.gentoo.org/useflags/snmp)           Includes all UPS drivers that use SNMP.
  [`ssl`](https://packages.gentoo.org/useflags/ssl)             Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  [`systemd`](https://packages.gentoo.org/useflags/systemd)     Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`tcpd`](https://packages.gentoo.org/useflags/tcpd)           Add support for TCP wrappers
  [`test`](https://packages.gentoo.org/useflags/test)           Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`xml`](https://packages.gentoo.org/useflags/xml)             Includes all UPS drivers that use XML.
  [`zeroconf`](https://packages.gentoo.org/useflags/zeroconf)   Support for DNS Service Discovery (DNS-SD)
  ------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-23 21:45] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sys-power/nut`

## [Configuration standalone]

Search a UPS with nut-scanner:

`root `[`#`]`/usr/bin/nut-scanner`

    Scanning USB bus.
    Scanning XML/HTTP bus.
    No start IP, skipping NUT bus (old connect method)
    [nutdev1]
            driver = "usbhid-ups"
            port = "auto"
            vendorid = "051D"
            productid = "0002"
            product = "Back-UPS SMC 1500 FW:879.L4 .I USB FW:L4"
            serial = "***"
            vendor = "American Power Conversion"
            bus = "003"

Take note of driver name and port type for configuration file.

If UPS is connected via USB port, add user nut to group usb.

`root `[`#`]`usermod -a -G usb nut`

### [Files]

#### [][/etc/nut/nut.conf]

Set mode to standalone if the machine is connected to the UPS directly and to run NUT on this machine.

`root `[`#`]`nano -w /etc/nut/nut.conf`

[FILE] **`/etc/nut/nut.conf`Desired settings**

    MODE=standalone

#### [][/etc/nut/ups.conf]

The main UPS configuration file. Make sure that the UPS name (the text in the brackets) doesn\'t have any spaces. For configuration specific to the UPS you need to look it up here: [NUT Hardware Compatibility Lookup](https://www.networkupstools.org/stable-hcl.html)

`root `[`#`]`nano -w /etc/nut/ups.conf`

[FILE] **`/etc/nut/ups.conf`Example ups.conf configuration**

    [APCSMC1500]
        driver = usbhid-ups
        port = auto
        desc = "APC SMC1500 UPS"
    # Change some variables in UPS hardware. Not all devices or drivers
    # implement this, so this may not have effect on your system.
        override.battery.charge.low = 30
        override.battery.runtime.low = 180

#### [][/etc/nut/upsd.users]

Configure at least one user so that upsmon can be launched later. [upsd] will create a TCP connection that upsmon will use to check on the status of the UPS.

`root `[`#`]`nano -w /etc/nut/upsd.users`

[FILE] **`/etc/nut/upsd.users`Example upsd.users configuration**

    [monmaster]
        password = masterpassword
        upsmon master

#### [][/etc/nut/upsmon.conf]

Create a MONITOR configuration in [/etc/nut/upsmon.conf]:

`root `[`#`]`nano -w /etc/nut/upsmon.conf`

[FILE] **`/etc/nut/upsmon.conf`Example upsmon configuration**

    MONITOR APCSMC1500@127.0.0.1 1 monmaster masterpassword master

    # If you want that NUT can shutdown the computer, you need root privileges:
    RUN_AS_USER root

    MINSUPPLIES 1
    SHUTDOWNCMD "/sbin/shutdown -h +0"
    NOTIFYCMD /usr/sbin/upssched
    POLLFREQ 5
    POLLFREQALERT 1
    HOSTSYNC 15
    DEADTIME 15
    POWERDOWNFLAG /etc/killpower

    NOTIFYMSG ONLINE    "UPS %s on line power"
    NOTIFYMSG ONBATT    "UPS %s on battery"
    NOTIFYMSG LOWBATT   "UPS %s battery is low"
    NOTIFYMSG FSD       "UPS %s: forced shutdown in progress"
    NOTIFYMSG COMMOK    "Communications with UPS %s established"
    NOTIFYMSG COMMBAD   "Communications with UPS %s lost"
    NOTIFYMSG SHUTDOWN  "Auto logout and shutdown proceeding"
    NOTIFYMSG REPLBATT  "UPS %s battery needs to be replaced"
    NOTIFYMSG NOCOMM    "UPS %s is unavailable"
    NOTIFYMSG NOPARENT  "upsmon parent process died - shutdown impossible"

    NOTIFYFLAG ONLINE   SYSLOG+WALL+EXEC
    NOTIFYFLAG ONBATT   SYSLOG+WALL+EXEC
    NOTIFYFLAG LOWBATT  SYSLOG+WALL+EXEC
    NOTIFYFLAG FSD      SYSLOG+WALL+EXEC
    NOTIFYFLAG COMMOK   SYSLOG+WALL+EXEC
    NOTIFYFLAG COMMBAD  SYSLOG+WALL+EXEC
    NOTIFYFLAG SHUTDOWN SYSLOG+WALL+EXEC
    NOTIFYFLAG REPLBATT SYSLOG+WALL+EXEC
    NOTIFYFLAG NOCOMM   SYSLOG+WALL+EXEC
    NOTIFYFLAG NOPARENT SYSLOG+WALL

    RBWARNTIME 43200

    NOCOMMWARNTIME 600

    FINALDELAY 5

#### [][/etc/nut/upssched.conf]

Configure operations on that upsmon will check on the status of the UPS:

`root `[`#`]`nano -w /etc/nut/upssched.conf`

[FILE] **`/etc/nut/upssched.conf`Example upssched.conf configuration**

    CMDSCRIPT /usr/bin/upssched-cmd
    PIPEFN /var/lib/nut/upssched/upssched.pipe
    LOCKFN /var/lib/nut/upssched/upssched.lock

    AT ONBATT * START-TIMER onbatt 300
    AT ONLINE * CANCEL-TIMER onbatt online
    AT LOWBATT * EXECUTE onbatt
    AT COMMBAD * START-TIMER commbad 30
    AT COMMOK * CANCEL-TIMER commbad commok
    AT NOCOMM * EXECUTE commbad
    AT SHUTDOWN * EXECUTE powerdown
    AT REPLBATT * EXECUTE replacebatt

`root `[`#`]`mkdir -p /var/lib/nut/upssched`

`root `[`#`]`chown nut:nut /var/lib/nut/upssched`

#### [][/usr/bin/upssched-cmd]

`root `[`#`]`nano -w /usr/bin/upssched-cmd`

[FILE] **`/usr/bin/upssched-cmd`Example upssched.conf configuration**

    #! /bin/sh
    #
    # This script should be called by upssched via the CMDSCRIPT directive.
    #
    # Here is a quick example to show how to handle a bunch of possible
    # timer names with the help of the case structure.
    #
    # This script may be replaced with another program without harm.
    #
    # The first argument passed to your CMDSCRIPT is the name of the timer
    # from your AT lines.

    case $1 in
            onbatt)
                    logger -t upssched-cmd "The UPS is on battery"
                    mail -s "The UPS is on battery" admin@example.com &
                    # For example, uncommenting, you can stop some power-hog services
                    #rc-service boinc stop
                    #rc-service xmr-stak stop
                    ;;
            online)
                    logger -t upssched-cmd "The UPS is back on power"
                    mail -s "The UPS is back on power" admin@example.com &
                    # For example, uncommenting, you can restart useful power-hog services
                    #rc-service boinc start
                    #rc-service xmr-stak start
                    ;;
            commbad)
                    logger -t upssched-cmd "The server lost communication with UPS"
                    mail -s "The server lost communication with UPS" admin@example.com &
                    ;;
            commok)
                    logger -t upssched-cmd "The server re-establish communication with UPS"
                    mail -s "The server re-establish communication with UPS" admin@example.com &
                    ;;
            powerdown)
                    logger -t upssched-cmd "The UPS is shutting down the system"
                    mail -s "The UPS is shutting down the system" admin@example.com &
                    ;;
            replacebatt)
                    logger -t upssched-cmd "The UPS needs new battery"
                    mail -s "The UPS needs new battery" admin@example.com &
                    ;;
            *)
                    logger -t upssched-cmd "Unrecognized command: $1"
                    ;;
    esac

### [Services]

#### [OpenRC]

To add the services to start on system boot:

`root `[`#`]`rc-update add upsdrv default `

`root `[`#`]`rc-update add upsd default `

`root `[`#`]`rc-update add upsmon default `

To start [upsd] now run:

`root `[`#`]`rc-service upsdrv start `

`root `[`#`]`rc-service upsd start `

`root `[`#`]`rc-service upsmon start `

To check the status of the UPS manually (adjust the UPS name as needed):

`root `[`#`]`upsc APCSMC1500@127.0.0.1 ups.status`

    OL

OL means that the UPS is \"online\" and not drawing from the battery and is configured correctly.

In the event of a shutdown due to a power failure, nut can additionally turn off the UPS by adding nut.powerfail to the shutdown runlevel:

`root `[`#`]`rc-update add nut.powerfail shutdown`

## [][LAN client/server configuration]

### [Server configuration]

Starting from standalone configuration, change:

#### [Server files]

##### [][/etc/nut/nut.conf]

`root `[`#`]`nano -w /etc/nut/nut.conf`

[FILE] **`/etc/nut/nut.conf`Desired settings**

    MODE=netserver

##### [][/etc/nut/upsd.conf]

`root `[`#`]`nano -w /etc/nut/upsd.conf`

[FILE] **`/etc/nut/upsd.conf`Desired settings**

    LISTEN 127.0.0.1 3493
    LISTEN 192.168.1.1 3493

##### [][/etc/nut/upsd.users]

`root `[`#`]`nano -w /etc/nut/upsd.users`

[FILE] **`/etc/nut/upsd.users`Example upsd.users configuration**

    [monmaster]
        password = masterpassword
        upsmon master

    [monslave]
        password = slavepassword
        upsmon slave

### [Client configuration]

#### [Client files]

##### [][/etc/nut/nut.conf]

`root `[`#`]`nano -w /etc/nut/nut.conf`

[FILE] **`/etc/nut/nut.conf`Desired settings**

    MODE=netclient

##### [][/etc/nut/ups.conf]

This file is not needed for slave monitor.

##### [][/etc/nut/upsd.conf]

This file is not needed for slave monitor.

##### [][/etc/nut/upsd.users]

`root `[`#`]`nano -w /etc/nut/upsd.users`

[FILE] **`/etc/nut/upsd.users`Example upsd.users configuration**

    [monslave]
        password = slavepassword
        upsmon slave

##### [][/etc/nut/upsmon.conf]

Copy the standalone configuration, but create a different MONITOR configuration in [/etc/nut/upsmon.conf]:

`root `[`#`]`nano -w /etc/nut/upsmon.conf`

[FILE] **`/etc/nut/upsmon.conf`Example upsmon configuration**

    MONITOR APCSMC1500@192.168.1.1 1 monslave slavepassword slave

##### [][/etc/nut/upssched.conf]

This file can be the same of standalone configuration.

##### [][/usr/bin/upssched-cmd]

This file can be the same of standalone configuration.

#### [Client services]

On client machine, only the upsmon service is needed. To add the services to start on system boot:

`root `[`#`]`rc-update add upsmon default `

To start [upsd] now run:

`root `[`#`]`rc-service upsmon start `

To check the status of the UPS manually (adjust the UPS name as needed):

`root `[`#`]`upsc APCSMC1500@192.168.1.1 ups.status`

    OL

## [External resources]

-   [Official user manual](https://networkupstools.org/docs/user-manual.chunked/index.html)
-   [Detailed NUT Configuration](https://wiki.ipfire.org/addons/nut/detailed)