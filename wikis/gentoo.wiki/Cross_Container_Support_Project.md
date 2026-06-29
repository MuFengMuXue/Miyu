This page contains [[changes](https://wiki.gentoo.org/index.php?title=Cross_Container_Support_Project&diff=1300177)] which are not marked for translation.

\

[] The information in this article is probably **outdated**. You can help the Gentoo community by verifying and [updating this article](https://wiki.gentoo.org/index.php?title=Cross_Container_Support_Project&action=edit).

This page is aimed to introduce the GSoC 2012 project: Cross Container Support.

I will document the progress of my project here.

## Contents

-   [[1] [Running Qemu-user on chroot]](#Running_Qemu-user_on_chroot)
    -   [[1.1] [Host configuration]](#Host_configuration)
        -   [[1.1.1] [Qemu-user installation]](#Qemu-user_installation)
        -   [[1.1.2] [binfmt_misc kernel configuration]](#binfmt_misc_kernel_configuration)
    -   [[1.2] [Entering and exiting the chroot]](#Entering_and_exiting_the_chroot)
-   [[2] [Setup Crossdev]](#Setup_Crossdev)
-   [[3] [Cross Container]](#Cross_Container)
    -   [[3.1] [Install a cross compiler]](#Install_a_cross_compiler)
    -   [[3.2] [Create the chroot]](#Create_the_chroot)
    -   [[3.3] [Switch to native compiler]](#Switch_to_native_compiler)

## [Running Qemu-user on chroot]

This section extends the [qemu-user](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Compiling_with_qemu_user_chroot "Embedded Handbook/General/Compiling with qemu user chroot") and describes how to build a chroot with qemu-user on an **[x86]** machine.

### [Host configuration]

#### [Qemu-user installation]

In order to take advantage of qemu-user mode we need to do a few things. First, merge the main package. Note the use of the `static` USE flag.

`root `[`#`]`echo "=app-emulation/qemu-user-1.1.0-r1" >> /etc/portage/package.accept_keywords `

`root `[`#`]`USE="static" emerge -b1 app-emulation/qemu-user `

#### [binfmt_misc kernel configuration]

First ensure the kernel module binfmt_misc has been built.

Add this to your kernel .config: CONFIG_BINFMT_MISC=m or CONFIG_BINFMT_MISC=y.

If this module is not built already, then the development host will require a reboot after the kernel update and modules_install.

[KERNEL] **3.2.1-gentoo-r2 (`CONFIG_BINFMT_MISC`)**

    Executable file formats / Emulations  --->
       [*] Kernel support for MISC binaries

Mount the binfmt_misc handler if it\'s not already, then register the supported executable formats with the kernel via the procfs.

`root `[`#`]`[ -d /proc/sys/fs/binfmt_misc ] || modprobe binfmt_misc `

`root `[`#`]`[ -f /proc/sys/fs/binfmt_misc/register ] || mount binfmt_misc -t binfmt_misc /proc/sys/fs/binfmt_misc `

Next, register qemu-user-arch to the binfmt_misc module. You don\'t need to add them one by one and Luca has provided a initscript to get the bin formats registered\':

`root `[`#`]`/etc/init.d/qemu-binfmt start`

The service on boot:

`root `[`#`]`rc-update add qemu-binfmt default`

More details of registering bin formats can be found in the [/var/db/repos/gentoo/app-emulation/qemu-user/files/qemu-binfmt.initd.\*] files.

### [Entering and exiting the chroot]

Choose a stage3 tarball from [installation media](https://www.gentoo.org/downloads/).

An arm architecture is used here as an example to show how to enter/exit the chroot.

-   Download and unpack arm stage tarball:

`root `[`#`]`mkdir arm-chroot && cd arm-chroot`

`root `[`#`]`wget http:// stage3-armv7a-date.tar.bz2`

`root `[`#`]`tar -xvf stage3-armv7a-date.tar.bz2`

-   Install the static qemu-user into the chroot:

`root `[`#`]` ROOT=$PWD/ emerge -K qemu-user`

-   Mount the required directories:

`root `[`#`]`mkdir -p usr/portage`

`root `[`#`]` mount --bind /usr/portage usr/portage `

`root `[`#`]` mount --bind /proc proc `

`root `[`#`]` mount --bind /sys sys`

-   Chroot into the environment:

`root `[`#`]`chroot . /bin/busybox mdev -s `

`root `[`#`]` chroot . /bin/bash --login`

-   Unmount stuff when not in use:

`root `[`#`]`umount usr/portage `

`root `[`#`]` umount sys `

`root `[`#`]` umount proc`

## [Setup Crossdev]

The first thing that is necessary is the creation of an [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository"). If you have one, emerge the script:

`root `[`#`]`emerge --ask sys-devel/crossdev`

This will provide you with the crossdev script. This script automates the steps necessary to build a toolchain. These steps are, in short:

1.  binutils: Build a cross-binutils, which links and processes for the target architecture.
2.  linux-headers: Install a set of C library and kernel headers for the target architecture.
3.  libc-headers: Additional header files
4.  gcc-stage-1: Build a basic (stage 1) gcc cross-compiler. This will be used to compile the C library. It will be unable to build anything almost else (because it can\'t link against the C library it doesn\'t have).
5.  libc: Build the cross-compiled C library (using the stage 1 cross compiler).
6.  gcc-stage-2: Build a full (stage 2) C cross-compiler.

All cross toolchains will be kept locally in the ebuild repository, separate from native tools.

[FILE] **`/etc/portage/make.conf`**

    source /var/lib/layman/make.conf

    PORTDIR_OVERLAY="/usr/local/portage $"

The script is used like:

`root `[`#`]`crossdev -t powerpc-unknown-linux-gnu`

This will build a cross-compiling toolchain for PowerPC machines.

By default, the newest stable version of the binutils, libraries, and C compiler will be used. It is quite often the case they will not compile themselves through the entire build process. Less bleeding edge versions can be specified with additional flags:

    --b 2.22      # specifies the version of binutils
    --g 4.6.3     # specifies the version of gcc
    --l 2.15-r2   # specifies the version of the tuple-specified libc
    --k 3.5       # specifies the version of the kernel headers

It is recommended trying older versions, particularly of gcc, if the script fails.

If you want to remove a toolchain, use the clean flag:

`root `[`#`]`crossdev -C powerpc-unknown-linux-gnu`

This will unmerge the packages created by crossdev.

If you got the errors about fortran, use the fellow command:

`root `[`#`]`USE="-fortran nossp" crossdev -t powerpc-unknown-linux-gnu`

\

## [Cross Container]

The lxc.sh tool can download, configure and create a multi-arch Gentoo guest. Using this tool, the user build a native gcc in chroot. You can download it here: [lxc.sh](https://github.com/jinghuang/cross_container_support)

Next, we will take **armv7a_hardfloat** as a example to build the native compiler in chroot.

### [Install a cross compiler]

You must install the cross compiler manually:

`root `[`#`]`USE="-fortran nossp" crossdev -t armv7a-hardfloat-linux-gnueabi`

### [Create the chroot]

You can create an arm Gentoo guest:

`root `[`#`]`./lxc.sh create -i `*`ip_address`*` -g `*`gateway`*` -n `*`guest_name`*` -r `*`rootfs`*` -a arm`\
`What is the subarch of arm? armv7a`

You can also start and destroy the arm Gentoo guest:

`root `[`#`]`./lxc.sh start -n `*`guest_name`*

`root `[`#`]`./lxc.sh destroy -n `*`guest_name`*` -r `*`rootfs`*

Additional developers, bug fixes, comments, etc. are welcome.

### [Switch to native compiler]

In chroot, you can switch to native compiler:

`root `[`#`]`cd /root `

`root `[`#`]`source switch.sh native `

Then, you can get the native armv7a-hardfloat-linux-gnueabi-gcc.

To use it, just specify the **CC=armv7a-hardfloat-linux-gnueabi-gcc** in the Makefile.

You also could switch to emulated gcc as well:

`root `[`#`]`source switch.sh emu`