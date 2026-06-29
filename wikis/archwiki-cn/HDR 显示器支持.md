**翻译状态：**

  * 本文（或部分内容）译自 [HDR monitor support](<https://wiki.archlinux.org/title/HDR_monitor_support> "arch:HDR monitor support")，最近一次同步于 2025-07-30，若英文版本有所[更改](<https://wiki.archlinux.org/title/HDR_monitor_support?diff=0&oldid=842185>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/HDR_monitor_support_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Steam](<../zh-cn/Steam.html> "Steam")
  * [游戏](<../zh-cn/%E6%B8%B8%E6%88%8F.html> "游戏")
  * [Gamescope](<../zh-cn/Gamescope.html> "Gamescope")

HDR 支持已[合并](<https://gitlab.freedesktop.org/wayland/wayland-protocols/-/merge_requests/14>)到 [Wayland](<../zh-cn/Wayland.html> "Wayland") 协议中，部分混成器已实现该功能。而 [Xorg](<../zh-cn/Xorg.html> "Xorg") [没有支持 HDR 的计划](<https://gitlab.freedesktop.org/xorg/xserver/-/issues/1037#note_521100>)。 

##  要求

  * 支持 HDR 的显示器。尽管现在有许多宣称支持 HDR 的显示器，但采用边缘照明局部调光（edge-lit local dimming）的设备提供的 HDR 体验可能无法令人满意。更多信息请参阅 [Local Dimming on TVs](<https://www.rtings.com/tv/tests/picture-quality/local-dimming>)。
  * 支持 HDR 的显卡驱动：已确认 [AMDGPU](<../zh-cn/AMDGPU.html> "AMDGPU") 和 [NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA")（550.54.14 及以后的版本）可正常工作。 
    * [NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA") 565.57.01 之前的版本存在一个可能导致 HDR 模式下色彩表现不正确或偏淡的 bug。[[1]](<https://www.nvidia.com/en-us/drivers/details/233008/>)
    * [Intel 图形处理器](<../zh-cn/Intel_%E5%9B%BE%E5%BD%A2%E5%A4%84%E7%90%86%E5%99%A8.html> "Intel 图形处理器")自内核版本 5.12 起为第 9 代及更新的核显提供实验性的 HDR 支持[[2]](<https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=1a911350dd6c777b4a08ca60fe6e2249fd3c254a>)，但据[报告](<https://www.reddit.com/r/linux/comments/1atnp5k/comment/kqzj69z/>)其实现不完整。
  * 兼容的混成器，参见 [#混成器](<#%E6%B7%B7%E6%88%90%E5%99%A8>)。
  * 兼容的应用程序，参见 [#应用程序](<#%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F>)
  * 支持 HDR 的 Vulkan WSI（窗口系统集成），参见 [#Vulkan HDR WSI](<#Vulkan_HDR_WSI>)。

##  配置

### Vulkan HDR WSI

对于 [NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA") 和版本 25 之前的 [mesa](<https://archlinux.org/packages/?name=mesa>)包，需要安装 [vk-hdr-layer-kwin6-git](<https://aur.archlinux.org/packages/vk-hdr-layer-kwin6-git/>)AUR 才能支持 `VK_EXT_swapchain_colorspace` 和 `VK_EXT_hdr_metadata` 这两个 Vulkan 扩展 [[3]](<https://www.phoronix.com/news/Mesa-Vulkan-WSI-HDR-CM>) [[4]](<https://github.com/Zamundaaa/VK_hdr_layer?tab=readme-ov-file#vulkan-wayland-hdr-wsi-layer>)。没有这两个扩展则无法通过 Vulkan API 使用 HDR。 

通过设置 `ENABLE_HDR_WSI=1` 来启用 Wayland 下的 Vulkan HDR WSI。不建议全局启用，应分别为每个需要使用 HDR 的游戏或其它应用程序启用。 

###  混成器

####  KWin (KDE Plasma)

参见 [KDE#HDR](<../zh-cn/KDE.html#HDR> "KDE")。 

#### Hyprland

首先确保 [hyprland](<https://archlinux.org/packages/?name=hyprland>)包 的版本 ≥ 0.47.0 并配置 `xx_color_management_v4` 变量为 true。 

##### Monitor v1

在 Hyprland 配置文件中对应显示器的配置行末尾追加：`, bitdepth, 10, cm, hdr`

**注意：** Monitor v2 是通过“monitorv2”声明的，Monitor v1 则直接通过“monitor”声明。

##### Monitor v2

在对应显示器的配置中添加以下内容： 
    
       supports_wide_color = 1
       supports_hdr = 1
    
更多设置请参阅 [Hyprland Wiki](<https://wiki.hypr.land/Configuring/Monitors/#monitor-v2>)。 

更多信息可在 [Hyprland 实验性功能文档](<https://wiki.hyprland.org/Configuring/Variables/#experimental>)和 [Hyprland 显示器文档](<https://wiki.hypr.land/Configuring/Monitors/#color-management-presets>)中找到。 

#### GNOME

首先确保 [mutter](<https://archlinux.org/packages/?name=mutter>)包 的版本 ≥ 48.0。 

在 GNOME 的显示设置中启用 HDR。每个显示器都有 单独的 HDR 开关，在分辨率和刷新率设置旁。 

**注意：** 在 GNOME 中使用 Gamescope HDR 时会出现“褪色”现象，因为 GNOME 缺少对 scRGB 和 `frog-color-management-v1` 协议的支持 [[5]](<https://gitlab.gnome.org/GNOME/mutter/-/issues/4083>) [[6]](<https://github.com/ValveSoftware/gamescope/issues/1825>)。参见 [#使用 Gamescope](<#%E4%BD%BF%E7%94%A8_Gamescope>)

####  Steam 的 Gamescope 会话

Valve 的混成器 [Gamescope](<../zh-cn/Gamescope.html> "Gamescope") 提供了实验性 HDR 支持。按以下步骤可尝试在 Gamescope 环境中运行 Steam 客户端： 

**提示：** 建议使用 [AMDGPU](<../zh-cn/AMDGPU.html> "AMDGPU") 显卡驱动运行 Gamescope⸺已知 [NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA") 驱动存在严重问题。

  * 安装 [gamescope](<https://archlinux.org/packages/?name=gamescope>)包 和 [gamescope-session-steam-git](<https://aur.archlinux.org/packages/gamescope-session-steam-git/>)AUR。
  * 可创建可选配置文件 `~/.config/environment.d/gamescope-session.conf`，内容如下：
        
        if [ "$XDG_SESSION_DESKTOP" = "gamescope" ] ; then
            SCREEN_WIDTH=1920       # 屏幕宽度
            SCREEN_HEIGHT=1080      # 屏幕高度
            CONNECTOR=*,eDP-1       # 显示接口
            CLIENTCMD="steam -gamepadui -pipewire-dmabuf"  # 客户端启动命令
            GAMESCOPECMD="/usr/bin/gamescope --hdr-enabled --hdr-itm-enable \
            --hide-cursor-delay 3000 --fade-out-duration 200 --xwayland-count 2 \
            -W $SCREEN_WIDTH -H $SCREEN_HEIGHT -O $CONNECTOR"  # Gamescope 启动参数
        fi
        
    * 需将分辨率数值设置为实际值（可通过 `xrandr --query` 命令查询显示设备参数）。
    * 若未自动识别显示接口，需手动设置 `CONNECTOR` 参数。

现在可通过以下任一方式启动 Gamescope： 

#####  通过显示管理器

登出，在[显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")中选择“Steam Big Picture”登录。 

#####  通过控制台

  1. 按下 `Ctrl+Alt+F _x_` 进入一个新的 TTY。
  2. 登录后执行 `gamescope-session-plus steam` 在 Gamescope 中启动 [Steam 独立会话](<https://github.com/ChimeraOS/gamescope-session>)。 
     * 若网络不可用，安装并[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") [NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager")。

#####  配置 Steam

  1. 在常规设置中的“显示”部分，启用 HDR 和实验性 HDR 支持。
  2. 选择一款支持 HDR 的游戏，点击旁边的齿轮图标。
  3. 将兼容性设置为强制使用 Proton 8.0 或 Proton Experimental。
  4. 将游戏分辨率设置为与显示器一致，否则将默认以 Steam Deck 的分辨率启动。
  5. 点击“开始游戏”启动游戏。进入游戏后检查设置中的 HDR 选项，并将其启用。
  6. 若需切换回正常桌面会话，请在 Steam 菜单中选择“电源” -> “切换到桌面模式”。

#### COSMIC

[COSMIC](<../zh-cn/COSMIC.html> "COSMIC") 的开发者在[博文](<https://blog.system76.com/post/may-flowers-spring-cosmic-showers>)中承诺将在初始稳定版本中加入 HDR 支持。 

###  应用程序

####  游戏

#####  Wine/Proton

通过 [Wine](<../zh-cn/Wine.html> "Wine") 或 [Steam Proton](<../zh-cn/Steam.html#Proton_Steam-Play> "Steam") 实现 HDR 需要 [DXVK](<../zh-cn/Wine.html#DXVK> "Wine")（2.1 及以上版本）或 [VKD3D-Proton](<../zh-cn/Wine.html#VKD3D-Proton> "Wine")（2.8 及以上版本），具体的依赖视游戏所使用的 DirectX 版本而定。 

**提示：** 建议使用 Proton 8.0 及以上版本，或 Proton GE 44+。这些版本均包含符合要求的 DXVK 和 VKD3D。

######  不使用 Gamescope

若不使用 Gamescope 启用 HDR，需要运行包含 Wayland 驱动的 Wine 构建版本。 

**注意：** Wine 的原生 [Wayland](<../zh-cn/Wayland.html> "Wayland") 驱动仍属实验性质，具体游戏表现可能优于也可能劣于 Xwayland。

  * [proton-ge-custom](<https://github.com/GloriousEggroll/proton-ge-custom>)：安装 [proton-ge-custom-bin](<https://aur.archlinux.org/packages/proton-ge-custom-bin/>)AUR，并设置 `PROTON_ENABLE_WAYLAND=1` 与 `PROTON_ENABLE_HDR=1` [[7]](<https://github.com/GloriousEggroll/proton-ge-custom/releases/tag/GE-Proton10-1>)。

**注意：**`PROTON_ENABLE_HDR=1` 实际上设置的是 `DXVK_HDR=1` [[8]](<https://github.com/GloriousEggroll/proton-ge-custom/blob/master/proton#L1741>)。

  * [wine-tkg](<https://github.com/Frogging-Family/wine-tkg-git>)：安装 wine-tkg，设置 `DXVK_HDR=1`，并取消设置环境变量 `DISPLAY`。

  * [proton-cachyos](<https://github.com/cachyos/proton-cachyos>) 或 [wine-cachyos](<https://github.com/CachyOS/wine-cachyos>)：安装 [proton-cachyos](<https://aur.archlinux.org/packages/proton-cachyos/>)AUR、[wine-cachyos-opt](<https://aur.archlinux.org/packages/wine-cachyos-opt/>)AUR、[wine-cachyos](<https://aur.archlinux.org/packages/wine-cachyos/>)AUR 三者之一，并设置 `PROTON_ENABLE_WAYLAND=1` 与 `DXVK_HDR=1` [[9]](<https://www.reddit.com/r/linux_gaming/comments/1km81f4/proton_cachy_10_released_native_wayland_gaming/>)。

**提示：** 你也可以使用 [protonup-qt](<https://aur.archlinux.org/packages/protonup-qt/>)AUR 将上述的 Wine 构建轻松安装到 Lutris、Bottles 或 Steam 中。

######  使用 Gamescope

Gamescope 正常启用 HDR 需要混成器支持 scRGB，且支持 `xx-color-management-v4`、[`frog-color-management-v1`](<https://gitlab.freedesktop.org/wayland/wayland-protocols/-/merge_requests/14>) 两个协议之一。 

因此，Gamescope 无法与 [vk-hdr-layer-kwin6-git](<https://aur.archlinux.org/packages/vk-hdr-layer-kwin6-git/>)AUR 一起使用。请确保没有将 `ENABLE_HDR_WSI` 设置为 `1`。 

根据需要，有多种方式使用 Gamescope： 

  * 使用 Gamescope 启动 Steam。使用该方式，从 Steam 启动的所有游戏都会启用 HDR，但 Steam 和这些游戏将被运行在一个 Gamescope 窗口内：

    $ gamescope --hdr-enabled --steam -- env DXVK_HDR=1 steam
    
  * 在 Steam 设置中使用以下“启动选项”，为通过 Steam 启动的每个游戏启用 HDR：

    $ DXVK_HDR=1 gamescope -f --hdr-enabled -- %command%
    
  * 在 Gamescope 中启动非 Steam 游戏：

    $ DXVK_HDR=1 gamescope -f --hdr-enabled -- _可执行文件_
    
**注意：** 默认情况下，Gamescope 会以 1280x720 分辨率启动。若需自定义分辨率，可使用 `-W`（宽）和 `-H`（高）参数设置需要的分辨率。

##### RetroArch

RetroArch 目前仅在 Git 版本 [retroarch-git](<https://aur.archlinux.org/packages/retroarch-git/>)AUR 中支持 HDR。请在 RetroArch 的视频设置中启用 HDR。 
    
    $ retroarch
    
#####  原生 SDL

要运行使用 SDL 的原生游戏并启用 HDR，请设置 `SDL_VIDEODRIVER=wayland`。 

例如运行 Quake II RTX： 
    
    $ SDL_VIDEODRIVER=wayland quake2rtx
    
#### mpv

为了获得最佳图像质量，mpv 的维护者推荐使用 `gpu-next` 输出模式 [[10]](<https://github.com/mpv-player/mpv/discussions/16105#discussioncomment-12629196>)。 

**注意：** 这需要支持 HDR 的 Vulkan WSI，参见 [#Vulkan HDR WSI](<#Vulkan_HDR_WSI>)。
    
    $ mpv --vo=gpu-next --target-colorspace-hint --gpu-api=vulkan --gpu-context=waylandvk "path/to/video"
    
其他启用 [Wayland HDR 支持](<https://github.com/mpv-player/mpv/discussions/16105#discussioncomment-12619072>)的方式包括使用 `dmabuf-wayland` 和 `drm` 视频输出。 
    
    $ mpv --vo=dmabuf-wayland "path/to/video"
    
  * 在 tty 终端下，也可以使用：

    $ mpv --vo=drm "path/to/video"
    
#### Firefox

[firefox](<https://archlinux.org/packages/?name=firefox>)包 从 138.0 版本开始引入了可用的实验性 HDR 支持，通过隐藏的配置项 `gfx.wayland.hdr` 启用。可在 `about:config` 中启用。 

稳定的 HDR 支持仍在开发中 [[11]](<https://bugzilla.mozilla.org/show_bug.cgi?id=hdr>) [[12]](<https://bugzilla.mozilla.org/show_bug.cgi?id=1642854>)。 

#### Chromium

[chromium](<https://archlinux.org/packages/?name=chromium>)包 目前正在开发 HDR 支持 [[13]](<https://chromium-review.googlesource.com/c/chromium/src/+/6771393>)。 

##  提示与技巧

###  HDR 视频样本

[Kodi](<../zh-cn/Kodi.html> "Kodi") 的 Wiki 提供了一份[合理使用的 HDR 视频样本列表](<https://kodi.wiki/view/Samples#4K_\(UltraHD\)_&_HDR_Formats>)，可使用支持 HDR 的视频播放器（如 [#mpv](<#mpv>)）播放来测试 HDR 输出效果。 

##  问题解决

###  启用 HDR10 时屏幕共享异常

Pipewire 会尝试以 BGRA 格式进行流传输，但由于 WebRTC 当前无法解析该格式，因此会导致异常。具体表现为抛出 `ParamId:EnumFormat: 0:0 Invalid argument` 错误，并导致该应用的 WebRTC 套接字崩溃 [[14]](<https://github.com/hyprwm/xdg-desktop-portal-hyprland/issues/52>)。 

##  另请参阅

  * [X.Org 开发者大会 2022｜Harry Wentland：“HDR 更难吗？”](<https://www.youtube.com/watch?t=21171&v=yTO8QRIfOjA>)（英文视频）
  * [wlroots/wlroots｜HDR10 支持](<https://gitlab.freedesktop.org/wlroots/wlroots/-/issues/3941>)（英文）
  * [Xaver Hugl 的博客｜关于 KWin 中 HDR 与色彩管理的最新进展](<https://zamundaaa.github.io/wayland/2023/12/18/update-on-hdr-and-colormanagement-in-plasma.html>)（英文）
