[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Pandoc&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://pandoc.org/)

[[]][Official documentation](https://pandoc.org/MANUAL.html)

[[]][Official documentation](https://github.com/jgm/pandoc/wiki)

[[]][Package information](https://packages.gentoo.org/packages/app-text/pandoc)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Pandoc "wikipedia:Pandoc")

[[]][GitHub](https://github.com/jgm/pandoc)

[[]][Bugs (upstream)](https://github.com/jgm/pandoc/issues)

[[]][[#pandoc](ircs://irc.libera.chat/#pandoc)] ([[webchat](https://web.libera.chat/#pandoc)])

**[pandoc]** is a command line tool for document format and markup language conversion written in [Haskell](https://wiki.gentoo.org/wiki/Haskell "Haskell"). Much like a compiler, [pandoc] parses documents with a recursive grammar, converts the input to an intermediate representation, stores that intermediate representation in an abstract syntax tree (AST), and then walks the AST to reproduce the document in the desired output format. However, [pandoc] has its own API for scripted document conversion and custom inport/export filters can be written in [Lua](https://wiki.gentoo.org/wiki/Lua "Lua").

[pandoc] supports a vast number of input and output formats but the list of supported formats is not orthogonal, some formats are export only. Additionally, [pandoc] has its own flavor of markdown that serves as its native document format.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Converting between document types causes loss of some formatting information]](#Converting_between_document_types_causes_loss_of_some_formatting_information)
    -   [[3.2] [Inability to convert MS Word .doc files]](#Inability_to_convert_MS_Word_.doc_files)
    -   [[3.3] [\"File \`lmodern.sty\' not found\" when converting from markdown to pdf]](#.22File_.60lmodern.sty.27_not_found.22_when_converting_from_markdown_to_pdf)
    -   [[3.4] [\"File \`xcolor.sty\' not found\" when converting from markdown to pdf]](#.22File_.60xcolor.sty.27_not_found.22_when_converting_from_markdown_to_pdf)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [app-text/pandoc](https://packages.gentoo.org/packages/app-text/pandoc) [[]] [Metapackage for pandoc version 3]

  ----------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`doc`](https://packages.gentoo.org/useflags/doc)                             Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`embed-data-files`](https://packages.gentoo.org/useflags/embed-data-files)   Embed data files in binary for relocatable executable.
  [`hscolour`](https://packages.gentoo.org/useflags/hscolour)                   Include coloured haskell sources to generated documentation (dev-haskell/hscolour)
  [`profile`](https://packages.gentoo.org/useflags/profile)                     Add support for software performance analysis (will likely vary from ebuild to ebuild)
  [`test`](https://packages.gentoo.org/useflags/test)                           Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`trypandoc`](https://packages.gentoo.org/useflags/trypandoc)                 Build trypandoc cgi executable.
  ----------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2024-10-01 21:02] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

For the **[amd64]** and **[arm64]** architectures the binary package [[[app-text/pandoc-bin]](https://packages.gentoo.org/packages/app-text/pandoc-bin)[]] is available. To install this precompiled version, replace pandoc with pandoc-bin in the following installation command:

`root `[`#`]`emerge --ask app-text/pandoc`

## [Configuration]

### [Files]

-   [\$HOME/.local/share] or as specified in `$XDG_DATA_HOME` - Local (per user) configuration file.

## [Troubleshooting]

### [Converting between document types causes loss of some formatting information]

To some extent this is expected behavior. Not all document formats are equally robust. Further, the intermediate representation used by [pandoc] does not preserve every possible formatting option.

### [Inability to convert MS Word [.doc] files]

This is expected behavior, modern MS Office [.docx] files are supported but legacy [.doc] files are not. There are two possible workarounds:

The most basic option is to use [[antiword](https://wiki.gentoo.org/wiki/Antiword "Antiword")] to convert the [.doc] to plain text.

`user `[`$`]`antiword legacy_document.doc > legacy_document.txt`

This is a valid for many use cases but a lot of formatting information can be lost this way.

A more robust solution is to leverage a little-known feature of antiword, DocBook XML output support, in order to ensure a well formatted document conversion:

`user `[`$`]`antiword -x db infile.doc | pandoc -f docbook`

The last option is to import the [.doc] document into [LibreOffice](https://wiki.gentoo.org/wiki/LibreOffice "LibreOffice") and export it as either LibreOffice\'s native [.odt] or MS Office\'s modern [.docx] format. Once you have the [.docx] version of the file you can leverage pandoc as normal.

This can even be accomplished from the command line as follows:

`user `[`$`]`libreoffice --convert-to odt legacy_document.doc`

Your mileage may vary as to whether the antiword DocBook XML or LibreOffice conversion methods results in a better document conversion, but there should be few if any differences between the two methods in the resulting output.

### [][\"File \`lmodern.sty\' not found\" when converting from markdown to pdf]

By default, Pandoc will attempt to create the PDF using [LaTeX](https://wiki.gentoo.org/wiki/LaTeX "LaTeX"), which requires the [lm] LaTeX package provided by [[[dev-texlive/texlive-fontsrecommended]](https://packages.gentoo.org/packages/dev-texlive/texlive-fontsrecommended)[]] to be installed:

`root `[`#`]`emerge --ask dev-texlive/texlive-fontsrecommended`

### [][\"File \`xcolor.sty\' not found\" when converting from markdown to pdf]

Similarly, Pandoc also requires the LaTeX package [xcolor] for PDF creation, which is supplied by [[[dev-texlive/texlive-latexrecommended]](https://packages.gentoo.org/packages/dev-texlive/texlive-latexrecommended)[]]:

`root `[`#`]`emerge --ask dev-texlive/texlive-latexrecommended`

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-text/pandoc`

## [See also]

-   [antiword](https://wiki.gentoo.org/wiki/Antiword "Antiword") --- a program for displaying legacy Microsoft Word [.doc] documents in common use from MS Word 97 -- 2007 as plain text.
-   [unrtf](https://wiki.gentoo.org/wiki/Unrtf "Unrtf") --- a program for displaying legacy Rich Text Format [.rtf] documents as HTML or plain text.
-   [[[app-text/lowdown]](https://packages.gentoo.org/packages/app-text/lowdown)[]] a program converting from markdown to html, latex, man, odt and other

## [External resources]

-   [Page about pandoc on Gentoo on the pandoc wiki](https://github.com/jgm/pandoc/wiki/Pandoc-with-gentoo)