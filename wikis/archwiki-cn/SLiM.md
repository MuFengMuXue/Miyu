[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:SLiM](<../zh-cn/Talk:SLiM.html>)讨论)

[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** Last content update was in 2012（在 [Talk:SLiM#](<../zh-cn/Talk:SLiM.html>) 中讨论）

**警告：** SliM 显示管理器已经停止开发，[SliM 的官方网站](<http://slim.berlios.de/>)已经关闭，此外，SliM 与 [systemd](</wzh/index.php?title=Systemd_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "Systemd \(简体中文\)（页面不存在）") 也不是特别的兼容，请考虑换一个 [显示管理器](<../zh-cn/Display_manager.html> "Display manager")，或直接使用 startx。

[SLiM](<http://slim.berlios.de/>) 是**S** imple **L** og**i** n **M** anager（简单登录管理器）的缩写。SLiM是简单、轻量级和容易配置的，相对较易在低端和高端的系统中使用。对于那些希望寻找一个不依赖于[GNOME](<../zh-cn/GNOME.html> "GNOME")或者[KDE](<../zh-cn/KDE.html> "KDE")，可以在[Xfce](<../zh-cn/Xfce.html> "Xfce")、[Openbox](<../zh-cn/Openbox.html> "Openbox")、[Fluxbox](<../zh-cn/Fluxbox.html> "Fluxbox")等环境下使用的登录管理器的人来说，SLiM也是非常合适的。 

##  安装

[安装](<../zh-cn/Pacman.html> "Pacman")位于[官方软件仓库](<../zh-cn/Official_repositories.html> "Official repositories")的软件包 [slim](<https://archlinux.org/packages/?name=slim>)包。 

##  配置

###  启用SLiM

**注意：**[slim](<https://archlinux.org/packages/?name=slim>)包已经不提供 ConsoleKit 支持，而是使用 systemd-logind，所以系统需要通过 systemd 启动。

启用**slim** [服务](<../zh-cn/Systemd.html> "Daemons"). 启用 systemd 之后，已经无法使用 `inittab` 启动 slim。 

###  单用户环境

要将SLiM配置为加载某个特定的环境，只需编辑[~/.xinitrc](<../zh-cn/Xinit.html#xinitrc> "Xinitrc") 如下： 
    
    #!/bin/sh
    
    #
    # ~/.xinitrc
    #
    # Executed by startx (run your window manager from here)
    #
    
    exec [session-command]
    
将 _**[session-command]**_ 替换为适当的会话命令。例如： 
    
    exec awesome
    exec dwm
    exec startfluxbox
    exec fvwm2
    exec gnome-session
    exec openbox-session
    exec startkde
    exec startlxde
    exec startxfce4
    exec enlightenment_start
    
如果你的桌面环境不在上述列表中，请参考你的软件文档。 

Remember to make `~/.xinitrc` executable: 
    
    chmod +x ~/.xinitrc
    
**注意：**[slim](<https://archlinux.org/packages/?name=slim>)包 no longer has ConsoleKit support, but relies on systemd-logind, and the system being booted with systemd.

###  自动登录

想要使SLiM自动以特定用户身份登录（无须输入密码），需要修改 `/etc/slim.conf` 中的以下几行。 
    
    # default_user        simone
    
取消该行的注释，然后将“simone”改为需要自动登录的用户名。 
    
    # auto_login          no
    
取消该行的注释，然后将‘no’改为‘yes’。自动登录功能就被启用了。 

### Zsh

默认的登录命令不能正确初始化你的环境 [[source](<https://web.archive.org/web/20161211225408/http://wp.edsel.nu/2010/06/04/slim-simple-login-manager-on-freebsd/>)]。 将 login_cmd 一行改为： 
    
    #login_cmd           exec /bin/sh - ~/.xinitrc %session
    login_cmd           exec /bin/zsh -l ~/.xinitrc %session
    
###  多桌面环境

如果你希望可以加载多个不同的桌面环境，SLiM可以设置为登录到你指定的任何一个桌面环境。 

在你的/etc/X11/xinit/xinitrc文件中加入一段类似下面内容的case语句，并且编辑/etc/slim.conf中的sessions变量。 你可以在登录界面上按F1选择会话。请注意这个特性仍处于实验阶段。 
    
    # The following variable defines the session which is started if the user doesn't explicitly select a session
    
    DEFAULT_SESSION=twm
    
    case $1 in
    kde)
    	exec startkde
    	;;
    xfce4)
    	exec startxfce4
    	;;
    icewm)
    	icewmbg &
    	icewmtray &
    	exec icewm
    	;;
    wmaker)
    	exec wmaker
    	;;
    blackbox)
    	exec blackbox
    	;;
    *)
    	exec $DEFAULT_SESSION
    	;;
    esac

范例源码： <http://svn.berlios.de/svnroot/repos/slim/trunk/xinitrc.sample>

SLiM的文档： <http://slim.berlios.de/manual.php>

###  主题

安装[slim-themes](<https://archlinux.org/packages/?name=slim-themes>)包软件包： 
    
    # pacman -S slim-themes archlinux-themes-slim
    
软件包 [archlinux-themes-slim](<https://archlinux.org/packages/?name=archlinux-themes-slim>)包 包含了多个不同主题。可以在 `/usr/share/slim/themes` 中查看。在to see the themes available. Enter the theme name on the `current_theme` line in `/etc/slim.conf`: 

编辑`/etc/slim.conf`中的`current_theme`那行，将"default"改为你想要的主题名： 
    
    #current_theme       default
    current_theme       archlinux-simplyblack
    
要预览一个主题，可以运行 
    
    $ slim -p /usr/share/slim/themes/<theme name>
    
要退出，只需在登录行输入 "exit" 并回车。 

####  多屏幕设置

定制 `/usr/share/slim/themes/<your-theme>/slim.theme` 中的主题，修改百分比，就可以在多屏幕环境使用。假设宽为 450 高为 250 : 
    
    input_panel_x           50%
    input_panel_y           50%
    
修改为: 
    
    # 将 "archlinux-simplyblack" 面板放在 1440x900 屏幕的中间
    input_panel_x           495
    input_panel_y           325
    
    # 将 "archlinux-retro" 面板放在 1680x1050 屏幕的中间
    input_panel_x           615
    input_panel_y           400
    
如果主题有背景图片，可以设置背景样式('stretch', 'tile', 'center' 或 'color')。更多信息请访问 [slim 主题的标准文档](<http://slim.berlios.de/themes_howto.php>)。 

###  增强Slim功能

slim登录脚本主要靠你自己写，这对很多人来说比较困难，比如自动加载一些配置文件如~/.xprofile, ~/.xmodmap等。而且slim还无法记住上次登录使用的桌面环境。 

AUR里面有个包[slim-plus](<https://github.com/aur-archive/slim-plus>)可以解决这些问题。提供了一个Xsession脚本增强slim功能，加载配置文件，记住上次会话等。非常适合xfce等小型桌面环境。而且包含很多实用补丁。如果你想自己编写启动脚本，那里带的Xsession脚本可以做参考。 

安装完成后，如果以前使用的就是slim，那么需要编辑slim来使用/etc/X11/Xsession来加载会话，找到如下行： 
    
     login_cmd           exec /bin/bash -login ~/.xinitrc %session
    
替换为 
    
     login_cmd           exec /bin/bash -login /etc/X11/Xsession %session
     
只需要修改/etc/slim.conf的Sessions行，添加你需要的会话，slim启动后按F1选择就可以了。会话的名称可以在/usr/share/xsessions/下的*.desktop处得到。 

如果你安装的桌面环境没有提供.desktop文件，就需要自行编辑/etc/X11/Xsession文件尾部，不过脚本本身带有提供很多窗口管理器的启动脚本。 

Xsession脚本会自动加载常见配置文件。使用ck-launch-session加载桌面，解决一些挂载，无法关机等问题。并且使用~/.dmrc记录上次会话。由于slim功能有限，暂时无法选择语言。你自己可以编辑~/.dmrc来设置语言为中文。 
    
     Language=zh_CN.UTF-8
    
###  设置和Splashy一起工作时正常关机

如果你同时使用splashy和slim，有时你无法在gnome，xfce，lxde，等桌面环境中正常关机或者重启。 那么请检查你的/etc/slim.conf 和 /etc/splash.conf, 设置需要为 DEFAULT_TTY=7 或者 xserver_arguments vt07. 

###  Slim的登录信息

By default, Slim fails to log logins to utmp and wtmp which causes who, last, etc.. to misreport login information. 修正这些你需要编辑你的slim.conf: 
    
     sessionstart_cmd    /usr/bin/sessreg -a -l $DISPLAY %user
     sessionstop_cmd     /usr/bin/sessreg -d -l $DISPLAY %user
    
###  设置默认DPI

如果你设置DPI是通过在/etc/X11/Xinit/Xserverrc中添加参数-dpi 96，那么设置在slim中是不起作用的。你需要在slim.conf中这样设置： 
    
     xserver_arguments   -nolisten tcp vt07 
    
更改为： 
    
     xserver_arguments   -nolisten tcp vt07 -dpi 96
    
###  使用随机主题

在slim.conf中的current_theme行，添加多个主题，使用`,`分隔就可以使用随机主题了。 

##  更多的Slim参数

这个列表显示了所有的参数变量以及其默认值。 

**注意：** welcome_msg 允许2个变量**%host** 与 **%domain**  
sessionstart_cmd 读取 **%user** _(execd right before login_cmd)_ 并且它也会读取 sessionstop_cmd  
login_cmd allows **%session** and **%theme**

Option Name | Default Value   
---|---  
default_path |  `/bin:/usr/bin:/usr/local/bin`  
default_xserver |  `/usr/bin/X`  
xserver_arguments |  `vt07 -auth /var/run/slim.auth`  
numlock |   
daemon |  `yes`  
xauth_path |  `/usr/bin/xauth`  
login_cmd |  `exec /bin/bash -login ~/.xinitrc %session`  
halt_cmd |  `/sbin/shutdown -h now`  
reboot_cmd |  `/sbin/shutdown -r now`  
suspend_cmd |   
sessionstart_cmd |   
sessionstop_cmd |   
console_cmd |  `/usr/bin/xterm -C -fg white -bg black +sb -g %dx%d+%d+%d -fn %dx%d -T `  
screenshot_cmd |  `import -window root /slim.png`  
welcome_msg |  `Welcome to %host`  
session_msg |  `Session:`  
default_user |   
focus_password |  `no`  
auto_login |  `no`  
current_theme |  `default`  
lockfile |  `/var/run/slim.lock`  
logfile |  `/var/log/slim.log`  
authfile |  `/var/run/slim.auth`  
shutdown_msg |  `The system is halting...`  
reboot_msg |  `The system is rebooting...`  
sessions |  `wmaker,blackbox,icewm`  
sessiondir |   
hidecursor |  `false`  
input_panel_x |  `50%`  
input_panel_y |  `40%`  
input_name_x |  `200`  
input_name_y |  `154`  
input_pass_x |  `-1`  
input_pass_y |  `-1`  
input_font |  `Verdana:size=11`  
input_color |  `#000000`  
input_cursor_height |  `20`  
input_maxlength_name |  `20`  
input_maxlength_passwd |  `20`  
input_shadow_xoffset |  `0`  
input_shadow_yoffset |  `0`  
input_shadow_color |  `#FFFFFF`  
welcome_font |  `Verdana:size=14`  
welcome_color |  `#FFFFFF`  
welcome_x |  `-1`  
welcome_y |  `-1`  
welcome_shadow_xoffset |  `0`  
welcome_shadow_yoffset |  `0`  
welcome_shadow_color |  `#FFFFFF`  
intro_msg |   
intro_font |  `Verdana:size=14`  
intro_color |  `#FFFFFF`  
intro_x |  `-1`  
intro_y |  `-1`  
background_style |  `stretch`  
background_color |  `#CCCCCC`  
username_font |  `Verdana:size=12`  
username_color |  `#FFFFFF`  
username_x |  `-1`  
username_y |  `-1`  
username_msg |  `Please enter your username`  
username_shadow_xoffset |  `0`  
username_shadow_yoffset |  `0`  
username_shadow_color |  `#FFFFFF`  
password_x |  `-1`  
password_y |  `-1`  
password_msg |  `Please enter your password`  
msg_color |  `#FFFFFF`  
msg_font |  `Verdana:size=16:bold`  
msg_x |  `40`  
msg_y |  `40`  
msg_shadow_xoffset |  `0`  
msg_shadow_yoffset |  `0`  
msg_shadow_color |  `#FFFFFF`  
session_color |  `#FFFFFF`  
session_font |  `Verdana:size=16:bold`  
session_x |  `50%`  
session_y |  `90%`  
session_shadow_xoffset |  `0`  
session_shadow_yoffset |  `0`  
session_shadow_color |  `#FFFFFF`  
  
##  更多

  * [Display manager](</wzh/index.php?title=Display_manager_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "Display manager \(简体中文\)（页面不存在）")
  * [SLiM 官方网站](<http://slim.berlios.de/>)
