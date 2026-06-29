# VLAN

Virtual LANs give you the ability to subdivide a LAN. Linux can accept VLAN tagged traffic and presents each VLAN ID as a different network interface (eg:  for VLAN ID ).

This article explains how to configure a VLAN using  and systemd-networkd or netctl.

## Instant Configuration
In the following examples, let us assume the interface is , the assigned name is  and the VLAN ID is .

## Create the VLAN device
Add the VLAN interface with the following command:

 # ip link add link eth0 name eth0.100 type vlan id 100

Run  to confirm that it has been created.

This interface behaves like a normal interface. All traffic routed to it will go through the master interface (in this example, ) but with a VLAN tag. Only VLAN-aware devices can accept them if configured correctly, else the traffic is dropped.

Using a name like  is just convention and not enforced; you can alternatively use  or something descriptive like . To see the VLAN ID on an interface, in case you used an unconventional name:

 # ip -details link show eth0.100

The  () flag shows full details of an interface:

 # ip -details addr show
 4: eth0.100@eth0:  mtu 1500 qdisc noqueue state UP group default
    link/ether 96:4a:9c:84:36:51 brd ff:ff:ff:ff:ff:ff promiscuity 0
    vlan protocol 802.1Q id 100
    inet6 fe80::944a:9cff:fe84:3651/64 scope link
       valid_lft forever preferred_lft forever

## Add an IP
Now add an IPv4 address to the just created VLAN link, and activate the link:

## Turning down the device
To cleanly shut down the setting before you remove the link, you can do:

## Removing the device
Removing a VLAN interface is significantly less convoluted

## Persistent Configuration
## systemd-networkd
## Single interface
Use the following number-prefixed configuration files (Remember the file contents are case sensitive and the number-prefix can be changed):

You will have to have associated .network files for each .netdev to handle addressing and routing. For example, to set the eth0.100 interface with a static IP and the eth0.200 interface with DHCP (but ignoring the supplied default route), use:

Then enable . See systemd-networkd for details.

## Single interface with multiple VLANs each with its own gateway
Each vlan gets its own routing table and a RoutingPolicyRule that specifies which source ip addresses this routing applies to.

## Checks
Use . E.g.:

## Bonded interface
Similar to above, you are just going to stack more of the concepts in place. You will want to ensure that you have got a bond set up in your switch and also make sure its a trunk with tagged vlans corresponding to what you create below. Convention would be to create a bond interface with the name , however there is a known issue where the  module, when loaded, creates a bond device of the name  which systemd then refuses to configure (as systemd tries to respectfully leave alone any device it did not create).

For the purposes of this write up, we are going to use  and you can make the choice yourself.

First, we create the bond device:

Now create a .network directive that references the vlans and interface carriers. In this case we will use the convention for a dual port fiber module:

We are using the vlan naming convention here, you can use something else but realize that this is a named reference so you will have to have a corresponding set of files with the same name.

We will now set up the physical network interfaces:

At this time you could reboot, and likely should, because the bonded interface is created at boot time. Restarting systemd-networkd will consume changes from these files typically, but device creation seems to occur at startup.

We will now set up the VLANs. You should be aware that having multiple VLANs can result in a situation where your machine has multiple default routes, so you will need to specify a Destination directive in the network directives to ensure that only one VLAN is being used for a default route. In this case we will use the VLAN with an ID of 10 as our default route.

Now create the associated network directive to set an address:

We will create a similar pair of files for the VLAN with an ID of 20:

And again for the VLAN with an ID of 30:

Note that the Destination on  is set to , which will match all outbound, becoming the default route.

## netctl
You can use netctl for this purpose, see the self-explanatory example profiles in {{ic|/etc/netctl/examples/vlan-{dhcp,static}}}.

## Setting bridge IP
Sometimes you might want to configure the bridge ip on which docker operates, for example when the default ip clashes with other ip addresses in the network. Docker has a straight forward way of setting the  (bridge IP) via the . When this file does not exist yet you can create it.
{{hc|/etc/docker/docker.json|2=
{
    "bip": "/24"
}
}}

## Troubleshooting
## udev renames the virtual devices
An annoyance is that udev may try to rename virtual devices as they are added, thus ignoring the  configured for them (in this case ):

This could generate the following output:

udev has ignored the configured virtual interface name  and named it .

The solution is to edit  and append  to the end of the physical interface configuration line.

For example, for the interface  ():
{{hc|/etc/udev/rules.d/network_persistent.rules|
SUBSYSTEM=="net", ATTR{address}=="aa:bb:cc:dd:ee:ff", NAME="eth0", DRIVERS=="?*"
}}

A reboot should mean that VLANs configure correctly with the names assigned to them.
