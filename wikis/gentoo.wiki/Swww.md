[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Awww&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[![Codeberg Logo](/images/thumb/c/cc/Codeberg-logo.png/30px-Codeberg-logo.png)][Codeberg](https://codeberg.org/LGFae/awww)

*Formerly known as swww.*

**awww** is an Answer to your Wayland Wallpaper Woes. It supports setting wallpapers without restarting the daemon, and animated wallpapers.

** Note**\
awww will not run on [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME"), because [Mutter](https://wiki.gentoo.org/wiki/Mutter "Mutter") does not implement [the wlr-layer-shell protocol](https://wayland.app/protocols/wlr-layer-shell-unstable-v1)\].

## [Installation]

** Note**\
The awww ebuild resides in the [GURU repository](https://wiki.gentoo.org/wiki/Project:GURU "Project:GURU"). The following instructions assume that this repository is set up on your machine. If this is not the case, follow the [GURU setup instructions.](https://wiki.gentoo.org/wiki/Project:GURU/Information_for_End_Users "Project:GURU/Information for End Users")

### [Emerge]

`root `[`#`]`emerge --ask gui-apps/awww`

### [Usage]

Start [[[awww-daemon(1)]](https://man.archlinux.org/man/awww-daemon.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] (e.g. via the compositor\'s configuration file).

Set the wallpaper by using the `img` command of [[[awww(1)]](https://man.archlinux.org/man/awww.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")], described in [[[awww-img(1)]](https://man.archlinux.org/man/awww-img.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")], e.g.:

`user `[`$`]`awww img image.gif`

Stop the daemon via the `kill` command:

`user `[`$`]`awww kill`