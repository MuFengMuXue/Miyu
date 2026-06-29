[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Hamachi&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.vpn.net/)

Hamachi is a cross platform VPN tunneling engine.

## Contents

-   [[1] [Install]](#Install)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Services]](#Services)
        -   [[2.1.1] [OpenRC]](#OpenRC)
        -   [[2.1.2] [Systemd]](#Systemd)
    -   [[2.2] [Server]](#Server)
    -   [[2.3] [Client]](#Client)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Install]

### [Emerge]

`root `[`#`]`emerge --ask net-vpn/logmein-hamachi`

## [Configuration]

### [Services]

#### [OpenRC]

To immediately start the logmein-hamachi service:

`root `[`#`]`rc-service logmein-hamachi start`

To have the service start during the default runlevel (system boot), enter:

`root `[`#`]`rc-update add logmein-hamachi default`

#### [Systemd]

To start the logmein-hamachi service:

`root `[`#`]`systemctl start logmein-hamachi`

To start the service automatically at boot level, enter:

`root `[`#`]`systemctl enable logmein-hamachi`

If made any change to its config, restart it with:

`root `[`#`]`systemctl restart logmein-hamachi`

### [Server]

`root `[`#`]`hamachi login`

`root `[`#`]`hamachi set-nick gentoo`

`root `[`#`]`hamachi create 12345678`

Set a strong password

Be polite, and delete your network when you\'re done.

`root `[`#`]`hamachi delete 12345678`

`root `[`#`]`hamachi set-ip-mode ipv4`

To show the PID, IP, status, client, ID, and nickname:

`root `[`#`]`hamachi`

### [Client]

`root `[`#`]`hamachi login`

`root `[`#`]`hamachi set-nick alsogentoo`

`root `[`#`]`hamachi do-join 12345678`

Enter the server\'s strong password.

## [Usage]

### [Invocation]

To display all available commands:

`root `[`#`]`hamachi ?`

## [See also]

-   [Haguichi](https://wiki.gentoo.org/wiki/Haguichi "Haguichi") --- a graphical front-end to [Hamachi], a VPN tunneling engine.

## [External resources]

-   [Network types setup overview](https://support.logmeininc.com/hamachi/help/logmein-hamachi-network-types-hamachi-c-hamachi-networktypes)