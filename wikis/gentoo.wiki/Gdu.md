[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Gdu&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[[]][GitHub](https://github.com/dundee/gdu)

**Gdu**, or go DiskUsage(), is a disk usage analyzer written in the [Go](https://wiki.gentoo.org/wiki/Go "Go") programming language.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Scan a directory]](#Scan_a_directory)

## [Installation]

### [Emerge]

Gdu is a package from [GURU](https://wiki.gentoo.org/wiki/GURU "GURU"), to enable the GURU repository:

`root `[`#`]`eselect repository enable guru `

`root `[`#`]`emaint sync -r guru `

`root `[`#`]`emerge --ask sys-fs/gdu`

## [Usage]

### [Scan a directory]

To scan a directory to find the size of the files and directories inside, simply run [gdu] in the desired directory.

`user `[`$`]`gdu /home/larry`