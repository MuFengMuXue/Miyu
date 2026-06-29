**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Framebuffer "wikipedia:Framebuffer")

The **framebuffer\'**s original function is as a video RAM cache to allow more flexibility to (older) video cards. Many newer cards come with framebuffers on board, which are often already compatible with many operating systems. Enabling framebuffer support in the Linux kernel will often cause graphical artifacts or black screen displays. For most newer cards, this option should not be selected when using the LiveDVD.

## Contents

-   [[1] [Checking the console driver]](#Checking_the_console_driver)
-   [[2] [The kernel selection]](#The_kernel_selection)
    -   [[2.1] [DRM framebuffer drivers]](#DRM_framebuffer_drivers)
    -   [[2.2] [Early framebuffer drivers]](#Early_framebuffer_drivers)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Checking the console driver]

On the boot media:

`root `[`#`]`dmesg | grep fb0`

    [   11.388220] fbcon: amdgpudrmfb (fb0) is primary device
    [   11.796455] amdgpu 0000:0a:00.0: [drm] fb0: amdgpudrmfb frame buffer device

In the previous output, fb0 is the primary display. The console will appear here. The frame buffer device tells that is indeed a framebuffer console. fb0: amdgpudrmfb tells that the driver in use is the kernel\'s AMDGPU DRM FB framebuffer driver.

That is included with the kernel amdgpu driver. No other framebuffer drivers are strictly required but see early console drivers below.

Other video cards will show something similar.

** Warning**\
Users intent on installing nvidia-drivers see the [Early framebuffer drivers](#Early_framebuffer_drivers) section below.

nVidia users may find that the above grep returns nouveaufb. It is not possible to use the kernel nouveau driver and nvidia-drivers concurrently. Only the early framebuffer drivers may be selected.

## [The kernel selection]

Most of the the kernel framebuffer options are for use with hardware over 20 years old. These options almost always interfere with modern Direct Render Manager (DRM) provided framebuffers as both will attempt to configure the hardware and neither will work.

### [DRM framebuffer drivers]

For everyone except nvidia-drivers users.

[KERNEL]

    Device Drivers --->
     Graphics support --->
      <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support) Search for <code>CONFIG_DRM</code> to find this item. --->
        [*]   Enable legacy fbdev support for your modesetting driver Search for <code>CONFIG_DRM_FBDEV_EMULATION</code> to find this item.
        (100)   Overallocation of the fbdev buffer Search for <code>CONFIG_DRM_FBDEV_OVERALLOC</code> to find this item.

Note that the fbdev option is invisible unless the following option is also selected further down in the Graphic support menu:

[KERNEL]

    Device Drivers --->
     Graphics support --->
       Frame buffer Devices --->
         <*>    Support for frame buffer devices Search for <code>CONFIG_FB</code> to find this item. --->

Back on the Graphics support menu, choose the DRM driver for the system. Xorg will use this later.

For example, to use AMDGPU:

[KERNEL]

    Device Drivers --->
     Graphics support --->
      <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support) Search for <code>CONFIG_DRM</code> to find this item. --->
        <M> AMD GPU Search for <code>CONFIG_DRM_AMDGPU</code> to find this item.
          [ ]   Enable amdgpu support for SI parts
          [ ]   Enable amdgpu support for CIK parts
          [*]   Always enable userptr write support Search for <code>CONFIG_DRM_AMDGPU_USERPTR</code> to find this item.
          [ ]   Force the compiler to throw an error instead of a warning when compiling
                ACP (Audio CoProcessor) Configuration  --->
                Display Engine Configuration  --->
          [ ]   HSA kernel driver for AMD GPU devices
          < > Nouveau (NVIDIA) cards
          < > Intel 8xx/9xx/G3x/G4x/HD Graphics
          < > Virtual GEM provider
          < > Virtual KMS (EXPERIMENTAL)│
          < > DRM driver for VMware Virtual GPU
          < > Intel GMA500/600/3600/3650 KMS Framebuffer

There are very few uses for the Virtual drivers.

** Important**\
Building these drivers as modules (\<M\>) avoids the requirement to discover and include the required firmware in the kernel.

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

will install the required firmware.

### [Early framebuffer drivers]

Early because the DRM Framebuffer drivers typically require firmware to be loaded which implies that they are often built as loadable modules. They, therefore, start sometime later than built in drivers. This mean that the early console messages are lost as the console is blank until the DRM driver is initialized.

Only four Early Framebuffer Drivers are safe for modern hardware:

[KERNEL]

    Device Drivers --->
     Graphics support --->
       Frame buffer Devices --->
         <*>    Support for frame buffer devices Search for <code>CONFIG_FB</code> to find this item. --->
           <*>   VGA 16-color graphics support Search for <code>CONFIG_GB_VGA16</code> to find this item.
           [*]   VESA VGA graphics support Search for <code>CONFIG_FB_VESA</code> to find this item.
           [*]   EFI-based Framebuffer Support Search for <code>CONFIG_FB_EFI</code> to find this item.

It is safe to choose them all as none of then try to control the hardware. The kernel will pick and choose at boot time.

** Important**\
All the others must be disabled.

To later use a compiled framebuffer different than the default, like one supporting Tux for every online CPU, pass the [command-line parameter](https://wiki.gentoo.org/wiki/Kernel/Command-line_parameters#Available_options "Kernel/Command-line parameters") when booting.

[![](/images/thumb/1/10/IMG_20250727_094354.jpg/300px-IMG_20250727_094354.jpg)](https://wiki.gentoo.org/wiki/File:IMG_20250727_094354.jpg)

[](https://wiki.gentoo.org/wiki/File:IMG_20250727_094354.jpg "Enlarge")

Tux for every online CPU

## [See also]

-   [Intel](https://wiki.gentoo.org/wiki/Intel "Intel") --- the open source graphics driver for Intel GMA on-board graphics cards and Intel iGPU and Intel Arc dedicated graphics cards, starting with the Intel 810.
-   [Nouveau](https://wiki.gentoo.org/wiki/Nouveau "Nouveau") --- an open source driver for [NVIDIA](https://wiki.gentoo.org/wiki/NVIDIA "NVIDIA") graphic cards.
-   [Radeon](https://wiki.gentoo.org/wiki/Radeon "Radeon") --- a family of *open source* graphics drivers for *older* AMD/ATI Radeon graphics cards.
-   [Xorg/Guide](https://wiki.gentoo.org/wiki/Xorg/Guide#Verify_legacy_framebuffer_drivers_have_been_disabled "Xorg/Guide") --- Verify legacy framebuffer drivers have been disabled

## [External resources]

-   [https://forums.gentoo.org/viewtopic-p-8111658.html#8111658](https://forums.gentoo.org/viewtopic-p-8111658.html#8111658)