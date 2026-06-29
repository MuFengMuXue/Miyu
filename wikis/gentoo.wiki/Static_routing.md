Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/Static_routing/es "Enrutado estático (100% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Static_routing/hu "Statikus útválasztás (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Static_routing/ru "Статическая маршрутизация (100% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Static_routing/ja "静的ルーティング (100% translated)")

A *route* is a rule set in the kernel that is used to determine which physical network interface or gateway is needed in order to reach a particular network (or single host). There are many types of routed protocols; this article covers routing of the IP protocol in the Linux kernel.

Although IP routes are stored in the kernel, they are modifiable by userspace tools as described in the following examples.

## Contents

-   [[1] [Showing routes]](#Showing_routes)
-   [[2] [Adding a static route]](#Adding_a_static_route)
-   [[3] [Adding a permanent static route]](#Adding_a_permanent_static_route)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Showing routes]

Show the routing table with [iproute2](https://wiki.gentoo.org/wiki/Iproute2 "Iproute2"):

`user `[`$`]`ip route`

    default via 192.168.1.1 dev wlan1 metric 1
    192.168.50.0/24 dev lan proto kernel scope link src 192.168.50.1
    127.0.0.0/8 via 127.0.0.1 dev lo
    192.168.1.0/24 dev wlan1 proto kernel scope link src 192.168.1.1

## [Adding a static route]

The IP address, subnet mask (CIDR), and gateway are necessary prerequisite information before adding a static route.

In this example the `10.10.10.0` network with a `255.255.255.0` subnet mask will be routed to the `192.168.1.50` gateway. CIDR style netmasks are required when adding routes using commands from the [[[sys-apps/iproute2]](https://packages.gentoo.org/packages/sys-apps/iproute2)[]] package ([ip]). The following example will add the `10.10.10.0/24` route:

`root `[`#`]`ip route add 10.10.10.0/24 via 192.168.1.50`

Show the routing table using the [ip route] command:

`user `[`$`]`ip route`

    default via 192.168.1.1 dev wlan1 metric 1
    10.10.10.0/24 dev wlan1 via 192.168.1.50 src 10.10.10.1
    192.168.50.0/24 dev lan proto kernel scope link src 192.168.50.1
    127.0.0.0/8 via 127.0.0.1 dev lo
    192.168.1.0/24 dev wlan1 proto kernel scope link src 192.168.1.1

The routing table is sorted from most specific routes to most general. This is how it is read by the routing process. [Longest prefix match](https://en.wikipedia.org/wiki/Longest_prefix_match "wikipedia:Longest prefix match") - means the the smallest network, or the network with the largest netmask, or the most specific route f.e. `255.255.255.255` is at first position in the routing table.

## [Adding a permanent static route]

For users of the [netifrc](https://wiki.gentoo.org/wiki/Netifrc "Netifrc") scripts (OpenRC\'s standard network tools), permanent static routes can be added by opening a preferred text editor to [/etc/conf.d/net] and adjusting the file accordingly.

Reference the current routing table for help.

[FILE] **`/etc/conf.d/net`**

    routes_wlan1="10.10.10.0/24 via 192.168.1.50
        default via 192.168.1.1"

With [dhcpcd as network manager](https://wiki.gentoo.org/wiki/Network_management_using_DHCPCD "Network management using DHCPCD") the static route goes into [[/etc/dhcpcd.conf](https://wiki.gentoo.org/wiki/Dhcpcd#Static_IP_address "Dhcpcd")] instead.

Both statements above mean:

1.  IP packets destined to the `10.10.10.0/24` network are send to `192.168.1.50`.
2.  IP packets destined to all `0.0.0.0/0` other networks are send to `192.168.1.1`.

** Note**\
`0.0.0.0/0` means all other networks without a prefix (Subnet mask), the default route.

The **default route** `0.0.0.0/0` is used if:

-   The host has no physical or logical IP interface in the target network segment.
-   The host has to send IP packets outside of its own IP network segment, and there is no specific route found in the routing table for target IP network.

## [See also]

-   [iproute2](https://wiki.gentoo.org/wiki/Iproute2 "Iproute2") --- a tool developed to unify network interface configuration, routing, and tunneling for Linux systems.
-   [Network management](https://wiki.gentoo.org/wiki/Network_management "Network management") --- describes possibilities for managing the network stack.
-   [Dhcpcd#Static_IP_addresses](https://wiki.gentoo.org/wiki/Dhcpcd#Static_IP_addresses "Dhcpcd")

## [External resources]

-   [Longest prefix match](https://en.wikipedia.org/wiki/Longest_prefix_match "wikipedia:Longest prefix match") (on Wikipedia)
-   [[[Gentoo Bug 5409326]](https://bugs.gentoo.org/show_bug.cgi?id=540326#c9)[]]