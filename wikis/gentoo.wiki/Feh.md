**Resources**

[[]][Home](https://feh.finalrewind.org/)

[[]][GitHub](https://github.com/derf/feh)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/feh)

[[]][[#feh](ircs://irc.libera.chat/#feh)] ([[webchat](https://web.libera.chat/#feh)])

[[]][Package information](https://packages.gentoo.org/packages/media-gfx/feh)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Feh "wikipedia:Feh")

**feh** is an open-source image viewer that is mainly aimed at command-line users. It can be used to view images on disk or, more often, for setting the desktop background for tiling [window managers](https://wiki.gentoo.org/wiki/Window_managers "Window managers") like [i3](https://wiki.gentoo.org/wiki/I3 "I3"). It has several command line options to change the behavior for either of these uses, mostly entered around how to resize the image for the view.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Setting backgrounds]](#Setting_backgrounds)
    -   [[2.2] [Viewing images]](#Viewing_images)
-   [[3] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [media-gfx/feh](https://packages.gentoo.org/packages/media-gfx/feh) [[]] [A fast, lightweight imageviewer using imlib2]

  ------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`curl`](https://packages.gentoo.org/useflags/curl)           Add support for client-side URL transfer library
  [`debug`](https://packages.gentoo.org/useflags/debug)         Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`exif`](https://packages.gentoo.org/useflags/exif)           Add support for reading EXIF headers from JPEG and TIFF images
  [`inotify`](https://packages.gentoo.org/useflags/inotify)     Enable inotify filesystem monitoring support
  [`magic`](https://packages.gentoo.org/useflags/magic)         Use libmagic from sys-apps/file to filter unsupported file formats
  [`test`](https://packages.gentoo.org/useflags/test)           Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`xinerama`](https://packages.gentoo.org/useflags/xinerama)   Add support for querying multi-monitor screen geometry through the Xinerama API
  ------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-10 04:12] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[media-gfx/feh]](https://packages.gentoo.org/packages/media-gfx/feh)[]]:

`root `[`#`]`emerge --ask media-gfx/feh`

## [Usage]

### [Setting backgrounds]

To use it to set one\'s desktop background to a scaled version of a wallpaper:

`user `[`$`]`feh --bg-scale /path/to/wallpaper`

where [/path/to/wallpaper] is the path to the wallpaper one wishes to use as desktop background. Likewise to set the desktop background to a tiled version of the wallpaper:

`user `[`$`]`feh --bg-tile /path/to/wallpaper`

Adding these commands to [\~/.xsession] is an easy way to have the wallpaper set when X is started. Alternatively cron can be used to change the background in a time interval:

`user `[`$`]`crontab -e`

[CODE]

    */5 *  *  * * DISPLAY=":0.0" feh --randomize --bg-fill /path/to/wallpaper_library

This will run feh every 5 minutes, and every time randomly chooses a picture from the directory [/path/to/wallpaper_library]. The environment variable `DISPLAY` must be set inside of cron because cron was started before X. For more help with automated tasks on intervals, see the page for [cron](https://wiki.gentoo.org/wiki/Cron "Cron").

### [Viewing images]

feh can also be used as a standalone image viewer. feh can accept a single image, a number of images, or a directory as input.

`user `[`$`]`feh /path/to/image`

`user `[`$`]`feh /path/to/directory`

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------
  Control                                                                                                                                                              Action
  [↑]   Zoom In
  [↓]   Zoom Out
  [←]   Previous Image
  [→]   Next Image
  Left Mouse Drag                                                                                                                                                      Pans the Image
  Right Mouse Click                                                                                                                                                    Secondary Menu
  [+]   Zoom In
  [-]   Zoom Out
  Scroll Up                                                                                                                                                            Previous Picture
  Scroll Down                                                                                                                                                          Next Picture
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------

For further details on its usage see [The ArchWiki\'s article on feh](https://wiki.archlinux.org/index.php/feh#Usage).

## [See also]

-   [Imv](https://wiki.gentoo.org/wiki/Imv "Imv") --- a free and open-source simple image viewer for [X11](https://wiki.gentoo.org/wiki/X11 "X11") and [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland").