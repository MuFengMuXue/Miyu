This page contains [[changes](https://wiki.gentoo.org/index.php?title=Nftables&oldid=1403558&diff=1417871)] which are not marked for translation.

Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Nftables/hu "Nftables (3% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Nftables/ja "nftables (100% translated)")

**Resources**

[[]][Home](https://netfilter.org/)

[[]][GitWeb](https://git.netfilter.org/nftables)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Nftables "wikipedia:Nftables")

[[]][Official documentation](https://wiki.nftables.org/wiki-nftables/)

[[]][Bugs (upstream)](https://bugzilla.netfilter.org/)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/nftables)

[[]][[#netfilter](ircs://irc.libera.chat/#netfilter)] ([[webchat](https://web.libera.chat/#netfilter)])

**nftables** is the successor to [[iptables](https://wiki.gentoo.org/wiki/Iptables "Iptables")]. It replaces the existing [iptables], [ip6tables], [arptables], and [ebtables] framework. It uses the Linux [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") and a new userspace utility called [nft]. nftables provides a compatibility layer for the [iptables]/[ip6tables] and framework.

## Contents

-   [[1] [Introduction]](#Introduction)
    -   [[1.1] [Tables]](#Tables)
    -   [[1.2] [Chains]](#Chains)
        -   [[1.2.1] [IPv4/IPv6/INET/Bridge hooks]](#IPv4.2FIPv6.2FINET.2FBridge_hooks)
        -   [[1.2.2] [ARP hooks]](#ARP_hooks)
        -   [[1.2.3] [Netdev hooks]](#Netdev_hooks)
    -   [[1.3] [Rules]](#Rules)
        -   [[1.3.1] [Matches]](#Matches)
        -   [[1.3.2] [Statements]](#Statements)
    -   [[1.4] [Sets]](#Sets)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
    -   [[2.2] [USE flags]](#USE_flags)
    -   [[2.3] [Emerge]](#Emerge)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [OpenRC]](#OpenRC)
    -   [[3.2] [systemd]](#systemd)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [Tables]](#Tables_2)
        -   [[4.1.1] [Creating tables]](#Creating_tables)
        -   [[4.1.2] [Listing tables]](#Listing_tables)
        -   [[4.1.3] [Deleting tables]](#Deleting_tables)
    -   [[4.2] [Chains]](#Chains_2)
        -   [[4.2.1] [Adding chains]](#Adding_chains)
        -   [[4.2.2] [Listing chain rules]](#Listing_chain_rules)
        -   [[4.2.3] [Deleting chains]](#Deleting_chains)
    -   [[4.3] [Rules]](#Rules_2)
        -   [[4.3.1] [Adding rules]](#Adding_rules)
        -   [[4.3.2] [Listing all rules]](#Listing_all_rules)
        -   [[4.3.3] [Deleting rules]](#Deleting_rules)
-   [[5] [Modular Ruleset Management]](#Modular_Ruleset_Management)
    -   [[5.1] [Example Modules]](#Example_Modules)
        -   [[5.1.1] [Variable definitions]](#Variable_definitions)
        -   [[5.1.2] [Jumping to the ingress filter]](#Jumping_to_the_ingress_filter)
        -   [[5.1.3] [Basic drop filter]](#Basic_drop_filter)
        -   [[5.1.4] [Basic ICMP filter]](#Basic_ICMP_filter)
        -   [[5.1.5] [Allow DHCP traffic]](#Allow_DHCP_traffic)
        -   [[5.1.6] [Allow inbound and forwarded SSH traffic]](#Allow_inbound_and_forwarded_SSH_traffic)
        -   [[5.1.7] [Allow outbound and forwarded NTP traffic]](#Allow_outbound_and_forwarded_NTP_traffic)
        -   [[5.1.8] [NAT LANs]](#NAT_LANs)
        -   [[5.1.9] [Masquerade Docker Traffic]](#Masquerade_Docker_Traffic)
-   [[6] [Logging]](#Logging)
    -   [[6.1] [Log action]](#Log_action)
    -   [[6.2] [syslog-ng nftables configuration]](#syslog-ng_nftables_configuration)
-   [[7] [Examples]](#Examples)
-   [[8] [Troubleshooting]](#Troubleshooting)
    -   [[8.1] [No such file or directory]](#No_such_file_or_directory)
    -   [[8.2] [Conflicting intervals]](#Conflicting_intervals)
    -   [[8.3] [Connections blocked after nftables restart or reboot]](#Connections_blocked_after_nftables_restart_or_reboot)
    -   [[8.4] [Family netdev and ingress hook]](#Family_netdev_and_ingress_hook)
-   [[9] [See also]](#See_also)
-   [[10] [External Resources]](#External_Resources)
-   [[11] [References]](#References)

## [Introduction]

As with the iptables framework, nftables is built upon rules which specify actions. These rules are attached to chains. A chain can contain a collection of rules and is registered in the netfilter hooks. Chains are stored inside tables. A table is specific for one of the layer 3 protocols. One of the main differences with iptables is that there are no predefined tables and chains anymore.

[CODE] **Configuration hierarchy**

    Table
    ├─Chain1
    │ ├─Rule1a
    │ └─Rule1b
    ├─Chain2
    │ ├─Rule2a
    │ ├─Rule2b
    │ └─Rule2c
    └─Chain3
      └─Rule3a

** Note**\
Both [iptables](https://wiki.gentoo.org/wiki/Iptables "Iptables") and nftables use the [Netfilter framework](https://en.wikipedia.org/wiki/Netfilter#/media/File:Netfilter-packet-flow.svg). Because iptables does not allow for the manual configuration of hooks - the default tables are used for tapping into the Netfilter framework, while nftables requires the hooks to be defined inside of user-defined chains. Iptables also does not support dual stack (**inet**) configurations or **netdev**. Other than these differences, they are functionally identical, acting as interfaces for **Netfilter**.

### [Tables]

A table is a container for chains. Unlike [iptables](https://wiki.gentoo.org/wiki/Iptables "Iptables"), nftables has no predefined tables (filter, raw, mangle\...). An iptables-like structure can be used, but this is not required. Tables must be defined with an `address family` and `name`, which can be anything.

The `address families` used by [nftables] are documented under [man nft 8]:

  ---------------- ---------------------------------------------------------------------
  Address family   Description
  **ip**           Used for IPv4 related chains.
  **ip6**          Used for IPv6 related chains.
  **inet**         Mixed IPv4/IPv6 chains (kernel 3.14 and up).
  **arp**          Used for ARP related chains.
  **bridge**       Used for bridging related chains.
  **netdev**       Used for chains that filter early in the stack (kernel 4.2 and up).
  ---------------- ---------------------------------------------------------------------

** Note**\
If a family is not specified, **ip** is used.

### [Chains]

Chains are used to group rules. As with the tables, nftables does not have any predefined chains. Chains are grouped in **base** and **non-base** types. Base chains are registered in one of the netfilter hooks, non-base chains are not. **base chain**s must be defined with a `hook` type, and `priority`. In contrast, **non-base chains** are not attached to a hook and they don\'t see any traffic by default. They can be used as jump targets to arrange a rule-set in a tree of chains.

The `chains` used by [nftables] are documented under [man nft 8]:

  ------------ -------------------------- -------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------
  Chain        Families                   Hooks                                                    Description
  **filter**   **all**                    **all**                                                  Standard chain, generally used for filtering.
  **nat**      **ip**, **ip6**, **nat**   **prerouting**, **input**, **output**, **postrouting**   Used to perform Native Address Translation using conntrack. Only the first packet of a connection uses this chain.
  **route**    **ip**, **ip6**            **output**                                               Packets that traverse this chain type, if about to be accepted, trigger a route lookup if the IP header has changed.
  ------------ -------------------------- -------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------

Each address family has different hook capabilities, defined under the respective ` ADDRESS FAMILY` section of [man nft 8]:

#### [][IPv4/IPv6/INET/Bridge hooks]

  -------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------
  Hook                       Description
  **prerouting**             Processes all packets entering the system, invoked before the routing process, used for early filtering or changing attributes which would affect routing.
  **input**                  Processes packets destined for the local system.
  **forward**                Processes packets received by the local system, but destined for another one.
  **output**                 Processes packets sent by the local system (includes NATed packets).
  **postrouting**            Processes all packets leaving the system, regardless of the source.
  **ingress** (Since 5.10)   Processes all packets entering the system, before **prerouting** (and all other layer 3 handlers). Only available to the **inet** `address family`.
  -------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------

#### [ARP hooks]

  ------------ --------------------------------------------------
  Hook         Description
  **input**    Processes ARP packets the local system receives.
  **output**   Processes ARP packets leaving the local system.
  ------------ --------------------------------------------------

#### [Netdev hooks]

  ------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Hook          Description
  **ingress**   Processes all packets entering the system. Invoked after network taps such as [tcpdump](https://wiki.gentoo.org/wiki/Tcpdump "Tcpdump"), and before layer 3 handlers.
  **egress**    Processes all packets leaving the system. Invoked before [tcpdump](https://wiki.gentoo.org/wiki/Tcpdump "Tcpdump") egress.
  ------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Rules]

**Rules** specify what action is taken for a given packet. **Rules** are attached to **chains**. Each **rule** can have an expression to match packets and one or more actions to perform when matching. Unlike iptables, it is possible to specify multiple actions per **rule**, and counters are off by default. A **counter** must be specified explicitly in each rule for which packet- and byte-counters are desired.

Each rule has a unique handle number by which it can be distinguished.

The following matches are available:

-   **ip**: IP protocol.
-   **ip6**: IPv6 protocol.
-   **tcp**: TCP protocol.
-   **udp**: UDP protocol.
-   **udplite**: UDP-lite protocol.
-   **sctp**: SCTP protocol.
-   **dccp**: DCCP protocol.
-   **ah**: Authentication headers.
-   **esp**: Encrypted security payload headers.
-   **ipcomp**: IPcomp headers.
-   **icmp**: icmp protocol.
-   **icmpv6**: icmpv6 protocol.
-   **ct**: Connection tracking.
-   **meta**: meta properties such as interfaces.

#### [Matches]

  ------------- ------------ ---------------------------------------------------------------
  Match         Arguments    Description/Example
  **ip**        version      Ip Header version
                hdrlength    IP header length
                tos          Type of Service
                length       Total packet length
                id           IP ID
                frag-off     Fragmentation offset
                ttl          Time to live
                protocol     Upper layer protocol
                checksum     IP header checksum
                saddr        Source address
                daddr        Destination address
  **ip6**       version      IP header version
                priority
                flowlabel    Flow label
                length       Payload length
                nexthdr      Next header type (Upper layer protocol number)
                hoplimit     Hop limit
                saddr        Source Address
                daddr        Destination Address
  **tcp**       sport        Source port
                dport        Destination port
                sequence     Sequence number
                ackseq       Acknowledgement number
                doff         Data offset
                flags        TCP flags
                window       Window
                checksum     Checksum
                urgptr       Urgent pointer
  **udp**       sport        Source port
                dport        destination port
                length       Total packet length
                checksum     Checksum
  **udplite**   sport        Source port
                dport        destination port
                cscov        Checksum coverage
                checksum     Checksum
  **sctp**      sport        Source port
                dport        destination port
                vtag         Verification tag
                checksum     Checksum
  **dccp**      sport        Source port
                dport        destination port
  **ah**        nexthdr      Next header protocol (Upper layer protocol)
                hdrlength    AH header length
                spi          Security Parameter Index
                sequence     Sequence Number
  **esp**       spi          Security Parameter Index
                sequence     Sequence Number
  **ipcomp**    nexthdr      Next header protocol (Upper layer protocol)
                flags        Flags
                cfi          Compression Parameter Index
  **icmp**      type         icmp packet type
  **icmpv6**    type         icmpv6 packet type
  **ct**        state        State of the connection
                direction    Direction of the packet relative to the connection
                status       Status of the connection
                mark         Connection mark
                expiration   Connection expiration time
                helper       Helper associated with the connection
                l3proto      Layer 3 protocol of the connection
                saddr        Source address of the connection for the given direction
                daddr        Destination address of the connection for the given direction
                protocol     Layer 4 protocol of the connection for the given direction
                proto-src    Layer 4 protocol source for the given direction
                proto-dst    Layer 4 protocol destination for the given direction
  **meta**      length       Length of the packet in bytes: *meta length \> 1000*
                protocol     ethertype protocol: *meta protocol vlan*
                priority     TC packet priority
                mark         Packet mark
                iif          Input interface index
                iifname      Input interface name
                iiftype      Input interface type
                oif          Output interface index
                oifname      Output interface name
                oiftype      Output interface hardware type
                pkttype      Packet type: unicast, multicast or broadcast
                skuid        UID associated with originating socket
                skgid        GID associated with originating socket
                rtclassid    Routing realm
  ------------- ------------ ---------------------------------------------------------------

#### [Statements]

Statements represent the action to be performed when a rule matches. They exist in two kinds: Terminal statements, unconditionally terminate the evaluation of the current rules and non-terminal statements that either conditionally or never terminate the current rules. There can be an arbitrary amount of non-terminal statements, but there must be only a single terminal statement. The terminal statements can be:

-   **accept**: Accept the packet and stop the ruleset evaluation.
-   **drop**: Drop the packet and stop the ruleset evaluation.
-   **reject**: Reject the packet with an icmp message.
-   **queue**: Queue the packet to userspace and stop the ruleset evaluation.
-   **continue**:
-   **return**: Return from the current chain and continue at the next rule of the last chain. In a base chain it is equivalent to accept.
-   **jump \<chain\>**: Continue at the first rule of \<chain\>. It will continue at the next rule after a return statement is issued.
-   **goto \<chain\>**: Similar to jump, but after the new chain the evaluation will continue at the last chain instead of the one containing the goto statement.

### [Sets]

*nftables* allows defining anonymous and named **[sets](https://wiki.nftables.org/wiki-nftables/index.php/Sets)** ([dictionaries](https://wiki.nftables.org/wiki-nftables/index.php/Dictionaries) and [maps](https://wiki.nftables.org/wiki-nftables/index.php/Maps)). For example, the following nft script defines the fullbogons set, adds elements to it and drops packages from the IPs conforming the set.

[FILE] **`rules.nft`**

    #!/sbin/nft
    add set filter fullbogons
    add element filter fullbogons
    add element filter fullbogons
    add element filter fullbogons
    add element filter fullbogons
    add rule filter input iifname eth0 ct state new ip saddr @fullbogons counter drop comment "drop from blacklist"

## [Installation]

### [Kernel]

*Example Config*: A **bare minimum** for basic IPv4 firewalling with NAT:

[KERNEL] **Nftables kernel requirements**

    [*] Networking support Search for <code>CONFIG_NET</code> to find this item.  --->
       Networking options  --->
           [*] Network packet filtering framework (Netfilter) Search for <code>CONFIG_NETFILTER</code> to find this item.  --->
               Core Netfilter Configuration  --->
                   <M> Netfilter connection tracking support Search for <code>CONFIG_NF_CONNTRACK</code> to find this item.
                   <M> Netfilter nf_tables support Search for <code>CONFIG_NF_TABLES</code> to find this item.
                   <M>   Netfilter nf_tables conntrack module Search for <code>CONFIG_NFT_CT</code> to find this item.
                   <M>   Netfilter nf_tables log module Search for <code>CONFIG_NFT_LOG</code> to find this item.
                   <M>   Netfilter nf_tables limit module Search for <code>CONFIG_NFT_LIMIT</code> to find this item.
                   <M>   Netfilter nf_tables masquerade support Search for <code>CONFIG_NFT_MASQ</code> to find this item.
                   <M>   Netfilter nf_tables nat module Search for <code>CONFIG_NFT_NAT</code> to find this item.
               IP: Netfilter Configuration  --->
                   <M> IPv4 nf_tables support Search for <code>CONFIG_NF_TABLES_IPV4</code> to find this item.
                   <M> IPv4 packet rejection Search for <code>CONFIG_NF_REJECT_IPV4</code> to find this item.
                   <M> IP tables support (required for filtering/masq/NAT) Search for <code>CONFIG_IP_NF_IPTABLES</code> to find this item.
                   <M>   Packet filtering Search for <code>CONFIG_IP_NF_FILTER</code> to find this item.
                   <M>     REJECT target support Search for <code>CONFIG_IP_NF_TARGET_REJECT</code> to find this item.
                   <M>   iptables NAT support Search for <code>CONFIG_IP_NF_NAT</code> to find this item.
                   <M>     MASQUERADE target support Search for <code>CONFIG_IP_NF_TARGET_MASQUERADE</code> to find this item.

*Additional Common Config:* For **mixed IPv4 and IPv6 rules** combined into one table: *CONFIG_NF_TABLES_INET*

(If family *inet* is not enabled, only families *ip* and *ip6* can be used individually)

[KERNEL] **Nftables inet family**

    [*] Networking support  --->
        Networking options  --->
            [*] Network packet filtering framework (Netfilter)  --->
                Core Netfilter Configuration  --->
                    <M> Netfilter nf_tables support
                    [*]   Netfilter nf_tables mixed IPv4/IPv6 tables support

*Additional Optional Config:* **Early filtering based on network device** requires netdev tables support*: CONFIG_NF_TABLES_NETDEV*

[KERNEL] **Nftables netdev family**

    [*] Networking support  --->
        Networking options  --->
            [*] Network packet filtering framework (Netfilter)  --->
                Core Netfilter Configuration  --->
                    <M> Netfilter nf_tables support
                    [*]   Netfilter nf_tables netdev tables support

Nftables is very modular, and has many more options than mentioned here. Certain software likely requires additional features.

Depending on the goal, the bare minimum shown here may suffice, or other additional options can be enabled as modules so the kernel will load them as needed.

Disclaimer: This network section of the kernel changes frequently. More modules = more compatibility (they only load when requested).

### [[] USE flags]

### [USE flags for] [net-firewall/nftables](https://packages.gentoo.org/packages/net-firewall/nftables) [[]] [Linux kernel firewall, NAT and packet mangling tools]

  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+gmp`](https://packages.gentoo.org/useflags/+gmp)                 Add support for dev-libs/gmp (GNU MP library)
  [`+readline`](https://packages.gentoo.org/useflags/+readline)       Enable support for libreadline, a GNU line-editing library that almost everyone wants
  [`debug`](https://packages.gentoo.org/useflags/debug)               Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`doc`](https://packages.gentoo.org/useflags/doc)                   Create man pages for the package (requires app-text/asciidoc)
  [`json`](https://packages.gentoo.org/useflags/json)                 Enable JSON support via dev-libs/jansson
  [`libedit`](https://packages.gentoo.org/useflags/libedit)           Use the libedit library (replacement for readline)
  [`python`](https://packages.gentoo.org/useflags/python)             Add optional support/bindings for the Python language
  [`static-libs`](https://packages.gentoo.org/useflags/static-libs)   Build static versions of dynamic libraries as well
  [`test`](https://packages.gentoo.org/useflags/test)                 Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)     Verify upstream signatures on distfiles
  [`xtables`](https://packages.gentoo.org/useflags/xtables)           Add libxtables support to try to automatically translate rules added by iptables-compat
  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-01-19 04:26] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[net-firewall/nftables]](https://packages.gentoo.org/packages/net-firewall/nftables)[]]:

`root `[`#`]`emerge --ask net-firewall/nftables`

## [Configuration]

### [OpenRC]

The init script, [/etc/init.d/nftables], supports the following actions:

-   **save** - Stores the currently loaded ruleset in the location defined by `NFTABLES_SAVE`, default: [/var/lib/nftables/rules-save].
-   **reload** - Loads the currently loaded ruleset from `NFTABLES_SAVE`.
-   **stop** - Intended to be called on system shutdown. If `SAVE_ON_STOP` is enabled, saves the ruleset.
-   **start** - Intended to be called on system boot, loads the ruleset from `NFTABLES_SAVE`.
-   **clear** - Flushes the currently loaded ruleset, equivalent to [nft flush ruleset].
-   **list** - lists the currently loaded ruleset.

** Note**\
Configuration is available at [/etc/conf.d/nftables].

Nftables can be started at boot with:

`root `[`#`]`rc-update add nftables default`

** Warning**\
Failing to invoke [/etc/init.d/nftables save] manually after altering the ruleset could result in an older ruleset being loaded if there is an issue during system shutdown and saving the ruleset fails.

### [systemd]

After first setup:

`root `[`#`]`touch /var/lib/nftables/rules-save`

`root `[`#`]`systemctl enable --now nftables-store`

`root `[`#`]`systemctl enable --now nftables-load`

## [Usage]

All nftable commands are executed with the [nft] utility from [[[net-firewall/nftables]](https://packages.gentoo.org/packages/net-firewall/nftables)[]].

### [Tables]

#### [Creating tables]

The following command adds a **table** called *base_table* for the IPv4 and IPv6 layers:

`root `[`#`]`nft add table inet base_table`

Likewise, a table for arp can be created with

`root `[`#`]`nft add table arp base_table`

** Note**\
The name \"base_table\" used here is completely arbitrary. Any name can be used.

#### [Listing tables]

The following command lists all tables:

`root `[`#`]`nft list tables`

    table inet base_table
    table arp base_table

The tables can be filtered by type by adding the **address family** as an argument:

`root `[`#`]`nft list tables inet`

    table inet base_table

The contents of the table **base_table** can be listed with:

`root `[`#`]`nft list table inet base_table`

    table inet base_table
    }

** Tip**\
Adding **-a** as an argument to the [nft] command displays the rule handle after the rule.

`root `[`#`]`nft -a list table inet base_table`

    table inet base_table
    }

#### [Deleting tables]

The following command deletes the **table** called *base_table*, which is part of the **address family** *inet*:

`root `[`#`]`nft delete table inet base_table`

### [Chains]

#### [Adding chains]

The following command adds a **base chain** called *input_filter* to the **inet** *base_table* table. It is registered to the *input* **hook** with **priority** *0*, and **type** *filter*.

`root `[`#`]`nft add chain inet base_table input_filter "" `

** Note**\
A non-base chain can be added by not specifying the chain configurations between the curly braces.

** Important**\
Chains cannot be redefined once made, that means the hook type and priority are immutable. The chain must be deleted and redefined to keep the name but change these parameters. Deletion requires all references to the chain are also removed!

#### [Listing chain rules]

The rules for a chain can be listed using:

`root `[`#`]`nft list chain inet base_table input_filter`

    table inet base_filter
    }

#### [Deleting chains]

Chains can be removed with:

`root `[`#`]`nft delete chain inet base_table input_filter`

** Note**\
Chains can only be deleted if there are no rules in them, and they are not used as a jump target.

** Tip**\
**destroy** can be used instead of **delete** to ensure a chain does not exist. Unlike **delete**, **destroy** will not return an error if the chain did not already exist.

### [Rules]

#### [Adding rules]

The following command adds a **rule** to the **chain** called *input_filter*, on the *base_table* **table**, dropping all incoming traffic to port 80:

`root `[`#`]`nft add rule inet base_table input_filter tcp dport 80 drop`

#### [Listing all rules]

The following command can be used to list all rules in the current ruleset (with handles):

`root `[`#`]`nft -a list ruleset`

    table inet base_table
            chain output_filter
    }

#### [Deleting rules]

To delete a rule, the rule\'s handle number is required:

`root `[`#`]`nft delete rule inet base_table input_filter handle 3`

## [Modular Ruleset Management]

[nft] supports atomic rule replacement by using [nft -f]. Thus it is possible to conveniently manage the rules using files.

** Important**\
When loading rules [nft -f], as opposed to calling [nft] repeatedly in a shell script, failures will result in **none** of the file\'s rules being loaded.

** Note**\
Comments may be added to the file by prefixing them with **\#**, but these comments will not be visible in [nft list] output; they can also be appended to the end of rules as `comment "<arbitrary string>"`, and these will be preserved as-is in [nft list] output.

Nftables allows [including] additional files and directories. A directory, such as [/etc/nftables.conf.d/] can be created which contains additional rulesets to be loaded.

** Tip**\
Any of these files can be made executable, as long as the shebang `#! /sbin/nft -f` is included.

The following file creates a basic skeleton of a ruleset, which can be used with modules, loaded from [/etc/nftables.conf.d/]:

[FILE] **`/etc/nftables.rules`Basic router ruleset**

    #! /sbin/nft -f

    flush ruleset

    table netdev filter
    }

    table inet filter
      chain input_hook

      chain base_filter
        # Allow loopback traffic
        iifname lo counter accept
        oifname lo counter accept
      }

      chain drop_filter

      chain forward

      chain forward_hook

      chain output
      chain output_hook
    }

    table inet nat
      chain postrouting
    }
    include "/etc/nftables.rules.d/*.rules"

** Note**\
This ruleset uses a common filter, *base_filter*, for input, output, and forwarded traffic. Each filter has an associated hook which can be used for addition of rules.

### [Example Modules]

** Important**\
These modules will be loaded in lexicographical order, which can drastically change the behavior of a ruleset.

#### [Variable definitions]

** Important**\
Sets can be used to define IPs and ports, but cannot be used for interface names.

[FILE] **`/etc/nftables.rules.d/00-definitions.rules`Define variables which can be used in other modules.**

    #! /sbin/nft -f

    define lan_interface = fib.lan
    define wifi_interface = ax1800
    define management_interface = fib.management
    define dmz_interface = ethernet2

    define wan_interface = fib.wan

    define wifi_network = 192.168.1.0/24
    define lan_network = 192.168.10.0/24
    define management_network = 192.168.255.0/24
    define dmz_network = 192.168.2.0/24

    table inet filter
      }
      set dmz_nets
      }
      set untrusted_nets
      }
    }

#### [Jumping to the ingress filter]

[FILE] **`/etc/nftables.rules.d/00-ingress.rules`Hook the device ingress for *fib1* and *fib2*, filtering with the defined *ingress_filter* chain.**

    #! /sbin/nft -f

    table netdev filter
      chain ingress
    }

#### [Basic drop filter]

[FILE] **`/etc/nftables.rules.d/01-drop-policy.rules`Populate the *drop_filter* chain to drop some spammy traffic found on the DMZ.**

    #! /sbin/nft -f

    define dmz_spam_udp =
    define dmz_spam_tcp =

    table inet filter
      }
      set spam_tcp
      }

      chain drop_filter
    }

#### [Basic ICMP filter]

** Important**\
There is absolutely nothing wrong with allowing all ICMP, in fact, it\'s probably best.^[\[1\]](#cite_note-1)^

[FILE] **`/etc/nftables.rules.d/01-icmp.rules`Allow basic ICMP traffic**

    #! /sbin/nft -f

    define allowed_icmp_types =
    define trusted_icmp_types =
    define allowed_icmpv6_types =

    table inet filter
      chain icmp_filter
      chain icmpv6_filter
    }

#### [Allow DHCP traffic]

[FILE] **`/etc/nftables.rules.d/05-dhcp.rules`Allow DHCP client and server traffic on appropriate interfaces.**

    #! /sbin/nft -f

    define dhcp_server_interfaces =
    define dhcp_client_interfaces =

    table inet filter
      }
      set dhcp_client
      }
      set dhcp6_server
      }
      set dhcp6_client
      }
      chain input_hook
      chain output_hook
    }

#### [Allow inbound and forwarded SSH traffic]

[FILE] **`/etc/nftables.rules.d/22-ssh.rules`Allow inbound and forwarded SSH from the *\$management_network*; allow SSH to be forwarded to GitHub servers, from certain networks, and users on the router.**

    #! /sbin/nft -f
    define github_ssh_servers =

    table inet filter
      }
      set external_ssh_clients
      }
      set ssh_clients
      }
      set ssh_ports
      }
      chain ssh_filter
      chain base_filter
    }

#### [Allow outbound and forwarded NTP traffic]

[FILE] **`/etc/nftables.rules.d/21-ntp.rules`Allow forwarded NTP traffic, outbound from the NTP user.**

    #! /sbin/nft -f
    table inet filter
      }
      set ntp4_ports
      }
      chain base_filter
      chain ntp_filter
    }

#### [NAT LANs]

[FILE] **`/etc/nftables.rules.d/05-lan-nat.rules`NAT some local networks.**

    #! /sbin/nft -f

    table inet nat
      }
      chain postrouting
    }

#### [Masquerade Docker Traffic]

[FILE] **`/etc/nftables.rules.d/10-docker.rules`Masquerade docker traffic**

    #! /sbin/nft -f

    define docker_default_net = 172.17.0.0/16
    define docker_server_net = 10.100.100.0/24
    define docker_nets =

    table inet filter
      }
      set dns_ports
      }
      set web_ports
      }

      chain docker_filter
      chain forward_hook
    }

    table inet nat
      }
    }

## [Logging]

### [Log action]

The **log** rule can be used to log traffic to the kernel log.

** Tip**\
A *prefix* can be used to prefix the packet data.

** Note**\
**log** rules do not need to target, and can use **counter**s.

From the example configuration above, `log prefix "Dropped input traffic: " counter drop` results in:

[CODE] **dmesg output**

    [228391.038768] Dropped input traffic: IN=fib.wan OUT= MAC=[macaddr] SRC=[srcip] DST=[dstip] LEN=60 TOS=0x00 PREC=0x00 TTL=49 ID=0 DF PROTO=TCP SPT=61679 DPT=54728 WINDOW=65535 RES=0x00 SYN URGP=0
    [228392.039028] Dropped input traffic: IN=fib.wan OUT= MAC=[macaddr] SRC=[srcip] DST=[dstip] LEN=60 TOS=0x00 PREC=0x00 TTL=49 ID=0 DF PROTO=TCP SPT=61679 DPT=54728 WINDOW=65535 RES=0x00 SYN URGP=0
    [228393.466640] Dropped input traffic: IN=fib.wan OUT= MAC=[macaddr] SRC=[srcip] DST=[dstip] LEN=44 TOS=0x00 PREC=0x00 TTL=37 ID=36042 PROTO=TCP SPT=22103 DPT=427 WINDOW=1024 RES=0x00 SYN URGP=0
    [228394.239649] Dropped input traffic: IN=fib.wan OUT= MAC=[macaddr] SRC=[srcip] DST=[dstip] LEN=60 TOS=0x00 PREC=0x00 TTL=49 ID=0 DF PROTO=TCP SPT=61679 DPT=54728 WINDOW=65535 RES=0x00 SYN URGP=0
    [228396.088849] Dropped input traffic: IN=fib.wan OUT= MAC=[macaddr] SRC=[srcip] DST=[dstip] LEN=132 TOS=0x00 PREC=0x00 TTL=46 ID=47803 PROTO=UDP SPT=12306 DPT=54728 LEN=112
    [228398.440759] Dropped input traffic: IN=fib.wan OUT= MAC=[macaddr] SRC=[srcip] DST=[dstip] LEN=60 TOS=0x00 PREC=0x00 TTL=49 ID=0 DF PROTO=TCP SPT=61679 DPT=54728 WINDOW=65535 RES=0x00 SYN URGP=0
    [228402.822458] Dropped input traffic: IN=fib.wan OUT= MAC=[macaddr] SRC=[srcip] DST=[dstip] LEN=132 TOS=0x04 PREC=0x00 TTL=42 ID=28841 PROTO=UDP SPT=57221 DPT=54728 LEN=112
    [228405.338582] Dropped input traffic: IN=fib.wan OUT= MAC=[macaddr] SRC=[srcip] DST=[dstip] LEN=36 TOS=0x00 PREC=0xC0 TTL=1 ID=40280 PROTO=2
    [228405.339550] Dropped input traffic: IN=fib.wan OUT= MAC=[macaddr] SRC=[srcip] DST=[dstip] LEN=36 TOS=0x00 PREC=0xC0 TTL=1 ID=40280 PROTO=2
    [228405.779990] Dropped input traffic: IN=fib.wan OUT= MAC=[macaddr] SRC=[srcip] DST=[dstip] LEN=48 TOS=0x00 PREC=0x00 TTL=46 ID=49199 PROTO=UDP SPT=12306 DPT=54728 LEN=28
    [228406.641443] Dropped input traffic: IN=fib.wan OUT= MAC=[macaddr] SRC=[srcip] DST=[dstip] LEN=60 TOS=0x00 PREC=0x00 TTL=49 ID=0 DF PROTO=TCP SPT=61679 DPT=54728 WINDOW=65535 RES=0x00 SYN URGP=0
    [228409.477377] Dropped input traffic: IN=fib.wan OUT= MAC=[macaddr] SRC=[srcip] DST=[dstip] LEN=132 TOS=0x00 PREC=0x00 TTL=54 ID=49526 PROTO=UDP SPT=34989 DPT=62993 LEN=112
    [228409.683232] Dropped input traffic: IN=fib.wan OUT= MAC=[macaddr] SRC=[srcip] DST=[dstip] LEN=132 TOS=0x00 PREC=0x00 TTL=54 ID=49656 PROTO=UDP

### [syslog-ng nftables configuration]

Most logging daemons will log nftables traffic to the kernel log file, since it is logged to the kernel log. This can make it difficult to view dropped traffic, since it is mixed with non-firewall related traffic.

To configure [syslog-ng](https://wiki.gentoo.org/wiki/Syslog-ng "Syslog-ng") to log certain nftables traffic to other files:

[FILE] **`/etc/syslog-ng/syslog-ng.conf`Filter *fib.wan* interface traffic to [/var/log/nft/wan.log]**

    source kernsrc ;

    destination nft_WAN ;

    filter f_nft_WAN ;

    log ;

** Tip**\
In this case, `and not filter(f_nft_WAN)` can be added to the **f_messages** and **f_syslog** filters to prevent traffic from being logged multiple times.

## [Examples]

See the [Nftables examples article](https://wiki.gentoo.org/wiki/Nftables/Examples "Nftables/Examples").

## [Troubleshooting]

Before loading new or edited rules check them with [nft]

`user `[`$`]`nft -c -f ruleset`

### [No such file or directory]

If this error is printed for every chain of a table definition make sure, that the table\'s family is available through the kernel. This happens for example if the table uses family *inet* and the kernel configuration did not enable mixed IPv4 and IPv6 rules (CONFIG_NF_TABLES_INET).

### [Conflicting intervals]

A set definition of IP ranges causes this error if ranges overlap. For example 224.0.0.0/3 and 240.0.0.0/5 overlap completely. Either add *auto-merge* to the set\'s options, drop the range that is fully included or change syntax to 224.0.0.0-255.255.255.255.

[CODE] **Sample Set**

    table netdev filter
      # fix the last two IPs overlapping
      auto-merge
    }

### [Connections blocked after nftables restart or reboot]

The default configuration of the save and restore functions uses numeric mode to store the rule set. The persisted rule set could have changed from the original upload from a manually written file. Such a transformation might break things. Therefore, ensure that:

1.  /etc/conf.d/nftables contains the parameter -n for the SAVE_OPTIONS
2.  Loading the rule set as root yields a working configuration
3.  The save and restore cycle of restarting nftables service causes the issue

If all three conditions are met, remove the -n parameter from SAVE_OPTIONS in /etc/conf.d/nftables. Then load the rule set again from the manually written file and restart the service. This cycles through save and restore and should create a fully working rule set.

** Note**\
This affected at least version 0.9.9, see [[[bug #819456]](https://bugs.gentoo.org/show_bug.cgi?id=819456)[]].

### [Family netdev and ingress hook]

Broken packets should be rejected early which requires an ingress hook for family netdev. This sets up a chain that acts for a dedicated network device before packets enter further processing -- improved performance. The configuration looks like this:

[CODE] **Family netdev and ingress chain**

    table netdev filter
    }

Mind the device name enp4s0. If this changes for example when changing hardware or an upgrade changed device naming this family is broken. In turn none of the rules will be loaded. The error looks like this (filename and line numbers differ depending on the host configuration):

[CODE] **Error at chains instead of non-existing device**

    /etc/nftables.conf:94:9-15: Error: Could not...
    chain ingress {
          ^^^^^^^
    /etc/nftables.conf:94:9-15: Error: Could not...
      chain ingress {
            ^^^^^^^
    /etc/nftables.conf:94:9-15: Error: Could not...
      chain ingress {
            ^^^^^^^
    /etc/nftables.conf:94:9-15: Error: Could not...
      chain ingress {
            ^^^^^^^
    /etc/nftables.conf:94:9-15: Error: Could not...
      chain ingress {
            ^^^^^^^

Check that the device name is actually correct and exists, e.g. [ip addr list].

## [See also]

-   [Iptables](https://wiki.gentoo.org/wiki/Iptables "Iptables") --- a program used to configure and manage the kernel\'s netfilter modules. Contains a section about migration to nftables

## [External Resources]

-   [https://kernelnewbies.org/nftables_examples](https://kernelnewbies.org/nftables_examples)
-   [https://wiki.archlinux.org/index.php/Nftables](https://wiki.archlinux.org/index.php/Nftables)
-   [https://wiki.nftables.org/wiki-nftables/index.php/Main_Page](https://wiki.nftables.org/wiki-nftables/index.php/Main_Page)
-   [https://wiki.nftables.org/wiki-nftables/index.php/Quick_reference-nftables_in_10_minutes](https://wiki.nftables.org/wiki-nftables/index.php/Quick_reference-nftables_in_10_minutes)
-   [https://wiki.nftables.org/wiki-nftables/index.php/Moving_from_iptables_to_nftables](https://wiki.nftables.org/wiki-nftables/index.php/Moving_from_iptables_to_nftables)

## [References]

1.  [[[↑](#cite_ref-1)] [[http://shouldiblockicmp.com/](http://shouldiblockicmp.com/)]]