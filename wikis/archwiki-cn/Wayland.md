**翻译状态：**

  * 本文（或部分内容）译自 [Wayland](<https://wiki.archlinux.org/title/Wayland> "arch:Wayland")，最近一次同步于 2026-01-24，若英文版本有所[更改](<https://wiki.archlinux.org/title/Wayland?diff=0&oldid=862504>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Wayland_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [内核级显示模式设置](<../zh-cn/%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE.html> "内核级显示模式设置")
  * [Xorg](<../zh-cn/Xorg.html> "Xorg")
  * [屏幕捕获#Wayland](<../zh-cn/%E5%B1%8F%E5%B9%95%E6%8D%95%E8%8E%B7.html#Wayland> "屏幕捕获")

[Wayland](<https://wayland.freedesktop.org/>) 是一个显示服务器协议，已普遍作为 [X 窗口系统](<../zh-cn/X_Window_System.html> "X Window System")的继任者 [[1]](<https://blogs.kde.org/2025/11/26/going-all-in-on-a-wayland-future/>) [[2]](<https://blogs.gnome.org/alatiera/2025/06/08/the-x11-session-removal/>) [[3]](<https://discourse.ubuntu.com/t/ubuntu-25-10-drops-support-for-gnome-on-xorg/62538>) [[4]](<https://pagure.io/fesco/issue/3408>)。可参见 [Wikipedia 上的 Wayland 与 Xorg 的对比](<https://en.wikipedia.org/wiki/Wayland_\(display_server_protocol\)#Differences_between_Wayland_and_X> "wikipedia:Wayland \(display server protocol\)")。 

由于使用 Wayland 协议的显示服务器也可作为[混成窗口管理器](<https://en.wikipedia.org/wiki/Compositing_window_manager> "wikipedia:Compositing window manager")，因此被称为**混成器** （compositor）。你可以在[#混成器](<#%E6%B7%B7%E6%88%90%E5%99%A8>)中找到相关信息。 

为了兼容原生 [X11](<../zh-cn/Xorg.html> "X11") 应用程序，使其在 Wayland 中无缝运行，可以使用 [#Xwayland](<#Xwayland>)，它在 Wayland 中提供了 X 服务器。 

##  系统需求

和 [Xorg](<../zh-cn/Xorg.html> "Xorg") 不同的是，Wayland 本身只是一个协议，没有一个通用的“显示服务器”可供安装。需要安装的是兼容的 GPU 驱动（本节）和混成器（下一节）或将混成器内置其中的[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")（例如 [GNOME](<../zh-cn/GNOME.html> "GNOME") 或 [Plasma](<../zh-cn/KDE.html> "Plasma")）。大多数 Wayland 混成器只能在使用[内核级显示模式设置](<../zh-cn/%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE.html> "内核级显示模式设置")的系统上工作。 

GPU 驱动与 Wayland 混成器必须支持相同的缓冲区 API (Buffer API) 才能够互相兼容。现在主要有两种 API：[GBM](<https://en.wikipedia.org/wiki/Generic_Buffer_Management> "wikipedia:Generic Buffer Management") 和 [EGLStreams](<https://www.phoronix.com/scan.php?page=news_item&px=XDC2016-Device-Memory-API>)。 

缓冲区 API | GPU 驱动支持 | Wayland 混成器支持   
---|---|---  
GBM | 除版本号低于 495 的 [NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA") 驱动，均支持 | 全部   
EGLStreams | [NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA") |  [GNOME](<../zh-cn/GNOME.html> "GNOME")  
  
    * 版本 ≥ 495 的 NVIDIA 驱动同时支持 EGLStreams 和 GBM。[[5]](<https://www.phoronix.com/scan.php?page=news_item&px=NVIDIA-495.44-Linux-Driver>)

自 NVIDIA 在版本 495 引入 GBM 支持以来，许多混成器 (包括 Mutter 和 KWin) 都开始默认使用 GBM 。通常认为 GBM 更好，有更为广泛的支持，而以前仅支持 EGLStreams 是因为之前无法在 Wayland 下通过专有驱动程序来使用 NVIDIA GPU。此外，在 NVIDIA 支持 GBM 后，KWin 放弃了对 EGLStreams 的支持 

如果您使用的是流行的桌面环境/混成器，GPU 也受 NVIDIA 支持，那么很可能已经在使用 GBM 后端了。要检查是否使用 GBM 后端，请执行 `journalctl -b 0 --grep "renderer for"`。要强制使用 GBM 后端，请设置以下[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")： 
    
    GBM_BACKEND=nvidia-drm
    __GLX_VENDOR_LIBRARY_NAME=nvidia
    
##  混成器

**堆叠式** 、**平铺式** 和**动态** 的区别参见[窗口管理器#类型](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html#%E7%B1%BB%E5%9E%8B> "窗口管理器")。 

###  堆叠式

  * **cosmic-comp** — [COSMIC](<../zh-cn/COSMIC.html> "COSMIC") 桌面环境的混成器。

     <https://github.com/pop-os/cosmic-comp> || [cosmic-comp](<https://archlinux.org/packages/?name=cosmic-comp>)包

  * **hikari** — 基于 wlroots 并受 [cwm](<../zh-cn/Cwm.html> "Cwm") 启发开发，在 FreeBSD 上开发很活跃，但也支持 Linux。

     <https://hikari.acmelabs.space/> || [hikari](<https://aur.archlinux.org/packages/hikari/>)AUR

  * **KDE[KWin](<https://en.wikipedia.org/wiki/KWin> "w:KWin")** — 请参阅 [KDE#启动 Plasma](<../zh-cn/KDE.html#%E5%90%AF%E5%8A%A8_Plasma> "KDE")。

     <https://userbase.kde.org/KWin> || [kwin](<https://archlinux.org/packages/?name=kwin>)包

  * **[labwc](</wzh/index.php?title=Labwc&action=edit&redlink=1> "Labwc（页面不存在）") （英语：[labwc](<https://wiki.archlinux.org/title/labwc> "en:labwc")）** — 基于 wlroots 并受 Openbox 启发的混成器。

     <https://github.com/labwc/labwc> || [labwc](<https://archlinux.org/packages/?name=labwc>)包

  * **[Mutter](<https://en.wikipedia.org/wiki/Mutter_\(software\)> "w:Mutter \(software\)")** — 请参阅 [GNOME#运行 GNOME](<../zh-cn/GNOME.html#%E8%BF%90%E8%A1%8C_GNOME> "GNOME")。

     <https://gitlab.gnome.org/GNOME/mutter> || [mutter](<https://archlinux.org/packages/?name=mutter>)包

  * **waybox** — 一个 *box 风格（极简主义）的 Wayland 混成器，主要基于 Openbox 设计。

     <https://github.com/wizbright/waybox> || [waybox](<https://aur.archlinux.org/packages/waybox/>)AUR

  * **wayfire** — 3D 混成器，受 [Compiz](<../zh-cn/Compiz.html> "Compiz") 启发并基于 wlroots 开发。

     <https://wayfire.org/> || [wayfire](<https://aur.archlinux.org/packages/wayfire/>)AUR

  * **[Weston](<../zh-cn/Weston.html> "Weston")** — Wayland 混成器，设计注重正确性、可靠性、可预测性和性能。

     <https://gitlab.freedesktop.org/wayland/weston> || [weston](<https://archlinux.org/packages/?name=weston>)包

  * **wio** — 基于 wlroots 的混成器，致力于复刻 Plan 9 的 Rio 桌面的外观和质感。

     <https://gitlab.com/Rubo/wio> || [wio-wl](<https://aur.archlinux.org/packages/wio-wl/>)AUR

  * **wlmaker** — 基于 wlroots 的混成器，受 [Window Maker](</wzh/index.php?title=Window_Maker&action=edit&redlink=1> "Window Maker（页面不存在）")（英语：[Window Maker](<https://wiki.archlinux.org/title/Window_Maker> "en:Window Maker")） 启发。

     <https://phkaeser.github.io/wlmaker/> || [wlmaker](<https://aur.archlinux.org/packages/wlmaker/>)AUR

  * **woodland** — 一个极简轻量级的基于 wlroots 的堆叠式混成器，适用于 Wayland，受 wayfire 和 TinyWl 启发。

     <https://github.com/DiogenesN/woodland> || [woodland](<https://aur.archlinux.org/packages/woodland/>)AUR

###  平铺式

  * **[Cagebreak](</wzh/index.php?title=Cagebreak&action=edit&redlink=1> "Cagebreak（页面不存在）") （英语：[Cagebreak](<https://wiki.archlinux.org/title/Cagebreak> "en:Cagebreak")）** — 基于 Cage，受 [Ratpoison](<../zh-cn/Ratpoison.html> "Ratpoison") 启发。

     <https://github.com/project-repo/cagebreak> || [cagebreak](<https://aur.archlinux.org/packages/cagebreak/>)AUR

  * **miracle-wm** — 基于 Mir 的 Wayland 混成器，风格类似 i3 和 sway，旨在比两者更炫目且功能更丰富，如 swayfx。

     <https://github.com/miracle-wm-org/miracle-wm> || [miracle-wm](<https://aur.archlinux.org/packages/miracle-wm/>)AUR

  * **[niri](<../zh-cn/Niri.html> "Niri")** — 可滚动的平铺式 Wayland 混成器。

     <https://github.com/YaLTeR/niri/> || [niri](<https://archlinux.org/packages/?name=niri>)包

  * **[Qtile](<../zh-cn/Qtile.html> "Qtile")** — 功能齐全、可定制性强的平铺式 Xorg 窗口管理器和 Wayland 混成器，使用 Python 开发、配置。

     <https://github.com/qtile/qtile> || [qtile](<https://archlinux.org/packages/?name=qtile>)包

  * **[Sway](<../zh-cn/Sway.html> "Sway")** — 基于 wlroots、与 [i3](<../zh-cn/I3.html> "I3") 兼容的 Wayland 混成器。

     <https://github.com/swaywm/sway> || [sway](<https://archlinux.org/packages/?name=sway>)包

  * **SwayFx** — [Sway](<../zh-cn/Sway.html> "Sway")，但带有视觉效果！

     <https://github.com/WillPower3309/swayfx> || [swayfx](<https://aur.archlinux.org/packages/swayfx/>)AUR

  * **Velox** — 基于 swc 的简单窗口管理器，受 dwm 和 [xmonad](<../zh-cn/Xmonad.html> "Xmonad") 启发。

     <https://github.com/michaelforney/velox> || [velox-git](<https://aur.archlinux.org/packages/velox-git/>)AUR

###  动态

  * **[cwc](</wzh/index.php?title=Cwc&action=edit&redlink=1> "Cwc（页面不存在）") （英语：[cwc](<https://wiki.archlinux.org/title/cwc> "en:cwc")）** — 基于 wlroots、类似[awesome](<../zh-cn/Awesome.html> "Awesome")的 Wayland 混成器

     <https://cudiph.github.io/cwc/apidoc/> || [cwc](<https://aur.archlinux.org/packages/cwc/>)AUR

  * **[dwl](</wzh/index.php?title=Dwl&action=edit&redlink=1> "Dwl（页面不存在）") （英语：[dwl](<https://wiki.archlinux.org/title/dwl> "en:dwl")）** — 基于 wlroots、类似 [dwm](<../zh-cn/Dwm.html> "Dwm") 的 Wayland 混成器。

     <https://codeberg.org/dwl/dwl> || [dwl](<https://aur.archlinux.org/packages/dwl/>)AUR

  * **[Hyprland](<../zh-cn/Hyprland.html> "Hyprland")** — 不以牺牲外观为代价的动态平铺式 Wayland 混成器。

     <https://hypr.land> || [hyprland](<https://archlinux.org/packages/?name=hyprland>)包

  * **japokwm** — 基于 wlroots 创建布局的动态平铺式 Wayland 混成器。

     <https://github.com/werererer/japokwm> || [japokwm-git](<https://aur.archlinux.org/packages/japokwm-git/>)AUR

  * **[Mangowc](</wzh/index.php?title=Mangowc&action=edit&redlink=1> "Mangowc（页面不存在）") （英语：[Mangowc](<https://wiki.archlinux.org/title/Mangowc> "en:Mangowc")）** — 基于 [dwl](</wzh/index.php?title=Dwl&action=edit&redlink=1> "Dwl（页面不存在）")（英语：[dwl](<https://wiki.archlinux.org/title/dwl> "en:dwl")） 的混成器，提供标准配置文件、可选的滚动布局以及视觉特效支持。

     <https://github.com/DreamMaoMao/mangowc> || [mangowc](<https://aur.archlinux.org/packages/mangowc/>)AUR

  * **[river](</wzh/index.php?title=River&action=edit&redlink=1> "River（页面不存在）") （英语：[river](<https://wiki.archlinux.org/title/river> "en:river")）** — 受 dwm 和 [bspwm](<../zh-cn/Bspwm.html> "Bspwm") 启发的动态平铺式 Wayland 混成器。

     <https://codeberg.org/river/river> || [river](<https://archlinux.org/packages/?name=river>)包

###  其它

  * **Cage** — 像自助终端那样，全屏显示单个应用程序。

     <https://www.hjdskes.nl/projects/cage/> || [cage](<https://archlinux.org/packages/?name=cage>)包

  * **GNOME Kiosk** — 基于 Mutter 的混成器，适用于固定用途或单应用部署，如墙面显示器和销售终端（kiosk）。

     <https://gitlab.gnome.org/GNOME/gnome-kiosk> || [gnome-kiosk](<https://aur.archlinux.org/packages/gnome-kiosk/>)AUR

  * **phoc** — 适用于移动设备的基于 wlroots 的轻量混成器。

     <https://gitlab.gnome.org/World/Phosh/phoc> || [phoc](<https://archlinux.org/packages/?name=phoc>)包

  * **Wayback** — X11 兼容层，允许使用 Wayland 组件运行完整的 X11 桌面环境。实验性，开发处于早期阶段。

     <https://wayback.freedesktop.org/> || [wayback-x11](<https://aur.archlinux.org/packages/wayback-x11/>)AUR

上述某些混成器支持从[显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")启动。请查看 `/usr/share/wayland-sessions/_混成器_.desktop` 文件来了解如何启动显示上述混成器。 

##  显示管理器

下面列出的显示管理器均支持启动 Wayland 混成器。 

名称  | 运行于  | 描述   
---|---|---  
[emptty](<https://archlinux.org/packages/?name=emptty>)包 | tty  | 简单的 TTY CLI 显示管理器。   
[plasma-login-manager-git](<https://aur.archlinux.org/packages/plasma-login-manager-git/>)AUR | Wayland  | KDE目前正在活跃开发的显示管理器。   
[GDM](<../zh-cn/GDM.html> "GDM") | Wayland  |  [GNOME](<../zh-cn/GNOME.html> "GNOME") 的显示管理器。   
[greetd](<../zh-cn/Greetd.html> "Greetd") | Wayland/Xorg/tty 参考 [Greetd#Greeters](<../zh-cn/Greetd.html#Greeters> "Greetd")。  | 极简且使用灵活的登录守护程序。   
[lemurs](<https://archlinux.org/packages/?name=lemurs>)包 | tty  | 用 Rust 编写的 TUI 显示管理器。   
[lidm](<https://aur.archlinux.org/packages/lidm/>)AUR | tty  | 用C语言开发的全彩可定制的TUI 显示管理器.   
[LightDM](<../zh-cn/LightDM.html> "LightDM") | Xorg[[6]](<https://github.com/canonical/lightdm/issues/267>) | 跨桌面显示管理器。   
[Ly](<../zh-cn/Ly.html> "Ly") | tty  | 用 Zig 语言编写的 TUI 显示管理器。   
[SDDM](<../zh-cn/SDDM.html> "SDDM") | Wayland/Xorg  | 基于 QML 开发的显示管理器。   
[tbsm](<https://aur.archlinux.org/packages/tbsm/>)AUR | tty  | 用纯 Bash 编写的简单 CLI 会话启动器。   
[uwsm](<../zh-cn/%E9%80%9A%E7%94%A8Wayland%E4%BC%9A%E8%AF%9D%E7%AE%A1%E7%90%86%E5%99%A8.html> "Uwsm") | tty  | 管理独立混成器的会话和 XDG 自启的管理器。提供一个TUI 菜单，但也可以与其他显示管理器一起使用。   
  
## Xwayland

[Xwayland(1)](<https://man.archlinux.org/man/Xwayland.1>) 是一个在 Wayland 下运行的 X 服务器，以兼容尚未支持 Wayland 的原生 [X11](<../zh-cn/Xorg.html> "X11") 应用程序。要使用它，请[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [xorg-xwayland](<https://archlinux.org/packages/?name=xorg-xwayland>)包。 

Xwayland 通过混成器启动，因此请参见所使用混成器的文档了解其兼容性和启动方式。 

**注意：**

  * 安全性：Xwayland 是一个 X 服务器，因此不具备 Wayland 的安全特性。
  * 性能：大部分情况下，Xwayland 的性能与 X11 [几乎相同](<https://openbenchmarking.org/result/2202053-NE-NVIDIARTX35>)。
  * 兼容性：Xwayland 并不完全向后兼容 X11。某些应用程序在 Xwayland 下可能无法正常工作。

### Wayback

[Wayback](<https://wayback.freedesktop.org/>)（[wayback-x11](<https://aur.archlinux.org/packages/wayback-x11/>)AUR、[wayback-x11-git](<https://aur.archlinux.org/packages/wayback-x11-git/>)AUR）是一个 X11 兼容层，允许使用 Wayland 组件运行完整的 X11 桌面环境，旨在最终取代 Xorg，从而减轻 X11 应用程序的维护负担。 

###  NVIDIA 驱动

**注意：** 470 版本之前的 NVIDIA 驱动（例如 [nvidia-390xx-dkms](<https://aur.archlinux.org/packages/nvidia-390xx-dkms/>)AUR）不支持硬件加速的 Xwayland，导致非 Wayland 原生应用程序在 Wayland 会话中性能不佳。

需要启用 [DRM KMS](<../zh-cn/NVIDIA.html#DRM_%E5%86%85%E6%A0%B8%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE> "NVIDIA")。有关您的显示管理器（例如 [GDM](<../zh-cn/GDM.html#Wayland_%E5%92%8C%E4%B8%93%E6%9C%89_NVIDIA_%E9%A9%B1%E5%8A%A8> "GDM")）的更多信息，请参阅[官方文档](<https://download.nvidia.com/XFree86/Linux-x86_64/515.48.07/README/xwayland.html>)。 

###  检测应用程序是否通过 Xwayland 运行

使用 [xorg-xeyes](<https://archlinux.org/packages/?name=xorg-xeyes>)包 的 `xeyes` 可以确定应用程序是否通过 Xwayland 运行，如果鼠标指针在 Xwayland 程序上，xeyes 窗口中的眼珠会转向鼠标指针。 

或使用 [xorg-xwininfo](<https://archlinux.org/packages/?name=xorg-xwininfo>)包 的 `xwininfo`。如果鼠标指针在 Xwayland 程序上，鼠标指针会变成“＋”。此时点击窗口，它会输出窗口信息并终止。 

或使用 [xorg-xlsclients](<https://archlinux.org/packages/?name=xorg-xlsclients>)包 的 `xlsclients`。运行 `xlsclients -l` 可列出所有正运行在 Xwayland 的应用程序。 

或者也可以使用 [extramaus](<https://aur.archlinux.org/packages/extramaus/>)AUR。如果鼠标指针在 Xwayland 程序上，红色指针会随之移动。 

**提示：** 对于 KDE Plasma，还可以使用 [KWin 调试控制台](<../zh-cn/KDE.html#KWin_debug_console> "KDE")检查窗口。

##  图形库

### GTK

[gtk3](<https://archlinux.org/packages/?name=gtk3>)包 和 [gtk4](<https://archlinux.org/packages/?name=gtk4>)包 包已经提供了 Wayland 支持。GTK 默认使用 Wayland 后端，但是可以通过修改环境变量为 `GDK_BACKEND=x11` 覆盖默认设置切换到 Xwayland。 

关于主题问题，请参阅 [GTK#Wayland_后端](<../zh-cn/GTK.html#Wayland_%E5%90%8E%E7%AB%AF> "GTK")。 

### Qt

要在 [Qt](<../zh-cn/Qt.html> "Qt") 5 中启用 Wayland 支持，请安装 [qt5-wayland](<https://archlinux.org/packages/?name=qt5-wayland>)包。Qt 5 应用程序就会在 Wayland 会话下运行。 

虽然通常不需要，但若要显式使用 Wayland 插件运行 Qt 应用程序 [[7]](<https://wiki.qt.io/QtWayland#How_do_I_use_QtWayland.3F>)，请使用 `-platform wayland` 或 `QT_QPA_PLATFORM=wayland` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")。 

要在 Wayland 会话中强制使用 [X11](<../zh-cn/Xorg.html> "X11")，请使用 `QT_QPA_PLATFORM=xcb`。 

这对于某些不使用系统 Qt 实现的应用可能是必需的。`QT_QPA_PLATFORM="wayland;xcb"` 允许 Qt 在 Wayland 不可用时使用 xcb (X11) 插件 [[8]](<https://www.qt.io/blog/2018/05/29/whats-new-in-qt-5-11-for-the-wayland-platform-plugin>)。 

在某些混成器，例如sway，Qt 应用原生运行可能会有功能缺失。例如， KeepassXC 将无法最小化到托盘。在运行前安装qt5ct并设置`QT_QPA_PLATFORMTHEME=qt5ct`即可解决此问题。 

由于 [Qt WebEngine 在 Wayland 上使用分数缩放时出现错误尺寸和文本渲染问题](<https://bugreports.qt.io/browse/QTBUG-113574>)的 Qt WebEngine 错误，使用 Qt WebEngine 的应用程序（例如 [Calibre](<https://bugs.launchpad.net/calibre/+bug/2018658>)）可能会显示锯齿字体。一个解决方法是启动应用程序时设置 `QT_SCALE_FACTOR_ROUNDING_POLICY=RoundPreferFloor`，这可以防止应用程序窗口进行分数缩放。 

### Clutter

Clutter 工具包有 Wayland 后端支持，可以作为 Wayland 客户端运行。此后端支持已在 [clutter](<https://aur.archlinux.org/packages/clutter/>)AUR 中启用。 

要在 Wayland 上运行 Clutter 应用，请设置 `CLUTTER_BACKEND=wayland` 环境变量。 

### SDL

在 [SDL](<../zh-cn/SDL.html> "SDL")3 中，如果混成器支持 [fifo-v1 协议](<https://wayland.app/protocols/fifo-v1>)，则默认使用 Wayland [[9]](<https://github.com/libsdl-org/SDL/blob/8c54961de02d8f62ed155925cb334efcaa2d1f95/src/video/wayland/SDL_waylandvideo.c#L536C9-L536C20>)。否则，会先尝试 X11。可以将 `SDL_VIDEO_DRIVER` 环境变量设置为 `x11` 或 `wayland` 来强制使用其一（或者，使用优先级较低的下述 SDL2 环境变量）[[10]](<https://github.com/libsdl-org/SDL/blob/8c54961de02d8f62ed155925cb334efcaa2d1f95/docs/README-migration.md?plain=1#L802>)。 

[sdl2-compat](<https://archlinux.org/packages/?name=sdl2-compat>)包 遵循上述 SDL3 规则，但有[特定应用程序的例外](<https://github.com/libsdl-org/sdl2-compat/blob/8b85f95bbcc3411c78c1f2cbd62b23b7f96093c2/src/sdl2_compat.c#L504-L538>)。至于 SDL2 本身（例如 [sdl2](<https://aur.archlinux.org/packages/sdl2/>)AUR），请设置 `SDL_VIDEODRIVER=wayland`。`SDL_VIDEODRIVER="wayland,x11"` 允许 SDL2 在 Wayland 不可用时使用 X11 [[11]](<https://wiki.libsdl.org/SDL2/FAQUsingSDL>)。可能还需要安装 [libdecor](<https://archlinux.org/packages/?name=libdecor>)包 才能启用窗口装饰（例如在 GNOME 上）。 

参见[官方说明](<https://wiki.libsdl.org/SDL3/README-wayland>)。 

### GLFW

[glfw](<https://archlinux.org/packages/?name=glfw>)包 支持 Wayland，如果[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量") `XDG_SESSION_TYPE` 设置为 `wayland`，并且应用程序开发人员没有设置特定的后端，则使用 Wayland 后端。 

查看[源代码](<https://github.com/glfw/glfw/blob/3.4/src/platform.c#L87-L99>)以获取更多信息。 

### GLEW

如果 [glew-wayland-git](<https://aur.archlinux.org/packages/glew-wayland-git/>)AUR 包无法与所需的 GLEW 应用程序一起使用，则可以使用 [glew](<https://archlinux.org/packages/?name=glew>)包 和 Xwayland。参见 [FS#62713](<https://bugs.archlinux.org/task/62713>)。 

### EFL

Enlightenment 已[完全支持 Wayland](<https://www.enlightenment.org/about-wayland>)。 

要在 Wayland 上运行基于 EFL 的应用程序，请设置 `ELM_DISPLAY=wl`。 

### winit

winit 是 Rust 语言中的窗口处理库。默认使用 Wayland 后端，但可以通过修改环境变量将其切换到 Xwayland： 

  * 在 0.29.2 版本之前，设置 `WINIT_UNIX_BACKEND=x11`
  * 对于 0.29.2 及更高版本，取消设置 `WAYLAND_DISPLAY`，这将强制回退到使用 `DISPLAY` 变量的 X11 [[12]](<https://github.com/rust-windowing/winit/blob/baf10de95843f156b0fbad6b10c3137f1ebd4f1e/src/changelog/v0.29.md?plain=1#L134>)

### Electron

**注意：** 在 [Plasma](<../zh-cn/KDE.html> "KDE") 中，某些 Electron 应用程序可能在窗口上使用错误的图标（默认的 Wayland 图标），而在任务栏上使用正确的图标。使用特殊应用程序/窗口规则强制指定“桌面文件名”（即 `.desktop` 文件的文件名）可以绕过此问题。

使用命令行标志或环境变量可启用 Electron 的 Wayland 支持。 

####  命令行标志

**注意：** 某些应用程序不会将标志转发给 Electron，需要应用程序开发者提供解决方案。

关于启用 Electron Wayland 支持的命令行标志，请参见 [Chromium#原生 Wayland 上运行](<../zh-cn/Chromium.html#%E5%8E%9F%E7%94%9F_Wayland_%E4%B8%8A%E8%BF%90%E8%A1%8C> "Chromium")。但需要注意，命令行标志 `--ozone-platform-hint=auto` 自 Electron 38 起已不再有效。 

这些标志可以手动传递或[#通过配置文件添加](<#%E9%80%9A%E8%BF%87%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E6%B7%BB%E5%8A%A0>)。通过[编辑 .desktop 文件](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html#%E7%BC%96%E8%BE%91_.desktop_%E6%96%87%E4%BB%B6> "桌面项")可以每次通过桌面项启动时传递。 

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 旧版本的 Electron 需要 `--enable-features=WebRTCPipeWireCapturer`，但它从哪个版本开始默认启用？此外，非自由软件捆绑的 Electron 的默认行为可能是错误的。（在 [en:Talk:Wayland](<https://wiki.archlinux.org/title/Talk:Wayland> "en:Talk:Wayland") 中讨论）

Electron 默认启用通过 PipeWire 进行的 WebRTC 屏幕捕获。该捕获基于 [xdg-desktop-portal](<https://archlinux.org/packages/?name=xdg-desktop-portal>)包。 

顶部栏缺失的问题可以通过使用 `--enable-features=WaylandWindowDecorations` 来解决。这在 [GNOME](<../zh-cn/GNOME.html> "GNOME") 下通常是必需的（自 [electron17](<https://github.com/electron/electron/pull/29618>) 起支持）。 

#####  通过配置文件添加

Electron 读取 `~/.config/electron _XX_ -flags.conf`（ _XX_ 为 Electron 版本号）文件添加到命令行参数（一行一个），如果版本特定的文件不存在，则回退到全版本的 `~/.config/electron-flags.conf`。 

例如，将上述参数写入共享配置文件： 
    
    ~/.config/electron-flags.conf
    
    --enable-features=WaylandWindowDecorations
    --ozone-platform-hint=auto

**注意：** 这些配置文件仅对官方仓库的 Electron 软件包和使用这些 Electron 包的应用程序有效。对于自带 Electron 的软件包（如 [slack-desktop](<https://aur.archlinux.org/packages/slack-desktop/>)AUR）来说，这些配置文件是无效的。不过在某些情况下也有替代品，如 [slack-electron](<https://aur.archlinux.org/packages/slack-electron/>)AUR。

####  环境变量

使用 Electron 28 至 37 版本的应用程序可以使用[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量") `ELECTRON_OZONE_PLATFORM_HINT`，将其设置为 `auto` 或 `wayland`。 

如果同时指定，命令行标志优先。 

### Java

[Java](<../zh-cn/Java.html> "Java") 平台的开源实现 OpenJDK 尚未原生支持 Wayland。在 [Wakefield](<https://openjdk.java.net/projects/wakefield/>) 项目（旨在在 OpenJDK 中实现 Wayland）可用之前，可以使用 Xwayland。 

参见 [Debian:Wayland#Java Programs (supported since OpenJDK 16?)](<https://wiki.debian.org/Wayland#Java_Programs_.28supported_since_OpenJDK_16.3F.29> "debian:Wayland")： 

    从 OpenJDK 16 开始，JRE 可以动态加载 GTK3（支持 Wayland），根据此[讨论](<https://stackoverflow.com/questions/39197208/java-gui-support-on-wayland>)，这似乎是支持的。
    可以设置 `_JAVA_AWT_WM_NONREPARENTING` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")为 "1" 以修复应用程序启动时出现空白屏幕的问题。

由于 Xwayland 没有与 Wayland 完全的功能对等，[WLToolkit](<https://wiki.openjdk.org/display/wakefield/Pure+Wayland+toolkit+prototype>) 可以在 Wakefield 未准备好时填补空白。可以通过 `-Dawt.toolkit.name=WLToolkit` 激活。一些程序支持它。 

##  输入法

### Fcitx 5

参见 [Fcitx 5#Wayland](<../zh-cn/Fcitx_5.html#Wayland> "Fcitx 5")。 

### IBus

参见 [[13]](<https://github.com/ibus/ibus/wiki/WaylandDesktop>)。 

##  提示与技巧

###  自动化

  * [ydotool](<https://github.com/ReimuNotMoe/ydotool>) ([ydotool](<https://archlinux.org/packages/?name=ydotool>)包) - 通用的命令行自动化工具 (不限于 Wayland)。[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")/[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `ydotool.service` [用户单元](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "用户单元")。参见 [ydotoold(8)](<https://man.archlinux.org/man/ydotoold.8>)，[ydotool(1)](<https://man.archlinux.org/man/ydotool.1>)。
  * [wtype](<https://github.com/atx/wtype>) ([wtype](<https://archlinux.org/packages/?name=wtype>)包) - 适用 Wayland 的 xdotool type。参见 [wtype(1)](<https://man.archlinux.org/man/wtype.1>)。
  * [keyboard](<https://github.com/boppreh/keyboard>) \- 可在 Windows 和 Linux 上稳定工作、实验性支持 OS X 的 Python 库。另请参见[鼠标 (mouse)](<https://github.com/boppreh/mouse>) 库。
  * [wlrctl](<https://git.sr.ht/~brocellous/wlrctl>) ([wlrctl](<https://aur.archlinux.org/packages/wlrctl/>)AUR) - 用于各种 wlroots 扩展的命令行工具（支持 foreign-toplevel-management、virtual-keyboard、virtual-pointer）。

###  重新映射键盘或鼠标按键

参见[输入重映射工具](<../zh-cn/%E8%BE%93%E5%85%A5%E9%87%8D%E6%98%A0%E5%B0%84%E5%B7%A5%E5%85%B7.html> "输入重映射工具")。 

###  录制

参见[屏幕捕获#屏幕录制](<../zh-cn/%E5%B1%8F%E5%B9%95%E6%8D%95%E8%8E%B7.html#%E5%B1%8F%E5%B9%95%E5%BD%95%E5%88%B6> "屏幕捕获")和[屏幕捕获#通过X11应用程序录制Wayland窗口](<../zh-cn/%E5%B1%8F%E5%B9%95%E6%8D%95%E8%8E%B7.html#%E9%80%9A%E8%BF%87X11%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%BD%95%E5%88%B6Wayland%E7%AA%97%E5%8F%A3> "屏幕捕获")。 

###  应用程序关闭后保留剪贴板内容

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[剪贴板](<../zh-cn/%E5%89%AA%E8%B4%B4%E6%9D%BF.html> "剪贴板")。**

**附注：** 这是 Xorg 上的标准行为。还有许多其他剪贴板管理器。（在 [Talk:Wayland](<../zh-cn/Talk:Wayland.html>) 中讨论）

由于 Wayland 的设计理念，剪贴板数据存储在源客户端的内存中。当客户端关闭时，剪贴板数据将丢失。您可以使用 [wl-clip-persist](<https://archlinux.org/packages/?name=wl-clip-persist>)包 来解决这个问题，它在后台运行以读取剪贴板数据并将其存储在自己的内存中，与源客户端分离。 

###  将混成器作为 systemd 服务自动启动

**提示：**[通用Wayland会话管理器](<../zh-cn/%E9%80%9A%E7%94%A8Wayland%E4%BC%9A%E8%AF%9D%E7%AE%A1%E7%90%86%E5%99%A8.html> "通用Wayland会话管理器")可自动为混成器生成 systemd 单元，此外还可用于[将图形应用程序与 systemd 集成](<../zh-cn/%E9%80%9A%E7%94%A8Wayland%E4%BC%9A%E8%AF%9D%E7%AE%A1%E7%90%86%E5%99%A8.html#%E9%80%9A%E7%94%A8Wayland%E4%BC%9A%E8%AF%9D%E7%AE%A1%E7%90%86%E5%99%A8#%E8%BD%AF%E4%BB%B6%E4%B8%8E%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8> "通用Wayland会话管理器")。

如果不想使用[显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")或 [shell](<../zh-cn/%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%A7%A3%E9%87%8A%E5%99%A8.html> "Shell")，可以通过 [systemd](<../zh-cn/Systemd.html> "Systemd") 自动启动 Wayland 混成器。调整 `ExecStart` 行启动指定混成器。以下是 [KDE Plasma](<../zh-cn/KDE_Plasma.html> "KDE Plasma") 的示例: 
    
    /etc/systemd/system/wayland-compositor.service
    
    [Unit]
    After=graphical.target systemd-user-sessions.service modprobe@drm.service
    Conflicts=getty@tty1.service
    [Service]
    User=_username_
    WorkingDirectory=~
    PAMName=login
    TTYPath=/dev/tty1
    UnsetEnvironment=TERM
    StandardOutput=journal
    ExecStart=/usr/lib/plasma-dbus-run-session-if-needed /usr/bin/startplasma-wayland
    [Install]
    WantedBy=graphical.target

###  在基于 wlroots 的混成器上使用另一个渲染器

您可以通过为基于 wlroots 的混成器设定 `WLR_RENDERER` 环境变量以使用另一个 [wlroots 渲染器](<https://gitlab.freedesktop.org/wlroots/wlroots/-/tree/master/render>)如 vulkan。请参阅 [wlroots 文档](<https://gitlab.freedesktop.org/wlroots/wlroots/-/blob/master/docs/env_vars.md>)以查找可用的渲染器。 

##  故障排除

###  颜色校正

请参阅[背光#色彩校正](<../zh-cn/%E8%83%8C%E5%85%89.html#%E8%89%B2%E5%BD%A9%E6%A0%A1%E6%AD%A3> "背光")。 

###  慢动作、图形显示故障和崩溃

Gnome-shell 用户从 X 切换到 Wayland 时可能会遇到此问题。根本原因之一是可能用户自己为基于 Xorg 的 gnome-shell 设置了 `CLUTTER_PAINT=disable-clipped-redraws:disable-culling` 变量。只需尝试将变量从 `/etc/environment` 或其它 rc 文件中移除，即可查看是否一切恢复正常。 

###  远程显示

  * [sway](<../zh-cn/Sway.html> "Sway") 使用的[wlroots0.18](<https://archlinux.org/packages/?name=wlroots0.18>)包 和[wlroots0.19](<https://archlinux.org/packages/?name=wlroots0.19>)包 从 0.10 版本开始通过 [wayvnc](<https://archlinux.org/packages/?name=wayvnc>)包 提供了一个 VNC 后端。RDP 后端则已被移除。[[14]](<https://github.com/swaywm/wlroots/releases/tag/0.10.0>)
  * 目前 [mutter](<https://archlinux.org/packages/?name=mutter>)包 在编译时就启用了远程桌面功能，详情请参阅 [[15]](<https://wiki.gnome.org/Projects/Mutter/RemoteDesktop>) 和 [gnome-remote-desktop](<https://archlinux.org/packages/?name=gnome-remote-desktop>)包。
  * [krfb](<https://archlinux.org/packages/?name=krfb>)包 为 [kwin](<https://archlinux.org/packages/?name=kwin>)包 提供了一个 VNC 服务器。`krfb-virtualmonitor` 可用于将另一台设备设置为额外的显示器。
  * 在 2013 年 Weston 合并了对 FreeRDP 的支持，可通过编译标志 (compile flag) 启用。[weston](<https://archlinux.org/packages/?name=weston>)包 自 6.0.0 版本开始启用了 FreeRDP。
  * [waypipe](<https://archlinux.org/packages/?name=waypipe>)包 (或 [waypipe-git](<https://aur.archlinux.org/packages/waypipe-git/>)AUR) 是适用于 Wayland 应用的透明代理，可通过封装的命令在 [SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH") 上运行。 
    * 以下是一个在 Plasma 下启动远程 KDE kcalc 的示例：

    $ waypipe ssh example.local env QT_QPA_PLATFORM=wayland QT_QPA_PLATFORMTHEME=KDE dbus-launch kcalc

###  游戏、远程桌面和虚拟机窗口中的输入捕获问题

与 Xorg 不同的是，Wayland 并不允许独占输入设备捕获 (也被称为主动捕获或显式捕获，比如[键盘](<https://tronche.com/gui/x/xlib/input/XGrabKeyboard.html>)、[鼠标](<https://tronche.com/gui/x/xlib/input/XGrabPointer.html>)等设备)。Wayland 依赖混成器传递键盘快捷键，并将指针设备限制在应用窗口中。 

输入捕获方式的变化破坏了当前应用程序的行为，意味着： 

  * 热键组合和修饰符输入会被混成器捕获，并且不会发送到远程桌面和虚拟机窗口中。
  * 鼠标指针将不会被限制在应用程序的窗口中，这可能会导致视差效应，即虚拟机或远程桌面的窗口内鼠标指针的位置与主机的鼠标指针发生偏差。

Wayland 通过为 Wayland 和 Xwayland 添加协议扩展来解决此问题。为此 Wayland 混成器需要添加对这些扩展的支持。如果是本地 Wayland 客户端，其使用的部件工具集 (widget toolkits，比如 GTK，Qt) 需要支持这些插件；如果没有使用部件工具集，则需要支持应用程序本身。如果是 Xorg 应用程序，则不需要改变应用程序或者部件工具集，因为 Xwayland 的支持就足够了。 

[wayland-protocols](<https://archlinux.org/packages/?name=wayland-protocols>)包 中已经包含了这些扩展, 并由 [xorg-xwayland](<https://archlinux.org/packages/?name=xorg-xwayland>)包 支持。 

相关的扩展有： 

  * [Xwayland 键盘捕获协议](<https://gitlab.freedesktop.org/wayland/wayland-protocols/-/blob/main/unstable/xwayland-keyboard-grab/xwayland-keyboard-grab-unstable-v1.xml>)
  * [混成器快捷键禁止协议](<https://gitlab.freedesktop.org/wayland/wayland-protocols/-/blob/main/unstable/keyboard-shortcuts-inhibit/keyboard-shortcuts-inhibit-unstable-v1.xml>)
  * [相对指针协议](<https://gitlab.freedesktop.org/wayland/wayland-protocols/-/blob/main/unstable/relative-pointer/relative-pointer-unstable-v1.xml>)
  * [指针约束协议](<https://gitlab.freedesktop.org/wayland/wayland-protocols/-/blob/main/unstable/pointer-constraints/pointer-constraints-unstable-v1.xml>)

支持的 Wayland 混成器有： 

  * Mutter，[GNOME](<../zh-cn/GNOME.html> "GNOME") 的混成器 (窗口管理器) ，[从 3.28 版本](<https://bugzilla.gnome.org/show_bug.cgi?id=783342>)开始支持
  * wlroots 支持相对指针协议和指针约束协议
  * Kwin 
    * [KDE#X11快捷键在Wayland上冲突](<../zh-cn/KDE.html#X11%E5%BF%AB%E6%8D%B7%E9%94%AE%E5%9C%A8Wayland%E4%B8%8A%E5%86%B2%E7%AA%81> "KDE")
    * [键盘快捷键禁止](<https://invent.kde.org/plasma/kwin/-/blob/master/src/wayland/keyboard_shortcuts_inhibit_v1_interface.cpp>)

支持的部件工具集有： 

  * GTK，从 3.22.18 版本开始支持。

###  GTK 主题没有生效

请查看 <https://github.com/swaywm/sway/wiki/GTK-3-settings-on-Wayland>. 

###  避免加载 NVIDIA 模块

在 Wayland 混成器（如 [sway](<../zh-cn/Sway.html> "Sway")）启动之前，将 `__EGL_VENDOR_LIBRARY_FILENAMES=/usr/share/glvnd/egl_vendor.d/50_mesa.json` 添加到系统[环境变量](<../zh-cn/Environment_variable.html> "Environment variable")中。 

###  放大/表面缩放

屏幕放大问题尚未解决，2022 年中合并了一个拉取请求[提供了 wp-surface-scale 协议](<https://gitlab.freedesktop.org/wayland/wayland-protocols/-/merge_requests/145>)。 

###  Wayland 卡顿/延迟（自内核 6.11.2，AMD）

在此问题在未来的内核版本中修复之前，一个临时解决方案是在 cmdline 中添加 `amdgpu.dcdebugmask=0x400`。 

参见：<https://community.frame.work/t/wayland-lag-stuttering-since-kernel-6-11-2/59422>

###  切换工作区/虚拟桌面时游戏/应用程序被挂起

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 如果找到，请在此处添加更多信息并引用上游文档：该功能难以捉摸且似乎文档记录不佳。 (在 [en:Talk:Wayland](<https://wiki.archlinux.org/title/Talk:Wayland> "en:Talk:Wayland") 中讨论)

当切换工作区/虚拟桌面或使用 `Alt+Tab` 时，游戏（以及可能的其他图形应用程序）会被挂起，进入某种奇怪的状态，并（部分）停止运行。这包括 VRR 应用程序和开启了 VSync 的应用程序，但可能不仅限于此。症状包括音频（部分）中断、游戏无法进行、ping 大幅上升或掉线，但仅在游戏窗口未处于焦点时才会出现。 

某些游戏可能可以通过切换到窗口模式来规避此问题，但有些则不行。这在需要大量使用网页浏览、文档和第三方工具的更复杂游戏中极其烦人，或者当游戏因某种原因被中断时也是如此。 

可能的解决方法包括设置环境变量 `MESA_VK_WSI_PRESENT_MODE=immediate` 和/或 `vk_xwayland_wait_ready=false`，但设置这些会破坏所有 VSync 或 VRR 实现。 

##  另见

  * [Wayland 在线文档](<https://wayland.freedesktop.org/docs/html/>)（英文）
  * [官方仓库](<https://gitlab.freedesktop.org/wayland>)（英文）
  * [Fedora：如何排查 Wayland 问题](<https://fedoraproject.org/wiki/How_to_debug_Wayland_problems> "fedora:How to debug Wayland problems")（英文）
  * [我们现在是 Wayland 了！](<https://wearewaylandnow.com/>)（英文）- "Wayland 可用了吗？"的更新版本
  * [Wayland 项目汇总](<https://awesomeopensource.com/projects/wayland>)（英文）
  * [光标主题](<../zh-cn/%E5%85%89%E6%A0%87%E4%B8%BB%E9%A2%98.html> "光标主题")
  * [Arch Linux 论坛讨论](<https://bbs.archlinux.org/viewtopic.php?id=107499>)（英文）（页面将持续关注 Wayland 信息，如有兴趣请留意）
  * [i3 迁移指南 - i3 上常用 X11 应用的 Wayland 替代品](<https://github.com/swaywm/sway/wiki/i3-Migration-Guide#common-x11-apps-used-on-i3-with-wayland-alternatives>)（英文）
  * [Wayland Explorer - 阅读 Wayland 文档的更好方法](<https://wayland.app/protocols/>)（英文）
  * [如何判断应用程序是否在使用 Xwayland](<https://askubuntu.com/questions/1393618/how-can-i-tell-if-an-application-is-using-xwayland>)（英文）
