**Resources**

[[]][Home](http://umurmur.net/)

[[]][GitHub](https://github.com/umurmur/umurmur)

uMurmur is a minimalistic server for Mumble designed to run on embedded systems (DD-WRT or OpenWRT) or older PC hardware. It does not include the Qt framework, which makes it a much smaller package and lighter on system resources.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Services]](#Services)
        -   [[2.2.1] [OpenRC]](#OpenRC)
        -   [[2.2.2] [Systemd]](#Systemd)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [net-voip/umurmur](https://packages.gentoo.org/packages/net-voip/umurmur) [[]] [Minimalistic Murmur (Mumble server)]

  ----------------------------------------------------------- ------------------------------------------------------------------------
  [`gnutls`](https://packages.gentoo.org/useflags/gnutls)     Prefer net-libs/gnutls as SSL/TLS provider (ineffective with USE=-ssl)
  [`mbedtls`](https://packages.gentoo.org/useflags/mbedtls)   Use net-libs/mbedtls as TLS provider
  [`shm`](https://packages.gentoo.org/useflags/shm)           Enable shared memory support
  ----------------------------------------------------------- ------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-07-29 06:52] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install uMurmur via:

`root `[`#`]`emerge --ask net-voip/umurmur`

## [Configuration]

For the most up to date details on configuration visit the [configuration article](https://github.com/umurmur/umurmur/wiki/Configuration) on uMurmur\'s GitHub page.

In short, configuration is as follows.

### [Files]

-   [/etc/conf.d/umurmurd] - File that controls what options are passed to the [umurmurd] daemon upon starting or restarting.
-   [/etc/umurmur/umurmur.conf] - Primary configuration file. Used to set channel names, IP addresses, group names, password, etc.

Modify the primary configuration file as desired. Be sure to set a password if the service should be private:

[FILE] **`/etc/umurmur/umurmur.conf`**

    password = "mysecretpassword";

### [Services]

#### [OpenRC]

After configuration is in a working state, start the server:

`root `[`#`]`rc-service umurmurd start`

To have the daemon start each time the system boots add it to the default runlevel:

`root `[`#`]`rc-update add umurmurd default`

To restart the service:

`root `[`#`]`rc-service umurmurd restart`

#### [Systemd]

For systemd users, run the following command to start the daemon:

`root `[`#`]`systemctl start umurmurd.service`

To have the daemon start on system boot issue:

`root `[`#`]`systemctl enable umurmurd.service`

To restart the service:

`root `[`#`]`systemctl restart umurmurd.service`

## [See also]

-   [Mumble](https://wiki.gentoo.org/wiki/Mumble "Mumble") --- an open source, cross platform, low-latency, high quality voice over IP (VoIP) client.

## [External resources]

-   [Installing uMurmur on DD-WRT](https://github.com/umurmur/umurmur/wiki/DD-WRT)