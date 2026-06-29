# Simple stateful firewall

This page explains how to set up a stateful firewall using iptables. It also explains what the rules mean and why they are needed. For simplicity, it is split into two major sections. The first section deals with a firewall for a single machine, the second sets up a NAT gateway in addition to the firewall from the first section.

## Prerequisites
First, install the userland utilities  or verify that they are already installed.

This article assumes that there are currently no iptables rules set. To check the current ruleset and verify that there are currently no rules run the following:

or

If there are rules, you may be able to reset the rules by loading a default rule set:

 # iptables-restore  /proc/net/xt_recent/sshbf}}}}

## IPv6
If you do not use IPv6, you can consider disabling it, otherwise follow these steps to enable the IPv6 firewall rules.

Copy the IPv4 rules used in this example as a base, and change any IPs from IPv4 format to IPv6 format:

 # cp /etc/iptables/iptables.rules /etc/iptables/ip6tables.rules

A few of the rules in this example have to be adapted for use with IPv6. The ICMP protocol has been updated in IPv6, replacing the ICMP protocol for use with IPv4. Hence, the reject error return codes  and  have to be converted to ICMPv6 codes.

The available ICMPv6 error codes are listed in RFC 4443, which specifies that connection attempts blocked by a firewall rule should use . Doing so will basically inform the remote system that the connection was rejected by a firewall, rather than a listening service.

If it is preferred not to explicitly inform about the existence of a firewall filter, the packet may also be rejected without the message:

  -A INPUT -j REJECT

The above will reject with the default return error of . You should note though, that identifying a firewall is a basic feature of port scanning applications and most will identify it regardless.

In the next step make sure the protocol and extension are changed to be IPv6 appropriate for the rule regarding all new incoming ICMP echo requests (pings):

 # ip6tables -A INPUT -p ipv6-icmp --icmpv6-type 128 -m conntrack --ctstate NEW -j ACCEPT

Netfilter conntrack does not appear to track ICMPv6 Neighbor Discovery Protocol (the IPv6 equivalent of ARP), so we need to allow ICMPv6 traffic regardless of state for all directly attached subnets. The following should be inserted after dropping , but before any other DROP or REJECT targets, along with a corresponding line for each directly attached subnet:

 # ip6tables -A INPUT -s fe80::/10 -p ipv6-icmp -j ACCEPT

If you want to enable DHCPv6, you need to accept incoming connections on UDP port 546:

 # ip6tables -A INPUT -p udp --sport 547 --dport 546 -j ACCEPT

Since there is no kernel reverse path filter for IPv6, you may want to enable one in ip6tables with the following:

 # ip6tables -t mangle -A PREROUTING -m rpfilter -j ACCEPT
 # ip6tables -t mangle -A PREROUTING -j DROP

## Saving the rules
The rule sets are now finished and should be saved to a file so that they can be loaded on every boot.

Save the IPv4 and IPv6 rules with these commands:

 # iptables-save -f /etc/iptables/iptables.rules
 # ip6tables-save -f /etc/iptables/ip6tables.rules

## Resulting ip6tables.rules file
Example of  file after running all the commands from above:

Then enable and start  and the . Check the status of the services to make sure the rules are loaded correctly.

## Setting up a NAT gateway
This section of the guide deals with NAT gateways. It is assumed that you already read the first part of the guide and set up the INPUT, OUTPUT, TCP and UDP chains like described above. All rules so far have been created in the filter table. In this section, we will also have to use the nat table. There is an ASCII art of the situation at Controlling What To NAT.

## Setting up the filter table
## Creating necessary chains
In our setup, we will create two new chains in the filter table, fw-interfaces and fw-open, using the following commands:

 # iptables -N fw-interfaces
 # iptables -N fw-open

## Setting up the FORWARD chain
Setting up the FORWARD chain is similar to the INPUT chain in the first section.

Now we set up a rule with the conntrack match, identical to the one in the INPUT chain:

 # iptables -A FORWARD -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT

The next step is to enable forwarding for trusted interfaces and to make all packets pass the fw-open chain.

 # iptables -A FORWARD -j fw-interfaces
 # iptables -A FORWARD -j fw-open

The remaining packets are denied with an ICMP message:

 # iptables -A FORWARD -j REJECT --reject-with icmp-host-unreachable
 # iptables -P FORWARD DROP

## Setting up the fw-interfaces and fw-open chains
The meaning of the fw-interfaces and fw-open chains is explained later, when we deal with the POSTROUTING and PREROUTING chains in the nat table, respectively.

## Setting up the nat table
All over this section, we assume that the outgoing interface (the one with the public internet IP) is ppp0. Keep in mind that you have to change the name in all following rules if your outgoing interface has another name.

## Setting up the POSTROUTING chain
Now, we have to define who is allowed to connect to the internet. Let us assume we have the subnet 192.168.0.0/24 (which means all addresses that are of the form 192.168.0.*) on eth0. We first need to accept the machines on this interface in the FORWARD table, that is why we created the fw-interfaces chain above:

 # iptables -A fw-interfaces -i eth0 -j ACCEPT

Now, we have to alter all outgoing packets so that they have our public IP address as the source address, instead of the local LAN address. To do this, we use the MASQUERADE target:

 # iptables -t nat -A POSTROUTING -s 192.168.0.0/24 -o ppp0 -j MASQUERADE

Do not forget the -o ppp0 parameter above. If you omit it, your network will be screwed up.

Let us assume we have another subnet, 10.3.0.0/16 (which means all addresses 10.3.*.*), on the interface eth1. We add the same rules as above again:

 # iptables -A fw-interfaces -i eth1 -j ACCEPT
 # iptables -t nat -A POSTROUTING -s 10.3.0.0/16 -o ppp0 -j MASQUERADE

The last step is to enable packet forwarding (if it is not already enabled).

Machines from these subnets can now use your new NAT machine as their gateway. Note that you may want to set up a DNS and DHCP server to simplify network settings on the client machines. This is not the topic of this guide.

## Setting up the PREROUTING chain
Sometimes, we want to change the address of an incoming packet from the gateway to a LAN machine. To do this, we use the fw-open chain defined above, as well as the PREROUTING chain in the nat table in the following two simple examples.

First, we want to change all incoming SSH packets (port 22) to the ssh server of the machine 192.168.0.5:

 # iptables -t nat -A PREROUTING -i ppp0 -p tcp --dport 22 -j DNAT --to 192.168.0.5
 # iptables -A fw-open -d 192.168.0.5 -p tcp --dport 22 -j ACCEPT

The second example will show you how to change packets to a different port than the incoming port. We want to change any incoming connection on port 8000 to our web server on 192.168.0.6, port 80:

 # iptables -t nat -A PREROUTING -i ppp0 -p tcp --dport 8000 -j DNAT --to 192.168.0.6:80
 # iptables -A fw-open -d 192.168.0.6 -p tcp --dport 80 -j ACCEPT

The same setup also works with udp packets.

## Saving the rules
Save the rules:

 # iptables-save -f /etc/iptables/iptables.rules

This assumes that you have followed the steps above to enable the iptables systemd service.
