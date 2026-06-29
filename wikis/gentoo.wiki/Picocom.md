[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Picocom&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][GitHub](https://github.com/npat-efault/picocom)

[[]][Package information](https://packages.gentoo.org/packages/net-dialup/picocom)

**Picocom** is a minimal terminal emulation program similar to minicom.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
-   [[3] [Removal]](#Removal)
    -   [[3.1] [Unmerge]](#Unmerge)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask net-dialup/picocom`

## [Usage]

Command line utility, for example:

`user `[`$`]`picocom -b 19600 /dev/ttyUSB0`

This opens the serial comms port ttyUSB0 at a baudrate of 19600.

Note: The user will require permission to access [/dev/ttyUSB0]

To exit, use [Ctrl]+[a], then [Ctrl]+[x].

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose net-dialup/picocom`