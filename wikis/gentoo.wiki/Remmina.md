[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Remmina&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[[]][Home](https://remmina.org/)

[[]][Package information](https://packages.gentoo.org/packages/net-misc/remmina)

[[]][GitLab](https://gitlab.com/Remmina/Remmina)

[[]][Official project wiki](https://gitlab.com/Remmina/Remmina/wikis/home)

[[]][[#remmina](ircs://irc.libera.chat/#remmina)] ([[webchat](https://web.libera.chat/#remmina)])

[[]][Blog](https://remmina.org/blog/)

**Remmina** is a remote desktop client with support for various protocols, e.g. RDP, VNC, and SPICE.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [RDP]](#RDP)

## [Installation]

### [USE flags]

### [USE flags for] [net-misc/remmina](https://packages.gentoo.org/packages/net-misc/remmina) [[]] [A GTK+ RDP, SPICE, VNC and SSH client]

  ----------------------------------------------------------------------- ------------------------------------------------------------------------------------
  [`+appindicator`](https://packages.gentoo.org/useflags/+appindicator)   Build in support for notifications using the libindicate or libappindicator plugin
  [`X`](https://packages.gentoo.org/useflags/X)                           Add support for X11
  [`crypt`](https://packages.gentoo.org/useflags/crypt)                   Add support for encryption \-- using mcrypt or gpg where applicable
  [`cups`](https://packages.gentoo.org/useflags/cups)                     Add support for CUPS (Common Unix Printing System)
  [`examples`](https://packages.gentoo.org/useflags/examples)             Install examples, usually source code
  [`gvnc`](https://packages.gentoo.org/useflags/gvnc)                     Enable GVNC plugin using gtk-vnc, suitable for KVM and Vino servers
  [`keyring`](https://packages.gentoo.org/useflags/keyring)               Enable support for freedesktop.org Secret Service API password store
  [`kwallet`](https://packages.gentoo.org/useflags/kwallet)               Enable KDE Wallet plugin
  [`nls`](https://packages.gentoo.org/useflags/nls)                       Add Native Language Support (using gettext - GNU locale utilities)
  [`python`](https://packages.gentoo.org/useflags/python)                 Add optional support/bindings for the Python language
  [`rdp`](https://packages.gentoo.org/useflags/rdp)                       Enables RDP/Remote Desktop support
  [`spice`](https://packages.gentoo.org/useflags/spice)                   Support connecting to SPICE-enabled virtual machines
  [`ssh`](https://packages.gentoo.org/useflags/ssh)                       Enable support for SSH/SFTP protocol
  [`vnc`](https://packages.gentoo.org/useflags/vnc)                       Enable VNC (remote desktop viewer) support
  [`wayland`](https://packages.gentoo.org/useflags/wayland)               Enable dev-libs/wayland backend
  [`webkit`](https://packages.gentoo.org/useflags/webkit)                 Add support for the WebKit HTML rendering/layout engine
  [`zeroconf`](https://packages.gentoo.org/useflags/zeroconf)             Support for DNS Service Discovery (DNS-SD)
  ----------------------------------------------------------------------- ------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-21 05:26] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask net-misc/remmina`

## [Usage]

### [RDP]

First, ensure Remmina is built with [[[net-misc/remmina\[rdp\]]](https://packages.gentoo.org/packages/net-misc/remmina)[]].

To connect to a RDP session, click the + in the top left, give it a name, and in the Protocol dropdown, choose `RDP - Remote Desktop Protocol`.

Then, put the IP or domain name with port in the Server input box, enter the username and password, then click `Save and Connect` to save the server.