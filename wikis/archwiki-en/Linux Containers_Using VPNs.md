# Linux Containers/Using VPNs

This article describes how to setup a Linux Container to run several VPN protocols with a "kill switch" for secure/private internet use.  Doing so offers a distinct advantage over using full-blown virtualization like VirtualBox or QEMU in that the resource overhead is minimal by comparison and able to run on low powered devices.

## Container setup
Basic setup and understanding of Linux Containers is required.  This article assumes that readers have a base LXC setup and operational.

## OpenVPN in server mode
This subsection details some extra setup required for serving OpenVPN in a container.  Users wanting to use a provided OpenVPN profile do not need to read this subsection.

## Host setup
# The host OS needs a bridge ethernet setup to allow the container to run. Refer to Linux Containers#Host network configuration for this.
# One needs to enable packet forwarding.  Refer to Internet sharing#Enable packet forwarding for this.
# Although not strictly required, a firewall is highly recommended.

## OpenVPN in client mode
The container's configuration needs to be modified to use OpenVPN as follows:

Install .  If using the container to connect to a 3rd party VPN provider, simply place the config file, ,  in  for use.  To verify OpenVPN functionality within the container, start OpenVPN via  and once satisfied enable it to run at boot.

For other use cases and setup, refer to OpenVPN.

## WireGuard
Install .  Users will either have a WireGuard config supplied by a 3rd party VPN service or will be setting up WireGuard to serve in this role.  If using the container to connect to the VPN provider, simply place the config file, , in  for use.

To verify WireGuard functionality within the container, start WireGuard via  and once satisfied enable it to run at boot.

For other use cases, refer to WireGuard.

## Firewall configuration within the container
A properly configured firewall running within the container is highly recommended.  The role of the firewall within the container is two fold:
# Provide a functional "kill switch" to maintain privacy should the connection to the VPN fail.
# Keep nasty stuff out.

This guide uses  which is easy to configure, but other examples can certainly be used.

The strategy of a functional "kill switch" is simply to setup a deny policy and then allow specific services and traffic on the VPN device only.  This way if that device's connection is interrupted, there is not a local fallback.

Edit  and change the DEFAULT_OUTPUT_POLICY from "ACCEPT" to "DROP":

Setup the deny policy:
 ufw default deny outgoing
 ufw default deny incoming

Optionally add any predefined or custom rules defined in a file such as :
 ufw allow ssh
 ufw allow from my-custom-app1
 ufw allow from my-custom-app2

Optionally further restrict access from the internal LAN IP range or even a single IP address:
 ufw allow from 192.168.1.0/24

Users of WireGuard will have an interface created that bears the same name as the respective configuration file, for example,  whereas OpenVPN users are likely using .  In the line below, substitute 'foo' with the name of the WireGuard config (omitting the .conf suffix) or if using OpenVPN, substitute 'foo' with tun0 or with whatever device is being used:

 ufw allow out on foo from any to any

Finally, allow access to the IP address of the VPN provider on the expected port and define the expected protocol.  In the line below there are three variables to consider defined as such:
* 'xxx' represents the IP address of the WireGuard peer/OpenVPN server.  It will be defined in the respective config file provided by the VPN provider.
* 'yyy' represents the port on which the communication is to take place.  Again, this will be in the config file.
* 'zzz' represents the protocol to be used and is selected from either udp or tcp.  Note that WireGuard only supports udp whereas OpenVPN supports either.

 ufw allow out to xxx port yyy proto zzz

Start ufw and enable  to start at boot.

## A hacky work-around for using a VPN's domain name in the profile
If it is desired to use a domain name in the VPN profile, a shell script on the host can pre-resolve it to a numerical IP, and then pass that IP address to the container via storing it in a variable written to a file therein.  That file can in turn be read by a modified VPN systemd service.  It works, but is a bit hacky.

Edit the two variables to match the container name and the server name corresponding to your use case:
## On the host
Install  (needed for dig) and create the following script:

From now on, call that script to start the container.  It will use dig to get the IP address from the domain name and then it will start the container.
## From inside the container
Modify the systemd service starting the VPN as well as create a skeleton profile that can be modified with the IP address defined in  by the script we just created.

To make a skeleton config file, simply rename the live one to another name.

For example using WireGuard:

 mv /etc/wireguard/foo.conf /etc/wireguard/foo.skel

Now edit  to substitute the Endpoint = www.myvpnserver.org to @@@, for example:

 Endpoint = @@@:51820

Or if using OpenVPN:

 mv /etc/openvpn/client/foo.conf /etc/openvpn/client/foo.skel

Edit  to substitute the remote www.myvpnserver.org to @@@, for example:

 remote @@@

Finally, create a drop-in file, to read in the IP and to substitute it for the actual profile.

Example using WireGuard:

Example using OpenVPN:

## Test the service
From within the running container, (connected via ssh or via ) test the setup by exporting a browser to the host's machine X server:
 $ DISPLAY=:0 firefox

The result should be a firefox window in the host's X server with the title, "Mozilla Firefox (playtime)."  A number of websites can be used to verify IP address and status of DNS entries.  Once such site is ipleak dot net.

At this point, only a the DNS entry/entries corresponding to those defined in the profile should be displayed.
