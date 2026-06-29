[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Unbound&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.nlnetlabs.nl/projects/unbound/about/)

[[]][Official documentation](https://unbound.docs.nlnetlabs.nl/en/latest/)

[[]][Package information](https://packages.gentoo.org/packages/net-dns/unbound)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Unbound_(DNS_server) "wikipedia:Unbound (DNS server)")

[[]][GitHub](https://github.com/NLnetLabs/unbound)

**Unbound** is a validating, recursive, caching DNS resolver.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Additional software]](#Additional_software)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [DNSSEC Configuration]](#DNSSEC_Configuration)
    -   [[2.3] [Service]](#Service)
        -   [[2.3.1] [OpenRC]](#OpenRC)
-   [[3] [Removal]](#Removal)
    -   [[3.1] [Unmerge]](#Unmerge)

## [Installation]

### [USE flags]

### [USE flags for] [net-dns/unbound](https://packages.gentoo.org/packages/net-dns/unbound) [[]] [A validating, recursive and caching DNS resolver]

  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+ecdsa`](https://packages.gentoo.org/useflags/+ecdsa)             Enable ECDSA support
  [`+http2`](https://packages.gentoo.org/useflags/+http2)             Enable HTTP/2 support for DoHnet-libs/nghttp2
  [`+tfo`](https://packages.gentoo.org/useflags/+tfo)                 Enable TCP Fast Open client+server
  [`debug`](https://packages.gentoo.org/useflags/debug)               Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`dnscrypt`](https://packages.gentoo.org/useflags/dnscrypt)         Enable DNSCrypt support
  [`dnstap`](https://packages.gentoo.org/useflags/dnstap)             Enable dnstap support
  [`ecs`](https://packages.gentoo.org/useflags/ecs)                   Enable EDNS client subnet support
  [`gost`](https://packages.gentoo.org/useflags/gost)                 Enable GOST support
  [`python`](https://packages.gentoo.org/useflags/python)             Add optional support/bindings for the Python language
  [`redis`](https://packages.gentoo.org/useflags/redis)               Enable cache db backend which usesdev-libs/hiredis
  [`selinux`](https://packages.gentoo.org/useflags/selinux)           !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`static-libs`](https://packages.gentoo.org/useflags/static-libs)   Build static versions of dynamic libraries as well
  [`systemd`](https://packages.gentoo.org/useflags/systemd)           Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)                 Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`threads`](https://packages.gentoo.org/useflags/threads)           Add threads support for various packages. Usually pthreads
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)     Verify upstream signatures on distfiles
  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-21 04:24] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask net-dns/unbound`

### [Additional software]

For testing DNS resolving, use [dig] part of the [[[net-dns/bind]](https://packages.gentoo.org/packages/net-dns/bind)[]] package.

## [Configuration]

### [Files]

-   [/etc/unbound/unbound.conf] - Global (system wide) configuration file.

### [DNSSEC Configuration]

To be able to use dnssec validation, a trust anchor (file) needs to be created and pointed to from the unbound configuration file.

One can use the [unbound-anchor] tool that comes with the unbound install to create the initial trust anchor, BUT as indicated in the manual, this is at your own risk and you MUST validate the trust anchor thus created. Please see unbound documentation for details.

Alternative the anchor can be found in the root zone file than can be downloaded at [https://www.internic.net/domain/root.zone](https://www.internic.net/domain/root.zone) and searching for DNSKEY. Again care is need to validate this is indeed the correct public key.

As of May 2022, as an example ONLY (please don\'t use unless it has verified it by other means), this is what was found looking in the root.zone file.

. IN DNSKEY 257 3 8 AwEAAaz/tAm8yTn4Mfeh5eyI96WSVexTBAvkMgJzkKTOiW1vkIbzxeF3+/4RgWOq7HrxRixH lFlExOLAJr5emLvN7SWXgnLh4+B5xQlNVz8Og8kvArMtNROxVQuCaSnIDdD5LKyWbRd2n9WGe2R8PzgCmr3EgVLrjyBxWezF0jLHwVN8efS3rCj/ EWgvIWgb9tarpVUDK/b58Da+sqqls3eNbuv7pr+eoZG+SrDK6nWeL3c6H5Apxz7LjVc1uTIdsIXxuOLYA4/ilBmSVIzuDWfdRUfhHdY6+cn8HFRm +2hM8AnXGXws9555KrUB5qihylGa8subX2Nn6UwNR1AkUTV74bU=

Once created the anchor will need regular updates, this can be done by setting (in the configuration file) automatic updates. Thus uses the [unbound-anchor] tool to refresh the trust anchor file.

Assuming the file is named **/etc/unbound/var/dnssec-trust-anchors.key**\...

[FILE] **`/etc/unbound/unbound.conf`**

    ...

    server:

    ...
         auto-trust-anchor-file: "/etc/unbound/var/dnssec-trust-anchors.key"

### [Service]

#### [OpenRC]

`root `[`#`]`rc-update add unbound `

`root `[`#`]`rc-service unbound start `

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose net-dns/unbound`