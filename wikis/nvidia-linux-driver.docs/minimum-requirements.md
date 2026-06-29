## Chapter 2. Minimum Requirements

## Minimum Software Requirements

| Software Element | Supported versions | Check With... |
|----|----|----|
| Linux kernel | 4.15 and newer | **`cat /proc/version`** |
| X.Org xserver | 1.7, 1.8, 1.9, 1.10, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.17, 1.18, 1.19, 1.20, 21.1 | **`Xorg -version`** |
| Kernel modutils | 2.1.121 and newer | **`insmod --version`** |
| glibc |  2.11 | **`/lib/libc.so.6`** |
| libvdpau \* | 0.2 | **`pkg-config --modversion vdpau`** |
| libvulkan \*\* | 1.0.61 | **`pkg-config --modversion vulkan`** |

\* Required for hardware-accelerated video playback. See [Appendix G, *VDPAU Support*](vdpausupport.html "Appendix G. VDPAU Support") for more information.

\*\* Required for applications which use the Vulkan API.

If you need to build the NVIDIA kernel module:

| Software Element | Min Requirement | Check With...        |
|------------------|-----------------|----------------------|
| binutils         | 2.9.5           | **`size --version`** |
| GNU make         | 3.77            | **`make --version`** |
| gcc              | 2.91.66         | **`gcc --version`**  |

All official stable kernel releases from 4.15 and up are supported; pre-release versions, such as 4.19-rc1, are not supported. The Linux kernel can be downloaded from http://www.kernel.org or one of its mirrors.

binutils and gcc can be retrieved from http://www.gnu.org or one of its mirrors.

Sometimes very recent X server versions are not supported immediately following release, but we aim to support all new versions as soon as possible. Support is not added for new X server versions until after the video driver ABI is frozen, which usually happens at the release candidate stage. Prerelease versions that are not release candidates, such as "1.10.99.1", are not supported.

If you are setting up the X Window System for the first time, it is often easier to begin with one of the open source drivers that ships with X.Org (either "vga", "vesa", or "fbdev"). Once your system is operating properly with the open source driver, you may then switch to the NVIDIA driver.

These software packages may also be available through your Linux distributor.
