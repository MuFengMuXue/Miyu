# QEMU/Advanced networking

## Advanced bridge network configuration
## Creating bridge manually
The following describes how to bridge a virtual machine to a host interface such as , which is probably the most common configuration. This configuration makes it appear that the virtual machine is located directly on the external network, on the same Ethernet segment as the physical host machine.

We will replace the normal Ethernet adapter with a bridge adapter and bind the normal Ethernet adapter to it.

* Install , which provides  to manipulate bridges.

* Enable IPv4 forwarding:

 # sysctl -w net.ipv4.ip_forward=1

To make the change permanent, change  to  in .

* Load the  module and configure it to be loaded on boot. See Kernel modules for details.

* Optionally create the bridge. See Bridge with netctl for details. Remember to name your bridge as , or change the scripts below to your bridge's name. In the  script below,  is set up if not listed, as it is assumed that by default the host is not accessing network via the bridge.

* Create the script that QEMU uses to bring up the tap adapter with  750 permissions:

* Create the script that QEMU uses to bring down the tap adapter in  with  750 permissions:

* Use  to add the following to your  file:

* You launch QEMU using the following  script:

{{hc|run-qemu|
#!/bin/bash
: '
e.g. with img created via:
qemu-img create -f qcow2 example.img 90G
run-qemu -cdrom archlinux-x86_64.iso -boot order=d -drive file=example.img,format=qcow2 -m 4G -enable-kvm -cpu host -smp 4
run-qemu -drive file=example.img,format=qcow2 -m 4G -enable-kvm -cpu host -smp 4
'

nicbr0() {
    sudo ip link set dev $1 promisc on up &> /dev/null
    sudo ip addr flush dev $1 scope host &>/dev/null
    sudo ip addr flush dev $1 scope site &>/dev/null
    sudo ip addr flush dev $1 scope global &>/dev/null
    sudo ip link set dev $1 master br0 &> /dev/null
}
_nicbr0() {
    sudo ip link set $1 promisc off down &> /dev/null
    sudo ip link set dev $1 nomaster &> /dev/null
}

HASBR0="$( ip link show | grep br0 )"
if [ -z $HASBR0 ] ; then
    ROUTER="192.168.1.1"
    SUBNET="192.168.1."
    NIC=$(ip link show | grep en | grep 'state UP' | head -n 1 | cut -d":" -f 2 | xargs)
    IPADDR=$(ip addr show | grep -o "inet $SUBNET\(| cut -d ' ' -f2)
    sudo ip link add name br0 type bridge &> /dev/null
    sudo ip link set dev br0 up
    sudo ip addr add $IPADDR/24 brd + dev br0
    sudo ip route del default &> /dev/null
    sudo ip route add default via $ROUTER dev br0 onlink
    nicbr0 $NIC
    sudo iptables -I FORWARD -m physdev --physdev-is-bridged -j ACCEPT
fi

USERID=$(whoami)
precreationg=$(ip tuntap list | cut -d: -f1 | sort)
sudo ip tuntap add user $USERID mode tap
postcreation=$(ip tuntap list | cut -d: -f1 | sort)
TAP=$(comm -13  /dev/null
sudo ip tuntap del $TAP mode tap

if [ -z $HASBR0  ; then
    _nicbr0 $NIC
    sudo ip addr del dev br0 $IPADDR/24 &> /dev/null
    sudo ip link set dev br0 down
    sudo ip link delete br0 type bridge &> /dev/null
    sudo ip route del default &> /dev/null
    sudo ip link set dev $NIC up
    sudo ip route add default via $ROUTER dev $NIC onlink &> /dev/null
fi
}}

Then to launch a virtual machine, do something like this

 $ run-qemu -hda myvm.img -m 512

* It is recommended for performance and security reasons to disable the firewall on the bridge:

In order to apply the parameters described above on boot, you will also need to load the br-netfilter module on boot. Otherwise, the parameters will not exist when sysctl will try to modify them.

Run  to apply the changes immediately.

See the libvirt wiki and Fedora bug 512206. If you get errors by sysctl during boot about non-existing files, make the  module load at boot. See Kernel module#systemd.

Alternatively, you can configure iptables to allow all traffic to be forwarded across the bridge by adding a rule like this:

 -I FORWARD -m physdev --physdev-is-bridged -j ACCEPT

## Network sharing between physical device and a Tap device through iptables
Bridged networking works fine between a wired interface (Eg. eth0), and it is easy to setup. However if the host gets connected to the network through a wireless device, then bridging is not possible.

See Network bridge#Wireless interface on a bridge as a reference.

One way to overcome that is to setup a tap device with a static IP, making linux automatically handle the routing for it, and then forward traffic between the tap interface and the device connected to the network through iptables rules.

See Internet sharing as a reference.

There you can find what is needed to share the network between devices, included tap and tun ones. The following just hints further on some of the host configurations required. As indicated in the reference above, the client needs to be configured for a static IP, using the IP assigned to the tap interface as the gateway. The caveat is that the DNS servers on the client might need to be manually edited if they change when changing from one host device connected to the network to another.

To allow IP forwarding on every boot, one need to add the following lines to sysctl configuration file inside :

 net.ipv4.ip_forward = 1
 net.ipv6.conf.default.forwarding = 1
 net.ipv6.conf.all.forwarding = 1

The iptables rules can look like:

 # Forwarding from/to outside
 iptables -A FORWARD -i ${INT} -o ${EXT_0} -j ACCEPT
 iptables -A FORWARD -i ${INT} -o ${EXT_1} -j ACCEPT
 iptables -A FORWARD -i ${INT} -o ${EXT_2} -j ACCEPT
 iptables -A FORWARD -i ${EXT_0} -o ${INT} -j ACCEPT
 iptables -A FORWARD -i ${EXT_1} -o ${INT} -j ACCEPT
 iptables -A FORWARD -i ${EXT_2} -o ${INT} -j ACCEPT
 # NAT/Masquerade (network address translation)
 iptables -t nat -A POSTROUTING -o ${EXT_0} -j MASQUERADE
 iptables -t nat -A POSTROUTING -o ${EXT_1} -j MASQUERADE
 iptables -t nat -A POSTROUTING -o ${EXT_2} -j MASQUERADE

The prior supposes there are 3 devices connected to the network sharing traffic with one internal device, where for example:

 INT=tap0
 EXT_0=eth0
 EXT_1=wlan0
 EXT_2=tun0

The prior shows a forwarding that would allow sharing wired and wireless connections with the tap device.

The forwarding rules shown are stateless, and for pure forwarding. One could think of restricting specific traffic, putting a firewall in place to protect the guest and others. However those would decrease the networking performance, while a simple bridge does not include any of that.

Bonus:  Whether the connection is wired or wireless, if one gets connected through VPN to a remote site with a tun device, supposing the tun device opened for that connection is tun0, and the prior iptables rules are applied, then the remote connection gets also shared with the guest. This avoids the need for the guest to also open a VPN connection. Again, as the guest networking needs to be static, then if connecting the host remotely this way, one most probably will need to edit the DNS servers on the guest.

## Networking with VDE2
## What is VDE?
VDE stands for Virtual Distributed Ethernet. It started as an enhancement of uml_switch. It is a toolbox to manage virtual networks.

The idea is to create virtual switches, which are basically sockets, and to "plug" both physical and virtual machines in them. The configuration we show here is quite simple; However, VDE is much more powerful than this, it can plug virtual switches together, run them on different hosts and monitor the traffic in the switches. You are invited to read the documentation of the project.

The advantage of this method is you do not have to add sudo privileges to your users. Regular users should not be allowed to run modprobe.

## Basics
VDE support can be installed via the  package.

In our config, we use tun/tap to create a virtual interface on my host. Load the  module (see Kernel modules for details):

 # modprobe tun

Now create the virtual switch:

 # vde_switch -tap tap0 -daemon -mod 660 -group users

This line creates the switch, creates , "plugs" it, and allows the users of the group  to use it.

The interface is plugged in but not configured yet. To configure it, run this command:

 # ip addr add 192.168.100.254/24 dev tap0

Now, you just have to run KVM with these  options as a normal user:

 $ qemu-system-x86_64 -net nic -net vde -hda ''Configure networking for your guest as you would do in a physical network.

## Startup scripts
Example of main script starting VDE:

{{hc|/etc/systemd/scripts/qemu-network-env|
#!/bin/sh
# QEMU/VDE network environment preparation script

# The IP configuration for the tap device that will be used for
# the virtual machine network:

TAP_DEV=tap0
TAP_IP=192.168.100.254
TAP_MASK=24
TAP_NETWORK=192.168.100.0

# Host interface
NIC=eth0

case "$1" in
  start)
        echo -n "Starting VDE network for QEMU: "

        # If you want tun kernel module to be loaded by script uncomment here
	#modprobe tun 2>/dev/null
	## Wait for the module to be loaded
 	#while ! lsmod | grep -q "^tun"; do echo "Waiting for tun device"; sleep 1; done

        # Start tap switch
        vde_switch -tap "$TAP_DEV" -daemon -mod 660 -group users

        # Bring tap interface up
        ip address add "$TAP_IP"/"$TAP_MASK" dev "$TAP_DEV"
        ip link set "$TAP_DEV" up

        # Start IP Forwarding
        echo "1" > /proc/sys/net/ipv4/ip_forward
        iptables -t nat -A POSTROUTING -s "$TAP_NETWORK"/"$TAP_MASK" -o "$NIC" -j MASQUERADE
        ;;
  stop)
        echo -n "Stopping VDE network for QEMU: "
        # Delete the NAT rules
        iptables -t nat -D POSTROUTING -s "$TAP_NETWORK"/"$TAP_MASK" -o "$NIC" -j MASQUERADE

        # Bring tap interface down
        ip link set "$TAP_DEV" down

        # Kill VDE switch
        pgrep vde_switch | xargs kill -TERM
        ;;
  restart|reload)
        $0 stop
        sleep 1
        $0 start
        ;;
  *)
        echo "Usage: $0 {start|stop|restart|reload}"
        exit 1
esac
exit 0
}}

Example of systemd service using the above script:

Change permissions for  to be executable.

You can start  as usual.

## Alternative method
If the above method does not work or you do not want to mess with kernel configs, TUN, dnsmasq, and iptables you can do the following for the same result.

 # vde_switch -daemon -mod 660 -group users
 # slirpvde --dhcp --daemon

Then, to start the virtual machine with a connection to the network of the host:

 $ qemu-system-x86_64 -net nic,macaddr=52:54:00:00:EE:03 -net vde disk_image

## VDE2 Bridge
Based on [https://selamatpagicikgu.wordpress.com/2011/06/08/quickhowto-qemu-networking-using-vde-tuntap-and-bridge/ quickhowto: qemu networking using vde, tun/tap, and bridge graphic. Any virtual machine connected to vde is externally exposed. For example, each virtual machine can receive DHCP configuration directly from your ADSL router.

## Basics
Remember that you need  module and  package.

Create the vde2/tap device:

 # vde_switch -tap tap0 -daemon -mod 660 -group users
 # ip link set tap0 up

Create bridge:

 # brctl addbr br0

Add devices:

 # brctl addif br0 eth0
 # brctl addif br0 tap0

And configure bridge interface:

 # dhcpcd br0

## Startup scripts
All devices must be set up. And only the bridge needs an IP address. For physical devices on the bridge (e.g. ), this can be done with netctl using a custom Ethernet profile with:

The following custom systemd service can be used to create and activate a VDE2 tap interface for users in the  user group.

And finally, you can create the bridge interface with netctl.
