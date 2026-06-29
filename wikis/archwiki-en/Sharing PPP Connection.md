# Sharing PPP Connection

## Requirements
Before proceeding, you must make sure:
# You must have a working PPP connection.
# You must have an extra Ethernet interface card in your computer with which to share your connection.

## Installing
The following packages must be installed for both Wired and Wireless sharing:

* : for controlling packets in your network.
* : for acting as a DHCP and DNS caching server.
* : for setting up a network bridge.

Depending on whether you want to share a wireless or wired connection, you also have to install:

* wired:  or  (this article uses  since  is deprecated).
* wireless:  or  (this article uses  since  is deprecated).

## Sharing via wired ethernet
* Set the PPP connection up.
: You can assign an IP address to the interface as usual, by running (as root):
 # ip addr add 192.168.0.254 dev eth0
* Set the kernel to router mode. This is done by running:
 # sysctl net.ipv4.ip_forward=1
* Configure dnsmasq. Make the following changes to  (uncomment if necessary):

* Start the dnsmasq daemon.
* Finally, set firewall to forward connections to and from the Internet for clients connecting to your WLAN. This is done by issuing:
 # iptables -t nat -A POSTROUTING -o ppp0 -j MASQUERADE
:In the above the ppp0 interface is the used PPP interface, you can substitute it for yours if needed.
* You are done! Happy surfing!

## Network bridge
Let us assume your PPP connection is on eth0, and you want to share the connection on eth1 and eth2.

 # ip addr add 0.0.0.0 dev eth1  # remove IP from eth0
 # ip link set eth1 up           # ensure the interface is up

 # ip addr add 0.0.0.0 dev eth2  # remove IP from eth1
 # ip link set eth2 up           # ensure the interface is up

 # brctl addbr br0               # create br0 node
 # brctl addif br0 eth1          # add eth0 to bridge br0
 # brctl addif br0 eth2          # add eth1 to bridge br0

 # ip addr add 192.168.0.254 dev br0
change your interface in  to br0:
 interface=br0
and restart the dnsmasq daemon.

Now you should be able to connect to the internet using eth1 or eth2.

## Sharing via WLAN
* Set up the PPP connection.
* Set up the WLAN connection: choose an SSID and select Ad-hoc as network type. In the following it is assumed that you are using the wlan0 interface.

: Set the wlan0 interface up address for example 192.168.0.254. Setting up the interface is usually done by running:
 # iw wlan0 set type ibss
 # iw wlan0 ibss join MyFreeWlan

: After that you can assign an IP address to the interface as usual, by running:
 # ip addr add 192.168.0.254 dev wlan0
: Please note that different wlan cards may be configured differently and one should adapt this documentation accordingly.
* Set the kernel to router mode. This is done by running:
 # echo 1 > /proc/sys/net/ipv4/ip_forward
* Configure dnsmasq. Make the following changes to  (uncomment if necessary):

* Start the dnsmasq daemon.
* Finally, set firewall to forward connections to and from the Internet for clients connecting to your WLAN. This is done by issuing:
 # iptables -t nat -A POSTROUTING -o ppp0 -j MASQUERADE

: In the above the ppp0 interface is assumed to be the used PPP interface, you can substitute it for yours if needed.
* You are done! Happy surfing!

## Sharing script
A quick script for sharing eth0 over wlan0 on an ad-hoc network.
