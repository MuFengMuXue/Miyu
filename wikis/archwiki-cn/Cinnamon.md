**翻译状态：**

  * 本文（或部分内容）译自 [Cinnamon](<https://wiki.archlinux.org/title/Cinnamon> "arch:Cinnamon")，最近一次同步于 2020-07-23，若英文版本有所[更改](<https://wiki.archlinux.org/title/Cinnamon?diff=0&oldid=623968>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Cinnamon_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Nemo](</wzh/index.php?title=Nemo&action=edit&redlink=1> "Nemo（页面不存在）")
  * [Desktop environment](<../zh-cn/Desktop_environment.html> "Desktop environment")

[Cinnamon](<https://github.com/linuxmint/Cinnamon>) 是一个提供先进创新的特点和传统的用户体验的 Linux 桌面。不过，其底层技术实质是基于 [GNOME](<../zh-cn/GNOME.html> "GNOME") 的分支。 截至 2.0 版本，Cinnamon 就已经是一个完整的桌面环境，不仅仅是 GNOME Shell 和 Unity 的前端了。 

##  安装

Cinnamon 可通过 [cinnamon](<https://archlinux.org/packages/?name=cinnamon>)包 软件包进行[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")。 

**注意：** 如果您有英特尔的 GPU，请确保 [不要在 xf86-video-intel 驱动下使用](<../zh-cn/Intel_graphics.html#Installation> "Intel graphics") Cinnamon，因为这会导致随机冻屏的问题 (但是仍可移动鼠标)。可使用 [modesetting(4)](<https://man.archlinux.org/man/modesetting.4>) 驱动代替，而不必移除 [xf86-video-intel](<https://archlinux.org/packages/?name=xf86-video-intel>)包 (KDE 也 [建议这样做](<https://community.kde.org/Plasma/5.9_Errata#Intel_GPUs>))。

###  Cinnamon 应用

Cinnamon 引入了基于 GNOME 核心应用程序的 X-App，但是这些应用已经进行了修改，可在 Cinnamon、MATE 和 XFCE 上使用；这些应用具有传统的用户界面 (UI)。 

应用  | GNOME  | Cinnamon   
---|---|---  
文字编辑器  | Gedit/Pluma  |  [xed](<https://archlinux.org/packages/?name=xed>)包  
图片查看器  | Eye of GNOME  |  [xviewer](<https://aur.archlinux.org/packages/xviewer/>)AUR  
文档阅读器  | Evince/Atril  |  [xreader](<https://archlinux.org/packages/?name=xreader>)包  
媒体播放器  | Totem  |  [xplayer](<https://aur.archlinux.org/packages/xplayer/>)AUR  
图像管理器  | gThumb  |  [pix](<https://aur.archlinux.org/packages/pix/>)AUR  
  
###  后备模式

当 Cinnamon 发生崩溃事件时, 会激活其 _后备_ 模式。要控制此模式下打开的窗口，需要安装 [metacity](<https://archlinux.org/packages/?name=metacity>)包 软件包以及 [gnome-shell](<https://archlinux.org/packages/?name=gnome-shell>)包 以显示任务栏。 

##  启动

###  图形化登录

在喜欢的[显示管理器](<../zh-cn/Display_manager.html> "Display manager")中选择 _Cinnamon_ 或 _Cinnamon (Software Rendering)_ 。 _Cinnamon_ 选项是启用了 3D 加速的会话，一般情况下请使用这个。如果显卡驱动出现问题，可以试试 _Cinnamon (Software Rendering)_ ，它禁用了 3D 加速功能。 

###  手动启动 Cinnamon

如果您喜欢从控制台启动 Cinnamon，可添加以下行到 [Xinitrc](<../zh-cn/Xinit.html#xinitrc> "Xinitrc"): 
    
    ~/.xinitrc
    
     exec cinnamon-session
    
如果想用 _Cinnamon (Software Rendering)_ ，请用 `cinnamon-session-cinnamon2d` 代替 `cinnamon-session`。 

###  重启 Cinnamon

从命令行中执行以下行: 
    
    $ nohup cinnamon --replace > /dev/null 2>&1 &
    
##  配置

Cinnamon 很容易配置，大部分的配置都可在图形化界面下完成。更多详情可查看以下网站 [applets](<https://cinnamon-spices.linuxmint.com/applets>)，[extensions](<https://cinnamon-spices.linuxmint.com/extensions>) 和 [theming](<https://cinnamon-spices.linuxmint.com/themes>). 

###  Cinnamon 系统设置

_cinnamon-settings_ 可在命令行中启动指定的设置模块。如果后面没有跟随 (正确的) 参数，它将启动 _System Settings_ (系统设置)。例如，要启动面板 (panel) 设置： 
    
    $ cinnamon-settings panel
    
列出所有可用的模块： 
    
     $ pacman -Ql cinnamon | awk -F'[_.]' '/cs_.+\.py/ {print $2}'
    
打印机
    安装 [system-config-printer](<https://archlinux.org/packages/?name=system-config-printer>)包 进行打印机配置。
网络
    要添加网络模块的支持, 请启用 [Network Manager](<../zh-cn/NetworkManager.html#Configuration> "NetworkManager")。要在 Network Manager 里面保存 Wifi 密码，需要安装 [GNOME Keyring](<../zh-cn/GNOME_Keyring.html> "GNOME Keyring")。
蓝牙
    要添加蓝牙设备支持，请安装软件包 [blueberry](<https://archlinux.org/packages/?name=blueberry>)包。

###  应用程序和扩展

许多 Cinnamon 的应用程序和扩展可以在 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") ([package search](<https://aur.archlinux.org/packages?O=0&K=cinnamon-&do_Search=Go>)) 中找到，也可以在 Cinnamon 的“小程序”和“拓展”中找到 (_在线获取更多_ 选项卡中): 
    
    $ cinnamon-settings applets
    $ cinnamon-settings extensions
    
也可以从 [Cinnamon spices](<https://cinnamon-spices.linuxmint.com/>) 下载并手动安装。 

**注意：** 如果你安装后没有发现这些拓展或者是应用程序, 按下 `Alt+F2` 并在对话框键入 `r` 重启 Cinnamon。

###  按下电源按钮睡眠

这是电源按钮的默认行为。如需更改，打开 `cinnamon-settings` 面板进入**系统设置** ，点击**电源管理** 。更改**按下电源按钮时** 选项，选择你所希望使用的操作。 

###  管理 Cinnamon 使用的语言

**注意：** Cinnamon 控制面板从 2.2 版本开始删除了语言配置模块 [[1]](<http://segfault.linuxmint.com/2014/04/cinnamon-2-2/>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-17 ⓘ]

  * 要添加删除语言，请查看 [Locale](<../zh-cn/Locale.html> "Locale")。
  * 要在启用的语言间切换，请安装软件包 [mintlocale](<https://aur.archlinux.org/packages/mintlocale/>)AUR。
  * 要在 Cinnamon 中正确显示另外的语言，请安装 [cinnamon-translations](<https://archlinux.org/packages/?name=cinnamon-translations>)包 软件包。
  * 要修改键盘布局: **系统设置 > 硬件 > 键盘 > 布局**。

###  使用不同的窗口管理器

Cinnamon 目前不支持这样做。 

##  提示与技巧

###  创建自定义应用程序

关于创建自定义应用程序，可以在[这里](<https://projects.linuxmint.com/reference/git/cinnamon-tutorials/write-applet.html>)找到教程。 

###  默认的桌面背景壁纸路径

当在 Cinnamon 设置自定义的路径的壁纸时，Cinnamon 会将其复制到 `~/.cinnamon/backgrounds`. 因此，每次改变你的壁纸时，你都得再次在设置菜单添加你的墙纸到/或将其复制到 `~/.cinnamon/backgrounds`。 

此外， Mint 的官方壁纸在每次大版本发行时都会放出供自由使用。查看 [AUR](<https://aur.archlinux.org/packages/?O=0&K=mint-backgrounds>)。 

###  显示 "家目录" 和文件系统桌面图标

默认情况下 Cinnamon 在启动时就会启用桌面图标，但是不会在屏幕上显示它们。要显示家目录、文件系统、回收站、已挂载的卷和网络服务的图标，请打开 Cinnamon 的设置，然后点击 桌面。点上要在屏幕上看到的图标的复选框。 

###  菜单编辑器

菜单小程序支持自定义命令。右键单击"菜单"小程序，然后点击"配置..."，然后点击“打开菜单编辑器”。选择一个子菜单（或者创建一个新的子菜单），然后选择“新建项目”。填好名称、命令和备注。如果需要在终端运行，选中“在终端运行”复选框，图形化应用程序不选中“在终端运行”复选框。然后点击”确定“并关闭菜单编辑器。启动器就添加到了菜单。 

###  工作空间

可以将工作空间调度器添加到面板。右键单击面板，然后选择 _将小程序添加到面板_ 选项。将 _工作空间切换_ 小程序添加到面板中。要更改其位置，请在面板上单击鼠标右键，然后将 _面板编辑模式_ 的开关更改为打开 (On)。点击将切换器拖动到所需位置，并在完成后关闭面板编辑模式。 

默认情况下，有两个工作空间。要添加更多，请按 `Ctrl+ Alt +上键` 显示所有的工作空间，然后点击右边的加号按钮在屏幕添加更多的工作空间。 

此外，还可以在命令行中选择数字进行切换： 
    
    $ gsettings set org.cinnamon.desktop.wm.preferences num-workspaces 4
    
将 4 替换为想要切换到的工作空间编号。 

###  隐藏桌面图标

默认情况下，[Nemo](</wzh/index.php?title=Nemo&action=edit&redlink=1> "Nemo（页面不存在）") 中启用了桌面图标渲染功能。要禁用这个功能，用下面命令行改变设置： 
    
    $ gsettings set org.nemo.desktop show-desktop-icons false
    
###  主题、图标和背景

Linux Mint 风格的主题、图标和背景可通过安装 [mint-themes](<https://aur.archlinux.org/packages/mint-themes/>)AUR, [mint-x-icons](<https://aur.archlinux.org/packages/mint-x-icons/>)AUR, [mint-y-icons](<https://aur.archlinux.org/packages/mint-y-icons/>)AUR 和 [mint-backgrounds](<https://aur.archlinux.org/packages/mint-backgrounds/>)AUR 软件包获得。 因而，最后者是所有 Linux Mint 版本中包含的所有背景 (图片) 的集合。AUR 上还提供了各个 Linux Mint 版本的背景。 

主题和图标可在 `设置 → 主题` 中编辑。背景则在 `设置 → 背景` 中。 

官方 Linxu Mint Cinnamon 主题也包含在了 [mint-themes](<https://aur.archlinux.org/packages/mint-themes/>)AUR 软件包内。 

可以如下这样在 Shell 中设置桌面主题： 
    
    $ gsettings set org.cinnamon.theme name "_Theme-Name_ "
    
###  声音效果

Cinnamon 不附带用于桌面启动之类事件的声音 (它们是 Linux Mint 默认使用的声音效果)。这些声音效果可与安装 [mint-artwork](<https://aur.archlinux.org/packages/mint-artwork/>)AUR。声音事件可以在 `设置 → 声音 → 声音效果` 中编辑。 

###  调整窗口的大小

用 Alt+右键 调整窗口的大小，使用 gsettings： 
    
    $ gsettings set org.cinnamon.desktop.wm.preferences resize-with-right-button true
    
###  截图

[截一个图](<../zh-cn/Taking_a_screenshot.html#Cinnamon> "Taking a screenshot")这篇文章中有讲到，安装 [gnome-screenshot](<https://archlinux.org/packages/?name=gnome-screenshot>)包 就能有截图功能了。 默认快捷键为 `Prt Sc`，可以在小程序的 _快捷键 > 系统 > 截图与录像_下的 _菜单 > 偏好设置 > 键盘_中更改。默认保存目录为 `$HOME/Pictures`, 不过可以像下面这样自定义路径： 
    
    $ gsettings set org.gnome.gnome-screenshot auto-save-directory file:///home/_USER_ /_some_path_
    
###  阻止 Cinnamon 覆盖 xrandr/xinput 配置

_cinnamon-settings-daemon_ 提供了一些插件，它们可以管理显示、键盘和鼠标。这些插件会覆盖用户设置配置 (例如 [xinitrc](<../zh-cn/Xinit.html#xinitrc> "Xinitrc") 文件中的 _xrandr_ 命令)。要防止这种情况发生，有必要防止这些 _设置守护程序插件_ (settings daemon plugins) 启动。 

可以将有关的插件的 _.desktop_ 条目 (位于 `/etc/xdg/autostart/`) 复制到 `$HOME/.config/autostart` 处。之后在复制好的文件当中加一行 `Hidden=true`。 

**提示：** 用 `cinnamon-session --debug` 命令启动会话，以查看哪些插件被报告已被启动。

要保留显示、键盘和鼠标设置，请考虑禁用以下功能： 
    
    cinnamon-settings-daemon-a11y-keyboard.desktop
    cinnamon-settings-daemon-a11y-settings.desktop
    cinnamon-settings-daemon-keyboard.desktop
    cinnamon-settings-daemon-mouse.desktop
    cinnamon-settings-daemon-xrandr.desktop
    
##  故障排除

###  调试

可以使用`cinnamon-looking-glass` 工具 (杂项 - Cinnamon 调试器) 来检查多种 Cinnamon 环境中的各种事务： 

  * a list of currently-open windows - 当前打开的窗口的列表
  * a list of currently-loaded extensions (applets, desklets, etc.) - 当前加载的扩展 (小程序、桌板等）
  * logs - 日志

如果遇到桌面崩溃等事情 (通常是因为扩展不兼容或者有 Bug)， _logs (日志)_ 功能就显得尤为有用。 

###  出现 cinnamon-settings: No module named Image 错误

如果 _cinnamon-settings_ 不能启动，同时还伴有这样无法找到某个模块的错误信息（例如 Image module，图像模块)，可能是使用了已过期的已编译文件，这些文件指向了不再存在的文件位置。这种情况下，请移除 `/usr/lib/cinnamon-settings` 和其子文件夹下的所有 `*.pyc` 文件。请参阅[上游 Bug 报告](<https://github.com/linuxmint/Cinnamon/issues/2495>)。 

###  崩溃后从 tty 启动 Cinnamon

如果 Cinnamon 已经完全没反应了，可以在 tty (按 Alt+F2 进入) 中用如下命令重启它： 
    
     $ export DISPLAY=:0; cinnamon --replace &
    
###  视频画面撕裂

因为 [muffin](<https://archlinux.org/packages/?name=muffin>)包 基于 [mutter](<https://archlinux.org/packages/?name=mutter>)包, [GNOME](<../zh-cn/GNOME.html> "GNOME") 能用的视频撕裂修复方法应该对 Cinnamon 也有用。参见 [GNOME/Troubleshooting#Tear-free video with Intel HD Graphics](</wzh/index.php?title=GNOME/Troubleshooting&action=edit&redlink=1> "GNOME/Troubleshooting（页面不存在）") 获取更多信息。 

###  禁用 _网络管理_ 小程序

即使你不使用 [NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager") 并从从默认面板删除 _网络管理_ 小程序，Cinnamon 依然会载入 _nm-applet_ 并显示在系统托盘上。你**不能** 卸载 [NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager")，因为 [NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager") 被 [cinnamon](<https://archlinux.org/packages/?name=cinnamon>)包 和 [cinnamon-control-center](<https://archlinux.org/packages/?name=cinnamon-control-center>)包 依赖，但是可以很容易地将其禁用。要达成目的，首先应该把自启动文件从 `/etc/xdg/autostart/nm-applet.desktop` 复制到 `~/.config/autostart/nm-applet.desktop`，然后用喜欢的文本编辑器打开，并在尾部加上 `X-GNOME-Autostart-enabled=false`。 

此外，你也可以通过创建以下符号链接来禁用： 
    
    $ ln -s /bin/true /usr/local/bin/nm-applet
    
从系统托盘中将特定图标 (例如 _nm-applet_ 图标) 列入黑名单的功能已被[请求上游](<https://github.com/linuxmint/Cinnamon/issues/3318>)。 
