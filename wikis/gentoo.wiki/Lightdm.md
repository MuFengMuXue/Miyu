This page contains [[changes](https://wiki.gentoo.org/index.php?title=LightDM&oldid=1417715&diff=1419174)] which are not marked for translation.

Other languages:

-   [English]
-   [français](https://wiki.gentoo.org/wiki/LightDM/fr "LightDM (92% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/LightDM/it "LightDM (36% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/LightDM/hu "LightDM (92% translated)")
-   [português do Brasil](https://wiki.gentoo.org/wiki/LightDM/pt-br "LightDM (36% translated)")
-   [čeština](https://wiki.gentoo.org/wiki/LightDM/cs "LightDM/cs (4% translated)")
-   [русский](https://wiki.gentoo.org/wiki/LightDM/ru "LightDM (56% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/LightDM/zh-cn "LightDM (35% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/LightDM/ja "LightDM (99% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/LightDM/ko "LightDM (36% translated)")

**Resources**

[[]][Package information](https://packages.gentoo.org/packages/x11-misc/lightdm)

[[]][Wikipedia](https://en.wikipedia.org/wiki/LightDM "wikipedia:LightDM")

[[]][GitHub](https://github.com/canonical/lightdm)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/lightdm)

**LightDM** is a cross-desktop [display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager") whose aim is to be the standard display manager for the X server.

The key features (as listed by upstream) include:

-   A well-defined greeter API allowing multiple GUIs.
-   Support for all display manager use cases, with plugins where appropriate.
-   Low code complexity.
-   Fast performance.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [GTK]](#GTK)
    -   [[2.2] [Qt]](#Qt)
    -   [[2.3] [Boot service]](#Boot_service)
        -   [[2.3.1] [OpenRC]](#OpenRC)
            -   [[2.3.1.1] [With display-manager]](#With_display-manager)
            -   [[2.3.1.2] [With the deprecated xdm init script]](#With_the_deprecated_xdm_init_script)
        -   [[2.3.2] [systemd]](#systemd)
    -   [[2.4] [Command-line tool]](#Command-line_tool)
-   [[3] [Tips]](#Tips)
    -   [[3.1] [Running commands at log-in]](#Running_commands_at_log-in)
    -   [[3.2] [Unlock GNOME Keyring]](#Unlock_GNOME_Keyring)
    -   [[3.3] [Locking the screen with elogind after suspend or sleep]](#Locking_the_screen_with_elogind_after_suspend_or_sleep)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [LightDM crashes upon first login if hostname changes during login]](#LightDM_crashes_upon_first_login_if_hostname_changes_during_login)
    -   [[4.2] [LightDM fails to launch with Nvidia GPU]](#LightDM_fails_to_launch_with_Nvidia_GPU)
-   [[5] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [x11-misc/lightdm](https://packages.gentoo.org/packages/x11-misc/lightdm) [[]] [A lightweight display manager]

  ------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------
  [`+gnome`](https://packages.gentoo.org/useflags/+gnome)                   Add GNOME support
  [`+gtk`](https://packages.gentoo.org/useflags/+gtk)                       Pull in the gtk+ greeter
  [`+introspection`](https://packages.gentoo.org/useflags/+introspection)   Add support for GObject based introspection
  [`X`](https://packages.gentoo.org/useflags/X)                             Add support for X11
  [`audit`](https://packages.gentoo.org/useflags/audit)                     Enable support for Linux audit subsystem using sys-process/audit
  [`elogind`](https://packages.gentoo.org/useflags/elogind)                 Enable session tracking via sys-auth/elogind
  [`non-root`](https://packages.gentoo.org/useflags/non-root)               Use non-root user by default
  [`systemd`](https://packages.gentoo.org/useflags/systemd)                 Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`vala`](https://packages.gentoo.org/useflags/vala)                       Enable bindings for dev-lang/vala
  ------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-10-26 03:26] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[x11-misc/lightdm]](https://packages.gentoo.org/packages/x11-misc/lightdm)[]]:

`root `[`#`]`emerge --ask x11-misc/lightdm`

## [Configuration]

The (global) configuration file for LightDM can be found at [/etc/lightdm/lightdm.conf]. Upon successful authentication, LightDM starts an Xsession through the following configuration option (enabled by default):

[FILE] **`/etc/lightdm/lightdm.conf`**

    [Seat:*]
    ...
    session-wrapper=/etc/lightdm/Xsession
    ...

### [GTK]

The greeter allows to select logging into one of the installed type of sessions through the icon in the Panel on top of the display. This makes it unnecessary to configure the session startup through user profile configurations. For example, [[[xfce-base/xfce4-session]](https://packages.gentoo.org/packages/xfce-base/xfce4-session)[]] installs [/usr/share/xsessions/xfce.desktop] which enables the greeter to offer the [Xfce](https://wiki.gentoo.org/wiki/Xfce "Xfce") session. The default is an Xsession which relies on user profile files.

The GTK greeter configuration can be modified by manually editing the following file:

[/etc/lightdm/lightdm-gtk-greeter.conf]

### [Qt]

Currently Gentoo does not support the Qt greeter since it was moved out into it\'s own project at [https://github.com/surlykke/qt-lightdm-greeter](https://github.com/surlykke/qt-lightdm-greeter) however USE flag support is in the [[[x11-misc/lightdm]](https://packages.gentoo.org/packages/x11-misc/lightdm)[]] package if someone wanted to add the greeter support.

### [Boot service]

#### [OpenRC]

##### [With display-manager]

`root `[`#`]`emerge --ask gui-libs/display-manager-init`

Set LightDM as the default display manager:

[FILE] **`/etc/conf.d/display-manager`**

    DISPLAYMANAGER="lightdm"

To start LightDM on boot, add dbus and display-manager to the default runlevel. [dbus](https://wiki.gentoo.org/wiki/Dbus "Dbus") is necessary because LightDM depends on it to pass messages:

`root `[`#`]`rc-update add dbus default `

`root `[`#`]`rc-update add display-manager default`

To start LightDM now:

`root `[`#`]`rc-service dbus start `

`root `[`#`]`rc-service display-manager start`

##### [With the deprecated xdm init script]

Set LightDM as the default display manager:

[FILE] **`/etc/conf.d/xdm`**

    DISPLAYMANAGER="lightdm"

To start LightDM on boot, add dbus and xdm to the default runlevel. [dbus](https://wiki.gentoo.org/wiki/Dbus "Dbus") is necessary because LightDM depends on it to pass messages:

`root `[`#`]`rc-update add dbus default`

`root `[`#`]`rc-update add xdm default`

To start LightDM now:

`root `[`#`]`/etc/init.d/dbus start`

`root `[`#`]`/etc/init.d/xdm start`

#### [systemd]

To start LightDM on boot:

`root `[`#`]`systemctl enable lightdm`

To start LightDM now:

`root `[`#`]`systemctl start lightdm`

### [Command-line tool]

LightDM includes a command-line tool, [dm-tool], which can be used to switch user sessions, lock the current [seat](https://wiki.gentoo.org/wiki/Multiseat "Multiseat"), etc. To see a list of available commands, use the `--help` option:

`user `[`$`]`dm-tool --help`

For example, to lock the current seat:

`user `[`$`]`dm-tool lock`

## [Tips]

### [Running commands at log-in]

A user can run some programs automatically when logging in using LightDM by adding commands in [\~/.xprofile], which will be sourced by LightDM. For example:

[FILE] **`~/.xprofile`**

    # Starting redshift, setting the dpi with xrandr and set the brightness to 50% with xbacklight
    xrandr --dpi 192 &
    redshift-gtk &
    xbacklight -set 50 &

### [Unlock GNOME Keyring]

To unlock your GNOME Keyring ([[[gnome-base/gnome-keyring]](https://packages.gentoo.org/packages/gnome-base/gnome-keyring)[]]) automatically on login, edit [/etc/pam.d/lightdm] to look as follows. Note: Lines ending with the comment `#keyring` should be added.

[FILE] **`/etc/pam.d/lightdm`**

    auth     substack        system-local-login
    auth     optional        pam_gnome_keyring.so #keyring
    account  substack        system-local-login
    password substack        system-local-login
    session  substack        system-local-login
    session  optional        pam_gnome_keyring.so auto_start #keyring

### [Locking the screen with elogind after suspend or sleep]

For security, it is good practice to lock the screen after [elogind](https://wiki.gentoo.org/wiki/Elogind "Elogind") triggers suspend or sleep. This can be done easily by doing the following:

Install light-locker:

`root `[`#`]`emerge --ask x11-misc/light-locker`

Start light-locker after the X server has started by putting [light-locker &] into either an [\~/.xprofile] or [\~/.xinitrc] file.

[FILE] **`~/.xprofile`**

    # Starting light-lock with X session
    light-locker &

Create a [lock.sh] file under [/lib64/elogind/system-sleep/] (be sure to add execute permissions to the file):

`root `[`#`]`chmod +x /lib64/elogind/system-sleep/lock.sh`

## [Troubleshooting]

### [LightDM crashes upon first login if hostname changes during login]

In some cases LightDM may crash when trying to log in for the first time if the hostname changes in the time between the boot and login ([launchpad bug #1677058](https://bugs.launchpad.net/ubuntu/+source/lightdm-gtk-greeter/+bug/1677058)).

This may be encountered if [[[net-misc/networkmanager]](https://packages.gentoo.org/packages/net-misc/networkmanager)[]] is using the default settings to obtain the hostname from DHCP server and the hostname differs from the default one set on boot.

To disable NetworkManager hostname setting behavior, set the following line in `[main]` section of [/etc/NetworkManager/NetworkManager.conf]:

[FILE] **`/etc/NetworkManager/NetworkManager.conf`**

    [main]
    ...
    hostname-mode=none
    ...

### [LightDM fails to launch with Nvidia GPU]

Users with Nvidia GPUs may encounter failures when using LightDM ([GitHub issue #263](https://github.com/canonical/lightdm/issues/263)).

A workaround for this issue involves editing [/etc/lightdm/lightdm.conf] and adding the line `logind-check-graphical=false` within the `[LightDM]` section.

[FILE] **`/etc/lightdm/lightdm.conf`**

    [LightDM]
    ...
    logind-check-graphical=false
    ...

## [See also]

-   [SDDM](https://wiki.gentoo.org/wiki/SDDM "SDDM") --- a modern [display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager") that supports both the [X server](https://wiki.gentoo.org/wiki/X_server "X server") and the [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") protocol.