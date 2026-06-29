Other languages:

-   [English]
-   [français](https://wiki.gentoo.org/wiki/Display_manager/fr "Gestionnaire d'affichage (ou de connexion) (100% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Display_manager/hu "Kijelzőkezelő (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Display_manager/ru "Дисплейный менеджер (100% translated)")
-   [தமிழ்](https://wiki.gentoo.org/wiki/Display_manager/ta "திரை மேலாளர் (100% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Display_manager/ja "ディスプレイマネージャ (100% translated)")

*Not to be confused with [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager").*

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/X_display_manager_(program_type) "wikipedia:X display manager (program type)")

A **display manager** (**DM**), sometimes known as **login manager**, presents the user with a graphical login screen to start a GUI session, either [X](https://wiki.gentoo.org/wiki/Xorg "Xorg") or [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland").

A display manager is not mandatory. X or Wayland can be started from a [shell](https://wiki.gentoo.org/wiki/Shell "Shell") in a [VT](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator"), but a DM can provide extra or useful functionality.

For how to run X without a DM, see [X without Display Manager](https://wiki.gentoo.org/wiki/X_without_Display_Manager "X without Display Manager").

## Contents

-   [[1] [Available software]](#Available_software)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [OpenRC]](#OpenRC)
    -   [[2.2] [systemd]](#systemd)
-   [[3] [See also]](#See_also)

## [Available software]

Some display managers are listed below.

** Note**\
Some Wayland DMs below are found in the overlay [wayland-desktop](https://github.com/bsd-ac/wayland-desktop), but not yet merged to the official Portage tree.

  ------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------- -------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                                                                                                         Package                                                                                                                                                                                                                                                                                                                                                                      Type              Description

  [CDM](https://wiki.gentoo.org/index.php?title=CDM&action=edit&redlink=1 "CDM (page does not exist)")   [[[x11-misc/cdm]](https://packages.gentoo.org/packages/x11-misc/cdm)[]]                   Console           Minimalistic.

  [GNOME/gdm](https://wiki.gentoo.org/wiki/GNOME/gdm "GNOME/gdm")                                [[[gnome-base/gdm]](https://packages.gentoo.org/packages/gnome-base/gdm)[]]             X / Wayland       Often used with GNOME.

  [greetd](https://wiki.gentoo.org/wiki/Greetd "Greetd")                                                       [[[gui-apps/gtkgreet]](https://packages.gentoo.org/packages/gui-apps/gtkgreet)[]]\   Wayland           Frontends for [greetd](https://wiki.gentoo.org/wiki/Greetd "Greetd"). TUIGreetd runs in console.
                                                                                                               [[[gui-apps/tuigreet]](https://packages.gentoo.org/packages/gui-apps/tuigreet)[]]\
                                                                                                               [gui-apps/qtgreet](https://github.com/bsd-ac/wayland-desktop/tree/master/gui-apps/qtgreet)

  [LightDM](https://wiki.gentoo.org/wiki/LightDM "LightDM")                                                    [[[x11-misc/lightdm]](https://packages.gentoo.org/packages/x11-misc/lightdm)[]]       X                 Lightweight, and customizable via greeters.

  [LXDM](https://wiki.gentoo.org/wiki/LXDE "LXDE")                                                             [[[lxde-base/lxdm]](https://packages.gentoo.org/packages/lxde-base/lxdm)[]]             X                 LXDE Display Manager.

  [Qingy](https://wiki.gentoo.org/wiki/Qingy "Qingy")                                                          [[[sys-apps/qingy]](https://packages.gentoo.org/packages/sys-apps/qingy)[]]             console           getty replacement.

  [SDDM](https://wiki.gentoo.org/wiki/SDDM "SDDM")                                                             [[[x11-misc/sddm]](https://packages.gentoo.org/packages/x11-misc/sddm)[]]                X / Wayland       Modern, fast DM aiming to be simple and beautiful. Highly customizable, eye candy display manager from [KDE](https://wiki.gentoo.org/wiki/KDE "KDE").

  [SLiM](https://wiki.gentoo.org/wiki/SLiM "SLiM")                                                             [[[x11-misc/slim]](https://packages.gentoo.org/packages/x11-misc/slim)[]]                X                 Requires only a few dependencies.

  [WDM](https://wiki.gentoo.org/index.php?title=WDM&action=edit&redlink=1 "WDM (page does not exist)")   [[[x11-misc/wdm]](https://packages.gentoo.org/packages/x11-misc/wdm)[]]                   X                 Modification of XDM.

  XDM                                                                                                          [[[x11-apps/xdm]](https://packages.gentoo.org/packages/x11-apps/xdm)[]]                   X                 X.Org\'s DM.
  ------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------- -------------------------------------------------------------------------------------------------------------------------------------------------------

## [Configuration]

** Warning**\
Before setting up and using a display manager, be sure that the chosen GUI environment, [startx](https://wiki.gentoo.org/wiki/Xorg/Guide#Using_startx "Xorg/Guide") or [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland"), works without problems. If something does not work refer to the troubleshooting guides, such as [Xorg/Guide](https://wiki.gentoo.org/wiki/Xorg/Guide "Xorg/Guide").

In all major Linux operating systems, display managers are started automatically on boot. In order for this to happen automatically, a script must be added to the init system\'s appropriate runlevel. Examples for [OpenRC](https://wiki.gentoo.org/wiki/Display_manager#OpenRC "Display manager") and [systemd](https://wiki.gentoo.org/wiki/Display_manager#systemd "Display manager") are provided below.

### [OpenRC]

Under most circumstances, the [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") init system (Gentoo\'s default [init system](https://wiki.gentoo.org/wiki/Init_system "Init system")) will be used to start the display manager. The following examples will set [SDDM](https://wiki.gentoo.org/wiki/SDDM "SDDM") as the display manager, adjust as necessary for other display managers.

If [[[gui-libs/display-manager-init]](https://packages.gentoo.org/packages/gui-libs/display-manager-init)[]] is not present, emerge it with:

`root `[`#`]`emerge --ask gui-libs/display-manager-init`

The configuration file should be modified to use [SDDM](https://wiki.gentoo.org/wiki/SDDM "SDDM"):

[FILE] **`/etc/conf.d/display-manager`Set SDDM as the display manager**

    CHECKVT=7
    DISPLAYMANAGER="sddm"

To start the chosen display manager on boot, add the *display-manager* to the system\'s *default* runlevel:

`root `[`#`]`rc-update add display-manager default`

To start the *display-manager* immediately, run:

`root `[`#`]`rc-service display-manager start`

### [systemd]

If using [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") as the init system, first locate the chosen [\<display-manager\>.service] file.

To start [SDDM](https://wiki.gentoo.org/wiki/SDDM "SDDM") on boot, enable the service:

`root `[`#`]`systemctl enable sddm.service`

To start [SDDM](https://wiki.gentoo.org/wiki/SDDM "SDDM") immediately, run:

`root `[`#`]`systemctl start sddm.service`

## [See also]

-   [Desktop environment](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") --- provides a list of desktop environments available in Gentoo.
-   [Login](https://wiki.gentoo.org/wiki/Login "Login") --- logging in to a shell, and setting up the default environment.
-   [Window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager") --- manages the creation, manipulation, and destruction of on-screen windows and window decorations in [Xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg").
-   [Xorg/Guide](https://wiki.gentoo.org/wiki/Xorg/Guide "Xorg/Guide") --- explains what Xorg is, how to install it, and the various configuration options.
-   [X without Display Manager](https://wiki.gentoo.org/wiki/X_without_Display_Manager "X without Display Manager") --- describes how to start an X11 session without a display manager