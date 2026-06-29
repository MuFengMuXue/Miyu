## Chapter 5. Listing of Installed Components

The NVIDIA Accelerated Linux Graphics Driver consists of the following components (filenames in parentheses are the full names of the components after installation). Some paths may be different on different systems (e.g., X modules may be installed in /usr/X11R6/ rather than /usr/lib/xorg/).

- An X driver (`/usr/lib/xorg/modules/drivers/nvidia_drv.so`); this driver is needed by the X server to use your NVIDIA hardware.

- A GLX extension module for X (`/usr/lib/xorg/modules/extensions/libglxserver_nvidia.so.580.105.08`); this module is used by the X server to provide server-side GLX support.

- EGL and OpenGL ES libraries ( `/usr/lib/libEGL.so.1`,`/usr/lib/libGLESv1_CM.so.580.105.08`, and `/usr/lib/libGLESv2.so.580.105.08` ); these libraries provide the API entry points for all OpenGL ES and EGL function calls. They are loaded at run-time by applications.

- A Wayland EGL external platform library (`/usr/lib/libnvidia-egl-wayland.so.1`) and its corresponding configuration file (`/usr/share/egl/egl_external_platform.d/10_nvidia_wayland.json` ); this library provides client-side Wayland EGL application support using either dmabuf or EGLStream buffer sharing protocols, as well as server-side protocol extensions enabling the client-side EGLStream-based buffer sharing path. The EGLStream path can only be used in combination with an EGLStream-enabled Wayland compositor, e.g: https://gitlab.freedesktop.org/ekurzinger/weston.

  More information can be found along with the EGL external interface and Wayland library source code at https://github.com/NVIDIA/eglexternalplatform and https://github.com/NVIDIA/egl-wayland.

- A GBM EGL external platform library (`/usr/lib/libnvidia-egl-gbm.so.1`) and its corresponding configuration file (`/usr/share/egl/egl_external_platform.d/15_nvidia_gbm.json` ); this library provides GBM EGL application support.

  The source code for the GBM EGL external platform library can be found at https://github.com/NVIDIA/egl-gbm. See [Chapter 41, *GBM and GBM-based Wayland Compositors*](gbm.html "Chapter 41. GBM and GBM-based Wayland Compositors") for more details on GBM support in the NVIDIA driver.

- Vendor neutral graphics libraries provided by libglvnd (`/usr/lib/libOpenGL.so.0`,`/usr/lib/libGLX.so.0`, and `/usr/lib/libGLdispatch.so.0`); these libraries are currently used to provide full OpenGL dispatching support to NVIDIA's implementation of EGL.

  Source code for libglvnd is available at https://github.com/NVIDIA/libglvnd

- GLVND vendor implementation libraries for GLX (`/usr/lib/libGLX_nvidia.so.0`) and EGL (`/usr/lib/libEGL_nvidia.so.0`); these libraries provide NVIDIA implementations of OpenGL functionality which may be accessed using the GLVND client-facing libraries.`libGLX_nvidia.so.0` and `libEGL_nvidia.so.0` can be used as Vulkan ICDs. The Vulkan ICD configuration file included with the driver references `libGLX_nvidia.so.0`, however in environments where X11 client libraries are not available,`libEGL_nvidia.so.0` should be used.

  The Vulkan ICD configuration file is installed as `/etc/vulkan/icd.d/nvidia_icd.json`.

  An additional Vulkan layer configuration file is installed as `/etc/vulkan/implicit_layer.d/nvidia_layers.json`. These layers add functionality to the Vulkan loader.

- A GLVND GLX client ICD loader library (`/usr/lib/libGL.so.1`), This library provides API entry points for all GLX function calls, and is loaded at run-time by applications.

  This library is included as a convenience to support systems that do not already have an existing libglvnd installation. On systems with libglvnd libraries already installed, the existing libraries should be used instead.

- Various libraries that are used internally by other driver components. These include `/usr/lib/libnvidia-cfg.so.580.105.08`,`/usr/lib/libnvidia-eglcore.so.580.105.08`,`/usr/lib/libnvidia-glcore.so.580.105.08`,`/usr/lib/libnvidia-glsi.so.580.105.08`,`/usr/lib/libnvidia-glvkspirv.so.580.105.08`,`/usr/lib/libnvidia-gpucomp.so.580.105.08`,`/usr/lib/libnvidia-rtcore.so.580.105.08`, and `/usr/lib/libnvidia-allocator.so.580.105.08`.

- A VDPAU (Video Decode and Presentation API for Unix-like systems) library for the NVIDIA vendor implementation, (`/usr/lib/vdpau/libvdpau_nvidia.so.580.105.08`); see [Appendix G, *VDPAU Support*](vdpausupport.html "Appendix G. VDPAU Support") for details.

- The CUDA library (`/usr/lib/libcuda.so.580.105.08`) which provides runtime support for CUDA (high-performance computing on the GPU) applications.

- The CUDA Debugger library (`/usr/lib/libcudadebugger.so.580.105.08`) which provides support for debugging CUDA applications.

- Cryptography library wrappers, (`/usr/lib/libnvidia-pkcs11.so.580.105.08`) and (`/usr/lib/libnvidia-pkcs11.openssl3.so.580.105.08`), which dynamically link to the system's OpenSSL libraries and provide cryptography operations when the GPU and driver are operating in Confidential Compute mode. The driver attempts to use OpenSSL 3 first and if OpenSSL 3 is not available then it will attempt to use OpenSSL 1.1.

- The PTX JIT Compiler library (`/usr/lib/libnvidia-ptxjitcompiler.so.580.105.08`) is a JIT compiler which compiles PTX into GPU machine code and is used by the CUDA driver.

- The NVVM Compiler library (`/usr/lib/libnvidia-nvvm.so.4.0.0`) is loaded by the CUDA driver to do JIT link-time-optimization.

- Two OpenCL libraries (`/usr/lib/libOpenCL.so.1.0.0`,`/usr/lib/libnvidia-opencl.so.580.105.08`); the former is a vendor-independent Installable Client Driver (ICD) loader, and the latter is the NVIDIA Vendor ICD. A config file `/etc/OpenCL/vendors/nvidia.icd` is also installed, to advertise the NVIDIA Vendor ICD to the ICD Loader.

- The `nvidia-cuda-mps-control` and `nvidia-cuda-mps-server` applications, which allow MPI processes to run concurrently on a single GPU.

- A kernel module (``/lib/modules/`uname -r`/kernel/drivers/video/nvidia-modeset.ko``); this kernel module is responsible for programming the display engine of the GPU. User-mode NVIDIA driver components such as the NVIDIA X driver, OpenGL driver, and VDPAU driver communicate with nvidia-modeset.ko through the /dev/nvidia-modeset device file.

- A kernel module (``/lib/modules/`uname -r`/kernel/drivers/video/nvidia.ko``); this kernel module provides low-level access to your NVIDIA hardware for all of the above components. It is generally loaded into the kernel when the X server is started, and is used by the X driver and OpenGL. nvidia.ko consists of two pieces: the binary-only core, and a kernel interface that must be compiled specifically for your kernel version. Note that the Linux kernel does not have a consistent binary interface like the X server, so it is important that this kernel interface be matched with the version of the kernel that you are using. This can either be accomplished by compiling yourself, or using precompiled binaries provided for the kernels shipped with some of the more common Linux distributions.

- NVIDIA Unified Memory kernel module (``/lib/modules/`uname -r`/kernel/drivers/video/nvidia-uvm.ko``); this kernel module provides functionality for sharing memory between the CPU and GPU in CUDA programs. It is generally loaded into the kernel when a CUDA program is started, and is used by the CUDA driver on supported platforms.

- The nvidia-tls library (`/usr/lib/libnvidia-tls.so.580.105.08`); this file provides thread local storage support for the NVIDIA OpenGL libraries (libGLX_nvidia, libnvidia-glcore, and libglxserver_nvidia).

- The nvidia-ml library (`/usr/lib/libnvidia-ml.so.580.105.08`); The NVIDIA Management Library provides a monitoring and management API. See [Chapter 28, *The NVIDIA Management Library*](nvidia-ml.html "Chapter 28. The NVIDIA Management Library") for more information.

- The application nvidia-installer (`/usr/bin/nvidia-installer`) is NVIDIA's tool for installing and updating NVIDIA drivers. See [Chapter 4, *Installing the NVIDIA Driver*](installdriver.html "Chapter 4. Installing the NVIDIA Driver") for a more thorough description.

  Source code is available at https://download.nvidia.com/XFree86/nvidia-installer/.

- The application nvidia-modprobe (`/usr/bin/nvidia-modprobe`) is installed as setuid root and is used to load the NVIDIA kernel module, create the `/dev/nvidia*` device nodes and configure certain runtime settings in the kernel by processes (such as CUDA applications) that don't run with sufficient privileges to do those things themselves.

  Source code is available at https://download.nvidia.com/XFree86/nvidia-modprobe/.

- The application nvidia-xconfig (`/usr/bin/nvidia-xconfig`) is NVIDIA's tool for manipulating X server configuration files. See [Chapter 6, *Configuring X for the NVIDIA Driver*](editxconfig.html "Chapter 6. Configuring X for the NVIDIA Driver") for more information.

  Source code is available at https://download.nvidia.com/XFree86/nvidia-xconfig/.

- The application nvidia-settings (`/usr/bin/nvidia-settings`) is NVIDIA's tool for dynamic configuration while the X server is running. See [Chapter 25, *Using the nvidia-settings Utility*](nvidiasettings.html "Chapter 25. Using the nvidia-settings Utility") for more information.

- The libnvidia-gtk libraries (`/usr/lib/libnvidia-gtk2.so.580.105.08` and `/usr/lib/libnvidia-gtk3.so.580.105.08`); these libraries are required to provide the nvidia-settings user interface.

  Source code is available at https://download.nvidia.com/XFree86/nvidia-settings/.

- The application nvidia-smi (`/usr/bin/nvidia-smi`) is the NVIDIA System Management Interface for management and monitoring functionality. See [Chapter 27, *Using the nvidia-smi Utility*](nvidia-smi.html "Chapter 27. Using the nvidia-smi Utility") for more information.

- The application nvidia-debugdump (`/usr/bin/nvidia-debugdump`) is NVIDIA's tool for collecting internal GPU state. It is normally invoked by the nvidia-bug-report.sh (`/usr/bin/nvidia-bug-report.sh`) script. See [Chapter 29, *Using the nvidia-debugdump Utility*](nvidia-debugdump.html "Chapter 29. Using the nvidia-debugdump Utility") for more information.

- The daemon nvidia-persistenced (`/usr/bin/nvidia-persistenced`) is the NVIDIA Persistence Daemon for allowing the NVIDIA kernel module to maintain persistent state when no other NVIDIA driver components are running. See [Chapter 30, *Using the nvidia-persistenced Utility*](nvidia-persistenced.html "Chapter 30. Using the nvidia-persistenced Utility") for more information.

  Source code is available at https://download.nvidia.com/XFree86/nvidia-persistenced/.

- The NVCUVID library (`/usr/lib/libnvcuvid.so.580.105.08`); The NVIDIA CUDA Video Decoder (NVCUVID) library provides an interface to hardware video decoding capabilities on NVIDIA GPUs with CUDA.

- The NvEncodeAPI library (`/usr/lib/libnvidia-encode.so.580.105.08`); The NVENC Video Encoding library provides an interface to video encoder hardware on supported NVIDIA GPUs.

- The NVAPI library (`/usr/lib/libnvidia-api.so.1;`); NVAPI provides an interface for managing properties of GPUs. The NVAPI library provides runtime support for NVAPI applications.

- The NvFBC library (`/usr/lib/libnvidia-fbc.so.580.105.08`); The NVIDIA Framebuffer Capture library provides an interface to capture and optionally encode the framebuffer of an X server screen.

- An X driver configuration file (`/usr/share/X11/xorg.conf.d/nvidia-drm-outputclass.conf`); If the X server is sufficiently new, this file will be installed to configure the X server to load the `nvidia_drv.so` driver automatically if it is started after the NVIDIA DRM kernel module (`nvidia-drm.ko`) is loaded. This feature is supported in X.Org xserver 1.16 and higher when running on Linux kernel 3.13 or higher with CONFIG_DRM enabled.

- Predefined application profile keys and documentation for those keys can be found in the following files in the directory `/usr/share/nvidia/`:`nvidia-application-profiles-580.105.08-rc`,`nvidia-application-profiles-580.105.08-key-documentation`.

  See [Appendix J, *Application Profiles*](profiles.html "Appendix J. Application Profiles") for more information.

- The OptiX library (`/usr/lib/libnvoptix.so.1`); This library implements the OptiX ray tracing engine. It is loaded by the `liboptix.so.*` library bundled with applications that use the OptiX API.

  OptiX also includes a data file `/usr/share/nvidia/nvoptix.bin`.

- The NVIDIA Optical Flow library (`/usr/lib/libnvidia-opticalflow.so.580.105.08`); The NVIDIA Optical Flow library can be used for hardware-accelerated computation of optical flow vectors and stereo disparity values on Turing and later NVIDIA GPUs. This is useful for some forms of computer vision and image analysis. The Optical Flow library depends on the NVCUVID library, which in turn depends on the CUDA library.

- NGX (`/usr/lib/libnvidia-ngx.so.580.105.08`); and the NVIDIA NGX Updater (`/usr/bin/nvidia-ngx-updater`); NGX is a collection of software which provides AI features to applications. Developers interested in using NGX in their applications should visit the following resources:

  - https://developer.nvidia.com/rtx/ngx

  - https://developer.nvidia.com/dlss

  NGX comes with nvidia-ngx-updater, a binary which updates NGX features without requiring a full application update. By default this functionality is disabled on Linux and needs to be enabled via a configuration file; see [Chapter 38, *NGX*](ngx.html "Chapter 38. NGX") for details.

- A kernel module (``/lib/modules/`uname -r`/kernel/drivers/video/nvidia-peermem.ko``); this kernel module allows Mellanox HCAs access to NVIDIA GPU memory read/write buffers without needing to copy data to host memory. See [Chapter 43, *GPUDirect RDMA Peer Memory Client*](nvidia-peermem.html "Chapter 43. GPUDirect RDMA Peer Memory Client") for more information.

- NGX for Proton and Wine (`/usr/lib/nvidia/wine/nvngx.dll`); (`/usr/lib/nvidia/wine/_nvngx.dll`);

  NGX for Proton and Wine is a Microsoft Windows dynamic-link library used by Microsoft Windows applications which support NVIDIA DLSS.

  In addition to driver-side support, changes to third-party software are required in order to support DLSS within Proton and Wine.

- NvPresent (`/usr/lib/libnvidia-present.so.580.105.08`), containing a Vulkan layer implementing NVIDIA Smooth Motion. See [Chapter 39, *NVIDIA Smooth Motion*](nvpresent.html "Chapter 39. NVIDIA Smooth Motion") for details.

- Firmware (`/lib/firmware/nvidia/580.105.08/gsp_*.bin`) which offloads tasks from the CPU to the GPU. See [Chapter 44, *GSP Firmware*](gsp.html "Chapter 44. GSP Firmware") for more information.

- VulkanSC ICD (`/usr/lib/libnvidia-vksc-core.so.1`), which provides NVIDIA's implementation of VulkanSC. More information about VulkanSC can be found at https://www.khronos.org/vulkansc/ .

  Pipeline Cache Compiler (`/usr/bin/nvidia-pcc`), which enables offline shader compilation for VulkanSC.

  The VulkanSC ICD configuration file is installed as `/etc/vulkansc/icd.d/nvidia_icd.json`.

  VulkanSC support is only provided in x86_64 driver packages. Note that the VulkanSC ICD distributed in this package is intended for development purposes only, and is NOT safety certified.

- A JSON file (`/usr/share/nvidia/files.d/sandboxutils-filelist.json`), which lists all the driver files (library, firmware, binary, configuration, ...) used by container runtime environments such as nvidia-container-toolkit and enroot.

Problems will arise if applications use the wrong version of a library. This can be the case if there are either old libGL libraries or stale symlinks left lying around. If you think there may be something awry in your installation, check that the following files are in place (these are all the files of the NVIDIA Accelerated Linux Graphics Driver, as well as their symlinks):

``` screen
    /usr/lib/xorg/modules/drivers/nvidia_drv.so

    /usr/lib/xorg/modules/extensions/libglxserver_nvidia.so.580.105.08
    /usr/lib/xorg/modules/extensions/libglxserver_nvidia.so -> libglxserver_nvidia.so.580.105.08

    /usr/lib/libGL.so.1.0.0;
    /usr/lib/libGL.so.1 -> libGL.so.1.0.0;
    /usr/lib/libGL.so -> libGL.so.1

    (libGL.so.1.0.0 is the name of the libglvnd client-side GLX ICD loader
    library included with the NVIDIA Linux driver. A compatible ICD loader
    provided by your distribution may have a slightly different filename.)

    /usr/lib/libnvidia-glcore.so.580.105.08

    /usr/lib/libcuda.so.580.105.08
    /usr/lib/libcuda.so -> libcuda.so.580.105.08

    /lib/modules/`uname -r`/video/nvidia.{o,ko}, or
    /lib/modules/`uname -r`/kernel/drivers/video/nvidia.{o,ko}
```

If there are other libraries whose "soname" conflicts with that of the NVIDIA libraries, ldconfig may create the wrong symlinks. It is recommended that you manually remove or rename conflicting libraries (be sure to rename clashing libraries to something that ldconfig will not look at -- we have found that prepending "XXX" to a library name generally does the trick), rerun 'ldconfig', and check that the correct symlinks were made. An example of a library that often creates conflicts is "/usr/lib/mesa/libGL.so\*".

If the libraries appear to be correct, then verify that the application is using the correct libraries. For example, to check that the application /usr/bin/glxgears is using the libglvnd GLX libraries, run:

``` screen
    % ldd /usr/bin/glxgears
    linux-vdso.so.1 (0x00007ffc8a5d4000)
    libGL.so.1 => /usr/lib/x86_64-linux-gnu/libGL.so.1 (0x00007f6593896000)
    libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f65934f8000)
    libX11.so.6 => /usr/lib/x86_64-linux-gnu/libX11.so.6 (0x00007f65931c0000)
    libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f6592dcf000)
    libGLX.so.0 => /usr/lib/x86_64-linux-gnu/libGLX.so.0 (0x00007f6592b9e000)
    libGLdispatch.so.0 => /usr/lib/x86_64-linux-gnu/libGLdispatch.so.0 (0x00007f65928e8000)
    libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f65926c9000)
    /lib64/ld-linux-x86-64.so.2 (0x00007f6593d28000)
    libxcb.so.1 => /usr/lib/x86_64-linux-gnu/libxcb.so.1 (0x00007f65924a1000)
    libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f659229d000)
    libXau.so.6 => /usr/lib/x86_64-linux-gnu/libXau.so.6 (0x00007f6592099000)
    libXdmcp.so.6 => /usr/lib/x86_64-linux-gnu/libXdmcp.so.6 (0x00007f6591e93000)
    libbsd.so.0 => /lib/x86_64-linux-gnu/libbsd.so.0 (0x00007f6591c7e000)
    librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007f6591a76000)
```

In the example above, the list of libraries reported by **ldd** includes `libGLX.so.0` and `libGLdispatch.so.0`. If the GLX client library is something other than the GLVND `libGL.so.1`, then you will need to either remove the library that is getting in the way or adjust your dynamic loader search path using the `LD_LIBRARY_PATH` environment variable. You may want to consult the man pages for **ldconfig** and **ldd**.
