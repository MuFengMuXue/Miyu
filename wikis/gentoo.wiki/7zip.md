[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=7-Zip&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

*Not to be confused with [p7zip](https://wiki.gentoo.org/wiki/P7zip "P7zip").*

**Resources**

[[]][Home](https://www.7-zip.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/7-Zip "wikipedia:7-Zip")

**7-Zip** is a file [archiver](https://wiki.gentoo.org/wiki/Data_compression "Data compression").

** Important**\
The 7-zip archive format does **not** store standard Unix file permissions such as owner/group or extended file attributes.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Extraction]](#Extraction)
    -   [[2.2] [Archiving]](#Archiving)
        -   [[2.2.1] [Making a password-protected archive]](#Making_a_password-protected_archive)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [app-arch/7zip](https://packages.gentoo.org/packages/app-arch/7zip) [[]] [Free file archiver for extremely high compression]

  ------------------------------------------------------------- ---------------------------------------------------------------------
  [`+symlink`](https://packages.gentoo.org/useflags/+symlink)   Install additional symlink to 7z, 7za and 7zr
  [`jwasm`](https://packages.gentoo.org/useflags/jwasm)         Use dev-lang/jwasm to include optimized code (doesn\'t support AES)
  [`rar`](https://packages.gentoo.org/useflags/rar)             Enable support for non-free rar decoder
  [`uasm`](https://packages.gentoo.org/useflags/uasm)           Use dev-lang/uasm to include optimized code
  ------------------------------------------------------------- ---------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-28 16:28] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

7-Zip can be installed by running:

`root `[`#`]`emerge --ask app-arch/7zip`

## [Usage]

### [Extraction]

To extract all files from an archive, use either `e` or `x` in the following command:

`user `[`$`]`7zz <e/x> <archive name>`

In the above command, `e` will simply just **e**xtract the archive, while `x` will e**x**tract the archive, but with full paths.

### [Archiving]

To add files and/or folders to an archive, use the following command:

`user `[`$`]`7zz a <folder/file(s) name(s)>`

#### [Making a password-protected archive]

** Warning**\
The [7zip man-page](https://linux.die.net/man/1/7z) **STRONGLY** advises against using 7-zip for back-up purposes due to the fact that owner/group permissions are **NOT** stored.

A password-protected archive can be created using the following flags:

-   `-p` : Prompt\'s the user for a password

Optionally, archive header encryption can also be enabled using `-mhe=on`, which forces the `7z` format to be used.

## [See also]

-   [Data compression](https://wiki.gentoo.org/wiki/Data_compression "Data compression") --- a list of some of the **compression and file-archiver utilities** available in Gentoo Linux
-   [P7zip](https://wiki.gentoo.org/wiki/P7zip "P7zip") --- a command-line port of [7-Zip](https://www.7-zip.org/) for POSIX compliant systems such as Unix, macOS, BeOS, and Amiga.
-   [Tar](https://wiki.gentoo.org/wiki/Tar "Tar") --- an [archiver](https://wiki.gentoo.org/wiki/Data_compression "Data compression") tool that provides the ability to create tar archives, as well as various other kinds of manipulation.
-   [Zip](https://wiki.gentoo.org/wiki/Zip "Zip") --- provides classic ZIP [compression](https://wiki.gentoo.org/wiki/Data_compression "Data compression")

## [External resources]

[https://linux.die.net/man/1/7z](https://linux.die.net/man/1/7z) - 7-zip Linux man-page