[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Dtc&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.devicetree.org/)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/dtc)

[[]][Official documentation](https://elinux.org/Device_Tree_Reference/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/devicetree "wikipedia:devicetree")

**Device Tree Compiler** (DTC) is a tool to create device tree binaries (dtbs) from device tree source.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Decompiling dtb to dts]](#Decompiling_dtb_to_dts)
-   [[3] [Removal]](#Removal)
    -   [[3.1] [Unmerge]](#Unmerge)

## [Installation]

### [USE flags]

### [USE flags for] [sys-apps/dtc](https://packages.gentoo.org/packages/sys-apps/dtc) [[]] [Open Firmware device tree compiler]

  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`python`](https://packages.gentoo.org/useflags/python)             Add optional support/bindings for the Python language
  [`static-libs`](https://packages.gentoo.org/useflags/static-libs)   Build static versions of dynamic libraries as well
  [`test`](https://packages.gentoo.org/useflags/test)                 Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`yaml`](https://packages.gentoo.org/useflags/yaml)                 support .yaml-encoded device trees
  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-19 15:52] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sys-apps/dtc`

## [Usage]

Used when creating device tree binaries. Typically when create a primary bootloader like U-boot

### [Decompiling dtb to dts]

[dtc] can be used to decompile a **dtb** (*device tree blob*) back into a **dts** (*device tree source*) with:

`user `[`$`]`dtc -I dtb infile.dtb -O dts -o outfile.dts`

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose sys-apps/dtc`