**Resources**

[[]][Home](https://gentle.sysrq.in/)

[[]][Package information](https://packages.gentoo.org/packages/app-portage/gentle)

[[]][GitWeb](https://git.sysrq.in/gentle/)

[[]][[#gentle](ircs://irc.libera.chat/#gentle)] ([[webchat](https://web.libera.chat/#gentle)])

[[]][Bugs (upstream)](https://bugs.sysrq.in/)

**gentle** (*Gent*oo *L*azy *E*ntry) is a [metadata.xml](https://wiki.gentoo.org/wiki/Metadata.xml "Metadata.xml") generator for ebuilds.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
-   [[3] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [app-portage/gentle](https://packages.gentoo.org/packages/app-portage/gentle) [[]] [Gentoo Lazy Entry - a metadata.xml generator]

  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`doc`](https://packages.gentoo.org/useflags/doc)     Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`test`](https://packages.gentoo.org/useflags/test)   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-03 21:45] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install gentle:

`root `[`#`]`emerge --ask app-portage/gentle`

## [Usage]

The [gentle] command takes an ebuild file as input, unpacks sources into a temporary directory and tries to guess upstream metadata.

`user `[`$`]`gentle foo-1.0.ebuild`

## [See also]

-   [metagen](https://wiki.gentoo.org/index.php?title=Metagen&action=edit&redlink=1 "Metagen (page does not exist)")
-   [upstream-ontologist](https://wiki.gentoo.org/index.php?title=Upstream-ontologist&action=edit&redlink=1 "Upstream-ontologist (page does not exist)")