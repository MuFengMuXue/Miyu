[[]][Home](https://github.com/linuxmint/nemo)

[[]][Package information](https://packages.gentoo.org/packages/gnome-extra/nemo)

**Nemo** is a fork of [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME")\'s [Nautilus](https://wiki.gentoo.org/index.php?title=Nautilus&action=edit&redlink=1 "Nautilus (page does not exist)") file manager for [Cinnamon](https://wiki.gentoo.org/wiki/Cinnamon "Cinnamon"). Like the rest of Cinnamon\'s forks of GNOME software it preserved the more traditional GUI style while being actively developed to keep up with modern features.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [gnome-extra/nemo](https://packages.gentoo.org/packages/gnome-extra/nemo) [[]] [A file manager for Cinnamon, forked from Nautilus]

  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+nls`](https://packages.gentoo.org/useflags/+nls)         Add Native Language Support (using gettext - GNU locale utilities)
  [`exif`](https://packages.gentoo.org/useflags/exif)         Add support for reading EXIF headers from JPEG and TIFF images
  [`gtk-doc`](https://packages.gentoo.org/useflags/gtk-doc)   Build and install gtk-doc based developer documentation for dev-util/devhelp, IDE and offline use
  [`selinux`](https://packages.gentoo.org/useflags/selinux)   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`test`](https://packages.gentoo.org/useflags/test)         Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`tracker`](https://packages.gentoo.org/useflags/tracker)   Add support for app-misc/tinysparql search
  [`wayland`](https://packages.gentoo.org/useflags/wayland)   Enable dev-libs/wayland backend
  [`xmp`](https://packages.gentoo.org/useflags/xmp)           Enable support for Extensible Metadata Platform (Adobe XMP)
  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-05 17:49] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

**Nemo** can be easily installed via [emerge]:

`root `[`#`]`emerge --ask gnome-extra/nemo`

## [See also]

-   [File managers](https://wiki.gentoo.org/wiki/File_managers "File managers") --- a computer program that allows for the manipulation of files and directories on a computer\'s [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem").