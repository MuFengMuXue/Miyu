**翻译状态：**

  * 本文（或部分内容）译自 [LXDM](<https://wiki.archlinux.org/title/LXDM> "arch:LXDM")，最近一次同步于 2024-10-22，若英文版本有所[更改](<https://wiki.archlinux.org/title/LXDM?diff=0&oldid=806163>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/LXDM_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** Some sections are not translated, the original page has evolved a little since the last translation, the TranslationStatus is erroneous since a section [removed in 2013](<../Special:%E5%B7%AE%E5%BC%82/284730.html> "Special:差异/284730") is still present here!（在 [Talk:LXDM#](<../zh-cn/Talk:LXDM.html>) 中讨论）

相关文章

  * [LXDE](<../zh-cn/LXDE.html> "LXDE")
  * [显示管理器](<../zh-cn/Display_manager.html> "Display manager")

LXDM 是轻量级的 [LXDE](<../zh-cn/LXDE.html> "LXDE") [桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")使用的[显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")。 

LXDM 不支持 XDMCP 协议，要使用 XDMCP，请使用 [LightDM](<../zh-cn/LightDM.html> "LightDM"). 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%98%E6%96%B9%E8%BD%AF%E4%BB%B6%E5%8C%85> "Help:阅读") [GTK+](<../zh-cn/GTK.html> "GTK+") 2版本的[lxdm](<https://archlinux.org/packages/?name=lxdm>)包 软件包 或 [GTK+](<../zh-cn/GTK.html> "GTK+") 3版本的[lxdm-gtk3](<https://archlinux.org/packages/?name=lxdm-gtk3>)包软件包 。 

[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") [systemd](<../zh-cn/Systemd.html> "Systemd") 服务 `lxdm.service`。 

##  配置

**警告：****lxdm.conf** 中必须包含语言选择控制，请设置 **lang=1** 否则 LXDM 会不停循环启动，无法载入会话。

LXDM 的配置文件都位于 `/etc/lxdm`。主配置文件是 `lxdm.conf`，注释非常详细。`Xsession` 是系统 X 会话配置文件，一般不需要修改。目录中的其他文件都是 shell脚本，在 LXDM 发生相应事件时运行： 

  1. `LoginReady`: 在 LXDM 准备显示登录窗口时以 root 权限运行。
  2. `PreLogin`: 用户登录前以 root 权限运行。
  3. `PostLogin`: 用户登录后以登录的用户运行。
  4. `PostLogout`: 用户注销后以用户权限运行。
  5. `PreReboot`: 通过 LXDM 重启时以 root 运行。
  6. `PreShutdown`: 通过 LXDM关机时以 root 运行。

###  默认会话

默认会话可以全局配置，也可以在用户级别配置。用户设置优先于全局设置。 

####  全局设置

要修改 LXDM 的默认会话或桌面环境，请编辑 `/etc/lxdm/lxdm.conf` 把会话行改为如下： 
    
    session=/usr/bin/startlxde

例如 [Xfce](<../zh-cn/Xfce.html> "Xfce"): 
    
    session=/usr/bin/startxfce4

例如 [Openbox](<../zh-cn/Openbox.html> "Openbox"): 
    
    session=/usr/bin/openbox-session

例如 [GNOME](<../zh-cn/GNOME.html> "GNOME"): 
    
    session=/usr/bin/gnome-session

例如 [LXQt](<../zh-cn/LXQt.html> "LXQt"): 
    
    session=/usr/bin/xfwm4

在使用的主题无会话选择框或者自动登录有问题时，这个设置很有用。 

####  各个用户设置

要定义独立用户的会话，请编辑 `~/.dmrc` 并定义会话。 

例如：用户1要用 xfce4，用户2要用cinnamon,用户3要用GNOME: 

用户1的设置： 
    
    [Desktop]
    Session=xfce
    
用户2的设置： 
    
    [Desktop]
    Session=cinnamon
    
用户3的设置： 
    
    [Desktop]
    Session=gnome
    
可用如下命令显示已安装的会话列表 
    
    $ ls /usr/share/xsessions/
    
###  自动登录

如果要免密自动登录一个用户，找到 `/etc/lxdm/lxdm.conf` 中的: 
    
    #autologin=dgod
    
取消前面的注释，并将dgod改为想要免密登录用户名。 

###  上次的登录选项

以前使用的 LXDM 选项可以在以下位置找到： 
    
    /var/lib/lxdm/lxdm.conf
    
    [base]
    last_session=/usr/share/xsessions/LXDE.desktop
    last_lang=sv_SE.UTF-8
    last_langs=sv_SE.UTF-8 fa_IR.UTF-8 en_US.UTF-8

**注意：** 卸载 LXDM 时，此文件不会自动删除。如果要删除 LXDM 选项的所有痕迹，则必须手动删除它。

##  提示和技巧

###  添加表情图标

一个96x96像素的图像（jpg或png格式）可以选择性地在每个用户上替代默认图标进行显示。只需将目标图像复制或使用符号链接到 `$HOME/.face`。[gnome-control-center](<https://archlinux.org/packages/?name=gnome-control-center>)包 包提供了一些适用于lxdm屏幕的默认图标。 在安装该软件包后，在 `/usr/share/pixmaps/faces` 目录下查找。 

**注意：**

  * 用户不需要保留 [gnome-control-center](<https://archlinux.org/packages/?name=gnome-control-center>)包 包来使用这些图像。只需安装它，将它们复制到其他地方，然后卸载它即可。

  * 用户的目录应该对其他人具有r-x权限，而.face文件对其他人应该有r--权限。但显然，这会带来安全和访问方面的影响，因为现在任何人都可以浏览你的主目录。

  * 一个名为 `lxdm-config` 的图形化工具随lxdm一起提供，可以用于在主目录中放置 `.face` 文件，以及其他配置文件。

###  同时登录和切换用户

LXDM 可以让多个用户同时登录到不同 ttys，下面的命令可以登录另一个用户，而不需要注销当前用户会话： 
    
    $ lxdm -c USER_SWITCH
    
**注意：** 用USER_SWITCH登录新用户时，使用的是tty7的下一个tty。使用USER_SWITCH 命令登录用户1后，用户2正常登录，用户2会在tty7,，用户1将会位于 tty1。

###  主题

LXDM 主题位于 `/usr/share/lxdm/themes`. 

LXDM 仅提供了一个主题 Industrial. 要显示主题背景文件 `wave.svg`，请安装软件包 [librsvg](<https://archlinux.org/packages/?name=librsvg>)包. 

[lxdm-themes](<https://aur.archlinux.org/packages/lxdm-themes/>)AUR 提供了 6 个额外的主题：Archlinux, ArchlinuxFull, ArchlinuxTop, Arch-Dark, Arch-Stripes 和 IndustrialArch. [lxdm-git](<https://aur.archlinux.org/packages/lxdm-git/>)AUR 也提供了 ArchStripes 和 ArchDark(名字改了一下以避免冲突). 

主题文件通过 `/etc/lxdm/lxdm.conf` 配置: 
    
    ## the theme of greeter
    theme=theme_name
    
要让 LXDM 使用 GTK 主题(位于 `/usr/share/themes`)，在配置文件中设置： 
    
    ## GTK theme
    gtk_theme=gtk_theme_name
    
###  高级会话配置

用户登录后，LXDM 会按下面顺序引用全部文件： 

  1. `/etc/profile`
  2. `~/.profile`
  3. `/etc/xprofile`
  4. `~/.xprofile`

这些文件可以设置会话的环境变量，启动必须的服务例如 ssh-agent。详情请参考 [Xprofile](<../zh-cn/Xprofile.html> "Xprofile")。 

LXDM **不会** 引用 `~/.xinitrc`，所以如果需要从使用这些文件的显示管理器迁移到 LXDM，需要将设置移动到其它文件，例如 `~/.xprofile`. LXDM 也不会引用 `~/.bash_profile`。 

如果还想使用 `~/.xinitrc`，可以在 `/etc/lxdm/PostLogin` 中加入： 
    
    source ~/.xinitrc
    
LXDM 也会使用 .[Xresource](<../zh-cn/X_%E8%B5%84%E6%BA%90.html> "X 资源"), .[Xkbmap](</wzh/index.php?title=Xkbmap&action=edit&redlink=1> "Xkbmap（页面不存在）"), 和 .[Xmodmap](<../zh-cn/Xmodmap.html> "Xmodmap")。LXDM 系统配置和用户配置的详细状况可以参考 `/etc/lxdm/Xsession`[[1]](<https://github.com/archlinux/svntogit-community/blob/packages/lxdm/trunk/Xsession>)。 

##  问题处理

###  白闪

当使用默认的LXDM主题 `theme=Industrial` 和一个暗色背景图片（例如 `bg=/usr/share/backgrounds/img.png`）时，LXDM启动之前可能会出现短暂的明亮闪光。 这是由于所选 [GTK+](<../zh-cn/GTK.html> "GTK+") 主题的 `bg_color:` 属性引起的。 为了避免这种情况，请将 `gtk_theme=Adwaita` 更改为 `gtk_theme=Adwaita-dark` 或其他暗色主题。 

###  注销问题

如果您在使用 lxdm 时无法注销（例如卡住、显示冻结等），请尝试取消 `/etc/lxdm/lxdm.conf` 中的 reset=1 选项的注释，以便在每次注销时刷新 xserver 
