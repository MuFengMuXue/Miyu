This page contains [[changes](https://wiki.gentoo.org/index.php?title=Vulkan&oldid=1409783&diff=1424748)] which are not marked for translation.

Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Vulkan/hu "Vulkan (16% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Vulkan/ja "Vulkan (42% translated)")

**Resources**

[[]][Home](https://www.khronos.org/vulkan/)

[[]][Blog](https://www.vulkan.org/blog)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Vulkan_(API) "wikipedia:Vulkan (API)")

**Vulkan** is a next-generation graphics API created by The Khronos Group. It\'s designed to be used across a variety of platforms, from desktop to mobile computers.

Compared to [OpenGL](https://wiki.gentoo.org/wiki/OpenGL "OpenGL"), Vulkan is a much lower-level API and enables developers to squeeze more performance out of a video card.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Prerequisites]](#Prerequisites)
        -   [[1.1.1] [ICDs]](#ICDs)
        -   [[1.1.2] [Mesa]](#Mesa)
    -   [[1.2] [Loader]](#Loader)
    -   [[1.3] [Development]](#Development)
-   [[2] [Usage]](#Usage)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Wrong ELF class]](#Wrong_ELF_class)
-   [[4] [See also]](#See_also)
-   [[5] [References]](#References)

## [Installation]

### [Prerequisites]

#### [ICDs]

To use Vulkan in any useful capacity, at least one ICD (Installable Client Driver) is required. ICDs may already be installed on the system, depending on the value(s) assigned to the [VIDEO_CARDS](https://wiki.gentoo.org/wiki/Make.conf#VIDEO_CARDS "Make.conf") variable. The current Vulkan support table is provided below:

  -------------------------------------------------------- -------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------
  Driver name                                              `VIDEO_CARDS` value   Package                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               Supported
  RADV                                                     `amdgpu`                         [[[media-libs/mesa]](https://packages.gentoo.org/packages/media-libs/mesa)[]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   Yes^1^
  [AMDVLK](https://wiki.gentoo.org/wiki/AMDVLK "AMDVLK")   `amdgpu`                         [[[media-libs/amdvlk]](https://packages.gentoo.org/packages/media-libs/amdvlk)[]] or [[[media-libs/amdvlk-bin]](https://packages.gentoo.org/packages/media-libs/amdvlk-bin)[]] from [GURU repository](https://wiki.gentoo.org/wiki/Project:GURU "Project:GURU")   Almost^5^
  radeon/r600                                              N/A                              N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   No
  RADV                                                     `radeonsi`                       [[[media-libs/mesa]](https://packages.gentoo.org/packages/media-libs/mesa)[]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   Yes^1^
  ANV                                                      `intel`                          [[[media-libs/mesa]](https://packages.gentoo.org/packages/media-libs/mesa)[]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   Yes^2^
  NVK                                                      `nouveau nvk`                    [[[x11-drivers/xf86-video-nouveau]](https://packages.gentoo.org/packages/x11-drivers/xf86-video-nouveau)[]] [[[media-libs/mesa]](https://packages.gentoo.org/packages/media-libs/mesa)[]]                                                                  Yes^4^
  NVIDIA                                                   `nvidia`                         [[[x11-drivers/nvidia-drivers]](https://packages.gentoo.org/packages/x11-drivers/nvidia-drivers)[]]                                                                                                                                                                                                                                                                                                                                                                                                                                                  Yes^3^
  -------------------------------------------------------- -------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------

^1^ Uses the *RADV* Vulkan driver included in Mesa.

^2^ Uses the *ANV* Vulkan driver included in Mesa. Partial support begins on Ivy Bridge and up, more information can be found on [intel](https://wiki.gentoo.org/wiki/Intel#Feature_support "Intel").

^3^ Uses the *NVIDIA* Vulkan driver included in [NVIDIA/nvidia-drivers](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers "NVIDIA/nvidia-drivers").

^4^ Currently supports Maxwell (some GTX 700 and 800 series, most 900 series) and later GPUs up to and including Ada, requires at least a Linux 6.6 kernel.^[\[1\]](#cite_note-1)^

^5^ Uses the [AMDVLK](https://wiki.gentoo.org/wiki/AMDVLK "AMDVLK") aka *AMD Open Source Driver for Vulkan* and maintained in GURU. Therefore it has not been placed in `::gentoo` yet.

It may be useful to check the [Vulkan Hardware Database](https://vulkan.gpuinfo.org/) which has detailed GPU hardware capabilities for Vulkan-capable GPUs.

#### [Mesa]

To enable the Vulkan drivers in [[[media-libs/mesa]](https://packages.gentoo.org/packages/media-libs/mesa)[]], set the [[[vulkan]](https://packages.gentoo.org/useflags/vulkan)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE](https://wiki.gentoo.org/wiki/USE "USE") flag.

### [Loader]

Applications don\'t interact with these ICDs directly, but use the [Vulkan Loader](https://github.com/KhronosGroup/Vulkan-Loader#introduction) provided by the package [[[media-libs/vulkan-loader]](https://packages.gentoo.org/packages/media-libs/vulkan-loader)[]]. This loader picks the correct ICD for the application and handles inserting Vulkan layers.

Any packages that are built with Vulkan support will pull in [[[media-libs/vulkan-loader]](https://packages.gentoo.org/packages/media-libs/vulkan-loader)[]], but it can also be installed manually:

`root `[`#`]`emerge --ask media-libs/vulkan-loader`

### [USE flags for] [media-libs/vulkan-loader](https://packages.gentoo.org/packages/media-libs/vulkan-loader) [[]] [Vulkan Installable Client Driver (ICD) Loader]

  ----------------------------------------------------------- ---------------------------------
  [`X`](https://packages.gentoo.org/useflags/X)               Add support for X11
  [`layers`](https://packages.gentoo.org/useflags/layers)     Include the vulkan layers
  [`wayland`](https://packages.gentoo.org/useflags/wayland)   Enable dev-libs/wayland backend
  ----------------------------------------------------------- ---------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-16 08:15] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Development]

To use Vulkan Validation layers, set the [[[layers]](https://packages.gentoo.org/useflags/layers)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag on [[[media-libs/vulkan-loader]](https://packages.gentoo.org/packages/media-libs/vulkan-loader)[]]. This will pull in [[[media-libs/vulkan-layers]](https://packages.gentoo.org/packages/media-libs/vulkan-layers)[]] automatically.

To use [vulkaninfo] or [vkcube] for verifying if Vulkan works, install [[[dev-util/vulkan-tools]](https://packages.gentoo.org/packages/dev-util/vulkan-tools)[]]:

`root `[`#`]`emerge --ask dev-util/vulkan-tools`

This is not related with [VulkanTools](https://github.com/LunarG/VulkanTools), part of the LunarG Vulkan SDK and currently not packaged on Gentoo.

## [Usage]

Support for Vulkan in Gentoo packages can be controlled by setting the [[[vulkan]](https://packages.gentoo.org/useflags/vulkan)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag. For example, [[[media-libs/libsdl2]](https://packages.gentoo.org/packages/media-libs/libsdl2)[]] can optionally enable Vulkan support if set.

## [Troubleshooting]

### [Wrong ELF class]

This error that may appear when running [vulkaninfo] diagnostic tool from [[[dev-util/vulkan-tools]](https://packages.gentoo.org/packages/dev-util/vulkan-tools)[]] and used for Vulkan debugging.

     ERROR: [Loader Message] Code 0 : /usr/lib32/libvulkan_intel.so: wrong ELF class: ELFCLASS32
     ERROR: [Loader Message] Code 0 : /usr/lib32/libvulkan_radeon.so: wrong ELF class: ELFCLASS32

This error can be ignored as both 32-bit and 64-bit drivers are attempted to be loaded on a multilib system.

For more information please see [Vulkan-Loader\'s issue #108](https://github.com/KhronosGroup/Vulkan-Loader/issues/108).

## [See also]

-   [Xorg/Hardware 3D acceleration guide](https://wiki.gentoo.org/wiki/Xorg/Hardware_3D_acceleration_guide "Xorg/Hardware 3D acceleration guide") --- a guide to getting 3D acceleration working using the DRM with Xorg in Gentoo.
-   [OpenGL](https://wiki.gentoo.org/wiki/OpenGL "OpenGL") --- a graphics API created by The Khronos Group.
-   [OpenCL](https://wiki.gentoo.org/wiki/OpenCL "OpenCL") --- a framework for writing programs that execute across heterogeneous computing platforms (CPUs, GPUs, DSPs, FPGAs, ASICs, etc.).
-   [NVIDIA/nvidia-drivers](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers "NVIDIA/nvidia-drivers") --- The [[[x11-drivers/nvidia-drivers]](https://packages.gentoo.org/packages/x11-drivers/nvidia-drivers)[]] package contains the *proprietary* graphics driver for [NVIDIA](https://wiki.gentoo.org/wiki/NVIDIA "NVIDIA") graphic cards.
-   [AMDVLK](https://wiki.gentoo.org/wiki/AMDVLK "AMDVLK") --- an open-source Vulkan driver for AMD Radeon™ graphics adapters on Linux

## [References]

1.  [[[↑](#cite_ref-1)] [[https://docs.mesa3d.org/drivers/nvk.html](https://docs.mesa3d.org/drivers/nvk.html)]]