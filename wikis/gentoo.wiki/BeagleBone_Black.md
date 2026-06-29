**Resources**

[[]][Home](https://beagleboard.org/black)

[[]][Wikipedia](https://en.wikipedia.org/wiki/BeagleBoard#BeagleBone_Black "wikipedia:BeagleBoard")

## Contents

-   [[1] [Installing Gentoo on a Beaglebone Black Rev. C]](#Installing_Gentoo_on_a_Beaglebone_Black_Rev._C)
    -   [[1.1] [You will need]](#You_will_need)
    -   [[1.2] [Emerge the toolchain]](#Emerge_the_toolchain)
    -   [[1.3] [Create an overlay for crossdev]](#Create_an_overlay_for_crossdev)
    -   [[1.4] [Setup portage for crossdev]](#Setup_portage_for_crossdev)
    -   [[1.5] [Update manifest for local crossdev repository]](#Update_manifest_for_local_crossdev_repository)
    -   [[1.6] [Run Crossdev and let it setup a build environment]](#Run_Crossdev_and_let_it_setup_a_build_environment)
    -   [[1.7] [Configure U-Boot for the BBB]](#Configure_U-Boot_for_the_BBB)
    -   [[1.8] [Grab kernel configured specifically for the Beaglebone]](#Grab_kernel_configured_specifically_for_the_Beaglebone)
    -   [[1.9] [Create the root filesystem for the SD card]](#Create_the_root_filesystem_for_the_SD_card)
        -   [[1.9.1] [Optional]](#Optional)
    -   [[1.10] [Finish creating the root filesystem for the SD card]](#Finish_creating_the_root_filesystem_for_the_SD_card)
    -   [[1.11] [Format the MicroSD card the way BeagleBoard wants it]](#Format_the_MicroSD_card_the_way_BeagleBoard_wants_it)
    -   [[1.12] [Almost ready]](#Almost_ready)
    -   [[1.13] [Moment of truth]](#Moment_of_truth)
        -   [[1.13.1] [Optional follow-on]](#Optional_follow-on)
    -   [[1.14] [Tips and tricks]](#Tips_and_tricks)
        -   [[1.14.1] [boot options]](#boot_options)
        -   [[1.14.2] [modify the install]](#modify_the_install)
        -   [[1.14.3] [analog input]](#analog_input)
-   [[2] [Older Beaglebone versions]](#Older_Beaglebone_versions)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Installing Gentoo on a Beaglebone Black Rev. C]

These instructions are specifically for the Beaglebone Black Rev. C. This guide will utilize u-boot from the original sources and a modified 3.14.17 kernel from Beagleboard.org\'s github repo.

### [You will need]

-   USB -\> serial port debug connector so you can view boot errors, see the u-boot prompt if necessary, and not have to switch out HDMI cables on your monitor. More detail at [elinux.org](https://elinux.org/Beagleboard:BeagleBone_Black_Serial).
-   4GB micro SD card to create the Gentoo image (you can flash to NAND later).
-   An SD card

<!-- -->

    reader/writer to write the Gentoo image.

-   Create the udev rules mentioned [beagleboard.org](https://beagleboard.org/getting-started). These work for eudev as well.

### [Emerge the toolchain]

`root `[`#`]`emerge dev-vcs/git sys-devel/crossdev sys-fs/dosfstools app-arch/lzop `

Do not merge u-boot-tools as we will be using a version of u-boot configured specifically for the BBB (Beaglebone Black).

### [Create an overlay for crossdev]

`root `[`#`]`mkdir -p /usr/local/portage/ `

`root `[`#`]`echo "local_overlay" > /usr/local/portage/profiles/repo_name `

`root `[`#`]`echo "masters = gentoo" > /usr/local/portage/metadata/layout.conf `

`root `[`#`]`chown -R portage:portage /usr/local/portage `

edit /etc/portage/make.conf:

[FILE] **`/etc/portage/make.conf`**

    PORTDIR_OVERLAY="/usr/local/portage"

### [Setup portage for crossdev]

`root `[`#`]`mv -i package.use use && mkdir package.use && mv use package.use `

`root `[`#`]`mv -i package.accept_keywords accept_keywords && mkdir package.accept_keywords && mv accept_keywords package.accept_keywords `

`root `[`#`]`mv -i package.license license && mkdir package.license && mv license package.license `

`root `[`#`]`mv -i package.mask mask && mkdir package.mask && mv mask package.mask `

`root `[`#`]`mv -i package.keywords keywords && mkdir package.keywords && mv keywords package.keywords `

More info: [forums.gentoo.org](https://forums.gentoo.org/viewtopic-t-959774-start-0.html) and [wiki.gentoo.org](https://wiki.gentoo.org/wiki/Raspberry_Pi_Cross_building#crossdev "Raspberry Pi Cross building").

### [Update manifest for local crossdev repository]

-   If you get masked by corruption, it may be due to manifests not being built for the local portage overlay. Run the below.

`root `[`#`]`cd /usr/local/portage/cross-armv7a-hardfloat-linux-gnueabihf/ `

`root `[`#`]`for d in $(find -type l); do (cd $d; for f in $(find -type f -name "*.ebuild"); do (ebuild $f manifest); done); done `

### [Run Crossdev and let it setup a build environment]

-   I settled on the tuple: \"armv7a-hardfloat-linux-gnueabihf.\" TI recommends \"arm-linux-gnueabihf.\" [wiki.ti.com](http://processors.wiki.ti.com/index.php/Linux_Core_U-Boot_User%27s_Guide)

-   :::: cmd-box


    `user `[`$`]`crossdev -S -P -v -t armv7a-hardfloat-linux-gnueabihf`


    ::::

-   Test with:

    :::: cmd-box


    `user `[`$`]`armv7a-hardfloat-linux-gnueabihf-gcc --version`


    ::::

You should see binutils, gcc, glibc, linux-headers, and gdb under [/usr/local/portage/cross-armv7a-hardfloat-linux-gnueabihf] and stuff under [/usr/armv7a-hardfloat-linux-gnueabihf].

-   If you change your mind on the tuple, to uninstall the existing target run:

    :::: cmd-box


    `user `[`$`]`crossdev -C armv7a-hardfloat-linux-gnueabihf`


    ::::

### [Configure U-Boot for the BBB]

-   Note: [\[1\]](https://github.com/beagleboard/u-boot) is out-of-date, last commit is 3 years old.

-   make a build directory:

    :::: cmd-box


    `user `[`$`]`mkdir ~/bbb`


    ::::

-   grab latest stable from [denx.de](ftp://ftp.denx.de/pub/u-boot/), extract and `cd` to the extracted directory.

-   :::: cmd-box


    `root `[`#`]`make ARCH=arm CROSS_COMPILE=armv7a-hardfloat-linux-gnueabihf- am335x_boneblack_config`


    ::::

This article helped me find the correct make target: [crashcourse.ca](http://www.crashcourse.ca/wiki/index.php/U-Boot_on_the_BBB).

-   :::: cmd-box


    `user `[`$`]`make ARCH=arm CROSS_COMPILE=armv7a-hardfloat-linux-gnueabihf-`


    ::::

-   install mkimage so it\'s in your path. (As root)

    :::: cmd-box


    `root `[`#`]`install tools/mkimage /usr/local/bin`


    ::::

-   to test: `mkimage -V` should say 2014.07.

### [Grab kernel configured specifically for the Beaglebone]

-   Note: [https://github.com/beagleboard/kernel.git](https://github.com/beagleboard/kernel.git) is deprecated, but does still provide information on hardware support in each branch.

-   Robert C. Nelson keeps the main-line kernel patches in github. (git clone [https://github.com/RobertCNelson/bb-kernel](https://github.com/RobertCNelson/bb-kernel) -b \[version\] and follow instructions)

-   This one from beaglebone.org will build the firmware into the kernel under linux/firmware and includes patched sources. The older versions required you to run patch.sh, download the firmware manually, and drop it in the firmware folder.

-   Go to [github.com](https://github.com/beagleboard/linux.git) and decide which branch you want to check out. I settled on the latest long-term release kernel, 3.14.17.

-   :::: cmd-box


    `user `[`$`]`git clone -b 3.14 --single-branch `[`https://github.com/beagleboard/linux.git`](https://github.com/beagleboard/linux.git)


    ::::

If you get any GIT errors about not having [user.name] or [user.email], try this:

`user `[`$`]`git config --global user.email "asdf@gmail.com" `

`user `[`$`]`git config --global user.name "Username" `

-   check that you got the right kernel version.

    :::: cmd-box


    `user `[`$`]`cd linux; cat Makefile | head`


    ::::

and look at the top lines in Makefile:

[FILE] **`Makefile`**

    VERSION = 3
    PATCHLEVEL = 14
    SUBLEVEL = 17

-   copy bb.org config to [.config] by running the bb.org target:

    :::: cmd-box


    `user `[`$`]`make ARCH=arm CROSS_COMPILE=armv7a-hardfloat-linux-gnueabihf- bb.org_defconfig`


    ::::
-   If there\'s anything you want to tweak in the kernel, do so now with:

    :::: cmd-box


    `user `[`$`]`make ARCH=arm CROSS_COMPILE=armv7a-hardfloat-linux-gnueabihf- menuconfig`


    ::::
-   Compile the kernel:

    :::: cmd-box


    `user `[`$`]`make ARCH=arm CROSS_COMPILE=armv7a-hardfloat-linux-gnueabihf- -j8`


    ::::
-   Generate a uImage:

    :::: cmd-box


    `user `[`$`]`make ARCH=arm CROSS_COMPILE=armv7a-hardfloat-linux-gnueabihf- -j8 uImage dtbs LOADADDR=0x82000000`


    ::::

I have no idea why the LOADADDR is set to this, just following instructions from TI here: [wiki.ti.com](http://processors.wiki.ti.com/index.php/AM335x_U-Boot_User%27s_Guide). If you omit the `LOADADDR` you\'ll get a build error.

-   Compile kernel modules:

    :::: cmd-box


    `user `[`$`]`make ARCH=arm CROSS_COMPILE=armv7a-hardfloat-linux-gnueabihf- -j8 modules`


    ::::
-   make a directory for the kernel modules and install them:

    ::::: cmd-box


    `user `[`$`]`mkdir ~/bbb/linux_modules`





    `user `[`$`]`make ARCH=arm CROSS_COMPILE=armv7a-hardfloat-linux-gnueabihf- INSTALL_MOD_PATH=../linux_modules modules_install`


    :::::

### [Create the root filesystem for the SD card]

-   grab the latest Gentoo source from your mirror

[CODE]

    releases/arm/autobuilds/20140819/stage3-armv7a_hardfp-20140819.tar.bz2
    snapshots/portage-latest.tar.bz2

-   extract the tarballs:

`user `[`$`]`mkdir ~/bbb/deploy`

Add username for root paths:

`user `[`$`]`export user=$(whoami) `

As root, extract the stage3 since it will execute mknod:

`root `[`#`]`tar xjpf stage3-armv7a_hardfp-20121006.tar.bz2 -C /home/$/bbb/deploy`

As root, extract the portage snapshot:

`root `[`#`]`tar xjpf portage-latest.tar.bz2 -C /home/$/bbb/deploy/usr/`

-   Manually add files to root partition so u-boot will find them and boot your kernel.\

`user `[`$`]`cp ~/bbb/linux/arch/arm/boot/uImage ~/bbb/deploy/boot`

IMPORTANT: BBB will not boot without this file:

`user `[`$`]`cp ~/bbb/linux/arch/arm/boot/zImage ~/bbb/deploy/boot`

Copy the device tree blob:

`user `[`$`]`cp ~/bbb/linux/arch/arm/boot/dts/am335x-boneblack.dtb ~/bbb/deploy/boot`

Copy the kernel modules:

`user `[`$`]`cp -r ~/bbb/linux_modules/lib/modules ~/bbb/deploy/lib`

-   Make a directory where I can mount the boot partition under [/]

    :::: cmd-box


    `user `[`$`]`mkdir ~/bbb/deploy/boot/uboot`


    ::::

edit [\~/bbb/deploy/etc/fstab]:

[FILE] **`~/bbb/deploy/etc/fstab`**

    /dev/mmcblk0p2       /       ext4        noatime,errors=remount-ro   0 1
    /dev/mmcblk0p1      /boot/uboot auto        noatime             1 2

-   edit [\~/bbb/deploy/etc/shadow] so root can login:

    :::: cmd-box


    `root `[`#`]`openssl passwd -1`


    ::::

grab hash output, edit [deploy/etc/shadow], and put here:

[FILE] **`~/bbb/deploy/etc/shadow`**

    root:<hash_output>:10770:0:::::

-   edit [\~/bbb/deploy/etc/inittab] since everyone expects serial port to run at 115200 and have the name [ttyO0]

[FILE] **`~/bbb/deploy/etc/inittab`**

    s0:12345:respawn:/sbin/agetty -L 115200 ttyO0 vt100

#### [Optional]

-   setup a static IP on your BBB first, since we don\'t have dhcpcd installed: edit [\~/bbb/deploy/etc/conf.d/net].

[FILE] **`~/bbb/deploy/etc/conf.d/net`**

    config_eth0="<your IP> netmask <your netmask> brd <network broadcast IP>"
    routes_eth0="default via <your router IP>"
    dns_servers_eth0="<nameserver IP> <another nameserver IP>"

-   edit \~/bbb/deploy/etc/conf.d/hostname:\

[FILE] **`~/bbb/deploy/etc/conf.d/hostname`**

    hostname="beaglebone"

-   add net.eth0 to startup:

`root `[`#`]`cd /home/$/bbb/deploy/etc/init.d; ln -s net.lo net.eth0 `

`root `[`#`]`cd /home/$/bbb/deploy/etc/runlevels/default; ln -s /etc/init.d/net.eth0 `

-   replace hwclock with swclock. BBB does not have a built-in hardware clock so setting based on last modified date is the next best thing.

`root `[`#`]`cd /home/$/bbb/deploy/etc/runlevels/boot `

`root `[`#`]`unlink hwclock `

`root `[`#`]`ln -s /etc/init.d/swclock . `

-   Set timezone (can\'t finish until system is up and running).

`root `[`#`]`ls /usr/share/zoneinfo `

`root `[`#`]`echo "America/YOUR_TIMEZONE" > /home/$/deploy/etc/timezone `

### [Finish creating the root filesystem for the SD card]

-   tar it all up:

`root `[`#`]`cd /home/$/bbb/deploy `

`root `[`#`]`tar cvzpf ../deploy.tar.gz . `

### [Format the MicroSD card the way BeagleBoard wants it]

-   Similar scripts: [github.com/beagleboard](https://github.com/beagleboard/image-builder/blob/master/tools/setup_sdcard.sh), [dev.gentoo.org](http://dev.gentoo.org/~armin76/arm/beaglebone/mkcard.sh), [omappedia.org](http://omappedia.org/wiki/Minimal-FS_SD_Configuration).
-   I chose a modified version of TI\'s from here: [downloads.ti.com](http://downloads.ti.com/dsps/dsps_public_sw/psp/LinuxPSP/AM335x_04_06/04_06_00_08/index_FDS.html). Original is under host-tools/mksd-am335x.sh.

Sfdisk devs having not played nice I([User:GovanifY](https://wiki.gentoo.org/index.php?title=User:GovanifY&action=edit&redlink=1 "User:GovanifY (page does not exist)")) adapted the formatting without CHS, as any implementation has been deemed useless and so removed. Please tell me if anything bad happens without the CHS settings!

-   Use \'lsblk\' to verify your sd device id. If through an sd card reader it might be mmcblk0 with partitions mmcblk0p1 & p2. If this is the case alter the script before hand to use \"\$1\"p1 and \"\$1\"p2 instead of \"\$1\"1 & \"\$1\"2.

[FILE] **`host-tools/mksd-am335x.sh`**

    #!/bin/bash

    #Text parsing WON'T WORK unless it is in english
    export LC_ALL=C
    if [[ -z $1 || -z $2 || -z $3 || -z $4 ]]
    then
        echo "mksd-am335x Usage:"
        echo "  mksd-am335x <device> <MLO> <u-boot.img> <uImage> <rootfs tar.gz >"
        echo "  Example: mksd-am335x /dev/sdc MLO u-boot.img uImage nfs.tar.gz"
        exit
    fi
    if ! [[ -e $2 ]]
    then
        echo "Incorrect MLO location!"
        exit
    fi
    if ! [[ -e $3 ]]
    then
        echo "Incorrect u-boot.img location!"
        exit
    fi
    if ! [[ -e $4 ]]
    then
        echo "Incorrect uImage location!"
        exit
    fi
    if ! [[ -e $5 ]]
    then
        echo "Incorrect rootfs location!"
        exit
    fi

    echo "All data on "$1" now will be destroyed! Continue? [y/n]"
    read ans
    if ! [ $ans == 'y' ]
    then
        exit
    fi

    echo "[Partitioning $1...]"

    DRIVE=$1
    dd if=/dev/zero of=$DRIVE bs=1024 count=1024

    SIZE=`fdisk -l $DRIVE | grep Disk | awk ''`

    echo DISK SIZE - $SIZE bytes

    CYLINDERS=`echo $SIZE/255/63/512 | bc`

    echo CYLINDERS - $CYLINDERS
     | sfdisk $DRIVE

    echo "[Making filesystems...]"

    mkfs.vfat -F 32 -n boot "$1"1 &> /dev/null
    # the "-T small" is so I have enough inodes for portage
    mkfs.ext4 -L rootfs -T small "$1"2 &> /dev/null

    echo "[Copying files...]"

    mount "$1"1 /mnt/sdcard
    cp $2 /mnt/sdcard/MLO
    cp $3 /mnt/sdcard/u-boot.img
    umount "$1"1

    mount "$1"2 /mnt/sdcard
    tar zxvf $5 -C /mnt/sdcard
    chmod 755 /mnt/sdcard
    umount "$1"2

    echo "[Done]"

-   Run the script to format the SD card. All data will be lost on it.\

`root `[`#`]`mkdir /mnt/sdcard`

plugin your SD card and check dmesg for the name of your SD card: mine was [/dev/sdf].

You will probably have to manually umount the sdcard if Linux automounts it. The script will complain if the SD card is mounted.

(as root)\

`root `[`#`]`cd /home/$/bbb; ./mksd-am335x.sh /dev/sdf u-boot-2014.07/MLO u-boot-2014.07/u-boot.img linux/arch/arm/boot/uImage deploy.tar.gz`

-   Don\'t pull out the card until the light on the SD-Card reader stops flashing, even if the script has stopped. I guess it takes awhile for the journal to catch up. Check `df -kh` (and watch it go down in size, weird) and `dmesg` for more info and possible errors. I have seen `INFO: task umount:2515 blocked for more than 120 seconds.` messages before and it will still be blinking. When it\'s done the reader light should stay illuminated.

### [Almost ready]

-   Emerge a serial terminal emulator like PuTTY, etc.
-   Create a profile with these settings:\

[CODE] **Terminal Profile Settings**

    /dev/ttyUSB0
    speed(baud):  115200
    data bits:    8
    stop bits:    1
    parity:       none
    flow control: none

-   Open your serial terminal window with this profile.
-   Connect your serial debug cable to the BBB as described here: [elinux.org](https://elinux.org/Beagleboard:BeagleBone_Black_Serial).
-   Insert your SD card into the BBB.
-   Hold down the button closest to the SD card and press the button closest to the Ethernet port once. More info: [elinux.org](https://elinux.org/Beagleboard:BeagleBoneBlack#BeagleBone_Black_Connector_and_Switch_Locations).

### [Moment of truth]

-   You should see a Gentoo prompt! Thank God!

#### [Optional follow-on]

-   you should now have a running system and network connectivity

    ::::: cmd-box


    `root `[`#`]`date MMDDhhmmYYYY`





    `root `[`#`]`emerge --config sys-libs/timezone-data`


    :::::
-   Time will start from this point on next time you boot:

    ::::: cmd-box


    `root `[`#`]`touch /sbin/rc`





    `root `[`#`]`emerge --sync`


    :::::

### [Tips and tricks]

#### [boot options]

If you want to override boot options without messing with uEnv.txt, make sure you compile your kernel with Boot options-\>Kernel command line type: \"Always use the default kernel command string,\" or `CONFIG_CMDLINE_FORCE=y`. Then edit the Default kernel command string as desired.

You can create a [/boot/uEnv.txt] and override u-boot settings if you want. I couldn\'t figure this out so please add this info if you can.

#### [modify the install]

If you just need to tweak u-boot or kernel files:

`root `[`#`]`mount /dev/sdf1 /mnt/p1; mount /dev/sdf2 /mnt/p2; `

`root `[`#`]`cp /home/$/bbb/u-boot-2014.07/ /mnt/p1 `

`root `[`#`]`cp /home/$/bbb/linux/arch/arm/boot/ /mnt/p2 `

If you need to dump a new root file structure to the SD card. Be very careful here, don\'t want to replace your root filesystem with ARM junk.

`root `[`#`]`mount /dev/sdf2 /mnt/sdcard `

`root `[`#`]`rm -rf /mnt/sdcard/* `

`root `[`#`]`cd /home/$/bbb `

`root `[`#`]`tar xzvpf deploy.tar.gz -C /mnt/sdcard `

#### [analog input]

To get the analog input (AIN) working, make sure you have the `CONFIG_MFD_TI_AM335X_TSCADC` kernel option enabled (used linux-3.8-beaglebone). Also, to active this, perform the following after you boot to load them and find where they were put:

`root `[`#`]`echo BB-ADC > /sys/devices/bone_capemgr.8/slots `

`root `[`#`]`find /sys/ -name AIN* `

## [Older Beaglebone versions]

The installation procedure also works for the Beaglebone aka Beaglebone white (see [beagleboard.org](https://beagleboard.org/bone)). This was tested with revision A6a. Instead of the am335x-boneblack.dtb the am335x-bone.dtb has to be used.

## [See also]

-   [BeagleBone](https://wiki.gentoo.org/wiki/BeagleBone "BeagleBone")
-   [Embedded_Handbook/Boards/BeagleBone Black](https://wiki.gentoo.org/wiki/Embedded_Handbook/Boards/BeagleBone_Black "Embedded Handbook/Boards/BeagleBone Black")

## [External resources]

-   [BeagleBone Black](https://www.elinux.org/BeagleBoneBlack) on elinux.org
-   [BeagleBone Black: Analog Input Pins](http://embedded-basics.blogspot.com/2014/10/beaglebone-black-analog-input-pins.html) on embedded-basics.blogspot.com