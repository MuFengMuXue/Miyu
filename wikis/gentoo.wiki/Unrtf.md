[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Unrtf&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.gnu.org/software/unrtf/unrtf.html)

[[]][Package information](https://packages.gentoo.org/packages/app-text/unrtf)

**[unrtf]** is a program for displaying legacy Rich Text Format [.rtf] documents as HTML or plain text. In previous decades before the rise of XML-based office file formats, RTF was used as a \"lowest common denominator\" format that allowed for document sharing between otherwise incompatible word processors.

As with simular tools such as [[antiword](https://wiki.gentoo.org/wiki/Antiword "Antiword")], [unrtf] is often used in combination with standard Linux tools such as [[tail](https://wiki.gentoo.org/wiki/Coreutils#tail "Coreutils")] and [[grep](https://wiki.gentoo.org/wiki/Grep "Grep")]. Additionally, it has the ability to extract embedded images from documents and save them to disk.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
    -   [[1.2] [USE flags]](#USE_flags)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [Removal]](#Removal)
-   [[5] [See Also]](#See_Also)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask app-text/unrtf`

### [USE flags]

### [USE flags for] [app-text/unrtf](https://packages.gentoo.org/packages/app-text/unrtf) [[]] [Converts RTF files to various formats]

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-19 09:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

## [Configuration]

### [Files]

-   [/usr/share/unrtf/] the default location of configuration files for [unrtf].

## [Usage]

### [Invocation]

`user `[`$`]`unrtf --help`

    Usage: unrtf [--version] [--verbose] [--help] [--nopict|-n] [--noremap] [-P config_search_path] [--html] [--text] [--vt] [--latex] [--rtf] [-t <file_with_tags>)] <filename>

The output of `--help` is a bit spartan, but the relevant section of the [unrtf] man file explains the options as follows:

-   `--noremap` disables character set conversion (currently only works for 8-bit character sets).
-   `--html` selects HTML output (default).
-   `--rtf` selects RTF output. The resulting output will often be much smaller than the input.
-   `--text` selects plain ASCII text output.
-   `--vt` selects text output with VT100 escape codes.
-   `--latex` selects output of a LaTeX document.
-   `--verbose` prints additional information.
-   `--quiet` suppress output of leading comments
-   `--version` prints the program version.
-   `-t` *tags_file* specifies the tags output configuration file to be used. The command \"unrtf -t html\" is functionally identical to \"unrtf \--html\". The configuration files are a simple format. To change the behavior of unrtf, a local copy of a system configuration file can be be made and edited. The most complete configuration file and hence the best starting point is [/usr/share/unrtf/html.conf].
-   `-P` *config_search_path* specifies the directories in which the configuration file for the specified format will be sought. The path can be provided as a single directory or a list of colon separated directories. The default is [/usr/share/unrtf] where distributed output configuration files are installed.

## [Removal]

`root `[`#`]`emerge --ask --depclean --verbose app-text/unrtf`

## [See Also]

-   [antiword](https://wiki.gentoo.org/wiki/Antiword "Antiword") --- a program for displaying legacy Microsoft Word [.doc] documents in common use from MS Word 97 -- 2007 as plain text.
-   [pandoc](https://wiki.gentoo.org/wiki/Pandoc "Pandoc") --- a command line tool for document format and markup language conversion written in [Haskell](https://wiki.gentoo.org/wiki/Haskell "Haskell")