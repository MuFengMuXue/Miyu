[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Dhcpcd-ui&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://roy.marples.name/projects/dhcpcd-ui)

[[]][Package information](https://packages.gentoo.org/packages/net-misc/dhcpcd-ui)

[[]][GitHub](https://github.com/rsmarples/dhcpcd-ui)

**dhcpcd-ui** is a Qt and GTK monitor and configuration graphical user interface for [dhcpcd](https://wiki.gentoo.org/wiki/Dhcpcd "Dhcpcd").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Building from source]](#Building_from_source)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Removal]](#Removal)
-   [[4] [External resources]](#External_resources)
-   [[5] [References]](#References)

## [Installation]

### [USE flags]

To get one of the graphical user interfaces enable the respective USE flag.

### [USE flags for] [net-misc/dhcpcd-ui](https://packages.gentoo.org/packages/net-misc/dhcpcd-ui) [[]] [Desktop notification and configuration for dhcpcd]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)             Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`gtk`](https://packages.gentoo.org/useflags/gtk)                 Add support for x11-libs/gtk+ (The GIMP Toolkit)
  [`libnotify`](https://packages.gentoo.org/useflags/libnotify)     Enable desktop notification support
  [`ncurses`](https://packages.gentoo.org/useflags/ncurses)         Add ncurses support (console display library)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-18 22:39] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

Support for `qt4` has been removed with commit [43f5c510450633d249f596fcc4f74255df76bb73](https://gitweb.gentoo.org/repo/gentoo.git/commit/net-misc/dhcpcd-ui?id=43f5c510450633d249f596fcc4f74255df76bb73) [[[bug #630638]](https://bugs.gentoo.org/show_bug.cgi?id=630638)[]].

### [Emerge]

Install dhcpcd-ui:

`root `[`#`]`emerge --ask net-misc/dhcpcd-ui`

### [Building from source]

Alternatively, for installing the bleeding edge^[\[1\]](#cite_note-1)^ of dhcpcd-ui you can use the live ebuild from the bar overlay^[\[2\]](#cite_note-2)^.

`root `[`#`]`emerge --ask --noreplace app-eselect/eselect-repository dev-vcs/git `

`root `[`#`]`eselect repository enable bar `

`root `[`#`]`emerge --sync bar `

`root `[`#`]`emerge --ask =net-misc/dhcpcd-ui-9999:bar `

`root `[`#`]`emerge --ask --deselect net-misc/dhcpcd `

## [Configuration]

Uncomment the `controlgroup` line in [/etc/dhcpcd.conf]:

[FILE] **`/etc/dhcpcd.conf`**

    # Allow users of this group to interact with dhcpcd via the control socket.
    controlgroup wheel

Change group and permissions of [/etc/dhcpcd.conf] in order to make it writable for the user interface:

`root `[`#`]`chgrp wheel /etc/dhcpcd.conf `

`root `[`#`]`chmod g+w /etc/dhcpcd.conf `

\

## [Removal]

Uninstall dhcpcd-ui:

`root `[`#`]`emerge --ask --depclean --verbose net-misc/dhcpcd-ui`

## [External resources]

-   [Forum thread](http://forums.gentoo.org/viewtopic-p-7617702.html)

## [References]

1.  [[[↑](#cite_ref-1)] [[http://roy.marples.name/projects/dhcpcd-ui/timeline](http://roy.marples.name/projects/dhcpcd-ui/timeline)]]
2.  [[[↑](#cite_ref-2)] [[https://github.com/tokiclover/bar-overlay/tree/master/net-misc](https://github.com/tokiclover/bar-overlay/tree/master/net-misc)]]