[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=QBittorrent&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.qbittorrent.org)

[[]][GitHub](https://github.com/qbittorrent/qBittorrent)

[[]][Package information](https://packages.gentoo.org/packages/net-p2p/qbittorrent)

**qBittorrent** is an open source alternative BitTorrent client.

qBittorrent aims for a polished and intuitive interface, that is similar to the µTorrent UI. Additionally, qBittorrent runs and provides the same features on all major platforms (FreeBSD, Linux, macOS, OS/2, Windows).

qBittorrent is based on the Qt toolkit and libtorrent-rasterbar library.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Service for webui]](#Service_for_webui)
        -   [[2.2.1] [OpenRC]](#OpenRC)
        -   [[2.2.2] [systemd]](#systemd)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
        -   [[3.1.1] [GUI]](#GUI)
        -   [[3.1.2] [WebUI]](#WebUI)
-   [[4] [Tips]](#Tips)
    -   [[4.1] [Resetting login credentials]](#Resetting_login_credentials)
        -   [[4.1.1] [OpenRC]](#OpenRC_2)
        -   [[4.1.2] [systemd]](#systemd_2)
-   [[5] [Removal]](#Removal)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [net-p2p/qbittorrent](https://packages.gentoo.org/packages/net-p2p/qbittorrent) [[]] [BitTorrent client in C++ and Qt]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+dbus`](https://packages.gentoo.org/useflags/+dbus)             Enable support for notifications and power-management features via D-Bus
  [`+gui`](https://packages.gentoo.org/useflags/+gui)               Enable support for a graphical user interface
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  [`webui`](https://packages.gentoo.org/useflags/webui)             Install qBittorrent Web UI (qbittorrent-nox)
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-08 20:25] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

To install qBittorrent:

`root `[`#`]`emerge --ask net-p2p/qbittorrent`

## [Configuration]

Most people usually use the inbuilt GUI to manage settings, though the configuration files can be manually edited (with appropriate care).

### [Files]

-   [\~/.config/qBittorrent/qBittorrent.conf] - main configuration file for a user.

### [Service for webui]

The qBittorrent WebUI service can be started when system starts or reboots. See the [WebUI](https://wiki.gentoo.org/wiki/QBittorrent#WebUI "QBittorrent") section for how to access and use the WebUI.

Note that the availability of the WebUI is dependent on the [[[webui]](https://packages.gentoo.org/useflags/webui)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag being set.

#### [OpenRC]

`root `[`#`]`rc-update add qbittorrent default`

#### [systemd]

`root `[`#`]`systemctl enable qbittorrent`

## [Usage]

### [Invocation]

qBittorrent offers both a GUI to be run on a graphical desktop, and a WebUI that can be accessed from a web browser.

#### [GUI]

To start the qBittorrent GUI, simply run:

`user `[`$`]`qbittorrent`

#### [WebUI]

For WebUI, the USE flag [[[webui]](https://packages.gentoo.org/useflags/webui)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] has to be added. To open qBittorrent in *WebUI* mode, run the following:

`user `[`$`]`qbittorrent-nox`

The WebUI can be accessed using a [web browser](https://wiki.gentoo.org/wiki/Category:Web_browser "Category:Web browser"). Assuming the WebUI is running on the same system, a socket address `localhost:8080` should work. The *default* qBittorrent port is :8080

[   Note to editors] []

If a webui server is used, [qbittorrent-nox] surely doesn\'t have to be launched, so we should probably explain this here and in the \"service\" section, along with how to make the choice and the differences between both options.

## [Tips]

### [Resetting login credentials]

Should WebUI login credentials be lost, the login credentials can be reset without **losing** any configuration or torrents. Before performing a reset, qBittorrent should be **stopped** first to avoid the process overwriting the configuration:

#### [OpenRC]

`root `[`#`]`rc-service qbittorrent stop`

#### [systemd]

`root `[`#`]`systemctl stop qbittorrent`

Edit the configuration file:

[FILE] **`"~/.config/qBittorrent/qBittorrent.conf"`**

    ...
    # Comment out the WebUI Password and Username
    [Preferences]
    #WebUI\Password_PBKDF2="..."
    #WebUI\Username=larry
    ...

Save the *qBittorrent.conf* and start qBittorrent WebUI in terminal. The output should look like, as shown below:

`user `[`$`]`qbittorrent-nox`

    WebUI will be started shortly after internal preparations. Please wait...

    ******** Information ********
    To control qBittorrent, access the WebUI at: http://localhost:8080
    The WebUI administrator username is: admin
    The WebUI administrator password was not set. A temporary password is provided for this session: NKB7ALQ6M
    You should set your own password in program preferences.

Access the WebUI with the temporary password provided in the output and change the login credentials there.

## [Removal]

qBittorrent can be removed with unmerging it:

`root `[`#`]`emerge --ask --depclean --verbose net-p2p/qbittorrent`

## [See also]

[BitTorrent](https://wiki.gentoo.org/wiki/BitTorrent "BitTorrent") --- a decentralized file sharing protocol.

## [External resources]

-   [https://github.com/qbittorrent/qBittorrent/wiki/Explanation-of-Options-in-qBittorrent](https://github.com/qbittorrent/qBittorrent/wiki/Explanation-of-Options-in-qBittorrent) - Detailed explanation on settings options