**Resources**

[[]][Specifications](https://2018.compactpc.com.tw/download.aspx?file=ebox-335xdx3_series.pdf)

[[]][User Manual](https://www.wdlsystems.com/manuals/ICOP_Manuals/ebox-3350dx2_m.pdf)

[Vortex86](https://en.wikipedia.org/wiki/Vortex86) [SoC](https://en.wikipedia.org/wiki/System_on_a_chip) which uses the x86 CPU by DM&P Electronics.

** Note**\
While this article is mostly targetting at the EBOX-3350DX3, it will provide a starting point for all Vortex86 based systems. (Do note that the DX2 is closer to an i586.)

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Table]](#Table)
    -   [[1.2] [CPU]](#CPU)
        -   [[1.2.1] [/proc/cpuinfo]](#.2Fproc.2Fcpuinfo)
        -   [[1.2.2] [march=native]](#march.3Dnative)
-   [[2] [Install]](#Install)
    -   [[2.1] [Stage3]](#Stage3)
    -   [[2.2] [Chroot]](#Chroot)
    -   [[2.3] [make.conf]](#make.conf)
    -   [[2.4] [Binary Host]](#Binary_Host)
    -   [[2.5] [Kernel]](#Kernel)
        -   [[2.5.1] [sys-kernel/installkernel]](#sys-kernel.2Finstallkernel)
        -   [[2.5.2] [Dist-kernel]](#Dist-kernel)
    -   [[2.6] [Configuring the system]](#Configuring_the_system)
    -   [[2.7] [Bootloader]](#Bootloader)
        -   [[2.7.1] [GRUB]](#GRUB)
    -   [[2.8] [Finalizing]](#Finalizing)

## [Hardware]

### [Table]

  ---------------------------- ------------------------------------------------------------------- -------- ------------------------ ------------------ ---------------- -------
  Device                       Make/model                                                          Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  Vortex86DX3 (2) @ 1.00 GHz   N/A                                                                 Works    N/A                      N/A                N/A
  GPU                          RDC Semiconductor, Inc. RDC M2015 VGA-compatible graphics adapter   Works    N/A                      N/A                N/A
  Ethernet                     RDC R6040                                                           Works    N/A                      N/A                N/A
  IDE/SD Card Reader           RDC PATA                                                            Works    N/A                      N/A                N/A
  ---------------------------- ------------------------------------------------------------------- -------- ------------------------ ------------------ ---------------- -------

### [CPU]

#### [][/proc/cpuinfo]

`user `[`$`]`cat /proc/cpuinfo `

processor : 1

vendor_id : Vortex86 SoC

cpu family : 6

model : 1

model name : Vortex86DX3

stepping : 1

cpu MHz : 999.904

physical id : 1

siblings : 1

core id : 0

cpu cores : 1

apicid : 1

initial apicid : 1

fdiv_bug : no

f00f_bug : no

coma_bug : no

fpu : yes

fpu_exception : yes

cpuid level : 3

wp : yes

flags : fpu pse tsc msr cx8 apic sep pge cmov mmx fxsr sse cpuid

bugs : itlb_multihit

bogomips : 1999.77

clflush size : 32

cache_alignment : 32

address sizes : 32 bits physical, 32 bits virtual

power management:

#### [][march=native]

[FILE] **`/etc/portage/make.conf`make.conf (resolve-march-native)**

    COMMON_FLAGS="-march=pentiumpro -mtune=generic -mbranch-cost=3 -mfxsr -mmmx -mno-accumulate-outgoing-args -mno-sahf -msse"

## [Install]

The install process requires another computer running Gentoo to complete.

Insert the SD card into the host computer and mount it to [/mnt/gentoo]. In this example the article will use one partition with the xfs file system.

For help on creating the partition layout, please follow [Handbook:X86/Installation/Disks](https://wiki.gentoo.org/wiki/Handbook:X86/Installation/Disks "Handbook:X86/Installation/Disks")

`root `[`#`]`cd /mnt/gentoo`

### [Stage3]

Download one of the following stage3 files:

-   stage3-i486-openrc
-   stage3-i486-systemd
-   stage3-i686-hardened-openrc
-   stage3-i686-hardened-systemd
-   stage3-i686-openrc
-   stage3-i686-systemd
-   stage3-i686-musl

** Note**\
stage3-i686-openrc or stage3-i686-systemd are likely the best choices for the DX3 and up. Use the i486 stages for earlier models.

Untar the selected stage to [/mnt/gentoo]:

`root `[`#`]`tar xvf stage3-*.tar.xz`

### [Chroot]

Chroot into the stage3 using [Handbook:X86/Installation/Base#Chrooting](https://wiki.gentoo.org/wiki/Handbook:X86/Installation/Base#Chrooting "Handbook:X86/Installation/Base")

or using [[[sys-apps/arch-chroot]](https://packages.gentoo.org/packages/sys-apps/arch-chroot)[]]

`root `[`#`]`arch-chroot /mnt/gentoo`

### [make.conf]

[FILE] **`/etc/portage/make.conf`make.conf**

    COMMON_FLAGS="-O2 -fomit-frame-pointer -march=native"
    MAKEOPTS="-j2"

### [Binary Host]

While it is possible to use the official binary host, please note that only the packages in the stage3 are provided by Gentoo on x86.

See [Gentoo_Binary_Host_Quickstart](https://wiki.gentoo.org/wiki/Gentoo_Binary_Host_Quickstart "Gentoo Binary Host Quickstart") for information on setting this.

### [Kernel]

During the install process it is recommended to use Gentoo\'s [distribution kernel](https://wiki.gentoo.org/wiki/Project:Distribution_Kernel "Project:Distribution Kernel") for first boot. This is to provide a known working bootable system with support built in for any additional hardware the user may require. Once the user has confirmed the system is in a working state after first boot, then the user is free to use a kernel that they prefer.

#### [][sys-kernel/installkernel]

Setup [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]] for automatic INITRAMFS and GRUB generation.

[FILE] **`/etc/portage/package.use/installkernel`installkernel**

    sys-kernel/installkernel dracut grub

[[[sys-kernel/dracut]](https://packages.gentoo.org/packages/sys-kernel/dracut)[]] has a dependency on Rust which needs to be disabled to a lack of SSE2 support.

[FILE] **`/etc/portage/package.use/dracut`dracut**

    sys-kernel/dracut -dracut-cpio

#### [Dist-kernel]

`root `[`#`]`emerge --ask sys-kernel/gentoo-kernel-bin`

### [Configuring the system]

From the point follow the x86 Handbook from [Handbook:X86/Installation/System](https://wiki.gentoo.org/wiki/Handbook:X86/Installation/System "Handbook:X86/Installation/System") and return here at the bootloader stage.

### [Bootloader]

#### [GRUB]

Install to the SD card using:

`root `[`#`]`grub-install --target=i386-pc /dev/sda`

** Important**\
Use the device path for your SD card location and don\'t blindly copy.

Regenerate Grub\'s config:

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

### [Finalizing]

Once checking all config files its time to insert the SD card into the EBOX and power on for boot.

It might be wise to enable SSH at this point and create a local user to allow remote connections:

`root `[`#`]`rc-update sshd default`

If all goes well the system will now be booting into Gentoo.