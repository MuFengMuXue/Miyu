**Resources**

[[]][Home](http://www.mumble.info/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Mumble_(software) "wikipedia:Mumble (software)")

[[]][GitHub](https://github.com/mumble-voip/mumble)

Murmur is the server component to [Mumble](https://wiki.gentoo.org/wiki/Mumble "Mumble") built on the Qt framework. See [uMurmur](https://wiki.gentoo.org/wiki/UMurmur "UMurmur") for a lighter weight embedded version.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Services]](#Services)
        -   [[2.2.1] [OpenRC]](#OpenRC)
        -   [[2.2.2] [systemd]](#systemd)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Initial setup]](#Initial_setup)
    -   [[3.2] [Gaining SuperUser privileges]](#Gaining_SuperUser_privileges)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [net-voip/murmur](https://packages.gentoo.org/packages/net-voip/murmur) [[]] [Open source, low-latency, high quality voice chat server]

  ------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+ice`](https://packages.gentoo.org/useflags/+ice)           Use dev-libs/Ice to enable remote control capabilities.
  [`+sqlite`](https://packages.gentoo.org/useflags/+sqlite)     Add support for sqlite - embedded sql database
  [`mysql`](https://packages.gentoo.org/useflags/mysql)         Add mySQL Database support
  [`postgres`](https://packages.gentoo.org/useflags/postgres)   Add support for the postgresql database
  [`test`](https://packages.gentoo.org/useflags/test)           Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`zeroconf`](https://packages.gentoo.org/useflags/zeroconf)   Support for DNS Service Discovery (DNS-SD)
  ------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-12 22:34] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask net-voip/murmur`

## [Configuration]

### [Files]

-   [/etc/murmur/murmur.ini] - Daemon configuration file.
-   [/etc/conf.d/murmur] - OpenRC service configuration file.
-   [/usr/lib/systemd/system/murmur.service] - systemd service configuration file.

### [Services]

#### [OpenRC]

To have the murmur daemon run on system boot, issue:

`root `[`#`]`rc-update add murmur default`

To start murmur, issue:

`root `[`#`]`rc-service murmur start`

#### [systemd]

To have the murmur daemon run on system boot, issue:

`root `[`#`]`systemctl enable murmur.service`

To start murmur on systemd, issue:

`root `[`#`]`systemctl start murmur.service`

## [Usage]

### [Initial setup]

After the emerge, pay attention to the einfo message that is printed; it contains important setup information. It will likely look similar to the following message.

     * Useful scripts are located in /usr/share/doc/murmur-1.3.4/scripts.
     * Please execute:
     * murmurd -ini /etc/murmur/murmur.ini -supw
     * chown murmur:murmur /var/lib/murmur/murmur.sqlite
     * to set the build-in 'SuperUser' password before starting murmur.
     * Please restart dbus before starting murmur, or else dbus registration
     * will fail.
     *
     * (Note: Above message is only printed the first time package is
     * installed. Please look at /usr/share/doc/murmur-1.3.4/README.gentoo*
     * for future reference)

You **must** also set at least `pidfile` in the [/etc/murmur/murmur.ini] file, otherwise the init will not see the service as started. Specifying the `logfile` is also a nice thing, as service spits out a warning about failing to open it:

    ; If set, Murmur will write its process ID to this file
    ; when running in daemon mode (when the -fg flag is not
    ; specified on the command line). Only available on
    ; Unix-like systems.
    pidfile=/run/murmur/murmur.pid

    ; Specifies the file Murmur should log to. By default, Murmur
    ; logs to the file 'murmur.log'. If you leave this field blank
    ; on Unix-like systems, Murmur will force itself into foreground
    ; mode which logs to the console.
    logfile=/var/log/murmur/murmur.log

### [Gaining SuperUser privileges]

A SuperUser account is created by default on every instance of a Murmur service. This account is created to assist in administration tasks such as kicking or banning an abusive user or quickly creating new channels. In order to obtain SuperUser privileges, the correct password must be used. The SuperUser password is written to the Murmur log file ([/var/log/murmur/murmur.log]). Use any pager program or text editor to view the log (for security reasons the log is only view able for users with root privileges), or simply grep for the following line:

`root `[`#`]`cat /var/log/murmur/murmur.log | grep "Password for 'SuperUser'"`

Once the password has been obtained, use a client to connect to the server as the user called \"SuperUser\". Instructions on adding SuperUser privileges to other accounts can be found [here on the Mumble wiki](http://wiki.mumble.info/wiki/Murmurguide#Becoming_Administrator_and_Registering_a_User).

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose net-voip/murmur`

## [See also]

-   [uMurmur](https://wiki.gentoo.org/wiki/UMurmur "UMurmur") --- a minimalistic server for Mumble designed to run on embedded systems (DD-WRT or OpenWRT) or older PC hardware.
-   [Mumble](https://wiki.gentoo.org/wiki/Mumble "Mumble") --- an open source, cross platform, low-latency, high quality voice over IP (VoIP) client.

## [External resources]

-   [http://wiki.mumble.info/wiki/MurmurGuide](http://wiki.mumble.info/wiki/MurmurGuide) - The Mumble wiki\'s guide for running Murmur (covers Windows and Linux).