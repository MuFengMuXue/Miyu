**翻译状态：**

  * 本文（或部分内容）译自 [Timeshift](<https://wiki.archlinux.org/title/Timeshift> "arch:Timeshift")，最近一次同步于 2024-7-26，若英文版本有所[更改](<https://wiki.archlinux.org/title/Timeshift?diff=0&oldid=812754>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Timeshift_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Btrfs](<../zh-cn/Btrfs.html> "Btrfs")
  * [系统维护](<../zh-cn/%E7%B3%BB%E7%BB%9F%E7%BB%B4%E6%8A%A4.html> "系统维护")
  * [同步和备份程序](<../zh-cn/%E5%90%8C%E6%AD%A5%E5%92%8C%E5%A4%87%E4%BB%BD%E7%A8%8B%E5%BA%8F.html> "同步和备份程序")

[Timeshift](<https://github.com/linuxmint/timeshift>) 最初是 [Tony George](<https://teejeetech.com/>) 创建的一个工具，现在是 [Xapp project](<https://github.com/linuxmint/xapp>) 项目的一部分。 

Timeshift 可帮助定期创建文件系统的增量快照，然后在以后恢复到这些快照，以撤销对系统的所有更改。 

它支持针对所有文件系统的 [rsync](<../zh-cn/Rsync.html> "Rsync") 快照，也可使用 [Btrfs](<../zh-cn/Btrfs.html> "Btrfs") 驱动器的内置快照功能，这需要驱动器[根目录](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E6%A0%B9%E5%88%86%E5%8C%BA> "分区")和 [home](<../zh-cn/%E5%88%86%E5%8C%BA.html#/home> "分区") 目录分别使用 `@` 和 `@home` 子卷布局配置。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [timeshift](<https://archlinux.org/packages/?name=timeshift>)包 软件包，并[安装/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Help:阅读")您选择的 cron 计划任务程序（请参阅 [cron#配置](<../zh-cn/Cron.html#%E9%85%8D%E7%BD%AE> "Cron")，cronie 已作为 Timeshift 的依赖而被安装）。这将保证 Timeshift 应用程序中的快照有计划地进行。 

另外，也可以安装 [timeshift-systemd-timer](<https://aur.archlinux.org/packages/timeshift-systemd-timer/>)AUR 来代替 cron 计划任务程序。 

##  btrfs 快照的 GRUB 条目

要在每次[生成 GRUB 配置](<../zh-cn/GRUB.html#%E7%94%9F%E6%88%90%E4%B8%BB%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6> "GRUB")时向 [GRUB](<../zh-cn/GRUB.html> "GRUB") 菜单添加快照，请安装 [grub-btrfs](<https://archlinux.org/packages/?name=grub-btrfs>)包 软件包。该软件包附带 `grub-btrfsd.service`，[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")后可在创建新快照时自动更新 GRUB 配置。 

要使 grub-btrfsd 与 Timeshift 一起工作，请运行以下命令编辑服务： 
    
    # systemctl edit --full grub-btrfsd
    
并将 `grub-btrfsd --syslog /.snapshots` 替换为 `grub-btrfsd --syslog -t`。 

##  问题解决

###  Timeshift 图形用户界面无法在 Wayland 上启动

[XWayland](<../zh-cn/Wayland.html#XWayland> "Wayland") 只允许启动 X 服务器的用户连接客户端（请参阅[以根用户权限启动图形用户界面](</wzh/index.php?title=%E4%BB%A5%E6%A0%B9%E7%94%A8%E6%88%B7%E8%BA%AB%E4%BB%BD%E8%BF%90%E8%A1%8C_GUI_%E5%BA%94%E7%94%A8&action=edit&redlink=1> "以根用户身份运行 GUI 应用（页面不存在）")（英语：[Running GUI applications as root](<https://wiki.archlinux.org/title/Running_GUI_applications_as_root> "en:Running GUI applications as root")））。 

由于 Timeshift 需要 root 权限，试图通过应用程序启动器或终端使用命令 `timeshift-launcher` 启动 Timeshift [GUI](<https://en.wikipedia.org/wiki/Graphical_user_interface> "wikipedia:Graphical user interface") 时，会出现包含 `xhost: command not found` 的错误。 

遇到此错误的用户还可能会看到他们的[身份验证组件](<../zh-cn/Polkit.html#%E8%BA%AB%E4%BB%BD%E9%AA%8C%E8%AF%81%E7%BB%84%E4%BB%B6> "Polkit")提示输入密码，但输入密码后却发现 Timeshift GUI 无法启动。[[1]](<https://arcolinuxforum.com/viewtopic.php?t=2453>)

这是因为命令 `timeshift-launcher` 需要 [xorg-xhost](<https://archlinux.org/packages/?name=xorg-xhost>)包 软件包，请[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")它。 

**警告：** 该命令可授予任何本地用户访问 X 屏幕的权限。建议不要在多用户系统上运行 `xhost`。详情请参见 [xhost](<../zh-cn/Xhost.html> "Xhost") 和[以根用户权限启动图形用户界面](</wzh/index.php?title=%E4%BB%A5%E6%A0%B9%E7%94%A8%E6%88%B7%E8%BA%AB%E4%BB%BD%E8%BF%90%E8%A1%8C_GUI_%E5%BA%94%E7%94%A8&action=edit&redlink=1> "以根用户身份运行 GUI 应用（页面不存在）")（英语：[Running GUI applications as root](<https://wiki.archlinux.org/title/Running_GUI_applications_as_root> "en:Running GUI applications as root")）。
