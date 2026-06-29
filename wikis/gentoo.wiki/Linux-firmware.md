This page contains [[changes](https://wiki.gentoo.org/index.php?title=Linux_firmware&oldid=1421479&diff=1441928)] which are not marked for translation.

Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Linux_firmware/hu "Linux firmware (97% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Linux_firmware/ru "Прошивка Linux (82% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Linux_firmware/zh-cn "Linux 固件 (95% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Linux_firmware/ja "Linux ファームウェア (100% translated)")

**Resources**

[[]][Home](https://git.kernel.org/?p=linux/kernel/git/firmware/linux-firmware.git)

[[]][Package information](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)

Linux firmware is a package distributed alongside the Linux kernel that contains firmware [binary blobs](https://en.wikipedia.org/wiki/binary_blob "wikipedia:binary blob") necessary for partial or full functionality of certain hardware devices. These binary blobs are usually proprietary because some hardware manufacturers do not release source code necessary to build the firmware itself.

Modern graphics cards from [AMD](https://wiki.gentoo.org/wiki/AMD "AMD") and [NVIDIA](https://wiki.gentoo.org/wiki/NVIDIA "NVIDIA") almost certainly require binary blobs to be loaded for the hardware to operate correctly.

Starting at Broxton (a Skylake-based micro-architecture) [Intel CPUs](https://wiki.gentoo.org/wiki/Intel "Intel") require binary blobs for additional low-power idle states (DMC), graphics workload scheduling on the various graphics parallel engines (GuC), and offloading some media functions from the CPU to GPU (HuC).^[\[1\]](#cite_note-1)^

Additionally, modern [Intel Wi-Fi chipsets](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi") almost always require blobs.^[\[2\]](#cite_note-2)^

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
    -   [[1.4] [Optional: Savedconfig]](#Optional:_Savedconfig)
    -   [[1.5] [Optional: Compression]](#Optional:_Compression)
-   [[2] [Troubleshooting]](#Troubleshooting)
    -   [[2.1] [Searching for loaded firmware]](#Searching_for_loaded_firmware)
        -   [[2.1.1] [On kernels with Gentoo patchset]](#On_kernels_with_Gentoo_patchset)
        -   [[2.1.2] [On all kernels]](#On_all_kernels)
-   [[3] [Removal]](#Removal)
    -   [[3.1] [Unmerge]](#Unmerge)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)
-   [[6] [References]](#References)

## [Installation]

For security reasons, hotloading firmware into a running kernel has been shunned upon. Modern init systems such as [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") have strongly discouraged loading firmware from userspace.

### [Kernel]

** Warning**\
Including firmware files into binary kernel images that are not available under the terms of the GPL, may result in a violation of the GPL if the image is distributed. It is wise to consult a lawyer *before* distributing images that contain firmware files from [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]].

A few kernel options are important to consider when building in firmware support for certain devices in the Linux kernel (for kernels beginning with 4.18):

Firmware loading facility (`CONFIG_FW_LOADER`)

Build named firmware blobs into the kernel binary (`CONFIG_EXTRA_FIRMWARE`)

[KERNEL] **Enable support for Linux firmware**

    Device Drivers  --->
      Generic Driver Options  --->
        Firmware loader --->
           -*- Firmware loading facility
           ()    Build named firmware blobs into the kernel binary
           # Optional: Enable compressed firmware support
           [*]   Enable compressed firmware support
           [*]     Enable XZ-compressed firmware support
           [*]     Enable ZSTD-compressed firmware support

### [USE flags]

### [USE flags for] [sys-kernel/linux-firmware](https://packages.gentoo.org/packages/sys-kernel/linux-firmware) [[]] [Linux firmware files]

  ----------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------
  [`+initramfs`](https://packages.gentoo.org/useflags/+initramfs)               Create and install initramfs for early microcode loading in /boot (only AMD for now)
  [`+redistributable`](https://packages.gentoo.org/useflags/+redistributable)   Install also non-free (but redistributable) firmware files
  [`bindist`](https://packages.gentoo.org/useflags/bindist)                     Flag to enable or disable options for prebuilt (GRP) packages (eg. due to licensing issues)
  [`compress-xz`](https://packages.gentoo.org/useflags/compress-xz)             Compress firmware using xz (app-arch/xz-utils) before installation
  [`compress-zstd`](https://packages.gentoo.org/useflags/compress-zstd)         Compress firmware using zstd (app-arch/zstd) before installation
  [`deduplicate`](https://packages.gentoo.org/useflags/deduplicate)             Create symlinks for all firmware that is duplicate using rdfind
  [`dist-kernel`](https://packages.gentoo.org/useflags/dist-kernel)             Delegate microcode initramfs generation to sys-kernel/installkernel
  [`savedconfig`](https://packages.gentoo.org/useflags/savedconfig)             Allows individual selection of firmware files
  [`unknown-license`](https://packages.gentoo.org/useflags/unknown-license)     Install firmware files whose license is unknown
  ----------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-19 22:39] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

### [Optional: Savedconfig]

After emerging [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]], the configuration file is made into [/etc/portage/savedconfig/sys-kernel/linux-firmware-ddmmyyyy]. This file can be edited and the unwanted lines be commented out or deleted. Edit and save the file and re-emerge [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] with the [`savedconfig`](https://wiki.gentoo.org/wiki/Savedconfig "Savedconfig") USE flag:

`root `[`#`]`echo sys-kernel/linux-firmware savedconfig >> /etc/portage/package.use/kernel`

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

### [Optional: Compression]

Firmware to be loaded into the kernel can be compressed in order to achieve greater space efficiency and faster read speeds (at the expense of processing time). See the `CONFIG_FW_LOADER_COMPRESS` kernel symbol for additional information.

[[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] supports either [xz](https://wiki.gentoo.org/wiki/Xz-utils "Xz-utils") or [zstd](https://wiki.gentoo.org/wiki/Zstd "Zstd") (starting from Linux kernel 5.19^[\[3\]](#cite_note-3)^) compression via appropriate USE-flags. The kernel configuration should include `CONFIG_FW_LOADER_COMPRESS_XZ` and/or `CONFIG_FW_LOADER_COMPRESS_ZSTD` options to support these compression formats.

## [Troubleshooting]

### [Searching for loaded firmware]

#### [On kernels with Gentoo patchset]

Users who use a kernel built from [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]], [[[sys-kernel/gentoo-kernel]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel)[]], or [[[sys-kernel/gentoo-kernel-bin]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel-bin)[]] can enable the `CONFIG_GENTOO_PRINT_FIRMWARE_INFO` option to let the kernel print loaded firmware to [dmesg] output:

[KERNEL] **Let the kernel print loaded firmware**

    Gentoo Linux  --->
      [*] Print firmware information that the kernel attempts to load Search for <code>CONFIG_GENTOO_PRINT_FIRMWARE_INFO</code> to find this item.

While the kernel is running, search [dmesg] output to find what firmware has been loaded:

`root `[`#`]`dmesg | grep 'Loading firmware'`

    [    5.897583] Loading firmware: regulatory.db
    [    5.898151] Loading firmware: regulatory.db.p7s
    [    6.182140] Loading firmware: mediatek/BT_RAM_CODE_MT7922_1_1_hdr.bin
    [    6.340065] Loading firmware: i915/tgl_dmc_ver2_12.bin
    [    6.410950] Loading firmware: mediatek/WIFI_RAM_CODE_MT7922_1.bin
    [    6.490630] Loading firmware: mediatek/WIFI_MT7922_patch_mcu_1_1_hdr.bin
    [    6.505037] Loading firmware: mediatek/WIFI_RAM_CODE_MT7922_1.bin
    [    6.558260] Loading firmware: mediatek/WIFI_RAM_CODE_MT7922_1.bin

#### [On all kernels]

On every kernel, regardless of whether it has the Gentoo patchset applied, the kernel\'s [dynamic debug](//docs.kernel.org/admin-guide/dynamic-debug-howto.html) feature can be utilized to let the kernel function responsible for loading firmware [print a debug message](//git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/tree/drivers/base/firmware_loader/main.c?h=v7.0#n811) on each firmware load.

First, ensure that the kernel is configured to print a debug message for each firmware load when requested:

[KERNEL] **Enable debug messages for firmware loads**

    Kernel hacking  --->
      printk and dmesg options  --->
        [*] Enable dynamic printk() support Search for <code>CONFIG_DYNAMIC_DEBUG</code> to find this item.
    Device Drivers  --->
      Generic Driver Options  --->
        Firmware loader  --->
          -*- Firmware loading facility
          [*]   Log filenames and checksums for loaded firmware Search for <code>CONFIG_FW_LOADER_DEBUG</code> to find this item.

[Pass kernel command-line parameters](https://wiki.gentoo.org/wiki/Kernel/Command-line_parameters#Passing_parameters_to_the_kernel "Kernel/Command-line parameters") `dyndbg="func fw_log_firmware_info +p"` to the kernel, then search [dmesg] output while the kernel is running:

`root `[`#`]`dmesg | grep 'Loaded FW'`

    [    5.898144] faux_driver regulatory: Loaded FW: regulatory.db, sha256: 5560f4f0fdac7d1bb2adf8d4d083f39e3bee5ba55192feadadc091df55a813eb
    [    5.898183] faux_driver regulatory: Loaded FW: regulatory.db.p7s, sha256: 5dd27969661bed1e021ce435f535a53f201705bda14c2dba0db6353d1cdc6fff
    [    6.183756] bluetooth hci0: Loaded FW: mediatek/BT_RAM_CODE_MT7922_1_1_hdr.bin, sha256: b5dbcf0d27439db36a797203cabeb46220a8557ac488ecf69a0cfcb473b2dfa1
    [    6.346244] i915 0000:00:02.0: Loaded FW: i915/tgl_dmc_ver2_12.bin, sha256: 3c013ef0ad96ba73aee8e5bd04a8e27cc9b1c6e9183b1a83ce124485f325afca
    [    6.412646] mt7921e 0000:aa:00.0: Loaded FW: mediatek/WIFI_RAM_CODE_MT7922_1.bin, sha256: 1226f5b30531b2f027897a4a499fb77c31f4a39025c98e5a9896769aaa781fda
    [    6.491285] mt7921e 0000:aa:00.0: Loaded FW: mediatek/WIFI_MT7922_patch_mcu_1_1_hdr.bin, sha256: 6d04988f5f44fc41e9404a492291a7a519b38e6aea6369b2f939cd0c70765f5a
    [    6.506392] mt7921e 0000:aa:00.0: Loaded FW: mediatek/WIFI_RAM_CODE_MT7922_1.bin, sha256: 1226f5b30531b2f027897a4a499fb77c31f4a39025c98e5a9896769aaa781fda
    [    6.559062] mt7921e 0000:aa:00.0: Loaded FW: mediatek/WIFI_RAM_CODE_MT7922_1.bin, sha256: 1226f5b30531b2f027897a4a499fb77c31f4a39025c98e5a9896769aaa781fda

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose sys-kernel/linux-firmware`

## [See also]

-   [Fwupd](https://wiki.gentoo.org/wiki/Fwupd "Fwupd") --- a daemon that provides a safe, reliable way of applying firmware updates on Linux.
-   [Kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") --- a central part of the Gentoo [operating system (OS)](https://en.wikipedia.org/wiki/operating_system "wikipedia:operating system")
-   [Iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi") --- the wireless driver for [Intel\'s current wireless chips](https://wireless.wiki.kernel.org/en/users/drivers/iwlwifi#introduction).
-   [Microcode](https://wiki.gentoo.org/wiki/Microcode "Microcode") --- describes various ways to update a CPU\'s microcode in Gentoo.
-   [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU") --- the open source graphics drivers for AMD Radeon and other GPUs.
-   [Intel](https://wiki.gentoo.org/wiki/Intel "Intel") --- the open source graphics driver for Intel GMA on-board graphics cards and Intel iGPU and Intel Arc dedicated graphics cards, starting with the Intel 810.

## [External resources]

-   [[[bug #732852]](https://bugs.gentoo.org/show_bug.cgi?id=732852)[]]

## [References]

1.  [[[↑](#cite_ref-1)] [[https://01.org/linuxgraphics/downloads/firmware](https://01.org/linuxgraphics/downloads/firmware)]]
2.  [[[↑](#cite_ref-2)] [[https://wireless.wiki.kernel.org/en/users/drivers/iwlwifi](https://wireless.wiki.kernel.org/en/users/drivers/iwlwifi)]]
3.  [[[↑](#cite_ref-3)] [[https://lore.kernel.org/lkml/YpnwZ%2FQ5yTKRDBOD@kroah.com/T/#u](https://lore.kernel.org/lkml/YpnwZ%2FQ5yTKRDBOD@kroah.com/T/#u)]]