**Resources**

[[]][Home](https://xmlgraphics.apache.org/batik/)

[[]][GitHub](https://github.com/apache/xmlgraphics-batik)

[[]][dev-java/batik](https://packages.gentoo.org/packages/dev-java/batik)

[[]][Bugs](https://bugs.gentoo.org/buglist.cgi?quicksearch=batik)

Batik is a Java-based toolkit for applications or applets that want to use images in the Scalable Vector Graphics (SVG) format for various purposes, such as display, generation or manipulation.

The package has more than 30 modules and is packaged using the [java-pkg-simple](https://devmanual.gentoo.org/eclass-reference/java-pkg-simple.eclass/) [eclass](https://wiki.gentoo.org/wiki/Eclass "Eclass") while the upstream [build system](https://wiki.gentoo.org/wiki/Build_automation "Build automation") is [maven](https://wiki.gentoo.org/wiki/Maven "Maven").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)

## [Installation]

### [USE flags]

### [USE flags for] [dev-java/batik](https://packages.gentoo.org/packages/dev-java/batik) [[]] [XML Graphics Batik]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`doc`](https://packages.gentoo.org/useflags/doc)                 Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`source`](https://packages.gentoo.org/useflags/source)           Zip the sources and install them
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-03-29 14:11] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask dev-java/batik`

## [Usage]

`user `[`$`]`batik-rasterizer`

See [upstream for SVG Rasterizer](https://xmlgraphics.apache.org/batik/tools/rasterizer.html)

`user `[`$`]`batik-slideshow`

`user `[`$`]`batik-squiggle`

See [upstream for Squiggle, the SVG Browser](https://xmlgraphics.apache.org/batik/tools/browser.html)

`user `[`$`]`batik-svgpp`

See [upstream for SVG Pretty Printer](https://xmlgraphics.apache.org/batik/tools/pretty-printer.html)

`user `[`$`]`batik-ttf2svg`

See [upstream for SVG Font Converter](https://xmlgraphics.apache.org/batik/tools/font-converter.html)