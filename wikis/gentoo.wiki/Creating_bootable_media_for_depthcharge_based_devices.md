[Depthcharge](https://chromium.googlesource.com/chromiumos/platform/depthcharge), the ChromeOS bootloader^[\[1\]](#cite_note-1)^, is one of the available [payloads](https://doc.coreboot.org/payloads.html) for [coreboot](https://coreboot.org) (and also [Libreboot](https://libreboot.org)) and as such mostly found on Chromebooks. This guide shows how to create bootable media, e.g. an installation media USB drive, for those devices.

** Note**\
So far these instructions have only been tested with the ARMv7-A based target device [ASUS Chromebook C201](https://wiki.gentoo.org/wiki/ASUS_Chromebook_C201 "ASUS Chromebook C201").

## Contents

-   [[1] [Installing required tools]](#Installing_required_tools)
-   [[2] [Preparing the partitions]](#Preparing_the_partitions)
-   [[3] [Install a Gentoo rootfs]](#Install_a_Gentoo_rootfs)
-   [[4] [Creating a cross-compiler]](#Creating_a_cross-compiler)
-   [[5] [Configuring the Linux kernel]](#Configuring_the_Linux_kernel)
-   [[6] [Finalizing]](#Finalizing)
-   [[7] [External resources]](#External_resources)
-   [[8] [References]](#References)

## [Installing required tools]

The guide assumes that the current platform is a Gentoo Linux one. The majority of steps however can be performed from any distribution, just translate the Gentoo-specific way of doing things (such as installing software) to the other distribution\'s practices.

** Note**\
Throughout this guide this current platform will be referred to as the *host system* whereas the device that shall be booted will be referred to as the *target device*.

Install [[[dev-embedded/u-boot-tools]](https://packages.gentoo.org/packages/dev-embedded/u-boot-tools)[]], [[[sys-apps/dtc]](https://packages.gentoo.org/packages/sys-apps/dtc)[]], [[[sys-block/parted]](https://packages.gentoo.org/packages/sys-block/parted)[]] and [[[sys-boot/vboot-utils]](https://packages.gentoo.org/packages/sys-boot/vboot-utils)[]]:

`root `[`#`]`emerge --ask dev-embedded/u-boot-tools sys-apps/dtc sys-block/parted sys-boot/vboot-utils`

Some drivers might also require proprietary firmware available from [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]].

## [Preparing the partitions]

This is the recommended partition layout and size:

  ------------ ------------------------------------------------------------ -----------------
  /dev/sd\*1   kernel partition (similar to a traditional boot partition)   64MiB
  /dev/sd\*2   root partition                                               available space
  ------------ ------------------------------------------------------------ -----------------

** Important**\
The term \"sd\*\" in the following commands needs to be replaced with the term currently corresponding to the bootable media -- in case of an SD Card, it will be something like \"mmcblkX\". In any case the \"\*\" represents a letter and the \"X\" represents a number.

** Warning**\
This will delete all data on [/dev/sd\*]

`root `[`#`]`parted /dev/sd* mklabel gpt `

`root `[`#`]`parted -a optimal /dev/sd* unit mib mkpart Kernel 1 65 `

`root `[`#`]`parted -a optimal /dev/sd* unit mib mkpart Root 65 100% `

Depthcharge requires some specific parameters to be set. These signal the bootloader the presence of a valid kernel partition:

`root `[`#`]`cgpt add -i 1 -t kernel -S 1 -T 5 -P 15 /dev/sd* `

Create a filesystem on the root partition and mount it:

`root `[`#`]`mkfs.ext4 /dev/sd*2 `

`root `[`#`]`mount /dev/sd*2 /mnt `

## [Install a Gentoo rootfs]

** Note**\
At this point consider alternatively using an [armv7a_hardfp-musl] stage3 from the [Hardened musl](https://wiki.gentoo.org/wiki/Project:Hardened_musl#Goals "Project:Hardened musl") project.

Get a stage3 tarball from the main website\'s [download section](https://www.gentoo.org/downloads/#other-arches) that is suitable for the architecture (e.g. [ARMv7a\|HardFP]) of the target device and extract it to the bootable media\'s root filesystem:

`root `[`#`]`tar xvpf /PATH/TO/STAGE3-TARBALL -C /mnt/ `

Switch the bootable media's Gentoo to unstable to ensure the availability of the latest version of [[[sys-boot/vboot-utils]](https://packages.gentoo.org/packages/sys-boot/vboot-utils)[]] and speed up the bootable media. Replace [TARGETARCH] with the target device\'s architecture, e.g. [arm] for ARMv7-A based devices.

`root `[`#`]`echo "ACCEPT_KEYWORDS=\"~TARGETARCH\"" >> /mnt/etc/portage/make.conf `

`root `[`#`]`echo "MAKEOPTS=\"-j4\"" >> /mnt/etc/portage/make.conf `

Set the bootable media's root password to "gentoo", cf. [Setting a default root password](https://wiki.gentoo.org/wiki/Setting_a_default_root_password "Setting a default root password"):

`root `[`#`]`sed -i 's/root\:\*/root\:\$6\$I9Q9AyTL\$Z76H7wD8mT9JAyrp\/vaYyFwyA5wRVN0tze8pvM\.MqScC7BBm2PU7pLL0h5nSxueqUpYAlZTox4Ag2Dp5vchjJ0/' /mnt/etc/shadow `

Finish this step by unmounting the bootable media's root filesystem:

`root `[`#`]`umount /mnt `

## [Creating a cross-compiler]

** Important**\
This section can be skipped if the host system\'s architecture is the same as the target system\'s. These steps are only necessary if the host system is **not** based on the same architecture as the target device.

** Note**\
The instructions for setting up a cross-compilation toolchain are very specific to Gentoo, i.e. if the host system runs a different Linux distribution the respective distribution's documentation on cross-compilation should be consulted instead.

Create an ebuild repository for the cross toolchain by following the [section in the Crossdev article](https://wiki.gentoo.org/wiki/Crossdev#Crossdev_overlay "Crossdev").

Then install [[[sys-devel/crossdev]](https://packages.gentoo.org/packages/sys-devel/crossdev)[]] and create the cross toolchain. Replace [TUPLE] with the [system tuple](https://wiki.gentoo.org/wiki/Embedded_Handbook/Tuples "Embedded Handbook/Tuples") fitting the target architecture, e.g. [arm-linux-gnueabihf] for ARMv7-A based target devices with at least VFPv3-D16^[\[2\]](#cite_note-2)^ (also commonly referred to as hardfloat, HardFP or hf).

`root `[`#`]`emerge --ask sys-devel/crossdev `

`root `[`#`]`crossdev --stable --target TUPLE `

Finally prepare cross-compiling the kernel. Replace [TARGETARCH] with the target device\'s architecture, e.g. [arm] for ARMv7-A based devices and replace [TUPLE] again with the system tuple fitting the target architecture, e.g. [arm-linux-gnueabihf]. Mind the trailing \"[-]\".

`user `[`$`]`export ARCH=TARGETARCH `

`user `[`$`]`export CROSS_COMPILE=TUPLE- `

## [Configuring the Linux kernel]

If all necessary drivers are built into the kernel (i.e. no loadable modules are needed to boot the target device) there\'s no need to have an initramfs, which keeps things simple. Especially if the host system\'s architecture differs from the target device\'s architecture creating an initramfs would at least involve cross-compiling busybox. With that in mind configure [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]] as usual, cf. [Configuring the Linux kernel](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Kernel "Handbook:AMD64/Installation/Kernel").

Build the kernel and device tree binaries:

`user `[`$`]`make zImage dtbs `

From the kernel build directory, copy the zImage and the target device\'s device tree binary to the desired working directory. Replace [DTBINARY] with the filename of the target device\'s device tree binary, e.g. [rk3288-veyron-speedy.dtb] for the Asus Chromebook C201 (which is based on Rockchip\'s RK3288 SoC and a board with the codename \"Veyron Speedy\").

`user `[`$`]`cp -a arch/arm/boot/zImage /PATH/TO/ARBITRARY_WORKING_DIRECTORY `

`user `[`$`]`cp -a arch/arm/boot/dts/DTBINARY /PATH/TO/ARBITRARY_WORKING_DIRECTORY `

Change to the desired working directory:

`user `[`$`]`cd /PATH/TO/ARBITRARY_WORKING_DIRECTORY `

\
Create the configuration file ([gentoo.its]) for the FIT image with the following content. Again replace [DTBINARY] with the filename of the target device\'s device tree binary, e.g. [rk3288-veyron-speedy.dtb] for the Asus Chromebook C201.

[FILE] **`gentoo.its`**

    /dts-v1/;

    / ;
            };
            fdt@1;
            };
        };
        configurations ;
        };
    };

Pack the FIT image:

`user `[`$`]`sync `

`user `[`$`]`mkimage -f gentoo.its gentoo.itb `

Create a file ([kernel.flags]) that contains the CMDLINE parameters.

** Important**\
The term \"sd\*\" in the following file needs to be replaced with the term corresponding to the bootable media **in future**, i.e. when booting on the target system. This depends on the target device, but \"sda\" or \"sdb\" respectively \"mmcblk0p\" or \"mmcblk1p\" are good guesses.

[FILE] **`kernel.flags`**

    console=tty1 root=/dev/sd*2 rootfstype=ext4 rootwait rw

Sign and pack the kernel:

`user `[`$`]`sync `

`user `[`$`]`futility --debug vbutil_kernel --arch arm --version 1 --keyblock /usr/share/vboot/devkeys/kernel.keyblock --signprivate /usr/share/vboot/devkeys/kernel_data_key.vbprivk --bootloader kernel.flags --config kernel.flags --vmlinuz gentoo.itb --pack vmlinuz.signed `

Install the kernel to the kernel partition.

** Important**\
The term \"sd\*\" in the following command needs to be replaced with the term **currently** corresponding to the bootable media -- in case of a SD Card something like \"mmcblkXp\". In any case the \"\*\" represents a letter and the \"X\" represents a number.

`root `[`#`]`dd vmlinuz.signed of=/dev/sd*1 `

## [Finalizing]

Now boot the target device from the created media, log in and [configure the network](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Networking "Handbook:AMD64/Installation/Networking"). Once the network connection is working prepare Portage:

`root `[`#`]`emerge-webrsync `

Finally install required tools, [[[dev-embedded/u-boot-tools]](https://packages.gentoo.org/packages/dev-embedded/u-boot-tools)[]], [[[sys-apps/dtc]](https://packages.gentoo.org/packages/sys-apps/dtc)[]], [[[sys-block/parted]](https://packages.gentoo.org/packages/sys-block/parted)[]] and [[[sys-boot/vboot-utils]](https://packages.gentoo.org/packages/sys-boot/vboot-utils)[]]:

`root `[`#`]`emerge --ask dev-embedded/u-boot-tools sys-apps/dtc sys-block/parted sys-boot/vboot-utils`

** Note**\
If the created bootable media is to be used on a day-to-day base, i.e. as a regular system, it is highly recommended to read the [Gentoo Handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64 "Handbook:AMD64") and work through the steps not covered by this guide.

## [External resources]

-   PDF: Additional information on depthcharge: Google, [Depthcharge - The ChromeOS bootloader (PDF)](https://www.chromium.org/chromium-os/2014-firmware-summit/ChromeOS%20firmware%20summit%20-%20Depthcharge.pdf), ChromeOS firmware summit, 2014. Retrieved on June 21st, 2019

## [References]

1.  [[[↑](#cite_ref-1)] [[Depthcharge](https://www.chromium.org/chromium-os/developer-information-for-chrome-os-devices/custom-firmware#TOC-Depthcharge), [Developer Information for Chrome OS Devices](https://www.chromium.org/chromium-os/developer-information-for-chrome-os-devices). Retrieved on June 21st, 2019]]
2.  [[[↑](#cite_ref-2)] [[ARM architecture - Floating-point (VFP)](https://en.wikipedia.org/wiki/ARM_architecture#Floating-point_(VFP)), [Wikipedia](https://wikipedia.org). Retrieved February 26th, 2019]]