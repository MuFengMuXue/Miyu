**Resources**

[[]][Home](http://unity.ubuntu.com)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Unity_(user_interface) "wikipedia:Unity (user interface)")

**Unity** is an alternative shell for the [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME") desktop environment, developed by Canonical in its Ayatana project.

It consists of several components including the Launcher, Dash, Lenses, Panel and Indicators.

More info about its individual components can be found at [Ubuntu\'s Unity article](https://wiki.ubuntu.com/Unity)

Unity is currently a plugin of the *[Compiz](https://wiki.gentoo.org/wiki/Compiz "Compiz")* window manager.

Under Canonical\'s developing convergence plans it will soon be a QT5 QML Desktop using their Mir [display server](https://wiki.gentoo.org/wiki/Display_server "Display server").

Mir is being developed as an alternative display server to X or Wayland, more info about it can be found at [Ubuntu\'s Mir article](https://wiki.ubuntu.com/Mir)

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [unity-gentoo]](#unity-gentoo)
    -   [[1.2] [gentoo-unity7]](#gentoo-unity7)
-   [[2] [Usage]](#Usage)
-   [[3] [Technical]](#Technical)
    -   [[3.1] [Startup files]](#Startup_files)
-   [[4] [External resources]](#External_resources)

## [Installation]

### [unity-gentoo]

** Warning**\
As of Feb 12, 2023, the *unity-gentoo* overlay is not maintained. You can try [gentoo-unity7](https://wiki.gentoo.org/wiki/Unity#gentoo-unity7 "Unity") overlay instead.

** Warning**\
The *unity-gentoo* overlay has not been updated to support elogind and hence hard-requires systemd, seemingly unnecessarily.

You can install Unity by adding the [*unity-gentoo*](https://github.com/shiznix/unity-gentoo) [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") via [eselect repository](https://wiki.gentoo.org/wiki/Eselect/Repository "Eselect/Repository"):

`root `[`#`]`eselect repository enable unity-gentoo`

Select one of the \'unity-gentoo\' profiles:

** Warning**\
Ensure to keep the same profile version as the system starts with. New installs are 23.0 by default on amd64. Selecting a 17.0 profile from a 23.0 starting point will be disastrous once emerge installs files.

Once \'unity-gentoo\' profile has been installed, make sure you sync it up.

`root `[`#`]`emerge --sync`

or

`root `[`#`]`emerge-webrsync`

Then verify its installation:

`root `[`#`]`eselect profile list`

Emerge *unity-base/unity-build-env*:

`root `[`#`]`emerge -av unity-build-env`

Finally, emerge *unity-base/unity-meta*:

`root `[`#`]`emerge -uDNavt unity-meta`

### [gentoo-unity7]

Alternatively, you can install Gentoo Unity⁷ Desktop from [*gentoo-unity7*](https://github.com/c4pp4/gentoo-unity7) overlay.

## [Usage]

You should be starting it via a [display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager") or by setting `XSESSION=unity` for [startx]:

`root `[`#`]`systemctl start lightdm`

`user `[`$`]`XSESSION=unity startx`

## [Technical]

At its core Unity uses a lot of Gnome, and since \>=gnome-3.8 systemd is required.

[Project:GNOME/GNOME3 upgrade guide#Systemd](https://wiki.gentoo.org/wiki/Project:GNOME/GNOME3_upgrade_guide#Systemd "Project:GNOME/GNOME3 upgrade guide")

GNOME 3 requires systemd to be running to get it working properly, otherwise, you will get broken power management and multiseat handling, and also some more problems because upstream has moved away from the obsolete consolekit to logind (that needs systemd to be running to work).

### [Startup files]

1.  The display manager (lightdm) or XSESSION=unity and \'startx\' uses the *sys-apps/upstart* desktop services daemon to start \'gnome-session \--session=unity\'
    This executes /usr/share/gnome-session/sessions/unity.session which starts compiz as the window manager.
2.  /etc/X11/xinit/xinitrc.d/65compiz_profile-on-session is sourced at Xsession startup and if \$DESKTOP_SESSION=unity, it sets the COMPIZ_CONFIG_PROFILE=ubuntu variable.
    When compiz starts it checks the value of \$COMPIZ_CONFIG_PROFILE and uses the \'ubuntu\' entry located in /etc/compizconfig/config
    This \'ubuntu\' entry sets the compiz profile to \'unity\' and sets the compizconfig backend to use gsettings (dconf) which reads the compiz settings from the dconf registry.
3.  Default compizconfig settings find their way into the desktop user\'s dconf registry by way of /etc/xdg/autostart/compiz-migrate-to-dconf.desktop
    This is auto started at Xsession startup and actually copies the settings from the global gconf registry to the desktop user\'s dconf registry.
4.  Default compizconfig settings find their way into the global gconf registry when compiz is emerged.
    At src_install() time the compiz ebuild uses the \'update-gconf-defaults\' tool to read all files in /usr/share/gconf/defaults/ and write them out to a gconf registry file located in /etc/gconf/gconf.xml.unity/
    It then updates /etc/gconf/2/local-defaults.path to include the new /etc/gconf/gconf.xml.unity/ directory

## [External resources]

-   [unity-gentoo ebuild repository](https://github.com/shiznix/unity-gentoo)
-   [gentoo-unity7 ebuild repository](https://github.com/c4pp4/gentoo-unity7)
-   [Overlay unity-gentoo thread on Gentoo Forum](https://forums.gentoo.org/viewtopic-p-7091922.html#7091922)
-   [Unity article in Arch Linux Wiki](https://wiki.archlinux.org/index.php/Unity)