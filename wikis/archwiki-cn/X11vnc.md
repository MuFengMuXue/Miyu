[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:X11vnc](<../zh-cn/Talk:X11vnc.html>)讨论)

相关文章

  * [TigerVNC](<../zh-cn/TigerVNC.html> "TigerVNC")

[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** Still out of sync after the update of 2021-05-26（在 [Talk:X11vnc#](<../zh-cn/Talk:X11vnc.html>) 中讨论）

[x11vnc](<https://en.wikipedia.org/wiki/x11vnc> "wikipedia:x11vnc")是一个VNC服务器，它允许人们使用任何VNC viewer远程查看并控制真实的X显示器（即与物理显示器、键盘和鼠标相对应的显示器）。虽然它已不再由原作者Karl Runge开发，但LibVNC和GitHub社区已经接管了开发工作。 

_x11vnc_ 不会为远程控制创建一个额外的显示（或X桌面）。相反，它实时显示现有的X11显示器，与Xvnc不同，它是[TigerVNC](<../zh-cn/TigerVNC.html> "TigerVNC")的一部分，是[官方软件仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方仓库")中的替代VNC服务器。 

还要注意的是，x11vnc并没有附带一个客户端。所有VNC viewer都可以完成这项工作，而不必使用其所有功能。TigerVNC的 _vncviewer_ 是推荐的客户端。 

##  设置 x11vnc

###  安装

[安装](<../zh-cn/Pacman_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Pacman \(简体中文\)")位于[官方软件仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方仓库")的 [x11vnc](<https://archlinux.org/packages/?name=x11vnc>)包 软件包。 

###  运行

首先，通过 _startx_ 或[显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")来启动X 服务器。你可能需要将X设置为无头运行。 

然后，运行以下命令，所有可用的选项在[x11vnc(1)](<https://man.archlinux.org/man/x11vnc.1>)中都有解释。 
    
    $ x11vnc -display :0
    
另一个选项是将x11vnc命令放在一个脚本中，在登录时调用，例如： 
    
    x11vnc -wait 50 -noxdamage -passwd PASSWORD -display :0 -forever -o /var/log/x11vnc.log -bg
    
####  设置 X authority

您可以为VNC服务器设置X authority。 这可以通过`-auth`参数和相应的文件来实现，这取决于你的X 服务器是如何启动的。一般来说，分配X authority需要以root身份运行"'x11vnc'"。 

####  启动 X
    
    $ x11vnc -display :0 -auth ~/.Xauthority
    
如果失败，则你可能需要作为root来运行： 
    
    # x11vnc -display :0 -autho /home/USER/.Xauthority
    
其中 _USER_ 是运行X 服务器的用户的用户名。 

#### GDM

作为root，运行 
    
    # x11vnc -display :0 -auth /var/lib/gdm/:0.Xauth
    
###  设置密码

运行: 
    
    $ x11vnc -usepw
    
将会使用在`~/.vnc/passwd`找到的密码，或是在`~/.vnc/passwdfile`第一行找到的密码，如果这些文件都找不到，它会提示用户输入密码，密码将会保存在`~/.vnc/passwd`中。 

VNC viewer应该在连接时提示输入密码。 

###  访问

在其他机器运行VNC客户端，然后输入运行了x11vnc服务器的IP地址。点击连接，然后你需要设置。 

##  SSH端口转发

为了安全地使用`x11vnc`，您首先需要安装并且配置好[SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH")。 

在启动`x11vnc`的时候，指定命令行选项“`-localhost`”，这将导致VNC服务只能绑定到本地网络界面。此时从外界直接连入的连接将被拒绝。 

当您需要从另一台电脑上访问这个VNC服务的时候，首先用[SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH")登录到运行VNC的主机，将VNC服务监听的端口转发到您的本地主机。以下的例子中假设运行VNC的主机名为"foo"，VNC监听5900端口上： 
    
    ssh foo -L 5900:localhost:5900
    
SSH连接建立以后，打开VNC客户端程序，但是不要让它连接到foo的5900端口，而是连接到本机（localhost）的5900端口。 

这样，您就可以通过加密渠道安全地访问远程X服务了。 

##  参见

  * [original author site](<http://www.karlrunge.com/x11vnc/>)
  * <https://github.com/LibVNC/x11vnc>
  * [Wikipedia:x11vnc](<https://en.wikipedia.org/wiki/x11vnc> "wikipedia:x11vnc")
