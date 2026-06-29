**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Netifrc "Project:Netifrc")][Project](https://wiki.gentoo.org/wiki/Project:Netifrc "Project:Netifrc")

[[]][Package information](https://packages.gentoo.org/packages/net-misc/netifrc)

[[]][GitWeb](https://gitweb.gentoo.org/proj/netifrc.git)

[[]][GitHub (mirror)](https://github.com/gentoo/netifrc)

**netifrc** is Gentoo\'s default framework for configuring and [managing network](https://wiki.gentoo.org/wiki/Network_management "Network management") interfaces on systems running [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC"). It comes installed as part of the [system profile](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)") and is available in OpenRC [stage 3 file](https://wiki.gentoo.org/wiki/Stage_file "Stage file").

netifrc is powerful and convenient, but new users beware: using it requires knowledge of the *exact* system needs. Because of its modular approach it may require additional packages to be installed for what many users may consider \"basic functionality\" for home use.

The netifrc package can be uninstalled or simply left unused in favor of using [another network manager](https://wiki.gentoo.org/wiki/Network_management#Comparison_of_network_managers "Network management").

** Tip**\
For some simple network setups, such as cabled [Ethernet](https://wiki.gentoo.org/wiki/Ethernet "Ethernet") to a home router, no network configuration may be necessary, further than installing a [dhcp server](https://wiki.gentoo.org/wiki/Handbook:AMD64/Networking/Modular#DHCP "Handbook:AMD64/Networking/Modular").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration file]](#Configuration_file)
    -   [[2.1] [Basic examples]](#Basic_examples)
        -   [[2.1.1] [DHCP]](#DHCP)
        -   [[2.1.2] [DHCP with WPA Supplicant]](#DHCP_with_WPA_Supplicant)
        -   [[2.1.3] [Static address (CIDR notation)]](#Static_address_.28CIDR_notation.29)
        -   [[2.1.4] [Static address (netmask notation)]](#Static_address_.28netmask_notation.29)
    -   [[2.2] [Advanced examples]](#Advanced_examples)
        -   [[2.2.1] [Network bridge, multiple interfaces, IPv6]](#Network_bridge.2C_multiple_interfaces.2C_IPv6)
-   [[3] [Interfaces]](#Interfaces)
    -   [[3.1] [Services]](#Services)
    -   [[3.2] [Determine interface names]](#Determine_interface_names)
    -   [[3.3] [Creating symlinks]](#Creating_symlinks)
    -   [[3.4] [Bring up / down / restart interfaces]](#Bring_up_.2F_down_.2F_restart_interfaces)
    -   [[3.5] [Enable at boot]](#Enable_at_boot)
    -   [[3.6] [Disable at boot]](#Disable_at_boot)
-   [[4] [VLANs]](#VLANs)
-   [[5] [Bonding/LACP]](#Bonding.2FLACP)
-   [[6] [systemd]](#systemd)
-   [[7] [Additional hints]](#Additional_hints)
    -   [[7.1] [Maximum transmission unit size]](#Maximum_transmission_unit_size)
    -   [[7.2] [Priority of network interfaces]](#Priority_of_network_interfaces)
    -   [[7.3] [Troubleshooting: Link event detection]](#Troubleshooting:_Link_event_detection)
    -   [[7.4] [Setting ethtool options]](#Setting_ethtool_options)
-   [[8] [Documentation]](#Documentation)
-   [[9] [See also]](#See_also)
-   [[10] [External resources]](#External_resources)

## [Installation]

### [USE flags]

The [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") package has the `netifrc` [USE flag](https://packages.gentoo.org/useflags/netifrc), pulling in the package and enabling Gentoo\'s network stack ([net.\*] scripts).

### [Emerge]

The netifrc modules come in standard stage 3 file so they should be already installed on the system. In the case they have been removed, they can be re-installed via:

`root `[`#`]`emerge --ask net-misc/netifrc`

## [Configuration file]

[/etc/conf.d/net]

Within netifrc, each network interface is:

-   **Configured** in the [/etc/conf.d/net] file.
-   **Controlled** through it\'s own [/etc/init.d/net.\<interface_name\>] service script file, except for some dynamic interfaces such as Veth.

** Important**\
The config procedure involves both editing [/etc/conf.d/net] and [creating the corresponding service script](#Creating_symlinks) for each interface.

Netifrc provides a comprehensive set of features and configuration options. The complete guide is found on the [netifrc documentation at Gentoo\'s GitWeb site](https://gitweb.gentoo.org/proj/netifrc.git/tree/doc/net.example.Linux.in).

### [Basic examples]

#### [DHCP]

Although it\'s not necessary to explicitly configure it, here\'s an example to make use of DHCP on an interface.

[FILE] **`/etc/conf.d/net`Example DHCP configuration**

    # Note: DHCP is the default behavior if /etc/conf.d/net is empty or missing
    config_eth0="dhcp"

#### [DHCP with WPA Supplicant]

If WiFi is used, a module is needed for performing network authentication, such as wpa_supplicant.

[FILE] **`/etc/conf.d/net`Example DHCP configuration**

    # Note: This depends on wpa_supplicant being installed
    modules_wlan0="wpa_supplicant"
    config_wlan0="dhcp"

#### [][Static address (CIDR notation)]

If no DHCP is used, a static address can be configured.

[FILE] **`/etc/conf.d/net`Example static IP using CIDR**

    # For a static IP using CIDR notation
    config_eth0="192.168.0.7/24"
    routes_eth0="default via 192.168.0.1"
    # The 8.8.8.8 is provided here to show that multiple DNS servers entries can be added for a single interface.
    dns_servers_eth0="192.168.0.1 8.8.8.8"

** Tip**\
Use CIDR instead of the older Netmask notation today. For IPv6 or a dual stack IPv4/IPv6 setup it\'s mandatory.

#### [][Static address (netmask notation)]

This is a different notation for the same static address, route and DNS configuration.

[FILE] **`/etc/conf.d/net`Example static IP using netmask**

    # For a static IP using netmask notation
    config_eth0="192.168.0.7 netmask 255.255.255.0"
    routes_eth0="default via 192.168.0.1"
    dns_servers_eth0="192.168.0.1 8.8.8.8"

** Note**\
A default (empty or missing) [/etc/conf.d/net] will automatically use DHCP to configure any network interface(s) started by [net.\*] scripts.

### [Advanced examples]

#### [][Network bridge, multiple interfaces, IPv6]

[File]**`/etc/conf.d/net`Example multiple interfaces, IPv6 and a bridge** (click expand on right to view)

    # Configuration summary:
    # - 3 hardware interfaces
    # - 1 bridge
    # - 6 bridge ports used by VMs
    # - IPv4 / IPv6 Dual Stack
    # - static IPv6 tokens via hooks on all interfaces
    # - Note: Veth interfaces (containers) are not configured here (auto-created)
    # - Note: Line breaks on multiple routes are important

    # Configure Hardware Interfaces

    # eno1
    config_eno1="192.168.0.30/25 fd00::31/64"
    routes_eno1="default via 192.168.0.1
    default via fd00::1"

    # eno2
    config_eno2="192.168.0.31/25 fd00::31/64"
    routes_eno2="default via 192.168.0.1
    default via fd00::1"

    # enp7s0 (10G DAC)
    # bridge uplink, must be set to Null
    config_enp7s0="null"

    # Configure the Bridge
    config_br0="192.168.0.32/24 fd00::32/64"
    routes_br0="default via 192.168.0.1
    default via fd00::1"

    # set some bridge interface options
    bridge_forward_delay_br0=0
    bridge_hello_time_br0=1000
    bridge_stp_state_br0=0

    # attach the ports to the bridge and make their init scripts needed
    bridge_br0="enp7s0 tap1 tap2 tap3 tap4 tap5 tap6"
    rc_net_br0_need="net.enp7s0 net.tap1 net.tap2 net.tap3 net.tap4 net.tap5 net.tap6"

    # Create Bridge Ports (virtual interfaces for VMs)

    # VM-WINDOWS:eth0
    config_tap1="null"
    tuntap_tap1="tap"
    iproute2_tap1="user root"

    # VM-WINDOWS:eth1
    config_tap2="null"
    tuntap_tap2="tap"
    iproute2_tap2="user root"

    # VM-DEB1:eth0
    config_tap3="null"
    tuntap_tap3="tap"
    iproute2_tap3="user root"

    # VM-UBU1:eth0
    config_tap4="null"
    tuntap_tap4="tap"
    iproute2_tap4="user root"

    # VM-PFSENSE:eth0
    config_tap5="null"
    tuntap_tap5="tap"
    iproute2_tap5="user root"

    # VM-PFSENSE:eth1
    config_tap6="null"
    tuntap_tap6="tap"
    iproute2_tap6="user root"

    # Hook functions
    # for implementing features that are not handled by netifrc itself

    # set IPV6 interface token on physical interfaces
    preup() " = "eno1" ] ; then
         ip token set ::30 dev eno1
      fi
      if [ "$" = "eno2" ] ; then
         ip token set ::31 dev eno2
      fi
      return 0
    }

    # assign IPv6 token to bridges (workaround)
    # assign fe80: identifiers to match suffix
    postup() " = "eno1" ] ; then
         ip addr flush scope link dev eno1
         ip addr add fe80::31/64 dev eno1
      fi
      if [ "$" = "eno2" ] ; then
         ip addr flush scope link dev eno2
         ip addr add fe80::31/64 dev eno2
      fi
      if [ "$" = "br0" ] ; then
         ip token set ::30 dev br0
         ip addr flush scope link dev br0
         ip addr add fe80::30/64 dev br0
      fi
      return 0
    }

\

When migrating a bridge from [brctl] to [iproute], see the [Netifrc/Brctl Migration](https://wiki.gentoo.org/wiki/Netifrc/Brctl_Migration "Netifrc/Brctl Migration") article.

## [Interfaces]

### [Services]

As stated above, each network interface configured in [/etc/conf.d/net] needs its own service script located in the [/etc/init.d/] directory:

[/etc/init.d/net.lo]

[/etc/init.d/net.xyz (example)]

### [Determine interface names]

The first step in configuring netifrc is to get a list of the [network interfaces](https://wiki.gentoo.org/wiki/Handbook:Parts/Networking/Advanced#Network_interface_naming "Handbook:Parts/Networking/Advanced") present on the system. This is possible a couple different ways:

**Alternative 1:** The [ip] command will list all available interfaces when given the [link] action.

`user `[`$`]`ip link`

    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
         link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT group default qlen 1000
         link/ether 9a:02:79:45:ce:d2 brd ff:ff:ff:ff:ff:ff
    3: eth1: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
         link/ether ac:1f:6b:ad:43:23 brd ff:ff:ff:ff:ff:ff
       ...

The above command output is a cropped example. On a typical system, more interfaces will be present. Be aware that most of them are no physical interfaces, but virtual ones used for a variety of purposes.

In this example, `eth0` and `eth1` are physical (\"real\") network interfaces. They can be used for network connections outside the machine. In the description fields it can be seen that `eth0` is up and running (active) while `eth1` is down (not active).

Depending on the system, many interface names may be listed including: [eno1], [enp2s0], [wlan0], [ethernet0], [wireless0], etc. A system can have more than one interface connected to more than one network if the hardware is available.

**Alternative 2:** if [dmesg] is installed, a list of messages should be generated each time the system boots. Although the above method is better in practice, this approach can also be used to determine available network interfaces:

`user `[`$`]`dmesg | grep -i "network interface"`

For more information on the use of [dmesg] see the man page locally ([man dmesg]) or [online](http://man7.org/linux/man-pages/man1/dmesg.1.html).

**Alternative 3:** List known devices in [/sys/class/net]:

`user `[`$`]`ls /sys/class/net`

    eth0 eth1 lo sit0

** Tip**\
If network interfaces cannot be discovered using the means above, but the physical system hardware indicates otherwise, it is likely the appropriate kernel drivers for the network interface(s) have not been built for the currently running kernel or the system is lacking required firmware for interaction with the interface. Either the kernel will need to be configured to support the NIC driver and recompiled or the firmware will need to be installed; in some cases both changes will need to be performed For more information on how to perform these changes see the [kernel configuration article](https://wiki.gentoo.org/wiki/Kernel/Configuration "Kernel/Configuration").

### [Creating symlinks]

Now that the interface name is determined and configuration is done in [/etc/conf.d/net], the service script must be created. This is done by creating a symlink to [/etc/init.de/net.lo]:

`root `[`#`]`ln -s /etc/init.d/net.lo /etc/init.d/net.<interface_name>`

Replace `<interface_name>` with the name of the interface, for example `eth0`. Repeat for all interfaces that are configured and need to be started. These include hardware interfaces as well as bridges, tap interfaces etc.

When done with all interfaces, the existence of the script symlinks:

`root `[`#`]`ls /etc/init.d/net.* -l`

    lrwxrwxrwx 1 root root     6 Oct 10  2019 net.br0 -> net.lo
    lrwxrwxrwx 1 root root     6 Oct 10  2019 net.eth0 -> net.lo
    lrwxrwxrwx 1 root root     6 Oct 10  2019 net.eth1 -> net.lo
    lrwxrwxrwx 1 root root     6 Oct 10  2019 net.enp7s0 -> net.lo
    -rwxr-xr-x 1 root root 18514 Oct 09 15:37 net.lo
    lrwxrwxrwx 1 root root     6 Oct 10  2019 net.tap1 -> net.lo
    lrwxrwxrwx 1 root root     6 Oct 10  2019 net.tap2 -> net.lo
    lrwxrwxrwx 1 root root     6 Oct 10  2019 net.tap3 -> net.lo

In the example above, service scripts for 1 bridge (br0), 2 ethernet interfaces (eth0, eth1), 1 sfp+ interface (enp7s0) and 3 bridge ports (tap1, tap2, tap3) have been created. Note that [net.lo] is the only real file and the symlink target of all others.

### [][Bring up / down / restart interfaces]

As everything is configured now, interfaces can be managed by netifrc. This example uses the `eth0` interface:

Start (bring up) an interface:

`root `[`#`]`rc-service net.eth0 start`

Stop (bring down) an interface:

`root `[`#`]`rc-service net.eth0 stop`

** Warning**\
Stopping the primary routing interface will likely break the network connection. Care must be taken especially on remote machines, e.g. on SSH access. Restarting interfaces is usually the better choice.

Restart an interface:

`root `[`#`]`rc-service net.eth0 restart`

### [Enable at boot]

Running the [rc-update] is the final step in the configuration process. Add each interface to the system\'s init process so they are automatically started when the system boots. Normally interfaces are added to the *default* runlevel:

`root `[`#`]`rc-update add net.<interface_name> default`

Repeat the above command for each interface. A status message should appear showing successful adds to the init process.

### [Disable at boot]

If interfaces are no longer desired to be loaded during the init process they need to be removed from OpenRC or systemd. Run the following command for each interface that should be removed:

`root `[`#`]`rc-update del net.<interface_name> default`

## [VLANs]

To add a vlan to an interface:

[FILE] **`/etc/conf.d/net`Add VLAN 100 to interface eth0, and call it lan.**

    config_eth0="null"
    vlans_eth0="100"
    eth0_vlan100_name="lan"

** Note**\
Here, the host interface *eth0* has configuration disabled, because configuration is done on the created VLAN interface.

** Tip**\
Although not required, it can be helpful to name the created VLAN interfaces.

## [][Bonding/LACP]

To enable *802.3ad* LACP:

[FILE] **`/etc/conf.d/net`Bond eth0 and eth1, add vlan 100.**

    config_eth0="null"
    config_eth1="null"

    slaves_bond0="eth0 eth1"
    mode_bond0="802.3ad"
    config_bond0="null"

    vlans_bond0="100"
    bond0_vlan100_name="lan"

** Important**\
When using *802.3ad*, using VLANs is generally required.

## [systemd]

This article focuses on OpenRC as Gentoo\'s default init system. It is however possible run netifrc on systemd but at current, this requires deep knowledge (disable sysv-utils USE on systemd, adjust bootloader etc). For the sake of completeness, there are a couple differences to be documented here for systemd:

-   The [net@.service] unit is provided.
-   The systemd service calls a wrapper script (provided by netifrc).

Enable and start this unit on boot:

`root `[`#`]`systemctl --now enable net@<interface_name>.service`

Disable this unit:

`root `[`#`]`systemctl disable net@<interface_name>.service`

## [Additional hints]

### [Maximum transmission unit size]

To set a specific [MTU](https://en.wikipedia.org/wiki/Maximum_transmission_unit "wikipedia:Maximum transmission unit") size for an interface edit the [/etc/conf.d/net] file like below:

[FILE] **`/etc/conf.d/net`MTU size**

    mtu_eth0="1492"

### [Priority of network interfaces]

When 2 or more network interfaces are up, to set their priority, as example for preferred internet access on wlan0:

[FILE] **`/etc/conf.d/net`**

    # Routing priority
    metric_wlan0="90"
    metric_eth0="100"

### [Troubleshooting: Link event detection]

If an Ethernet cable is plugged in *after* the bootup process occurred, the network interfaces may not manually refresh themselves - even when using a DHCP client to manage the connections. A new address will not be assigned until the interface is manually refreshed by running the associated service script.

Two packages are available to aid in refreshing the network interface(s) during link events:

-   [[[sys-apps/netplug]](https://packages.gentoo.org/packages/sys-apps/netplug)[]]
-   [[[sys-apps/ifplugd]](https://packages.gentoo.org/packages/sys-apps/ifplugd)[]]

The [[[sys-apps/ifplugd]](https://packages.gentoo.org/packages/sys-apps/ifplugd)[]] package appears to be more maintained and is the recommended choice:

`root `[`#`]`emerge --ask sys-apps/ifplugd`

Once the install is complete network interfaces should be refreshed automatically whenever the system detects a link change event.

### [Setting ethtool options]

Sometimes it might be needed to set specific ethtool options. This can be done via [/etc/conf.d/net]. For example, to disable TCP segmentation offload, generic segmentation offload, and generic receive offload on network interface eth0:

[FILE] **`/etc/conf.d/net`**

    ethtool_offload_eno1="tso off gro off gso off"

## [Documentation]

Netifrc itself has no man page. The full configuration options are found on the [netifrc documentation at Gentoo\'s GitWeb site](https://gitweb.gentoo.org/proj/netifrc.git/tree/doc/net.example.Linux.in) or locally in [/usr/share/doc/netifrc-\<version_number\>/net.example.bz2]. Search \"`Cable in/out detection`\".

## [See also]

-   [Networking (AMD64 Handbook)](https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Networking "Handbook:AMD64/Full/Networking") - The Gentoo Handbook explains netifrc scripts in a high level of detail.
-   [Eudev: Classic interface naming](https://wiki.gentoo.org/wiki/Eudev#Keep_classic_network_interface_naming "Eudev") - How to keep classic naming for network interfaces instead of udev\'s \'predictable\' interface naming.
-   [Network management using DHCPCD](https://wiki.gentoo.org/wiki/Network_management_using_DHCPCD "Network management using DHCPCD") --- explains how to use dhcpcd for complete network stack management.
-   [Brctl Migration](https://wiki.gentoo.org/wiki/Netifrc/Brctl_Migration "Netifrc/Brctl Migration") --- outlines details necessary to migrate a netifrc-based bridge setup from [brctl] to [iproute].

## [External resources]

-   [Forum post](https://forums.gentoo.org/viewtopic-t-1016976-start-3.html)