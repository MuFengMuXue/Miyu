**[] Archived article**\
\
This article is **archived (obsolete)**. Contents are surely incorrect for current usage, and are intended for historical reference only.

Masked and set for removal in Gentoo. Unreliable software, unmaintained in Gentoo. Having it in the main repositories may give users an impression of it being a safe tool. Removal on 2024-09-01.

\
TLDR: **Do not use this article!**

**Resources**

[[]][Home](https://github.com/TheChymera/mkstage4)

[[]][Package information](https://packages.gentoo.org/packages/app-backup/mkstage4)

**mkstage4** is a script to create stage 4 files. [** This script was slated for removal from the [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository") for being unreliable, unmaintained in Gentoo, and potentially unsafe.**]

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
-   [[3] [Invocation]](#Invocation)
-   [[4] [See also]](#See_also)
-   [[5] [External references]](#External_references)

## [Installation]

To install mkstage4, the [[[app-backup/mkstage4]](https://packages.gentoo.org/packages/app-backup/mkstage4)[]] package may need unmasking. This may not apply for all systems depending on prior-use and configuration.

To unmask, add the following to a file:

[FILE] **`/etc/portage/package.accept_keywords/mkstage4`How to unmask the mkstage4 package**

    app-backup/mkstage4 ~amd64

### [Emerge]

Install with the following command:

`root `[`#`]`emerge --ask app-backup/mkstage4`

## [Usage]

To produce a stage 4 archive of the current system using mkstage4:

`root `[`#`]`mkstage4 -s <name>`

This will create a Stage 4 archive of all files under [/] (current root partition). Similarly, to specify a different location to make a Stage 4 archive of:

`root `[`#`]`mkstage4 -t /custom/mount/point <name>`

If using a smaller storage device, or just wish to not fill up internal storage, specify writing the stage 4 tarball to a different partition/drive using:

`root `[`#`]`cd <destination directory> `

`root `[`#`]` mkstage4 -s <name>`

This will write the Stage 4 archive to the destination directory.

## [Invocation]

`root `[`#`]`mkstage4 -h`

    Usage:
        mkstage4 [-b -c -k -l -q] [-C <compression-type>] [-s || -t <target-mountpoint>] [-e <additional excludes dir*>] [-i <additional include target>] <archive-filename> [custom-tar-options]
        -b: excludes boot directory.
        -c: excludes some confidential files (currently only .bash_history and connman network lists).
        -k: separately save current kernel modules and src (creates smaller archives and saves decompression time).
        -l: excludes lost+found directory.
        -q: activates quiet mode (no confirmation).
        -C: specify tar compression (default: bz2, available: xz bz2 zst gz).
        -s: makes tarball of current system.
        -t: makes tarball of system located at the <target-mountpoint>.
        -e: an additional excludes directory (one dir one -e, do not use it with *).
        -i: an additional target to include. This has higher precedence than -e, -t, and -s.
        -h: displays help message.

## [See also]

-   [Stage file](https://wiki.gentoo.org/wiki/Stage_file "Stage file") --- an archive that contains all the files to run a minimal Gentoo environment, typically to serve as a seed for a Gentoo installation

## [External references]

-   [GitHub repository](https://github.com/TheChymera/mkstage4) - For more information on advanced and further use of mkstage4
-   [Stage 4 Tarballs Made Easy](https://www.tutorials.chymera.eu/blog/2014/05/18/mkstage4-stage4-tarballs-made-easy/) - blog post on usage