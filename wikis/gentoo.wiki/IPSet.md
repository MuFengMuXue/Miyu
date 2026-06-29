**Resources**

[[]][Home](https://www.netfilter.org)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Netfilter#ipset "wikipedia:Netfilter")

*IPSet is used to set up, maintain and inspect so called IP sets in the Linux kernel. Depending on the type of the set, an IP set may store IP(v4/v6) addresses, (TCP/UDP) port numbers, IP and MAC address pairs, IP address and port number pairs, etc.* - Wikipedia

IPSet is a tool for [Iptables](https://wiki.gentoo.org/wiki/Iptables "Iptables"), successor of IPpool. It is an administration tool for IP sets which can be added to IPTables rules to filter out networks.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Prerequisites]](#Prerequisites)
    -   [[1.2] [Kernel]](#Kernel)
    -   [[1.3] [USE flags]](#USE_flags)
    -   [[1.4] [Emerge]](#Emerge)
-   [[2] [Filtering]](#Filtering)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Installation]

### [Prerequisites]

You will need to configure your kernel to support ipset.

### [Kernel]

For example, if ipset support is compiled as a module:

[KERNEL] **Kernel settings for ipset**

    [*] Networking support  --->
        Networking options  --->
        [*] Network packet filtering framework (Netfilter) --->
            <M>  IP set support --->

    as well as
                 Core Netfilter Configuration --->
                    <M>  set target and match support

then select the desired ipset types.

### [USE flags]

### [USE flags for] [net-firewall/ipset](https://packages.gentoo.org/packages/net-firewall/ipset) [[]] [IPset tool for iptables, successor to ippool]

  ----------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------
  [`+strip`](https://packages.gentoo.org/useflags/+strip)                       Allow symbol stripping to be performed by the ebuild for special files
  [`dist-kernel`](https://packages.gentoo.org/useflags/dist-kernel)             Enable subslot rebuilds on Distribution Kernel upgrades
  [`modules`](https://packages.gentoo.org/useflags/modules)                     Build the kernel modules
  [`modules-compress`](https://packages.gentoo.org/useflags/modules-compress)   Install compressed kernel modules (if kernel config enables module compression)
  [`modules-sign`](https://packages.gentoo.org/useflags/modules-sign)           Cryptographically sign installed kernel modules (requires CONFIG_MODULE_SIG=y in the kernel)
  ----------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-29 20:48] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install IPSet:

`root `[`#`]`emerge --ask net-firewall/ipset`

## [Filtering]

The simple following script can be used to filter IP addresses based on a file that have to be retrieved on the internet, and then create or update iptables firewall rules:

[FILE] **`~/scripts/ips.sh`Example IPSet script**

    #!/bin/sh
    opt="hash:net --hashsize 64"
    datadir=/var/lib/ipset
    target=https://feeds.dshield.org/block.txt
    set=IPBlock
    wget -qNO - $target > $datadir/$set || exit
    tmp=$-tmp
    ipset create $tmp $opt
    networks="$(grep -E '^[0-9]' $datadir/block.txt | sed -rne 's/(^([0-9]\.)[0-9]).*$/\1/p')"
    for i in $networks; do
        ipset add $tmp $/24
    done
    ipset create -exist $set $opt &&
    ipset swap $tmp $set &&
    ipset destroy $tmp &&
    echo "IPSet: $set updated"
    unset -v i networks opt set tmp

The above script is just a simple way to retrieve different or various IPSet table and make use of an up to date filtering.

The script creates a new table and swap and destroys a previous set if one exists. For a more refined script see the following examples:

-   [ips.bash](https://github.com/tokiclover/dotfiles/blob/master/bin/ips.bash) - [bash](https://wiki.gentoo.org/wiki/Bash "Bash") version
-   [ips.zsh](https://github.com/tokiclover/dotfiles/blob/master/bin/ips.zsh) - [zsh](https://wiki.gentoo.org/wiki/Zsh "Zsh") version

Save the rules to a file and start IPSet init service:

`root `[`#`]`/etc/init.d/ipset save`

`root `[`#`]`/etc/init.d/ipset start`

`root `[`#`]`rc-update add ipset boot`

The previous network filtering can be added to iptables with the following command:

`root `[`#`]`iptables -I INPUT -m set --match-set IPBlock src,dst -j Drop`

## [See also]

-   [Iptables](https://wiki.gentoo.org/wiki/Iptables "Iptables") --- a program used to configure and manage the kernel\'s netfilter modules.

## [External resources]

-   [Forum thread](https://forums.gentoo.org/viewtopic-t-863121.html)