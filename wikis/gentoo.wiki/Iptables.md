Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Iptables/hu "Iptables (14% translated)")

**Resources**

[[]][Home](https://www.netfilter.org/projects/iptables)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Netfilter#iptables "wikipedia:Netfilter")

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/iptables)

[iptables] is a program used to configure and manage the kernel\'s netfilter modules. It should be replaced with its successor [nftables](https://wiki.gentoo.org/wiki/Nftables "Nftables").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Prerequisites]](#Prerequisites)
    -   [[1.2] [Kernel]](#Kernel)
        -   [[1.2.1] [Client]](#Client)
        -   [[1.2.2] [Router]](#Router)
    -   [[1.3] [USE flags]](#USE_flags)
    -   [[1.4] [Emerge]](#Emerge)
-   [[2] [Firewall]](#Firewall)
    -   [[2.1] [First run]](#First_run)
        -   [[2.1.1] [IPv4]](#IPv4)
        -   [[2.1.2] [IPv6]](#IPv6)
    -   [[2.2] [General rules]](#General_rules)
    -   [[2.3] [Stateless firewall]](#Stateless_firewall)
    -   [[2.4] [Stateful firewall]](#Stateful_firewall)
    -   [[2.5] [GeoIP country blocking rules]](#GeoIP_country_blocking_rules)
    -   [[2.6] [Generating firewall rules]](#Generating_firewall_rules)
        -   [[2.6.1] [Generating firewall rules for client]](#Generating_firewall_rules_for_client)
        -   [[2.6.2] [Generating firewall rules for server]](#Generating_firewall_rules_for_server)
-   [[3] [Show firewall rules and status]](#Show_firewall_rules_and_status)
    -   [[3.1] [IPv4]](#IPv4_2)
    -   [[3.2] [IPv6]](#IPv6_2)
-   [[4] [Migration to nftables]](#Migration_to_nftables)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [Installation]

### [Prerequisites]

First off, configure the kernel with netfilter support. To allow adding rules based on IP filtering like black listing IP addresses based on a live feed [\[1\]](https://forums.gentoo.org/viewtopic-t-863121.html), do not forget to add [IPSet](https://wiki.gentoo.org/wiki/IPSet "IPSet") support to the kernel and merge the [[[net-firewall/ipset]](https://packages.gentoo.org/packages/net-firewall/ipset)[]] package.

### [Kernel]

Kernel configuration required by [iptables] depends on the intended use case.

#### [Client]

For client computers some basic options need to be activated in the kernel. This configuration does not provide network address translation or any other high sophisticated features. In \"Network packet filtering framework\" only the tables \"filter\" are needed with connection tracking support and with `REJECT` target support.

[KERNEL] **Kernel settings for client**

    [*] Networking support  --->
        Networking options  --->
            ...
            [*] TCP/IP networking
            [ ]   IP: multicasting
            [ ]   IP: advanced router
            [ ]   IP: kernel level autoconfiguration
            < >   IP: tunneling
            < >   IP: GRE demultiplexer
            [ ]   IP: TCP syncookie support
            <*>   Virtual (secure) IP: tunneling
            < >   IP: AH transformation
            < >   IP: ESP transformation
            < >   IP: IPComp transformation
            <*>   IP: IPsec transport mode (obsolete in kernel 5.4)
            <*>   IP: IPsec tunnel mode (obsolete in kernel 5.4)
            < >   IP: IPsec BEET mode (obsolete in kernel 5.4)
            < >   Large Receive Offload (ipv4/tcp)
            <*>   INET: socket monitoring interface
            < >     UDP: socket monitoring interface
            [ ]   TCP: advanced congestion control  ----
            [ ]   TCP: MD5 Signature Option support (RFC2385)
            <*>   The IPv6 protocol  --->
            [ ] Security Marking
            [ ] Timestamping in PHY devices
            [*] Network packet filtering framework (Netfilter)  --->
                --- Network packet filtering framework (Netfilter)
                [ ]   Network packet filtering debugging
                [ ]   Advanced netfilter configuration
                      Core Netfilter Configuration  --->
                          <M> Netfilter LOG over NFNETLINK interface
                          <*> Netfilter connection tracking support
                          [ ]   Supply CT list in procfs (OBSOLETE)
                          < >   FTP protocol support
                          < >   IRC protocol support
                          < >   NetBIOS name service protocol support
                          < >   SIP protocol support
                          < >   Connection tracking netlink interface
                          < > Netfilter nf_tables support
                          -*- Netfilter Xtables support (required for ip_tables)
                                *** Xtables combined modules ***
                          < >   nfmark target and match support
                                *** Xtables targets ***
                          < >   LOG target support
                          < >   "NFLOG" target support
                          < >   "TCPMSS" target support
                                *** Xtables matches ***
                          <*>   "conntrack" connection tracking match support
                          < >   IPsec "policy" match support
                          < >   "state" match support
                < >   IP set support  ----
                < >   IP virtual server support  ----
                      IP: Netfilter Configuration  --->
                          <*> IPv4 connection tracking support (required for NAT)
                          <*> IP tables support (required for filtering/masq/NAT)
                          <*>   Packet filtering
                          <*>     REJECT target support
                          < >   ULOG target support (obsolete)
                          < >   IPv4 NAT
                          < >   Packet mangling
                          < >   raw table support (required for NOTRACK/TRACE)
                      IPv6: Netfilter Configuration  --->
                          <*> IPv6 connection tracking support
                          <*> IP6 tables support (required for filtering)
                          < >   "ipv6header" IPv6 Extension Headers Match
                          <*>   Packet filtering
                          <*>     REJECT target support
                          < >   Packet mangling
                          < >   raw table support (required for TRACE)

#### [Router]

Activate the following kernel options:

[KERNEL] **Kernel settings for router**

    [*] Networking support  --->
        Networking options  --->
            [*] TCP/IP networking
            [*]   IP: multicasting
            [*]   IP: advanced router
            ...
            [*]   IP: ARP daemon support
            [*]   IP: TCP syncookie support
            <M>   IP: AH transformation
            <M>   IP: ESP transformation
            <M>   IP: IPComp transformation
            <M>   IP: IPsec transport mode (obsolete in kernel 5.4)
            <M>   IP: IPsec tunnel mode (obsolete in kernel 5.4)
            <M>   IP: IPsec BEET mode (obsolete in kernel 5.4)
            <*>   Large Receive Offload (ipv4/tcp)
            <*>   INET: socket monitoring interface
            <M>     UDP: socket monitoring interface
            [ ]   TCP: advanced congestion control  --->
            ...
            <M>   The IPv6 protocol  --->
            ...
            [*] Network packet filtering framework (Netfilter)  --->
                [*]   Advanced netfilter configuration
                Core Netfilter Configuration  --->
                    <M>   "addrtype" address type match support
                    <M>   "comment" match support
                    <M>   "hl" hoplimit/TTL match support
                    <M>   "limit" match support
                    <M>   "multiport" Multiple port match support
                    <M>   "recent" match support

One can setup the IPv6 support category as modular (*\<M\>*) to be safe and enable almost all Netfilter sub-categories as well. Or, enable only what is needed and leave the other modules unset. A number of settings are almost always needed:

-   *IP virtual server support* core components (scheduler are certainly optional)
-   *IP: Netfilter Configuration* support
-   *IPv6: Netfilter Configuration* for IPv6 support
-   *IP set support* for IP filtering based on IP, MAC, ports
-   pick up what is needed in *Core Netfilter Configuration* with at least:
    -   Netfilter: NFQEUE, LOG;
    -   Connection tracking: flow, mark, events, netlink;
    -   Netfilter Xtables: NFQEUE, LOG, conn, state helper with Xtables match: conn\...

[KERNEL]

    [*] Networking support  --->
        Networking options  --->
            [*] Network packet filtering framework (Netfilter)  --->
                --- Network packet filtering framework (Netfilter)
                [ ]   Network packet filtering debugging
                [*]   Advanced netfilter configuration
                [*]     Bridged IP/ARP packets filtering
                        Core Netfilter Configuration  --->
                <M>   IP set support  --->
                <M>   IP virtual server support  --->
                      IP: Netfilter Configuration  --->
                      IPv6: Netfilter Configuration  --->
                      DECnet: Netfilter Configuration  --->
                <M>   Ethernet Bridge tables (ebtables) support  --->

### [USE flags]

### [USE flags for] [net-firewall/iptables](https://packages.gentoo.org/packages/net-firewall/iptables) [[]] [Linux kernel (2.4+) firewall, NAT and packet mangling tools]

  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`conntrack`](https://packages.gentoo.org/useflags/conntrack)       Build against net-libs/libnetfilter_conntrack when enables the connlabel matcher
  [`netlink`](https://packages.gentoo.org/useflags/netlink)           Build against libnfnetlink which enables the nfnl_osf util
  [`nftables`](https://packages.gentoo.org/useflags/nftables)         Support nftables kernel interface
  [`pcap`](https://packages.gentoo.org/useflags/pcap)                 Build against net-libs/libpcap which enables the nfbpf_compile util
  [`static-libs`](https://packages.gentoo.org/useflags/static-libs)   Build static versions of dynamic libraries as well
  [`test`](https://packages.gentoo.org/useflags/test)                 Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)     Verify upstream signatures on distfiles
  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-05 07:37] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install iptables:

`root `[`#`]`emerge --ask net-firewall/iptables`

## [Firewall]

### [First run]

For some services such as [sshguard](https://wiki.gentoo.org/wiki/Sshguard "Sshguard") and [fail2ban](https://wiki.gentoo.org/wiki/Fail2ban "Fail2ban") a running firewall is mandatory. First save a blank firewall rule set and start the firewall.

#### [IPv4]

`root `[`#`]`rc-service iptables save `

`root `[`#`]`rc-service iptables start `

To start on boot:

`root `[`#`]`rc-update add iptables default`

#### [IPv6]

`root `[`#`]`rc-service ip6tables save `

`root `[`#`]`rc-service ip6tables start `

To start on reboot:

`root `[`#`]`rc-update add ip6tables default`

### [General rules]

To create firewall rules, the [iptables] or [ip6tables] commands in the next set of examples will be defined through `ipt=$(type -p iptables)` or `ipt=$(type -p ip6tables)`. As these commands are deprecated in favor of [Nftables](https://wiki.gentoo.org/wiki/Nftables "Nftables") and the [nft] command, by default both are symlinks to [xtables-legacy-multi]; the symlink target can be specified via [eselect iptables].

When the rules are saved, they are usually stored in [/var/lib/iptables/rules-save] or [/var/lib/ip6tables/rules-save]. This allows the firewall service to reload the rules at boot time.

Let\'s begin with a little example:

`root `[`#`]`"$ipt" -P INPUT DROP`

This will implement a fairly strong firewall: it will drop every packet that will be sent to the host (as this matches the INPUT chain).

The following examples show how firewall rules are further generated.

### [Stateless firewall]

Traditional firewalls use stateless firewall rules like so:

`root `[`#`]`"$ipt" -A INPUT --dport 80 -j ACCEPT`

That simply allows the local port 80 to accept traffic (`--dport` configures the destination port), which usually implies HTTP servers as those generally listen on port 80).

### [Stateful firewall]

In a stateful firewall approach, the previous example would be handled like so:

`root `[`#`]`"$ipt" -P INPUT DROP `

`root `[`#`]`"$ipt" -A INPUT -i eth0 -p tcp --dport 80 --syn -m conntrack --ctstate NEW -j ACCEPT `

`root `[`#`]`"$ipt" -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT `

By default, everything will be dropped like a hot potato. However, incoming traffic might be accepted based on the connection state of the packets (starting with NEW and further allowing all established/related traffic). Performance-wise, it would even be better to place the last line before the second to avoid going into complicated filtering chains for already related and established connections.

This is how a stateful firewall operates to avoid opening unneeded holes and accept in/outbound packets based on the state of the packets.

### [GeoIP country blocking rules]

This approach allows matching packets based on source or destination geographic location. Entire countries can be matched for logging or traffic can be dropped entirely.

Install the Xtables addon for iptables:

`root `[`#`]`emerge -a net-firewall/xtables-addons`

Download the GeoIP database:

`root `[`#`]`mkdir /root/geoip`

`root `[`#`]`cd /root/geoip`

`root `[`#`]`/lib64/xtables-addons/xt_geoip_dl`

Convert the GeoIP csv file to packed format for xt_geoip:

`root `[`#`]`mkdir -p /usr/share/xt_geoip`

`root `[`#`]`/lib64/xtables-addons/xt_geoip_build -D /usr/share/xt_geoip`

Identify an IP address for testing purposes. One method is to `nslookup example.com` then `whois example.com` to verify the IPv4 address is in the desired country. Ping the address to verify it responds, then add the following rules to verify they are matching the desired country and working as expected:

    # block INPUT if IPv4 matches
    # note that -I will insert the rule at the beginning of the chain, applying it first
    iptables -I INPUT -m geoip -i eth0 --src-cc BY,RU -j DROP
    iptables -I INPUT -m geoip -i eth0 --dst-cc BY,RU -j DROP
    # block FORWARD if IPv4 matches src or dst address
    # note that -I will insert the rule at the beginning of the chain, applying it first
    iptables -I FORWARD -m geoip -i eth0 --src-cc BY,RU -j DROP
    iptables -I FORWARD -m geoip -i eth0 --dst-cc BY,RU -j DROP

### [Generating firewall rules]

#### [Generating firewall rules for client]

A script as simple as shown below should be sufficient for most client computers. Store it in a safe place such as [\~/firewall]. It is only needed for first-time initialization of the firewall rules.

[CODE] **Simple firewall script for a workstation**

    #!/bin/bash

    iptables -F
    iptables -X
    iptables -Z

    iptables -P INPUT DROP
    iptables -P FORWARD DROP
    iptables -P OUTPUT ACCEPT

    iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
    iptables -A INPUT -i lo -j ACCEPT
    iptables -A INPUT -p icmp --icmp-type 3 -j ACCEPT
    iptables -A INPUT -p icmp --icmp-type 11 -j ACCEPT
    iptables -A INPUT -p icmp --icmp-type 12 -j ACCEPT
    iptables -A INPUT -p tcp --syn --dport 113 -j REJECT --reject-with tcp-reset

    ip6tables -F
    ip6tables -X
    ip6tables -Z

    ip6tables -P INPUT DROP
    ip6tables -P FORWARD DROP
    ip6tables -P OUTPUT ACCEPT

    ip6tables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
    ip6tables -A INPUT -i lo -j ACCEPT
    ip6tables -A INPUT -m conntrack --ctstate INVALID -j DROP
    ip6tables -A INPUT -p ipv6-icmp -j ACCEPT
    ip6tables -A INPUT -p udp -m conntrack --ctstate NEW -j REJECT --reject-with icmp6-port-unreachable
    ip6tables -A INPUT -p tcp -m tcp --tcp-flags FIN,SYN,RST,ACK SYN -m conntrack --ctstate NEW -j REJECT --reject-with tcp-reset

An example of a more sophisticated rule set with logging is shown in [this forum discussion](https://forums.gentoo.org/viewtopic-p-7578926.html#7578926).

#### [Generating firewall rules for server]

This section will try to build up your above script with a set of rules for common external-facing services. Append these to [\~/firewall].

I highly recommend adding ssh rules below if you are working on a remote server through ssh.

[CODE] **Some more rules**

    # Allow ssh
    iptables -A INPUT -p TCP --dport ssh -j ACCEPT
    ip6tables -A INPUT -p TCP --dport ssh -j ACCEPT
    # Allow webserver
    iptables -A INPUT -p TCP --dport http -j ACCEPT
    ip6tables -A INPUT -p TCP --dport http -j ACCEPT
    # Allow ftp
    iptables -A INPUT -p TCP --dport ftp -j ACCEPT
    ip6tables -A INPUT -p TCP --dport ftp -j ACCEPT
    # Mailserver
    iptables -A INPUT -p TCP --dport 143 -j ACCEPT
    ip6tables -A INPUT -p TCP --dport 143 -j ACCEPT
    iptables -A INPUT -p TCP --dport 110 -j REJECT
    ip6tables -A INPUT -p TCP --dport 110 -j REJECT
    iptables -A INPUT -p TCP --dport 195 -j ACCEPT
    ip6tables -A INPUT -p TCP --dport 195 -j ACCEPT
    iptables -A INPUT -p TCP --dport 443 -j ACCEPT
    ip6tables -A INPUT -p TCP --dport 443 -j ACCEPT
    iptables -A INPUT -p TCP --dport 465 -j ACCEPT
    ip6tables -A INPUT -p TCP --dport 465 -j ACCEPT
    iptables -A INPUT -p TCP --dport 587 -j ACCEPT
    ip6tables -A INPUT -p TCP --dport 587 -j ACCEPT
    iptables -A INPUT -p TCP --dport 873 -j ACCEPT
    ip6tables -A INPUT -p TCP --dport 873 -j ACCEPT
    iptables -A INPUT -p TCP --dport 943 -j ACCEPT
    ip6tables -A INPUT -p TCP --dport 943 -j ACCEPT
    iptables -A INPUT -p TCP --dport 993 -j ACCEPT
    ip6tables -A INPUT -p TCP --dport 993 -j ACCEPT

    iptables -A INPUT -p TCP --dport 631 -j ACCEPT
    ip6tables -A INPUT -p TCP --dport 631 -j ACCEPT
    iptables -A INPUT -p TCP --dport 111 -j ACCEPT
    ip6tables -A INPUT -p TCP --dport 111 -j ACCEPT
    iptables -A INPUT -p TCP --dport 25 -j ACCEPT
    ip6tables -A INPUT -p TCP --dport 25 -j ACCEPT

    # DNS server
    iptables -A INPUT -p udp --dport 53 -j ACCEPT
    ip6tables -A INPUT -p udp --dport 53 -j ACCEPT
    iptables -A INPUT -p tcp --sport 53 -j ACCEPT
    ip6tables -A INPUT -p tcp --sport 53 -j ACCEPT

After saving your desired firewall rules.

`root `[`#`]`chmod 744 ~/firewall `

`root `[`#`]`~/firewall `

This will load your firewall rules into [iptables] and [ip6tables].

`root `[`#`]`/etc/init.d/iptables save `

`root `[`#`]`/etc/init.d/ip6tables save `

Will save your [iptables] and [ip6tables] so they are available the next time iptables service is loaded.

`root `[`#`]`rc-service iptables start `

`root `[`#`]`rc-service ip6tables start `

`root `[`#`]`rc-update add iptables default `

`root `[`#`]`rc-update add ip6tables default `

If you need to add a rule. Run it in the command prompt (like individual rules in [\~/firewall]).

Also add it to [\~/firewall] if you are sure if you ever reset your firewall, you want those settings back in.

Once satisfied run:

`root `[`#`]`/etc/init.d/iptables save `

`root `[`#`]`/etc/init.d/ip6tables save `

Also. If anything ever goes drastically wrong. You may reset your firewall settings by running [\~/firewall], proceeded by the above save.

## [Show firewall rules and status]

### [IPv4]

`root `[`#`]`iptables -L -n`

Print all rules (similar to [iptables-save])ː

`root `[`#`]`iptables -S`

Like every other [iptables] command, it applies to the specified table (of which `filter` is the default), so NAT rules get listed byː

`root `[`#`]`iptables -t nat -L -n `

`root `[`#`]`iptables -t nat -S `

### [IPv6]

`root `[`#`]`ip6tables -L -n`

Print all rules (similar to [ip6tables-save])ː

`root `[`#`]`ip6tables -S`

Like every other [ip6tables] command, it applies to the specified table (of which `filter` is the default), so NAT rules get listed byː

`root `[`#`]`ip6tables -t nat -L -n `

`root `[`#`]`ip6tables -t nat -S `

## [Migration to nftables]

** Warning**\
Depending on the active iptables rules **adding** nftables rules breaks networking completely. Especially masquerading of iptables is incompatible with nftables. Review the translated rules thoroughly before replacing iptables rules with the nftables variant.

All tools to export and translate to nftables are part of the iptables package. The migration requires the following steps in general^[\[1\]](#cite_note-1)^:

1.  emerge iptables with USE flag nftables to add necessary tools
2.  export iptables rules to a file
3.  translate exported iptables rules to nftables rules
4.  replace iptables with nftables

`root `[`#`]`iptables-save > iptables-rules.txt`

`root `[`#`]`iptables-restore-translate -f iptables-rules.txt >nftables-rules.txt`

`root `[`#`]`cat nftables-rules.txt`

`root `[`#`]`nft -c -f nftables-rules.txt `

If you are certain that the machine will either revert to iptables in case of errors or work correctly with the translated nftables rules:

`root `[`#`]`/etc/init.d/iptables stop `

`root `[`#`]`nft -f nftables-rules.txt `

`root `[`#`]`/etc/init.d/nftables start `

Third party tools, e.g. [[[net-firewall/ufw]](https://packages.gentoo.org/packages/net-firewall/ufw)[]], do not support nftables and will call iptables by default. In many such cases, it doesn\'t seem possible to dispose of iptables, at least at the moment.

If iptables has been installed with the flag **nftables**, it is possible to use:

`root `[`#`]`eselect iptables set xtables-nft-multi`

This will forward every call to `iptables` to `iptables-nft`, a translation layer that will operate transparently for the calling application.

[Raspberry Pi](https://wiki.gentoo.org/wiki/Raspberry_Pi "Raspberry Pi") users will probably need to follow this procedure when using kernel 6.18.y with [[[net-firewall/ufw]](https://packages.gentoo.org/packages/net-firewall/ufw)[]].

## [See also]

-   [iptables (Security Handbook)](https://wiki.gentoo.org/wiki/Security_Handbook/Firewalls_and_Network_Security#iptables "Security Handbook/Firewalls and Network Security")
-   [nftables](https://wiki.gentoo.org/wiki/Nftables "Nftables") --- the successor to [[iptables]].

## [External resources]

-   [Linux Firewalls Using iptables](http://borg.uu3.net/iptables/iptables-intro.html)
-   [Forums posting with ip6tables -A INPUT -s fe80::/10 -p ipv6-icmp -j ACCEPT](https://forums.gentoo.org/viewtopic-p-7654940.html#7654940)
-   [firewall-mv](https://cgit.gentoo.org/user/mv.git/tree/net-firewall/firewall-mv)
-   [IPv6](https://en.wikipedia.org/wiki/IPv6 "wikipedia:IPv6")

## [References]

1.  [[[↑](#cite_ref-1)] [[https://wiki.nftables.org/wiki-nftables/index.php/Moving_from_iptables_to_nftables](https://wiki.nftables.org/wiki-nftables/index.php/Moving_from_iptables_to_nftables)]]