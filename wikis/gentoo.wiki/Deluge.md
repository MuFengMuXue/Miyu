[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Deluge&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://deluge-torrent.org/)

[[]][Package information](https://packages.gentoo.org/packages/net-p2p/deluge)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Deluge_(software) "wikipedia:Deluge (software)")

[[]][GitHub](https://github.com/deluge-torrent/deluge)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/deluge)

**Deluge** is an open-source, cross platform [BitTorrent](https://wiki.gentoo.org/wiki/BitTorrent "BitTorrent") client. It features a GTK-based GUI, a command line interface, a web interface, and also supports remote clients. Deluge is written in Python 3.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Headless server]](#Headless_server)
    -   [[2.2] [Deluge web UI]](#Deluge_web_UI)
        -   [[2.2.1] [Adding SSL support to UI]](#Adding_SSL_support_to_UI)
    -   [[2.3] [Remote GTK client]](#Remote_GTK_client)
-   [[3] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [net-p2p/deluge](https://packages.gentoo.org/packages/net-p2p/deluge) [[]] [BitTorrent client with a client/server model]

  --------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`appindicator`](https://packages.gentoo.org/useflags/appindicator)   Build in support for notifications using the libindicate or libappindicator plugin
  [`console`](https://packages.gentoo.org/useflags/console)             Enable default console UI
  [`gui`](https://packages.gentoo.org/useflags/gui)                     Enable support for a graphical user interface
  [`libnotify`](https://packages.gentoo.org/useflags/libnotify)         Enable desktop notification support
  [`sound`](https://packages.gentoo.org/useflags/sound)                 Enable sound support
  [`test`](https://packages.gentoo.org/useflags/test)                   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`webinterface`](https://packages.gentoo.org/useflags/webinterface)   Install dependencies needed for the web interface
  --------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-13 15:40] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask net-p2p/deluge`

## [Configuration]

### [Headless server]

1.  Start the deluged daemon

    :::: cmd-box


    `root `[`#`]`/etc/init.d/deluged start`


    ::::

    -   To start the daemon on system launch, issue:

        :::: cmd-box


        `root `[`#`]`rc-update add deluged default`


        ::::
2.  Make sure that Deluge is built with the `console` USE flag.
3.  Enable remote connections
    -   Switch to the deluge user

        :::: cmd-box


        `root `[`#`]`su --shell /bin/bash deluge`


        ::::
    -   Open the deluge cli

        :::: cmd-box


        `deluge $``deluge-console`


        ::::
    -   Change the configuration value

        :::: cmd-box


        `>>>``config -s allow_remote True`


        ::::
    -   Leave the deluge cli

        :::: cmd-box


        `>>>``exit`


        ::::
4.  Set the server username and password

    :::: cmd-box


    `deluge $``echo "Larry:GentooLinuxrocks" >> ~/.config/deluge/auth`


    ::::
5.  Restart deluged

    :::: cmd-box


    `root `[`#`]`/etc/init.d/deluged restart`


    ::::

### [Deluge web UI]

1.  Make sure that Deluge is built with the `webinterface` USE flag.
2.  Configure deluge-web

    ::: box-caption
    [FILE] **`/etc/conf.d/deluge-web`Setting up the UI**
    :::

    :::
        # /etc/conf.d/deluge-web
        # Change this to the user:group that should run deluge.
        DELUGE_WEB_USER="deluge:deluge"
        DELUGE_WEB_HOME="/var/lib/deluge"
        DELUGE_WEB_OPTS="-p 8112 --interface "<ipv6 address or ipv4 address to bind>" -L=debug -c /var/lib/deluge -l /var/lib/deluge/deluge-web.log"
    :::

    -   Starting the daemon on system launch can be done with

        :::: cmd-box


        `root `[`#`]`rc-update add deluge-web default`


        ::::

#### [Adding SSL support to UI]

1.  Make sure the certificate and key files are PEM encoded, and copy [certificate.crt.pem] and [certificate.key.pem] to the deluge home directory. Usually this is the [/var/lib/deluge] directory by default.
2.  Edit the web.conf file.

    ::: box-caption
    [FILE] **`/var/lib/deluge/web.conf`Adding SSL support**
    :::

    :::
        {
            "base": "/",
            "cert": "ssl/seedbox.cert",
            "pkey": "ssl/seedbox.key",
    :::

** Note**\
If the CA certificates are required, combine them (aka make a bundle with certificate and CA\'s) in the [certificate.crt.pem] file.

### [Remote GTK client]

1.  Make sure that Deluge is built with the `gui` USE flag.
2.  Launch deluge-gtk, go to *Edit -\> Preferences -\> Interface* and disable classic mode, then restart deluge-gtk.
3.  Add the headless server to the connection manager, filling in the username, password, IP address and port. Then click connect.
4.  Optionally, add the server as a default to hide the Connection Manager prompt.

## [External resources]

-   [https://dev.deluge-torrent.org/wiki/Plugins](https://dev.deluge-torrent.org/wiki/Plugins) - A list of useful plugins, both included and third-party.