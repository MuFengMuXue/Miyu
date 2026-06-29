Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/IPv6_router_guide/es "Guía del enrutador IPv6 (41% translated)")
-   [français](https://wiki.gentoo.org/wiki/IPv6_router_guide/fr "Guide du routeur IPv6 (28% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/IPv6_router_guide/hu "IPv6 router útmutató (97% translated)")
-   [русский](https://wiki.gentoo.org/wiki/IPv6_router_guide/ru "Руководство по развертыванию IPv6-маршрутизатора (46% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/IPv6_router_guide/zh-cn "IPv6 router guide (1% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/IPv6_router_guide/ja "IPv6 ルータガイド (70% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/IPv6_router_guide/ko "IPv6 router guide/ko (37% translated)")

\
This guide provides details on setting up a Gentoo Linux system as an [IPv6](https://wiki.gentoo.org/wiki/IPv6 "IPv6") router.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Emerge]](#Emerge)
        -   [[1.2.1] [Additional software]](#Additional_software)
    -   [[1.3] [Confirming IPv6 status]](#Confirming_IPv6_status)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Obtaining an address and prefix]](#Obtaining_an_address_and_prefix)
    -   [[2.2] [Enable forwarding]](#Enable_forwarding)
    -   [[2.3] [Stateless configuration]](#Stateless_configuration)
    -   [[2.4] [Stateful configuration]](#Stateful_configuration)
    -   [[2.5] [Service]](#Service)
        -   [[2.5.1] [OpenRC]](#OpenRC)
-   [[3] [DNS setup]](#DNS_setup)
    -   [[3.1] [IPv6 and DNS]](#IPv6_and_DNS)
    -   [[3.2] [BIND configuration]](#BIND_configuration)
    -   [[3.3] [DJBDNS configuration]](#DJBDNS_configuration)
-   [[4] [IPv6 clients]](#IPv6_clients)
    -   [[4.1] [Using radvd]](#Using_radvd)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Package is missing IPv6 support]](#Package_is_missing_IPv6_support)
-   [[6] [See Also]](#See_Also)
-   [[7] [External resources]](#External_resources)

## [Installation]

### [Kernel]

Any kernels version v2.6.0 or higher can support [IPv6](https://www.linux-ipv6.org/).

`root `[`#`]`emerge --ask sys-kernel/gentoo-sources`

[KERNEL] **Required IPv6 options**

    [*] Networking support --->
        Networking options --->
            <M> The IPv6 protocol --->

### [Emerge]

`root `[`#`]`emerge --ask sys-apps/iproute2`

`root `[`#`]`emerge --ask net-misc/radvd`

** Tip**\
The `ipv6` USE variable may need to be enabled for some packages, and can be added to [/etc/portage/make.conf].

#### [Additional software]

There are a few packages which specifically deal with IPv6 items. Most of these are located in the [net-misc](https://packages.gentoo.org/categories/net-misc) category.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------
  Package                                                                                                                                                                                                                                                                                                                                                                     Description
  [[[net-misc/radvd]](https://packages.gentoo.org/packages/net-misc/radvd)[]]            Router advertisement daemon
  [[[net-misc/dhcpd]](https://packages.gentoo.org/packages/net-misc/dhcpd)[]]            ISC DHCP server, DHCPv4 and DHCPv6 capability
  [[[net-misc/dibbler]](https://packages.gentoo.org/packages/net-misc/dibbler)[]]      DHCPv6 server
  [[[net-misc/ipv6calc]](https://packages.gentoo.org/packages/net-misc/ipv6calc)[]]   Converts an IPv6 address to a compressed format
  [[[dev-perl/Socket6]](https://packages.gentoo.org/packages/dev-perl/Socket6)[]]      IPv6 related part of the C socket.h defines and structure manipulators
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------

### [Confirming IPv6 status]

If IPv6 is enabled, the loopback device should show an IPv6 address:

`root `[`#`]`ip -6 addr show lo`

    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
        inet6 ::1/128 scope host
           valid_lft forever preferred_lft forever

## [Configuration]

### [Obtaining an address and prefix]

[dhcpcd] can be used to obtain a single, host only, /128 IPv6 address for the *WAN* interface, and a /64 IPv6 prefix for the *LAN* interface.

[FILE] **`/etc/dhcpcd.conf`Request a IPv6 prefix for *eth0.lan* and *eth0.management* to be routed publicly with *eth0.wan*.**

    # Disable router solicitations for all interfaces, enable only for selected ones
    noipv6rs

    # Interface configuration for the wan vlan on the eth0 interface
    interface eth0.wan
      # Enable router solicitation for this interface
      ipv6rs
      # Request a normal address usins iaid 1 for interface eth0.wan
      ia_na 1
      # Request a prefix using iaid 2 and assign it to the eth0.lan interface using sla_id 0 and prefix size of 64
      ia_pd 2 eth0.lan/0/64

** See also**\
[Dhcpcd](https://wiki.gentoo.org/wiki/Dhcpcd "Dhcpcd")

** Warning**\
[rfc6177](https://datatracker.ietf.org/doc/html/rfc6177) is barely seen as a recommendation by residential ISPs, Prefix Delegation may not work.

### [Enable forwarding]

IPv6 packet forwarding must be enabled in kernel before a system can function as a router, this can be done using [sysctl]:

`root `[`#`]`sysctl -w net.ipv6.conf.all.forwarding=1`

** Important**\
The [radvd] init script used later enables (and disables) forwarding, making the next step unnecessary.

To assign IPv6 addresses to clients, the IPv6 specification allows both methods, stateless and stateful IP assignment. The IPv6 Stateless Address Autoconfiguration uses a process called Router Advertisement and allows clients to obtain an IP and a default route by simply bringing an interface up. It is called \"stateless\" because there is no record of IPs assigned and the host they are assigned to. Stateful assignment is handled by DHCPv6. It is \"stateful\" because the server keeps a state of the clients who have requested IPs and received them.

** Note**\
The IPv6 Stateless Address Autoconfiguration configures IP routing and connectivity, the DHCPv6 is required to assign IPv6 addresses, and provide information such as DNS servers.

### [Stateless configuration]

Stateless configuration is easily accomplished using the Router Advertisement Daemon, or [radvd]:

[/etc/radvd.conf] is used to configure [radvd], and is not created by default. If the IPv6 prefix configuration is left empty, the already assigned or configured IPv6 prefix is used:

[FILE] **`/etc/radvd.conf`Router Advertisement (RA) configuration for the *eth0.lan* interface.**

    interface eth0.lan
    ;
    };

** Important**\
The Router Advertisements (RA) are send periodically on the *eth0.lan* interface to the all-nodes multicast address. Using an interface connected to the LAN, local area network.

** Tip**\
Further information is available in [man radvd.conf].

### [Stateful configuration]

** Warning**\
Dibbler project is concluded.

To have a stateful configuration, install and configure [[[net-misc/dibbler]](https://packages.gentoo.org/packages/net-misc/dibbler)[]].

`root `[`#`]`emerge --ask dibbler`

Configure the dibbler client by editing [/etc/dibbler/client.conf].

[CODE] **Sample dibbler client configuration**

    iface ppp0

Now start the dibbler client, and configure it to start at boot:

`root `[`#`]`rc-service dibbler-client start `

`root `[`#`]`rc-update add dibbler-client default `

### [Service]

#### [OpenRC]

To start [radvd] and start it on boot:

`root `[`#`]`rc-service radvd start `

`root `[`#`]`rc-update add radvd default `

## [DNS setup]

### [IPv6 and DNS]

Just as DNS for IPv4 uses A records, DNS for IPv6 uses AAAA records. (This is because IPv4 is an address space of 2\^32 while IPv6 is an address space of 2\^128). For reverse DNS, the INT standard is deprecated but still widely supported. ARPA is the latest standard. Support for the ARPA format will be described here.

### [BIND configuration]

Recent versions of BIND include excellent IPv6 support. This section will assume at least minimal knowledge about the configuration and use of BIND. We will assume that bind is not running in a chroot. If this assumption is wrong, simply append the chroot prefix to most of the paths in the following section.

First add entries for both forward and reverse DNS zone files in [/etc/bind/named.conf].

[FILE] **`/etc/bind/named.conf`named.conf entries**

    ## (We allow bind to listen to IPv6 addresses.
    ## Using 'any' is the only way to do it prior to bind-9.3)
    options
        [...]
    };
    ## (This will provide the forward DNS for the domain 'ipv6-rules.com':)
    zone "ipv6-rules.com" IN ;
    ## (This format for reverse DNS is "bitwise." It's done by taking the IPv6 prefix,
    ## reversing the order of the numbers and putting a period between each number)
    zone "6.9.2.0.0.0.f.1.0.7.4.0.1.0.0.2.ip6.arpa" ;

Now zone files and entries will need added for all hosts:

[FILE] **`/etc/bind/pri/ipv6-rules.com`**

    $TTL    2h
    @       IN      SOA     ipv6-rules.com. webmaster.ipv6-rules.com.  (
                                    2003052501 ; Serial
                                    28800      ; Refresh
                                    14400      ; Retry
                                    3600000    ; Expire
                                    86400 )    ; Minimum
                    NS      ns1.ipv6-rules.com

    IN      AAAA    2001:470:1f00:296::1 ; address for ipv6-rules.com
    host1   IN      AAAA    2001:470:1f00:296::2 ; address for host1.ipv6-rules.com
    host2   IN      AAAA    2001:470:1f00:296::3:3 ; address for host2.ipv6-rules.com

[FILE] **`/etc/bind/pri/ipv6-rules.com.arpa`**

    $TTL 3d ; Default TTL (bind 8 needs this, bind 9 ignores it)
    @       IN SOA ipv6-rules.com. webmaster.ipv6-rules.com. (
                            2003052501      ; Serial number (YYYYMMdd)
                            24h             ; Refresh time
                            30m             ; Retry time
                            2d              ; Expire time
                            3d )            ; Default TTL
            IN      NS     ns1.ipv6-rules.com.
    ; IPv6 PTR entries
    $ORIGIN 6.9.2.0.0.0.f.1.0.7.4.0.1.0.0.2.ip6.arpa.

    1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0 IN      PTR     ipv6-rules.com.
    2.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0 IN      PTR     host1.ipv6-rules.com.
    3.0.0.0.3.0.0.0.0.0.0.0.0.0.0.0 IN      PTR     host2.ipv6-rules.com.

### [DJBDNS configuration]

There are currently some third-party patches available to the [[[net-dns/djbdns]](https://packages.gentoo.org/packages/net-dns/djbdns)[]] package that allow it to do IPv6 name serving. DJBDNS can be installed with these patches by emerging it with `ipv6` in the USE variable.

** Warning**\
Not all record types are support yet with these patches. In particular, NS and MX records are not supported.

`root `[`#`]`emerge --ask net-dns/djbdns`

After djbdns is installed, it can be setup by running [tinydns-setup] and answering a few questions about which IP addresses to bind to, where to install tinydns, etc.

`root `[`#`]`tinydns-setup`

Assuming [tinydns] has been installed into [/var/tinydns], edit [/var/tinydns/root/data]. This file will contain all the data needed to get tinydns handling DNS for the IPv6 delegation.

[CODE] **sample data file**

    ## (*.ipv6-rules.com is authoritatively handled by 192.168.0.1)
    .ipv6-rules.com:192.168.0.1:a:259200
    ## (Authoritative reverse DNS for 2001:470:1f00:296::/64)
    .6.9.2.0.0.0.f.1.0.7.4.0.1.0.0.2.ip6.arpa:192.168.0.1:a
    ## (Specify the IPs for host1 and host2)
    6host1.ipv6-rules.com:200104701f0002960000000000000001:86400
    6host2.ipv6-rules.com:200104701f0002960000000000000002:86400
    ## (Point www to host1)
    3www.ipv6-rules.com:200104701f0002960000000000000002:86400

Lines prefixed with a `6` will have both an AAAA and a PTR record created. Those prefixed with a `3` will only have an AAAA record created. Besides manually editing the [data] file, it is possible to use the scripts [add-host6] and [add-alias6] to add new entries. After changes are made to the [data] file, simply run `make` from [/var/tinydns/root]. This will create [/var/tinydns/root/data.cfb], which tinydns will use as its source of information for DNS requests.

## [IPv6 clients]

### [Using radvd]

Clients behind this router should now be able to connect to the rest of the net via IPv6. If using radvd, configuring hosts should be as easy as bringing the interface up. (This is probably already done by the net.ethX init scripts).

`root `[`#`]`ip link set eth0 up `

`root `[`#`]`ip addr show eth0`

    1: eth0: <BROADCAST,MULTICAST,UP> mtu 1400 qdisc pfifo_fast qlen 1000
        link/ether 00:01:03:2f:27:89 brd ff:ff:ff:ff:ff:ff
        inet6 2001:470:1f00:296:209:6bff:fe06:b7b4/128 scope global
           valid_lft forever preferred_lft forever
        inet6 fe80::209:6bff:fe06:b7b4/64 scope link
           valid_lft forever preferred_lft forever
        inet6 ff02::1/128 scope global
           valid_lft forever preferred_lft forever

Should this not work ensure that the IPv6 firewall is allowing ICMPv6 packets through:

`root `[`#`]`ip6tables -A INPUT -p icmpv6 -j ACCEPT`

## [Troubleshooting]

### [Package is missing IPv6 support]

Packages will typically emerge with the `ipv6` *USE* flag, but if IPv6 is not working on a specific program, checking that it is built with that is a good first step.

** Note**\
There is no issue adding `USE="ipv6"` to [/etc/portage/make.conf], but this is often unnecessary.

** Note**\
Some packages (erroneously) detect IPv6 support automatically and hence have no ipv6 USE flag. Thus not all packages, which should support IPv6, will support it if they have not been compiled with an IPv6 enabled kernel.

## [See Also]

-   [IPv6](https://wiki.gentoo.org/wiki/IPv6 "IPv6") --- the most recent version of the [Internet Protocol](https://en.wikipedia.org/wiki/Internet_Protocol "wikipedia:Internet Protocol") (IP)
-   [IPv6 tunnels](https://wiki.gentoo.org/wiki/IPv6_tunnels "IPv6 tunnels")

## [External resources]

There are many excellent resources online pertaining to IPv6.

-   [www.ipv6.org](http://www.ipv6.org/) - General IPv6 information
-   [www.linux-ipv6.org/](http://www.linux-ipv6.org/) - USAGI project
-   [www.deepspace6.net](http://www.deepspace6.net/) - Linux/IPv6 site
-   [www.kame.net](http://www.kame.net/) - \*BSD implementation
-   [RFC 4861 - Neighbor Discovery for IP version 6 (IPv6)](https://www.rfc-editor.org/rfc/rfc4861.html)
-   [RFC 4862 - IPv6 Stateless Address Autoconfiguration](https://www.rfc-editor.org/rfc/rfc4862.html)

On IRC, try the [[#ipv6](ircs://irc.libera.chat/#ipv6)] ([[webchat](https://web.libera.chat/#ipv6)]) channel on [Libera.Chat](https://www.libera.chat/). Connect to the Libera.Chat servers using an IPv6 enabled client by connecting to irc.ipv6.libera.chat.

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Peter Johanson, Jorge Paulo, Camille Huot, Pasi Valminen, , [Markos Chandras (Hwoarang)](https://wiki.gentoo.org/wiki/User:Hwoarang "User:Hwoarang") **\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*