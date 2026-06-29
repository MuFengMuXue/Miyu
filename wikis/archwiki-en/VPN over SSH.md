# VPN over SSH

There are several ways to set up a Virtual Private Network through SSH. Note that, while this may be useful from time to time, it may not be a full replacement for a regular VPN. See for example == Using badvpn's tun2socks ==

 is a collection of utilities for various VPN-related use cases.

## Start SSH dynamic SOCKS proxy
First, we will set up a normal SSH dynamic socks proxy like usual:

 $ ssh -TND 4711 @

## Set up badvpn and tunnel interface
Afterwards, we can go ahead with setting up the TUN.

 # ip tuntap add dev tun0 mode tun user
 # ip addr replace 10.0.0.1/24 dev tun0
 # badvpn-tun2socks --tundev tun0 --netif-ipaddr 10.0.0.2 --netif-netmask 255.255.255.0 --socks-server-addr localhost:4711

Now you have a working local  interface which routes all traffic going into it through the SOCKS proxy you set up earlier.

## Get traffic into the tunnel
All that's left to do now is to set up a local route to get some traffic into it. Let us set up a route that routes all traffic into it. We will need three routes:

# Route that goes to the SSH server that we use for the tunnel with a low metric.
# Route for DNS server (because tun2socks does not do UDP which is necessary for DNS) with a low metric.
# Default route for all other traffic with a higher metric than the other routes.

The idea behind setting the metrics specifically is because we need to ensure that the route picked to the SSH server is always direct because otherwise it would go back into the SSH tunnel which would cause a loop and we would lose the SSH connection as a result. Apart from that, we need to set an explicit DNS route because tun2socks does not tunnel UDP (required for DNS). We also need a new default route with a lower metric than your old default route so that traffic goes into the tunnel at all. With all of that said, let us get to work:

 # ip route add  via  metric 5
 # ip route add  via  metric 5
 # ip route add default via 10.0.0.2 metric 6

Now all traffic (except for DNS and the SSH server itself) should go through .

## OpenSSH's built in tunneling
OpenSSH has built-in TUN/TAP support using . Here, a layer 3/point-to-point/ TUN tunnel is described. It is also possible to create a layer 2/ethernet/TAP tunnel.

## Enable forwarding for the TUN device
To enable forwarding for the TUN device, edit  and set  to ,  or . Setting  enables forwarding for both  and  tunnels. See  for details.

Then reload .

## Create tun interfaces using systemd-networkd
Once these files are created, enable them by restarting .

Also, you may manage tun interfaces with  command.

## Creating interfaces in SSH command
SSH creates both interfaces automatically, but IP and routing should be configured after the connection is established.

## Start SSH
or you may add keep-alive options if you are behind a NAT.

## Troubleshooting
* ssh should have access rights to tun interface or permissions to create it. Check owner of tun interface and/or /dev/net/tun.
* Obviously if you want to access a network rather than a single machine you should properly set up IP packet forwarding, routing and maybe a netfilter on both sides.
* If you do not enable tunneling, you may get the following error when you want to create an SSH tunnel using :

## Using PPP over SSH
pppd can easily be used to create a tunnel through an SSH server:

 # pppd updetach noauth silent nodeflate pty "/usr/bin/ssh root@remote-gw /usr/sbin/pppd nodetach notty noauth" ipparam vpn 10.0.8.1:10.0.8.2

When the VPN is established, you can route traffic through it. To get access to an internal network:

 # ip route add 192.168.0.0/16 via 10.0.8.2

To route all Internet traffic through the tunnel, for example, to protect your communication on an unencrypted network, first add a route to the SSH server through your regular gateway:

 # ip route add  via

Next, replace the default route with the tunnel

 # ip route replace default via 10.0.8.2

## Helper script
[https://github.com/halhen/pvpn pvpn (package ) is a wrapper script around  over SSH.
