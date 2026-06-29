**翻译状态：**

  * 本文（或部分内容）译自 [Xprofile](<https://wiki.archlinux.org/title/Xprofile> "arch:Xprofile")，最近一次同步于 2015-03-10，若英文版本有所[更改](<https://wiki.archlinux.org/title/Xprofile?diff=0&oldid=364903>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Xprofile_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [xinitrc](<../zh-cn/Xinit.html#xinitrc> "Xinitrc")

xprofile 文件，`~/.xprofile` 以及 `/etc/xprofile`, 允许您在刚打开 X 会话时运行命令 - 在[窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")运行之前。Xprofile 用于随会话自动运行程序，或从[显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")启动,尤其是那个会话没有自带自动启动程序功能时 - 比如一个独立的[窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")。 

xprofile 文件在语法和概念上类似 [xinitrc](<../zh-cn/Xinit.html#xinitrc> "Xinitrc"), `~/.xinitrc` 和 `/etc/X11/xinit/xinitrc.d/`. 

##  兼容性

xprofile 和 [xinitrc](<../zh-cn/Xinit.html#xinitrc> "Xinitrc") 文件在原生情况下会被以下显示管理器引用: 

  * [GDM](<../zh-cn/GDM.html> "GDM") \- `/etc/gdm/Xsession`
  * [LightDM](<../zh-cn/LightDM.html> "LightDM") \- `/etc/lightdm/Xsession`
  * [LXDM](<../zh-cn/LXDM.html> "LXDM") \- `/etc/lxdm/Xsession`
  * [SDDM](<../zh-cn/SDDM.html> "SDDM") \- `/usr/share/sddm/scripts/Xsession`

###  在用 init 开启会话之时引用 xprofile

使用以下程序启动会话时能够引用 xprofile 文件: 

  * `startx`
  * `xinit`
  * [XDM](<../zh-cn/XDM.html> "XDM")
  * 任何使用 `~/.xsession` 或者 `~/.xinitrc` 的[显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")

以上程序，都会直接或间接地执行，`~/.xinitrc` (如果不存在的话，通常是复制自 `/etc/skel/.xinitrc`) 或 `/etc/X11/xinit/xinitrc`. 这就是我们要从下列文件引用 xprofile 的原因. 
    
    ~/.xinitrc 和 /etc/X11/xinit/xinitrc 和 /etc/skel/.xinitrc
    
    #!/bin/sh
    
    # Make sure this is before the 'exec' command or it won't be sourced.
    [ -f /etc/xprofile ] && source /etc/xprofile
    [ -f ~/.xprofile ] && source ~/.xprofile
    
    ...
    
`xinitrc.d/*` 文件已经引用自默认 xinitrc 文件。 

##  配置

首先，如果文件不存在的话创建 `~/.xprofile`. 然后只需加入你想要随会话一同启动的程序的命令。见以下: 
    
    ~/.xprofile
    
    tint2 &
    nm-applet &
    