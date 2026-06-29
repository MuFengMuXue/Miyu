**Resources**

[[]][Home](https://nordvpn.com)

[[]][Wikipedia](https://en.wikipedia.org/wiki/NordVPN "wikipedia:NordVPN")

[[]][GitLab](https://gitlab.com/lahouari.dc)

** Note**\
This wiki article has unofficial overlays and might have errors

## Contents

-   [[1] [Disclaimer]](#Disclaimer)
-   [[2] [What is a VPN]](#What_is_a_VPN)
-   [[3] [NordVPN]](#NordVPN)
-   [[4] [Account]](#Account)
-   [[5] [Installation]](#Installation)
    -   [[5.1] [Adding the overlay]](#Adding_the_overlay)
        -   [[5.1.1] [Layman]](#Layman)
        -   [[5.1.2] [Eselect-repository]](#Eselect-repository)
        -   [[5.1.3] [Manual]](#Manual)
    -   [[5.2] [Install NordVPN]](#Install_NordVPN)
        -   [[5.2.1] [Masked Issue]](#Masked_Issue)
-   [[6] [Groups]](#Groups)
-   [[7] [Starting and Enabling]](#Starting_and_Enabling)
    -   [[7.1] [OpenRC]](#OpenRC)
    -   [[7.2] [SystemD]](#SystemD)
-   [[8] [Configuration]](#Configuration)
    -   [[8.1] [Login]](#Login)
    -   [[8.2] [Connect]](#Connect)
    -   [[8.3] [NordLynx]](#NordLynx)
    -   [[8.4] [Double Vpn]](#Double_Vpn)
    -   [[8.5] [Obfuscate]](#Obfuscate)
    -   [[8.6] [OpenVPN]](#OpenVPN)
        -   [[8.6.1] [TCP]](#TCP)
        -   [[8.6.2] [UDP]](#UDP)
-   [[9] [See Also]](#See_Also)
-   [[10] [External Resources]](#External_Resources)
-   [[11] [Known Issues]](#Known_Issues)

## [Disclaimer]

This tutorial can have errors and contains packages that are not from the main Gentoo packages hence the title is User:Jeff132312342q4323/NordVPN and not NordVPN with that continue onwards with your own caution.

Also just cause it has a username does not mean you cannot edit it (please do fix the mistakes and add information for eselect-repository and etc.) but just that it is not an official package yet.

With that lets go

## [What is a VPN]

A VPN is a virtual private network that enables you to have a secure connection between your device and the internet you are connected to. This is through a VPN / all your data is routed through an encrypted tunnel. This hides your true IP address when accessing the internet. Most VPNs are used by people for a plethora of reasons including but not limited to using restricted services in their country, privacy and etc.

## [NordVPN]

NordVPN is a proprietary VPN provider. NordVPN operates in Panama as the country has no mandatory data retention laws. Furthermore, It does not participate in Fourteen Eyes or Five Eyes alliances. Checkout out the [Wikipedia page](https://en.wikipedia.org/wiki/NordVPN) for more detailed information. On Linux, it is a terminal / command-line-based tool.

## [Account]

NordVPN requires a paid account to access and use its VPN service. To make an account go to the [NordVPN\'s Website](https://nordvpn.com).

## [Installation]

To install NordVPN as it is not in the official Gentoo repository you must use/add the nordvpn overlay but if you would like an older version check out all the overlays on the [Gentoo Portage Overlays website](https://gpo.zugaina.org/net-vpn/nordvpn).

### [Adding the overlay]

#### [Layman]

To start using layman first install it by doing

`root `[`#`]`emerge -a layman`

and then update the overlays existing on your Gentoo box by doing

`root `[`#`]`layman -S`

and then to install the nordvpn overlay type in

`root `[`#`]`layman -a nordvpn `

    * Adding overlay...

\* Overlay \"nordvpn\" is not official. Continue installing? \[y/n\]: y

and then it will display some text and add the overlay.

This unofficial overlay is [here](https://gitlab.com/lahouari.dc/nordvpn) so any issues you face that others might also face it is best to make an issue [here](https://gitlab.com/lahouari.dc/nordvpn)

**as of 2022 jan this method does not work please use manual method or the eselect-repository add method**

#### [Eselect-repository]

As of oct 2025, Layman has been substitute with eselect-repository. Make sure that the package [[[app-eselect/eselect-repository]](https://packages.gentoo.org/packages/app-eselect/eselect-repository)[]] is installed with the `git` flag and add the overlay as a repository with the command

`root `[`#`]`eselect repository add nordvpn git `[`https://gitlab.com/lahouari.dc/nordvpn`](https://gitlab.com/lahouari.dc/nordvpn)

This will add the unofficial overlay to the repository list, as shown by the command

`root `[`#`]`eselect repository list `

\...

     [NNN] nordvpn # (https://gitlab.com/lahouari.dc/nordvpn/)

\...

Before using [emerge] to install NordVPN, it is necessary to synchronize the new repo with

`root `[`#`]`emaint -r nordvpn sync`

who will synchronize the newly added repository, or with

`root `[`#`]`emaint --auto sync`

who will synchronize all the repositories added to the system.

#### [Manual]

go to `/var/db/repos`

`user `[`$`]` git clone `[`https://gitlab.com/lahouari.dc/nordvpn.git`](https://gitlab.com/lahouari.dc/nordvpn.git)

then go to `/etc/portage/repos.conf`

then make and edit `nordvpn.conf`

and add the following lines

\

[FILE] **`/etc/portage/repos.conf/nordvpn.conf`FileBox example**

    [nordvpn]
    location = /var/db/repos/nordvpn

### [Install NordVPN]

you can install the NordVPN package by using the following command

`root `[`#`]`emerge -a net-vpn/nordvpn`

and then type yes to install it

#### [Masked Issue]

If you have an issue that says it is masked you can do

`root `[`#`]`emerge -a net-vpn/nordvpn --autounmask`

then type yes and then do

`root `[`#`]`dispatch-conf`

and then type \"u\" when asked after which you type the previous command

`root `[`#`]`emerge -a net-vpn/nordvpn --autounmask`

and press yes to install NordVPN

## [Groups]

You have to add the user to the nordvpn group which you can do by using this command (replace \"username\" to your username)

`root `[`#`]`usermod -a -G nordvpn "username"`

## [Starting and Enabling]

### [OpenRC]

you have to start the nordvpn service and enable it with the following commands

`root `[`#`]`rc-service nordvpn start`

`root `[`#`]`rc-update add nordvpn default`

### [SystemD]

you have to start the nordvpn service and enable it with the following commands

`root `[`#`]`systemctl start nordvpnd.service`

`root `[`#`]`systemctl enable nordvpnd.service`

## [Configuration]

### [Login]

type in

`user `[`$`]`nordvpn login`

and then type in your email and password

### [Connect]

to connect to a random server type in

`user `[`$`]`nordvpn connect`

### [NordLynx]

to use the NordLynx type in

`user `[`$`]`nordvpn set technology nordlynx`

### [Double Vpn]

to use Double Vpn type in

`user `[`$`]`nordvpn connect Double_VPN`

### [Obfuscate]

to use obfuscate type in

`user `[`$`]`nordvpn set obfuscate on`

### [OpenVPN]

to use openvpn type this for openvpn

`user `[`$`]`nordvpn set openvpn on`

#### [TCP]

type in this for TCP (only for OpenVPN users)

`user `[`$`]`nordvpn set protocol tcp`

#### [UDP]

type in this for UDP (only for OpenVPN users)

`user `[`$`]`nordvpn set protocol udp`

## [See Also]

-   [OpenVPN](https://wiki.gentoo.org/wiki/OpenVPN "OpenVPN")

## [External Resources]

-   [nordvpn.com](https://nordvpn.com)
-   [Wikipedia - VPN](https://en.wikipedia.org/wiki/Virtual_private_network)

## [Known Issues]

Currently, after some testing, OpenVPN protocol does not work yet. But good news NordLynx does so considering using it for the time being.