[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Home](https://mangopi.org/mqpro)

[[]][[#gentoo-riscv](ircs://irc.libera.chat/#gentoo-riscv)] ([[webchat](https://web.libera.chat/#gentoo-riscv)])

[[]][mangopi-sbc/MQ-Pro](https://github.com/mangopi-sbc/MQ-Pro)

This page describes several methods for building a RISC-V Gentoo image for the Mango Pi MQ-Pro or similar devices.

## Contents

-   [[1] [Introduction]](#Introduction)
    -   [[1.1] [Hardware]](#Hardware)
-   [[2] [Useful Notes]](#Useful_Notes)
    -   [[2.1] [Musl]](#Musl)
    -   [[2.2] [Serial Output]](#Serial_Output)
    -   [[2.3] [Faster Installations]](#Faster_Installations)
    -   [[2.4] [make.conf]](#make.conf)
        -   [[2.4.1] [RISC-V ISA Standard and Extensions]](#RISC-V_ISA_Standard_and_Extensions)
    -   [[2.5] [Official Sources]](#Official_Sources)
-   [[3] [Prerequisites]](#Prerequisites)
    -   [[3.1] [Configure QEMU-user and binfmt]](#Configure_QEMU-user_and_binfmt)
    -   [[3.2] [Generate a cross-toolchain using Crossdev]](#Generate_a_cross-toolchain_using_Crossdev)
-   [[4] [Firmware]](#Firmware)
    -   [[4.1] [OpenSBI]](#OpenSBI)
    -   [[4.2] [U-Boot]](#U-Boot)
-   [[5] [Linux Kernel]](#Linux_Kernel)
-   [[6] [Root Filesystem]](#Root_Filesystem)
    -   [[6.1] [Build a seed tarball]](#Build_a_seed_tarball)
        -   [[6.1.1] [Set the system profile]](#Set_the_system_profile)
    -   [[6.2] [Catalyst]](#Catalyst)
    -   [[6.3] [Customise the RootFS]](#Customise_the_RootFS)
    -   [[6.4] [Bootloader Configuration]](#Bootloader_Configuration)
-   [[7] [Imaging the Device]](#Imaging_the_Device)
    -   [[7.1] [Boot Process]](#Boot_Process)
        -   [[7.1.1] [Storage Layout]](#Storage_Layout)
    -   [[7.2] [Partition Table]](#Partition_Table)
    -   [[7.3] [Write the SPL and U-Boot]](#Write_the_SPL_and_U-Boot)
    -   [[7.4] [Format and Mount the Boot and Root Partitions]](#Format_and_Mount_the_Boot_and_Root_Partitions)
    -   [[7.5] [Burn the image to an SD card]](#Burn_the_image_to_an_SD_card)
-   [[8] [Boot the D1]](#Boot_the_D1)
-   [[9] [See also]](#See_also)
-   [[10] [External resources]](#External_resources)

## [Introduction]

This page aims to provide an easy-to-follow introduction to installing Gentoo onto Embedded hardware using the MQ-Pro as an example device.

The majority of the instructions here are not specific to the MQ-Pro and may be applied to other devices with similar hardware based on the Allwinner D1 SoC, or more broadly to both RISC-V and ARM devices.

Please apply some common sense when adapting these instructions for other devices and do **not** blindly copy and paste commands without understanding what they do.

It should also be noted that the processes described hereafter are not always the most efficient in terms of commands used, and multiple commands may be used with, for example, environment variables that would typically be exported, or repeated additional options where a wrapper would be useful. This is intentional as it is intended to be a learning experience for the reader.

This article is intended to supplement the [Embedded Handbook](https://wiki.gentoo.org/wiki/Embedded_Handbook "Embedded Handbook").

### [Hardware]

The [Mango Pi MQ Pro] is a (tiny) RISC-V Single Board Computer (SBC) based on the Allwinner D1-H SoC with a single-core XuanTie C906 RISC-V CPU running at 1.0 GHz. It comes in variants of 512 MB/1 GB of DDR3 memory and uses the [rv64gcv] subarch.

This SBC supports TF/SD, eMMC, and USB storage devices, and has a Raspberry Pi Zero-compatible 40-pin GPIO header. It comes equipped with a Realtek [rtl8723ds] 2.4GHz 802.11 bgn + bluetooth 4.2 module. An unpopulated space exists on the PCB for a NOR or NAND flash memory chip; there are no known examples of this being populated from the factory however the SoC does support loading firmware from this location.

## [Useful Notes]

Some useful notes that may be of interest to the reader can be found below.

### [Musl]

This example uses a musl Libc. It is possible to use a glibc, however as this is a \'standard\' Gentoo configuration it is not elaborated on here.

The TL;DR is:

-   use the tuple `riscv64-unknown-linux-musl` instead of `riscv64-unknown-gnu` wherever crossdev is in use.
-   Obtain (or build) any lp64d non-musl stage3 tarball and use that instead of the musl stage3 tarball.
-   Select an appropriate non-musl profile.

### [Serial Output]

Currently only serial output has been achieved on a MangoPI MQ and no HDMI output. Using a serial adapter to test boot and login are required. Also something to note with serial. When you go to plug in the device with USB you must have the serial lines unplugged. For some reason the device will not boot if they are connected when USB power is applied. You can however power the device via the GPIO pins labeled for 5v power via the serial cable if your using one that includes power lines.

### [Faster Installations]

Anywhere that QEMU-user is invoked to build a cross-arch package, using portage within a chroot may be replaced with an external installation utilising [crossdev](https://wiki.gentoo.org/wiki/Crossdev "Crossdev") to cross-compile binaries and portage to install them into the image as follows:

`root `[`#`]`riscv64-unknown-linux-musl-emerge --ask sys-kernel/dracut `

`root `[`#`]`cd rootfs `

`root `[`#`]`ROOT=$PWD/ riscv64-unknown-linux-musl-emerge --ask --usepkgonly --oneshot sys-kernel/dracut`

It will be faster to cross-compile packages and install them into the image than to use QEMU-user to build them within the chroot, though this is not the preferred approach.

### [make.conf]

Some useful additions for cross-compiling packages and identifying breakage in failed package builds:

[FILE] **`/etc/portage/make.conf`**

    # Colour in portage output, useful for debugging
    # Needed for ninja (e.g. z3)
    CLICOLOR_FORCE=1
    # https://gitlab.kitware.com/cmake/cmake/-/merge_requests/6747
    # https://github.com/ninja-build/ninja/issues/174
    CMAKE_COMPILER_COLOR_DIAGNOSTICS=ON
    CMAKE_COLOR_DIAGNOSTICS=ON

    # Common flags for cross-compiling and colour;
    COMMON_FLAGS="-mabi=lp64d -march=rv64gcv_zicsr_zba_zbb -O2 -pipe -fdiagnostics-color=always -frecord-gcc-switches"

    # Enable QA messages for from iwdevtools
    PORTAGE_ELOG_CLASSES="$ qa"

#### [RISC-V ISA Standard and Extensions]

When identifying the RISC-V ISA standard and extensions for the target device, the following table may be useful:

  ----------- ---------------------------------------------------------------- -- -- --
  Name        Description
  RV32I       Base Integer Instruction Set - 32-bit
  RV32E       Base Integer Instruction Set (embedded) - 32-bit, 16 registers
  RV64I       Base Integer Instruction Set - 64-bit
  RV128I      Base Integer Instruction Set - 128-bit
  Extension
  M           Standard Extension for Integer Multiplication and Division
  A           Standard Extension for Atomic Instructions
  F           Standard Extension for Single-Precision Floating-Point
  D           Standard Extension for Double-Precision Floating-Point
  G           Shorthand for the base and above extensions
  Q           Standard Extension for Quad-Precision Floating-Point
  L           Standard Extension for Decimal Floating-Point
  C           Standard Extension for Compressed Instructions
  B           Standard Extension for Bit Manipulation
  J           Standard Extension for Dynamically Translated Languages
  T           Standard Extension for Transactional Memory
  P           Standard Extension for Packed-SIMD Instructions
  V           Standard Extension for Vector Operations
  N           Standard Extension for User-Level Interrupts
  H           Standard Extension for Hypervisor
  S           Standard Extension for Supervisor-level Instructions
  ----------- ---------------------------------------------------------------- -- -- --

RISC-V defines the order that must be used to define the ISA subset:

      RV [32, 64, 128] I, M, A, F, D, G, Q, L, C, B, J, T, P, V, N

For example, `RV32IMAFDQC` is legal, whereas `RV32IMAFDCQ` is not

In the case of the MQ-Pro, the following identifiers are both valid: `rv64imafdcv`, `rv64gcv`

There are some additional extensions to take into account:

-   `zicsr` (Control and Status Register \[CSR\] Instructions); implied by the F extension
-   Bitmanip extensions `Zba` (address generation) and `Zbb` (Basic bit manipulation)

This results in the following being the descriptive and shorthand flags for the MQ-Pro: `rv64imafdcv_zicsr_zba_zbb`, `rv64gcv_zba_zbb`

### [Official Sources]

The official Board Support Package/SDK for this board can be gathered using [[[dev-vcs/git-repo]](https://packages.gentoo.org/packages/dev-vcs/git-repo)[]] (AKA Google Repo); Thanks to linux-sunxi for mirroring the SDK outside of the AllWinner registrationwall.

`user `[`$`]`repo init -u `[`https://github.com/linux-sunxi/d1-sdk-manifest.git`](https://github.com/linux-sunxi/d1-sdk-manifest.git)` -b master -m tina-d1-open.xml `

`user `[`$`]`repo sync `

    Fetching: 100% (16/16), done in 19m35.328s
    Updating files: 100% (751/751), done.
    Updating files: 100% (67929/67929), done.
    Updating files: 100% (14843/14843), done.
    Updating files: 100% (6682/6682), done.
    Checking out: 100% (16/16), done in 20.887s
    repo sync has finished successfully.

It is recommended that this not be used; the packages contained within are hopelessly outdated and many of the fixes have been upstreamed. [crossdev] should be used to generate a cross-compiler toolchain.

With that said, the official sources provide a good starting point when trying to understand a new board.

## [Prerequisites]

When working with (and particularly while debugging) embedded hardware a UART interface that may be attached to the device is essential. Consult the [documentation](https://mangopi.org/_media/mq-prov14-sch.pdf) for the device to determine UART interface pinout. The MQ-Pro has a UART interface on the 40-pin GPIO header and its the same pinout as the raspberry pi systems, pins 8 and 10 on the header and is required to make this little guy work ATM as HDMI output is not working!

In addition to the general compilers that come with gentoo you will also need to install swig as its used to build UBOOT.

`root `[`#`]`emerge --ask dev-lang/swig `

### [Configure QEMU-user and binfmt]

When working with embedded systems it is often desirable to chroot into the image that is to be deployed to the target device. QEMU-user may be used to chroot into a rootfs for a different architecture than the host system. This is particularly useful for installing packages and configuring the system before deploying it to the target device.

Configure and install QEMU; make a binpkg to install into the chroot:

`root `[`#`]`echo 'QEMU_SOFTMMU_TARGETS="riscv64 x86_64"' >> /etc/portage/make.conf `

`root `[`#`]`echo 'QEMU_USER_TARGETS="riscv64"' >> /etc/portage/make.conf `

`root `[`#`]`echo app-emulation/qemu static-user >> /etc/portage/package.use/qemu `

`root `[`#`]`echo ':riscv64:M::\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\xf3\x00:\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xff\xff:/usr/bin/qemu-riscv64:' > /proc/sys/fs/binfmt_misc/register `

`root `[`#`]`echo ':riscv64:M::\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\xf3\x00:\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xff\xff:/usr/bin/qemu-riscv64:' > /etc/binfmt.d/qemu-riscv64-static.conf `

`root `[`#`]`systemctl restart systemd-binfmt `

`root `[`#`]`emerge --ask app-emulation/qemu`

`root `[`#`]`gpasswd -a larry kvm `

`root `[`#`]`quickpkg app-emulation/qemu `

### [Generate a cross-toolchain using Crossdev]

[crossdev](https://wiki.gentoo.org/wiki/Crossdev "Crossdev") should be used to to build an up-to-date cross-compiler from the Gentoo repository. This will then be used to build firmware binaries, the kernel, and any software that is to be installed into the image.

Install [[[sys-devel/crossdev]](https://packages.gentoo.org/packages/sys-devel/crossdev)[]] and generate a RISC-V cross toolchain (see [Cross Build Environment](https://wiki.gentoo.org/wiki/Cross_build_environment "Cross build environment") for further information)

`root `[`#`]`emerge --ask sys-devel/crossdev`

[Create an ebuild repository](https://wiki.gentoo.org/wiki/Creating_an_ebuild_repository "Creating an ebuild repository") for crossdev, preventing it from choosing a (seemingly) random repository to store its packages:

`root `[`#`]`mkdir -p /var/db/repos/crossdev/ `

`root `[`#`]`echo 'crossdev' > /var/db/repos/crossdev/profiles/repo_name `

`root `[`#`]`echo 'masters = gentoo' > /var/db/repos/crossdev/metadata/layout.conf `

`root `[`#`]`chown -R portage:portage /var/db/repos/crossdev `

If the Gentoo ebuild repository is synchronized using Git, or any other method with Manifest files that do not include checksums for ebuilds:

[FILE] **`/var/db/repos/crossdev/metadata/layout.conf`**

    masters = gentoo
    thin-manifests = true

Instruct Portage and crossdev to use this ebuild repository:

[FILE] **`/etc/portage/repos.conf/crossdev.conf`**

    [crossdev]
    location = /var/db/repos/crossdev
    priority = 10
    masters = gentoo
    auto-sync = no

`root `[`#`]`crossdev --target riscv64-unknown-linux-gnu`

The crossdev-built cross-toolchain will be installed to [/usr/riscv64-unknown-linux-musl]. The cross-compiler may be used by prefixing the target to the command, e.g.

`user `[`$`]`riscv64-unknown-linux-musl-gcc`

## [Firmware]

The firmware used to boot any D1-based boards consists of three parts, broadly comparable to those used in [aarch64] SoCs. These are:

-   U-Boot Secondary Program Loader (SPL), responsible for initializing DRAM and loading further firmware from storage
-   OpenSBI, which runs in machine mode and provides a standard \"SBI\" interface to less privileged modes.
-   U-Boot which initialises additional hardware and boots a binary.

### [OpenSBI]

OpenSBI has supported the D1 SoC and the C906 CPU since version 1.1.

A slimmed-down version of OpenSBI may be produced; only the following drivers are required:

-   `FDT_IRQCHIP_PLIC`
-   `FDT_RESET_SUNXI_WDT`
-   `FDT_SERIAL_UART8250`

Check out, configure, and build OpenSBI:

`user `[`$`]`git clone `[`https://github.com/riscv-software-src/opensbi`](https://github.com/riscv-software-src/opensbi)` `

`user `[`$`]`pushd opensbi `

`user `[`$`]`CROSS_COMPILE=riscv64-unknown-linux-musl- PLATFORM=generic make menuconfig `

`user `[`$`]`CROSS_COMPILE=riscv64-unknown-linux-musl- PLATFORM=generic FW_PIC=y make `

`user `[`$`]`popd `

### [U-Boot]

As of May 2023, Mainline U-Boot does not support the D1 SoC. A community patchset is being developed to add support for the D1 SoC and the C906 CPU which may be used instead.

While there is some additional work to be done before this fork can be upstreamed, it is already capable of booting Linux from an SD card, USB, or the network.

The U-Boot Secondary Program Loader is capable of loading U-Boot from storage media using several different \"modes\". The RAW mode and RAW partition mode have the U-Boot binary written loaded from a block device at a configurable location, or from a partition with a configurable GUID Type Code. It may also be configured to load a `.itb` file from a supported filesystem type.

The U-Boot SPL may be built with any combination of boot modes, however this will increase the size of the resulting binary.

** Tip**\
One of the potential outputs of this process is the file [u-boot-sunxi-with-spl.bin]. This file consists of both the SPL and U-Boot binary packaged together as a single image (SPL + U-Boot). The D1 SoC is able to read these binaries and boot from them; it may be preferable to simply load this image for simplicity.

** Note**\
The reasons for this will be discussed in greater detail later, however if RAW mode is to be used, a GPT filesystem is desired, and the SPL + U-Boot image is not, it is recommended that `CONFIG_SYS_MMCSD_RAW_MODE_U_BOOT_SECTOR` be set to `1024`(KB)

[KERNEL] **SPL boot flow configuration options**

    -> Enable SPL (SPL [=y])
      -> SPL configuration options
        [*] MMC raw mode: by sector
        (0x1024) Address on the MMC to load U-Boot from
        (0x10) U-Boot main hardware partition image offset
        [*] MMC Raw mode: by partition
        (1)   Partition to use to load U-Boot from (NEW)
        [*]   MMC raw mode: by partition type
        (BC13C2FF-59E6-4262-A352-B275FD6F7172) Partition Type on the MMC to load U-Boot from (NEW)
        [*] Support CPU drivers
        [*] Support FAT filesystems
        (u-boot.itb) File to load for U-Boot from the filesystem (NEW)

UBOOT uses pylibfdt and there is currently an issue with the setup.py script that errors out when being processed. You will need to apply the below patch to the script before you compile UBOOT. You can either make a patch from the below diff file or just manually edit setup.py.

[FILE] **`setup.py`pylibfdt Patch**

    diff --git a/scripts/dtc/pylibfdt/setup.py b/scripts/dtc/pylibfdt/setup.py
    index 8baae08770ca..c6fe5a6a446f 100755
    --- a/scripts/dtc/pylibfdt/setup.py
    +++ b/scripts/dtc/pylibfdt/setup.py
    @@ -37,7 +37,7 @@
         long_description = fh.read()

     # Decodes a Makefile assignment line into key and value (and plus for +=)
    -RE_KEY_VALUE = re.compile('(?P<key>\w+) *(?P[+])?= *(?P<value>.*)$')
    +RE_KEY_VALUE = re.compile(r'(?P<key>\w+) *(?P[+])?= *(?P<value>.*)$')

     def get_top_builddir():
         if '--top-builddir' in sys.argv:

Check out, configure, and build U-Boot according to the desired boot flow:

NOTE: You may want to append \--depth=1 to speed up the git clone. This will omit some of the commit data but you don\'t need that for building.

`user `[`$`]`git clone `[`https://github.com/smaeul/u-boot`](https://github.com/smaeul/u-boot)` -b d1-wip `

`user `[`$`]`pushd u-boot `

`user `[`$`]`CROSS_COMPILE=riscv64-unknown-linux-musl- make mangopi_mq_pro_defconfig `

`user `[`$`]`CROSS_COMPILE=riscv64-unknown-linux-musl- make menuconfig `

`user `[`$`]`CROSS_COMPILE=riscv64-unknown-linux-musl- OPENSBI=../opensbi/build/platform/generic/firmware/fw_dynamic.bin make -j$(nproc) `

`user `[`$`]`popd `

## [Linux Kernel]

The Allwinner D1 Linux BSP Kernel is [Available on GitHub](https://github.com/Tina-Linux/tina-d1x-linux-5.4). This kernel is based on Linux 5.4 and its use is not recommended.

A community-maintained fork of the mainline kernel is [available](https://github.com/smaeul/linux/commits/d1/all) which which supports most of the hardware peripherals (Audio, Ethernet, MMC, SPI NAND, USB, RGB LCD, HDMI, MIPI DSI). As of the writing of this article it is based on the 6.1.0 series.

** Important**\
When booting a kernel on this device use the devicetree provided in RAM by the platform firmware (for U-Boot, this means `$fdtcontroladdr`). Do *not* load a DTB from storage.

Check out and build the kernel:

NOTE: You may want to append \--depth=1 to speed up any git clone operations. This will omit some of the commit data but you don\'t need that for building.

`user `[`$`]`git clone `[`https://github.com/smaeul/linux`](https://github.com/smaeul/linux)` -b d1/all `

`user `[`$`]`pushd linux `

`user `[`$`]`ARCH=riscv make defconfig `

`user `[`$`]`ARCH=riscv make menuconfig `

`user `[`$`]`ARCH=riscv CROSS_COMPILE=riscv64-unknown-linux-musl- make -j$(nproc) vmlinux all modules `

`user `[`$`]`popd `

Skipping ahead a bit, once a rootfs is available, install the kernel modules to the rootfs:

`root `[`#`]`ARCH=riscv INSTALL_MOD_PATH=../rootfs make modules_install`

## [Root Filesystem]

There are several methods that may be used to create or obtain a Gentoo root filesystem for the D1 SoC. The simplest method is simply downloading and unpacking a stage3 tarball from [https://www.gentoo.org/downloads/](https://www.gentoo.org/downloads/), if a suitable one is available:

`user `[`$`]`aria2c -x16 -s16 `[`https://bouncer.gentoo.org/fetch/root/all/releases/riscv/autobuilds/20230428T170354Z/stage3-rv64_lp64d_musl-20230428T170354Z.tar.xz`](https://bouncer.gentoo.org/fetch/root/all/releases/riscv/autobuilds/20230428T170354Z/stage3-rv64_lp64d_musl-20230428T170354Z.tar.xz)

`root `[`#`]`mkdir rootfs`

`root `[`#`]`tar xpvf stage3-*.tar.xz --xattrs-include='*.*' --numeric-owner -C rootfs`

This example will assume that this has not been selected and instead [Catalyst will be used](https://wiki.gentoo.org/wiki/Catalyst_Musl_Stages_Creation "Catalyst Musl Stages Creation") to generate an appropriate stage3 tarball from scratch. If using an upstream stage3 tarball is desired, skip ahead to customising the rootfs.

It is possible directly use the [crossdev] root under [/usr] to build a rootfs; it is broadly similar to using Catalyst however instead of generating a seed tarball the rootfs is built by chrooting directly into the crossdev root. There are some advantages to this approach, particularly that it is possible to save a significant amount of time.

While this may be faster for quick development or building for a single device, if intending to target multiple devices it is usually better to use Catalyst as a generic stage 1 image may be created and used as the base for multiple stage 3 images. Using Catalyst also provides better isolation between the host and target systems.

### [Build a seed tarball]

To create a stage3 tarball, Calalyst requires a [seed tarball]. Catalyst will chroot into the seed and emerge packages for the new stage to ensure that packages generated for stage tarballs are isolated from the host system.

This example will build a seed tarball from scratch; an appropriate stage3 tarball from upstream may be placed in [/var/tmp/catalyst/builds/default] and used instead.

#### [Set the system profile]

`root `[`#`]`PORTAGE_CONFIGROOT=/usr/riscv64-unknown-linux-musl eselect profile list `

    Available profile symlink targets:
      [1]   default/linux/riscv/20.0/rv64gc/lp64d (stable)
      [2]   default/linux/riscv/20.0/rv64gc/lp64d/desktop (dev)
      [3]   default/linux/riscv/20.0/rv64gc/lp64d/desktop/gnome (dev)
      [4]   default/linux/riscv/20.0/rv64gc/lp64d/desktop/gnome/systemd (dev)
      [5]   default/linux/riscv/20.0/rv64gc/lp64d/desktop/gnome/systemd/merged-usr (dev)
      [6]   default/linux/riscv/20.0/rv64gc/lp64d/desktop/plasma (dev)
      [7]   default/linux/riscv/20.0/rv64gc/lp64d/desktop/plasma/systemd (dev)
      [8]   default/linux/riscv/20.0/rv64gc/lp64d/desktop/plasma/systemd/merged-usr (dev)
      [9]   default/linux/riscv/20.0/rv64gc/lp64d/desktop/systemd (dev)
      [10]  default/linux/riscv/20.0/rv64gc/lp64d/desktop/systemd/merged-usr (dev)
      [11]  default/linux/riscv/20.0/rv64gc/lp64d/systemd (stable)
      [12]  default/linux/riscv/20.0/rv64gc/lp64d/systemd/merged-usr (stable)
      [13]  default/linux/riscv/20.0/rv64gc/lp64 (stable)
      [14]  default/linux/riscv/20.0/rv64gc/lp64/desktop (dev)
      [15]  default/linux/riscv/20.0/rv64gc/lp64/desktop/gnome (dev)
      [16]  default/linux/riscv/20.0/rv64gc/lp64/desktop/gnome/systemd (dev)
      [17]  default/linux/riscv/20.0/rv64gc/lp64/desktop/gnome/systemd/merged-usr (dev)
      [18]  default/linux/riscv/20.0/rv64gc/lp64/desktop/plasma (dev)
      [19]  default/linux/riscv/20.0/rv64gc/lp64/desktop/plasma/systemd (dev)
      [20]  default/linux/riscv/20.0/rv64gc/lp64/desktop/plasma/systemd/merged-usr (dev)
      [21]  default/linux/riscv/20.0/rv64gc/lp64/desktop/systemd (dev)
      [22]  default/linux/riscv/20.0/rv64gc/lp64/desktop/systemd/merged-usr (dev)
      [23]  default/linux/riscv/20.0/rv64gc/lp64/systemd (stable)
      [24]  default/linux/riscv/20.0/rv64gc/lp64/systemd/merged-usr (stable)
      [25]  default/linux/riscv/20.0/rv64gc/multilib (exp)
      [26]  default/linux/riscv/20.0/rv64gc/multilib/systemd (exp)
      [27]  default/linux/riscv/20.0/rv64gc/multilib/systemd/merged-usr (exp)
      [28]  default/linux/riscv/20.0/rv64gc/lp64d/musl (dev)
      [29]  default/linux/riscv/20.0/rv64gc/lp64/musl (dev)

`root `[`#`]`PORTAGE_CONFIGROOT=/usr/riscv64-unknown-linux-musl eselect profile set 28`

If a profile marked experimental `(exp)` is desired, use the `--force` flag to enable the profile.

To prevent errors from occurring while building the seed, the following `USE` flags should be set to prevent conflicts over the default [su] provider:

`root `[`#`]`mkdir /usr/riscv64-unknown-linux-musl/etc/portage/package.use `

`root `[`#`]`echo "sys-apps/util-linux -su" > /usr/riscv64-unknown-linux-musl/etc/portage/package.use/system `

or

`root `[`#`]`sed -i -e "s:-pam::" /usr/riscv64-unknown-linux-musl/etc/portage/make.conf`

Emerge the system:

`root `[`#`]`riscv64-unknown-linux-musl-emerge -va1 @system --keep-going`

** Note**\
At this point in the process, the Catalyst stage generation may be skipped and instead the system may be built by chrooting into the crossdev environment.

Create a seed tarball:

`root `[`#`]`cd /usr/riscv64-unknown-linux-musl/ `

`root `[`#`]`tar -cvJf /tmp/riscv64-musl-seed.tar.xz *`

### [Catalyst]

Install catalyst:

`root `[`#`]`emerge --ask dev-util/catalyst`

** Important**\
As of May 2023 the released version of Catalyst does not successfully build a stage 1 image. Try using the live ebuild instead.

Create a catalyst work directory, move the seed tarball to catalyst\'s workdir, and build a portage snapshot:

`root `[`#`]`mkdir -p /var/tmp/catalyst/builds `

`root `[`#`]`mv /tmp/riscv64-musl-seed.tar.xz /var/tmp/catalyst/builds/ `

`root `[`#`]`emerge --sync `

`root `[`#`]`mkdir -p /var/tmp/catalyst/repos; pushd /var/tmp/catalyst/repos/ `

`root `[`#`]`git clone --mirror /var/db/repos/gentoo `

`root `[`#`]`popd `

`root `[`#`]`catalyst --snapshot stable `

    18 May 2023 10:31:46 AEST: NOTICE  : Loading configuration file: /etc/catalyst/catalyst.conf
    NOTICE:catalyst:Loading configuration file: /etc/catalyst/catalyst.conf
    18 May 2023 10:31:46 AEST: NOTICE  : conf_values[options] = ['autoresume', 'bindist', 'kerncache', 'pkgcache', 'seedcache']
    NOTICE:catalyst:conf_values[options] = ['autoresume', 'bindist', 'kerncache', 'pkgcache', 'seedcache']
    18 May 2023 10:31:46 AEST: NOTICE  : >>> /usr/bin/git -C /var/tmp/catalyst/repos/gentoo.git fetch --quiet --depth=1
    NOTICE:catalyst:>>> /usr/bin/git -C /var/tmp/catalyst/repos/gentoo.git fetch --quiet --depth=1
    18 May 2023 10:31:46 AEST: NOTICE  : >>> /usr/bin/git -C /var/tmp/catalyst/repos/gentoo.git update-ref HEAD FETCH_HEAD
    NOTICE:catalyst:>>> /usr/bin/git -C /var/tmp/catalyst/repos/gentoo.git update-ref HEAD FETCH_HEAD
    18 May 2023 10:31:46 AEST: NOTICE  : >>> /usr/bin/git -C /var/tmp/catalyst/repos/gentoo.git gc --quiet
    NOTICE:catalyst:>>> /usr/bin/git -C /var/tmp/catalyst/repos/gentoo.git gc --quiet
    18 May 2023 10:31:47 AEST: NOTICE  : Creating gentoo tree snapshot afe106ae95ed7ba6536c870774c1b7e62d940ebd from /var/tmp/catalyst/repos/gentoo.git
    NOTICE:catalyst:Creating gentoo tree snapshot afe106ae95ed7ba6536c870774c1b7e62d940ebd from /var/tmp/catalyst/repos/gentoo.git
    18 May 2023 10:31:47 AEST: NOTICE  : >>> /usr/bin/git -C /var/tmp/catalyst/repos/gentoo.git archive --format=tar afe106ae95ed7ba6536c870774c1b7e62d940ebd |
    NOTICE:catalyst:>>> /usr/bin/git -C /var/tmp/catalyst/repos/gentoo.git archive --format=tar afe106ae95ed7ba6536c870774c1b7e62d940ebd |
    18 May 2023 10:31:47 AEST: NOTICE  :     /usr/bin/tar2sqfs /var/tmp/catalyst/snapshots/gentoo-afe106ae95ed7ba6536c870774c1b7e62d940ebd.sqfs -q -f -j1 -c gzip
    NOTICE:catalyst:    /usr/bin/tar2sqfs /var/tmp/catalyst/snapshots/gentoo-afe106ae95ed7ba6536c870774c1b7e62d940ebd.sqfs -q -f -j1 -c gzip
    18 May 2023 10:31:55 AEST: NOTICE  : Wrote snapshot to /var/tmp/catalyst/snapshots/gentoo-  .sqfs
    NOTICE:catalyst:Wrote snapshot to /var/tmp/catalyst/snapshots/gentoo-afe106ae95ed7ba6536c870774c1b7e62d940ebd.sqfs

Create the catalyst spec files that match the desired stage type:

Replace `afe106ae95ed7ba6536c870774c1b7e62d940ebd` in `snapshot_treeish` with the commit id that was given when running [catalyst -s stable]

`root `[`#`]`cd /var/tmp/catalyst`

[FILE] **`stage1-riscv64-musl-openrc.spec`**

    subarch: rv64_lp64d_musl
    target: stage1
    version_stamp: openrc-20230514
    interpreter: /usr/bin/qemu-riscv64
    rel_type: default
    profile: default/linux/riscv/20.0/rv64gc/lp64d/musl
    snapshot_treeish: afe106ae95ed7ba6536c870774c1b7e62d940ebd
    source_subpath: riscv64-seed
    compression_mode: pixz
    decompressor_search_order: xz bzip2
    update_seed: yes
    update_seed_command: -uDN @world

[FILE] **`stage3-riscv64-musl-openrc.spec`**

    subarch: rv64_lp64d_musl
    target: stage3
    version_stamp: openrc-20230514
    interpreter: /usr/bin/qemu-riscv64
    rel_type: default
    profile: default/linux/riscv/20.0/rv64gc/lp64d/musl
    snapshot_treeish: afe106ae95ed7ba6536c870774c1b7e62d940ebd
    source_subpath: default/stage1-rv64_lp64d_musl-openrc-20230518
    compression_mode: pixz
    decompressor_search_order: xz bzip2

Finally, using Catalyst, build a Stage 1 image from the seed tarball, and a Stage 3 image from the Stage 1 image:

`root `[`#`]`catalyst -f stage1-riscv64-musl-openrc.spec`

`root `[`#`]`catalyst -f stage3-riscv64-musl-openrc.spec`

** Tip**\
If [\@system] fails to build try checking out the [releng repo](https://github.com/gentoo/releng.git) and setting the `portage_confdir` variable to its location.

`user `[`$`]`git clone -o upstream `[`https://github.com/gentoo/releng.git`](https://github.com/gentoo/releng.git)` `

`user `[`$`]`doas su -c 'echo "portage_confdir = /path/to/releng/releases/portage/stages-qemu" >> /var/tmp/catalyst/builds/default/stage1-riscv64-musl-openrc.spec'`

This ensures that the most up-to-date portage configuration is available to the build process.

If this fails, and a suitable stage 3 image is avaialable, try using that as the seed. If that fails, or is unavailable, ask for support in `#gentoo-releng`.

If a stage successfully builds the output will be located at [/var/tmp/catalyst/builds/default].

### [Customise the RootFS]

Once a stage 3 image has been obtained or constructed the next task is personalisation of the root filesystem. This involves mounting the root filesystem, followed by executing a chroot command to enter it. For the purpose of the following commands, it is assumed that the root filesystem is stored at [/var/tmp/catalyst/builds/default/stage3-riscv64-musl-openrc-20230518.tar.xz].

`root `[`#`]`mkdir rootfs `

`root `[`#`]`tar xpvf /var/tmp/catalyst/builds/default/stage3-*.tar.xz --xattrs-include='*.*' --numeric-owner -C rootfs`

Emerge QEMU into the target and chroot; customise the system image (at least set the root password and add a regular user). Proceed with a typical Stage 3 configuration outside of Kernel and Bootloader.

`root `[`#`]`mount --bind rootfs rootfs `

`root `[`#`]`cd rootfs `

`root `[`#`]`ROOT=$PWD/ emerge --usepkgonly --oneshot --nodeps qemu `

`root `[`#`]`mount --bind /proc proc `

`root `[`#`]`mount --bind /sys sys `

`root `[`#`]`mount --bind /dev dev `

`root `[`#`]`mount --bind /dev/pts dev/pts`

`root `[`#`]`mkdir -p var/db/repos/gentoo `

`root `[`#`]`mount --bind /var/db/repos/gentoo var/db/repos/gentoo `

`root `[`#`]`mkdir -p usr/src/linux `

`root `[`#`]`mount --bind ../linux usr/src/linux `

`root `[`#`]`chroot . /bin/bash --login `

\
Modify the inittab file so that you can enable serial output on ttyS0. You will need to uncomment out the line for ttyS0 and change the speed.

[FILE] **`inittab`inittab**

    # SERIAL CONSOLES
    s0:12345:respawn:/sbin/agetty -L 115200 ttyS0 vt100
    #s1:12345:respawn:/sbin/agetty -L 9600 ttyS1 vt100

\
Install the kernel and modules to the rootfs image:

`root `[`#`]`pushd /usr/src/linux `

`root `[`#`]`make install && make modules_install`

If one is required to boot this configuration, or if it is otherwise desirable, generate an initramfs from within the chroot using a tool like Dracut.

`root `[`#`]`dracut --kver 6.1.0-rc3-hash`

Finally, exit the chroot and recursively unmount it:

`root `[`#`]` exit `

`root `[`#`]` umount -R rootfs`

### [Bootloader Configuration]

For this device it makes sense to use an extlinux configuration file (also known as U-Boot Standard Boot) to determine bootup parameters. This enables U-Boot to load a dynamic configuration from the disk, enabling the user to amend the bootloader configuration without requiring changes to the U-Boot environment.

U-boot is capable of reading from ext2, ext4 and FAT filesystems; each of these filesystems may be used to store the kernel and extlinux configuration file.

Regardless of the choice of filesystem, each of these files must be located in a directory called [/boot] on the root of the partition that it is located. This means that the kernel and configuration file must be located at [/boot/Image] and [/boot/extlinux/extlinux.conf] respectively.

Within the unpacked rootfs, with the kernel at [/boot/Image], create a file at [/boot/extlinux/extlinux.conf] that looks similar to this:

**NOTE:** For the mangopi you MUST use rootwait or you will get root file system kernel failures.

[FILE] **`/boot/extlinux/extlinux.conf`**

    label default
        linux /Image
        append root=/dev/mmcblk0p2 rootwait console=ttyS0,115200 console=tty0 earlycon=sbi rootflags=data=writeback rw no_console_suspend consleblank=0

## [Imaging the Device]

### [Boot Process]

The boot process of the D1-H SoC is as follows:

1.  When the SoC is powered on, the CPU fetches instructions beginning at address 0x0, where is the Boot ROM (BROM) or Primary Program Loader is located.
2.  The BROM loads the Secondary Program Loader (SPL) from some form of Non Volatile Memory (NVM).
3.  The SPL loads a U-Boot FIT image (presumably from the same NVM). This FIT image contains the U-Boot binary, the Device Tree Blob (DTB) and the OpenSBI binary. This image may be combined with the SPL.
4.  U-Boot loads the Linux Kernel.

In the context of the D1-H, the BROM is located in SoC itself on 64K of built-in memory. It may be upgraded in the field via SD card or USB. The BROM consists of two components: the Firmware Exchange Launch (FEL) module and the Medium Boot module. The FEL is responsible for writing data to local NVM, while the Medium Boot module is responsible for loading a legitimate BOOT0 (SPL) from NVM executing it. In devices with some form of permanently attached storage, the FEL may be used to recover from a failed boot or corrupted bootloader.

The BROM will attempt to load the SPL from (in order) onboard NOR/NAND memory, attached eMMC, or SD card storage. To do this it will look for a valid signature at 8k or 128k.

#### [Storage Layout]

** Important**\
The information in this section is specific to the boot process for *Allwinner* based SoCs. While this process is not well documented for RISC-V it seems to be the same as for arm64 Allwinner SoCs and should not be relied on if adapting these instructions for other manufacturers. Read the Device/SoC documentation to find out how the manufacturer expects it to boot and what the storage layout should be.

A typical Allwinner-based board has a U-Boot configured to use the following layout on (micro-)SD cards or eMMC storage (v2018.05 or later, legacy U-Boot versions used a different layout):

  ------- -------- ------ -----------------------------------------------
  start   sector   size   usage
  0KB     0        8KB    Unused, available for an MBR or (limited) GPT
  8KB     16       32KB   SPL loader
  40KB    80       \-     U-Boot proper
  ------- -------- ------ -----------------------------------------------

This layout is determined by:

-   The BROM, which looks for a valid EGON/TOC0 header at 8KB or 128KB (sectors 16 and 256 respectively) and loads the SPL from there
-   `40`(KB) being the default value for U-Boot\'s `CONFIG_SYS_MMCSD_RAW_MODE_U_BOOT_SECTOR` configuration item.

After this, partitions will typically begin from 1MB (which is the default setting of most partitioning tools); this is not a hard requirement, U-Boot may be larger than 984KB, if required.

** Note**\
If using a GPT partition table it is recommended that 128KB be used as the offset for the SPL as it may overlap with the GPT otherwise. While there are hacks to reduce the size of the GPT so that this will not occur it is more compatible to use the higher offset.

`CONFIG_SYS_MMCSD_RAW_MODE_U_BOOT_SECTOR` will need to be adjusted to cater for the new U-Boot offset if not using a combined SPL+U-Boot image.

Alternately `-j 4064` may be passed to [sgdisk] to manipulate the partition table so that a gap is placed between the headers and entries, avoiding this problem altogether.

** Tip**\
The SPL may be configured to load U-Boot from a different location, such as the FAT partition used for [/boot]. This is useful for development purposes, but is not recommended for production deployments; Try enabling `CONFIG_SPL_FS_FAT` in the U-Boot configuration. It\'s even possible to change this layout entirely and use `CONFIG_SYS_MMCSD_RAW_MODE_U_BOOT_USE_PARTITION` to read from a RAW partition on the boot device (a few MB should be fine) and load U-Boot from there.

### [Partition Table]

When partitioning a disk image for the MQ-Pro, ensure that sufficient space is left at the beginning of the image so that the SPL and U-Boot are not accidentally overwritten.

[/boot] may be combined with the rootfs or a separate partition. U-boot supports FAT, ext2, and ext4 - this limits the choice of rootfs filesystems to those that are supported by U-Boot, however.

** Tip**\
Creating an image may be skipped and [/dev/loop0] may be substituted with the appropriate device node if working with a physical TF card/eMMC device.

Create an image and mount it on an available loop device:

`user `[`$`]`fallocate -l 8G mangopi.img `

`user `[`$`]`doas losetup --find --show mangopi.img `

/dev/loop0

Use [sgdisk] to create partitions; reserve 10M (this is \'very\' conservative) at the beginning of the image/disk for the SPL and U-Boot, and create a 200M boot partition. The remaining space may be used for the rootfs:

`root `[`#`]

    sgdisk --clear --set-alignment=2 \
      --new=1:10M:+200M --change-name=1:boot --typecode=1:EBD0A0A2-B9E5-4433-87C0-68B6B72699C7 \
      --new=2:210M:0 --change-name=2:root --typecode=2:0FC63DAF-8483-4772-8E79-3D69D8477DE4 \
      /dev/loop0

    Creating new GPT entries in memory.
    Warning: The kernel is still using the old partition table.
    The new table will be used at the next reboot or after you
    run partprobe(8) or kpartx(8)
    The operation has completed successfully.

** Tip**\
Using a RAW partition boot mode might look more like:

`root `[`#`]

    sgdisk --clear --set-alignment=2 \
      --new=1:3M:10M --change-name=1:uboot --typecode=1:BC13C2FF-59E6-4262-A352-B275FD6F7172  \
      --new=2:10M:+200M --change-name=2:boot --typecode=2:EBD0A0A2-B9E5-4433-87C0-68B6B72699C7 \
      --new=3:210M:0 --change-name=3:root --typecode=3:0FC63DAF-8483-4772-8E79-3D69D8477DE4 \
      /dev/loop0

### [Write the SPL and U-Boot]

The SPL and U-Boot may be written to the image using [dd].

Write the SPL + U-Boot to the image at 128k:

`root `[`#`]`dd if=u-boot-sunxi-with-spl.bin of=/dev/loop0 bs=1024 seek=128 `

    914+1 records in
    914+1 records out
    936729 bytes (937 kB, 915 KiB) copied, 0.00485607 s, 193 MB/s

If not using the SPL + U-Boot image either write the SPL to the image at 128k instead, then write U-boot to the image at 1024K or to the specified partition (RAW modes), or write the file to the FAT partition of the image. For a RAW partition layout it should be written to the beginning of the partition.

`root `[`#`]`dd if=u-boot/spl/u-boot-spl.bin of=/dev/loop0 bs=1024 seek=128 `

`root `[`#`]`dd if=u-boot/u-boot.itb of=/dev/loop0 bs=1024 seek=1024`

### [Format and Mount the Boot and Root Partitions]

The boot partition may be formatted with [mkfs.fat]:

`root `[`#`]`mkfs.fat -F 32 -n boot /dev/loop0p1 `

`root `[`#`]`mkfs.ext4 -L root /dev/loop0p2 `

** Tip**\
For a more conventional [/boot] layout, make [/boot] a symlink to [/mnt/sdcard/boot] and mount the sdcard at [/mnt/sdcard].

`root `[`#`]`mkdir -p /mnt/mangopi `

`root `[`#`]`mount /dev/loop0p2 /mnt/mangopi `

`root `[`#`]`cp -a rootfs/* /mnt/mangopi `

`root `[`#`]`mkdir -p /mnt/mangopi/mnt/sdcard `

`root `[`#`]`mount /dev/loop0p1 /mnt/mangopi/mnt/sdcard `

`root `[`#`]`mv /mnt/mangopi/boot /mnt/mangopi/mnt/sdcard/ `

`root `[`#`]`ln -s /mnt/sdcard/boot /mnt/mangopi/boot `

Edit fstab to cater for any file systems that need to be mounted on the device, then unmount the image:

`root `[`#`]`umount -R /mnt/mangopi/mnt/sdcard `

`root `[`#`]`sync `

`root `[`#`]`losetup -d /dev/loop0`

### [Burn the image to an SD card]

There are many methods available to do this. Balena etcher is a common method for those that want an easy-to-use GUI, however this example will use [dd]:

`root `[`#`]`dd if=mangopi.img | pv | dd of=/dev/mmcblk0 bs=4M`

If the SD card is larger than the size of the disk image (which is recommended; it saves a lot of time when imaging) [resize2fs] or a similar utility depending on file system may be used to resize the rootfs partition.

Move the secondary GPT to the actual end of the disk, delete the last partition then recreate it, and finally resize the file system:

`root `[`#`]`sgdisk -e /dev/mmcblk0 `

`root `[`#`]`sgdisk -d 2 /dev/mmcblk0 `

`root `[`#`]`sgdisk -N 2 /dev/mmcblk0 `

`root `[`#`]`partprobe /dev/mmcblk0p2 `

`root `[`#`]`resize2fs /dev/mmcblk0p2`

## [Boot the D1]

Insert the SD card into the device and power it on. The device should boot from the SD card. If the device does not boot successfully connect the UART tty and check the U-Boot output.

\

## [See also]

-   [RISC-V hardware list](https://wiki.gentoo.org/wiki/RISC-V_hardware_list "RISC-V hardware list") --- a list of **RISC-V hardware** owned by the Gentoo community within the [[#gentoo-riscv](ircs://irc.libera.chat/#gentoo-riscv)] ([[webchat](https://web.libera.chat/#gentoo-riscv)]) channel.
-   [Embedded Handbook](https://wiki.gentoo.org/wiki/Embedded_Handbook "Embedded Handbook") --- a collection of community maintained documents providing a consolidation of embedded and SoC knowledge for Gentoo.

## [External resources]

-   [linux-sunxi D1 SDK Howto](https://linux-sunxi.org/D1_SDK_Howto)
-   [linux-sunxi U-Boot info](https://linux-sunxi.org/U-Boot)
-   [D1 User Manual](https://mangopi.org/_media/d1-h_user_manual_v1.0.pdf)
-   [Combining Sunxi Boot with GUID Partition Tables](https://zameermanji.com/blog/2021/11/22/combining-sunxi-boot-with-guid-partition-tables/)
-   [LKML: riscv: Allwinner D1 platform support](https://lore.kernel.org/lkml/20220815050815.22340-12-samuel@sholland.org/T/#m331b9f3fa53dc86956f08a8e83844978c0513096)