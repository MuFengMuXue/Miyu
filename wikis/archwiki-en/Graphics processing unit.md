# Graphics processing unit

A graphics processing unit (GPU) is the hardware in your computer that generates the video feed that appears on your display. They are present in two device types: Integrated Graphics Processors (IGP) and dedicated (or discrete) graphics, also known as graphics cards. The acronym is often abused to refer to the graphics card as a whole.

Their ease to perform parallel calculation has given birth to general-purpose computing on graphics processing units (GPGPU).

## Installation
The Linux kernel includes open-source video drivers and support for hardware accelerated framebuffers. However, userland support is required for OpenGL, Vulkan, 2D acceleration in Xorg and hardware video acceleration.

First, identify the graphics card (the Subsystem output shows the specific model):

 $ lspci -vnnd ::03xx

Then, installing its video driver is required. See the tables below for the three major vendors.

For 32-bit software, enable the multilib repository and install lib32- prefixed userspace drivers, such as , , , etc.

For X11, other Device Dependent X (DDX) drivers can be found in the  group or searching for xf86-video. In most cases, you do not need to install any DDX drivers; see Xorg#Drivers for details.

## AMD
AMD supports the open source driver. A proprietary driver was provided before but it is no longer packaged. See Hardware video acceleration#Comparison tables for details on VA-API support per GPU family.

{| class="wikitable"  style="text-align:center"
|-
! Documentation
! GPU family
! DRM driver
! OpenGL
! Vulkan
! DDX driver
! VA-API
|-
| AMDGPU
| GCN 3 and later (e.g. RDNA 1-4)
| rowspan="5" | Included in Linux
| rowspan="4" |
|
| 2
| rowspan="3" |
|-
| AMDGPU1 / ATI
| GCN 1&2
| colspan="2" | Depends on the chosen driver
|-
| rowspan="4" | ATI
| TeraScale 1-3
| rowspan="3" | None
| rowspan="3" | 2
|-
| R300 through R500
| rowspan="2" | None
|-
| R100 & R200
|
|-
| Rage 4 and older
| colspan="5" | Not available [https://www.x.org/wiki/RadeonFeature/|}

# Enabled by default since ≥6.19, can be manually chosen otherwise
# Using the modesetting driver is reported to work without issues

## Intel
Intel provides and supports open source drivers, except for PowerVR-based graphics (GMA 3600 series) which are not supported.

See Hardware video acceleration#Comparison tables for more details on VA-API support per GPU family, only the packages are listed below.

{| class="wikitable"  style="text-align:center"
|-
! Documentation
! GPU family
! DRM driver
! OpenGL
! Vulkan
! DDX driver
! VA-API
|-
| rowspan="6" | Intel graphics
| Gen 12.1 and later
| rowspan="6" | Included in Linux
| rowspan="5" |
| rowspan="3" | 1
| rowspan="6" | 2
|
|-
| Gen 8 through 11
| or legacy
|-
| Gen 7 & 7.5
| rowspan="2" |
|-
| Gen 5 & 6
| rowspan="3" | None
|-
| Gen 3 through 4.5
| rowspan="2" | None
|-
| Gen 2
|
|}

# Gen 7 and 7.5 have [https://gitlab.freedesktop.org/mesa/mesa/-/blob/main/src/intel/vulkan_hasvk/anv_device.c#L1600 incomplete support, Gen 8 is limited to Vulkan 1.3.
# The modesetting DDX driver is recommended for Gen 3 hardware and later. See Intel graphics#Installation for details.

## NVIDIA
NVIDIA does not support the fully open driver. They switched to a hybrid approach (with an open DRM driver and closed userland) in 2022.

See Hardware video acceleration#NVIDIA for details on which APIs are supported, and Hardware video acceleration#VDPAU drivers for details per GPU family.

{| class="wikitable"  style="text-align:center"
|-
! License
! Documentation
! GPU family
! DRM driver
! OpenGL
! Vulkan
! DDX driver
|-
| rowspan="2" | Open
| rowspan="2" | Nouveau1
| Kepler (NVE0/GKXXX) and newer
| rowspan="2" | Included in Linux
| rowspan="2" |
|
| rowspan="2" | 2
|-
| Fahrenheit (NV04/05) through Fermi (NVC0/GF1XX)
| None
|-
| Open DRM driver, proprietary userland
| rowspan="6" | NVIDIA1
| Turing (NV160/TUXXX) and newer
|
| colspan="3" |
|-
| rowspan="5" | Proprietary
| Maxwell (NV110/GMXXX) through  Ada Lovelace (NV190/ADXXX)
|
| colspan="3" |
|-
| Kepler (NVE0/GKXXX)
|
| colspan="3" |
|-
| Fermi (NVC0/GF1XX)
|
|
| rowspan="2" | None
|
|-
| Tesla (NV50/G80-90-GT2XX)
|
|
|
|-
| Curie (NV40/G70) and older
| colspan="6" | No longer packaged
|}

# For NVIDIA Optimus enabled laptop which uses an integrated video card combined with a dedicated GPU, see NVIDIA Optimus.
# The modesetting DDX driver is recommended for for NV50 (G80) and later. See Nouveau#Installation for details.

## Loading
Most driver kernel modules should load automatically on system boot.

If it does not happen, then:

* Make sure you do not have  or  as a kernel parameter, since they require KMS.
* Also, check that you have not disabled the driver by using any kernel module blacklisting.

## Monitoring
Monitoring your GPU is often used to check the temperature, core and VRAM utilization, and the P-states of your GPU.

## CLI
*
*
*
*

## GUI
*
*
*
*
*
*
