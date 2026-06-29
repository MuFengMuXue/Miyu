[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=PPTP&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](http://pptpclient.sourceforge.net/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Point-to-Point_Tunneling_Protocol "wikipedia:Point-to-Point Tunneling Protocol")

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/pptpclient)

** Warning**\
PPTP has many security vulnerabilities and is considered obsolete. Retaining for anyone who still needs this.

The Point-to-Point Tunneling Protocol (**PPTP**) is a method for creating virtual private networks. PPTP allows the [Point-to-Point Protocol](https://en.wikipedia.org/wiki/Point-to-Point_Protocol "wikipedia:Point-to-Point Protocol") (PPP) to be tunneled through an IP network on TCP port 1723.

## [Client]

[KERNEL] **Enabling TUN/TAP device driver support**

    Device Drivers --->
      [*] Network device support --->
            [*]   Network core driver support
            <*>     Universal TUN/TAP device driver support

## [Server]

[KERNEL] **Enabling TUN/TAP device driver support**

    Device Drivers --->
      [*] Network device support --->
            [*]   Network core driver support
            <*>     Universal TUN/TAP device driver support

[KERNEL] **Enabling PPP support**

    Device Drivers --->
      [*] Network device support --->
            <M>   PPP (point-to-point protocol) support
            <M>     PPP BSD-Compress compression
            <M>     PPP Deflate compression
            [*]     PPP filtering
            <M>     PPP MPPE compression (encryption)
            <M>     PPP over Ethernet
            <M>     PPP support for async serial ports
            <M>     PPP support for sync tty ports

## [External resources]

-   [https://wiki.archlinux.org/index.php/PPTP_VPN_client_setup_with_pptpclient](https://wiki.archlinux.org/index.php/PPTP_VPN_client_setup_with_pptpclient)
-   [https://wiki.archlinux.org/index.php/PPTP_Server](https://wiki.archlinux.org/index.php/PPTP_Server)