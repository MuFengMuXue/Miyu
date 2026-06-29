[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=U-boot-tools&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[[]][Home](https://www.denx.de/wiki/U-Boot/WebHome)

[[]][Package information](https://packages.gentoo.org/packages/dev-embedded/u-boot-tools)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Das_U-Boot "wikipedia:Das U-Boot")

**U-Boot tools** is a collection of utilities for working with Das U-boot - a bootloader often used on embedded systems.

Currently the Das U-boot source is not available as a Gentoo Package.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Additional software]](#Additional_software)
    -   [[1.4] [Unmerge]](#Unmerge)

## [Installation]

### [USE flags]

### [USE flags for] [dev-embedded/u-boot-tools](https://packages.gentoo.org/packages/dev-embedded/u-boot-tools) [[]] [utilities for working with Das U-Boot]

  ------------------------------------------------------------- ----------------------------------------------
  [`envtools`](https://packages.gentoo.org/useflags/envtools)   Build only the target-side environment tools
  ------------------------------------------------------------- ----------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-27 14:22] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask dev-embedded/u-boot-tools`

### [Additional software]

-   [Embedded Handbook/Bootloaders/Das U-Boot](https://wiki.gentoo.org/wiki/Embedded_Handbook/Bootloaders/Das_U-Boot "Embedded Handbook/Bootloaders/Das U-Boot") for further information on Das U-boot

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose dev-embedded/u-boot-tools`