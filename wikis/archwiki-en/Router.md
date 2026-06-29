# Router

This article is a tutorial for turning a computer into an internet gateway/router. To strengthen its security it should not run any services available to the outside world. Towards the LAN, run only gateway specific services; especially do not run httpd, ftpd, samba, nfsd, etc. as those belong on a server in the LAN since they introduce security risks.

This article does not attempt to show how to set up a shared connection between two machines using cross-over cables. For a simple internet sharing solution, see Internet sharing.

## Hardware requirements
* See Partitioning#Partition scheme for advice on the minimum required disk space.
* At least two physical network interfaces: a gateway connects two networks with each other (actually a router can be made using a single physical interface that underlays two VLAN interfaces and is connected to a VLAN-aware switch, so-called router-on-a-stick configuration, but it is not covered in this article). You will need to be able to connect those networks to the same physical computer. One interface must connect to the external network, while the other connects to the internal network.
* A hub, switch or UTP cable: You need a way to connect the other computers to the gateway

## Network interface configuration
## Persistent interface naming
systemd automatically chooses unique interface names for all your interfaces. These are persistent and will not change when you reboot.
However you might want to rename your interfaces e.g. in order to highlight their different networks to which they connect. Throughout the following sections of this guide, the convention stated below is used:

* intern0: the network card connected to the LAN. On an actual computer it will probably have the name enp2s0, enp1s1, etc.
* extern0: the network card connected to the external network (or WAN). It will probably have the name enp2s0, enp1s1, etc.

You may change the assigned names of your devices by following Network configuration#Change interface name. Due to the example-rich nature of this article, you might want to choose the names above.

## IP configuration
## With netctl
Now you will need to configure the network interfaces. One way to do so, is using netctl profiles. You will need to create two profiles.

Next, we set up the interfaces with netctl:

 # netctl enable extern0-profile
 # netctl enable intern0-profile

## With systemd-networkd
A straight-forward and simple way to configure network interfaces is via systemd-networkd.

* Apply a DHCP client configuration for the  interface.
* Apply a static IP configuration for the  interface.

See systemd-networkd#Configuration for configuration details and an overview of the available options. Run  to apply the configuration changes.

## ADSL connection/PPPoE
Using ppp, we can connect an ADSL modem to the  interface of the firewall and have Arch manage the connection. Make sure to put the modem in bridged mode though (either half-bridge or RFC1483), otherwise, the modem will act as a router too. Install the  package.

It should be noted that if you use only PPPoE to connect to the internet (i.e. you do not have another WAN port, except for the one that connects to your modem) you do not need to set up the  as the external pseudo-interface will be ppp0.

## PPPoE configuration
You can use netctl to setup the PPPoE connection. To get started, do

 # cp /etc/netctl/examples/pppoe /etc/netctl/

and start editing. For the interface configuration, choose the interface that connects to the modem. If you only connect to the internet through PPPoE, this will probably be . Fill in the rest of the fields with your ISP information. See the PPPoE section in the  man page for more information on the fields.

## DNS and DHCP
The following comparison table lists the available DHCP servers and their features:

{| class="wikitable"
! Server !! DHCPv4 !! DHCPv6 !! IPv6 Router Advertisement !! GUI !! Interfaces !! Storage backend(s) !! Note
|-
| dhcpd ||  ||  ||  || Glass-ISC-DHCP || ? || File || Unmaintained since 2022. Superseded by Kea.
|-
| dnsmasq ||  ||  ||  ||  || D-Bus || File || Also DNS, PXE and TFTP.
|-
| Kea ||  ||  ||  || Stork || REST, RADIUS, NETCONF || File, MySQL, PostgreSQL, Cassandra || Also DNS. Supersedes dhcpd.
|-
|  ||  ||  ||  || Pi-hole#FTL Integrated Web interface || ? || SQLite || Component of the Pi-hole project. Fork of dnsmasq.
|-
| systemd-networkd ||  ||  ||  ||  || D-Bus || File || Installed with systemd.
|-
|}

A comparison of available DNS servers can be found in Domain name resolution#DNS servers.

## dnsmasq
To use dnsmasq as DNS server, and optionally DHCP server, for the LAN, install the  package.

The default configuration already enables its DNS server, see dnsmasq#Configuration for options.

For this router example, dnsmasq can to be configured to be a DHCP server with a configuration similar to the following:

See dnsmasq#DHCP server for other options. For example, you can also add "static" DHCP leases, i.e. assign an IP-address to the MAC-address of a computer on the LAN. This way, whenever the computer requests a new lease, it will get the same IP. That is very useful for network servers with a DNS record. You can also deny certain MACs from obtaining an IP.

Now start and enable the .

## systemd-networkd
To use systemd-networkd instead of dnsmasq as DHCP server, add a  section to the configuration file for the  interface. See systemd-networkd#DHCP server for the available options.

To make systemd-resolved answer DNS requests on the routers interfaces, their addresses have to be added as described in systemd-resolved#Additional listening interfaces.

## Connection sharing
Time to tie the two network interfaces together.

## Manual
First of all, we need to allow packets to hop from one network interface to the other. For this, one needs to have packet forwarding enabled in kernel via . See Internet sharing#Enable packet forwarding for details.

Assuming  is set correctly (i.e. is ), packets still need to be properly sent and received. Hence, it is necessary to translate the IP addresses between the outward facing network and the subnet used locally. The technique is called masquerading . We also need two forwarding rules to keep connections going and enable LAN to WAN forwarding. For this task, we are going to use iptables.

Refer to the section Internet sharing#Enable NAT for how to masquerade the  interface and packages from  to . Afterwards persist the newly added rules via , see iptables#Configuration and usage for details.

Start and enable .  The router should now be fully functional and route your traffic. Since it is facing the public Internet, it makes sense to additionally secure it using a Simple stateful firewall.

## With systemd-networkd
Amend or create the previously discussed network configuration for  to include the  option in the  section. This configuration will implicitly enable packet forwarding on all interfaces, see . See systemd-networkd#DHCP server for an example configuration.

## Connection sharing with shorewall
See Shorewall for a detailed configuration guide.

## IPv6 tips
Useful reading: IPv6 and the wikipedia:IPv6.

## Unique Local Addresses
You can use your router in IPv6 mode even if you do not have an IPv6 address from your ISP. Unless you disable IPv6, all interfaces should have been assigned a unique  address.

For internal networking the block  has been reserved. These addresses are guaranteed to be unique and non-routable from the open Internet. Addresses that belong to the  block are called Unique Local Addresses. To get started generate a ULA /64 blocks to use in your network. An algorithm is described at, for example, RFC 4193 section 3.2.2. For this example we will use . Firstly, we must assign a static IPv6 on the internal interface. Modify the  we created above to include the following line:

  Address6=('fd00:aaaa:bbbb:cccc::1/64')

This will add the ULA to the internal interface. As far as the router goes, this is all you need to configure.

## Global Unicast Addresses
If your ISP or WAN network can access the IPv6 Internet, you can additionally assign global link addresses to your router and propagate them through SLAAC to your internal network. The global unicast prefix is usually either static or provided through prefix delegation.

## Static IPv6 prefix
If your ISP has provided you with a static prefix, then edit  and simply add the IPv6 and the IPv6 prefix (usually /64) you have been provided

  Address6=('2002:1:2:3:4:5:6:7/64')

You can use this in addition to the ULA address described above.

## Acquiring IPv6 prefix via DHCPv6-PD
If your ISP handles IPv6 via prefix delegation, then you can follow the instructions in the IPv6#Prefix delegation (DHCPv6-PD) on how to properly configure your router. Following the conventions of this article, the WAN interface is  (or  if you are connecting through PPPoE) and the LAN interface is .

## Router Advertisement and Stateless Autoconfiguration (SLAAC)
To properly hand out IPv6s to the network clients, we will need to use an advertising daemon. Follow the details of the main IPv6 article on how to set up . According to this guide's convention, the LAN-facing interface is . You can either advertise all prefixes or choose which prefixes will be assigned to the local network.

## Optional additions
## UPnP
The above configuration of shorewall does not include UPnP support. Use of UPnP is discouraged as it may make the gateway vulnerable to attacks from within the LAN. However, some applications require this to function correctly.

To enable UPnP on your router, you need to install an UPnP Internet Gateway Device (IGD) protocol daemon. To get it, install the  package.

Read the Shorewall guide on UPnP for more information.

## Remote administration
OpenSSH can be used to administer your router remotely. This is useful for running it in headless mode (no monitor or input devices).

## Caching web proxy
See Squid for the setup of a web proxy to speed up browsing and/or adding an extra layer of security.

## Time server
To use the router as a time server, see System time#Time synchronization for available Network Time Protocol (NTP) server implementations.

Then, configure shorewall or iptables to allow NTP traffic in and out.

## Content filtering
Install and configure Privoxy if you need a content filtering solution.

## Traffic shaping
Traffic shaping is very useful, especially when you are not the only one on the LAN. The idea is to assign a priority to different types of traffic. Interactive traffic (ssh, online gaming) probably needs the highest priority, while P2P traffic can do with the lowest. Then there is everything in between.

## Traffic shaping with shorewall
See Shorewall#Traffic shaping.
