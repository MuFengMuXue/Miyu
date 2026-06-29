**Resources**

[[]][Home](https://wayland.freedesktop.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Wayland_(display_server_protocol) "wikipedia:Wayland (display server protocol)")

[[]][gitweb in freedesktop.org](https://cgit.freedesktop.org/wayland/wayland)

** Note**\
This is a general introduction to Wayland. For information about Wayland-related software, such compositors, launchers, etc., refer to the [List of software for Wayland](https://wiki.gentoo.org/wiki/List_of_software_for_Wayland "List of software for Wayland").

[Wayland] is a [communication protocol](https://en.wikipedia.org/wiki/communication_protocol "wikipedia:communication protocol") between a [display server](https://en.wikipedia.org/wiki/display_server "wikipedia:display server") and its clients:

> Wayland is the language (protocol) that applications can use to talk to a display server in order to make themselves visible and get input from the user (a person). A Wayland server is called a \"compositor\". Applications are Wayland clients.
>
> Wayland also refers to a system architecture. It is not just a server-client relationship between a compositor and applications. There is no single common Wayland server like Xorg is for X11, but every graphical environment brings with it one of many compositor implementations. Window management and the end user experience are often tied to the compositor rather than swappable components.^[\[1\]](#cite_note-1)^

GNOME and KDE have full Wayland support: GNOME provides the Mutter compositor, and KDE provides the KWin compositor. However, there are also various independent compositors available, including a number based on the [wlroots](https://wiki.gentoo.org/wiki/Wlroots "Wlroots") library.

For background information, including some of the rationales for moving from developing X11 to developing Wayland, be sure to follow the links in the \"[External resources](#External_resources)\" section below.

## Contents

-   [[1] [Introduction for users]](#Introduction_for_users)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [USE flags]](#USE_flags)
        -   [[2.1.1] [Global]](#Global)
        -   [[2.1.2] [Local]](#Local)
    -   [[2.2] [Emerge]](#Emerge)
-   [[3] [Toolkit support]](#Toolkit_support)
    -   [[3.1] [GTK]](#GTK)
    -   [[3.2] [Qt]](#Qt)
-   [[4] [Running X-only applications via Xwayland]](#Running_X-only_applications_via_Xwayland)
-   [[5] [Wayback]](#Wayback)
-   [[6] [Wayland over a network]](#Wayland_over_a_network)
-   [[7] [Running Wayland/X11 applications as a different user]](#Running_Wayland.2FX11_applications_as_a_different_user)
    -   [[7.1] [Wayland applications]](#Wayland_applications)
    -   [[7.2] [X applications]](#X_applications)
-   [[8] [Troubleshooting]](#Troubleshooting)
    -   [[8.1] [Setting the screen resolution]](#Setting_the_screen_resolution)
-   [[9] [See also]](#See_also)
-   [[10] [External resources]](#External_resources)
-   [[11] [References]](#References)

## [Introduction for users]

From a user\'s point of view, Wayland is nothing more than a framework. In particular, Wayland itself does *not* implement any display server analogous to the Xorg server. Individual Wayland *compositors*, implemented by various projects, combine the functionality of a display server with the functionality of a window manager (WM).

Thus, using Wayland involves choosing a compositor, and configuring that compositor to \"configure the server\", i.e. set screen resolutions, input and video drivers options, etc.

The [reference implementation](https://en.wikipedia.org/wiki/reference_implementation "wikipedia:reference implementation") compositor is [Weston](https://wiki.gentoo.org/wiki/Weston "Weston"). However, Weston is minimal and intended primarily for developers, rather than for end-users.

In addition to the core Wayland specifications, various extension specifications are being developed. The [Wayland explorer](https://wayland.app/protocols/) site provides information about the specifications, and the extent to which they are implemented by some of the main compositors (including KWin, Mutter and Sway). A particular compositor not implementing certain functionality doesn\'t necessarily mean that other compositors don\'t support it, nor that it\'s not possible under Wayland.

Nonetheless, this situation means there might not (yet) be standard ways of doing certain things: for example, Wayland currently has nothing corresponding to X\'s [[[xmodmap(1)]](https://man.archlinux.org/man/xmodmap.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")], with each compositor providing its own way to remap keys (if it does so at all).

However, the [wlroots](https://wiki.gentoo.org/wiki/Wlroots "Wlroots") library is used as a common base by a number of compositors, including [Sway](https://wiki.gentoo.org/wiki/Sway "Sway") (from which it was originally derived), dwl, and [Wayfire](https://wiki.gentoo.org/wiki/Wayfire "Wayfire"). Neither [Mutter](https://wiki.gentoo.org/wiki/Mutter "Mutter"), the GNOME Wayland compositor, nor [KWin](https://wiki.gentoo.org/wiki/KWin "KWin"), the KDE Wayland compositor, use wlroots; both are independent implementations.

## [Installation]

### [USE flags]

#### [Global]

Several packages are aware of the global [[[wayland]](https://packages.gentoo.org/useflags/wayland)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag").

#### [Local]

### [USE flags for] [dev-libs/wayland](https://packages.gentoo.org/packages/dev-libs/wayland) [[]] [Wayland protocol libraries]

  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`doc`](https://packages.gentoo.org/useflags/doc)           Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`selinux`](https://packages.gentoo.org/useflags/selinux)   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`test`](https://packages.gentoo.org/useflags/test)         Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-24 21:30] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask dev-libs/wayland`

## [Toolkit support]

### [GTK]

Wayland is completely supported in [GTK](https://wiki.gentoo.org/wiki/GTK "GTK") 3.22^[\[2\]](#cite_note-2)^. Nevertheless, when porting application in general two issues must be considered:

-   Ensure that the application uses gtk+-3.0 for its pkg-config request.
-   All calls to the gdk_x11\_ namespace and raw Xlib calls must be wrapped in [build-time and run-time backend checks](https://developer.gnome.org/gtk3/stable/ch26s02.html#id-1.6.3.4.9).

More details including plans and progress can be found on the [GNOME wiki](https://wiki.gnome.org/Initiatives/Wayland/GTK%2B).

### [Qt]

For [Qt](https://wiki.gentoo.org/wiki/Qt "Qt") an additional package called [[[dev-qt/qtwayland]](https://packages.gentoo.org/packages/dev-qt/qtwayland)[]] is required. In the Qt Wiki it says: \"QtWayland is a Qt 5 module that wraps the functionality of Wayland. QtWayland is separated into a client and server side. The client side is the wayland platform plugin, and provides a way to run Qt applications as Wayland clients. The server side is the QtCompositor API, and allows users to write their own Wayland compositors.\" To run all Qt applications on the Wayland backend, the environment variable `QT_QPA_PLATFORM=wayland` needs to be set. This is not necessary if using the Wayland version of KDE Plasma.

Porting Qt applications is much easier than GTK applications. More information on how to use QtWayland can be found at [https://wiki.qt.io/Qtwayland](https://wiki.qt.io/Qtwayland) and at [https://wayland.freedesktop.org/qt5.html](https://wayland.freedesktop.org/qt5.html).

## [Running X-only applications via Xwayland]

Some applications do not yet support running on Wayland. [[[Xwayland(1)]](https://man.archlinux.org/man/Xwayland.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] is an X server that runs as a Wayland client, allowing the use of X-only applications in a Wayland environment. For further information, please refer to the [Xwayland](https://wiki.gentoo.org/wiki/Xwayland "Xwayland") page.

Additionally, some X-only GTK applications might require the `GDK_BACKEND` environment variable to be set to `x11` rather than `wayland`:

`user `[`$`]`GDK_BACKEND=x11 ./start-tor-browser.desktop`

To check the current value of `GDK_BACKEND`, run:

`user `[`$`]`env | grep GDK_BACKEND`

    GDK_BACKEND=wayland

More generally, to check which programs are running as X clients, install the [xlsclients] package:

`root `[`#`]`emerge --ask x11-apps/xlsclients`

then run [[[xlsclients(1)]](https://man.archlinux.org/man/xlsclients.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]:

`user `[`$`]`xlsclients`

    localhost java

## [Wayback]

[Wayback](https://gitlab.freedesktop.org/wayback/wayback) is an (experimental as of 2025-09-17) X11 compatibility layer which

> allows for running full X11 desktop environments using Wayland components. It is essentially a stub compositor which provides just enough Wayland capabilities to host a rootful Xwayland server.
>
> It is intended to eventually replace the classic X.Org server, thus reducing maintenance burden of X11 applications, but a lot of work needs to be done first.
>
> Wayback is an experimental state: expect breaking changes, and lots of bugs. Please submit pull requests fixing bugs instead of bug reports if you are able.

## [Wayland over a network]

-   [[[waypipe(1)]](https://man.archlinux.org/man/waypipe.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")], provided by the [[[gui-apps/waypipe]](https://packages.gentoo.org/packages/gui-apps/waypipe)[]] package, is a transparent proxy for Wayland applications, intended to provide behavior analogous to that of `ssh -X` in an X context.

<!-- -->

-   [[[wayvnc(1)]](https://man.archlinux.org/man/wayvnc.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")], provided by the [[[gui-apps/wayvnc]](https://packages.gentoo.org/packages/gui-apps/wayvnc)[]] package, is a VNC server for wlroots-based Wayland compositors, such as Sway, Hyprland, Wayfire, Hikari, and dwl. For example, [Wayland over SSH](https://wiki.gentoo.org/wiki/User:AdaptL/Wayland_Over_SSH "User:AdaptL/Wayland Over SSH")

## [][Running Wayland/X11 applications as a different user]

Assume Wayland is run by \<host user\>, and \<guest\> wants to run a Wayland/X11 application in that Wayland instance.

### [Wayland applications]

For a pure Wayland application, the procedure is relatively simple:

1\. In this step the environment variables `XDG_RUNTIME_DIR` and `WAYLAND_DISPLAY` refer to those of the \<host\> user.

The \<guest\> user needs the permissions `rx` to the directory [\$], the permissions `rwx` to the socket [\$/\$], and the permissions `rw` to the lockfile [\$/\$.lock].

If the filesystem supports ACLs and [[[virtual/acl]](https://packages.gentoo.org/packages/virtual/acl)[]] is installed, this can be done as the original user with the commands:

`user `[`$`]`setfacl -m <guest username>:r-x -- "$"`

`user `[`$`]`setfacl -m <guest username>:rwx -- "$/$"`

`user `[`$`]`setfacl -m <guest username>:rw -- "$/$.lock"`

2\. As the \<guest\> user, export the path to the \<host\> socket as `WAYLAND_DISPLAY`:

[CODE]

    export WAYLAND_DISPLAY=/path/to/original_XDG_RUNTIME_DIR/original_WAYLAND_DISPLAY

Both are done by default if [[[app-admin/sudox::mv]](https://gpo.zugaina.org/Overlays/mv/app-admin/sudox)[]] from the mv overlay is used to change the user permissions.

### [X applications]

For an X11 application, things are more complicated: As for native X11, you have to export the MIT cookies. This can be done by using [[[app-admin/sudox::mv]](https://gpo.zugaina.org/Overlays/mv/app-admin/sudox)[]] to change the user or by copying or giving access to the [\~/.Xauthority] file.

Unfortunately, many compositors do not start Xwayland with support for cookies: Depending on the compositor, it might be necessary to generate the [\~/.Xauthority] file manually on startup and to run Xwayland with `-auth` [\~/.Xauthority] as the first option (after the display name).

The already mentioned [[[app-admin/sudox::mv]](https://gpo.zugaina.org/Overlays/mv/app-admin/sudox)[]] provides corresponding startup scripts and desktop files for wayfire.

## [Troubleshooting]

### [Setting the screen resolution]

If the resolution is not properly detected and cannot be changed from the desktop environment\'s settings, try to add this to the grub cmdline under /etc/default/grub (change the resolution and depth accordingly like this widthxheightxdepth):

[FILE] **`/etc/default/grub`**

    GRUB_GFXMODE=1680x1050x24
    GRUB_GFXPAYLOAD_LINUX=keep

Then update grub:

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

Then reboot.

If that does not work, modify `GRUB_CMDLINE_LINUX_DEFAULT` and repeat the process:

[FILE] **`/etc/default/grub`**

    GRUB_CMDLINE_LINUX_DEFAULT="video=VGA-1:1920x1080@60"

Change `VGA-1` to `HDMI-1`, `DVI-0`, `DP-1` or whatever connector the monitor using in the system as well as the resolution and refresh rates.

** Note**\
If you are running the sway compositor, you can instead specify your ideal resoultion with the \`mode\` argument under the \`output\` block of whatever the name of your display is in your sway configuration like so:

[CODE] **Change Resolution in Sway**

    output HDMI-A-1

For login mangers like SDDM which use xorg, it may be necessary to edit the xorg resolution as specified under [Xorg/Guide#Setting the screen resolution](https://wiki.gentoo.org/wiki/Xorg/Guide#Setting_the_screen_resolution "Xorg/Guide").

## [See also]

-   [List of software for Wayland](https://wiki.gentoo.org/wiki/List_of_software_for_Wayland "List of software for Wayland") --- various desktop related packages for Wayland - For desktop related softwares.
-   [Xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg") --- an open source implementation of the [X server](https://wiki.gentoo.org/wiki/X_server "X server").
-   Sakaki\'s EFI Install Guide --- includes a tutorial-style chapter covering the installation of GNOME over Wayland ([[systemd] version](https://wiki.gentoo.org/wiki/User:Sakaki/Sakaki%27s_EFI_Install_Guide/Setting_up_the_GNOME_3_Desktop "User:Sakaki/Sakaki's EFI Install Guide/Setting up the GNOME 3 Desktop"), [[OpenRC] version](https://wiki.gentoo.org/wiki/User:Sakaki/Sakaki%27s_EFI_Install_Guide/Setting_up_the_GNOME_3_Desktop_under_OpenRC "User:Sakaki/Sakaki's EFI Install Guide/Setting up the GNOME 3 Desktop under OpenRC")).

## [External resources]

-   [The Wayland Protocol](https://wayland-book.com/) - Online book describing the Wayland protocol
-   [\"The Real Story Behind Wayland and X\"](https://www.youtube.com/watch?v=RIctzAQOe44) - YouTube video of 2013 presentation by former Xorg developer Daniel Stone ([PDF of presentation slides](https://people.freedesktop.org/~daniels/lca2013-wayland-x11.pdf))
-   [Archlinux wiki article](https://wiki.archlinux.org/index.php/Wayland)
-   [Qt support](https://wiki.qt.io/Qtwayland)
-   [GTK support](https://wiki.gnome.org/Initiatives/Wayland/GTK%2B)
-   [Wayland Known Significant Issues](https://community.kde.org/Plasma/Wayland_Known_Significant_Issues) - KDE community wiki page about bugs and inconveniences in Wayland
-   [\"Towards running a Wayland Compositor on OpenBSD\"](https://2023.eurobsdcon.org/slides/eurobsdcon2023-matthieu_herrb-wayland-openbsd.pdf) - PDF of slides of 2023 presentation by Xorg developer Matthieu Herrb
-   [\[GNOME\] X11 Session Removal FAQ](https://blogs.gnome.org/alatiera/2025/06/23/x11-session-removal-faq/) - Updated 2025-06-23; includes answers to questions such as \"Is Xorg unmaintained and abandoned?\"
-   [Wayland Is Growing Up. And Now We Don't Have a Choice](https://fireborn.mataroa.blog/blog/i-want-to-love-linux-it-doesnt-love-me-back-post-4-wayland-is-growing-up-and-now-we-dont-have-a-choice/) - Posted 2025-06-19; a review of the current state of Wayland from the perspective of someone with accessibility requirements

## [References]

1.  [[[↑](#cite_ref-1)] [[Wayland](https://wayland.freedesktop.org/). Accessed on 2024-03-28.]]
2.  [[[↑](#cite_ref-2)] [[https://wiki.gnome.org/Projects/GTK/Roadmap](https://wiki.gnome.org/Projects/GTK/Roadmap)]]