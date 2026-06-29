# Network configuration

This article describes how to configure network connections on OSI layer 3 and above. Medium-specifics are handled in the /Ethernet and /Wireless subpages.

## Check the connection
To troubleshoot a network connection, go through the following conditions and ensure that you meet them:

# Your network interface is listed and enabled. Otherwise, check the device driver – see /Ethernet#Device driver or /Wireless#Device driver.
# You are connected to the network. The cable is plugged in or you are connected to the wireless LAN.
# Your network interface has an IP address.
# Your routing table is correctly set up.
# You can ping a local IP address (e.g. your default gateway).
# You can ping a public IP address (e.g. , which is a DNS server operated by the Quad9 Foundation and is a convenient address to test with).
# Check if you can resolve domain names (e.g. ).

## Ping
ping is used to test if you can reach a host.

For every reply received, the ping utility will print a line like the above until you interrupt () it interactively. For more information see the  manual. Note that computers can be configured not to respond to ICMP echo requests. If you receive an error message (see ping error indications) or no reply, this may be related to incomplete configuration, but also your default gateway or your Internet Service Provider (ISP). You can run a traceroute to further diagnose the route to the host.

## Network management
To set up a network connection, go through the following steps:

# Ensure your network interface is listed and enabled.
# Connect to the network. Plug in the Ethernet cable or connect to the wireless LAN.
# Configure your network connection:
#* Most networks use the Dynamic Host Configuration Protocol for network configuration. Clients can automatically obtain a dynamic or static IP address from the DHCP server via a standalone DHCP client or using a network manager.
#* If the network does not have a DHCP server, you can configure a static IP address, routing table and DNS servers manually for each client. See #Static IP address for details.

## Manual
## iproute2
iproute2 is a dependency of the  meta package and provides the  command-line interface, used to manage network interfaces, IP addresses and the routing table. Be aware that configuration made using  will be lost after a reboot. For persistent configuration, you can automate ip commands using scripts and systemd units. Also note that  commands can generally be abbreviated, for clarity they are however spelled out in this article.

## Static IP address
A static IP address can be configured with most standard network managers and also dhcpcd.

To manually configure a static IP address, add an IP address as described in #IP addresses, set up your routing table and configure your DNS servers.

## IP addresses
IP addresses are managed using .

List IP addresses:

 $ ip address show

Add an IP address to an interface:

 # ip address add address/prefix_len broadcast + dev interface

:Note that:

:* the address is given in CIDR notation to also supply a subnet mask
:*  is a special symbol that makes  derive the broadcast address from the IP address and the subnet mask

:

Delete an IP address from an interface:

 # ip address del address/prefix_len dev interface

Delete all addresses matching a criteria, e.g. of a specific interface:

 # ip address flush dev interface

## Routing table
The routing table is used to determine if you can reach an IP address directly or what gateway (router) you should use. If no other route matches the IP address, the default gateway is used.

The routing table is managed using .

PREFIX is either a CIDR notation or  for the default gateway.

List IPv4 routes:

 $ ip route show

List IPv6 routes:

 $ ip -6 route show

Add a route:

 # ip route add PREFIX via address dev interface

Delete a route:

 # ip route del PREFIX via address dev interface

## Automatic
Automatic network configuration is accomplished using Dynamic Host Configuration Protocol (DHCP). The network's DHCP server provides IP address(es), the default gateway IP address(es) and optionally also DNS name servers upon request
from the DHCP client.

See Router#DNS and DHCP for a DHCP server comparison table.

## Network managers
A network manager lets you manage network connection settings in so called network profiles to facilitate switching networks.

{| class="wikitable sortable"
! rowspan="2"| Software
! colspan="3"| Connection type
! rowspan="2"| Wireless authentication
! colspan="3"| IP address, route and DNS management
! colspan="3"| Interface
|-
! Ethernet
! PPPoE
! Mobile broadband
! Static IP
! DHCP client
! Domain name resolution
! CLI
! TUI
! GUI
|-
! 1
|  ||  ||  || 2 ||  ||  ||  (writes ) ||  ||  ||
|-
! dhcpcd
|  ||  ||  ||  ||  ||  ||  ||  ||  ||
|-
! ConnMan
|  ||  ||  (via ) ||  (via  or iwd) ||  ||  ||  (runs a builtin resolver and writes ) ||  ||  ||
|-
! netctl
|  ||  ||  (via ) ||  (via ) ||  ||  ||  ||  ||  ||
|-
! NetworkManager
|  ||  ||  ||  (via  or iwd) ||  ||  ||  ||  ||  ||
|-
! style="white-space: nowrap;" | systemd-networkd
|  ||  ||  || 2 ||  ||  ||  (uses systemd-resolved) ||  ||  ||
|-
! wpa_supplicant
|  ||  ||  ||  || colspan="3"  ||  ||  ||
|-
! iwd
|  ||  ||  ||  ||  ||  ||  ||  ||  ||
|}

# No longer maintained as of early 2022. ISC advises no longer using it in production.
# Wireless authentication can be configured separately with wpa_supplicant or iwd.
# Wireless authentication must be configured separately with wpa_supplicant.
# Only Wi-Fi connections can be managed.
# NetworkManager does not use dhcpcd for DHCPv6, see NetworkManager#DHCP client.

## Network interfaces
Network interfaces are managed by udev and configured by  files. The default configuration assigns names to your network interface controllers using [https://systemd.io/PREDICTABLE_INTERFACE_NAMES/ Predictable Network Interface Names, which prefixes interfaces names with  (wired/Ethernet),  (wireless/WLAN), or  (mobile broadband/WWAN). See .

## Listing network interfaces
Both wired and wireless interface names can be found via  or . Note that  is the virtual loopback interface and not used in making network connections.

Wireless device names can also be retrieved using . See also /Wireless#Get the name of the interface.

If your network interface is not listed, make sure your device driver was loaded successfully. See /Ethernet#Device driver or /Wireless#Device driver.

## Enabling and disabling network interfaces
Network interfaces can be enabled or disabled using , see .

To check the status of the interface :

The  in  is what indicates the interface is up, not the later .

## Change interface name
You can change the device name by defining the name manually with a  file. The file must be ordered lexicographically before , for example:

Alternatively, a udev rule can be used:

{{hc|/etc/udev/rules.d/10-network.rules|2=
SUBSYSTEM=="net", ACTION=="add", ATTR{address}=="aa:bb:cc:dd:ee:ff", NAME="net0"
}}

These rules will be applied automatically at boot. To apply the change immediately, do a manual trigger of the udev rule on the  subsystem:

 # udevadm trigger --verbose --subsystem-match=net --action=add

If you want to run a test on the changes made,  can be of help.

If the network card has a dynamic MAC, you can use  (which can be checked using ):

Or, use a udev rule with :

To get the  of all currently-connected devices, see where the symlinks in  lead. For example:

The device path should match both the new and old device name, since the rule may be executed more than once on bootup. For example, in the given rule,  would be wrong since it will stop matching once the name is changed to . Only the system-default rule will fire the second time around, causing the name to be changed back.

If you are using a USB network device (e.g. Android phone tethering) that has a dynamic MAC address and you want to be able to use different USB ports, you could use a rule that matched depending on vendor and model ID instead:

or

{{hc|/etc/udev/rules.d/10-network.rules|2=
SUBSYSTEM=="net", ACTION=="add", ATTRS{idVendor}=="12ab", ATTRS{idProduct}=="3cd4", NAME="net2"
}}

## Revert to traditional interface names
If you would prefer to retain traditional interface names such as , Predictable Network Interface Names can be disabled by changing the default  for udev's  built-in:

Alternatively,  can be completely disabled by masking the corresponding udev rule:

 # ln -s /dev/null /etc/udev/rules.d/80-net-setup-link.rules

or by adding  to the kernel parameters.

## Set device MTU and queue length
You can change the device MTU and queue length by defining manually with a  config. For example:

Or through a udev rule:

{{hc|/etc/udev/rules.d/10-network.rules|2=
ACTION=="add", SUBSYSTEM=="net", KERNEL=="wl*", ATTR{mtu}="1500", ATTR{tx_queue_len}="2000"
}}

: Using a value larger than 1500 (so called jumbo frames) can significantly speed up your network transfers. Note that all network interfaces, including switches in the local network, must support the same MTU in order to use jumbo frames. For PPPoE, the MTU should not be larger than 1492. You can also set MTU via .

: Small value for slower devices with a high latency like modem links and ISDN. High value is recommended for server connected over the high-speed internet connections that perform large data transfers.

## Set the hostname
A hostname is a unique name created to identify a machine on a network, configured in —see  and  for details. The file can contain the system's domain name, if any. To set the hostname, edit  to include a single line with :

Alternatively, using :

 # hostnamectl hostname yourhostname

To temporarily set the hostname (until reboot), use  from :

 # hostname yourhostname

To set the "pretty" hostname and other machine metadata, see .

## Local network hostname resolution
To make your machine accessible in your LAN via its hostname you can:

* edit the  file for every device in your LAN, see
* set up a DNS server to resolve your hostname and make the LAN devices use it (e.g. via DHCP)
* or the easy way: use a Zero-configuration networking service:
** Hostname resolution via Microsoft's NetBIOS. Provided by Samba on Linux. It only requires the . Computers running Windows, macOS, or Linux with  running, will be able to find your machine.
** Hostname resolution via mDNS. Provided by either  with Avahi (see Avahi#Hostname resolution for setup details) or systemd-resolved. Computers running macOS, or Linux with Avahi or systemd-resolved running, will be able to find your machine. The older Win32 API does not support mDNS, which may prevent some older Windows applications from accessing your device.

## Tips and tricks
## Bonding or LAG
See netctl or systemd-networkd, or Wireless bonding.

## IP address aliasing
IP aliasing is the process of adding more than one IP address to a network interface. With this, one node on a network can have multiple connections to a network, each serving a different purpose. Typical uses are virtual hosting of Web and FTP servers, or reorganizing servers without having to update any other machines (this is especially useful for nameservers).

## Example
To manually set an alias, for some NIC, use  to execute

 # ip addr add 192.168.2.101/24 dev enp2s0 label enp2s0:1

To remove a given alias execute

 # ip addr del 192.168.2.101/24 dev enp2s0:1

Packets destined for a subnet will use the primary alias by default. If the destination IP is within a subnet of a secondary alias, then the source IP is set respectively. Consider the case where there is more than one NIC, the default routes can be listed with .

## Promiscuous mode
Toggling promiscuous mode will make a (wireless) NIC forward all traffic it receives to the OS for further processing. This is opposite to "normal mode" where a NIC will drop frames it is not intended to receive. It is most often used for advanced network troubleshooting and packet sniffing.

If you want to enable promiscuous mode on interface , enable .

## Investigate sockets
ss is a utility to investigate network ports and is part of the  package. It has a similar functionality to the deprecated netstat utility.

Common usage includes:

Display all TCP Sockets with service names:
 $ ss -at

Display all TCP Sockets with port numbers:
 $ ss -atn

Display all UDP Sockets:
 $ ss -au

For more information see .

## Troubleshooting
## The TCP window scaling problem
TCP packets contain a "window" value in their headers indicating how much data the other host may send in return. This value is represented with only 16 bits, hence the window size is at most 64KiB. TCP packets are cached for a while (they have to be reordered), and as memory is (or used to be) limited, one host could easily run out of it.

Back in 1992, as more and more memory became available, RFC:1323 was written to improve the situation: Window Scaling. The "window" value, provided in all packets, will be modified by a Scale Factor defined once, at the very beginning of the connection. That 8-bit Scale Factor allows the Window to be up to 32 times higher than the initial 64KiB.

It appears that some broken routers and firewalls on the Internet are rewriting the Scale Factor to 0 which causes misunderstandings between hosts. The Linux kernel 2.6.17 introduced a new calculation scheme generating higher Scale Factors, virtually making the aftermaths of the broken routers and firewalls more visible.

The resulting connection is at best very slow or broken.

## How to diagnose the problem
First of all, let us make it clear: this problem is odd. In some cases, you will not be able to use TCP connections (HTTP, FTP, ...) at all and in others, you will be able to communicate with some hosts (very few).

When you have this problem, the output from dmesg is okay, logs are clean and  will report normal status... and actually everything appears normal.

If you cannot browse any website, but you can ping some random hosts, chances are great that you are experiencing this problem: ping uses ICMP and is not affected by TCP problems.

You can try to use Wireshark. You might see successful UDP and ICMP communications but unsuccessful TCP communications (only to foreign hosts).

## Ways of fixing it
## Bad
To fix it the bad way, you can change the  value, on which Scale Factor calculation is based. Although it should work for most hosts, it is not guaranteed, especially for very distant ones.

 # sysctl -w net.ipv4.tcp_rmem="4096 87380 174760"

## Good
Simply disable Window Scaling. Since Window Scaling is a nice TCP feature, it may be uncomfortable to disable it, especially if you cannot fix the broken router. There are several ways to disable Window Scaling, and it seems that the most bulletproof way (which will work with most kernels) is to add the following line to  (see also sysctl):

 net.ipv4.tcp_window_scaling = 0

## Best
This problem is caused by broken routers/firewalls, so let us change them. Some users have reported that the broken router was their very own DSL router.

## More about it
This section is based on the LWN article TCP window scaling and broken routers and an archived Kernel Trap article: Window Scaling on the Internet.

There are also several relevant threads on the LKML.

## local hostname is resolved over the network
 (an NSS module provided by systemd and enabled by default in ) provides  and the local hostname resolution to an IP address. Some software may, however, still instead read  directly; see [https://bugzilla.mozilla.org/show_bug.cgi?id=87717#c55 for examples.

To prevent such software from unsafely resolving the local hostname over the network, add an entry for it to the  file:

For a system with a permanent IP address, replace  with that permanent IP address. For a system with a fully qualified domain name, insert the fully qualified domain name before the hostname (see the following link for the reasoning). For example:
