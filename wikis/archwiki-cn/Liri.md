**翻译状态：**

  * 本文（或部分内容）译自 [Liri](<https://wiki.archlinux.org/title/Liri> "arch:Liri")，最近一次同步于 2020-07-27，若英文版本有所[更改](<https://wiki.archlinux.org/title/Liri?diff=0&oldid=689328>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Liri_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Wayland](<../zh-cn/Wayland.html> "Wayland")
  * [桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")
  * [显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")
  * [窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")
  * [Qt](<../zh-cn/Qt.html> "Qt")

[Liri](<https://liri.io/>) 是具有现代设计和功能的桌面环境。 Liri 是 Hawaii，Papyros 和 [Liri Project](<https://github.com/liri-project>) 之间的合并。 

**警告：** Liri 目前处于 Alpha 阶段，可能存在问题。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")元软件包 [liri-git-meta](<https://aur.archlinux.org/packages/liri-git-meta/>)AUR 以获取所有 LiriOS 生态系统。 

或者，可以使用 [flatpak](<https://archlinux.org/packages/?name=flatpak>)包 安装它。 请参阅 [LiriOS 下载页面](<https://liri.io/download/#flatpak-panel>)中的 Flatpak 说明。 

##  启动桌面

###  使用图形登录管理器运行

支持 Wayland 的登录管理器（例如 [SDDM](<../zh-cn/SDDM.html> "SDDM") 和 [GDM](<../zh-cn/GDM.html> "GDM")）可以运行 Liri 会话。 

###  从 tty 运行

登录到 tty 并输入： 
    
    $ liri-session

会话管理器会自动检测硬件，并相应地运行合成器。 

但是，可以强制使用一种模式，例如，强制使用嵌套模式并在 Weston 内部运行： 
    
    $ liri-session -platform wayland

**注意：** 不要使用 `~/.xinitrc` 启动 Liri。[Xinit](<../zh-cn/Xinit.html> "Xinit") 通常用于启动 [Xorg](<../zh-cn/Xorg.html> "Xorg") ，但是 Liri 使用 Wayland，这是一种更新的图形协议。

###  使用 systemd 用户会话运行

首先，您需要按照 [systemd/用户](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "Systemd/用户")中的说明使用 systemd 用户会话设置 D-Bus。然后[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `liri.service` 用户单元 

每次您要[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") Liri 会话时： 
    
    $ systemctl --user isolate liri.target

目前已知 _logind_ 集成不适用于 systemd 用户会话，因此某些功能可能无法正常工作。systemd 用户会话是相当新的，开发人员正在使用它测试 Liri。 

##  另请参见

  * [官方网站](<https://liri.io/>)
  * [Liri 的 GitHub 页面](<https://github.com/lirios>)
