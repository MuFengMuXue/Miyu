**utelnetd** is a small and efficient stand alone [Telnet](https://en.wikipedia.org/wiki/Telnet "wikipedia:Telnet") server daemon. Telnet can be useful for several applications, such as a backup when updating [SSH](https://wiki.gentoo.org/wiki/SSH "SSH"), and configuring industrial grade routers via console cables.

** Note**\
Telnet sends data including passwords in plain text.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Service]](#Service)
-   [[3] [Testing]](#Testing)

## [Installation]

### [Emerge]

Install [[[net-misc/utelnetd]](https://packages.gentoo.org/packages/net-misc/utelnetd)[]]:

`root `[`#`]`emerge --ask utelnetd`

## [Configuration]

### [Service]

To automatically start utelnetd at boot:

`root `[`#`]`rc-update add utelnetd default`

To start it immediately:

`root `[`#`]`rc-service utelnetd start`

## [Testing]

`user `[`$`]`telnet localhost`

`telnet` is provided by `net-misc/telnet-bsd`.