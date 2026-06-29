## Chapter 41. GBM and GBM-based Wayland Compositors

### Overview

GBM is a memory allocation API developed as a component of the Mesa project. Most Wayland compositors use the GBM API to initialize an EGLDisplay object directly on a GPU, and to allocate the EGLSurface representing the desktop. The NVIDIA driver includes a GBM backend enabling the use of such software on NVIDIA GPUs. A GBM EGL external platform library is also included to enable the use of GBM objects in EGL.

### Requirements

The following are necessary to enable use of the NVIDIA driver's GBM backend and its EGL and related Wayland client support:

- DRM KMS must be enabled. See [Chapter 36, *Direct Rendering Manager Kernel Modesetting (DRM KMS)*](kms.html "Chapter 36. Direct Rendering Manager Kernel Modesetting (DRM KMS)") for details.

- libgbm.so.1 from Mesa version 21.2 (https://gitlab.freedesktop.org/mesa/mesa).

- egl-wayland version 1.1.8 or later must be present (if installed separately from the the NVIDIA driver). To support applications that use the wl_drm Wayland protocol to select a GPU to render on, such as Xwayland, version 1.1.9 or later must be present.

### Xwayland and GBM

Xwayland uses the GLAMOR backend to accelerate X application rendering using EGL. While not required for basic functionality, GLAMOR acceleration is required for good performance when running accelerated Vulkan or OpenGL X11 applications. The GLAMOR integration code in Xwayland has paths to use either EGLStreams or GBM to allocate surfaces for use with accelerated rendering. To use the GBM path with the NVIDIA driver's GBM backend and GBM EGL external platform library, the installed copy of Xwayland should be a build from the master branch of https://gitlab.freedesktop.org/xorg/xserver at least as recent as commit 5daf42b4. Xwayland versions 21.1.3 and above satisfy this requirement.

See [Chapter 40, *OpenGL, Vulkan and VDPAU on Xwayland*](xwayland.html "Chapter 40. OpenGL, Vulkan and VDPAU on Xwayland") for more details on Xwayland support in the NVIDIA driver.

### Logging/Tracing

The NVIDIA GBM backend supports logging information about its behavior and the reasons for various function call failures to stderr. Such information may be useful for developers debugging applications or end users diagnosing system behavior issues. Set the environment variable '\_\_NV_GBM_TRACE_ENABLED' to a non-zero integer value to enable this logging.
