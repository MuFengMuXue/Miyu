# IPv6

In Arch Linux, IPv6 is enabled by default.

The tldp Linux+IPv6-HOWTO (or  from ) article is older, and less maintained. Yet it attempts to cover many topics that are mentioned in this article, starts from the basics, and advances in a slower pace. It also has many command line examples. Beginners might want to read or skim it before reading this wiki article.

## Static configuration
Sometimes, using a static address can improve security. For example, if your local router uses Neighbor Discovery or radvd (RFC 2461), your interface will automatically be assigned an address based on its MAC address (using IPv6's Stateless Autoconfiguration), unless a privacy extension or stable private address is enabled. This may be less than ideal for security since it allows a system to be tracked even if the network portion of the IP address changes.

## systemd-networkd
To configure static IPv4 and IPv6 via systemd-networkd, you can do something like this:

 Name=XXXX (for example ens3)

 [Network
 Address=XXX.XX.X.XX/32 (IPv4 address)
 Gateway=10.0.0.1 (IPv4 gateway)
 Address=XXXX:XXXX:X:XXX::2/64 (IPv6 address)
 Gateway=XXXX:XXXX:X:XXX::1 (IPv6 gateway)

The network parameters will be different for everyone, but should be provided by ISP. Create or edit the file in /etc/systemd/network/example.network. Once it's done, you need to restart networkd service. To check IPv4 and IPv6 connection try ping -c3 google.com and ping -6 -c3 google.com.

## netctl
To assign a static IP address using netctl, look at the example profile in . The following lines are important:

 ...
 # For IPv6 static address configuration
 IP6=static
 Address6=('1234:5678:9abc:def::1/64' '1234:3456::123/96')
 Routes6=('abcd::1234')
 Gateway6='1234:0:123::abcd'

## Neighbor discovery
Pinging the multicast address  results in all hosts in link-local scope responding. An interface has to be specified:

 $ ping ff02::1%eth0

After that, you can get a list of all the IPv6 neighbors in the local network with:

 $ ip -6 neigh

With a ping to the multicast address  only routers will respond.

If you add an option , link-local hosts will respond with their link-global scope addresses. The interface can be omitted in this case:

 $ ping -I 2001:4f8:fff6::21 ff02::1

To ping everyone on all interfaces, and announce your address to everyone, use a script.

 #!/usr/bin/bash
 declare -a l_ifs
 readarray l_ifs }} ! Variable name
! Description
|-
|
| Preference for Privacy Extensions (RFC3041).  1: enable and prefer temp addresses over public addresses.
|-
|
| Preferred temp address lifetime in seconds. Note the wrong spelling has to be used.
|-
|
| Maximum temp address lifetime in seconds.
|-
|}

## dhcpcd
dhcpcd's default configuration includes the option , which enables "Stable Private IPv6 Addresses instead of hardware based ones", implementing RFC 7217. Therefore, it is not necessary to change anything, except if it is desired to change of IPv6 address more often than each time the system is connected to a new network. Set it to  for a stable address.

## NetworkManager
The use of IPv6 Privacy Extensions in NetworkManager can be controlled with the  setting in  or in the connection's profile. If it is not set globally nor per-connection, NetworkManager will fall back to reading .

To explicitly enable IPv6 Privacy Extensions by default, add these lines to :

Apply the configuration and reconnect to all active connections.

To control the use of IPv6 Privacy Extensions for individual NetworkManager-managed connections, edit the desired connection keyfile in  and append to its  section the key-value pair :

Reload the connection and reconnect to it afterwards.

## systemd-networkd
systemd-networkd does not enable IPv6 privacy extensions by default. To enable them set  in the  section in per-connection .network files or globally with a configuration file in . E.g.:

systemd-networkd does not honor the sysctl setting  unless the  option is set to .

Other options for the IPv6 Privacy Extensions like  and  are honored, however.

See systemd-networkd and  for details.

## ConnMan
Use the following setting in your service file:

See ConnMan for details.

## Stable private addresses
Another option is a stable private IP address (RFC 7217). This allows for IPs that are stable within a network without exposing the MAC address of the interface.

In order to have the kernel generate a key (for , for example) we can set:

 # sysctl net.ipv6.conf.wlan0.addr_gen_mode=3

Bring the interface down and up and you should see  next to each IPv6 address after running . The kernel has generated a 128-bit secret for generating ip addresses for this interface, to see it run . We are going to persist this value so add the following lines to :

 # Enable IPv6 stable privacy mode
 net.ipv6.conf.wlan0.stable_secret = output_from_previous_command
 net.ipv6.conf.wlan0.addr_gen_mode = 2

## NetworkManager
The above settings are not honored by NetworkManager, but NetworkManager uses stable private addresses by default.[https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/blob/nm-1-12/NEWS#L367-369=== systemd-networkd ===

The above settings are not honored by systemd-networkd. To ensure stable private addresses are always used, you can set:

 [IPv6AcceptRA
 Token=prefixstable

The above tells systemd-networkd to use a secret derived from the machine ID. You can also specify a secret yourself or even apply the setting to only specific prefixes appearing in Router Advertisement messages. See  for details.

You can also generate stable private link-local addresses if desired:

 IPv6LinkLocalAddressGenerationMode=stable-privacy

## IPv6 and PPPoE
The standard tool for PPPoE, , provides support for IPv6 on PPPoE as long as your ISP and your modem support it. Just add the following to

 +ipv6

If you are using netctl for PPPoE then just add the following to your netctl configuration instead:

 PPPoEIP6=yes

## Prefix delegation (DHCPv6-PD)
Prefix delegation is a common IPv6 deployment technique used by many ISPs. It is a method of assigning a network prefix to a user site (i.e. local network). A router can be configured to assign different network prefixes to various subnetworks. The ISP hands out a network prefix using DHCPv6 (usually a  or ) and a dhcp client assigns the prefixes to the local network. For a simple two interface gateway it practically assigns an IPv6 prefix to the interface connected to the local network from an address acquired through the interface connected to WAN (or a pseudo-interface such as ppp).

DHCPv6 requires the client to receive incoming connections on port 546 UDP. For an nftables-based firewall, that can be configured with one line in the input chain in :

 table inet filter {
   chain input {
     udp dport dhcpv6-client accept
     ...
   }
 ...
 }

## With dhcpcd
dhcpcd apart from IPv4 dhcp support also provides a fairly complete implementation of the DHCPv6 client standard which includes DHCPv6-PD. If you are using  edit . You might already be using dhcpcd for IPv4 so just update your existing configuration.

This configuration will ask for a prefix from WAN interface () and delegate it to the internal interface ().
In the event that a  range is issued, you will need to use the 2nd  that is commented out instead.
It will also disable router solicitations on all interfaces except for the WAN interface ().

## With WIDE-DHCPv6
[https://wide-dhcpv6.sourceforge.net/ WIDE-DHCPv6 is an open-source implementation of Dynamic Host Configuration Protocol for IPv6 (DHCPv6) originally developed by the KAME project. It can be installed with .

If you are using wide-dhcpv6, edit

{{bc|
# use the interface connected to your WAN
interface WAN {
  send ia-pd 0;
};

id-assoc pd 0 {
  # use the interface connected to your LAN
  prefix-interface LAN {
    sla-id 1;
    sla-len 8;
  };
};
}}

The wide-dhcpv6 client can be started/enabled using the  systemd unit file, where  is the interface name in the configuration file, e.g. for a interface name "WAN" use .

## systemd-networkd
Configure both your upstream (wan) and downstream (lan) interface. This will enable DHCPv6-PD on the interface where the DHCPv6 client is running. The delegated prefixes are distributed by IPv6 Router Advertisement on the downstream network.

## Other clients
dhclient can also request a prefix, but assigning that prefix, or parts of that prefix to interfaces must be done using a dhclient exit script. For example: https://github.com/jaymzh/v6-gw-scripts/blob/master/dhclient-ipv6.

## NAT64
Wikipedia:NAT64 is the IPv6 transition mechanism where IPv6 only hosts are able to communicate with IPv4 hosts using NAT.

Linux kernel does not support NAT64 natively but there are several packages to add support for NAT64.

*
*

## Disable IPv4
There are very few reasons to disable either IPv4 or the IPv6 address stack on Linux, dual-stacked Linux has worked just fine since 1999. But as global IPv6 adoption grows, IPv6-only networks have become increasingly common. NAT64 and DNS64 are commonly used transition mechanisms for IPv6-only networks to communicate with legacy IPv4-only networks.

Common reasons to disable IPv4 networking:

* You know your service provider is an IPv6-only network.
* Your ISP does Carrier Grade NAT (CGN or CGNAT) and your IPv4 performance is inferior to native IPv6.
* You are a network engineer deploying NAT64 in your Autonomous System (AS).

## Disable IPv4 in systemd-networkd
To configure an IPv6-only interface in , set  in your network configuration, see example below:

## Disable IPv6
For some ISPsthe IPv6 traffic is slower than the IPv4 one: if you can confirm with certainty you are affected by such issues, disabling IPv6 may speed up your network speeds.

This should not be done blindly: for most users, IPv4-only networking will degrade performance behind Carrier-grade NAT and hamper their usage of P2P or WebRTC applications (e.g. some games). Instead, configuring IPv4 to be preferred over IPv6 is the best of both worlds.

## Disable functionality
Adding  to the kernel line disables the whole [https://docs.kernel.org/networking/ipv6.html IPv6 stack, which is likely what you want if you are experiencing issues. See Kernel parameters for more information.

Alternatively, adding  instead will keep the IPv6 stack functional but will not assign IPv6 addresses to any of your network devices.

## sysctl
One can disable the IPv6 stack for all or specific network interfaces by adding the following sysctl configuration to :

 # Disable IPv6
 net.ipv6.conf.all.disable_ipv6 = 1
 net.ipv6.conf.nic0.disable_ipv6 = 1
 ...
 net.ipv6.conf.nicN.disable_ipv6 = 1

This however only works, if one restarts the  after boot, since  starts before the network interfaces are completely configured. On boot one can only set the configuration for ,  and , because they are an internal part of the IPv6 stack.

## systemd unit
If one wants to disable the IPv6 stack for all network interfaces on boot, with the ability to easily enable IPv6 later, a systemd unit which runs after the network manager is necessary.

A unit for systemd-networkd would look like this:

After enabling this unit, any start or restart of systemd-networkd will enforce the  value of the IPv6 stack status on all network interfaces.

The  value can be set on boot with #sysctl.

To adjust this unit for other network manager one needs to replace all occurrences of  with the configuration unit of their network manager.

## Other programs
Disabling IPv6 functionality in the kernel does not prevent other programs from trying to use IPv6. In most cases, this is completely harmless, but if you find yourself having issues with that program, you should consult the program's manual pages for a way to disable that functionality.

## dhcpcd
dhcpcd will continue to harmlessly attempt to perform IPv6 router solicitation. To disable this, as stated in the  man page, add the following to :

 noipv6rs
 noipv6

## NetworkManager
To disable IPv6 in NetworkManager, right click the network status icon, and select Edit Connections > Wired > Network name > Edit > IPv6 Settings > Method > Ignore/Disabled. Then click Save.

This can also be done as:

 # nmcli connection modify ConnectionName ipv6.method "disabled"

Followed by a restart of the network connection:

 # nmcli connection up ConnectionName

To confirm the settings have been applied, use  and check no inet6 entry is displayed. Alternatively,  should have the value 1.

## ntpd
Following advice in systemd#Drop-in files, edit  to define how systemd starts it.

This will create a drop-in snippet that will be run instead of the default . The  flag prevents IPv6 from being used by the ntp daemon. Put the following into the drop-in snippet:

 ExecStart=
 ExecStart=/usr/bin/ntpd -4 -g -u ntp:ntp

which first clears the previous , and then replaces it with one that includes the  flag.

## GnuPG
Disable IPv6 in the dirmngrs configuration file:

Restart the  user unit afterwards.

## sshd
Ensure sshd is using IPv4 by adding the following to :

And restart the .

## systemd-timesyncd
On occasion systemd-timesyncd will attempt to query an IPv6 timeserver even when IPv6 has been disabled. This can result in the system clock not being updated and the journal showing an error similar to:

 systemd-timesyncd[336: Failed to set up connection socket: Address family not supported by protocol

The unit status of  will show an attempt to connect with an IPv6 address in its Status entry, similar to:

 Status: "Connecting to time server (2.pool.ntp.org)"

Per , only the "2." ntp.org pools serve IPv6. So to prevent this remove  and  from the NTP and FallbackNTP entries in  file.

## systemd-networkd
networkd supports disabling IPv6 on a per-interface basis. When a network unit's  section has either  or , networkd will not try to configure IPv6 on the matching interfaces.

Note however that even when using the above option, networkd will still be expecting to receive router advertisements if IPv6 is not disabled globally. If IPv6 traffic is not being received by the interface (e.g. due to sysctl or ip6tables settings), it will remain in the configuring state and potentially cause timeouts for services waiting for the network to be fully configured. To avoid this, the  option should also be set in the  section.

## Prefer IPv4 over IPv6
Uncomment the following line in :

 #
 #    For sites which prefer IPv4 connections change the last line to
 #
 precedence ::ffff:0:0/96  100
