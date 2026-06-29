**AMDVLK** ([AMD Open source Driver for Vulkan](https://github.com/GPUOpen-Drivers/AMDVLK)) is an open-source Vulkan driver for AMD Radeon™ graphics adapters on Linux led by the [GPUOpen](https://en.wikipedia.org/wiki/GPUOpen) initiative.

AMDVLK can work with the [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU") driver or on a headless system. It also greatly supports interoperability with the [mesa RADV](https://wiki.gentoo.org/wiki/Vulkan "Vulkan") driver.

As of September 2025, AMDVLK was discontinued by AMD in favor of focusing on Mesa\'s RADV driver^[\[1\]](#cite_note-1)^

[![AMDVLK-illust.png](/images/thumb/2/23/AMDVLK-illust.png/300px-AMDVLK-illust.png)](https://wiki.gentoo.org/wiki/File:AMDVLK-illust.png)

[](https://wiki.gentoo.org/wiki/File:AMDVLK-illust.png "Enlarge")

## Contents

-   [[1] [Prerequisites]](#Prerequisites)
    -   [[1.1] [Source-based or prebuilt?]](#Source-based_or_prebuilt.3F)
    -   [[1.2] [Hardware detection]](#Hardware_detection)
    -   [[1.3] [Choosing the right driver version]](#Choosing_the_right_driver_version)
        -   [[1.3.1] [Mainline supported models (:0 slot)]](#Mainline_supported_models_.28:0_slot.29)
        -   [[1.3.2] [Legacy supported models for *:legacy-polaris* slot]](#Legacy_supported_models_for_:legacy-polaris_slot)
        -   [[1.3.3] [Very old models for *:legacy-si* slot]](#Very_old_models_for_:legacy-si_slot)
    -   [[1.4] [Vulkan ICD]](#Vulkan_ICD)
-   [[2] [Vital preparations]](#Vital_preparations)
    -   [[2.1] [Enable the GURU ebuild repository]](#Enable_the_GURU_ebuild_repository)
    -   [[2.2] [Turn on DRI3 and disable modesetting X driver]](#Turn_on_DRI3_and_disable_modesetting_X_driver)
-   [[3] [Installation]](#Installation)
    -   [[3.1] [Binary driver]](#Binary_driver)
    -   [[3.2] [Source-based driver]](#Source-based_driver)
        -   [[3.2.1] [Raytracing support and DXC]](#Raytracing_support_and_DXC)
        -   [[3.2.2] [Additional system requirements to build]](#Additional_system_requirements_to_build)
-   [[4] [Configuration and features]](#Configuration_and_features)
    -   [[4.1] [Mesa RADV interoperability]](#Mesa_RADV_interoperability)
    -   [[4.2] [Runtime settings]](#Runtime_settings)
    -   [[4.3] [Headless usage]](#Headless_usage)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Wrong ELF class]](#Wrong_ELF_class)
    -   [[5.2] [Known issues and limitations]](#Known_issues_and_limitations)
        -   [[5.2.1] [Known issues for mainline driver]](#Known_issues_for_mainline_driver)
        -   [[5.2.2] [Known issues for *:legacy-polaris* and *:legacy-si*]](#Known_issues_for_:legacy-polaris_and_:legacy-si)
-   [[6] [See also]](#See_also)
-   [[7] [References]](#References)

## [Prerequisites]

### [][Source-based or prebuilt?]

In 2023, it became clear that source-based driver is very difficult to maintain due to it\'s big requirements. So **media-libs/amdvlk-bin** was introduced. This is the ported driver binary from RHEL/Debian built by AMD itself. It does not require compilation, so it can be installed easily, but still provides more than 90% performance of source-based one.

At this moment there are two possible variants:

1.  **media-libs/amdvlk** for compiling from source code.
2.  **media-libs/amdvlk-bin** provides binaries built by AMD itself.

it\'s recommended to seek for **media-libs/amdvlk-bin** first.

### [Hardware detection]

Follow the hardware detection guide on the [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU#Hardware_detection "AMDGPU") page if in doubt.

### [Choosing the right driver version]

Starting from 2023.Q4.1 AMDVLK dropped support for old Pre-GFX10 GPU models. To support old hardware and to reduce the e-waste, an AMDVLK maintainer has decided to keep those old versions as separate [slot](https://wiki.gentoo.org/wiki/SLOT "SLOT") called **legacy-polaris**.

[Check the AMDVLK page on GitHub](https://github.com/GPUOpen-Drivers/AMDVLK#product-support) for the actual supported hardware.

#### [][Mainline supported models (:0 slot)]

It is supporting the following (since 2024.Q1.1):

-   Radeon™ RX 7900/7800/7700/7600 Series
-   Radeon™ RX 6900/6800/6700/6600/6500 Series
-   Radeon™ RX 5700/5600/5500 Series
-   Radeon™ Pro W5700/W5500 Series

#### [Legacy supported models for *:legacy-polaris* slot]

The last driver which supports legacy graphics cards is [2023.Q3.3](https://github.com/GPUOpen-Drivers/AMDVLK/releases/tag/v-2023.Q3.3). It supports vulkan **1.3.264** with the following GPUs:

-   Radeon™ RX Vega Series
-   Radeon™ RX 400/500 Series
-   Radeon™ Pro WX 9100, x200 Series
-   Radeon™ Pro W5700/W5500 Series
-   Radeon™ Pro 400/500 Series *(probably?)*

Although the \"2023.Q3.3\" also supports modern GPUs, in general it is not the best fit for them.

#### [Very old models for *:legacy-si* slot]

This is very old driver (3y+ old), it only support vulkan version **1.2.179** and is added primary as an experiment. It supports:

-   Radeon™ R5/R7/R9 200/300 Series
-   Radeon™ RX 400/500 Series
-   Radeon™ M200/M300/M400 Series
-   Radeon™ HD 8000M Series
-   Radeon™ HD 7000 Series
-   AMD FirePro™ Workstation Wx000/Wx100/Wx300 Series

All of these GPUs is more than 8 years old.

### [Vulkan ICD]

The driver automatically pulls the vulkan ICD loader package. Check the [Vulkan](https://wiki.gentoo.org/wiki/Vulkan "Vulkan") page for more information on choosing a Vulkan driver.

## [Vital preparations]

### [Enable the GURU ebuild repository]

** Important**\
The Gentoo Security team warns: GURU repository packages are manually reviewed by trusted contributors. However, the repository is primarily maintained by other users. It\'s not recommended to use this repository on hardened systems, in a critical environment, or if the testing (\~amd64) packages is prohibited.

The AMDVLK packages can be found in the [GURU overlay](https://wiki.gentoo.org/wiki/Project:GURU "Project:GURU"). It\'s maintained by [User:RarogCmex](https://wiki.gentoo.org/wiki/User:RarogCmex "User:RarogCmex"). Follow the guide [Project:GURU/Information for End Users](https://wiki.gentoo.org/wiki/Project:GURU/Information_for_End_Users "Project:GURU/Information for End Users") to enable GURU ebuild repository.

### [Turn on DRI3 and disable modesetting X driver]

** Note**\
This section is for Xorg users only. Wayland users can skip this section.

On systems that use Gentoo\'s mainline [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU") driver stack, **there is a high chance that all necessary stuff is already available**: DRI3 and xf86-video-amdgpu driver configured and installed. If not, follow the [Xorg/Hardware_3D_acceleration_guide](https://wiki.gentoo.org/wiki/Xorg/Hardware_3D_acceleration_guide "Xorg/Hardware 3D acceleration guide") and [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU") to configure it. Generally, the following lines may need to be added to the [[xorg.conf](https://wiki.gentoo.org/wiki/Xorg.conf "Xorg.conf")] file:

[FILE] **`/etc/X11/xorg.conf`**

    Section "Device"
    Identifier "AMDgpu"
    Option  "DRI" "3"
    EndSection

Ensure that there is no **Driver \"modesetting\"** line in the [xorg.conf] file.

## [Installation]

### [Binary driver]

Add [::GURU](https://wiki.gentoo.org/wiki/AMDVLK#Vital_preparations "AMDVLK"), then install it with the [right slot version](https://wiki.gentoo.org/wiki/AMDVLK#Choosing_the_right_driver_version "AMDVLK"):

For mainline:

`root `[`#`]`emerge --ask media-libs/amdvlk-bin:0`

For legacy-polaris:

`root `[`#`]`emerge --ask media-libs/amdvlk-bin:legacy-polaris`

For legacy-si:

`root `[`#`]`emerge --ask media-libs/amdvlk-bin:legacy-si`

That\'s all.

### [Source-based driver]

**media-libs/amdvlk** has a [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") to add [wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") support. If wayland support is necessary then be sure to set the flag and re-emerge:

`root `[`#`]`emerge --ask media-libs/amdvlk`

After installation Xorg or [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") may require re-configuring.

#### [Raytracing support and DXC]

`media-libs/amdvlk` since 2022.4.3 support raytracing via corresponding use flag and requires the [[[dev-util/DirectXShaderCompiler]](https://packages.gentoo.org/packages/dev-util/DirectXShaderCompiler)[]] package from the GURU overlay to build its support. However, for compatibility purposes, it\'s generally recommended to always keep this flag enabled, unless there\'s a (weak) CPU limitation.

#### [Additional system requirements to build]

16 GiB of RAM is recommended to successfully build the AMDVLK driver from source. However, on systems with less than 16 GiBs of RAM, one workaround may be building the driver using a single thread; i.e. `MAKEOPTS="-j1"`. You may have to play around with different compilation flags, depending on your system. Use `CHECKREQS_DONOTHING=1` to bypass the memory checking during installation ([check-reqs.eclass](https://devmanual.gentoo.org/eclass-reference/check-reqs.eclass/index.html)).

For example, this can be performed in a one-shot from the command-line as follows:

`root `[`#`]`CHECKREQS_DONOTHING=1 MAKEOPTS="-j1" emerge --ask media-libs/amdvlk`

*UPD: There are successful experiments building it in a VM with the \"-O1\" optimization flag and 6GB RAM*

## [Configuration and features]

### [Mesa RADV interoperability]

AMDVLK can be simultaneously installed with mesa\'s RADV driver. If RADV is also installed in the system, the AMDVLK driver will be enabled by default after installation. It\'s possible to switch between AMDVLK and RADV by setting an environment variable `AMD_VULKAN_ICD=AMDVLK` or `AMD_VULKAN_ICD=RADV`.

### [Runtime settings]

The driver exposes many settings that can customize the driver\'s behavior and facilitate debugging. Settings can be added into the [amdVulkanSettings.cfg] or [amdPalSettings.cfg] files under one of the paths below, formatted with one name/value pair per-line:

-   [/etc/amd]
-   \$

See the [AMDVLK Github Page](https://github.com/GPUOpen-Drivers/AMDVLK#runtime-settings) for the full list of settings.

### [Headless usage]

AMDVLK can be installed and used on headless systems to run headless Vulkan applications (e.g. *waifu2x-ncnn-vulkan*).

## [Troubleshooting]

### [Wrong ELF class]

That misleading error occurs if using a multilib system. See the [Vulkan#Wrong_ELF_class](https://wiki.gentoo.org/wiki/Vulkan#Wrong_ELF_class "Vulkan").

### [Known issues and limitations]

[See GitHub page](https://github.com/GPUOpen-Drivers/AMDVLK#known-issues).

The package maintainer ([User:RarogCmex](https://wiki.gentoo.org/wiki/User:RarogCmex "User:RarogCmex")) warns about:

-   Usage with DRI_PRIME with lead nvidia GPU is impossible at this moment because the driver does not work with *modesetting*.

#### [Known issues for mainline driver]

-   If you are using upstream stack, you may need to upgrade the kernel to 5.3 or later version and firmware (under /lib/firmware/amdgpu/) to the right version (*sys-kernel/linux-firmware*), and then update [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs")
-   Timeline semaphore is not fully supported in Linux kernel until version 5.5. You can install Vulkan timeline semaphore layer to enable the extension if you are using earlier version of Linux kernel

#### [Known issues for *:legacy-polaris* and *:legacy-si*]

-   CTS may hang in VK.synchronization.internally_synchronized_objects.pipeline_cache_compute with Linux kernel versions lower than 4.13
-   The driver can only work with firmware of ME feature version \>= 25 (it is possible to check the version with command \"sudo cat /sys/kernel/debug/dri/0/amdgpu_firmware_info\"). If using upstream stack with GPUs of SI or CI family, it may needed to upgrade the kernel to 4.19 or later version and firmware (under /lib/firmware/amdgpu/) to the right version from [https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/tree/amdgpu](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/tree/amdgpu), and then update ramfs (sudo mkinitramfs -o /boot/initrd.img-\`uname -r\` \`uname -r\`)
-   Timeline semaphore is not fully supported in Linux kernel until version 5.5. It is possible to install Vulkan timeline semaphore layer to enable the extension if using earlier version of the Linux kernel.

## [See also]

-   [Vulkan](https://wiki.gentoo.org/wiki/Vulkan "Vulkan") --- a next-generation graphics API created by The Khronos Group.
-   [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU") --- the open source graphics drivers for AMD Radeon and other GPUs.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://github.com/GPUOpen-Drivers/AMDVLK/discussions/416](https://github.com/GPUOpen-Drivers/AMDVLK/discussions/416)]]