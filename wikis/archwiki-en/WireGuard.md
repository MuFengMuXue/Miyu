# WireGuard

From the WireGuard project homepage:
:WireGuard is an extremely simple yet fast and modern VPN that utilizes state-of-the-art cryptography. It aims to be faster, simpler, leaner, and more useful than IPsec, while avoiding the massive headache. It intends to be considerably more performant than OpenVPN. WireGuard is designed as a general purpose VPN for running on embedded interfaces and super computers alike, fit for many different circumstances. Initially released for the Linux kernel, it is now cross-platform (Windows, macOS, BSD, iOS, Android) and widely deployable.

A rough introduction to the main concepts used in this article can be found on WireGuard's project homepage. WireGuard has been included in the Linux kernel since late 2019.

## Installation
Install the  package for userspace utilities.

Alternatively, various network managers provide support for WireGuard, provided that peer keys are available. See #Persistent configuration for details.

## Graphical clients
*
*

## Command-line tools
*
*
*

## Usage
The commands below demonstrate how to set up a basic tunnel between two or more peers with the following settings:

{| class="wikitable"
! rowspan="2" |
! colspan="3" | External (public) addresses
! colspan="2" | Internal IP addresses
! rowspan="2" | Port
|-
! Domain name
! IPv4 address
! IPv6 address
! IPv4 address
! IPv6 address
|-
! Peer A
|
| 198.51.100.101
| 2001:db8:a85b:70a:ffd4:ec1b:4650:a001
| 10.0.0.1/24
| fdc9:281f:04d7:9ee9::1/64
| UDP/51871
|-
! Peer B
| peer-b.example
| 203.0.113.102
| 2001:db8:40f0:147a:80ad:3e88:f8e9:b002
| 10.0.0.2/24
| fdc9:281f:04d7:9ee9::2/64
| UDP/51902
|-
! Peer C
|
| dynamic
| dynamic
| 10.0.0.3/24
| fdc9:281f:04d7:9ee9::3/64
| UDP/51993
|}

The external addresses should already exist. For example, if ICMP echo requests are not blocked, peer A should be able to ping peer B via its public IP address(es) and vice versa.

The internal addresses will be new addresses, created either manually using the  utility or by network management software, which will be used internally within the new WireGuard network. The following examples will use 10.0.0.0/24 and fdc9:281f:04d7:9ee9::/64 as the internal network. The  and  in the IP addresses is the CIDR.

## Key generation
Create a private and public key for each peer. If connecting dozens of peers optionally consider a vanity keypair to personalize the Base64 encoded public key string. See #Vanity keys.

To create a private key run:

 $ (umask 0077; wg genkey > peer_A.key)

To create a public key:

 $ wg pubkey  peer_A.pub

Alternatively, do this all at once:

 $ wg genkey | (umask 0077 && tee peer_A.key) | wg pubkey > peer_A.pub

One can also generate a pre-shared key to add an additional layer of symmetric-key cryptography to be mixed into the already existing public-key cryptography, for post-quantum resistance. A pre-shared key should be generated for each peer pair and should not be reused. For example, three interconnected peers, A, B, and, C will need three separate pre-shared keys, one for each peer pair.

Generate a pre-shared key for each peer pair using the following command (make sure to use  for this as well):

 $ wg genpsk > peer_A-peer_B.psk
 $ wg genpsk > peer_A-peer_C.psk
 $ wg genpsk > peer_B-peer_C.psk

## Vanity keys
Currently, WireGuard does not support comments or attaching human-memorable names to keys. This makes identifying the key's owner difficult particularly when multiple keys are in use. One solution is to generate a public key that contains some familiar characters (perhaps the first few letters of the owner's name or of the hostname etc.). , or alternatively , do this.

For example:

## Manual configuration
## Peer setup
Manual setup is accomplished by using  and .

Peer A setup:

In this example, peer A will listen on UDP port 51871 and will accept connection from peers B and C.

 # ip link add dev wg0 type wireguard
 # ip addr add 10.0.0.1/24 dev wg0
 # ip addr add fdc9:281f:04d7:9ee9::1/64 dev wg0
 # wg set wg0 listen-port 51871 private-key /path/to/peer_A.key
 # wg set wg0 peer PEER_B_PUBLIC_KEY preshared-key /path/to/peer_A-peer_B.psk endpoint peer-b.example:51902 allowed-ips 10.0.0.2/32,fdc9:281f:04d7:9ee9::2/128
 # wg set wg0 peer PEER_C_PUBLIC_KEY preshared-key /path/to/peer_A-peer_C.psk allowed-ips 10.0.0.3/32,fdc9:281f:04d7:9ee9::3/128
 # ip link set wg0 up

 should be the contents of .

The keyword  is a list of addresses that will get routed to the peer. Make sure to specify at least one address range that contains the WireGuard connection's internal IP address(es).

Peer B setup:

 # ip link add dev wg0 type wireguard
 # ip addr add 10.0.0.2/24 dev wg0
 # ip addr add fdc9:281f:04d7:9ee9::2/64 dev wg0
 # wg set wg0 listen-port 51902 private-key /path/to/peer_B.key
 # wg set wg0 peer PEER_A_PUBLIC_KEY preshared-key /path/to/peer_A-peer_B.psk endpoint 198.51.100.101:51871 allowed-ips 10.0.0.1/32,fdc9:281f:04d7:9ee9::1/128
 # wg set wg0 peer PEER_C_PUBLIC_KEY preshared-key /path/to/peer_B-peer_C.psk allowed-ips 10.0.0.3/32,fdc9:281f:04d7:9ee9::3/128
 # ip link set wg0 up

Peer C setup:

 # ip link add dev wg0 type wireguard
 # ip addr add 10.0.0.3/24 dev wg0
 # ip addr add fdc9:281f:04d7:9ee9::3/64 dev wg0
 # wg set wg0 listen-port 51993 private-key /path/to/peer_C.key
 # wg set wg0 peer PEER_A_PUBLIC_KEY preshared-key /path/to/peer_A-peer_C.psk endpoint 198.51.100.101:51871 allowed-ips 10.0.0.1/32,fdc9:281f:04d7:9ee9::1/128
 # wg set wg0 peer PEER_B_PUBLIC_KEY preshared-key /path/to/peer_B-peer_C.psk endpoint peer-b.example:51902 allowed-ips 10.0.0.2/32,fdc9:281f:04d7:9ee9::2/128
 # ip link set wg0 up

## Additional routes
To establish connections more complicated than point-to-point, additional setup is necessary.

## Point-to-site
To access the network of a peer, specify the network subnet(s) in  in the configuration of the peers who should be able to connect to it. E.g. .

Make sure to also set up the routing table with . E.g.:

 # ip route add 192.168.35.0/24 dev wg0
 # ip route add fd7b:d0bd:7a6e::/64 dev wg0

## Site-to-point
If the intent is to connect a device to a network with WireGuard peer(s), set up routes on each device so they know that the peer(s) are reachable via the device.

After that, enable IP forwarding on the peer through which other devices on the network will connect to WireGuard peer(s).

## Site-to-site
To connect two (or more) networks, apply both #Point-to-site and #Site-to-point on all sites.

## Routing all traffic over WireGuard
To route everything over the WireGuard tunnel, use:

 # ip route add default dev wg0 table 2468
 # wg set wg0 fwmark 1234
 # ip rule add not fwmark 1234 table 2468 pref 10

In the first line, the default route is added to an alternative routing table (table 2468). The only purpose of this alternative routing table is to hand packets over to the wg0 interface.

In the second line, all outgoing packets handled by the wg0 interface are marked with a firewall mark.

In the third line, packets lacking this firewall mark are directed to the alternative routing table 2468, which routes them to the wg0 interface.  indicates that this rule has priority 10. To list all rules with their corresponding priority, use . These rules determine which routing table will be employed for a certain packets.

This implementation's main strength lies in its avoidance of using any endpoint. This is advantageous because WireGuard endpoints can roam. It is possible to define WireGuard peers without an endpoint.

The local access network will be inaccessible in this implementation. To whitelist LAN use:

 # ip rule add suppress_prefixlength 0 table main pref 5

It's fairly straightforward to add things to the whitelist using . For instance, to give a certain user permission to send queries outside the WireGuard tunnel, use:

 # ip rule add uidrange 955-955 table main pref 5

955 is the user ID of the user. The user IDs of all users can be found in .

## DNS
To use a peer as a DNS server, add its WireGuard tunnel IP address(es) to :/etc/resolv.conf. For example, to use peer B as the DNS server:

## Basic checkups
Invoking the  command without parameters will give a quick overview of the current configuration.

As an example, when peer A has been configured we are able to see its identity and its associated peers:

At this point one could reach the end of the tunnel. If the peers do not block ICMP echo requests, try pinging a peer to test the connection between them.

Using ICMPv4:

 $ ping 10.0.0.2

Using ICMPv6:

 $ ping fdc9:281f:04d7:9ee9::2

After transferring some data between peers, the  utility will show additional information:

## Persistent configuration
Persistent configuration can be achieved using , which is shipped with , or using a network manager. Network managers that support WireGuard are systemd-networkd, netctlNetworkManager and ConnMan[https://git.kernel.org/pub/scm/network/connman/connman.git/tree/doc/vpn-config-format.txt.

## wg-quick
 configures WireGuard tunnels using configuration files from .

The current WireGuard configuration can be saved by utilizing the  utility's  command. For example:

 # wg showconf wg0 > /etc/wireguard/wg0.conf

To start a tunnel with a configuration file, use

 # wg-quick up interfacename

or use the systemd service—. To start the tunnel at boot, enable the unit.

Peer A setup:

* To route all traffic through the tunnel to a specific peer, add the default route ( for IPv4 and  for IPv6) to . E.g. . wg-quick will automatically take care of setting up correct routing and fwmarkso that networking still functions.
* To use a peer as a DNS server, set  in the  section. Search domains are also set with the  option. Separate all values in the list with commas.

Peer B setup:

Peer C setup:

## systemd-networkd
systemd-networkd has native support for setting up WireGuard interfaces. An example is provided in the  man page.

Peer A setup:

* To use a peer as a DNS server, specify its WireGuard tunnel's IP address(es) in the .network file using the  option. For search domains use the  option. See  for details.
* To use a peer as the only DNS server set  and  in the  section of .network file's.
* To automatically create routes for everything in , add  to the  or  sections in the .netdev file. Alternatively, additional routes can be specified manually using  sections in the .network file.

Peer B setup:

Peer C setup:

## systemd-networkd: routing all traffic over WireGuard
In this example, Peer B connects to Peer A with a public IP address. Peer B routes all its traffic over the WireGuard tunnel and uses Peer A for handling DNS requests.

Peer A setup

Peer B setup:

In the netdev configuration, the most interesting lines are  and . The RouteTable line specifies that a new routing table with id 1000 is created for the wireguard interface, and no rules are set on the main routing table.

The FirewallMark simply marks all packets send and received by this wireguard interface with the number 0x8888, which can be used to define policy rules on these packets.

We define two routing policies here. For all packets *not* marked with 0x8888 (i.e. all non-wireguard/normal traffic), we specify that the routing table 1000 must be used (which is the wireguard routing table). This rule routes all traffic through wireguard.

We exempt our endpoint with a higher priority by routing it through the main table ( is default).

Exempting specific addresses

In order to exempt specific addresses (such as private LAN addresses) from routing over the WireGuard tunnel, add them to another RoutingPolicyRule with higher priority.

Route for specific user

It may be desirable to route WAN traffic over the tunnel only for a specific user, for example, the transmission user in order to use the tunnel for torrent traffic.

The higher priority rule (30000), matches all traffic generated by the transmission user and routes it through the main table (no wireguard) BUT only using rules with a prefix length larger than 0. This excludes the default catch-all rule. Therefore, only traffic matching specific rules (such as those defining the subnet of your local home network) of the main table are routed through the main table.

The lower priority rule (30001), matches all traffic generated by the transmission user and routes it through table 1000 which is the wireguard table.

Note: these rules are to be put instead of the two rules defined at the start of this section to route all traffic through wireguard.

Testing

Test the proxy with

 # ipv4
 $ curl -4 zx2c4.com/ip

 # ipv6
 $ curl -6 zx2c4.com/ip

Check systemd-networkd log for any error and warning messages.

 $ journalctl -u systemd-networkd.service

Invoke wg command from wireguard-tools.

## Netctl
Netctl has native support for setting up WireGuard interfaces. A typical set of WireGuard netctl profile configuration files would look like this:

Peer A setup:

Peer B setup:

Peer C setup:

Then start and/or enable the wg0 interface on every participating peer as needed, i.e.

 # netctl start wg0

To implement persistent site-to-peer, peer-to-site or site-to-site type of connection with WireGuard and Netctl, just add appropriate  line into the netctl profile configuration file and add this network to  in the WireGuard profile, e.g.  in the  and  in  and then do not forget to enable IP forwarding.

## NetworkManager
NetworkManager has native support for setting up WireGuard interfaces. For all details about WireGuard usage in NetworkManager, read Thomas Haller's blog post—[https://blogs.gnome.org/thaller/2019/03/15/wireguard-in-networkmanager/ WireGuard in NetworkManager.

The following examples configure WireGuard via the keyfile format .nmconnection files. See  and  for an explanation on the syntax and available options.

Peer A setup:

* To route all traffic through the tunnel to a specific peer, add the default route ( for IPv4 and  for IPv6) to . E.g. . Special handling of the default route in WireGuard connections is supported since NetworkManager 1.20.0.
* To use a peer as a DNS server, specify its WireGuard tunnel's IP address(es) with the  and  settings. Search domains can be specified with the  and  options. See  for more details. For example, using the keyfile format:

To use a peer as the only DNS server, set a negative DNS priority (e.g. ) and add  to the  settings.

Peer B setup:

Peer C setup:

## Specific use-case: VPN server
The purpose of this section is to set up a WireGuard "server" and generic "clients" to enable access to the server/network resources through an encrypted and secured tunnel like OpenVPN and others.  The "server" runs on Linux and the "clients" can run on any number of platforms (the WireGuard Project offers apps on both iOS and Android platforms in addition to Linux, Windows and MacOS).  See the official project install link for more.

## Server
On the peer that will act as the "server", first enable IPv4 forwarding.

If the server has a public IP configured, be sure to:

* Allow UDP traffic on the specified port(s) on which WireGuard will be running (for example allowing traffic on ).
* Setup the forwarding policy for the firewall if it is not included in the WireGuard configuration for the interface itself . The example below should have the iptables rules and work as-is.

If the server is behind NAT, be sure to forward the specified port(s) on which WireGuard will be running (for example, ) from the router to the WireGuard server.

## Key generation
Generate key pairs for the server and for each client as explained in #Key generation.

## Server configuration
Create the "server" configuration file:

Additional peers ("clients") can be listed in the same format as needed. Each peer requires the  to be set. However, specifying  is optional.

Notice that the  has a netmask of  and the clients on  . The clients only use their IP and the server only sends back their respective addresses.

The interface can be managed manually using  or using a systemd service managed via .

The interface may be brought up using  respectively by starting and potentially enabling the interface via , e.g. . To close the interface use  respectively stop .

## Client configuration
Create the corresponding "client" configuration file(s):

Using the catch-all  will forward all IPv4 () and IPv6 () traffic over the VPN.

## Testing the tunnel
Once a tunnel has been established, one can use netcat to send traffic through it to test out throughput, CPU usage, etc.
On one side of the tunnel, run  in listen mode and on the other side, pipe some data from  into  in sending mode.

In the example below, port 2222 is used for the traffic (be sure to allow traffic on port 2222 if using a firewall).

On one side of the tunnel listen for traffic:

 $ nc -vvlnp 2222

On the other side of the tunnel, send some traffic:

 $ dd if=/dev/zero bs=1024K count=1024 | nc -v 10.0.0.203 2222

Status can be monitored using  directly.

## Tips and tricks
## Store private keys in encrypted form (wg-quick)
It may be desirable to store private keys in encrypted form, such as through use of . Just replace the  line under  in the WireGuard configuration file with:

 PostUp = wg set %i private-key  /sys/kernel/debug/dynamic_debug/control

## Reload peer (server) configuration
In case the WireGuard peer (mostly server) adding or removing another peers from its configuration and wants to reload it without stopping any active sessions, one can execute the following command to do it:

 # wg syncconf ${WGNET}  mtu 1400 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
link/none
}}

Another option is falling back to a MTU of  and finding appropriate value for given path with a trial/error approach.

An MTU of  and above can lead to partially broken links which could be interpreted as a firewall or routing issue instead of actual MTU size.

## Key is not the correct length or format
To avoid the following error, put the key value in the configuration file and not the path to the key file.

## Unable to establish a persistent connection behind NAT / firewall
By default, WireGuard peers remain silent while they do not need to communicate, so peers located behind a NAT and/or firewall may be unreachable from other peers until they reach out to other peers themselves (or the connection may time out). Adding  to the  settings of a peer located behind a NAT and/or firewall can ensure that the connection remains open.

To temporarily set the persistent-keepalive setting via command line, run the following command:

 # wg set wg0 peer public_key persistent-keepalive 25

## Loop routing
Adding the endpoint IP to the allowed IPs list, the kernel will attempt to send handshakes to said device binding, rather than using the original route. This results in failed handshake attempts.

As a workaround, the correct route to the endpoint needs to be manually added using

 # ip route add endpoint_ip via gateway dev network_interface

E.g. for peer B from above in a standard LAN setup:

 # ip route add 203.0.113.102 via 192.168.0.1 dev eth0

To make this route persistent, the command can be added as  to the  section of . However, on certain setups (e.g. using  in combination with NetworkManager) this might fail on resume. Furthermore, this only works for a static network setup and fails if gateways or devices change (e.g. using Ethernet or Wi-Fi on a laptop).

Using NetworkManager, a more flexible solution is to start WireGuard using a dispatcher script. As root, create

If not already running, start and enable . Also make sure that NetworkManager is not managing routes for , see #Routes are periodically reset.

## Connection lost after sleep using systemd-networkd
systemd version 253 introduced a change in how network interfaces are reconfigured when resuming from a suspended stateIn doing so, network connections managed by systemd-networkd will lose connection to the WireGuard interface.  Unless a kill switch is configured, this risks exposing the public IP address after resuming from suspension. To fix this, uncomment and change the value to  for  in .[https://github.com/systemd/systemd/issues/26665#issuecomment-1454353725 If your WireGuard interface uses the  setting, you may also need to set  to .

Review the systemd-networkd page in full to become informed of any other potential side effects of this change.
