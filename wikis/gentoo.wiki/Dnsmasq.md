Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/Dnsmasq/es "Dnsmasq (75% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Dnsmasq/it "Dnsmasq (61% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Dnsmasq/hu "Dnsmasq (91% translated)")
-   [polski](https://wiki.gentoo.org/wiki/Dnsmasq/pl "Dnsmasq (39% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Dnsmasq/ru "Dnsmasq (94% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Dnsmasq/zh-cn "Dnsmasq (78% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Dnsmasq/ja "Dnsmasq (92% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Dnsmasq/ko "Dnsmasq (61% translated)")

**Resources**

[[]][Home](http://www.thekelleys.org.uk/dnsmasq/doc.html)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Dnsmasq "wikipedia:Dnsmasq")

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/dnsmasq)

[dnsmasq] is a simple DHCP/DNS server which can be used in a local network of up to a 1000 clients. Key features are easy configuration and a small system footprint. It also has support for IPv6.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Service]](#Service)
        -   [[2.1.1] [OpenRC]](#OpenRC)
    -   [[2.2] [Service configuration]](#Service_configuration)
    -   [[2.3] [Main configuration file]](#Main_configuration_file)
    -   [[2.4] [Hosts file]](#Hosts_file)
    -   [[2.5] [Additional hosts file]](#Additional_hosts_file)
    -   [[2.6] [Upstream nameservers]](#Upstream_nameservers)
-   [[3] [Features]](#Features)
    -   [[3.1] [DNS services]](#DNS_services)
    -   [[3.2] [DNSSEC]](#DNSSEC)
    -   [[3.3] [DHCP services]](#DHCP_services)
    -   [[3.4] [Example: Local-only caching DNS server]](#Example:_Local-only_caching_DNS_server)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [Resetting leases]](#Resetting_leases)
    -   [[4.2] [Reloading non-main configuration settings]](#Reloading_non-main_configuration_settings)

## [Installation]

### [USE flags]

Make a proper USE flag selection:

### [USE flags for] [net-dns/dnsmasq](https://packages.gentoo.org/packages/net-dns/dnsmasq) [[]] [Small forwarding DNS server]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`+dhcp`](https://packages.gentoo.org/useflags/+dhcp)             Enable support for acting as a DHCP server.
  [`+dumpfile`](https://packages.gentoo.org/useflags/+dumpfile)     Include code to dump packets to a libpcap-format file for debugging
  [`+inotify`](https://packages.gentoo.org/useflags/+inotify)       Enable inotify filesystem monitoring support
  [`+loop`](https://packages.gentoo.org/useflags/+loop)             Include functionality to probe for and remove DNS forwarding loops
  [`auth-dns`](https://packages.gentoo.org/useflags/auth-dns)       Add support for acting as an authorative DNS server.
  [`conntrack`](https://packages.gentoo.org/useflags/conntrack)     Add support for Linux conntrack connection marking.
  [`dbus`](https://packages.gentoo.org/useflags/dbus)               Enable dbus support for anything that needs it (gpsd, gnomemeeting, etc)
  [`dhcp-tools`](https://packages.gentoo.org/useflags/dhcp-tools)   Install extra command line tools for manually managing DHCP leases.
  [`dnssec`](https://packages.gentoo.org/useflags/dnssec)           Enable support DNSSEC validation and caching.
  [`id`](https://packages.gentoo.org/useflags/id)                   Whether report \*.bind CHAOS info to clients, otherwise forward such requests upstream instead
  [`idn`](https://packages.gentoo.org/useflags/idn)                 Enable support for Internationalized Domain Names
  [`ipv6`](https://packages.gentoo.org/useflags/ipv6)               Add support for IP version 6
  [`libidn2`](https://packages.gentoo.org/useflags/libidn2)         Enable support for Internationalized Domain Names, via net-dns/libidn2 rather than net-dns/libidn
  [`lua`](https://packages.gentoo.org/useflags/lua)                 Enable Lua scripting support
  [`nettlehash`](https://packages.gentoo.org/useflags/nettlehash)   Use hashing functions from dev-libs/nettle
  [`nls`](https://packages.gentoo.org/useflags/nls)                 Add Native Language Support (using gettext - GNU locale utilities)
  [`script`](https://packages.gentoo.org/useflags/script)           Enable support for calling scripts when leases change.
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`static`](https://packages.gentoo.org/useflags/static)           !!do not set this during bootstrap!! Causes binaries to be statically linked instead of dynamically
  [`tftp`](https://packages.gentoo.org/useflags/tftp)               Enables built in TFTP server for netbooting.
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-15 07:06] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Next, install the [[[net-dns/dnsmasq]](https://packages.gentoo.org/packages/net-dns/dnsmasq)[]] package:

`root `[`#`]`emerge --ask net-dns/dnsmasq`

## [Configuration]

There are various resources that can be modified to change dnsmasq behavior. These include

-   the command line options as provided through [/etc/conf.d/dnsmasq]
-   the main configuration file ([/etc/dnsmasq.conf])

### [Service]

#### [OpenRC]

Add dnsmasq to the default runlevel if it needs to be started automatically:

`root `[`#`]`rc-update add dnsmasq default`

To start the service now:

`root `[`#`]`rc-service dnsmasq start`

### [Service configuration]

In [/etc/conf.d/dnsmasq], the command line options passed on to the dnsmasq daemon at start-up can be configured.

[FILE] **`/etc/conf.d/dnsmasq`Example dnsmasq service configuration**

    DNSMASQ_OPTS="--user=dnsmasq --group=dnsmasq -H /srv/virt/gentoo/hosts --max-cache-ttl=10"

### [Main configuration file]

The main configuration of dnsmasq is done through its configuration file, [/etc/dnsmasq.conf]. The file uses a `key[=value]` syntax and the one provided by the package is well documented and recommended to read through. Inside the file, or through the command line options, additional resources can be referred to (such as a DHCP hosts file).

Below is a sample configuration file:

[FILE] **`/etc/dnsmasq.conf`**

    # Listen only to this interface
    interface=eth1

    # Assign names based on mac address
    dhcp-host=00:1e:68:c2:ff:ee,endor,192.168.0.54,24h

    # Any other DHCP request gets an ip from this range
    dhcp-range=eth1,192.168.0.100,192.168.0.120,12h

    # Enable the TFTP server and set the root directory for files available via TFTP.
    enable-tftp
    tftp-root=/var/lib/tftpboot
    dhcp-boot=/pxelinux.0

After editing the configuration file, the service has to be restarted - reloading is supported, but for other resources.

`root `[`#`]`/etc/init.d/dnsmasq restart`

### [Hosts file]

The dnsmasq application uses the [/etc/hosts] file as one of its sources for providing DNS services, unless the `-h` (`--no-hosts`) command line argument is passed along.

If the [/etc/hosts] file is updated, the dnsmasq service needs to receive a SIGHUP signal in order to reload the settings. This is also supported through the init scripts\' *reload* command:

`root `[`#`]`/etc/init.d/dnsmasq reload`

This behavior can also be disabled through the `no-hosts` parameter in the configuration file.

### [Additional hosts file]

It is possible to refer to an (additional) hosts file to use as source for DNS queries. To do so, add the `-H /path/to/hostsfile` (`--addn-hosts=/path/to/hostsfile`) command line option. It is also possible to pass a directory; in that case, all files inside that directory will be treated as additional hosts files.

Similar to the standard hosts file, a SIGHUP signal reloads the file.

This behavior can also be set through the `addn-hosts` parameter in the configuration file.

### [Upstream nameservers]

By default, dnsmasq uses the name servers specified in [[/etc/resolv.conf](https://wiki.gentoo.org/wiki/Resolv.conf "Resolv.conf")] as its upstream nameservers.

A different file can be used through the `-r` (`--resolv-file`) command line option.

This behavior can also be set through the `resolv-file` parameter in the configuration file.

## [Features]

Dnsmasq supports DNS, TFTP, PXE, router advertisements and DHCP services. As such, it is a versatile network management tool for small and medium-sized networks.

### [DNS services]

In order to (only) provide DNS services, first identify the *upstream nameserver* to use. If this is the same nameserver as specified in [[/etc/resolv.conf](https://wiki.gentoo.org/wiki/Resolv.conf "Resolv.conf")] then no additional steps need to be taken. Otherwise, point dnsmasq to the proper [resolv.conf] file through the `-r` (`--resolv-file`) command line. Its syntax is the one used by the [/etc/resolv.conf] file, although dnsmasq only looks at the *nameserver* definitions.

For instance:

`root `[`#`]`echo "nameserver 8.8.8.8" >> /etc/dnsmasq.conf.resolv`

Next point dnsmasq to this file through the configuration file:

[FILE] **`/etc/dnsmasq.conf`Configuring a custom resolv file**

    resolv-file=/etc/dnsmasq.conf.resolv

To verify that the service is running (after restarting as the configuration file has just been changed), use the [dig] command (provided through [[[net-dns/bind]](https://packages.gentoo.org/packages/net-dns/bind)[]]), asking the DNS server (running on localhost in the following example) to resolve a local or remote address:

`user `[`$`]`dig @localhost +short www.gentoo.org`

    www-bytemark-v4v6.gentoo.org.
    89.16.167.134

### [DNSSEC]

Dnsmasq can validate DNSSEC data while passing through data. This can be accomplished by adding these lines to the config file (remember to enable `dnssec` USE flag):

[FILE] **`/etc/dnsmasq.conf`Enabling DNSSEC**

    # Uncomment these to enable DNSSEC validation and caching:
    # (Requires dnsmasq to be built with DNSSEC option.)
    conf-file=/usr/share/dnsmasq/trust-anchors.conf
    dnssec

    # Replies which are not DNSSEC signed may be legitimate, because the domain
    # is unsigned, or may be forgeries. Setting this option tells dnsmasq to
    # check that an unsigned reply is OK, by finding a secure proof that a DS
    # record somewhere between the root and the domain does not exist.
    # The cost of setting this is that even queries in unsigned domains will need
    # one or more extra DNS queries to verify.
    dnssec-check-unsigned

After this change dnsmasq will return SERVFAIL and no DNS data if the validation fails. If the validation succeeds it sets the *ad* (\"authenticated data\") flag. In case the domain does not support DNSSEC dnsmasq behaves as before.

### [DHCP services]

In order to enable the DHCP services of dnsmasq, use the `dhcp-range` configuration setting.

For instance, to enable IPv6 address configuration through router advertisement (RA) with infinite lease time, and IPv4 address configuration also with infinite lease time:

[FILE] **`/etc/dnsmasq.conf`Enabling IPv6 and IPv4 leases**

    dhcp-range=2001:db8:81:e2::,ra-only,infinite
    dhcp-range=192.168.100.100,192.168.100.149,infinite

It is possible to use static definitions for known hosts, either through the main configuration file (`dhcp-host=` settings) or through a separate file. If a separate file is used, point dnsmasq to it through the `--dhcp-hostsfile` command line option. The advantage of the latter approach is that it is sufficient to send a SIGHUP signal (or reload the service) in order to reread the entries, whereas definitions in the configuration file require a full service restart.

For more information about the syntax of the `dhcp-host` parameter please refer to the manual page or configuration file as its syntax is very extensive.

### [Example: Local-only caching DNS server]

A common use of this program, is caching DNS queries locally. This allows one to speed up DNS queries, especially on networks where UDP traffic is congested. To manage the upstream DNS server configuration dynamically, e.g. when roaming with a laptop, [[[net-dns/openresolv]](https://packages.gentoo.org/packages/net-dns/openresolv)[]] is used. Some of these configurations are copied verbatim from the [[[resolvconf.conf(5)]](https://man.archlinux.org/man/resolvconf.conf.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page. `USE=dbus` is required for dynamic configuration to function correctly.

[FILE] **`/etc/dnsmasq.conf`**

    listen-address=127.0.0.1
    conf-file=/etc/dnsmasq-conf.conf
    resolv-file=/etc/dnsmasq-resolv.conf
    enable-dbus  # openresolv will use D-BUS to reload dnsmasq on configuration changes
    bind-interfaces  # allow running multiple instances of dnsmasq for different purposes

[FILE] **`/etc/resolvconf.conf`**

    resolv_conf=/etc/resolv.conf
    name_servers=127.0.0.1
    dnsmasq_conf=/etc/dnsmasq-conf.conf
    dnsmasq_resolv=/etc/dnsmasq-resolv.conf

Don\'t forget to enable and start the dnsmasq service, as described earlier in this article.

If using [dhcpcd](https://wiki.gentoo.org/wiki/Dhcpcd "Dhcpcd") or [Netifrc](https://wiki.gentoo.org/wiki/Netifrc "Netifrc") to manage your network configuration, these programs will by default use `/sbin/resolvconf` to update the DNS configuration. [NetworkManager](https://wiki.gentoo.org/wiki/NetworkManager "NetworkManager") needs `USE=resolvconf`, although it also has a built-in method of spawning and configuring dnsmasq for each connection.

## [Usage]

This section covers various usage scenarios (maintenance and operational tasks) for the dnsmasq service.

### [Resetting leases]

Clients that had a network interface update which results in a different MAC address might not get the intended IP address immediately. This is because the dnsmasq service has provided this IP address to the old MAC address, and will wait until the lease of this address has expired before re-assigning it.

The dnsmasq service stores its leases in [/var/lib/misc/dnsmasq.leases]. If the lease needs to be removed faster, shut down the dnsmasq service, remove the lease from the [dnsmasq.leases] file and start the service again.

`root `[`#`]`/etc/init.d/dnsmasq stop `

`root `[`#`]`nano -w /var/lib/misc/dnsmasq.leases `

`root `[`#`]`/etc/init.d/dnsmasq start`

### [Reloading non-main configuration settings]

Next to the [dnsmasq.conf] file, the dnsmasq service can use external definitions for the following services:

-   DHCP host configuration entries (through `--dhcp-hostsfile` command line option)
-   DHCP options (through `--dhcp-optsfile` command line option)

When these files are modified, a SIGHUP signal has dnsmasq reload these configuration files.

** Note**\
The [resolv.conf] files are by default polled by dnsmasq; changes on these files are automatically picked up unless the `-n` (`--no-poll`) command line option is set or the `no-poll` configuration parameter is used.