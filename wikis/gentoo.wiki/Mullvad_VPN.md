**Resources**

[[]][Home](https://mullvad.net/en)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Mullvad_VPN "wikipedia:Mullvad VPN")

[[]][GitHub](https://github.com/mullvad/mullvadvpn-app)

**Mullvad VPN** is a no-log, open-source VPN.

## Contents

-   [[1] [Requirements]](#Requirements)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Netfilter]](#Netfilter)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Emerge]](#Emerge)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Enabling the service]](#Enabling_the_service)
        -   [[3.1.1] [OpenRC]](#OpenRC)
        -   [[3.1.2] [systemd]](#systemd)
    -   [[3.2] [Starting the client]](#Starting_the_client)

## [Requirements]

Notice: this section is currently WIP.

### [Kernel]

-   [Wireguard](https://wiki.gentoo.org/wiki/Wireguard "Wireguard") (CONFIG_WIREGUARD)
-   netfilter, [nftables](https://wiki.gentoo.org/wiki/Nftables "Nftables")
-   CAN, Netlink?

### [Netfilter]

\"mullvad\" netfilter table must be set

## [Installation]

Mullvad is available on the [GURU](https://wiki.gentoo.org/wiki/Project:GURU/Information_for_End_Users "Project:GURU/Information for End Users"). Please follow those steps to enable the GURU if it is not already enabled.

### [Emerge]

`root `[`#`]`emerge --ask net-vpn/mullvadvpn-app`

## [Usage]

### [Enabling the service]

Installing Mullvad provides both a [daemon](https://wiki.gentoo.org/index.php?title=Daemon&action=edit&redlink=1 "Daemon (page does not exist)") and the app (client) itself. In order to use Mullvad, first enable the daemon, and then start the app.

#### [OpenRC]

`root `[`#`]`rc-update add mullvad-daemon default`

`root `[`#`]`rc-service mullvad-daemon start`

#### [systemd]

`root `[`#`]`systemctl enable mullvad-daemon`

`root `[`#`]`systemctl start mullvad-daemon`

### [Starting the client]

Run the installed client using the `mullvad-vpn` command:

`user `[`$`]`mullvad-vpn`