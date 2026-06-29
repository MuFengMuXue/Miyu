[[]]This article has some todo items:\

-   migrate \"pm-utils\" instructions to use [elogind](https://wiki.gentoo.org/wiki/Elogind "Elogind") instead, see [https://gitweb.gentoo.org/repo/gentoo.git/commit/profiles/package.mask?id=315d70c92b40d8bb1af7402aab9f0e6bd53f5a0e](https://gitweb.gentoo.org/repo/gentoo.git/commit/profiles/package.mask?id=315d70c92b40d8bb1af7402aab9f0e6bd53f5a0e)

This article shows how to set up OpenRC to act as a convenient, transparent, and flexible networking client which supports roaming as an alternative to [other roaming solutions](https://wiki.gentoo.org/wiki/Network_management "Network management") often used on notebooks.

## Contents

-   [[1] [Requirements]](#Requirements)
-   [[2] [Configuration and setup]](#Configuration_and_setup)
    -   [[2.1] [OpenRC service management]](#OpenRC_service_management)
        -   [[2.1.1] [Suspend to RAM example]](#Suspend_to_RAM_example)
        -   [[2.1.2] [Exclusive network interface example]](#Exclusive_network_interface_example)
        -   [[2.1.3] [Network specific log-in procedure example]](#Network_specific_log-in_procedure_example)
    -   [[2.2] [WiFi management]](#WiFi_management)
    -   [[2.3] [Ethernet management]](#Ethernet_management)
-   [[3] [References]](#References)

## [Requirements]

The currently stable version of these packages are all that is needed (no \*kit software required):

-   [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") ([[[sys-apps/openrc]](https://packages.gentoo.org/packages/sys-apps/openrc)[]]) - management of services
    -   have the netifrc USE flag enabled if you want the good old net.\* style network management
-   [wpa_supplicant](https://wiki.gentoo.org/wiki/Wpa_supplicant "Wpa supplicant") --- an app for [Wi-Fi](https://wiki.gentoo.org/wiki/Wi-Fi "Wi-Fi") authentication([[[net-wireless/wpa_supplicant]](https://packages.gentoo.org/packages/net-wireless/wpa_supplicant)[]])
    -   enable the qt5 USE flag if you want to have a GUI for the Wi-FI client
-   [[[sys-apps/ifplugd]](https://packages.gentoo.org/packages/sys-apps/ifplugd)[]] - for hotplugging of ethernet interfaces
    -   [[[sys-apps/netplug]](https://packages.gentoo.org/packages/sys-apps/netplug)[]] can be used as an alternative, but development has been discontinued
-   [dhcpcd](https://wiki.gentoo.org/wiki/Dhcpcd "Dhcpcd") --- a popular DHCP client capable of handling both IPv4 and IPv6 configuration. ([[[net-misc/dhcpcd]](https://packages.gentoo.org/packages/net-misc/dhcpcd)[]])
    -   other compatible DHCP clients exist (dhclient provided by [[[net-misc/dhcp]](https://packages.gentoo.org/packages/net-misc/dhcp)[]] or udhcp provided by [[[sys-apps/busybox]](https://packages.gentoo.org/packages/sys-apps/busybox)[]]), but dhcpcd is the recommended solution as it works well with often reconfigured wireless interfaces (so the wireless interface doesn\'t need hotplugging)

## [Configuration and setup]

Before you start configuring the interfaces, make sure that they work (meaning you have the required drivers installed) and that you know their names. A convenient way is to make a [Udev rule to give them human-readable names](https://wiki.gentoo.org/wiki/Udev#NIC_assigned_eth0.2C_but_is_moved_to_eth1 "Udev") like ethernet0, wireless0.

### [OpenRC service management]

For each interface an init script must be created for OpenRC to manage that interface by making a symlink to net.lo

`root `[`#`]`ln -s /etc/init.d/net.lo /etc/init.d/net.$ `

where **\$** is the name of the interface, e.g. eth0, wlan0, ethernet0, wireless0

If simple roaming is required, any network interface will satisfy the virtual **net** service. Therefore it is recommended to set rc_depend_strict=\"NO\" in [/etc/rc.conf].

[FILE] **`/etc/rc.conf`**

    rc_depend_strict="NO"

The services responsible for managing the interfaces must be added to one or more runlevel. This makes it possible to have network profiles by having most services in the default runlevel and then adding the interfaces to [stacked runlevels](https://wiki.gentoo.org/wiki/OpenRC/Stacked_runlevel "OpenRC/Stacked runlevel") and having different configuration files in [/etc/conf.d/] for each runlevel as [/etc/conf.d/net.\$

The options and syntax of [/etc/conf.d/net] is described in the [Gentoo Handbook](https://wiki.gentoo.org/wiki/Handbook:X86/Networking/Introduction "Handbook:X86/Networking/Introduction") which shows how to set up more complicated networks (this how-to assumes that all connections are initiated via DHCP)

#### [Suspend to RAM example]

With most services in the default runlevel and network services in a runlevel \"network\", which is [stacked](https://wiki.gentoo.org/wiki/OpenRC/Stacked_runlevel "OpenRC/Stacked runlevel") on top of the default runlevel, a PM hook for [[[sys-power/pm-utils]](https://packages.gentoo.org/packages/sys-power/pm-utils)[]] can be crated which transparently stops network services before suspending, thus preventing timeouts and other problems.

`root `[`#`]`mkdir /etc/runlevels/network/ `

`root `[`#`]`rc-update --stack add default network # include init scripts form the default runlevel in the network runelvel `

`root `[`#`]`rc-update del net.ethernet0 default # remove networking scripts from the default runlevel `

`root `[`#`]`rc-update add net.ethernet0 network # and add them to the network runlevel `

`root `[`#`]`rc-update del net.wireless0 default `

`root `[`#`]`rc-update add net.wireless0 network `

`root `[`#`]`rc-update del netmount default # remove dependent networking services from the default runlevel `

`root `[`#`]`rc-update add netmount network # which would start the networking scripts because of "need net" stanza `

[FILE] **`/etc/pm/sleep.d/00network`PM hook example**

    #!/bin/bash

    # properly stop and start the network

    if [ -r "$" ]; then
        . "$"
    elif [ -r "$" ]; then
        . "$"
    else
    # pm-utils version is too old, or something else is wrong
        exit $NA
    fi

    case "$1" in
        hibernate|suspend)
            exec rc default
            ;;
        thaw|resume)
            exec rc network
            ;;
        *) exit $NA
            ;;
    esac

The hook must be executable:

`root `[`#`]`chmod a+x /etc/pm/sleep.d/00network`

To boot into the network runlevel rather than the default one, [/etc/inittab] must be changed as explained in [the Handbook](https://wiki.gentoo.org/wiki/Complete_Handbook/Configuring_the_boot_process#Init "Complete Handbook/Configuring the boot process")

[FILE] **`/etc/inittab`**

    # Default runlevel.
    id:4:initdefault:         #was 3 - can still be 3, it only depends which runlevel is assigned to network below

    l0:0:wait:/sbin/rc shutdown
    l0s:0:wait:/sbin/halt -dhp
    l1:1:wait:/sbin/rc single
    l2:2:wait:/sbin/rc nonetwork
    l3:3:wait:/sbin/rc default
    l4:4:wait:/sbin/rc network      # was default
    l5:5:wait:/sbin/rc default
    l6:6:wait:/sbin/rc reboot
    l6r:6:wait:/sbin/reboot -dk

The bootloader can also support multiple options for different setups:

[FILE] **`/boot/grub/grub.conf`Grub v1 example**

    default 0
    timeout 30

    title Gentoo Linux 2.6.24-r5 with network
    root (hd0,0)
    kernel /boot/kernel-genkernel-x86-2.6.24-gentoo-r5 root=/dev/sda3
    initrd /boot/initramfs-genkernel-x86-2.6.24-gentoo-r5

    title Gentoo Linux 2.6.24-r5 no network
    root (hd0,0)
    kernel /boot/kernel-genkernel-x86-2.6.24-gentoo-r5 root=/dev/sda3 3
    initrd /boot/initramfs-genkernel-x86-2.6.24-gentoo-r5

#### [Exclusive network interface example]

It may be desirable to have always only one networking interface configured. This can be done by the postup or postdown functions defined in [/etc/conf.d/net]^[\[1\]](#cite_note-handbook-functions-1)^

[FILE] **`/etc/conf.d/net`**

    postup_wireless0()

    postup_ethernet0()

    postdown_wireless0()

    postdown_ethernet0()

#### [Network specific log-in procedure example]

The postup or postup\_\$ (this function would be triggered only after successful connection to the given \$) functions defined in [/etc/conf.d/net]^[\[1\]](#cite_note-handbook-functions-1)^ can be used to submit data to e.g. a web log-in form.

[FILE] **`/etc/conf.d/net`**

    postup_someESSID()

### [WiFi management]

See [wpa_supplicant](https://wiki.gentoo.org/wiki/Wpa_supplicant "Wpa supplicant").

### [Ethernet management]

OpenRC automatically hotplugs all interfaces if configured in [/etc/rc.conf]:

[FILE] **`/etc/rc.conf`**

    rc_hotplug="*"

so the respective services will be started if that interface becomes available and ifplugd will be automatically started for every ethernet interface to ensure that the device gets configured when a carrier is acquired (e.g. a cable is plugged in). ifplugd will emit beeps on state change which can be disabled in [/etc/conf.d/net]

[FILE] **`/etc/conf.d/net`disabling ifplugd beeping for interface ethernet0**

    ifplugd_ethernet0="--no-beep"

## [References]

1.  [[↑ ^[1.0](#cite_ref-handbook-functions_1-0)^ ^[1.1](#cite_ref-handbook-functions_1-1)^] [[Gentoo Handbook, Adding Functionality](https://wiki.gentoo.org/wiki/Handbook:X86/Networking/Extending "Handbook:X86/Networking/Extending")]]