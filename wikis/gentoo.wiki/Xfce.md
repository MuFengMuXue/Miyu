This page contains [[changes](https://wiki.gentoo.org/index.php?title=Xfce&oldid=1426105&diff=1436536)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Xfce/de "Xfce (33% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/Xfce/es "Xfce (23% translated)")
-   [français](https://wiki.gentoo.org/wiki/Xfce/fr "Xfce/fr (94% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Xfce/it "Xfce (23% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Xfce/hu "Xfce (100% translated)")
-   [polski](https://wiki.gentoo.org/wiki/Xfce/pl "Xfce (94% translated)")
-   [português do Brasil](https://wiki.gentoo.org/wiki/Xfce/pt-br "Xfce (24% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Xfce/ru "Xfce (79% translated)")
-   [فارسی](https://wiki.gentoo.org/wiki/Xfce/fa "Xfce (2% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Xfce/zh-cn "Xfce (38% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Xfce/ja "Xfce (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Xfce/ko "Xfce/ko (24% translated)")

**Resources**

[[]][Home](https://xfce.org/)

[[]][Official documentation](https://docs.xfce.org/start)

[[]][Package information](https://packages.gentoo.org/packages/xfce-base/xfce4-meta)

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Xfce "Project:Xfce")][Project](https://wiki.gentoo.org/wiki/Project:Xfce "Project:Xfce")

[[]][Guide](https://wiki.gentoo.org/wiki/Xfce/Guide "Xfce/Guide")

[[]][Wikipedia](https://en.wikipedia.org/wiki/Xfce "wikipedia:Xfce")

[[]][GitWeb](https://git.xfce.org/)

**Xfce** is a lightweight [desktop environment](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") built to be fast, good looking, and user friendly.

** Tip**\
Wayland support is [planned in the form of \'xfwl4\'](https://alexxcons.github.io/blogpost_15.html): \"Xfwl4 will not be based on the existing xfwm4 code. Instead, it will be written from scratch in rust, using smithay building blocks.\"

## Contents

-   [[1] [Prerequisites]](#Prerequisites)
    -   [[1.1] [Selecting a profile]](#Selecting_a_profile)
        -   [[1.1.1] [Combined hardened profiles]](#Combined_hardened_profiles)
    -   [[1.2] [Avoiding unnecessary dependencies]](#Avoiding_unnecessary_dependencies)
    -   [[1.3] [xfce4-notifyd]](#xfce4-notifyd)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [USE flags]](#USE_flags)
    -   [[2.2] [Emerge]](#Emerge)
    -   [[2.3] [Additional software]](#Additional_software)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Launching Xfce]](#Launching_Xfce)
        -   [[3.1.1] [Starting Xfce without a display manager]](#Starting_Xfce_without_a_display_manager)
            -   [[3.1.1.1] [startx]](#startx)
            -   [[3.1.1.2] [startxfce4]](#startxfce4)
        -   [[3.1.2] [Display managers]](#Display_managers)
-   [[4] [Configuration]](#Configuration)
    -   [[4.1] [Volume keys]](#Volume_keys)
    -   [[4.2] [Consistent GTK 3 themes]](#Consistent_GTK_3_themes)
    -   [[4.3] [GTK client side decorations]](#GTK_client_side_decorations)
    -   [[4.4] [Other themes]](#Other_themes)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Enable vertical window snapping]](#Enable_vertical_window_snapping)
    -   [[5.2] [Audio mixer complains about missing pavucontrol binary]](#Audio_mixer_complains_about_missing_pavucontrol_binary)
    -   [[5.3] [Xfce4-screensaver unable to unlock]](#Xfce4-screensaver_unable_to_unlock)
    -   [[5.4] [Authorization or permissions issues]](#Authorization_or_permissions_issues)
    -   [[5.5] [Dual-monitors get mirrored after monitor suspend]](#Dual-monitors_get_mirrored_after_monitor_suspend)
    -   [[5.6] [Desktop shows solid color instead of selected wallpaper]](#Desktop_shows_solid_color_instead_of_selected_wallpaper)
-   [[6] [See also]](#See_also)

## [Prerequisites]

### [Selecting a profile]

** Important**\
Read [relevant documentation](https://wiki.gentoo.org/wiki/Portage/Profiles#Changing_profile "Portage/Profiles") before performing any profile changes.

Using the basic *desktop* [profile](https://wiki.gentoo.org/wiki/Portage/Profiles "Portage/Profiles") will provide a good set of defaults for Xfce. Other profiles can be used, but this gives a good balance between dependencies and usability, all else aside. To select the *desktop* profile:

`root `[`#`]`eselect profile set default/linux/amd64/23.0/desktop`

#### [Combined hardened profiles]

Users that run hardened profiles can also combine it with all the features of the desktop profile. For steps on doing this please follow [Hardened_Desktop_Profiles](https://wiki.gentoo.org/wiki/Hardened_Desktop_Profiles "Hardened Desktop Profiles").

### [Avoiding unnecessary dependencies]

The package [[[app-text/poppler]](https://packages.gentoo.org/packages/app-text/poppler)[]] will be pulled in as a dependency when emerging Xfce. On desktop profiles, this package will use the `qt6` USE flag by default, and so will pull in Qt dependencies that may not be needed for Xfce. One way to avoid this is to [disable this USE flag](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/USE#Declaring_USE_flags_for_individual_packages "Handbook:AMD64/Working/USE") for poppler:

[FILE] **`/etc/portage/package.use/xfce`Unset qt6 USE flag for poppler**

    app-text/poppler -qt6

Of course, `-qt6` can also added to [/etc/portage/make.conf], to unset the flag globally, if desired.

### [xfce4-notifyd]

This is an optional step to install [[[xfce-extra/xfce4-notifyd]](https://packages.gentoo.org/packages/xfce-extra/xfce4-notifyd)[]] in place of [[[x11-misc/notification-daemon]](https://packages.gentoo.org/packages/x11-misc/notification-daemon)[]]. Skip this section if the choice of notification daemon is unimportant.

Emerging [[[xfce-base/xfce4-meta]](https://packages.gentoo.org/packages/xfce-base/xfce4-meta)[]] will pull in the [[[virtual/notification-daemon]](https://packages.gentoo.org/packages/virtual/notification-daemon)[]] dependency. This virtual dependency is designed to insure that Xfce will be provided with a notification-daemon, whatever suitable software the user chooses to fulfill this role.

By default, [[[virtual/notification-daemon]](https://packages.gentoo.org/packages/virtual/notification-daemon)[]] will satisfy this dependency by drawing in GNOME\'s [[[x11-misc/notification-daemon]](https://packages.gentoo.org/packages/x11-misc/notification-daemon)[]] package. Xfce users may prefer to use [[[xfce-extra/xfce4-notifyd]](https://packages.gentoo.org/packages/xfce-extra/xfce4-notifyd)[]], if a notification-daemon has not already been installed.

By installing [[[xfce-extra/xfce4-notifyd]](https://packages.gentoo.org/packages/xfce-extra/xfce4-notifyd)[]] before emerging Xfce, the virtual package [[[virtual/notification-daemon]](https://packages.gentoo.org/packages/virtual/notification-daemon)[]] will use [xfce4-notifyd], and pull in no other packages. Use the `--oneshot` option to [avoid adding xfce4-notifyd to the world file](https://wiki.gentoo.org/wiki/Selected-packages_set_(Portage)#Emerge_a_package_without_adding_it_to_the_world_file "Selected-packages set (Portage)"):

`root `[`#`]`emerge --ask --oneshot xfce-extra/xfce4-notifyd`

Now proceed with the installation.

## [Installation]

### [USE flags]

### [USE flags for] [xfce-base/xfce4-meta](https://packages.gentoo.org/packages/xfce-base/xfce4-meta) [[]] [The Xfce Desktop Environment (meta package)]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------
  [`+svg`](https://packages.gentoo.org/useflags/+svg)               Add support for SVG (Scalable Vector Graphics)
  [`archive`](https://packages.gentoo.org/useflags/archive)         Install app-arch/xarchiver.
  [`calendar`](https://packages.gentoo.org/useflags/calendar)       Add support for calendars (not using mcal!)
  [`cdr`](https://packages.gentoo.org/useflags/cdr)                 Add support for CD writer hardware
  [`editor`](https://packages.gentoo.org/useflags/editor)           Install the app-editors/mousepad text editor.
  [`image`](https://packages.gentoo.org/useflags/image)             Install the media-gfx/ristretto image viewer.
  [`media`](https://packages.gentoo.org/useflags/media)             Install the media-video/parole media player.
  [`minimal`](https://packages.gentoo.org/useflags/minimal)         Install a very minimal build (disables, for example, plugins, fonts, most drivers, non-critical features)
  [`mpd`](https://packages.gentoo.org/useflags/mpd)                 Install the media-sound/xfmpc MPD client.
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)   Add sound server support via media-libs/libpulse (may be PulseAudio or PipeWire)
  [`remote-fs`](https://packages.gentoo.org/useflags/remote-fs)     Install the x11-misc/gigolo frontend to manage remote filesystem connections.
  [`search`](https://packages.gentoo.org/useflags/search)           Install the dev-util/catfish search tool frontend.
  [`upower`](https://packages.gentoo.org/useflags/upower)           Enable power management support
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-06-21 16:59] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Emerge [[[xfce-base/xfce4-meta]](https://packages.gentoo.org/packages/xfce-base/xfce4-meta)[]] for a default set of Xfce packages, to get a reasonably complete desktop environment:

`root `[`#`]`emerge --ask xfce-base/xfce4-meta`

\
The [[[xfce-base/xfce4-meta]](https://packages.gentoo.org/packages/xfce-base/xfce4-meta)[]] package will provide the following user-facing applications, plus some libraries and system software:

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Package                                                                                                                                                                                                                                                                                                                                                                                                                        Description
  [[[x11-terms/xfce4-terminal]](https://packages.gentoo.org/packages/x11-terms/xfce4-terminal)[]]                                 Terminal emulator that integrates well with Xfce, \"friendlier\" than the standard [xterm] program.
  [[[xfce-base/xfce4-panel]](https://packages.gentoo.org/packages/xfce-base/xfce4-panel)[]]                                          Desktop panel with application launchers, panel menus, a workspace switcher, and more.
  [[[xfce-base/xfce4-settings]](https://packages.gentoo.org/packages/xfce-base/xfce4-settings)[]]                                 Configuration system for the Xfce desktop environment, providing configuration dialogs and tools.
  [[[xfce-base/thunar]](https://packages.gentoo.org/packages/xfce-base/thunar)[]]                                                         [Thunar](https://wiki.gentoo.org/wiki/Thunar "Thunar") is Xfce\'s file manager.
  [[[xfce-base/xfce4-appfinder]](https://packages.gentoo.org/packages/xfce-base/xfce4-appfinder)[]]                              Application finder.
  [[[xfce-base/thunar-volman]](https://packages.gentoo.org/packages/xfce-base/thunar-volman)[]]                                    Manages removable media and drives.
  [[[xfce-base/tumbler]](https://packages.gentoo.org/packages/xfce-base/tumbler)[]]                                                      File previewer for Thunar.
  [[[xfce-base/xfce4-power-manager]](https://packages.gentoo.org/packages/xfce-base/xfce4-power-manager)[]]                  An application to monitor and manage power usage (especially important for laptops). Choose maximum-performance or battery-saving modes. Adjust screen brightness and setup hibernate, suspend, and shutdown actions (i.e., when the lid is shut or buttons are pressed). Can warn when the battery reaches certain levels, or even turn off the machine. Includes panel plugins to display battery/charging status, and control brightness.
  [[[xfce-extra/xfce4-pulseaudio-plugin]](https://packages.gentoo.org/packages/xfce-extra/xfce4-pulseaudio-plugin)[]]   Volume control for the panel. [[[media-sound/volumeicon]](https://packages.gentoo.org/packages/media-sound/volumeicon)[]] may be an option for systems without [pulseaudio].
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To see everything that is installed by [[[xfce-base/xfce4-meta]](https://packages.gentoo.org/packages/xfce-base/xfce4-meta)[]], see the dependency tab for that package on [packages.gentoo.org](https://wiki.gentoo.org/wiki/Packages.gentoo.org "Packages.gentoo.org").

It is not strictly necessary to use [[[xfce-base/xfce4-meta]](https://packages.gentoo.org/packages/xfce-base/xfce4-meta)[]], Xfce can be \"custom built\" by installing just the desired components, but be aware that this requires some knowledge of what is needed.

### [Additional software]

There are a number of additional applications that are part of the Xfce project and are of note:

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Package                                                                                                                                                                                                                                                                                                                                                                                                                  Description
  [[[app-cdr/xfburn]](https://packages.gentoo.org/packages/app-cdr/xfburn)[]]                                                         CD burning application.
  [[[app-editors/mousepad]](https://packages.gentoo.org/packages/app-editors/mousepad)[]]                                       Lightweight text editor.
  [[[x11-themes/xfwm4-themes]](https://packages.gentoo.org/packages/x11-themes/xfwm4-themes)[]]                              Several window-manager themes.
  [[[xfce-extra/thunar-archive-plugin]](https://packages.gentoo.org/packages/xfce-extra/thunar-archive-plugin)[]]   Plugin for Thunar to work with archives; uses [[[app-arch/file-roller]](https://packages.gentoo.org/packages/app-arch/file-roller)[]].
  [[[xfce-extra/xfce4-battery-plugin]](https://packages.gentoo.org/packages/xfce-extra/xfce4-battery-plugin)[]]      Displays battery percentage, time remaining, power source (AC or battery), fan status, warnings, and can even be configured to execute commands at certain power levels, which can be used to put the laptop into hibernate mode when the battery is almost exhausted.
  [[[xfce-extra/xfce4-mount-plugin]](https://packages.gentoo.org/packages/xfce-extra/xfce4-mount-plugin)[]]            One-click mounting of devices listed in [[/etc/fstab](https://wiki.gentoo.org/wiki//etc/fstab "/etc/fstab")].
  [[[xfce-extra/xfce4-sensors-plugin]](https://packages.gentoo.org/packages/xfce-extra/xfce4-sensors-plugin)[]]      Monitor hardware sensors, such as CPU temperature, fan RPM, hard drive temp, motherboard voltage, and more.
  [[[xfce-extra/xfce4-verve-plugin]](https://packages.gentoo.org/packages/xfce-extra/xfce4-verve-plugin)[]]            A small command line embedded into the panel; quicker than opening up another terminal to run a command.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This is just a partial selection of packages available in the Gentoo repository, see [xfce-extra](https://packages.gentoo.org/categories/xfce-extra) , or use [eix](https://wiki.gentoo.org/wiki/Eix "Eix") ([eix \--category xfce-extra]), to see packages from the *xfce-extra* category. See also [https://www.xfce.org/projects/](https://www.xfce.org/projects/) for more information.

The following applications work well in Xfce to round out a basic desktop environment:

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------
  Package                                                                                                                                                                                                                                                                                                                                                                     Description
  [[[x11-misc/alacarte]](https://packages.gentoo.org/packages/x11-misc/alacarte)[]]   GNOME\'s menu editor works fine in Xfce.
  [[[x11-terms/tilda]](https://packages.gentoo.org/packages/x11-terms/tilda)[]]         Lightweight quake-style terminal emulator.
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------

## [Usage]

### [Launching Xfce]

Xfce can either be run from a terminal after login, launched automatically after login, or be started by a graphical display manager that will greet the user and ask for login details.

#### [Starting Xfce without a display manager]

[startx] and [startxfce4] are two of the [readily available options](https://wiki.gentoo.org/wiki/X_without_Display_Manager "X without Display Manager") for starting Xfce without using a display manager.

##### [startx]

When using [startx], create an [\~/.xinitrc] file with the following contents:

[FILE] **`~/.xinitrc`Starting xfce4 when invoking startx**

    exec startxfce4

If experiencing authorization or permissions issues, see the [troubleshooting section](https://wiki.gentoo.org/wiki/Xfce#Authorization_or_permissions_issues "Xfce").

##### [startxfce4]

To launch the Xfce4 desktop, simply type [startxfce4] at the command-line and press enter:

`user `[`$`]`startxfce4`

#### [Display managers]

It is possible to use a display manager to start Xfce. Please refer to the [display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager") article to configure a display manager.

Most display managers use [.desktop] files to configure available sessions. The following is an example desktop file that could be used to launch Xfce via a display manager:

[FILE] **`xfce4.desktop`Xfce4 desktop file for display managers**

    [Desktop Entry]
    Encoding=UTF-8
    Name=Xfce4
    Comment=Use this session to run Xfce 4 as desktop environment
    Exec=/usr/bin/startxfce4
    Icon=/usr/share/pixmaps/xfce4_xicon1.png
    Type=Application

The desktop file can be placed in the right location for the display manager.

## [Configuration]

Xfce is a desktop environment and as such can be tuned and tailored to the needs of (almost) every user. In this section, a number of popular (or more challenging) aspects are covered.

### [Volume keys]

Install [[[xfce-extra/xfce4-volumed-pulse]](https://packages.gentoo.org/packages/xfce-extra/xfce4-volumed-pulse)[]] to manage the volume keys:

`root `[`#`]`emerge --ask xfce-extra/xfce4-volumed-pulse`

[[[media-sound/tudor-volumed]](https://packages.gentoo.org/packages/media-sound/tudor-volumed)[]] may be an option for systems not using [pulseaudio].

Alternatively, custom keys can be bound to [amixer] by running [xfce4-keyboard-settings]:

-   [volume up] button: amixer set Master 5%+
-   [volume down] button: amixer set Master 5%-
-   [mute] button: amixer set Master toggle

### [Consistent GTK 3 themes]

One option is to use the [Greybird](https://github.com/shimmerproject/Greybird) theme, which has support for GTK 2, GTK 3, xfwm4, emerald, and metacity:

`root `[`#`]`emerge --ask x11-themes/greybird`

Go to [Xfce menu] -\> [Settings] -\> [Appearance]. Or run [xfce4-appearance-settings]. Select \"Greybird\" from the \"Style\" list.

Now GTK 2 and GTK 3 applications should have a consistent look.

### [GTK client side decorations]

XFCE by default disables GTK client side decorations. If one wishes to enable them, they can set `GTK_CSD=1` environment variable. Apps like [Firefox](https://wiki.gentoo.org/wiki/Firefox "Firefox") use client side decorations to hide their own title bar.

### [Other themes]

Other themes available in Portage that are compatible with XFCE can be emerged with the following list:

`root `[`#`]`emerge --ask x11-themes/clearlooks-phenix x11-themes/gnome-themes-standard x11-themes/light-themes x11-themes/murrine-themes x11-themes/shiki-colors x11-themes/tactile3 x11-themes/zukini`

## [Troubleshooting]

### [Enable vertical window snapping]

Most modern desktop environments have vertical window snapping enabled by default. This is also possible in Xfce, but not by default. To enable, navigate to: [Settings] → [Window manager] → [Advanced tab].

-   Make sure the \"Snap windows to screen border\" checkbox has been *checked*.
-   Make sure the checkboxes under \"Wrap workspaces when reaching the screen edge\" have been *unchecked*. These interfere with vertical window snapping.

Once the checkboxes are set it should be now possible to drag a window to the right or left side of the screen, which should cause the window to resize to 50% of the screen width.

Keyboard shortcuts can be set in order to do this via the typical [Super]+[←] or [Super]+[→] behavior. Navigate to [Settings] → [Window manager] → [Keyboard tab].

Set the \"Tile window to the left\" and \"Tile window to the right\" actions with the [Super]+[←] and [Super]+[→] key combinations respectively.

### [Audio mixer complains about missing pavucontrol binary]

Clicking the speaker (audio) icon in the panel and then selecting [Audio mixer\...] results in a message saying \"pavucontrol binary not found\".

The solution is to install [[[media-sound/pavucontrol]](https://packages.gentoo.org/packages/media-sound/pavucontrol)[]]:

`root `[`#`]`emerge --ask media-sound/pavucontrol`

### [Xfce4-screensaver unable to unlock]

Xfce-screensaver uses gnome-keyring by default to authenticate. By applying the installation method above, gnome-keyring will not be pulled and pam will be unable to service the default configuration installed in /etc/pam.d/xfce4-screensaver. Either pull gnome-keyring, otherwise the file should be modified to allow system-auth to be used on passwords:

[FILE] **`/etc/pam.d/xfce4-screensaver`**

    auth include system-auth
    password include system-auth

### [Authorization or permissions issues]

When experiencing authorization or permissions issues within xfce4 in an OpenRC profile (symptoms include being unable to open power manager and unable to suspend/hibernate) make sure that [[[sys-auth/elogind]](https://packages.gentoo.org/packages/sys-auth/elogind)[]] is installed and [properly configured](https://wiki.gentoo.org/wiki/Elogind "Elogind"), and that the `elogind` USE flag is globally enabled.

If launching with startx, replace the appropriate line in [\~/.xinitrc] with the following:

[FILE] **`~/.xinitrc`Starting xfce4 the right way when invoking startx**

    exec dbus-launch --exit-with-session xfce4-session

### [Dual-monitors get mirrored after monitor suspend]

There are (at least) three ways to solve this issue. First is to save the display settings as the default monitor layout profile, then enable that profile as \"new monitors connect\". There\'s also the option to show a dialog whenever new monitors are detected, which will default to the profile instead of mirroring, when one is available. Navigate to [Settings -\> Display -\> Advanced] to find these options. Remember to configure the display settings before saving the first profile.

2nd way is to kill [xfsettingsd] after logging to the Xfce session. However this will also make some functionality unavailable, such as global hotkeys. A custom script can be created that kills the service, and add that to the autostarting applications list.

3rd is to have a custom script that can be executed via a [.desktop] icon on the desktop, panel, or ran manually each time the monitors are turned on.

Review the monitor IDs using the [xrandr] command.

The custom script could look something like the following:

[FILE] **`~/bin/configuremonitors.sh`configuremonitors.sh**

    xrandr --output HDMI-A-0 --right-of DisplayPort-0 --auto

### [Desktop shows solid color instead of selected wallpaper]

Enable `jpeg` and `tiff` USE flags for [[[x11-libs/gdk-pixbuf]](https://packages.gentoo.org/packages/x11-libs/gdk-pixbuf)[]], then re-emerge it:

[FILE] **`/etc/portage/package.use/xfce`**

    x11-libs/gdk-pixbuf jpeg tiff

`root `[`#`]`emerge --ask --changed-use x11-libs/gdk-pixbuf`

## [See also]

-   [Desktop environment](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") --- provides a list of desktop environments available in Gentoo.

<!-- -->

-   [Xfce/Guide](https://wiki.gentoo.org/wiki/Xfce/Guide "Xfce/Guide") --- provides an extensive introduction to Xfce, a fast, lightweight, full-featured desktop environment.