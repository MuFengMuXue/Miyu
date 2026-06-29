[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Make&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.gnu.org/software/make/make.html)

[[]][Package information](https://packages.gentoo.org/packages/sys-devel/make)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Make_(software) "wikipedia:Make (software)")

**Make** is a [tool to *build*](https://wiki.gentoo.org/wiki/Build_automation#Available_software "Build automation") software from source code (which usually includes compiling). [makefiles](https://en.wikipedia.org/wiki/Make_(software)#Makefiles "wikipedia:Make (software)") contain the instructions to build packages, and these are sometimes generated with [Autotools](https://wiki.gentoo.org/wiki/Autotools "Autotools").

The [make] utility is [specified by](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/make.html#tag_20_76) [POSIX](https://wiki.gentoo.org/wiki/POSIX "POSIX"). Gentoo\'s default [make] implementation is [GNU Make](https://www.gnu.org/software/make/), [[[dev-build/make]](https://packages.gentoo.org/packages/dev-build/make)[]] (often called *gmake*), installed as part of the \@system set. However, the main Gentoo repository also provides [bmake](http://www.crufty.net/help/sjg/bmake.html), [[[dev-build/bmake]](https://packages.gentoo.org/packages/dev-build/bmake)[]], derived from NetBSD\'s [make].

## [Invocation]

[The emake function should be used to call **make**.](https://devmanual.gentoo.org/ebuild-writing/functions/src_compile/building/)

[CODE] **Example of using emake in an ebuild**

    src_compile()

## [See also]

-   [Autotools](https://wiki.gentoo.org/wiki/Autotools "Autotools") --- a build system often used for open source projects.
-   [Build automation](https://wiki.gentoo.org/wiki/Build_automation "Build automation") --- software that automates the compilation, clean up, and installation stages of the software creation process.

## [External resources]

-   [[man 5 ebuild](https://dev.gentoo.org/~zmedico/portage/doc/man/ebuild.5.html)] - See the section **emake \[make options\]**