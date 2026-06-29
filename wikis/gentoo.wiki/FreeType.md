[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=FreeType&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://freetype.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/FreeType "wikipedia:FreeType")

[[]][Official documentation](https://freetype.org/freetype2/docs/documentation.html)

[[]][Package information](https://packages.gentoo.org/packages/media-libs/freetype)

*FreeType* is a freely available software library to render fonts. It is written in C, designed to be small, efficient, highly customizable, and portable while capable of producing high-quality output (glyph images) of most vector and bitmap font formats.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
-   [[3] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [media-libs/freetype](https://packages.gentoo.org/packages/media-libs/freetype) [[]] [High-quality and portable font engine]

  --------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+adobe-cff`](https://packages.gentoo.org/useflags/+adobe-cff)                   Use Adobe CFF as default font-renderer
  [`+cleartype-hinting`](https://packages.gentoo.org/useflags/+cleartype-hinting)   Bytecode hinting mode for TrueType fonts that activates subpixel hinting (a.k.a. ClearType hinting) by default
  [`+png`](https://packages.gentoo.org/useflags/+png)                               Add support for libpng (PNG images)
  [`X`](https://packages.gentoo.org/useflags/X)                                     Add support for X11
  [`brotli`](https://packages.gentoo.org/useflags/brotli)                           Enable Brotli compression support
  [`bzip2`](https://packages.gentoo.org/useflags/bzip2)                             Support bzip2 compressed PCF fonts.
  [`debug`](https://packages.gentoo.org/useflags/debug)                             Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`doc`](https://packages.gentoo.org/useflags/doc)                                 Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`fontforge`](https://packages.gentoo.org/useflags/fontforge)                     Install internal headers required for TrueType debugger in media-gfx/fontforge (built with USE=truetype-debugger)
  [`harfbuzz`](https://packages.gentoo.org/useflags/harfbuzz)                       Use media-libs/harfbuzz for auto-hinting OpenType fonts.
  [`static-libs`](https://packages.gentoo.org/useflags/static-libs)                 Build static versions of dynamic libraries as well
  [`svg`](https://packages.gentoo.org/useflags/svg)                                 Add support for SVG (Scalable Vector Graphics)
  [`utils`](https://packages.gentoo.org/useflags/utils)                             Install utilities and examples from ft2demos
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)                   Verify upstream signatures on distfiles
  --------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-05 14:43] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask media-libs/freetype`

## [Usage]

As FreeType is a library, it generally isn\'t used directly, but via other software. However, if the `utils` USE flag is enabled, a number of command-line utilities will be installed:

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------
  Program                                                                                                                                                                                                                                                                                                                                                                                                                         Description
  [[[ftbench(1)]](https://man.archlinux.org/man/ftbench.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]      Benchmark some common FreeType paths
  [[[ftdiff(1)]](https://man.archlinux.org/man/ftdiff.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]         Compare font hinting modes
  [[[ftdump(1)]](https://man.archlinux.org/man/ftdump.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]         Simple font dumper
  [[[ftgamma(1)]](https://man.archlinux.org/man/ftgamma.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]      Screen gamma calibration helper
  [[[ftgrid(1)]](https://man.archlinux.org/man/ftgrid.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]         Simple glyph grid viewer
  [[[ftlint(1)]](https://man.archlinux.org/man/ftlint.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]         Simple font tester
  [[[ftmulti(1)]](https://man.archlinux.org/man/ftmulti.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]      Multiple masters font viewer
  [[[ftsdf(1)]](https://man.archlinux.org/man/ftsdf.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]            A Signed Distance Fields viewer
  [[[ftstring(1)]](https://man.archlinux.org/man/ftstring.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]   String viewer
  [[[ftvalid(1)]](https://man.archlinux.org/man/ftvalid.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]      Font layout table validator
  [[[ftview(1)]](https://man.archlinux.org/man/ftview.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]         Simple glyph viewer
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------

Note that the [ftinspect] utility, introduced in FreeType 2.13.0, does not get installed; refer to [[[bug #903087]](https://bugs.gentoo.org/show_bug.cgi?id=903087)[]].

## [See also]

-   [Fonts](https://wiki.gentoo.org/wiki/Fonts "Fonts") --- home page for information about using fonts on Gentoo
-   [Fonts/Background](https://wiki.gentoo.org/wiki/Fonts/Background "Fonts/Background") --- a quick and informal introduction to font-related concepts, terminology, and systems, with the aim of facilitating understanding and solving font-related issues
-   [Fonts/Software](https://wiki.gentoo.org/wiki/Fonts/Software "Fonts/Software") --- list of end-user software for working with fonts