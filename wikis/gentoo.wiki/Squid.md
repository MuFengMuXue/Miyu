[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Squid&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](http://www.squid-cache.org/)

[[]][Package information](https://packages.gentoo.org/packages/net-proxy/squid)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Squid_(software) "wikipedia:Squid (software)")

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/squid)

**Squid** is a web cache and a proxy server application used speed up web browsing.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Boot services]](#Boot_services)
    -   [[2.1] [OpenRC]](#OpenRC)
-   [[3] [SSL configuration]](#SSL_configuration)
    -   [[3.1] [Certificate generation]](#Certificate_generation)
    -   [[3.2] [Configure Squid]](#Configure_Squid)
-   [[4] [Monitoring Configuration]](#Monitoring_Configuration)
-   [[5] [Browser configuration]](#Browser_configuration)
    -   [[5.1] [Firefox]](#Firefox)
-   [[6] [Custom error page icons]](#Custom_error_page_icons)
-   [[7] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [net-proxy/squid](https://packages.gentoo.org/packages/net-proxy/squid) [[]] [Full-featured web proxy cache]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+htcp`](https://packages.gentoo.org/useflags/+htcp)             Enable HTCP protocol
  [`+wccp`](https://packages.gentoo.org/useflags/+wccp)             Enable Web Cache Coordination Protocol
  [`+wccpv2`](https://packages.gentoo.org/useflags/+wccpv2)         Enable Web Cache Coordination V2 Protocol
  [`caps`](https://packages.gentoo.org/useflags/caps)               Use Linux capabilities library to control privilege
  [`ecap`](https://packages.gentoo.org/useflags/ecap)               Adds support for loadable content adaptation modules (http://www.e-cap.org)
  [`esi`](https://packages.gentoo.org/useflags/esi)                 Enable ESI for accelerators, will cause squid reverse proxies to be capable of the Edge Acceleration Specification (www.esi.org)
  [`gnutls`](https://packages.gentoo.org/useflags/gnutls)           Prefer net-libs/gnutls as SSL/TLS provider (ineffective with USE=-ssl)
  [`kerberos`](https://packages.gentoo.org/useflags/kerberos)       Add kerberos support
  [`ldap`](https://packages.gentoo.org/useflags/ldap)               Add LDAP support (Lightweight Directory Access Protocol)
  [`logrotate`](https://packages.gentoo.org/useflags/logrotate)     Use app-admin/logrotate for rotating logs
  [`mysql`](https://packages.gentoo.org/useflags/mysql)             Add mySQL Database support
  [`nis`](https://packages.gentoo.org/useflags/nis)                 Support for NIS/YP services
  [`pam`](https://packages.gentoo.org/useflags/pam)                 Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`perl`](https://packages.gentoo.org/useflags/perl)               Add optional support/bindings for the Perl language
  [`postgres`](https://packages.gentoo.org/useflags/postgres)       Add support for the postgresql database
  [`qos`](https://packages.gentoo.org/useflags/qos)                 Adds support for Quality of Service using netfilter conntrack - see qos_flow directive for more info
  [`radius`](https://packages.gentoo.org/useflags/radius)           Add support for RADIUS authentication
  [`samba`](https://packages.gentoo.org/useflags/samba)             Add support for SAMBA (Windows File and Printer sharing)
  [`sasl`](https://packages.gentoo.org/useflags/sasl)               Add support for the Simple Authentication and Security Layer
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`snmp`](https://packages.gentoo.org/useflags/snmp)               Add support for the Simple Network Management Protocol if available
  [`sqlite`](https://packages.gentoo.org/useflags/sqlite)           Add support for sqlite - embedded sql database
  [`ssl`](https://packages.gentoo.org/useflags/ssl)                 Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  [`ssl-crtd`](https://packages.gentoo.org/useflags/ssl-crtd)       Adds support for dynamic SSL certificate generation in SslBump environments
  [`systemd`](https://packages.gentoo.org/useflags/systemd)         Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`tproxy`](https://packages.gentoo.org/useflags/tproxy)           Enables real Transparent Proxy support for Linux Netfilter TPROXY
  [`valgrind`](https://packages.gentoo.org/useflags/valgrind)       Enable annotations for accuracy. May slow down runtime slightly. Safe to use even if not currently using dev-debug/valgrind
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-14 04:28] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[net-proxy/squid]](https://packages.gentoo.org/packages/net-proxy/squid)[]]:

`root `[`#`]`emerge --ask net-proxy/squid`

## [Boot services]

### [OpenRC]

To start squid on boot:

`root `[`#`]`rc-update add squid default`

To start squid immediately:

`root `[`#`]`rc-service squid start`

## [SSL configuration]

Make sure the `ssl` USE flag has been enabled. At the time of writing, Google Chrome, Chromium, and Firefox 30+ have support for SSL proxies. Unfortunately configuring them is not as straight forward as going into the options dialog of each respective browser.

### [Certificate generation]

Generate a self-signed SSL certificate, or use a CA to sign the certificate so it is trusted by all clients.

`user `[`$`]`openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -nodes`

### [Configure Squid]

Edit Squid\'s config file located at [/etc/squid/squid.conf], replacing the `http_port 3128` line with:

[FILE] **`/etc/squid/squid.conf`Modifying Squid configuration to use a SSL proxy**

    https_port 3128 cert=/etc/squid/cert.pem key=/etc/squid/key.pem

## [Monitoring Configuration]

The following configuration enables a HTTP endpoint on localhost only to retrieve statistics for monitoring.

[FILE] **`/etc/squid/squid.conf`Modifying Squid configuration for monitoring**

    # use simple credential/ HTTP Basic auth and only for info-endpoint
    cachemgr_passwd YourPasswordHere info
    # deny all the other endpoints like configuration or restart
    cachemgr_passwd disable all

    # Restrict manager to localhost
    http_access allow localhost manager
    # deny all access from anywhere else
    http_access deny manager

After a reload of the service the following command prints statistics. See the bottom of this page for tools shipped with Squid. Preferably use plain wget or cURL. Also never write passwords in plain text as part of commands. Use Bash\'s `read` or proper secrets management instead. (With the above settings and for info endpoint only this is not critical.)

`user `[`$`]`wget --user 'manager' --password YourPasswordHere -O - `[`http://localhost:3128/squid-internal-mgr/info`](http://localhost:3128/squid-internal-mgr/info)

## [Browser configuration]

### [Firefox]

Set [Firefox](https://wiki.gentoo.org/wiki/Firefox "Firefox") to manual proxy, and point it at `localhost port 3128` or `127.0.0.1 port 3128`.

## [Custom error page icons]

CSS controls the Squid icon on error pages. To insert a custom icon simply replace the link URL in [/etc/squid/errorpage.css] section #titles (as long as a 91x50 pixel image is used nothing else needs to be changed). To use a different size image make sure padding is .5 x height and padding left is exactly width of future image replacement.

Once modifications have been finished, restart the Squid service:

`root `[`#`]`rc-service squid restart`

## [See also]

-   [https://bugs.squid-cache.org/show_bug.cgi?id=5283](https://bugs.squid-cache.org/show_bug.cgi?id=5283) -- squidclient broken and queued for removal with 7.0.0