**翻译状态：**

  * 本文（或部分内容）译自 [Yakuake](<https://wiki.archlinux.org/title/Yakuake> "arch:Yakuake")，最近一次同步于 2022/09/12，若英文版本有所[更改](<https://wiki.archlinux.org/title/Yakuake?diff=0&oldid=745755>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Yakuake_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [KDE](<../zh-cn/KDE.html> "KDE")

[Yakuake](<https://kde.org/applications/system/org.kde.yakuake>) 是一个适用于 [KDE](<../zh-cn/KDE.html> "KDE") 的下拉式终端，类似于 [GNOME](<../zh-cn/GNOME.html> "GNOME") 的 [Guake](</wzh/index.php?title=Guake&action=edit&redlink=1> "Guake（页面不存在）")、[Tilda](</wzh/index.php?title=Tilda&action=edit&redlink=1> "Tilda（页面不存在）")或 Quake 中使用的终端。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [yakuake](<https://archlinux.org/packages/?name=yakuake>)包 软件包。 

##  使用

安装后，您可以在终端启动 yakuake： 
    
    $ yakuake
    
Yakuake 启动后，您可以点击“配置 Yakuake” 通过点击 _菜单_ 按钮（界面右下中间）并选择 _配置键盘快捷键_ 以更改收放终端的热键，默认是 `F12`。 

##  配置

###  Plasma 上的透明/模糊背景

尽管大多数配置选项可以在 Yakuake GUI 更改，一些选项只能借助修改配置文件更改，例如 [Plasma](<../zh-cn/KDE.html> "Plasma") 下的模糊背景选项。 

**注意：** 在 Yakuake 的 Konsole 配置文件中启用 _Blur background_ 选项会为 Yakuake 的窗口启用模糊，但将显示警告如 `Konsole 在桌面特效启用前启动。您需要重启 Konsole 来显示透明背景。` 见 [有关此警告的上游漏洞报告](<https://bugs.kde.org/show_bug.cgi?id=395520>)。此警告有一定误导性，因为 Yakuake 使用不支持模糊/透明的 KonsolePart，但 Yakuake 本身可以对其窗口启用此效果。

要为 Yakuake 启用模糊背景，编辑以下文件： 
    
    ~/.config/yakuakerc
    
    [Appearance]
    Blur=true
    Translucency=true

然后重启 Yakuake 以应用更改。 

##  Yakuake 脚本

如 [Guake](</wzh/index.php?title=Guake&action=edit&redlink=1> "Guake（页面不存在）") 一样，Yakuake 允许运行时发送 [D-Bus](<../zh-cn/D-Bus.html> "D-Bus") 信息以控制它。因此，该特性可被用于在用户定义的会话启动 Yakuake。您可以创建标签页，为其指定名称，并在任何打开的标签页中要求运行任何特定命令，或者只是显示/隐藏 Yakuake 窗口：在终端中手动操作或通过为其创建自定义脚本。 

下面是该脚本的一个示例。这包括打开标签页，重命名标签页，拆分 shell 以及运行命令。 
    
    #!/bin/bash
    # 基于用户首选项启动 Yakuake。这些信息基于 <https://forums.gentoo.org/viewtopic-t-873915-start-0.html>
    # 前一个网站中添加会话部分已损坏，故采用此：<https://koston.pl/blog/sublime-text-3-cheatsheet-modules-web-develpment/>
    
    # 在 Yakuake 不接受 fcitx 输入时需要此行
    /usr/bin/yakuake --im /usr/bin/fcitx --inputstyle onthespot &
    
    # 在发送 dbus 命令前让 Yakuake 等待 2 秒
    sleep 2      
                                                     
    # 在 'user' 标签页启动 htop 然后向右拆分 'user' 终端，并在新终端运行 iotop                                                 
    TERMINAL_ID_0=$(qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.terminalIdsForSessionId 0)
    qdbus org.kde.yakuake /yakuake/tabs setTabTitle 0 "user"
    qdbus org.kde.yakuake /yakuake/sessions runCommandInTerminal 0 "htop"
    qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.splitTerminalLeftRight "$TERMINAL_ID_0"
    qdbus org.kde.yakuake /yakuake/sessions runCommandInTerminal 1 "iotop
    
    # 上下拆分并启动根会话（提示输入密码）                                                                          
    SESSION_ID_1=$(qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.addSession)
    TERMINAL_ID_1=$(qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.terminalIdsForSessionId "$SESSION_ID_1")
    qdbus org.kde.yakuake /yakuake/tabs setTabTitle 1 "root"
    qdbus org.kde.yakuake /yakuake/sessions runCommandInTerminal 2 "su"
    qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.splitTerminalTopBottom "$TERMINAL_ID_1"
    qdbus org.kde.yakuake /yakuake/sessions runCommandInTerminal 3 "su" 
    
    # 在其自己的标签页启动 irssi                                                                              
    qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.addSession
    qdbus org.kde.yakuake /yakuake/tabs setTabTitle 2 "irssi"
    qdbus org.kde.yakuake /yakuake/sessions runCommandInTerminal 4 "ssh home -t 'tmux attach -t irssi; bash -l'" 
    
    # 在其自己的标签页启动 ssh shell，并左右拆分                                                                             
    SESSION_ID_2=$(qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.addSession)
    TERMINAL_ID_2=$(qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.terminalIdsForSessionId "$SESSION_ID_2")
    qdbus org.kde.yakuake /yakuake/tabs setTabTitle 3 "work server"
    qdbus org.kde.yakuake /yakuake/sessions runCommandInTerminal 5 "ssh work"
    qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.splitTerminalLeftRight "$TERMINAL_ID_2"
    qdbus org.kde.yakuake /yakuake/sessions runCommandInTerminal 6 "ssh work"
    
###  用 dbus-send 替代 qdbus

您可用更常见的 _dbus-send_ 替换与 [Qt](<../zh-cn/Qt.html> "Qt") 捆绑的 _qdbus_ 。例如，要显示/隐藏 Yakuake： 
    
    $ dbus-send --type=method_call --dest=org.kde.yakuake /yakuake/window org.kde.yakuake.toggleWindowState
    
##  疑难解答

###  真彩程序不正确显示

见 [Konsole#真彩程序无法正确显示](<../zh-cn/Konsole.html#%E7%9C%9F%E5%BD%A9%E7%A8%8B%E5%BA%8F%E6%97%A0%E6%B3%95%E6%AD%A3%E7%A1%AE%E6%98%BE%E7%A4%BA> "Konsole")。 

##  参见

  * [Yakuake 脚本于 coderwall.com](<https://coderwall.com/p/kq9ghg/yakuake-scripting>)
