相关文章

  * [桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")
  * [GDM](<../zh-cn/GDM.html> "GDM")

**翻译状态：**

  * 本文（或部分内容）译自 [COSMIC](<https://wiki.archlinux.org/title/COSMIC> "arch:COSMIC")，最近一次同步于 2026-04-27，若英文版本有所[更改](<https://wiki.archlinux.org/title/COSMIC?diff=0&oldid=871994>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/COSMIC_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[COSMIC](<https://en.wikipedia.org/wiki/Pop!_OS> "wikipedia:Pop! OS") 是一个使用 [Rust](<../zh-cn/Rust.html> "Rust") 编程语言开发的[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")，使用**[iced](<https://iced.rs>)** 跨平台 Rust GUI库和 [Smithay](<https://github.com/Smithay/smithay>) 作为其合成器 Cosmic-comp 的构建模块。Cosmic-comp 相当于 smithay 自己的 anvil 合成器参考实现，就像 [Wayland](<../zh-cn/Wayland.html> "Wayland") 项目使用 Weston 作为合成器参考实现一样。它的第一个版本被称为 **Epoch** 。 

##  安装

安装 [cosmic-session](<https://archlinux.org/packages/?name=cosmic-session>)包 软件包或 [cosmic](<https://archlinux.org/groups/x86_64/cosmic/>)包组 组，开发版本可以安装 [cosmic-session-git](<https://aur.archlinux.org/packages/cosmic-session-git/>)AUR 获得，它依赖于所有的组件包 

当您通过源代码进行构建时， 请注意，依赖项 [cosmic-applets-git](<https://aur.archlinux.org/packages/cosmic-applets-git/>)AUR 需要至少 8GB RAM。限制连接到单任务是一个构建它的办法。如果你需要重复构建它，设置环境变量 `CARGO_TARGET_DIR` 有助于减少下载次数： 
    
    MOLD_JOBS=1 CARGO_TARGET_DIR=_/tmp/mytarget_
    
###  作为 cosmic-session 的依赖项被引入的组件

COSMIC 由一个合成器（compositor）、一个库（library）和一些小程序（applets）组成，这些组件可以分别作为独立的部分进行安装：[cosmic-comp](<https://archlinux.org/packages/?name=cosmic-comp>)包，[cosmic-applets](<https://archlinux.org/packages/?name=cosmic-applets>)包，[cosmic-app-library](<https://archlinux.org/packages/?name=cosmic-app-library>)包，[cosmic-bg](<https://archlinux.org/packages/?name=cosmic-bg>)包，[cosmic-icon-theme](<https://archlinux.org/packages/?name=cosmic-icon-theme>)包，[cosmic-launcher](<https://archlinux.org/packages/?name=cosmic-launcher>)包，[cosmic-notifications](<https://archlinux.org/packages/?name=cosmic-notifications>)包，用于在屏幕上叠加显示通知或提示信息的 [cosmic-osd](<https://archlinux.org/packages/?name=cosmic-osd>)包，提供底部或顶部的面板（panel）以及 dock 栏的 [cosmic-panel](<https://archlinux.org/packages/?name=cosmic-panel>)包，[cosmic-settings](<https://archlinux.org/packages/?name=cosmic-settings>)包，以及其他的一些包. 

###  独立组件

文本编辑器, [cosmic-text-editor](<https://archlinux.org/packages/?name=cosmic-text-editor>)包, 文件管理器 [cosmic-files](<https://archlinux.org/packages/?name=cosmic-files>)包, 终端模拟器, [cosmic-terminal](<https://archlinux.org/packages/?name=cosmic-terminal>)包, 媒体播放器 [cosmic-player](<https://archlinux.org/packages/?name=cosmic-player>)包, 壁纸选择器, [cosmic-wallpapers](<https://archlinux.org/packages/?name=cosmic-wallpapers>)包。 

###  COSMIC文件管理器中的网络共享

为了在COSMIC文件管理器中连接网络共享，需要安装这些相关的GVFS包： 

协议  | 软件包   
---|---  
AppleTalk  |  [gvfs](<https://archlinux.org/packages/?name=gvfs>)包  
File Transfer Protocol (FTP)  |  [gvfs](<https://archlinux.org/packages/?name=gvfs>)包  
Network File System (NFS)  |  [gvfs-nfs](<https://archlinux.org/packages/?name=gvfs-nfs>)包  
Server Message Block (SMB)  |  [gvfs-smb](<https://archlinux.org/packages/?name=gvfs-smb>)包  
SSH  |  [gvfs](<https://archlinux.org/packages/?name=gvfs>)包  
WebDAV  |  [gvfs-dnssd](<https://archlinux.org/packages/?name=gvfs-dnssd>)包  
  
COSMIC并不提供秘密存储或密钥功能，所以要记住密码，需要安装诸如gnome-keyring之类的密码存储元件。查看[GNOME/Keyring](<../zh-cn/GNOME/Keyring.html> "GNOME/Keyring")获得更多信息。 

##  启动

最简单的方法是通过已安装的[Display Manager](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")启动它，如[GNOME](<../zh-cn/GNOME.html> "GNOME")、[KDE Plasma](<../zh-cn/KDE_Plasma.html> "KDE Plasma")默认使用的GDM、SDDM 等，将会在登录界面发现一个额外的cosmic启动选项。 

如果要仅从tty启动，只需运行： 
    
    $ start-cosmic
    
###  使用 Cosmic 会话管理器

COSMIC包含了一个基于[greetd](<../zh-cn/Greetd.html> "Greetd")的显示会话管理器[cosmic-greeter](<https://archlinux.org/packages/?name=cosmic-greeter>)包。如果要使用这个dm，请激活`cosmic-greeter.service`服务。 

##  配置

The [panel](<https://github.com/pop-os/cosmic-panel>) can be used to configure besides using the settings applet, [examples of applets](<https://github.com/pop-os/cosmic-applets>) are provided. 

###  SSH_AUTH_SOCK 未设置

如果你在使用 Cosmic 登录管理器时看到了 `$SSH_AUTH_SOCK not set` 消息， [启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")由依赖项 [gcr-4](<https://archlinux.org/packages/?name=gcr-4>)包 提供的 `gcr-ssh-agent.socket` systemd [用户单元](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "用户单元")。 

###  夜光

因为 COSMIC DE 当前并不包含 `wlr-gamma-control-unstable-v1` 协议（参见 [pop-os/cosmic-comp#2059](<https://github.com/pop-os/cosmic-comp/issues/2059>)）， wlsunset 和 gammastep 之类的工具并不能在 COSMIC 会话中控制[背光](<../zh-cn/%E8%83%8C%E5%85%89.html> "背光")和色温。 

为了解决这个问题，你可以使用 [redshift](<https://archlinux.org/packages/?name=redshift>)包 或 [gammastep](<https://archlinux.org/packages/?name=gammastep>)包 之类的工具，在 COSMIC DE 混成器启动前通过 TTY 上的 libdrm 直接调节 DRM 伽马表。另一个可选项是用依赖于 systemd 服务的 [drm-colortemp](<https://github.com/jjo/drm-colortemp>) 或 [nebula-drm-git](<https://aur.archlinux.org/packages/nebula-drm-git/>)AUR 以自动化这一过程。 

##  参见

  * [COSMIC Welcome Page](<https://system76.com/cosmic/>)
  * [System76 博客](<https://blog.system76.com/>)
  * [Pop!_OS 欢迎界面](<https://pop.system76.com/>)
