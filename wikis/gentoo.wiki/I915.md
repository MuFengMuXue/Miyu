This page contains [[changes](https://wiki.gentoo.org/index.php?title=Intel&oldid=1412269&diff=1431428)] which are not marked for translation.

Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Intel/hu "Intel (87% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Intel/zh-cn "Intel (59% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Intel/ja "Intel (100% translated)")

**Resources**

[[]][Home](https://01.org/linuxgraphics)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Intel_GMA "wikipedia:Intel GMA")

[[]][GitWeb (userspace driver)](https://cgit.freedesktop.org/xorg/driver/xf86-video-intel)

[[]][Official documentation](https://01.org/linuxgraphics/)

**Intel** is the open source graphics driver for Intel GMA on-board graphics cards and Intel iGPU and Intel Arc dedicated graphics cards, starting with the Intel 810.

## Contents

-   [[1] [Hardware detection]](#Hardware_detection)
-   [[2] [Feature support]](#Feature_support)
-   [[3] [Installation]](#Installation)
    -   [[3.1] [Firmware]](#Firmware)
        -   [[3.1.1] [DMC firmware]](#DMC_firmware)
        -   [[3.1.2] [GuC/HuC firmware]](#GuC.2FHuC_firmware)
        -   [[3.1.3] [Discrete Cards firmware]](#Discrete_Cards_firmware)
    -   [[3.2] [Kernel]](#Kernel)
    -   [[3.3] [X drivers]](#X_drivers)
        -   [[3.3.1] [Intel DDX]](#Intel_DDX)
            -   [[3.3.1.1] [USE flags]](#USE_flags)
            -   [[3.3.1.2] [Emerge]](#Emerge)
            -   [[3.3.1.3] [xorg.conf]](#xorg.conf)
        -   [[3.3.2] [Modesetting DDX]](#Modesetting_DDX)
            -   [[3.3.2.1] [xorg.conf]](#xorg.conf_2)
            -   [[3.3.2.2] [Screen tearing]](#Screen_tearing)
            -   [[3.3.2.3] [Enable early KMS]](#Enable_early_KMS)
    -   [[3.4] [VAAPI]](#VAAPI)
    -   [[3.5] [Vulkan]](#Vulkan)
    -   [[3.6] [Tools]](#Tools)
-   [[4] [Configuration]](#Configuration)
    -   [[4.1] [Kernel]](#Kernel_2)
        -   [[4.1.1] [Fastboot]](#Fastboot)
    -   [[4.2] [Permissions]](#Permissions)
    -   [[4.3] [xorg.conf]](#xorg.conf_3)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Screen flickering]](#Screen_flickering)
    -   [[5.2] [KDE Plasma eating CPU]](#KDE_Plasma_eating_CPU)
    -   [[5.3] [Black screen]](#Black_screen)
    -   [[5.4] [Brightness does not change with keyboard shortcuts]](#Brightness_does_not_change_with_keyboard_shortcuts)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)
-   [[8] [References]](#References)

## [Hardware detection]

To choose the right driver, first detect the graphics card. [[lspci](https://wiki.gentoo.org/wiki/Lspci "Lspci")] can be used for this task

`root `[`#`]`lspci | grep -i VGA`

This should show something like this:

`root `[`#`]`lspci | grep -i VGA`

    00:02.0 VGA compatible controller: Intel Corporation 3rd Gen Core processor Graphics Controller (rev 09)

** Note**\
The [lspci] output for the graphics controller may refer to *CPU generations*, whereas the **Feature support** table below refers to *GPU generations*. E.g., "3rd Gen" in the example lspci output above corresponds to "Gen7" in the table below.

## [Feature support]

  -------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------- ----------- --------------------------------------------------------------- ----------------------------------------------------- -------------------------------------------------------- --------------------------------------------------------------------------------------------------
  Generation                                                                                                                                                     Chipset                                                                                                                                                                                                                                                                      OpenGL   OpenGL ES   OpenCL                                                          [VAAPI](https://wiki.gentoo.org/wiki/VAAPI "VAAPI")   [Vulkan](https://wiki.gentoo.org/wiki/Vulkan "Vulkan")   [`VIDEO_CARDS`](https://wiki.gentoo.org/wiki/VIDEO_CARDS "VIDEO CARDS")
  [Gen 1](https://en.wikipedia.org/wiki/List_of_Intel_graphics_processing_units#First_generation "wikipedia:List of Intel graphics processing units")    810, 815                                                                                                                                                                                                                                                                     No       No          No                                                              No                                                    No                                                       unsupported
  [Gen 2](https://en.wikipedia.org/wiki/List_of_Intel_graphics_processing_units#Second_generation "wikipedia:List of Intel graphics processing units")   i830M, 845G, 855GM, 865G                                                                                                                                                                                                                                                     1.3      No          No                                                              No                                                    No                                                       *intel i915*^[\[table\ 1\]](#cite_note-classic-1)^
  [Gen 3](https://en.wikipedia.org/wiki/List_of_Intel_graphics_processing_units#Third_generation "wikipedia:List of Intel graphics processing units")    915G/GM, 945G/GM, G31, G/Q33, Q35, Atom D4xx/D5xx/N4xx/N5xx                                                                                                                                                                                                                  1.4      No          1.2^[\[table\ 2\]](#cite_note-ocl_beignet_unsupported-2)^       No                                                    No                                                       *intel i915*^[\[table\ 1\]](#cite_note-classic-1)^
  [Gen 4](https://en.wikipedia.org/wiki/List_of_Intel_graphics_processing_units#Gen4 "wikipedia:List of Intel graphics processing units")                965G/GM/Q, G35, G41, G/Q43, G/GM/Q45                                                                                                                                                                                                                                         2.1      2.0         1.2^[\[table\ 2\]](#cite_note-ocl_beignet_unsupported-2)^       G/GM45: MPEG2 only                                    No                                                       *intel*
  [Gen 5](https://en.wikipedia.org/wiki/List_of_Intel_graphics_processing_units#Gen5 "wikipedia:List of Intel graphics processing units")                [Nehalem](https://en.wikipedia.org/wiki/Nehalem_(microarchitecture) "wikipedia:Nehalem (microarchitecture)") (Ironlake)                                                                                                                                              2.1      2.0         1.2^[\[table\ 2\]](#cite_note-ocl_beignet_unsupported-2)^       Yes                                                   No                                                       *intel*
  [Gen 6](https://en.wikipedia.org/wiki/List_of_Intel_graphics_processing_units#Gen6 "wikipedia:List of Intel graphics processing units")                [Sandy Bridge](https://en.wikipedia.org/wiki/Sandy_Bridge "wikipedia:Sandy Bridge")                                                                                                                                                                                  3.3      3.0         2.0^[\[table\ 2\]](#cite_note-ocl_beignet_unsupported-2)^       Yes                                                   No                                                       *intel*
  [Gen 7](https://en.wikipedia.org/wiki/List_of_Intel_graphics_processing_units#Gen7 "wikipedia:List of Intel graphics processing units")                [Ivy Bridge](https://en.wikipedia.org/wiki/Ivy_Bridge_(microarchitecture) "wikipedia:Ivy Bridge (microarchitecture)"), Valley View^[\[table\ 3\]](#cite_note-valleyview-3)^                                                                                          4.2      3.0         2.0^[\[table\ 4\]](#cite_note-ocl_propietary_unsupported-4)^    Yes                                                   1.0                                                      *intel*
  [Gen 7.5](https://en.wikipedia.org/wiki/List_of_Intel_graphics_processing_units#Gen7 "wikipedia:List of Intel graphics processing units")              [Haswell](https://en.wikipedia.org/wiki/Haswell_(microarchitecture) "wikipedia:Haswell (microarchitecture)")                                                                                                                                                         4.6      3.2         2.0^[\[table\ 4\]](#cite_note-ocl_propietary_unsupported-4)^    Yes                                                   1.0                                                      *intel*
  [Gen 8](https://en.wikipedia.org/wiki/List_of_Intel_graphics_processing_units#Gen8 "wikipedia:List of Intel graphics processing units")                [Broadwell](https://en.wikipedia.org/wiki/Broadwell_(microarchitecture) "wikipedia:Broadwell (microarchitecture)"), Cherryview^[\[table\ 5\]](#cite_note-cherryview-5)^                                                                                              4.6      3.2         3.0^[\[table\ 6\]](#cite_note-ocl-6)^                           Yes                                                   1.1                                                      *intel*
  [Gen 9](https://en.wikipedia.org/wiki/List_of_Intel_graphics_processing_units#Gen9 "wikipedia:List of Intel graphics processing units")                [Skylake](https://en.wikipedia.org/wiki/Skylake_(microarchitecture) "wikipedia:Skylake (microarchitecture)"), Broxton^[\[table\ 7\]](#cite_note-broxton-7)^                                                                                                          4.6      3.2         3.0^[\[table\ 6\]](#cite_note-ocl-6)^                           Yes                                                   1.2                                                      *intel*
  [Gen 9.5](https://en.wikipedia.org/wiki/List_of_Intel_graphics_processing_units#Gen9 "wikipedia:List of Intel graphics processing units")              [Kaby Lake](https://en.wikipedia.org/wiki/Kaby_Lake "wikipedia:Kaby Lake"), [Coffee Lake](https://en.wikipedia.org/wiki/Coffee_Lake "wikipedia:Coffee Lake"), [Gemini Lake](https://en.wikipedia.org/wiki/Goldmont_Plus "wikipedia:Goldmont Plus")   4.6      3.2         3.0^[\[table\ 6\]](#cite_note-ocl-6)^                           Yes                                                   1.2                                                      *intel*
  [Gen 11](https://en.wikipedia.org/wiki/Intel_Graphics_Technology#Gen11 "wikipedia:Intel Graphics Technology")                                          [Ice Lake](https://en.wikipedia.org/wiki/Ice_Lake_(microprocessor) "wikipedia:Ice Lake (microprocessor)")                                                                                                                                                            4.6      3.2         3.0^[\[table\ 6\]](#cite_note-ocl-6)^                           Yes                                                   1.2                                                      *intel*
  [Gen 12](https://en.wikipedia.org/wiki/Intel_Graphics_Technology#Gen12 "wikipedia:Intel Graphics Technology")                                          [Tiger Lake](https://en.wikipedia.org/wiki/Tiger_Lake "wikipedia:Tiger Lake"), [Alder Lake](https://en.wikipedia.org/wiki/Alder_Lake "wikipedia:Alder Lake"), [Raptor Lake](https://en.wikipedia.org/wiki/Raptor_Lake "wikipedia:Raptor Lake")       4.6      3.2         3.0^[\[table\ 6\]](#cite_note-ocl-6)^                           Yes                                                   1.2                                                      *intel*
  [DG2](https://en.wikipedia.org/wiki/List_of_Intel_graphics_processing_units#Gen_12.7 "wikipedia:List of Intel graphics processing units")              [Alchemist](https://en.wikipedia.org/wiki/Intel_Arc#Alchemist "wikipedia:Intel Arc")                                                                                                                                                                                 4.6      3.2         3.0^[\[table\ 6\]](#cite_note-ocl-6)^                           Yes                                                   1.3                                                      *intel*^[\[table\ 8\]](#cite_note-arc-8)^
  [BMG](https://en.wikipedia.org/wiki/List_of_Intel_graphics_processing_units#Battlemage_based "wikipedia:List of Intel graphics processing units")      [Battlemage](https://en.wikipedia.org/wiki/Intel_Arc#Battlemage "wikipedia:Intel Arc")                                                                                                                                                                               4.6      3.2         3.0^[\[table\ 6\]](#cite_note-ocl-6)^                           Yes                                                   1.3                                                      *intel*^[\[table\ 9\]](#cite_note-battlemage-9)^
  -------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------- ----------- --------------------------------------------------------------- ----------------------------------------------------- -------------------------------------------------------- --------------------------------------------------------------------------------------------------

1.  [[↑ ^[1.0](#cite_ref-classic_1-0)^ ^[1.1](#cite_ref-classic_1-1)^] [Mesa 22.0 and higher have dropped support for i915 classic driver. Users can install the additional media-libs/mesa-amber package.]]
2.  [[↑ ^[2.0](#cite_ref-ocl_beignet_unsupported_2-0)^ ^[2.1](#cite_ref-ocl_beignet_unsupported_2-1)^ ^[2.2](#cite_ref-ocl_beignet_unsupported_2-2)^ ^[2.3](#cite_ref-ocl_beignet_unsupported_2-3)^] [Used to be supported by [Beignet project](https://wiki.freedesktop.org/www/Software/Beignet/) which is now deprecated and no longer maintained.]]
3.  [[[↑](#cite_ref-valleyview_3-0)] [Valley View is the name of the graphics core associated with the [Silvermont](https://en.wikipedia.org/wiki/Silvermont "wikipedia:Silvermont") microarchitecture (Bay Trail platform, among others)]]
4.  [[↑ ^[4.0](#cite_ref-ocl_propietary_unsupported_4-0)^ ^[4.1](#cite_ref-ocl_propietary_unsupported_4-1)^] [Used to be supported by proprietary [Legacy OpenCL drivers from Intel](https://www.intel.com/content/www/us/en/developer/articles/technical/legacy-opencl-drivers.html#latest_linux_driver), which are no longer maintained.]]
5.  [[[↑](#cite_ref-cherryview_5-0)] [Cherryview is the name of the graphics core associated with the [Airmont](https://en.wikipedia.org/wiki/Airmont "wikipedia:Airmont") microarchitecture (Braswell, Cherry Trail platforms, among others)]]
6.  [[↑ ^[6.0](#cite_ref-ocl_6-0)^ ^[6.1](#cite_ref-ocl_6-1)^ ^[6.2](#cite_ref-ocl_6-2)^ ^[6.3](#cite_ref-ocl_6-3)^ ^[6.4](#cite_ref-ocl_6-4)^ ^[6.5](#cite_ref-ocl_6-5)^ ^[6.6](#cite_ref-ocl_6-6)^] [Supported by [[[dev-libs/intel-compute-runtime]](https://packages.gentoo.org/packages/dev-libs/intel-compute-runtime)[]]]]
7.  [[[↑](#cite_ref-broxton_7-0)] [Broxton is the name of the graphics core associated with the [Goldmont](https://en.wikipedia.org/wiki/Goldmont "wikipedia:Goldmont") microarchitecture (Apollo Lake platform, among others)]]
8.  [[[↑](#cite_ref-arc_8-0)] [Requires at least kernel version 6.0.0 and Mesa 22.2]]
9.  [[[↑](#cite_ref-battlemage_9-0)] [Requires at least kernel version 6.12.0 and Mesa 24.3]]

A full list of Intel CPU graphic capabilities is [here](https://en.wikipedia.org/wiki/Intel_HD_and_Iris_Graphics#Capabilities "wikipedia:Intel HD and Iris Graphics").

## [Installation]

### [Firmware]

Systems using Skylake, Broxton, or newer Intel graphics will need additional [firmware](https://wiki.gentoo.org/wiki/Linux_firmware "Linux firmware")^[\[1\]](#cite_note-firmware-10)^ from [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] package:

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

Otherwise errors such as the following might appear in [dmesg]:

    kernel: i915 0000:00:02.0: Direct firmware load for i915/skl_dmc_ver1_27.bin failed with error -2
    kernel: i915 0000:00:02.0: Failed to load DMC firmware [https://01.org/linuxgraphics/intel-linux-graphics-firmwares], disabling runtime power management.

#### [DMC firmware]

**D**isplay **M**icro**c**ontroller firmware provides support for advanced graphics low-power idle states.^[\[1\]](#cite_note-firmware-10)^

To build the DMC firmware into the kernel binary (in this case, [i915/skl_dmc_ver1_27.bin]):

[KERNEL] **(Before Linux 4.18) Build firmware blobs into the kernel binary**

    Device Drivers  --->
        Generic Driver Options  --->
            -*- Userspace firmware loading support
            [*] Include in-kernel firmware blobs in kernel binary
                (i915/skl_dmc_ver1_27.bin) External firmware blobs to build into the kernel binary
                (/lib/firmware) Firmware blobs root directory

[KERNEL] **(Since Linux 4.18) Build firmware blobs into the kernel binary**

    Device Drivers  --->
        Generic Driver Options  --->
            Firmware loader  --->
                -*- Firmware loading facility
                (i915/skl_dmc_ver1_27.bin) Build named firmware blobs into the kernel binary
                (/lib/firmware) Firmware blobs root directory

** Warning**\
Including the firmware in-kernel may cause suspend-to-ram to fail, if this is a concern don\'t include the blob built into the kernel, instead, add the firmware blob into the [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs"). An example is available as a part of the [[dracut] article](https://wiki.gentoo.org/wiki/Dracut#Adding_files_to_the_image "Dracut").

Alternatively compile the i915 driver as a kernel module and it will automatically load the firmware from the filesystem.

#### [][GuC/HuC firmware]

**G**raphics **µC**ontroller firmware offloads functions from the host driver. **H**EVC/H.265 **µC**ontroller firmware improves hardware acceleration of media decoding.^[\[1\]](#cite_note-firmware-10)^

For Gen11+ GPUs, GuC/HuC firmware loads by default since Linux 5.4 (see [commit](https://www.fclose.com/linux-kernels/87/d8/55e-drm-i915-guc-dont-enable-guc-huc-in-auto-mode-on-pre-gen11)).

For Gen9 and Gen9.5 GPUs, GuC/HuC firmware won\'t load by default. It is possible to enable loading of the firmware using kernel parameter `i915.enable_guc_loading=1` (before kernel 4.16) or `i915.enable_guc=3` (since kernel 4.16). [HuC firmware (and GuC as a dependent) is needed for AVC/HEVC/VP9 low power encoding bitrate control, including CBR, VBR, etc.](https://github.com/intel/media-driver#known-issues-and-limitations). Enabling GuC/HuC firmware loading causes issues in some systems. Disable it if the system experiences freezing (for example, after resuming from hibernation).

GuC firmware for Gen 12+ now only uses major version numbers e.g. [tgl_guc_70.bin]^[\[2\]](#cite_note-11)^ and HuC firmware does not have a version number e.g. [tgl_huc.bin]^[\[3\]](#cite_note-12)^.

To identify the firmware file name, either by checking `/var/log/kern.log`:

[FILE] **`/var/log/kern.log`**

    kernel: [    1.294069] [drm] GuC: Failed to fetch firmware i915/kbl_guc_ver9_33.bin (error -2)
    kernel: [    1.294079] [drm] HuC: Failed to fetch firmware i915/kbl_huc_ver01_07_1398.bin (error -2)

Or by grepping the `MODULE_FIRMWARE` in the kernel source tree:

`user `[`$`]`grep -rB1 'MODULE_FIRMWARE.*SKL' /usr/src/linux/drivers/gpu/drm/i915`

    /usr/src/linux/drivers/gpu/drm/i915/intel_guc_fw.c-#define I915_SKL_GUC_UCODE GUC_FW_PATH(skl, SKL_FW_MAJOR, SKL_FW_MINOR)
    /usr/src/linux/drivers/gpu/drm/i915/intel_guc_fw.c:MODULE_FIRMWARE(I915_SKL_GUC_UCODE);
    --
    /usr/src/linux/drivers/gpu/drm/i915/intel_csr.c-#define I915_CSR_SKL "i915/skl_dmc_ver1_27.bin"
    /usr/src/linux/drivers/gpu/drm/i915/intel_csr.c:MODULE_FIRMWARE(I915_CSR_SKL);
    --
    /usr/src/linux/drivers/gpu/drm/i915/intel_huc_fw.c- SKL_HUC_FW_MINOR, SKL_BLD_NUM)
    /usr/src/linux/drivers/gpu/drm/i915/intel_huc_fw.c:MODULE_FIRMWARE(I915_SKL_HUC_UCODE);

Then configure to build the firmware file into the kernel as above.

#### [Discrete Cards firmware]

Intel\'s discrete graphics cards have a number of additional pieces of firmware resident in non-volatile storage. These are updated automatically on MS Windows by the Intel graphics drivers package. If your card has never been installed in a PC running MS Windows it may contain older versions.

[igsc] from [[[dev-util/intel-graphics-system-controller]](https://packages.gentoo.org/packages/dev-util/intel-graphics-system-controller)[]] can be used to check the versions of these items of firmware (except PCON[\[1\]](https://github.com/intel/igsc/issues/13#issuecomment-2543860100)) and upgrade them.

An independent matrix of firmware versions is maintained at [\[2\]](https://www.techpowerup.com/forums/threads/intel-arc-firmware-compilation-matrix.312440/) The firmware can be extracted from the MS Windows driver package [\[3\]](https://www.intel.com/content/www/us/en/download/785597/intel-arc-graphics-windows.html), using for example 7-Zip.

### [Kernel]

The legacy fbdev support is required since kernel 3.14.14 at least for i915 (`CONFIG_DRM_I915_FBDEV=y`).^[\[4\]](#cite_note-13)[\[5\]](#cite_note-14)^

For hybrid Intel/AMD systems, follow also the steps of [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU") drivers.

Since kernel version 4.4 the driver has moved and the legacy fbdev support is now `CONFIG_DRM_FBDEV_EMULATION=y`.

[KERNEL] **i915 Driver - Linux 6.13**

    Device Drivers  --->
        Misc devices  --->
            (only needed for DG2 onwards; see PXP related note)
            <M/*> Intel Management Engine Interface Search for <code>CONFIG_INTEL_MEI</code> to find this item.
              <M> ME Enabled Intel Chipsets Search for <code>CONFIG_INTEL_MEI_ME</code> to find this item.
              <M> Intel Trusted Execution Envrionment with ME Interface Search for <code>CONFIG_INTEL_MEI_TXE</code> to find this item.
              <M> Intel MEI GSC embedded device Search for <code>CONFIG_INTEL_MEI_GSC</code> to find this item.
              <M>   Intel visual sensing controller device transport driver Search for <code>CONFIG_INTEL_MEI_VSC_HW</code> to find this item.
              <M> Intel HDCP2.2 services of ME Interface Search for <code>CONFIG_INTEL_MEI_HDCP</code> to find this item.
              <M> Intel PXP services of Me Interface Search for <code>CONFIG_INTEL_MEI_PXP</code> to find this item.
              <M> Intel GSC Proxy services of ME Interface Search for <code>CONFIG_INTEL_MEI_GSC_PROXY</code> to find this item.
        Graphics support  --->
            <*> /dev/agpgart (AGP Support) Search for <code>CONFIG_AGP</code> to find this item. --->
                <*> Intel 440LX/BX/GX, I8xx and E7x05 chipset support Search for <code>CONFIG_AGP_INTEL</code> to find this item.
            <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support) Search for <code>CONFIG_DRM</code> to find this item. --->
                Supported DRM Clients  --->
                    [*] Enable legacy fbdev support for your modesetting driver Search for <code>CONFIG_DRM_FBDEV_EMULATION</code> to find this item.
                <M/*> Intel 8xx/9xx/G3x/G4x/HD Graphics Search for <code>CONFIG_DRM_I915</code> to find this item.
                  ()  Force probe driver for selected new Intel hardware Search for <code>CONFIG_DRM_I915_FORCE_PROBE</code> to find this item.
                  [*] Enable capturing GPU state following a hang Search for <code>CONFIG_DRM_I915_CAPTURE_ERROR</code> to find this item.
                  [*]   Compress GPU error state Search for <code>CONFIG_DRM_I915_COMPRESS_ERROR</code> to find this item.
                  [*] Always enable userptr support Search for <code>CONFIG_DRM_I915</code> to find this item.
                  [*] Enable Intel PXP Support Search for <code>CONFIG_DRM_I915_PXP</code> to find this item.
                      (only needed for DG2 onwards; enable MEI under misc devices)
                  [ ] Enable KVM host support Intel GVT-g graphics virtualization Search for <code>CONFIG_DRM_I915_GVT_KVMGT</code> to find this item.
        [*] IOMMU Hardware Support Search for <code>CONFIG_IOMMU_SUPPORT</code> to find this item. --->
            [*] Support for Intel IOMMU using DMA Remapping Devices Search for <code>CONFIG_INTEL_IOMMU_SVM</code> to find this item.
            [*]   Enable Intel DMA Remapping Devices by default Search for <code>CONFIG_INTEL_IOMMU_DEFAULT_ON</code> to find this item.
            [*]   Enable Intel IOMMU scalable mode by default Search for <code>CONFIG_INTEL_IOMMU_SCALABLE_MODE_DEFAULT_ON</code> to find this item.
            [*]   Intel IOMMU performance events Search for <code>CONFIG_INTEL_IOMMU_PERF_EVENTS</code> to find this item.

** Note**\
Kernel version 4.19 or later is recommended for Coffee Lake because it will work without enabling alpha support. Kernel 4.14 requires loading module i915 with alpha_support=1 or enabling `CONFIG_DRM_I915_ALPHA_SUPPORT` in kernel config.

** Note**\
For DG2 successful loading of the [HuC firmware](https://wiki.gentoo.org/wiki/Intel#GuC.2FHuC_firmware "Intel") requires Intel PXP support and the Intel Management Engine Interface.^[\[6\]](#cite_note-15)^

A newer, yet still experimental, driver for XE-based graphics (such as DG2 and BMG) has slowly been added to the stable kernel branch. This new driver is named [Xe](https://www.kernel.org/doc/html//next/gpu/rfc/xe.html).

[KERNEL] **Xe Driver - Linux 6.18**

    Device Drivers  --->
        Graphics Support  --->
            <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support) Search for <code>CONFIG_DRM</code> to find this item. --->
                <M> Intel Xe2 Graphics Search for <code>CONFIG_DRM_XE</code> to find this item.
                  [*] Enable display support Search for <code>CONFIG_DRM_XE_DISPLAY</code> to find this item.
                  ()  Force probe xe for selected Intel hardware IDs Search for <code>CONFIG_DRM_XE_FORCE_PROBE</code> to find this item.
                  drm/Xe Debugging  --->
                  drm/Xe Profile Guided Optimisation  --->

** Warning**\
This driver is still experimental and under development. Some features such as [fan speed monitoring](https://lore.kernel.org/dri-devel/aADWaEFKVmxSnDLo@fedora/) and others are anticipated for future kernel releases.

\
A broad overview of this module can be found at the [Xe -- Merge Acceptance Plan kernel.org](https://www.kernel.org/doc/html//next/gpu/rfc/xe.html) page. Development of the driver can be found at the [intel-xe kernel-lore page](https://lore.kernel.org/intel-xe/).\

Use This driver at your own risk!

### [X drivers]

Portage uses the [`VIDEO_CARDS`](https://wiki.gentoo.org/wiki/VIDEO_CARDS "VIDEO CARDS") variable, which expands into the [`USE_EXPAND`](https://wiki.gentoo.org/wiki//etc/portage/make.conf#USE_EXPAND "/etc/portage/make.conf") variable, for supporting various graphics cards. Assuming the [[[x11-base/xorg-drivers]](https://packages.gentoo.org/packages/x11-base/xorg-drivers)[]] package has already been installed, setting the `VIDEO_CARDS` variable in [/etc/portage/package.use] will pull in the correct video driver:

[FILE] **`/etc/portage/package.use/00video`Gen 2 and Gen 3**

    */* VIDEO_CARDS: -* intel i915

[FILE] **`/etc/portage/package.use/00video`Gen 4 and higher**

    */* VIDEO_CARDS: -* intel

** Important**\
Beginning with **x11-base/xorg-drivers-21.1**, the [[[x11-base/xorg-drivers]](https://packages.gentoo.org/packages/x11-base/xorg-drivers)[]] package changes [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") settings. This will omit selection of the deprecating [[[x11-drivers/xf86-video-intel]](https://packages.gentoo.org/packages/x11-drivers/xf86-video-intel)[]] driver by default in favor of the more maintained, generic modesetting DDX driver built into [[[x11-base/xorg-server]](https://packages.gentoo.org/packages/x11-base/xorg-server)[]]. Older systems with the [[[video_cards_i915]](https://packages.gentoo.org/useflags/video_cards_i915)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag set will continue to have the Intel DDX driver installed.

After editing [/etc/portage/packages.use/00video], update the system so the changes take effect by passing the `--changed-use --deep` options to [emerge]:

`root `[`#`]`emerge --ask --changed-use --deep @world`

Those wishing to not accept the Intel graphic driver defaults in the main repository can read on into the sub-sections below.

#### [Intel DDX]

Before proceeding with the *[Intel DDX driver](https://en.wikipedia.org/wiki/X.Org_Server#DDX "wikipedia:X.Org Server")*, note that this driver has been *slowly deprecating* for several years. Other major^[\[7\]](#cite_note-16)[\[8\]](#cite_note-17)^ Linux distributions have switched to the *modesetting DDX driver* (detailed in [the section below](https://wiki.gentoo.org/wiki/Intel#Modesetting_DDX "Intel")). Intel has not updated it for quite some time^[\[9\]](#cite_note-18)^, thus burdening Gentoo\'s X11 package maintainers.

The Intel DDX driver may be faster than the generic modesetting driver on pre-Gen11 chipsets as it is able to more closely interact with hardware acceleration of these chips using SNA. On Gen11 and newer, SNA is not supported.^[\[10\]](#cite_note-19)^ Using it is discouraged unless faced with concrete issues caused by the modesetting driver.

##### [USE flags]

Check the USE flags of [[[x11-drivers/xf86-video-intel]](https://packages.gentoo.org/packages/x11-drivers/xf86-video-intel)[]]:

### [USE flags for] [x11-drivers/xf86-video-intel](https://packages.gentoo.org/packages/x11-drivers/xf86-video-intel) [[]] [X.Org driver for Intel cards]

  ------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+sna`](https://packages.gentoo.org/useflags/+sna)           Enable SandyBridge\'s New Acceleration (useful on all chipsets, not just SandyBridge)
  [`+udev`](https://packages.gentoo.org/useflags/+udev)         Enable virtual/udev integration (device discovery, power and storage device support, etc)
  [`debug`](https://packages.gentoo.org/useflags/debug)         Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`dri`](https://packages.gentoo.org/useflags/dri)             Enable direct rendering: used for accelerated 3D and some 2D, like DMA
  [`tools`](https://packages.gentoo.org/useflags/tools)         Build the intel-virtual-output tool
  [`uxa`](https://packages.gentoo.org/useflags/uxa)             Enable UMA Acceleration Architecture
  [`valgrind`](https://packages.gentoo.org/useflags/valgrind)   Enable annotations for accuracy. May slow down runtime slightly. Safe to use even if not currently using dev-debug/valgrind
  [`xvmc`](https://packages.gentoo.org/useflags/xvmc)           Enables X-Video Motion Compensation support
  ------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2024-06-05 01:18] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

##### [Emerge]

`root `[`#`]`emerge --ask x11-drivers/xf86-video-intel`

##### [xorg.conf]

To force Xorg server to use the Intel DDX driver with SNA for hardware acceleration, the following file can be created in [/etc/X11/xorg.conf.d/]:

[FILE] **`/etc/X11/xorg.conf.d/20-intel.conf`Force Intel DDX**

    Section "Device"
        Identifier "Intel Graphics"
        Driver "intel"
        Option "AccelMethod" "sna"
        Option "DRI" "crocus"
    EndSection

The value for the `DRI` option should be `crocus` for Gen 4 through Gen 7.5 and `iris` for Gen 8 and higher. This line should be omitted for Gen 2 and Gen 3.

#### [[] Modesetting DDX]

As mentioned above, the modesetting DDX driver is now the default driver on newer Intel graphics chipsets for Gentoo. This driver uses GLAMOR to accelerate 2D graphical over Mesa (the open source OpenGL implementation). As of `x11-base/xorg-drivers-1.19` this has become the default for Gentoo.

As of `xorg-server/xorg-server-1.20.6` GLAMOR support is enabled unless the [[[minimal]](https://packages.gentoo.org/useflags/minimal)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag is enabled. No additional steps or configuration are necessary.

##### [xorg.conf]

If it\'s necessary to force Xorg to load the modesetting driver the following config snippet can be used:

[FILE] **`/etc/X11/xorg.conf.d/20-modesetting.conf`Force modesetting DDX**

    Section "Device"
        Identifier "Intel Graphics"
        Driver "modesetting"
        Option "AccelMethod" "glamor"
        Option "DRI" "3"
    EndSection

** Note**\
If both [20-intel.conf] and [20-modesetting.conf] files are defined in [/etc/X11/xorg.conf.d/], the X server will attempt to load the files in alpha-numeric order.

##### [Screen tearing]

The `TearFree` option is not enabled by default (since it increases GPU memory consumption, among other things). If experiencing screen tear, you may create the configuration file, and enable it manually:

[FILE] **`/etc/X11/xorg.conf.d/20-intel.conf`**

    Section "Device"
        Identifier "Intel Graphics"
        Driver "intel"
        Option "TearFree" "true"
    EndSection

Other options against screen tearing:

1.  Use [Sway](https://wiki.gentoo.org/wiki/Sway "Sway") (implementation of [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") protocol, that is tear free by design) instead of Xorg.
2.  Use [[[media-libs/mesa]](https://packages.gentoo.org/packages/media-libs/mesa)[]], and [Plasma 6](https://wiki.gentoo.org/wiki/KDE#Starting_Plasma "KDE"). The Info Center reports wrong `VIDEO_CARDS` and kernel DRMs as `Graphics Processor: llvmpipe`. Correct settings show `Graphics Platform: Wayland` and `Graphics Processor: Mesa Intel`.

##### [Enable early KMS]

To enable [Kernel Mode Setting (KMS)](https://www.kernel.org/doc/html/latest/gpu/drm-kms.html) as soon as possible, modesetting either needs to be built into the kernel, or be loaded with initramfs if it is built as a module. Distribution Kernels have the Modesetting DDX built as a module. So, in order to get early KMS, those who use it have to create a .conf file in [/etc/dracut.conf.d] and do the following:

[FILE] **`/etc/dracut.conf.d/intel.conf`**

    add_drivers+=" i915 "

Then run:

`root `[`#`]`dracut`

Users of gentoo-kernel can also use savedconfig to change modesetting from module to built-in.

### [VAAPI]

Intel GMA X4500HD / G45 / GM45 (late [Gen 4](https://en.wikipedia.org/wiki/List_of_Intel_graphics_processing_units#Gen4 "wikipedia:List of Intel graphics processing units")) and newer supports [VAAPI](https://wiki.gentoo.org/wiki/VAAPI "VAAPI") hardware video acceleration with package [[[media-libs/libva-intel-driver]](https://packages.gentoo.org/packages/media-libs/libva-intel-driver)[]].

`root `[`#`]`emerge -a media-libs/libva-intel-driver`

Newer Intel graphics since [Gen 8](https://en.wikipedia.org/wiki/List_of_Intel_graphics_processing_units#Gen8 "wikipedia:List of Intel graphics processing units") (Broadwell) have better support with [[[media-libs/libva-intel-media-driver]](https://packages.gentoo.org/packages/media-libs/libva-intel-media-driver)[]].

`root `[`#`]`emerge -a media-libs/libva-intel-media-driver`

If mesa shows

`root `[`#`]`emerge -v media-libs/mesa`

    * Ignoring USE=vaapi      since VIDEO_CARDS does not contain d3d12, nouveau, r600, radeonsi, or virgl

this seems to be OK for Intel cards. At least [https://forums.gentoo.org/viewtopic-t-1148798-highlight-mesa+vaapi+intel.html](https://forums.gentoo.org/viewtopic-t-1148798-highlight-mesa+vaapi+intel.html) says so and vainfo correctly states that VAAPI is supported on relevant systems.

### [Vulkan]

Vulkan is supported in the main ebuild repository for Intel Core processors using the Mesa driver^[\[11\]](#cite_note-20)^.

This will build a working Vulkan driver, but it will not provide a [libvulkan.so.1], but a drivers-specific [libvulkan_intel.so]. The package [[[media-libs/vulkan-loader]](https://packages.gentoo.org/packages/media-libs/vulkan-loader)[]] provides [libvulkan.so.1].

If [libvulkan_intel.so] is missing, then you need to compile [[[media-libs/mesa]](https://packages.gentoo.org/packages/media-libs/mesa)[]] with the [[[vulkan]](https://packages.gentoo.org/useflags/vulkan)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag.

### [Tools]

[[[x11-apps/igt-gpu-tools]](https://packages.gentoo.org/packages/x11-apps/igt-gpu-tools)[]] provides utilities for debugging.

For example, GPU min/max/current frequency can be displayed by:

`root `[`#`]`intel_gpu_frequency`

The [intel_gpu_top] utility displays the current GPU state in a [top]-like fashion:

`root `[`#`]`intel_gpu_top`

    intel-gpu-top: Intel Ivybridge (Gen7) @ /dev/dri/card0
        437/ 441 MHz;  57% RC6;  0.70/12.20 W;       45 irqs/s

          IMC reads:        2 MiB/s
         IMC writes:      618 MiB/s

             ENGINES     BUSY                           MI_SEMA MI_WAIT
           Render/3D    8.99% |██                     |      0%      0%
             Blitter    0.00% |                       |      0%      0%
               Video    0.00% |                       |      0%      0%

** Tip**\
**Video BUSY** on 0% means that hardware decoding/encoding is not used.

## [Configuration]

### [Kernel]

#### [Fastboot]

The i915 kernel driver reduces flickering caused by modesetting operations during boot time. It does so by avoiding unnecessary modesetting operations ^[\[12\]](#cite_note-21)^. Fastboot is enabled by default on Skylake, Valleyview, Cherry Trail, and newer CPUs.

For CPUs older than Skylake, fastboot can be enabled by passing the `i915.fastboot=1` parameter to the i915 kernel driver during boot. This can either be set using the built-in kernel command-line or via a bootloader\'s kernel options. [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB") users can see the [/etc/default/grub] file.

### [Permissions]

If the [`acl`](https://packages.gentoo.org/useflags/acl) USE flag is enabled globally and [`elogind`](https://packages.gentoo.org/useflags/elogind) is being used (default for desktop profiles) permissions to video cards will be handled automatically. It is possible to check the permissions using [getfacl]:

`user `[`$`]`getfacl /dev/dri/card0 | grep larry`

`user:`**`larry`**`:rw-`

A broader solution is to add the user(s) needing access the video card to the [video] group:

`root `[`#`]`gpasswd -a larry video`

Note that users will be able to run X without permission to the DRI subsystem, but hardware acceleration will be disabled.

### [xorg.conf]

Choose one of the following configurations.

Classic (Intel DDX) driver [[[x11-drivers/xf86-video-intel]](https://packages.gentoo.org/packages/x11-drivers/xf86-video-intel)[]]:

The X server is not aware of i915 or i965 they will need to be addressed as Driver `intel`.

[FILE] **`/etc/X11/xorg.conf.d/intel.conf`Explicit intel driver section**

    Section "Device"
       Identifier  "intel"
       Driver      "intel"
    EndSection

Gen 4+ driver (Mesa\'s modesetting):

** Note**\
Experiences of this configuration can be found in the [Discussion](https://wiki.gentoo.org/wiki/Talk:Intel "Talk:Intel") of this page. Add any difficulties there so this section can be improved.

As of xorg-server-1.17, the modesetting driver was moved into [[[x11-base/xorg-server]](https://packages.gentoo.org/packages/x11-base/xorg-server)[]]. This driver has more features than the classic driver, such as the ability to support acceleration via GLAMOR.

This configuration is the default for `VIDEO_CARDS="intel i965"` beginning with x11-base/xorg-drivers-1.19. If the classic (Intel CCX) driver is desired, then [[[x11-drivers/xf86-video-intel]](https://packages.gentoo.org/packages/x11-drivers/xf86-video-intel)[]] must be installed manually:

`root `[`#`]`emerge --ask x11-drivers/xf86-video-intel`

xorg-server is easily configured to prefer `modesetting` over the older `intel` driver.

[FILE] **`/etc/X11/xorg.conf.d/modesetting.conf`Explicit modesetting driver section**

    Section "Device"
       Identifier  "modesetting"
       Driver      "modesetting"
    EndSection

The [X server](https://wiki.gentoo.org/wiki/X_server "X server") is designed to work out-of-the-box, with no need to manually edit X.Org\'s configuration files. It should detect and configure devices such as displays, keyboards, and mice.

In any case, the main configuration file of the X server is the [xorg.conf](https://wiki.gentoo.org/wiki/Xorg.conf "Xorg.conf").

## [Troubleshooting]

-   [[[Gentoo bugtracker: known bugs]](https://bugs.gentoo.org/buglist.cgi?quicksearch=xf86-video-intel&order=bug_id%20DESC)[]]
-   [[[Freedesktop.org bugtracker: known bugs]](https://bugs.freedesktop.org/buglist.cgi?bug_status=UNCONFIRMED&bug_status=NEW&bug_status=CONFIRMED&bug_status=ASSIGNED&bug_status=REOPENED&bug_status=NEEDINFO&bug_status=PLEASETEST&bug_status=IN_PROGRESS&product=xorg&component=Driver%2Fintel&order=bug_id%20DESC)[]]
-   [[[Freedesktop.org bugtracker: known bugs]](https://bugs.freedesktop.org/buglist.cgi?bug_status=UNCONFIRMED&bug_status=NEW&bug_status=CONFIRMED&bug_status=ASSIGNED&bug_status=REOPENED&bug_status=NEEDINFO&bug_status=PLEASETEST&bug_status=IN_PROGRESS&product=DRI&component=DRM%2FIntel&order=bug_id%20DESC)[]]
-   The modesetting DDX might cause video out of sync artifacts (when scrolling, or on videos) (see [\[4\]](https://forums.gentoo.org/viewtopic-p-8538508.html#8538508)). If the system experiences such artifacts, try the [DDX driver](https://wiki.gentoo.org/wiki/Intel#Modesetting_DDX "Intel").

### [Screen flickering]

Panel Self Refresh (PSR), a power saving feature used by Intel iGPUs, causes flickering in some instances. A temporary solution is to disable this feature using the kernel parameter `i915.enable_psr=0`

### [KDE Plasma eating CPU]

If [/usr/bin/plasmashell] is always consuming several percent of CPU, perhaps this is related to a vsync problem. Qt Quick Animation seems to loop too fast when the driver does not manage vsync ([Reference](https://bugreports.qt.io/browse/QTBUG-45959)).

A way to enable vsync with SNA is to enable the `TearFree` option in [xorg.conf]:

[FILE] **`/etc/X11/xorg.conf.d/20-intel.conf`**

    Section "Device"
        Identifier "Device0"
        Driver "intel"
        Option "AccelMethod" "SNA"
        Option "TearFree" "true"
    EndSection

See also [this](https://community.linuxmint.com/tutorial/view/2304) Linux Mint tutorial.

### [Black screen]

`CONFIG_FRAMEBUFFER_CONSOLE` must be set to \"y\" (i.e. built-in to the kernel). Otherwise, it is possible to always have a black screen unless `nomodeset` is passed to the kernel, thus disabling kernel mode setting (KMS). `acpi_osi="Linux"` can be passed to the kernel command line to try to solve this issue. This is usually done through the bootloader.

Kernel with version 4.2 or newer is needed with some 8th generation chipsets^[\[13\]](#cite_note-22)^.

### [Brightness does not change with keyboard shortcuts]

First, make sure vendor compatibility is on in the kernel configuration: Toshiba for Toshiba, etc.

If it is, or when the brightness buttons are working, the issue is that the kernel can not detect *where* the brightness control is.

Luckily, this is easy enough to modify, as long as the kernel version is \>= 3.13.x and \< 4.2.

Add the following argument to the kernel command-line:

[CODE] **Pre-4.2 kernel command-line argument**

    video.use_native_backlight=1

On kernels \>= 4.2, the [video.use_native_backlight] option is no longer available.^[\[14\]](#cite_note-23)^ One of the following should be used instead (experiment to see which works on the system):

[CODE] **4.2+ kernel command-line argument**

    acpi_backlight=video

[CODE] **4.2+ kernel command-line argument**

    acpi_backlight=native

[CODE] **4.2+ kernel command-line argument**

    acpi_backlight=vendor

Do the key bindings map to actions viewable in xev? Can the screen brightness be adjusted using [xbacklight]? You can always do a work around via a keyboard remapping. For [LXDE](https://wiki.gentoo.org/wiki/LXDE "LXDE") it can be done via:

[FILE] **`~/.config/openbox/lxde-rc.xml`**

    <keybind key="XF86MonBrightnessUp">
        <action name="Execute">
            <command>xbacklight +5</command>
        </action>
    </keybind>
    <keybind key="XF86MonBrightnessDown">
        <action name="Execute">
            <command>xbacklight -5</command>
        </action>
    </keybind>

** Warning**\
With the [Modesetting DDX](https://wiki.gentoo.org/wiki/Intel#Modesetting_DDX "Intel"), the [[[x11-apps/xbacklight]](https://packages.gentoo.org/packages/x11-apps/xbacklight)[]] package will not work^[\[15\]](#cite_note-24)^. Use [[[sys-power/acpilight]](https://packages.gentoo.org/packages/sys-power/acpilight)[]] for a compatible interface.

## [See also]

-   [Xorg/Guide](https://wiki.gentoo.org/wiki/Xorg/Guide "Xorg/Guide") --- explains what Xorg is, how to install it, and the various configuration options.
-   [Hprofile](https://wiki.gentoo.org/wiki/Hprofile "Hprofile") --- an application that can be used to manage multiple profiles be it hardware or software.

## [External resources]

-   [https://www.x.org/wiki/IntelGraphicsDriver/](https://www.x.org/wiki/IntelGraphicsDriver/) - Intel at the X.Org wiki.
-   [https://keyj.emphy.de/files/linuxgraphics_en.pdf](https://keyj.emphy.de/files/linuxgraphics_en.pdf) - Linux Graphics Demystified.

## [References]

1.  [[↑ ^[1.0](#cite_ref-firmware_10-0)^ ^[1.1](#cite_ref-firmware_10-1)^ ^[1.2](#cite_ref-firmware_10-2)^] [[Firmware](https://01.org/linuxgraphics/downloads/firmware), Intel. Retrieved on October 27, 2018]]
2.  [[[↑](#cite_ref-11)] [[https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/commit/i915?id=067440c18f220ee03121b7e4c3615fe7e1f3f67a](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/commit/i915?id=067440c18f220ee03121b7e4c3615fe7e1f3f67a)]]
3.  [[[↑](#cite_ref-12)] [[https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/commit/?id=51fff4e69b4554dd3fee21e3c55a0f94937293e3](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/commit/?id=51fff4e69b4554dd3fee21e3c55a0f94937293e3)]]
4.  [[[↑](#cite_ref-13)] [Gentoo Forums, [\"Black screen on boot after kernel upgrade - grub2\"](https://forums.gentoo.org/viewtopic-t-998526.html)]]
5.  [[[↑](#cite_ref-14)] [Gentoo Forums, [\"Black screen on kernel 3.14.14\"](https://forums.gentoo.org/viewtopic-p-7596748.html)]]
6.  [[[↑](#cite_ref-15)] [[https://gitlab.freedesktop.org/drm/intel/-/issues/7732#note_1708266](https://gitlab.freedesktop.org/drm/intel/-/issues/7732#note_1708266)]]
7.  [[[↑](#cite_ref-16)] [[https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/AUPYPJMFJZMHPEKN24LBABZKIEOV4NU5/](https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/AUPYPJMFJZMHPEKN24LBABZKIEOV4NU5/)]]
8.  [[[↑](#cite_ref-17)] [[https://tjaalton.wordpress.com/2016/07/23/intel-graphics-gen4-and-newer-now-defaults-to-modesetting-driver-on-x/](https://tjaalton.wordpress.com/2016/07/23/intel-graphics-gen4-and-newer-now-defaults-to-modesetting-driver-on-x/)]]
9.  [[[↑](#cite_ref-18)] [[https://cgit.freedesktop.org/xorg/driver/xf86-video-intel/log/](https://cgit.freedesktop.org/xorg/driver/xf86-video-intel/log/)]]
10. [[[↑](#cite_ref-19)] [[https://gitlab.freedesktop.org/drm/intel/-/issues/1864](https://gitlab.freedesktop.org/drm/intel/-/issues/1864)]]
11. [[[↑](#cite_ref-20)] [[https://bugs.gentoo.org/show_bug.cgi?id=580148#c25](https://bugs.gentoo.org/show_bug.cgi?id=580148#c25)]]
12. [[[↑](#cite_ref-21)] [[\[Intel-gfx\] \[RFC\] fastboot](https://lists.freedesktop.org/archives/intel-gfx/2012-May/017653.html), freedesktop.org. Retrieved on February 9, 2019]]
13. [[[↑](#cite_ref-22)] [Gentoo Forums, [\"N3700 8086:22b1 i915 black screen, works in kernel 4.2.6\"](https://forums.gentoo.org/viewtopic-t-1034212.html)]]
14. [[[↑](#cite_ref-23)] [RedHat Bug 1272633: [\"video.use_native_backlight=1 doesn\'t work\" (comment 5)](https://bugzilla.redhat.com/show_bug.cgi?id=1272633#c5)]]
15. [[[↑](#cite_ref-24)] [Freedesktop Bug 96572: [\"xbacklight doesn\'t work with modesetting on intel\"](https://bugs.freedesktop.org/show_bug.cgi?id=96572)]]