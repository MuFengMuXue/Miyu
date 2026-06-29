**翻译状态：**

  * 本文（或部分内容）译自 [Inkscape](<https://wiki.archlinux.org/title/Inkscape> "arch:Inkscape")，最近一次同步于 2020-04-04，若英文版本有所[更改](<https://wiki.archlinux.org/title/Inkscape?diff=0&oldid=603990>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Inkscape_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Inkscape](<https://inkscape.org/>) 是矢量图形创建和编辑程序。它是根据自由软件许可 GNU GPL 分发的。其既定目标是成为功能强大的图形工具，同时完全符合 XML、SVG 和 CSS 标准。 

##  安装

[inkscape](<https://archlinux.org/packages/?name=inkscape>)包 可以从[官方储存库](<../zh-cn/Official_repositories.html> "Official repositories")安装。开发版本可以从 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 安装 [inkscape-git](<https://aur.archlinux.org/packages/inkscape-git/>)AUR。 

##  疑难问题解决

###  KDE Plasma 环境无法显示工具提示

在 KDE 的系统设置下，找到 颜色 > 选项，然后禁用“将颜色应用于非 QT 应用程序”。如果更改之前正在运行 Inkscape，请重新启动 Inkscape。 

###  空格键和鼠标不起作用

默认情况下, 输入时 [libinput](<../zh-cn/Libinput.html> "Libinput") 禁用了 mousepad。你可以修改此设置，在 `/etc/X11/xorg.conf.d/30-touchpad.conf`的 `InputClass` 部分添加一行新内容: 
    
    Section "InputClass"
        ...
        ...
        Option "DisableWhileTyping" "0"
    EndSection
    
###  无法修改键盘快捷键

为了能够更改键盘快捷方式，请创建可以编辑的快捷方式文件的副本： 
    
    mkdir -p ~/.config/inkscape/keys
    cp /usr/share/inkscape/keys/default.xml ~/.config/inkscape/keys/
    
之后请重新启动 Inkscape。 

##  参见

  * [Multimedia in Arch Linux](<../zh-cn/Multimedia_in_Arch_Linux.html> "Multimedia in Arch Linux")
  * [Wikipedia 的 Inkscape](<https://en.wikipedia.org/wiki/Inkscape> "wikipedia:Inkscape")
