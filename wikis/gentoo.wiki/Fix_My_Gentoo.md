This guide has been elaborated in response to repeated posts to the forum by users that \"nothing works\". This article covers rescuing an installation when a chroot is not possible, when almost nothing seems to work but there is a need for certain binary packages to fix the system.

The case where gcc is broken after a `--depclean` isn\'t covered here. [[gcc-config]](https://wiki.gentoo.org/wiki/Upgrading_GCC "Upgrading GCC") is probably what is needed - be more careful [using the `--depclean` option](https://wiki.gentoo.org/wiki/Knowledge_Base:Remove_orphaned_packages "Knowledge Base:Remove orphaned packages") in the future.

It is actually very difficult to break Gentoo so badly that it can\'t be fixed.

## Contents

-   [[1] [Prerequsites]](#Prerequsites)
    -   [[1.1] [Summary]](#Summary)
-   [[2] [Getting started]](#Getting_started)
    -   [[2.1] [Terminology]](#Terminology)
    -   [[2.2] [The rescue install]](#The_rescue_install)
        -   [[2.2.1] [Mounts]](#Mounts)
    -   [[2.3] [Chroot into rescue install]](#Chroot_into_rescue_install)
    -   [[2.4] [Edit /etc/portage/make.conf]](#Edit_.2Fetc.2Fportage.2Fmake.conf)
-   [[3] [Building packages]](#Building_packages)
    -   [[3.1] [Quick package (quickpkg)]](#Quick_package_.28quickpkg.29)
    -   [[3.2] [Emerge]](#Emerge)
        -   [[3.2.1] [More packages]](#More_packages)
-   [[4] [Installing binary packages]](#Installing_binary_packages)
    -   [[4.1] [Using emerge]](#Using_emerge)
    -   [[4.2] [Using qmerge]](#Using_qmerge)
    -   [[4.3] [Using tar]](#Using_tar)
        -   [[4.3.1] [Extracting tar step-by-step method]](#Extracting_tar_step-by-step_method)
            -   [[4.3.1.1] [Sanity checks]](#Sanity_checks)
            -   [[4.3.1.2] [Understanding the tar command]](#Understanding_the_tar_command)
            -   [[4.3.1.3] [Extract]](#Extract)
-   [[5] [Tidying up]](#Tidying_up)
-   [[6] [See also]](#See_also)

## [Prerequsites]

Some binary packages may be necessary to fix the system.

Binary packages may be found on a binhost or tinderbox on the web but they are unlikely to be built for the local system, with corresponding USE flags and CFLAGS.

This guide provides instructions on building binary packages that can be used to repair a system. Neither another system, a spare partition or even another install will be required. All that is needed is:

-   A working internet connection.

<!-- -->

-   A way to boot the broken box with some recovery media, e.g. [SystemRescue](https://www.system-rescue.org/), if it won\'t boot

<!-- -->

-   About 20 GiB of free space on in the broken installation. 5 GiB may do, depending on what needs to be built.

### [Summary]

As the bootable install is not working and a working install is needed to build binary packages, another install is needed (just an extracted stage3 somewhere). This install doesn\'t need to be bootable.

It is sufficient to be able to [chroot] into it and run [emerge]. This rescue install will share some elements with the broken install which saves space and makes things easier in the final steps.

## [Getting started]

### [Terminology]

-   [/mnt/gentoo]: Mount the broken installation here.

<!-- -->

-   [/mnt/gentoo/home/rescue]: The new rescue install, it can be anywhere but it needs to be on a hard disk.

### [The rescue install]

-   Mount the broken install at [/mnt/gentoo] to be able to use its hard drive space and its [/var/db/repos/gentoo].

<!-- -->

-   Make a directory at [/mnt/gentoo/home/rescue] or somewhere with free space:

    :::: cmd-box


    `root `[`#`]`mkdir /mnt/gentoo/home/rescue`


    ::::

<!-- -->

-   Follow the handbook to fetch a stage3 tarball and untar it to [/mnt/gentoo/home/rescue].

<!-- -->

-   Do not get a Portage snapshot, the one in the main install will be utilized.

<!-- -->

-   Follow the [Handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64 "Handbook:AMD64") for all the odds and ends, like copying [/etc/resolv.conf].

#### [Mounts]

** Note**\
The rescue install will use the new Portage filesystem layout - the broken install may not.

-   Mount [/dev] and friends in [/mnt/gentoo/home/rescue] just as if doing a new install but do **not** chroot yet.

<!-- -->

-   Bind mount the main ebuild repository to the rescue system:

    :::: cmd-box


    `root `[`#`]`mount -o bind /mnt/gentoo/var/db/repos/gentoo /mnt/gentoo/home/rescue/var/db/repos/gentoo`


    ::::

<!-- -->

-   Bind mount the distfiles directory:

    :::: cmd-box


    `root `[`#`]`mount -o bind /mnt/gentoo/var/cache/distfiles /mnt/gentoo/home/rescue/var/cache/distfiles`


    ::::

<!-- -->

-   Bind mount the binary package directory:

    :::: cmd-box


    `root `[`#`]`mount -o bind /mnt/gentoo/var/cache/binpkgs /mnt/gentoo/home/rescue/var/cache/binpkgs`


    ::::

<!-- -->

-   Copy over [/mnt/gentoo/etc/portage] to [/mnt/home/rescue/etc/portage]:

    :::: cmd-box


    `root `[`#`]`cp -r /mnt/gentoo/etc/portage /mnt/gentoo/home/rescue/etc/portage`


    ::::

Now the rescue install has all the settings from the broken installation.

### [Chroot into rescue install]

Follow the [chroot instructions from the handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Entering_the_new_environment "Handbook:AMD64/Installation/Base") but into the [/mnt/gentoo/home/rescue] directory instead.

### [][Edit /etc/portage/make.conf]

Inside of the new working rescue chroot, Portage must be told to create and save binary packages of everything we build.

Edit [/etc/portage/make.conf] by adding `buildpkg` to `FEATURES`.

This causes Portage to save binary tarballs of every package built to [/var/cache/binpkgs].

** Warning**\
Do not [emerge \--sync]. Packages that match the state of the broken installation are needed; this requires the repository to be in the *same* state.

## [Building packages]

Two choices:

1.  [quickpkg]
2.  [emerge]

### [][Quick package (quickpkg)]

** Warning**\
Take care with [quickpkg], it either drops configuration files or copies them in their current state from the install. This may be undesirable.

If the package needed is part of the stage3, use the [quickpkg] tool to make a binary package.

### [Emerge]

[emerge] will just work within the stage3 extracted. Build something small as a test like [[[sys-apps/sed]](https://packages.gentoo.org/packages/sys-apps/sed)[]] then check that the package has appeared in [/var/cache/binpkgs].

#### [More packages]

[emerge] whatever is needed. [/home/rescue] will stay around until deleted and it is only a chroot away. Upon return, don\'t forget to redo the bind mounts.

## [Installing binary packages]

After creating binary packages using any of the methods described above, they must be installed somehow to the broken system.

The best method to install binary packages depends on what is broken. The options below are presented in increasing order of risk (least risky first):

1.  Install \"properly\" using [emerge] where it works.
2.  Use [qmerge] (which doesn\'t need Python, it\'s part of [[[app-portage/portage-utils]](https://packages.gentoo.org/packages/app-portage/portage-utils)[]].
3.  Raw extract with [tar] the binpkgs (tarballs) onto the broken system until the safer option can be used.

### [Using emerge]

This requires chrooting into the install to be rescued. If a part of the toolchain is missing, this should work. Run:

`root `[`#`]`emerge -K `

This will either install the binary tarball and its dependencies or fail if the binaries cannot be found.

### [Using qmerge]

Outside of the chroot, run:

`root `[`#`]`qmerge `

### [Using tar]

If a chroot can not be created, [emerge] is not an option. Maybe [[[sys-libs/glibc]](https://packages.gentoo.org/packages/sys-libs/glibc)[]] is missing and there is no statically linked [[[sys-apps/busybox]](https://packages.gentoo.org/packages/sys-apps/busybox)[]]?

Each binary package is like a single package stage3. It has some extra information on the end that Portage uses, which will provoke a warning from [tar] that can be safely ignored.

** Warning**\
There is no safety net, [tar] will just spray files all over the filesystem.

#### [Extracting tar step-by-step method]

For safety\'s sake, unmount the rescue install at [/mnt/gentoo/home/rescue].

`root `[`#`]`umount /mnt/gentoo/home/rescue`

It may be necessary to unmount all the things mounted inside [/mnt/gentoo/home/rescue] first.

##### [Sanity checks]

Before issuing the [tar] command, verify:

-   The install is mounted at [/mnt/gentoo]

<!-- -->

-   Understand the `-xpf` and `-C` options to [tar]. Review the man page if unsure:

    :::: cmd-box


    `root `[`#`]`man tar`


    ::::

##### [Understanding the tar command]

** Warning**\
The `-p` option is essential. Without it, [tar] will work, the files will be installed but execute permissions will be dropped.

** Warning**\
Check the destination path: `-C /mnt/gentoo`, this is where all the output files will be sent.

** Tip**\
[tar] will work out the compression for itself, so the `-j` option is not required.

`root `[`#`]`tar --xattrs -xpf /mnt/gentoo/var/cache/binpkgs/ -C /mnt/gentoo`

This tells [tar] to e**x**tract, **p**reserving permissions, the **f**ile [/mnt/gentoo/var/cache/binpkgs/\] and **C**hange directory to [/mnt/gentoo] before it does anything else.

In fact, the input file name above is not correct. The full path to the tarball is required. Tab completion helps a lot.

Nervous users can add the `-v` option to [tar].

##### [Extract]

As described above, unpack the tarball (binary package) into the broken system.

`root `[`#`]`tar --xattrs -xpf /mnt/gentoo/var/cache/binpkgs/ -C /mnt/gentoo`

The package is now effectively installed to the broken install. Repeat as necessary for all packages until [emerge] can be used (see above) instead.

## [Tidying up]

Once the damage is fixed, delete [/home/rescue], or keep it around for next time.

With adequate space, it may be desirable to add `buildpkg` to the `FEATURES` variable as a regular thing. Then, the tarballs needed for rescuing the system will already exist.

Both [/var/cache/distfiles] and [/var/cache/binpkgs] will grow without limit. Run [eclean] occasionally to prune them.

## [See also]

-   [Knowledge Base:Recovering from a kernel boot failure](https://wiki.gentoo.org/wiki/Knowledge_Base:Recovering_from_a_kernel_boot_failure "Knowledge Base:Recovering from a kernel boot failure")
-   [Project:Portage/Fixing broken portage](https://wiki.gentoo.org/wiki/Project:Portage/Fixing_broken_portage "Project:Portage/Fixing broken portage") --- provides guidance on how to manually update or fix a broken Portage installation - particularly in the event [emerge -v1 sys-apps/portage] cannot be run.
-   [Recovering from a malfunctioning installation](https://wiki.gentoo.org/wiki/Gentoo_installation_tips_and_tricks#Recovering_from_a_malfunctioning_installation "Gentoo installation tips and tricks")
-   [Support](https://wiki.gentoo.org/wiki/Support "Support") --- provide **support** for technical issues encountered when installing or using Gentoo Linux
-   [Troubleshooting](https://wiki.gentoo.org/wiki/Troubleshooting "Troubleshooting") --- provide users with a set of techniques and tools to troubleshoot and fix problems with their Gentoo setups.