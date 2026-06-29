[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Antiword&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](http://www.winfield.demon.nl/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Antiword "wikipedia:Antiword")

[[]][Package information](https://packages.gentoo.org/packages/app-text/antiword)

**[antiword]** is a program for displaying legacy Microsoft Word [.doc] documents in common use from MS Word 97 -- 2007 as plain text. Typically, antiword is used to display MS Word documents in a terminal window often in combination with standard Linux tools such as [[head](https://wiki.gentoo.org/wiki/Coreutils#head "Coreutils")] and [[grep](https://wiki.gentoo.org/wiki/Grep "Grep")]. Additionally, it has the ability to extract images from MS Word documents and save them to disk.

Despite the fact that development of [antiword] has stagnated and there have been no releases since 2005 it is nonetheless frequently used by other software packages to handle legacy MS Word documents. For example, the desktop publishing software Scribus uses antiword as an import filter for [.doc] documents and users of the text-based email client [[mutt](https://wiki.gentoo.org/wiki/Mutt "Mutt")] frequently use it to display such documents in the terminal as well.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Environment variables]](#Environment_variables)
    -   [[1.4] [Files]](#Files)
-   [[2] [Removal]](#Removal)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [antiword cannot find its home directory]](#antiword_cannot_find_its_home_directory)
-   [[5] [Limitations]](#Limitations)
-   [[6] [See Also]](#See_Also)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask app-text/antiword`

### [USE flags]

### [USE flags for] [app-text/antiword](https://packages.gentoo.org/packages/app-text/antiword) [[]] [free MS Word reader]

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-19 09:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Environment variables]

-   `ANTIWORDHOME` the location of antiword\'s configuration files.
-   `COLUMNS` the width of output unless overridden by the `-w` option.

### [Files]

-   [/usr/share/antiword/] --- Global (system wide) configuration files for mapping code pages to UTF-8 output.
-   [\~/.antiword] --- This file may contain a path which specifies an alternate location for code page map files; `$ANTIWORDHOME` is preferred.

## [Removal]

`root `[`#`]`emerge --ask --depclean --verbose app-text/antiword`

## [Usage]

### [Invocation]

`user `[`$`]`antiword -h`

      Name: antiword
        Purpose: Display MS-Word files
        Author: (C) 1998-2005 Adri van Os
        Version: 0.37  (21 Oct 2005)
        Status: GNU General Public License
        Usage: antiword [switches] wordfile1 [wordfile2 ...]
        Switches: [-f|-t|-a papersize|-p papersize|-x dtd][-m mapping][-w #][-i #][-Ls]
            -f formatted text output
            -t text output (default)
            -a  Adobe PDF output
            -p  PostScript output
              paper size like: a4, letter or legal
            -x <dtd> XML output
              like: db (DocBook)
            -m <mapping> character mapping file
            -w <width> in characters of text output
            -i <level> image level (PostScript only)
            -L use landscape mode (PostScript only)
            -r Show removed text
            -s Show hidden (by Word) text

## [Troubleshooting]

### [[antiword] cannot find its home directory]

This is a known issue with [antiword] that comes up most often in hosted environments. The solution is to set `$ANTIWORDHOME` to the location of its configuration files, usually [/usr/share/antiword].

## [Limitations]

-   While quite usable, Antiword is far from complete and cannot render complex layouts or obscure formatting to a text terminal without compromise.
-   [antiword] predates Microsoft Office XML formats and therefore lacks support for the [.docx] file format entirely.
-   [antiword] cannot tell the difference between a file that cannot be read and a file that does not exist.
-   [antiword] long predates the XDG Base Directory Specification so it lacks direct support for it.

## [See Also]

-   [unrtf](https://wiki.gentoo.org/wiki/Unrtf "Unrtf") --- a program for displaying legacy Rich Text Format [.rtf] documents as HTML or plain text.
-   [pandoc](https://wiki.gentoo.org/wiki/Pandoc "Pandoc") --- a command line tool for document format and markup language conversion written in [Haskell](https://wiki.gentoo.org/wiki/Haskell "Haskell")