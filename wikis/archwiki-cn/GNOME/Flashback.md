相关文章

  * [桌面环境](<../../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")
  * [窗口管理器](<../../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")

**翻译状态：**

  * 本文（或部分内容）译自 [GNOME/Flashback](<https://wiki.archlinux.org/title/GNOME/Flashback> "arch:GNOME/Flashback")，最近一次同步于 2024-11-16，若英文版本有所[更改](<https://wiki.archlinux.org/title/GNOME/Flashback?diff=0&oldid=820780>)，则您可以帮助同步与[翻译](<../../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/GNOME_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)/Flashback_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[GNOME Flashback](<https://wiki.gnome.org/Projects/GnomeFlashback>)（之前称为“GNOME Fallback”）是一个为 GNOME 3 提供的外壳。桌面布局和底层技术与 GNOME 2 相似。它完全不使用 3D 加速，因此通常比启用了 llvmpipe 的 GNOME Shell 更加快速且对 CPU 的占用更低。 

##  安装

GNOME Flashback 可以从 [gnome-flashback](<https://archlinux.org/packages/?name=gnome-flashback>)包 [安装](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")。建议同时安装其可选依赖项，以获得更完整的桌面环境。 

您还可以安装以下提供额外 GNOME 面板小程序的包： 

  * **GNOME Applets** — 小型 GNOME 面板应用程序

     <https://wiki.gnome.org/Projects/GnomeApplets> || [gnome-applets](<https://archlinux.org/packages/?name=gnome-applets>)包

  * **Pomodoro Applet** — 用于计时番茄工作法的 GNOME 面板小程序

     <https://github.com/stump/pomodoro-applet> || [pomodoro-applet](<https://aur.archlinux.org/packages/pomodoro-applet/>)AUR

  * **Sensors Applet** — 显示硬件传感器读数（包括 CPU 温度、风扇速度和电压读数）的 GNOME Flashback 面板小程序

     <https://sensors-applet.sourceforge.net/> || [sensors-applet](<https://archlinux.org/packages/?name=sensors-applet>)包

建议安装 [gnome](<https://archlinux.org/groups/x86_64/gnome/>)包组，其中包含标准 GNOME 体验所需的应用程序。 

##  启动

###  图形化登录

在所选[显示管理器](<../../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")的菜单中选择“GNOME Flashback (Metacity)”。 

希望使用 [Compiz](<../../zh-cn/Compiz.html> "Compiz") 的用户应选择“GNOME Flashback (Compiz)”。 

###  手动启动

  * 对于 **GNOME Flashback (Metacity)** 会话，在 `~/.xinitrc` 文件中添加以下内容： 
        
        export XDG_CURRENT_DESKTOP=GNOME-Flashback:GNOME
        exec gnome-session --session=gnome-flashback-metacity

  * 对于 **GNOME Flashback (Compiz)** 会话，在 `~/.xinitrc` 文件中添加以下内容： 
        
        export XDG_CURRENT_DESKTOP=GNOME-Flashback:GNOME
        exec gnome-session --session=gnome-flashback-compiz

编辑 `.xinitrc` 后，可以使用 _startx_ 启动 GNOME Flashback。详情请参见 [xinitrc](<../../zh-cn/Xinit.html#xinitrc> "Xinitrc")。 

##  配置

GNOME Flashback 与 GNOME 共享大部分设置。更多详情请参见 [GNOME#配置](<../../zh-cn/GNOME.html#%E9%85%8D%E7%BD%AE> "GNOME")。 

###  自定义 GNOME 面板

  * 要配置面板，按住 `Alt` 键，然后在空白区域右键单击面板。
  * 要移动面板上的小程序，按住 `Alt` 键，并使用中键拖动它。

**注意：** 如果 `Alt+右键单击`组合无法使用，请尝试使用 `Super+Alt+右键单击`。

###  替代窗口管理器

您可以通过创建一个自定义的 GNOME 会话来使用替代的[窗口管理器](<../../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")，该会话应包含以下组件： 
    
    RequiredComponents=gnome-flashback-init;gnome-flashback;gnome-panel;**窗口管理器** ;gnome-settings-daemon;nautilus-classic;
    
其中**窗口管理器** 是您希望使用的窗口管理器。请参见 [GNOME/提示与技巧#自定义 GNOME 会话](<../../zh-cn/GNOME/%E6%8F%90%E7%A4%BA%E4%B8%8E%E6%8A%80%E5%B7%A7.html#%E8%87%AA%E5%AE%9A%E4%B9%89_GNOME_%E4%BC%9A%E8%AF%9D> "GNOME/提示与技巧")。 

另请参见[这篇文章](<https://web.archive.org/web/20190808234014/http://makandracards.com/makandra/1367-running-the-awesome-window-manager-within-gnome>)，了解如何在 GNOME 中运行 awesome 窗口管理器。 

##  提示与技巧

###  面板速度设置

隐藏/显示延迟

要调整启用自动隐藏时面板消失或重新出现的时间，请执行以下命令： 
    
    $ gsettings set org.gnome.gnome-panel.toplevel:/org/gnome/gnome-panel/layout/toplevels/_panel_ / hide-delay _time_
    $ gsettings set org.gnome.gnome-panel.toplevel:/org/gnome/gnome-panel/layout/toplevels/_panel_ / unhide-delay _time_
    
其中 _panel_ 为 _top-panel_ 或 _bottom-panel_ ， _time_ 为毫秒值，例如 300。 

动画速度

要设置面板动画的速度，请执行以下命令： 
    
    $ gsettings set org.gnome.gnome-panel.toplevel:/org/gnome/gnome-panel/layout/toplevels/_panel_ / animation-speed _value_
    
其中 _panel_ 为 _top-panel_ 或 _bottom-panel_ ， _value_ 为 `"'fast'"`, `"'medium'"` 或 `"'slow'"`。 

###  替换应用程序菜单图标

**注意：** 此更改将在更新您的图标主题包时被覆盖。

将 `/usr/share/icons/_icon-theme_ /16x16/places/start-here.png` 替换为您自己的图标（其中 `_icon-theme_` 为您的图标主题的名称）。 

完成更改后，重新启动 GNOME 面板： `gnome-panel --replace`。 

##  参见

  * [GnomeFlashback - GNOME Wiki](<https://wiki.gnome.org/Projects/GnomeFlashback>)
