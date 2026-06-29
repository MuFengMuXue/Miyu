**翻译状态：**

  * 本文（或部分内容）译自 [LXQt](<https://wiki.archlinux.org/title/LXQt> "arch:LXQt")，最近一次同步于 2024-09-22，若英文版本有所[更改](<https://wiki.archlinux.org/title/LXQt?diff=0&oldid=816996>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/LXQt_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [LXDE](<../zh-cn/LXDE.html> "LXDE")
  * [桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")
  * [窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")

2013 伊始，洪任谕（“PCMan”）启动了将 [LXDE](<../zh-cn/LXDE.html> "LXDE") 移植到 [Qt](<../zh-cn/Qt.html> "Qt") 的项目。LXDE-Qt 的[首个预览版](<https://blog.lxde.org/?p=1013>)于 2013 年 7 月 3 日发布。2013 年 7 月 21 日，Razor-qt（一个与 LXDE 设计相似的桌面）与 LXDE 宣布合并。 

于是 [LXQt](<https://lxqt-project.org>) （the Lightweight Qt Desktop Environment）诞生了。这个桌面集合了 Razor-qt 和 LXDE 的组件。尽管 LXDE 目前的精力已经集中到 LXQt 的开发上，GTK2 版本的 LXDE 依然在维护。 目前，LXQT已经初步支持[Wayland](<../zh-cn/Wayland.html> "Wayland")。 

##  安装

首先，安装并配置 [Xorg](<../zh-cn/Xorg.html> "Xorg")。随后[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [lxqt](<https://archlinux.org/groups/x86_64/lxqt/>)包组 包组和一个图标主题（如 [breeze-icons](<https://archlinux.org/packages/?name=breeze-icons>)包 或 [oxygen-icons](<https://archlinux.org/packages/?name=oxygen-icons>)包）。 

你还可以安装以下附加功能包： 

  * **nm-tray** — 一个简单的基于Qt的NetworkManager前端。

     <https://github.com/palinek/nm-tray> || [nm-tray](<https://aur.archlinux.org/packages/nm-tray/>)AUR

  * **[SDDM](<../zh-cn/SDDM.html> "SDDM")** — LXQt 推荐的显示管理器。

     <https://github.com/sddm/sddm> || [sddm](<https://archlinux.org/packages/?name=sddm>)包

  * 如果需要，可安装锁屏组件，比如 [slock](<https://archlinux.org/packages/?name=slock>)包 或 [xscreensaver](<https://archlinux.org/packages/?name=xscreensaver>)包。二者均已包含在 LXQt 安装包中，其它锁屏程序也可能会集成其中。 
    * 如果您使用 [LightDM](<../zh-cn/LightDM.html> "LightDM") 作为显示管理器，则可以使用 [light-locker](</wzh/index.php?title=Light-locker&action=edit&redlink=1> "Light-locker（页面不存在）")。
    * 如果要在挂起/休眠时禁用屏幕锁定，请在 _LXQt > 首选项 > LXQt设置 > 会话设置 > 挂起/休眠之前锁定屏幕_下勾选相应复选框。

**提示：** LXQt 在会话中使用 [xdg-utils](<https://archlinux.org/packages/?name=xdg-utils>)包 中的 _xdg-screensaver_ 作为屏幕锁，它只能与 XScreenSaver 和 [xautolock](<https://archlinux.org/packages/?name=xautolock>)包 配合工作。可以使用它或自行选用其他屏幕锁。例如，要使用 _slock_ ，可以遵照 [Slock#Lock on suspend](<../zh-cn/Slock.html#Lock_on_suspend> "Slock") 并安装打过补丁的 [xdg-utils-slock](<https://aur.archlinux.org/packages/xdg-utils-slock/>)AUR 来获得符合 LXQt 设计期望的感觉。

  * 你可以编辑 `~/.config/lxqt/lxqt.conf` 并添加你的锁屏选项而不需要[xautolock](<https://archlinux.org/packages/?name=xautolock>)包 ，比如使用i3lock需要添加以下内容：

    [Screensaver]
    lock_command=i3lock
    
  * 对于音频，请参阅 [General recommendations#声音](<../zh-cn/General_recommendations.html#%E5%A3%B0%E9%9F%B3> "General recommendations")。

  * 某些 LXQt 面板插件需要安装额外的包来发挥功能，请查阅 [lxqt-panel](<https://archlinux.org/packages/?name=lxqt-panel>)包 的[可选依赖](<../zh-cn/PKGBUILD.html#optdepends> "PKGBUILD")。

##  启动桌面

###  使用 xinit

在 [Xinitrc](<../zh-cn/Xinit.html#xinitrc> "Xinitrc") 中添加: 
    
    ~/.xinitrc
    
    exec startlxqt

###  图形界面登入

在[显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")的桌面菜单中选择 _LXQt Desktop_. 

##  配置

LXQt 通常能通过尝试使用 GUI 应用程序修改其设置。它的配置文件位于 `~/.config/lxqt` 目录中。这个目录会被自动初始化，新用户的默认配置可在 `/usr/share/lxqt` 中找到。 

###  屏幕亮度

如果你发现 LXQt 的亮度快捷键调整屏幕对比度而非亮度，你可以在 LXQt 配置中心 > 快捷键修改来让亮度快捷键调用 xbacklight 命令。 
    
    xbacklight -inc 10
    xbacklight -dec 10
    
如果使用英特尔内核模式设置，xbacklight 将无法正常工作，但是可以使用下列命令代替实现功能 
    
    pkexec lxqt-backlight_backend --inc
    pkexec lxqt-backlight_backend --dec
    
要让快捷键正常工作，可能需要创建两个脚本来上下调节屏幕亮度，然后将快捷键指向脚本路径。 

另一个改变屏幕亮度的方法是使用 [brightnessctl](<https://archlinux.org/packages/?name=brightnessctl>)包。 

###  面板部件

如果无法将“CPU 统计信息”和“系统统计信息”部件添加到面板中，请确保已安装 [libstatgrab](<https://archlinux.org/packages/?name=libstatgrab>)包 和 [libsysstat](<https://archlinux.org/packages/?name=libsysstat>)包。 

###  使用不同的窗口管理器

LXQt 显示一个对话框，用于在首次登录时选择首选的[窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")。之后，您可以通过 _会话设置_ ， `lxqt-config-session` 指定用于 LXQt 的不同窗口管理器;或通过编辑 `~/.config/lxqt/session.conf`。更改以下行： 
    
    window_manager=_current_window_manager_
    
改为想选择的某个[窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")： 
    
    window_manager=_想选择的窗口管理器_
    
###  自动启动

要在登录的时候启动 X 应用程序，在 LXQt 主菜单中依次点击 _首选项 > LXQt 设置 > LXQt 会话设置_。此外，也可以通过下面命令启动： 
    
    $ lxqt-config-session
    
从这个窗口中，点击左侧的 _自动启动_ 。将程序添加到全局自动启动 (程序会在所有实现了 [XDG Autostart](<../zh-cn/XDG_Autostart.html> "XDG Autostart") 规范的会话中启动) 或本地自动启动 (标记为 LXQt 自动启动) (参见 [issue 746](<https://github.com/lxqt/lxqt/issues/746>) 获取此选项的 Bug 信息)。对于每个添加的项目，`lxqt-config-session` 会在相应的 [XDG Autostart](<../zh-cn/XDG_Autostart.html> "XDG Autostart") 目录中创建一个 Desktop 条目 (即 _.desktop_ 文件)。 

_全局自动启动_ 和 _LXQt 自动启动_ 间的区别不取决于相应的 .desktop 文件位于什么目录，而是取决于 `OnlyShowIn` 设置。如果 `OnlyShowIn=true`，则将项目视为 _LXQt 自动启动_ 。此外，如果 `X-LXQt-Module=true`，则项目不会显示在 `lxqt-config-session` 中。 

###  设置环境变量

LXQt 会话的[环境变量](<../zh-cn/Environment_variables.html> "Environment variables")在 _会话设置_ 中定义。 

###  编辑应用程序菜单

可以通过编辑 `/usr/share/applications/lxqt-*.desktop` 中的 _.desktop_ 文件修改菜单，参阅[桌面配置项](<../zh-cn/Desktop_entries.html> "Desktop entries")。 

###  主题

摘自[官方wiki](<https://github.com/lxqt/lxqt/wiki/Theming>)： 

LXQt 主题是 [qss样式表](<http://doc.qt.io/qt-4.8/stylesheet.html>)。它们要么位于 `/usr/share/lxqt/themes/`，要么位于`~/.local/share/lxqt/themes`。到目前为止，可以使用以下主题： 

  * Ambiance
  * Arch Colors
  * Clearlooks
  * Dark
  * Frost
  * KDE-Plasma
  * Kvantum
  * Leech
  * Light
  * Silver
  * System (普通小部件主题)
  * Valendas

可以在[这里](<https://github.com/lxde/lxqt/issues/572>)关注一些关于主题的讨论。请注意，将“系统”主题与Qt小部件样式Breeze，Oxygen或Qtcurve一起使用会导致任务管理器按钮中出现未剪切的文本。 为了提高某些主题的透明度，需要合成器。只有 Breeze、Oxygen 和 Kvantum 小部件样式支持所有面板菜单的透明度。 如果有人对没有自定义主题的环境外观感兴趣，请创建以下文件（如果<prefix>是 /usr）： 

`mkdir /usr/share/lxqt/themes/notheme`

`touch /usr/share/lxqt/themes/notheme/lxqt-panel.qss`

然后在 中 `lxqt-config-appearance` 选择 Notheme。 

##  提示与技巧

###  屏幕混成器

可以用下列命令将 [picom](<https://archlinux.org/packages/?name=picom>)包 等混成器应用添加到自动启动应用当中： 
    
    picom --vsync -r 12 --no-fading-openclose -b
    
###  自定义离开菜单

只需将软件各自提供的 `.desktop` 文件复制到 `~/.local/share/applications` 并将其修改为包含 `NoDisplay=true` 指令，就可以自定义“离开”下可用的选项。 

参考：[#876](<https://github.com/lxqt/lxqt/issues/876>)。 

要考虑屏蔽的文件的完整列表包括： 
    
    lxqt-hibernate.desktop
    lxqt-leave.desktop
    lxqt-lockscreen.desktop
    lxqt-logout.desktop
    lxqt-reboot.desktop
    lxqt-shutdown.desktop
    lxqt-suspend.desktop
    
例子：要移去“休眠”选项： 
    
    $ mkdir -p ~/.local/share/applications
    $ sed '/OnlyShowIn/aNoDisplay=true' </usr/share/applications/lxqt-hibernate.desktop >~/.local/share/applications/lxqt-hibernate.desktop
    
##  故障排除

###  桌面图标聚拢在一块

在桌面上移动图标时，可能会将它们彼此放得太近而粘连在一起。如果实在没办法把它们分开，请在会话设置中停用桌面，移除 `~/.config/pcmanfm-qt/lxqt/desktop-items-0.conf` 后再启动桌面。 

###  用 [Xrdp](<../zh-cn/Xrdp.html> "Xrdp") 运行LXQt

使用 [Xrdp](<../zh-cn/Xrdp.html> "Xrdp") 运行 LXQt 进行远程登录的好处是快速方便，同时最大限度地减少服务器上的资源消耗。设置 [Xrdp](<../zh-cn/Xrdp.html> "Xrdp") 相当轻松，只需要用户调整 `~/.xinitrc` 。由于 LXQt 似乎依赖于某些 D-Bus 服务功能，因此该文件的末尾应该有以下行[[1]](<https://gist.github.com/valorad/443b076f42877a657847df8c77d36dc4>)： 
    
    exec dbus-run-session -- startlxqt
    
##  参阅

  * [LXQt 主页](<https://lxqt-project.org>)
  * [LXQt 开发相关信息](<https://github.com/lxde/lxqt>)
  * [在deviantART上的LXQt相关内容](<https://lxqt-de.deviantart.com/>)
  * [LXQt在GitHub上的维基页面信息](<https://github.com/lxde/lxqt/wiki>)
