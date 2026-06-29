# OpenGL

From Wikipedia:OpenGL:
: OpenGL (Open Graphics Library) is a cross-language, cross-platform application programming interface (API) for rendering 2D and 3D vector graphics.

Learn more at Khronos.

Development of OpenGL ceased in 2017 in favour of Vulkan, the "next generation" API which offers higher performance on newer hardware.

## Installation
To run applications that use OpenGL, you will need to install the correct driver(s) for your hardware (either GPUs or CPUs).

Mesa is an open-source OpenGL implementation, continually updated to support the latest OpenGL specification. It has a collection of open-source drivers for Intel graphics, AMD (formerly ATI) and NVIDIA GPUs. Mesa also provides software rasterizers, such as llvmpipe.

There are two Mesa packages, each with a distinct set of drivers:

*  is the up-to-date Mesa package which includes most of the modern drivers for newer hardware:
**  : for AMD's Radeon R300, R400, and R500 GPUs.
**  : for AMD's Radeon R600 GPUs up to Northern Islands. Officially supported by AMD.
**  : for AMD's Southern Island GPUs and later. Officially supported by AMD.
**  : Nouveau is the open-source driver for NVIDIA GPUs.
**  : a virtual GPU driver for virtio, can be used with QEMU based VMMs (like KVM or Xen).
**  : for VMware virtual GPUs.
**  : for Intel's Gen 3 hardware.
**  : for Intel's Gen 4 to Gen 7 hardware.
**  : for Intel's Gen 8 hardware and later. Officially supported by Intel.
**  : a Gallium driver used to run OpenGL on top of Vulkan.
**  : for OpenGL 3.3 support on devices that only support D3D12 (i.e. WSL).
**  : a software rasterizer and a reference Gallium driver.
**  : a software rasterizer which uses LLVM for x86 JIT code generation and is multi-threaded.

*  is the legacy Mesa package which includes the classic (non-Gallium3D) drivers for older hardware:
**  : for Intel's Gen 2 hardware. Same binary as .
**  : for Intel's Gen 3 hardware. Same binary as .
**  : for Intel's Gen 4 to Gen 11 hardware. Officially supported by Intel.
**  : for AMD's Radeon R100 GPUs. Same binary as .
**  : for AMD's Radeon R200 GPUs.
**  : for NVIDIA NV04 (Fahrenheit) to NV20 (Kelvin) GPUs.
**  : a legacy software rasterizer.

:

*  is the proprietary driver for NVIDIA GPUs, which includes an OpenGL implementation.

## Verification
To verify your OpenGL installation, you can use  , which should display output like this (with different values depending on your setup, of course):

On X11 platform,  works as well.

From the same package, you can also use  or  (on X11) or  (on Wayland) as a basic OpenGL test. You should see 3 rotating gears when running the program.

## Switching between drivers
For Hybrid graphics, see PRIME.

## Mesa
You can override the driver used for an application with the following environment variable:

 MESA_LOADER_DRIVER_OVERRIDE=driver

By default, Mesa searches for drivers in . You can view the list of installed drivers with

 $ ls /lib/dri/

 in  is the actual name of the driver. If Mesa failed to find the specified driver, it will fall back to .

You can also use an OpenGL software rasterizer by setting the following environment variables:

 LIBGL_ALWAYS_SOFTWARE=true
 GALLIUM_DRIVER=driver

 can be either , , or .

## OpenGL over Vulkan (Zink)
From the Mesa documentation:

: The Zink driver is a Gallium driver that emits Vulkan API calls instead of targeting a specific GPU architecture. This can be used to get full desktop OpenGL support on devices that only support Vulkan.

If you are experiencing issues in your default OpenGL drivers (a bug in RadeonSI, Iris, etc.), you could try using the Zink driver.

According to this Phoronix benchmark, the average FPS might be lower in some applications compared to RadeonSI.

Note that Zink no longer works out-of-the-box on X systems that use the AMD or Intel DDX drivers ( and , respectively). Upstream developers recommend use of the generic  DDX driver. Alternatively, to bypass this issue, you can use the following environment variables:

 $ LIBGL_KOPPER_DRI2=1 MESA_LOADER_DRIVER_OVERRIDE=zink

To use Zink on the proprietary NVIDIA driver, use this command or similar:

 $ env __GLX_VENDOR_LIBRARY_NAME=mesa __EGL_VENDOR_LIBRARY_FILENAMES=/usr/share/glvnd/egl_vendor.d/50_mesa.json MESA_LOADER_DRIVER_OVERRIDE=zink GALLIUM_DRIVER=zink LIBGL_KOPPER_DRI2=1 application

## Troubleshooting
## Lenovo GPU Graphics Mesa Error
Mesa was using CPU (llvmpipe) for rendering, which crashed some GUI software. Fixed this by going to BIOS settings and choosing Dynamic Graphics over Discrete Graphics (If using another computer, choose the option that lets you switch between GPUs than disabling the integrated GPU). This will happen if main GPU driver is not installed but you expect the integrated one to work. [https://download.lenovo.com/pccbbs/pubs/legion_s7_16_7/html/en-us/explore_GPUMode.html
