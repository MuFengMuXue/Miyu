This page is inspired by [Android USB tethering](https://wiki.gentoo.org/wiki/Android_USB_tethering "Android USB tethering"). It only documents the differences.

## Contents

-   [[1] [Tested devices]](#Tested_devices)
-   [[2] [Kernel]](#Kernel)
-   [[3] [Tools needed]](#Tools_needed)
-   [[4] [ipheth interface]](#ipheth_interface)
-   [[5] [udev trigger]](#udev_trigger)

## [Tested devices]

-   iPhone 4S, iOS5
-   iPhone 5, iOS6
-   iPhone 5S, iOS9
-   iPhone 7, iOS 14.7.1
-   iPhone 11 Pro Max, iOS 18.5
-   iPhone 15 Pro, iOS 18.1.1

## [Kernel]

[KERNEL] **Linux 4.4**

    Device Drivers
      -> Network device support (NETDEVICES)
        -> USB Network Adapters (USB_NET_DRIVERS)
             <*>  Apple iPhone USB Ethernet driver (USB_IPHETH)

## [Tools needed]

You will also need [[[app-pda/usbmuxd]](https://packages.gentoo.org/packages/app-pda/usbmuxd)[]] and [[[app-pda/ifuse]](https://packages.gentoo.org/packages/app-pda/ifuse)[]] from the default portage tree.

`root `[`#`]`emerge --ask app-pda/usbmuxd app-pda/ifuse`

## [ipheth interface]

If everything is installed successfully, plug in the iPhone with USB cable. You should see something like:

[CODE] **dmesg: iPhone ipheth**

    [    2.080017] usb 8-1: new high-speed USB device number 2 using ehci_hcd
    [    2.215940] usb 8-1: New USB device found, idVendor=05ac, idProduct=12a0
    [    2.215946] usb 8-1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
    [    2.215950] usb 8-1: Product: iPhone
    [    2.215953] usb 8-1: Manufacturer: Apple Inc.
    [    2.215956] usb 8-1: SerialNumber: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    [   26.988569] ipheth 8-1:4.2: Apple iPhone USB Ethernet device attached
    [   26.988939] usbcore: registered new interface driver ipheth

A new network interface **eth1** plugged by ipheth can be found, after running DHCP on it:

`root `[`#`]`ip a show eth1`

    4: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UNKNOWN qlen 1000
        link/ether 9e:20:7b:6b:94:bd brd ff:ff:ff:ff:ff:ff
        inet 172.20.10.2/28 brd 172.20.10.15 scope global eth1
        inet6 fe80::9c20:7bff:fe6b:94bd/64 scope link
           valid_lft forever preferred_lft forever

\
If no output is observed from dmesg, try mounting the iphone via ifuse:

`root `[`#`]`ifuse /mnt/`

The device must be unlocked and incoming connections must be allowed while ifuse is mounting. Ifuse will guide provide guidance though the process; follow its instructions and try mounting until it succeeds.

## [udev trigger]

The [hotplug feature of OpenRC](https://wiki.gentoo.org/wiki/OpenRC/Event_driven "OpenRC/Event driven") can be used to set up the ipheth interface automatically.

[[[sys-fs/udev-init-scripts]](https://packages.gentoo.org/packages/sys-fs/udev-init-scripts)[]] ships [/lib/udev/net.sh], which can be used to hotplug network interfaces. The main part of the script is

[FILE] **`/lib/udev/net.sh`net interface hotplug**

    IFACE=$1
    ACTION=$2
    ...
    SCRIPT=/etc/init.d/net.$IFACE
    ...
    IN_HOTPLUG=1 "$" --quiet "$"

and it can be called with a [udev rule](https://wiki.gentoo.org/wiki/Udev "Udev"):

[FILE] **`/lib/udev/rules.d/90-iphone-tether.rules`net.sh trigger**

    # udev rules for setting correct configuration and pairing on tethered iPhones
    ATTR!="05ac", GOTO="ipheth_rules_end"

    # Execute pairing program when appropriate
    ACTION=="add", SUBSYSTEM=="net", ENV=="ipheth", SYMLINK+="iphone", RUN+="ipheth-pair", RUN+="net.sh eth1 start"
    SUBSYSTEM=="net", ACTION=="remove", ENV=="ipheth", SYMLINK+="iphone", RUN+="net.sh %k stop"

    LABEL="ipheth_rules_end"

Enable hotplug to eth1, the ipheth device:

[FILE] **`/etc/rc.conf`rc_hotplug**

    # rc_hotplug is a list of services that we allow to be hotplugged.
    # By default we do not allow hotplugging.
    # A hotplugged service is one started by a dynamic dev manager when a matching
    # hardware device is found.
    # This service is intrinsically included in the boot runlevel.
    # To disable services, prefix with a !
    # Example - rc_hotplug="net.wlan !net.*"
    # This allows net.wlan and any service not matching net.* to be plugged.
    # Example - rc_hotplug="*"
    # This allows all services to be hotplugged
    rc_hotplug="net.eth1"

add net.eth1:

`root `[`#`]`ln -s /etc/init.d/net. `

After plugging in the iPhone, we can see the service started:

`root `[`#`]`rc-status`

    ...
    Dynamic Runlevel: hotplugged
     net.eth1                        [  started  ]
    ...