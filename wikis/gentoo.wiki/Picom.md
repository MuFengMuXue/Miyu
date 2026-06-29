[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Picom&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://github.com/yshui/picom)

[[]][Package information](https://packages.gentoo.org/packages/x11-misc/picom)

[[]][GitHub](https://github.com/yshui/picom)

[[]][Official documentation](https://github.com/yshui/picom/wiki)

**picom** is a lightweight compositor for [X11](https://wiki.gentoo.org/wiki/X11 "X11"). It was forked from the original Compton because it seems to have become unmaintained^[\[1\]](#cite_note-1)^.

There are three different render backends available: *glx*, *xrender*, and *xr_glx_hybrid*, with the first one being the preferred and performant option ^[\[2\]](#cite_note-2)^.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
-   [[3] [Usage]](#Usage)
-   [[4] [Tips]](#Tips)
-   [[5] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [x11-misc/picom](https://packages.gentoo.org/packages/x11-misc/picom) [[]] [A lightweight compositor for X11 (previously a compton fork)]

  --------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+doc`](https://packages.gentoo.org/useflags/+doc)       Build documentation and man pages (requires app-text/asciidoc)
  [`+drm`](https://packages.gentoo.org/useflags/+drm)       Enable support for using drm for vsync
  [`dbus`](https://packages.gentoo.org/useflags/dbus)       Enable dbus support for anything that needs it (gpsd, gnomemeeting, etc)
  [`opengl`](https://packages.gentoo.org/useflags/opengl)   Enable features that require opengl (opengl backend, and opengl vsync methods)
  [`pcre`](https://packages.gentoo.org/useflags/pcre)       Add support for Perl Compatible Regular Expressions
  [`test`](https://packages.gentoo.org/useflags/test)       Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  --------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-31 19:54] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask x11-misc/picom`

## [Configuration]

Configuration file can be specified by the `--config` parameter. By default, the configuration file is read from locations listed below.

An on-change configuration autoload is supported.

### [Files]

If no `--config` parameter is provided the following files are searched for in the following order.

-   [\$XDG_CONFIG_HOME/picom.conf] - Local (per user) configuration file.
-   [\$XDG_CONFIG_HOME/picom/picom.conf] - Local (per user) configuration file.
-   [\$XDG_CONFIG_DIRS/picom.conf] - Global (system wide) configuration file.
-   [\$XDG_CONFIG_DIRS/picom/picom.conf] - Global (system wide) configuration file.

\
The [XDG/Base Directories](https://wiki.gentoo.org/wiki/XDG/Base_Directories "XDG/Base Directories") defines `$XDG_CONFIG_HOME` (`~/.config`) and `$XDG_CONFIG_DIRS` (`/etc/xdg`).

** Important**\
The Picom configuration files do not exist by default; They must be created manually, or by copying the sample configuration.

Sample configuration file:

-   [/usr/share/doc/picom-/picom.sample.conf.bz2]

It can be copied to one of the above mentioned locations, and modified as wanted.

`user `[`$`]`mkdir --verbose --parents ~/.config/picom`

    mkdir: created directory '/home/user/.config/picom

`user `[`$`]`bzcat --verbose /usr/share/doc/picom-12.5/picom.sample.conf.bz2 > ~/.config/picom/picom.conf`

    /usr/share/doc/picom-12.5/picom.sample.conf.bz2: done

## [Usage]

It can be started as a background process:

`user `[`$`]`picom --daemon`

To start Picom without an existing configuration file, the `--backend` parameter is mandatory:

`user `[`$`]`picom --backend [ xrender | glx | xr_glx_hybrid ]`

\

## [Tips]

For those using [Dwm](https://wiki.gentoo.org/wiki/Dwm "Dwm") and dmenu, it is possible to exclude the status bar from rules. For example, to exclude dwm status bar from having corner radius:

[FILE] **`~/.config/picom/picom.conf`**

    rules: ()

Similarly, dmenu can also be matched with \"class_i = \'dmenu\'\".

## [References]

1.  [[[↑](#cite_ref-1)] [[\[1\]](https://github.com/chjj/compton/commit/master), Last commit to master on April 30, 2017. Retrieved on March 10, 2021]]
2.  [[[↑](#cite_ref-2)] [[Backends · yshui/picom Wiki](https://github.com/yshui/picom/wiki/Backends#choosing-a-backend), GitHub. Retrieved on June 18, 2025]]