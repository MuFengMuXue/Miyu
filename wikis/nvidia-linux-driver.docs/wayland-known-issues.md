## Appendix L. Wayland Known Issues

### Overview

There are several areas in which the NVIDIA driver lacks feature parity between X11 and Wayland. These may be due to limitations of the driver itself, the Wayland protocol, or the specific Wayland compositor in use. Over time this list is expected to shorten as missing functionality is implemented both in the driver and in upstream components, but the following captures the situation as of the release of this driver version. Note that this assumes a compositor with reasonably complete support for graphics-related Wayland protocol extensions.

### NVIDIA Driver Limitations

- Wayland compositors may not be designed to handle the case where two DRM drivers instantiate independent device nodes capable of driving the same display. When the nvidia-drm driver does not remove conflicting framebuffers and instantiate its own DRM fbdev support, simpledrm will remain present for driving the initial framebuffer console if initially loaded. In this situation, both simpledrm and nvidia-drm have DRI device nodes driving the same display. This can lead to issues such as a black screen, corruption, or flickering. A workaround for this is to set the fbdev=1 module parameter for the nvidia-drm kernel module.

- The nvidia-drm module does support the DEGAMMA_LUT, CTM, and GAMMA_LUT CRTC properties. However the COLOR_ENCODING and COLOR_RANGE plane properties are unsupported. This may impact some advanced compositor features related to color correction.

- The nvidia-settings configuration tool has limited functionality on Wayland.

- Front-buffer rendering in GLX does not work with Xwayland.

- Explicit Sync refers to using DRM Syncobj timeline synchronization points to explicitly signal ownership transfers of shared buffers to and from the compositor. Explicit Sync support requires a kernel that contains the following two commits, which fix bugs preventing Explicit Sync from working correctly. These are present in 6.8.x or newer kernels.

  - "drm/syncobj: fix DRM_SYNCOBJ_WAIT_FLAGS_WAIT_AVAILABLE" with commit hash 101c9f637efa1655f55876644d4439e552267527.

  - "drm/syncobj: handle NULL fence in syncobj_eventfd_entry_func" with commit hash 2aa6f5b0fd052e363bb9d4b547189f0bf6b3d6d3.

### Wayland Protocol or Compositor Limitations

- The following workstation features are not supported by any Wayland compositors or the Wayland protocol. They will also likely require new EGL extensions or other means to expose the related hardware functionality. Features followed by an asterisk (\*) are supported with VK_KHR_display.

  - SLI Mosaic ([Chapter 31, *Configuring SLI Mosaic*](sli.html "Chapter 31. Configuring SLI Mosaic"))

  - Frame Lock and Genlock ([Chapter 32, *Configuring Frame Lock and Genlock*](framelock.html "Chapter 32. Configuring Frame Lock and Genlock"))\*

  - Swap Groups\*

  - Advanced display pipeline features including warp and blend, pixel shift, and emulated YUV420.

  - Stereo rendering\*

- There is no established public API through which Wayland compositors can power off video memory via RTD3 ([Chapter 22, *PCI-Express Runtime D3 (RTD3) Power Management*](dynamicpowermanagement.html "Chapter 22. PCI-Express Runtime D3 (RTD3) Power Management")).

- Display multiplexers (muxes) are typically used in laptops with both integrated and discrete GPUs to provide a direct connection between the discrete GPU and the built-in display (internal mux) or an external display (external mux). On X11, the display mux can be automatically switched when a full-screen application is running on the discrete GPU, enabling enhanced display features and improved performance, but no Wayland compositors currently support this functionality.

- Indirect GLX is not supported by Xwayland.

- Hardware overlays cannot be used by GLX applications with Xwayland.
