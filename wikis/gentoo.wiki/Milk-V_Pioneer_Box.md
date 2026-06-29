Gentoo on the [Milk-V Pioneer Box](https://milkv.io/pioneer).

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Serial console]](#Serial_console)
    -   [[1.2] [RISC-V and MCU consoles]](#RISC-V_and_MCU_consoles)
    -   [[1.3] [Mainboard console]](#Mainboard_console)
-   [[2] [Early boot process]](#Early_boot_process)
-   [[3] [Installing Gentoo]](#Installing_Gentoo)
    -   [[3.1] [Preparing the disks (the easy way)]](#Preparing_the_disks_.28the_easy_way.29)
    -   [[3.2] [Installing the Gentoo installation files]](#Installing_the_Gentoo_installation_files)
    -   [[3.3] [Installing the Gentoo base system]](#Installing_the_Gentoo_base_system)
    -   [[3.4] [CFLAGS]](#CFLAGS)
    -   [[3.5] [VIDEO_CARDS]](#VIDEO_CARDS)
    -   [[3.6] [Configuring the Linux kernel]](#Configuring_the_Linux_kernel)
    -   [[3.7] [Configuring the bootloader]](#Configuring_the_bootloader)
-   [[4] [Firmware]](#Firmware)
    -   [[4.1] [Video card]](#Video_card)
        -   [[4.1.1] [Dracut]](#Dracut)
        -   [[4.1.2] [References]](#References)
    -   [[4.2] [Onboard NIC]](#Onboard_NIC)
-   [[5] [Microarchitectural vulnerabilities]](#Microarchitectural_vulnerabilities)
    -   [[5.1] [GhostWrite]](#GhostWrite)
    -   [[5.2] [Security RISCs]](#Security_RISCs)
        -   [[5.2.1] [Cache+Time (new)]](#Cache.2BTime_.28new.29)
        -   [[5.2.2] [Flush+Fault (new)]](#Flush.2BFault_.28new.29)
        -   [[5.2.3] [CycleDrift (new)]](#CycleDrift_.28new.29)
        -   [[5.2.4] [Flush+Flush / Fence+Flush (old)]](#Flush.2BFlush_.2F_Fence.2BFlush_.28old.29)
-   [[6] [Building the bootloader]](#Building_the_bootloader)
    -   [[6.1] [LinuxBoot]](#LinuxBoot)
    -   [[6.2] [EDK2]](#EDK2)
    -   [[6.3] [zsbl]](#zsbl)
    -   [[6.4] [OpenSBI]](#OpenSBI)
    -   [[6.5] [U-Boot]](#U-Boot)
    -   [[6.6] [GRUB]](#GRUB)
-   [[7] [Changing the boot flow]](#Changing_the_boot_flow)
    -   [[7.1] [Using an SD card]](#Using_an_SD_card)
        -   [[7.1.1] [GRUB example]](#GRUB_example)
    -   [[7.2] [Overwriting the SPI flash]](#Overwriting_the_SPI_flash)
        -   [[7.2.1] [The short version]](#The_short_version)
        -   [[7.2.2] [The long version]](#The_long_version)
    -   [[7.3] [Miscellaneous references]](#Miscellaneous_references)
-   [[8] [Solved problems]](#Solved_problems)
    -   [[8.1] [The boot process periodically hangs]](#The_boot_process_periodically_hangs)
        -   [[8.1.1] [LinuxBoot flow]](#LinuxBoot_flow)
        -   [[8.1.2] [EDK2/GRUB flow]](#EDK2.2FGRUB_flow)
    -   [[8.2] [Box stops powering on]](#Box_stops_powering_on)
    -   [[8.3] [Nothing happens when booting from an SD card]](#Nothing_happens_when_booting_from_an_SD_card)
    -   [[8.4] [Flaky console keyboard]](#Flaky_console_keyboard)
    -   [[8.5] [No hardware clock]](#No_hardware_clock)
    -   [[8.6] [No sound]](#No_sound)
    -   [[8.7] [Clock skew detected!]](#Clock_skew_detected.21)
    -   [[8.8] [SD card stops working]](#SD_card_stops_working)
    -   [[8.9] [GPU Lockups]](#GPU_Lockups)
-   [[9] [Unsolved problems]](#Unsolved_problems)
    -   [[9.1] [USB keyboard/mouse stop working]](#USB_keyboard.2Fmouse_stop_working)
    -   [[9.2] [NVMe is flaky]](#NVMe_is_flaky)

## [Hardware]

The best resource for the hardware inside the Pioneer Box is [https://milkv.fyi/](https://milkv.fyi/). We will avoid repeating the information there, and note only the default partition layout on the 1TB NVMe drive.

  ----------------------------------------------------------------------------------------------------- ---------------------- ------------------------------------------------------------------------------------------------ ------
  Partition                                                                                             Description            Fedora 38 mount point                                                                            Size
  [/dev/nvme0n1p1]   FAT32 UEFI partition   [/boot/efi]   122M
  [/dev/nvme0n1p2]   ext4 boot partition    [/boot]       488M
  [/dev/nvme0n1p3]   ext4 Fedora 38 root    [/]           14G
  ----------------------------------------------------------------------------------------------------- ---------------------- ------------------------------------------------------------------------------------------------ ------

This leaves roughly 939.2G at the end of the drive unused. The perfect place to install Gentoo.

### [Serial console]

The serial console on the box is exposed via the USB-C port on the front of the case. It is connected to UART Bridge controller on the motherboard. If you attach to it using a USB **data** cable, you should see something like the following on the client machine:

[FILE] **`/var/log/dmesg`**

    [156955.801245] usb 1-1.1: new full-speed USB device number 3 using ehci-pci
    [156955.906915] usb 1-1.1: New USB device found, idVendor=10c4, idProduct=ea60, bcdDevice= 1.00
    [156955.906924] usb 1-1.1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
    [156955.906928] usb 1-1.1: Product: CP2102 USB to UART Bridge Controller
    [156955.906931] usb 1-1.1: Manufacturer: Silicon Labs
    [156955.906933] usb 1-1.1: SerialNumber: 0001

To make use of this, you need two kernel modules (again on the client):

[KERNEL] **Serial-to-USB modules for the Pioneer**

    Device Drivers
      -> <m> USB support (CONFIG_USB_SUPPORT)
        -> <m> USB Serial Converter support (CONFIG_USB_SERIAL)
          -> <m> USB CP210x family of UART Bridge Controllers (CONFIG_USB_SERIAL_CP210X)

The resulting modules are called `usbserial` and `cp210x`. If you have them loaded, you should see e.g. [/dev/ttyUSB0] created when you connect your USB cable to the Pioneer:

[FILE] **`/var/log/dmesg`**

    [ 1459.897552] cp210x 4-1:1.0: cp210x converter detected
    [ 1459.901513] usb 4-1: cp210x converter now attached to ttyUSB0
    [ 5148.313291] usb 4-1: USB disconnect, device number 5

Now just run screen (this requires root or sudo unless you\'ve added yourself to the [[[acct-group/dialout]](https://packages.gentoo.org/packages/acct-group/dialout)[]] group),

`user `[`$`]`screen /dev/ttyUSB0 115200`

and reboot the Pioneer.

### [RISC-V and MCU consoles]

But wait, there\'s more. On the Pioneer Box, the front-of-the-box serial port/cable is already attached to the pins on the motherboard. But there are at two other serial consoles available, both having three pins and running at 3.3 volts:

1.  The \"RISC-V\" console. This is labeled and you can see it on the motherboard.
2.  The \"MCU\" console. Again, labeled. Its pins are right next to the \"RISC-V\" console pins.

To connect to these, you\'ll need another adapter. I\'m sure there are others that will work, but I\'ve used the three-pin [TTL-232R-RPI from FTDI](https://ftdichip.com/products/ttl-232r-rpi/). It\'s well-documented, inexpensive, and the kernel drivers for it are upstream:

[KERNEL]

    Device Drivers
      -> <y> USB support
        -> <m> USB Serial Converter support
          -> <m> USB FTDI Single Port Serial Driver

This will build a module called `ftdi_sio` that will detect the adapter and give you a [/dev/ttyUSBX] to connect to with `screen` on the client:

[FILE] **`/var/log/dmesg`**

    [Wed Sep 11 13:46:30 2024] usb 2-3: FTDI USB Serial Device converter now attached to ttyUSB0

** Note**\
Maybe I\'m just new at this, but on my board, the labels for the three RX/TX/GND pins are all off-by-one. The sets on the board actually consists of *four* pins, the last one being labeled with merely a dot. I had to shift all three of my cables down by one to get anything on the console:

-   RX cable -\> dot pin,
-   TX cable -\> RX pin
-   GND cable -\> TX pin

### [Mainboard console]

But wait, there\'s more. There\'s *also* a secret (undocumented) [mainboard console](https://github.com/milkv-pioneer/issues/issues/33#issuecomment-1919711235). This shows output even before the RISC-V console does.

## [Early boot process]

Out of the box, the Pioneer uses LinuxBoot to launch a customized version of Fedora 38, but there are actually several possible [boot paths](https://github.com/sophgo/sophgo-doc/blob/main/SG2042/HowTo/bootflow.rst). The process is summarized below. Later we go into more detail about [changing the boot flow](#Changing_the_boot_flow).

1.  The board determines whether or not a usable SD card is inserted. For example, the following output from the [mainboard console](#Mainboard_console) shows an SD card being detected:

        NOTICE:  BOOT: 0x7000140000/0x1/0x5
        NOTICE:  Booting Trusted Firmware
        NOTICE:  BL1: v2.7(release):83c4f9e3e
        NOTICE:  BL1: Built : 10:39:27, Jul 12 2022
        INFO:    BL1: RAM 0x7010002000 - 0x7010011000
        NOTICE:  SD initializing 100000000Hz
        Hit key to stop autoboot: 00
        NOTICE:  BOOT: 0x7000140000/0x1/0x5
        NOTICE:  Booting Trusted Firmware
        NOTICE:  BL1: v2.7(release):83c4f9e3e
        NOTICE:  BL1: Built : 10:39:27, Jul 12 2022
        INFO:    BL1: RAM 0x7010002000 - 0x7010011000
        NOTICE:  SD initializing 100000000Hz
        NOTICE:  boot from SD

    If an SD card is inserted, then from now on, everything will be relative to the the first FAT32 partition on the SD card. Otherwise, they\'ll refer to \"files\" stored on the SPI flash ([/dev/mtd0]), which does not have a nice filesystem on it (more on this later).

2.  [fip.bin] is loaded from either the SD card or the SPI flash (see the first step). This is a Firmware Image Package (FIP), presumably generated using [fiptool](https://github.com/sophgo/fiptool). It is most likely signed and encrypted according to the [SOPHGO Secure Boot User Guide](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/en/01.software/BSP/Secure_Boot_User_Guide/build/html/index.html), making it difficult to replace. [An updated copy of fip.bin](https://github.com/sophgo/edk2-non-osi/blob/devel-sg2042/Silicon/Sophgo/SG2042/Boot/fip.bin) lives in SOPHGO\'s [edk2-non-osi](https://github.com/sophgo/edk2-non-osi/) repository. We see from the [mainboard console](#Mainboard_console) that [fip.bin] is indeed loaded from an inserted SD card:

        INFO:    BL1: Loading BL2
        NOTICE:  Locate FIP in SD FAT
        INFO:    Loading image id=1 at address 0x7010020000
        INFO:    Image id=1 loaded: 0x7010020000 - 0x701005ca41
        NOTICE:  BL1: Booting BL2

3.  The [zero stage bootloader](https://github.com/sophgo/zsbl) (ZSBL) is loaded from [zsbl.bin] either on the SD card or from the SPI flash. ZSBL reads a configuration file [riscv64/conf.ini] (either from SPI flash or from the SD card), collects the relevant information, and then hands it off to OpenSBI. This process is handled by the [boot() function](https://github.com/sophgo/zsbl/blob/master/plat/sg2042/boot.c).

4.  [OpenSBI](https://github.com/sophgo/opensbi) runs.

5.  Depending on [riscv64/conf.ini], one of [LinuxBoot](https://www.linuxboot.org/), [U-Boot](https://www.denx.de/project/u-boot/), or [EDK2](https://github.com/sophgo/sophgo-edk2)/GRUB are launched next.

    LinuxBoot

    :   :::
        ** Warning**\
        EDK2/GRUB is now the recommended approach.
        :::

        This is the stock bootloader. It loads its own early-stage initramfs ([riscv64/initrd.img]) and Linux kernel ([riscv64/riscv64_Image]), both of which are included in the stock Fedora under [/boot/efi/riscv64]. Those copies are not actually used, however. The real copies are stored in the SPI flash where you can\'t easily access them. Before LinuxBoot loads, a serial console is needed to see the output from the boot process, but eventually it initializes the display and you can see what\'s going on. Hardware support is likely why this is the default boot method. Linux already has drivers for your hardware, but e.g. U-Boot does not.

    EDK2/GRUB
    :   This process uses a file called [riscv64/SRA1-20.fd] that is the result of building EDK2, and EDK2 is the \"official\" implementation of UEFI. The file [riscv64/SRA1-20.fd] knows to hand-off the rest of the process to a GRUB EFI image living at some predetermined path, which is why we call this the \"EDK2/GRUB\" process and not just \"EDK2.\" The file shipped with the Pioneer is named [riscv64/SG2042.fd], but newer versionsof EDK2 have renamed it. (The name doesn\'t actually matter, so long as you point [riscv64/conf.ini] to the correct file.) **Of the three, this is the recommended boot path, as it can easily be built on Gentoo and works with newer kernels.**

    U-Boot

    :   :::
        ** Warning**\
        EDK2/GRUB is now the recommended approach.
        :::

        U-Boot is a more minimal UEFI implementation. You build U-Boot to get [u-boot.bin], which in turn is what you point [conf.ini] at. U-Boot can then itself launch the GRUB EFI image, or any other image. This is a little bit faster (and a lot easier to build) than its EDK2 counterpart.

## [Installing Gentoo]

The easiest (and safest) way to install Gentoo is to take advantage of the empty space at the end of the NVMe drive. This leaves the stock Fedora available if you shoot yourself in the foot. The process roughly follows the Gentoo installation handbook, with a few modifications. There is no RISC-V handbook, but you should read and understand (say) the [amd64 handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64 "Handbook:AMD64") before attempting this. We mention only the steps that differ.

### [][Preparing the disks (the easy way)]

1.  Instead of using a LiveUSB, boot into the Fedora 38 that ships with the box.
2.  Log in, open a terminal, and `su` to root.
3.  Run `cfdisk /dev/nvme0n1`, and create a new primary partition of type 83/Linux using the rest of the disk. Keep the existing UEFI and boot partitions, ignoring swap entirely :)
4.  Save your changes and format the new partition, [/dev/nvme0n1p4], with your favorite filesystem.
5.  `mkdir /mnt/gentoo`

### [Installing the Gentoo installation files]

1.  Download an rv64gc/lp64d stage3 from [https://www.gentoo.org/downloads/#riscv](https://www.gentoo.org/downloads/#riscv). These are the architecture and floating point ABI [supported by the C920 processors](https://github.com/sophgocommunity/Pioneer_Doc/blob/main/resources/T-Head_XuanTie_C920_Processor_Datasheet.pdf?raw=true) in the Pioneer.
2.  Follow the handbook.

### [Installing the Gentoo base system]

### [CFLAGS]

** Warning**\
Read the [GhostWrite](#GhostWrite) section before choosing your `CFLAGS`.

According to [/proc/cpuinfo], the C920 processors in the Pioneer box have an ISA of `rv64gcv`, which is [shorthand](https://en.wikipedia.org/wiki/RISC-V#ISA_base_and_extensions) for `rv64imafdcv`. The \"v\" however refers not to the final, ratified v1.0 of the vector extension, but instead to a draft v0.7.1 that is known by the name `XTheadVector`. So long as you have [gcc-14 or newer](https://gcc.gnu.org/gcc-14/changes.html#riscv) though, the draft extension is supported as well. To enable it within GCC, you can add (for example)

[FILE] **`/etc/portage/make.conf`**

    COMMON_FLAGS="$COMMON_FLAGS -march=rv64gcv"

to your [make.conf]. Beware however that this can make you vulnerable to [GhostWrite](#GhostWrite), which exploits `XTheadVector`. A safer choice is to omit the \"v\":

[FILE] **`/etc/portage/make.conf`**

    COMMON_FLAGS="$COMMON_FLAGS -march=rv64gc"

In addition to `-march`, there are `-mabi` and `-mtune` flags that may help:

[FILE] **`/etc/portage/make.conf`**

    COMMON_FLAGS="$COMMON_FLAGS $ -mtune=thead-c906"

At the time of writing, the variable `$` is defined in the riscv profiles ([profiles/arch/riscv/make.defaults]) and is equivalent to `-mabi=lp64d`. The `-mtune=thead-c906` tells GCC to optimize for the T-Head C906, a close relative of the C920s in the Pioneer Box. As of GCC 16 `-mtune=xt-c920` can be used (xt-c920 is for systems that implement RVV 0.7.1, while xt-c920v2 is for RVV 1.0).

References:

1.  [https://gcc.gnu.org/onlinedocs/gcc/RISC-V-Options.html](https://gcc.gnu.org/onlinedocs/gcc/RISC-V-Options.html)
2.  [https://www.sifive.com/blog/all-aboard-part-1-compiler-args](https://www.sifive.com/blog/all-aboard-part-1-compiler-args)
3.  [https://www.reddit.com/r/RISCV/comments/1c7fyd6/differences_between_the_xuantie_c906_c910_and_c920/](https://www.reddit.com/r/RISCV/comments/1c7fyd6/differences_between_the_xuantie_c906_c910_and_c920/)
4.  [https://www.phoronix.com/news/GCC-XuanTie-RISC-V-CPUs](https://www.phoronix.com/news/GCC-XuanTie-RISC-V-CPUs)

### [VIDEO_CARDS]

This is our video card,

`user `[`$`]`lspci -k | head -n5 `

    0000:00:00.0 PCI bridge: Device 1e30:2042
    0000:01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Caicos [Radeon HD 6450/7450/8450 / R5 230 OEM]
            Subsystem: Hightech Information System Ltd. Device 3000
            Kernel driver in use: radeon
            Kernel modules: radeon, amdgpu

And according to the [Radeon](https://wiki.gentoo.org/wiki/Radeon "Radeon") page, the value of `VIDEO_CARDS` corresponding to the [Caicos R5 230 card](#Hardware) should be,

[FILE] **`/etc/portage/make.conf`**

    VIDEO_CARDS="radeon r600"

### [Configuring the Linux kernel]

We\'re going to build our own kernel, if for no other reason than to mitigate [GhostWrite](#GhostWrite). Your best bet is to use the latest linux-next, until further notice. There are still some patches floating around (not merged in the upstream kernel) to fix important issues. I have consolidated these into one big patch against the linux-next kernel:

-   [https://dev.gentoo.org/\~mjo/distfiles/linux-next-20260508-sg2042.patch](https://dev.gentoo.org/~mjo/distfiles/linux-next-20260508-sg2042.patch)

(Most of those are destined for upstream but at least one will probably be rewritten and resubmitted.)

** Warning**\
You must build the latest bootloader (zsbl, OpenSBI, and EDK2) to use an upstream kernel. Make sure you have the latest fip.bin as well!

In addition to the options below, there are the \"Gentoo\" kernel options that we won\'t have if we\'re not using [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]]. Rather than list them all here, I will just tell you to [read the patch that adds these options](https://dev.gentoo.org/~mpagano/genpatches/trunk/6.15/4567_distro-Gentoo-Kconfig.patch), and figure out for yourself which ones you want.

Finally, we will also be missing the [Gentoo patch that adds additional linking restrictions](https://dev.gentoo.org/~mpagano/genpatches/trunk/6.15/1510_fs-enable-link-security-restrictions-by-default.patch). These are unlikely to break anything, but the hardlink patch does technically violate POSIX. In any case, you should enable them through sysctl instead:

[FILE] **`/etc/sysctl.d/fs-protections.conf`**

    fs.protected_fifos = 2
    fs.protected_regular = 2
    fs.protected_symlinks = 1
    fs.protected_hardlinks = 1

CONFIG_ARCH_SOPHGO=y

General support for the Sophgo SoC.

CONFIG_ERRATA_THEAD=y, CONFIG_ERRATA_THEAD_MAE=y, CONFIG_ERRATA_THEAD_CMO=y

Errata for THead products. Might not be necessary, but the C920 processor is from THead. Enabling the errata won\'t hurt anything if it doesn\'t apply to your machine, so better safe than sorry.

ERRATA_THEAD_WRITE_ONCE=y

Another errata for your processor. Requires [a patch](https://lore.kernel.org/sophgo/20260421143154.1590156-1-guoren@kernel.org/T) on top of linux-next (as of 2026-05-17).

[https://lore.kernel.org/sophgo/20260421143154.1590156-1-guoren@kernel.org/T/#u](https://lore.kernel.org/sophgo/20260421143154.1590156-1-guoren@kernel.org/T/#u)

RISCV_ISA_V=n

Can be used to disable the CPU\'s vector extension. You should probably disable it to mitigate [Ghostwrite](#GhostWrite).

CONFIG_MMU=y

You want virtual memory. The C920 has an [SV39](https://docs.kernel.org/arch/riscv/vm-layout.html)-compatible MMU.

CONFIG_EFI=y

This might be necessary to use the \"platform reset,\" but more importantly, it lets U-Boot launch this kernel directly without having to go through GRUB.

CONFIG_DRM=y, CONFIG_DRM_RADEON=y

Support direct rendering with the [Radeon](https://wiki.gentoo.org/wiki/Radeon "Radeon") CAICOS card. Needed for the framebuffer console, among other things.

CONFIG_FB_RADEON=y, CONFIG_DRM_FBDEV_EMULATION=y

Support a framebuffer console with the supplied Radeon card. Building this in to the kernel should give you visible output (sans a serial cable) a tiny bit sooner.

CONFIG_BLK_DEV_NVME=y

Support the NVMe drive with all of your files on it. You should probably build this in, just in case.

CONFIG_R8169=m, CONFIG_IXGBE=m

Modules for the Realtek (onboard) and Intel (PCIe) NICs

CONFIG_RTC_DS1307=y, CONFIG_RTC_DRV_EFI=n

Hardware clocks for keeping time when the machine reboots. The first one is for the \"real\" clock. An EFI clock is visible but doesn\'t work as far as I can tell, so it just gets in the way. Compile the real one in to avoid [a temporary clock skew issue](#Clock_skew_detected.21).

CONFIG_SPI=y, CONFIG_SPI_SG2044_NOR=m

Not a typo, the 2044 driver provides the \"sg2042-spifmc-nor\" compatible. For the built-in flash memory.

CONFIG_RISCV_PMU_SBI=y

Hardware support for performance events to be monitored with [[[dev-util/perf]](https://packages.gentoo.org/packages/dev-util/perf)[]].

CONFIG_SND_PCI=y, CONFIG_SND_HDA_INTEL=m, CONFIG_SND_HDA_CODEC_HDMI=m

Support audio via HDMI/DisplayPort on the Radeon (the only sound card in the machine).

CONFIG_SND_PCM_TIMER=y, CONFIG_SND_SEQUENCER=y

Not strictly required, but you should enable them if you want your media player to make noise.

CONFIG_DEBUG_FS=?

If you really want to be able to change the CPU frequency, it is possible using debugfs and by [hacking the kernel source code](https://github.com/sophgo/sophgo-doc/blob/main/SG2042/HowTo/How%20to%20adjust%20CPU%20operating%20frequency.rst).

CONFIG_MMC_BLOCK=y, CONFIG_MMC_SDHCI_PLTFM=y, CONFIG_MMC_SDHCI_OF_DWCMSHC=y

Support for the SD card reader, and for using an SD card as a block device. Compile them in, in case you need to boot from an SD card in an emergency.

CONFIG_GPIO_DWAPB=m

According to [the device tree](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/arch/riscv/boot/dts/sophgo/sg2042.dtsi), this is the GPIO controller we have.

CONFIG_SPI_DW_MMIO=m

I don\'t know what this does, but we have one. At the very least it makes [/sys/bus/platform/drivers/dw_spi_mmio] available.

CONFIG_PCIE_SG2042_HOST=y

The PCIe controller on the board.

CONFIG_SOPHGO_SG2042_MSI=y

The MSI controller on the board.

CONFIG_SENSORS_SG2042_MCU=m

Provides power control and some basic hardware information.

CONFIG_SOPHGO_SG2042_PLL=m, CONFIG_CLK_SOPHGO_SG2042_CLKGEN=m, CONFIG_SOPHGO_SG2042_RPGATE=m

Clock support.

CONFIG_I2C_DESIGNWARE_PLATFORM=y

According to [the device tree](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/arch/riscv/boot/dts/sophgo/sg2042.dtsi), this is the I2C controller we have. Again I don\'t know how this helps, but it does seem to work. With the module loaded, I can run e.g.

`user `[`$`]`cat /sys/devices/platform/soc/7030005000.i2c/i2c-8/name`

Synopsys DesignWare I2C adapter

Compiling it in plays a part in [avoiding clock skew](#Clock_skew_detected.21).

CONFIG_PWM=y, CONFIG_PWM_SOPHGO_SG2042=m

Enable the pulse-width modulation driver for power delivery and voltage regulation (often used, for example, to control fan speed).

CONFIG_PINCTRL=y, CONFIG_PINCTRL_SOPHGO_SG2042=m

Parses the pin configuration from the device tree and supports multiplexing.

RISCV_EFFICIENT_UNALIGNED_ACCESS=y

Assume that unaligned memory access is fast. True on my box, and avoids probing for it at each boot.

### [Configuring the bootloader]

Unfortunately, in order to use an upstream kernel, we must [build our own bootloader](#Building_the_bootloader). You should build ZSBL, OpenSBI, and EDK2/GRUB. These can all (make sure you get the correct branch!) be built from within Gentoo. Afterwards, you\'ll need to [change the boot flow](#Changing_the_boot_flow) to use EDK2/GRUB, since it is not the default. You should do this on an SD card to avoid breaking the default boot path.

**Update**: recent binaries of ZSBL ([zsbl.bin]), OpenSBI ([fw_dynamic.bin]), and [fip.bin] are now available [in one of the SOPHGO repositories](https://github.com/sophgo/edk2-non-osi/tree/devel-sg2042/Silicon/Sophgo/SG2042/Boot).

## [Firmware]

During installation, you\'ll have the chance to install [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]]. Gentoo allows fine-grained control of which [Linux firmware](https://wiki.gentoo.org/wiki/Linux_firmware "Linux firmware") are installed. In particular, the [savedconfig](https://wiki.gentoo.org/wiki/Savedconfig "Savedconfig") feature can be used to choose only the necessary blobs. The following is a short but comprehensive list; only the video card and onboard NIC require firmware blobs.

### [Video card]

Provided by [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]]

-   [radeon/BTC_rlc.bin]
-   [radeon/CAICOS_mc.bin]
-   [radeon/CAICOS_me.bin]
-   [radeon/CAICOS_pfp.bin]
-   [radeon/CAICOS_smc.bin]
-   [radeon/SUMO_uvd.bin]

#### [Dracut]

If you use dracut, then you should instruct it to include the video card\'s firmware into the initial ramdisk:

[FILE] **`/etc/dracut.conf.d/radeon.conf`**

    install_items+=" /usr/lib/firmware/radeon/* "

Otherwise your system may boot successfully, e.g., reachable via network, but the display will stay black, because Linux is not able to initialize the video card.

#### [References]

1.  [Radeon page on the Gentoo wiki](https://wiki.gentoo.org/wiki/Radeon#Firmware "Radeon")
2.  [GPU Firmware on milkv.fyi](https://milkv.fyi/en/firmware.html#gpu-firmware)

### [Onboard NIC]

1.  [rtl_nic/rtl8125b-2.fw]

References:

1.  [Firmware page on milkv.fyi](https://milkv.fyi/en/firmware.html#firmware)

## [Microarchitectural vulnerabilities]

### [GhostWrite]

The Pioneer Box is vulnerable to [GhostWrite](https://ghostwriteattack.com/). To mitigate the vulnerability, you have choices. You can do it in userspace, by ensuring that you don\'t compile any code with support for the vector instructions. Take for example the [GhostWrite proof-of-concept](https://github.com/cispa/ghostwrite), contained in [ghostwrite.c]. If we try to compile it with the vector instructions enabled via `-march=rv64gcv`, it works:

`user `[`$`]`gcc -march=rv64gcv -o ghostwrite ghostwrite.c `

`user `[`$`]`sudo ./ghostwrite `

    Virtual address:        3f83478000
    Physical address:       1f6805f000

    Value before:                 caaa
    Value after:                  cafe

If instead we compile it with `-march=rv64gc`, omitting the \"v\", then it fails:

`user `[`$`]`gcc -march=rv64gc -o ghostwrite ghostwrite.c `

    ghostwrite.c: Assembler messages:
    ghostwrite.c:58: Error: unrecognized opcode `vsetvli zero,zero,e8,m1', extension `v' or `zve64x' or `zve32x' required
    ghostwrite.c:59: Error: unrecognized opcode `vmv.v.x v0,a0', extension `v' or `zve64x' or `zve32x' required

The second way to mitigate GhostWrite is wholesale, in the kernel.

[KERNEL] **Disable RISCV_ISA_V**

    Platform type  --->
      <n> VECTOR support

The description of the `RISCV_ISA_V` option is \"Say N here if you want to disable all vector related procedure in the kernel.\" Disabling it does *not* affect the ISA string visible in [/proc/cpuinfo], but it does disable the dangerous instructions, even in userspace. With `RISCV_ISA_V=n`, the GhostWrite proof-of-concept will compile (with `-march=rv64gcv`), but fail at runtime:

`user `[`$`]`gcc -march=rv64gcv -o ghostwrite ghostwrite.c `

`user `[`$`]`sudo ./ghostwrite `

    Virtual address:        3fa7f07000
    Physical address:       100da74000

    Value before:                 caaa
    Illegal instruction

### [Security RISCs]

Researchers at CISPA have identified several hardware vulnerabilities that affect the Pioneer Box:

IEEE Symposium on Security and Privacy presentation

Paper

Github repository

I\'ve opened a bug about these: [https://github.com/milkv-pioneer/issues/issues/38](https://github.com/milkv-pioneer/issues/issues/38)

#### [][Cache+Time (new)]

*Cache+Time* exploits branch prediction in combination with the ability to flush the instruction cache using the standard `fence.i` instruction, and possibly the proprietary `icache.iva` instruction. It is related to [Spectre](https://en.wikipedia.org/wiki/Spectre_(security_vulnerability)).

The Pioneer box is vulnerable to this and there are presently no mitigations.

#### [][Flush+Fault (new)]

This is a variant of the usual *Flush+Reload* attack that works even when the instruction and data caches are separate. Both proofs of concept use `fence.i`, but the proprietary `dcache.civa` and `icache.iva` might be usable instead.

The Pioneer is vulnerable to this and there are presently no mitigations.

#### [][CycleDrift (new)]

*CycleDrift* relies on unprivileged access to the `rdcycle` and `rdinstret` instructions. In newer linux kernels, this is mitigated by default:

-   [https://github.com/torvalds/linux/commit/cc4c07c89aada16229084eeb93895c95b7eabaa3](https://github.com/torvalds/linux/commit/cc4c07c89aada16229084eeb93895c95b7eabaa3)

After that patch, the instructions are privileged by default, and can only be made unprivileged with the `perf_user_access` sysctl. There does not seem to be an easy way to do this using the SOPHGO kernel.

#### [][Flush+Flush / Fence+Flush (old)]

This is a known attack that depends on a second \"flush\" operation being faster if the cache is still empty. We mention it only because the standard `fence.i` instruction is *not* vulnerable---it takes the same amount of time either way. The proprietary `dcache.civa` however reintroduces the exploit, because it is unprivileged and has variable timing.

The Pioneer box is vulnerable to this as well, with no mitigation yet.

## [Building the bootloader]

Before we start messing with the boot flow, we should know how to build the bootloader ourselves. The \"bootloader\" consists of several independent projects, most of which have been forked by SOPHGO. Rather than cross-compile them, we can build them on the Pioneer itself. This simplifies things a bit, but we still mostly follow the [envsetup.sh script](https://github.com/sophgo/bootloader-riscv/blob/master/scripts/envsetup.sh) in SOPHGO\'s [bootloader-riscv](https://github.com/sophgo/bootloader-riscv) repository.

**Update**: recent binaries of ZSBL ([zsbl.bin]), OpenSBI ([fw_dynamic.bin]), and [fip.bin] are now available [in one of the SOPHGO repositories](https://github.com/sophgo/edk2-non-osi/tree/devel-sg2042/Silicon/Sophgo/SG2042/Boot).

### [LinuxBoot]

I don\'t even know where to begin with this one. The only way I know to obtain [riscv64_Image] and [initrd.img] is to steal them from the [pre-built OS images provided by SOPHGO](https://github.com/sophgo/sophgo-doc/blob/main/SG2042/HowTo/FAQ.rst), but those are outdated and will not work with an upstream kernel.

It\'s better to avoid this method entirely.

### [EDK2]

This should be your preferred bootloader, since it actually works.

The only trick here is that there are *three* forked SOPHGO repositories that you need to clone, and that all of them have a special branch you need to check out. Their build script doesn\'t mention this!

`user `[`$`]`git clone https://github.com/sophgo/edk2.git edk2.git `

`user `[`$`]`git clone https://github.com/sophgo/edk2-platforms.git edk2-platforms.git `

`user `[`$`]`git clone https://github.com/sophgo/edk2-non-osi.git edk2-non-osi.git `

`user `[`$`]`cd edk2-platforms.git; git checkout devel-sg2042; cd .. `

`user `[`$`]`cd edk2-non-osi.git; git checkout devel-sg2042; cd .. `

`user `[`$`]`cd edk2.git; git checkout devel-sg2042; cd ..`

Now to build:

`user `[`$`]`cd edk2.git `

`user `[`$`]`git submodule sync `

`user `[`$`]`git submodule update --init --recursive `

`user `[`$`]`export PACKAGES_PATH="$(pwd)/../edk2-platforms.git:$(pwd)/../edk2-non-osi.git" `

`user `[`$`]`. edksetup.sh `

`user `[`$`]`make -j64 -C BaseTools `

`user `[`$`]`build -a RISCV64 -t GCC5 -b RELEASE -p Platform/Sophgo/SG2042Pkg/SRA1-20/SRA1-20.dsc`

When all is said and done, you should be in possession of [Build/SRA1-20/RELEASE_GCC5/FV/SRA1-20.fd].

### [zsbl]

There are two tricks that you may need to build the zero-stage boot loader:

1.  Installing [[[sys-apps/dtc]](https://packages.gentoo.org/packages/sys-apps/dtc)[]]. This is required for the build.
2.  Adding `-znotext` to \"LDFLAGS\" by appending `-Wl,-znotext` to `CC`. This avoids a RELRO linking issue.

We also typically use `make V=1` and `make CROSS_COMPILE=""` to ensure that the build is verbose, and that the right toolchain names are used, respectively. In summation,

`user `[`$`]`git clone https://github.com/sophgo/zsbl.git zsbl.git `

`user `[`$`]`cd zsbl.git `

`user `[`$`]`mkdir build `

`user `[`$`]`make V=1 O=build ARCH=riscv sg2042_defconfig `

`user `[`$`]`cd build `

`user `[`$`]`make -j64 V=1 CROSS_COMPILE="" ARCH=riscv CC="gcc -Wl,-znotext"`

### [OpenSBI]

Somewhat recently, SOPHGO have changed the default branch of their repo to the upstream master branch. Be sure to check out the `sg2042-dev` branch before you build it; otherwise, everything will appear to work up until the point where you [reboot and it hangs](https://github.com/sophgo/opensbi/issues/36#issuecomment-2623136490).

`user `[`$`]`git clone https://github.com/sophgo/opensbi.git opensbi.git `

`user `[`$`]`cd opensbi.git `

`user `[`$`]`git checkout sg2042-dev `

`user `[`$`]`make -j64 V=1 PLATFORM_RISCV_ABI=lp64 PLATFORM_RISCV_ISA=rv64gc CROSS_COMPILE= PLATFORM=generic FW_PIC=y`

### [U-Boot]

It looks like SOPHGO has given up on this one. The original git repo has disappeared, and the fork at [https://github.com/sophgo/u-boot-2021.10](https://github.com/sophgo/u-boot-2021.10) doesn\'t support the SG2042. I was never able to get it to boot the newer kernels anyway. Use EDK2 instead.

### [GRUB]

You can use the [[[sys-boot/grub]](https://packages.gentoo.org/packages/sys-boot/grub)[]] from Gentoo. Set up `GRUB_PLATFORMS`,

[FILE] **`/etc/portage/package.use`**

    sys-boot/grub GRUB_PLATFORMS: efi-64

and install it. If you really want to, you can add [[[sys-boot/efibootmgr]](https://packages.gentoo.org/packages/sys-boot/efibootmgr)[]] to [/etc/portage/profile/package.provided](https://wiki.gentoo.org/wiki//etc/portage/profile/package.provided "/etc/portage/profile/package.provided"). It gets pulled in by GRUB, but won\'t work on the Pioneer.

Now, rather than mess with grub-install, what we want to do is build a single EFI image. First we need to create a \"default\" config file that will tell GRUB where to look for [grub.cfg]. If we skip this step, it may not know where to look.

[FILE] **`defaults.cfg`**

    search.fs_uuid <your-disks-uuid> root
    set prefix=($root)'/grub'
    configfile $prefix/grub.cfg

The UUID of your disk can be found under [/dev/disk/by-uuid]. Now we generate the EFI image:

`user `[`$`]`GRUB_MODULES="acpi boot cat configfile disk echo elf exfat ext2 fat fdt file gettext gzio halt hashsum help hexdump keystatus linux lsacpi lsefimmap lsefi lsefisystab lsmmap ls minicmd mmap msdospart normal part_gpt part_msdos probe progress read reboot regexp search_fs_file search_fs_uuid search_label search serial setjmp xzio" `

`user `[`$`]`grub-mkimage -v -o BOOTRISCV64.EFI -O riscv64-efi -p efi -c defaults.cfg $GRUB_MODULES`

(You can probably reduce that list of modules even further if you feel like it.) Now, to \"install\" GRUB, we simply copy [BOOTRISCV64.EFI] to the location where U-Boot or EDK will be expecting it. For U-Boot, it\'s the root of the device, so most likely the first partition on your SD card.

## [Changing the boot flow]

The boot flow can be altered with a configuration file called [conf.ini]. The two methods for supplying it are laid out in a [HowTo by SOPHGO](https://github.com/sophgo/sophgo-doc/blob/main/SG2042/HowTo/Configuration%20Info%20in%20INI%20file.rst).

** Warning**\
The output from EDK2/GRUB and U-Boot are only visible over the serial console. You won\'t see anything on your monitor until Linux boots and initializes the display.

The first is to create and write [conf.ini] to the SPI flash via [/dev/mtd0]. This is the more difficult method for two reasons. First, [/dev/mtd0] is a [Memory Technology Device](http://linux-mtd.infradead.org/doc/general.html), and does not have a normal filesystem that can be mounted somewhere. But more importantly, this is the \"baked in\" configuration file that the box will use if there is no SD card inserted. It\'s probably best not to mess with it right away, so we will focus on the second method.

### [Using an SD card]

Which is, to create and write [conf.ini] to an SD card. The first thing to know is that it\'s not quite as easy as the HowTo suggests. Your SD card needs the following files, at a minimum:

-   [fip.bin] ([downloaded from Github](https://github.com/sophgo/edk2-non-osi/blob/devel-sg2042/Silicon/Sophgo/SG2042/Boot/fip.bin))
-   [zsbl.bin] ([built from ZSBL](#ZSBL), or [downloaded from Github](https://github.com/sophgo/edk2-non-osi/blob/devel-sg2042/Silicon/Sophgo/SG2042/Boot/zsbl.bin))
-   [riscv64/fw_dynamic.bin] ([built from OpenSBI](#OpenSBI), or [downloaded from Github](https://github.com/sophgo/edk2-non-osi/blob/devel-sg2042/Silicon/Sophgo/SG2042/Boot/fw_dynamic.bin))
-   [riscv64/conf.ini] (you write this from scratch)
-   [riscv64/mango-milkv-pioneer.dtb] (a device tree blob, built from zsbl)
-   [riscv64/SRA1-20.fd] ([built from EDK2](#EDK2))
-   [EFI/BOOT/BOOTRISCV64.EFI] ([built with GRUB](#GRUB))

And finally, if you want to put your kernel on the SD card too,

-   [kernel-gentoo-6.19.0+] (the name of the kernel I\'ll be using)
-   [sg2042-milkv-pioneer.dtb] (another device tree blob, built with the kernel)

Yes, there are two separate DTBs: the one that needs to be fed to the bootloader via [riscv64/conf.ini], and the one that needs to be passed to the kernel via GRUB. No, you can\'t use the same one for both; if you try to use the kernel DTB with zsbl, you\'ll get a page fault in EDK2.

#### [GRUB example]

Let\'s switch from the default LinuxBoot process to GRUB, assuming:

1.  You already have an SD card whose first partition has been formatted as FAT32.
2.  You have [built GRUB](#GRUB) and can build a `BOOTRISCV64.EFI` image.
3.  You have [built SRA1-20.fd](#EDK2) from EDK2.

We\'re going to build a new GRUB image, but we have to be careful to point it to the right [grub.cfg]. You have some choices here, but I\'m going to put [grub.cfg] on the SD card along with everything else, so that booting from the card is largely independent of the rest of the system. To do that, refer back to how we built GRUB using a file called [defaults.cfg]. Inside that file, we specify a \"root\" partition by UUID, and in this case, I want to use the UUID of the SD card. Yours will be different, but it can be found the same way:

`user `[`$`]`ls -lh /dev/disk/by-uuid/ `

    total 0
    lrwxrwxrwx 1 root root 15 2024-09-09 15:36 104ad877-cc35-4e61-9e63-0ceea0d353ed -> ../../nvme0n1p3
    lrwxrwxrwx 1 root root 15 2024-09-09 16:06 1E9C-55A8 -> ../../mmcblk1p1
    lrwxrwxrwx 1 root root 15 2024-09-09 15:36 1EE7-06EB -> ../../nvme0n1p1
    lrwxrwxrwx 1 root root 15 2024-09-09 16:06 4b98d180-42f7-4bc1-b25f-2871b610a9a9 -> ../../mmcblk1p2
    lrwxrwxrwx 1 root root 15 2024-09-09 15:36 4d9f57b4-cf22-4c6e-a13f-ead74716b706 -> ../../nvme0n1p4
    lrwxrwxrwx 1 root root 15 2024-09-09 15:36 d9518f6d-f175-4331-83de-cb10ef6d8885 -> ../../nvme0n1p2

I want `1E9C-55A8` because it corresponds to [/dev/mmcblk1p1], the first partition on my SD card. Anyway, put that in your [defaults.cfg] and [build a new BOOTRISCV64.EFI](#GRUB). Once you have it, move it to [EFI/BOOT/BOOTRISCV64.EFI] on your SD card.

Finally, we need the GRUB configuration file, which (thanks to our [defaults.cfg]), we know should live at [grub/grub.cfg] on the SD card:

[FILE] **`grub/grub.cfg`**

    set default=0
    set timeout_style=menu
    set timeout=2

    set debug="linux,loader,mm"
    set term="vt100"
    set pager=1

    menuentry 'Gentoo 6.19.0+'

** Note**\
In this example, I have put the kernel on the SD card, too, to avoid having to locate them inside of GRUB.

The entry above refers to a device tree blob, [/sg2042-milkv-pioneer.dtb], so you should copy that onto the SD card from your (compiled) kernel source tree as well.

Finally, we will need to create a [conf.ini] to tell ZSBL to tell OpenSBI to use [SRA1-20.fd]. This should live at [riscv64/conf.ini] on your SD card:

[FILE] **`riscv64/conf.ini`**

    [sophgo-config]

    [devicetree]
    name = mango-milkv-pioneer.dtb

    [kernel]
    name = SRA1-20.fd

    [eof]

Once again this refers to [mango-milkv-pioneer.dtb] that is built with newer versions of ZSBL, so don\'t forget to put that in the [riscv64] directory on your SD card.

If you are very lucky, you can now reboot the machine, and it will load GRUB and then, after two more seconds, Linux. **Keep in mind that you can\'t see any of this except through a serial console.** To recap, this example requires the following files on your SD card:

-   [fip.bin]
-   [zsbl.bin]
-   [riscv64/fw_dynamic.bin]
-   [riscv64/conf.ini]
-   [riscv64/mango-milkv-pioneer.dtb]
-   [riscv64/SRA1-20.fd]
-   [EFI/BOOT/BOOTRISCV64.EFI]
-   [kernel-gentoo-6.19.0+]
-   [sg2042-milkv-pioneer.dtb]

}}

### [Overwriting the SPI flash]

This process isn\'t for the faint of heart. Proceed at your own risk! There\'s not too much risk if you have a bootable SD card. You should be familiar with [Using an SD card](#Using_an_SD_card) first anyway.

#### [The short version]

There\'s no real filesystem on the SPI flash and thus no file names. What there is, is a convention: ZSBL expects [conf.ini] to live at the very beginning of [/dev/mtd0], and a \"partition table\" to be present at a specific address on [/dev/mtd1]. That partition table is more like a directory list in that it contains information about the rest of the \"files\" on the SPI flash. And how to those \"files\" and the \"partition table\" get there? Well, there is a utility called [gen_spi_flash](https://github.com/sophgo/bootloader-riscv/blob/master/scripts/gen_spi_flash.c) that follows the same convention as ZSBL, and builds you a file called [spi_flash.bin]. That file gets written to [/dev/mtd1] with `flashcp` and then when you reboot, everything is where ZSBL expects it to be. There is an example (but no documentation) of using the script in [envsetup.sh](https://github.com/sophgo/bootloader-riscv/blob/master/scripts/envsetup.sh#L1714) in one of the SOPHGO repos.

#### [The long version]

The SPI flash is accessible via [/dev/mtd0] and [/dev/mtd1]\... sort of. But they\'re not normal block devices, and don\'t contain normal filesystems. So you can\'t just mount them and write files to it. The boot process likewise cannot just read files off of these devices---there is a convention that needs to be followed. So let\'s reverse engineer it. ZSBL is what loads the files, and there are a few that it\'s expecting. What follows is from [plat/sg2042/boot.c] in the ZSBL git repository.

First, there are two flash devices, corresponding to [/dev/mtd0] and [/dev/mtd1]. The driver included with ZSBL knows about both of these:

[FILE] **`include/driver/spi-flash/mango_spif.h`**

    #define FLASH0_BASE     0x7000180000
    #define FLASH1_BASE        0x7002180000

And just like when booting from an SD card, there are a few \"files\" that ZSBL will be looking for:

conf.ini

fw_dynamic.bin

mango.dtb

riscv64_Image

initrd.img

You might be thinking: if the names of the other files can be changed by [conf.ini], then don\'t we have to read [conf.ini] first? And you would be right. ZSBL has a special function `read_conf_and_parse()` that reads [conf.ini] from the first flash device. In the branch for the SPI flash (as opposed to an SD card), we find

[CODE]

    bm_spi_init(FLASH0_BASE);
    bm_spi_flash_read((uint8_t *)boot_file[conf_file_index].addr, 0, sizeof(conf_file) - 1);
    // back to DMMR mode
    mmio_write_32(FLASH0_BASE + REG_SPI_DMMR, 1);

These are low-level commands to read bytes from [/dev/mtd0], and store them at the address pointed to by `boot_file[conf_file_index].addr`. But ultimately, that address is just the address of a buffer called `conf_file`,

[CODE]

    uint8_t conf_file[1024] = ;
    BOOT_FILE boot_file[ID_MAX] = ,
        ...

So it\'s reading 1023 bytes from [/dev/mtd0] into the `conf_file` buffer. So far so good. If you compare what we now know with the [HowTo](https://github.com/sophgo/sophgo-doc/blob/main/SG2042/HowTo/Configuration%20Info%20in%20INI%20file.rst#spi-nor-flash), it makes sense that we can just

`user `[`$`]`flashcp conf.ini /dev/mtd0`

to update/overwrite the configuration.

But once the configuration has been parsed, there are the other \"files\" to worry about, and their names can change depending on the entries in [conf.ini]. This gets weird because there is no filesystem and therefore no file names on the SPI flash! (Remember, we read \"conf.ini\" by reading a fixed number of bytes from a fixed hardware address.)

The function `build_bootfile_info()` is what uses the contents of [conf.ini]. Basically it fills an array, called `boot_file`, with the names and addresses from either [conf.ini] or the defaults:

[FILE] **`include/driver/io/io.h`**

    typedef struct boot_file  BOOT_FILE;

[FILE] **`plat/sg2042/boot.c`**

    BOOT_FILE boot_file[ID_MAX] = ,
            ...
        [ID_DEVICETREE] = ,
    };

Defaults for `.len` and `.offset` are not provided; they depend on the files themselves and need to be read from the \"disk\" at some point. The default addresses are supplied by a header:

[FILE] **`plat/sg2042/include/platform.h`**

    #define OPENSBI_ADDR   0x0
    #define KERNEL_ADDR    0x2000000
    #define RAMFS_ADDR 0x30000000
    #define DEVICETREE_ADDR    0x20000000

And it looks like the default names are right there in `.name`, but they\'re not. The real default names differ on an SD card and on the SPI flash. Here they are:

[CODE]

    static char *img_name_sd[] = ;

    static char *img_name_spi[] = ;

Back in `build_bootfile_info()`, we can now look at a representative example:

[CODE]

    if (sg2042_board_info.config_ini.fw_name == NULL)
        boot_file[ID_OPENSBI].name = imgs[ID_OPENSBI];

When booting from flash, `imgs[ID_OPENSBI]` will refer to \"fw_dynamic.bin\" in `img_name_spi`, so this is checking to see if the configuration file provided a value, and if not, falling back to the default. Okay.

But how are the filenames being used? Remember, no filesystem. This sends us down another rabbit hole, in `read_all_img()`, which is responsible for reading the \"files.\" It uses an I/O abstraction that can be found under `drivers/io` in the ZSBL tree, and if we look at the flash implementation, it\'s doing a few things. First, it initializes the device. The underlying implementation here just calls,

[FILE] **`drivers/io/io_flash.c`**

    int flash_device_init(void)


which is helpful, because it tells us that everything we\'re doing is relative to [/dev/mtd1]. In other words, [conf.ini] is the only thing stored on [/dev/mtd0], and everything else goes on [/dev/mtd1].

After initializing the device, what we ultimately want to do is read a file, and once we get there, that part is simple: it\'s reading a certain amount of bytes from an offset. Namely, it\'s reading the-length-of-the-file bytes from where the file is supposed to start. But we don\'t know those! Which brings us to the intermediate step: we have to obtain some \"file info\" based on a name:

[CODE]

    if (io_dev->func.get_file_info(boot_file, i, &info))

This, in turn, defers to the flash implementation in `flash_device_get_file_info()`, where the real magic happens:

[FILE] **`drivers/io/io_flash.c`**

    int flash_device_get_file_info(BOOT_FILE *boot_file, int id, FILINFO *f_info)


        f_info->fsize = info.size;
        boot_file[id].offset = info.offset;

        pr_debug("load %s image from sf 0x%x to memory 0x%lx size %d\n",
             boot_file[id].name, info.offset, info.lma, info.size);

        return 0;
    }

This is reading a \"partition table\" to search for a file by name. It turns out that the \"partition table\" is just a struct that gets dumped to disk:

[FILE] **`include/driver/spi-flash/mango_spif.h`**

    #define DISK_PART_TABLE_ADDR      0x600000

    struct part_info ;

[FILE] **`driver/spi-flash/mango_spif.c`**

    static int mango_get_part_info(uint32_t addr, struct part_info *info)


        return ret;
    }

    int mango_get_part_info_by_name(uint32_t addr, const char *name, struct part_info *info)
     while (!ret && strcmp(info->name, name));

        return ret;
    }

So after all that, it\'s expecting there to be a \"partition table\" stored at a fixed address, where in reality that just means some struct (containing file metadata) dumped to disk.

Now the problem becomes: if we have a bunch of files and want to put them on [/dev/mtd1], where do we put them, and then how do we generate the \"partition table\" that will let ZSBL find them?

Well, thankfully, SOPHGO have written a utility to do it for us. It\'s called [gen_spi_flash](https://github.com/sophgo/bootloader-riscv/blob/master/scripts/gen_spi_flash.c), and it compiles to a simple CLI program that can generate the flash image for us. Right away, we see that it shares the `DISK_PART_TABLE_ADDR` and `struct part_info` definitions with ZSBL:

[FILE] **`gen_spi_flash.c`**

    #define DISK_PART_TABLE_ADDR  0x600000

    ...

    /* disk partition table */
    struct part_info ;

If we look inside `main()` we see that the program takes (on the CLI) four arguments at a time: a partition name, a file name, an offset, and a load memory address (LMA).

[FILE] **`gen_spi_flash.c`**

    for (i = 0; i < part_num; i++) **

    #define OPENSBI_ADDR   0x0
    #define KERNEL_ADDR    0x2000000
    #define RAMFS_ADDR 0x30000000
    #define DEVICETREE_ADDR    0x20000000

They were used as the defaults in ZSBL, and the [envsetup.sh] script that SOPHGO runs to generate the flash image uses those same values. ([SG2042.fd], like [u-boot.bin], is an alternate \"kernel\" that will be used *instead* of [riscv64_Image], so it\'s OK to load those all into the same address.) Here\'s an excerpt from the SOPHGO script:

`user `[`$`]`dtb_group=$(ls *.dtb | awk '') `

`user `[`$`]`./gen_spi_flash $dtb_group \`

            fw_dynamic.bin fw_dynamic.bin 0x660000 0x00000000 \
            riscv64_Image riscv64_Image 0x6b0000 0x02000000 \
            SG2042.fd SG2042.fd 0x02000000 0x02000000 \
            zsbl.bin zsbl.bin 0x2a00000 0x40000000 \
            initrd.img initrd.img 0x2b00000 0x30000000

** Warning**\
Don\'t use that `ls` command in real life. You only have one DTB. A more explicit command is provided below.

The flash offsets, however, look to be up to you. ZSBL will find them by partition name, so there are only a few constraints:

1.  Leave space at the beginning for two copies of [fip.bin]. Although it doesn\'t appear on the command line, `gen_spi_flash` will store two of them right at the beginning of the output image.
2.  The partition table starts at `DISK_PART_TABLE_ADDR` (0x600000), and takes up whatever the size of a `struct part_info` is. The DTB files are written after that (there\'s a comment in the source to that effect), ignoring the offset you specify. So the actual files should probably start far enough after 0x600000 to leave room for the struct and your device tree blobs.
3.  The LMA of zsbl seems important, because it can\'t be fudged in [conf.ini]. Maybe it\'s hard-coded in the firmware (in [fip.bin])?
4.  Each file should leave enough room for the previous one (ha ha).

Anyway, I hope you\'re familiar with hexadecimal. With that out of the way, here are the steps to make this all work:

1.  Copy all of the files that you want to write to flash into one directory. I\'m going to use [/boot/efi]. You\'ll need [fip.bin], [zsbl.bin], [conf.ini], and anything else referred to by [conf.ini].
2.  Compile gen_spi_flash
3.  Figure out what arguments to pass to `gen_spi_flash`, and in what order
4.  Run it
5.  Write [conf.ini] to [/dev/mtd0] using `flashcp`
6.  Write [spi_flash.bin] to [/dev/mtd1] using `flashcp`
7.  Reboot and pray

We can\'t do a U-Boot example, because [U-Boot doesn\'t support the SPI flash](https://github.com/sophgo/u-boot/issues/8) on the Pioneer yet. So instead we\'ll do [LinuxBoot](#LinuxBoot) and [EDK2/GRUB](#EDK2).

** Note**\
*Neither* of these are buildable at the moment, but if you\'ve made it this far, you\'re probably capable of stealing the necessary files from one of SOPHGO\'s pre-built OS images.

Make a new directory to work in:

`user `[`$`]`mkdir new-firmware `

`user `[`$`]`cd new-firmware`

The first thing we need to do is obtain [fip.bin] from SOPHGO\'s edk2-non-osi repository.

`user `[`$`]`wget https://github.com/sophgo/edk2-non-osi/raw/refs/heads/devel-sg2042/Silicon/Sophgo/SG2042/Boot/fip.bin`

Next we\'ll copy over the files that we decided are necessary from the local repos where we built them.

`user `[`$`]`cp /path/to/zsbl.git/build/arch/riscv/boot/dts/mango-milkv-pioneer.dtb ./ `

`user `[`$`]`cp /path/to/zsbl.git/build/zsbl.bin ./ `

`user `[`$`]`cp /path/to/opensbi.git/build/platform/generic/firmware/fw_dynamic.bin ./ `

`user `[`$`]`cp /path/to/edk2.git/Build/SRA1-20/RELEASE_GCC5/FV/SRA1-20.fd ./ `

`user `[`$`]`cp /path/to/pre-built/riscv64_Image ./ `

`user `[`$`]`cp /path/to/pre-built/initrd.img ./ `

`user `[`$`]`/path/to/gen_spi_flash \`

            mango-milkv-pioneer.dtb mango-milkv-pioneer.dtb 0x601000 0x020000000 \
            fw_dynamic.bin fw_dynamic.bin 0x660000 0x00000000 \
            riscv64_Image riscv64_Image 0x6b0000 0x02000000 \
            SRA1-20.fd SRA1-20.fd 0x02000000 0x02000000 \
            zsbl.bin zsbl.bin 0x2a00000 0x40000000 \
            initrd.img initrd.img 0x2b00000 0x30000000

Create a [conf.ini]:

[FILE] **`conf.ini`**

    [sophgo-config]

    [devicetree]
    name = mango-milkv-pioneer.dtb

    [kernel]
    name = riscv64_Image

    [ramfs]
    name = initrd.img

    [eof]

Make a backup of the existing flash contents:

`user `[`$`]`dd if=/dev/mtd0 of=mtd0-backup.bin `

`user `[`$`]`dd if=/dev/mtd1 of=mtd1-backup.bin`

And finally, `flashcp` the new stuff to the SPI flash:

`user `[`$`]`flashcp conf.ini /dev/mtd0 `

`user `[`$`]`flashcp spi_flash.bin /dev/mtd1`

The time has come: remove your SD card, reboot, and pray.

### [Miscellaneous references]

-   [Pioneer boot process (forum thread)](https://community.milkv.io/t/pioneer-boot-process/1488)
-   [How to build bsp (official how-to)](https://github.com/sophgo/sophgo-doc/blob/main/SG2042/HowTo/How%20to%20build%20SG2042%20bsp.rst)
-   [Source code for generating fip.bin? (Github issue)](https://github.com/sophgo/bootloader-riscv/issues/74)

## [Solved problems]

### [The boot process periodically hangs]

The stock boot process occasionally hangs, although at slightly different places. This happens with both the LinuxBoot flow on the SPI flash, and with the EDK2/GRUB flow on an SD card with [SG2042.fd] obtained from a Fedora image. A few examples of these are included below.

This is \"solved\" because it stopped happening after I rebuilt the bootloader components and switched to U-Boot on an SD card as my primary boot flow. On an SD card, U-Boot seems like the obvious choice for a bootloader anyway. Since the hangs aren\'t predictable, I can\'t say for sure if the LinuxBoot hangs are gone now that I\'ve replaced most of the bootloader components on the flash.

#### [LinuxBoot flow]

An example of LinuxBoot hanging when booting from the SPI flash:

    [    8.339299] usb 1-2.3.2: new low-speed USB device number 6 using xhci_hcd
    [    8.571905] usb 1-2.3.2: New USB device found, idVendor=0c45, idProduct=22bc, bcdDevice= 1.00
    [    8.586162] usb 1-2.3.2: New USB device strings: Mfr=1, Product=2, SerialNumber=0
    [    8.599408] usb 1-2.3.2: Product: Majestouch Convertible3 TKL
    [    8.610911] usb 1-2.3.2: Manufacturer:
    [    8.638602] input:       Majestouch Convertible3 TKL as /devices/platform/4c00000000.pcie/pci1
    [    8.729299] hid-generic 0003:0C45:22BC.0002: input: USB HID v1.00 Keyboard [      Majestouch 0
    [    8.753479] input:       Majestouch Convertible3 TKL Consumer Control as /devices/platform/4c2
    [    8.849360] input:       Majestouch Convertible3 TKL System Control as /devices/platform/4c003
    [    8.877345] hid-generic 0003:0C45:22BC.0003: input: USB HID v1.00 Device [      Majestouch Co1
    [    9.849941] u-root init: error creating mount -t "efivarfs" -o  "efivarfs" "/sys/firmware/efiy
    [   10.026558] ISOFS: Unable to identify CD-ROM format.
    <HANG>

#### [][EDK2/GRUB flow]

Two examples of EDK2/GRUB hanging. The first is more obviously a problem\...

    Emulated images:
                x64 Image 0xBFB4A000-0xBFB61FFF (Entry 0xBFB4EA34)
                x64 Image 0xBFAF1000-0xBFB49FFF (Entry 0xBFB1965C)
                x64 Image 0xBFA98000-0xBFAF0FFF (Entry 0xBFAC065C)
    Wrapped EFI_EVENTs:
                x64 ImageBase 0xBFAF1000 Event BF2F6C18 Fn BFB19A60 Context 0
                x64 ImageBase 0xBFA98000 Event BF244D18 Fn BFAC0A60 Context 0
    !!!! RISCV64 Exception Type - 0000000000000003(EXCEPT_RISCV_BREAKPOINT) !!!!
         t0 = 0x00000000000000003        t1 = 0x000000000BFB95976
         t2 = 0x0000000000000002C        t3 = 0x000000000BFC272A8
         t4 = 0x00000000000000000        t5 = 0x00000000000000002
         t6 = 0x00000000000000002        s0 = 0x000000000047FF5C8
         s1 = 0x00000000000000013        s2 = 0x00000000000000000
         s3 = 0x00000000000000000        s4 = 0x00000000000000000
         s5 = 0x00000000000000000        s6 = 0x00000000000000002
         s7 = 0x00000000000000040        s8 = 0x00000000000004000
         s9 = 0x0000000000004EAC0       s10 = 0x00000000000000000
        s11 = 0x00000000000000000        a0 = 0x00000000000000000
         a1 = 0x0000000000000005A        a2 = 0x00000000000000000
         a3 = 0x0000000000000000A        a4 = 0x00000000000000001
         a5 = 0x00000000000000000        a6 = 0x000000000000000FF
         a7 = 0x00000000000000000      zero = 0x00000000000000000
         ra = 0x000000000BFE100D4        sp = 0x000000000BFC2F220
         gp = 0x00000000000000000        tp = 0x0000000000014E000
       sepc = 0x000000000BFB95A32   sstatus = 0x08000000200006100
      stval = 0x00000000000000000
    <HANG>

whereas in the second, the kernel simply stops loading:

      Booting `Gentoo (Sophgo 6.1.80+ nomod)'

    loader/efi/linux.c:102:linux: UEFI stub kernel:.80  40.64MiB  100%  1.24GiB/s ]
    loader/efi/linux.c:103:linux: PE/COFF header @ 00000040
    loader/efi/linux.c:132:linux: LoadFile2 initrd loading enabled
    loader/efi/linux.c:515:linux: kernel file size: 98123776
    loader/efi/linux.c:517:linux: kernel numpages: 23956
                                [ kernel-sophgo-6.1.80  37.70MiB  92%  13.08GiB/s ]
    <HANG>

### [Box stops powering on]

Unplug the power cord (yes, the physical power cord), wait a few minutes, and try again.

### [Nothing happens when booting from an SD card]

Ensure that you have all of the right files in all of the right places, and that there are no typos in [riscv64/conf.ini]. The first partition must be FAT32. When in doubt, remove [riscv64/conf.ini] from the SD card to see if that was the problem. You should be able to see the SD card being initialized over a serial console, and as an extreme measure, you can try wiping its partition table and rebooting.

Even though the card (obviously) needs to be initialized to read [riscv64/conf.ini] off of its first partition, the boot process hangs (and displays nothing about the SD card) if your [riscv64/conf.ini] or one of the files it needs are messed up.

### [Flaky console keyboard]

After rebooting into Gentoo (using the default LinuxBoot flow), the keyboard is flaky and starts dropping keys and/or sending keys that were not pressed. This happens with the stock Fedora kernel as well as the latest git kernel. Both `showkey` and `evtest` confirm that (only) the correct keystrokes *are* being sent\... but something goes wrong and they don\'t make it to the screen.

The solution? Well, it seems to be a problem with the default firmware stored in flash. If you boot from an [SD card with GRUB on it](#GRUB_Example), the problem disappears. Though it is far more difficult, the problem also disappears if you overwrite the firmware in the SPI flash with newer stuff.

### [No hardware clock]

First, did you buy a CR-1220 battery and put it in the socket? The board doesn\'t come with one. Okay.

After the default boot flow, your clock will be all wrong, because there won\'t be a device corresponding to the hardware clock ([/dev/rtcN]). By all means it looks like there should be one; the device tree contains e.g.

[FILE] **`mango-milkv-pioneer.dts`**

    &i2c0 ;
    };

\...but there just isn\'t. Even after putting a CR-1220 battery in the socket on the motherboard, nothing.

Well, this turns out to be another problem with the default (flash) firmware or device tree, just like the flaky console keyboard. If you boot from GRUB on an SD card, the clock device will appear. In fact, two of them will appear, which creates a new problem: if you are using an initramfs, sometimes you wind up with the wrong one as [/dev/rtc0], and Gentoo (the `hwclock` service) still won\'t know what to do with it. Compare

[FILE] **`/var/log/dmesg (initramfs)`**

    [    3.854973] dracut: Gentoo-2.15
    Starting systemd-udevd version 255
    [    4.749060] rtc-efi rtc-efi.0: registered as rtc0
    [    4.753940] rtc-efi rtc-efi.0: setting system clock to 2024-01-26T13:39:37 UTC (1706276377)
    [    4.795633] gpio-keys soc:gpio-poweroff: there is not valid maps for state default
    [    4.795873] xhci_hcd 0002:c4:00.0: xHCI Host Controller
    [    4.795908] xhci_hcd 0002:c4:00.0: new USB bus registered, assigned bus number 1
    [    4.798080] rtc-ds1307 0-0068: registered as rtc1

with

[FILE] **`/var/log/dmesg (no initramfs)`**

    [   11.426623] rtc-ds1307 0-0068: registered as rtc0
    [   11.432365] rtc-ds1307 0-0068: setting system clock to 2024-08-27T22:56:34 UTC (1724799394)
    [   11.442015] rtc-efi rtc-efi.0: registered as rtc1

If you really want to use an initramfs, you can pass `-f /dev/rtc1` to `hwclock` in [/etc/conf.d/hwclock]. The systemd equivalent is left as an exercise.

### [No sound]

If you still have no sound even after building the right modules into the kernel, maybe you have weird device numbering and need to tell ALSA about it. For example,

`user `[`$`]`aplay -l `

    **** List of PLAYBACK Hardware Devices ****
    card 0: HDMI [HDA ATI HDMI], device 3: HDMI 0 [HDMI 0 *]
      Subdevices: 1/1
      Subdevice #0: subdevice #0

The *only* device I have is `device 3`? ALSA is not expecting this. To tell ALSA to use my (only) device, I had to create the following:

[FILE] **`/etc/asound.conf`**

    pcm.!default

    ctl.!default

Afterwards, I also had to run `alsamixer` from [[[media-sound/alsa-utils]](https://packages.gentoo.org/packages/media-sound/alsa-utils)[]] to unmute the `S/PDIF` source.

### [][Clock skew detected!]

Even with the RTC clock working and set to the correct time, OpenRC likes to tell me that clock skew is detected every time I reboot:

     * WARNING: clock skew detected!
     * Restoring Mixer Levels ...
     [ ok ]

dmesg tells me that the system clock is being set during boot:

[FILE] **`/var/log/dmesg`**

    [Thu Sep 12 12:41:45 2024] [    T1] rtc-ds1307 0-0068: setting system clock to 2024-09-12T16:41:45 UTC (1726159305)

But several of the files under [/run/openrc] that are created very early are being created with the wrong time (system clock appears set close to the epoch). The system time then stays wrong (epoch plus a few seconds) until the udev-trigger service runs, and, I am guessing, the default udev rule that calls `hwclock` finally fixes the time.

I don\'t *really* know what\'s happening here, but it looks like the console output is out of order. I added `printk` statements to the kernel, and I can see that e.g. hwclock and ntpd are starting in the middle of the kernel output. That can\'t be possible if the console output is in order, and *that* means that I can\'t really be sure when the system clock was set.

The current theory is that the console output is ordered incorrectly, and that the RTC clock is probed much later than we want it to be. In any case, based on that assumption and the fact that the `ds1307` is on the `i2c0` in [arch/riscv/boot/dts/sophgo/mango-milkv-pioneer.dts], I\'ve fixed it by compiling both the RTC and I2C drivers into the kernel:

-   `CONFIG_RTC_DS1307=y`
-   `CONFIG_I2C_DESIGNWARE_PLATFORM=y`

\

### [SD card stops working]

Sometimes, after a crash, the machine will stop booting, with nothing being sent to the serial console. This turns out to be an issue with the SD card that can only be diagnosed via the [mainboard console](#Mainboard_console):

    NOTICE:  Booting Trusted Firmware
    NOTICE:  BL1: v2.7(release):83c4f9e3e
    NOTICE:  BL1: Built : 10:39:27, Jul 12 2022
    INFO:    BL1: RAM 0x7010002000 - 0x7010011000
    NOTICE:  SD initializing 100000000Hz
    NOTICE:  sdhci read data timeout
    ASSERT: lib/fatfs/diskio.c:57

I\'ve had luck sticking the SD card in a Windows machine to run chkdsk on the FAT partition, and then putting it back. (There aren\'t any errors on the disk, so who knows why it works.)

The last time this happened, chkdsk didn\'t fix it, and I wound up replacing my SD card with this one for \$10: [Micro Center 32GB microSDHC Card Class 10 Flash Memory Card with Adapter](https://www.microcenter.com/product/658457/micro-center-32gb-microsdhc-card-class-10-flash-memory-card-with-adapter). That fixed the problem straight away.

### [GPU Lockups]

Every few days, the radeon GPU locks up, and goes into a reset loop:

[FILE] **`/var/log/dmesg`**

    Dec 16 00:32:40 [kernel] [529658.719358][T25609] radeon 0000:01:00.0: ring 0 stalled for more than 10240msec
    Dec 16 00:32:40 [kernel] [529658.719379][T25609] radeon 0000:01:00.0: GPU lockup (current fence id 0x00000000004aa63c last fence id 0x00000000004aa65a on ring 0)
    Dec 16 00:32:40 [kernel] [529658.835324][ T1617] radeon 0000:01:00.0: Saved 951 dwords of commands on ring 0.
    Dec 16 00:32:40 [kernel] [529658.835374][ T1617] radeon 0000:01:00.0: GPU softreset: 0x0000000C
    ...
    Dec 16 00:32:40 [kernel] [529658.844958][ T1617] radeon 0000:01:00.0: GPU reset succeeded, trying to resume
    Dec 16 00:32:40 [kernel] [529658.891789][ T1617] [drm] PCIE GART of 1024M enabled (table at 0x0000000000162000).
    Dec 16 00:32:40 [kernel] [529658.891945][ T1617] radeon 0000:01:00.0: WB enabled
    Dec 16 00:32:40 [kernel] [529658.891954][ T1617] radeon 0000:01:00.0: fence driver on ring 0 use gpu addr 0x0000000080000c00
    Dec 16 00:32:40 [kernel] [529658.891961][ T1617] radeon 0000:01:00.0: fence driver on ring 3 use gpu addr 0x0000000080000c0c
    Dec 16 00:32:40 [kernel] [529658.894940][ T1617] radeon 0000:01:00.0: fence driver on ring 5 use gpu addr 0x0000000000072118
    Dec 16 00:32:40 [kernel] [529658.911497][ T1617] [drm] ring test on 0 succeeded in 1 usecs
    Dec 16 00:32:40 [kernel] [529658.911517][ T1617] [drm] ring test on 3 succeeded in 6 usecs
    Dec 16 00:32:40 [kernel] [529659.088655][ T1617] [drm] ring test on 5 succeeded in 2 usecs
    Dec 16 00:32:40 [kernel] [529659.088679][ T1617] [drm] UVD initialized successfully.
    Dec 16 00:32:41 [kernel] [529660.255374][ T1617] [drm:r600_ib_test] *ERROR* radeon: fence wait timed out.
    Dec 16 00:32:41 [kernel] [529660.255416][ T1617] [drm:radeon_ib_ring_tests] *ERROR* radeon: failed testing IB on GFX ring (-110).
    Dec 16 00:32:41 [kernel] [529660.363641][ T1617] radeon 0000:01:00.0: GPU softreset: 0x00000088
    ...
    Dec 16 00:32:41 [kernel] [529660.377768][ T1617] radeon 0000:01:00.0: GPU reset succeeded, trying to resume
    Dec 16 00:32:41 [kernel] [529660.424569][ T1617] [drm] PCIE GART of 1024M enabled (table at 0x0000000000162000).
    Dec 16 00:32:41 [kernel] [529660.424725][ T1617] radeon 0000:01:00.0: WB enabled
    Dec 16 00:32:41 [kernel] [529660.424734][ T1617] radeon 0000:01:00.0: fence driver on ring 0 use gpu addr 0x0000000080000c00
    Dec 16 00:32:41 [kernel] [529660.424742][ T1617] radeon 0000:01:00.0: fence driver on ring 3 use gpu addr 0x0000000080000c0c
    Dec 16 00:32:41 [kernel] [529660.427753][ T1617] radeon 0000:01:00.0: fence driver on ring 5 use gpu addr 0x0000000000072118
    Dec 16 00:32:41 [kernel] [529660.444268][ T1617] [drm] ring test on 0 succeeded in 2 usecs
    Dec 16 00:32:41 [kernel] [529660.444288][ T1617] [drm] ring test on 3 succeeded in 6 usecs
    Dec 16 00:32:41 [kernel] [529660.621441][ T1617] [drm] ring test on 5 succeeded in 2 usecs
    Dec 16 00:32:41 [kernel] [529660.621462][ T1617] [drm] UVD initialized successfully.
    Dec 16 00:32:42 [kernel] [529660.760522][ T1617] [drm] ib test on ring 0 succeeded in 0 usecs
    Dec 16 00:32:42 [kernel] [529660.760574][ T1617] [drm] ib test on ring 3 succeeded in 0 usecs
    Dec 16 00:32:42 [kernel] [529660.911862][ T1617] [drm] ib test on ring 5 succeeded
    Dec 16 00:32:42 [kernel] [529661.025809][ T2371] ------------[ cut here ]------------
    Dec 16 00:32:42 [kernel] [529661.025825][ T2371] WARNING: CPU: 51 PID: 2371 at drivers/gpu/drm/ttm/ttm_bo.c:356 ttm_bo_release+0x350/0x38c
    Dec 16 00:32:42 [kernel] [529661.025853][ T2371] Modules linked in: tun lz4 lz4_compress lz4_decompress zram zsmalloc usbhid nft_ct nf_conntrack nf_defrag_ipv4 evdev nf_tables nfnetlink xhci_pci ahci spi_dw_mmio xhci_hcd gpio_dwapb snd_hda_codec_hdmi libahci spi_dw sophgo_spifmc gpio_generic usbcore ixgbe snd_hda_intel spi_nor snd_intel_dspcfg r8169 libata usb_common snd_hda_codec snd_hda_core mdio snd_pcm snd_timer snd soundcore unix
    Dec 16 00:32:42 [kernel] [529661.025979][ T2371] CPU: 51 PID: 2371 Comm: sway Not tainted 6.1.80+ #71
    Dec 16 00:32:42 [kernel] [529661.025987][ T2371] Hardware name: Sophgo Mango (DT)
    Dec 16 00:32:42 [kernel] [529661.025992][ T2371] epc : ttm_bo_release+0x350/0x38c
    Dec 16 00:32:42 [kernel] [529661.025999][ T2371]  ra : radeon_bo_unref+0x14/0x22
    Dec 16 00:32:42 [kernel] [529661.026014][ T2371] epc : ffffffff803647e0 ra : ffffffff80382ae4 sp : ffffffc80b243cb0
    Dec 16 00:32:42 [kernel] [529661.026020][ T2371]  gp : ffffffff8134afd0 tp : ffffffd90937e800 t0 : ffffffc80b243cf8
    Dec 16 00:32:42 [kernel] [529661.026025][ T2371]  t1 : ffffffff8005faca t2 : 0000000000000000 s0 : ffffffd90239d9e0
    Dec 16 00:32:42 [kernel] [529661.026029][ T2371]  s1 : ffffffd90239d878 a0 : ffffffd90239d9e0 a1 : 0000000000000000
    Dec 16 00:32:42 [kernel] [529661.026034][ T2371]  a2 : fffffff6ff912000 a3 : 0000000000002687 a4 : 0000000000000000
    Dec 16 00:32:42 [kernel] [529661.026039][ T2371]  a5 : 0000000000000001 a6 : 0000000000000000 a7 : 0000000000000000
    Dec 16 00:32:42 [kernel] [529661.026044][ T2371]  s2 : ffffffff813b5158 s3 : ffffffd9020606f0 s4 : ffffffd904439cd8
    Dec 16 00:32:42 [kernel] [529661.026048][ T2371]  s5 : 0000000000000008 s6 : 0000003f996fc410 s7 : 0000000000000007
    Dec 16 00:32:42 [kernel] [529661.026053][ T2371]  s8 : 0000003f9a449558 s9 : 0000003ff2e0c518 s10: 0000003ff2e0ccd8
    Dec 16 00:32:42 [kernel] [529661.026057][ T2371]  s11: 0000003f9a29ded8 t3 : 0000003f9a2c2b38 t4 : 0000000000000005
    Dec 16 00:32:42 [kernel] [529661.026062][ T2371]  t5 : 0000003f96f74b38 t6 : 0000003ff2e0c078
    Dec 16 00:32:42 [kernel] [529661.026066][ T2371] status: 0000000200000120 badaddr: 0000000000000000 cause: 0000000000000003
    Dec 16 00:32:42 [kernel] [529661.026071][ T2371] [<ffffffff803647e0>] ttm_bo_release+0x350/0x38c
    Dec 16 00:32:42 [kernel] [529661.026080][ T2371] [<ffffffff80382ae0>] radeon_bo_unref+0x10/0x22
    Dec 16 00:32:42 [kernel] [529661.026088][ T2371] [<ffffffff80394e0a>] radeon_gem_object_free+0x16/0x3a
    Dec 16 00:32:42 [kernel] [529661.026099][ T2371] [<ffffffff803313dc>] drm_gem_dmabuf_release+0x32/0x4a
    Dec 16 00:32:42 [kernel] [529661.026106][ T2371] [<ffffffff8046db80>] dma_buf_release+0x1e/0x76
    Dec 16 00:32:42 [kernel] [529661.026113][ T2371] [<ffffffff8012f9de>] __dentry_kill+0x116/0x20a
    Dec 16 00:32:42 [kernel] [529661.026122][ T2371] [<ffffffff80119c32>] __fput+0x98/0x19e
    Dec 16 00:32:42 [kernel] [529661.026131][ T2371] [<ffffffff8002601e>] task_work_run+0x8e/0xd4
    Dec 16 00:32:42 [kernel] [529661.026144][ T2371] [<ffffffff80004380>] do_work_pending+0x308/0x3f4
    Dec 16 00:32:42 [kernel] [529661.026153][ T2371] [<ffffffff80119b4a>] fput+0x4c/0x9c
    Dec 16 00:32:42 [kernel] [529661.026160][ T2371] [<ffffffff8000343c>] resume_userspace_slow+0x4/0xa
    Dec 16 00:32:42 [kernel] [529661.026169][ T2371] ---[ end trace 0000000000000000 ]---
    Dec 16 00:32:52 [kernel] [529671.519364][T25609] radeon 0000:01:00.0: ring 0 stalled for more than 10476msec
    Dec 16 00:32:52 [kernel] [529671.519381][T25609] radeon 0000:01:00.0: GPU lockup (current fence id 0x00000000004aa667 last fence id 0x00000000004aa671 on ring 0)
    Dec 16 00:32:52 [kernel] [529671.630627][  T892] radeon 0000:01:00.0: Saved 311 dwords of commands on ring 0.
    Dec 16 00:32:52 [kernel] [529671.630665][  T892] radeon 0000:01:00.0: GPU softreset: 0x00000009
    ...
    Dec 16 00:32:52 [kernel] [529671.643435][  T892] radeon 0000:01:00.0: GPU reset succeeded, trying to resume
    Dec 16 00:32:53 [kernel] [529671.696313][  T892] [drm] PCIE GART of 1024M enabled (table at 0x0000000000162000).
    Dec 16 00:32:53 [kernel] [529671.696474][  T892] radeon 0000:01:00.0: WB enabled
    Dec 16 00:32:53 [kernel] [529671.696484][  T892] radeon 0000:01:00.0: fence driver on ring 0 use gpu addr 0x0000000080000c00
    Dec 16 00:32:53 [kernel] [529671.696491][  T892] radeon 0000:01:00.0: fence driver on ring 3 use gpu addr 0x0000000080000c0c
    Dec 16 00:32:53 [kernel] [529671.700560][  T892] radeon 0000:01:00.0: fence driver on ring 5 use gpu addr 0x0000000000072118
    Dec 16 00:32:53 [kernel] [529671.717162][  T892] [drm] ring test on 0 succeeded in 1 usecs
    Dec 16 00:32:53 [kernel] [529671.717188][  T892] [drm] ring test on 3 succeeded in 7 usecs
    Dec 16 00:32:53 [kernel] [529671.894345][  T892] [drm] ring test on 5 succeeded in 2 usecs
    Dec 16 00:32:53 [kernel] [529671.894363][  T892] [drm] UVD initialized successfully.
    Dec 16 00:32:54 [kernel] [529673.055354][  T892] [drm:r600_ib_test] *ERROR* radeon: fence wait timed out.
    Dec 16 00:32:54 [kernel] [529673.055387][  T892] [drm:radeon_ib_ring_tests] *ERROR* radeon: failed testing IB on GFX ring (-110).
    Dec 16 00:32:54 [kernel] [529673.166998][  T892] radeon 0000:01:00.0: GPU softreset: 0x00000009
    ...
    Dec 16 00:32:54 [kernel] [529673.183406][  T892] radeon 0000:01:00.0: GPU reset succeeded, trying to resume
    Dec 16 00:32:54 [kernel] [529673.238557][  T892] [drm] PCIE GART of 1024M enabled (table at 0x0000000000162000).
    Dec 16 00:32:54 [kernel] [529673.238726][  T892] radeon 0000:01:00.0: WB enabled
    Dec 16 00:32:54 [kernel] [529673.238736][  T892] radeon 0000:01:00.0: fence driver on ring 0 use gpu addr 0x0000000080000c00
    Dec 16 00:32:54 [kernel] [529673.238745][  T892] radeon 0000:01:00.0: fence driver on ring 3 use gpu addr 0x0000000080000c0c
    Dec 16 00:32:54 [kernel] [529673.242963][  T892] radeon 0000:01:00.0: fence driver on ring 5 use gpu addr 0x0000000000072118
    Dec 16 00:32:54 [kernel] [529673.259656][  T892] [drm] ring test on 0 succeeded in 1 usecs
    Dec 16 00:32:54 [kernel] [529673.259682][  T892] [drm] ring test on 3 succeeded in 7 usecs
    Dec 16 00:32:54 [kernel] [529673.436868][  T892] [drm] ring test on 5 succeeded in 2 usecs
    Dec 16 00:32:54 [kernel] [529673.436891][  T892] [drm] UVD initialized successfully.
    Dec 16 00:32:54 [kernel] [529673.576081][  T892] [drm] ib test on ring 0 succeeded in 0 usecs
    Dec 16 00:32:54 [kernel] [529673.576136][  T892] [drm] ib test on ring 3 succeeded in 0 usecs
    Dec 16 00:32:55 [kernel] [529673.727540][  T892] [drm] ib test on ring 5 succeeded

This turned out to be a webkit-gtk problem, and not a hardware/kernel issue. Newer versions of webkit-gtk no longer build on risc-v, \"solving\" this. (Firefox ESR should work instead.)

## [Unsolved problems]

### [][USB keyboard/mouse stop working]

I thought I had this fixed, but I don\'t. Sometimes after rebooting, the keyboard and/or mouse will be dead. Usually unplugging them and plugging them back in again solves the issue. This is what dmesg shows:

`user `[`$`]`dmesg -T | grep -i USB `

    [Mon Oct 14 09:03:31 2024] [    T1] __power_supply_register: Expected proper parent device for 'test_usb'
    [Mon Oct 14 09:03:34 2024] [  T859] usbcore: registered new interface driver usbfs
    [Mon Oct 14 09:03:34 2024] [  T859] usbcore: registered new interface driver hub
    [Mon Oct 14 09:03:34 2024] [  T859] usbcore: registered new device driver usb
    [Mon Oct 14 09:03:34 2024] [  T850] xhci_hcd 0002:c4:00.0: new USB bus registered, assigned bus number 1
    [Mon Oct 14 09:03:34 2024] [  T850] xhci_hcd 0002:c4:00.0: new USB bus registered, assigned bus number 2
    [Mon Oct 14 09:03:34 2024] [  T850] xhci_hcd 0002:c4:00.0: Host supports USB 3.1 Enhanced SuperSpeed
    [Mon Oct 14 09:03:34 2024] [  T850] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 6.01
    [Mon Oct 14 09:03:34 2024] [  T850] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
    [Mon Oct 14 09:03:34 2024] [  T850] usb usb1: Product: xHCI Host Controller
    [Mon Oct 14 09:03:34 2024] [  T850] usb usb1: Manufacturer: Linux 6.1.80+ xhci-hcd
    [Mon Oct 14 09:03:34 2024] [  T850] usb usb1: SerialNumber: 0002:c4:00.0
    [Mon Oct 14 09:03:34 2024] [  T850] hub 1-0:1.0: USB hub found
    [Mon Oct 14 09:03:34 2024] [  T850] usb usb2: We don't know the algorithms for LPM for this host, disabling LPM.
    [Mon Oct 14 09:03:34 2024] [  T850] usb usb2: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 6.01
    [Mon Oct 14 09:03:34 2024] [  T850] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
    [Mon Oct 14 09:03:34 2024] [  T850] usb usb2: Product: xHCI Host Controller
    [Mon Oct 14 09:03:34 2024] [  T850] usb usb2: Manufacturer: Linux 6.1.80+ xhci-hcd
    [Mon Oct 14 09:03:34 2024] [  T850] usb usb2: SerialNumber: 0002:c4:00.0
    [Mon Oct 14 09:03:34 2024] [  T850] hub 2-0:1.0: USB hub found
    [Mon Oct 14 09:03:34 2024] [  T850] xhci_hcd 0002:c6:00.0: new USB bus registered, assigned bus number 3
    [Mon Oct 14 09:03:34 2024] [  T850] xhci_hcd 0002:c6:00.0: new USB bus registered, assigned bus number 4
    [Mon Oct 14 09:03:34 2024] [  T850] xhci_hcd 0002:c6:00.0: Host supports USB 3.0 SuperSpeed
    [Mon Oct 14 09:03:34 2024] [  T850] usb usb3: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 6.01
    [Mon Oct 14 09:03:34 2024] [  T850] usb usb3: New USB device strings: Mfr=3, Product=2, SerialNumber=1
    [Mon Oct 14 09:03:34 2024] [  T850] usb usb3: Product: xHCI Host Controller
    [Mon Oct 14 09:03:34 2024] [  T850] usb usb3: Manufacturer: Linux 6.1.80+ xhci-hcd
    [Mon Oct 14 09:03:34 2024] [  T850] usb usb3: SerialNumber: 0002:c6:00.0
    [Mon Oct 14 09:03:34 2024] [  T850] hub 3-0:1.0: USB hub found
    [Mon Oct 14 09:03:34 2024] [  T850] usb usb4: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 6.01
    [Mon Oct 14 09:03:34 2024] [  T850] usb usb4: New USB device strings: Mfr=3, Product=2, SerialNumber=1
    [Mon Oct 14 09:03:34 2024] [  T850] usb usb4: Product: xHCI Host Controller
    [Mon Oct 14 09:03:34 2024] [  T850] usb usb4: Manufacturer: Linux 6.1.80+ xhci-hcd
    [Mon Oct 14 09:03:34 2024] [  T850] usb usb4: SerialNumber: 0002:c6:00.0
    [Mon Oct 14 09:03:34 2024] [  T850] hub 4-0:1.0: USB hub found
    [Mon Oct 14 09:03:34 2024] [  T273] usb 1-1: new high-speed USB device number 2 using xhci_hcd
    [Mon Oct 14 09:03:34 2024] [  T981] usb 3-1: new high-speed USB device number 2 using xhci_hcd
    [Mon Oct 14 09:03:34 2024] [  T273] usb 1-1: device descriptor read/64, error -71
    [Mon Oct 14 09:03:34 2024] [  T981] usb 3-1: New USB device found, idVendor=2109, idProduct=3431, bcdDevice= 4.20
    [Mon Oct 14 09:03:34 2024] [  T981] usb 3-1: New USB device strings: Mfr=0, Product=1, SerialNumber=0
    [Mon Oct 14 09:03:34 2024] [  T981] usb 3-1: Product: USB2.0 Hub
    [Mon Oct 14 09:03:34 2024] [  T981] hub 3-1:1.0: USB hub found
    [Mon Oct 14 09:03:34 2024] [  T273] usb 1-1: device descriptor read/64, error -71
    [Mon Oct 14 09:03:35 2024] [  T273] usb 1-1: new high-speed USB device number 3 using xhci_hcd
    [Mon Oct 14 09:03:35 2024] [  T273] usb 1-1: device descriptor read/64, error -71
    [Mon Oct 14 09:03:35 2024] [  T273] usb 1-1: device descriptor read/64, error -71
    [Mon Oct 14 09:03:35 2024] [  T273] usb usb1-port1: attempt power cycle
    [Mon Oct 14 09:03:36 2024] [ T1047] usb 2-1: new SuperSpeed USB device number 2 using xhci_hcd
    [Mon Oct 14 09:03:36 2024] [ T1047] usb 2-1: device descriptor read/8, error -71
    [Mon Oct 14 09:03:36 2024] [ T1047] usb 2-1: new SuperSpeed USB device number 2 using xhci_hcd
    [Mon Oct 14 09:03:36 2024] [ T1047] usb 2-1: device descriptor read/8, error -71
    [Mon Oct 14 09:03:36 2024] [ T1047] usb 2-1: new SuperSpeed USB device number 3 using xhci_hcd
    [Mon Oct 14 09:03:36 2024] [ T1047] usb 2-1: device descriptor read/8, error -71
    [Mon Oct 14 09:03:36 2024] [ T1047] usb 2-1: new SuperSpeed USB device number 3 using xhci_hcd
    [Mon Oct 14 09:03:36 2024] [ T1047] usb 2-1: device descriptor read/8, error -71
    [Mon Oct 14 09:03:36 2024] [ T1047] usb usb2-port1: attempt power cycle
    [Mon Oct 14 09:03:37 2024] [  T273] usb 1-1: new high-speed USB device number 4 using xhci_hcd
    [Mon Oct 14 09:03:37 2024] [  T273] usb 1-1: device descriptor read/8, error -71
    [Mon Oct 14 09:03:37 2024] [  T273] usb 1-1: device descriptor read/8, error -71
    [Mon Oct 14 09:03:37 2024] [  T273] usb 1-1: new high-speed USB device number 5 using xhci_hcd
    [Mon Oct 14 09:03:37 2024] [  T273] usb 1-1: device descriptor read/8, error -71
    [Mon Oct 14 09:03:38 2024] [  T273] usb 1-1: device descriptor read/8, error -71
    [Mon Oct 14 09:03:38 2024] [  T273] usb usb1-port1: unable to enumerate USB device
    [Mon Oct 14 09:03:38 2024] [ T1047] usb 2-1: new SuperSpeed USB device number 4 using xhci_hcd
    [Mon Oct 14 09:03:38 2024] [ T1047] usb 2-1: device descriptor read/8, error -71
    [Mon Oct 14 09:03:38 2024] [ T1047] usb 2-1: new SuperSpeed USB device number 4 using xhci_hcd
    [Mon Oct 14 09:03:38 2024] [ T1047] usb 2-1: device descriptor read/8, error -71
    [Mon Oct 14 09:03:38 2024] [ T1047] usb 2-1: new SuperSpeed USB device number 5 using xhci_hcd
    [Mon Oct 14 09:03:38 2024] [ T1047] usb 2-1: device descriptor read/8, error -71
    [Mon Oct 14 09:03:38 2024] [ T1047] usb 2-1: new SuperSpeed USB device number 5 using xhci_hcd
    [Mon Oct 14 09:03:39 2024] [ T1047] usb 2-1: device descriptor read/8, error -71
    [Mon Oct 14 09:03:39 2024] [ T1047] usb usb2-port1: unable to enumerate USB device
    [Mon Oct 14 09:03:39 2024] [  T273] usb 1-2: new high-speed USB device number 6 using xhci_hcd
    [Mon Oct 14 09:03:39 2024] [  T273] usb 1-2: device descriptor read/64, error -71
    [Mon Oct 14 09:03:39 2024] [  T273] usb 1-2: device descriptor read/64, error -71
    [Mon Oct 14 09:03:40 2024] [  T273] usb 1-2: new high-speed USB device number 7 using xhci_hcd
    [Mon Oct 14 09:03:40 2024] [  T273] usb 1-2: device descriptor read/64, error -71
    [Mon Oct 14 09:03:40 2024] [  T273] usb 1-2: device descriptor read/64, error -71
    [Mon Oct 14 09:03:40 2024] [  T273] usb usb1-port2: attempt power cycle
    [Mon Oct 14 09:03:40 2024] [ T1047] usb 2-2: new SuperSpeed USB device number 6 using xhci_hcd
    [Mon Oct 14 09:03:40 2024] [ T1047] usb 2-2: device descriptor read/8, error -71
    [Mon Oct 14 09:03:40 2024] [ T1047] usb 2-2: new SuperSpeed USB device number 6 using xhci_hcd
    [Mon Oct 14 09:03:40 2024] [ T1047] usb 2-2: device descriptor read/8, error -71
    [Mon Oct 14 09:03:41 2024] [ T1047] usb 2-2: new SuperSpeed USB device number 7 using xhci_hcd
    [Mon Oct 14 09:03:41 2024] [ T1047] usb 2-2: device descriptor read/8, error -71
    [Mon Oct 14 09:03:41 2024] [ T1047] usb 2-2: new SuperSpeed USB device number 7 using xhci_hcd
    [Mon Oct 14 09:03:41 2024] [ T1047] usb 2-2: device descriptor read/8, error -71
    [Mon Oct 14 09:03:41 2024] [ T1047] usb usb2-port2: attempt power cycle
    [Mon Oct 14 09:03:42 2024] [  T273] usb 1-2: new high-speed USB device number 8 using xhci_hcd
    [Mon Oct 14 09:03:42 2024] [  T273] usb 1-2: device descriptor read/8, error -71
    [Mon Oct 14 09:03:42 2024] [  T273] usb 1-2: device descriptor read/8, error -71
    [Mon Oct 14 09:03:42 2024] [  T273] usb 1-2: new high-speed USB device number 9 using xhci_hcd
    [Mon Oct 14 09:03:42 2024] [  T273] usb 1-2: device descriptor read/8, error -71
    [Mon Oct 14 09:03:42 2024] [  T273] usb 1-2: device descriptor read/8, error -71
    [Mon Oct 14 09:03:43 2024] [  T273] usb usb1-port2: unable to enumerate USB device
    [Mon Oct 14 09:03:43 2024] [ T1047] usb 2-2: new SuperSpeed USB device number 8 using xhci_hcd
    [Mon Oct 14 09:03:43 2024] [ T1047] usb 2-2: device descriptor read/8, error -71
    [Mon Oct 14 09:03:43 2024] [ T1047] usb 2-2: new SuperSpeed USB device number 8 using xhci_hcd
    [Mon Oct 14 09:03:43 2024] [ T1047] usb 2-2: device descriptor read/8, error -71
    [Mon Oct 14 09:03:43 2024] [ T1047] usb 2-2: new SuperSpeed USB device number 9 using xhci_hcd
    [Mon Oct 14 09:03:43 2024] [ T1047] usb 2-2: device descriptor read/8, error -71
    [Mon Oct 14 09:03:43 2024] [ T1047] usb 2-2: new SuperSpeed USB device number 9 using xhci_hcd
    [Mon Oct 14 09:03:43 2024] [ T1047] usb 2-2: device descriptor read/8, error -71
    [Mon Oct 14 09:03:44 2024] [ T1047] usb usb2-port2: unable to enumerate USB device

### [NVMe is flaky]

The boot often hangs while waiting for the NVMe. It usually succeeds after a while, but it holds up the boot process:

[FILE] **`/var/log/dmesg`**

    [Sun Sep  1 19:13:30 2024] [  T423] nvme nvme0: I/O 22 QID 0 timeout, completion polled
    [Sun Sep  1 19:13:30 2024] [    T9] nvme nvme0: 1/0/0 default/read/poll queues
    [Sun Sep  1 19:13:30 2024] [  T419]  nvme0n1: p1 p2 p3 p4

and occasionally, it does fail, and the boot is stalled indefinitely:

[FILE] **`/var/log/dmesg`**

    [   68.600873][  T389] nvme nvme0: I/O 14 QID 0 timeout, disable controller
    [   68.712860][  T349] nvme nvme0: Removing after probe failure status: -4
    [   68.728785][    T1] Waiting for root device /dev/nvme0n1p4...

The NVMe just seems generally flaky, even after booting:

[FILE] **`/var/log/dmesg`**

    Sep 12 12:36:45 [kernel] [  150.539498][ T1018] nvme nvme0: I/O 335 (I/O Cmd) QID 1 timeout, aborting
    Sep 12 12:36:45 [kernel] [  150.539543][ T1018] nvme nvme0: I/O 866 (I/O Cmd) QID 1 timeout, aborting
    Sep 12 12:36:45 [kernel] [  151.371484][ T1018] nvme nvme0: I/O 441 (I/O Cmd) QID 1 timeout, aborting
    Sep 12 12:36:45 [kernel] [  153.538882][   C52] nvme nvme0: Abort status: 0x0
    Sep 12 12:36:45 [kernel] [  156.538909][   C52] nvme nvme0: Abort status: 0x0
    Sep 12 12:36:48 [kernel] [  159.538940][   C52] nvme nvme0: Abort status: 0x0
    Sep 12 12:37:53 [kernel] [  193.547498][  T415] nvme nvme0: I/O 864 (I/O Cmd) QID 1 timeout, aborting
    Sep 12 12:37:53 [kernel] [  194.635484][  T415] nvme nvme0: I/O 447 (I/O Cmd) QID 1 timeout, aborting
    Sep 12 12:37:53 [kernel] [  196.546797][   C40] nvme nvme0: Abort status: 0x0
    Sep 12 12:37:53 [kernel] [  199.546814][   C40] nvme nvme0: Abort status: 0x0
    Sep 12 12:37:53 [kernel] [  224.267492][  T415] nvme nvme0: I/O 864 QID 1 timeout, reset controller
    Sep 12 12:37:53 [kernel] [  224.307642][   C18] nvme0n1: I/O Cmd(0x2) @ LBA 95243456, 104 blocks, I/O Error (sct 0x3 / sc 0x71)
    Sep 12 12:37:53 [kernel] [  224.307689][   C18] I/O error, dev nvme0n1, sector 95243456 op 0x0:(READ) flags 0x80700 phys_seg 13 prio class 2
    Sep 12 12:37:53 [kernel] [  224.327795][ T1082] nvme nvme0: 1/0/0 default/read/poll queues
    Sep 12 12:38:54 [kernel] [  285.707542][  T415] nvme nvme0: I/O 87 QID 1 timeout, completion polled