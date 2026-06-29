# PPTP server

Point-to-Point Tunneling Protocol (PPTP) is a method for implementing virtual private networks. PPTP uses a control channel over TCP and a GRE tunnel operating to encapsulate PPP packets.

This entry will show you on how to create a PPTP server in Arch.

## Installation
Install the  package.

## Configuration
A typical configuration may look like:

Now create the pppd options file, in our example this is :

Now create credentials file for authenticating users:

Now you can be authenticated with user2 as username and 123 for password.

Create a sysctl configuration file  and enable kernel packet forwarding that allow connecting clients to have access to your subnet (see also Internet Share#Enable packet forwarding):

Now apply changes to let the sysctl configuration take effect:

 # sysctl --system

## iptables firewall configuration
Configure your iptables settings to enable access for PPTP Clients

Now save the new iptables rules with:

 # iptables-save > /etc/iptables/iptables.rules

To load /etc/iptables/iptables.rules automatically after boot, enable the  unit.

Read Iptables for more information.

## UFW firewall configuration
Configure your ufw settings to enable access for PPTP Clients.

You must change default forward policy in

Now change , add following code after header and before *filter line

Allow GRE packets (protocol 47) in , find the line with:  and add rule:

Open pptp port 1723

Restart ufw for good measure

## Start the server
Now you can start and enable your PPTP Server using .

## Troubleshooting
As with any service, see Systemd#Troubleshooting to investigate errors.

## Error 619 on the client side
Search for the  option in  and comment it out. When this is enabled, wtmp will be used to record client connections and disconnections.

 #logwtmp

## pptpdLong config file line ignored
Add a blank line at the end of . [https://sourceforge.net/p/poptop/bugs/35/

## ppp0: ppp: compressor dropped pkt
If you have this error while a client is connected to the server, add the following script to :

 #!/bin/sh
 CURRENT_MTU="`ip link show $1 | grep -Po '(?<=mtu )(FIXED_MTU="`expr $CURRENT_MTU + 4`"
 ip link set $1 mtu $FIXED_MTU

Make the script executable.

See also: [https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=330973
