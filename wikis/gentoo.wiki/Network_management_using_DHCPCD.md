Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/Network_management_using_DHCPCD/es "Gestión de red mediante DHCPCD (29% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Network_management_using_DHCPCD/hu "Hálózati menedzsment a DHCPCD használatával (68% translated)")
-   [polski](https://wiki.gentoo.org/wiki/Network_management_using_DHCPCD/pl "Network management using DHCPCD/pl (0% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Network_management_using_DHCPCD/ru "Управление сетью с помощью DHCPCD (68% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Network_management_using_DHCPCD/zh-cn "使用DHCPCD网络管理器 (29% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Network_management_using_DHCPCD/ja "DHCPCDを使用したネットワーク管理 (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Network_management_using_DHCPCD/ko "DHCPCD로 네트워크 관리하기 (26% translated)")

This article is based on a [posting in the Gentoo Forums](https://forums.gentoo.org/viewtopic-t-965190.html) and explains how to use dhcpcd for complete network stack management.

Of course, it\'s possible to use dhcpcd together with net.\* scripts. In fact, if dhcpcd is installed, it\'s used as the default DHCP client if `config_eth0="dhcp"` is set in [/etc/conf.d/net]. This article is specifically about using dhcpcd standalone.

## Contents

-   [[1] [Setup]](#Setup)
-   [[2] [Wireless]](#Wireless)
    -   [[2.1] [wpa_supplicant]](#wpa_supplicant)
        -   [[2.1.1] [Using OpenRC]](#Using_OpenRC)
        -   [[2.1.2] [Using Systemd]](#Using_Systemd)
    -   [[2.2] [Using net-wireless/iwd]](#Using_net-wireless.2Fiwd)
-   [[3] [Testing]](#Testing)
-   [[4] [Static IP address]](#Static_IP_address)
-   [[5] [Migration from Gentoo net.\* scripts]](#Migration_from_Gentoo_net..2A_scripts)
-   [[6] [Graphical User interface]](#Graphical_User_interface)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)

## [Setup]

Make sure [dhcpcd](https://wiki.gentoo.org/wiki/Dhcpcd "Dhcpcd") is installed. Next, add it to the default runlevel and start the service.

If using [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC"), do:

`root `[`#`]`rc-update add dhcpcd default `

`root `[`#`]`rc-service dhcpcd start `

Or, if using [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd"):

`root `[`#`]`systemctl enable dhcpcd `

`root `[`#`]`systemctl start dhcpcd `

This setup deviates from the default networking instructions in the Gentoo Handbook. It has the advantage that it provides automatic switching between wired and wireless network interfaces.

## [Wireless]

### [wpa_supplicant]

[wpa_supplicant](https://wiki.gentoo.org/wiki/Wpa_supplicant "Wpa supplicant") can be used for authentication of wireless and wired network interfaces. Create the configuration file if it does not exist:

[FILE] **`/etc/wpa_supplicant/wpa_supplicant.conf`**

    # Allow users in the 'wheel' group to control wpa_supplicant
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=wheel

    # Make this file writable for wpa_gui / wpa_cli
    update_config=1

For authentication for the wired interface, add the configuration file mentioned in [Setup wired 802.1X](https://wiki.gentoo.org/wiki/Wpa_supplicant#Setup_wired_802.1X "Wpa supplicant").

First follow the setup guide for [dhcpcd](https://wiki.gentoo.org/wiki/Network_management_using_DHCPCD#Setup "Network management using DHCPCD").

Emerge [wpa_supplicant] (Version \>=2.6-r2 is needed in order to get the [CONFIG_MATCH_IFACE](https://forums.gentoo.org/viewtopic-t-1036958-start-4.html) option [added in April 2017](https://gitweb.gentoo.org/repo/gentoo.git/commit/net-wireless/wpa_supplicant?id=423af2686b225f76bb8ae52221690581a56a9625)):

`root `[`#`]`emerge --ask net-wireless/wpa_supplicant`

#### [Using [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC")]

Complete its [conf.d] file with the `-M` option for the wireless network interface:

[FILE] **`/etc/conf.d/wpa_supplicant`**

    wpa_supplicant_args="-B -M -c /etc/wpa_supplicant/wpa_supplicant.conf"

In case authentication for the [wired interface](https://wiki.gentoo.org/wiki/Wpa_supplicant#Setup_wired_802.1X "Wpa supplicant") is needed, this configuration file should look like:

[FILE] **`/etc/conf.d/wpa_supplicant`**

    wpa_supplicant_args="-ieth0 -Dwired -c/etc/wpa_supplicant/wpa_supplicant_wired.conf -B -M -c/etc/wpa_supplicant/wpa_supplicant.conf"

With the configuration done, run it as a service:

`root `[`#`]`rc-update add wpa_supplicant default`

`root `[`#`]`rc-service wpa_supplicant start`

#### [Using [Systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd")]

[Systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") allows a simpler per-device setup without needing to create the above [conf.d] files. As explained under *wpa_supplicant* item in the [Native services](https://wiki.gentoo.org/wiki/Systemd#Native_services "Systemd") section, a service symlink such as `wpa_supplicant@wlan0.service` looks for a separate configuration file to manage the device `wlan0` in this case.

To configure a specific device this way, first copy or rename the [/etc/wpa_supplicant/wpa_supplicant.conf] file as [/etc/wpa_supplicant/wpa_supplicant-DEVNAME.conf] where `DEVNAME` should be the name of the device, such as `wlan0`.

Then, navigate to [/etc/systemd/system/multi-user.target.wants] and create the symlink:

`root `[`#`]`ln -s /lib/systemd/system/wpa_supplicant@.service wpa_supplicant@DEVNAME.service`

where `DEVNAME` is *same* device name as in the conf file above.

** Important**\
Note the **@** signs on both arguments in the symlink step.

Test the system:

`root `[`#`]`systemctl daemon-reload `

`root `[`#`]`systemctl start wpa_supplicant@DEVNAME `

`root `[`#`]`systemctl status wpa_supplicant@DEVNAME `

### [][Using net-wireless/iwd]

See the [iwd](https://wiki.gentoo.org/wiki/Iwd "Iwd") article.

## [Testing]

Stop the [dhcpcd] service, then start [dhcpcd] with the -d (`--debug`) and -B (`--nobackground`) options enabled to see it starting the connection:

`root `[`#`]`rc-service dhcpcd stop `

`root `[`#`]`dhcpcd -dB `

    dhcpcd-6.11.3 starting
    dev: loaded udev
    eth0: executing `/lib/dhcpcd/dhcpcd-run-hooks' PREINIT
    eth0: executing `/lib/dhcpcd/dhcpcd-run-hooks' NOCARRIER
    wlan0: executing `/lib/dhcpcd/dhcpcd-run-hooks' PREINIT
    wlan0: executing `/lib/dhcpcd/dhcpcd-run-hooks' CARRIER
    DUID xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx
    wlan0: IAID XX:XX:XX:XX
    wlan0: delaying IPv6 router solicitation for 0.9 seconds
    wlan0: delaying IPv4 for 0.3 seconds
    eth0: waiting for carrier
    wlan0: reading lease `/var/lib/dhcpcd/dhcpcd-wlan0-.lease'
    wlan0: rebinding lease of 192.168.178.23
    wlan0: sending REQUEST (xid 0x66820be2), next in 3.3 seconds
    wlan0: acknowledged 192.168.178.23 from 192.168.178.1
    wlan0: leased 192.168.178.23 for 864000 seconds
    wlan0: renew in 432000 seconds, rebind in 756000 seconds
    wlan0: writing lease `/var/lib/dhcpcd/dhcpcd-wlan0-.lease'
    wlan0: IP address 192.168.178.23/24 already exists
    wlan0: changing route to 192.168.178.0/24
    wlan0: changing default route via 192.168.178.1
    wlan0: ARP announcing 192.168.178.23 (1 of 2), next in 2.0 seconds
    wlan0: executing `/lib/dhcpcd/dhcpcd-run-hooks' BOUND
    wlan0: soliciting an IPv6 router
    wlan0: sending Router Solicitation
    wlan0: ARP announcing 192.168.178.23 (2 of 2)

## [Static IP address]

In case the network interface card should be configured with a [static IP address](https://wiki.gentoo.org/wiki/Static_routing "Static routing"), type it into the [graphical user interface](https://wiki.gentoo.org/wiki/Dhcpcd-ui#Usage "Dhcpcd-ui"). Without the graphical user interface, entries can also be manually added to [/etc/dhcpcd.conf] as described in [Dhcpcd](https://wiki.gentoo.org/wiki/Dhcpcd#Static_IP_addresses "Dhcpcd").

## [][Migration from Gentoo net.\* scripts]

When migrating from [Gentoo\'s net.\* scripts](https://wiki.gentoo.org/wiki/Netifrc "Netifrc") it is essential to remove the [net.\*] scripts from the runlevels. To see what runlevels they are currently in:

`user `[`$`]`rc-config list | grep 'wpa_supplicant\|dhcpcd\|net\.'`

      net.wlp8s0                default
      dhcpcd                    default

Any match starting with `net.` must not have a runlevel assigned. In the above example, [net.wlp8s0] needs to be removed:

`root `[`#`]`rc-update del net.wlp8s0 `

`root `[`#`]`rc-service net.wlp8s0 stop`

## [Graphical User interface]

A [dhcpcd graphical user interface](https://wiki.gentoo.org/wiki/Dhcpcd-ui "Dhcpcd-ui") is provided by [[[net-misc/dhcpcd-ui]](https://packages.gentoo.org/packages/net-misc/dhcpcd-ui)[]].

## [See also]

-   [Dhcpcd](https://wiki.gentoo.org/wiki/Dhcpcd "Dhcpcd") --- a popular DHCP client capable of handling both IPv4 and IPv6 configuration.
-   [Dhcpcd-ui](https://wiki.gentoo.org/wiki/Dhcpcd-ui "Dhcpcd-ui") --- a Qt and GTK monitor and configuration graphical user interface for [dhcpcd](https://wiki.gentoo.org/wiki/Dhcpcd "Dhcpcd").

## [External resources]

-   [Post 93 of Gentoo Forums :: View topic - TIP: Complete network stack without net.\* scripts](https://forums.gentoo.org/viewtopic-t-965190-start-93.html)