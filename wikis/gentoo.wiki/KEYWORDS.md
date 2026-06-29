This page contains [[changes](https://wiki.gentoo.org/index.php?title=KEYWORDS&oldid=1406267&diff=1423320)] which are not marked for translation.

Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/KEYWORDS/hu "KEYWORDS (83% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/KEYWORDS/zh-cn "KEYWORDS (33% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/KEYWORDS/ja "KEYWORDS (100% translated)")

** See also**\
This article is for anyone working on [ebuilds](https://wiki.gentoo.org/wiki/Ebuild "Ebuild"). Most users may want to refer to other articles, such as [accepting a keyword for a single package](https://wiki.gentoo.org/wiki/Knowledge_Base:Accepting_a_keyword_for_a_single_package "Knowledge Base:Accepting a keyword for a single package").

In an ebuild the `KEYWORDS` variable informs in which [architectures](https://wiki.gentoo.org/wiki/Handbook:Main_Page#Architectures "Handbook:Main Page") the ebuild is stable or still in testing phase.

## Contents

-   [[1] [Some possible values for KEYWORDS]](#Some_possible_values_for_KEYWORDS)
    -   [[1.1] [Prefix keywords]](#Prefix_keywords)
    -   [[1.2] [Special keywords]](#Special_keywords)
    -   [[1.3] [Using more than one keyword]](#Using_more_than_one_keyword)
-   [[2] [Using a package that is released for another architecture only]](#Using_a_package_that_is_released_for_another_architecture_only)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Some possible values for KEYWORDS]

The following box contains some example values for the `KEYWORDS` variable:

[FILE] **`example.ebuild`**

    KEYWORDS="alpha amd64 arm arm64 hppa m68k ~mips ppc ppc64 s390 sparc x86"

See the [/var/db/repos/gentoo/profiles/arch.list] for a list of keywords.

The prefix `~` (a tilde character) placed in front of various architectures in the example above means that architecture is in a \"testing phase\" and is not ready for production usage.

### [Prefix keywords]

Gentoo Linux keywords consist only of `$ARCH` (ex. `arm64`). However portage can be used on different operating systems due to the [Prefix Project](https://wiki.gentoo.org/wiki/Project:Prefix "Project:Prefix").

Keywords used by prefix have an operating system suffix, like `~arm64-`**`macos`** or `amd64-`**`linux`**. These keywords would mean that that ebuild package is testing on arm64 MacOS and stable on amd64 Linux **for prefix**.

Usual keyword rules apply to prefix keywords (ex. only arch team can add them).

### [Special keywords]

In addition to the normal `KEYWORDS` values Portage supports three special tokens:

-   `*` - Package is visible if it is stable on any architecture.
-   `~*` - Package is visible if it is in testing on any architecture.
-   `**` - Package is always visible (`KEYWORDS` are ignored completely).

** Note**\
The behavior of \~*arch* and \~\* differ: \~*arch* includes *arch*, \~\* doesn\'t include \*. To use the most recent version of a package which is marked stable or unstable on any architecture, specify \"\* \~\*\".

### [Using more than one keyword]

To use a recent version which is marked stable or unstable on any arch use:

[FILE] **`/etc/portage/package.accept_keywords`**

    app-text/fdftk * ~*

To use a recent version which is marked unstable on your architecture or stable on any arch use:

[FILE] **`/etc/portage/package.accept_keywords`**

    app-text/fdftk ~''arch'' *

## [Using a package that is released for another architecture only]

When the `-*` KEYWORD is specified, this indicates that the package is known to be broken on all systems which are not otherwise listed in KEYWORDS. For example, a binary only package which is built for the **[x86]** will look like:

`user `[`$`]`equery meta fdftk`

     * app-text/fdftk [gentoo]
    Maintainer:  robbat2@gentoo.org
    Maintainer:  tex@gentoo.org (Gentoo TeX Project)
    Upstream:    None specified
    Homepage:    http://www.adobe.com/devnet/acrobat/fdftoolkit.html
    Location:    /var/portage/repos/gentoo/app-text/fdftk
    Keywords:    6.0-r1:0: x86 -*
    License:     Adobe

To accept this package on a **[amd64]** system anyways, then use one of the other keywords in the [package.accept_keywords] like this:

[FILE] **`/etc/portage/package.accept_keywords`**

    app-text/fdftk x86

For detailed information see the [[[portage(5)]](https://man.archlinux.org/man/portage.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")](5) man page.

## [See also]

-   [ACCEPT_KEYWORDS](https://wiki.gentoo.org/wiki/ACCEPT_KEYWORDS "ACCEPT KEYWORDS")
-   [Knowledge Base:Accepting a keyword for a single package](https://wiki.gentoo.org/wiki/Knowledge_Base:Accepting_a_keyword_for_a_single_package "Knowledge Base:Accepting a keyword for a single package")
-   [Knowledge Base:Accepting a keyword for all packages](https://wiki.gentoo.org/wiki/Knowledge_Base:Accepting_a_keyword_for_all_packages "Knowledge Base:Accepting a keyword for all packages")
-   [Stable request](https://wiki.gentoo.org/wiki/Stable_request "Stable request") --- the procedure for moving an ebuild from testing to stable.
-   [Package testing](https://wiki.gentoo.org/wiki/Package_testing "Package testing") --- provides information for ebuild developers on **testing ebuilds**.
-   [/etc/portage/package.accept_keywords](https://wiki.gentoo.org/wiki//etc/portage/package.accept_keywords "/etc/portage/package.accept keywords") --- files or directories of files containing definitions for per-package `ACCEPT_KEYWORDS` statements.
-   [equery ke(y)words](https://wiki.gentoo.org/wiki/Equery#Capabilities "Equery") --- display keywords for specified PKG.

## [External resources]

-   [Gentoo Development Guide: Keywording](https://devmanual.gentoo.org/keywording/)
-   [https://github.com/mgorny/nattka/#filing-keywordingstabilization-bugs](https://github.com/mgorny/nattka/#filing-keywordingstabilization-bugs)