** Warning**\
This page is in the process of being merged into the [universal Raspberry Pi Install Guide. Steps in ~~strikethrough~~ have been migrated](https://wiki.gentoo.org/wiki/Raspberry_Pi_Install_Guide "Raspberry Pi Install Guide")

## Contents

-   [[1] [Overview]](#Overview)
    -   [[1.1] [History]](#History)
    -   [[1.2] [What works]](#What_works)
    -   [[1.3] [Untested]](#Untested)
    -   [[1.4] [Whats required]](#Whats_required)
-   [[2] [Installation overview]](#Installation_overview)
    -   [[2.1] [Using crossdev to build a cross compiler]](#Using_crossdev_to_build_a_cross_compiler)
-   [[3] [Fetch the Raspberry Pi firmware]](#Fetch_the_Raspberry_Pi_firmware)
-   [[4] [Fetch, configure, and build the Raspberry Pi kernel]](#Fetch.2C_configure.2C_and_build_the_Raspberry_Pi_kernel)
    -   [[4.1] [Fetch the Raspberry Pi kernel]](#Fetch_the_Raspberry_Pi_kernel)
    -   [[4.2] [Configure the kernel]](#Configure_the_kernel)
    -   [[4.3] [Cross compiling the kernel]](#Cross_compiling_the_kernel)
-   [[5] [Partition the microSD card]](#Partition_the_microSD_card)
    -   [[5.1] [Background]](#Background)
    -   [[5.2] [Partitioning]](#Partitioning)
        -   [[5.2.1] [Make the partition table and add partitions]](#Make_the_partition_table_and_add_partitions)
        -   [[5.2.2] [Set flags and partition types]](#Set_flags_and_partition_types)
        -   [[5.2.3] [Save the new partition table]](#Save_the_new_partition_table)
    -   [[5.3] [Make filesystems]](#Make_filesystems)
-   [[6] [Fetch the Gentoo bits of the install]](#Fetch_the_Gentoo_bits_of_the_install)
    -   [[6.1] [Install the arm64 stage 3]](#Install_the_arm64_stage_3)
    -   [[6.2] [Install a Gentoo repository snapshot]](#Install_a_Gentoo_repository_snapshot)
-   [[7] [Populating /boot]](#Populating_.2Fboot)
    -   [[7.1] [The Raspberry Pi Foundation provided files]](#The_Raspberry_Pi_Foundation_provided_files)
    -   [[7.2] [Install the kernel to the microSD card]](#Install_the_kernel_to_the_microSD_card)
        -   [[7.2.1] [Install the kernel binary]](#Install_the_kernel_binary)
        -   [[7.2.2] [Install the device tree]](#Install_the_device_tree)
        -   [[7.2.3] [Install the kernel modules]](#Install_the_kernel_modules)
        -   [[7.2.4] [Checking the kernel install]](#Checking_the_kernel_install)
-   [[8] [Raspberry Pi 3 peripherals]](#Raspberry_Pi_3_peripherals)
    -   [[8.1] [Serial port configuration]](#Serial_port_configuration)
    -   [[8.2] [Install Bluetooth firmware]](#Install_Bluetooth_firmware)
-   [[9] [Setup]](#Setup)
    -   [[9.1] [/etc/fstab]](#.2Fetc.2Ffstab)
    -   [[9.2] [/boot/config.txt]](#.2Fboot.2Fconfig.txt)
    -   [[9.3] [Alternative: Use the /boot/config.txt file from a working Raspbian install]](#Alternative:_Use_the_.2Fboot.2Fconfig.txt_file_from_a_working_Raspbian_install)
    -   [[9.4] [/boot/cmdline.txt]](#.2Fboot.2Fcmdline.txt)
    -   [[9.5] [Alternative: Use the /boot/cmdline.txt file from a working Raspbian install]](#Alternative:_Use_the_.2Fboot.2Fcmdline.txt_file_from_a_working_Raspbian_install)
    -   [[9.6] [Setting the console keymap]](#Setting_the_console_keymap)
-   [[10] [What next]](#What_next)
    -   [[10.1] [Random hints]](#Random_hints)
        -   [[10.1.1] [WiFi and Bluetooth]](#WiFi_and_Bluetooth)
        -   [[10.1.2] [CFLAGS]](#CFLAGS)
        -   [[10.1.3] [MAKEOPTS]](#MAKEOPTS)
        -   [[10.1.4] [Networking]](#Networking)
        -   [[10.1.5] [sshd]](#sshd)
    -   [[10.2] [Updating the tool chain]](#Updating_the_tool_chain)
    -   [[10.3] [Useful packages]](#Useful_packages)
        -   [[10.3.1] [Network time sync]](#Network_time_sync)
-   [[11] [Troubleshooting]](#Troubleshooting)
    -   [[11.1] [No video output]](#No_video_output)
    -   [[11.2] [Not booting]](#Not_booting)
-   [[12] [Where to get help]](#Where_to_get_help)
-   [[13] [Acknowledgements]](#Acknowledgements)

## [Overview]

### [History]

The Raspberry Pi 3 with a 64-bit capable CPU became available on Feb. 2016. At the outset, it was difficult to install Gentoo on the Pi 3 in 64-bit mode. A lot of work by a lot of people has almost brought a 64-bit Gentoo install on the Pi 3 down to almost a standard handbook install.

Currently the raspberrypi-userland is not fully supported in 64-bit userland, therefore e.g. the raspberry pi camera will not work natively here.

### [What works]

All the Pi 3 hardware is supported in 64-bit mode.

-   Wi-Fi
-   USB
-   Ethernet (needs USB)
-   Bluetooth
-   Hardware Video Acceleration
-   Sound over HDMI
-   Video output through DSI

### [Untested]

-   PAL/NTSC video output
-   Analogue sound output

### [Whats required]

-   Gentoo install (or prefix install) on a PC
-   microSD card reader for the PC
-   Raspberry Pi 3
-   microSD card \> 8G
-   USB keyboard
-   USB mouse
-   HDMI display

The content of the microSD card will be wiped during the install.

## [Installation overview]

Install crossdev on the PC.

Fetch the Raspberry Pi firmware.

Fetch the Raspberry Pi kernel.

Partition the microSD card.

Fetch the Gentoo bits of the install.

~~Cross compile and install the kernel.~~

Setup.

Boot the Pi to test.

~~== Install crossdev on the PC ==~~

** Tip**\
This section is no longer required as the Pi Foundation provides a 64 bit kernel.

There are no prebuilt kernel images for the Pi 3 in its arm64 mode. Until an **[arm64]** kernel is running, the system cannot boot in 64-bit mode. It\'s a chicken and egg problem. Once the Pi is bootstrapped with a kernel, it can build its own kernels.

crossdev is Gentoos\' tool for building cross compiler tool chains. Once its installed, we will use it to build the **[arm64]** kernel on the Gentoo PC. Install the crossdev tool:

`root `[`#`]`emerge --ask sys-devel/crossdev`

### [Using crossdev to build a cross compiler]

`root `[`#`]`crossdev -t aarch64-unknown-linux-gnu`

An [overlay may need nominated](https://wiki.gentoo.org/wiki/Crossdev#Crossdev_overlay "Crossdev") to store the cross ebuilds, crossdev will provide an alert if this is the case.

** Important**\
Crossdev may insist that many of the files in [/etc/portage/] are directories

Convert files as crossdev asks e.g.

    error: please convert /etc/portage/package.env to a directory

by appending \_file to the existing filename

`root `[`#`]`mv /etc/portage/package.env /etc/portage/package.env_file`

making the directory

`root `[`#`]`mkdir /etc/portage/package.env`

then moving [package.env_file] into the directory.

`root `[`#`]`mv /etc/portage/package.env_file /etc/portage/package.env`

Rinse and repeat until crossdev is happy.

crossdev will take a while. It\'s building the following packages:

-   binutils: binutils-\[latest\]
-   gcc: gcc-\[latest\]
-   Linux headers: linux-headers-\[latest\]
-   libc:glibc-\[latest\]

When crossdev completes a cross toolchain will be available:

`user `[`$`]`gcc-config -l `

    [1] aarch64-unknown-linux-gnu-9.3.0 *
    [2] x86_64-pc-linux-gnu-9.3.0 *

It will also create an **[arm64]** target root in [/usr/aarch64-unknown-linux-gnu] This is used by cross emerge.

Pure cross compiling packages, other than the kernel, is out of scope of this guide.

## [Fetch the Raspberry Pi firmware]

** Tip**\
This section is no longer required as the Pi Foundation provides a 64 bit kernel. See [Raspberry_Pi_Install_Guide#Installing_the_Raspberry_Pi_Foundation_files](https://wiki.gentoo.org/wiki/Raspberry_Pi_Install_Guide#Installing_the_Raspberry_Pi_Foundation_files "Raspberry Pi Install Guide")

The Raspberry Pi firmware is maintained in a git repository. Git will be needed to obtain a copy of the firmeware files.

`root `[`#`]`emerge --ask dev-vcs/git`

As a normal user, create a directory somewhere for raspberry pi firmware and kernel files:

`user `[`$`]`mkdir ~/raspberrypi`

Clone the firmware sources:

** Important**\
The stable branch of the following git repo has been confirmed to work. The master branch may or may not work depending on your build. Unless you know what you\'re doing, just use the stable branch.

`user `[`$`]`cd ~/raspberrypi `

`user `[`$`]`git clone -b stable --depth=1 https://github.com/raspberrypi/firmware `

The [/boot] directory will be needed out of the master branch. The `--depth` option is used so that not all the history will be fetched (it is unnecessary). This will save a lot of space, bandwidth, and time.

There is nothing to build. [\~/raspberrypi/firmware/boot] is used as is.

## [][Fetch, configure, and build the Raspberry Pi kernel]

** Tip**\
This section is no longer required as the Pi Foundation provides a 64 bit kernel. See [Raspberry_Pi_Install_Guide#Installing_the_Raspberry_Pi_Foundation_files](https://wiki.gentoo.org/wiki/Raspberry_Pi_Install_Guide#Installing_the_Raspberry_Pi_Foundation_files "Raspberry Pi Install Guide")

### [Fetch the Raspberry Pi kernel]

Stay in [raspberrypi] directory and run:

`user `[`$`]`git clone --depth=1 https://github.com/raspberrypi/linux -b rpi-5.10.y`

With absolutely no fanfare at all, 64-bit support was added to this kernel tree late in 2016. No more searching for odd patches.

Not everything has been accepted by the mainline kernel yet but it\'s getting closer. Feel free to test mainline kernel builds every once in a while. If it builds successfully and the Rpi can be used to test successful boot, then this section of the guide can be updated with instructions for mainline Linux.

The master/main Raspberry Pi Foundation branch may be broken. Test if needed. It is better to use a tagged release branch. At the time of writing that is rpi-5.10.y. The 5.10 mainline kernel is still at -rc status. Checkout should be optional and will work only if \--depth option is omitted (beware, **large** repo).

`user `[`$`]`cd linux `

`user `[`$`]`git checkout rpi-5.10.y `

    Checking out files: 100% (33079/33079), done.

    Branch rpi-5.10.y set up to track remote branch rpi-5.10.y from origin.

    Switched to a new branch 'rpi-5.10.y'

With the kernel source tree in place, ready for configuring and cross compiling.

### [Configure the kernel]

** Important**\
`ARCH=arm64` must be specified everywhere or the kernel build system will use the host arch. This will destroy the arm64 [.config] file

As user:

`user `[`$`]`cd ~/raspberrypi/linux`

The [bcmrpi3_defconfig] config file is almost right as it stands. It defaults to the powersave CPU governor, which runs the Pi at 600MHz.

All the governors are there. The ondemand governor is recommended.

`user `[`$`]`ARCH=arm64 CROSS_COMPILE=aarch64-unknown-linux-gnu- make bcmrpi3_defconfig`

Either use menuconfig to change the default CPU governor, add something to the kernel command line, or change it after booting.

`user `[`$`]`ARCH=arm64 CROSS_COMPILE=aarch64-unknown-linux-gnu- make menuconfig`

Search for `CPU_FREQ_DEFAULT_GOV` go to that location and set the default to ondemand. Exit menuconfig, saving the change.

\

    .config - Linux/arm64 5.10.88-raspberrypi Kernel Configuration
     > CPU Power Management > CPU Frequency scaling ──────────────────────────────────
      ┌────────────────────────── CPU Frequency scaling ───────────────────────────┐
      │  Arrow keys navigate the menu.  <Enter> selects submenus ---> (or empty    │
      │  submenus ----).  Highlighted letters are hotkeys.  Pressing <Y> includes, │
      │  <N> excludes, <M> modularizes features.  Press <Esc><Esc> to exit, <?>    │
      │  for Help, </> for Search.  Legend: [*] built-in  [ ] excluded  <M> module │
      │ ┌────────────────────────────────────────────────────────────────────────┐ │
      │ │    [*] CPU Frequency scaling                                           │ │
      │ │    [*]   CPU frequency transition statistics                           │ │
      │ │    [ ]     CPU frequency transition statistics details                 │ │
      │ │          Default CPUFreq governor (powersave)  --->                    │ │
      │ │    <*>   'performance' governor                                        │ │
      │ │    -*-   'powersave' governor                                          │ │
      │ │    <*>   'userspace' governor for userspace frequency scaling          │ │
      │ │    <*>   'ondemand' cpufreq policy governor                            │ │

The kernel [.config] contains lots of support for hardware you don\'t have and possibly have never heard of. More confident readers may be tempted to trim things out now. A word of advice - **don\'t**, at least, not until the system boots.

### [Cross compiling the kernel]

The build is conventional, other than telling the build system to build for arm64 and use the cross compiler.

`user `[`$`]`ARCH=arm64 CROSS_COMPILE=aarch64-unknown-linux-gnu- make -jN`

Change `N` to the number of parallel make jobs you want to run. Convention is N number of CPU cores + 1.

## [Partition the microSD card]

** Tip**\
Follow [Raspberry_Pi_Install_Guide#Preparing_the_disks](https://wiki.gentoo.org/wiki/Raspberry_Pi_Install_Guide#Preparing_the_disks "Raspberry Pi Install Guide") instead of this section

** Warning**\
This step will destroy ALL the data on the microSD card

### [Background]

The Raspberry Pi does not need a boot loader. There is no firmware for the ARM CPU, like there is in a PC. Instead, the GPU manages loading software for the CPU to execute, while the CPU is held reset. Its the GPU that has the \'BIOS\' that gets everything started.

This makes it impossible to brick the Pi, since at worst, the microSD card needs to be reloaded.

This arrangement does impose some constraints on the microSD card.

    The partition table must be MSDOS
    The first partition (/boot) must be vfat.

The [bootcode.bin] file has some useful defaults that make setup easier, which we will take advantage of later.

### [Partitioning]

Depending on how the microSD card is connected to the PC, it may be [/dev/sdX] or [/dev/mmcblkY]

** Warning**\
Check! Do get it right - Don\'t ruin your PC install

In the example below, it\'s [/dev/sdk].

Using the partitioning tool of your choice, make three partitions on your microSD card.

    boot 128Mb
    swap 2G
    root (/) the rest.

Using [fdisk], and your microSD card block device, not my [/dev/sdk]

`root `[`#`]`fdisk /dev/...`

#### [Make the partition table and add partitions]

Make a new MS-DOS disklabel

    Command (m for help): o

Add a new partition - this will be 128Mb for [/boot]

    Command (m for help): n
    Partition type
       p   primary (0 primary, 0 extended, 4 free)
       e   extended (container for logical partitions)
    Select (default p): p
    Partition number (1-4, default 1): 1
    First sector (2048-15523839, default 2048):
    Last sector, +sectors or +size (2048-15523839, default 15523839): +128M

Has created a new partition 1 of type \'Linux\' and of size 128 MiB.

Add a 2G partition 2 for swap.

Put the remaining space in partition 3 for root.

Check with

    Command (m for help): p

Using an 8G microSD card it should show

    Device     Boot   Start      End  Sectors  Size Id Type
    /dev/sdk1          2048   264191   262144  128M 83 Linux
    /dev/sdk2        264192  4458495  4194304    2G 83 Linux
    /dev/sdk3       4458496 15523839 11065344  5.3G 83 Linux

#### [Set flags and partition types]

Toggle the bootable flag on partition 1

    Command (m for help): a
    Partition number (1-3, default 3): 1

The bootable flag on partition 1 is enabled now.

Mark partition 1 as FAT

    Command (m for help): t
    Partition number (1-3, default 3): 1
    Partition type (type L to list all types): c

    Changed type of partition 'Linux' to 'W95 FAT32 (LBA)'.

** Important**\
The Pi checks the type of partition 1 in the partition table and will not boot if its 82

Mark partition 2 as swap

    Command (m for help): t
    Partition number (1-3, default 3): 2
    Partition type (type L to list all types): 82

    Changed type of partition 'Linux swap / Solaris' to 'Linux swap / Solaris'.

Check again.

    Device     Boot   Start      End  Sectors  Size Id Type
    /dev/sdk1  *       2048   264191   262144  128M  c W95 FAT32 (LBA)
    /dev/sdk2        264192  4458495  4194304    2G 82 Linux swap / Solaris
    /dev/sdk3       4458496 15523839 11065344  5.3G 83 Linux

#### [Save the new partition table]

** Warning**\
Nothing has been written to the microSD card yet. This is the last opportunity to back out

Exit [fdisk] with either [w] or [q]

      w   write table to disk and exit
      q   quit without saving changes

### [Make filesystems]

You know the block devices from the partitioning step above. Fill in the \... to match your system.

vfat for [/boot]

`root `[`#`]`mkfs -t vfat -F 32 /dev/...1`

** Important**\
Be sure to add the `-F 32` switch. When using [mkfs] to make a vfat file system and `-F 32` is not explicitly defined, [mkdosfs] will automatically select between 12, 16 and 32-bit, whatever [mkdosfs] thinks will fit better for the file system size, which in this case it would default to FAT16. This partition MUST be formatted FAT32 in order for the Raspberry Pi to boot.

[mkswap] for swap

`root `[`#`]`mkswap /dev/...2`

ext4 for root

`root `[`#`]`mkfs -i 8192 -t ext4 /dev/...3 `

** Important**\
`-i 8192` makes an inode for every two filesystem blocks, 8kB

The inode count cannot be changed after filesystem creation and can limit the number of files on a files system. The Gentoo repository alone needs over 17,000 inodes.

## [Fetch the Gentoo bits of the install]

** Tip**\
Follow [Raspberry_Pi_Install_Guide#Installing_the_Gentoo_installation_files](https://wiki.gentoo.org/wiki/Raspberry_Pi_Install_Guide#Installing_the_Gentoo_installation_files "Raspberry Pi Install Guide") instead of this section

To make it easy to cross refer to the [Gentoo_Handbook](https://wiki.gentoo.org/wiki/Gentoo_Handbook "Gentoo Handbook")

`root `[`#`]`mkdir /mnt/gentoo`

Mount the microSD card root filesystem at [/mnt/gentoo]

`root `[`#`]`mount /dev/xxx3 /mnt/gentoo`

### [Install the arm64 stage 3]

Fetch the [arm64 stage3](https://distfiles.gentoo.org/releases/arm64/autobuilds/) and untar it with

`root `[`#`]`tar xpvf stage3-*.tar.xz --xattrs-include='*.*' --numeric-owner -C /mnt/gentoo`

[/mnt/gentoo/tmp] should be empty.

### [Install a Gentoo repository snapshot]

*This step is not actually needed to boot the Pi but [emerge] won\'t work without it. No software can be installed without the Gentoo repository containing the ebuilds to emerge.*

Following the [Handbook](https://wiki.gentoo.org/wiki/Gentoo_Handbook "Gentoo Handbook") fetch and unpack a [Gentoo repository shapshot](https://distfiles.gentoo.org/snapshots/portage-latest.tar.bz2) in the normal way.

Careful readers can copy their host [/var/db/repos/gentoo] as long as [./packages] and [./distfiles] are omitted.

If [emerge-webrsync] is not able to be executed, unpack the Gentoo repository snapshot manually like the following.

`root `[`#`]`tar xvpf portage-latest.tar.bz2 --strip-components=1 -C /mnt/gentoo/var/db/repos/gentoo`

## [][Populating /boot]

** Tip**\
Follow [Raspberry_Pi_Install_Guide#Installing_the_Raspberry_Pi_Foundation_files](https://wiki.gentoo.org/wiki/Raspberry_Pi_Install_Guide#Installing_the_Raspberry_Pi_Foundation_files "Raspberry Pi Install Guide") instead of this section

### [The Raspberry Pi Foundation provided files]

Mount the microSD card boot at [/mnt/gentoo/boot]. (The microSD card root should still be mounted at [/mnt/gentoo])

`root `[`#`]`mount /dev/xxx1 /mnt/gentoo/boot`

As root, copy the content of your normal users [\~/raspberrypi/firmware/boot] to [/mnt/gentoo/boot].

`root `[`#`]`cp -rv ~/raspberrypi/firmware/boot/* /mnt/gentoo/boot`

You should end up with files in [/mnt/gentoo/boot], not a directory called [boot].

Not all the files there are required. It\'s a one size fits all for all models of Raspberry Pi operating in 32-bit mode.

### [Install the kernel to the microSD card]

The kernel was built above, now to install it. The kernel is in three parts:

1.  Kernel binary.
2.  Kernel modules.
3.  The device tree.

#### [Install the kernel binary]

As root, copy the kernel binary from the build location

`root `[`#`]`cp /home/<user>/raspberrypi/linux/arch/arm64/boot/Image /mnt/gentoo/boot/kernel8.img`

** Important**\
If the [/boot/kernel8.img] file exists, the [bootcode.bin] sets up the Pi for 64-bit operation and loads [/boot/kernel8.img] as the kernel.

It is possible to use other kernel file names by adding entries to [/boot/config.txt]

** Important**\
If you do not choose to edit [/boot/config.txt], you need to delete [/boot/kernel.img] and [/boot/kernel7.img], or the firmware will load them instead of the kernel that was just installed.

#### [Install the device tree]

The device tree binary ([.dtb]) describes the hardware to the kernel. This avoids having all the existing hardware configurations hard coded into the kernel.

Due to the way the Raspberry Pi 64-bit kernel support has been added, there are going to be two different device trees with the same file name. A 32-bit version and a 64-bit version. They are not interchangeable. Move the 32-bit version out of the way.

For Raspberry Pi 3B:

`root `[`#`]`mv /mnt/gentoo/boot/bcm2710-rpi-3-b.dtb /mnt/gentoo/boot/bcm2710-rpi-3-b.dtb_32`

For Raspberry Pi 3B Plus:

`root `[`#`]`mv /mnt/gentoo/boot/bcm2710-rpi-3-b-plus.dtb /mnt/gentoo/boot/bcm2710-rpi-3-b-plus.dtb_32`

That\'s renamed the 32-bit version.

Copy the dtb from the build location

For Raspberry Pi 3B:

`root `[`#`]`cp /home/<user>/raspberrypi/linux/arch/arm64/boot/dts/broadcom/bcm2710-rpi-3-b.dtb /mnt/gentoo/boot`

For Raspberry Pi 3B Plus:

`root `[`#`]`cp /home/<user>/raspberrypi/linux/arch/arm64/boot/dts/broadcom/bcm2710-rpi-3-b-plus.dtb /mnt/gentoo/boot`

It is possible to use other device tree file names by adding entries to [/boot/config.txt]

#### [Install the kernel modules]

From the top of the kernel tree, install the kernel modules.

`root `[`#`]`cd /home/<user>/raspberrypi/linux `

`root `[`#`]`ARCH=arm64 CROSS_COMPILE=aarch64-unknown-linux-gnu- make modules_install INSTALL_MOD_PATH=/mnt/gentoo `

The `INSTALL_MOD_PATH` is the root of the filesystem the modules are to be installed into. Due to kernel naming

`user `[`$`]`uname -a `

    Linux Pi3 64bit 4.10.0-rc6-v8+ #2 SMP PREEMPT Thu Feb 2 20:34:34 GMT 2017 aarch64 GNU/Linux

it\'s unlikely you will have a 4.10.0-rc6-v8+ so omitting `INSTALL_MOD_PATH` is probably harmless to your build host install.

#### [Checking the kernel install]

`root `[`#`]`ls /mnt/gentoo/boot `

    COPYING.linux           bcm2708-rpi-cm.dtb      bcm2710-rpi-cm3.dtb  fixup_db.dat  kernel8.img   start_db.elf
    LICENCE.broadcom        bcm2709-rpi-2-b.dtb     bootcode.bin         fixup_x.dat   overlays      start_x.elf
    bcm2708-rpi-b-plus.dtb  bcm2710-rpi-3-b.dtb     fixup.dat            kernel.img    start.elf
    bcm2708-rpi-b.dtb       bcm2710-rpi-3-b.dtb_32  fixup_cd.dat         kernel7.img   start_cd.elf

Notice the two [bcm2710-rpi-3-b.dtb] device tree binaries and the [kernel8.img].

`root `[`#`]`ls /mnt/gentoo/lib/modules `

    4.10.0-rc6-v8+

~~Shows that the kernel modules were installed to the correct location.~~

## [Raspberry Pi 3 peripherals]

Now that we have the base operating system in, we will need to do some file configuration by hand to get the peripherals working.

### [Serial port configuration]

The Gentoo stage 3 comes with the default Gentoo serial port configuration. In Raspbian Jessie, udev rules exist that provide aliases for GPIO14:15 ([/dev/serial0]) and the Bluetooth serial port ([/dev/serial1]). If you\'re not using the pi3-miniuart-bt or the pi3-disable-bt device tree overlays, [ttyS0] (mini UART) points to [/dev/serial0] (GPIO14:15) while [ttyAMA0] (Bluetooth) points to [/dev/serial1] (Bluetooth).

If, however, the pi3-miniuart-bt overlay is in use, udev rules automagically make [ttyAMA0] point to [/dev/serial0] (GPIO14:15) while [ttyS0] points to [/dev/serial1] (Bluetooth). If the pi3-disable-bt overlay is in use, [ttyAMA0] still points to [/dev/serial0] (GPIO14:15) while Bluetooth/[ttyS0] are disabled.

This allows the use of [/dev/serial1] in any Bluetooth configuration files and command line arguments regardless of which serial port it is assigned to. It also allows the use of /[dev/serial0] in any apps and/or configuration files/command line arguments which reference the GPIO14:15 pins regardless of which overlay is/is not in use.

In order to make things easier when working with the device tree overlays for the Bluetooth module as well as any applications which were written in a Raspbian environment that uses the [serial0] and [serial1] aliases, we\'ll need to first create a udev rule to mimic this behavior.

Open up [/mnt/gentoo/etc/inittab] -

`root `[`#`]`nano -w /mnt/gentoo/etc/inittab`

Find this line and comment it out by prepending a \# at the beginning of the line -

[FILE] **`/mnt/gentoo/etc/inittab`**

    f0:12345:respawn:/sbin/agetty 9600 ttyAMA0 vt100

Save and exit the file. This prevents Gentoo from assigning the serial console to [ttyAMA0] on [/root] mount, which will conflict with Bluetooth operation if left uncommented.

Next, create the empty file [99-com.rules] in [/mnt/gentoo/etc/udev/rules.d] -

`root `[`#`]`nano -w /mnt/gentoo/etc/udev/rules.d/99-com.rules`

Copy and paste this into the empty file, then save and exit the file -

[FILE] **`/mnt/gentoo/etc/udev/rules.d/99-com.rules`**

    SUBSYSTEM=="input", GROUP="input", MODE="0660"
    SUBSYSTEM=="i2c-dev", GROUP="i2c", MODE="0660"
    SUBSYSTEM=="spidev", GROUP="spi", MODE="0660"
    SUBSYSTEM=="bcm2835-gpiomem", GROUP="gpio", MODE="0660"

    SUBSYSTEM=="gpio*", PROGRAM="/bin/sh -c '\
            chown -R root:gpio /sys/class/gpio && chmod -R 770 /sys/class/gpio;\
            chown -R root:gpio /sys/devices/virtual/gpio && chmod -R 770 /sys/devices/virtual/gpio;\
            chown -R root:gpio /sys$devpath && chmod -R 770 /sys$devpath\
    '"

    KERNEL=="ttyAMA[01]", GROUP="dialout", PROGRAM="/bin/sh -c '\
            ALIASES=/proc/device-tree/aliases; \
            if cmp -s $ALIASES/uart0 $ALIASES/serial0; then \
                    echo 0;\
            elif cmp -s $ALIASES/uart0 $ALIASES/serial1; then \
                    echo 1; \
            else \
                    exit 1; \
            fi\
    '", SYMLINK+="serial%c"

    KERNEL=="ttyS0", GROUP="dialout", PROGRAM="/bin/sh -c '\
            ALIASES=/proc/device-tree/aliases; \
            if cmp -s $ALIASES/uart1 $ALIASES/serial0; then \
                    echo 0; \
            elif cmp -s $ALIASES/uart1 $ALIASES/serial1; then \
                    echo 1; \
            else \
                    exit 1; \
            fi \
    '", SYMLINK+="serial%c"

This will assign [ttyS0] and [ttyAMA0] to the [dialout] group just as they are in Raspbian Jessie. It will also provide the [serial0] (GPIO14:15) and [serial1] (Bluetooth) aliases, which eases the task of switching the serial ports around between the Bluetooth and GPIO14:15.

~~=== Install Wi-Fi firmware ===~~

** Tip**\
The firmware files listed here are now in linux-firmware

The Raspberry Pi 3 WiFi requires firmware to operate. The files [brcmfmac43430-sdio.raspberrypi,3-model-b.txt] and [brcmfmac43430-sdio.bin] are both required to be present in [/mnt/gentoo/lib/firmware/brcm] for Raspberry Pi 3B, while the files [brcmfmac43455-sdio.raspberrypi,3-model-b-plus.txt] and [brcmfmac43455-sdio.bin] are required for Raspberry Pi 3B Plus.

They can be downloaded via [git.kernel.org](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/tree/brcm) or [github.com/armbian](https://github.com/armbian/firmware/raw/master/brcm/).

Create the firmware directory:

`root `[`#`]`mkdir -p /mnt/gentoo/lib/firmware/brcm`

Fetch the Raspberry Pi 3B Wireless Firmware:

`root `[`#`]`wget -P /mnt/gentoo/lib/firmware/brcm https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/brcm/brcmfmac43430-sdio.raspberrypi,3-model-b.txt `

`root `[`#`]`wget -P /mnt/gentoo/lib/firmware/brcm https://github.com/armbian/firmware/raw/master/brcm/brcmfmac43430-sdio.bin `

Fetch the Raspberry PI 3B+ Wireless Firmware:

`root `[`#`]`wget -P /mnt/gentoo/lib/firmware/brcm https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/brcm/brcmfmac43455-sdio.raspberrypi,3-model-b-plus.txt `

`root `[`#`]`wget -P /mnt/gentoo/lib/firmware/brcm https://github.com/armbian/firmware/raw/master/brcm/brcmfmac43455-sdio.bin `

~~=== Kernel ===~~

~~You\'ll also want to ensure that Broadcom IEEE802.11n embedded FullMAC WLAN driver with SDIO bus interface support is enabled in the kernel. In the menu shown below, this is all that needs to be enabled. You can set the FullMAC WLAN driver as a module or compile it into the kernel. If you plan to use only the onboard WiFi, everything else under the Wireless LAN menu can be disabled.~~

[KERNEL]

    Device Drivers-->
      Network Device Support-->
                  Wireless LAN-->
                   [*]   Broadcom devices
                   < >     Broadcom 43xx wireless support (mac80211 stack)
                   < >     Broadcom 43xx-legacy wireless support (mac80211 stack)
                   < >     Broadcom IEEE802.11n PCIe SoftMAC WLAN driver
                  <*/M>    Broadcom FullMAC WLAN driver
                   [*]     SDIO bus interface support for FullMAC driver
                   [ ]     USB bus interface support for FullMAC driver
                   [ ]     Broadcom device tracing
                   [ ]     Broadcom driver debug functions

~~Once the firmware files are copied over to [/mnt/gentoo/lib/firmware/brcm], the appropriate kernel settings are built, and a wireless network manager (such as wpa_supplicant) is installed, the WiFi should work.~~

### [Install Bluetooth firmware]

** Tip**\
This section is still required - these files are not in linux-firmware

The Raspberry Pi 3B needs the [BCM43430A1.hcd] firmware file, and the Raspberry Pi 3B+ needs the [BCM4345C0.hcd] firmware file. The firmware files can be found in the Raspbian [bluez-firmware](https://github.com/RPi-Distro/bluez-firmware/tree/master/broadcom) GitHub repository. The firmware files need to be placed in the [/mnt/gentoo/lib/firmware/brcm] directory.

Create the firmware directory:

`root `[`#`]`mkdir -p /mnt/gentoo/lib/firmware/brcm`

Fetch the Raspberry Pi 3B Bluetooth firmware:

`root `[`#`]`wget -P /mnt/gentoo/lib/firmware/brcm https://raw.githubusercontent.com/RPi-Distro/bluez-firmware/master/broadcom/BCM43430A1.hcd`

Fetch the Raspberry Pi 3B+ Bluetooth firmware:

`root `[`#`]`wget -P /mnt/gentoo/lib/firmware/brcm https://raw.githubusercontent.com/RPi-Distro/bluez-firmware/master/broadcom/BCM4345C0.hcd`

After boot:

** Note**\
With an update to the firmware a new device tree overlay was introduced that enables autoprobing of Bluetooth driver without need of hciattach/btattach.

[FILE] **`/boot/config.txt`**

    dtparam=krnbt=on

With that parameter set, the bluetooth driver will be loaded automatically and no further action is required.

Attach the serial device [/dev/ttyAMA0] to the Bluetooth stack using [btattach], which is provided by the [[[net-wireless/bluez]](https://packages.gentoo.org/packages/net-wireless/bluez)[]] package:

`root `[`#`]`btattach -B /dev/ttyAMA0 -P bcm -S 3000000`

Alternatively, [hciattach] can be used if [[[net-wireless/bluez]](https://packages.gentoo.org/packages/net-wireless/bluez)[]] is built with the `deprecated` USE flag enabled:

`root `[`#`]`hciattach /dev/ttyAMA0 bcm43xx 3000000 flow - <bdaddr>`

Both commands will create a HCI device (e.g. [hci0]) in [/sys/class/bluetooth] and load the required firmware. To have the HCI device created at boot using [btattach], the following [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") init script can be used:

[FILE] **`/mnt/gentoo/etc/init.d/btattach`**

    #!/sbin/openrc-run

    command="/usr/bin/btattach"
    command_args="-B /dev/ttyAMA0 -P bcm -S 3000000"
    command_background=true
    pidfile="/run/btattach.pid"

    depend()

Make the init script executable:

`root `[`#`]`chmod +x /mnt/gentoo/etc/init.d/btattach`

After booting Pi

Start [btattach]:

`root `[`#`]`rc-service btattach start`

Start [btattach] at boot:

`root `[`#`]`rc-update add btattach default`

## [Setup]

** Note**\
Don\'t do it like this. Its not wrong, it needs a chroot and that will not be described in detail

The chroot environment is very handy as it allows you to configure your startup run levels ([rc-update]) as well as update your Portage snapshot ([emerge \--sync]). Additionally, you can set the root password as well as create users in the chroot environment.

If you plan to only access your Pi via SSH, you\'ll need at least networking on startup, which requires either net.eth0 or dhcpcd to be added to the default run level, as well as OpenSSH itself (sshd).

Much of the setup prior to booting a new Gentoo install is done in a chroot. Chrooting into an arm64 install from some other arch is beyond the scope of this guide. Instead, only the bare minimum setup from outside the chroot is covered. Consult the [Embedded Handbook/General/Compiling with qemu user chroot](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Compiling_with_qemu_user_chroot "Embedded Handbook/General/Compiling with qemu user chroot") page to learn how to use qemu to establish a cross-chroot.

~~=== Root password ===~~

** Important**\
You need this to be able to log in at all

There are several ways to generate a password hash for [/etc/shadow]. I usually copy the hash from another system. My Pi uses an [/etc/shadow] root entry:

    root:$6$xxPVR/Td5iP$/7Asdgq0ux2sgNkklnndcG4g3493kUYfrrdenBXjxBxEsoLneJpDAwOyX/kkpFB4pU5dlhHEyN0SK4eh/WpmO0::0:99999:7:::

The matching password is raspberry.

Feel free to use that line to replace the root entry in [/mnt/gentoo/etc/shadow]

You can change the password once you are logged in.

### [][/etc/fstab]

On the Pi, the microSD card will be [/dev/mmcblk0] with partitions [/dev/mmcblk0p1], [/dev/mmcblk0p2], and [/dev/mmcblk0p3]

Edit [/mnt/gentoo/etc/fstab] to match.

[FILE] **`/mnt/gentoo/etc/fstab`**

    /dev/mmcblk0p1          /boot           vfat            noauto,noatime  1 2
    /dev/mmcblk0p2          none            swap            sw              0 0
    /dev/mmcblk0p3          /               ext4            noatime         0 1

### [][/boot/config.txt]

This file will not exist until its created. Create it with the following content.

[FILE] **`/mnt/gentoo/boot/config.txt`**

    # have a properly sized image
    disable_overscan=1

    # lets have the VC4 hardware accelerated video
    dtoverlay=vc4-fkms-v3d

    # for sound over HDMI
    hdmi_drive=2

    # Enable audio (loads snd_bcm2835)
    dtparam=audio=on

    # gpu_mem is for closed-source driver only; since we are only using the
    # open-source driver here, set low
    gpu_mem=16

    # Force booting in 64bit mode
    arm_64bit=1

** Warning**\
dtoverlay=vc4-fkms-v3d is the depreciated fake kms. Try dtoverlay=vc4-kms-v3d instead

### [][Alternative: Use the /boot/config.txt file from a working Raspbian install]

Here is a [config.txt] file from a working Raspbian install. If the above does not work, this one should.

[FILE] **`/mnt/gentoo/boot/config.txt`**

    # For more options and information see
    # http://rpf.io/configtxt
    # Some settings may impact device functionality. See link above for details

    # uncomment if you get no picture on HDMI for a default "safe" mode
    #hdmi_safe=1

    # uncomment this if your display has a black border of unused pixels visible
    # and your display can output without overscan
    disable_overscan=1

    # uncomment the following to adjust overscan. Use positive numbers if console
    # goes off screen, and negative if there is too much border
    #overscan_left=16
    #overscan_right=16
    #overscan_top=16
    #overscan_bottom=16

    # uncomment to force a console size. By default it will be display's size minus
    # overscan.
    #framebuffer_width=1280
    #framebuffer_height=720

    # uncomment if hdmi display is not detected and composite is being output
    #hdmi_force_hotplug=1

    # uncomment to force a specific HDMI mode (this will force VGA)
    #hdmi_group=1
    #hdmi_mode=1

    # uncomment to force a HDMI mode rather than DVI. This can make audio work in
    # DMT (computer monitor) modes
    #hdmi_drive=2

    # uncomment to increase signal to HDMI, if you have interference, blanking, or
    # no display
    #config_hdmi_boost=4

    # uncomment for composite PAL
    #sdtv_mode=2

    #uncomment to overclock the arm. 700 MHz is the default.
    #arm_freq=800

    # Uncomment some or all of these to enable the optional hardware interfaces
    #dtparam=i2c_arm=on
    #dtparam=i2s=on
    #dtparam=spi=on

    # Uncomment this to disable the Bluetooth module on /dev/ttyAMA0
    dtoverlay=pi3-miniuart-bt

    # Uncomment this to enable the lirc-rpi module
    #dtoverlay=lirc-rpi

    # Additional overlays and parameters are documented /boot/overlays/README

    # Enable audio (loads snd_bcm2835)
    dtparam=audio=on

    # NOOBS Auto-generated Settings:
    #hdmi_force_hotplug=1
    enable_uart0=1
    gpu_mem=128

### [][/boot/cmdline.txt]

This file will not exist until its created. Create it with the following content.

[FILE] **`/mnt/gentoo/boot/cmdline.txt`**

    root=/dev/mmcblk0p3 rootfstype=ext4 rootwait

This boots the Pi with a kernel command line of

    8250.nr_uarts=0 cma=256M@256M dma.dmachans=0x7f35 bcm2708_fb.fbwidth=1920 bcm2708_fb.fbheight=1080 bcm2709.boardrev=0xa02082 bcm2709.serial=0x8e2830fe smsc95xx.macaddr=B8:27:EB:28:30:FE bcm2708_fb.fbswap=1 bcm2709.uart_clock=48000000 vc_mem.mem_base=0x3dc00000 vc_mem.mem_size=0x3f000000  root=/dev/mmcblk0p3 rootfstype=ext4 rootwait

It really is one long line.

### [][Alternative: Use the /boot/cmdline.txt file from a working Raspbian install]

Here is the [cmdline.txt] file from a working Raspbian install. If the above does not work, this one should. Be sure to set `root` to your root partition, and `rootfstype` to your partition type. [/dev/mmcblk0p7] and `ext4` are shown below as examples.

[FILE] **`/mnt/gentoo/boot/cmdline.txt`**

    dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p7 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait

### [Setting the console keymap]

This step is optional if you can log in using the default

    keymap="us"

Set the keymap to something you use, e.g.

[FILE] **`/mnt/gentoo/etc/conf.d/keymaps`**

    keymap="dvorak-uk"

~~== Boot the Pi to test ==~~

~~Unmount the microSD card.~~

`root `[`#`]`umount /mnt/gentoo/boot `

`root `[`#`]`umount /mnt/gentoo `

When the prompt returns, move the microSD card to the Raspberry Pi and power on.

For 10 seconds (it seems much longer) you should see the GPU \'Rainbow\' test pattern, then the familiar boot messages.

Log in at the Pi console. Nothing was added to any runlevels during the install, so networking was not started, nor anything that depends on networking, like ntpd and sshd.

~~The Pi does not have a hardware real time clock. Its time will be Jan 1, 1970.~~

## [What next]

As always with Gentoo, if it booted, that\'s the hard bit done.

    All The setup steps in the Gentoo Handbook
    Fix the MAC address or use a static IP
    Allow root logins via ssh
    Add a crond, a logger and other things the handbook does before the reboot.
    Add Kernel Sources (or at least the .config)

### [Random hints]

#### [WiFi and Bluetooth]

It\'s unlikely that WiFi or Bluetooth will work at first boot. Expect to add some control tools for both.

#### [CFLAGS]

** Note**\
You could use `-ftree-vectorize` and/or `-Os` but they may cause more build failures or, in the case of vectorize, issues at runtime.

    CFLAGS="-march=armv8-a+crc -mtune=cortex-a53 -O2 -pipe"

gcc-6.x allows the use of `-march=native` but that will prevent the use of distcc. The above is the same as gcc-11.2 would set for `-march=native` anyway.

#### [MAKEOPTS]

With only 1G RAM, and four cores, the conventional `MAKEOPTS="-j4"` is a bit aggressive for building larger things. It will force swapping or even appear to lock up the Pi completely, to the point where it won\'t even respond to the console.

Use files in [/etc/portage/env/] and entries in [/etc/portage/package.env] to set `MAKEOPTS` on a per package basis.

#### [Networking]

Note that [dhcpcd] is not in the stage 3, nor is `eth0` in the default runlevel.

Install netifrc, dhcpcd, and add to openrc.

`root `[`#`]`emerge --ask --noreplace net-misc/netifrc net-misc/dhcpcd`

Depending on user requirements set the eth0 configuration.

[FILE] **`/etc/conf.d/net`**

    config_eth0="dhcp"

or

[FILE] **`/etc/conf.d/net`**

    config_eth0="192.168.0.2/24"
    routes_eth0="default via 192.168.0.1"

`root `[`#`]`ln -sr /etc/init.d/net.lo /etc/init.d/net.eth0`

`root `[`#`]`rc-update add net.eth0 default`

#### [sshd]

The default configuration for [sshd] will not allow password based root logins. A few possible solutions exist to this issue:

1.  Add a normal ssh public key for the root user. This involves logging in as the root user, then generating the keys.
2.  Add a normal user so the wheel group. Connect via SSH as this user, then use [su] or [sudo] to gain root privileges.
3.  Edit the [/etc/ssh/sshd_config] in order to allow password based root logins. This method of resolution is *insecure* and *not recommended*.

### [Updating the tool chain]

Once you boot, you may have the desire to update `@world` first thing. Once you\'ve booted the Raspberry Pi and confirmed that you have an internet connection, you\'ll want to first run [emerge \--sync] to get the absolute latest tree, then do a world upgrade.

`root `[`#`]`emerge --sync `

`root `[`#`]`emerge -auDN @world `

### [Useful packages]

#### [Network time sync]

The Raspberry Pi 3 does not have a hardware real time clock on board. There are vendors online where you can order RTC modules made for the Pi, but if you don\'t plan to run one, I highly recommend installing a NTP client.

First, we\'ll set the initial time using the [date] command. Date and time will be entered in `mmddhhmmyyyy` format and the time is in 24-hr format -

`root `[`#`]`date mmddhhmmyyyy`

As an example, if the time is 10:05PM on 7/31/2017 -

`root `[`#`]`date 073122052017`

As with most things Gentoo, the NTP daemon is just an emerge away -

`root `[`#`]`emerge --ask net-misc/ntp`

Or you can also use busybox variant:

`root `[`#`]`rc-update add busybox-ntpd default`

Don\'t forget to edit the config file:

[FILE] **`/etc/conf.d/busybox-ntpd`**

    # Config file for /etc/init.d/busybox-ntpd
    # run "/sbin/ntpd --help" to see all possible options.
    # Get time from specified server and run in background
    NTPD_OPTS="-N -p 1.gentoo.pool.ntp.org"

And start it:

`root `[`#`]`rc-service busybox-ntpd start`

Remove the hardware clock service hwclock from the boot runlevel and replace it with the software clock service swclock -

`root `[`#`]`rc-update del hwclock boot `

`root `[`#`]`rc-update add swclock boot `

Make sure you have the correct time zone set to the area which most closely matches your locale in [/usr/share/zoneinfo] -

`root `[`#`]`ls /usr/share/zoneinfo `

`root `[`#`]`echo "<YOUR_TIME_ZONE>" > /etc/timezone`

As an example, if you live in California, you would do -

`root `[`#`]`echo "America/Los_Angeles" > /etc/timezone`

Install your timezone libraries -

`root `[`#`]`emerge --ask sys-libs/timezone-data`

Start the NTP client and add it to the default runlevel -

`root `[`#`]`rc-service ntp-client start `

`root `[`#`]`rc-update add ntp-client default `

## [Troubleshooting]

### [No video output]

It may be an issue with the boot config. Useful if using an DVI to HDMI cable.

[FILE] **`/boot/config.txt`**

    #uncomment
    #hdmi_drive=2
    #dtoverlay=vc4-fkms-v3d

    #add
    hdmi_drive=1

### [Not booting]

USB Booting is not enabled by default, it will need to be enabled.

[FILE] **`/boot/config.txt`**

    program_usb_boot_mode=1

## [Where to get help]

On Internet Relay Chat

    #gentoo-arm (webchat)
    #gentoo-embedded (webchat)

On the [Gentoo Forums](https://forums.gentoo.org/), start a new topic in the Gentoo on ARM forum.

I don\'t mind a PM on the forums with a link to your post. I don\'t do one to one help via email or the forums PM system. You will either get no response at all or a request to make a public post. That way others may learn from your misfortune.

## [Acknowledgements]

Everyone contributing to the arm64 software base.

Especially Sakaki, who showed the way on the [final steps](https://forums.gentoo.org/viewtopic-t-1058530-highlight-.html).