**Resources**

[[]][Home](https://www.teamviewer.com/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/TeamViewer "wikipedia:TeamViewer")

**TeamViewer** is a proprietary (closed source), all-in-one solution for remote access and support over the Internet. It has both a client and a server mode and requires either a built-in or system [Wine](https://wiki.gentoo.org/wiki/Wine "Wine").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Service]](#Service)
        -   [[2.2.1] [OpenRC]](#OpenRC)
        -   [[2.2.2] [systemd]](#systemd)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Files]](#Files_2)
    -   [[4.2] [Unmerge]](#Unmerge)
    -   [[4.3] [Crash with Wayland]](#Crash_with_Wayland)
-   [[5] [See also]](#See_also)

## [Installation]

Be aware there are a few versions of TeamViewer available in the main Gentoo repository.

### [USE flags]

### [USE flags for] [net-misc/teamviewer](https://packages.gentoo.org/packages/net-misc/teamviewer) [[]] [All-In-One Solution for Remote Access and Support over the Internet]

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-11 07:47] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Be aware it is necessary to accept TeamViewer\'s End User License Agreement (EULA) before the software can be installed.

`root `[`#`]`emerge --ask net-misc/teamviewer`

It is recommended that OpenRC users using the desktop or plasma profiles enable `elogind` in [make.conf]:

[FILE] **`/etc/portage/make.conf`**

    USE="$ elogind"

Then rebuild the system for the USE change:

`root `[`#`]`emerge -avDU @world`

## [Configuration]

### [Files]

Supposing TeamViewer 15 has been installed, the configuration files would be found in the following locations:

-   [/etc/teamviewer15/global.conf] - Global (system wide) configuration file.
-   [\~/.config/teamviewer/] - Local (per user) configuration file.

### [Service]

The TeamViewer daemon must be started before using the TeamViewer front-end. Those who want TeamViewer to be running every time they boot their system will need to add it the list of services that run during system start.

#### [OpenRC]

Start TeamViewer during system start:

`root `[`#`]`rc-update add teamviewerd default`

Start the TeamViewer daemon now:

`root `[`#`]`rc-service teamviewerd start`

#### [systemd]

Start TeamViewer during system start:

`root `[`#`]`systemctl enable teamviewerd`

Start the TeamViewer daemon now:

`root `[`#`]`systemctl start teamviewerd`

## [Usage]

### [Invocation]

After the service has been started, simply start TeamViewer from the Applications menu in a desktop environment. Those using a command line can start it via:

`user `[`$`]`teamviewer`

## [Removal]

### [Files]

In order to scrub all traces of TeamViewer from the system each user\'s [\~/.config/teamviewer] folder should be removed:

`user `[`$`]`rm -rf ~/.config/teamviewer*`

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose net-misc/teamviewer`

### [Crash with Wayland]

If the client crashes on Wayland. Try

`user `[`$`]`QT_QPA_PLATFORM="xcb" teamviewer`

[Reference.](https://community.teamviewer.com/English/discussion/126737/teamviewer-cannot-start-in-kde-wayland-with-qt-qpa-platform-wayland/p1)

## [See also]

-   [TigerVNC](https://wiki.gentoo.org/wiki/TigerVNC "TigerVNC") --- a client/server software package allowing remote network access to graphical desktops.
-   [AnyDesk](https://wiki.gentoo.org/wiki/AnyDesk "AnyDesk") --- a proprietary (closed source), software for remote access and support over the Internet similar to [TeamViewer]