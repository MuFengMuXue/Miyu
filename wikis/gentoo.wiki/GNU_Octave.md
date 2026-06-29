[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=GNU_Octave&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://gnu.org/software/octave/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/GNU_Octave "wikipedia:GNU Octave")

[[]][GitWeb](https://hg.savannah.gnu.org/hgweb/octave)

[[]][[#octave](ircs://irc.libera.chat/#octave)] ([[webchat](https://web.libera.chat/#octave)])

**GNU Octave** is a free and open-source computing environment and high-level interactive programming language, that is primarily intended for numerical computations.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Octave packages]](#Octave_packages)
-   [[2] [See also]](#See_also)
-   [[3] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [sci-mathematics/octave](https://packages.gentoo.org/packages/sci-mathematics/octave) [[]] [High-level interactive language for numerical computations]

  ------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------
  [`+glpk`](https://packages.gentoo.org/useflags/+glpk)               Add support for sci-mathematics/glpk for linear programming
  [`+qhull`](https://packages.gentoo.org/useflags/+qhull)             Add support for media-libs/qhull, to allow \`delaunay\', \`convhull\', and related functions
  [`+qrupdate`](https://packages.gentoo.org/useflags/+qrupdate)       Add support for sci-libs/qrupdatefor QR and Cholesky update functions
  [`+sparse`](https://packages.gentoo.org/useflags/+sparse)           Add enhanced support for sparse matrix algebra with SuiteSparse
  [`curl`](https://packages.gentoo.org/useflags/curl)                 Add support for client-side URL transfer library
  [`doc`](https://packages.gentoo.org/useflags/doc)                   Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`fftw`](https://packages.gentoo.org/useflags/fftw)                 Use FFTW library for computing Fourier transforms
  [`gnuplot`](https://packages.gentoo.org/useflags/gnuplot)           Use sci-visualization/gnuplot to render plots if OpenGL is unavailable
  [`gui`](https://packages.gentoo.org/useflags/gui)                   Enable support for a graphical user interface
  [`hdf5`](https://packages.gentoo.org/useflags/hdf5)                 Add support for the Hierarchical Data Format v5
  [`imagemagick`](https://packages.gentoo.org/useflags/imagemagick)   Use media-gfx/graphicsmagick to read and write images
  [`java`](https://packages.gentoo.org/useflags/java)                 Add support for Java
  [`json`](https://packages.gentoo.org/useflags/json)                 Allow using jsonencode and jsondecode commands via dev-libs/rapidjson
  [`klu`](https://packages.gentoo.org/useflags/klu)                   Add support for KLU (sci-libs/klu)
  [`portaudio`](https://packages.gentoo.org/useflags/portaudio)       Add support for the crossplatform portaudio audio API
  [`postscript`](https://packages.gentoo.org/useflags/postscript)     Enable support for the PostScript language (often with ghostscript-gpl or libspectre)
  [`readline`](https://packages.gentoo.org/useflags/readline)         Enable support for libreadline, a GNU line-editing library that almost everyone wants
  [`sndfile`](https://packages.gentoo.org/useflags/sndfile)           Add support for libsndfile
  [`spqr`](https://packages.gentoo.org/useflags/spqr)                 Add support for SPQR (sci-libs/spqr)
  [`ssl`](https://packages.gentoo.org/useflags/ssl)                   Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  [`sundials`](https://packages.gentoo.org/useflags/sundials)         Enable the ode15i and ode15s ODE solvers using sci-libs/sundials
  [`zlib`](https://packages.gentoo.org/useflags/zlib)                 Add support for zlib compression
  ------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-26 21:55] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sci-mathematics/octave`

### [Octave packages]

Octave\'s functionality (i.e. selection of functions available to the user in octave) is extended via octave-packages^[\[1\]](#cite_note-1)^, usually provided by octave-forge^[\[2\]](#cite_note-2)^. There are two ways to install octave packages:

-   Use Octave\'s own [pkg] command to install missing packages (requires the `curl` USE flag)
-   Use [[[app-portage/g-octave]](https://packages.gentoo.org/packages/app-portage/g-octave)[]] to generate ebuilds for octave-packages from Octave-Forge and install them via Portage

There is conflicting information about which method to prefer ^[\[3\]](#cite_note-3)^ ^[\[4\]](#cite_note-4)^, so no recommendation can be given at this point.

## [See also]

-   [Matlab](https://wiki.gentoo.org/wiki/Matlab "Matlab") --- explains how to install and run MathWorks Matlab on Gentoo.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://octave.sourceforge.io/packages.php](https://octave.sourceforge.io/packages.php)]]
2.  [[[↑](#cite_ref-2)] [[https://octave.sourceforge.io/](https://octave.sourceforge.io/)]]
3.  [[[↑](#cite_ref-3)] [[https://wiki.octave.org/Octave-Forge#Installing_packages](https://wiki.octave.org/Octave-Forge#Installing_packages)]]
4.  [[[↑](#cite_ref-4)] [[https://wiki.octave.org/Octave_for_GNU/Linux#Gentoo](https://wiki.octave.org/Octave_for_GNU/Linux#Gentoo)]]