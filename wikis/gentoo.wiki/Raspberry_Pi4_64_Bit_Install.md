This page contains [[changes](https://wiki.gentoo.org/index.php?title=Raspberry_Pi4_64_Bit_Install&diff=1421916)] which are not marked for translation.

\

** Warning**\
This page is in the process of being merged into the [universal Raspberry Pi Install Guide](https://wiki.gentoo.org/wiki/Raspberry_Pi_Install_Guide "Raspberry Pi Install Guide")

This wiki page explains how to install a 64bit Gentoo system on the Raspberry Pi 4.

## Contents

-   [[1] [Introduction]](#Introduction)
    -   [[1.1] [Not tested]](#Not_tested)
-   [[2] [Preparing the external storage]](#Preparing_the_external_storage)
-   [[3] [Mounting the base filesystem]](#Mounting_the_base_filesystem)
-   [[4] [Installing the Gentoo base system]](#Installing_the_Gentoo_base_system)
    -   [[4.1] [QEMU user chroot]](#QEMU_user_chroot)
-   [[5] [Configuring Portage]](#Configuring_Portage)
    -   [[5.1] [COMMON_FLAGS]](#COMMON_FLAGS)
    -   [[5.2] [VIDEO_CARDS]](#VIDEO_CARDS)
-   [[6] [Raspberry Pi Firmware]](#Raspberry_Pi_Firmware)
-   [[7] [\"BIOS\" configuration: /boot/config.txt]](#.22BIOS.22_configuration:_.2Fboot.2Fconfig.txt)
    -   [[7.1] [Kernel command line: /boot/cmdline.txt]](#Kernel_command_line:_.2Fboot.2Fcmdline.txt)
-   [[8] [Kernel]](#Kernel)
    -   [[8.1] [Raspberry official binary kernel]](#Raspberry_official_binary_kernel)
    -   [[8.2] [Manual build]](#Manual_build)
        -   [[8.2.1] [Kernel config tweaks]](#Kernel_config_tweaks)
            -   [[8.2.1.1] [Setting the default CPU governor]](#Setting_the_default_CPU_governor)
        -   [[8.2.2] [Building the kernel]](#Building_the_kernel)
        -   [[8.2.3] [Installing the kernel]](#Installing_the_kernel)
        -   [[8.2.4] [Installing Device Tree Files and Overlays]](#Installing_Device_Tree_Files_and_Overlays)
-   [[9] [Configuring the system]](#Configuring_the_system)
    -   [[9.1] [Zram]](#Zram)
    -   [[9.2] [Removing unnecessary cron jobs]](#Removing_unnecessary_cron_jobs)
        -   [[9.2.1] [Disabling the man-db daily cron job]](#Disabling_the_man-db_daily_cron_job)
            -   [[9.2.1.1] [Masking the cron job file]](#Masking_the_cron_job_file)
            -   [[9.2.1.2] [Disabling the daily cron task]](#Disabling_the_daily_cron_task)
            -   [[9.2.1.3] [Manually updating the cache]](#Manually_updating_the_cache)
    -   [[9.3] [Making the DUID static]](#Making_the_DUID_static)
-   [[10] [Misc]](#Misc)
    -   [[10.1] [WiFi]](#WiFi)
    -   [[10.2] [EEProm updates]](#EEProm_updates)
    -   [[10.3] [Power over Ethernet]](#Power_over_Ethernet)
    -   [[10.4] [microSD trim/discard]](#microSD_trim.2Fdiscard)
    -   [[10.5] [USB attached SSD]](#USB_attached_SSD)
    -   [[10.6] [Cross-compiling]](#Cross-compiling)
-   [[11] [See also]](#See_also)
-   [[12] [Acknowledgements]](#Acknowledgements)

## [Introduction]

The install procedure of Gentoo on the Pi 4 is a standard Gentoo installation similar to the one described in the [AMD64 Handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64 "Handbook:AMD64") but without a live medium: the storage (SD card or external SSD) that will be used by the Pi 4 needs to be setup on a separate Gentoo machine (whose platform is probably not **[aarch64]**)

### [Not tested]

-   Analogue Video Output
-   Analogue Audio Output
-   Camera
-   Screen

## [Preparing the external storage]

** See also**\
[Preparing the disks](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Disks "Handbook:AMD64/Installation/Disks").

This section is obsoleted by the [Raspberry Pi Install Guide](https://wiki.gentoo.org/wiki/Raspberry_Pi_Install_Guide#Preparing_the_disks "Raspberry Pi Install Guide") ~~Minimally, the storage can be formatted with 2 partitions.~~

-   A fat32 formatted **[ESP]** [/boot] partition with the required firmware and kernel blobs. 512MB is sufficient.
-   An ext4 formatted [/] (root) partition for the system.

Assuming the target storage is mounted at [/dev/sda], this can be written with:

`root `[`#`]`fdisk `[`/dev/sda`]

    Welcome to fdisk (util-linux 2.38.1).
    Changes will remain in memory only, until you decide to write them.
    Be careful before using the write command.

To create the GPT label:

`Command (m for help)``g`

Created a new GPT disklabel (GUID: E361F483-EDF0-5846-BDCE-5A92124726D9).

To create the first 1gb partition:

`Command (m for help)``n`

    Partition number (1-128, default 1):
    First sector (2048-124735454, default 2048):

Last sector, +/-sectors or +/-size (2048-124735454, default 124733439): [+1G]

To create the root partition, spanning the rest of the volume:

`Command (m for help)``n`

    Partition number (2-128, default 2):
    First sector (2099200-124735454, default 2099200):
    Last sector, +/-sectors or +/-size (2099200-124735454, default 124733439):

    Created a new partition 2 of type 'Linux filesystem' and of size 58.5 GiB.

The first partition\'s type can be set to **[ESP]** with:

`Command (m for help)``t`

    Partition number (1,2, default 2): 1
    Partition type or alias (type L to list all): 1

    Changed type of partition 'Linux filesystem' to 'EFI System'.

The staged partition table can be read with:

`Command (m for help)``p`

    Disk /dev/sdf: 59.48 GiB, 63864569856 bytes, 124735488 sectors
    Disk model: UHSII uSD Reader
    Units: sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disklabel type: gpt
    Disk identifier: E361F483-EDF0-5846-BDCE-5A92124726D9

    Device       Start       End   Sectors  Size Type
    /dev/sdf1     2048   2099199   2097152    1G EFI System
    /dev/sdf2  2099200 124733439 122634240 58.5G Linux filesystem

If the partition table looks correct, it can be written with:

`Command (m for help)``w`

    The partition table has been altered.
    Calling ioctl() to re-read partition table.
    Syncing disks.

Once the partitions have been created, filesystems can be written with:

`root `[`#`]`mkfs.fat `[`/dev/sda1`]

`root `[`#`]`mkfs.ext4 `[`/dev/sda2`]

## [Mounting the base filesystem]

In this guide, [/dev/sda2] will be mounted to [/mnt/gentoo].

`root `[`#`]`mount `[`/dev/sda2`]` `[`/mnt/gentoo`]

** Note**\
The boot partition will be mounted later, when needed.

## [Installing the Gentoo base system]

** See also**\
[Installing a stage file](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Stage#Installing_a_stage_file "Handbook:AMD64/Installation/Stage").

From the target root directory, the stage3 file can be extracted with:

`/mnt/gentoo #``tar xvf stage3-`**[`arm64`]**`-<release timestamp>.tar.xz`

### [QEMU user chroot]

** See also**\
[Compiling with QEMU user chroot](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Compiling_with_qemu_user_chroot "Embedded Handbook/General/Compiling with qemu user chroot").

If the Gentoo machine being used to setup the Pi\'s storage device is not **[aarch64]** (e.g. **[amd64]**), QEMU needs to be setup and configured to chroot into this environment:

Once configured, the user target can be copied with:

`user `[`$`]`cp /usr/bin/qemu-`**[`aarch64`]**` `[`/mnt/gentoo/usr/bin`]

Then the chroot can be entered using [[[sys-apps/arch-chroot]](https://packages.gentoo.org/packages/sys-apps/arch-chroot)[]]:

`root `[`#`]`arch-chroot `[`/mnt/gentoo`]

## [Configuring Portage]

** See also**\
[Installing the base system](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base "Handbook:AMD64/Installation/Base").

### [COMMON_FLAGS]

Raspberry Pi 4B users should use the `-mcpu=cortex-a72` compiler in favor of `-march` and `-mtune` altogether. `march` and `mtune` behavior on **[arm64]** systems is different from **[amd64]**. [Source](https://community.arm.com/arm-community-blogs/b/tools-software-ides-blog/posts/compiler-flags-across-architectures-march-mtune-and-mcpu)

[FILE] **`/etc/portage/make.conf`**

    COMMON_FLAGS="-mcpu=cortex-a72 -ftree-vectorize -O2 -pipe -fomit-frame-pointer"

** Note**\
`-ftree-vectorize` and `-fomit-frame-pointer` allow utilization of more registers.

** Warning**\
`-mcpu=native` could be used but may cause issues with [distcc](https://wiki.gentoo.org/wiki/Distcc "Distcc").

### [VIDEO_CARDS]

The mesa drivers the Pi 4 needs to have full hardware acceleration are [v3d] and [vc4]

[FILE] **`/etc/portage/make.conf`**

    VIDEO_CARDS="v3d vc4"

It also needs specific firmware, loaded in the section [\"BIOS\" configuration](#.22BIOS.22_configuration:_.2Fboot.2Fconfig.txt)

## [Raspberry Pi Firmware]

The Raspberry Pi 4 second stage bootloader (`bootcode.bin`) is included on SPI flash and does not need to be added to the [/boot] (**[ESP]**) volume. ^[\[1\]](#cite_note-1)^

The following files are not included on builtin device storage, and must be added to the **[ESP]**:

-   `start4.elf`
-   `fixup4.dat`

** Important**\
[/boot] must be a `fat32` formatted, **[ESP]** labeled partition to be bootable.

These files are part of [[[sys-boot/raspberrypi-firmware]](https://packages.gentoo.org/packages/sys-boot/raspberrypi-firmware)[]], and are automatically installed to [/boot] on emerge:

`root `[`#`]`emerge --ask sys-boot/raspberrypi-firmware`

** Tip**\
This package essentially just copies the [official firmware files](https://github.com/raspberrypi/firmware/tree/master/boot) to the boot partition.

## [][\"BIOS\" configuration: /boot/config.txt]

** See also**\
[Raspberry Pi Bootloader Configuration](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#raspberry-pi-bootloader-configuration)

The following options may be useful:

-   `disable_overscan=1` Disable video overscanning.
-   `dtoverlay=vc4-kms-v3d` Enable GPU acceleration
-   `kernel kernel8.img` Change the path to the kernel file. The default for the RPi4 is `kernel8.img`.
-   `cmdline=cmdline.txt` Change the path to the `cmdline.txt` (kernel commandline) file.
-   `initramfs init.gz followkernel` Change the path to the loaded initramfs, `followkernel` should be used as it loads the image immediately after the kernel in memory.
-   `arm_boost=1` Enable 1.8GHz frequency boost instead of 1.5Ghz.
-   `dtparam=audio=on` Enable audio output
-   `dtparam=i2c_arm=on` Enable I2C.
-   `dtparam=spi=on` Enable SPI

** Tip**\
Any of these options can be written to [/boot/config.txt].

** See also**\
A full list of options is available [in the official documentation](https://www.raspberrypi.com/documentation/computers/config_txt.html).

There is a new [alternative audio mode](https://www.raspberrypi.org/forums/viewtopic.php?f=29&t=269769&p=1636828#p1636828) that does not use the `audio=on` **[dtparam]**.

### [][Kernel command line: /boot/cmdline.txt]

This file [/boot/cmdline.txt] contains the command line that is given to the kernel. One important information it needs to contain is where the root file system is.

[FILE] **`/boot/cmdline.txt`**

    console=tty1 root=PARTUUID=[root-partition-uuid] fsck.repair=yes rootwait

or

[FILE] **`/boot/cmdline.txt`**

    console=tty1 root=UUID=[root-filesystem-uuid] fsck.repair=yes rootwait

** Important**\
root=UUID=\[root-filesystem-uuid\] requires an initrd to provide the userspace [mount] command.

## [Kernel]

The kernel can either be manually compiled and fully customized or the official binary kernel from Raspberry can be installed.

** Important**\
Make sure the kernel blob filename in [/boot] is referenced correctly in [/boot/config.txt](#.22BIOS.22_configuration:_.2Fboot.2Fconfig.txt)

### [Raspberry official binary kernel]

Install [[[sys-kernel/raspberrypi-image]](https://packages.gentoo.org/packages/sys-kernel/raspberrypi-image)[]] and [[[sys-kernel/raspberrypi-sources]](https://packages.gentoo.org/packages/sys-kernel/raspberrypi-sources)[]]

`root `[`#`]`emerge --ask sys-kernel/raspberrypi-image sys-kernel/raspberrypi-sources`

### [Manual build]

If building in a chroot:

`/usr/src/linux #``make bcm2711_defconfig`

To cross compile the kernel:

`root `[`#`]`ARCH=arm64 CROSS_COMPILE=aarch64-unknown-linux-gnu- make bcm2711_defconfig`

Check the other kernel configuration settings given in [configure the kernel](https://wiki.gentoo.org/wiki/Raspberry_Pi_3_64_bit_Install#Configure_the_kernel "Raspberry Pi 3 64 bit Install").

#### [Kernel config tweaks]

##### [Setting the default CPU governor]

The default CPU governor (**[CPU_FREQ_DEFAULT_GOV]**) is `powersave`. **This runs the CPU at 600MHz all the time**. CPU governors can be controlled in /proc or the default CPU governor can be changed to be `schedutil` or `ondemand`:

[KERNEL] **Set the default CPU governor**

        CPU Power Management  --->
            CPU Frequency scaling  --->
                [*] CPU Frequency scaling
                    Default CPUFreq governor (schedutil) --->
                <*> 'schedutil' cpufreq policy governor

#### [Building the kernel]

To build in a chroot:

`/usr/src/linux #``make -j<threads>`

To cross compile:

`/usr/src/linux #``ARCH=arm64 CROSS_COMPILE=aarch64-unknown-linux-gnu- make -j<threads>`

#### [Installing the kernel]

** Warning**\
[make dtbs_install] does not install DTBs and overlays to the correct directory.

The kernel can be installed to [/boot] with:

`/usr/src/linux #``make dtbs_install`

Kernel modules can be installed with:

`/usr/src/linux #``make -j<threads> modules_install`

#### [Installing Device Tree Files and Overlays]

Compiled DTBs are stored in [arch/arm64/boot/dts/]. [bcm2711-rpi-4-b.dtb] is required for the RPI4:

`root `[`#`]`mkdir --parents /boot/overlays `

`root `[`#`]`cp -vR arch/arm64/boot/dts/overlays/*.dtbo /boot/overlays `

`root `[`#`]`cp -v arch/arm64/boot/dts/broadcom/bcm2711-rpi-4-b.dtb /boot`

** Note**\
DTBs may change between kernel updates, remember to use versions with the appropriate kernel.

** Tip**\
The Pi 400 uses [arch/arm64/boot/dts/broadcom/bcm2711-rpi-400.dtb].

## [Configuring the system]

The AMD64 handbook can be followed starting [Configuring the system](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/System "Handbook:AMD64/Installation/System") until the end, except for [Configuring the bootloader](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Bootloader "Handbook:AMD64/Installation/Bootloader") which is taken care of in [#Firmware / Boot partition](#Firmware_.2F_Boot_partition) section. Then, the storage can be safely unmounted and plugged in the Pi 4 and have it successfully booting and working as expected.

### [Zram]

SWAP space was intentionally not allocated to the SD card, because it can destroy SD cards without wear-leveling. To use compressed RAM for swap space, as well as [/var/log]:

[FILE] **`/etc/conf.d/zram-init`**

    # zram settings...
    # SPDX-License-Identifier: GPL-2.0-only

    # load zram kernel module on start?
    load_on_start=yes

    # unload zram kernel module on stop?
    unload_on_stop=yes

    # Number of devices.
    # This value is also passed to the kernel module on modprobe.
    num_devices=4
    # swap - 500M (or a fourth of available memory if uncommenting)
    type0=swap
    flag0= # The default "16383" is fine for us
    size0=512
    #size0=`LC_ALL=C free -m | awk '/^Mem:/'`
    maxs0=1 # maximum number of parallel processes for this device
    algo0=zstd # zstd (since linux-4.18), lz4 (since linux-3.15), or lzo.
    labl0=zram_swap # the label name

    # /var/log - 1G
    type1=/var/log
    size1=1024
    opts1=relatime # e.g. "noatime" or "strictatime" are also reasonable choices
    mode1=1755
    maxs1=1
    algo1=zstd
    labl1=var_log_dir

    # /var/lib/dhcpcd/ - 1m
    type2=/var/lib/dhcpcd
    size2=1
    opts2=relatime # e.g. "noatime" or "strictatime" are also reasonable choices
    mode2=1755
    maxs2=1
    algo2=zstd
    labl2=dhcpcd_dir

    # /var/lib/chrony/ - 1m
    type3=/var/lib/chrony
    size3=1
    opts3=relatime # e.g. "noatime" or "strictatime" are also reasonable choices
    mode3=1755
    owgr3=123:123
    maxs3=1
    algo3=zstd
    labl3=chrony_dir

** Note**\
If using a 1GB model, a smaller [/var/log] should be used.

** Tip**\
Remember to increment device numbers when adding devices, and change `num_devices`.

Then [zram-init] can be added to the *boot* runlevel:

`root `[`#`]`rc-update add zram-init boot`

### [Removing unnecessary cron jobs]

Unnecessary writing can kill SD cards, logging to memory or remotely and disabling unneeded periodic tasks can extend the life of a Raspberry Pi\'s root file system device.

#### [Disabling the man-db daily cron job]

By default, [[[sys-apps/man-db]](https://packages.gentoo.org/packages/sys-apps/man-db)[]] installs [/etc/cron.daily/man-db] which updates [man] cache files daily. This action is only necessary when new man pages are added, and can be removed by masking that file from being installed, and deleting it moving it to another runlevel.

##### [Masking the cron job file]

** Important**\
These changes will not persist if [[[sys-apps/man-db]](https://packages.gentoo.org/packages/sys-apps/man-db)[]] is updated.

[FILE] **`/etc/portage/make.conf`Ensure portage does not reinstall that file to /etc/cron.daily**

    INSTALL_MASK="/etc/cron.daily/man-db"

##### [Disabling the daily cron task]

The cron task can be removed or moved to a less frequent cron job:

`root `[`#`]`mv /etc/cron.daily/man-db /etc/cron.monthly/man-db`

or:

`root `[`#`]`chmod -x /etc/cron.daily/man-db`

##### [Manually updating the cache]

The man page cache can be manually updated with:

`root `[`#`]`mandb`

** Tip**\
This should be run when packages are updated.

### [Making the DUID static]

By default, [dhcpcd] will generate a randomized DUID when it first runs. To change this to be derived from the interface MAC address, so it can be safely stored in RAM:

[FILE] **`/etc/dhcpcd.conf`Make DUID based on MAC**

    duid ll

## [Misc]

### [WiFi]

WiFi needs three firmware files in [/lib/firmware/brcm/]. These are now provided by [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]]

    brcmfmac43455-sdio.bin
    brcmfmac43455-sdio.clm_blob
    brcmfmac43455-sdio.txt

Which is almost but not quite the same as the Pi3. The catch is in **[brcmfmac43455-sdio.txt]** where **[grep boardflags3]** produces different results for the Pi3 and Pi4 files.

    The Pi4 version returns boardflags3=0x44200100
    The Pi3 version returns boardflags3=0x48200100

With the wrong brcmfmac43455-sdio.txt file, bluetooth will work but not WiFi.

These files, including the Pi 4 version of above file, are found in [[[sys-firmware/raspberrypi-wifi-ucode]](https://packages.gentoo.org/packages/sys-firmware/raspberrypi-wifi-ucode)[]], to install it you\'ll also need to install [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] with the [savedconfig](https://wiki.gentoo.org/wiki/Savedconfig "Savedconfig") USE flag and remove the conflicting files from the saved configuration, and then re-emerge linux-firmware to apply the new de-conflicted saved configuration:

    /lib/firmware/brcm/brcmfmac43430-sdio.bin
    /lib/firmware/brcm/brcmfmac43430-sdio.txt
    /lib/firmware/brcm/brcmfmac43436-sdio.bin
    /lib/firmware/brcm/brcmfmac43436-sdio.clm_blob
    /lib/firmware/brcm/brcmfmac43436-sdio.txt
    /lib/firmware/brcm/brcmfmac43455-sdio.bin
    /lib/firmware/brcm/brcmfmac43455-sdio.clm_blob
    /lib/firmware/brcm/brcmfmac43455-sdio.txt
    /lib/firmware/brcm/brcmfmac43456-sdio.bin
    /lib/firmware/brcm/brcmfmac43456-sdio.clm_blob
    /lib/firmware/brcm/brcmfmac43456-sdio.txt

### [EEProm updates]

[[[dev-embedded/rpi-eeprom]](https://packages.gentoo.org/packages/dev-embedded/rpi-eeprom)[]] provides the eeprom files and the updater, as well as a service to check and apply the updates.

There are 3 release channels of firmware updates:

-   critical - Default - rarely updated
-   stable - Updated when new/advanced features have been successfully beta tested.
-   beta - New or experimental features are tested here first.

To configure which release channel you\'d like the updater service to follow, edit [/etc/conf.d/rpi-eeprom-update].

### [Power over Ethernet]

The Pi3b PoE HAT will power the P4 and a USB SSD.

Fan control works.

### [][microSD trim/discard]

The microSD interface supports the trim command:

`Pi4_~arm64 ~ #``fstrim -av`

     /boot: 7.7 GiB (8250073088 bytes) trimmed on /dev/mmcblk0p1

If you have a suitable microSD card, consider adding fstrim to a weekly or monthly cron job.

### [USB attached SSD]

Users with USB3 attached SSDs may have noticed that trim is not supported. It is a feature of USB storage that trim is disabled by default. [Trim can be enabled](https://wiki.gentoo.org/wiki/Discard_over_USB "Discard over USB") with mixed success. Only USB3 is supported and the USB3 to SSD bridge device must be able to pass the trim command.

One other thing to note, the Raspberry pi currently only supports booting from usb mass storage devices (including external hard drives) that have a 512 byte logical sector size. You may need to reformat (with the drive manufacturer\'s utility) them to enable 512 byte emulation.

See also [Unreliable USB Attached SCSI](https://wiki.gentoo.org/wiki/Raspberry_Pi_Install_Guide#Unreliable_USB_Attached_SCSI "Raspberry Pi Install Guide").

### [Cross-compiling]

[Cross-compiling](https://wiki.gentoo.org/wiki/Crossdev "Crossdev") is by far the fastest way to create packages for aarch64. Afterwards, binhost can be set up to download the packages that you desire. It is possible to create the entire RPI4 by using cross-compile and creating it through a stage2. [Distcc](https://wiki.gentoo.org/wiki/Raspberry_Pi/Cross_building "Raspberry Pi/Cross building") is also another great method for compiling aarch64 code. Code can be offloaded onto the main computer. Distcc will have more difficulties in boostraping though, unlike Cross-compiling.

## [See also]

-   [Raspberry Pi](https://wiki.gentoo.org/wiki/Raspberry_Pi "Raspberry Pi") --- a series of small single-board computers.

## [Acknowledgements]

NeddySeagoon for taking over maintenance and upstreaming many ebuilds from sakaki\'s overlay after sakaki\'s retirement ( [Neddy\'s fork](https://github.com/NeddySeagoon/genpi64-overlay) )

sakaki\'s topic on the [Raspberry Pi forums](//www.raspberrypi.org/forums/viewtopic.php?p=1491136)

All the contributors to [issue 3032](https://github.com/raspberrypi/linux/issues/3032) on the Raspberry Pi GitHub repository.

1.  [[[↑](#cite_ref-1)] [[https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#raspberry-pi-4-and-raspberry-pi-5-boot-flow](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#raspberry-pi-4-and-raspberry-pi-5-boot-flow)]]