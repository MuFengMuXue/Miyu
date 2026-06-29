**Resources**

[[]][Home](http://www.pandaboard.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Pandaboard "wikipedia:Pandaboard")

The **Pandaboard** is an ARMv7 architecture single board computer based on a Texas Instruments OMAP4430 SOC (System On Chip) @ 1GHz. A later model, the **Pandaboard ES** include an OMAP4460 clocked @ 1.2GHz.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Requirements]](#Requirements)
    -   [[1.2] [Preparation]](#Preparation)
    -   [[1.3] [Hardware]](#Hardware)
    -   [[1.4] [SD card setup]](#SD_card_setup)
    -   [[1.5] [Unpack stage3 and portage]](#Unpack_stage3_and_portage)
    -   [[1.6] [Bootloader and kernel]](#Bootloader_and_kernel)
        -   [[1.6.1] [Using the Ubuntu kernel]](#Using_the_Ubuntu_kernel)
        -   [[1.6.2] [Using the mainline kernel]](#Using_the_mainline_kernel)
        -   [[1.6.3] [kernel config]](#kernel_config)
        -   [[1.6.4] [uImage]](#uImage)
        -   [[1.6.5] [zImage]](#zImage)
        -   [[1.6.6] [Kernel modules]](#Kernel_modules)
        -   [[1.6.7] [Install the bootloader and kernel]](#Install_the_bootloader_and_kernel)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [fstab]](#fstab)
    -   [[2.2] [Setting a password]](#Setting_a_password)
    -   [[2.3] [Boot script]](#Boot_script)
    -   [[2.4] [Network configuration]](#Network_configuration)
    -   [[2.5] [Clock and time]](#Clock_and_time)
    -   [[2.6] [SSH access]](#SSH_access)
    -   [[2.7] [Serial terminal]](#Serial_terminal)
    -   [[2.8] [Finishing up]](#Finishing_up)
-   [[3] [Post installation]](#Post_installation)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)
-   [[6] [Special thanks]](#Special_thanks)

## [Installation]

Installing Gentoo a Pandaboard is quite simple for anyone with some experience installing Gentoo. An SD card is required with at least 2 GB size. If the goal is to have a self hosting Gentoo installation, a minimum of 8 GB is recommended. A Gentoo install on a Pandaboard with a base system and compiled kernel (as of 2015) can be around 4 GB. This can balloon very quickly so if a desktop enviroment installation is planned, a card with more capacity is highly recommended as the Pandaboard can accommodate SD cards up to 32 GB. Anyone familiar with the Gentoo Linux installation process would find that it is not much different from a regular installation, however, if building on an amd64 or other PC there are extra steps required thereby having to cross compile the kernel and bootloader for the ARMv7 architecture. Also there is the issue of not being able to natively run some of the binaries necessary in a normal installation because of the differing architecture. There are some workarounds to this as described through the article.

### [Requirements]

To be able to install Gentoo, the following are required:

-   A machine with Gentoo and an SD card reader on it
-   A Pandaboard or Pandaboard ES
-   One SD card at least 2 GB, preferably 8 GB or larger
-   A network connection

### [Preparation]

The installation on this device is a bit different, and therefore maybe not so easy as a regular installation, as it is not possible to install Gentoo on it by booting an installation environment. For installing Gentoo (and any other distro, really) a host system is required to prepare a minimal installation on the SD card.

The basic steps to set up the installation are:

1.  Prepare the SD card
2.  Extract stage3 to the 2nd partition of the SD card
3.  Extract portage snapshot (required to emerge things and ntp(see below))
4.  Cross compile and install the bootloader (U-boot) and kernel
5.  Setup fstab
6.  Setup root password
7.  Configure hostname and networking (optional, but recommended)
8.  Enable SSH access (optional, but recommended)
9.  Enable serial console access (optional, but recommended)

### [Hardware]

** Important**\
As stated above, the hardware listed in the following commands might not match the hardware in each Pandaboard verbatim. Use the following information as a hardware reference guide.

The Pandaboard has the following specifications:

-   OMAP4430 @ 1GHz
-   PowerVR SGX540 graphics
-   1 GB LPDDR2 RAM
-   WiLink 6.0 Wireless (wl12xx Linux module)

`root `[`#`]`lsusb`

    Bus 001 Device 003: ID 0424:ec00 Standard Microsystems Corp. SMSC9512/9514 Fast Ethernet Adapter
    Bus 001 Device 002: ID 0424:9514 Standard Microsystems Corp. SMC9514 Hub

### [SD card setup]

OMAP-based systems need a special setup of the SD card to boot from it. For more information please check this link. (TODO: Find the broken link..)

The following script will format an SD card accordingly, creating two partitions. The first partition size is based on the size of the SD card itself, and it is formatted in vfat. The second partition is the free space left on the card after the first partition, and it is formatted in ext4.

`user `[`$`]`wget `[`http://dev.gentoo.org/~armin76/arm/pandaboard/mkcard.sh`](http://dev.gentoo.org/~armin76/arm/pandaboard/mkcard.sh)

** Warning**\
This will overwrite the contents of the [/dev/mmcblk0] device. Make sure a backup has been performed of the card before continuing, if there is any valuable data on it

Be sure to replace `mmcblk0` in the command below with the name of the SD card device

`root `[`#`]`bash mkcard.sh /dev/mmcblk0`

Now mount the partitions on the card in preparation to install Gentoo to the Pandaboard.

`root `[`#`]`mkdir -p /mnt/gentoo `

`root `[`#`]`mount /dev/mmcblk0p2 /mnt/gentoo `

`root `[`#`]`mkdir /mnt/gentoo/boot `

`root `[`#`]`mount /dev/mmcblk0p1 /mnt/gentoo/boot `

### [Unpack stage3 and portage]

The unpacking of the stage3 and portage is much the same as a regular Gentoo installation.

Here\'s some information about the stages.

       Architecture: arm
       Subarchitecture: armv7a
       CHOST: armv7a-hardfloat-linux-gnueabi
       Profile: default/linux/arm/13.0

The new EABI is used, also called gnueabi along with hardfloat. That is armhf on Debian.

Therefore, an [armv7a-hardfloat-linux-gnueabi] stage3 is needed for best performance, available under the [releases/arm/autobuilds] directory in a preferred Gentoo mirror. The armv7a_hardfp stage3 is the required download.

Optionally, also grab a portage snapshot

Extract the stage3 and snapshot, this may take a while. (Adjust the tarball name accordingly)

`root `[`#`]`tar xjpf stage3-armv7a_hardfp-20101118.tar.bz2 -C /mnt/gentoo `

`root `[`#`]`tar xjpf portage-latest.tar.bz2 -C /mnt/gentoo/usr `

### [Bootloader and kernel]

A kernel and a bootloader for the Pandaboard need to be fetched and built to boot the Pandaboard.

The Pandaboard doesn\'t have a NAND/flash device, so the bootloader (U-Boot) needs to be located on the SD card, along with the kernel.

For building the required software needed to boot the Pandaboard, the following tools are emerged on the host system.

-   [[[sys-devel/crossdev]](https://packages.gentoo.org/packages/sys-devel/crossdev)[]] - For creating a crosscompiler to compile the kernel and U-Boot
-   [[[dev-embedded/u-boot-tools]](https://packages.gentoo.org/packages/dev-embedded/u-boot-tools)[]] - This includes mkimage which creates boot.scr and kernel/ramdisk images that U-Boot can understand
-   [[[sys-fs/dosfstools]](https://packages.gentoo.org/packages/sys-fs/dosfstools)[]] - The Pandaboard requires the first SD card partition to have a FAT based filesystem

`root `[`#`]`emerge --ask sys-devel/crossdev dev-embedded/u-boot-tools sys-fs/dosfstools `

`root `[`#`]`crossdev -S armv7a-hardfloat-linux-gnueabi `

`user `[`$`]`wget `[`ftp://ftp.denx.de/pub/u-boot/u-boot-latest.tar.bz2`](ftp://ftp.denx.de/pub/u-boot/u-boot-latest.tar.bz2)` `

`user `[`$`]`tar xjpf u-boot-latest.tar.bz2 && cd u-boot-* `

`user `[`$`]`make ARCH=arm CROSS_COMPILE=armv7a-hardfloat-linux-gnueabi- omap4_panda_config `

`user `[`$`]`make ARCH=arm CROSS_COMPILE=armv7a-hardfloat-linux-gnueabi- `

#### [Using the Ubuntu kernel]

Originally the vanilla kernel.org wasn\'t as tested as the one used on Ubuntu. TI decided to provide support to Ubuntu, so it makes sense to have all the fixes Ubuntu have by using their kernel.

If the following link returns a 404 not found error, download the latest [.tar.gz] file from the precise distribution in the following link, the latest stable kernel version will be labeled \"security, updates (main)\". [https://launchpad.net/ubuntu/+source/linux-ti-omap4](https://launchpad.net/ubuntu/+source/linux-ti-omap4)

Fetch the Linux Kernel for the Pandaboard from Ubuntu precise distribution:

`user `[`$`]`wget '`[`https://launchpad.net/ubuntu/+archive/primary/+files/linux-ti-omap4_3.2.0-1472.93.tar.gz'`](https://launchpad.net/ubuntu/+archive/primary/+files/linux-ti-omap4_3.2.0-1472.93.tar.gz')

Extract the kernel sources and change to the directory, the given example is for the Ubuntu kernel, modify for the version being used:

`user `[`$`]`tar zxvf linux-ti-omap4_3.2.0-1472.93.tar.gz && cd ubuntu-precise`

The default kernel config for this kernel version is really minimal, and doesn\'t have support for wifi or accelerated graphics drivers. Gentoo developer [Raúl Porcel (armin76) ](https://wiki.gentoo.org/wiki/User:Armin76 "User:Armin76") provided a basic kernel config along with the original Gentoo on Pandaboard documentation for reference.

`user `[`$`]`wget `[`http://dev.gentoo.org/~armin76/arm/pandaboard/kconfig`](http://dev.gentoo.org/~armin76/arm/pandaboard/kconfig)` -O .config`

After downloading the kconfig, update and customize it:

`user `[`$`]`make ARCH=arm CROSS_COMPILE=armv7a-hardfloat-linux-gnueabi- oldconfig menuconfig`

#### [Using the mainline kernel]

Another option is using the mainline kernel sources. Using the mainline kernel may have newer features but may also lack support for hardware 3D and/or DSP acceleration.

The mainline (vanilla-sources) kernel can be found at [https://www.kernel.org/pub/linux/kernel/](https://www.kernel.org/pub/linux/kernel/)

Fetch the mainline kernel:

`user `[`$`]`wget '`[`https://www.kernel.org/pub/linux/kernel/v4.x/linux-4.2.5.tar.xz'`](https://www.kernel.org/pub/linux/kernel/v4.x/linux-4.2.5.tar.xz')

Extract the kernel source and change to the directory, modify versions to suit:

`user `[`$`]`tar zxvf linux-4.2.5.tar.xz && cd linux-4.2.5`

Create a default config and customize it:

`root `[`#`]`make ARCH=arm CROSS_COMPILE=armv7a-hardfloat-linux-gnueabi- omap2plus_defconfig menuconfig`

#### [kernel config]

[KERNEL] **Kernel Options relevant for Pandaboard**

    Device Drivers  --->
      [*] Network device support  --->
        <M>   USB Network Adapters  --->
          <M>     SMSC LAN95XX based USB 2.0 10/100 ethernet devices
        [*]   Wireless LAN  --->
          [*]   TI Wireless LAN support  --->
            <M>   TI wl12xx support

#### [uImage]

This section describes cross-compiling a legacy u-boot uImage

Replace 9 with the number of cores there are on the host computer:

`user `[`$`]`make -j9 ARCH=arm CROSS_COMPILE=armv7a-hardfloat-linux-gnueabi- uImage`

If the command fails due to no `LOADADDR` being specified add the required parameter to the [make] command. This usually needs to be set when compiling a mainline kernel [uImage] target.

`user `[`$`]`make -j9 ARCH=arm CROSS_COMPILE=armv7a-hardfloat-linux-gnueabi- LOADADDR=0x82000000 uImage`

Once the build is complete there will be a kernel image at [arch/arm/boot/uImage]

#### [zImage]

This section describes cross-compiling a zImage, u-boot can now boot this.

`user `[`$`]`make -j9 ARCH=arm CROSS_COMPILE=armv7a-hardfloat-linux-gnueabi- zImage`

Once the build is complete there will be a kernel image at [arch/arm/boot/zImage]

#### [Kernel modules]

Compile and install the kernel modules, installing to the mounted root on the SD card.

`user `[`$`]`make -j9 ARCH=arm CROSS_COMPILE=armv7a-hardfloat-linux-gnueabi- INSTALL_MOD_PATH=/mnt/gentoo modules modules_install`

#### [Install the bootloader and kernel]

Now copy the needed u-boot bootloader and Linux kernel files (the ones that were built before) to boot the Pandaboard.

`root `[`#`]`cp u-boot-*/MLO /mnt/gentoo/boot `

`root `[`#`]`cp u-boot-*/u-boot.img /mnt/gentoo/boot `

`root `[`#`]`cp "$linux-source"/arch/arm/boot/uImage /mnt/gentoo/boot `

`root `[`#`]`cp "$linux-source"/arch/arm/boot/dts/omap4-panda.dtb /mnt/gentoo/boot `

## [Configuration]

### [fstab]

The file [/etc/fstab] needs to be set up to configure the root filesystem, and optionally a mount point [/boot] so it\'s possible to mount it and copy new boot files there in the future.

Edit the fstab similarly:

`root `[`#`]`$EDITOR /mnt/gentoo/etc/fstab`

[FILE] **`/mnt/gentoo/etc/fstab`**

    # This is the important part
    # NOTE: If the BOOT partition is ReiserFS, add the notail option to opts.
    /dev/mmcblk0p1      /boot       vfat        noauto,noatime  1 2
    /dev/mmcblk0p2      /       ext4        noatime     0 1

    # Comment or remove the following lines if there is no SWAP, cdrom, or floppy
    #/dev/SWAP      none        swap        sw      0 0
    #/dev/cdrom     /mnt/cdrom  auto        noauto,ro   0 0
    #/dev/fd0       /mnt/floppy auto        noauto      0 0

### [Setting a password]

This is one of the most important parts of the installation. As without the root password it will not be possible to login!

For setting the password, the [passwd] command has to be executed. However that\'s not possible since an x86/amd64 or other architecture PC can\'t run ARM binaries. Therefore, another way has to be chosen to modify the file that contains the passwords ([/etc/shadow]) inside the chroot, so it is possible to set a default root password.

(Generate a password)

`user `[`$`]`openssl passwd -1`

`root `[`#`]`$EDITOR /mnt/gentoo/etc/shadow`

Replace the root user password similarly to the example given below. The secret is the second field which needs to be substituted with the output the [openssl] command returned. In these two examples, the last line sets the password to \"gentoo\".

[FILE] **`/mnt/gentoo/etc/shadow`**

    root:s3cr3t:14698:0:::::
    ---8<---
    root:$6$I9Q9AyTL$Z76H7wD8mT9JAyrp/vaYyFwyA5wRVN0tze8pvM.MqScC7BBm2PU7pLL0h5nSxueqUpYAlZTox4Ag2Dp5vchjJ0:14698:0:::::

### [Boot script]

TODO: explain preEnv.txt uEnv.txt

To boot the Pandaboard, a boot script is needed along with the [mkimage] command to create the file [boot.scr]. This file is read by U-Boot in the boot process and can contain extra commands and environment configuration. It is possible to add any linux command line options here necessary for the boot process, such as a different location of the root filesystem.

Some examples of U-Boot boot.scr files (delete as appropriate in future)

Example for uImage and fdt without initramfs. For booting without an initramfs there needs to be a minus \"-\" as second argument to bootm or bootz commands, in place where the ramdisk address would usually be.

`root `[`#`]`$EDITOR /mnt/gentoo/boot/boot.txt`

[FILE] **`/mnt/gentoo/boot/boot.txt`**

    fatload mmc 0:1 $ uImage
    fatload mmc 0:1 $ omap4-panda.dtb
    setenv bootargs earlyprintk console=ttyO2,115200n8 root=/dev/mmcblk0p2 rootwait
    bootm $ - $

Example for zImage and fdt with ramdisk

`root `[`#`]`$EDITOR /mnt/gentoo/boot/boot.txt`

[FILE] **`/mnt/gentoo/boot/boot.txt`**

    fatload mmc 0:1 $ zImage
    fatload mmc 0:1 $ uInitrd
    fatload mmc 0:1 $ omap4-panda.dtb
    setenv bootargs earlyprintk console=ttyO2,115200n8 root=/dev/mmcblk0p2 rootwait
    bootz $ $ $

Create [boot.scr] with [mkimage] provided by u-boot-tools

`root `[`#`]`mkimage -A arm -T script -C none -n "Gentoo Pandaboard boot script" -d /mnt/gentoo/boot/boot.txt /mnt/gentoo/boot/boot.scr`

Create a ramdisk with mkimage (optional?)

`root `[`#`]`mkimage -A arm -O linux -T ramdisk -n "Gentoo Pandaboard ramdisk" -d /mnt/gentoo/boot/theinitramfs /mnt/gentoo/boot/uInitrd`

### [Network configuration]

Please read the network configuration chapter of the ARM handbook to configure the network.

### [Clock and time]

One of the problems the Pandaboard has, is that it doesn\'t have a battery to save the clock time. To mitigate this, on Gentoo there is an option in the init system called [swclock] which sets the date of the system upon boot from a last modified date of a file.

`root `[`#`]`ln -sf /etc/init.d/swclock /mnt/gentoo/etc/runlevels/boot`

[hwclock] has to be removed from the startup because it sets the date from the RTC, which is 2000-01-01 upon startup and overrides swclock\'s date.

`root `[`#`]`rm /mnt/gentoo/etc/runlevels/boot/hwclock`

[swclock] uses the [/lib/rc/cache/shutdowntime]\'s modification time to set the date, therefore update it to have the current date and time.

`root `[`#`]`touch /mnt/gentoo/lib/rc/cache/shutdowntime`

Although this doesn\'t fix the issue, at least helps to set a sane date and time. Consider using NTP, documented in the next chapter

### [SSH access]

If SSH is required, add sshd to the startup of the system so it\'s possible to administrate the Pandaboard from over the network.

`root `[`#`]`ln -sf /etc/init.d/sshd /mnt/gentoo/etc/runlevels/default`

### [Serial terminal]

By default the ttyS0 port is configured at 9600 bps. However, almost all of the ARM devices run the serial port at 115200 bps. Also, in the case of the Pandaboard, the port is ttyO2 instead of the normal ttyS0. So this should be added to the [/etc/inittab] file:

`root `[`#`]`nano -w /mnt/gentoo/etc/inittab`

Comment out or remove the lines containing ttyS\* and add a new line replacing 9600 with 115200 and ttyS0 with ttyO2

[FILE] **`/mnt/gentoo/etc/inittab`**

    # SERIAL CONSOLES
    #s0:12345:respawn:/sbin/agetty -L 9600 ttyS0 vt100
    #s1:12345:respawn:/sbin/agetty -L 9600 ttyS1 vt100
    s0:12345:respawn:/sbin/agetty 115200 ttyO2 vt100

### [Finishing up]

Unmount the SD card, when the contents have finished writing it is safe to remove. This may take a while depending the speed of the SD card.

`root `[`#`]`umount /mnt/gentoo/boot /mnt/gentoo`

## [Post installation]

This is pretty much all of the installation. It is highly recommended to read all the recommendations of the handbook.

Once the card is ready, put it into the Pandaboard and it should be able to boot.

One of the problems of the Pandaboard is that it doesn\'t save the date because it doesn\'t have a battery for the clock.

After logging into the new Gentoo on Pandaboard installation, is it recommended setting a date and emerging net-misc/ntp to keep the clock up-to-date. Also it\'s recommended to put both [ntp-client] and [ntpd] to boot on startup, so a proper date and time is set.

However, keep in mind that NTP requires a network connection and a NTP server being reachable, either on the local network or on the Internet.

Emerge ntp, start both ntp-client and ntpd and add them to the default runlevel on booting:

`root `[`#`]`emerge net-misc/ntp `

`root `[`#`]`rc-update add ntpd default `

`root `[`#`]`rc-update add ntp-client default `

`root `[`#`]`/etc/init.d/ntp-client start `

`root `[`#`]`/etc/init.d/ntpd start `

The Pandaboard has integrated hardware that needs either a driver, firmware or tools to work. Making work such hardware is documented on the following page:

TODO: (find links again..)

## [See also]

-   [TrimSlice](https://wiki.gentoo.org/wiki/TrimSlice "TrimSlice") - An **[arm]** embedded board.

## [External resources]

## [Special thanks]

-   Raúl Porcel for writing the original Pandaboard GuideXML documentation
-   pandaboard.org for providing a Pandaboard to document and support Gentoo on it
-   Jordi Inglés, who gave an 8 GB SDHC for the project
-   Siarhei Siamashka (ssvb) for giving helpful hints
-   Michał Majchrowicz for checking the doc in the Pandaboard ES
-   Daniel Díaz
-   Steev for being a great help and converting the GuideXML to HTML
-   calculus for giving someone an urge to migrate the document to the wiki

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Raúl Porcel ([armin67 ](https://wiki.gentoo.org/index.php?title=User:Armin67&action=edit&redlink=1 "User:Armin67 (page does not exist)"))**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*