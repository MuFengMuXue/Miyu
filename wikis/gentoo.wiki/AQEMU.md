[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines") (Incomplete article. No instructions about installing package that does not exist in [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository").). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=AQEMU&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://sourceforge.net/projects/aqemu/)

[[]][GitHub](https://github.com/tobimensch/aqemu)

AQEMU is a user-friendly GUI front-end to the [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU") and [KVM](https://wiki.gentoo.org/wiki/KVM "KVM") emulators. The AQEMU front-end is written using the Qt5 framework.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Enabling VM graphical output]](#Enabling_VM_graphical_output)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Installation]

** Warning**\
This package has been removed as of 2022 due to inactivity.

### [USE flags]

Cannot load package information. Is the atom *app-emulation/aqemu* correct?

### [Emerge]

Install [aqemu]:

`root `[`#`]`emerge --ask app-emulation/aqemu`

## [Configuration]

Configuration for AQEMU is a breeze. Simply follow the setup wizard to create a virtual hard drive, then set up a virtual machine.

### [Enabling VM graphical output]

In version 0.8.2-r2 or lower, there is no setting to enable the graphical output from the virtual machines. To have the machine display output to a GTK window an additional option currently not \"supported\" in AQEMU is needed. Presuming a virtual machine has already been created, follow these instructions:

1.  Start AQEMU.
2.  Click the *Advanced* tab.
3.  Under *Additional QEME/KVM Arguments* enter `-display gtk` in the textbox then click *Apply*.
4.  Start the virtual machine. Output should be displayed in a GTK window.

## [See also]

-   [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU") --- a generic, open-source hardware emulator and virtualization suite.

## [External resources]

-   [http://bsdwiki.reedmedia.net/wiki/using_aqemu_for_virtualization.html](http://bsdwiki.reedmedia.net/wiki/using_aqemu_for_virtualization.html)