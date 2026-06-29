[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=MuPDF&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://mupdf.com/)

[[]][Package information](https://packages.gentoo.org/packages/app-text/mupdf)

[[]][Wikipedia](https://en.wikipedia.org/wiki/MuPDF "wikipedia:MuPDF")

[[]][GitHub](https://github.com/ArtifexSoftware/mupdf)

[[]][Bugs (upstream)](https://bugs.ghostscript.com/buglist.cgi?product=MuPDF)

MuPDF is a free and open-source software framework written in C that implements a PDF, XPS, and EPUB parsing and rendering engine, that can work as a standalone pdf reader. In Gentoo, several packages like [[[app-text/llpp]](https://packages.gentoo.org/packages/app-text/llpp)[]] or [[[app-text/zathura-pdf-mupdf]](https://packages.gentoo.org/packages/app-text/zathura-pdf-mupdf)[]] use it internally for PDF rendering.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [app-text/mupdf](https://packages.gentoo.org/packages/app-text/mupdf) [[]] [A lightweight PDF viewer and toolkit written in portable C]

  ------------------------------------------------------------------- --------------------------------------------------------------------------------------
  [`+javascript`](https://packages.gentoo.org/useflags/+javascript)   Enable javascript support
  [`+jpeg2k`](https://packages.gentoo.org/useflags/+jpeg2k)           Support for JPEG 2000, a wavelet-based image compression format
  [`X`](https://packages.gentoo.org/useflags/X)                       Add support for X11
  [`archive`](https://packages.gentoo.org/useflags/archive)           Enable support for CBR and other archive formats using libarchive
  [`barcode`](https://packages.gentoo.org/useflags/barcode)           Enable support for barcode detection/generation for mutool using zxingcpp
  [`brotli`](https://packages.gentoo.org/useflags/brotli)             Enable Brotli compression support
  [`opengl`](https://packages.gentoo.org/useflags/opengl)             Add support for OpenGL (3D graphics)
  [`ssl`](https://packages.gentoo.org/useflags/ssl)                   Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  ------------------------------------------------------------------- --------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-28 14:22] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

** Note**\
In order to use MuPDF as a pdf reader and not just as a framework you will need to enable `opengl`,`javascript` and `X` if X11 will be used, without those use flags enabled, you will not get a [mupdf] binary.

The package provides the following binaries:

-   [mupdf]
-   [mupdf-gl]
-   [mupdf-x11]
-   [mupdf-x11-curl]
-   [mutool]: all purpose tool for dealing with PDF files (draw, clean, extract, info, create, pages, poster, show, run JavaScript, convert, merge)

### [Emerge]

Install [[[app-text/mupdf]](https://packages.gentoo.org/packages/app-text/mupdf)[]]:

`root `[`#`]`emerge --ask app-text/mupdf`

## [External resources]

-   [http://www.linuxfromscratch.org/blfs/view/cvs/pst/mupdf.html](http://www.linuxfromscratch.org/blfs/view/cvs/pst/mupdf.html)
-   [https://packages.debian.org/buster/mupdf](https://packages.debian.org/buster/mupdf)
-   [https://wiki.archlinux.org/index.php/MuPDF](https://wiki.archlinux.org/index.php/MuPDF)
-   [https://www.mupdf.com/product/ecosystem](https://www.mupdf.com/product/ecosystem) --- Overview of projects, viewers, tools, and libraries based on MuPDF