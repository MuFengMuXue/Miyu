[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Pax&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Package information](https://packages.gentoo.org/packages/app-arch/pax)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Pax_(command) "wikipedia:Pax (command)")

[[]][Man page](http://man7.org/linux/man-pages/man1/pax.1.html)

*Not to be confused with [PaX, a patch to harden the Linux kernel](https://wiki.gentoo.org/wiki/Hardened/PaX_Quickstart "Hardened/PaX Quickstart").*

**pax** is a file [archiving utility](https://wiki.gentoo.org/wiki/Data_compression "Data compression") specified by [POSIX](https://wiki.gentoo.org/wiki/POSIX "POSIX"), intended to replace the [cpio](https://wiki.gentoo.org/wiki/Cpio "Cpio") utility^[\[1\]](#cite_note-1)^. It was first specified in POSIX-1.2001/2004.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Removal]](#Removal)
    -   [[2.1] [Unmerge]](#Unmerge)
-   [[3] [See also]](#See_also)
-   [[4] [References]](#References)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask app-arch/pax`

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-arch/pax`

## [See also]

-   [Data compression](https://wiki.gentoo.org/wiki/Data_compression "Data compression") --- a list of some of the **compression and file-archiver utilities** available in Gentoo Linux
-   [cpio](https://wiki.gentoo.org/wiki/Cpio "Cpio") --- a file [archiving](https://wiki.gentoo.org/wiki/Data_compression "Data compression") utility
-   [POSIX](https://wiki.gentoo.org/wiki/POSIX "POSIX") --- a collection of standards for Unix-like operating systems

## [References]

1.  [[[↑](#cite_ref-1)] [[POSIX-1.2001/2004, \"pax\", \"Rationale\"](https://pubs.opengroup.org/onlinepubs/009695399/utilities/pax.html#tag_04_100_18). Retrieved on 2025-02-04.]]