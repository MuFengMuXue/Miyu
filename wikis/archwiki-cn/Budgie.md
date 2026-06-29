**翻译状态：**

  * 本文（或部分内容）译自 [Budgie](<https://wiki.archlinux.org/title/Budgie> "arch:Budgie")，最近一次同步于 2026-04-05，若英文版本有所[更改](<https://wiki.archlinux.org/title/Budgie?diff=0&oldid=867405>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Budgie_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Desktop environment](<../zh-cn/Desktop_environment.html> "Desktop environment")
  * [Display manager](<../zh-cn/Display_manager.html> "Display manager")
  * [Window manager](<../zh-cn/Window_manager.html> "Window manager")
  * [GTK](<../zh-cn/GTK.html> "GTK")

Budgie 是一个桌面环境，以前是 Solus 里的一个项目，2022 年 1 月在新成立的[Buddies of Budgie](<https://blog.buddiesofbudgie.org/>) 组织下独立。它使用 [GTK](<../zh-cn/GTK.html> "GTK") 3 作为窗口部件，并使用 [C](<../zh-cn/C.html> "C") 和 Vala 编写。从 Budgie 10.10 开始，Budgie 作出了一个从 Xorg 改用 wayland 的巨大的跳跃，对 Xorg 的支持被立即放弃了。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [budgie](<https://archlinux.org/groups/x86_64/budgie/>)包组 软件包组以获取本桌面环境的所有组件，其中包括[budgie-desktop](<https://archlinux.org/packages/?name=budgie-desktop>)包 软件包及用于显示配置的 [budgie-desktop-services](<https://archlinux.org/packages/?name=budgie-desktop-services>)包 ，用于系统设置的 [budgie-control-center](<https://archlinux.org/packages/?name=budgie-control-center>)包 等运行时依赖。下列软件包是可选安装的，可以为桌面提供更多功能： 

[budgie-desktop-view](<https://archlinux.org/packages/?name=budgie-desktop-view>)包 ：桌面图标支持 

[network-manager-applet](<https://archlinux.org/packages/?name=network-manager-applet>)包 ：任务栏集成的网络管理 

[blueman](<https://archlinux.org/packages/?name=blueman>)包 ：蓝牙支持 

由 [Ubuntu Budgie](<https://ubuntubudgie.org/>) 开发的其他附属程序包含于 [budgie-extras](<https://archlinux.org/packages/?name=budgie-extras>)包 软件包中（请注意，此软件包还会修改现有功能，并可能导致问题）。 

###  配置用户目录

Budgie 根据 [XDG 用户目录](<../zh-cn/XDG_%E7%94%A8%E6%88%B7%E7%9B%AE%E5%BD%95.html> "XDG 用户目录")指令创建众所周知的用户目录，如桌面、下载等。登出再登录就可以让 Budgie 菜单检测到配置的变化。 

###  文件管理器

Budgie 没有自带文件管理器，也没有默认安装其他文件管理器。 [GNOME文件](<../zh-cn/GNOME/%E6%96%87%E4%BB%B6.html> "GNOME/文件") (Nautilus) 工作得很好，[这些](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E5%B7%A5%E5%85%B7.html> "应用程序列表/工具")其他的文件管理器也可用。 

##  启动

从[显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")桌面菜单中选择 _Budgie Desktop_ 会话，或者修改 [xinitrc](<../zh-cn/Xinit.html#xinitrc> "Xinitrc") 使其包括 Budgie 桌面： 
    
    ~/.xinitrc
    
    export XDG_CURRENT_DESKTOP=Budgie:GNOME
    exec budgie-desktop
    
##  使用方法

Budgie 的侧栏被称作 "Raven"，可以在上面查看通知消息，设置系统和应用音量，查看日历，以及查看正在播放的视频或音乐等。通知部分可以通过按下 `Super+N` 键或点击面板中的通知小程序来访问它。小程序部分可以通过 `Super+A` 快速打开。侧栏也可以通过单击面板中的 "Raven Trigger" 小程序打开，并出现在之前选中的窗格中。 

##  主题

Budgie 使用 [GTK](<../zh-cn/GTK.html> "GTK") 3 作为用户界面，因此被许多 GTK 主题支持。Budgie 还提供了一个内置主题，该主题仅适用于其自身的元素，如面板和 Raven，可以在 Budgie Desktop Setting 中切换。图标主题和光标主题也可以在 Budgie Desktop Setting 中设置。 

##  配置

Budgie 桌面的配置可以通过内置的 Budgie Desktop Setting 来完成，改变系统设置则通过 [budgie-control-center](<https://archlinux.org/packages/?name=budgie-control-center>)包 来完成。 

###  改变按钮布局

使用 [dconf](<https://archlinux.org/packages/?name=dconf>)包、[dconf-editor](<https://archlinux.org/packages/?name=dconf-editor>)包 或者 gsettings 可改变窗口按钮布局。 

比如： 
    
    gsettings set com.solus-project.budgie-wm button-layout 'close,minimize,maximize:appmenu'
    gsettings set com.solus-project.budgie-helper.workarounds fix-button-layout 'close,minimize,maximize:menu'
    
###  使用不同的窗口管理器

Budgie 不支持使用不同的窗口管理器。 

##  参见

  * [Wikipedia:Budgie (desktop environment)](<https://en.wikipedia.org/wiki/Budgie_\(desktop_environment\)> "wikipedia:Budgie \(desktop environment\)")
  * [Budgie 桌面官方网站 (英文)](<https://blog.buddiesofbudgie.org/>)
  * [Budgie git 官方开发 git 仓库](<https://github.com/BuddiesOfBudgie/budgie-desktop>)
