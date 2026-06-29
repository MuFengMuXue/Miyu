**翻译状态：**

  * 本文（或部分内容）译自 [Intel graphics](<https://wiki.archlinux.org/title/Intel_graphics> "arch:Intel graphics")，最近一次同步于 2024-05-13，若英文版本有所[更改](<https://wiki.archlinux.org/title/Intel_graphics?diff=0&oldid=808039>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Intel_graphics_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Intel GMA 3600](<../zh-cn/Intel_GMA_3600.html> "Intel GMA 3600")
  * [Xorg](<../zh-cn/Xorg.html> "Xorg")
  * [Kernel mode setting](<../zh-cn/Kernel_mode_setting.html> "Kernel mode setting")
  * [Xrandr](<../zh-cn/Xrandr.html> "Xrandr")
  * [Hybrid graphics](<../zh-cn/Hybrid_graphics.html> "Hybrid graphics")
  * [Vulkan](<../zh-cn/Vulkan.html> "Vulkan")
  * [GPGPU](<../zh-cn/GPGPU.html> "GPGPU")

由于 Intel 提供并维护开源驱动程序，因此 Intel 显卡基本上是即插即用的。 

有关 Intel GPU 型号以及相应芯片组和 CPU 的全面列表，请参阅 [Wikipedia:list of Intel graphics processing units](<https://en.wikipedia.org/wiki/list_of_Intel_graphics_processing_units> "wikipedia:list of Intel graphics processing units") 和 [Gentoo:Intel#Feature support](<https://wiki.gentoo.org/wiki/Intel#Feature_support> "gentoo:Intel")。 

**注意：**

  * 开源驱动不支持基于 PowerVR 架构的图形卡 (比如[GMA 3600](<../zh-cn/Intel_GMA_3600.html> "Intel GMA 3600") 系列)
  * Intel 第 _N_ 代硬件不代表 CPU 的代数，它表示不同于 CPU 代数的 [GPU 的代数](<https://en.wikipedia.org/wiki/list_of_Intel_graphics_processing_units> "wikipedia:list of Intel graphics processing units")
  * 参见 [Xorg#驱动安装](<../zh-cn/Xorg.html#%E9%A9%B1%E5%8A%A8%E5%AE%89%E8%A3%85> "Xorg") 来识别你的显卡

##  安装

  * [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")以下任一软件包，它提供用于 3D 加速的 [DRI](<https://en.wikipedia.org/wiki/Direct_Rendering_Infrastructure> "wikipedia:Direct Rendering Infrastructure") 驱动程序。 
    * [mesa](<https://archlinux.org/packages/?name=mesa>)包 是最新的 [Mesa](<../zh-cn/OpenGL.html> "OpenGL") 软件包，其中包括用于 Intel 第 3 代及更高版本硬件的现代 Gallium3D 驱动程序。这是推荐选择。
    * [mesa-amber](<https://archlinux.org/packages/?name=mesa-amber>)包 是旧版 Mesa 软件包，包括用于第 2 代至第 11 代硬件的经典（非 Gallium3D）驱动程序。此驱动程序对于第 7 代和较旧的硬件具有更好的性能和稳定性，但是不再维护。

  * 为支持 32 位程序，请同时从 [multilib](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "Multilib") 仓库中安装 [lib32-mesa](<https://archlinux.org/packages/?name=lib32-mesa>)包 或 [lib32-mesa-amber](<https://archlinux.org/packages/?name=lib32-mesa-amber>)包 软件包。

  * 对于 [DDX](<https://en.wikipedia.org/wiki/X.Org_Server#DDX> "wikipedia:X.Org Server") 驱动支持（可提供对 [Xorg](<../zh-cn/Xorg.html> "Xorg") 的 2D 加速），安装以下任一软件包： 
    * 包含在 [xorg-server](<https://archlinux.org/packages/?name=xorg-server>)包 软件包内的 _modesetting_ 驱动是对于第 4 代及以上硬件的推荐选择。它通过 _glamor_ 使用 DRI 来实现加速。
    * [xf86-video-intel](<https://archlinux.org/packages/?name=xf86-video-intel>)包 软件包为第 2 代至第 9 代硬件提供了旧的 Intel DDX 驱动。通常不建议使用此软件包，请参见下面的注释。

  * 为支持 [Vulkan](<../zh-cn/Vulkan.html> "Vulkan") （Haswell 及更新架构，对于老更老架构的支持是[不完整或缺失的](<https://gitlab.freedesktop.org/mesa/mesa/-/issues/8249#note_1758622>)），安装 [vulkan-intel](<https://archlinux.org/packages/?name=vulkan-intel>)包 软件包。对于 32 位的 [Vulkan](<../zh-cn/Vulkan.html> "Vulkan") 支持，安装 [lib32-vulkan-intel](<https://archlinux.org/packages/?name=lib32-vulkan-intel>)包 软件包。

另请参见[硬件视频加速](<../zh-cn/%E7%A1%AC%E4%BB%B6%E8%A7%86%E9%A2%91%E5%8A%A0%E9%80%9F.html> "硬件视频加速"). 

**注意：**

  * 有的文档 ([Debian & Ubuntu](<https://www.phoronix.com/scan.php?page=news_item&px=Ubuntu-Debian-Abandon-Intel-DDX>), [Fedora](<https://www.phoronix.com/scan.php?page=news_item&px=Fedora-Xorg-Intel-DDX-Switch>), [KDE](<https://community.kde.org/Plasma/5.9_Errata#Intel_GPUs>)) 推荐不安装 [xf86-video-intel](<https://archlinux.org/packages/?name=xf86-video-intel>)包 驱动程序，而是回落到给第四代及更新 GPU (2006年以来的GMA 3000及以上显卡) 使用的 modesetting 驱动程序。请参考 [[1]](<https://web.archive.org/web/20160714232204/https://www.reddit.com/r/archlinux/comments/4cojj9/it_is_probably_time_to_ditch_xf86videointel/>)、[[2]](<https://www.phoronix.com/scan.php?page=article&item=intel-modesetting-2017&num=1>), [Xorg#安装](<../zh-cn/Xorg.html#%E5%AE%89%E8%A3%85> "Xorg") 和 [modesetting(4)](<https://man.archlinux.org/man/modesetting.4>). 然而，modesetting 驱动程序可能导致比如 [XFCE 上的屏幕撕裂和鼠标抖动](<https://gitlab.freedesktop.org/xorg/xserver/-/issues/1364>)、[切换Chromium中虚拟的桌面产生伪影](<https://bugs.chromium.org/p/chromium/issues/detail?id=370022>) 和[mpv中的vsync抖动/视频抖动](<https://gitlab.freedesktop.org/xorg/xserver/-/issues/928>) 等问题
  * [xf86-video-intel](<https://archlinux.org/packages/?name=xf86-video-intel>)包 软件包未正确支持第 11 代及更新硬件，会导致硬件加速的缺失和可能会导致 Plasma Desktop 几乎不可用的渲染问题。参见 [[3]](<https://gitlab.freedesktop.org/xorg/driver/xf86-video-intel/-/commit/7181c5a41c3f00eaf996caa156523c708a18081e>)
  * 有多起报告（参见 [[4]](<https://bbs.archlinux.org/viewtopic.php?id=263323>) [[5]](<https://github.com/qutebrowser/qutebrowser/issues/4641>)）称当安装有 [xf86-video-intel](<https://archlinux.org/packages/?name=xf86-video-intel>)包 软件包时，整个图形栈会卡死，甚至切换至不同的虚拟控制台（通过按下 `Ctrl+Alt+F _n_`）都无法解决问题，只有通过使用 [SysRq](<../zh-cn/%E5%BF%AB%E6%8D%B7%E9%94%AE.html#%E5%86%85%E6%A0%B8%EF%BC%88SysRq%EF%BC%89> "快捷键") 杀死用户进程可以解决问题

##  加载

Intel 内核模块应会在系统引导时自动加载。 

如果它没有自动加载，请尝试： 

  * 由于 Intel 需要内核模式设置，确保您**没有** 在[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")中添加 `nomodeset`
  * 请同时确认您没有在 `/etc/modprobe.d/` 或 `/usr/lib/modprobe.d/` 中把 Intel 列入 modprobe 的黑名单导致禁用了 Intel。

###  启用 KMS 早启动

`i915` 驱动支持[内核级显示模式设置](<../zh-cn/Kernel_mode_setting.html> "Kernel mode setting") (KMS)，并且从 [mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio") v32 开始启用，因为 `kms` 钩子被默认包含。对于其他配置方式，请参考 [Kernel_mode_setting#KMS_早启动](<../zh-cn/Kernel_mode_setting.html#Early_KMS_start> "Kernel mode setting")获得有关如何在启动过程中第一时间启用KMS的说明。 

###  启用 GuC / HuC 固件加载

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 尽管 Intel 的文档没有说，但是 Tiger Lake 和 Rocket Lake GPU 可能实际上支持 `enable_guc=3`, 并且默认设置了 `enable_guc=1`.（在 [Talk:Intel graphics#TGL/RKL GuC Submission](</wzh/index.php?title=Talk:Intel_graphics&action=edit&redlink=1> "Talk:Intel graphics（页面不存在）") 中讨论）

从第 9 代硬件 (Skylake 及以后的架构) 开始, Intel GPU 都包含了一个用于提供以下功能的图形微控制器 “ _Graphics micro (μ) Controller_ ” (GuC) [[6]](<https://01.org/linuxgraphics/downloads/firmware>): 

  * 安装 [intel-media-driver](<https://archlinux.org/packages/?name=intel-media-driver>)包 软件包来启用[硬件视频加速](<../zh-cn/Hardware_video_acceleration.html> "Hardware video acceleration")后，能够把一些多媒体解码功能从 CPU 分载（offload）到 _HEVC/H.265 微控制器 （micro (µ) Controller）_ (HuC) 上。该功能于第 9 代推出。
  * 使用 GuC 进行调度、上下文提交（context submission）和电源管理。该功能通过第 12 代硬件于 Alder Lake-P（移动端）推出。

为了使用这些功能，您必须加载 GuC 固件。对于 HuC 支持，一些视频特性(如 SKL 低功耗编码模式下的 CBR 速率控制)也需要加载 HuC 固件才能实现。 [[7]](<https://github.com/intel/media-driver#known-issues-and-limitations>) GuC 和 HuC 的固件文件都包含在 [linux-firmware](<https://archlinux.org/packages/?name=linux-firmware>)包 软件包中。 

GuC 功能由 `i915.enable_guc` [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")控制，用法如下： 

enable_guc 的值 | GuC Submission | HuC Firmware Loading | 作为平台默认值 | 支持的平台   
---|---|---|---|---  
0 | 否 | 否 | Tiger Lake, Rocket Lake, 和 Pre-Gen12 [[8]](<https://github.com/torvalds/linux/blob/b3454ce0b2c8a56e760e6baa88ed10278585072b/drivers/gpu/drm/i915/gt/uc/intel_uc.c#L26-L36>) | All   
1 | 是 | 否 | – | Alder Lake-P (Mobile) 及更新   
2 | 否 | 是 | Alder Lake-S (Desktop) [[9]](<https://github.com/torvalds/linux/blob/b3454ce0b2c8a56e760e6baa88ed10278585072b/drivers/gpu/drm/i915/gt/uc/intel_uc.c#L38-L42>) [[10]](<https://lore.kernel.org/all/87ee6wit2r.fsf@intel.com/T/>) | Gen9 及更新   
3 | 是 | 是 | Alder Lake-P (Mobile) 及更新 | 第 9.5 代或更新（某些程度上更好）   
  
如果 GuC submission 或者 HuC 固件加载并未在您的 GPU 上默认启用，您可以手动启用它。 

**警告：**[即使您的显卡不支持相关功能](<https://bugs.freedesktop.org/show_bug.cgi?id=111918>)，手动启用 GuC/HuC 固件加载也可能会污染内核。此外，启用GuC/HuC固件加载可能会导致某些系统出现问题；如果您遇到冻结（例如，从休眠恢复后），请禁用它。

首先确保您已经[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")了 [linux-firmware](<https://archlinux.org/packages/?name=linux-firmware>)包 软件包。 

配置 `i915.enable_guc` [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")，比如： 
    
    /etc/modprobe.d/i915.conf
    
    options i915 enable_guc=2

然后[重建 initramfs](<../zh-cn/Mkinitcpio.html#%E6%89%8B%E5%8A%A8%E7%94%9F%E6%88%90> "Mkinitcpio")，在下一次启动时您可以通过 [dmesg](<../zh-cn/%E6%A0%B8%E5%BF%83%E5%B7%A5%E5%85%B7.html#%E5%9F%BA%E7%A1%80> "Dmesg") 命令来确认 GuC 和 HuC 都已被启用。 
    
    # dmesg
    
    [30130.586970] i915 0000:00:02.0: [drm] GuC firmware i915/icl_guc_33.0.0.bin version 33.0 submission:disabled
    [30130.586973] i915 0000:00:02.0: [drm] HuC firmware i915/icl_huc_9.0.0.bin version 9.0 authenticated:yes

如果您的显卡不支持它们，你会看到： 
    
    # dmesg
    
    [    0.571339] i915 0000:00:02.0: [drm] Incompatible option enable_guc=2 - GuC is not supported!
    [    0.571340] i915 0000:00:02.0: [drm] Incompatible option enable_guc=2 - HuC is not supported!

或者，使用以下方法进行检查： 
    
    # cat /sys/kernel/debug/dri/0/gt/uc/guc_info
    # cat /sys/kernel/debug/dri/0/gt/uc/huc_info
    
**注意：** 从 Linux 4.20.11 起，当 GuC/HuC 被启用时，不支持通过设置 `enable_gvt=1` 来使用 [GVT-g 图形虚拟化](<../zh-cn/Intel_GVT-g.html> "Intel GVT-g") 功能。i915模块将无法初始化，如系统日志所示： 
    
    # journalctl
    
    ... kernel: [drm:intel_gvt_init [i915]] *ERROR* i915 GVT-g loading failed due to Graphics virtualization is not yet supported with GuC submission
    ... kernel: i915 0000:00:02.0: [drm:i915_driver_load [i915]] Device initialization failed (-5)
    ... kernel: i915: probe of 0000:00:02.0 failed with error -5
    ... kernel: snd_hda_intel 0000:00:1f.3: failed to add i915 component master (-19)
    
请注意相关警告并非致命，正如[[11]](<https://github.com/intel/gvt-linux/issues/77#issuecomment-707541069>) 中解释的那样： 
    
    # journalctl -b 
    
    ... kernel: i915 0000:00:02.0: Direct firmware load for i915/gvt/vid_0x8086_did_0x5916_rid_0x02.golden_hw_state failed with error -2
    
##  Xorg 配置

通常不需要为了运行 [Xorg](<../zh-cn/Xorg.html> "Xorg") 去配置任何东西。 

但是如果需要使用一些驱动选项或是 [Xorg](<../zh-cn/Xorg.html> "Xorg") 未正常启动，您可以创建一个 Xorg 配置文件。 

###  使用 modesetting 驱动

如果您已经安装了 [xf86-video-intel](<https://archlinux.org/packages/?name=xf86-video-intel>)包 软件包但是想要显式加载 modesetting 驱动而不是让 DDX 驱动有着更高的优先级，比如试着去比较它们： 
    
    /etc/X11/xorg.conf.d/20-intel.conf
    
    Section "Device"
      Identifier "Intel Graphics"
      Driver "modesetting"
    EndSection
    
###  使用 Intel 驱动

**注意：** 以下操作需要安装 [xf86-video-intel](<https://archlinux.org/packages/?name=xf86-video-intel>)包 软件包。

创建一个与下述类似的 Xorg 配置文件： 
    
    /etc/X11/xorg.conf.d/20-intel.conf
    
    Section "Device"
      Identifier "Intel Graphics"
      Driver "intel"
    EndSection
    
您可以在 `Driver "intel"` 下方开新行添加额外的选项。请参考 [intel(4)](<https://man.archlinux.org/man/intel.4>) 手册页以获得完整的选项列表。 

**注意：** 您可能需要添加不止一段 `device` 配置，本文将在需要的地方指出。

#### AccelMethod

创建配置文件时，您可能需要指定 `Option "AccelMethod"` 。传统的选项包括 `UXA`, `SNA` (默认) 和 `BLT`. 

如果您在使用默认选项 `SNA` 时遇到问题 (比如花屏、文字损坏等)，尝试改用`UXA` 。只需要在[配置文件](<../zh-cn/Intel_graphics.html#Xorg%E9%85%8D%E7%BD%AE> "Intel graphics")中添加如下一行即可： 
    
    Option      "AccelMethod"  "uxa"
    
另请参阅 [intel(4) § CONFIGURATION DETAILS](<https://man.archlinux.org/man/intel.4#CONFIGURATION_DETAILS>) 手册文件中的 AccelMethod 选项。 

####  对于较新的 GPU 使用 Intel DDX 驱动

从第 8 代 Intel GPU 开始（Broadwell），需要 Iris Mesa 驱动： 
    
    Option      "DRI"  "iris"
    
####  禁用 TearFree，TripleBuffer，SwapbuffersWait

如果你在使用组合器（在比如 GNOME，KDE Plasma，Xfce 等现代桌面环境中是默认的），那么 TearFree，TripleBuffer 和 SwapbuffersWait 通常可以禁用以提高性能和省电。 
    
    Option      "TearFree"        "false"
    Option      "TripleBuffer"    "false"
    Option      "SwapbuffersWait" "false"
    
##  基于内核模块参数的选项

`i915` 内核模块允许您通过[内核模块参数](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html#%E9%85%8D%E7%BD%AE%E6%A8%A1%E5%9D%97%E5%8F%82%E6%95%B0> "内核模块")来配置选项。其中一些选项会影响到省电。 

您可以使用以下命令生成所有选项的列表以及简短说明和默认值： 
    
    $ modinfo -p i915
    
若要检查当前启用了哪些选项，请运行 
    
    # systool -m i915 -av
    
您将注意到，许多选项默认为 -1，说明芯片的省电状态都为默认值。然而，您可以通过[修改内核模块参数](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html#%E9%85%8D%E7%BD%AE%E6%A8%A1%E5%9D%97%E5%8F%82%E6%95%B0> "内核模块")来配置更积极的省电策略。 

**注意：** Diverting from the defaults will mark the kernel as [tainted](<https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/commit/?id=fc9740cebc3ab7c65f3c5f6ce0caf3e4969013ca>) from Linux 3.18 onwards. This basically implies using other options than the per-chip defaults is considered experimental and not supported by the developers.

###  Framebuffer 压缩 (enable_fbc)

启用 Framebuffer 压缩 (FBC) 功能能够减少电源消耗，同时减少刷新屏幕所需的内存带宽。 

如果您的硬件支持，此功能将被自动启用。您可以通过该命令来检查是否启用： 
    
    $ modinfo i915 | grep enable_fbc
    
    parm:           enable_fbc:Enable frame buffer compression for power savings (default: -1 (use per-chip default)) (int)
    
如果 parm 被设为 `-1`，那您不需要做任何事。如果在其他情况下要强制启用 FBC，请在内核参数中添加 `i915.enable_fbc=1` 或在 `/etc/modprobe.d/i915.conf` 中进行如下配置： 
    
    /etc/modprobe.d/i915.conf
    
    options i915 enable_fbc=1

**注意：** 在 Sandy Bridge (第6代)之前的几代 Intel GPU 上，帧缓冲（Framebuffer）压缩可能不可靠或不可用。 这导致系统日志中可能会记录类似如下信息： 
    
    kernel: drm: not enough stolen space for compressed buffer, disabling.
    
在Sandy Bridge之前的CPU上启用帧缓冲区压缩会导致无休止的错误消息： 
    
    # dmesg
    
    [ 2360.475430] [drm] not enough stolen space for compressed buffer (need 4325376 bytes), disabling
    [ 2360.475437] [drm] hint: you may be able to increase stolen memory size in the BIOS to avoid this
    
解决方案是禁用帧缓冲压缩，这将增加些微功耗（约0.06W）。为了禁用它，请在内核参数中添加`i915.enable_fbc=0` 。 请[参阅此处](<https://web.archive.org/web/20200228230053/https://kernel.ubuntu.com/~cking/power-benchmarking/background-colour-and-framebuffer-compression/>) 了解更多关于禁用帧缓冲的影响。

### Fastboot

**注意：** Skylake 和更新的架构，会在默认情况下启用此参数[[12]](<https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=3d6535cbed4a4b029602ff83efb2adec7cb8d28b>)。以及 Bay- 和 Cherry-Trail (VLV/CHV)[[13]](<https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=7360c9f6b857e22a48e545f4e99c79630994e932>) 自 Linux 5.1 版本以来也会启用。[[14]](<https://kernelnewbies.org/Linux_5.1#Graphics>)

Intel Fastboot 的目标是在 [Xorg](<../zh-cn/Xorg.html> "Xorg") 启动之前将帧缓冲区保留为 BIOS 或[引导加载程序](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "Arch 的启动流程")设置的内容，以避免出现屏闪。[[15]](<https://lists.freedesktop.org/archives/intel-gfx/2012-May/017653.html>)[[16]](<https://www.phoronix.com/scan.php?page=news_item&px=MTEwNzc>)

要在未默认启用快速启动的平台上强制启用快速启动，请设置 `i915.fastboot=1` [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")，或在 `/etc/modprobe.d/i915.conf` 里作如下设置： 
    
    /etc/modprobe.d/i915.conf
    
    options i915 fastboot=1

###  Intel GVT-g 图形虚拟化支持

请参考 [Intel GVT-g](<../zh-cn/Intel_GVT-g.html> "Intel GVT-g") 以了解详细信息。 

###  启用性能支持

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** What does Mesa actually do using the performance counters? What's the effect of this? Some report drastic performance increases on Intel Tiger Lake, attributing it to a support for Dynamic Tuning [[17]](<https://www.reddit.com/r/linux/comments/u7zxa0/psa_for_intel_tiger_lake_dynamic_tuning_laptops/>). (在 [Talk:Intel 图形处理器#Potential performance gains via Observation Architecture](</wzh/index.php?title=Talk:Intel_%E5%9B%BE%E5%BD%A2%E5%A4%84%E7%90%86%E5%99%A8&action=edit&redlink=1> "Talk:Intel 图形处理器（页面不存在）") 中讨论)

从第六代处理器 (Sandy Bridge 及更新的架构) 开始，Intel GPU 提供性能计数器，用于向驱动程序提供内部性能数据。 驱动程序和硬件寄存器将此基础结构称为 _Observation Architecture_ (内部称为 "OA") [[18]](<https://www.phoronix.com/scan.php?page=news_item&px=Intel-HSW-Observation-Arch>)，但英特尔的文档一般普遍将此功能称为 提供 _可观测性能计数器（Observability Performance Counters）_[[19]](<https://01.org/sites/default/files/documentation/observability_performance_counters_haswell.pdf>) [[20]](<https://01.org/sites/default/files/documentation/intel-gfx-prm-osrc-skl-vol14-observability.pdf>). 

默认情况下，只有使用 [CAP_SYS_ADMIN](<https://lwn.net/Articles/486306/>)（相当于root）或 [CAP_PERFMON](<https://lwn.net/Articles/812719/>) [能力](<../zh-cn/Capabilities.html> "Capabilities")（Capabilities）运行的程序才能使用 OA​ [[21]](<https://github.com/torvalds/linux/blob/b14ffae378aa1db993e62b01392e70d1e585fb23/drivers/gpu/drm/i915/i915_perf.c#L267>) [[22]](<https://github.com/torvalds/linux/blob/b14ffae378aa1db993e62b01392e70d1e585fb23/drivers/gpu/drm/i915/i915_perf.c#L3481-L3484>)。 大多数应用程序将在没有这两种情况下运行，从而导致以下警告： 
    
    MESA-INTEL: warning: Performance support disabled, consider sysctl dev.i915.perf_stream_paranoid=0
    
若要在不使用能力(或 root)的情况下启用性能支持，请按 [sysctl](<../zh-cn/Sysctl.html> "Sysctl") 中的描述设置内核参数。 

**警告：**`perf_event_paranoid` 系列选项默认为限制访问，因为允许应用程序访问性能数据存在风险 [[23]](<https://docs.kernel.org/admin-guide/perf-security.html>)。话虽如此， `dev.i915.perf_stream_paranoid` 只会影响对 GPU 性能计数器的访问，这比访问 CPU 架构执行上下文寄存器之类的带来的风险要小。

##  技巧和窍门

###  设置缩放模式

这对于某些全屏应用程序很有用： 
    
    $ xrandr --output LVDS1 --set PANEL_FITTING _param_
    
其中 `_param_` 可以为： 

  * `center`: 分辨率将完全保持原设置，不会进行缩放
  * `full`: 缩放分辨率，以便使用整个屏幕
  * `full_aspect`: 将分辨率缩放到可能的最大值，但保持纵横比。

如果它不起作用，请尝试： 
    
    $ xrandr --output LVDS1 --set "scaling mode" _param_
    
其中 `_param_` 可以为 `"Full"`、 `"Center"` 或 `"Full aspect"`。 

**注意：** 此选项目前不适用于外接显示器 (比如 VGA, DVI, HDMI, DP). [[24]](<https://bugs.freedesktop.org/show_bug.cgi?id=90989>)

###  GMA 4500上的硬件加速 H.264 解码

对于某些 GMA 4500 系列的 GPU，[libva-intel-driver](<https://archlinux.org/packages/?name=libva-intel-driver>)包 软件包只提供对 MPEG-2 解码的硬件加速，而并不包括 H.264 解码。要检查这是否对您的 GPU 有影响，请同时安装驱动和 [libva-utils](<https://archlinux.org/packages/?name=libva-utils>)包 软件包，并检查 `vainfo` 命令的输出结果中是否包含以 `VAProfileH264` 开头的项目。 

对于 H.264 的解码支持是在另一个 g45-h264 分支中独立维护的。您可以安装 [libva-intel-driver-g45-h264](<https://aur.archlinux.org/packages/libva-intel-driver-g45-h264/>)AUR 软件包来使用它。然而，要注意该支持是实验性的，并且其开发工作已被放弃。在GMA 4500系列GPU上使用VA-API与此驱动程序能够帮助 CPU 分载（offload），但可能无法实现像非硬件加速那样平滑的播放。使用 mplayer 进行的测试表明，使用 vaapi 播放 H.264编码的1080p 视频可以将 CPU 负载减半(与 XV overlay相比) ，但是播放非常卡顿，而720p 播放效果相当不错 [[25]](<https://bbs.archlinux.org/viewtopic.php?id=150550>)。这与其他人的经历相印证 [[26]](<https://web.archive.org/web/20160325142959/http://www.emmolution.org/?p=192&cpage=1#comment-12292>)。在 BIOS 中将预先分配的显存大小设置得更高，可以获得更好的硬件解码播放效果。这样做了之后即使是1080p h264视频也可以流畅播放[[27]](<https://lists.libreplanet.org/archive/html/guix-patches/2019-11/msg00652.html>)。同时使用 [mpv-git](<https://aur.archlinux.org/packages/mpv-git/>)AUR 、[ffmpeg-git](<https://aur.archlinux.org/packages/ffmpeg-git/>)AUR 和 [libva-intel-driver-g45-h264](<https://aur.archlinux.org/packages/libva-intel-driver-g45-h264/>)AUR 也可以流畅播放(1080p/720p)视频。通过 MPV 和 Firefox 插件“发送到 MPV 播放器”[[28]](<https://addons.mozilla.org/firefox/addon/send-to-mpv-player/>) ，可以观看硬件加速的 YouTube 视频。 

###  覆写报告的 OpenGL 版本

`MESA_GL_VERSION_OVERRIDE` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")可以为任何应用程序覆写报告的 OpenGL 版本。比如，设置 `MESA_GL_VERSION_OVERRIDE=4.5` 环境变量将会把 OpenGL 版本报告为 4.5. 

**注意：** 您可以使用此变量报告任何已知的 OpenGL 版本，即使 GPU 不支持它。一些应用程序可能不再崩溃，而一些可能反而开始崩溃。所以您可能不希望全局设置这个变量。

###  监控

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[Hardware video acceleration#Verification](<../zh-cn/Hardware_video_acceleration.html#Verification> "Hardware video acceleration")。**

**附注：** This overlaps the content at the previously linked page and would probably be a better fit in a generic page instead of this one dedicated to Intel GPUs. Otherwise, [Hardware video acceleration#Verification](<../zh-cn/Hardware_video_acceleration.html#Verification> "Hardware video acceleration") should be modified to link to each dedicated page instead of duplicating content.（在 [Talk:Intel 图形处理器](<../zh-cn/Talk:Intel_%E5%9B%BE%E5%BD%A2%E5%A4%84%E7%90%86%E5%99%A8.html>) 中讨论）

  * **intel_gpu_top** — 适用于 Intel GPU 的类似 top 命令的任务监视器。 （需要 root 权限）

     <https://gitlab.freedesktop.org/drm/igt-gpu-tools> || [intel-gpu-tools](<https://archlinux.org/packages/?name=intel-gpu-tools>)包

  * **nvtop** — 适用于 AMD、Intel 和 NVIDIA 的 GPU 进程监视器（目前对 Intel GPU 仅有非常基础的支持）

     <https://github.com/Syllo/nvtop> || [nvtop](<https://archlinux.org/packages/?name=nvtop>)包

###  设置亮度和伽玛值

参见[背光](<../zh-cn/%E8%83%8C%E5%85%89.html> "背光")。 

###  测试新的实验性 Xe 驱动

为了尝试（实验性的）[新的 Xe 驱动](<https://www.kernel.org/doc/html//next/gpu/rfc/xe.html>)，你需要： 

  * [linux](<https://archlinux.org/packages/?name=linux>)包 6.8 或更高版本
  * [Tiger Lake](<https://en.wikipedia.org/wiki/Tiger_Lake> "wikipedia:Tiger Lake") 或更新的集成显卡，或者独立显卡
  * 官方源的 [mesa](<https://archlinux.org/packages/?name=mesa>)包 软件包。或者保证 mesa 使用 `-D intel-xe-kmd=enabled` 进行编译

运行此命令，然后记录下您的 PCI ID： 
    
    lspci -nn | grep VGA
    
    00:02.0 VGA compatible controller [0300]: Intel Corporation TigerLake-LP GT2 [Iris Xe Graphics] [8086:**9a49**] (rev 01)
    
然后将带有合适 PCI ID 的以下内容添加到[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")里： 
    
    ... i915.force_probe=!**9a49** xe.force_probe=**9a49**
    
确保您有在需要时可以撤销变更的备用启动方案。 

##  故障排除

###  画面撕裂

####  使用了 Intel 驱动

SNA 加速方法在一些机器上引起撕裂。要解决这个问题，请在驱动程序中启用 `TearFree` 选项，方法是在[配置文件](<../zh-cn/Intel_graphics.html#Xorg_%E9%85%8D%E7%BD%AE> "Intel graphics")中添加以下内容： 
    
    /etc/X11/xorg.conf.d/20-intel.conf
    
    Section "Device"
      Identifier "Intel Graphics"
      Driver "intel"
      Option "TearFree" "true"
    EndSection

参见[原始错误报告](<https://bugs.freedesktop.org/show_bug.cgi?id=37686>)以获得更多信息。 

**注意：**

  * 当 `SwapbuffersWait` 为 `false` 时，该选项可能不工作
  * 此选项可能会显著增加内存分配并降低性能。[[29]](<https://bugs.freedesktop.org/show_bug.cgi?id=37686#c123>)
  * 对于对vsync定时非常挑剔的应用程序来说，这个选项是有问题的，比如 [Super Meat Boy](<https://en.wikipedia.org/wiki/Super_Meat_Boy> "wikipedia:Super Meat Boy").
  * 此选项不适用于UXA加速方法，仅适用于SNA。
  * 对于 Intel UHD 620 或 630 显卡，您需要添加 `Option "TripleBuffer" "true"` 选项才能使 `TearFree` 工作。
  * 通过添加 `Option "DRI" "2"` 来禁用 DRI3 可能是必须的，不然任意全屏应用（比如视频播放）会使 TearFree 失效。[[30]](<https://bugs.freedesktop.org/show_bug.cgi?id=96847#c7>)

####  使用了 modesetting 驱动

modesetting 驱动[在最近才支持](<https://gitlab.freedesktop.org/xorg/xserver/-/merge_requests/1006>) TearFree [[31]](<https://www.phoronix.com/news/xf86-video-modesetting-TearFree>)[[32]](<https://www.phoronix.com/news/Modesetting-TearFree-Merged>)。直到 2023 年 11 月，这个补丁还没有进入稳定版，所以现在你会需要 [xorg-server-git](<https://aur.archlinux.org/packages/xorg-server-git/>)AUR。 
    
    /etc/X11/xorg.conf.d/20-intel.conf
    
    Section "Device"
      Identifier "Intel Graphics"
      Driver "modesetting"
      Option "TearFree" "true"
    EndSection
    
###  禁用垂直同步 (VSYNC)

适用于以下情景： 

  * 由于 GPU 的原因，Chomium/Chrome 有滞后和性能低下的问题，而在使用 --disable-gpu 选项启动时能流畅运行。
  * glxgears 测试未显示预期性能

Intel 驱动程序使用[三重缓冲](<https://www.intel.com/support/graphics/sb/CS-004527.htm>)进行垂直同步；这允许充分的性能释放并避免画面撕裂。若要关闭垂直同步（例如用于基准测试），请在主目录中使用如下 `.drirc` 文件： 
    
    ~/.drirc
    
    <device screen="0" driver="dri2">
    	<application name="Default">
    		<option name="vblank_mode" value="0"/>
    	</application>
    </device>

**注意：** 不要使用 [driconf](<https://aur.archlinux.org/packages/driconf/>)AUR 来创建此文件。它有问题，会设置错误的驱动程序。

###  DRI3 问题

_DRI3_ 是 [xf86-video-intel](<https://archlinux.org/packages/?name=xf86-video-intel>)包 中的默认 DRI 版本。在某些系统上，这可能会导致[这样](<https://bugs.chromium.org/p/chromium/issues/detail?id=370022>)的问题。要切换回 DRI2，请在[配置文件](<../zh-cn/Intel_graphics.html#Xorg_%E9%85%8D%E7%BD%AE> "Intel graphics")中添加以下行： 
    
    Option "DRI" "2"
    
对于 `modesetting` 驱动程序，这种禁用 DRI3 的方法不起作用。所以我们可以设置环境变量 `LIBGL_DRI3_DISABLE=1`。 

###  GTK应用程序中的字体和屏显损坏（挂起/恢复后缺少字形）

如果您在 GTK 应用程序中遇到缺少字形的问题，以下解决方法可能会有所帮助。编辑 `/etc/environment` 并添加以下行： 
    
    /etc/environment
    
    COGL_ATLAS_DEFAULT_BLIT_MODE=framebuffer

另请参考 [FreeDesktop bug 88584](<https://bugs.freedesktop.org/show_bug.cgi?id=88584>). 

###  启动过程中加载模块时显示空白屏幕

[![](../File:Tango-edit-cut.png)](<../File:Tango-edit-cut.png>)**这一章节正在考虑移除。**

**原因:** 从 [mkinitcpio v32](<https://gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio/-/releases/v32>) 开始，`kms` 钩子被默认包含，因此大部分配置会默认启动早启动。 (在 [Talk:Intel 图形处理器](<../zh-cn/Talk:Intel_%E5%9B%BE%E5%BD%A2%E5%A4%84%E7%90%86%E5%99%A8.html>) 讨论)

如果您使用 KMS 晚启动，然后屏幕在加载模块（Loading modules）时显示为空白，您可以试着把 `i915` 和 `intel_agp` 添加到 initramfs 中。请参考[内核级显示模式设置#KMS_早启动](<../zh-cn/%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE.html#KMS_%E6%97%A9%E5%90%AF%E5%8A%A8> "内核级显示模式设置")。 

另外，附加以下[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")似乎也有效： 
    
    video=SVIDEO-1:d
    
如果您需要输出到VGA，请尝试以下操作： 
    
    video=VGA-1:1280x800
    
###  X 窗口系统在使用 Intel 驱动程序时冻结或崩溃

一些关于 X 窗口系统崩溃、冻结或 GPU 挂起的问题，可以通过设置 NoAccel 选项禁用 GPU 来解决。请在[配置文件](<../zh-cn/Intel_graphics.html#Xorg_%E9%85%8D%E7%BD%AE> "Intel graphics")中添加以下内容： 
    
      Option "NoAccel" "True"
    
或者，尝试通过设置 DRI 选项来只禁用 3D 加速： 
    
      Option "DRI" "False"
    
###  添加未检测到的分辨率

这个问题在 [Xrandr 页面](<../zh-cn/Xrandr.html#%E6%B7%BB%E5%8A%A0%E6%9C%AA%E8%A2%AB%E6%A3%80%E6%B5%8B%E5%88%B0%E7%9A%84%E6%9C%89%E6%95%88%E5%88%86%E8%BE%A8%E7%8E%87> "Xrandr")中有详细的说明。 

###  无法调节背光

如果您的设备从挂起中恢复后，调整屏幕背光亮度的热键失效，请根据 [Backlight](<../zh-cn/%E8%83%8C%E5%85%89.html> "Backlight") 一文检查您的配置。 

如果问题仍然存在，请尝试如下任一[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数"): 
    
    acpi_osi=Linux
    acpi_osi="!Windows 2012"
    acpi_osi=
    
还要确保您没有使用 fastboot 模式 (`i915.fastboot` 内核参数) ，因为它[会破坏背光控制](<https://www.phoronix.com/forums/forum/software/mobile-linux/1066447-arch-linux-users-with-intel-graphics-can-begin-enjoying-a-flicker-free-boot>)。 

###  Chromium 和 Firefox 损坏或无响应

如果您在 Chromium 和/或 Firefox 中遇到了损坏、无响应、性能滞后或缓慢的问题，一些可能的解决方案包括： 

  * [把 AccelMethod 设置为 "uxa"](<../zh-cn/Intel_graphics.html#AccelMethod> "Intel graphics")
  * [禁用垂直同步 (VSYNC)](<../zh-cn/Intel_graphics.html#%E7%A6%81%E7%94%A8%E5%9E%82%E7%9B%B4%E5%90%8C%E6%AD%A5_\(VSYNC\)> "Intel graphics")
  * [启用 TearFree 选项](<../zh-cn/Intel_graphics.html#%E7%94%BB%E9%9D%A2%E6%92%95%E8%A3%82> "Intel graphics")
  * 禁用 DRI 和加速法 (在 Intel 第十代处理器 Iris 显卡上测试过): 
        
        Option "NoAccel" "True"
        Option "DRI" "False"
        
###  4.0+ 版本的内核会在使用 Broadwell 或 Core-M 芯片时崩溃

X/Wayland 加载后几秒钟，机器将冻结，journalctl 将记录内核崩溃并提到 Intel 显卡： 
    
    Jun 16 17:54:03 hostname kernel: BUG: unable to handle kernel NULL pointer dereference at           (null)
    Jun 16 17:54:03 hostname kernel: IP: [<          (null)>]           (null)
    ...
    Jun 16 17:54:03 hostname kernel: CPU: 0 PID: 733 Comm: gnome-shell Tainted: G     U     O    4.0.5-1-ARCH #1
    ...
    Jun 16 17:54:03 hostname kernel: Call Trace:
    Jun 16 17:54:03 hostname kernel:  [<ffffffffa055cc27>] ? i915_gem_object_sync+0xe7/0x190 [i915]
    Jun 16 17:54:03 hostname kernel:  [<ffffffffa0579634>] intel_execlists_submission+0x294/0x4c0 [i915]
    Jun 16 17:54:03 hostname kernel:  [<ffffffffa05539fc>] i915_gem_do_execbuffer.isra.12+0xabc/0x1230 [i915]
    Jun 16 17:54:03 hostname kernel:  [<ffffffffa055d349>] ? i915_gem_object_set_to_cpu_domain+0xa9/0x1f0 [i915]
    Jun 16 17:54:03 hostname kernel:  [<ffffffff811ba2ae>] ? __kmalloc+0x2e/0x2a0
    Jun 16 17:54:03 hostname kernel:  [<ffffffffa0555471>] i915_gem_execbuffer2+0x141/0x2b0 [i915]
    Jun 16 17:54:03 hostname kernel:  [<ffffffffa042fcab>] drm_ioctl+0x1db/0x640 [drm]
    Jun 16 17:54:03 hostname kernel:  [<ffffffffa0555330>] ? i915_gem_execbuffer+0x450/0x450 [i915]
    Jun 16 17:54:03 hostname kernel:  [<ffffffff8122339b>] ? eventfd_ctx_read+0x16b/0x200
    Jun 16 17:54:03 hostname kernel:  [<ffffffff811ebc36>] do_vfs_ioctl+0x2c6/0x4d0
    Jun 16 17:54:03 hostname kernel:  [<ffffffff811f6452>] ? __fget+0x72/0xb0
    Jun 16 17:54:03 hostname kernel:  [<ffffffff811ebec1>] SyS_ioctl+0x81/0xa0
    Jun 16 17:54:03 hostname kernel:  [<ffffffff8157a589>] system_call_fastpath+0x12/0x17
    Jun 16 17:54:03 hostname kernel: Code:  Bad RIP value.
    Jun 16 17:54:03 hostname kernel: RIP  [<          (null)>]           (null)
    
这可以通过禁用 execlist 支持来解决，该支持在 4.0 内核中被设为为默认值。添加以下[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")： 
    
    i915.enable_execlists=0
    
目前已知该问题直到 4.0.5 内核上仍存在。 

###  Windows 客户机运行迟缓

VirtualBox 中 Windows 客户机的视频输出有时会挂起，直到主机强制屏幕更新(例如移动鼠标光标)。删除 `enable_fbc=1` 选项可以解决这个问题。 

###  屏幕闪烁

面板自刷新 (PSR), 一种 Intel iGPU （核显）使用的节能技术已知在某些情况下会导致闪烁 [FS#49628](<https://bugs.archlinux.org/task/49628>) [FS#49371](<https://bugs.archlinux.org/task/49371>) [FS#50605](<https://bugs.archlinux.org/task/50605>). 临时的解决办法是通过设置 `i915.enable_psr=0` [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")来禁用该功能。 

###  在 i915 驱动上使用 OpenGL 2.1

正如[这篇文章](<https://www.phoronix.com/scan.php?page=news_item&px=Mesa-i915-OpenGL-2-Drop>)所说，把 [mesa](<https://archlinux.org/packages/?name=mesa>)包 从 13.x 版本更新到 17 可能会导致第三代 Intel GPU （如GMA3100，参阅[这里](<https://en.wikipedia.org/wiki/List_of_Intel_graphics_processing_units#Third_generation> "w:List of Intel graphics processing units")）上的 OpenGL 2.1 支持失效，并使其降级到 OpenGL 1.4。然而您可以通过配置 `/etc/drirc` 或 `~/.drirc` 文件中的选项来手动恢复它： 
    
    /etc/drirc
    
    <driconf>
    ...
        <device driver="i915">
            <application name="Default">
                <option name="**stub_occlusion_query** " value="**true** " />
                <option name="**fragment_shader** " value="**true** " />
            </application>
        </device>
    ...
    </driconf>

**注意：**

  * 作出该让步的原因是 Chromium 和其他应用程序的糟糕体验。如果有需要，您可以参考 [此文](<https://dri.freedesktop.org/wiki/ConfigurationInfrastructure/>) 来对 drirc 文件作特定于应用程序的修改，比如专门针对 Chromium 禁用 gl2.1。
  * 新的包含在 [mesa](<https://archlinux.org/packages/?name=mesa>)包 软件包内的基于 Gallium 的 i915 驱动会一直报告 OpenGL 2.1，所以这些设置对于那个驱动来说不再需要了。

###  KMS 问题：终端只在很小的一块区域中显示

其中一个低分辨率视频端口会在引导时启用，这将导致终端仅能使用屏幕的一小块区域。 要修复这个问题，在引导加载程序的内核命令行参数中，使用 i915 模块参数 `video=SVIDEO-1:d` 来明确禁用该端口。有关详细信息，请参阅[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")。 

如果这不起作用，请尝试禁用 TV1 或 VGA1，而不是 SVIDEO-1。视频端口名称可以用 [xrandr](<../zh-cn/Xrandr.html> "Xrandr") 列出。 

###  Haswell CPU 使用 HDMI 输出时没有声音

根据一个 [Linux 内核问题](<https://bugzilla.kernel.org/show_bug.cgi?id=60769>)，在设置 `intel_iommu=on` 参数时声音不会通过 HDMI 端口输出。要修复该问题，使用如下[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")： 
    
    intel_iommu=on,igfx_off
    
或者也可以禁用 IOMMU： 
    
    intel_iommu=off
    
###  低功耗 Intel CPU 会崩溃或冻结

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 在额外的声明里提到，`enable_dc=0` 可能不会影响到电源管理（在 [Intel graphics#Incorrect statements regarding power usage penalty of enable_dc=0](<../zh-cn/Intel_graphics.html#Incorrect_statements_regarding_power_usage_penalty_of_enable_dc=0> "Intel graphics") 中讨论）

由于低功耗 Intel CPU 上电源管理功能的问题，低功耗 Intel 处理器和/或笔记本电脑处理器有随机挂起或崩溃的倾向。如果发生此类崩溃，您将看不到任何报告此问题的日志。添加以下[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")可能有助于解决问题。 

**注意：** 不建议同时使用以下三个内核参数
    
    intel_idle.max_cstate=1 i915.enable_dc=0 ahci.mobile_lpm_policy=1
    
`ahci.mobile_lpm_policy=1` 能修复部分联想笔记本电脑和一些宏碁笔记本电脑因 SATA 控制器电源管理问题而出现的挂起故障。该解决方法严格来说与 Intel 显卡无关，但它确实解决了相关问题。添加此内核参数可以将链路电源管理(LPM)从固件默认值修改为最大性能，并且还可以解决当您在某些联想机器上更改显示器亮度时出现的挂起问题。但这么做在现代超级本上会增加 1 至 1.5 W 的闲置功耗。有关更多信息，特别是有关其他状态的信息，请参阅 [Linux内核邮件列表](<https://lore.kernel.org/lkml/20171211165216.5604-1-hdegoede@redhat.com/>)和 [Red Hat 文档](<https://access.redhat.com/documentation/en-en/red_hat_enterprise_linux/6/html/power_management_guide/alpm>)。 

`i915.enable_dc=0` 会禁用GPU电源管理。这确实解决了某些 Intel 系统上的随机挂起问题，特别是 Goldmount 和 Kaby Lake Refresh 芯片。但使用此参数会提高笔记本电脑的功耗并缩短电池寿命。 

`intel_idle.max_cstate=1` 会限制处理器的睡眠状态，防止处理器进入深度睡眠状态。这绝对不是理想的做法，而且确实会导致更高的功率使用和更低的电池寿命。然而，它确实解决了许多 Intel 系统上的随机挂起问题。如果您使用的是 Intel Baytrail 或 Kaby Lake Refresh 芯片，请使用此参数。Intel Baytrail 芯片由于一个硬件缺陷，在没有这个内核参数的情况下会随机挂起[[33]](<https://bugzilla.kernel.org/show_bug.cgi?id=109051#c752>)。有关 max_cstate 参数的更多信息，请参见[内核文档](<https://docs.kernel.org/admin-guide/pm/intel_idle.html#kernel-command-line-options-and-module-parameters>)以及 [GitHub 上](<https://gist.github.com/wmealing/2dd2b543c4d3cff6cab7>)关于 cstates 的一篇文章。 

如果您尝试通过一次性添加 `intel_idle.max_cstate=1 i915.enable_dc=0 ahci.mobile_lpm_policy=1` 等三个参数来解决频繁挂起的问题，然后成功了，那您应该用排除法找出真正解决问题的那个参数。因为如果实际的问题与 SATA 电源管理有关，并且 `ahci.mobile_lpm_policy=1` 参数解决了这个问题，那么禁用 cstate 和显示电源管理是不可取的。 

参考 [Linux Reviews](<https://linuxreviews.org/Intel_graphics#Kernel_Parameters>) 网站以获取更多信息。 

###  添加对 165Hz 显示器的支持

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[内核级显示模式设置#强制设置显示模式与_EDID](<../zh-cn/%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE.html#%E5%BC%BA%E5%88%B6%E8%AE%BE%E7%BD%AE%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E4%B8%8E_EDID> "内核级显示模式设置")。**

**附注：** 这种技术似乎并不特定于 i915。在合并之前，请验证安装脚本是必需的，并且没有更简单的方法来将 EDID BIN 添加到 initramfs。（在 [Talk:Intel 图形处理器](<../zh-cn/Talk:Intel_%E5%9B%BE%E5%BD%A2%E5%A4%84%E7%90%86%E5%99%A8.html>) 中讨论）

对于某些 165Hz 显示器， _xrandr_ 可能不会显示165Hz选项，且 [#添加未检测到的分辨率](<#%E6%B7%BB%E5%8A%A0%E6%9C%AA%E6%A3%80%E6%B5%8B%E5%88%B0%E7%9A%84%E5%88%86%E8%BE%A8%E7%8E%87>)中的方法并不能解决这一问题。在这种情况下，请参见 StackExchange 上的问答 [i915-driver-stuck-at-40hz-on-165hz-screen](<https://unix.stackexchange.com/questions/680356/i915-driver-stuck-at-40hz-on-165hz-screen>)。 

**注意：** 除了创建 `/etc/initramfs-tools/hooks/edid` 文件之外，应该通过以下方式创建 [mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio") 钩子： 
    
    /etc/initcpio/install/edid
    
    #!/bin/bash
    
    build() {
        add_file /lib/firmware/edid/edid.bin
    }
    
    help() {
        cat <<HELPEOF
    This hook add support for 165Hz
    HELPEOF
    }
    
然后在 `/etc/mkinitcpio.conf` 文件的 HOOKS 中添加 _edid_ ，就像下面这样 
    
    /etc/mkinitcpio.conf
    
    HOOKS=(... fsck edid)

最后 [重新生成initramfs](<../zh-cn/Mkinitcpio.html#%E5%88%9B%E5%BB%BA%E5%92%8C%E5%90%AF%E7%94%A8%E9%95%9C%E5%83%8F> "Mkinitcpio"). 

###  Raptor Lake 和 Alder Lake-P 处理器从睡眠/挂起中恢复时冻结

来自不同供应商的 Raptor Lake 和 Alder Lake-P 第 12 代移动处理器的笔记本电脑的用户在从暂停状态中醒来后，遇到了了冻结和黑屏。这是因为根据 freedesktop issue [5531](<https://gitlab.freedesktop.org/drm/intel/-/issues/5531>) 和 [6401](<https://gitlab.freedesktop.org/drm/intel/-/issues/6401>) 的描述，许多笔记本电脑供应商提供了错误的 VBT（Video BIOS Table，视频 BIOS 表），错误地描述了连接到 iGPU 的实际端口。在这种情况下，所有被记录的案例都怀疑是重复的 eDP 条目。 

考虑到大多数供应商[不会](<https://gitlab.freedesktop.org/drm/i915/kernel/-/issues/7402>)为运行正常的 Windows 操作系统的笔记本电脑发布 BIOS 更新，Linux 用户只能在内核端解决这个问题。有两个方法可以防止出现重复的 eDP 条目以影响到内核：[修补内核](<https://bbs.archlinux.org/viewtopic.php?id=284176>)或者[加载一个 修改过的 VBT](<https://gitlab.freedesktop.org/drm/i915/kernel/-/issues/7709>)。 

为了修补内核，重复的 eDP 条目需要通过分析以下命令的输出被辨别出来： 
    
    # intel_vbt_decode /sys/kernel/debug/dri/1/i915_vbt
    
    Child device info:
            Device handle: 0x0008 (LFP 1 (eDP))
            Device type: 0x1806 (unknown)
     ...
     Child device info:
            Device handle: 0x0080 (LFP 2 (eDP))
            Device type: 0x1806 (unknown)

输出表明这里确实存在重复的 eDP，内核应该忽略掉第二个，但是用户还是被鼓励检查这个。然后可以使用下面的补丁修补内核，如果有需要的话重复条目的索引可以被替换为 `ignoreEntry = 1`。 
    
    --- a/drivers/gpu/drm/i915/display/intel_bios.c
    +++ b/drivers/gpu/drm/i915/display/intel_bios.c
    @@ -3688,6 +3688,14 @@
    {
           struct intel_bios_encoder_data *devdata;
    
    +       int ignoreEntry = 0;
    +
           list_for_each_entry(devdata, &i915->display.vbt.display_devices, node)
    -               func(i915, devdata);
    +       {
    +               if (ignoreEntry != 1)
    +               {
    +                       func(i915, devdata);
    +                       ignoreEntry++;
    +               }
    +       }
    }

第二种解决这个问题的方法是通过直接[清除 VBT 内重复条目](<https://gitlab.freedesktop.org/drm/i915/kernel/-/issues/7709>)来修改 VBT。 

复制 VBT，使用十六进制编辑器编辑它然后修改重复的 device handle 的 device type 至 `00 00`： 
    
    $ cat /sys/kernel/debug/dri/0/i915_vbt > vbt
    
    --- vbt
    +++ modified_vbt
    @@ -22,10 +22,10 @@
     00000150  00 08 00 20 00 08 00 10  00 08 00 02 00 08 00 01  |... ............|
     00000160  00 08 00 00 01 08 00 00  00 04 00 00 00 40 00 00  |.............@..|
     00000170  00 20 00 00 00 10 00 00  00 02 00 00 00 01 00 00  |. ..............|
    -00000180  00 00 01 00 00 02 8b 01  02 04 00 00 27 08 00 06  |............'...|
    -00000190  18 00 00 00 00 00 00 00  00 00 00 00 00 0a 00 00  |................|
    +00000180  00 00 01 00 00 02 8b 01  02 04 00 00 27 08 00 00  |............'...|
    +00000190  00 00 00 00 00 00 00 00  00 00 00 00 00 0a 00 00  |................|
     000001a0  03 00 00 00 c0 00 40 00  20 00 00 00 00 00 00 00  |......@. .......|
    -000001b0  00 00 20 00 80 00 06 18  00 00 00 00 00 00 00 00  |.. .............|
    +000001b0  00 00 20 00 80 00 00 00  00 00 00 00 00 00 00 00  |.. .............|
     000001c0  00 00 00 00 07 00 00 00  00 00 00 c0 00 10 00 20  |............... |
     000001d0  00 00 00 00 00 00 00 00  00 20 00 04 00 d2 60 00  |......... ....`.|
     000001e0  10 10 00 23 21 10 00 00  00 00 00 07 00 00 02 00  |...#!...........|
    
这个修改过的 VBT 可以通过复制到 `/lib/firmware/modified_vbt` 再传递 `i915.vbt_firmware=modified_vbt` 的内核参数来加载，以及如果有需要，[重新生成 initramfs](<../zh-cn/Mkinitcpio.html#%E5%88%9B%E5%BB%BA%E5%92%8C%E5%90%AF%E7%94%A8%E9%95%9C%E5%83%8F> "Mkinitcpio")。 

##  参阅

  * [linux graphics](<https://www.intel.cn/content/www/cn/zh/support/articles/000005520/graphics.html>)（包含一个有 106 种相关产品的列表）
  * [Intel® Processor Graphics](<https://www.intel.cn/content/www/cn/zh/developer/articles/guide/intel-graphics-developers-guides.html>)（包含一个含有处理器系列、正式的代号、发行日期和显示技术的表）
