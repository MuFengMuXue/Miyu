[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Nattka&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://github.com/mgorny/nattka/)

[[]][Package information](https://packages.gentoo.org/packages/app-portage/nattka)

[[]][Official documentation](https://dev.gentoo.org/~mgorny/doc/nattka/)

**NATTkA** is a toolkit for dealing with keywording and stabilization bugs in Gentoo.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [app-portage/nattka](https://packages.gentoo.org/packages/app-portage/nattka) [[]] [A New Arch Tester Toolkit \-- open-source stable-bot replacement]

  ------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`depgraph-order`](https://packages.gentoo.org/useflags/depgraph-order)   Process packages in depgraph order whenever possible.
  [`doc`](https://packages.gentoo.org/useflags/doc)                         Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`test`](https://packages.gentoo.org/useflags/test)                       Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-18 09:14] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-portage/nattka`

## [Usage]

Package list for keywording

`user `[`$`]`nattka make-package-list -a '~arm ~arm64 ~ppc64 ~x86' dev-java/assertj-core`

Package list for stablereq

`user `[`$`]`nattka make-package-list -s 'dev-java/log4j-12-api-2.18.0'`

## [See also]

-   [Pkgcheck](https://wiki.gentoo.org/wiki/Pkgcheck "Pkgcheck") --- a [pkgcore](https://wiki.gentoo.org/wiki/Pkgcore "Pkgcore")-based QA utility for ebuild repos.
-   [Pkgdev](https://wiki.gentoo.org/wiki/Pkgdev "Pkgdev") --- a collection of tools for Gentoo development.

## [External resources]

-   [Devmanual](https://devmanual.gentoo.org/keywording/index.html#moving-from-arch-to-arch)