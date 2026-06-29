[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Qtile&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](http://www.qtile.org/)

[[]][Official documentation](http://docs.qtile.org/en/latest/)

[[]][Package information](https://packages.gentoo.org/packages/x11-wm/qtile)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Qtile "wikipedia:Qtile")

[[]][GitHub](https://github.com//qtile/qtile)

[[]][[#qtile](ircs://irc.libera.chat/#qtile)] ([[webchat](https://web.libera.chat/#qtile)])

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/qtile)

**Qtile** is an open-source tiling [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager") that is written in, and extended with, the [Python](https://wiki.gentoo.org/wiki/Python "Python") programming language.

It can be used as an X11 window manager or a Wayland compositor.

** Note**\
Please refer to this [discussion](https://github.com/qtile/qtile/discussions/2409) to see the current state of development of the Wayland backend.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Qtile as a Wayland Compositor]](#Qtile_as_a_Wayland_Compositor)
    -   [[2.1] [Support for X11 applications (XWayland)]](#Support_for_X11_applications_.28XWayland.29)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Starting as an X11 window manager]](#Starting_as_an_X11_window_manager)
    -   [[3.2] [Starting as a Wayland compositor]](#Starting_as_a_Wayland_compositor)
    -   [[3.3] [Configuration file]](#Configuration_file)

## [Installation]

### [USE flags]

Qtile currently has no package-specific USE flags.

Apply these USE flags before emerging Qtile:

`root `[`#`]`echo x11-libs/cairo X glib opengl svg >> /etc/portage/package.use/qtile`

### [Emerge]

Then emerge Qtile:

`root `[`#`]`emerge --ask x11-wm/qtile`

## [Qtile as a Wayland Compositor]

** Note**\
Qtile requires [dev-python/pywlroots](https://github.com/bsd-ac/wayland-desktop/tree/master/dev-python/pywlroots), [dev-python/pywayland](https://github.com/bsd-ac/wayland-desktop/tree/master/dev-python/pywayland), and [dev-python/python-xkbcommon](https://github.com/bsd-ac/wayland-desktop/tree/master/dev-python/python-xkbcommon) to be installed for Wayland support, however pywayland, and python-xkbcommon are dependencies of pywlroots hence emerging the latter is enough.

These packages are found in the overlay [wayland-desktop](https://github.com/bsd-ac/wayland-desktop), please refer to [Wayland Desktop Landscape](https://wiki.gentoo.org/wiki/Wayland_Desktop_Landscape "Wayland Desktop Landscape") for more information about said overlay.

Emerge pywlroots :

`root `[`#`]`emerge --ask dev-python/pywlroots`

### [][Support for X11 applications (XWayland)]

** Note**\
Support for XWayland also requires [gui-libs/wlroots](https://packages.gentoo.org/packages/gui-libs/wlroots) and pywlroots to be built with XWayland support which at the time of writing pywlroots already do.

Emerge XWayland:

`root `[`#`]`emerge --ask x11-base/xwayland`

## [Configuration]

### [Starting as an X11 window manager]

Start Qtile using a [display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager") or the [startx] command.

If want to use startx and want [elogind](https://wiki.gentoo.org/wiki/Elogind "Elogind") support, setup ConsoleKit and create the following file:

[FILE] **`~/.xinitrc`**

    exec dbus-launch --sh-syntax --exit-with-session qtile start

### [Starting as a Wayland compositor]

Start qtile from a command line using:

`user `[`$`]`qtile start -b wayland`

Or start Qtile using [display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager") by creating a session file:

[FILE] **`/usr/share/wayland-sessions/qtile-wayland.desktop`**

    [Desktop Entry]
    Name=Qtile (Wayland)
    Comment=Qtile Session
    Exec=qtile start -b wayland
    Type=Application
    Keywords=wm;tiling

### [Configuration file]

Qtile can be customized by editing the config file in [\~/.config/qtile/config.py]. This file is generated when there is no present configuration file. If Qtile is running while configuring it, restart Qtile using its default keybind, [Super]+[Ctrl]+[R] to apply changes.

The default configuration file can be found at [https://github.com/qtile/qtile/blob/master/libqtile/resources/default_config.py](https://github.com/qtile/qtile/blob/master/libqtile/resources/default_config.py).

To check if the changes are written correctly:

`user `[`$`]`python3 -m py_compile ~/.config/qtile/config.py`