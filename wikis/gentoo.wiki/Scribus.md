[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Scribus&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.scribus.net/)

[[]][Official documentation](https://docs.scribus.net)

[[]][Package information](https://packages.gentoo.org/packages/app-office/scribus)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Scribus "wikipedia:Scribus")

[[]][Bugs (upstream)](https://bugs.scribus.net/)

[[]][[#scribus](ircs://irc.libera.chat/#scribus)] ([[webchat](https://web.libera.chat/#scribus)])

[[]][Blog](https://www.scribus.net/category/news/)

**Scribus** is a full-featured [Qt](https://wiki.gentoo.org/wiki/Qt "Qt")-based desktop publishing package available for Linux, Windows, MacOS, and other operating systems. Scribus uses its own XML-based file format [.sla] to to store documents. It is Unicode native and supports layouts with complex scripts such as kanji and right-to-left scripts such as Arabic and Hebrew. In Scribus the document is just a canvas with various frames. Text must be placed inside of a text frame. Images tables have their own frame types and, much like commonly used graphics programs such as [GIMP](https://wiki.gentoo.org/wiki/GIMP "GIMP"), frames can be layered to achive a specific effect.

Scribus can import text from a variety of common open formats with various limitations. OpenDocument Text [.odt] documents have the highest degree of support, Scribus\' import filter can import document text along with paragraph style information. Additionally, HTML and PUB documents have a high degree of support as well. Microsoft\'s Office Open XML [.docx] can be read by Scribus with reasonable fidelity. Indirect support for legacy Microsoft Word [.doc] files is possible indirectly via [[antiword](https://wiki.gentoo.org/wiki/Antiword "Antiword")]. Lowest common denominator file formats such as [.rtf], MarkDown, and plain text will work but by their nature contain no useful paragraph formatting information.

## Contents

-   [[1] [Support for Desktop Publishing File Formats]](#Support_for_Desktop_Publishing_File_Formats)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [USE flags]](#USE_flags)
    -   [[2.2] [Emerge]](#Emerge)
    -   [[2.3] [Additional software]](#Additional_software)
    -   [[2.4] [Invocation]](#Invocation)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Scribus can import .doc files on Windows but not on Linux]](#Scribus_can_import_.doc_files_on_Windows_but_not_on_Linux)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)

## [Support for Desktop Publishing File Formats]

Generally, Scribus cannot read or write the closed source undocumented file formats of commercial desktop publishing programs. The rare exception being Scribus support for the Microsoft Publisher 2000 documents by means of the [libmspub library](https://wiki.documentfoundation.org/DLP/Libraries/libmspub) produced by the OpenDocument foundation. This library has partial import capability for Publisher 95--98 documents but functionality remains spotty.

Lightweight desktop publishing interchange formats such as QuarkXPress Tag, InDesign\'s IDML, and InCopy\'s ICML can all be used with Scribus as they\'re publicly documented.

## [Installation]

### [USE flags]

### [USE flags for] [app-office/scribus](https://packages.gentoo.org/packages/app-office/scribus) [[]] [Desktop publishing (DTP) and layout program]

  ------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+boost`](https://packages.gentoo.org/useflags/+boost)                   Enable support for Boost based enhancement
  [`+minimal`](https://packages.gentoo.org/useflags/+minimal)               Don\'t install headers (only required for e.g. plug-in developers)
  [`+pdf`](https://packages.gentoo.org/useflags/+pdf)                       Add general support for PDF (Portable Document Format), this replaces the pdflib and cpdflib flags
  [`+templates`](https://packages.gentoo.org/useflags/+templates)           Document templates
  [`debug`](https://packages.gentoo.org/useflags/debug)                     Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`examples`](https://packages.gentoo.org/useflags/examples)               Install examples, usually source code
  [`graphicsmagick`](https://packages.gentoo.org/useflags/graphicsmagick)   Build and link against GraphicsMagick instead of ImageMagick (requires USE=imagemagick if optional)
  [`osg`](https://packages.gentoo.org/useflags/osg)                         3D rendering via dev-games/openscenegraph
  [`scripts`](https://packages.gentoo.org/useflags/scripts)                 Install the scripts
  [`tk`](https://packages.gentoo.org/useflags/tk)                           Install tk based scripts e.g. FontSample.py
  ------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-09 19:41] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-office/scribus`

### [Additional software]

Legacy Microsoft Word [.doc] document file support via [[antiword](https://wiki.gentoo.org/wiki/Antiword "Antiword")].

### [Invocation]

`user `[`$`]`scribus --help`

    Scribus, Open Source Desktop Publishing
    ---------------------------------------
    Homepage:       http://www.scribus.net
    Documentation:  http://docs.scribus.net
    Wiki:           http://wiki.scribus.net
    Issues:         http://bugs.scribus.net

    Usage: scribus [options] [files]

    Options:
         -fi,  --font-info                      Show information on the console when fonts are being loaded
         -h,   --help                           Print help (this message) and exit
         -l,   --lang                           Uses xx as shortcut for a language, eg `en' or `de'
         -la,  --langs-available                List the currently installed interface languages
         -ns,  --no-splash                      Do not show the splashscreen on startup
         -nns, --never-splash                   Stop showing the splashscreen on startup. Writes an empty file called .neversplash in ~/.config/scribus
         -pr,  --prefs                    Use path for user given preferences location
         -pi,  --profile-info                   Show location of ICC profile information on console while starting
         -u,   --upgradecheck                   Download a file from the Scribus website and show the latest available version
         -v,   --version                        Output version information and exit
         -py,  --python-script <script> [arguments ...]  Run script in Python [with optional arguments]. This option must be last option used
         -g,   --no-gui                         Do not start GUI
         --                                     Explicit end of command line options

## [Troubleshooting]

### [Scribus can import [.doc] files on Windows but not on Linux]

Scribus uses [antiword](https://wiki.gentoo.org/wiki/Antiword "Antiword") as an import filter for legacy Microsoft Office [.doc] files. Upstream builds of Scribus for Windows bundle *antiword* with with Scribus. Upstream builds for Linux do not contain *antiword* by default but will use it if it happens to be present on the system. Gentoo mimics this behavior. This issue can be addressed by installing antiword:

`root `[`#`]`emerge --ask app-text/antiword`

Once Scribus is restarted the [.doc] will become a valid import option. Alternatively, if [LibreOffice](https://wiki.gentoo.org/wiki/LibreOffice "LibreOffice") is installed the document can be converted to OpenDocument Text format directly:

`user `[`$`]`libreoffice --headless --convert-to odt *.doc`

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-office/scribus`

## [See also]

-   [TeX Live](https://wiki.gentoo.org/wiki/TeX_Live "TeX Live") --- a complete [TeX](https://en.wikipedia.org/wiki/TeX "wikipedia:TeX") distribution with several programs to create professional documents.
-   [AsciiDoc](https://wiki.gentoo.org/index.php?title=AsciiDoc&action=edit&redlink=1 "AsciiDoc (page does not exist)")
-   [LibreOffice](https://wiki.gentoo.org/wiki/LibreOffice "LibreOffice") --- a full office productivity suite.
-   [pandoc](https://wiki.gentoo.org/wiki/Pandoc "Pandoc") --- a command line tool for document format and markup language conversion written in [Haskell](https://wiki.gentoo.org/wiki/Haskell "Haskell")
-   [antiword](https://wiki.gentoo.org/wiki/Antiword "Antiword") --- a program for displaying legacy Microsoft Word [.doc] documents in common use from MS Word 97 -- 2007 as plain text.