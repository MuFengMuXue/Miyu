# PPTP Client

pptpclient is a program implementing the Microsoft PPTP protocol. As such, it can be used to connect to a Microsoft VPN network (or any PPTP-based VPN) provided by a school or workplace.

## Installation
Install the  package.

## Configure
To configure pptpclient you will need to collect the following information from your network administrator:

* The IP address or hostname of the VPN server.
* The username you will use to connect.
* The password you will use to connect.
* The authentication (Windows) domain name. This is not necessary for certain networks.

You must also decide what to name the tunnel.

## Configure using pptpsetup
You can configure and delete tunnels by running the pptpsetup tool as root. For example:

 pptpsetup --create my_tunnel --server vpn.example.com --username archie --password foo --encrypt
 pptpsetup --delete my_tunnel

You can #Connect after a tunnel has been configured.

## Configure by hand
You can also edit all necessary configuration files by hand, rather than relying on pptpsetup.

## Edit The options File
The  file sets security options for your VPN client. If you have trouble connecting to your network, you may need to relax the options. At a minimum, this file should contain the options , ,  and .

## Edit The chap-secrets File
The  file contains credentials for authenticating a tunnel. Make sure no one except root can read this file, as it contains sensitive information.
 chmod 0600 /etc/ppp/chap-secrets

Edit the file. It has the following format:

Replace each bracketed term with an appropriate value. Omit  if your connection does not require a domain.

## Name Your Tunnel
The  file contains tunnel-specific configuration options.  is the name you wish to use for your VPN connection. The file should look like this:

Again, omit  if your connection does not require a domain.  is the remote address of the VPN server,  is the domain your user belongs to,  is the name you will use to connect to the server, and  is the name of the connection.

## Connect
To make sure that everything is configured properly, as root execute:
 # pon  debug dump logfd 2 nodetach

If everything has been configured correctly, the  command should not terminate. Once you are satisfied that it has connected successfully, you can terminate the command.

To connect to your VPN normally, simply execute:
 # pon

Where  is the name of the tunnel you established earlier. Note that this command should be run as root.

## Routing
Once you have connected to your VPN, you should be able to interact with anything available on the VPN server. To access anything on the remote network, you need to add a new route to your routing table.

For more information on how to add routes, you can read this article which has many more examples: PPTP Routing Howto

## Split Tunneling
Packets with a destination of your VPN's network should be routed through the VPN interface (usually ). To do this, you create the route:
 # ip route add 192.168.10.0/24 dev ppp0

This will route all the traffic with a destination of 192.168.10.* through your VPN's interface, ().

## Route All Traffic
It may be desirable to route all traffic through your VPN connection. You can do this by running:
 # ip route add default dev ppp0

## Route All Traffic by /etc/ppp/ip-up.d
Make sure the script is executable.

## Split Tunneling based on port by /etc/ppp/ip-up.d
Make sure the script is executable and that the vpn table is added to

 201 vpn

## Disconnect
Execute the following to disconnect from a VPN:

 # poff

 is the name of your tunnel.

## Making A VPN Daemon and Connecting On Boot
You can create a simple daemon for your VPN connection by creating an appropriate  script:

{{Note|1=The stop functionality of this script will not work if the  and  arguments are passed to  when pon is started. The reason for this is that the  script contains a bug when determining the PID of the specified  process if arguments were passed to .

To resolve this issue, you can patch your  file by making the following changes on line 93:
{{bc|-PID=`ps axw | grep "[ /]pppd call $1 *\$" | awk '{print $1}'`
+PID=`ps axw | grep "[ /]pppd call $1" | awk '{print $1}'`}}}}

{{hc|/etc/rc.d/name-of-your-vpn|
#!/bin/bash

. /etc/rc.conf
. /etc/rc.d/functions

DAEMON=-vpn
ARGS=

[ -r /etc/conf.d/$DAEMON ] && . /etc/conf.d/$DAEMON

case "$1" in
 start)
   stat_busy "Starting $DAEMON"
   pon  updetach persist &>/dev/null &&  &>/dev/null
   if [ $? = 0 ]; then
     add_daemon $DAEMON
     stat_done
   else
     stat_fail
     exit 1
   fi
   ;;
 stop)
   stat_busy "Stopping $DAEMON"
   poff  &>/dev/null
   if [ $? = 0 ]; then
     rm_daemon $DAEMON
     stat_done
   else
     stat_fail
     exit 1
   fi
   ;;
 restart)
   $0 stop
   sleep 1
   $0 start
   ;;
 *)
   echo "usage: $0 {start|stop|restart}"
esac
}}

## Troubleshooting
If client connections keep timing out with "LCP: timeout sending Config-Requests", make sure that GRE is allowed through the client firewall. For iptables, the necessary command is:
 iptables -A INPUT -p 47 -j ACCEPT

Alternatively, if you only want to allow PPTP traffic that corresponds to a connection request coming from your local machine, you can use the conntrack PPTP helper:

 iptables -A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
 iptables -t raw -A OUTPUT -p tcp --dport 1723 -j CT --helper pptp

The second line should autoload the  and  kernel modules, which are needed for this.

If you get “EAP: unknown authentication type 26; Naking”, open /etc/ppp/options.pptp and commented out the lines refuse-chap and refuse-mschap
and add the options file entry to the tunnel file like this:

## Remarks
You can find more information about configuring pptpclient at their website: pptpclient website. The contents of this article were adapted from their Ubuntu How-To which also provides some hints on how to do things such as connecting on boot. These examples should be easy to adapt into daemons or other scripts to help automate your configuration.
