**Resources**

[[]][Home](http://multipath-tcp.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Multipath_TCP "wikipedia:Multipath TCP")

[[]][GitHub](https://github.com/multipath-tcp/mptcp)

MultiPath TCP (MPTCP) is an effort towards enabling the simultaneous use of several IP-addresses/interfaces by a modification of TCP that presents a regular TCP interface to applications, while in fact spreading data across several subflows. Benefits of this include better resource utilization, better throughput and smoother reaction to failures.

## Contents

-   [[1] [Installation =]](#Installation_.3D)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Services]](#Services)
    -   [[2.1] [systemd]](#systemd)
    -   [[2.2] [OpenRC]](#OpenRC)
-   [[3] [External resources]](#External_resources)

## [][Installation =]

### [Kernel]

[KERNEL]

     Networking support Search for <code>CONFIG_NET</code> to find this item. --->
       Networking options --->
         [*] TCP/IP networking Search for <code>CONFIG_INET</code> to find this item.
           [*]   MPTCP: Multipath TCP Search for <code>CONFIG_MPTCP</code> to find this item.
           [*]     MPTCP: IPv6 support for Multipath TCP Search for <code>CONFIG_MPTCP_IPV6</code> to find this item.

\

### [Emerge]

`root `[`#`]`emerge --ask net-misc/mptcpd`

\

## [Services]

### [systemd]

`root `[`#`]`systemctl enable avahi-daemon.service`

`root `[`#`]`systemctl start avahi-daemon.service`

### [OpenRC]

TODO: There is no OpenRC init script for this yet.

## [External resources]

-   [Userspace configuration](http://multipath-tcp.org/pmwiki.php/Users/ConfigureRouting)
-   [Official guide How to Install MPTCP](http://multipath-tcp.org/pmwiki.php/Users/HowToInstallMPTCP?)
-   [Gentoo Bugzilla: Request for adding MPTCP into gentoo-sources](https://bugs.gentoo.org/show_bug.cgi?id=477786)
-   [MPTCP-related Bugzilla](https://github.com/multipath-tcp/mptcp/issues?page=1&state=open)