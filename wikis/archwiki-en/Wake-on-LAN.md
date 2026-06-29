# Wake-on-LAN

Wake-on-LAN (WoL) is a feature to switch on a computer via the network.

## Hardware settings
Wake-On-LAN only works if you fulfill the following preconditions:

# The target computer's motherboard and Network Interface Controller has to support Wake-on-LAN.
# The target computer has to be physically connected (with a cable) to a router or to the source computer for WoL to work properly unless your wireless card has support for Wake on Wireless (WoWLAN or WoW).

You have to prepare the following in your BIOS/UEFI:

# Enable the Wake-on-LAN feature. Different motherboard manufacturers use slightly different language for this feature. Look for terminology such as "PCI Power up", "Allow PCI wake up event" or "Boot from PCI/PCI-E".
# (If available in BIOS/UEFI) Make sure that ErP is disabled, otherwise your Ethernet card will not be powered and will not be able to receive any wake-up packets sent from another device.

## Software configuration
## Enable WoL on an Ethernet network adapter
Depending on the hardware, the network driver may have WoL switched off by default.

To query this status or to change the settings, install , determine the name of the network interface, and query it using the command:

The Wake-on values define what activity triggers wake up:  (disabled),  (PHY activity),  (unicast activity),  (multicast activity),  (broadcast activity),  (ARP activity), and  (magic packet activity). The value  is required for WoL to work, if not, the following command enables the WoL feature in the driver:

 # ethtool -s interface wol g

This command might not last beyond the next reboot and in this case must be repeated via some mechanism. Common solutions are listed in the following subsections.

## Enable Wake on Wireless LAN
Depending on the hardware, the network driver may have Wake on Wireless LAN (WoWLAN) switched off by default.

To query this status or to change the settings, install , and query it using the command (interface will probably be phy0):

To enable WoWLAN you need to pick several features like  and  to make WoL work:

 # iw interface wowlan enable magic-packet disconnect

This command might not last beyond the next reboot and in this case must be repeated via some mechanism. Common solutions are listed in the following subsections.

## Make it persistent
## systemd.link
Link-level configuration is possible through systemd.link files. The actual setup is performed by the  udev builtin. Add the  option to the network link file:

Also see  for more information.

## systemd service
This is an equivalent of previous  option, but uses a standalone systemd service.

Alternatively install the  package, then activate this new service by starting .

## udev
udev is capable of running any command as soon as a device is visible. The following rule will turn on WOL on all network interfaces whose name matches . The file name is important and must start with a number between 81 and 99 so that it runs after , which renames interfaces with predictable names. Otherwise,  would be undefined and the rule would not run.

The  placeholder will be replaced by the value of the  variable for the matched device.

## cron
A command can be run each time the computer is (re)booted using "@reboot" in a crontab. First, make sure cron is enabled, and then edit a crontab for the root user that contains the following line:

 @reboot /usr/bin/ethtool -s interface wol g

## netctl
If using netctl, one can make this setting persistent by adding the following the netctl profile:

## NetworkManager
NetworkManager provides Wake-on-LAN ethernet support. One way to enable Wake-on-LAN by magic packet is through nmcli.

First, search for the name of the wired connection:

By following, one can view current status of Wake-on-LAN settings:

Enable Wake-on-LAN by magic packet on that connection:

 # nmcli c modify "wired1" 802-3-ethernet.wake-on-lan magic

Then reboot, possibly two times. To disable Wake-on-LAN, substitute  with .

The Wake-on-LAN settings can also be changed from the GUI using .

You can disable Wake-on-LAN for all connections permanently by adding a dedicated configuration file :

## Enable WoL in TLP
When using TLP for suspend/hibernate, the  setting should be set to  in  to allow resuming the computer with WoL.

## Trigger a wake up
To trigger WoL on a target machine, its MAC address must be known.
To obtain it, execute the following command from the machine:

Here the MAC address is .

In its simplest form, Wake-on-LAN broadcasts the magic packet as an ethernet frame, containing the MAC address within the current network subnet, below the IP protocol layer. The knowledge of an IP address for the target computer is not necessary, as it operates on layer 2 (Data Link).

If used to wake up a computer over the internet or in a different subnet, it typically relies on the router to relay the packet and broadcast it.
In this scenario, the external IP address of the router must be known. Keep in mind that most routers by default will not relay subnet directed broadcasts as a safety precaution and need to be explicitly told to do so.

Applications that are able to send magic packets for Wake-on-LAN:

*
*
*

## On the same LAN
If you are connected directly to another computer through a network cable, or the traffic within a LAN is not firewalled, then using Wake-on-LAN should be straightforward since there is no need to worry about port redirects.

In the simplest case the default broadcast address  is used:

 $ wol target_MAC_address

To broadcast the magic packet only to a specific subnet or host, use the  switch:

 $ wol -i target_IP target_MAC_address

## Across the internet
When the source and target computers are separated by a NAT router, different solution can be envisaged:

* If the router supports WoL, one can rely on it to properly broadcast the packet into the local network.

Otherwise Wake-on-LAN can be achieved via port forwarding. The router needs to be configured using one of these two options:

* Forward a different port to each target machine. This requires any target machine to have a static IP address on its LAN.
* Forward a single port to the broadcast address. Most routers do not allow to forward to broadcast, however if you can get shell access to your router, through telnet, ssh, serial cable or other mean, run the command:  This example assumes the network is 192.168.1.0/24 and uses net0 as network interface. Now, forward UDP port 9 to 192.168.1.254. This solution was successfully tested on a Linksys WRT54G running Tomato, and on the Verizon FIOS ActionTec router. For notes on how to do it on a router with DD-WRT firmware, see this tutorial and for a router with OpenWrt firmware, see this tutorial.

In any case, run the following command from the source computer to trigger wake-up:

 $ wol -p forwarded_port -i router_IP target_MAC_address

## Miscellaneous
## Check reception of the magic packets
In order to make sure the WoL packets reach the target computer, one can listen to the UDP port, usually port 9, for magic packets.
The magic packet frame expected contains 6 bytes of FF followed by 16 repetitions of the target computer's MAC (6 bytes each) for a total of 102 bytes.

## Using netcat
This can be performed by installing  on the target computer and using the following command:

 # nc -u -l 9 | xxd

Then wait for the incoming traffic to appear in the  terminal.

## Using ngrep
Install  on the target computer and type the following command:

 # ngrep '\xff{6}(.{6})\1{15}' -x port 9

## Example of WoL script
Here is a script that illustrates the use of  with different machines:

## Troubleshooting
## NetworkManager
## Network adapter is still powered off on shutdown
Setting auto negotiation to  may help if WOL is configured through nmcli and network adapter is still powered off on shutdown.

Set it using:

 # nmcli c modify "wired1" 802-3-ethernet.auto-negotiate yes

## Wake-up after shutdown
It is known that some motherboards are affected by a bug that can cause immediate or random wake-up after a shutdown whenever the BIOS WoL feature is enabled (as discussed in this thread for example).

## Fix using BIOS Settings
The following actions in the BIOS preferences can solve this issue with some motherboards:

# Disable all references to xHCI in the USB settings (note this will also disable USB 3.0 at boot time)
# Disable EuP 2013 if it is explicitly an option
# Optionally enable wake-up on keyboard actions

## Fix by kernel quirks
The issue can also be solved by adding the following kernel boot parameter:
This activates the following quirks:

*
*

## Battery draining problem
Some laptops have a battery draining problem after shutdown This might be caused by enabled WOL. To solve this problem, disable it by using ethtool as mentioned above.

 # ethtool -s net0 wol d

## Realtek
## r8168
Users with a Realtek 8168 8169 8101 8111(C) based NICs (cards / and on-board) may notice a problem where the NIC seems to be disabled on boot and has no link light. See Network configuration/Ethernet#Realtek no link / WOL problem.

If the link light on the network switch is enabled when the computer is turned off but Wake on LAN is still not working, booting the system using the  kernel module at least once and then switching back to the  kernel module included with the kernel has been reported to fix it.

For the  module you might need to set the  kernel module parameter to enable the wake on LAN functionality.

## r8125
Users with a Realtek 8125 NIC have reported being unable to use the Wake on LAN feature with the  kernel module. Installing  enables the functionality.

Make sure the correct kernel driver is in use with . If not, blacklist the  module.

Additionally, it might be necessary to enable WOL support and disable power saving features of the card.

## alx driver support
For some newer Atheros-based NICs (such as Atheros AR8161 and Killer E2500), WOL support has been disabled in the mainline  module due to a bug causing unintentional wake-up (see [https://lore.kernel.org/netdev/1372880891-12320-1-git-send-email-johannes@sipsolutions.net/ this patch discussion). A patch can be applied (or installed as a DKMS module using the  package) which both restores WOL support and fixes the underlying bug, as outlined in this thread.

See also the pre-patched sources in https://github.com/Snugface/alx.
