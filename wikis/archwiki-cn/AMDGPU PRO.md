相关文章

  * [AMDGPU](<../zh-cn/AMDGPU.html> "AMDGPU")
  * [Vulkan](<../zh-cn/Vulkan.html> "Vulkan")
  * [GPGPU](<../zh-cn/GPGPU.html> "GPGPU")
  * [DaVinci Resolve](<../zh-cn/DaVinci_Resolve.html> "DaVinci Resolve")

本页介绍了 AMD GPU 的闭源驱动程序。 

**提示：** 大多数用户不需要这些专有驱动程序。

##  专有组件的用途

AMD 通过标准分发渠道发布其开源驱动程序。他们还定期发布 _Radeon Software for Linux_ 套件，其中包括开放组件和专有组件。那里不需要开源组件，专有组件是从最新的 ubuntu lts 版本重新打包的。它们发布在 AUR 的 [amdgpu-pro-installer](<https://aur.archlinux.org/pkgbase/amdgpu-pro-installer>) 包组中。 

[该评论](<https://www.phoronix.com/forums/forum/phoronix/latest-phoronix-articles/1316628-radeon-software-for-linux-22-10-driver-being-prepared-for-release?p=1316713#post1316713>)解释了为什么 AMD 仍然打包闭源驱动程序: 
    
    如今，我们打包的驱动程序主要用于：
    * 软件迁移速度较慢的企业/LTS 发行版的客户不会自动获取最新的图形驱动程序 - 我们为他们提供开源和专有/工作站选项
    * 使用工作站应用程序的客户需要来自面向工作站的驱动程序的额外性能/认证（尽管 Marek 在去年做了很多出色的工作来提高工作站应用程序上的 Mesa 性能）
    * 第三个目标受众是寻找现成 OpenCL 的客户，它们可以与打包的开放/封闭驱动程序一起使用，也可以与最近发行版中基于上游的堆栈一起使用。
    
有几个专有组件：OpenGL、OpenCL、Vulkan 和 AMF。有时，由于开源的组件可能缺少特定功能，可能需要使用到这些（专有）组件。 

AMDGPU PRO OpenGL 是一种专有的用户态二进制驱动程序，它基于开源 amdgpu 内核驱动程序运行。从 [Radeon Software 18.50 与 Mesa 19 基准测试](<https://www.phoronix.com/vr.php?view=27266>)该文章可以看出：在 OpenGL 游戏方面，RadeonSI Gallium3D 驱动程序能全方位替代专有的 AMD OpenGL 驱动程序。[AMD 建议](<https://www.amd.com/en/support/kb/release-notes/amdgpu-installation>)购买 Radeon Pro 以外的非专业显卡用户使用 amdgpu 图形堆栈。使用该组件主要是因为对应的开源组件缺少某些软件所依赖的兼容层。请参阅下面的 gentoo wiki 链接。 

AMDGPU PRO Vulkan - 目前唯一具有光线追踪的实现（但是被用户报告为故障状态）。它也是 AMF 的必需依赖项。 

AMDGPU PRO OpenCL - 使用该组件主要是因为 Mesa OpenCL 不完全完整。仅适用于 Polaris GPU 的专有组件。未来的 GPU 会使用开放的 ROCm OpenCL。 

AMDGPU AMF - 用于 GPU 硬件编解码。 

##  安装

对于专有的 OpenGL 实现，安装 [amdgpu-pro-oglp](<https://aur.archlinux.org/packages/amdgpu-pro-oglp/>)AUR 和可选的 [lib32-amdgpu-pro-oglp](<https://aur.archlinux.org/packages/lib32-amdgpu-pro-oglp/>)AUR 以支持 32 位应用程序。 

有关可用的 OpenCL 实现，请参阅 [GPGPU#AMD/ATI](<../zh-cn/GPGPU.html#AMD/ATI> "GPGPU")。 

对于专有的 Vulkan 实现，安装 [vulkan-amdgpu-pro](<https://aur.archlinux.org/packages/vulkan-amdgpu-pro/>)AUR 和可选的 [lib32-vulkan-amdgpu-pro](<https://aur.archlinux.org/packages/lib32-vulkan-amdgpu-pro/>)AUR 以获得 32 位应用程序支持。 

对于高级媒体框架（AMF）实现，安装 [amf-amdgpu-pro](<https://aur.archlinux.org/packages/amf-amdgpu-pro/>)AUR。 

要让 OBS 使用它，请使用 [obs-studio-amf](<https://aur.archlinux.org/packages/obs-studio-amf/>)AUR。 

**注意：** 自 2022 年 10 月起，由于 AMD 驱动程序的一个错误，您需要 [amdgpu-pro-installer-fix](<https://aur.archlinux.org/pkgbase/amdgpu-pro-installer-fix>) 包(或者 <https://github.com/HannesMann/archlinux-amdgpu-pro> \- 如果-fix包不起作用) 和 20220815.8413c63-1 版本的 [linux-firmware](<https://archlinux.org/packages/?name=linux-firmware>)包 来让 H264 和 HEVC 工作。

##  用法

###  使用专有的 OpenGL

使用 progl 命令运行应用程序，例如： 
    
    $ progl glmark2
    
####  如何确保程序使用的是 AMDGPU-PRO 驱动程序

执行下面的命令： 
    
    $ glxinfo | grep "OpenGL vendor string" | cut -f2 -d":" | xargs
    
如果返回的是 `AMD`, 那就表明运行的是开源驱动程序。如果返回 `Advanced Micro Devices, Inc.`，则表明运行了专有驱动程序。 

或者, 也可以运行 [glmark2](<../zh-cn/%E5%9F%BA%E5%87%86%E6%B5%8B%E8%AF%95.html#glmark2> "Benchmarking")。 当用的是开源驱动，在 OpenGL 信息里面就可以看到： 
    
       GL_VENDOR:     AMD
       GL_RENDERER:   Radeon RX 580 Series (POLARIS10, DRM 3.40.0, 5.10.7-arch1-1, LLVM 11.0.1)
       GL_VERSION:    4.6 (Compatibility Profile) Mesa 20.3.3
    
如果用的是闭源驱动，看到的就应该是： 
    
       GL_VENDOR:     ATI Technologies Inc.
       GL_RENDERER:   Radeon RX 580 Series
       GL_VERSION:    4.6.14756 Compatibility Profile Context
    
###  使用专有的 Vulkan

用 `vk_pro` 命令（脚本）启动应用程序，例如： 
    
    $ vk_pro vkmark
    
更过信息可以参考 [Vulkan#通过_AMD_Vulkan_Prefixes_选择](<../zh-cn/Vulkan.html#%E9%80%9A%E8%BF%87_AMD_Vulkan_Prefixes_%E9%80%89%E6%8B%A9> "Vulkan")。 

###  使用 Advanced Multimedia Framework

参考 [FFmpeg#AMD AMF](<../zh-cn/FFmpeg.html#AMD_AMF> "FFmpeg")

##  故障排除

###  Intel + AMD 混合显示

对于使用 Intel GPU 和 AMD GPU 混合配置的用户，由于不同的 MESA 实现，专有 AMDGPU Pro 工作站驱动程序的使用可能无法按预期工作。 

症状如下：开机时黑屏，但鼠标光标移动正常。 

不幸的是，[反向 PRIME](<../zh-cn/PRIME.html#Reverse_PRIME> "PRIME") 不能作为解决方案。请参考[开发者回复](<https://gitlab.freedesktop.org/drm/amd/-/issues/985#note_359417>)。 

###  卸载软件包

如果遇到问题，例如由于黑屏而无法登录系统，可以通过卸载与 AMDGPU PRO 相关的所有软件包来恢复所有状态。 

切换[虚拟控制台](</wzh/index.php?title=%E8%99%9A%E6%8B%9F%E6%8E%A7%E5%88%B6%E5%8F%B0&action=edit&redlink=1> "虚拟控制台（页面不存在）")（例如 `Ctrl+Alt+F2`），登录并运行： 
    
    # pacman -R $(pacman -Qg Radeon_Software_for_Linux | cut -f2 -d" "
    
再重启系统。 

###  Southern Islands (SI) 或者 Sea Islands (CIK) 显卡

如果使用 Southern Islands (SI) 或 Sea Islands (CIK) 显卡，遇到在运行 `clinfo` 时打印： 
    
    amdgpu_device_initialize: DRM version is 2.50.0 but this driver is only compatible with 3.x.x.
    
要保证使用的是 amdgpu 驱动程序，而不是 radeon。 

用下面的命令检查当前正在使用的驱动程序： 
    
    lspci -k
    
    03:00.0 Display controller: Advanced Micro Devices, Inc. [AMD/ATI] Opal XT [Radeon R7 M265/M365X/M465]
            Subsystem: Acer Incorporated [ALI] Aspire V5 Radeon R7 M265
            **Kernel driver in use: radeon**
            Kernel modules: radeon, amdgpu
    
更多信息请参考 [AMDGPU#开启_Southern_Islands_(SI)_和_Sea_Islands_(CIK)_支持](<../zh-cn/AMDGPU.html#%E5%BC%80%E5%90%AF_Southern_Islands_\(SI\)_%E5%92%8C_Sea_Islands_\(CIK\)_%E6%94%AF%E6%8C%81> "AMDGPU")。 

##  参考链接

  * [Gentoo:AMDGPU-PRO](<https://wiki.gentoo.org/wiki/AMDGPU-PRO> "gentoo:AMDGPU-PRO")
