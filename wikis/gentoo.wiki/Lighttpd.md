Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Lighttpd/hu "lighttpd (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Lighttpd/ru "Lighttpd (88% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Lighttpd/zh-cn "Lighttpd (41% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Lighttpd/ja "lighttpd (100% translated)")

**Resources**

[[]][Home](https://www.lighttpd.net)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Lighttpd "wikipedia:Lighttpd")

[[]][[#lighttpd](ircs://irc.libera.chat/#lighttpd)] ([[webchat](https://web.libera.chat/#lighttpd)])

[lighttpd] (pronounced /*lighty*/) is a fast and lightweight [web server](https://wiki.gentoo.org/wiki/Category:Web_servers "Category:Web servers").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [IP access lists]](#IP_access_lists)
    -   [[2.2] [Start up]](#Start_up)
        -   [[2.2.1] [OpenRC]](#OpenRC)
        -   [[2.2.2] [systemd]](#systemd)
-   [[3] [Troubleshooting]](#Troubleshooting)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [www-servers/lighttpd](https://packages.gentoo.org/packages/www-servers/lighttpd) [[]] [Lightweight high-performance web server]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`+brotli`](https://packages.gentoo.org/useflags/+brotli)         Enable output compression via app-arch/brotli (recommended)
  [`+lua`](https://packages.gentoo.org/useflags/+lua)               Enable Lua scripting support
  [`+nettle`](https://packages.gentoo.org/useflags/+nettle)         Use dev-libs/nettle as crypto library
  [`+pcre`](https://packages.gentoo.org/useflags/+pcre)             Add support for Perl Compatible Regular Expressions
  [`+zlib`](https://packages.gentoo.org/useflags/+zlib)             Enable output compression via gzip or deflate algorithms from virtual/zlib
  [`dbi`](https://packages.gentoo.org/useflags/dbi)                 Enable dev-db/libdbi (database-independent abstraction layer) support
  [`gnutls`](https://packages.gentoo.org/useflags/gnutls)           Build module for TLS via net-libs/gnutls
  [`kerberos`](https://packages.gentoo.org/useflags/kerberos)       Add kerberos support
  [`ldap`](https://packages.gentoo.org/useflags/ldap)               Add LDAP support (Lightweight Directory Access Protocol)
  [`libdeflate`](https://packages.gentoo.org/useflags/libdeflate)   Enable output compression via app-arch/libdeflate
  [`maxminddb`](https://packages.gentoo.org/useflags/maxminddb)     Add support for geolocation using dev-libs/libmaxminddb
  [`mbedtls`](https://packages.gentoo.org/useflags/mbedtls)         Build module for TLS via net-libs/mbedtls
  [`nss`](https://packages.gentoo.org/useflags/nss)                 Build module for TLS via Mozilla\'s Network Security Services
  [`php`](https://packages.gentoo.org/useflags/php)                 Include support for the PHP language
  [`sasl`](https://packages.gentoo.org/useflags/sasl)               Add support for the Simple Authentication and Security Layer
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`ssl`](https://packages.gentoo.org/useflags/ssl)                 Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  [`unwind`](https://packages.gentoo.org/useflags/unwind)           Add support for call stack unwinding and function name resolution
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  [`webdav`](https://packages.gentoo.org/useflags/webdav)           Enable webdav properties
  [`xattr`](https://packages.gentoo.org/useflags/xattr)             Add support for extended attributes (filesystem-stored metadata)
  [`zstd`](https://packages.gentoo.org/useflags/zstd)               Enable output compression via Zstandard (app-arch/zstd) algorithm
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-21 08:45] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[www-servers/lighttpd]](https://packages.gentoo.org/packages/www-servers/lighttpd)[]]:

`root `[`#`]`emerge --ask www-servers/lighttpd`

## [Configuration]

The lighttpd configuration is handled by [/etc/lighttpd/lighttpd.conf]. The first example shows a single-site access, with SSL and no dynamic capabilities (such as [PHP](https://wiki.gentoo.org/wiki/PHP "PHP")).

[FILE] **`/etc/lighttpd/lighttpd.conf`Example 1**

    server.modules += ("mod_openssl")
    $SERVER["socket"] == "192.0.2.10:443"

To enable additional functionalities configure needed modules in [/etc/lighttpd/lighttpd.conf]. For instance, to enable PHP using the FastCGI processor:

[FILE] **`/etc/lighttpd/lighttpd.conf`Example 2 - Enabling PHP support**

    ...
    include "mod_fastcgi.conf"
    ...

### [IP access lists]

This third example shows how to allow access to a particular site */server-status* only to certain IP addresses. To allow using service status for the external host having an IP address: *198.51.100.1* and for the localhost *127.0.0.1*, set the following lines in the [lighttpd.conf] file:

[FILE] **`/etc/lighttpd/lighttpd.conf`Example 3 - Enabling and configuring an IP access lists for /server-status page**

    # enable access module
    server.modules =
    ...
    # enable server-status page globally
    status.status-url  = "/server-status"

    ...
    # restrict access to server-status to listed IP hosts
    $HTTP["remoteip"] !~ "198.51.100.1|127.0.0.1"

### [Start up]

In order for the [lighttpd] service to start automatically it must be properly added to the init handler program. Gentoo has two main init handler programs: [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") and [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd").

#### [OpenRC]

With OpenRC use the [rc-update] command:

`root `[`#`]`rc-update add lighttpd default`

#### [systemd]

With systemd use the [systemctl] command:

`root `[`#`]`systemctl enable lighttpd.service`

## [Troubleshooting]

Verifying [/etc/lighttpd/lighttpd.conf] configuration file with [lighttpd-angel], it will return the exit code `0`, if everything is configured properly:

`root `[`#`]`lighttpd-angel -t -f /etc/lighttpd/lighttpd.conf`

    Syntax OK
    lighttpd-angel.c.140: child (pid=32491) exited normally with exitcode: 0

If the configuration file has errors, it will print it to stdout, like in the example below:

`root `[`#`]`lighttpd-angel -t -f /etc/lighttpd/lighttpd.conf`

    2012-09-02 12:52:08: (plugin.c.131) Cannot load plugin mod_fastcgi more than once, please fix your config
    2012-09-02 12:52:08: (network.c.379) can't bind to port: 192.168.0.1 80 Address already in use
    lighttpd-angel.c.140: child (pid=32139) exited normally with exitcode: 255

## [See also]

-   [Apache](https://wiki.gentoo.org/wiki/Apache "Apache") --- an efficient, extensible [web server](https://wiki.gentoo.org/wiki/Category:Web_servers "Category:Web servers"). It is one of the most popular web servers used the Internet.
-   [Nginx](https://wiki.gentoo.org/wiki/Nginx "Nginx") --- a robust, small, high performance [web server](https://wiki.gentoo.org/wiki/Category:Web_servers "Category:Web servers") and reverse proxy server.

## [External resources]

-   [https://redmine.lighttpd.net/projects/lighttpd/wiki](https://redmine.lighttpd.net/projects/lighttpd/wiki) - The Lighttpd wiki.