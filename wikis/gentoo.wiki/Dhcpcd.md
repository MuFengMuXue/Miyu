Other languages:

-   [British English](https://wiki.gentoo.org/wiki/Dhcpcd/en-gb "Dhcpcd (19% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/Dhcpcd/es "Dhcpcd (47% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Dhcpcd/hu "dhcpcd (93% translated)")
-   [polski](https://wiki.gentoo.org/wiki/Dhcpcd/pl "Dhcpcd (28% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Dhcpcd/ru "Dhcpcd (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Dhcpcd/zh-cn "Dhcpcd (49% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Dhcpcd/ja "dhcpcd (91% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Dhcpcd/ko "dhcpcd/ko (37% translated)")

**Resources**

[[]][Home](https://roy.marples.name/projects/dhcpcd/)

[[]][GitWeb](https://roy.marples.name/git/dhcpcd.git/)

[[]][Package information](https://packages.gentoo.org/packages/net-misc/dhcpcd)

**D**ynamic **H**ost **C**onfiguration **P**rotocol **C**lient **D**aemon ([[[net-misc/dhcpcd]](https://packages.gentoo.org/packages/net-misc/dhcpcd)[]]) is a popular DHCP client capable of handling both IPv4 and IPv6 configuration.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Static IP addresses]](#Static_IP_addresses)
    -   [[2.3] [Static values for domain/search in resolv.conf]](#Static_values_for_domain.2Fsearch_in_resolv.conf)
    -   [[2.4] [IPv6 Prefix Request]](#IPv6_Prefix_Request)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
    -   [[3.2] [Run it as a service]](#Run_it_as_a_service)
    -   [[3.3] [Manually starting dhcpcd]](#Manually_starting_dhcpcd)
    -   [[3.4] [Renew a lease]](#Renew_a_lease)
    -   [[3.5] [Release a lease]](#Release_a_lease)
-   [[4] [Troubleshooting]](#Troubleshooting)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [net-misc/dhcpcd](https://packages.gentoo.org/packages/net-misc/dhcpcd) [[]] [A fully featured, yet light weight RFC2131 compliant DHCP client]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+embedded`](https://packages.gentoo.org/useflags/+embedded)     Embed the definitions of dhcp options in the dhcpcd executable
  [`+udev`](https://packages.gentoo.org/useflags/+udev)             Enable virtual/udev integration (device discovery, power and storage device support, etc)
  [`debug`](https://packages.gentoo.org/useflags/debug)             Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`ipv6`](https://packages.gentoo.org/useflags/ipv6)               Add support for IP version 6
  [`privsep`](https://packages.gentoo.org/useflags/privsep)         Enable support for privilege separation
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-10 21:49] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Use the following command to install dhcpcd:

`root `[`#`]`emerge --ask net-misc/dhcpcd`

## [Configuration]

### [Files]

All [dhcpcd] configuration can be set in the [/etc/dhcpcd.conf] file, but for most installations [dhcpcd] will work out of the box presuming most computers nowadays are behind a router or access point running a DHCP server. Though [man 5 dhcpcd.conf]^[\[1\]](#cite_note-manpage-1)^ will be helpful in case advanced configuration is required.

### [Static IP addresses]

In case the network interface card should be configured with a [static IP address](https://wiki.gentoo.org/wiki/Static_routing "Static routing"), add their data to [/etc/dhcpcd.conf].^[\[1\]](#cite_note-manpage-1)^ The following is an example of manually adding a static address, routes, and DNS by editing DHCPCD\'s configuration file using a text editor of choice:

[FILE] **`/etc/dhcpcd.conf`**

    static ip_address=192.168.0.10/24
    static routers=192.168.0.1
    static domain_name_servers=192.168.0.1

### [][Static values for domain/search in resolv.conf]

[FILE] **`/etc/dhcpcd.conf`**

    static domain_name=mynetwork
    static domain_search=mynetwork

** Note**\
The [[[resolv.conf(5)]](https://man.archlinux.org/man/resolv.conf.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page notes that \"\[t\]he domain directive is an obsolete name for the search directive that handles one search list entry only.\"

### [IPv6 Prefix Request]

[FILE] **`/etc/dhcpcd.conf`Request a prefix for *eth0.lan* and *eth0.management* to be routed publicly with *eth0.wan*.**

    # Disable router solicitations for all interfaces, enable only for selected ones
    noipv6rs

    # Interface configuration for the wan vlan on the eth0 interface
    interface eth0.wan
      # Enable router solicitation for this interface
      ipv6rs
      # Request a normal address using iaid 1 for interface eth0.wan
      ia_na 1
      # Request a prefix using iaid 2 and assign it to the eth0.lan interface using sla_id 0 and prefix size of 64
      ia_pd 2 eth0.lan/0/64
      # Request a prefix using iaid 3 and assign it to the eth0.management interface using sla_id 0 and prefix size of 64
      ia_pd 3 eth0.management/0/64

## [Usage]

### [Invocation]

`root `[`#`]`dhcpcd --help`

    usage: dhcpcd   [-146ABbDdEGgHJKLMNPpqTV]
            [-C, --nohook hook] [-c, --script script]
            [-e, --env value] [-F, --fqdn FQDN] [-f, --config file]
            [-h, --hostname hostname] [-I, --clientid clientid]
            [-i, --vendorclassid vendorclassid] [-j, --logfile logfile]
            [-l, --leasetime seconds] [-m, --metric metric]
            [-O, --nooption option] [-o, --option option]
            [-Q, --require option] [-r, --request address]
            [-S, --static value]
            [-s, --inform address[/cidr[/broadcast_address]]]
     [--inform6]        [-t, --timeout seconds] [-u, --userclass class]
            [-v, --vendor code, value] [-W, --whitelist address[/cidr]] [-w]
            [--waitip [4 | 6]] [-y, --reboot seconds]
            [-X, --blacklist address[/cidr]] [-Z, --denyinterfaces pattern]
            [-z, --allowinterfaces pattern] [--inactive] [interface] [...]
           dhcpcd   -n, --rebind [interface]
           dhcpcd   -k, --release [interface]
           dhcpcd   -U, --dumplease interface
           dhcpcd   --version
           dhcpcd   -x, --exit [interface]

### [Run it as a service]

See [Network management using DHCPCD](https://wiki.gentoo.org/wiki/Network_management_using_DHCPCD "Network management using DHCPCD").

### [Manually starting dhcpcd]

[dhcpd] can be manually started on a specific interface, such as [enp1s0] with:

`root `[`#`]`dhcpcd enp1s0`

Be sure to replace `enp1s0` in the command above with the appropriate network interface name.

### [Renew a lease]

To renew the lease on [enp1s0], **\--rebind** or **-n** can be used:

`root `[`#`]`dhcpcd -n enp1s0`

### [Release a lease]

To release a lease on [enp1s0], **\--release** or **-k** can be used:

`root `[`#`]`dhcpcd -k enp1s0`

## [Troubleshooting]

-   [dhcpcd not working for IPv6 (#CONFIG_PACKET is not set)](https://forums.gentoo.org/viewtopic-t-1068686.html)
-   If [/etc/resolv.conf] does not update with VPN\'s DNS, consider installing [[[net-dns/openresolv]](https://packages.gentoo.org/packages/net-dns/openresolv)[]].

## [See also]

-   [The Handbook\'s recommendations on handling network interfaces](https://wiki.gentoo.org/wiki/Handbook:AMD64/Networking/Introduction "Handbook:AMD64/Networking/Introduction")
-   [Netifrc](https://wiki.gentoo.org/wiki/Netifrc "Netifrc") --- Gentoo\'s default framework for configuring and [managing network](https://wiki.gentoo.org/wiki/Network_management "Network management") interfaces on systems running [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC").
-   [Network management using DHCPCD](https://wiki.gentoo.org/wiki/Network_management_using_DHCPCD "Network management using DHCPCD") --- explains how to use dhcpcd for complete network stack management.

## [External resources]

-   [Dhcpcd on the Arch Wiki](https://wiki.archlinux.org/index.php/Dhcpcd)
-   [Forums post: No Internet access when update to dhcpcd 6.10.0](https://forums.gentoo.org/viewtopic-p-7870084.html#7870084)
-   [DHCP](https://en.wikipedia.org/wiki/DHCP "wikipedia:DHCP") on Wikipedia
-   [RFC 2131 - Dynamic Host Configuration Protocol](https://tools.ietf.org/html/rfc2131)

## [References]

1.  [[↑ ^[1.0](#cite_ref-manpage_1-0)^ ^[1.1](#cite_ref-manpage_1-1)^] [[DHCPCD.CONF(5)](https://linux.die.net/man/5/dhcpd.conf), [Roy Marples\'s personal blog](https://roy.marples.name/blog/), March 9th, 2015. Retrieved on May 07th, 2015.]]

\