# Software access point

A software access point, also called virtual router or virtual Wi-Fi, enables a computer to turn its wireless interface into a Wi-Fi access point. It saves the trouble of getting a separate wireless router.

## Requirements
## Wi-Fi device must support AP mode
You need an nl80211 compatible wireless device, which supports the AP wireless mode. This can be verified by running the  command, under the  block there should be  listed:

## Wireless client and software AP with a single Wi-Fi device
Creating a software AP is independent from your own network connection (Ethernet, wireless, ...). Many wireless devices even support simultaneous operation both as AP and as wireless "client" at the same time. Using that capability you can create a software AP acting as a "wireless repeater" for an existing network, using a single wireless device. The capability is listed in the following section in the output of :

{{hc|1=$ iw list|2=
Wiphy phy1
...
        valid interface combinations:
                 * #{ managed } <= 2048, #{ AP, mesh point } <= 8, #{ P2P-client, P2P-GO } <= 1,
                   total <= 2048, #channels <= 1, STA/AP BI must match
...
}}

The constraint  means that your software AP must operate on the same channel as your Wi-Fi client connection; see the  setting in  below.

If you want to use the capability/feature, perhaps because an Ethernet connection is not available, you need to create two separate virtual interfaces for using it.
Virtual interfaces for a physical device  can be created as follows:
The virtual interfaces with unique MAC address are created for the network connection () itself and for the software AP/hostapd "wireless repeater":

 # iw dev wlan0 interface add wlan0_sta type managed addr 12:34:56:78:ab:cd
 # iw dev wlan0 interface add wlan0_ap  type managed addr 12:34:56:78:ab:ce

These can be made persistent using  as described in BBS#236923. Alternatively if systemd-networkd is not in use, a systemd unit file can be created:

Random MAC address can be generated using macchanger.

## Configuration
Setting up an access point consists of two main parts:
# Setting up the Wi-Fi link layer, so that wireless clients can associate to your computer's software access point and exchange IP packets with it.
# Setting up the network configuration on your computer, so that it properly relays IP packets between its own internet connection and the wireless clients.

## Wi-Fi link layer
The actual Wi-Fi link is established via the  package, which has WPA2 support.

hostapd comes with a default configuration file which includes numerous options listed and corresponding descriptions, you might want to take a look to gather some basic knowledge.

Adjust the options in hostapd configuration file if necessary. Especially, change the  and the .  and  can be enabled for latest Wi-Fi 5 and Wi-Fi 6 adapters. The option  affects your AP's capabilities including channel width which is important to transfer speed.

See hostapd Linux documentation page for more information.

For automatically starting hostapd on boot, enable the .

If you are starting hostapd on boot, make sure the wireless network interface is brought up first, otherwise it will fail. To ensure your wireless interface is ready, edit the unit configuration file and state that it is bound to and should start after your network interface:

Also make sure that the interface is not managed by other network managers. If you are using NetworkManager, see NetworkManager#Ignore specific devices.

## Network configuration
There are two basic ways for implementing this:
# bridge: creates a network bridge on your computer, wireless clients will appear to access the same network interface and the same subnet that is used by your computer.
# NAT: with IP forwarding/masquerading and DHCP service, wireless clients will use a dedicated subnet, data from/to that subnet is NAT-ted. This is similar to a normal Wi-Fi router which is connected to the internet.

The bridge approach is simpler, but it requires that any service that is needed by the wireless clients, in particular DHCP, is available on the computer's external interface. This means it will not work if the external modem which assigns IP addresses, supplies the same one to different clients.

The NAT approach is more versatile, as it clearly separates Wi-Fi clients from your computer and it is completely transparent to the outside world. It will work with any kind of network connection, and (if needed) traffic policies can be introduced using the usual iptables approach.

It is possible to combine these two approaches: for example having a bridge that contains both an ethernet device and the wireless device with a static ip, offering DHCP and setting NAT configured to relay the traffic to an additional network device connected to the WAN.

## Bridge setup
You need to create a network bridge and add your network interface (e.g. ) to it. You should not add the wireless device (e.g. ) to the bridge; hostapd will add it on its own.

See Network bridge.

## NAT setup
See Internet sharing#Configuration for configuration details.

In that article, the device connected to the LAN is . That device would be in this case your wireless device (e.g. ).

## Tools
## linux-wifi-hotspot
The  package provides a script that can create either a bridged or a NATed access point for internet sharing. It combines hostapd, dnsmasq and iptables for the good functioning of the access point. Includes both command line and gui. The basic syntax to create a NATed virtual network is the following:

 # create_ap wlan0 eth0 MyAccessPoint MyPassPhrase

Alternatively, the template configuration provided in  can be adapted to ones need and the script run with:

 # create_ap --config /etc/create_ap.conf

To use the GUI, run in terminal:

 # wihotspot

Enable/start the  to run the script at boot time with the configuration specified in .

For more information see linux-wifi-hotspot on GitHub.

## RADIUS
See the FreeRADIUS wiki for instructions.

## nm-connection-editor
Install the  package to be able to actually share the connection. Note that NetworkManager starts its own instance of dnsmasq, independent of , as a DHCP server.

It is not possible to create hotspot using the .

* Open  ("Edit Connections" will open the it from nm-applet application menu in )
* Click the "+" button in the lower right then "Wi-Fi" as the Connection Type and Press "Create...".
* In the Wi-Fi tab change the Mode to "Hotspot" and fill rest of the options.

## Troubleshooting
## WLAN is very slow
Frequent causes for a lower than expected throughput include

* An improper choice of operation mode with a  lower than the one supported can limit the router artificially. Check that a modern operating mode is selected.
* A crowded or otherwise noise afflicted  can severely degrade performance especially in densely populated areas. Try changing to a different channel or even switch frequencies.
* Unset or improperly set regulatory domain.

## NetworkManager is interfering
hostapd may not work, if the device is managed by NetworkManager. You can mask the device using MAC:

Or interface name:

## Cannot start AP mode in 5 GHz band
Apparently with the special country code  (global), all usable frequencies in the 5Ghz band will have the  (no-initiating-radiation) flag set, which will prevent hostapd from using them. You will need to have  installed and have your country code set to make frequencies allowed in your country available for hostapd.

Note that recent Intel devices have a Location-Aware Regulatory (LAR) feature, which ignores the userspace regulatory database and instead deduces the regulatory region by listening to other nearby access points.  This means the devices will not transmit on any 5 GHz frequencies until they have first seen other access points on the 5 GHz frequency bands, preventing any 5 GHz transmission at all in many cases. Older kernels had an option to disable this which was removed in 2019 due to it causing the firmware to crash.  Since this removal, Intel cards supporting LAR can no longer be used as access points in the 5 GHz band.

## Windows 10+ refuses to connect with hostapd using WPA3
Windows seems to refuse connecting to WPA3 access points with . Using  instead of  may solve the issue.

## Access point does not accept running in 40Mhz mode (HT)
You may receive the following message:
 20/40 MHz operation not permitted on channel pri=13 sec=9 based on overlapping BSSes

That means that too many nearby access points are detected by your Wi-Fi device. It then refuses to use more than 20Mhz channel width in order to share more fairly the wireless spectrum.
You may be able to disable that with , but that may likely violate local regulatory requirements.
