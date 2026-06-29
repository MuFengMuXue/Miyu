# Dhcpcd

dhcpcd is a DHCP and DHCPv6 client. It is currently the most feature-rich open source DHCP client; see the home page for the full list of features.

## Installation
Install the  package.

 is a GTK frontend for the dhcpcd daemon, and optionally wpa_supplicant. It features a configuration dialogue and the ability to enter a pass phrase for wireless networks.

## Running
To start the daemon for all network interfaces, start/enable .

To start the daemon for a specific interface alone, start/enable the template unit , where interface can be found with Network configuration#Listing network interfaces.

Using the template unit is recommended; see #dhcpcd and systemd network interfaces for details. In either case, you will be assigned a dynamic IP address. To assign a static IP address, see #Static profile.

## Configuration
The main configuration is done in . See  for details. Some of the frequently used options are highlighted below.

## DHCP static route(s)
If you need to add a static route client-side, add it to . The example shows a new hook-script which adds a static route to a VPN subnet on  via a gateway machine at :

You can add multiple routes to this file.

## DHCP Client Identifier
The DHCP client may be uniquely identified in different ways by the server:

# hostname (or the hostname value sent by the client),
# MAC address of the network interface controller through which the connection is being made, linked to this is the third,
# Identity Association ID (IAID), which is an abstraction layer to differentiate different use-cases and/or interfaces on a single host,
# DHCP Unique Identifier (DUID).

For a further description, see RFC 3315.

It depends on the DHCP-server configuration which options are optional or required to request a DHCP IP lease.

If the dhcpcd default configuration fails to obtain an IP, the following options are available to use in :

*  sends the hostname set in
*  sends the MAC address as identifier
*  derives the IAID to use for DHCP discovery. It has to be used in an interface block (started by , see but more frequently the next option is used:
*  triggers using a combination of DUID and IAID as identifier.

The DUID value is set in . For efficient DHCP lease operation it is important that it is unique for the system and applies to all network interfaces alike, while the IAID represents an identifier for each of the systems' interfaces (see RFC 4361).

Care must be taken on a network running Dynamic DNS to ensure that all three IDs are unique. If duplicate DUID values are presented to the DNS server, e.g. in the case where a virtual machine has been cloned and the hostname and MAC have been made unique but the DUID has not been changed, then the result will be that as each client with the duplicated DUID requests a lease the server will remove the predecessor from the DNS record.

## Static profile
Required settings are explained in Network configuration. These typically include the network interface name, IP address, router address, and name server.

Configure a static profile for dhcpcd in , for example:

More complicated configurations are possible, for example combining with the  option. See  for details.

## Fallback profile
It is possible to configure a static profile within dhcpcd and fall back to it when DHCP lease fails. This is useful particularly for headless machines, where the static profile can be used as "recovery" profile to ensure that it is always possible to connect to the machine.

The following example configures a  profile with  as IP address,  as gateway and name server, and makes this profile fallback for interface .

## Hooks
dhcpcd executes all scripts found in  in a lexical order. See  and  for details.

## 10-wpa_supplicant
Enable this hook by creating a symbolic link, which ensures the current version is used, even after package updates:

 # ln -s /usr/share/dhcpcd/hooks/10-wpa_supplicant /usr/lib/dhcpcd/dhcpcd-hooks/

The  hook, if enabled, automatically launches wpa_supplicant on wireless interfaces. It is started only if:

* no wpa_supplicant process is already listening on that interface.
* a wpa_supplicant configuration file exists. dhcpcd checks

 /etc/wpa_supplicant/wpa_supplicant-interface.conf
 /etc/wpa_supplicant/wpa_supplicant.conf
 /etc/wpa_supplicant-interface.conf
 /etc/wpa_supplicant.conf

by default, in that order, but a custom path can be set by adding  into .

If you manage wireless connections with wpa_supplicant itself, the hook may create unwanted connection events. For example, if you stop wpa_supplicant the hook may bring the interface up again. Also, if you use netctl-auto, wpa_supplicant is started automatically with  for config, so starting it again from the hook is unnecessary and may result in boot-time parse errors of the  file, which only contains dummy values in the default packaged version.

To disable the hook remove the symbolic link you added, or add  to .

## Tips and tricks
## Speed up DHCP by disabling ARP probing
dhcpcd contains an implementation of a recommendation of the DHCP standard (RFC 2131) to verify via ARP if the assigned IP is not used by something else. This is usually not needed in home networks, so it is possible to save about 5 seconds on every connect by disabling it:

This is equivalent to passing  to , and disables the described ARP probing, speeding up connections to networks with DHCP.

## Remove old DHCP lease
The file , where  is the name of the interface on which you have a lease, contains the actual DHCP lease reply sent by the DHCP server. For a wireless interface, the filename is , where  is the name of the wireless network. It is used to determine the last lease from the server, and its  attribute is used to determine when it was issued. This last lease information is then used to request the same IP address previously held on a network, if it is available. If you do not want that, simply delete this file.

If the DHCP server still assigns the same IP address, this may happen because it is configured to keep the assignment stable and recognizes the requesting DHCP client id or DUID (see #DHCP Client Identifier). You can test it by stopping dhcpcd and removing or renaming . dhcpcd will generate a new one on next run.

Keep in mind that the DUID is intended as persistent machine identifier across reboots and interfaces. If you are transferring the system to new computer, preserving this file should make it appear as old one.

## Different IPs when multi-booting
If you are dualbooting Arch and macOS or Windows and want each to receive different IP addresses, you can exert control about the IPs leased by specifying a different DUID in each operating system installation.

In Windows the DUID should be stored in the

 \HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip6\Parameters\Dhcpv6DUID
registry key.

On macOS it is directly accessible in .

If you are using a dnsmasq DHCP server, the different DUIDs can be used in appropriate  rules in its configuration.

## /etc/resolv.conf
If resolvconf is available, DNS information will be sent to it; otherwise, dhcpcd itself will write to .

 overwriting can be stopped by disabling the hook . Do so by adding the following to the last section of :

 nohook resolv.conf

Note that disabling this hook also disables dhcpcd's use of resolvconf in general.

Alternatively, you can create a file called  containing your DNS servers. dhcpcd will prepend this file to the beginning of .

Or you can configure dhcpcd to use the same DNS servers every time. To do this, add the following line at the end of your , where  is a space separated list of DNS IP addresses.

 static domain_name_servers=dns-server-ip-addresses

For example, to set it to Google's DNS servers:

 static domain_name_servers=8.8.8.8 8.8.4.4

## Troubleshooting
## Client ID
If you are on a network with DHCPv4 that filters Client IDs based on MAC addresses, you may need to change the following line:

To:

Else, you may not obtain a lease since the DHCP server may not read your DHCPv6-style Client ID correctly. See RFC 4361 for more information.

## Check DHCP problem by releasing IP first
A problem may occur when DHCP gets a wrong IP assignment, such as when two routers are tied together through a VPN. The router that is connected through the VPN may be assigning IP address. To fix it, as root, release the IP address:

 # dhcpcd -k

Then request a new one:

 # dhcpcd

You may have to run those two commands many times.

## Problems with noncompliant routers
For some (noncompliant) routers, you will not be able to connect properly unless you comment the line

 require dhcp_server_identifier

in . This should not cause issues unless you have multiple DHCP servers on your network (not typical); see [https://technet.microsoft.com/en-us/library/cc977442.aspx this page for more information.

## dhcpcd and systemd network interfaces
 can be enabled without specifying an interface. This may, however, create a race condition at boot with systemd-udevd trying to apply a predictable network interface name:
 error changing net interface name wlan0 to wlp4s0: Device or resource busy"

To avoid this problem use  or  in  to stop dhcpcd from binding to kernel names, for example:

 denyinterfaces wlan* eth*

It is also possible to enable dhcpcd on a per interface basis as described in #Running. The downside of the template unit is, however, that it does not support hot-plugging of a wired connection and will fail if the network cable is not connected. To work-around the failure, see #Timeout delay.

## Timeout delay
If dhcpcd operates on a single interface and fails to obtain a lease after 30 seconds (for example when the server is not ready or the cable not plugged), it will exit with an error.

To have dhcpcd wait indefinitely for one-time, edit the unit and set the  option to :

To have it wait indefinitely, let the unit restart after it exited:

## Known issues
## dhcpcd@.service causes slow startup
By default the  waits to get an IP address before forking into the background via the  flag for dhcpcd. If the unit is enabled, this may cause the boot to wait for an IP address before continuing. To fix this, create a drop-in file for the unit with the following:

See also .
