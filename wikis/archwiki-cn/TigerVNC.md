**翻译状态：**

  * 本文（或部分内容）译自 [TigerVNC](<https://wiki.archlinux.org/title/TigerVNC> "arch:TigerVNC")，最近一次同步于 2021-06-13，若英文版本有所[更改](<https://wiki.archlinux.org/title/TigerVNC?diff=0&oldid=669441>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/TigerVNC_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [x11vnc](<../zh-cn/X11vnc.html> "X11vnc")

[TigerVNC](<https://tigervnc.org/>) 是 [Virtual Network Computing](<https://en.wikipedia.org/wiki/Virtual_Network_Computing> "wikipedia:Virtual Network Computing") (VNC) 协议的一种实现。本文着重介绍服务端的功能。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [tigervnc](<https://archlinux.org/packages/?name=tigervnc>)包 软件包。 

##  为虚拟（无界面）会话运行 vncserver

###  初始设置

**注意：** 在内存允许的条件下，Linux 系统可以启动任意数量的 VNC 服务端，它们同时并行运行，互不干扰。

简易教程如下。推荐用户阅读 vncserver 的 man 手册来了解所有的配置项。 

  1. 用 `vncpasswd` 创建密码，它会将哈希处理之后的密码存储在 `$XDG_CONFIG_HOME/tigervnc/config`。
  2. 编辑 `/etc/tigervnc/vncserver.users` 来定义用户映射。该文件中定义的每个用户都会拥有对应的端口来运行会话。该文件中的数字对应的是 TCP 端口。默认情况下，:1 是 TCP 端口 5901 (5900+1)。如果需要运行一个并行的服务端，第二个实例可以运行在下一个最大的、未被占用的端口，即 5902 (5900+2)。
  3. 创建 `$XDG_CONFIG_HOME/tigervnc/config`，其中至少要有一行定义会话的类型，比如 `session=foo` （将foo替换为你想要运行的桌面环境）。你可以通过查看 `/usr/share/xsessions/` 里的 `.desktop` 文件来知道有哪些桌面环境在当前系统上可以使用。

文件内容举例： 
    
    $XDG_CONFIG_HOME/tigervnc/config
    
    session=lxqt
    geometry=1920x1080
    localhost
    alwaysshared

###  启动与停止 tigervnc

[start](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") `vncserver@.service`，如果需要让它随系统启动，[enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") 它。注意 `/etc/tigervnc/vncserver.users` 中定义的编号需要在@符号后面指定，比如启动:1的命令是： 
    
    # systemctl start vncserver@:1
    
**注意：** 已经不再支持直接调用 `/usr/bin/vncserver` 了，因为这样做不会建立完整可用的会话环境。systemd 服务是唯一受支持的使用 TigerVNC 的方式。参见 [Issue #1096](<https://github.com/TigerVNC/tigervnc/issues/1096>)。

##  直接转发本地显示内容

Tigervnc 带有 libvnc.so，它可以在 X 初始化过程中直接加载，以提供更好的性能。 创建如下文件并重启 X： 
    
    /etc/X11/xorg.conf.d/10-vnc.conf
    
    Section "Module"
    Load "vnc"
    EndSection
    
    Section "Screen"
    Identifier "Screen0"
    Option "UserPasswdVerifier" "VncAuth"
    Option "PasswordFile" "/root/.vnc/passwd"
    EndSection

##  运行 x0vncserver 来直接控制本地显示内容

[tigervnc](<https://archlinux.org/packages/?name=tigervnc>)包 同时也提供 `x0vncserver`，允许直接控制物理 X 会话。在使用 _vncpasswd_ 定义了会话密码后，请这样启动服务端： 
    
    $ x0vncserver -rfbauth ~/.vnc/passwd
    
更多信息请参阅 [x0vncserver(1)](<https://man.archlinux.org/man/x0vncserver.1>)。 

**注意：**

  * [x11vnc](<../zh-cn/X11vnc.html> "X11vnc") 是另一个可以直接控制当前 X 会话的 VNC 服务端。
  * `x0vncserver` 目前不支持客户端和服务端之间的剪贴板共享（即使有 `autocutsel` 支持也不行）。参阅 [Issue #529](<https://github.com/TigerVNC/tigervnc/issues/529>)。

###  从 xprofile 启动 x0vncserver

一种启动 _x0vncserver_ 的简单方法是在某个 [xprofile](<../zh-cn/Xprofile.html> "Xprofile") 文件中添加如下行： 
    
    ~/.xprofile
    
    ...
    x0vncserver -rfbauth ~/.vnc/passwd &

###  通过 systemd 启动与停止 x0vncserver

####  通过系统服务启动

该选项允许用户访问当前显示界面，包括由显示管理器提供的登录界面。 

该服务将在用户退出会话后自动重新启动。 

下面的例子使用了LightDM，但可以通过修改 `XAUTHORITY` 变量来将其适用于其他显示管理器。 
    
    /etc/systemd/system/x0vncserver.service
    
    [Unit]
    Description=Remote desktop service (VNC) for :0 display
    Requires=display-manager.service
    After=network-online.target
    After=display-manager.service
    
    [Service]
    Type=simple
    Environment=HOME=/root
    Environment=XAUTHORITY=/var/run/lightdm/root/:0
    ExecStart=x0vncserver -display :0 -rfbauth $XDG_CONFIG_HOME/tigervnc/passwd
    Restart=on-failure
    RestartSec=500ms
    
    [Install]
    WantedBy=multi-user.target
    
这是一个 system unit, `-rfbauth $XDG_CONFIG_HOME/tigervnc/passwd` 指向 `/root/.vnc/passwd`

Start/enable `x0vncserver.service`. 

####  通过用户服务启动

对大多数用户来说，快速远程访问当前桌面的最简单方法是运行 _x0vncserver_ 来得到一个 VNC 服务器。为此可以创建一个 systemd unit，将其中的用户和选项替换为实际值： 
    
    ~/.config/systemd/user/x0vncserver.service
    
    [Unit]
    Description=Remote desktop service (VNC)
    
    [Service]
    Type=simple
    # wait for Xorg started by ${USER}
    ExecStartPre=/bin/sh -c 'while ! pgrep -U "$USER" Xorg; do sleep 2; done'
    ExecStart=/usr/bin/x0vncserver -rfbauth %h/.vnc/passwd
    # or login with your username & password
    #ExecStart=/usr/bin/x0vncserver -PAMService=login -PlainUsers=${USER} -SecurityTypes=TLSPlain
    
    [Install]
    WantedBy=default.target

在 [systemd用户服务](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "Systemd/用户")模式下 [start](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") 并 [enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") `x0vncserver.service` 服务，也就是带上 `--user` 参数。 

##  使用 XDMCP 为需要的会话运行 Xvnc

可以让 _systemd_ socket activation 与 [XDMCP](</wzh/index.php?title=XDMCP&action=edit&redlink=1> "XDMCP（页面不存在）") 结合使用，为每个想登录的用户自动生成 VNC 服务器，这样无需为每个用户都准备服务器或端口。这种方法使用显示管理器来验证用户和登录，所以也不需要设置 VNC 密码。这种方法的缺点是会话无法在服务器上保持运行，退出后无法重新连接到它。 

该方法首先需要设置 [XDMCP](</wzh/index.php?title=XDMCP&action=edit&redlink=1> "XDMCP（页面不存在）")，并确保显示管理器正在运行。 然后创建： 
    
    /etc/systemd/system/xvnc.socket
    
    [Unit]
    Description=XVNC Server
    
    [Socket]
    ListenStream=5900
    Accept=yes
    
    [Install]
    WantedBy=sockets.target
    
    /etc/systemd/system/xvnc@.service
    
    [Unit]
    Description=XVNC Per-Connection Daemon
    
    [Service]
    ExecStart=-/usr/bin/Xvnc -inetd -query localhost -geometry 1920x1080 -once -SecurityTypes=None
    User=nobody
    StandardInput=socket
    StandardError=syslog

使用 systemctl 来 [start](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") 并 [enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") `xvnc.socket`。现在多个用户同时连接到 5900 端口，均可获得单独的桌面。 

如果 VNC 服务器直接暴露在公网，请在 `xvnc@.service` 里给 `Xvnc` 添加 `-localhost` 选项（注意 `-query localhost` 和 `-localhost` 是不同的开关），然后遵循 [#通过 SSH 隧道连接到 vncserver](<#%E9%80%9A%E8%BF%87_SSH_%E9%9A%A7%E9%81%93%E8%BF%9E%E6%8E%A5%E5%88%B0_vncserver>)。由于我们只在连接后才选择用户，所以 VNC 服务端以 _nobody_ 用户运行，且直接使用了 `Xvnc` 而不是 `vncserver` 脚本，所以忽略了 `~/.vnc` 中的选项。或者也可以[自动启动](<../zh-cn/%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8.html> "Autostart") _vncconfig_ 来打开剪贴板共享（在非 VNC 会话中 _vncconfig_ 将立即退出）。一种自动启动的方法是创建： 
    
    /etc/X11/xinit/xinitrc.d/99-vncconfig.sh
    
    #!/bin/sh
    vncconfig -nowin &

##  连接到 vncserver

**警告：** TigerVNC 默认的连接方式不安全，它缺乏身份验证，且在连接建立过程中无法防止中间人攻击。请确保知晓当前服务器的安全设置，并且不要以不安全的方式连接到可信网络之外的 vncserver。

**注意：** TigerVNC 默认使用 _TLSVnc_ 作为验证和加密方式，也可以用 `SecurityTypes` 参数来改成其他方式。 _TLSVnc_ 意味着标准的 VNC 身份验证，使用 GNUTLS 加密流量，但不会验证服务器的身份。TigerVNC 支持更换其他安全方案，如 _X509Vnc_ ，它结合了标准 VNC 身份验证、GNUTLS 加密、服务器身份识别，推荐将它用于安全连接。 如果服务器上的 `SecurityTypes` 设置了非加密方式（如 _None_ , _VncAuth_ , _Plain_ , _TLSNone_ , _TLSPlain_ , _X509None_ , _X509Plain_ ）为高优先级，这样无法使用加密，是不明智的。运行 _vncviewer_ 时，更安全的方式是明确指定 `SecurityTypes` 且不接受未加密的流量。其他的模式仅在 [#通过 SSH 隧道连接到 vncserver](<#%E9%80%9A%E8%BF%87_SSH_%E9%9A%A7%E9%81%93%E8%BF%9E%E6%8E%A5%E5%88%B0_vncserver>) 时使用。

连接到 vncserver 的客户端不限数量。下面是一个简单的例子，其中 vncserver 运行在 10.1.10.2 的 5901 端口上，端口可以用缩写 :1 来表示： 
    
    $ vncviewer 10.1.10.2:1
    
###  无密码验证

`-passwd` 开关允许我们定义服务器上 `~/.vnc/passwd` 文件的位置。用户在服务器上必须有权访问该文件，可以是通过 [SSH](<../zh-cn/Secure_Shell.html> "Secure Shell") 访问，也可以是实体访问。两种情况下都应将该文件放在客户端文件系统的一个安全位置，比如一个仅给期望用户以读取权限的位置。 
    
    $ vncviewer -passwd _/path/to/server-passwd-file_
    
直接提供密码也是可以的。 

**注意：** 下方的密码输入方式是不安全的，本机上任何可以运行 `ps` 的人都可以看到密码。
    
    $ vncviewer -passwd <(echo MYPASSWORD | vncpasswd -f)
    
###  图形界面客户端示例

  * [gtk-vnc](<https://archlinux.org/packages/?name=gtk-vnc>)包
  * [krdc](<https://archlinux.org/packages/?name=krdc>)包
  * [vinagre](<https://archlinux.org/packages/?name=vinagre>)包
  * [remmina](<../zh-cn/Remmina.html> "Remmina")
  * [virt-viewer](<https://archlinux.org/packages/?name=virt-viewer>)包
  * [vncviewer-jar](<https://aur.archlinux.org/packages/vncviewer-jar/>)AUR

TigerVNC 的 vncviewer 也带有一个简单的图形界面，不带参数运行即可： 
    
    $ vncviewer
    
##  通过 SSH 隧道连接到 vncserver

对于提供 SSH 的服务器来说，这种方法有一个优点，除了已经打开的 SSH 端口外不需要再打开其他端口，因为 VNC 流量是在 SSH 隧道中传输的。 

###  服务端配置

服务端必须运行 _vncserver_ 或 _x0vncserver_ 。 

无论运行哪个服务端，都建议在 `~/.vnc/config` 添加 `localhost` 选项或使用 `-localhost` 开关（适用于 _x0vncserver_ ），只允许来自 localhost 的连接，这样可以确保连接都来自于 ssh 或实体机上认证过的用户。例如： 
    
    ~/.vnc/config
    
    session=lxqt
    geometry=1920x1080
    localhost
    alwaysshared

确保已经 [start](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") 或 [restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `vncserver@.service`。例如（参见 [#初始设置](<#%E5%88%9D%E5%A7%8B%E8%AE%BE%E7%BD%AE>)）： 
    
    # systemctl start vncserver@:1
    
对于 _x0vncserver_ 则是： 
    
    $ x0vncserver **-localhost** -SecurityTypes none
    
###  客户端配置

远程计算机上的 VNC 服务端已被设置为仅接受本地连接。 现在，客户端必须与远程计算机（本例中为 10.1.10.2）建立 SSH 连接，并在客户端的某个端口（如 9901）和服务器的 5901 端口之间建立隧道。关于该功能的详细信息，参见 [OpenSSH#Forwarding other ports](<../zh-cn/OpenSSH.html#Forwarding_other_ports> "OpenSSH") 和 [ssh(1)](<https://man.archlinux.org/man/ssh.1>)。 
    
    $ ssh 10.1.10.2 -L 9901:localhost:5901
    
当通过 SSH 建立连接后，请保持该 shell 窗口打开，它现在是与服务器之间的安全隧道。或者也可以使用 `-f` 选项直接在后台运行 SSH。客户端要想通过这一加密隧道连接到服务端，请指定 _vncviewer_ 连接到客户端 localhost 上的转发端口。 
    
    $ vncviewer localhost:9901
    
实际上就是 vncviewer 连接到了本地的 9901 端口，而该端口映射到了服务器本地的 5901 端口。通过 SSH，向正确的端口建立了连接。 

**提示：** 只用一行命令即可实现在连接期间保持端口转发，在连接关闭后立即关闭转发： 
    
    $ ssh -fL 9901:localhost:5901 10.1.10.2 sleep 10; vncviewer localhost:9901

上述命令中 `-f` 选项使 ssh 在后台运行，它将因为 `sleep 10` 而保持运行。接着运行 vncviewer，在 vncviewer 使用隧道期间，ssh 在后台继续运行。当隧道不再使用，ssh 将关闭，这正是我们所需要的行为。 

另外，vncviewer 的 `-via` 选项提供了上述命令的快捷方式： 
    
    $ vncviewer -via 10.1.10.2 localhost::5901

（注意双冒号：vncviewer 的语法是 `[host]:[display#]` 或 `[host]::[port]`。） 

###  从 Android 设备通过 SSH 连接到 vncserver

为了用 Android 设备作为客户端，通过 SSH 连接到 VNC 服务端，可以进行以下设置： 

  1. 服务器运行 SSH
  2. 服务器运行 vncserver（带有 `-localhost` 标志以确保安全）
  3. Android 设备上的 SSH 客户端： _ConnectBot_ 是一个流行的选择，本例中将使用它
  4. Android 设备上的 VNC 客户端：此处采用 _androidVNC_

在 _ConnectBot_ 中连接到目标主机。轻点 options 按钮，选择 _Port Forwards_ 并添加一个端口： 
    
    Type: Local
    Source port: 5901
    Destination: 127.0.0.1:5901
    
在 _androidVNC_ 中连接到 VNC 端口，即 SSH 连接中设置的本地端口： 
    
    Password: the vncserver password
    Address: 127.0.0.1
    Port: 5901
    
##  提示和技巧

###  连接到 OS X 系统

参见 <https://help.ubuntu.com/community/AppleRemoteDesktop> 。 已在 Remmina 上测试。 

###  推荐的安全设置

[#通过 SSH 隧道连接到 vncserver](<#%E9%80%9A%E8%BF%87_SSH_%E9%9A%A7%E9%81%93%E8%BF%9E%E6%8E%A5%E5%88%B0_vncserver>) 中，SSH 处理身份验证和加密，如果没有采用该方法，则建议用 _X509Vnc_ ，因为 _TLSVnc_ 缺乏身份验证。 
    
    $ vncserver -x509key _/path/to/key.pem_ -x509cert _/path/to/cert.pem_ -SecurityTypes X509Vnc :1
    
颁发 x509 证书超出了本指南的范围，而 [Let's Encrypt](<https://en.wikipedia.org/wiki/Let%27s_Encrypt> "wikipedia:Let's Encrypt") 提供了一种简便方法。也可以使用 [OpenSSL](<../zh-cn/OpenSSL.html> "OpenSSL") 来颁发证书，然后与客户端共享公钥并使用 `-X509CA` 参数指定证书。下面是一个示例（服务器运行在 10.1.10.2 上）： 
    
    $ vncviewer 10.1.10.2 -X509CA _/path/to/cert.pem_
    
###  切换全屏

从 VNC 客户端的菜单可以切换全屏。默认快捷键是 `F8`。 

###  鼠标后退和前进按钮失效的解决方法

VNC 协议目前只支持 7 个鼠标按钮（左、中、右、向上滚动、向下滚动、向左滚动、向右滚动），如果鼠标有后退和前进按钮，这些按钮无法使用，按钮的输入将被忽略。 

在单击鼠标后退/前进按钮时，[evrouter](<https://www.bedroomlan.org/projects/evrouter/>) 将其改为键盘按键发送，可以解决此限制。如果需要，可以在服务器上使用 [xautomation](<https://archlinux.org/packages/?name=xautomation>)包 和 [xbindkeys](<https://archlinux.org/packages/?name=xbindkeys>)包 中的 xte 将键盘按键映射回鼠标单击。 

####  用键盘 XF86Back/XF86Forward 按键代替鼠标后退/前进按钮

如果只需要在用 Web 浏览器或文件浏览器时后退/前进，则此方法既简单又合适。 

客户端安装 [evrouter](<https://aur.archlinux.org/packages/evrouter/>)AUR 和 [xautomation](<https://archlinux.org/packages/?name=xautomation>)包。配置 evrouter，想知道如何查找设备名称、窗口名称、按钮名称等，请参阅 [Mouse buttons#evrouter](<../zh-cn/Mouse_buttons.html#evrouter> "Mouse buttons") 和 evrouter 手册页。以下是示例配置： 
    
    ~/.evrouterrc
    
    Window "OtherComputer:0 - TigerVNC": # 筛选窗口标题
    
    # 使用 Shell 防止重复按键（参见 evrouter 手册）
    "USB mouse" "/dev/input/by-id/usb-Mouse-name-event-mouse" none key/275 "Shell/xte 'key XF86Back'"
    "USB mosue" "/dev/input/by-id/usb-Mouse-name-event-mouse" none key/276 "Shell/xte 'key XF86Forward'"
    
    # 如果需要重复按键，请使用下面的 XKey（参见 evrouter 手册）
    #"Logitech Gaming Mouse G400" "/dev/input/by-id/usb-Logitech_Gaming_Mouse_G400-event-mouse" none key/275 "XKey/XF86Back"
    #"Logitech Gaming Mouse G400" "/dev/input/by-id/usb-Logitech_Gaming_Mouse_G400-event-mouse" none key/276 "XKey/XF86Forward"

客户端启动 evrouter。按照上面的配置，点击鼠标后退按钮时，向 VNC 服务器发送键盘按键 XF86Back，点击前进按钮时发送 XF86Forward。 

####  在服务端将键盘按键映射回的鼠标点击

必要时可以在服务端将键盘按键映射回鼠标点击。此时最好使用客户端或服务端都不使用的按键值。下面的例子将按键值 XF86Launch8/XF86Launch9 用作鼠标按钮 8/9。 

客户端上的 evrouter 配置： 
    
    ~/.evrouterrc
    
    Window "OtherComputer:0 - TigerVNC": # 窗口标题
    
    # 使用 Shell 防止重复按键（参见 evrouter 手册）
    "USB mouse" "/dev/input/by-id/usb-Mouse-name-event-mouse" none key/275 "Shell/xte 'key XF86Launch8'"
    "USB mosue" "/dev/input/by-id/usb-Mouse-name-event-mouse" none key/276 "Shell/xte 'key XF86Launch9'"

服务端安装 [xautomation](<https://archlinux.org/packages/?name=xautomation>)包 和 [xbindkeys](<https://archlinux.org/packages/?name=xbindkeys>)包。配置 xbindkeys，配置中使用 xte 将键盘按键 XF86Launch8/XF86Launch9 映射到鼠标按钮 8/9。 
    
    ~/.xbindkeysrc
    
    "xte 'mouseclick 8'"
         XF86Launch8
    
    "xte 'mouseclick 9'"
         XF86Launch9
    
启用 xbindkeys `$ xbindkeys -f ~/.xbindkeysrc`。服务端将 XF86Launch8/XF86Launch9 映射为鼠标按钮 8/9。 

##  疑难解答

###  vncserver 内的终端起始于 / （根目录）

这是上游引入的已知问题。参阅：<https://github.com/TigerVNC/tigervnc/issues/1108>

###  无法输入 '<' 符号

如果在客户端上按下 `<` 却发送了 `>` 字符，请尝试重新映射键盘 [[1]](<https://insaner.com/blog/2013/05.html#20130422063137>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2020-04-03 ⓘ]： 
    
    $ x0vncserver -RemapKeys="0x3c->0x2c"
    
###  窗口显示为黑色方框

这种情况很可能是应用程序依赖于 Xorg 的 Composite 扩展。如基于 webkit 的应用程序：midori、psi-plus 等。 

这种情况下使用下列命令重启 vncserver： 
    
    $ vncserver -geometry ... -depth 24 :1 +extension Composite
    
VNC 下的 Composite 扩展仅在 24 位色深时才能正常工作。 

###  没有鼠标指针

当使用 `x0vncserver` 时没有可见的鼠标指针，请使用下列命令启动 vncviewer： 
    
    $ vncviewer DotWhenNoCursor=1 <server>
    
或者将 `DotWhenNoCursor=1` 写入 tigervnc 配置文件，配置文件默认存放在 `~/.vnc/default.tigervnc`。 

###  从远程主机复制剪贴板内容

如果无法从远程主机复制到本地，请在服务端运行 `autocutsel`，如 [[2]](<https://bbs.archlinux.org/viewtopic.php?id=101243>) 中所述： 
    
    $ autocutsel -fork
    
然后按下 F8 打开 VNC 菜单，选择 `Clipboard: local -> remote` 选项。 

###  启动 GNOME 3 时显示 "Authentication is required to create a color managed device" 对话框

一种解决方法是创建一个 "vnc" 组，将 gdm 用户和其他使用 vnc 的用户添加到该组。按如下方式 [[3]](<https://github.com/TurboVNC/turbovnc/issues/47>) 修改 `/etc/polkit-1/rules.d/gnome-vnc.rules`： 
    
       polkit.addRule(function(action, subject) {
          if ((action.id == "org.freedesktop.color-manager.create-device" ||
               action.id == "org.freedesktop.color-manager.create-profile" ||
               action.id == "org.freedesktop.color-manager.delete-device" ||
               action.id == "org.freedesktop.color-manager.delete-profile" ||
               action.id == "org.freedesktop.color-manager.modify-device" ||
               action.id == "org.freedesktop.color-manager.modify-profile") &&
              subject.isInGroup("vnc")) {
             return polkit.Result.YES;
          }
       });
    
###  没有窗口装饰/边框/标题栏/无法移动窗口

启动一个窗口管理器来修复一个空的 xterm frame。例如在 xfce 上，可在终端中运行 `xfwm4 &`。 

###  按用户运行 systemd service unit
    
    $ sudoedit /usr/lib/systemd/system/tigervnc@.service
    
    [Unit]
    Description=Remote desktop service (VNC)
    After=syslog.target network.target
    
    [Service]
    Type=simple
    ExecStart=/sbin/runuser -l USERNAME -c "/usr/bin/vncserver %i"
       
    [Install]
    WantedBy=multi-user.target
    
假设在 display 9 上启动服务： 
    
    $ sudo systemctl start tigervnc@:9
    
在启动时运行： 
    
    $ sudo systemctl enable tigervnc@:9
    
##  另外参见

  * <https://github.com/TigerVNC/tigervnc>
