**Resources**

[[]][Home](https://iwd.wiki.kernel.org/)

[[]][Package information](https://packages.gentoo.org/packages/net-wireless/iwd)

[[]][iwd(8) manpage](http://man7.org/linux/man-pages/https://manpages.debian.org/bookworm/iwd/iwd.8.en.html.html)

[[]][GitWeb](https://git.kernel.org/pub/scm/network/wireless/iwd.git/)

[[]][[#iwd](ircs://irc.libera.chat/#iwd)] ([[webchat](https://web.libera.chat/#iwd)])

**iwd** (**i**Net **W**ireless **D**aemon) is a wireless daemon intended to replace wpa_supplicant, written by [Intel](https://wiki.gentoo.org/wiki/Category:Intel "Category:Intel").

Potential benefits of iwd over [[wpa_supplicant]](https://wiki.gentoo.org/wiki/Wpa_supplicant "Wpa supplicant") include:

-   simplification of network management
-   faster network discovery
-   fast and reliable roaming
-   using less system resources
-   using features offered by the Linux kernel
-   support for enterprise security methods like EAP
-   support for kernel asymmetric key rings and [Trusted Platform Modules](https://wiki.gentoo.org/wiki/Trusted_Boot#Trusted_Platform_Module "Trusted Boot") (TPM)
-   support for multiple clients

## Contents

-   [[1] [Background]](#Background)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
    -   [[2.2] [USE flags]](#USE_flags)
    -   [[2.3] [Emerge]](#Emerge)
-   [[3] [Interface management]](#Interface_management)
-   [[4] [Iwd daemon configuration]](#Iwd_daemon_configuration)
-   [[5] [Starting and stopping the iwd service]](#Starting_and_stopping_the_iwd_service)
    -   [[5.1] [OpenRC]](#OpenRC)
    -   [[5.2] [Systemd]](#Systemd)
-   [[6] [Network management]](#Network_management)
    -   [[6.1] [Netifrc]](#Netifrc)
    -   [[6.2] [iwd native]](#iwd_native)
    -   [[6.3] [dhcpcd]](#dhcpcd)
    -   [[6.4] [NetworkManager]](#NetworkManager)
    -   [[6.5] [ConnMan]](#ConnMan)
    -   [[6.6] [systemd-networkd]](#systemd-networkd)
-   [[7] [Client software]](#Client_software)
    -   [[7.1] [Iwctl]](#Iwctl)
    -   [[7.2] [NetworkManager frontends]](#NetworkManager_frontends)
    -   [[7.3] [Dedicated iwd clients]](#Dedicated_iwd_clients)
-   [[8] [Configuration per connection]](#Configuration_per_connection)
    -   [[8.1] [Security]](#Security)
    -   [[8.2] [Static network configuration]](#Static_network_configuration)
-   [[9] [See also]](#See_also)
-   [[10] [External resources]](#External_resources)
    -   [[10.1] [Man pages]](#Man_pages)
    -   [[10.2] [General]](#General)
-   [[11] [References]](#References)

## [Background]

*For details readers are referred to the LWN article \"[iwd: simplifying WiFi management](https://lwn.net/Articles/770991/)\" in 2018 by Jonathan Corbet.*

Why does iwd have to replace wpa_supplicant? In fact users can continue to use wpa_supplicant if they are satisfied.

For developers however wpa_supplicant is bad. It was the first software for Wifi authentication, and in the end it became too big and too complicated. Although it came to have many problems, it became difficult to fix them. Very few releases have been made since the version 2.0 in 2013.

Then the community decided to write a new software from scratch, and it is iwd.

## [Installation]

### [Kernel]

General instructions for [WiFi](https://wiki.gentoo.org/wiki/Wifi "Wifi") apply, including the required device drivers and [IEEE 802.11](https://en.wikipedia.org/wiki/IEEE_802.11 "wikipedia:IEEE 802.11") support.

In addition iwd requires the Linux kernel to have quite some options to be enabled. For systems running on a [AMD64](https://wiki.gentoo.org/wiki/AMD64 "AMD64") architecture, or CPUs that support [SSSE3](https://en.wikipedia.org/wiki/SSSE3 "wikipedia:SSSE3") or [X86_AES](https://en.wikipedia.org/wiki/AES_instruction_set "wikipedia:AES instruction set") instructions some hardware acceleration can be achieved. The [[cpuid2cpuflags]](https://wiki.gentoo.org/wiki/CPU_FLAGS_X86 "CPU FLAGS X86") utility can be used to check for support.

[KERNEL]

    Security options  --->
        [*] Enable access key retention support
        [*] Diffie-Hellman operations on retained keys
    Networking support  --->
        [*] Wireless  --->
            <M> cfg80211 - wireless configuration API
    Cryptographic API  --->
        Public-key cryptography  --->
            [*] RSA (Rivest-Shamir-Adleman)
            [*] DH (Diffie-Hellman)
        Block ciphers  --->
            [*] AES (Advanced Encryption Standard)
            [*] AES (Advanced Encryption Standard) (fixed time)
            [*] DES and Triple DES EDE
        Length-preserving ciphers and modes  --->
            [*] ARC4 (Alleged Rivest Cipher 4)
            [*] ECB (Electronic Codebook)
        Hashes, digests and MACs  --->
            [*] HMAC (Keyed-Hash MAC)
            [*] MD4
            [*] MD5
            [*] SHA-1
            [*] SHA-224 and SHA-256
            [*] SHA-384 and SHA-512
         Accelerated Cryptographic Algorithms for CPU (x86)  --->
            [*] Ciphers: AES, modes: ECB, CBC, CTS, CTR, XTR, XTS, GCM (AES-NI)               // X86_AES
            [*] Ciphers: Triple DES EDE with modes: ECB, CBC                                  // AMD64
            [*] Hash functions: SHA-1 (SSSE3/AVX/AVX2/SHA-NI)                                 // AMD64 and SSSE3
            [*] Hash functions: SHA-224 and SHA-256 (SSSE3/AVX/AVX2/SHA-NI)                   // AMD64 and SSSE3
            [*] Hash functions: SHA-384 and SHA-512 (SSSE3/AVX/AVX2/SHA-NI)                   // AMD64 and SSSE3
         Userspace interface  --->
            [*] Hash algorithms
            [*] Symmetric key cipher algorithms
         [*] Asymmetric (public-key cryptographic) key type  --->
            [*] Asymmetric public-key crypto algorithm subtype
            [*] X.509 certificate parser
            [*] PKCS#8 private key parser                                                     // Linux kernel 4.20 or higher
            [*] PKCS#7 message parser

### [USE flags]

Some packages are aware of the [[[iwd]](https://packages.gentoo.org/useflags/iwd)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag").

### [USE flags for] [net-wireless/iwd](https://packages.gentoo.org/packages/net-wireless/iwd) [[]] [Wireless daemon for linux]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`+client`](https://packages.gentoo.org/useflags/+client)         Enable iwctl client tool
  [`+monitor`](https://packages.gentoo.org/useflags/+monitor)       Enable iwmon monitor tool
  [`ofono`](https://packages.gentoo.org/useflags/ofono)             Enable support for oFono SIM authentication
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`standalone`](https://packages.gentoo.org/useflags/standalone)   Enable standalone mode with built-in DHCP client and DNS handling\"
  [`systemd`](https://packages.gentoo.org/useflags/systemd)         Use systemd-resolve rather than resolvconf for DNS handling in standalone mode
  [`wired`](https://packages.gentoo.org/useflags/wired)             Enable ethernet authentication daemon
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-13 18:50] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install the [[[net-wireless/iwd]](https://packages.gentoo.org/packages/net-wireless/iwd)[]] package:

`root `[`#`]`emerge --ask net-wireless/iwd`

## [Interface management]

On iwd startup it may destroy an existing network interface and create a new one. For example iwd might rename the interface `wlp2s0` to `wlan0`. (The former is typically created by [udev](https://wiki.gentoo.org/wiki/Udev "Udev").) When iwd terminates, it destroys the wireless interface it created. (It does not necessarily mean the original name is restored.) The newly created interface will be configured optimally for iwd\'s use.

It is possible to suppress this behavior by:

-   passing commandline options [-p] (+the the name of the phy) and [-i] (+ the name of the interface) to the iwd daemon, or
-   configuring setting `[DriverQuirks].DefaultInterface` to a comma-seperated list of drivers or glob matches in [/etc/iwd/main.conf]

It may also be necessary to prevent udev from [renaming the interface](https://wiki.gentoo.org/wiki/Udev#Optional:_Disable_or_override_predictable_network_interface_naming "Udev").

In the remainder of this article, it is assumed that the wireless interface is named `wlan0`.

## [Iwd daemon configuration]

Iwd keeps its main configuration file in [/etc/iwd/main.conf]. It is documented in the official [manual page](//git.kernel.org/pub/scm/network/wireless/iwd.git/tree/src/iwd.config.rst).

** Note**\
iwd has updated its configuration file syntax. Previous settings like `enable_network_configuration` are now obsolete and replaced by `EnableNetworkConfiguration`.

## [Starting and stopping the iwd service]

### [OpenRC]

** Note**\
[NetworkManager](https://wiki.gentoo.org/wiki/NetworkManager "NetworkManager") takes care of starting the process for iwd. If the iwd service is started, it will gracefully crash.

Please make sure that [wpa_supplicant] is stopped prior to starting iwd:

`root `[`#`]`rc-update delete wpa_supplicant `

`root `[`#`]`rc-service wpa_supplicant stop `

Then start iwd, and add it to the default runlevel:

`root `[`#`]`rc-update add iwd default `

`root `[`#`]`rc-service iwd start `

### [Systemd]

** Note**\
[NetworkManager](https://wiki.gentoo.org/wiki/NetworkManager "NetworkManager") is able to use [D-Bus](https://wiki.gentoo.org/wiki/D-Bus "D-Bus") to start the iwd service when needed. Therefore the service doesn\'t need to be enabled explicitly.

Any active [wpa_supplicant] services should be stopped prior to starting the iwd service:

`root `[`#`]`systemctl disable --now wpa_supplicant`

The iwd service can be started as per:

`root `[`#`]`systemctl enable --now iwd`

## [Network management]

Be sure to heed the warning in the [network management](https://wiki.gentoo.org/wiki/Network_management#Available_software "Network management") article about mixing and matching the different methods for network management.

### [Netifrc]

[netifrc](https://wiki.gentoo.org/wiki/Netifrc "Netifrc") is Gentoo\'s default method of managing networks. It doesn\'t officially support iwd as a backend yet, but it works, barring minor issues, see [[[bug #690808]](https://bugs.gentoo.org/show_bug.cgi?id=690808)[]].

Enable iwd by editing [/etc/conf.d/net] file:

[FILE] **`/etc/conf.d/net`**

    modules_phy0="iwd debug"
    modules_wlan0="iwd debug"
    iwd_wlan0="phy0 debug"
    config_wlan0="dhcp"

The debug parameters help to resolve the minor issues. When strange behavior is observed then please comment on [[[bug #690808]](https://bugs.gentoo.org/show_bug.cgi?id=690808)[]] and upload the syslog.

Netifrc will start iwd as needed, so no need for the iwd daemon to be started by [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC"), instead create a symlink from [/etc/init.d/net.wlan0] to [/etc/init.d/net.lo], and start the `net.wlan0` service:

`root `[`#`]`rc-service iwd stop `

`root `[`#`]`rc-update delete iwd `

`root `[`#`]`cd /etc/init.d `

`root `[`#`]`ln -s net.lo net.wlan0 `

`root `[`#`]`rc-service net.wlan0 start `

### [iwd native]

iwd contains a DHCP client and can manage routes and DNS resolving. If the `standalone` USE flag is not set, the following manual configuration is necessary; edit [/etc/iwd/main.conf] as follows:

[FILE] **`/etc/iwd/main.conf`**

    [General]
    EnableNetworkConfiguration=true
    [Network]
    RoutePriorityOffset=200
    NameResolvingService=resolvconf

Where:

-   `EnableNetworkConfiguration` is required to activate the native network management
-   `RoutePriorityOffset` is optional and sets the route metric
-   `NameResolvingService` is used to configure a DNS manager and can be set to \'[resolvconf](https://wiki.gentoo.org/wiki/Resolv.conf "Resolv.conf")\' (from [[[net-dns/openresolv]](https://packages.gentoo.org/packages/net-dns/openresolv)[]]), \'systemd\' or \'none\'. Configuring this may be necessary for DNS resolution when connecting to public networks.

### [dhcpcd]

Add [dhcpcd](https://wiki.gentoo.org/wiki/Network_management_using_DHCPCD "Network management using DHCPCD") to the default runlevel and start it up, next to the iwd service:

`root `[`#`]`rc-update add dhcpcd default `

`root `[`#`]`rc-service dhcpcd start `

### [NetworkManager]

[NetworkManager](https://wiki.gentoo.org/wiki/NetworkManager "NetworkManager") has supported the iwd backend since version 1.12. Verify the `iwd` USE flag is set:

`root `[`#`]`echo "net-misc/networkmanager iwd" >> /etc/portage/package.use/networkmanager`

`root `[`#`]`emerge --ask --newuse net-misc/networkmanager`

Enable the iwd backend for WiFi devices as per upstream\'s instructions^[\[1\]](#cite_note-1)^:

[FILE] **`/etc/NetworkManager/conf.d/iwd.conf`**

    [device]
    wifi.backend=iwd

Starting with NetworkManager 1.30 it is possible to enable iwd-driven autoconnect logic instead of NetworkManager\'s.

[FILE] **`/etc/NetworkManager/conf.d/iwd.conf`**

    [device]
    wifi.backend=iwd
    wifi.iwd.autoconnect=yes

Restart the NetworkManager service:

For OpenRC:

`root `[`#`]`rc-service NetworkManager restart`

For systemd:

`root `[`#`]`systemctl restart NetworkManager`

### [ConnMan]

[ConnMan](https://wiki.gentoo.org/wiki/Connman "Connman") supports iwd somewhat. Make sure to set the `iwd` USE flag and (re-)emerge:

`root `[`#`]`echo "net-misc/connman iwd" >> /etc/portage/package.use/zz-autounmask`

`root `[`#`]`emerge --ask --newuse net-misc/connman`

ConnMan still relies on [wpa_supplicant] for scanning, but connecting via iwd is possible.

### [systemd-networkd]

[systemd-networkd](https://wiki.gentoo.org/wiki/Systemd#systemd-networkd "Systemd") will handle iwd-managed interfaces just like any other network interface. Add a `.network` file and start or restart the service:

[FILE] **`/etc/systemd/network/wlan0.network`**

    [Match]
    Name=wlan0

    [Network]
    DHCP=yes
    IgnoreCarrierLoss=3s

`root `[`#`]`systemctl enable --now systemd-networkd `

`root `[`#`]`systemctl enable --now systemd-resolved`

## [Client software]

Iwd comes with a commandline interface called [iwctl] when [[[client]](https://packages.gentoo.org/useflags/client)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag enabled.

There are also a few graphical user interface based applications. These frontends communicate with iwd over D-Bus, and will not work with iwd versions without D-Bus.

### [Iwctl]

[iwctl] is iwd\'s tool to control iwd. It supports both a command line interface and an interactive mode. A complete command line would be [iwctl station list] to see what adapters you might be able to use:

`user `[`$`]`iwctl station list`

                                Devices in Station Mode
    --------------------------------------------------------------------------------
      Name                State          Scanning
    --------------------------------------------------------------------------------
      wlan0               disconnected

An interactive session of [iwctl] commands can be used to connect to a WiFi network access point. First check the status of the WiFi network interface, set it in scanning mode if needed, and then obtain the list of WiFi access points. Finally connect to the access point.

`user `[`$`]`iwctl`

    # station wlan0 show
                                     Station: wlan0
    --------------------------------------------------------------------------------
      Settable  Property            Value
    --------------------------------------------------------------------------------
                Scanning            no
                State               disconnected

    # station wlan0 scan
    # station wlan0 get-networks
                                   Available networks
    --------------------------------------------------------------------------------
        Network name                    Security  Signal
    --------------------------------------------------------------------------------
        FRITZ!Box 7362 SL               psk       ***
        WLAN-105127                     psk       *

    # station wlan0 connect "FRITZ!Box 7362 SL"
    Type the network passphrase for FRITZ!Box 7362 SL psk.
    Passphrase:

That last step would auto-generate the [/var/lib/iwd/\<station\>.\] files.

Note that it is not possible to assign a priority to a network, instead iwd will prioritize networks based on:

-   signal strength level
-   security features
-   maximum rate
-   channel utilization
-   time since the last connect.

### [NetworkManager frontends]

When using NetworkManager then [[[gnome-extra/nm-applet]](https://packages.gentoo.org/packages/gnome-extra/nm-applet)[]] or other [NetworkManager frontends](https://en.wikipedia.org/wiki/NetworkManager#Graphical_front-ends_and_command_line_interfaces) can be used as per normal to make connections.

### [Dedicated iwd clients]

-   [[[net-wireless/iwgtk]](https://packages.gentoo.org/packages/net-wireless/iwgtk)[]]: offering similar functionality as iwctl.
-   [[[net-wireless/iwmenu::guru]](https://github.com/gentoo-mirror/guru/tree/master/net-wireless/iwmenu)[]]: [iwmenu](https://github.com/e-tho/iwmenu) manages Wi-Fi through your launcher of choice.

## [Configuration per connection]

Connection settings can be edited manually if required. Iwd keeps its configuration file per connection in [/var/lib/iwd/].

This directory contains files named like *\<station\>.\<networktype\>*, where:

-   *station* is the name (SSID) of the network
-   *networktype* can be:
    -   `psk` for pre-shared key, like WPA-PSK or WPA2-PSK
    -   `8021x` for WPA-Enterprise, like EAP-PWD or EAP-PEAP.

The configuration settings are described in [iwd.network](https://man.archlinux.org/man/iwd.config.5). A few examples are given below.

### [Security]

For WPA authentication the contents of the file looks like this:

[FILE] **`/var/lib/iwd/my-station-a.psk`**

    [Security]
    Passphrase=<human readable password>
    # The next line is automatically created by iwd.
    PreSharedKey=924179acd138039828674bb2339a4a2c95cce4a41deb934d99c00380d0be8490

`Passphrase` in case of WPA2-PSK needs to be the same as is set in the router and is known from [wpa_supplicant\'s psk=](https://wiki.gentoo.org/wiki/Wpa_supplicant#WPA2_with_wpa_supplicant "Wpa supplicant") entries. There is no need to set `PreSharedKey` manually; it will be calculated and added to the configuration file automatically by iwd.

### [Static network configuration]

Iwd defaults to DHCP, either [natively](#iwd_native) or using an external DHCP-client. For static IPv4 configuration add something like this to [/var/lib/iwd/station.psk]:

[FILE] **`/var/lib/iwd/station.psk`**

    [IPv4]
    Address=192.168.1.100
    Netmask=255.255.255.0
    Gateway=192.168.1.1
    Broadcast=192.168.1.255
    DNS=192.168.1.1

## [See also]

-   [Wifi](https://wiki.gentoo.org/wiki/Wifi "Wifi") --- describes the setup of a [Wi-Fi](https://en.wikipedia.org/wiki/Wi-Fi "wikipedia:Wi-Fi") (wireless) network device.
-   [Wpa_supplicant](https://wiki.gentoo.org/wiki/Wpa_supplicant "Wpa supplicant") --- an app for [Wi-Fi](https://wiki.gentoo.org/wiki/Wi-Fi "Wi-Fi") authentication

## [External resources]

### [Man pages]

-   [[[iwd(8)]](https://man.archlinux.org/man/iwd.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
-   [[[iwd.ap(5)]](https://man.archlinux.org/man/iwd.ap.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
-   [[[iwd.config(5)]](https://man.archlinux.org/man/iwd.config.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
-   [[[iwd.network(5)]](https://man.archlinux.org/man/iwd.network.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
-   [[[iwctl(1)]](https://man.archlinux.org/man/iwctl.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
-   [[[iwmon(1)]](https://man.archlinux.org/man/iwmon.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
-   [[[iwd.debug(7)]](https://man.archlinux.org/man/iwd.debug.7.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]

### [General]

-   [Getting Started with iwd](https://iwd.wiki.kernel.org/gettingstarted) - Official upstream introduction
-   [Iwd](https://wiki.archlinux.org/index.php/Iwd) - Archlinux wiki article
-   [eiwd](https://github.com/illiliti/eiwd) - Unofficial iwd without D-Bus; fork of dylanaraps/eiwd, which was abandoned in 2020

## [References]

1.  [[[↑](#cite_ref-1)] [IWD Wiki, [Using IWD with Network Manager](https://iwd.wiki.kernel.org/networkmanager)]]