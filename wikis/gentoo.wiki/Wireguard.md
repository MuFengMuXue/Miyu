This page contains [[changes](https://wiki.gentoo.org/index.php?title=WireGuard&diff=1411450)] which are not marked for translation.

\

**Resources**

[[]][Home](https://www.wireguard.io/)

[[]][Package information](https://packages.gentoo.org/packages/net-vpn/wireguard-tools)

[[]][GitWeb](https://git.zx2c4.com/wireguard-linux)

[[]][Wikipedia](https://en.wikipedia.org/wiki/WireGuard "wikipedia:WireGuard")

**WireGuard** is a modern, simple, and secure VPN that utilizes state-of-the-art cryptography. Considered an alternative to [OpenVPN](https://wiki.gentoo.org/wiki/OpenVPN "OpenVPN"), it can be used to create secure connections. Its goals are to be fast, simple, lean, and easy to configure. Wireguard consists of two components: userspace tools and a kernel module.

Wireguard is written and maintained by [Jason A. Donenfeld (zx2c4)](https://wiki.gentoo.org/wiki/User:Zx2c4 "User:Zx2c4") , a Gentoo developer.

Official and potentially more up-to-date installation instructions can be [found upstream](https://www.wireguard.com/install/).

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Kernel module loading]](#Kernel_module_loading)
    -   [[2.2] [Files]](#Files)
        -   [[2.2.1] [wg.conf]](#wg.conf)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Generate a keypair]](#Generate_a_keypair)
    -   [[3.2] [Network management methods]](#Network_management_methods)
        -   [[3.2.1] [wg-quick]](#wg-quick)
        -   [[3.2.2] [netifrc]](#netifrc)
        -   [[3.2.3] [Network Namespaces]](#Network_Namespaces)
            -   [[3.2.3.1] [Setup]](#Setup)
            -   [[3.2.3.2] [Configuration]](#Configuration_2)
            -   [[3.2.3.3] [(Optional) Cron job]](#.28Optional.29_Cron_job)
        -   [[3.2.4] [NetworkManager]](#NetworkManager)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Rebuilding modules on kernel upgrades for kernels less than 5.6]](#Rebuilding_modules_on_kernel_upgrades_for_kernels_less_than_5.6)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)
-   [[8] [References]](#References)

## [Installation]

### [Kernel]

Starting with Linux kernel 5.6, Wireguard is included in the upstream kernel sources. It is enabled via the following menuconfig option:

[KERNEL] **Enable `CONFIG_WIREGUARD`**

    Device Drivers  --->
        [*] Network device support  --->
            [*] Network core driver support
            <*>   WireGuard secure network tunnel

### [USE flags]

### [USE flags for] [net-vpn/wireguard-tools](https://packages.gentoo.org/packages/net-vpn/wireguard-tools) [[]] [Required tools for WireGuard, such as wg(8) and wg-quick(8)]

  --------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`+wg-quick`](https://packages.gentoo.org/useflags/+wg-quick)   Install the wg-quick(8) helper tool. Most users want to use this.
  [`selinux`](https://packages.gentoo.org/useflags/selinux)       !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  --------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-23 22:32] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install the wireguard-tools package to generate encryption keys and manage Wireguard interfaces:

`root `[`#`]`emerge --ask net-vpn/wireguard-tools`

## [Configuration]

### [Kernel module loading]

** Note**\
If wireguard support is added to the kernel as a module, configuring a wireguard interface should load the wireguard kernel module automatically, so there may be no need to set it to load in [/etc/modules-load.d/].

If WireGuard support has been added as a module, it may be necessary to instruct the selected init system to load the WireGuard kernel modules when the system boots.

Create a new file in the [/etc/modules-load.d/] directory in order to instruct the module loading service to get the module loaded on boot:

[FILE] **`/etc/modules-load.d/wireguard.conf`**

    wireguard

Or if VPN access is not needed very often, load kernel module manually:

`root `[`#`]`modprobe wireguard`

Loaded modules can be reviewed with [lsmod].

### [Files]

#### [wg.conf]

A WireGuard configuration file (the first of which is normally named [wg0.conf]) can be written as outlined in the man page. Review the CONFIGURATION FILE FORMAT and CONFIGURATION FILE FORMAT EXAMPLE sections in [man 8 wg]:

`user `[`$`]`man 8 wg`

As mentioned in the man page, WireGuard configuration files are defined in the INI format. A typical configuration file looks something like the following:

[FILE] **`wg0.conf`Wireguard configuration file example**

    [Interface]
    PrivateKey = yAnz5TF+lXXJte14tji3zlMNq+hd2rYUIgJBgB3fBmk=
    ListenPort = 51820

    [Peer]
    PublicKey = xTIBA5rboUvnH4htodjb6e697QjLERt1NAB4mZqp8Dg=
    Endpoint = 192.95.5.67:1234
    AllowedIPs = 10.192.122.3/32, 10.192.124.1/24

    [Peer]
    PublicKey = TrMvSoP4jYQlY6RIzBgbssQqY3vxI2Pi+y71lOWWXX0=
    Endpoint = [2607:5300:60:6b0::c05f:543]:2468
    AllowedIPs = 10.192.122.4/32, 192.168.0.0/16

    [Peer]
    PublicKey = gN65BkIKy1eCE9pP1wdc8ROUtkHLF2PfAqYdyYBz6EA=
    Endpoint = test.wireguard.com:18981
    AllowedIPs = 10.10.10.230/32

## [Usage]

### [Generate a keypair]

Before using WireGuard a keypair has to be generated. This can be accomplished using [wg(8)]:

`user `[`$`]`$(umask 077; wg genkey | tee privatekey | wg pubkey > publickey)`

### [Network management methods]

Various [network management](https://wiki.gentoo.org/wiki/Network_management "Network management") methods are available to supervise Wireguard tunnels.

#### [wg-quick]

Configuration can be automated using the [wg-quick] utility, which will create tunnels using configuration files in the [/etc/wireguard] file:

`root `[`#`]`wg-quick up wg0`

For more information on [wg-quick] consult [man 8 wg-quick].

The [[[net-misc/netifrc]](https://packages.gentoo.org/packages/net-misc/netifrc)[]] scripts (typically used with OpenRC) can be used to quickly bring Wireguard interfaces. Presuming a correctly defined [/etc/wireguard/wg0.conf] file has been created:

`root `[`#`]`ln -s /etc/init.d/wg-quick /etc/init.d/wg-quick.wg0 `

`root `[`#`]`rc-update add wg-quick.wg0 default `

To bring up the interface now:

`root `[`#`]`/etc/init.d/wg-quick.wg0 start`

\

** Warning**\
Deleting

`root `[`#`]`ip link del wg0`

or bringing down

`root `[`#`]`ip link set wg0 down`

the WireGuard interface will **\*\*NOT\*\*** stop packets routed to the WireGuard interface; packets will instead be routed normally through other interfaces!

#### [netifrc]

This implementation of WireGuard uses the same logic as [wg-quick], but putting the logic directly in [/etc/conf.d/net] for [netifrc].

\
Using the `wg-quick` USE flag will add [[[virtual/resolvconf]](https://packages.gentoo.org/packages/virtual/resolvconf)[]] as a dependency. This might be a deal-breaker for systems that want to keep the [resolv.conf] file from being modified by external utilities. Luckily, this implementation does not use such dependencies; it\'s okay to add the `-wg-quick` USE flag to [[[net-vpn/wireguard-tools]](https://packages.gentoo.org/packages/net-vpn/wireguard-tools)[]].

[FILE] **`/etc/portage/package.use/wireguard`**

    net-vpn/wireguard-tools -wg-quick

\
Copy the following [netifrc] configuration file to [/etc/conf.d/net] and edit the interfaces as needed to work with the machine:

`root `[`#`]`cat /etc/conf.d/net`

    # Make sure to change all values for our setup! These are just an example.
    #
    # Make sure that net-dns/openresolv, virtual/resolvconf, their dependencies, and other resolv.conf managers
    # aren't installed to keep the setup simple and secure! This might require us to add -wg-quick to
    # net-vpn/wireguard-tools and rebuild the package.

    # Bring up hardware network interface; change enp5s0, to our interface, shown when running: ip addr
    config_enp5s0="dhcp"

    # Setup a DNS server here if we're going to change to another DNS server when bringing up the Wireguard interface.
    # Some providers give us an address; it's better to change the address for privacy reasons.
    # Change enp5s0 to our interface, shown when running: ip addr
    dns_servers_enp5s0="1.2.3.4 123.12.21.1"

    # Bring up Wireguard virtual network interface; the IP here is from our VPN provider or custom Wireguard setup.
    config_wg0="5.6.7.8/32"

    # Connect to Wireguard endpoint using config; we need to create this config if it doesn't exist.
    wireguard_wg0="/etc/wireguard/wg0.conf"

    # Prevent DHCP from setting a DNS server gotten from our router.
    dhcp="nodns"

    postup()
    '))

            # Get the firewall mark used by the WG interface.
            local -r  WG_FWMARK="$(wg show "$IFACE" fwmark)"

            # The WG routing table *CAN* be different than the WG firewall mark. It's the same here so that each WG interface has it's own unique table.
            local -r  WG_ROUTING_TABLE="$WG_FWMARK"

            sysctl -q net.ipv4.conf.all.src_valid_mark=1

            for current_wg_address in "$"; do
                ip route add "$current_wg_address" dev "$IFACE" table "$WG_ROUTING_TABLE"
            done

            # If there are multiple WG interfaces, the following commands might break them:
            ip -4 rule add not fwmark "$WG_FWMARK" table "$WG_ROUTING_TABLE"
            ip -6 rule add not fwmark "$WG_FWMARK" table "$WG_ROUTING_TABLE"

            ip -4 rule add table main suppress_prefixlength 0
            ip -6 rule add table main suppress_prefixlength 0

            # Instead of running multiple 'nft' commands, we add all the modifications into one 'nft' command to keep nftables atomic.
            local nftcmd=''
            printf -v nftcmd '%sadd table %s %s\n'                                                                "$nftcmd" inet "$_inet_table"
            printf -v nftcmd '%sadd chain %s %s preraw \n'          "$nftcmd" inet "$_inet_table"
            printf -v nftcmd '%sadd chain %s %s premangle \n'       "$nftcmd" inet "$_inet_table"
            printf -v nftcmd '%sadd chain %s %s postmangle \n'     "$nftcmd" inet "$_inet_table"

            local ip_version=''
            for current_wg_address in $; do
                [[ "$current_wg_address" =~ \. ]] && ip_version=ip || ip_version=ip6
                printf -v nftcmd '%sadd rule %s %s preraw iifname != "%s" %s daddr %s fib saddr type != local drop\n' "$nftcmd" inet "$_inet_table" "$IFACE" "$ip_version" "$current_wg_address"
            done

            printf -v nftcmd '%sadd rule %s %s postmangle meta l4proto udp mark %s ct mark set mark \n'           "$nftcmd" inet "$_inet_table" "$WG_FWMARK"
            printf -v nftcmd '%sadd rule %s %s premangle meta l4proto udp meta mark set ct mark \n'               "$nftcmd" inet "$_inet_table"
            nft -f <(echo -n "$nftcmd")
        fi

        # This function should return 0 on success.
        return 0
    }

    predown()
    "
            return 1
        fi

        # This WireGuard implementation uses the same logic as what's inside the 'wg-quick' script.
        if [[ "$IFACE" =~ ^wg[[:digit:]]+$ ]]; then

            local -r WG_FWMARK="$(wg show "$IFACE" fwmark)"
            local -r WG_ROUTING_TABLE="$WG_FWMARK"

            nft delete table inet "$_inet_table"
            ip -4 rule delete table "$WG_ROUTING_TABLE"
            ip -6 rule delete table "$WG_ROUTING_TABLE"

            # If there are multiple WG interfaces, the following commands might break them:
            ip -4 rule delete table main suppress_prefixlength 0
            ip -6 rule delete table main suppress_prefixlength 0

            # This step is already done by netifrc.
            #ip link delete dev "$IFACE"
        fi

        # This function should return 0 on success.
        return 0
    }

Remove any [wg-quick] extensions in [/etc/wireguard/wg0.conf] as they will not be recognized by [wg] (the tool that [netifrc] uses). Read the man page for [wg] to know what is syntactically correct. In short, remove the following lines in the configuration file if they exist:

[CODE] **Lines to remove**

    Address = ...
    MTU = ...
    DNS = ...
    Table = ...
    PreUp = ...
    PreDown = ...
    PostUp = ...
    PostDown = ...
    SaveConfig = ...

The contents of [Address =] should go into [config_wg0=]. The contents of [DNS =] should go into [dns_servers_wg0=].

\

** Important**\
In order for this implementation to work, a firewall mark **\*\*MUST\*\*** be set in the WireGuard configuration file!

[CODE]

    FwMark = 334455

If a firewall mark is not set, packets will not be routed to the WireGuard interface!

\
Once the WireGuard and netifrc configuration files are done, we are ready to use them. To bring up the WireGuard interface, make the symlink for [wg0] and start it just like any other physical interface:

`root `[`#`]`ln -s /etc/init.d/net.lo /etc/init.d/net.wg0 `

`root `[`#`]`rc-service net.wg0 start `

To have WireGuard start at system boot:

`root `[`#`]`rc-update add net.wg0 default`

\

** Warning**\
Deleting

`root `[`#`]`ip link del wg0`

or bringing down

`root `[`#`]`ip link set wg0 down`

the WireGuard interface will **\*\*NOT\*\*** stop packets routed to the WireGuard interface; packets will instead be routed normally through other interfaces!

#### [Network Namespaces]

This implementation of WireGuard uses network namespaces, which are isolated networks that can be assigned interfaces. The benefit of doing this instead of changing firewall rules is that it\'s more clear that all or specified packets will go through a WireGuard interface even if the WireGuard interface goes down or gets deleted.

TL;DR:

To bring up a WireGuard interface (simplified):

-   Make a new network namespace, \"physical\"
-   Make a new WireGuard interface, \"wg0\", in network namespace \"physical\"
-   Move \"wg0\" from network namespace \"physical\" to \"init\"/\"1\"
-   Move all interfaces that can connect to the internet in network namespace \"init\"/\"1\" to \"physical\"

\
To bring down a WireGuard interface (simplified):

-   Move all interfaces that can connect to the internet in network namespace \"physical\" to \"init\"/\"1\"
-   Delete \"wg0\"
-   Delete \"physical\"

\
To bring up a WireGuard interface, we make a new network namespace with some name like, \"physical\"; then, we make a new WireGuard interface with the name \"wg0\" in the \"physical\" namespace then move it to the \"init\"/\"1\" namespace (the namespace that all interfaces start in). Then, move all interfaces that can connect to the internet to the \"physical\" interface. To bring down a WireGuard interface, we move all the interfaces that we previously moved to \"physical\" back to \"init\"/\"1\". Then, we delete the \"wg0\" WireGuard interface and the \"physical\" network namespace since we\'re not using them anymore. This is a simplified explanation, there are other steps that happen in between, such as routing packets to the WireGuard interface, but this is the biggest difference compared to other implementations.

This implementation also has the benefit of giving the user the ability to allow specified applications to temporarily bypass the WireGuard interface. For example, let\'s say we\'re using public WiFi at a hotel, shop, airport, etc. and we want to route all our packets through WireGuard to our home network. Everything works fine except when the hotel requires users to authenticate themselves through a web portal before they actually give us a connection to the internet.

Before, we would have to bring down the WireGuard interface, authenticate ourselves through the portal via our browser of choice (such as [LibreWolf](https://wiki.gentoo.org/wiki/LibreWolf "LibreWolf")), then bring up the WireGuard interface again. In the time when the WireGuard interface was down, other running applications with network capabilities might connect to the internet. This can be a serious security, privacy, and anonymity concern if we **really** don\'t want anyone else to know what our machine is trying to connect to.

With network namespaces, we can handle the situation without ever bringing down the WireGuard interface. When WireGuard is set up using network namespaces, the only interface running applications can see/use is the WireGuard interface. All the interfaces that actually connect to the internet are in a different namespace and cannot be directly seen/used unless we give an application the ability to do so. We can do this by prefixing the command to run the application with another that temporarily bypasses the WireGuard interface until we close the application.

##### [Setup]

Normally we move interfaces with the [ip] command provided by [[[sys-apps/iproute2]](https://packages.gentoo.org/packages/sys-apps/iproute2)[]], but for wireless ones, we need to use the [iw] command provided by [[[net-wireless/iw]](https://packages.gentoo.org/packages/net-wireless/iw)[]]. If our machine has wireless interfaces, such as a laptop, we need to install [iw].

`root `[`#`]`emerge --ask net-wireless/iw`

Using the `wg-quick` USE flag will add [[[virtual/resolvconf]](https://packages.gentoo.org/packages/virtual/resolvconf)[]] as a dependency. This might be a deal-breaker for systems that want to keep the [resolv.conf] file from being modified by external utilities. Luckily, this implementation does not use such dependencies; it\'s okay to add the `-wg-quick` USE flag to [[[net-vpn/wireguard-tools]](https://packages.gentoo.org/packages/net-vpn/wireguard-tools)[]].

[FILE] **`/etc/portage/package.use/wireguard`**

    net-vpn/wireguard-tools -wg-quick

\
Now, this implementation involves copy-pasting a WireGuard configuration file, some scripts, and optionally setting up a cron job for automated starting of the WireGuard interface.

** Note**\
At the time of making this namespace solution, OpenRC seems to have several bugs related to namespaces, even though OpenRC supports network namespaces via [netns] in [/etc/conf.d/net]. Testing has shown that

-   interfaces are not reliably placed when they are given a specified network namespace ([netns_eth0=\"physical\"]) even when the namespace exists.
-   services that depend on said interface ([ depend()  ]) start in the specified namespace when they shouldn\'t.

\

This is why we use a cron job to automate the starting of WireGuard instead of using an OpenRC Service Script.

Make the directory for WireGuard configuration files:

`root `[`#`]`mkdir -p /etc/wireguard`

Set the correct permissions because this directory can contain keys:

`root `[`#`]`chmod 700 /etc/wireguard`

Copy the following WireGuard configuration file to [/etc/wireguard/wg0.conf]:

`root `[`#`]`cat /etc/wireguard/wg0.conf`

    # /etc/wireguard/wg0.conf

    [Interface]
    PrivateKey = INTERFACE_PRIVATE_KEY_PLACEHOLDER

    # Space-separated list of addresses for the WG interface.
    Address =

    # (Optional) Maximum Transmission Unit (MTU) of the WG interface. If there is no specified MTU, then 'ip' will decide the optimal value.
    MTU =

    # (Optional) Space-separated list of IPv4, IPv6, or hostname Domain Name System (DNS) for the WG interface.
    DNS =

    # The name of the namespace where all the non-WG interfaces will be.
    Namespace = physical

    # (Optional) Space-separated list of interfaces that the WG interface will use. The specified interfaces will be in the same namespace. If there are no
    # specified interfaces, then all interfaces will be used except for the loopback (lo) and other WG interfaces. If the only specified interface is "NONE",
    # no interfaces will be modified.
    PhysicalInterface =

    # (Optional) Space-separated list of services that should use the WG interface; the only services that *NEED* to be listed here are the ones that are stopped
    # because of an interface stopping (a service with a 'net' dependency). If we're not sure, run 'rc-status' after this script runs to see which services get
    # stopped, then add them to this variable.
    #
    # All other services that are still running will use the WG interface. :)
    ExtraServiceYes =

    # (Optional) Space-separated list of services that should *NOT* use the WG interface. These services will bypass the WG interface and run in the
    # "wg_outgoing_namespace" namespace.
    ExtraServiceNo =

    [Peer]
    PublicKey = PEER_PUBLIC_KEY_PLACEHOLDER
    PresharedKey = PRESHARED_KEY_PLACEHOLDER
    AllowedIPs = 0.0.0.0/0, ::/0
    Endpoint = IP_ADDRESS_OR_DOMAIN_PLACEHOLDER:51820

    # This can help keep the connection alive when this machine is behind a NAT.
    PersistentKeepAlive = 25

(Optional) Set the correct permissions for the file; this is not required because we already set the permissions for the directory this file sits in:

`root `[`#`]`chmod 600 /etc/wireguard/wg0.conf`

Copy the following scripts into [/usr/local/bin] so that they can be found by the [PATH] environment variable:

`root `[`#`]`cat /usr/local/bin/wg-netns`

    #!/bin/bash

    # /usr/local/bin/wg-netns

    # NOTE:
    # * This script was written for OpenRC, but don't let that scare one from adapting it to other init systems or turning it into a generic script. All of the
    #   OpenRC-specific commands in this script can be found by searching for 'rc-'; there's only like... 4 :)
    #   Understand that it might not be as simple as replacing the 'rc-*' text, one needs to understand the syntax of the line of code and the surrounding code.
    #
    # * This implementation of WireGuard (WG) uses "The New Namespace Solution" provided by the official WG docs.
    #   https://www.wireguard.com/netns/#the-new-namespace-solution
    #
    # * The "init" namespace is the one that all interfaces start in (process id 1).
    #
    # * At any point, we can check what interfaces are in what namespace by running:
    #   - 'ip link'                (shows interfaces in the "init" / "1" namespace)
    #   - 'ip -n <namespace> link' (shows interfaces in the "namespace"  namespace)
    #
    # * To run a command inside a specific namespace, prefix the command with:
    #   'ip netns exec <namespace>'
    #
    # * We only need one WG interface because we can have multiple peers per interface.
    #
    # * If the system uses Pluggable Authentication Modules (PAM) for OpenRC, add the following line to /etc/pam.d/run_init:
    #   "auth sufficient pam_rootok.so"
    #   This makes it so that running OpenRC commands as root (or running this script as root) will not prompt for further authentication.

    # -----------------------------------   ----------------------------------------
    # |The "init"/"1" namespace         |   |"mynetns0" namespace                  |
    # |Seen by running 'ip link'        |   |Seen by running 'ip -n mynetns1 link' |
    # |                                 |   |                                      |
    # |Applications will normally       |   |                                      |
    # |use this namespace and      wg0---------+                             eth0-----> Internet
    # |only see the WG                  |   |                                      |
    # |interfaces.                      |   |                                      |
    # |                                 |   |                                eth1-----> Internet
    # |If we want an app to        wg1---------+                                   |
    # |bypass the WG interfaces,        |   |                                      |
    # |we can prefix the command to run |   |                               wlan0-----> Internet
    # |the app with:                    |   |                                      |
    # |'ip netns exec <namespace>'      |   |                                      |
    # |to run the app in the specified  |   ----------------------------------------
    # |namespace.                       |
    # |                                 |   ----------------------------------------
    # |                                 |   |"mynetns1" namespace                  |
    # |                                 |   |                                      |
    # |                                 |   |                                      |
    # |                                 |   |                                      |
    # |                            wg2---------+                             eth2-----> Internet
    # |                                 |   |                                      |
    # |                                 |   |                                      |
    # |                                 |   ----------------------------------------
    # |                                 |
    # |                                 |                  ...
    # |                                 |
    # |                                 |
    # |                                 |   ----------------------------------------
    # |                                 |   |"mynetns999" namespace                |
    # |                                 |   |                                      |
    # |                                 |   |                                      |
    # |                                 |   |                                      |
    # |                          wg999---------+                           eth999-----> Internet
    # |                                 |   |                                      |
    # |                                 |   |                                      |
    # -----------------------------------   ----------------------------------------

    ####################
    # Internal variables
    ####################

    # NOTE:
    # The following variables should **NOT** be modified; these are made by this script.

    # This is an internal variable not intended for the user.
    declare -a Interface_list=()

    # This is an internal variable not intended for the user.
    declare    wg_config_file_data_built_by_this_script=''

    ###########################
    # User-modifiable variables
    ###########################

    # NOTE:
    # The following variables can be modified here. Array variables are incremental to the WG config file; non-array variables get overridden by the WG config file.

    # Space-separated list of addresses for the WG interface.
    declare -a Wg_address=()

    # (Optional) Maximum Transmission Unit (MTU) of the WG interface. If there is no specified MTU, then 'ip' will decide the optimal value.
    declare    wg_mtu=''

    # (Optional) Space-separated list of IPv4, IPv6, or hostname Domain Name System (DNS) for the WG interface.
    declare -a Wg_dns=()

    # The name of the namespace where all the non-WG interfaces will be.
    declare    wg_outgoing_namespace=''

    # (Optional) Space-separated list of interfaces that the WG interface will use. The specified interfaces will be in the same namespace. If there are no
    # specified interfaces, then all interfaces will be used except for the loopback (lo) and other WG interfaces. If the only specified interface is "NONE",
    # no interfaces will be modified.
    declare -a Wg_physical_interface=()

    # (Optional) Space-separated list of services that should use the WG interface; the only services that **NEED** to be listed here are the ones that are stopped
    # because of an interface stopping (a service with a 'net' dependency). If we're not sure, run 'rc-status' after this script runs to see which services get
    # stopped, then add them to this variable.
    #
    # All other services that are still running will use the WG interface. :)
    declare -a Extra_service_through_wg=()

    # (Optional) Space-separated list of services that should **NOT** use the WG interface. These services will bypass the WG interface and run in the
    # "wg_outgoing_namespace" namespace.
    declare -a Extra_service_through_no_wg=()

    # What this script will do.
    declare -r SELF_ACTION="$1"

    # The name of the WG interface.
    declare -r WG_INTERFACE="$2"

    # What the WG interface name should match; must start with '^' and end with '$'.
    declare -r WG_INTERFACE_REGEX='^wg[[:digit:]]+$'

    # This is just a way to tell the difference between the initial namespace and a WireGuard one.
    declare -r INITIAL_NAMESPACE="initial_namespace"

    ###########
    # Functions
    ###########

    # This function prints the command about to be executed to stderr before it actually executes. This is helpful for debugging.
    print_cmd()


    # This function prints a message and a spinner to stderr to let the user know that the script is still running. This is so that we don't fill multiple lines
    # waiting for something.
    message_spin()
    " >&2
                sleep .1
            done
        done
    }

    # This is a wrapper for the message_spin function to easily add a message and spinner to any command.
    message_spin_wrapper()


    # Configure the WG interface.
    configure_wg_interface()


        # Configure the "WG_INTERFACE" interface like usual, and set it as the default route.
        wg setconf "$WG_INTERFACE" <(echo "$wg_config_file_data_built_by_this_script")

        for current_wg_address in "$"
        do
            print_cmd ip address add "$current_wg_address" dev "$WG_INTERFACE"
        done

        print_cmd ip link set "$WG_INTERFACE" up

        # Select which IP addresses will be routed to the WG interface; to route all IPv4 and IPv6 packets, add "AllowedIPs = 0.0.0.0/0, ::/0" to the
        # WG config file.
        for current_wg_address in $(wg show "$WG_INTERFACE" allowed-ips | gawk '')
        do
            print_cmd ip route add "$current_wg_address" dev "$WG_INTERFACE"
        done
    }

    # Move an interface from one namespace to another.
    #
    # If the working namespace is the initial namespace, move the specified interface into the "wg_outgoing_namespace" namespace, and vice-versa.
    move_interface()
     iw dev "$current_interface" info &>/dev/null
        then
            # Use the 'iw' command since the interface is wireless.
            #
            # NOTE:
            # 'iw' doesn't use the name of the interface, it uses it's "physical index".
            wiphy_index=$($ iw dev "$current_interface" info | gawk '$1 == "wiphy" ')
            print_cmd $ iw phy phy"$wiphy_index" set netns $
            return
        fi

        # The interface is not wireless, so we use the 'ip' command.
        print_cmd $ ip link set "$current_interface" netns $
    }

    # This function might or might not be needed depending on the init system.
    wait_for_interface_to_be_up()
    "
        do
            # Skip interfaces that are not supposed to be up.
            [[ ! "$current_interface" =~ :UP$ ]] && continue

            # Wait until the current interface is up.
            message_spin_wrapper "Waiting for $ to be up" wait_for_current_interface_to_be_up
        done
    }

    wait_for_current_interface_to_be_up()
     ip link | grep -E -- "$.*state UP")" ]] && break
            sleep 1
        done
    }

    # Perform an action on a service.
    act_on_extra_service()
    "
        do
            print_cmd rc-service "$current_service" "$INTERFACE_ACTION" &
        done

        # Start/stop services that should **NOT** use the WG interface.
        #
        # NOTE:
        # Technically, we don't have to wait for the interfaces to be up before we start services that will be ran in the same namespace as said interfaces;
        # this is due to the OpenRC behavior explained in the "wait_for_interface_to_be_up" function. The code is placed here anyway to keep this script as
        # simple as possible.
        for current_service in "$"
        do
            print_cmd $ rc-service "$current_service" "$INTERFACE_ACTION" &
        done

        # We run service commands in parallel to speed things up, but we still have to wait for all of them to finish.
        wait -f
    }

    get_interface_to_act_on()
    " == "NONE" ]] && return

        # If we have any specified interfaces, we will only act on them.
        for current_interface in "$"
        do
            # Build the 'ip link' output for the specified interfaces.
            print_interface+="$($ ip link show "$current_interface")"$'\n'
        done

        # If this variable is empty, it means that we did not specify any interfaces. The behavior now, is to act on all interfaces.
        if [[ -z "$print_interface" ]]
        then
            print_interface="$($ ip link)"
        fi

        # This function will return the name and state of the final set of interfaces in the form of '<name>:<state>'.
        echo "$print_interface" | gawk '$1 ~ /^[[:digit:]]+:$/ '
    }

    # Perform an action on an interface.
    act_on_interface()

        # $
        #
        # These parameter expansions will modify the commands that they're in. We use these because we might need to run a command in a specific network
        # namespace or make some modification to a value due to the specific network namespace. Using these parameter expansions prevents us from writing x2
        # as much code.
        [[ "$WORKING_NAMESPACE" != "$INITIAL_NAMESPACE" ]] && are_we_working_in_wg_namespace="1"

        # We only care about performing the following on a "stop" because we will lose information about our system (specifically network interfaces) when we
        # "stop".
        if [[ "$INTERFACE_ACTION" == "stop" ]]
        then
            # Before we do anything, we want to have all of our network interfaces that are supposed to be started actually started. This is different from
            # the interface being "UP" as stated by 'ip link'.
            #
            # NOTE:
            # There seems to be a bug where OpenRC cannot resume network interfaces in a different network namespace when recovering from sleep.
            # This causes a permanent "inactive" status on the interface, causing the script to loop forever. To prevent this from happening, we can skip
            # this step when bringing down WireGuard.
            [[ -z "$are_we_working_in_wg_namespace" ]] && message_spin_wrapper "Waiting for the init system to start network interfaces" wait_for_init_system_to_start_network_interface

            # Keep track of the state of each interface that we are going to modify so that we know which ones to start up (the ones that were already up).
            Interface_list=($(get_interface_to_act_on))
        fi

        for current_interface in "$"
        do
            # Only start interfaces that were up before we stopped them.
            [[ ! "$current_interface" =~ :UP$ && "$INTERFACE_ACTION" == "start" ]] && continue

            current_interface="$"

            # If the interface is the loopback or a WG one, skip.
            [[ "$current_interface" == "lo" || "$current_interface" =~ $WG_INTERFACE_REGEX ]] && continue

            case "$INTERFACE_ACTION" in
            start|stop)
                start_stop_interface
                ;;

            move)
                move_interface
                ;;

            esac
        done

        # We run service commands in parallel to speed things up, but we still have to wait for all of them to finish.
        wait -f

        act_on_extra_service
    }

    start_stop_interface()
     rc-service -D net."$current_interface" "$INTERFACE_ACTION" &
    }

    act_on_dns()
    "
            do
                [[ "$current_dns" =~ ^[[:digit:].]+$|: ]] && Nameserver+=("$current_dns") || Search+=("$current_dns")
            done

            # /etc/resolv.conf has specific syntax:
            # - only one 'nameserver' per keyword
            # - if there are multiple 'search' directives, only the search list from the last instance is used
            # See 'man resolv.conf' for more info.
            "
                [[ "$"     -gt 0 ]] && printf 'search     %s\n' "$"
            } \
            >>/etc/resolv.conf
            ;;

        use_old)

            # Restore the system DNS configuration.
            [[ ! -f "$TEMP_DNS" ]] && return

            print_cmd cp "$TEMP_DNS" /etc/resolv.conf
            print_cmd rm "$TEMP_DNS"
            ;;

        esac
    }

    # This function might or might not be needed depending on the init system.
    wait_for_init_system_to_start_network_interface()


    # This function returns a status of "0" (yes/true) or "1" (no/false), answering the question:
    is_there_another_wg_interface_using_this_namespace()
    :$/" '$2 ~ reg '))
        local                      line=''
        local                       key=''
        local -a                  value=()
        local      current_wg_interface=''

        # For each existing WG interface...
        for current_wg_interface in "$"
        do
            # Skip the interface that we are wanting to modify.
            [[ "$current_wg_interface" == "$WG_INTERFACE" ]] && continue

            # ...check if its config file is using the "wg_outgoing_namespace" namespace.
            while read -r line
            do
                # Remove comments.
                line="$(echo "$line" | grep -oE '^[^#]+')"

                key="$(echo "$line" | gawk '')"
                value=($(echo "$line" | gawk ''))

                # If another existing WG interface is using the "wg_outgoing_namespace" namespace, return true.
                [[ "$key" == "Namespace" && "$" == "$wg_outgoing_namespace" ]] && return 0

            done \
            </etc/wireguard/"$current_wg_interface".conf
        done

        # If we did not find an existing WG interface that is using the "wg_outgoing_namespace" namespace, return false.
        return 1
    }

    bring_wg_interface_up()


    bring_wg_interface_down()


    add_data_from_conf_file()
    ')"
            value=($(echo "$line" | gawk ''))

            case "$key" in
            Address)
                Wg_address+=($)
                ;;

            MTU)
                wg_mtu="$"
                ;;

            DNS)
                Wg_dns+=($)
                ;;

            Namespace)
                wg_outgoing_namespace="$"
                ;;

            PhysicalInterface)
                Wg_physical_interface+=($)
                ;;

            ExtraServiceYes)
                Extra_service_through_wg+=($)
                ;;

            ExtraServiceNo)
                Extra_service_through_no_wg+=($)
                ;;

            *)

                # This is building up a config file that the 'wg' command can use.
                wg_config_file_data_built_by_this_script+="$line"$'\n'
                ;;

            esac

        done \
        <"$WG_CONF_FILE"
    }

    check_data_before_running_this_script()


    ################
    # Script startup
    ################

    add_data_from_conf_file
    check_data_before_running_this_script

    case "$SELF_ACTION" in
    up)
        bring_wg_interface_up
        ;;

    down)
        bring_wg_interface_down
        ;;

    esac

`root `[`#`]`cat /usr/local/bin/wg-bypass`

    #!/bin/bash

    # /usr/local/bin/wg-bypass

    # Run a command in a specific network namespace.
    wg-bypass()


    wg-bypass "$@"

Set the correct permissions so that we can execute the files:

`root `[`#`]`chmod 755 /usr/local/bin/ `

##### [Configuration]

Now that we have all the files we need, we can begin using our custom values. We are mainly going to be modifying the [wg0.conf] file, but the [wg-netns] file can be edited too if needed. Regardless, each file contains comments that should explain why it does the things it does.

\
In the [wg0.conf] file, the only variables that need to be modified are:

-   PrivateKey
-   Address
-   PublicKey
-   PresharedKey (if used)
-   AllowedIPs (if we don\'t want to route all packets)
-   Endpoint

Everything else is either optional or already has a default value.

** Note**\
\

-   Some variables in [wg0.conf] can be modified in [wg-netns] to act as global defaults, but take note of which ones append data and which ones override data.
-   To avoid confusion with variables that don\'t need commas and ones that do, we use commas for all variables.

[FILE] **`wg0.conf`Example configuration**

    [Interface]
    PrivateKey = ecoetnhuastn0620757ostnhoausho
    Address = 123.123.123.123/32, a::cee:25/128, 222::666/128
    MTU = 1420
    DNS =
    Namespace = physical
    PhysicalInterface = eth0, wlan0, wlan1
    ExtraServiceYes = uwsgi.searxng, nginx.myotherwebsite
    ExtraServiceNo = nginx.mycoolwebsite

    [Peer]
    PublicKey = 0624204euoeu24424042thaoestuhuoeauh
    PresharedKey = oesutuh75757557tnuhoeasuthoeuseohu
    AllowedIPs = 10.0.20.0/24, 5555::/64
    Endpoint = my.dynamicdns.org:55333
    PersistentKeepAlive = 25

    [Peer]
    PublicKey = hhhhhhuhetuheteu062000206020620
    PresharedKey = 75357375thhthuteohuonuheoutoehuo
    AllowedIPs = 11.55.222.0/24, 1234::/64
    Endpoint = 173.10.3.5:61199

The [wg0.conf] file is basically a normal WireGuard configuration file with extra features.

\
Users that have [PAM](https://wiki.gentoo.org/wiki/PAM "PAM") enabled on their system might need to modify their PAM configuration file for OpenRC. By default, PAM will require authentication for each OpenRC command (even if the user is root). The [wg-netns] has multiple [rc-] commands in it; if PAM fails, the script will fail. To fix this, edit the [/etc/pam.d/run_init] file and add the line:

[CODE]

    auth sufficient pam_rootok.so

There should already be a message in this file with this exact line commented-out; simply uncomment the line, save, and exit. This change will make it so that we don\'t need to authenticate ourselves to PAM when we run an OpenRC command as root (being root is already enough).

\
Once we are done editing our [wg0.conf] file, we can bring up the WireGuard interface by running:

`root `[`#`]`wg-netns up wg0`

And bring it down by running:

`root `[`#`]`wg-netns down wg0`

We can check the status of the \"init\"/\"1\" namespace by running:

`user `[`$`]`ip address`

And the status of a specific namespace with:

`root `[`#`]`ip -n physical address`

To have an application bypass the WireGuard interface (such as LibreWolf):

`user `[`$`]`wg-bypass librewolf`

In this case, LibreWolf will not use the WireGuard interface until it closes and starts without [wg-bypass].

##### [][(Optional) Cron job]

To automatically start the WireGuard interface at system boot, we can set up a cron job to execute [wg-netns]. We will be using Fcron ([[[sys-process/fcron]](https://packages.gentoo.org/packages/sys-process/fcron)[]]) as our cron daemon.

** Important**\
If using a different cron daemon, ensure that the command only runs once!

Open the system crontab using fcrontab:

`root `[`#`]`fcrontab -u systab -e`

Add the following line:

[CODE]

    @runatreboot(true),runonce(true) 1 /usr/local/bin/wg-netns up wg0

Once we save and exit, the output should look similar to the following:

`root `[`#`]`fcrontab -u systab -e`

    0000-00-00 00:00:00 INFO fcrontab: editing systab's fcrontab
    Modifications will be taken into account right now.

** Important**\
If using SELinux, the contexts of some fcron files might need to be fixed; run the following command to fix them:

`root `[`#`]`restorecon -r /var/spool/fcron`

#### [NetworkManager]

Wireguard is officially supported by NetworkManager as of version 1.16^[\[1\]](#cite_note-1)^. Managing WireGuard is possible through the [nmcli] and [nmtui] commands. Review the [latest documentation upstream](https://networkmanager.dev/docs/api/latest/settings-wireguard.html) for the extensive list of key-value properties.

** Important**\
\* NetworkManager requires runtime dependencies (command-line interface tools) from the [[[net-vpn/wireguard-tools]](https://packages.gentoo.org/packages/net-vpn/wireguard-tools)[]] package in order to manage connection profiles. Be sure this package has been installed before attempting to use [nmcli] command.

-   In order for non-root users to edit network connections, each user must be [added to the plugdev group](https://wiki.gentoo.org/wiki/NetworkManager#User_permission "NetworkManager").

After creating a WireGuard configuration file (such as [wg0.conf]), the file can be imported into NetworkManager as a connection profile:

`user `[`$`]`nmcli connection import type wireguard file /path/to/wg0.conf`

After the configuration has been imported, the connection can be activated via:

`user `[`$`]`nmcli connection up wg0`

After adding a new connection, restart the interface by bringing it down, then back up up in a single command. Using the single command avoids disruption when working over the VPN connection itself:

`user `[`$`]`nmcli connection down wg0 && nmcli connection up wg0`

See the [NetworkManager](https://wiki.gentoo.org/wiki/NetworkManager "NetworkManager") article for more details on managing connection profiles.

## [Removal]

### [Unmerge]

To find Wireguard-related packages:

`root `[`#`]`emerge --ask --search wireguard`

To remove the userspace tools:

`root `[`#`]`emerge --ask --depclean --verbose net-vpn/wireguard-tools`

## [Troubleshooting]

### [Rebuilding modules on kernel upgrades for kernels less than 5.6]

When upgrading to a newer kernel that is less than version 5.6 (version 4.9.x LTS is a fitting example), it is important to re-emerge the Wireguard kernel modules. This is handled by default when using [[genkernel](https://wiki.gentoo.org/wiki/Genkernel "Genkernel")], but can be quickly performed using the following auto-generated Portage set:

`root `[`#`]`emerge --ask @module-rebuild`

## [See also]

-   [OpenVPN](https://wiki.gentoo.org/wiki/OpenVPN "OpenVPN") --- software that enables the creation of secure point-to-point or site-to-site connections.
-   [vpnc](https://wiki.gentoo.org/wiki/Vpnc "Vpnc") --- IPsec (Cisco/Juniper) VPN concentrator client

## [External resources]

-   [https://github.com/trailofbits/algo](https://github.com/trailofbits/algo) - A project with scripts to help setup a personal VPN server.
-   [http://lkml.iu.edu/hypermail/linux/kernel/1606.3/02833.html](http://lkml.iu.edu/hypermail/linux/kernel/1606.3/02833.html) - The initial Request for Comments post to the Kernel Mailing List.
-   [https://www.latacora.com/blog/2018/05/16/there-will-be/](https://www.latacora.com/blog/2018/05/16/there-will-be/) - A blog post complementing WireGuard.
-   [https://www.maketecheasier.com/set-up-wireguard-vpn-on-linux/](https://www.maketecheasier.com/set-up-wireguard-vpn-on-linux/) - How to Set Up Wireguard VPN for a Client and a Sever (e.g. for hosting a private game server for friends)

## [References]

1.  [[[↑](#cite_ref-1)] [[https://gitlab.freedesktop.org/NetworkManager/NetworkManager/blob/master/NEWS#L301-303](https://gitlab.freedesktop.org/NetworkManager/NetworkManager/blob/master/NEWS#L301-303)]]