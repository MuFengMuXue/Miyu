[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=LilyPond&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://lilypond.org)

[[]][Package information](https://packages.gentoo.org/packages/media-sound/lilypond)

[[]][Official documentation](https://lilypond.org/manuals.html)

[[]][Wikipedia](https://en.wikipedia.org/wiki/LilyPond "wikipedia:LilyPond")

**LilyPond** is a music engraving program, devoted to producing the highest-quality sheet music possible.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Usage]](#Usage)

## [Installation]

### [USE flags]

### [USE flags for] [media-sound/lilypond](https://packages.gentoo.org/packages/media-sound/lilypond) [[]] [GNU Music Typesetter]

  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)       Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`doc`](https://packages.gentoo.org/useflags/doc)           Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`emacs`](https://packages.gentoo.org/useflags/emacs)       Add support for GNU Emacs
  [`profile`](https://packages.gentoo.org/useflags/profile)   Add support for software performance analysis (will likely vary from ebuild to ebuild)
  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-04-23 18:36] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask media-sound/lilypond`

### [Usage]

LilyPond\'s documentation [notes](https://lilypond.org/doc/v2.24/Documentation/usage/normal-usage):

> Most users run LilyPond through a GUI; if you have not done so already, please read the Tutorial. If you use an alternate editor to write LilyPond files, see the documentation for that program.

[Frescobaldi](https://wiki.gentoo.org/index.php?title=Frescobaldi&action=edit&redlink=1 "Frescobaldi (page does not exist)"), [[[media-sound/frescobaldi]](https://packages.gentoo.org/packages/media-sound/frescobaldi)[]], is one such GUI: a LilyPond sheet music text editor with MIDI support. Refer to [the Frescobaldi site](https://www.frescobaldi.org/) for further information.

However, LilyPond can be run directly from the command line. For example, to create a PDF from a LilyPond input file, such as the \"Welcome to LilyPond\" file:

`user `[`$`]`lilypond /usr/share/lilypond/2.24.4/ly/Welcome_to_LilyPond.ly`

Output of PNG, PS, SVG, and MIDI files is also supported; for information about MIDI output, refer to [the \"MIDI block\" section of the LilyPond Notation Reference](https://lilypond.org/doc/v2.25/Documentation/notation/the-midi-block).