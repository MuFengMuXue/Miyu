**翻译状态：**

  * 本文（或部分内容）译自 [Gamescope](<https://wiki.archlinux.org/title/Gamescope> "arch:Gamescope")，最近一次同步于 2025-1-26，若英文版本有所[更改](<https://wiki.archlinux.org/title/Gamescope?diff=0&oldid=822154>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Gamescope_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Steam](<../zh-cn/Steam.html> "Steam")
  * [Gaming](<../zh-cn/%E6%B8%B8%E6%88%8F.html> "Gaming")

[Gamescope](<https://github.com/ValveSoftware/gamescope>) 是来自 Valve 并用于 [Steam Deck](</wzh/index.php?title=Steam_Deck&action=edit&redlink=1> "Steam Deck（页面不存在）") 的[微混成器](<../zh-cn/Wayland.html#Compositors> "Wayland"). 其目标是提供一种针对游戏量身定制的独立合成器，并支持许多以游戏为中心的功能，例如: 

  * 分辨率伪装.
  * 使用 AMD FidelityFX™ Super Resolution 或 NVIDIA Image Scaling 进行图像上采样.
  * 限制帧率.

作为一个微混成器，它被设计为在现有桌面环境之上作为嵌套会话运行，尽管也可以将其用作嵌入式混成器。 

##  安装

Gamescope 可以通过 [gamescope](<https://archlinux.org/packages/?name=gamescope>)包包或[gamescope-git](<https://aur.archlinux.org/packages/gamescope-git/>)AUR包[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")。另外，还有[gamescope-plus](<https://aur.archlinux.org/packages/gamescope-plus/>)AUR包提供了包含不在主线版本中的一些额外补丁的版本。 

###  安装要求

  * AMD: Mesa 20.3 或更高
  * Intel: Mesa 21.2 或更高
  * NVIDIA: 专有驱动 515.43.04 或更高，以及 `nvidia_drm.modeset=1` [内核参数](<../zh-cn/Kernel_parameter.html> "Kernel parameter")

##  使用

Gamescope 有很多选项。可以通过在终端执行 `gamescope --help` 命令获取完整选项列表。 

###  从显示管理器运行

参见[steam#无窗口管理器的大屏幕模式](<../zh-cn/Steam.html#%E6%97%A0%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8%E7%9A%84%E5%A4%A7%E5%B1%8F%E5%B9%95%E6%A8%A1%E5%BC%8F> "Steam")

###  从桌面环境运行

下面的命令会用 Gamescope 运行 supertuxkart，强制使用 1920x1080 60 FPS分辨率。 
    
    $ gamescope -W 1920 -H 1080 -r 60 -- supertuxkart
    
###  运行 Steam 上的游戏

您可以使用 Gamescope 从 Steam 运行游戏，只需将以下内容添加到游戏启动选项即可： 
    
    $ gamescope -e -- steam
    
**注意：** 标志 `-e` 告诉 Gamescope 启用 Steam Integration.

你也可以通过添加以下游戏启动参数，用 Gamescope 运行 Steam 上的游戏 
    
    gamescope -- %command%
    
**注意：** 从Steam启动时，仍然需要设置分辨率、FPS等标志，否则Gamescope将以不正确的分辨率启动。例如，您可以通过与从终端相同的方式执行此操作
    
    gamescope -W 1920 -H 1080 -r 60 -- %command%
    
###  运行Wine

当使用 Gamescope 通过 [Wine](<../zh-cn/Wine.html> "Wine") 运行程序时，简单地用 _wine_ 加上可执行程序名称即可。 
    
    $ gamescope -W 1920 -H 1080 -r 60 -- wine supertuxkart
    
几乎全部流行的 Wine 管理器都支持 Gamescope，例如 [Lutris](</wzh/index.php?title=Lutris&action=edit&redlink=1> "Lutris（页面不存在）")，[Bottles](<../zh-cn/Bottles.html> "Bottles")，和 [PlayOnLinux](</wzh/index.php?title=PlayOnLinux&action=edit&redlink=1> "PlayOnLinux（页面不存在）")。使用它们就像安装所需的 Gamescope 软件包并检查“使用Gamescope”（或类似）选项一样简单。 

**注意：** Wine 管理器还倾向于使用GUI界面来配置基本的Gamescope选项，这使它们成为使用Gamescope的最简单方法。

###  运行 Flatpak

您也可以将 Gamescope 与 [Flatpak](<../zh-cn/Flatpak.html> "Flatpak") 或 [Steam](<../zh-cn/Steam.html> "Steam") 提供的 Wine 管理器一起使用，方法与安装软件包相同。但是，它要求您首先使用以下命令从 Flathub 安装 Gamescope： 
    
    $ flatpak install gamescope
    
###  上采样

可以用 `-F fsr` 和 `-F nis` 标志对游戏分别使用 AMD FidelityFX™ Super Resolution 1.0 (FSR) 或 NVIDIA Image Scaling v1.0.3 (NIS) 进行上采样。你也可以用 `-S integer` 进行整数上采样，或者用 `-S stretch` 拉伸画面. 

使用 FSR 将 720p 游戏上采样至 1440p ： 
    
    $ gamescope -h 720 -H 1440 -F fsr -- supertuxkart
    
使用 NIS 在内部以 1080p 分辨率运行游戏但是以 4K 显示: 
    
    $ gamescope -w 1920 -h 1080 -W 3840 -H 2160 -F nis -- supertuxkart
    
低分辨率的游戏通常默认在全屏上使用线性过滤，有时会被拉伸。这在经典的JRPG中尤为明显。要获得像素化外观并保持纵横比： 
    
    $ gamescope -F nearest -S fit -- tecnoballz
    
在游戏运行时调整使用的滤镜： 

  * `Super+n` 切换最近邻采样。
  * `Super+u` 切换FSR上采样。
  * `Super+y` 切换NIS上采样。
  * `Super+o` FSR锐度减1。
  * `Super+i` FSR锐度加1。

###  HDR 支持

运行游戏时，Gamescope 是 HDR10 的必要条件 ，要使用此功能， 请给 Gamescope 启动参数加上 `--hdr-enabled` 标志. 

**注意：** Linux上的HDR支持仍处于起步阶段，有许多需要注意的地方。有关详细信息，请参阅[HDR monitor support](</wzh/index.php?title=HDR_monitor_support&action=edit&redlink=1> "HDR monitor support（页面不存在）")。

### Mangoapp

[不支持](<https://github.com/flightlessmango/MangoHud?tab=readme-ov-file#gamescope>)将传统 [MangoHud](<../zh-cn/MangoHud.html> "MangoHud") 和 Gamescope 结合使用。相反，应当使用 gamescope 的 `--mangoapp` 标志。这允许 MangoHud 在 gamescope ，而不是在底层应用程序上运行。某些 MangoHud 配置，如显示 FSR 或 HDR 状态，需要使用带有 gamescope 的 mangoapp 才能工作。某些 MangoHud 配置，比如显示 FSR 或 HDR 状态，需要使用 gamescope 才能工作。 

###  可变刷新率

如果显示器支持它，通过传递 `--adaptive-sync` 标志以启用可变刷新率。 

###  Wayland 支持

Gamescope 默认不支持 [Wayland](<../zh-cn/Wayland.html> "Wayland") 客户端。要启用对 Wayland 客户端的支持，请给 Gamescope 启动参数加上 `--expose-wayland` 标志。 

###  SDR 增益范围

Since [SteamOS 3.5.5](<https://store.steampowered.com/news/app/1675200/view/5484882897552407488>), Valve has changed the default color rendering for the Steam Deck LCD. The effect is achieved through Gamescope by changing the "wideness" of the gamut for SDR content, which can result in a warmer and more vibrant color appearance depending on the adjustment. 

In a Steam game's launch options, simply add `--sdr-gamut-wideness` followed by a value that's equal or between 0-1: 
    
    gamescope --sdr-gamut-wideness 1 -- %command%
    
##  常见问题

###  光标表现不正确

如果光标没有被应用程序捕捉到，例如限制相机的移动或者没有正确地从菜单中消失，那么使用 `--force-grab-cursor` 标志。一些 proton 或 wine 游戏需要这种变通方法。 

###  切换至全屏模式后性能降低

当使用Gamescopes全屏热键 `Meta+f` 时，这是一个已知的错误，如果你遇到这个问题，可以在启动游戏时使用全屏标志 `-f` 来解决。 

###  设置 Gamescopes 优先级

另一个已知的低性能或卡顿的原因是没有正确设置Gamescope的优先级。如果你在Gamescope运行时在终端中看到这样的错误，说明你遇到了现在所说的这种情况： 
    
    No CAP_SYS_NICE, falling back to regular-priority compute and threads.
    Performance will be affected.

用下面的命令可以修复： 
    
    # setcap 'CAP_SYS_NICE=eip' $(which gamescope)
    
**警告：** 使用此命令将导致忽略一些 Vulkan 环境变量： 例如，如果通过设置 `MESA_VK_DEVICE_SELECT` 为 Gamescope 指定要使用的 GPU。看 [这里](<https://github.com/ValveSoftware/gamescope/issues/107>)。您可以使用[ananicy-git](<https://aur.archlinux.org/packages/ananicy-git/>)AUR或类似的方法来绕过这个限制。

###  在 NVIDIA 环境运行 Flatpak 应用没有窗口

这是因为 Flatpak Gamescope 访问 NVIDIA DRM's GBM 后端失败. 这可以简单地通过下面的命令设置一个环境变量解决： 
    
    $ flatpak override --env=GBM_BACKENDS_PATH=/usr/lib/x86_64-linux-gnu/GL/nvidia-_XXX_ -_YY_ -_ZZ_ /extra/gbm _packageid_
    
其中 `packageid` 是 Gamescope 或您要使用Gamescope的应用程序的Flatpak包标识符，如Bottles。将 `nvidia-_XXX_ -_YY_ -_ZZ_` 替换为当前安装的nvidia驱动程序版本；在Flatpak内部，可以使用以下命令进行查询： 
    
    $ flatpak run --command=ls _packageid_ /usr/lib/x86_64-linux-gnu/GL
    
其中 `_packageid_` 是任何一个 Flatpak 包标识符，请注意该目录只存在于 Flatpak 内。 

**注意：**

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** This step can probably be automated by a [pacman hook](<../zh-cn/Pacman_hook.html> "Pacman hook"). (在 [Talk:Gamescope](<../zh-cn/Talk:Gamescope.html>) 中讨论)

The command **must** be reran, and modified accordingly, on every driver update. 

###  使用 Intel 显卡出现图像损坏

If gamescope outputs corrupted image colors on Intel graphics disabling lossless color compression can be a work-around at the cost of increased memory bandwidth utilization. [[1]](<https://github.com/ValveSoftware/gamescope/issues/356>) To disable it pass `INTEL_DEBUG=noccs` [environment variable](<../zh-cn/Environment_variable.html> "Environment variable"). 

###  启用 HDR 时 VRR 卡顿

If VRR and HDR work independently, but the framerate is unstable when they're both enabled, then you may be hitting issues with long HDR compositing times. See <https://github.com/ValveSoftware/gamescope/issues/1006>. This only applies to using Gamescope in embedded mode, and not when using gamescope within an existing wayland or X session. 

使用AMD显卡时可以使用实验性的 AMD 颜色管理解决这个问题，这会使用硬件 planes 完成最终图像的合成。使用以下两个步骤之一： 

###  Steam Deck 内核

  * The Steam Deck Linux kernel [linux-neptune-65](<https://aur.archlinux.org/packages/linux-neptune-65/>)AUR or a kernel built with the [Steam Deck color management patch ](<https://gitlab.com/evlaV/linux-integration/-/commit/90e3a855c922d0b8c4b18c886c5cf73223d69475.patch>)
  * [gamescope](<https://archlinux.org/packages/?name=gamescope>)包 or [gamescope-git](<https://aur.archlinux.org/packages/gamescope-git/>)AUR

####  启用实验性AMD颜色管理的 Linux 内核

  * Linux 6.8 及以上，编译时 `KCFLAGS` 包含 `-DAMD_PRIVATE_COLOR`，例如 [linux-amd-color](<https://aur.archlinux.org/packages/linux-amd-color/>)AUR
  * gamescope [patched to work with upstream kernel](<https://github.com/ValveSoftware/gamescope/pull/1149>), available in AUR as [gamescope-amd-color](<https://aur.archlinux.org/packages/gamescope-amd-color/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]

###  Wayland下在较老的AMD显卡上崩溃

Gamescope 3.14.3 引入了[一个Wayland后端](<https://github.com/ValveSoftware/gamescope/commit/ce1156af053239e662aa021dbfc6a64cb770f64a>)，以提升Wayland下的性能。虽然，尽管如此，它目前无法在较旧的AMD GPU上运行。追踪上游问题[#1218](<https://github.com/ValveSoftware/gamescope/issues/1218>)。 

Gamescope在启动时崩溃，例如这样： 
    
    gamescope: types/wlr_linux_dmabuf_v1.c:526: feedback_compile: Assertion `table_len > 0' failed.
    
您可以通过强制回退旧的 SDL2 后端，添加 `--backend` 标志来解决这个问题： 
    
    $ gamescope --backend sdl  -- game
    
###  Swapchain 错误

Swapchain错误的一个常见原因是不正确地尝试使用 mangohud 而不是 mangoapp。请参阅[上文](<#%E4%BD%BF%E7%94%A8>)。 

###  从 Steam 启动游戏，在大约24分钟后卡顿

如果从steam启动gamescope后，您在大约24分钟后遇到严重的卡顿，那么您可以添加Steam overlay 的 `-e` 标志 或用不同的值覆盖环境变量 `LD_PRELOAD` 来解决这个问题。例如： 
    
    $ LD_PRELOAD="" gamescope -- %command%
    
参见<https://github.com/ValveSoftware/gamescope/issues/163>

###  高回报率的鼠标导致卡顿

在游戏窗口中移动一个高回报率(observed with 4000Hz)的鼠标时，可能导致卡顿或暂时冻结 [[2]](<https://github.com/ValveSoftware/gamescope/issues/1279>)。设置一个更低的比如 1000Hz 的回报率应该可以绕过这个问题。 

##  另请参阅

  * [Gamescope Github Page](<https://github.com/ValveSoftware/gamescope>)
  * [Gamescope at Steamtinkerlaunch Github Wiki](<https://github.com/sonic2kk/steamtinkerlaunch/wiki/GameScope>)
