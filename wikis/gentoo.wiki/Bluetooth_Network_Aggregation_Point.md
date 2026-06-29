This page contains [[changes](https://wiki.gentoo.org/index.php?title=Bluetooth_Network_Aggregation_Point&oldid=1020711&diff=1303848)] which are not marked for translation.

Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Bluetooth_Network_Aggregation_Point/hu "Bluetooth Hálózati Aggregációs Pont
    (Bluetooth Network Aggregation Point) (100% translated)")
-   [தமிழ்](https://wiki.gentoo.org/wiki/Bluetooth_Network_Aggregation_Point/ta "ஊடலை வலையமைப்பு திரள்வு புள்ளி (13% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Bluetooth_Network_Aggregation_Point/ja "Bluetooth ネットワークアグリゲーションポイント (100% translated)")

This article covers the setup of a Bluetooth Network Aggregation Point (NAP) on Gentoo Linux.

## Contents

-   [[1] [What is a NAP]](#What_is_a_NAP)
-   [[2] [Scope of this article]](#Scope_of_this_article)
-   [[3] [Prerequisites]](#Prerequisites)
-   [[4] [Setting up a network bridge]](#Setting_up_a_network_bridge)
-   [[5] [Connecting a cell phone to the Internet]](#Connecting_a_cell_phone_to_the_Internet)
    -   [[5.1] [Background service]](#Background_service)
-   [[6] [Troubleshooting]](#Troubleshooting)
    -   [[6.1] [BlueZ ebuild bug]](#BlueZ_ebuild_bug)
    -   [[6.2] [No webpages can be loaded]](#No_webpages_can_be_loaded)
    -   [[6.3] [Restore your old Internet connection]](#Restore_your_old_Internet_connection)
    -   [[6.4] [Tools for testing]](#Tools_for_testing)
-   [[7] [See also]](#See_also)

## [What is a NAP]

The Bluetooth specification incorporates the ability to create a Personal Area Network (PAN). It is an Ethernet transparent protocol, thus all standard protocols (especially IP) can be used in such a PAN. A NAP can be thought of being the Master in such a network. It will provide the connectivity to other networks (Internet for instance), for up to eight via Bluetooth connected PAN devices (cell phones, PDAs, laptops maybe). These devices will consume less power using Bluetooth instead of Wi-Fi.

## [Scope of this article]

We will deal with the creation of a Gentoo NAP, in order to connect a Bluetooth enabled cell phone with the Internet. Then for instance, one could synchronize the cell phone\'s contacts/calendar with a SyncML capable groupware server, located anywhere on the Internet (or the local network). We will henceforth call the NAP server \"Gentoo-Box\" and the PAN client \"cell phone\".

## [Prerequisites]

A [Bluetooth installation](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth") must be done first. If you use *simple-agent* or [bluetoothctl], no GUI programs or applets are needed. Set the \"test-programs\" USE flag on the *net-wireless/bluez* package, to get the latest *bluez-test-nap* script. We also need [Network Bridging](https://wiki.gentoo.org/wiki/Network_bridge "Network bridge"), but with our own host configuration.

## [Setting up a network bridge]

As the BlueZ NAP server relies on Gentoo to handle the Ethernet link created by BlueZ, this section will create an Ethernet bridge using [netifrc](https://wiki.gentoo.org/wiki/Netifrc "Netifrc"). Make sure to **backup all files before editing** them.

Consider the following scenario, as this is probably the easiest and most common case:

                                                           +−−−−−−−−−−+
                                 Global IP address  ┌─────>╎ Internet ╎
                                                    │      +−−−−−−−−−−+
                                                    │
                                                    v
                              ┌────────────────────────────────────────────┐
                              │                   Router                   │
                              │ (with DHCP and routing (NAT) capabilities) │
                              └────────────────────────────────────────────┘
                                             ^              ^
                                             │              │
    ┌────────────┐       ┌────────────┐      │              │      +−−−−−−−−−−−−−−−+
    │ Cell phone │<─────>│ Gentoo-Box │<─────┘              └─────>╎ Local network ╎
    └────────────┘       └────────────┘                            +−−−−−−−−−−−−−−−+
                                             Local IP address

Execute [ip addr] to locate the network card which connects to the router:

`root `[`#`]`ip addr`

    1: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
            link/ether 00:13:8f:a2:8e:76 brd ff:ff:ff:ff:ff:ff
            inet 192.168.0.2/24 brd 192.168.0.255 scope global eth0
               valid_lft forever preferred_lft forever
            inet6 fe80::00:13:8f:a2:8e:76/64 scope link
               valid_lft forever preferred_lft forever

The line \"inet 192.168.0.2/24 brd 192.168.0.255 scope global eth0\" is the one to look for.

Remember the device name (*eth0*) and edit [/etc/conf.d/net]:

[FILE] **`/etc/conf.d/net`**

    ...
    # Comment out this line, and add the following lines:
    #config_eth0="dhcp"
    config_eth0="null"
    bridge_br1="eth0"
    config_br1="dhcp"
    bridge_forward_delay_br1=100
    bridge_stp_state_br1=1
    ...

This tells netifrc to not ask for a DHCP lease on *eth0* (actually it tells netifrc to do nothing for *eth0*), and create a new bridge *br1*, which contains *eth0*. As *eth0* used to get its IP address via DHCP, *br1* is set to do exactly that. The options \"bridge_stp_state_br1=1\" and \"bridge_forward_delay_br1=100\" make sure, the Spanning Tree Protocol is used, and the forwarding state of the bridge will be reached within one second of a topology change. The last options speed up the cell phone connection considerably, as Gentoo tends to default to around 10 seconds, thus every cell phone connect would take at least that long.

Create a new symbolic link, and restart the network:

`root `[`#`]`ln -sr /etc/init.d/net.lo /etc/init.d/net.br1 `

`root `[`#`]`rc-service net.eth0 stop && rc-service net.br1 start`

    ...
     * Bringing up interface br1
     *   Creating bridge br1 ...
     *   Adding ports to br1
     *     eth0 ...                                                                                         [ ok ]
     *   192.168.0.2 ...                                                                                    [ ok ]

Verify the connection to the Internet and, if everything works well, add *br1* to the \"default\" runlevel:

`root `[`#`]`ping -c1 wiki.gentoo.org `

`root `[`#`]`rc-update add net.br1 default `

## [Connecting a cell phone to the Internet]

Start the NAP service and notice interface *br1*. Enter in a terminal:

`root `[`#`]`bluez-test-nap br1`

Watch Syslog when you tell your cell phone to connect to the Internet using the Gentoo-Box as NAP:

`root `[`#`]`tail -F /var/log/messages`

    Nov 04 17:37:38 [bluetoothd] bnep: bridge br1: interface bnep0 added
    Nov 04 17:37:38 [kernel] br1: port 2(bnep0) entered blocking state
    Nov 04 17:37:38 [kernel] br1: port 2(bnep0) entered disabled state
    Nov 04 17:37:38 [kernel] device bnep0 entered promiscuous mode
    Nov 04 17:37:38 [kernel] br1: port 2(bnep0) entered blocking state
    Nov 04 17:37:38 [kernel] br1: port 2(bnep0) entered listening state
    Nov 04 17:37:40 [kernel] br1: port 2(bnep0) entered learning state
    Nov 04 17:37:42 [kernel] br1: port 2(bnep0) entered forwarding state
    Nov 04 17:37:42 [kernel] br1: topology change detected, propagating

You should now be able to connect and load webpages.

### [Background service]

The NAP service can be started in four more ways:

-   To run the script in the background, and stop it (CTRL-C = KeyboardInterrupt = SIGINT):

`root `[`#`]`bluez-test-nap br1 >/dev/null 2>&1 & `

`root `[`#`]`killall -SIGINT bluez-test-nap `

-   To run at startup, let [[/etc/init.d/local]](https://wiki.gentoo.org/wiki/Local.d "Local.d") read next scripts. These files must be made executable:

[FILE] **`/etc/local.d/bluez-test-nap.start`**

    exec /usr/bin/bluez-test-nap br1 >/dev/null 2>&1 &

[FILE] **`/etc/local.d/bluez-test-nap.stop`**

    killall -SIGINT bluez-test-nap

`root `[`#`]`chmod +x /etc/local.d/bluez-test-nap.start /etc/local.d/bluez-test-nap.stop`

-   Instead of the local.d files approach, it\'s better to use a real [init script](https://wiki.gentoo.org/wiki/Handbook:X86/Working/Initscripts "Handbook:X86/Working/Initscripts"). This file must be made executable:

[FILE] **`/etc/init.d/nap`**

    #!/sbin/openrc-run
    # Copyright 1999-2019 Gentoo Authors
    # Distributed under the terms of the GNU General Public License v2

    command="/usr/bin/bluez-test-nap"
    command_args="br1"
    command_background="yes"
    description="Bluetooth NAP"
    pidfile="/var/run/nap.pid"
    retry="-INT/4/-TERM/1/-KILL/1"

    depend()

    start_pre()
    " ]; then
            eerror "Is $ a broken symlink?"
            eerror "Please see: https://bugs.gentoo.org/696070"
        fi
    }

`root `[`#`]`chmod +x /etc/init.d/nap`

-   In case of plugging and unplugging an USB dongle, just an [udev rule](https://wiki.gentoo.org/wiki/Udev#Rules "Udev") can do the job:

[FILE] **`/etc/udev/rules.d/90-bluetooth.rules`**

    ACTION=="add", KERNEL=="hci0", \
      RUN+="/bin/sh -c 'sleep 0.5; exec /usr/bin/bluez-test-nap br1 >/dev/null 2>&1 &'"
    ACTION=="remove", KERNEL=="hci0", \
      RUN+="/usr/bin/killall -SIGINT bluez-test-nap"
    # In case of trouble (ugly):
    #ACTION=="remove", KERNEL=="hci0", \
    #  RUN+="/bin/sh -c 'killall -INT bluez-test-nap; killall -KILL bluetoothd; rc-service bluetooth restart'"

Or:

[FILE] **`/etc/udev/rules.d/90-bluetooth.rules`**

    ACTION=="add", KERNEL=="hci0", \
      RUN+="/bin/sh -c 'sleep 0.5; rc-service nap start'"
    ACTION=="remove", KERNEL=="hci0", \
      RUN+="/bin/sh -c 'rc-service nap stop'"

## [Troubleshooting]

### [BlueZ ebuild bug]

The *bluez-test-nap* symlink points to Buildroot, and needs a fix. Please see: [[[bug #696070]](https://bugs.gentoo.org/show_bug.cgi?id=696070)[]].

`root `[`#`]`ls -al /usr/bin/bluez-test-nap`\
`lrwxr-xr-x 1 root root 80 Jun 18 12:53 /usr/bin/bluez-test-nap -> /var/tmp/portage/net-wireless/bluez-5.76-r1/image/usr/lib64/bluez/test/test-nap `

`root `[`#`]`ln -sf /usr/lib64/bluez/test/test-nap /usr/bin/bluez-test-nap `

`root `[`#`]`ls -al /usr/bin/bluez-test-nap`\
`lrwxr-xr-x 1 root root 31 Jul 2 12:50 /usr/bin/bluez-test-nap -> /usr/lib64/bluez/test/test-nap`

### [No webpages can be loaded]

If the phone does not show any sign of being connected, try [Wireshark](https://wiki.gentoo.org/wiki/Wireshark "Wireshark") to figure out what packets are being sent and received. Maybe a simple

`root `[`#`]`echo 1 > /proc/sys/net/ipv4/ip_forward`

can do the trick. Make sure no firewall settings on the Gentoo-Box interfere.

### [Restore your old Internet connection]

If you lose your Internet connectivity, if things break, restore your backup of [/etc/conf.d/net] and restart networking:

[FILE] **`/etc/conf.d/net`**

    (old file)

`root `[`#`]`rc-service net.eth0 restart`

### [Tools for testing]

There is a *bluez-test-network* utility, that you can use for testing PAN connection initiated from server side, and a *monitor-bluetooth* utility to watch what is going behind the [D-Bus](https://wiki.gentoo.org/wiki/D-Bus "D-Bus") scene, because watching [/var/log/messages] can be not enough.

## [See also]

-   [Bluetooth](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth") --- describes the configuration and usage of Bluetooth controllers and devices.