[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=LXDE&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

*Not to be confused with [the LXD container manager](https://wiki.gentoo.org/wiki/LXD "LXD").*

**Resources**

[[]][Home](https://lxde.org/)

[[]][Package information](https://packages.gentoo.org/packages/lxde-base/lxde-meta)

[[]][Wikipedia](https://en.wikipedia.org/wiki/LXDE "wikipedia:LXDE")

[[]][GitWeb](https://git.lxde.org/gitweb/)

[[]][Bugs (upstream)](https://sourceforge.net/p/lxde/bugs/)

**LXDE** (abbreviation for **L**ightweight **X**11 **D**esktop **E**nvironment) is a free desktop environment with comparatively low resource requirements.

This guide introduces the user to LXDE (the Lightweight X11 Desktop Environment), explains its components, and leads the user through the installation.

## Contents

-   [[1] [Concepts]](#Concepts)
    -   [[1.1] [What is LXDE?]](#What_is_LXDE.3F)
    -   [[1.2] [Components of LXDE]](#Components_of_LXDE)
        -   [[1.2.1] [Core components]](#Core_components)
        -   [[1.2.2] [Other applications used by LXDE]](#Other_applications_used_by_LXDE)
        -   [[1.2.3] [Additional applications LXDE can use]](#Additional_applications_LXDE_can_use)
-   [[2] [Installation]](#Installation)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [GTK icon warning]](#GTK_icon_warning)
    -   [[3.2] [Right-click menu]](#Right-click_menu)
    -   [[3.3] [Taking screenshots with xwd]](#Taking_screenshots_with_xwd)
    -   [[3.4] [Lightweight screen lock and screensaver]](#Lightweight_screen_lock_and_screensaver)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

### [Concepts]

#### [][What is LXDE?]

After installing a base Gentoo system, and the [X server](https://wiki.gentoo.org/wiki/X_server "X server"), there are many choices to consider regarding which graphical environment will be best to use. There are many options available, ranging from minimalistic window managers like [Openbox](https://wiki.gentoo.org/wiki/Openbox "Openbox"), to full-featured [desktop environments](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") like [KDE](https://wiki.gentoo.org/wiki/KDE "KDE"), and [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME").

Some users might like having a lightweight graphical environment, but do not wish to install and configure every component individually like with Openbox. For quite some time users in this position would install [Xfce](https://wiki.gentoo.org/wiki/Xfce "Xfce") because it fit the description of a lightweight environment and came with a suite of lightweight applications. While Xfce provides a full-featured environment without the extensive resource usage of KDE or GNOME, it has the potential to lean towards the heavy side. At last an alternative to Xfce has been created: the Lightweight X11 Desktop Environment, or [LXDE] for short.

Users however who dislike all those dependencies ([dbus](https://wiki.gentoo.org/wiki/Dbus "Dbus"), [polkit](https://wiki.gentoo.org/wiki/Polkit "Polkit"), \...) inevitably pulled in by lxsession should have a look at [Lumina](https://wiki.gentoo.org/wiki/Lumina "Lumina").

#### [Components of LXDE]

LXDE, being a desktop environment, is comprised of several components. Each program offers a certain functionality; together they form a complete desktop environment. Currently there are eleven core components and several other programs necessary to make a complete LXDE installation. These programs are the ones pulled in by the [[[lxde-base/lxde-meta]](https://packages.gentoo.org/packages/lxde-base/lxde-meta)[]] package, discussed in the following installation section.

##### [Core components]

-   [[[lxde-base/lxappearance]](https://packages.gentoo.org/packages/lxde-base/lxappearance)[]] is a GTK theme and icon configurator that allows you to customize the look of LXDE.
-   [[[lxde-base/lxde-common]](https://packages.gentoo.org/packages/lxde-base/lxde-common)[]] is a collection of default configuration files.
-   [[[lxde-base/lxde-icon-theme]](https://packages.gentoo.org/packages/lxde-base/lxde-icon-theme)[]] is the main set of icons.
-   [[[lxde-base/lxmenu-data]](https://packages.gentoo.org/packages/lxde-base/lxmenu-data)[]] is the application menu manager.
-   [[[lxde-base/lxinput]](https://packages.gentoo.org/packages/lxde-base/lxinput)[]] is a keyboard and mouse configurator.
-   [[[lxde-base/lxpanel]](https://packages.gentoo.org/packages/lxde-base/lxpanel)[]] is the panel that includes the application menu, system tray, and clock.
-   [[[lxde-base/lxrandr]](https://packages.gentoo.org/packages/lxde-base/lxrandr)[]] is a graphical interface to X Resize and Rotate, allowing for display manipulation.
-   [[[lxde-base/lxsession]](https://packages.gentoo.org/packages/lxde-base/lxsession)[]] is a session manager, providing options to shutdown, reboot, and suspend the system.
-   [[[lxde-base/lxsession-edit]](https://packages.gentoo.org/packages/lxde-base/lxsession-edit)[]] allows you to enable / disable applications at startup.
-   [[[lxde-base/lxshortcut]](https://packages.gentoo.org/packages/lxde-base/lxshortcut)[]] is an easy way to edit application shortcuts, especially for desktop icons.
-   [[[lxde-base/lxtask]](https://packages.gentoo.org/packages/lxde-base/lxtask)[]] is the task manager used to view / edit running services and programs.
-   [[[lxde-base/lxterminal]](https://packages.gentoo.org/packages/lxde-base/lxterminal)[]] is the vte-based tabbed terminal emulator.

##### [Other applications used by LXDE]

-   [openbox](https://wiki.gentoo.org/wiki/Openbox "Openbox") --- a highly configurable stacking [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager") for [X11](https://wiki.gentoo.org/wiki/X11 "X11") with extensive standards support.
-   [PCManFM](https://wiki.gentoo.org/wiki/PCManFM "PCManFM") --- a powerful yet lightweight file manager application, default file manager of [LXDE].
-   [[[x11-misc/obconf]](https://packages.gentoo.org/packages/x11-misc/obconf)[]] is the configurator for OpenBox, allowing you to change window decorations and more.
-   [[[media-gfx/gpicview]](https://packages.gentoo.org/packages/media-gfx/gpicview)[]] is the default image viewer.

##### [Additional applications LXDE can use]

-   Text Editors: [app-editors/leafpad](https://wiki.gentoo.org/wiki/Leafpad "Leafpad")
-   LXDE Display Manager: [[[lxde-base/lxdm]](https://packages.gentoo.org/packages/lxde-base/lxdm)[]]

## [Installation]

After the [X server](https://wiki.gentoo.org/wiki/X_server "X server") has been emerged and configured, LXDE is ready to be installed. While each component can be installed individually, the more efficient and typically preferred method is to emerge the meta package set:

`root `[`#`]`emerge --ask lxde-base/lxde-meta`

Upon review of the emerge command\'s output (if the current set of USE flags looks good, etc.) enter \"yes\" when prompted to emerge the packages. Just like with other desktop environments, the X Server must be told to load LXDE automatically. This is done by adding it to user\'s [\~/.xinitrc] file.

`user `[`$`]`echo "exec startlxde" >> ~/.xinitrc`

This will automatically start a LXDE session when the [[startx](https://wiki.gentoo.org/wiki/Xorg/Guide#Using_startx "Xorg/Guide")] command is typed at the console.

An error message may be seen when a session is started without [D-Bus](https://wiki.gentoo.org/wiki/D-Bus#Services "D-Bus") running and the shutdown and reboot options will not be available. This might be solved with [adding elogind](https://wiki.gentoo.org/wiki/Elogind#startx_integration "Elogind").

\

** Note**\
If a [login manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager") such as SLiM, XDM, GDM, or KDM is used then editing the [\~/.xinitrc] file is not needed. LXDE will show up as a choice on the login manager\'s screen.

** Important**\
As each user has their own [.xinitrc] file. Make sure to properly modify the file for each user for a correct setup. This process involves using the [su] command to change to each user\'s account or another safe method. Using the root account for modifying [.xinitrc] files is generally not a good idea.

## [Configuration]

### [GTK icon warning]

Now that the X server knows to start LXDE type in [startx] to fire up LXDE. The first thing that may appear is a warning about an improper GTK icon set. To fix this minor hangup change the icon theme. Click on the LXDE application menu (in the lower left-hand corner of the panel), and navigate to [Preferences] \--\> [Appearance]. In the [LXappearance] menu, click on the [Icon] tab, and choose nuoveXT.2.2. Click [Apply] and then click [Close]. The next time a user logs in to LXDE the error message will not appear. Users are not limited to using the nuoveXT.2.2 icon theme. They may install any other icon theme through `LXappearance`. When other icon themes are selected the GTK icon warning will no longer appear when starting [PCManFM](https://wiki.gentoo.org/wiki/PCManFM "PCManFM").

### [Right-click menu]

In LXDE, not every appearance option is handled through LXappearance as one might believe. Rather, there are some common options that are handled through a right-click menu on the desktop. At the bottom of that menu is the \"Desktop Settings\" menu. Here users can find icon sizes, single-click and double-click behavior, maximum thumbnail size, and desktop wallpaper settings. It may behoove one to look through the these tabs for additional appearance settings. It can be quite confusing.

** Note**\
These \"Desktop Settings\" can also be found by opening up the PCManFM file manager, and navigating to [Edit] \--\> [Preferences]

### [Taking screenshots with xwd]

There are many ways to take screenshots in LXDE, but all methods require some work in order for them to operate as desired. The solution below uses xwd to capture screenshots, imagemagick convert to save them to png, and notify-send to send a notification to desktop.

See [[[x11-apps/xwd]](https://packages.gentoo.org/packages/x11-apps/xwd)[]], [[[media-gfx/imagemagick]](https://packages.gentoo.org/packages/media-gfx/imagemagick)[]], [[[xfce-extra/xfce4-notifyd]](https://packages.gentoo.org/packages/xfce-extra/xfce4-notifyd)[]].

It will place the screenshots in [\$HOME/screenshots/]

First create key bindings:

[FILE] **`~/.config/openbox/lxde-rc.xml`**

    ...
    </keyboard>
      ...
      <keybind key="Print">
        <action name="Execute">
          <command>/usr/local/bin/screenshot.sh</command>
        </action>
      </keybind>
      <keybind key="A-Print">
        <action name="Execute">
          <command>/usr/local/bin/screenshot.sh window</command>
        </action>
      </keybind>
      ...
    </keyboard>
    ...

Then create and make executable the following simple script:

[FILE] **`/usr/local/bin/screenshot.sh`**

    #!/bin/bash

    FOLDER="$HOME/screenshots/"

    if [ ! -d "$" ]; then
      mkdir $
    fi

    DATE=$(date +%Y-%m-%d@%H.%M.%S)
    FNAME="$screenshot-$.png"
    C=0
    while [ -f "$" ] ; do
        FNAME="$screenshot-$.$.png"
        let C++
    done

    touch $

    if [ "$1" != "window" ]; then
      if xwd -root -screen | magick convert xwd:- "$"; then
        notify-send "Desktop screenshot saved!" "Desktop screenshot was saved as:\n $"
      else
        notify-send "Desktop screenshot could not be saved!" "There was an error."
      fi
    else
      if xwd -screen | magick convert xwd:- "$"; then
        notify-send "Window screenshot saved!" "Window screenshot was saved as:\n $"
      else
        notify-send "Window screenshot could not be saved!" "There was an error."
      fi
    fi

### [Lightweight screen lock and screensaver]

A lightweight screensaver and locker can be done with xautolock, xset, and i3lock/slock. Add the following to the [.xinitrc] file:

[FILE] **`~/.xinitrc`**

    xautolock -time 5 -locker "i3lock -c 000000" &
    xset +dpms dpms 20 100 &
    exec startlxde

The values of xset is also influenced by `BATT_DPMS_STANDBY` and its AC counterpart in [/etc/laptop-mode/conf.d/dpms-standby.conf]. If laptop-mode-tools are installed, these values could be misleading.

## [See also]

-   [Desktop environment](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") --- provides a list of desktop environments available in Gentoo.
-   [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME") --- a feature-rich desktop environment provided by the [GNOME project](https://www.gnome.org).
-   [KDE](https://wiki.gentoo.org/wiki/KDE "KDE") --- a free software community, producing a wide range of applications including the popular Plasma desktop environment.
-   [Lumina](https://wiki.gentoo.org/wiki/Lumina "Lumina") --- a lightweight [desktop environment](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment"), free of [D-Bus](https://wiki.gentoo.org/wiki/D-Bus "D-Bus") and \*kit, designed to have as few system dependencies and requirements as possible.
-   [Xfce](https://wiki.gentoo.org/wiki/Xfce "Xfce") --- a lightweight [desktop environment](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") built to be fast, good looking, and user friendly.

## [External resources]

There are many resources available regarding the various facets of the Lightweight X11 Desktop Environment. Some additional resources are listed below:

-   The [Official LXDE forums](https://forum.lxde.org/)
-   The [Official LXDE wiki](http://wiki.lxde.org/en/Main_Page) contains instructions on customizing the LXDE installation, including keyboard layouts, autostarting applications, changing the default window manager, and much more.

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **nathanzachary, yngwin, nightmorph**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*