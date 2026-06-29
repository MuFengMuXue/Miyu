**翻译状态：**

  * 本文（或部分内容）译自 [Weston](<https://wiki.archlinux.org/title/Weston> "arch:Weston")，最近一次同步于 2024-03-23，若英文版本有所[更改](<https://wiki.archlinux.org/title/Weston?diff=0&oldid=804297>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Weston_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")
  * [窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")
  * [Wayland](<../zh-cn/Wayland.html> "Wayland")
  * [Xorg](<../zh-cn/Xorg.html> "Xorg")

Weston 是一个开源的、基于[Wayland](<../zh-cn/Wayland.html> "Wayland") 显示服务器协议的窗口管理器(compositor)，专为正确性、可靠性、可预测性和性能而设计。Weston作为Wayland协议的实现，提供了显示管理器的窗口管理和基本功能 ，包括不限于窗口的创建、移动、缩放、透明度处理、输入事件分发以及多屏幕支持等功能。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [weston](<https://archlinux.org/packages/?name=weston>)包 软件包。 

##  使用

要以本机方式（从 TTY）启动 Weston 或在正在运行的 X 会话中运行 Weston： 
    
    $ weston
    
想了解详细信息和配置，请参阅 [weston(1)](<https://man.archlinux.org/man/weston.1>) 。 

###  示例应用

在 Weston 中内置了原生wayland演示应用，可以运行这些示例程序。要启动终端仿真器，请执行以下命令： 
    
    $ weston-terminal
    
可移动的花 
    
    $ weston-flower 
    
显示图片 
    
    $ weston-image _image1.jpg image2.jpg..._
    
###  快捷键

**提示：**`Super` (windows按键) 可以自定义, 详细查看 [weston.ini](<#Configuration>)

**Weston 键盘快捷键** 组合键  | 动作   
---|---  
`Ctrl+Alt+Backspace` | 退出 Weston 合成器   
`Super+Scroll` (或 `PageUp`/`PageDown`)  | 放大/缩小 窗口   
`Super+Tab` | 切换窗口   
`Super+LMB` | 启动窗口   
`Super+MMB` | 旋转窗口   
`Super+RMB` | 改变窗口大小   
`Super+Alt+Scroll` | 改变窗口透明度   
`Super+k` | 强制关闭当前活动窗口   
`Super+Up/Down` | 切换到 上一个/下一个 工作区   
`Super+Shift+Up/Down` | 移动当前活动窗口到其他工作区   
`Super+F _n_` | 切换到工作区 _n_ (例如：F2)   
`Super+s` | 截屏   
`Super+r` | 录制屏幕   
  
##  配置

下面是一个示例配置文件。参见 [weston.ini(5)](<https://man.archlinux.org/man/weston.ini.5>) 了解更多信息。 
    
    ~/.config/weston.ini
    
    [core]
    # xwayland support
    xwayland=true
    
    [libinput]
    enable-tap=true
    
    [shell]
    #background-image=/usr/share/backgrounds/gnome/Aqua.jpg
    background-type=scale-crop
    background-color=0xff000000
    #background-color=0xff002244
    #panel-color=0x90ff0000
    panel-color=0x00ffffff
    panel-position=bottom
    #clock-format=none
    #animation=zoom
    #startup-animation=none
    close-animation=none
    focus-animation=dim-layer
    #binding-modifier=ctrl
    num-workspaces=6
    locking=false
    cursor-theme=Adwaita
    cursor-size=24
    
    # 平板电脑选项
    #lockscreen-icon=/usr/share/icons/gnome/256x256/actions/lock.png
    #lockscreen=/usr/share/backgrounds/gnome/Garden.jpg
    #homescreen=/usr/share/backgrounds/gnome/Blinds.jpg
    #animation=fade
    
    # 用于笔记本电脑显示器
    [output]
    name=LVDS1
    mode=preferred
    #mode=1680x1050
    #transform=rotate-90
    
    #[output]
    #name=VGA1
    # 下面使用 modeline 设置模式，您可以使用 cvt 工具获取首选分辨率的模式线
    #mode=173.00 1920 2048 2248 2576 1080 1083 1088 1120 -hsync +vsync
    #transform=flipped
    
    #[output]
    #name=X1
    #mode=1024x768
    #transform=flipped-rotate-270
    
    # 屏幕键盘输入法
    #[input-method]
    #path=/usr/lib/weston/weston-keyboard
    
    [keyboard]
    keymap_rules=evdev
    #keymap_layout=us,de
    #keymap_variant=colemak,
    #keymap_options=grp:shifts_toggle
    #keymap_options=caps:ctrl_modifier,shift:both_capslock_cancel
    repeat-rate=30
    repeat-delay=300
    
    # keymap_options from /usr/share/X11/xkb/rules/base.lst
    #numlock-on=true
    
    [terminal]
    font=monospace
    font-size=18
    
    [launcher]
    icon=/usr/share/weston/icon_flower.png
    path=/usr/bin/weston-flower
    
    [launcher]
    icon=/usr/share/icons/gnome/32x32/apps/utilities-terminal.png
    path=/usr/bin/weston-terminal --shell=/usr/bin/bash
    
    #[launcher]
    #icon=/usr/share/icons/gnome/32x32/apps/utilities-terminal.png
    #path=/usr/bin/gnome-terminal
    
    [launcher]
    icon=/usr/share/icons/hicolor/32x32/apps/firefox.png
    path=MOZ_ENABLE_WAYLAND=1 /usr/bin/firefox
    
    #[launcher]
    #icon=/usr/share/icons/Adwaita/32x32/apps/multimedia-volume-control.png
    #path=/usr/bin/st alsamixer -c0
    
最少 `weston.ini` 配置: 
    
    ~/.config/weston.ini
    
    [core]
    xwayland=true
    
    [keyboard]
    keymap_layout=us
    
    [launcher]
    icon=/usr/share/weston/terminal.png
    path=/usr/bin/weston-terminal
    
###  显示器

Weston 的输出与 `xorg.conf` 显示器的输出略有不同： 
    
    $ ls /sys/class/drm
    
    card0
    card0-VGA-1
    card1
    card1-DVI-I-1
    card1-HDMI-A-1
    card1-VGA-2
    
`card0` 是未使用的显卡(内置视频适配器)。附加适配器 `card1` 通过视频线连接到一个 HDMI 和一个 DVI 显示器，因此输出名称为 `HDMI-A-1` 和 `DVI-I-1`。 

### Xwayland

请参阅 [Wayland#Xwayland](<../zh-cn/Wayland.html#Xwayland> "Wayland") 了解可用软件包的详细信息和概述。 

设置以下内容以开启 Xwayland 的使用： 
    
    ~/.config/weston.ini
    
    [core]
    xwayland=true

**注意：** 如果尚未配置 X，则可能需要配置键盘映射： [Xorg中的键盘配置](<https://wiki.archlinux.org/title/Xorg/Keyboard%20configuration>)

###  高 DPI 显示器

对于 [Retina](<https://en.wikipedia.org/wiki/Retina_Display> "wikipedia:Retina Display") 或 [HiDPI](<../zh-cn/HiDPI.html> "HiDPI") 的显示器, 使用: 
    
    ~/.config/weston.ini
    
    [output]
    name=...
    scale=2
    
###  Weston 字体

Weston 使用默认的无衬线字体作为窗口标题栏、时钟等。有关如何更改此字体的说明，请参见[字体配置#设置默认和后备字体](<../zh-cn/%E5%AD%97%E4%BD%93%E9%85%8D%E7%BD%AE.html#%E8%AE%BE%E7%BD%AE%E9%BB%98%E8%AE%A4%E5%92%8C%E5%90%8E%E5%A4%87%E5%AD%97%E4%BD%93> "字体配置")。 

###  Systemd启动

weston虽没法作为systemd系统服务启动，但可通过[systemd用户](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "Systemd/用户")服务进行启动，我们先创建 weston 的[服务](<../zh-cn/Systemd.html> "守护程序")和 socket [单元](<../zh-cn/Systemd.html#%E6%9C%8D%E5%8A%A1%EF%BC%88service%EF%BC%89%E7%B1%BB%E5%9E%8B> "Systemd")。 

####  systemd用户服务启动

创建用户级weston套节字(socket) [单元](<../zh-cn/Systemd.html#%E6%9C%8D%E5%8A%A1%EF%BC%88service%EF%BC%89%E7%B1%BB%E5%9E%8B> "Systemd")，用于监听图形应用 

**提示：** 若您没有 `/etc/systemd/user/` 目录的权限，也可在 `$HOME/.config/systemd/user` 目录下进行创建，两者使用效果相同
    
    /etc/systemd/user/weston.socket
    
    [Unit]
    Description=Weston, a Wayland compositor
    Documentation=man:weston(1) man:weston.ini(5)
    Documentation=https://wayland.freedesktop.org/
    
    [Socket]
    ListenStream=%t/wayland-0
    
创建用户级weston服务(service)单元 
    
    /etc/systemd/user/weston.service
    
    [Unit]
    Description=Weston, a Wayland compositor, as a user service
    Documentation=man:weston(1) man:weston.ini(5)
    Documentation=https://wayland.freedesktop.org/
    
    # 使用 systemd 套接字激活
    Requires=weston.socket
    After=weston.socket
    
    # 由于我们是图形会话的一部分，因此请确保我们之前已启动
    Before=graphical-session.target
    
    [Service]
    Type=notify
    TimeoutStartSec=60
    WatchdogSec=20
    # 日志默认输出到journal
    #StandardOutput=journal
    StandardError=journal
    # 确保已创建最少配置 ~/.config/weston.ini
    ExecStart=/usr/bin/weston --modules=systemd-notify.so
    
    [Install]
    WantedBy=graphical-session.target
    
创建完毕后重新加载 `systemd --user daemon-reload` ，然后在使用 `systemd --user start weston.service` 启动weston 

以上的使用需要我们提前登录到系统，并手动运行，若想实现自动启动请参考下面步骤。 

####  systemd系统会话管理

一些场合下，我们希望在系统引导后自动启动weston，当然也支持ssh远程登录后手动启动weston，如您不想使用第三方[登录管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "登录管理器")，也可使用[systemd](<../zh-cn/Systemd.html> "Systemd")服务单元来完成该操作，下面使用sysemd服务来创建[用户会话](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "Systemd/用户")。 

**注意：** 访问`/etc/systemd/system/`要使用root权限,普通用户无法创建
    
    /etc/systemd/system/weston-autologin.service
    
    [Unit]
    Description=Weston graphical session
    
    # 确保我们在允许登录后启动。
    After=systemd-user-sessions.service
    
    # 如果需要，可以将其作为图形会话的一部分。
    #Before=graphical.target
    
    # 不是不需，但以防万一。
    #ConditionPathExists=/dev/tty7
    
    [Service]
    Type=simple
    Environment=XDG_SESSION_TYPE=wayland
    ExecStart=/usr/bin/systemctl --wait --user start weston-session.target
    
    # 要运行会话的用户。需要依据实际用户修改！
    User=user
    Group=user
    
    # 为 Weston 要求的用户设置完整的用户会话。
    PAMName=login
    
    # 需要一个虚拟终端。
    TTYPath=/dev/tty7
    TTYReset=yes
    TTYVHangup=yes
    TTYVTDisallocate=yes
    
    # 如果不控制 tty，则无法启动。
    StandardInput=tty-fail
    
    # 日志输出默认为journal
    #StandardOutput=journal
    StandardError=journal
    
    # 使用 utmp 记录此用户，让它显示命令 'w' 和 'who'
    UtmpIdentifier=tty7
    UtmpMode=user
    
    [Install]
    WantedBy=graphical.target
    
请确保 `User` 和 `Group` 条目是使用有效的[用户](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html> "用户和用户组")。同时还需创一个`weston-session.target`的用户[target](<../zh-cn/Systemd.html#%E7%9B%AE%E6%A0%87%EF%BC%88target%EF%BC%89> "Systemd")
    
    /etc/systemd/user/weston-session.target
    
    [Unit]
    Description=Weston session
    
    BindsTo=weston-session.target
    Before=weston-session.target
    
通知系统重新[加载](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd")配置 
    
     $ sudo systemd damon-reload
     $ systemd damon-reload --user
    
最后确保您的默认[target](<../zh-cn/Systemd.html#%E7%9B%AE%E6%A0%87%EF%BC%88target%EF%BC%89> "Systemd")使用的是graphical 
    
     $ sudo systemctl set-default graphical.target
     $ systemctl --user set-default graphical-session.target
    
##  提示与技巧

###  录像录制

Weston 具有内置的截屏和视频录制功能，可以通过按 `Super`+`r` 组合键来启动和停止。截屏视频保存到 Weston 当前工作目录中的文件 `capture.wcap` 中。WCAP 格式是 Weston 特有的无损视频格式，它只记录帧数的差异。为了能够播放录制的截屏视频，需要将WCAP文件转换为媒体播放器可以理解的格式。首先，将捕获转换为 YUV 像素格式： 
    
    $ wcap-decode --yuv4mpeg2 capture.wcap > capture.y4m
    
然后，可以使用 [FFmpeg](<../zh-cn/FFmpeg.html> "FFmpeg") 或 [x264](<https://archlinux.org/packages/?name=x264>)包 将 YUV 文件转码为其他格式（有关详细信息，请参阅 `x264 -h`）。 

###  窗口切换

要切换带有 `Super+Space` 而不是 `Super+Tab` 的窗口，请在 `desktop-shell/shell.c` 中将 `KEY_TAB` 更改为 `KEY_SPACE`，然后重新编译 [weston](<https://archlinux.org/packages/?name=weston>)包。 

###  触摸屏幕映射

触摸显示映射可以通过使用 [udev](<../zh-cn/Udev.html> "Udev") 规则来实现。就像 `WL_SEAT` 或 `ID_SEAT` 设备环境变量将设备绑定到指定的席位一样，`WL_OUTPUT` 变量可用于将设备绑定到相应的输出。此变量应与显示器名称匹配。有关显示器命名约定的说明，请参见 [#显示器](<#%E6%98%BE%E7%A4%BA%E5%99%A8>)。 

##  参考

  * [官方 Weston 项目Gitlab仓库](<https://gitlab.freedesktop.org/wayland/weston>)
  * [启动和运行Weston](<https://wayland.pages.freedesktop.org/weston/toc/running-weston.html>)
