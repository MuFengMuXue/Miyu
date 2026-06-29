**翻译状态：**

  * 本文（或部分内容）译自 [Universal Wayland Session Manager](<https://wiki.archlinux.org/title/Universal_Wayland_Session_Manager> "arch:Universal Wayland Session Manager")，最近一次同步于 2025-10-02，若英文版本有所[更改](<https://wiki.archlinux.org/title/Universal_Wayland_Session_Manager?diff=0&oldid=847910>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Universal_Wayland_Session_Manager_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[通用Wayland会话管理器](<https://github.com/Vladimir-csp/uwsm>) (**uwsm**) 运行时会将独立 [Wayland混成器](<../zh-cn/Wayland.html#%E6%B7%B7%E6%88%90%E5%99%A8> "Wayland")变成一组[systemd](<../zh-cn/Systemd.html> "Systemd") 单元。这提供一个包括环境的稳定的会话管理，并且支持[XDG Autostart](<../zh-cn/XDG_Autostart.html> "XDG Autostart")，与登录会话双向连接，并且可以完全关闭。 

**注意：** 强烈建议使用[dbus-broker](<../zh-cn/D-Bus.html#dbus-broker> "Dbus")作为D-Bus守护进程的实现。因为它会重复利用systemd激活环境，而不是启动一个独立的环境。这个简化的环境管理可以有恰当的清理，也支持[reference implementation](<../zh-cn/D-Bus.html#Reference_implementation> "D-Bus")，但是不允许取消设置一个变量，所以更高效的清理方式是将其设置为空字符。唯一可能的清理办法是使用`loginctl terminate-user ""`来将D-Bus守护进程引用的环境分离

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [uwsm](<https://archlinux.org/packages/?name=uwsm>)包（或者你也可以安装[uwsm-git](<https://aur.archlinux.org/packages/uwsm-git/>)AUR的Git版本以获取`master`分支上的最新提交） 

##  配置

###  服务启动通知和混成器设置的变量

**注意：** 如果被管理的混成器已经将 `WAYLAND_DISPLAY`（和其他有用的环境变量）添加到 systemd 激活的环境中，那么你可以跳过这部分，并且无需使用 `uwsm finalize`。

为了找到当前的混成器，一个Wayland软件作为systemd服务运行需要 `WAYLAND_DISPLAY` 环境变量（如果它们预期是在[Xwayland](<../zh-cn/Wayland.html#Xwayland> "Xwayland")中运行则是 `DISPLAY`）。因此，一旦混成器设置了这个和其他有用的环境变量，都应该被放进 systemd/dbus 激活环境中。 

`uwsm finalize` 命令会根据 `UWSM_FINALIZE_VARNAMES` 列表（使用空白字符 (white-space) 作为分隔符），将 `WAYLAND_DISPLAY`、`DISPLAY` 和其他环境变量加入到激活环境。建议在混成器就绪后执行该命令。 

如果在激活环境中需要其他由混成器设置的变量，可以将变量名称作为参数传递给 `uwsm finalize` 或将其放入 `UWSM_FINALIZE_VARNAMES` 中的使用空白字符分隔的列表中。例如： 
    
    exec uwsm finalize _VAR1 VAR2 ..._
    export UWSM_FINALIZE_VARNAMES=_VAR1 VAR2 ..._
    
###  环境变量

所有来源于 _uwsm_ 的环境变量都设置在`${XDG_CONFIG_HOME}/uwsm/env`并且可用于在这个会话中所有的被管理混成器和图形化软件。 

如果你想仅仅为一个指定的 _混成器_ （以及对应图形会话中的图形应用程序）设置一些环境变量，那么请将变量放在`${XDG_CONFIG_HOME}/uwsm/env-_compositor_`

这个文件的模板如下： 
    
    ~/.config/uwsm/env
    
    export _KEY1_ =_VAR1_
    export _KEY2_ =_VAR2_
    export _KEY3_ =_VAR3_
    _..._

##  使用

###  启动

**注意：** 如果在`uwsm start`中的环境变量被成功使用，那么环境预加载器不再生效POSIX shell配置。

_uwsm_ 可以从TTY或者[显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")启动。 

####  从TTY启动

将如下代码添加进`~/.profile`： 
    
    if uwsm check may-start && uwsm select; then
      exec uwsm start default
    fi

如果你想始终启动指定 _混成器_ ，将上述代码替换为： 
    
    if uwsm check may-start; then
      exec uwsm start _compositor_.desktop
    fi

####  从显示管理器中启动

你可以创建一个自定义[桌面项](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html> "桌面项")以通过 _uwsm_ 启动你的混成器： 
    
    /usr/share/wayland-sessions/my-compositor-uwsm.desktop
    
    [Desktop Entry]
    Name=My compositor (with UWSM)
    Comment=My cool compositor, UWSM session
    
    # either full command line with metadata and executable
    Exec=uwsm start -N "My compositor" -D mycompositor:mylib -C "My cool compositor" -- my-compositor
    
    # or a reference to another entry
    Exec=uwsm start -- my-compositor.desktop
    
    DesktopNames=mycompositor;mylib
    Type=Application

###  终止会话

如果你想终止当前 _uwsm_ 会话，那么你可以使用`loginctl terminate-user ""`（关闭整个用户会话）或`uwsm stop`（如果uwsm取代了[登录shell](<../zh-cn/%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%A7%A3%E9%87%8A%E5%99%A8.html#%E7%99%BB%E5%BD%95_Shell> "命令行解释器")，那么它会在`uwsm start`后启动代码或终止用户会话） 

**注意：** 请不要使用混成器的原生退出机制或者直接杀死其进程。这将会使混成器从所有客户端之下强制抽除，并干扰有序的单元停用流程。

##  技巧提示

###  软件与自动启动

默认情况下，uwsm 通过在`session.slice`中的一个自定义systemd服务来启动混成器。很多Wayland混成器允许你在混成器服务中启动其他软件，然而这将会消耗混成器资源，甚至会干扰通知sockets 

要将应用程序作为独立的 systemd 范围单元 (scope units) 启动，你可以使用 `uwsm app`，它既可以启动可执行文件： 
    
    uwsm app -- _/my/program/path_
    
也可以启动[桌面项](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html> "桌面项")： 
    
    uwsm app -- _myprogram_.desktop
    
uwsm 默认会将启动的范围单元放置在 `app-graphical.slice`。如果你想要将它们放置在 `background-graphical.slice` 或 `session-graphical.slice`，应该分别使用 `-s b` 和 `-s s`： 
    
    uwsm app -s b -- _background-app_.desktop
    
####  替代

你可以使用以下方案作为替代，比起`uwsm app`（运行一个Python脚本）会更快： 

  * uwsm 的 `uwsm-app` 脚本，与 uwsm 的应用守护进程进行通信。
  * [app2unit-git](<https://aur.archlinux.org/packages/app2unit-git/>)AUR，一个shell脚本。你可以通过设置`APP2UNIT_SLICES`环境变量为如下值来让它作为`uwsm app`的替代方案：
        
        APP2UNIT_SLICES='a=app-graphical.slice b=background-graphical.slice s=session-graphical.slice'

  * [runapp](<https://aur.archlinux.org/packages/runapp/>)AUR，由C++编写，但是少了些许功能。

##  另见

  * [uwsm(1)](<https://man.archlinux.org/man/uwsm.1>)
