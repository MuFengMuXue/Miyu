# Nftables

nftables is a netfilter project that aims to replace the existing {ip,ip6,arp,eb}tables framework. It provides a new packet filtering framework, a new userspace utility (nft), and a compatibility layer for {ip,ip6}tables. It uses the existing hooks, connection tracking system, userspace queueing component, and logging subsystem of netfilter.

It consists of three main components: a kernel implementation, the libnl netlink communication and the nftables userspace front-end.
The kernel provides a netlink configuration interface, as well as run-time rule-set evaluation, libnl contains the low-level functions for communicating with the kernel, and the nftables front-end is what the user interacts with via nft.

You can also visit the official nftables wiki page for more information.

## Installation
Install the userspace utilities package .

If you have  installed, install  which will automatically uninstall  and prevent conflicts with .

## Front-ends
*
*
*
*

## Usage
nftables makes no distinction between temporary rules made in the command line and permanent ones loaded from or saved to a file.

All rules have to be created or loaded using  command line utility.

Refer to #Configuration section on how to use.

Current ruleset can be printed with:

 # nft list ruleset

Remove all ruleset leaving the system with no firewall:

 # nft flush ruleset

Read ruleset from  by restarting .

## Simple firewall
 comes with a simple and secure firewall configuration stored in the  file.

The  will load rules from that file when started or enabled.

## Configuration
nftables userspace utility  performs most of the rule-set evaluation before handing rule-sets to the kernel. Rules are stored in chains, which in turn are stored in tables. The following sections indicate how to create and modify these constructs.

To read input from a file use the / option:

 # nft --file filename

Note that any rules already loaded are not automatically flushed.

See  for a complete list of all commands.

## Tables
Tables hold #Chains. Unlike tables in iptables, there are no built-in tables in nftables. The number of tables and their names is up to the user. However, each table only has one address family and only applies to packets of this family. Tables can have one of five families specified:

{| class="wikitable"
! nftables family || iptables utility
|-
| ip || iptables
|-
| ip6 || ip6tables
|-
| inet || iptables and ip6tables
|-
| arp || arptables
|-
| bridge || ebtables
|-
|}

 (i.e. IPv4) is the default family and will be used if family is not specified.

To create one rule that applies to both IPv4 and IPv6, use .  allows for the unification of the  and  families to make defining rules for both easier.

See  for a complete description of address families.

In all of the following,  is optional, and if not specified is set to .

## Create table
The following adds a new table:

 # nft add table family_type table_name

## List tables
To list all tables:

 # nft list tables

## List chains and rules in a table
To list all chains and rules of a specified table:

 # nft list table family_type table_name

For example, to list all the rules of the  table of the  family:

 # nft list table inet my_table

## Delete table
To delete a table:

 # nft delete table family_type table_name

This will destroy all chains in the table.

## Flush table
To flush/clear all rules from a table:

 # nft flush table family_type table_name

## Chains
The purpose of chains is to hold #Rules. Unlike chains in iptables, there are no built-in chains in nftables. This means that if no chain uses any types or hooks in the netfilter framework, packets that would flow through those chains will not be touched by nftables, unlike iptables.

Chains have two types. A base chain is an entry point for packets from the networking stack, where a hook value is specified. A regular chain may be used as a jump target for better organization.

See the traffic flow diagram showing the ordering between individual hooks. Within a given hook, netfilter performs operations in order of increasing numerical priority.

In all of the following  is optional, and if not specified is set to .

## Create chain
## Base chain
To add a base chain it is mandatory to specify type, hook and priority values:

 # nft add chain family_type table_name chain_name '{ type chain_type hook hook_type priority priority_value ; policy policy ;}'

 can be , , or .

For IPv4/IPv6/Inet address families  can be , , , , or . See  for a list of supported family_type, chain_type and hook_type combinations.

 takes either a priority name or an integer value. See  for a list of standard priority names and values. Chains with lower numbers are processed first and can be negative. Optionally base chains can have a  ( or the default ), to define what happens to packets not explicitly accepted or refused in contained rules.

For example, to add a base chain that filters input packets:

 # nft add chain inet my_table my_chain '{ type filter hook input priority 0; }'

Replace  with  in any of the above to add a new chain but return an error if the chain already exists.

## Regular chain
The following adds a regular chain named  to the table named :

 # nft add chain family_type table_name chain_name

For example, to add a regular chain named  to the  table of the  address family:

 # nft add chain inet my_table my_tcp_chain

## List chains
The following lists all chains without rules (see #List rules) of a family_type:

 # nft list chains family_type

For example, the following lists the chains of ipv6:

 # nft list chains ip6

if you omit the family_type all chains are printed.

## Edit a chain
To edit a chain, simply call it by its name and define the rules you want to change.

 # nft chain family_type table_name chain_name '{ [ type chain_type hook hook_type device device_name priority priority_value ; policy policy_type ;  }'

For example, to change the  chain policy of the default table from  to

 # nft chain inet my_table my_input '{ policy drop ; }'

## Delete a chain
To delete a chain:

 # nft delete chain family_type table_name chain_name

The chain must not contain any rules or be a jump target.

## Flush rules from a chain
To flush rules from a chain:

 # nft flush chain family_type table_name chain_name

## Rules
Rules are either constructed from expressions or statements and are contained within chains.

## Add rule
To add a rule to a chain:

 # nft add rule family_type table_name chain_name handle handle_value statement

The rule is appended at , which is optional. If not specified, the rule is appended to the end of the chain.

The  switch, which can be added to any valid list command, must be used to determine a rule handle. This switch tells  to list the handles in its output. The  argument is useful for viewing some numeric output, like unresolved IP addresses.

{{hc|# nft --handle --numeric list chain inet my_table my_input|2=
table inet my_table {
     chain input {
          type filter hook input priority 0;
          ip saddr 127.0.0.1 accept # handle 10
     }
}
}}

To prepend the rule to the position:

 # nft insert rule family_type table_name chain_name handle handle_value statement

If  is not specified, the rule is prepended to the chain.

## Expressions
Typically a  includes some expression to be matched and then a verdict statement. Verdict statements include , , , , , , and . Other statements than verdict statements are possible. See  for more information.

There are various expressions available in nftables and, for the most part, coincide with their iptables counterparts. The most noticeable difference is that there are no generic or implicit matches. A generic match was one that was always available, such as  or . Implicit matches were protocol-specific, such as  when a packet was determined to be TCP.

The following is an incomplete list of the matches available:

* meta    (meta properties, e.g. interfaces)
* icmp    (ICMP protocol)
* icmpv6  (ICMPv6 protocol)
* ip      (IP protocol)
* ip6     (IPv6 protocol)
* tcp     (TCP protocol)
* udp     (UDP protocol)
* sctp    (SCTP protocol)
* ct      (connection tracking)

The following is an incomplete list of match arguments (for a more complete list, see ):

In a way, iif and oif versus iifname and oifname are similar to static versus dynamic. Or the programming concept of definition versus declaration. Or to early binding versus delayed binding. See a use case and a link to further explanation.

## List rules
The following lists all rules of a chain:

 # nft list chain family_type table_name chain_name

For example, the following lists the rules of the chain named  in the  table named :

 # nft list chain inet my_table my_output

## Deletion
Individual rules can only be deleted by their handles. Obtaining the handles was shown at #Add rule. Assuming

{{hc|# nft --handle --numeric list chain inet my_table my_input|2=
table inet my_table {
     chain input {
          type filter hook input priority 0;
          ip saddr 127.0.0.1 accept # handle 10
     }
}
}}

 # nft delete rule inet my_table my_input handle 10
deletes it.

All the chains in a table can be flushed with the  command. Individual chains can be flushed using either the  or  commands.

 # nft flush table table_name
 # nft flush chain family_type table_name chain_name
 # nft delete rule family_type table_name chain_name

The first command flushes all of the chains in the ip  table. The second flushes the  chain in the   table. The third deletes all of the rules in  chain in the   table.

## Sets
Sets are named or anonymous, and consist of one or more elements, separated by commas, enclosed by curly braces. Anonymous sets are embedded in rules and cannot be updated, you must delete and re-add the rule. E.g., you cannot just remove "http" from the dports set in the following:

 # nft add rule ip6 filter input tcp dport {telnet, http, https} accept

Named sets can be updated, and can be typed and flagged. sshguard uses named sets for the IP addresses of blocked hosts.

 table ip sshguard {
        set attackers {
                type ipv4_addr
                flags interval
                elements = { 1.2.3.4 }
        }

To add or delete elements from the set, use:

 # nft add element ip sshguard attackers { 5.6.7.8/32 }
 # nft delete element ip sshguard attackers { 1.2.3.4/32 }

Note the type ipv4_addr can include a CIDR netmask (the  here is not necessary, but is included for completeness' sake). Note also, the set defined here by {{ic|TABLE ip sshguard { SET attackers }}} is addressed as .

## Atomic reloading
Flush the current ruleset:

 # echo "flush ruleset" > /tmp/nftables

Dump the current ruleset:

 # nft -s list ruleset >> /tmp/nftables

Now you can edit  and apply your changes with:

 # nft -f /tmp/nftables

## Examples
## Workstation
{{hc|/etc/nftables.conf|2=
flush ruleset

table inet my_table {
	set LANv4 {
		type ipv4_addr
		flags interval

		elements = { 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, 169.254.0.0/16 }
	}
	set LANv6 {
		type ipv6_addr
		flags interval

		elements = { fd00::/8, fe80::/10 }
	}

	chain my_input_lan {
		udp sport 1900 udp dport >= 1024 meta pkttype unicast limit rate 4/second burst 20 packets accept comment "Accept UPnP IGD port mapping reply"

		udp sport netbios-ns udp dport >= 1024 meta pkttype unicast accept comment "Accept Samba Workgroup browsing replies"

	}

	chain my_input {
		type filter hook input priority filter; policy drop;

		iif lo accept comment "Accept any localhost traffic"
		ct state invalid drop comment "Drop invalid connections"
		fib daddr . iif type != { local, broadcast, multicast } drop comment "Drop packets if the destination IP address is not configured on the incoming interface (strong host model)"
		ct state { established, related } accept comment "Accept traffic originated from us"

		meta l4proto { icmp, ipv6-icmp } accept comment "Accept ICMP"
		ip protocol igmp accept comment "Accept IGMP"

		udp dport mdns ip6 daddr ff02::fb accept comment "Accept mDNS"
		udp dport mdns ip daddr 224.0.0.251 accept comment "Accept mDNS"

		ip6 saddr @LANv6 jump my_input_lan comment "Connections from private IP address ranges"
		ip saddr @LANv4 jump my_input_lan comment "Connections from private IP address ranges"

		counter comment "Count any other traffic"
	}

	chain my_forward {
		type filter hook forward priority filter; policy drop;
		# Drop everything forwarded to us. We do not forward. That is routers job.
	}

	chain my_output {
		type filter hook output priority filter; policy accept;
		# Accept every outbound connection
	}

}
}}

## Server
{{hc|/etc/nftables.conf|2=
flush ruleset

table inet my_table {
	set LANv4 {
		type ipv4_addr
		flags interval

		elements = { 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, 169.254.0.0/16 }
	}
	set LANv6 {
		type ipv6_addr
		flags interval

		elements = { fd00::/8, fe80::/10 }
	}

	chain my_input_lan {
		meta l4proto { tcp, udp } th dport 2049 accept comment "Accept NFS"

		udp dport netbios-ns accept comment "Accept NetBIOS Name Service (nmbd)"
		udp dport netbios-dgm accept comment "Accept NetBIOS Datagram Service (nmbd)"
		tcp dport netbios-ssn accept comment "Accept NetBIOS Session Service (smbd)"
		tcp dport microsoft-ds accept comment "Accept Microsoft Directory Service (smbd)"

		udp sport { bootpc, 4011 } udp dport { bootps, 4011 } accept comment "Accept PXE"
		udp dport tftp accept comment "Accept TFTP"
	}

	chain my_input {
		type filter hook input priority filter; policy drop;

		iif lo accept comment "Accept any localhost traffic"
		ct state invalid drop comment "Drop invalid connections"
		fib daddr . iif type != { local, broadcast, multicast } drop comment "Drop packets if the destination IP address is not configured on the incoming interface (strong host model)"
		ct state { established, related } accept comment "Accept traffic originated from us"

		meta l4proto { icmp, ipv6-icmp } accept comment "Accept ICMP"
		ip protocol igmp accept comment "Accept IGMP"

		udp dport mdns ip6 daddr ff02::fb accept comment "Accept mDNS"
		udp dport mdns ip daddr 224.0.0.251 accept comment "Accept mDNS"

		ip6 saddr @LANv6 jump my_input_lan comment "Connections from private IP address ranges"
		ip saddr @LANv4 jump my_input_lan comment "Connections from private IP address ranges"

		tcp dport ssh accept comment "Accept SSH on port 22"

		tcp dport ipp accept comment "Accept IPP/IPPS on port 631"

		meta l4proto { tcp, udp } th dport { http, https, 8008, 8080 } accept comment "Accept HTTP (ports 80, 443, 8008, 8080)"

		udp sport bootpc udp dport bootps ip saddr 0.0.0.0 ip daddr 255.255.255.255 accept comment "Accept DHCPDISCOVER (for DHCP-Proxy)"
	}

	chain my_forward {
		type filter hook forward priority filter; policy drop;
		# Drop everything forwarded to us. We do not forward. That is routers job.
	}

	chain my_output {
		type filter hook output priority filter; policy accept;
		# Accept every outbound connection
	}

}
}}

## Limit rate
{{bc|1=
table inet my_table {
	chain my_input {
		type filter hook input priority filter; policy drop;

		iif lo accept comment "Accept any localhost traffic"
		ct state invalid drop comment "Drop invalid connections"
		fib daddr . iif type != { local, broadcast, multicast } drop comment "Drop packets if the destination IP address is not configured on the incoming interface (strong host model)"

		meta l4proto icmp icmp type echo-request limit rate over 10/second burst 4 packets drop comment "No ping floods"
		meta l4proto ipv6-icmp icmpv6 type echo-request limit rate over 10/second burst 4 packets drop comment "No ping floods"

		ct state { established, related } accept comment "Accept traffic originated from us"

		meta l4proto { icmp, ipv6-icmp } accept comment "Accept ICMP"
		ip protocol igmp accept comment "Accept IGMP"

		tcp dport ssh ct state new limit rate 15/minute accept comment "Avoid brute force on SSH"

	}

}
}}

## Jump
When using jumps in configuration file, it is necessary to define the target chain first. Otherwise one could end up with .

{{bc|1=
table inet my_table {
    chain web {
        tcp dport http accept
        tcp dport 8080 accept
    }
    chain my_input {
        type filter hook input priority filter;
        ip saddr 10.0.2.0/24 jump web
        drop
    }
}
}}

## Different rules for different interfaces
If your box has more than one network interface, and you would like to use different rules for different interfaces, you may want to use a "dispatching" filter chain, and then interface-specific filter chains. For example, let us assume your box acts as a home router, you want to run a web server accessible over the LAN (interface ), but not from the public internet (interface ), you may want to consider a structure like this:

{{bc|
table inet my_table {
  chain my_input { # this chain serves as a dispatcher
    type filter hook input priority filter; policy drop;

    iif lo accept comment "always accept loopback"
    iifname enp2s0 jump my_input_public
    iifname enp3s0 jump my_input_private
  }
  chain my_input_public { # rules applicable to public interface interface
    ct state {established,related} accept
    ct state invalid drop
    udp dport bootpc accept
    tcp dport bootpc accept
  }
  chain my_input_private {
    ct state {established,related} accept
    ct state invalid drop
    udp dport bootpc accept
    tcp dport bootpc accept
    tcp port http accept
    tcp port https accept
    reject with icmpx port-unreachable comment "all other traffic"
  }
  chain my_output { # we let everything out
    type filter hook output priority filter;
    accept
  }
}
}}

Alternatively you could choose only one  statement, such as for the single upstream interface, and put the default rules for all other interfaces in one place, instead of dispatching for each interface.

## Masquerading
nftables has a special keyword  "where the source address is automagically set to the address of the output interface" (source). This is particularly useful for situations in which the IP address of the interface is unpredictable or unstable, such as the upstream interface of routers connecting to many ISPs. Without it, the Network Address Translation rules would have to be updated every time the IP address of the interface changed.

To use it:

* make sure masquerading is enabled in the kernel (true if you use the default kernel), otherwise during kernel configuration, set .
* the  keyword can only be used in chains of type .
* masquerading is a kind of source NAT, so only works in the output path.

Example for a machine with two interfaces: LAN connected to , and public internet connected to :

{{bc|
table inet my_nat {
  chain my_masquerade {
    type nat hook postrouting priority srcnat;
    oifname "enp2s0" masquerade
  }
}
}}

Since the table type is  both IPv4 and IPv6 packets will be masqueraded. If you want only ipv4 packets to be masqueraded (since extra adress space of IPv6 makes NAT not required)  expression can be used infront of  or the table type can be changed to .

## NAT with port forwarding
This example will masquerade traffic exiting through a WAN interface called eth0 and forward ports 22 and 80 to . You will need to set  to  via sysctl.

{{bc|
table nat {
    chain prerouting {
        type nat hook prerouting priority dstnat;
        iif eth0 tcp dport {22, 80} dnat to 10.0.0.2
    }
    chain postrouting {
        type nat hook postrouting priority srcnat;
        oif eth0 masquerade
    }
}
}}

## Count new connections per IP
Use this snippet to count HTTPS connections:

{{hc|/etc/nftables.conf|
table inet filter {
    set https {
        type ipv4_addr;
        flags dynamic;
        size 65536;
        timeout 60m;
    }

    chain input {
        type filter hook input priority filter;
        ct state new meta l4proto { tcp, udp } th dport 443 update @https { ip saddr counter }
    }
}
}}

To print the counters, run .

## Dynamic blackhole
Use this snippet to drop all HTTPS connections for 1 minute from a source IP (or /64 IPv6 range) that exceeds the limit of 10/second.

{{hc|/etc/nftables.conf|
table inet dev {
    set blackhole_ipv4 {
        type ipv4_addr;
        flags dynamic, timeout;
        size 65536;
    }
    set blackhole_ipv6 {
        type ipv6_addr;
        flags dynamic, timeout;
        size 65536;
    }

    chain input {
        type filter hook input priority filter; policy accept;
        ct state new meta l4proto { tcp, udp } th dport 443 \
                meter flood_ipv4 size 128000 { ip saddr timeout 10s limit rate over 10/second } \
                add @blackhole_ipv4 { ip saddr timeout 1m }
        ct state new meta l4proto { tcp, udp } th dport 443 \
                meter flood_ipv6 size 128000 { ip6 saddr and ffff:ffff:ffff:ffff:: timeout 10s limit rate over 10/second } \
                add @blackhole_ipv6 { ip6 saddr and ffff:ffff:ffff:ffff:: timeout 1m }

        ip saddr @blackhole_ipv4 counter drop
        ip6 saddr and ffff:ffff:ffff:ffff:: @blackhole_ipv6 counter drop
    }
}
}}

To print the blackholed IPs, run .

## Tips and tricks
## Saving current rule set
The output of  command is a valid input file for it as well. Current rule set can be saved to file and later loaded back in.

 # nft -s list ruleset | tee filename

## Simple stateful firewall
See Simple stateful firewall for more information.

## Single machine
Flush the current ruleset:

 # nft flush ruleset

Add a table:

 # nft add table inet my_table

Add the input, forward, and output base chains. The policy for input and forward will be to drop. The policy for output will be to accept.

 # nft add chain inet my_table my_input '{ type filter hook input priority 0 ; policy drop ; }'
 # nft add chain inet my_table my_forward '{ type filter hook forward priority 0 ; policy drop ; }'
 # nft add chain inet my_table my_output '{ type filter hook output priority 0 ; policy accept ; }'

Add two regular chains that will be associated with tcp and udp:

 # nft add chain inet my_table my_tcp_chain
 # nft add chain inet my_table my_udp_chain

Related and established traffic will be accepted:

 # nft add rule inet my_table my_input ct state '{ related, established }' accept

All loopback interface traffic will be accepted:

 # nft add rule inet my_table my_input iif lo accept

Drop any invalid traffic:

 # nft add rule inet my_table my_input ct state invalid drop

Accept ICMP and IGMP:

 # nft add rule inet my_table my_input meta l4proto '{ icmp, ipv6-icmp }' accept
 # nft add rule inet my_table my_input ip protocol igmp accept

New udp traffic will jump to the UDP chain:

 # nft add rule inet my_table my_input meta l4proto udp ct state new jump my_udp_chain

New tcp traffic will jump to the TCP chain:

 # nft add rule inet my_table my_input 'meta l4proto tcp tcp flags & (fin|syn|rst|ack) == syn ct state new jump my_tcp_chain'

At this point you should decide what ports you want to open to incoming connections, which are handled by the TCP and UDP chains. For example to open connections for a web server add:

 # nft add rule inet my_table my_tcp_chain tcp dport 80 accept

To accept HTTPS connections for a webserver on port 443:

 # nft add rule inet my_table my_tcp_chain tcp dport 443 accept
 # nft add rule inet my_table my_udp_chain udp dport 443 accept

To accept SSH traffic on port 22:

 # nft add rule inet my_table my_tcp_chain tcp dport 22 accept

To accept incoming DNS requests:

 # nft add rule inet my_table my_tcp_chain tcp dport 53 accept
 # nft add rule inet my_table my_udp_chain udp dport 53 accept

Be sure to make your changes permanent when satisfied.

## Prevent brute-force attacks
Sshguard is program that can detect brute-force attacks and modify firewalls based on IP addresses it temporarily blacklists. See Sshguard#nftables on how to set up nftables to be used with it.

## Logging traffic
You can log packets using the  action. The most simple rule to log all incoming traffic is:

 # nft add rule inet filter input log

See nftables wiki for details.

## Monitor
Listen to all events, report in native nft format.

 # nft monitor

See

## Ruleset debugging trace temporary
meta nftrace set 1 ruleset packet tracing on/off. Use monitor trace command to watch traces.

In another shell "include" the file inside the interactive shell:

 # nft -i
 nft> include "/root/nftables.trace"

Example, adjust to your needs:

{{hc|/root/nftables.trace|
add table ip temp-trace {comment "Temporary table!!"; flags owner;}
add chain ip temp-trace icmp-prerouting { type filter hook prerouting priority raw - 1 ; }
add rule ip temp-trace icmp-prerouting ip protocol icmp meta nftrace set 1
}}

This file adds a temporary table (flags owner) so that it gets automatically removed, if the calling (process) interactive nft is closed. The Base Chain needs to be adjusted for your use case. You can create multiple chains and multiple rules with "meta nftrace set 1"  "ip protocol icmp" is used just as an example and is not necessary. There are many ways to achieve a similar effect, the advantage is that by closing the interactive shell the previous state is automatically restored, and if an error is inside the file nothing gets executed.

See nftables wiki and a python tool automating the process and coloring.

## Using iptables-nft
The older iptables language remains quite dominant in Linux documentation, and quite a few things still depend on iptables to run (such as Docker's networking). Although it's also perfectly workable to use legacy iptables and nftables at the same time, using iptables-nft's translation is preferred because:
* It puts everything in the same place, using the newer, more efficient, non-locking framework.
* It checks for conflicts.

There are two ways to use the old iptables language with nftables:

*  and  (idem for , , etc.) take iptable language and output nft language. They do not change running nft settings. See .
: For configuration you want to maintain later on, it's a good idea to use the  tool and integrate the result code into your existing rules. For example, if you find something useful in simple stateful firewall or the wider Internet, you can translate them to put into your nft config.
*  and  (again idem for  etc.) uses the above translation and put them into the running nft settings. It also offers statistics like regular iptables does. See .
: Those commands work reasonably well given what they have to work with. They should "just work" with simple usage, but occasionally you will need to step in and debug.

## Dynamic named sets using systemd-networkd
systemd-networkd's connections can use the  option to populate predefined named sets with host IP addresses, network prefixes and interface indexes. This allows to avoid hardcoding them in . The  option is supported in , ,  and  sections. See .

For example, to process connections from a local network (where IP addresses are assigned via DHCP or SLAAC) in a separate  chain:

{{hc|/etc/nftables.conf|2=
...
table inet my_table {

	set eth_ipv4_prefix {
		type ipv4_addr
		flags interval
		comment "Populated by systemd-networkd"
	}
	set eth_ipv6_prefix {
		type ipv6_addr
		flags interval
		comment "Populated by systemd-networkd"

		elements = { fe80::/10 }
	}
	set eth_ifindex {
		type iface_index
		comment "Populated by systemd-networkd"
	}
...
	chain my_input {
		type filter hook input priority filter; policy drop;

		iif @eth_ifindex ip6 saddr @eth_ipv6_prefix jump my_input_lan comment "Connections from LAN"
		iif @eth_ifindex ip saddr @eth_ipv4_prefix jump my_input_lan comment "Connections from LAN"
	}
...
}
}}

## Troubleshooting
## Working with Docker
Using nftables can interfere with Docker networking (and probably other container runtimes as well). You can find various workarounds on the internet which either involve patching iptables rules and ensuring a defined service start order or disabling dockers iptables management completely which makes using docker very restrictive (think port forwarding or docker-compose).

A reliable method is letting docker run in a separate network namespace where it can do whatever it wants. It is probably best to not use  and instead use  to prevent docker from mixing nftables and iptables rules.

Use the following docker service drop-in file:

Adjust the  IP addresses if they are not appropriate for your setup.

Enable IP forwarding and set-up NAT for docker0 with the following postrouting rule:

 iifname docker0 oifname eth0 masquerade

Then, ensure that kernel IP forwarding is enabled.

Now you can setup a firewall and port forwarding for the  interface using nftables without any interference.
