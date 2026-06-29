[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Dedicated_Build_Machine-Single_ARCH&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[[]]This article has some todo items:\

-   A lot of the packages will be broken, explain where to report

This page shows how to create a single dedicated build machine to compile software for multiple target devices of a single **ARCH**.

The main target **ARCH** for this is the *amd64* architecture due to the amount of resources needed to handle the building process, but the process itself is agnostic to what **ARCH** is being used.

Throughout this article **BUILD** will refer to the build machine on which we are doing the compilation of the software and **HOST** will refer to the machine which will finally be running the compiled software.

## Contents

-   [[1] [Overview]](#Overview)
    -   [[1.1] [Caveats of **EAPI** \< 7]](#Caveats_of_EAPI_.3C_7)
    -   [[1.2] [Double nesting]](#Double_nesting)
-   [[2] [Prepare **BUILD** machine]](#Prepare_BUILD_machine)
-   [[3] [Prepare individual chroots]](#Prepare_individual_chroots)
-   [[4] [Mount necessary directories]](#Mount_necessary_directories)
-   [[5] [Compiling for **HOST**]](#Compiling_for_HOST)

## [Overview]

### [][Caveats of **EAPI** \< 7]

### [Double nesting]

## [Prepare **BUILD** machine]

## [Prepare individual chroots]

## [Mount necessary directories]

## [Compiling for **HOST**]