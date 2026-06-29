This page contains [[changes](https://wiki.gentoo.org/index.php?title=KDE&oldid=1432108&diff=1440300)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/KDE/de "KDE (53% translated)")
-   [English]
-   [Türkçe](https://wiki.gentoo.org/wiki/KDE/tr "KDE (7% translated)")
-   [español](https://wiki.gentoo.org/wiki/KDE/es "KDE (82% translated)")
-   [français](https://wiki.gentoo.org/wiki/KDE/fr "KDE (99% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/KDE/it "KDE (100% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/KDE/hu "KDE (99% translated)")
-   [polski](https://wiki.gentoo.org/wiki/KDE/pl "KDE/pl (0% translated)")
-   [português do Brasil](https://wiki.gentoo.org/wiki/KDE/pt-br "KDE (44% translated)")
-   [čeština](https://wiki.gentoo.org/wiki/KDE/cs "KDE (5% translated)")
-   [русский](https://wiki.gentoo.org/wiki/KDE/ru "KDE (100% translated)")
-   [українська](https://wiki.gentoo.org/wiki/KDE/uk "KDE (7% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/KDE/zh-cn "KDE (73% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/KDE/ja "KDE (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/KDE/ko " KDE (18% translated)")

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:KDE "Project:KDE")][Project](https://wiki.gentoo.org/wiki/Project:KDE "Project:KDE")

[[]][Home](https://www.kde.org/)

[[]][Package information](https://packages.gentoo.org/packages/kde-plasma/plasma-meta)

[[]][Wikipedia](https://en.wikipedia.org/wiki/KDE "wikipedia:KDE")

**KDE** is a free software community, producing a wide range of applications including the popular Plasma desktop environment.

Gentoo support for the KDE project is excellent, with comprehensive packaging of KDE Frameworks, Plasma, and Applications, as well as a wide array of other miscellaneous KDE-based software.

## Contents

-   [[1] [Prerequisites]](#Prerequisites)
    -   [[1.1] [Profile]](#Profile)
        -   [[1.1.1] [Combined hardened profiles]](#Combined_hardened_profiles)
    -   [[1.2] [Services]](#Services)
        -   [[1.2.1] [Session tracker]](#Session_tracker)
        -   [[1.2.2] [Device manager]](#Device_manager)
        -   [[1.2.3] [Miscellaneous]](#Miscellaneous)
    -   [[1.3] [X server]](#X_server)
    -   [[1.4] [Wayland]](#Wayland)
-   [[2] [Plasma]](#Plasma)
    -   [[2.1] [Available versions]](#Available_versions)
    -   [[2.2] [Installation]](#Installation)
        -   [[2.2.1] [USE flags]](#USE_flags)
        -   [[2.2.2] [Emerge]](#Emerge)
    -   [[2.3] [Starting Plasma]](#Starting_Plasma)
        -   [[2.3.1] [Display manager]](#Display_manager)
        -   [[2.3.2] [No display manager]](#No_display_manager)
    -   [[2.4] [Widgets]](#Widgets)
    -   [[2.5] [KWallet]](#KWallet)
        -   [[2.5.1] [KWallet auto-unlocking]](#KWallet_auto-unlocking)
        -   [[2.5.2] [Disabling KWallet]](#Disabling_KWallet)
    -   [[2.6] [SSH/GPG Agent startup/shutdown scripts]](#SSH.2FGPG_Agent_startup.2Fshutdown_scripts)
    -   [[2.7] [Non-root user authentication for dialogs]](#Non-root_user_authentication_for_dialogs)
    -   [[2.8] [Run GUI applications with root privileges]](#Run_GUI_applications_with_root_privileges)
    -   [[2.9] [Files]](#Files)
    -   [[2.10] [Removal]](#Removal)
-   [[3] [Applications]](#Applications)
    -   [[3.1] [Available versions]](#Available_versions_2)
    -   [[3.2] [Installation]](#Installation_2)
    -   [[3.3] [Localization]](#Localization)
    -   [[3.4] [KDE PIM]](#KDE_PIM)
-   [[4] [Frameworks]](#Frameworks)
    -   [[4.1] [Available versions]](#Available_versions_3)
-   [[5] [More KDE software]](#More_KDE_software)
-   [[6] [Troubleshooting]](#Troubleshooting)
-   [[7] [See also]](#See_also)
-   [[8] [External links]](#External_links)
-   [[9] [References]](#References)

## [Prerequisites]

### [Profile]

** Important**\
Read [relevant documentation](https://wiki.gentoo.org/wiki/Profile_(Portage)#Switching_between_profiles "Profile (Portage)") before performing any profile changes.

Choosing an appropriate [profile](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)"), although not required, is recommended as it sets a number of global and package-specific USE flags to ease installation and ensure a smooth KDE experience.

In order to choose the most suitable profile, first list what\'s available:

`root `[`#`]`eselect profile list`

      ...
      [21]  default/linux/amd64/23.0 (stable)
      [22]  default/linux/amd64/23.0/systemd (stable)
      [23]  default/linux/amd64/23.0/desktop (stable)
      [24]  default/linux/amd64/23.0/desktop/systemd (stable)
      [25]  default/linux/amd64/23.0/desktop/gnome (stable)
      [26]  default/linux/amd64/23.0/desktop/gnome/systemd (stable)
      [27]  default/linux/amd64/23.0/desktop/plasma (stable)
      [28]  default/linux/amd64/23.0/desktop/plasma/systemd (stable)
      ...

Then, select the right profile, substituting `X` with the appropriate profile number:

`root `[`#`]`eselect profile set X`

For Plasma desktop environment choose `desktop/plasma` with [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") or `desktop/plasma/systemd` with [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd"). Note that other USE flag combinations than set by the profile may technically be possible (especially if selected applications are run instead of a full KDE Plasma desktop environment), but may be unsupported, untested, or lead to unexpected loss of functionality.

#### [Combined hardened profiles]

Users that run hardened profiles can also combine it with all the features of the plasma desktop profile. For steps on doing this please follow [KDE/Hardened_KDE_Plasma_profile](https://wiki.gentoo.org/wiki/KDE/Hardened_KDE_Plasma_profile "KDE/Hardened KDE Plasma profile").

### [Services]

Default choices of these services will be pulled in automatically - by the installation steps in the following chapters - depending on the [profile](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)") selection made earlier, but still need to be set up properly before starting KDE Plasma for the first time. For deviating from the defaults, it is recommended to install them in advance of KDE Plasma or KDE Gear via [emerge \--oneshot] so that [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") will take them into account. Follow the links for information how to set up these services.

#### [Session tracker]

Choose exactly one of:

-   [elogind](https://wiki.gentoo.org/wiki/Elogind "Elogind"): Standalone logind package, default for [desktop/plasma] profile, extracted from systemd project for use with [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") or other init systems.
-   [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd"): Uses the session tracker part of systemd. Users of systemd do not need to take any other initiative here.

#### [Device manager]

** Tip**\
By default, systemd-utils is used on OpenRC systems, and systemd is used on systemd systems. Users who don\'t want to change providers should skip this step.

Choose exactly one of:

-   [udev](https://wiki.gentoo.org/wiki/Udev "Udev"): Enables support for udev Linux dynamic and persistent device naming.
-   [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd"): Uses the device manager part of systemd. Users of systemd do not need to take any other initiative here.

#### [Miscellaneous]

-   [D-Bus](https://wiki.gentoo.org/wiki/D-Bus "D-Bus"): Enables use of the D-Bus message bus system.
-   [PipeWire](https://wiki.gentoo.org/wiki/PipeWire "PipeWire"): PipeWire is used for sound as well as screensharing and window previews on Wayland.
-   [polkit](https://wiki.gentoo.org/wiki/Polkit "Polkit"): Enables the polkit framework for controlling privileges for system-wide services.
-   [udisks](https://wiki.gentoo.org/wiki/Udisks "Udisks"): Enables support for some storage related services.

### [X server]

Read and follow the instructions in the [X server](https://wiki.gentoo.org/wiki/X_server "X server") article to setup the X environment.

### [Wayland]

In Plasma 6, Wayland is the default session. Many users have been shifted to a Wayland session without even realizing.

Starting from Plasma 6.2.1 in Gentoo, [[[kde-plasma/plasma-login-sessions]](https://packages.gentoo.org/packages/kde-plasma/plasma-login-sessions)[]] controls the default Plasma session via USE flags:

### [USE flags for] [kde-plasma/plasma-login-sessions](https://packages.gentoo.org/packages/kde-plasma/plasma-login-sessions) [[]] [KDE Plasma login sessions]

  ------------------------------------------------------------- ------------------------------------------------------------------------------------
  [`+wayland`](https://packages.gentoo.org/useflags/+wayland)   Install Wayland session file for Display Managers
  [`X`](https://packages.gentoo.org/useflags/X)                 Install X11 session file for Display Managers (default is Wayland if both enabled)
  ------------------------------------------------------------- ------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-25 06:18] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

Users can set [[[X]](https://packages.gentoo.org/useflags/X)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] or [[[wayland]](https://packages.gentoo.org/useflags/wayland)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] on this package if they wish to control the default.

For Plasma 6, have a system with applicable `VIDEO_CARDS` USE expand settings and kernel with DRMs (Direct Rendering Manager) enabled for Mesa. KWin, the window manager and Wayland compositor, uniquely falls back to low performance software Rendering if unsatisfied.

## [Plasma]

Plasma 6 is the current generation of KDE\'s desktop environment, based on Qt 6 and KDE Frameworks 6.

### [Available versions]

  ------------------------------ ------------------------------------ ----------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  KDE                            Gentoo                               Ebuild repository                                                                   Status
  KDE Plasma 6.6.4               kde-plasma/plasma-meta-6.6.4         gentoo                                                                              Stable for **[amd64]** and **[arm64]**; testing for **[loong]**, **[ppc64]**, **[riscv]** and **[x86]**
  KDE Plasma 6.6.5               kde-plasma/plasma-meta-6.6.5         gentoo                                                                              Testing for **[amd64]**, **[arm64]**, **[loong]**, **[ppc64]**, **[riscv]** and **[x86]**
  KDE Plasma 6.6 stable branch   kde-plasma/plasma-meta-6.6.49.9999   [KDE](https://wiki.gentoo.org/wiki/KDE/Ebuild_repository "KDE/Ebuild repository")   Live version
  KDE Plasma 6 master branch     kde-plasma/plasma-meta-9999          [KDE](https://wiki.gentoo.org/wiki/KDE/Ebuild_repository "KDE/Ebuild repository")   Live version
  ------------------------------ ------------------------------------ ----------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

** Note**\
Before proceeding, make sure to choose a Plasma profile.

### [Installation]

#### [USE flags]

The [[[kde-plasma/plasma-meta]](https://packages.gentoo.org/packages/kde-plasma/plasma-meta)[]] package provides the full Plasma desktop, configurable by a wealth of USE flags:

### [USE flags for] [kde-plasma/plasma-meta](https://packages.gentoo.org/packages/kde-plasma/plasma-meta) [[]] [Merge this to pull in all Plasma 6 packages]

  ------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------
  [`+browser-integration`](https://packages.gentoo.org/useflags/+browser-integration)   Enable integration with Chrome/Firefox with browser extensions
  [`+crash-handler`](https://packages.gentoo.org/useflags/+crash-handler)               Pull in kde-plasma/drkonqi for assisted upstream crash reports
  [`+display-manager`](https://packages.gentoo.org/useflags/+display-manager)           Pull in a graphical display manager
  [`+elogind`](https://packages.gentoo.org/useflags/+elogind)                           Enable session tracking via sys-auth/elogind
  [`+firewall`](https://packages.gentoo.org/useflags/+firewall)                         Pull in kde-plasma/plasma-firewall for system firewall administration
  [`+kwallet`](https://packages.gentoo.org/useflags/+kwallet)                           Enable support for KWallet auto-unlocking via kde-plasma/kwallet-pam
  [`+networkmanager`](https://packages.gentoo.org/useflags/+networkmanager)             Enable net-misc/networkmanager support
  [`+sddm`](https://packages.gentoo.org/useflags/+sddm)                                 Pull in the x11-misc/sddm display manager and system settings module
  [`+smart`](https://packages.gentoo.org/useflags/+smart)                               Pull in kde-plasma/plasma-disks for disk health monitoring
  [`+wallpapers`](https://packages.gentoo.org/useflags/+wallpapers)                     Install wallpapers for the Plasma Workspace
  [`+xwayland`](https://packages.gentoo.org/useflags/+xwayland)                         Enable Wayland windows screensharing to XWayland applications via gui-apps/xwaylandvideobridge
  [`X`](https://packages.gentoo.org/useflags/X)                                         Add support for X11
  [`accessibility`](https://packages.gentoo.org/useflags/accessibility)                 Add support for accessibility (eg \'at-spi\' library)
  [`bluetooth`](https://packages.gentoo.org/useflags/bluetooth)                         Enable Bluetooth Support
  [`crypt`](https://packages.gentoo.org/useflags/crypt)                                 Pull in kde-plasma/plasma-vault for encrypted vaults integration
  [`cups`](https://packages.gentoo.org/useflags/cups)                                   Add support for CUPS (Common Unix Printing System)
  [`discover`](https://packages.gentoo.org/useflags/discover)                           Pull in resources management GUI; a centralised GHNS alternative and optional sys-apps/fwupd frontend
  [`flatpak`](https://packages.gentoo.org/useflags/flatpak)                             Pull in kde-plasma/flatpak-kcm for flatpak permissions administration
  [`grub`](https://packages.gentoo.org/useflags/grub)                                   Pull in Breeze theme for sys-boot/grub
  [`gtk`](https://packages.gentoo.org/useflags/gtk)                                     Enable Breeze widget style and system settings module for GTK+
  [`ocr`](https://packages.gentoo.org/useflags/ocr)                                     Enable Optical Character Recognition support via app-text/tesseract
  [`oxygen-theme`](https://packages.gentoo.org/useflags/oxygen-theme)                   Pull in Oxygen icons, sound theme and visual style for KDE Plasma
  [`plymouth`](https://packages.gentoo.org/useflags/plymouth)                           Pull in Breeze theme for sys-boot/plymouth
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)                       Install Plasma applet for PulseAudio volume management
  [`rdp`](https://packages.gentoo.org/useflags/rdp)                                     Enables RDP/Remote Desktop support
  [`sdk`](https://packages.gentoo.org/useflags/sdk)                                     Pull in kde-plasma/plasma-sdk for Plasma development
  [`systemd`](https://packages.gentoo.org/useflags/systemd)                             Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`thunderbolt`](https://packages.gentoo.org/useflags/thunderbolt)                     Pull in kde-plasma/plasma-thunderbolt control center module
  [`unsupported`](https://packages.gentoo.org/useflags/unsupported)                     Allow packages that are known to ruin runtime experience \*\* DO NOT FILE BUGS WITH THIS ENABLED \*\*
  [`virtualkeyboard`](https://packages.gentoo.org/useflags/virtualkeyboard)             Pull in kde-plasma/plasma-keyboard
  [`wacom`](https://packages.gentoo.org/useflags/wacom)                                 Pull in kde-plasma/wacomtablet control center module
  [`webengine`](https://packages.gentoo.org/useflags/webengine)                         Use kde-apps/khelpcenter to access the locally installed KDE Help System Handbook
  ------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-25 06:18] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

#### [Emerge]

`root `[`#`]`emerge --ask kde-plasma/plasma-meta`

Alternatively, [[[kde-plasma/plasma-desktop]](https://packages.gentoo.org/packages/kde-plasma/plasma-desktop)[]] provides a very basic desktop, leaving users free to install only the extra packages they require - or rather, figure out missing features on their own.

** Warning**\
Please note that installing just [[[kde-plasma/plasma-desktop]](https://packages.gentoo.org/packages/kde-plasma/plasma-desktop)[]] will exclude important packages needed for KDE Plasma to function, such as [[[kde-plasma/powerdevil]](https://packages.gentoo.org/packages/kde-plasma/powerdevil)[]] (power management, suspend and hibernate options), [[[kde-plasma/systemsettings]](https://packages.gentoo.org/packages/kde-plasma/systemsettings)[]], and many more. This package should be used with the understanding that additional packages will need to be installed to ensure a functioning environment. Do not expect support when using this package.

### [Starting Plasma]

#### [Display manager]

[SDDM](https://wiki.gentoo.org/wiki/SDDM "SDDM") (Simple Desktop Display Manager) is the recommended login manager and is pulled in automatically via [[[kde-plasma/plasma-meta]](https://packages.gentoo.org/packages/kde-plasma/plasma-meta)[]] by default. This is the preferred option. Alternatively, [LightDM](https://wiki.gentoo.org/wiki/LightDM "LightDM") can be used and pulled in by setting USE flag `-sddm` for [[[kde-plasma/plasma-meta]](https://packages.gentoo.org/packages/kde-plasma/plasma-meta)[]]. Change the setting accordingly in [/etc/conf.d/display-manager]. Also, be sure to read through the [SDDM](https://wiki.gentoo.org/wiki/SDDM "SDDM") page if further issues appear.

#### [No display manager]

Plasma can be started the old-fashioned way with [startx], but extra care needs to be taken to ensure it gets a valid session.

[FILE] **`~/.xinitrc`**

    #!/bin/sh
    exec dbus-launch --exit-with-session startplasma-x11

When using [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland"), Plasma can be launched with [dbus-run-session startplasma-wayland].

This can be added to a user\'s profile file which will be executed when logging in:

[FILE] **`~/.profile`**

    #!/bin/sh
    dbus-run-session startplasma-wayland

### [Widgets]

Many useful widgets are in the [[[kde-plasma/kdeplasma-addons]](https://packages.gentoo.org/packages/kde-plasma/kdeplasma-addons)[]] package (already pulled in by [[[kde-plasma/plasma-meta]](https://packages.gentoo.org/packages/kde-plasma/plasma-meta)[]]):

`root `[`#`]`emerge --ask kde-plasma/kdeplasma-addons`

### [KWallet]

Many users will be introduced to [[[kde-frameworks/kwallet]](https://packages.gentoo.org/packages/kde-frameworks/kwallet)[]], Plasma\'s encrypted password storage, while adding a (wireless) network connection after login or adding E-Mail accounts in [[[kde-apps/kmail]](https://packages.gentoo.org/packages/kde-apps/kmail)[]].

For managing KWallets, importing and exporting passwords, there is [[[kde-apps/kwalletmanager]](https://packages.gentoo.org/packages/kde-apps/kwalletmanager)[]]:

`root `[`#`]`emerge --ask kde-apps/kwalletmanager`

#### [KWallet auto-unlocking]

[[[kde-plasma/kwallet-pam]](https://packages.gentoo.org/packages/kde-plasma/kwallet-pam)[]] provides a mechanism to avoid being subsequently asked for access to kwallet after login.

`root `[`#`]`emerge --ask kde-plasma/kwallet-pam`

It requires the following setup:

-   For KWallet security, use classic blowfish encryption instead of GPG
-   Choose same password for login and kwallet
-   Configure a display manager with support for PAM - both [[[x11-misc/sddm]](https://packages.gentoo.org/packages/x11-misc/sddm)[]] and [[[x11-misc/lightdm]](https://packages.gentoo.org/packages/x11-misc/lightdm)[]] fulfill that requirement:

[FILE] **`/etc/pam.d/sddm`Config lines for KWallet PAM unlocking via SDDM**

    -auth           optional        pam_kwallet5.so
    -session        optional        pam_kwallet5.so auto_start

For unlocking on tty login (no display manager, or like [[[gui-apps/tuigreet]](https://packages.gentoo.org/packages/gui-apps/tuigreet)[]]), edit [/etc/pam.d/login] accordingly. The user will need to specify the **force_run** parameter.

[FILE] **`/etc/pam.d/greetd`Config lines for KWallet PAM unlocking via Greetd**

    -auth           optional        pam_kwallet5.so
    -session        optional        pam_kwallet5.so auto_start force_run

** Note**\
For LightDM, [/etc/pam.d/lightdm] needs to be edited instead.

** Note**\
If the filesystem containing a user\'s KWallet files is mounted by [pam_mount](https://wiki.gentoo.org/wiki/Pam_mount "Pam mount") upon logging on, it may be required to copy [\~/.local/share/kwalletd/kdewallet.salt] to the same path on the root filesystem. Otherwise, PAM attempts to unlock KWallet before the home directory is available and fails. The file [\~/.local/share/kwalletd/kdewallet.kwl] which actually contains the encrypted KWallet passwords does not need to be copied.

#### [Disabling KWallet]

To disable the KWallet subsystem completely, edit the following file:

[FILE] **`~/.config/kwalletrc`**

    [Wallet]
    Enabled=false

### [][SSH/GPG Agent startup/shutdown scripts]

ssh-agent scripts are located in [/etc/xdg/plasma-workspace/env] and [/etc/xdg/plasma-workspace/shutdown]. Shutdown scripts require executable bit set because they are not sourced. The [Keychain](https://wiki.gentoo.org/wiki/Keychain "Keychain") article provides more information about this.

### [Non-root user authentication for dialogs]

Some KDE dialogs such as printers, adding wireless networks and adding users require administrator authentication. This is handled through [[[sys-auth/polkit]](https://packages.gentoo.org/packages/sys-auth/polkit)[]] and operates independently from [[[app-admin/sudo]](https://packages.gentoo.org/packages/app-admin/sudo)[]]. By default in Gentoo, the root account is the only administrator, and so even if a user account can run root commands through [sudo], authentication in these KDE dialogs will fail.

Adding wireless networks using [[[net-misc/networkmanager]](https://packages.gentoo.org/packages/net-misc/networkmanager)[]] is allowed by a polkit rule which is part of the Gentoo package and already allows access for every user in the group `plugdev`. For other dialogs the behavior must be configured manually: If all users of the group `wheel` are required to be administrators, create a copy of [/usr/share/polkit-1/rules.d/50-default.rules] starting with a number lower than 50, and edit the line [return \[\"unix-user:0\"\]] to the following:

[FILE] **`/etc/polkit-1/rules.d/49-wheel.rules`Administrator wheel group**

    polkit.addAdminRule(function(action, subject) );

The [Polkit](https://wiki.gentoo.org/wiki/Polkit "Polkit") wiki page provides more details on rules configuration.

### [Run GUI applications with root privileges]

** Warning**\
It could be a *very* bad idea to start GUI applications with root privileges, versus adding the regular user to the relevant group or simply just running the command unprivileged. Only use [kdesu] when absolutely necessary.

KDE Plasma has a utility to start graphical programs with root privileges. It is provided by [[[kde-plasma/kdesu-gui]](https://packages.gentoo.org/packages/kde-plasma/kdesu-gui)[]] and is already pulled in by [[[kde-plasma/plasma-meta]](https://packages.gentoo.org/packages/kde-plasma/plasma-meta)[]]. It requires [Xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg"), and only works within X^[\[1\]](#cite_note-1)^.

`root `[`#`]`emerge --ask kde-plasma/kdesu-gui`

It can be used by invoking [kdesu] either from KRunner or a terminal emulator:

`user `[`$`]`kdesu `

A message dialog will be displayed prompting for the root password.

** Note**\
Some applications such as kwrite, dolphin etc. refuse to be opened with [kdesu] for security reasons.

** Note**\
By default, kdesu internally uses [su], which may not be preferred for some use cases. It is possible to use [sudo] or other sudo-compatible commands, by changing [kdesurc]:

[FILE] **`$XDG_CONFIG_HOME/kdesurc`Use sudo instead of su in kdesu**

    [super-user-command]
    super-user-command=sudo

### [Files]

XDG standard directories are being used for KDE Plasma and KDE applications:

-   [\$XDG_CONFIG_HOME] (defaults to [\$HOME/.config]) - Configuration files
-   [\$XDG_DATA_HOME] (defaults to [\$HOME/.local/share]) - Application data

### [Removal]

The first step to remove KDE Plasma and its dependencies is to unmerge [[[kde-plasma/plasma-meta]](https://packages.gentoo.org/packages/kde-plasma/plasma-meta)[]]. This will not yet remove any files from the installation, so the desktop environment will keep running:

`root `[`#`]`emerge --ask --depclean --verbose kde-plasma/plasma-meta`

In a next step it can be useful to scan [/etc/portage] directory for any KDE Plasma specific entries in [package.mask], [package.unmask] and [package.accept_keywords] and clean them up.

Finally, run the command to uninstall any Plasma packages and their dependencies. It would make sense to quit any running Plasma session beforehand:

`root `[`#`]`emerge --ask --depclean  `

** Warning**\
Please note that this will not just remove KDE Plasma but also any other package not registered (or being depended on) in \@world. Carefully read through the list of packages to be removed before continuing. Alternatively, run this command prior to unmerging of kde-plasma/plasma-meta to get an overview of already dangling packages on the system.

## [Applications]

KDE Gear consists of various applications and supporting libraries based on Qt/KDE Frameworks.

### [Available versions]

  ------------------------------ -------------------------------------- ----------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  KDE                            Gentoo                                 Ebuild repository                                                                   Status
  KDE Gear 25.12.3               kde-apps/kde-apps-meta-25.12.3         gentoo                                                                              Stable for **[amd64]** and **[arm64]**; testing for **[x86]**
  KDE Gear 26.04.1               kde-apps/kde-apps-meta-26.04.1         gentoo                                                                              Testing for **[amd64]**, **[arm64]** and **[x86]**
  KDE Gear 26.04 stable branch   kde-apps/kde-apps-meta-26.04.49.9999   [KDE](https://wiki.gentoo.org/wiki/KDE/Ebuild_repository "KDE/Ebuild repository")   Live version
  KDE Gear master branch         kde-apps/kde-apps-meta-9999            [KDE](https://wiki.gentoo.org/wiki/KDE/Ebuild_repository "KDE/Ebuild repository")   Live version
  ------------------------------ -------------------------------------- ----------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

KDE Gear is divided in the following meta packages:

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------
  Package name                                                                                                                                                                                                                                                                                                                                                                                                       Description
  [[[kde-apps/kdeaccessibility-meta]](https://packages.gentoo.org/packages/kde-apps/kdeaccessibility-meta)[]]   Accessibility applications and utilities.
  [[[kde-apps/kdeadmin-meta]](https://packages.gentoo.org/packages/kde-apps/kdeadmin-meta)[]]                           Administrative utilities, which help in managing the system.
  [[[kde-apps/kdecore-meta]](https://packages.gentoo.org/packages/kde-apps/kdecore-meta)[]]                              Basic applications such as file browser, editor, terminal emulator.
  [[[kde-apps/kdeedu-meta]](https://packages.gentoo.org/packages/kde-apps/kdeedu-meta)[]]                                 Educational applications and games.
  [[[kde-apps/kdegames-meta]](https://packages.gentoo.org/packages/kde-apps/kdegames-meta)[]]                           Standard desktop games.
  [[[kde-apps/kdegraphics-meta]](https://packages.gentoo.org/packages/kde-apps/kdegraphics-meta)[]]                  Graphics applications such as image viewers, color pickers, etc.
  [[[kde-apps/kdemultimedia-meta]](https://packages.gentoo.org/packages/kde-apps/kdemultimedia-meta)[]]            Audio and video playback applications and services.
  [[[kde-apps/kdenetwork-meta]](https://packages.gentoo.org/packages/kde-apps/kdenetwork-meta)[]]                     Network applications and VNC services.
  [[[kde-apps/kdepim-meta]](https://packages.gentoo.org/packages/kde-apps/kdepim-meta)[]]                                 PIM applications such as emailer, addressbook, organizer, etc.
  [[[kde-apps/kdesdk-meta]](https://packages.gentoo.org/packages/kde-apps/kdesdk-meta)[]]                                 Various development tools.
  [[[kde-apps/kdeutils-meta]](https://packages.gentoo.org/packages/kde-apps/kdeutils-meta)[]]                           Standard desktop utilities such as an archiver, a calculator, etc.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------

### [Installation]

The [[[kde-apps/kde-apps-meta]](https://packages.gentoo.org/packages/kde-apps/kde-apps-meta)[]] package provides the full KDE Gear bundle:

`root `[`#`]`emerge --ask kde-apps/kde-apps-meta`

If not all the packages are required, one or several smaller meta packages from the list above may be picked instead. Alternatively, it is possible to set [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag") to reduce the number of applications installed by [[[kde-apps/kde-apps-meta]](https://packages.gentoo.org/packages/kde-apps/kde-apps-meta)[]].

### [Localization]

Plasma and Applications are shipping their [localization](https://wiki.gentoo.org/wiki/Localization "Localization") per-package. Enable desired localization in System Settings.

### [KDE PIM]

KDE PIM is a whole suite of applications to manage personal information including mail, calendar, contacts and more. It has several optional runtime dependencies to extend its functionality:

-   Virus detection: [[[app-antivirus/clamav]](https://packages.gentoo.org/packages/app-antivirus/clamav)[]]
-   Spam filtering: [[[mail-filter/bogofilter]](https://packages.gentoo.org/packages/mail-filter/bogofilter)[]] or [[[mail-filter/spamassassin]](https://packages.gentoo.org/packages/mail-filter/spamassassin)[]]

## [Frameworks]

KDE Frameworks is a collection of libraries and software frameworks that provide the foundation for KDE Plasma and KDE Gear (applications), but may be leveraged by any Qt application.

As Frameworks are mostly libraries and provide little user functionality, it\'s not necessary to install them manually - the required packages will be pulled in automatically as dependencies.

### [Available versions]

  ---------------------------------- -------------------------- ----------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  KDE                                Gentoo                     Ebuild repository                                                                   Status
  KDE Frameworks 6.25.0              kde-frameworks/\*-6.25.0   gentoo                                                                              Stable for **[amd64]**, **[arm64]** and **[ppc64]**; testing for **[loong]**, **[riscv]** and **[x86]**
  KDE Frameworks 6.26.0              kde-frameworks/\*-6.26.0   gentoo                                                                              Testing for **[amd64]**, **[arm64]**, **[loong]**, **[ppc64]**, **[riscv]** and **[x86]**
  KDE Frameworks 6 (master) branch   kde-frameworks/\*-9999     [KDE](https://wiki.gentoo.org/wiki/KDE/Ebuild_repository "KDE/Ebuild repository")   Live version
  ---------------------------------- -------------------------- ----------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [More KDE software]

The most important KDE applications are in the Gentoo ebuild repository and many are located in the [kde-apps](https://packages.gentoo.org/category/kde-apps) and [kde-misc](https://packages.gentoo.org/category/kde-misc) categories.

## [Troubleshooting]

Refer to the [Troubleshooting](https://wiki.gentoo.org/wiki/KDE/Troubleshooting "KDE/Troubleshooting") sub-article.

## [See also]

-   [KDE/Ebuild repository](https://wiki.gentoo.org/wiki/KDE/Ebuild_repository "KDE/Ebuild repository") --- provides instructions on adding Gentoo\'s KDE ebuild development repository to a system.
-   [kde-sunset ebuild repository](https://wiki.gentoo.org/wiki/Overlay:Kde-sunset "Overlay:Kde-sunset") - For old KDE software that has been removed from the main ebuild repository.
-   [Desktop environment](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") --- provides a list of desktop environments available in Gentoo.

## [External links]

-   [Official KDE user wiki](https://userbase.kde.org/)
-   [Official KDE forum](https://forum.kde.org/)
-   [KDE Store (themes, widgets, wallpapers, etc.)](https://store.kde.org/)

## [References]

1.  [[[↑](#cite_ref-1)] [[https://bugs.kde.org/show_bug.cgi?id=427912](https://bugs.kde.org/show_bug.cgi?id=427912)]]