*Not to be confused with [I2C](https://wiki.gentoo.org/wiki/I2C "I2C").*

**Resources**

[[]][Home](https://geti2p.net/)

[[]][net-vpn/i2p (java)](https://packages.gentoo.org/packages/net-vpn/i2p)

[[]][net-vpn/i2pd (C++)](https://packages.gentoo.org/packages/net-vpn/i2pd)

[[]][Wikipedia](https://en.wikipedia.org/wiki/I2P "wikipedia:I2P")

[[]][Official documentation](https://geti2p.net/en/docs)

[[]][GitHub](https://github.com/i2p/i2p.i2p)

The Invisible Internet Project (**I2P**) is an anonymous network, similar to [Tor](https://wiki.gentoo.org/wiki/Tor "Tor"). The key difference is that I2P is internal, focusing on providing anonymous services within the network rather than proxying traffic to the regular internet (although some proxy services do exist).

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Java]](#Java)
        -   [[1.1.1] [USE flags]](#USE_flags)
    -   [[1.2] [i2pd (C++)]](#i2pd_.28C.2B.2B.29)
        -   [[1.2.1] [USE flags]](#USE_flags_2)
-   [[2] [Setup]](#Setup)
    -   [[2.1] [Services]](#Services)
        -   [[2.1.1] [OpenRC]](#OpenRC)
        -   [[2.1.2] [systemd]](#systemd)
    -   [[2.2] [Configuration]](#Configuration)
        -   [[2.2.1] [Firewall]](#Firewall)
        -   [[2.2.2] [Browser]](#Browser)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Eepsites]](#Eepsites)
    -   [[3.2] [Bittorrent]](#Bittorrent)
    -   [[3.3] [IRC]](#IRC)
    -   [[3.4] [SSH]](#SSH)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [Java]

`root `[`#`]`emerge --ask net-vpn/i2p`

#### [USE flags]

### [USE flags for] [net-vpn/i2p](https://packages.gentoo.org/packages/net-vpn/i2p) [[]] [A privacy-centric, anonymous network]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-27 00:30] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [][i2pd (C++)]

`root `[`#`]`emerge --ask net-vpn/i2pd`

#### [USE flags]

### [USE flags for] [net-vpn/i2pd](https://packages.gentoo.org/packages/net-vpn/i2pd) [[]] [A C++ daemon for accessing the I2P anonymous network]

  ------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+upnp`](https://packages.gentoo.org/useflags/+upnp)   Enable UPnP port mapping support
  [`test`](https://packages.gentoo.org/useflags/test)     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-07 01:32] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

## [Setup]

### [Services]

Examples below are for java implementation of the i2p. When using the C++ version, substitute **i2p** for **i2pd.**

#### [OpenRC]

To start the i2p service when the system boots:

`root `[`#`]`rc-update add i2p default`

To start the i2p service now:

`root `[`#`]`rc-service i2p start`

#### [systemd]

To start the i2p service when the system boots:

`root `[`#`]`systemctl enable i2p.service`

To start the i2p service now:

`root `[`#`]`systemctl start i2p.service`

### [Configuration]

Most I2P configuration is done in the Router Console, accessible via web browser at `localhost:7657` once the router service has been started.

Default configuration for i2pd is available at `localhost:7070`.

#### [Firewall]

I2P selects a random port between 9000 and 31000 for inbound traffic when the router is first run. This port is forwarded automatically by UPnP, but if your gateway/firewall does not support UPnP, it will need to be manually forwarded (both TCP and UDP) for best performance. Visit [http://localhost:7657/confignet](http://localhost:7657/confignet) to find out which port.

#### [Browser]

You can use a pac file to delegate browser requests to different proxies. Here connections to localhost are handled directly (no proxy). Eepsites are handled by I2P proxy on port 4444. Other traffic goes via Tor SOCKS proxy on running on port 9050.

[FILE] **`/usr/local/proxy.pac`**

    function FindProxyForURL(url, host)


Save this file as [/usr/local/proxy.pac], and point your browser to it. Most browsers accept Proxy configuration URL, where you can specify `file:///usr/local/proxy.pac`.

I2P\'s CSS can make browsers sluggish. You can add the following to your [profile_dir/chrome/userContent.css] to speed up rendering:

[FILE] **`profile_dir/chrome/userContent.css`**

    @-moz-document url-prefix('http://localhost:7657/')

    }

## [Usage]

### [Eepsites]

To access websites hosted on the I2P network, a web browser must be configured to use a proxy at `localhost:4444` for HTTP and `localhost:4445` for HTTPS. This can be accomplished globally in most browsers\' proxy settings, or specifically for sites with the .i2p TLD using a plugin like FoxyProxy for [Firefox](https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard) or [Chrome](https://chrome.google.com/webstore/detail/foxyproxy-standard/gcknhkkoolaabfmlnjonogaaifnjlfnp) See also: [https://geti2p.net/en/about/browser-config](https://geti2p.net/en/about/browser-config)

### [Bittorrent]

I2PSnark, the I2P Bittorrent client, is accessible at `localhost:7657/i2psnark` with no additional configuration. However, the above Eepsite configuration is necessary to reach the trackers on which the torrents are found.

### [IRC]

Using any IRC client, set up a connection to `localhost:6668` No account creation is required. If using Pidgin, be sure to fill in the **Ident name** and **Real name** fields in addition to **Username**, otherwise Pidgin may expose identity information from other configured accounts.

### [SSH]

*openssh* doesn\'t have any native support for SOCKS5, so you will need to install *openbsd-netcat*. You\'ll need to modify your SSH config too. It is possible with *netcat\' also but the configuration below uses flags specific to the OpenBSD variant.*

`root `[`#`]`emerge --ask net-analyzer/openbsd-netcat`

This enables proxying through a SOCKS5 I2P tunnel for all *.i2p* hosts. You will need to go to [http://localhost:7657/i2ptunnelmgr](http://localhost:7657/i2ptunnelmgr) and create a SOCKS5 **client** tunnel. Note the port you have used and replace \'1234\' in the below config with it.

[FILE] **`~/.ssh/config`**

    Host *.i2p
        # Tell SSH to pass its connections through netcat, using a SOCKS5 proxy at 127.0.0.1:1234.
        ProxyCommand nc -X 5 -x 127.0.0.1:1234 %h %p

        # Privacy protections
        # Prevents SSH from telling the remote server about all of your public keys, potentially revealing your ID
        ForwardAgent no
        IdentitiesOnly yes

            # Merges connections to a server to prevent expensive reconnections
            # To avoid this, invoke ssh asb: ssh -o 'ControlMaster no' ...
        ControlMaster auto
        ControlPath ~/.ssh/master-%r@%n:%p

            # Compression for low bandwidth lines (like I2P)
        Compression yes

## [See also]

-   [Tor](https://wiki.gentoo.org/wiki/Tor "Tor") - An onion routing internet anonymity system.

## [External resources]

-   [I2P - Protocol Stack](https://geti2p.net/en/docs/protocol)