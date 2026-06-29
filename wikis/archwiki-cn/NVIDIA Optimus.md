**翻译状态：**

  * 本文（或部分内容）译自 [NVIDIA Optimus](<https://wiki.archlinux.org/title/NVIDIA_Optimus> "arch:NVIDIA Optimus")，最近一次同步于 2025-02-09，若英文版本有所[更改](<https://wiki.archlinux.org/title/NVIDIA_Optimus?diff=0&oldid=826016>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/NVIDIA_Optimus_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [PRIME](<../zh-cn/PRIME.html> "PRIME")
  * [Bumblebee](<../zh-cn/Bumblebee.html> "Bumblebee")
  * [Nouveau](<../zh-cn/Nouveau.html> "Nouveau")
  * [NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA")
  * [nvidia-xrun](<../zh-cn/Nvidia-xrun.html> "Nvidia-xrun")
  * [External GPU](<../zh-cn/External_GPU.html> "External GPU")

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：**

  * 明确哪些内容特定于 X，哪些内容可用于 Wayland。
  * 删除剩余的“Intel”提及，改为“集成”：Optimus 也适用于 AMD 集成显卡。

(在 [Talk:NVIDIA Optimus](<../zh-cn/Talk:NVIDIA_Optimus.html>) 中讨论)

[NVIDIA Optimus](<https://en.wikipedia.org/wiki/NVIDIA_Optimus> "wikipedia:NVIDIA Optimus") 是一项允许集成图形处理器（GPU）和英伟达（NVIDIA）独立图形处理器置入并通过一台笔记本电脑访问的技术。作为前提条件，请为两张显卡安装相关的 [GPU 驱动](<../zh-cn/Xorg.html#Driver_installation> "Xorg")。 

##  可用方法

这里有几种可行的方法： 

  * [#仅使用集成显卡](<#%E4%BB%85%E4%BD%BF%E7%94%A8%E9%9B%86%E6%88%90%E6%98%BE%E5%8D%A1>) \- 能节约用电，因为此时英伟达 GPU 是完全关闭（不通电）的。
  * [#仅使用英伟达显卡](<#%E4%BB%85%E4%BD%BF%E7%94%A8%E8%8B%B1%E4%BC%9F%E8%BE%BE%E6%98%BE%E5%8D%A1>) \- 能比集成显卡提供更强的性能表现，但是更耗电（这对移动设备不太友好）。此方法和 [optimus-manager](<#%E4%BD%BF%E7%94%A8_optimus-manager>) 以及 [nvidia-xrun](<#%E4%BD%BF%E7%94%A8_nvidia-xrun>) 两者一样采用了相同的底层处理，所以在选用一种更自动化的方法之前，应该先利用这个方法来排除故障和验证一些常规功能。
  * 两者兼用 (在需要的时候使用英伟达 GPU，其他时候关闭它以节省电量): 
    * [#使用 PRIME 渲染分载（render offload）](<#%E4%BD%BF%E7%94%A8_PRIME_%E6%B8%B2%E6%9F%93%E5%88%86%E8%BD%BD%EF%BC%88render_offload%EF%BC%89>) \- 英伟达官方支持方法。
    * [#使用 optimus-manager](<#%E4%BD%BF%E7%94%A8_optimus-manager>) \- 用一个简单的命令切换显卡（需要注销重新登录来生效）。还支持与 PRIME 渲染分载的混合模式。这可实现需要时使用英伟达 GPU 达到最大性能，不用时则将后者关闭。自 1.4 版本起，还支持 AMD+NVIDIA 组合。
    * [#使用 nvidia-xrun](<#%E4%BD%BF%E7%94%A8_nvidia-xrun>) \- 使用英伟达显卡在另外的 TTY 上运行单独的 X 会话。这可实现需要时使用英伟达 GPU 达到最大性能，不用时则将后者关闭。
    * [#使用大黄蜂（Bumblebee）](<#%E4%BD%BF%E7%94%A8%E5%A4%A7%E9%BB%84%E8%9C%82%EF%BC%88Bumblebee%EF%BC%89>) \- 提供了与 Windows 下相似的功能，可以选择需要的程序使用英伟达显卡，而其他的程序则用集成显卡运行。不过大黄蜂有重大的性能问题。
    * [#使用 switcheroo-control](<#%E4%BD%BF%E7%94%A8_switcheroo-control>) \- 类似于大黄蜂，但专为 [GNOME](<../zh-cn/GNOME.html> "GNOME") 用户设计。允许应用程序在其[桌面项](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html> "桌面项")文件中指定是否偏好使用独立显卡，并允许你从右键菜单中手动选择在英伟达 GPU 上运行任意应用程序。
    * [#使用 nouveau](<#%E4%BD%BF%E7%94%A8_nouveau>) \- （与英伟达官方提供的专有驱动相比）提供的性能较差，而且可能导致睡眠和休眠问题。不适用于最新的英伟达 GPU。
    * [#使用 EnvyControl](<#%E4%BD%BF%E7%94%A8_EnvyControl>) \- 类似于 optimus-manager，但不需要复杂的配置或后台运行守护进程，如果你是 GNOME 用户，也不需要安装修补版的 GDM。
    * [#使用 NVidia-eXec](<#%E4%BD%BF%E7%94%A8_NVidia-eXec>) \- 类似于大黄蜂，但没有性能影响。它适用于 Xorg 和 Wayland。这个包是实验性的，目前仅在 GNOME/GDM 下进行测试。
    * [#使用 nvidia-switch](<#%E4%BD%BF%E7%94%A8_nvidia-switch>) \- 类似于 nvidia-xrun，但不需要切换 TTY，切换将通过登录和注销在显示管理器中完成。这个包在基于 Debian 的系统上进行测试，但像 nvidia-xrun 一样，它应该可以在所有 Linux 系统上工作。

**注意：** 所有这些方法选择都是互斥的，如果测试了一种方法后又决定使用另一种方法，则必须确保在尝试另一种方法之前，还原通过遵循前一种方法所做的所有配置更改，否则可能会发生文件冲突和不定行为。

##  仅使用集成显卡

如果你只想使用某个特定的GPU而不进行切换，请检查你系统BIOS中的选项。应该有一个选项可以禁用其中一个显卡。有些笔记本电脑只允许禁用独立显卡，或者反之，但如果你只计划使用其中一个显卡，值得检查一下。 

如果你的BIOS不允许禁用Nvidia显卡，你可以从Linux内核本身禁用它。参见[Hybrid graphics#完全关闭独立GPU](<../zh-cn/Hybrid_graphics.html#%E5%AE%8C%E5%85%A8%E5%85%B3%E9%97%AD%E7%8B%AC%E7%AB%8BGPU> "Hybrid graphics")。 

###  在不切换渲染提供程序的情况下使用CUDA

你可以在不将渲染切换到Nvidia显卡的情况下使用CUDA。你只需要确保在启动CUDA应用程序之前Nvidia显卡已通电，详见[Hybrid graphics#完全关闭独立GPU](<../zh-cn/Hybrid_graphics.html#%E5%AE%8C%E5%85%A8%E5%85%B3%E9%97%AD%E7%8B%AC%E7%AB%8BGPU> "Hybrid graphics")。 

现在，当你启动CUDA应用程序时，它将自动加载所有必要的内核模块。在使用CUDA后关闭Nvidia显卡之前，必须先卸载`nvidia`内核模块： 
    
    # rmmod nvidia_uvm
    # rmmod nvidia
    
##  仅使用英伟达显卡

专有的英伟达驱动可配置为主渲染提供程序。它也有明显的画面撕裂问题——除非通过启动 [NVIDIA#DRM 内核级显示模式设置](<../zh-cn/NVIDIA.html#DRM_%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE> "NVIDIA")启用 PRIME Sync，更多信息请参见 [[1]](<https://devtalk.nvidia.com/default/topic/957814/linux/prime-and-prime-synchronization/>)。专有驱动确实允许使用独立 GPU，而且（截至 [2017 年一月](<https://www.phoronix.com/scan.php?page=article&item=nouveau-410-blob&num=1>)）它相比 nouveau 驱动有更明显的性能优势。 

首先，安装[英伟达](<../zh-cn/NVIDIA.html> "NVIDIA")驱动和 [xorg-xrandr](<https://archlinux.org/packages/?name=xorg-xrandr>)包 软件包。然后，配置 `/etc/X11/xorg.conf.d/10-nvidia-drm-outputclass.conf`，其中的选项将与软件包提供的 `/usr/share/X11/xorg.conf.d/10-nvidia-drm-outputclass.conf` 文件结合提供与此配置的兼容性。 

**注意：** 在一些配置上，此配置会使英伟达驱动无法通过 EDID 文件自动探测显示参数值。解决方案可参考[#分辨率和屏幕扫描错误“EDID errors in Xorg.log”](<#%E5%88%86%E8%BE%A8%E7%8E%87%E5%92%8C%E5%B1%8F%E5%B9%95%E6%89%AB%E6%8F%8F%E9%94%99%E8%AF%AF%E2%80%9CEDID_errors_in_Xorg.log%E2%80%9D>)。
    
    /etc/X11/xorg.conf.d/10-nvidia-drm-outputclass.conf
    
    Section "OutputClass"
        Identifier "intel"
        MatchDriver "i915"
        Driver "modesetting"
    EndSection
    
    Section "OutputClass"
        Identifier "nvidia"
        MatchDriver "nvidia-drm"
        Driver "nvidia"
        Option "AllowEmptyInitialConfiguration"
        Option "PrimaryGPU" "yes"
        ModulePath "/usr/lib/nvidia/xorg"
        ModulePath "/usr/lib/xorg/modules"
    EndSection
    
接下来，依所使用的登录图形的方式不同而有所不同，请按实际情况选择阅读。 

### startx

请在 `~/.xinitrc` 文件的开头处添加下列两行内容： 
    
    ~/.xinitrc
    
    xrandr --setprovideroutputsource modesetting NVIDIA-0
    xrandr --auto
    
现在重启以加载驱动，X 服务器也应该启动了。 

如果显示 DPI 不正确，请再添加下列一行： 
    
    xrandr --dpi 96
    
如果在启动 X 服务器时出现黑屏，请确保 `~/.xinitrc` 文件中的两个 `xrandr` 命令后面没有“&”符号。如果有“&”号，窗口管理器可能在 `xrandr` 命令执行完成前就运行了，从而导致了黑屏。 

###  显示管理器

如果打算使用[显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")，就不是使用 `~/.xinitrc` 文件了，而是需要为显示管理器创建或编辑显示配置脚本。 

#### LightDM

为 [LightDM](<../zh-cn/LightDM.html> "LightDM") 显示管理器创建/编辑脚本： 
    
    /etc/lightdm/display_setup.sh
    
    #!/bin/sh
    xrandr --setprovideroutputsource modesetting NVIDIA-0
    xrandr --auto
    
然后赋予脚本[可执行](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "可执行")权限。 

通过编辑 `/etc/lightdm/lightdm.conf` 的 `[Seat:*]` 部分配置 LightDM 来运行这个脚本： 
    
    # nano /etc/lightdm/lightdm.conf
    
    [Seat:*]
    display-setup-script=/etc/lightdm/display_setup.sh

现在重启，然后显示管理器应该能启动了。 

#### SDDM

为 [SDDM](<../zh-cn/SDDM.html> "SDDM") 显示管理器创建/编辑脚本（SDDM 是 [KDE](<../zh-cn/KDE.html> "KDE") 的默认显示管理器）： 
    
    /usr/share/sddm/scripts/Xsetup
    
    xrandr --setprovideroutputsource modesetting NVIDIA-0
    xrandr --auto
    
#### GDM

要为 [GDM](<../zh-cn/GDM.html> "GDM") 创建启动脚本，请创建两个新的 .desktop 文件，如下： 
    
    /usr/share/gdm/greeter/autostart/optimus.desktop
    /etc/xdg/autostart/optimus.desktop
    
    [Desktop Entry]
    Type=Application
    Name=Optimus
    Exec=sh -c "xrandr --setprovideroutputsource modesetting NVIDIA-0; xrandr --auto"
    NoDisplay=true
    X-GNOME-Autostart-Phase=DisplayServer
    
并且请确保 GDM [使用 Xorg 作为后端](<../zh-cn/GDM.html#%E4%BD%BF%E7%94%A8Xorg%E5%90%8E%E7%AB%AF> "GDM")。 

###  检查 3D 设置

可通过安装 [mesa-utils](<https://archlinux.org/packages/?name=mesa-utils>)包 并运行以下命令来检查英伟达显卡是否被使用： 
    
    $ glxinfo | grep NVIDIA
    
###  更多信息

更多信息请参见英伟达官方网页上的这个主题文章 [[2]](<https://us.download.nvidia.cn/XFree86/Linux-x86/370.28/README/randr14.html>)。 

##  使用可切换显卡

###  使用 PRIME 渲染分载（render offload）

这是 NVIDIA 官方支持可切换显卡的方法。 

参见 [PRIME#PRIME 渲染分载](<../zh-cn/PRIME.html#PRIME_%E6%B8%B2%E6%9F%93%E5%88%86%E8%BD%BD> "PRIME")。 

###  使用 nouveau

图形切换参见 [PRIME](<../zh-cn/PRIME.html> "PRIME")，开源 NVIDIA驱动程序见 [nouveau](<../zh-cn/Nouveau.html> "Nouveau")。 

###  使用大黄蜂（Bumblebee）

参见 [Bumblebee](<../zh-cn/Bumblebee.html> "Bumblebee")。 

###  使用 switcheroo-control

参见 [PRIME#GNOME 集成](<../zh-cn/PRIME.html#GNOME_%E9%9B%86%E6%88%90> "PRIME")。 

###  使用 nvidia-xrun

参见 [nvidia-xrun](<../zh-cn/Nvidia-xrun.html> "Nvidia-xrun")。 

###  使用 optimus-manager

参见 [Optimus-manager](<https://github.com/Askannz/optimus-manager>) 上游文档。它涵盖了在 Arch Linux 系统中的安装和配置。 

###  使用 EnvyControl

参见 [EnvyControl](<https://github.com/geminis3/envycontrol>) 上游文档。它涵盖了安装和使用说明。 

###  使用 NVidia-eXec

参见 [NVidia-eXec](<https://github.com/pedro00dk/nvidia-exec>) 上游文档。它涵盖了安装和使用说明。 

###  使用 nvidia-switch

参见 [nvidia-switch](<https://github.com/nvidiaswitch/nvidia-switch>) 上游文档。它涵盖了安装和使用说明。 

##  疑难解答

###  垂直同步撕裂

开启 [DRM 内核级显示模式设置](<../zh-cn/NVIDIA.html#DRM%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE> "NVIDIA")，这将启用 PRIME 同步并修复撕裂问题。 

官方论坛查看详细信息：[forum thread](<https://devtalk.nvidia.com/default/topic/957814/linux/prime-and-prime-synchronization/>)。 

###  Failed to initialize the NVIDIA GPU at PCI:1:0:0 (GPU fallen off the bus / RmInitAdapter failed!)

添加 `rcutree.gp_init_delay=1` 到内核参数。原始话题见 [[3]](<https://github.com/Bumblebee-Project/Bumblebee/issues/455#issuecomment-22497464>) 和 [[4]](<https://bbs.archlinux.org/viewtopic.php?id=169742>)。 

###  分辨率和屏幕扫描错误“EDID errors in Xorg.log”

这是由于 NVIDIA 的驱动程序没有检测显示器的 EDID。你需要手动指定路径的 EDID 文件或以类似的方式提供相同的信息。 

增加这些线路和变化部分反映你自己的系统： 
    
    /etc/X11/xorg.conf
    
    Section "Device"
           	Option		"ConnectedMonitor" "CRT-0"
           	Option		"CustomEDID" "CRT-0:/sys/class/drm/card0-LVDS-1/edid"
    	Option		"IgnoreEDID" "false"
    	Option		"UseEDID" "true"
    EndSection
    
如果 Xorg 不会启动，尝试将所有 CRT 替换为 DFB。`card0` 是标识为英特尔卡，显示器通过 LVDS 连接。EDID 二进制文件位于此目录。如果硬件配置不同，CustomEDID 的值可能有所不同，但这已得到证实。不管怎样，路径都将从 `/sys/class/drm` 开始。 

或者你可以使用工具如 [read-edid](<https://archlinux.org/packages/?name=read-edid>)包 生成你的 EDID，并将驱动指向此文件。也可以使用 modelines，但是务必要修改 `UseEDID` 和 `IgnoreEDID`。 

###  无 EDID 错误的分辨率问题

使用 _nvidia-xconfig_ 时，可能会在 `xorg.conf` 中生成错误的信息，特别是错误的显示器刷新率，限制了可能的分辨率。尝试注释掉 `HorizSync`/`VertRefresh` 行。如果这有帮助，你可能还可以删除本文中未提及的其他内容。 

###  锁定问题(lspci 挂起)

问题：lspci 挂起，系统暂停失败，关机时挂起，optirun 挂起。多出现在新的笔记本电脑或使用了类似 bbswitch GTX 的 965m 时（例如 bumblebee）以及 nouveau 的情况。 

当独立显卡接通电源，可能出现这种情况，参见 ([kernel bug 156341](<https://bugzilla.kernel.org/show_bug.cgi?id=156341>))。 

具体解决方法参见 [this issue](<https://github.com/Bumblebee-Project/Bumblebee/issues/764#issuecomment-234494238>)。 你可以添加 `acpi_osi="!Windows 2015"` 或 `acpi_osi=! acpi_osi="Windows 2009"` 到[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")中。 

###  笔记本电脑未发现屏幕/NVIDIA Optimus

检查输出是否类似： 
    
    $ lspci | grep VGA
    
    00:02.0 VGA compatible controller: Intel Corporation Core Processor Integrated Graphics Controller (rev 02)
    01:00.0 VGA compatible controller: nVidia Corporation Device 0df4 (rev a1)
    
NVIDIA 驱动自 319.12 Beta [[5]](<https://www.nvidia.com/object/linux-display-amd64-319.12-driver.html>) 起已经包含在内核（版本 3.9 级以上）中。 

另一个解决方案是安装 [Intel](<../zh-cn/Intel_%E5%9B%BE%E5%BD%A2%E5%A4%84%E7%90%86%E5%99%A8.html> "Intel") 驱动进行显示，如果需要运行 3D 软件，可以使用 [Bumblebee](<../zh-cn/Bumblebee.html> "Bumblebee") 来使用 NVIDIA 显卡。 

###  随机冻结 "(EE) NVIDIA(GPU-0): WAIT"

在使用集成 AMD 卡和专用 NVIDIA 卡的设置上使用专有驱动时，用户报告冻结长达 10 秒，Xorg 日志中出现以下错误： 
    
    [   219.796] (EE) NVIDIA(GPU-0): WAIT (2, 8, 0x8000, 0x0002e1c4, 0x0002e1cc)
    [   226.796] (EE) NVIDIA(GPU-0): WAIT (1, 8, 0x8000, 0x0002e1c4, 0x0002e1cc)
    
虽然尚未找到根本原因，但似乎与集成卡和专用卡与 Xorg 的交互方式冲突有关。 

解决方法是使用可切换显卡，详见 [PRIME#PRIME render offload](<../zh-cn/PRIME.html#PRIME_render_offload> "PRIME")。 

###  使用 optimus-manager 时出现 "No Devices detected"

在某些情况下， _lspci_ 会将 PCI 域作为第一列输出，导致 _optimus-manager_ 生成的文件在尝试映射 `BusID` 时在多款笔记本电脑上出现问题。 

如果你遇到黑屏、GUI 部分加载或 Xorg 崩溃并显示 `(EE) - No Devices detected`，解决方法和错误报告可在[上游 GitHub](<https://github.com/Askannz/optimus-manager/issues/471#issuecomment-1315628537>) 找到。 

###  Xorg：外部显示器仅在鼠标移动时更新

解决方法是卸载 iGPU 的 Xorg 驱动（例如 [xf86-video-amdgpu](<https://archlinux.org/packages/?name=xf86-video-amdgpu>)包 或 [xf86-video-intel](<https://archlinux.org/packages/?name=xf86-video-intel>)包）[[6]](<https://bbs.archlinux.org/viewtopic.php?id=284651>)。只要外部显示器端口（HDMI/DP/USB-C）直接连接到 NVIDIA dGPU，这应该有效。 

**提示：** 桌面行为可能会变得不稳定（例如切换虚拟桌面或 Alt-Tab 时外部显示器图像冻结），也可以通过禁用笔记本电脑的显示器来解决。

###  低功耗（TDP）

自 530.41 驱动版本以来，出现了显卡锁定在低功耗限制的情况（参见 [GitHub issue 483](<https://github.com/NVIDIA/open-gpu-kernel-modules/issues/483>)）。NVIDIA 驱动已禁用使用 `nvidia-smi` 命令手动设置功耗限制的功能，因此许多笔记本电脑被锁定在低功耗和性能不佳的状态。 

要解决此问题（适用于 Ampere 代或更新），[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `nvidia-powerd.service`，这将启用 [DynamicBoost](<https://download.nvidia.com/XFree86/Linux-x86_64/535.54.03/README/dynamicboost.html>)。 

###  NVIDIA GPU 无法关闭或保持停用状态

某些进程可能会由于它们与 GPU 的交互方式而保持你的 NVIDIA GPU 处于活动状态。这会导致功耗显著增加、电池寿命缩短和温度升高。 

你可以通过运行以下命令检查你的 GPU 是否处于活动状态或已挂起： 
    
    $ cat /sys/bus/pci/devices/0000\:01\:00.0/power/runtime_status
    
如果状态为 `active`，你可能正在运行一个保持 GPU 活动的进程。 

如果你使用一个探测 GPU 温度的温度监控器，它通常会调用 `nvidia-smi` 来获取此温度，这将唤醒你的 GPU 并保持其处于活动状态。 

你可以使用 [nvtop](<https://archlinux.org/packages/?name=nvtop>)包 检查是否有进程（如 Xorg）正在使用 NVIDIA GPU，但此方法并非在所有情况下都有效。例如，如果你运行 [ollama](<https://archlinux.org/packages/?name=ollama>)包 服务器，它将始终保持你的 GPU 处于活动状态，但不会显示在 `nvtop` 或调用 `nvidia-smi` 中。 

记得检查与你选择的故障排除方法相关的文章。 
