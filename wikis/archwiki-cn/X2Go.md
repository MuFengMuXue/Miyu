**翻译状态：**

  * 本文（或部分内容）译自 [X2Go](<https://wiki.archlinux.org/title/X2Go> "arch:X2Go")，最近一次同步于 2019-08-02，若英文版本有所[更改](<https://wiki.archlinux.org/title/X2Go?diff=0&oldid=571538>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/X2Go_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[X2Go](<https://wiki.x2go.org>) 使你可以通过网络访问一台计算机的图形化桌面。访问时的网络传输使用了 [Secure Shell](<../zh-cn/Secure_Shell.html> "Secure Shell") 协议，因而传输是加密的。 

**注意：** X2Go 并不能兼容所有桌面环境。你可以先查阅 [X2Go 桌面环境兼容性](<https://wiki.x2go.org/doku.php/doc:de-compat>)，尤其是当你要映射当前的桌面环境时。

##  安装

[官方仓库](<../zh-cn/Official_repositories.html> "Official repositories")中提供了下列两个软件包供[安装](<../zh-cn/Pacman.html> "Pacman")： 

  * [x2goserver](<https://aur.archlinux.org/packages/x2goserver/>)AUR \- X2Go 服务器
  * [x2goclient](<https://aur.archlinux.org/packages/x2goclient/>)AUR \- 基于 Qt5 的 X2Go 客户端

##  服务器端配置

###  配置 Secure Shell 守护进程

X2Go 使用 [Secure Shell](<../zh-cn/Secure_Shell.html> "Secure Shell") 才能工作，所以你首先需要配置 sshd 守护进程使其允许 X11 转发并启动它。参阅 [OpenSSH - X11 转发](<../zh-cn/OpenSSH.html#X11_forwarding> "OpenSSH")和 [OpenSSH - 管理 sshd 守护进程](<../zh-cn/OpenSSH.html#Daemon_management> "OpenSSH")。 

###  加载 fuse 内核模块

为使服务器端能够访问客户端计算机上的文件，你需要加载 `fuse` [内核模块](<../zh-cn/Kernel_modules.html> "Kernel modules")。 

你可以查看 `lsmod | grep fuse` 是否返回匹配项，若无，则需要加载 `fuse` [内核模块](<../zh-cn/Kernel_module.html> "Kernel module")。 

###  设置 SQLite 数据库

在服务器端执行下列命令以初始化 x2go 服务器运行所需的 SQLite 数据库： 
    
    # x2godbadmin --createdb
    
### Control published applications

X2Go can publish the installed applications in a menu to the client. This is controlled by the files in `/etc/x2go/applications/`. This location however is not created by default and can be created by creating a symlink to `/usr/share/applications/`. 

Alternatively instead of creating a symlink one could also create a folder and link only the desired applications instead. See [[1]](<https://wiki.x2go.org/doku.php/wiki:advanced:published-applications>) for more information. 

###  启动 X2Go 服务器端守护进程

至此，只需[启动](<../zh-cn/Systemd.html> "Systemd") `x2goserver.service` 即可。 

##  客户端配置

运行 X2Go 客户端 
    
    $ x2goclient
    
**注意：** 确保你可以打开一个从客户端到服务器的 ssh 会话 `ssh _username@host_`

现在，你可以创建多个会话，它们将出现在 X2Go 客户端程序主窗口的右面并且可以用鼠标点击选中。每一项都是由你的用户名、主机名、IP 地址和 SSH 连接端口组成。你还可以进一步基于不同连接速度（从 modem 到 LAN）以及想要远程启动的不同桌面环境定义若干个配置文件。 

###  访问本地桌面

To access the local desktop, the one currently running on the server rather than a new one, one can choose the option "Connection to local desktop" in "session type" in the _X2Go Client_ as long as the users match, if it is user _foo_ accessing the session of user _foo_. 

无论如何，要访问本地不同用户的桌面，你需要安装 [x2godesktopsharing](<https://aur.archlinux.org/packages/x2godesktopsharing/>)AUR 并加载 `x2godesktopsharing`。 

###  客户端与服务器（桌面）交换数据

在 x2go 客户端（例如：笔记本电脑）上，本地目录可被共享。服务器端将通过 fuse 和 sshfs 访问这些目录并将其挂载到服务器端你的家目录下的若干子目录上。这样你就可以在服务器上访问你的笔记本电脑上的数据或者互传文件。也可以每次启动会话时自动挂载共享目录。 

###  临时离开一个会话

X2Go 的另一个特色功能就是可以挂起一个会话。这意味着你可以从一个客户端里离开某一个会话，然后用另一个客户端重新打开这个会话（即便是同一地点的另一个客户端）。这样你可以在局域网启动一个会话，随后在笔记本电脑上重新打开这个会话。在此期间，会话数据由一个 [SQLite](<../zh-cn/SQLite.html> "SQLite") 数据库存储和管理。会话的状态由一个名为 _x2gocleansessions_ 的进程来保持。 

##  排错

###  桌面环境不启动

####  本地会话阻止了 X2Go 的新会话

当本地已经有一个桌面会话在运行而 X2Go 尝试新建一个会话时失败。这是典型的 D-Bus 相关的问题，详情参阅 [[2]](<https://bugzilla.redhat.com/show_bug.cgi?id=1350004>)。 如果 D-Bus 启动失败，尝试用 _定制桌面_ 类型代替默认的会话类型。For the command, use the desktop starter as an option of `dbus-launch`, for example `dbus-launch startxfce4`. This is a way to launch a session bus instance, set the appropriate environment variables so that the new session can find the bus. 

####  路径问题

用 ssh 登录时，桌面环境的可执行程序（如 _startkde_ 、 _startgnome_ 或 _startxfce4_ 等）可能未包含在 `$PATH` 环境变量中。在此情况下，不要简单地选择默认的 KDE、Gnome 或 XFCE，而应使用桌面环境可执行程序的全路径，例如 `/usr/bin/startxfce4`。 也可以启动 [openbox](<../zh-cn/Openbox.html> "Openbox") 或其他窗口管理器，这会提示你输入服务器的用户名和口令，然后会看到 X2Go 图标一闪而过随后进入桌面。 

###  x2go 客户端中无选择屏幕

由于 [iproute2](<https://archlinux.org/packages/?name=iproute2>)包 的回退导致 _ss_ 指定了 `-u` 标记时不显示结果，as done in `/usr/bin/x2golistdesktops`。[[3]](<https://lore.kernel.org/netdev/553EE0D9.3050601@ionic.de/>)

详情参阅 [[4]](<https://bugs.x2go.org/cgi-bin/bugreport.cgi?bug=799>)，[[5]](<https://bbs.archlinux.org/viewtopic.php?pid=1541035>)。 

###  会话没有正常登出

由于[这个 bug](<https://bugs.x2go.org/cgi-bin/bugreport.cgi?bug=914>) 导致 X2Go 会话可能不能正常登出。X2Go 可能被会话初始化脚本输出的过量日志行搞懵了。一个简单的解决方法是定制一个会话脚本并且将日志输出重定向到某个文件或空文件`/dev/null`，然后指定把 X2Go 客户端应用程序指向这个定制脚本。 

以下是 XFCE 的一个定制脚本范例： 
    
    #!/bin/sh
    #
    #xfce4-session spits out quite a bit of text during logout, which I guess
    #confuses x2go so we would get a black screen and session hang.
    #adding redirect to a logfile like "~/logfile" or "/dev/null" nicely solved it
    # see <https://bugs.x2go.org/cgi-bin/bugreport.cgi?bug=914>
    /usr/bin/xfce4-session > /dev/null
    
###  通知区无显示

参照[#本地会话阻止了 X2Go 的新会话](<#%E6%9C%AC%E5%9C%B0%E4%BC%9A%E8%AF%9D%E9%98%BB%E6%AD%A2%E4%BA%86_X2Go_%E7%9A%84%E6%96%B0%E4%BC%9A%E8%AF%9D>)的解决方法。 

###  共享文件夹未挂载（Windows 客户端）

The ssh-daemon used by the X2go windows client uses depreceated ssh-dss keys by default and because Arch does not accept them your shared folders will not mount. Check out this [bug report](<https://bugs.x2go.org/cgi-bin/bugreport.cgi?bug=1009>) for more information. 

This can be solved on the windows side by generating different type of key: 
    
    C:\Program Files (x86)\x2goclient\ssh-keygen -b 2048 -t rsa
    
And simply replace `c:\Users\User\.x2go\etc\ssh_host_dsa_key` and `c:\Users\User\.x2go\etc\ssh_host_dsa_key.pub` with the newly generated key files. 

Other workarrounds from [[6]](<https://bugs.x2go.org/cgi-bin/bugreport.cgi?bug=1009>) might help, too. 

### Workaround for failing compositing window manager for remote session

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** 请提供模板的第一个位置参数以概括原因。（在[Talk:X2Go](<../zh-cn/Talk:X2Go.html>)讨论）

This is useful for situations, when the computer running x2goserver is used also for local sessions with e.g. compiz as the window manager. For remote connections with x2goclient, compiz fails to load and metacity should be used instead. The following is for GNOME, but could be modified for other desktop environments. (Getting compiz ready is not part of this how-to.) 

Create /usr/local/share/applications/gnome-wm-test.desktop: 
    
    [Desktop Entry]
    Type=Application
    Encoding=UTF-8
    Name=gnome-wm-test
    Exec=/usr/local/bin/gnome-wm-test.sh
    NoDisplay=true
    
Create script /usr/local/bin/gnome-wm-test.sh: 
    
    #!/bin/sh
    # Script for choosing compiz when possible, otherwise metacity
    # Proper way to use this script is to set the key to mk-gnome-wm
    # /desktop/gnome/session/required_components/windowmanager
    xdpyinfo 2> /dev/null | grep -q "^ *Composite$" 2> /dev/null
    IS_X_COMPOSITED=$?
    if [ $IS_X_COMPOSITED -eq 0 ] ; then
        gtk-window-decorator &
        WM="compiz ccp --indirect-rendering --sm-client-id $DESKTOP_AUTOSTART_ID"
    else
        WM="metacity --sm-client-id=$DESKTOP_AUTOSTART_ID"
    fi
    exec bash -c "$WM"
    
Modify the following gconf key to start the session with gnome-wm-test window manager: 
    
    $ gconftool-2 --type string --set /desktop/gnome/session/required_components/windowmanager "gnome-wm-test"
    
###  /bin/bash: No such file or directory when connect (or what ever shell you use)

In you ssh configuration, if you chroot a user, this user need to have his own /bin directory inside his chrooted directory. If not, you will not be able to connect. 

##  参阅

  * [Screenshot KDE 会话截屏](<https://wiki.archlinux.de/?title=Bild:X2go-1.png>)
  * [Screenshot 配置对话框截屏](<https://wiki.archlinux.de/?title=Bild:X2go-2.png>)
