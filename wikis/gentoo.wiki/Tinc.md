**Resources**

[[]][Home](https://tinc-vpn.org)

[[]][Package information](https://packages.gentoo.org/packages/net-vpn/tinc)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Tinc_(protocol) "wikipedia:Tinc (protocol)")

**tinc** is a versatile VPN which can work in a P2P configuration as well as more traditional topologies. It can be used to create a private mesh network without needing to configure individual connections between each nodes, as long as a path exists between them.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Basics]](#Basics)
    -   [[2.2] [Network configuration]](#Network_configuration)
    -   [[2.3] [Summary]](#Summary)
-   [[3] [Automatic startup]](#Automatic_startup)
    -   [[3.1] [OpenRC]](#OpenRC)
    -   [[3.2] [systemd]](#systemd)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [Emerge]

** Tip**\
Ensure that the tinc versions across all machines are matching, at least up to major version.

`root `[`#`]`emerge --ask net-vpn/tinc`

## [Configuration]

### [Basics]

All steps must be repeated per-machine unless otherwise noted. box1 is used as a placeholder.

First, choose a VPN/network name. As an example, *larrynet* is used here:

`root `[`#`]`mkdir -p /etc/tinc/larrynet/hosts`

All configuration will be done within [/etc/tinc/larrynet].

Create the main tinc config file at [/etc/tinc/larrynet/tinc.conf]:

[FILE] **`/etc/tinc/larrynet/tinc.conf`**

    Name = box1
    Device = /dev/net/tun
    AddressFamily = ipv4
    ConnectTo = box2

Generate a key for the host (choose the default save locations):

`root `[`#`]`tincd -n larrynet -K 4096`

There should now be a:

-   *private* key (do not share this with any other person or machine!) at [/etc/tinc/larrynet/rsa_key.priv], and
-   *public* key at [/etc/tinc/larrynet/hosts/box1]. This file will later need to be shared across each machine in the network.

The next step is to configure the network which may need to be adapted per desired configuration.

### [Network configuration]

On each host, some basics must be set. box2 must be configured to know about box1\'s location and details:

[FILE] **`/etc/tinc/larrynet/hosts/box1`**

    # This is where tinc can find box1 on the public internet / via some other already existing routing mechanism
    Address =

    # "This node accepts packets for this subnet" (or IP in this case)
    # This will mean box1 is identified as 192.168.100.1
    # Change this address per-host!
    Subnet = 192.168.100.1

Create hooks for tinc to bring up and shutdown the network:

[FILE] **`/etc/tinc/larrynet/tinc-up`**

    #!/bin/sh
    ip link set $ up

    # Change this address per-host to match the hosts/$hostname file!
    ip addr add 192.168.100.1 dev $

    ip route add 192.168.100.0/24 dev $

[FILE] **`/etc/tinc/larrynet/tinc-down`**

    #!/bin/sh
    ip route del 192.168.100.0/24 dev $

    # Change this address per-host to match the hosts/$hostname file!
    ip addr del 192.168.100.1 dev $

    ip link set $ down

And make them executable:

`root `[`#`]`chmod +x /etc/tinc/larrynet/tinc-up /etc/tinc/larrynet/tinc-down`

### [Summary]

For **each** machine, follow these steps:

1\. Create [/etc/tinc/larrynet/tinc.conf] with the hostname as above.

2\. Create a [/etc/tinc/larrynet/hosts/\$hostname] file as above *for each host in the network*, i.e. every machine must have a hosts file for every other machine.

## [Automatic startup]

### [OpenRC]

Edit [/etc/conf.d/tinc.networks] to add the network name:

[FILE] **`/etc/conf.d/tinc.networks`**

    [...]
    NETWORK: larrynet

Start up the network:

`root `[`#`]`/etc/init.d/tincd start`

Start it on boot:

`root `[`#`]`rc-update add tincd default`

### [systemd]

`root `[`#`]`systemctl enable --now tincd@larrynet`

## [See also]

-   [OpenVPN](https://wiki.gentoo.org/wiki/OpenVPN "OpenVPN")
-   [VPN services](https://wiki.gentoo.org/wiki/VPN_services "VPN services")

## [External resources]

-   [https://tinc-vpn.org/examples](https://tinc-vpn.org/examples)
-   [https://wiki.archlinux.org/index.php/Tinc](https://wiki.archlinux.org/index.php/Tinc)
-   [https://www.digitalocean.com/community/tutorials/how-to-install-tinc-and-set-up-a-basic-vpn-on-ubuntu-14-04](https://www.digitalocean.com/community/tutorials/how-to-install-tinc-and-set-up-a-basic-vpn-on-ubuntu-14-04)