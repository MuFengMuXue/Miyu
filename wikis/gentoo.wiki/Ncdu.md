[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Ncdu&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][ncdu](https://code.blicky.net/yorhel/ncdu)

[[]][Package information (ncdu)](https://packages.gentoo.org/packages/sys-fs/ncdu)

[[]][Package information (ncdu-bin)](https://packages.gentoo.org/packages/sys-fs/ncdu-bin)

Ncdu is a disk usage analyzer with an ncurses interface. It is designed to find space hogs on a remote server where you don't have an entire graphical setup available, but it is a useful tool even on regular desktop systems. Ncdu aims to be fast, simple and easy to use, and should be able to run in any minimal POSIX-like environment with ncurses installed.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Directory usage statistics]](#Directory_usage_statistics)
    -   [[2.2] [Extended information]](#Extended_information)
-   [[3] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [sys-fs/ncdu](https://packages.gentoo.org/packages/sys-fs/ncdu) [[]] [NCurses Disk Usage]

  ----------------------------------------------------------------- -----------------------------------------
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- -----------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-26 00:28] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [USE flags for] [sys-fs/ncdu-bin](https://packages.gentoo.org/packages/sys-fs/ncdu-bin) [[]] [NCurses Disk Usage]

  ----------------------------------------------------------------- -----------------------------------------
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- -----------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-09-22 23:55] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sys-fs/ncdu`

`root `[`#`]`emerge --ask sys-fs/ncdu-bin`

## [Usage]

** Note**\
This article uses [ncdu] to refer to running ncdu, but installing [[[sys-fs/ncdu-bin]](https://packages.gentoo.org/packages/sys-fs/ncdu-bin)[]] will use the command [ncdu-bin]

### [Directory usage statistics]

To get basic directory usage statistics, run [ncdu] or [ncdu-bin]:

`user `[`$`]`ncdu`

### [Extended information]

To enable reading additional information, such as ownership, permissions, and last modification time, use the `-e` argument:

`user `[`$`]`ncdu -e`

## [See also]

-   [Dust](https://wiki.gentoo.org/wiki/Dust "Dust") --- a command-line tool similar to [du] that displays file and directory usage with a bar displaying its percentage.