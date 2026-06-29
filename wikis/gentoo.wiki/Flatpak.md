**Resources**

[[]][Home](https://flatpak.org/)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/flatpak)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Flatpak "wikipedia:Flatpak")

[[]][Official documentation](https://docs.flatpak.org/en/latest/)

[[]][[#flatpak](ircs://irc.libera.chat/#flatpak)] ([[webchat](https://web.libera.chat/#flatpak)])

[[]][GitWeb](https://github.com/flatpak/flatpak.git)

**Flatpak** is a package management framework aiming to provide support for sandboxed, distro-agnostic binary packages for Linux desktop applications. Just as [chroot](https://wiki.gentoo.org/wiki/Chroot "Chroot"), [Docker](https://wiki.gentoo.org/wiki/Docker "Docker"), and [LXD](https://wiki.gentoo.org/wiki/LXD "LXD") provide a means to isolate primarily *server-based* applications from the underlying operating system, Flatpak provides a mechanism to isolate primarily *desktop-based* applications from the underlying operating system. When combined with features like [systemd-homed](https://wiki.gentoo.org/wiki/Systemd-homed "Systemd-homed"), it becomes possible to contain a user and all of that user\'s applications within a single directory, the user\'s `$HOME`, in a manner that is portable across systems of the same CPU architecture.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
    -   [[1.4] [Add flathub repository]](#Add_flathub_repository)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Permissions]](#Permissions)
-   [[3] [Basic usage]](#Basic_usage)
-   [[4] [Theming]](#Theming)
    -   [[4.1] [GTK]](#GTK)
-   [[5] [Desktop integration for Wayland]](#Desktop_integration_for_Wayland)
    -   [[5.1] [Installation]](#Installation_2)
    -   [[5.2] [Ensuring portals are running]](#Ensuring_portals_are_running)
-   [[6] [Troubleshooting]](#Troubleshooting)
    -   [[6.1] [Installed applications\' desktop entries do not show in launchers]](#Installed_applications.27_desktop_entries_do_not_show_in_launchers)
    -   [[6.2] [After updating nvidia-drivers 3D applications crash or become slow]](#After_updating_nvidia-drivers_3D_applications_crash_or_become_slow)
    -   [[6.3] [Flatpaked GTK apps under Wayland and jagged fonts]](#Flatpaked_GTK_apps_under_Wayland_and_jagged_fonts)
    -   [[6.4] [Certain flatpak applications failing to access proper cursor]](#Certain_flatpak_applications_failing_to_access_proper_cursor)
    -   [[6.5] [File Chooser or similar Dialogues not opening]](#File_Chooser_or_similar_Dialogues_not_opening)
    -   [[6.6] [Searching for any package returns \"No matches found\"]](#Searching_for_any_package_returns_.22No_matches_found.22)
    -   [[6.7] [flatpak: /usr/lib64/libxmlb.so.2: no version information available (required by /usr/lib64/libappstream.so.5)]](#flatpak:_.2Fusr.2Flib64.2Flibxmlb.so.2:_no_version_information_available_.28required_by_.2Fusr.2Flib64.2Flibappstream.so.5.29)
    -   [[6.8] [ebuild selected to satisfy has unmet requirements.]](#ebuild_selected_to_satisfy_has_unmet_requirements.)
-   [[7] [See also]](#See_also)
-   [[8] [References]](#References)

## [Installation]

### [Kernel]

[KERNEL] **Required**

    File systems  --->
       [*] FUSE (Filesystem in Userspace) support Search for <code>CONFIG_FUSE_FS</code> to find this item.

[KERNEL] **Optional, recommended - Enable [Landlock](https://landlock.io/) sandbox (`CONFIG_SECURITY_LANDLOCK=y`)**

    Security options  --->
       [*] Landlock support Search for <code>CONFIG_SECURITY_LANDLOCK</code> to find this item.
       (landlock,yama) Ordered list of enabled LSMs Search for <code>CONFIG_LSM</code> to find this item.

** Note**\
Order is important. Here a [reference](https://origin.kernel.org/doc/html/latest/userspace-api/landlock.html): `landlock,lockdown,yama,integrity,apparmor`

** Note**\
Instead of adding `landlock` to the **Ordered list of enabled LSMs**, Landlock can also be loaded at boot time. For this, set `lsm=landlock,...` in the [Kernel Command-line parameters](https://wiki.gentoo.org/wiki/Kernel/Command-line_parameters "Kernel/Command-line parameters").

### [USE flags]

### [USE flags for] [sys-apps/flatpak](https://packages.gentoo.org/packages/sys-apps/flatpak) [[]] [Linux application sandboxing and distribution framework]

  ----------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`X`](https://packages.gentoo.org/useflags/X)                           Add support for X11
  [`doc`](https://packages.gentoo.org/useflags/doc)                       Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`introspection`](https://packages.gentoo.org/useflags/introspection)   Add support for GObject based introspection
  [`policykit`](https://packages.gentoo.org/useflags/policykit)           Enable PolicyKit (polkit) authentication support
  [`seccomp`](https://packages.gentoo.org/useflags/seccomp)               Enable seccomp (secure computing mode) to perform system call filtering at runtime to increase security of programs
  [`systemd`](https://packages.gentoo.org/useflags/systemd)               Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)                     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-21 16:16] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

Xorg session users will want X enabled.

### [Emerge]

** Note**\
Chromium-based browsers suggest disabling the `suid` USE flag for [[[sys-apps/bubblewrap]](https://packages.gentoo.org/packages/sys-apps/bubblewrap)[]] for performance reasons. Also there are technologies such as Valve Pressure Vessel (used in Steam) which requires it to work. Without `suid`, bubblewrap requires the kernel option `CONFIG_USER_NS=y` to be set.

** Important**\
Flatpak request users restart their system after installing [[[sys-apps/flatpak]](https://packages.gentoo.org/packages/sys-apps/flatpak)[]] before asking for support with issues.

`root `[`#`]`emerge --ask sys-apps/flatpak`

### [Add flathub repository]

** Tip**\
All operations with flatpak can be performed as user or as root, if performing as user \--user flag can help if there are issues with permissions.

`user `[`$`]`flatpak remote-add --user --if-not-exists flathub `[`https://flathub.org/repo/flathub.flatpakrepo`](https://flathub.org/repo/flathub.flatpakrepo)

## [Configuration]

### [Files]

-   [/var/lib/flatpak] --- global flatpak state (system-wide installed apps and repos)
-   [\$HOME/.local/share/flatpak] --- per-user flatpak state (locally installed apps and repos)
-   [\$HOME/.var/app/] --- per application state (configuration files and cache)

### [Permissions]

In some instances, it may be necessary to edit the sandbox permissions of a flatpak application. The most convenient way of doing this is via the GUI tool Flatseal.

`user `[`$`]`flatpak install com.github.tchx84.Flatseal`

## [Basic usage]

To install an application, e.g. Thunderbird, run:

`user `[`$`]`flatpak search Thunderbird`

Get the **Application ID**: *org.mozilla.Thunderbird* and install the application:

`user `[`$`]`flatpak --user install org.mozilla.Thunderbird`

To run the application, use created .desktop file or run:

`user `[`$`]`flatpak run org.mozilla.Thunderbird`

To update installed applications and runtimes:

`user `[`$`]`flatpak update`

To remove the application:

`user `[`$`]`flatpak uninstall org.mozilla.Thunderbird`

## [Theming]

Flatpak documentiation offers [a good guide](https://docs.flatpak.org/en/latest/desktop-integration.html) about desktop integration and theming.

### [GTK]

Flatpak applications don\'t follow the system\'s GTK theme by default. First find out what\'s the current GTK theme, e.g. Materia-dark-compact, and then install it for Flatpak applications to use. ^[\[1\]](#cite_note-1)^

`user `[`$`]`gsettings get org.gnome.desktop.interface gtk-theme`

`user `[`$`]`flatpak install flathub org.gtk.Gtk3theme.Materia-dark-compact`

## [Desktop integration for Wayland]

When using WMs such as [Sway](https://wiki.gentoo.org/wiki/Sway "Sway"), installing an [xdg-desktop-portal](https://wiki.gentoo.org/wiki/Xdg-desktop-portal "Xdg-desktop-portal") implementation is needed for full integration. Available implementations include:

-   [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME") backend: [[[sys-apps/xdg-desktop-portal-gnome]](https://packages.gentoo.org/packages/sys-apps/xdg-desktop-portal-gnome)[]]
-   [GTK](https://wiki.gentoo.org/wiki/GTK "GTK") backend: [[[sys-apps/xdg-desktop-portal-gtk]](https://packages.gentoo.org/packages/sys-apps/xdg-desktop-portal-gtk)[]]
-   [KDE](https://wiki.gentoo.org/wiki/KDE "KDE") backend: [[[kde-plasma/xdg-desktop-portal-kde]](https://packages.gentoo.org/packages/kde-plasma/xdg-desktop-portal-kde)[]] (in development)
-   [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland")/wlroots backend: [[[gui-libs/xdg-desktop-portal-wlr]](https://packages.gentoo.org/packages/gui-libs/xdg-desktop-portal-wlr)[]] (in development)
-   [LXQt](https://wiki.gentoo.org/wiki/LXQt "LXQt") backend [[[gui-libs/xdg-desktop-portal-lxqt]](https://packages.gentoo.org/packages/gui-libs/xdg-desktop-portal-lxqt)[]] (in development)
-   Flatpak backend: \'flatpak-portal\' (included in the [[[sys-apps/flatpak]](https://packages.gentoo.org/packages/sys-apps/flatpak)[]] package)

Please note that these are separate entities that do not substitute each other and some of them may not be run at the same time as some of the others.

### [Installation]

First, emerge [[[sys-apps/xdg-desktop-portal]](https://packages.gentoo.org/packages/sys-apps/xdg-desktop-portal)[]]:

`root `[`#`]`emerge --ask sys-apps/xdg-desktop-portal`

Then emerge any needed backends:

`root `[`#`]`emerge --ask sys-apps/xdg-desktop-portal-gtk gui-libs/xdg-desktop-portal-wlr gui-libs/xdg-desktop-portal-lxqt sys-apps/xdg-desktop-portal-gnome`

** Note**\
Desktop environment backends such as `xdg-desktop-portal-gnome` or `xdg-desktop-portal-lxqt` may be installed by default depending on how the desktop environment was installed

### [Ensuring portals are running]

Please note that sometimes these libraries aren\'t pulled automatically by the OS and need to be run by the user, for example they can be pulled in [Sway](https://wiki.gentoo.org/wiki/Sway "Sway") configuration:

[FILE] **`~/.config/sway/config`Running xdg portals**

    exec /usr/libexec/xdg-desktop-portal-gtk -r
    exec /usr/libexec/xdg-desktop-portal-wlr -r
    exec /usr/libexec/flatpak-portal -r
    exec "sh -c 'sleep 5;exec /usr/libexec/xdg-desktop-portal -r'"

## [Troubleshooting]

### [][Installed applications\' desktop entries do not show in launchers]

It is important to reboot the system after first installing Flatpak. Otherwise, installed applications\' desktop entries may not show in launchers.

### [After updating nvidia-drivers 3D applications crash or become slow]

Make sure to update the flatpak nvidia platform.

`user `[`$`]`flatpak update`

### [Flatpaked GTK apps under Wayland and jagged fonts]

Some users [report jagged fonts](https://github.com/flatpak/flatpak/issues/2861) on Wayland. This happens because if GTK apps can\'t detect whether they should perform font antialiasing, they disable ones by default. It obtain info ether from the system or via `xdg-desktop-portal-gtk` if flatpaked. It also requires setting up the proper wayland scheme for it from `gnome-base/gsettings-desktop-schemas`, but that package already in list of flatpak dependencies.

So a workaround is to install `xdg-desktop-portal-gtk` and reboot/restart the desktop:

`root `[`#`]`emerge --ask sys-apps/xdg-desktop-portal-gtk`

To make sure if it is launched, see **\"Ensuring portals are running\"** topic above.

Since in early 2022 GTK wayland schemas are moved from `gnome-base/gnome-settings-daemon` to `gnome-base/gsettings-desktop-schemas`, the gnome settings daemon is no more required and can be uninstalled.

### [Certain flatpak applications failing to access proper cursor]

Some flatpaks such as `com.discordapp.Discord` or `com.spotify.Client` have an issue where they cannot find the systems cursor, and so default to the ugly default cursor that is used when no proper replacement is found.

A solution to this is to copy the systems icon directory to a location in the users home directory. In this example `~/.local/share/icons` will be used:

** Note**\
`/usr/share/icons` is one of the several directories icons can be used from. You could also use `/usr/share/cursors`

`user `[`$`]`cp -r /usr/share/icons ~/.local/share/`

Next, use `flatpak-override` to give the flatpak in question (com.discordapp.Discord in this example) access to the home directory in which the cursors are inside:

`root `[`#`]`flatpak override --filesystem=home com.discordapp.Discord`

To remove the filesystem override, run:

`user `[`$`]`flatpak override --nofilesystem=home com.discordapp.Discord`

After the filesystem override is set, the `XCURSOR_PATH` and `XCURSOR_THEME` variables must be set, where `XCURSOR_PATH` is the path to the theme and `XCURSOR_PATH` is the name of the theme like so:

`user `[`$`]`flatpak override --env=XCURSOR_PATH=/home/$USER/.local/share/icons com.discordapp.Discord`

`user `[`$`]`flatpak override --env=XCURSOR_THEME=Adwaita-dark com.discordapp.Discord`

Finally, run the flatpak to see the applied changes:

`user `[`$`]`flatpak run com.discordapp.Discord`

### [File Chooser or similar Dialogues not opening]

File Chooser, App Chooser, Email, Print, or Notification dialogues (and more) are provided by an XDG Desktop Portal, as per [Desktop Integration for Wayland](https://wiki.gentoo.org/wiki/Flatpak#Desktop_integration_for_Wayland "Flatpak"). Check also whether your `XDG_CURRENT_DESKTOP` environment variable corresponds to the `UseIn` attribute for your XDG Desktop Portal. Flatpak\'s logic for this has been changed[\[1\]](https://github.com/flatpak/flatpak/commit/8ca4addc7352df428ee1888632f63083ba862dc2) to mimic that of *xdg-desktop-portal* more closely and thus **requires** the environment variable to be set, otherwise matching interfaces will be ignored even if there is only one implementation.

For instance *xdg-desktop-portal-gtk* has its `UseIn` defined in `/usr/share/xdg-desktop-portal/portals/gtk.portal` as `UseIn=gnome`. Therefore your `XDG_CURRENT_DESKTOP` environment variable should be set to `gnome` if not automatically done so by your desktop environment (users without DE may need to set this in `~/.xinitrc` or another appropriate location) for the GTK portal to be used as a file chooser (and similar).

\

### [][Searching for any package returns \"No matches found\"]

See \"Add flathub repository\" section of this documentation

### [][flatpak: /usr/lib64/libxmlb.so.2: no version information available (required by /usr/lib64/libappstream.so.5)]

Issue:

`root `[`#`]`emerge --oneshot dev-libs/libxmlb dev-libs/appstream`

### [ebuild selected to satisfy has unmet requirements.]

This is caused by setting [[[dracut]](https://packages.gentoo.org/useflags/dracut)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] as a global USE flag rather than in [/etc/portage/package.use] for [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]].

Fix by removing [[[dracut]](https://packages.gentoo.org/useflags/dracut)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] from [/etc/portage/make.conf] and following [Handbook:AMD64/Installation/Kernel#Initramfs](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Kernel#Initramfs "Handbook:AMD64/Installation/Kernel")

## [See also]

-   [Docker](https://wiki.gentoo.org/wiki/Docker "Docker") --- a [container](https://en.wikipedia.org/wiki/Container_(virtualization) "wikipedia:Container (virtualization)")-based [virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") system
-   [LXD](https://wiki.gentoo.org/wiki/LXD "LXD") --- a system container manager
-   [systemd/systemd-nspawn](https://wiki.gentoo.org/wiki/Systemd/systemd-nspawn "Systemd/systemd-nspawn") --- a lightweight, loosely [chroot](https://wiki.gentoo.org/wiki/Chroot "Chroot")-like, OS-level [OCI container](https://opencontainers.org/) environment native to [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd").

## [References]

1.  [[[↑](#cite_ref-1)] [[https://www.linuxuprising.com/2018/05/how-to-get-flatpak-apps-to-use-correct.html](https://www.linuxuprising.com/2018/05/how-to-get-flatpak-apps-to-use-correct.html)]]