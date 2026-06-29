相关文章

  * [文件管理器功能](<../zh-cn/%E6%96%87%E4%BB%B6%E7%AE%A1%E7%90%86%E5%99%A8%E5%8A%9F%E8%83%BD.html> "文件管理器功能")
  * [PCManFM](<../zh-cn/PCManFM.html> "PCManFM")
  * [窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")

**翻译状态：**

  * 本文（或部分内容）译自 [SpaceFM](<https://wiki.archlinux.org/title/SpaceFM> "arch:SpaceFM")，最近一次同步于 2024-8-7，若英文版本有所[更改](<https://wiki.archlinux.org/title/SpaceFM?diff=0&oldid=814056>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/SpaceFM_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

**注意：** 自 2018-03-04 以来，该项目未出现任何 [commits](<https://github.com/IgnorantGuru/spacefm>)：已放弃开发。一个 [fork](<https://github.com/thermitegod/spacefm>) 正在积极维护中。

[SpaceFM](<https://ignorantguru.github.io/spacefm/>) （PCManFM 的一个分叉）是一个轻量级、高度可配置、独立于桌面的多面板标签式文件和桌面管理器。它具有内置虚拟文件系统、基于 [udev](<../zh-cn/Udev.html> "Udev") 的设备管理器、可定制的菜单系统和 [Bash](<../zh-cn/Bash.html> "Bash") 集成。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [spacefm](<https://aur.archlinux.org/packages/spacefm/>)AUR 软件包。 

如果需要 GTK 2 版本，也可以使用 [spacefm-gtk2](<https://aur.archlinux.org/packages/spacefm-gtk2/>)AUR 软件包。 

##  用法

参见 [User's Manual](<https://ignorantguru.github.io/spacefm/spacefm-manual-en.html>)。 

###  文件搜索

SpaceFM 提供与 [catfish](<https://archlinux.org/packages/?name=catfish>)包 类似的内置文件搜索功能： 
    
    $ spacefm -f
    
###  桌面管理

SpaceFM 包括一个轻量级桌面管理器。[[1]](<https://ignorantguru.github.io/spacefm/spacefm-manual-en.html#invocation-desktopmanager>)。它可以替换桌面菜单、添加桌面图标和设置壁纸。 

要恢复原本窗口管理器菜单，请打开 `Desktop preferences`
    
    $ spacefm --desktop-pref
    
并在 `Desktop` 选项卡中启用 `Right click shows WM menu` 选项。考虑将上述命令添加到按键绑定和/或原本桌面菜单中，以方便访问。 

要将 SpaceFM 作为[守护进程](<../zh-cn/Systemd.html> "守护进程")运行而不管理桌面[[2]](<https://ignorantguru.github.io/spacefm/spacefm-manual-en.html#invocation-daemonmode>)，请使用： 
    
    $ spacefm -d
    
SpaceFM 如何作为守护进程自动启动或为独立的[窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")管理桌面取决于窗口管理器本身。如果窗口管理器不提供自动启动文件，请编辑 [xinitrc](<../zh-cn/Xinit.html#xinitrc> "Xinitrc") 或 [xprofile](<../zh-cn/Xprofile.html> "Xprofile")。 

###  挂载远程主机

SpaceFM 支持通过 [udevil](<../zh-cn/Udisks.html#Mount_helpers> "Udisks") 来挂载远程主机。要添加远程主机，请在 URL 栏中添加访问 URL。这时会弹出一个终端窗口，显示挂载过程，这对错误跟踪很有用。 

[udevil help](<https://ignorantguru.github.io/udevil/udevil--help.html>) 中提供了所支持远程主机的概述。例如，挂载远程 FTP 服务器： 
    
    ftp://user:pass@sys.domain/share
    
##  提示与技巧

###  在应用程序中打开压缩包，而不是解压缩

默认情况下，SpaceFM 会在双击压缩包时将其解压缩。如果你想用默认的存档管理器（如 [file-roller](<https://archlinux.org/packages/?name=file-roller>)包 ）打开它，那么选择一个存档，右键单击右键菜单，然后： Open / Archive default / Open With App 

###  仅在文件/文件夹上显示自定义右键菜单命令

如果您需要自定义的右键菜单命令仅在选择文件或文件夹时显示，请在 `Menu Item Properties -> Context` 中添加以下规则： 
    
    MIME Type equals true
    File Is Dir equals true
    File Is Text equals true
    
##  问题解决

###  栏的大小不可调整

只有在首次启动 SpaceFM（GTK 2 版本）时才会出现这种情况。[[3]](<https://github.com/IgnorantGuru/spacefm/issues/382>)

### Segmentation faults

如果 SpaceFM 在崩溃时出现以下错误 
    
    localhost kernel: [245086.687050] spacefm[30684]: segfault at 3e8000003e8 ip 00007fc95c586866 sp 00007fffb1dc9cc0 error 4 in libgtk-x11-2.0.so.0.2400.24[7fc95c446000+435000]
    
SpaceFM 使用许多不同的图形用户界面元素，因此很容易受到主题故障的影响（尤其是在 GTK 3 中）。试试不同的主题，如 Raleigh（默认主题）。在 GTK 2 中，仅 SpaceFM 可以这样做： 
    
    GTK2_RC_FILES=/usr/share/themes/Raleigh/gtk-2.0/gtkrc spacefm
    
关于详细信息，请参见 [[4]](<https://ignorantguru.github.io/spacefm/spacefm-manual-en.html#invocation-gtkthemes>)。 
