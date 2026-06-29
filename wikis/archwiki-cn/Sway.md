**翻译状态：**

  * 本文（或部分内容）译自 [Sway](<https://wiki.archlinux.org/title/Sway> "arch:Sway")，最近一次同步于 2026-04-29，若英文版本有所[更改](<https://wiki.archlinux.org/title/Sway?diff=0&oldid=872430>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Sway_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")

Sway（缩写自 **S** irCmpwn's **Way** land compositor[[1]](<https://github.com/swaywm/sway/blob/f0ddf6d74c98ba6c502783b8f41be859c56712c9/README.md>)）是一款专为 [Wayland](<../zh-cn/Wayland.html> "Wayland") 设计的合成器，旨在与 [i3](<../zh-cn/I3.html> "I3") 完全兼容。根据[官网](<https://swaywm.org>)所述： 

    Sway 是 Wayland 的合成器，也是 x11 的 i3 窗口管理器的替代品。它可以根据您现有的 i3 配置工作，并支持 i3 的大部分特性以及一些附加功能

若您喜欢视觉效果，也可以试试 [swayfx](<https://aur.archlinux.org/packages/swayfx/>)AUR，这是一个带有视觉效果的 Sway 分支。 

Sway 的另一个分支 [sway-scroll-git](<https://aur.archlinux.org/packages/sway-scroll-git/>)AUR 具有滚动布局（如同 PaperWM 和 [niri](<https://archlinux.org/packages/?name=niri>)包）。还支持动画效果、窗口内容缩放和概览模式。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [sway](<https://archlinux.org/packages/?name=sway>)包。由于依赖关系紧密，请在更新 _sway_ 时始终更新 _wlroots_ 。 

**注意：** 所有专有显卡驱动程序都[不受支持](<https://github.com/swaywm/sway/wiki#nvidia-users>)，包括 [NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA")。在 NVIDIA 驱动程序版本 495 之后，需要启用[内核级显示模式设置](<../zh-cn/NVIDIA.html#DRM_%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE> "NVIDIA")并在运行 sway 时附加 `--unsupported-gpu` 参数。

您还可以安装 [swaylock](<https://archlinux.org/packages/?name=swaylock>)包、 [swayidle](<https://archlinux.org/packages/?name=swayidle>)包 和 [swaybg](<https://archlinux.org/packages/?name=swaybg>)包，用以锁定屏幕、设定空闲管理和设置壁纸。 

默认的应用程序启动器为 [wmenu](<https://archlinux.org/packages/?name=wmenu>)包，默认的[终端模拟器](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E5%B7%A5%E5%85%B7.html#%E7%BB%88%E7%AB%AF%E6%A8%A1%E6%8B%9F%E5%99%A8> "终端模拟器")是 [foot](<../zh-cn/Foot.html> "Foot")。在启动 _sway_ 之前，建议安装它们或在配置文件中设置新的启动器和终端。您可在 Sway wiki 的[迁移指南](<https://github.com/swaywm/sway/wiki/i3-Migration-Guide>)上找到一些 i3 实用程序的其他 Wayland 兼容替代品。 

##  启动

Sway 在启动之前需要访问您的硬件设备（如键盘、鼠标和显卡），这些硬件设备的集合称为 seat，如同 [sd-login(3) § DEFINITION OF TERMS](<https://man.archlinux.org/man/sd-login.3#DEFINITION_OF_TERMS>) 的 seat 小节所述。 

在 Arch Linux 上，Sway 可以使用以下任一方式访问您的 seat。 

  * [systemd-logind(8)](<https://man.archlinux.org/man/systemd-logind.8>) 和 [polkit](<https://archlinux.org/packages/?name=polkit>)包
  * [seatd](<https://archlinux.org/packages/?name=seatd>)包，会作为 [wlroots0.19](<https://archlinux.org/packages/?name=wlroots0.19>)包的依赖与 Sway 一起安装

若 `polkit` 已安装在您的系统上， Sway 应会自动访问你的 seat。 

若 `polkit` 未安装在您的系统上，并且您想使用 `seatd` 来替代，请将您添加到 `seat` [用户组](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "用户和用户组")并[启用/启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用/启动") `seatd.service`，然后重新登录。 

您可以选择以下方法之一来启动 Sway。 

###  手动启动

要启动 Sway，只需在 Linux 终端执行 `sway`。 

###  自动启动

与 X 类似，可以通过将以下内容添加到 shell 初始化文件来启动 Sway（请参阅[命令行解释器#登录 Shell](<../zh-cn/%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%A7%A3%E9%87%8A%E5%99%A8.html#%E7%99%BB%E5%BD%95_Shell> "命令行解释器")）： 
    
    if [ -z "$WAYLAND_DISPLAY" ] && [ -n "$XDG_VTNR" ] && [ "$XDG_VTNR" -eq 1 ] ; then
       exec sway
    fi

有关更多详细信息，请参阅 [Xinit#登录时自动启动 X](<../zh-cn/Xinit.html#%E7%99%BB%E5%BD%95%E6%97%B6%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8_X> "Xinit")。 

###  使用显示管理器启动

Sway 会话位于 `/usr/share/wayland-sessions/sway.desktop`。它可以被 [GDM](<../zh-cn/GDM.html> "GDM") 和 [SDDM](<../zh-cn/SDDM.html> "SDDM") 等现代显示管理器自动识别。 

也可以将 [systemd 用户服务](<https://github.com/swaywm/sway/wiki/Systemd-integration#running-sway-itself-as-a---user-service>)作为一个显示管理器去运行 sway。 

您还可以使用基于文本的显示管理器，请参阅[显示管理器#控制台](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html#%E6%8E%A7%E5%88%B6%E5%8F%B0> "显示管理器")。 

##  配置

若您已在使用 i3，则可以将 i3 配置文件复制到 `~/.config/sway/config`，该文件开箱即用。否则，请将位于 `/etc/sway/config` 的示例配置文件复制到 `~/.config/sway/config`。有关配置的信息参见 [sway(5)](<https://man.archlinux.org/man/sway.5>)。 

**注意：** 用户配置文件中应当包含 `include /etc/sway/config.d/*` 一行，以便从引置文件（drop-in files）中读取并应用配置。[sway](<https://archlinux.org/packages/?name=sway>)包 提供了一个引置文件 `50-systemd-user.conf`，其会将多个环境变量导入 systemd 用户会话和 dbus。一些应用需要这些环境变量以正常运行（如[xdg-desktop-portal-wlr](<https://archlinux.org/packages/?name=xdg-desktop-portal-wlr>)包）。

###  键盘布局

默认情况下，sway 从 US QWERTY 键盘布局开始。配置多个键盘布局： 
    
    ~/.config/sway/config
    
    input * {
        xkb_layout "us,de,ru"
        xkb_variant "colemak,,typewriter"
        xkb_options "grp:win_space_toggle"
    }
    
    input <identifier> xkb_model "pc101"
    
更多细节请参阅 [xkeyboard-config(7)](<https://man.archlinux.org/man/xkeyboard-config.7>) 与 [sway-input(5)](<https://man.archlinux.org/man/sway-input.5>)。 

在启动 `sway` 时，也可以使用环境变量（`XKB_DEFAULT_LAYOUT`、`XKB_DEFAULT_VARIANT` 等）配置键盘布局。配置选项优先于环境变量。 

###  打字延迟和速率

要更改打字延迟和速率，您可以在 `input` 节添加以下行： 
    
    ~/.config/sway/config
    
    input <identifier> repeat_delay 300
    input <identifier> repeat_rate 30
    
###  状态栏

Sway 附带了一个默认状态栏，名为 _swaybar_ ，可在纯 [Wayland](<../zh-cn/Wayland.html> "Wayland") 环境中运行。 _swaybar_ 可以调用 shell 脚本或其他程序来在状态栏中显示信息。有关详细信息，请参阅 [sway-bar(5)](<https://man.archlinux.org/man/sway-bar.5>) 与 [swaybar-protocol(7)](<https://man.archlinux.org/man/swaybar-protocol.7>)。 

**提示：** _swaybar_ 对[托盘图标](<https://github.com/swaywm/sway/issues/3799>)的支持并不完整，请考虑使用 [waybar](<https://archlinux.org/packages/?name=waybar>)包 等替代方案，在 `bar` 节设置 `swaybar_command waybar` 即可启用。

[i3status](<../zh-cn/I3.html#i3status> "I3") 是在 Wayland 下获取实用的默认状态栏的一个选项，您只需在 sway 配置的末尾添加以下代码段： 
    
    ~/.config/sway/config
    
    bar {
        status_command i3status
    }
    
欲为 i3status 启用色彩输出，请在 i3status 配置中调整以下部分： 
    
    ~/.config/i3status/config
    
    general {
        colors = true
        interval = 5
    }

### Output

`sway` 的 `output` 命令可以为不同的显示输出指定详细配置，包括但不限于壁纸、缩放、位置等。如有需要，您可将不同的 output 命令整合到一行，例如： 
    
    ~/.config/sway/config
    
    output HDMI-A-1 mode 1920x1080 pos 1920 0 bg ~/wallpaper.png stretch
    
output 有多种方式匹配显示输出。可以使用其指定的输出名称，也可以使用 `"*"` 匹配所有显示输出，或是使用显示器的不同名称（由品牌、型号和序列号组成的字符串），例如： 
    
    ~/.config/sway/config
    
    output "Some Company ABC123 0x00000000" pos 1920 0
    
可以使用以下命令获取输出名称和一些其他信息： 
    
    $ swaymsg -t get_outputs
    
要深入了解配置和附加选项，请参阅 [sway-output(5)](<https://man.archlinux.org/man/sway-output.5>)。 

####  壁纸

sway 用专用程序处理壁纸，最简单的例子是 [swaybg](<https://archlinux.org/packages/?name=swaybg>)包，其可直接由 `sway` 管理。若要运行 `output ... bg` 命令，请安装 [swaybg](<https://archlinux.org/packages/?name=swaybg>)包。 

可以将以下行附加在 sway 配置的任意位置，其会在所有显示器上设置背景图像： 
    
    ~/.config/sway/config
    
    output "*" bg /path/to/image fill
    
当然，`/path/to/image` 应当被替换为存在的图像路径。 

如果只需要纯色背景，可以按如下方式设置： 
    
    output * bg #000000 solid_color
    
请参阅 [Sway wiki](<https://github.com/swaywm/sway/wiki/Useful-add-ons-for-sway#wallpaper>) 以了解更多用于管理壁纸的工具。 

#### HiDPI

**注意：** Xwayland 也会被缩放，且会降低分辨率[[2]](<https://github.com/swaywm/sway/issues/5444>)。欲以原始分辨率运行 Xwayland 下的程序，则需禁用缩放。您可使用一些工具临时禁用缩放，如使用 swaymsg： 
    
    swaymsg output "*" scale 1
    
欲恢复到自动设定则设为 `0`。

#####  自动设定

Sway 默认使用整数倍缩放。若满足以下条件[[3]](<https://github.com/swaywm/sway/blob/1.9/sway/config/output.c#L317-L368>)： 

  * 屏幕通过 EDID（ Extended Display Identification Data，外部显示设备标识数据）提供有效的物理显示信息。

  * DPI（每英寸像素数）至少为 192。

  * 屏幕分辨率的高至少为 1200 像素。

那么 Sway 会使用 2 倍缩放。一些设备（如 [Framework Laptop 16](</wzh/index.php?title=Framework_Laptop_16&action=edit&redlink=1> "Framework Laptop 16（页面不存在）")）的 DPI 近似（但不是）192，在这种情况下，您可能需要手动配置分数倍缩放。 

#####  手动设定

在配置文件里用 `output` 命令设置缩放倍数。可以设置分数倍缩放，不过 HiDPI 屏幕通常为 2。 
    
    ~/.config/sway/config
    
    output <名称> scale <倍数>
    
可以使用以下命令获知显示器名称： 
    
    $ swaymsg -t get_outputs
    
####  撕裂

Sway 默认会同步帧更新（vsync，垂直同步）以使输出画面的每一帧都帧完整而不撕裂，但是会带来一些延迟。在一些使用场景（如游戏）下禁用垂直同步可以使输出更为顺畅： 
    
    ~/.config/sway/config
    
    output <name> allow_tearing yes
    output * max_render_time off
    
###  输入设备

可以调整特定输入设备的配置。例如，若要为所有触摸板启用点击以单击和自然滚动，请使用以下配置： 
    
    ~/.config/sway/config
    
    input type:touchpad {
        tap enabled
        natural_scroll enabled
    }
    
要为特定触摸板设定配置，请使用 `swaymsg -t get_inputs` 获取设备标识符并用其代替上述配置中的 `type:touchpad`。 

**注意：** 命令 `swaymsg -t get_inputs` 的输出可能会使用`\`来转义`/`等符号（如 `"2:14:ETPS\/2_Elantech_Touchpad"`），配置时需要删除`\`。

关于更多文档和选项（如加速度或完全禁用输入），请参阅 [sway-input(5)](<https://man.archlinux.org/man/sway-input.5>)。 

若您使用数位板，请参阅 [Graphics tablet#Sway](</wzh/index.php?title=%E6%95%B0%E4%BD%8D%E6%9D%BF&action=edit&redlink=1> "数位板（页面不存在）")（英语：[Graphics tablet#Sway](<https://wiki.archlinux.org/title/Graphics_tablet#Sway> "en:Graphics tablet")）。 

####  触摸屏映射

在多显示器环境中，触摸屏的触摸输入目标可以仅被映射到该触摸屏。 
    
    ~/.config/sway/config
    
    set $display1      "Dell Inc. DELL P2414H VHVTW542165L"
    set $display2      "Dell Inc. DELL P2418HT MYDM775F152L"
    set $display2-touch "8146:24835:Melfas_LGD_AIT_Touch_Controller"
    
    input $display2-touch map_to_output $display2
    
###  自定义快捷键

键盘上的[特殊按键](<../zh-cn/%E9%94%AE%E7%9B%98%E8%BE%93%E5%85%A5.html> "键盘输入")可用于执行命令，如控制音量、屏幕亮度和媒体播放： 
    
    ~/.config/sway/config
    
    bindsym XF86AudioRaiseVolume exec pactl set-sink-volume @DEFAULT_SINK@ +5%
    bindsym XF86AudioLowerVolume exec pactl set-sink-volume @DEFAULT_SINK@ -5%
    bindsym XF86AudioMute exec pactl set-sink-mute @DEFAULT_SINK@ toggle
    bindsym XF86AudioMicMute exec pactl set-source-mute @DEFAULT_SOURCE@ toggle
    bindsym XF86MonBrightnessDown exec brightnessctl set 5%-
    bindsym XF86MonBrightnessUp exec brightnessctl set 5%+
    bindsym XF86AudioPlay exec playerctl play-pause
    bindsym XF86AudioPause exec playerctl play-pause
    bindsym XF86AudioNext exec playerctl next
    bindsym XF86AudioPrev exec playerctl previous
    bindsym XF86AudioStop exec playerctl stop
    bindsym XF86Search exec bemenu-run
    
有关详细信息和替代实用程序，请参阅： 

  * [PulseAudio#键盘控制音量](<../zh-cn/PulseAudio.html#%E9%94%AE%E7%9B%98%E6%8E%A7%E5%88%B6%E9%9F%B3%E9%87%8F> "PulseAudio")
  * [WirePlumber#键盘控制音量](<../zh-cn/WirePlumber.html#%E9%94%AE%E7%9B%98%E6%8E%A7%E5%88%B6%E9%9F%B3%E9%87%8F> "WirePlumber")
  * [ALSA#键盘控制音量](<../zh-cn/ALSA.html#%E9%94%AE%E7%9B%98%E6%8E%A7%E5%88%B6%E9%9F%B3%E9%87%8F> "ALSA")
  * [背光#背光实用程序](<../zh-cn/%E8%83%8C%E5%85%89.html#%E8%83%8C%E5%85%89%E5%AE%9E%E7%94%A8%E7%A8%8B%E5%BA%8F> "背光")
  * [MPRIS](<../zh-cn/MPRIS.html> "MPRIS")。

要允许在锁屏时执行快捷键，请将 `--locked` 参数添加到 bindsym。 
    
    bindsym --locked XF86AudioPlay exec playerctl play-pause
    
**提示：**[wev](<https://archlinux.org/packages/?name=wev>)包 工具提供类似于 [xorg-xev](<https://archlinux.org/packages/?name=xorg-xev>)包 的功能，但运行于 Wayland。

**注意：** Systemd 会处理一些特殊按键，如电源键和盖子打开/关闭事件。这可能会干扰在 sway 中配置的快捷键。请参阅 [loginctl(1)](<https://man.archlinux.org/man/loginctl.1>) 与 [logind.conf(5)](<https://man.archlinux.org/man/logind.conf.5>) 以获取有关如何在 [systemd](<../zh-cn/Systemd.html> "Systemd") 中配置它们的详细信息。

####  图形指示条

在调整某些百分比值设置（如亮度或音量）时，可以显示一个图形指示条。在 Sway 中提供此工具的一个不错的选择是 [wob](<https://archlinux.org/packages/?name=wob>)包（或 [wob-git](<https://aur.archlinux.org/packages/wob-git/>)AUR），其是 Wayland 上 layer-shell 协议的实现，提供了流行的 X 工具 [xob](<https://aur.archlinux.org/packages/xob/>)AUR 的部分功能。有关使用示例，请参阅[项目网站](<https://github.com/francma/wob>)。 

####  工作区概览

如果您在工作区开启了很多窗口，导致难以分辨，那么 [sov](<https://aur.archlinux.org/packages/sov/>)AUR 可以派上用场。它是一个叠加层，可以显示所有工作区的概览，使 sway 导航更容易。其可以显示程序名称、窗口标题，支持多 output 配置。关于详细信息，请参阅[项目网站](<https://github.com/milgra/sov>)。 

###  空闲管理

Sway 有一个名为 [swayidle](<https://archlinux.org/packages/?name=swayidle>)包 的专用空闲管理守护程序来处理空闲会话。可以用不同的方法来启动和参数化守护程序。最简单的方法是使用 sway 本身的配置。`swayidle` 接受大量参数来配置 `timeout`（超时，又名“空闲”）、`resume`（恢复，超时后从空闲中恢复）、`before-sleep`（睡眠前）等事件，请参阅 [swayidle(1)](<https://man.archlinux.org/man/swayidle.1>) 了解更多细节和事件的进一步解释。然后，可以为每个事件分配一个操作。要为一个事件分配多个操作，只需重复触发器即可。 

以下配置可使 `swayidle` 在 30 分钟后锁定屏幕，并在 5 秒后将其关闭： 
    
    ~/.config/sway/config
    
    exec swayidle -w \
    	timeout 1800 'swaylock -f' \
    	timeout 1805 'swaymsg "output * power off"' \
    		resume 'swaymsg "output * power on"'
    
要更快地关闭锁定屏幕，例如在10秒后，请为锁定管理器设置进程列表，并相应地执行 `swaymsg "output * power off"` ，如下： 
    
    timeout 10 'if pgrep -x swaylock; then swaymsg "output * power off"; fi' resume 'if pgrep -x swaylock; then swaymsg "output * power on"; fi' 
    
要在屏幕锁定前挂起和暂停播放媒体，请将以下配置添加到 swayidle 命令： 
    
    before-sleep 'playerctl pause;swaylock -f'
    
**注意：** Systemd 也处理一些空闲事件，这些事件可能与在 sway 中配置的事件冲突。请参阅 [loginctl(1)](<https://man.archlinux.org/man/loginctl.1>) 和 [logind.conf(5)](<https://man.archlinux.org/man/logind.conf.5>) 以获取关于如何配置它们的详细信息。

若您不希望在 Firefox、Chrome 或 VLC 播放视频时触发 swaylock，您可以用 [idlehack-git](<https://aur.archlinux.org/packages/idlehack-git/>)AUR 监听 dbus 的 screensaver inhibit（阻止屏保）请求并调用 swayidle-inhibit。Firefox、Chrome 和 VLC 等程序会发出该事件以阻止系统空闲。 

####  恢复时屏幕内容短暂显示

使用 `before-sleep swaylock` 可能会使系统从睡眠中恢复时屏幕内容短暂显示。欲缓解该问题，您可使 logind 忽略盖子（lid）事件并改用 Sway 处理盖子和电源按钮事件。 
    
    /etc/systemd/logind.conf
    
    [Login]
    HandlePowerKey=ignore
    HandlePowerKeyLongPress=ignore
    HandleSuspendKey=ignore
    HandleLidSwitch=ignore
    HandleLidSwitchExternalPower=ignore
    HandleLidSwitchDocked=ignore
    
    ~/.config/sway/config
    
    bindswitch --locked lid:toggle exec swaylock --daemonize && systemctl sleep
    
    exec swayidle -w \
              timeout 60  'if pgrep swaylock; then systemctl sleep; fi' \
              timeout 150 'swaylock --daemonize' \
              timeout 155 'systemctl sleep'
    
使用 `--locked` 选项以在屏幕锁定时合盖休眠系统。若要使笔记本在合盖后依然工作，使用 `unbindswitch lid:toggle`。可以使用 `pgrep swaylock` 以使电脑被意外唤醒后再次休眠。 

logind 集成 [bug 较多](<https://github.com/swaywm/swayidle/pull/133>)且[难以维护](<https://github.com/swaywm/swayidle/issues/117>)。另见 [[4]](<https://whynothugo.nl/journal/2022/10/26/systemd-locking-and-sleeping/>)。 

###  悬浮窗口和窗口分配

要启用悬浮窗口或窗口分配，请打开应用程序，然后使用 `app_id`、`class`、`instance` 和 `title` 属性来启用悬浮窗口/窗口分配。以下命令可以列出所有打开的窗口的属性： 
    
    $ swaymsg -t get_tree
    
欲获取所有打开的窗口的 `app_id`，请执行： 
    
    $ swaymsg -t get_tree | grep "app_id"
    
仅获取当前选中窗口的 `app_id`，请执行： 
    
    $ swaymsg -t get_tree | jq -r '..|try select(.focused == true)'
    
X11 窗口没有 `app_id` 属性，要匹配它们，您可以使用 `class`、`window_type`、`window_role` 和/或 `instance` 等属性。请在 `swaymsg -t get_tree` 命令的输出中查找相关属性并为窗口创建足够详细的规则。 
    
    ~/.config/sway/config
    
    for_window [app_id="galculator"] floating enable
    for_window [window_type="dialog"] floating enable
    for_window [window_role="dialog"] floating enable
    assign [app_id="firefox"] 3
    assign [class="^Urxvt$" instance="^htop$"] 9

这类似于在[X11](<../zh-cn/Xorg.html> "X11")中使用 [xorg-xprop](<https://archlinux.org/packages/?name=xorg-xprop>)包 查找 `class` 或 `wm_name` 属性。 

使用多个显示器时，悬浮的 scratchpad（暂存器）窗口可能会变得很大，覆盖多个显示器。可以使用以下命令将悬浮窗口居中并调整为当前显示器大小的 80%： 
    
    $ swaymsg move position center; swaymsg resize set 80ppt 80ppt
    
###  剪贴板

Wayland 下剪贴板内容由复制来源应用程序管理，如果该程序关闭，则复制的内容就不再可用。 

欲持久化剪贴板内容，请使用"剪贴板管理器"，其会自行再复制并保留一份剪贴板内容。 

举一个针对 Wayland 设计的剪贴板管理器 [clipman](<https://github.com/chmouel/clipman>)，它可以通过 [clipman](<https://aur.archlinux.org/packages/clipman/>)AUR 或 [clipman-git](<https://aur.archlinux.org/packages/clipman-git/>)AUR 进行安装。 

如果要在 Sway 中使用 clipman， 请将以下行添加到配置文件中： 
    
    ~/.config/sway/config
    
    exec wl-paste -t text --watch clipman store --no-persist

关于剪贴板的详细信息和替代程序，请参阅[剪贴板](<../zh-cn/%E5%89%AA%E8%B4%B4%E6%9D%BF.html> "剪贴板")。 

### Xresources

在 Sway 中使用 `~/.Xresources` 需要把它拷贝到`~/.Xdefaults`。 

### Xwayland

请参阅 [Wayland#Xwayland](<../zh-cn/Wayland.html#Xwayland> "Wayland") 以了解详细信息和可用软件包的概述。 

默认情况下 Xwayland 处于启用状态。 

欲完全禁用 Xwayland 并运行“纯”Wayland 会话，请使用以下配置以禁用 Xwayland： 
    
    ~/.config/sway/config
    
    xwayland disable
    
若您想一眼知晓哪些窗口使用 Xwayland，可以使用以下配置： 
    
    ~/.config/sway/config
    
    for_window [shell="xwayland"] title_format "[XWayland] %title"
    
**注意：** 一些程序需要[特殊的环境变量或配置选项](<../zh-cn/Wayland.html#%E5%9B%BE%E5%BD%A2%E5%BA%93> "Wayland")才能在原生 Wayland 下运行，而另一些程序（包括大多数专有应用程序）根本不支持 Wayland。目前，建议保持启用 Xwayland，以便使用旧版应用程序。

###  使用另一个 wlroots 渲染器

要使用另一个渲染器如 Vulkan，请参阅 [Wayland#在基于 wlroots 的混成器上使用另一个渲染器](<../zh-cn/Wayland.html#%E5%9C%A8%E5%9F%BA%E4%BA%8E_wlroots_%E7%9A%84%E6%B7%B7%E6%88%90%E5%99%A8%E4%B8%8A%E4%BD%BF%E7%94%A8%E5%8F%A6%E4%B8%80%E4%B8%AA%E6%B8%B2%E6%9F%93%E5%99%A8> "Wayland")。 

###  程序自启动

参见 [i3#自启动程序](<../zh-cn/I3.html#%E8%87%AA%E5%90%AF%E5%8A%A8%E7%A8%8B%E5%BA%8F> "I3")章节，并将配置文件名调整为适用于 Sway 的版本。 

##  提示和技巧

###  启动时启用 NumLock

Sway 在启动时默认禁用 `NumLock`。欲使其自动启用，请将键盘的 `xkb_numlock` 输入配置设置为 `enable`。例如，欲使所有键盘如此，请将以下行添加到 Sway 配置： 
    
    ~/.config/sway/config
    
    input type:keyboard xkb_numlock enabled
    
任何情况下，都可以通过键盘上的相关按键来切换 `NumLock` 状态。 

**提示：** 如需，也可以用 `xkb_capslock` 以相同方式设置 `CapsLock`。

**注意：** 用通配符启用这些可能会导致在重新加载 Sway 配置文件时 Firefox 崩溃，参见 [Bugzilla 1652820](<https://bugzilla.mozilla.org/show_bug.cgi?id=1652820>)，请尝试[指定特定键盘](<https://bugzilla.mozilla.org/show_bug.cgi?id=1652820#c31>)而非通配符。

###  当前键盘布局

可以按如下方式检索当前键盘布局，其中 `_kbd_identifier_` 需要替换为键盘的标识符： 
    
    $ swaymsg -t get_inputs | jq -r '.[] | select(.identifier == "_kbd_identifier_ ") | .xkb_active_layout_name'
    
###  组合键

组合键（compose key）和其它按键结合使用可用于输入键盘不支持的字符。例如将 `PrintScreen` 设为组合键： 
    
    $ swaymsg 'input * xkb_options compose:prsc'
    
可在 [Xorg/Keyboard configuration#Configuring compose key](</wzh/index.php?title=Xorg/%E9%94%AE%E7%9B%98%E9%85%8D%E7%BD%AE&action=edit&redlink=1> "Xorg/键盘配置（页面不存在）")（英语：[Xorg/Keyboard configuration#Configuring compose key](<https://wiki.archlinux.org/title/Xorg/Keyboard_configuration#Configuring_compose_key> "en:Xorg/Keyboard configuration")） 查看可用的组合。组合也可以在 [XCompose 文件](</wzh/index.php?title=Xorg/%E9%94%AE%E7%9B%98%E9%85%8D%E7%BD%AE&action=edit&redlink=1> "Xorg/键盘配置（页面不存在）")（英语：[Xorg/Keyboard configuration#Key combinations](<https://wiki.archlinux.org/title/Xorg/Keyboard_configuration#Key_combinations> "en:Xorg/Keyboard configuration")）中配置，需要重新启动应用程序才能使更改生效。 

###  背光切换

若要使用某按键（如 `Pause`）关闭（和打开）显示器，请在 Sway`config` 中绑定以下脚本： 
    
    #!/bin/sh
    read lcd < /tmp/lcd
        if [ "$lcd" -eq "0" ]; then
            swaymsg "output * power on"
            echo 1 > /tmp/lcd
        else
            swaymsg "output * power off"
            echo 0 > /tmp/lcd
        fi
    
也可以直接使用 [toggle](<https://github.com/swaywm/sway/pull/6099>) 选项，只是使用多显示器时需要明确指定 output： 
    
    $ swaymsg "output _output_name_ power toggle"
    
###  屏幕捕获和屏幕共享

请查看[屏幕捕获#Wayland](<../zh-cn/%E5%B1%8F%E5%B9%95%E6%8D%95%E8%8E%B7.html#Wayland> "屏幕捕获"). 

###  色温调节

请查看[背光#Wayland](<../zh-cn/%E8%83%8C%E5%85%89.html#Wayland> "背光"). 

###  色彩管理

可以将以下行添加到 Sway 配置以使用色彩管理配置文件： 
    
    ~/.config/sway/config
    
    output * _色彩管理配置文件_ icc /path/to/your/color_profile.icc

###  用键盘控制 swaynag

Swaynag 是 sway 附带的默认警告/提示程序，仅支持用户用鼠标与之交互。诸如 [swaynagmode](<https://aur.archlinux.org/packages/swaynagmode/>)AUR 之类的帮助程序可通过键盘快捷键启用交互。 

Swaynagmode 的工作原理是首先启动 swaynag，然后侦听触发操作的信号，例如选择下一步按钮、关闭提示或接受所选按钮。这些信号会被另外的带有控制参数的 swaynagmode 脚本实例（如 `swaynagmode --select right` 和 `swaynagmode --confirm`）发送。 

默认情况下，Swaynagmode 在初始化时触发 sway 的 `nag` 模式，在退出时返回 `default`。这样，您就可以在 sway 配置中轻松定义快捷键： 
    
    ~/.config/sway/config
    
    set $nag exec swaynagmode
    mode "nag" {
      bindsym {
        Ctrl+d    mode "default"
    
        Ctrl+c    $nag --exit
        q         $nag --exit
        Escape    $nag --exit
    
        Return    $nag --confirm
    
        Tab       $nag --select prev
        Shift+Tab $nag --select next
    
        Left      $nag --select next
        Right     $nag --select prev
    
        Up        $nag --select next
        Down      $nag --select prev
      }
    }
    
**注意：** 从 sway 版本 1.2 开始，模式名称区分大小写。

您可将 sway 配置为通过配置命令 `swaynag_command swaynagmode` 使用 swaynagmode。 

###  更改光标主题和大小

要设置[光标主题](<../zh-cn/%E5%85%89%E6%A0%87%E4%B8%BB%E9%A2%98.html> "光标主题")和大小，请使用以下配置： 
    
    ~/.config/sway/config
    
    seat seat0 xcursor_theme _光标主题_ _光标大小_
    
其中` _光标主题_`可以设置或替换为特定名称（如 `default`、`Adwaita` 或 `Simple-and-Soft`），以及` _光标大小_`值如 `48`。 

要查看二者的值，可以使用 `echo $XCURSOR_SIZE` 和 `echo $XCURSOR_THEME`。 

更改配置后需要重新加载 Sway 以使更改生效。 

**注意：** Wayland 光标可由应用程序确定，这意味着应用程序可能不会遵循 `$XCURSOR_SIZE` 和 `$XCURSOR_THEME` 的值。

###  使用 systemd 管理仅用于 Sway 的守护程序

Systemd 提供了一个 `graphical-session.target` 用户单元，其会在任何图形会话（无论是 Xorg 还是 Wayland）正在运行时活动。可以将应该在所有图形环境中运行的用户服务绑定到该目标，其还允许将特定于某窗口管理器的目标绑定到 `graphical-session.target` 以启动和停止仅在该窗口管理器下运行的服务。请参阅 [systemd.special(7)](<https://man.archlinux.org/man/systemd.special.7>)。 

用户可能希望仅为 Sway 启动某些服务/守护程序（如 [swayidle](<https://archlinux.org/packages/?name=swayidle>)包 或 [kanshi](<https://archlinux.org/packages/?name=kanshi>)包），并且可能还希望这些服务在 Sway 停止时停止。此外，使用 [systemd-oomd.service(8)](<https://man.archlinux.org/man/systemd-oomd.service.8>) 的用户可能希望将服务放在单独的 cgroup 中，以便单个内存密集型服务不会关闭整个 Sway 会话（请参阅 [Fedora bug 报告](<https://bugzilla.redhat.com/show_bug.cgi?id=1933494>)）。 

此功能的部分或全部由 Arch 的 Sway 软件包提供。例如，[sway](<https://archlinux.org/packages/?name=sway>)包 和 [sway-git](<https://aur.archlinux.org/packages/sway-git/>)AUR 都提供一个 `50-systemd-user.conf` 引置文件（见[#配置](<#%E9%85%8D%E7%BD%AE>)）。 

如果您打算使用下面介绍的自己手搓的方法或使用专门的软件包（如[sway-systemd-git](<https://aur.archlinux.org/packages/sway-systemd-git/>)AUR、[sway-services-git](<https://aur.archlinux.org/packages/sway-services-git/>)AUR 或 [uwsm](<https://archlinux.org/packages/?name=uwsm>)包）来实现此功能，则应考虑删除提供相同功能的文件。 

要自己手搓该功能，可以创建一个 `sway-session.target`，让该目标启动需要的守护进程/服务。此 systemd 目标应当是用户目标（请参见 [systemd/用户](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "Systemd/用户")）。 例如： 
    
    ~/.config/systemd/user/sway-session.target
    
    [Unit]
    Description=Sway compositor session
    Documentation=man:systemd.special
    BindsTo=graphical-session.target
    Wants=graphical-session-pre.target
    After=graphical-session-pre.target

然后，将以下行添加到 Sway 的配置文件中（例如，将该行追加到 `~/.config/sway/config`或将新文件添加到 `/etc/sway/config.d/`）： 
    
    ~/.config/sway/config
    
    ...
    ...
    ...
    exec_always systemctl --user start sway-session.target

如此，每当 Sway 启动时也会运行 `sway-session.target`。 

最后，将所需的服务链接到 `sway-session.target`。例如添加 [kanshi](<https://archlinux.org/packages/?name=kanshi>)包（或 [kanshi-git](<https://aur.archlinux.org/packages/kanshi-git/>)AUR）服务（见 [kanshi#使用 systemd 管理 kanshi](<../zh-cn/Kanshi.html#%E4%BD%BF%E7%94%A8_systemd_%E7%AE%A1%E7%90%86_kanshi> "Kanshi")）。 

当该[用户单元](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "Systemd/用户")处于[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")状态时，其仅在 Sway 运行时激活，并在 Sway 关闭时停用。 

`sway-session.target`文件的创建和环境的导入也可以通过 [sway-systemd-git](<https://aur.archlinux.org/packages/sway-systemd-git/>)AUR 来完成。除了将服务分离到 cgroup 中之外，sway-systemd 还将每个 GUI 应用程序放在自己的 cgroup 中。这样就可以对单个应用程序进行独立的资源约束，参见 [sway-systemd README](<https://github.com/alebastr/sway-systemd>)。此外，[uwsm](<https://archlinux.org/packages/?name=uwsm>)包 提供了一个更综合的解决方案。 

###  启动后更改屏幕分辨率

您可使用 GUI 程序 [nwg-displays](<https://archlinux.org/packages/?name=nwg-displays>)包、[wdisplays](<https://archlinux.org/packages/?name=wdisplays>)包、[swayrandr-git](<https://aur.archlinux.org/packages/swayrandr-git/>)AUR 或终端程序 [wlr-randr](<https://archlinux.org/packages/?name=wlr-randr>)包 来更改屏幕分辨率和方向、排列显示器以及设定缩放。 

###  创建无外设（Headless）输出

创建与物理 video 接口无关的输出 （`HEADLESS-1`、`HEADLESS-2`等）： 
    
    $ swaymsg create_output
    
显示新输出的说明： 
    
    $ swaymsg -pt get_outputs | grep -A 10 HEADLESS
    
使用 `output` 命令配置新的输出，例如： 
    
    ~/.config/sway/config
    
    output HEADLESS-1 {
    pos 1920,0
    mode 1280x720@75Hz
    }

###  将修饰键（modifier）修改为 CapsLock 并保留 Super

要将修饰键更改为 `CapsLock` 并在 US 键盘布局上继续使用 `Super`，请创建 `~/.config/xkb/symbols/custom`，具有以下内容： 
    
    ~/.config/xkb/symbols/custom
    
    xkb_symbols "basic" {
        include "us"
        name[Group1]= "English (US Custom)";
        key <CAPS> { [ Hyper_L ] };
        modifier_map Mod4 { Hyper_L };
        key <LWIN> { [ Super_L ] };
        modifier_map Mod5 { Super_L };
    };

对于其他语言，请编辑第二行和第三行，并在 Sway 配置文件开头附加引用该键盘布局： 
    
    ~/.config/sway/config
    
    input * xkb_layout custom
    set $mod Mod4
    set $super Mod5
    
###  通过 VNC 远程访问无外设（Headless） Sway 会话

以下示例教程讲述了通过 SSH 启动并通过 VNC 远程访问无外设 Sway 会话。 

[wayvnc](<https://archlinux.org/packages/?name=wayvnc>)包 是一个 VNC 服务器，适用于基于 wlroots 的 Wayland 混成器，可以用于承载无外设 Sway 会话。 

要启动一个无外设 Sway 会话，请将 `WLR_BACKENDS` 设为 `headless`，可选将 `WLR_LIBINPUT_NO_DEVICES` 设为 `1`（参见 [wayvnc FAQ](<https://github.com/any1/wayvnc/blob/master/FAQ.md>)）： 
    
    $ WLR_BACKENDS=headless WLR_LIBINPUT_NO_DEVICES=1 sway
    
**提示：** 在命令结尾添加 `&` 以使其后台运行。

现在，请运行 `wayvnc` 以启动 VNC 服务器： 
    
    $ WAYLAND_DISPLAY=wayland-1 wayvnc
    
**注意：** 默认情况下，[wayvnc](<https://archlinux.org/packages/?name=wayvnc>)包 仅会监听本机 5900 端口（`localhost:5900`），可以另行配置（参见 `man wayvnc`）。您可能会想按照 [OpenSSH#转发其他端口](<../zh-cn/OpenSSH.html#%E8%BD%AC%E5%8F%91%E5%85%B6%E4%BB%96%E7%AB%AF%E5%8F%A3> "OpenSSH") 所述转发端口。请注意 [wayvnc](<https://archlinux.org/packages/?name=wayvnc>)包 默认**不加密** 且**不验证身份** ！

###  输出热插拔钩子

若您想在一个输出连接（或断开连接）时搞点事情，可以阅读 [kanshi](<../zh-cn/Kanshi.html> "Kanshi")。 

##  疑难解答

###  应用程序启动器

**提示：** Sway wiki 包含一个[已知应用程序启动器列表](<https://github.com/swaywm/sway/wiki#program-launchers>)。

[dmenu](<https://archlinux.org/packages/?name=dmenu>)包 在 Sway 中运行得相对较好，但运行于 Xwayland，并且存在问题：如果将光标移动到原生 Wayland 窗口，Xwayland 应用程序可能会无响应。因为 Wayland 客户端/窗口在不具有屏幕焦点时无法访问输入设备，而 Xwayland 服务器本身就是 Wayland 混成器的客户端，因此其 Xwayland 客户端之一必须具有焦点才能访问用户输入。一旦其某个客户端具有焦点，其就可以收集输入，并通过 X11 协议将其提供给所有 Xwayland 客户端。因此，将光标移动到 Xwayland 窗口并按 Esc 键退出应该可以解决此问题，有时运行 `pkill` 也可以。 

[bemenu](<https://archlinux.org/packages/?name=bemenu>)包 是一个原生的 Wayland dmenu 替代品，二者都可以选择与 [j4-dmenu-desktop](<https://archlinux.org/packages/?name=j4-dmenu-desktop>)包 结合使用，为启动桌面文件提供原生 Wayland 组合（如同 i3-dmenu-desktop），例如： 
    
    j4-dmenu-desktop --dmenu='bemenu -i --nb "#3f3f3f" --nf "#dcdccc" --fn "pango:DejaVu Sans Mono 12"' --term='termite'
    
如果选择不禁用 Xwayland，则可能需要将 `BEMENU_BACKEND` 环境变量设置为 `wayland`。 

您还可以使用浮动终端和 fzf 自己手搓一个应用程序启动器，如 [GitHub issue](<https://github.com/swaywm/sway/issues/1367>) 所述。 

[plasma-workspace](<https://archlinux.org/packages/?name=plasma-workspace>)包 软件包提供的 `krunner` 应用也可以作为启动器，支持 Xwayland 和原生 Wayland。 

[rofi](<https://archlinux.org/packages/?name=rofi>)包 现已同时支持 Wayland 和 X11。 

[wofi](<https://archlinux.org/packages/?name=wofi>)包 是一个命令启动器，提供了 rofi 的部分功能，运行于 Wayland。Wofi缺少 rofi 的一些功能，如 SSH 模式和窗口切换模式。其基于 [wlroots0.19](<https://archlinux.org/packages/?name=wlroots0.19>)包 库，并使用 GTK3 进行渲染，与 sway 配合得很好。 

[fuzzel](<https://archlinux.org/packages/?name=fuzzel>)包 是一个为基于 wlroots 的 Wayland 混成器开发的应用程序启动器，类似于 rofi 的 _drun_ 模式。 

###  虚拟化

Sway 可以在 [VirtualBox](<../zh-cn/VirtualBox.html> "VirtualBox") 和 [VMware](<../zh-cn/VMware.html> "VMware") ESXi 中使用。 

要使 Sway 在 [QEMU](<../zh-cn/QEMU.html> "QEMU") 中工作，必须以 `-vga qxl` 参数启动QEMU。另见 [QEMU#qxl](<../zh-cn/QEMU.html#qxl> "QEMU")。 

####  无法从 tty 启动 Sway

对于 ESXi， 您需要在 _Hardware Configuration > Video card settings_ 下启用 3D 支持。另见 [VMware#在 Intel、Optimus 和 AMD 上启用 3D 图形加速](<../zh-cn/VMware.html#%E5%9C%A8_Intel%E3%80%81Optimus_%E5%92%8C_AMD_%E4%B8%8A%E5%90%AF%E7%94%A8_3D_%E5%9B%BE%E5%BD%A2%E5%8A%A0%E9%80%9F> "VMware")。 

####  光标不可见

当使用某些图形驱动程序（例如VMSVGA图形控制器或专有的 [NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA") 驱动）时，光标可能会变得不可见。可以使用软件光标来解决此问题，具体讨论参见 [Issue 3814](<https://github.com/swaywm/sway/issues/3814>)： 
    
    $ export WLR_NO_HARDWARE_CURSORS=1
    
###  未检测到 sway socket

使用 `swaymsg` 时（如 `swaymsg -t get_outputs`）有时会返回以下消息： 
    
    sway socket not detected.
    ERROR: Unable to connect to
    
当在终端多路复用器（如 [GNU Screen](<../zh-cn/GNU_Screen.html> "GNU Screen") 或 [tmux](<../zh-cn/Tmux.html> "Tmux")）内运行时，`swaymsg` 无法连接到 `SWAYSOCK` 中提供的套接字。 

要查看当前 `SWAYSOCK` 的值，请执行： 
    
    $ env | grep -F "SWAYSOCK"
    
    SWAYSOCK=/run/user/1000/sway-ipc.1000.4981.sock

欲解决该问题，您可以尝试连接到一个正在运行的 sway 进程的套接字： 
    
    $ export SWAYSOCK=/run/user/$(id -u)/sway-ipc.$(id -u).$(pgrep -x sway).sock
    
欲避免此错误，请在终端多路复用器之外运行该命令。 

###  无法连接 Wayland 服务器

Tmux 会为每个会话创建环境变量（执行 `tmux show-environment` 以查询），因此，若您想要使用 [tmux-resurrect](<https://github.com/tmux-plugins/tmux-resurrect>) 或 [tmux-continuum](<https://github.com/tmux-plugins/tmux-continuum>) 重新恢复一个已有的 tmux 会话，或 tmux 服务器在 sway 启动前就在运行，环境变量就会过期。 

将以下内容添加到 `.tmux.conf`，之后您可以在恢复会话前使用 `update-environment` 更新环境变量： 
    
    set-option -g update-environment "DISPLAY WAYLAND_DISPLAY SWAYSOCK SSH_AUTH_SOCK"
    
###  无法获取 socket 路径

从 `swaymsg -t` 命令请求在tty上的消息可能会返回以下消息： 
    
    Unable to retrieve socket path
    
`SWAYSOCK` 环境变量在启动Sway后设置，因此解决此错误的一个方法是在Sway内部的终端中请求 `swaymsg -t [message]`。 

###  按键设置和键盘布局

默认情况下，如果您使用多个键盘布局（如 `input * xkb_layout "us,ru"`），在切换到某个次要布局时可能会导致快捷键失效。 

得益于 [Pull 3058](<https://github.com/swaywm/sway/pull/3058>) ，现在您只需在相应的 `bindsym` 行中添加 `--to-code`，如下： 
    
    bindsym --to-code {
      $mod+$left focus left
      $mod+$down focus down
      $mod+$up focus up
      $mod+$right focus right
    }
    
亦可创建一个变量 `set $mybind bindsym --to-code`，然后将所有的 `bindsym` 替换为 `$mybind`，如下： 
    
    $mybind $mod+w thing
    
###  Java 应用程序

当打开一些基于Java的应用程序（如 JetBrains的 IntelliJ、CLion 或 PyCharm）时，可能会显示空白画面。欲解决该问题，可以将环境变量 `_JAVA_AWT_WM_NONREPARENTING` 设为 `1` 来启动应用程序。 

若您从应用程序启动器（如 [rofi](<https://archlinux.org/packages/?name=rofi>)包 或 [dmenu](<https://archlinux.org/packages/?name=dmenu>)包）启动应用程序，则可以修改应用程序的[桌面项](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html#%E7%BC%96%E8%BE%91%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F> "桌面项")。 

OpenJDK 11 和 Sway 1.5 已经修复了一些 Java 应用程序的问题。然而，对于某些应用程序，需要进行额外的配置才能使用更新版本的 OpenJDK。对于 Android Studio，您需要设置 `STUDIO_JDK=/usr/lib/jvm/java-11-openjdk/`[[5]](<https://github.com/swaywm/sway/issues/5414>)。 

JRE 硬编码了一个窗口管理器列表，但该列表不包含 Sway，若您遇到灰色面板、菜单无焦点或窗口尺寸调整错误等问题，可以尝试[伪装成其它窗口管理器](<../zh-cn/Java.html#%E4%BC%AA%E8%A3%85%E6%88%90%E5%8F%A6%E4%B8%80%E4%B8%AA%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8> "Java")。 

###  边框上的滚动

如果在应用程序边框上使用鼠标滚轮导致Sway崩溃，您可以为 `app_id`（例如Firefox）使用`border none` 来禁用边框。 

###  “cannot open display” 错误

如果一个程序启动后出现“cannot open display”（无法打开显示器）并崩溃，那么该应用程序很可能是 X11 程序。您可以使用 Xwayland 兼容层在 Wayland 下运行 X11 程序，详见 [#Xwayland](<#Xwayland>)。 

###  WINE 中鼠标不工作

运行程序时，WINE 需要设定一个主显示器（primary monitor），但是 Wayland 没有主显示器的概念，这会引发问题（如 “clicks not registering”）。您可以使用 [xrandr](<../zh-cn/Xrandr.html> "Xrandr") 为 Xwayland 指定主显示器，只需向您的 Sway 配置添加以下内容： 
    
    ~/.config/sway/config
    
    ...
    exec_always xrandr --output XWAYLAND0 --primary
    ...

若如此做，因为 Sway 的一个 [bug](<https://github.com/swaywm/sway/issues/6651>)，您需要将屏幕显示偏移量设为 `0,0`。 

需要注意 XWAYLAND0（或其它 XWAYLAND 显示名称）可能不代表您的显示器，其后缀数字也可能在不同会话中变化。可以使用以下配置，其可将第一个 XWAYLAND 显示设定为主显示器： 
    
    exec_always xrandr --output $(xrandr | grep -m 1 XWAYLAND | awk '{print $1;}') --primary
    
您可按需调整此配置，使用不带参数的 `xrandr` 命令可以查看各 

**注意：** Xwayland 会把新连接的显示器识别为全新的显示器，这包括了关闭后又重新打开的显示器。若您设置的“主显示器”也被关闭后又打开，其将不再被视为主显示器。

###  NVIDIA GPU 上游戏闪烁

即便[官方不支持 NVIDIA 之类的专有驱动](<https://github.com/swaywm/sway/wiki#nvidia-users>)，但依然可以使用，甚至可以用来玩游戏。若如此做，您可能会看到屏幕上半区闪烁，可以尝试将 [wlroots0.19](<https://archlinux.org/packages/?name=wlroots0.19>)包 替换为 [wlroots-nvidia](<https://aur.archlinux.org/packages/wlroots-nvidia/>)AUR，也可以手动用补丁编译您自己的版本。 

###  屏幕捕获/WebRTC 不工作

确保您的配置包含以下内容： 
    
    include /etc/sway/config.d/*
    
然而，AUR 的部分 -git 软件包不提供 `/etc/sway/config.d`，此时您需要添加： 
    
    exec dbus-update-activation-environment DISPLAY I3SOCK SWAYSOCK WAYLAND_DISPLAY XDG_CURRENT_DESKTOP=sway
    
##  参见

  * [Sway 官方网站](<https://swaywm.org>)
  * [Sway GitHub 项目](<https://github.com/swaywm/sway>)
  * [Sway wiki](<https://github.com/swaywm/sway/wiki>)
  * [Sway 1.0 发布](<https://drewdevault.com/2019/03/11/Sway-1.0-released.html>)
