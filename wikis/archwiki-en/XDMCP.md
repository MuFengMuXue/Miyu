# XDMCP

From Wikipedia:
: The X Display Manager Control Protocol (XDMCP) uses UDP port 177. An X server requests that a display manager start a session by sending a Query packet. If the display manager allows access for that X server, it responds by sending a Willing packet back to the X server.

This allows for opening X sessions remotely.

## Setup graphical logins
## XDM
Comment the last line of the configuration file with a :

Then allow any host to get a login window in by un-commenting the following:

In case you have multiple network interfaces also add a line like this:

 LISTEN 192.168.0.10

Where  is your server IP address.

Then restart .

## GDM
Enable XDMCP in the configuration file:

Then restart .

## LightDM
Enable the XDMCP Server in the configuration file:

On a headless system, disable the automatic start of one seat so that LightDM can run in the background:

 start-default-seat=false

Then restart .

## Accessing X from a remote machine on your LAN
You can access your login manager on the network computer (using  in the  following command). TCP and UDP streams are opened. So it is not possible to access the login manager via an SSH connection.

 $ Xnest -query 192.168.0.10 -geometry 1280x1024 :1

Or, with Xephyr, if you experience refreshing problems with Xnest:

 $ Xephyr -query 192.168.0.10 -screen 1280x1024 -br -reset -terminate :1

Or, if you are on runlevel 3

 $ X -query server address

Xserver should recognize your monitor and set appropriate resolution.

After allowing XDMCP access as described above, edit  and comment out:
 #:0 local /usr/bin/X :0
Then launch XDM as root, e.g.

## Thin client setup
First of all one should setup dhcp and tftp server. Dnsmasq has both of them.
For network boot image check [https://www.thinstation.org/ thinstation project.
If your network card does not support PXE, you can try Etherboot

## GUI-based Clients
* Remmina
* Xming for Windows

## Troubleshooting
## Session declined: Maximum Number of Sessions Reached
Edit  and increase . It is worth noting that there may be a limit regarding how many XDMCP connections are allowed at once, so it's worth increasing  as wellif multiple clients are connecting from the same IP.

 [xdmcp
 Enable=true
 MaxSessions=X
 DisplaysPerHost=X
