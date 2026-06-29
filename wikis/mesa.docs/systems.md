# Platforms and Drivers

Mesa is primarily developed and used on Linux systems. But there's also
support for Windows, other flavors of Unix and other systems such as
Haiku. We're actively developing and maintaining several hardware and
software drivers.

The primary API is OpenGL but there's also support for OpenGL ES, Vulkan,
EGL, OpenCL and VA-API.

Hardware drivers include:

-  Intel GMA, HD Graphics, Iris. See [Intel's
   Website](https://www.intel.com/content/www/us/en/developer/topic-technology/open/overview.html)
-  AMD Radeon series. See
   [RadeonFeature](https://www.x.org/wiki/RadeonFeature)
-  NVIDIA GPUs (Maxwell and later). See NVK
-  Qualcomm Adreno 2xx-8xx. See Freedreno
-  Broadcom VideoCore 4 and 5. See VC4 and
   V3D
-  ARM Mali Utgard. See Lima
-  ARM Mali Midgard, Bifrost. See Panfrost
-  Vivante GCxxx. See [Etnaviv
   Wiki](https://github.com/etnaviv/etna_viv)
-  Older NVIDIA GPUs (GeForce 5 / FX and later). See [Nouveau
   Wiki](https://nouveau.freedesktop.org)
-  NVIDIA Tegra (K1 and later).

Layered drivers include:

-  D3D12 - driver providing OpenGL on top of
   Microsoft's Direct3D 12 API.
-  KosmicKrisp - driver providing Vulkan
   on top of Apple's Metal API.
-  SVGA3D - driver for VMware virtual GPU
-  VirGL - project for accelerated graphics for
   QEMU guests
-  Zink - driver providing OpenGL on top of
   Khronos' Vulkan API.

Software drivers include:

-  LLVMpipe - uses LLVM for JIT code generation
   and is multi-threaded
-  Softpipe - a reference Gallium driver with a shader interpreter.

Additional driver information:

-  [DRI hardware drivers](https://dri.freedesktop.org/) for the X
   Window System
-  Xlib driver for the X Window System
   and Unix-like operating systems

## Deprecated Systems and Drivers

In the past there were other drivers for older GPUs and operating
systems. These have been removed from the Mesa source tree and
distribution. If anyone's interested though, the code can be found in
the Git repo. The list includes:

-  3dfx Glide
-  3DLABS Gamma
-  ATI Mach 64
-  ATI Rage 128
-  ATI Radeon 7000 - 9250
-  DEC OpenVMS
-  Intel i810
-  Intel i830 - i865
-  Linux Framebuffer
-  Matrox
-  MS-DOS
-  NVIDIA Riva TNT - GeForce 4
-  S3 Savage
-  Silicon Integrated Systems
-  swrast
-  VIA Unichrome
-  VDPAU
