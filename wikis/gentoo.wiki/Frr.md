**Resources**

[[]][Home](https://frrouting.org/)

[[]][Official documentation](http://docs.frrouting.org/en/latest/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/FRRouting "wikipedia:FRRouting")

[[]][GitHub](https://github.com/FRRouting/frr)

[[]][Bugs (upstream)](https://github.com/FRRouting/frr/issues/)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/frr)

[[]]This article has some todo items:\

-   add systemd configuration steps

FRR is a set of unified tools to configure and manage dynamic routing protocols. It was created as a fork from [the Quagga Project](https://www.quagga.net/).

The FRRouting software consists of 2 basic parts:

-   The **zebra** daemon
-   The routing process deamons: **ripd**,**ospfd** etc.

The zebra daemon is a *abstraction layer* between the kernel and the running routing processes. zebra acts as a relay. Each routing protocol such as as BFD, BGP, Babel, OpenFabric, LDP, EIGRP, ISIS, NHRP, OSPFv2, OSPFv3, Segment Routing, PIM, PBR, RIP, RIPng, STATIC and VRRP runs its own separate running daemon.

FRRouting can *install*, *add*, *change* and *remove* kernel IP routing information. All routing daemons communicate directly to *zebra* daemon. The *zebra* daemon then, alters the linux IP networking information on the host. [iproute2](https://wiki.gentoo.org/wiki/Iproute2 "Iproute2") and *nettools* alter directly the linux IP networking.

  ------------------- ---------------------------- ------- -------- -------- -------- ------ ------ -------- ------- --------- ------- -------- -------------------------------------------------------------- -------------------------------------------------- --------- -------------- -- -- -- -- -- -- -- -- -- -- -- -- -- --
  **Control Plane**   bgpd                         ospfd   ospf6d   ripngd   isisd    pimd   ldpd   babeld   bfdd    fabricd   pathd   (\...)   [iproute2](https://wiki.gentoo.org/wiki/Iproute2 "Iproute2")   [BIRD](https://wiki.gentoo.org/wiki/BIRD "BIRD")   ethtool   *other tool*
                      zebra
  **Data Plane**      Linux kernel IP networking
  **Hardware**        eth0                                                   enp8s0                          wlan1                              *other interface*
  ------------------- ---------------------------- ------- -------- -------- -------- ------ ------ -------- ------- --------- ------- -------- -------------------------------------------------------------- -------------------------------------------------- --------- -------------- -- -- -- -- -- -- -- -- -- -- -- -- -- --

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [SLOTTING]](#SLOTTING)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [OpenRC]](#OpenRC)
    -   [[2.2] [systemd]](#systemd)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Login]](#Login)
    -   [[3.2] [Show routing table]](#Show_routing_table)
    -   [[3.3] [Show configuration]](#Show_configuration)
    -   [[3.4] [Configure IP addressing]](#Configure_IP_addressing)
    -   [[3.5] [Exit configure mode]](#Exit_configure_mode)
    -   [[3.6] [Verify configuration]](#Verify_configuration)
    -   [[3.7] [Save configuration]](#Save_configuration)
    -   [[3.8] [Exit router]](#Exit_router)
    -   [[3.9] [Test connectivity]](#Test_connectivity)
    -   [[3.10] [Remove configuration]](#Remove_configuration)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Using help]](#Using_help)
    -   [[4.2] [Routing protocol debugging]](#Routing_protocol_debugging)
        -   [[4.2.1] [Method 1]](#Method_1)
        -   [[4.2.2] [Method 2]](#Method_2)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

### [SLOTTING]

It\'s important to know that frr does not typically maintain full backwards compatibility between versions. For reference:

-   [https://frrouting.org/release/9.1/](https://frrouting.org/release/9.1/) (which was surprisingly compatible)
-   [https://frrouting.org/release/10.0/](https://frrouting.org/release/10.0/) (single vs multi file configuration and bgp defaults)
-   [https://frrouting.org/release/10.1/](https://frrouting.org/release/10.1/) (bgp defaults, rpki)

As can be seen blind upgrades are dangerous for frr with potentially catastrophic consequences. For this reason we\'ve decided to (starting with frr 9.0.4, 9.1.2, 10.0.2 and 10.1.1) SLOT frr into sub-slots based on major.minor version. This allows you to emerge net-misc/frr:0/9.1 for example. This will add net-misc/frr to world, and may still result in upgrades happening when upgrading world unless you take precautionary measures. To prevent this you have three options (none of which the author is lead to understood is generally supported).

Option 1: edit /var/lib/portage/world manually, eg:

    $ grep frr world
    net-misc/frr:0/9.1

Option 2: mask net-misc/frr and unmask net-misc/frr:0/9.1, eg:

    /etc/portage # grep frr -r package.*
    package.mask/99frr:net-misc/frr
    package.unmask/99frr:net-misc/frr:0/9.1

This has the downside that if (when) we mask a subslot you may not notice. Eg, if we now proceed to add net-misc/frr:0/9.1 to packages.mask globally, then your unmask will override that.

Option 3: mask newer versions only, eg:

    /etc/portage # grep frr -r package.*
    package.mask/99frr:>=net-misc/frr-10.0*

Please note that wherever possible we will endeavour to hard-mask a slot at least 30 days prior to removal, most likely by way of KEYWORDS=-\* to accommodate all options above, in addition to adding an entry to packages.mask to clarify why.

### [USE flags]

### [USE flags for] [net-misc/frr](https://packages.gentoo.org/packages/net-misc/frr) [[]] [The FRRouting Protocol Suite]

  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`doc`](https://packages.gentoo.org/useflags/doc)           Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`fpm`](https://packages.gentoo.org/useflags/fpm)           Enable Forwarding Plane Manager support
  [`grpc`](https://packages.gentoo.org/useflags/grpc)         Enable gRPC plugin
  [`nhrp`](https://packages.gentoo.org/useflags/nhrp)         Build Next Hop Resolution Protocol daemon
  [`ospfapi`](https://packages.gentoo.org/useflags/ospfapi)   Build OSPFAPI support
  [`pam`](https://packages.gentoo.org/useflags/pam)           Add support for PAM (via sys-libs/pam) to the Virtual Terminal Interface Shell (vtysh)
  [`rpki`](https://packages.gentoo.org/useflags/rpki)         Enable RPKI
  [`snmp`](https://packages.gentoo.org/useflags/snmp)         Add support for the Simple Network Management Protocol if available
  [`test`](https://packages.gentoo.org/useflags/test)         Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-01 20:24] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask net-misc/frr`

## [Configuration]

Review frr\'s configuration [/etc/frr/daemons] file to enable additional routing protocols. In the default setting all routing protocols are disabled.

-   [/etc/frr/daemons] - Global (system wide) FRR configuration file.

[FILE] **`/etc/frr/daemons`**

    ...
    bgpd=no
    ospfd=no
    ospf6d=no
    ripd=no
    ripngd=no
    isisd=no
    pimd=no
    ldpd=no
    nhrpd=no
    eigrpd=no
    babeld=no
    sharpd=no
    pbrd=no
    bfdd=no
    fabricd=no
    vrrpd=no
    pathd=no
    ...

Add larry to frrvty group to be able to use vtysh:

`root `[`#`]`gpasswd -a larry frrvty`

Add larry to the frr group:

`root `[`#`]`gpasswd -a larry frr`

### [OpenRC]

Add frr to the default runlevel:

`root `[`#`]`rc-update add frr default`

Start frr daemon:

`root `[`#`]`/etc/init.d/frr start`

### [systemd]

** Note**\
If the main routing table is large, you may want to remove the [myhostname] module from the [host] entry in [/etc/nsswitch.conf] to avoid slow DNS lookups [\[1\]](https://github.com/systemd/systemd/issues/11384)

## [Usage]

Following section describes a basic configuration example for FRR. Configuring a additional IP address `192.0.2.100/32` and the IPv6 address `2001:db8::100/128` on a loopback interface `lo`, then finally to test in using [iproute2](https://wiki.gentoo.org/wiki/Iproute2 "Iproute2") tools. The goal of this usage configuration example is to show, FRR is yet another management tool for the linux kernel IP networking.

Commands overview:

+:------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Action                                                      | Command                                                                                                                                                                      |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Use vtysh to configure frr                                  | :::: cmd-box                                                                                                                                                                 |
|                                                             |                                                                                                                                                                         |
|                                                             |                                                                                                                                                                              |
|                                                             | `user `[`$`]`vtysh`  |
|                                                             |                                                                                                                                                                              |
|                                                             |                                                                                                                                                                        |
|                                                             | ::::                                                                                                                                                                         |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Show help using the `?` key.                                | :::: cmd-box                                                                                                                                                                 |
|                                                             |                                                                                                                                                                         |
|                                                             |                                                                                                                                                                              |
|                                                             | `Router#``?`                                                                                                |
|                                                             |                                                                                                                                                                              |
|                                                             |                                                                                                                                                                        |
|                                                             | ::::                                                                                                                                                                         |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Show basic IP networking information                        | :::: cmd-box                                                                                                                                                                 |
|                                                             |                                                                                                                                                                         |
|                                                             |                                                                                                                                                                              |
|                                                             | `Router#``show ip route`                                                                                    |
|                                                             |                                                                                                                                                                              |
|                                                             |                                                                                                                                                                        |
|                                                             | ::::                                                                                                                                                                         |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Show running configuration                                  | :::: cmd-box                                                                                                                                                                 |
|                                                             |                                                                                                                                                                         |
|                                                             |                                                                                                                                                                              |
|                                                             | `Router#``show run`                                                                                         |
|                                                             |                                                                                                                                                                              |
|                                                             |                                                                                                                                                                        |
|                                                             | ::::                                                                                                                                                                         |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Get into global configuration mode                          | :::: cmd-box                                                                                                                                                                 |
|                                                             |                                                                                                                                                                         |
|                                                             |                                                                                                                                                                              |
|                                                             | `Router#``conf`                                                                                             |
|                                                             |                                                                                                                                                                              |
|                                                             |                                                                                                                                                                        |
|                                                             | ::::                                                                                                                                                                         |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Change int interface configuration mode, interface loopback | :::: cmd-box                                                                                                                                                                 |
|                                                             |                                                                                                                                                                         |
|                                                             |                                                                                                                                                                              |
|                                                             | `Router(config)#``int lo`                                                                                   |
|                                                             |                                                                                                                                                                              |
|                                                             |                                                                                                                                                                        |
|                                                             | ::::                                                                                                                                                                         |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Configure IP address on a loopback interface                | :::: cmd-box                                                                                                                                                                 |
|                                                             |                                                                                                                                                                         |
|                                                             |                                                                                                                                                                              |
|                                                             | `Router(config-if)#``ip address 192.0.2.100/32`                                                             |
|                                                             |                                                                                                                                                                              |
|                                                             |                                                                                                                                                                        |
|                                                             | ::::                                                                                                                                                                         |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Configure IPv6 address on a loopback interface              | :::: cmd-box                                                                                                                                                                 |
|                                                             |                                                                                                                                                                         |
|                                                             |                                                                                                                                                                              |
|                                                             | `Router(config-if)#``ipv6 address 2001:db8::100/128`                                                        |
|                                                             |                                                                                                                                                                              |
|                                                             |                                                                                                                                                                        |
|                                                             | ::::                                                                                                                                                                         |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Exit global configuration mode                              | :::: cmd-box                                                                                                                                                                 |
|                                                             |                                                                                                                                                                         |
|                                                             |                                                                                                                                                                              |
|                                                             | `Router(config-if)#``end`                                                                                   |
|                                                             |                                                                                                                                                                              |
|                                                             |                                                                                                                                                                        |
|                                                             | ::::                                                                                                                                                                         |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Show current configuration                                  | :::: cmd-box                                                                                                                                                                 |
|                                                             |                                                                                                                                                                         |
|                                                             |                                                                                                                                                                              |
|                                                             | `Router#``show int lo`                                                                                      |
|                                                             |                                                                                                                                                                              |
|                                                             |                                                                                                                                                                        |
|                                                             | ::::                                                                                                                                                                         |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Save frr configuration                                      | :::: cmd-box                                                                                                                                                                 |
|                                                             |                                                                                                                                                                         |
|                                                             |                                                                                                                                                                              |
|                                                             | `Router#``wr`                                                                                               |
|                                                             |                                                                                                                                                                              |
|                                                             |                                                                                                                                                                        |
|                                                             | ::::                                                                                                                                                                         |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Display configured IP address using iproute2                | :::: cmd-box                                                                                                                                                                 |
|                                                             |                                                                                                                                                                         |
|                                                             |                                                                                                                                                                              |
|                                                             | `user `[`$`]`ip add` |
|                                                             |                                                                                                                                                                              |
|                                                             |                                                                                                                                                                        |
|                                                             | ::::                                                                                                                                                                         |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Initial IP network settings used during the example configuration:

  ----------- ----------- ------------ --------------
  Interface   Settings    IP           IPv6
  **lo**      *address*   127.0.0.1    ::1
              *netmask*   /32          /128
  **wlan0**   *address*   192.0.2.10   2001:db8::10
              *netmask*   /24          /64
              *gateway*   192.0.2.1    2001:db8::1
  ----------- ----------- ------------ --------------

  : Initial networking setup

Display configured IP settings using [iproute2](https://wiki.gentoo.org/wiki/Iproute2 "Iproute2"):

`user `[`$`]`ip add`

    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 brd 127.255.255.255 scope host lo
           valid_lft forever preferred_lft forever
    2: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP qlen 1000
        link/ether de:ad:be:ef:de:ad brd ff:ff:ff:ff:ff:ff
        inet 192.0.2.10/24 brd 192.0.2.255 scope global wlan0

Display the IPv6 interface configuration using iproute2:

`user `[`$`]`ip -6 add`

    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 state UNKNOWN qlen 1000
        inet6 ::1/128 scope host
           valid_lft forever preferred_lft forever
    2: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 state UP qlen 1000
        inet6 2001:db8::10/64 scope global
           valid_lft forever preferred_lft forever
        inet6 fe80::eac:d1ff:fe94:0/64 scope link
           valid_lft forever preferred_lft forever

Show the Linux IPv4 routing table:

`user `[`$`]`ip route`

    default via 192.0.2.1 dev wlan0  metric 2005
    192.0.2.0/24 dev wlan0 proto kernel scope link src 192.0.2.10

Show the Linux IPv6 routing table:

`user `[`$`]`ip -6 route`

    default via 2001:db8::1 dev wlan0 metric 1024 pref medium
    2001:db8::/64 dev wlan0 proto kernel metric 256 pref medium
    fe80::/64 dev wlan0 proto kernel metric 256 pref medium

### [Login]

Use the [vtysh] command to login to the FRR command line interface:

`user `[`$`]`vtysh`

    Hello, this is FRRouting (version 8.1-gentoo).
    Copyright 1996-2005 Kunihiro Ishiguro, et al.

    Router#

### [Show routing table]

Compare output shown below to the Linux [ip route], shows exactly same output. Notice the default route has a K prefix which means it is a kernel route:

+--------------------------------------------------------------------------------------------+
| :::: cmd-box                                                                               |
|                                                                                       |
|                                                                                            |
| `Router#``show ip route ` |
|                                                                                            |
|                                                                                      |
|                                                                                            |
|     Codes: K - kernel route, C - connected, S - static, R - RIP,                           |
|            O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,                              |
|            T - Table, v - VNC, V - VNC-Direct, A - Babel, F - PBR,                         |
|            f - OpenFabric,                                                                 |
|            > - selected route, * - FIB route, q - queued, r - rejected, b - backup         |
|            t - trapped, o - offload failure                                                |
|                                                                                            |
|     K>* 0.0.0.0/0 [0/0] via 192.0.2.1, eth0, 00:00:09                                      |
|     C>* 192.0.2.0/24 is directly connected, eth0, 00:13:52                                 |
| ::::                                                                                       |
+--------------------------------------------------------------------------------------------+

Now the same, but for the IPv6 protocol:

+----------------------------------------------------------------------------------------------+
| :::: cmd-box                                                                                 |
|                                                                                         |
|                                                                                              |
| `Router#``show ipv6 route ` |
|                                                                                              |
|                                                                                        |
|                                                                                              |
|     Codes: K - kernel route, C - connected, S - static, R - RIPng,                           |
|            O - OSPFv3, I - IS-IS, B - BGP, N - NHRP, T - Table,                              |
|            v - VNC, V - VNC-Direct, A - Babel, F - PBR,                                      |
|            f - OpenFabric,                                                                   |
|            > - selected route, * - FIB route, q - queued, r - rejected, b - backup           |
|            t - trapped, o - offload failure                                                  |
|                                                                                              |
|     K>* ::/0 [0/1024] via 2001:db8::1, wlan0, 00:04:44                                       |
|     C>* 2001:db8::/64 is directly connected, wlan0, 00:12:00                                 |
|     C>* fe80::/64 is directly connected, wlan0, 00:12:03                                     |
| ::::                                                                                         |
+----------------------------------------------------------------------------------------------+

### [Show configuration]

To display current configuration use the `show running-config` command:

`Router#``show run `

    Building configuration...

    Current configuration:
    !
    frr version 8.1-gentoo
    frr defaults traditional
    hostname Router
    service integrated-vtysh-config
    !
    end

### [Configure IP addressing]

Get into edit mode:

`Router#``conf `

    Router(config)#

Choose the `lo` loopback interface:

`Router(config)#``int lo `

    Router(config-if)#

Configure the IP 192.0.2.100/32 on loopback interface, notice the IP prefix length `/32`:

`Router(config-if)#``ip address 192.0.2.100/32 `

Configure the IPv6 address 2001:db8::100/128 on the loopback interface, notice the `/128` prefix length:

`Router(config-if)#``ipv6 address 2001:db8::100/128 `

### [Exit configure mode]

End the edit mode mode session:

`Router(config-if)#``end `

    Router#

### [Verify configuration]

Show running configuration:

`Router#``show run `

    Current configuration:
    !
    frr version 8.1
    frr defaults traditional
    hostname Router
    service integrated-vtysh-config
    !
    interface lo
     ip address 192.0.2.100/32
     ipv6 address 2001:db8::100/128
    exit
    !
    end

Show the loopback interface configuration, and notice the configured `inet` and `inet6` addresses in the output:

`Router#``sh int lo `

    Interface lo is up, line protocol is up
      Link ups:       0    last: (never)
      Link downs:     0    last: (never)
      vrf: default
      index 1 metric 0 mtu 65536 speed 0
      flags: <UP,LOOPBACK,RUNNING>
      Type: Loopback
      inet 192.0.2.100/32
      inet6 2001:db8::100/128
      Interface Type Other
      Interface Slave Type None
      protodown: off

Show the IPv4 routing table, notify both prefixes `192.0.2.10/24` and `192.0.2.100/32` are in the routing table:

`Router#``show ip route `

    Codes: K - kernel route, C - connected, S - static, R - RIP,
           O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
           T - Table, v - VNC, V - VNC-Direct, A - Babel, F - PBR,
           f - OpenFabric,
           > - selected route, * - FIB route, q - queued, r - rejected, b - backup
           t - trapped, o - offload failure

    C>* 192.0.2.10/24 is directly connected, wlan0, 00:05:14
    C>* 192.0.2.100/24 is directly connected, lo, 00:05:14

Show the IPv6 routing table, notify both prefixes `2001:db8::/64` and `2001:db8::100/128` are in the routing table:

`Router#``show ipv6 route `

    frr# show ipv6 route
    Codes: K - kernel route, C - connected, S - static, R - RIPng,
           O - OSPFv3, I - IS-IS, B - BGP, N - NHRP, T - Table,
           v - VNC, V - VNC-Direct, A - Babel, F - PBR,
           f - OpenFabric,
           > - selected route, * - FIB route, q - queued, r - rejected, b - backup
           t - trapped, o - offload failure

    C>* 2001:db8::/64 is directly connected, wlan0, 00:24:31
    C>* 2001:db8::100/128 is directly connected, lo, 00:31:28
    C>* fe80::/64 is directly connected, eth0, 00:56:16

### [Save configuration]

Save running configuration:

`Router#``write `

    Building Configuration...
    Integrated configuration saved to /etc/frr/frr.conf
    [OK]

### [Exit router]

Exit FRR using the [exit] command:

`Router#``exit `

### [Test connectivity]

Verify IP configuration using [iproute2](https://wiki.gentoo.org/wiki/Iproute2 "Iproute2"). Notice the additional IP address setup on loopback interface:

`user `[`$`]`ip add`

    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
           valid_lft forever preferred_lft forever
        inet 192.168.0.100/32 brd 192.168.0.100 scope global lo
           valid_lft forever preferred_lft forever
        inet6 2001:db8::100/128 scope global
           valid_lft forever preferred_lft forever
        inet6 ::1/128 scope host
           valid_lft forever preferred_lft forever
    1: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP qlen 1000
        link/ether 0c:ac:d1:94:00:00 brd ff:ff:ff:ff:ff:ff
        inet 192.0.2.10/24 brd 192.0.2.255 scope global eth0
           valid_lft forever preferred_lft forever
        inet6 2001:db8::10/64 scope global
           valid_lft forever preferred_lft forever
        inet6 fe80::eac:d1ff:fe94:0/64 scope link
           valid_lft forever preferred_lft forever

Verify IP connectivity in the network:

`user `[`$`]`ping 192.0.2.100`

    PING 192.0.2.100 (192.0.2.100): 56 data bytes
    64 bytes from 192.0.2.100: seq=0 ttl=42 time=0.051 ms
    ^C
    --- 192.0.2.100 ping statistics ---
    1 packets transmitted, 1 packets received, 0% packet loss
    round-trip min/avg/max = 0.051/0.051/0.051 ms

Verify IPv6 connectivity in the network:

`user `[`$`]`ping 2001:db8::100`

    PING 2001:db8::100 (2001:db8::100): 56 data bytes
    64 bytes from 2001:db8::100: seq=0 ttl=64 time=0.062 ms
    ^C
    --- 2001:db8::100 ping statistics ---
    1 packets transmitted, 1 packets received, 0% packet loss
    round-trip min/avg/max = 0.058/0.058/0.058 ms

### [Remove configuration]

Remove the example configuration using the using vtysh:

`user `[`$`]`vtysh`

Apply following command sequence to remove the configuration:

    conf
    interface lo
     no ip address 192.0.2.100/32
     no ipv6 address 2001:db8::100/128
    end
    wr

## [Troubleshooting]

Verify the zebra daemon is up and running:

`root `[`#`]`ss -tulpn | grep zebra`

    tcp   LISTEN 0      3          127.0.0.1:2601      0.0.0.0:*    users:(("zebra",pid=1799,fd=22))

Verify configured routing protocol daemons are up and running:

`root `[`#`]`ss -tulpn | egrep 'Net|:26'`

    Netid State  Recv-Q Send-Q Local Address:Port Peer Address:PortProcess
    tcp   LISTEN 0      3          127.0.0.1:2608      0.0.0.0:*    users:(("isisd",pid=1823,fd=11))
    tcp   LISTEN 0      3          127.0.0.1:2609      0.0.0.0:*    users:(("babeld",pid=1826,fd=10))
    tcp   LISTEN 0      3          127.0.0.1:2611      0.0.0.0:*    users:(("pimd",pid=1829,fd=12))
    tcp   LISTEN 0      3          127.0.0.1:2612      0.0.0.0:*    users:(("ldpd",pid=1838,fd=17))
    tcp   LISTEN 0      3          127.0.0.1:2616      0.0.0.0:*    users:(("staticd",pid=1842,fd=11))
    tcp   LISTEN 0      3          127.0.0.1:2617      0.0.0.0:*    users:(("bfdd",pid=1845,fd=18))
    tcp   LISTEN 0      3          127.0.0.1:2601      0.0.0.0:*    users:(("zebra",pid=1799,fd=22))
    tcp   LISTEN 0      3          127.0.0.1:2602      0.0.0.0:*    users:(("ripd",pid=1811,fd=11))
    tcp   LISTEN 0      3          127.0.0.1:2604      0.0.0.0:*    users:(("ospfd",pid=1817,fd=11))
    tcp   LISTEN 0      3          127.0.0.1:2605      0.0.0.0:*    users:(("bgpd",pid=1804,fd=17))
    tcp   LISTEN 0      3              [::1]:2606         [::]:*    users:(("ospf6d",pid=1820,fd=11))
    tcp   LISTEN 0      3              [::1]:2603         [::]:*    users:(("ripngd",pid=1814,fd=11))

### [Using help]

Show basic mode commands, use the [?] key for help:

`Router#``? `

      add               Add registration
      clear             Reset functions
      configure         Configuration from vty interface
      copy              Copy from one file to another
      debug             Debugging functions
      disable           Turn off privileged mode command
      enable            Turn on privileged mode command
      end               End current mode and change to enable mode
      exit              Exit current mode and down to previous mode
      find              Find CLI command matching a regular expression
      graceful-restart  Graceful Restart commands
      list              Print command list
      mtrace            Multicast trace route to multicast source
      no                Negate a command or set its defaults
      output            Direct vtysh output to file
      ping              Send echo messages
      quit              Exit current mode and down to previous mode
      rpki              Control rpki specific settings
      show              Show running system information
      terminal          Set terminal line parameters
      traceroute        Trace route to destination
      watchfrr          Watchfrr Specific sub-command
      write             Write running configuration to memory, network, or terminal

After choosing initial entry command `show`, continue using [?] key to display further possible commands:

`Router#``show ? `

      babel             Babel information
      bfd               Bidirection Forwarding Detection
      bgp               BGP information
      bmp               BGP Monitoring Protocol
      daemons           Show list of running daemons
      debugging         Debugging functions
      error             Information on errors
      evpn              EVPN
      fpm               Forwarding Plane Manager configuration
      history           The list of commands stored in history
      interface         Interface status and configuration
      ip                IP information
      ipv6              IPv6 information
      isis              IS-IS routing protocol
      l2vpn             Show information about Layer2 VPN
      logging           Show current logging configuration
      mac               mac access lists
      memory            Memory statistics
      modules           Loaded modules
      mpls              MPLS information
      nexthop-group     Show Nexthop Groups
      openfabric        OpenFabric routing protocol
      pathd             pathd daemon
      pbr               Policy Based Routing
      route-map         route-map
      route-map-unused  unused route-map information
      router-id         Show the configured router-id
      rpki              Control rpki specific settings
      running-config    Current operating configuration
      segment-routing   Segment Routing
      sr-te             SR-TE info
      startup-config    Contents of startup configuration
      thread            Thread information
      version           Displays zebra version
      vnc               VNC information
      vrf               VRF
      vrrp              Virtual Router Redundancy Protocol
      watchfrr          watchfrr information
      work-queues       Work Queue information
      yang              YANG information
      zebra             Zebra information

Continue using the [?] help key on each command level, to view possible configuration settings.

`Router#``show ip ? `

      access-list          List IP access lists
      as-path-access-list  List AS path access lists
      bgp                  BGP information
      eigrp                IP-EIGRP show commands
      fib                  IP forwarding table
      forwarding           IP forwarding status
      igmp                 IGMP information
      import-check         IP import check tracking table
      mroute               IP multicast routing table
      msdp                 MSDP information
      multicast            Specify the VRF
      nht                  IP nexthop tracking table
      ospf                 OSPF information
      pim                  PIM information
      prefix-list          Build a prefix list
      protocol             IP protocol filtering status
      rib                  IP unicast routing table
      rip                  Show RIP routes
      route                IP routing table
      router-id            Show the configured router-id
      rpf                  Display RPF information for multicast source
      ssmpingd             ssmpingd operation

Show the routing table:

`Router#``show ip route `

Internal help works like a tree, where using the [?] key displays further levels of commands.

### [Routing protocol debugging]

Depending on the used FRRouting version, there are 2 different ways to display the routing protocol debugging output. Method 2 is the more universal working method that will work using all FRRouting versions.

#### [Method 1]

** Note**\
This works using FRR version 9.x. and higher.

Since FRRouting version 9 it is possible to get routing protocol debug messages displayed using [vtysh] only. Without leaving the vtysh default prompt.

Enable babel route debugging using the [debug babel route] command:

`Router#``debug babel route `

To view the protocol debugging in the prompt use the [terminal monitor] command

`Router#``terminal monitor `

    2023-10-15 09:08:09.231 [DEBG] babeld: [N3PWX-KJW20] Modify route: delete old; add new.
    2023-10-15 09:08:09.231 [DEBG] babeld: [K58FD-K9K7G] removing route (ipv6) to zebra
    2023-10-15 09:08:09.231 [DEBG] babeld: [K58FD-K9K7G] adding route (ipv6) to zebra

Disable debugging output after finishing troubleshooting:

`Router#``no terminal monitor `

`Router#``no debug babel route `

#### [Method 2]

** Tip**\
This debugging aproach works using all FRR versions

To view protocol debug output, use the [log syslog debugging] configuration to write the debugging output systems to [/var/log/messages] file:

    conf
    log syslog debugging
    exit

Get and overview of the debugging options:

`Router#``debug ? `

      babel             Babel information
      bfd               Bidirection Forwarding Detection
      bgp               BGP information
      eigrp             EIGRP information
      igmp              IGMP protocol activity
      isis              IS-IS routing protocol
      memstats-at-exit  Print memory statistics at exit
      mpls              MPLS information
      mroute            PIM interaction with kernel MFC cache
      msdp              MSDP protocol activity
      mtrace            Mtrace protocol activity
      nhrp              NHRP information
      northbound        Northbound debugging
      openfabric        OpenFabric routing protocol
      ospf              OSPF information
      ospf6             Open Shortest Path First (OSPF) for IPv6
      pathd             path debugging
      pbr               Policy Based Routing
      pim               PIM protocol activity
      prefix-list       Prefix-list test access
      resolver          Debug DNS resolver actions
      rfapi-dev         RF API debugging/testing command
      rip               RIP information
      ripng             RIPng configuration
      route-map         Debug option set for route-maps
      rpki              Enable debugging for rpki
      spf-delay-ietf    SPF Back-off Debugging
      ssmpingd          ssmpingd activity
      static            Static route daemon
      unique-id         Options per individual log message, by unique ID
      vrf               VRF Debugging
      vrrp              Virtual Router Redundancy Protocol
      zebra             Zebra configuration

In example below a simple [debug rip events] routine is shown:

`Router#``debug rip events `

View the routing protocol debug events in the system syslog [/var/log/messages] file:

`root `[`#`]`tail -f /var/log/messages `

    Apr  2 15:19:38 Router daemon.debug ripd[1811]: [RG149-CQVW5] update timer fire!
    Apr  2 15:19:38 Router daemon.debug ripd[1811]: [V19ZJ-CH6H5] SEND UPDATE to eth0 ifindex 2
    Apr  2 15:19:38 Router daemon.debug ripd[1811]: [RDKCB-7NMQT] multicast announce on eth0
    Apr  2 15:19:38 Router daemon.debug ripd[1811]: [JEJ1H-ZE96E] update routes on interface eth0 ifindex 2
    Apr  2 15:19:38 Router daemon.debug ripd[1811]: [VEJY5-67P5X] SEND to  224.0.0.9520
    Apr  2 15:20:14 Router daemon.debug ripd[1811]: [RG149-CQVW5] update timer fire!
    Apr  2 15:20:14 Router daemon.debug ripd[1811]: [V19ZJ-CH6H5] SEND UPDATE to eth0 ifindex 2
    Apr  2 15:20:14 Router daemon.debug ripd[1811]: [RDKCB-7NMQT] multicast announce on eth0
    Apr  2 15:20:14 Router daemon.debug ripd[1811]: [JEJ1H-ZE96E] update routes on interface eth0 ifindex 2
    Apr  2 15:20:14 Router daemon.debug ripd[1811]: [VEJY5-67P5X] SEND to  224.0.0.9520

Disable debugging output after finishing troubleshooting:

`Router#``no debug rip events `

## [See also]

-   [Iproute2](https://wiki.gentoo.org/wiki/Iproute2 "Iproute2") --- a tool developed to unify network interface configuration, routing, and tunneling for Linux systems.
-   [Static routing](https://wiki.gentoo.org/wiki/Static_routing "Static routing") --- covers routing of the IP protocol in the Linux kernel.
-   [BIRD](https://wiki.gentoo.org/wiki/BIRD "BIRD") --- routing daemon implementing OSPF, RIPv2 & BGP, Babel for IP

## [External resources]

-   [FRR\'s linux kernel settings recommendations for advanced usage](https://docs.frrouting.org/en/latest/installation.html#linux-notes)
-   [FRR vtysh - terminal monitor](https://docs.frrouting.org/en/latest/vtysh.html#clicmd-terminal-monitor-DAEMON)
-   [Official Quagga website](https://www.nongnu.org/quagga/)
-   [Quagga\_(software)](https://en.wikipedia.org/wiki/Quagga_(software))
-   [GNU/Zebra](https://en.wikipedia.org/wiki/GNU_Zebra)