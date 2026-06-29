This page contains [[changes](https://wiki.gentoo.org/index.php?title=AMDGPU&oldid=1427212&diff=1442272)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/AMDGPU/de "AMDGPU (7% translated)")
-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/AMDGPU/hu "AMDGPU (96% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/AMDGPU/zh-cn "AMDGPU (18% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/AMDGPU/ja "AMDGPU (100% translated)")

**Resources**

[[]][Home](https://www.amd.com/en/support/linux-drivers)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Amdgpu "wikipedia:Amdgpu")

[[]][Issue tracker](https://gitlab.freedesktop.org/drm/amd)

**AMDGPU** is the open source graphics drivers for AMD Radeon and other GPUs.

Older Radeon cards are supported by the [radeon](https://wiki.gentoo.org/wiki/Radeon "Radeon") driver.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Prerequisites]](#Prerequisites)
        -   [[1.1.1] [Hardware detection]](#Hardware_detection)
        -   [[1.1.2] [Feature support]](#Feature_support)
    -   [[1.2] [Firmware]](#Firmware)
    -   [[1.3] [Kernel]](#Kernel)
        -   [[1.3.1] [Incorporating firmware]](#Incorporating_firmware)
            -   [[1.3.1.1] [Discovering which firmware blobs are needed]](#Discovering_which_firmware_blobs_are_needed)
            -   [[1.3.1.2] [Firmware blobs for a known card model]](#Firmware_blobs_for_a_known_card_model)
    -   [[1.4] [X11 driver]](#X11_driver)
        -   [[1.4.1] [Emerge]](#Emerge)
-   [[2] [Power management]](#Power_management)
    -   [[2.1] [Enabling DPM and PowerPlay features]](#Enabling_DPM_and_PowerPlay_features)
        -   [[2.1.1] [DPM]](#DPM)
        -   [[2.1.2] [PowerPlay feature mask]](#PowerPlay_feature_mask)
    -   [[2.2] [Configuration]](#Configuration)
        -   [[2.2.1] [Viewing current metrics]](#Viewing_current_metrics)
        -   [[2.2.2] [Update feature mask]](#Update_feature_mask)
        -   [[2.2.3] [Performance profiles]](#Performance_profiles)
        -   [[2.2.4] [Power states]](#Power_states)
        -   [[2.2.5] [Power levels]](#Power_levels)
        -   [[2.2.6] [Clock speed and voltage]](#Clock_speed_and_voltage)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Debug tools]](#Debug_tools)
        -   [[3.1.1] [x11-apps/mesa-progs]](#x11-apps.2Fmesa-progs)
        -   [[3.1.2] [sys-apps/amdgpu_top]](#sys-apps.2Famdgpu_top)
    -   [[3.2] [Identifying which graphics card is in use]](#Identifying_which_graphics_card_is_in_use)
    -   [[3.3] [Prime Synchronization]](#Prime_Synchronization)
    -   [[3.4] [Fallback driver]](#Fallback_driver)
    -   [[3.5] [Kernel]](#Kernel_2)
        -   [[3.5.1] [Older kernels]](#Older_kernels)
        -   [[3.5.2] [AMD Secure Memory Encryption]](#AMD_Secure_Memory_Encryption)
    -   [[3.6] [AMDGPU/RadeonSI drivers do not work]](#AMDGPU.2FRadeonSI_drivers_do_not_work)
    -   [[3.7] [Full-screen windows perform poorly]](#Full-screen_windows_perform_poorly)
    -   [[3.8] [GPU Name shows up as id]](#GPU_Name_shows_up_as_id)
    -   [[3.9] [Xrandr doesn\'t see HDMI port with hybrid system]](#Xrandr_doesn.27t_see_HDMI_port_with_hybrid_system)
    -   [[3.10] [Screen Tearing]](#Screen_Tearing)
    -   [[3.11] [Flickering and white screens]](#Flickering_and_white_screens)
    -   [[3.12] [Frequent and Sporadic Crashes]](#Frequent_and_Sporadic_Crashes)
    -   [[3.13] [Missing cursor on RDNA3 GPUs]](#Missing_cursor_on_RDNA3_GPUs)
-   [[4] [Tools]](#Tools)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [[] Installation]

Setting up a system to use AMDGPU requires identifying the proper card, installing the corresponding firmware, configuring the kernel, and installing the [X11 driver](https://wiki.gentoo.org/wiki/Xorg/Hardware_3D_acceleration_guide "Xorg/Hardware 3D acceleration guide").

### [[] Prerequisites]

#### [[] Hardware detection]

To choose the right driver, first detect the graphics card. Use [lspci](https://wiki.gentoo.org/wiki/Hardware_detection "Hardware detection") for this task:

`root `[`#`]`lspci | grep -i VGA`

Check the output for one of the product names listed in the table below.

#### [[] Feature support]

Video cores supported by the AMDGPU driver feature [OpenGL](https://en.wikipedia.org/wiki/OpenGL "wikipedia:OpenGL") 4.6 and [OpenGL ES](https://en.wikipedia.org/wiki/OpenGL_ES "wikipedia:OpenGL ES") 3.2. The [`VIDEO_CARDS`](https://wiki.gentoo.org/wiki/VIDEO_CARDS "VIDEO CARDS") variable must be set to `-* amdgpu radeonsi`. Via [[[media-libs/mesa]](https://packages.gentoo.org/packages/media-libs/mesa)[]] (version 20.0 or higher) the driver additionally supports [Vulkan](https://wiki.gentoo.org/wiki/Vulkan "Vulkan") (`RADV` driver) and [OpenCL](https://wiki.gentoo.org/wiki/OpenCL#AMD "OpenCL") 2.0 is available via [ROCm](https://wiki.gentoo.org/wiki/ROCm "ROCm") ([[[dev-libs/rocm-opencl-runtime]](https://packages.gentoo.org/packages/dev-libs/rocm-opencl-runtime)[]]). There is also support for [VAAPI](https://wiki.gentoo.org/wiki/VAAPI "VAAPI") via `radeonsi`.

  ------------------ --------------------------------------------- ------------------------------------------ ---------------------------- --------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Family             Chipset name                                  Microarchitecture^[\[1\]](#cite_note-1)^   ISA^[\[2\]](#cite_note-2)^   Product name                                                                                                                Notes

  Southern Islands   CAPE VERDE, PITCAIRN, TAHITI, OLAND, HAINAN   GCN1.0+                                    DCE 6.x                      HD7750-HD7970, R9 270, R9 280, R9 370X, R7 240, R7 250                                                                      Stable support since kernel 6.19.^[\[3\]](#cite_note-phoronix_Valve-Old-AMD-Linux-Love-Song-3)[\[4\]](#cite_note-phoronix_Linux-6.19-AMDGPU-GCN-1.0-1.1-4)^ Previously, optional experimental support was included since kernel 4.9-rc1 while continued stable support for GCN1.x could be found in the older [radeon](https://wiki.gentoo.org/wiki/Radeon "Radeon") driver.

  Sea Islands        BONAIRE, KABINI, MULLINS, KAVERI, HAWAII      GCN2.x                                     DCE 8.x                      HD7790, R7 260, R9 290, R7 360, R9 390                                                                                      Stable support since kernel 6.19.^[\[3\]](#cite_note-phoronix_Valve-Old-AMD-Linux-Love-Song-3)[\[4\]](#cite_note-phoronix_Linux-6.19-AMDGPU-GCN-1.0-1.1-4)^ Previously, support in the kernel was optional and had to be activated with `DRM_AMDGPU_CIK=y`. Also, the older [radeon](https://wiki.gentoo.org/wiki/Radeon "Radeon") driver provides stable support for Sea Islands (GCN2.x) cards.

  Volcanic Islands   CARRIZO, FIJI, STONEY, TONGA, TOPAZ, WANI     GCN3.x                                     DCE 10/11.x                  R9 285, R9 380, R9 380X, R9 Fury, R9 Nano, R9 Fury X, Pro Duo                                                               Supported since kernel 4.7-rc6.

  Arctic Islands     POLARIS10/11/12, VEGAM                        GCN4.x                                     DCE 11.2                     RX 460, RX 470, RX 480, RX 540, RX 550, RX 560, RX 570, RX 580, RX 590, Pro WX 3200                                         Requires kernel 4.15 or newer.

  Vega               VEGA10/11/12/20                               GCN5.x                                     DCE 12.x                     RX Vega 56, RX Vega 64, Radeon Vega II, Radeon VII                                                                          Requires kernel 4.15 or newer.

  Vega               RAVEN                                         GCN5.x                                     DCN 1.0                      Raven Ridge APU series                                                                                                      Requires kernel 4.16 or newer.^[\[5\]](#cite_note-5)[\[6\]](#cite_note-6)^

  Vega               RENOIR                                        GCN5.x                                     DCN 2.1                      Renoir, Lucienne, and Cezanne APU series

  Navi               NAVI10/12/14                                  RDNA                                       DCN 2.0                      RX 5500, RX 5500 XT, RX 5600, RX 5600 XT, RX 5700, RX 5700 XT                                                               Requires kernel 5.3, Mesa 19.2 and LLVM 9.0 or newer.^[\[7\]](#cite_note-amd-navi-7)^

  Navi               NAVI21/22/23/24                               RDNA2                                      DCN 3.0                      RX 6500 XT, RX 6600, RX 6600 XT, RX 6650 XT, RX 6700, RX 6700 XT, RX 6750 XT, RX 6800, RX 6800 XT, RX 6900 XT, RX 6950 XT   RX 6\*00 series supported since kernel 5.9.12 with `CONFIG_DRM_AMD_DC_DCN3_0=Y`.^[\[8\]](#cite_note-8)[\[9\]](#cite_note-9)^

  Navi               NAVI31/32/33                                  RDNA 3                                     DCN 3.2                      RX 7000 series                                                                                                              Requires kernel 6.0 and Mesa 22.2 or newer.^[\[10\]](#cite_note-10)^

  Navi               PHOENIX                                       RDNA 3                                     DCN 3.1.4                    Phoenix Point APU series                                                                                                    e.g. Ryzen 5 7540U and 8740U, Ryzen 5 7640U/HS, Ryzen 7 7840U/H/HS and 7940HS, Ryzen 7 8700G

  Navi               STRIX                                         RDNA 3.5                                   DCN 3.5                      Strix Point APU series                                                                                                      Also called *RDNA 3+* or *RDNA3 refresh*, requires kernel 6.10 and Mesa 24.1 or newer.^[\[11\]](#cite_note-11)[\[12\]](#cite_note-12)^\
                                                                                                                                                                                                                                                                       e.g. Ryzen AI 9 365/HX 370

  Navi               NAVI44/48                                     RDNA 4                                     DCN 3.2                      RX 9060, RX 9060 XT, RX 9070, RX 9070 XT                                                                                    Requires kernel 6.12 LTS and at least Mesa 25.0 (24.3 will also work, but with some bugs).^[\[13\]](#cite_note-13)^ Kernel 6.15^[\[14\]](#cite_note-14)^ and Mesa 25.1^[\[15\]](#cite_note-15)^ or newer recommended. For Vulkan AMDVLK 2025.Q1.3 or newer is needed.^[\[16\]](#cite_note-16)^
  ------------------ --------------------------------------------- ------------------------------------------ ---------------------------- --------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [[] Firmware]

It is necessary to install the proper firmware (or microcode) for the card. Firmware files are provided by [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]].

There are two main approaches to loading firmware:

1.  Build AMDGPU as a module and simply have [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] installed (the firmware will be loaded at runtime),
2.  Build AMDGPU *and the required firmware* into the kernel (the firmware will be loaded at build time).

\
The easiest approach is to do 1 first then, if you wish, figure out which firmware blobs you need and do 2.

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

If using the [savedconfig](https://wiki.gentoo.org/wiki/Savedconfig "Savedconfig") USE flag, make sure all necessary files for the hardware is in the configuration file. If in doubt, disable savedconfig until you know what you need.

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

The firmware files installed this way will be incorporated into the kernel.

** Note**\
Navi10 cards (RX 5700, RX 5700XT \[FE\]) require at least version 20190923 of [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]].

### [[] Kernel]

** Note**\
The easiest way of installation is to choose \"AMD GPU\" as a module (M) and to **not** have it included in an [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs"). This will load the driver a little later once udev becomes active and the firmware will never need to be manually managed in this case. Otherwise carefully read the *[Incorporating firmware](https://wiki.gentoo.org/wiki/AMDGPU#Incorporating_firmware "AMDGPU")* section below.

Set the following kernel options for the graphic chipsets mentioned above:

[KERNEL] **Configuring the kernel for AMD graphics (Linux kernels 4.15 and newer)**

    Processor type and features  --->
        [*] MTRR (Memory Type Range Register) support Search for <code>CONFIG_MTRR</code> to find this item.
    Memory Management options  --->
        [*] Memory hotplug Search for <code>CONFIG_MEMORY_HOTPLUG</code> to find this item.  --->
        [*]   Allow for memory hot remove Search for <code>CONFIG_MEMORY_HOTREMOVE</code> to find this item.
        [*] Device memory (pmem, HMM, etc...) hotplug support Search for <code>CONFIG_ZONE_DEVICE</code> to find this item.
        [*] Unaddressable device memory (GPU memory, ...) Search for <code>CONFIG_DEVICE_PRIVATE</code> to find this item.
    Device Drivers  --->
        [*] PCI support Search for <code>CONFIG_PCI</code> to find this item.  --->
            [*] PCIE Express Port Bus support Search for <code>CONFIG_PCIEPORTBUS</code> to find this item.  --->
                [*] PCIE Express Hotplug driver Search for <code>CONFIG_HOTPLUG_PCI_PCIE</code> to find this item.
        Graphics support  --->
            <*/M> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support) Search for <code>CONFIG_DRM</code> to find this item. --->
                Supported DRM clients  --->
                    [*] Enable legacy fbdev support for your modesetting driver Search for <code>CONFIG_DRM_FBDEV_EMULATION</code> to find this item.
                < > ATI Radeon Search for <code>CONFIG_DRM_RADEON</code> to find this item.
                <M/*> AMD GPU Search for <code>CONFIG_DRM_AMDGPU</code> to find this item.
                [ /*]   Enable amdgpu support for SI parts Search for <code>CONFIG_DRM_AMDGPU_SI</code> to find this item.
                        (only needed for Southern Islands GPUs with the amdgpu driver)
                [ /*]   Enable amdgpu support for CIK parts Search for <code>CONFIG_DRM_AMDGPU_CIK</code> to find this item.
                        (only needed for Sea Islands GPUs with the amdgpu driver)
                        ACP (Audio CoProcessor) Configuration  --->
                            [*] Enable AMD Audio CoProcessor IP support Search for <code>CONFIG_DRM_AMD_ACP</code> to find this item.
                                (only needed for APUs)
                        Display Engine Configuration  --->
                            [*] AMD DC - Enable new display engine Search for <code>CONFIG_DRM_AMD_DC</code> to find this item.
                            [ /*] AMD DC support for Southern Islands ASICs Search for <code>CONFIG_DRM_AMD_DC_SI</code> to find this item.
                [*] HSA kernel driver for AMD GPU devices Search for <code>CONFIG_HSA_AMD</code> to find this item.
                [*]   Enable HMM-based shared virtual memory manager Search for <code>CONFIG_HSA_AMD_SVM</code> to find this item.
        <*/M> Sound card support Search for <code>CONFIG_SOUND</code> to find this item.  --->
            <*/M> Advanced Linux Sound Architecture Search for <code>CONFIG_SND</code> to find this item.  --->
                [*] PCI sound devices Search for <code>CONFIG_SND_PCI</code> to find this item. --->
                    HD-Audio  --->
                        <*> HD Audio PCI Search for <code>CONFIG_SND_HDA_INTEL</code> to find this item.
                        [ /*] Support initialization patch loading for HD-audio Search for <code>CONFIG_SND_HDA_PATCH_LOADER</code> to find this item.
                        [ /*] Use the device identifier field for controls Search for <code>CONFIG_CONFIG_SND_HDA_CTL_DEV_ID</code> to find this item.
                        (2048)   Pre-allocated buffer size for HD-audio driver Search for <code>CONFIG_SND_HDA_PREALLOC_SIZE</code> to find this item.
                        <*> Build whatever audio codec your soundcard needs codec support
                        <*/M> HD-audio HDMI codec support Search for <code>CONFIG_SND_HDA_CODEC_HDMI</code> to find this item.

** Note**\
Some older graphics cards are supported by both the [amdgpu] and the [[radeon](https://wiki.gentoo.org/wiki/Radeon "Radeon")] kernel module. When using AMDGPU, it is recommended to **unset** the ATI Radeon option so that the [radeon] module is not built, or alternatively, to [blacklist](https://wiki.gentoo.org/wiki/Kernel_Modules#Blacklist "Kernel Modules") the [radeon] module (after rebooting check with [lsmod \| grep radeon] to see if the blacklisting worked). The two modules are not meant to be loaded simultaneously, unless for specific systems that require it, e.g. for [multiseat](https://wiki.gentoo.org/wiki/Multiseat "Multiseat") configurations.

The options from the Sound card support menu need only to be set if the card supports HDMI or DisplayPort audio and its use is desired. On newer kernels where Enable AMD Audio CoProcessor IP support appears, that should also be set.

AMDGPU with Display Core was first implemented for VEGA10 (GCN5.0) and RAVEN (with DCN 1.0) GPUs/APUs. Kernels before version 4.17 have (experimental) DC support for older cards (GCN1.1 and newer) via command line option `amdgpu.dc=1`, which may work better than the older radeon kernel module. Likewise, if DC needs to be disabled for any particular reason, option `amdgpu.dc=0` can be used on the kernel command line.

See the [radeon](https://wiki.gentoo.org/wiki/Radeon "Radeon") article for more details about using HDMI/DisplayPort audio.

#### [[] Incorporating firmware]

The firmware package installed in [an earlier section](https://wiki.gentoo.org/wiki/AMDGPU#Firmware "AMDGPU") provides files in [/lib/firmware/amdgpu] (for Volcanic Islands and newer cards) and/or [/lib/firmware/radeon] (for Southern Islands and Sea Islands cards). AMDGPU must be able to access the correct firmware files when it is loaded.

** Important**\
If the `amdgpu` module is compiled as a loadable kernel module (i.e. AMDGPU in the kernel configuration is set to `M`), the firmware files need to be accessible at the time it is loaded. In particular, if the module is loaded from an initrd/[initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs"), the kernel will initialize it during early boot, just like when the module is built into the kernel directly (i.e. AMDGPU in the kernel configuration is set to `*`). For the firmware files to be accessible at this stage they need to be either included in the initrd/initramfs (which needs to be loaded by the bootloader, e.g. [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB")) or included directly in the kernel image.

[KERNEL] **Including firmware in the kernel (4.18 and later)**

    Device Drivers  --->
        Generic Driver Options --->
            Firmware loader  --->
                [*] Firmware loading facility Search for <code>CONFIG_FW_LOADER</code> to find this item.
                (amdgpu/<YOUR-MODEL>.bin or radeon/<YOUR-MODEL>.bin) External firmware blobs to build into the kernel binary Search for <code>CONFIG_EXTRA_FIRMWARE</code> to find this item.
                (/lib/firmware) Firware blobs root directory Search for <code>CONFIG_EXTRA_FIRMWARE_DIR</code> to find this item.

** Note**\
With [[[sys-kernel/genkernel]](https://packages.gentoo.org/packages/sys-kernel/genkernel)[]] \> 4.0 it is easily possible to include specified firmware files in an [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs"). Refer to the [Firmware loading](https://wiki.gentoo.org/wiki/Genkernel#Firmware_loading "Genkernel") section of the [genkernel](https://wiki.gentoo.org/wiki/Genkernel "Genkernel") article. Likewise, with [Dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut") it is also easily possible to [add files to the image](https://wiki.gentoo.org/wiki/Dracut#Adding_files_to_the_image "Dracut").

** Important**\
Kernel 4.19.9^[\[17\]](#cite_note-17)^ (Dec. 2018) requires a different (older) set of firmware files than listed here in order to boot successfully. For all current kernels it is recommended to always make sure that [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] is updated.

In the case that the firmware needs to be included in the kernel or in an [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs"), and if using the savedconfig USE flag for [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]], make sure that the savedconfig configuration file is updated with a changed set of firmware files as well (like the change in 2018 mentioned above). Incorporate all the newly added files to the kernel configuration file in the firmware line, then rebuild and install the new kernel image. Otherwise boot will likely fail with a blank screen and firmware load errors thrown to the kernel log.

It is important you include all the firmware blobs that are needed by the driver. The required blobs can either be determined by a discovery approach or, if you know your card model, using the table in [the next section](https://wiki.gentoo.org/wiki/AMDGPU#Known_firmware_blobs "AMDGPU").

##### [[] Discovering which firmware blobs are needed]

In the case you are unsure which blobs are needed, a trial and error method often leads to success. In a multi-step process a basic bootable system may suffice to get the required information: missing firmware is indicated by an amdgpu error in dmesg, which helps to identify the required firmware files.

** Note**\
This method will, without any firmware files, very likely result in a blank screen since the AMDGPU driver doesn\'t work properly without firmware. A very basic method to still get the required information is to type in the blind and save the dmesg output into a file, which can be analyzed when rebooting without the AMDGPU driver in use. A better choice might be to intermittently include all the firmware as in `amdgpu/*` since dmesg normally shows which firmware was loaded tied to `CONFIG_GENTOO_PRINT_FIRMWARE_INFO=y` being set in the kernel [.config], *or* to force the use of another framebuffer driver (like vesafb or efifb).

`root `[`#`]`dmesg -t | grep amdgpu | grep firmware`

    amdgpu 0000:07:00.0: Direct firmware load for amdgpu/green_sardine_sdma.bin failed with error -2
    [drm:sdma_v4_0_early_init] *ERROR* sdma_v4_0: Failed to load firmware "amdgpu/green_sardine_sdma.bin"
    amdgpu 0000:07:00.0: Direct firmware load for amdgpu/green_sardine_asd.bin failed with error -2

`root `[`#`]`dmesg -t | grep amdgpu | grep firmware `

    Loading firmware: amdgpu/green_sardine_sdma.bin
    Loading firmware: amdgpu/green_sardine_asd.bin
    Loading firmware: amdgpu/green_sardine_ta.bin
    Loading firmware: amdgpu/green_sardine_pfp.bin
    Loading firmware: amdgpu/green_sardine_me.bin
    Loading firmware: amdgpu/green_sardine_ce.bin
    Loading firmware: amdgpu/green_sardine_rlc.bin
    Loading firmware: amdgpu/green_sardine_mec.bin
    Loading firmware: amdgpu/green_sardine_dmcub.bin
    Loading firmware: amdgpu/green_sardine_vcn.bin

** Important**\
The following will only work when [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] is installed and the required (but in the example above missing) firmware is actually available. For very new graphics cards the firmware may be included in the unstable package, which can be installed using `~` in [ACCEPT_KEYWORDS](https://wiki.gentoo.org/wiki/ACCEPT_KEYWORDS "ACCEPT KEYWORDS"), e.g. `~amd64` like in [ACCEPT_KEYWORDS=\"\~amd64\" emerge \--ask sys-kernel/linux-firmware] or by adding it to [/etc/portage/package.accept_keywords].

The way the AMDGPU firmware files are named, all files starting with the GPU model code name are the right firmware blobs to include. In the above example the code name is \"Green Sardine\", thus this command looking for `green_sardine` will get the required list for `CONFIG_EXTRA_FIRMWARE`:

`user `[`$`]`ls /lib/firmware/amdgpu/green_sardine*.bin | sed 's/\/lib\/firmware\///' | echo $(cat) `

    amdgpu/green_sardine_asd.bin amdgpu/green_sardine_ce.bin amdgpu/green_sardine_dmcub.bin amdgpu/green_sardine_me.bin amdgpu/green_sardine_mec2.bin amdgpu/green_sardine_mec.bin amdgpu/green_sardine_pfp.bin amdgpu/green_sardine_rlc.bin amdgpu/green_sardine_sdma.bin amdgpu/green_sardine_ta.bin amdgpu/green_sardine_vcn.bin

** Note**\
If using [genkernel](https://wiki.gentoo.org/wiki/Genkernel "Genkernel"), refer to the [Firmware loading](https://wiki.gentoo.org/wiki/Genkernel#Firmware_loading "Genkernel") section there. If using [Dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut"), refer to the [Adding files to the image](https://wiki.gentoo.org/wiki/Dracut#Adding_files_to_the_image "Dracut") section.

##### [[] Firmware blobs for a known card model]

If you know what card model you have then this section will tell you which blobs you need.

`amdgpu/<YOUR-MODEL>.bin` or `radeon/<YOUR-MODEL>.bin` should be replaced with the full list of filenames given with the chipset\'s name in the table below, separated by spaces. Use [echo] to expand the filenames. E.g. for Volcanic Islands/TONGA, run:

`user `[`$`]`echo amdgpu/tonga_.bin`

    amdgpu/tonga_ce.bin amdgpu/tonga_k_smc.bin amdgpu/tonga_mc.bin amdgpu/tonga_me.bin amdgpu/tonga_mec2.bin amdgpu/tonga_mec.bin amdgpu/tonga_pfp.bin amdgpu/tonga_rlc.bin amdgpu/tonga_sdma1.bin amdgpu/tonga_sdma.bin amdgpu/tonga_smc.bin amdgpu/tonga_uvd.bin amdgpu/tonga_vce.bin

Then `amdgpu/tonga_ce.bin amdgpu/tonga_k_smc.bin amdgpu/tonga_mc.bin amdgpu/tonga_me.bin amdgpu/tonga_mec2.bin amdgpu/tonga_mec.bin amdgpu/tonga_pfp.bin amdgpu/tonga_rlc.bin amdgpu/tonga_sdma1.bin amdgpu/tonga_sdma.bin amdgpu/tonga_smc.bin amdgpu/tonga_uvd.bin amdgpu/tonga_vce.bin` is the string that should be put into the kernel configuration.

After expanding the firmware file names from the following table and copying them into the kernel configuration, save the configuration, then compile and install the new kernel and modules.

  -------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Chipset name   Firmware
  CAPE VERDE     [radeon/verde\_.bin radeon/TAHITI\_.bin]
  PITCAIRN       [radeon/pitcairn\_.bin radeon/TAHITI\_.bin]
  TAHITI         [radeon/tahiti\_.bin]
  OLAND          [amdgpu/oland\_.bin]
  HAINAN         [radeon/hainan\_.bin radeon/TAHITI_uvd.bin]
  BONAIRE        [radeon/bonaire\_.bin]
  KABINI         [radeon/kabini\_.bin]
  KAVERI         [radeon/kaveri\_.bin]
  HAWAII         [amdgpu/hawaii\_.bin]
  MULLINS        [radeon/mullins\_.bin]
  CARRIZO        [amdgpu/carrizo\_.bin]
  FIJI           [amdgpu/fiji\_.bin]
  TONGA          [amdgpu/tonga\_.bin]
  TOPAZ          [amdgpu/topaz\_.bin]
  STONEY         [amdgpu/stoney\_.bin]
  POLARIS10      [amdgpu/polaris10\_.bin]
  POLARIS11      [amdgpu/polaris11\_.bin]
  POLARIS12      [amdgpu/polaris12\_.bin]
  VEGA10         [amdgpu/vega10\_.bin]
  RAVEN          [amdgpu/raven\_.bin]
  VEGA12         [amdgpu/vega12\_.bin]
  RENOIR         [amdgpu/renoir\_.bin]
  CEZANNE        [amdgpu/green_sardine\_.bin]
  REMBRANDT      [amdgpu/yellow_carp\_.bin]
  NAVI10         [amdgpu/navi10\_.bin]
  NAVI14         [amdgpu/navi14\_.bin]
  NAVI21         [amdgpu/sienna_cichlid\_.bin]
  NAVI22         [amdgpu/navy_flounder\_.bin]
  NAVI23         [amdgpu/dimgrey_cavefish\_.bin]
  NAVI24         [amdgpu/beige_goby\_.bin]
  NAVI31         [amdgpu/gc_11_0_0\_.bin amdgpu/psp_13_0_0\_.bin amdgpu/smu_13_0_0.bin amdgpu/dcn_3_2_0_dmcub.bin amdgpu/sdma_6_0_0.bin amdgpu/vcn_4_0_0.bin]
  NAVI32         [amdgpu/dcn_3_2_0_dmcub.bin amdgpu/gc_11_0_3\_.bin amdgpu/psp_13_0_10\_.bin amdgpu/sdma_6_0_3.bin amdgpu/smu_13_0_10.bin amdgpu/vcn_4_0_0.bin]
  NAVI33         [amdgpu/dcn\_\_dmcub.bin amdgpu/gc_10_3_6\_.bin amdgpu/gc_11_0_2\_.bin amdgpu/psp_13_0_5\_.bin amdgpu/psp_13_0_7\_.bin amdgpu/sdma\_.bin amdgpu/smu_13_0_7.bin amdgpu/vcn\_.bin]
  STRIX          [amdgpu/psp_14_0_1\_.bin amdgpu/dcn_3_5_1_dmcub.bin amdgpu/gc_11_5_1.bin amdgpu/sdma_6_1_1.bin amdgpu/vcn\_.bin amdgpu/gc_11_5_1\_.bin]
  NAVI44         [amdgpu/dcn_4_0_1_dmcub.bin amdgpu/gc_12_0_0\_.bin amdgpu/psp_14_0_2\_.bin amdgpu/sdma_7_0_0.bin amdgpu/smu_14_0_2.bin amdgpu/vcn_5_0_0.bin]
  NAVI48         [amdgpu/dcn_4_0_1_dmcub.bin amdgpu/gc_12_0_1\_.bin amdgpu/psp_14_0_3\_.bin amdgpu/sdma_7_0_1.bin amdgpu/smu_14_0_3.bin amdgpu/vcn_5_0_0.bin]
  -------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [[] X11 driver]

#### [[] Emerge]

Portage uses the [`VIDEO_CARDS`](https://wiki.gentoo.org/wiki/VIDEO_CARDS "VIDEO CARDS") [USE_EXPAND](https://wiki.gentoo.org/wiki/USE_EXPAND "USE EXPAND") variable for enabling support for various graphics cards in packages. Setting `VIDEO_CARDS` to `-* amdgpu radeonsi` (see the [feature matrix](https://wiki.gentoo.org/wiki/AMDGPU#Feature_support "AMDGPU") section above) and asking Portage to update changed USE flags in the [\@world set](https://wiki.gentoo.org/wiki/World_set_(Portage) "World set (Portage)") will pull in the correct driver:

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* amdgpu radeonsi

** Note**\
All AMD video cards supported by `amdgpu` require `video_cards_radeonsi` to enable OpenGL support provided by [[[media-libs/mesa]](https://packages.gentoo.org/packages/media-libs/mesa)[]]. This adds a hard-dependency on [[[x11-libs/libdrm]](https://packages.gentoo.org/packages/x11-libs/libdrm)[]] with `video_cards_radeon` enabled, which may be satisfied via [/etc/portage/package.use](https://wiki.gentoo.org/wiki//etc/portage/package.use "/etc/portage/package.use") if support for the old `radeon` kernel driver is not desired.

`root `[`#`]`emerge --ask --deep --changed-use @world`

The system should now be prepared to use amdgpu after the next reboot.

## [[] Power management]

** Note**\
This section only covers the newer AMDGPU Dynamic Power Management (DPM) methods (beginning from Radeon HD 2000 series / r600). Older dynpm and profile methods can be found on the [radeon](https://wiki.gentoo.org/wiki/Radeon#Power_management "Radeon") wiki page.

Dynamic Power Management (DPM) is a technique that allows for the driver to dynamically adjust the core clock frequency, memory clock frequency, and voltage levels based on the current GPU demand. Since kernel 3.13, DPM is enabled by default for a majority of AMD hardware.^[\[18\]](#cite_note-18)^

AMDGPU supports [PowerPlay](https://en.wikipedia.org/wiki/AMD_PowerPlay "wikipedia:AMD PowerPlay") profiles. These profiles replaced the `power_dpm_state` on newer hardware.

** Important**\
The following sections assume that card0 is the GPU users want to adjust. Identify the correct card number listed in [/sys/class/drm/] and modify the commands accordingly.

To check if the system is using PowerPlay, review the contents of the devices\'s sysfs directory:

`user `[`$`]`ls /sys/class/drm/card0/device/pp_*`

Any files returned with the `pp_` prefix indicate PowerPlay is implemented by the drivers.

** Warning**\
The \'files\' in [/sys/class/drm/card0/device/] expose low-level graphics APIs. Changing their contents requires specific command operations and may irrevocably damage system hardware.^[\[19\]](#cite_note-19)^

### [[] Enabling DPM and PowerPlay features]

#### [[] DPM]

The following kernel parameter can be used to explicitly enable (1) or disable (0) DPM. The default is -1 (auto)^[\[20\]](#cite_note-20)^.

[CODE] **Enable DPM**

    amdgpu.dpm=1

#### [[] PowerPlay feature mask]

** Note**\
Enabling DPM also appears to enable PowerPlay, if it is supported, as the kernel parameter `amdgpu.powerplay` has not been documented since kernel 4.5^[\[21\]](#cite_note-21)^.

The PowerPlay feature mask kernel parameter overrides display features of the GPU. It is required to unlock access to adjust clocks and voltages in sysfs. The mask consists of 32 bits, currently there are 20 features implemented^[\[22\]](#cite_note-22)^. The default is the current set of stable display features^[\[23\]](#cite_note-23)^.

[CODE] **kernel:root/drivers/gpu/drm/amd/include/amd_shared.h**

    * @PP_SCLK_DPM_MASK: Dynamic adjustment of the system (graphics) clock.
    * @PP_MCLK_DPM_MASK: Dynamic adjustment of the memory clock.
    * @PP_PCIE_DPM_MASK: Dynamic adjustment of PCIE clocks and lanes.
    * @PP_SCLK_DEEP_SLEEP_MASK: System (graphics) clock deep sleep.
    * @PP_POWER_CONTAINMENT_MASK: Power containment.
    * @PP_UVD_HANDSHAKE_MASK: Unified video decoder handshake.
    * @PP_SMC_VOLTAGE_CONTROL_MASK: Dynamic voltage control.
    * @PP_VBI_TIME_SUPPORT_MASK: Vertical blank interval support.
    * @PP_ULV_MASK: Ultra low voltage.
    * @PP_ENABLE_GFX_CG_THRU_SMU: SMU control of GFX engine clockgating.
    * @PP_CLOCK_STRETCH_MASK: Clock stretching.
    * @PP_OD_FUZZY_FAN_CONTROL_MASK: Overdrive fuzzy fan control.
    * @PP_SOCCLK_DPM_MASK: Dynamic adjustment of the SoC clock.
    * @PP_DCEFCLK_DPM_MASK: Dynamic adjustment of the Display Controller Engine Fabric clock.
    * @PP_OVERDRIVE_MASK: Over- and under-clocking support.
    * @PP_GFXOFF_MASK: Dynamic graphics engine power control.
    * @PP_ACG_MASK: Adaptive clock generator.
    * @PP_STUTTER_MODE: Stutter mode.
    * @PP_AVFS_MASK: Adaptive voltage and frequency scaling.
    * @PP_GFX_DCS_MASK: GFX Async DCS.

Determine the current system mask:

`user `[`$`]`printf 'amdgpu.ppfeaturemask=0x%x\n' "$(($(cat /sys/module/amdgpu/parameters/ppfeaturemask)))" `

    amdgpu.ppfeaturemask=0x0007bfff

Features may be changed by setting the kernel parameter at boot.

[CODE] **Set PowerPlay mask**

    amdgpu.ppfeaturemask=0x0007bfff

** Note**\
Setting all 32 bits (`0xffffffff`) is not recommended as this will enable potentially unstable features by default.

** Warning**\
Enabling or disabling features without understanding their intent may lead to hardware damage or data loss.

** Note**\
On recent kernels like v6.14 (or those that contain commit [b472b8d829c1](https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/commit/?id=b472b8d829c1562c5597c1f212957b6b2696d40e)), the CPU will be tainted as being out-of-spec if overdrive is enabled.

### [[] Configuration]

** Warning**\
Some of these instructions interface directly with the hardware and have the potential to irreversibly damage the device. Proofread the commands before executing.

AMDGPU handles configuration of the hardware through exposed APIs, using sysfs files located in [/sys/class/drm/card0/device/]. The files contained within this directory will depend on the specific hardware and features that are enabled. Some of the files can be safely read by the user using `cat`, `less`, or any other non-root text editing program. Although, many of the files output binary data that is not human readable.

Adjusting the clock rates and voltages (under/over clocking) is accomplished through the DPM and PowerPlay APIs. The full documentation can be found at [kernel.org](https://www.kernel.org/doc/html/latest/gpu/amdgpu/thermal.html) and should be reviewed before proceeding.

#### [[] Viewing current metrics]

The amdgpu driver provides a sysfs API for retrieving current gpu metrics data through the `gpu_metrics` file and gives a snapshot of all sensors at the same time. This include temperature, frequency, engines utilization, power consume, throttler status, fan speed and cpu core statistics (available for APU only).

It can be parsed using a script such as [amdgpu_metrics.py](https://gist.github.com/leuc/e45f4dc64dc1db870e4bad1c436228bb)

#### [[] Update feature mask]

Before any parameters can be adjusted, the correct feature mask must be set with a kernel parameter. Generally, setting the PP_OVERDRIVE_MASK bit `0x4000` in combination with the system\'s current mask is sufficient for adjusting the profile, clock, and voltage values.

Determine the new system mask.

`user `[`$`]`printf 'amdgpu.ppfeaturemask=0x%x\n' "$(($(cat /sys/module/amdgpu/parameters/ppfeaturemask) | 0x4000))" `

    amdgpu.ppfeaturemask=0x0007ffff

Update kernel parameter.

[CODE] **kernel parameter: PowerPlay feature mask**

    amdgpu.ppfeaturemask=0x0007ffff

#### [[] Performance profiles]

The amdgpu driver provides a sysfs API for adjusting certain power related parameters. The file `power_dpm_force_performance_level` is used for this. A full description of the profiles can be found in the [kernel documentation](https://www.kernel.org/doc/html/latest/gpu/amdgpu/thermal.html#power-dpm-force-performance-level). The default is set to \'auto\'.

The performance profile must be set to manual to enable modification of power profiles, clock speeds, and voltages.

To change the current profile:

`root `[`#`]`echo 'manual' > /sys/class/drm/card0/device/power_dpm_force_performance_level`

** Note**\
These changes do not persist after a reboot.

#### [[] Power states]

The amdgpu driver provides a sysfs API for adjusting the heuristics related to switching between power levels in a power state. The file `pp_power_profile_mode` is used for this. A full description of the profiles can be found in the [kernel documentation](https://www.kernel.org/doc/html/latest/gpu/amdgpu/thermal.html#pp-power-profile-mode).

To view the supported profiles look at the contents of the `pp_power_profile_mode` file (the asterisk \* shows the current profile)

** Note**\
The output of this command will vary depending on the specific hardware and kernel drivers.

`user `[`$`]`cat /sys/class/drm/card0/device/pp_power_profile_mode `

    PROFILE_INDEX(NAME) CLOCK_TYPE(NAME) FPS MinFreqType MinActiveFreqType MinActiveFreq BoosterFreqType BoosterFreq PD_Data_limit_c PD_Data_error_coeff PD_Data_error_rate_coeff
     0 BOOTUP_DEFAULT :
                        0(       GFXCLK)       0       5       1       0       4     800 4587520  -65536       0
                        1(       SOCCLK)       0       5       1       0       1       0 3276800   -6553   -6553
                        2(        MEMLK)       0       5       1       0       4     800  327680  -65536       0
     1 3D_FULL_SCREEN :
                        0(       GFXCLK)       0       5       1       0       4     650 4587520   -3276  -65536
                        1(       SOCCLK)       0       5       1       0       1       0  655360   -6553   -6553
                        2(        MEMLK)       0       5       4     850       4     800  327680  -65536       0
     2   POWER_SAVING :
                        0(       GFXCLK)       0       5       1       0       3       0 5898240  -65536       0
                        1(       SOCCLK)       0       5       1       0       1       0 3407872   -6553   -6553
                        2(        MEMLK)       0       5       1       0       3       0 1966080  -65536       0
     3          VIDEO*:
                        0(       GFXCLK)       0       5       1       0       4     500 4587520  -65536       0
                        1(       SOCCLK)       0       5       1       0       1       0 3473408   -6553   -6553
                        2(        MEMLK)       0       5       1       0       4     500 1966080  -65536       0
     4             VR :
                        0(       GFXCLK)       0       5       4    1000       1       0 3932160       0       0
                        1(       SOCCLK)       0       5       1       0       1       0  655360   -6553   -6553
                        2(        MEMLK)       0       5       1       0       4     800  327680  -65536       0
     5        COMPUTE :
                        0(       GFXCLK)       0       5       4    1000       1       0 3932160       0       0
                        1(       SOCCLK)       0       5       1       0       1       0  655360   -6553   -6553
                        2(        MEMLK)       0       5       4     850       3       0  327680  -65536  -32768
     6         CUSTOM :
                        0(       GFXCLK)       0       5       1       0       4     800 4587520  -65536       0
                        1(       SOCCLK)       0       5       1       0       1       0 3276800   -6553   -6553
                        2(        MEMLK)       0       5       1       0       4     800  327680  -65536       0

To update the power profile, first change the performance mode to manual.

`root `[`#`]`echo 'manual' > /sys/class/drm/card0/device/power_dpm_force_performance_level`

Then update `pp_power_profile_mode` with the number of the pre-defined profile.

`root `[`#`]`echo '3' > /sys/class/drm/card0/device/pp_power_profile_mode`

The power profiles can be modified by sending commands to the `pp_power_profile_mode` file. The command syntax begins with the profile index number, then the clock type number, followed by a number for each column in the output.

For example, to change the `CUSTOM` power profile `GFXCLK` Booster Frequency from 800 to 500.

`root `[`#`]`echo '6 0 0 5 1 0 4 500 4587520 -65536 0' > /sys/class/drm/card0/device/pp_power_profile_mode`

** Note**\
These changes do not persist after a reboot.

#### [[] Power levels]

The amdgpu driver provides a sysfs API for adjusting what power levels are enabled for a given power state. The files `pp_dpm_sclk`, `pp_dpm_mclk`, `pp_dpm_socclk`, `pp_dpm_fclk`, `pp_dpm_dcefclk` and `pp_dpm_pcie` are used for this. A full description of the profiles can be found in the [kernel documentation](https://www.kernel.org/doc/html/latest/gpu/amdgpu/thermal.html#pp-dpm).

`pp_dpm_socclk` and `pp_dpm_dcefclk` interfaces are only available for Vega10 and later ASICs. `pp_dpm_fclk` interface is only available for Vega20 and later ASICs.

Reading back the files will show the available power levels within the power state and the clock information for those levels.

`user `[`$`]`cat /sys/class/drm/card0/device/pp_dpm_sclk`

    0: 500Mhz
    1: 700Mhz *
    2: 2765Mhz

`user `[`$`]`cat /sys/class/drm/card0/device/pp_dpm_mclk`

    0: 96Mhz *
    1: 541Mhz
    2: 675Mhz
    3: 1094Mhz

#### [[] Clock speed and voltage]

The amdgpu driver provides a sysfs API for adjusting the clocks and voltages in each power level within a power state. The `pp_od_clk_voltage` is used for this. A full description of the profiles can be found in the [kernel documentation](https://www.kernel.org/doc/html/latest/gpu/amdgpu/thermal.html#pp-od-clk-voltage).

Determine the current values.

`user `[`$`]`cat /sys/class/drm/card0/device/pp_od_clk_voltage`

    OD_SCLK:
     0: 700Mhz
     1: 2744Mhz
    OD_MCLK:
     0: 97Mhz
     1: 1094MHz
    OD_VDDGFX_OFFSET:
     0mV
    OD_RANGE:
     SCLK:     500Mhz       3150Mhz
     MCLK:     674Mhz       1200Mhz

** Note**\
The actual memory controller clock rates are shown here, not the effective clock of the DRAMs.

To update the clock speeds and voltages, first change the performance mode to manual.

`root `[`#`]`echo 'manual' > /sys/class/drm/card0/device/power_dpm_force_performance_level`

Then write a string to the file for each adjustment. Follow the syntax given in the [kernel documentation](https://www.kernel.org/doc/html/latest/gpu/amdgpu/thermal.html#pp-od-clk-voltage).

`root `[`#`]`echo 's 1 2410' > /sys/class/drm/card0/device/pp_od_clk_voltage`

`root `[`#`]`echo 'm 1 1024' > /sys/class/drm/card0/device/pp_od_clk_voltage`

Once finished, commit your changes.

`root `[`#`]`echo 'c' > /sys/class/drm/card0/device/pp_od_clk_voltage`

`user `[`$`]`cat /sys/class/drm/card0/device/pp_od_clk_voltage`

    OD_SCLK:
     0: 700Mhz
     1: 2410Mhz
    OD_MCLK:
     0: 97Mhz
     1: 1024MHz
    OD_VDDGFX_OFFSET:
     0mV
    OD_RANGE:
     SCLK:     500Mhz       3150Mhz
     MCLK:     674Mhz       1200Mhz

These changes can be reverted.

`root `[`#`]`echo 'r' > /sys/class/drm/card0/device/pp_od_clk_voltage`

** Note**\
These changes do not persist after a reboot.

## [[] Troubleshooting]

### [[] Debug tools]

#### [][[] x11-apps/mesa-progs]

It might be helpful to install the package [[[x11-apps/mesa-progs]](https://packages.gentoo.org/packages/x11-apps/mesa-progs)[]], which provides the [glxgears] and [glxinfo] utilities.

\

#### [][[] sys-apps/amdgpu_top]

The AMD/Radeon usage viewer [[[app-misc/radeontop]](https://packages.gentoo.org/packages/app-misc/radeontop)[]] is no longer developed and incompatible with newer GPU\'s. [[[sys-apps/amdgpu_top]](https://packages.gentoo.org/packages/sys-apps/amdgpu_top)[]] is a replacement and has a TUI and GUI interface.

### [[] Identifying which graphics card is in use]

First make sure that the kernel was compiled with the following settings:

[KERNEL] **Activate VGA Arbitration and Laptop Hybrid Graphics**

    Device Drivers  --->
        Graphics support  --->
            [*] VGA Arbitration Search for <code>CONFIG_VGA_ARB</code> to find this item.
            [*] Laptop Hybrid Graphics - GPU switching support Search for <code>CONFIG_VGA_SWITCHEROO</code> to find this item.

Check, if the discrete graphics card was recognized:

`user `[`$`]`lspci -k`

    [...]
    01:00.0 Display controller: Advanced Micro Devices, Inc. [AMD/ATI] Mars [Radeon HD 8670A/8670M/8750M]
            Subsystem: Lenovo Mars [Radeon HD 8670A/8670M/8750M]
            Kernel driver in use: radeon
    [...]

After that. Make sure that the path [/sys/kernel/debug/] was mounted successfully:

`root `[`#`]`findmnt debugfs`

    TARGET            SOURCE  FSTYPE  OPTIONS
    /sys/kernel/debug debugfs debugfs rw,nosuid,nodev,noexec,relatime

Then, check, if the driver **vga_switcheroo** was loaded successfully and can output values:

`root `[`#`]`cat /sys/kernel/debug/vgaswitcheroo/switch`

    0:DIS: :DynOff:0000:01:00.0
    1:IGD:+:Pwr:0000:00:02.0

This output has the following structure^[\[24\]](#cite_note-24)^:

  ---------- ----- ------------------------------------------------ ------------- --------------------------
  Iterator   ID    Active state                                     Power state   Device ID (xxxx:xx:xx.x)
  0          DIS   inactive (denoted by the lack of a `+` symbol)   DynOff        0000:01:00.0
  1          IGD   active (denoted by `+` symbol)                   Pwr           0000:00:02.0
  ---------- ----- ------------------------------------------------ ------------- --------------------------

`DIS` represents the *discrete* graphics card, which is *inactive*, but currently *disconnected* (`DynOff`).\
`IGD` is the *integrated* graphics card, which is *active* (`+`) and is currently *in use* (`Pwr`).

The status can be manipulated using the following command:

`root `[`#`]`echo "<some_parameter>" > /sys/kernel/debug/vgaswitcheroo/switch`

Replace `<some_parameter>` with one of the following paramters^[\[25\]](#cite_note-25)^:

  ----------- ------------------------------------------------------------------------------------------------------------------------------
  Parameter   Description
  ON          Turns on the disconnected GPU, which is currently not displaying anything and *does* not switch outputs.
  IGD         Connects the *integrated* graphics card with the display.
  DIS         Connects the *discrete* graphics card with the display.
  OFF         Turns off the graphics card, which is currently disconnected.
  DIGD        Inside of an **X session**: Queues a switch to the *integrated* graphics card to occur, when the X server is next restarted.
  DDIS        Inside of an **X session**: Queues a switch to the *discrete* graphics card to occur, when the X server is next restarted.
  ----------- ------------------------------------------------------------------------------------------------------------------------------

By using the environment variable `DRI_PRIME=1`, one can use the discrete graphics card individually:

`user `[`$`]`DRI_PRIME=1 glxgears`

This opens an *X* window with rotating gears.

Let it run in the background and check, `vga_switcheroo` again:

`root `[`#`]`cat /sys/kernel/debug/vgaswitcheroo/switch`

    0:DIS: :DynPwr:0000:01:00.0
    1:IGD:+:Pwr:0000:00:02.0

** Note**\
This time the status of the *discrete* graphics card switched to *DynPwr*, which means, that it is active and running.

Another indicator is to check the temperature sensors. This requires [[[sys-apps/lm-sensors]](https://packages.gentoo.org/packages/sys-apps/lm-sensors)[]]:

`user `[`$`]`sensors`

    [...]
    radeon-pci-0100
    Adapter: PCI adapter
    temp1:            +42.0°C  (crit = +120.0°C, hyst = +90.0°C)
    [...]

** Note**\
When `vga_switcheroo` displays the status `DynOff`, `sensors` will display the temperature as `N/A` or as something else, which may not make sense; for example: *-128°C*.

To use the discrete graphics card globally, one can set the environment variable in the [/etc/environment] file:

[FILE] **`/etc/environment`**

    DRI_PRIME=1

One might export it in the [\~/.bashrc] file as an alternative:

[FILE] **`/home/larry/.bashrc`**

    export DRI_PRIME=1

Or individually in front of the command, like above using [glxgears]:

`user `[`$`]`DRI_PRIME=1 /usr/bin/chromium `

`user `[`$`]`DRI_PRIME=1 /usr/bin/vlc `

### [[] Prime Synchronization]

The [[[x11-drivers/xf86-video-amdgpu]](https://packages.gentoo.org/packages/x11-drivers/xf86-video-amdgpu)[]] driver does not support Prime Synchronization. This might cause tearing on monitors connected to the integrated GPU if the AMD GPU is set as the primary GPU. One possible workaround is to use the *modesetting* driver instead, to do this remove `amdgpu` from the `VIDEO_CARDS` variable. Or use a xorg configuration file to force the use of the *modesetting* driver. That being said, other issues may be encountered with the *modesetting* driver^[\[26\]](#cite_note-26)^.

[FILE] **`/etc/X11/xorg.conf.d/force-modesetting.conf`**

    Section "Device"
        Identifier "modesetting"
        Driver "modesetting"
    EndSection

Another possible workaround is to set the integrated GPU as the primary GPU. This will **not** enable Prime Synchronization. However, tearing will be prevented nonetheless through AMD\'s *TearFree*. In this case it will be necessary to use the `DRI_PRIME=1` and `LIBVA_DRIVER_NAME=radeonsi`(for [VAAPI](https://wiki.gentoo.org/wiki/VAAPI "VAAPI")) variables on applications that should be rendered on the AMD GPU.

### [[] Fallback driver]

If having no other machine to browse web pages for solutions, the vesa or fbdev drivers can be used to start X without 3d and 2d acceleration.

-   `vesa` for classic [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") systems
-   `fbdev` for [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") booted systems

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: ... vesa fbdev

`root `[`#`]`emerge --ask --update --newuse --deep @world`

### [[] Kernel]

#### [[] Older kernels]

Older kernels that do not support the amdgpu driver will not provide the AMDGPU option. For VEGA and newer chips there is no video output without DC (Display Code), which was first included in vanilla Kernel 4.15. In both cases a fairly recent kernel can provide the required drivers. For very new AMD graphics cards and APUs trying a not yet stable kernel package (denoted by a **[\~]**, see [KEYWORDS](https://wiki.gentoo.org/wiki/KEYWORDS "KEYWORDS")) may provide the required kernel-sources.

#### [[] AMD Secure Memory Encryption]

If amdgpu fails to load or the screen stays frozen, it might be an incompatibility of the amdgpu module with AMD Secure Memory Encryption (SME).

SME can be temporarily disabled on the kernel command line (using GRUB, or in [/etc/default/grub] or as part of `GRUB_CMDLINE_LINUX`) by adding `mem_encrypt=off`. If this fixes the issue, a permanent solution is to configure the kernel accordingly.

[KERNEL]

    Processor type and features  --->
        [*] AMD Secure Memory Encryption (SME) support Search for <code>CONFIG_AMD_MEM_ENCRYPT</code> to find this item.
        [ ]   Activate AMD Secure Memory Encryption (SME) by default Search for <code>CONFIG_AMD_MEM_ENCRYPT_ACTIVE_BY_DEFAULT</code> to find this item.

`AMD_MEM_ENCRYPT` may remain enabled, but either `AMD_MEM_ENCRYPT_ACTIVE_BY_DEFAULT` must remain unset or the kernel command line option `mem_encrypt=off` must be used in order to turn Memory Encryption off. Likewise, with `mem_encrypt=on` SME can be activated for unaffected systems on the kernel command line or more permanently using `GRUB_CMDLINE_LINUX` in [/etc/default/grub] for GRUB.

### [][[] AMDGPU/RadeonSI drivers do not work]

If the graphics card is not supported by including `amdgpu` and `radeonsi` alone in `VIDEO_CARDS`, try adding `radeon` to [make.conf]\'s `VIDEO_CARDS` definition. For example:

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* amdgpu radeonsi radeon

After the values have been set update the system so the changes take effect:

`root `[`#`]`emerge --ask --changed-use --deep @world`

### [[] Full-screen windows perform poorly]

The installed version of [[[sys-devel/llvm]](https://packages.gentoo.org/packages/sys-devel/llvm)[]] may be too old. Try emerging an [unstable/testing version](https://wiki.gentoo.org/wiki/Knowledge_Base:Accepting_a_keyword_for_a_single_package "Knowledge Base:Accepting a keyword for a single package").

### [[] GPU Name shows up as id]

The installed version of [[[x11-libs/libdrm]](https://packages.gentoo.org/packages/x11-libs/libdrm)[]] may be too old. Try emerging an [unstable/testing version](https://wiki.gentoo.org/wiki/Knowledge_Base:Accepting_a_keyword_for_a_single_package "Knowledge Base:Accepting a keyword for a single package"). This might also improve performance.

### [][[] Xrandr doesn\'t see HDMI port with hybrid system]

On hybrid system with AMD iGPU and dGPU xrandr can show only eDP port, but not HDMI:

`user `[`$`]`xrandr`

    Screen 0: minimum 320 x 200, current 1920 x 2160, maximum 16384 x 16384
    eDP connected primary 1920x1080+0+1080 (normal left inverted right x axis y axis) 382mm x 215mm
       1920x1080    144.03*+  60.01
       1680x1050    144.03
       1280x1024    144.03
       1440x900     144.03
       1280x800     144.03
       1280x720     144.03
       1024x768     144.03
       800x600      144.03
       640x480      144.03

Whereas Xorg log shows that port was detected and EDID of the monitor decoded without issues:

`user `[`$`]`cat /var/log/Xorg.0.log`

    [...]
    [     8.282] (II) AMDGPU(G0): Output HDMI-A-1-0 has no monitor section
    [     8.294] (II) AMDGPU(G0): EDID for output HDMI-A-1-0
    [     8.295] (II) AMDGPU(G0): Manufacturer: DEL  Model: a11e  Serial#: 843731010
    [...]
    [     8.295] (II) AMDGPU(G0): Supported established timings:
    [     8.295] (II) AMDGPU(G0): 720x400@70Hz
    [...]
    [     8.295] (II) AMDGPU(G0): EDID (in hex):
    [     8.295] (II) AMDGPU(G0):   00ffffffffffff0010ac1ea142504a32
    [     8.295] (II) AMDGPU(G0):   0c1f010380351e78ea05f5a557529c27
    [...]
    [     8.296] (II) AMDGPU(G0): Printing probed modes for output HDMI-A-1-0
    [     8.296] (II) AMDGPU(G0): Modeline "1920x1080"x60.0  148.50  1920 2008 2052 2200  1080 1084 1089 1125 +hsync +vsync (67.5 kHz eP)
    [...]

If it doesn\'t then it is different issue. And it should be addressed first.

Xrandr would have 2 providers since there are 2 GPUs:

`user `[`$`]`xrandr --listproviders`

    Providers: number : 2
    Provider 0: id: 0x54 cap: 0xf, Source Output, Sink Output, Source Offload, Sink Offload crtcs: 4 outputs: 1 associated providers: 1 name:Unknown AMD Radeon GPU @ pci:0000:07:00.0
    Provider 1: id: 0x84 cap: 0xf, Source Output, Sink Output, Source Offload, Sink Offload crtcs: 5 outputs: 1 associated providers: 1 name:Radeon RX 5500M @ pci:0000:03:00.0

And we need to link source with output:

`user `[`$`]`xrandr --setprovideroutputsource provider source`

In provided example it would be this:

`user `[`$`]`xrandr --setprovideroutputsource 1 0`

After this xrandr shows HDMI and can manipulate layout properly:

`user `[`$`]`xrandr`

    Screen 0: minimum 320 x 200, current 1920 x 2160, maximum 16384 x 16384
    eDP connected primary 1920x1080+0+1080 (normal left inverted right x axis y axis) 382mm x 215mm
       1920x1080    144.03*+  60.01
    [...]
    HDMI-A-1-0 connected 1920x1080+0+0 (normal left inverted right x axis y axis) 527mm x 296mm
       1920x1080     60.00*+  50.00    59.94
    [...]

### [[] Screen Tearing]

One method to prevent screen tearing on Xorg is to enable the TearFree option in X11 like so:

[FILE] **`/usr/share/X11/xorg.conf.d/10-amdgpu.conf`**

    Section "OutputClass"
        Identifier "AMDgpu"
        MatchDriver "amdgpu"
        Driver "amdgpu"
        Option "TearFree" "true"
    EndSection

### [[] Flickering and white screens]

** Note**\
This issue has already been reported in the Gentoo forums: [https://forums.gentoo.org/viewtopic-t-1160883.html](https://forums.gentoo.org/viewtopic-t-1160883.html)

The suggested fix at upstream level is to set the `sg_display` module parameter like this: `amdgpu.sg_display=0`

As an alternative apply the following patch to the kernel source code: [https://patchwork.freedesktop.org/patch/519023](https://patchwork.freedesktop.org/patch/519023)

Seems to concern Linux kernels \>= 6.1.4.

### [[] Frequent and Sporadic Crashes]

Some users may be experiencing frequent and seemingly random graphics card crashes while using the AMDGPU drivers. Checking the kernel log may show many different errors, some common ones involving `*ERROR* Waiting for fences timed out!` and `*ERROR* ring gfx timeout`. This is usually followed by a reset of the graphics device/drivers.

This may be caused by an unintentional overclocking of the hardware, either by the AMDGPU driver or the device firmware. The following steps will show how to check the current system configuration and state. If discrepancies are found, reference the [Power management](https://wiki.gentoo.org/wiki/AMDGPU#Power_management "AMDGPU") section above for details on how to modify these values.

** Note**\
This is a specific example discovered by one user. The examples below assume the GPU is `CARD0` and the output is specific to a Radeon™ RX 6650 XT EAGLE 8G.

** Note**\
This only applies to hardware that has Dynamic Power Management (DPM) enabled. DPM is turned on by default for most modern AMDGPUs.

Begin by looking up the graphics card specifications, using a database such as the [TechPowerUp GPU Database](https://www.techpowerup.com/gpu-specs) or the manufacturer\'s specifications.

  ------------------------------------------------------------------------------------------------------------------------ ------------ ------------ ------------- ------------------------- -------------------- ------------
                                                                                                                           Base Clock   Game Clock   Boost Clock   Effective Memeory Clock   Effective VRAM Bus   Bandwidth
  [Specification](https://www.techpowerup.com/gpu-specs/gigabyte-rx-6650-xt-eagle.b9670)   2055 MHz     2410 MHz     2635 MHz      2190 MHz (17.5 Gbps)      128-bit              280.3 GBps
  ------------------------------------------------------------------------------------------------------------------------ ------------ ------------ ------------- ------------------------- -------------------- ------------

  : Radeon™ RX 6650 XT EAGLE 8G

In this example:

-   *Base Clock* is the default clock rate.
-   *Game Clock* is the expected clock rate when running typical gaming applications.
-   *Boost Clock* is the maximum clock rate when running a burst (infrequent) workload.
-   *Memory Clock* is the effective memory clock rate; the base DRAM clock rate multiplied by the number of channels.
-   *VRAM Bus* is the effective data bus bit width.
-   *Bandwidth* is the rate of data transfer (data_rate \* bus_width / 8)

\
Navigate to the device\'s AMDGPU sysfs directory.

`user `[`$`]`cd /sys/class/drm/card0/device/`

View the defined core and memory clock rates listed in the `pp_dpm_sclk` and `pp_dpm_mclk` files. The system uses these values to automatically adjust the clock rates under various loads. The current rate is denoted with an asterisk.

`user `[`$`]`cat pp_dpm_sclk`

    0: 500Mhz
    1: 700Mhz *
    2: 2765Mhz

`user `[`$`]`cat pp_dpm_mclk`

    0: 96Mhz *
    1: 541Mhz
    2: 675Mhz
    3: 1094Mhz

Verify the engine clock `SCLK` is within the limits of the hardware. In this case, the minimum rate is 500 MHz, it increments up to 700 MHz under load, and then up to a maximum of 2765 MHz.

Verify the DRAM memory clock `OD_MCLK` is within the limits of the hardware. In this case, the minimum reported rate is 96 MHz and the maximum is 1094 MHz.

This device uses GDDR6 (G6), which is dual channel Double Data Rate (DDR) memory^[\[27\]](#cite_note-27)[\[28\]](#cite_note-28)[\[29\]](#cite_note-29)^.

-   The maximum data transfer rate in transfers per second = clock cycles per second \* transfers per clock cycle \* data frequency multiplier; 1,094 MHz \* 2 T (double data rate) \* 8 = 17,504 MT/s. This corresponds to 17.5 Gbps.
-   The bus width is per chip per channel. In this case there are 4 physical ICs on the card^[\[30\]](#cite_note-30)^, each with an I/O width of 16 bits per channel; 16 bits \* 2 channel \* 4 IC = 128 bits total effective VRAM bus width.
-   The bandwidth = transfers per second \* bus width; 17,504 MT/s \* 128 bits/T = 2,240,512 Mb/s (280,064 MB/s).

\
Now view the over drive (boost) clock and voltage configuration in the `pp_od_clk_voltage` file.

`user `[`$`]`cat pp_od_clk_voltage`

    OD_SCLK:
     0: 700Mhz
     1: 2744Mhz
    OD_MCLK:
     0: 97Mhz
     1: 1094MHz
    OD_VDDGFX_OFFSET:
     0mV
    OD_RANGE:
     SCLK:     500Mhz       3150Mhz
     MCLK:     674Mhz       1200Mhz

The overdrive (boost) engine SCLK range is set to allow values between 500 and 3150 MHz for the engine clock. With discrete steps at 700 MHz and 2744 MHz.

The overdrive (boost) memory MCLK range is set to allow values between 674 MHz and 1200 MHz for the actual memory clock (1348 MHz and 2400 MHz effective). With discrete steps at 97 MHz and 1094 MHz.

** Note**\
The relationship between OD_SCLK, OD_MCLK, and OD_RANGE is not well documented. The values presented above were as-found on the system in question.

Combining all of this information together and comparing the reported and specified values shows a discrepancy for clock rates, with some well above the recommended values. Adjusting these limits (under-clocking the defaults) has resulted in zero crashes, and improved thermal and FPS performance.

  ------------------------------------------------------------------------------------------------------------------------ ------------ ------------ --------------- ------------------------- -------------------- ------------------------
                                                                                                                           Base Clock   Game Clock   Boost Clock     Effective Memeory Clock   Effective VRAM Bus   Bandwidth
  [Specification](https://www.techpowerup.com/gpu-specs/gigabyte-rx-6650-xt-eagle.b9670)   2055 MHz     2410 MHz     2635 MHz        2190 MHz (17.5 Gbps)      128-bit              280.3 GBps
  sysfs                                                                                                                    \- MHz       2765 MHz     2744/3150 MHz   2400 MHz (19.2 Gbps)      128-bit              307.2 GBps (@1200 MHz)
  ------------------------------------------------------------------------------------------------------------------------ ------------ ------------ --------------- ------------------------- -------------------- ------------------------

  : Radeon™ RX 6650 XT EAGLE 8G

### [[] Missing cursor on RDNA3 GPUs]

Hardware cursor doesn\'t work on new GPUs. To make cursor visible you should add software cursor option into 20-amdgpu.conf.

[FILE] **`/etc/X11/xorg.conf.d/20-amdgpu.conf`**

    Section "Device"
        Identifier "AMD"
        Driver "amdgpu"
        Option "SWCursor" "True"
    EndSection

Note that in X11 sessions this option may also fix high CPU usage when moving the cursor in some situations (cf these [Gentoo](https://forums.gentoo.org/viewtopic-t-1175502-highlight-9070.html)/[Arch](https://bbs.archlinux.org/viewtopic.php?id=306283) forum posts).

## [Tools]

Some tools to monitor and configure the GPU are available (not limited to AMD.)

These two are GUI tools:

-   [corectrl](https://gitlab.com/corectrl/corectrl) - available at farmboy0 overlay [here](https://github.com/farmboy0/portage-overlay/tree/master/kde-misc/corectrl).
-   [LACT](https://github.com/ilya-zlobintsev/LACT) - available at GURU overlay [here](https://github.com/gentoo/guru/tree/master/sys-apps/lact).

## [[] See also]

-   [AMDGPU-PRO](https://wiki.gentoo.org/wiki/AMDGPU-PRO "AMDGPU-PRO") --- the next generation *closed source* graphics component that operates on top of the open source [AMDGPU] drivers for newer AMD/ATI Radeon graphics cards.
-   [AMDVLK](https://wiki.gentoo.org/wiki/AMDVLK "AMDVLK") --- an open-source Vulkan driver for AMD Radeon™ graphics adapters on Linux

## [[] External resources]

-   [A list of RadeonSI articles on the Phoronix site.](https://www.phoronix.com/scan.php?page=search&q=RadeonSI)
-   [\[1\]](https://www.kernel.org/doc/html/next/gpu/amdgpu/amd-hardware-list-info.html) Official kernel documentation on firmware version

## [[] References]

1.  [[[↑](#cite_ref-1)] [AMD previously called the microarchitecture *Display Core* (DC). GCN stands for *Graphics Core Next* and was introduced with the Radeon HD7000 series (GCN1.0). It was superseded by RDNA, short for *Radeon DNA*, introduced with the Radeon RX 5000 series (NAVI) in 2019.]]
2.  [[[↑](#cite_ref-2)] [The actual Instruction Set Architecture (ISA) is defined by the *Display Core Engine* (DCE), which was superseded by *Display Core Next* (DCN), introduced with the *Raven Ridge* APUs (mobile Vega graphics core).]]
3.  [[↑ ^[3.0](#cite_ref-phoronix_Valve-Old-AMD-Linux-Love-Song_3-0)^ ^[3.1](#cite_ref-phoronix_Valve-Old-AMD-Linux-Love-Song_3-1)^] [Phoronix - [Valve\'s Open-Source Radeon Linux Driver \"Love Song For Gamers With Old GPUs\"](https://www.phoronix.com/news/Valve-Old-AMD-Linux-Love-Song)]]
4.  [[↑ ^[4.0](#cite_ref-phoronix_Linux-6.19-AMDGPU-GCN-1.0-1.1_4-0)^ ^[4.1](#cite_ref-phoronix_Linux-6.19-AMDGPU-GCN-1.0-1.1_4-1)^] [Phoronix - [AMD GCN 1.0/1.1 GPUs Will Default To AMDGPU Driver In Linux 6.19](https://www.phoronix.com/news/Linux-6.19-AMDGPU-GCN-1.0-1.1)]]
5.  [[[↑](#cite_ref-5)] [Phoronix - [Report: Ryzen \"Raven Ridge\" APU Not Using HBM2 Memory](https://www.phoronix.com/scan.php?page=news_item&px=Raven-Ridge-APU-Not-HBM2)]]
6.  [[[↑](#cite_ref-6)] [Phoronix - [25 More AMDGPU DC Patches, Mostly Focused On Raven DCN](https://phoronix.com/scan.php?page=news_item&px=AMDGPU-DC-25-DCN)]]
7.  [[[↑](#cite_ref-amd-navi_7-0)] [Phoronix - [AMD Navi 10 Firmware Finally Lands In The Linux-Firmware Tree](https://www.phoronix.com/scan.php?page=news_item&px=Navi-10-Linux-Firmware-Git)]]
8.  [[[↑](#cite_ref-8)] [[https://www.phoronix.com/scan.php?page=news_item&px=Radeon-RX-6900-XT](https://www.phoronix.com/scan.php?page=news_item&px=Radeon-RX-6900-XT)]]
9.  [[[↑](#cite_ref-9)] [[https://cateee.net/lkddb/web-lkddb/DRM_AMD_DC_DCN3_0.html](https://cateee.net/lkddb/web-lkddb/DRM_AMD_DC_DCN3_0.html)]]
10. [[[↑](#cite_ref-10)] [Phoronix - [AMD Radeon RX 7900 XTX + RX 7900 XT Linux Support & Performance](https://www.phoronix.com/review/rx7900xt-rx7900xtx-linux)]]
11. [[[↑](#cite_ref-11)] [Phoronix - [AMD Radeon 890M \"RDNA3.5\" Graphics Run Well With Latest Open-Source Linux Driver](https://www.phoronix.com/review/amd-radeon-890m-rdna35)]]
12. [[[↑](#cite_ref-12)] [Phoronix - [AMD Updates DMCUB Firmware For RDNA3.5 Graphics With Strix Point](https://www.phoronix.com/news/AMD-DMCUB-Firmware-RDNA3.5)]]
13. [[[↑](#cite_ref-13)] [Phoronix - [AMD Radeon RX 9070 + RX 9070 XT Linux Performance](https://www.phoronix.com/review/amd-radeon-rx9070-linux)]]
14. [[[↑](#cite_ref-14)] [Phoronix - [Radeon RX 9070 Fan Speed Reporting & Other Last Minute AMD Changes For Linux 6.15](https://www.phoronix.com/news/RX-9070-Fan-Speed-Linux-6.15)]]
15. [[[↑](#cite_ref-15)] [Phoronix - [Mesa RADV/RadeonSI Now Support RDNA4 GPUs With Radeon GPU Profiler](https://www.phoronix.com/news/Mesa-RDNA4-AMD-RGP)]]
16. [[[↑](#cite_ref-16)] [Phoronix - [AMDVLK 2025.Q1.3 Brings Radeon RX 9070 Series Support](https://www.phoronix.com/news/AMDVLK-2025.Q1.3-Released)]]
17. [[[↑](#cite_ref-17)] [[Linux kernel commit 39bdb32 with added firmware files to POLARIS10 and POLARIS11](https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/commit/?h=linux-4.19.y&id=39bdb32876df3710825d33b5c455ec2ffa9db64e)]]
18. [[[↑](#cite_ref-18)] [[https://kernelnewbies.org/Linux_3.11#AMD_Radeon_experimental_dynamic_power_management_support](https://kernelnewbies.org/Linux_3.11#AMD_Radeon_experimental_dynamic_power_management_support)]]
19. [[[↑](#cite_ref-19)] [[https://www.kernel.org/doc/html/latest/gpu/amdgpu/thermal.html](https://www.kernel.org/doc/html/latest/gpu/amdgpu/thermal.html)]]
20. [[[↑](#cite_ref-20)] [[https://www.kernel.org/doc/html/latest/gpu/amdgpu/module-parameters.html](https://www.kernel.org/doc/html/latest/gpu/amdgpu/module-parameters.html)]]
21. [[[↑](#cite_ref-21)] [[https://www.phoronix.com/news/AMDGPU-PP-4.5-Steps](https://www.phoronix.com/news/AMDGPU-PP-4.5-Steps)]]
22. [[[↑](#cite_ref-22)] [[https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpu/drm/amd/include/amd_shared.h](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpu/drm/amd/include/amd_shared.h)]]
23. [[[↑](#cite_ref-23)] [[https://www.kernel.org/doc/html/latest/gpu/amdgpu/module-parameters.html?highlight=ppfeaturemask](https://www.kernel.org/doc/html/latest/gpu/amdgpu/module-parameters.html?highlight=ppfeaturemask)]]
24. [[[↑](#cite_ref-24)] [[https://github.com/torvalds/linux/blob/be8454afc50f43016ca8b6130d9673bdd0bd56ec/drivers/gpu/vga/vga_switcheroo.c#L653-L660](https://github.com/torvalds/linux/blob/be8454afc50f43016ca8b6130d9673bdd0bd56ec/drivers/gpu/vga/vga_switcheroo.c#L653-L660)]]
25. [[[↑](#cite_ref-25)] [[https://help.ubuntu.com/community/HybridGraphics](https://help.ubuntu.com/community/HybridGraphics)]]
26. [[[↑](#cite_ref-26)] [[https://gitlab.freedesktop.org/xorg/driver/xf86-video-amdgpu/-/issues/11](https://gitlab.freedesktop.org/xorg/driver/xf86-video-amdgpu/-/issues/11)]]
27. [[[↑](#cite_ref-27)] [[https://www.micron.com/-/media/client/global/documents/products/technical-note/dram/tned03_gddr6.pdf](https://www.micron.com/-/media/client/global/documents/products/technical-note/dram/tned03_gddr6.pdf)]]
28. [[[↑](#cite_ref-28)] [[http://monitorinsider.com/GDDR5X.html](http://monitorinsider.com/GDDR5X.html)]]
29. [[[↑](#cite_ref-29)] [[http://monitorinsider.com/GDDR6.html](http://monitorinsider.com/GDDR6.html)]]
30. [[[↑](#cite_ref-30)] [[https://csstalker.gjisland.net/blog/archives/6848](https://csstalker.gjisland.net/blog/archives/6848)]]