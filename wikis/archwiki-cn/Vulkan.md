**翻译状态：**

  * 本文（或部分内容）译自 [Vulkan](<https://wiki.archlinux.org/title/Vulkan> "arch:Vulkan")，最近一次同步于 2024-01-11，若英文版本有所[更改](<https://wiki.archlinux.org/title/Vulkan?diff=0&oldid=23144>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Vulkan_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

来自 [wikipedia:Vulkan (API)](<https://en.wikipedia.org/wiki/Vulkan_\(API\)> "wikipedia:Vulkan \(API\)"): 

    Vulkan是一种低开销、跨平台的3D图形和计算API。它于2016年首次发布，是 [OpenGL](<../zh-cn/OpenGL.html> "OpenGL") 的继任者。

在 [Khronos](<https://www.khronos.org/vulkan/>) 了解更多信息。 

##  安装

**提示：** 在[混合图形技术](<../zh-cn/%E6%B7%B7%E5%90%88%E5%9B%BE%E5%BD%A2%E6%8A%80%E6%9C%AF.html> "混合图形技术")（[NVIDIA Optimus](<../zh-cn/NVIDIA_Optimus.html> "NVIDIA Optimus")/AMD Dynamic Switchable Graphics）上: 

  * Vulkan 目前没有被 [Bumblebee](<../zh-cn/Bumblebee.html> "Bumblebee") [[1]](<https://github.com/Bumblebee-Project/Bumblebee/issues/769>) 官方支持，但可以工作在 [primus_vk](<https://archlinux.org/packages/?name=primus_vk>)包 或 [primus-vk-git](<https://aur.archlinux.org/packages/primus-vk-git/>)AUR上。
  * Radeon Vulkan 驱动程序现在支持 [PRIME](<../zh-cn/PRIME.html> "PRIME") [[2]](<https://www.phoronix.com/scan.php?page=news_item&px=RADV-PRIME-Lands>)。

要运行 Vulkan 程序，你需要[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Help:阅读") [vulkan-icd-loader](<https://archlinux.org/packages/?name=vulkan-icd-loader>)包 软件包（如果想运行32位程序，还需要安装 [lib32-vulkan-icd-loader](<https://archlinux.org/packages/?name=lib32-vulkan-icd-loader>)包）以及显卡的驱动程序。有几个软件包可以[提供](<../zh-cn/PKGBUILD.html#provides> "PKGBUILD") vulkan 驱动程序： 

  * [Intel](<../zh-cn/Intel_%E5%9B%BE%E5%BD%A2%E5%A4%84%E7%90%86%E5%99%A8.html> "Intel"): [vulkan-intel](<https://archlinux.org/packages/?name=vulkan-intel>)包 (或 [lib32-vulkan-intel](<https://archlinux.org/packages/?name=lib32-vulkan-intel>)包)
  * [NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA"): 有两种实现： 
    * [nvidia-utils](<https://archlinux.org/packages/?name=nvidia-utils>)包 (或 [lib32-nvidia-utils](<https://archlinux.org/packages/?name=lib32-nvidia-utils>)包) - NVIDIA 专有
    * [vulkan-nouveau](<https://archlinux.org/packages/?name=vulkan-nouveau>)包(或[lib32-vulkan-nouveau](<https://archlinux.org/packages/?name=lib32-vulkan-nouveau>)包) - NVK (Mesa 项目的一部分)

**提示：** 启用 NVK 还需要额外的系统配置，有关详细信息，请参阅 [Nouveau#使用 Mesa NVK Vulkan 驱动程序](<../zh-cn/Nouveau.html#%E4%BD%BF%E7%94%A8_Mesa_NVK_Vulkan_%E9%A9%B1%E5%8A%A8%E7%A8%8B%E5%BA%8F> "Nouveau")。

  * [AMD](<../zh-cn/AMDGPU.html> "AMDGPU"): 有两种实现，可以同时安装： 
    * [vulkan-radeon](<https://archlinux.org/packages/?name=vulkan-radeon>)包 (或 [lib32-vulkan-radeon](<https://archlinux.org/packages/?name=lib32-vulkan-radeon>)包) - RADV （Mesa 项目的一部分）
    * [vulkan-amdgpu-pro](<https://aur.archlinux.org/packages/vulkan-amdgpu-pro/>)AUR (或 [lib32-vulkan-amdgpu-pro](<https://aur.archlinux.org/packages/lib32-vulkan-amdgpu-pro/>)AUR) - AMDGPU PRO（由 AMD维护）
  * **Lavapipe** : [vulkan-swrast](<https://archlinux.org/packages/?name=vulkan-swrast>)包 (32位程序支持需安装[lib32-vulkan-swrast](<https://archlinux.org/packages/?name=lib32-vulkan-swrast>)包) 软件光栅化器，仅推荐用于没有 Vulkan 支持的设备
  * **SwiftShader** : [swiftshader-git](<https://aur.archlinux.org/packages/swiftshader-git/>)AUR

对于 Vulkan 程序开发，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Help:Reading") [vulkan-headers](<https://archlinux.org/packages/?name=vulkan-headers>)包，以及可选的 [vulkan-validation-layers](<https://archlinux.org/packages/?name=vulkan-validation-layers>)包 与 [vulkan-tools](<https://archlinux.org/packages/?name=vulkan-tools>)包 （你可以在这里找到 vulkaninfo 工具）。 

##  验证

要查看系统上当前安装了哪些 Vulkan 实现，请使用以下命令： 
    
    $ ls /usr/share/vulkan/icd.d/
    
为确保 Vulkan 在你的硬件上工作，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Help:Reading") [vulkan-tools](<https://archlinux.org/packages/?name=vulkan-tools>)包 并使用 `vulkaninfo` 命令调出你的系统信息。如果你得到了显卡信息，就说明 Vulkan 在正常工作。 
    
    $ vulkaninfo
    
访问 <https://linuxconfig.org/install-and-test-vulkan-on-linux> 以获取更多信息。 

##  切换

###  在设备之间切换

在具有多个 GPU 的系统上，您可能需要强制使用特定 GPU。 [vkdevicechooser](<https://aur.archlinux.org/packages/vkdevicechooser/>)AUR 提供了简单的方法来做到这一点。它将安装到系统的 Vulkan层 目录， `/usr/share/vulkan/implicit_layer.d/`. 

要运行强制使用特定设备的 Vulkan 应用程序，请使用以下环境变量启动它： 
    
    $ ENABLE_DEVICE_CHOOSER_LAYER=1 VULKAN_DEVICE_INDEX=_device_index_
    
需要用 `vulkaninfo` (没有启用图层) 所报告的设备id`GPU id`替换` _device_index_`

**注意：** 一些应用程序 (例如[Steam](<../zh-cn/Steam.html> "Steam")) 可能会改变设备索引` _device_index_`。

###  在 AMD 驱动程序之间切换

在 AMD 系统上，一次安装多个 Vulkan 驱动程序是有效的，可能需要在它们之间切换。 

####  通过 AMD Vulkan Prefixes 选择

[AMD Vulkan Prefixes](<https://gitlab.com/AndrewShark/amd-vulkan-prefixes>)是用于在两种Vulkan实现之间切换的脚本。[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Help:Reading") [amd-vulkan-prefixes](<https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/amd-vulkan-prefixes>)[CNRepo](<../zh-cn/Arch_Linux_%E4%B8%AD%E6%96%87%E7%A4%BE%E5%8C%BA%E4%BB%93%E5%BA%93.html> "Arch Linux 中文社区仓库") ，并在运行程序前添加前缀。可添加的前缀有 `vk_radv` 与 `vk_pro` 。例如，使用 AMDGPU PRO驱动程序: 
    
    $ vk_pro _command_
    
##  软件渲染

您可以安装名为lavapipe 的 Vulkan 光栅化软件，例如用于调试硬件问题：[vulkan-swrast](<https://archlinux.org/packages/?name=vulkan-swrast>)包 。(或者它的32位版本[lib32-vulkan-swrast](<https://archlinux.org/packages/?name=lib32-vulkan-swrast>)包). 
    
    $ LIBGL_ALWAYS_SOFTWARE=1 __GLX_VENDOR_LIBRARY_NAME=mesa VK_ICD_FILENAMES=/usr/share/vulkan/icd.d/lvp_icd.i686.json:/usr/share/vulkan/icd.d/lvp_icd.x86_64.json vulkaninfo
    
##  Vulkan 硬件数据库

[硬件数据库](<https://vulkan.gpuinfo.org/>)提供了用户报告的 GPU/驱动程序组。使用 [vulkan-caps-viewer-wayland](<https://aur.archlinux.org/packages/vulkan-caps-viewer-wayland/>)AUR 或 [vulkan-caps-viewer-x11](<https://aur.archlinux.org/packages/vulkan-caps-viewer-x11/>)AUR 可以提供自己的信息。 

##  疑难解答

###  NVIDIA - vulkan 无法工作并无法初始化

检查是否安装了其他 vulkan 驱动程序，这可能会阻止 NVIDIA 的 vulkan 驱动程序被检测到。 

或者，设置[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量") `VK_ICD_FILENAMES` 为 `/usr/share/vulkan/icd.d/nvidia_icd.json` 。 

如果你有双图形系统，比如 [NVIDIA Optimus](<../zh-cn/NVIDIA_Optimus.html> "NVIDIA Optimus") ，确保你的系统使用的是安装Vulkan驱动程序的显卡。 

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** optimus-manager 只是 [NVIDIA Optimus](<../zh-cn/NVIDIA_Optimus.html> "NVIDIA Optimus") 的几个实用程序之一。 (在 [Talk:Vulkan](<../zh-cn/Talk:Vulkan.html>) 中讨论)

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** Command in code block requires a [prompt symbol](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html#Command_line_text> "Help:Style").（在[Talk:Vulkan](<../zh-cn/Talk:Vulkan.html>)讨论）
    
    optimus-manager --status
    
    Optimus Manager (Client) version 1.4
    
    Current GPU mode : nvidia
    GPU mode requested for next login : no change
    GPU at startup : integrated
    Temporary config path: no
    
###  找不到显示 GPU 的设备。是否安装了 intel-mesa 驱动程序？

尝试将 intel_icd 与 primus_vk_wrapper 两者都配置进 VK_ICD_FILENAMES 列表 
    
    export VK_ICD_FILENAMES=/usr/share/vulkan/icd.d/intel_icd.x86_64.json:/usr/share/vulkan/icd.d/nv_vulkan_wrapper.json
    
###  在 vulkaninfo 之后出现 AMDGPU - ERROR_INITIALIZATION_FAILED

如果在 GCN1 或 GCN2 系列的 AMD 卡上运行 `vulkaninfo` 后，你会收到如下错误消息： 
    
    ERROR at /build/vulkan-tools/src/Vulkan-Tools-1.2.135/vulkaninfo/vulkaninfo.h:240:vkEnumerateInstanceExtensionProperties failed with ERROR_INITIALIZATION_FAILED

然后检查你是否已正确启用对此型号显卡的支持（[AMDGPU#开启 Southern Islands (SI) 和 Sea Islands (CIK) 支持](<../zh-cn/AMDGPU.html#%E5%BC%80%E5%90%AF_Southern_Islands_\(SI\)_%E5%92%8C_Sea_Islands_\(CIK\)_%E6%94%AF%E6%8C%81> "AMDGPU")）。 

可以使用 `lspci -k` 检查 gpu 驱动程序是否已正确加载，在运行该命令后检查内核驱动中关于 gpu 的信息，它应该是 `amdgpu`。 
    
    $ lspci -k
    
    ...
    01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Curacao PRO [Radeon R7 370 / R9 270/370 OEM]
    	Subsystem: Gigabyte Technology Co., Ltd Device 226c
    	Kernel driver in use: amdgpu
    	Kernel modules: radeon, amdgpu
    ...
    
关于这个问题的一些论坛主题：[[3]](<https://bbs.archlinux.org/viewtopic.php?id=254015>) [[4]](<https://bbs.archlinux.org/viewtopic.php?id=253843>)

###  在抛出 'dxvk::DxvkError' 的实例后调用终止

同时拥有 AMD 和 NVIDIA 驱动程序可能会导致问题。检查 
    
    pacman -Qs vulkan
    
    local/lib32-amdvlk 2022.Q2.3-1
        AMD's standalone Vulkan driver
    local/lib32-nvidia-utils 515.57-1
        NVIDIA drivers utilities (32-bit)
    local/lib32-vulkan-icd-loader 1.3.221-1
        Vulkan Installable Client Driver (ICD) Loader (32-bit)
    local/nvidia-utils 515.57-1
        NVIDIA drivers utilities
    local/vulkan-icd-loader 1.3.221-1
        Vulkan Installable Client Driver (ICD) Loader
    local/vulkan-tools 1.3.217-1 (vulkan-devel)
        Vulkan Utilities and Tools
    
并删除错误的驱动程序包。 

###  AMDGPU - Vulkan 应用程序启动过慢

如果您安装了[cuda](<https://archlinux.org/packages/?name=cuda>)包 软件包，您可能会发现 Vulkan 应用程序（例如 Chromium）启动缓慢。这是因为 [nvidia-utils](<https://archlinux.org/packages/?name=nvidia-utils>)包 提供了 Vulkan 驱动程序，而 Vulkan 会在 radeon 驱动程序之前尝试 nvidia 驱动程序。要解决此问题，请将[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量") `VK_DRIVER_FILES` 设置为 `/usr/share/vulkan/icd.d/radeon_icd.i686.json:/usr/share/vulkan/icd.d/radeon_icd.x86_64.json`。 
