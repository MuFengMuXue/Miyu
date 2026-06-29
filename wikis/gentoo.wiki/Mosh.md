[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Mosh&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](http://mosh.mit.edu/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Mosh_(software) "wikipedia:Mosh (software)")

**Mosh** is a SSH client server that is aware of connectivity problems of the original SSH implementation. Mosh can migrate physical connections and IP addresses while staying connected. Mosh depends on [SSH](https://wiki.gentoo.org/wiki/SSH "SSH").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Firewall]](#Firewall)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Connecting]](#Connecting)
-   [[4] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [net-misc/mosh](https://packages.gentoo.org/packages/net-misc/mosh) [[]] [Mobile shell that supports roaming and intelligent local echo]

  --------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------
  [`+client`](https://packages.gentoo.org/useflags/+client)       Build network client
  [`+hardened`](https://packages.gentoo.org/useflags/+hardened)   Activate default security enhancements for toolchain (gcc, glibc, binutils)
  [`+server`](https://packages.gentoo.org/useflags/+server)       Build network server
  [`+utempter`](https://packages.gentoo.org/useflags/+utempter)   Include libutempter support
  [`examples`](https://packages.gentoo.org/useflags/examples)     Include example scripts
  [`nettle`](https://packages.gentoo.org/useflags/nettle)         Use dev-libs/nettle for some cryptographic functions instead of dev-libs/openssl. With Nettle, some of mosh\'s own code is used for OCB.
  [`syslog`](https://packages.gentoo.org/useflags/syslog)         Enable support for syslog
  [`ufw`](https://packages.gentoo.org/useflags/ufw)               Install net-firewall/ufw rule set
  --------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-19 09:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[net-misc/mosh]](https://packages.gentoo.org/packages/net-misc/mosh)[]]:

`root `[`#`]`emerge --ask net-misc/mosh`

## [Configuration]

Mosh requires [UTF-8](https://wiki.gentoo.org/wiki/UTF-8 "UTF-8") [locales](https://wiki.gentoo.org/wiki/Localization/Guide#Locale_system "Localization/Guide") to be set in order to run. To check, run:

`user `[`$`]`locale -a`

In case it does not return the [UTF-8](https://wiki.gentoo.org/wiki/UTF-8 "UTF-8") locale see [UTF-8#Setting up UTF-8 with Gentoo Linux](https://wiki.gentoo.org/wiki/UTF-8#Setting_up_UTF-8_with_Gentoo_Linux "UTF-8").

### [Firewall]

Each mosh client requires a free and accessible UDP port between 60000 and 61000 on the server to function.

With [Ufw](https://wiki.gentoo.org/wiki/Ufw "Ufw"), allow these ports with:

`root `[`#`]`ufw allow 60000:61000/udp`

## [Usage]

### [Connecting]

Once the remote host has SSH running, mosh installed, and the UFT8 locale set connection is possible:

`user `[`$`]`mosh user@remote-host.com`

## [See also]

-   [ssh](https://wiki.gentoo.org/wiki/Ssh "Ssh") --- the ubiquitous tool for logging into and working on remote machines securely.