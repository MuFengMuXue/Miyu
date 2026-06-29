# Open vSwitch

Open vSwitch (OVS) is a multilayer software switch. It is designed to enable massive network automation through programmatic extension, while still supporting standard management interfaces and protocols. Open vSwitch is well suited to function as a virtual switch in environments with virtual machines.

## Installation
Install the  package.

## Required services and setup
To use ovs-vswitchd, start/enable .

 will also start the  which is used for saving the OVS configuration in a database for persistent settings across reboots.

## Create a Bridge
 # ovs-vsctl add-br mybridge

Most commands can be reversed with replacing add with del, for example del-br.

Print the newly created bridge with one port with an interface named mybridge.

## Add physical adapter to the bridge
Get the current active interface and configuration:

Disable any running automated config.

If dhcpcd is running:

 # dhcpcd -k eno1

Stop  if using systemd-networkd.

Remove the current ip configuration:

 # ip addr del 192.168.1.10/24 dev eno1

Add physical interface to mybridge:

 # ovs-vsctl add-port mybridge eno1

Print the current setup:

Test the config:

## Make changes persistent over reboots
Open vSwitch will automatically apply any changes made with ovs-commands. But to get it working we need to change some things with systemd-networkd.

First, remove any old configuration for eno1 and bring the interface up during boot. We will also run DHCP on mybridge with the following config:

## Vlans
Setup trunk with vlan 10 + 20 plus tag untagged traffic to vlan 1 through the physical port:

 # ovs-vsctl set port eno1 vlan_mode=native-untagged
 # ovs-vsctl set port eno1 tag=1 # tag untagged vlan 1
 # ovs-vsctl set port eno1 trunks=10,20 # allow tagged vlans 10 and 20

Create a new vport1, type internal for use on the host system with vlan 10:

 # ovs-vsctl add-port mybridge vport1 tag=10 -- set Interface vport1 type=internal
 # dhcpcd vport1 # to test it out!

## Virtual ports
ip_forward is needed for virtual ports and support for vm's:

 # echo 1 > /proc/sys/net/ipv4/ip_forward

Manually create a tuntap interface:

 # ip tuntap add mode tap vport2

To make both the above changes persistent across reboots:

Create a new port and tag it vlan 20:

 # ovs-vsctl add-port mybridge vport2 -- set port vport2 tag=20

vport2 can now be used in libvirt.
