This page contains [[changes](https://wiki.gentoo.org/index.php?title=/etc/portage/package.mask&oldid=1402131&diff=1422124)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki//etc/portage/package.mask/de "/etc/portage/package.mask (100% translated)")
-   [English]
-   [magyar](https://wiki.gentoo.org/wiki//etc/portage/package.mask/hu "/etc/portage/package.mask (25% translated)")
-   [日本語](https://wiki.gentoo.org/wiki//etc/portage/package.mask/ja "/etc/portage/package.mask (100% translated)")

**[/etc/portage/package.mask]** is a file, or a directory of files, controlled by the system administrator that can be used to prevent certain packages from being installed.

## Contents

-   [[1] [Format]](#Format)
-   [[2] [Example]](#Example)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Format]

-   One `DEPEND` atom per line.
-   Anything following a `#` (hash) is treated as a comment, and is ignored.
-   For `DEPEND` atom syntax, see [version specifier](https://wiki.gentoo.org/wiki/Version_specifier "Version specifier").

## [Example]

[FILE] **`/etc/portage/package.mask`package.mask example**

    # Mask versions 1.97 and greater of powertop since they have less features.
    >=sys-power/powertop-1.97

    # Prevent MySQL from being installed by masking the package (use MariaDB)
    dev-db/mysql

    # Want to go without Java 8; mask JDK and JRE that use Java 8.
    virtual/jdk:1.8
    virtual/jre:1.8

Now Portage helpfully explains when packages are masked.

`root `[`#`]`emerge virtual/jdk:1.8`

    Calculating dependencies... done!
    Dependency resolution took 3.47 s (backtrack: 0/20).

    !!! All ebuilds that could satisfy "virtual/jdk:1.8" have been masked.
    !!! One of the following masked packages is required to complete your request:
    - virtual/jdk-1.8.0-r9::gentoo (masked by: package.mask)
    /etc/portage/package.mask:
    # Want to go without Java 8; mask JDK and JRE that use Java 8.

    For more information, see the MASKED PACKAGES section in the emerge
    man page or refer to the Gentoo Handbook.

## [See also]

-   [Knowledge Base:Masking a package](https://wiki.gentoo.org/wiki/Knowledge_Base:Masking_a_package "Knowledge Base:Masking a package")
-   [/etc/portage](https://wiki.gentoo.org/wiki//etc/portage "/etc/portage") --- the primary configuration directory for [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), Gentoo\'s package manager.

## [External resources]

-   [Portage manpage](https://dev.gentoo.org/~zmedico/portage/doc/man/portage.5.html)