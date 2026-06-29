**翻译状态：**

  * 本文（或部分内容）译自 [PRIME](<https://wiki.archlinux.org/title/PRIME> "arch:PRIME")，最近一次同步于 2025-05-29，若英文版本有所[更改](<https://wiki.archlinux.org/title/PRIME?diff=0&oldid=829614>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/PRIME_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [NVIDIA Optimus](<../zh-cn/NVIDIA_Optimus.html> "NVIDIA Optimus")
  * [外接显卡](<../zh-cn/%E5%A4%96%E6%8E%A5%E6%98%BE%E5%8D%A1.html> "外接显卡")

PRIME 是一种用于管理最新一些台式机和笔记本电脑上的[混合图形](<../zh-cn/%E6%B7%B7%E5%90%88%E5%9B%BE%E5%BD%A2%E6%8A%80%E6%9C%AF.html> "混合图形技术")的技术（[NVIDIA 的 Optimus](<../zh-cn/NVIDIA_Optimus.html> "NVIDIA Optimus")，Radeon 的 AMD 动态可切换图形）。PRIME GPU 分载（offloading）和反向 PRIME（reverse PRIME）是在 Linux 内核中支持无复用混合显示的尝试。 

    本文出现的一些不常用缩写的解释：
    iGPU - integrated GPU，集成显卡
    dGPU - discrete/dedicated GPU，独立/专用显卡

##  PRIME GPU 分载

用户希望在更强大的显卡上渲染应用程序，并将结果发送到连接显示器的显卡。 

命令 `xrandr --setprovideroffloadsink provider sink` 可用于让渲染分载提供程序（offload provider）将其输出发送到接收端（sink）提供程序（也就是连接了显示器的提供程序）。提供程序和接收端标识符可以是数字（0x7d、0x56）或区分大小写的名称（Intel、radeon）。 

**注意：** 当使用来自官方存储库的大多数默认 Xorg DDX（`xf86-video-*` 或内置[内核级显示模式设置](<../zh-cn/%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE.html> "内核级显示模式设置")）驱动程序时，不再需要此设置，因为它们默认启用 DRI3，因此会自动地这样设置。不过，再次显式设置它们一次也不会有什么害处。

样例: 
    
    $ xrandr --setprovideroffloadsink radeon Intel
    
命令中的提供程序也可以用序号代替名字： 
    
    $ xrandr --setprovideroffloadsink 1 0
    
###  对于开源程序 - PRIME

要将独立显卡用于最需要它的应用程序（例如游戏、3D 建模器...），请在程序的启动命令前面加上环境变量 `DRI_PRIME=1`： 
    
    $ DRI_PRIME=1 glxinfo | grep "OpenGL renderer"
    
    OpenGL renderer string: Gallium 0.4 on AMD TURKS

**注意：** 除了数值外，您还可以指定 PCI 设备名称。格式类似于 `/sys/bus/pci/devices/`，但前缀为 `pci-` 并将分号和点替换为下划线，例如 `DRI_PRIME=pci-0000_01_00_0`。

其他应用程序仍将使用功耗较低的集成显卡。一旦 X 服务器重新启动，这些设置就会丢失，可能需要制作一个脚本并在桌面环境启动时自动运行（或者将其放在 `/etc/X11/xinit/xinitrc.d/ ` 目录下面）。不过，这样可能会缩短电池寿命并增加热量。 

更多信息可以参考 [Gentoo:AMDGPU#Identifying which graphics card is in use](<https://wiki.gentoo.org/wiki/AMDGPU#Identifying_which_graphics_card_is_in_use> "gentoo:AMDGPU")。 

为了让 `DRI_PRIME` 在 Vulkan 应用程序上工作，需要安装 [vulkan-mesa-layers](<https://archlinux.org/packages/?name=vulkan-mesa-layers>)包，以及用于 32 位应用程序的 [lib32-vulkan-mesa-layers](<https://archlinux.org/packages/?name=lib32-vulkan-mesa-layers>)包。 

###  PRIME 渲染分载

NVIDIA 驱动程序从[版本 435.17](<https://download.nvidia.com/XFree86/Linux-x86_64/435.17/README/primerenderoffload.html>) 开始支持这个方案。iGPU 驱动程序 [xf86-video-amdgpu](<https://archlinux.org/packages/?name=xf86-video-amdgpu>)包（450.57）和 [xf86-video-intel](<https://archlinux.org/packages/?name=xf86-video-intel>)包（455.38）官方支持[内核级显示模式设置](<../zh-cn/%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE.html> "内核级显示模式设置")（modesetting）。 

要在 NVIDIA 显卡上运行程序，您可以使用 [nvidia-prime](<https://archlinux.org/packages/?name=nvidia-prime>)包 软件包提供的 `prime-run` 脚本： 
    
    $ prime-run glxinfo | grep "OpenGL renderer"
    $ prime-run vulkaninfo
    
####  PCI-Express Runtime D3 (RTD3) 电源管理

#####  开源驱动程序

在 GPU 不和 PRIME 分载或反向 PRIME 一起使用的时候，内核 PCI 电源管理就会关闭该 GPU。 

[内核级显示模式设置](<../zh-cn/%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE.html> "内核级显示模式设置")、[xf86-video-amdgpu](<https://archlinux.org/packages/?name=xf86-video-amdgpu>)包、[xf86-video-intel](<https://archlinux.org/packages/?name=xf86-video-intel>)包、[xf86-video-nouveau](<https://archlinux.org/packages/?name=xf86-video-nouveau>)包 驱动程序都支持此功能。 

以下命令可用于检查每个 GPU 当前的[电源状态](<https://docs.kernel.org/power/pci.html#native-pci-power-management>)： 
    
     $ cat /sys/class/drm/card*/device/power_state
    
##### NVIDIA

**注意：**

  * 安培（Ampere）架构的显卡通常不需要配置，因为默认情况下已经启用。对于某些安培架构显卡的用户，可能需要 udev 规则。
  * 一些使用混合显卡的用户报告称，在升级到较新的 NVIDIA 驱动程序（似乎 >525）后，他们的独立 NVIDIA 安培 GPU 无法保持在 D3Cold 电源状态 [[1]](<https://forums.developer.nvidia.com/t/nvidia-gpu-fails-to-power-off-prime-razer-blade-14-2022/250023>)。
  * 一些使用前安培显卡的用户报告称，在较新的驱动程序上 D3 支持已损坏，可以通过禁用 GSP 固件来解决，使用 `NVreg_EnableGpuFirmware=0`[[2]](<https://bbs.archlinux.org/viewtopic.php?pid=2182638>)。

对于在 Intel Coffee Lake 或更高版本 CPU 以及某些 Ryzen CPU（如 5800H）平台上运行的图灵（Turning）架构显卡，可以[在不使用的时候完全关闭 GPU](<https://us.download.nvidia.com/XFree86/Linux-x86_64/550.54.14/README/dynamicpowermanagement.html>)。 

**注意：** 如果您计划使用挂起或休眠，请参见 [NVIDIA/提示和技巧#保留挂起后的显存](<../zh-cn/NVIDIA/%E6%8F%90%E7%A4%BA%E5%92%8C%E6%8A%80%E5%B7%A7.html#%E4%BF%9D%E7%95%99%E6%8C%82%E8%B5%B7%E5%90%8E%E7%9A%84%E6%98%BE%E5%AD%98> "NVIDIA/提示和技巧")。

需要以下 [udev](<../zh-cn/Udev.html> "Udev") 规则，如 NVIDIA 所建议的： 
    
    /etc/udev/rules.d/80-nvidia-pm.rules
    
    # Enable runtime PM for NVIDIA VGA/3D controller devices on driver bind
    ACTION=="bind", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x030000", TEST=="power/control", ATTR{power/control}="auto"
    ACTION=="bind", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x030200", TEST=="power/control", ATTR{power/control}="auto"
    
    # Disable runtime PM for NVIDIA VGA/3D controller devices on driver unbind
    ACTION=="unbind", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x030000", TEST=="power/control", ATTR{power/control}="on"
    ACTION=="unbind", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x030200", TEST=="power/control", ATTR{power/control}="on"

一些用户还[报告](<https://aur.archlinux.org/packages/nvidia-prime-rtd3pm#comment-920182>)以下附加行也是必要的： 
    
    /etc/udev/rules.d/80-nvidia-pm.rules
    
    # Enable runtime PM for NVIDIA VGA/3D controller devices on adding device
    ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x030000", TEST=="power/control", ATTR{power/control}="auto"
    ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x030200", TEST=="power/control", ATTR{power/control}="auto"

同时设置以下[模块参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html#%E8%AE%BE%E7%BD%AE%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97%E9%80%89%E9%A1%B9> "内核参数")： 
    
    /etc/modprobe.d/nvidia-pm.conf
    
    options nvidia "NVreg_DynamicPowerManagement=0x02"

此外，您可以安装 [nvidia-prime-rtd3pm](<https://aur.archlinux.org/packages/nvidia-prime-rtd3pm/>)AUR，它提供了这两个配置文件。 

在设置好 [udev](<../zh-cn/Udev.html> "Udev") 规则和[模块参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html#%E8%AE%BE%E7%BD%AE%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97%E9%80%89%E9%A1%B9> "内核参数")后，您需要重新启动笔记本电脑。 

要检查 NVIDIA GPU 是否已关闭，可以使用以下命令： 
    
    $ cat /sys/bus/pci/devices/0000:01:00.0/power/runtime_status
    
您将看到 `suspended` 或 `running`。如果显示 `suspended`，则 GPU 已关闭，现在功耗将为 0 瓦，从而延长电池寿命。 

在某些情况下，例如 NVIDIA RTX A1000，可能不会列出上述任何选项，而是显示 `active`。这并不一定意味着 GPU 处于 `running` 状态。在这种情况下，您可以使用以下命令检查状态： 
    
    $ cat /sys/bus/pci/devices/0000:01:00.0/power/runtime_suspended_time
    
当 GPU 处于 `suspended` 状态时，每次运行该命令时计数器都会递增。当 GPU 的状态变为 `running` 时，它将停止递增。 

如果您注意到 `runtime_suspended_time` 没有递增，您可以使用以下命令检查您的 D3 状态。 
    
    $ cat /proc/driver/nvidia/gpus/0000:01:00.0/power
    
如果它显示 `Runtime D3 status: Not supported`，您可能需要按照[此论坛帖子](<https://bbs.archlinux.org/viewtopic.php?pid=2181317#p2181317>)中的步骤禁用它。[一位用户指出](<https://bbs.archlinux.org/viewtopic.php?pid=2187680#p2187680>)禁用 `GpuFirmware` 仅适用于闭源驱动程序，不适用于 [nvidia-open](<https://archlinux.org/packages/?name=nvidia-open>)包。 

还需要[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `nvidia-persistenced.service` 服务以避免内核在 NVIDIA 设备资源不再使用时清空设备状态[[3]](<https://us.download.nvidia.com/XFree86/Linux-x86_64/550.54.14/README/nvidia-persistenced.html>)。 

####  配置应用程序使用 GPU 渲染

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[外接显卡#Xorg 在集成显卡上渲染，PRIME 渲染分载到外接显卡](<../zh-cn/%E5%A4%96%E6%8E%A5%E6%98%BE%E5%8D%A1.html#Xorg_%E5%9C%A8%E9%9B%86%E6%88%90%E6%98%BE%E5%8D%A1%E4%B8%8A%E6%B8%B2%E6%9F%93%EF%BC%8CPRIME_%E6%B8%B2%E6%9F%93%E5%88%86%E8%BD%BD%E5%88%B0%E5%A4%96%E6%8E%A5%E6%98%BE%E5%8D%A1> "外接显卡")。**

**附注：** 此小节提到了这些变量。也许这可以与此部分合并以避免重复？（在 [Talk:PRIME](<../zh-cn/Talk:PRIME.html>) 中讨论）

即使没有启用动态电源管理，应用程序的渲染分载也要启用[[4]](<https://web.archive.org/web/20211203072304/https://jeansenvaars.wordpress.com/2021/12/02/endeavouros-hybrid-gpu-benchmarks/>)。 

要在动态电源管理启用时将应用程序分载到 NVIDIA GPU，需添加以下[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")：[[5]](<https://download.nvidia.com/XFree86/Linux-x86_64/550.54.14/README/primerenderoffload.html>)
    
    __NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia _command_
    
在 [Steam](<../zh-cn/Steam.html> "Steam") 游戏上使用时, 启动命令行选项可以设置为： 
    
    __NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia %command%
    
**注意：**`__NV_PRIME_RENDER_OFFLOAD` 的值可能需要根据系统设置为 `0`。建议检查哪个 GPU 是 `0`，哪个是 `1`，因为此变量指定将使用哪个 GPU。

####  GNOME 集成

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [switcheroo-control](<https://archlinux.org/packages/?name=switcheroo-control>)包 并[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `switcheroo-control.service` 以使用 GNOME 集成。 

GNOME 尊重[桌面项](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html> "桌面项")中的 `PrefersNonDefaultGPU` 属性。或者也可以通过右键单击图标并选择 _Launch using Discrete Graphics Card_ 来使用 GPU 启动应用程序。 

###  关于windows游戏

用 Wine 或者 Proton 运行 Windows DirectX 游戏时，你需要使用如下命令指示 DXVK 要使用的 GPU： 
    
    DXVK_FILTER_DEVICE_NAME "[your preferred card name]"
    
用 `vulkaninfo` 或许显卡名称; DXVK使用字字符串匹配。 

####  疑难解答

如果安装了 [bumblebee](<https://archlinux.org/packages/?name=bumblebee>)包，则需要将其删除，因为它将 `nvida_drm` 列入黑名单，该驱动程序由 X 服务器加载 NVIDIA 驱动程序来实现渲染分载。 

###  PRIME 同步

当使用 PRIME 时，主 GPU 渲染屏幕内容/应用程序，并将其传递给备用 GPU 进行显示。参考[an NVIDIA thread 此帖](<https://forums.developer.nvidia.com/t/prime-and-prime-synchronization/44423>)，"传统的 vsync 可以将应用程序的呈现与系统内存中的副本同步，但需要一种额外的机制来将系统内存中的副本与 iGPU 的显示引擎同步。与传统的垂直同步不同，这种机制必须涉及到 dGPU 和 iGPU 驱动之间的通信。" 

这种同步是使用 PRIME 同步实现的。要检查显示系统是否启用了 PRIME 同步，可以查看 `xrandr --prop` 的输出。 

使用下面的命令启用（PRIME 同步）: 
    
    $ xrandr --output <output-name> --set "PRIME Synchronization" 1
    
**注意：**

  * 在 NVIDIA 驱动程序上使用 PRIME 同步的先决条件是启用 [NVIDIA#DRM 内核级显示模式设置](<../zh-cn/NVIDIA.html#DRM_%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE> "NVIDIA")。
  * PRIME 同步无法在 [AMDGPU](<../zh-cn/AMDGPU.html> "AMDGPU") DDX 驱动上使用（[xf86-video-amdgpu](<https://archlinux.org/packages/?name=xf86-video-amdgpu>)包）。

##  反向 PRIME

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 缺少有关为开源/闭源的 amdgpu 驱动程序配置 Intel + AMD 反向 prime 的信息 (在 [Talk:PRIME](<../zh-cn/Talk:PRIME.html>) 中讨论)

**注意：**

  * 470 beta 之前的 NVIDIA 驱动程序上的 AMDGPU + NVIDIA 不支持反向 PRIME。更多详细信息，请参考 [[6]](<https://forums.developer.nvidia.com/t/hp-omen-15-ryzen-4600h-nvidia-1660ti-no-display-over-hdmi/165265/2>)。
  * 当前仅启用外部显示器时，将只能获得 1 FPS。 更多信息参考[[7]](<https://gitlab.freedesktop.org/xorg/xserver/-/issues/1028>)，一个解决方案是使用 `LIBGL_DRI3_DISABLE=true` 环境变量。

如果第二个 GPU 的输出无法被主 GPU 访问，可以使用**反向 PRIME** 来使用它们。这将涉及使用主 GPU 渲染图像，然后将它们传递给第二个 GPU。 

它可能开箱即用，但如果不能，则需要按照以下步骤进行配置。 

###  配置

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** 上半段Intel+NVIDIA，下半段Intel+Radeon。 识别 GPU 总线 ID 应放到通用部分。（在[Talk:PRIME](<../zh-cn/Talk:PRIME.html>)讨论）

首先, 识别集成显卡的总线 ID（BusID） 
    
    lspci -d ::03xx
    
    00:02.0 VGA compatible controller: Intel Corporation UHD Graphics 630 (Mobile)
    01:00.0 VGA compatible controller: NVIDIA Corporation TU117M [GeForce GTX 1650 Mobile / Max-Q] (rev a1)
    
在上面的示例中，Intel 集成显卡的总线 ID 是 00:02.0 ，翻译到 pci 总线上为 PCI:0:2:0。 

如下设置您的 `xorg.conf` 并调整总线 ID。 
    
    /etc/X11/xorg.conf
    
    Section "ServerLayout"
            Identifier "layout"
            Screen 0 "intel"
            Inactive "nvidia"
            Option "AllowNVIDIAGPUScreens"
    EndSection
    
    Section "Device"
            Identifier "nvidia"
            Driver "nvidia"
    EndSection
    
    Section "Screen"
            Identifier "nvidia"
            Device "nvidia"
    EndSection
    
    Section "Device"
            Identifier "intel"
            Driver "modesetting"
            BusID "PCI:0:2:0"
    EndSection
    
    Section "Screen"
            Identifier "intel"
            Device "intel"
    EndSection
    
命令 `xrandr --setprovideroutputsource provider source` 将提供程序设置为源输出。 例如： 
    
    $ xrandr --setprovideroutputsource radeon Intel
    
完成后，独立显卡的输出应该在 xrandr 中可用，可以执行以下操作来配置内部和外部显示器： 
    
    $ xrandr --output HDMI-1 --auto --above LVDS1
    
###  已知问题

如果重启后你只有一个提供程序，可能是因为当 Xorg 启动时`nvidia`模块还没加载。您需要启用早期模块加载。 有关详细信息，请参阅[NVIDIA#早启动](<../zh-cn/NVIDIA.html#%E6%97%A9%E5%90%AF%E5%8A%A8> "NVIDIA")。 

##  疑难解答

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 本节中的解决方法缺乏来源支持（在 [Talk:PRIME](<../zh-cn/Talk:PRIME.html>) 中讨论）

###  XRandR 只识别出一个显卡

删除或者移走 `/etc/X11/xorg.conf` 以及 `/etc/X11/xorg.conf.d/` 目录下任何与 GPU 有关的文件 

###  当程序使用独立显卡渲染时，程序黑屏

某些情况下 PRIME 的正常工作需要一个混合窗口管理器。如果你的窗口管理器不进行混合渲染，你可以在其基础上使用[混合窗口管理器](<../zh-cn/Xorg.html#%E6%B7%B7%E5%90%88%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8%E5%88%97%E8%A1%A8> "Xorg")。 

如果你使用 Xfce，你可以进入 _菜单 > 设置 > 窗口管理器调整 > 混合器_并启用混合渲染，然后再次尝试你的应用程序。 

####  在基于 GL 的渲染合成器下黑屏

目前基于 GL 的渲染合成器和 PRIME 分载渲染还有一些问题。当基于 Xrender 的渲染合成器（xcompmgr、xfwm、compton的默认后端，cairo-compmgr 和一些其他的合成器）可以正常工作，基于 GL 的渲染合成器（Mutter/muffin、Compiz、使用 GLX 后端的 compton、Kwin 的 OpenGL 后端等）一开始会显示黑屏，就好像没有运行渲染合成器一样。虽然也可以通过调整使用渲染分载的程序窗口大小来强制显示图像，但这并不是一个实用的解决方案，因为它不适用于全屏的 Wine 应用程序。这意味着像 GNOME3 和 Cinnamon 这样的桌面环境在使用 PRIME 分载时存在问题。 

此外，如果使用的是英特尔 IGP，也许可以通过把 IGP 当作 UXA 而不是 SNA 运行来修复 GL合成问题，然而这可能会导致渲染分载进程出现问题（例如，`xrandr --listproviders` 可能不会打印独立 GPU）。 

###  某些程序在 Wayland 下打开时有延迟

如果你启用了 RTD3（来自[#NVIDIA](<#NVIDIA>)），在使用 Wayland 时，程序打开时会感到一些延迟，这是因为它会先尝试启动 GPU（这需要大约1秒或更长时间），然后才尝试打开程序，浪费了时间和电池寿命。这是 NVIDIA 驱动的问题。更多细节参见[此帖](<https://bbs.archlinux.org/viewtopic.php?pid=2094847#p2094847>)。 

欲解决该问题，请在您的 `/etc/environment`文件中添加以下两行： 
    
    /etc/environment
    
    __EGL_VENDOR_LIBRARY_FILENAMES=/usr/share/glvnd/egl_vendor.d/50_mesa.json
    __GLX_VENDOR_LIBRARY_NAME=mesa

###  使用 DXVK 运行 Wine 游戏时出错

当使用 PRIME 分载时，遇到 `Major opcode of failed request: 156 (NV-GLX)` 是一个已知问题。目前唯一的解决方法是启动X会话时[完全使用 NVIDIA GPU](<../zh-cn/NVIDIA_Optimus.html#%E4%BB%85%E4%BD%BF%E7%94%A8NVIDIA%E6%98%BE%E5%8D%A1> "NVIDIA Optimus")。一个用户友好的方式是在 NVIDIA 独显和PRIME分载方法之间切换是使用 [optimus-manager](<../zh-cn/NVIDIA_Optimus.html#%E4%BD%BF%E7%94%A8optimus-manager> "NVIDIA Optimus") 工具或自己编写一些自动化脚本。 

##  参见

  * [Nouveau Optimus](<https://wiki.freedesktop.org/nouveau/Optimus/>)
