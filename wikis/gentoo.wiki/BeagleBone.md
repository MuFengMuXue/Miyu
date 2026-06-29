**Resources**

[[]][Home](https://beagleboard.org/bone-original)

[[]][Wikipedia](https://en.wikipedia.org/wiki/BeagleBoard#BeagleBone "wikipedia:BeagleBoard")

Installing Gentoo in the BeagleBone is pretty simple if you\'re already a Gentoo user. You need to use an SD card, at least of 2 GB of size. If you are familiar with the Gentoo Linux installation process, there is not much different here.

## Contents

-   [[1] [Requirements]](#Requirements)
-   [[2] [Preparation]](#Preparation)
    -   [[2.1] [Overview]](#Overview)
    -   [[2.2] [Emerging needed tools]](#Emerging_needed_tools)
    -   [[2.3] [Build a crosscompiler]](#Build_a_crosscompiler)
    -   [[2.4] [Obtain and build U-Boot]](#Obtain_and_build_U-Boot)
    -   [[2.5] [Obtain and build a kernel]](#Obtain_and_build_a_kernel)
-   [[3] [SD card setup]](#SD_card_setup)
    -   [[3.1] [Overview]](#Overview_2)
    -   [[3.2] [Formatting the SD card]](#Formatting_the_SD_card)
    -   [[3.3] [Configure U-Boot]](#Configure_U-Boot)
    -   [[3.4] [Copy U-Boot, MLO, and the kernel to the SD card]](#Copy_U-Boot.2C_MLO.2C_and_the_kernel_to_the_SD_card)
-   [[4] [Installing Gentoo]](#Installing_Gentoo)
    -   [[4.1] [Overview]](#Overview_3)
    -   [[4.2] [Stages information]](#Stages_information)
    -   [[4.3] [Extracting a stage3]](#Extracting_a_stage3)
    -   [[4.4] [Extract a Portage snapshot (optional)]](#Extract_a_Portage_snapshot_.28optional.29)
    -   [[4.5] [Setup fstab]](#Setup_fstab)
    -   [[4.6] [Set the default root password]](#Set_the_default_root_password)
    -   [[4.7] [Setup hostname and networking]](#Setup_hostname_and_networking)
    -   [[4.8] [Enabling SSH access (optional)]](#Enabling_SSH_access_.28optional.29)
    -   [[4.9] [Enabling serial console access (optional)]](#Enabling_serial_console_access_.28optional.29)
    -   [[4.10] [Finishing the installation]](#Finishing_the_installation)
-   [[5] [Booting the system]](#Booting_the_system)
    -   [[5.1] [Accessing the console (optional)]](#Accessing_the_console_.28optional.29)
-   [[6] [After booting]](#After_booting)
    -   [[6.1] [Keeping the clock up to date]](#Keeping_the_clock_up_to_date)
-   [[7] [Special thanks]](#Special_thanks)
-   [[8] [See also]](#See_also)
-   [[9] [External resources]](#External_resources)

## [Requirements]

To be able to install Gentoo, you\'ll need the following:

-   An x86/amd64 based PC with Gentoo and an SD card reader on it.
-   A BeagleBone.
-   One SD card (2 GB is enough).
-   A network connection.

## [Preparation]

### [Overview]

Before we start the installation process, we need to get/build a kernel, bootloader and X-Loader for the BeagleBone.

The BeagleBone doesn\'t have a NAND/flash device, so the bootloader (U-Boot) needs to be located on the SD card, along with X-Loader and the kernel.

### [Emerging needed tools]

For building the stuff needed to boot our BeagleBone, we need the following tools emerged on the host system where we\'re going to build them.

-   [[[dev-vcs/git]](https://packages.gentoo.org/packages/dev-vcs/git)[]] - To download U-Boot, X-Loader and the kernel.
-   [[[sys-devel/crossdev]](https://packages.gentoo.org/packages/sys-devel/crossdev)[]] - To create a crosscompiler.
-   [[[dev-embedded/u-boot-tools]](https://packages.gentoo.org/packages/dev-embedded/u-boot-tools)[]] - To create a kernel image U-Boot can understand.
-   [[[sys-fs/dosfstools]](https://packages.gentoo.org/packages/sys-fs/dosfstools)[]] - To create FAT32 filesystems.

`root `[`#`]`emerge --ask dev-vcs/git sys-devel/crossdev dev-embedded/u-boot-tools sys-fs/dosfstools`

### [Build a crosscompiler]

Build a crosscompiler:

`root `[`#`]`crossdev -S armv7a-hardfloat-linux-gnueabi`

### [Obtain and build U-Boot]

Obtain U-Boot:

`root `[`#`]`wget `[`ftp://ftp.denx.de/pub/u-boot/u-boot-2012.10-rc3.tar.bz2`](ftp://ftp.denx.de/pub/u-boot/u-boot-2012.10-rc3.tar.bz2)` `

`root `[`#`]`tar xjpf u-boot-2012.10-rc3.tar.bz2 && cd u-boot-* `

Compile U-Boot:

`root `[`#`]`make ARCH=arm CROSS_COMPILE=armv7a-hardfloat-linux-gnueabi- am335x_evm_config `

`root `[`#`]`make ARCH=arm CROSS_COMPILE=armv7a-hardfloat-linux-gnueabi- `

### [Obtain and build a kernel]

For booting the BeagleBone we need a kernel. The vanilla kernel.org doesn\'t support the BeagleBone as of October 2012, for this reason we\'ll use a kernel provided by TI.

Obtain the kernel:

`root `[`#`]`git clone `[`git://arago-project.org/git/projects/linux-am33x.git`](git://arago-project.org/git/projects/linux-am33x.git)` `

`root `[`#`]`cd linux-am33x `

`root `[`#`]`git checkout -f v3.2-staging `

Or use the following if you are only interested in the last revision of this branch:

`root `[`#`]`git clone --depth 1 --branch v3.2-staging --single-branch `[`git://arago-project.org/git/projects/linux-am33x.git`](git://arago-project.org/git/projects/linux-am33x.git)

Obtain needed firmware:

`root `[`#`]`# wget "`[`http://arago-project.org/git/projects/?p=am33x-cm3.git;a=blob_plain;f=bin/am335x-pm-firmware.bin;hb=HEAD`](http://arago-project.org/git/projects/?p=am33x-cm3.git;a=blob_plain;f=bin/am335x-pm-firmware.bin;hb=HEAD)`" -O firmware/am335x-pm-firmware.bin`

Configure the kernel:

`root `[`#`]`make ARCH=arm CROSS_COMPILE=armv7a-hardfloat-linux-gnueabi- am335x_evm_defconfig`

Run menuconfig for enable ext4 support:

`root `[`#`]`make ARCH=arm CROSS_COMPILE=armv7a-hardfloat-linux-gnueabi- menuconfig`

Enable ext4 as built-in:

[KERNEL]

    File systems --->
       <*>The Extended 4 (ext4) filesystem

Enable devtmpfs support for newer systems:

[KERNEL] **Enabling devtmpfs support**

    Device Drivers --->
      Generic Driver Options --->
        [*] Maintain a devtmpfs filesystem to mount at /dev
        [*]   Automount devtmpfs at /dev, after the kernel mounted the rootfs

The kernel includes CPU frequency scaling support, but by default is configured to use the userspace governor, that means that unless you have any CPU frequency scaling manager in the rootfs, the cpu will be stuck at 600MHz.

You can change the governor anytime you want, but if you are like me and prefer the ondemand governor set by default, which makes a CPU frequency scaling manager redundant, or if you prefer the performance governor which is like disabling CPU frequency scaling, you can choose the default governor in the following kernel config menu.

Set the default governor in menuconfig:

[KERNEL]

    Code Listing 3.8: Configuring the default governor in menuconfig
    CPU Power Management --->
       CPU Frequency Scaling --->
          Default CPUFreq governor (userspace)  --->

Cross-compile the kernel (replace `9` in the command with an appropriate number of cores on the build computer):

`root `[`#`]`make -j9 ARCH=arm CROSS_COMPILE=armv7a-hardfloat-linux-gnueabi- uImage`

Depending on the gcc version used in your cross compiler, this might not work. The 3.2-staging kernel is not intended to work with gcc-5, but you can create a separate cross compiler with gcc-4. Look at the options in `crossdev -h` for information on how to specify this. To keep this running next to your existing cross compiler, you can call it `armv7a-gcc4-linux-gnueabi` for example and change the make command accordingly.

Also, when using gcc-4.9.4, you need one patch to prevent a build error:

`root `[`#`]`wget "https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git/patch/kernel/timeconst.pl?id=fab58c4dc8da9983c88357da7455955e1fa05c38" -O fix-timeconst-error.patch `

`root `[`#`]`git apply fix-timeconst-error.patch `

Once it gets built we\'ll have a kernel image on arch/arm/boot/uImage.

## [SD card setup]

### [Overview]

OMAP-based systems need a special setup of the SD card to boot from it. For more information please check [this link](http://omappedia.org/wiki/Minimal-FS_SD_Configuration).

### [Formatting the SD card]

The following script will format your SD card accordingly, creating two partitions. The first partition size is based on the size of the SD card itself, and it\'s formatted in vfat. The second partition is the free space left on the card after the first partition, and it\'s formatted in ext4.

Format the SD card:

`root `[`#`]`wget `[`http://dev.gentoo.org/~armin76/arm/beaglebone/mkcard.sh`](http://dev.gentoo.org/~armin76/arm/beaglebone/mkcard.sh)

Replace `mmcblk0` in the command below with the name SD card device. When using a USB-based SD card reader, the card may show up as a [/dev/sd\*] device, for example [/dev/sdd].

`root `[`#`]`bash mkcard.sh /dev/mmcblk0`

### [Configure U-Boot]

The default configuration of U-Boot differs a bit from our setup, we fix that by creating a file called [uEnv.txt] with the following contents:

[FILE] **`uEnv.txt`**

    bootfile=uImage
    loaduimage=run loaduimagefat; run mmcboot

### [][Copy U-Boot, MLO, and the kernel to the SD card]

Now we\'ll mount the first partition on the card and copy the needed files (the ones that we built before) to boot our BeagleBone.

`root `[`#`]`mkdir /mnt/p1 ; mount /dev/mmcblk0p1 /mnt/p1 `

`root `[`#`]`cp uEnv.txt /mnt/p1 `

`root `[`#`]`cp u-boot-2012.10-rc3/ /mnt/p1 `

`root `[`#`]`cp linux-am33x/arch/arm/boot/uImage /mnt/p1 `

## [Installing Gentoo]

### [Overview]

The installation on this device is a bit different, and therefore easy, as we can\'t install Gentoo on it by booting an installation environment. For installing Gentoo (and any other distro, really) you need to put the SD card on your PC and prepare there the minimal installation.

What we\'ll have to do to setup our installation is:

1.  Extract stage3 to the 2nd partition of the SD card
2.  Extract portage snapshot (required to emerge things and ntp(see below))
3.  Setup fstab
4.  Setup root password
5.  Configure hostname and networking (optional, but recommended)
6.  Enable SSH access (optional, but recommended)
7.  Enable serial console access (optional, but recommended)

### [Stages information]

Here\'s some information about the stages.

-   Architecture: arm
-   Subarchitecture: armv7a_hardf
-   CHOST: armv7a-hardfloat-linux-gnueabi
-   Profile: default/linux/arm/10.0

We\'ll be using the new EABI, also called gnueabi. That is armel on Debian.

Therefore, we need an armv7a-hardfloat-linux-gnueabi stage3 for best performance, available under the releases/arm/autobuilds directory in your [favorite mirror](https://gentoo.org/downloads/mirrors/).

Optionally grab a Portage snapshot.

### [Extracting a stage3]

Mount the second partition of the SD card and extract the stage3 you downloaded.

Mount the partition and extracting the stage3:

`root `[`#`]`mkdir /mnt/p2 `

`root `[`#`]`mount /dev/mmcblk0p2 /mnt/p2 `

`root `[`#`]`tar xjpf stage3-armv7a_hardfp-20121006.tar.bz2 -C /mnt/p2 `

### [][Extract a Portage snapshot (optional)]

Extract the snapshot:

`root `[`#`]`tar xjpf portage-latest.tar.bz2 -C /mnt/p2/usr`

### [Setup fstab]

Edit the [/mnt/p2/etc/fstab] file to look like this:

[FILE] **`/mnt/p2/etc/fstab`**

    # NOTE: If your BOOT partition is ReiserFS, add the notail option to opts.
    /dev/mmcblk0p1      /boot       vfat        noauto,noatime  1 2
    /dev/mmcblk0p2      /       ext4        noatime     0 1

If they exist, remove (or comment out) the following lines since this system does not have a swap partition, CD-ROM, or floppy:

[FILE] **`/mnt/p2/etc/fstab`**

    /dev/SWAP     none        swap        sw      0 0
    /dev/cdrom      /mnt/cdrom  auto        noauto,ro   0 0
    #/dev/fd0       /mnt/floppy auto        noauto      0 0

### [Set the default root password]

This is the most important part of the installation. As without the root password we won\'t be able to login!

For setting the password, we need to be able to run passwd. However that\'s not possible since our PC can\'t run ARM binaries. Therefore we need to modify the file that contains the passwords ([/etc/shadow]) inside the chroot, so we can set a default root password.

Generate a password:

`root `[`#`]`openssl passwd -1`

Open the shadow file:

`root `[`#`]`nano -w /mnt/p2/etc/shadow`

Replace the first line with the following line (where `password` is the output from the [openssl] command above):

[FILE] **`/mnt/p2/etc/shadow`**

    root:password:14698:0:::::

### [Setup hostname and networking]

Please read the network configuration chapter of the ARM handbook to configure the network.

### [][Enabling SSH access (optional)]

We can add [sshd] to the startup of our system so we can access our BeagleBone using [ssh]. Add [sshd] to the startup:

`root `[`#`]`ln -sf /etc/init.d/sshd /mnt/p2/etc/runlevels/default`

### [][Enabling serial console access (optional)]

By default the ttyS0 port is configured at 9600 bps. However, almost all of the ARM devices run the serial port at 115200 bps. Also, in the case of the BeagleBone, the port is ttyO0(that is a t-t-y-capitalO-zero) instead of the normal ttyS0. So this should be added to the [/etc/inittab] file. Replace `9600` with `115200` on the ttyS0 line, and replace `ttyS0` with `ttyO0`.

`root `[`#`]`nano -w /mnt/p2/etc/inittab`

[FILE] **`/etc/inittab`**

    s0:12345:respawn:/sbin/agetty 115200 ttyO0 vt100

### [Finishing the installation]

Let\'s unmount the SD card:

`root `[`#`]`umount /mnt/p1 /mnt/p2`

This is pretty much all of the installation. It is highly recommended readers of this guide read all the recommendations of the handbook.

## [Booting the system]

### [][Accessing the console (optional)]

If you want to see the BeagleBone boot, connect an USB cable to the mini USB port (you should have it if you aren\'t powering it using an external PSU\...) and load the `ftdi_sio` kernel module with the following command:

`root `[`#`]`modprobe ftdi_sio vendor=0x0403 product=0xa6d0`

In newer kernels, the ftdi_sio module requires a different interaction:

`root `[`#`]`modprobe ftdi_sio`

`root `[`#`]`echo "0403 a6d0" > /sys/bus/usb-serial/drivers/ftdi_sio/new_id`

New devices called ttyUSB0 and ttyUSB1 should show up on /dev. You should use ttyUSB1 with a terminal emulator like [picocom](https://wiki.gentoo.org/wiki/Picocom "Picocom") or [minicom](https://wiki.gentoo.org/wiki/Minicom "Minicom") configuring it with 115200bps 8N1

Once you have the card ready, put it into the Beaglebone\... and you should be able to boot it.

## [After booting]

### [Keeping the clock up to date]

One of the problems of the BeagleBone is that it doesn\'t save the date because it doesn\'t have a battery for the clock.

After logging into our new Gentoo on Beaglebone installation, I\'d recommend setting a date and emerging [[[net-misc/ntp]](https://packages.gentoo.org/packages/net-misc/ntp)[]] to keep the clock up-to-date. Also it\'s recommended to put both [ntp-client] and [ntpd] to boot on startup, so you get a proper date setup.

However, keep in mind that NTP requires a network connection and a NTP server being reachable, either on the local network or on the Internet.

`root `[`#`]`emerge --ask net-misc/ntp`

`root `[`#`]`rc-update add ntpd default `

`root `[`#`]`rc-update add ntp-client default `

`root `[`#`]`service ntpd start `

`root `[`#`]`service ntp-client start `

## [Special thanks]

-   [https://beagleboard.org/bone](https://beagleboard.org/bone) for providing me a Beaglebone to document and support Gentoo on it
-   Siarhei Siamashka (ssvb) for giving helpful hints

## [See also]

-   [BeagleBone Black](https://wiki.gentoo.org/wiki/BeagleBone_Black "BeagleBone Black")
-   [BeagleBone (Embedded Handbook)](https://wiki.gentoo.org/wiki/Embedded_Handbook/Boards/BeagleBone "Embedded Handbook/Boards/BeagleBone")

## [External resources]

-   [BeagleBone](https://www.elinux.org/BeagleBone) on elinux.org

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Raúl Porcel ( [Raúl Porcel (armin76) ](https://wiki.gentoo.org/wiki/User:Armin76 "User:Armin76"))**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*