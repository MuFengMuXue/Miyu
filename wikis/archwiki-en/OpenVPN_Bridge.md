# OpenVPN/Bridge

This page describes how to create a network bridge on Arch Linux and host an OpenVPN server using a IP layer-2 based Ethernet bridge (TAP) rather than a IP layer-3 based IP tunnel (TUN). The general OpenVPN page describes setting up PAM authentication or OpenSSL security certificates in more detail.

## Introduction
The OpenVPN documentation page gives a full overview of server-side and client-side options that OpenVPN supports. It is easier to set up OpenVPN in tunneling mode and control routing the traffic and it is generally advised to do so if it serves your purpose. However, some network applications, such as Windows file sharing, rely on network broadcasts at the Ethernet level and benefit from believing they are physically located on the same subnet, and software bridging serves this purpose.

There are multiple ways to set bridging up. The dynamic method is where OpenVPN will be managing its own bridge on the system and will start, stop and configure it itself. This is the quickest way to set bridging up, although it interrupts other network services when OpenVPN starts and stops. If the system is going to manage its own bridge, maybe because other virtual network adapters connect to the bridge besides just that of OpenVPN, then it is preferable to use the static method.

## Dynamic Bridge Installation
You will need to install OpenVPN and Linux bridging utilities which are available in the  and  packages. To use the example script below you will also need to install the  package.

## Dynamic Bridge Configuration
OpenVPN will create/destroy the TAP device automatically for the name specified in the configuration file. OpenVPN settings common to TUN or TAP are not shown in the example configuration file below, only settings that affect TAP mode. Make sure the  and  scripts are executable after you write them.

(sections common to TUN and TAP omitted)

These examples are for using dhcp. If you are going to use static IP addresses, you will need to adjust accordingly.

## Using Systemd
The OpenVPN systemd script looks for .conf files in the /etc/openvpn folder by default. So assuming you have a file named server.conf, you can enable and start .

Be careful about having dhcpcd enabled separately (ie. dhcpcd@eth0.service) at the same time. It is possible, though unlikely, for it to complete after OpenVPN and ruin your dhcp setup for OpenVPN. You could probably disable dhcpcd@eth0.service since you know openvpn@server.service will be resetting dhcp anyway.

## Static Bridge Installation
The first thing you want to do is install these packages: , , .

## Static Bridge Configuration
Earlier versions of guides for OpenVPN provided by the OpenVPN team or various Linux packagers give example scripts for constructing a bridge when starting OpenVPN and destroying it when shutting OpenVPN down.

However, this is a somewhat deprecated approach, since OpenVPN as of 2.1.1 defaults to not allowing itself to call external scripts or programs unless explicitly enabled to, for security reasons.

Also, constructing the bridge is relatively slow compared to all other parts of the network initialization process. (In fact, so slow that dhcpcd will time out before the bridge is ready. See #Static Bridge Troubleshooting.) Also, when restarting OpenVPN after configuration changes, there is no reason to rebuild a working bridge, interrupting all your other network applications. So, setting up a static bridge configuration as follows is the recommended method.

To create an OpenVPN bridge for your server, you are going to have to use netctl and create two network profiles - one for the tap interface and one for the bridge.

Go to  and copy the tuntap example file to the directory:

 # cd /etc/netctl/
 # cp examples/tuntap openvpn_tap

Now edit  to create a tap interface. It may look like this:

Do not configure the IP address here, this is going to be done for the bridge interface!

To create the  profile, copy the example file:

 # cp examples/bridge openvpn_bridge

Now edit . It may look like this:

For more information, for example how to use DHCP instead, check the netctl article.

Now enable and start both profiles with:

 # netctl enable openvpn_tap
 # netctl enable openvpn_bridge
 # netctl start openvpn_tap
 # netctl start openvpn_bridge

## Static Bridge Troubleshooting
## Failed to start the network
This is probably because you are using DHCP on the bridge and setting up the bridge takes longer than dhcpcd is willing to wait. You can fix this by setting the FWD_DELAY parameter in your bridge network profile (openvpn_bridge). Start with a value of 5 and decrease it until it works.

## No IP Address on bridge when using DHCP
You may need to release the IP address that is assigned to your ethernet interface before requesting an IP through via DHCP.  To do this:

Then, modify the dhcpcd conf file to ensure that an ip address is not assigned to the ethernet interface (in this case, ):

Towards the end of the file (assuming your bridge is named ):

Now create the network bridge as described above, then run  to assign the ip address to your interface.  Check to see that  shows a valid ip address assigned to the bridge (i.e. ).

## More Resources
* OpenVPN - General page on configuring OpenVPN, including setting up authentication methods.
