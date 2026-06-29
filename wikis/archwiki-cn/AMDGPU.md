**翻译状态：**

  * 本文（或部分内容）译自 [AMDGPU](<https://wiki.archlinux.org/title/AMDGPU> "arch:AMDGPU")，最近一次同步于 2025-01-22，若英文版本有所[更改](<https://wiki.archlinux.org/title/AMDGPU?diff=0&oldid=825479>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/AMDGPU_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [ATI](<../zh-cn/ATI.html> "ATI")
  * [Xorg](<../zh-cn/Xorg.html> "Xorg")
  * [Vulkan](<../zh-cn/Vulkan.html> "Vulkan")
  * [AMDGPU PRO](<../zh-cn/AMDGPU_PRO.html> "AMDGPU PRO")

[AMDGPU](<https://en.wikipedia.org/wiki/AMDGPU> "wikipedia:AMDGPU") 是 [Graphics Core Next](<https://en.wikipedia.org/wiki/Graphics_Core_Next> "wikipedia:Graphics Core Next") 系列 AMD Radeon 图形卡的开源图形驱动程序。 

##  选择正确的驱动

请根据您的显卡，参考[Xorg#AMD](<../zh-cn/Xorg.html#AMD> "Xorg")选择合适的显卡驱动。目前驱动支持从 [Southern Islands](<https://www.x.org/wiki/RadeonFeature/>)（GCN 1，发布于2012年） 到最新的显卡，而AMD没有计划支持 GCN 架构之前的显卡。如果您使用的是 AMD 不支持的显卡，可以选择使用开源的 [ATI](<../zh-cn/ATI.html> "ATI") 驱动。 

##  安装

安装 [mesa](<https://archlinux.org/packages/?name=mesa>)包 软件包，它提供用于3D加速的DRI驱动程序和用于[加速视频解码](<#%E8%A7%86%E9%A2%91%E5%8A%A0%E9%80%9F>)的 VA-API/VDPAU 驱动。 

  * 对于32位程序，请从 [multilib](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "Multilib") 仓库中安装 [lib32-mesa](<https://archlinux.org/packages/?name=lib32-mesa>)包 软件包以获得支持。
  * 对于 DDX 驱动支持(可提供对 [Xorg](<../zh-cn/Xorg.html> "Xorg") 的 2D 加速)，可以安装 [xf86-video-amdgpu](<https://archlinux.org/packages/?name=xf86-video-amdgpu>)包 软件包。
  * 对于 [Vulkan](<../zh-cn/Vulkan.html> "Vulkan") 支持： 
    * **安装[vulkan-radeon](<https://archlinux.org/packages/?name=vulkan-radeon>)包** 驱动：尽管 _vulkan-driver_ 提供的第一个选择不是它（因为[可选按照字母顺序排序](<../zh-cn/Pacman.html#%E8%99%9A%E5%8C%85> "Pacman")）。
    * 对应安装的原生驱动，可选择性安装 [lib32-vulkan-radeon](<https://archlinux.org/packages/?name=lib32-vulkan-radeon>)包 软件包来获得32位应用程序支持。

###  实验版本

对于某些用户来说使用 mesa 的上游实验构建可能是值得的。 

安装 [mesa-git](<https://aur.archlinux.org/packages/mesa-git/>)AUR 软件包，它提供用于3D加速的DRI驱动程序。 

  * 对于32位程序支持，请从 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 或者 _mesa-git_ 仓库安装 [lib32-mesa-git](<https://aur.archlinux.org/packages/lib32-mesa-git/>)AUR
  * 对于 DDX 驱动支持(可提供对 [Xorg](<../zh-cn/Xorg.html> "Xorg") 的2D加速)，安装 [xf86-video-amdgpu-git](<https://aur.archlinux.org/packages/xf86-video-amdgpu-git/>)AUR软件包。
  * 如果您使用 _mesa-git_ 仓库并且要启用 [Vulkan](<../zh-cn/Vulkan.html> "Vulkan") 支持，请安装 [amdonly-gaming-vulkan-radeon-git](<https://aur.archlinux.org/packages/amdonly-gaming-vulkan-radeon-git/>)AUR 软件包。可选安装 [lib32-amdonly-gaming-vulkan-radeon-git](<https://aur.archlinux.org/packages/lib32-amdonly-gaming-vulkan-radeon-git/>)AUR来支持32位应用程序。如果您用的是来自 AUR 的 [mesa-git](<https://aur.archlinux.org/packages/mesa-git/>)AUR 软件包，则不需要进行该操作。

**提示：** 如果您不想用 [mesa-git](<https://aur.archlinux.org/packages/mesa-git/>)AUR 编译安装驱动（很耗时），您也可以使用 [mesa-git](<../zh-cn/%E9%9D%9E%E5%AE%98%E6%96%B9%E7%94%A8%E6%88%B7%E4%BB%93%E5%BA%93.html#mesa-git> "非官方用户仓库") 这个非官方用户仓库

###  启用 Southern Islands (SI) 和 Sea Islands (CIK) 支持

[官方支持的内核](<../zh-cn/%E5%86%85%E6%A0%B8.html#%E5%AE%98%E6%96%B9%E6%94%AF%E6%8C%81%E7%9A%84%E5%86%85%E6%A0%B8> "内核")启用了 AMDGPU 驱动，支持 Southern Islands（GCN 1，发布于2012年）和 Sea Islands （GCN 2，发布于2013年）显卡。`amdgpu` 内核驱动程序需要在[radeon](<../zh-cn/ATI.html> "ATI")之前加载。可以通过运行`lspci -k`来检查加载了哪个内核驱动程序。示例输出如下： 
    
    $ lspci -k -d ::03xx
    
    01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Curacao PRO [Radeon R7 370 / R9 270/370 OEM]
    	Subsystem: Gigabyte Technology Co., Ltd Device 226c
    	Kernel driver in use: amdgpu
    	Kernel modules: radeon, amdgpu
    
如果 `amdgpu` 驱动没有被加载使用，可以跟着下面的内容进行处理。 

####  加载 amdgpu 内核驱动

`amdgpu` 和 `radeon` 两个模块都需要设置的[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")是 `cik_support=` 和 `si_support=`。 

它们需要在内核参数或 _modprobe_ 配置文件中进行设置，具体参数取决于显卡的 GCN 版本。 

如果不确定您拥有的是哪个版本的显卡，那么也可以同时使用这两个参数。 

**提示：**[dmesg](<../zh-cn/%E6%A0%B8%E5%BF%83%E5%B7%A5%E5%85%B7.html#%E5%9F%BA%E7%A1%80> "核心工具")可能会指示应该使用的正确内核参数: `[..] amdgpu 0000:01:00.0: Use radeon.cik_support=0 amdgpu.cik_support=1 to override`.

#####  在内核命令行中设置内核模块参数

设置以下[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")之一: 

  * Southern Islands (SI): `radeon.si_support=0 amdgpu.si_support=1`
  * Sea Islands (CIK): `radeon.cik_support=0 amdgpu.cik_support=1`

####  指定正确的模块加载顺序

当内核启用 AMDGPU 对 SI/CIK 显卡的支持时，[radeon](<../zh-cn/ATI.html> "ATI")驱动可能会在`amdgpu`驱动之前加载。 

确保`amdgpu`在[Mkinitcpio#MODULES](<../zh-cn/Mkinitcpio.html#MODULES> "Mkinitcpio")数组中被设置为第一个模块，例如`MODULES=(amdgpu radeon)`。 

#####  设置内核参数

对于 Southern Islands (SI) 使用 `si_support=1` [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")，对于 Sea Islands (CIK) 使用 `cik_support=1`: 
    
    /etc/modprobe.d/amdgpu.conf
    
    options amdgpu si_support=1
    options amdgpu cik_support=1
    
    /etc/modprobe.d/radeon.conf
    
    options radeon si_support=0
    options radeon cik_support=0

确保 `modconf` 添加到 `HOOKS` 数组中在 `/etc/mkinitcpio.conf` 和 [Mkinitcpio#创建和启用镜像](<../zh-cn/Mkinitcpio.html#%E5%88%9B%E5%BB%BA%E5%92%8C%E5%90%AF%E7%94%A8%E9%95%9C%E5%83%8F> "Mkinitcpio")。 

####  编译支持 amdgpu 驱动的内核

在构建或者编译内核的时候，需要在配置中设置 `CONFIG_DRM_AMDGPU_SI=Y` 和/或者 `CONFIG_DRM_AMDGPU_CIK=Y`。 

####  在系统启动时候完全禁用 radeon 内核驱动模块

内核可能仍会根据涉及的具体图形芯片探测并加载 radeon 模块，但在确认 amdgpu 正常工作后，radeon 模块就不需要加载了。 在每个步骤之间重新启动以确认它在移动到下一步之前有效： 

  1. 在内核命令行添加模块参数以确保 `amdgpu` 按预期工作，
  2. 使用 `MODULES=(amdgpu)` mkinitcpio 方法但**不要将** `radeon` 添加到配置中，
  3. 在登录桌面后测试 `modprobe -r radeon` 命令确保能够在卸载 `radeon` 内核模块后不影响系统图形界面的运行，
  4. 将 `radeon` 模块列入黑名单，以免在第二阶段启动期间被内核探测：

    /etc/modprobe.d/radeon.conf
    
    blacklist radeon

当上面的配置生效之后，命令 `lsmod` 和 `dmesg` 的输出现在应该只会显示 amdgpu 驱动模块被加载的消息，不会存在 radeon 驱动模块的消息。系统中的 `/sys/module/radeon` 目录应该也不存在。如果存在，则说明配置没有生效，radeon 驱动模块仍然被系统加载了。 

###  ACO编译器

[ACO编译器](<https://steamcommunity.com/games/221410/announcements/detail/1602634609636894200>)是一个由 [Valve Corporation](<https://en.wikipedia.org/wiki/Valve_Corporation> "wikipedia:Valve Corporation")开发的开源着色器（shader）编译器，可直接与 [LLVM编译器](<https://llvm.org/>) 以及 [Windows 10](<https://en.wikipedia.org/wiki/Windows_10> "wikipedia:Windows 10") 竞争。与 LLVM 相比，它提供更短的编译时间，并且在玩游戏时表现更好。 

一些基准性能测试可以在 [GitHub](<https://gist.github.com/pendingchaos/aba1e4c238cf039d17089f29a8c6aa63>) 和 Phoronix [(1)](<https://www.phoronix.com/scan.php?page=article&item=radv-aco-llvm&num=1>) [(2)](<https://www.phoronix.com/scan.php?page=article&item=radv-aco-gcn10&num=1>) [(3)](<https://www.phoronix.com/scan.php?page=article&item=mesa20radv-aco-amdvlk&num=1>)中看到。 

从 [mesa](<https://archlinux.org/packages/?name=mesa>)包[20.2](<https://docs.mesa3d.org/relnotes/20.2.0.html#new-features>) 版本开始, ACO 是默认着色器编译器。 

##  加载

应该会在系统启动时自动加载。 

如果没有自动加载: 

  * 如果需要的话，确保 [#开启 Southern Islands (SI) and Sea Islands (CIK) 支持](<#%E5%BC%80%E5%90%AF_Southern_Islands_\(SI\)_and_Sea_Islands_\(CIK\)_%E6%94%AF%E6%8C%81>)。
  * 确保你已经安装最新的 [linux-firmware](<https://archlinux.org/packages/?name=linux-firmware>)包 软件包。
  * 确保你没有将 `nomodeset` 或 `vga=` 作为内核参数，因为`amdgpu` 需要[内核级显示模式设置](<../zh-cn/%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE.html> "内核级显示模式设置")。
  * 确保你没有禁用 `amdgpu` 通过使用[内核模块黑名单](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html#%E9%BB%91%E5%90%8D%E5%8D%95> "内核模块")。

尽管驱动有可能自动加载，但是加载可能会发生在 X 服务器需要它的时间点之后。这种情况下请参考[内核级显示模式设置#KMS 早启动](<../zh-cn/%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE.html#KMS_%E6%97%A9%E5%90%AF%E5%8A%A8> "内核级显示模式设置")。 

##  Xorg 配置

[Xorg](<../zh-cn/Xorg.html> "Xorg") 会自动加载驱动程序，并且使用显示器的 EDID 来设置原始分辨率。只有在调整驱动程序时才需要配置。 

如果你想手动配置，新建 `/etc/X11/xorg.conf.d/20-amdgpu.conf` 文件，并在其中添加以下内容： 
    
    /etc/X11/xorg.conf.d/20-amdgpu.conf
    
    Section "OutputClass"
         Identifier "AMD"
         MatchDriver "amdgpu"
         Driver "amdgpu"
     EndSection

使用此部分配置，您可以启用功能并调整驱动程序设置，请在设置驱动程序选项之前先查看 [amdgpu(4)](<https://man.archlinux.org/man/amdgpu.4>)。 

###  无撕裂渲染

_TearFree_ 使用硬件翻页机制控制撕裂预防。默认情况下，如果旋转画面输出、使用RandR变换和RandR 1.4 从属输出时，TearFree会被启用，其他情况下默认关闭。你可以通过指定`true`或`false`来控制此配置保持启用/关闭： 
    
    Option "TearFree" "true"
    
###  DRI 级别

_DRI_ 设置要启用的最大 DRI 级别。DRI2 的有效值为“2”，DRI3 的有效值为“3”。如果 [Xorg](<../zh-cn/Xorg.html> "Xorg") 版本 >= 1.18.3，则 DRI3 的默认值为“3”，否则使用 DRI2： 
    
    Option "DRI" "3"
    
###  可变刷新率

参考[可变刷新率](<../zh-cn/%E5%8F%AF%E5%8F%98%E5%88%B7%E6%96%B0%E7%8E%87.html> "可变刷新率")。 

###  10-bit 色深

**警告：** 当启用 10 位深度颜色时，许多应用程序可能会出现图形瑕疵或崩溃。尤其是 [Steam](<../zh-cn/Steam/%E7%96%91%E9%9A%BE%E8%A7%A3%E7%AD%94.html#Steam:_An_X_Error_occurred> "Steam/Troubleshooting")，它因 X 错误而崩溃。

较新的 AMD 显卡支持 10bpc 颜色，但默认为 24 位颜色，必须明确启用 30 位颜色。 如果应用程序也支持，启用它可以减少渐变中的可见条带/伪影。 要检查您的显示器是否支持它，请在您的 [Xorg 日志文件](<../zh-cn/Xorg.html#General> "Xorg")中搜索“EDID”（例如 `/var/log/Xorg.0.log` 或 `~/ .local/share/xorg/Xorg.0.log`): 
    
    [   336.695] (II) AMDGPU(0): EDID for output DisplayPort-0
    [   336.695] (II) AMDGPU(0): EDID for output DisplayPort-1
    [   336.695] (II) AMDGPU(0): Manufacturer: DEL  Model: a0ec  Serial#: 123456789
    [   336.695] (II) AMDGPU(0): Year: 2018  Week: 23
    [   336.695] (II) AMDGPU(0): EDID Version: 1.4
    [   336.695] (II) AMDGPU(0): Digital Display Input
    **[   336.695] (II) AMDGPU(0): 10 bits per channel**
    
要检查它当前是否启用可以通过搜索“Depth”: 
    
    [   336.618] (**) AMDGPU(0): Depth 30, (--) framebuffer bpp 32
    [   336.618] (II) AMDGPU(0): Pixel depth = 30 bits stored in 4 bytes (32 bpp pixmaps)
    
使用默认配置，log 会显示 depth 为 24，并且 24 位色彩存储在 4 个字节中。 

要检查 10 bits色深是否工作，请退出 Xorg（如果它正在运行）并运行 `Xorg -retro` 这将显示黑白网格，然后按 `Ctrl-Alt-F1` 和 { {ic|Ctrl-C}} 退出 X，然后运行 `Xorg -depth 30 -retro`。 如果这些命令能正常执行，那么就说明10位色深生效了。 

要通过 `startx` 以 10 位色深启动，请使用 `startx -- -depth 30`。 要永久启用它，请添加到（如果没有指定文件则新建）： 
    
    /etc/X11/xorg.conf.d/20-amdgpu.conf
    
    Section "Screen"
    	Identifier "asdf"
    	DefaultDepth 30
    EndSection

###  降低输出延迟

如果您想最大程度地减少延迟，您可以禁用翻页（page fliping）和无撕裂（tear free）： 
    
    /etc/X11/xorg.conf.d/20-amdgpu.conf
    
    Section "OutputClass"
         Identifier "AMD"
         MatchDriver "amdgpu"
         Driver "amdgpu"
         Option "EnablePageFlip" "off"
         Option "TearFree" "false"
    EndSection

参考[游戏#降低_DRI_延迟](<../zh-cn/%E6%B8%B8%E6%88%8F.html#%E9%99%8D%E4%BD%8E_DRI_%E5%BB%B6%E8%BF%9F> "游戏")来降低显示延迟。 

**注意：** 设置这些选项可能会导致出现撕裂和短暂的瑕疵。

##  特性

###  视频加速

参考[硬件视频加速#AMD/ATI](<../zh-cn/%E7%A1%AC%E4%BB%B6%E8%A7%86%E9%A2%91%E5%8A%A0%E9%80%9F.html#AMD/ATI> "硬件视频加速"). 

###  性能监控

GPU性能监控通常用于检查温度以及 GPU 的 P-states。 

####  命令行界面

  * **amdgpu_top** — 显示AMDGPU使用率的工具

     <https://github.com/Umio-Yasuno/amdgpu_top> || [amdgpu_top](<https://archlinux.org/packages/?name=amdgpu_top>)包

  * **nvtop** — AMD、Intel 和 NVIDIA 的 GPU 进程监控

     <https://github.com/Syllo/nvtop> || [nvtop](<https://archlinux.org/packages/?name=nvtop>)包

  * **radeontop** — GPU 利用率查看器，包括总活动百分比和单个块

     <https://github.com/clbr/radeontop> || [radeontop](<https://archlinux.org/packages/?name=radeontop>)包

####  图形用户界面

  * **amdgpu_top** — 显示AMDGPU使用率的工具

     <https://github.com/Umio-Yasuno/amdgpu_top> || [amdgpu_top](<https://aur.archlinux.org/packages/amdgpu_top/>)AUR

  * **AmdGuid** — 完全用Rust编写的一个基本的图形用户界面风扇控制工具

     <https://github.com/Eraden/amdgpud> || [amdguid-wayland-bin](<https://aur.archlinux.org/packages/amdguid-wayland-bin/>)AUR, [amdguid-glow-bin](<https://aur.archlinux.org/packages/amdguid-glow-bin/>)AUR

  * **TuxClocker** — Qt5监控和超频工具。

     <https://github.com/Lurkki14/tuxclocker> || [tuxclocker](<https://aur.archlinux.org/packages/tuxclocker/>)AUR

####  手动

检查GPU的P-states，执行： 
    
    $ cat /sys/class/drm/card0/device/pp_od_clk_voltage
    
监控GPU，执行： 
    
    # watch -n 0.5 cat /sys/kernel/debug/dri/0/amdgpu_pm_info
    
检查GPU利用率，执行： 
    
    $ cat /sys/class/drm/card0/device/gpu_busy_percent
    
检查GPU频率，执行： 
    
    $ cat /sys/class/drm/card0/device/pp_dpm_sclk
    
检查GPU温度，执行： 
    
    $ cat /sys/class/drm/card0/device/hwmon/hwmon*/temp1_input
    
检查显存频率，执行： 
    
    $ cat /sys/class/drm/card0/device/pp_dpm_mclk
    
检查显存占用，执行： 
    
    $ cat /sys/class/drm/card0/device/mem_info_vram_used
    
检查显存大小，执行： 
    
    $ cat /sys/class/drm/card0/device/mem_info_vram_total
    
###  超频

从 Linux 4.17 开始, 只要开启了相关功能，就可以通过 `/sys/class/drm/card0/device/pp_od_clk_voltage` 调整显卡的频率和电压。 

####  启动参数

需要通过附加[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数") `amdgpu.ppfeaturemask=0xffffffff` 来解锁在 sysfs 中对其的访问限制。 

并非所有比特位都有定义，随着时间的推移可能会添加新功能。设置所有 32 位可能会（在将来的更新中）启用不稳定的功能，这些功能可能会导致屏幕闪烁或无法从挂起中恢复等问题。结合默认的 ppfeaturemask 设置 PP_OVERDRIVE_MASK 位 0x4000 应该就足够了。 要为系统计算一个合理的参数，可以执行： 
    
    $ printf 'amdgpu.ppfeaturemask=0x%x\n' "$(($(cat /sys/module/amdgpu/parameters/ppfeaturemask) | 0x4000))"
    
####  手动（默认）

**注意：** 在 sysfs 中，`/sys/class/drm/...` 之类的路径只是符号链接，可能会在重新启动之间发生变化。永久位置可以在 `/sys/devices/` 中找到，例如 `/sys/devices/pci0000:00/0000:00:01.0/0000:01:00.0/`。想要得到可靠的结果可能要相应地调整命令。

要深入了解所有可能的选项，请参阅[amdgpu功耗与发热控制](<https://docs.kernel.org/gpu/amdgpu/thermal.html#pp-od-clk-voltage>)内核文档。 

可以为最大 P-state 7 设置 GPU 核心频率， 以 Polaris GPU 为例可以执行下面的命令设置为 1209MHz 频率和 900mV 电压： 
    
    # echo "s 7 1209 900" > /sys/class/drm/card0/device/pp_od_clk_voltage
    
同样的操作可以应用于 VRAM，例如 Polaris 5xx 系列卡上的最大 P-state 2： 
    
    # echo "m 2 1850 850" > /sys/class/drm/card0/device/pp_od_clk_voltage
    
**警告：** 仔细检查输入的值，因为错误可能会导致硬件损坏！

执行下面的命令让修改生效： 
    
    # echo "c" > /sys/class/drm/card0/device/pp_od_clk_voltage
    
要检查超频是否成功，可以读取 3D 负载下的时钟和电压： 
    
    # watch -n 0.5  cat /sys/kernel/debug/dri/0/amdgpu_pm_info
    
可以使用下面的命令重置为默认设置： 
    
    # echo "r" > /sys/class/drm/card0/device/pp_od_clk_voltage
    
如果要避免深度节能 P-states 引起的闪烁、伪影和卡顿之类的问题，也可以禁止驱动程序切换到某些 P-states。要让显卡强制使用最高的 VRAM P-state，同时允许 GPU 本身以较低的频率运行，首先找到最高的可用P-state，然后设置： 
    
    # cat /sys/class/drm/card0/device/pp_dpm_mclk
    
    0: 96Mhz *
    1: 456Mhz 
    2: 675Mhz 
    3: 1000Mhz 
    
    # echo "manual" > /sys/class/drm/card0/device/power_dpm_force_performance_level
    # echo "3" >  /sys/class/drm/card0/device/pp_dpm_mclk
    
仅允许三个最高的 GPU pstates： 
    
    # echo "5 6 7" >  /sys/class/drm/card0/device/pp_dpm_sclk
    
执行下面命令可以限制GPU的极限功耗（参数以 50 瓦为例）： 
    
    # echo **50** 000000 > /sys/class/drm/card0/device/hwmon/hwmon0/power1_cap
    
**注意：** 上述程序已使用 Polaris RX 560 卡进行测试。不同的 GPU 可能会有不同的行为或错误。

####  辅助工具

如果不想（或不敢）完全通过手动超频 GPU，社区提供了一些超频工具来帮助超频和监控 AMD 显卡。 

#####  命令行工具

  * **amdgpu-clocks** — 用于监控和设置 AMD GPU 自定义电源状态的脚本。它还提供了一个 Systemd 服务，可以在系统启动时自动置。

     <https://github.com/sibradzic/amdgpu-clocks> || [amdgpu-clocks-git](<https://aur.archlinux.org/packages/amdgpu-clocks-git/>)AUR

#####  图形界面工具

  * **TuxClocker** — Qt5 监控和超频工具。

     <https://github.com/Lurkki14/tuxclocker> || [tuxclocker](<https://aur.archlinux.org/packages/tuxclocker/>)AUR

  * **CoreCtrl** — 一个 GUI 超频工具，具有类似 WattMan 的 UI，支持每个应用程序配置文件。

     <https://gitlab.com/corectrl/corectrl> || [corectrl](<https://archlinux.org/packages/?name=corectrl>)包

  * **LACT** — 一个GTK工具，可显示信息和控制你的AMD GPU。

     <https://github.com/ilya-zlobintsev/LACT> || [lact](<https://aur.archlinux.org/packages/lact/>)AUR

####  开机自动修改

一种办法是使用system的单元，如果希望设置在开机时自动应用修改，可以参考[这个 Reddit 帖子](<https://www.reddit.com/r/Amd/comments/agwroj/how_to_overclock_your_amd_gpu_on_linux/>)来实现开机时自动配置和启用设定。 

另一种办法是使用udev规则，例如要设置为低性能等级来延长续航： 
    
    /etc/udev/rules.d/30-amdgpu-low-power.rules 
    
    SUBSYSTEM=="pci", DRIVER=="amdgpu", ATTR{power_dpm_force_performance_level}="low"
    
###  性能等级

AMDGPU 提供了不同的性能等级，可以使用power_dpm_force_performance_level 调节，有下列参数可供选择： 

  * **auto** : 驱动根据当前情况动态选择最佳电源配置。
  * **low** : 时钟频率强制设置为最低功耗状态。
  * **high** : 时钟频率强制设置为最高功耗状态。
  * **manual** : 用户可以为不同的时钟频率区间手动调整功耗状态（用于[#电源配置](<#%E7%94%B5%E6%BA%90%E9%85%8D%E7%BD%AE>)）。
  * **profile_standard** , **profile_min_sclk** , **profile_min_mclk** , **profile_peak** : 时钟频率和功耗门控被关闭，根据用户需求时钟频率可设置为不同配置。该模式推荐用于特定工作负载。

要让AMDGPU设备工作在一个低性能等级，可以执行下面的命令： 
    
    # echo "low" > /sys/class/drm/card0/device/power_dpm_force_performance_level
    
**注意：** 每次启动系统后应该重新设置性能等级，参见[#开机自动修改](<#%E5%BC%80%E6%9C%BA%E8%87%AA%E5%8A%A8%E4%BF%AE%E6%94%B9>)使修改自动应用。

###  电源配置

AMDGPU 通过电源配置提供多种优化，最常用的一种是 OpenCL 密集型应用程序的计算模式。下面的命令可以列出所有的可用电源配置： 
    
    cat /sys/class/drm/card0/device/pp_power_profile_mode
    
    NUM        MODE_NAME     SCLK_UP_HYST   SCLK_DOWN_HYST SCLK_ACTIVE_LEVEL     MCLK_UP_HYST   MCLK_DOWN_HYST MCLK_ACTIVE_LEVEL
      0   BOOTUP_DEFAULT:        -                -                -                -                -                -
      1   3D_FULL_SCREEN:        0              100               30                0              100               10
      2     POWER_SAVING:       10                0               30                -                -                -
      3            VIDEO:        -                -                -               10               16               31
      4               VR:        0               11               50                0              100               10
      5        COMPUTE *:        0                5               30               10               60               25
      6           CUSTOM:        -                -                -                -                -                -
    
**注意：** 命令参数路径中用 `card0` 标识机器中的特定 GPU，如果有多个 GPU，要确保找到正确的路径。

要使用特定的电源配置文件，首先应该启用对它们的手动控制： 
    
    # echo "manual" > /sys/class/drm/card0/device/power_dpm_force_performance_level
    
然后通过写入与其关联的 NUM 字段来选择电源配置文件，例如下面的命令可以启用计算运行（COMPUTE）： 
    
    # echo "5" > /sys/class/drm/card0/device/pp_power_profile_mode
    
**注意：** 电源配置改动要在每次启动时重新配置，参考 [#开机启动](<#%E5%BC%80%E6%9C%BA%E5%90%AF%E5%8A%A8>) 来自动化该过程

###  启用 GPU 显示缩放

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[xrandr](<../zh-cn/Xrandr.html> "Xrandr")。**

**附注：** 不特定于 AMDGPU。（在 [Talk:AMDGPU#将 "启用 GPU 显示缩放" 移动到 xrandr](</wzh/index.php?title=Talk:AMDGPU&action=edit&redlink=1> "Talk:AMDGPU（页面不存在）") 中讨论）

为了避免使用显示器内置的缩放器，而要使用 GPU 自己的缩放器，在不使用显示器的原始分辨率时，可以用下面的命令实现： 
    
    $ xrandr --output "<output>" --set "scaling mode" "<scaling mode>"
    
`"scaling mode"` 可以设置的值有: `None, Full, Center, Full aspect`

  * 要显示可用的输出和设置，执行：

    $ xrandr --prop
    
  * 要为每个有效显示输出都设置 `scaling mode = Full aspect`，使用下面的命令:

    $ for output in $(xrandr --prop | grep -E -o -i "^[A-Z\-]+-[0-9]+"); do xrandr --output "$output" --set "scaling mode" "Full aspect"; done
    
##  排除故障

###  模块参数

amdgpu模块含有一些使用掩码的配置参数(`modinfo amdgpu | grep mask`)，这些参数文档请参阅[内核源码](<https://raw.githubusercontent.com/torvalds/linux/master/drivers/gpu/drm/amd/include/amd_shared.h>)

###  Xorg 或应用程序无法启动

  * "(EE) AMDGPU(0): [DRI2] DRI2SwapBuffers: drawable has no back or front?" error after opening glxgears, can open Xorg server but OpenGL apps crash.
  * "(EE) AMDGPU(0): Given depth (32) is not supported by amdgpu driver" error, Xorg won't start.

在 Xorg 下将屏幕颜色深度设置为 16 或 32 会导致异常或崩溃。为避免这种情况，可以通过往配置的 _Screen_ 区块添加设置来使用标准的 24 位屏幕颜色深度： 
    
    /etc/X11/xorg.conf.d/10-screen.conf
    
    Section "Screen"
           Identifier     "Screen"
           DefaultDepth    24
           SubSection      "Display"
                   Depth   24
           EndSubSection
    EndSection
    
###  屏幕伪影和频率问题

由于 GPU 时钟速度的管理方式存在问题，[动态电源管理](<../zh-cn/ATI.html#Dynamic_power_management> "ATI")可能会在显示器运行高刷新率(120+hz)时导致屏幕伪影 [.org/show_bug.cgi?id=96868](<https://bugs.freedesktop>)[[1]](<https://bugs.freedesktop.org/show_bug.cgi?id=102646>)。 

一个规避的办法 [[2]](<https://bugs.freedesktop.org/show_bug.cgi?id=96868#c13>) 是手动将 `/sys/class/drm/card0/device/power_dpm_force_performance_level` 设置为 `high` 或 `low`

要使设置持久化生效，可以创建一个 udev 规则： 
    
    /etc/udev/rules.d/30-amdgpu-pm.rules
    
    KERNEL=="card0", SUBSYSTEM=="drm", DRIVERS=="amdgpu", ATTR{device/power_dpm_force_performance_level}="high"
    
执行下面的命令检查 KERNEL 参数名称： 
    
     $ find /sys/class/drm/ -regextype awk -regex '.+/card[0-9]+' -printf '%f\n'
    
另一个图形界面的解决方案 [[3]](<https://github.com/marazmista/radeon-profile>)是用 [radeon-profile-git](<https://aur.archlinux.org/packages/radeon-profile-git/>)AUR 和 [radeon-profile-daemon-git](<https://aur.archlinux.org/packages/radeon-profile-daemon-git/>)AUR 来管理 _power_dpm_ 。 

更换内核版本也可能解决这个问题，该问题看起来已在6.12.9版本修复。 

####  Chromium 伪影

如果在使用 [Chromium](<../zh-cn/Chromium.html> "Chromium") 时看到伪影，可以尝试强制使用基于 vulkan 的后端。在 `chrome://flags` 中 _启用_ `#ignore-gpu-blocklist` 和 `#enable-vulkan`。 

###  R9 390 系列性能不佳或不稳定

如果在使用 AMD R9 390 系列显卡时遇到问题 [[4]](<https://bugs.freedesktop.org/show_bug.cgi?id=91880>)，可以在[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")中设置`radeon.cik_support=0 radeon.si_support=0 amdgpu .cik_support=1 amdgpu.si_support=1 amdgpu.dpm=1 amdgpu.dc=1` 来强制使用 amdgpu 驱动模块而不是 radeon 驱动模块。 

如果还不起作用，请尝试通过在[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")中设置：`radeon.cik_support=0 radeon.si_support=0 amdgpu.cik_support=1 amdgpu.si_support=1` 来禁用动态电源管理（DPM）。 

###  因内核错误"[drm] IP block:gmc_v8_0 is hung!"画面冻结

如果在执行 GPU 密集型任务期间遇到冻结和内核崩溃，并出现内核错误"[drm] IP block:gmc_v8_0 is hung!" [[5]](<https://bugs.freedesktop.org/show_bug.cgi?id=102322>)时，一个规避的方法是在[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")中设置 `amdgpu.vm_update_mode=3` 来强制使用 CPU 完成 GPUVM 页面表更新。 这里列出了这个方法的缺点 [[6]](<https://bugs.freedesktop.org/show_bug.cgi?id=102322#c15>)。 

###  屏幕闪烁或出现白/灰屏

当改变分辨率或连接外接显示器时屏幕出现闪烁或白屏，在[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")中加入`amdgpu.sg_display=0`。 

###  在 Vega 显卡上玩游戏时系统冻结或崩溃

由于 GPU 核心频率的管理方式存在问题，使用显卡驱动的动态电源管理可能会导致系统在玩游戏时完全冻结。[[7]](<https://gitlab.freedesktop.org/drm/amd/-/issues/716>) 一个规避方法是禁用动态电源管理, 更多细节可以参考 [ATI#动态电源管理](<../zh-cn/ATI.html#%E5%8A%A8%E6%80%81%E7%94%B5%E6%BA%90%E7%AE%A1%E7%90%86> "ATI")。 

###  火狐浏览器 WebRenderer 损坏

当用户强制启用 [WebRenderer](<../zh-cn/Firefox/%E5%BE%AE%E8%B0%83.html#WebRender> "Firefox/Tweaks") 时，可能会出现伪影和其他异常（例如无法选择扩展选项）。解决方法是回退到 OpenGL 合成。 

###  两倍速或 _花栗鼠（chipmunk）_ 音频，或连接 4K@60Hz 设备时无音频

这有时是由 AMDGPU 设备和通过 HDMI 连接的 4K 显示器之间的通信问题引起的。一种可能的规避方法是通过显示器的内置设置启用 HDR 或“超高清深色”。在许多基于 Android 的电视上，这对应着将相关选项设置为“标准”（Standard）而不是“最佳”（Optimal）。 

###  独立显卡的电源管理/动态重新激活问题

如果遇到内核驱动已经加载，但游戏时独立显卡不可用或在使用时独立显卡被禁用（类似于 [[8]](<https://gitlab.freedesktop.org/drm/amd/-/issues/1820>)） 的问题，可以通过设置[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数") `amdgpu.runpm=0` 来防止独显在运行时动态断电。 

### kfd: amdgpu: TOPAZ not supported in kfd

在系统日志或内核消息密钥环中打印危急级别的错误消息 
    
    kfd: amdgpu: TOPAZ not supported in kfd
    
如果没有使用 [Radeon Open Compute](<../zh-cn/GPGPU.html#ROCm> "GPGPU") 的计划，可以安全的忽略这个问题。因为旧显卡不支持 TOPAZ。[[9]](<https://github.com/RadeonOpenCompute/ROCm/issues/1148#issuecomment-747849592>) [[10]](<https://www.reddit.com/r/linuxquestions/comments/yhbbiz/kfd_kfd_amdgpu_topaz_not_supported_in_kfd/>)

###  MCLK锁定在最大（1000MHz）或最小（96MHz）频率导致的高待机功耗或低游戏性能问题（6.4内核）

在高分辨率和刷新率的设置下，MCLK（vram，显存频率）可能会锁定在最高值（1000MHz）[[11]](<https://gitlab.freedesktop.org/drm/amd/-/issues/1403>) [[12]](<https://gitlab.freedesktop.org/drm/amd/-/issues/2646>) ，造成GPU待机功耗过高。使用Linux 6.4.x内核，MCLK锁定在最低频率（96MHz）影响游戏性能[[13]](<https://gitlab.freedesktop.org/drm/amd/-/issues/2657>) [[14]](<https://gitlab.freedesktop.org/drm/amd/-/issues/2611>)。 

这可能是因为显示器没有为受影响的分辨率和刷新率设置使用一个低V-Blank值的协调视频时序（Coordinated Video Timings， CVT），参考[这篇内容](<https://gist.github.com/Rend0e/3bddac4285dc1f4fbe303f326f36f6cc>)来解决。 

###  未能挂起（suspend）到内存

当系统进入S3状态后，`amdgpu`内核模块会尝试缓存显存数据到内存中，以避免显存不能充分刷新，显存中的数据老化导致数据丢失。 

如果你使用了大量显存而空闲内存不足，[这会导致挂起失败](<https://gitlab.freedesktop.org/drm/amd/-/issues/2125>)。因为IO子系统可能会在此之前挂起，不论是否有足够的swap空间该问题都可能发生。 

你可能会看到类似的消息： 
    
    kernel: systemd-sleep: page allocation failure: order:0, mode:0x100c02(GFP_NOIO|__GFP_HIGHMEM|__GFP_HARDWALL), nodemask=(null),cpuset=/,mems_allowed=0
    kernel: Call Trace:
    kernel:  <TASK>
    kernel:  dump_stack_lvl+0x47/0x60
    kernel:  warn_alloc+0x165/0x1e0
    kernel:  __alloc_pages_slowpath.constprop.0+0xd7d/0xde0
    kernel:  __alloc_pages+0x32d/0x350
    kernel:  ttm_pool_alloc+0x19f/0x600 [ttm 0bd92a9d9dccc3a4f19554535860aaeda76eb4f4]
    
通过一个[用户空间服务](<https://git.dolansoft.org/lorenz/memreserver>)可解决该问题，该服务能够在系统挂起前将足够的内存交换到SWAP，确保能够申请到足够的内存用以显存缓存。 

###  关机和挂起（suspend）失败

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 缺少内核信息和bug报告 (在 [Talk:AMDGPU](<../zh-cn/Talk:AMDGPU.html>) 中讨论)

_hid_sensor_*_3d_ 这类内核模块能够造成系统在启动、关机和挂起时死锁。进程列表里将会显示了多个`udev-worker`实例，导致系统睡眠时冻结。 

你会看到类似消息： 
    
    kernel: PM: suspend entry (deep)
    kernel: Filesystems sync: 0.002 seconds
    kernel: Freezing user space processes
    kernel: Freezing user space processes failed after 20.004 seconds (1 tasks refusing to freeze, wq_busy=0):
    kernel: task:(udev-worker)   state:D stack:0     pid:479   tgid:479   ppid:422    flags:0x00004006
    kernel: Call Trace:
    kernel:  <TASK>
    kernel:  __schedule+0x3db/0x1520
    kernel:  ? srso_alias_return_thunk+0x5/0xfbef5
    kernel:  ? __wake_up_common+0x78/0xa0
    kernel:  ? srso_alias_return_thunk+0x5/0xfbef5
    
要解决该问题，将有问题的模块添加到黑名单中，创建配置文件如`/etc/modprobe.d/blacklist-hid_sensors.conf`： 
    
    blacklist hid_sensor_accel_3d
    blacklist hid_sensor_gyro_3d
    blacklist hid_sensor_magn_3d
    
##  参考资料

  * [Gentoo:AMDGPU](<https://wiki.gentoo.org/wiki/AMDGPU> "gentoo:AMDGPU")
