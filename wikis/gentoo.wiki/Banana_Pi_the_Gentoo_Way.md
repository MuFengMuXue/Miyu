[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

This guide provides details on how to install Gentoo with a user compiled kernel and a Gentoo stage 3 on the Banana Pi. I have been using a number of Banana Pi\'s in a clustered distcc cross compiling environment for nearly a year. There has been a lot of controversy about the Banana Pi and it developers. The hardware is a nice board, but some of the practices concerning the methods undertook by the developers concerning business practices and the software side is certainly controversial. Best summed up on the [Linux-Sunxi.org/Banana_Pi](https://linux-sunxi.org/Banana_Pi) page.

To provide some clarification on documentation from different sources. Nearly everything provided on the Lemaker websites, and other Banana Pi websites has been copied from the Linux-Sunxi.org pages. While all the direct copies of the Linux-Sunxi.org website have been taken down. I am assuming some copyright infringement issues surfaced. For some reason, Lemaker prefers to maintain their own full kernel git repositories rather than simply having a simple patch repository and providing patches to upstream Linux-Sunxi.org and U-Boot to be included in their respective git repositories. This practice makes it more difficult for LeMaker patches to be applied to other kernel sources by the general user base. Some early patches were provided and are included in the Linux-Sunxi.org git repositories, but latter refinements have not been submitted for inclusion.

I have to provide some cautionary advice concerning some of the ready to go images for the Banana Pi, along with some of the git repositories. The LeMaker Gentoo release is not put together very well, specifically when it comes to CFLAGS. It is obvious that they are inexperienced and are not aware of the impact of having incorrect or missing CFLAGS. I have seen countless posts of people spending countless hours attempting to get hardware acceleration working, while the CFLAGS supplied with the LeMaker Gentoo release, will not allow hardware acceleration to its fullest. At least it did not earlier this year 2015. Here is a post of mine concerning [CFLAGS for the Banana Pi](https://forums.gentoo.org/viewtopic-t-1011644-highlight-.html).

I have found numerous posts on a number of forums, as well as the Lemaker forums themselves, with claims of malicious content. I my self have not bothered with disseminating any of the so-called official releases, and cannot confirm any of the claims. Considering the clashes and legal disputes over trademarks and domain ownership, along with the claim of open source, when the Banana Pi is certainly not, visit the Linux-Sunxi.org website for more details on that. It may certainly be true that some parties may have injected malicious content in an attempt to harm other participating parties.

The best way to avoid any possible security risks, is to use software that has been reviewed and tested by a reputable process and group. Therefore this guide will provide details on how to compile a kernel from the [Linux-Sunxi.org](https://linux-sunxi.org/Main_Page) git repository, who is an open source software community dedicated to providing open source operating system support for Allwinner SoC based devices. Instructions for using the Banana Pi (Lemaker) developers git repository are also included. The Operating System Source files will be a standard Gentoo Arm 7 Stage 3 pulled from an Approved Gentoo Mirror.

** Note**\
As of 2020, a mainline Linux kernel `>=5.4`, as provided by [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]] works on the Banana Pi.

This is better than using the [outdated and unmaintained sunxi-3.4 branch](https://github.com/linux-sunxi/linux-sunxi/tree/sunxi-3.4). Use the [sunxi_defconfig]. You will also need a mainline u-boot with support for dtb (e.g. v2019.10).

In this case, the files needed to boot are the [sun7i-a20-bananapi.dtb], the kernel\'s zImage, and the [boot.scr generated from the boot.cmd](https://linux-sunxi.org/U-Boot#Boot).

To speed up compilation, it is suggested that you set up a distcc cross compiling environment on an **[AMD64]** or other faster architecture. [Distcc](https://wiki.gentoo.org/wiki/Distcc "Distcc") and [Distcc/Cross-Compiling](https://wiki.gentoo.org/wiki/Distcc/Cross-Compiling "Distcc/Cross-Compiling"). Not all packages will compile on other machines in the cluster, but many will. If you have a number of Banana Pi devices, use the buildpkg feature so that binary packages are built that can then be quickly installed on the other Banana Pi\'s or distributed to devices in other locations. An [NFS](https://wiki.gentoo.org/wiki/NFS "NFS") mount can be used to have the packages directory mounted on all the Banana Pi devices on your lan, so that binary packages are available to all devices without having to manually distribute the binary packages.

## Contents

-   [[1] [Intro to the Banana Pi]](#Intro_to_the_Banana_Pi)
-   [[2] [Preparing The SDCard]](#Preparing_The_SDCard)
-   [[3] [Install Root File System - Arm 7 Stage 3]](#Install_Root_File_System_-_Arm_7_Stage_3)
-   [[4] [Cross Compiling]](#Cross_Compiling)
-   [[5] [DistCC/Cross-Compiling]](#DistCC.2FCross-Compiling)
-   [[6] [U-Boot]](#U-Boot)
-   [[7] [Script.bin]](#Script.bin)
-   [[8] [Compile the Kernel]](#Compile_the_Kernel)
-   [[9] [Final Boot File]](#Final_Boot_File)
-   [[10] [Booting to an SATA SSD Disk]](#Booting_to_an_SATA_SSD_Disk)
-   [[11] [Finalizing in preparation for booting]](#Finalizing_in_preparation_for_booting)
-   [[12] [Optional]](#Optional)
-   [[13] [Plug in your sdcard and boot]](#Plug_in_your_sdcard_and_boot)
-   [[14] [Tips & Tricks & Uses]](#Tips_.26_Tricks_.26_Uses)
-   [[15] [See also]](#See_also)

## [Intro to the Banana Pi]

The Banana Pi has a Cortex-A7 Arm processor Model A20 manufactured by [Allwinner Technology](http://www.allwinnertech.com/en/clq/processora/A20.html). Which is a different architecture than what most common place computers have. Most desktops and laptops are either the newer amd64 or the older x86. It is not possible to compile code with one gcc architecture for another. Therefore to compile a kernel for the Banana Pi, if you do not already have an Arm 7 device running, you must setup a Cross Compiling environment on an amd64 or x86 computer. Fortunately it is a relatively simple thing to do. I highly suggest everyone at least once, go through the procedure as it is not all that difficult, what you will learn will provide for a great building block for the future.

If you just want to get up and running with out all the compiling. I am providing the 4 necessary files already compiled and tested out. These files including the kernel have been configured and compiled from the [Linux-Sunx.org git repository](https://github.com/linux-sunxi/linux-sunxi)

  --------------------------- -------------------------------
  Files Included              What it is for
  script.bin                  board instructions
  u-boot-sunxi-with-spl.bin   bootloader
  uEnv-sda1.txt               boot parameters for ssd drive
  uEnv.txt                    boot parameters for sdcard
  uImage                      kernel - version 3.4.103+
  config                      kernel config
  --------------------------- -------------------------------

\

  --------------------------------------------------------------------------------------------------------------------------------------------------
  Downloads
  [Banana Pi Boot Files](https://s3-us-west-2.amazonaws.com/sowis/bananapi/bananapi-boot-files-3.4.103%2B.tar.bz2)
  [md5sum](https://s3-us-west-2.amazonaws.com/sowis/bananapi/md5.txt)
  --------------------------------------------------------------------------------------------------------------------------------------------------

If you download the prepared files you can skip much of the instruction and only need to do the below sections.

  ---------------------------------------------------------------------------------
  Sections Needed Using Pre-Compiled Kernel
  [Preparing The SDCard](#Preparing_The_SDCard)
  [Install Root File System](#Install_Root_File_System_-_Arm_Stage_3)
  [Final Boot File](#Final_Boot_File)
  [Booting to an SSD Disk](#Booting_to_an_SSD_Disk)
  [Finalizing in preparation for booting](#Finalizing_in_preparation_for_booting)
  [Optional](#Optional)
  [Plug in your sdcard and boot](#Plug_in_your_sdcard_and_boot)
  [Tips & Tricks](#Tips_.26_Tricks)
  ---------------------------------------------------------------------------------

## [Preparing The SDCard]

Insert your sdcard and run lsblk.

`root `[`#`]`lsblk`

Look for your sdcard, you should see a list of all your drives and mounted partitions with their attachment points starting with sda. I will be using /dev/sdX with X being used as the letter for for your sdcard.

** Warning**\
Make sure you run the next command on your sdcard, if you run it on the wrong drive, like your currently installed and running OS. It will destroy the bootloader and partition tables, which will not be recoverable, unless you make a backup first, you have been warned.

This will clear all the data in the first part of the sdcard to ensure no old data causes any problems.

`root `[`#`]`dd if=/dev/zero of=/dev/sdX bs=1k count=1023 seek=1`

You need a minimum of two partitions. 1. Boot - 75Mb - 150Mb will do, perhaps larger if you intend on storing a lot of different kernels or other files. 2. Root - Can be the rest of the disk, or you may make a home partition, var partition or can even do a swap partition. Any partition configuation you want.

`root `[`#`]`fdisk /dev/sdX`

At the fdisk prompt, delete old partitions and create a new one:

     a.Type o. This will clear out any partitions on the drive.
     b.Type p press enter to list partitions. There should be no partitions left.
     c.Type n press enter, then p press enter for primary, 1 for the first partition on the sdcard/drive press enter, 2048 for the first
       sector press enter.
     d.Type +150M and press enter.
     e.Type p and you will see the first partition listed.
     f.Type n press enter, then p press enter for primary, 2 for the second partition on the sdcard/drive press enter, press enter to select
       the default, should be 309248 if you did a 150MB first partition, if you press enter the default will be for the rest of the space left on
       the disk. If you plan on additional partitions select the size you want for your second partition.
     g.Type p press enter and you should see two partition, first one 150M the second one the rest of your sdcard/disk.
     h.Type t press enter, type 1 for the first partition press enter, type l press enter, you will see a list, press b and press enter to
       select W95 FAT32.
     i.Type p press enter, you should now see two partitions with the first as W95 FAT32 and the second as Linux. Linux does not need a boot
       partition toggled as bootable, you may do so if you wish, as it will not hurt anything, but it is absolutely unnecessary.
     j. Type w press enter to write the partition data to the sdcard/disk.

Now we are going to format the partitions with a file system.

`root `[`#`]`mkfs.vfat -F 32 /dev/sdX1 `

`root `[`#`]`mkfs.ext4 /dev/sdX2`

Create mountpoints\...

`root `[`#`]`mkdir -p /mnt/bananapi/boot `

`root `[`#`]`mkdir /mnt/bananapi/root`

..and mount the partitions.

`root `[`#`]`mount /dev/sdX1 /mnt/bananapi/boot `

`root `[`#`]`mount /dev/sdX2 /mnt/bananapi/root`

If you downloaded the pre-compiled files place them in /mnt/bananapi/boot

`root `[`#`]`tar xvjpf bananapi-boot-files-3.4.103+.tar.bz2 -C /mnt/bananapi/boot/`

## [Install Root File System - Arm 7 Stage 3]

Go to the mirrors page and download a **stage3-armv7a_hardfp-latest.tar.bz2** or with most recent date **stage3-armv7a_hardfp-20150721.tar.bz2** [Gentoo Mirrors](https://www.gentoo.org/downloads/mirrors/) Get what ever the latest build is, it may be different than shown below:

`root `[`#`]`tar xvjpf stage3-armv7a_hardfp-latest.tar.bz2 -C /mnt/bananapi/root/`

If using the pre-compiled kernel skip to: [Final Boot Files](#Final_Boot_File)

## [Cross Compiling]

If you do not have a running arm device/computer to build from, and are running an Amd64 or x86 Desktop/Laptop. You will need to setup a cross compiling environment. Follow the [Distcc/Cross-Compiling guide](https://wiki.gentoo.org/wiki/Distcc/Cross-Compiling "Distcc/Cross-Compiling"). You may also want to review the [Raspberry Pi Cross building](https://wiki.gentoo.org/wiki/Raspberry_Pi/Cross_building "Raspberry Pi/Cross building") & [BeagleBone Black](https://wiki.gentoo.org/wiki/BeagleBone_Black "BeagleBone Black"). Since compiling on one Banana Pi is not all that speedy you will want to take advantage of faster computers on you network. [Distcc](https://wiki.gentoo.org/wiki/Distcc "Distcc")

When you install your arm crossdev, it is important that you use the cflags that you will be using on the Banana Pi. If neon-vfpv4 is not used, you will be losing some graphics performance capability. While you are compiling on your Cross-Compiler, you can watch the console feed for warnings and errors, if EXTRA_CONF settings are incorrect or missing, you will see warnings, though the compilation in most cases will continue.

Here is a link to some information: [Arm Cortex A Processors & GCC Commands](https://community.arm.com/groups/tools/blog/2013/04/15/arm-cortex-a-processors-and-gcc-command-lines).

You will need to emerge and install crossdev and will need git for downloading git repositories.

`root `[`#`]`emerge dev-vcs/git sys-devel/crossdev`

You will need to run this command on every machine that is not an Arm device that will be used for compiling and or distcc.

`root `[`#`]`crossdev -S -P -v EXTRA_ECONF="-march=armv7-a -mfpu=neon-vfpv4 -ffast-math" -t armv7a-unknown-linux-gnueabihf`

## [][DistCC/Cross-Compiling]

[Distcc](https://wiki.gentoo.org/wiki/Distcc "Distcc") will speed up compilation of packages by distributing the compiling to one or more computers in your lan. Not all programs compiled on the Bananan Pi will finish compiling with distcc enabled. With a few programs it will be necessary to set your set your MAKEOPTS to MAKEOPTS=\"-j1 -l2\", which will keep all compilation on the single device. If a package fails when compiling, the first thing to try is change your MAKEOPTS.

[`#`]`emerge -av sys-devel/distcc`

** Important**\
Remember to install [[[sys-devel/distcc]](https://packages.gentoo.org/packages/sys-devel/distcc)[]] on all of the participating machines.

You need to add the features setting to the make.conf file on all computers that are going to be used for distcc:

[FILE] **`/etc/portage/make.conf`**

    FEATURES="distcc"

** Important**\
Don\'t use distcc-pump, as it is not supported in Portage anymore: [[[bug #702146]](https://bugs.gentoo.org/show_bug.cgi?id=702146)[]]

You will now have to set the distcc hosts in the /etc/distcc/hosts file:

[FILE] **`/etc/distcc/hosts`**

    # --- /etc/distcc/hosts -----------------------
    # See the "Hosts Specification" section of
    # "man distcc" for the format of this file.
    #
    # By default, just test that it works in loopback mode.
    192.168.x.xx,lzo
    192.168.x.xxx,lzo
    localhost,lzo

** Important**\
The order of the hosts are important. Put your fastest computer first with the next fastest next and so on. Put the Banana Pi last, as that theoretically will be the slowest machine.

You have to configure the /etc/conf.d/distcc file on all your computers that you want listening to receive distcc orders from the Banana Pi as well as on the Banana Pi:

[FILE] **`/etc/conf.d/distcc`**

    DISTCCD_OPTS="--port 3632 --log-level notice --log-file /var/log/distccd.log -N 15 --listen 192.168.x.xxx --allow 192.168.x.xx --allow 192.168.x.xxx"

Start Distcc and add to rc-update to be started on boot on all machines you want distcc to be running on:

`root `[`#`]`/etc/init.d/distccd start`

`root `[`#`]`rc-update add distccd default`

If you have [Iptables](https://wiki.gentoo.org/wiki/Iptables "Iptables") running you will need to open the distcc ports on all machines:

[CODE]

    iptables -A INPUT -p tcp -i bond0 -s 192.168.x.xxx -d 192.168.x.xxx --dport 3632 -j ACCEPT

You will need to make some changes on the Banana Pi so the computers that are receiving distcc orders from the Banana Pi use the correct gcc version: Reference the [Distcc/Cross-Compiling](https://wiki.gentoo.org/wiki/Distcc/Cross-Compiling "Distcc/Cross-Compiling") documentation:

`root `[`#`]`cd /usr/lib/distcc/bin `

`root `[`#`]`ls -l`

    total 0
    lrwxrwxrwx  1 root root 15 Mar 2 09:45 c++ -> /usr/bin/distcc
    lrwxrwxrwx  1 root root 15 Mar 2 09:45 cc -> /usr/bin/distcc
    lrwxrwxrwx  1 root root 15 Mar 2 09:45 g++ -> /usr/bin/distcc
    lrwxrwxrwx  1 root root 15 Mar 2 09:45 gcc -> /usr/bin/distcc
    lrwxrwxrwx  1 root root 15 Mar 2 09:45 armv7a-unknown-linux-gnueabihf-c++ -> /usr/bin/distcc
    lrwxrwxrwx  1 root root 15 Mar 2 09:45 armv7a-unknown-linux-gnueabihf-g++ -> /usr/bin/distcc
    lrwxrwxrwx  1 root root 15 Mar 2 09:45 armv7a-unknown-linux-gnueabihf-gcc -> /usr/bin/distcc

You will need to replace the links with a link to a wrapper that will tell the build machines which version of gcc to use:

[FILE] **`/usr/lib/distcc/bin/armv7a-unknown-linux-gnueabihf-wrapper`Distcc crossdev wrapper file**

    #!/bin/bash
    exec /usr/lib/distcc/bin/armv7a-unknown-linux-gnueabihf-g$ "$@"

`root `[`#`]`rm c++ g++ gcc cc `

`root `[`#`]`chmod a+x /usr/lib/distcc/bin/armv7a-unknown-linux-gnueabihf-wrapper `

`root `[`#`]`ln -s armv7a-unknown-linux-gnueabihf-wrapper cc `

`root `[`#`]`ln -s armv7a-unknown-linux-gnueabihf-wrapper gcc `

`root `[`#`]`ln -s armv7a-unknown-linux-gnueabihf-wrapper g++ `

`root `[`#`]`ln -s armv7a-unknown-linux-gnueabihf-wrapper c++ `

Double check that you did things right:

`root `[`#`]`ls -l`

    total 4
    lrwxrwxrwx 1 root root 15 Mar  2 09:56 armv7a-unknown-linux-gnueabihf-c++ -> /usr/bin/distcc
    lrwxrwxrwx 1 root root 15 Mar  2 09:56 armv7a-unknown-linux-gnueabihf-g++ -> /usr/bin/distcc
    lrwxrwxrwx 1 root root 15 Mar  2 09:56 armv7a-unknown-linux-gnueabihf-gcc -> /usr/bin/distcc
    -rw-r--r-- 1 root root 85 Mar  2 08:10 armv7a-unknown-linux-gnueabihf-wrapper
    lrwxrwxrwx 1 root root 38 Mar  2 09:57 c++ -> armv7a-unknown-linux-gnueabihf-wrapper
    lrwxrwxrwx 1 root root 38 Mar  2 09:57 cc -> armv7a-unknown-linux-gnueabihf-wrapper
    lrwxrwxrwx 1 root root 38 Mar  2 09:57 g++ -> armv7a-unknown-linux-gnueabihf-wrapper
    lrwxrwxrwx 1 root root 38 Mar  2 09:57 gcc -> armv7a-unknown-linux-gnueabihf-wrapper

You can monitor distcc a number of ways:

`root `[`#`]`watch -n1 DISTCC_DIR="/var/tmp/portage/.distcc/" distccmon-text`

`user `[`$`]`distccmon-text 10`

If you have a window manager or desktop running you can use the gui

`user `[`$`]`distccmon-gui`

To monitor Portage\'s [distcc] usage:

`root `[`#`]`DISTCC_DIR="/var/tmp/portage/.distcc/" distccmon-text 10 `

`root `[`#`]`DISTCC_DIR="/var/tmp/portage/.distcc/" distccmon-gui`

If you use [Conky](https://wiki.gentoo.org/wiki/Conky "Conky"), you can see distcc being used in inbound and outbound connections. Conky can be configured to display distcc details via the distccmon monitor or display activity by portage and or activity in the /var/tmp/portage/.distcc folder.

## [U-Boot]

You will need to build a bootloader specific for the Banana Pi. You have a choice of using either the Linux-Sunxi git repositories or the Lemaker git repository. If you prefer to us the Linux-Sunxi repository you can simply download the boards.cfg from LeMaker to see if it has been updated and not provided to upstream Linux-Sunxi. You can simply edit the changes or copy over the LeMaker boards.cfg. You can visit the git repository to check without having to clone both repositories. With LeMaker being in such a disarray, there is no telling who has access to their repositories, therefore I stay away from them. I have included the links to the Lemaker repository for those that still want to use them.

If you do not have u-boot-tools installed install it:

`root `[`#`]`emerge -av u-boot-tools`

Make a build folder to work in. It can be called anything and can be located anywhere you want. Most things can be configured as a regular user, but then have to be compiled as root.

`root `[`#`]`mkdir /mnt/bananapi-build`

`root `[`#`]`cd /mnt/bananapi-build`

Since both repositories are named the same, you will need to keep them separated:

`root `[`#`]`mkdir sunxi lemaker`

`root `[`#`]`cd sunxi`

Clone the Sunxi git repository:

`root `[`#`]`git clone https://github.com/linux-sunxi/u-boot-sunxi.git`

Change to the LeMaker folder:

`root `[`#`]`cd ../lemaker`

Clone the LeMaker

`root `[`#`]`git clone https://github.com/LeMaker/u-boot-sunxi.git`

Check for differance:

`root `[`#`]`cd ..`

`root `[`#`]` diff lemaker/u-boot-sunxi/boards.cfg sunxi/u-boot-sunxi/boards.cfg`

If they are different you can either append the sunxi boards.cfg or make a copy and over-write it.

`root `[`#`]`mv sunxi/u-boot-sunxi/boards.cfg /mnt/bananapi-build/sunxi/u-boot-sunxi/boards-sunxi.cfg && cp lemaker/boards.cfg sunxi/u-boot-sunxi`

To use Sunxi:

`root `[`#`]`cd sunxi/u-boot-sunxi/`

To use LeMaker:

`root `[`#`]`cd lemaker/u-boot-sunxi/`

Then run the following commands in either repository - First you need to configure for the Banana Pi:

`root `[`#`]`make ARCH=arm CROSS_COMPILE=armv7a-unknown-linux-gnueabihf- BananaPi_config`

If you have the Banana Pi Pro

`root `[`#`]`make ARCH=arm CROSS_COMPILE=armv7a-unknown-linux-gnueabihf- BananaPro_config`

Now you need to compile the bootloader:

`root `[`#`]`make ARCH=arm CROSS_COMPILE=armv7a-unknown-linux-gnueabihf-`

Lets put the booatloader in the boot partition. We do not have to, you can keep it anywhere, but it is nice to have it there, as it will always be with the device if it ever needs to be reloaded.

`root `[`#`]`cp u-boot-sunxi-with-spl.bin /mnt/bananapi/boot`

Burn the bootloader into the SD card:

** Warning**\
Make sure you are dd\'ing to the sdcard, if you dd to the drive of the computer you are currently using, it will wipe out your current bootloader and most probably NOT boot.

`root `[`#`]`dd if=/mnt/bananapi/boot/u-boot-sunxi-with-spl.bin of=/dev/sdX bs=1024 seek=8`

## [Script.bin]

You will now need to make the script.bin file. Once again you can use either the Linux-Sunxi or the LeMaker git repository. To make sure you are using the latest updated .fex file if using Linux-Sunxi get BananPi.fex or BananaPro.fex from the LeMaker repository.

For Sunxi:

`root `[`#`]`cd /mnt/bananapi-build/sunxi`

`root `[`#`]`git clone git://github.com/linux-sunxi/sunxi-tools.git`

For LeMaker:

`root `[`#`]`cd /mnt/bananapi-build/lemaker`

`root `[`#`]`git clone git://github.com/LeMaker/sunxi-boards.git`

To check for differences Banana Pi:

`root `[`#`]`diff /mnt/bananapi-build/lemaker/sunxi-boards/sys_config/a20/Bananapi.fex /mnt/bananapi-build/sunxi/sunxi-boards/sys_config/a20/Bananapi.fex`

To check for differences Banana Pro

`root `[`#`]`diff /mnt/bananapi-build/lemaker/sunxi-boards/sys_config/a20/BananaPro.fex /mnt/bananapi-build/sunxi/sunxi-boards/sys_config/a20/BananaPro.fex`

You can either append or copy over the Lemaker fex file to the Sunxi folder:

`root `[`#`]`cp /mnt/bananapi-build/lemaker/sunxi-boards/sys_config/a20/Banana* /mnt/bananapi-build/sunxi/sunxi-tools`

To build with Sunxi:

`root `[`#`]`cd sunxi/sunxi-tools`

To build with LeMaker:

`root `[`#`]`cd lemaker/sunxi-tools`

You will now need to make a change to the BananaPi.fex and BananaPro.fex files. No matter which repository you decide to use. Open the file and search for \"ctp_det_used\":

[FILE] **`BananaPi.fex`**

    Change
    from: ctp_det_used = 1
    to: ctp_det_used = 0cd sunxi-boards

[FILE] **`BananaPro.fex`**

    Change
    from: ctp_det_used = 1
    to: ctp_det_used = 0cd sunxi-boards

`root `[`#`]`make fex2bin`

For the Banana Pi

`root `[`#`]`fex2bin BananaPi.fex script.bin`

For the BananaPro

`root `[`#`]`fex2bin BananaPro.fex script.bin`

`root `[`#`]`cp script.bin /mnt/bananapi/boot`

## [Compile the Kernel]

`root `[`#`]`cd /mnt/bananapi-build/linux-sunxi`

`root `[`#`]`git clone -b sunxi-3.4 https://github.com/linux-sunxi/linux-sunxi.git`

To get started with a Sunxi kernel configuration use the sun7i_defconfig. Download the [sun7i_lemaker_defconfig](https://s3-us-west-2.amazonaws.com/sowis/bananapi/sun7i_lemaker_defconfig) which has more things selected, both are a good starting points depending on what all you want configured in the kernel.

`root `[`#`]`wget https://s3-us-west-2.amazonaws.com/sowis/bananapi/sun7i_lemaker_defconfig`

To use the sun71_lemaker_defconfig:

`root `[`#`]`cp sun71_lemaker_defconfig arch/arm/configs/`

Here is my custom config, some unnecessary things are turned off, while iptables and NFS are on as well as a few other common things were compiled into the kernel. Everything I needed is compiled into the kernel. There are a lot of modules selected, did not spend the time to go through and de-select every unneeded module. Simply did not compile the modules as they are not needed for my needs. [custom_bananapi_defconfig](https://s3-us-west-2.amazonaws.com/sowis/bananapi/custom_bananapi_defconfig)

`root `[`#`]`wget https://s3-us-west-2.amazonaws.com/sowis/bananapi/custom_bananapi_defconfig`

`root `[`#`]`cp custom_bananapi_defconfig arch/arm/configs`

There are a lot of things with the LeMaker config selected that are only needed if you intend on attaching various devices to the board. For a smaller kernel go ahead de-select the devices you will not be needing, and or add devices you will be using or other features/modules you want. You only need to modify one, or use one as is.

`root `[`#`]`nano arch/arm/configs/sun71_defconfig`

`root `[`#`]`nano arch/arm/configs/sun71_lemaker_defconfig`

`root `[`#`]`nano arch/arm/configs/custom_bananapi_defconfig`

\
If you prefer to use a GUI for configuring the kernel use one of the below:

  ------------
  menuconfig
  nconfig
  xconfig
  gconfig
  ------------

\
First load the bananapi kernel configuration choose only one!

`root `[`#`]`make ARCH=arm CROSS_COMPILE=armv7a-unknown-linux-gnueabihf- sun7i_defconfig`

`root `[`#`]`make ARCH=arm CROSS_COMPILE=armv7a-unknown-linux-gnueabihf- sun7i_lemaker_defconfig`

`root `[`#`]`make ARCH=arm CROSS_COMPILE=armv7a-unknown-linux-gnueabihf- custom_bananapi_defconfig`

Tweak the kernel configuration: Change nconfig to which ever is your favorite gui in the list above:

`root `[`#`]`make ARCH=arm CROSS_COMPILE=armv7a-unknown-linux-gnueabihf- nconfig`

Compile the Kernel:

`root `[`#`]`make ARCH=arm CROSS_COMPILE=armv7a-unknown-linux-gnueabihf- uImage modules`

Create Modules: Creating modules is not necessary if necessary features are compiled directly into the kernel, as with my custom config.

`root `[`#`]`make ARCH=arm CROSS_COMPILE=armv7a-unknown-linux-gnueabihf- INSTALL_MOD_PATH=output modules_install`

After the Kernel is finished compiling:

`root `[`#`]`cp arch/arm/boot/uImage /mnt/bananapi/boot`

Copy the modules over to the root file system: Replace XX with what ever the kernel number is: The modules will be placed in output/lib/moduels/3.4.XX the xx being what ever version the kernel has been bumped to, when the kernel and modules complete the version will be displayed:

`root `[`#`]`cp output/lib/modules/3.4.XX /mnt/bananapi/root/lib/modules/`

## [Final Boot File]

You will need to create a uEnv.txt file that will contain specific directions for the boot process:

`root `[`#`]`nano /mnt/bananapi/boot/uEnv.txt`

These settings have NO Memory Reserve. Which works fine for a headless setup. If you are going to be running a window manager or desktop, you will want to reserve some memory. Here is the link to the Linux-Sunxi [Kernel Arguments Page](https://linux-sunxi.org/Kernel_arguments) for some additional settings. What ever amount of memory is reserved, will not be available for general system use.

[FILE] **`/mnt/bananapi/boot/uEnv.txt`**

    bootargs=console=ttyS0,115200 console=tty0 sunxi_ve_mem_reserve=0 sunxi_g2d_mem_reserve=0 sunxi_no_mali_mem_reserve console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline rootwait
    aload_script=fatload mmc 0 0x43000000 script.bin;
    aload_kernel=fatload mmc 0 0x48000000 uImage; bootm 0x48000000;
    uenvcmd=run aload_script aload_kernel

## [Booting to an SATA SSD Disk]

Here are some hdparm results to show you why you want to use an ssd.

sdcard: root@bananapi \~ \# hdparm -Tt /dev/mmcblk0

/dev/mmcblk0:

    Timing cached reads:   726 MB in  2.00 seconds = 362.66 MB/sec
    Timing buffered disk reads:  48 MB in  3.02 seconds =  15.91 MB/sec

root@bananapi \~ \# hdparm -Tt /dev/sda

/dev/sda:

    Timing cached reads:   784 MB in  2.00 seconds = 391.21 MB/sec
    Timing buffered disk reads: 374 MB in  3.00 seconds = 124.60 MB/sec

It is not only the overall MB/sec but even more importantly the small file rate. Bonnie++, iozone, piozone tests have consistently shown on numerous arm devices that 4k,8k,16k read writes are much slower with an sdcard. A \$100 150MB/sec read capable sdcard will be NO faster. Next in speed is usb disk and internal emmc for those boards that have them. With SATA SSD far outstripping anything else.

[FILE] **`/mnt/bananapi/boot/uEnv.txt`**

    bootargs=console=ttyS0,115200 console=tty0 sunxi_ve_mem_reserve=0 sunxi_g2d_mem_reserve=0 sunxi_no_mali_mem_reserve console=tty1 root=/dev/sda1 rootfstype=ext4 elevator=deadline rootwait
    aload_script=fatload mmc 0 0x43000000 script.bin;
    aload_kernel=fatload mmc 0 0x48000000 uImage; bootm 0x48000000;
    uenvcmd=run aload_script aload_kernel

## [Finalizing in preparation for booting]

You will need to edit the make.conf and specifically set the correct [CFLAGS](https://wiki.gentoo.org/wiki/CFLAGS "CFLAGS") and [GCC-Optimization](https://wiki.gentoo.org/wiki/GCC_optimization "GCC optimization"), or certain functionality will not be possible. [Use Flags](https://www.gentoo.org/support/use-flags/) This is my make.conf, take note of the MAKEOPTS, and other settings specific to Distcc, you need to set some depending on whether you are using Distcc and how many total cpu\'s are avaialable, reference the [Distcc](https://wiki.gentoo.org/wiki/Distcc "Distcc") and [Distcc/Cross-Compiling](https://wiki.gentoo.org/wiki/Distcc/Cross-Compiling "Distcc/Cross-Compiling") documentation for details. Unless you intend upon using the [Overlay](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") and [eselect-repository](https://wiki.gentoo.org/wiki/Eselect-repository "Eselect-repository") packages, you should leave those commented out. Gentoo is very flexible, spend some time learning some of the things that can be done with it, you will eventually figure out what you need and do not need in the [make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf"). These make.conf settings have been very stable and efficient. Two Banana Pi devices withstood six months of pressure testing with various server configurations.

Here are some links to some details that might help you decide what the best CFLAGS may be. [Arm Cortex Processors & GCC](https://community.arm.com/groups/tools/blog/2013/04/15/arm-cortex-a-processors-and-gcc-command-lines) [Neon](https://www.arm.com/products/processors/technologies/neon.php) [DSP & SIMD](https://www.arm.com/products/processors/technologies/dsp-simd.php) [Neon Development Article](http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.dht0002a/BABIIFHA.html)

`root `[`#`]`nano /mnt/bananapi/root/etc/portage/make.conf`

[FILE] **`/mnt/bananapi/root/etc/portage/make.conf`**

    CFLAGS="-O2 -pipe -march=armv7-a -mfpu=neon-vfpv4 -ffast-math -mfloat-abi=hard"
    CXXFLAGS="-O2 -pipe -march=armv7-a -mfpu=neon-vfpv4 -ffast-math -mfloat-abi=hard"
    CHOST="armv7a-unknown-linux-gnueabihf"
    #MAKEOPTS="-j41 -l2"
    MAKEOPTS="-j1 -l2"
    USE="threads nptl nls bash-completion python udev -systemd"
    #FEATURES="distcc distcc-pump"
    PORTDIR="/usr/portage"
    DISTDIR="$/distfiles"
    PKGDIR="$/packages"
    FEATURES="$ buildpkg"
    EMERGE_DEFAULT_OPTS="$ --usepkg --binpkg-respect-use=y --binpkg-changed-deps=n"
    PORTAGE_ELOG_CLASSES="log warn error info"
    PORTAGE_ELOG_SYSTEM="echo:log,error,warn,info  save:log,error,warn,info syslog:log,error,warn,info"
    ACCEPT_LICENSE="*"

[FILE] **`/mnt/bananapi/root/etc/portage/package.use/00localization`**

    LINGUAS: en

Edit /mnt/bananapi/etc/shadow so root can login:

Get a hash output for the root password:

`root `[`#`]`openssl passwd -1`

`root `[`#`]`nano /mnt/bananapi/root/etc/shadow`

[FILE] **`/mnt/bananapi/root/etc/shadow`**

    root:<hash_output>:10770:0:::::

## [Optional]

If you are not going to have keyboard access and need access via SSH. dhcpcd is not installed so a static address will have to be set:

`root `[`#`]`nano /mnt/bananapi/root/etc/conf.d/net`

[FILE] **`/mnt/bananapi/root/etc/conf.d/net`**

    config_eth0="<your IP> netmask <your netmask> brd <network broadcast IP>"
    routes_eth0="default via <your router IP>"
    dns_servers_eth0="<nameserver IP> <another nameserver IP>"

The bare minimum will work for just getting in via ssh, edit [/mnt/bananapi/root/etc/conf.d/net]:

[FILE] **`/mnt/bananapi/root/etc/conf.d/net`**

    config_eth0="192.168.x.xxx netmask 255.255.255.0"

Edit /mnt/bananapi/root/etc/hostname:

[FILE] **`/mnt/bananapi/root/etc/hostname`**

    hostname="BananaPi"

Add net.eth0 to startup:

`root `[`#`]`cd /mnt/bananapi/root/etc/init.d `

`root `[`#`]`ln -s net.lo net.eth0 `

`root `[`#`]`cd /mnt/bananapi/root/etc/runlevels/default `

`root `[`#`]`ln -s /etc/init.d/net.eth0 `

Add sshd to startup:

`root `[`#`]`cd /mnt/bananapi/root/etc/runlevels/default `

`root `[`#`]`ln -s /etc/init.d/sshd `

Replace hwclock with swclock, so the OS gets a time on boot as it has no hardware clock:

`root `[`#`]`cd /mnt/bananapi/root/etc/runlevels/boot `

`root `[`#`]`unlink hwclock `

`root `[`#`]`ln -s /etc/init.d/swclock `

Set timezone - This will have to be set after your first boot:

`root `[`#`]`ls /usr/share/zoneinfo`

`root `[`#`]`echo "Your_Country/YOUR_TIMEZONE" > deploy/etc/timezone`

## [Plug in your sdcard and boot]

If all went well you should get a boot prompt.

## [][Tips & Tricks & Uses]

[NFS](https://wiki.gentoo.org/wiki/NFS "NFS") can be used to distribute binary packages to all Banana Pi devices on the network, or other Arm 7 devices that use the same [CFLAGS](https://wiki.gentoo.org/wiki/CFLAGS "CFLAGS"). The NFS server can be a Banana Pi or any other computer in your LAN. Preferably another computer as the 1 GBit/s network interface card is really only capable of 500-600 MBit/sec. [Bonding](https://wiki.gentoo.org/wiki/Handbook:Parts/Networking/Modular#Bonding "Handbook:Parts/Networking/Modular") can be used on your NFS server to help with good throughput. A one time setup of an NFS share to mount as your package directory will allow all devices to pull the binary packages without any manual distribution or intervention.

## [See also]

-   [Banana Pi](https://wiki.gentoo.org/wiki/Banana_Pi "Banana Pi")
-   [BeagleBone_Black](https://wiki.gentoo.org/wiki/BeagleBone_Black "BeagleBone Black")
-   [Cubox-i](https://wiki.gentoo.org/wiki/Cubox-i "Cubox-i") --- describes how to install Gentoo on the [SolidRun](https://www.solid-run.com/) Cubox-i and HummingBoard.
-   [Raspberry_Pi/Cross_building](https://wiki.gentoo.org/wiki/Raspberry_Pi/Cross_building "Raspberry Pi/Cross building") --- offload much of the heavy lifting for compilation to a more powerful build system
-   [Distcc/Cross-Compiling](https://wiki.gentoo.org/wiki/Distcc/Cross-Compiling "Distcc/Cross-Compiling") --- shows the reader how to set up distcc for cross-compiling across different processor architectures.