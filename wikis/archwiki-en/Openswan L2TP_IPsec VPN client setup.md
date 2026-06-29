# Openswan L2TP/IPsec VPN client setup

This article describes how to configure and use a L2TP/IPsec Virtual Private Network client on Arch Linux. It covers the installation and setup of several needed software packages. L2TP refers to the Layer 2 Tunneling Protocol, and for IPsec, the Openswan implementation is employed.

This guide is primarily targeted for clients connecting to a Windows Server machine, as it uses some settings that are specific to the Microsoft implementation of L2TP/IPsec. However, it is adaptable with any other common L2TP/IPsec setup. The Openswan wiki features instructions to set up a corresponding L2TP/IPSec Linux server.

## Installation
To use with NetworkManager, install the  and  packages.

Otherwise install the  and  packages.

## Configuration
## NetworkManager
Open the NetworkManager UI, then:
# Go to Network > VPN. Click "+"
# Select "Layer 2 Tunneling Protocol (L2TP)."
# You can choose a name for the VPN.
# Enter Your VPN Server IP for the Gateway.
# Enter Your VPN Username for the User name.
# Right-click the ? in the Password field, select Store the password only for this user. (If this option gives you trouble, you might want to use "Store password for all users")
# Enter Your VPN Password for the Password.
# Leave the NT Domain field blank.
# Click the IPsec Settings... button.
# Check the Enable IPsec tunnel to L2TP host checkbox.
# Leave the Gateway ID field blank.
# Enter Your VPN IPsec PSK for the Pre-shared key.
# OK, then click Add to save the VPN connection information.

Now you should be able to start the VPN, by switching the Toggle-Button on.

## OpenSwan
Edit  to contain the following lines:

This file contains the basic information to establish a secure IPsec tunnel to the VPN server. It enables NAT Traversal for if your machine is behind a NAT'ing router (most people are), and various other options that are necessary to connect correctly to the remote IPsec server. The next file contains your pre-shared key (PSK) for the server.

Create the file : It should contain the following line:
 192.168.0.123 68.68.32.79 : PSK "your_pre_shared_key"

Remember to replace the local () and remote () IP addresses with the correct numbers for your location. The pre-shared key will be supplied by the VPN provider and will need to be placed in this file in cleartext form. You may find this file already exists and already have some data, try to back it up and create a new file only with your PSK if you will see  when enabling connection in next section. Do not forget to set proper permissions (600) for this file or you will get error message .

Add the connection, so it is available to use:

 # ipsec auto --add L2TP-PSK

At this point the IPsec configuration is complete and we can move on to the L2TP configuration.

## Running Openswan in a container
Do not forget to add CAP_SYS_MODULE capability and access to host module tree. Example for nspawn:
 --bind=/lib/modules --capability=CAP_SYS_MODULE

## xl2tpd
Edit  so it has the following contents:

This file configures xl2tpd with the connection name, server IP address (which again, please remember to change to your servers address) and various options that will be passed to pppd once the tunnel is set up.

Now create  with the following contents:

Place your assigned username and password for the VPN server in this file. A lot of these options are for interoperability with Windows Server L2TP servers. If your VPN server uses PAP authentication, replace  with .

This concludes the configuration of the applicable software suites to connect to a L2TP/IPsec server. To start the connection do the following:

Start  and .
 # ipsec auto --up L2TP-PSK
 # echo "c vpn-connection" > /var/run/xl2tpd/l2tp-control

At this point the tunnel is up and you should be able to see the interface for it if you type:

 $ ip link

You should see a  device that represents the tunnel. Right now, nothing is going to get routed through it. You need to add some routing rules to make it work right:

## Routing
## Routing traffic to a single IP address or subnet through the tunnel
This is as easy as adding a routing rule to your kernel table:

 # ip route add xxx.xxx.xxx.xxx via yyy.yyy.yyy.yyy dev pppX

Note xxx.xxx.xxx.xxx is the specific ip address (e.g. 192.168.3.10) or subnet (e.g. 192.168.3.0/24) that you wish to communicate with through the tunnel device (e.g. ppp0).

Note yyy.yyy.yyy.yyy is "peer ip" of your pppX device used to route traffic to tunnel destination xxx.xxx.xxx.xxx.

See example below for command to identify tunnel device name and peer ip and then add route. :

 # ip route add 192.168.3.0/24 via 192.0.2.1 dev ppp0

## Routing all traffic through the tunnel
This is a lot more complex, but all your traffic will travel through the tunnel. Start by adding a special route for the actual VPN server through your current gateway:

 # ip route add 68.68.32.79 via 192.168.1.1 dev eth0

This will ensure that once the default gateway is changed to the ppp interface that your network stack can still find the VPN server by routing around the tunnel. If you miss this step you will lose connectivity to the Internet and the tunnel will collapse. Now add a default route that routes to the PPP remote end:

 # ip route add default via yyy.yyy.yyy.yyy dev pppX

The remote PPP end can be discovered by following the step in the previous section. Now to ensure that ALL traffic is routing through the tunnel, delete the original default route:

 # ip route delete default via 192.168.1.1 dev eth0

To restore your system to the previous state, you can reboot or reverse all of the above steps.

The route creation can also be automated by placing a script in /etc/ppp/ip-up.d.

## Troubleshooting
Issue: journalctl logs VPN connection: failed to connect: 'Could not restart the ipsec service.

Solution Make sure you have strongswan installed

Issue: I get a message from pppd saying "Failed to authenticate ourselves to peer" and I have verified my password is correct. What could be wrong?

Solution 1: If you see the following in your /var/log/daemon.log:

then you are authenticating against a SonicWALL LNS that does not know how to handle CHAP-style authentication correctly.

The solution to this is to add the following to your options.l2tp.client file:

This will cause the SonicWALL to default to the next authentication mechanism, namely MSCHAP-v2. This should authenticate successfully, and from this point xl2tpd should successfully construct a tunnel between you and the remote L2TP server.

Solution 2: If you see the following in your journal after running  as root:

Try adding domain name in front of username in your options.l2tpd.client file (note the double backslash), i.e:

Issue: cannot initiate connection with ID wildcards (kind=CK_TEMPLATE) after running  when using Openswan 3.0.0.

Determine the private IP of the VPN server in the target network behind the VPN, and add the corresponding line to :

## Tips and tricks
## Script start up and shut down
You can create some scripts either in your home directory or elsewhere(remember where you put them) to bring up the tunnel then shut it back down.

First, a utility script to automatically discover PPP distant ends:

{{hc|getip.sh|
#!/bin/bash

ifconfig $1 | grep "P-t-P" | gawk -F: '{print $2}' | gawk '{print $1}'
}}

Next, the script to bring the tunnel up. This will replace the default route, so all traffic will pass via the tunnel:

Finally, the shutdown script, it simply reverses the process:

## A further script
Above script really help me work. And notice the script use fixed ip, and someone like me may change net vpn addr, i would like to put my further script below(not sure how to add attachment, so just raw ):

{{bc|
#!/bin/bash
if [ $# != 1 ] ; then
	echo "Usage: (sudo) sh $0 {init|start|stop}"
	exit 1;
fi

VPN_ADDR=XXX
IFACE=wlan0

function getIP(){
	ip addr show $1 | grep "inet " | awk '{print $2}' | sed 's:/.*::'
}

function getGateWay(){
	ip route show default | awk '/default/ {print $3}'
}
function getVPNGateWay(){
	ip route | grep -m 1 "$VPN_ADDR" | awk '{print $3}'
}

GW_ADDR=$(getGateWay)

function init(){
	cp ./options.l2tpd.client /etc/ppp/
	cp ./ipsec.conf /etc/
	cp ./ipsec.secrets /etc/
	cp ./xl2tpd.conf /etc/xl2tpd/
}

function start(){
	sed -i "s/^lns =.*/lns = $VPN_ADDR/g" /etc/xl2tpd/xl2tpd.conf
	sed -i "s/plutoopts=.*/plutoopts=\"--interface=$IFACE\"/g" /etc/ipsec.conf
	sed -i "s/left=.*$/left=$(getIP $IFACE)/g" /etc/ipsec.conf
	sed -i "s/right=.*$/right=$VPN_ADDR/g" /etc/ipsec.conf
	sed -i "s/^.*: PSK/$(getIP $IFACE) $VPN_ADDR : PSK/g" /etc/ipsec.secrets
	systemctl start openswan
	sleep 2    #delay to ensure that IPsec is started before overlaying L2TP

	systemctl start xl2tpd
	ipsec auto --up L2TP-PSK
	echo "c vpn-connection" > /var/run/xl2tpd/l2tp-control
	sleep 2    #delay again to make that the PPP connection is up.

        ip route add $VPN_ADDR via $GW_ADDR dev $IFACE
        ip route add default via $(getIP ppp0)
        ip route del default via $GW_ADDR
}

function stop(){
	ipsec auto --down L2TP-PSK
	echo "d vpn-connection" > /var/run/xl2tpd/l2tp-control
	systemctl stop xl2tpd
	systemctl stop openswan

	VPN_GW=$(getVPNGateWay)
        ip route del $VPN_ADDR via $VPN_GW dev $IFACE
        ip route add default via $VPN_GW
}

$1
exit 0
}}

## Script to resolve dns names and connect
Very useful if you have dynamic IP for the server.

{{bc|
#!/bin/python

from os import system
from socket import gethostbyname
from netifaces import ifaddresses, AF_INET
from time import sleep

# netifaces is a library installed with pip, not part of default insatllation of python
# The script is useful if you have dynamic IP, or need to use a domain for the vpn server
# gist: https://gist.github.com/physicalit/bf9e27c7ecbc12843cd68e442358616c
# The template files are identical to the examples from the link above, except they use the sign ` /var/run/xl2tpd/l2tp-control')
    sleep(2) # very important or is not going to see ppp0 interface
    if not vpn:
        peer = ifaddresses('ppp0')route = system('ip route add 192.168.88.0/24 via {0} dev ppp0'.format(peer))
        if not route:
            print("VPN sucesfully connected. Route created.")
        else:
            print("VPN KO")
}}
