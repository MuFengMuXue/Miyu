[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=ReText&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://github.com/retext-project/retext)

**ReText** is a Linux ready, simple (yet powerful) text editor for [Markdown](https://en.wikipedia.org/wiki/Markdown "wikipedia:Markdown") and reStructured text. ReText includes a built in \"Live preview\" function so that writers can see their changes in real-time.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Troubleshooting]](#Troubleshooting)
    -   [[2.1] [No icons in toolbar]](#No_icons_in_toolbar)
-   [[3] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [app-editors/retext](https://packages.gentoo.org/packages/app-editors/retext) [[]] [Simple editor for Markdown and reStructuredText]

  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`test`](https://packages.gentoo.org/useflags/test)   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-14 09:42] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Emerge ReText just like any standard program:

`root `[`#`]`emerge --ask app-editors/retext`

## [Troubleshooting]

### [No icons in toolbar]

If the icons are missing the icon theme needs to be specified in gconf or in the ReText configuration file.

[FILE] **`~/.config/ReText project/ReText.conf`**

    [General]
    iconTheme=gnome

Available icon themes are located in [/usr/share/icons/] (hicolor will not work).

## [See also]