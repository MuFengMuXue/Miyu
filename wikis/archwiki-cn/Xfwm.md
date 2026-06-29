**翻译状态：**

  * 本文（或部分内容）译自 [Xfwm](<https://wiki.archlinux.org/title/Xfwm> "arch:Xfwm")，最近一次同步于 2022-08-13，若英文版本有所[更改](<https://wiki.archlinux.org/title/Xfwm?diff=0&oldid=741241>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Xfwm_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")
  * [窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")
  * [Xfce](<../zh-cn/Xfce.html> "Xfce")
  * [Xorg](<../zh-cn/Xorg.html> "Xorg")

**Xfwm** 是用于 [Xfce](<../zh-cn/Xfce.html> "Xfce") 桌面环境的窗口管理器。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [xfwm4](<https://archlinux.org/packages/?name=xfwm4>)包 软件包。 

##  启动

使用 [xinit](<../zh-cn/Xinit.html> "Xinit") 启动 `xfwm4`。 

##  配置

Xfwm 的大多数窗口表现和快捷键设置可以通过 `xfwm4-settings` 修改,高级设置和窗口合成可以通过 `xfwm4-tweaks-settings` 修改,工作区数量和名字可以通过 `xfwm4-workspace-settings` 修改。 

###  合成管理器

**注意：**

  * 这个窗口合成器可能导致应用中出现画面撕裂,请见 [#画面撕裂](<#%E7%94%BB%E9%9D%A2%E6%92%95%E8%A3%82>)。
  * 窗口合成器自从 Xfwm 4.12 开始默认启用。

要启用或禁用 Xfwm 窗口合成器和修改它的设置,前往 _窗口管理器微调_ : 
    
    $ xfwm4-tweaks-settings
    
或者,使用带有 `--compositor` 参数的 _xfconf_ 来启用它。例如: 
    
    ~/.xinitrc
    
    exec xfwm4 --compositor=on
    
    $ xfconf-query -c xfwm4 -p /general/use_compositing -s _true_
    
###  窗口卷起

双击标题栏或在窗口菜单中点击 _卷起窗口_ 会让窗口内容消失,只留下标题栏。要使用 `xfconf` 禁用这个功能,运行命令: 
    
    $ xfconf-query -c xfwm4 -p /general/mousewheel_rollup -s false
    
###  窗口平铺

Xfwm 可以在将窗口移动到屏幕边缘时会自动将其平铺。它通过调整窗口大小以适合屏幕的上半部分来实现自动平铺。要使用 `xfconf` 启用或禁用这个操作,运行命令: 
    
    $ xfconf-query -c xfwm4 -p /general/tile_on_move -s false
    $ xfconf-query -c xfwm4 -p /general/tile_on_move -s true
    
或者,勾选(取消勾选) _Window Manager Tweaks > Accessibility > Automatically tile windows when moving toward the screen edge_。 

###  Xfce 设置管理器提供的额外设置

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [官方软件仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方软件仓库")的 [xfce4-settings](<https://archlinux.org/packages/?name=xfce4-settings>)包。 

**注意：** 安装 [xfce4-settings](<https://archlinux.org/packages/?name=xfce4-settings>)包 可能会修改一些任务的默认应用。请见 [xdg-open](<../zh-cn/Xdg-utils.html#xdg-open> "Xdg-open") 以设置你想要的默认应用。

###  附加主题

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [官方软件仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方软件仓库")的 [xfwm4-themes](<https://archlinux.org/packages/?name=xfwm4-themes>)包。 

安装的主题会在 `xfwm4-settings` 窗口中显示出来。 

##  提示与技巧

###  在窗口最大化时隐藏标题栏

前往 `Accessibility` 并勾选 `Hide title of windows when maximized`。 

**注意：** 如果你想把当前最大化窗口的标题栏放在面板上,安装 [xfce4-windowck-plugin](<https://aur.archlinux.org/packages/xfce4-windowck-plugin/>)AUR。

##  故障排除

###  在浏览器中下载的项目没有图标

这可以通过[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")[官方软件仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方软件仓库")的 [xfce4-settings](<https://archlinux.org/packages/?name=xfce4-settings>)包 来修复。 

###  工作区数量发生意外更改

请注意 _Xfwm_ 给添加和移除工作区分配了快捷键。默认情况分别是 `Alt+Delete` 和 `Alt+Insert`。 

如果在登录时工作区的数量会重置,请在启动 Xfwm **之后** 修改工作区数量。可以通过 `sleep` 命令来保证启动顺序。[[1]](<https://bugs.launchpad.net/ubuntu/+source/xfwm4/+bug/787934>)
    
    ~/.xinitrc
    
    (sleep 3 && xfconf-query -v -c xfwm4 -p /general/workspace_count -s _number_) &
    exec xfwm4
    
或者,通过 [xfce4-session](<https://archlinux.org/packages/?name=xfce4-session>)包: 
    
    ~/.config/autostart/workspace.desktop
    
    [Desktop Entry]
    Exec=sh -c "sleep 3 && xfconf-query -v -c xfwm4 -p /general/workspace_count -s _number_ "

另见: [注销会改变工作区](<https://forum.xfce.org/viewtopic.php?id=6056>)

###  画面撕裂

如果有画面撕裂现象,你可以试着修改 Xfwm 的 `--vblank` 模式选项(_glx_ ,_xpresent_ 或 _off_),先使用以下命令尝试一下[[2]](<https://forum.xfce.org/viewtopic.php?id=13092>): 
    
    $ xfwm4 --replace --vblank=glx &
    
要想保存这个设置: 
    
    $ xfconf-query -c xfwm4 -p /general/vblank_mode -s glx
    
如果你使用 Intel 显卡并且如 [Intel graphics#Tearing](<../zh-cn/Intel_graphics.html#Tearing> "Intel graphics") 中所述在 Xorg 中启用了 _TearFree_ 选项,请禁用 _Synchronize drawing to the vertical blank_ 选项。 

如果这不能修复撕裂现象,请考虑关闭 Xfwm 的窗口合成器并使用替代的[合成管理器](<../zh-cn/Xorg.html#%E5%90%88%E6%88%90> "Xorg")。 

###  Dock 窗口上方的水平线

Xfwm 可能会错误地渲染一些 Dock 窗口的阴影(例如[Plank](</wzh/index.php?title=Plank&action=edit&redlink=1> "Plank（页面不存在）"))。这可能会导致屏幕上有一条水平线。一个解决方案是禁用 _设置 > 窗口管理器微调 > 窗口合成_中的 _显示 Dock 窗口下的阴影_ 。 

##  另见

  * [Xfwm - 介绍](<https://docs.xfce.org/xfce/xfwm4/introduction>)
