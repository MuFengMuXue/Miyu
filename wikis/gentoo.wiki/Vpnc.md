Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/Vpnc/es "Vpnc (15% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Vpnc/hu "Vpnc (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Vpnc/ru "Vpnc (35% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Vpnc/zh-cn "Vpnc (12% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Vpnc/ja "vpnc (31% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Vpnc/ko "Vpnc/ko (11% translated)")

[[]][Home](https://davidepucci.it/doc/vpnc/)

[[]][Package information](https://packages.gentoo.org/packages/net-vpn/vpnc)

[[]][GitHub](https://github.com/streambinder/vpnc)

[[]][Bugs (upstream)](https://github.com/streambinder/vpnc/issues)

**VPNC** is a IPsec (Cisco/Juniper) VPN concentrator client to manage secure connections, for users needing to connect to office network from home or during travel. Connecting to a Cisco and Juniper VPN concentrator is possible using Linux, and it should be possible setup a working tunnel using a Gentoo workstation or laptop.

VPNC is a VPN client compatible with Cisco\'s EasyVPN equipment. It supports IPSec (ESP) with Mode Configuration and Xauth. Supports only shared-secret IPSec authentication with: *Xauth, AES (256, 192, 128), 3DES, 1DES, MD5, SHA1, DH1/2/5 and IP tunneling*. VPNC runs entirely in userspace. Only *universal TUN/TAP device driver support* is needed in kernel.

## Contents

-   [[1] [About this guide]](#About_this_guide)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
    -   [[2.2] [Emerge]](#Emerge)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Environment variables]](#Environment_variables)
    -   [[3.2] [Files]](#Files)
        -   [[3.2.1] [Windows profile .pcf]](#Windows_profile_.pcf)
    -   [[3.3] [Service]](#Service)
        -   [[3.3.1] [OpenRC]](#OpenRC)
        -   [[3.3.2] [runit]](#runit)
        -   [[3.3.3] [systemd]](#systemd)
-   [[4] [Usage]](#Usage)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Configuration debugging]](#Configuration_debugging)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [About this guide]

This guide describes basic workings of vpnc client. It includes handling IP routing and DNS configuration. The connection terminates on a vendor specific IPSec concentrator Cisco/Juniper.

## [Installation]

### [Kernel]

In order for Linux to be able to open a VPN connection *Universal TUN/TAP device driver support* must be enabled in the kernel. What is it and why is it needed? Below is a relatively straight forward explanation from the kernel configuration dialog:

To verify that the kernel has TUN/TAP support, [grep] the kernel\'s configuration file:

`root `[`#`]`grep TUN= /usr/src/linux/.config`

    CONFIG_TUN=m

As can be seen above, `CONFIG_TUN=m` is compiled as a module. If it is disabled in the setup, enable it in the kernel of choice, rebuild, install, reboot and return to this document before continuing with the next steps.

[KERNEL] **Configuration location in the kernel configuration dialog**

    Device Drivers  --->
        [*] Network device support  --->
            [*] Network core driver support
            <*>   Universal TUN/TAP device driver support

If TUN/TAP support is built directly into the kernel, [dmesg] output should look like the following:

`root `[`#`]`dmesg | grep TUN`

    [    1.027934] tun: Universal TUN/TAP device driver, 1.6

### [Emerge]

Now that a working kernel setup is completed, install the [[[net-misc/vpnc]](https://packages.gentoo.org/packages/net-misc/vpnc)[]] package:

`root `[`#`]`emerge --ask net-misc/vpnc`

## [Configuration]

In order to make the following sections more clear, we need an example setup to work from. Example assumes that the home network computers are on the `192.0.2.0/24` network. The VPN client in question is run by a Gentoo computer `client1`using an private IP address it receives from local connected router.

### [Environment variables]

Configuration:

-   `dev` - `tun0` or `tap0` device

IP address table:

  ----------------------- ----------- --------------------- ---------------- ---------------------
  Hostname                Interface   IP address            Gateway          Network description
  **client1**             eth0        `192.0.2.10/24`` `    `192.0.2.1`` `   Private or Public
                          tun0        `192.168.255.10/24`   `tun0`` `        VPN
  **vpngw.example.org**               `203.0.113.2`` `                       Public - *internet*
  **dns1.example.org**                `192.168.100.100`                      VPN
  ----------------------- ----------- --------------------- ---------------- ---------------------

** Note**\
This is a *example* IP scenario used in this document. For real world usage, change the according IP networking entries.

\
The state of the current DNS and IP setup on the gentoo `client1` before the vpnc connection has been established:

`user `[`$`]`ip route`

    default via 192.0.2.1 dev eth0 proto dhcp src 192.0.2.10 metric 1002
    192.0.2.0/24 dev eth0 proto dhcp scope link src 192.0.2.10 metric 1002

`user `[`$`]`ip add show eth0`

    2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
        link/ether 0c:cf:f4:fb:00:00 brd ff:ff:ff:ff:ff:ff
        inet 192.0.2.10/24 brd 192.0.2.255 scope global dynamic noprefixroute eth0
           valid_lft 82782sec preferred_lft 71982sec
        inet6 fe80::ecf:f4ff:fefb:0/64 scope link proto kernel_ll
           valid_lft forever preferred_lft forever

`user `[`$`]`more /etc/resolv.conf`

    # Generated by dhcpcd
    nameserver 192.0.2.1

### [Files]

-   [/etc/conf.d/vpnc] - Gentoo\'s config file for vpnc daemon.
-   [/etc/vpnc/vpnc.conf] - Global (system wide) configuration file.
-   [/etc/vpnc/work.conf] - Conventional filename for additional configuration rules.

The configuration file for vpnc connection settings can be located in a couple places, depending on how many profiles need to be configured. By default, vpnc looks for [/etc/vpnc/vpnc.conf] for its connection settings. This setup will only address a single profile example and will use the configuration file location [/etc/vpnc/vpnc.conf].

[FILE] **`/etc/vpnc/vpnc.conf`**

    IPSec gateway vpngw.example.org
    IPSec ID tunnel-split
    IPSec secret gentoo-linux-rocks
    Xauth username larry
    Xauth password gentoo-linux-rocks-and-I-am-a-cow

The configuration file example above should be modified to reflect the appropriate values for the local setup. The gateway option `vpngw.example.org` can be a fully qualified domain name or an IP address. The ID and secret options should be given by a network administrator.

#### [Windows profile .pcf]

If the authentication credentials cannot be obtained but a working setup on a Windows box is available which utilizes the official Cisco VPN client, then it suffices to export the profile. The user name and password options are for the normal network sign-on, such as a Windows NT domain account. When the profile is exported from a Windows machine, then the result is most likely a file ending in [.pcf]. This file will have all the necessary information. Below is an example:

[FILE] **`profile.pcf`**

    [main]
    Description=
    Host=vpngw.example.org
    AuthType=1
    GroupName=tunnel-split
    GroupPwd=
    enc_GroupPwd=F3256220AA200A1D532556024F4F314B0388D48B0FBF2DB12
    EnableISPConnect=0
    ISPConnectType=0
    ISPConnect=FOOBAR
    ISPCommand=
    Username=
    SaveUserPassword=0
    UserPassword=
    enc_UserPassword=
    NTDomain=
    EnableBackup=0
    BackupServer=
    EnableMSLogon=1
    MSLogonType=0
    EnableNat=1
    TunnelingMode=0
    TcpTunnelingPort=10000
    CertStore=0
    CertName=
    CertPath=
    CertSubjectName=
    CertSerialHash=00000000000000000000000000000000
    SendCertChain=0
    VerifyCertDN=
    DHGroup=2
    ForceKeepAlives=0
    PeerTimeout=90
    EnableLocalLAN=0
    EnableSplitDNS=1
    ForceNetLogin=0

In the above example, we can see entries for

-   `Host`,
-   `GroupName`
-   `enc_GroupPwd`.

The user credentials may or may not be exported depending on the setup:

-   `Username`
-   `UserPassword`

To generate a working vpnc configuration out of it, use `pcf2vpnc`, included with vpnc.

** Note**\
The password can be decrypted with the help from the [cisco-decrypt] program, shipped with the latest vpnc.

Converting the [\~/profile.pcf] file into a [/etc/vpnc/vpnc.conf] working configuration using the [pcf2vpnc] tool:

`user `[`$`]`pcf2vpnc profile.pcf`

    ## generated by pcf2vpnc
    IKE Authmode psk
    IKE DH Group dh2
    IPSec secret ASD1v5J.a&H.tkfJ

    IPSec gateway VPNGW.EXAMPLE.ORG
    IPSec ID group_id

    ## To add your username and password,
    ## use the following lines:
    # Xauth username <your username>
    # Xauth password <your password>

### [Service]

vpnc contains an init script ([/etc/init.d/vpnc]) to handle multiple configurations at same time. The default script looks for [/etc/vpnc/vpnc.conf], but additional configurations are possible. Before and after shutdown and start-up custom-made scripts can be executed that are connected by their name to the corresponding init script. Script names end in [-preup.sh], [-postup.sh], [-predown.sh] and [-postdown.sh], stored in the [/etc/vpnc/scripts.d/] directory. The general naming scheme is sketched in the shown table.

  ------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------
  Init script name                                                                                             Needed configuration file                                                                                  Pre-up script name
  [/etc/init.d/vpnc]        [/etc/vpnc/vpnc.conf]   [/etc/vpnc/scripts.d/vpnc-preup.sh]
  [/etc/init.d/vpnc.work]   [/etc/vpnc/work.conf]   [/etc/vpnc/scripts.d/work-preup.sh]
  ------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------

#### [OpenRC]

Add vpnc to default runlevel with the following commands (in this case for the standard configuration). Add the `tun` module (if built that way) to the kernel\'s autoload mechanism at startup.

`root `[`#`]`rc-update add vpnc default`

To show all output and prompts on standard output edit the [/etc/conf.d/vpnc] configuration file.

Set the `VPNCOUTPUT` variable to `yes` to all output and promts for the authentication, entering password on the prompt.

Or leave it at the default setting `no`, where its default is to not display screen output. This way the saved password `Xauth password` in the global configuration file [/etc/vpnc/vpnc.conf] is used.

#### [runit]

[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Vpnc&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

#### [systemd]

[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Vpnc&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

## [Usage]

Now that a configuration is in place it is time to test the setup. To start [vpnc] do the following:

`root `[`#`]`service vpnc start`

     * Starting VPNC: vpnc ...                                                [ ok ]

The above command output shows that, once [vpnc] (as root) is executed, a prompt comes up asking for a password. After entering the password (which will not be echoed to the terminal), the [vpnc] process will automatically become a background process.

** Note**\
If the `Xauth password` option is specified in the vpnc config file, then at vpnc startup no password will be asked. Additionally, if vpnc needs some extra options not specified in the configuration file, or if something is forgotten, don\'t worry, it will ask for it.

`user `[`$`]`ip add`

    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
           valid_lft forever preferred_lft forever
        inet6 ::1/128 scope host proto kernel_lo
           valid_lft forever preferred_lft forever
    2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
        link/ether 0c:cf:f4:fb:00:00 brd ff:ff:ff:ff:ff:ff
        inet 192.0.2.10/24 brd 192.0.2.255 scope global dynamic noprefixroute eth0
           valid_lft 82974sec preferred_lft 72174sec
        inet6 fe80::ecf:f4ff:fefb:0/64 scope link proto kernel_ll
           valid_lft forever preferred_lft forever
    3: tun0: <POINTOPOINT,MULTICAST,NOARP,UP,LOWER_UP> mtu 1412 qdisc pfifo_fast state UNKNOWN group default qlen 500
        link/none
        inet 192.168.255.10/32 scope global tun0
           valid_lft forever preferred_lft forever
        inet6 fe80::4d36:4f9:735f:ee44/64 scope link stable-privacy proto kernel_ll
           valid_lft forever preferred_lft forever

`user `[`$`]`ip route`

    default via 192.0.2.1 dev eth0 proto dhcp src 192.0.2.10 metric 1002
    192.0.2.0/24 dev eth0 proto dhcp scope link src 192.0.2.10 metric 1002
    192.168.100.100 dev tun0 scope link
    192.168.255.0/24 dev tun0 scope link
    203.0.113.2 via 192.0.2.1 dev eth0 src 192.0.2.10

`user `[`$`]`more /etc/resolv.conf`

    #@VPNC_GENERATED@ -- this file is generated by vpnc
    # and will be overwritten by vpnc
    # as long as the above mark is intact
    # Generated by dhcpcd
    nameserver 192.168.100.100
    search example.org

Verify the vpn configured DNS server is reachable:

`user `[`$`]`ping dns1`

    PING dns1.example.org (192.168.100.100) 56(84) bytes of data.
    64 bytes from dns1.example.org (192.168.100.100): icmp_seq=1 ttl=64 time=2.40 ms
    64 bytes from dns1.example.org (192.168.100.100): icmp_seq=2 ttl=64 time=3.44 ms
    64 bytes from dns1.example.org (192.168.100.100): icmp_seq=3 ttl=64 time=3.20 ms

    --- dns1.example.org ping statistics ---
    3 packets transmitted, 3 received, 0% packet loss, time 2003ms
    rtt min/avg/max/mdev = 2.404/3.013/3.441/0.442 ms

As can be seen from the above command output(s), [vpnc] has done the following:

-   Created the tun0 network interface, a virtual interface to handle the traffic across the VPN tunnel
-   Obtained the IP address for the tun0 device from the VPN provider
-   Set routes to route VPN related traffic only to the VPN gateway
-   Set DNS server for the VPN

At this point, the workstation is capable of communicating with hosts via the VPN. Because [vpnc] sets the default route to the local gateway, and only the VPN network intersting traffic will be routed to the IPSec concentrator appliance.

To end the current vpnc session use [service vpnc stop] command. An example is shown below:

`root `[`#`]`service vpnc stop`

    * Stopping VPNC: vpnc ...                                                [ ok ]

## [Troubleshooting]

### [Configuration debugging]

Use the `--debug n` running option to get more verbose output. Following options are available:

`user `[`$`]`vpnc --help`

    --debug <0/1/2/3/99>
         Show verbose debug messages
          *  0: Do not print debug information.
          *  1: Print minimal debug information.
          *  2: Show statemachine and packet/payload type information.
          *  3: Dump everything exluding authentication data.
          * 99: Dump everything INCLUDING AUTHENTICATION data (e.g. PASSWORDS).
     conf-variable: Debug<0/1/2/3/99>

Example output of configuration debugging `--debug 1` a not working connection session:

`root `[`#`]`vpnc --debug 1 /etc/vpnc/vpnc.conf`

    vpnc version 0.5.3
    response was invalid [1]:  (ISAKMP_N_INVALID_EXCHANGE_TYPE)(7)

Optionally enable debug output in the [/etc/vpnc/vpnc.conf] configuration file add follwing line at the last line:

    ...
    Xauth username larry
    debug 2

## [See also]

-   [OpenVPN](https://wiki.gentoo.org/wiki/OpenVPN "OpenVPN") --- software that enables the creation of secure point-to-point or site-to-site connections.
-   [WireGuard](https://wiki.gentoo.org/wiki/WireGuard "WireGuard") --- a modern, simple, and secure VPN that utilizes state-of-the-art cryptography.
-   [VPN services](https://wiki.gentoo.org/wiki/VPN_services "VPN services")

## [External resources]

-   [vpnc-devel Mailing list Davide Pucci - Asking for patch merge](https://lists.unix-ag.uni-kl.de/pipermail/vpnc-devel/2017-November/004233.html)
-   [Davide Pucci - taking over the long-term maintanance announced on the official vpnc-devel mailing list](https://davidepucci.it/doc/vpnc/)
-   [vpnc - forked repository for long-term maintainenace of vpnc](https://github.com/streambinder/vpnc)
-   [Old VPNC homepage](http://www.unix-ag.uni-kl.de/~massar/vpnc/)

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **David H. Askew, Christian Faulhammer, Thomas Fischer, nightmorph**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*