# AMDGPU PRO

This page describes close source drivers for AMD GPUs.

## Purpose of proprietary components
AMD releases their open source drivers via standard distribution channels. And they also periodically do releases of their Radeon Software for Linux suite, which includes both open and proprietary components. Open source components are not needed from there, and proprietary components are repacked from the latest Ubuntu LTS version. They are published in AUR in the amdgpu-pro-installer package base.

Comment by John Bridgman from AMD explaining why they still package close source drivers:

:These days our packaged drivers are mostly intended for:
:* customers using slower moving enterprise/LTS distros which do not automatically pick up the latest graphics drivers - we offer them both open source and proprietary/workstation options
:* customers using workstation apps who need the extra performance/certification from a workstation-oriented driver (although Marek has done a lot of great work over the last year to improve Mesa performance on workstation apps)
:* The third target audience is customers looking for ready-to-go OpenCL, either for use with the packaged open/closed drivers or with the upstream-based stack in a recent distro.

There are several proprietary components: OpenGL, OpenCL, Vulkan and AMF. Sometimes you may want to use these components due to specific features that open source components may lack.

AMDGPU PRO OpenGL is a proprietary, binary userland driver, which works on top of the open-source amdgpu kernel driver. From Radeon Software 18.50 vs Mesa 19 benchmarks article: When it comes to OpenGL games, the RadeonSI Gallium3D driver simply dominates the proprietary AMD OpenGL driver. Users of graphic cards other than Radeon Pro are advised to use the amdgpu graphics stack. Mostly used because of lacking compatibility layers that some software relies on. See gentoo wiki linked below.

AMDGPU PRO Vulkan - required dependency for AMF.

AMDGPU PRO OpenCL - used because Mesa OpenCL is not fully complete. Proprietary component only for Polaris GPUs. The onward GPUs use the open ROCm OpenCL.

AMDGPU AMF - used for GPU encoding/decoding.

## Installation
For proprietary OpenGL implementation, use the amdgpu-pro-installer package base. It contains all the following packages:

* : For proprietary OpenGL implementation
* : For proprietary OpenGL implementation 32 bit applications support
* : For proprietary Vulkan implementation
* : For proprietary Vulkan implementation 32 bit applications support
*  : For Advanced Media Framework implementation

For available OpenCL implementations see General-purpose computing on graphics processing units#OpenCL on AMD/ATI GPU.

## Usage
## Using proprietary OpenGL
Launch your application with progl, for example:

 $ progl glmark2

## How to ensure you are using AMDGPU-PRO driver
Run the following command:

 $ glxinfo | grep "OpenGL vendor string" | cut -f2 -d":" | xargs

If it returns , then you are running open source driver. If it returns  or , then you are running proprietary driver.

Alternatively, run glmark2. When using open driver, in OpenGL Information you will see:

    GL_VENDOR:     AMD
    GL_RENDERER:   Radeon RX 580 Series (POLARIS10, DRM 3.40.0, 5.10.7-arch1-1, LLVM 11.0.1)
    GL_VERSION:    4.6 (Compatibility Profile) Mesa 20.3.3

But when using closed driver, you will see:

    GL_VENDOR:     ATI Technologies Inc.
    GL_RENDERER:   Radeon RX 580 Series
    GL_VERSION:    4.6.14756 Compatibility Profile Context

## Using proprietary Vulkan
AMD Vulkan Prefixes is a script for switching between different Vulkan implementations. Install  and prepend your application with the prefix you want. The executables provided are  and . For example, to use the proprietary Vulkan implementation:

 $ vk_pro vkmark

## Using Advanced Multimedia Framework
See FFmpeg#AMD AMF.

## Troubleshooting
## Intel + AMD hybrid graphics
For users of a hybrid setup with both an Intel GPU and an AMD GPU, usage of the proprietary AMDGPU Pro Workstation Driver might not work as expected due to different MESA implementations.

The symptom is the following: when you boot your machine, you get a black screen, but with your mouse cursor is moving normally.

Unfortunately, Reverse PRIME is not a solution. See the developer response.

## Uninstalling packages
If you are in trouble, for example, you cannot login to your system due to black screen, you can revert all back by uninstalling all packages related to AMDGPU PRO.

Switch a virtual console (with e.g. ), login and run:

 # pacman -R $(pacman -Qg Radeon_Software_for_Linux | cut -f2 -d" ")

then reboot.

## Southern Islands (SI) or Sea Islands (CIK) GPUs
If using Southern Islands (SI) or Sea Islands (CIK) GPU, when running , you get:

 amdgpu_device_initialize: DRM version is 2.50.0 but this driver is only compatible with 3.x.x.

then ensure you are using the  driver, but not .

Check which driver is currently in use:

See AMDGPU#Enable Southern Islands (SI) and Sea Islands (CIK) support for more information.

## Firmware and AMD drivers
AMD drivers and firmware (especially recent firmware) can get out of sync and create issues or not work at all. You can search in the journal for :

 system VCN FW Encode interface version=1.9, expected version=1.8

Downgrading the firmware seems to fix the problem.
