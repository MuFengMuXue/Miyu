# Netctl

netctl is a CLI and profile-based network manager and an Arch project.

## Installation
Install the  package.

netctl's #Special systemd units used in automating connections require some additional dependencies; see that section for more information.

Other optional dependencies are shown in the table below.

{| class="wikitable"
! Feature
! Dependency
|-
| WPA ||
|-
| DHCP ||  or
|-
| wifi-menu ||
|-
| PPPoE ||
|-
|}

## Configuration
netctl uses profiles to manage network connections and different modes of operation to start profiles automatically or manually on demand.

The netctl profile files are stored in  and example configuration files are available in .

To use an example profile, simply copy it from  to  and configure it to your needs; see basic #Example profiles below. The first parameter you need to create a profile is the network , see Network configuration#Network interfaces for details.

See  for a complete list of profile options.

## Usage
See  for a complete list of netctl commands.

## Starting a profile
Once you have created your profile, attempt to establish a connection, where profile is only the profile name, not the full path:

 # netctl start profile

If the above command results in a failure, then run  as root and  to obtain a more in-depth explanation of the failure.

## Enabling a profile
A profile can be enabled to start at boot by using:

 # netctl enable profile

This will create and enable a systemd service that will start when the computer boots. Changes to the profile file will not propagate to the service file automatically. After such changes, it is necessary to reenable the profile:

 # netctl reenable profile

After enabling a profile, it will be started at next boot. Obviously this can only be successful, if the network cable for a wired connection is plugged in, or the wireless access point used in a profile is in range respectively.

If you need to switch multiple profiles frequently (i.e., traveling with a laptop), use #Special systemd units instead of enabling a profile.

## Special systemd units
netctl provides special systemd services for automatically switching of profiles for wired and wireless connections. See  for a complete list of special systemd units.

## Wired
Install the  package and start/enable the  systemd unit. DHCP profiles will be started/stopped when the network cable is plugged in/unplugged.
* The  will prefer profiles that use DHCP.
* To automatically start a  static IP profile the option  needs to be set in it.
* To prioritize a profile with a static IP over DHCP profiles, you can set , which is higher than the default priority given to DHCP profiles of .

## Wireless
Start/enable  systemd unit. netctl profiles will be started/stopped automatically as you move from the range of one network into the range of another network (roaming).

* Profiles must use  or  to work with netctl-auto rather than .
* If you want some wireless profile not to be started automatically by , you have to explicitly add  to that profile.
* You can use  in the WPAConfigSection (see ) to set priority of a profile when multiple wireless access points are available. Larger numbers indicate a higher priority.

Note that interface is not literal, but to be substituted by the name of your device's interface, e.g. . See  for details.

It is possible to manually control an interface otherwise managed by netctl-auto without having to stop . This is done using the netctl-auto command. For a complete list of available actions see .

## Tips and tricks
## Example profiles
## Wired
For a DHCP connection, only the  has to be configured after copying the  example profile to .

For example:

For a static IP configuration copy the  example profile to  and modify , ,  and ) as needed.

For example:

Take care to include the subnet notation of . It equates to a netmask of ) and without it the profile will fail to start. See also CIDR notation. To alias more than one IP address per a NIC set . To alias more than one DNS server address set Eg. .

## Wireless (WPA-PSK)
The following applies for the standard wireless connections using a pre-shared key (WPA-PSK).

## Obfuscate wireless passphrase
You can also follow the following step to obfuscate the wireless passphrase (wifi-menu does it automatically when using the  flag):

Users not wishing to have the passphrase to their wireless network stored in plain text have the option of storing the corresponding 256-bit pre-shared key instead, which is calculated from the passphrase and the SSID using standard algorithms.

Calculate your 256-bit PSK using wpa_passphrase:
{{hc|$ wpa_passphrase your_essid|2=
  network={
  ssid="your_essid"
  #psk="passphrase"
  psk=64cf3ced850ecef39197bb7b7b301fc39437a6aa6c6a599d0534b16af578e04a
}
}}

The pre-shared key (psk) now needs to replace the plain text passphrase of the  variable in the profile.

## Using an experimental GUI
If you want a graphical user interface to manage netctl and your connections and you are not afraid of highly experimental unofficial packages, there are some options available.  provides a Qt-based graphical interface, DBus daemon and KDE widget.  uses  as its graphical interface.

There is also an application that displays desktop notifications on profile changes and shows a tray icon: .

## Bonding
From kernel documentation:

:The Linux bonding driver provides a method for aggregating multiple network interfaces into a single logical "bonded" interface. The behavior of the bonded interfaces depends on the mode. Generally speaking, modes provide either hot standby or load balancing services. Additionally, link integrity monitoring may be performed.

## Load balancing
Copy  to  and edit it, for example:

Now you can disable your old configuration and set bond0 to be started automatically. Switch to the new profile, for example:

 # netctl switch-to bond0

Setting the MODE in the netctl configuration is not always successful and it may be necessary to pass options directly to the bonding module on load as noted here.  This may be needed to use LACP / mode 4.

## Wired to wireless failover
This example describes how to use bonding to fallback to wireless when the wired Ethernet goes down. This is most useful when both the wired and wireless interface will be connected to the same network. Your wireless router/access point must be configured in bridge mode.

You will need an additional package: .

First, load the module at boot:

Then, configure the options of the  driver to use  and configure the  parameter to the device you want to be the active one (normally the wired interface). Also, be sure to use the same device name as returned when running :

The  option is needed, for the link failure detection. The  option avoids the  error. More information can be obtained on the kernel documentation.

Next, configure a netctl profile to enslave the two hardware interfaces. Use the name of all the devices you want to enslave. If you have more than two wired or wireless interfaces, you can enslave all of them on a bond interface. But, for most cases you will have only two devices, a wired and a wireless one:

Disable any other profiles (specially a wired or wireless) you had enabled before and then enable the failover profile on startup:

 # netctl enable failover

Now you need to configure wpa_supplicant to connect to any known network you wish. You should create a file for each interface and enable it on systemd. Create the following file with this content:

And append to the end of this file any network you want to connect to:

 network={
     ssid="SSID"
     psk=PSK
 }

To generate the obfuscated PSK you can run wpa_passphrase as on the wpa_supplicant#Connecting with wpa_passphrase page.

Now, enable the  template service on the network interface, for example .

You can try now to reboot your machine and see if your configuration worked.

Now, you can test your failover setup, by initiating a big download. Unplug your wired interface. Your download should keep going over the wireless interface. Then, plug your wired interface again and it should keep working. You can debug by checking journalctl for the  and  units.

## Using any interface
In some cases it may be desirable to allow a profile to use any interface on the system. A common example use case is using a common disk image across many machines with differing hardware (this is especially useful if they are headless). If you use the kernel's naming scheme, and your machine has only one ethernet interface, you can probably guess that eth0 is the right interface. If you use udev's Predictable Network Interface Names, however, names will be assigned based on the specific hardware itself (e.g. enp1s0), rather than simply the order that the hardware was detected (e.g. eth0, eth1). This means that a netctl profile may work on one machine and not another, because they each have different interface names.

A quick and dirty solution is to make use of the  directory. Choose a name for your interface alias ( in this example), and write the following to a file with that name (making sure it is executable).

Then create a profile that uses the interface. Pay special attention to the  directive. The rest are only provided as examples.

When the  profile is started, any machine using the two files above will automatically bring up and configure the first ethernet interface found on the system, regardless of what name udev assigned to it. Note that this is not the most robust way to go about configuring interfaces. If you use multiple interfaces, netctl may try to assign the same interface to them, and will likely cause a disruption in connectivity. If you do not mind a more complicated solution,  is likely to be more reliable.

## Using hooks
netctl supports hooks in  and per interface hooks in . You can set any option in a hook/interface that you can
in a profile. Most importantly this includes  and .

When a profile is read, netctl sources all executable scripts in , then it reads the profile file for the connection and finally it sources an executable script with the name of the interface used in the profile from the  directory. Therefore, declarations in an interface script override declarations in the profile, which override declarations in hooks.

The variables  and  are available in hooks/interfaces only when using

## Examples
## Execute commands on established connection
## Set default DHCP client
To set or change the DHCP client used for all profiles:

Do not forget to make the file executable.

Alternatively, it may also be specified for a specific network interface by creating an executable file  with the following line:

 DHCPClient='dhclient'

## Minimal WPAConfigSection
As stated in , the  variable is an array of configuration lines passed to wpa_supplicant. So, a minimal WPAConfigSection would contain:

 Description='A wireless connection using a custom network block configuration'
 Interface=wlan0
 Connection=wireless
 Security=wpa-configsection
 IP=dhcp
 WPAConfigSection=(
     'ssid="University"'
     'psk="very secret passphrase"'
 )

## /etc/resolv.conf
If you use  options in your profile, netctl calls resolvconf to overwrite resolv.conf.

## Troubleshooting
## Job for netctl@wlan(...).service failed
Some people have an issue when they connect to a network with netctl, for example:

When looking at the journal from running  as root, either of the following are shown:

1. If your device ( in this case) is up:
 networkThe interface of network profile 'wlan0-ssid' is already up

Setting the interface down should resolve the problem:
 # ip link set wlan0 down

Then retry:
 # netctl start wlan0-ssid

2. If the error continues, try again after adding the  option:

Save it and try to connect with the profile:
 # netctl start wlan0-ssid

## dhcpcd: ipv4_addroute: File exists
On some systems dhcpcd in combination with netctl causes timeout issues on resume, particularly when having switched networks in the meantime. netctl will report that you are successfully connected but you still receive timeout issues. In this case, the old default route still exists and is not being renewed. A workaround to avoid this misbehaviour is to switch to dhclient as the default dhcp client. More information on the issue can be found [https://bbs.archlinux.org/viewtopic.php?pid=1399842#p1399842 here.

## DHCP timeout issues
If you are having timeout issues when requesting leases via DHCP you can set the timeout value higher than netctl's 30 seconds by default. Create a file in  or , add  to it for a timeout of 40 seconds and make the file executable.

## dhcpcd debugging
If dhcpcd fails to obtain an address, add the  option to  and then run  as root to view the debugging messages which may indicate, for example, that the IP address offered by the server is rejected by the client after detecting that the IP address is already in use.

## Connection timeout issues
If you are having timeout issues that are unrelated to DHCP (on a static ethernet connection for example), and are experiencing errors similar to the following when starting your profile:

Then you should increase carrier and up timeouts by adding  and  to your profile file:

Do not forget to reenable your profile:

 # netctl reenable profile

## Problems with netctl-auto on resume
Sometimes netctl-auto fails to reconnect when the system resumes from suspend, hibernate or hybrid-sleep. An easy solution is to restart the service for netctl-auto.
This can be automated with an additional service like the following:

To enable this service for your wireless card, for example, enable  as root. Change  to the required network interface.

If the device is not yet running on resume when the unit is started, this will fail. It can be fixed by adding the following dependency in the After line:

## netctl-auto does not automatically unblock a wireless card to use an interface
Many laptops have a hardware button (or switch) to turn off wireless card, however, the card can also be blocked by the kernel. This can be handled by rfkill.

If you want netctl-auto to automatically unblock your wireless card to connect to a particular network, set  option for the wireless connection of your choice, as specified in the .

## RTNETLINK answers: File exists (with multiple NICs)
This is a very misleading response, it really means that you have assigned a default gateway in an earlier netctl control file. When netctl starts up the n-th NIC and goes to set its local route, it fails because there is already a default route from n-1.

Remove it and everything works, except you no longer have a default route and so cannot access things such as the internet.  does not work as it gets executed for each network card.

A possible solution is creating a new service.  Replace "FIRST_INTERFACE" and "SECOND_INTERFACE" with your interface names, and replace "192.168.xxx.yyy" with your default gateway.

## Problems with Eduroam and other MSCHAPv2 connections
See wpa_supplicant#Problems with Eduroam.

## Journal warnings for profiles using .include directives
Profiles still using systemd's old  directives will produce journal warnings, for example:
 systemd/etc/systemd/system/netctl@.service:1: .include directives are deprecated, and support for them will be removed in a future version of systemd. Please use drop-in files instead.

See  for details.

Executing
 netctl reenable profile
will update the profile to the new drop-in unit file format.

## Hooks do not work
If you have multiple hooks in , variables like  and  will be executed only from one file. To fix this, define the variables like this:

This will append your commands to be executed with already defined ones.

## Network mounts time out on shutdown
If you are using network mounts in combination with  or , it may be necessary to unmount them before the corresponding services are stopped. One way to achieve this is to create an drop-in file for  or  with the following content:

This will make sure the network mounts are disconnected before the automatic network service is stopped.
