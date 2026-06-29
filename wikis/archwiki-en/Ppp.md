# Ppp

ppp (Paul's PPP Package) is an open source package which implements the point-to-point protocol (PPP) on Linux and Solaris systems. It is implemented as single pppd daemon and acts as backend for ,  and netctl. 3G, L2TP and PPPoE connections are internally based on PPP protocol and therefore can be managed by ppp.

## Installation
Install the  package.

## Configuration
## PPPoE
Create the connection configuration file:

If  option is used, pppd will create the  file with obtained DNS addresses while establishing a connection. By default, the  hook script moves this file to , allowing the system to use these name servers. If this is undesirable (e.g. you are using a local caching DNS), edit the  as you need.

Put a line like this in  or  as required by the authentication method used by your ISP.

Chap should always be preferred, when possible, if aiming at security (to understand how chap works see this), however it is OK to write these two files at the same time, pppd will automatically use the appropriate one:

 someloginname * yourpassword

You can now start the link using the command:

 # pppd call your_provider

Alternatively, you can use this

 # pon your_provider

where your_provider is the exact name of your options file in .

To see whether your PPPoE connection is started correctly, check the pppd output in system logs:

 # journalctl -b /usr/bin/pppd

On a successful connection, you will see something like the following:

 Jul 09 22:42:33 localhost pppdPlugin pppoe.so loaded.
 Jul 09 22:42:33 localhost pppd[239: PPPoE plugin from pppd 2.5.2
 Jul 09 22:42:33 localhost pppdpppd 2.5.2 started by root, uid 0
 Jul 09 22:42:39 localhost pppd[239: PPP session is 292
 Jul 09 22:42:39 localhost pppdConnected to a0:f3:e4:4f:e3:b0 via interface enp4s0
 Jul 09 22:42:39 localhost pppd[239: Using interface ppp0
 Jul 09 22:42:39 localhost pppdConnect: ppp0  enp4s0
 Jul 09 22:42:39 localhost pppd[239: CHAP authentication succeeded: CHAP authentication success
 Jul 09 22:42:39 localhost pppdCHAP authentication succeeded
 Jul 09 22:42:39 localhost pppd[239: peer from calling number A0:F3:E4:4F:E3:B0 authorized
 Jul 09 22:42:39 localhost pppdCannot determine ethernet address for proxy ARP
 Jul 09 22:42:39 localhost pppd[239: local  IP address 10.6.2.137
 Jul 09 22:42:39 localhost pppdremote IP address 10.6.1.1
 Jul 09 22:42:39 localhost pppd[239: primary   DNS address 10.6.1.1
 Jul 09 22:42:39 localhost pppdsecondary DNS address 210.21.196.6

By default the configuration in  is treated as the default, so if you want to make "your_provider" the default, you can create a link like this

 # ln -s /etc/ppp/peers/your_provider /etc/ppp/peers/provider

Now you can start the link by simply running:

 # pon

To close a connection, use this

 # poff your_provider

## Using NetworkManager (nmcli)
On systems using NetworkManager, you can
use  to configure a PPoE connection:

 nmcli con edit type pppoe con-name ""
 nmcli> set pppoe.username
 nmcli> set pppoe.password
 nmcli> set connection.autoconnect
 nmcli> save
 nmcli> quit

## Easy wizard configuration
 provides a dialog interface to create pppd configuration easily. The usage is as simple as running  as root and it will guide the configuration creation.

 # pppconfig --dialog

The resulting configuration can be called using  and discarded using  as mentioned before.

## Starting pppd on boot
* Configure the  module to load on boot. See Kernel module#systemd for more information.
* Enable the systemd service .

## Tips and tricks
## Do an auto redial
If pppd is running, you can force a connection reset by sending the  signal to the process:

 # export PPPD_PID=$(pidof pppd)
 # kill -s HUP $PPPD_PID

And you have redialed the connection.

## Using cron
As root, do the following:

Create a bash script similar to this and give it a name (e.g. ):

 #!/bin/bash

 message="Restarting the PPP connection @:" $(date)
 pppd_id=$(pidof pppd)

 kill -s HUP $pppd_id
 echo $message

Give it execute permissions and put it on a path visible to root.

Then create a cron job using . Check that your  env variable is set if the command fails. So add anywhere in the file,

 0 4 * * * /bin/bash /root/pppd_redial.sh

Confirm that  service is up and running. If this is not the case, just enable and start it.

Save and exit. Your PPPoE connection will now restart every day at 4AM.

## Using a systemd timer
An alternative way to force a reconnect is using a systemd timer and the poff script (in particular its  option). Simply create a .service and .timer files with the same name:

Now just enable and start the timer and systemd will cause a restart at the specified time.

## Troubleshooting
## Default route
If you have a preconfigured default route before the pppd is started, the default route is kept, so take a look in  and if you have something like:

 pppd[nnnn: not replacing existing default route via xxx.xxx.xxx.xxx

and  is not the correct route for you

* Create a new script in  with this content:

* Restart the  service.

## Masquerading seems to be working fine but some sites do not work
The MTU under pppoe is 1492 bytes. Most sites use an MTU of 1500. So your connection sends an ICMP 3:4 (fragmentation needed) packet, asking for a smaller MTU, but some sites have their firewall blocking that.

Enabling the PMTU clamping in iptables can solve that:

 iptables -I FORWARD -o ppp0 -p tcp --tcp-flags SYN,RST SYN -j TCPMSS --clamp-mss-to-pmtu

Now, for some reason, just trying to save the resulting iptables configuration with iptables-save and restoring it later, does not work. It has to be executed after the other iptables configuration had been loaded. So, here is a systemd unit to solve it:

And enable it.

## pppd cannot load kernel module ppp_generic
When starting PPTP client, the pppd process cannot locate the appropriate module:

 Couldn't open the /dev/ppp device: No such device or address
 Please load the ppp_generic kernel module.

The solution is to create a  file with:

 alias char-major-108 ppp_generic

The correct module will be loaded after reboot.
