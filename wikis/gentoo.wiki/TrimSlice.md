[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Home](http://trimslice.com/web/pr-110124)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Trim-Slice "wikipedia:Trim-Slice")

This guide shows how to install Gentoo on the TrimSlice. Consult the Embedded Handbook for [supplementary information about the TrimSlice hardware](https://wiki.gentoo.org/wiki/Embedded_Handbook/Boards/TrimSlice "Embedded Handbook/Boards/TrimSlice"). Furthermore it\'s possible to [migrate the TrimSlice to mainline U-Boot](https://wiki.gentoo.org/wiki/Trimslice_U-Boot "Trimslice U-Boot").

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Requirements]](#Requirements)
-   [[3] [Preparing to install your TrimSlice]](#Preparing_to_install_your_TrimSlice)
    -   [[3.1] [Overview]](#Overview_2)
    -   [[3.2] [Emerging needed tools]](#Emerging_needed_tools)
    -   [[3.3] [Build a crosscompiler]](#Build_a_crosscompiler)
-   [[4] [Obtaining/Building a kernel]](#Obtaining.2FBuilding_a_kernel)
-   [[5] [Creating the boot script]](#Creating_the_boot_script)
-   [[6] [SD card setup]](#SD_card_setup)
    -   [[6.1] [Overview]](#Overview_3)
    -   [[6.2] [Creating the partition table and formatting the SD card]](#Creating_the_partition_table_and_formatting_the_SD_card)
    -   [[6.3] [Copying the kernel to the SD card]](#Copying_the_kernel_to_the_SD_card)
-   [[7] [Installing Gentoo]](#Installing_Gentoo)
    -   [[7.1] [Overview]](#Overview_4)
    -   [[7.2] [Stages information]](#Stages_information)
    -   [[7.3] [Extracting a stage3]](#Extracting_a_stage3)
    -   [[7.4] [Extracting a portage snapshot (optional)]](#Extracting_a_portage_snapshot_.28optional.29)
    -   [[7.5] [Setup fstab]](#Setup_fstab)
    -   [[7.6] [Setting the default root password]](#Setting_the_default_root_password)
    -   [[7.7] [Setup hostname and networking]](#Setup_hostname_and_networking)
    -   [[7.8] [Enabling SSH access (optional)]](#Enabling_SSH_access_.28optional.29)
    -   [[7.9] [Enabling serial console access (optional)]](#Enabling_serial_console_access_.28optional.29)
    -   [[7.10] [Finishing the installation]](#Finishing_the_installation)
-   [[8] [Booting up our new system]](#Booting_up_our_new_system)
-   [[9] [After booting]](#After_booting)
    -   [[9.1] [OpenRC]](#OpenRC)
-   [[10] [Accelerated graphics drivers]](#Accelerated_graphics_drivers)
    -   [[10.1] [Overview]](#Overview_5)
    -   [[10.2] [Tegra overlay]](#Tegra_overlay)
    -   [[10.3] [Emerging the accelerated graphics driver]](#Emerging_the_accelerated_graphics_driver)
-   [[11] [External resources]](#External_resources)
-   [[12] [Special thanks]](#Special_thanks)

## [Overview]

Installing Gentoo in the TrimSlice is pretty simple if you\'re already a Gentoo user. You need to use an SD card, at least of 2 GB of size. If you are familiar with the Gentoo Linux installation process, there is not much different here.

** Warning**\
Please keep in mind that this guide was tested on the TrimSlice devkit, so bluetooth and wifi support are out of the scope of this guide since the devkit lacks those.

## [Requirements]

To be able to install Gentoo, you\'ll need the following:

-   An **[x86]**/**[amd64]** based PC with Gentoo and an SD card reader on it.
-   A TrimSlice.
-   One SD card (2 GB is enough).
-   A network connection.

## [Preparing to install your TrimSlice]

### [Overview]

Before we start the installation process, we need to get/build a kernel for the TrimSlice.

### [Emerging needed tools]

For building the stuff needed to boot our TrimSlice, we need the following tools emerged on the host system where we\'re going to build them.

-   [[[sys-devel/crossdev]](https://packages.gentoo.org/packages/sys-devel/crossdev)[]] - To create a crosscompiler.
-   [[[dev-embedded/u-boot-tools]](https://packages.gentoo.org/packages/dev-embedded/u-boot-tools)[]] - to create a kernel image U-Boot can understand.

`root `[`#`]`emerge --ask sys-devel/crossdev dev-embedded/u-boot-tools`

### [Build a crosscompiler]

Building a crosscompiler:

`root `[`#`]`crossdev -S armv7a-unknown-linux-gnueabi`

## [][Obtaining/Building a kernel]

For booting the TrimSlice we need a kernel. The vanilla kernel.org doesn\'t have all the drivers, etc needed for the TrimSlice yet. Therefore we\'ll use the kernel maintained by Compulab (the company behind TrimSlice).

Compulab\'s git tree is available at [http://gitorious.org/trimslice-kernel](http://gitorious.org/trimslice-kernel). On this guide we\'ll be using the `1.01-upstream` branch:

`root `[`#`]`wget `[`http://gitorious.org/trimslice-kernel/trimslice-kernel/archive-tarball/trimslice/1.01-upstream`](http://gitorious.org/trimslice-kernel/trimslice-kernel/archive-tarball/trimslice/1.01-upstream)

Extract and change to the kernel sources directory:

`root `[`#`]`tar zxvf 1.01-upstream && cd trimslice-kernel-trimslice-kernel`

Configure the kernel:

`root `[`#`]`make ARCH=arm trimslice_defconfig`

At this point [make menuconfig] could be ran to customize the kernel further.

Cross-compiling the kernel (replace `9` with the number of cores you have in the local computer):

`root `[`#`]`make -j9 ARCH=arm CROSS_COMPILE=armv7a-unknown-linux-gnueabi- uImage`

Once it gets built we\'ll have a kernel image on arch/arm/boot/uImage.

## [Creating the boot script]

Since we\'re using an SD card to do our install, we\'ll have to create a boot script that U-Boot will read from the SD card upon startup so it knows where to load the kernel from and the specific parameters to boot from SD.

Create a file called [boot.script] with the following contents:

[FILE] **`boot.script`**

    setenv bootargs 'root=/dev/mmcblk0p1 rw rootwait console=tty1 console=ttyS0,115200n8 mem=384M@0M mem=512M@512M nvmem=128M@384M vmalloc=248M nohdparm noinitrd init=/sbin/init rootwait loglevel=8 video=tegrafb'
    ext2load mmc 0:1 4080000 /boot/uImage
    bootm 4080000

Now we need to convert it to a format U-Boot can understand. Converting boot.script to boot.scr:

`root `[`#`]`mkimage -A arm -T script -C none -n "TrimSlice boot script" -d boot.script boot.scr`

This will generate a file called [boot.scr] that contains the commands U-Boot will execute upon starting. We\'ll copy that file to the [/boot] directory.

## [SD card setup]

### [Overview]

We\'ll just create a partition that uses all the space on the card.

** Warning**\
I\'ve been told that most of the USB SD card readers display the SD card as an [/dev/sd\*] device, so make sure you modify the parameters i mention as [/dev/mmcblk0] accordingly.

### [Creating the partition table and formatting the SD card]

First we need to create the partition table on the SD card. This will erase all the contents on the card, so make sure you don\'t have any important data on it.

`root `[`#`]`fdisk /dev/mmcblk0`

    Command (m for help): o

    Command (m for help): n
    Command action
       e   extended
       p   primary partition (1-4)
    p
    Partition number (1-4, default 1): 1
    First sector (2048-15654911, default 2048): (Hit enter)
    Using default value 2048
    Last sector, +sectors or +size (2048-15654911, default 15654911): (Hit enter)
    Using default value 15654911

    Command (m for help): w

Now format the new partition:

`root `[`#`]`mkfs.ext3 -i 4096 /dev/mmcblk0p1`

### [Copying the kernel to the SD card]

Now mount the first partition on the card and copy the needed files (the ones that we built before) to boot the TrimSlice. Copy the kernel to the SD card:

`root `[`#`]`mkdir /mnt/p1 ; mount /dev/mmcblk0p1 /mnt/p1 ; mkdir /mnt/p1/boot `

`root `[`#`]`cp boot.scr /mnt/p1/boot `

`root `[`#`]`cp arch/arm/boot/uImage /mnt/p1/boot `

## [Installing Gentoo]

### [Overview]

The installation on this device is a bit different, and therefore easy, as we can\'t install Gentoo on it by booting an installation environment. For installing Gentoo (and any other distro, really) you need to put the SD card on your PC and prepare there the minimal installation.

What we\'ll have to do to setup our installation is:

1.  Extract stage3 to the 1st partition of the SD card.
2.  Extract portage snapshot (required to emerge things and ntp(see below)).
3.  Setup [/etc/fstab].
4.  Setup root password.
5.  Configure hostname and networking (optional, but recommended).
6.  Enable SSH access (optional, but recommended).
7.  Enable serial console access (optional, but recommended).

### [Stages information]

Here\'s some information about the stages.

-   Architecture: arm
-   Subarchitecture: armv7a
-   `CHOST`: `armv7a-unknown-linux-gnueabi`
-   Profile: default/linux/arm/10.0
-   We\'ll be using the new EABI, also called gnueabi. That is `armel` on Debian.

Therefore, we need an armv7a-unknown-linux-gnueabi stage3 for best performance, available under the releases/arm/autobuilds directory in favorite Gentoo mirror.

Optionally you can also grab a Portage snapshot.

### [Extracting a stage3]

Extract the downloaded stage3:

`root `[`#`]`tar xjpf stage3-armv7a-20101118.tar.bz2 -C /mnt/p1`

### [][Extracting a portage snapshot (optional)]

Extracting the snapshot:

`root `[`#`]`tar xjpf portage-latest.tar.bz2 -C /mnt/p1/usr`

### [Setup fstab]

Edit the [/mnt/p1/etc/fstab] file to look like this:

[FILE] **`/mnt/p2/etc/fstab`**

    # (This is the important part)
    # NOTE: If your BOOT partition is ReiserFS, add the notail option to opts.
    /dev/mmcblk0p1      /       ext3        noatime     0 1

    # (Remove the following lines as we don't have SWAP, cdrom, or floppy)
    /dev/SWAP       none        swap        sw      0 0
    /dev/cdrom      /mnt/cdrom  auto        noauto,ro   0 0
    #/dev/fd0       /mnt/floppy auto        noauto      0 0

### [Setting the default root password]

This is the most important part of the installation. As without the root password we won\'t be able to login!

For setting the password, we need to be able to run [passwd]. However that is not possible since our PC cannot run ARM binaries. Therefore we need to modify the file that contains the passwords ([/etc/shadow]) inside the chroot, so we can [set a default root password](https://wiki.gentoo.org/wiki/Setting_a_default_root_password "Setting a default root password"). Since passwords may not be stored in plaintext use openssl to convert the password:

`user `[`$`]`openssl passwd -6`

    Password:
    Verifying - Password:
    $6$I9Q9AyTL$Z76H7wD8mT9JAyrp/vaYyFwyA5wRVN0tze8pvM.MqScC7BBm2PU7pLL0h5nSxueqUpYAlZTox4Ag2Dp5vchjJ0

In this example the string corresponds to the password \"gentoo\".

`root `[`#`]`openssl passwd -1`

The resulting string needs to be placed in [TARGET/etc/shadow]. Fire up your editor:

`root `[`#`]`nano -w /mnt/p1/etc/shadow`

Now replace the line beginning with `root:` with the line shown below, substituting [SHADOW_COMMAND_OUTPUT] with the string provided by the [openssl] command above.

[FILE] **`/etc/shadow`**

    root:SHADOW_COMMAND_OUTPUT:14698:0:::::

For example, this line makes the password be \"gentoo\":

[FILE] **`/etc/shadow`**

    root:$6$I9Q9AyTL$Z76H7wD8mT9JAyrp/vaYyFwyA5wRVN0tze8pvM.MqScC7BBm2PU7pLL0h5nSxueqUpYAlZTox4Ag2Dp5vchjJ0:14698:0:::::

### [Setup hostname and networking]

Please read the [network configuration chapter](https://wiki.gentoo.org/index.php?title=Network_configuration_chapter&action=edit&redlink=1 "Network configuration chapter (page does not exist)") of the ARM handbook to configure the network.

### [][Enabling SSH access (optional)]

Add [sshd] to the startup of the system to access the TrimSlice using [ssh]. When using OpenRC, run:

`root `[`#`]`ln -s /mnt/p1/etc/init.d/sshd /mnt/p1/etc/runlevels/default`

### [][Enabling serial console access (optional)]

By default the ttyS0 port is configured at 9600 bps. However, almost all of the ARM devices run the serial port at 115200 bps. So this should be added to the [/etc/inittab] file:

`root `[`#`]`nano -w /mnt/p1/etc/inittab`

Replace `9600` with `115200` on the `ttyS0` line:

[FILE] **`/mnt/p1/etc/inittab`**

    s0:12345:respawn:/sbin/agetty 115200 ttyS0 vt100

### [Finishing the installation]

Let\'s unmount the SD card:

`root `[`#`]`umount /mnt/p1`

** Note**\
This may take a while depending the speed of the SD card

This is pretty much all of the installation. I\'d highly recommend that you read all the recommendations of the handbook.

## [Booting up our new system]

Once you have the card ready, put it into the TrimSlice\... and you should be able to boot it.

## [After booting]

One of the problems of the TrimSlice is that it doesn\'t save the date because it doesn\'t have a battery for the clock.

After logging into our new Gentoo on TrimSlice installation, I\'d recommend setting a date and emerging [[[net-misc/ntp]](https://packages.gentoo.org/packages/net-misc/ntp)[]] to keep the clock up-to-date. Also it\'s recommended to put both ntp-client and ntpd to boot on startup, so you get a proper date setup.

However, keep in mind that NTP requires a network connection and a NTP server being reachable, either on the local network or on the Internet.

`root `[`#`]`emerge --ask net-misc/ntp`

### [OpenRC]

Put both [ntp-client] and [ntpd] in the boot runlevel on startup:

`root `[`#`]`rc-update add ntpd default `

`root `[`#`]`rc-update add ntp-client default `

Start ntp-client and ntpd:

`root `[`#`]`/etc/init.d/ntp-client start `

`root `[`#`]`/etc/init.d/ntpd start `

## [Accelerated graphics drivers]

### [Overview]

The TrimSlice has a graphic chip that needs a binary driver provided by Nvidia for accelerated graphics. Those can be found on the overlay below.

### [Tegra overlay]

I\'ve created an overlay for providing ebuilds for installing the accelerated graphics drivers and libraries that are available on the Nvidia L4T.

The overlay is available in the official Gentoo overlays repository: [http://git.overlays.gentoo.org/gitweb/?p=proj/tegra.git;a=summary](http://git.overlays.gentoo.org/gitweb/?p=proj/tegra.git;a=summary).

Please check the official documentation about [using overlays](https://wiki.gentoo.org/wiki/Project:Overlays/User_Guide "Project:Overlays/User Guide").

### [Emerging the accelerated graphics driver]

Once you\'ve added the overlay to your list of overlays, you can emerge the drivers:

`root `[`#`]`emerge --ask --verbose tegra-drivers`

## [External resources]

-   [Trimslice.com](http://trimslice.com/)
-   [Trimslice.com forum](http://www.trimslice.com/forum/)

## [Special thanks]

-   [Trimslice.com](http://trimslice.com/) for providing me a TrimSlice devkit to document and support Gentoo on it.
-   Siarhei Siamashka ([ssvb ](https://wiki.gentoo.org/index.php?title=User:Ssvb&action=edit&redlink=1 "User:Ssvb (page does not exist)")) for giving helpful hints.

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Raúl Porcel ([armin67 ](https://wiki.gentoo.org/index.php?title=User:Armin67&action=edit&redlink=1 "User:Armin67 (page does not exist)"))**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*