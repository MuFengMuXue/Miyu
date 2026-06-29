**翻译状态：**

  * 本文（或部分内容）译自 [Foot](<https://wiki.archlinux.org/title/Foot> "arch:Foot")，最近一次同步于 2025-05-07，若英文版本有所[更改](<https://wiki.archlinux.org/title/Foot?diff=0&oldid=833420>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Foot_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[foot](<https://codeberg.org/dnkl/foot>) 是一个快速、轻量和简约的 [Wayland](<../zh-cn/Wayland.html> "Wayland") 终端模拟器。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [foot](<https://archlinux.org/packages/?name=foot>)包 软件包或 [foot-git](<https://aur.archlinux.org/packages/foot-git/>)AUR 开发版本。 

此外还可以安装 [foot-terminfo](<https://archlinux.org/packages/?name=foot-terminfo>)包 以获取增强的 terminfo。 

##  配置

_foot_ 加载 `$XDG_CONFIG_HOME/foot/foot.ini` 中的配置文件（默认为 `$HOME/.config/foot/foot.ini`）。配置文件模板位于 `/etc/xdg/foot/foot.ini`，复制模板到 `$XDG_CONFIG_HOME/foot/foot.ini` 并取消要修改设置的注释。重启 _foot_ 以应用新设置。 

手册页面 [foot.ini(5)](<https://man.archlinux.org/man/foot.ini.5>) 提供了关于如何配置 _foot_ 的详细信息。 

###  颜色

您可以通过修改 `[colors]` 节自定义颜色。 

主题位于 `/usr/share/foot/themes`。要应用主题，请在 `[main]`} 下添加 `include` 关键字。 
    
    $HOME/.config/foot/foot.ini
    
    [main]
    include=/usr/share/foot/themes/_主题名称_

###  服务器（守护进程）模式

正常运行时， _foot_ 会为每个窗口启动一个新的 _foot_ 进程。 

_foot_ 也可以在服务器模式下运行。在该模式下，一个进程会托管多个窗口。所有 Wayland 通信、VT 解析和渲染都在服务器进程中完成。 

**注意：**

  * 在服务器模式下运行 _foot_ 的优势包括减少内存占用和启动时间。
  * 缺点是会影响性能；所有窗口的输入和输出都在同一线程中复用（但每个窗口都有自己的渲染线程）。这意味着，如果一个窗口忙于输出等工作，其他窗口就会受到影响。此外，如果服务器进程崩溃，所有窗口都将消失。

运行 _footclient_ 以打开新窗口，其会一直运行到终端窗口关闭，然后以客户端进程（通常是 shell）的退出值退出。 

[启用/启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用/启动")[用户单元](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "用户单元") `foot-server.service` 或相应的 `foot-server.socket` 以激活套接字，以便在登录时自动启动脚本服务器。 

##  提示与技巧

### GNOME

####  显示边框

目前，[GNOME](<../zh-cn/GNOME.html> "GNOME") 不支持 Wayland 上的服务器端装饰。在 GNOME 上运行的 _foot_ 将显示一个普通的平面窗口。您可以配置 _foot_ 显示边框，以便更容易区分不同的 _foot_ 窗口。 
    
    $HOME/.config/foot/foot.ini
    
    [csd]
    border-width=2
    border-color=ff404040

### terminfo

标准的 [foot](<https://archlinux.org/packages/?name=foot>)包 使用 ncurses 的 [terminfo(5)](<https://man.archlinux.org/man/terminfo.5>)。安装 [foot-terminfo](<https://archlinux.org/packages/?name=foot-terminfo>)包 以使用 _foot_ 的上游 terminfo，其包含一些功能改进， 主要针对 [tmux](<../zh-cn/Tmux.html> "Tmux") 优化，如应用程序同步更新和 24 位颜色支持。 

请参阅 [foot 的 wiki 条目](<https://codeberg.org/dnkl/foot/wiki/Home.md#foot-s-terminfo-vs-ncurses-terminfo>)以获取更多信息。 

##  疑难解答

###  登录后 foot-server 未启动

`foot-server.service` 单元和 `foot-server.socket` 单元需要 `graphical-session.target`，但是 Sway 不会自动设定这些，请遵循 [Sway#使用 systemd 管理仅用于 Sway 的守护程序](<../zh-cn/Sway.html#%E4%BD%BF%E7%94%A8_systemd_%E7%AE%A1%E7%90%86%E4%BB%85%E7%94%A8%E4%BA%8E_Sway_%E7%9A%84%E5%AE%88%E6%8A%A4%E7%A8%8B%E5%BA%8F> "Sway")创建一个 `sway-session.target` 单元并在 Sway 启动时将其启动。 
