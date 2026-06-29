**Resources**

[[]][Home](https://www.isc.org/bind/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/BIND "wikipedia:BIND")

[[]][BIND Administrator Reference Manual](https://bind9.readthedocs.io/en/latest/#)

[[]][Guide](https://wiki.gentoo.org/wiki/BIND/Guide "BIND/Guide")

[[]][[#bind](ircs://irc.libera.chat/#bind)] ([[webchat](https://web.libera.chat/#bind)])

[[]][[#dns](ircs://irc.libera.chat/#dns)] ([[webchat](https://web.libera.chat/#dns)])

**BIND**, or the **B**erkeley **I**nternet **N**ame **D**aemon, is a popular free software DNS server, and also one of the most frequently used name servers on the Internet.

With BIND, users are able to set up a name server for managing their own DNS records, for caching DNS, or acting as a slave DNS server. The software supports DNSSEC which provides cryptographic signatures on the DNS records as a means to natively authenticate the integrity and ownership of the records.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Service]](#Service)
        -   [[2.1.1] [OpenRC]](#OpenRC)
    -   [[2.2] [Chroots]](#Chroots)
    -   [[2.3] [Recipes]](#Recipes)
        -   [[2.3.1] [Easy caching DNS]](#Easy_caching_DNS)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Installation]

BIND is offered through the [[[net-dns/bind]](https://packages.gentoo.org/packages/net-dns/bind)[]] package. As with most packages, it is good practice to check the USE flags before emerging. Since BIND is a popular name server software, it is also a popular target for hackers and malicious groups. Is wise to securely configure BIND, which includes building in support for only features that will be actually used. If a feature will not be used, reduce the surface area of security vulnerabilities by disabling it.

### [USE flags]

### [USE flags for] [net-dns/bind](https://packages.gentoo.org/packages/net-dns/bind) [[]] [Berkeley Internet Name Domain - Name Server]

  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+caps`](https://packages.gentoo.org/useflags/+caps)               Use Linux capabilities library to control privilege
  [`dnstap`](https://packages.gentoo.org/useflags/dnstap)             Enables dnstap packet logging
  [`doc`](https://packages.gentoo.org/useflags/doc)                   Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`doh`](https://packages.gentoo.org/useflags/doh)                   Enables dns-over-https
  [`fixed-rrset`](https://packages.gentoo.org/useflags/fixed-rrset)   Enables fixed rrset-order option
  [`geoip`](https://packages.gentoo.org/useflags/geoip)               Add geoip support for country and city lookup based on IPs
  [`gssapi`](https://packages.gentoo.org/useflags/gssapi)             Enable gssapi support
  [`idn`](https://packages.gentoo.org/useflags/idn)                   Enable support for Internationalized Domain Names
  [`jemalloc`](https://packages.gentoo.org/useflags/jemalloc)         Use dev-libs/jemalloc for memory management
  [`lmdb`](https://packages.gentoo.org/useflags/lmdb)                 Enable LMDB support to store configuration for \'addzone\' zones
  [`selinux`](https://packages.gentoo.org/useflags/selinux)           !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`static-libs`](https://packages.gentoo.org/useflags/static-libs)   Build static versions of dynamic libraries as well
  [`systemtap`](https://packages.gentoo.org/useflags/systemtap)       Build support for profiling and tracing using dev-debug/systemtap
  [`test`](https://packages.gentoo.org/useflags/test)                 Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)     Verify upstream signatures on distfiles
  [`xml`](https://packages.gentoo.org/useflags/xml)                   Add support for XML files
  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-21 04:24] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask net-dns/bind`

## [Configuration]

### [Service]

#### [OpenRC]

To have automatically start BIND at system boot:

`root `[`#`]`rc-update add named default`

To start the service now:

`root `[`#`]`rc-service named start`

Most management of BIND is done through its [rndc] command, although the [/etc/init.d/named] (OpenRC) init script can be passed the following arguments, in addition the typical start/stop/restart routines:

`checkconfig`

`checkzones`

`reload`

For example:

`root `[`#`]`rc-service named reload`

### [Chroots]

System that will be using BIND in a chrooted environment should set the `CHROOT` variable in [/etc/conf.d/named] accordingly. Check the comments as well, as they provide information on automatically creating the chrooted environment using [emerge \--config].

### [Recipes]

#### [Easy caching DNS]

`root `[`#`]`echo 'dns_servers="127.0.0.1"' >> /etc/conf.d/net`

As root edit [/etc/bind/named.conf] add an internet service provider\'s DNS where the x.x.x.x are.

[FILE] **`/etc/bind/named.conf`**

    forwarders ;

`root `[`#`]`rc-service named restart`

`user `[`$`]`dig google.com`

## [See also]

-   [BIND (Security Handbook)](https://wiki.gentoo.org/wiki/Security_Handbook/Securing_services#Bind "Security Handbook/Securing services")

## [External resources]

-   [https://bind9.readthedocs.io/en/latest/#](https://bind9.readthedocs.io/en/latest/#) - Official BIND Administrator Reference Manual (ARM)
-   [https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/domain-name-server.html](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/domain-name-server.html) - The Linux Documenation Projects guide for BIND (a bit antiquated), but perhaps helpful reference maternal.
-   [https://zytrax.com/books/dns/](https://zytrax.com/books/dns/) - DNS for Rocket Scientists - A high quality, detailed open source guide to DNS.
-