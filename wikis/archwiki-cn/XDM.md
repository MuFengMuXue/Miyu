**翻译状态：**

  * 本文（或部分内容）译自 [XDM](<https://wiki.archlinux.org/title/XDM> "arch:XDM")，最近一次同步于 2018-05-09，若英文版本有所[更改](<https://wiki.archlinux.org/title/XDM?diff=0&oldid=684591>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/XDM_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Display Manager](<../zh-cn/Display_Manager.html> "Display Manager")

摘自 [XDM 手册页](<https://www.xfree86.org/current/xdm.1.html>): 

    _Xdm 能为本地和远程服务器提供一系列图形显示功能。xdm的设计满足图形显示的基本要求并遵循开放组织标准(XDMCPX Display Manager Control Protocol)，即X显示管理协议。Xdm提供的功能与init, getty等以文本登录为主的程序相似:提供登录会话，获取用户名和密码，并将授权给予登录用户并提供工作会话。_

XDM 提供了一个简单而又直观的图形登录界面。 

##  安装

安装软件包 [xorg-xdm](<https://archlinux.org/packages/?name=xorg-xdm>)包 然后[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") `xdm.service` 服务。 

要使用 Arch Linux XDM 主题，可以安装软件包 [xdm-archlinux](<https://archlinux.org/packages/?name=xdm-archlinux>)包，然后**不启用** `xdm.service`，而是启用 `xdm-archlinux.service`。 

##  配置

###  定义会话

和 [GDM]] 或 [LightDM](<../zh-cn/LightDM.html> "LightDM") 等大部分[显示管理器](<../zh-cn/Display_manager.html> "Display manager")不同，XDM 不会从 `/usr/share/xsessions` 目录中的 .desktop 文件读取会话。XDM 没有会话菜单。XDM 会执行账号主目录下的 `.xsession` 文件。 

例如要启动 xface，`~/.xsession` 应该是： 
    
    startxfce4
    
请确保 `.xsession` 文件可执行： 
    
    $ chmod 700 ~/.xsession
    
###  主题

详情请参考 xdm 手册，默认的配置文件位于 `/etc/X11/xdm/Xresources`,[xdm-archlinux](<https://archlinux.org/packages/?name=xdm-archlinux>)包 主题的配置文件位于 `/etc/X11/xdm/archlinux/Xresources`。 

####  壁纸

可以使用 [qiv](<https://archlinux.org/packages/?name=qiv>)包 设置 XDM 的壁纸: 

  * 安装 [qiv](<https://archlinux.org/packages/?name=qiv>)包
  * 创建一个文件夹用于存放图片。 (例如 `/root/backgrounds` 或者 `/usr/local/share/backgrounds`)
  * 把图片放进文件夹

  * 编辑 `/etc/X11/xdm/Xsetup_0`. 将 `xconsole` 修改为：

     /usr/bin/qiv -zr /root/backgrounds/*
    
####  字体

编辑 `/etc/X11/xdm/Xresources`. 添加/替换 下面字段: 
    
     xlogin**greetFont:  -adobe-helvetica-bold-o-normal--20-** -**-** -**-** -iso8859-1
     xlogin**font:       -adobe-helvetica-medium-r-normal--14-** -**-** -**-** -iso8859-1
     xlogin**promptFont: -adobe-helvetica-bold-r-normal--14-** -**-** -**-** -iso8859-1
     xlogin**failFont:   -adobe-helvetica-bold-r-normal--14-** -**-** -**-** -iso8859-1
    
####  登录对话框位置
    
     xlogin*frameWidth: 1
     xlogin*innerFramesWidth: 1
     xlogin*logoPadding: 0
     xlogin*geometry:    300x175-0-0
    
####  删除徽标

注释掉以下字段: 
    
     #xlogin*logoFileName: /usr/X11R6/lib/X11/xdm/pixmaps/xorg.xpm
     #xlogin*logoFileName: /usr/X11R6/lib/X11/xdm/pixmaps/xorg-bw.xpm
    
###  多 X 会话和登录

启用 [XDMCP](</wzh/index.php?title=XDMCP&action=edit&redlink=1> "XDMCP（页面不存在）") 后，可以在同一个机器上运行多个 X 会话： 
    
    # X -query ip_xdmcp_server :2
    
这将启动第二个会话，在窗口中需要 [xorg-server-xephyr](<https://archlinux.org/packages/?name=xorg-server-xephyr>)包
    
    # Xephyr -query this_machine_ip :2
    
###  无密码登录

要启用 XDM 无密码登录，将下面内容加入 `/etc/X11/xdm/Xresources`: 
    
    xlogin*allowNullPasswd: true
    