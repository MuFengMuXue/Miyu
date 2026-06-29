[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Dust&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][GitHub](https://github.com/bootandy/dust)

[[]][Package information](https://packages.gentoo.org/packages/sys-block/dust)

Dust is a command-line tool similar to [du] that displays file and directory usage with a bar displaying its percentage.

## Contents

-   [[1] [Installing]](#Installing)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Displaying usage statistics]](#Displaying_usage_statistics)
    -   [[2.2] [Not displaying bars]](#Not_displaying_bars)
    -   [[2.3] [Reverse output]](#Reverse_output)
    -   [[2.4] [Filter files]](#Filter_files)
-   [[3] [See also]](#See_also)

## [Installing]

### [USE flags]

### [USE flags for] [sys-block/dust](https://packages.gentoo.org/packages/sys-block/dust) [[]] [A more intuitive version of du]

  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-19 00:21] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sys-block/dust`

## [Usage]

### [Displaying usage statistics]

To display the storage use in a directory, run [dust]:

`user `[`$`]`dust`

### [Not displaying bars]

To have the usage bars not show up, use the `-b` or `--no-percent-bars` arguments:

`user `[`$`]`dust --no-percent-bars`

### [Reverse output]

To have the biggest directories show up on the top, use the `-r` or \--reverse argument:

`user `[`$`]`dust --reverse`

### [Filter files]

To filter the files searched, use `-e` or `--filter` arguments:

`user `[`$`]`dust --filter "build\.log"`

## [See also]

-   [ncdu](https://wiki.gentoo.org/wiki/Ncdu "Ncdu") --- a disk usage analyzer with an ncurses interface