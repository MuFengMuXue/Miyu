This article discusses the concept of setting up a network bridge, in order to connect two portions of a network together.

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [Kernel]](#Kernel)
-   [[3] [Installation]](#Installation)
-   [[4] [Host configuration]](#Host_configuration)
    -   [[4.1] [OpenRC]](#OpenRC)
        -   [[4.1.1] [Single NIC bridge]](#Single_NIC_bridge)
    -   [[4.2] [systemd]](#systemd)
        -   [[4.2.1] [DHCP]](#DHCP)
        -   [[4.2.2] [Static]](#Static)
-   [[5] [Using NetworkManager]](#Using_NetworkManager)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [Introduction]

A network bridge can be used to connect two independent network segments at layer 2 level (much like a network switch). Common applications include transparent proxying, transparent filtering (using [iptables](https://wiki.gentoo.org/wiki/Iptables "Iptables")) and saving money on hardware as some mainboards come with two PHY interfaces. In this article, `enp1s0` and `enp2s0` will be the network interfaces used but of course they can be replaced by whatever interface names are present on a system (such as `eth0` and `eth1`).

In order to create a bridge on Linux a special bridging device is created (brX) that contains at least two network devices as ports (e.g. ethX or pppX). As the bridge works on layer 2, no IP addresses are needed on the port devices --- on a typical setup, the bridging device itself will receive the IP (e.g. via DHCP).

## [Kernel]

[KERNEL] **Enabling Ethernet Bridging**

    [*] Networking support  --->
       Networking options  --->
          <M> 802.1d Ethernet Bridging

## [Installation]

** Note**\
With older versions of netifrc (No longer in ::gentoo), or needs for some other reasons, install the [[[net-misc/bridge-utils]](https://packages.gentoo.org/packages/net-misc/bridge-utils)[]] package to have access to the utilities needed to manage the bridge device.

It is recommended to configure bridges with a console connection. SSH access is likely to be lost if working on one of the ports being adding to the bridge.

Make certain the physical Ethernet interfaces in the bridge are not in [/etc/init.d/] as symbolic links as part of the original install:

`root `[`#`]`rc-update delete net.enp1s0 boot `

`root `[`#`]`rc-update delete net.enp2s0 boot `

`root `[`#`]`rm /etc/init.d/net.enp2s0 `

`root `[`#`]`rm /etc/init.d/net.enp1s0 `

It is always best to learn how to do things first by hand, then automate it. As this is a layer 2 connection being created, IP addresses assigned to the physical ports are not needed. The bridged physical interfaces (*enp1s0* and *enp2s0* in the below example) are put into promiscuous mode, so they will not be able to receive an IP address (e.g. via dhcp). The bridge will also not function properly if static IP addresses are forced on the interfaces.

Now create a bridge with no interfaces assigned (yet):

`root `[`#`]`ip link add br0 type bridge `

Add the two interfaces to the bridge:

`root `[`#`]`ip link set dev enp1s0 master br0 `

`root `[`#`]`ip link set dev enp2s0 master br0 `

View the results:

`root `[`#`]`ip link show`

    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    2: enp1s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master br0 state UP mode DEFAULT group default qlen 1000
        link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff
    3: enp2s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master br0 state UP mode DEFAULT group default qlen 1000
        link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff
    4: br0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT group default qlen 1000
        link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff

Note that `stp` does not get turned on unless specified.

## [Host configuration]

### [OpenRC]

[netifrc](https://wiki.gentoo.org/wiki/Netifrc "Netifrc") is OpenRC\'s native network management suite.

Bridges devices must be added to the [/etc/conf.d/net] file.

As an example, bridge configuration with static addresses:

[FILE] **`/etc/conf.d/net`Add bridge device example**

    # Set up the initial layer 2 bridge interface
    bridge_br0="enp1s0 enp2s0"

    # Bridge static config
    config_br0="192.168.26.199 netmask 255.255.255.0"
    routes_br0="default via 192.168.26.254"

    bridge_forward_delay_br0=0
    bridge_hello_time_br0=1000

For dynamic addressing, use the DHCP option:

[FILE] **`/etc/conf.d/net`DHCP bridge config**

    # Set up the initial layer 2 bridge interface
    bridge_br0="enp1s0 enp2s0"

    # Bridge dynamic config
    config_br0="dhcp"

    bridge_forward_delay_br0=0
    bridge_hello_time_br0=1000

** Note**\
It is important to include `bridge_forward_delay_br0=0` and `bridge_hello_time_br0=1000` in the [/etc/conf.d/net] file in order to bring the bridge interface up quickly. Other values will cause network packets to be dropped for the first 30 seconds after the bridge has become active. This, in turn, could prevent DHCP from working as intended.

More documentation can be found by reading [/usr/share/doc/netifrc-\*/net.example.bz2], for example: [less /usr/share/doc/netifrc-0.5.1/net.example.bz2]

Next, create the init script by linking [net.lo] to [net.br0] and start the interface as follows:

`root `[`#`]`ln -s /etc/init.d/net.lo /etc/init.d/net.br0 `

`root `[`#`]`rc-service net.br0 start `

Finally, to make sure the bridge is automatically set up on subsequent boots add the newly generated init script to the system\'s default run level:

`root `[`#`]`rc-update add net.br0 default`

#### [Single NIC bridge]

There are cases when a bridge is needed even when only a single NIC is available on the system, such as a bridge for [LXC](https://wiki.gentoo.org/wiki/LXC "LXC"), [LXD](https://wiki.gentoo.org/wiki/LXD "LXD"), [Podman](https://wiki.gentoo.org/wiki/Podman "Podman"), [Xen](https://wiki.gentoo.org/wiki/Xen "Xen") or [docker](https://wiki.gentoo.org/wiki/Docker "Docker"), so that containers can be easily exposed to the LAN. In such a scenario, it is possible to put a single interface in the bridge configuration:

[FILE] **`/etc/conf.d/net`Single interface DHCP bridge config**

    config_enp1s0="null"
    bridge_br0="enp1s0"

    # Bridge dynamic config
    config_br0="dhcp"

    bridge_forward_delay_br0=0
    bridge_hello_time_br0=1000

The host machine will still have access to the network as the default route is now configured through the bridge interface. Now any containers using this bridge as the parent will be exposed to the LAN, which can be quite useful but also needs careful firewall protections as all ports are now exposed.

### [systemd]

As of systemd 210 and up, a special service called [systemd-networkd](https://wiki.archlinux.org/index.php/systemd-networkd) is available for network configuration. This service can handle bridge construction.

The basic procedure of creating a network configuration with systemd-networkd is creating several [.network] and [.netdev] files.

First, create a bridge. With systemd-networkd this is as simple as creating a new [.netdev] file:

[FILE] **`/etc/systemd/network/MyBridge.netdev`Systemd-networkd example**

    [NetDev]
    Name=br0
    Kind=bridge

After the bridge definition is created, assign the interfaces to the bridge:

[FILE] **`/etc/systemd/network/MyEth.network`Interface assignment example**

    [Match]
    Name=eth*

    [Network]
    Bridge=br0

Multiple interfaces can be matched and attached to the bridge.

Notice that this bridge is still not active. Activation can be achieved by creating a [.network] definition to use the bridge.

#### [DHCP]

[FILE] **`/etc/systemd/network/MyBridge.network`DHCP configuration**

    [Match]
    Name=br0

    [Network]
    DHCP=ipv4

#### [Static]

[FILE] **`/etc/systemd/network/MyBridge.network`Static configuration**

    [Match]
    Name=br0

    [Network]
    DNS=192.168.1.1
    Address=192.168.1.2/24
    Gateway=192.168.1.1

Defining a gateway is only necessary if one intends to use the physical network interface as access to another network. When using the bridge as a private network, omit it as systemd-networkd will add the bridge as a default route when the Gateway option is set.

Do remember to enable and start the systemd-networkd service.

## [Using NetworkManager]

An alternative way of setting up a bridge is to use tools provided in the [[[net-misc/networkmanager]](https://packages.gentoo.org/packages/net-misc/networkmanager)[]] package.

Verify the kernel has full support for [Iptables](https://wiki.gentoo.org/wiki/Iptables "Iptables") before proceeding.

Optionally install bridge management tools:

`root `[`#`]`emerge --ask bridge-utils ebtables`

Next enable iptables support for NetworkManager:

[FILE] **`/etc/portage/package.use/network`Enable iptables support**

    net-misc/networkmanager connection-sharing dhcpcd gnutls iwd resolvconf nftables -systemd -teamd iptables

Then create a bridge using NetworkManager\'s [nmcli] interface:

`root `[`#`]`nmcli con add type bridge con-name br0 ifname br0 <ip4 10.0.0.3/24 gw4 10.0.0.1> `

`root `[`#`]`nmcli con add type bridge-slave con-name br0-slave0 ifname eth0 master br0 `

`root `[`#`]`nmcli con add type bridge-slave con-name br0-slave1 ifname eth1 master br0 `

`root `[`#`]`nmcli con mod br0 ipv4.dns 1.1.1.1 ipv4.method manual `

`root `[`#`]`nmcli con up br0 `

## [See also]

-   [Netifrc/Brctl_Migration](https://wiki.gentoo.org/wiki/Netifrc/Brctl_Migration "Netifrc/Brctl Migration")
-   [Iproute2](https://wiki.gentoo.org/wiki/Iproute2 "Iproute2") --- a tool developed to unify network interface configuration, routing, and tunneling for Linux systems.

## [External resources]

-   [Official Linux network bridge documentation.](https://wiki.linuxfoundation.org/networking/bridge)
-   [Generic Linux network bridge how-to.](http://www.tldp.org/HOWTO/Ethernet-Bridge-netfilter-HOWTO.html)
-   [Creating a bridge with NetworkManager.](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/Networking_Guide/sec-Network_Bridging_Using_the_NetworkManager_Command_Line_Tool_nmcli.html)