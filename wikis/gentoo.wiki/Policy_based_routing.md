For certain network setups one routing table is simply not enough.

For example some network configurations can include two or more gateways exist to an uplink provider so that load balancing can be performed between the two uplinks. For example, a network administrator may choose to send all SSH traffic over one uplink gateway and all HTTP over the other.

Network configurations with just one gateway will send all traffic over one uplink while the other(s) remain unused.

With policy based routing, system administrators can choose by various parameters which packets should use which routing table and therefore perhaps take another route.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Create new routing table]](#Create_new_routing_table)
    -   [[2.2] [Decide which packets takes what routing table]](#Decide_which_packets_takes_what_routing_table)
    -   [[2.3] [ip rule]](#ip_rule)
    -   [[2.4] [iptables mark]](#iptables_mark)
        -   [[2.4.1] [Issues found]](#Issues_found)
    -   [[2.5] [Packet seems to disappear]](#Packet_seems_to_disappear)
-   [[3] [See also]](#See_also)

## [Installation]

### [Kernel]

[KERNEL] **Networking support**

    Networking options
        CONFIG_IP_ADVANCED_ROUTER
        IP_MULTIPLE_TABLES
        Network packet filtering framework (Netfilter)
          Core Netfilter Configuration
            CONFIG_NETFILTER_XT_MARK (only if you intend to use fwmarks as indicators for ip rule)
            IP_NF_MANGLE (only if you intend to use fwmarks as indicators for ip rule)

### [Emerge]

-   [[[sys-apps/iproute2]](https://packages.gentoo.org/packages/sys-apps/iproute2)[]]
-   [[[net-firewall/iptables]](https://packages.gentoo.org/packages/net-firewall/iptables)[]] (when intending to use fwmarks as indicators)

## [Configuration]

### [Create new routing table]

1.  Edit the [/etc/iproute2/rt_tables] file.
    1.  Append \[ID of the table\] \[Name of the table\]
2.  Add rules with [ip rule](https://wiki.gentoo.org/wiki/Static_routing "Static routing") but with table \[Table name or table ID\]
3.  Check with

    ::::: gw-box
    ::: box-caption
    [CODE]
    :::

    :::
        ip route show table [Table name or table ID]
    :::
    :::::

### [Decide which packets takes what routing table]

By default every packets takes the routing table main (ID 254). You can now specify rules for packets to take different routing tables (which will need created first), every packet which is not matching any rule still takes the default routing table (main).

### [ip rule]

A full list of the possible parameters you can get [here](http://man7.org/linux/man-pages/man8/ip-rule.8.html) If this is not sufficient for you (i.e. an source port), you can use fwmark. These fwmark you can set with iptables, so can create an ip rule with every match iptables is capable of.

### [iptables mark]

Simply use `-j MARK --set-mark <marknumber in decimal form>`. The target MARK only works in mangle. For incoming packets I use `-t mangle -A PREROUTING`, for outgoing packets `-t mangle -A OUTPUT`. Please be aware that the mark gets lost when the packet is processed by a process (i.e. apache), so if your packet arrives your network card and the way home doesn\'t work properly it\'s of no use if you mark the incoming packet, you have to mark the new generated outgoing packet.

#### [Issues found]

### [Packet seems to disappear]

Most likely the packet gets dropped because of it was considered \"martian\". In the actual kernel these packets get dropped silently. You can enable logging by:

[FILE] **`/etc/sysctl.conf`Enable log of martian packets**

    net.ipv4.conf.default.log_martians = 1
    net.ipv4.conf.all.log_martians = 1

If you now see messages with indicated when packets are considered martian, disable dropping them by:

[FILE] **`/etc/sysctl.conf`Disable dropping of martian packets**

    # Enables source route verification
    net.ipv4.conf.default.rp_filter=0
    # Enable reverse path
    net.ipv4.conf.all.rp_filter=0

## [See also]

-   [Static routing](https://wiki.gentoo.org/wiki/Static_routing "Static routing") --- covers routing of the IP protocol in the Linux kernel.