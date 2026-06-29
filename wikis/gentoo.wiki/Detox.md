[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Detox&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](http://detox.sourceforge.net/)

[[]][Official documentation](http://detox.sourceforge.net/readme.html)

[detox] is a utility that safely removes spaces and strange characters from filenames and directories.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)

## [Installation]

### [USE flags]

### [USE flags for] [app-misc/detox](https://packages.gentoo.org/packages/app-misc/detox) [[]] [Safely remove spaces and strange characters from filenames]

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-19 09:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-misc/detox`

## [Configuration]

### [Files]

-   [/etc/detoxrc] - Detox\'s global configuration file. Specify an alternate configuration file using the `-f` option at the command line.
-   [\~/.detoxrc] - Detox\'s local (per user) configuration file. Specify an alternate configuration file using the `-f` option at the command line.
-   [/usr/share/detox/iso8859_1.tbl] - Detox\'s default ISO 8859-1 translation table. Copy this file into user space in the event that it needs modification. Specify an alternate \'sample\' file using the `-s` option at the command line.
-   [/usr/share/detox/unicode.tbl] - Detox\'s default Unicode (UTF-8) translation table. Copy this file into user space in the event that it needs modification. Specify an alternate \'sample\' file using the `-s` option at the command line.

## [Usage]

### [Invocation]

`user `[`$`]`detox --help`

    usage: detox [-hLnrvV] [-f configfile] [-s sequence] [--dry-run] [--special]
              file [file ...]

            -f configfile   choose which config file to use
            -h --help       this message
            -L              list available sequences and exit
                            with -v ... dump sequence contents
            -n --dry-run    do a dry run (don't actually do anything)
            -r              be recursive (descend into subdirectories)
            --remove-trailing (deprecated)
                            remove trailing _ and - before a period
            -s sequence     choose which sequence to detox with
            --special       work on links and special files
            -v              be verbose
            -V              show the current version

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-misc/detox`