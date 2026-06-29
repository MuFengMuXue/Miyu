# Avahi

From Wikipedia:Avahi (software):
:Avahi is a free Zero-configuration networking (zeroconf) implementation, including a system for multicast DNS/DNS-SD service discovery. It allows programs to publish and discover services and hosts running on a local network with no specific configuration. For example you can plug into a network and instantly find printers to print to, files to look at and people to talk to. It is licensed under the GNU Lesser General Public License (LGPL).

## Installation
Install the  package and enable the  or  if you want to use the socket activation.

## Using Avahi
## Hostname resolution
Avahi provides local hostname resolution using a "hostname.local" naming scheme. To enable it, install the  package and start/enable .

Then, edit the file  and change the  line to include  before  and :

 hosts: mymachines '''mdns_minimal resolve [!UNAVAIL=return files myhostname dns

## Configuring mDNS for custom TLD
The  module handles queries for the  TLD only. Note the , which specifies that if  cannot find , it will not continue to search for it in , , etc.

In case you want Avahi to support other TLDs, you should:

* replace  with the full  module. There also are IPv4-only and IPv6-only modules
* customize  with the  of your choice
* whitelist Avahi custom TLDs in

## Tools
Avahi includes several utilities which help you discover the services running on a network. For example, run this to discover services in your network:

 $ avahi-browse --all --ignore-local --resolve --terminate

If this command yields nothing, it is likely due to a firewall blocking mDNS traffic.

If you just want to do an mDNS query to resolve a .local hostname to an IP address (similar to dig or nslookup), use:

 $ avahi-resolve-host-name some-host-name.local

Note that the  command can do both DNS and mDNS lookups.

The Avahi Zeroconf Browser  shows the various services on your network. Note that it needs Avahi's optional dependencies ,  and . You can also browse SSH and VNC Servers using  and  respectively.

## Firewall
Be sure to open UDP port  if you are using a firewall.

## Link-Local (Bonjour/Zeroconf) chat
Avahi can be used for Bonjour protocol support under Linux. Check Wikipedia:Comparison of instant messaging clients or List of applications/Internet#Instant messaging clients for a list of clients supporting the Bonjour protocol.

## Obtaining IPv4LL IP address
The dhcpcd client can attempt to obtain an IPv4LL address if it failed to get one via DHCP. By default this option is disabled. To enable it, comment noipv4ll string:

Alternatively, run :

 # avahi-autoipd -D

## Adding services
Avahi advertises the services whose  files are found in . Files in this directory must be readable by the  user/group.

If you want to advertise a service for which there is no  file, it is very easy to create your own.
As an example, let us say you wanted to advertise a quote of the day (QOTD) service operating per RFC:865 on TCP port  which you are running on your machine

The first thing to do is to determine the .  indicates that the type should be "the DNS-SD service type for this service. e.g. '_http._tcp'". Since the DNS-SD register was merged into the IANA register in 2010, we look for the service name on the IANA register or in  file. The service name shown there is . Since we are running QOTD on tcp, we now know the service is  and the port (per IANA and RFC 865) is .

Our service file is thus:

For more complicated scenarios, such as advertising services running on a different server, DNS sub-types and so on, consult .

Keep in mind that Avahi does not support arbitrary strings in the  field, you can only set values known in service database of Avahi. If you want to register something custom you will likely have to edit the database definition, build an updated version and distribute it to your hosts.

## SSH
Avahi comes with an example service file to advertise an SSH server. To enable it:

 # cp /usr/share/doc/avahi/ssh.service /etc/avahi/services/

## File sharing
## NFS
If you have an NFS share set up, you can use Avahi to be able to automount them in Zeroconf-enabled browsers (such as Konqueror on KDE and Finder on macOS) or file managers such as GNOME/Files.

Create a  file in  with the following contents:

The port is correct if you have insecure as an option in your ; otherwise, it needs to be changed (note that insecure is needed for macOS clients). The path is the path to your export, or a subdirectory of it. For some reason the automount functionality has been removed from Leopard, however a script is available. This was based upon this post.

## Samba
With the Avahi daemon running on both the server and client, the file manager on the client should automatically find the server.

## Vsftpd
You can also auto-discover regular FTP servers, such as vsftpd. Install the  package and change the settings of vsftpd according to your own personal preferences (see this thread on ubuntuforums.org or ).

Create a  file in  with the following contents:

The FTP server should now be advertised by Avahi. You should now be able to find the FTP server from a file manager on another computer in your network. You might need to enable #Hostname resolution on the client.

## Troubleshooting
## Hostname changes with appending incrementing numbers
This can happen if you have not disabled systemd-resolved's multicast DNS resolver. This is also a known bug that is caused by a hostname race condition. One possible workaround is disabling IPv6 to attempt to prevent the race condition. If multiple interfaces are present use allow-interfaces to limit Avahi to a single interface. Another possible workaround is to disable the cache to prevent Avahi from checking for host name conflicts altogether, but this prevents Avahi from performing lookups.

## systemd-resolved prevents nss-mdns from working
nss-mdns only works if the DNS server listed in  returns  to SOA queries for the "local" domain.Check if your configured DNS server answers the SOA query for the "local" domain with  first. For example:

 $ host -t SOA local

If the DNS server responds with , you do not need to follow the steps below.
Avahi should be able to find resources in the network normally, even if using systemd-resolved.

In older versions of systemd-resolved the global setting for  in  lead to Avahi-incompatible response codes for the "local" domain. This resulted in Avahi not finding resources (printers) correctly. See [https://github.com/systemd/systemd/issues/21659 systemd issue 21659 for reference.

However, if the DNS query above fails to return  for the "local" domain, you can use the full  NSS module instead of  and create  to allow only the "local" domain. For example:

## ECONNREFUSED (Connection refused) on avahi socket
If your Avahi instance starts and operates correctly, but nss does not seem to forward requests to mdns, this may be caused by stuck socket . This can be verified e.g. with strace. In this case you may have to restart both  and  to make it work correctly.
