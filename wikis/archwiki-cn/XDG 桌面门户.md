**翻译状态：**

  * 本文（或部分内容）译自 [XDG Desktop Portal](<https://wiki.archlinux.org/title/XDG_Desktop_Portal> "arch:XDG Desktop Portal")，最近一次同步于 2025-09-01，若英文版本有所[更改](<https://wiki.archlinux.org/title/XDG_Desktop_Portal?diff=0&oldid=841483>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/XDG_Desktop_Portal_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Flatpak](<../zh-cn/Flatpak.html> "Flatpak")
  * [PipeWire#WebRTC 屏幕共享](<../zh-cn/PipeWire.html#WebRTC_%E5%B1%8F%E5%B9%95%E5%85%B1%E4%BA%AB> "PipeWire")

引自 [Flatpak 文档](<https://docs.flatpak.org/zh-cn/latest/desktop-integration.html#portals>)： 

    门户是用于安全访问沙箱外资源的框架。沙箱内程序可以使用的特性包括：检测网络状态；使用文件选择器来打开文件；打开 URI；阻止设备睡眠、休眠或关机；打印；发送邮件；显示通知；截取屏幕或录屏［……］

门户（portals）系统最初专为 [Flatpak](<../zh-cn/Flatpak.html> "Flatpak") 应用程序设计，但任何应用程序均可借助门户访问跨桌面环境和 UI 框架的统一功能。这一功能得到了广泛使用，例如通过 [PipeWire](<../zh-cn/PipeWire.html> "PipeWire") 在 [Wayland](<../zh-cn/Wayland.html> "Wayland") 上实现[屏幕共享](<../zh-cn/PipeWire.html#WebRTC_%E5%B1%8F%E5%B9%95%E5%85%B1%E4%BA%AB> "PipeWire")，或让 [Firefox](<../zh-cn/Firefox.html> "Firefox") 采用与当前桌面环境相同 UI 框架的[文件打开/保存对话框](<../zh-cn/Firefox.html#KDE_%E9%9B%86%E6%88%90> "Firefox")。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [xdg-desktop-portal](<https://archlinux.org/packages/?name=xdg-desktop-portal>)包 以及至少一个 [#后端](<#%E5%90%8E%E7%AB%AF>)，该软件包包含一个 [systemd/用户](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "Systemd/用户")服务，通过 [D-Bus](<../zh-cn/D-Bus.html> "D-Bus") 自动触发启动。 

##  后端

当一个软件通过 XDG 桌面门户发起请求时，[xdg-desktop-portal](<https://archlinux.org/packages/?name=xdg-desktop-portal>)包 会将这个请求转发至可用的后端实现，由后端实现适合桌面环境的 UI，并访问特定于桌面环境的 API 处理诸如打开 URI、录制屏幕之类的请求。后端可以安装多个，例如使用 [Sway](<../zh-cn/Sway.html> "Sway") 可以安装 [xdg-desktop-portal-wlr](<https://archlinux.org/packages/?name=xdg-desktop-portal-wlr>)包 支持屏幕共享，并同时安装 [xdg-desktop-portal-gtk](<https://archlinux.org/packages/?name=xdg-desktop-portal-gtk>)包 作为后备，处理 [xdg-desktop-portal-wlr](<https://archlinux.org/packages/?name=xdg-desktop-portal-wlr>)包 未实现的接口。 

门户后端配置储存在 `/usr/share/xdg-desktop-portal/portals/*.portal` 中。门户后端配置文件包含其支持的接口和桌面环境。 

###  所有可用后端及其接口支持情况

后端 | 支持的桌面环境 | 使用的 UI 框架 | 接口支持情况   
---|---|---|---  
对话框 | 账户信息 | 应用程序选择器 | 后台活动 | 剪贴板 | 桌面启动项 | 电子邮件 | 文件选择器 | 全局快捷键 | 用户会话管理 | 输入设备捕获 | 系统通知 | 打印 | 远程桌面 | 屏幕录制 | 截屏 | 密钥 | 系统设置 | 壁纸   
[xdg-desktop-portal-cosmic](<https://archlinux.org/packages/?name=xdg-desktop-portal-cosmic>)包 | [COSMIC](<../zh-cn/COSMIC.html> "COSMIC") | iced | 是 | 否 | 否 | 否 | 否 | 否 | 否 | 是 | 否 | 否 | 否 | 否 | 否 | 否 | 是 | 是 | 否 | 是 | 否   
[xdg-desktop-portal-dde](<https://archlinux.org/packages/?name=xdg-desktop-portal-dde>)包 | [深度桌面环境](<../zh-cn/%E6%B7%B1%E5%BA%A6%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "深度桌面环境") |  [Qt](<../zh-cn/Qt.html> "Qt") 5 | 是 | 是 | 是 | 是 | 否 | 否 | 否 | 是 | 是 | 是 | 否 | 是 | 否 | 否 | 否 | 是 | 是 | 是 | 是   
[xdg-desktop-portal-gnome](<https://archlinux.org/packages/?name=xdg-desktop-portal-gnome>)包 | [GNOME](<../zh-cn/GNOME.html> "GNOME") |  [GTK](<../zh-cn/GTK.html> "GTK") 4 | 是 | 是 | 是 | 是 | 是 | 是 | 否 | 是 | 否 | 否 | 是 | 是 | 是 | 是 | 是 | 是 | 否 | 是 | 是   
[xdg-desktop-portal-gtk](<https://archlinux.org/packages/?name=xdg-desktop-portal-gtk>)包 | （通用） |  [GTK](<../zh-cn/GTK.html> "GTK") 3 | 是 | 是 | 是 | 否 | 否 | 是 | 是 | 是 | 否 | 是 | 否 | 是 | 是 | 否 | 否 | 否 | 否 | 是 | 否   
[xdg-desktop-portal-hyprland](<https://archlinux.org/packages/?name=xdg-desktop-portal-hyprland>)包 |  [Hyprland](<../zh-cn/Hyprland.html> "Hyprland")1 |  [Qt](<../zh-cn/Qt.html> "Qt") 6 | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 是 | 否 | 是 | 否 | 否 | 否 | 是 | 是 | 否 | 否 | 否   
[xdg-desktop-portal-kde](<https://archlinux.org/packages/?name=xdg-desktop-portal-kde>)包 | [KDE Plasma](<../zh-cn/KDE_Plasma.html> "KDE Plasma") |  [Qt](<../zh-cn/Qt.html> "Qt") 6 | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 否 | 是 | 否   
[xdg-desktop-portal-liri-git](<https://aur.archlinux.org/packages/xdg-desktop-portal-liri-git/>)AUR | [Liri](<../zh-cn/Liri.html> "Liri") |  [Qt](<../zh-cn/Qt.html> "Qt") 5 | 是 | 是 | 是 | 是 | 否 | 否 | 是 | 是 | 否 | 是 | 否 | 是 | 是 | 否 | 是 | 是 | 否 | 是 | 是   
[xdg-desktop-portal-lxqt](<https://archlinux.org/packages/?name=xdg-desktop-portal-lxqt>)包 | [LXQt](<../zh-cn/LXQt.html> "LXQt") |  [Qt](<../zh-cn/Qt.html> "Qt") 6 | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 是 | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 否   
[xdg-desktop-portal-td](<https://aur.archlinux.org/packages/xdg-desktop-portal-td/>)AUR | theDesk |  [Qt](<../zh-cn/Qt.html> "Qt") 6 | 是 | 是 | 否 | 否 | 否 | 否 | 否 | 是 | 否 | 否 | 否 | 是 | 否 | 否 | 否 | 是 | 否 | 是 | 否   
[xdg-desktop-portal-wlr](<https://archlinux.org/packages/?name=xdg-desktop-portal-wlr>)包 | wlroots | – | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 是 | 是 | 否 | 否 | 否   
[xdg-desktop-portal-xapp](<https://archlinux.org/packages/?name=xdg-desktop-portal-xapp>)包 |  [Cinnamon](<../zh-cn/Cinnamon.html> "Cinnamon")2 | – | 否 | 否 | 否 | 是 | 否 | 否 | 否 | 否 | 否 | 是 | 否 | 否 | 否 | 否 | 否 | 是 | 否 | 是 | 是   
  
  1. 适用于所有基于 wlroots 的混成器，但提供针对 [Hyprland](<../zh-cn/Hyprland.html> "Hyprland") 的额外功能，例如可在截屏或屏幕录制时共享单个窗口。
  2. 其也为 [MATE](<../zh-cn/MATE.html> "MATE") 和 [Xfce](<../zh-cn/Xfce.html> "Xfce") 提供部分支持。

除此以外，以下后端跨桌面环境实现了特定接口： 

  * [darkman](<https://archlinux.org/packages/?name=darkman>)包 实现了系统设置接口（仅颜色方案设置）。
  * [gnome-keyring](<https://archlinux.org/packages/?name=gnome-keyring>)包 实现了密钥接口。
  * [kwallet](<https://archlinux.org/packages/?name=kwallet>)包 实现了密钥接口。
  * [pikeru](<https://aur.archlinux.org/packages/pikeru/>)AUR 使用自己的 GUI 实现了文件选择器接口。
  * [xdg-desktop-portal-shana](<https://aur.archlinux.org/packages/xdg-desktop-portal-shana/>)AUR 通过将请求重定向至 GNOME/GTK/KDE/LXQt 后端实现了文件选择器接口。
  * [xdg-desktop-portal-termfilechooser-git](<https://aur.archlinux.org/packages/xdg-desktop-portal-termfilechooser-git/>)AUR 使用[终端文件选择器](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E5%B7%A5%E5%85%B7.html#%E6%8E%A7%E5%88%B6%E5%8F%B0> "应用程序列表/工具")实现了文件选择器接口。

##  配置

当收到请求时，`xdg-desktop-portal` 将会使用位于 `/usr/share/xdg-desktop-portal/_桌面环境_ -portals.conf` 的配置文件，其中 _桌面环境_ 由[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量") `XDG_CURRENT_DESKTOP` 决定。配置文件由桌面环境提供，决定应当使用的后端。 

如果需要自定义配置，或者使用的桌面环境并没有提供默认配置，可以创建门户配置文件 `$XDG_CONFIG_HOME/xdg-desktop-portal/portals.conf` 以决定全局或者特定接口使用的后端。如果使用多个桌面环境，也可以创建并配置特定桌面环境的配置文件 `$XDG_CONFIG_HOME/xdg-desktop-portal/_桌面环境_ -portals.conf`。 

例如，如果正在使用的桌面环境没有门户后端，希望使用[xdg-desktop-portal-gtk](<https://archlinux.org/packages/?name=xdg-desktop-portal-gtk>)包 作为通用后备后端，同时通过 [xdg-desktop-portal-lxqt](<https://archlinux.org/packages/?name=xdg-desktop-portal-lxqt>)包 使用 LXQt 文件选择器，可以使用以下配置： 
    
    ~/.config/xdg-desktop-portal/portals.conf
    
    [preferred]
    default=gtk
    org.freedesktop.impl.portal.FileChooser=lxqt

参见 [portals.conf(5)](<https://man.archlinux.org/man/portals.conf.5>)。 

###  桌面环境伪装

某些情况下（例如独立使用[窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")时），可能需要让 `xdg-desktop-portal` 以为正在使用特定的桌面环境。可以在 `xdg-desktop-portal.service` [用户单元](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "用户单元")中使用[附加配置片段](<../zh-cn/Systemd.html#%E9%99%84%E5%8A%A0%E9%85%8D%E7%BD%AE%E7%89%87%E6%AE%B5> "附加配置片段")添加环境变量 [XDG_CURRENT_DESKTOP](<../zh-cn/XDG_CURRENT_DESKTOP.html> "XDG CURRENT DESKTOP")。例如，可以指定使用 KDE 配置的后端： 
    
    ~/.config/systemd/user/xdg-desktop-portal.service.d/override.conf
    
    [Service]
    Environment="XDG_CURRENT_DESKTOP=KDE"

##  疑难解答

###  门户无法启动

要使 [xdg-desktop-portal-wlr](<https://archlinux.org/packages/?name=xdg-desktop-portal-wlr>)包 和 [xdg-desktop-portal-hyprland](<https://archlinux.org/packages/?name=xdg-desktop-portal-hyprland>)包 正常工作，必须在 [systemd 用户会话](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html#%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F> "Systemd/用户")中设置 `XDG_CURRENT_DESKTOP` 和 `WAYLAND_DISPLAY` 环境变量。 

`XDG_CURRENT_DESKTOP` 需要设置为混成器名称，例如 `XDG_CURRENT_DESKTOP=sway`。`WAYLAND_DISPLAY` 则由混成器自动设置。这两个变量通常会在混成器启动时自动设置，但如果 systemd 用户会话先于混成器启动，混成器启动时需要导入这两个变量。 

**注意：**[Hyprland](<../zh-cn/Hyprland.html> "Hyprland") 不会自动设置 `XDG_CURRENT_DESKTOP` 环境变量，需要手动配置。请参阅 [Hyprland Wiki](<https://wiki.hyprland.org/Configuring/Environment-variables/#xdg-specifications>)。

使用 `systemctl --user show-environment` 检查这些变量是否已设置。如果未设置，请在启动混成器时运行以下命令（例如，将其写入混成器的配置文件），将这些环境变量导入到 systemd 用户会话和 [D-Bus](<../zh-cn/D-Bus.html> "D-Bus") 中： 
    
    $ systemctl --user import-environment WAYLAND_DISPLAY XDG_CURRENT_DESKTOP
    $ dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP=_混成器名称_
    
**注意：** 这些环境变量需要在混成器启动时设置，通常通过混成器自身的配置完成，请参见混成器的文档说明。

**提示：**[Sway](<../zh-cn/Sway.html> "Sway") 提供了一个可自动完成此操作的插入文件，请参阅 [Sway#配置](<../zh-cn/Sway.html#%E9%85%8D%E7%BD%AE> "Sway")。

更多详情请参阅 [[1]](<https://github.com/emersion/xdg-desktop-portal-wlr#running>) 和 [[2]](<https://github.com/emersion/xdg-desktop-portal-wlr/wiki>)。 

###  在多显示器环境下使用 xdg-desktop-portal-wlr

`xdg-desktop-portal-wlr` 需要一个外部选择器来选择要共享的显示器。默认按顺序查找 [slurp](<https://archlinux.org/packages/?name=slurp>)包、[wofi](<https://archlinux.org/packages/?name=wofi>)包 和 [bemenu](<https://archlinux.org/packages/?name=bemenu>)包。若使用 slurp，收到屏幕共享请求后，鼠标指针会变成十字形，需要点击要共享的屏幕。若使用 wofi 或 bemenu，会出现一个可用显示器的菜单供选择。如果没有任何选择器可用，`xdg-desktop-portal-wlr` 会回退到找到的第一个显示器。详见 [xdg-desktop-portal-wlr(5) § SCREENCAST OPTIONS](<https://man.archlinux.org/man/xdg-desktop-portal-wlr.5#SCREENCAST_OPTIONS>)。 

###  KDE Plasma 下 GTK 应用程序字体渲染不佳

部分 GTK 应用程序在 Plasma 环境中需要安装 [xdg-desktop-portal-gtk](<https://archlinux.org/packages/?name=xdg-desktop-portal-gtk>)包 才能正确渲染字体。请安装该软件包，然后运行： 
    
    $ /usr/lib/xdg-desktop-portal --replace
    
###  GTK（可能还有其它的）文件选择器无法工作

如果应用程序通过 [Xwayland](<../zh-cn/Wayland.html#Xwayland> "Xwayland") 运行（最简单的检查方法是运行 `xeyes`，然后将鼠标指针移至应用程序窗口内，若程序运行在 [Xwayland](<../zh-cn/Wayland.html#Xwayland> "Xwayland") 下，其中眼睛会看向鼠标指针），那么 `xdg-desktop-portal-gtk` 会按需启动，但在选择文件后可能没有任何反应。这种情况下，为 `xdg-desktop-portal-gtk` 的环境添加 `DISPLAY=:0` 可能会解决问题。要实现此操作，可以按照前文（[#门户无法启动](<#%E9%97%A8%E6%88%B7%E6%97%A0%E6%B3%95%E5%90%AF%E5%8A%A8>)）关于 `import-environment` 的说明进行设置，或者直接编辑 `xdg-desktop-portal-gtk` 的 systemd 用户单元文件。此外，也可以尝试通过配置开启应用程序的原生 [Wayland](<../zh-cn/Wayland.html> "Wayland") 支持（例如[对于 Electron 程序](<../zh-cn/Wayland.html#Electron> "Wayland")）。 

##  参见

  * [项目主页](<https://flatpak.github.io/xdg-desktop-portal/>)
  * [门户文档](<https://flatpak.github.io/xdg-desktop-portal/docs/>)：列出了应用程序和后端可使用的所有接口。
