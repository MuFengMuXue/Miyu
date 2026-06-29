# MAC address spoofing

Media Access Control (MAC) randomization can be used for increased privacy by not disclosing your real MAC address to the network.
This article gives several methods to spoof a MAC address.

## Manually
There are two methods for spoofing a MAC address: installing and configuring either  or . Both of them are outlined below.

## iproute2
First, you can check your current MAC address with the command:

 # ip link show interface

where  is the name of your network interface.

The section that interests us at the moment is the one that has "link/ether" followed by a 6-byte number. It will probably look something like this:

 link/ether 00:1d:98:5a:d1:3a

The first step to spoofing the MAC address is to bring the network interface down. It can be accomplished with the command:

 # ip link set dev interface down

Next, we actually spoof our MAC. Any hexadecimal value will do, but some networks may be configured to refuse to assign IP addresses to a client whose MAC does not match up with any of known vendors. Therefore, unless you control the network(s) you are connecting to, use MAC prefix of any real vendor (basically, the first three bytes), and use random values for next three bytes. For more information please read Wikipedia:Organizationally unique identifier.

To change the MAC, we need to run the command:

 # ip link set dev interface address XX:XX:XX:XX:XX:XX

Where any 6-byte value will suffice for .

The final step is to bring the network interface back up. This can be accomplished by running the command:

 # ip link set dev interface up

If you want to verify that your MAC has been spoofed, simply run  again and check the value for 'link/ether'. If it worked, 'link/ether' should be whatever address you decided to change it to.

## macchanger
Another method uses  (a.k.a., the GNU MAC Changer). It provides a variety of features such as changing the address to match a certain vendor or completely randomizing it.

Install the package .

The spoofing is done on per-interface basis, specify network interface name as  in each of the following commands.

The MAC address can be spoofed with a fully random address:

 # macchanger -r interface

To randomize only device-specific bytes of current MAC address (that is, so that if the MAC address was checked it would still register as being from the same vendor), you would run the command:

 # macchanger -e interface

To change the MAC address to a specific value, you would run:

 # macchanger --mac=XX:XX:XX:XX:XX:XX interface

Where  is the MAC you wish to change to.

Finally, to return the MAC address to its original, permanent hardware value:

 # macchanger -p interface

## Automatically
## systemd-udevd
udev allows you to perform MAC address spoofing by creating  files or udev rules.

## systemd.link
To set a static spoofed MAC address:

To randomize the MAC address on every boot, set  instead of .

## udev rule
Use  attribute to match the correct device by its original MAC address and change it using the  command:

{{hc|/etc/udev/rules.d/81-mac-spoof.rules|2=
ACTION=="add", SUBSYSTEM=="net", ATTR{address}=="original MAC", RUN+="/usr/bin/ip link set dev $name address spoofed MAC"
}}

## systemd unit
## Creating unit
Below you find two examples of systemd units to change a MAC address at boot, one sets a static MAC using ip and one uses macchanger to assign a random MAC address. The systemd  is used to ensure the MAC is changed before a network manager like Netctl or NetworkManager, systemd-networkd or dhcpcd service starts.

## iproute2
systemd unit setting a predefined MAC address:

## macchanger
systemd unit setting a random address while preserving the original NIC vendor bytes. Ensure that  is installed:

A full random address can be set using the  option, see #macchanger.

## Enabling service
Append the desired network interface to the service name (e.g. ) and enable the service (e.g. ).

Reboot, or stop and start the prerequisite and requisite services in the proper order. If you are in control of your network, verify that the spoofed MAC has been picked up by your router by examining the static, or DHCP address tables within the router.

## netctl interfaces
You can use a netctl hook to run a command each time a netctl profile is re-/started for a specific network interface. Replace  accordingly:

Make the script executable.

Source: akendo.eu (archive)

## NetworkManager
NetworkManager supports two types MAC Address Randomization: randomization during scanning, and for network connections. Both modes can be configured by modifying  or by creating a separate configuration file in  which is recommended since the aforementioned configuration file may be overwritten by NetworkManager.

Randomization during Wi-Fi scanning is enabled by default, but it may be disabled by adding the following lines to  or a dedicated configuration file under :

MAC randomization for network connections can be set to different modes for both wireless and ethernet interfaces.

In terms of MAC randomization the most important modes are  and .  generates a random MAC address when you connect to a new network and associates the two permanently. This means that you will use the same MAC address every time you connect to that network. In contrast,  will generate a new MAC address every time you connect to a network, new or previously known. You can configure the MAC randomization by adding the desired configuration under :

To configure MAC randomization for a specific connection (for example, if the network does not like random MAC addresses), edit the connection to set  to one of the modes (e.g.  or ).

See the following GNOME blog post for more details.

## wpa_supplicant
wpa_supplicant can use random MAC address for each ESS connection(AP) (see for details).

Add this to your configuration:

## iwd
To randomize the MAC address when iwd starts (see  for details):

Specifying  enables control over when MAC address is randomized. If set to  MAC is not spoofed and  is ignored. If set to  MAC is assigned every time iwd is started. If set to  MAC is spoofed once for each network and reused for each connection to a known network.

Specifying  enables control over which part of the address is randomized. If set to , only the NIC specific octets (last three octets) are randomized. The permanent mac address of the network interface is used for the initial 3 octets. If set to , all six octets of the address are randomized.

## Troubleshooting
## Connection to DHCPv4 network fails
If you cannot connect to a DHCPv4 network and you are using dhcpcd, you might need to modify the dhcpcd configuration to obtain a lease.
