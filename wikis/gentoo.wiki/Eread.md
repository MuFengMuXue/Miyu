Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Gentoolkit/de "Gentoolkit (53% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/Gentoolkit/es "Gentoolkit (25% translated)")
-   [français](https://wiki.gentoo.org/wiki/Gentoolkit/fr "Gentoolkit (34% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Gentoolkit/hu "Gentoolkit (96% translated)")
-   [português do Brasil](https://wiki.gentoo.org/wiki/Gentoolkit/pt-br "Gentoolkit (55% translated)")
-   [svenska](https://wiki.gentoo.org/wiki/Gentoolkit/sv "Gentoolkit (8% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Gentoolkit/ru "gentoolkit (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Gentoolkit/zh-cn "Gentoolkit (28% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Gentoolkit/ja "Gentoolkit (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Gentoolkit/ko "Gentoolkit/ko (21% translated)")

**[Portage - the heart of Gentoo](https://wiki.gentoo.org/wiki/Portage "Portage")**\
[emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge") --- [configuration](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf") --- [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") --- [dispatch-conf](https://wiki.gentoo.org/wiki/Dispatch-conf "Dispatch-conf")\
[\
[world file](https://wiki.gentoo.org/wiki/Selected-packages_set_(Portage) "Selected-packages set (Portage)") --- [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag") --- [ebuilds](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") --- [profiles](https://wiki.gentoo.org/wiki/Portage/Profiles "Portage/Profiles")\
[upgrades](https://wiki.gentoo.org/wiki/Upgrading_Gentoo "Upgrading Gentoo") --- [using testing packages](https://wiki.gentoo.org/wiki/Knowledge_Base:Accepting_a_keyword_for_a_single_package "Knowledge Base:Accepting a keyword for a single package") --- [Gentoo binhost](https://wiki.gentoo.org/wiki/Gentoo_Binary_Host_Quickstart "Gentoo Binary Host Quickstart")\
[tools](https://wiki.gentoo.org/wiki/Useful_Portage_tools "Useful Portage tools") --- [gentoolkit] --- [eselect](https://wiki.gentoo.org/wiki/Eselect "Eselect")\
[Portage FAQ](https://wiki.gentoo.org/wiki/Project:Portage/FAQ "Project:Portage/FAQ") --- [cheat sheet](https://wiki.gentoo.org/wiki/Gentoo_Cheat_Sheet "Gentoo Cheat Sheet") --- [FAQ](https://wiki.gentoo.org/wiki/FAQ "FAQ")\
[all articles](https://wiki.gentoo.org/wiki/Category:Portage "Category:Portage")\
]

*Not to be confused with [Genkernel](https://wiki.gentoo.org/wiki/Genkernel "Genkernel").*

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Portage-Tools "Project:Portage-Tools")][Project](https://wiki.gentoo.org/wiki/Project:Portage-Tools "Project:Portage-Tools")

[[]][Package information](https://packages.gentoo.org/packages/app-portage/gentoolkit)

[[]][GitWeb](https://gitweb.gentoo.org/proj/gentoolkit.git/)

[[]][Bugs (upstream)](https://bugs.gentoo.org/)

**gentoolkit** is a suite of tools to ease the administration of a Gentoo system, and [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") in particular.

Gentoo is a very unique distribution, with certain specifics that are not present in other systems. Several tools developed to help with Gentoo usage have been contributed, and are grouped in the [[[app-portage/gentoolkit]](https://packages.gentoo.org/packages/app-portage/gentoolkit)[]] package.

[gentoolkit] contains tools to help users manage packages and keep track of what is going on in their systems. Most users - particularly those who update systems often - will benefit from having gentoolkit installed.

The gentoolkit commands have [man pages](https://wiki.gentoo.org/wiki/Man_page "Man page"), type [man \<command\>] for each command for full documentation.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [eclean]](#eclean)
-   [[3] [equery]](#equery)
    -   [[3.1] [epkginfo]](#epkginfo)
    -   [[3.2] [eshowkw]](#eshowkw)
-   [[4] [eread]](#eread)
-   [[5] [euse]](#euse)
-   [[6] [revdep-rebuild]](#revdep-rebuild)
-   [[7] [Other tools]](#Other_tools)
-   [[8] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [app-portage/gentoolkit](https://packages.gentoo.org/packages/app-portage/gentoolkit) [[]] [Collection of administration scripts for Gentoo]

  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`test`](https://packages.gentoo.org/useflags/test)   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-25 04:06] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install gentoolkit:

`root `[`#`]`emerge --ask app-portage/gentoolkit`

## [eclean]

**[eclean](https://wiki.gentoo.org/wiki/Eclean "Eclean")** is a tool to remove old source files and old binary packages from the system.

When building and installing packages, the source files are downloaded and preserved in `DISTDIR`, usually [/var/cache/distfiles]. This can accumulate several gigabytes of material over time if it is not cleaned periodically. Users should run [eclean-dist] to clean source files from `DISTDIR`.

It is possible to create archives of installed packages by using [quickpkg] or `FEATURES="buildpkg"`. These archived packages are kept in `PKGDIR`, usually [/var/cache/binpkgs]. When they are no longer needed, or if they are too old, [eclean-pkg] can be run to remove them from `PKGDIR`. It is a good way to ensure that any binary packages on the system are only the latest versions.

For more information on [eclean] and tips on maintaining a cruft-free system, please read [man eclean] or check the [eclean](https://wiki.gentoo.org/wiki/Eclean "Eclean") article.

## [equery]

**[equery](https://wiki.gentoo.org/wiki/Equery "Equery")** is a tool designed to make asking portage for information easier. Among other operations, it can display package dependencies, metadata, and installed files.

### [epkginfo]

**[epkginfo](https://wiki.gentoo.org/wiki/Epkginfo "Epkginfo")** is an alias for [equery meta] command.

### [eshowkw]

**eshowkw** is an alias for [equery keywords] command.

## [eread]

[eread] is a simple utility to display elog files produced by Portage since version 2.1. The saving of elog files can be enabled by setting a couple of variables in [/etc/portage/make.conf]:

[FILE] **`make.conf`Enabling elog**

    PORTAGE_ELOG_CLASSES="log"
    PORTAGE_ELOG_SYSTEM="save"

** Note**\
This is only one way of saving elog messages. For more information on how Portage\'s elog system works, please refer to the appropriate page in the [Portage Handbook](https://wiki.gentoo.org/wiki/Handbook:X86/Portage/Files#Logging_features "Handbook:X86/Portage/Files").

Once elog has been set up to satisfaction, run [eread] to view the log files.

`user `[`$`]`eread`

    This is a list of portage log items. Choose a number to view that file or type
    q to quit.

    1) app-portage:gentoolkit-0.2.4_pre2:20070320-000256.log
    2) app-portage:gentoolkit-0.2.4_pre2:20070320-000258.log
    3) app-portage:gentoolkit-0.2.4_pre2:20070320-000319.log
    4) app-portage:gentoolkit-0.2.3:20070320-000408.log
    Choice?

Select a number and the file will be displayed using the paging program specified in the `PAGER` environment variable. If `PAGER` is not set, it will use [less]. The `PAGER` environmental variable can be set using [eselect] (module `pager`).

After displaying the elog item, the user will be prompted to delete the file.

## [euse]

**[euse](https://wiki.gentoo.org/wiki/Euse "Euse")** provides functionality to set (disable/enable) and obtain information about [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag") in [make.conf](https://wiki.gentoo.org/wiki/Make.conf "Make.conf"), without having to edit the file directly.

## [revdep-rebuild]

** Important**\
It is not necessary to run this tool for general use. The portage [FEATURE](https://wiki.gentoo.org/wiki/FEATURES "FEATURES") preserve-libs makes the original purpose obsolete. The primary purpose of this tool is now [ABI](https://wiki.gentoo.org/wiki/ABI "ABI") changes for specific libraries when instructions are provided by developers.

This tool is Gentoo\'s **rev**erse **dep**endency rebuilder. It will scan the installed ebuilds to find packages that have become broken as a result of an upgrade of a package they depend on. It can emerge those packages for users automatically but it can also happen that a given package does not work with the currently installed dependencies, in which case the broken package should be upgraded to a more recent version.

[revdep-rebuild] will pass flags to [emerge] which lets the `--pretend` flag pass through, to see what is going to be emerged again before going any further.

`user `[`$`]`revdep-rebuild -p`

     * Configuring search environment for revdep-rebuild

     * Checking reverse dependencies
     * Packages containing binaries and libraries broken by a package update
     * will be emerged.

     * Collecting system binaries and libraries
     * Generated new 1_files.rr
     * Collecting complete LD_LIBRARY_PATH
     * Generated new 2_ldpath.rr
     * Checking dynamic linking consistency
    [ 48% ]  *   broken /usr/lib/gstreamer-0.10/libgsttaglib.la (requires /usr/lib/libtag.la)
    [ 64% ]  *   broken /usr/lib/libgdkglext-x11-1.0.la (requires /usr/lib/libGLU.la)
    [ 67% ]  *   broken /usr/lib/libgtkglext-x11-1.0.la (requires /usr/lib/libGLU.la)
    [ 85% ]  *   broken /usr/lib/python2.6/site-packages/gtk-2.0/gtk/gdkgl/_gdkgl.la (requires /usr/lib/libGLU.la)
     *   broken /usr/lib/python2.6/site-packages/gtk-2.0/gtk/gtkgl/_gtkgl.la (requires /usr/lib/libGLU.la)
    [ 97% ]  *   broken /usr/qt/3/lib/libqt-mt.la (requires -lpng)
    [ 100% ]
     * Generated new 3_broken.rr
     * Assigning files to packages
     *   /usr/lib/gstreamer-0.10/libgsttaglib.la -> media-plugins/gst-plugins-taglib
     *   /usr/lib/libgdkglext-x11-1.0.la -> x11-libs/gtkglext
     *   /usr/lib/libgtkglext-x11-1.0.la -> x11-libs/gtkglext
     *   /usr/lib/python2.6/site-packages/gtk-2.0/gtk/gdkgl/_gdkgl.la -> dev-python/pygtkglext
     *   /usr/lib/python2.6/site-packages/gtk-2.0/gtk/gtkgl/_gtkgl.la -> dev-python/pygtkglext
     *   /usr/qt/3/lib/libqt-mt.la -> x11-libs/qt
     * Generated new 4_raw.rr and 4_owners.rr
     * Cleaning list of packages to rebuild
     * Generated new 4_pkgs.rr
     * Assigning packages to ebuilds
     * Generated new 4_ebuilds.rr
     * Evaluating package order
     * Generated new 5_order.rr
     * All prepared. Starting rebuild
    emerge --oneshot --pretend  dev-python/pygtkglext:0
    media-plugins/gst-plugins-taglib:0.10
    x11-libs/gtkglext:0
    x11-libs/qt:3

    These are the packages that would be merged, in order:

    Calculating dependencies... done!
    [ebuild   R   ] media-plugins/gst-plugins-taglib-0.10.17
    [ebuild   R   ] x11-libs/gtkglext-1.2.0
    [ebuild   R   ] x11-libs/qt-3.3.8b-r2
    [ebuild   R   ] dev-python/pygtkglext-1.1.0
     * Now you can remove -p (or --pretend) from arguments and re-run revdep-rebuild.

To rebuild some packages run [revdep-rebuild] without the `-p` flag and the listed packages will be emerged again.

`root `[`#`]`revdep-rebuild`

## [Other tools]

gentoolkit also provides other tools:

  ------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                                                                                                   Description
  [ebump]     Ebuild revision bumper (more useful for developers).
  [enalyze]   Gentoo\'s installed packages analysis and repair tool. See man page, which states \"CAUTION: This is beta software and is not yet feature complete\".
  [imlate]    Displays candidates for keywords for an architecture (more useful for developers?).
  ------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------

See the [man pages](https://wiki.gentoo.org/wiki/Man_page "Man page") for each of these tools for more info.

## [See also]

-   [Q applets](https://wiki.gentoo.org/wiki/Q_applets "Q applets") --- a collection of small, fast [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") **q**uery utilities written in C.
-   [Useful Portage tools](https://wiki.gentoo.org/wiki/Useful_Portage_tools "Useful Portage tools") --- provides a list of Gentoo-specific system management tools, notably for [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), available in the [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository").

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Matt Butcher, John P. Davis, Erwin, Shyam Mani, Xavier Neys, Karl Trygve, José Luis Rivero, Joshua Saddler, Douglas Anderson**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*