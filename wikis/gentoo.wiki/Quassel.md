**Resources**

[[]][Home](https://quassel-irc.org/)

[[]][Package information](https://packages.gentoo.org/packages/net-irc/quassel)

[[]][Bugs (upstream)](https://bugs.quassel-irc.org/)

[[]][GitHub](https://github.com/quassel/quassel)

**Quassel** is a daemon/headless IRC client written in C++ that supports 24/7 connectivity. Quassel has both a \"core\" daemon and a client can be used to attached to a running \"core\" instance. Because of the separation in architecture, the core component can run on the local system, or on another system.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
    -   [[1.2] [USE flags]](#USE_flags)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
        -   [[2.1.1] [OpenRC]](#OpenRC)
        -   [[2.1.2] [systemd]](#systemd)
    -   [[2.2] [SSL/TLS certificate generation]](#SSL.2FTLS_certificate_generation)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Services]](#Services)
        -   [[3.1.1] [OpenRC]](#OpenRC_2)
        -   [[3.1.2] [systemd]](#systemd_2)
    -   [[3.2] [Client connection]](#Client_connection)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Migrate SQLite to PostgreSQL]](#Migrate_SQLite_to_PostgreSQL)
-   [[5] [See also]](#See_also)

## [Installation]

### [Emerge]

To install:

`root `[`#`]`emerge --ask net-irc/quassel`

### [USE flags]

With GUI support enabled by default, ebuild includes a sensible USE flag selection for desktop usage. Enable support for URL previews if desired.

### [USE flags for] [net-irc/quassel](https://packages.gentoo.org/packages/net-irc/quassel) [[]] [Qt/KDE IRC client supporting a remote daemon for 24/7 connectivity]

  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+dbus`](https://packages.gentoo.org/useflags/+dbus)                   Support desktop notifications via the StatusNotifier D-Bus service (used by most modern desktop environments).
  [`+server`](https://packages.gentoo.org/useflags/+server)               Build the server binary. If this USE flag is disabled, the \'core\' server binary for quassel is not built, and cannot be used. You need this enabled on the server, but you might want to disable it on the client.
  [`+system-icons`](https://packages.gentoo.org/useflags/+system-icons)   Use kde-frameworks/breeze-icons rather than icons bundled with Quassel.
  [`crypt`](https://packages.gentoo.org/useflags/crypt)                   Support core-\>network per-channel and per-query blowfish encryption via app-crypt/qca.
  [`gui`](https://packages.gentoo.org/useflags/gui)                       Enable support for a graphical user interface
  [`kde`](https://packages.gentoo.org/useflags/kde)                       Add support for software made by KDE, a free software community
  [`ldap`](https://packages.gentoo.org/useflags/ldap)                     Add LDAP support (Lightweight Directory Access Protocol)
  [`monolithic`](https://packages.gentoo.org/useflags/monolithic)         Build standalone client with integrated core, no external quasselcore needed. Only useful if you don\'t want to use Quassel\'s client/server model. The server and X flags are not needed in this case but it is possible to enable them too.
  [`oxygen`](https://packages.gentoo.org/useflags/oxygen)                 Support the Oxygen icon set that was the default for KDE4.
  [`postgres`](https://packages.gentoo.org/useflags/postgres)             Add support for the postgresql database
  [`spell`](https://packages.gentoo.org/useflags/spell)                   Add dictionary support
  [`syslog`](https://packages.gentoo.org/useflags/syslog)                 Enable support for syslog
  [`test`](https://packages.gentoo.org/useflags/test)                     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`urlpreview`](https://packages.gentoo.org/useflags/urlpreview)         Use dev-qt/qtwebengine rendering engine for showing URL thumbnails.
  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-21 20:11] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

## [Configuration]

### [Files]

#### [OpenRC]

Gentoo\'s Quassel package should come with a useful and fairly self-explanatory file to adjust Quassel\'s default behavior for OpenRC in the [/etc/conf.d/quasselcore] configuration file.

#### [systemd]

systemd\'s variables will need to be set in the [/usr/lib64/systemd/system/quasselcore.service] file. Options will be the same as those used when running Quassel from the CLI and will need to be added as `ExecStart=` values.

It is not good practice to edit files in the [/lib/systemd/system] directory. Create a copy in [/etc/systemd/system] and edit that file. systemd will always source the [/etc/systemd/system] directory as priority^[\[1\]](#cite_note-1)^ over the same files found in [/lib] (aka [/usr/lib]^[\[2\]](#cite_note-2)^).

`root `[`#`]`cp /lib/systemd/system/quasselcore.service /etc/portage/system/`

[FILE] **`/etc/systemd/system/quasselcore.service`Example of a default port change**

    [Unit]
    Description=Quassel Core
    After=network.target

    [Service]
    User=quassel
    Group=quassel
    ExecStart=/usr/bin/quasselcore --configdir=/var/lib/quassel --port=4141

    [Install]
    WantedBy=multi-user.target

### [][SSL/TLS certificate generation]

Create an SSL/TLS certificate:

`root `[`#`]`( cd /var/lib/quassel/ && openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout quasselCert.key -out quasselCert.crt && cat quasselCert. > quasselCert.pem )`

## [Usage]

### [Services]

#### [OpenRC]

To enable Quassel core on start-up:

`root `[`#`]`rc-update add quasselcore default`

Start Quassel core:

`root `[`#`]`/etc/init.d/quasselcore start`

#### [systemd]

To enable Quassel core on start-up and start the service immediately:

`root `[`#`]`systemctl enable --now quasselcore`

### [Client connection]

Connect to the core with a Quassel client, and the client will prompt for initial setup configuration, including database credentials. At times it may be necessary to change Quassel\'s behavior, such as its default listening address, default port, etc.

To change the default port from the CLI:

`root `[`#`]`quasselcore --configdir=/var/lib/quassel --port=4141`

Other options can be displayed with:

`root `[`#`]`quasselcore --help`

## [Troubleshooting]

### [Migrate SQLite to PostgreSQL]

Create users in PostgreSQL for Quassel, here a user and database called \"quassel\" will be used as an example. See [PostgreSQL/QuickStart](https://wiki.gentoo.org/wiki/PostgreSQL/QuickStart "PostgreSQL/QuickStart") for information on how to do this.

Then setup Quassel with the newly created user:

`root `[`#`]`quasselcore --configdir=/var/lib/quassel --select-backend=PostgreSQL`

## [See also]

-   [Irssi](https://wiki.gentoo.org/wiki/Irssi "Irssi") --- a powerful text-mode IRC client for connecting to internet relay chat (IRC) networks.
-   [WeeChat](https://wiki.gentoo.org/wiki/WeeChat "WeeChat") --- a light, extensible, actively maintained, well documented, highly featured text-mode [IRC](https://wiki.gentoo.org/wiki/IRC "IRC") client.

1.  [[[↑](#cite_ref-1)] [[https://www.freedesktop.org/software/systemd/man/file-hierarchy.html#General%20Structure](https://www.freedesktop.org/software/systemd/man/file-hierarchy.html#General%20Structure)]]
2.  [[[↑](#cite_ref-2)] [[https://www.freedesktop.org/software/systemd/man/file-hierarchy.html#Persistent%20Variable%20System%20Data](https://www.freedesktop.org/software/systemd/man/file-hierarchy.html#Persistent%20Variable%20System%20Data)]]