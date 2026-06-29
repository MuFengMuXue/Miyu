# GNS3

Graphical Network Simulator 3 (shortened to GNS3) is a network software emulator first released in 2008. It allows the combination of virtual and real devices, and is used to simulate complex networks.

GNS3 can incorporate virtual machines, Linux Containers, and emulated network hardware into its topologies, and can connect the simulated network to physical devices.

See the official documentation for more information.

## Installation
## Local
Install  and  packages to run the GNS3 locally. Local installation, as opposed to running the official GNS3 virtual machine, could be used to increase performance, as a result of eliminating overhead from the hypervisor.

Enable/start the  service, where user is the username for the user-level account on which GNS3 will be run.

libvirt can be used to create the end devices "Cloud" (providing a virtual wan interfaces, isolating the tested network to the other devices in the main network) and NAT. To make libvirt work correctly, GNS3 needs dnsmasq and . Install them and ensure the libvirtd daemon is running before using GNS3 with Cloud and NAT end devices.

Install  and  to use VirtualBox machines in a topology.

Install Wireshark to sniff packets from the links between devices of a virtual topology.

## The official virtual machine
The official GNS3 virtual machine, which is Ubuntu with GNS3 preinstalled, could be used as an alternative to local installation. Go to GNS3 Github and download the VirtualBox version of the GNS3 virtual machine with the exact same version number as your GNS3 version. Unzip and import the virtual machine in VirtualBox.

To create a network connection between the GNS3 virtual machine and the host OS, a host-only network must be configured. In File > Host Network Manager, set up a host-only network. In most cases, it will be called  or similar. Note the IP address dedicated to the interface in the GUI. For some reason, VirtualBox does not assign the IP to the interface, nor does it enable it. Therefore, this must be performed manually in the terminal. See Network configuration#Routing table for more information on assigning IP addresses.

 # ip addr add IP_address/subnet_mask dev vboxnet0
 # ip link set dev vboxnet0 up

Launch the GNS3 startup wizard, select the GNS3 virtual machine, and it should be able to start the virtual machine.

## VPCS
Virtual PC Simulator (VPCS) is a small program (it consumes 2MB of RAM per instance), which allows you to simulate a lightweight PC supporting basic networking things like setting the IP address (statically or by DHCP), and a few simple network commands like arp, ping and traceroute.

VPCS is not a virtual machine by any means, so you can not add any additional features or services into it.

Install the  package to use VPCS.

## Dynamips
Dynamips is an emulator of old (End-of-Life) Cisco 7200, 3700, 3600, 2600 and 1700 series routers.

Packet over SONET/SDH (POS) is the only technology, which can not be simulated with IOL or IOSv. To work with POS you need to use c7200 platform with PA-POS-OC3 port adapter module.

Install the  package to use Dynamips.

## Troubleshooting
## GNS3 virtual machine is not on the same network as the local server
The following warning may be encountered:

 The GNS3 VM (IP 192.168.56.101, NETWORK 192.168.56.0/24) is not on the same network as the local server (IP 127.0.0.1, NETWORK 127.0.0.0/8), please make sure the local server binding is in the same network as the GNS3 VM

To fix this, go to the Edit > Preferences > Server > Host Binding drop-down menu, and change the binding of the local server to whichever IP address (sub-net and mask) matches the IP address listed on the Information screen in the GNS3 virtual machine. See https://gns3.com/initiatives/gns3-vm-is-not-on-the-same-netwo.

## virbr0 does not exist, please install libvirt
If  is installed, but  does not exist, that means the default network has not been started through libvirt, and you will not be able to setup a NAT in GNS3.

To temporarily start the default network, use virsh:

 # virsh net-start default

And to auto-start it on reboot:

 # virsh net-autostart default

## IOU images require a valid license key
In order to start IOU images you need to put a valid license in ~/.iourc. Apparently, the key depends on your active NIC. It needs to be re-generated  changing from wired to wireless connections on laptops. Unfortunately, the GNS3 GUI does not throw a meaningful error message this case. The IOU image just will not start.
