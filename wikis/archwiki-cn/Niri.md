**翻译状态：**

  * 本文（或部分内容）译自 [Niri](<https://wiki.archlinux.org/title/Niri> "arch:Niri")，最近一次同步于 2025-11-14，若英文版本有所[更改](<https://wiki.archlinux.org/title/Niri?diff=0&oldid=850551>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Niri_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

Niri 是一个可滚动的平铺式 [Wayland](<../zh-cn/Wayland.html> "Wayland") 合成器。与 [Sway](<../zh-cn/Sway.html> "Sway") 或 [Hyprland](<../zh-cn/Hyprland.html> "Hyprland") 不同的地方在于，Niri 将窗口排列在一个无限延伸的水平桌面上，你可以向左或向右滚动（当然也可以实现更复杂的布局）。它类似于 [GNOME](<../zh-cn/GNOME.html> "GNOME") 的 PaperWM 和 [KDE](<../zh-cn/KDE.html> "KDE") 的 Karousel。 

##  安装

可以通过[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [niri](<https://archlinux.org/packages/?name=niri>)包 来获取 Niri。 

此外，为了获得更好的使用体验，你可能还需要安装以下软件： 

  * **[fuzzel](<https://archlinux.org/packages/?name=fuzzel>)** ：Niri 的默认应用启动器
  * **[mako](<https://archlinux.org/packages/?name=mako>)** ：通知管理器
  * **[waybar](<https://wiki.archlinux.org/title/Waybar> "en:Waybar")** ：Wayland 状态栏
  * **[xdg-desktop-portal-gtk](<https://archlinux.org/packages/?name=xdg-desktop-portal-gtk>)** 、**[xdg-desktop-portal-gnome](<https://archlinux.org/packages/?name=xdg-desktop-portal-gnome>)** ：用于实现屏幕共享功能
  * **[alacritty](<../zh-cn/Alacritty.html> "Alacritty")** ：Niri 的默认终端
  * **[swaybg](<https://archlinux.org/packages/?name=swaybg>)** ：设置桌面背景图片
  * **[swayidle](<https://archlinux.org/packages/?name=swayidle>)** 、**[swaylock](<https://archlinux.org/packages/?name=swaylock>)** ：用于在空闲时锁定屏幕
  * **[xwayland-satellite](<https://archlinux.org/packages/?name=xwayland-satellite>)** ：用于运行 X11 应用程序
  * **[udiskie](<https://archlinux.org/packages/?name=udiskie>)** ：用于管理和自动挂载 USB 驱动器

##  启动

Niri 附带了一个可以被[显示管理器](<../zh-cn/Display_manager.html> "Display manager")执行的 [桌面项](<../zh-cn/Desktop_entries.html> "Desktop entries")。在显示管理器中选择它将会启动 `niri-session`。`niri-session` 会把 [环境变量](<../zh-cn/Environment_variables.html> "Environment variables")导入至[systemd](<../zh-cn/Systemd.html> "Systemd"). 

你也可以从 [getty](<../zh-cn/Getty.html> "Getty") 执行: 
    
    niri-session
    
这可以结合[Getty#自动登录到虚拟控制台](<../zh-cn/Getty.html#%E8%87%AA%E5%8A%A8%E7%99%BB%E5%BD%95%E5%88%B0%E8%99%9A%E6%8B%9F%E6%8E%A7%E5%88%B6%E5%8F%B0> "Getty")来实现一个无缝的[启动](<../zh-cn/Arch_boot_process.html> "Arch boot process")体验。 

##  配置

Niri 从 `~/.config/niri/config.kdl` 读取配置文件。它是一个有多个部分的 KDL 文件。首次启动创建的配置文件通过注释给出了默认的选项设置。然而，随着更新所引入的新选项并不会在用户的配置中所体现，你可能需要查看 [Niri 官方文档](<https://yalter.github.io/niri/Configuration%3A-Introduction.html>)。 

Niri 在配置文件保存时会自动应用更改。无效的配置在自动应用更改时并不会使 Niri 崩溃，而是会保留上一次可工作的状态，并提醒用户配置文件无效。 可以执行 `niri validate` 来在 Niri 会话外检查配置是否有效。 

###  键盘布局

要配置键盘布局，编辑 `input/keyboard/xkb` 部分. 

例如，假设你想要有一个 `CapsLock` 当作 `Ctrl` 的 "US Int Alt Gr" 布局： 
    
    ~/.config/niri/config.kdl
    
    input {
        keyboard {
            xkb {
                layout "us"
                variant "altgr-intl"
                options "ctrl:nocaps"
            }
        }
        ...
    }
    
###  显示输出

首先执行 `niri msg outputs` 以获取所有 Niri 识别到的输出。然后你可以给每个显示器应用配置。例如设置 HDMI 显示器为 2560x1440 60Hz 并有 1.2 倍缩放，且关闭笔记本显示器，可以这样设置： 
    
    ~/.config/niri/config.kdl
    
    output "HDMI-A-1" {
        mode "2560x1440@60.000"
        scale 1.2
    }
    
    output "eDP-1" {
        off
    }
    
####  使用 kanshi 来动态设置布局

你也可以使用 [kanshi](<../zh-cn/Kanshi.html> "Kanshi") 来动态设置布局，例如当你想要在连接至外部显示器时关闭内置显示器。 

###  按键绑定

这一部分允许配置各种 Niri 可用的快捷键。很多已经在初次启动时生成的默认配置中配置好了。它们都可以重新改为其他按键。 

请注意 Niri _不_ 加载任何默认的绑定。若一个绑定没有在配置文件中指定，那么它就不会生效。“默认”只是在自动生成的配置文件中提供的。因此，在移除它们时请小心。建议使用注释来注释掉不需要的绑定。 

按键绑定的设置要通过使用修饰键和`+`号以及在大括号内写上要执行的动作。'spawn' 这个动作会启动指定的程序。例如，你会有这样的按键绑定：`Mod+T` 启动 [alacritty](<../zh-cn/Alacritty.html> "Alacritty") 以及 `Mod+D` 启动 [fuzzel](<https://archlinux.org/packages/?name=fuzzel>)包。默认配置下直接运行 Niri 时 `Mod` 一般是 `Super` 键，当它在其他环境下作为一个窗口运行时则是 `Alt` 键。 
    
    ~/.config/niri/config.kdl
    
    binds {
        ...
        Mod+T { spawn "alacritty"; }
        Mod+D { spawn "fuzzel"; }
        ...
    }
    
注意使用 `spawn` 时所有用空格分开的参数都需要用引号包裹： 
    
    ~/.config/niri/config.kdl
    
    binds {
        ...
        Mod+Ctrl+semicolon {
            spawn "swaylock" "-c" "121212" "-e" "-f" "-F"
        }
        ...
    }
    
####  WASD-式操作

可以配置 Niri 的工作区、窗口切换快捷键类似于游戏中的 WASD 那样： 
    
    ~/.config/niri/config.kdl
    
    binds {
        ...
        Mod+A { focus-column-left; }
        Mod+S { focus-window-or-workspace-down; }
        Mod+W { focus-window-or-workspace-up; }
        Mod+D { focus-column-right; }
        ...
    }
    
注意这可能也需要更改其他的绑定。同时，一些人可能会喜欢在右手侧配置，或是 Vim 式的操作。 

###  自动启动

Niri 可以让某些程序随 Niri 一起启动。 例如上面提到的程序，比如 [mako](<https://archlinux.org/packages/?name=mako>)包, [waybar](<https://archlinux.org/packages/?name=waybar>)包 和 [swayidle](<https://archlinux.org/packages/?name=swayidle>)包/[swaylock](<https://archlinux.org/packages/?name=swaylock>)包 可以这样配置 
    
    ~/.config/niri/config.kdl
    
    spawn-at-startup "mako"
    spawn-at-startup "waybar"
    spawn-at-startup "swayidle" "-w" "timeout" "601" "niri msg action power-off-monitors" "timeout" "600" "swaylock -f" "before-sleep" "swaylock -f"
    
注意这些进程被绑定到了 Niri 的会话，使得当 Niri 退出**或** 挂起时，它们也会被杀死。为使它们能持续运行，你可能需要通过添加 `"&"` 参数来把它们设置成后台任务。 

### XWayland

Niri 不提供 XWayland 支持来运行 X11 应用。它推荐使用 [xwayland-satellite](<https://archlinux.org/packages/?name=xwayland-satellite>)包 这个外部工具来作为替代。这个包被列到了可选依赖中，安装它之后不需要做额外的配置。 

##  另见

  * [Niri's own wiki](<https://yalter.github.io/niri/>)
