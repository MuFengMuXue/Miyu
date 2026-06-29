[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Inkscape&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://inkscape.org/)

[[]][Official documentation](https://inkscape.org/learn/)

[[]][Package information](https://packages.gentoo.org/packages/media-gfx/inkscape)

**Inkscape** is a free and open source [vector graphics](https://en.wikipedia.org/wiki/vector_graphics "wikipedia:vector graphics") editor for GNU/Linux, Windows and macOS.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [See also]](#See_also)

## [Installation]

### [USE flags]

The [[[app-text/dblatex]](https://packages.gentoo.org/packages/app-text/dblatex)[]] package has a local `inkscape` [USE flag](https://packages.gentoo.org/useflags/inkscape).

### [USE flags for] [media-gfx/inkscape](https://packages.gentoo.org/packages/media-gfx/inkscape) [[]] [SVG based generic vector-drawing program]

  ------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`X`](https://packages.gentoo.org/useflags/X)                             Add support for X11
  [`cdr`](https://packages.gentoo.org/useflags/cdr)                         Enable support for CorelDRAW files via media-libs/libcdr
  [`dia`](https://packages.gentoo.org/useflags/dia)                         Enable DIA flow chart import via app-office/dia
  [`exif`](https://packages.gentoo.org/useflags/exif)                       Add support for reading EXIF headers from JPEG and TIFF images
  [`graphicsmagick`](https://packages.gentoo.org/useflags/graphicsmagick)   Build and link against GraphicsMagick instead of ImageMagick (requires USE=imagemagick if optional)
  [`imagemagick`](https://packages.gentoo.org/useflags/imagemagick)         Enable optional support for the ImageMagick or GraphicsMagick image converter
  [`inkjar`](https://packages.gentoo.org/useflags/inkjar)                   Enable support for OpenOffice.org SVG jar files
  [`jpeg`](https://packages.gentoo.org/useflags/jpeg)                       Add JPEG image support
  [`openmp`](https://packages.gentoo.org/useflags/openmp)                   Build support for the OpenMP (support parallel computing), requires \>=sys-devel/gcc-4.2 built with USE=\"openmp\"
  [`postscript`](https://packages.gentoo.org/useflags/postscript)           Enable support for the PostScript language (often with ghostscript-gpl or libspectre)
  [`readline`](https://packages.gentoo.org/useflags/readline)               Enable support for libreadline, a GNU line-editing library that almost everyone wants
  [`sourceview`](https://packages.gentoo.org/useflags/sourceview)           Enable syntax highlighting support via x11-libs/gtksourceview
  [`spell`](https://packages.gentoo.org/useflags/spell)                     Add dictionary support
  [`svg2`](https://packages.gentoo.org/useflags/svg2)                       Enable support for new SVG2 features
  [`test`](https://packages.gentoo.org/useflags/test)                       Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`visio`](https://packages.gentoo.org/useflags/visio)                     Enable support for Microsoft Visio diagrams via media-libs/libvisio
  [`wayland`](https://packages.gentoo.org/useflags/wayland)                 Enable dev-libs/wayland backend
  [`wpg`](https://packages.gentoo.org/useflags/wpg)                         Enable support for WordPerfect graphics via app-text/libwpg
  ------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-11 14:07] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask media-gfx/inkscape`

## [See also]

-   [GIMP](https://wiki.gentoo.org/wiki/GIMP "GIMP") - the GNU Image Manipulation Program; can be used as a simple paint tool, photo retouching and general image manipulation.