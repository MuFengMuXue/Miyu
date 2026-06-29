**Resources**

[[]][Home](https://www.amd.com/en/support/kb/release-notes/rn-radpro-lin-16-40)

[[]][Wikipedia](https://en.wikipedia.org/wiki/AMDGPU "wikipedia:AMDGPU")

**AMDGPU-PRO** is the next generation *closed source* graphics component that operates on top of the open source [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU") drivers for newer AMD/ATI Radeon graphics cards.

Users whose main use for their graphics card is gaming and other general home-use graphical hardware acceleration should use the open source AMDGPU drivers instead, since the performance of the open source drivers can be as much 100% more compared to AMDGPU-PRO.^[\[1\]](#cite_note-1)^ However, the PRO driver provides a few features that Mesa still lacks, namely OpenGL compatibility profiles, OpenCL 2.0, and a fully conformant Vulkan implementation. Also, most of the games for which Mesa outperforms the closed-source driver run in Wine, rather than natively. Thus, the closed-source driver is mostly useful to users who want to play games (such as Civilization V) or use applications (such as UCSF Chimera) that rely on compatibility profiles, or want to run anything that uses Vulkan with advanced shaders, or want to fully exploit OpenCL.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Use AMDGPU-PRO Vulkan drivers for specific games]](#Use_AMDGPU-PRO_Vulkan_drivers_for_specific_games)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)
-   [[5] [References]](#References)

## [Installation]

### [Emerge]

AMDGPU-PRO is currently available as:

-   [[[media-video/amdgpu-pro-amf]](https://packages.gentoo.org/packages/media-video/amdgpu-pro-amf)[]]
-   [[[dev-libs/amdgpu-pro-opencl]](https://packages.gentoo.org/packages/dev-libs/amdgpu-pro-opencl)[]]
-   [[[media-libs/amdgpu-pro-vulkan]](https://packages.gentoo.org/packages/media-libs/amdgpu-pro-vulkan)[]]

## [Usage]

### [Use AMDGPU-PRO Vulkan drivers for specific games]

** Warning**\
If the drivers were manually installed, please take care to remove the old files at e.g. [/opt/amdgpu-pro] before proceeding.

** Note**\
It may be possible to set `VK_ICD_FILENAMES` via [the env.d directory](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/EnvVar#The_env.d_directory "Handbook:AMD64/Working/EnvVar"). It is likely better to set the variable per-application though as it may not always outperform Mesa, as mentioned above!

For some games, it might be useful to use AMDGPU-PRO Vulkan drivers instead of Mesa\'s RADV drivers. AMDGPU-PRO\'s Vulkan implementation gives better Ray Tracing performance than Mesa\'s RADV driver.^[\[2\]](#cite_note-2)^ You can manually install the Vulkan drivers to use on a per-game basis:

First, install the Vulkan drivers:

`root `[`#`]`emerge --ask media-libs/amdgpu-pro-vulkan`

Then start Steam (or the Vulkan based game) with the following command (following is for 64-bit):

`user `[`$`]`VK_ICD_FILENAMES=/usr/share/vulkan/icd.d/amd_pro_icd64.json /usr/bin/steam`

If it is a 32-bit game or application, instead run:

`user `[`$`]`VK_ICD_FILENAMES=/usr/share/vulkan/icd.d/amd_pro_icd32.json /usr/bin/foo`

For this to work, you need Vulkan working in general and have [[[dev-util/vulkan-headers]](https://packages.gentoo.org/packages/dev-util/vulkan-headers)[]] and [[[media-libs/vulkan-loader]](https://packages.gentoo.org/packages/media-libs/vulkan-loader)[]] installed.

## [See also]

-   [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU") --- the open source graphics drivers for AMD Radeon and other GPUs.
-   [AMDVLK](https://wiki.gentoo.org/wiki/AMDVLK "AMDVLK") --- an open-source Vulkan driver for AMD Radeon™ graphics adapters on Linux

## [External resources]

-   [A list of AMDGPU-PRO articles at Phoronix.com](https://www.phoronix.com/scan.php?page=search&q=AMDGPU-PRO)

## [References]

1.  [[[↑](#cite_ref-1)] [[Phoronix - Radeon RX 550: AMDGPU-PRO vs. DRM-Next + Mesa 17.2-dev](https://www.phoronix.com/scan.php?page=article&item=rx550-open-hybrid&num=2) - "*Similar to what we\'ve been seeing on other AMD hardware, the pure open-source driver stack can be much faster than AMDGPU-PRO.*"]]
2.  [[[↑](#cite_ref-2)] [[Phoronix - Radeon RX 7900 XTX: AMDGPU-PRO vs. Mesa 24.2-devel](https://www.phoronix.com/review/amdvlk-radv-rt/2) - "*So simply put, for those wondering the AMDVLK driver is still leading over the Mesa RADV driver when it comes to Vulkan ray-tracing\...*"]]