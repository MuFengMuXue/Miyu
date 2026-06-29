# OpenVPN

This article describes a basic installation and configuration of OpenVPN, suitable for private and small business use. For more detailed information, please see  and the OpenVPN documentation. OpenVPN is a robust and highly flexible VPN daemon. It supports SSL/TLS security, Ethernet bridging, TCP or UDP tunnel transport through proxies or NAT. Additionally it has support for dynamic IP addresses and DHCP, scalability to hundreds or thousands of users, and portability to most major OS platforms.

OpenVPN is tightly bound to the OpenSSL library, and derives much of its crypto capabilities from it. It supports conventional encryption using a pre-shared secret key (Static Key mode) or public key security (SSL/TLS mode) using client & server certificates. Additionally it supports unencrypted TCP/UDP tunnels.

OpenVPN is designed to work with the TUN/TAP virtual networking interface that exists on most platforms. Overall, it aims to offer many of the key features of IPSec but with a relatively lightweight footprint. OpenVPN was written by James Yonan and is published under the GNU General Public License (GPL).

## Installation
Install the  package, which provides both server and client mode.

There's also  client to connect to newer server.

Available frontends:

*
*
*

## Kernel configuration
OpenVPN requires TUN/TAP support, which is already configured in the default kernel. Users of custom kernel should make sure to enable the  module () in Device Drivers > Network device support > Network core driver support > Universal TUN/TAP device driver support.

Read Kernel module for more information.

## Connect to a VPN provided by a third party
To connect to a VPN service provided by a third party, most of the following can most likely be ignored, especially regarding server setup. Begin with #The client configuration profile and skip ahead to #Starting OpenVPN after that. One should use the provider certificates and instructions, see VPN providers for examples that can be adapted to other providers. OpenVPN client in Linux Containers also has general applicable instructions, while it goes a step further by isolating an OpenVPN client process into a container.

## Create a Public Key Infrastructure (PKI) from scratch
When setting up an OpenVPN server, users need to create a Public Key Infrastructure (PKI) which is detailed in the Easy-RSA article.  Once the needed certificates, private keys, and associated files are created via following the steps in the separate article, one should have 5 files in  at this point:

 ca.crt
 dh.pem
 servername.crt
 servername.key
 ta.key

Alternatively, as of OpenVPN 2.4, one can use Easy-RSA to generate certificates and keys using elliptic curves. See the OpenVPN documentation for details.

## A basic Layer-3 IP routing configuration
OpenVPN is an extremely versatile piece of software and many configurations are possible, in fact machines can be both servers and clients.

With the release of v2.4, server configurations are stored in  and client configurations are stored in  and each mode has its own respective systemd unit, namely,  and .

## Example configuration
The OpenVPN package comes with a collection of example configuration files for different purposes. The sample server and client configuration files make an ideal starting point for a basic OpenVPN setup with the following features:

* Uses Public Key Infrastructure (PKI) for authentication.
* Creates a VPN using a virtual TUN network interface (OSI Layer-3 IP routing).
* Listens for client connections on UDP port 1194 (OpenVPN's official IANA port number* Distributes virtual addresses to connecting clients from the 10.8.0.0/24 subnet.

For more advanced configurations, please see the  man page and the [https://openvpn.net/index.php/open-source/documentation OpenVPN documentation.

## The server configuration file
Copy the example server configuration file  to .

Edit the file making a minimum of the following changes:

If TLS with elliptic curves is used, specify  and  (or ). DH parameters file is not used when using elliptic curves. Starting from OpenVPN 2.4.8, it is required to specify the type of elliptic curves in server configuration. Otherwise the server would fail to recognize the curve type and possibly use an incompatible one, resulting in authentication errors.

## Hardening the server
If security is a priority, additional configuration is recommended including: limiting the server to use a strong cipher/auth method and (optionally) limiting the set of enabled TLS ciphers to the newer ciphers. Starting from OpenVPN 2.4, the server and the client will automatically negotiate AES-256-GCM in TLS mode.

Add the following to :

Bleeding edge security:

Compatibility with most devices:

## Enabling compression
Enabling compression is not recommended by upstream; doing so opens to the server the so-called VORACLE attack vector.  See this article.

## Deviating from the standard port and/or protocol
It is generally recommended to use OpenVPN over UDP, because TCP over TCP is a bad ideaSome networks may disallow OpenVPN connections on the default port and/or protocol. One strategy to circumvent this is to mimic HTTPS traffic which is very likely unobstructed.

To do so, configure  as such:

## Running multiple instances of OpenVPN on different ports on the physical machine
One can have multiple, concurrent instances of OpenVPN running on the same box.  Each server needs to be defined in  as a separate .conf file.  At a minimum, the parallel servers need to be running on different ports.  A simple setup directs traffic connecting in to a separate IP pool.  More advanced setups are beyond the scope of this guide.

Consider this example, running 2 concurrent servers, one port 443/udp and another on port 80/tcp.

First modify  created as so:

Now copy it and modify the copy to run on 80/tcp:

Be sure to setup the corresponding entries in the firewall, see the relevant sections in #Firewall configuration.

## The client configuration profile
Copy the example client configuration file  to .

Edit the following:

* The  directive to reflect either the server's Fully Qualified Domain Name, hostname (as known to the client), or its IP address.
* Uncomment the  and  directives to drop privileges.
* The , , and  parameters to reflect the path and names of the keys and certificates.
* Enable the TLS HMAC handshake protection ( or ).

## Run as unprivileged user
Using the options  and  in the configuration file makes OpenVPN drop its  privileges after establishing the connection. The downside is that upon VPN disconnect the daemon is unable to delete its set network routes again. If one wants to limit transmitting traffic without the VPN connection, then lingering routes may be considered beneficial. It can also happen, however, that the OpenVPN server pushes updates to routes at runtime of the tunnel. A client with dropped privileges will be unable to perform the update and exit with an error.

As it could seem to require manual action to manage the routes, the options  and  might seem undesirable. Depending on setup, however, there are different ways to handle these situations:

* For errors of the unit, a simple way is to edit it and add a  to the  section. Though, this alone will not delete any obsoleted routes, so it may happen that the restarted tunnel is not routed properly.
* The package contains the , which can be used to let openvpn fork a process with root privileges with the only task to execute a custom script when receiving a down signal from the main process, which is handling the tunnel with dropped privileges (see also its [https://community.openvpn.net/openvpn/browser/plugin/down-root/README?rev=d02a86d37bed69ee3fb63d08913623a86c88da15 README).

The OpenVPN HowTo's linked below go further by creating a dedicated non-privileged user/group, instead of the already existing . The advantage is that this avoids potential risks when sharing a user among daemons:

* The OpenVPN HowTo explains another way how to create an unprivileged user mode and wrapper script to have the routes restored automatically.
* It is possible to let OpenVPN start as a non-privileged user in the first place, without ever running as root, see this OpenVPN wiki (howto). The howto assumes the presence of System V init, rather than Systemd and does not cover the handling of / scripts - those should be handled the same way as the ip command, with additional attention to access rights.
* It is also possible to run OpenVPN from within unprivileged podman container, see this section of OpenVPN HowTo

## Converting certificates to encrypted .p12 format
Some software will only read VPN certificates that are stored in a password-encrypted .p12 file. These can be generated with the following command:

 # openssl pkcs12 -export -inkey keys/bugs.key -in keys/bugs.crt -certfile keys/ca.crt -out keys/bugs.p12

## Testing the OpenVPN configuration
Run  (as the root user) on the server, and  (as the root user) on the client.  Example output should be similar to the following:

Find the IP address assigned to the tunX interface on the server, and ping it from the client.

Find the IP address assigned to the tunX interface on the client, and ping it from the server.

## Configure the MTU with Fragment and MSS
If experiencing issues when using (remote) services over OpenVPN (e.g. web browsing, DNS, NFS), it may be needed to set a MTU value manually.

The following message may indicate the MTU value should be adjusted:

 read UDPv4 Path-MTU=1407: Message too long (code=90)

In order to get the  maximum segment size (MSS), the client needs to discover the smallest MTU along the path to the server. In order to do this  ping the server and disable fragmentation, then specify the maximum packet size # ping -M do -s 1500 -c 1 example.com

Decrease the 1500 value by 10 each time, until the ping succeeds.

Update the client configuration to use the succeeded MTU value, e.g.:

OpenVPN may be instructed to test the MTU every time on client connect. Be patient, since the client may not inform about the test being run and the connection may appear as nonfunctional until finished.  The following will add about 3 minutes to OpenVPN start time. It is advisable to configure the fragment size unless a client will be connecting over many different networks and the bottle neck is not on the server side:

## IPv6
## Connect to the server via IPv6
Starting from OpenVPN 2.4, OpenVPN will use  defined by the OS when just using  or , which in most cases will be IPv4 only. To use both IPv4 and IPv6, use  or . To enforce only IPv4-only, use  or . On older OpenVPN versions, one server instance can only support either IPv4 or IPv6.

## Provide IPv6 inside the tunnel
In order to provide IPv6 inside the tunnel, have an IPv6 prefix routed to the OpenVPN server. Either set up a static route on the gateway (if a static block is assigned), or use a DHCPv6 client to get a prefix with DHCPv6 Prefix delegation (see IPv6 Prefix delegation for details). Also consider using a unique local address from the address block fc00::/7. Both methods have advantages and disadvantages:

* Many ISPs only provide dynamically changing IPv6 prefixes. OpenVPN does not support prefix changes, so change the server.conf every time the prefix is changed (Maybe can be automated with a script).
* ULA addresses are not routed to the Internet, and setting up NAT is not as straightforward as with IPv4. This means one cannot route the entire traffic over the tunnel. Those wanting to connect two sites via IPv6, without the need to connect to the Internet over the tunnel, may want to use the ULA addresses for ease.

Alternatively, a NDP proxy should work. See [https://unix.stackexchange.com/questions/136211/routing-public-ipv6-traffic-through-openvpn-tunnel this StackExchange post.

After having received a prefix (a /64 is recommended), append the following to the server.conf:

 server-ipv6 2001:db8:0:123::/64

This is the IPv6 equivalent to the default 10.8.0.0/24 network of OpenVPN and needs to be taken from the DHCPv6 client. Or use for example fd00:1234::/64.

Those wanting to push a route to a home network (192.168.1.0/24 equivalent), need to also append:

 push "route-ipv6 2001:db8:0:abc::/64"

OpenVPN does not yet include DHCPv6, so there is no method to e.g. push DNS server over IPv6. This needs to be done with IPv4. The OpenVPN Wiki provides some other configuration options.

## Starting OpenVPN
## Manual startup
To troubleshoot a VPN connection, start the client's daemon manually with  as root. The server can be started the same way using its own configuration file (e.g., ).

## systemd service configuration
To start the OpenVPN server automatically at system boot, enable  on the applicable machine. For a client, enable  instead. (Leave  out of the  string.)

For example, if the client configuration file is , the service name is . Or, if the server configuration file is , the service name is .

## Letting NetworkManager start a connection
One might not always need to run a VPN tunnel and/or only want to establish it for a specific NetworkManager connection. This can be done by adding a script to . In the following example "Provider" is the name of the NetworkManager connection:

See NetworkManager#Network services with NetworkManager dispatcher for more details.

## NetworkManager-native VPN configuration
NetworkManager supports OpenVPN management using .

## GUI configuration
In your desktop environment network settings (or ). Click the plus sign to add a new connection and choose OpenVPN and manually enter the settings. You also can optionally import #The client configuration profile by selecting Import a saved VPN configuration... and selecting the appropriate file.

## CLI configuration
For importing a configuration:

 $ nmcli connection import type openvpn file file.ovpn

To do a manual configuration:

 $ nmcli connection add type vpn vpn-type openvpn ...

See  for the detailed options.

If you want to setup login and password, check that there is no  line in the openvpn file or remove it. Then after the import:

 $ nmcli connection modify name \
    +vpn.data "connection-type=password-tls, username=USERNAME" \
    vpn.user-name USERNAME \
    +vpn.secrets "password=PASS"

You will then be able to connect without re-entering the password with:

 $ nmcli connection up name

## Sync state with connection
NetworkManager supports syncing the VPN state with a interface connection state, i.e start the VPN together with the connection and bringing it down when the connection goes down.

To achieve this, open  and select a network connection (not the VPN), then head to the General section, tick Automatically connect to VPN and select the appropriate configuration in the dropdown menu.

## Automatically connect to VPN via CLI
First, list your connections as follows:

Copy the UUID of the VPN Connection you want to connect automatically to (here, d46e4a92-778e-4792-b085-e1f638ecb8e3), then edit the primary connection (here the Ethernet one) to make it use the VPN:

 $ nmcli c edit enp1s0
 nmcli> set connection.secondaries d46e4a92-778e-4792-b085-e1f638ecb8e3
 nmcli> save persistent
 Connection 'enp1s0' (1715b889-3c47-3e21-a86f-94ce207297a9) successfully updated.

Afterwards, restart

## Import VPN configuration
With the  client:

 $ openvpn3 config-import --config path/to/config.conf

To list the configurations:

 $ openvpn3 configs-list

## Troubleshooting
## No certificate password
If you get:

 Warning: password for 'vpn.secrets.password' not given in 'passwd-file' and nmcli cannot ask without '--ask' option.
 Error: Connection activation failed: No valid secrets

Even with

 cert-pass-flags=0

You can add:

 [vpn-secrets
 cert-pass=anything_you_want

## Routing client traffic through the server
Without further configuration only traffic directly to and from the OpenVPN server's IP passes through the VPN. To have other traffic, like web traffic pass through the VPN, correspondent routes must be added.  Either add routes in the client's configuration or configure the server to push these routes to the client.

To redirect traffic to and from a subnet of the server, add  right before the , like:

 route 192.168.1.0 255.255.255.0

To redirect all traffic including Internet traffic to the server, add the following in the client's configuration:

 redirect-gateway def1 bypass-dhcp ipv6

If running an IPv4-only server, drop the  option. If running IPv6-only, use .

To make the server push routes, append  to the configuration file (i.e. ) of the server. Note this is not a requirement and may even give performance issue:

 push "redirect-gateway def1 bypass-dhcp ipv6"

If running an IPv4-only server, drop the  option. If running IPv6-only, use

Use the  option to allow clients reaching other subnets/devices behind the server:

 push "route 192.168.1.0 255.255.255.0"
 push "route 192.168.2.0 255.255.255.0"

Optionally, push local DNS settings to clients (e.g. the DNS-server of the router and domain prefix .internal):

 push "dhcp-option DNS 192.168.1.1"
 push "dhcp-option DOMAIN internal"

After setting up the configuration file, enable packet forwarding on the server. Additionally, the server's firewall needs to be adjusted to allow VPN traffic, which is described below for both ufw and iptables.

## Firewall configuration
## firewalld
If using the default port 1194, enable the  service. Otherwise, create a new service with a different port.

 # firewall-cmd --zone=public --add-service openvpn

Now add masquerade to the zone:

 # firewall-cmd --zone=FedoraServer --add-masquerade

Make these changes permanent:

 # firewall-cmd --runtime-to-permanent

## ufw
In order to allow ufw forwarding (VPN) traffic append the following to :

Change , and append the following code after the header and before the "*filter" line:
* Change the IP/subnet mask to match the  set in the OpenVPN server configuration.
* Change the network interface to the connection used by OpenVPN server.

Make sure to open the chosen OpenVPN port (default 1194/udp):

 # ufw allow 1194/udp

To apply the changes. reload/restart ufw:

 # ufw reload

## iptables
In order to allow VPN traffic through an iptables firewall, first create an iptables rule for NAT forwarding [https://openvpn.net/index.php/open-source/documentation/howto.html#redirect on the server. An example (assuming the interface to forward to is named ):

 # iptables -t nat -A POSTROUTING -s 10.8.0.0/24 -o eth0 -j MASQUERADE

If running multiple servers on different IP pools, add a corresponding line for each one, for example:

 # iptables -t nat -A POSTROUTING -s 10.8.1.0/24 -o eth0 -j MASQUERADE

If the server cannot be pinged through the VPN, one may need to add explicit rules to open up TUN/TAP interfaces to all traffic. If that is the case, do the following # iptables -A INPUT -i tun+ -j ACCEPT
 # iptables -A FORWARD -i tun+ -j ACCEPT
 # iptables -A INPUT -i tap+ -j ACCEPT
 # iptables -A FORWARD -i tap+ -j ACCEPT

Additionally be sure to accept connections from the OpenVPN port (default 1194) and through the physical interface:

 # iptables -A INPUT -i eth0 -m state --state NEW -p udp --dport 1194 -j ACCEPT
 # iptables -A FORWARD -i tun+ -o eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT
 # iptables -A FORWARD -i eth0 -o tun+ -m state --state RELATED,ESTABLISHED -j ACCEPT
 # iptables -A FORWARD -i tap+ -o eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT
 # iptables -A FORWARD -i eth0 -o tap+ -m state --state RELATED,ESTABLISHED -j ACCEPT

When satisfied, make the changes permanent as shown in iptables#Configuration and usage.

Those with multiple  or  interfaces, or more than one VPN configuration can "pin" the name of the interface by specifying it in the OpenVPN configuration file, e.g.  instead of . This is advantageous if different firewall rules for different interfaces or OpenVPN configurations are wanted.

## Prevent leaks if VPN goes down
This prevents all traffic through the default interface (enp3s0 for example) and only allows traffic through tun0.
If the OpenVPN connection drops, the system will lose its internet access thereby preventing connections through the default network interface.

One may want to set up a script to restart OpenVPN if it goes down.

## ufw
  # Default policies
  ufw default deny incoming
  ufw default deny outgoing

  # Openvpn interface (adjust interface accordingly to your configuration)
  ufw allow in on tun0
  ufw allow out on tun0

  # Local Network (adjust ip accordingly to your configuration)
  ufw allow in on enp3s0 from 192.168.1.0/24
  ufw allow out on enp3s0 to 192.168.1.0/24

  # Openvpn (adjust port accordingly to your configuration)
  ufw allow in on enp3s0 from any port 1194
  ufw allow out on enp3s0 to any port 1194

## vpnfailsafe
Alternatively, the [https://github.com/wknapik/vpnfailsafe vpnfailsafe () script can be used by the client to prevent DNS leaks and ensure that all traffic to the internet goes over the VPN. If the VPN tunnel goes down, internet access will be cut off, except for connections to the VPN server(s). The script contains the functionality of update-resolv-conf, so the two do not need to be combined.

## dhcpcd
 adds special routes to the system routing table. If running  and the local DHCP configuration changes, perhaps because the Wi-Fi access point has changed, then  will delete all of these special routes. The easiest way to restore them is to prompt  to reconnect, using :

 # Prompt openvpn to reconnect when the network reconnects.
 if $if_configured && $if_up && [ "$reason" != ROUTERADVERT ]; then
     state="$(systemctl show -P ActiveState openvpn-client@config)"
     if [ "$state" == 'active' ]; then
         pid="$(systemctl show -P MainPID openvpn-client@config)"
         kill -USR1 "$pid"
     fi
 fi

Replace  with the name of your client config.

## Layer-3 IPv4 routing
This section describes how to connect client/server LANs to each other using Layer-3 IPv4 routing.

## Prerequisites for routing a LAN
For a host to be able to forward IPv4 packets between the LAN and VPN, it must be able to forward the packets between its NIC and its tun/tap device. See Internet sharing#Enable packet forwarding for configuration details.

## Routing tables
By default, all IP packets on a LAN addressed to a different subnet get sent to the default gateway.  If the LAN/VPN gateway is also the default gateway, there is no problem and the packets get properly forwarded. If not, the gateway has no way of knowing where to send the packets.  There are a couple of solutions to this problem.

* Add a static route to the default gateway routing the VPN subnet to the LAN/VPN gateway's IP address.
* Add a static route on each host on the LAN that needs to send IP packets back to the VPN.
* Use iptables' NAT feature on the LAN/VPN gateway to masquerade the incoming VPN IP packets.

## Connect the server LAN to a client
The server is on a LAN using the 10.66.0.0/24 subnet.  To inform the client about the available subnet, add a push directive to the server configuration file:

## Connect the client LAN to a server
Prerequisites:

* Any subnets used on the client side, must be unique and not in use on the server or by any other client. In this example we will use 192.168.4.0/24 for the clients LAN.
* Each client's certificate has a unique Common Name, in this case bugs.
* The server may not use the duplicate-cn directive in its configuration file.
* The CCD folder must be accessible via user and group defined in the server configuration file (typically nobody:nobody)

Create a client configuration directory on the server.  It will be searched for a file named the same as the client's common name, and the directives will be applied to the client when it connects.

 # mkdir -p /etc/openvpn/ccd

Create a file in the client configuration directory called bugs, containing the  directive.  It tells the server what subnet should be routed to the client:

Add the client-config-dir and the  directive to the server configuration file. It tells the server what subnet should be routed from the tun device to the server LAN:

If accessing a machine in the client LAN from a machine in the server LAN, remember that packet forwarding needs to be enabled on the client (Internet sharing#Enable packet forwarding).

## Connect both the client and server LANs
Combine the two previous sections:

## Connect clients and client LANs
By default clients will not see each other. To allow IP packets to flow between clients and/or client LANs, add a client-to-client directive to the server configuration file:

In order for another client or client LAN to see a specific client LAN, add a push directive for each client subnet to the server configuration file (this will make the server announce the available subnet(s) to other clients):

## DNS
For Linux, the OpenVPN client can receive DNS host information from the server, but the client expects an external command to act on this information. No such commands are configured by default. They must be specified with the  and  options. There are a few alternatives for what scripts to use, but none are officially recognised by OpenVPN, so in order for any of them to work,  must be set to 2. The  plugin can be used instead of the  option if running as an unprivileged user.

## The pull-resolv-conf custom scripts
These scripts are maintained by OpenVPN. They are  and , and they are packaged in . The following is an excerpt of a resulting client configuration using the scripts in conjunction with the  plugin:

These scripts use the  command if present. systemd-resolvconf and Openresolv both implement this command. See their wiki pages for more information on getting a working resolvconf implementation.

If no implementation of resolvconf is present,  preserves the existing  at  and writes a new one. This new one will not have any of the original DNS servers.

When editing these scripts, copy them somewhere else and edit them there, so that the changes do not get overwritten by the next  package upgrade.  is a pretty good place.

 # cp /usr/share/openvpn/contrib/pull-resolv-conf/* /etc/openvpn/client/

Edit  and .

## The update-resolv-conf custom script
The openvpn-update-resolv-conf script is available as an alternative to packaged scripts. It needs to be saved for example at  and made executable.

Users preferring a package may use  but will still need to do the following:

Once the script is installed add lines like the following into the OpenVPN client configuration file:

 script-security 2
 up /etc/openvpn/update-resolv-conf
 down /etc/openvpn/update-resolv-conf

Now, when launching the OpenVPN connection,  should be updated accordingly, and also should get returned to normal when the connection is closed.

## The update-systemd-resolved custom script
The update-systemd-resolved script links OpenVPN with  via DBus to update the DNS records.

Copy the script into  and mark as executable (or install ) and append the following lines into the OpenVPN client configuration file:

In order to send all DNS traffic through the VPN tunnel and prevent DNS leaks, also add the following line (see Make sure that the systemd-resolved service is configured and running. Also, since openvpn 2.5.0-3 scripts are running as openvpn user instead of root. Thus, add a PolicyKit rule to allow OpenVPN systemd units to call DBus with SetLinkDNS:

{{hc|/etc/polkit-1/rules.d/00-openvpn-resolved.rules|
polkit.addRule(function(action, subject) {
    if (action.id == 'org.freedesktop.resolve1.set-dns-servers' ||
        action.id == 'org.freedesktop.resolve1.set-domains' ||
        action.id == 'org.freedesktop.resolve1.set-dnssec') {
        if (subject.user == 'openvpn') {
            return polkit.Result.YES;
        }
    }
});
}}

## Override DNS servers using NetworkManager
By default  plugin appends DNS servers provided by OpenVPN to .

To verify that the correct DNS server(s) are configured, see  if systemd-resolved is in use, for other resolvers see Domain name resolution.

## Layer-2 Ethernet bridging
Establishing an Ethernet bridge enables access to other devices within a subnet of the server. For example, accessing other machines in the local network of the OpenVPN server via Samba would be possible with this approach. Clients would be assigned an IP address as if it were within the same subnet.

This is generally a two step process: 1) establishing the tap interface and the network bridge on the OpenVPN server to bridge the tap interface and the Ethernet interface, and 2) configuring the OpenVPN server.

See OpenVPN Bridge.

## Configuration generators
## ovpngen
The  package provides a simple shell script that creates OpenVPN compatible tunnel profiles in the unified file format suitable for the OpenVPN Connect app for Android and iOS.

Simply invoke the script with 5 tokens:

# Server Fully Qualified Domain Name of the OpenVPN server (or IP address).
# Full path to the CA cert.
# Full path to the client cert.
# Full path to the client private key.
# Full path to the server TLS shared secret key.
# Optionally a port number.
# Optionally a protocol (udp or tcp).

Example:

 # ovpngen example.org /etc/openvpn/server/ca.crt /etc/easy-rsa/pki/signed/client1.crt /etc/easy-rsa/pki/private/client1.key /etc/openvpn/server/ta.key > foo.ovpn

If the server is configured to use tls-crypt, as is suggested in #The server configuration file, [https://github.com/graysky2/ovpngen/issues/4 manually edit the resulting  replacing  and  with  and .

The resulting  can be edited if desired as the script does insert some commented lines.  will not automatically route all traffic through the VPN, so consider following #Routing client traffic through the server to enable redirection.

The client expects this file to be located in . Note the change in file extension from 'ovpn' to 'conf' in this case.

## openvpn-unroot
The steps necessary for OpenVPN to #Run as unprivileged user, can be performed automatically using openvpn-unroot ().

It automates the actions required for the OpenVPN howto by adapting it to systemd, and also working around the bug for persistent tun devices mentioned in the note.

## Troubleshooting
## Client daemon not reconnecting after suspend
, available on the AUR, solves this problem by sending a SIGHUP to openvpn after waking up from suspend.

Alternatively, restart OpenVPN after suspend by creating the following systemd service:

Enable this service for it to take effect.

## Connection drops out after some time of inactivity
If the VPN-Connection drops some seconds after it stopped transmitting data and, even though it states it is connected, no data can be transmitted through the tunnel, try adding a directive to the server's configuration:

In this case the server will send ping-like messages to all of its clients every 10 seconds, thus keeping the tunnel up.
If the server does not receive a response within 120 seconds from a specific client, it will assume this client is down.

A small ping-interval can increase the stability of the tunnel, but will also cause slightly higher traffic. Depending on the connection, also try lower intervals than 10 seconds.

## PID files not present
The default systemd service file for openvpn-client does not have the --writepid flag enabled, despite creating /run/openvpn-client. If this breaks a configuration (such as an i3bar VPN indicator), simply change  using a drop-in snippet:

 ExecStart=
 ExecStart=/usr/sbin/openvpn --suppress-timestamps --nobind --config %i.conf --writepid /run/openvpn-client/%i.pid

## Route configuration fails with systemd-networkd
When using systemd-networkd to manage network connections and attempting to tunnel all outgoing traffic through the VPN, OpenVPN may fail to add routes. This is a result of systemd-networkd attempting to manage the tun interface before OpenVPN finishes configuring the routes. When this happens, the following message will appear in the OpenVPN log.

 openvpn[458: RTNETLINK answers: Network is unreachable
 openvpnERROR: Linux route add command failed: external program exited with error status: 2

From systemd-233, systemd-networkd can be configured to ignore the tun connections and allow OpenVPN to manage them. To do this, create the following file:

Restart  to apply the changes. To verify that the changes took effect, start the previously problematic OpenVPN connection and run . The output should have a line similar to the following:

 7 tun0             none               routable    unmanaged

## tls-crypt unwrap error: packet too short
This error shows up in the server log when a client that does not support tls-crypt, or a client that is misconfigured to use tls-auth while the server is configured to use tls-crypt, attempts to connect.

To support clients that do not support tls-crypt, replace  with  (the default) in . Also replace  with  (the default) in .

## NetworkManager fails to connect using imported configuration
There is a known upstream bug [https://bugs.kde.org/show_bug.cgi?id=396530in conjunction with importing existing OpenVPN configurations (.ovpn files) under KDE via the GUI ( not ) that causes certain advanced options such as  to be silently ignored. The created NetworkManager connection profile will therefore be incomplete and the connection ultimately fails.

Logs might reveal errors such as the following:

 TLS Error: TLS handshake failed
 TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity)

A workaround is to resort to NetworkManager's command-line utility nmcli to import the connection profile as is shown in #CLI configuration.

## OpenVPN connection fails after update to OpenSSL3
There exists an issue with PKCS#12 encoded user certificates/private key files (usually denoted by a .pfx or .p12 file ending) with OpenSSL3, c.f. also [https://bbs.archlinux.org/viewtopic.php?pid=2067602. This leads to connections which worked perfectly before updating to OpenSSL3 not being able to connect with the following log messages produced (in this case via NetworkManager):

The reason is that older versions of OpenSSL used algorithms, which are now deprecated, to encrypt the PKCS#12 files.

To solve this issue the PKCS#12 file must be re-encrypted with a non-legacy algorithm.
