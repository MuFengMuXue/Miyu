# Firewalld

firewalld is a firewall daemon developed by Red Hat. It uses nftables by default. From project home page:

:Firewalld provides a dynamically managed firewall with support for network/firewall zones that define the trust level of network connections or interfaces. It has support for IPv4, IPv6 firewall settings, ethernet bridges and IP sets. There is a separation of runtime and permanent configuration options. It also provides an interface for services or applications to add firewall rules directly.

## Installation
Install the  package. You have to install related packages manually if you wish so, as the  package is split into separate packages:

*  - graphical user interface,
*  - system tray applet,
*  - test suite,
*  - Python bindings.

## Usage
Enable and start .

You can control the firewall rules with the  console utility.

 utility can be used to configure when firewalld is not running. It features similar syntax to .

A graphical interface is available from the  package.

With the nftables backend, firewalld does not assume complete control over the hosts firewalling. Since nftables allows multiple "namespaces" via tables, firewalld will scope all of its rules, sets, and chains to the  table. Firewalld does not do a complete flush of firewall rules, it will only flush rules in the  table.

nftables allows multiple chains to hook into netfilter at the same point. Packets that are accepted by a chain are still subject to the rules of other chains hooked into the hook type and in the drop case processing always stops immediately and no other hooks will process the packet. To ensure predictability of the execution order of chains, firewalld gives its rules slightly lower precedence than default nftables hook priority values. Consequently, firewall rules created outside of firewalld (e.g. by libvirt, Docker, Podman, systemd-nspawn, etc.) will be processed before firewalld rules and packets accepted by them will still be subject to firewalld rules.

## Configuration
Configuration at run time can be changed using .

## Zones
Zone is a collection of rules that can be applied to a specific interface.

To have an overview of the current zones and interfaces they are applied to:

 # firewall-cmd --get-active-zones

Some commands (such as adding/removing ports/services) require a zone to specified.

Zone can be specified by name by passing  parameter.

If no zone is specified default zone is assumed.

## Zone information
You can list all the zones with entirety their configuration:

 # firewall-cmd --list-all-zones

or just a specific zone

 # firewall-cmd --info-zone=zone_name

## Changing zone of an interface
 # firewall-cmd --zone=zone --change-interface=interface_name

There  is a new zone that you want to assign interface to.

## Using NetworkManager to manage zones
NetworkManager can assign different connection profiles to different zones. This allows for example, adding a home Wi-Fi connection to the "home" zone, a work Wi-Fi connection to the "work" zone, and all other Wi-Fi connections to the default "public" zone.

List connection profiles:

 $ nmcli connection show

Assign the "myssid" profile to the "home" zone:

 $ nmcli connection modify myssid connection.zone home

## Default zones
When a new interface is connected the default zone will be applied. You can query the name of the default zone using:

 # firewall-cmd --get-default-zone

The default zone can be changed using following command.

 # firewall-cmd --set-default-zone=zone

## Services
Services are pre-made rules corresponding to a specific daemon. For example, the  service corresponds to SSH and opens ports 22 when assigned to a zone.

To get a list of available services, enter the following command:

 # firewall-cmd --get-services

You can query information about a particular service:

 # firewall-cmd --info-service service_name

## Adding or removing services from a zone
To add a service to a zone:

 # firewall-cmd --zone=zone_name --add-service service_name

Removing a service:

 # firewall-cmd --zone=zone_name --remove-service service_name

## Ports
Ports can be directly opened on a specific zone.

 # firewall-cmd --zone=zone_name --add-port port_num/protocol

There  is either  or .

To close the port use  option with same port number and protocol.

## NAT masquerade
Masquerading is a form of source NAT where the source address is unknown at the time the firewall rule created in the kernel, and instead the source address of a packet is dynamically modified to the primary IP address of the outgoing interface # firewall-cmd --permanent --zone=public --add-masquerade

Since version 1.0.0, to make NAT masquerade work between different firewall zones, you have to create a new policy object which is used to filter traffic between them:

 # firewall-cmd --new-policy internal-to-public --permanent
 # firewall-cmd --permanent --policy internal-to-public --add-ingress-zone internal
 # firewall-cmd --permanent --policy internal-to-public --add-egress-zone public
 # firewall-cmd --permanent --policy internal-to-public --set-target ACCEPT

## Port forwarding
If you have firewalld configured on a router, and you have enabled NAT masquerading as above, it is simple to set up port forwarding through firewalld:

 # firewall-cmd --zone=public --add-forward-port=port=12345:proto=tcp:toport=22:toaddr=10.20.30.40

This will forward port  on the firewall's public interface to port  (standard SSH) on the internal system at IP address . To remove this forwarded port:

 # firewall-cmd --zone=public --remove-forward-port=port=12345:proto=tcp:toport=22:toaddr=10.20.30.40

Unfortunately you have to type the entire forward declaration in order to remove it, specifying only the port and the protocol is not enough.

## Rich rules
With rich rules/rich language syntax more complex firewall rules can be created in an easy to understand way.

To add a rich rule:
 # firewall-cmd [--zone=zone_name --add-rich-rule=&apos;rich_rule&apos;
where  is a rich language rule.

For example, to allow all connection from network  to the NFS service:
 # firewall-cmd --add-rich-rule='rule family="ipv4" source address="192.168.1.0/24" service name="nfs" accept'
To allow connection from  to port :
 # firewall-cmd --add-rich-rule='rule family="ipv4" source address="192.168.2.3" port port="1234" protocol="tcp" accept'
For more rich language syntax, see .

To remove a rich rule:
 # firewall-cmd  [--zone=zone_name --remove-rich-rule=&apos;rich_rule&apos;

## Tips and tricks
## Port or service timeout
Service or port can be added for a limited amount of time using  option passed during addition command. Value is either number of seconds, minutes if postfixed with  or hours .
For example, adding SSH service for 3 hours:
 # firewall-cmd --add-service ssh --timeout=3h

## Converting runtime configuration to permanent
You can make the runtime (current temporary) configuration permanent (meaning it persists through restarts)

 # firewall-cmd --runtime-to-permanent

## Check services details
The configuration files for the default supported services are located at  and user-created service files would be in .

## Troubleshooting
## IPv6 reverse packet filter dropping legitimate packages
 implements an IPv6 reverse packet filter that by default is set to strict. Unfortunately if there are multiple interfaces connected to the same network (e.g. a laptop with both wired and wireless connected) only one of those interfaces, chosen at random, are returned by the reverse path lookup. Incoming packets on other interfaces on the same network are dropped. Because IPv4 and one of the IPv6-enabled interfaces still work this tends to show up as intermittent connectivity issues like hanging connection attempts or a preference for the worse interface. This issue can be verified by running  on each interface and seeing that only one of them gets any replies.

The workaround is to change the reverse path filter setting to loose. This setting only checks that a reverse path exists at all, and matches the default IPv4 reverse path filter setting (not implemented by firewalld, but implemented in the kernel and configured by systemd).
