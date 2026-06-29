**翻译状态：**

  * 本文（或部分内容）译自 [Cutefish](<https://wiki.archlinux.org/title/Cutefish> "arch:Cutefish")，最近一次同步于 2024-6-5，若英文版本有所[更改](<https://wiki.archlinux.org/title/Cutefish?diff=0&oldid=810019>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Cutefish_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

Cutefish 是一个桌面环境，最初是为[CutefishOS](<https://cutefish-ubuntu.github.io/>) 项目编写的，它注重简洁、美观和实用。它使用[Qt5](<../zh-cn/Qt.html> "Qt")框架编写，提供简单、通用的外观和感觉。 

##  安装

可通过[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [cutefish](<https://archlinux.org/groups/x86_64/cutefish/>)包组 来安装Cutefish。 

##  启动

Cutefish 可以通过显示管理器启动，也可以从控制台手动启动。Cutefish 附带的显示管理器是[SDDM](<../zh-cn/SDDM.html> "SDDM")。 

###  图形化

[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `sddm.service`. 

###  手动

可以通过[xinitrc](<../zh-cn/Xinit.html#xinitrc> "Xinitrc")或直接在[startx](<../zh-cn/Xinit.html> "Startx")命令行中调用 `cutefish-session` 。 

##  配置

Cutefish 的配置主要可以在 Dock 上的设置程序中完成。 

###  键绑定

Cutefish 本身不支持按键绑定，但使用[sxhkd](<../zh-cn/Sxhkd.html> "Sxhkd")守护进程可以添加自定义按键绑定。 

它可以通过自定义会话启动： 
    
    /usr/bin/cutefish-session-sxhkd
    
    #!/bin/bash
    nohup sxhkd & 
    cutefish-session
    
    /usr/share/xsessions/cutefish-session-sxhkd.desktop
    
    [Desktop Entry]
    Type=Application
    Exec=cutefish-session-sxhkd
    TryExec=cutefish-session-sxhkd
    Name=Cutefish Desktop (with sxhkd)
    Keywords=session-sxhkd
    Comment=session-sxhkd

如果你是从archinstall安装的cutefish,修改这个之后有可能进不去，譬如sddm,可以不用修改
    
    $HOME/.config/sxhkd/sxhkdrc
    
    ctrl + alt + t
        cutefish-terminal
    
    super + d
        cutefish-launcher
    
###  终端颜色方案

Cutefish Terminal 本身没有内置的配色方案切换器。不过，我们可以编辑源代码 加入我们自己的配色方案。 

首先使用[ABS](<../zh-cn/Arch_%E6%9E%84%E5%BB%BA%E7%B3%BB%E7%BB%9F.html> "ABS")获取 [cutefish-terminal](<https://archlinux.org/packages/?name=cutefish-terminal>)包 的[PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD")。 

在构建步骤中或手动地[编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Textedit")主题，即 `Cutefish-Dark.colorcheme` 或 `Cutefish-Light.colorcheme` 中的 `_/path/to/the/sources/_ qmltermwidget/lib/color-schemes/`。 

为避免每次更新都重复这一步骤，最好创建一个补丁，以便更新后重复使用。 

##  参见

  * [CutefishOS](<https://cutefish-ubuntu.github.io/>)
  * [CutefishOS Github](<https://github.com/cutefishos/>)
