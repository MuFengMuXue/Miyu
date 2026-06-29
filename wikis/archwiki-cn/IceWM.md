**翻译状态：**

  * 本文（或部分内容）译自 [IceWM](<https://wiki.archlinux.org/title/IceWM> "arch:IceWM")，最近一次同步于 2022-02-05，若英文版本有所[更改](<https://wiki.archlinux.org/title/IceWM?diff=0&oldid=713972>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/IceWM_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Window manager](<../zh-cn/Window_manager.html> "Window manager")

根据[维基百科](<https://en.wikipedia.org/wiki/Icewm> "wikipedia:Icewm")上的内容: 

    IceWM is a window manager for the X Window System graphical infrastructure, written by Marko Maček. It was coded from scratch in C++ and is released under the terms of the GNU Lesser General Public License. It is relatively lightweight in terms of memory and CPU usage, and comes with themes that allow it to imitate the UI of Windows 95, OS/2, Motif, and other graphical user interfaces.

翻译： 

    IceWM是一个由Marko Maček写的X窗口系统图形窗口管理器的基础设施。它是用 C++ 编写的，在 GNU Lesser General Public License 协议下发布。在内存和 CPU 使用方面，它相对轻量，且带有模仿 Windows 95、OS/2、Motif 和其他图形化用户界面的主题。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [icewm](<https://archlinux.org/packages/?name=icewm>)包 包。 

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [icewm-git](<https://aur.archlinux.org/packages/icewm-git/>)AUR 包以获得[开发版本](<https://github.com/bbidulock/icewm>)。 

##  开始

使用 [xinit](<../zh-cn/Xinit.html> "Xinit") 来运行 `icewm`， 或者使用 `icewm-session` 来运行 icewmbg 和 icewmtray。 

**注意：**`icewm-session` 需要 `startup` 脚本来执行。

##  配置

尽管 IceWM 的配置在最初是基于文本的，但是仍有一些图形界面的工具可以使用，特别是 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 中的 [icewm-utils](<https://aur.archlinux.org/packages/icewm-utils/>)AUR。然而这些工具都相对较旧，而且大多数用户都喜欢对配置文件进行简单的编辑。配置文件可以在整个系统的范围内（在 `/etc/icewm/` 之中）或单个用户的范围内（在 `~/.icewm/` 之中）进行更改。 

如果要更改您的 icewm 配置， 只需要将默认配置文件从 `/usr/share/icewm/` 复制到 `~/.icewm/`，比如这样： 
    
     $ cp -r /usr/share/icewm/ ~/.icewm/
    
  * `preferences` 是 IceWM 的核心配置文件。
  * `menu` 控制 IceWM 的主题菜单包含什么。
  * `keys` 允许用户使用定制自己的快捷方式。
  * `toolbar` 控制任务栏上的一排启动图标。
  * `winoptions` 个别的各应用程序的行为。
  * `theme` 主题的路径/名称。
  * `startup` 在启动时执行的脚本和命令。
  * `shutdown` 在关机时执行的。

###  自动启动

`startup` 脚本**不是** [icewm](<https://archlinux.org/packages/?name=icewm>)包 提供的 ，所以您需要自己[创建](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "创建")它，并使之[可执行](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "Executable")。 

为您希望在 IceWM 会话开始时启动的程序添加命令。 

**注意：** 安装系统托盘小程序的启动命令前必须有 `sleep 1 &&`，否侧 IceWM 将会创造一个丑陋的黑色窗口；这种情况下，使用任务栏上的 xkill。

下面是一个 IceWM 启动脚本的例子，它使用 IceWM 会话启动 [network-manager-applet](<https://archlinux.org/packages/?name=network-manager-applet>)包 和 [XScreenSaver](<../zh-cn/XScreenSaver.html> "XScreenSaver")。 
    
    ~/.icewm/startup
    
    #!/bin/sh
    
    # start network manager
        sleep 1 &&
        nm-applet &
    
    # enable bluetooth applet
        sleep 1 &&
        blueman-applet &!
    
    # enable screensaver
        xscreensaver -nosplash &
    
    # start redshift
        redshift &
    
    # allow notifications
        /usr/lib/notification-daemon-1.0/notification-daemon &
    
    # enable lockscreen
        exec xautolock -detectsleep -time 15 -locker "i3lock -n -i /home/user/lockscreen.png" -killtime 20 -killer "systemctl suspend" #lock after inactivity and then sleep
    
###  生成菜单项

  * 官方软件仓库中的 [menumaker](<https://archlinux.org/packages/?name=menumaker>)包 是一个 Python 脚本，它根据系统中安装的内容自动填充您的应用程序菜单。尽管这可能会导致许多无用的的应用程序充满菜单，但它仍然可能比手动编辑菜单配置文件更好。当运行 MenuMaker 时，使用 -f 覆盖现有的菜单文件：

    $ mmaker -f icewm
    
如果您要避免使用终端的应用程序（比如 _alsamixer_ ），您可以使用 mmaker 命令运行以下开关： `--no-legacy` 和 `--no-debian`。就像这样： 
    
    $ mmaker -f --no-legacy --no-debian icewm
    
  * 或者，您可以使用 [Xdg-menu](<../zh-cn/Xdg-menu.html> "Xdg-menu") 生成一个菜单。详见 [Xdg-menu#IceWM](<../zh-cn/Xdg-menu.html#IceWM> "Xdg-menu") 部分。

###  主题

[icewm](<https://archlinux.org/packages/?name=icewm>)包 包中包含了一小些主题。这些可以通过 [icewm-extra-themes](<https://aur.archlinux.org/packages/icewm-extra-themes/>)AUR 包中提供的主题进行补充。更多的主题可以在 [box-look.org](<https://www.box-look.org/browse/cat/142/ord/latest/>) 中下载。 

###  桌面图标

像 [PCManFM](<../zh-cn/PCManFM.html> "PCManFM") 或者 [rox](<https://archlinux.org/packages/?name=rox>)包 这样的文件管理器可以管理壁纸并添加桌面图标。或者，您也可以安装 [Idesk](<../zh-cn/Idesk.html> "Idesk")，这是一个可以帮您把图标添加到桌面的小程序。 

##  提示和技巧

###  混成

IceWM 是一个不含混成的窗口管理器。如果您需要在 IceWM 使用混成效果，您可以单独选择一个混成管理器，比如 [Xcompmgr](<../zh-cn/Xcompmgr.html> "Xcompmgr") 或者 [Picom](<../zh-cn/Picom.html> "Picom")。 

##  问题解决

###  没有开始菜单图标（Intel 显卡）

如果您的 IceWM 运行在[Intel 显卡](<../zh-cn/Intel_graphics.html> "Intel graphics")上，您可能会发现您的任务栏中的开始菜单没有图标。这是 [xf86-video-intel](<https://archlinux.org/packages/?name=xf86-video-intel>)包 驱动程序最近的变化造成的，“最近的变化”意味着新但是并不稳定，SNA加速后端是默认开启的。 要修复开始菜单问题（及其他可能的图形问题）您需要切换回就得 UXA 后端。请参考以下文章：[Intel graphics#AccelMethod](<../zh-cn/Intel_graphics.html#AccelMethod> "Intel graphics")。 

###  当 PCManFM 管理桌面时无法注销

如果您使用 [PCManFM](<../zh-cn/PCManFM.html> "PCManFM")管理桌面，您可能会发现 IceWM 的注销按钮不能正常工作。您可以自行定义注销命令并作为一种解决方案。这允许您在 PCManFM 管理桌面时注销。为此，您可以打开 `~/.icewm/preferences`，取消以下这行的注释： `# LogoutCommand=""` 然后输入一个可以用来注销的命令。比如： `LogoutCommand="pkill -u username"` 其中的 username 是您的用户名。 

###  注销菜单中没有关机和重启的选项

  * 注销命令已经定义：

如果之前定义了注销命令，则关机和重启命令将被忽略。如果您想要在注销菜单中的关机和重启选项，那么您一定不能定义注销命令。 

  * 注销命令未被定义：

如果您已经定义了关机和重启命令（比如用 `systemctl poweroff` 和 `systemctl reboot`），并且您还没有定义注销命令，可是您仍然发现注销菜单中没有关机和重启选项。请升级到 `icewm 1.3.8-2`。在 [FS#37884](<https://bugs.archlinux.org/task/37884>) 中获取更多信息。 

##  参见

  * [IceWM 的官方网站](<https://ice-wm.org/>)
  * [IceWM - The Cool Window Manager](<https://www.osnews.com/story.php/7774/IceWM--The-Cool-Window-Manager/>) \- OSNews 上的详细介绍
  * [IceWM - A desktop for Windows emigrants](<https://web.archive.org/web/20100613011705/http://polishlinux.org/apps/window-managers/icewm-a-desktop-for-windows-emmigrants/>) \- polishlinux.org 上的概述和教程
