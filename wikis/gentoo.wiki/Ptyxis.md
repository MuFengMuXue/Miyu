[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Ptyxis&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://devsuite.app/)

[[]][GitHub](https://github.com/yonasBSD/ptyxis-terminal)

[[]][Package information](https://packages.gentoo.org/packages/x11-terms/ptyxis)

**Ptyxis** is a terminal emulator for a container-oriented desktop.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Troubleshooting]](#Troubleshooting)
    -   [[2.1] [Notifications Do not Work]](#Notifications_Do_not_Work)
    -   [[2.2] [Terminal Transparency]](#Terminal_Transparency)
    -   [[2.3] [Open Terminal Here Not Working with Dolphin]](#Open_Terminal_Here_Not_Working_with_Dolphin)
-   [[3] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [x11-terms/ptyxis](https://packages.gentoo.org/packages/x11-terms/ptyxis) [[]] [A terminal for a container-oriented desktop]

  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`X`](https://packages.gentoo.org/useflags/X)         Add support for X11
  [`test`](https://packages.gentoo.org/useflags/test)   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-30 21:32] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask x11-terms/ptyxis`

## [Troubleshooting]

### [Notifications Do not Work]

See the troubleshooting section of the [GitHub repository](https://github.com/yonasBSD/ptyxis-terminal?tab=readme-ov-file#troubleshooting-issues).

### [Terminal Transparency]

See discussion on [Fedora forums](https://discussion.fedoraproject.org/t/use-dconf-to-set-transparency-for-ptyxis/135003).

### [Open Terminal Here Not Working with Dolphin]

Depending on the Ptyxis version, the \"Open Terminal Here\" option in Dolphin may not function properly when Ptyxis is the default terminal. It appears that more recent versions of Ptyxis may have a simple workaround as seen [here](https://discuss.kde.org/t/dolphins-open-terminal-here-doesnt-work-correctly-plasma-6/40670/7). However, this workaround does not work for older versions (possibly before 49.2) of Ptyxis as seen [here](https://github.com/ublue-os/bazzite/issues/3518).

Another workaround was found for Bazzite Linux that also works on Gentoo. Place this [bash wrapper](https://github.com/ublue-os/bazzite/blob/1545b4c1e952c1af533b57952241b673c4dde386/system_files/desktop/kinoite/usr/bin/kde-ptyxis) in /usr/local/bin and make it executable. This forces Pytxis to open a new window when called, which allows Dolphin to open the terminal in the correct directory. It is possible that this solution will no longer be necessary with future versions of Ptyxis.

## [See also]

-   [Terminal_emulator](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator") --- emulates a video terminal within another display architecture (e.g. in [X](https://wiki.gentoo.org/wiki/X_server "X server")).