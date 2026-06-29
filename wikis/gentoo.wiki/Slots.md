The **`SLOT`** [[ebuild]](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") variable specifies a package version\'s **slot**. Slots can allow multiple versions of a package to be installed and managed simultaneously by Portage.

## Contents

-   [[1] [Version specifiers]](#Version_specifiers)
-   [[2] [Behavior]](#Behavior)
-   [[3] [How different packages use slotting]](#How_different_packages_use_slotting)
-   [[4] [Listing package slots with eix]](#Listing_package_slots_with_eix)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Version specifiers]

Slotted versions are denoted by adding a colon (`:`) plus the slot name after the package version. For example, slot 3 of [x11-libs/gtk+-3.24.39::gentoo] can be specified using [x11-libs/gtk+-3.24.39:3::gentoo].

## [Behavior]

Every package version has one slot. Versions in different slots can be installed simultaneously. For example, to install [[[sys-kernel/gentoo-kernel-6.6.21:**6.6.21**]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel)[]] alongside [[[sys-kernel/gentoo-kernel-6.1.81:**6.1.81**]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel)[]], the following command can be used:

`root `[`#`]`emerge --ask gentoo-kernel:6.6.21 gentoo-kernel:6.1.81`

This installs [[[sys-kernel/gentoo-kernel-6.6.21]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel)[]] into slot [6.6.21] and [[[sys-kernel/gentoo-kernel-6.1.81]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel)[]] into slot [6.1.81]:

`user `[`$`]`eselect kernel list`

    Available kernel symlink targets:
      [1]   linux-6.1.81-gentoo *
      [2]   linux-6.6.21-gentoo

A package version can only be installed into its own slot. Thus, [[[sys-kernel/gentoo-kernel-6.1.81]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel)[]] cannot be installed into slot [6.6.21], [6], or [foo].

## [How different packages use slotting]

Most packages don\'t use slots.

As can be inferred from section [Behavior](#Behavior), [[[sys-kernel/gentoo-kernel]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel)[]] uses a different slot for each version. Some packages, such as [[[sys-devel/gcc]](https://packages.gentoo.org/packages/sys-devel/gcc)[]], use different slots for different *major revisions* --- [[[sys-devel/gcc-13.2.1_p20240210:**13**]](https://packages.gentoo.org/packages/sys-devel/gcc)[]] can be installed alongside [[[sys-devel/gcc-14.0.1_pre20240317:**14**]](https://packages.gentoo.org/packages/sys-devel/gcc)[]], but not alongside [[[sys-devel/gcc-13.2.1_p20240113-r1:**13**]](https://packages.gentoo.org/packages/sys-devel/gcc)[]].

In general, if two package versions own a few of the same files, they cannot be installed simultaneously, so they are placed in the same slot. Packages such as [[[sys-kernel/gentoo-kernel]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel)[]] and [[[sys-devel/gcc]](https://packages.gentoo.org/packages/sys-devel/gcc)[]] incorporate the slot into the installed filenames (e.g. [/boot/kernel-6.8.6-gentoo-dist] and [/usr/x86_64-pc-linux-gnu/gcc-bin/13/gcc]), eliminating conflicts between slots.

## [Listing package slots with [eix]]

[eix] (from the [[[app-portage/eix]](https://packages.gentoo.org/packages/app-portage/eix)[]] package) can be used to list a single package\'s slotted versions.

Before performing any operations using [eix], update its database:

`user `[`$`]`eix-update`

List the available versions:

`user `[`$`]`eix -e dev-lang/lua `

    [I] dev-lang/lua
         Available versions:
         (5.1)  5.1.5-r200
         (5.3)  5.3.6-r102
         (5.4)  5.4.6

         Installed versions:  5.1.5-r200(5.1)(06:33:41 25/03/2024)(deprecated readline) 5.4.6(5.4)(04:58:26 25/03/2024)(deprecated readline)
         Homepage:            https://www.lua.org/
         Description:         A powerful light-weight programming language designed for extending applications</blockquote>

The slots are shown in parentheses (5.1, 5.3 and 5.4 in this case).

To prevent packages from being installed into certain slots, add them to [[/etc/portage/package.mask](https://wiki.gentoo.org/wiki//etc/portage/package.mask "/etc/portage/package.mask")].

## [See also]

-   [Sub-slots and Slot-Operators](https://wiki.gentoo.org/wiki/Sub-slots_and_Slot-Operators "Sub-slots and Slot-Operators")
-   [Project:Quality Assurance/Subslots](https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Subslots "Project:Quality Assurance/Subslots")

## [External resources]

-   [Slotting](https://devmanual.gentoo.org/general-concepts/slotting/index.html) --- a detailed guide for [ebuild] developers.
-   [Package and Slot Moves](https://devmanual.gentoo.org/ebuild-maintenance/package-moves/#changing-ebuild's-slot) --- how slot moves should be done.