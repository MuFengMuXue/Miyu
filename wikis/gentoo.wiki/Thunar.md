[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Thunar&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://docs.xfce.org/xfce/thunar/start)

[[]][GitHub](https://github.com/Xfce)

[[]][GitLab](https://gitlab.com/xfce)

[[]][Package information](https://packages.gentoo.org/packages/xfce-base/thunar)

**Thunar** is a modern file manager for the [Xfce](https://wiki.gentoo.org/wiki/Xfce "Xfce") Desktop Environment. Thunar has been designed from the ground up to be fast and easy to use. Its user interface is clean and intuitive and does not include any confusing or useless options by default. Thunar starts up quickly and navigating through files and folders is fast and responsive. It is written in GTK+ 3.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Additional software]](#Additional_software)
        -   [[1.3.1] [GVfs]](#GVfs)
        -   [[1.3.2] [thunar-volman]](#thunar-volman)
        -   [[1.3.3] [thunar-archive-plugin]](#thunar-archive-plugin)
        -   [[1.3.4] [thunar-media-tags-plugin]](#thunar-media-tags-plugin)
        -   [[1.3.5] [thunar-shares-plugin]](#thunar-shares-plugin)
        -   [[1.3.6] [thunar-vcs-plugin]](#thunar-vcs-plugin)
    -   [[1.4] [Thumbnails]](#Thumbnails)
        -   [[1.4.1] [Tumbler]](#Tumbler)
        -   [[1.4.2] [raw-thumbnailer]](#raw-thumbnailer)
        -   [[1.4.3] [ffmpegthumbnailer]](#ffmpegthumbnailer)
-   [[2] [Troubleshooting]](#Troubleshooting)
    -   [[2.1] [Thunar takes a long time to start]](#Thunar_takes_a_long_time_to_start)
    -   [[2.2] [Missing dependency GVfs]](#Missing_dependency_GVfs)
    -   [[2.3] [Unable to mount drives]](#Unable_to_mount_drives)
-   [[3] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [xfce-base/thunar](https://packages.gentoo.org/packages/xfce-base/thunar) [[]] [File manager for the Xfce desktop environment]

  ----------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------
  [`+trash-panel-plugin`](https://packages.gentoo.org/useflags/+trash-panel-plugin)   Build the trash status indicator plugin for the XFCE panel
  [`X`](https://packages.gentoo.org/useflags/X)                                       Add support for X11
  [`exif`](https://packages.gentoo.org/useflags/exif)                                 Add support for reading EXIF headers from JPEG and TIFF images
  [`gtk-doc`](https://packages.gentoo.org/useflags/gtk-doc)                           Build and install gtk-doc based developer documentation for dev-util/devhelp, IDE and offline use
  [`introspection`](https://packages.gentoo.org/useflags/introspection)               Add support for GObject based introspection
  [`libnotify`](https://packages.gentoo.org/useflags/libnotify)                       Enable desktop notification support
  [`pcre`](https://packages.gentoo.org/useflags/pcre)                                 Add support for Perl Compatible Regular Expressions
  [`policykit`](https://packages.gentoo.org/useflags/policykit)                       Enable PolicyKit (polkit) authentication support
  [`terminal`](https://packages.gentoo.org/useflags/terminal)                         Enable integrated terminal support
  [`udisks`](https://packages.gentoo.org/useflags/udisks)                             Enable storage management support (automounting, volume monitoring, etc)
  ----------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-10 15:24] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Emerge Thunar:

`root `[`#`]`emerge --ask xfce-base/thunar`

### [Additional software]

#### [GVfs]

[GVfs](https://wiki.gentoo.org/wiki/Gvfs "Gvfs") comes with a set of backends, including trash support, SFTP, SMB, HTTP, DAV, and many others.

Thunar will interact with gvfs via udisks when the **udisks** `USE` is enabled.

In the location dialog (opened with Ctrl+L) type one of the following: smb://, ftp://, ssh://, sftp://, davs:// followed by the server hostname or IP address.

Although GVfs comes from gnome-base/gvfs, it is well suited for any non-gnome or XFCE desktop as well.

#### [thunar-volman]

`root `[`#`]`emerge --ask xfce-base/thunar-volman`

Automatic management of removable devices in Thunar.

To let Thunar handle automatic mounting, one must launch thunar in daemon mode.

Make sure the command [thunar \--daemon] is autostarted on login.

#### [thunar-archive-plugin]

`root `[`#`]`emerge --ask xfce-extra/thunar-archive-plugin`

Archive plugin supports extracting .zip and .tar.gz files from context menus (or any other typical archive supported)

#### [thunar-media-tags-plugin]

`root `[`#`]`emerge --ask xfce-extra/thunar-media-tags-plugin`

Media tags plugin - special features for media files , **media tags**, etc

#### [thunar-shares-plugin]

`root `[`#`]`emerge --ask xfce-extra/thunar-shares-plugin`

Shares plugin - share files using **SAMBA**

#### [thunar-vcs-plugin]

`root `[`#`]`emerge --ask xfce-extra/thunar-vcs-plugin`

Version Control System plugin - adds subversion and **GIT** actions to the context menu

### [Thumbnails]

By default, thumbnails *ARE* shown by thunar - but only when they have been pre-generated by another tool. Thunar can not auto-generate its own thumbnails, [on its own.]

The thumbnailer / thumbnail server / daemon for XFCE is named **xfce-base/tumbler**, see the section just below.

There are also alternatives, some image viewers like **media-gfx/eom** will create one thumbnail when each image is opened in it.

Speciality programs for specific file types are also available.

The thumbnails are tiny copies that get stored forever in the **\~/.cache/thumbnails** dir, named by hashes according to the thumbnail spec.

#### [Tumbler]

Tumbler is an external program from the XFCE ecosystem to generate thumbnails. It requires **dbus**.

By default, **jpeg** *USE* is on, and the **ffmpeg** *USE* flag will install **media-video/ffmpegthumbnailer**.

By default, the **gstreamer** *USE* flag hooks into system gstreamer & gst-plugins for a wide range of audio/video formats.

Other possible *USE* flags: **curl**, **epub**, **odf**, **pdf**, **raw**.

`root `[`#`]`emerge --ask xfce-base/tumbler`

#### [raw-thumbnailer]

A lightweight and fast raw image thumbnailer that can be used to display raw images, using **media-libs/libopenraw**.

`root `[`#`]`emerge --ask media-gfx/raw-thumbnailer`

#### [ffmpegthumbnailer]

A lightweight video thumbnailer that can be used either by Tumbler, other file managers, or manually, using **media-video/ffmpeg**.

`root `[`#`]`emerge --ask media-video/ffmpegthumbnailer`

## [Troubleshooting]

### [Thunar takes a long time to start]

In some cases it has been reported that Thunar would take a long time to start for the first time. This is caused by gvfs checking the network and preventing Thunar to start until the operation finishes. If this is an issue, it may be possible to edit [/usr/share/gvfs/mounts/network.mount] and change `AutoMount=true` to `AutoMount=false`.

### [Missing dependency GVfs]

If the trashcan and external drives do not show up in Thunar, but GVfs is installed and the appropriate USE flags are enabled, it is likely that there is no dbus session running.

Please refer to [D-Bus](https://wiki.gentoo.org/wiki/D-Bus#The_session_bus "D-Bus") for instructions.

### [Unable to mount drives]

When using a window wanager, polkit, which is required to mount drives in Thunar, may not be launched automatically. Multiple graphical polkit applications exist, like [[[gnome-extra/polkit-gnome]](https://packages.gentoo.org/packages/gnome-extra/polkit-gnome)[]] or [[[mate-extra/mate-polkit]](https://packages.gentoo.org/packages/mate-extra/mate-polkit)[]]. The following example will use the former.

First, emerge [[[gnome-extra/polkit-gnome]](https://packages.gentoo.org/packages/gnome-extra/polkit-gnome)[]]:

`root `[`#`]`emerge --ask gnome-extra/polkit-gnome`

Make polkit be launched automatically by the window manager via editing its configuration file. For example, in Sway:

[FILE] **`~/.config/sway/config`**

    exec /usr/libexec/polkit-gnome-authentication-agent-1

Exit the window manager and log out to apply these changes.

## [See also]

-   [Xfce/Guide](https://wiki.gentoo.org/wiki/Xfce/Guide "Xfce/Guide") --- provides an extensive introduction to Xfce, a fast, lightweight, full-featured desktop environment.
-   [Dolphin](https://wiki.gentoo.org/wiki/Dolphin "Dolphin") --- [KDE](https://wiki.gentoo.org/wiki/KDE "KDE")\'s file manager that allows navigating and browsing the contents of hard drives, USB sticks, SD cards, and more. Creating, moving, or deleting files and folders is simple and fast.
-   [File managers](https://wiki.gentoo.org/wiki/File_managers "File managers") --- a computer program that allows for the manipulation of files and directories on a computer\'s [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem").
-   [PCManFM](https://wiki.gentoo.org/wiki/PCManFM "PCManFM") --- a powerful yet lightweight file manager application, default file manager of [LXDE](https://wiki.gentoo.org/wiki/LXDE "LXDE").
-   [Recommended applications](https://wiki.gentoo.org/wiki/Recommended_applications "Recommended applications") --- applications recommended for use in a graphical environment ([X11](https://wiki.gentoo.org/wiki/Xorg "Xorg"), [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland"))