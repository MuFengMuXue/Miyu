[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Gsettings&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[gsettings] is a command-line program allowing getting and setting configuration values in a [dconf](https://en.wikipedia.org/wiki/dconf "wikipedia:dconf") database. Unlike the [[[dconf(1)]](https://man.archlinux.org/man/dconf.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] tool, [[[gsettings(1)]](https://man.archlinux.org/man/gsettings.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] performs type and consistency checks. [gsettings] is provided by the [[[dev-libs/glib]](https://packages.gentoo.org/packages/dev-libs/glib)[]] package.

Collections of configuration data are called *schemas*; the [[[gsettings-desktop-schemas]](https://packages.gentoo.org/packages/gsettings-desktop-schemas)[]] package provides various schemas for the [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME") desktop.

## [Usage]

List installed schemas:

`user `[`$`]`gsettings list-schemas`

List the keys associated with a particular schema, including their current values:

`user `[`$`]`gsettings list-recursively org.gnome.desktop.interface`

Describe the meaning of a particular key, e.g. `gtk-theme`:

`user `[`$`]`gsettings describe org.gnome.desktop.interface gtk-theme`

Get the current value of a particular key, e.g. `text-scaling-factor`:

`user `[`$`]`gsettings get org.gnome.desktop.interface text-scaling-factor`

Set the current value of a particular key, e.e. `text-scaling-factor`:

`user `[`$`]`gsettings set org.gnome.desktop.interface text-scaling-factor 2.0`

## [See also]

-   [GTK](https://wiki.gentoo.org/wiki/GTK "GTK") --- a toolkit for creating graphical user interfaces.
-   [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME") --- a feature-rich desktop environment provided by the [GNOME project](https://www.gnome.org).