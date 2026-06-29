# Systemd-networkd

systemd-networkd is a system daemon that manages network configurations. It detects and configures network devices as they appear; it can also create virtual network devices. This service can be especially useful to set up complex network configurations for a container managed by systemd-nspawn or for virtual machines. It also works fine on simple connections.

## Installation
 is part of the default Arch installation and contains all needed files to operate a wired network.  Wireless adapters, covered later in this article, can be set up by services, such as wpa_supplicant or iwd.

## Required services and setup
To use systemd-networkd, start/enable .

It is optional to also configure systemd-resolved, which is a network name resolution service to local applications, considering the following points:

* It is important to understand how resolv.conf and systemd-resolved interact to properly configure the DNS that will be used, some explanations are provided in systemd-resolved.
* systemd-resolved is required if DNS entries are specified in .network files.
* systemd-resolved is also required to obtain DNS addresses from DHCP servers or IPv6 router advertisements.(by setting ( and/or  in the  section, and  (the default) in the corresponding section(s) , , , see ).
* Note that systemd-resolved can also be used without systemd-networkd.

## systemd-networkd-wait-online
Enabling  also enables , which is a oneshot system service that waits for the network to be configured. The latter has , so it will be started only when  itself is enabled or pulled in by some other unit. See also systemd#Running services after the network is up.

By default,  waits for all links managed by systemd-networkd to be fully configured or failed, and for at least one link to be online.

See  for details.

## Configuration
## systemd example network files
A quick way to enable a network interface is to use one of the provided .example files located in . For instance, to enable Wi-Fi and Ethernet, you can create symbolic links to the example files:

 # ln -s /usr/lib/systemd/network/80-wifi-station.network.example /etc/systemd/network/80-wifi-station.network
 # ln -s /usr/lib/systemd/network/89-ethernet.network.example /etc/systemd/network/89-ethernet.network

You can use networkctl to add any additional custom configuration. See the #networkctl section.

## Multiple interfaces that are not connected all the time
For system with multiple network interfaces that are not expected to be connected all the time (e.g. if a dual-port Ethernet card, but only one cable plugged in), starting  will fail after the default timeout of 2 minutes. This may cause an unwanted delay in the startup process. To change the behaviour to wait for any interface rather than all interfaces to become online, edit the service and add the  parameter to the  line:

Alternatively, use  to wait for a specific interface. For example, to wait for , disable  and enable .

## Wait until network interfaces have a routable address
Per , "online means that the link's operational state is equal or higher than "degraded"." (see  for the definition of "degraded" and other operational statuses).

To prevent  from exiting before network interfaces have a routable IP address (and thus having other services that require a working network connection starting too early), add  to the  section in .network files:

## Wait until DNS servers are reachable
 can be delayed until all configured interfaces can connect to their DNS servers. This improves the chances that DNS is operational when network-online.target is reached and units ordered after it begin to start.

To enable this feature, edit  and add the  option to the  line:

## Usage
The global configuration file in  may be used to override some defaults only. The main configuration is performed per network device. Configuration files are located in , the volatile runtime network directory  and the local administration network directory . Files in  have the highest priority.

There are three types of configuration files. They all use a format similar to systemd unit files.

; .network files: They will apply a network configuration for a matching device. See the  man page.
; .netdev files: They will create a virtual network device for a matching environment. See the  man page.
; .link files: When a network device appears, udev will look for the first matching .link file. See the  man page.

They all follow the same rules:

* If all conditions in the  section are matched, the profile will be activated
* an empty  section means the profile will apply in any case (can be compared to the  wildcard)
* all configuration files are collectively sorted and processed in lexical order, regardless of the directory in which they live
* files with identical name replace each other
After making changes to a configuration file, restart .

## networkctl
You can use  to query or modify the status of network links:

For example, to enable Multicast DNS for the Wi-Fi interface:

Replace  with your stable interface name or specify the full path instead. See .

## Wired adapter using DHCP
## Wired adapter using a static IP
 can be used more than once to configure multiple IPv4 or IPv6 addresses. See  for more options.

## Wireless adapter
In order to connect to a wireless network with systemd-networkd, a wireless adapter configured with another application such as wpa_supplicant or iwd is required.

If the wireless adapter has a static IP address, the configuration is the same (except for the interface name) as in a wired adapter.

To authenticate to the wireless network, use e.g. wpa_supplicant or iwd.

## Wired and wireless adapters on the same machine
This setup will enable a DHCP IP for both a wired and wireless connection making use of the metric directive to allow the kernel to decide on-the-fly which one to use.  This way, no connection downtime is observed when the wired connection is unplugged.

The kernel's route metric (same as configured with ip) decides which route to use for outgoing packets, in cases when several match. This will be the case when both wireless and wired devices on the system have active connections. To break the tie, the kernel uses the metric. If one of the connections is terminated, the other automatically wins without there being a gap with nothing configured (ongoing transfers may still not deal with this nicely but that is at a different OSI layer).

systemd-networkd does not set per-interface-type default route metrics, so it needs to be configured manually:

## DHCP server
This is an example of a DHCP server configuration which works well with hostapd to create a wireless hotspot.  adds the firewall rules for NAT and implies  to enable packet forwarding.

See  for all available options.

## Add a secondary route and gateway
Add on a single interface a second address and a secondary gateway for specific subnet.

## Usage with containers
systemd-networkd can provide fully automatic configuration of networking for systemd-nspawn containers using private networking when it is used on the host system as well as inside the container. See systemd-nspawn#Networking for a comprehensive overview.

For the examples below,

* we will limit the output of the  command to the concerned interfaces,
* we assume the host is the main operating system running on real hardware and the container is the guest system,
* all interface names and IP addresses are only examples.

## Network bridge with DHCP
## Bridge interface
First, create a virtual bridge interface with a .netdev unit file which tells systemd-networkd to create a device named  that functions as an Ethernet bridge.

Optionally add  to the  section for the bridge to inherit MAC address from one of the bridged interfaces. This also requires a creation of 25-br0.link file.

Restart  to have systemd-networkd create the bridge.

To see the newly created bridge on the host and on the container, type:

Note that the interface  is listed but is still DOWN at this stage.

## Bind Ethernet to bridge
The next step is to add a network interface to the newly created bridge. The configuration file of the bridge must be loaded before those of the bridged interfaces, so its configuration file should be alphanumerically prior to those. In the example below, we add any interface that matches the name  into the bridge .

The Ethernet interface must not have DHCP or an IP address associated, as the bridge requires an interface to bind to with no IP address.

## Bridge network
Now that the bridge has been created and has been bound to an existing network interface, the IP configuration of the bridge interface must be specified. This is defined in a third .network file, the example below uses DHCP.

## Inherit MAC address (optional)
For the bridge to inhering MAC address from one of the bridged interfaces, set  and .

## Configure the container
Use the  option when starting the container. See systemd-nspawn#Use a network bridge for details.

## Result
* on host

* on container

## Notice
* we have now one IP address for  on the host, and one for  in the container
* two new interfaces have appeared:  in the host and  in the container. This comes as a result of the  option as explained in systemd-nspawn#Use a network bridge for details.
* the DHCP address on  comes from the system  file.
* on host

the above command output confirms we have a bridge with two interfaces binded to.

* on host

* on container

the above command outputs confirm we have activated  and  interfaces with an IP address and Gateway 192.168.1.254. The gateway address has been automatically grabbed by systemd-networkd.

## Network bridge with static IP addresses
Setting a static IP address for each device can be helpful in case of deployed web services (e.g. FTP, HTTP, SSH). Each device will keep the same MAC address across reboots if your system  file has the  option (it has by default). This setup routes any service on the gateway to the desired device.

The following configuration needs to be done for this setup:

* on host

The configuration is very similar to the #Network bridge with DHCP section. First, a virtual bridge interface needs to be created and the main physical interface needs to be bound to it. This task can be accomplished with the following two files, with contents equal to those available in the DHCP section.

 /etc/systemd/network/MyBridge.netdev
 /etc/systemd/network/MyEth.network

Next, you need to configure the IP and DNS of the newly created virtual bridge interface. For example:

* on container

To get configure a static IP address on the container, we need to override the system  file, which provides a DHCP configuration for the  network interface of the container. This can be done by placing the configuration into . For example:

Make sure that  is enabled in the container.

## MACVLAN bridge
For the host to be able to reach containers connected via MACVLAN, the host itself also needs to connect via MACVLAN and not directly to the underlying Ethernet network interface.

On the host, attach the underlying Ethernet network interface to MACVLAN and make sure it does not get assigned IP addresses. For example, using  as the MACVLAN interface name and with  as the host's Ethernet interface:

Create the MACVLAN bridge :

Configure the host's network connection on the MACVLAN bridge (). The following example uses DHCP, replace the options as necessary.

For the container, attach a MACVLAN to the underlying Ethernet network interface ( in the examples above). For example, in  specify:

For containers started from the command line, pass them the  option.

In the container, the MACVLAN interface will have the name  (e.g. ). Configure the network connection as necessary (just like in the host) by matching the interface name. For example, using DHCP:

## Tips and tricks
## Interface and desktop integration
systemd-networkd does not have a proper interactive graphical management interface. Still, some tools are available to either display or modify the current state of the network, receive notifications or interact with the wireless configuration:

* networkctl provides a command-line shell interface to query or modify the network interface states. It is worth noting that in order to change only some aspects of an interface behavior, one is required to first edit one or more configuration files in .
* When networkd is configured with wpa_supplicant, both wpa_cli and wpa_gui offer the ability to associate and configure WLAN interfaces dynamically.
* The  daemon allows executing scripts in response to network interface state changes, similar to NetworkManager-dispatcher.
* The  creates simple notification messages on interface changes.
* As for the DNS resolver systemd-resolved, information about current DNS servers can be visualized with .

## Configuring static IP or DHCP based on SSID (location)
Often there is a situation where your home wireless network uses DHCP and office wireless network uses static IP. This mixed setup can be configured as follows:

## Bonding a wired and wireless interface
See also Wireless bonding.

Bonding allows connection sharing through multiple interfaces, so if e.g. the wired interface is unplugged, the wireless is still connected and the network connectivity remains up seamlessly.

Create a bond interface. In this case the mode is active-backup, which means packets are routed through a secondary interface if the primary interface goes down.

Set the wired interface as the primary:

Set the wireless as the secondary:

Configure the bond interface just like a normal interface:

Now if the wired network is unplugged, the connection should remain through the wireless:

## Speeding up TCP slow-start
On a higher bandwidth link with moderate latency (typically a home Internet connection that is above 10 Mbit/s) the default settings for the TCP Slow Start algorithm are somewhat conservative.  This issue exhibits as downloads starting slowly and taking a number of seconds to speed up before they reach the connection's full bandwidth.  It is particularly noticeable with a pacman upgrade, where each package downloaded starts off slowly and often finishes before it has reached the connection's full speed.

These settings can be adjusted to make TCP connections start with larger window sizes than the defaults, avoiding the time it takes for them to automatically increase on each new TCP connectionWhile this will usually decrease performance on slow connections (or if the values are increased too far) due to having to retransmit a larger number of lost packets, they can substantially increase performance on connections with sufficient bandwidth.

It is important to benchmark before and after changing these values to ensure it is improving network speed and not reducing it.  If you are not seeing downloads begin slowly and gradually speed up, then there is no need to change these values as they are already optimal for your connection speed.  When benchmarking, be sure to test against both a high speed and low speed remote server to ensure you are not speeding up access to fast machines at the expense of making access to slow servers even slower.

To adjust these values, edit the .network file for the connection:

The defaults of  work well for connections slower than 10 Mbit/s.  For a 100 Mbit/s connection, a value of  works well.  The manual page  says a value of  is considered excessive.

If the sysctl setting  is enabled then the connection will return to these initial settings after it has been idle for some time (and often a very small amount of time).  If this setting is disabled then the connection will maintain a higher window if a larger one was negotiated during packet transfer.  Regardless of the setting, each new TCP connection will begin with the  settings set above.

The sysctl setting  is not directly related to these values, as it controls how the congestion and receive windows are adjusted while a TCP link is active, and particularly when the path between the two hosts is congested and throughput must be reduced.  The above  values simply set the default window values selected for each new connection, before any congestion algorithm takes over and adjusts them as needed.  Setting higher initial values simply shortcuts some negotiation while the congestion algorithm tries to find the optimum values (or, conversely, setting the wrong initial values adds additional negotiation time while the congestion algorithm works towards correcting them, slowing down each newly established TCP connection for a few seconds extra).

## Prevent multiple default routes
systemd-networkd [https://github.com/systemd/systemd/issues/17698 does not set per-interface-type default route metrics, i.e. they need to be configured manually when using multiple network devices. For example, the following  shows multiple default routes:

Since the same default  value  is assigned, there is a race condition which of both is chosen as default route. Since the  device came up first, it is preferred and thus, access available via  may be ignored.

To prevent the race condition, assign different  values for the devices. See #Wired and wireless adapters on the same machine for a corresponding example.

If instead one device should not provide a default route, the  option in  and  sections can be used to omit creating the default route provided by the DHCP/RA server while keeping other classless static routes. This may be useful, for example, if the device provides a connection to a single other machine.

## Configuring a second static IP with its own MAC address on an existing interface
To make your computer appear as two completely separate devices to your router, you can create a virtual interface not just with a different IP but also with a different MAC address.

To achieve this, create a virtual interface (macvlan) on top of your physical interface with a unique MAC address:

Then add a network file as usual, using the same subnet and gateway, and avoiding the range of IP numbers used for DHCP if you configure a static IP. For example:

The macvlan interface route has metric 2. This ensures that traffic will prefer going through the main interface, since that (implicitly) has a default route with metric 1, unless specifically directed to use the macvlan interface.

Finally, add  to the  section of the .network file of your main interface!

At this point, a fast way to make your router aware of the new MAC (and configure it to accept that MAC) you can for example run  as root. After configuring your router for the "new device" you can test if the new interface has internet access with for example  that should then print your public IP number.
