[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Cpio&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Package information](https://packages.gentoo.org/packages/app-alternatives/cpio)

[[]][Wikipedia](https://en.wikipedia.org/wiki/cpio "wikipedia:cpio")

[[]][Man page](http://man7.org/linux/man-pages/man1/cpio.1.html)

**cpio** is a file [archiving](https://wiki.gentoo.org/wiki/Data_compression "Data compression") utility. It utilises a file format of the same name, [[[cpio(5)]](https://man.archlinux.org/man/cpio.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")].

By default, Gentoo uses [GNU cpio](https://www.gnu.org/software/cpio/) ([gcpio]) as its cpio implementation. However, [[[app-arch/libarchive]](https://packages.gentoo.org/packages/app-arch/libarchive)[]] provides an alternative implementation, [bsdcpio].

** Note**\
Since 2001, [[[cpio(1)]](https://man.archlinux.org/man/cpio.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] is no longer a [POSIX](https://wiki.gentoo.org/wiki/POSIX "POSIX") utility; its POSIX replacement is [pax](https://wiki.gentoo.org/wiki/Pax "Pax").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Removal]](#Removal)
    -   [[2.1] [Unmerge]](#Unmerge)
-   [[3] [See also]](#See_also)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask app-alternatives/cpio`

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-alternatives/cpio`

## [See also]

-   [Data compression](https://wiki.gentoo.org/wiki/Data_compression "Data compression") --- a list of some of the **compression and file-archiver utilities** available in Gentoo Linux
-   [pax](https://wiki.gentoo.org/wiki/Pax "Pax") --- a file [archiving utility](https://wiki.gentoo.org/wiki/Data_compression "Data compression") specified by [POSIX](https://wiki.gentoo.org/wiki/POSIX "POSIX"), intended to replace the [cpio] utility
-   [Tar](https://wiki.gentoo.org/wiki/Tar "Tar") --- an [archiver](https://wiki.gentoo.org/wiki/Data_compression "Data compression") tool that provides the ability to create tar archives, as well as various other kinds of manipulation.