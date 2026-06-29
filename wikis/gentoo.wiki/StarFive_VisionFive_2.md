**Resources**

[[]][Home](https://doc-en.rvspace.org/Doc_Center/visionfive_2.html)

[[]][[#gentoo-riscv](ircs://irc.libera.chat/#gentoo-riscv)] ([[webchat](https://web.libera.chat/#gentoo-riscv)])

[[]][starfive-tech/VisionFive2](https://github.com/starfive-tech/VisionFive2)

[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

This page describes several methods for installing Gentoo on the StarFive VisionFive 2.

## Contents

-   [[1] [Introduction]](#Introduction)
    -   [[1.1] [System build methods]](#System_build_methods)
    -   [[1.2] [Hardware]](#Hardware)
-   [[2] [Boot sequence]](#Boot_sequence)
    -   [[2.1] [Boot ROM]](#Boot_ROM)
    -   [[2.2] [Seondary Program Loader]](#Seondary_Program_Loader)
    -   [[2.3] [Bootloader]](#Bootloader)
-   [[3] [First start]](#First_start)
    -   [[3.1] [Serial connection]](#Serial_connection)
    -   [[3.2] [Powering up]](#Powering_up)
-   [[4] [Prerequisites]](#Prerequisites)
    -   [[4.1] [Preparing the crossdev environment]](#Preparing_the_crossdev_environment)
    -   [[4.2] [Optional: Configure QEMU-user and binfmt]](#Optional:_Configure_QEMU-user_and_binfmt)
        -   [[4.2.1] [Configure riscv64 QEMU targets]](#Configure_riscv64_QEMU_targets)
        -   [[4.2.2] [Emerge QEMU]](#Emerge_QEMU)
        -   [[4.2.3] [Start the qemu-binfmt service]](#Start_the_qemu-binfmt_service)
            -   [[4.2.3.1] [Openrc]](#Openrc)
            -   [[4.2.3.2] [Manual]](#Manual)
        -   [[4.2.4] [Confirming binfmt registration]](#Confirming_binfmt_registration)
        -   [[4.2.5] [Copying the interpreter binary]](#Copying_the_interpreter_binary)
        -   [[4.2.6] [Activating the user chroot]](#Activating_the_user_chroot)
    -   [[4.3] [Environment variables and initial setup]](#Environment_variables_and_initial_setup)
-   [[5] [Updating the bootloader]](#Updating_the_bootloader)
    -   [[5.1] [Building OpenSBI]](#Building_OpenSBI)
    -   [[5.2] [Building U-Boot]](#Building_U-Boot)
    -   [[5.3] [Updating U-Boot]](#Updating_U-Boot)
        -   [[5.3.1] [Updating from SD]](#Updating_from_SD)
            -   [[5.3.1.1] [Initialize SPI flash]](#Initialize_SPI_flash)
            -   [[5.3.1.2] [Read SD]](#Read_SD)
            -   [[5.3.1.3] [Flashing the firmware]](#Flashing_the_firmware)
        -   [[5.3.2] [UART method]](#UART_method)
-   [[6] [Build a system image]](#Build_a_system_image)
    -   [[6.1] [Download an existing RISC-V stage 3]](#Download_an_existing_RISC-V_stage_3)
    -   [[6.2] [Create the root filesystem]](#Create_the_root_filesystem)
        -   [[6.2.1] [Extract and prepare the pre-built stage 3 archive]](#Extract_and_prepare_the_pre-built_stage_3_archive)
        -   [[6.2.2] [Refresh the root filesystem]](#Refresh_the_root_filesystem)
        -   [[6.2.3] [Set the system profile for the target environment]](#Set_the_system_profile_for_the_target_environment)
        -   [[6.2.4] [Prepare the RISC-V root filesystem for chrooting]](#Prepare_the_RISC-V_root_filesystem_for_chrooting)
        -   [[6.2.5] [Customize and configure the RISC-V stage3]](#Customize_and_configure_the_RISC-V_stage3)
    -   [[6.3] [Build the kernel]](#Build_the_kernel)
    -   [[6.4] [Bootloader considerations]](#Bootloader_considerations)
-   [[7] [Imaging the device]](#Imaging_the_device)
    -   [[7.1] [microSD Card/eMMC]](#microSD_Card.2FeMMC)
        -   [[7.1.1] [Preparing the microSD Card]](#Preparing_the_microSD_Card)
        -   [[7.1.2] [Write the SPL and U-Boot]](#Write_the_SPL_and_U-Boot)
        -   [[7.1.3] [Incorporate the root filesystem to the media image]](#Incorporate_the_root_filesystem_to_the_media_image)
        -   [[7.1.4] [Transfer the image to the microSD card]](#Transfer_the_image_to_the_microSD_card)
    -   [[7.2] [Booting the device]](#Booting_the_device)
        -   [[7.2.1] [microSD Card]](#microSD_Card)
        -   [[7.2.2] [eMMC]](#eMMC)
            -   [[7.2.2.1] [From the SD Card to the eMMC card]](#From_the_SD_Card_to_the_eMMC_card)
            -   [[7.2.2.2] [From the host to the eMMC card]](#From_the_host_to_the_eMMC_card)
        -   [[7.2.3] [Back in U-Boot shell]](#Back_in_U-Boot_shell)
        -   [[7.2.4] [Flip the switch!]](#Flip_the_switch.21)
-   [[8] [Troubleshooting]](#Troubleshooting)
    -   [[8.1] [Kernel won\'t boot]](#Kernel_won.27t_boot)
    -   [[8.2] [SPI issues / First aid kit]](#SPI_issues_.2F_First_aid_kit)
    -   [[8.3] [init\[1\]: unhandled signal 4 code 0x1 at (...) in ld-linux-riscv64-lp64d.so.1]](#init.5B1.5D:_unhandled_signal_4_code_0x1_at_.28.E2.80.A6.29_in_ld-linux-riscv64-lp64d.so.1)
    -   [[8.4] [Repetitive NVMe QID timouts / reset controller]](#Repetitive_NVMe_QID_timouts_.2F_reset_controller)
-   [[9] [Useful notes]](#Useful_notes)
    -   [[9.1] [Musl]](#Musl)
    -   [[9.2] [Faster installation]](#Faster_installation)
    -   [[9.3] [make.conf]](#make.conf)
    -   [[9.4] [Clearing the U-Boot environment configuration]](#Clearing_the_U-Boot_environment_configuration)
-   [[10] [See also]](#See_also)
-   [[11] [External resources]](#External_resources)

## [Introduction]

This article is intended to supplement the [Embedded Handbook](https://wiki.gentoo.org/wiki/Embedded_Handbook "Embedded Handbook").

### [System build methods]

There are several different ways to approach building the system image (root filesystem). This article will try to incorporate two of them:

-   Utilizing a [Crossdev](https://wiki.gentoo.org/wiki/Crossdev "Crossdev") environment
-   Using a chroot to build packages with [QEMU Userspace emulation](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Compiling_with_QEMU_user_chroot "Embedded Handbook/General/Compiling with QEMU user chroot").

### [Hardware]

For a detailed overview of the StarFive hardware, please visit [StarFive_VisionFive_2/Hardware](https://wiki.gentoo.org/wiki/StarFive_VisionFive_2/Hardware "StarFive VisionFive 2/Hardware")

A JH7110 SoC block diagram is available at: [SoC block diagram](https://doc-en.rvspace.org/JH7110/Datasheet/JH7110_DS/c_block_diagram.html)

## [Boot sequence]

### [Boot ROM]

The VisionFive 2 uses the **JH7110 SOC**, which has a write-only *BootROM* (**BROM**) built in. At power on, the configuration of the two-switch RGPIO header determines which storage device will used to load the *Secondary Program Loader* (**SPL**):

  -------------------------------------- --------- ---------
  Option                                 RGPIO_0   RGPIO_1
  Onboard QSPI Flash (factory setting)   Low       Low
  SDIO3.0 (microSD card)                 High      Low
  eMMC                                   Low       High
  UART                                   High      High
  -------------------------------------- --------- ---------

[![](/images/thumb/5/55/Starfive_Visionfive_2_boot_selector_DIP_switch_states.png/300px-Starfive_Visionfive_2_boot_selector_DIP_switch_states.png)](https://wiki.gentoo.org/wiki/File:Starfive_Visionfive_2_boot_selector_DIP_switch_states.png)

[](https://wiki.gentoo.org/wiki/File:Starfive_Visionfive_2_boot_selector_DIP_switch_states.png "Enlarge")

Low/High states vs switch position\
RGPIO_0 = number 2 on the left\
RGPIO_1 = number 1 on the left (just underneath the GPIO header)

### [Seondary Program Loader]

If the BootROM is able to load the **SPL** (*Secondary Program Loader*) on the selected storage, it will perform basic operations such as RAM initialization, then launch load the Bootloader.

The SPL is loaded from the first partition with the GUID type code of `2E54B353-1271-4842-806F-E436D6AF6985` (HiFive BBL), by default U-Boot will attempt to load the Bootloader (FIT image) from partition 2. While not required, the recommended GUID type code for the bootloader partition is `BC13C2FF-59E6-4262-A352-B275FD6F7172`.

** Note**\
The SPL itself is typically based on U-Boot, which is used to load the main U-Boot bootloader/payload.

### [Bootloader]

The bootlader, typically, U-Boot with [OpenSBI](https://github.com/riscv-software-src/opensbi) and bundled **DTB**s (*Device Tree Blob*s) packed into a **FIT** (*Flat Image Tree*).

Finally, U-Boot is used to load and execute the kernel and/or initramfs to start the OS.

** Tip**\
The partition used by the SPL is defined by `CONFIG_SYS_MMCSD_RAW_MODE_U_BOOT_PARTITION=0x2` when building U-Boot

** Note**\
The **FIT** image (`u-boot.itb`) generally contains multiple DTBs for compatibility and can be inspected from the U-Boot build directory with with:

`user `[`$`]`./tools/dumpimage -l u-boot.itb`

## [First start]

Out of the box, the board\'s SPI flash is preloaded with boot code. Before doing anything, it\'s worth checking that this works. This is accomplished using the UART (serial) interface, as the HDMI interface is not initialized without an OS.

### [Serial connection]

UART is accessible via the pins 6 (GND), 8 (TX) and 10 (RX), similar to most Raspberry PIs.

  --------------------------------------- --------------------
  StarFive VisionFive 2 (1.3B) GPIO pin   Serial adapter pin
  6 (Ground)                              Ground
  8 (TX)                                  RX
  10 (RX)                                 TX
  --------------------------------------- --------------------

Illustration for a 1.3B board revision with a connected USB serial adapter (from left to right its pins are GND - black wire, RXD - blue wire, TXD - violet wire, 3.3V + VCC - yellow jumper, 5V - not connected):

[![Connecting the StarFive VisionFive 2 (rev. 1.3B) to an USB serial adapter](/images/3/34/Star5_v2_serial_connection.jpg)](https://wiki.gentoo.org/wiki/File:Star5_v2_serial_connection.jpg "Connecting the StarFive VisionFive 2 (rev. 1.3B) to an USB serial adapter")

** Note**\
Unless the serial adapter is labeled backwards, the RX pin on one end should be connected to the TX pin on the other.

** Tip**\
For extended debug sessions, using a **JST-XH** connection is preferred to dupont cables.

** Warning**\
GPIO pins on the VisionFive 2 can only tolerate 3.3v. If the serial adapter uses 5v for uart data lines, it could damage the board. Some, but not all serial adapters support voltage level adjustments by shorting VCC to 3.3v

Once physically connected, a serial communication program which can handle a serial port connection and transfer files over X-Modem or Y-Modem protocols like [[[net-dialup/minicom]](https://packages.gentoo.org/packages/net-dialup/minicom)[]] must be installed:

`root `[`#`]`emerge --ask net-dialup/minicom`

The serial port connection parameters should be set as being:

-   Speed: 115200 bps
-   Data: 8 bits
-   Parity: None
-   Stop bits: 1 bit
-   No control flow (hardware and software)

Using [minicom], this configuration cab be specified for device [/dev/ttyUSB0] using:

`user `[`$`]`minicom -D /dev/ttyUSB0 -b 115200`

Using picocom:

`user `[`$`]`picocom /dev/ttyUSB0 -b 115200`

### [Powering up]

As the board\'s QSPI flash already contains a firmware (preloaded at factory), it is possible to use the board when unboxing it. QSPI flash is too small to contain a full-fledged OS nevertheless it is more than enough to contain an [OpenSBI](https://riscv.org/wp-content/uploads/2019/06/13.30-RISCV_OpenSBI_Deep_Dive_v5.pdf)/U-Boot environment (comparable to OpenBOOT for SPARC machines users).

With the serial connection setup in Minicom and the serial cable connected to the StarFive VisionFive 2 UART pins, powering the board up should lead to the following display in Minicom:

[`U-Boot SPL 2021.10 (Sep 28 2024 - 01:14:56 +0800)`]` `

    LPDDR4: 8G version: g8ad50857.
    Trying to boot from SPI

    OpenSBI v1.2
       ____                    _____ ____ _____
      / __ \                  / ____|  _ \_   _|
     | |  | |_ __   ___ _ __ | (___ | |_) || |
     | |  | | '_ \ / _ \ '_ \ \___ \|  _ < | |
     | |__| | |_) |  __/ | | |____) | |_) || |_
      \____/| .__/ \___|_| |_|_____/|___/_____|
            | |
            |_|

    Platform Name             : StarFive VisionFive V2
    Platform Features         : medeleg
    Platform HART Count       : 5
    Platform IPI Device       : aclint-mswi
    Platform Timer Device     : aclint-mtimer @ 4000000Hz
    Platform Console Device   : uart8250
    Platform HSM Device       : ---
    Platform PMU Device       : ---
    Platform Reboot Device    : pm-reset
    Platform Shutdown Device  : pm-reset
    Platform Suspend Device   : ---
    Firmware Base             : 0x40000000
    Firmware Size             : 392 KB
    Firmware RW Offset        : 0x40000
    Runtime SBI Version       : 1.0

    Domain0 Name              : root
    Domain0 Boot HART         : 1
    Domain0 HARTs             : 0*,1*,2*,3*,4*
    Domain0 Region00          : 0x0000000002000000-0x000000000200ffff M: (I,R,W) S/U: ()
    Domain0 Region01          : 0x0000000040000000-0x000000004003ffff M: (R,X) S/U: ()
    Domain0 Region02          : 0x0000000040040000-0x000000004007ffff M: (R,W) S/U: ()
    Domain0 Region03          : 0x0000000000000000-0xffffffffffffffff M: (R,W,X) S/U: (R,W,X)
    Domain0 Next Address      : 0x0000000040200000
    Domain0 Next Arg1         : 0x0000000042200000
    Domain0 Next Mode         : S-mode
    Domain0 SysReset          : yes
    Domain0 SysSuspend        : yes

    Boot HART ID              : 1
    Boot HART Domain          : root
    Boot HART Priv Version    : v1.11
    Boot HART Base ISA        : rv64imafdcbx
    Boot HART ISA Extensions  : none
    Boot HART PMP Count       : 8
    Boot HART PMP Granularity : 4096
    Boot HART PMP Address Bits: 34
    Boot HART MHPM Count      : 2
    Boot HART MIDELEG         : 0x0000000000000222
    Boot HART MEDELEG         : 0x000000000000b109

    U-Boot 2021.10 (Sep 28 2024 - 01:14:56 +0800), Build: jenkins-github_visionfive2_6.6-5

    CPU:   rv64imacu_zba_zbb
    Model: StarFive VisionFive V2
    DRAM:  8 GiB
    MMC:   sdio0@16010000: 0, sdio1@16020000: 1
    Loading Environment from SPIFlash... SF: Detected gd25lq128 with page size 256 Bytes, erase size 4 KiB, total 16 MiB
    OK
    StarFive EEPROM format v2

    --------EEPROM INFO--------
    Vendor : StarFive Technology Co., Ltd.
    Product full SN: VF7110B1-2318-D008E000-00000000
    data version: 0x2
    PCB revision: 0xb2
    BOM revision: A
    Ethernet MAC0 address: 6c:cf:39:00:b0:16
    Ethernet MAC1 address: 6c:cf:39:00:b0:17
    --------EEPROM INFO--------

    In:    serial
    Out:   serial
    Err:   serial
    Model: StarFive VisionFive V2
    Net:   eth0: ethernet@16030000, eth1: ethernet@16040000
    Hit any key to stop autoboot:  0
    Card did not respond to voltage select! : -110
    Card did not respond to voltage select! : -110
    starfive_pcie pcie@2B000000: Port link up.
    starfive_pcie pcie@2B000000: Starfive PCIe bus probed.
    PCI: Failed autoconfig bar 10
    starfive_pcie pcie@2C000000: Port link down.
    starfive_pcie pcie@2C000000: Starfive PCIe bus probed.
    PCI: Failed autoconfig bar 10

    Device 0: unknown device

    Device 0: unknown device
    Tring booting distro ...
    Card did not respond to voltage select! : -110
    Card did not respond to voltage select! : -110

    Device 0: unknown device

    Device 0: unknown device
    StarFive #

So far so good, an U-Boot command prompt beginning with `StarFive # ` should show up at the end of the booting process. No worries for error messages like *Card did not respond to voltage select! : -110* and *Device 0: unknown device*, they are normal at this point. Enter something like `help` to get a list of what valid commands are under the U-Boot shell as a test:

`StarFive #``help`

    ?         - alias for 'help'
    base      - print or set address offset
    bdinfo    - print Board Info structure
    blkcache  - block cache diagnostics and control
    boot      - boot default, i.e., run 'bootcmd'
    bootd     - boot default, i.e., run 'bootcmd'
    bootefi   - Boots an EFI payload from memory
    bootelf   - Boot from an ELF image in memory
    booti     - boot Linux kernel 'Image' format from memory
    bootm     - boot application image from memory
    bootp     - boot image via network using BOOTP/TFTP protocol
    bootvx    - Boot vxWorks from an ELF image
    cmp       - memory compare
    config    - print .config
    coninfo   - print console devices and information
    cp        - memory copy
    cpu       - display information about CPUs
    crc32     - checksum calculation
    dhcp      - boot image via network using DHCP/TFTP protocol
    dm        - Driver model low level access
    echo      - echo args to console
    editenv   - edit environment variable
    eeprom    - EEPROM sub-system
    efidebug  - Configure UEFI environment
    env       - environment handling commands
    erase     - erase FLASH memory
    eraseenv  - erase environment variables from persistent storage
    exit      - exit script
    ext2load  - load binary file from a Ext2 filesystem
    (...)
    showvar   - print local hushshell variables
    size      - determine a file's size
    sleep     - delay execution for some time
    source    - run script from memory
    sysboot   - command to get and boot from syslinux files
    test      - minimal test like /bin/sh
    tftpboot  - boot image via network using TFTP protocol
    tftpput   - TFTP put command, for uploading files to a server
    true      - do nothing, successfully
    unlz4     - lz4 uncompress a memory region
    unzip     - unzip a memory region
    usb       - USB sub-system
    usbboot   - boot from USB device
    version   - print monitor, compiler and linker version

Everything is in good working order at this point. The StarFive VisionFive 2 can be powered down by removing its USB-C power cable (safe operation, will not corrupt anything).

** See also**\
If the system does not boot from SPI flash out of the box, see [SPI issues](https://wiki.gentoo.org/wiki/StarFive_VisionFive_2#SPI_issues_.2F_First_aid_kit "StarFive VisionFive 2")

## [Prerequisites]

This guide assumes the user will be cross compiling or using QEMU, preferring cross compilation. Setup is described below.

** Tip**\
While not described on this page, [Catalyst](https://wiki.gentoo.org/wiki/Catalyst "Catalyst") can be used to generate system images.

### [Preparing the crossdev environment]

If building the system image from non-RISC-V hardware, a cross development environment must be created.

** Important**\
If new to [Crossdev](https://wiki.gentoo.org/wiki/Crossdev "Crossdev"), do not use this quick-start info as a substitute to primary docs.

An abridged setup process is as follows:

First, if a crossdev overlay has not been created, it can be initalzied with:

`root `[`#`]`eselect repository create crossdev`

Then, the **[riscv64]** toolchain can be created with:

`root `[`#`]`crossdev --target riscv64-unknown-linux-gnu`

A **[r64]** **[lp64d]** profile can be selected for that crossdev environment wtih:

`root `[`#`]`PORTAGE_CONFIGROOT=/usr/riscv64-unknown-linux-gnu eselect profile set default/linux/riscv/23.0/rv64/lp64d`

** Tip**\
The U74 cores of a JH7110 SoC supports hardware **double precision** floating point operations, therefore any of the *RV64GC*/LP64**D** profiles are suitable starting point. *RV64GC*/LP64 stage 3 images require no hardware double precision floating point support thus can be used on all *RV64GC* processors.

Once the profile is selected, the environment can be setup with:

`root `[`#`]`USE=build riscv64-unknown-linux-gnu-emerge -v1 baselayout`

The cross build environment make.conf can be updated for optimized builds with:

[FILE] **`/usr/riscv64-unknwon-linux-gnu/etc/portage/make.conf`**

    # Added to the end of make.conf
    # Common flags for cross-compiling and colour; params pulled from -march=native
    COMMON_FLAGS="-mabi=lp64d -march=rv64imafdc_zicsr_zba_zbb -mcpu=sifive-u74 -mtune=sifive-7-series -O2 -pipe --param l1-cache-size=32 --param l2-cache-size=2048"
    CFLAGS="$"
    CXXFLAGS="$"
    FCFLAGS="$"
    FFLAGS="$"

Glibc can be re-emerged with:

`root `[`#`]`riscv64-unknown-linux-gnu-emerge -v1 sys-libs/glibc`

Finally, the system set can be rebuilt with:

`root `[`#`]`riscv64-unknown-linux-gnu-emerge -v1 @system`

** See also**\
[Crossdev#Build_packages_with_crossdev](https://wiki.gentoo.org/wiki/Crossdev#Build_packages_with_crossdev "Crossdev")

### [Optional: Configure QEMU-user and binfmt]

** Important**\
If unfamiliar with QEMU user chroots, this section is not a substitute for the reference material!

** See also**\
[Embedded_Handbook/General/Compiling_with_QEMU_user_chroot](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Compiling_with_QEMU_user_chroot "Embedded Handbook/General/Compiling with QEMU user chroot")

An abridged QEMU user chroot setup for RISC-V is as follows:

#### [Configure riscv64 QEMU targets]

[FILE] **`/etc/portage/package.use/qemu`**

    app-emulation/qemu static-user qemu_softmmu_targets_riscv64 qemu_user_targets_riscv64

#### [Emerge QEMU]

`root `[`#`]`emerge --ask --update --newuse --deep app-emulation/qemu`

#### [Start the qemu-binfmt service]

##### [Openrc]

`root `[`#`]`rc-service qemu-binfmt start`

##### [Manual]

The binfmt handlers can also be manually configured:

`root `[`#`]`mount binfmt_misc -t binfmt_misc /proc/sys/fs/binfmt_misc `

`root `[`#`]`echo ':riscv64:M::\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\xf3\x00:\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xff\xff:/usr/bin/qemu-riscv64:' > /etc/binfmt.d/qemu-riscv64-static.conf `

Then restart binfmt support:

-   **OpenRC:**

    :::: cmd-box


    `root `[`#`]`rc-service binfmt restart`


    ::::
-   **Systemd:**

    :::: cmd-box


    `root `[`#`]`systemctl restart systemd-binfmt`


    ::::

#### [Confirming binfmt registration]

When properly configured, the [/proc/sys/fs/binfmt_misc/qemu-riscv64] should exist:

`user `[`$`]`cat /proc/sys/fs/binfmt_misc/qemu-riscv64 `

    enabled
    interpreter /usr/bin/qemu-riscv64
    flags:
    offset 0
    magic 7f454c460201010000000000000000000200f300
    mask ffffffffffffff00fffffffffffffffffeffffff

#### [Copying the interpreter binary]

The interpreter can be copied into the rootfs with:

`root `[`#`]`cp /usr/bin/qemu-riscv64 /usr/riscv64-unknown-linux-gnu/usr/bin`

#### [Activating the user chroot]

The chroot can be activated with:

`root `[`#`]`arch-chroot /usr/riscv64-unknown-linux-gnu`

Before the environment can be used for the first time, locales and ldconfig must be generated, then the profile must be sourced again:

`root `[`#`]`locale-gen`

`root `[`#`]`ldconfig`

`root `[`#`]`. /etc/profile`

** Important**\
If using QEMU user chroots with a crossdev environment, the ROOT and CHOST definitions in the [/etc/portage/make.conf] must be disabled while using QEMU and re-enabled for crossdev use!

** Warning**\
The crossdev environment make.conf must be restored to working configuration before being used, if used for a QEMU chroot!

### [Environment variables and initial setup]

** Tip**\
Put the `export` statements within a shell-script that can be on-demand sourced or within a .bash_file file.

To keep things clear along the various procedures detailed in the next sections, start by defining some shell variables as they will be used all along this explanation (the dash for `RISCV_XCOMPILE` is not an error):

`root `[`#`]`export RISCV_WORKDIR_PATH=/path/to/a/work/directory `

`root `[`#`]`export RISCV_ROOTFS_PATH=$/rootfs `

`root `[`#`]`export RISCV_XARCH=riscv64-unknown-linux-gnu `

`root `[`#`]`export RISCV_XCOMPILE=$- `

`root `[`#`]`export RISCV_XDEV_ROOT=/usr/$ `

`root `[`#`]`export QEMU_LD_PREFIX=$ `

And create the directories structure where the job will done:

`root `[`#`]`mkdir -p $ `

## [Updating the bootloader]

If building the boot code from source is preferred over using StarFive provided binaries, they can be rebuilt using the created crossdev toolchain.

** Important**\
When building from sources, a stable release branch should be checked out, unless built purely for testing.

### [Building OpenSBI]

OpenSBI (*SBI* standing for *RISC-V Supervisor Binary Interface*) is an open software layer that provides runtime services for the M-Mode and thus is required by U-Boot. A short presentation in PDF to get an overview of what OpenSBI consists of can be found at [https://riscv.org/wp-content/uploads/2024/12/13.30-RISCV_OpenSBI_Deep_Dive_v5.pdf](https://riscv.org/wp-content/uploads/2024/12/13.30-RISCV_OpenSBI_Deep_Dive_v5.pdf)

It can be cloned wherever preferred by the user. In this guide, [\~/projects/] will be used:

`~/projects $``git clone `[`https://github.com/riscv/opensbi.git`](https://github.com/riscv/opensbi.git)

With the sources, the OpenSBI image can be built with:

`~/projects/opensbi $``make ARCH=riscv CROSS_COMPILE=riscv64-unknown-linux-gnu- PLATFORM=generic FW_OPTIONS=0`

    oaded configuration '/home/larry/projects/opensbi/platform/generic/configs/defconfig'
    Configuration saved to '/home/larry/projects/opensbi/build/platform/generic/kconfig/.config'
     CC-DEP    platform/generic/platform.dep
     CC-DEP    lib/sbi/riscv_asm.dep
     CC-DEP    lib/sbi/riscv_atomic.dep
    ...
     AS        platform/generic/firmware/fw_payload.o
     CPP       platform/generic/firmware/fw_payload.elf.ld
     ELF       platform/generic/firmware/fw_payload.elf
     OBJCOPY   platform/generic/firmware/fw_payload.bin

** Important**\
[build/platform/generic/firmware/fw_dynamic.bin] will be used when building U-Boot.

** Tip**\
`FW_OPTIONS=0` makes OpenSBI display a banner at system startup.

### [Building U-Boot]

Similarly to OpenSBI, U-Boot can be built by cloning the sources, and cross building:

`~/projects $``git clone `[`https://github.com/u-boot/u-boot`](https://github.com/u-boot/u-boot)

Once cloned, a stable tag, such as `v2025.04` can be checked out:

`~/projects/u-boot $``git checkout v2025.04`

The VisionFive 2 default config can be generated with:

`~/projects/u-boot $``make ARCH=riscv CROSS_COMPILE=riscv64-unknown-linux-gnu- starfive_visionfive2_defconfig`

** Tip**\
It is possible to customize U-Boot via a configuration menu by issuing: `make CROSS_COMPILE=riscv64-unknown-linux-gnu- menuconfig`

Finally, it can be compiled using the previously generated OpenSBI firmware:

`user `[`$`]`make ARCH=riscv CROSS_COMPILE=riscv64-unknown-linux-gnu- OPENSBI=$/projects/opensbi/build/platform/generic/firmware/fw_dynamic.bin`

### [Updating U-Boot]

** Warning**\
Updating U-Boot can reset the contents of U-Boot environment variables. Customized settings should be backed up **before** updating.

Older U-Boot versions may have bugs or compatibility issues with certain kernels. In the event of boot issues, a new U-Boot version can be installed to the SPI flash while U-Boot is running.

  ----------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------- ----------------------------------
  Official Firmware file                                                                                            Source-built Firmware File                                                                                           Base address in SPI flash memory
  [u-boot-spl.bin.normal.out]    [spi/u-boot-spl.bin.normal.out]   0x0
  [visionfive2_fw_payload.img]   [u-boot.itb]                      0x100000
  ----------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------- ----------------------------------

U-Boot supports several methods for firmware updates, including:

-   Firmware loaded from attached storage
-   TFTP
-   UART/Y-Modem

Additionally, the firmware may be updated from the running system using [[[sys-fs/mtd-utils]](https://packages.gentoo.org/packages/sys-fs/mtd-utils)[]].

** Important**\
While the VisionFive 2 can use boot code from SD or eMMC, the SPI flash should be preferred for general use.

** See also**\
[U-Boot StarFive 2 Update Docs](https://docs.u-boot.org/en/latest/board/starfive/visionfive2.html#flashing-a-new-u-boot-version)

#### [Updating from SD]

U-Boot can read firmware files from external storage, such as a SD card, and write it to the SPI flash.

Files from the table above can be copied an EXT4 or FAT32 partition on a SD card. Partition 3 on a SD card is used in this example.

##### [Initialize SPI flash]

With U-Boot running, the SPI flash can be initialized with:

`StarFive #``sf probe`

SF: Detected gd25lq128 with page size 256 Bytes, erase size 4 KiB, total 16 MiB

##### [Read SD]

MMC devices can be scanned with:

`StarFive #``mmc list`

    mmc@16010000: 0
    mmc@16020000: 1 (SD)

The SD card can be selected with:

`StarFive #``mmc dev 1`

    switch to partitions #0, OK
    mmc1 is current device

Partitions can be listed with:

`StarFive #``mmc part`

    Partition Map for mmc device 1  --   Partition Type: EFI

    Part    Start LBA   End LBA     Name
        Attributes
        Type GUID
        Partition GUID
      1 0x00001000  0x00001fff  ""
        attrs:  0x0000000000000000
        type:   2e54b353-1271-4842-806f-e436d6af6985
            (2e54b353-1271-4842-806f-e436d6af6985)
        guid:   0c4cd076-a05d-4b41-a482-3306a31a034d
      2 0x00002000  0x00003fff  ""
        attrs:  0x0000000000000000
        type:   bc13c2ff-59e6-4262-a352-b275fd6f7172
            (bc13c2ff-59e6-4262-a352-b275fd6f7172)
        guid:   048b83df-86ce-4a1f-a48f-103350b1667a
      3 0x00004000  0x00095fff  ""
        attrs:  0x0000000000000000
        type:   0fc63daf-8483-4772-8e79-3d69d8477de4
            (linux)
        guid:   84f09457-f4a4-42c9-8d7b-e5e04d9766e1
      4 0x00096000  0x0748b7ff  ""
        attrs:  0x0000000000000000
        type:   0fc63daf-8483-4772-8e79-3d69d8477de4
            (linux)
        guid:   6df36844-5180-4485-8817-ad8053dde054

Files on the third partition can be listed with:

`StarFive #``ls mmc 1:3`

       150071   u-boot-spl.bin.normal.out
      1277629   u-boot.itb

    2 file(s), 0 dir(s)

##### [Flashing the firmware]

With the files located, they can be loaded into memory, then written to the SPI:

First the SPL can be loaded to a scratch memory area with:

`StarFive #``load mmc 1:3 $loadaddr u-boot-spl.bin.normal.out`

150071 bytes read in 9 ms (15.9 MiB/s)

Then it can be written to the SPI with:

`StarFive #``sf update $loadaddr 0 $filesize`

    device 0 offset 0x0, size 0x24a37
    150071 bytes written, 0 bytes skipped in 0.793s, speed 193056 B/s

This process can be repeated for U-Boot, with an offset:

`StarFive #``load mmc 1:3 $loadaddr u-boot.itb`

1277629 bytes read in 56 ms (21.8 MiB/s)

`StarFive #``sf update $loadaddr 0x100000 $filesize`

    device 0 offset 0x100000, size 0x137ebd
    1183421 bytes written, 94208 bytes skipped in 9.103s, speed 143673 B/s

#### [UART method]

First, gather the following firmware files from the latest [VisionFive2 software release](https://github.com/starfive-tech/VisionFive2/releases)

Second, calculate their CRC-32 with [/usr/bin/crc32] (provided by [[[dev-perl/Archive-Zip]](https://packages.gentoo.org/packages/dev-perl/Archive-Zip)[]]) on the host, results might defer from what is show here:

`user `[`$`]`crc32 u-boot-spl.bin.normal.out visionfive2_fw_payload.img`

    4f92e463        u-boot-spl.bin.normal.out
    6949ec27        visionfive2_fw_payload.img

Third, ensure the StarFive VisionFive 2 is set up **to boot off the onboard SPI Flash memory**: both RGPIO_0 and RGPIO_1 switches must be set to High. Once done power the board on and the U-Boot command prompt should be reached after a few seconds. From that prompt there, run the following command to initialize a file transfer via the Y-Modem protocol (calculates a CRC for each chunk of transferred data to ensure no corruption has occurred):

`StarFive #``loady`

    ## Ready for binary (ymodem) download to 0x60000000 at 115200 bps...
    CCCCC

At this point, use [Ctrl]+[A] then [S] in Minicom to enter the file transfer menu, then select **Ymodem**, then a single firmware file of your choice (beginning with [u-boot-spl.bin.normal.out] or [visionfive2_fw_payload.img] is not important as long as both are processed) and wait for the transfer to complete.

`StarFive #``loady`

    ## Ready for binary (ymodem) download to 0x60000000 at 115200 bps...
    CC0(STX)/0(CAN) packets, 6 retries
    ## Total Size      = 0x00025a30 = 154160 Bytes

At this point the firmware payload lies in board\'s RAM but remains to be written on the SPI flash memory. Before committing it to the SPI flash memory, check the firmware payload\'s CRC-32 as it is seen on the StarFive VisionFive 2 board (the result should match what has been computed on the host):

`StarFive #``crc32 $loadaddr $filesize`

crc32 for 60000000 \... 60025a2f ==\> 4f92e463

** Tip**\
`$filesize` is a shell variable automatically initialized when the transfer completes. A couple of shell variables like `$loadaddr` are preset at system startup. To see all defined variables use the shell command: [printenv].

If the CRC-32 value calculated on the board matches the one calculated on the host, the firmware file contents can be comitted to the onboard SPI flash memory. Depending on which firmware file has been transferred, the command to use is:

-   For [u-boot-spl.bin.normal.out]:

`StarFive #``sf update $loadaddr 0x0 $filesize`

-   For [visionfive2_fw_payload.img]:

`StarFive #``sf update $loadaddr 0x100000 $filesize`

Repeat the operations above for the second firmware file. Once both firmware files have been transferred and committed to the onboard SPI flash memory, **powercycle** the board and the U-Boot command prompt should show up again after a couple of seconds. In the case some badluck would have happened making the board unable to boot on the onboard SPI flash memory, it is possible to recover from the situation using recovery boot image, see section *First aid kit*.

## [Build a system image]

** Warning**\
The BSP (VisionFive 2 SDK) is **outdated** and not very actively maintained so it will not be used here. However there is valuable valuable information inside.

There are two philosophies when it comes to installing an operating system onto a SBC / embedded device such as the VisionFive 2.

The first involves writing a static system image, typically a squashfs, onto some form of media (typically eMMC, though NVMe is on the rise). The initramfs is able to load this image into RAM and use it as a rootfs; when an update is required the whole image is replaced as a single operation. There are advantages to this approach, particularly for embedded devices where users are not expected to update individual packages and recovery \'in-the-field\' may be impractical, or to provide an A/B partition layout for updates. Systems configured in this way are also resilient when it comes to unexpected shutdowns as the only time that the rootfs storage volume is performing writes is when this image is being updated. This approach will be described as an *embedded installation* going forward and called out where possible.

The second approach involves writing a rootfs onto some accessible storage media the device and using a package manager to install and update packages as required. For a Gentoo system this approach is more flexible and allows for a more traditional Linux experience, but requires more effort to set up and maintain. This approach will be described as a *traditional installation* going forward and called out where possible and will be the taken path for the next sections.

The process of generating a system image for a Gentoo installation on the VisionFive 2 may be broadly described as follows:

1.  Check out the required files (pre-built Gentoo stage 3, OpenSBI, U-Boot, etc) ;
2.  Build a cross-compiler and a QEMU emulator
3.  Generate a Gentoo rootfs
4.  Generate a Linux kernel and ramdisk (U-Boot format conversion required)
5.  Flash the rootfs on some SD Card
6.  Try to boot the machine

### [Download an existing RISC-V stage 3]

** Tip**\
To see all the available images: [https://gentoo.osuosl.org/releases/riscv/autobuilds](https://gentoo.osuosl.org/releases/riscv/autobuilds)

Rather than building a full cross-dev environment and the subsequent stages archives with Catalyst, Gentoo offers some pre-built tarballs for RISC-V machines that avoids some tedious steps.

To begin with, grab a Gentoo stage 3 tarball from [https://www.gentoo.org/downloads/#riscv](https://www.gentoo.org/downloads/#riscv).

For the rest of the explanations, the *systemd* flavor of rv64gc/lp64d will be used.

To download one of the available images, a tool like [[[net-misc/aria2]](https://packages.gentoo.org/packages/net-misc/aria2)[]] or [[[net-misc/wget]](https://packages.gentoo.org/packages/net-misc/wget)[]] can be used. E.g.:

`root `[`#`]`aria2c -x16 -s16 `[`https://gentoo.osuosl.org/releases/riscv/autobuilds/20241213T160325Z/stage3-rv64_lp64d-systemd-20241213T160325Z.tar.xz`](https://gentoo.osuosl.org/releases/riscv/autobuilds/20241213T160325Z/stage3-rv64_lp64d-systemd-20241213T160325Z.tar.xz)` `

### [Create the root filesystem]

It is possible to build the root filesystem via two options:

-   Directly use a prebuilt Gentoo stage 3 archive (the path taken here) ;
-   Build all stages from scratch via \[Catalyst\] and a crossdev environment

#### [Extract and prepare the pre-built stage 3 archive]

** Important**\
Quoting the download page: *Multilib stages include toolchain support for all 64-bit and 32-bit ABI and are based on lp64d. They are mostly useful for development and testing purposes.*

Simply extract the stage 3 archive downloaded a few paragraphs ago:

`root `[`#`]`cd $ `

`root `[`#`]`tar -Jxpvf stage3-*.tar.xz -C $ `

From there, bind-mount the Gentoo repository. To avoid unfortunate incident it is advised to bind-mount as read-only:

`root `[`#`]`mkdir -p $/var/db/repos/gentoo `

`root `[`#`]`mount -o bind,ro /var/db/repos/gentoo $/var/db/repos/gentoo `

Same story for the Linux kernel but as read-write this time. To use the same kernel version in use on the host:

`root `[`#`]`mkdir -p $/usr/src/linux `

`root `[`#`]`mount -o bind /usr/src/linux $/usr/src/linux `

#### [Refresh the root filesystem]

** Warning**\
Stick with the method exposed here and do not mess up with \$, \$ or \$ **unless having the luxury of having a host system being broken beyond all repair** as some critical system binaries like [/lib/ld-linux.so.2] can be overwritten. If this would happen, restoring from a recent backup (e.g. virtual machine snapshot, filesystem snapshot or copy) would be the only way out!

From there two strategies are offered:

1.  All *\@system* packages are cross-built as binaries packages (and stored within the cross-compilation environment in [\$/var/db/pkg]) then re-emerged in the target environment ([\$]). This approach is interesting if rebuilding the very same target environment multiple time is expected as it can save a lot of time by avoiding re-compiling the same packages over and over again.
2.  All *\@system* packages are cross-built, deployed in the target ([\$]) environment and stored as binary packages **within** the target environment in [\$/var/db/pkg] (unless *buildpkg* is removed from the variable `FEATURES`).

To build everything within the cross-compilation environment then deploying the produced binary packages:

`root `[`#`]`$-emerge --keep-going --jobs=$(nproc) -e @system`

`root `[`#`]`ROOT=$ $-emerge --usepkgonly --jobs=$(nproc) -e @system`

If working directly within the target environment is preferred:

`root `[`#`]`ROOT=$ $-emerge --keep-going --jobs=$(nproc) -e @system`

As a suitable bare minimum the following should be refreshed:

-   [[[sys-libs/glibc]](https://packages.gentoo.org/packages/sys-libs/glibc)[]]
-   [[[sys-devel/gcc]](https://packages.gentoo.org/packages/sys-devel/gcc)[]]
-   [[[sys-devel/binutils]](https://packages.gentoo.org/packages/sys-devel/binutils)[]]

Any dependency hell or failure can be resolved by playing around with [\$/etc/portage/package.\*] directories content as usually done on the host system. Good luck! Once this stage is done go ahead to the next section.

\

#### [Set the system profile for the target environment]

** Important**\
Choose **the same profile** than the one chosen for the cross-build environment!

The very next step is to define the system profile for the target environment. The task is easy as **both profiles must match**: if the profile used for the cross-build environment is *default/linux/riscv/23.0/rv64/lp64d (stable)* then the profile to set for the target environment must also be *default/linux/riscv/23.0/rv64/lp64d (stable)* (or 35).

`root `[`#`]`PORTAGE_CONFIGROOT=$ eselect profile list | grep 23.0 `

      [28]  default/linux/riscv/23.0/rv64/lp64d (stable)
      [29]  default/linux/riscv/23.0/rv64/lp64d/desktop (dev)
      [30]  default/linux/riscv/23.0/rv64/lp64d/desktop/gnome (dev)
      [31]  default/linux/riscv/23.0/rv64/lp64d/desktop/gnome/systemd (dev)
      [32]  default/linux/riscv/23.0/rv64/lp64d/desktop/plasma (dev)
      [33]  default/linux/riscv/23.0/rv64/lp64d/desktop/plasma/systemd (dev)
      [34]  default/linux/riscv/23.0/rv64/lp64d/desktop/systemd (dev)
      [35]  default/linux/riscv/23.0/rv64/lp64d/systemd (stable)
      [36]  default/linux/riscv/23.0/rv64/lp64 (stable)
      [37]  default/linux/riscv/23.0/rv64/lp64/desktop (dev)
      [38]  default/linux/riscv/23.0/rv64/lp64/desktop/gnome (dev)
      [39]  default/linux/riscv/23.0/rv64/lp64/desktop/gnome/systemd (dev)
      [40]  default/linux/riscv/23.0/rv64/lp64/desktop/plasma (dev)
      [41]  default/linux/riscv/23.0/rv64/lp64/desktop/plasma/systemd (dev)
      [42]  default/linux/riscv/23.0/rv64/lp64/desktop/systemd (dev)
      [43]  default/linux/riscv/23.0/rv64/lp64/systemd (stable)
      [44]  default/linux/riscv/23.0/rv64/multilib (exp)
      [45]  default/linux/riscv/23.0/rv64/multilib/systemd (exp)
      [46]  default/linux/riscv/23.0/rv32/ilp32d (exp)
      [47]  default/linux/riscv/23.0/rv32/ilp32d/systemd (exp)
      [48]  default/linux/riscv/23.0/rv32/ilp32 (exp)
      [49]  default/linux/riscv/23.0/rv32/ilp32/systemd (exp)
      [50]  default/linux/riscv/23.0/rv64/split-usr/lp64d (stable)
      [51]  default/linux/riscv/23.0/rv64/split-usr/lp64d/desktop (dev)
      [52]  default/linux/riscv/23.0/rv64/split-usr/lp64d/desktop/gnome (dev)
      [53]  default/linux/riscv/23.0/rv64/split-usr/lp64d/desktop/plasma (dev)
      [54]  default/linux/riscv/23.0/rv64/split-usr/lp64 (stable)
      [55]  default/linux/riscv/23.0/rv64/split-usr/lp64/desktop (dev)
      [56]  default/linux/riscv/23.0/rv64/split-usr/lp64/desktop/gnome (dev)
      [57]  default/linux/riscv/23.0/rv64/split-usr/lp64/desktop/plasma (dev)
      [58]  default/linux/riscv/23.0/rv64/split-usr/multilib (exp)
      [59]  default/linux/riscv/23.0/rv32/split-usr/ilp32d (exp)
      [60]  default/linux/riscv/23.0/rv32/split-usr/ilp32 (exp)
      [63]  default/linux/riscv/23.0/rv64/lp64d/musl (dev)
      [64]  default/linux/riscv/23.0/rv64/lp64/musl (dev)
      [65]  default/linux/riscv/23.0/rv64/split-usr/lp64d/musl (dev)
      [66]  default/linux/riscv/23.0/rv64/split-usr/lp64/musl (dev)
      [67]  default/linux/riscv/23.0/rv32/ilp32d/musl (exp)
      [68]  default/linux/riscv/23.0/rv32/ilp32/musl (exp)
      [69]  default/linux/riscv/23.0/rv32/split-usr/ilp32d/musl (exp)
      [70]  default/linux/riscv/23.0/rv32/split-usr/ilp32/musl (exp)

For example the following will select *default/linux/riscv/23.0/rv64/lp64d (stable)* in the target environment (pay attention to the environment variable name):

`root `[`#`]`PORTAGE_CONFIGROOT=$ eselect profile set 35`

#### [Prepare the RISC-V root filesystem for chrooting]

Start by emerging [[[app-emulation/qemu]](https://packages.gentoo.org/packages/app-emulation/qemu)[]] into the target from the pre-built binary package created in the prerequisites section:

`root `[`#`]`ROOT=$ emerge --usepkgonly --oneshot --nodeps qemu `

For convenience, while being outside the target, copy the file [/etc/resolv.conf] in the target:

`root `[`#`]`cp /etc/resolv.conf $/etc `

Then *bind-mount* all required (pseudo-)filesystems in the target:

`root `[`#`]`cd $ `

`root `[`#`]`mount --bind /proc proc `

`root `[`#`]`mount --bind /dev dev `

`root `[`#`]`mount --bind /dev/pts dev/pts `

The last step is to chroot in the target and **change the root password**:

`root `[`#`]`chroot . /bin/bash --login `

`root `[`#`]`passwd root `

All of the puzzle pieces are in place and incidentally the RISC-V binaries are runnable inside the chrooted environment from a X86/64 machine.

#### [Customize and configure the RISC-V stage3]

** Tip**\
For a first time keep a lean environment: the less packages are emerged, the lower chances are to see breakages.

Some additional packages are required: [[[sys-apps/dtc]](https://packages.gentoo.org/packages/sys-apps/dtc)[]], [[[dev-embedded/u-boot-tools]](https://packages.gentoo.org/packages/dev-embedded/u-boot-tools)[]] and [[[sys-kernel/dracut]](https://packages.gentoo.org/packages/sys-kernel/dracut)[]]. Emerge them directly on the host:

`root `[`#`]`emerge --ask sys-apps/dtc dev-embedded/u-boot-tools sys-kernel/dracut`

Then proceed with a typical Stage 3 customization and emerge whatever package is needed (outside of Kernel and Bootloader) as seen before:

`root `[`#`]`$-emerge pkg1 pkg2 pkg3 ... `

`root `[`#`]`ROOT=$ $-emerge --usepkgonly pkg1 pkg2 pkg3 ... `

or:

`root `[`#`]`ROOT=$ $-emerge pkg1 pkg2 pkg3 ... `

### [Build the kernel]

** Note**\
There are some out-of-tree kernel modules (jpu/venc/vdec) that should be installed in addition to this kernel. These modules are available from the [VisionFive 2 soft_3rdpart repo](https://github.com/starfive-tech/soft_3rdpart), or by emerging [[[media-video/vf2vpudev]](https://packages.gentoo.org/packages/media-video/vf2vpudev)[]] from the [bingch overlay](https://gitlab.com/bingch/gentoo-overlay)

While QEMU can be used to build the kernel, it\'s extremely slow compared to using a cross-compiling toolchain.

The kernel could be cross-built directly in the kernel source dir on the host, but it\'s best to copy the sources into the crossdev environment, so the host kernel config is untouched:

`root `[`#`]`cp -a /usr/src/linux /usr/riscv64-unknown-linux-gnu/usr/src/linux`

In this guide, config specifically for this board will be used. Advanced users can start from the defconfig.

To perform a clean build:

`/usr/riscv64-unknown-linux-gnu/usr/src/linux #``make mrproper `

`/usr/riscv64-unknown-linux-gnu/usr/src/linux #``wget `[`https://github.com/starfive-tech/linux/raw/refs/heads/JH7110_VisionFive2_upstream/arch/riscv/configs/starfive_visionfive2_defconfig`](https://github.com/starfive-tech/linux/raw/refs/heads/JH7110_VisionFive2_upstream/arch/riscv/configs/starfive_visionfive2_defconfig)` -O .config `

`/usr/riscv64-unknown-linux-gnu/usr/src/linux #``make ARCH=riscv CROSS_COMPILE=riscv64-unknown-linux-gnu- olddefconfig `

`/usr/riscv64-unknown-linux-gnu/usr/src/linux #``make ARCH=riscv CROSS_COMPILE=riscv64-unknown-linux-gnu- -j $(nproc) `

`/usr/riscv64-unknown-linux-gnu/usr/src/linux #``make ARCH=riscv CROSS_COMPILE=riscv64-unknown-linux-gnu- dtbs `

To install kernel modules:

`/usr/riscv64-unknown-linux-gnu/usr/src/linux #``make ARCHARCH=riscv CROSS_COMPILE=riscv64-unknown-linux-gnu- INSTALL_MOD_PATH=/usr/riscv64-unknown-linux-gnu/ modules_install `

To install the kernel image:

`root `[`#`]`cp arch/riscv/boot/Image.gz /usr/riscv64-unknown-linux-gnu/boot/kernel.gz`

Install the DTBs:

`root `[`#`]`cp arch/riscv/boot/dts/starfive/jh7110-starfive-visionfive-2-v1.3b.dtb /usr/riscv64-unknown-linux-gnu/boot`

### [Bootloader considerations]

Unfortunately EXTCONF (SYSCONF) is an EFI/x86 thing and GRUB, despite supporting RISC-V, is another EFI-only thing. As the StarFive Visionfive 2 does not support EFI the only remaining option is to play with some U-Boot variables (those familiar with OpenBoot/SPARC will be in known territory). No worries, booting that way is as simple as using any sort of Linux shell.

## [Imaging the device]

As mentioned at the beginning, the StarFive VisionFive 2 can load U-Boot via several possibilities depending on the configuration of the RGPIO switches:

-   A microSD card (bottom side)
-   An eMMC card (bottom side)
-   Over an UART

Once U-Boot has been loaded, it can boot the Linux environment either via a local device (a microSD card, an eMMC or a NVMe stick), either via TFTP. As it has been said earlier U-Boot, if configured via an *extlinux configuration file*, **will not be able to use FIT images**.

### [][microSD Card/eMMC]

** Warning**\
Not all the microSD Cards currently on the market are compatible with the StarFive Vision 2. Basically, **any model having more than 128G capacity will fail to boot** with weird errors like: *dwmci_s: Response Timeout, BOOT fail,Error is 0xffffffff,* etc. Consult the compatibility list: [avl_list.html](https://doc-en.rvspace.org/JH7110/AVL/JH7110_DS/avl_list.html)

The approach is very similar to the the way that aarch64 devices are imaged due to the similar boot mechanisms:

-   The microSD card will be partitioned using GPT as a partition scheme.
-   An image will be generated manually on-disk which may then be installed onto the microSD card using tools such as [dd].

The [JH7110 Boot User guide.pdf](https://doc-en.rvspace.org/VisionFive2/Developer_Guide/JH7110_Boot_UG.pdf) mentions (section 4, page 15) that:

> StarFive recommends that you use 1-bit QSPI Nor Flash or UART mode since there is a low possibility that the VisionFive 2 may fail to boot in eMMC or SDIO3.0 boot mode. For more details, refer to eMMC/SDIO3.0 boot issue section in VisionFive 2 Errata Sheet.[\[1\]](https://doc-en.rvspace.org/JH7110/PDF/JH7110_Errata.pdf)

\"Not recommended\" means that future board or SiFive JH7110 SoC revisions might drop the capability. However it is still acceptable to use a microSD or eMMC Card to boot the system for the current context. Thus, the explanations will ignore this warning.

#### [Preparing the microSD Card]

The first step is to create a raw image and mount it on an available loopback block device:

`root `[`#`]`cd $ `

`root `[`#`]`fallocate -l 8G visionfive2.img `

`root `[`#`]`losetup --find --show visionfive2.img `

/dev/loop0

Now, just like a physical hard drive or SSD, the raw image has to be partitioned. In the present case four partitions will be used:

-   partition 1 will contain the U-Boot SPL (Secondary Program Loader)
-   partition 2 will contains U-Boot per se
-   partition 3 will contain the kernel image and whatever that latter requires (e.g. an initramfs image and so on)
-   partition 4 will contain the root filesystem (i.e. the Gentoo root filesystem)

\

** Note**\
If the microSD card is larger than the size of the disk image (which is recommended; it saves a lot of time when imaging) resize2fs or a similar utility depending on file system may be used to resize the rootfs partition later.

According to the [JH7110 Boot User guide.pdf](https://doc-en.rvspace.org/VisionFive2/Developer_Guide/JH7110_Boot_UG.pdf) (see pages 8 and 9), the partitioning scheme is the following:

  -------------- ----------------------- ----------------------- ----------------- ---------------- ------------------ ---------------------------------------------------
  Offset (hex)   Length in bytes (hex)   Length in bytes (dec)   First sector \#   Last sector \#   GPT Partition \#   Notes
  0x0            0x200                   512                     0                 0                N/A                Protected MBR
  0x200          0x200                   512                     1                 1                N/A                GPT header
  0x400          0x1FFC00                2096128                 4096              8191             1                  SPL
  0x200000       0x200000                2097152                 8192              16383            2                  U-Boot
  0x400000       0x400000                4194304                 16384             614399           3                  Linux Kernel image and related files (i.e. /boot)
  0x800000       \...                    \...                    614400            Last             4                  Root filesystem
  -------------- ----------------------- ----------------------- ----------------- ---------------- ------------------ ---------------------------------------------------

  : TC/eMMC card layout (512 bytes sectors)

Also a specific GPT partition type (UUID) is expected for all of the four partitions. Those to be used can be found in the [U-Boot source code](https://github.com/u-boot/u-boot) and more specifically in the file [include/configs/starfive-visionfive2.h](https://github.com/u-boot/u-boot/blob/master/include/configs/starfive-visionfive2.h).

  ------------------ -------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------
  GPT Partition \#   GPT partition type UUID                Notes
  1                  2E54B353-1271-4842-806F-E436D6AF6985   The boot ROM will seek for a partition with that type on the medium (being the first one is not mandatory)
  2                  BC13C2FF-59E6-4262-A352-B275FD6F7172   This position is hard-coded in the U-Boot binaries and have to be the second one with the default U-Boot configuration (can be changed by recompiling U-Boot)
  3                  EBD0A0A2-B9E5-4433-87C0-68B6B72699C7   With the default U-Boot configuration must be an ext2, ext4 or vFAT filesystem (BTRFS and others can be supported by recompiling U-Boot).
  4                  0FC63DAF-8483-4772-8E79-3D69D8477DE4
  ------------------ -------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------

  : Partition types to use

Putting things together, the partitioning can be done in an oneshot command:

`root `[`#`]

    sgdisk --clear \
      --new=1:4096:8191    --change-name=1:"spl"    --typecode=1:2E54B353-1271-4842-806F-E436D6AF6985 \
      --new=2:8192:16383   --change-name=2:"uboot"  --typecode=2:BC13C2FF-59E6-4262-A352-B275FD6F7172 \
      --new=3:16384:614399 --change-name=3:"kernel" --typecode=3:EBD0A0A2-B9E5-4433-87C0-68B6B72699C7 \
      --new=4:614400:0     --change-name=4:"root"   --typecode=4:0FC63DAF-8483-4772-8E79-3D69D8477DE4 \
      /dev/loop0

    Creating new GPT entries in memory.
    Warning: The kernel is still using the old partition table.
    The new table will be used at the next reboot or after you
    run partprobe(8) or kpartx(8)
    The operation has completed successfully.

Execute [partprobe] as suggested:

`root `[`#`]`partprobe -s /dev/loop0 `

/dev/loop0: gpt partitions 1 2 3 4

Now check and confirm what happened (forget the column `Code` which shows a shortened partition type):

`root `[`#`]`sgdisk -p /dev/loop0 `

    Disk /dev/loop0: 16777216 sectors, 8.0 GiB
    Sector size (logical/physical): 512/512 bytes
    Disk identifier (GUID): 94F6E0D1-F4B0-4585-A440-FC79A958A148
    Partition table holds up to 128 entries
    Main partition table begins at sector 2 and ends at sector 33
    First usable sector is 34, last usable sector is 16777182
    Partitions will be aligned on 2048-sector boundaries
    Total free space is 4062 sectors (2.0 MiB)

    Number  Start (sector)    End (sector)  Size       Code  Name
       1            4096            8191   2.0 MiB     FFFF  spl
       2            8192           16383   4.0 MiB     EA00  uboot
       3           16384          614399   292.0 MiB   0700  kernel
       4          614400        16777182   7.7 GiB     8300  root

All partitions matching what they should be in size and boundaries, U-Boot and SPL will be taken care of (in the next section).

#### [Write the SPL and U-Boot]

** Note**\
It is possible to combine the SPL and U-Boot into a single image. This will require a different partition layout but should otherwise be similar to this example. This is not covered here, but should be. Please help out by updating the wiki!

The SPL and U-Boot may be both directly dumped to the image using [dd]:

`root `[`#`]`cd $ `

`root `[`#`]`dd if=u-boot/spl/u-boot-spl.bin.normal.out of=/dev/loop0p1 `

`root `[`#`]`dd if=u-boot/u-boot.itb of=/dev/loop0p2`

#### [Incorporate the root filesystem to the media image]

The *boot* partition may be formatted as FAT32/VFAT with [mkfs.fat], and the root partition as ext4 with [mkfs.ext4]. The following commands may be used to format and mount the partitions:

`root `[`#`]`mkfs.fat -F 32 -n ROOT /dev/loop0p3 `

`root `[`#`]`mkfs.ext4 -L root /dev/loop0p4 `

    Creating filesystem with 2020347 4k blocks and 505920 inodes
    Filesystem UUID: 68acdb19-5d85-4401-a9e6-033e5b4a357d
    Superblock backups stored on blocks:
            32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632

    Allocating group tables: done
    Writing inode tables: done
    Creating journal (16384 blocks): done
    Writing superblocks and filesystem accounting information: done

Next, mount the root and boot filesystems (here under [/mnt//mnt/visionfive2] and copy the whole content located in `$`:

`root `[`#`]`mount /dev/loop0p4 /mnt/visionfive2 `

`root `[`#`]`mkdir -p /mnt/visionfive2/boot `

`root `[`#`]`mount /dev/loop0p3 /mnt/visionfive2/boot `

`root `[`#`]`rsync -aH --progress --delete-before --exclude=/dev --exclude=/proc --exclude=/sys --exclude=/var/tmp $/ /mnt/visionfive2/ `

Edit [/mnt/visionfive2/etc/fstab] to cater for any file systems that need to be mounted on the device. A typical content is the following:

[FILE] **`/mnt/visionfive2/etc/fstab`**

    LABEL=BOOT                                 /boot           vfat            defaults        0 1
    UUID=68acdb19-5d85-4401-a9e6-033e5b4a357d  /               ext4            defaults        0 1

** Note**\
The UUID 68acdb19-5d85-4401-a9e6-033e5b4a357d comes from what [mkfs.ext4] returned on the *Filesystem UUID* line.

Then unmount the image:

`root `[`#`]`umount -R /mnt/visionfive2 `

`root `[`#`]`losetup -d /dev/loop0 `

#### [Transfer the image to the microSD card]

** Important**\
Depending on what is used for reading/writing SD Cards the name of the device to dump the image on can vary:

-   /dev/mmcblkX: usually for a device directly connected to a PCI/PCIe bus
-   /dev/sdX: usually for a USB device

Simply dump the image using the following command upfront:

`root `[`#`]`dd if=visionfive2.img of=/dev/mmcblk0 bs=4M oflag=sync status=progress`

Now the secondary GPT has to be moved to the actual end of the TC/SD Card. The strategy is to delete the last partition then recreate it, and finally resize the file system. Fortunately [sgdisk] can do that automatically with its option `-e`:

`root `[`#`]`sgdisk -e /dev/mmcblk0 `

`root `[`#`]`sgdisk -d 4 /dev/mmcblk0 `

`root `[`#`]`sgdisk --new=4:614400:0 --change-name=4:"root" --typecode=4:0FC63DAF-8483-4772-8E79-3D69D8477DE4 /dev/mmcblk0 `

`root `[`#`]`partprobe /dev/mmcblk0`

Check to see what happened:

`root `[`#`]`sgdisk -p /dev/mmcblk0 `

    Disk /dev/sdd: 62333952 sectors, 29.7 GiB
    Model: STORAGE DEVICE
    Sector size (logical/physical): 512/512 bytes
    Disk identifier (GUID): 429D17C2-A779-4D47-B7C9-49820D387418
    Partition table holds up to 128 entries
    Main partition table begins at sector 2 and ends at sector 33
    First usable sector is 34, last usable sector is 62333918
    Partitions will be aligned on 2048-sector boundaries
    Total free space is 4062 sectors (2.0 MiB)

    Number  Start (sector)    End (sector)  Size       Code  Name
       1            4096            8191   2.0 MiB     FFFF  spl
       2            8192           16383   4.0 MiB     EA00  uboot
       3           16384          614399   292.0 MiB   0700  kernel
       4          614400        62333918   29.4 GiB    8300  root

This time the fourth partition where the root filesystem is has the correct size. Last but not least, as the fourth partition is using an ext4 filesystem, the latter can be extended with **resize2fs**:

`root `[`#`]`resize2fs /dev/mmcblk0p4 `

    Resizing the filesystem on /dev/mmcblk0p4 to 7714939 (4k) blocks.
    The filesystem on /dev/sdd4 is now 7714939 (4k) blocks long.

\

### [Booting the device]

Allright! The T-Time has come and it is time to boot the StarFive VisionFive 2. Once U-Boot is running, it is possible to load system images and start the Linux kernel via a couple of ways:

-   On a microSD Card or eMMC
-   On a NVMe stick
-   Via BOOTP/TFTP (PXE)

#### [microSD Card]

Again a reminder: **not all microSD Cards are compatible with the board especially those having more than 128G**. If you have weird boot errors (or if nothing seems to happen at all), check for that compatibility issue first.

Now:

1.  power the StarFive VisionFive 2 down
2.  ensure the boot selection switches are in the position: RGPIO_0 = Low, RGPIO_1 = High
3.  Insert the TC/SD card in the StarFive VisionFive 2\'s TC/SD card slot
4.  run [minicom] using the correct TTY device (e.g. ttyUSB0) and settings (speed = 115200 bps with 8 bits, no parity, 1 stop bit =\> 8N1 which is the default) =\> `minicom -D /dev/ttyUSB0 -b 115200`
5.  (Fingers crossed!) power the StarFive VisionFive 2 up

If all is in order the StarFive VisionFive 2 should boot:

[`U-Boot SPL 2024.10 (Dec 15 2024 - 12:54:37 -0500)`]` `

    DDR version: dc2e84f0.
    Trying to boot from MMC2

    OpenSBI v1.5.1
       ____                    _____ ____ _____
      / __ \                  / ____|  _ \_   _|Booting the device
     | |  | |_ __   ___ _ __ | (___ | |_) || |
     | |  | | '_ \ / _ \ '_ \ \___ \|  _ < | |
     | |__| | |_) |  __/ | | |____) | |_) || |_
      \____/| .__/ \___|_| |_|_____/|____/_____|
            | |
            |_|

    Platform Name             : StarFive VisionFive 2 v1.3B
    Platform Features         : medeleg
    Platform HART Count       : 5
    Platform IPI Device       : aclint-mswi
    Platform Timer Device     : aclint-mtimer @ 4000000Hz
    Platform Console Device   : uart8250
    Platform HSM Device       : ---
    Platform PMU Device       : ---
    Platform Reboot Device    : pm-reset
    Platform Shutdown Device  : pm-reset
    Platform Suspend Device   : ---
    Platform CPPC Device      : ---
    Firmware Base             : 0x40000000
    Firmware Size             : 367 KB
    Firmware RW Offset        : 0x40000
    Firmware RW Size          : 111 KB
    Firmware Heap Offset      : 0x51000
    Firmware Heap Size        : 43 KB (total), 2 KB (reserved), 11 KB (used), 29 KB (free)
    Firmware Scratch Size     : 4096 B (total), 416 B (used), 3680 B (free)
    Runtime SBI Version       : 2.0

    Domain0 Name              : root
    Domain0 Boot HART         : 1
    Domain0 HARTs             : 0*,1*,2*,3*,4*
    Domain0 Region00          : 0x0000000010000000-0x0000000010000fff M: (I,R,W) S/U: (R,W)
    Domain0 Region01          : 0x0000000002000000-0x000000000200ffff M: (I,R,W) S/U: ()
    Domain0 Region02          : 0x0000000040040000-0x000000004005ffff M: (R,W) S/U: ()
    Domain0 Region03          : 0x0000000040000000-0x000000004003ffff M: (R,X) S/U: ()
    Domain0 Region04          : 0x000000000c000000-0x000000000fffffff M: (I,R,W) S/U: (R,W)
    Domain0 Region05          : 0x0000000000000000-0xffffffffffffffff M: () S/U: (R,W,X)
    Domain0 Next Address      : 0x0000000040200000
    Domain0 Next Arg1         : 0x0000000040400000
    Domain0 Next Mode         : S-mode
    Domain0 SysReset          : yes
    Domain0 SysSuspend        : yes

    Boot HART ID              : 1
    Boot HART Domain          : root
    Boot HART Priv Version    : v1.11
    Boot HART Base ISA        : rv64imafdcbx
    Boot HART ISA Extensions  : zihpm,sdtrig
    Boot HART PMP Count       : 8
    Boot HART PMP Granularity : 12 bits
    Boot HART PMP Address Bits: 34
    Boot HART MHPM Info       : 2 (0x00000018)
    Boot HART Debug Triggers  : 8 triggers
    Boot HART MIDELEG         : 0x0000000000000222
    Boot HART MEDELEG         : 0x000000000000b109

    U-Boot 2024.10 (Dec 15 2024 - 12:54:37 -0500)

    CPU:   sifive,u74-mc
    Model: StarFive VisionFive 2 v1.3B
    DRAM:  8 GiB
    Core:  136 devices, 26 uclasses, devicetree: board
    WDT:   Not starting watchdog@13070000
    MMC:   mmc@16010000: 0, mmc@16020000: 1
    Loading Environment from SPIFlash... SF: Detected gd25lq128 with page size 256 Bytes, erase size 4 KiB, total 16 MiB
    OK
    StarFive EEPROM format v2

    --------EEPROM INFO--------
    Vendor : StarFive Technology Co., Ltd.
    Product full SN: VF7110B1-2318-D008E000-18003780
    data version: 0x2
    PCB revision: 0xb2
    BOM revision: A
    Ethernet MAC0 address: 6c:cf:39:00:b0:16
    Ethernet MAC1 address: 6c:cf:39:00:b0:17
    --------EEPROM INFO--------

    starfive_7110_pcie pcie@2b000000: Starfive PCIe bus probed.
    starfive_7110_pcie pcie@2c000000: Starfive PCIe bus probed.
    In:    serial@10000000
    Out:   serial@10000000
    Err:   serial@10000000
    Net:   eth0: ethernet@16030000, eth1: ethernet@16040000
    starting USB...
    Bus xhci_pci: Register 5000420 NbrPorts 5
    Starting the controller
    USB XHCI 1.00
    scanning bus xhci_pci for devices... 2 USB Device(s) found
           scanning usb for storage devices... 0 Storage Device(s) found
    Working FDT set to ff72d9c0
    Hit any key to stop autoboot:  0
    Card did not respond to voltage select! : -110
    No EFI system partition
    No EFI system partition
    Failed to persist EFI variables
    No EFI system partition
    Failed to persist EFI variables
    No EFI system partition
    Failed to persist EFI variables
    ** Booting bootflow '<NULL>' with efi_mgr
    Loading Boot0000 'mmc 1' failed
    EFI boot manager: Cannot load any image
    Boot failed (err=-14)
    Card did not respond to voltage select! : -110
    ethernet@16040000 Waiting for PHY auto negotiation to complete...... done
    BOOTP broadcast 1
    BOOTP broadcast 2
    BOOTP broadcast 3
    BOOTP broadcast 4
    BOOTP broadcast 5

    Abort
    StarFive #

Once the U-Boot shell is reached check if all of the partitions are seen and the very first step of this is to list the [MMC devices]:

`StarFive #``mmc list `

    mmc@16010000: 0
    mmc@16020000: 1 (SD)

Now switch to the device identified with *(SD)*:

`StarFive #`` mmc dev 1 `

    switch to partitions #0, OK
    mmc1 is current device

Then list the partitions on it:

`StarFive #``mmc part `

    Partition Map for mmc device 1  --   Partition Type: EFI

    Part    Start LBA       End LBA         Name
            Attributes
            Type GUID
            Partition GUID
      1     0x00001000      0x00001fff      "spl"
            attrs:  0x0000000000000000
            type:   2e54b353-1271-4842-806f-e436d6af6985
                    (2e54b353-1271-4842-806f-e436d6af6985)
            guid:   f9960331-7953-4977-81ba-6862140ea8c6
      2     0x00002000      0x00003fff      "uboot"
            attrs:  0x0000000000000000
            type:   bc13c2ff-59e6-4262-a352-b275fd6f7172
                    (bc13c2ff-59e6-4262-a352-b275fd6f7172)
            guid:   08ecf256-fda7-4af3-9460-ff9834c103d3
      3     0x00004000      0x00095fff      "kernel"
            attrs:  0x0000000000000000
            type:   ebd0a0a2-b9e5-4433-87c0-68b6b72699c7
                    (data)
            guid:   e5f05b4e-02f5-4813-9364-c81283f2c1ec
      4     0x00096000      0x00ffffde      "root"
            attrs:  0x0000000000000000
            type:   0fc63daf-8483-4772-8e79-3d69d8477de4
                    (linux)
            guid:   a2c21296-1448-4610-8cb9-4da94983805f

To finish try a [ls] on the third (FAT32/VFAT) and the fourth (ext4) partitions:

`StarFive #`` ls mmc 1:3 `

      3146435   System.map-6.12.2-gentoo
      8144522   vmlinuz-6.12.2-gentoo

    2 file(s), 0 dir(s)

`StarFive #``ls mmc 1:4 `

    <DIR>       4096 .
    <DIR>       4096 ..
    <DIR>      16384 lost+found
    <SYM>          7 bin
    <DIR>       4096 boot
    <DIR>      12288 dev
    <DIR>       4096 etc
    <DIR>       4096 home
    <SYM>          7 lib
    <SYM>          9 lib64
    <DIR>       4096 media
    <DIR>       4096 mnt
    <DIR>       4096 opt
    <DIR>       4096 proc
    <SYM>          7 sbinBooting the device
    <DIR>       4096 root
    <DIR>       4096 run
    <DIR>       4096 tmp
    <DIR>       4096 usr
    <DIR>       4096 var

At this point the worst is behind:

1.  The board recognize the TC/SD card and can boot on it
2.  U-Boot sees what it must see

\
Last detour before heading the rest for the sake of the demonstration:

`StarFive #``fdt print /binman `

    binman ;
                                    };
                                    opensbi ;
                                    };
                                    fdt-1 ;
                                    };
                            };
                            configurations ;
                            };
                    };
            };
            spl-img ;
                    };
            };
    };

This reflects what has been written on the first two partitions of the medium (/dev/loop0p1 and /dev/loop0p2) in previous sections.

** Important**\
Do **not** use the DTB build by U-Boot! The kernel will start but will panic when spawing /sbin/init. Always use the DTB coming with the Linux kernel.

From the U-Boot shell, if no initramfs (i.e. no kernel module) is used, the following commands load and start a Linux kernel:

`StarFive #``load mmc 1:3 $fdt_addr_r jh7110-starfive-visionfive-2-v1.3b.dtb `

    38025 bytes read in 6 ms (6 MiB/s)

`StarFive #``load mmc 1:3 $kernel_addr_r Image `

    21627364 bytes read in 1316 ms (15.7 MiB/s)

`StarFive #``env set bootargs console=ttyS0,115200 rootwait earlycon=sbi root=/dev/mmcblk1p4 rw `

`StarFive #``booti $kernel_addr_r - $fdt_addr_r `

    ## Flattened Device Tree blob at 46000000
       Booting using the fdt blob at 0x46000000
    Working FDT set to 46000000
       Loading Device Tree to 00000000fe6ea000, end 00000000fe6f6488 ... OK
    Working FDT set to fe6ea000

    Starting kernel ...

    [    0.000000] Linux version 6.12.4-gentoo-r1 (root@oxygen.universe.lan) (riscv64-unknown-linux-gnu-gcc (Gentoo 14.2.1_p20241116 p3) 14.2.1 20241116, GNU ld (Gentoo 2.43 p3) 2.43.1) #2 SMP Wed Dec 18 09:55:15 EST 2024
    [    0.000000] Machine model: StarFive VisionFive 2 v1.3B
    [    0.000000] SBI specification v2.0 detected
    [    0.000000] SBI implementation ID=0x1 Version=0x10005

** Note**\
In the case of a systemd based system: messages complaining about \"failed to chase symlink\" might appear. They are harmless and can be ignored.

Once the boot process completes, a login prompt should be reached:

[`This is StarFive (Linux riscv64 6.12.4-gentoo-r1) 13:27:11`]`  `

    StarFive login:

*Et voila!* The Gentoo Linux environment on TC/SD card is fully functional, keep the image used to flash the TC/SD Card aside to allow a reproduction on demand of that Gentoo environment. Congratulations! So what\'s next?

#### [eMMC]

The microSD Card is a cheap convenient method to start with nevertheless is has an irritating aspect: the speed! It can only reaches at best around 15MB/s or so even with fast SD Cards, even with high-end UHS-II/V60 microSD cards. A much more more pleasant way to work is to use an eMMC chip which can speed things up.

The Starfive Vision Five 2 can virtually accept any brand of eMMC (Orange Pi 5 eMMC are known to work) as long as they have a single or a double B2B connector. Pay attention to the orientation: **only one of the two B2B connectors at the back of the board is wired** to the rest of the board, the other not being connected to anything (its sole goal is to reinforce the mechanical stability). Simply follow the markings on the PCB:

-   The B2B connector near the J99 label is the **live** connector
-   The B2B connector near the J9 label is the **dummy** connector (not connected to anything)

** Important**\
Ensure to correctly snap the connector in place: a click *must* be heard without putting too much force.

Now the eMMC has been put on its socket two strategies can be followed:

1.  Write from the host PC directly on the eMMC card via a eMMC/SD Card adaptator having B2B connector
2.  Transfer the content from the (functional) microSD card to the eMMc

Whatever approach is chosen it is worth noticing that, per standards, an eMMC card has two hardware partitions (they can\'t be removed) that play the very same role than the first two partitions of the SD Card (i.e. where the U-Boot SDL and U-Boot itself resides). Both have a 4 MB size and are respectively named *boot0* and *boot1* prefixed by their MMC slot name:

`root@StarFive #``lsblk `

    NAME         MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
    mmcblk1      179:0    0 59.5G  0 disk
    ├─mmcblk1p1  179:1    0    2M  0 part
    ├─mmcblk1p2  179:2    0    4M  0 part
    ├─mmcblk1p3  179:3    0  292M  0 part /boot
    └─mmcblk1p4  179:4    0 23.7G  0 part /
    mmcblk0      179:8    0  233G  0 disk
    mmcblk0boot0 179:16   0    4M  1 disk
    mmcblk0boot1 179:24   0    4M  1 disk

On the example above, [/dev/mmcblk1] is the SD Card slot whereas [/dev/mmcblk0] is the eMMC slot (default settings if the device tree has not been modified from its vanilla form). Also another block device not listed here is [/dev/mmcblk0rpmb]. That latter is known as the *Replay Protected Memory Block* (RPMB) and can be set aside for the rest of the explanations.

##### [From the SD Card to the eMMC card]

A word about those mmcblk0bootX hardware partitions before moving on: they are too short for us (4 MiB = 8192 sectors) so none of them will be used here so the process is straightforward to what has been previously shown. First things first: partition the eMMC!

`root@StarFive #``sgdisk --clear \ `

     --new=1:4096:8191    --change-name=1:"spl"    --typecode=1:2E54B353-1271-4842-806F-E436D6AF6985 \
     --new=2:8192:16383   --change-name=2:"uboot"  --typecode=2:BC13C2FF-59E6-4262-A352-B275FD6F7172 \
     --new=3:16384:614399 --change-name=3:"kernel" --typecode=3:C12A7328-F81F-11D2-BA4B-00A0C93EC93B \
     --new=4:614400:0     --change-name=:"root"    --typecode=4:0FC63DAF-8483-4772-8E79-3D69D8477DE4 \
     /dev/mmcblk0

The operation has completed successfully

Then refresh the system knowledge about their existence:

`root@StarFive #``partprobe -s /dev/mmcblk0 `

/dev/mmcblk0: gpt partitions 1 2 3 4

Dump U-Boot and its SPL loader on the first two partitions:

`root@StarFive #``dd if=/dev/mmcblk1p1 of=/dev/mmcblk0p1 oflag=sync bs=1M `

`root@StarFive #``dd if=/dev/mmcblk1p2 of=/dev/mmcblk0p2 oflag=sync bs=1M `

Now respectively create a vfat and an ext4 on the last two partitions as seen before:

`root@StarFive #``mkfs.vfat /dev/mmcblk0p3 `

`root@StarFive #``mkfs.ext4 /dev/mmcblk0p4 `

Mount both of those filesystems:

`root@StarFive #``mkdir /mnt/gentoo `

`root@StarFive #``mount /dev/mmcblk0p4 /mnt/gentoo `

`root@StarFive #``mount /dev/mmcblk0p3 /mnt/gentoo/boot `

The remaining work to do is to copy the root filesystem and the contents of [/boot]. Two options:

1.  Create a tarball on the host, copy it on a USB key then plug the USB key in one of the USB ports of the StarFive Visionfive 2 and finally *untar* the tarball (cold copy)
2.  The ugly and reckless way: rsync the live filesystems onto the eMMC (warm/hot copy) even if some files are opened (2-3 attempts can be made if rsync complains).

** Warning**\
Do **not** dump live filesystems via a **dd** command as used for copying U-Boot!

-   USB key method:
    -   Tarball creation on the host:`cd $ && tar -zcvpf rootfs-svf2.tar.gz --one-file-system rootfs`
    -   Tarball extraction on the StarFive Visionfive 2:`tar -zxvpf rootfs-20250101.tar.gz --strip-component=1 -C /mnt/gentoo rootfs.tar.gz`
-   Live filesystems copy method:
    -   On the StarFive Visionfive 2:`rsync -aH --progress --delete-before --exclude=/proc --exclude=/sys --exclude=/dev --exclude=/run --exclude=/mnt / /mnt/gentoo/`
    -   Repeat again one or two more times in case of

**Before rebooting**: check [/etc/fstab] for devices referenced as [/dev/mmcblk1pX] and change the path for [/dev/mmcblk1pX]. Then refresh the information known by systemd if applicable:

`root@StarFive #``systemctl daemon-reload `

And reboot!

`root@StarFive #``reboot `

##### [From the host to the eMMC card]

The approach is the same used for the SD Card describe a few paragraphs ago:

-   Put the eMMC card on a USB-eMMC adapter having B2B connectors
-   Partition the eMMC like hereabove for the SD Card
-   Copy the U-Boot stuff on the first two partitions
-   Copy the rootfilesystem
-   And\... reboot!

#### [Back in U-Boot shell]

Once arrived at the U-Boot shell start by ejecting the SD-Card from its slot and keep it aside in case of as a Gentoo environment is \"alive\" there. Very handy in case of the Gentoo environment residing on the eMMC would be broken for a reason or another.

Change the variable `bootargs` to make Linux use the eMMC card rather than the SD Card:

`StarFive #``env save `

Suggestion to render things a bit simpler by avoiding typing or copying/pasting the same long commands over and over again:

`StarFive #``env set load_gentoo 'load mmc 0:3 $ jh7110-starfive-visionfive-2-v1.3b.dtb; load mmc 0:3 $ vmlinuz-$; load mmc 0:3 $ initramfs-$.uimg' `

`StarFive #``env set start_gentoo 'booti $ $ $' `

`StarFive #``env save `

    Saving Environment to SPIFlash... Erasing SPI flash...Writing to SPI flash...done
    OK

Then to start Gentoo:

`StarFive #``StarFive # run load_gentoo `

`StarFive #``StarFive # run start_gentoo `

    41177 bytes read in 7 ms (5.6 MiB/s)
    6772505 bytes read in 156 ms (41.4 MiB/s)
    16228406 bytes read in 362 ms (42.8 MiB/s)
    StarFive # run start_gentoo
       Uncompressing Kernel Image to 0
    ## Loading init Ramdisk from Legacy Image at 46100000 ...
       Image Name:
       Created:      2024-12-30  23:44:17 UTC
       Image Type:   RISC-V Linux RAMDisk Image (zstd compressed)
       Data Size:    16228342 Bytes = 15.5 MiB
       Load Address: 00000000
       Entry Point:  00000000
       Verifying Checksum ... OK
    ## Flattened Device Tree blob at 46000000
       Booting using the fdt blob at 0x46000000
    Working FDT set to 46000000
       Loading Ramdisk to fd75e000, end fe6d7ff6 ... OK
       Loading Device Tree to 00000000fd750000, end 00000000fd75d0d8 ... OK
    Working FDT set to fd750000

    Starting kernel ...

    [    0.000000] Linux version 6.12.7-gentoo (root@oxygen.universe.lan) (gcc (Gentoo 14.2.1_p20241221 p6) 14.2.1 20241221, GNU ld (Gentoo 2.43 p3) 2.43.1) #2 SMP Mon Dec 30 17:41:58 EST 2024
    [    0.000000] Machine model: StarFive VisionFive 2 v1.3B
    [    0.000000] SBI specification v2.0 detected
    [    0.000000] SBI implementation ID=0x1 Version=0x10006
    [    0.000000] SBI TIME extension detected
    [    0.000000] SBI IPI extension detected
    [    0.000000] SBI RFENCE extension detected
    [    0.000000] SBI SRST extension detected
    [    0.000000] SBI DBCN extension detected
    [    0.000000] efi: UEFI not found.
    (...)

This not done yet! The boot configuration must be changed via the boot selector DIP switches.

#### [][Flip the switch!]

The very last thing to change is to flip the boot selector switches to tell the board to boot on the eMMC rather than teh SD Card. **Power the board down first!**

Once the board is unplugged from any current source simply set the following configuration for the boot selector switch:

-   RGPIO_0: Low
-   RGPIO_1: High

Remove the SD Card from the board then power the board back on (fingers crossed): the SBI startup banner should appear followed by a U-Boot shell.

Congratulations ! The Starfive Visionfive 2 is bootable and usable with only the eMMC card.

## [Troubleshooting]

### [][Kernel won\'t boot]

If the kernel will not work for unexplained reasons, and there is not any console output after it executes, rebuilding/reflashing U-boot can solve problems.

** See also**\
[StarFive VisionFive 2#Updating_the_bootloader](https://wiki.gentoo.org/wiki/StarFive_VisionFive_2#Updating_the_bootloader "StarFive VisionFive 2")

### [][SPI issues / First aid kit]

If, for one reason or another, the onboard SPI Flash memory has become corrupt, StarFive provides a recovery image at: from [https://github.com/starfive-tech/Tools/tree/master/recovery](https://github.com/starfive-tech/Tools/tree/master/recovery)

Multiple images are available, but any **jh7110** image may work.

With the board powered down, configure the boot switches for UART and start an X-modem capable console. After powering the board up again, a series of \"C\"\'s should appear, meaning that the board is waiting for a firmware image to be sent to it via the X-Modem protocol:

[`U-Boot SPL 2021.10 (Sep 28 2024 - 01:14:56 +0800)`]` `

    (C)StarFive
    CCCCCCCCCCCCCCCCCCCCC

Using Minicom, the recovery binary can be transferred with X-Modem by pressing ([Ctrl]+[A] then [S], select `xmodem`). Once the recovery image has been transferred, the board will automatically boot it. A menu is presented from where a recovery operation can be selected:

[`U-Boot SPL 2021.10 (Sep 28 2024 - 01:14:56 +0800)`]` `

    (C)StarFive
    CCCCCCCCCCCCCCCCCCCCC
    JH7110 secondboot version: 230322-c514da9
    CPU freq: 1250MHz
    idcode: 0x1860C8
    ddr 0x00000000, 4M test
    ddr 0x00400000, 8M test
    DDR clk 2133M, size 8GB

    *********************************************************
    ****************** JH7110 program tool ******************
    *********************************************************
    0: update 2ndboot/SPL in flash
    1: update 2ndboot/SPL in emmc
    2: update fw_verif/uboot in flash
    3: update fw_verif/uboot in emmc
    4: update otp, caution!!!!
    5: exit
    NOTE: current xmodem receive buff = 0x40000000, 'load 0x********' to change.
    select the function to test:

** Warning**\
Do not use option 4 (OTP) unless you understand the implications: OTP is a *One Time Programmable* aka WORM (*Write-Once Read Many*) memory. After OTP memory has been programmed (\"fused\"), it **cannot be programmed again**. OTP fuses [do not have public documentation](https://github.com/starfive-tech/Tools/issues/8).

Options [0] and [2] can be used to reprogram the onboard SPI Flash memory, while options [1] and [2] are used for an attached eMMC module.

### [][init\[1\]: unhandled signal 4 code 0x1 at (...) in ld-linux-riscv64-lp64d.so.1]

**Symptom:** the kernel starts but panics while trying to run [/sbin/init] like below

    Starting kernel ...

    sbi_trap_error: hart0: trap0: load fault handler failed (error -2)

    sbi_trap_error: hart0: trap0: mcause=0x0000000000000005 mtval=0x0000000040050088
    sbi_trap_error: hart0: trap0: mepc=0x00000000400085ca mstatus=0x0000000200001800
    sbi_trap_error: hart0: trap0: ra=0x000000004000f40e sp=0x000000004004fef0
    sbi_trap_error: hart0: trap0: gp=0x0000000000000000 tp=0x0000000040050000
    sbi_trap_error: hart0: trap0: s0=0x000000004004ff00 s1=0x0000000040050000
    sbi_trap_error: hart0: trap0: a0=0x0000000040050088 a1=0x0000000000000002
    sbi_trap_error: hart0: trap0: a2=0x0000000000000000 a3=0x0000000000000019
    (...)
    [    4.953256] EXT4-fs (mmcblk1p4): mounted filesystem 3b5a1824-0f83-49d2-a3d5-2698a6e83dd9 r/w with ordered data mode. Quota mode: disabled.
    [    4.965782] VFS: Mounted root (ext4 filesystem) on device 179:4.
    [    4.971897] devtmpfs: mounted
    [    4.978632] Freeing unused kernel image (initmem) memory: 3652K
    [    4.984674] Run /sbin/init as init process
    [    5.052665] init[1]: unhandled signal 4 code 0x1 at 0x0000003f9f9cc6dc in ld-linux-riscv64-lp64d.so.1[146dc,3f9f9b8000+20000]
    [    5.063994] CPU: 3 UID: 0 PID: 1 Comm: init Tainted: G                T  6.12.4-gentoo-r1 #2
    [    5.072429] Tainted: [T]=RANDSTRUCT
    [    5.075915] Hardware name: starfive,visionfive-2-v1.3b (DT)
    [    5.081482] epc : 0000003f9f9cc6dc ra : 0000003f9f9b90f8 sp : 0000003fc2b27760
    [    5.088699]  gp : 0000000000000000 tp : 0000000000000000 t0 : 0000000000000008
    [    5.095915]  t1 : 0000003f9f9dbe98 t2 : 0000000000000008 s0 : 0000003fc2b27e60
    [    5.103131]  s1 : 0000002ad0d9d559 a0 : 0000003fc2b27798 a1 : 0000000000000000
    [    5.110347]  a2 : 0000003fc2b279b8 a3 : 0000002ad0d9d568 a4 : 0000003f9f9db0c8
    [    5.117562]  a5 : 0000003fc2b27788 a6 : ffffffffffffffff a7 : 0000000000000030
    [    5.124778]  s2 : 0000002ad0db0408 s3 : 0000003fc2b27900 s4 : 0000003f9f9db260
    [    5.131994]  s5 : 0000003f9f9db260 s6 : 0000000000000000 s7 : 0000000000000000
    [    5.139209]  s8 : 0000000000000000 s9 : 0000000000000001 s10: 0000003f9f9d9ca0
    [    5.140462] mmc0: Failed to initialize a non-removable card
    [    5.146423]  s11: 0000003f9f9d9cc0 t3 : 0000002ad0d9d5e0 t4 : 0000003f9f9dbe90
    [    5.146431]  t5 : 000000000000003b t6 : 00000000003dd1fb
    [    5.146436] status: 0000000200000020 badaddr: 000000000000b920 cause: 0000000000000002
    [    5.146451] Code: 3423 0585 3823 0595 3c23 05a5 3023 07b5 3423 0625 (b920) bd24
    [    5.179896] Kernel panic - not syncing: Attempted to kill init! exitcode=0x00000004

-   **Cause:** The S7 HART has been used rather than one of the U74 HARTs. The U-Boot device tree does not disable the U7 HART whereas the Linux kernel one does. Consequence: the Linux kernel is booting on the S7 HART which does not support the LP64D ABI hence the traps and the subsequent kernel panic.
-   **Remedy:**
    -   Load the Linux kernel DTB [jh7110-starfive-visionfive-2-v1.3b.dtb] located in [arch/riscv/boot/dts/starfive] rather than [u-boot.dtb] from the U-Boot shell.
    -   If the above file is not present, ensure to check:

[KERNEL] **Linux DTB automatic compilation**

    Device Drivers  --->
        -*- Device Tree and Open Firmware support  --->
            [ ]   Device Tree runtime unit tests
            [*]   Build all Device Tree Blobs
            [*]   Device Tree overlays

### [][Repetitive NVMe QID timouts / reset controller]

**Symptom:** Messages similar to those below are reported on the system console / system logs:

    nvme nvme0: I/O 0 (I/O Cmd) QID 1 timeout, aborting
    nvme nvme0: I/O 0 QID 1 timeout, reset controller

-   **Causes:** Multiples causes have been reported:

1.  An instable or too \"weak\" power supply ;
2.  The NVMe is using the 512 bytes/sector format (puts a strain on the controller due to a higher number of I/O requests);

-   **Remedy:**
    -   Power supply issue: try with a \"beefier\" power supply. The Starfive Visionfive, via its USB-C port, can sustain up to 20V and is able to negociate with PD (Power Delivery) and a QC 2.0/3.0 power supplies. Refer to the [](https://doc-en.rvspace.org/VisionFive2/PDF/VisionFive2_Datasheet.pdf) section 4.1 for details;
    -   **NVMe sector size issue**: Check what LBA formats are supported and switch to a 4K profile using the `nvme` command

## [Useful notes]

Some useful notes that may be of interest to the reader can be found below.

### [Musl]

This example uses a glib libc. It is possible to use musl libc as the systems C library. The TL;DR is:

-   Use the tuple `riscv64-unknown-linux-musl` instead of `riscv64-unknown-linux-gnu` wherever crossdev is in use.
-   Obtain (or build) any lp64d musl stage3 tarball and use that.
-   Select an appropriate musl profile.

### [Faster installation]

Anywhere that QEMU-user is invoked to build a cross-arch package, using Portage within a chroot may be replaced with an external installation utilizing [crossdev](https://wiki.gentoo.org/wiki/Crossdev "Crossdev") to cross-compile binaries and portage to install them into the image as follows:

`root `[`#`]`riscv64-unknown-linux-gnu-emerge --ask sys-kernel/dracut `

`root `[`#`]`cd rootfs `

`root `[`#`]`ROOT=$PWD/ riscv64-unknown-linux-gnu-emerge --ask --usepkgonly --oneshot sys-kernel/dracut `

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

    # Common flags for cross-compiling and colour; params pulled from -march=native
    COMMON_FLAGS="-mabi=lp64d -march=rv64imafdc_zicsr_zba_zbb -mcpu=sifive-u74 -mtune=sifive-7-series -O2 -pipe -fdiagnostics-color=always -frecord-gcc-switches --param l1-cache-size=32 --param l2-cache-size=2048"

    # Enable QA messages for from iwdevtools
    PORTAGE_ELOG_CLASSES="$ qa"

### [Clearing the U-Boot environment configuration]

The configuration is stored within the QSPIFlash:

-   Start address: 0xF0000 =\> `CONFIG_ENV_OFFSET=0xF0000`
-   Length: 64KiB (65536 bytes) =\> `CONFIG_ENV_SIZE=0x10000`

\
No magic here: those values comes from the U-Boot [.config] file.

The trick is: as the QSPIFlash content is not 1:1 mapped in the CPU addressable space (only the QSPIFlash control registers are) it is required to go via the *sf* commands (instead of the *mw* command) like below:

`StarFive #``sf probe`

    SF: Detected gd25lq128 with page size 256 Bytes, erase size 4 KiB, total 16 MiB

Then:

`StarFive #``sf erase 0xf0000 0x10000`

    SF: 65536 bytes @ 0xf0000 Erased: OK

## [See also]

-   [RISC-V hardware list](https://wiki.gentoo.org/wiki/RISC-V_hardware_list "RISC-V hardware list") --- a list of **RISC-V hardware** owned by the Gentoo community within the [[#gentoo-riscv](ircs://irc.libera.chat/#gentoo-riscv)] ([[webchat](https://web.libera.chat/#gentoo-riscv)]) channel.
-   [Embedded Handbook](https://wiki.gentoo.org/wiki/Embedded_Handbook "Embedded Handbook") --- a collection of community maintained documents providing a consolidation of embedded and SoC knowledge for Gentoo.

## [External resources]

-   [All public StarFive documents archive](https://rvspace.org/en/project/Document_Publish_Status)
-   [Upstream documentation](https://doc-en.rvspace.org/Doc_Center/visionfive_2.html)
-   [Upstream build system.](https://github.com/starfive-tech/VisionFive2)
-   [Upstream kernel support tracking](https://rvspace.org/en/project/JH7110_Upstream_Plan)
-   [Andrew\'s Experimental Gentoo Image discussion on rvspace.org](https://forum.rvspace.org/t/experimental-gentoo-image/1807)
-   [Updating firmware via UART](https://forum.rvspace.org/t/guide-upgrading-firmware-with-only-a-serial-uart-connection-via-u-boot/1589)
-   [VF2 Technical Reference Manual](https://doc-en.rvspace.org/VisionFive2/PDF/VisionFive2_SW_TRM.pdf)
-   [U-Boot VF2 documentation](https://github.com/u-boot/u-boot/blob/master/doc/board/starfive/visionfive2.rst)
-   [U-Boot booting documentation](https://u-boot.readthedocs.io/en/latest/develop/bootstd.html)
-   [RISC-V Standard Extensions](https://en.wikichip.org/wiki/risc-v/standard_extensions)