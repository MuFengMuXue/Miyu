Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/DISTDIR/de "DISTDIR (88% translated)")
-   [English]
-   [Türkçe](https://wiki.gentoo.org/wiki/DISTDIR/tr "DISTDIR (6% translated)")
-   [español](https://wiki.gentoo.org/wiki/DISTDIR/es "DISTDIR (18% translated)")
-   [français](https://wiki.gentoo.org/wiki/DISTDIR/fr "DISTDIR (88% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/DISTDIR/it "DISTDIR (12% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/DISTDIR/hu "DISTDIR (88% translated)")
-   [русский](https://wiki.gentoo.org/wiki/DISTDIR/ru "DISTDIR (100% translated)")
-   [українська](https://wiki.gentoo.org/wiki/DISTDIR/uk "DISTDIR (6% translated)")
-   [தமிழ்](https://wiki.gentoo.org/wiki/DISTDIR/ta "DISTDIR/ta (18% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/DISTDIR/zh-cn "DISTDIR (35% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/DISTDIR/ja "DISTDIR (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/DISTDIR/ko "DISTDIR (47% translated)")

The `DISTDIR` variable defines the location where Portage will store the downloaded source code archives. Its value defaults to [[/var/cache/distfiles](https://wiki.gentoo.org/wiki//var/cache/distfiles "/var/cache/distfiles")] on new installations. Previously the default was [\$/distfiles] which resolved to [/usr/portage/distfiles] by default.

This location, which is also often referred to as the *distfiles* location, will host the source code archives of all software installed (or attempted to install) on the system. This location is not automatically cleaned up, so users should consider using tools such as the [eclean-dist] command (which comes as part of the [[[app-portage/gentoolkit]](https://packages.gentoo.org/packages/app-portage/gentoolkit)[]] package) to keep the storage used by this location under control. Read the [Eclean article](https://wiki.gentoo.org/wiki/Eclean "Eclean") for more details.

Users can set the `DISTDIR` variable in [[/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")]:

** Warning**\
**Only trusted users should be granted write access to `DISTDIR`\'s location**.

\

File integrity check and unpacking is a [non-atomic](https://bugs.gentoo.org/915330) operation, allowing for an attack where a file is swapped in between, possibly leading to compromise the system.

[FILE] **`/etc/portage/make.conf`Using a different DISTDIR location**

    DISTDIR=/var/gentoo/distfiles

## [[] Source of archives]

To download source code archives, Portage will download files from servers defined in the [`GENTOO_MIRRORS`](https://wiki.gentoo.org/wiki/GENTOO_MIRRORS "GENTOO MIRRORS") variable first (to alleviate load on upstream project resources and for other reasons). The `SRC_URI` variable in individual [ebuilds](https://wiki.gentoo.org/wiki/Ebuild "Ebuild"), points to the package\'s original source files, which is originally downloaded by the ebuild maintainers during ebuild creation and development.

Part of ebuild development is the creation of [[Manifest](https://wiki.gentoo.org/wiki/Repository_format/package/Manifest "Repository format/package/Manifest")] files, which ensure the upstream source files are not modified from the time they are downloaded by the ebuild developer, distributed to Gentoo\'s mirror system, then to their destination on the endpoint system.

### [[] Bypassing Gentoo mirrors]

** Warning**\
Over time, upstream projects who host package source files will move their project\'s source URLs to new locations. In some instances, upstream projects will discontinue development, which eventually leads to the inability to obtain software sources from upstream locations.\
\
Due to the Gentoo mirroring system, ebuild maintainers can still \'support\' ebuilds with deprecated upstream sources. This allows software to be gracefully phased out of the ::gentoo ebuild repository, which is part of a good [user experience](https://en.wikipedia.org/wiki/User_experience "wikipedia:User experience") for the Gentoo community. For these reasons and others, **users who choose to bypass the Gentoo mirror system should expect unreliable downloads for source files**.

To download the source archives bypassing Gentoo mirrors, set the `GENTOO_MIRRORS` variable to an empty value from the command-line. For example:

`root `[`#`]`GENTOO_MIRRORS="" emerge --ask www-client/firefox`

## [[] See also]

-   [Local distfiles cache](https://wiki.gentoo.org/wiki/Local_distfiles_cache "Local distfiles cache") --- details some approaches to setting up a local distfiles cache which will save bandwidth when several machines are running Gentoo on the same local area network.
-   [PKGDIR](https://wiki.gentoo.org/wiki/PKGDIR "PKGDIR") --- is the location [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") keeps binary packages.
-   [Knowledge Base: Remove obsoleted distfiles](https://wiki.gentoo.org/wiki/Knowledge_Base:Remove_obsoleted_distfiles "Knowledge Base:Remove obsoleted distfiles")
-   [Eclean](https://wiki.gentoo.org/wiki/Eclean "Eclean") --- a tool for cleaning repository source files and binary packages.