[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Zathura&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://pwmt.org/projects/zathura/)

[[]][Package information](https://packages.gentoo.org/packages/app-text/zathura)

[[]][Package information](https://packages.gentoo.org/packages/app-text/zathura-meta)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Zathura_(document_viewer) "wikipedia:Zathura (document viewer)")

[[]][GitHub](https://github.com/pwmt/zathura)

[[]][Bugs (upstream)](https://github.com/pwmt/zathura/issues)

**Zathura** is a free, plugin-based document viewer. Plugins are available for PDF (via poppler or MuPDF), PostScript, DjVu, and EPUB. It was written to be lightweight and controlled with vi-like keybindings.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)

## [Installation]

### [USE flags]

### [USE flags for] [app-text/zathura](https://packages.gentoo.org/packages/app-text/zathura) [[]] [Highly customizable & functional document viewer]

  ------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+man`](https://packages.gentoo.org/useflags/+man)           Build and install man pages
  [`X`](https://packages.gentoo.org/useflags/X)                 Add support for X11
  [`landlock`](https://packages.gentoo.org/useflags/landlock)   Build the sandboxed version using the Landlock (a Linux Security Module)
  [`seccomp`](https://packages.gentoo.org/useflags/seccomp)     Enable seccomp (secure computing mode) to perform system call filtering at runtime to increase security of programs
  [`synctex`](https://packages.gentoo.org/useflags/synctex)     Use libsynctex to get latex codeline from pdf
  [`test`](https://packages.gentoo.org/useflags/test)           Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`wayland`](https://packages.gentoo.org/useflags/wayland)     Enable dev-libs/wayland backend
  ------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-12 08:01] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [USE flags for] [app-text/zathura-meta](https://packages.gentoo.org/packages/app-text/zathura-meta) [[]] [Meta package for app-text/zathura plugins]

  ----------------------------------------------------------------- ----------------------------------------------------------------------------------------------------
  [`+pdf`](https://packages.gentoo.org/useflags/+pdf)               Add general support for PDF (Portable Document Format), this replaces the pdflib and cpdflib flags
  [`cb`](https://packages.gentoo.org/useflags/cb)                   Install plug-in for ComicBook support
  [`djvu`](https://packages.gentoo.org/useflags/djvu)               Support DjVu, a PDF-like document format esp. suited for scanned documents
  [`epub`](https://packages.gentoo.org/useflags/epub)               Install plug-in E-Book support
  [`postscript`](https://packages.gentoo.org/useflags/postscript)   Enable support for the PostScript language (often with ghostscript-gpl or libspectre)
  ----------------------------------------------------------------- ----------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-08-06 18:17] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[app-text/zathura]](https://packages.gentoo.org/packages/app-text/zathura)[]] and [[[app-text/zathura-meta]](https://packages.gentoo.org/packages/app-text/zathura-meta)[]]:

`root `[`#`]`emerge --ask app-text/zathura app-text/zathura-meta`

## [Usage]

If you use [xdg-open], you might like to set it to be your default PDF application. First, ensure a desktop entry for zathura exists at [/usr/share/applications/org.pwmt.zathura.desktop]. Then, set zathura as default using [xdg-mime]:

`user `[`$`]`xdg-mime default org.pwmt.zathura.desktop application/pdf`