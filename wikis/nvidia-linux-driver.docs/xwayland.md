## Chapter 40. OpenGL, Vulkan and VDPAU on Xwayland

### Overview

Xwayland is an X11 server implemented as a Wayland client, allowing one to run X11 applications on a Wayland desktop in a relatively seamless fashion. The NVIDIA driver is able to facilitate accelerated 3D rendering for such applications, but there are some particular considerations compared to a typical X11 configuration which are outlined in this chapter.

Note that some NVIDIA driver features may not be available, see [Appendix L, *Wayland Known Issues*](wayland-issues.html "Appendix L. Wayland Known Issues") for details.

### Requirements

The following are necessary to enable accelerated rendering on Xwayland with the NVIDIA driver:

- DRM KMS must be enabled. See [Chapter 36, *Direct Rendering Manager Kernel Modesetting (DRM KMS)*](kms.html "Chapter 36. Direct Rendering Manager Kernel Modesetting (DRM KMS)") for details.

- The installed copy of Xwayland should be a build from the master branch of https://gitlab.freedesktop.org/xorg/xserver at least as recent as commit c468d34c. Note that if this requirement is not satisfied, the NVIDIA GPU can still be used for rendering, however it will fall back to a suboptimal path for presentation resulting in degraded performance.

- libxcb version 1.13 or later must be present.

- egl-wayland version 1.1.7 or later must be present (if installed separately from the the NVIDIA driver).

- If using the GNOME desktop environment, kms-modifiers must be enabled through gsettings. This can be done with the following command **`gsettings set org.gnome.mutter experimental-features [\"kms-modifiers\"]`**
