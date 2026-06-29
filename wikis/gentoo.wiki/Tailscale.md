[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Tailscale&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://tailscale.com/)

[[]][Official documentation](https://tailscale.com/kb)

[[]][Package information](https://packages.gentoo.org/packages/net-vpn/tailscale)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Tailscale "wikipedia:Tailscale")

[[]][GitHub](https://github.com/tailscale/tailscale)

[[]][Bugs (upstream)](https://tailscale.com/kb/1227/bug-report)

[[]][Blog](https://tailscale.com/blog)

Tailscale facilitates remote access between devices and services across complex network boundaries such as [CGNAT](https://en.wikipedia.org/wiki/CGNAT "wikipedia:CGNAT").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Signing up]](#Signing_up)
    -   [[2.2] [Service]](#Service)
        -   [[2.2.1] [OpenRC]](#OpenRC)
        -   [[2.2.2] [systemd]](#systemd)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
    -   [[3.2] [Enabling the VPN]](#Enabling_the_VPN)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [[] Installation]

Tailscale requires either [[iptables](https://wiki.gentoo.org/wiki/Iptables "Iptables")] or [[nftables](https://wiki.gentoo.org/wiki/Nftables "Nftables")] to be present. Ensure one or the other is installed before continuing.

\

[KERNEL] **Enable `CONFIG_TUN` in the kernel**

    Device Drivers  --->
        [*] Network device support  --->
            [*] Network core driver support
            <*>   Universal TUN/TAP device driver support

### [[] Emerge]

Tailscale does not support any `USE` flags.

Merge the package:

`root `[`#`]`emerge --ask net-vpn/tailscale`

## [[] Configuration]

### [[] Signing up]

Setting up Tailscale requires an account. Tailscale does not store passwords, but instead relies on third-party single sign-on (SSO) providers such as Google, GitHub or OpenID connect. Users can sign up at [login.tailscale.com](https://login.tailscale.com/).

** See also**\
[https://tailscale.com/kb/1013/sso-providers](https://tailscale.com/kb/1013/sso-providers) has a list of supported SSO providers.

### [[] Service]

#### [[] OpenRC]

Add the Tailscale daemon to the [default] runlevel:

`root `[`#`]`rc-service tailscale start `

`root `[`#`]`rc-update add tailscale default `

#### [[] systemd]

Enable the Tailscale daemon:

`root `[`#`]`systemctl start tailscaled.service `

`root `[`#`]`systemctl enable tailscaled.service `

## [[] Usage]

### [[] Invocation]

`user `[`$`]`tailscale --help`

    USAGE
     The easiest, most secure way to use WireGuard.

    USAGE
      tailscale [flags] <subcommand> [command flags]

    For help on subcommands, add --help after: "tailscale status --help".

    This CLI is still under active development. Commands and flags will
    change in the future.

    SUBCOMMANDS
      up          Connect to Tailscale, logging in if needed
      down        Disconnect from Tailscale
      set         Change specified preferences
      login       Log in to a Tailscale account
      logout      Disconnect from Tailscale and expire current node key
      switch      Switch to a different Tailscale account
      configure   Configure the host to enable more Tailscale features
      syspolicy   Diagnose the MDM and system policy configuration
      netcheck    Print an analysis of local network conditions
      ip          Show Tailscale IP addresses
      dns         Diagnose the internal DNS forwarder
      status      Show state of tailscaled and its connections
      metrics     Show Tailscale metrics
      ping        Ping a host at the Tailscale layer, see how it routed
      nc          Connect to a port on a host, connected to stdin/stdout
      ssh         SSH to a Tailscale machine
      funnel      Serve content and local servers on the internet
      serve       Serve content and local servers on your tailnet
      version     Print Tailscale version
      web         Run a web server for controlling Tailscale
      file        Send or receive files
      bugreport   Print a shareable identifier to help diagnose issues
      cert        Get TLS certs
      lock        Manage tailnet lock
      licenses    Get open source license information
      exit-node   Show machines on your tailnet configured as exit nodes
      update      Update Tailscale to the latest/different version
      whois       Show the machine and user associated with a Tailscale IP (v4 or v6)
      drive       Share a directory with your tailnet
      completion  Shell tab-completion scripts

    FLAGS
      --socket value
            path to tailscaled socket (default /var/run/tailscale/tailscaled.sock)

### [[] Enabling the VPN]

Once the service is running, enable the VPN and follow the instructions:

`root `[`#`]`tailscale up`

## [[] Removal]

### [[] Unmerge]

Unmerge the package:

`root `[`#`]`emerge --ask --depclean --verbose net-vpn/tailscale`

## [[] See also]

-   [WireGuard](https://wiki.gentoo.org/wiki/WireGuard "WireGuard") --- a modern, simple, and secure VPN that utilizes state-of-the-art cryptography.
-   [[[net-vpn/headscale]](https://packages.gentoo.org/packages/net-vpn/headscale)[]] --- third-party self-hosted implementation of Tailscale control center.

## [[] External resources]

-   [Manage permissions (ACLs)](https://tailscale.com/kb/1018/acls) --- used to restrict traffic between devices in both directions, optionally based on port number.
-   [Subnet routers and traffic relay nodes](https://tailscale.com/kb/1019/subnets) --- allows access to devices that can\'t run Tailscale on a local network.
-   [Exit Nodes (route all traffic)](https://tailscale.com/kb/1103/exit-nodes) --- routes all traffic through one device, similarly to popular VPN services. By default, Tailscale acts as an overlay network and does not route internet traffic.
-   [Setting up a server on your Tailscale network](https://tailscale.com/kb/1245/set-up-servers) --- provides instructions for setting up a server and limiting access to it.
-   [Tailscale Funnel](https://tailscale.com/kb/1223/funnel) --- exposes a service to the internet.