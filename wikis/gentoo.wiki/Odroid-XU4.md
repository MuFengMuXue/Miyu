[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Home](https://wiki.odroid.com/odroid-xu4/odroid-xu4)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Odroid "wikipedia:Odroid")

This article is a step by step guide on getting a fully functional Gentoo distribution of GNU/Linux on Odroid-XU4. It will begin with assuming the user has done nothing to the XU4 and assuming that the XU4 has internet access to it. The guide will walk through how to install Gentoo from another OS onto another partition, then configuring the bootloader (U-Boot) to boot off of that partition. This guide is based off of [Installation alternatives](https://wiki.gentoo.org/wiki/Installation_alternatives#Installing_Gentoo_from_an_existing_Linux_distribution "Installation alternatives") article.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Cross-compiling from a Gentoo machine]](#Cross-compiling_from_a_Gentoo_machine)
        -   [[2.1.1] [ARM toolchain]](#ARM_toolchain)
        -   [[2.1.2] [Bootloader installation]](#Bootloader_installation)
        -   [[2.1.3] [Partitioning]](#Partitioning)
        -   [[2.1.4] [Kernel installation]](#Kernel_installation)
        -   [[2.1.5] [Bootloader configuration]](#Bootloader_configuration)
        -   [[2.1.6] [Stage3 installation]](#Stage3_installation)
        -   [[2.1.7] [System cross-configuration]](#System_cross-configuration)
        -   [[2.1.8] [First boot]](#First_boot)
        -   [[2.1.9] [Onboard configuration]](#Onboard_configuration)
    -   [[2.2] [Installation from an already bootable Linux distribution]](#Installation_from_an_already_bootable_Linux_distribution)
        -   [[2.2.1] [Partitioning]](#Partitioning_2)
        -   [[2.2.2] [Formatting the partitions]](#Formatting_the_partitions)
        -   [[2.2.3] [Boot the current distro]](#Boot_the_current_distro)
        -   [[2.2.4] [Get the appropriate stage3]](#Get_the_appropriate_stage3)
        -   [[2.2.5] [Extract stage3]](#Extract_stage3)
        -   [[2.2.6] [Copy X11 configuration files]](#Copy_X11_configuration_files)
        -   [[2.2.7] [chroot to the new environment]](#chroot_to_the_new_environment)
        -   [[2.2.8] [Get a Portage snapshot]](#Get_a_Portage_snapshot)
        -   [[2.2.9] [Set up make.conf]](#Set_up_make.conf)
        -   [[2.2.10] [Update the system]](#Update_the_system)
        -   [[2.2.11] [Build the kernel]](#Build_the_kernel)
        -   [[2.2.12] [Set up the boot loader]](#Set_up_the_boot_loader)
        -   [[2.2.13] [Set a root password]](#Set_a_root_password)
        -   [[2.2.14] [Reboot]](#Reboot)
-   [[3] [Extras]](#Extras)
    -   [[3.1] [X11]](#X11)
    -   [[3.2] [EGL/GLES/OpenCL MALI drivers]](#EGL.2FGLES.2FOpenCL_MALI_drivers)
    -   [[3.3] [Create a non-root user]](#Create_a_non-root_user)
    -   [[3.4] [Networking]](#Networking)
    -   [[3.5] [SSH for remote access]](#SSH_for_remote_access)
    -   [[3.6] [Name server]](#Name_server)
    -   [[3.7] [Fan/temperature control]](#Fan.2Ftemperature_control)
-   [[4] [See also]](#See_also)
-   [[5] [References]](#References)

## [Hardware]

### [Standard]

  -------- --------------------- ------------- ------------------------ ------------------ ---------------- --------------------------------------------------------------
  Device   Make/model            Status        Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  CPU      Samsung Exynos 5422   Works         N/A                      N/A                5.4.211          Cortex-A15 2.0 GHz quad-core and Cortex-A7 1.5 Ghz quad-core
  GPU      Mali-T628 MP6         Not tested    N/A                      N/A                N/A              Needs external binary driver.
  -------- --------------------- ------------- ------------------------ ------------------ ---------------- --------------------------------------------------------------

## [Installation]

### [Cross-compiling from a Gentoo machine]

In case a Gentoo host machine is available, it is recommended to cross-build the target Gentoo system from the host Gentoo machine.

Native tools like [[[sys-devel/crossdev]](https://packages.gentoo.org/packages/sys-devel/crossdev)[]] and [[[sys-kernel/genkernel]](https://packages.gentoo.org/packages/sys-kernel/genkernel)[]], along with the availability of upstream sources^[\[1\]](#cite_note-1)^ make cross-building straightforward.

#### [ARM toolchain]

Prior to any cross-build operation, an ARM toolchain is required. It can be built thanks to the [[[sys-devel/crossdev]](https://packages.gentoo.org/packages/sys-devel/crossdev)[]] tool.

If not already done, install it and configure its [overlay](https://wiki.gentoo.org/wiki/Crossdev#Crossdev_overlay "Crossdev").

Then [crossdev] can build the ARM toolchain:

`root `[`#`]`crossdev -S -t armv7a-unknown-linux-gnueabihf`

#### [Bootloader installation]

The bootloader needs to be installed at the beginning of a DOS-labeled disk.

The [handbook](https://wiki.gentoo.org/wiki/Handbook:X86/Installation/Disks "Handbook:X86/Installation/Disks") explains how to create a new DOS partition table on the SD/eMMC card.

Once the DOS partition table is created, the bootloader sources are retrieved from the Hardkernel git repository:

`user `[`$`]`git clone -b odroidxu4-v2017.05 --depth 1 `[`https://github.com/hardkernel/u-boot.git`](https://github.com/hardkernel/u-boot.git)

A prebuilt U-Boot image is available in the [sd_fuse] directory and should fit common needs.

U-Boot along with TrustZone areas can be installed at the beginning of the SD/eMMC card with the provided [sd_fusing.sh] tool (adjust the path to the SD/eMMC card):

`user `[`$`]`cd u-boot/sd_fuse/ `

`user `[`$`]`./sd_fusing.sh /dev/mmcblkY`

#### [Partitioning]

The U-boot bootloader and TrustZone-related sections reside at the beginning of the disk until sector #2046^[\[2\]](#cite_note-2)^.

For future-proof reasons, it is safe and recommended from upstream to create user partitions from sector #3072.

If creating partitions are done with [fdisk], take care of redefining the suggested start sector of each partition since [fdisk] thinks first sectors are free. Either set the start sector of the first partition to 3072 or after the last sector of the previously created partition.

Creating the partitions are then performed as described in the [handbook](https://wiki.gentoo.org/wiki/Handbook:X86/Installation/Disks#Partitioning_the_disk_with_MBR_for_BIOS_.2F_legacy_boot "Handbook:X86/Installation/Disks").

As an exhaustive example, one could choose to create a swap partition, and for a server usage, a separate [/var] partition. The partitioning scheme would look like this:

  ------------------------ ------------------ ------------ -------- -----------------
  Part number              Size               Filesystem   Name     Type
  1                        128M               ext2         boot     Linux (83)
  2 (optional)             2G                 N/A          swap     Linux swap (82)
  3                        8G+                ext4         rootfs   Linux (83)
  4 (extended, optional)   N/A                N/A          N/A      N/A
  5                        rest of the disk   ext4         var      Linux (83)
  ------------------------ ------------------ ------------ -------- -----------------

If either the swap or the [/var] partitions are not required, then the partition table can be made up of primary partitions only.

The partition sizes have to be adapted to the disk capacity.

Once the partitions are written to the disk, create filesystems (adjust partition numbers):

`root `[`#`]`mkfs.ext2 -L boot /dev/mmcblkYp1 `

`root `[`#`]`mkfs.ext4 -L rootfs /dev/mmcblkYp3 `

`root `[`#`]`mkfs.ext4 -L var /dev/mmcblkYp5 # if applicable`

If a swap partition is used, it has to be initialized:

`root `[`#`]`mkswap /dev/mmcblkYp2`

In the next chapters, the target Gentoo system will be installed in these partitions. Thus they have to be mounted in the host Gentoo filesystem. Throughout this article, the partitions will be mounted under the [/mnt/odroid/] mountpoint.

`root `[`#`]`mkdir /mnt/odroid `

`root `[`#`]`mount /dev/mmcblkYp3 /mnt/odroid `

`root `[`#`]`mkdir /mnt/odroid/boot `

`root `[`#`]`mount /dev/mmcblkYp1 /mnt/odroid/boot `

`root `[`#`]`mkdir /mnt/odroid/var # if applicable `

`root `[`#`]`mount /dev/mmcblkYp5 /mnt/odroid/var # if applicable`

#### [Kernel installation]

Compared to the upstream kernel build guide^[\[3\]](#cite_note-3)^, [[[sys-kernel/genkernel]](https://packages.gentoo.org/packages/sys-kernel/genkernel)[]] and [[[dev-embedded/u-boot-tools]](https://packages.gentoo.org/packages/dev-embedded/u-boot-tools)[]] allow for cross-building the kernel and initramfs.

First download the Odroid Linux kernel branch:

`user `[`$`]`git clone -b odroid-5.4.y --depth 1 `[`https://github.com/hardkernel/linux.git`](https://github.com/hardkernel/linux.git)` linux-5.4.y-odroid`

Then cross-build the kernel and initramfs with the Odroid XU4-specific configuration (adjust -j\<number of jobs\>):

`root `[`#`]`cd linux-5.4.y-odroid `

`root `[`#`]`genkernel --kerneldir=. --kernel-config=arch/arm/configs/odroidxu4_defconfig --cross-compile=armv7a-unknown-linux-gnueabihf --makeopts=-j<number of jobs> --no-install all`

The generated initramfs needs to be converted to a U-boot compatible image thanks to the u-boot-tools\' [mkimage] utility.

`root `[`#`]`emerge --ask dev-embedded/u-boot-tools`

Generate the U-boot image:

`user `[`$`]`` mkimage -A arm -O linux -T ramdisk -C none -a 0 -e 0 -n uInitrd -d /var/tmp/genkernel/initramfs-arm-`make kernelrelease` uInitrd-`make kernelrelease` ``

Finally, the kernel and initramfs images, along with the device tree blob and overlays, are installed into the [/boot] partition of the SD/eMMC card:

`root `[`#`]`mkdir /mnt/odroid/boot/overlays `

`root `[`#`]`INSTALL_MOD_PATH=/mnt/odroid/ make modules_install `

`root `[`#`]`` cp -f /var/tmp/genkernel/kernel-arm-`make kernelrelease` /mnt/odroid/boot/zImage  ``

`root `[`#`]`` cp -f uInitrd-`make kernelrelease` /mnt/odroid/boot/uInitrd  ``

`root `[`#`]`cp -f arch/arm/boot/dts/exynos5422-odroidxu4.dtb /mnt/odroid/boot/ `

`root `[`#`]`cp -f arch/arm/boot/dts/overlays/*.dtbo /mnt/odroid/boot/overlays/ `

`root `[`#`]`` cp -f .config /mnt/odroid/boot/config-`make kernelrelease`  ``

`root `[`#`]`cd ..`

#### [Bootloader configuration]

For U-boot to be able to boot the system, it will search for [/boot/boot.ini].

Hardkernel provides various platform support files^[\[4\]](#cite_note-4)^, including a [boot.ini] example.

`user `[`$`]`git clone -b 5.4 `[`https://github.com/mdrjr/5422_bootini.git`](https://github.com/mdrjr/5422_bootini.git)

In [boot.ini], the `root=UUID` argument in the `bootargs` variable needs to be adjusted to the actual root filesystem UUID (*rootfs* in the partitioning scheme example).

The *rootfs* UUID can be obtained with [lsblk \--fs /dev/mmcblkYp1].

Replace `<rootfs actual UUID>` in [boot.ini] with the one given by [lsblk]. Also, if the *boot* ([/dev/mmcblkYp1]) partition has not been FAT-formatted as in the partitioning scheme above, replace **every** occurrence of the `fatload` command with the generic `load` one. It is safe anyway to use `load` whichever the filesystem in use.

[FILE] **`boot.ini`boot.ini changed lines**

    setenv bootargs "console=tty1 console=ttySAC2,115200n8 root=UUID=<rootfs actual UUID> rootwait ro fsck.repair=yes net.ifnames=0 $ $ $ smsc95xx.macaddr=$ $"
    [...]
    load mmc [...]

Finally, copy the files to the *boot* partition:

`root `[`#`]`cp -f 5422_bootini/boot.ini 5422_bootini/config.ini /mnt/odroid/boot/`

#### [Stage3 installation]

At this stage, the CPU is able to execute the U-boot bootloader which is then able to boot the Linux kernel and initramfs. The initramfs is able to mount the root filesystem thanks to `root=UUID=` in [/boot/boot.ini]. But the root filesystem is still empty. That is where stage3 comes into play to populate it.

Download the preferred [stage3] tarball from gentoo.org or any closer mirror. Choose between [openrc] and [systemd]. For instance, here is a [systemd] stage3 tarball download (replace DATE):

`user `[`$`]`wget -P stage3-armv7a_hardfp-systemd `[`https://distfiles.gentoo.org/releases/arm/autobuilds/current-stage3-armv7a_hardfp-systemd/stage3-armv7a_hardfp-systemd-DATE.tar.xz`](https://distfiles.gentoo.org/releases/arm/autobuilds/current-stage3-armv7a_hardfp-systemd/stage3-armv7a_hardfp-systemd-DATE.tar.xz)` `[`https://distfiles.gentoo.org/releases/arm/autobuilds/current-stage3-armv7a_hardfp-systemd/stage3-armv7a_hardfp-systemd-DATE.tar.xz.DIGESTS`](https://distfiles.gentoo.org/releases/arm/autobuilds/current-stage3-armv7a_hardfp-systemd/stage3-armv7a_hardfp-systemd-DATE.tar.xz.DIGESTS)` `[`https://distfiles.gentoo.org/releases/arm/autobuilds/current-stage3-armv7a_hardfp-systemd/stage3-armv7a_hardfp-systemd-DATE.tar.xz.sha256`](https://distfiles.gentoo.org/releases/arm/autobuilds/current-stage3-armv7a_hardfp-systemd/stage3-armv7a_hardfp-systemd-DATE.tar.xz.sha256)

Optionaly verify the tarball:

`user `[`$`]`cd stage3-armv7a_hardfp-systemd `

`user `[`$`]`sha256sum -c stage3-armv7a_hardfp-systemd-DATE.tar.xz.sha256`

Next, extract the tarball into the *rootfs* partition:

`root `[`#`]`cd /mnt/odroid `

`root `[`#`]`tar xpvf  --xattrs-include='*.*' --numeric-owner`

#### [System cross-configuration]

In order for the system to start properly, it is needed to perform some configurations, like [/etc/fstab] filesystem information, the Gentoo ebuild repository and the [root] default password.

The [handbook](https://wiki.gentoo.org/wiki/Handbook:X86/Installation/Base#Optional:_Selecting_mirrors "Handbook:X86/Installation/Base") can be followed to configure Gentoo mirrors with [[[app-portage/mirrorselect]](https://packages.gentoo.org/packages/app-portage/mirrorselect)[]] and to configure the Gentoo ebuild repository. Take care of writing into the SD/eMMC\'s *rootfs* partition and not the host one:

`root `[`#`]`mirrorselect -i -o >> /mnt/odroid/etc/portage/make.conf`

Then, to be able to login as root, its password has to be initialized since the [stage3]\'s root password is undefined:

`user `[`$`]`openssl passwd -6`

Copy-paste the generated hash to [/mnt/odroid/etc/shadow] in the second column of the [root] row.

Optionaly, if a keyboard is connected to the Odroid board, it could be convenient to set the console keyboard layout:

`root `[`#`]`echo "KEYMAP=<keyboard layout>" >> /mnt/odroid/etc/vconsole.conf`

Lastly, populate the [/mnt/odroid/etc/fstab] filesystem information as described in the [handbook](https://wiki.gentoo.org/wiki/Handbook:X86/Installation/System#Filesystem_information "Handbook:X86/Installation/System") for the partitions to be mounted on startup.

#### [First boot]

Insert the SD/eMMC card into the Odroid XU4 board, place the boot selection jumper accordingly and boot the board.

When asked to login, login as [root] with the previously defined password.

#### [Onboard configuration]

On the first boot, it is highly recommended to configure the init system ([OpenRC] or [Systemd]) in order to have networking functional as well as the hostname, timezone, time and locales configured.

The [handbook](https://wiki.gentoo.org/wiki/Handbook:X86/Installation/Base#Configuring_Portage "Handbook:X86/Installation/Base") is again the preferred reference for this configuration. The [Systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") wiki article is also of great help if this init system is chosen.

For convenient further installations and configurations, one can choose to enable an SSH remote access from the local network. For doing so, a regular user is usually added to avoid SSH [root] access:

`root `[`#`]`useradd -m -G users,wheel <login>`

Next, the SSH service can be started.

For [Systemd]:

`root `[`#`]`systemctl start sshd.service`

For [OpenRC]:

`root `[`#`]`rc-service sshd start`

Once the network is accessible and the [gentoo] portage repository is initiated, the [Portage configuration](https://wiki.gentoo.org/wiki/Handbook:X86/Installation/Base#Configuring_Portage "Handbook:X86/Installation/Base") can be performed.

`root `[`#`]`emerge-webrsync `

`root `[`#`]`emerge --sync`

Then, **very importantly**, choose the right Portage profile with the [eselect profile] command set before any package is emerged.

Finally, for system consistency reason, it is recommended to update the system:

`root `[`#`]`emerge --update --deep --newuse --with-bdeps=y --ask @world`

### [Installation from an already bootable Linux distribution]

Specific hardware needed: An SD card to USB adaptor.

#### [Partitioning]

Put the SD card into a SD card to USB adaptor and begin to partition it. If it is a fresh SD card from hardkernel then there should be plenty of room to split the first partition in 2(my card is 16gb).

A signed u-boot has to be used, creating a uboot, bootloader from source is possible but require a signed stage. Odroid has been signing these stages, check their support forum. [More information from Odroid here](https://wiki.odroid.com/odroid-xu4/software/building_u-boot_mainline)

This method uses the already existing bootloader from the image used to bootstrap the system. It is recommended to do this before the partitioning in case the command overwrites the start of a partition.

** Warning**\
This is a VERY dangerous command. If a mistake is made, permanent loss of data can occure.

[CODE] **Device names**

    /dev/mmcblkX where the initial system is located
    /dev/mmcblkY where the final gentoo system will be located

Boot loader installation:

`root `[`#`]`dd if=/dev/mmcblkX of=/dev/mmcblkY skip=1 seek=1 bs=512 count=2046 `

Partitions example:

`root `[`#`]`fdisk -l /dev/mmcblk0`

    Disk /dev/mmcblk0: 58.2 GiB, 62537072640 bytes, 122142720 sectors
    Units: sectors of 1 * 512 } 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disklabel type: dos
    Disk identifier: 0x3cedfd53

    Device         Boot  Start       End   Sectors  Size Id Type
    /dev/mmcblk0p1        2048    526335    524288  256M  c W95 FAT32 (LBA)
    /dev/mmcblk0p2      526336 122142719 121616384   58G 83 Linux

#### [Formatting the partitions]

It is recommended to have the [[[sys-fs/dosfstools]](https://packages.gentoo.org/packages/sys-fs/dosfstools)[]] and [[[sys-fs/exfat-utils]](https://packages.gentoo.org/packages/sys-fs/exfat-utils)[]] available on the host and final system.

`root `[`#`]`mkfs.vfat -F32 -n BOOT /dev/mmcblkYp1 `

`root `[`#`]`mkfs.ext4 -L root /dev/mmcblkYp2 `

#### [Boot the current distro]

Boot into the system currently installed onto the XU4, Ubuntu/Debian/other it doesn't really matter(Does it work?). On the current OS of the XU4, mount the empty partition to /mnt (mine is mmcblk0p2, yours is whatever partition you made)

`root `[`#`]`mount /dev/mmcblk0p2 /mnt `

`root `[`#`]`cd /mnt `

#### [Get the appropriate stage3]

Get the stage3 tarball from gentoo.org, you will need the ARMv7a\|HardFP and change the xxxx to the proper date in the filename. To get the proper information on this [page](http://distfiles.gentoo.org/releases/arm/autobuilds/current-stage3-armv7a_hardfp-openrc/).

`root `[`#`]`wget https://distfiles.gentoo.org/releases/arm/autobuilds/current-stage3-armv7a_hardfp-openrc/stage3-armv7a_hardfp-openrc-xxxx.tar.xz`

#### [Extract stage3]

Extract the tarball, we now have a root file system that we can start working with:

`root `[`#`]`tar xpvf stage3-armv7a_hardfp-openrc*.tar.xz --xattrs-include='*.*' --numeric-owner`

#### [Copy X11 configuration files]

Just in case\...

`root `[`#`]`cp -a /etc/X11 /mnt/etc/`

#### [chroot to the new environment]

Once extracted, go to the / directory then chroot into the partition:

`root `[`#`]`cd / `

`root `[`#`]`mount -t proc none /mnt/proc `

`root `[`#`]`mount --rbind /sys /mnt/sys `

`root `[`#`]`mount --rbind /dev /mnt/dev `

`root `[`#`]`cp -L /etc/resolv.conf /mnt/etc `

`root `[`#`]`chroot /mnt /bin/bash `

`root `[`#`]`env-update (might fail without the portage snapshot) `

`root `[`#`]`source /etc/profile `

#### [Get a Portage snapshot]

We need to get the Portage snapshot, before we can do this we must set the date (emerge-webrsync didn't work on my machine for some reason):

`root `[`#`]`date MMDDHHMMYYYY `

`root `[`#`]`cd /usr `

`root `[`#`]`wget `[`http://gentoo.osuosl.org/snapshots/portage-latest.tar.bz2`](http://gentoo.osuosl.org/snapshots/portage-latest.tar.bz2)` `

`root `[`#`]`tar -xvjf portage-latest.tar.bz2 `

`root `[`#`]`emerge –sync `

`root `[`#`]`rm portage-latest.tar.bz2 `

#### [Set up make.conf]

Before we do anything we must alter the make.config file, if we don't compilations will take a long time on a single arm core. Be sure to add `makeopts=”-j9”`. Use flags are up to you, for the purpose of this guide I kept them as small as possible. Future experimentation would be switching -march=armv7-a to native, though that will cause problems for distcc, but that's for another guide.

`root `[`#`]`nano /etc/portage/make.conf`

[CODE] **make.config sample**

    # These settings were set by the catalyst build script that automatically
    # built this stage.
    # Please consult /usr/share/portage/config/make.conf.example for a more
    # detailed example.
    CFLAGS="-O2 -pipe -march=armv7-a -mfpu=vfpv3-d16 -mfloat-abi=hard"
    # WARNING: Changing your CHOST is not something that should be done lightly.
    # Please consult https://wiki.gentoo.org/wiki/Changing_the_CHOST_variable before changing
    CHOST="armv7a-unknown-linux-gnueabihf"
    PORTDIR="/var/db/repos/gentoo"
    DISTDIR="/var/cache/distfiles"
    PKGDIR="/var/cache/binpkgs"

    # This sets the language of build output to English.
    # Please keep this setting intact when reporting bugs.
    LC_MESSAGES=C

    USE="-bindist"
    MAKEOPTS="-j3"

#### [Update the system]

Before we compile a kernel we must update the system, note this will take a while(several hours, gcc takes about half of the time, be sure you have makeopts="-j3", as bigger values tend to saturate memory), be sure that the date was set correctly before running emerge:

`root `[`#`]`emerge --sync `

`root `[`#`]`emerge --update --deep --newuse @world `

`root `[`#`]`emerge --depclean `

`root `[`#`]`emerge -a app-portage/gentoolkit (needed for revdep-rebuild) `

`root `[`#`]`revdep-rebuild `

#### [Build the kernel]

Time to compile the kernel, unfortunately the official gentoo sources do not work for the odroid-xu4 SoC. If one tries to compile with gentoo-sources and configure the XU4 to boot, it will fail. If one tries to boot the XU4 with a non-gentoo kernel/different config, the system will boot however there will be problems(network interfaces not being detected for example). What needs to happen is one must git clone hardkernel's official kernel and then compile it with any features one might want. There are 2 ways to do this, manual and automatically with genkernel. Below is how to do it with genkernel.

Ensure that partitions are correctly mapped:

`root `[`#`]`nano /etc/fstab`

\

`root `[`#`]`mount /dev/mmcblk1p1 /boot`

Verify [[[dev-vcs/git]](https://packages.gentoo.org/packages/dev-vcs/git)[]] and [[[sys-devel/bc]](https://packages.gentoo.org/packages/sys-devel/bc)[]] are installed so that the next steps can operated as expected. Emerge the packages if necessary.

For the 1st time:

`root `[`#`]`cd /usr/src `

`root `[`#`]`git clone `[`https://github.com/hardkernel/linux.git`](https://github.com/hardkernel/linux.git)` -b odroidxu4-4.14.y --depth 1 odroidxu4-4.14.y `

`root `[`#`]`ln -s odroidxu4-4.14.y linux `

Followed by from now and future updates from the git tree:

`root `[`#`]`mount /dev/mmcblk0p1 /boot `

`root `[`#`]`cd /usr/src/odroidxu4-4.14.y/ `

`root `[`#`]`git pull # simply put, it synchronizes the local with the remote repository; `

`root `[`#`]`cd .. `

`root `[`#`]`genkernel --kernel-config=/usr/src/linux/arch/arm/configs/odroidxu4_defconfig all `

You will then need the [[[dev-embedded/u-boot-tools]](https://packages.gentoo.org/packages/dev-embedded/u-boot-tools)[]] to create a uInitrd from the current initramfs, once all the files are created, let\'s copy all of them to /boot

`root `[`#`]`cd /usr/src/odroidxu4-4.14.y/ `

`root `[`#`]`` mkimage -A arm -O linux -T ramdisk -C none -a 0 -e 0 -d /boot/initramfs-genkernel-arm-`make kernelrelease` uInitrd-`make kernelrelease`  ``

`root `[`#`]`` cp arch/arm/boot/zImage /boot/zImage-`make kernelrelease`  ``

`root `[`#`]`` cp arch/arm/boot/dts/exynos5422-odroidxu4.dtb uInitrd-`make kernelrelease` /boot  ``

Remember the value returned by [make kernelrelease] you will need to adjust the file names in the [boot.ini]

In case someone would like to use any of the **menuconfig**, for instance, or add / remove any driver or something else to / from the new kernel, I think it would be useful to copy the final **/usr/src/linux/.config** file back to **/usr/src/linux/arch/arm/configs/odroidxu4_defconfig**, or to copy the **/usr/src/linux/.config** to some safe place for further use.

#### [Set up the boot loader]

Modify boot loader to boot new kernel and filesystem:

`root `[`#`]`cd /boot`

`root `[`#`]`nano boot.ini`

Below is the original boot.ini from the latest Ubuntu image, adjust the line with:

[CODE] **original**

    fatload mmc 0:1 0x40008000 zImage

to

[CODE] **new**

    fatload mmc 0:1 0x40008000 kernel-genkernel-arm-4.9.34

\

[CODE] **Complete boot.ini**

    ODROIDXU-UBOOT-CONFIG

    # U-Boot Parameters
    setenv initrd_high "0xffffffff"
    setenv fdt_high "0xffffffff"

    # Mac address configuration
    setenv macaddr "00:1e:06:61:7a:39"

    #------------------------------------------------------------------------------------------------------
    # Basic Ubuntu Setup. Don't touch unless you know what you are doing.
    # --------------------------------
    setenv bootrootfs "console=tty1 console=ttySAC2,115200n8 root=UUID=e139ce78-9841-40fe-8823-96a304a09859 rootwait ro fsck.repair=yes net.ifnames=1"

    # --- Screen Configuration for HDMI --- #
    # ---------------------------------------
    # Uncomment only ONE line! Leave all commented for automatic selection.
    # Uncomment only the setenv line!
    # ---------------------------------------
    # ODROID-VU forced resolution
    # setenv videoconfig "video=HDMI-A-1:1280x800@60"
    # -----------------------------------------------
    # ODROID-VU forced EDID
    # setenv videoconfig "drm_kms_helper.edid_firmware=edid/1280x800.bin"
    # -----------------------------------------------
    # 1920x1200 60hz without monitor data using generic information
    # setenv videoconfig "drm_kms_helper.edid_firmware=edid/1920x1200_60hz.bin"
    # -----------------------------------------------
    # 1920x1200 30hz without monitor data using generic information
    # setenv videoconfig "drm_kms_helper.edid_firmware=edid/1920x1200_30hz.bin"
    # -----------------------------------------------
    # 1920x1080 (1080P) with monitor provided EDID information. (1080p-edid)
    # setenv videoconfig "video=HDMI-A-1:1920x1080@60"
    # -----------------------------------------------
    # 1920x1080 (1080P) without monitor data using generic information (1080p-noedid)
    # setenv videoconfig "drm_kms_helper.edid_firmware=edid/1920x1080.bin"
    # -----------------------------------------------
    # 1920x1080 50hz (1080P) with monitor provided EDID information. (1080p 50hz-edid)
    # setenv videoconfig "video=HDMI-A-1:1920x1080@50"
    # -----------------------------------------------
    # 1920x1080 50hz (1080P) without monitor data using generic information (1080p 50hz-noedid)
    # setenv videoconfig "drm_kms_helper.edid_firmware=edid/1920x1080_50hz.bin"
    # -----------------------------------------------
    # 1680x1050 without monitor data using generic information
    # setenv videoconfig "drm_kms_helper.edid_firmware=edid/1680x1050.bin"
    # -----------------------------------------------
    # 1600x1200 without monitor data using generic information
    # setenv videoconfig "drm_kms_helper.edid_firmware=edid/1600x1200.bin"
    # -----------------------------------------------
    # 1600x900 without monitor data using generic information
    # setenv videoconfig "drm_kms_helper.edid_firmware=edid/1600x900.bin"
    # -----------------------------------------------
    # 1440x900 with monitor provided EDID information.
    # setenv videoconfig "video=HDMI-A-1:1440x900@60"
    # -----------------------------------------------
    # 1440x900 without monitor data using generic information
    # setenv videoconfig "drm_kms_helper.edid_firmware=edid/1440x900.bin"
    # -----------------------------------------------
    # 1366x768 without monitor data using generic information
    # setenv videoconfig "drm_kms_helper.edid_firmware=edid/1366x768.bin"
    # -----------------------------------------------
    # 1360x768 without monitor data using generic information
    # setenv videoconfig "drm_kms_helper.edid_firmware=edid/1360x768.bin"
    # -----------------------------------------------
    # 1280x1024 without monitor data using generic information
    # setenv videoconfig "drm_kms_helper.edid_firmware=edid/1280x1024.bin"
    # -----------------------------------------------
    # 1280x720 (720P) with monitor provided EDID information. (720p-edid)
    # setenv videoconfig "video=HDMI-A-1:1280x720@60"
    # -----------------------------------------------
    # 1280x720 (720P) without monitor data using generic information (720p-noedid)
    # setenv videoconfig "drm_kms_helper.edid_firmware=edid/1280x720.bin"
    # -----------------------------------------------
    # 1024x768 without monitor data using generic information
    # setenv videoconfig "drm_kms_helper.edid_firmware=edid/1024x768.bin"
    # -----------------------------------------------
    # 1024x600 without monitor data using generic information (ODROID VU7+)
    # setenv videoconfig "drm_kms_helper.edid_firmware=edid/1024x600.bin"
    # -----------------------------------------------
    # 800x600 without monitor data using generic information
    # setenv videoconfig "drm_kms_helper.edid_firmware=edid/800x600.bin"
    # -----------------------------------------------
    # 800x480 without monitor data using generic information (ODROID 7")
    # setenv videoconfig "drm_kms_helper.edid_firmware=edid/800x480.bin"
    # -----------------------------------------------
    # 720x576 without monitor data using generic information
    # setenv videoconfig "drm_kms_helper.edid_firmware=edid/720x576.bin"
    # -----------------------------------------------
    # 720x480 without monitor data using generic information
    # setenv videoconfig "drm_kms_helper.edid_firmware=edid/720x480.bin"
    # -----------------------------------------------
    # 640x480 without monitor data using generic information
    # setenv videoconfig "drm_kms_helper.edid_firmware=edid/640x480.bin"
    # -----------------------------------------------
    # 480x800 without monitor data using generic information
    # setenv videoconfig "drm_kms_helper.edid_firmware=edid/480x800.bin"

    # --- HDMI / DVI Mode Selection ---
    # ------------------------------------------
    # - HDMI Mode
    setenv vout "hdmi"
    # - DVI Mode (disables sound over HDMI as per DVI compat)
    # setenv vout "dvi"

    # --- HDMI CEC Configuration ---
    # ------------------------------------------
    setenv cecenable "false" # false or true
    # set to true to enable HDMI CEC

    # Enable/Disable ODROID-VU7 Touchsreen
    setenv disable_vu7 "true" # false

    # CPU Governor Selection
    # Available governos: conservative, userspace, powersave, ondemand, performance, schedutil
    setenv governor "performance"

    # External watchdog board enable
    setenv external_watchdog "false"
    # debounce time set to 3 ~ 10 sec, default 3 sec
    setenv external_watchdog_debounce "3"

    #------------------------------------------------------------------------------
    #
    # HDMI Hot Plug detection
    #
    #------------------------------------------------------------------------------
    #
    # Forces the HDMI subsystem to ignore the check if the cable is connected or
    # not.
    # false : disable the detection and force it as connected.
    # true : let cable, board and monitor decide the connection status.
    #
    # default: true
    #
    #------------------------------------------------------------------------------
    setenv HPD "true"

    setenv hdmi_phy_control "HPD=$ vout=$"

    # Load kernel, initrd and dtb in that sequence
    fatload mmc 0:1 0x40008000 kernel-genkernel-arm-4.9.34
    fatload mmc 0:1 0x42000000 uInitrd
    if test "$" = "xu4"; then fatload mmc 0:1 0x44000000 exynos5422-odroidxu4.dtb; setenv fdtloaded "true"; fi
    if test "$" = "xu3"; then fatload mmc 0:1 0x44000000 exynos5422-odroidxu3.dtb; setenv fdtloaded "true"; fi
    if test "$" = "xu3l"; then fatload mmc 0:1 0x44000000 exynos5422-odroidxu3-lite.dtb; setenv fdtloaded "true"; fi
    #failsafe
    if test "$" != "true"; then fatload mmc 0:1 0x44000000 exynos5422-odroidxu4.dtb; fi

    fdt addr 0x44000000

    if test "$" = "false"; then fdt rm /cec@101B0000; fi
    if test "$" = "false"; then setenv hid_quirks "usbhid.quirks=0x0eef:0x0005:0x0004"; fi
    if test "$" = "true"; then setenv external_watchdog "external_watchdog=$ external_watchdog_debounce=$"; fi

    # final boot args
    setenv bootargs "$ $ $ $ smsc95xx.macaddr=$ $ governor=$"

    # Boot the board
    bootz 0x40008000 0x42000000 0x44000000

#### [Set a root password]

`root `[`#`]`passwd`

#### [Reboot]

Boot the new kernel and into the new Gentoo environment and that's it! You should be able to boot without problem! Welcome to Gentoo on the Odroid-XU4!

## [Extras]

### [X11]

Willing for a graphical environment, X11 is a classical - although there is a pretty interesting article in a recent **Odroid Magazine** about Wayland - so there is the need for the specific driver. Emerge [eselect-repository] and add the **hossie** overlay:

`root `[`#`]`emerge -vD --quiet-build eselect-repository && emerge --sync && eselect repository enable hossie`

Emerge the **exynos armsoc** X11 driver:

`root `[`#`]`emerge -vuDN --quiet-build x11-drivers/xf86-video-armsoc`

Emerge all **xorg/X11** stuff according to the usual [Gentoo_Handbook](https://wiki.gentoo.org/wiki/Handbook:Main_Page "Handbook:Main Page")

The original Ubuntu image has a \"**xorg.conf**\" configuration file and \"**xorg.conf.d**\" directory for extra configurations in /etc/X11, that has already both been copied to Gentoo in an earlier step. Then, it should be possible to get a graphical desktop like fluxbox or WindowMaker, for instance.

### [][EGL/GLES/OpenCL MALI drivers]

Usually the latest working driver is located here: [5422_mali](https://github.com/mdrjr/5422_mali/tree/master)

Or from the odroid debian package: [mali-fbdev](http://deb.odroid.in/5422-s/pool/main/m/mali-fbdev/)

unmask the opencl use flag

Tentative to create an ebuild should be based on : [New eselect-opengl design](https://wiki.gentoo.org/wiki/User:MGorny/New_eselect-opengl_design "User:MGorny/New eselect-opengl design")

### [Create a non-root user]

[Handbook:AMD64/Installation/Finalizing](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Finalizing "Handbook:AMD64/Installation/Finalizing")

### [Networking]

Networking hasn't been declared yet, please verify the interfaces have been detected before the below commands are executed

`root `[`#`]`cd /etc/init.d `

`root `[`#`]`ln -s net.lo net.eth0 `

`root `[`#`]`rc-update add net.eth0 default `

### [SSH for remote access]

Adding SSHD as a default service

`root `[`#`]`rc-update add sshd default`

If on a switch it's necessary to declare a static ip

`root `[`#`]`cd /etc/conf.d `

`root `[`#`]`nano net `

### [Name server]

Since everything is being define manually, resolv.conf must have a nameserver in it:

`root `[`#`]`cd /etc `

`root `[`#`]`nano resolv.conf `

`root `[`#`]`nameserver 8.8.8.8 `

Start installing all necessary software that you need!

### [][Fan/temperature control]

Gentoo puts all of the temperature monitors in the [/sys/devices/virtual/thermal/] directory. In order to change the fan settings you must modify the .dtb, these are located in [/usr/src/linux/arch/arm/boot/dts].

One can modify the exynos5422-odroidxu4.dts easily, however notice that exynos5422-odroidxu3-common.dtsi is included, here is where one portion of the fan control:

[CODE]

    fan0: pwm-fan ;

Where 255 = 100%

To change the CPU states modify the exynos5422-cpu-thermal.dtsi file

** Note**\
It might be worth experimenting with march=native rather than pre-defined as it is currently, but if the use case for the xu4 is distcc this will cause problems.

The current guide uses the stock initrd, using genkernel to generate a new initrd has not been tested.

## [See also]

-   [Crossdev](https://wiki.gentoo.org/wiki/Crossdev "Crossdev") --- a set of [bash] scripts that utilize [emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge") to provide a system integrated cross-compilation capability.
-   [Handbook:X86](https://wiki.gentoo.org/wiki/Handbook:X86 "Handbook:X86") --- A handbook dedicated to installing and configuring the **[x86]** architecture., an effort to centralize documentation into a coherent handbook.
-   [Setting_a_default_root_password](https://wiki.gentoo.org/wiki/Setting_a_default_root_password "Setting a default root password")

## [References]

1.  [[[↑](#cite_ref-1)] [[Hardkernel Git repositories](https://github.com/hardkernel/), [GitHub](https://github.com/). Retrieved on November 2nd, 2022]]
2.  [[[↑](#cite_ref-2)] [[Odroid XU4 partition table](https://wiki.odroid.com/odroid-xu4/software/partition_table#tab__odroid-xu341), [Odroid wiki](https://wiki.odroid.com/). Retrieved on November 3rd, 2022]]
3.  [[[↑](#cite_ref-3)] [[Linux kernel 5.4 build guide](https://wiki.odroid.com/odroid-xu4/os_images/linux/ubuntu_5.4/ubuntu_5.4/kernel_build_guide), [Odroid wiki](https://wiki.odroid.com/). Retrieved on November 4th, 2022]]
4.  [[[↑](#cite_ref-4)] [[Odroid XU4 platform files](https://wiki.odroid.com/odroid-xu4/os_images/linux/ubuntu_5.4/platform_files), [Odroid wiki](https://wiki.odroid.com/). Retrieved on November 4th, 2022]]