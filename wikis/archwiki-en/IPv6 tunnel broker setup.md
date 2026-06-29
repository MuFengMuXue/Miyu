# IPv6 tunnel broker setup

This article introduces a method for obtaining an IPv6 address using 6in4, also known as SIT.

The following sections will use the tunnel service provided by Hurricane Electric as a setup example. Hurricane Electric offers a free tunnel broker service to add IPv6 connectivity to an IPv4-only host. Read the "Tunnel Broker" section of their FAQ for a list of prerequisites.

## Registering for a tunnel
Registering for a tunnel on its website.

## Setting up Hurricane Electric tunnel
There is some ways you can achieve this, such as using the ip command to test the tunnel manually, a custom systemd unit, or using a network manager like #systemd-networkd.

## Custom systemd unit
Create the following systemd unit, replacing bold text with the IP addresses you got from Hurricane Electric:

Then start/enable .

## systemd-networkd
If systemd-networkd handles your network connections, it is probably a better idea to let it handle tunnel broker too (instead of using a .service file).

Replace all NNNN to your own address.

And, add this line to  section of your default Internet connection .network file:

## Using the tunneling with dynamic IPv4 IP
## Updating via cron job
The simplest way of using tunnelling with a dynamic IPv4 IP is to set up a cron job that is going to periodically update your current address. The example URL and an Update Key can be found in the Advanced tab of the Tunnel Details page.

To check if the update works, run the following command (replace ,  and  by the details of your account and tunnel):

 $ wget -O - https://USERNAME:UPDATEKEY@ipv4.tunnelbroker.net/nic/update?hostname=TUNNELID

If it works, create a cron job by opening  and adding a new line:

 */10 * * * * wget -q -O /dev/null https://USERNAME:UPDATEKEY@ipv4.tunnelbroker.net/nic/update?hostname=TUNNELID

## Updating via ddclient
Alternatively this can be configured by installing  and configuring :

 protocol=dyndns2
 use=web
 web=checkip.dns.he.net
 server=ipv4.tunnelbroker.net
 ssl=yes
 login=USERNAME
 password=UPDATEKEY
 TUNNELID

And finally start/enable .
