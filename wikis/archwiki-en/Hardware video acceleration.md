# Hardware video acceleration

Hardware video acceleration makes it possible for the video card to decode/encode video, thus offloading the CPU and saving power.

There are several ways to achieve this on Linux:

* Video Acceleration API (VA-API) is a specification and open source library to provide both hardware accelerated video encoding and decoding, developed by Intel.
* Video Decode and Presentation API for Unix (VDPAU) is an open source library and API to offload portions of the video decoding process and video post-processing to the GPU video-hardware, developed by NVIDIA.
* Advanced Media Framework SDK (AMF) is an open source framework which allows "Optimal" access to AMD GPUs for multimedia processing, developed by AMD.
* NVDEC/NVENC - NVIDIA's proprietary APIs for hardware video acceleration, used by NVIDIA GPUs from Fermi onwards.
* Vulkan Video is an extension of the Vulkan graphics API designed to support hardware-accelerated video encoding and decoding.

For comprehensive overview of driver and application support see #Comparison tables.

## Installation
## Intel
## VA-API
The Intel graphics open-source driver supports VA-API:

* HD Graphics series starting from Broadwell (2014) and newer (e.g. Intel Arc) are supported by .
* GMA 4500 (2008) up to Coffee Lake (2017) are supported by .
* Haswell Refresh to Skylake VP9 decoding and Broadwell to Skylake hybrid VP8 encoding is supported by .

Also see VAAPI supported hardware and features.

## Vulkan Video
ANV open-source vulkan driver provides Vulkan Video support via .

## Intel Video Processing Library (Intel VPL)
For Intel VPL, install the base library , and at least one of the following runtime implementations:

* : provides support for Tiger Lake and newer GPUs
*  (Discontinued): provides support for older Intel GPUs

## NVIDIA
The Nouveau open-source driver supports VA-API:

* GeForce 8 series and newer GPUs up until GeForce GTX 750 are supported by .
* Requires  firmware package, presently extracted from the NVIDIA binary driver.

The NVIDIA proprietary driver supports (via ):

* VDPAU on GeForce 8 series and newer GPUs;
* NVDEC on Fermi and newer GPUs * NVENC on Kepler and newer GPUs;
* Vulkan Video on Pascal and newer GPUs [https://developer.nvidia.com/vulkan/video/get-started.

## AMD/ATI
AMD and ATI open-source drivers support VA-API via :

* VA-API on Radeon HD 2000 and newer GPUs.

RADV open-source vulkan driver provides Vulkan Video support via .

* AMF on Fiji and newer GPUs supported by .

## Translation layers
*
*

## Verification
Your system may work perfectly out-of-the-box without needing any configuration. Therefore it is a good idea to start with this section to see that it is the case.

## Verifying VA-API
Verify the settings for VA-API by running , which is provided by :

 means that your card is capable to decode this format,  means that you can encode to this format.

In this example the  driver is used, as you can see in this line:

 vainfo: Driver version: Intel i965 driver for Intel(R) Skylake - 1.7.3

If the following error is displayed when running :

 libva info: va_openDriver() returns -1
 vaInitialize failed with error code -1 (unknown libva error),exit

You need to configure the correct driver, see #Configuring VA-API.

## Verifying VDPAU
Install  to verify if the VDPAU driver is loaded correctly and retrieve a full report of the configuration:

## Verifying Vulkan Video
Install  and use vulkaninfo to verify if the video processing extensions are available:

## Configuration
Although the video driver should automatically enable hardware video acceleration support for both VA-API and VDPAU, it may be needed to configure VA-API/VDPAU manually. Only continue to this section if you went through #Verification.

The default driver names, used if there is no other configuration present, are guessed by the system. However, they are often hacked together and may not work. The guessed value will be printed in the Xorg log file, which is  if rootless, or  if Xorg is running as root. To search the log file for the values of interest:

In this case  is the default for both VA-API and VDPAU.

This does not represent the configuration however. The values above will not change even if you override them.

## Configuring VA-API
You can override the driver for VA-API by using the  environment variable:

* Intel graphics:
** For  use .
** For  use .
* NVIDIA:
** For Nouveau use .
** For NVIDIA NVDEC use .
* AMD:
** For AMDGPU driver use .

{{Note|
* You can find the installed drivers in . They are used as {{ic|/usr/lib/dri/${LIBVA_DRIVER_NAME}_drv_video.so}}.
* Some drivers are installed several times under different names for compatibility reasons. You can see which by running .
*  can be used to overrule the VA-API drivers location.
* Since version 12.0.1 Mesa provides  instead of .
}}

## Configuring VDPAU
You can override the driver for VDPAU by using the  environment variable.

The correct driver name depends on your setup:

* For the open source AMD, Intel and Nouveau drivers you need to set it to .
* For NVIDIA's proprietary version set it to .

{{Note|
* You can find the installed drivers in . They are used as {{ic|/usr/lib/vdpau/libvdpau_${VDPAU_DRIVER}.so}}.
* Some drivers are installed several times under different names for compatibility reasons. You can see which by running .
* For hybrid setups (both NVIDIA and AMD), it may be necessary to set the  environment variable. For more information see PRIME.
}}

## Configuring Vulkan Video
* Intel graphics: Vulkan Video support in  can be enabled with the  environment variable. * AMD: Vulkan Video support in  is enabled by default for VCN 2, 3, and 4+ since Mesa 25. To force-enable support on older cards, set the  environment variable to .

## Configuring applications
Multimedia frameworks:

* FFmpeg#Hardware video acceleration
* GStreamer#Hardware video acceleration

Video players:

* Kodi#Hardware video acceleration
* MPlayer#Hardware video acceleration
* mpv#Hardware video acceleration
* VLC media player#Hardware video acceleration

Web browsers:

* Chromium#Hardware video acceleration
* Firefox#Hardware video acceleration
* GNOME/Web#Video

Multimedia recording/streaming:

* Open Broadcaster Software#Hardware video acceleration

## Troubleshooting
## Failed to open VDPAU backend
You need to set  variable to point to correct driver. See #Configuring VDPAU.

Starting from  25.3.0 the VDPAU support was [https://gitlab.freedesktop.org/mesa/mesa/-/merge_requests/36632 removed from the open source drivers (, , ,  and ). If you were using any of these drivers before, you will need to replace them with one of the #Translation layers or configure your applications to use VA-API directly.

## VAAPI init failed
An error along the lines of  is encountered. This can happen because of improper detection of Wayland. One solution is to unset  so that mpv, MPlayer, VLC, etc. do not assume it is X11. Another mpv-specific solution is to add the parameter .

This error can also occur if you installed the wrong VA-API driver for your hardware.

## Video decoding corruption or distortion with AMDGPU driver
When experiencing video decoding corruption or distortion with AMDGPU driver, set  as an environment variable. === vainfo fails when using iHD ===

If you encounter the following error:

Try installing the  instead of the non-legacy one, which works with . [https://aur.archlinux.org/packages/intel-compute-runtime-legacy-bin#comment-1024408

## Comparison tables
## VA-API drivers
{| class="wikitable" style="text-align:center;"
! Codec
!  !  [https://github.com/intel/media-driver/blob/master/README.md
!  [https://nouveau.freedesktop.org/wiki/VideoAcceleration/
!  (NVDEC adapter)
|-
! colspan=5 | Decoding
|-
! MPEG-2
|
|
|
| rowspan=10 | See #NVIDIA driver only
|-
! VC-1
|
| rowspan=2
|
|-
! H.264/MPEG-4 AVC
|
|
|-
! H.265/HEVC 8bit
|
|
|
|-
! H.265/HEVC 10bit
|
|
|
|-
! VP8
|
|
|
|-
! VP9 8bit
|
|
| rowspan=2
|-
! VP9 10bit & 12bit
|
|
|-
! AV1 8bit & 10bit
|
|
|
|-
! colspan=5 | Encoding
|-
! MPEG-2
|
|
|
| rowspan=8 2
|-
! H.264/MPEG-4 AVC
|
|
|
|-
! H.265/HEVC 8bit
|
|
|
|-
! H.265/HEVC 10bit
|
| rowspan=2
|
|-
! VP8
|
| rowspan=3
|-
! VP9 8bit
|
| rowspan=2
|-
! VP9 10bit & 12bit
| rowspan=2
|-
! AV1 8bit & 10bit
|
|
|}

# Hybrid VP8 encoder and VP9 decoder supported by .
# NVIDIA CUDA adapter codec support is in active development and susceptible to change === VDPAU drivers ===

{| class="wikitable" style="text-align:center;"
! Codec
! Colordepth
!
! (VA-API adapter)
|-
! colspan=4 | Decoding
|-
! MPEG-2
! 8bit
|
| rowspan=3
|-
! H.263/MPEG-4 Visual
! 8bit
|
|-
! VC-1
! 8bit
|
|-
! H.264/MPEG-4 AVC
! 8bit
|
| See #VA-API drivers
|-
! rowspan=2 | H.265/HEVC
! 8bit
|
| rowspan=6
|-
! 10bit
| 3
|-
! rowspan=2 | VP9
! 8bit
|
|-
! 10bit/12bit
| 3
|-
! rowspan=2 | AV1
! 8bit
| 4
|-
! 10bit
| 3
|}

# Except GeForce 8800 Ultra, 8800 GTX, 8800 GTS (320/640 MB).
# Except GeForce GTX 970 and GTX 980.
# NVIDIA implementation is limited to 8bit streams [https://forums.developer.nvidia.com/t/vdpau-expose-hevc-main10-support-where-available-on-die/43163 # Starting with driver version 510.[https://www.phoronix.com/scan.php?page=news_item&px=NVIDIA-510-Linux-Beta

## NVIDIA driver only
{| class="wikitable" style="text-align:center;"
! rowspan=2 | Codec
! colspan=2 |  https://developer.nvidia.com/nvidia-video-codec-sdk
|-
! NVDEC
! NVENC
|-
! MPEG-2
| rowspan=3
| rowspan=2
|-
! VC-1
|-
! H.264/MPEG-4 AVC
|
|-
! H.265/HEVC 8bit
| rowspan=2
|
|-
! H.265/HEVC 10bit
|
|-
! VP8
|
| rowspan=3
|-
! VP9 8bit
|
|-
! VP9 10bit & 12bit
|
|-
! AV1 8bit & 10bit
|
|
|}

# Except GM108 (not supported)
# Except GM108 and GP108 (not supported)
# Except A100 (not supported)

## Application support
{| class="wikitable"
! rowspan=2 | Application
! colspan=4 | Decoding
! colspan=3 | Encoding
! rowspan=2 | Documentation
|-
! VA-API
! VDPAU
! NVDEC
! Vulkan
! VA-API
! NVENC
! Vulkan
|-
! FFmpeg
|
|
|
|
|
|
|
| FFmpeg#Hardware video acceleration
|-
! GStreamer
|
|
|
|
|
|
|
| GStreamer#Hardware video acceleration
|-
! Kodi
|
|
|
|
|
|
|
| Kodi#Hardware video acceleration
|-
! mpv
|
|
|
|
|
|
|
| mpv#Hardware video acceleration
|-
! VLC media player
|
|
|
|
|
|
|
| VLC media player#Hardware video acceleration
|-
! MPlayer
|
|
|
|
|
|
|
| MPlayer#Hardware video acceleration
|-
! Chromium
|
|
|
|
|
|
|
| Chromium#Hardware video acceleration
|-
! Firefox
|
|
|
|
|
|
|
| Firefox#Hardware video acceleration
|-
! GNOME/Web
| colspan=4
|
|
|
| GNOME/Web#Video
|}
