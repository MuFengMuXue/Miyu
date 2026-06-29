# Wireless bonding

## Network Interface Bonding with Removable Device Support
From Linux Ethernet Bonding Driver HOWTO:

:The Linux bonding driver provides a method for aggregating multiple network interfaces into a single logical "bonded" interface.

The Linux kernel bonding driver can be used to provide parallel network connections to maximize throughput, or to allow redundant network connections to maximize network availability.  Here is an example of using the kernel bonding driver to maximize availability, by allowing network connections to "failover" between a primary network device and any number of secondary devices, or alternatively, by selecting the highest speed connection available.  This approach provides Automatic Wired and Wireless Network Configuration with Removable Device Support, using only the kernel bonding module in "active-backup" mode, the sysfs, the  commands, and  "template" Unit files, without using systemd-networkd.

This example will run  continuously on any interface, as needed, and DHCP client on a virtual "bond0" interface.  This is useful, for instance, with a portable computer when you want to use the wired interface for speed and/or security when available, and the wireless interface when the wired interface is not available.  The basic idea is to have two "always active" wired and wireless interfaces, then "bond" or "enslave" them to a virtual interface "master", and then let the kernel bonding module handle switching between the interfaces.  Of course, this scheme can be applied to any other type of network interface, and extended to more than two physical or virtual network interfaces.

Note that host networking is managed directly with systemd, and that no other "connection manager" is used here, providing a more basic approach.  But then also, wpa_supplicant itself can still be managed directly using  from , to scan for, select, and connect to new wireless access points/base stations.

In this example, there are six systemd service unit files used, along with five associated configuration files, for the kernel bonding module, wpa_supplicant, , and for static network configuration and specifying the primary slave network interface name.  The six unit files are essentially generic service unit files which do not contain configuration data, and no modification is needed.  The various service units may be stopped, started, and restarted individually without ordering errors or failed states.  Any network interface device, such as typically a wired or wireless PC Card, may be removed and replaced, and reconfiguration will be automatic.

## DHCP configuration
If you also run a DHCPv6 client, make sure that the DHCP Client Identifier and the DHCPv6 Client Identifier are the same DUID.  The DHCP Server,  for instance, can be configured to give fixed IP addresses based upon multiple MAC addresses, or provided hostname, or provided Client Identifier.

There is a particular issue to address.  When starting kernel bonding, where the only working interface is the non-primary slave - for instance, starting with only a wireless interface available when the wired interface is the primary - then dhclient will quickly start and adopt the MAC address of the initial primary slave, and use that MAC address when attempting to communicate with the DHCP server.  When the wireless interface, some short time later, is authenticated, associated, and authorized with the access point/base station, establishing a connection to the network, the bonding driver will make the wireless interface the new active interface, and change the active MAC address on the bond0 interface, to match the wireless MAC address.  Because dhclient will continue to use the MAC address from the wired interface, and that MAC address is no longer accepted by the bond0 interface, all DHCP communication will fail.  If there is no saved lease file in /var/lib/dhclient/dhclient.leases, then no IPv4 address will be configured, and no IPv4 traffic will be possible.  It can also be seen that when dhclient starts quickly, it can read the primary slave's firmware MAC address, rather than any MAC address assigned to the device interface.  If the firmware MAC address is "null", then dhclient assigns a random MAC address.  BOOTP/DHCP packets using these firmware or random MAC addresses may "succeed" in gaining a reply on the primary slave device and fail on the non-primary slave device.  That can be confusing and annoying.

These are only issues with dhclient and IPv4.  Fortunately, on a dhclient DHCP request, after the lease expires, dhclient "does the right thing".  dhclient will function properly no matter on which slave interface it was started.

This problem cannot be solved by configuring the bonding driver with the default .  Almost all network interface devices will not pass traffic with a MAC address which is not their own.  An example of this kind of warning can be seen here.  Strange network behavior will be the result, where broadcast packets will pass, but ping/icmp packets will only pass in some circumstances and not others.

Ideally, dhclient would re-determine the bonding interface MAC address each time it initially retried contacting the DHCP server.  Without that, a different approach is to simply delay the start of dhclient until after the kernel bonding driver has configured an active slave.  If the active slave is to be the wireless interface, then wpa_supplicant will first have authenticated, associated, and authorized with the access point/base station, and dhclient will adopt the correct MAC address.  If the active slave is the primary slave, again dhclient will adopt the correct MAC address.  This delay is imposed with the simple  line in the dhclient service unit file, a conservatively long delay between the time systemd starts dhclient and the supplicant and the bonding driver selects the active interface.  This selection time is longest during system boot, when many processes are starting.  On faster hardware, a shorter delay, perhaps , may still be effective.

## Static Network configuration
Here, for instance, a static private IPv4 address will be assigned to the bonding interface as a "fail-safe", were the DHCP server to fail or be otherwise inaccessible.  The primary slave interface is also specified in this file.

{{hc|/etc/systemd/system/static@.service|2=
Description= Static Network Configuration on %I
Documentation= man:ip-address(8) man:ip-route(8) man:systemd.service(5)

Wants= network.target
Before= network.target

BindsTo= sys-subsystem-net-devices-%i.device

[Service
EnvironmentFile= /etc/conf.d/network.conf

Type= oneshot
RemainAfterExit= yes

# Apparently, "ip" is not synchronous/atomic, so allow some time.
ExecStart=-/usr/bin/ip link set %I up
ExecStart=-/usr/bin/sh -c '[ "$%IADDRS" ] && \
        for a in $%IADDRS;do /usr/bin/ip address add local $$a dev %I;done'
ExecStart= /usr/bin/sleep 1
ExecStart=-/usr/bin/sh -c '[ "$%IROUTES" ] && \
        for r in ${%IROUTES};do /usr/bin/ip route replace $$r dev %I;done'

ExecStop=-/usr/bin/sh -c '[ "$%IROUTES" ] && \
        for r in ${%IROUTES};do /usr/bin/ip route del $$r dev %I;done'
ExecStop= /usr/bin/sleep 1
ExecStop=-/usr/bin/sh -c '[ "$%IADDRS" ] && \
        for a in $%IADDRS;do /usr/bin/ip address del local $$a dev %I;done'

Install
WantedBy= sys-subsystem-net-devices-%i.device
}}

Of course, static network configuration may be used as an alternative to, or in addition to, dynamic network configuration, or not at all.

## wpa_supplicant configuration
{{hc|/etc/wpa_supplicant/wpa_supplicant.conf|2=
ctrl_interface=/var/run/wpa_supplicant
ctrl_interface_group=wheel
update_config=1
eapol_version=2
ap_scan=1
# fast_reauth=1
country=US

network={
        ssid="MyHome"
        priority=2
        proto=RSN
        group=CCMP
        pairwise=CCMP
        key_mgmt=WPA-PSK
        #psk="SuperSecret"
        psk=404fe69d94ef522ba8e7a0c456a67a583c8f39ba0b29a3ac22ebe9494cf9992b
}
}}

Be careful with the actual protocol configuration in the wpa_supplicant configuration file.  Using protocols incompatible with the base station can result in unstable and otherwise difficult to troubleshoot wireless connections.  Pre-compute the PSK with .   can overwrite this file.  Note that  can be run on any wired or wireless interface, as needed.

The supplicants and the DHCP client are ordered relative to the network-pre.target on shutdown.  The supplicants must not be stopped before the DHCP client releases the address lease.

Remember that the  commands do not work with the wired interface drivers or with older wireless drivers which rely upon the Wireless Extensions user-space driver, and will be ignored in those cases.

## Slave configuration
There is a "trick" which will be used here, in the naming of the slave service template unit files.  Two environment variables are to be passed to the slave unit files, the name of the network interface, and the name of the bonding interface.  Notice that there are two particular environment variables passed into a systemd unit file, %p/%P and %i/%I, these being the strings before and after the "@" character in the name of a template unit file.  Here, the bonding interface name is specified in that portion of the unit file name after the "@" character, and the network interface name is passed in that portion before the "@" character.  This allows two network interface names to be specified arbitrarily on the command line, without modifying the unit files themselves.

This "slave@.service" unit file will be hard linked to files having the same name as the network interfaces, such as "wlp2s0@.service" and "enp3s0@.service".  Note that symbolic links cannot be used here, since systemd would then set %p/%P to the target file name "slave", instead of the desired network interface name.

## Master configuration
Of course, "Environment=" could be used here instead of the Environment file, if static network configuration is not used, and then the Environment file could be avoided.  Settings from Environment files override settings made with "Environment=".

This master service unit file supports creation of a bonding master or a bridging master network interface.  The type of master interface created is determined by the name of the interface.  A bridging master is created when the interface name includes the character string "br", and a bonding master is created otherwise.

The RequiredBy dependencies are only here to activate the stop ordering of static or dynamic network configuration units during master stop and restart.  The network configurations must be taken-down and that process completed before the slave interfaces are freed and the master interface is deleted.

Enable/Install a bonding master unit or bridging master unit only when the master interface is also an IP interface for the host, which is to say, when there is a static or dynamic network configuration unit Enabled/Installed on that master interface.  If the bonding master or bridging master is not also an IP interface, then the master service unit should not be Enabled/Installed, since it will be started manually, or will be started by the slave service units, on boot, or when a network device is plugged.

## Enabling/Installing the Service Units
With those preliminaries, the interface names must be specified on the command line.

Whenever a unit file is edited, afterward run a daemon-reload.

Next, observe the available network interface names, after inserting any removable devices:

 # ip address

For each interface which will be enslaved, hard link "slave@.service" to "interface_name@.service":

 # ln /etc/systemd/system/slave@.service /etc/systemd/system/enp3s0@.service
 # ln /etc/systemd/system/slave@.service /etc/systemd/system/wlp2s0@.service

Now, determine which network interface devices will need a supplicant to access the network.  Typically this will just be the wireless interface. Start/enable the  unit for each interface, as needed (e.g. )

Then, enable the slave and master units, using any desired interface name. (Here, "bond0" is used:   )

Explicitly enable only the desired network configuration, specifying the interface name(here again, bond0:  )

And finally, activate the bonding interface, the DHCP client, and any static network configuration, by starting

The master and supplicant units will be started automatically when any configured slave device appears, and in particular, when the system boots.  Were any of the DHCP, or slave units to be started independently, the master unit would also be started, but normally these units will have already been started at boot.

## Testing the result
Check the results:

 # journalctl -afn100
 $ ip a
 $ ps wax

Using the wired ethernet interface,

Using the wireless interface,

To tear-down the bonding interface and shutdown the master, slave, and DHCP units, simply stop .

The supplicant units can be stopped independently with .

This approach to bonded wireless networking leaves wpa_supplicant running continuously on whatever interfaces it is started.  By running , it can be seen that wpa_supplicant, and the DHCP client daemon, seem to behave well, and do not use any noticeable CPU time.

Still, a hardware switch or rfkill can be used to actually disable the radio when desired.

Notice that the various service units are quite independent except for the ordering dependencies that have been explicitly configured.  So, for instance, a dhclient configured IPv4 address may be removed without disturbing any other network configuration or functionality by stoping .

Similarly, an address may be released and a new address acquired with a restart of .

And a static address or default gateway may be changed by stopping the static service unit (), editing the  file, and then starting the  unit again

Also, wpa_supplicant could be temporarily disabled when only the wired interface is being used, and then started again later.

This bonding interface will function properly even with only one interface available, for instance, when only a wired interface is being used.  And then, simply inserting a configured wireless network card, this new wireless interface will be automatically added to the bonded interface pool, and wpa_supplicant started.  Removing this wireless card again will remove the slave interface and stop wpa_supplicant.

Check that the Ethernet cable is actually plugged-in when wired networking is preferred.  And use, for instance,  or  to verify a connection to the correct Service Set Identifier/SSID when wireless networking is used.
