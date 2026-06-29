# Internet sharing

This article explains how to share the internet connection from one machine to other(s).

## Requirements
The machine acting as server should have an additional network device, aka network interface. That network device requires a functional data link layer to the machine(s) that are going to receive internet access:

* To be able to share internet to several machines a switch can provide the data link layer connection.
* A wireless device can share access to several machines as well, see Software access point first for this case.
* If you are sharing to only one machine, a crossover cable is sufficient. In case one of the two computers' Ethernet cards has auto MDI-X capability, a crossover cable is not necessary and a regular Ethernet cable can be used. Executing  as root helps to figure it. You might be able to proceed even if that command gives you errors or does not find anything on either machine and you do not have a crossover cable.

## Configuration
All configuration is done on the server computer, except for the final step of #Assigning IP addresses to the client PC(s).

## Static IP address
On the server computer, assign a static IPv4 address to the interface connected to the other machines. The first 3 bytes of this address cannot be exactly the same as those of another interface, unless both interfaces have netmasks strictly greater than /24.

 # ip link set up dev net0
 # ip addr add 192.168.123.100/24 dev net0 # arbitrary address

To have your static IP assigned at boot, you can use a network manager.

## Enable packet forwarding
To check the current packet forwarding settings, run:

 # sysctl -a | grep forward

You will note options for controlling forwarding per default, per interface, as well as separate options for IPv4/IPv6 per interface. For detailed description of all available options, see the kernel documentation.

To enable IPv4 and IPv6 packet forwarding, configure sysctl to set these settings:

 net.ipv4.ip_forward = 1
 net.ipv4.conf.all.forwarding = 1
 net.ipv6.conf.all.forwarding = 1

To make changes persistent across reboots, see Sysctl#Configuration. You might consider writing settings to a file with a descriptive filename, such as .

Afterwards it is advisable to double-check forwarding is enabled as required after a reboot.

## Packet forwarding with systemd-networkd
If you are using systemd-networkd to manage your network configuration, you can also persist those settings across reboots:

This essentially sets the same  as mentioned in previous section. For IPv6 the configuration is .

This sets up packet forwarding for the specific interface only. For internet sharing to properly work, you need to enable packet forwarding on both (all) interfaces where traffic should be routed between. Typically your  and  interfaces.

## Enable NAT
Besides the methods listed here, its also possible to use  to set up a NAT.

## With iptables
Install the  package. Use iptables to enable NAT:

 # iptables -t nat -A POSTROUTING -o internet0 -j MASQUERADE
 # iptables -A FORWARD -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
 # iptables -A FORWARD -i net0 -o internet0 -j ACCEPT

Use  instead of  if you installed docker. # iptables -t nat -A POSTROUTING -o internet0 -j MASQUERADE
 # iptables -I DOCKER-USER 1 -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
 # iptables -I DOCKER-USER 2 -i net0 -o internet0 -j ACCEPT

If connected via PPPoE, clamp mss to pmtu in order to prevent fragmentation:

 # iptables -t mangle -A FORWARD -o ppp0 -p tcp -m tcp --tcp-flags SYN,RST SYN -j TCPMSS --clamp-mss-to-pmtu

Read the iptables article for more information (especially saving the rule and applying it automatically on boot). There is also an excellent guide on iptables Simple stateful firewall.

## With nftables
Install the  package. To enable NAT with nftables, you will have to create the  chain in a new/existing table:

 # nft add table inet nat
 # nft add chain inet nat postrouting '{ type nat hook postrouting priority srcnat ; }'

After that, you have to masquerade the  addresses for :

 # nft add rule inet nat postrouting oifname internet0 masquerade

Many firewall configurations, like [https://gitlab.archlinux.org/archlinux/packaging/packages/nftables/-/blob/main/nftables.conf the default , set the default policy of the 'filter' table's 'forward' chain to 'drop'. In such cases, you will need rules to allow forwarding NAT traffic:

 # nft add rule inet filter forward ct state related,established accept
 # nft add rule inet filter forward iifname net0 oifname internet0 accept

You can find more information on NAT in nftables in the nftables Wiki. If you want to make these changes permanent, follow the instructions on nftables.

## With firewalld
Install the  package. firewalld is a firewall daemon which relies on nftables or iptables. First change the firewalld zones of network interfaces:

 # firewall-cmd --zone=external --change-interface=internet0 --permanent
 # firewall-cmd --zone=internal --change-interface=net0 --permanent

Then add a new policy to let traffic flow between the internal and external zone:

 # firewall-cmd --permanent --new-policy int2ext
 # firewall-cmd --permanent --policy int2ext --add-ingress-zone internal
 # firewall-cmd --permanent --policy int2ext --add-egress-zone external
 # firewall-cmd --permanent --policy int2ext --set-target ACCEPT
 # firewall-cmd --reload

## Assigning IP addresses to the client PC(s)
If you are planning to regularly have several machines using the internet shared by this machine, then is a good idea to install a DHCP server. See Router#DNS and DHCP for the available options. Then configure a DHCP client on every client PC, see Network configuration#Network managers.

Incoming connections to UDP port 67 has to be allowed for DHCP server. It also necessary to allow incoming connections to UDP/TCP port 53 for DNS requests.

 # iptables -I INPUT -p udp --dport 67 -i net0 -j ACCEPT
 # iptables -I INPUT -p udp --dport 53 -s 192.168.123.0/24 -j ACCEPT
 # iptables -I INPUT -p tcp --dport 53 -s 192.168.123.0/24 -j ACCEPT

Alternatively using firewalld
 # firewall-cmd --zone=internal --permanent --add-service dns
 # firewall-cmd --zone=internal --permanent --add-service dhcp
 # firewall-cmd --zone=internal --permanent --add-service dhcpv6

If you are not planning to use this setup regularly, you can manually add an IP to each client instead.

## Manually adding an IP
Instead of using DHCP, a static IP address and a default route via  can also be configured manually. There are many tools available to configure the network accordingly. One prominent example of such a tool is , see Network configuration#Network management. Alternatively, one can use a  file, see systemd-networkd#Wired adapter using a static IP to setup a static IP.

Configure a DNS server for each client, see Domain name resolution for details.

That is it. The client PC should now have Internet.

## Troubleshooting
If you are able to connect the two PCs but cannot send data (for example, if the client PC makes a DHCP request to the server PC, the server PC receives the request and offers an IP to the client, but the client does not accept it, timing out instead), check that you do not have other iptables rules interfering.

## Clients cannot access the internet or cannot connect
Symptoms might also include: Clients get  when pinging host, gets   or  when pinging devices outside the LAN (that should be forwarded by NAT), DHCP offers not crossing a bridge, ...

It is known that docker may cause these problems. Simply disabling  and  solves this problem.

docker github issue.

## Connected second PC unable to use bridged LAN
First PC have two LANs. Second PC have one LAN and connected to first PC. Lets go second PC to give all access to LAN after bridged interface:

 # sysctl net.bridge.bridge-nf-filter-pppoe-tagged=0
 # sysctl net.bridge.bridge-nf-filter-vlan-tagged=0
 # sysctl net.bridge.bridge-nf-call-ip6tables=0
 # sysctl net.bridge.bridge-nf-call-iptables=0
 # sysctl net.bridge.bridge-nf-call-arptables=0
