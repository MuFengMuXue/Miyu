[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Mgorny-dev-scripts&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][GitHub](https://github.com/projg2/mgorny-dev-scripts)

[[]][Package information](https://packages.gentoo.org/packages/app-portage/mgorny-dev-scripts)

mgorny-dev-scripts is a collection of useful utilities to improve the ebuild development experience.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Pkgdiff-mg]](#Pkgdiff-mg)
        -   [[2.1.1] [Basic diff]](#Basic_diff)
        -   [[2.1.2] [Comparing build system changes]](#Comparing_build_system_changes)
-   [[3] [See also]](#See_also)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask app-portage/mgorny-dev-scripts`

## [Usage]

### [Pkgdiff-mg]

[pkgdiff-mg] is a diff\'ing tool that shows the differences in the source code between two different package versions.

#### [Basic diff]

To show the complete diff between `package-1.0.0.ebuild` and `package-2.0.0.ebuild`:

`user `[`$`]`pkgdiff-mg package-1.0.0.ebuild package-2.0.0.ebuild`

#### [Comparing build system changes]

To only view the build system changes, use `--build-system` or `-b`:

`user `[`$`]`pkgdiff-mg -b package-1.0.0.ebuild package-2.0.0.ebuild`

## [See also]

-   [Iwdevtools](https://wiki.gentoo.org/wiki/Iwdevtools "Iwdevtools") --- a group of small tools to aid with Gentoo development, primarily intended for QA.
-   [Pkgdev](https://wiki.gentoo.org/wiki/Pkgdev "Pkgdev") --- a collection of tools for Gentoo development.