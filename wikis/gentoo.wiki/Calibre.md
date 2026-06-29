[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Calibre&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://calibre-ebook.com/)

[[]][Package information](https://packages.gentoo.org/packages/app-text/calibre)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Calibre_(software) "wikipedia:Calibre (software)")

[[]][GitHub](https://github.com/kovidgoyal/calibre)

[[]][[#calibre](ircs://irc.libera.chat/#calibre)] ([[webchat](https://web.libera.chat/#calibre)])

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/calibre)

**Calibre** is an electronic book management tool.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Troubleshooting]](#Troubleshooting)
    -   [[2.1] [Unable to obtain/generate cover art]](#Unable_to_obtain.2Fgenerate_cover_art)
-   [[3] [Removal]](#Removal)
    -   [[3.1] [Unmerge]](#Unmerge)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [app-text/calibre](https://packages.gentoo.org/packages/app-text/calibre) [[]] [Ebook management application]

  ----------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+font-subsetting`](https://packages.gentoo.org/useflags/+font-subsetting)   Enable font subsetting support
  [`+system-mathjax`](https://packages.gentoo.org/useflags/+system-mathjax)     Use a system copy of mathjax
  [`+udisks`](https://packages.gentoo.org/useflags/+udisks)                     Enable storage management support (automounting, volume monitoring, etc)
  [`ios`](https://packages.gentoo.org/useflags/ios)                             Enable support for Apple\'s iDevice with iOS operating system (iPad, iPhone, iPod, etc)
  [`speech`](https://packages.gentoo.org/useflags/speech)                       Enable text-to-speech support
  [`test`](https://packages.gentoo.org/useflags/test)                           Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`unrar`](https://packages.gentoo.org/useflags/unrar)                         Enable support for comic books compressed with the non-free Rar format
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)               Verify upstream signatures on distfiles
  ----------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-22 01:47] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-text/calibre`

## [Troubleshooting]

### [][Unable to obtain/generate cover art]

Calibre requires [[[dev-qt/qtgui]](https://packages.gentoo.org/packages/dev-qt/qtgui)[]] to have jpeg support for cover art. See [[[bug #676664]](https://bugs.gentoo.org/show_bug.cgi?id=676664)[]]

[FILE] **`/etc/portage/package.use/calibre`**

    dev-qt/qtgui jpeg

`root `[`#`]`emerge --ask --oneshot dev-qt/qtgui`

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-text/calibre`

## [See also]

-   [Gentoo Wiki:Suggestions/Archive](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Suggestions/Archive#Print_to_PDF_and.2For_Export_to_EBook_File_Format.3F "Gentoo Wiki:Suggestions/Archive")
-   [QT Desktop Applications](https://wiki.gentoo.org/wiki/Qt_Desktop_applications "Qt Desktop applications") --- a list of recommendations for a light-weight, non-KDE, Qt-only desktop environment.
-   [Recommended Applications](https://wiki.gentoo.org/wiki/Recommended_applications "Recommended applications") --- applications recommended for use in a graphical environment ([X11](https://wiki.gentoo.org/wiki/Xorg "Xorg"), [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland"))

## [External resources]

-   [https://calibre-ebook.com/](https://calibre-ebook.com/)