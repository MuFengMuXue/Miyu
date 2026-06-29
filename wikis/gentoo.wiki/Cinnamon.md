This page contains [[changes](https://wiki.gentoo.org/index.php?title=Cinnamon&oldid=1290341&diff=1440179)] which are not marked for translation.

Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/Cinnamon/es "Cinnamon (26% translated)")
-   [français](https://wiki.gentoo.org/wiki/Cinnamon/fr "Cinnamon (100% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Cinnamon/hu "Cinnamon (100% translated)")
-   [polski](https://wiki.gentoo.org/wiki/Cinnamon/pl "Cinnamon (15% translated)")
-   [português do Brasil](https://wiki.gentoo.org/wiki/Cinnamon/pt-br "Cinnamon (66% translated)")
-   [svenska](https://wiki.gentoo.org/wiki/Cinnamon/sv "Cinnamon (28% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Cinnamon/ru "Cinnamon (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Cinnamon/zh-cn "Cinnamon (30% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Cinnamon/ja "Cinnamon (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Cinnamon/ko "Cinnamon/ko (65% translated)")

**Resources**

[[]][Home](https://projects.linuxmint.com/cinnamon/)

[[]][Package information](https://packages.gentoo.org/packages/gnome-extra/cinnamon)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Cinnamon_(software) "wikipedia:Cinnamon (software)")

[[]][GitHub](https://github.com/linuxmint/Cinnamon)

[[]]This article has some todo items:\

-   remove/replace \"consolekit\", see [https://gitweb.gentoo.org/repo/gentoo.git/commit/sys-auth/consolekit?id=39ece3ff2467f0c1a3dc946767f3896d31055198](https://gitweb.gentoo.org/repo/gentoo.git/commit/sys-auth/consolekit?id=39ece3ff2467f0c1a3dc946767f3896d31055198)

**Cinnamon** is a contemporary [desktop environment](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") with a traditional graphical interface. GNOME 2, [LXDE](https://wiki.gentoo.org/wiki/LXDE "LXDE"), or [Xfce](https://wiki.gentoo.org/wiki/Xfce "Xfce") users will find it familiar. Cinnamon has very good graphical and functional features. Forked from GNOME 3\'s GNOME Shell and developed for [Linux Mint](https://linuxmint.com/), it is available on Gentoo for the **[amd64]** and **[x86]** architectures. Wayland support is experimental.^[\[1\]](#cite_note-1)^

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Prerequisites]](#Prerequisites)
        -   [[1.1.1] [OpenRC]](#OpenRC)
        -   [[1.1.2] [systemd]](#systemd)
        -   [[1.1.3] [Combined hardened profiles]](#Combined_hardened_profiles)
        -   [[1.1.4] [Xorg]](#Xorg)
        -   [[1.1.5] [Internationalization]](#Internationalization)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [System configuration]](#System_configuration)
    -   [[2.1] [systemd services]](#systemd_services)
    -   [[2.2] [OpenRC services]](#OpenRC_services)
        -   [[2.2.1] [dbus, openrc-settingsd, elogind]](#dbus.2C_openrc-settingsd.2C_elogind)
        -   [[2.2.2] [NetworkManager]](#NetworkManager)
        -   [[2.2.3] [Disabling NetworkManager applet]](#Disabling_NetworkManager_applet)
    -   [[2.3] [Sudo]](#Sudo)
    -   [[2.4] [Polkit rules and actions]](#Polkit_rules_and_actions)
    -   [[2.5] [Starting Cinnamon]](#Starting_Cinnamon)
-   [[3] [Theming]](#Theming)
    -   [[3.1] [Mint-X icons]](#Mint-X_icons)
    -   [[3.2] [Desktop icons text color]](#Desktop_icons_text_color)
    -   [[3.3] [Mint-X themes]](#Mint-X_themes)
    -   [[3.4] [Playing with themes]](#Playing_with_themes)
-   [[4] [Common applications]](#Common_applications)
    -   [[4.1] [Terminals]](#Terminals)
    -   [[4.2] [Gnome popular applications]](#Gnome_popular_applications)
    -   [[4.3] [Applications without Gnome]](#Applications_without_Gnome)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Refresh rate]](#Refresh_rate)
-   [[6] [See also]](#See_also)
-   [[7] [References]](#References)
-   [[8] [External resources]](#External_resources)

## [Installation]

### [Prerequisites]

Cinnamon works great both with and without systemd. To install without systemd dependencies, use [eselect] to switch to a profile without Gnome, such as `default/linux/amd64/23.0/desktop`. To install with systemd, use a Gnome-enabled profile such as `default/linux/amd64/23.0/desktop/gnome/systemd`. The architecture and version can be different in both cases.

** Important**\
Read [relevant documentation](https://wiki.gentoo.org/wiki/Profile_(Portage)#Changing_profile "Profile (Portage)") before performing any profile changes.

To get a list of available system profiles:

`root `[`#`]`eselect profile list`

    ...
      [21]  default/linux/amd64/23.0 (stable) *
      [22]  default/linux/amd64/23.0/systemd (stable)
      [23]  default/linux/amd64/23.0/desktop (stable)
      [24]  default/linux/amd64/23.0/desktop/systemd (stable)
      [25]  default/linux/amd64/23.0/desktop/gnome (stable)
      [26]  default/linux/amd64/23.0/desktop/gnome/systemd (stable)
    ...

#### [OpenRC]

When using OpenRC, set the right system profile:

`root `[`#`]`eselect profile set default/linux/amd64/23.0/desktop`

It is also possible to use the associated profile number according to the profiles list above:

`root `[`#`]`eselect profile set 20`

Read up on the instructions available in the [Gentoo without systemd](https://wiki.gentoo.org/wiki/Gentoo_without_systemd "Gentoo without systemd") article.

#### [systemd]

** Warning**\
Read the [[systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd")] documentation before changing to a [systemd] profile.

For Cinnamon with systemd support select the GNOME desktop profile ending in systemd:

`root `[`#`]`eselect profile set default/linux/amd64/23.0/desktop/systemd`

** Note**\
The system architecture (`amd64`) and version (`23.0`) can be different as long as the ending of the string is `/gnome/systemd`.

#### [Combined hardened profiles]

Users that run hardened profiles can also combine it with all the features of the desktop profile. For steps on doing this please follow [Hardened_Desktop_Profiles](https://wiki.gentoo.org/wiki/Hardened_Desktop_Profiles "Hardened Desktop Profiles").

#### [Xorg]

Of course for Cinnamon to work [Xorg must be installed and configured](https://wiki.gentoo.org/wiki/Xorg/Guide "Xorg/Guide"). Make sure an X server is set up before proceeding with this article. If needed, test Xorg as detailed in the [Using startx](https://wiki.gentoo.org/wiki/Xorg/Guide#Using_startx "Xorg/Guide") section of the Xorg Gentoo guide.

#### [Internationalization]

Cinnamon (and other applications) are internationalized, supporting a number of languages (Linguas). If this was not done during the initial Gentoo installation, add the appropriate language value to the `LINGUAS` variable in [/etc/portage/package.use]:

[FILE] **`/etc/portage/package.use/00localization`**

    */* LINGUAS: en

### [USE flags]

### [USE flags for] [gnome-extra/cinnamon](https://packages.gentoo.org/packages/gnome-extra/cinnamon) [[]] [A fork of GNOME Shell with layout similar to GNOME 2]

  --------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------
  [`+eds`](https://packages.gentoo.org/useflags/+eds)                         Enable support for Evolution-Data-Server (EDS)
  [`+gstreamer`](https://packages.gentoo.org/useflags/+gstreamer)             Add support for media-libs/gstreamer (Streaming media)
  [`+networkmanager`](https://packages.gentoo.org/useflags/+networkmanager)   Enable net-misc/networkmanager support
  [`+nls`](https://packages.gentoo.org/useflags/+nls)                         Add Native Language Support (using gettext - GNU locale utilities)
  [`gtk-doc`](https://packages.gentoo.org/useflags/gtk-doc)                   Build and install gtk-doc based developer documentation for dev-util/devhelp, IDE and offline use
  [`wayland`](https://packages.gentoo.org/useflags/wayland)                   Enable dev-libs/wayland backend
  --------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-18 16:27] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

Find more information on Python targets by visiting the Python project\'s [PYTHON TARGETS](https://wiki.gentoo.org/wiki/Project:Python/PYTHON_TARGETS "Project:Python/PYTHON TARGETS") article.

The `icu`, `pulseaudio`, and `gnome-keyring` USE flags are needed by Cinnamon\'s dependencies. If they are not set already, either allow [emerge \--ask gnome-extra/cinnamon] to create or update [package.use] (or [package.use/cinnamon], or set the USE flags manually using another method.

### [Emerge]

Finally, after performing all the steps above, ask Portage to emerge Cinnamon:

`root `[`#`]`emerge --ask gnome-extra/cinnamon`

** Note**\
The compilation duration for [[[net-libs/webkit-gtk]](https://packages.gentoo.org/packages/net-libs/webkit-gtk)[]] can be very long, especially on older hardware. This can be resolved by removing the `gnome-online-accounts` USE flag for those that don\'t want social media notifications on the desktop.

## [System configuration]

Before looking at the Cinnamon theming, configure the system to properly start Cinnamon at boot or upon user request, and enable the right privilege delegation settings so that end users can interact with the system in an intuitive manner.

### [systemd services]

[dbus] must be activated with systemd, use [systemctl] as detailed in the [systemd page](https://wiki.gentoo.org/wiki/Systemd#Enabling.2C_disabling.2C_starting.2C_and_stopping_services "Systemd").

### [OpenRC services]

#### [][dbus, openrc-settingsd, elogind]

Xorg server and Cinnamon need the [dbus], [openrc-settingsd] and [elogind] services, make sure that they will be started at system boot time:

`root `[`#`]`rc-update add dbus default `

`root `[`#`]`rc-update add openrc-settingsd default `

`root `[`#`]`rc-update add elogind boot `

Next, start the services (there is no need to restart the system):

`root `[`#`]`rc-service dbus start `

`root `[`#`]`rc-service openrc-settingsd start `

`root `[`#`]`rc-service elogind start `

#### [NetworkManager]

[NetworkManager](https://wiki.gentoo.org/wiki/NetworkManager "NetworkManager") is a Cinnamon dependency and is not needed if the network was configured during the initial Gentoo installation. It should not run concurrently with another network service. If NetworkManager is desired be sure to disable other network management programs or services before starting it. For example, if the system was originally configured to use Gentoo\'s netifrc scripts to manage the network connections, disable these network services:

`root `[`#`]`rc-service net.eth0 stop `

`root `[`#`]`rc-update del net.eth0 default `

** Note**\
When using [[[sys-fs/udev]](https://packages.gentoo.org/packages/sys-fs/udev)[]] network interfaces will be using [Predictable Network Interface Names](https://www.freedesktop.org/wiki/Software/systemd/PredictableNetworkInterfaceNames/) to name the active interfaces. This will produce names like [enp12s0], [eno1], [enp2s0], etc. When using [[[sys-fs/eudev]](https://packages.gentoo.org/packages/sys-fs/eudev)[]], the Gentoo udev fork avoiding systemd dependencies, the first network interface name is often still called [eth0].

After removing the other network services, add NetworkManager:

`root `[`#`]`rc-service NetworkManager start `

`root `[`#`]`rc-update add NetworkManager default `

#### [Disabling NetworkManager applet]

If NetworkManager is not used, the Network Manager applet will fail to start up, which will show up as a problem during startup.

To disable the applet, go to System Settings -\> Preferences -\> Applets, find \"Network Manager\" and click the minus button.

### [Sudo]

For an ordinary user to reboot or shutdown the system from Cinnamon, [sudo] is needed with some settings.

First install [[[app-admin/sudo]](https://packages.gentoo.org/packages/app-admin/sudo)[]]:

`root `[`#`]`emerge --ask app-admin/sudo`

Next modify the [sudo] configuration with the [visudo] command:

`root `[`#`]`visudo`

Visudo runs the default text editor to generate or update a [sudoers] file. Replace `username` in the text below with the username of each user that will be using Cinnamon:

[FILE] **`/etc/sudoers`**

    username  ALL=(root) NOPASSWD: /sbin/reboot
    username  ALL=(root) NOPASSWD: /sbin/halt
    username  ALL=(root) NOPASSWD: /sbin/poweroff
    username  ALL=(root) NOPASSWD: /sbin/shutdown

Or for the [wheel] group:

[FILE] **`/etc/sudoers`**

    %wheel  ALL=(root) NOPASSWD: /sbin/reboot
    %wheel  ALL=(root) NOPASSWD: /sbin/halt
    %wheel  ALL=(root) NOPASSWD: /sbin/poweroff
    %wheel  ALL=(root) NOPASSWD: /sbin/shutdown

### [Polkit rules and actions]

For an ordinary user to perform additional highly privileged actions from Cinnamon, policy kit must be configured. Use [pkaction] to get a list of actions; the names should be self-explanatory:

`root `[`#`]`pkaction`

    org.cinnamon.settings-daemon.plugins.power.backlight-helper
    org.cinnamon.settings-users
    org.cinnamon.settingsdaemon.datetimemechanism.configure
    org.freedesktop.ModemManager1.Contacts
    org.freedesktop.ModemManager1.Control
    org.freedesktop.ModemManager1.Device.Control
    org.freedesktop.ModemManager1.Firmware
    org.freedesktop.ModemManager1.Location
    org.freedesktop.ModemManager1.Messaging
    org.freedesktop.ModemManager1.USSD
    org.freedesktop.NetworkManager.enable-disable-network
    org.freedesktop.NetworkManager.enable-disable-wifi
    etc.

The simplest way is to authorize all actions by only testing [wheel] group membership. Put a JavaScript file with a [.rules] extension in [/etc/polkit-1/rules.d], named for example [55-allowing-all-actions.rules]:

[FILE] **`/etc/polkit-1/rules.d/55-allowing-all-actions.rules`Setting general polkit rule**

    polkit.addRule (function (action, subject)

    });

To only authorize some actions, the action names must be iterated. For a [wheel] group user to suspend, hibernate, shutdown and restart the system, make a [55-allowing-actions.rules] file like so:

[FILE] **`/etc/polkit-1/rules.d/55-allowing-actions.rules`Setting polkit rules**

    polkit.addRule (function (action, subject)

    });

Various actions can be added: those to change color profiles, use Nemo (Cinnamon files manager) as root, mount and eject media, set screen backlight, use network manager, change wallpaper, etc. Several `polkit.addRule (function (action, subject));` blocks can be used next to each other as well, and several files can be added.

** Important**\
[/etc/polkit-1/rules.d/50-default.rules] already exists. Newly created file(s) names should begin with a number bigger than 50, **55** for example, so they are processed after the [50-default.rules] file. Do not make a file which would be processed before it, for instance one beginning with **45**.

### [Starting Cinnamon]

When not using a login/display manager, make a [.xinitrc] file in the user\'s home directory, starting Cinnamon (D-bus will be launched too automatically):

[FILE] **`~/.xinitrc`Cinnamon launch directive**

    exec cinnamon-session

Then to start Xorg and Cinnamon, execute [startx] after logging in:

`user `[`$`]`startx`

With a display manager follow the [display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager") instructions.

## [Theming]

### [Mint-X icons]

By default Cinnamon comes with Gnome icons. [Mint-X icons are on GitHub](https://github.com/linuxmint/mint-x-icons). Download, unzip, and put the Mint-X icon set in [/usr/share/icons]:

`root `[`#`]`mv pathToUnzippedArchive/mint-x-icons-master/usr/share/icons/Mint-X /usr/share/icons/Mint-X`

Next, make a cache for it:

`root `[`#`]`gtk-update-icon-cache /usr/share/icons/Mint-X`

The new icon set can be selected in Cinnamon Control Center. Mint-X icons are green, but other icon sets with different colors can be installed too, like Mint-X-Grey or Mint-X-Orange. Make sure to create a cache for these as well.

** Important**\
Colored icons sets rely on Mint-X icon set: always install it, with or without colored icons sets.

### [Desktop icons text color]

** Note**\
Desktop icons text color is now white in Cinnamon version 2.6.13, so this chapter applies to older Cinnamon versions... and remains a good introduction to Cinnamon theming.

An icon\'s text color in Cinnamon desktop is black by default, which is not always readable. The instructions to change this color depends on the GTK 3 version that the system is using. Get the currently used version with:

`user `[`$`]`emerge --info x11-libs/gtk+`

-   In GTK versions less than 3.13.3, this setting can only be changed system-wide. Change the text color by adding CSS rules to the [/usr/share/themes/Adwaita/gtk-3.0/gtk.css] file (Adwaita is the default theme coming with GTK), after the `@import` line:

[FILE] **`/usr/share/themes/Adwaita/gtk-3.0/gtk.css`CSS rules for GTK \< 3.13.3**

    @import url("resource:///org/gnome/adwaita/gtk-main.css");

    /* added css rules */
    .nemo-desktop.nemo-canvas-item

    .nemo-desktop.nemo-canvas-item:selected

The 2^nd^ rule concerns the selected desktop icon and can be modified to get another background color or set the transparency.

-   In more recent GTK versions (3.13.3 onward), this must be tuned through a user-specific configuration file. Adwaita is now included in GTK as the theme replacing Raleigh, so rules must be set in the user\'s home directories. The file to edit is [\~/.config/gtk-3.0/gtk.css] (create [\~/.config/gtk-3.0/] directory if needed), and the change is now without the `@import` line. Additionally in this example, the left Nemo side bar is gray colored:

[FILE] **`~/.config/gtk-3.0/gtk.css`CSS rules for GTK ≥ 3.13.3**

    .nemo-desktop.nemo-canvas-item

    .nemo-desktop.nemo-canvas-item:selected

    NemoWindow .sidebar, NemoWindow .sidebar .view

### [Mint-X themes]

Cinnamon comes with a default cinnamon theme, obviously\... The Mint-X themes are [available for download](https://github.com/linuxmint/mint-themes) on GitHub. Download them, unzip, and copy to [/usr/share/themes] if needed. They can be selected in the Cinnamon Control Center.

### [Playing with themes]

Almost all theme settings can be changed in the [cinnamon.css] file in the theme directory.

For example with the Cinnamon theme, which is not in [/usr/share/themes] but in [/usr/share/cinnamon/theme], first copy the theme\'s directory to a user [.themes] sub-directory, named for example [other-cinnamon], which will be the new theme name:

`root `[`#`]`mkdir /home/userName/.themes/other-cinnamon `

`root `[`#`]`cp -R /usr/share/cinnamon/theme /home/userName/.themes/other-cinnamon/cinnamon `

`root `[`#`]`chown -R userName:userName /home/userName/.themes/other-cinnamon `

Edit [\~/.themes/other-cinnamon/cinnamon/cinnamon.css]. The results of the changes can be viewed immediately by selecting another theme in Cinnamon Control Center, then reselecting the theme being changed.

## [Common applications]

### [Terminals]

-   [[[lxde-base/lxterminal]](https://packages.gentoo.org/packages/lxde-base/lxterminal)[]] - Requires no dependencies.
-   [[[x11-terms/xfce4-terminal]](https://packages.gentoo.org/packages/x11-terms/xfce4-terminal)[]] - Requires some dependencies but is better featured than [[[lxde-base/lxterminal]](https://packages.gentoo.org/packages/lxde-base/lxterminal)[]].
-   [[[x11-terms/gnome-terminal]](https://packages.gentoo.org/packages/x11-terms/gnome-terminal)[]] - Doesn\'t require systemd if `-nautilus` and `-gnome-shell` USE flags are set for this package.

### [Gnome popular applications]

A number of popular applications are available as well, built for Gnome and working flawlessly in Cinnamon:

-   standard calculator ([[[gnome-extra/gnome-calculator]](https://packages.gentoo.org/packages/gnome-extra/gnome-calculator)[]])
-   screen copy utility ([[[media-gfx/gnome-screenshot]](https://packages.gentoo.org/packages/media-gfx/gnome-screenshot)[]])
-   image viewer ([[[media-gfx/eog]](https://packages.gentoo.org/packages/media-gfx/eog)[]])
-   PDF reader ([[[app-text/evince]](https://packages.gentoo.org/packages/app-text/evince)[]])
-   system monitor ([[[gnome-extra/gnome-system-monitor]](https://packages.gentoo.org/packages/gnome-extra/gnome-system-monitor)[]])
-   archive manager ([[[app-arch/file-roller]](https://packages.gentoo.org/packages/app-arch/file-roller)[]])
-   disk burning ([[[app-cdr/brasero]](https://packages.gentoo.org/packages/app-cdr/brasero)[]])
-   text editor ([[[app-editors/gedit]](https://packages.gentoo.org/packages/app-editors/gedit)[]])

\

`root `[`#`]`emerge --ask gnome-extra/gnome-calculator media-gfx/gnome-screenshot media-gfx/eog app-text/evince gnome-extra/gnome-system-monitor app-arch/file-roller app-cdr/brasero app-editors/gedit`

### [Applications without Gnome]

Also working flawlessly in Cinnamon:

-   PDF readers [[[app-text/mupdf]](https://packages.gentoo.org/packages/app-text/mupdf)[]] and [[[app-text/qpdfview]](https://packages.gentoo.org/packages/app-text/qpdfview)[]]
-   light text editor [[[app-editors/leafpad]](https://packages.gentoo.org/packages/app-editors/leafpad)[]]
-   mp3 and video readers [[[media-video/mpv]](https://packages.gentoo.org/packages/media-video/mpv)[]] and [[[media-video/vlc]](https://packages.gentoo.org/packages/media-video/vlc)[]]

\
Compile [[[app-text/qpdfview]](https://packages.gentoo.org/packages/app-text/qpdfview)[]] and [[[media-video/vlc]](https://packages.gentoo.org/packages/media-video/vlc)[]] with `qt5` USE flags to get a GUI.

## [Troubleshooting]

If problems occur, try to get access to the live error messages. These can be displayed on a separate (virtual) terminal or in a log file. If the messages cannot be found, try starting Cinnamon from the command line rather than through a display manager. Alternatively have a look at [/var/log/Xorg.0.log].

When the error or warning messages are not sufficient to troubleshoot Cinnamon, start it with the `--debug` parameter to get more detailed Xorg messages:

[FILE] **`~/.xinitrc`Cinnamon debug launch**

    exec cinnamon-session --debug

If Cinnamon cannot launch, deleting (or renaming) [.cinnamon] in the home directory is not enough: other Cinnamon or Gnome items must be deleted (or renamed) too before X restarts. These can be found in the [.cache], [.config] and [.local] XDG directories. [.gnome2] can be deleted (or renamed) entirely.

### [Refresh rate]

It\'s possible to set custom refresh rate via [\~/.config/monitors.xml] file. Replace `<rate>60</rate>` with preferred setting.

## [See also]

-   [Desktop environment](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") --- provides a list of desktop environments available in Gentoo.
-   [Xfce](https://wiki.gentoo.org/wiki/Xfce "Xfce") --- a lightweight [desktop environment](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") built to be fast, good looking, and user friendly.
-   [MATE](https://wiki.gentoo.org/wiki/MATE "MATE") --- a [fork](https://en.wikipedia.org/wiki/Fork_(software_development) "wikipedia:Fork (software development)") of the [GNOME 2](https://wiki.gentoo.org/wiki/GNOME "GNOME") desktop environment designed to retain the look and feel of a \'traditional\' desktop environment.
-   [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME") --- a feature-rich desktop environment provided by the [GNOME project](https://www.gnome.org).
-   [KDE](https://wiki.gentoo.org/wiki/KDE "KDE") --- a free software community, producing a wide range of applications including the popular Plasma desktop environment.

## [References]

1.  [[[↑](#cite_ref-1)] [Clem. [Monthly News -- January 2024](//blog.linuxmint.com/?p=4639) Retrieved on September 21st, 2024.]]

## [External resources]

-   [polkit Reference Manual](https://www.freedesktop.org/software/polkit/docs/latest/index.html) and [polkit page](https://www.freedesktop.org/software/polkit/docs/latest/polkit.8.html)
-   The [web colors Wikipedia article](https://en.wikipedia.org/wiki/Web_colors)
-   An extensive [Gnome applications list](https://wiki.gnome.org/Apps)
-   [Cinnamon announcements](http://segfault.linuxmint.com/)