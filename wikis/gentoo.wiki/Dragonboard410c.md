**Resources**

[[]][Home](http://www.96boards.org/products/ce/dragonboard410c/)

[[]][GitHub](https://github.com/96boards/documentation)

** Warning**\
This is work in progress and incomplete. Don\'t expect to get something working out of following these instructions yet.

The Dragonboard410c is a credit-card sized minicomputer, akin to the popular RaspberryPi series. It\'s sporting a Qualcomm Snapdragon 410, quad-core Cortex A53 @ 1.2GHz (which implies 64bit arch) and an Adreno 306 GPU.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
-   [[2] [Initial Flash]](#Initial_Flash)
-   [[3] [Preparations]](#Preparations)
    -   [[3.1] [Cross-compiler/-toolchain]](#Cross-compiler.2F-toolchain)
    -   [[3.2] [skales tools]](#skales_tools)
    -   [[3.3] [miscellanous tools]](#miscellanous_tools)
    -   [[3.4] [Kernel]](#Kernel)
-   [[4] [boot.img]](#boot.img)
    -   [[4.1] [Kernel Compilation]](#Kernel_Compilation)
    -   [[4.2] [Initrd / Initramfs]](#Initrd_.2F_Initramfs)
    -   [[4.3] [Device Tree]](#Device_Tree)
    -   [[4.4] [Assemble db410c-boot.img]](#Assemble_db410c-boot.img)

## [Hardware]

### [Standard]

  ----------------- ------------------------------------------------------------------------------------------------------------------------------------- ------------- ------------------ ---------------- --------------------------------
  Device            Make/model                                                                                                                            Status        Kernel driver(s)   Kernel version   Notes
  CPU               [ARM Cortex A53](http://www.arm.com/products/processors/cortex-a/cortex-a53-processor.php) @ 1.2GHz   Works         N/A                N/A              quad-core, 64bit
  Graphics          Adreno 306 GPU @ 400MHz                                                                                                               not tested    TBD                TBD              Supports OpenGL ES 3.0, OpenCL
  Memory            1GB LPDDR3 @ 533MHz                                                                                                                   Works         N/A                N/A
  Onboard Storage   8GB eMMC 4.51                                                                                                                         Works         TBD                N/A
  ----------------- ------------------------------------------------------------------------------------------------------------------------------------- ------------- ------------------ ---------------- --------------------------------

## [Initial Flash]

The Dragonboard comes pre-installed with Android. For a quick and dirty flash, consult the Linux User Guide on [http://www.96boards.org/products/ce/dragonboard410c/docs/](http://www.96boards.org/products/ce/dragonboard410c/docs/). It guides you through a quick procedure that gets Linaro/Debian up and running.

We, however, want to build our own images. For that to work we need to download a couple of things. For that I\'d suggest you create a dedicated directory; I called mine [\~/dragonboard].

## [Preparations]

### [][Cross-compiler/-toolchain]

To compile our stuff, we need a cross-compiler. For that, we use the fabulous [crossdev] tool.

** Note**\
[crossdev] requires an overlay to store its newly generated ebuilds. If you don\'t want to pollute your existing ones, I\'d suggest using [-oO] to create a custom one.

** Note**\
If you run into problems with certain use-flags (like I did with [go]), use [crossdev]\'s [\--\[x\]env] flag to modify it.

`root `[`#`]`emerge crossdev`

`root `[`#`]`crossdev -t aarch64-unknown-linux-gnu -oO crossdev --genv 'USE="-go"' `

    ---------------------------------------------------------------------------------
     * crossdev version:      20151026
     * Host Portage ARCH:     amd64
     * Target Portage ARCH:   arm64
     * Target System:         aarch64-unknown-linux-gnu
     * Stage:                 4 (C/C++ compiler)
     * ABIs:                  arm64

     * binutils:              binutils-[latest]
     * gcc:                   gcc-[latest]
     * headers:               linux-headers-[latest]
     * libc:                  glibc-[latest]

     * CROSSDEV_OVERLAY:      crossdev
     * PORT_LOGDIR:           /var/log/portage/
     * PORTAGE_CONFIGROOT:
     * Portage flags:

### [skales tools]

We will further need the \"skales\" tools, which are basically a set of scripts.

`user `[`$`]`cd ~/dragonboard `

`user `[`$`]`git clone `[`git://codeaurora.org/quic/kernel/skales`](git://codeaurora.org/quic/kernel/skales)` `

    Cloning into 'skales'...
    remote: Counting objects: 276, done.
    remote: Total 276 (delta 0), reused 0 (delta 0)
    Receiving objects: 100% (276/276), 49.22 KiB | 39.00 KiB/s, done.
    Resolving deltas: 100% (171/171), done.
    Checking connectivity... done.

### [miscellanous tools]

For those to work we will also need [ftdget], which is a part of [sys-apps/dtc]. And for control- and flash-tasks we will need the [fastboot] utility from [dev-util/android-tools].

`root `[`#`]`emerge sys-apps/dtc dev-util/android-tools`

### [Kernel]

Gentoo-native sources provide drivers that have been accepted in mainline already.

But to get the latest and greatest from the 96boards and Linaro devs:

`user `[`$`]`git clone `[`https://github.com/96boards/linux/`](https://github.com/96boards/linux/)` db_410c_kernel `

    Cloning into 'db410c_kernel'...
    remote: Counting objects: 4526190, done.
    remote: Compressing objects: 100% (25/25), done.
    remote: Total 4526190 (delta 24), reused 20 (delta 20), pack-reused 4526145
    Receiving objects: 100% (4526190/4526190), 1.39 GiB | 255.00 KiB/s, done.
    Resolving deltas: 100% (3737318/3737318), done.
    Checking connectivity... done.
    Checking out files: 100% (52502/52502), done.

## [boot.img]

### [Kernel Compilation]

First we need a configuration. I am going with the provided stock configs.

`user `[`$`]`cd db_410c_kernel `

`user `[`$`]`make ARCH=arm64 CROSS_COMPILE=aarch64-unknown-linux-gnu- defconfig distro.conf`

Then compile the kernel. Use a value corresponding to your compiling CPU\'s core-count for [X] - e.g. 4 or 5 for a quad-core.

`user `[`$`]`make ARCH=arm64 CROSS_COMPILE=aarch64-unknown-linux-gnu- -jX`

This will take a while. You can interrupt at any time, though, and resume with the same command.

### [][Initrd / Initramfs]

If you want to use upstream\'s initrd, get it here: [http://builds.96boards.org/snapshots/dragonboard410c/linaro/debian/latest/](http://builds.96boards.org/snapshots/dragonboard410c/linaro/debian/latest/)

`user `[`$`]`wget `[`http://builds.96boards.org/snapshots/dragonboard410c/linaro/debian/latest/initrd.img-4.4.0-linaro-lt-qcom`](http://builds.96boards.org/snapshots/dragonboard410c/linaro/debian/latest/initrd.img-4.4.0-linaro-lt-qcom)

(The filename might differ slightly, so just browse the [latest] directory.)

** Note**\
This step is not needed right now, as we will use upstream\'s initrd. Resume below.

Install the kernel\'s modules to a temporary directory and run depmod on them.

`user `[`$`]`mkdir ../db_410c_modules/modules -p `

`user `[`$`]`cat include/config/kernel.release `

    4.4.0+   # kernel version

Be sure to get the version right or the kernel will not be able to find its modules later on.

`root `[`#`]`depmod -a -b ../db_410c_modules/modules 4.4.0+`

** Note**\
resume here

### [Device Tree]

We will assemble the boot.img in a separate directory, so change there.

`user `[`$`]`mkdir ~/dragonboard/boot.img `

`user `[`$`]`cd ~/dragonboard/boot.img`

Use the [dtbTool] from skales to assemble [dt.img].

`user `[`$`]`../skales/dtbTool -o dt.img -s 2048 \ ../db_410c_kernel/arch/arm64/boot/dts/qcom`

** Note**\
If you lack the [dts/qcom] directory, follow the instructions to compile the kernel above.

### [Assemble [db410c-boot.img]]

You have several options here for your cmdline. Upstream suggests the following:

`user `[`$`]`export cmdline="root=/dev/ram0 rw rootwait console=ttyMSM0,115200n8" `

    # This loads the rootfs from your ramdisk.

`user `[`$`]`export cmdline="root=/dev/disk/by-partlabel/rootfs rw rootwait console=ttyMSM0,115200n8" `

    # This is your choice if you have a rootfs installed on your eMMC userdata partition.

`user `[`$`]`export cmdline="root=/dev/disk/by-partlabel/rootfs rw rootwait console=ttyMSM0,115200n8 text" `

    # This just adds a text console.

`user `[`$`]`../skales/mkbootimg --kernel ../db_410c_kernel/arch/arm64/boot/Image \`\
`--ramdisk initrd.img-4.4.0-linaro-lt-qcom \`\
`--output db410c-boot.img \`\
`--dt dt.img \`\
`--pagesize 2048 \`\
`--base 0x80000000 \`\
`--cmdline "$"`

** Note**\
If [mkbootimg] fails, whining about [AttributeError: \'bytes\' object has no attribute \'encode\'], just edit it to call [python2] instead of [python].\
Also note that, although similar in name, [skales/mkbootimg] is different from the binary provided by [dev-embedded/u-boot-tools].