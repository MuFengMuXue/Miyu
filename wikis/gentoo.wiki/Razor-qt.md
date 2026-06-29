**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:LXQt "Project:LXQt")][Project](https://wiki.gentoo.org/wiki/Project:LXQt "Project:LXQt")

[[]][Home](https://lxqt-project.org/)

[[]][Package information](https://packages.gentoo.org/packages/lxqt-base/lxqt-meta)

[[]][Wikipedia](https://en.wikipedia.org/wiki/LXQt "wikipedia:LXQt")

[[]][GitHub](https://github.com/lxqt/lxqt)

[[]][Bugs (upstream)](https://github.com/lxqt/lxqt/issues)

**LXQt** is a lightweight desktop environment based on the Qt toolkit. It is the result of the merge between the LXDE-Qt and the Razor-qt projects.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE Flags]](#USE_Flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Keywords]](#Keywords)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Launching LXQt]](#Launching_LXQt)
        -   [[2.1.1] [startx]](#startx)
        -   [[2.1.2] [Display manager]](#Display_manager)
    -   [[2.2] [Changing the GTK themes]](#Changing_the_GTK_themes)
    -   [[2.3] [Automounting volumes]](#Automounting_volumes)
    -   [[2.4] [Adding custom actions to PCManFM-Qt]](#Adding_custom_actions_to_PCManFM-Qt)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Applications]](#Applications)
    -   [[3.2] [Wi-Fi]](#Wi-Fi)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Support]](#Support)
-   [[5] [See also]](#See_also)

## [Installation]

### [USE Flags]

### [USE flags for] [lxqt-base/lxqt-meta](https://packages.gentoo.org/packages/lxqt-base/lxqt-meta) [[]] [Meta ebuild for LXQt, the Lightweight Desktop Environment]

  ----------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------
  [`+about`](https://packages.gentoo.org/useflags/+about)                       Install lxqt-base/lxqt-about
  [`+archiver`](https://packages.gentoo.org/useflags/+archiver)                 Install app-arch/lxqt-archiver
  [`+desktop-portal`](https://packages.gentoo.org/useflags/+desktop-portal)     Enable the LXQt sys-apps/xdg-desktop-portal backend implementation
  [`+display-manager`](https://packages.gentoo.org/useflags/+display-manager)   Install a graphical display manager
  [`+filemanager`](https://packages.gentoo.org/useflags/+filemanager)           Install x11-misc/pcmanfm-qt file manager
  [`+icons`](https://packages.gentoo.org/useflags/+icons)                       Install kde-frameworks/breeze-icons
  [`+lximage`](https://packages.gentoo.org/useflags/+lximage)                   Install media-gfx/lximage-qt image viewer
  [`+policykit`](https://packages.gentoo.org/useflags/+policykit)               Enable PolicyKit (polkit) authentication support
  [`+processviewer`](https://packages.gentoo.org/useflags/+processviewer)       Install x11-misc/qps package
  [`+screenshot`](https://packages.gentoo.org/useflags/+screenshot)             Install x11-misc/screengrab package
  [`+sddm`](https://packages.gentoo.org/useflags/+sddm)                         Install x11-misc/sddm display manager
  [`+sudo`](https://packages.gentoo.org/useflags/+sudo)                         Install lxqt-base/lxqt-sudo
  [`+terminal`](https://packages.gentoo.org/useflags/+terminal)                 Install x11-terms/qterminal package
  [`+trash`](https://packages.gentoo.org/useflags/+trash)                       Install gnome-base/gvfs to enable \'trash:///\', \'computer:///\' and other such \"places\" in x11-misc/pcmanfm-qt
  [`+window-manager`](https://packages.gentoo.org/useflags/+window-manager)     Install kde-plasma/kwin window manager
  [`admin`](https://packages.gentoo.org/useflags/admin)                         Install lxqt-base/lxqt-admin
  [`nls`](https://packages.gentoo.org/useflags/nls)                             Install dev-qt/qttranslations to better support different locales
  [`powermanagement`](https://packages.gentoo.org/useflags/powermanagement)     Install lxqt-base/lxqt-powermanagement package
  [`ssh-askpass`](https://packages.gentoo.org/useflags/ssh-askpass)             Install lxqt-base/lxqt-openssh-askpass user password prompt tool
  [`wayland`](https://packages.gentoo.org/useflags/wayland)                     Install lxqt-base/lxqt-wayland-session to support Wayland sessions
  ----------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-21 11:30] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Get the complete LXQt desktop environment by installing the [[[lxqt-base/lxqt-meta]](https://packages.gentoo.org/packages/lxqt-base/lxqt-meta)[]] package:

`root `[`#`]`emerge --ask lxqt-base/lxqt-meta`

### [Keywords]

LXQt has been stable for amd64 and x86 since version 0.13.0 so normally no keywords are needed.

However, for other architectures, it may be necessary to add a few packages to [package.accept_keywords]:

[FILE] **`/etc/portage/package.accept_keywords/lxqt`**

    lxqt-base/*
    media-gfx/lximage-qt
    x11-misc/obconf-qt
    x11-misc/pcmanfm-qt

Additional packages may need keyworded; [emerge] will provide current package keywording information if it is the case. See [accepting a keyword for a single package](https://wiki.gentoo.org/wiki/Knowledge_Base:Accepting_a_keyword_for_a_single_package "Knowledge Base:Accepting a keyword for a single package") for more information on making packages from the testing branch available.

## [Configuration]

### [Launching LXQt]

#### [startx]

To launch LXQt using the [startx] command, without a display manager, the following file can be used with or without [elogind](https://wiki.gentoo.org/wiki/Elogind "Elogind") (possibly works with [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") as well):

[FILE] **`~/.xinitrc`**

    exec startlxqt

It may be desirable to start [D-Bus](https://wiki.gentoo.org/wiki/D-Bus "D-Bus") manually, for example if notifications are not working or if there are several [dbus-launch] processes in the output from [pstree]:

[FILE] **`~/.xinitrc`**

    exec ck-launch-session dbus-launch --exit-with-session startlxqt

Alternatively, the [dbus] service can be [started at boot time](https://wiki.gentoo.org/wiki/D-Bus#Services "D-Bus").

To disable energy saver that power off display after 10 minutes of inactivity (even when watching YouTube) add this two lines:

[FILE] **`~/.xinitrc`**

    xset s off
    xset -dpms

** Note**\
Script execution will stop after the first line starting with [exec], so any other commands that should run as well will need to go **above** it.

It is possible to configure the user\'s login shell to [run startx on login](https://wiki.gentoo.org/wiki/X_without_Display_Manager#Starting_X11_automatically "X without Display Manager").

#### [Display manager]

A display manager (DM) presents the user with a graphical login screen after boot, to log into a GUI session. Some may prefer this to using startx at the terminal, or automatically launching LXQt. A DM may also be useful if multiple [desktop environments](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") or [window managers](https://wiki.gentoo.org/wiki/Window_manager "Window manager") are installed on the same machine.

Examples of display managers that will work with LXQT are [SDDM](https://wiki.gentoo.org/wiki/SDDM "SDDM"), [GDM](https://wiki.gentoo.org/wiki/GNOME/GDM "GNOME/GDM"), or [LightDM](https://wiki.gentoo.org/wiki/LightDM "LightDM").

See the [display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager") article for a list of available display managers for Gentoo. See each DMs wiki page for installation and setup instructions.

### [Changing the GTK themes]

The LXQt appearance settings GUI has no support for changing GTK themes, installing [[[lxde-base/lxappearance]](https://packages.gentoo.org/packages/lxde-base/lxappearance)[]] may be useful.

Alternatively, changing the themes manually is possible, for example using the GTK2_RC_FILES variable:

[FILE] **`~/.xinitrc`**

    export GTK2_RC_FILES=/home/user/.themes/Drakfire\ Black/gtk-2.0/gtkrc
    exec startlxqt

The [GTK page of the Arch Linux wiki](https://wiki.archlinux.org/index.php/GTK%2B) has more information for configuring GTK 2 and GTK 3 themes.

For Qt 5 applications (since the update to Qt 5.7) install [x11-themes/qtstyleplugins] from the [abendbrot] overlay to get the GTK style.

### [Automounting volumes]

By default, LXQt tries to automount every attached disk at startup and when they are plugged in. It may result in unwanted popup windows asking for the root password to mount disks.

The automount options are located in the PCManFM file manager settings:

-   In the applications menu, open **Accessories-\>PCManFM File Manager**.
-   Select the **Edit-\>Preferences** menu item.
-   Click on **Volume**.
-   Disable or enable the desired features.

### [Adding custom actions to PCManFM-Qt]

PCManFM-Qt supports the [desktop file specification extension](http://www.nautilus-actions.org/?q=node/377) so it is possible to add custom actions to the contextual menu for files and directories.

[[[x11-libs/libfm]](https://packages.gentoo.org/packages/x11-libs/libfm)[]] and [[[x11-libs/libfm-extra]](https://packages.gentoo.org/packages/x11-libs/libfm-extra)[]] v1.2.4 or above are required, and the `vala` USE flag must be enabled:

[FILE] **`/etc/portage/package.use/lxqt`**

    x11-libs/libfm vala

Rebuilding the package can be done with:

`root `[`#`]`emerge -1a libfm`

Once this is done, special .desktop files can be created in [\~/.local/share/file-manager/actions/]. For example here is a simple action that will pop up a notification with the path to the selected file or folder:

[FILE] **`~/.local/share/file-manager/actions/test.desktop`**

    [Desktop Entry]
    Name = Test action
    Profiles = on_icon;

    [X-Action-Profile on_icon]
    Exec = notify-send "You selected %f"

PCManFM-Qt needs to be restarted to become aware of any change made to the custom actions. The safest and simplest way is to logout and login again (restart LXQt).

Alternatively it is possible to exit all instances of PCManFM-Qt with [pcmanfm-qt -q] before launching it again, but be aware that it will likely switch to a different set of settings (it can use two different config directories, one \"default\" and one \"lxqt\", as in [\~/.config/pcmanfm-qt/]) and for example automount volumes which may cause issues.

## [Usage]

### [Applications]

Any Qt application can be used with LXQt, but if Qt applications that do not depend on any component of KDE are preferred, please see the [Qt Desktop applications](https://wiki.gentoo.org/wiki/Qt_Desktop_applications "Qt Desktop applications") article.

### [Wi-Fi]

Add [NetworkManager](https://wiki.gentoo.org/wiki/NetworkManager "NetworkManager") in the default runlevel:

`root `[`#`]`rc-update add NetworkManager default`

In order to have [GUI for Wi-Fi networks](https://wiki.gentoo.org/wiki/NetworkManager#GTK_GUIs "NetworkManager") --- install **nm-applet**:

`root `[`#`]`emerge --ask gnome-extra/nm-applet`

[![](/images/thumb/a/a3/Nm-applet-png.png/300px-Nm-applet-png.png)](https://wiki.gentoo.org/wiki/File:Nm-applet-png.png)

[](https://wiki.gentoo.org/wiki/File:Nm-applet-png.png "Enlarge")

nm-applet

If the LXQt panel is set to autohide and [mouse hover on Wi-Fi ico hides the panel](https://wiki.gentoo.org/wiki/File:Lxqt-tray-widget-obsolote.webp "File:Lxqt-tray-widget-obsolote.webp") :

1.  Emerge [gnome-extras/nm-applet](https://packages.gentoo.org/packages/gnome-extra/nm-applet) with USE flag **appindicator**
2.  Emerge [lxqt-base/lxqt-panel](https://packages.gentoo.org/packages/lxqt-base/lxqt-panel) with USE flag **statusnotifier**
3.  Edit autostart in LXQt: change **nm-applet** to **nm-applet \--indicator**.

See [related bug](https://bugs.gentoo.org/768666).

## [Troubleshooting]

### [Support]

Gentoo support channels are [[#gentoo-qt](ircs://irc.libera.chat/#gentoo-qt)] ([[webchat](https://web.libera.chat/#gentoo-qt)]) on Libera.Chat, and lxqt@gentoo.org. Bugs should be reported at the [Gentoo\'s Bugzilla](https://bugs.gentoo.org/).

Upstream IRC channels are #lxqt for user support, and #lxqt-dev for development, on OFTC.

## [See also]

-   [Desktop environment](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") --- provides a list of desktop environments available in Gentoo.
-   [Xfce](https://wiki.gentoo.org/wiki/Xfce "Xfce") --- a lightweight [desktop environment](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") built to be fast, good looking, and user friendly.