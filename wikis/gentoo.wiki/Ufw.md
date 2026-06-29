[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Ufw&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://launchpad.net/ufw)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Uncomplicated_Firewall "wikipedia:Uncomplicated Firewall")

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/ufw-firewall)

**Ufw** is the **u**ncomplicated **f**ire**w**all, and is designed to be very simple to implement. It uses logs such as those obtained by [syslog-ng](https://wiki.gentoo.org/wiki/Syslog-ng "Syslog-ng") for monitoring, and uses [iptables](https://wiki.gentoo.org/wiki/Iptables "Iptables") as a back end. Ufw supports both IPv4 and IPv6.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Service]](#Service)
    -   [[2.1] [OpenRC]](#OpenRC)
    -   [[2.2] [systemd]](#systemd)
    -   [[2.3] [Configuration]](#Configuration)
        -   [[2.3.1] [KDE Connect]](#KDE_Connect)
-   [[3] [External Resources]](#External_Resources)

## [Installation]

### [Kernel]

The following kernel configuration must be made before ufw will work.

** Note**\
You must make configurations for [iptables](https://wiki.gentoo.org/wiki/Iptables "Iptables") & run the [iptables](https://wiki.gentoo.org/wiki/Iptables "Iptables") wiki page on top of these

[KERNEL] **IPv4 settings**

    [*] Networking support  --->
            Networking options  --->
                [*] Network packet filtering framework (Netfilter)  --->
                    Core Netfilter Configuration  --->
                        <M>   NetBIOS name service protocol support

IP version 6 is not required, however it is highly recommended.

[KERNEL] **IPv6 settings**

    [*] Networking support  --->
            Networking options  --->
                [*] Network packet filtering framework (Netfilter)  --->
                    [*] Advanced netfilter configuration
                    IPv6: Netfilter Configuration  --->
                        <M>   "rt" Routing header match support
                        <M>   "HL" hoplimit target support

### [USE flags]

### [USE flags for] [net-firewall/ufw](https://packages.gentoo.org/packages/net-firewall/ufw) [[]] [A program used to manage a netfilter firewall]

  ------------------------------------------------------------- ---------------------------
  [`examples`](https://packages.gentoo.org/useflags/examples)   Example ufw config files
  [`ipv6`](https://packages.gentoo.org/useflags/ipv6)           IPv6 support for iptables
  ------------------------------------------------------------- ---------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-09-02 17:00] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask net-firewall/ufw`

## [Service]

To allow [ssh](https://wiki.gentoo.org/wiki/Ssh "Ssh") by default:

`root `[`#`]`ufw allow ssh`

** Important**\
The ssh access is blocked by default.

** Note**\
This is a workaround for [[[bug #871747]](https://bugs.gentoo.org/show_bug.cgi?id=871747)[]].

If you get the warning \"ERROR: problem running\" then this can be solved by installing [dev-python/pip](https://packages.gentoo.org/packages/dev-python/pip)

`root `[`#`]`emerge --ask dev-python/pip`

### [OpenRC]

To start ufw at boot:

`root `[`#`]`rc-update add ufw default`

To start ufw immediately:

`root `[`#`]`rc-service ufw start`

### [systemd]

To start ufw at boot:

`root `[`#`]`systemctl enable ufw`

To start ufw immediately:

`root `[`#`]`systemctl start ufw`

### [Configuration]

To create a simple configuration, run:

`root `[`#`]`ufw default deny incoming`

`root `[`#`]`ufw allow from 192.168.0.0/24`

`root `[`#`]`ufw allow <application-name>`

To get a list of possible applications to add, run:

`root `[`#`]`ufw app list`

Then replace \<application-name\> with the name of the desired application. For example, to allow incoming Deluge traffic:

`root `[`#`]`ufw allow Deluge`

Next run

`root `[`#`]`ufw enable`

The last step is only required only the first time you install the package.

After changes to the rules, restart the firewall:

`root `[`#`]`ufw reload`

Specific use-cases and applications follow:

#### [KDE Connect]

To allow KDE Connect to work on the local network (192.168.0.x), ports 1714 through 1764 have to be opened for both UDP and TCP.

`root `[`#`]`ufw allow proto udp from 192.168.0.0/24 to any port 1714:1764 `

`root `[`#`]`ufw allow proto tcp from 192.168.0.0/24 to any port 1714:1764 `

## [External Resources]

-   [https://wiki.archlinux.org/index.php/Uncomplicated_Firewall](https://wiki.archlinux.org/index.php/Uncomplicated_Firewall)