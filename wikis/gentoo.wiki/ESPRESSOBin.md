[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Home](http://espressobin.net/)

[[]][Ebuild repository](https://github.com/gentoo/arm)

[[]][Link](https://github.com/sarnold/u-boot-ATF-manifest/tree/marvell-armada)

[[]][Link](https://github.com/sarnold/arm64-multiplatform)

[![caption](/images/thumb/d/df/Espressobin-with-ssd-1080.jpg/500px-Espressobin-with-ssd-1080.jpg)](https://wiki.gentoo.org/wiki/File:Espressobin-with-ssd-1080.jpg "caption")

## Contents

-   [[1] [Overview]](#Overview)
    -   [[1.1] [History]](#History)
    -   [[1.2] [What Works]](#What_Works)
    -   [[1.3] [Untested]](#Untested)
    -   [[1.4] [What\'s Required]](#What.27s_Required)
    -   [[1.5] [Update U-boot]](#Update_U-boot)
-   [[2] [Installation Overview]](#Installation_Overview)
    -   [[2.1] [Install Crossdev on the PC]](#Install_Crossdev_on_the_PC)
    -   [[2.2] [Build mainline u-boot (optional)]](#Build_mainline_u-boot_.28optional.29)
    -   [[2.3] [Use Crossdev to Build A Cross Compiler]](#Use_Crossdev_to_Build_A_Cross_Compiler)
-   [[3] [Fetch, Configure and Build the Kernel]](#Fetch.2C_Configure_and_Build_the_Kernel)
    -   [[3.1] [Fetch the Kernel]](#Fetch_the_Kernel)
    -   [[3.2] [Configure The Kernel]](#Configure_The_Kernel)
    -   [[3.3] [Cross Compiling The Kernel]](#Cross_Compiling_The_Kernel)
-   [[4] [Partition the microSD card]](#Partition_the_microSD_card)
    -   [[4.1] [Background]](#Background)
    -   [[4.2] [Partitioning]](#Partitioning)
        -   [[4.2.1] [Clean the card and format with options]](#Clean_the_card_and_format_with_options)
-   [[5] [Fetch the Gentoo bits of the install]](#Fetch_the_Gentoo_bits_of_the_install)
    -   [[5.1] [Install the arm64 Stage 3]](#Install_the_arm64_Stage_3)
    -   [[5.2] [Install a Portage Snapshot]](#Install_a_Portage_Snapshot)
-   [[6] [Populating /boot]](#Populating_.2Fboot)
    -   [[6.1] [Install the Kernel to the microSD Card]](#Install_the_Kernel_to_the_microSD_Card)
        -   [[6.1.1] [Install The Kernel Binary]](#Install_The_Kernel_Binary)
        -   [[6.1.2] [Install The Device Tree]](#Install_The_Device_Tree)
        -   [[6.1.3] [Create the Symlinks for Vendor U-Boot]](#Create_the_Symlinks_for_Vendor_U-Boot)
        -   [[6.1.4] [Install The Kernel Modules]](#Install_The_Kernel_Modules)
        -   [[6.1.5] [Checking The Kernel Install (vendor u-boot)]](#Checking_The_Kernel_Install_.28vendor_u-boot.29)
-   [[7] [Flashing and Configuring the Bootloader]](#Flashing_and_Configuring_the_Bootloader)
    -   [[7.1] [Obtaining the Firmware]](#Obtaining_the_Firmware)
    -   [[7.2] [Flashing the Firmware]](#Flashing_the_Firmware)
    -   [[7.3] [Post-flash Configuration]](#Post-flash_Configuration)
        -   [[7.3.1] [Vendor u-boot]](#Vendor_u-boot)
        -   [[7.3.2] [Mainline u-boot]](#Mainline_u-boot)
    -   [[7.4] [Create extlinux.conf]](#Create_extlinux.conf)
-   [[8] [Marvell ESPRESSOBin Peripherals]](#Marvell_ESPRESSOBin_Peripherals)
    -   [[8.1] [Serial Port Configuration]](#Serial_Port_Configuration)
    -   [[8.2] [Network Setup]](#Network_Setup)
    -   [[8.3] [Root Password]](#Root_Password)
    -   [[8.4] [/etc/fstab]](#.2Fetc.2Ffstab)
-   [[9] [Boot the Board to Test]](#Boot_the_Board_to_Test)
-   [[10] [What Next]](#What_Next)
    -   [[10.1] [Random Hints]](#Random_Hints)
        -   [[10.1.1] [Boot from SATA]](#Boot_from_SATA)
        -   [[10.1.2] [WiFi and Bluetooth]](#WiFi_and_Bluetooth)
        -   [[10.1.3] [CFLAGS]](#CFLAGS)
        -   [[10.1.4] [ACCEPT_KEYWORDS]](#ACCEPT_KEYWORDS)
        -   [[10.1.5] [MAKEOPTS]](#MAKEOPTS)
        -   [[10.1.6] [Networking]](#Networking)
        -   [[10.1.7] [sshd]](#sshd)
    -   [[10.2] [Updating The Tool Chain]](#Updating_The_Tool_Chain)
    -   [[10.3] [Useful Packages]](#Useful_Packages)
        -   [[10.3.1] [Network Time Sync]](#Network_Time_Sync)
-   [[11] [Where to Get Help]](#Where_to_Get_Help)
    -   [[11.1] [References]](#References)
-   [[12] [Acknowledgements]](#Acknowledgements)

## [Overview]

This documents the basic setup for Marvell Espressobin ARM64 network switch-ish board. It appears to be the only similar-class Marvell board with open docs (ie, not protected by NDA). Googling reveals a mix of both proprietary and \"open\" resources (and github appears to contain a mix of both, so ignore links and other references to \"extranet\"). There appears to be one main site for the ESPRESSOBin boards, with the corresponding vendor sources mainly on github.

### [History]

The Marvell Espressobin was originally a kickstarter board by Globalscale Technologies Inc. It is a high performance 64 bit dual-core networking computing platform based on the ARMv8 architecture and has low power consumption. The board is powered by Marvell\'s Armada 3700 dual-core SoC chipset which runs up to 1.2GHz.

At this point there are several variants of the Espressobin hardware, however, the newer device trees exist only in the Marvell and GTI github repos (and corresponding vendor kernel images). The actual hardware differences are mainly DDR size/speed and eMMC (whether it exists and how big). The board stencil should show which hardware version is present:

-   v5 espressobin: DDR3 with or without soldered eMMC
-   v7 espressobin: DDR4 with or without soldered eMMC
-   \"ultra\" espressobin: DDR4 with 8 GB eMMC

The above differences are reflected in the new device-tree names.

** Important**\
The mainline kernel has recently updated from the single espressobin device tree file to separate blobs for each variant. This change breaks the older/factory u-boot so a newer u-boot needs to be flashed to successfully load both new and legacy dt blobs.

Pros:

-   Solid mainline support
-   Great network/SATA performance
-   Mini PCIe expansion slot
-   2 GbE LAN ports, 1 GbE WAN port
-   USB 3 host port
-   ATF-based boot protocol
-   1 GB or 2 GB RAM

Cons:

-   no video/audio
-   ATF-based boot protocol
    -   somewhat complicated u-boot build process

The Gentoo arm64 offering is still experimental at the time of writing. That means that very little is marked stable. Expect to use ACCEPT_KEYWORDS=\"\~arm64\" and then use package.accept_keywords too.

### [What Works]

All the core hardware should be supported in latest mainline kernel (tested on 4.13.12) and u-boot 2017.11-rc4.

-   Network switch
-   USB 2.0/3
-   MMC
-   SATA
-   PCIE
-   UART over micro-USB
-   Hardware Crypto
-   SPI flash

### [Untested]

-   GPIO/SPI/I2C (on the connectors)
-   PCIe

### [][What\'s Required]

-   Gentoo Install on a PC
-   microSD card reader for the PC
-   ESPRESSOBin board
-   12V PSU
-   microSD card \> 8G
-   micro USB cable
-   network cable

The contents of the microSD card will be wiped during the install.

### [Update U-boot]

Starting with the 5.10.x mainline kernel, the U-boot/ATF firmware needs updating in order to load the newer device trees (required for eMMC and v7 hardware). The build process is reasonably well-documented on the espressobin wiki (see the Reference links at the bottom). Some of us are lazy (or just need to do other stuff) and have already tested the flash images from the espressobin wiki to make sure they load the new device trees (download said flash image blobs from the [espressobin tech-spec](http://espressobin.net/tech-spec/) page and flash either the debug or release blob for the board). Do not forget to setup the u-boot environment again after flashing. Also note this applies if using any of the newer vendor kernels (either Marvell or GTI).

## [Installation Overview]

-   Install crossdev on the PC
-   Build mainline u-boot (optional)
-   Fetch the mainline kernel (or use the builder script)
-   Partition the microSD card
-   Fetch the Gentoo bits of the install
-   Cross compile and install the kernel
-   Setup networking and root passwd
-   Boot with serial console to test

### [Install Crossdev on the PC]

crossdev is Gentoos\' tool for building cross compiler tool chains. Once it\'s installed, it will be used to build the arm64 kernel on the Gentoo PC.

`root `[`#`]`emerge --ask crossdev`

will install the crossdev tool.

### [][Build mainline u-boot (optional)]

U-boot has a rather complicated build and flash process, which is now documented in the repo manifest link below. The version of u-boot in SPI flash on the board I received is 2015.01-armada-17.02.0-g8128e91 and the default environment is set to boot from mmc. The 2017 updates seem to work fine, albeit with worse initial env config than factory.

As mentioned in the above note, building u-boot (either mainline or Marvell) is optional; that said, some extra \"features\" can be gained by building/flashing mainline u-boot instead of the Marvell fork. One useful feature in mainline that\'s already enabled are the distro defaults, which includes the extlinux/syslinux boot config file.

To build mainline u-boot/ATF for espressobin, either follow the manual steps in the two reference links below, or else follow the readme steps on the marvell-armada branch of [this repo manifest](https://github.com/sarnold/u-boot-ATF-manifest/tree/marvell-armada)

** Important**\
When choosing to build u-boot, there is a secondary cross toolchain that must

also be built along with the primary one below. For espressobin, this is a cortex-M3 baremetal

arm toolchain.

After building the aarch64 toolchain, the secondary toolchain can be built with a command something like this:

`root `[`#`]`USE="hardened multitarget lzma -multilib -openmp -go -fortran -jit -vtv" EXTRA_ECONF="--enable-newlib-nano-formatted-io --enable-newlib-nano-malloc --with-newlib --disable-multilib --disable-libsanitizer --with-arch=armv7e-m+fp --with-float-abi=hard --with-mode=thumb --with-abi=aapcs-linux --enable-libstdcxx-time=no" ELIBC="newlib" crossdev --ov-output /path/to/your/local-crossdev -t arm-none-eabi --ex-gdb`

** Important**\
Create your crossdev overlay first; see the following section.

### [Use Crossdev to Build A Cross Compiler]

`root `[`#`]`crossdev -t aarch64-unknown-linux-gnu`

Recommended crossdev setup:

-   do use the most current version, eg, at least sys-devel/crossdev-20201129
-   do setup your crossdev overlay first
-   optionally adjust USE and EXTRA_ECONF flags as needed

To setup an ebuild repository for crossdev to use, see the appropriate [section in the Crossdev article](https://wiki.gentoo.org/wiki/Crossdev#Crossdev_overlay "Crossdev"). Setup your overlay as shown, populate the config files, then use the *\--ov-output* option to set the path to your overlay.

The crossdev command expects at least the target tuple, with optional version specifiers for the toolchain components and more (see the help output and README file). The short command above will use the \"latest\" versions available and its own overlay detection (which you probably don\'t want) so use of the output-overlay argument is recommended, as shown in the following examples.

** Important**\
Do not use -S to build a stable toolchain, arm64 moves quickly

There are some crossdev examples in the arm overlay; an example \"fancy\" crossdev command for arm64 might be:

`root `[`#`]`USE="hardened multitarget lzma -multilib -openmp -go -fortran -jit" EXTRA_ECONF="--disable-multilib --disable-libsanitizer" crossdev --ov-output /path/to/your/local-crossdev -t aarch64-unknown-linux-gnu --ex-gdb`

** Important**\
Crossdev insists that many of the files in /etc/portage/ are directories

Convert files as crossdev asks e.g.

    error: please convert /etc/portage/package.env to a directory

by appending \_file to the existing filename

`root `[`#`]`mv /etc/portage/package.env /etc/portage/package.env_file`

making the directory

`root `[`#`]`mkdir /etc/portage/package.env`

then moving package.env_file into the directory.

`root `[`#`]`mv /etc/portage/package.env_file /etc/portage/package.env`

Rinse and repeat until crossdev is happy.

crossdev will take a while. It is building

    binutils:              binutils-[latest]
    gcc:                   gcc-[latest]
    headers:               linux-headers-[latest]
    libc:                  glibc-[latest]

When crossdev completes, the cross toolchain is ready:

`user `[`$`]`$ gcc-config -l `

    [1] aarch64-unknown-linux-gnu-9.2.0 *

It will also create an arm64 target root in [/usr/aarch64-unknown-linux-gnu/] This is used by cross emerge.

Pure cross compiling, other than the kernel, is out of scope of this guide.

## [][Fetch, Configure and Build the Kernel]

There are some prebuilt vendor kernel images for this board, but mainline is preferred.

### [Fetch the Kernel]

The kernel choices, either \"stock\" mainline or gentoo-sources, can be built by hand, or using the kernel build scripts with some Armbian patches (older kernels only). Note there are older ebuilds in the arm overlay that incorporate the appropriate gentoo patches, mvebu64 patches, as well as updated defconfigs available, see [https://github.com/sarnold/arm64-multiplatform](https://github.com/sarnold/arm64-multiplatform)

UPDATE: For the Gentoo way with no extra patches, use gentoo-sources 5.10.14-ish \*and\* the mainline u-boot flash-image.

So either use the builder scripts (borrowed from RCN repo and updated for ESPRESSOBin) or grab the defconfig and do it manually. The build scripts will clone linux-stable if not configured (see the file system.sh.sample and copy it to system.sh, then set your CC prefix kernel path).

`user `[`$`]`git clone https://github.com/sarnold/arm64-multiplatform `

`user `[`$`]`cd arm64-multiplatform`

For the latest, use the v5.10.x branch, edit system.sh, then run build_kernel.sh and wait for your shiny new kernel in the deploy/ directory.

At the end of the build, it will output the kernel version string to export for the install commands later. Something like:

    -----------------------------
    Script Complete
    eewiki.net: [user@localhost:~$ export kernel_version=4.13.12-aarch64-r0]
    -----------------------------

** Note**\
The build_kernel.sh script will start from a fresh clone of the kernel source, apply patches,

run make menuconfig, etc. To make changes or fiddle in the kernel tree, rebuild using the tools/rebuild.sh

script instead (the latter will start a build using the existing tree).

### [Configure The Kernel]

Once the scripts have cloned the kernel tree and applied any patches, it will wait at the menuconfig screen. Note the default config used should have all the required hardware support already enabled, but may not have all the network tools you want yet (the config is still a WIP).

More confident readers may be tempted to trim things out or add things now. A word of advice - **don\'t**, at least, not until the system boots.

### [Cross Compiling The Kernel]

The scripts will use the toolchain arch set in system.sh but if you want to compile it manually the proper command line would be something like:

`user `[`$`]`make ARCH=arm64 CROSS_COMPILE=aarch64-unknown-linux-gnu-`

## [Partition the microSD card]

** Warning**\
This Step Will Destroy ALL The Data on the Card

### [Background]

The current vendor u-boot environment is already set to look for a kernel and device tree blob in the boot directory of the first partition, as well as use the first partition as root. Therefore only one partition is required (or at least make sdX1 the rootfs).

** Warning**\
Many boards (even in mainline u-boot) do not yet support all ext4 defaults so 64bit metadata and checksums must be disabled

### [Partitioning]

Depending on how the microSD card is connected to you PC, it my be /dev/sdX or /dev/mmcblkY

** Warning**\
Check! Do Get It Right - Don\'t Ruin your PC Install

In the example below, it\'s /dev/sdb. On sdcards, using a swapfile instead of a separate partition is recommended.

#### [Clean the card and format with options]

`root `[`#`]`export DISK=/dev/your_sdcard_device `

`root `[`#`]`dd if=/dev/zero of=$ bs=1M count=10`

Using the partitioning tool of your choice, make one partition on your microSD card.

    root (/)

Using fdisk, and your microSD card block device, not the example /dev/sdb unless it\'s correct for your setup

`root `[`#`]`fdisk $ `

Use ext4 for root:

`root `[`#`]`mkfs.ext4 -L rootfs -O ^metadata_csum,^64bit -T news $1 `

** Important**\
-T news makes more inodes for lots of small files

The i-node count cannot be changed after filesystem creation and can limit the number of files on a files system. The Gentoo repository alone needs over 17,000 i-nodes.

## [Fetch the Gentoo bits of the install]

To make it easy to cross refer to the [Gentoo_Handbook](https://wiki.gentoo.org/wiki/Gentoo_Handbook "Gentoo Handbook")

`root `[`#`]`mkdir /mnt/gentoo`

Mount the microSD card root filesystem at /mnt/gentoo

`root `[`#`]`mount /dev/sdb1 /mnt/gentoo`

### [Install the arm64 Stage 3]

Following the [Gentoo_Handbook](https://wiki.gentoo.org/wiki/Gentoo_Handbook "Gentoo Handbook") fetch the [arm64 stage3](http://distfiles.gentoo.org/experimental/arm64/) and untar it to /mnt/gentoo in the normal way.

/mnt/gentoo/tmp should be empty. Clear it now.

`root `[`#`]`rm -rf /mnt/gentoo/tmp/*`

### [Install a Portage Snapshot]

*This step is not actually needed to boot but emerge won\'t work without it*

Following the [Gentoo Handbook](https://wiki.gentoo.org/wiki/Gentoo_Handbook "Gentoo Handbook"), fetch and unpack a [portage snapshot](http://distfiles.gentoo.org/snapshots/portage-latest.tar.bz2) in the normal way.

Careful readers can copy their host [/var/db/repos/gentoo].

## [][Populating /boot]

All that\'s needed here is the kernel binary and the proper device tree blob(s). If you have not flashed mainline u-boot, the file names have to match what the vendor u-boot expects, so just copy the files as-is and make symlinks to the required names (see below). For mainline u-boot simply use [make install] for the kernel/dtbs/modules or copy them however you wish.

### [Install the Kernel to the microSD Card]

The kernel was built above, now to install it.

The kernel is in three parts

1.  kernel binary
2.  device tree blob
3.  kernel modules

#### [Install The Kernel Binary]

As root or via sudo, copy the kernel binary from the build location, either from your kernel tree (/path/to/your/tree/linux/arch/arm64/boot/Image) or the deploy directory:

`user `[`$`]`sudo cp -v ./arm64-multiplatform/deploy/$.Image /mnt/gentoo/boot/`

#### [Install The Device Tree]

The device tree binary (.dtb) describes the hardware to the kernel. This avoids having all the existing hardware configurations hard coded into the kernel.

Extract the following .dtb file from ./arm64-multiplatform/deploy/\$-aarch64-r0-dtbs.tar.gz and copy it to the boot directory:

`user `[`$`]`sudo cp -v ./arm64-multiplatform/deploy/armada-3720-espressobin.dtb /mnt/gentoo/boot/`

#### [Create the Symlinks for Vendor U-Boot]

Change to the mounted boot directory and symlink the files to the expected names:

`user `[`$`]`cd /mnt/gentoo/boot `

`user `[`$`]`sudo ln -snf $.Image Image `

`user `[`$`]`sudo ln -snf armada-3720-espressobin.dtb armada-3720-community.dtb `

`user `[`$`]`cd -`

#### [Install The Kernel Modules]

For a hand-built/installed kernel, don\'t foget to run make with the modules_install arg. From the top of the kernel tree, install the kernel modules

`user `[`$`]`cd /path/to/your/tree/linux `

`user `[`$`]`ARCH=arm64 CROSS_COMPILE=aarch64-unknown-linux-gnu- sudo make modules_install INSTALL_MOD_PATH=/mnt/gentoo`

Otherwise, unpack the kernel modules tarball from the deploy directory:

`user `[`$`]`sudo tar xfv ./arm64-multiplatform/deploy/$-modules.tar.gz -C /mnt/gentoo/`

#### [][Checking The Kernel Install (vendor u-boot)]

`user `[`$`]`ls /mnt/gentoo/boot`

    4.13.12-aarch64-r0.Image   armada-3720-espressobin.dtb  Image
    armada-3720-community.dtb  config-4.13.12-aarch64-r0

`user `[`$`]`ls /mnt/gentoo/lib/modules`

    4.13.12-aarch64-r0

Shows that the kernel and modules were installed to the correct locations.

## [Flashing and Configuring the Bootloader]

You really should update the bootloader firmware, especially if you still have a 2015 version in SPI flash. That said, there is some risk involved, so make sure you have solid power/serial connections. And don\'t panic\... There are documented recovery methods if somehow your cat eats the power cord at just the wrong time.

### [Obtaining the Firmware]

The available choices are:

-   [Download](http://espressobin.net/tech-spec/) the espressobin flash images
-   [Build](http://wiki.espressobin.net/tiki-index.php?page=Build+From+Source+-+Bootloader) Marvell/GTI u-boot/ATF
-   [Build](https://github.com/sarnold/u-boot-ATF-manifest/tree/marvell-armada) mainline u-boot/ATF

Note the main differences between the above two build options are 1) mainline u-boot, and 2) master branches for the dependencies (as recommended in the ATF docs).

### [Flashing the Firmware]

Once you have a shiny new flash image, use either tftp or a USB stick/sdcard to flash it. See the [bootloader update](http://wiki.espressobin.net/tiki-index.php?page=Update+the+Bootloader) page on the espressobin wiki and choose a method.

** Important**\
Be sure to use the correct flash image for your board; read the wiki pages and the build manifest readme file for more info.

When the flash process is complete, you must complete the following steps for either vendor or mainline u-boot in order to get things booting again. The vendor upgrade images do not restore mmc or sata boot configs, and mainline u-boot has a minor bug in the default distro boot environment.

When the bubt command completes, reset the board, and then stop the autoboot process to get a u-boot prompt again. Run the following command and then hit a key to stop the boot:

`Marvell>>``reset `

    resetting ...

When back at the u-boot prompt, load the default environment and print it.

`=>``env default -a `

    ## Resetting to default environment

`=>``printenv `

The output from the printenv command will depend on the choice of u-boots; see the Boot from SATA section below for the vendor output.

### [Post-flash Configuration]

A correct u-boot environment is required; choose one of the following.

#### [Vendor u-boot]

If not using mainline u-boot, the correct values must be defined for mmcroot, etc, and then saved using [saveenv].

For vendor u-boot, compare the output of *printenv* with the vendor environment variables in the Boot from SATA section, then restore any missing ones or define what you need for root partitions, etc. There is not really any set standard, just make sure the result fulfills the basic reqs, ie the result should be able to execute the following to boot from the sdcard device:

    setenv console console=ttyMV0,115200 earlycon=ar3700_uart,0xd0012000
    setenv bootargs $console root=/dev/mmcblk0p1 rw rootwait net.ifnames=0 biosdevname=0
    mmc dev 0
    ext4load mmc 0:1 $kernel_addr $image_name
    ext4load mmc 0:1 $fdt_addr $fdt_name
    booti $kernel_addr - $fdt_addr

** Important**\
Be sure to use the existing address vars, do not invent your own.

For the initrd case, add one more *ext4load* command to the above; then replace the \"-\" with \$ramdisk_addr_r in the last line. After defining the name of the initrd file, the initrd load command should look something like this:

    ext4load mmc 0:1 $ramdisk_addr_r $initrd_name

#### [Mainline u-boot]

And now for something completely different\... mainline u-boot. After flashing mainline u-boot, the *printenv* output should look like the following:

`=>``printenv `

    boot_a_script=load $ $:$ $ $$; source $
    boot_efi_binary=load $ $:$ $ efi/boot/bootaa64.efi; if fdt addr $; then bootefi $ $;else bootefi $ $;fi
    boot_efi_bootmgr=if fdt addr $; then bootefi bootmgr $;else bootefi bootmgr;fi
    boot_extlinux=sysboot $ $:$ any $ $$
    boot_net_usb_start=usb start
    boot_pci_enum=pci enum
    boot_prefixes=/ /boot/
    boot_script_dhcp=boot.scr.uimg
    boot_scripts=boot.scr.uimg boot.scr
    boot_syslinux_conf=extlinux/extlinux.conf
    boot_targets=mmc1 mmc0 usb0 scsi0 pxe dhcp
    bootcmd=run distro_bootcmd
    bootcmd_dhcp=setenv devtype dhcp; run boot_net_usb_start; run boot_pci_enum; if dhcp $ $; then source $; fi;setenv efi_fdtfile $; setenv efi_old_vci $;setenv efi_old_arch $;setenv bootp_vci PXEClient:Arch:00011:UNDI:003000;setenv bootp_arch 0xb;if dhcp $; then tftpboot $ dtb/$;if fdt addr $; then bootefi $ $; else bootefi $ $;fi;fi;setenv bootp_vci $;setenv bootp_arch $;setenv efi_fdtfile;setenv efi_old_arch;setenv efi_old_vci;
    bootcmd_mmc0=devnum=0; run mmc_boot
    bootcmd_mmc1=devnum=1; run mmc_boot
    bootcmd_pxe=run boot_net_usb_start; run boot_pci_enum; dhcp; if pxe get; then pxe boot; fi
    bootcmd_scsi0=devnum=0; run scsi_boot
    bootcmd_usb0=devnum=0; run usb_boot
    distro_bootcmd=scsi_need_init=; setenv nvme_need_init; for target in $; do run bootcmd_$; done
    efi_dtb_prefixes=/ /dtb/ /dtb/current/
    eth1addr=00:51:82:11:22:01
    eth2addr=00:51:82:11:22:02
    eth3addr=00:51:82:11:22:03
    ethaddr=F0:AD:4E:06:7B:9D
    fdt_addr=0x6f00000
    fdt_addr_r=0x6f00000
    kernel_addr=0x7000000
    kernel_addr_r=0x7000000
    load_efi_dtb=load $ $:$ $ $$
    mmc_boot=if mmc dev $; then devtype=mmc; run scan_dev_for_boot_part; fi
    nvme_boot=run boot_pci_enum; run nvme_init; if nvme dev $; then devtype=nvme; run scan_dev_for_boot_part; fi
    nvme_init=if $; then setenv nvme_need_init false; nvme scan; fi
    pxefile_addr_r=0x6e00000
    ramdisk_addr_r=0xa000000
    scan_dev_for_boot=echo Scanning $ $:$...; for prefix in $; do run scan_dev_for_extlinux; run scan_dev_for_scripts; done;run scan_dev_for_efi;
    scan_dev_for_boot_part=part list $ $ -bootable devplist; env exists devplist || setenv devplist 1; for distro_bootpart in $; do if fstype $ $:$ bootfstype; then run scan_dev_for_boot; fi; done; setenv devplist
    scan_dev_for_efi=setenv efi_fdtfile $; for prefix in $; do if test -e $ $:$ $$; then run load_efi_dtb; fi;done;run boot_efi_bootmgr;if test -e $ $:$ efi/boot/bootaa64.efi; then echo Found EFI removable media binary efi/boot/bootaa64.efi; run boot_efi_binary; echo EFI LOAD FAILED: continuing...; fi; setenv efi_fdtfile
    scan_dev_for_extlinux=if test -e $ $:$ $$; then echo Found $$; run boot_extlinux; echo SCRIPT FAILED: continuing...; fi
    scan_dev_for_scripts=for script in $; do if test -e $ $:$ $$; then echo Found U-Boot script $$; run boot_a_script; echo SCRIPT FAILED: continuing...; fi; done
    scsi_boot=run scsi_init; if scsi dev $; then devtype=scsi; run scan_dev_for_boot_part; fi
    scsi_init=if $; then scsi_need_init=false; scsi scan; fi
    soc=mvebu
    usb_boot=usb start; if usb dev $; then devtype=usb; run scan_dev_for_boot_part; fi
    vendor=Marvell

    Environment size: 4113/65532 bytes

If the **scriptaddr** variable is not defined in the above output, then it will need to be set and saved manually. Note this variable *is* defined correctly in the header file, but somehow gets dropped from the default env (and is one of the **required** distro vars).

Run the following two commands to correct the default env:

`=>``setenv scriptaddr 0x6d00000 `

`=>``saveenv `

    Saving Environment to SPIFlash... SF: Detected w25q32dw with page size 256 Bytes, erase size 4 KiB, total 4 MiB
    Erasing SPI flash...Writing to SPI flash...done
    OK

### [Create extlinux.conf]

The basic requirement for the *distro_bootcmd* to run is the extlinux.conf file; a basic example would look something like the following:

[FILE] **`extlinux.conf`**

    LABEL Gentoo arm64 espressobin
            KERNEL ../vmlinuz-5.10.14-aarch64-x0
            APPEND console=ttyMV0,115200 earlycon=ar3700_uart,0xd0012000 root=/dev/mmcblk0p1 rw rootfstype=ext4 rootwait net.ifnames=0 biosdevname=0
            FDT ../dtbs/5.10.14-aarch64-x0/marvell/armada-3720-espressobin.dtb

Create a file similar to the above under `/boot/extlinux`. Be sure to use tabs for indenting:

`user `[`$`]`cd /mnt/gentoo/boot `

`user `[`$`]`sudo mkdir extlinux `

`user `[`$`]`sudo nano extlinux/extlinux.conf `

`user `[`$`]`cd -`

## [Marvell ESPRESSOBin Peripherals]

Now that the base operating system is in place, you will need to do some file configuration by hand to get the peripherals working.

### [Serial Port Configuration]

The Gentoo Stage3 comes with the default Gentoo serial port configuration, however, you need to make sure the default serial ports are commented out, and set the board-specific serial port.

Open up [/etc/inittab] -

`root `[`#`]` nano -w /etc/inittab`

Make sure the ttyS serial port lines are commented, then find this line at the bottom and set the speed and tty port device -

[FILE] **`/etc/inittab`**

    T0:12345:respawn:/sbin/agetty 115200 ttyMV0 vt100

Save and exit the file. This ensures Gentoo will launch a login getty on the correct serial interface.

### [Network Setup]

It seems like all network switch setups are unique, but there is an effort to converge using the Distributed Switch Architecture (DSA). The ESPRESSOBin has two LAN ports and one WAN port, which apparently need a virtual \"eth0\" to be configured correctly. This means eth0 must be \"up\" (but not configured) before the actual network devices are usable. Unless you make udev naming rules, the default interfaces are lan0, lan1, and wan. Upstream docs name the left-most port as \"lan1\" which is where you want to plug in for local use.

`user `[`$`]`ifconfig -a`

    bond0: flags=5122<BROADCAST,MASTER,MULTICAST>  mtu 1500
            ether a6:e9:9a:6c:17:e1  txqueuelen 1000  (Ethernet)
            RX packets 0  bytes 0 (0.0 B)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 0  bytes 0 (0.0 B)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

    dummy0: flags=130<BROADCAST,NOARP>  mtu 1500
            ether d6:73:f5:c7:65:2c  txqueuelen 1000  (Ethernet)
            RX packets 0  bytes 0 (0.0 B)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 0  bytes 0 (0.0 B)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

    eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
            inet6 fe80::f2ad:4eff:fe03:861b  prefixlen 64  scopeid 0x20<link>
            ether f0:ad:4e:03:86:1b  txqueuelen 532  (Ethernet)
            RX packets 203950  bytes 145809090 (139.0 MiB)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 145454  bytes 42938767 (40.9 MiB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
            device interrupt 8

    lan0: flags=4098<BROADCAST,MULTICAST>  mtu 1500
            ether f0:ad:4e:03:86:1b  txqueuelen 1000  (Ethernet)
            RX packets 0  bytes 0 (0.0 B)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 0  bytes 0 (0.0 B)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

    lan1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
            inet 192.168.10.29  netmask 255.255.255.0  broadcast 192.168.10.255
            inet6 fe80::f2ad:4eff:fe03:861b  prefixlen 64  scopeid 0x20<link>
            ether f0:ad:4e:03:86:1b  txqueuelen 1000  (Ethernet)
            RX packets 203950  bytes 141322190 (134.7 MiB)
            RX errors 0  dropped 15488  overruns 0  frame 0
            TX packets 145480  bytes 41953390 (40.0 MiB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

    lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
            inet 127.0.0.1  netmask 255.0.0.0
            inet6 ::1  prefixlen 128  scopeid 0x10<host>
            loop  txqueuelen 1000  (Local Loopback)
            RX packets 41  bytes 2720 (2.6 KiB)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 41  bytes 2720 (2.6 KiB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

    wan: flags=4098<BROADCAST,MULTICAST>  mtu 1500
            ether f0:ad:4e:03:86:1b  txqueuelen 1000  (Ethernet)
            RX packets 0  bytes 0 (0.0 B)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 0  bytes 0 (0.0 B)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

The corresponding Gentoo network config needs all of these enabled, however, only lan1 is needed for initial setup. Here is the initial config for one network interface:

[FILE] **`/etc/conf.d/net`**

    # This blank configuration will automatically use DHCP for any net.*
    # scripts in /etc/init.d.  To create a more complete configuration,
    # please review /usr/share/doc/openrc*/net.example* and save your configuration
    # in /etc/conf.d/net (this file :]!).

    dns_domain_lo="your.domain"

    config_eth0=null

    config_lan1="192.168.10.29 netmask 255.255.255.0 brd 192.168.10.255"
    routes_lan1="default via 192.168.10.1"

    dns_domain_lan1="your.domain"
    dns_servers_lan1="8.8.8.8"

    rc_net_lan1_need="net.eth0"

    # The network scripts are now part of net-misc/netifrc
    # In order to avoid sys-apps/openrc-0.12 from removing
    # this file, this comment was
    # added; you can safely remove this comment.  Please see
    # /usr/share/doc/netifrc*/README* for more information.

** Important**\
Remember to start both eth0 and lan1.

### [Root Password]

** Important**\
You need this to be able to log in at all

There are several ways to generate a password hash for /etc/shadow; usually it suffices to copy the hash from another system.

All stage3 root filesystems should use an /etc/shadow root entry

    root:x::0:99999:7:::

Instead of copying the hash, you can also use openssl to generate a fresh one:

-   edit [/mnt/gentoo/etc/shadow] so root can login:

    :::: cmd-box


    `root `[`#`]`openssl passwd -1`


    ::::

grab hash output, edit [/mnt/gentoo/etc/shadow], and put here:

[FILE] **`/mnt/gentoo/etc/shadow`**

    root:<hash_output>:10770:0:::::

The password can always be changed once you are logged in.

### [][/etc/fstab]

On this board, the microSD card will be [/dev/mmcblk0] with one partition, [/dev/mmcblk0p1]

Edit /mnt/gentoo/etc/fstab to match.

`root `[`#`]`nano -w /mnt/gentoo/etc/fstab`

[FILE] **`/mnt/gentoo/etc/fstab`**

    /swapfile               none            swap            sw              0 0
    /dev/mmcblk0p1          /               ext4            noatime         0 1

## [Boot the Board to Test]

Unmount the microSD card.

`root `[`#`]`umount /mnt/gentoo/`

When the prompt returns, move the microSD card to the board, plug in micro-usb and power cables and open a console using your favorite tool, then plug in the AC side and power it up.

Log in at the serial console as root. Nothing was added to any runlevels during the install, so networking was not started, nor anything that depends on networking, like ntpd and sshd.

Many embedded boards do not have a hardware real time clock. The time will probably be Jan 1, 1970; note you can use busybox-ntpd to set the clock after the network is up.

## [What Next]

As always with Gentoo, if it booted, that\'s the hard bit done.

1.  All The setup steps in the Gentoo Handbook
2.  Fix the MAC address or use a static IP
3.  Allow root logins via ssh
4.  Add a crond, a logger and other things the handbook does before the reboot.
5.  Add Kernel Sources (or at least the .config)

### [Random Hints]

#### [Boot from SATA]

** Important**\
The following applies to the Marvell vendor u-boot only. See above for flashing and configuring mainline u-boot.

Yes, it\'s actually fairly easy to boot directly from an SSD connected to the SATA controller without using the micro-SDCard at all. For this to work, setup the SSD the same way as the card (hint: you can just rsync everything on the card to your SSD). Then make the u-boot changes shown below.

The default u-boot environment has several variables set for NFS and MMC card, but the key one is \"bootcmd\" which defaults to the card slot (note it may point \"root\" to the first or second partition depending on the vendor configuration. Googling will bring up the vendor page with how to boot a bricked device from SATA and restore the u-boot in SPI flash; ignore that (unless your board is really bricked).

So, switching jumpers simply to boot from the SATA device is not needed, just two modified u-boot environment variables will do it. To make this change, just pop out the SDCard and connect a serial console as above, then power it up and hit a key to stop autoboot to get a u-boot prompt.

    Booting Trusted Firmware
    BL1: v1.2(release):armada-17.02.0:
    BL1: Built : 09:41:56, Jun  2 2NOTICE:  BL2: v1.2(release):armada-17.02.0:
    NOTICE:  BL2: Built : 09:41:57, Jun  2 20NOTICE:  BL31: v1.2(release):armada-17.02.0:
    NOTICE:  BL31:

    U-Boot 2015.01-armada-17.02.0-g8128e91 (Jun 02 2017 - 09:41:51)

    I2C:   ready
    DRAM:  1 GiB
    Board: DB-88F3720-ESPRESSOBin
           CPU    @ 1000 [MHz]
           L2     @ 800 [MHz]
           TClock @ 200 [MHz]
           DDR    @ 800 [MHz]
    Comphy-0: PEX0          2.5 Gbps
    Comphy-1: USB3          5 Gbps
    Comphy-2: SATA0         5 Gbps
    Now running in RAM - U-Boot at: 3ff2b000
    U-Boot DT blob at : 000000003fa18168
    MMC:   XENON-SDHCI: 0
    SF: Detected W25Q32DW with page size 256 Bytes, erase size 4 KiB, total 4 MiB
    PCIE-0: Link down
    SCSI:  Target spinup took 0 ms.
    AHCI 0001.0300 32 slots 1 ports 6 Gbps 0x1 impl SATA mode
    flags: ncq led only pmp fbss pio slum part sxs
    Net:   neta0
    Hit any key to stop autoboot:  3  0
    Marvell>>

Once you see the prompt above you can try some commands like \"printenv\" and \"help\". For example:

`Marvell>>``printenv `

    baudrate=115200
    bootargs=console=ttyMV0,115200 earlycon=ar3700_uart,0xd0012000 root=/dev/mmcblk0p2 rw ip=0.0.0.0:0.0.0.0:10.4.50.254:255.255.255.0:marvell:eth0:none nfsroot=0.0.0.0:/srv/nfs/
    bootcmd=mmc dev 0; ext4load mmc 0:1 $kernel_addr $image_name;ext4load mmc 0:1 $fdt_addr $fdt_name;setenv bootargs $console root=/dev/mmcblk0p1 rw rootwait net.ifnames=0 biosdevname=0; booti $kernel_addr - $fdt_addr
    bootdelay=3
    console=console=ttyMV0,115200 earlycon=ar3700_uart,0xd0012000
    eth1addr=00:00:00:00:51:82
    eth2addr=00:00:00:00:51:83
    ethact=neta0
    ethaddr=F0:AD:4E:03:86:1B
    ethprime=egiga0
    fdt_addr=0x1000000
    fdt_high=0xffffffffffffffff
    fdt_name=boot/armada-3720-community.dtb
    gatewayip=10.4.50.254
    get_images=mmc dev 0; fatload mmc 0 $kernel_addr $image_name; fatload mmc 0 $fdt_addr $fdt_name; run get_ramfs
    get_ramfs=if test "$" != "-"; then setenv ramfs_addr 0x3000000; tftp $ramfs_addr $ramfs_name; else setenv ramfs_addr -;fi
    hostname=marvell
    image_name=boot/Image
    initrd_addr=0xa00000
    initrd_size=0x2000000
    ipaddr=0.0.0.0
    kernel_addr=0x2000000
    loadaddr=0x2000000
    loads_echo=0
    netdev=eth0
    netmask=255.255.255.0
    ramfs_addr=-
    ramfs_name=-
    root=root=/dev/mmcblk0p2 rw
    rootpath=/srv/nfs/
    serverip=0.0.0.0
    set_bootargs=setenv bootargs $console $root ip=$ipaddr:$serverip:$gatewayip:$netmask:$hostname:$netdev:none nfsroot=$serverip:$rootpath $extra_params
    stderr=serial
    stdin=serial
    stdout=serial

    Environment size: 1480/65532 bytes

The variables we need to modify to switch defaults from SDCard partition 1 to SATA partition 1 are \"bootargs\" and \"bootcmd\". To change them, we need to run \"setenv FOO\" for each one, but that will only change them temporarily (suitable for testing). To save the changes to flash, we\'ll need to run the saveenv\" command once we\'re happy with the changes.

** Warning**\
The following changes work for me, but as always, YMMV. Test them first, save them after you verify they work for you.

Change the required variables:

`Marvell>>``setenv bootargs "$console root=/dev/sda1 rw rootwait net.ifnames=0 biosdevname=0" `

`Marvell>>``setenv bootcmd "scsi scan; scsi dev 0; ext4load scsi 0 $kernel_addr $image_name; ext4load scsi 0:1 $fdt_addr $fdt_name; booti $kernel_addr - $fdt_addr" `

Test the changes

`Marvell>>``run bootcmd `

    Setting SCSI to 0
    Target spinup took 0 ms.
    AHCI 0001.0300 32 slots 1 ports 6 Gbps 0x1 impl SATA mode
    flags: ncq led only pmp fbss pio slum part sxs
    scanning bus 0 for devices...
      Device 0: (0:0) Vendor: ATA Prod.: C400-MTFDDAK128M Rev: 040H
                Type: Hard Disk
                Capacity: 122104.3 MB = 119.2 GB (250069680 x 512)
    Invalid port number 2
    Invalid port number 3
    Invalid port number 4
    Invalid port number 5
    Invalid port number 6
    Invalid port number 7
    Found 1 device(s).

    SCSI device 0:
        Device 0: (0:0) Vendor: ATA Prod.: C400-MTFDDAK128M Rev: 040H
                Type: Hard Disk
                Capacity: 122104.3 MB = 119.2 GB (250069680 x 512)
    ... is now current device
    14895616 bytes read in 709 ms (20 MiB/s)
    7466 bytes read in 50 ms (145.5 KiB/s)
    ## Flattened Device Tree blob at 01000000
       Booting using the fdt blob at 0x1000000
       Using Device Tree in place at 0000000001000000, end 0000000001004d29

    Starting kernel ...

\
If it works, great! If not, check the console output for errors, look for typos, etc. Once you\'ve verified the changes do what you want, save them:

`Marvell>>``saveenv `

#### [WiFi and Bluetooth]

Options are mainly PCIe or USB, so take your pick and report back.

#### [CFLAGS]

This works quite well, except for the packages where it doesn\'t work\...

[FILE] **`make.conf`**

    LINK_OPTS="-flto=2"
    VEC_OPTS="-ftree-vectorize -ftree-loop-distribution -fvect-cost-model=cheap"
    BASE_TUNE_OPTS="-march=armv8-a -mcpu=cortex-a53+simd"
    TUNE_OPTS="-march=armv8-a+crc+fp+simd -mabi=lp64 -mcpu=cortex-a53+crc+fp+simd"

    #CFLAGS="$ -O2 -pipe"
    CFLAGS="$ -O2 -pipe $ $"
    CXXFLAGS="$"
    LDFLAGS="$ -fuse-linker-plugin"

    CPU_FLAGS_ARM="edsp neon thumb vfp vfpv3 vfpv4 vfp-d32 aes sha1 sha2 crc32 v4 v5 v6 v7 v8 thumb2"

Note gcc-6.x allows the use of -march=native but that will prevent the use of distcc. The above is the same as gcc-6.3 would set for -march=native anyway.

#### [ACCEPT_KEYWORDS]

Outside of the \@system set, arm64 is either testing or keyword masked. Set

[FILE] **`make.conf`**

    ACCEPT_KEYWORDS="~arm64"

and expect to use package.accept_keywords too.

** Warning**\
The stage 3 tarball has been built with gcc-4.9 was gcc-5.4 is in testing \...

Upgrade gcc then rebuild all of the installed C++ software.

** Important**\
News item 2015-10-22 GCC 5 Defaults to the New C++11 ABI

#### [MAKEOPTS]

With only 1G RAM, and two cores, the conventional

[FILE] **`make.conf`**

    MAKEOPTS="-j3"

could be a bit aggressive for building larger things. It will force swapping or even appear to lock up completely, to the point where it won\'t even respond to the console. Unlike many other boards that may segfault under heavy load, this board will try to swap everything out (and hasn\'t locked up yet).

Use files in [/etc/portage/env/] and entries in [/etc/portage/package.env] to set MAKEOPTS on a per package basis.

#### [Networking]

The basic config given above works fine for \"typical\" building and testing; if you want to make a firewall/gateway/router, that\'s beyond the scope of this HowTo.

#### [sshd]

The default configuration for sshd will not allow password based root logins.

    add your ssh public key for root
    make a normal user in the wheel group
    edit /etc/ssh/sshd_config to allow password based root logins

** Important**\

### [Updating The Tool Chain]

Once you boot, you may have the desire to update \@world first thing. However, as of the time of this writing, the latest stage3 for arm64 was built in December 2016. A lot of things in the tool chain will be out of date with what is on the current Portage tree. Once you\'ve booted the board and confirmed that you have an internet connection, you\'ll want to first run emerge \--sync to get the absolute latest tree, then run perl-cleaner \--all to get all of your Perl packages up to date.

`root `[`#`]` emerge --sync `

`root `[`#`]` perl-cleaner --all `

`root `[`#`]` emerge -auDN @world`

### [Useful Packages]

#### [Network Time Sync]

This board does not have a hardware real time clock on board. There are vendors online where you can order RTC modules made for the standard interfaces, but if you don\'t plan to run one, I highly recommend installing a NTP client.

First, set the initial time using the \'date\' command. Date and time will be entered in mmddhhmmyyyy format and the time is in 24-hr format -

`root `[`#`]`date mmddhhmmyyyy`

As an example, if the time is 10:05PM on 7/31/2017 -

`root `[`#`]` date 073122052017`

As with most things Gentoo, the NTP daemon is just an emerge away -

`root `[`#`]`emerge --ask net-misc/ntp`

Remove the hardware clock service hwclock from the boot runlevel and replace it with the software clock service swclock -

`root `[`#`]` rc-update del hwclock boot `

`root `[`#`]` rc-update add swclock boot`

Make sure you have the correct time zone set to the area which most closely matches your locale in /usr/share/zoneinfo -

`root `[`#`]` ls /usr/share/zoneinfo `

`root `[`#`]` echo "<YOUR_TIME_ZONE>" > /etc/timezone`

As an example, if you live in California, you would do -

`root `[`#`]` echo "America/Los_Angeles" > /etc/timezone`

Install your timezone libraries -

`root `[`#`]`emerge --ask sys-libs/timezone-data`

Start the NTP client and add it to the default runlevel -

`root `[`#`]` rc-service ntp-client start `

`root `[`#`]` rc-update add ntp-client default`

## [Where to Get Help]

On Internet Relay Chat [[#gentoo-arm](ircs://irc.libera.chat/#gentoo-arm)] ([[webchat](https://web.libera.chat/#gentoo-arm)]) [[#gentoo-embedded](ircs://irc.libera.chat/#gentoo-embedded)] ([[webchat](https://web.libera.chat/#gentoo-embedded)])

On the [Gentoo Forums](https://forums.gentoo.org/), start a new topic in the Gentoo on ARM forum.

### [References]

-   [http://espressobin.net/tech-spec/](http://espressobin.net/tech-spec/)
-   [http://wiki.espressobin.net/tiki-index.php?page=Update+the+Bootloader](http://wiki.espressobin.net/tiki-index.php?page=Update+the+Bootloader)
-   [http://wiki.espressobin.net/tiki-index.php?page=Bootloader+recovery+via+UART](http://wiki.espressobin.net/tiki-index.php?page=Bootloader+recovery+via+UART)
-   [https://github.com/globalscaletechnologies](https://github.com/globalscaletechnologies)
-   [https://trustedfirmware-a.readthedocs.io/en/latest/plat/marvell/armada/build.html](https://trustedfirmware-a.readthedocs.io/en/latest/plat/marvell/armada/build.html)
-   [https://marcin.juszkiewicz.com.pl/2021/02/15/ebbr-on-espressobin/](https://marcin.juszkiewicz.com.pl/2021/02/15/ebbr-on-espressobin/)

## [Acknowledgements]

Everyone contributing to the arm64 software base.

Especially everyone\...