**翻译状态：**

  * 本文（或部分内容）译自 [OpenGL](<https://wiki.archlinux.org/title/OpenGL> "arch:OpenGL")，最近一次同步于 2024-6-15，若英文版本有所[更改](<https://wiki.archlinux.org/title/OpenGL?diff=0&oldid=810058>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/OpenGL_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

摘自 [Wikipedia:OpenGL](<https://en.wikipedia.org/wiki/OpenGL> "wikipedia:OpenGL"): 

    OpenGL (Open Graphics Library) 是一个跨语言、跨平台的应用程序编程接口（API），用于渲染 2D 和 3D 矢量图形。

可在[Khronos](<https://www.khronos.org/opengl/>)上了解更多信息。 

OpenGL 的开发已于 2017 年停止，取而代之的是 [Vulkan](<../zh-cn/Vulkan.html> "Vulkan")，这是“下一代”API，可在较新的硬件上提供更高的性能。 

##  安装

要运行使用 OpenGL 的应用程序，您需要为您的硬件（GPU 或 CPU）[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")正确的驱动程序。 

**提示：**

  * 对于 AMD（和 ATI），建议使用开源驱动程序，除非您有充分的理由使用专有驱动程序。
  * 对于 NVIDIA，建议将专有驱动程序用在比 [Kepler (NVE0/GK _XXX_)](<https://nouveau.freedesktop.org/CodeNames.html#NVE0>) 系列更新的显卡上，并且总体上性能更好。

**注意：**

  * 英特尔的GenN硬件不是指CPU的一代，而是指[GPU的一代](<https://en.wikipedia.org/wiki/List_of_Intel_graphics_processing_units> "wikipedia:List of Intel graphics processing units")，这与CPU的一代不同。
  * 要查找 AMD（和 ATI）GPU 系列，请查阅[Wikipedia:List of AMD graphics processing units#Features overview](<https://en.wikipedia.org/wiki/List_of_AMD_graphics_processing_units#Features_overview> "wikipedia:List of AMD graphics processing units")
  * 要查找 NVIDIA GPU 的代号，请查看 [Nouveau 项目中的代码列表](<https://nouveau.freedesktop.org/CodeNames.html>)

[Mesa](<https://mesa3d.org/>) 是一个开源的 OpenGL 实现，它不断更新以支持最新的 OpenGL 规范。它有一系列用于 [Intel 图形处理器](<../zh-cn/Intel_%E5%9B%BE%E5%BD%A2%E5%A4%84%E7%90%86%E5%99%A8.html> "Intel 图形处理器")、[AMDGPU](<../zh-cn/AMDGPU.html> "AMDGPU")（以前称为 [ATI](<../zh-cn/ATI.html> "ATI")）和 [NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA") GPU 的开源驱动程序。Mesa 还提供软件[光栅器](<https://en.wikipedia.org/wiki/Rasterisation> "wikipedia:Rasterisation")，例如 llvmpipe。 

有两个 Mesa 软件包可选，每个软件包都有一组不同的驱动程序： 

  * [mesa](<https://archlinux.org/packages/?name=mesa>)包 mesa 是最新的 Mesa 软件包，其中包括用于较新硬件的大多数现代驱动程序： 
    * `r300` : 适用于AMD的Radeon R300, R400, 和 R500 GPU。
    * `r600` : 适用于 AMD 的 Radeon R600 GPU，最高支持Northern Islands架构。由 AMD 官方支持。
    * `radeonsi` : 适用于 AMD 的 Southern Island GPU 及更高版本。由 AMD 官方支持。
    * `nouveau` : [Nouveau](<../zh-cn/Nouveau.html> "Nouveau")是用于 NVIDIA GPU 的开源驱动程序。
    * `virtio_gpu` : 一个适用于 virtio 的虚拟 GPU 驱动程序，可与基于 [QEMU](<../zh-cn/QEMU.html> "QEMU") 的 VMM（如 [KVM](<../zh-cn/KVM.html> "KVM") 或 [Xen](<../zh-cn/Xen.html> "Xen")）一起使用。
    * `vmwgfx` : 适用于 [VMware](<../zh-cn/VMware.html> "VMware") 虚拟 GPU。
    * `i915` : 适用于英特尔的第 3 代硬件。
    * `crocus` : 适用于英特尔的第 4 代至第 7 代硬件。
    * `iris` : 适用于英特尔的第 8 代硬件及更高版本。由英特尔正式支持。
    * `zink` : 用于在 [Vulkan](<../zh-cn/Vulkan.html> "Vulkan") 上运行 OpenGL 的 Gallium 驱动程序。
    * `d3d12` : 用于仅支持 D3D12（即 WSL）的设备上的 OpenGL 3.3 支持。
    * `swrast`：旧的软件光栅化器。从 Mesa 22.0.0[[1]](<https://docs.mesa3d.org/relnotes/22.0.0.html>)起，该驱动程序已停用，但源代码中仍有该驱动程序（ArchLinux 截止到 24.1.1[[2]](<https://gitlab.archlinux.org/archlinux/packaging/packages/mesa/-/blob/main/PKGBUILD?ref_type=heads#L140>) 仍包含该驱动程序）。
    * `softpipe` : 软件光栅器和参考 Gallium 驱动程序。
    * `llvmpipe` : 软件光栅化器，它使用 LLVM 生成 x86 JIT 代码，并且是多线程的。

  * [mesa-amber](<https://archlinux.org/packages/?name=mesa-amber>)包 是传统的 Mesa 软件包，其中包括用于旧硬件的经典（非 Gallium3D）驱动程序： 
    * `i830` : 适用于英特尔的第 2 代硬件。与 `i965` 相同的二进制文件。
    * `i915` : 适用于英特尔的第 3 代硬件。与 `i965` . 相同的二进制文件。
    * `i965` : 适用于英特尔的第 4 代至第 11 代硬件。由英特尔正式支持。
    * `radeon` : 适用于 AMD 的 Radeon R100 GPU。与 `r200` 相同的二进制文件。
    * `r200` : 适用于 AMD 的 Radeon R200 GPU。
    * `nouveau_vieux` : 适用于 NVIDIA NV04(Fahrenheit) 至 NV20(Kelvin) GPU。
    * `swrast` : 旧版软件光栅器

**注意：** 使用 Mesa 时，系统会自动选择正确的驱动程序，因此安装软件包后无需配置。

  * [nvidia-utils](<https://archlinux.org/packages/?name=nvidia-utils>)包 是用于[NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA") GPU 的专有驱动程序，其中包括关于 OpenGL 的实现。

  * [amdgpu-pro-oglp](<https://aur.archlinux.org/packages/amdgpu-pro-oglp/>)AUR 是用于 AMD GPU 的[专有驱动程序](<../zh-cn/AMDGPU_PRO.html> "AMDGPU PRO")。

##  验证安装

要验证您的 OpenGL 安装，您可以使用 [mesa-utils](<https://archlinux.org/packages/?name=mesa-utils>)包 `eglinfo` ，它应该显示如下输出（当然，根据您的设置，其值不同）： 
    
    $ eglinfo -B
    
    Wayland platform:
    EGL API version: 1.4
    EGL vendor string: Mesa Project
    EGL version string: 1.4
    EGL client APIs: OpenGL OpenGL_ES
    OpenGL compatibility profile vendor: Mesa Project
    OpenGL compatibility profile renderer: i915 (chipset: Pineview M)
    OpenGL compatibility profile version: 2.1 Mesa 23.1.5
    OpenGL compatibility profile shading language version: 1.20
    OpenGL ES profile vendor: Mesa Project
    OpenGL ES profile renderer: i915 (chipset: Pineview M)
    OpenGL ES profile version: OpenGL ES 2.0 Mesa 23.1.5
    OpenGL ES profile shading language version: OpenGL ES GLSL ES 1.0.16
    
    X11 platform:
    EGL API version: 1.5
    EGL vendor string: Mesa Project
    EGL version string: 1.5
    EGL client APIs: OpenGL OpenGL_ES
    OpenGL core profile vendor: Mesa
    OpenGL core profile renderer: llvmpipe (LLVM 15.0.7, 128 bits)
    OpenGL core profile version: 4.5 (Core Profile) Mesa 23.1.5
    OpenGL core profile shading language version: 4.50
    OpenGL compatibility profile vendor: Mesa
    OpenGL compatibility profile renderer: llvmpipe (LLVM 15.0.7, 128 bits)
    OpenGL compatibility profile version: 4.5 (Compatibility Profile) Mesa 23.1.5
    OpenGL compatibility profile shading language version: 4.50
    OpenGL ES profile vendor: Mesa
    OpenGL ES profile renderer: llvmpipe (LLVM 15.0.7, 128 bits)
    OpenGL ES profile version: OpenGL ES 3.2 Mesa 23.1.5
    OpenGL ES profile shading language version: OpenGL ES GLSL ES 3.20

在 X11 平台上，也可以使用`glxinfo`。 

在同一个软件包中，您还可以使用 `eglgears_x11` 或 `glxgears` （在 X11 上）或 `eglgears_wayland` （在 Wayland 上）作为基本 OpenGL 测试。运行程序时，您应该会看到 3 个旋转齿轮。 

##  在驱动程序之间切换

有关[混合图形技术](<../zh-cn/%E6%B7%B7%E5%90%88%E5%9B%BE%E5%BD%A2%E6%8A%80%E6%9C%AF.html> "混合图形技术")，请参阅 [PRIME](<../zh-cn/PRIME.html> "PRIME")。 

**注意：** 根据这篇 [Reddit 帖子](<https://www.reddit.com/r/linuxhardware/comments/he9nhe/amd_and_nvidia_gpus_in_the_same_machine_it_works/>) ，您可以使用来自不同供应商的 2 个 GPU 同时使用 [PRIME](<../zh-cn/PRIME.html> "PRIME")，而不会出现任何问题。

### Mesa

您可以使用以下[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")覆盖用于应用程序的驱动程序： 
    
    MESA_LOADER_DRIVER_OVERRIDE=_driver_
    
默认情况下，Mesa 在 `/lib/dri/` 中搜索驱动程序。您可以使用以下命令查看已安装的驱动程序列表。 
    
    $ ls /lib/dri/
    
`_driver_ _dri.so` 中的 `_driver_` 是驱动程序的实际名称。如果 Mesa 无法找到指定的驱动程序，就会退回到 `llvmpipe`。 

您还可以通过设置以下[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")来使用 OpenGL 软件光栅器： 
    
    LIBGL_ALWAYS_SOFTWARE=true
    GALLIUM_DRIVER=_driver_
    
`_driver_` 可以是 `softpipe`, `llvmpipe` 或 `swr`。 

**提示：** 在大多数用例中， `llvmpipe` 与 `swr` 比 `softpipe` 更快。

##  Vulkan 上的 OpenGL (Zink)

来自 [Mesa 文档](<https://docs.mesa3d.org/drivers/zink.html>): 

    Zink 驱动程序是一个 Gallium 驱动程序，它能发出 Vulkan API 调用，而不是针对特定的 GPU 架构。它可用于在仅支持 Vulkan 的设备上获得完整的桌面 OpenGL 支持。

如果您在默认 OpenGL 驱动程序中遇到问题（RadeonSI、Iris 等中的错误），您可以尝试使用 Zink 驱动程序。 

根据[此 Phoronix 基准测试](<https://www.phoronix.com/review/radeon-zink-summer23>), 与 RadeonSI 相比，某些应用程序的平均 FPS 可能更低。 

要在 NVIDIA 驱动程序上使用 Zink，请使用以下命令或类似命令： 
    
    $ env __GLX_VENDOR_LIBRARY_NAME=mesa __EGL_VENDOR_LIBRARY_FILENAMES=/usr/share/glvnd/egl_vendor.d/50_mesa.json MESA_LOADER_DRIVER_OVERRIDE=zink GALLIUM_DRIVER=zink _application_
    
##  开发

**注意：** 本节适用于希望在项目中使用 OpenGL 的开发者。最终用户不需要本节中的任何内容。

在代码中使用 OpenGL 需要函数加载器，在 [Khronos](<https://www.khronos.org/opengl/wiki/OpenGL_Loading_Library>) 上阅读更多内容。 

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 将与 OpenGL 和 Arch repo 相关的软件包列表放在 Arch repo 中。 (在 [Talk:OpenGL](<../zh-cn/Talk:OpenGL.html>) 中讨论)

###  OpenGL 硬件数据库

[GPUInfo](<https://www.gpuinfo.org/>) 提供了用户报告的 GPU/驱动程序组合、支持的扩展、功能等。此信息可用于验证 OpenGL 和 Vulkan 下特定硬件的兼容性/合规性。 
