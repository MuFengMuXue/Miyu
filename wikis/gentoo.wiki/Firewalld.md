FirewallD is DBUS-enabled firewall software for Linux, which works on top of the in-kernel iptables firewall. It was created by Red Hat, but it is available on many Linux distributions, including in Gentoo as [[[net-firewall/firewalld]](https://packages.gentoo.org/packages/net-firewall/firewalld)[]].

From the [project homepage](https://firewalld.org/):

Firewalld provides a dynamically managed firewall with support for network/firewall zones that define the trust level of network connections or interfaces. It has support for IPv4, IPv6 firewall settings, ethernet bridges and IP sets. There is a separation of runtime and permanent configuration options. It also provides an interface for services or applications to add firewall rules directly.

Its [documentation is available on the project website](https://firewalld.org/documentation/) in HTML format.

## Contents

-   [[1] [Preparation]](#Preparation)
    -   [[1.1] [Kernel]](#Kernel)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [USE flags]](#USE_flags)
-   [[3] [Emerge]](#Emerge)
    -   [[3.1] [Services]](#Services)
        -   [[3.1.1] [OpenRC]](#OpenRC)
        -   [[3.1.2] [Systemd]](#Systemd)
        -   [[3.1.3] [Check status]](#Check_status)
-   [[4] [Configuration]](#Configuration)
-   [[5] [See Also]](#See_Also)
-   [[6] [References]](#References)

## [Preparation]

### [Kernel]

The following config options should be enabled in the kernel if using a manually compiled kernel like sys-kernel/gentoo-sources:

[KERNEL]

    [*] Networking support  --->
         Networking options  --->
             [*] Network packet filtering framework (Netfilter)  --->
                 IP: Netfilter Configuration  --->
                  [M] IPv4 socket lookup support
                  [M] IPv4 tproxy support
                  [*] IPv4 nf_tables support  --->
                    [M] nf_tables fib / ip route lookup support
                  [M] IPv4 packet rejection
                  [M] IP tables support (required for filtering/masq/NAT)  --->
                    [M] Packet filtering  --->
                      [M] REJECT target support
                    [M] iptables NAT support  --->
                      [M] MASQUERADE target support
                      [M] REDIRECT target support
                    [M] iptables NAT support
                    [M] Packet mangling
                    [M] raw table support
                    [M] Security table
                 IPv6: Netfilter Configuration  --->
                  [M] IPv6 socket lookup support
                  [M] IPv6 tproxy support
                  [*] IPv6 nf_tables support  --->
                    [M] nf_tables fib / ipv6 route lookup support
                  [M] IPv6 packet rejection
                  [M] IP6 tables support (required for filtering) --->
                    [M] Packet filtering  --->
                      [M] REJECT target support
                    [M] Packet mangling
                    [M] raw table support (required for TRACE)
                    [M] Security table (IP6_NF_SECURITY
                    [M] ip6tables NAT support  --->
                      [M] MASQUERADE target support
             [*] Advanced netfilter configuration  --->
                 Core Netfilter Configuration  --->
                  [*] Netfilter ingress support
                  [M] Netfilter NFQUEUE over NFNETLINK interface
                  [M] Netfilter OSF over NFNETLINK interface
                  [M] Netfilter connection tracking support
                  [M] Netfilter nf_tables support  --->
                    [*] Netfilter nf_tables mixed IPv4/IPv6 tables support
                    [M] Netfilter nf_tables conntrack module
                    [M] Netfilter nf_tables log module
                    [M] Netfilter nf_tables limit module
                    [M] Netfilter nf_tables masquerade support
                    [M] Netfilter nf_tables redirect support
                    [M] Netfilter nf_tables nat module
                    [M] Netfilter nf_tables tunnel module
                    [M] Netfilter nf_tables queue module
                    [M] Netfilter nf_tables quota module
                    [M] Netfilter nf_tables reject support
                    [M] Netfilter x_tables over nf_tables module
                    [M] Netfilter nf_tables hash module
                    [M] Netfilter nf_tables fib inet support
                    [M] Netfilter nf_tables xfrm/IPSec security association matching
                    [M] Netfilter nf_tables socket match support
                    [M] Netfilter nf_tables tproxy support
                    [M] Netfilter nf_tables SYNPROXY
                  [M] Netfilter Xtables support (required for ip_tables)  --->
                    [M] ctmark target and match support
                    [M] "SNAT and DNAT" targets support
                    [M] MASQUERADE target support
                    [M] "conntrack" connection tracking match support
                    [M] "multiport" Multiple port match support
                    [M] "state" match support
             [M] IP set support  --->

## [Installation]

### [USE flags]

### [USE flags for] [net-firewall/firewalld](https://packages.gentoo.org/packages/net-firewall/firewalld) [[]] [Firewall daemon with D-Bus interface providing a dynamic firewall]

  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`gui`](https://packages.gentoo.org/useflags/gui)           Enable support for a graphical user interface
  [`selinux`](https://packages.gentoo.org/useflags/selinux)   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`test`](https://packages.gentoo.org/useflags/test)         Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-14 12:38] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

## [Emerge]

Install firewalld:

`root `[`#`]`emerge --ask --verbose net-firewall/firewalld`

** Warning**\
Attention needs to be paid when emerging firewalld if the machine is using a manually compiled kernel like sys-kernel/gentoo-sources.

If there are warnings about kernel config options that should be enabled but aren\'t, then they need to be enabled in the kernel config, the kernel needs to be recompiled and installed. Afterwards the machine needs to be rebooted into the new kernel.

When all that is done, re-emerge the package like this:

`root `[`#`]`emerge --oneshot --ask --verbose net-firewall/firewalld`

** Important**\
If the package complains about any further missing kernel config options that weren\'t shown the first time, the process needs to be repeated.

** Tip**\
The best way to set these is to search for the config name in the kernel\'s search function either using menuconfig or xconfig

If the package is emerged without further complaints, then it\'s good to proceed.

### [Services]

#### [OpenRC]

To activate the firewall, the firewalld daemon needs to be started.

`root `[`#`]`rc-service firewalld start`

It can also be stopped or restarted with the same command, by replacing the [start] with [stop] or [restart]. Also [status] can be used to check the status of the firewalld daemon.

Ideally the firewall should be started when Gentoo starts. This can be done with:

`root `[`#`]`rc-update add firewalld default`

#### [Systemd]

To activate the firewall on systemd, we need to start the firewalld daemon service:

`root `[`#`]`systemctl start firewalld`

It can also be stopped with the same command, by replace the [start] with [stop]. To check the status of the daemon/service [status] can be used instead.

Ideally the firewall should be started when Gentoo starts. This can be done with:

`root `[`#`]`systemctl enable firewalld`

#### [Check status]

Irrespective of OpenRC or Systemd, To check if the firewall itself is running, the following command can be used:

`root `[`#`]`firewall-cmd --state`

## [Configuration]

Configuration may be modified with [firewall-cmd]; changes will remain in effect until the service is restarted. To persist changes, either:

-   Run

    :::: cmd-box


    `root `[`#`]`firewall-cmd --runtime-to-permanent`


    ::::

    after [firewalld] is in the desired state

or:

-   Include the [\--permanent] flag with a given command. Running

    :::: cmd-box


    `root `[`#`]`firewall-cmd --reload`


    ::::

    will be required for the changes with [\--permanent] to take effect.

## [See Also]

-   [Iptables](https://wiki.gentoo.org/wiki/Iptables "Iptables") --- a program used to configure and manage the kernel\'s netfilter modules.
-   [nftables](https://wiki.gentoo.org/wiki/Nftables "Nftables") --- the successor to [[iptables](https://wiki.gentoo.org/wiki/Iptables "Iptables")].
-   [ufw](https://wiki.gentoo.org/wiki/Ufw "Ufw") --- the **u**ncomplicated **f**ire**w**all

## [References]

-   [https://www.firewalld.org/](https://www.firewalld.org/)
-   [https://firewalld.org/documentation/](https://firewalld.org/documentation/)