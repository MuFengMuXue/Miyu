**Resources**

[[]][GitHub](https://github.com/WayfireWM/wayfire)

[[]][Home](https://wayfire.org/)

[[]][[#wayfire](ircs://irc.libera.chat/#wayfire)] ([[webchat](https://web.libera.chat/#wayfire)])

Wayfire is a Wayland compositor inspired by Compiz and based on [wlroots](https://wiki.gentoo.org/wiki/Wlroots "Wlroots").

Wayfire aims to create a customizable, extendable and lightweight environment without sacrificing its appearance. It features a lot of graphical effects, such as the desktop cube, wobbly windows, fire animation, fish eye, workspace scale view and window rotations, among many other features.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Manual configuration]](#Manual_configuration)
        -   [[2.1.1] [Plugins]](#Plugins)
        -   [[2.1.2] [Shortcuts]](#Shortcuts)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Supported Wayland protocols]](#Supported_Wayland_protocols)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [gui-wm/wayfire](https://packages.gentoo.org/packages/gui-wm/wayfire) [[]] [compiz like 3D wayland compositor]

  --------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+dbus`](https://packages.gentoo.org/useflags/+dbus)     Enable dbus support for anything that needs it (gpsd, gnomemeeting, etc)
  [`+gles3`](https://packages.gentoo.org/useflags/+gles3)   Enable OpenGL ES 3.x Features.
  [`X`](https://packages.gentoo.org/useflags/X)             Enable support for X11 applications (XWayland).
  [`openmp`](https://packages.gentoo.org/useflags/openmp)   Build support for the OpenMP (support parallel computing), requires \>=sys-devel/gcc-4.2 built with USE=\"openmp\"
  [`test`](https://packages.gentoo.org/useflags/test)       Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  --------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-01-20 05:58] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask gui-wm/wayfire`

## [Configuration]

The default configuration file is [\~/.config/wayfire.ini] but Wayfire also supports loading custom configuration files. A graphical interface for configuration is provided by the optional package [gui-apps/wcm](https://packages.gentoo.org/packages/gui-apps/wcm).

-   ::::::
    ::::
    :::
    [![](/images/thumb/f/f1/Wayfire1.png/120px-Wayfire1.png)](https://wiki.gentoo.org/wiki/File:Wayfire1.png)
    :::
    ::::

    ::: gallerytext
    Wayfire demo
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/8/87/Wayfire2.png/120px-Wayfire2.png)](https://wiki.gentoo.org/wiki/File:Wayfire2.png)
    :::
    ::::

    ::: gallerytext
    Wayfire demo
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/7/7b/Wayfire3.png/120px-Wayfire3.png)](https://wiki.gentoo.org/wiki/File:Wayfire3.png)
    :::
    ::::

    ::: gallerytext
    Wayfire demo
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/9/9d/Wayfire4.png/120px-Wayfire4.png)](https://wiki.gentoo.org/wiki/File:Wayfire4.png)
    :::
    ::::

    ::: gallerytext
    Wayfire demo
    :::
    ::::::

** Important**\
[[[gui-apps/wcm]](https://packages.gentoo.org/packages/gui-apps/wcm)[]] overwrites current configuration file.

### [Manual configuration]

Copy over the default configuration from [/usr/share/wayfire] like so:

`user `[`$`]`cp /usr/share/wayfire/wayfire.ini ~/.config/`

#### [Plugins]

Wayfire plugins can be enabled and disabled via adding and removing entries in the `plugins =` in the **`[core]`** section of [\~/.config/wayfire.ini].

For example, to remove the `wrot` plugin which allows for window rotation, comment it out in [\~/.config/wayfire.ini] by adding `#` as the *first* character of the line:

[FILE] **`~/.config/wayfire.ini`**

    [core]
    plugins = \
      alpha \
      animate \
      autostart \
      command \
      cube \
      decoration \
      expo \
      fast-switcher \
      fisheye \
      foreign-toplevel \
      grid \
      gtk-shell \
      idle \
      invert \
      move \
      oswitch \
      place \
      resize \
      switcher \
      vswitch \
      window-rules \
      wm-actions \
      wobbly \
    #  wrot \
      zoom

To install extra plugins, emerge the [[[gui-libs/wayfire-plugins-extra]](https://packages.gentoo.org/packages/gui-libs/wayfire-plugins-extra)[]] package:

`root `[`#`]`emerge --ask gui-libs/wayfire-plugins-extra`

#### [Shortcuts]

** Important**\
Prior to 0.9.0, keybindings had to use evdev codes; refer to the relevant link in the \"[External resources](#External_resources)\" section. Since 0.9.0, one can use the `xkb-bindings` plugin to allow the use of xkb keysyms instead.

External shortcuts in Wayfire are managed by the `command` plugin. A custom keybinding requires two things:

-   A `binding_`- or `repeatable_binding_`-prefixed variable.
-   A `command_`-prefixed variable.

The `repeatable_binding_` prefix assumes that the key in question is going to be held down.

Available meta keys include:

-   `<super>`
-   `<alt>`
-   `<shift>`

As an example, to add a keybinding to start Firefox by pressing `<super>-<shift>-1`:

[FILE] **`~/.config/wayfire.ini`**

    binding_firefox = <super> <shift> KEY_1
    command_firefox = firefox

The order and name of the variables doesn\'t matter, as long as the `binding_`- and `command_`-prefixed variables have the same suffix, e.g. `binding_x`, `command_x`. Note that an underscore, `_`, must be used as the separator.

## [Usage]

Wayfire is only a Wayland compositor and does not provide the full capabilities expected from a [desktop environment](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment"). It is best used alongside [gui-apps/wf-shell](https://packages.gentoo.org/packages/gui-apps/wf-shell), which adds among other features a GTK3-based status bar and wallpaper support.

Wayfire needs additional applications which implement other parts of the XDG specifications from Freedesktop, such as desktop notifications, application launchers, screenshotting, screen recording and screen locking among other important necessities; refer to the [List of software for Wayland](https://wiki.gentoo.org/wiki/List_of_software_for_Wayland "List of software for Wayland") article for examples.

### [Supported Wayland protocols]

For information about Wayland protocols supported by Wayfire, refer to the [Wayfire/Wayland protocols](https://wiki.gentoo.org/wiki/Wayfire/Wayland_protocols "Wayfire/Wayland protocols") page.

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose gui-wm/wayfire`

## [See also]

-   [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") --- a [communication protocol](https://en.wikipedia.org/wiki/communication_protocol "wikipedia:communication protocol") between a [display server](https://en.wikipedia.org/wiki/display_server "wikipedia:display server") and its clients
-   [List of software for Wayland](https://wiki.gentoo.org/wiki/List_of_software_for_Wayland "List of software for Wayland") --- various desktop related packages for Wayland

## [External resources]

-   [Official wiki home](https://github.com/WayfireWM/wayfire/wiki/)
-   [pywayfire](https://github.com/WayfireWM/pywayfire) - Python binding