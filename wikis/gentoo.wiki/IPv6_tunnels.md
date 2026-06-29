**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Tunnel_broker "wikipedia:Tunnel broker")

[[]][[#networking](ircs://irc.libera.chat/#networking)] ([[webchat](https://web.libera.chat/#networking)])

[[]][[#ipv6](ircs://irc.libera.chat/#ipv6)] ([[webchat](https://web.libera.chat/#ipv6)])

[[]][[alt.internet.ipv6](news:alt.internet.ipv6) ([weblink](https://www.novabbs.com/devel/thread.php?group=alt.internet.ipv6))]

[[]][r/ipv6](https://reddit.com/r/ipv6)

**IPv6 tunnels** are a mechanism by which the [IPv6](https://wiki.gentoo.org/wiki/IPv6 "IPv6") protocol can be encapsulated (\"tunneled\") over IPv4. This is necessary because some ISPs do not offer native IPv6 connections. To get around this limitation, there are several \"tunnel brokers\" that offer free IPv6 tunnels. This will allow tunneling all the IPv6 connections through an IPv4 connection.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Tunnel configuration]](#Tunnel_configuration)
    -   [[2.1] [Hurricane Electric]](#Hurricane_Electric)
    -   [[2.2] [Testing the connection]](#Testing_the_connection)
    -   [[2.3] [radvd configuration]](#radvd_configuration)

## [Installation]

### [Kernel]

Any kernels version v2.6.0 or higher can support [IPv6](https://www.linux-ipv6.org/).

`root `[`#`]`emerge --ask sys-kernel/gentoo-sources`

[KERNEL] **Required IPv6 options**

    [*] Networking support --->
        Networking options --->
            <M> The IPv6 protocol --->

    Device Drivers --->
        Network device support --->
            <M> Universal TUN/TAP device driver support  # This option is only required when using ptrtd for 6to4 conversion

### [Emerge]

`root `[`#`]`emerge --ask sys-apps/iproute2`

## [Tunnel configuration]

  -------------------------------------------------------------------------------------------- -----------------------------
  Broker                                                                                       Location
  [Hurricane Electric](https://tunnelbroker.net/)              North America, Europe, Asia
  [https://6project.org](https://6project.org)                 China, Europe, UK, US
  [https://BGPTunnel.com](https://BGPTunnel.com)               Germany
  [https://ipv6onlyhosting.com](https://ipv6onlyhosting.com)   Switzerland
  [https://ipv6.ip4market.ru/](https://ipv6.ip4market.ru/)     Russia
  [https://tb.netassist.ua/](https://tb.netassist.ua/)         Ukraine
  [https://tunnelbroker.se](https://tunnelbroker.se)           Sweeden
  -------------------------------------------------------------------------------------------- -----------------------------

### [Hurricane Electric]

Hurricane Electric (HE for short) offers free IPv6 tunnels and allocates a /64 block of addresses for each customer. It also allows configuration of reverse DNS. Getting a tunnel from HE is as easy as going to [https://www.tunnelbroker.net/](https://www.tunnelbroker.net/) and filling out a one page form.

** Note**\
Registration includes listing information like home address and phone number.

After a tunnel is approved and a /64 block is allocated, start to configure the system. HE provides sample configurations based on [ifconfig] and the iproute utilities. The following two examples assume that the following configuration is used:

  ---------------------------- ------------------------
  Local IPv4 Address (eth0)    68.36.91.195
  HE IPv4 Address              64.71.128.82
  Local IPv6 tunnel Address    2001:470:1F00:FFFF::2
  Remote IPv6 tunnel Address   2001:470:1F00:FFFF::1
  IPv6 Block                   2001:470:1F00:296::/64
  ---------------------------- ------------------------

Using the [[[sys-apps/iproute2]](https://packages.gentoo.org/packages/sys-apps/iproute2)[]] package and the [ip] command, do the following.

** Warning**\
Use of [ifconfig] can cause serious headaches with multiple tunnel devices. The tunnels need to be removed in backorder, which means the latest created tunnel must be removed first.

Create a tunnel between the local (eth0) IPv4 and HE\'s remote IPv4 address:

`root `[`#`]`ip tunnel add he6 mode sit remote 64.71.128.82 local 68.36.91.195 ttl 64 dev eth0`

Extract the tunneling overhead from the MTU:

`root `[`#`]`ip link set he6 mtu 1280`

Bring the tunnel up:

`root `[`#`]`ip link set he6 up`

Assign the IPv6 address to it:

`root `[`#`]`ip addr add 2001:470:1F00:FFFF::2 dev he6`

Route all global unicast IPv6 addresses through our \'he6\' tunnel device:

`root `[`#`]`ip route add 2000::/3 dev he6`

The following example shows how to establish this at boot time:

[CODE] **netifrc example**

    iptunnel_he6="mode sit remote 64.71.128.82 local 68.36.91.195 ttl 64 dev eth0"
    depend_he6="net.eth0"
    config_he6="2001:470:1F00:FFFF::2/64"
    routes_he6="default via 2001:470:1F00:FFFF::1 dev he6"
    mtu_he6="1280"

To make this device start on boot:

`root `[`#`]`cd /etc/init.d `

`root `[`#`]`ln -s net.lo net.he6 `

`root `[`#`]`rc-update add net.he6 default `

** Note**\
If there is no default policy of ACCEPT for the IPv4 iptables then add:

`root `[`#`]`iptables -A INPUT -i eth0 -p ipv6 -j ACCEPT`

When tunneling IPv6 over IPv4, the packets will first come through the IPv4 chain before being passed to the IPv6 chain.

### [Testing the connection]

Now that the tunnel is configured, test the connection. The easiest way to do this is to use the `ping6` utility and try to ping an IPv6 host.

`root `[`#`]`emerge --ask iputils`

`user `[`$`]`ping6 www.kame.net`

    PING www.kame.net(orange.kame.net) 56 data bytes
    64 bytes from orange.kame.net: icmp_seq=1 ttl=52 time=290 ms
    64 bytes from orange.kame.net: icmp_seq=2 ttl=52 time=277 ms
    64 bytes from orange.kame.net: icmp_seq=3 ttl=52 time=280 ms
    64 bytes from orange.kame.net: icmp_seq=4 ttl=52 time=279 ms
    64 bytes from orange.kame.net: icmp_seq=5 ttl=52 time=277 ms

    --- www.kame.net ping statistics ---
    5 packets transmitted, 5 received, 0% packet loss, time 4038ms
    rtt min/avg/max/mdev = 277.040/281.041/290.046/4.699 ms

### [radvd configuration]

[FILE] **`/etc/radvd.conf`Use the prefix assigned by the tunnel broker.**

    interface eth1
    ;
    };

** Important**\
Do not forget to start/reload radvd when making configuration changes.